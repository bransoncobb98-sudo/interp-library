# Classification request: batch 12 of 53 (40 records, IC-0841 to IC-0880)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-012-reply.json`.

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

## IC-0841: The Marriage Counselor

- Title: The Marriage Counselor
- Author (byline): Joey Ouellette
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: April 1999
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TIGER, SUSAN
- Teaser before the introduction: Yes
- Spoken words (computed): 2203
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joey Ouellette
ISBN: 978-0573626708
Publisher: Samuel French, Inc.
Date (Month/Year): April 1999
```

### Introduction (context only: never use it for content warnings)

```text
Actor 1: The Marriage Counselor Actor 2: by Joey Ouellette
```

### Performance text (classify this)

```text
NOTE: Throughout this selection, the judge serves as the silent “marriage counselor”

TIGER: (to audience) She is impossible, totally, totally impossible. I can't stand living with her for another hour, another minute. I'm losing my hair I'm so upset. It's coming out in big hunks. I'm getting constipated. And it's all her fault.

SUSAN: (to audience) I can't take any more of this. He is an insensitive, self-centered jerk. I've tried, believe me, I've tried, my mother says don't give up, don't give up, but of course she's already divorced. I've had enough. I have. It's all his fault.

TIGER and SUSAN: (Together.) See what I mean?

TIGER: She shaves her legs with my razor, my razor, the one I use on my face!

SUSAN: He shaves his face with my razor, my razor, the one I use on my legs!

TIGER and SUSAN: (Together.) It's unsanitary.

TIGER: She leaves her dirty underwear all over the house!

SUSAN: He clips his fingernails in the living room!

TIGER: She eats potato chips in bed. And she won't share.

SUSAN: That's because you're getting fat.

TIGER: Me? I'm getting fat?

SUSAN: I'm glad you agree.

TIGER and SUSAN: (Together.) TIGER: Do you see? Do you see? SUSAN: He is totally unreasonable!

SUSAN: Maybe we should try to speak one at a time.

TIGER: Nana na na na na na.

SUSAN: Don't be such a child.

TIGER: Don't be such a . . . virus.

SUSAN: Virus? I'm a virus?

TIGER: Look, do you want to do this, or what? I could just walk out of here! You wanted to come to a marriage counselor, I agreed, as usual I gave in-

SUSAN: (Interrupts.) Ho ho ho! You gave in! You never give in! Your stubbornness is the cause of every problem we have.

TIGER: My stubbornness? I'm stubborn?

SUSAN: I'm glad you finally admit it. . . . It's not my fault you're not as smart as I am.

TIGER: Oh, I am, I am. It's just that you're cold and I'm sensitive.

SUSAN: You mean stupid.

TIGER: No, I mean sensitive.

SUSAN: No, you mean sensitive.

TIGER: No, I mean stupid. You're the sensitive one. I'm the stupid one. (TIGER realizes what he's said. SUSAN smiles at him.)

SUSAN: Why don't we start at the beginning?

TIGER: We don't have time to start at the beginning. We're paying this bozo, aren't we?

(To the “Judge”.) Sorry.

SUSAN: Two hundred dollars an hour.

TIGER: I take that sorry back.

SUSAN: I'll go first.

TIGER: I'll go first.

SUSAN: We've never-

TIGER: (Continuing.) Been to a marriage counselor

SUSAN: (Continuing.) Before- TIGER (Continuing.) But-

SUSAN: (Continuing.) We thought we should try it.

TIGER: We've tried everything else.

SUSAN: We really have. . . . Self-help books.

TIGER: Acupuncture.

SUSAN: Talking to friends.

TIGER: Hypnosis.

SUSAN: Talking to psychics.

TIGER: Prostitutes. (Silence.) Did I say prostitutes? I meant to say Protestants. Protestants. Talking to Protestants.

SUSAN: Relatives.

TIGER: Talking to Catholics.

SUSAN: Clergymen.

TIGER: Going to the houses of Jehovah's Witnesses.

SUSAN: Lawyers. (Silence.) Did I say lawyers?

TIGER: I, I think you did. Have you been to a lawyer?

SUSAN: Have you been to a prostitute?

TIGER: Don't be silly! What would I go to a prostitute for? I mean I know what I go to a prostitute for, I mean, I haven't been to one, but I've seen pictures. I mean I haven't seen pictures, I just heard about it from a friend of mine, who I haven't seen in seventeen years, and I haven't had any contact with since. It was before I even met you. Have you been to a lawyer?

SUSAN: Yes.

TIGER: (Screaming.) Ahhhh!

SUSAN: Maybe we should start at the beginning.

TIGER: All the way back to the beginning? At four dollars a minute? This is more expensive than phone sex. Not that I've ever done it. I had a friend, I haven't spoken to him in years, he used to do, and no I didn't watch. He just told me about it. Not on the phone. It was seventeen years ago, before I even met you.

SUSAN: So that's what those calls on the phone bill were.

TIGER: What calls?

SUSAN: All those thirty second ones.

TIGER: I have no idea what you're talking about.

SUSAN: (To the “Judge”.) Are we hopeless? What do you think?

TIGER: I think I want to go home.

SUSAN: After we fought all day, after we fought all the way here in the car, and all through our nice lunch, you want to just walk home and waste all that we've accomplished today?

TIGER: Did you say walk home?

SUSAN: We're finally here, at a marriage counselor's. We've been talking about coming since our honeymoon.

TIGER: You did say walk home, didn't you? Don't deny it now!

SUSAN: I took the car keys out of your pocket in the elevator on the way up.

TIGER: I wondered what that tingling was. Why did you take them?

SUSAN: Just in case this doesn't tum out. I'm giving you this last chance. And then I'm keeping the car.

TIGER: Well, as long as you're being open-minded about it.

SUSAN: Can we get on with this?

TIGER: Hey, I'm not the one holding things up.

SUSAN: Oh, it's all my fault.

TIGER: Okay.

SUSAN: Can we start at the beginning?

TIGER: Alright. Do you want to go first? See, see, I'm trying, I'm trying to be polite, I'm trying to make this work. I'm trying. I'll go first. Unless you want to go first. But don't start with the barbecue.

SUSAN: I won't. You see, my sister Jeanine is like my best friend, and she said you don't get out enough, you don't date enough, and so she took me to this barbecue

TIGER: (Interrupting.) She's starting with the barbecue!

SUSAN: I have to start with the barbecue!

TIGER: You said you wouldn't!

SUSAN: I have to!

TIGER: No you don't! You don't have to do anything. That's what you always tell me. I don't have to listen to you. I don't have to do the dishes. I don't have to dress up like a nurse. Oh, I guess that's getting kind of personal.

SUSAN: But the barbecue is the beginning of us. Where do you want me to start then?

TIGER: Never mind. Just never mind. I'll go first. She's having an affair!

SUSAN: Tiger!

TIGER: What? You don't want me to tell strangers? You want me to lie? What's the point in coming here and paying two hundred dollars an hour if we're going to lie?

SUSAN: (Interrupts) I'm not having an affair.

TIGER: Quiet woman! It's my turn, it's my turn and for once in my life I'm going to take my turn and talk when it's my turn to talk! I forgot what I was going to say. Now I remember! I remember. Let me ask you, how many times a week does UPS come to your house? I mean your office? Once maybe? Twice? They come everyday, everyday to my house, when I'm at work and she's, she's home alone in her bathrobe. Five days a week!

SUSAN: I order a lot of books.

TIGER: She's sleeping with every UPS man in the country! They're probably taking turns and fighting over who gets to come to my house. People are dying because the medicines they need are sitting in my driveway, getting cold. The whole UPS company is going to fold. Fold. And then no one will be able to communicate and the whole country will fall apart.

SUSAN: Wait a minute-

TIGER: (Interrupts.) No! No! No! No! No! No! I don't want to listen to your lies. What's the point in parading them through here? I told the truth. That is the whole true story, and that's why I didn't want to come here. There is no point. We have no future. How can we have one?

SUSAN: May I speak? It's true that I have thought about other men, but I think that's normal.

TIGER: I've never thought about other men.

SUSAN: I've been faithful. It's true that I find a man in uniform irrestible, but I have been faithful. I've just been ordering a lot of books . . . I wouldn't be fantasizing about other men if you loved me!

TIGER: I did love you!

SUSAN: He never wanted me. He wanted my sister.

TIGER: Oh, we're back to the barbecue again! Can't we leave the barbecue behind us?

SUSAN: We went to a barbecue-

TIGER: (Interrupts.) She doesn't ever listen, do you see, do you see, never listens to me.

SUSAN: I went to the barbecue with my sister Jeanine.

TIGER: Ah! Ah! Ah! Ahhhhhhh!

SUSAN: Jeanine and I are like best friends, or we were then. Tiger was already at the barbecue. He started talking to us, my sister and I, we were standing side by side. Tiger said will you go out with me? I couldn't believe it. I said yes. But he wasn't talking to me. He was talking to Jeanine. He was asking Jeanine.

TIGER: It's not true, it's not true. Look at me, would you? I'm a normal, ugly, boring, stupid, repulsive man. I was asking both of them. I was asking everybody. I asked trees and mailboxes.

SUSAN: He was asking Jeanine. He didn't want to go out with me.

TIGER: Okay, okay, it's true I was more attracted to her sister, but I was a little drunk, and Jeanine kept laughing at everything I said and she wasn't wearing a Tee-shirt that said, "I hate everything".

SUSAN: You said you liked that tee-shirt! . . . So Tiger took me out on a date.

TIGER: I took her someplace nice.

SUSAN: He took me fishing.

TIGER: It was a nice boat.

SUSAN: I fell in the water.

TIGER: Never touched her!

SUSAN: He nudged me a little bit but I thought he was being romantic, not trying to push me out of the boat.

TIGER: Alright, alright, the truth is I was passing a little bit of gas and I was moving around to try to hide it, you know, everybody does it. I guess maybe I could have nudged her a little bit.

SUSAN: I can't swim.

TIGER: I saved her though, I saved her! I could have let her drown. Who would have known?

SUSAN: He scooped me out with his big fish landing net.

TIGER: She bent the frame too. I had to buy a new net. Those nets aren't cheap.

SUSAN: He tried to give mouth to mouth. But I wasn't having trouble breathing.

TIGER: Can't blame a guy for trying.

SUSAN: He chipped my tooth with his tooth. He chipped my front tooth, this one right here. (SUSAN shows the “judge”)

TIGER: It hurt me too, it hurt me too!

SUSAN: He felt so guilty, he asked me out again.

TIGER: How do you know I felt guilty, you're inventing feelings and putting them into my mouth.

SUSAN: Did you feel guilty?

TIGER: Of course I felt guilty. I pushed her into sewer water, hit her over the head with a landing net and chipped her tooth. The least I could do was to ask her out again.

SUSAN: He took me pheasant hunting.

TIGER: (Uneasy.) I'm an outdoorsy kind of guy.

SUSAN: He shot me in the rear end.

TIGER: I said I was sorry! It was a light load. She only got a couple of shotgun pellets.

SUSAN: Forty-two! The doctor counted as he dug each one out. I should've known then.

TIGER: She bent over-

SUSAN: (Interrupts.) To tie my shoe-

TIGER: (Interrupts.) And something that looked like a pheasant landed on her butt. I mean her rear end.

SUSAN: We never did find the bird.

TIGER: I think it got trampled into the dirt when you were jumping up and down screaming and calling me vile names.

SUSAN: He felt really guilty after that.

TIGER: Of course I felt guilty! I shot her. I'd be a horrible person if I didn't feel guilty for shooting someone!

SUSAN: So he asked me to go away with him to a cabin.

TIGER: Can't we talk about something else?

SUSAN: We were cutting firewood.

TIGER: I don't want to talk about this anymore. Let's talk about the barbecue.

SUSAN: He cut three of my toes off.

TIGER: It was a bad axe, it wasn't my fault, there was something wrong with the axe!

SUSAN: I can't wear open-toed shoes anymore . . . So he proposed to me.

TIGER: I cut her toes off, what was I supposed to do? Sorry about your toes, see you later?

SUSAN: We got married. You probably think I'm stupid, but I didn't see then that he was motivated by guilt. I thought he really liked me for who I was . . . [but] he really wanted me sister Jeanine.

TIGER: It's not true, it's not true!

SUSAN: After we got married she stopped phoning me. She never comes for visits. No Christmas cards. And she just lives a few blocks away.

TIGER: She hates me. Isn't it obvious that her sister hates me? Can't stand the sight of me! Any person in their right mind avoids me.

SUSAN: My sister loves me and she doesn't want to ruin my marriage. So she's stayed away these past six years. Afraid that just the sight of her would tempt him into . . .

TIGER: Into what?

SUSAN: Adultery.

TIGER: That's ridiculous! That's insane! What's adultery?

SUSAN: You never wanted me. Only Jeanine.

TIGER: No, I'm a jerk and Jeanine knows it. That's why she stays away. Just like your mother.

SUSAN: You punched mother.

TIGER: It was an accident. She hit me first!

SUSAN: She was brushing a bug off your face.

TIGER: How was I supposed to know that?

SUSAN: You don't want me. You want Jeanine.

TIGER: That's crazy. Do you call her? Do you send her a Christmas card? Why should she send you one? It doesn't mean anything.

SUSAN: She's never visited me.

TIGER: That's because she can't get in our driveway because it's filled with UPS trucks.

SUSAN: You've never loved me! You just married me out of guilt!

TIGER: No, I married you because I'm stupid! Stupid stupid stupid stupid!

SUSAN: (to judge.) Make him stop, make him stop!

TIGER: (to judge) Make her stop! She's the one who had to bring up that stupid barbecue.

SUSAN: I wish I'd never gone to it!

TIGER: Not as much as I do!
```

---

## IC-0842: Medusa’s Tale

- Title: Medusa’s Tale
- Author (byline): Carol S. Lashof
- Work: Plays in One-Act
- Publisher: Ecco Press
- Publication date as stated: Sept 1991
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: PERSEUS, MEDUSA, ATHENA, POSEIDON, NARRATOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1954
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carol S. Lashof AWARD HISTORY
Book: Plays in One-Act
ISBN: 978-0880013055 2009 National Qualifier
Publisher: Ecco Press
Date (Month/Year): Sept 1991
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: In Greek mythology, the stories of Medusa are often contradictory. Was she a victim or a villain? Was she always ugly or once beautiful?

ACTOR: One story reports Medusa's beauty was so stunning that many men courted her, but she became a priestess in Athena's temple.

ACTRESS: Her golden hair and her beauty attracted the lustful eyes of the sea god, Poseidon.

ACTOR: They consummated their relationship in Athena's temple, a terrible violation of a sacred place.

ACTRESS: Stories differ as to whether he raped Medusa or she enticed him first.

ACTOR: Regardless . . . when Athena learned what had happened she flew into a rage and cursed Medusa with snakes for hair and a face that turned those who looked at her to stone.

ACTRESS: But this was not enough for Athena:. . . eventually she sent her brother Perseus to bring back the gorgon’s head.

TOGETHER: This is Medusa’s Tale by Carol S. Lashof
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

MEDUSA hums a jaunty love song-perhaps "Froggie Went a 'Couriing."

PERSEUS: I am the hero Perseus, son of the great god Zeus.

MEDUSA: And I'm Medusa, cast out by gods and kings. You've come to slay me, I presume? (Pause.) Cat got your tongue? You warriors, you're all alike. Look at these fellows: civilized young men, from the very best families, but no appreciation whatsoever for the art of conversation. They do make handsome statues, though, don't they?

PERSEUS: It's true that you turn people to stone just by looking at them? Evil monster, beware ...

MEDUSA: Do I look like an evil monster? Tell me. I want to know.

PERSEUS: Don't think you can trick me into meeting your eyes. Athena has blessed me with wisdom. She has sent me to carry out her will.

MEDUSA: Athena! If you're her slave, then I'll gladly stop your blood dead in your veins.

PERSEUS: I am not her slave. I am her brother. She is the greatest goddess of them all, sprung fully armed from Zeus's noble brow. And I, too, am a child of the almighty Zeus, lord of the heavens. Who but he could have slipped through the bars of that tower, a hundred feet high, where she was locked up, my mother. ...

MEDUSA: And how did Zeus manage this fancy trick? Did he come as a mosquito and buzz in between the bars of her prison window? Did he impregnate her with a sting?

PERSEUS: Blasphemer! He came as a shower of gold.

MEDUSA: (Pause. Astonished.) Are you Danae's child? You can't be. She did have a son, but they were both drowned long ago, she and her baby. I knew Danae. (Pause.) We were girls together. She used to braid my hair while I told her stories of distant lands. She was hungry for knowledge. But then her father killed her.

PERSEUS: My mother told me we were rescued from the sea when I was a baby.

MEDUSA: When you get angry, you knit your brows just the way Danae used to do. No! Don't turn away from me. Close your eyes. Let me look at you. You've got your mother's figure-long and slim.

PERSEUS: Don't touch me, hag! I don't believe you knew my mother. She would never have gone near such a monster as you.

MEDUSA: I was no monster, then. I was honored for my beauty. Poseidon himself was in love with me. Do you know what the love of the gods has done for me?

PERSEUS: Everyone knows you were cursed by the gods for your crimes.

MEDUSA: No one knows! (Pause.) If I set you free, will you listen to my story? Will you go home and tell Danae?

PERSEUS: I'll never go home unless I can take your bloody head with me.

MEDUSA: (Pause.) All right. If it has to be that way. Listen closely so you may judge for yourself what the love of the gods is worth. . . . Now we are in Athens. Look there. On the hill. Above the well. Glaring white against the blue horizon. Athena's sanctuary. And there she is. The goddess of justice. Favorite daughter of Zeus. And here comes Poseidon, Earthshaker. Brother of Zeus and Lord of the Ocean.

ATHENA: Honored uncle, what brings you to my blessed city?

POSEIDON: Just passing through.

ATHENA: Flourishing. Thanks to the olive tree, all the citizens of Athens enjoy my bounty.

POSEIDON: And the women and slaves of Athens enjoy a mule's life.

ATHENA: Slaves must drive the mill wheels so their masters may be free to keep the wheels of justice turning. I have given the Athenians the gifts of law and commerce-and they adore me for it.

POSEIDON: They're afraid of Zeus and his thunderbolts, that's all.

ATHENA: You're jealous of the love these mortals bear for me.

POSEIDON: Love! You're far too icy-hearted to know anything about love.

ATHENA: Naturally, I disdain the appetites that drive mere beasts to grunt and thrash. (Two girls are heard approaching from the distance, chattering and laugh-ing.)

POSEIDON: Now here comes a truly lovable being. Who's she? The dark one with her hair down her back.

ATHENA: Medusa. She's been conducting a faithful pilgrimage to all my temples. She blesses me for protecting her chastity, the wellspring of her freedom.

POSEIDON: Chastity! The emptiest of all the empty virtues. . . . but if she knew the love of a real god ...

ATHENA: She would spurn you. And your brutish love.

POSEIDON: Do you think so? Let me have just half an hour alone with her.

ATHENA: You may have half of all eternity. Nothing you can do could wrest her love from me.

POSEIDON: We'll see. (POSIDON approaches, whistling a sea song.) And what's your name?

MEDUSA: Medusa.

POSEIDON: How old are you?

MEDUSA: Seventeen.

POSEIDON: Too old for a mother's caresses.

MEDUSA: I never knew my mother. She died when I was born.

POSEIDON: You're old enough to be a mother yourself.

MEDUSA: I don't want children. That's why I follow Athena.

POSEIDON: Do you know who I am?

MEDUSA: Of course. You're Poseidon. My father works for you.

POSEIDON: Wouldn't you like to bear the child of a god?

MEDUSA: No. Mv friend Danae had a child by Zeus and her father killed her for it. An oracle told him that he'd be killed by his grandson. So he killed the baby and Danae, too, so she wouldn't produce any more sons. He tossed them both in a casket and shoved them out to sea. They must have drowned. Or starved.

POSEIDON: A god would never allow a son of his to come to harm. I could easily pay a visit to my brother Zeus and find out about Danae for you.

MEDUSA: W ould you?

POSEIDON: For a price. Don't you care to know what's happened to your friend?

MEDUSA: What good would it do? I'm sure she's dead.

POSEIDON: All right, then. Be seeing you, (Whistling,Poseidon begins to walk away.)

MEDUSA: Wait! (Pause. Almost a whisper.] What is your price?

POSEIDON: To intercede on behalf of your friend? What would you give me?

MEDUSA: My hair. I'll cut off all my hair and give it to you. (Poseidon laughs.) Men always beg me for just one lock. They say they will keep it always, it will be their clearest treasure.

POSEIDON: You have a dearer treasure than your shiny hair. Have you given that away?

MEDUSA: I don't know what you mean. You're hurting me. Let me go!

POSEIDON: All I want is a kiss. Hmmm. Don't clench your teeth. Oww! So you bite, do you? Vixen! Oof! And kick, too? That's all right, I like a little spice in my stew. Go ahead. Run to Athena's sanctuary. It's a fine and private place.

(Gasping for breath, MEDUSA scuttles across the stone colonnade. The heavy doors of the temple creak.)

MEDUSA: In Athena's name. Please. This is holy ground.

POSEIDON: (Laughing.) Wherever I am is holy ground.

MEDUSA: Athena! Please! Save me, Athena!

NARRATOR: POSEIDON laughs. MEDUSAscreams. Then there is silence. Finally, we hear MEDUSAsobbing; POSEIDON, whistling, emerges onto the colonnade. The temple doors clang shut, muffling the sound of MEDUSA’s sobs.

ATHENA: I didn't count on your brutalizing her within the walls of my own temple. It's an offense against all the gods. There'll be no harmony in the heavens till penance has been done!

POSEIDON: So punish the girl for taking refuge in your sanctuary. Am I to blame because she clung to the feet of your statue while I took her? So, Athena, do you still claim the girl as yours? Such a fine creature. What a pity if she'd gone to her grave a virgin. Hush. Here she is now. Ask her if she still adores you. (MEDUSA approaches, weeping.) Come, my dear, don't cry. There's no harm done.

MEDUSA: (Strangling a scream.) Stay away from me! Athena. Don't let him touch me, please.

POSEIDON: That's right, Brighteyes, hide the girl behind your skirts. But you did nothing while we took our pleasure in the heart of your temple. You stood in the doorway and watched. (Silence.)

ATHENA: You should have run away before it was too late. It's foolish pride for a mortal girl to have no fear of gods.

POSEIDON: See, Medusa. Athena will have nothing more to do with you. Come, you'll live with me in my golden palace. [to audience] And if she's a sweet, tender girl and treats me as a god deserves, then I'll give her jewels and fine sons, and I'll make all my minions bow to her.

ATHENA: You won't have her, Poseidon. No one will have her. Father Zeus. Thunderer. Give me the power to punish this sacrilege. (There is a deafening crash of thunder, followed by a moment's silence. Then the air is filled with hissing. MEDUSA cries out in anguish.) Zeus has struck you with his lightning. The pain will soon subside. But the vipers will remain, a warning to all vain, glorious mortals. Come, look at your reflection. See the penance you have earned.

MEDUSA: Poseidon, help me! Help me rip them out!

POSEIDON: Nothing could be more hideous. In all the wild sea I have never seen creatures so vile.

MEDUSA: Will you turn from me, too, Poseidon?. I'll go with you. I'll learn to find pleasure in your touch. I'll bear your sons ...

POSEIDON: You would bear me monsters.

MEDUSA: But look at me! You found me beautiful. See. My eyes are still bright, my lips still moist, my skin still smooth as cream. [POSEIDON leaves] Don't leave me!

ATHENA: Do you dare to turn to him, who ruined you, and beg for pity? Every creature on this earth will turn away from you. See those women, hurrying to be home by dark? The story of your infamy will soon be spread among them-and they will learn not to be so unafraid. And any other mortal who lacks the wisdom to turn his back on you or shut his eyes will turn to stone. *******************************

NARRATOR: And so Medusa concludes her story . . . . ****************************

PERSEUS: I never really wanted to come here. Let me go-before you cloud my wits completely.

MEDUSA: Nobody's keeping you, my young hero. (Pause.) Give my regards to your mother. (Pause.) What's the matter? Can't you bear to leave me? Or have you forgotten something? Oh, yes, my head. You came for my head, didn't you?

PERSEUS: When I was home, the women hissed at my mother on the street and called her names. The boys threw clods of dung at me. Then Athena came to me. She told me I was destined to be a hero. She told me how to find this desolate place. She said you would be asleep. I only had to avoid looking at you-and then I could easily kill you, she said. (Pause.) Did you know that she wears your image emblazoned on her armor? Your face is beautiful. The snakes are hideous, but your eyes, your mouth, more beautiful than any woman I've ever seen. Suppose you'd borne Poseidon's son, wouldn't you want him to grow up to be a hero?

MEDUSA: Do you believe me, then?

PERSEUS: I don't know. Athena is my guardian. I must believe in her. She is wise and just. She would not punish someone who was virtuous.

MEDUSA: She failed me. And she punishes me for having seen her failure.

PERSEUS: I must kill you. Or else I am nothing.

MEDUSA: Yes, I know. But after you have killed me, then what? Will you go home to your mother? Wll you tell her my story?

PERSEUS: Yes. I'll tell her.

MEDUSA: And what will you do with my head?

PERSEUS: I'll put it in this leather pouch.

MEDUSA: And if anyone makes trouble for you, you'll just whip out my head and turn him into a statue

PERSEUS: I don't know. What difference does it make to you?

MEDUSA: I just want to know how the story ends. (Pause.) You're doomed to be a hero. MEDUSA hums a jaunty love song-perhaps "Froggie Went a 'Couriing." [PERSEUS beheads MEDUSA with one pass of his sword and places her head in a leather pouch]

PERSEUS: [Sadly] Listen! (Pause.) In this leather pouch is the severed head of Medusa, the gorgon known throughout Greece to be the most loathsome of creatures. Hideous vipers grow from her scalp. They are still alive and writhing, though she is dead. One glance at them and you would turn to stone. Many men perished trying to slay this monster. Then I came to the barren island where she lived in exile.
```

---

## IC-0843: The Miraculous Journey of Edward Tulane

- Title: The Miraculous Journey of Edward Tulane
- Author (byline): Not specified
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: 2021
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR, ACTRESS, TRAVELER, ABILENE, EDWARD, MARTIN, BRYCE, SARAH RUTH, BRYCE’S FATHER, NEAL, LUCIUS, OLD DOLL, SHOPPER
- Teaser before the introduction: Yes
- Spoken words (computed): 1941
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dwayne Hartford (from the book by Kate DiCamillo)
ISBN: 978-1619591752
Publisher: Dramatic Publishing
Date (Month/Year): 2021
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: The Miraculous Journey of Edward Tulane adapted by Dwayne Hartford from the

book by Kate DiCamillo. ACTOR: Because if you have no intention to love and be loved, then the whole journey is

pointless.
```

### Performance text (classify this)

```text
Adapted by Dwayne Hartford (from the book by Kate DiCamillo)

Suggested Roles:

ACTOR: Traveler; Edward; Father; Bryce’s Father; Neal

ACTRESS: Abilene/Shopper; Martin; Bryce; Sarah Ruth; Lucius; Old Doll

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

TRAVELER: (Pg 7-8) Once, in a house on Egypt Street, there lived a rabbit made almost entirely of china. But how did such a thing come to be? Did the rabbit belong in this fine house? Was this the rabbit's home? Ah. Now that is an interesting question.

ABILENE: Oh, grandmother! (ABILENE takes the rabbit.) He is the most beautiful thing I have ever seen. Thank you! I love him. (She considers a name) Edward . . . Edward Tulane. Just look at him. He's so dignified and refined.

TRAVELER: (Pg 10) Of course, Edward didn't answer. He couldn't, you see. His mouth was painted on, as was the rest of his face. But still he had his thoughts.

EDWARD: (Pg 11-12) I do look good. Now be careful you don't wrinkle my jacket. And fix the tie. I'm sure it's crooked.

FATHER (OFF STAGE): Abilene! Come along now. You'll be late for school, and I'll be late for work.

ABILENE: Oh, your watch. (She removes a watch from one of his pockets, winds it and places it in his hand.) Now remember, when the big hand is on twelve and the little hand is on three, I will come home to you. Have a pleasant day looking out the window.

TRAVELER: And so Edward Tulane spent his days, staring out upon Egypt Street, listening to the ticking of his watch. And at three o'clock Abilene would return.

ABILENE: Hello, Edward. I'm home. And how was your day? (ABILENE picks up EDWARD)

EDWARD: What are you doing? Don't move me now. It'll be dark soon, and I'll be able to see my reflection in the window.

ABILENE: Cynthia Worthington is so mean. She wouldn't let me have a turn at recess today.

EDWARD: (Pg 13) Blah, blah, blah. Must she go on so? I mean really.

TRAVELER: Yes, Edward had little patience for people. What they said didn't interest him, unless they were talking about him, of course.

ABILENE: (Pg 19) (hugs Edward as she tucks herself and Edward in bed) Good night, Edward. I don't care how old I get, I will always love you.

EDWARD: Yes, yes, but tum me on my side so that I can see the stars. Oh, dear.

TRAVELER: (Pg 13) Life continued this way for years. (Pg 15) [Then] one day it was announced that the family would take a voyage on a great ship. (Pg 19) Edward, Abilene and her parents set sail for England.

ABILENE: Shall we sit up here on deck, Edward? I believe the sea air will do us good.

EDWARD: Is my hat on straight? I'm sure to be complimented on the hat.

MARTIN: (Pg 21) Hey. What does he do? (Referring to EDWARD) Does he wind up?

ABILENE: Certainly not. (MARTIN grabs EDWARD and runs away from ABILENE)

EDWARD: Stop it! Young man, I demand you release me at once. (MARTIN throws EDWARD in the air)

ABILENE: (Pg 22) Don't throw him, he's made of china! He'll break! He's mine. Give him to me!

TRAVELER: And Edward flew over the railing and sailed out over the ocean.

ABILENE: Edward! Nol

TRAVELER: As Edward Tulane hit the water, he caught one last glimpse of Abilene, standing on the deck, holding his gold pocket watch. (Pg 23) Finally he landed on the ocean floor, face down in the muck. Weeks passed. And then months. Edward, for lack of anything better to do, started to think.

EDWARD: Are the stars still shining even though I can't see them anymore? I'll never see the stars again. (Pg 49) If I had wings I would fly away. I would fly away high up to the stars.

TRAVELER: (Pg 24) On the two hundred and ninety-seventh day [there was] a powerful storm. And up to the surface he came. Before he knew what had happened, Edward was pulled up out of the water. *****

BRYCE: (Pg 51) Heyl I got you. See? I saved you.

EDWARD: You saved me, but for what?

BRYCE: My little sister had a baby doll that was made out of china just like you. She loved that doll, but he come home drunk, stepped on the doll's head and smashed it into a hundred million pieces. I couldn't make them go back together. I tried and tried. Sarah Ruth ain't had nothing to play with since.

EDWARD: (disdainfully) So you want me to be the replacement for a doll.

BRYCE: He says she don't need nothing because she's sick and ain't gonna live. But he don't know.

TRAVELER: (Pg 52-53) They arrived at a house. It was small and crooked – not much more than a shack.

BRYCE: Sarah? (Sarah Ruth coughs violently) Want to see what I brung you? Close your eyes.

(Sarah Ruth stops coughing and closes her eyes – Bryce holds up Edward) All right, you can open them. (Bryce moves Edward as if he is dancing – Sarah Ruth laughs) I got him special for you.

EDWARD: Special (Sarah Ruth holds Edward like a baby) No one has ever held me like this.

BRYCE: From the minute I first seen him, I knew you two belonged together. What’s his name?

SARAH RUTH: Jangles (She rocks Edward back and forth)

TRAVELER: Later that night after the brother and sister had fallen asleep, a large figure appeared over Sarah Ruth’s bed. (The children awake)

BRYCE: (Pg 54-55) (fearful, but also defiant) It’s a doll. He belongs to her.

BRYCE’S FATHER: Don’t you sass me. (He raises a hand and strikes; Bryce reacts to the slap)

BRYCE: (long pause as father exits) I'm all right. He hardly touched me. But he'll feel bad about it and won't come around for a while. And that's just fine with us, ain't it, Sarah Ruth?

EDWARD: (to SARAH RUTH) I wish I could protect you from that man. I wish I could.

TRAVELER: Days passed. Every morning Bryce went out to find food for his sister. Edward spent all his time with Sarah Ruth. Some days they played with an old cigar box filled with buttons. (SARAH RUTH starts to cough. She grabs EDWARD and holds him tightly)

EDWARD: I wish I could protect you -- from everything. But I can only ... You just hold on tight.

BRYCE: Hey there, honey. Now, I'II hold Jangles; him and me got a surprise for you. (BRYCE takes EDWARD and hides the rabbit from SARAH RUTH while he attaches the strings.) I got this idea the first night I brung him to you. Today, I was working for the junk man. And he said I could have some of this here twine. (Pg 56-57) When you were really little, Mama used to dance with you. She used to hold you and dance you around the room.

SARAH RUTH: Mama. Died.

BRYCE: Well now we have another dancer in the house. Dance, Jangles. (BRYCE has rigged EDWARD with strings like a marionette.)

EDWARD: What's happening to me?

SARAH RUTH: (Sarah Ruth laughs) Dancing!

EDWARD: Do you like it, Sarah Ruth? (SARAH RUTH applauds and laughs.) Bryce! Make my legs kick again! She loves that! (EDWARD joins the laughing. SARAH RUTH's laughing turns to coughing.)

BRYCE: You want some fresh air? Let's go take a peek at the stars for a minute.

EDWARD: If l had wings, I would fly high up to the stars, where the air is clear and sweet. I would hold Sarah Ruth in my arms, and high above the world, she could breathe and laugh and talk, and she wouldn't ever have to cough again.

TRAVELER: Days and weeks passed. Sarah Ruth grew weaker. (BRYCE plays the harmonica as EDWARD dances.)

EDWARD: Why isn't she laughing? Sarah Ruth? I'm doing the kicks you like. Sarah Ruth?

(BRYCE stops playing and goes to SARAH RUTH's side.) Don't stop! Keep playing, Bryce! Keep playing!

TRAVELER: But Bryce stopped playing.

EDWARD: (Pg 58-59) Breathe. Please, please, breathe.

TRAVELER: Then, on a bright morning in September, six months after Edward first came to the shack, Sarah Ruth stopped breathing.

BRYCE: No reason to stay here no more. Come on, Jangles.

TRAVELER: Under a hot, late-summer sun, the boy silently carried the rabbit all the way into the city.

BRYCE: I bet nobody's ever seen a dancing rabbit before. Well, they're going to see one now.

(BRYCE plays the harmonica and manipulates EDWARD to dance.)

TRAVELER: Bryce set out Sarah Ruth’s button box and people dropped pennies and nickels into it. Edward Tulane danced on a dirty street comer. On and on, Bryce played. On and on, Edward danced.

EDWARD: Are you crying, Bryce? Tears. Do they help?

BRYCE: (Pg 60) (wiping his tears and picks up the button box) Looks like we got us enough money to get something to eat. Come on, Jangles.

TRAVELER: The diner was called Neal's. Bryce sat at the counter. He set Edward on the stool next to him.

BRYCE: Give me some pancakes, and some eggs, and steak, too.

TRAVELER: He ate it all – [but when the check came. . . ]

BRYCE: I ain’t got enough.

NEAL: (Pg 61-62) (angry and threatening) You came in here hungry, right? You ordered some food - a lot of food - and I cooked it, right? You ate it. Now, I want my money.

BRYCE: You ever seen a rabbit dance? (BRYCE starts manipulating EDWARD to dance) He could dance to pay for what I ate.

EDWARD: I can! Watch! I'll pay for him! I will!

NEAL: (NEAL grabs EDWARD) This is what I think of dancing rabbits.

TRAVELER: Edward felt himself swinging through the air. He was moving so quickly he couldn't see Bryce. He couldn't see Neal. He couldn't see the countertop. (NEAL slams EDWARD’s head into the countertop.) And the world -- Edward's world -- went black.

EDWARD: (in a dream vision) Wait - I know this house. I'm on Egypt Street. How did I get here? Abilene?

ABILENE: (Pg 63) Edward! I've never forgotten you. I say your name every day.

EDWARD: The stars. (EDWARD looks up at the stars.) Sarah Ruth?

BRYCE: Hey, Jangles.

EDWARD: Bryce! (pointing to the stars) Sarah Ruth is in the stars! (Pg 64) I want to be with her. If only I had wings. (Wings are revealed on EDWARD 's back) What is happening to me? Wings! Sarah Ruth! I'm coming! (he begins to cry) (Pg 65) My heard is broken. ***** A Doll Shop*****

LUCIUS: Exceedingly well made. You don't see craftsmanship like this every day. How did you end up so dirty and abused? I fixed your broken head. Now I'll fix the rest of you. I'm Lucius Clarke. I'm a doll mender, and a rather good one at that. Your head was in twenty-one pieces.

EDWARD: Where am I? Twenty-one pieces.

LUCIUS: (Pg 66) A crying little boy brought you here. He couldn't afford my services so he gave you to me if I promised to repair you.

EDWARD: Bryce . . . You should have left my head in twenty-one pieces. I will never be truly whole again.

LUCIUS: Someday. Eventually. All in good time. In the doll business, we have a saying: there is real time, and there is doll time.

TRAVELER: Edward Tulane entered doll time - a time of waiting. Slowly and carefully, Lucius Clarke did everything he said he would. Except for the very faint lines on his face, Edward Tulane looked the same as he did many years ago. Edward was placed on a high shelf for display.

EDWARD: (Pg 67) I am done with hope. I am done with love. I am done.

LUCIUS: (He sets an old restored doll on the shelf next to EDWARD) Here you go, my lovely. Sit here, next to this gentleman. You two have much in common. You have both been saved.

OLD DOLL: How do you do? Have you been here long?

EDWARD: Yes, months and months. But I don't care. One place is the same as the other.

OLD DOLL: But that's not true! I've lived for a hundred years and I've been in countless places. Some were wonderful and some were dreadful. But they are never the same. That's part of the adventure, you know? (Pg 68) My face has its share of cracks as well. I too have seen life. We have learned, yes?

EDWARD: Yes. Hard lessons.

OLD DOLL: Wonderful lessons. And we keep learning, don't we? Every time a new person comes into our lives, we start off on a new adventure. I wonder who will come for me this time. Someone will come. They always do.

EDWARD: I don't care if anyone comes for me.

OLD DOLL: Don't say that! You must keep your heart open, ready to love and to be loved.

EDWARD: I'm done with being loved. I'm done with loving. It's too painful.

OLD DOLL: (Pg 69) You disappoint me. If you have no intention to love and be loved, then the whole journey is pointless. Someone will come for you. But first, you must open your heart.

EDWARD: Someone will come. Someone will come.

TRAVELER: And every time he thought those words, he allowed himself to hope a little more. Weeks turned into months. Months turned into years.

EDWARD: Someone will come.

TRAVELER: Then one rainy spring morning, someone came.

SHOPPER: (Pg 70-71) I'm looking for something for my daughter. Something ... unique.

LUCIUS: (He lifts EDWARD off the shelf) Madam, if I may. This one’s not a doll. Perhaps he is what you are looking for. (The SHOPPER takes EDWARD and stares into his eyes)

EDWARD: I know you.

TRAVELER: A memory came to Edward Tulane. The memory of a little girl, many years ago. Abilene . . . a little girl who had grown up into a woman.

SHOPPER: Edward? (She hugs Edward as he cries - Beat)

TRAVELER: Once, there was a china rabbit who was loved by a little girl. (beat) Once there was a rabbit who loved a little girl and watched her die. The rabbit danced on the streets to the music of a sad little boy. The rabbit's head was broken and put together again by a doll mender. And the rabbit swore that he would not make the mistake of loving again. (beat) Once, oh marvelous once, there was a rabbit who found his way home.
```

---

## IC-0844: A Monster Calls

- Title: A Monster Calls
- Author (byline): Patrick Ness
- Work: Not specified
- Publisher: Candlewick
- Publication date as stated: March 2013
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR 1, NARRATOR 2, MONSTER, CONOR, MUM
- Teaser before the introduction: Yes
- Spoken words (computed): 1035
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patrick Ness
ISBN: 978-0763660659
Publisher: Candlewick
Date (Month/Year): March 2013
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Elizabeth Kubler Ross created a pathway to grief with her five stages: Denial, Anger, Bargaining, Depression, Acceptance.

ACTRESS: These stages are meant to allow grief to be understood, and the sufferer to let go.

ACTOR: When Conor O’Malley finds out his mother is dying of cancer, he lives in denial and pent-up anger.

ACTRESS: No one talks about her death -- not her, not his grandmother, not his father, and not him.

ACTOR: Not until he is forced to face the inevitable and deal with his grief. This grief takes the form of a monster.

ACTRESS: A monster who forces him to face the truth and guides him to acceptance.

TOGETHER: A Monster Calls by Patrick Ness
```

### Performance text (classify this)

```text
Suggested Roles: Actress: Narrator 2, Monster, Mum

Actor: Narrator 1, Conor

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NARRATOR 1: (Pg 1-2) The monster showed up just after midnight. As they do.

NARRATOR 2: Conor was awake when it came. He’d had a nightmare.

NARRATOR 2: Well, not a nightmare. The nightmare. The one he’d been having a lot lately.

NARRATOR 1: The one with the darkness and the wind and the screaming.

NARRATOR 2: He’d told no one about the nightmare. Not his mum, obviously, but no one else either.

NARRATOR 1: What happened in the nightmare was something no one else ever needed to know.

NARRATOR 2: The nightmare was slipping from him, but there was something he couldn’t put his finger on, something different . . . He listened, but all he could hear was the quiet house around him. Nothing.

NARRATOR 1: And then something. Something he realized was the thing that had woken him. Someone was calling his name . . .

MONSTER: Conor.

MONSTER: (Pg 4) Conor.

CONOR: (heart thumping and impatient) What?

NARRATOR 2: A cloud moved in front of the moon, and then passed, and the moon shone again.

NARRATOR 1: On a yew tree. Which now stood firmly in the middle of his backyard. And here was the monster.

MONSTER: (Pg 136) The yew is a healing tree. It is the form I choose most to walk in. (Pg 137) If your mother can be healed, then the yew tree will do it.

CONOR: (Pg 30) What do you want from me?

MONSTER: (Pg 36) You will tell me the truth.

CONOR: The truth?

MONSTER: Not just any truth. Your truth. You know that your truth, the one that you hide, Conor O’Malley, is the thing you are most afraid of. For this is why you called me.

CONOR: (confused) Called you? I didn’t call you— (Pg 141) “What’s going to happen with my mum? You said you were a tree of healing. Well, I need you to heal!”

MONSTER: (Pg 172) Conor O’Malley, I did not come to heal her, I came to heal you.

CONOR: Me? I don’t need healing. My mum’s the one who’s...

NARRATOR 2: But he couldn’t say it. Even now he couldn’t say it. Even though he’d known it all along.

NARRATOR 1: Of course he did, no matter how much he’d wanted to believe it wasn’t true, he knew. But still, he couldn’t say it. Couldn’t say she was--

MONSTER: It is time, for [your truth].

NARRATOR 1: The mist surrounded them again. And once more, [he] was in the middle of the nightmare . . .

NARRATOR 2: (Pg 174-175) He recognized the clearing he was in, bordered on three sides by a dark forest; the fourth side, a cliff, flying off into further blackness. And on the cliff’s edge, his mum. (Actress assumes the character of Conor’s Mum at the edge of a cliff)

CONOR: (drops to his knees, struggling to stand; he yells) Mum! You have to get out of here!

MUM: (Turning at the sound of his voice) I’m fine, darling. There’s nothing to worry about.”

(Turns back to the cliff as if she’s heard something calling her)

CONOR: (whispering to himself) No.

NARRATOR 2: He pulled himself forward some more, but she was too far, too far to reach in time, and he felt so heavy--

NARRATOR 1: There was a low sound from below the cliff. A rumbling, booming noise. Conor knew. It was too late. The real monster was coming.

NARRATOR 2: (Pg 178-181) With a roar, a cloud of burning darkness lifted two giant fists over the cliff top. They hovered in the air, over his mum as she tried to scramble back. But she was too weak, much too weak-

NARRATOR 1: At last, Conor could run. With a shout, he broke across the clearing, running so fast he nearly toppled over, and he threw himself toward her as the dark fists pulled her over the edge. And his hands caught hers. (Actor lunges toward his mum as he speaks this last line)

MUM: (yelling) Help me, Conor! Don’t let go!

CONOR: I won’t! I promise!

NARRATOR 2: The nightmare monster pulled harder, its fists straining around his mother’s body. And she began to slip from Conor’s grasp.

CONOR: No!

MUM: (screaming in terror) Please, Conor! Hold on to me!

NARRATOR 1: [But even as she said this, her hands] were slipping from his grasp, and she was getting heavier and heavier;

NARRATOR 2: The nightmare monster pulling harder and harder. He fell forward onto his chest from the weight of her. She screamed again.

CONOR: (falling forward from the weight of his mum’s grasp -- whispering) Please! Please! (he loses his grip and his mother falls; Conor screams) NO!

MONSTER: And here is the truth of Conor O’Malley. (Pg 185-189) You let her go.

CONOR: (shouting) I didn’t let her go! She fell!

MONSTER: You must tell the truth or you will never leave this nightmare. You will be trapped here alone for the rest of your life.

CONOR: (still shouting and fighting the urge to speak) I don’t know what you mean!

MONSTER: (low and threatening) You do know.

NARRATOR 1: And there was a sudden quiet. Because yes, Conor knew. The truth.

NARRATOR 2: The real truth from the nightmare.

CONOR: Please don’t make me, please don’t make me say it.

MONSTER: You let her go. You could have held on for longer, but you loosened your grip. You wanted her to go.

CONOR: NO!

MONSTER: You must speak the truth, Conor O’Malley. Say it. You must.

CONOR: I can’t.

MONSTER: You let her go. Why? Tell me WHY! Before it’s too late!

NARRATOR 1: A moan started in his throat, a moan that rose into a cry and then a loud wordless yell and he opened his mouth.

NARRATOR 2: And he spoke the truth.

CONOR: (crying out) I can’t stand it anymore! I can’t stand knowing that she’ll go! I just want it to be over! I want it to be finished! I’ve known forever that she wasn’t going to make it. And I started to think how much I wanted it to be over. How I couldn’t stand the waiting anymore. I couldn’t stand how alone it made me feel.

NARRATOR 2: He began to cry now, more than he thought he’d ever done. More than when he found out his mum was ill. (Pg 203)

NARRATOR 1: He wanted to ask the monster what was going to happen then, but he didn’t dare. Because he knew. (Actor assumes the role of Conor and pantomimes the following)

NARRATOR 2: [And then they were in his mother’s hospital room] (Pg 202) The monster’s hands gently but firmly guided him toward [her]. (Pg 203-205) (Conor looks down at her and takes her hand.) She opened her eyes, briefly, catching him there. Then she closed them again. But she’d seen him. And he knew it was here. He knew there really was no going back. That it was going to happen. And he knew he was going to get through it. And at last, he spoke the final and total truth . . .

CONOR: (tears falling from his eyes) I don’t want you to go.

MUM: (in a heavy voice) I know my love. I know.

CONOR: I don’t want you to go. (he leans forward and puts his arms around her, holding her)

NARRATOR 2: And that was all he needed to say. He could feel the monster, holding him up and letting him stand there.

NARRATOR 1: (Actor speaks from actor’s position, still cradling Conor’s mother in his arms) He knew it would come. The moment she would slip from his grasp, no matter how tightly he held on. And by doing so, he could finally let her go.

MONSTER: (whispering) But not this moment. Not just yet.
```

---

## IC-0845: The Moon Please

- Title: The Moon Please
- Author (byline): Diana Son
- Work: Take Ten II: More 10-Minute Plays; Pgs 207-216
- Publisher: Knopf Doubleday Publishing
- Publication date as stated: Nov 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CIEL, JAY
- Teaser before the introduction: No
- Spoken words (computed): 1466
- Already set (do not supply): none

### Source block (context only)

```text
Author: Diana Son
Book: Take Ten II: More 10-Minute Plays; Pgs 207-216
ISBN: 978-1400032174
Publisher: Knopf Doubleday Publishing
Date (Month/Year): Nov 2003
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: September 11, 2001 – New York City

ACTRESS: New parents Jay and Ciel are struggling to navigate work, finances, and sleepless nights with a newborn.

ACTOR: Their everyday chaos and arguments could change everything. You see, Ciel’s first day back at work will take her to the Twin Towers on 9/11.

ACTRESS: Should she stay home with the baby?

TOGETHER: The Moon Please by Diana Son
```

### Performance text (classify this)

```text
CIEL: (Pg 207-216) (JAY walks in as CIEL looks through a stack of papers) I'm missing a page. I'm (riffles through report) The page with the pie chart. It should be right here.

JAY: What color is this tie?

CIEL: I can't go in there without that page. You know how Schaefer is, he's gotta have his visual! Dammit, I can't believe this is happening to me today. (notices JAY 's tie) Brown. It doesn't go.

JAY: This tie is brown? It's not blue?

CIEL: No. (JAY stares at the tie, willing it to turn blue) Wear your maroon tie . . . the one with the squiggly stripes. (riffling again)

JAY: Just print another copy, honey, it doesn't have to be /

CIEL: I can't print it out. The baby's been sleeping so lightly lately and our printer makes such a rack /

JAY: She's gotta get used to our noises. Remember what the doctor said? I mean, this is a one-bedroom apartment. We've all gotta share the space.

CIEL: I know that, but I just can't deal with her being awake when I leave and I have to leave in (checks watch) 10 minutes at the latest. Can you wait until Georgia gets here?

JAY: What time is she supposed to come?

CIEL: (checks watch) 20 minutes ago.

JAY: I can't be late to my interview. I mean, they're not gonna hire someone who can't even come to the interview on time. Maybe you should call her.

CIEL: What time's your interview?

JAY: Nine.

CIEL: What about my pie chart?

JAY: Print it at the office.

CIEL: I forgot to pack my pump. (heading for the kitchen) We're not meeting at the office. We're doing the pitch at a conference room.

JAY: (leaving for the bedroom) You better call Georgia. (CIEL returns to the living room and picks up the phone)

CIEL: Be quiet when you're in there, please. (JAY in the bedroom, takes down a tie and freezes when he hears the baby) (as she dials) It's just that it took me 45 minutes to get her down. (into phone) Hey! What are you still doing home? It's 8:20, you said you'd be here twe- (CIEL listens. JAY peers into the baby's bassinet and watches her breathe as if it were possible the next breath won't come) Georgia. . . It's going to take you half an hour just to get here. I have to be all the way downtown by nine (drops the phone [still holding it] and covers her eyes. Puts it to her ear again. Meanwhile, JAY can't resist the temptation to touch the baby ever so slightly, to establish a connection without waking her) I can't believe you. This is my first day back at work! How can you do this to me, Georgia? I'm the only one making any money, what are we gonna do if I get fi- (JAY reenters with the new tie. Ciel doesn't pursue this line of thinking) You are totally irresponsible. I can't. No, forget it, I don't even want you to come. (slams down the phone. JAY waits for her to make the first move) I can't believe her.

JAY: I guess that's what we get for not hiring a real babysitter.

CIEL: You don't think it's better for the baby that we have a friend, someone we know and trust, to stay with her? Instead of some stranger?

JAY: A stranger might be here right now. (CIEL doesn't want to start this now. She heads back to the kitchen to get her pump) So, is she coming? Over?

CIEL: No! I don't know!

JAY: Ciel, we're never gonna be able to move out of this one-bedroom apartment unless I get a job and start making some /

CIEL: (turning around) I wasn't volunteering you to stay home, Jay.

JAY: You're gonna stay home? (long silence, heavy sigh) *Fine*, I'll blow off my interview.

CIEL: That's not what I'm saying, Jay. I know how anxious you are to get back to work.

JAY: I think she's starting to notice me. Lately. You know what I mean? (CIEL doesn't know the right response) For the first couple of months, I was just some guy who was hanging around being mommy's helper. But lately I can tell that she, like, I don't know, maybe knows who I am.

CIEL: Are you saying you want to be a stay-at-home dad? Because that would be even better than /

JAY: I don't know. It's a big commitment. It depends what happens at this interview.

CIEL: (heads for the phone) I'll call Georgia back. I'll call Shaefer, tell him I'll be a few min-utes late/

JAY: No, you go. (CIEL stops dialing) It's more important that you be there on time. It's your first day back. If you're late, Shaefer's gonna leap to all kinds of conclusions, about how you're not committed to the job / (CIEL stuffs the report in her bag and picks up her keys)

CIEL: If I leave now, I can print my pie chart at the client's office.

JAY: What floor are they on?

CIEL: The 275th or something like . . . I have it (fishes through her purse for her date book)

JAY: They only go up to 110.

CIEL: When I was at NYU, they had these old-fashioned elevators in the main building that could fit like 30 people and you had to shout over everyone's heads what floor you wanted: 7, please; 11 please; 13. . . And somebody would inevitably say "The moon, please." Typical freshman humor . . . but sweet, really. Whenever I'm in the towers, I think about that. I want to say it. "The moon, please." (finds her datebook) 95th floor. (slams the datebook shut and kisses JAY) Thank you, honey. Good luck on your interview. I'll call you after lunch. (opens the door) I'll call Georgia right now!

JAY: (indicating the baby) Sssh! (CEIL waves good-bye and exits. JAY dials the phone)

CIEL: (walking back in) I forgot the pump.

JAY: (into phone, tentative) Hi Kathy, this is Jay Coleman, I have a 9 A.M. interview and I'm going to be a few minutes late. Sorry for the inconvenience. Okay, thank you. Bye.

(CIEL with the pump on her shoulder waves at JAY as she puts her hand on the doorknob)

CIEL: (whispering) Bye again.

JAY: You look happy.

CIEL: (CIEL walks back to him) What? (on edge) What did you say?

JAY: You look happy. You look psyched to be going to work.

CIEL: What do you mean by that? I look happy to be going to work? Are you saying you don't think I have conflicted feelings? (steps closer to avoid yelling) How dare you accuse me of /

JAY: Accuse?!

CIEL: Our daughter's not even 3 months old yet! She's still half moosh and I have to leave her for ten hours a day! You think I want to go back to work? (beat) You don't have a job, Jay. How can I even fantasize about staying home with her when you're not bringing in any /

JAY: How am I supposed to make any money if I can't even go to a job interview on time.

CIEL: (slams down her bag) Go to your interview. Go. Go! I'd love to quit my job. I'll call Shaefer right now -- tell him to pitch to a client without me. (JAY can't tell whether to take her seriously) Go to your interview, Jay.

JAY: (after a pause) All right. (slowly gathers his stuff) Are you gonna call Georgia?

CIEL: Don't worry about it. Maybe I'll call her, maybe I'll stay with the baby myself. Maybe I'll get fired, maybe Shaefer will be completely sympathetic. Who knows?

JAY: (tries to kiss her before he leaves) I'll see you later.

(CIEL watches him leave. Exhales. Her mind races-what has she gotten herself into? Walks into the bedroom and looks at the baby. She picks her up gingerly, hoping not to wake her and rests her against her shoulder. Inhales her scent deeply. JAY comes back into the apartment. She eases the baby off her shoulder and lowers her back into the bassinet. Makes sure the baby doesn't wake then walks into the living room)

CIEL: Jay...?

JAY: I'm sorry, you're right. It was totally insensitive of me to accuse you of not feeling ambivalent about going back to work. (slight pause) You have worked so hard to get to your position and you deserve to come back with a bang. Yes, you're a mother but you're also the *best* vice president they have. (long pause. Takes off his tie and shoes) How many ounces of milk do we have in the freezer? I think I saw at least 5 or 6 of those bags and those are each 8 ounces. That'll get us through the day. Do you know where the Bjorn is? It's such a beautiful day, I was thinking of taking the baby out to the park. Maybe even see if she likes the swing /

CIEL: You're forcing me to go to work.

JAY: (now he's mad) What!?

CIEL: You're, like, pushing me out the door. And you have the nerve to talk about what a great day you're going to have with the baby while I'm locked in my office!

JAY: Ciel, you should have seen your face light up when you were walking out the door knowing you were going to work all day.

CIEL: Jay, just because you're too scared or, or, or lazy /

JAY: You're worried that your new mommy friends are going to think you're a terrible mother just because you like to work. Face it, Ciel, you're a workaholic. You love it.

CIEL: (rage causing volume) How dare you tell me I love to work. I have to work /

JAY: (simultaneously) The status, the power /

CIEL: This is the third job interview you've blown off.

JAY: Even when I had a job you were working all the time. You didn't even want to take the full three months off! (their voices rise)

CIEL: That was before I had the baby /

JAY: Oh, so, what? You've had a personality transplant since you gave birth?

CIEL: You don't think giving birth is a transformative /

JAY: You've been working this whole time from home! You've been preparing this pitch for months!

CIEL: It's my account!

JAY: (simultaneously) You couldn't stomach the idea of Shaefer giving Grace Chan this account.

CIEL: Grace Chan couldn't deliver this account if it was a pepperoni pizza. I did all the leg work, I developed the relationships, and I deserve the damn commission /

JAY: So, go! (after a pause, CIEL grabs her bag and hooks it onto her shoulder)

CIEL: (calmly) I am the youngest person in my position. I am the only woman, and I got where I am because my work is excellent. Just let me nail this account and . . . and then we'll / (the baby starts to cry. They look at each other, then start for the room)

JAY: I'll get her

CIEL: No, I'll get her. (they stop)

JAY: If you pick her up, she's going to freak out when you leave. (cell phone rings) That's your phone.

CIEL: What time is it?

JAY: 8:35. If you take a cab, you could be there before nine.

(CIEL looks at JAY then continues toward the baby's room. The cell phone continues ringing. She picks up the baby and nestles her into her chest. The baby wails)

CIEL: Okay, it's okay. Sshhhh . . . Thatta girl. Mama's here. (exhales and looks up. There's so much to lose -- She rests her head against the baby's and looks at JAY) Mama's gonna stay.
```

---

## IC-0846: Mother for Hire

- Title: Mother for Hire
- Author (byline): Linda Lee Bower
- Work: More One-Act Plays for Acting Students
- Publisher: Meriwether Publishing
- Publication date as stated: July 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ANDY, SALLY
- Teaser before the introduction: No
- Spoken words (computed): 1371
- Already set (do not supply): none

### Source block (context only)

```text
Author: Linda Lee Bower
Book: More One-Act Plays for Acting Students
ISBN: 1566080878
Publisher: Meriwether Publishing
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
ANDY: I can understand literature, symbolism, allegories, imagery, syntax and elliptical construction, but for the life of me I cannot understand why women love babies.

SALLY: How in the world can a man want THREE degrees in God knows what and not want a son?

ANDY: I really think it’s genetic…that motherly instinct has practically ruined the female mind.

SALLY: Maybe it’s a control issue….men can control themselves-their education- but they don’t have power over when a baby cries.

ANDY: If she wants one so bad why doesn’t she just become a…

BOTH: “Mother for Hire”

SALLY: By Linda Lee Bower.
```

### Performance text (classify this)

```text
(ANDY is sitting at the desk, writing, munching potato chips and drinking cheap wine. SALLY breezes in, carrying a large pizza box.)

ANDY: (Without looking up) Well, it's about time. I had about given you up for lost.

SALLY: I had to work late, and then-

ANDY: I hope Pratt and Wiggins didn't work your poor fingers to the bone. This paper is due tomorrow, so I'll need you to type it for me tonight.

SALLY: What's this one on? The hidden symbolism of the witches in the ninety-ninth verse of the Canterbury Tales?

ANDY: Do I detect a touch of scorn for my scholarly pursuits? (He now catches the smell of the pizza and looks up.) At least you brought something to eat. I'm starving. (He gets up, grabs the box, takes it to the table, and opens it.) Wow! That is some pizza.

SALLY: All twelve toppings - double.

ANDY: You must have robbed a bank on the way home.

SALLY: It's a celebration!

ANDY: Did you get a raise?

SALLY: Better than that.

ANDY: What could be better than a raise? I have to buy lots of books this semester.

SALLY: I'm going to be a mother.

ANDY: What?

SALLY: I'm going to have a baby.

ANDY: Sally, that is not cause for celebration.

SALLY: It is for me.

ANDY: Honey, we have been over that before. It's just not the right time.

SALLY: Will it ever be the right time for you? First you wanted to finish your B.A. degree. Then your M.A. degree. and now you are on your Ph.D. degree. What will come next? The Zh.D. degree in Esoteric and Unintelligible Poetry? Are you ever going to actually enter the working world? You are prepared for nothing except life in medieval England.

ANDY: Aw, come on. I do work.

SALLY: When?

ANDY: I teach two classes.

SALLY: In what?

ANDY: Medieval English Literature.

SALLY: Exactly.

ANDY: I suppose you want me to be a Wall Street tycoon.

SALLY: Not necessarily.

ANDY: Listen, you have gotten to be pretty uppity since you went to work for that brokerage firm.

SALLY: What's wrong with being successful?

ANDY: I'm not going to sell my soul for money. I suppose you want me to wear a three-piece suit, too.

SALLY: You don't even want to get married.

ANDY: We just can't afford to have a baby now.

SALLY: You don't have to worry about a thing. You won't have to pay for it, because it isn't your baby.

ANDY: You're going to have a baby and it isn't mine?

SALLY: Yes and no.

ANDY: Which is it?

SALLY: Yes I'm going to have a baby, and no, it isn't yours.

ANDY: Whose is it?

SALLY: Mr. Wiggins.

ANDY: Mr. Wiggins? Your boss? SALLY Yes.

ANDY: I'll kill you.

SALLY: Don't be silly. I'm not even pregnant yet.

ANDY: I must be missing something. I thought I understood English pretty well.

SALLY: All you have is book learning. You don't have any common sense.

ANDY: Well, will you kindly elucidate.

SALLY: I'm going to be a surrogate mother.

ANDY: A surrogate mother?

SALLY: Yes. Mr. and Mrs. Wiggins have decided to have a baby. But Mrs. Wiggins isn't tall enough.

ANDY: Tall enough for what?

SALLY: Don't be vulgar.

ANDY: Well, do they do it standing up?

SALLY: They want a tall baby.

ANDY: So he'll have to duck his head when he enters the world?

SALLY: I mean, they want him to grow up to be tall. Psychologists say that tall men get more respect in the business world than short men.

ANDY: (Looking down at himself and surveying his unimpressive stature) Oh?

SALLY: And besides, Mrs. Wiggins doesn't have time.

ANDY: Time for what?

SALLY: Don't be vulgar.

ANDY: I'm not being vulgar. I'm all agog to learn the new technology.

SALLY: Well, if you'll just let me tell you how it happened.

ANDY: I'm all ears.

SALLY: Mrs. Wiggins had an appointment to come to the office this afternoon.

ANDY: They do it by appointment?

SALLY: Andy!

ANDY: It looks like Mr. Wiggins is the one who doesn't have time, if his wife had to make an appointment to see him.

SALLY: She has a high-powered career herself, and they have to coordinate their schedules. Anyway, she came to the office this afternoon, and that's why I'm a little late.

ANDY: Why? Did you have to power up the Xerox machine?

SALLY and ANDY: Don't be vulgar.

SALLY: She wanted to interview me. She likes me, and I fit themcharacteristics they want.

ANDY: Your typing speed?

SALLY: My height. And also my athletic abilities, particularly my great tennis game.

ANDY: They want a tall baby who plays tennis.

SALLY: Mr. Wiggins says that a good tennis game is a big advantage for a stockbroker. You know, to play with clients, and get to meet people - potential clients - at the tennis club.

ANDY: And how much more income per year does the tall baby get for his tennis game?

SALLY: More than your entire annual salary, I'm sure.

ANDY: And I suppose this tall baby has already been registered at the Harvard Business School.

SALLY: Mr. Wiggins is an alumnus.

ANDY: And what if this tall baby doesn't want to go to Harvard, or be a stockbroker, or play tennis either?

SALLY: Well, he will have all the advantages, and Mr.Wiggins will groom him, so why wouldn't he?

ANDY: What if he wants to be - heaven forbid - an impractical English Ph.D. candidate?

SALLY: Horrors.

ANDY: I'll kill you.

SALLY: Don't be silly. Anyway, that is too far away for me to deal with. I'm excited about today. I'm going to have a baby!

ANDY: All this came about today?

SALLY: Oh, no. Mr Wiggins asked me about it a month ago.

ANDY: I always knew Wiggins was a pervert.

SALLY: And if everything works out OK - and there is no reason why it wouldn't - I can do it again.

ANDY: I don't even want you to do it once.

SALLY: Well, that's just too bad. You think your Ph.D. is so all important that you can't get married and have a baby. I'm going to have one anyway, so there.

ANDY: Why didn't you tell me you wanted a baby so much? And that you wanted to get married?

SALLY: I have told you many times.

ANDY: When?

SALLY: All I ever got was "We can't afford it," or "It just isn't the right time."

ANDY: But

SALLY: If I put it in the language of Chaucer would you understand? "Whan that Aprill with hise shoutes soote/ The droghte of March hath perced to the roote."

ANDY: But what good will it do you to be a surrogate mother? As soon as you have the baby, you will give it to somebody else.

SALLY: I'm doing it for the money.

ANDY: How much are they paying you?

SALLY: They will pay all my medical expenses, plus twenty thousand dollars.

ANDY: Twenty thousand dollars?

SALLY: All I need to do is have several babies for other women, and then I will have lots of money and I can afford to have my own baby.

ANDY: Several?

SALLY: Sure.

ANDY: Like how many?

SALLY: I'm young. I can have babies for ten years, at least. At the rate you're going it will be ten years before you are ready to get married and have a baby. I can get in plenty of practice.

ANDY: Listen, Sally, can't we think about this a little?

SALLY: I have already thought about it.

ANDY: Just like that?

SALLY: Yes.

ANDY: How can you just do it with a strange man?

SALLY: Mr. Wiggins isn't a stranger.

ANDY: You've done it with him before? I'll kill you.

SALLY: For heaven's sake, Andy. We don't actually do it.

ANDY: oh. How does it work, then?

SALLY: It's done with artificial insemination.

ANDY: I don't care. It's-

SALLY: They want to start it as soon as possible. So I have to keep a temperature chart to determine when I ovulate so I can go to the fertility clinic on the right day. And, I'm sorry to tell you, we can't have relations for a while, so there won't be any, um, interference.

ANDY: For ten years? How can you do this to me?

SALLY: What do you care? You're always worried - "Did you put it in?" So afraid I might get pregnant. Well, I am going to get pregnant, but you don't have to worry about it.

ANDY: Are you really going to get twenty thousand dollars?

SALLY: Yes, isn't it wonderful!

ANDY: Ah... well, then, in that case, perhaps

SALLY: But you aren't going to get any of it. I'm going to save it for my future baby.

ANDY: And whose baby will that be?

SALLY: Well, it depends If it still "isn't the right time" for you, then maybe I will go to a sperm bank.

ANDY: And where does that leave me?

SALLY: Where you have always been. Up in your ivory tower.

ANDY: Does this mean you won't type my papers anymore?

SALLY: I'm so excited. Mmmm. Let's eat the pizza before it gets cold. (She separates a wedge and begins to eat.)

ANDY: I'm not hungry anymore. (Blackout)
```

---

## IC-0847: The Mountaintop

- Title: The Mountaintop
- Author (byline): Katori Hall
- Work: Not specified
- Publisher: 978-0822226031
- Publication date as stated: Aug 2013
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CAMAE, KING
- Teaser before the introduction: Yes
- Spoken words (computed): 1898
- Already set (do not supply): none

### Source block (context only)

```text
Author: Katori Hall
ISBN: Dramatists Play Service
Publisher: 978-0822226031
Date (Month/Year): Aug 2013
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: April 3, 1968 -- the last day of the Reverend Dr. Martin Luther King, Jr’s life.

ACTRESS: He’s at the Lorraine Hotel, room 306 in Memphis, Tennessee, working on yet another powerful speech and orders a simple cup of coffee from room service.

ACTOR: But with his coffee arrives a mysterious maid, bringing him much more than a late-night beverage.

TOGETHER: The Mountaintop by Katori Hall
```

### Performance text (classify this)

```text
CAMAE: (Pg 14-16) Walkin’ will only get you so far, Preacher Kang.

KING: We’re not just walking: we’re marching.

CAMAE: Whatever it is, it ain’t workin’.

KING: It doesn’t work when you have trifling Negroes who call themselves using a peaceful protest to get a free color television. Just last week me and my men organized a march for –

CAMAE: Them garbage men?

KING: (correcting) Yes, the sanitation workers. Must have been thousands upon thousands of people there. Well, we hadn’t walked but one block before we heard the sound of glass breaking. I was swept up in a tornado of arms, legs, coughing mace. I didn’t wanna leave those people, Camae . . . but my men pushed me into a passing car, and . . . I looked through that back window and saw such blessed peace descend into chaos (beat) Don’t they know . . . We’re marching for a living wage . . . not a damn color TV! It just gives these police an excuse to shoot innocent folks. Like that boy . . . that sixteen-year-old boy they shot. (quietly to himself) Larry Payne. I’ll never forget his name . . . After the march, the papers called me ‘Chicken a la King.” Said I was a Commie coward that leaves other people to clean up my mess. “Martin Loser King . . “

CAMAE: Seem like times been a little rough on you. Folk done got tired through, Preacher Kang. (sighs) Like I say, walkin’ will only get us so far –

KING: (Pg 16 – 19) (annoyed) Well, killin’ will get you hung. So what are we supposed to do?

CAMAE: I got a plan. But . . . I’m just a woman. Folk’ll never listen to me.

KING: So if you were me, what would you do?

CAMAE: (stands on one of the beds. Throughout her speech King is her congregation, egging her on with well-timed sayings like, Well! Preach! or Make it plain! Camae with a King voice) We have gathered here today to deal with a serious issue. How do we deal with the white man? I have told you that the white man is our brother. And he should be treated as such. But it is hard to do this when our brother beats his fist upon our flesh. When he greets us with ‘Nigger’ and ‘Go back to Africa.’ We have walked. We have been drowned by hoses. Our dreams washed away. We have been bitten by dogs. Our skin forever scarred by hatred. To this I say, my brethren, a new day is coming. We are fighting to sit at the same counter, but why, my brothers and sisters? We should build our own counters. Our own restaurants. Our own neighborhoods. Our own schools. The white man ain’t got nothin’ I want. (steps down). Well, that’s what I would say . . . if I was you.

KING: White folks don’t seem to want to listen. (beat) Sometimes I wonder where they get this hatred of us from. So many white people hate us, Camae. Bombin’ folks’ homes. Shootin’ folks . . . blowin’ up children.

CAMAE: Last time I heard you was preachin’ ‘everybody the same.’ Negro folk. White folk. We all alike. What one thing we all got in common? (beat)

KING: (searches hard to come up with an answer) We scared, Camae. Scared of each other. Scared of ourselves. Scared of losin’ somethin’ that they’ve known their whole lives. Fear makes us human. We all need the same basic things. A hug. A smile. (beat-- looks her up and down) Not too many maids spouting off well-formed diatribes like that. You made it sound real pretty, but nobody can make it pretty like me. I’ve been doing this for years, darlin’. Gonna be doin’ it till the day I die. (begins to get short of breath)

CAMAE: (Pg 21) Speak by love, die by hate. (pause) We all have weaknesses, Preacher Kang. I’m sho’ you got yo’ own. (beat) For what it worth, I know God like you. She told me She like you. (Pg 22-23) (King stumbles holding his chest) You awright?

KING: I can’t breathe . . . can’t, can’t breathe . . .

CAMAE: Micahel? MICHAEL!! Michael, just breathe!

KING: (soto voice) can’t . . . can’t . . . (the thunder in King’s heart stops. Silence. They breathe together slowly together) You called me Michael . . . How would you know that?

CAMAE: Calm down, Preacher Kang. I didn’t mean to call you out you name.

KING: But that is my childhood name. How do you know my real name? (backs away from her; softly) So, you one of them, huh?

CAMAE: I’m so sorry. I never wanted to do this.

KING: (shaking his head) A spy. Get out! I said GET OUT. (enraged, King searches for bugs. He yells yelling at no one in particular) What, y’all think you can trap me! Record me with a woman! Well, you’re not going to catch me!

CAMAE: Preacher Kang, calm down!

KING: You think you can break me! Well, you can’t break me! (Grabs Camae by her arm and pulls her towards the door)

CAMAE: Preacher Kang, you’re hurting me!! You wrong! You wrong!

KING: (Pg 24-25) How do you know so much about me! WHO IN THE HELL ARE YOU?

CAMAE: (gives him a look as if she is communicating to him telepathically)

KING: You’re. An. Angel? Wow. An angel?

CAMAE: Yes. I’m here to take you to the other side.

KING: (Suddenly very serious) I’m not going to hell, am I?

CAMAE: Naw! Heaven is we’re we headed. (beat) Sorry I called you Michael. Not too many folk prolly know that ‘about you. God said yo’ Christian name calms you.

KING: You’re really an angel? But . . but why’d God send you? (pause) Why He -

CAMAE: She!

KING: She send you?

CAMAE: (Pg 26-27) Believe you me I ain’t want this job. First day? Bring you over? The Kang? But God been getting’ these prayers from a littl’un named Bunny. (in a little child’s voice)

‘Please, God, don’t let my daddy die alone.’ (in her regular voice) Well, it just ‘bout broke my heart. I just had to come . . .

KING: You know her nickname . . . my sweet Bernice. My baby girl spoke to you?

CAMAE: Her prayers are powerful. I don’t like chiren too much, but she . . . she something.’ (pause) Look, I know you afraid, Preacher Kang . . . You should be.

KING: (with total calm) You talk about fear, Camae, well . . . I have felt fear. Felt it even when I stood in front of my own congregation. Sunday mornings have been the mornings I am most afraid. ‘Cause in this country, in America, the tall tree is felled first. Tall trees have more wood to burn, Camae. We are the sacrifice.

CAMAE: You been knowin’ I was comin’, haven’t you?

KING: Yes. In my darkest hours, I’ve even prayed for you. Been so many death threats that some nights I have asked God, ‘Please just get it over with.’ Fear, Camae, is my best friend. Cause I know if I’m still afraid, then I’m still alive.

CAMAE: Tomorrow. When it time, you gonna have to take my hand.

KING: Tomorrow? But I’m not ready to die. I still got so much work to do. (picks up papers from his desk and reads aloud) Why America is going to hell –

CAMAE: Preacher Kang, you gone have to put that down.

KING: (in his “King voice”) A country that sends its boys to bathe little-bitty brown babies in the blood of our greed is headed for a crossroads of conscience . . . America, my sweet America, is surrounded by rising water, waiting to drown. But the children of the Nile will rise, they will RISE! Can I get an Amen?

CAMAE: AMEN!!

KING: I need to be alone to finish my sermon so. . . you gone have to fly on away. (returns to his sermon) (Pg 28) If only they could see that love is the most radical weapon there is. But they won’t listen. Even my own men – ‘You splittin the movement, Martin! You can’t focus on war, and poverty, and Negroes!’ (to Camae) Just a little more time, just a little bit more . . .

CAMAE: -- this hard on me.

KING: Hard on YOU? What about on me? On my family? On the movement? HAS GOD THOUGHT ABOUT THAT?!

CAMAE: (Pg 29-30) What about yo’ mens? Can’t they see it through?

KING: They don’t dream the same dreams I do, Camae. They think I’m crazy to dream this big. Bbut how can we fight the war in Vietnam but not the war against Negroes in our streets? How can we try to put a man on the moon, but not feed starving children in Mississippi? There’s just so much I gotta do. So much I haven’t accomplished.

CAMAE: Well, let me tell you something, Preacher Kang. Like most men, you ain’t gone be able to finish what you started.

KING: My house has been bombed! I have been pelted wit’ rocks. Spit at. Pummelled. I have been stabbed in my chest. And I walked away. Alive! Tell me I ain’t got favor wit’ God.

CAMAE: You just a man, baby. You’re not God, though some folk’ll say you got mighty close. Honey, I know all about your trials and tribulations. I done read yo’ blessings file. It bigger than yo’ FBI file and bigga than the Bible. I know it might be hard for you to leave this life . . . But you ‘bout to burn out, stuperstar. You gone need to pass off that baton.

KING: (Pg 35) Camae? . . . . (beat. King dissolves into tears) I’ve been prayin’ that it would stop. (Camae comforts him) That it would all go away. I never wanted to do this. I just wanted to be a minister in my small church. That was enough . . .

CAMAE: But God had bigger plans for you. (Pg 36-37) Powerful the man that get more done dead than alive.

KING: I don’t want to be a martyr.

CAMAE: But the suit fits you well. Tomorrow, you’ll be a man-made martyr. A saint!

KING: Don’t call me that. I’m a sinner, not a saint. I’m not deservin’ of the title.

CAMAE: You think I am? Honey, I’ve robbed. I’ve cheated. I’ve failed. But what I’m ashamed of most is, I’ve hated. Hated myself. Sacrificed my flesh so that others might feel whole again. I thought it was my duty. Last night, in the back of an alley I breathed my last breath. A man clasped his hands ‘round my throat. I stared into his eyes and saw the hell this world had put him through. The time he saw his father hang a man. The time he saw his mother raped. I felt so sorry for him. I saw what the world had done to him, and I still couldn’t forgive. I hated him. When I passed to the other side, God stood before me. I was just weepin’ at her feet. Beggin’ her not to throw me down. All that sinning.’ All that hatred in my heart. But I heard Her say. “I got a special task for you and if you complete it, all your sins will be washed away.” And my task was you. You have the biggest heart I done ever knownt. You have the strength to love those who could never love you back. If I had just a small fraction of the love you have for this world, then maybe, just maybe I could become half the angel you are.

KING: Will I die at the hands of a white man, too?

CAMAE: Yes. Speak by love. Die by hate.

KING: (Pg 38-41) Is the future as beautiful as you?

CAMAE: Yes . . . and it’s as ugly as me, too. It might break your heart.

KING: I wanna see it. I will go willingly into your arms, Camae. If you just let me see these dreams I’ll never ever see.

CAMAE: (considers, then) Let’s take you to the mountaintop.

(King nods, gulping back tears – He sees and reacts to the following as Camae narrates – she exits
scene during the last refrain, leaving King to speak his last passage alone)
The Prince of Peace. Shot. Black raised fists
His blood stains the concrete outside I’m black and I’m PROUD!
Room 306 The baton passes on
A worker wipes away the blood but not
Drive-bys, Iraq,
before
NBA, high-paid slaves
Jesse baptizes his hands on the balcony
Amerian flags
The baton passes on.
And black presidents!
Memphis burning, DC burning
The baton passes on
Cities burning, Vietnam burning
Coffins coming home The Towers sigh
Another Kennedy killed The world turns gray
The baton passes on September 11th
One bright morning day
Robben Island sets Mandela free
The baton passes on
Rodney King screams:
‘Can’t we all just get along?’

KING: (Pg 42) (alone to the audience) Well . . . nobody said it was gonna be easy. The baton may have been dropped. But anyone can pick it back up. This baton is no longer the burden my image can bear. For you are the climbers, the new carriers of the cross. I beg you, don’t give in and toss it off. The Promised Land is so close, and yet so far away . . .
```

---

## IC-0848: Mr. Marmalade

- Title: Mr. Marmalade
- Author (byline): Noah Haidle
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: January 2006
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MR. MARMALADE, LUCY, SOOKIE, EMILY, GEORGE, LARRY
- Teaser before the introduction: Yes
- Spoken words (computed): 1163
- Already set (do not supply): none

### Source block (context only)

```text
Author: Noah Haidle
ISBN: 978-0822221425
Publisher: Dramatists Play Service
Date (Month/Year): January 2006
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Lynda Barry, an American cartoonist, author and teacher once said: “We don’t create a fantasy world to escape reality,

ACTRESS: “We create it to be able to stay . . . and to understand what otherwise would be intolerable.”

ACTOR: Lucy is a young girl with a very active imagination. Her best friend is Mr. Marmalade. Who really doesn’t have too much time for her.

ACTRESS: Together they create an imaginary world that often echoes too closely the reality that Lucy is struggling to comprehend.

ACTOR: As our selection opens, Lucy’s mom has left yet again for an evening on the town and Lucy is left in the care of Emily, the babysitter.

TOGETHER: Mr. Marmalade by Noah Haidle
```

### Performance text (classify this)

```text
Suggested Characters: Actress: Lucy Actor: Sookie (Lucy’s Mom), Emily (the babysitter), George, Larry, Mr. Marmalade

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

A living room in New Jersey. Lucy is playing with Ken and Barbie when Mr. Marmalade appears. He’s very well dressed. Suit, briefcase, nice shoes. Lucy hums as she plays with her dolls. (Music is a way for Lucy to cope with being alone most of the time) Suggested song: Pure Imagination from Willy Wonka & the Chocolate Factory – *See link at the end of this selection for video of this song.

MR. MARMALADE: (Pg 5) Good evening.

LUCY: (Pg 39) Mr. Marmalade! (Pg 5) I thought you weren’t coming.

MR. MARMALADE: I carved out some time.

LUCY: Thirty minutes?

MR. MARMALADE: Ten.

LUCY: That’s not very many.

MR. MARMALADE: It’s the best I could do.

LUCY: We’d better get started.

MR. MARMALADE: What is it today?

LUCY: House.

MR. MARMALADE: (he opens his briefcase and whips out a tea set) Whenever you’re ready.

(Pantomimes preparations for an elaborate tea party)

LUCY: Would you like a cup of coffee?

MR. MARMALADE: Have we started?

LUCY: Yes.

MR. MARMALADE: I would love a cup of coffee. (Lucy begins to prepare a cup when Mr. Marmalade’s beeper goes off – Lucy creates this sound effect) (Pg 8) Oh, *shoot*, my beeper.

LUCY: You’re not going back to the office tonight, are you, dear?

MR. MARMALADE: Not play beeper. My real beeper. (Actor moves “off stage” and becomes Sookie, Lucy’s mother)

SOOKIE: (Pg 6-7) (Offstage) Lucy!?

LUCY: Mom, I’m busy.

SOOKIE: (Offstage) Lucy!? What are you doing?

LUCY: Mr. Marmalade just got home from the office, and he has to leave in like five minutes so I’d greatly appreciate it if you left us alone, [MOM]!

MR. MARMALADE: (Pg 8) I have to go.

LUCY: You said ten minutes.

MR. MARMALADE: I know I did. I’m sorry. I have to go. Goodbye. (He disappears)

LUCY: (sadly) Goodbye.

SOOKIE: (Offstage) Babysitter’ll be here in half an hour. Can you hold down the fort until then?

LUCY: Which one is it?

SOOKIE: (Offstage) Emily.

LUCY: Uggghhhh!

LUCY: (Pg 10 – 11) (on the phone) You gotta go? Are you sure? Okay. No. I understand. Ciao.

(Hangs up phone)

EMILY: Who were you talking to? Was it Mr. Marmalade?

LUCY: How do you know Mr. Marmalade?

EMILY: We hang out all the time. We go to the mall and get our nails done.

LUCY: Mr. Marmalade does not get his nails done!!!

EMILY: Chill out. We don’t go to the mall. Your Mom told me about him.

LUCY: What’d she say?

EMILY: Says he’s a deadbeat.

LUCY: He’s very busy. He’s a very important man.

EMILY: Don’t matter how important he is. He’s gotta make time for you. My boyfriend George used to say he was too busy to hang out with me.

LUCY: What’d you do?

EMILY: I stopped hooking up with him.

LUCY: Then did he have more time for you?

EMILY: You better believe he did.

LUCY: . . . Let’s play Tea Party.

EMILY: (Pg 15-16) (Rolling her eyes) When I was your age I liked to play line.

LUCY: How do you play line?

EMILY: You just get in a line and pretend to be waiting for something. I like to wait for the bus.

LUCY: That doesn’t sound very fun.

EMILY: Do you want to try it?

LUCY: I guess so.

EMILY: Here, you get behind me. (They stand in a line) What are you waiting for?

LUCY: The butcher?

EMILY: No. We’re at the bus station. What bus are you waiting for?

LUCY: The number seven.

EMILY: There is not bus number seven, Lucy.

LUCY: Then I guess it’s going to be a long wait.

EMILY: I don’t want to hurt your feelings, but you’re not very good at Line. (The doorbell)

LUCY: Who is that?

EMILY: It’s George, my boyfriend.

LUCY: George isn’t supposed to come over.

EMILY: We’re going to do our math homework. (She puts on lipstick and fusses with her hair) How do I look?

LUCY: Easy.

EMILY: Good. (She adjusts her breasts, trying to make them look bigger. The doorbell rings again) Coming. I’m coming! (Off stage . . . Opens door) . . . You brought Larry?

GEORGE: (Offstage) Larry, Lucy. Lucy, Larry. Have fun, kids! (Sheepishly Larry enters. He’s five years old)

LARRY: I’m Larry.

LUCY: Nice to meet you, Larry. (She kisses him on the cheek)

LARRY: What are you doing?

LUCY: It’s how people greet each other. . . . (Pg 19-20) [so] do you want to play Doctor? (Larry nods, speechless) What seems to be the problem?

LARRY: Nothing. I feel fine.

LUCY: No, not what’s really the matter. Pretend.

LARRY: (Pretending to be in great pain as he grabs a body part) Ohhhhh. I’m having chest pains.

LUCY: That’s very serious. You need a heart transplant. Let’s get you that new heart! (The pair pantomime an elaborate heart transplant procedure – kid style based on what they’ve obviously seen on television shows, complete with sound effects) How’s that new heart?

LARRY: I don’t have the chest pains anymore.

LUCY: You’ve made a complete recovery! (Pg 16) (Larry walks around the room) Hey!

LARRY: This place is pretty nice. So you live here with your parents and everything?

LUCY: It’s just me and my mom. My dad, he divorced my mom when I was two, or something.

***** Flashback in the world of pretend – a baby cries in the kitchen.***** In this flashback, Lucy plays her MOM and Mr. Marmalade plays her DAD

MR. MARMALADE: (Pg 41-43) Will you shut that kid up?

LUCY: (Offstage) I can’t hear you, honey. The baby’s crying.

MR. MARMALADE: I know the baby’s crying. I can hear the baby crying.

LUCY: (Offstage) Just a second! (She comes in carrying a baby wrapped in a blanket - crying)

MR. MARMALADE: Put a muzzle on that kid!

LUCY: She’ll be back asleep in a minute.

MR. MARMALADE: But then she’ll be awake in another minute. Go back in the kitchen! I can’t hear myself think.

LUCY: I’m so sorry. (to baby) Shhhh. Shhhh. Be quiet. Be quiet.

MR. MARMALADE: Who’s idea was it to have a kid anyway?

LUCY: She’ll be quiet in a second. Shhhhh. Shhhhh.

MR. MARMALADE: You should have had an abortion.

LUCY: Don’t say that?

MR. MARMALADE: Why not? That kid is killing me.

LUCY: It was your idea to have a big family.

MR. MARMALADE: Like hell it was.

LUCY: You said you wanted it all. A house with a white picket fence. Kids running around.

MR. MARMALADE: I never said that.

LUCY: Yes, you did.

MR. MARMALADE: You’re putting words in my mouth! (he hits her in the face, Lucy reacts – long pause) I can’t take this anymore. I’m leaving.

LUCY: You can’t leave! I won’t bother you. I won’t make a sound. I promise. . . . . I won’t nag you about your drinking. Do you want another beer? I’ll go get you another beer.

MR. MARMALADE: It’s too late. *****Flashback ends*****

LUCY: (Pg 22-24) (to Larry) You have to go.

LARRY: What? Why?

LUCY: Because I said so.

LARRY: Did I do something wrong?

LUCY: No, I can’t explain. I’m sorry. You just have to leave. Right now.

LARRY: Okay. I don’t understand. But I’ll go anyway.

LUCY: I shouldn’t have played Doctor with you. I shouldn’t have led you on.

LARRY: Yeah. Okay. Maybe I’ll see you at school. (He exits.)

LUCY: Yeah. See you at school. *****Scene Change *****

(Alone, Lucy again picks up a doll and begins to hum)

MR. MARMALADE: (Pg 25-27) Good evening, [Lucy].

LUCY: (excited to see him) [Mr. Marmalade, what are you doing here?] I thought we were having brunch on Sunday?

MR. MARMALADE: Some time freed up tonight. Thought I’d drop by.

LUCY: [Oh . . . ] How was work?

MR. MARMALADE: *Freakin’* nightmare. You have no idea.

LUCY: (taken aback at his obviously drunken demeanor) Have you been drinking?

MR. MARMALADE: I had a few after work to unwind. You would too if you’d ever worked a day in your life.

LUCY: I wouldn’t know.

MR. MARMALADE: No, you wouldn’t. (Mr. Marmalade opens his briefcase. Takes out a [flask of alcohol and drinks] *note in the play this is a vial of cocaine* - substance has been changed here in consideration of high school performers.)

LUCY: (Scolding) Mr. Marmalade!

MR. MARMALADE: What? You want some?

LUCY: (taken aback) No. I don’t!

MR. MARMALADE: Suit yourself. (takes another drink) You sure? This is some good *stuff*. Hey, let’s play House. “Hey honey, I’m home!”

LUCY: (softly) No.

MR. MARMALADE: That’s when you say, “How was work?” And I say, “It sucked.” But somebody’s gotta provide for this family. (Silence . . . Lucy is near tears) [What?] You don’t want to play House with me?

LUCY: Not like this. Not when you’re [drunk].

MR. MARMALADE: (brandishing his flask) This is like a cup of coffee. I don’t even feel it. Hey, Lucy, I work twenty hours a day. (getting angry and reaching for Lucy) I want to play House!

LUCY: (avoiding Mr. Marmalade) I won’t play House with you.

MR. MARMALADE: (grabbing for her arm again) Then let’s play Doctor. Come here!

LUCY: Get out!

MR. MARMALADE: (calming down) Okay, okay. I’ll see you on Sunday.

LUCY: No, you won’t.

MR. MARMALADE: What?

LUCY: I don’t want to see you anymore. (the following lines overlap as the tension and volume rises)

MR. MARMALADE: What? What the *hell* you talking about?

LUCY: I don’t want to play House with you anymore. Or Doctor.

MR. MARMALADE: (angry, yelling) What the *hell* you talking about?

LUCY: (also yelling to be heard) I don’t want to play with you at all. (long silence) You’re a bad person. (growing in intensity with each sentence) You neglect me. I deserve a lot better than you, [Dad!] (long silence – Mr. Marmalade exits) (Actor re-enters scene as Larry)

LARRY: (Pg 29) (Sees that Lucy is upset) Are you okay? (Looks offstage) Who was that guy?

LUCY: He used to be my friend. His name’s Mr. Marmalade.

LARRY: That guy was your friend?

LUCY: People change. He used to be a good guy.

LARRY: Well, he’s not anymore.

LUCY: Larry? . . . . Do you know how to play House?
```

---

## IC-0849: 20 Questions and a Motive for Murder

- Title: 20 Questions and a Motive for Murder
- Author (byline): Stephanie Christensen
- Work: 20 Questions and a Motive for Murder
- Publisher: Mushroom Cloud Press
- Publication date as stated: September 1, 2021
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1824
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
Priscilla: Welcome to the mansion of Professor Singh. My name is Priscilla and might I say, the full moon lights up the garden in a rather ghastly way this evening. Aaaand you all look deliciously hungry! Gather round, dear dinner guests, but not too close, or you might uncover a dish you do not like. Gibby: (raises hand) I’ve never met a dish I didn’t like! Priscilla: Clearly, you chunky monkey! I mean, revered guest. Angel: Ummmmm… can I just say this is really weird? I thought this was an end-of-semester dinner hosted by Professor Singh. Who invited all of these (motions to audience) creepers here? Why are they watching us so closely? Frankie (eccentric, egotistical, hippie): They came for me… I’m dinner AND the show! Diego: (looks at Frankie with flirtatious smile) Dinner indeed… you’se several snacks, girl. I can never keep my eyes off you in class. You too, Angel! Angel: EW. Priscilla: Enough! You college students drone on and on with your incessant complaints. Who are you, Priscilla? What are we doing here? “I feel unsafe.” POPPYCOCK. Gibby (scared): I think I might leave now. Priscilla: Not without your meal, you won’t. Have you ever left without eating a meal? Angel: Stop with the over-eating jokes. Am I making jokes about your nasty face mole and forehead wrinkles? (sassy, unapologetic) Ooh. I guess I just did. Gibby: YEAH! Am I making jokes about (points to audience member) that person’s gnarly hair? Really, dude… heard of a shower? Frankie (spiritual): All locks are sacred locks! (turns to audience member) NEVER cut your hair, okay? NEVER CUT YOUR SACRED HAIR. Diego: Yo, look, it’s Professor Singh! Professor Singh: Hello, children. Welcome to my home and congratulations on your exemplary grades this semester. Gibby, an A- and awful final paper. Angel, a B minus, how awkwardly predictable. Diego, with the consistent C plus. And, of course, an F for Frankie.

Frankie: F for Frankie, or F for freakin’ awesome? Priscilla: F for failure at life. Professor Singh: You have each fallen under a unique subcategory of failure in my class. Gibby: Whoa, whoa, whoa, I got an A! Angel: And I got a B! Plus, I don’t think you’re supposed to say all of our grades out loud in front of each other, Professor. That’s kind of messy. Frankie: Bad vibes, dude… you’ve got institutional university sellout written all over your face. Gibby: Yeah, and if this is a celebration dinner, why am I the only one here with an actual good grade? Diego (gives Gibby an offended look): Hey?!? Professor Singh: Oh Gibby. You still think an A- is good? (motions to an audience member) Ask that overachiever “try-hard” in the audience if they think an A- is good. (asks audience member) Do you? Do your parents think an A- is good? Does it keep you up at night?!? Angel: Whoa, professor, I think you need to chill on harassing the bystanders. Priscilla: SILLY CHILD, the strangers in the audience are not bystanders! They are here to join the dinner party and be punished as well. Frankie: (gasps in excitement) Well, WELCOME, friends! Gibby: (gulps) Did you say punished? Diego (turns to an audience member, raises eyebrows): Dawg, I think she said we’re being punished… I’m not sticking around that. Professor Singh: Yes, Gibby and Diego, punished. This is a tradition of mine every semester… tonight, you, my loser students, will sit for dinner and a game of 20 questions. It will be a lovely evening of torture! Angel: Somebody needs to call University and report this. Professor Singh: Priscilla, will you please seat our guests and introduce them to the game, while that (points dramatically) audience member brings out the first course? Priscilla: Why of course, my liege!

Diego: Man, I want a servant at my beck and call like that. It would be nice if it were a pretty girl
though, not miss wrinkly mc-mole pants.
Angel: (sarcastic) One day, some woman is going to be so lucky to have you.
Diego: Hey, Frankie loves it when I flirt with her.
Frankie: well, frankly, I find peace and connection with all living creatures.
Diego: (indignant) But she likes me the most.
Priscilla: Stop the incessant whining! Now, while you all enjoy this appetizing soup starter…
Angel: (opening dish cover) Is this Cup of Noodles?
Priscilla: We will be starting our little game. One of you have been specially selected as
Professor Singh’s least favorite student, and tonight, using the game of 20 questions, we will find
out exactly who that is.
Gibby: Oh, MAN. This social setting is literally my worst nightmare.
Priscilla: So, how about we start with Diego? You must ask a “yes” or “no” question, and the
goal is to make Professor Singh to give you an identifying description of the FAILURE he has in
mind.
Diego: Uhhh alright… is it a guy or a girl?
Angel: That is not a yes or no question, Diego.
Diego: Yes it is… either he says, “yes, it’s a guy” or “no, it’s a girl.”
Angel: We’re never going home.
Professor Singh: Diego, you’ve lost your turn. Question number two is for Frankie.
Frankie: Hmmm… does this person have a spiritual connection with you?
Professor Singh: No. Question 3 for Angel.
Angel: That didn’t narrow us down at all, Frankie. Is this person a girl?
Professor Singh: Yes.
Priscilla: (to the audience) Now you gasp, audience.
Angel: YES?! That narrows it down to two of us!

Professor Singh: Well, looks like someone is smart after all. Question 4 for Gibby. Gibby: Uh… uh… (wiping sweat from forehead and armpits). I’m sorry about this. I sweat profusely when I’m nervous. Angel: You’re not even on the chopping block anymore! Gibby: I know, but all of these people are watching me! Oh, shoot! I just dropped some sweat into my soup. Can I get another one? Professor Singh: Gibby, you’ve lost your turn. Question 5, Diego. Diego: Uh… Is she hot? Frankie: (flattered, clutches chest) Thank you! (blows kiss at Diego) Professor Singh: Disgustingly inappropriate. No. Question 6. Frankie: (gives him a look) rude! Angel: it’s your turn, Frankie… can we just wrap this up? Frankie: Was this person in your class, Professor Singh? (Professor Singh stares at her deadpan) (Frankie stares back innocently, blinks inquisitively) Professor Singh: (looking at her like she is crazy, speaks slowly) Yes. You. All. Were. Priscilla: Alriiiiigghhht, I think we’ve had enough of round one! We have 14 questions left and are making very embarrassing progress, considering how easy this game is with four people. Angel: (to audience) Do any of you have a car? I want to get out of here but I carpooled with Gibby, and he looks too impaired to drive. Gibby (making nervous noises, wiping sweat off self): Uggghhh this is awful, this is awful… can I have more napkins? Priscilla: Please prepare yourselves for the main course. Angel, since you seem to have a problem with the game, will you come join me in the kitchen to prepare the entrée? Angel: Ah yes, I would love to help the waitstaff. My self-esteem wasn’t low enough already. Gibby: Uh, while they’re doing that, can we continue the game, Professor Singh? (eyes track them walking into the kitchen, he turns to whisper to the audience) I’m 99.99% positive that Frankie is his least favorite student. She was the one who got an F, and she almost never comprehends what we are saying. Frankie (spiritual, zoned off): What was that, Gibby? I was tuning out. Professor Singh: That is an classically predictable guess, Gibby. Would you like to lock it in as your final answer? Audience, what do you think? Lock it in? Diego: Lock it in! Lock it in! Lock it in! Gibby: (nervous, sweating) UHHHH… Uh… I don’t know! Now I’m nervous. I want to be sure… but let’s do it. Let’s lock it in! Professor Singh: WRONG. You had a 50/50 shot, and just as I should’ve known, you absolutely butchered it. You failure students are so predictable with your butchering. Angel (screams, running in from the kitchen): AHHHH! HELP ME, HELP ME! SHE’S TRYING TO BUTCHER ME! Priscilla (holding a butcher knife over her head): STAND STILL, ANGEL! YOU ARE THE MAIN COURSE TONIGHT. Diego: Whoa whoa whoa, get behind me Angel! And you put down the knife, crazy lady! Frankie: Stand back! Your negative energy is palpable in the air! Gibby: WHAT THE GIBLETS IS GOING ON? Professor Singh: Oh students… Angel is my least favorite, it is true. And that, Angel, is because you have had so much potential for improvement. You got a B minus in my class, but you have a brilliant, intuitive mind. You are just wasting it on other ventures. Angel: Your class SUCKED, Professor Singh! You made us do pre-homework before our homework and stay late after school to practice our public speaking! Like literal torture, every day of the week! (motions to audience) these people relate! Professor Singh: And you still managed to embarrass me. To pay for your lack of motivation, you will become an example. This might seem scary now, but one simple murder, and the rest of these fools will surely try harder in their next endeavors. Gibby: Uhhh I’m pretty sure I’ll just pee myself. Frankie: Me too. Diego: Too late for me.

Angel: Diego, really? I’m right behind you! Priscilla: Come on, silly girl, give in to your fate now! You can’t come to a big dinner party full of murderous strangers at a murderous mansion, and not expect us to have a motive for murder. Angel: (looking desperately at the audience) Ah, come on, these strangers can’t be that bad. They don’t want to see me murdered, right? Right?! Frankie: No offense, Angel, but they kind of look like they do. Priscilla: They came for a hilarious show, after all! And that they will get! Diego (runs up to audience member): Listen, listen. They said we’re all going to be punished, right? You’re going to be punished, we’re going to be punished. So we can’t let them kill Angel! We have to do something! Gibby (also speaking to audience): I’ve got a plan. Follow my lead. Frankie is going to start chanting a spell to distract Professor Singh, while we all distract that Priscilla witch. Look, Frankie is starting now! Frankie (spiritually humming and moving arms up and down): Ooh chaka- laka, ooh chaka-laka! I enchant you! I enchant you! Red leather, yellow leather. Red leather, yellow leather. Listen to my spirit song! Ohmmm!!! Professor Singh: Get your malodourous armpits out of my face, Frankie. Gibby (to audience): Great, now it’s our job. I’ll yell red leather at Priscilla, and you yell yellow leather. RED LEATHER! (waits for response, proceed with chant after pausing whether or not audience responds or not). RED LEATHER! (pause again). RED LEATHER! Priscilla (looking back in forth with confusion between Gibby and audience, swiveling around to point butcher knife and both Gibby and the audience): What—what are you doing? What are you saying? There’s no such thing as red leather! Angel: Alright crazy lady, you’re about to be struck by an angel! AHHHHH!! (Angel throws a punch) Priscilla: (falls backwards and drops knife) Oh no, I dropped the knife! And you’ve hurt my face! Angel (throws a second punch): Take this! Diego: WHOA! K.O.! You knocked her out, Angel!

Gibby (to audience, either sarcastic if they did not participate or enthusiastic if they did): GREAT JOB! You guys did an awesome job of saying yellow leather. It’s like you had training in it or something. Frankie: Alright everyone, let’s make our great escape to freedom! F is for freedom, not failure! It’s time we get out of here and report Professor Creep to the police! Professor Singh (begging): No, please don’t! I’ll be fired! Angel: That’s really the most of your worries after attempted murder? Come on, everyone! (to audience) Creepy bystanders, it’s time we get out of here! Don’t mind if I throw one last punch first… Professor Singh (looks at Angel, gulps): Please no— Angel: You’ll wake up to the police, Professor Singh. Frankie: Radical teamwork, everyone! Seems like we all earned an A tonight. The End!
```

---

## IC-0850: A Trip Through “Monte Carla”

- Title: A Trip Through “Monte Carla”
- Author (byline): Elly Bogle
- Work: A Trip Through “Monte Carla”
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1618
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
Characters:
CARLA - a young white girl who had life handed to her...until tragedy struck
MOM - Carla’s dying mother
DAD - Carla’s unfaithful, homosexual father
GREG - Carla’s abusive boyfriend
LIAM - Liam Neeson from Taken
BEST FRIEND - Carla’s backstabbing friend
DOCTOR - a walking plot device

SHOW “PROLOGUE”

(The stage is bare. All actors stand onstage facing backwards and act as the set for

CARLA. If actors double characters, it is suggested that CARLA’s actor remains the

same throughout.)

ACTORS IN UNISON Now this is a story all about how my life got flipped, turned upside down…

(CARLA emerges from the ensemble and begins monologuing)

CARLA Hi. I'm Monte Carla. I'm an average girl who has never had anything bad happen to her in her whole entire life. Everything was going great. I had two loving parents. I had a best friend. I was content. Until, you know, the drama happened. Boy, was it bad. Especially since I never thought it would happen to me. Because

(pause) I’M WHITE!

(pause) I found out so much about myself and my family that I will never forget. The whole experience brought me closer to religion even though I was raised an atheist. You never understand why people fall to their knees until you, too, are driven to a point where only the cool ground can comfort you. Now, amongst the tragedy, I can truly be #blessed! But I left that wretched life behind me and am ready to move on with my life. Who I am is not defined by my past, so maybe one day I'll be stronger and learn how to heal the scars both on my heart and on my body. If you care to hear my story, stay. If you don’t, you have to stay too. Thanks and, uh, enjoy my shitshow of a life.

SCENE ONE

CARLA It started back in May. My mother and I were out shopping when:

(BOOM! A wild MOM appears!)

MOM Oh honey it's so great to see you.

CARLA You see me every day, mom.

MOM I know, but it seems like after your father and I decided not to tell you about our divorce, you've been so distant.

CARLA You're getting divorced?!

MOM I knew I should never have told you, but your father insisted. He said if we ever wanted you to see us or trust us again that we should be open and honest. Gosh, I feel so stupid for listening to him.

(distracted) Ooh, this is a cute skirt! What do you think?

CARLA That is cute. How much is it?

(shaking head) NO WAIT! Back up. I thought you and dad were happy.

MOM We were.

CARLA Then why get divorced?

MOM Your father is gay.

CARLA What?

MOM It’s true. One day he just...decided to sleep with the milkman behind my back. Literally, behind my back. I was sitting in the other room! They were on the couch, just doing it and listening to 90s Hip Hop!!!

CARLA

(gasps) Not 90s Hip Hop!

MOM I could’ve just...died right there.

CARLA Don’t be melodramatic. You’re not dying.

MOM I’ve actually been meaning to talk to you about that. Carla, honey, I have cancer.

CARLA What do you mean you have cancer?!

MOM Honey don't shout. You don't want me to have a heart attack. You know I have high blood pressure and a heart just itching to pop.

CARLA No, I actually DON’T know that! Why haven’t you told me any of this?!

MOM And there goes my heart.

(grabs heart)

I'm going... I'm going... Oh would you look at that? I'm truly dying. Tell your father I never truly stopped loving him.

CARLA But you aren’t even officially divorced yet?

MOM That doesn’t mean I can’t love the man I married.

CARLA But he cheated on you a room away from you. How…?

MOM It's actually kinda hot. I don’t know if I’m more impressed or turned on, but I’m definitely both.

(pause) OH OW! Yep that's the heart again. Goodbye Carla. I would say I love you but you're actually just adopted and I never really cared about you. Your adoption day was the capital-W Worst day of my life. Goodbye now.

(dies)

(The actor portraying MOM returns to the ensemble.)

CARLA

(to audience) With my mother dead and my father distant, I went out to find something I could believe in. Something that wouldn’t shatter my world. That's when I met Greg:

SCENE TWO

(GREG enters, finger guns flying)

GREG You must be

(finger gun) Carla.

CARLA How do you know my name?

GREG I've secretly been stalking you

(finger gun) but you won't find out until we start dating and I end up slowly making your life worse even though I seemed like I was going to be your

(finger gun) saving grace.

CARLA Sounds about right. Say, I'm trying to live on the edge. Would you maybe want to go out?

GREG More like

(finger gun) ruin your already shitty life, but sure!

CARLA Such a gentleman!

GREG Now I'm going to control you mentally and emotionally so that you are nothing more than a

(finger gun) shell of what you once were.

(GREG returns to the ensemble)

CARLA

(to audience) Greg was perfect. Everything I could have ever wanted in a partner. Things were going great with us. Then one day he... Took advantage of me.

(GREG cautiously approaches CARLA)

GREG Hey, Monte, I don’t mean to take advantage of you or anything, but

(finger gun) can you spot me some money? I need a McFlurry because I have a

(finger gun) CRAVING that cannot be satiated by Blizzards.

(CARLA reluctantly hands money to GREG who runs offstage excitedly)

CARLA

(to audience) But that wasn’t nearly as bad as… that night...

(GREG comes back)

GREG Carla,

(finger gun) can I be frank with you?

CARLA Who’s Frank?

GREG No I mean like,

(finger gun) honest.

CARLA Oh of course, what is it?

GREG I cheated on you… with your best friend.

CARLA What?!

(BEST FRIEND appears and lays a comforting hand on CARLA’s shoulder that she

quickly brushes away in disgust)

BEST FRIEND It’s true. I let it happen. I wasn’t even thinking, I just…

CARLA I HATE YOU! BOTH OF YOU! Just… stay away from me. Please.

BEST FRIEND Don’t leave!

CARLA I do what I want!

GREG If you leave then...we’re through!

(CARLA runs offstage. GREG and BEST FRIEND stare after her pleadingly for a bit and

then leave because stage directions )

CARLA

(to audience) I lost my best friend and boyfriend that night. It was horrible! But then, as if Greg’s infidelity wasn’t bad enough, he…

(gets choked up) he took things too far.

GREG Hey I’m going to kill you now.

CARLA What did I do?!

GREG You left me and I’m a jealous prick so, this just...makes sense.

CARLA Just when I thought things couldn’t get any worse!

GREG

(Stabby Stabby)

CARLA You literally aren’t even stabbing anything

DAD

(Punches GREG)

Don't worry, I'm here, honey!

GREG What you, GREG- I mean EGG?

(to audience) Ha! Shakespeare!

(in character once more) OW! PAIN!

(GREG dies...kinda) Well, I guess this is it for me. I have been

(weak finger gun) killed.

(actually dies)

CARLA Dad, what are you doing here?

DAD I realized I needed to see my baby girl grow up and I couldn't sleep around with that bad hombre anymore because if I can't get on my feet for myself, how would you ever be able to, as my blood? I know it sounds conceited, but I feel like I influence every aspect of your life. I needed to save myself to save you. I’m asserting my authority as a parent.

CARLA Oh dad, even though you suck, I missed you!

(CARLA and DAD hug and then just like a typical drama piece father, DAD leaves...to

the ensemble)

SCENE THREE

CARLA

(to audience) Having my dad back in my life was great. We talked about Mom, shared stories, bonded over silly things we both did, picked out cute guys together, attended and organized PTA meetings, it really was a dream come true. OR SO I THOUGHT!

(Guess who’s back, back again… you’re right! It’s DAD! But only his voice because the

actor is hidden in the ensemble. CARLA picks up a ringing phone, and DAD and LIAM

hide in the ensemble as mere voices on the other end of the call. They get no body

because OPPRESSION IS REAL AND ALIVE TODAY!)

LIAM Hello, Monte Carla. I am Bond, James Bond. Haha, I kid. I am LIAM NEESON FROM TAKEN.

(LIAM turns to wink to the audience) But now, I am the kidnapper. If you ever want to see your flamboyant dad, I suggest you give me a small loan of a million euro.

CARLA But I don’t have any money!

LIAM What about a college fund?

CARLA Nope. Bad parents.

LIAM Credit card?

CARLA Not for you.

LIAM Do you have any alpaca fur?

CARLA Why would I?

LIAM If you do not have payment, then you do not have a dad. He is my father now.

CARLA I won’t let you get away with this!

LIAM You already have.

DAD I’m sorry, Carla. I’m his father now.

CARLA NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!

(end pla-)

CARLA Wait, wait, wait. This is not a good ending for a dramatic script. We need more death, more tragedy, more cancer!

LIAM Uh...I have breast cancer?

CARLA Perfect! Now, tell me, did you cry when you found out? Will I cry when you die?

No.

Hmm…

But your dad… he’s dead.

D-d-d-d-deAD?!?!

Yes. I shot him.

LIAM

CARLA

LIAM

CARLA

LIAM

CARLA Probably because he was gay! You homophobe!

No, I swear! I love the gays!

Goodbye, Liam.

(hangs up) Damn homophobes.

SCENE FOUR LIAM

CARLA

CARLA

(stepping towards audience) So that’s my story. I had a great, normal life. I was happy. My family was happy. Then my dad came out. Now, here I am. An orphan. My mother is dead. My father is dead. I no longer have anything left to love. My life is meaningless. I would kill myself, but…

(CARLA is interrupted as DOCTOR emerges from the ensemble)

DOCTOR Monte Carla, right?

CARLA Yeah?

DOCTOR I’m a medical doctor and I have a degree. So you can trust me.

CARLA Okay…?

DOCTOR Carla, you have cancer.

CARLA WHAT?! But I haven’t even gotten tested!

DOCTOR And AIDS, but what’s important is the cancer.

CARLA But I’m a virgin, Doc.

DOCTOR Cancer isn’t an STD…

CARLA I MEANT THE AIDS! AIDs is an STD! Some doctor...

DOCTOR Oh, right. Well, it turns out you’re not a virgin.

CARLA How will I survive?!?!

DOCTOR Odds are, you won’t, but there is a small chance that...

CARLA Yes?

DOCTOR There’s a small chance you suffer from “Main Character Syndrome”

CARLA What’s that?

DOCTOR Essentially, it’s the idea that even though you have nothing to live for, you will go on for the sake of a decent ending.

CARLA Hell yeah!

(CARLA attempts to do the high school musical jump (unsuccessfully) while DOCTOR

and the ensemble slowly try to leave the stage so that no one will ever associate them

with this again.)

(Fin)
```

---

## IC-0851: Junk We Never Said Thank You For

- Title: Junk We Never Said Thank You For
- Author (byline): K.R. Schneider
- Work: Junk We Never Said Thank You For
- Publisher: Mushroom Cloud Press
- Publication date as stated: December 11, 2023
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: COLLIN, AMELIA
- Teaser before the introduction: No
- Spoken words (computed): 2402
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
K.R. Schneider

[Two long-time friends, Amelia and Collin sit around a backyard campfire, reminiscing on their childhood adventures before Collin’s wedding the following morning. Amelia is already seated. Collin walks over.]

COLLIN: I figured everybody would be asleep by now.

AMELIA: (shrugs) I’m not tired really. The fire’s warm. It’s kind of peaceful out here.

COLLIN: You mind?

AMELIA: You? Never. (she gestures for him to join her)

COLLIN: Ohh, sometimes you mind me.

AMELIA: (teasing) Only when you’re an idiot, and that’s only like sixty percent of the time.

COLLIN: Gee, thanks. I’ve always hoped for a best friend who called me an idiot.

AMELIA: Honesty equals love, so at least you know I love you.

COLLIN: Comforting. Thanks.

AMELIA: Anytime. (it’s quiet for a couple of beats) What are you doing up anyway?

COLLIN: Couldn’t sleep, I guess.

AMELIA: Nervous for your big day tomorrow?

COLLIN: (laughs) I’m not sure nervous is the right word. I was just…thinking.

AMELIA: Yeah? What about?

COLLIN: I guess just that…we’ve been through a lot together.

AMELIA: You and Julie?

COLLIN: No, dummy. You and me. We’ve been through a lot together.

AMELIA: You’re thinking about me on the night before your wedding? Definitely not a good sign, man.

COLLIN: (rolls his eyes) No, I just mean, you’re my best friend, Mill. You’ve done a lot for me.

AMELIA: More than my share, I’d say.

COLLIN: Probably. I did stuff for you too, right?

AMELIA: I think you gave me a high five once.

COLLIN: Oh shut up. I let you crash on my couch for like a month in college.

AMELIA: Yeah. Do you remember the blind date you went on while I was crashing on your couch?

COLLIN: (winces) Oof. Yeah. Vividly.

[FLASHBACK to college. Collin comes home from a date. Amelia is on the couch in his apartment watching TV.]

COLLIN: Never again, Millie!

AMELIA: (shuts off the TV with remote) It could not have been that bad. What’d she do, bite?

COLLIN: Why do I never learn? Blind dates are the bane of my existence!

AMELIA: So she did bite?

COLLIN: (rolls his eyes) I didn’t get close enough to risk it.

AMELIA: You’re so dramatic. I’m sure she was a nice girl. Who even set you up?

COLLIN: Milo.

AMELIA: Yikes. Okay, maybe not. Why would you let Milo set you up on a date? Do you want a venereal disease?

COLLIN: This one was bad bad, Mill. Like - you remember Loony Lisa from 8th grade science camp?

AMELIA: Oh yeah! She sent you all of those letters drenched in perfume and that weird doll with her face on it.

COLLIN: Worse than that.

AMELIA: No way. It could not have been worse than Loony Lisa.

COLLIN: No? Allow me to demonstrate. Come here. You be me. [Collin sets up two chairs and gestures to one. Amelia reluctantly sits down].

COLLIN: Okay - we’re at dinner. You start the conversation. Just be normal. Be…me.

AMELIA: You want me to pretend you and normal are synonymous?

COLLIN: Can you not be a sarcastic pain in my neck for ninety seconds, please?

AMELIA: Right. Yes. This isn’t weird at all. My apologies. Proceed.

COLLIN: Thank you. Now, we’re at dinner. Just introduce yourself. Ask me about me.

AMELIA: Okay. [she becomes Collin - slouches back in her chair, shifts her face]

COLLIN: What are you doing? What is that?

AMELIA: I’m being you.

COLLIN: I don’t sit like that. I don’t look like that.

AMELIA: Well in lieu of plastic surgery, Collin, I can’t wear your face!

COLLIN: No - I don’t….make that face. You look half annoyed and half constipated.

AMELIA: Fine. I’m going to buy you a mirror because my impressions are always spot-on. But fine. (clears her throat and lowers her voice) Hi. Nice to meet you. I’m Collin.

COLLIN: (shifts his posture to act like his date) Milo says you’re a phenomenal kisser.

AMELIA: (breaking character) That was not her opening line!

COLLIN: Yes! It was. Now focus, it gets worse.

AMELIA: Wait, does Milo know if you’re a phenomenal kisser?

COLLIN: Millie, focus!

AMELIA: So, he does?

COLLIN: Amelia!

AMELIA: Right, sorry. (as Collin) So, tell me about yourself. What’s your name? What do you do? Are you going to school?

COLLIN: (as his date) My name’s Gwen. I am currently a student, but I don’t think the whole student thing is really fulfilling my life plan.

AMELIA: (breaks character again) This is so weird. Why can’t you just tell me about your date like we’re normal people??

COLLIN: Okay, fine. So she tells me that she’s planning on quitting school because she’d like to be a full time mother.

AMELIA: So she has kids?

COLLIN: No! She doesn’t have kids. She would like to consider having my kids.

AMELIA: No.

COLLIN: She asked me about my sperm count.

AMELIA: Shut up.

COLLIN: Not a joke.

AMELIA: What did you say??

COLLIN: Well obviously at that point I knew the date was over.

AMELIA: But what did you say?

COLLIN: I told her I didn’t think we’d be a good fit for a relationship.

AMELIA: Uh huh.

COLLIN: But then she said she didn’t necessarily need a relationship.

AMELIA: Yikes. Milo is setting you up for a venereal disease.

COLLIN: So then she tells me her car is right down the block. If I were interested…

AMELIA: Which you weren’t.

COLLIN: I mean she was pretty hot.

(There’s a knock on the door).

AMELIA: You didn’t.

COLLIN: No. I’m just saying - she was hot.

(There’s another knock at the door).

COLLIN: Did you order a pizza or something?

AMELIA: Nope.

COLLIN: Invite someone over?

AMELIA: Maybe your date followed you home.

COLLIN: It can’t be. Right?

AMELIA: Goofy Gwen. Here to procreate. Right on cue.

COLLIN: You answer the door.

AMELIA: No way!

(The knocking persists).

COLLIN: Millie, please!

AMELIA: What am I supposed to say?

COLLIN: Tell her I’m not home!

AMELIA: You’re eight feet from the door!

COLLIN: I’ll hide! Pretend you’re my angry girlfriend or something.

(Still knocking)

AMELIA: You owe me, Collin.

COLLIN: Yes! I absolutely owe you!

AMELIA: Buying my dinner every time we go out for the rest of your life!

COLLIN: Fine. Okay. Just answer the door! [Amelia opens the door. Collin hides behind the furniture. We don’t hear Gwen, but we hear Amelia’s responses to her which become more and more hysterical. Collin winces and panics in reaction to every comment made.]

AMELIA: Hello? .... I’m Debbie. Who are you? … NO, I’m Collin’s girlfriend! Who are you? … He did what? … That cheater! I’m the mother of his unborn child! … We’re getting married! … If he comes home tonight I’m going to light his car on fire! … [Amelia slams the door shut and immediately stops the hysterics]. Crazy enough for ya?

COLLIN: A little too good. Light my car on fire?

AMELIA: Crazy responds to crazy.

COLLIN: She probably won’t be back right?

[PRESENT: Amelia is laughing. Collin is shaking his head, horrified.]

COLLIN: She absolutely did come back.

AMELIA: Yeah, real glad I was done squatting at your pace by that point.

COLLIN: She set my couch pillows on fire.

AMELIA: You let her inside your apartment.

COLLIN: Milo let her inside my apartment.

AMELIA: It’s a miracle you’re still friends with him.

COLLIN: See what I mean though? You’ve been there for all of my crazy stuff, Mill.

AMELIA: Goofy Gwen was an exceptionally crazy one.

COLLIN: You remember that night we climbed the water tower?

AMELIA: (nods) Yeah you almost wet yourself before we got to the top.

COLLIN: I don’t like heights!

AMELIA: Didn’t Milo dare you?

COLLIN: He bet me I couldn’t drop a penny from the top and hit him.

AMELIA: He was right. You couldn’t.

COLLIN: I might have been able to if I wasn’t shaking my tail off.

[FLASHBACK to junior year of high school. Collin and Amelia are climbing the side of the water tower. Collin is above, moving very slowly. Amelia is below.]

AMELIA: Could you pick up the pace?

COLLIN: (squeaky and nervous) How far of a drop do you think this is?

AMELIA: From here? I don’t know, like fifty feet?

COLLIN: It seems higher than fifty feet!

AMELIA: Collin, we still have like 100 feet to go!

COLLIN: What do you think happens to a body that falls 150 feet?

AMELIA: I think it dies, which is what’s going to happen to you if you don’t pick up the pace!

COLLIN: Don’t rush me!

AMELIA: This was your idea!

COLLIN: I wasn’t serious! Milo was the one who was serious!

AMELIA: Then why doesn’t Milo climb up here?

COLLIN: How high do you think we are now?

AMELIA: 52 feet because you’ve taken a singular step since the last time you asked!

COLLIN: (breathing heavily) This was not a responsible decision.

AMELIA: Let’s just get to the top, and you can freak out up there. If you freak out here, you’ll take me out with you!

COLLIN: Okay. Okay. Breathe.

AMELIA: I am breathing. You start climbing! [They finish the climb to the top. Collin is shaking, maybe also hyperventilating. Amelia is calm.]

COLLIN: (with his eyes shut) How far down is it?

AMELIA: We’ve been over this.

COLLIN: I can’t look.

AMELIA: It’s actually kind of awesome.

COLLIN: (peeks one eye open, then the other, looks around them - still nervous but also impressed with the view) Okay. This is kind of awesome.

AMELIA: (points) I can see my house from here.

COLLIN: (points in a slightly different direction) Mine too.

AMELIA: Okay. Get your penny. Prove your point. (Collin digs in his pockets and comes out with a coin. He holds it out.) That’s a nickel.

COLLIN: I have this or a dime, and this is a larger projectile!

AMELIA: You bet a penny. We climbed 150 feet into the air, and you don’t have a penny??

COLLIN: Like Milo will notice he got hit with a nickel.

AMELIA: Like you’ll even hit Milo with the nickel.

COLLIN: Oh, yea of little faith.

(Collin puts the nickel back into his pocket, steps to the edge and grips the railing. He looks around, seems pretty comfortable. Then he looks down. He is instantly uncomfortable - he starts to sway, closes his eyes, opens them again, backs up, squats down - still holding tight to the railing).

AMELIA: Collin?

COLLIN: A drop like this would definitely kill me.

AMELIA: Yeah. Good thing you’re launching a coin and not your body.

COLLIN: I think I’m gonna’ throw up.

AMELIA: Are you kidding me? It took us an hour to climb up here!

COLLIN: I can’t do it. You do it.

AMELIA: Fine. I’ll do it. Give me the nickel.

COLLIN: (stand up - eyes shut tight - holds his arms out as his sides) Take it out of my pocket.

AMELIA: I’m not taking it out of your pocket! Just hand me the nickel!

COLLIN: I can’t move. I’ll plummet to my death.

AMELIA: You climbed up here. We have to climb down.

COLLIN: (risks a look down) No! Nope! Not happening!

AMELIA: WHAT?

COLLIN: It’s fine. I’m okay. This isn’t the worst place to spend the rest of my life. I’ll just stay here.

AMELIA: How did I not know you were afraid of heights. How did you not know you were afraid of heights?? Come on - let’s just climb down. I’ll go first, okay?

COLLIN: Not a chance. This is my home now. Call my mom; tell her I loved her.

AMELIA: (pulls out her cell phone) Oh for the love of God.

COLLIN: Are you really calling my mom?

AMELIA: No, dummy. I’m calling the fire department to get your scared little kitten butt down from this tree.

[PRESENT: Both of them are laughing.]

COLLIN: Definitely not my proudest moment.

AMELIA: Yeah, but it makes for a good story. Nice little preview of my wedding speech.

COLLIN: You’re not telling that story in your speech tomorrow.

AMELIA: Live in suspense, buddy.

COLLIN: Can’t you tell some story where I was like strong and heroic and not peeing my pants in fear? Make me look a little bit cool.

AMELIA: Unfortunately, you’ve gotta’ be cool to look cool.

COLLIN: Sometimes I’m cool.

AMELIA: Give me one example.

COLLIN: What about the time I heroically took you to prom at the last minute?

AMELIA: My date got mono.

COLLIN: And I, very coolly, stepped in to save the day.

AMELIA: That’s not heroic. That’s common decency.

COLLIN: I’d rather be remembered as decent than as a big chicken.

AMELIA: I’ll see what I can do for you.

COLLIN: Come on - are you gonna’ tell any story that makes me look cool?

AMELIA: I don’t know if cool is the right word - but, yeah…maybe…

[FLASHBACK: Amelia’s father’s funeral. She is crying on the church steps. Collin comes out and sits next to her.]

COLLIN: Man, it’s hot in there. (loosens his tie) Why is it common practice to make a funeral an oven? Everybody’s already in black layers, and you’re gonna’ roast ‘em alive? It’s never made sense to me.

AMELIA: I’m fine, Collin.

COLLIN: I know.

AMELIA: I don’t need the comedy routine, okay? I’m fine.

COLLIN: I know.

AMELIA: You can go back inside.

COLLIN: I’m good right here.

AMELIA: I just needed some air.

COLLIN: Okay.

AMELIA: It’s not that I can’t handle it. I’m fine. I can do it, okay? I’m not running away from it. I just…I just…

COLLIN: Needed some air.

AMELIA: Yeah.

COLLIN: Okay. You need some air. We’ll sit in the air.

AMELIA: You don’t have to sit with me.

COLLIN: So you mentioned.

AMELIA: I just need to be alone for a minute.

COLLIN: That’s fine. I’ll be alone with you.

AMELIA: I don’t need you.

COLLIN: No. You don’t.

AMELIA: I don’t need anybody. I’m fine. All by myself.

COLLIN: Yes you are.

AMELIA: Then why are you still sitting here?

COLLIN: Because I love you, Mill. Because this day sucks. Because your dad died. Because you have been the strong one for as long as I can remember, and you shouldn’t have to be that today. (she opens her mouth to protest) It doesn’t matter whether you can. You can. But I love you, and I’m your best friend, and you don’t have to be the strong one today. You let me do it.

AMELIA: I don’t know how.

COLLIN: (wraps an arm around her) Right now you just sit on these steps with me, and you breathe.

AMELIA: (leans into him) I feel like I can’t breathe. I hate this. It’s not fair. This day, this whole dying thing, it’s not fair.

COLLIN: No. It isn’t. It sucks.

AMELIA: It really sucks. (she sobs into his shoulder for a time)

COLLIN: I’ve got you, Milie. I’m right here.

AMELIA: (collects herself, takes a deep breath) How am I gonna’ go back in there?

COLLIN: Through the doors. Down the aisle.

AMELIA: Yeah, but everybody saw me freak out in there, and I’m supposed to be--

COLLIN: You’re not supposed to be anything today. All your supposed-to-bes are on me today. So you’re gonna’ take a breath, you’re gonna’ hold my hand, and we’re gonna’ walk back in there together. Whenever you’re ready.

AMELIA: I’m ready.

COLLIN: You sure? It really is an oven in there.

(He offers his hand; she takes it).

[PRESENT: Amelia is somber, she’s been crying but not heavily. She wipes her eyes, smiles at Collin.]

AMELIA: That was the coolest you’ve ever been for me.

COLLIN: (scoffs) That wasn’t cool. That was…I don’t know…I didn’t think about it, really. You were hurting. I wanted to make it easier.

AMELIA: Yeah. It takes effortlessness to be cool. That wasn’t effort. It was just you.

COLLIN: And that was cool?

AMELIA: That was definitely cool.

COLLIN: I’m gonna’ repeat back to you what you said, so you know: “It was just you. That was definitely cool.” You think I’m cool. You said it.

AMELIA: I take it back.

COLLIN: You can’t take it back; you said it!

AMELIA: If I had known it would go to your ego like this, I would have kept it to myself.

COLLIN: But you do think I’m cool.

AMELIA: You’re a headache.

COLLIN: A cool headache. A soft sea breeze. A damp washcloth to the forehead.

AMELIA: (mocking his tone) A brain freeze.

COLLIN: Okay, fine, I’m done.

AMELIA: Thank you.

COLLIN: Hey, Mill?

AMELIA: Yeah?

COLLIN: Thanks. For all that junk. For the junk I never say thank you for.

AMELIA: That’s the point of a friend, dummy. You don’t have to say thank you for the junk. The junk is what makes us friends. If there isn’t any junk, it’s just the surface layer, just the easy stuff.

COLLIN: You’re easy stuff.

AMELIA: And clearly we’ve capped our serious conversation limit for the evening.

COLLIN: Yeah, ten minutes, and I’m tapped. (taps his head) It’s all one-liners, and punch lines in here now.

AMELIA: Junk?

COLLIN: Less important junk.

[He winks at her. They share a look. Freeze.]
```

---

## IC-0852: Office Case

- Title: Office Case
- Author (byline): Matt Mills
- Work: Office Case
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2028
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
(Two upbeat office workers, Martin and Debby, sit at their cubicles. They work with energy, typing, clicking, coffee-sipping, and so on as they talk.)

Martin: This has got to be the best batch of coffee Martha has ever made.
Debby: I know! In my three years at Moderninnovatech, this is by far the least chunky.
Martin: I’ve got such a caffeine-high, I could sell a million units at once.
Debby: I could rip a chair in half.
Martin: I could do basic math.
Debby: I could insert USB drives correctly on the first try.
Martin: Okay that’s just ridiculous, Debby.
Debby: ...Martin?
Martin: I’m on the horn with a client, so. Go ahead. (to headset) No, not you, ya dumb-dumb.
What’s up, Debby?
Debby: Since this coffee means we could do anything… what do you actually want to do?
Martin: What do you mean?
Debby: Like. If you could choose to do anything in the world, what would it be?
Martin: Well, I’d love to sell you several units so I can make my daily quota and play paintball
the rest of the afternoon.
Debby: I don’t mean today, I mean--
Martin: (to headset) No, not you, I’m obviously talking to Debby. (listens) …”Who’s Debby”?!
Debby: Martin, of course I’ll buy several units to get you up to quota, but--
Martin: (to headset) You don’t know who Debby is?! Well she’s only my cubicle-mate, annnd
Moderninnovatech’s third most successful salesman. Out of salesmen whose names start with
‘D’ and ‘E’.
Debby: Don’t you ever think about what you want from life? Like. For the rest of it.
Martin: (ponders a while) No, I don’t.
Debby: Neither did I. Until I drank this suddenly potable coffee.
Martin: (holds up a finger) Sorry Debbie, I was talking to this client. (to headset) Yeah you, ya
big weirdo. (to Debby) Customers, am I right?
Debby: Usually my dreams take place in this office, because almost all of my life is spent here,
but today… Thanks to this sweet cup of Martha’s Joe, I can see my dream so, so clearly. I’m
gonna be an accountant! No, that’s just ‘cause I saw a calculator in the corner of my eye. I want
to be a… window. No. A… tree, that’s not it. A cubicle.
Martin: I’d love to be a tree that got made into a guitar.
Debby: Why don’t you just be a guitar?
Martin: Why don’t you just GET OFF MY BACK?! (off Debby’s shock) Oh not you, Debby. This
dumb client keeps asking to buy stuff.
Debby: Martin. Don’t you see?!
Martin: Sixteen hours a day! ...Well, I do blink a lot, so maybe more like nine--
Debby: We’ve never thought about our dreams because we’re always trapped here! Working
our nine-to-nine jobs, just trying to make ends meet. It’s like that song--”Despite my young age, I
am still just a bat in a cave!”
Martin: Ooh, I love The Dashing Muchkins.
Debby: I just want-- (turns) Oh hey, Jeff and Janice.
Martin: Why the long faces?

(We see Jeff and Janice’s stoic faces barely poking over the cubicle wall.)
Janice: Didn’t you hear?
Jeff: Apparently not.
Debby: Hear what?
Martin: Did you guys finally lose a staring contest?
Janice: (stares for a moment) Moderninnovatech canceled vacation days.
Jeff: Vacation days.
Debby: Pfft, ha-ha. Good one. That’s not possible.
Martin: I’m no lawyer but I watch TV sometimes and I’m pretty sure that’s illegal.
Janice: Not in these corporate states of America.
Jeff: Read the memo if you don’t believe.
Debby: Pfft, memos. Like a memo would say th-- (reads a memo) My god, they weren’t kidding.
Martin: They canceled our vacation days?? Just like that?! Canceled! ...All of them??
Debby: Just like the vacations my parents promised when I was a kid. They’re all canceled. I
guess Moderninnovatech doesn’t love us… maybe the company’s getting divorced?
Jeff: I’m gonna go boil water to pretend I’m in Florida.
Janice: And I’ll be sticking my head in the freezer to pretend I’m in Alaska.
Martin: After everything we’ve given this company. Multiple sales, thousands of dollars worth of
coupon books…

Debby: I was in my mid-20’s when I started here. I was GORGEOUS. Now I’m in my late-20’s.
And I am DISGUSTING. We’ll never get that time back. Instead they just take more time away
from us. Even this great coffee isn’t worth that!
Martin: I was going to visit my dying father this year. Or go to Comic-Con. I can’t believe they’ve
done this. I was so excited to finally go to Comic-Con!
Debby: What even are we?
Martin: Humans?
Debby: If we just go along with this, keep pumping out record-low sales for this company while
they take away our FREEDOMS, we may as well just be robots!
Martin: That would be pretty cool, actually. My knee does this weird clicky thing--
Debby: Martin. If we don’t fight for our lives right now then we’ll never be able to again!
Martin: Yeah! Can it wait ‘til tomorrow? I’m pooped.
Debby: We may not be who we want to be. We may not know what we want to be. We may not
have marketable skills or social acumen or basic hygiene. We may be broke, tired, and of sub-
par intelligence. We may not floss every day--
Martin: Whoa, Debby. I’ve gotta stop this monologue of yours. I floss every day.
Debby: My point is… this is our opportunity.
Martin: For what?
Debby: Exactly!
Martin: ... I don’t get it.
Debby: Let’s find out! Don’t you want to see what we’re capable of?
Martin: Sure.
Debby: Don’t you want to stick it to Moderninnovatech?!
Martin: I’ve stuck it to people for far less.
Debby: Then what are we gonna do?!
Martin: We’re gonna rob this place blind!!!
Debby: Yeah!!! … Wait, did you just say ‘rob this place blind’?
Martin: Uhm. Yeah?
Debby: Okay just making sure. That’s what I was thinking, too!
Martin: All right!
Debby: Let’s do it!

(Later that night, Debby and Martin sneak throughout the office, searching every nook and
cranny.)
Debby: We’ve gotta find those keys if we want in the vault.
Martin: I can’t believe Mr. Bossenheimer would hide keys to a room with millions of dollars of
cash in it. Like, what if there’s a money emergency??
Debby: Whoa, Martin! Here he comes!
Martin: Oh no. I’m out!
Debby: Martin?!

(Martin ducks into a cupboard. Mr. Bossenheimer approaches Debby.)
Debby: Hello, Mr. Bossenheimer!
Mr. Bossenheimer: Whoa, hey there Debby! Burning the midnight oil, eh?
Debby: No sir, I’m not a pyromaniac and my permanent record shows that I’ve never been
convicted of arson, so don’t even bother looking.
Mr. Bossenheimer: Ah. I just meant... you’re working late. That’s good to see! We need that kind
of initiative around here.
Debby: Ah yes, working. That is what I am doing, Mr. Bossenheimer. Sticking around here.
Totally what I’m doing, Bossenheimer--
Mr. Bossenheimer: Rob.
Debby: What?! Why would I rob--
Mr. Bossenheimer: Call me Rob.
Debby: Why would I do that? I’ve never thought of the word ‘rob’ before, and I never will again.
Mr. Bossenheimer: I just meant… Never mind. I’ll let you get back to it.

(He walks off. Debby opens a few cupboard doors. Finally opens Martin’s and he pops out.) Martin: Phew, that was a close one. Debby: Sorry I forgot which cabinet you put yourself in. Martin: Happens with me and my children all the time. Did you happen to find the keys while I was in there? Debby: No. I can’t believe they aren’t in the kitchen drawers. I know Mr. Bossenheimer has a set, but I also know that he probably wouldn’t just hand them over for me to rob all of Moderninnovatech’s cash. Except, maybe he would--we are on a first-name basis now. Martin: What’s his first name? Debby: I can’t remember. Martin: Can you guess? Debby: It starts with a letter. I know that.

Martin: Hm. I’m not sure that’s enough. Maybe you should distract him and we’ll steal them.
Debby: My teachers always did tell me I was great at distracting others…
Martin: See? Maybe this is what you were meant to be.
Debby: You mean… I’ve found… my purpose?
Martin: ...Well maybe, sure.
Debby: Let’s do this. Again.

(Mr. Bossenheimer is chilling in his office, bouncing and singing lightly along to a song. Debby sneaks in.) Debby: Hello again Mr. Bossenheimer. Mr. Bossenheimer: Whoa, oh Debby you scared me. Why’d you sneak up on me like that? Debby: Sneak, no. I’m not. I just. New shoes, you know. Super quiet. As I requested. Not. Um. You know what I was thinking? Is a funny word? ‘Keys’. (laughs) I mean, who thought of that, right? Mr. Bossenheimer: Huh. I guess I never thought about that. You’re right, that is weird. Debby: You have keys, right? I mean, we all have keys. Mine go to my car, my apartment... Maybe yours go to a house, a different car, and uh, I don’t know. Maybe like a giant stockpile of cash? Mr. Bossenheimer: (chuckles) Now I’m just thinking about how silly the word ‘keys’ is. Debby: Right, like it makes me want to just take out all the keys I have and go… (takes out her keys, yells at them) ‘Ahh you’re such a silly word!’ Right? Join me. Mr. Bossenheimer: You want me to take out my keys and yell at them? Debby: Just do it, Bossenheimer!

(He shrugs, reaches in both of his pockets.)
Mr. Bossenheimer: Okay then. (at his keys) You’re so silly!
Debby: I like yelling at them for specifically what they are, like. Dumb car key! Dumb apartment
key...
Mr. Bossenheimer: I don’t know if I need to--
Debby: You need to.
Mr. Bossenheimer: Well. I guess I do have a pretty stupid house key. And car key. And vault
key--
Debby: Right? So dumb. Like it makes me wanna just…

(She grabs his keys, shaking them all.) Debby: Shake ‘em up!!! Mr. Bossenheimer: Whoa there, be careful.

Debby: Oh I will. Here you go, here are all of your keys. I’m sure you’re not missing any. Don’t even bother checking. Okay great talk Mr. Boss, see ya later! Mr. Bossenheimer: Uh, okay--

(Martin and Debby rush to the vault and pull out the keys.)
Debby: All right, this is it. The key to our futures.
Martin: I thought it was the key to the vault.
Debby: Yes but inside the vault is our futures.
Martin: I thought there was money in there? Aw man, we did all this for ‘futures’? What a
bummer. I don’t even know what those are.
Debby: No, it’s… Okay I’ll just open it.

(She puts the key in, twists. The door opens and their jaws drop with amazement.)
Debby: Wow...
Martin: It’s so…
Debby: Empty.
Martin: Yeah. I guess there’s nothing in our futures.

(Jeff and Janice pop up from behind a table.)
Janice: You’re late.
Jeff: Very late.
Debby: Wh-- what? What. I don’t. How are you two.
Martin: Why are you two…
Debby: What?
Martin: How.
Debby: Why?
Martin: Quoi?
Debby:Que?
Martin: Pasa?
Janice: We were late too.
Jeff: Too late.
Debby: You mean…
Martin: Someone else robbed this place blind?
Debby: Before we could?
Martin: Before you could?
Debby: Before you or we could?
Janice: Martha got here hours ago.

Jeff: Coffee-high. Janice: She was here before them two. Jeff: Too.

(They turn to see two downtrodden co-workers waving.)
Debby: Aw man. And here I thought we were special.
Martin: It just goes to show you. If you ever think you’re special, don’t.
Debby: But now what do we do with our lives? We can’t work here anymore. I’m too lazy to
return Bossenheimer’s keys.
Martin: I was really looking forward to having freedom. Time to think about what I want to think
about. Or just play some paintball.
Debby: Hey… why can’t we be free? I mean, what’s stopping us from walking out that door,
casting aside all of our responsibilities, our shackles of modern living, and finding who we really
are? Why can’t we go explore who we want to be?
Martin: Money.
Debby: Oh. Yeah. I forgot about money…

(The next day, they’re back at their desks working away.)
Martin: Moderninnovatech, how can I help you?
Debby: You can’t.
Jeff: You guys too?
Debby: Don’t remind us.
Martin: Yeah, especially when I’m on the phone. (to headset) No, you shut up too.
Janice: We’ve got a plan.
Jeff: Yeah.
Janice: A good plan.
Jeff: I think.
Debby: What is it? Stalk people over their cubicle walls?
Martin: Talk in weirdly sterile patterns? (to headset) No, I wasn’t telling you to do that…
Although you’re pretty good at that.
Janice: Far better.
Jeff: We…
Janice: Are going…
Jeff: To rob…
Janice: Fort Knox...
Jeff: Blind.

(Debby and Martin look to each other, interested.)
Debby: Now that’s a smart plan.
Martin: I’ll finally be able to focus on my paintball career. (to headset) Please stop listening to
my conversations, sir. Let’s go get our futures!
Debby: Let’s go!
Martin: Comic-Con, here I come!
Debby: Life-purpose, here I come!
Jeff: Florida. Here I come.
Janice: Alaska. Here I come.
Martin: Okay, no one really cares about your things…
Debby: Yeah.
Martin: Let’s just stay excited for our things.
Debby: Yeah.
Martin and Debby: The futures!
```

---

## IC-0853: Play Nice

- Title: Play Nice
- Author (byline): K.R. Schneider
- Work: Play Nice
- Publisher: Mushroom Cloud Press
- Publication date as stated: December 11, 2023
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1760
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
K.R. Schneider
[Dennis and Madeline, a married couple on the brink of divorce, sit in a car. Madeline is frozen,
looking out the window in annoyance while Dennis speaks to the audience.]
Dennis: They say you don't really know a person until you live with them. In my case, you don't
really know a person until they spend the entire fifth year of marriage trying to hit you in the face
with a hairdryer. Or...toaster. Or that one time my flat screen. Madeline’s a special kind of crazy.
And she hates me. So this marriage is gonna' take the swan dive; that much is clear.
Unfortunately, I'm not really up for breaking the news to my parents over family Christmas. Call
me spineless, call me whatever you like. More than likely Madeline's already beat you to it. So
we've decided to wait until after the holidays and just tell them...via email. Needless to say the
four hour car ride has not been the highlight of my holiday season. And smart money says it's
just gonna' get worse.
[Dennis sits back to drive – Madeline unfreezes]
Dennis: Listen, Madeline. Can we try to be civil this weekend? It’s only two days, and my
parents--
Madeline: You understand that I can’t stand you, correct?
Dennis: Yeah. I got that. I’m not all that fond of you either if we’re being honest.
Madeline: Oh, you want to be honest! That’s a laugh.
Dennis: Madeline, I just-
Madeline: I hate you, Dennis. Truly. I hate you.
Dennis: I’m not real fond of you either, Hades. But we’re in this. So when we get to my parents’
house we have to act like we wouldn’t rather be in prison for homicide. No matter how many
times I’ve considered it.
[Madeline freezes – offended – Dennis speaks to the audience].
Dennis: Okay, so I haven’t really considered killing her. Well…maybe once. But you can bet
she’s plotted my gruesome disappearance a time or two!
[Unfreeze]
Madeline: You know what, fine. Whatever! I can play happy family. What I can’t do is choke
down another turkey your mother burned.
Dennis: You’re kidding. You want to talk about my mother’s cooking? I think I chipped a tooth
on the last meat-brick you made.
Madeline: You said you liked my meatloaf!
Dennis: Yeah. I said I liked your sister too, and we both know that wasn’t true.
Madeline: What’s wrong with my sister?
Dennis: Nothing. You know…nothing. Some guys like a girl that’s been around the block.
Or…across the ocean.
Madeline: What is that supposed to mean!?
Dennis: Oh, come on, Maddie-
Madeline: DON’T call me that!
Dennis: Your sister is a tramp.
Madeline: She’s finding herself. And you are an insensitive chauvinist.
Dennis: And you’re Lucifer, but we all deal with that somehow.
[Madeline pulls back to hit Dennis – She freezes – Dennis addresses the audience].
Dennis: Okay, maybe I deserved that one. But the kind of hole you can dig with the shovel she
hands me is just too tempting to resist. I decide maybe it's best to just spend the rest of the trip
with my mouth shut. It's actually worked pretty well too. But once we get to my parents house
the storm is bound to come crashing through.
[Back to driving – Madeline unfreezes].
Dennis: Well, here we are!
Madeline: Super, you’re a GPS now.
Dennis: This is gonna’ be a long weekend.
Madeline: I hate you.
Dennis: Really? Because the first 47 times you said that today just didn’t seem to drive the nail
in.
Madeline: Let’s just get this over with.
[They sit in Dennis’ parents living room. It’s decorated for Christmas. Dennis is appreciating
the decorations. He seems to be in a pretty good mood. Madeline is scowling. She hates it here.]
Madeline: Wow, I forgot how much your mother’s silver plastic tree just screams class. You
think it was on sale?
Dennis: (defensive) It’s family tradition. It doesn’t matter that it’s cheap! (An idea occurs to him)
Just think of it as my family’s version of your sister.
Madeline: God, I hate you.
Dennis: Forty-eight. That’s forty-eight times since we left.
Madeline: Die.
Dennis: I wish. Can we please just open gifts in silence?
Madeline: Sure, sure. Let’s pretend that everything is just peachy.
Dennis: I told you. I’m not ready to tell them!
Madeline: Yeah, because you’re totally spineless, “Denny”.
Dennis: Stop it! Only my mother calls me that.
Madeline: I think that proves my point.
Dennis: Just open your gift.
Madeline: Wow, Doris! It's beautiful. [reads off of the card] For many years of happy marriage.
Dennis: Of course she did.
Madeline: Just thank her and let's move on.
Dennis: Thanks, Mom. That’s great. [opens his own gift] Oh...wow! Look honey, it's a picture
frame. And it’s….engraved. Look what it says.
Madeline: [reading] Denny and Maddie. Well isn't that...nice.
Dennis: It's great. We'll put it to good use.
Madeline: Smash it. Burn it. Drop it out an upstairs window.
Dennis: Shut up.
[Madeline sits back, satisfied, with her arms across her chest – freezes. Dennis addresses the
audience].
Dennis: So I love my mother okay? Sue me. My wife is demented. If your wife was demented
you might call your mother a little more often than normal too. But! Madeline got her digs in –
she seems to feel pretty satisfied with herself. I’ve got to be in the clear here, right?
[Madeline unfreezes, expression automatically angry – punches Dennis in the arm].
Dennis: What the – ouch! What?
Madeline: What. Is. That??
Dennis: What!
Madeline: That package! What is the name on that tag?
Dennis: Uh – Chloe?
Madeline: Chloe. Chloe? Chloe! I cannot believe your mother! I thought you hadn’t told her!
Dennis: I haven’t! What are you talking about?
Madeline: Chloe? Chloe? (Dennis continues to look at her like she’s nuts.) Chloe is your ex
girlfriend. And you know what, I'm sure your mother just loves her. I'm sure she even invited her.
Dennis: Madeline! I have no idea what you’re talking about. I have never dated a Chloe. Never
in my life.
Madeline: Are you cheating on me? You’re cheating on me!
Dennis: Cheating on you. Yeah. That's what I'm doing, Madeline. I'm cheating on you and I'm
telling my mother all about it so she can gift wrap sweaters for my mistress.
Madeline: I knew it!
Dennis: I imagine that gift is for my cousin, Chloe.
Madeline: That’s what they all say!
Dennis: I don’t-you are insane! When did you go insane? What the hell was I doing? How did I
miss that?
Madeline: That is so hurtful!
Dennis: Are you crying!? Madeline, you’ve been throwing small appliances at my head for a
year! I’m not cheating on you; I just think you’re nuts!

Madeline: I am not nuts! I hate you.
Dennis: I think you mentioned that.
Madeline: I mean it, Dennis Arthur Zorowitz. I think you are pond scum. I can't believe I ever
married you!
Dennis: Yeah, well don't flatter yourself, Maddie. Like you could've found anyone else to put up
with you.
Madeline: How can you say that to me? You are so hurtful!
Dennis: You're not exactly a picnic!
Madeline: At least I tell you how I'm feeling. But could you show me the same courtesy? Of
course not. You're much too insensitive for that.
Dennis: I am so sick of you telling me what a horrible person I am. I'm the one that asked for a
divorce if you'll recall! I think that should pretty much tell you how I feel.
Madeline: You're sending mixed signals.
Dennis: HOW?
Madeline: Never mind. I'm not speaking to you.
Dennis: Promise?
Madeline: See, this is exactly what I’m talking about!
Dennis: I thought you weren't speaking to me.
Madeline: You are a jerk.
Dennis: [sigh] I can't wait until this is over.
Madeline: Well at least we agree on something.
Dennis: One thing in five years - quite the record.
Madeline: I hate you.
Dennis: Do you really feel it necessary to mention that every few minutes? Did you think I
would forget?

Madeline: You know what - that's it. I can't do this anymore. Dennis: What are you talking about? Madeline: You know what, “Denny!” Let’s get this over with. Let’s tell your mother! Dennis: Let’s not make any rash decisions here! Madeline: Dennis. We. Cannot. Stand. Each other. Dennis: Yes. Madeline. I realize. Madeline: I don’t think you do! I’m done pretending. I cannot stand you! Dennis: And why is that? What did I ever actually do to you? Madeline: (takes a deep breath - she’s ready for this) You snore. You wear socks with your sandals. You drink milk from the carton. You hog the remote. You sweep the floor dirt under the rug. You dust around the pictures and not under them. You have a horrible sense of direction. You fake laugh when nothing is funny. Your favorite tie does not match ANY of your shirts. You eat all but the very last few chips from the bag and don't throw it away. Dennis: Oh, is that all!? Madeline: (sighs and looks him over) And if your hairline recedes any further back it’s going to get embarrassing to be seen in public with you. Dennis: I am not losing my hair! Madeline: Sure. Dennis: Fine! Do you want to know what I hate about you? Madeline: No. Dennis: Oh. Okay. (a couple beats of silence and then): You bite your fingernails. You eat all of the M&Ms out of the trail mix. You alphabetize everything. (Madeline attempts to speak. Dennis cuts her off.) No, that's not cute. You chomp your gum. You THROW THINGS AT MY HEAD. You have never been nice to my mother! And you litter. Madeline: You are SUCH a momma’s boy! If you hate me that much, let’s just TELL her! Dennis: I don’t want to upset her, Madeline! She has a weak heart. What if she has a heart attack? What if she DIES? It’s CHRISTMAS! Madeline: I hate you!

Dennis: I know!
Madeline: Dennis. This is ridiculous. I'm telling your mother!
Dennis: Oh no you're not!
Madeline: Oh yes I am!
Dennis: She's gonna' die!
Madeline: She's not gonna' die. Doris! Dennis and I have something to tell you!
Dennis: No we don't!
Madeline: Yes we do. (Madeline and Dennis turn to a new direction - speak to Doris off stage)
Doris, Dennis and I- (Doris has a concerning physical reaction off stage.) Doris!?
Dennis: Mom!? (They react to Doris’ question off stage.) Divorced? No! Of course we aren't
getting divorced!
Madeline: Dennis!
Dennis: She is going to die! (drags Madeline back to their chairs) Look Mom! (gets close to
Madeline) We love each other! No divorce. I promise. We love each other.
[Dennis settles back into his chair, pleased. Madeline crosses her arms, annoyed.]
Madeline: (defeated) I hate you.
Dennis: (puts his arm around her) I know. We'll tell 'em at Easter!
[Madeline freezes with his arm around her – Dennis grins and winks at the audience.]
```

---

## IC-0854: It’s an Emergency

- Title: It’s an Emergency
- Author (byline): Lisa Ridarelli
- Work: It’s an Emergency
- Publisher: Mushroom Cloud Press
- Publication date as stated: September 1, 2022
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1254
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
By: Lisa Ridarelli

Cast of Characters

PALOMA

SERGIO

Setting

Paloma’s apartment

(PALOMA, in neat silk pajamas, lounges on couch. She drinks tea, talks on the phone.)

PALOMA

Thanks for checkin’ on me. (Pause.) Yea, it’s been a few months. Nope. Have not seen him. I’ve got an oil diffuser misting, calm music. Pretty much a living room spa. (Pause.)

You said, I’m resilient? Whew, I like that. Of course. Okay, muah, bye.

(PALOMA hangs up, takes a moment, sighs,
smiles to herself. She sips her tea, sits down
to journal. DOORBELL. She looks through
the peep hole.)

PALOMA

(To herself) Oh no. Oh, no, no, no, no. (Through the door) I have nothing to say to you, Sergio! Zero reason to communicate!

SERGIO

My name’s not Sergio. I’m here with pizza. It’s... Fred.

PALOMA

Fred? Yeah, and I’m freakin’ Ethel! I see you through the hole. Seriously, pretending to be Domino’s? Nuh-uh. You are no Fred!

SERGIO

Yes, I am. I’m Fred, the local pizza guy.

PALOMA

Your mustache is lopsided. The “Dominos” on your hat is in craft glue. And I don’t eat pizza-- I’m keto! (Pause.) Is this an emergency?

22..

(Pause.)

SERGIO

...Yes.

(PALOMA heaves, swings the door open as SERGIO ENTERS.)

SERGIO

Of the heart.

(She slams the door on him again.)

SERGIO

Ugh, Paloma! For real! It’s important! Please let me in. You’re the love of my life. You’re my everything. I’m only in town for this one last hour. Then I leave forever. And I feel like it’s all over now...

PALOMA

‘Cause it is!

SERGIO

I might as well just stop trying...

PALOMA

Please do!

SERGIO

Just quit it all!

PALOMA

Hey, whoa. What now?

(She opens door, steps back. It just got real.)

SERGIO

(As he enters) Naw, oh no, not like that. I won’t do anything like that. (Speaking very gently) I brought some of your very personal items I know you could not live without.

(Taking items out of a bag) Here-- jewelry, salt lamp, your cat mug.

PALOMA

Won’t you come in.

32..

(SERGIO smiles, gestures for a hug or kiss. Paloma presents hand for a handshake. He tries to kiss it, she pulls away.)

I said emergencies only so this best be urgent. Speak.

SERGIO

Yea, absolutely. It is. As I was saying...

(He goes to sit.)

PALOMA

I didn’t say get comfortable.

SERGIO

Oh, sorry, yes, my dove.

PALOMA

Dove???!!

SERGIO

Apologies!! Old habits. Ugh, my sweet doe eyed--

PALOMA

Agggghh!!!

SERGIO

I mean, Paloma! Seriously didn’t mean to. Imma get right to it. The emergency is...

Kristoff... is dead.

PALOMA

Oh God. As in, a passing? A transition to the other side? I’m... beside myself. I’ve been barbaric. That is awful. I’m sorry I’ve been a villain. Here...

(PALOMA extends her arms for a hug. They stand and hug for a moment. SERGIO fake cries, whimpers. While hugging...)

Hey. Everything’s gonna be alright. Oh, I’m so sorry. (A beat) Remind me, who exactly was Kristoff again?

SERGIO

My succulent.

42..

PALOMA

Ughh!! Seriously?! A plant!

(She shoves him off of her. Sergio goes flying back to the couch.)

SERGIO

Dang, girl!! You’re strong! You been boxing again?

PALOMA

You came here because a plant died?!

SERGIO

Well, hey listen! It’s more than that! Kristoff was an important plant, like family! Haven’t you heard that saying?

PALOMA

That’s pets. “Pets are like family.”

SERGIO

Kristoff came into my life the day we met. I thought you’d understand ‘cause... you connect deeply to the earth! You fed our plants Fiji water while we drank tap. You sang to them. I was hoping for maybe some sympathy, empathy, any of the thees!

PALOMA

Well, I’m sorry for your loss. But you can bury Kristoff out where I buried the number of craps I give.

(She shoos him to the door. He swoops around her, fakes a cough.)

SERGIO

Wait. Cough-- attack! Oh-- I’m choking! Choking! I need-- water!!

(He leaps over to the refrigerator, opens it, takes out a water filter, pours directly into mouth.)

SERGIO

Uh oh, someone’s drinkin’ Kiwi Strawberry Snapple. I know someone only drinks KSS when they feel down...

(He walks to her sweetly.)

Do you miss me even the teensiest bit?

52..

(PALOMA jumps to SERGIO, knocks him over. They roll over once on the floor, struggling.)

SERGIO

Whoa, you HAVE been training!

(She pulls him up and twists his arm into a locked position. He squeals.)

Ahhh... uncle! Mercy!! You win! You’re stronger than me! Please let go! (She lets go.)

Wheww!! Babe... I mean... understood. Time to go. Thank you for the moment of mourning, well, “observation.” And the water. (Beat.) Oh! I noticed you took down the picture of us on your fridge... no problem. I always carry a spare wallet size with me so I’ll just leave this one here on the counter for--

PALOMA

Sergio.

SERGIO

Yea.

PALOMA

Serge.

SERGIO

Yes.

PALOMA

Why are you really here?

(He looks at the ceiling. He takes one step closer. He cocks his head. Another beat of silence... then falls to his knees, bawling.)

SERGIO

I MISS YOU!!!! COME BACK TO ME, BABY DOVE!!! Please, my life is meaningless without you!!!!!

(He wraps around her legs.)

PALOMA

I’m sorry. It wasn’t just the one big thing. It was thing after thing after thing.

62..

SERGIO

That’s the thing! Things are just things! We can go back in time and redo the whole thing!

PALOMA

Like when I surprised you with a charcuterie, you told me I chose all the wrong cheeses and it was inconsumable!

SERGIO

Naw!! I just meant... traditional charcuteries usually have some mozzarella...

PALOMA

You’re the charcuterie master?

SERGIO

I was a cheesemonger...

PALOMA

So you know everything there is to know? You’ve met the creator of the first charcuterie?!

(She gets right in his face. A pause. For a moment, her frown melts into a small smile. Faces inches from one another.)

SERGIO

Yeah, that was Strabo, first century, Romans.

PALOMA

The word is French.

(They kiss, close-mouthed, tight-lipped. An angry kiss. Paloma wipes her mouth and pushes him off.)

Ughhhh!

SERGIO

Did that mean--

PALOMA

No!

SERGIO

Are you sure ‘cause-- 72..

PALOMA

Certain. Okay, we’ve had a memorable goodbye. Could you please?

SERGIO

Yes. By all means. I know our time has truly come to a close. My parting words are-- hold up. Is this... the playlist I think it is?

PALOMA

It’s on shuffle. If you like the song, that’s coincidence.

SERGIO

No!!! It’s a sign!! Our wedding playlist!! Phil Collins! You WERE thinking of us-- we were gonna play this at the wedding!

PALOMA

Sure, before you decided to cancel days before! Trust me, not on purpose.

SERGIO

Paloma! Remember, we danced to this, just us? (He extends his hand for a dance. She slowly advances, wincing.) On Terrell’s patio with the big Christmas lights that one July?

And you made a whole playlist the next day.

(A moment between them as they slow dance. Time slows down.)

PALOMA

Ahh, yes. You’re referring to the playlist I spent six hours curating. Yes. (Beat.) Now six hours of my life that I will never get back. Because someone... decided weddings were too trendy and mainstream and wanted to cancel days before?!! (Breaking out of the dance.) Now I don’t know if I EVER wanna get married! I’m questioning all of existence! The only one who can give me the peace I need is my ferret, NUZZLES!

SERGIO

Paloma. I apologized. I know I was a monster. I just looked around at everyone getting a divorce. On top of climate change and capitalism and world hunger and disease and I-- I admit it, I snapped! I freaked out! But don’t you remember-- this was our song?

PALOMA

Mmm, yes, I do remember. I said, “Phil Collins is my favorite too.” Well, guess what...

IT’S OVERPLAYED!!!

(BAM! She stomps on his foot. He grabs it in pain. PALOMA smiles to herself, takes a sip of a drink. SERGIO hops.)

82..

SERGIO

Alright! Understood. I see that our door is closed and you’ve swallowed the key. You’ve tied up the brown paper packages with string.

PALOMA

What do I have to do in order for you to scurry away, peacefully?

SERGIO

Wow. Whew... well may I make a kind request for one final hug goodbye?

(A pause. He looks teary-eyed, bats his eyelashes, opens arms. They start at one side of the room and over the next monologue, Paloma gradually backs him to the other side, by the door.)

PALOMA

You have my enthusiastic consent... to pay me $20,000 for the other half of the wedding!

Plus the cost of the private honeymoon boat I had to cancel, without refund! While you’re at it, send me my rustic napkin holder, the extendable mango wood coffee table, and my matcha tea set! You can buy a new damn plant. This is NOT an emergency!!!

(He is cowered into a corner, the shape of his body is tiny. He squeaks out...)

SERGIO

Can we be friends?

PALOMA

AHHHHH!!!

(Paloma picks him up, they grapple, slap their hands rapidly and awkwardly, have a back and forth. She then lifts him up off the ground, tosses him over her shoulder into a fireman’s carry. She carries him out the door, takes him off, goes back in, and slams the door in a huff. She collapses to the floor. A beat. Sergio sneaks around the exterior of the entire building to a window. A few beats. Then through the open window...)

SERGIO

Owwww, ow, ouch!! Paloma, darling... I mean... girl. For real-- uhh, I definitely just broke my ankle! (Knocking) Swear to God. Please, this is not a joke, not kidding!

Paloma, pleaaaseee!! It’s an emergency!!

End of Play
```

---

## IC-0855: Shakespeare in Like

- Title: Shakespeare in Like
- Author (byline): Shawn LaSota
- Work: Shakespeare in Like
- Publisher: Mushroom Cloud Press
- Publication date as stated: September 1, 2022
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, WILLIAM, WOMAN
- Teaser before the introduction: No
- Spoken words (computed): 1492
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
A Humorous Duo Script

By Shawn LaSota

Shawn LaSota
524 N. Wood St
Erie, KS 66733
(620)249-9587
shawnlasota@gmail.com

©2022 SHAWN LASOTA

CHARACTERS:

WILLIAM: It’s William Shakespeare, a somewhat oblivious man trying to write a romantic poem that is less than flattering to the woman he is trying to woo.

SHAKESPEARE IN LIKE

WOMAN: A blunt woman with a shrill voice that makes nails on chalkboards and fighting cats sound like a symphony. She is not an intellectual woman, but serves as the comedic and down-to-earth voice of reason within the play.

Synopsis: William Shakespeare is trying to make his lady swoon by writing Sonnet 130 and reciting it to her. Unfortunately, it does not turn out to be as flattering as intended, and this mistress does not mince words with her dissatisfaction.

SHAKESPEARE IN LIKE

SHAKESPEARE IN LIKE

WILLIAM and WOMAN are at center stage. He has a book open in front of him along with a quill, violently scribbling. The WOMAN is bored, looking around at the scenery and sighing loudly for WILLIAM’s attention. He acknowledges this by glancing over his shoulder with an annoyed expression.

WOMAN: Willy, I’m bored…

WILLIAM: William, please, darling. Just a moment longer.

WOMAN: But you’re taking so loooooong.

William: (under his breath)And yet, it will take longer the more that you interrupt me with your incessant whining.

WOMAN: Did you say something?

WILLIAM: No, darling. Of course not.

(William reads over what he has just written, dabs his notebook with his quill once more and beams at his beloved)

William: Finished. Possibly my greatest sonnet yet, darling, and it is all for you.

Woman: What’s a sonnet?

WILLIAM: SHAKESPEARE IN LIKE

A what now?

WOMAN: You said “sonnet.” What’s a sonnet?

WILLIAM: Well, it’s a poem. A lyrical sort, I suppose. It is fourteen lines long. Three quatrains and a final couplet. All of it is written in iambic pentameter.

WOMAN: I am big what?

WILLIAM: Iambic pentameter. It means 5 feet of 10 syllables paired into stressed and unstressed rhythm that...you know what...never mind.

WOMAN: Well, I’ve never heard of any poem like that before.

WILLIAM: I know, I just sort of, you know, created it.

WOMAN: You did? Really? Well, what are you going to call these types of sonnets?

WILLIAM: I’m going to call them...Shakespearian Sonnets.

WOMAN: Really?

WILLIAM: What?

WOMAN: A little on the nose, don’t you think?

WILLIAM: SHAKESPEARE IN LIKE

What’s wrong with it?

WOMAN: I just think a guy that writes a lot about hubris being a downfall to several characters ought to be a little bit less full of himself.

WILLIAM: Ah, well...maybe you’re right. I’m sure someone else will come up with a better name for this type of sonnet. But alas, I have finished and it is perhaps the most romantic sonnet I’ve ever written...and it was entirely inspired by you, my love.

WOMAN: Really? Oh my God. What’s it called?

WILLIAM: Sonnet...130.

WOMAN: Seriously?

WILLIAM: What?

WOMAN: That’s the best you’ve got. Sonnet 130?

WILLIAM: Well, it’s the 130th one I’ve written.

WOMAN: So you can write super long plays, but you can’t name a 14-line sonnet?

WILLIAM: I’ll worry about it later. Would you like to hear it?

WOMAN: Who were the 129 others for? Huh? How many other women have you written sonnets for?

SHAKESPEARE IN LIKE

WILLIAM: Probably not as many as you’d think.

WOMAN: What?

WILLIAM: Nothing, my love. Would you like me to recite it to you?

WOMAN: I suppose…

WILLIAM: (clears throat) My mistress’s eyes are nothing like the sun; Coral is far more red than her lips’ red; If snow be white, why then her breasts are dun; If hairs be wires, black wires grow on her head. I have seen…

WOMAN: Are you out of your mind?

WILLIAM: I’m sorry, my love?

WOMAN: What did you say about me? You balding one earring wearing son of a…

WILLIAM: What is the matter, my dear?

WOMAN: My eyes aren’t like the sun? My skin is pale? My hair is like wires growing out of my head? And what on Earth did you say about my breasts? Dun? What the hell is that? Sounds like you’re calling them a nasty grayish-brown color…

WILLIAM: (nervously)No, it means they’re...um...wonderful.

SHAKESPEARE IN LIKE

WOMAN: It better. If this poem doesn’t turn around fast, then I’m going to make it so it's your skull some Danish guy in a leotard is having a conversation with, if you catch my drift.

WILLIAM: Yes, dear. It will all make sense in due time. (clears throat) I have seen roses damask, red and white, but no such roses see I in her cheeks; And in some perfumes is there more delight than in the breath that from my mistress reeks.

WOMAN: You think my breath stinks! Who the hell do you think you are?

WILLIAM: Please, my dear, I promise the romance is coming. If you’ll only be patient.

WOMAN: I can’t wait for you to see what I’m going to get you for your birthday…

WILLIAM: (clears throat) I love to hear her speak, yet well I know that music hath a far more pleasing sound...Crap...I heard it as I said it.

WOMAN: So I have an annoying voice now?

WILLIAM: Nagging at best, my love.

WOMAN: You vile standing tuck!

WILLIAM: Hey, that’s good. Can I borrow that?

WOMAN: Get on with it!

SHAKESPEARE IN LIKE

William: Okay, okay. I promise you, you’ll see that this is really super romantic. I grant I never saw a goddess go; My mistress, when she walks, treads on the ground.

WOMAN: So now I’m not graceful? Do I walk like I’m dragging a wooden leg?

WILLIAM: For the love of...will you just hold on?

WOMAN: This poem is one big insult. Apparently, I’m ugly, plain, colorless, stinky, and have an annoying voice. The only kind thing in it is what you said about my breasts being dun. (looks down at herself) And you’re darn right they are.

WILLIAM: Here it is, my dear, the last couplet. I promise you will see that this was all with good intention. And yet, by heaven, I think my love as rare as any she belied with false compare.

WOMAN: Go on…

WILLIAM: Well, that’s it. That’s the end of the sonnet.

WOMAN: Are you kidding me right now?

WILLIAM: It’s romantic.

WOMAN: Where? When? What part of that was intended to make me swoon and like you, huh?

WILLIAM: SHAKESPEARE IN LIKE

That couplet...it means that...well, even though you are not perfect, I love you in spite of all of those imperfections.

WOMAN: (sarcastic) Well, aren’t you just a knight in shining armor? How did I ever get so lucky to find a guy that would put up with my bad breath and annoying voice? What can I possibly do to show you my appreciation? You can dip your quill in my ink any time you want.

WILLIAM: Do you really like it?

WOMAN: No, you idiot. No woman wants to be told about her imperfections. We know them already, duh! We already know that we stink and fart and burp and do all the gross things that men do.

WILLIAM: (cringes) You do those things?

WOMAN: I will cut you, William. I’m in no mood! Yeah, we do those things, but we don’t want to be reminded of them and we don’t want you to make it like you’re taking one for the team by putting up with our bodily functions. We want to be spoiled. We want to be made to feel like the only woman in your world. We want to feel like goddesses and queens.

WILLIAM: Is that what you really want?

WOMAN: William, you’ve written such amazing love scenes...how have you still not figured out what women want?

WILLIAM: Well, the women in my plays are acted by men.

WOMAN: SHAKESPEARE IN LIKE

Figures. Women want to swoon. And no woman is going to swoon over being told that her breath stinks, you idiot.

WILLIAM: So, if I...compare you to say...a summer’s day? But say that you’re more lovely and more temperate...you’d be into that?

WOMAN: Keep talking.

WILLIAM: If I said things like...um...Rough winds do shake the darling buds of May, And summer’s lease hath all too short a date...

WOMAN: Go on.

WILLIAM: Sometimes too hot the eye of heaven shines, and often is his gold complexion dimm’d; And every fair from fair sometime declines, By chance or nature’s changing course untrimm’d.

WOMAN: Can’t trust that weather. Go on, baby, tell me more.

WILLIAM: (turns to her) But thy eternal summer shall not fade, nor lose possession of that fair thou ow’st.

WOMAN: Mmmm, now we’re cookin’.

WILLIAM: Nor shall death brag thou wander’st in his shade, when in eternal lines to time thou grow’st: So long as men can breathe or eyes can see, so long lives this, and this gives life to thee.

WOMAN: Oh, William, that was beautiful. Just wonderful. Did you come up with that right off the top of your head just for me?

SHAKESPEARE IN LIKE

WILLIAM: Um, yes. I totally didn’t have that pre-written and it most definitely wasn’t for a man.

WOMAN: That’s a really odd and specific thing to say.

WILLIAM: Fair enough.

WOMAN: Oh, William, that was just what I needed to hear. I love you, my darling.

WILLIAM: And I you, my love.

(They embrace)

WOMAN: Enough to give me your favorite bed?

WILLIAM: Well, I mean, let’s not rush into anything.

End Scene
```

---

## IC-0856: The Next Table

- Title: The Next Table
- Author (byline): Bridget Grace Sheaff
- Work: The Next Table
- Publisher: Mushroom Cloud Press
- Publication date as stated: September 1, 2021
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TOBY, ERICA
- Teaser before the introduction: No
- Spoken words (computed): 1236
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
Two cafe tables sit side by side onstage. TOBY is already seated at one table, his back to the other table. ERICA sits in the seat directly behind him so they are back to back. When she pulls out her chair, he turns around, they make brief eye contact and share a smile, and then she sits. They both read the menu. After a second, ERICA sneezes.

Beat.

TOBY: Cute sneeze.

ERICA: What?

TOBY: You have a cute sneeze.

ERICA: Oh. Thanks? You should hear me cough sometime. (she quietly rolls her eyes at herself in a “what is wrong with me” way and goes back to reading the menu.)

Beat.

TOBY: Gesundheit, by the way.

ERICA: Thank you.

Beat.

ERICA: Do you speak German?

TOBY: What?

ERICA: Sorry… Gesundheit is German. I just… nevermind.

Beat.

TOBY: It’s just a thing people say when you sneeze.

ERICA: Right, like “bless you.”

TOBY: Right.

Beat.

TOBY: If I had said “Bless you” would you have asked if I was a priest?

ERICA: No.

TOBY: Okay.

ERICA: Are you?

TOBY: What?

ERICA: A priest?

TOBY: No… I just… you sneezed.

ERICA: Right. Yes. This is my fault.

TOBY: For sneezing?

ERICA: Kind of.

TOBY: That’s silly.

ERICA: Yeah.

Beat.

ERICA: Gesundheit is a fun word.

TOBY: I was just thinking that.

ERICA: Yeah. (realizing she’s interrupting) Sorry. I’ll let you… go back to… not being a German speaking priest or whatever.

Beat.

TOBY: Have you (clearing his throat) ever been here before?

ERICA: Like… do I come here often?

TOBY: No, like, have you ever gotten the salmon?

ERICA: Oh. Yes, actually.

TOBY: How was it?

ERICA: I got food poisoning.

TOBY: What!?

ERICA: Oh my- I was totally kidding. I really didn’t. That was just a stupid joke.

TOBY: Okay.

ERICA: Really, I don’t know why I said that. It just slipped out.

TOBY: Yeah, okay. Beat.

ERICA: You’re not going to get the salmon now, are you?

TOBY: I’m thinking no.

ERICA: Really, I didn’t/ get food poisoning

TOBY: I’m kidding. I wasn’t going to get it anyway.

ERICA: Oh. Good.

Beat.

ERICA: Soup is good.

TOBY: Which soup?

ERICA: No, sorry, just… in general, I find soup to be… good… most of the time.

TOBY: Ah.

Beat.

TOBY: Are you eating with anyone?

ERICA: No.

TOBY: Oh?

ERICA: No, I like eating at restaurants alone.

TOBY: Is that a joke?

ERICA: That one’s actually not a joke.

TOBY: Oh. Beat.

ERICA: How about you?

TOBY: I don’t know if I ever thought about it.

ERICA: I meant, are you eating with anyone?

TOBY: Oh, no, I mean yes, I mean... not right now.

ERICA: I can see that.

TOBY: I’m on a blind date.

ERICA: Ew.

TOBY: I’m sorry?

ERICA: (lying) Nothing… I just sneezed again… is all.

Beat.

TOBY: What’s wrong with blind dates?

ERICA: I really sneezed! I wasn’t-

TOBY: My friends set it up for me. I’ve never met her.

ERICA: That’s, like, part of the point… right?

TOBY: Yeah… I guess you’re right. Beat.

TOBY: She could be perfectly wonderful.

ERICA: Or she could be awful or… a Republican… or eat cotton balls or something.

TOBY: Eat cotton balls?

ERICA: People do weird things. Beat.

TOBY: If she turns out to be the love of my life, you’re going to feel pretty stupid.

ERICA: I feel pretty stupid all the time, not much changes that.

TOBY: Sorry… I shouldn’t have-

ERICA: (laughing) You were kidding, I can appreciate that. Beat.

TOBY: At least my joke was funnier than saying that the salmon gives you food poisoning.

ERICA: Are you still on that?

TOBY: I’m just saying.

ERICA: You should focus on your date.

TOBY: She’s not here yet.

ERICA: Well, then maybe focus on the fact that she could have very well have already come in and left the second she saw you.

Beat.

TOBY: Do people really do that?

ERICA: I was kidding!

TOBY: No, like really, do they really just leave before getting to know you?

ERICA: I don’t know. I mean… I can imagine it happens. But I only ever imagine the worst things happening, okay? So, don’t take my word for it. I don’t know you, I don’t know her, I’m just going to sit here and eat soup because I happen to like most soups.

Beat.

ERICA: Though, it’s a little hot outside today for soup, so/ maybe I’ll get-

TOBY: I’m not like you, okay. I’m an optimist. I give most people the benefit of the doubt and assume they wouldn’t judge a book by it’s cover.

ERICA: Sure.

TOBY: And I think if she did show up and she did walk out… then it’s her loss. Not my loss. Her loss.

ERICA: This is a really good pep talk.

TOBY: Or she could just be running late.

ERICA: Which is also rude.

TOBY: Sometimes people run late.

ERICA: You know, if you eat alone you can avoid that issue altogether.

TOBY: But then who would I talk to?

Beat.

ERICA: What’s her name?

TOBY: What?

ERICA: Your date? These friends of yours, they told you her name, right?

TOBY: Tiffany.

ERICA: Tiffany. And what’s your name?

TOBY: Why?

ERICA: I wanted to know if your names go well together. Like, my name is Erica so I can’t date an “Eric” or an “Aaron” or a “Cole.”

TOBY: (pronouncing the names) Eric, sure… (Aaron) Errr-on… sure… Co- (wait)... Cole... Why not a “Cole”?

ERICA: I just think Cole is a stupid name.

TOBY: Oh. Beat.

ERICA: If you’re not going to tell me your name, I’m going to assume you’re a spy or something.

TOBY: I’d be okay with that.

ERICA: Fine. I’m just saying I have an instinct for these things and you not telling me your name is not a great sign. Beat.

ERICA: Unless… is your name Cole?

TOBY: No.

ERICA: Did I totally offend you, Cole?

TOBY: No, no, it’s… I’m Toby.

ERICA: Toby. Beat.

ERICA: Toby and Tiffany. T-t-t-Tiffany and T-t-t-Toby. Sittin’ in a T-t-t-tree.

TOBY: (a little annoyed) Yes, I know, two “T” names.

ERICA: Caught that, did ya?

TOBY: Why do you think I didn’t want to tell you?

ERICA: Relax. You shouldn’t care so much what other people think.

Beat.

ERICA: (singing DEEP BLUE SOMETHING under her breath) “And I said ‘what about Breakfast at Tiffany’s?’ You said ‘I think I remember the film’-”

TOBY: It’s doomed. This is going to be terrible.

ERICA: T-t-t-terrible.

TOBY: I’m serious.

ERICA: Don’t- You’re going to be fine.

TOBY: What if I’m not? What if she’s… I dunno, what if she hates me?

ERICA: This is why I don’t like blind dates. There’s all of this expectation and build up over someone you don’t even know.

TOBY: Aren’t all dates like that?

ERICA: I don’t know… It’s just dinner. Shouldn’t you eat with someone you’re comfortable with? Who you can talk to like they’re, like, ordinary.

TOBY: Well, yeah, ideally. But how often does that happen?

Beat.

TOBY: You’re probably right.

ERICA: Who knows, anyway.

TOBY: I didn’t mean to disrupt your dinner or anything.

ERICA: I’m actually not that hungry.

TOBY: Oh?

ERICA: I mostly came in to… nevermind.

TOBY: What?

ERICA: It’s embarrassing.

TOBY: Okay. Beat.

TOBY: I’m not going to push it or anything, but I am imagining a lot of embarrassing things you could say right now and none of them are as embarrassing as the salmon-food-poisoning joke.

ERICA: I just- I came in to feel busy.

TOBY: What?

ERICA: See, nevermind.

TOBY: No, I’m not… I don’t think I understand.

ERICA: When you’re sitting in a restaurant you have things to do. Decisions to make. Things to read. It’s better than just wandering aimlessly.

TOBY: Do you wander aimlessly?

ERICA: Everyone’s gotta have a hobby.

TOBY: Okay. Beat.

TOBY: I don’t think that’s embarrassing.

ERICA: Really?

TOBY: No more embarrassing than being on a blind date.

ERICA: Yeah. I mean, no, but… yeah, thank you for saying that anyway.

Beat.

ERICA: Do you think-

TOBY: I think that’s her.

ERICA: What?

TOBY: My date. Tiffany.

ERICA: Oh. Tiffany. Well. There ya go. She didn’t come in and leave.

TOBY: Or she changed her mind.

ERICA: That too.

TOBY: So.

ERICA: Well, have fun.

TOBY: Hopefully.

ERICA stands to leave.

ERICA: You should get the salmon.

TOBY: (laughs) Okay.

ERICA and TOBY share a moment. Intense? Fleeting? A Change of Heart? It’s up to the performers and the audience. It could be different every time. Lights down.

END OF PLAY
```

---

## IC-0857: Tutoring Session

- Title: Tutoring Session
- Author (byline): Ellie Lynch
- Work: Tutoring Session
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS
- Teaser before the introduction: No
- Spoken words (computed): 834
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
Written by

Ellie Lynch TUTORING SESSION

CHARACTERS:

EUNICE is smart and in love with Frank.

FRANK is a dumb football player.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

EUNICE sits at a table on her phone. FRANK walks in hurriedly.

FRANK Sorry I’m late. Football went over.

EUNICE I told you. I have something at 5.

Frank puts his hand on Eunice’s. Eunice is visibly flustered.

FRANK Please don’t go. I need you.

EUNICE (O.S.) He needs me.

EUNICE (CONT'D)
I guess I don’t have to go to D&D
this week. Although I spent hours
writing my campaign..

FRANK Ew, Eunice. I don’t want to hear about your weird sex stuff.

EUNICE Oh, no. It’s-

FRANK
Plus, I’ve got to bring my grade up
in this class. Otherwise, I’ll have
to retake English over the summer
before college.

EUNICE Alright, so what are we doing this week?

22..

FRANK
Some Shakespeare story. I forgot
what it’s called. Here are my
notes.

Frank dumps out his book bag and shifts through multiple crumpled-up pieces of paper before he finds one.

FRANK (CONT'D) I think this is it.

EUNICE This is just a picture of a football.

FRANK Oh yeah. I got distracted in class today, thinking about football.

EUNICE
Frank, you really have to start
paying attention in class if you
want to get into-

FRANK Princeton, I know.

EUNICE
Wait, Princeton? Frank, I don’t
think you have a chance of getting
into Princeton. And I can say that
because I am not going to get into
Princeton. And I am your tutor.

FRANK
They said they’d give me a full
ride if I could get my GPA up to a
2.0.

EUNICE But..

FRANK
I know, I know. (Pause) I thought
Harvard was more my speed. But they
need me over there! They lost their
quarterback because of some arson
case that was totally rigged!

EUNICE I don’t- 33..

FRANK
Eunice! Focus! I’ve got a
scholarship to earn here, and I’m
paying you by the hour.

EUNICE Alright.

Eunice opens Frank’s textbook.

EUNICE (CONT'D) (CONT'D)
Ah, okay. Romeo and Juliet. I’ll
read for Juliet and you can read
for Romeo.

FRANK But I want to be the guy..

EUNICE No, Juliet is.. okay. Fine. You read for Juliet.

FRANK
Thanks for understanding, Eunice.
You know how it is. “Romeo, Romeo,
wherefore art thou, Romeo? Deny thy
father and refuse they name! And I
shall no longer be a Catapult.”

EUNICE “Capulet.”

FRANK Eunice, it’s not your line yet.

Frank gets a phone call.

FRANK (CONT'D)
Hey baby. No, no I’m not up to
anything. Football practice was
good, oh, yeah Carl’s in the
hospital again. Yeah, I tackled him
a little too hard, what a little
bitch. I fuckin told him if he
didn’t lean into the hits he’d end
up back in the ICU and all the
coaches agreed it’s really his own
damn fault at the end of the day.
Okay yeah I’ll see you at home. Bye
mom. Oh, what’s for dinner? Jesus
Christ, again? I’m just gonna order
pizza. Okay love you.

Frank kisses into the phone and hangs up.

44..

EUNICE (O.S.) He loves his mom...

EUNICE (CONT'D) Okay. We should get back to work.

FRANK Yeah, sure. Sorry.

Frank gets another notification on his phone.

FRANK (CONT'D)
Oh, shit! I just got my acceptance
letter from Princeton! I guess they
were just playing hard to get about
the whole GPA thing. Okay, never
mind Eunice. I guess none of this
really matters anymore. I’ll Venmo
you for the hour, though.

Frank rises and grabs his book bag. He pauses.

FRANK (CONT'D) (CONT'D) Also, I need to tell you something.

EUNICE (O.S.) This could be it!

EUNICE (CONT'D) Yeah.. me too.

FRANK Oh! Okay. You go first.

EUNICE
Well.. we’ve been meeting up once a
week since Freshman year of high
school and in these four years I’ve
really started to develop... well..
it’s a bit embarrassing really-

FRANK
Wait, Eunice. Sorry to interrupt
but you’ve had something in your
teeth this whole time and I
honestly have had no idea how to
tell you it’s so distracting.

Eunice looks into her phone and tries to get it out of her teeth.

EUNICE Did I get it?

55..

FRANK Not really, no.

EUNICE Anyways, what did you have to tell me?

FRANK
Oh, it was that. What I just told
you. About the shit in your teeth.
Anyways, as you were saying?
Sorry.. could you hurry it up? My
pizza is on the way.

EUNICE Oh.. um.. I got into that school I was telling you about.

FRANK Snead State Community?

EUNICE You remembered!

FRANK
That’s great. I think community
college will be a good pace for
you. Anyways, I’ve gotta go. I
guess this is it for us.

EUNICE Yeah, but I mean I’ll see you in class and stuff.

FRANK Well, sure. But it’s not like I’ll talk to you. My friends are there.

Frank starts to leave.

EUNICE Congrats on Princeton! Go tigers!

FRANK Don’t forget. The thing. In your mouth.

EUNICE Oh. Right. Thanks.
```

---

## IC-0858: 4-0

- Title: 4-0
- Author (byline): Taylor Shann
- Work: 4-0
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JACK, HELEN
- Teaser before the introduction: No
- Spoken words (computed): 1098
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
A bar, night. HELEN waits, checking her phone with a drink on the bar. Whatever is going on, she ain’t happy. JACK walks by, in his softball shirt with a softball, cheering:

JACK: FREE ENTERPRISE-ERS! FREE ENTERPRISE-ERS! FREE- (recognizes HELEN) Helen! Mr Boss man! Ms. Boss woman. Whatever!

HELEN: I’ve been calling. Several times. Texted you, 911. No answer.

JACK: No phones in the celebration zone!

HELEN: So you won.

JACK: WE won. Free Enterprise; best company softball team ever... (holds up ball) is 4-0. And we beat’em BAD. 10-2. Mark hit a homer, even the Intern scored a run. One more win, and our playoff slot is in the bag. I gotta send the results email-

HELEN: Jack- did you, by chance, hit Bill Henderson with a pitch?

JACK: I wasn’t aiming for him, but dude should’a moved. It’s softball, not baseball.

HELEN: The ‘dude’ is Bill Henderson, and you hit him in the face. Bill’s wife, Victoria Henderson, is the head of the Audubon society. Victoria called my boss, who called me, and now, I’m HERE. Talking to YOU.

JACK: And we won! Up top! (beat) That means high five. Up top!

HELEN Jack, I know the team is important to you, based on the emails you send out, to everyone, to people who work in the Hong Kong office, I know, because they email me about it, and they say, what the hell is this, and why the hell is in my inbox, and how did he get all these different fonts into ONE email-

JACK: I download them. I had to get past the work firewall, but, Rashmi helped with that.

HELEN: …yeah. Here’s the thing- the emails I can handle. But last month you threw beer cans at Doctors without Borders. Last week, you urinated in the ACLU’s Water cooler; and it’s on Youtube. Today, you gave a man a concussion. He may be bleeding internally. And do you know who you're playing next week?

JACK: Uh... the... they help out retarded kids. (she stares at him) AF something. I dunno. Mark should know. (she stares at him) What?

HELEN: The American Foundation for Disabled Children. Which is a charity that deals with DISABLED CHILDREN. I don’t want to hear the R word again. Are we clear?

JACK: Got it. No more reta- R words.

HELEN: Good. You're playing them Wednesday. And Jack. You're going to lose.

JACK: What?

HELEN: You and Mark and Rashmi and Intern, the whole gang, are going to lose against the AFDC. You are going to not win. You will be good sports about not winning.

JACK: (puts softball on the bar, leans back) Why would we do that?

HELEN: We put the softball team together to make us- the company-look good. We are an energy company, but we play non profits for charity and social causes. For PR. For them to not sue us. For 8 years.

JACK: 8 years of losing, until I got voted captain. Now we’re unbeatable.

HELEN Yes! You have beat them! Badly! Free Enterprise is the undefeated giant dick all stars of the NYC Charity Softball League. And every time you pee in the proverbial cooler, they call me. EVERY. TIME.. I am literally, one crying down syndrome child away from getting fired. So next Wednesday night, your email will say, in 12 point Times New Roman only, “FREE ENTERPRISE. LOSES.” Or I will make it my job to insure you no longer have one. Are we clear?

JACK laughs hysterically.

HELEN: Excuse me?

JACK: Every day I come in and I basically do the jobs of three people. Mark takes 2 hours to do what I do in 30 minutes. When I go on vacation, everything is on fire when I get back. So you’re going to fire me? Over this?

HELEN: I… spoke to HR. They say the decision is mine.

JACK: And how are you going to meet your end of quarter deadline without me, exactly? Last I checked, you thought Excel was something that makes the internet work.

HELEN: They SEE what you do all day. They track you on your computer, and what you do, after your work is done, is THIS. The team, the standings, the bar, the fonts.

JACK: I just want to make sure I understand you. You want us to throw away a 4-0 record so, what exactly, non-profits will approve of what we do?

HELEN: If them ‘feeling better’ means we don’t show up on the blogs, and I still have my job, then… yes!

JACK: Let me think about it. (picks up softball, tosses it in the air a few times) No. If you have to fire me, go ahead and fire me. Unemployment with Xbox sounds great. But no way is my team gonna throw a game against a bunch of retarded kids.

JACK goes to leave.

HELEN: If you go 5-0, I’ll disband the team.

JACK: ... You can’t do that.

HELEN: Take it up with HR. Lose, or lose your team and your record. No more equipment, entry fees, uniforms. No more bar tab. You're done.

JACK: I’ll quit.

HELEN: Good luck collecting unemployment, then.

JACK: You won’t meet your end of quarter earnings.

HELEN: I’ll give Mark your job.

JACK: Mark’s an idiot!

HELEN: Maybe, but Mark won’t get me fired. (goes to leave)

JACK: Damn it! (slams the softball on the bar). You took away espn.com. You took away Rum Fridays. You make me clock out when I go to the coffee cart. What did I ever do to you?

HELEN: Do you think I care that you print out sports columns and read them in the bathroom? Do you think it matters to me that your trips to the ‘coffee cart’ involve posting on facebook about the fact that dr pepper is on sale at the CVS around the corner? Do I think alcohol is the devil? No! But when my boss finds those columns, on the floor of the bathroom and your NAME is on it; when you’re not at your desk three times in a row on the same day in the same hour and my boss walks by, and when you walk through the front door with three twelve packs of soda you CLEARLY PURCHASED ON COMPANY TIME… they call me.

JACK: So your solution is this?! Just tell me to stop!

HELEN: I DID!

JACK: WHEN?!

HELEN: CHECK YOUR EMAIL!

JACK: I WILL! (checks his email, it takes a good twenty seconds) WELL I DIDN’T READ THOSE, I’M SORRY.

HELEN: FINE!

They both pause, still angry.

JACK: I’m good at what I do.

HELEN: I know, Jack. But you are such an ass.

JACK: I’ve never lost on purpose. At anything. Ever. Not even when I played HALO with my little sister.

HELEN: It’s just one game.

JACK: Yeah, for now. And what about the next charity? And the one after that? We got cancer, cars for kids, you name it.

HELEN: Jack, this isn’t about winning or losing. (picks up the ball) I’m just asking you play ball.

HELEN tosses the ball to him, he catches it.
```

---

## IC-0859: Buds W/Spuds Text copyright 2008 Frank Cernik

- Title: Buds W/Spuds Text copyright 2008 Frank Cernik
- Author (byline): Not specified
- Work: Buds W/Spuds Text copyright 2008 Frank Cernik
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ANCHOR, REPORTER, CHEF, COLUMBUS, SQUATTING DOG, LIES THROUGH TEETH, SLEEPS WITH CHILDREN, HISTORY NARRATOR, CONNOR O’BRIEN, HIPPIE TECHIE, CULT LEADER, WORSHIPPERS, DISCLAIMER GUY, STEVE IRWIN, ANNOUNCER, POTATO1, POTATO2, STUDIO AUDIENCE, SOLDIER, SIR
- Teaser before the introduction: No
- Spoken words (computed): 1134
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
Frank Cernik

Buds With Spuds

ANCHOR: Good evening, Ladies and what pass for Gentlemen, and welcome to the Tournament. I am the Anchor, and this is my colleague, Another Character. This morning, while most of you were asleep, or rather not, there occurred a terrible tragedy. Little Brian O’Connor, an Irish schoolchild and apprentice farmer, discovered that his morning potato had mold on it. As I understand it, Reporter is on the scene as we speak. Let’s pop over to him now. Is this news substantiated, Reporter?

REPORTER: Unfortunately so, Anchor. While most potatoes, when left alone, begin to grow offshoots, Brian O’Brien’s grew a strange tye-dye mold and sent his dog, tail between its legs, to the nether regions of hell. Apparently Brian was upset by this, but proceeded to eat the potato anyway. Back to you, Anchor.

(Channel change)

CHEF: So you toss on a couple dashes of bacon bits and then start talking with your mother-in-law over the phone. Remember to hold up the potato and imagine it to be her. It kinda looks like her, doesn’t it? It’s just as ugly, I’ll tell you that. See this lump here? Yeah, this one. Have you ever noticed how mothers-in-law always have inexplicable lumps in weird places at family reunions? Maybe her husband was just beating her, but, really, who could blame him? Well, anyway, after you’ve had enough, put the potato back on the surface and SMASH IT TO PIECES WITH YOUR TENDERIZING HAMMER. Voila! Mashed potatoes! And now I think our blender is done whirring, so let’s go check up on our potato shakes.

(Channel change)

(Indians/Native Americans/Indigenous Americans/American Indians gathered around a fire, passing around a peace joint and eating fry bread) (Columbus approaches)

COLUMBUS: Hola, Squaws and Warriors! What up here in da Hood?

SQUATTING DOG: Who the Trickster are you? Why are you so white? You look like Michael Jackson.

COLUMBUS: I am Columbus. I am an explorer in the service of the buxom Queen Isabel. Just giving you the heads up, I just discovered you, so now you belong to Spain. Who are you all?

LIES THROUGH TEETH: That’s Squatting Dog, I’m Lies Through Teeth, and over there is Sleeps with Children.

SLEEPS WITH CHILDREN: (Holding up both hands, following word making fun of stereotypical Indian greeting) How … do you live without tasting of the young flesh? You want to go out sometime and have a Shirley Temple on the rocks or something?

COLUMBUS: Sure! Just make sure she doesn’t have Syphilis first! (laughs) (cut to SqD, LTT, and SwT, who aren’t laughing)

SLEEPS WITH CHILDREN: That’s not funny.

LIES THROUGH TEETH: Dude, just take this potato and leave, alright?

COLUMBUS: Deal!

HISTORY NARRATOR: Columbus then climbed onto the Niña and sailed away, throwing the potato at an Irish Farmer as soon as he could. The Farmer, a drunkard by the name of Connor O’Brien, was knocked unconscious.

CONNOR O’BRIEN: (reawakening, thick Irish accent (duh)) What’s this? It’s a strange brown lump! It’s a message from God, may He rest in peace! I must shove it into the earth that I may grow more messages from God!

HISTORY NARRATOR: Still extremely drunk, Connor then turned to the side and vomited a great vomit. As he retched, he noticed that the sound he made sounded like “Pleh-raaa-do!”, and so named this message from Columbus the Potato, though Dan Quayle would argue with this divine inspiration, and respell the word with an e at the end.

CONNOR O’BRIEN: A Potato! Forget my other crops, this sucker’s taking up my entire plot of land. (begins ripping out other crops)

HISTORY NARRATOR: The nearby farmers soon began to emulate O’Brien and stocked up on the savory starch. In doing so, they set themselves up to die during the Great Potato Famine by creating an unhealthy reliance on these root vegetables that were brown on the outside and white on the inside. England soon developed an insatiable craving for this inverted Eminem and sent a colonizing fleet to the Americas. Within a few short years, Idaho was born.

(Static, then a new character appears)

HIPPIE TECHIE: Hai thar! This is the Hippie Techie, and I’m going to tell you what really brought potatoes to the worldwide attention. This isn’t what the government wants you to know. I don’t have much time before they find me, but you have to know: Potatoes are a government conspiracy. You all know about Roswell. What was in those UFO’s was potatoes. In their own language, they are known as Spuds. The Irish and the Idahoans see Spuds as superior to our species, and are all cultists in a cult! I have footage! Hold on a sec, I’ve got to upload it…

(Potato worship footage)

CULT LEADER: We are the Spuddites! We like Spuds! After death, where do we go?

WORSHIPPERS: We become eyes in the Immortal Potato!

CULT LEADER: What do we call it???

WORSHIPPERS: TUBERDOM! TUBERDOM! TUBERDOM!

CULT LEADER: Now, who has the sour cream? Let us sacrifice a RADISH!!!!

WORSHIPPERS: (shout in mob madness glee)

(back to reality)

HIPPIE TECHIE: After that it gets pretty racy. Harmless as these people may seem, we cannot allow Spuds to take control of the planet! Eat them, my brethren and sistren! Eat them while you still can!

DISCLAIMER GUY: This message has been paid for by the Potato Farmers of America and the Ireland-Idaho Coalition, and approved by the former Bishop of Turkey.

(Channel change)

STEVE IRWIN: We’re in the Idaho outback right now, tracking down the wild Sweet Potato. Now be warned, these little buggers are a lot more dangerous than their name would suggest. Look! Over there! That’s a big one! Now, I’m going to go run at it and tackle it, exposing every part of me possible, however, I assure you, I am in no actual danger. (runs, jumps, is hit in the chest) Oh, bugger! This one’s stinger got me in the chest. I can feel the venom spreading quickly. It seems that this one got in a lucky shot to my heart!

(Channel change)

ANNOUNCER: And now, back to Everyone Loves Potatoes!

POTATO1: (stays still, does nothing)

POTATO2: (ditto)

POTATO1: (repeats itself)

STUDIO AUDIENCE: (laughs hysterically, some catcalls)

(Channel change)

(Battlefield in Iraq/Afghanistan/Some other country)

SOLDIER: We are under heavy fire! I repeat, under heavy fire! There are potatoes flying everywhere! I just saw Corporal O’Connor’s head explode! There were bacon bits everywhere, and I got some butter on my hand, and we’re running out of shredded cheese and Mrs Dash! It’s a bad time to be us, sir! Are you sure that the enemy’s gravy stockpiles are here, sir?

SIR: Private, you are not being employed to ask questions! Complete the mission! I don’t care if they’re throwing chives at you! You take them out, you get the gravy, you get back here, and I’ll give you a medal! Is that clear?

SOLDIER: Yes sir, I’m just not sure if this biological warfare is worth it all, sir!

SIR: Those are the thoughts of the weak! Buck up, Soldier!

SOLDIER: Sir yes sir!

(Channel change)

ANCHOR: Well, that was certainly an interesting story. Parents, you can take your hands off of your children’s eyes and ears now. That’s about all the time we have today, but I’d like to conclude with an interesting factoid: The tumor that had inhabited Lance Armstrong’s left testicle looked a lot like a Spunta variety potato. So be careful next time, because the potato you’re eating just might wind up giving you cancer in your balls. I’m the Anchor, and this is Another Character, and this has been Humorous Interpretation. You stay snazzy, Speech and Debate.
```

---

## IC-0860: CHILD'S PLAY A Play, by Alyssa Zaczek

- Title: CHILD'S PLAY A Play, by Alyssa Zaczek
- Author (byline): Alyssa Zaczek
- Work: CHILD'S PLAY A Play, by Alyssa Zaczek
- Publisher: Mushroom Cloud Press
- Publication date as stated: 2013
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: RYAN, JESSICA, RYAN & JESSICA
- Teaser before the introduction: No
- Spoken words (computed): 2818
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
SCENE I At center, RYAN, a charming yet awkward Jason Bateman-type, speaks to the audience.

RYAN: My life is filled with routine. I don’t mind it, actually, I’m a man of simple means. I like toys. I love the nostalgia of things from your childhood, you know? GI Joes and trains with whistles and Rock’em Sock’em Robots. They’re comforting. So every morning I get up, I cook breakfast, and I go to work. At a toy store. It’s been the same for years and years, until she showed up. You would think I’d recognize trouble in high heels when it walks right towards you and introduces itself, but it’s been so long without trouble for me, I guess it took me a while. The scene shifts into Ryan at the toy shop, struggling with a remote control, trying to get a helicopter off the ground. JESSICA, sultry and captivating, watches, unbeknownst to him. After a few attempts to get the helicopter moving, Jessica speaks:

JESSICA: Still playing with toy helicopters, huh? Some things never change. Ryan, flustered, drops the remote control and turns in a hurry.

RYAN: Jesus, I’m sorry, ma’am, I didn’t see you there. (With obligation; this is the usual spiel: ) Welcome to Toy Tantrum: Our Toy Selection is Cr-azy! How may I help you?

JESSICA: (After a beat) You don’t recognize me?

RYAN: I’m sorry?

JESSICA: You don’t recognize me.

RYAN: What-

JESSICA: Gangly little Ryan Richards, still playing with toys after all these years. She smiles in disbelief as a look of comprehension washes over Ryan.

RYAN: Wait . . .

JESSICA: (Singing) Oh, Camp Kickapoo, we’ll spend a week at-you, and cook a s’more or two, in the summer sun!

RYAN: Jessica? Jessica Monroe?

JESSICA: Good to see you again, Ryan.

RYAN: Oh my god. Wow. The last time I saw you-

JESSICA: We were seventeen?

RYAN: Yeah. Yeah. Wow.

JESSICA: So this must be your toy store, then! The one you talked my ear off about opening. Good for you!

RYAN: Uh, no, not exactly.

JESSICA: Oh?

RYAN: My wife and I are trying to save up for me to open a store of my own, but for now I just work here. I’m a manager.

JESSICA: (Taken aback) Your wife?

RYAN: Nancy.

JESSICA: Nancy Lewis? That know-it-all math freak from camp? (Ryan grimaces; she realizes what she’s said) Sorry.

RYAN: Yeah, that’s her. She’s Nancy Richards now. (An awkward beat) So, what brings you back home? Last I heard you were some hot-shot advertising executive in the city.

JESSICA: Ah yes, my fame and fortune in the city. Well, that came to a grinding halt last week when I got fired. (Laughs) Thirty years old and getting canned like I’m a teenager working at a pizza stand all over again. So I had to move back home. Can’t afford the hot-shot apartment and the hot-shot life anymore.

RYAN: Oh. Jes, I’m sorry.

JESSICA: That’s alright. But it brings me to my next question: are you hiring? SCENE II The scene shifts to Ryan and Jessica sitting at a table in the Toy Tantrum break room. It is after hours. They drink coffee, and our first sight of them is a burst of laughter, having been in conversation.

RYAN: So that was your first day in toy retail, huh?

JESSICA: Needless to say I know nothing about children’s toys. Or children! I don’t know why you even hired me.

RYAN: Hey, anything to help a friend.

JESSICA: Well, thanks. It was good of you. I’m surprised you don’t have a store of your own by now, really. I don’t mean anything by that, it’s just . . . you were always so passionate about the toys of your childhood, you know? All those stories you told me about your father playing Lincoln Logs with you before he died; they were sweet. I really thought . . . I don’t know, I really thought you would make it.

RYAN: We’re working on it. It’s been hard-

JESSICA: Supporting the kids?

RYAN: What? Oh, no, we don’t have any kids.

JESSICA: Why not?

RYAN: Nancy never wanted them. Too focused on her work. Accounting, you know, it’s sort of taxing. No pun intended.

JESSICA: That sucks.

RYAN: What?

JESSICA: Ryan, come on.

RYAN: Come on, what?

JESSICA: You’ve always wanted kids! Even at seventeen years old you couldn’t shut up for a week about all the stuff you wanted to do with your kids when you were a dad! You want to open a toy store, for Christ’s sake, like some sort of new-age Willy Wonka! You were born to be a dad!

RYAN: I don’t know about that. . . Nancy was just always more work-oriented. And I loved that about her-

JESSICA: Loved? Past-tense?

RYAN: (After a beat) Look, if you must know, things haven’t been great lately, that’s all I’m going to say.

JESSICA: Well. (There is a pause, as Jessica takes a sip of her coffee. Ryan watches her.) What are you looking at?

RYAN: Remember that night at camp, when we snuck out of our cabins and went down to the lake? And it was getting colder at night by then but you still insisted that we try to get into the water? So we stripped down to our underwear, and I watched you the whole time, by the way, and when we waded in up to our chests we were shivering and blue. And you felt something brush against your leg – a fish or a piece of seaweed or something – and you screamed, like your family had been axe-murdered, and jumped against my chest with that splash – Jesus, I thought you were going to wake every counselor on the place. But instead you just looked at me, and you started to laugh, like it was the funniest thing in the world, like you were a movie star, and you-

JESSICA: Kissed you. (Looking up from her coffee, smiling) I kissed you.

RYAN: And it was the most amazing first kiss I’ve ever had, I think. Even if my lips were blue and my teeth were chattering and I smelled like lake water and seaweed. (A beat) I don’t know, it’s just nice, remembering. Jessica stares at Ryan for a beat as he smiles into his coffee cup. Finally:

JESSICA: Are you stupid?

RYAN: What?

JESSICA: Do you honestly think that I came back home just to work retail in a kids’ toy shop? I could have gotten a crappy apartment and a mile’s worth of chain restaurants and shopping malls anywhere, Ryan, did you really think I had no other reason for coming back home?

RYAN: I . . . I thought maybe you missed your family, your old house . . . ?

JESSICA: Of course not!

RYAN: Okay, so what?

JESSICA: I remember the night we kissed. I remember it clear as day. It’s almost fifteen years later and I can still remember how our teeth clicked against each other’s before we found our rhythm in that kiss, that perfect kiss. Do you remember what happened next?

RYAN: Jessica . . .

JESSICA: We were inseparable. We wrote each other letter at night to give to each other in the mornings. We snuck out to kiss in the woods behind the cabins and we held hands at the campfires. We talked about what we’d be doing at twenty, at twenty five, at thirty. We fell in love.

RYAN: Jes, please-

JESSICA: Didn’t we?

RYAN: (Hesitantly) Yes.

JESSICA: And almost fifteen years later, part of me feels like I missed out on a huge . . . something. Like a chunk of my life is missing because I didn’t call you after camp. You know, life happened, and we both got busy with our own things, but . . . doesn’t part of you wonder if you were supposed to end up with your first true love?

RYAN: I’m married, Jessica.

JESSICA: Yes, and you haven’t said a single good word about your marriage yet! But you can sit in front of me and reminisce about the good old days, about a romance that happened so long ago? About watching me undress in the moonlight? That’s not a healthy marriage, Ryan, that’s denial!

RYAN: And what is it you came here expecting me to do? Leave my wife? Get a divorce and run away with you? Jessica stands, and leans against the table, looking down at Ryan. She is a vision in sex-appeal.

JESSICA: Haven’t you thought about it? Every once and a while? What would have happened back then, had we ever gotten a place to really have privacy? If maybe I wouldn’t have been just your first love, but your first-

RYAN: You didn’t call me. You told me you’d call and you never did. I tried to call you but your parents always told me you were out. It’s been over a decade, and you expect me to fall to my knees in longing for you? What world are you living in?

JESSICA: I’m living in the world where I never stopped loving you! (A beat) I have no excuse for not calling you. I was . . . afraid, of how much I loved you, after so short a time. And I know that’s the worst excuse in the book, I know. But we used to lay out on the grass and talked about our futures; about a life together. We did! I know you’re going to try not to remember it now, but we wanted this.

RYAN: Well, I grew up. Those were children’s fantasies.

JESSICA: We were old enough to know what love felt like! And don’t act like you’re so mature now; which one of us has spent their entire adult life working a dead end job at a toy store and which one of us moved on?

RYAN: (Exploding) I don’t know, Jes! You tell me! Because you’re the one holding onto a relationship that barely happened, fifteen years ago! You’re the one that never got over a fling at summer camp! I’ve had a life since then! A job, a wife, a mortgage! What do you have? What do you have? A beat. Jessica has recoiled; Ryan is now standing up out of his chair in anger.

JESSICA: I don’t have much, Ryan, and I know you think I’m out of my damn mind, but I have love for you. I have thought about you so often. And maybe your wife loves you too, I don’t know. But I think she loves her job more than she’s ever loved you, the real you. I remember the Ryan who, at seventeen years old, had a budgeted plan for becoming an entrepreneur after college. I remember the Ryan who tinkered with anything that moved and loved games, like Red Rover and Capture the Flag. I remember the Ryan that was filled with joy and life. The person I see in front of me is sad, and beaten down. And . . . I would take care of you. I’d help you with your dream, too. I’d see you, for who you really are.

RYAN: Nothing would change. You work here, I work here. If we quit, we’re unemployed, we’d have to move, the divorce would cost money, we’d go bankrupt. We’d be homeless, for God’s sake.

JESSICA: We’d figure it out.

RYAN: Dammit, Jessica, not everything in life can be solved with a little naiveté and hope!

JESSICA: I believe that it can!

RYAN: You’re a fool.

JESSICA: Come away with me.

RYAN: Stop.

JESSICA: I’m serious. We could leave tonight, tomorrow. You write Nancy a letter, and we leave. I have enough saved up for us to move to the city and get a god-awful apartment, but it could be something. I’ll get another job as an exec, I’m sure of it! And then, then we can open your store together. Get married, have a couple of kids, the whole white picket fence package. You could finally play catch with the son you’ve always wanted. A beat. Jessica has painted a beautiful picture of the life Ryan has, admittedly, always wanted. She crosses to him, takes his hands.

JESSICA: We could be a real family, have a real life. You could stop living this boring, exhausting gray one. I loved you then and I would love you just as much now. And I think . . . I think part of you feels the same way, too. Slowly, hesitantly, she reaches up and cups his face in her hands. She carefully and deliberately kisses him. He kisses back softly, for a brief moment, then puts his hands about her wrists and pulls them gently from his face, breaking their embrace.

RYAN: I know you won’t believe it, and I know you’d like to think that every love story ends with riding off into the sunset, but those are children’s tales. Love is not child’s play, Jessica. Neither is real life. I loved you then, that’s true, and a part of me always will. But ‘first love’, it’s not always the same as ‘true love’ or ‘forever love’. Nancy and I promised each other a forever. We’ve been with each other for birthdays, Christmases, Thanksgivings with her family and mine. We’ve had fights; we’ve seen each other cry. We’ve done normal couple things – dinners and movies and love making and doing nothing at all. We’ve built a life. And it’s not perfect. But it’s ours. This is my boring, exhausting, gray life. It’s not perfect, but it’s mine. And I’m not going to trade something that I’ve grown to love for something I’m not sure I can love forever. Jessica nods, and pulls away completely. She’s crying, a little.

JESSICA: I really thought-

RYAN: I know.

JESSICA: You must think I’m such an idiot.

RYAN: No, I really don’t. I think you’re brave, Jes, you always were.

JESSICA: Yeah, so brave. Brave enough to think I could change your mind. She laughs a sad little laugh. Ryan crosses to her, and kisses her forehead.

RYAN: Stay, and finish your coffee?

JESSICA: No, I better not. I better not. Consider this my official resignation, I guess?

RYAN: After one day? They’re going to think I scared you away.

JESSICA: They’re lucky I didn’t scare you away. (A beat) Take care of yourself, Ryan. And tell Nancy you love her when you get home, alright?

RYAN: Yeah. Yeah, I will, Jes. Take care. Jessica turns to leave, but stops herself short of the door.

JESSICA: One more thing. In a month or so, you’re going to get a letter from me. An invitation, to a party of sorts. Don’t be afraid to open it, okay? You should open it.

RYAN: (Bewildered, yet compliant) I will.

JESSICA: (Smiling, sadly) Goodbye, Ryan. She shares a final, lingering look with him, and then hums the Camp Kickapoo song as she exits. Ryan watches her go, even after she’s left. After a beat of this, he turns and speaks to us:

RYAN: I went home that night and kissed my wife. I told her I loved her, but I didn’t tell her about Jessica. It wasn’t something she needed to know. I didn’t think about it again until I got Jessica’s letter. It was a cordial invitation to the funeral of Ms. Jessica Monroe. Turns out that by the time Jessica ran into me, she was already dying, and she knew it. Cancer, eating away at her brain. She knew the whole time, and never said a word. I was almost angry, until another piece of paper fell out.

Ryan takes the letter from his pocket, begins to read.

RYAN: ‘Dear Ryan: If you’re reading this, then, well, you know what that means. I’m sorry I didn’t tell you, but I didn’t want you to feel compelled to take pity on the poor dying girl. I wanted – I needed – to know if you loved me back, for real. I got my answer, and that’s okay. I will always keep our time together close to my heart, and I’ll never forget- Seamlessly, Jessica’s voice takes over, as she steps out from behind Ryan to read the letter to him as he holds it in front of him.

JESSICA: -the times we kissed and the way you always made me laugh. First loves are a powerful thing, you understand. They stay with you. You were a good friend to me, right to the very end. Even after fifteen years you wouldn’t let me make an impulsive decision that wasn’t right for me, and I thank you for that. Ryan, please know that I-

RYAN: -I will always love you, and that –

JESSICA: -once I’m gone, you should forget any of this ever happened. All those things that I said and did, they were the ravings of a sick woman, living out her last romantic fantasy. But, I’m glad my last romantic fantasy was with you. Even if fantasy is all it will ever be. But before I go, promise me one thing.

RYAN: Buy your toy shop. Convince Nancy to help you find a way to do it, now. Co-invest, or something, I don’t care, just-

JESSICA: -do it. Not for me. God no, not for me. For you. For your dad, and the Lincoln Logs, and the children you may or may not ever have. Just do it for you, Ryan. Be a kid again.

RYAN & JESSICA: Love always, Jessica.’ Ryan smiles at the letter, and slowly folds it back up. After a beat, he addresses the audience a final time:

RYAN: My life is filled with routine. Every morning, I get up, I cook breakfast, and my wife Nancy and I? We open our toy store. And it will be this way for years and years. (A triumphant, beatific beat) Thanks to her. He smiles, and Jessica, his childhood love, smiles too. END OF PLAY.
```

---

## IC-0861: Countdown to Love Text copyright 2006 Andrew Messer.

- Title: Countdown to Love Text copyright 2006 Andrew Messer.
- Author (byline): Not specified
- Work: Countdown to Love Text copyright 2006 Andrew Messer.
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1201
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
John: (on the phone) Hi, Mom. Yes, I’m doin okay. Yes, the burning sensation is gone. No, the doctor said it wasn’t contagious anymore. Yes, there’s a speed dating event at one of the local clubs, and I’m planning on going. Oh, of course I’ll meet someone nice…

Countdown to Love

John: Okay, deodorant? Check. Smile? Check. Rugged good looks?
Announcer: LADIES AND GENTLEMEN! Welcome to Super Speed Dating, sponsored by KG95 Radio,
Brad’s Bridalwear, and the Gregson firm of Divorce Attorneys at Law. Now, ladies, please move to the
left, gentlemen, move to the right, and find your first date from the opposite line when time is called!
TIME!
Carly: (meditative artistic weirdo) I am…Carly.
John: Hi…Carly. I’m John. Umm, where are you from?
Carly: I am from my own mind…and Rhode Island.
John: Ah, not much space to move around there, I hear.
Carly: Are you calling me fat?
John: No…no, I…!
Carly: Well, no matter. For…my body is…a temple.
Announcer: 15 seconds remaining!
John: So, should we exchange numbers, Carly?
Carly: I don’t use telephones. They damage my aura.

John: Well, I most definitely don’t want to put a chink in your aura.
Can I email you?
Announcer: TIME!
John: ‘Can I email you?’ Ugh. How could I be so stupid? If her aura couldn’t handle a telephone,
imagine what effects the internet would have…Ugh! Oh, hi, I’m John.
Patricia: Hello, John! My name is…Patricia.
John: Well, it’s nice to meet you, but what’s with the script?
Patricia: John, have you ever dreamed of retiring early on a…beach in Malibu?
John: Umm, sure, who hasn’t?
Patricia: And do you use everyday household products like bleach, dishwashing detergent, hand lotion,
fabric softener, or tire sealant?
John: Well, yes…but not usually in that order.
Patricia: And do you have family and friends that also use these everyday household products?
John: Yes, I do. Except for Uncle Marvin, he’s not very…
Patricia: Grrreat! Now you and ten of your friends or family can realize your dreams of early retirement!
All I need is your address and Social Security number!
Announcer: TIME!
John: Strange…it was our first date and she already wanted to meet my family…hmm. Eh well…who’s
ne… Oh, dear…God…

(She towers above him, and character gives impression of being huge) Beilula: Howdy, sweet cheeks! I’m Beilula!

John: Hhhi. Um, I’m John. Nice to meet you. Where could you possibly be from?
Beilula: I’m from Oklahoma.
John: Oklahoma! You must have lived on a farm, then.
Beilula: Yep, my daddy has a pig farm. I still visit from time to time to wrassle those pigs.
John: You wrestle pigs?
Beilula: Oh yeah. Nothin’ like sackin’ pigs. You should try it sometime!
John: Well, I’m a little on the lanky and thin side, so, I’m not much good in the sack… department. I
mean, I could never get a pig in the sack. I mean...I could never sack a pig like you! Oh God…

(terrified;jaw drops)
Announcer: TIME!
John: She could have killed me with her bare hands! Okay…the next date’s bound to be better. Oh,
sophisticated, too… Um, hi, I’m John.
Rachel: Hi, John, I’m Rachel, I’ll be right with you, I’m on the phone with a client right now. Yeah, Bill,
that’s right…
John: Oookay………well, you know, we have a time limit…
Rachel: Yes, just hang on a minute, alright?! No, Bill, I’m still here…
John: Well, hehe, so am I…
Rachel: Look, shut up, okay?! No, not you Bill…Bill? BILL?
UGH! You blew it!
John: Sorry…but at least now we can get back to our…
Announcer: TIME!

John: Well…it was nice meeting you too…crap… Ohh, she looks interesting…
Violet: Hi, sexy. I’m Violet. And I have got just one question for YOU.
John: Hi, Violet. I’m John. Whhat’s your question?
Violet: How much money you got on you?
John: About 23 dollars, why?
Violet: Oh, well. For five dollars…I can tell you a secret. And for ten dollars, I can SHOW you a secret.
And for twenty three dollars…
Announcer: TIME!
John: Well, I feel a bit violated.
Darya: Hi, I’m Darya.
John: Hi, Darya? I’m John, I assume you’re my next date?
Darya: Yes, but I prefer the term intra-species relationship, it’s much more earthly. Speaking of the
earth….what…what are you wearing?!
John: Oh, actually it’s Aqua Velva…
Darya: No, no that! Your pants!
John: My pants?
Darya: Yes, where were they made? Let me see!
John: Where were they….HEY! Let go of me!
Darya: Let me see the tag!
John: Heeyyy! Ahhh!

Darya: Let me seee….*rriiipp* ‘Made in….INDONESIA?!’ *groin kick*
Announcer: TIME!
John: Oowww…well, where are your pants made…? Oh, there has to somebody for me in this crowd…
Autumn: My name’s Autumn and the most important thing you should know about me is that I have an
extra arm growing out of my…
Announcer: TIME!
Cheryl: Hullo there, I’m Cheryl! Oh, you’re quite the hunk of man steak! I’d like to fry you up in my
frying pan…
Announcer: TIME!
Ursula: I’m married to Jesus, and nobody else!
Announcer: TIME!
Eric: Uh, hi there. I’m Eric, and I could really use a friend right now. I mean, the ladies just aren’t going
for me, man. And I’m pretty sure I saw one of my exes, and she’s just like Satan incarnate…
Announcer: TIME!
Monica: Hi, name’s Monica. And while I don’t like to brag, I actually hold the record in Utah for longest
recorded high-speed police pursuit.
Announcer: TIME!
Terri: Hi, I’m Terri, but um, you have a piece of lint like right there. And um, here. And here. You’re
swimming in it. This is unclean. We need to get you vacuumed, and washed, and…
Announcer: TIME!

Martha: Hey kid. I’ve had a partial frontal lobotomy and a total hysterectomy…so I’ve got a one track
mind…with no strings attached. Eh?
Announcer: TIME!
John: MOM?!
Announcer: TIME!
Sandra: Hi, I’m Sandra, I want a white wedding, white dress, white flowers, white kids, white house, white
dog, white cat, and a white picket fence!
Announcer: TIME!
Yolanda: Hi, my name is Yolanda, and I want you to know, right from the start, I used to be a man.
Announcer: TIME!
John: (sighs, quits, dejected) Blegh! Fine, THAT’S IT! I quit! There’s nobody normal here! It’s like
they all escaped from an asylum or something!
Hi, I’m John…and I just don’t care anymore.
Sara: Hi, I’m Sara. And neither do I. This is like a convention for dateless rejects…
John: Oh, you’re telling me? Either they want your kids, or they want your pants, or they have something
IN their pants…so what do YOU want?
Sara: Well…right now I’d just settle for a cup of coffee…or maybe a bite to eat?
John: Oh…well…let’s go.
(on the phone, later) Hi Mom. Yeah, it was alright. I met some…interesting people. Well, they weren’t
ALL bad, there was this one…Hang on a second, Mom. I’ve got another call. –switch- Hello? Oh, hey
Sara! Yeah, just hang on a minute, I’ve got to get someone off the other line. –switch- Hey, Mom.
I’ve got to let you go…
END
```

---

## IC-0862: Exit Interview

- Title: Exit Interview
- Author (byline): Bridget Grace Sheaff
- Work: Exit Interview
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, BRANDON, NICOLE
- Teaser before the introduction: No
- Spoken words (computed): 1845
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
CHARACTERS:
NICOLE- Sharp, witty, very intelligent. Determined. Energetic. Very perceptive.
Compassionate.
BRANDON- Clever. Wants to be the nice guy. Terrified of the idea that people might not like
him. Hard-working. Would give you the shirt off his back.

(Note from the playwright: Both of these people are trying to make this an amicable parting. It’s early in the breakup and real feelings are on the line, but both Nicole and Brandon want to walk away with as much dignity as possible. The things that are funny in the beginning should be allowed to be funny. The last things this needs is an air of defeat and defensiveness. Positive stakes. They still want what is best for the other person as well.

(At rise, NICOLE, business attire, sits at a conference room table, binder and pen in hand. She reads over her documents, glancing up at the door and the clock every now and then. BRANDON enters, wearing a suit and carrying a box of desk contents. He sets it down on a chair and reaches to shake NICOLE’S hand.)

NICOLE (shaking his hand): Thank you for coming in today, Brandon. I know you are busy.

BRANDON: It’s no trouble at all.

NICOLE: I wanted to ask you a few questions today about your decision. I thought it was important that we take some time, learn the reasons for your departure. We are disappointed to be losing you.

BRANDON: Yes, it wasn’t an easy decision. But I think it's time I move on.

NICOLE: Sure. I hope you will be open and honest in this time, that you feel you can give complete answers.

BRANDON: Of course.

NICOLE: We’re really looking to use the criticism and feedback here to drive some organizational improvements. Make some changes for the future. This process could be a learning experience for both of us, don’t you think?

BRANDON: Agreed.

NICOLE: Well… Let’s dive right into it. So you’ve been here, what, nine months?

BRANDON: Almost ten.

NICOLE: Ah. I suppose that depends on when you start counting from.

BRANDON: Sure. NICOLE (taking notes): So. What caused you to start looking for something new at this time?

BRANDON: Like I said, I think I knew it was time to move on.

NICOLE: Of course…. do you care to expand on that?

BRANDON: Well, I think I looked at my life and my goals and I really asked myself where I wanted to be in five years, what kind of future I wanted, and it wasn’t… here, ya know? I valued this position and I feel I learned a lot. I will always look fondly on my time here. It’s time for, like you said, something new.

NICOLE: You want something different.

BRANDON: Exactly. (NICOLE begins to write something down) No, wait, no that’s not it. This, um, this isn’t a good fit anymore, ya know?

NICOLE: I see.

BRANDON: I don’t know if I’m saying the right thing.

NICOLE: All you have to do is be honest. That’s all.

BRANDON: Yes, of course.

NICOLE: That’s all I’ve ever wanted from you.

BRANDON: I know that.

NICOLE: (the facade cracking) Don’t just tell me what you think I want to hear. You can’t be the nice guy all the time. You aren’t the hero.

BRANDON: I wasn’t… yeah, sure. Okay. NICOLE (recovering cheerfully): So. What did you dislike about the company?

BRANDON: So, suddenly, I don’t like where this is going.

NICOLE: Honesty is important so we can improve our performance.

BRANDON: This doesn’t sound like honesty, this sounds like masochism.

NICOLE: (almost laughing) Will you answer the question?

BRANDON: Mostly, it was great.

NICOLE: Yes. You mentioned that. Right now I’m trying to mine a little deeper, find out where we could have done better by you. Maybe get a sense of what you want, what you are looking for.

BRANDON: Well… there were times I didn’t feel valued. Sometimes. I felt taken for granted.

NICOLE: (this is a surprise) Taken for granted?

BRANDON: You know, I felt like I sometimes wasn’t part of major decisions. And there were times when I felt… like, stupid.

NICOLE: Like when?

BRANDON: When I would get things wrong or disagree with you or try to make choices or jokes or even when I would try new things, shake things up a bit, ya know. Or sometimes-

NICOLE: That sounds like you felt stupid a lot.

BRANDON: Well.

NICOLE: Well, no one can MAKE you feel stupid.

BRANDON: See, right there. It was stuff like that. When the responsibility for my problems was solely on me. If I was the one having the problem, then I was being overly sensitive or not taking initiative and it was never anyone else’s fault. It made me feel… It was like my feelings and thoughts didn’t matter to you.

NICOLE: Wow.

BRANDON: You asked me to be honest.

NICOLE: Did you share your concerns with anyone prior to deciding to leave?

BRANDON: … No, I didn’t talk to you, but-

NICOLE: (calm yet sarcastic) Oh, interesting. I was about to say I don’t remember hearing about this before. But, now, you want to talk?

BRANDON: I always wanted to talk, that wasn’t-

NICOLE: If you didn’t bring these problems to our attention, how could you have expected us to fix them?

BRANDON: That’s what I’m saying. If I had talked to you about them, you wouldn’t have really acknowledged them. It would have ended up being my fault.

NICOLE: How do you know that for sure?

BRANDON: I guess I don’t.

NICOLE: And without being aware of it-

BRANDON: Look, I’m not saying I did the right thing by not talking to you about it. I’m saying that there was a reason and a logic to it at the time and when the reason no longer outweighed the problem, then I knew it was time to move on.

NICOLE: Did you share your concerns with anyone OUTSIDE the company prior to deciding to leave?

BRANDON: I don’t want to answer that.

NICOLE: So you did.

BRANDON: I really don’t-

NICOLE: Did you talk to Stacy?

BRANDON: I was looking for advice!

NICOLE: Who else? Charlie? Michael? Winston Churchill? Who knows all of this?

BRANDON: I didn’t-

NICOLE: How many people did you talk to about this without talking to me?

BRANDON: A few, okay, but it’s not the way you’re making it out.

NICOLE: And probably your mother, right?

BRANDON: Well...

NICOLE: (laughing sardonically) Of course.

BRANDON: What does that mean?

NICOLE: You know what it means.

BRANDON: Look, it wasn’t like I went around sharing private details about my time here. I wasn’t telling secrets. I needed… I was looking for help.

NICOLE: No, you were looking for confirmation that you were right. You were looking for people to be on your side.

BRANDON: Doesn’t everyone?

NICOLE: How could I have been on your side if you didn’t talk to me? BRANDON:... I don’t know.

(Pause.)

NICOLE: I think we have gotten slightly off track.

BRANDON: I agree.

NICOLE: What does your new company offer that encouraged you to leave this position?

BRANDON: New company?

NICOLE: I assume you already have a new position. How long have you known you were moving on? And what is the name of your new company?

BRANDON: There’s no new company.

NICOLE: Have you worked with them before? Am I familiar with them? And are they prettier than me?

BRANDON: There isn’t anyone else.

NICOLE: I have trouble believing that.

BRANDON: It’s not like that.

NICOLE: Then what is it like?

BRANDON: Nicole, I don’t know what this is helping.

NICOLE: Was there a single event responsible for your decision to leave?

BRANDON: I don’t think that’s relevant.

NICOLE: Based on that response, I think it might be.

BRANDON: No, it wasn’t one thing.

NICOLE: Are you sure?

BRANDON: Why would I lie about this?

NICOLE: There wasn’t one conflict? Or one task? One request that might have pushed you over the line? What happened? What went wrong? Is there a way to fix it?

BRANDON: This whole line of questioning is meaningless.

NICOLE: Why have you decided to leave the company?

BRANDON: I already answered this.

NICOLE: Why have you decided to leave?

BRANDON: I told you!

NICOLE: I don’t like that answer, try again.

BRANDON: Nicole, stop it.

NICOLE: Tell me WHY, Brandon.

BRANDON: I can’t.

NICOLE: Yes. It’s easy. Think words. Open mouth. Say them.

BRANDON: No… Not, “I can’t tell you.” I… I can’t anymore, okay?

(Pause.)

NICOLE: I have a few more questions.

BRANDON: So do I.

NICOLE: That’s not how this works.

BRANDON: Oh really? I think it’s my turn to ask the questions.

(BRANDON grabs the binder from NICOLE and starts reading the questions aloud.)

BRANDON: “Number 16: Do you feel you had the resources and support necessary to be successful? If not, what was missing?”

NICOLE: (reaching for the binder) Brandon, give it back.

BRANDON: (plowing through)“Number 17: Did you have clear goals and know what was expected of you in your position?”

NICOLE: (still fighting) Knock it off. This isn’t how this goes.

BRANDON: (speaking over her) “Number 22: What are the key qualities and skills we should seek in your replacement?!” Are you kidding me?!

NICOLE: I am the one asking the questions!

BRANDON: No, right now, it would appear I am the one asking the questions.

NICOLE: That’s not fair.

BRANDON: Why?

NICOLE: Because I’m not the one who wants to leave!

(Silence. BRANDON hands the binder back to her and sits again.)

NICOLE: If there had been opportunity for promotion or advancement, would you have stayed?

BRANDON: Nicole…

NICOLE: Answer the question.

BRANDON: That wasn’t how this was going to work. You never… it was clear from the beginning that I wasn’t going to move up here. It took me a while to see that and to accept it, and once I did I knew that it was time to move on.

NICOLE: So for nine months…

BRANDON: Ten. Ten months. Depending on where you start counting. And no. Of course not. Not the whole time.

NICOLE: So what you are saying is that if I… if we had changed our minds…

BRANDON: If, if, if. Who knows?

NICOLE: Right.

BRANDON: But you didn’t want that anyway.

NICOLE: You’re probably right.

(So much is unsaid in the silence that follows.)

NICOLE: What did you value about your time here?

BRANDON: Lots of things.

NICOLE: Be specific.

BRANDON: Um, I always felt like I was cared for.

NICOLE: I thought you felt stupid.

BRANDON: I did. Sometimes. But it wasn’t like it happened on purpose. And I still knew that you… I always liked when you would smile at me without saying anything and how you laughed at all my jokes, especially when they WERE stupid.

NICOLE: Hm.

BRANDON: I liked going on adventures. And learning new things. And being challenged. You were always challenging and exciting.

NICOLE: Yeah.

BRANDON: I valued your insight. Your passion. You were clever, charming. You stuck by your convictions.

NICOLE: A lot of past tense in that sentence.

BRANDON: You still are. And I still like it. I need to put it in past tense.

NICOLE: Yeah.

BRANDON: What did you value?

NICOLE: No.

BRANDON: Nicole… come on.

NICOLE: You... made me feel safe. And wanted. And smart. Not smarter than you or anything. I felt listened to. I liked that you listened to me.

BRANDON: Me too.

NICOLE: What would make you consider working for us again in the future?

(Silence.)

NICOLE: You know what, forget I asked.

BRANDON: Yeah.

NICOLE: Would you… recommend this to another person?

BRANDON: In a heartbeat.

NICOLE: Alright. I think that’s all my questions.

BRANDON: No, it’s not.

(Silence.)

BRANDON: I saw the list, Nicole. Go ahead. Ask.

NICOLE: I’m afraid of the answer.

BRANDON: I know.

NICOLE: If you already know, can’t you tell me?

BRANDON: I think the answer might be less important than the question.

NICOLE: I haven’t gotten any real answers this whole time.

BRANDON: Because you haven’t been asking what you want to know. I can only answer what you ask me.

(Pause.)

BRANDON: Please ask.

NICOLE: Was it ever real?

BRANDON: Try again.

NICOLE: (summoning strength) Did you ever really love me?

BRANDON: Of course I did. Do. That’s not what this is about.

NICOLE: How is it not about that?

BRANDON: Because I’m not the hero, Nicole. I can’t just be the nice guy.

NICOLE: Right. Sure.

BRANDON: So. It’s over.

NICOLE: (a moment of pure desperation) Help me understand why.

BRANDON: It’s what needs to happen.

NICOLE: I don’t get it.

BRANDON: Me neither. But these questions aren’t going to make it any less hard.

NICOLE: I know.

BRANDON: You will be fine without me.

NICOLE: That is 100% not the point.

BRANDON: Yeah.

(BRANDON stands to leave, sliding the box towards NICOLE.)

BRANDON: I think it’s all in there.

NICOLE: Thanks.

(BRANDON looks at NICOLE intensely for one moment. She doesn’t look at him. He leans over to kiss her on the forehead and she pulls away. BRANDON retreats and exits. NICOLE sits, ruined but determined.)

END SCENE
```

---

## IC-0863: Face-Baggage a play by Nick Monroy Copyright 2009 by Nick Monroy

- Title: Face-Baggage a play by Nick Monroy Copyright 2009 by Nick Monroy
- Author (byline): Not specified
- Work: Face-Baggage a play by Nick Monroy Copyright 2009 by Nick Monroy
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1764
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
(Play opens in a Facebook office. Nikki is sitting at her desk. Danny walks in.)

Nikki Hi welcome to Facebook. I’m Nikki. Please have a seat.

Danny (A little timid) Hi. I’ve never actually been here before.

Nikki That’s ok. Have a seat. So what can I do for you today?

Danny I would like to sign up for Facebook

Nikki Ok, great. We can do that for you.

Danny Yeah, I’ve been trying to avoid it this whole time. I think people tend to get a little too obsessed with it and it almost takes over their lives.

Nikki Yeah, that’s been known to happen.

Danny

Yeah, well I would really just like something basic. I’m more interested in keeping touch with friends and family. I have a sister who lives across the country so I’d really like to stay in touch with her. Maybe even meet knew people, you know, nothing too crazy.

Nikki That’s fine. Ok, then let me just activate an account for you. Name please?

Danny Danny Costa. Do you need to see my ID?

Nikki No, we’ll just take your word for it.

Danny So I can just make up a name and a fake account to go along with it?

Nikki You could if you want to. But you said you just “wanted something basic”. So let’s get started on your profile. We’ll start off with Basic Information. Ok. Are you single, in a relationship, married?

Danny Single.

Nikki Ok. Really? A good looking guy like you...

Danny Yeah....well...I don’t know....it’s complicated.

Nikki OH!?!?!

Danny What?

Nikki Would you like me to put its complicated?

Danny I thought it was just being single or being in a relationship

Nikki Well yes, but you can also put down "it’s complicated"

Danny What’s complicated?

Nikki It.

Danny What's it?

Nikki Let’s just skip it for now. Political Views?

Danny Wow, really? Uh, I’m pretty moderate I guess.

Nikki Ok. Religious Views?

Danny Uh. I don't know. I guess I believe in God

Nikki Ok. That's fine. Which God?

Danny The one from the Bible I guess

Nikki OK, good. So I’ll put down Christian

Danny Well, no. I mean I don't go to church or anything

Nikki So. Catholic?

Danny Yeah I guess. Or No, I wouldn't per say call myself....Let’s just put other.

Nikki
Sure. Ok. Now lets move on to Personal Information
Danny
That wasn't personal enough?

Nikki Haha. No sir. We still need to cover your activities, interests, favorite music, movies, books, and quotes.

Danny Well wouldn't my favorite music, movies and books just go under interests?

Nikki I don’t make up the rules sir. I just work here.

Danny

Fine. I guess for activities you can put hanging out with friends. Interests you can put sports and partying. Music you can put rock and hip hop. Movies...I guess...godfather and scarface. And I don’t really have any favorite books or quotes.

Nikki Ok....

Danny Is something wrong?

Nikki

No, no. That's fine. This is all fine...I just...wonder why you're interested in joining facebook when you obviously already lead such an exciting life.

Danny I'm sorry what?

Nikki Nothing. Enough with all the information. Moving on. How do you feel?

Danny What?

Nikki How do you feel? Right now?

Danny Right now....I don’t know. I guess...slightly confused by all of this.

Nikki Aright. Danny….is...slightly...confused...by...all...of...this

Danny What did you just do?

Nikki Oh, I just updated your status

Danny Ok what's that for?

Nikki Now all your friends know that you're feeling slightly confused by all of this

Danny Why? I don’t think they would really care

Nikki

It doesn’t matter if they care. I'll let you in on a little secret. Most people actually don’t care how you feel. They may be bored at work and looking through their friends statuses but they really don’t care how how happy you are that you're engaged or how sad you are that someone you know is dead.

Danny So then what's the point of updating your status?

Nikki Let’s move on to the final piece. Your profile picture. Did you bring a photo to use as your main profile pic?

Danny Yes I did. (Hands her a photo)

Nikki (Sarcastic) Oh...you squatting down next to your car. That’s great.

Danny Is it?

Nikki Yeah, sure. I bet nobody has a picture like this.

Danny

I was thinking of maybe using a picture of my new tattoos, but you can’t really see my face in them.

Nikki Oh. Wonderful. This will do for now.

Danny So can I find my friends and family now?

Nikki Well since we started you've already had 5 friend requests.

Danny

Oh, nice. Is my sister one of them? (Looks at the requests) Oh my god. These are all people I went to high school with. I wasn’t even in the same grade at this guy.

Nikki What about this other guy? It says you two are related.

Danny

Uh…if you count step-father’s cousin as “family”. Yeah, I’d like to ignore these to be honest. You said there were
5 friend requests. Who’s the fifth?
(Nikki smiles. Points to herself)
Oh.....ok. Yeah sure ill accept you.

Nikki
Cool beans
Danny
So now how would I find my current friends?
(Looks at him)
What...what?

Nikki Come here

Danny What is it?

Nikki Come closer. (Pokes him in the nose)

Danny Um. Ok.

Nikki I just poked you, silly

Danny Yeah I noticed. (Beat) So how would I go about finding my friends? (Silence)

Nikki
Are you gonna poke me back? (Confusion) Come on you can’t just leave me hanging.
(Awkwardly pokes her in the arm. A is happy)
So, you would like to find your current friends.

Danny Yes please. That’s really all I wanted to do.

Nikki

Ok. Well there are several ways we can do this. We can check "people you may know" or we can.....oh no. Oh no no no.

Danny What...

Nikki Oh man I'm sorry. Your vampire was just attacked.

Danny What

Nikki Listen to me. Someone just attacked your zombie; if you don’t retaliate now then you’ll be stuck as an ensign zombie forever.

Danny What do I do?

Nikki Click here. Click here!!!. Ok now click here. Now click attack. There. You did it.

Danny That’s it?

Nikki How did that feel?

Danny I guess it felt pretty ok

Nikki Good, cause you're gonna have to do it again, a vampire just bit you.

Danny What do I do?

Nikki Bite back bite back bit back

Danny Ok ok. Jeez. Is that it? Can I find my sister now?

Nikki You can. But first, I strongly suggest you join this cause.

Danny What cause?

Nikki Save Darfur.

Danny What?

Nikki You need to join the cause to save Darfur.

Danny I don’t even know who Darfur is.

Nikki

Listen…if you don’t join the cause to save Darfur then they’re all going to die. Do you want innocent people to die?

Danny No. All I really want is to just stay in touch with my sister…

Nikki So you want the people of Darfur to die. That’s fine, that’s fine.

Danny All right! I’ll join your cause. But then I’m just gonna give my sister a call.

Nikki NO!!! I mean, why would you want to call her?

Danny Because. She just had a baby last week and I want to see how she’s doing.

Nikki Oh! I see now. Well then, we can keep you in contact with your sister.

Danny Thank you.

Nikki In fact, you can also see photos and videos of her new baby when she posts them to her account.

Danny That would be great.

Nikki And you can also send her bumper stickers.

Danny What’s that?

Nikki

Just look. I already sent you a bumper sticker. Accept it. See, it’s a picture of a puppy and a kitty cuddling and it says “BFF”. Isn’t that great?

Danny No, not really. Listen, my sister’s name is (name). If you can just do a quick search for her.

Nikki (Slightly offended) Ok. All right, there, I found her.

Danny Thank you. Can you add her for me please?

Nikki I can. But wouldn’t you rather vote for which one of us is hotter?

Danny What? No! That’s gross.

Nikki So vote that I’m hotter than your sister.

Danny No, I won’t. Listen, my sister just had a baby. This is a very important event in our lives.

Nikki

Important event? I’ll tell you about “important events”! My friend is looking to sublet an apartment in Park Slope this summer. Only 800 dollars a month before utilities.

Danny For Christ’s sake. (Gets up and pulls out his cell phone) That’s it I’m just gonna phone my sister myself.

Nikki I wouldn’t do that if I were you.

Danny You’re gonna try and stop me from calling my own sister?

Nikki Not me. But the Mafia will.

Danny What mafia?

Nikki MY Mafia. Don’t make me start a war with you.

Danny This is getting out of control. I thought facebook was just about networking with people.

Nikki It is. It always has been. (Starts to hit on him) So much so that you don’t even need that precious little phone anymore.

Danny Excuse me?

Nikki

Why would you want to have a long boring conversation with someone on the phone, when you can just as easily show someone how much you appreciate them by sending them a martini on facebook?

Danny Because that doesn’t…

Nikki Don’t you want to have a martini with me?

Danny I…

Nikki

Yeah. Why don’t you just give me your phone maybe we can…super poke. (They’re about to kiss, until he stops)

Danny

No. I can’t do this. Look, I’m sure all these things you can do on facebook are fun, but I still think that the best way to stay in touch with my family is to just call.

Nikki (Starts to lose it) Don’t you ever use the C-word around me again!

Danny Call?

Nikki Ahhh!

Danny Ok, this is crazy, you’re crazy, and now I think facebook is crazy. I would appreciate it if you just delete my account.

Nikki Ha! Oh, we can “deactivate” your account if you want. But nothing ever gets deleted. It’s online forever!

Danny Um, ok. I guess I just won’t log on then.

Nikki (Foiled) Fine! You know what? Facebook doesn’t need you! I don’t need you. You think you’re my only appointment today? There are thousands of people signing up for facebook each and every day. Normal people, famous people, politicians, corporations. You can’t stop us! No one can stop us!

Danny I’m not actually trying to stop you. I just got a text from my sister. It’s a picture of my nephew. Wanna see?

Nikki Get out!!!! (B awkardly leaves. She goes back to her desk and pages secretary) You can send in Barack Obama now.

End
```

---

## IC-0864: THE GR8 TXT MSG WAR

- Title: THE GR8 TXT MSG WAR
- Author (byline): Hank Frederick
- Work: THE GR8 TXT MSG WAR
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GIRL, GUY
- Teaser before the introduction: No
- Spoken words (computed): 558
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
THE GR8 TXT MSG WAR A weeknight conversation between two high schoolers (Girl & Guy), conducted completely over text message. In some cases, the text message has been written out the way someone might describe seeing it; in other cases, the original text formatting and grammar has been left for interpretation. It is the author’s intent that the performers liberally adapt the script in order to both accurately and humorously communicate the text exchange to the audience, in the context of their particular talents and the performance venue. THE BASIC PLOT, for those who have trouble speaking textese: The conversation takes place after school. Girl has a surprise for boy. Surprise is she is allowed to go to the prom. Boy not as excited as he should be. Girl says he should ask her. Boy says maybe. She threatens him. She declares her love, such as it is. Boy agrees. Girl is happy. Talks boy into taking her shopping as well. Boy says he secretly loves shopping. They pick a time and then say goodnight.

GIRL: I’ve got a surprise, number four, letter “U”.

GUY: Number four, me?

GIRL: R U going to ask me what it is?

GUY: Yeah probably, semicolon dash closed-parentheses.

GIRL: How bout doin it now, colon dash upper-case D.

GUY: I kno wut ur gonna say.

GIRL: Oh yah?

GUY: That Im handsome and smrt.

GIRL: So smrt.

GUY: ROFL.

GIRL: Guess again.

GUY: They told u that ur an alien.

GIRL: Haha

GUY: Cuz of ur big feet.

GIRL: ANGRY FACE. (or, “>-o”)

GUY: JK

GIRL: Letter N, Letter E, way, the real surprise is dot dot dot they say its OK 4 me 2 go 2 prom!!

GUY: omgggggggggggggg

GIRL: So, got Letter N, Letter E thing to ask me?

GUY: dunno like wut?

GIRL: lik maybe about who Im goin to prom with?

GUY: OIC

GIRL: Colon dash close-parentheses.

GUY: So who u goin wit?

GIRL: O. Thought u might no already.

GUY: Nah no clue.

GIRL: Colon dash forward slash.

GUY: Colon dash asterisk.

GIRL: Colon dash open-parentheses.

GUY: Question Mark?

GIRL: Forget it.

GUY: Dot. Dot. Dot.

GIRL: Dot. Dot. Dot.

GUY: OK.

GIRL: So I wuz talking 2 Jeff about prom.

GUY: O RLY!

GIRL: He hasnt asked any1 yet.

GUY: Thx for letting me kno.

GIRL: NP.

GUY: Jeff told me he wants to take Leann because she puts out (No response)

GUY: LOL?

GIRL: K WTF?

GUY: No swearing. Stern face.

GIRL: WTH?

GUY: That H better be a “heck” LOL.

GIRL: Use ur imagination.

GUY: Okkkkkk

GIRL: Maybe Jeff should ask me.

GUY: y?

GIRL: cuz id put out.

GUY: sexy

GIRL: maybe id do it if you asked me to prom

GUY: thats not a bad motivation

GIRL: u should go cuz I luv u

GUY: Ok will you grow swans with me?

GIRL: WUT

GUY: Darn I scream still at old lady prawns

GIRL: Are u making fun of me

GUY: Stupid autoelect is dressing with my eggs

GIRL: ?

GUY: Autocorrect. Is messing with my sex.

GIRL: ??

GUY: Texts.

GIRL: Whatevs.

GUY: Will u go to pong with me? (No response)

GUY: PROM.

GIRL: With u?

GUY: Prom. y/n?

GIRL: dot dot dot y!!!

GUY: hooray lol

GIRL: Only if you go 2 the mall with me?

GUY: Old Navy?

GIRL: No, Lidz. I need a new Raiders hat!

GUY: Dats y I luv u... but can we still go to Old Navy?

GIRL: Haha sure.

GUY: Need nicer boxers 4 prom :-).

GIRL: Ur ridiculous. Luv u.

GUY: Yah?

GIRL: Yah.

GUY: Same 2 u.

GIRL: >-o

GUY: I luv u 2!

GIRL: Yayyyyy I gotta do chem hw

GUY: me 2. lidz 2morrow?

GIRL: after we buy prom tickets.

GUY: Nite babe.

GIRL: XOXOXOXOXOXOXOXOXOXOXOXO.

GUY: Ur a sweetie.

GIRL: Letter C, Letter U, Number 2, morrow.

GUY: Not if I, Letter C, Letter U, first.
```

---

## IC-0865: Minnesota

- Title: Minnesota
- Author (byline): Spill Major
- Work: Minnesota
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1070
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
(Open to a row of airline seats. Two passengers getting settled: a young woman and a larger, older
man.)
Girl: You’re on my seatbelt.
Guy: I’m President Grover Cleveland.
Girl: President Grover Cleveland, you’re on my seatbelt. (He leans up so she can get it.)
Guy: I wonder if they’ll give me two bags of peanuts.
Girl: You are a President.
Guy: It doesn’t go very far, anymore.
Girl: Oh. President Grover Cleveland?
Guy: Please, Call me Steve.
Girl: President Steve, why are you flying to Minneapolis?
Guy: I’ve never been there.
Girl: Were they a state then?
Guy: Huh?
Girl: When you were President.
Guy: How old do you think I am?
Girl: Oh.
Guy: Although I miss the days when locomotives were preferred to these crazy flying stage coaches.

(an awkward silence) Girl: (suddenly) President Steve - aren’t you dead? Guy: (looking at her for the first time) I thought so too. (He wants to say more, but can think of nothing. After a long pause, he speaks again.) So, why are you hurtling towards Minneapolis in the belly of this winged metal beast? Girl: I go to law school at the University of Minnesota. Guy: Yes I’ve heard they let women into the Bar these days. Tell me something, Girl: Yes? Guy: Are you all hardcore lesbians, or are some of you just trying it out? Girl: I was thinking of giving you my peanuts before, but now my lesbo ass is keeping those nuts. Guy: I wouldn’t think you’d be interested in my nuts. Girl: What? Guy: I was married to a woman younger than you. Girl: And what happened to her? Guy: You know women. They sort of… get old. Then you lose track of them. Like loose change. Girl: That’s awful. Guy: Speaking of loose change… (he digs around in his pockets) who is this bastard on the dime? Looks like a real dweeb. Hey, can I give you ten cents for your peanuts? Girl: (She snaps.) Ten cents! Ten cents will buy you one peanut, maybe an almond. They don’t even give you meals on these things anymore – the nuts are all you get. I’m a college student, Mr. President – why do I keep calling you that – I’m a poor college student, those peanuts are the only thing I’m eating all day until I get back to my tub of ramen. But sure, even though you’re probably some prick named Steve, I’ll give you my peanuts. And since you seem pretty determined to suck me dry, is there anything else I can get you, Mr. President? Guy: Pickled herrings. Girl: What? Guy: I perused a book entitled, “America’s Great Leaders.” It contained only one quote from me, in regards to cheese and pickled herrings. I could go for some right now. Apparently they’re the legacy I worked so hard for. Girl: Too bad you didn’t work a little harder. They might have given you some extra peanuts. Guy: The federal government should not interfere in the economy. And young ladies should not be rude to former Presidents. Girl: I don’t have to do anything but sit next to you. I don’t care if you’re Millard Effing Fillmore. Guy: I told you it doesn’t go far anymore.

Girl: Stop it. Stop. And to think, when we were boarding, I wanted to compliment you on your great
hair weave.
Guy: It’s not a weave. It’s a hair system.
Girl: What’s the difference… an expensive wig is still a wig.
Guy: I would ask you to be respectful.
Girl: What?
Guy: Those words you use to describe my hair system were inappropriate.
Girl: Are you serious?
Guy: That word – the “w” word. That’s hate speech. To someone who suffers like me. Baldness is a
disease. It should be legally protected, I think.
Girl: You know what I think? That I’m going to stop talking to you, and then never make the mistake of
doing so again in my life.
Guy: (staring at her) Fascinating.
Girl: What?
Guy: You're sure you're not a lesbian?
Girl: So what if I was.
Guy: I.. never thought of an answer to that.
Girl: Are you playing a prank on me? Is this on Candid Camera. I swear, Justin Bieber pops out from
the bathroom, I will take this plane down.
Guy: Justin Bieber? Who is that?
Girl: Someone who is already more famous than you ever were.
Guy: I was President!
Girl: When the population was about 70 million. Now we have over 300. Justin Bieber probably has 70
million followers on Twitter.
Guy: I don't know what any of those words mean and I would prefer not to.
Girl: Look, I don't need this. I have enough on my mind.

Guy: Why are you going to Minnesota?
Girl: (she looks at him, then realizes it's hopeless to not say anything.) My cats died.
Guy: A great loss. Our nation mourns with you.
Girl: Do not make fun of me right now. Do not. I loved those cats. Both of them got hit by ice cream
trucks in the same week.
Guy: I am not sure why someone would put ice cream in a truck, but that still sounds like a particularly
cruel coincidence.
Girl: The first one, I cried. The second one, I laughed. I was beyond sad. I was away at law school, and
now I feel like I need to see my parents because...
Guy: Because you need to face the cruelties of fate with the people you love.
Girl: I don't know why. No, not that. I just want to be home.
Guy: That's why I'm hoping my trip is short. I'd like to get back to my home. (Girl says nothing, even
though Guy expects it.) You know, the White House.
Girl: Oh give it up already.
Guy: Last night I was in the Oval Office until 2 in the morning, vetoing bills on war pensions… or was
that last night? What have I done these past few days? (He looks to her.) Remember, I just gave that
speech on tariffs… (He realizes that he looks foolish.) No, maybe that hasn’t made it to the papers yet.
Maybe not. Is this my first term or second?
Girl: The years in-between.
Guy: You did recognize me!
Girl: I’ve heard of more than pickled herrings. (pause) President Cleveland, are you sure you’re not
some guy named Steve?
Guy: I am not. Steve lives in Minneapolis. President Cleveland, I mean, I have never been there.
Girl: Why change your name, then?
Guy: I was starting to think that people didn’t like me anymore.
Girl: Maybe you should pretend to be Steve for the rest of the flight.
Guy: Why?
Girl: So you feel like you’re going home. (Silence, for a bit.)

Guy: I’d still like a second bag of peanuts.
Girl: When they come, you can have mine.
Guy: And you will have many thanks of a grateful nation.
Girl: I’ll settle for the thanks of a grateful Steve. (Lights down)
```

---

## IC-0866: Not For Sale

- Title: Not For Sale
- Author (byline): Blair Waite
- Work: Not For Sale
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1732
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
Woman sitting alone in park on a bench.
Man walks in carrying a bucket of roses… sees woman and smiles. He watches her for a few
seconds without her noticing, then Man approaches woman with the roses.
Man: Beautiful rose for a beautiful lady?
Woman: No thank you.
Man: No, really, have a rose.
Hands her a rose, she does not take it.
Woman: No, thank you.
Man: Here is a rose.
Hands her a rose, she does not take it.
Woman: I don’t want to buy one.
Man: They are not for sale.
Woman: How is that? You have a bucket of them. There are easily over 100 roses in there. It
sure looks like you are trying to sell them.
Man: Well I am not.
Woman: But it LOOKS like you are.
Man: I just want to give you a rose, they are not for sale, all right. It’s a gift.
Woman: That’s awfully nice of you, but I still don’t want a rose.
Man: You really should take one. A beautiful rose for a beautiful lady.
Woman: Do you get your jollies from wandering around the park handing out roses or
something? Take a hint.
Man: Just take a rose.
Woman: What am I supposed to do with it?

Man: Smell it, love its beauty.
Woman: I’m just waiting on someone, I don’t have anywhere to put it. It would just be wasted
on me.
Man: It would not be wasted on such a beauty.
Woman: Thank you, but still no.
Man: Who are you waiting for?
Woman: A man.
Man: Well, (looks around for a moments) looks like he is not here.
Woman: Obviously. (Looks at watch) He was supposed to be here 5 minutes ago.
Man: Looks like he might not show up. Why don’t you take a rose to cheer you up?
Woman: I still don’t want a rose.
Man starts to walk away but turns back
Man: Do you know this person?
Woman: We’ve only talked online and on the phone, this is our first meeting. I may be getting
stood up.
Man: Uh oh. Who would stand up such a beautiful lady?
Man takes a seat next to the woman.
Woman: His name is Chris. I don’t even know what he looks like, but we’ve been talking for
months now. I feel like I know him, may even be falling in love with him. I don’t know why I
am telling you this, you are a stranger who is selling roses in the park.
Man: They are not for sale.
Woman: Doesn’t matter. You are a stranger.
Man: I may be a stranger, but I’m willing to listen. I have all day. (pauses then says jokingly)
Sales are slow.
Woman: See, I was right, you ARE selling them!
Man: It sounds like you really like this Chris guy. What is it about him?

Woman: We talk on the phone and online for hours at a time. I tell him my deepest secrets and I think he tells me his. He’s becoming my best friend. He just has a way of putting me to ease and making my day brighter by just talking to me. I can tell him the mundane details of my life and he seems to think it is the most interesting thing in the world. He is the best part of my day, the first person I want to talk to when anything happens. I talk to him first thing when I wake up and always right before going to bed. We met on a dating site, I almost blew him off because he didn’t have a profile picture. He said the reason he didn’t was he believes that the beauty inside a person is what is important and having a picture does not allow a person to get to know someone on a deeper level. Man: I get that. If you get to know someone for who they are instead of what they look like it really is better. Like they say, looks fade. Woman: The fact that he has not shown up is starting to make me wonder if he is even real. Man: Why wouldn’t he be real? Woman: Well, he’s not here. Maybe it was just some elaborate hoax to get some lonely girl to look like a fool. Man: That’s not very nice. I also don’t think that is the case. Maybe something held him up? Woman: I keep trying to tell myself that, which is why I am still sitting here waiting. Man: I’m sure that is the it. Maybe he was nervous and needed a few minutes before he could see you in person. Or maybe he saw you and was so stunned by your beauty he couldn’t approach you. Woman: That’s just silly, but I guess he could be a little nervous. He has always seemed so confident in the past though when we have talked. I was sure he would show up and he sounded so sincere in wanting to meet me. Man: There must be some reason you have not met up in person yet though, right? Woman: I’ve never thought about that… Man: Just something maybe you should have thought about. Woman: What? Are you saying he is some three-legged freak or a serial killer or something? Man: (laughs) No, just that maybe he is not perfect and afraid to show himself to you for fear that that would reject him. Men have fragile egos sometimes. Woman: Oh my, what if he is a serial killer? What if he shows up and then takes me into the woods and murders me? What if he locks me in his basement? What if he thinks this is just some sick game to mess with my head? Lure me in and then treat me cruelly? What if he makes me put lotion on my skin like in that movie! I’ve heard that serial killers are really charming.

He’s really charming. He’s also very smart, serial killers are supposed to be really smart too. He’s sweet and funny and he will probably murder me! Man: Whoa whoa whoa, calm down. I think you are getting too worked up right now. Why don’t you have a rose. It will help you calm down. Hands her a rose which she pushes away Woman: I don’t want a rose. Not from you anyway. Man: Why wouldn’t you want a rose from me? I can be sweet and charming! I promise I’m not a serial killer. Woman: Stop it. You are fine, I just don’t want a rose. You know what I meant. I want a rose from HIM, not you. Man: Have you ever seen a picture of this Chris guy? Do you even know who you are waiting for? Woman: (Defensive) No. Man: You mean to tell me you are waiting around for a person, but you don’t know who to look for? He could be anyone. What about that guy over there walking his dog? Or that jogger over there? Or the guy feeding the ducks? What about that older man sitting on the bench by the lake? It could be any of them if you didn’t see a picture. Woman: He’s told me what he looks like. He’s medium height, brown eyes, brown hair

(describe whoever the rose man is)
Man: Sounds like a lot of people, nothing really all that descriptive.
Woman: Thanks for pointing that out, I didn’t already know that.
Man: I didn’t mean anything by that. Have a rose.
Woman: Not now, no roses. I’m too upset.
Man: Roses have a way of cheering people up.
Woman: I don’t think anything can cheer me up right now except Chris… and maybe he doesn’t
even exist. Maybe he’s really a woman! I’ve heard of stories like that.
Man: A woman? (laughs) You said you’ve talked to him on the phone, right?
Woman: Yes.
Man: Wouldn’t you have been able to tell? Wouldn’t he have a higher voice or something?

Woman: I suppose you are right on that one. So… Chris is not a woman… but he could still be a serial killer. Man: I think that is highly unlikely as well. I’m sure he just got caught up with something and will be here soon. Would you like me to wait with you? You can have a rose while we wait and if Chris shows up and you don’t want it anymore, just give it back. Woman: I don’t want Chris to see me sitting with another guy and then get the wrong idea. Man: How ‘bout I just stand over here? Still close enough that we can talk, but not too close… He will probably just think I’m selling roses like you do and not think anything of it. Woman: I suppose that would be okay. It is nice to have a little company while I wait, but don’t be too close. Man: Ok. A few seconds of awkward silence. Man: Hey, do you think that is him walking towards us? Perks up, then let down, it’s not him. Woman: No, he’s got a little kid with him. Man: Chris could have a kid? Woman: He told me he doesn’t have any children, but he wants them someday. He’s told me all about what he wants in life. Man: Oh? Woman: Yeah, he wants a big family, 5 kids, ha! He wants to travel and see the world before having them, but he’s always wanted a big family. I come from a small family, so it would be nice to have lots of people around. Chris says he comes from a big family and loves the sound of laughter filling a house. I can just imagine it. He wants to move his way up in his job to sales manager and buy a house in the suburbs. He wants to be a real family man, build a tree house for the kids, things like that. This house he wants would have a white picket fence and a rose garden! The perfect life! Man: A rose garden you say? Woman: He says he really loves roses… Man: (pause) Why don’t you have a rose, Rachel? Woman: (distracted, dreaming of the future with Chris) I told you, I don’t want a rose right now. Wait. How do you? What?

Man: Hi, I’m Chris.
Woman: What?! I’m… what?
Man: I thought I would surprise you with 150 red roses, one for each day I have known… and
loved you.
They embrace.
```

---

## IC-0867: Playdate

- Title: Playdate
- Author (byline): Scott Haan
- Work: Playdate
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BENJAMIN, CASSIE
- Teaser before the introduction: No
- Spoken words (computed): 2133
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
CAST OF CHARACTERS 2 (1M, 1F)

CASSIE (F) A 4-year-old girl, played by someone older than that BENJAMIN (M) A 4-year-old boy, played by someone older than that

CHARACTERS

These characters can be played by actors of nearly any age (ranging from middle school to adult), but they are actually 4-year-old children playing grown-ups… at least at first. When the dialog indicates CASSIE (ADULT) and BENJAMIN (ADULT), the actors are portraying a child’s skewed image of how an adult behaves. When the dialog simply indicates CASSIE and BENJAMIN, the actors portray 4-year-olds talking to each other as children (during which the actors try to encapsulate the innocence and arrogance of the very young).

DIALOG

Many words throughout the script are intentionally misspelled in an attempt to capture how young children often (and adorably) mispronounce words. “Spaghetti” becomes “pa-sketti,” “hospital” becomes “hop-spital,” and so on. Some dialog is also written to make it sound as if they have slight speech impediments, as children learning to speak often do (“play” becomes “pway,” “think” becomes “fink” or “sink,” and so on), but this is less pronounced when they are pretending to be adults. You can also play with cadence; children often take breaths or pauses in unusual places, especially during long sentences.

SETTING

The living room of Cassie’s home, although it could be a blank stage. Two chairs – possibly comically oversized chairs to make the actors look small – are optional. A table between the chairs, for the actors to share while coloring, is also optional.

PROPERTIES

• 2 coloring books (pre-set)
• Crayons (pre-set)
• A blanket, or long-sleeved sweater or jacket, for Benjamin (pre-set)
• A blanket, or long-sleeved sweater or jacket, for Cassie (pre-set)
• A briefcase (carried on by BENJAMIN)
• A comic book starring a female super-hero, such as Wonder Woman (carried on by CASSIE)

PREMIERE PRODUCTIONS

Playdate was first presented on June 9-11, 2017 as part of the 10-Minute Play Festival at Civic Theatre of Greater Lafayette in Lafayette, IN. Director: Lyle Janney. Producer: Steven Koehler. Cast: Abby McClure (“Cassie”) and Chris Fulk (“Benjamin”).

Playdate was next presented on October 12-15, 2017 as part of “Tall Guy, Short Stories: 10-Minute Plays by Scott Haan” at Clinton County Civic Theatre in Frankfort, IN. Director: Jean Warren. Assistant Director: Scott Haan. Cast: Kelsey Lukasik (“Cassie”) and Griffin Hundley (“Benjamin”).

PLAYDATE

(A family living room. At lights up, CASSIE is sitting or standing onstage, reading a comic book. After a pause, BENJAMIN enters SR with a briefcase.)

BENJAMIN (ADULT): Hey! I’m home from work. (A beat as he drops his briefcase.) Get me food.

CASSIE (ADULT): Did you just say “Get me food”? You can’t order me around!

BENJAMIN (ADULT): (Completely serious, baffled by her response.) Yes, I can, because I’m the man, so you have to do what I say.

CASSIE (ADULT): (Shocked.) WHAT?!? Who told you THAT?

BENJAMIN (ADULT): (Proudly.) My daddy. He used to say that all the time when he still lived with us, before mommy kicked him out.

CASSIE (ADULT): (Fascinated by this.) Whoa. (Kicking.) Did she really kick him, like with her foot?

BENJAMIN (ADULT): Yep. And then mommy said, “Don’t let the door hit you on the way out,” but then she TRIED to hit him with the door anyway. That was confusing.

CASSIE (ADULT): Well, MY daddy says that men and women are the same.

BENJAMIN (ADULT): No they aren’t… I saw a pitcher (mispronouncing “picture”) once, and they have diff-int parts.

CASSIE (ADULT): I don’t mean that. I mean daddy says men and women are EQUAL, and I’m not pa-spost (mispronouncing “supposed”) to settle for someone who won’t treat me right.

BENJAMIN (ADULT): I don’t know about all that, but I know I’m still hungry, and you still didn’t get me food yet.

CASSIE (ADULT): Ugh, for reals?

BENJAMIN (ADULT): Yeah! I mean, I’m not picky. Just some pa-sketti-oh’s would be fine.

CASSIE (ADULT): You can go get your OWN food. Your legs aren’t broken… not yet, anyway.

BENJAMIN (ADULT): But I don’t even know where the kitchen is.

CASSIE (ADULT): (Pointing off SL.) It’s that way.

BENJAMIN (ADULT): (Doesn’t move.) Oh. Okay. (Pause.) You’re SURE you don’t want to get it for me?

CASSIE (ADULT): Very sure. I had a long day of working too, you know. I’m a aster-naut, and a vet-in-in-arian. What’s your job?

BENJAMIN (ADULT): (Matter-of-fact.) I’m Batman.

CASSIE (ADULT): You can’t be Batman. That’s not a job.

BENJAMIN (ADULT): Okay, then I’m a Ninja Turtle. (Launches into a karate move.)

CASSIE (ADULT): That’s not a job either. You’re not playing this right.

(After a beat, a grumpy BENJAMIN sits down, either on the floor or on one of the chairs, and crosses his arms in defiance. He is now a 4-year-old boy. As kids, the characters can either sit or lie down on the ground, or if that makes them too low for the audience to see, they can sit in the chairs instead.)

BENJAMIN: (Pouty.) I don’t fink I wanna play growed-up wif you any more.

(BENJAMIN grabs a coloring book and a crayon, and begins to color. After a few moments, CASSIE sits as well, now a 4-year-old girl. She puts down the comic book and picks up a coloring book instead. During the following dialog, they both color on and off.)

CASSIE: What’s your name again?

BENJAMIN: Benjamin. What’s your name?

CASSIE: Cassie. How old are you?

BENJAMIN: (Holding up four fingers, making sure the audience can see them.) This many. How old are you?

CASSIE: I’m four. I’ll be five in Jan-uh-wary. I already told my daddy I want a puppy. A wittle baby puppy.

BENJAMIN: (Proudly.) I know where babies come from.

CASSIE: So do I.

BENJAMIN: I mean people babies, not puppy babies.

CASSIE: So do I.

BENJAMIN: Babies get brung by the spork.

CASSIE: What’s a spork?

BENJAMIN: It’s the bird that makes babies. You call the spork to come to your house, and you catch it, and then you kill it and eat it!

CASSIE: Eww, you eat it?

BENJAMIN: Yeah! And when you eat a whole spork, your tummy gets really big and fat, and it makes you hafta throw up, and when you do, a baby comes out of your mouth.

CASSIE: That’s not what happens.

BENJAMIN: Yeah-huh!

CASSIE: No, it’s not.

BENJAMIN: Is so! And only mommies can eat sporks, because if a daddy eats one, it’s uh-legal and they hafs to go to jail.

CASSIE: No, babies come from a hops— a hop-spital. I saw it on da tee-bee. A mommy and a daddy go to there, and they have a whole big room full of babies, and you pick the one you want, and you buy it and take it home.

BENJAMIN: (Skeptical.) Really?

CASSIE: Yeah… And you gotta get there early a-fore the cute ones are gone. You don’t want a ugly baby.

BENJAMIN: Are the cute ones more ‘spensive?

CASSIE: No, but girls cost more than boys ‘cause they’re sweeter.

BENJAMIN: That’s stupid.

CASSIE: (Shocked.) Um! You said a bad word! Daddy says I’m not pa-spost to say that.

BENJAMIN: “Stupid” isn’t a bad word. It’s a name.

CASSIE: Nuh-uh. (Stage whisper on the first word only, which she thinks is a curse.) “Stupid” isn’t a NAME.

BENJAMIN: Yes, so! Daddy has a new friend named “Stupid!” Mommy says her whole name is “Stupid Widdle Hussy!”

CASSIE: Dat’s a weird name.

BENJAMIN: Yeah, but not everyone can use her whole name. I called her that once during one of my daddy weekends, and boy did I get in trouble!

CASSIE: What’s a daddy weekend?

BENJAMIN: Ever since my family got a da-borce, I live wif my mommy, but I get to go stay wif my daddy sometimes.

CASSIE: Oh. (Beat.) What’s a da-borce?

BENJAMIN: It’s when a mommy finds out a daddy is a… (Matter-of-fact, as if reciting something he has been told but doesn’t understand, but complete with sassy side-to-side head motions.) …“a two-timing low-life deadbeat, and she’s better off wif-out him.”

CASSIE: (Doesn’t really understand either.) Oh.

BENJAMIN: Let’s pway sum-fing. Do you gots a X-Box?

CASSIE: No…

BENJAMIN: Do you gots a ‘Tendo, or a Pwaystation?

CASSIE: No. My daddy says bideo games wot your bwain.

BENJAMIN: No they don’t. I have a X-Box at home and my brain is good. Wait. (BENJAMIN seems to freeze, unmoving, with a puzzled look on his face for two seconds. Suddenly, with no warning, he unleashes a single powerful sneeze.) Choo!

CASSIE: (Hurrying away from him in disgust.) Eww! You’re pa-spost to cover your mouth so you don’t spway germs.

BENJAMIN: I don’t gots germs. I just took a baff yesterday. What DO you have to play wif, a-sides coloring?

CASSIE: Um, I have Legos.

BENJAMIN: That’s boring stuff.

CASSIE: (With a shrug.) We could play grown-up again.

BENJAMIN: (Grudgingly.) Ugh! Okay, but I gets to play it MY way this time. And I don’t wanna hafta be married. (Pause He crosses his arms defiantly.) I need my freedom.

CASSIE: Okay. We can be grown-ups, but we’re not mawwied.

BENJAMIN: Good.

(BENJAMIN and CASSIE both stand, resuming their grown-up voices. CASSIE extends a hand to shake.)

CASSIE (ADULT): (Hand out.) Hello, person I don’t know. Nice to meet you. What’s your name?

BENJAMIN (ADULT): (Shaking her hand.) Benjamin. But you can call me Captain Awesome.

CASSIE (ADULT): Yeah, I won’t be doing that. My name is Cassie. (Walking and gesturing all around the room.) Welcome to my house. It has a thousand rooms, and a swimming pool, and a bouncy castle, and a zoo. And I have three ponies, and their names are Rainbow, Buttercup, and Sparkles.

BENJAMIN (ADULT): That’s nuffin’. (Walking and gesturing all around the room.) MY house has a MILLION rooms, with a real live train that goes through every room, and I always get to drive it. And it has laser tag, and a trampoline, and a race track, and a free candy store, and every video game ever. And plus, I have a pet tiger, and he eats ponies for breffest!

CASSIE (ADULT): Well, my… um… my ponies can’t be eaten. They’re covered with special fur that’s poison to tigers, and if a tiger tries to eat them, the tiger dies instantly.

BENJAMIN (ADULT): Well, I also have a T-rex, who is a-mmune to their special fur, and his name is Death To All Ponies! (Roars his T-rex impression, complete with short arms.)

CASSIE (ADULT): But their special fur protects them from ALL amm-inals that try to eat them.

BENJAMIN (ADULT): Hmm. (Pointing out above the audience.) Oh no! Monsters! Giant monsters are here to eat us up!

CASSIE (ADULT): Oh no!

BENJAMIN (ADULT): And they’re about to step on your ponies and SQUISH ‘em! (Grabbing a blanket or a long-sleeved jacket or sweater, he ties or holds it around his neck, quickly forming a makeshift cape.) But it’s okay, because I’m a super-hero! (Arms in front as if flying, he runs around the room.) I’ll save us from the monsters!

CASSIE (ADULT): (Grabbing her own blanket or jacket, and making her own cape.) Yes! And I’m a super-hero too, so I’ll save us too! Those monsters won’t step on MY ponies!

BENJAMIN (ADULT): (Stops running and looks at her incredulously.) YOU can’t be a super-hero.

CASSIE (ADULT): Why not?

BENJAMIN (ADULT): Duh! You’re a girl.

CASSIE (ADULT): (Hands on hips.) EXCUSE me? For your inflammation, girls can be ANYTHING.

BENJAMIN (ADULT): Name one good super-hero girl.

CASSIE (ADULT): Okay… (Counting on her fingers.) Wonder Woman, Supergirl, Batgirl, Bwack Widow…

BENJAMIN (ADULT): All right, so there’s a FEW.

CASSIE (ADULT): (Continues counting.) Bwack Canary, Scarlet Witch, Inbisible Woman, Captain Marvel…

BENJAMIN (ADULT): Okay, you can stop now! How do you know so many?

CASSIE (ADULT): My daddy reads to me every night, and sometimes he reads me his old comic books. The girl heroes are the best.

BENJAMIN (ADULT): UGH! Fine. You can be a girl hero.

CASSIE (ADULT): I know. And I’m also starting my own team of super-heroes, and we’re going to be called the Super-Dupers!

BENJAMIN (ADULT): Yay, okay! Who else is on our team?

CASSIE (ADULT): Oh, it’s not OUR team, it’s MY team. And we don’t allow members who think girls can’t be super-heroes. I’m sorry, but I don’t think you’re right for the Super-Dupers.

BENJAMIN (ADULT): (Under his breath.) Hmph. More like Super-POOPERS. (Furious, crossing his arms.) You’re mean! I’m mad at you.

(BENJAMIN throws off the cape and sits down, a child again. He gives CASSIE the stink-eye death stare.)

CASSIE: (Also a child again.) Don’t get angwy. You’re pa-post to use your big boy words.

BENJAMIN: I don’t wanna play any more. (He resumes coloring.)

CASSIE: (Sitting with him, also a child again.) You know, my daddy’s a super-hero for real life. (She resumes coloring as well.)

BENJAMIN: What? No, he’s not.

CASSIE: He is so, ‘cause he saved me from you at the pwayground. A-member the first day we ever met? I was walking past the swings, and YOU almos’ kicked me, but my daddy pulled me out of the way.

BENJAMIN: That doesn’t make him a super-hero, it just makes him a daddy.

CASSIE: And then your mommy came ober, and ‘pologized that you almos’ kicked me, and my daddy said it was okay, and they started talking and laughing.

BENJAMIN: (Accusatory.) You’re a-post to watch where you’re going, you know. (Changing his tone to boastful.) I’m a good swinger.

CASSIE: Your mommy is nice. I nebber met MY mommy.

BENJAMIN: Why not?

CASSIE: She had to go away. At the hop-spital, they told us that only one of us could go home with daddy, and the other one had to go to a pwace called Heaben. Daddy says mommy let ME be the one to go home ‘cause she wuvs me more than ANY-sing. But it’s okay, ‘cause when you move to there, they give you wings so you can fly around! (Pretends to run and fly again.)

BENJAMIN: Cool! I wanna move there too!

CASSIE: And also, I sink they have big spy cameras there, ‘cause daddy says mommy is still watching me from Heaben, even though it’s so far away.

BENJAMIN: (Mind blown.) Whoa. Can she see us right now?

CASSIE: I sink so.

(BENJAMIN and CASSIE both look upwards and all around the room, searching for cameras.)

BENJAMIN: I wanna be a spy when I’m growed up.

CASSIE: I want to be a powice ossifer, or maybe a amm-inal doctor.

BENJAMIN: But I still wanna play and have fun and stuff. Growed-ups are boring, and they do weird stuff ‘stead of fun stuff.

CASSIE: Like what?

BENJAMIN: Like on my daddy weekends, daddy and Stupid are always kissing and hugging and gross stuff like that. Yuck.

CASSIE: Y’know, MY daddy and YOUR mommy do kissing stuff, too.

BENJAMIN: (Disgusted.) Eww! No they don’t!

CASSIE: Yes they do. I seen ‘em. It’s how come they’re making us do a pwaydate, so they can kiss and stuff.

BENJAMIN: Nuh-uh. We’re having a playdate so they can do chores.

CASSIE: Chores?

BENJAMIN: Yeah, ‘cause I heard my mommy talking to my Aunt Becky on the phone about it, and mommy said it was goin’ good and pretty soon, they were finally gonna sweep togever.

CASSIE: (Disgusted.) Bluck! Eww. I hate chores.

BENJAMIN: Me, too.

CASSIE: But I sink it’s okay when people do kissy stuff. It means they wike each other.

BENJAMIN: Eww! No, it’s NOT okay! Their mouths touch, and that’s a-zactly how you get cooties.

CASSIE: Cooties aren’t weal.

BENJAMIN: YES, HUH! You don’t even believe in cooties?

CASSIE: Daddy took me to the doctor once, and the doctor said I hafta worry about “germs” an’ “buck-teria,” but not cooties.

BENJAMIN: You’re so weird. I don’t fink I wanna play any more. I’m gonna tell mommy I wanna leave.

(He stands.)

CASSIE: (Cautionary tone.) We’re not pa-spost to bother ‘em ‘less it’s a ‘mergency.

BENJAMIN: This IS a ma-mergency. You’re WEIRD, and it’s freaking me out. I’m gonna go talk to mommy. (Starts to walk towards SL.) Mommy!

CASSIE: (Knowingly.) Okay. I warned you.

(BENJAMIN exits SL, leaving CASSIE alone to color. After a few seconds, he runs back onstage, eyes wide as if he just saw something horrific offstage that has traumatized him forever. He is screaming and running non-stop towards SR.)

BENJAMIN: (Screaming as he runs, not even looking at her.) Eeeeewwwwwww!!! I don’t wanna play any more!!!

(BENJAMIN exits SR as fast as he can. CASSIE shrugs and goes back to coloring. Lights out.)

THE END
```

---

## IC-0868: STOP!

- Title: STOP!
- Author (byline): Ray Nesrym, © 2010
- Work: STOP!
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1480
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
MOM. Are you sure you’re ready for this?
CHILD. Mom the driver’s ed instructor said I was one of the best students in my class.
MOM. So you think you can do this?
CHILD. I’m sure I can do this, now will you give me the keys?
MOM. (reluctantly)Ok... Wait! What if you crash! You won’t crash will you?
CHILD. MOM!
MOM. Alright here you go. (hands over keys) Ok now go ahead and buckle you’re seatbelt,
then adjust your mirrors…and the seat…Oh! And don’t forget your wheel…Um… Are you
sure that’s low enough? I think the wheel should be lower.
CHILD. Mom it’s fine how it is.
MOM. It looks a little high… are you sure you don’t want it lower?
CHILD. Yes I’m sure, now buckle your seatbelt,
MOM. Why?
CHILD. In case we crash
MOM. Are you gonna crash? Maybe you shouldn’t drive yet
CHILD. Mom calm down. I’m not gonna crash, now are you ready to go?
MOM. Ok, now the next thing you do is start the car.
CHILD. Really, I had no idea.(starts car and changes gear)
MOM. Well dear that’s why I’m here, Now go ahead and put it in reverse
CHILD. Already done
MOM. Oh…ok, then go ahead and start pulling out of the drive way…Wait! Make sure no
one’s behind you first. Ok you can go. Woah! Slow down we aren’t in a hurry….Watch out
for the mailbox!
CHILD. ( while backing up) Mom, calm down. I’m just pulling out of the driveway.
MOM. Sorry...Don’t forget to start turning!
CHILD. (while turning) Mom, I got it ok?
MOM. Ok, go ahead and (gulp) put it in drive
CHILD. Gladly (changes gears)
MOM. (worried leaning to left) Um you need to stay a little more to the right
dear….Woah!(moves away form the window) not that far right!...Whew! that was close, you
could’ve hit a mailbox or something.
CHILD. Mom there’s not a single mailbox on this road how could I possibly hit one!
MOM. Well if there was one you might’ve hit it!
CHILD. But there wasn’t
MOM. But what if there was! You’re driving now, you’ve really got to be thinking about
these things!
CHILD. (annoyed) Of course mother
MOM. Now why are you going so slow the speed limit is twenty-five and you’re going
fifteen.
CHILD. I’m going twenty
MOM. Oh, well you can still go a little faster.
CHILD. Fine
MOM. Careful though!!! You don’t want to go to fast!
CHILD. (sarcastically)Really I didn’t know that
MOM. Are you being sarcastic?
CHILD. (with more sarcasm) Nope not at all.
MOM. So they didn’t teach you not to drive to fast in drivers ed?-
CHILD. Mom, I was kidding
MOM. Oh…well it wasn’t very funny…Um… I think you should probably start slowing
down.
CHILD. Why?
MOM. There’s a stop sign ahead, Don’t you see it?
CHILD. (confused)No…?
MOM. (worried clutching dash board) Oh my god! You don’t see the stop sign! What kind
of a driver are you?

CHILD. What stop sign are you talking about?
MOM. The one ahead of us, down by the school.
CHILD. Wait, the school? We aren’t even near there, Heck I can’t even see the school yet.
MOM. Well you should know it’s coming up and be prepared for it
CHILD. Fine I will be prepared for it, when we get there.
MOM. No, you need to start slowing down now so you can stop completely.
CHILD. Are you being sarcastic?
MOM. Of course not! Now are you gonna slow down or what?
CHILD. Fine
MOM. Now slow down, slower, slower! Keep slowing, more, more, you’re getting there,
slower, almost!
CHILD. Mom, we aren’t going to get anywhere at five miles-per-hour.
MOM. Just Keep going, but slower. AAaannnddddd…STOP(hits imaginary break) Whew,
now let this guy go since he has the right-of-way… Ok go ahead, Good job.
CHILD. Good job? Did I actually do something to meet your standards?
MOM. Well… Close enough, you could’ve stopped sooner, but it’s no big deal, just make
sure from now on when you stop the front of the car is behind the sign, not next to it.
CHILD. (sarcastically) Of course
MOM. There’s another stop sign up ahead, lets see if you can do this one by yourself.
CHILD. Ok…lets see… (mockingly)Now slow down, slower, slower, keep slowing. More,
more, you’re getting there, slower, almost, just keep going, but slower,
aaaannnnnddddd…stop. How was that?
MOM. You need to pull up more so you can see farther down the road.
CHILD. What next.
MOM. WATCH OUT! There’s a red light coming up.
CHILD. Mom, it’s green
MOM. No, the one after that!

CHILD. But, I’m not there yet. Shouldn't I worry about the one coming up first.
MOM. You’re right
CHILD. Oh no
MOM. What?
CHILD. Are you sick? You just said I was right!
MOM. Well, you are right, since you’re still a new driver we should try and make sure you
don’t worry about to much a once, it might confuse you. So just worry about the green light
ahead,
CHILD. It turned red already.
MOM. Oh no! slow down (covering eyes) you need to stop! Don’t hit the car in front of
you!
CHILD. (rolls eyes and stops car) Can I turn on the radio?
MOM. Of course not! It would distract you and you might end up crashing.
CHILD. You’re right, one big distraction is enough
MOM. exactly….wait a second-
CHILD. (quickly) Light’s green lets go
MOM. Turn right up here
CHILD. Ok I have to change lanes first though.
MOM. oh! Wait a second! (rolls down window looks out) Ok you can go
CHILD. Mom can you just calm down
MOM. No, not really, in fact I keep getting more worried. I think you should stop
CHILD. But there’s not a stop sign or red light anywhere near. Why do I need to stop this
time?
MOM. I didn’t mean like that, I meant stop driving for the day.
CHILD. Why? What have I done now? Did I turn to sharp or something?
MOM. Actually yes you did, but that’s not why I want you to stop. I’m just nervous. I don’t
want anything to happen
CHILD. Mom, nothing’s happened yet. I haven’t even done anything really dangerous yet. I
mean-
MOM. Wait…what do mean yet, were you planning on doing something dangerous?
CHILD. Of course not
MOM. Sorry, I’m just not ready for you to drive yet. Um… could you turn into this parking
lot… Slow down!!!! You’re turning too fast! You need to slow down when you turn, or you
could flip teh car over or something!... Now could you park between that red van and black
truck? You know how to park right?
CHILD. Yes mom.
MOM. Ok go ahead then…Turn sharper!!!! Now watch your sides…Straighten it! Straighten
it!!... Now pull forward, a little more, no that’s too much you need to go back!
CHILD. Mom, it doesn’t have to be perfect, we’re just switching seats.
MOM. Fine, well go ahead and put it in park then.
CHILD. Ok…I’m gonna leave the keys in alright?
MOM. What if someone tries to steal the car?
CHILD. Mom, we’re just switching seats, we aren’t even really leaving the car.
MOM. Fine, lets go (they switch seats) You know you’re supposed to walk around behind
the car not in front of it
CHILD. Does it matter?
MOM. Of course it does!
CHILD. Why?
MOM. Well… I don’t remember, but it’s for your own safety.
CHILD. of course it is
MOM. I know you wanted to keep driving, but I’m just really nervous. Maybe later you can
drive with your father. (pulls out quickly)
CHILD. Woah , Mom… did you even look behind you before you pulled out?
MOM. Oh it’s fine, I could tell there wasn’t anyone behind me,
CHILD. How could you tell?

MOM. After you’ve driven as long as I have you can just tell.
CHILD. um…ok…
MOM. Now Why is that lady ahead of us going so slow? (honking horn)GET OFF THE
ROAD GRANDMA!
CHILD. Um…mom? She’s going the speed limit.
MOM. She’s going slow!
CHILD. uh…I don’t think you should be tailgating her like that.
MOM. You’re right I can just pass her (turns wheel)
CHILD. MOM! You aren’t supposed to go in that line. It’s for the oncoming traffic.
MOM. Well there is no oncoming traffic now is there.
CHILD. …Um, there’s a stop sign coming up and you’re still going at least 15 miles over the
speed limit.
MOM. Well, if there’s no cop don’t stop.
CHILD. I’m pretty sure that’s not what the law says…Woah! Slow down! The light turned
yellow!
MOM. It’s fine, I can make it.
CHILD. I don’t know if that’s a good idea.
MOM. I know what I’m doing I’ve been driving for twenty-three years. Now if i want your
opinion then I'll ask for it.
CHILD. But jsut because you've been driving for twenty-three years doesn't meanThat
doesn’t mean you can’t-
*CRASH!*
CHILD. Way to go Mom, way to go.
```

---

## IC-0869: The Assistant

- Title: The Assistant
- Author (byline): Don Trickseven
- Work: The Assistant
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1919
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
(At rise, Drew is hunched on the couch, in extreme anxiety. His wife, Mel, is caressing him, trying to
soothe him and talk him through his crisis.)
Mel: Let’s get this straight.
Drew: I’m not sure that’s possible.
Mel: You know what you saw.
Drew: I’m not sure I do.
Mel: You saw Coach Wennum...
Drew: I think I saw him. I was close enough, that I think it was him.
Mel: And he was with a girl?
Drew: This girl, I think, her name is Cassandra. I know it was her, because she was the one who got
involved with Calvin during the Conference Tournament last year, and we had to talk to her.
Mel: The cheerleader, right.
Drew: She’s a senior.
Mel: Ok.
Drew: She’s an adult. They’re both adults.
Mel: Coach Wennum is 48.
Drew: If it was Coach.
Mel: Honey, you spend 8 hours a day with Coach. You’d know him from across the arena.
Drew: Yeah. I guess.
Mel: But what happened?
Drew: I think that...
Mel: No, not what you think. What did you see?
Drew: He definitely, definitely had her on the ground.
Mel: On the ground?

Drew: Right.
Mel: What do you mean he had her there?
Drew: Stop. Stop interrogating me. This is hard.
Mel: (She realizes how angry she is, and pulls back to try to help him.) I know sweetie. I know.
Drew: I almost didn’t tell you - or anyone.
Mel: Well... you did. You will.
Drew: I did see something.
Mel: And that’s why you have to say something.
Drew: Right. That’s how it works.
Mel: This is about you. And us. Our future.
Drew: How can you say that? It’s about coach, and the team. Those 12 guys. They’re counting on him to
put them on the right path.
Mel: Well what about that girl’s future?
Drew: She looked fine.
Mel: Did she really?
Drew: No. I couldn’t see.
Mel: Why were you even in there?
Drew: I forgot my phone. It was 20 minutes after practice, everyone’s usually long gone from the court. I
may not have even seen them, only the emergency lights were on. But I heard her.
Mel: She said something.
Drew: “No.”
Mel: She didn’t say anything.
Drew: No, no, she said, “No.”
Mel: How many times?
Drew: A lot. I think. Well, depends what “a lot” means. More than once.
Mel: I can’t believe you saw this.
Drew: Whatever I saw.
Mel: Wennum is a bastard. He was on top of that girl, that little girl, and she was telling him no.
Drew: You’re mad at him now, because you think she said no? Even though I’m not sure I heard it.

Mel: What did you just say! That’s what you just said. Drew: I don’t know what I said. Mel: You have to tell them. Drew: No. Mel: What if that was Leyla? Drew: Don’t say that. Our daughter wouldn’t let that happen. Mel: How dare you! Drew: Leyla would not be that stupid. Mel: How can you be so stupid? Drew: I’ve been taught to be that stupid. I’ve been taught that people can learn what’s right and wrong. I was taught that if you gave yourself to a greater thing, a program, you would make stronger people. People who can take care of themselves and their families. Mel: Well you are not that person. You are not taking care of you family, if you let this happen. Coach is taking care of you, and your family. You are his little squeaking child. An infant, letting him make all the decisions for you. Drew: That’s what Coach is good at! He’s there to make the decisions. Remember that time he drove all the way to _ to get Marion out of jail? Mel: You’ve only told the story twenty-two times. Drew: I was in that pickup with him. He did 90 for three hours to get there. All he kept saying to me is, “We can’t let this one get away from us.” He still had hope, for Marion. And you know only he saw it. I would have left him in that jail, for stealing a damn Xbox. How dumb can you be? But Coach was willing to keep him, even though he’d be suspended for a year and take up one of our scholarship spots. He went in there and you know, that police officer, he’d never seen anyone stand up for a black kid like that. Coach said to him, “You don’t know this kid. And that’s ok. It’s not your job to know him. But it’s my job to know him, know him better than he knows himself. And I tell you he’s not one of the bad ones.” They let him out. Mel: He did do the right thing there. Drew: Exactly. That night when the four of us were in the motel, I thought, this is why I wanted to do this. Mel: Four of you? Drew: Well, Nisha was with us, Marion’s girlfriend. She’s the one who told us what happened. Mel: She went with you. Drew: Yes, she insisted. Coach too. Mel: Whose room was she in? Drew: Oh no, don’t worry. I didn’t stay with her!

Mel: No. Whose room was she in.
Drew: Well, we couldn’t buy a room for Marion and Nisha... that wouldn’t have been responsible.
Mel: So she stayed with coach.
Drew: Uh huh.
Mel: Didn’t Marion break up with her right after that.
Drew: He did. He said she had... messed around. You’re not thinking Coach was involved there too, are
you?
Mel: Jesus, how could you not tell me that, either? What else are you hiding?
Drew: I’m not hiding anything. I’m telling you everything.
Mel: I’m sorry. But you are hiding it whether you know it or not. I know it’s hard.
Drew: It doesn’t have to be hard.
Mel: Yes it does. It is. Even if you lie, even if you never say anything, it will never be easy. This is not the
easy way out.
Drew: Not for me. But for the team - those men on the team -
Mel: And the girls?
Drew: It’s too late for them.
Mel: That’s so selfish.
Drew: You know what? If you’re so sure, you report it yourself.
Mel: What?
Drew: There’s a security camera in the gym. You can tell our security service to look at it. It’s off campus,
for this reason. No bias.
Mel: You want me to do this for you? You want me to be a human being so you can be a cowardly soldier
for this man?
Drew: Here’s the number. All the tips are anonymous.
Mel: You are smaller than I thought. You are not the man I married.
Drew: Maybe not. I tried, but maybe not.
Mel: They won’t even believe me.
Drew: If you say what tape to look at, and when, they have to look. The people at the other end don’t work
here. You don’t have to say who you are.
Mel: Then why don’t you do it?

Drew: I’d prefer you didn’t say who you were. I’m going to go tuck our daughter in. Mel: Don’t even think about leaving this room! You are going to stand here -

(Drew leaves. Mel is still furious, but dials.) Mel: Yes, I have something to report. (pause) Anonymously. (pause) Wyoming. (pause) It’s at –

(Drew returns, angry. He grabs the phone.) Drew: Hang it up! Hang it up!

(Mel yelps in pain. He hurt her hand as he grabbed the phone.)
Drew: I can’t believe you would go through with it.
Mel: You knew who I was when we got married. Although I didn’t know you, it seems.
Drew: It doesn’t seem like it. You put family first, then. Now it’s about... some vague thing. Justice.
Who are you to decide? Who are you to put your conscious before our family?
Mel: You hurt me.
Drew: I’m sorry. I’m angry.
Mel: You don’t know what anger is.
Drew: I don’t?
Mel: My father knew.
Drew: Oh Christ.
Mel: My father knew anger when his little girl got hurt.
Drew: What do you mean?
Mel: I mean when I was in college, I was assaulted.
Drew: Now I’m going to hear THIS? I cannot believe this. You would hide this from me?
Mel: You know nothing. See, you think you know everything, but you know nothing.
Drew: Not when people lie to me.
Mel: The way you have lied to me! The way you want to lie to everyone about Coach!
Drew: What happened to you, tell me right now.
Mel: Since you know everything, you know the story. A boy older than me, by a year. A friend from
Reading Squad, someone who led our outreach to schools. It was at a party.
Drew: Did he rape you?
Mel: Yes. He forced himself on me.

Drew: And you said no?
Mel: He knew he wasn’t doing the right thing.
Drew: Right. And what did you do?
Mel: I told my dad.
Drew: But did you tell the school? Did you turn him in?
Mel: Thanks for asking about me.
Drew: Well here you are. You’re fine. You must be fine, you didn’t even tell me about it.
Mel: I told my dad and we made sure the boy knew never to come near me again.
Drew: Oh, I see.
Mel: What?
Drew: You didn’t tell anyone else. You did exactly what you don’t want me to do. You shielded your little
group.
Mel: We were doing something very important. And I knew I was the only one.
Drew: You were sure.
Mel: I was sure. That stupid boy loved me.
Drew: Well, then.
Mel: I was wrong. And this situation is different. Coach could have a dozen girls that’s he’s...
Drew: Or maybe just one. Maybe he loved her.
Mel: No. That’s not what you saw.
Drew: You weren’t there. You didn’t see it.
Mel: Tell me what you would have needed to see.
Drew: I would have had to walk right up and see it, and ask them, is this ok? Are you both ok?
Mel: You wanted them to walk with you, you wanted Coach to turn himself in. Like he would do that.
Drew: He would. (lighting up) Wait, he would. Coach would know when to do the right thing, when he
had made a mistake.
Mel: Now that doesn’t make any sense.
Drew: I’ll talk to him. I will talk to him, and he will make the right choice. He’ll turn himself in, to the
university, to the police.
Mel: What makes you so sure?
Drew: He just needs to hear it. If he hears it, he will see his actions in the proper light, and it will be
obvious that he needs to change. I just have to show it to him.
Mel: What if he doesn’t do the right thing?
Drew: I don’t know.
Mel: It shouldn’t be up to him.
Drew: It’s up to me.
Mel: It shouldn’t be up to anyone. If he raped that girl, he has to be made responsible.
Drew: I will talk to him.
Mel: When?
Drew: Next week, when we’re back from the preseason tournament. I want the boys to have a good start to
the season.
Mel: When you’re back from the tournament! But there will be so many chances, and you might change
your mind, and oh - I can’t even list all the things wrong with that.
Drew: It’s the only choice I can make. Just like you could only tell your father, I can only tell coach. It’s
the only choice, for me.
Mel: I might have to make my own choice, now.
Drew: (staring at her, finally with compassion) I understand that.
Mel: Ok.
Drew: Ok. Ok. This time, I’m really leaving. You call if you want to. I won’t ask you either way.
Mel: Ok.
Drew: Goodnight.

(He leaves. Mel stares at the phone for a long time, holding it in her hand. She grows angrier, and angrier, whether at herself, or Drew, or Coach, is unclear. She may be about to dial or throw the phone away. At the peak of her rage, blackout. The play is over.)
```

---

## IC-0870: My Children! My Africa!

- Title: My Children! My Africa!
- Author (byline): Athol Fugard
- Work: Not specified
- Publisher: Theatre Communications Group
- Publication date as stated: Oct 1990
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: THAMI, ISABEL
- Teaser before the introduction: No
- Spoken words (computed): 1925
- Already set (do not supply): none

### Source block (context only)

```text
Author: Athol Fugard
ISBN: 1559360143
Publisher: Theatre Communications Group
Date (Month/Year): Oct 1990
```

### Introduction (context only: never use it for content warnings)

```text
Actor 1: When playwright Athol Fugard wrote his drama "My Children, My Africa," he did it to save his country. It was 1985. The apartheid laws that denied freedom to blacks were fueling riots, boycotts and demonstrations across South Africa. Worried that his country would never see peace, Fugard wrote the play in hopes that the polarization between blacks and whites would end.

Actor 2: Based on real events, "My Children, My Africa" tells the story of a teacher's attempt to bring understanding between two of his students. The teacher, Mr. M, arranges a debate between Isabel, a middle class white girl, and Thami, a black boy who grew up in the Coketown ghetto. Their journey toward understanding each other brings acceptance, but not without pain and tragedy along the way.

Together: My Children! My Africa! By Athol Fugard.
```

### Performance text (classify this)

```text
(THAMI waiting. ISABEL arrives.)

THAMI: Isabel.

ISABEL: (It takes her a few seconds to respond.) Hello, Thami.

THAMI: Thank you for coming.

ISABEL: (SHE is tense. Talking to him is not easy.) I wasn't going to. Let me tell you straight out that there is nothing in this world... nothing!...that I want to see less at this moment than anything or anybody from the location. But you said in your note that it was urgent, so here I am. If you've got something to say, I'll listen.

THAMI: Are you in a hurry?

ISABEL: I haven't got to be somewhere else, if that's what you mean. But if you're asking because it looks as if I would like to run away from here, from you!...very fast, then the answer is yes. But don't worry, I'll be able to control that urge for as long as you need to say what you want to.

THAMI: (Awkward in the face of Isabel's severe and unyielding attitude.) I just wanted to say goodbye.

ISABEL: Again?

THAMI: What do you mean?

ISABEL: You've already done that, Thami. Maybe you didn't use that word, but you turned your back on me and walked out of my life that last afternoon the three of us... (SHE can't finish.) How long ago was that?

THAMI: Three weeks I think.

ISABEL: So why do you want to do it again? Aren't you happy with the last time? It was so dramatic, Thami.

THAMI: (patiently.) I wanted to see you because I'm leaving the town; I'm going away for good.

ISABEL: Oh, I see. This is meant to be a "sad" goodbye is it? (SHE is on the edge.) I'm sorry if I'm hurting your feelings but I thought you wanted to see me because you had something to say about recent events in our little community... (Out of a pocket a crumpled little piece of newspaper which SHE opens with unsteady hands.) ...certain unrest related... I think that is the phrase they use...yes...here is is... (Reading.) "...unrest related incident in which according to witnesses the defenseless teacher was attacked by a group of blacks who struck him over the head with an iron rod before setting him on fire."

THAMI: Stop it, Isabel.

ISABEL: (Fighting hard for self-control.) Oh, Thami I wish I could! I've tried everything, but nothing helps. It just keeps going around and around inside my head. I've tried crying. I've tried praying! I've even tried confrontation. Ja, the day after it happened I tried to get into the location. I wanted to find the witnesses who reported it so accurately and ask them: ...why didn't you stop it! There was a police roadblock at the entrance and they wouldn't let me in. They thought I was crazy or something and "escorted" me back into the safekeeping of two now very frightened parents. There is nothing wrong with me! All I need is someone to tell me why he was killed. What madness drove those people to kill a man who had devoted his whole life to helping them. He was such a good man, Thami! He was one of the most beautiful human beings I have ever known and his death is the ugliest thing I have ever known.

THAMI: (Gives her a few seconds to calm down. Gently.) He was an informer, Isabel. Somehow or the other somebody discovered that Mr. M was an informer.

ISABEL: You mean that list of pupils taking part in the boycott? You call that informing?

THAMI: No. It was worse than that. He went to the police and gave them the names and addresses of our political action committee. All of them were arrested after his visit. They are now in detention.

ISABEL: Mr. M did that?

THAMI: Yes.

ISABEL: I don't believe it.

THAMI: It's true, Isabel.

ISABEL: No! What proof do you have?

THAMI: His own words. He told me so himself. I didn't believe it either when he was first accused, but the last time I saw him, he said it was true, that he had been to the police.

ISABEL: (Stunned disbelief.) Mr. M? A police spy? For how long?

THAMI: No. It wasn't like that. He wasn't paid or anything. He went to the police just that one time. He said he felt it was his duty.

ISABEL: What do you mean?

THAMI: Operation Qhumisa...the boycotts and strikes, the arson... you know he didn't agree with any of that. But he was also very confused about it all. I think he wished he had never done it.

ISABEL: So he went to the police just once. As a matter of conscience. That doesn't make him an "informer," Thami!

THAMI: Then what do you call somebody who gives information to the police?

ISABEL: No! You know what that word really means, the sort of person it suggests. Was Mr. M one of those? He was acting out of concern for his people...you said so yourself. He though he was doing the right thing! You don't murder a man for that!

THAMI: (Near the end of his patience.) Be careful, Isabel.

ISABEL: Of what?

THAMI: The words you use.

ISABEL: Oh? Which one don't you like? Murder? What do you want me to call it... "an unrest related incident?" If you are going to call him an informer, then I am going to call his death murder!

THAMI: It was an act of self-defense.

ISABEL: By who?

THAMI: The People.

ISABEL: (Almost speechless with outrage.) What? A mad mob attacks one unarmed defenseless man and you want me to call it...

THAMI: (Abandoning all attempts at patience. HE speaks with the full authority of the anger inside him.) Stop it, Isabel! You just keep quiet now and listen to me. You're always saying you want to understand us and what it means to be black...well if you do, listen to me carefully now. I don't call it murder, and I don't call the people who did it a mad mob and yes, I do expect you to see it as an act of self-defense... listen to me!.. .blind and stupid but still self-defense.

He betrayed us and our fight for freedom. Five men are in detention because of Mr. M's visit to the police station. There have been other arrests and there will be more. Why do you think I'm running away? How were those people to know he wasn't a paid informer who had been doing it for a long time and would do it again? They were defending themselves against what they thought was a terrible danger to themselves. What Angela Myalatya did to them and their cause is what your laws define as treason when it is done to you and threatens the safety and security of your comfortable white world. Anybody accused of it is put on trial in your courts and if found guilty they get hanged. Many of my people have been found guilty and have been hanged. Those hangings we call murder! Try to understand, Isabel. Try to imagine what it is like to be a black person, choking inside with rage and frustration, bitterness, and then to discover that one of your own kind is a traitor, has betrayed you to those responsible for the suffering and misery of your family, of your people. What would you do? Remember there is no magistrate or court you can drag him to and demand that he be tried for that crime. There is no justice for black people in this country other than what we make for ourselves. When you judge us for what happened in front of the school four days ago just remember that you carry a share of the responsibility for it. It is your laws that have made simple, decent black people so desperate that they turn into "mad mobs."

(ISABEL has been listening and watching intently. It looks as if SHE is going to say something but SHE stops herself)

THAMI: Say it, Isabel.

ISABEL: No.

THAMI: This is your last chance. You once challenged me to be honest with you. I'm challenging you now.

ISABEL: (SHE faces him.) Where were you when it happened, Thami? (pause.) And if you were, did you try to stop them?

THAMI: Isn't there a third question, Isabel? Was I one of the mob that killed him?

ISABEL: Yes. Forgive me, Thami...please forgive me! ...But there is that question as well. Only once! Believe me, only once.. .late at night when I couldn't sleep. I couldn't believe it was there in my head, but I heard the words... "Was Thami one of the ones who did it?"

THAMI: If the police catch me, that's the question they will ask.

ISABEL: I'm asking you because... (An open, helpless gesture.) ...I'm lost! I don't know what to think or feel anymore. Help me. Please. You're the only one who can. Nobody else seems to understand that I loved him. (This final confrontation is steady and unflinching on both sides.)

THAMI: Yes, I was there. Yes, I did try to stop it. (THAMI gives Isabel the time to deal with his answer.) I knew how angry the people were. I went to warn him. If he had listened to me he would still be alive, but he wouldn't. It was almost as if he wanted it to happen. I think he hated himself very much for what he had done, Isabel. Re kept saying to me that it was all over. Re was right. There was nothing left for him. That visit to the police station had finished everything. Nobody would have ever spoken to him again or let him teach their children.

ISABEL: Oh, Thami, it is all so wrong! So stupid! That's what I can't take...the terrible stupidity of it. We needed him. All of us.

THAMI: I know.

ISABEL: Then why is he dead?

THAMI: You must stop asking these questions, Isabel. You know the answers.

ISABEL: They don't make any sense, Thami.

THAMI: I know what you are feeling. (pause.) I also loved him. Doesn't help much to say it now, I know, but I did. Because he made me angry and impatient with his "old fashioned" ideas, I didn't want to admit it. Even if I had, it wouldn't have stopped me from doing what I did, the boycott and everything, but I should have tried harder to make him understand why I was doing it. You were right to ask about that. Now...? (A helpless gesture.) You know the most terrible words in your language, Isabel? Too late. I'll never forgive myself for not trying harder with him and letting him know.. .my true feelings for him. Right until the end I tried to deny it...to him, to myself.

ISABEL: I'm sorry I...

THAMI: That's all right.

ISABEL: Are the police really looking for you?

THAMI: Yes. Some of my friends have already been detained. They're pulling in anybody they can get their hands on.

ISABEL: Where are you going? Cape Town?

THAMI: No. That's the first place they'll look. I've written to my parents telling them about everything. I'm heading north.

ISABEL: To where?

THAMI: Far, Isabel. I'm leaving the country.

ISABEL: Does that mean what I think it does?

THAMI: (Nods.) I'm going to join the movement. I want to be a fighter. I've been thinking about it for a long time. Now I know it's the right thing to do. I don't want to end up being one of the mob that killed Mr. M-but that will happen to me if I stay here.

ISABEL: Oh, Thami.

THAMI: I know I'm doing the right thing. Believe me. And you?

ISABEL: I don't know what to do with myself, Thami. All I know is that I'm frightened of losing him. Re's only been dead four days and I think I'm already starting to forget what he looked like. But the worst thing is that there's nowhere for me to go and.. .you know.. .just be near him. That's so awful. I got my father to phone the police but they said there wasn't enough left of him to justify a grave. What there was had been disposed of in a "Christian manner." So where do I go? The burnt-out ruins of the school? I couldn't face that.

THAMI: Get your father or somebody to drive you to the top of the Wapadsberg Pass. It's on the road to Craddock. It was a very special place to him. He told me that it was there where it all started, where he knew what he wanted to do with his life...being a teacher, being the Mr. M we knew. You'll be near him up there
```

---

## IC-0871: My Friend Never Said Goodbye

- Title: My Friend Never Said Goodbye
- Author (byline): Robert Mauro
- Work: Two Character Plays for Student Actors, Pgs 81-90
- Publisher: Meriwether Publishing
- Publication date as stated: April 1988
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ANNIE, TOMMY
- Teaser before the introduction: Yes
- Spoken words (computed): 1322
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Mauro
Book: Two Character Plays for Student Actors, Pgs 81-90
ISBN: 978-0916260538
Publisher: Meriwether Publishing
Date (Month/Year): April 1988
```

### Introduction (context only: never use it for content warnings)

```text
TOMMY: Many people at some time in their lives think about completing suicide. Most decide to live because they eventually come to realize that the crisis is temporary and death is permanent. On other hand, people having a crisis sometimes perceive their dilemma as inescapable and feel an utter loss of control. The result is death at his or her own hands. There are currently almost 32,000 suicides annually in the U.S. It is estimated that for every suicide there are 6 survivors. Based on this estimate, approximately 5 million American became survivors of suicide in the last 25 years. Annie is a survivor left to deal with the fact that “My Friend Never Said Goodbye” by Robert Mauro.
```

### Performance text (classify this)

```text
ANNIE: (Pg 81-90) (Stands by weeds, then sits on bench) I never thought anything like this could happen. Tommy, I thought you were my friend. Then you do this. (Pause) You didn't give anyone even a hint. You just... did it. (She gets up and walks around.) Maybe if we had had a fight. Maybe if something had been bothering you. (She thinks.) Maybe something was. You were moody - but so was I. (She thinks.) Maybe it was my fault. Maybe it was something I did? Tommy? (She thinks; sit on bench.) Maybe. But it's too late now. You're gone. And I'll never know. (Looks up) Thanks, Tommy. Thanks for not trusting me enough to confide in me. (Pause) Tommy, we used to talk. We used to do everything together. (She tries to smile as she smells the flowers.) Everything. (She smiles and sighs.) It was always Tommy and Annie, never Tommy or Annie. We came as a set. Tommy, what went wrong? Was it me? (She pets the flowers.) This is not fair. You shouldn't have done it! (She is unable to speak.) I'm sorry. But you really know how to hurt a guy. You know? You hurt me. We had so much. We had something special. (She shakes her head.) "Had" is right. It's all gone now, but the memories.

ANNIE: I should have known something was wrong when summer came and you didn't want to go to the lake, our lake, with me anymore. You always liked the lake. We'd spend hours and hours alone out there. . . together. (She sits on bench.) You really hurt me, you know. (There is a long pause.) So what can we do about it now? Huh? Tell me. Can you do that? Is that possible? (She waits.) I guess not. It's gone forever. Boys. Hey, I've been hurt by boys before. You weren't the first. (She covers her mouth.) But you hurt me the most. You never even said goodbye! (She's almost in tears, then controls herself) Not even a last hug. Tommy, this is not right. You can't just do things like that to people who love you. It's not fair. It's not. I wouldn't do that to you. I wouldn't do that to my dog. You shouldn't have done this. (TOMMY enters and sits on the bench beside ANNIE.)

TOMMY: I'm really sorry, Annie. (She doesn't answer.) Annie?

ANNIE: (Totally ignoring TOMMY) It was just not fair, do you hear me?

TOMMY: Annie, it wasn't you. Really.

ANNIE: I'll never know now if it was me. If I hurt you.

TOMMY: Oh, no. Annie, you were the best thing that ever happened to me. You were. Annie?

ANNIE: You used to tell me everything, I thought.

TOMMY: I did tell you everything. At least at first.

ANNIE: (She gets up and walks around, clutching her flowers.) And I always told you everything. There were no secrets between us. None.

TOMMY: I know.

ANNIE: If I was mad, you knew it.

TOMMY: (Smiles) I know.

ANNIE: Maybe I was a grouch at times. . .

TOMMY: Hey. Never.

ANNIE: (To herself) Yes. I was. I know I was. And we'd argue and fight. (She smells the flowers.) But we always made up, Tommy.

TOMMY: We sure did. I'll always remember that. One of my good memories.

ANNIE: So why? Can you tell me?

TOMMY: (Gets up and follows her around, but she doesn't ever look at him. He tries to catch her eye, but can't.) I can tell you this much. . . Annie? Can you hear me? It wasn't you.

ANNIE: I know it was me. It was always me.

TOMMY: (Trying to catch her eye) No. No. It wasn't! I loved you! I always loved you! I'll always love you.

ANNIE: You probably just got tired of my grouchiness.

TOMMY: No. Never. Hey, I was a grouch at times, myself. Remember?

ANNIE: But you were no angel, Tommy.

TOMMY: (Sits on bench) Tell me about it.

ANNIE: (Covers her mouth for a second) Oh, I'm sorry.

TOMMY: Hey. Stop apologizing. I'm not worth it.

ANNIE: See? Even now I hurt you. You never thought much about yourself, and when I called you names you must have really been hurt.

TOMMY: Yeah, I was - but I deserved it, Annie.

ANNIE: You'd always say, "But I deserved it, Annie." (Pause as TOMMY nods) I miss you, Tommy. Do you know that?

TOMMY: I do now. Yes, I do now.

ANNIE: No matter how much we fought or called each other names, I still miss you. And you didn't even say goodbye. People who love each other shouldn't do that.

TOMMY: I know.

ANNIE: You should have told me something was wrong. I'd never have left you. I loved you.

TOMMY: I was going to write a note, but. . . I couldn't think of what to say. What could I say? You know me? I was never much with words.

ANNIE: You were never good with words.

TOMMY: Hey, I could barely spell.

ANNIE: And your spelling. You spelled "Love" (Spelling) LoU-V.

TOMMY: She remembers.

ANNIE: How could I forget that? You were never good with words. You had other ways of showing me you loved me.

TOMMY: Now that is one thing I'll really miss.

ANNIE: Big macho man. You'd die if the guys knew how you used to pick me daisies at the lake and put them in my hair...

TOMMY: Annie, don't... (He's in real pain.)

ANNIE: Who'd buy me silly cards and mail them to me for no reason. . .

TOMMY: Please don't, Annie. . .

ANNIE: For no reason, but because. . .

TOMMY: Don't.

ANNIE: Because you loved me.

TOMMY: (It's as if he's been wounded.) I loved you, Annie! I did. Annie, please don't be sad.

ANNIE: Everyone keeps saying, "Annie, please don't be sad." TOMMY: I'm not worth it, Annie.

ANNIE: "He's not worth it, Annie."

TOMMY: Annie... please... Annie.

ANNIE: Annie, Annie, Annie. What do they know? (She sits beside him on the bench.) What did anyone know? How can they possibly know how I feel? You broke my heart.

TOMMY: Annie, I didn't know.

ANNIE: Tommy...

TOMMY: Yes...

ANNIE: Why did you do this to me, Tommy? Can you tell me?

TOMMY: It had nothing to do with you! Can't you hear me?

ANNIE: I know it was me.

TOMMY: (Screaming in pain) NO! IT WAS NOT YOU!

ANNIE: Yes.

TOMMY: No, no. Can't you understand? It was not you, Annie. I love you.

ANNIE: He never really loved me.

TOMMY: (In real pain) What?

ANNIE: If you loved me, you'd have told me.

TOMMY: I did love you! And it had nothing to do with you. Nothing!

ANNIE: Whatever it was, it had something to do with me.

TOMMY: No.

ANNIE: Yes. I guess we're all partially to blame... That's what everyone says.

TOMMY: No.

ANNIE: I know it's true. I'll never forgive myself.

TOMMY: It's not your fault, Annie.

ANNIE: Yes. It had something to do with me.

TOMMY: No, no, no . . .

ANNIE: It had everything to do with us

TOMMY: How can you say that?

ANNIE: - because we were friends. And friends help each other no matter what it is that is bothering them. That's what friends are for.

TOMMY: Annie, I'm sorry. I should have told you.

ANNIE: Tommy, no matter what it was, I would have understood. You should have told me.

TOMMY: Annie, I'll tell you now. Can you hear me? Annie? Are you listening to me?

ANNIE: We always listened to each other. Always.

TOMMY: Always.

ANNIE: But now it's too late.

TOMMY: No.

ANNIE: Yes. Too late. You're gone forever.

TOMMY: Annie, I'm right here. Beside you. Right on this bench. Can't you see me?

ANNIE: I'll never see you again.

TOMMY: Annie, look! I'm right here!

ANNIE: If I could only feel your arms around me.

TOMMY: (He hugs her, but she feels nothing.) Annie, I love you!

ANNIE: (She shivers.) What was that icy chill?

TOMMY: Chill?

ANNIE: I must be getting a cold. (She stands.)

TOMMY: A chill? From me? I love you.

ANNIE: I'd tell you how much I loved you. But it's too late for that now. I'll never know why you did it, Tommy.

TOMMY: Annie, neither will I!

ANNIE: It was so sudden.

TOMMY: It was a dumb, stupid mistake. I was just so down over so many things. It seemed there was nothing left.

ANNIE: You could have gotten help. Everyone can.

TOMMY: I know that now.

ANNIE: It's too late now. I know you could have worked things out. Even this. Together we could have.

TOMMY: Yes.

ANNIE: I guess for as long as I live, I'll always blame myself for what happened.

TOMMY: Oh, no. Annie, I'll never be able to rest in peace if you think that. Annie, I love you.

ANNIE: I'm sorry if I caused you any pain. And I'm sorry if I can't come to see you anymore. . .

TOMMY: What? No . . .

ANNIE: It's been a year now. A whole new summer is here. It's beautiful. I wish we could enjoy it together. I wish I could be with you, but my doctor says it's not healthy to dwell on the past. So, Tommy, I've come for the last time.. .

TOMMY: Oh, no . . . please, Annie, don't leave me.

ANNIE: I just had to come here one last time. . .

TOMMY: No...

ANNIE: I had to come just one more time just to say goodbye to you... my dear, sweet friend... Tommy. (She stands.)

TOMMY: Annie, no. Don't go. I love you! Don't go!

ANNIE: I have to go. Goodbye, Tommy. (She exits.)

TOMMY: Noooo... Annie, please don't leave me alone. Annie! (Curtain falls as TOMMY puts his head in his hands.)
```

---

## IC-0872: My Life is Proof

- Title: My Life is Proof
- Author (byline): Barbara Lhota and Janet Milstein
- Work: Forensics Series V.2: Duo Practice & Performance
- Publisher: Smith and Kraus
- Publication date as stated: April 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: HARRY, ALICIA
- Teaser before the introduction: No
- Spoken words (computed): 1826
- Already set (do not supply): none

### Source block (context only)

```text
Author: Barbara Lhota and Janet Milstein
Book: Forensics Series V.2: Duo Practice & Performance
ISBN: 978-1575253091
Publisher: Smith and Kraus
Date (Month/Year): April 2003
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Incest is generally only brought up in “polite company” after watching Cersi and Jamie Lannister on Game of Thrones,

ACTRESS: But the fact is that some little girls face a very different reality.

ACTOR: According to the Journal of Adolescent Health, 1 in 9 girls are sexually abused before they’re 18 years old; and in over 80% of those cases, by a relative.

ACTRESS: In this scene, Alicia has taken an extremely brave step and is suing her grandfather for sexual, emotional, and physical abuse.

ACTOR: Harry, her attorney; however, makes the case for settling out of court.

TOGETHER: My Life is Proof by Barbara Lhota and Janet Milstein
```

### Performance text (classify this)

```text
HARRY: Alicia, please calm down. Look, I am not the enemy, all right? I'm here to help you. Forty thousand dollars is a lot of money.

ALICIA: Not when we're suing him for over a million. But that's not the point, Harry. He's not admitting he's guilty. He'll just say that his poor granddaughter is deranged. He's just a loving grandfather, helping her out by covering some of her psychiatric expenses.

HARRY: Alicia, first of all, perpetrators like your grandfather almost never admit their crimes. I've been doing these kinds of cases for eight years and in all that time maybe three have come clean.

ALICIA: Well that's not good enough. That's why I want to go to court.

HARRY: Secondly, for someone who is not a millionaire, forty thousand dollars is a lot of money to just be "helping out."

ALICIA: My mom got breast cancer and he gave her like thirty thousand dollars. To help with her medical expenses.

HARRY: I'm sorry to hear that. (Beat.) Alicia, just because he gave your mother money doesn't mean . . . cancer is a very serious life-threatening disease.

ALICIA: So is incest! A lot of people die from abuse, ya know!

HARRY: I didn't mean to belittle what happened to you. If anything I've said seemed to indicate that I didn't think what you suffered was traumatic, I apologize. I care. Very much. However, as I've told you before, this is never easy. It's messy, it's ugly, it's exhausting. Most lawyers won't even touch these types of cases. Because they know, in court, they'll lose.

ALICIA: Why? How can you be so sure?

HARRY: We have to prove your grandfather is guilty beyond a reasonable doubt. That would be hard enough to do if it happened yesterday and you had wounds and bruises. To prove he was the one who did it. But now, years later, it makes witnesses and physical evidence -- all of it -- that much harder.

ALICIA: Exactly. Harder, not impossible.

HARRY: Alicia, the chances of winning a case like this in court are ...

ALICIA: Then why did you take it in the first place?

HARRY: I didn't want to take it to be honest with you. The last sexual abuse case I had practically put me out of business. You do realize I have to front all of the expenses myself.

ALICIA: And I repeat, then why did you take it?

HARRY: Because nobody else would.

ALICIA: You know what I think? I think you chickened out, Harry. The new lawyer. The "hotshot." He moved it from state to federal court and you got scared. Suddenly, you're in the big league -- and you caved.

HARRY: I didn't cave. He also made me an offer that day, and I wanted to counter it.

ALICIA: The day you called me and told me about the federal court thing. That was the same day you asked me how much my expenses were, without any money for emotional duress. But initially when we talked, you were the one who added one million dollars for emotional duress.

HARRY: You think one million dollars is too much for what you've suffered?

ALICIA: No. There is no amount that could ever make up for what he did to me. My point is, you were confident enough to up my figure 600 percent. And you meet with this lawyer and he says "federal court" and you drop down to 45 percent. Admit it, you're scared.

HARRY: Not in the way you think. I told you day one that 99 percent of these cases settle out of court. If this went to court, I would be scared that, one, it would be detrimental to your well-being, and two, that you'd come away with no money at all.

ALICIA: Or that you'd come away with no money.

HARRY: That's ridiculous. Let me tell you something, Alicia. On my last two cases, I worked my tail off doing research, finding records, footing the bill to have witnesses flown in for testimonials. And you know what happened? We lost. I lost. Both defendants made offers to settle, but we hung tough. In the end it wasn't me I was concerned about. But those women . . .They couldn't afford the treatment they needed. I should have just given them the money I spent on their cases. Because we all wound up worse than when we started. I'm not caving. I'm just trying to be realistic.

ALICIA: I'm sorry.

HARRY: So am I. (Pause.) You're a tough cookie-and smart. You should have gone to law school.

ALICIA: My dad would have loved that. He lost it when I told him I was going to be an actor. "Ninety-nine percent of actors are unemployed. You'll wind up in the streets."

HARRY: Alicia, I really think you should take the money. Pay your bills, get the counseling you need.

ALICIA: I can't do it. I want to go to court.

HARRY: We'll get creamed. We have no proof.

ALICIA: My life is proof! I want him to admit what he's done!

HARRY: Someone who can rape his own granddaughter is certainly capable of lying under oath.

ALICIA: So the jury can find him guilty. He can't just do what he's done and have it be okay! Don't you get it? I need to stand up for myself! And for everyone else who this has happened to who can't stand up. I need to show him that I'm taking my life back! You can't imagine how many times and ways I've gone over confronting him. Making him admit it, torturing him the way he tortured me. I locked myself in the closet one day because I was afraid I would go buy a gun and kill him. I was in the hospital on his birthday because I wanted to kill myself. And where was he? Kicking up his heels in his cushy house in Florida celebrating. That is not justice. There is no justice!

HARRY: You're right. Our system is faulty. But it's the best we've got. It shouldn't be called the Justice System. It should be called the "trying-to-do-justice-system."

ALICIA: Then try with me for God's sake.

HARRY: You just said you were suicidal. That lawyer will kill you, Alicia. He's a shark.

ALICIA: I'm not afraid of him!! It can't be any worse than what I've already lived through!

HARRY: Fine. You think you can take it? Okay-okay! (Moving with a new energy that we have not seen.) I'm him. You're in the witness stand. Everybody's watching. Your mom, your sisters, and your grandfather.

ALICIA: I'm ready.

HARRY: So Alicia, you say that your grandfather forced you to have intercourse with him, is that right?

ALICIA: Yes.

HARRY: Umm-hmm. And you were how old?

ALICIA: Four to six years old.

HARRY: You don't know how old you were?

ALICIA: I meant it happened from the time I was four to the time I was six.

HARRY: How old are you now?

ALICIA: Twenty-four.

HARRY: Well, you must have an amazing memory.

ALICIA: It's hard to forget something like that.

HARRY: You're not allowed to speak unless I ask you a question. Now, you also claim that your two sisters were with you on certain occurrences of this supposed abuse. And you claim they were abused by your grandfather as well?

ALICIA: Yes, that's right.

HARRY: The court has heard both of their testimonies and they don't seem to remember any-

ALICIA: Because they're too scared to remember. Their bodies won't let them until they're able to handle it.

HARRY: I see. So you can "handle it.” Can you please tell the court what you do for a living?

ALICIA: I'm finishing up graduate school. I'm working on an internship.

HARRY: In what? What are you studying?

ALICIA: Theater.

HARRY: And what do you do in the theater, specifically? Do you make costumes? Sets?

ALICIA: I'm an actor.

HARRY: You're an actor! So you make things up for a living?

ALICIA: No. The playwrights make it up. We just help tell the story.

HARRY: I see. But you pretend a lot. Pretend to be someone you're not, to act as if things happened when they didn't. . . So you claim your grandfather sexually abused you in his former house in Brooklyn and in your parents' former house in New Jersey. Something strikes me as odd. Your parents both testified that they weren't aware of any abuse. Yet you say it happened in their house. How would you explain this?

ALICIA: I don't know.

HARRY: You don't know? Uh-huh. Tell me, Alicia, people in the theater like you. Do you make a lot of money?

ALICIA: No, I don't.

HARRY: Do you have a lot of bills? Student loans? How much would that be in student loans?

ALICIA: I don't know exactly. Maybe twenty-three thousand.

HARRY: Twenty-three thousand dollars? And then you have your living expenses and your car and unforeseen emergencies and you don't make much money as an actor. That must be rough on you. Scraping by with bills piling up. Wouldn't it be nice to have those bills paid off so you can be free to do your acting?

ALICIA: Lots of people have student loans. It's common these days.

HARRY: Answer the question. Wouldn't it be nice?

ALICIA: Yes.

HARRY: Would you say your grandfather has a lot of money?

ALICIA: Yes.

HARRY: So let's review here, your grandfather has a lot of money. You're at least twenty thousand dollars in debt and not making much at all working as an actor. You claim that your grandfather sexually, physically, and emotionally abused you and your two sisters. They don't recall any abuse. You say the abuse happened in the homes of your grandfather and your parents, but you don't know where your parents were while it was supposedly happening. Your father stated that he did not know of any abuse. Your mother said the same thing. You agreed that it would be nice to have your bills paid off. It's a lot of debt. And in your daily work, you pretend that things happened to you that didn't actually really take place at all. Would you agree with all of that?

ALICIA: (Beat.) Yes. [But] not what you're insinuating.

HARRY: Of course you would because you made all of this up, didn't you, Alicia?

ALICIA: No!

HARRY: You've been diagnosed with major depression on several occasions, have you not?

ALICIA: Yes, and post traumatic-

HARRY: You've been in more than one hospital because you overdosed on medication. Is that correct? You're not exactly a stable human being are you?

ALICIA: If I'm not, it's because-

HARRY: Answer the question!!

ALICIA: No.

HARRY: Your grandfather never laid a hand on you! Did he?!

ALICIA: Yes!!

HARRY: He never fondled you, he never raped you, he never did those sick, demented things that you're accusing him of!! Did he?!

ALICIA: Yes!!

HARRY: You are under oath, Alicia! You're depressed and unstable and broke and you want to blame someone for your life and make them pay for it and you picked him! Didn't you?!

ALICIA: (She suddenly curls inward, protecting herself. Her eyes are filled with terror and she looks like a little girl. Her speech is broken, like she's somewhere else. She makes a fearful, whining sound.) Go away. Get away from me. (She breathes heavily through her mouth and watches him with hyper-paranoia.)

HARRY: (Dropping the character.) Alicia?

ALICIA: Stay away from me. You stay over there. (She jumps at a tiny sound.) I'm not bad. Uhh. (She lightly touches her forehead with apprehension.) You're gonna hurt me.

HARRY: No, no. Alicia? You're safe now. It's me, Harry. You're in my office. It's safe here. (He moves toward her but she recoils.) I'm sorry. I'm sorry. Can you hear me? (She still looks terrified but she's silent now and she nods yes.) It's okay. It's all going to be okay. (She stares at him and starts to rock.)

LIGHTS OUT
```

---

## IC-0873: Naomi in the Living Room

- Title: Naomi in the Living Room
- Author (byline): Christopher Durang
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SUGGESTED ROLES, NAOMI, JOHN, JOHNNA
- Teaser before the introduction: Yes
- Spoken words (computed): 1701
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christopher Durang
ISBN: 978-0822214489
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Sometimes one of the most difficult things about being married is not the marriage itself, but the in-laws that come with it.

ACTRESS: If you have been having a hard time dealing with your mother-in-law, you haven’t seen anything yet.

ACTOR: Meet Naomi . . . Joanna’s mother-in-law. One moment she’s nice as pie, the next she’s jumping on top of furniture, pulling out her hair, and screaming at the top of her lungs.

ACTRESS: Poor Johnna finds herself trapped in the absolute craziness of the family she married into during a visit with. . .

TOGETHER: Naomi in the Living Room by Christopher Durang

SCENE: A living room. Enter NAOMI, followed by JOHN and JOHNNA, an attractive young couple. JOHN has a moustache and is dressed in a suit and tie. JOHNNA is wearing a dress with a string of pearls. NAOMI, though, looks odd. NAOMI plants herself somewhere definitive - by the mantelpiece, for instance - and gestures out toward the room.
```

### Performance text (classify this)

```text
SUGGESTED ROLES: Actor: John and Johanna Actress: Naomi

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NAOMI: And this is the living room. And you've seen the dining room, and the bedroom, and the bathroom.

JOHN: Yes, I know. I used to live here.

NAOMI: The dining room is where we dine. The bedroom is where we go to bed. The bathroom is where we take a bath. The kitchen is where we ... cook. That doesn't sound right. The kitchen is where we ... collect kitsch. Hummel figurines, Statue of Liberty salt and pepper shakers, underpants that say Home of the Whopper, and so on. Kitsch. The kitchen is where we look at kitsch. The laundry room is where we do laundry. And the living room is where Hubert and I do all of our living. Our major living. So that's the living room.

JOHNNA: What do you use the cellar for?

NAOMI: [suspicious] What?

JOHNNA: What do you use the cellar for?

NAOMI: We use the cellar to . . . we go to the cellar to . . . replenish our cells. We go to the attic to . . . practice our tics, our facial tics. [face contorts] And we go to the carport, to port the car. Whew! Please don't ask me any more questions, I'm afraid I may not have the strength to find the answers. [laughs] Please, sit down, don't let my manner make you uncomfortable. Sit on one of the sitting devices, we use them for sitting in the living room. [JOHN and JOHNNA go to sit on the couch]

NAOMI: [screams] DON'T SIT THERE, I WANT TO SIT THERE!!! [JOHN and JOHNNA look frightened. NAOMI charges to the couch] Shits! Ingrates! It's my house, it's my living room. I didn't ask you, I can ask you to leave. [JOHN and JOHNNA start to edge out of the room] No, no, sit down. Please, make yourselves at home, this is the living room, it's where Rupert and I do all our living. [JOHNNA sits in the chair, and JOHN stands behind her --NAOMI stretches her arms out on the couch] Wow. Boy oh boy. I need a big couch to sit on because I'M A BIG PERSONALITY!!!! [laughs] Tell me, are you two ever going to speak, or do I just have to go on and on by myself, or WHAT!!!!!! [stares at them intensely; they hesitate but then speak]

JOHNNA: This is a very comfortable chair. I love it.

NAOMI: Go on.

JOHNNA: Ummmm, this morning I washed my hair, and then I dryed it. And we had coffee in the kitchen. [pause, doesn't know what to say] And I love sitting in this chair.

NAOMI: I think I want to sit in it, get up, get up. [charges over, JOHN and JOHNNA move away, uncomfortable. NAOMI sits and moves around in the chair, luxuriating in it] Hmmmm, yes. Chair, chair. Chair in the living room. Hmmm, yes. [shouts at them] Well, go sit down on the couch, you morons! [screams off-stage] Leonard! Oh, Leonard! Come on in here in the living room and have some conversation with us. You don't want me to soak up everything our son says all by myself, do you? [stands and walks over to the couch. Smiles at JOHNNA] You probably didn't know John was Herbert's and my son, did you?

JOHNNA: Yes, he told me. I've met you before, you know.

NAOMI: Shut up! [calls out] Hubert! Rupert! Leonard! [to them] I hope he's not dead. I wouldn't know what room to put him in. We don't have a dead room. [smiles; screams] AAAAAAA- AAAAHHH! [looks at them] Goodness, my moods switch quickly. Tell me all about yourselves, do you have children? [listens attentively]

JOHNNA: We had five children, but they all died in a car accident. The babysitter was taking them for a ride, and she was drunk. We were very upset.

NAOMI: Uh huh. Do you like sitting on the couch?

JOHN: Mother, Johnna was telling you something sad.

NAOMI: Was she? I'm sorry, Johnna, tell it to me again.

JOHNNA: We had five children . . .

NAOMI: [Tries to concentrate, but] Wait a minute, something's bothering me!!!! [rushes over to a stuffed Santa pig on the mantel, snatches it up and throws it against the wall in a fury] This belongs in the kitchen, not in the living room. The living room is for living, it is not meant for sincerely designed but ludicrously corny artifacts! Kitsch! Do you like Hummel figurines?

JOHN: Very much. Now that the children are dead, Johnna and I have begun to collect Hummel figurines.

NAOMI: Uh, huh, isn't that interesting? Excuse me if I fall asleep. I'm not tired yet, but I just want to apologize in advance in case your boring talk puts me to sleep. I don't want to offend you. [screams] AAAAAAAAAAAAHHHHHHHH! I'm so bored I could scream. Did you ever hear that expression? AAAAAAAAAAAAHHHHHHHH!

JOHN: Excuse me, I want to change my clothes. I'm tired of my color scheme. I'll be right back. [exits]

JOHNNA: He's constantly talking about his color scheme. It's my cross to bear, I guess. That and the death of the children.

NAOMI: So who are you, anyway?

JOHNNA: I'm Johnna. I'm married to your son. All our children recently were killed.

NAOMI: Stop talking about your children, I heard you the first time. God, some people can't get over their own little personal tragedies, what a great big crashing boor. Lots of people have it worse, girlie! [calls off-stage] Hey, John, where did you get this turd of a wife, at the Salvation Army? I'd bring her back! [laughs maniacally]

JOHNNA: I think I want to go.

NAOMI: Boy, you can't take criticism, can you? This is the conversation pit. You can't leave the pit until you converse on at least five subjects with me. Starting now, go: [waits expectantly]

JOHNNA: I was reading about Dan Quayle's [Replace with current VP] grandmother the other day.

NAOMI: That's one. Go on.

JOHNNA: She said there should be prayer in the schools ...

NAOMI: That's two. [starts to massage her feet]

JOHNNA: And that we should have a strong defense ...

NAOMI: That's three.

JOHNNA: And that the Supreme Court should [was right to] repeal the Wade vs. Roe ruling that legalized abortions.

NAOMI: That's four.

JOHNNA: And that even in the case of pregnancy from incest, the woman should be forced to carry the child through to term.

NAOMI: That's four-A

JOHNNA: And then she said she hoped the mother would be forced to suffer and slave over a horrible job and take home a tiny teeny paycheck to pay for some hovel somewhere, and live in squalor with the teeny tiny baby, and that then she hoped she'd be sorry she ever had sexual intercourse.

NAOMI: That's still four-A.

JOHNNA: Don't you think she's lacking in Christian charity?

NAOMI: That's five, kind of. Yes, I do. But then so few people are true Christians anymore. I know I'm not. I'm psychotic. Get up off the couch, I want to sit there. [rushes over, JOHANNA has to vacate fast. NAOMI starts to luxuriate in sitting in the couch, moving sensuously] Oh, couch, couch, big couch in the living room, you are my manifest destiny. Mmmmm, yes, yes.

[to JOHNNA] Tell me, can you switch moods like I can? Go ahead, try.

JOHNNA: Very well. [happy] I'm so happy, I'm so happy. [screams] AAAAAAAH! Do you have chocolates for me? [desperate] I'm so sad, I'm so sad. Drop dead! [laughs hysterically] Aha-hahahahahahaha! That's a good one!

NAOMI: Very phoney, I didn't believe you for a moment. [changes subject abruptly] I don't understand politics, do you?

JOHNNA: Politics?

NAOMI: Politics, politics! What, are you deaf? Are you stupid? [Enter JOHN dressed just like JOHNNA - the same dress, pearls, stockings, shoes. He has shaved off his moustache, and he wears a wig with a bow in it like the one she has in her hair. They look very similar]

NAOMI: You took off your moustache.

JOHN: I just feel so much better this way.

JOHNNA: [embarrassed] John and I are in couples therapy because of this. Dr. Cucharacha says his cross-dressing is an intense kind of co-dependence.

NAOMI: If this Dr. Cucharacha cross-dresses, I wouldn't see him. That's what John here is doing. Too many men in women's clothing, nothing gets done!

JOHNNA: Why do you humiliate me so this way?

JOHN: [to Johnna] I want to be just like you. Say something so I can copy you.

JOHNNA: Oh, John. [looks away with a feminine gesture]

JOHN: Oh, John. [imitates her gesture] That doesn't give me much. Say something else.

JOHNNA: Maybe it's in your genes.

JOHN: Maybe it's in your genes.

NAOMI: This is a disgusting sight. I find this uncomfortable. Makes me want to vomit.

JOHNNA: Maybe we should go.

JOHN: Maybe we should go.

NAOMI: [upset] How come you don't dress like me? How come you dress like her?

JOHN: I want to be noticed, but I don't want to be considered insane.

JOHNNA: John, please, just stay quiet and pose if you must, but no more talking.

NAOMI: Insane? Is he referring to someone in this room as insane? [calls] Sally! Gretchen! Marsha! Felicity! [to them] I'm calling my army in here, and then we'll have some dead bodies.

JOHNNA: Maybe we should go.

JOHN: Maybe we should go. [keeps imitating JOHNNA's movement]

JOHNNA: Will you stop that?

NAOMI: Insane, I'll give you insane! What's the capital of Madagascar? You don't know, do you? Now who's insane? What's the square root of 347? You don't know, do you? Well, get out of here, if you think I'm so crazy. If you want to dress like her and not like me, I don't want you here. [JOHN begins to walk back and forth around the room, pretending he's on a fashion runway. JOHNNA covers her eyes] I can have Christmas by myself, I can wait for Santa by myself. I can bob for apples. By myself! Do you get it? You're dead meat with me, both of you. Leave here. I don't need you, and you're dead! [pause]

JOHNNA: Well, I guess we should be going.

JOHN: Well, I guess we should be going. [JOHNNA and JOHN, looking the same and walking the same, leave the house. NAOMI chases them to the door]

NAOMI: *Nuts to* you and the horse you came in on! [JOHN and JOHNNA exit. NAOMI comes back into the room and lets out enormous, heartfelt sobs. When they subside, she seems to be fairly content] Well, that was a nice visit.
```

---

## IC-0874: Next

- Title: Next
- Author (byline): Terrance McNally
- Work: Terrence McNally 15 Short Plays, Pgs 61-82
- Publisher: Smith and Kraus Pub Inc
- Publication date as stated: June 1994
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SGT. THECH, MARION
- Teaser before the introduction: Yes
- Spoken words (computed): 1523
- Already set (do not supply): none

### Source block (context only)

```text
Author: Terrence McNally
Book: Terrence McNally 15 Short Plays, Pgs 61-82
ISBN: 978-1880399347
Publisher: Smith and Kraus Pub Inc
Date (Month/Year): June 1994
```

### Introduction (context only: never use it for content warnings)

```text
Next by Terrance McNally
```

### Performance text (classify this)

```text
The scene opens in an examination room. Stage left there is an examination table, a scale and a cabinet filled with medical equipment. Stage right there is a desk and two chairs. The only bright color in the room is the American Flag, center stage. As the curtain rises, the room is empty.

SGT. THECH: (Pg 61-82) (Off stage) Next! (Marion Cheever

MARION: (enters. He is a fat man in his late carrying a briefcase) Hello? I'm next! Well! I think we can get this over with rather quickly.

SGT. THECH: (busy at her desk.) Your card and bottle, please.

MARION: (rummaging in briefcase) As I was starting to say, I think we can get this over with rather quickly. There's obviously been a mistake. (laughs) I mean I-

SGT. THECH: The government does not make mistakes. If your country has called you, it has its reasons. May I have your card and bottle, please? Is your name Marion Cheever?

MARION: Yes, it is. But you know I just had a fortieth birthday.

SGT. THECH: They're taking older men -- inching up all the time. Remove all articles of clothing including your shoes and socks.

MARION: Who are you?

SGT. THECH: Your examining officer, Sgt. Thech. And by the authority vested in me by this government, l order you to strip.

MARION: A lady examining officer! Oh that's funny! They must be pretty hard up these days.

SGT. THECH: And if you have not begun to strip in the next ten seconds I will complete these forms without further examination and report you to the board of examiners as fit for duty.

MARION: (as if coming out of a trance) Oh my God, I'm sorry. I don't know what I was thinking. What did you say?

SGT. THECH: You have ten seconds. (timing him) 1, one thousand; 2, one-thousand (Marion strips)

SGT. THECH: Age.

MARION: Forty . . . eight! I'm forty-eight years old.

SGT. THECH: Your occupation, Mr. Cheever.

MARION: I'm a dancer.

SGT. THECH: Toe or tap.

MARION: Oh really! Toe or tap! I'm the assistant manager of the Fine Arts Theatre, 58th Street and Park Avenue. You've probably heard of us. Toe or tap! I was funning!

SGT. THECH: Rheumatic fever.

MARION: (blinking hard) Unh! Did I have rheumatic fever? No, no I don't think so.

SGT. THECH: Mumps.

MARION: (jumping at this) Yes! Yes, yes, yes! I was in bed for months -- practically had last rites!

SGT. THECH: Venereal disease.

MARION: Not yet! I wish you'd let me tell you about my mumps!

SGT. THECH: Do you drink.

MARION: Whenever I smoke. Smoking makes me drink and drinking makes me smoke. It's a vicious circle.

SGT. THECH: All right, Mr. Cheever, on the scale now, please. (turns and sees him draped in the flag) Drop that flag.

MARION: I was just admiring it! I have one just like it at home. (Sgt. Thech returns the flag to its proper place. Marion walks along, unwilling to give up its protection) Could I have a little robe or something? (Sgt. Thech hands him a sheet) Thank you. Thank you.

SGT. THECH: On the scale.

MARION: (wrapping the sheet around himself) I'll refuse to go, you know. You're just wasting your time. (under his breath) I hate this whole day! It's humiliating, that's what it is. Calling a man in here and . . .

SGT. THECH: (listening to his chest with a stethoscope) Breath. In, out. In, out.

MARION: (Marion is very ticklish) Don't do that! (laughs)

SGT. THECH: Unh-hunh!

MARION: What did that mean? "Unh-hunh?" You heard something you didn't like?

SGT. THECH: Open. (sticks a tongue depressor down his throat and checks his eyes and ears with a light)

MARION: I hate this. I hate it a lot. (beat) When you were examining my heart, did you hear something I should know about? It wasn't very subtle, going "unh-hunh" like that. It's my ticker, so if there's anything wrong I'd like to know about it. (Sgt. Tbecb crosses the room, turns to face him and speaks very softly. We just see her lips moving) What? What did you say?

SGT. THECH: Your hearing is perfect.

MARION: Now just a minute. I will not be railroaded.

SGT. THECH: (holding up an eye chart) Read this chart -- third line.

MARION: (running all the letters together) TOZDY!

SGT. THECH: The second line.

MARION: The second line's a little fuzzy.

SGT. THECH: Try the top line. Mr. Cheever.

MARION: (with much squinting) The top line's a real problem. Let's see -- it's a . . . Z!

SGT. THECH: Excellent.

MARION: Now just a minute. It's an E. I said it was a Z. I failed that test. You give me credit for failing!

SGT. THECH: Failure is relative in any case, private.

MARION: Private? You've got me inducted when I haven't even been given a full opportunity to fail yet?

SGT. THECH: This is your opportunity, Mr. Cheever, don't pass it up. (takes his blood pressure)

MARION: I've heard of shanghaiing but this little episode is out and out kidnapping. I simply won't go. You can't just take a man out of civilian life and plop him into the army. So there's a war on, I didn't start it. I'm on the verge of my big break. I've stood in the back of that lousy theatre for eleven years and they are going to promote me next winter. I am going to be the manager, thank you. Unh-hunh, sergeant, I'm not going into any army, war or peace!

SGT. THECH: (makes ready to take a blood sample) Close your eyes and count to ten slowly and then touch the tip of your nose with your left index finger.

MARION: Oh, all right, that sounds easy. One, two, three, four . . . five, six (suddenly panicked) Wait! Wait, wait, wait! I saw it. (Sgt. Thech is holding a syringe) I hate needles. I'm not afraid of them, I just don't like them. (Sgt. Thech draws blood) Oh my God! I'm going to have a heart attack. (Sgt. Thech finishes) I'm bleeding. Look at this, I'm bleeding.

SGT. THECH: All right, Mr. Cheever, you can get dressed now. Your physical examination is over.

MARION: Oh. It's over? Well, that wasn't so bad. How did I do? Am I 4-F?

SGT. THECH: I found no evidence of physical abnormality.

MARION: (aghast) You found no evidence of physical abnormality? Now wait a minute. What about my blood pressure? I want more testing. I'm not leaving until I get a better verdict. What about my sinus condition? Did you know I had one? Of course not, you didn't look up my nose. What kind of examination is it without looking up a person's nose? A lot of things could be wrong up there. I can't breathe seven months out of the year. Write that down. And what about my eye test? I know I failed my eye test!

SGT. THECH: (busy at her desk) If you won't cooperate, I judge you on the basis of objective evidence. You do not squint, you're not wearing glasses and you saw my lips moving at fifteen feet away. You'd have to be a lot smarter and better rehearsed than you are to fool an examining officer.

MARION: (triumphant) Then what about my feet? You didn't even make me take my socks off. (takes off socks) Here. Now look at this. They're flat. See how flat they are? Do you see any arch? And see, see all those corns? I was born with all these corns. Ask yourself, is that normal?

(Sgt. Thech continues working at desk) (shows her his teeth) And my teeth! They're full of decay. My gums are very spongy. (desperately) And you haven't asked me one single question about my mind. For all you know I could be a raving lunatic.

SGT. THECH: (shrugs and administers the psychological/intelligence tests) I have twelve apples.

MARION: (thrown) You have what?

SGT. THECH: You have twelve apples. Together we have . . .

MARION: (involuntarily) Twenty-four apples. (realizes what he's done and groans)

SGT. THECH: Who was the first President of the United States?

MARION: George Washington. Was that right?

SGT. THECH: Who were the allies of the United States in the Second World War?

MARION: The good people.

SGT. THECH: Who were its enemies?

MARION: No one. We had no enemies.

SGT. THECH: Who are the allies of the United States now?

MARION: Just about everyone.

SGT. THECH: Who are its enemies?

MARION: Who can tell?

SGT. THECH: Name three of the twelve Apostles.

MARION: Joseph, his brother and his sister!

SGT. THECH: If you were seated in a theatre and saw a fire break out before the rest of the audience noticed it -- what would you do?

MARION: As a theatre manager I know this. The main thing is I wouldn't want to start a panic. So I'd very quietly leave and go home.

SGT. THECH: What is the similarity between a chair and a couch?

MARION: A chair and a couch? You can sit on them.

SGT. THECH: A rabbit and a squirrel.

MARION: (reasonably) You could sit on a rabbit and a squirrel. The rabbit might even like it.

SGT. THECH: Have you ever suffered from night terrors? Insomnia?

MARION: Of course, insomnia! Because of the night terrors.

SGT. THECH: Have you ever indulged in homosexual activities.

MARION: They have been very good to me.

SGT. THECH: When did you stop?

MARION: Who said anything about stopping?

SGT. THECH: Did you have a normal relationship with your father?

MARION: After we stopped dating the same girl, everything was fine.

SGT. THECH: Do you have any history of bedwetting?

MARION: Even my top sheet is rubber.

SGT. THECH: (abruptly) All right, Mr. Cheever, the examination is over.

MARION: Well? How did I do? Am I 4-F yet?

SGT. THECH: You'll get your classification in the mail. I don't think you have anything to worry about. I doubt if they would find someone like you acceptable. You may go now. I'm through with you. (turns her back to him and begins typing up his test results)

MARION: (dressing) Now you're through with me and would like me to go. You have taken my time, you have taken my blood, you have taken my urine, you have taken my secrets and now you would like me out of here? Well I'm not going. If I go I take all of me. I'd like my blood and my urine back! I mean I'm 4-F -- you can't have any use for them. (Sgt. Tbecb types) I demand an apology! I have given everything to everyone and now I want something back!

You know what the ushers at the theatre call me behind my back? Fatso. Yeah! Because that is exactly what I am. A fatso. (bangs on Sgt. Thech's desk with his fist) How dare you call me in here, examine me, ignore me, dismiss me and tell me I'm not acceptable. You are not accept-able! Stop it! And listen to me! I said stop! (puts his hands over the typewriter keys) Good. Very good! (describes everything Sgt. Thech does while she is doing it-- as if he were giving her the orders) That's right. Fold the paper. Open the drawer. Put it away. Close it. Now you're doing exactly what you're told. Get up. Fold the sheet. Check the instruments. Excellent. Now out you go. Close the door. There! (Sgt. Tbecb has left the room, closing the door behind her)

SGT. THECH: NEXT!
```

---

## IC-0875: Night Vision

- Title: Night Vision
- Author (byline): Dominique Morisseau
- Work: Facing Our Truth
- Publisher: Samuel French, Inc.
- Publication date as stated: 2015
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: AYANNA, EZRA
- Teaser before the introduction: Yes
- Spoken words (computed): 1264
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dominique Morisseau
Book: Facing Our Truth
ISBN: 978-0573704260
Publisher: Samuel French, Inc.
Date (Month/Year): 2015
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Stereotypes are the belief that most members of a group have the same characteristics.

ACTRESS: For example, ALL white women are “Karens”

ACTOR: Or ALL police officers like donuts.

ACTRESS: Or ALL black men are criminals. Ultimately these stereotypes dehumanize the individual and lead to actions and reactions based on these biased beliefs.

ACTOR: Now none of us want to admit to being biased . . . not externally anyway.

ACTRESS: But biases do exist. Call them internal, implicit or unconscious . . . even people who strive not to be are biased.

ACTOR: No matter how diligently we aspire not to judge others "by the color of their skin, but by the content of their character," we struggle to attain this ideal.

ACTRESS: Ok, Ok . . . I can admit, “Karen’s” are funny, and donut-loving police officers are harmless, but I can’t be biased against black people. (beat) I’m black.

TOGETHER: Night Vision by Dominique Morisseau
```

### Performance text (classify this)

```text
NOTE: To be performed by 2 black actors

(Lights up on the living room of a Brooklyn apartment. Somewhere, importantly: a black hooded sweatshirt. AYANNA, pregnant, enters with her husband EZRA)

AYANNA: (Pg 15-21) I cannot believe that. I'm still shaking.

EZRA: Sit down baby.

AYANNA: I don't want to sit down. I want to find him and kick his ass. I want to – Aren't you upset?

EZRA: I'm a lot of things.

AYANNA: I'm hurt. I'm angry. I'm disgusted. I have to pee. I want to find him and kick his ass.

EZRA: You're not going back out there, baby.

AYANNA: Then you should go out there.

EZRA: I should go back out there??? You want me to go out there and kick his ass?

AYANNA: Maybe.

EZRA: What if he has a gun? (Beat)

AYANNA: It was like . . . was he punching on her?

EZRA: I couldn't really see. Could you?

AYANNA: Not completely.

EZRA: Me neither. (A moment) I should've kicked his ass. I hesitated.

AYANNA: I'm calling the police.

EZRA: Yeah?

AYANNA: What else can I do?

EZRA: You? Nothing. Me? I can go find him.

AYANNA: No. You're not a vigilante. I don't want you hunting anyone. What if you become the prey?

EZRA: Then call the cops.

AYANNA: I'm calling the cops. (AYANNA pulls out her cell. EZRA peers out of the window)

EZRA: (almost to himself) It's the darkness out there. You could get swallowed by it. Damn busted streetlight. Been half a year and they haven't fixed it.

AYANNA: (into the phone) Hi, yes, I want to report a situation I just witnessed. A man was beating his girlfriend. She was screaming and he - Yes. Yes, I'm sure he was beating her. I'm sure. And she was screaming and then he took off and ran down the block - Yes. Yes, okay. He was a ... he was wearing a hooded sweatshirt. It was covering his face, but I think it was red. Yes. And his pants were dipped low . . . um . . . below his waist. He had on sneakers. He took off running toward Marcy and Green. You could still catch him if you hurry. He was a ... young . . . Black -

EZRA: Wait, baby - hold on now. Are you sure???

AYANNA: (cupping the phone) What? (into the phone) Yes, I'm still here. Give me a sec.

EZRA: He was Black?

AYANNA: Yes, I'm sure. My memory is ... I'm sure.

EZRA: Are you??? Cuz I'm not. l thought the sweatshirt was green.

AYANNA: It was red.

EZRA: Are you sure?

AYANNA: Yes! I'm - shit, I'm sure! (into the phone) Yes, he ran on foot. We screamed and he ran on foot. My husband yelled. Scared him off. She um, the girl ran too. Into a home. Yes, sure. Okay. Thank you. Uh, no." Anonymous please. Yes. No problem. (AYANNA hangs up. She looks at EZRA) You trying to freak me out?

EZRA: I don't remember red.

AYANNA: Ezra, are you kidding me? The sweatshirt was . . .

EZRA: . . . green, Ayanna. It was green.

AYANNA: Was it? No. That's not right. How could that be right? The streetlight near him wasn't even working. He was in the shadows. I remember red because when he ran, he fell into some headlights for a second. I remember thinking he looked like the devil.

EZRA: I remember green. I remember thinking when he fell into that pool of light that he looked pale underneath all that green. That's what I remember thinking.

AYANNA: Could hardly see his face. It was too dark.

EZRA: Then how did you know he was Black?

AYANNA: I... (A moment) What's happening right now? I called the cops. Was I not supposed to call the cops?

EZRA: No. You can call the cops. You did. You called the cops.

AYANNA: So then what's with the - I mean, why are you doubting me?

EZRA: I'm not doubting you, baby. I'm questioning you. Big difference.

AYANNA: But what in the - what for?

EZRA: Because you aren't sure. For this you have to be. It costs too much to be wrong.

AYANNA: No, I was sure. I was sure. I felt sure.

EZRA: But you aren't. (Beat)

AYANNA: I can't sit still. I'm going to shake myself into oblivion.

EZRA: Sit down. You're upset. You're moving too much. Just sit down.

AYANNA: Hypothyroidism. It's a risk. All my books say so. Not good for the baby. (shift) I'm all confused now.

EZRA: You're not helping anything right now, Ayanna.

AYANNA: I'm not helping? I tried to help. You told me I was wrong.

EZRA: I didn't-- I didn't say you were wrong. I just asked if you were sure.

AYANNA: Dammit Ezra! How am I supposed to be sure??? It's dark.

EZRA: It's nighttime. It's supposed to be dark. Now a brother is a hazard if he walks around at night? Should we carry a label? Caution. Objects appear darker than they really are.

AYANNA: I don't know. Someone was beating a woman. Someone was beating on a woman!!! What am I supposed to do? What if that wasn't his girlfriend? What if he was trying to rape her? What if you hadn't yelled and I hadn't screamed from a distance for him to STOP? What if he beat her to death? Should I not have - should I not try to send the police after him? Should I not have tried to describe him like I remember?

EZRA: Even if your memory is blurred? Even if it's clouded with emotion? Not for one second did I look at that man and think he was Black. Or even young. He was buried in clothing. I didn't know what race he was. He was a blur of half a man. A colorless half a man.

AYANNA: That belongs in jail.

EZRA: That maybe needed some help.

AYANNA: Needed some help?

EZRA: Maybe was homeless and insane or on drugs or high. Maybe was desperate and trying to rob her. Maybe was a kid in trouble - misguided. Maybe -

AYANNA: Maybe was an asshole that needed to be locked away.

EZRA: Maybe. (Beat)

AYANNA: I'm going to make some tea. Do you want some tea?

EZRA: No.

AYANNA: Are you ... are you upset? With me?

EZRA: No. I'm just- no.

AYANNA: I thought he was. He looked like - the way he was dressed. I didn't even consider that he wasn't. Until you got me confused. I didn't even consider for a second.

EZRA: That's the itch right there. That you didn't even consider - there was no possibility of it being another - in your mind, we're the default. How are we your default?

AYANNA: Ezra, I'm on your team. You know that, right? You and me, husband and wife. I wouldn't -- We're going to have a son. I'm on your side. I'm also one of "us." I wouldn't-

EZRA: I know.

AYANNA: Ethno-cultural empathy.

EZRA: What?

AYANNA: In my reading. You're more likely to have empathy for someone who looks like you. Shares your same background. Walked a mile in your shoes. You're concerned about the brother. Concerned that he may be getting a bad rap. I get it. Meanwhile you haven't said one thing about the woman. Even wondered if she was ok.

EZRA: That's what you think of me? That I don't care about her? That I wasn't worried about her getting the life knocked out of her? Why do you think I yelled?

AYANNA: Why didn't you chase him?

EZRA: And what should I have done with you? Leave you? In the middle of Green Ave in the dark? Pregnant and alone? That's the man you want to have a child with?

AYANNA: No. (Beat)

EZRA: I need to take a walk.

AYANNA: You're going to leave? While I'm emotional???

EZRA: No baby, not leaving. Just stepping out. Need some air. Come back. Rub your feet. Draw you a bath. Okay? (EZRA grabs his hooded sweatshirt.)

AYANNA: You're not going to -- You're not going to wear that.

EZRA: It's getting chilly out there.

AYANNA: Not tonight. Not tonight.

EZRA: It's all I have. This and a winter coat. I'm supposed to carry that weight now? It's supposed to be my burden to change my attire now?

AYANNA: You're going to make me insane.

EZRA: I'm just going to take a walk, baby. Come back. Put you to bed. Just wanna go make sure everything is okay out there. That's all. You stay here. Rest. (EZRA heads to the door. Looks at AYANNA) Listen ...if you're sure, then I trust you. I stand by what you saw. (He walks over. Kisses her on the forehead and leaves) (A moment. She peers out of the window.)

(Flash of police car lights. Sirens.) (Suddenly a kick in her stomach. Intuition. She grabs her belly urgently.)

AYANNA: Oh God . . . I'm not sure . . . (She holds her breath - hands over her heart)
```

---

## IC-0876: Nina in the Morning

- Title: Nina in the Morning
- Author (byline): Christopher Durang
- Work: Durang, Durang
- Publisher: Dramatists Play Service
- Publication date as stated: June 1996
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, NINA, JAMES, FOOTE, LA-LA, ROBERT
- Teaser before the introduction: Yes
- Spoken words (computed): 1144
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christopher Durang
Book: Durang, Durang
ISBN: 978-0822214601
Publisher: Dramatists Play Service
Date: June 1996
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Everyone has a story, a history that is unique.

ACTOR 2: Unfortunately, in America the elderly are not a valued sector of society. For this reason many Americans are in denial of aging, the plastic surgery industry his exploded and women are perpetually turning “29.”

ACTOR 1: As a culture, we appreciate vintage in wine, not people; we "distress" furniture to make it look old, but pay thousands of dollars to erase the wrinkles that time bestows on our faces. It’s a futile battle we are all destined to fight.

ACTOR 2: Today Nina is another day older as we take a tongue-in-cheek look at aging with

TOGETHER: Nina in the Morning by Christopher Durang.

The NARRATOR is onstage. He is dressed in a tuxedo and looks elegant. As the music is finishing, NINA enters. She walks towards her chaise with great regalness, as if she's in a procession, on her way to be crowned. When the NARRATOR speaks, he is speaking her thoughts, usually. So her facial expressions change with his comments. She does not otherwise look at him or relate to him (with a couple of noted exceptions)
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actor 1: Nina Actor 2: All other roles

NARRATOR: The mist hangs heavy over the ocean today. Nina woke from an uncertain sleep and walked to the chaise in her dressing room and sat in front of the beautiful, cherished mirror. (NINA sits on her chaise, and looks out to her mirror and gasps.) Her facelift had fallen during the night, and her cheeks were held in place by straight pins.

NINA: (Looking in mirror, touching her face delicately) Oh, Lord. Oh, Lord. How dreadful. (Enter JAMES, her child, dressed in short pants and a white shirt. He looks like a well-dressed prep-school boy)

JAMES: Good morning, mother.

NINA: Don't kiss mommy today, her face is precarious.

JAMES: I don't want to kiss you anyway. I hate you.

NINA: Please don't upset me, James. My plastic surgeon is in Aruba.

JAMES: What's this pin for? (Reaches for her face, pulls out a pin.)

NINA: James, stop that. Stop it. Foote! Foote! Come quickly, James is at my face again.

NARRATOR: But James kept reaching for Nina's face, over and over.

NINA: Stop it, you unruly child. (JAMES keeps trying to pull pins out of her face. NINA keeps trying to protect her face. All the pin business is mimed. FOOTE, the family manservant, enters. Dignified and in a tuxedo.)

FOOTE: You called, Madame?

NARRATOR: Foote, seeing Nina's predicament with her son, pulled James away from her, pushed him to the ground and sat on him. (FOOTE pulls JAMES away, pushes him on the ground and sits on him.)

NINA: Gently, Foote, gently.

JAMES: (Struggling with FOOTE.) I hate you, mother, I hate you.

NARRATOR: Foote took out a hypodermic from his jacket pocket, and gave the misbehaving child a shot. JAMES I hate you. I'm sleepy. (Passes out.)

FOOTE: Will that be all, Madame?

NARRATOR: Foote was the family manservant, and often gave the children general anesthesia whenever they became unruly. Foote had once been a dentist.

NINA: Thank you, Foote. James was pulling pins out again. I must have done something wrong raising them. I thought I often smiled. I wonder if they wanted anything else.

FOOTE: Do you wish me to remove any teeth while he's out?

NINA: No, no. Leave his teeth alone, Foote. I just want quiet for a while. Look at how peaceful James is, curled on the floor. I always liked my children best when they were unconscious.

FOOTE: If Madame needs me further, just call.

NINA: Thank you, Foote. You're a jewel. (FOOTE exits.)

NARRATOR: Foote withdrew, leaving Nina with her thoughts. She thought about her face. She thought about James. Psychotherapy had been no help for James except perhaps in helping him to express his anger more freely, and how useful had that been.

NINA: (Sort of to herself.) Not very.

NARRATOR: Nina's hands shook as she lifted a coffee cup to her face. Her perceptions were off, and she poured hot liquid down the left side of her face. She put cream and sugar on her face, stirred it and then rang the bell for Foote.

(NINA mimes the actions the NARRATOR says above while, or shortly after, he says them. She does all the gestures without emotion. She feels the heat of the coffee and the mess of the liquids after she has done all of them. She makes a face of pain, and confusion, then rings the bell.)

NINA: Foote, I need you. Bring a wet cloth. I'm sticky.

NARRATOR: Foote brought a basin of warm water and a roll of gauze and sponged her gingerly. (FOOTE enters and starts to pat NINA's face lightly with the cloth.)

NINA: Do you think I'm beautiful, Foote?

FOOTE: You once were very striking, Madame.

NINA: Yes, but now, what do you think of me now?

FOOTE: (Looks at her.) You have quite a nasty burn on your face, Madame. Would you care for a shot of novocaine?

NINA: Go away, Foote. I want to think.

NARRATOR: And again, Foote withdrew, dragging James after him. Nina racked her brain, trying to remember what she wanted to think. The colors of her wall were beige. She had wanted burnt orange, but the designer had run through the house screaming "Beige! Beige!" and they finally had to give him his way.

NINA: (Out, to the imagined designer.) I wanted burnt orange, but you have given me beige.

NARRATOR: Later the designer turned against her too, like her son James. No, no, Nina wanted pleasant thoughts, nice things. Flowers, butterflies . . .

NINA: (Hopefully.) Little duckies.

NARRATOR: The Little Prince by Saint-Exupéry. That was a nauseating little book, she had never finished it. Some monk gave it to her when her car had been stopped at a traffic light.

NINA: Foote, if any Jehovah's Witnesses come today, show them in, will you?

NARRATOR: But no Jehovah's Witnesses came. And Nina found she had to fill the time with thinking and reminiscing. Nina had once been beautiful.

NINA: I am very beautiful.

NARRATOR: Men would stop on the street to stare at her. She caused traffic accidents. Jealous women would rush up to her in their homeliness and try to kill her.

NINA: Homely women were always trying to shoot me. It was flattering really.

NARRATOR: Everywhere she went, her eyes would anxiously seek out the mirrors. Sometimes she would bring her own mirrors with her.

NINA: Put this up, would you?

NARRATOR: Nina would say, lugging a large mirror, and few could deny her. Her love affairs were unpredictable and random. Sometimes it would be royalty, other times it would be the men from Con Edison. (The NARRATOR turns his back, pretending to look at a power box. He is now the CON EDISON MAN. NINA comes up to him, stands close and seductive.)

NINA: I don't really know where the power box is, I'm afraid. Would you care to lie down? (The NARRATOR reverts to his narrator role, and addresses the audience again.)

NARRATOR: Sometimes when she was especially lonely, she would try to seduce her children.

NINA: Don't you find mommy especially attractive today?

NARRATOR: She would ask James . . . and Robert . . . and occasionally poor La-La.

LA-LA: (Happily and monotonously singing to herself.) La-la-la-la-la, la-la-la-la, la, la, la, la . . .

NARRATOR: La-La was retarded, and Nina hated her.

NINA: La-La! Pay attention! (LA-LA turns away, opens up her lunch box and starts looking through it happily.)

LA-LA: La-la-la-la-la, la-la-la . . .

NINA: Uhhhh. You're willfully retarded.

NARRATOR: Nina would shout this at La-La, and then hit her. But Nina mustn't think of the past now. The present was what held promise. Her plastic surgeon was due back in several days. (NINA rings the bell.)

NINA: (Grandly.) Foote, I want a cruller!

NARRATOR: She heard what she presumed were Foote's footsteps, but they belonged to her second son, Robert, who fired two shots, one of which grazed her shoulder. (Enter ROBERT, dressed the same as JAMES but with the addition of the glasses. He shoots a pistol twice at his mother. On the second shot, NINA moves her shoulder as if hit.)

ROBERT: I hate you, mother!

NARRATOR: Then he ran into the garden. (ROBERT runs off. NINA holds her shoulder and rings the bell again.)

NINA: Foote, bring the gauze again, please. My shoulder is bleeding. Foote! Foote!

NARRATOR: James's father had been a tax lawyer, but Robert's father had been one of twenty men; and La-La's father had been one of fifty-six men that busy summer she had the beach house painted. After a brief burst of self-judgment, she searched the thesaurus for alternatives to the word "promiscuity."

NINA: (Miming looking in a dictionary.) Synonyms include "debauchery." "Salacity." And "lubricity." "Lubricity." "Loooo-bricity." "Loooooo-briiiiiiii-ci-teeeeeeeeeee.

NARRATOR: Nina liked the sound of "lubricity" and that summer she would climb up the ladders and whisper the word into the house-painters' ears. (The NARRATOR finds himself near NINA. She stands and seductively whispers in his ear, as if he's the house painter.)

NINA: (Whispering into his ear.) Lubricity. (Enter FOOTE with some more gauze.)

FOOTE: Has Madame been shot?

NINA: Yes, Foote. Robert said something to me, something mean, and then he shot me. What took you so long?

FOOTE: I'm sorry, Madame. I was giving La-La a hypodermic shot to calm her down. She was complaining about something and acting retarded, and now she's quiet and good as a lamb.

NINA: Go away, Foote.

FOOTE: Yes, Madame.

NINA: Oh my life, my life, my life. What has become of my life? (Looks in the mirror anew.) And what has become of my face? Oh my. Pins are for curtains, not for faces.

NARRATOR: Nina stared at herself in the mirror and tried to decide whether or not to kill herself. She stared a long while. She didn't look well. Slowly she took the pins out of her face. (NINA mimes taking pins out. Then she pulls her cheeks downward, and stares tragically at herself in the mirror.)

NARRATOR: Her cheeks drooped downward, and her eyes filled with tears. Of course, when the doctor returned from Aruba, he'd make Nina look substantially better. And she didn't know how to kill herself, unless one of her children shot her.
```

---

## IC-0877: Nine Hours to Fallujah

- Title: Nine Hours to Fallujah
- Author (byline): Craig McNulty
- Work: 2006: The Best Ten-Minute Plays for Two Actors
- Publisher: Smith & Kraus, Inc.
- Publication date as stated: Nov 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BRIAN ALYESWORTH, TIME, SETTING, MO, BRIAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1440
- Already set (do not supply): none

### Source block (context only)

```text
Author: Craig McNulty
Book: 2006: The Best Ten-Minute Plays for Two Actors
ISBN: 978-1575255637
Publisher: Smith & Kraus, Inc.
Date (Month/Year): Nov 2007
```

### Introduction (context only: never use it for content warnings)

```text
Actor: As of September 2010, 4,427 US soldiers have been killed in Iraq. 54% of that number

were under the age of 25. With attacks coming as swiftly as they do randomly, fear can

be a constant companion for many soldiers. Actress: Soldiers know that blood and death come with the job. – But what if you find something

else during the war? What if you find love? Actor: To date more than 182,000 women have served in Iraq, Afghanistan and the

surrounding region. With the fear of death a constant companion, it is human nature to

find solace and relationships with others. Actress: In Nine Hours to Fallujah by Craig McNulty two young soldiers, Maureen (Mo) and

Brian discuss their feelings for each other and their fears of war. Together: Nine Hours to Fallujah by Craig McNulty

AT RISE: Sounds of explosions to a black stage. Lights come up on Brian (twenty-one) seated on an army blanket and writing in a journal. He has his shoes off and has articles spread around the blanket (towels, shirts, food rations). Coming up behind him is Maureen (a.k.a. "Mo")

(twenty-two) holding a handgun. Brian is consumed with writing in his journal and doesn't see her. She is looking intensely at him. She puts the gun away, takes a swig off a flask, and begins to sneak up on him. Even as she is standing right behind him and reading over his shoulder Brian still doesn't know she's there. She grabs him under his arm and says -
```

### Performance text (classify this)

```text
CHARACTERS MAUREEN JACKSON (aka "Mo"): twenty-two, marine reservist. She wants to be a teacher. She was part of a convoy that was attacked by insurgents, where she fought bravely and remained very calm and very cool - what Hemingway would've called grace under fire.

BRIAN ALYESWORTH: twenty-one, Marine reservist. Engineering major and film fanatic, but the type of guy who would be more into Scarface than Breathless.

TIME: November 8, 2004, 9:30 PM

SETTING: Iraq, U.S.A. military camp just outside of Fallujah

MO: Private Alyesworth. (Brian jumps, sending his book flying.)

BRIAN: Jesus Christ Mo! You scared the living shit outta me.

MO: See, if I was a suicide bomber, you'd be dead.

BRIAN: If you were a suicide bomber we'd both be dead.

MO: Yea, but, you be burning in the infidel fires of hell and I'd be in Allah's paradise.

BRIAN: With the rivers of honey and the seventy-two virgins?

MO: Yep. But I don't get how that's supposed to be an incentive, I mean, I'm not gay or even an occasional switch-hitter, so the seventy-two hottie Arab chicks don't do it for me. And seventy-two male virgins, what would that be, seventy-two teenage Arab boys who's idea of *passion* is throwing me to the ground for a session of amour that lasts all of sixty-four seconds? Wow, whoopee, that's a *heck of* a paradise for a girl to look forward to.

BRIAN: Maybe the men would look like Omar Sharif or Valentino.

MO: (Considers this.) Yea ... Nah, that still doesn't do it for me. (Interrupted by three particularly loud explosions in the distance.) I don't think the locals will be too happy to see the Stars and Stripes tomorrow.

BRIAN: Softening the enemy is the going expression ... Yea, probably as effec-tive as kicking a junkyard dog a couple of times thinking it's going to make him more docile.

MO: I understand the General gave a riveting speech yesterday

BRIAN: Invoking the usual suspects: sands of Iwo Jima, shores of Tripoli, John Wayne, John Rambo.

MO: He's seen Patton a few too many times.

BRIAN: The general was a "hero" in the epic war against Grenada. Two years ago smoking and watching Full Metaljacket never thought I would be in this position.

MO: None of us did Bri ... Just pay close attention to the children.

BRIAN: What?

MO: When the main fighting is going on they'll be gone. When things calm down and you'll see kids around, then the area is probably clear. Not absolutely but probably ... but if the kids are around, then they all sud-denly seem to split, that's when you know *it* is definitely hitting the fan.

BRIAN: OK.

MO: The first time you see someone shooting at you, I mean you can see their face, you're going to be tempted to go for a head shot, don't. Just remember like it was back in basic and aim for the torso ... (Mo's now looking through Brian's CD case.) Jesus, Limp Bisket isn't really your favorite band, is it?

BRIAN: What? Oh, not really. Jerry gave it to me, said it was good rolling out music.

MO: I would just hate to think of anyone dying and the last thing they lis-tened to is Limp Bisket. (Mo throws CD upstage.)

BRIAN: Mo!

MO: Or Eminem, he's such an *idiot*. (Mo throws Eminem CD as well.)

BRIAN: Mo, will you stop *messing* with my *stuff*!

MO: OK, just trying to help.

BRIAN: Just don't touch my stuff.

MO: If you had one thing to listen to before you checked out what would it be?

BRIAN: I don't know. Maybe something by U2 or maybe Nirvana ... tough question.

MO: It is a tough question. When I'm feeling down I listen to Bob Marley and I feel better, or I listen to Bright Eyes and it makes me feel worse ... but in a good way.

BRIAN: Who is Bright Eyes?

MO: It's the music I played that night, don't you remember?

BRIAN: Yea, I remember. (Mo takes letter out of her pocket.)

MO: So, I found this under my pillow ...

BRIAN: Yea, well, you weren't supposed to read it till Thursday. See where it says on the outside, Do not read till Thursday?

MO: Well you didn't date it genius, so for all I knew you meant last Thursday which would've made it a OK for me to read it today.

BRIAN: Oh, is that it? Guess I should've been more specific.

MO: Guess so, and who do you know that would get a letter that says don't open till Thursday and would actually wait for Thursday?

BRIAN: I had this nightmare. I had it more than once. There's all these soldiers who've had their arms, legs, and faces blown off, and they're burned ... badly. I'm nervous to see them. I'm afraid to be in the same room with them because I'm afraid I'll lose *it* and come off looking like a wuss. So all these dismembered soldiers are dressed up in various outfits, like Hawaiian shirts and football jerseys told how good they look and wheeled around to try to make them feel better, and the whole thing is horrific ...

MO: It's like so OK to be scared the night before, you wouldn't be human if you…

BRIAN: Been really sensitive last few days to sensations in my fingers and toes

MO: Is there something wrong with

BRIAN: There's nothing wrong, I've just been thinking I don't wanna go home like Stevens or Washington ...

MO: Or like that guy in The Sun Also Rises.

BRIAN: Who was in that?

MO: I don't know, it wasn't a movie.

BRIAN: I think it was.

MO: Jesus, did you ever have to take a liberal arts class or have a summer reading list?

BRIAN: Yea, but that's why God invented Cliff Notes, right?

MO: Whatever ... in the book by Hemingway the protagonist gets his genitals blown off in World War One? His equipment isn't up for the job anymore ...

BRIAN: Thanks Mo, that's a *heck of* story to tell someone the night before a major operation.

MO: Sorry sorry sorry, I know, bad Mo, mouth going before I was thinking.

BRIAN: Yea, well, anything like that and I want you to

MO: Now, getting shot in the leg, the fleshy part, not hitting bone, if you had to get it that would be the best place to get shot, with as Iowa caliber as possible. You'd get a Purple Heart and a one-way trip to Germany with that one.

BRIAN: Listen Mo, I'm Catholic ...

MO: OK, and I'm a Methodist, what does that got to do with anything

BRIAN: If my legs or arms or face were blown off I'd just as quick stick my gun in my mouth and blow my brains to Syria . . . but being a Roman Catholic ya can't kill yourself I guess you can kill as many other cats as you want and still see heaven just not yourself

MO: Never thought of you as being very religious.

BRIAN: Mo, a hot shot of as much morphine as you can get a hold of and just let me go off to sleep.

MO: (Furious) How can you ask me to do something like that?!

BRIAN: I just thought that we, I'm asking you because

MO: It wasn't the booze.

BRIAN: The?

MO: I just wanted you to knowl

BRIAN: That?

MO: I wasn't with you for an evening's entertainment or ... it wasn't like that for me.

BRIAN: Yea, well, me too. For an evening's "entertainment" I usually play poker or something, but not that.

MO: I don't want you to think because I'm saying no to this that I don't

BRIAN: 0K OK OK, it's fine, really.

MO: Can we just talk, like talk talk for a few minutes?

BRIAN: What difference would it make?

MO: Because if we were at school together and you were getting into a bus and riding out of town for summer break it wouldn't be a big deal, right? Sure, I might get killed in a car accident or OD on meth, but chances are none of that would happen. Chances are whatever we'd wanna work out between us,

BRIAN: So it was a big favor to ask of you and you don't feel too swell about l doing it, fine. I don't know if I could look into your eyes and do it for you, but right now there's nothing else to talk about.

MO: Brian, it's just more complicated than how I feel about you

BRIAN: You wanna tell me, what? That you don't sleep around? Great, thank you. I never thought you did. A few hours from now that information is going to be useful to me ... how?

MO: Yea ... no ... I don't know ... (Brian goes back to messing around with his backpack, Mo gets up and begins to leave.) We'll always have Iraq ... during the winter time ... in the middle of the Jihad right?

BRIAN: Right. (Brian stops putzing with his bag, stands up.) You know I've never seen Casablanca.

MO: Really?

BRIAN: Nope, just never got around to it. (Mo takes a long look at Brian.)

MO: You will. Trust me.

BRIAN: Maybe.

MO: Did you mean what you wrote at the bottom of the letter?

BRIAN: Yea, but I think you knew that already. (Mo slowly walks over to Brian, she runs her hand over his face and they share an intense kiss.)

MO: I love you, too. (Mo exits quickly stage right.)

BRIAN: Maureen, wait! (Brian goes to grab his boots to chase her when he is shot in the leg, in the calf) AHH!!! (Three sharp whistle blasts from stage right.)

MO: (Offstage.) Sniper Action Northwest Corner, incoming! (Prolonged machine-gun blasts offstage, Mo enters stage right with her weapon drawn and kneels next to wounded Brian.)

BRIAN: MO! What did you do?! (Mo grabs a towel and begins to wrap Brian's leg.)

MO: I got you covered baby, don't worry, I got you covered. (Lights to black as machine-gun bursts continue)
```

---

## IC-0878: No More Monsters Here

- Title: No More Monsters Here
- Author (byline): Marcus Gardley
- Work: Facing Our Truth
- Publisher: Samuel French, Inc.
- Publication date as stated: July 2015
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: REBECCA, DOC, GREATEST GRAND, RAHEEM, EMPLOYER, OOKIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1770
- Already set (do not supply): none

### Source block (context only)

```text
Author: Marcus Gardley
Book: Facing Our Truth
ISBN: 978-0573704260
Publisher: Samuel French, Inc.
Date (Month/Year): July 2015
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: On February 26, 2012, Trayvon Martin, an unarmed African American teen dressed in a hooded sweatshirt, was walking home from a convenience store in Sanford, Florida.

ACTOR: He was fatally shot by George Zimmerman, a neighborhood watch volunteer.

ACTRESS: Zimmerman claimed self-defense under the auspices of the “Stand Your Ground” law.

ACTOR: He was charged with second-degree murder.

ACTRESS: He was acquitted.

ACTOR: Follow closely the most recent high-profile shootings of black men.

ACTRESS: Say their names:

ACTOR: Michael Brown, ACTRESS: in Ferguson, MO;

ACTOR: George Floyd ACTRESS: in Minneapolis, MN and

ACTOR: Ahmaud Arbery ACTRESS: in Brunswick, GA (to name just a few)

ACTOR: You’ll notice a pattern.

ACTRESS: Only the slightest level of alleged misconduct or “suspicious” behavior is used to justify the fear that led to their deaths.

ACTOR: Fear – reasonable or unreasonable?

ACTRESS: No More Monsters Here by Marcus Gardley explores the question:

ACTOR: Can you truly understand someone until you’ve walked a mile in their shoes?
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actor: Doc, Greatest Grand, Employer and Ookie Actress: Rebecca and Raheem

(A black psychiatrist looks over a patient’s file. The patient is a white woman.)

REBECCA: (Pg 79-93) What’s up, Doc? You look worried. What’s the diagnosis? Am I insane? I’m insane, aren’t I?

DOC: Insane is such a strong word, Rebecca.

REBECCA: Oh God, I knew it! I’m my mother.

DOC: No, no, no. Calm down. Take a deep breath. What you have is totally normal… unfortunately. Plus there is a cure. You have negroidphobia.

REBECCA: Hold the phone. I got negro what?

DOC: Negroidphobia. It’s a fear of people of African descent -- primarily black men. Just as arachnophobia is a fear of spiders and alektorophobia is a fear of chickens, you have Negroidphobia which is a fear of nig-

REBECCA: -- Shut the gate, are you saying I hate black people! That’s a lie! One of my neighbors is African American. I’ve had her over the house for quiche. Plus, I know the theme song to the Fresh Prince of Bell Air. How can I be racist?

DOC: Nobody’s saying you’re a racist, Becky. I mean, you are but nobody’s sayin it. Racism implies that you see a culture as inferior or superior to another. It is a bi-product of privilege. No one can cure that but Jesus. What you have is more specific.

REBECCA: I’m offended.

DOC: Wow. You fear black men because you have bought into the myth that they are violent and you’re the one that is offended. Classic projection. (He writes on his pad)

REBECCA: This is going to sound racist, cliché and ignorant but honestly one of my best friends is a black. Shoronda. We got a secret handshake, she taught me how to twerk, I ate chicken at her church one Easter, plus she lets me touch her hair.

DOC: I guess Doctor King’s Dream has been fully realized then, hunh? WAKE UP! Nobody is saying that you hate blacks, Beckka. I’m saying you fear blacks. You failed our fear of a black planet test. When a black man walks pass your car, you admit to locking the doors and turning on your car alarm.

REBECCA: Yeah but I wasn’t locking it because he was black. I was locking it because he looked scary.

DOC: Exactly!

REBECCA: (beat) Oh god. I . . . I really do fear black men. Sweet Jesus, I’ve become my father.

(She cries)

DOC: There, there, there, Beckett. It’s okay. The first step to recovery is admitting [it]. You came to me because you’ve been having nightmares about Favor Flav (1) hiding in your closet. This fear you have is real. But a lot of Caucazoids have it. And that’s why I invented a cure. It’s in its experimental stages but so far it has helped a significant number of whites who have undergone treatment. The process only takes a few days.

REBECCA: What do I have to do?

DOC: It’s simple. You just have to put on this hoodie and live in the hood for three days as a black man. (Doc hands her a black hoodie) It looks like any old black hoodie but it’s actually a state-of-the-art transformational mask. Using holographic imaging, it forms a unique black face to cover your own. If you wear it, it will make you look like a black man. No one will assume that you are a white woman behind the mask. You will be black and literally walk in another man’s shoes for three days. This will no doubt cure you of your negroidphobia. Trust me, it’s surefire. Go ahead put it on. We can begin our treatment immediately.

REBECCA: Oh, I don’t know. Shouldn’t I have time to think about this first? What if something happens to me in the hood?

DOC: Be brave, Rebbie. Don’t you want to be a fully evolved, open-minded human being for your race? (Rebecca nods tentatively and quickly puts on the hoodie) You’ll also need to sag your jeans. (Rebecca tugs her jeans down around her hips) A cultural ambassador will help you change your walk and voice and attempt to teach you how to do the Harlem Shake(2) In time, no one will notice old Rebecca from the new Raheem. (They shake. Then he Harlem shakes as he exits. She gets dressed and practices her walk. It is ridiculous.) ******** 24 virtual hours later *********** Greatest Grand enters. She is 162, hunched over to her toes. She wakes Rebecca who has become Raheem.)

GREATEST GRAND: Rise and shine, Raheem. Breakfast is the most imported meal of the day. Gots to eat. Gots to eat black food if you wants to uplift the race.

RAHEEM: Uh . . . I ain’t hungry, granny. I’ll get something later.

GREATEST GRAND: Ain’t hungry!? Why? Have you gotten too good for soul food? I send you to that good school to gets an edumacation and you got too good for chitlins. You must not be feeling well. Steel grievin’ over Ray Ray’s death? Shugar, don’t you know you live in the hood? You might as well fact the fact that a lot of your homies are gonna get got at a young age. Hell, you 18. You lucky you still livin’ your damn self. The black man is an endangered species, baby and you is in danger.

RAHEEM: That’s a bit of an exaggeration isn’t it? I mean, I see a lot of brothers hanging on the street corner. On the basketball court, at the club. They chillin in the cut on the regular.

GREATEST GRAND: No, they’re getting cut down on the regular. Many bodies get laid to rest on the daily because the black male body is the great American sacrifice. History has had it hanging from trees, chained to gangs, burnt to bones and the future’s got it slavin behind bars. It must be put out of sight. Cause you’re public enemy number one. You still put the fear of God into even the good, hippy, free love, liberal minded folk. The media, the TV, the movies, hell even hip hop makes you out to be a bad ass. But it ain’t real. It’s just story. Stereotypes hyped up into stereo. But you can take your life and rewrite it, Raheem. Create a future for yourself that is bigger – better than this story you were told to buy into. Ergo baby, you need to get a job. (She throws a dress coat over him and hands him a tie. He puts it on) I spent the last of my social security to get you this suit. Don’t disappoint me now. ********* Wal-Mart ***********

EMPLOYER: According to your resume, you have no marketable skills. You’ve never even held a job before.

RAHEEM: I know but I can’t hold down a job if someone doesn’t hand one to me.

EMPLOYER: Well, my hands are tied. I can’t afford to take a chance on anybody right now.

RAHEEM: - Who says I’m a chance? I could be the best employee you ever had.

EMPLOYER: Fat chance: your resume has misspellings, you arrived thirty-three minutes late to your interview and you have no references.

RAHEEM: Yeah but this is Walmart. You got old people greeting folks at the door. You sell low quality products made by children in third world countries for poor people in the US many of whom are on welfare. I just want a job, man. I’m trying to bag groceries. Let’s keep it real. I can say paper or plastic with a smile. Check this: (He smiles) Paper? Plastic?

EMPLOYER: Yeah see, this is not going to work. I don’t think you possess the Walmart spirit.

RAHEEM: Look, my grandmother spent the last of her social security check to get me this suit.

EMPLOYER: That’s precious. We’ll call you if something becomes available. In the meantime, I suggest you find a career more suitable to your work experience. ******* On the streets ********

OOKIE (a street thug): Yo, son I heard you lookin for work. Pray tell, what’s your five-year plan, homie?

RAHEEM: Five-year plan? I’m just trin to make it to tomorrow. Trying to pay my Granny back for a suit she bought me.

OOKIE: That’s touching but you need a five-year plan, dawg.

RAHEEM: Wait, you sell drugs!

OOKIE: Pharmaceuticals. Drugs got a negative connotation. I sell pharmaceuticals. I feel like you judging me holla hard right now.

RAHEEM: Well, I was thinking of going to college.

OOKIE: College!? You stupid! Corn Nut’s brother got a degree from CUNY and right now he workin at the Starbucks on 125th. I make ten times what he make and I don’t pay Uncle Sam a penny. Open your eyes cuz, colleges have become corporations. You want to make real money, you got to have an entrepreneurial spirit. You got to focus on product. You got to sell. (OOKIE hands him several very large sandwich bags stuffed with marijuana)

RAHEEM: Oh, I don’t know. I hear the NYPD is giving brothers ten years just for dime bags. Plus, I don’t think I could handle prison, I’m too pretty. (RAHEEM shows her profile)

OOKIE: You’ll make over 500 dollars a day.

RAHEEM: OMG! Count me in. When can I start?

OOKIE: Today. I’m giving you some merchandise cause your story touched me and I know you just trying to hep your granny out so . . . do me a favor and don’t get caught. Try not to be so . . . how do I put this . . . black.

RAHEEM: Right. I’ll see what I can do.

(Raheem walks the street. Tries to remember how he walked when eh was Rebecca, but he can’t. He walks. He is being followed by someone. He walks faster – the figure follows him. Eventually, he stops. The figure stops)

RAHEEM: Who’s following me? Stop being an asshole and show yourself. I ain’t no punk. . Show yourself, I said! (Silence) I should known better than makin a drop off in the suburbs. Playa hatin! Aight Raheem, relax. Play it cool, homes. Be Rebecca. Try not to stand out. This is your last day in this hoodie. Last day wearin this mask. Just try to get through the night.

(Again he walks. He tries to walk white. He can’t do it. The figure follows again. Raheem runs, falls and the figure falls on top of him. They fight. The figure breaks free and pulls a gun from his pants and points it at RAHEEM. REBECCA screams.)

RAHEEM: Wait! Hold on! I’m not Raheem, I’m not black. I’m Rebecca. I’m white. (She tries to take the hoodie off but cannot. I’m Rebecca Smith. This is just an experiment, a cure. Please! Please sir don’t . . . don’t shoot. Things are not as they seem. I’m not as I . . . I’m a . . . (The figure cocks his gun. Rebecca screams. He shoots. Rebecca grabs her heart, she wails.) (BEAT- The figure takes his mask off. It is Doc.)

DOC: It’s okay. It’s okay Rebecca Smith. It was just a simulation. You are not shot. You are not bleeding. It was not real. You are well now. You are healed.

REBECCA: (Screams in anger and frustration)

DOC: You’re welcome?

REBECCA: That was not fair! That was not okay! I felt it. I felt the bullet go through me, okay. I felt them. (She cries)

DOC: Them?

REBECCA: Those men. Why’d you do that? Why you make me feel them; their pain. I saw their faces: Medgar Evers, Emmit Till, Oscar Grant, Sean Bell, Amidou Diallo(3) and lynched black men. It was inhumane. It was *wrong*. . . So *WRONG*!!!!

DOC: I have no idea what you’re talking about. There ware no men, Rebeck –

REBECCA: DON’T LIE TO ME! You used me! Got into my head. They’re in my head, still. Whispering. They’re mad! I’M SO MAD!

DOC: It’s just a side-effect, Mrs. Smith. Trust me, you are healed. You are better.

REBECCA: I don’t want to be better. I want them out of my head.

DOC: Look, please calm down. I sill want to run a few tests.

REBECCA: NO! Hell no! I will no longer be your test rat. This treatment should be banned. You should have your license revoked. This is racist! (She grabs her coat and purse)

DOC: Wow. Okay. So I guess you won’t be recommending me to your friends. (Rebecca screams in frustration and exits, slamming the door.)
```

---

## IC-0879: A No Play

- Title: A No Play
- Author (byline): Sarah Provost
- Work: More One-Act Plays for Acting Students
- Publisher: Meriwether Publishing Company
- Publication date as stated: July 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ANNIE, AVERY
- Teaser before the introduction: No
- Spoken words (computed): 2202
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sarah Provost
Book: More One-Act Plays for Acting Students
ISBN: 978-1566080873
Publisher: Meriwether Publishing Company
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
AVERY: (angrily) No.

ANNIE: (sadly) No.

AVERY: (defiantly) No.

ANNIE: (hysterically) No!

AVERY: (questioningly) No?

ANNIE: (hopefully) No?

BOTH: (with a smile) No.

AVERY: “No Play”

ANNIE: By Sarah Provost
```

### Performance text (classify this)

```text
(ANNIE is discovered at the stove. She sets the table for two with wine glasses and candles and stirs a pot of tomato sauce, singing "Yes, We Have No Bananas." AVERY drags himself through the door carrying a briefcase, which he sets in the middle of the table. He goes to a counter, his back to ANNIE, picks up a pile of junk mail and sorts through it.)

ANNIE: Hi, honey! How you doing? Wasn't it a beautiful day? I do hate to see summer end, but the fall sky is just so blue! And the first cool weather makes me feel like cooking. So guess what we're having tonight? La-a-a-sagna! (AVERY continues to sort through the mail without looking up.) Avery? Didn't you hear me? (He looks up briefly, a bit quizzical, then shakes his head.)

AVERY: No.

ANNIE: We're having lasagna! I hope you're hungry.

AVERY: No.

ANNIE: Not hungry for lasagna? Whoa! Are you OK?

AVERY: No.

ANNIE: Oh, poor baby! I'm sorry. What's the matter, is your stomach upset? Do you want some Turns or something?

AVERY: No.

ANNIE: Headache?

AVERY: No.

ANNIE: Well, what is it then? (He shrugs and exits to the bedroom, taking off his tie.) Honey? Do you want to lie down for a while?

AVERY: (Off) No.

ANNIE: Then come keep me company while I finish this up. I'll put it in the fridge and we can nuke it up tomorrow. You'll feel better then, huh? (He returns minus jacket and tie, wearing a similar happi-coat.)

AVERY: No.

ANNIE: Oh, I get it. We're just in a lousy mood tonight. Obviously, this man needs a hug! (He accepts her embrace briefly, then fends her off) What'sa matter, baby, is Walt on your back about that report? Did Adam win the football pool again?

AVERY: No.

ANNIE: Then what is it, for God's sake! Aren't you going to tell me what's bothering you? (AVERY considers for a moment, then speaks decisively as he pours himself a hefty scotch on the rocks.)

AVERY: No.

ANNIE: Why not? Huh? Avery? If you're not sick, and it's not a problem at work... Oh. Oh, I know. This is about the gerbil, isn't it? Some busybody happened to be passing by and couldn't wait to tell you about it, huh? Well, you could at least do me the courtesy of hearing my side of it before you get all judgmental! (He looks up at her, mystified.) Here's what happened. See, when I went to the mall for my Jazzercize class, this skirt is getting so tight, and I went by the pet store - I know it's out of the way, but I always have to check for kittens in the window. Don't give me that look, I'm not going to bring any home, not after the fit you threw last time. But oh, there was one in the window, a little baby gray with long hair, absolutely gorgeous, but he was asleep, so flat out, he looked like a rug. I just thought it was cute, y'know, and went on to my class. But when I walked past again and it was an hour later and he hadn't moved, well, I thought he might be ... y'know ...So I went in and asked the guy in the store - skinny kid with long greasy hair - to check on the kitten, and he looked at me like I was nuts and said, "He's sleeping, lady." And I could tell that he was just waiting for me to leave. He wasn't going to do anything! And with all that long hair, I couldn't even tell if he was breathing. The cat. So I told the guy I wanted to buy the cat and could I see him. Well, he opened the pen and picked the kitty up, none too carefully, and gave him to me. That cat could make Rip Van Winkle look insomniac! He just draped himself over my arm and went on sleeping, but I put my face right up next to his little pink nose and I could feel that he was breathing, so I gave him back. He was OK. The guy was snippy 'cause I fibbed about buying it, but I felt better that I'd checked. Now see, I don't usually actually go in the pet store 'cause once I'm in there I always have to see the puppies too and all the other little critters, I can't even not look at the lizards and tarantulas and all the ugly stuff. So I was way in the back of the store where the gerbils and hamsters and guinea pigs and bunnies are - they had the cutest little miniature lop-eared bunny, I'd've brought it home in a minute if... (AVERY shoots her a dark look.) Well, anyway, I was back there in the Rodent Round-up when I saw this little black gerbil peeking out from under the cover on top of his cage! Actually I couldn't tell it was a gerbil at first 'cause all I could see were his little quivery whiskers. But sure enough he was on top of his cage and not in it! At first I just told him he was a mighty clever little rascal, but then I began to get worried. What would happen to him? Maybe he couldn't get back in his cage to eat, or somebody might step on him, or lord, he could even wander into the kitten's cage by mistake. Though I don't suppose that snoozy little guy'd be much of a threat. So anyway, I called the kid and he got all snotty, grabbed the poor little thing and just threw him back in his cage! Threw him! I tried to talk sensibly to him about how he shouldn't be working in a pet store if that's the way he felt about animals, but he just got really snotty and, Avery, he as much as accused me of letting the little guy out in the first place! So I ... well, I did open the cage and let the gerbils out. And the hamsters and the guinea pigs and the little bunny too. And they were all hopping around, you know, so happy! So while he was trying to catch them I let the birds out and they flew out into the mall, some them, and as I was leaving I let the puppies out and they started to chase the gerbils and mice and stuff, but I knew they'd never catch them. I even opened the kitten's pen, but he was still asleep. Now I know you probably think I over-reacted, but if you had got a taste of that guy's attitude you would have done just the same thing, wouldn't you? Hm?

AVERY: (After a beat; bemused) No.

ANNIE: That is what you're upset about, isn't it?

AVERY: No.

ANNIE: You didn't know about it?

AVERY: No.

ANNIE: Oh. Well if it wasn't that, then what is it? God, I hate it when you get mad at me and won't tell me what I've done! It's not fair! Is it because I've put on a few pounds?

AVERY: No.

ANNIE: Because I am going back to Jazzercise ... Oh! If this is about the dent in the car, that wasn't my fault! Is that what's making you so crabby?

AVERY: (He hadn't known about that either.) No. (ANNIE begins to get weepy and mushy, goes to him and clings to his arm as he tries to read the paper.)

ANNIE: Avery, honey, don't do this to me! I love you so much, and it makes me crazy when you won't talk to me. Tell me what's bothering you. I'll fix it! What am I doing that's wrong? Avery? I'm not going to go away until you tell me what's upsetting you, and don't say it's me because you were in a crappy mood the moment you walked in here tonight, and I'm not going to take it!

AVERY: No? (Insulted and angry at his snotty tone, she begins to sniffle.)

ANNIE: You can't treat me like this! This is not the person I want to be. Listen to me! You've got me all whiney and clingy and miserable, and that's not the way I am at all. I'm a very happy person, Avery, very happy, or I was until I got mixed up with you! I'm an optimist, Avery, one of those people who always sees the glass as half full and the skies are partly sunny. You know that. You said it's what you loved about me, remember? How I could just chatter along -like a little bird, you said and talk you out of a bad mood, cheer you right up. Now you look at me like that guy in the store did. And you know what, Avery? I'm beginning to feel like that damn gerbil! Maybe it's time I stuck my nose out of the cage. Because that's what it feels like these days, Avery, like a gerbil cage! (She begins to sob.) And I keep running on my little wheel, trying to make you happy, but Avery, you are not a happy person! I am a happy person! I'm hopeful and cheerful and I always believe that things will work out for the best, and I never give up hope on anything except... I am now. I'm leaving Avery. (She starts out of the room, all injured dignity.)

AVERY: No!

ANNIE: No?

AVERY: No. (He goes to her, takes her arm, leads her back to sit at the table. He offers her his hanky and waits while she wipes her eyes and blows her nose. There is a long pause, then:) You really don't understand me at all, do you?

ANNIE: (Sniffling and sullen) No.

AVERY: No matter how many times we go through this, you never learn. It isn't always about you. Sometimes I'm just in a bad mood, OK? I've got a right to be in a bad mood now and then, don't I?

ANNIE: No.

AVERY: Well, maybe I carry it a little far sometimes, but Christ! You drive me crazy! You just push at me and push at me until I want to - Rargh! But that doesn't mean I don't care about you. Can't you understand that?

ANNIE: No.

AVERY: What the hell is it with women? What do you want from me? You want me to kiss your toes three times a day? Moon around writing love poems? You want diamonds and fur coats and roses, is that it?

ANNIE: No!

AVERY: I'm sorry if I'm not all lovey-dovey every minute of the day. But sometimes I just get this kind of ... do you know what existential dread is?

ANNIE: No.

AVERY: Have you ever read Heidegger?

ANNIE: No.

AVERY: Sartre?

ANNIE: No.

AVERY: Schopenhauer?

ANNIE: (That name sounds familiar at first, but ...) Vh ... No.

AVERY: Well, you ought to. I mean, he talks about how reality is just made up of this blind impelling force, and everyone has this force, and we call it will, OK? But our wills are all contradictory, so we're destined to be miserable. You see?

ANNIE: No.

AVERY: Like right now. I want to be left alone and you want to harass me. So we're both miserable. But it's more than that, even. It's not just other people, you got fate to contend with too. I mean, don't you sometimes get the feeling there's a big cloud over your head and everyone can see it but you, and some day when you least expect it a fist is going to come out of that cloud and bash you one?

ANNIE: No!

AVERY: Open your eyes! You're an optimist, huh? An optimist is just someone who refuses to see what's in front of her. (ANNIE, miffed, starts layering the lasagna into a casserole dish.) How can you go around prattling about gerbils when the world is full of despair? When we have bombs and diseases and banks going belly-up and we can't even hide under our electric blankets anymore or the radiation'll get us! The sky is falling, for Christ's sake, right through the hole in the ozone! Everybody in the Middle East is ready to nuke everybody else and Africa's going to blow up any minute. To say nothing of Central America! You think it's all Tupperware and Twinkies out there? Every time you turn around there's some maniac holed up in a HoJo with an Vzi. I mean, God, how can you go to work every day and read the paper every night and still keep so damn sunny-side up? (She turns away, puts the lasagna in the refrigerator and continues to stand with her back to him.) Oh, don't get all teary-eyed on me again. I'm not attacking you personally. I'm just trying to explain why sometimes I don't feel like being Mr. Happy. For all we know, the whole thing could slide into oblivion tomorrow, and I'll end up on the sidewalk selling pencils and drinking Mad Dog. For God's sake, Annie, doesn't the thought of nuclear winter mean anything to you?

ANNIE: (Defiantly) No!

AVERY: What about Social Security going bankrupt and medical insurance getting sky high and neither one of us getting any younger? You have to wear reading glasses and I have to get my gums flapped and osteoporosis and prostate trouble are waiting in the wings. Doesn't that worry you?

ANNIE: No.

AVERY: Haven't you noticed there's less snow every year? Doesn't global warming bother you at all?

ANNIE: No.

AVERY: The depletion of the rain forest?

ANNIE: No.

AVERY: Recombinant DNA? Alluvial flood plains? What about Tibet? (He's worked himself into a towering rage. A beat, then, in his face:)

ANNIE: No.

AVERY: Dammit, woman, don't you ever think about anything outside yourself?

ANNIE: No! (A beat) Wait a minute. That's not true. I pulled off the road today to look at that gorgeous sunset. Did you?

AVERY: No.

ANNIE: Did you notice the autumn crocuses blossoming under the shrubs?

AVERY: No.

ANNIE: How about the trees on the way home? All russet and amber and

AVERY: No! Dammit, Annie, do you really think that sunsets and rainbows and fuzzy gray kittens can make it all up to the homeless?

ANNIE: No. But do you think grumping around the house will alleviate the crisis in Algeria?

AVERY: No... Wait a minute. There isn't any "crisis in Algeria!"

ANNIE: No? Well, what about the crisis here? And what about me? Does making me unhappy make anything else any better?

AVERY: No! I don't want to make you unhappy. But can't you just ignore me and be happy on your own?

ANNIE: No. Because no matter how happy I am, it makes me unhappy to see you all unhappy. Because I love you. And so I want to make you happy but you just want me to get out of your face. I guess that isn't the way to make you happy, huh?

AVERY: (Softly) No. You weren't really going to leave me, were you?

ANNIE: No. Not unless you want me to.

AVERY: No. I love you too, Annie. Can't you just put up with me?

ANNIE: Maybe. But God, Avery, couldn't you make more of an effort?

AVERY: Maybe. (He goes to her, kisses her.) We could nuke that lasagna a little later, couldn't we?

ANNIE: Yes. (They kiss again. And again. AVERY starts to move them toward the bedroom.)

AVERY: Yes?

ANNIE: Yes.
```

---

## IC-0880: The Odious Ogre

- Title: The Odious Ogre
- Author (byline): Norton Juster
- Work: Not specified
- Publisher: Michael di Capua Books
- Publication date as stated: Sept 2010
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR 1, NARRATOR 2, TOWNFOLK 1, TOWNFOLK 2, TOWNFOLK 3, ODIUS OGRE, NARRATOR, YOUNG GIRL, TOWNSFOLK 1, TOWNSFOLK 2, TOWNSFOLK 3
- Teaser before the introduction: Yes
- Spoken words (computed): 1178
- Already set (do not supply): none

### Source block (context only)

```text
Author: Norton Juster
ISBN: 978-0545162029
Publisher: Michael di Capua Books
Date (Month/Year): Sept 2010
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Fe, Fi, Fo, Fum . . . I smell the blood of an Englishman.

ACTOR 2: That’s not an OGRE, that’s the Giant from Jack and the Beanstalk.

ACTOR 1: (In your best SHRECK VOICE) Oh, yeah, yeah . . . this one is about an ORGRE who, in order to regain his swamp, travels along with a donkey in order to bring a princess to a scheming lord who wishes to become King.

Actor 2: No . . . That’s SHREK – Right species . . different story. This is the story of

TOGETHER: The Odious Ogre by Norton Juster
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Narrator 1 / Young Girl – Female Narrator 2 / Ogre – Male

NARRATOR 1: There was once an Ogre who had a terrible reputation.

NARRATOR 2: Not that Ogres usually have good reputations, but his was worse than anyone could remember – or cared to remember.

NARRATOR 1: He was, it was widely believed, extraordinarily large, exceedingly ugly, unusually angry, constantly hungry, and absolutely merciless.

NARRATOR 2: Nobody, however, could claim to know anything about him for sure. To tell the truth, there wasn’t anyone to be found who had actually made his acquaintance and was still around to talk about it.

NARRATOR 1: Now, the one thing everyone did know for sure was that they could not think of anything to do about him.

TOWNFOLK 1: It’s hopeless!

TOWNFOLK 2: If we try to do anything it will only make things worse!

TOWNFOLK 3: Maybe if we’re nice he’ll only eat some of us.

NARRATOR 1: As you can imagine, no Ogre ever had it so good.

NARRATOR 2: Every time there was even a hint that he was in the neighborhood, people stuffed their ears with stale cake, blindfolded themselves, clutched their knees, and rolled up in a ball under the kitchen table.

NARRATOR 2: Since this is not the most effective defensive posture, the Ogre would wander through the town, making a leisurely buffet of the local population.

NARRATOR 1: For the Ogre, it was quite a relaxing life and, as happens, he grew a bit lazy and self-satisfied, maybe even smug, and definitely spoiled. Everything came so easily for him. He grew to expect it –

ODIUS OGRE: No one can resist me. I am invulnerable, impregnable, insuperable, indefatigable, insurmountable.

NARRATOR 1: He let each satisfying word roll smoothly off his tongue. The Ogre did have quite an impressive vocabulary, due mainly to having inadvertently swallowed a large dictionary while consuming the head librarian in one of the nearby towns.

ODIUS OGRE: What can they do? No one can resist me

NARRATOR 1: That’s the way it was for him. No doubts, no concerns, no worries.

ODIUS OGRE: I am invincible – Absolutely invincible!

NARRATOR 1: One afternoon, as he ambled down the road towards one of the nearby villages in search of dinner, he saw a small cottage way off in the distance that he had not noticed before.

ODIUS OGRE: Maybe I’ll stop for a little snack first

NARRATOR: He lurched down the long narrow track to see what tasty tidbit he might find.

NARRATOR 2: The cottage was deep in the woods, far removed from the busy goings-on of the world, and unknown to the Ogre, his reputation had NOT preceded him.

NARRATOR 1: He paused at the edge of the trees. The cottage was quite pretty. Even the Ogre, who didn’t care much for pretty (it doesn’t taste any better than ugly) was impressed.

NARRATOR 2: Outside the cottage a young girl worked busily in the garden.

ODIUS OGRE: (Sneaks up on young girl – Stomps feet, Roars, Licks his lips).

NARRATOR 2: The trees swayed to the ground. The birds flew off in great confusion and even the cottage seemed to shudder.

YOUNG GIRL: Oh, pardon me. I didn’t realize anyone was there. I’ll be right with you.

ODIUS OGRE: (Looks startled, mouth drops open, hand begin to shake) - [To himself/audience] What’s going on! Why didn’t she just shrivel up and collapse? How dare she treat me this way?

YOUNG GIRL: (Pauses from her work, looks up, smiles) What a nice strong voice you have. But do forgive my bad manners. Please sit down and have a cup of tea. We get so few visitors these days.

ODIUS OGRE: But how can you be so calm? Don’t you know how terrible I am? Haven’t you heard about me? Where have you been, for goodness’ sake?

YOUNG GIRL: Oh, you’re not really so terrible. Overbearing perhaps, arrogant for sure, somewhat self-important, a little too mean and violent, I’m afraid, and a bit missy. But I’ll bet if you brushed your teeth, combed your hair, found some new clothes, and totally changed your attitude you’d be quite nice.

NARRATOR 1: The ogre was now in real distress. His head felt all funny, He just didn’t understand what was happening. This was not the docile dumpling he had expected.

ODIUS OGRE: (To himself/audience) She hasn’t even heard of me. And not only isn’t she afraid of me, I think she likes me! I can’t be liked. It’s bad for business.”

YOUNG GIRL: One lump or two? It’s so nice of yu to drop by. Are you new to the neighborhood?

ODIUS OGRE: NEW! I’m the scourge of the countryside. Your worst nightmare! This is humiliating, so depressing, so unfair, so embarrassing. (Looking around nervously) (Young girl smiles patiently) Maybe it’s a trap. It must be a trap. YES, IT’S A TRAP! She probably has everyone hiding in the bushes, waiting to swoop down on me. Look at her! She’s so confident. If I pounce, she probably knows all kinds of secret, painful ways to stop me. What can I do? How can I live if I can’t ravage and plunder? (To the young girl) I think I should be leaving . . .

YOUNG GIRL: Oh, please don’t leave before you’ve had a muffin. I baked them myself this morning. They’re still warm.

ODIUS OGRE: A muffin! I don’t want a muffin. Muffins are nice, but couldn’t I have surrender?

NARRATOR 1: For the briefest of moments, his thoughts flashed back to delicious memories from his reprehensible life.

ODIUS OGRE: (Re-enact ravaging and plundering)

NARRATOR 1: But only for a moment, for his problem still stood facing him, generously offering her muffins,

ODIUS OGRE: This is not the way it’s supposed to be.

NARRATOR 2: He was sure of that, but what to do? Then suddenly he thought he knew.

NARRATOR 1: In a last desperate attempt to reassert his fearsome presence, he drew himself up to his most menacing height, his eyes slits of determination. He leaped up and hurled himself around the garden – bellowing, stomping, blustering, grimacing, twitching, snorting, belching, clawing, and drooling. When he finished, he stood back exhausted, awaiting her abject surrender.

NARRATOR 2: The girl was overwhelmed. She took a ddep breath, put the muffins down carefully and . . .

YOUNG GIRL: (Applauds) What fun, how magical, how wonderful! Would you consider doing that for the orphans’ picnic next week? I know the children would love it.

NARRATOR 1: The Ogre was stunned. Despair reached to the depths of his shallow soul.

ODIUS OGRE: It’s no use, I’m confounded, overcome, and undone.

NARRATOR 1: He turned and, without a word, began to walk back towards the trees, the scent of the warm muffins still lingering in the air. He had taken only a few steps when he stopped, stood perfectly still for several long seconds, then stumbled back . . . keeled over, and expired on the spot, a look of uncomprehending disbelief covering his anguished face.

NARRATOR 2: When the townspeople heard the news, they all arrived to celebrate and to buy him. But most of them would not dare look at him, since reputations, of course, die harder than Ogres.

NARRATOR 1: As you might expect, some of the less gracious among them wree reluctant to give the girl any credit at all.

TOWNSFOLK 1: He wasn’t that terrible. Anyone could have done it.

TOWNSFOLK 2: She must have had a lot of help.

TOWNSFOLK 3: I could have dealt with him myself, but I’ve been busy.

NARRATOR 2: None of that mattered to the girl. It wasn’t even clear to her what all the fuss was about. She had simply treated the Ogre as she treated every9one else, with kindness, generosity, and understanding.

NARRATOR 1: This was just too frightening for the Ogre to bear.

NARRATOR 2: She also understood that the terrible things that can happened when you come face-to-face with an Ogre can sometimes happen to the Ogre and not to you.
```
