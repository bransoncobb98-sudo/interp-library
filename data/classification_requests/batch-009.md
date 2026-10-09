# Classification request: batch 9 of 53 (40 records, IC-0721 to IC-0760)

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

## IC-0721: Beginning to the End

- Title: Beginning to the End
- Author (byline): Mary Krell-Oishi
- Work: Perspectives: Relevant Scenes for Teens, Pg 91+
- Publisher: Merriwether Publishing, Ltd
- Publication date as stated: March 1997
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: HE, SHE
- Teaser before the introduction: Yes
- Spoken words (computed): 2040
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mary Krell-Oishi
Book: Perspectives: Relevant Scenes for Teens, Pg 91+
ISBN: 978-1566080309
Publisher: Merriwether Publishing, Ltd
Date (Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: *According to the CDC, teen pregnancy rates are the lowest they have been in decades.

ACTRESS: However, some doctors, service providers and advocates are worried.

ACTOR: They site several factors, including intensifying political pushback against sex education and the impact of the COVID-19 pandemic on youth mental health.

ACTRESS: Decades of progress could begin to unravel. Teen pregnancy rates could again begin to rise.

ACTOR: And teens, ill-equipped to make such harrowing decisions about relationships and their futures, will be faced with monumental adult choices.

TOGETHER: Beginning to the End by Mary Krell-Oishi
```

### Performance text (classify this)

```text
(SHE and HE go through their relationship from when it starts to the final moment. Note: They do not speak directly to each other until specified in the script.)

HE: (Pg 91+) I asked her to go out with me about a month ago.

SHE: He's the cutest guy I've ever known.

HE: We hardly ever disagree.

SHE: We feel the same about almost everything.

HE: It's like we think the same thoughts.

SHE: Well, we do have one disagreement.

HE: There is one thing that kind of hangs us up.

SHE: I know he loves me. He says he does. He wouldn't lie about that.

HE: I respect her, I love her, everything. I don't know how else I can make her believe me. I would never hurt her.

SHE: I want to prove to him that I believe him and that I love him. It's just that. . .

HE: I don't know what the big deal is. I mean, I know we'll end up married some day. I feel it in my heart. There's no one else for me but her.

SHE: I feel like I'm disappointing him by holding back. But if I don't, that means I give up everything to him. Not that I don't want to. I do. But I don't know if I'm ready now. Not yet.

HE: I know that I'm ready. I think she is, too, but I think she's got some "social hang-up" about it. Like she's worried about what people will think. She should only be concerned about us, not anyone else. It's us that's important.

SHE: He is the most important thing to me. Maybe I'm just being silly.

HE: Not that I'd break up with her over this, but it's frustrating.

SHE: I just love him so much. I do. Maybe saying it isn't enough.

HE: She called me and said she wanted to see me.

SHE: I've thought a lot about it.

HE: She said it was important.

SHE: So, I made up my mind.

HE: She said it would be something special.

SHE: I want it to be special.

HE: I wonder. . . I hope. . .

SHE: Words just aren't enough.

HE: I love her. She must know that. We are as close as two people can be.

SHE: We share such a special experience. No one else will ever have that part of my soul. I feel like I could fly.

HE: This is what love is. I would do anything for her.

SHE: He walks into the room and my heart skips a beat. He fills the room with his light.

HE: Forever. Things will always be like this between us.

SHE: I feel different.

HE: Things will never change.

SHE: Things aren't right.

HE: She's been acting kinda funny lately. She's so moody.

SHE: I feel like crap.

HE: What's her problem? Everyday she's in a mood. It's getting old.

SHE: Something's just not right. Not with me, not with us.

HE: I'm getting really tired of her attitude lately.

SHE: I've been so moody lately. I don't know what's wrong.

HE: Things are still good, you know, between us. But other stuff, just talking and all, that's not so good. It's like we have nothing to say to each other without it turning into a disagreement. Not really a fight, but bickering. And it's not my fault. It's her.

SHE: He picks on me. No matter what I do or say, he has to comment on it. And I'm crying all the time lately. And when I cry I get "nerve-hungry" so I have to eat. I've probably gained five pounds.

HE: I don't know what her problem is, but it better stop. At first the tears were kind of cute, but now it's just old.

SHE: I'm tired of crying.

HE: She better snap out of it.

SHE: I'm so tired all the time.

HE: She's getting to be such a drag to be around. She's always tired.

SHE: Maybe I need vitamins or something.

HE: She said she needs to be alone for a couple days.

SHE: I need to think things through.

HE: Alone. Alone alone, not together alone. I can feel that things are not right.

SHE: I can't shut him out now. I need him.

HE: She's shutting me out. Maybe she's found someone else.

SHE: I need him to be there.

HE: If she's tired of me, fine. Hey, whatever.

SHE: I'm going to tell him today.

HE: She said she wanted to see me today. I wonder if this is it. The end. After the way she's been for the last few weeks, that would be fine with me. I don't need the moods.

SHE: I need for him to be strong. To be understanding and loving. I need to talk to him soon.

HE: She called me last night to ask me to meet her before school starts. I guess that means we're cutting morning classes. Hmmm. This doesn't sound good.

SHE: I asked him to meet me before school, that way we could skip classes and be alone.

HE: I don't like cutting classes. Not when we're this close to graduation and I have a good chance at a scholarship. This better be important.

SHE: Some things are just more important than school right now, you know?

HE: She says she "needs to talk." That can only mean trouble.

SHE: I need to talk to him. It's serious, you know. . .

HE: I know this is going to be something serious. Some really serious stuff.

SHE: I'm worried how he'll take this.

HE: I mean, what's the worst it could be?

SHE: This is the worst thing that could happen. I thought we were so careful.

HE: She's pregnant. Pregnant.

SHE: I'm pregnant.

HE: What a weird word. Say it out loud. Pregnant. It's not a word that is easy to say.

SHE: Pregnant. Try saying it fast five times without gagging. I guess it's not so hard when you're not the one who's in the condition.

HE: What does she want from me?

SHE: What are we going to do?

HE: She said she was on the pill.

SHE: I started the pill. But I guess I was too late or missed a day or something. I never needed it before because I never did this with anyone before.

HE: She told me there wouldn't be a problem.

SHE: I didn't think that this could happen to someone like me.

HE: I can't believe this is happening.

SHE: I'm so scared.

HE: My life is shot to hell.

SHE: What am I going to do?

HE: She's so irresponsible.

SHE: He's so angry.

HE: I feel like I've been betrayed.

SHE: The look in his eyes. I will never forget that look.

HE: OK, think. What am I going to do?

SHE: It's not like I planned for this to happen.

HE: This was definitely not in my plans.

SHE: He just looked at me and walked away.

HE: I didn't know what to say to her. I still don't.

SHE: He walked away.

HE: I just walked away. I mean, I'm going to call her and talk about what she is. . .we are going to do.

SHE: He called me last night. He sounded so distant.

HE: I could hardly talk to her. I'm so mad.

SHE: I didn't do this alone, you know.

HE: This is so wrong. I have plans. I'm going to college, I got a great scholarship.

SHE: He acts like he's the only one who's affected by this.

HE: I can't just give it all up.

SHE: This is my life.

HE: She can't expect me to give everything up.

SHE: I'll have to give everything up.

HE: I won't be an adult when I haven't had time to be a kid.

SHE: I'm so scared.

HE: Why did this happen?

SHE: What if he never calls me again?

HE: I have to call her and get this settled.

SHE: He said he loved me. Was that a lie?

HE: I do love her. But, I mean, maybe she's not the right one.

SHE: He told me that he'd always be there for me. Always. I thought he was the right one.

HE: I guess I was wrong.

SHE: What am I going to do?

HE: What does she want me to do?

SHE: Will I have to quit school?

HE: I'll have to give up college and get a job.

SHE: College is out.

HE: I'll probably have to marry her.

SHE: How can I have a career and a baby?

HE: I could join the army, I guess. That way I'd get paid and could save for college.

SHE: I don't want to do this.

HE: My parents are going to flip out. . .

SHE: I can't have a baby.

HE: . . . but, maybe if I tell them about it in a way that shows them I'm handling it. Show them that I can take care of things.

SHE: I don't want a baby, not now.

HE: It could work out.

SHE: He doesn't want it either. Look how he acted.

HE: I'll call her tonight.

SHE: I am totally alone in this.

HE: Maybe she'll go away and have the baby and then we can figure something out.

SHE: I am on my own. He's made that crystal clear.

HE: She wasn't home. Her mom said she was over at Angela's house spending the night. But I went over there and no one answered the door.

SHE: I need to think this through.

HE: I'll see her at school later. Tell her that, even though I am not happy about all this, I will take care of my responsibility.

SHE: It's my responsibility. It's my body.

HE: She wasn't at school and when I called her at home, no one answered. What is going on?

SHE: I feel like I'm dying inside.

HE: Where is she?

SHE: I made an appointment for the clinic for this afternoon. Angela said she'd go with me. I suppose I should tell him, but why?

HE: What is she doing?

SHE: When I first told him what was going on and he walked away, he walked out on me, on the situation, on everything I ever put my trust in.

HE: Angela told me that she was going to the clinic with her.

SHE: I can never trust him again.

HE: She can't do this.

SHE: (She faces him) It's my life.

HE: (He faces her) It's my baby, too.

SHE: You should have thought of that before you walked away.

HE: What did you expect me to do? I was shocked. It wasn't what I expected.

SHE: Funny, I said the same thing to myself as I watched you leave.

HE: You can't do this.

SHE: Try and stop me.

HE: But I love you.

SHE: Well, you have a helluva way of showing it.

HE: If you're doing this to punish me, it's the wrong way. I don't want you to do this.

SHE: Oh, really? So, you're ready to give up college, get married, pay bills, have a mortgage, and create a world for a child to live in? You're ready for all that, huh?

HE: No, I'm not ready. But there's really not much choice now, is there?

SHE: (Quietly) Yes, there is a choice. And it's my choice.

HE: Don't do this.

SHE: I have to.

HE: I told you, things will work out.

SHE: How? You join the army, travel around, save money, you go to college, you have your life.

While I stay home and have the baby and find out in ten years that you don't love me enough to stay with me or the child after all? I'll be under thirty, with a ten-year-old and no future. Is that your plan for me?

HE: How can you say that? I love you. You know I do.

SHE: I thought you did. But you loved a little girl who thought the sun rose and set on you. Well, in the last few weeks I've had to grow up and make some hard choices.

HE: What about my choices?

SHE: You have none.

HE: I can't believe you would do this.

SHE: I can't either. But I am. And I will have to live with it.

HE: We're through, then, if you do this.

SHE: (A long look) We were through anyway.

HE: At least let me go in with you. We can talk to someone, a counselor. There are other options.

SHE: I've talked to the counselor. I am being set up with a good family.

HE: What?

SHE: I'm meeting with the family today that will adopt the baby.

HE: Adopt? You mean you're not having an abortion?

SHE: An abortion? No! How could you think I would do that?

HE: But. . . I just assumed.

SHE: How could you think that? Don't you know me at all?

HE: I guess I just thought that. . .

SHE: Thought what? After all this time we've been together, you actually believed that I could have an abortion?

HE: I'm sorry, I. . .

SHE: Go away, please.

HE: No. I need to be a part of this.

SHE: Why?

HE: I don't know. I just do.

SHE: This is my decision, you know. You have no choices in this.

HE: I know.

SHE: Then why do you want to be there?

HE: I just want to be.

SHE: OK. (He starts to put his hand on her back to guide her in. She quietly responds to his touch without anger, just very matter of fact) Don't touch me.

HE: Sorry.
```

---

## IC-0722: Beirut

- Title: Beirut
- Author (byline): Alan Bowne
- Work: Duo!: The Best Scenes for the 90's : Scenes for Two
- Publisher: Hal Leonard Corporation
- Publication date as stated: 1995
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TORCH, BLUE
- Teaser before the introduction: No
- Spoken words (computed): 1290
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alan Bowne
Book: Duo!: The Best Scenes for the 90's : Scenes for Two
ISBN: 1557830304
Publisher: Hal Leonard Corporation
Date(Month/Year): 1995
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Torch has tested positive for the AIDS virus and has been quarantined with other “positives” in the Lower East Side of Manhattan, which is patrolled by guards and fenced off from the rest of the city. Torch has been tattooed with a decal proclaiming his status as a “positive”.

ACTOR: Blue is in love with him and sneaks past the guards to visit him. To escape detection, she has had a false decal pasted to her body so that she will appear to be a “positive,” too.

TOGETHER: Beirut by Alan Bowne
```

### Performance text (classify this)

```text
TORCH: What if you die from it, Blue? And I gotta live with that?

BLUE: Come over here.

TORCH: Answer me!

BLUE: Come over here and I’ll tell you.

TORCH: Tell me from there! I wanna hear this. How I can sit here and watch you shrivel up like a raisin. Sit here and watch you lose like 50 pounds in 24 hours. While your head! Puffs up! To twice its size! And that I done it to you. This I wanna hear. (Beat)

BLUE: You want pizza? You got pizza. With this decal I can sneak out and sneak in. You want stickball? You got it. Wanna get drunk? Wanna nice t-shirt? It’s all yours. And if one of us starts to die? Then a light meal, and a glass of wine. (Beat as he stares at her) We could go to sleep in each other’s arms.

TORCH: (Staring) You gonna get serious? Or what?

BLUE: I am serious.

TORCH: I could really see this. Oh sure. You and me playin house in here. On Sundays we take a little stroll inna park. You seen Tomkins Square lately? It’s where they pile the bodies. And burn ‘em on Sundays. We could walk around, sniffin the fresh air. We could watch the people who can’t control themselves? Squattin in the gutters. Or! We could go to the Laundromat on Avenue A? And watch people trying to unglue the t-shirts from their sores to wash ‘em. It’s the American dream!

BLUE: I usta think that too.

TORCH: Think what?

BLUE: That life was over here, and death was way over there. That they don’t mix. But now? They’re joined at the hip.

TORCH: What we need here! Is some adult maturity!

BLUE: It’s a lovely thing you’re feelin for me. How you don’t wanna infect me and all? But that’s just ridiculous, all right?

TORCH: I ain’t lissenin no more!

BLUE: Because I got two choices. First, I can live without risk and feel dead. Or second? I can risk death and feel alive. I would not be the woman who fell for and idiot like you if I would choose the first..

TORCH: Suicide! Is a sin! It’s anti-nature. Un-Italian! And non-American! (Beat)

BLUE: You had a choice about getting this disease? Or you had one word to say about one thing that has happened to you in your whole life, including you got born? No. it was always other people or god or somebody else that made your choices. You ain’t owned one minute of your life. Torch. But that moment you die? You can choose it. You can choose when, you can choose how. You own it, Torch. You don’t wanna give me a baby? O.K. Then give me that moment. That moment when we die. It will belong to us, Torch, and to nobody else. (Beat) All I’m sayin, is it don’t have to be a sin!

TORCH: You end up in hell!

BLUE: Oh my god! (Looking about in mock-terror at the sleazy room) How will be handle it?

TORCH: Shut up! And go home.

BLUE: So. That’s settled. I’m gonna get curtains for in here. And as for that guard? I know what to do about him. Got the idea from this TV program they showed the other night, NBC, coast to coast, about plagues like in Europe hundreds of years ago? This was supposed to make us. Feel better? I dunno. Anyway, they told how the people who got the Black Death? A more Christian disease than what we got now, I mean you died in a matter of mere days. How these people who caught it got very pissed off about the ones who didn’t catch it. So the sick ones would sit by their front windows until well person passed by on the street? And then suddenly reach out! Grab them! And breathe into their faces! People. Never. Change. (Beat; chuckling). So that’s what I’ll do to that guard. When he comes by, I’ll ask him to come closer. And then breathe on him!

TORCH: This thing here is not airborne! It’s a fluid transmission only!

BLUE: Thank you, doctor. So I’ll spit on him! We can always scare him off, scare him so bad he’ll stop bothering us. There’s power in being sick, Torch! (Beat)

TORCH: Blue?

BLUE: Yeah? Come here. I want you to look. In the candlelight? There’s these little specks floatin in the air. Little animals just waiting. TO kill off the things that get weak. They float and turn and dance in the light. Come on. Look.

TORCH: No.

BLUE: O.K., so here comes a microbe! (She approaches TORCH with mock menace)

TORCH: Stop it!

BLUE: I’m a germ! I’m gonna kill you!

TORCH: You cant’ do this!

BLUE: Call out the National Guard!

TORCH: You gonna haveta do this, Blue, all by yourself. (Big, emphatic) It ain’t. My. Responsibility! (Beat)

BLUE: You wimp of a cop-out!

TORCH: Huh?

BLUE: I bet you been telling that to girls. Your whole life!

TORCH: What is that suppose to mean?

BLUE: Men? Are worthless!

TORCH: Who?

BLUE: Always like – (Sarcastic macho mimicry) She begged me for it! Wadn’t my fault if she got hurt! Stupid chick! I can just see you! If I come down with this? You gonna be crawlin around here goin. It wadn’t me. She asked for it. I was just this. Innocent bystander!

TORCH: Jesus, I never met such a hypocrite! So we won’t do it! So get outa here!

BLUE: You say it.

TORCH: Say what?

BLUE: That you want me! (Beat) That what you feel, I gotta feel. That what I gotta face, you gotta face. (Beat)

TORCH: You are some kina fool. Some kina magazine. Like Modern Romance, like Teenage Love, like -- How’d I ever fall in love with you? In the middle! Of a disease????

BLUE: Piss on this love you got! I don’t want excuses here, Torch.

TORCH: So what do you want?

BLUE: I want you to be with me. And never leave (Beat)

TORCH: I get it. You want my soul, right?

BLUE: That’s right

TORCH: Typical woman.

BLUE: That’s right

TORCH: Sex ain’t enough for you, hey?

BLUE: Good-bye. (Contemptuously)

TORCH: How can this be? You love somebody and don’t wanna give ‘em a disease? And that makes you this. Sonofabitch?

BLUE: Pre-plague? You woulda said, Hey you! You getting’ all hung-up and hurt here? So it’s your own fault, you idiot!

TORCH: It’s not the same!

BLUE: It’s the same. (Rummages in her purse and throws packs of cigarettes at him) Here’s some extra cigarettes. And somewhere. In here. I brung you a mars bar.

TORCH: Under your thumb, that’s where you want us. In a cage which only you got the key! Well, lemme tell you, with a guy? It’s different! He wants a good time, a few laughs, and then. He wants. To go out. And play some pool! (Beat)

BLUE: What. Are you talking about?

TORCH: We’d be trapped here! Lookin for spots on each other alla time. I can’t live with you, Blue, in some kina romatic magazine. Even if I forget and drink outa the same glass as you? Much less bee with you? I would hate myself.

BLUE: Guys always do.

TORCH: Do what?

BLUE: Hate themselves after having sex. You guys can have this 4th of July experience with a woman and still feel like total crap afterwards. What is that?

TORCH: You keep changing! The subject!

BLUE: The subject! Is you are afraid!

TORCH: What? I don’t wanna murder you! Is that O.K.?

BLUE: No, I won’t accept that.

TORCH: It’s the truth!

BLUE: I gotta go.

TORCH: What, I’m some kina wimp! Cause I don’t wanna fill you with parvoviroids?

BLUE: Stop all this virus mumbo! What you don’t want. Is me. A human being on your hands who might feel pan. Or make a demand. Or need you when there’s nothing left. (Beat)

TORCH: That! Is totally. And complete. Bullshit!

BLUE: Torch, I didn’t risk my life to come here for a visit! I came to live with you, maybe even to die with you. I didn’t know what I’d find. Would your skin be smooth and white, like before, or would you be covered with sores? I didn’t know. And I didn’t care (Beat)

TORCH: (Pleading) Blue - -

BLUE: Fine . . . . . Die alone.
```

---

## IC-0723: The Bell Witch

- Title: The Bell Witch
- Author (byline): Rachael Carnes
- Work: The Best Ten-Minute Plays 2022, Pgs 29-38
- Publisher: Smith and Kraus
- Publication date as stated: Aug 2022
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, SETTING, JOHN, LUCY
- Teaser before the introduction: Yes
- Spoken words (computed): 1650
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rachael Carnes
Book: The Best Ten-Minute Plays 2022, Pgs 29-38
ISBN: 978-1575259659
Publisher: Smith and Kraus
Date (Month/Year): Aug 2022
*Source information for introduction
https://tnmuseum.org/junior-curators/posts/tennessee-legends-the-bell-witch?locale=en
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: On the banks of the Red River in Robertson County lies the sleepy town of Adams, Tennessee.

ACTRESS: With a population of 624, you might think that the area would get overlooked. But for decades the town has captured the attention of ghost hunters and historians from all over the world.

ACTOR: Why? Because it is the site of the infamous haunting of the Bell Witch.

ACTRESS: According to legend, from 1817 to 1821 a man named John Bell and his family were harassed by this invisible spirit who had the ability to speak, shapeshift and be in multiple places at once.

ACTOR: Return with us to 1817 and experience this legend through

TOGETHER: The Bell Witch by Rachael Carnes
```

### Performance text (classify this)

```text
CHARACTERS: JOHN BELL, a farmer; LUCY, his wife.

SETTING: Northern Robertson County, Tennessee. (1817)

NOTE: Imagine JOHN and LUCY'S children are here, too, witnessing.

Dim candlelight casts a pall on a wooden table, where LUCY dishes up thin stew for her husband JOHN, and their children.

JOHN: (Pg 29-38) The harvest being brought in, let us pray.

LUCY: John --

JOHN: Our father who art in heaven, we bless thee for this thy bounty.

LUCY: The children said they saw it again.

JOHN: For which we are about to receive --

LUCY: Out by the well --

JOHN: Now, my dear Lucy, this here's the richest farmland in the Red River Valley.

LUCY: Wolf with no head, John? In the woods --

JOHN: You'll scare the young uns. Let's to supper now.

LUCY: Cat with blazing eyes out by the shed. Goat on its hind legs --

JOHN: That's enough! How'd it look for a deacon in the church, his wife consortin' with --

LUCY: We both been hearin' the knockin' sounds 'round the walls.

JOHN: Branches -- Wind. Don't worry, children --

LUCY: Last night I heard the knocks inside. Right by my bedside. Three still, loud knocks, like this.

JOHN: Your mother ain't felt right since we lost your baby brother.

LUCY: I been hearing it: Sounds like rats chewin' the bed post? Chains drug through the house.

JOHN: Let's all pray for poor little baby Benjamin, rocked in his cradle by the Lord Jesus in heaven.

LUCY: I'm cooking this supper and I hear what sounds like a stone dropped on the floor beside me --

JOHN: That vicious fever took a piece a' your momma with it --

LUCY: I look down at the floor and I don't see nothin' but wooden planks. Then I hear a chokin' sound.

JOHN: She'll be right as rain soon, just needs her rest.

LUCY: I'm standing and stirring the pot and I hear these walls gulping for air?

JOHN: It touches a mother's heart, to lose her child. Burns her, like a hot poker.

LUCY: John! This has gone on for a year now.

JOHN: No, it ain't! We enjoy a quiet, peaceful life.

LUCY: The children are terrified! Betsy saw some kinda creature --

JOHN: Betsy's been reading those storybooks again. I told you --

LUCY: And Drewry hears wings flapping against the ceiling over his bed. They all do --

JOHN: A sparrow, a bat gets in is all -- What'd you expect? This here's the country. Fresh air!

LUCY: John, we need help.

JOHN: Bring more shame on this family? No, thank you. I am an upstanding man.

LUCY: We could just ask the neighbors, if maybe they've --

JOHN: Your frailty as a wife and mother cripples this house, but I refuse to let you ruin my reputation.

LUCY: You'd have our babies listen to the creaks and cracks -- The walls chokin'?

JOHN: Children: You must pray now to Jesus that your mother be delivered from this seditious fantasy.

LUCY: Joel's been struck. Richard William's had his hair pulled. Look at their bruises -- their cuts!

JOHN: Kids! They fight.

LUCY: They was just standing there. Just today, I saw Jesse fly across the room, no hand laid upon him!

JOHN: If this "spirit” is so malicious, why you don't have a scratch on you?

LUCY: Because she --

JOHN: "She?"

LUCY: Yes, she. It be a woman, John. Wronged. Buried out there in those woods --

JOHN: Children, go to bed.

LUCY: She shakes 'em in the’ sleep! Pulls their covers down -- puts icy fingers between their sheets!

JOHN: I don't want them to see their momma get a whoopin’.

LUCY: She hurts the children, but when I was sick with fever, she come to me. She tend me in my hour.

JOHN: John Junior, you go get a switch for me to use -- Rest of you, bed.

LUCY: I'm burnin' up, she cools my head with a wet cloth, she sings a little?

JOHN: I gotta drive the devil outta you.

LUCY: She says give her what she wants -- Or she'll stay here forever.

JOHN: And what does she want? Hmm? She want my sweat? My toil?

LUCY: She wants our land, John. JOHN Well, she can't have it.

LUCY: And she wants her tooth back.

JOHN: Excuse me?

LUCY: I am a Spirit; I once was happy, but I have been disturbed and made unhappy.

JOHN: What's wrong with you? Your voice is -- stop it right now!

LUCY: I am the Spirit of a person, buried in the woods nearby. My shallow grave's been disturbed --

JOHN: Ain't no grave out there.

LUCY: I'm disinterred and scattered.

JOHN: The dog's been bringing deer bones is all --

LUCY: One of my teeth -- this one -- is lost under the house. You seen it?

JOHN: Lucy Williams Bell! I will have no more of these incidents.

LUCY: I'm lookin' for my tooth.

JOHN: Now, Junior, that's a good boy, a fine piece a willow. Give it to your papa.

LUCY: And after I find my tooth, I'm gonna kill you.

JOHN: I got a switch in my hand now and so help me I will --

LUCY: But I'm not gonna do it quick.

JOHN: John Junior, you take your mama's arms. Hold for me -- She ain't well, son.

LUCY: I'm gonna keep pinching, scratching, poking you and yours with pins --

JOHN: Stop talking like that.

LUCY: How'd you get that nick on your chin, that abrasion, on your hand? Looks infected.

JOHN: Farm work -- Digging and plowing and -- Dirt gets in.

LUCY: You can't remember where those wounds come from, 'cuz it was me made you bleed.

JOHN: Your mind ain't right. Not since we left your people. I knew you couldn't do this.

LUCY: I'm gonna make it so you got a crowd gathered 'round your humble abode day and night.

JOHN: People warned me 'bout you. They said you was high hat -- City slicker. They was right!

LUCY: People will bring a picnic, wear they Sunday best, and steal a little dirt from outside, as a memento.

JOHN: No one's gonna hear about nothin. Your embarrassment stays within these walls.

LUCY: Suit yourself. I'll just set to swelling your throat. Make it dry and parched.

JOHN: I need some water --

LUCY: At first, you will. Then after a while, it'll feel like you got a stick sideways in your throat.

JOHN: Junior, you may be inclined to look away. But there's sense in a man learning his obligations.

LUCY: You hit me, and I will weaken your muscles and break your bones, from the inside out.

JOHN: Ow -- I -- Can't, stand. I feel --

LUCY: Dizzy, John? Sit a spell. With no one around, Kate's got all the time in the world to poison you.

JOHN: Kate? Who's Kate?

LUCY: Buried out in the woods, all these years. My body left unattended.

JOHN: We're God-fearing folk. We're a good, decent family.

LUCY: But you're not a good man, John. Sign the deed to this farm -- Knowin' what happened here?

JOHN: Nothin' happened.

LUCY: Sign the papers in a backroom. Your loving wife waiting. Were you gonna tell her, about the --

JOHN: Nothing will happen! That's what the man said. It's all in the past!

LUCY: A woman died here, John. Walking by herself, collecting herbs. Men set upon her then slit her --

JOHN: All I did was buy the land! So I could start a family, and build the farm --

LUCY: Build the farm on the backs of your slaves.

JOHN: I heard them in their quarters, complaining about a wolf with no head -- So I beat 'em.

LUCY: The whip's your way, ain't it, John? Well, Kate's gonna see to that. Drop by drop.

JOHN: She can't. She ain't real. Lucy -- This is my last warning.

LUCY: A little pinch of arsenic in your water, a drip of cyanide in your stew. You won't see it or feel it.

JOHN: My darlin' Lucy --

LUCY: Until one day, your hair's fallin' out, your liver's rot.

JOHN: I don't want to hurt you.

LUCY: I see you in the pulpit, on Sundays. Deliverin' your sermon: Starch white collar --

JOHN: The Lord is my shepherd --

LUCY: 'They'll come for me -- With their torches, their dogs.

JOHN: I shall not want.

LUCY: Funny thing, a mule.

JOHN: He leadeth me --

LUCY: Mistreat it, and they, say it looks for an opportunity to seek its revenge.

JOHN: He anointeth my soul --

LUCY: That mule remembers getting hit, punched. Remembers being scolded.

JOHN: Now I walk in the valley of good and evil --

LUCY: That mule looks for a moment when he can kick you in the head. Oops --

JOHN: My throat's -- I can't.

LUCY: Breathe?

JOHN: Stand --

LUCY: Bones, John? Like this one, under the table -- Or this one, next to chair?

JOHN: Those are just -- The stupid dog. Lucy! I love you.

LUCY: Name's not Lucy. It's Kate. Those men that set upon me used my body and didn't bury deep --

JOHN: That's in the eyes of God!

LUCY: When your wife told you I was talking to her, did you listen?

JOHN: She was tellin' tales. She ain't never been right.

LUCY: She's hangin' clothes or beatin' the carpet and she's hearin' voices and -- You know who it is.

JOHN: You shouldn't a been walking alone. It's your fault those men --

LUCY: Those men knocked my tooth loose. One of 'em put it in his pocket as a souvenir.

JOHN: I don't know nothing about your tooth.

LUCY: Wiped the blood on his boots and went home to his wife and children.

JOHN: I never seen it.

LUCY: John, lying makes you ugly.

JOHN: I'm a good man. A respectable citizen.

LUCY: I been trying to warn you. Trying to get you to pay some attention. But you can't see. You know my missing tooth was all bundled up in the deed you signed. You bought the land from the man that murdered me. You know it was him, 'cuz you saw him do it. Stood there. Watched him have his way -- And slit my throat. Then y’all freeze like school girls. What now?

Dig a pitiful shallow empty, leave my body -- swear a pact. And when people go lookin for me? The finest men in the county haven't seen nothin. Except my molar, you keep here on the hearth.

JOHN: I'm a sinner.

LUCY: I'm gonna finish you off. But first, I'll make sure you're the laughing stock of the county.

JOHN: I'll repent!

LUCY: Too late.

JOHN: I'll get the neighbors -- I'll drive you away.

LUCY: You can try, but I'll wander restless tormenting you and your children until the day that you die. (Beat) More stew, John?

JOHN: Lucy -- Your voice.

LUCY: What is it, dear?

JOHN: You sound like yourself again. You feel okay now?

LUCY: Maybe.
```

---

## IC-0724: The Best Christmas Pageant Ever (Play)

- Title: The Best Christmas Pageant Ever (Play)
- Author (byline): Barbara Robinson
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Aug 2009
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, BETH, CHARLIE, MOTHER, FATHER, LEROY, NARRATOR, IMOGENE, GLADYS, ELMER, MRS. SLOCUM, CLAUDE, RALPH, OLLIE, ALICE, REV. HOPKINS, MAXINE, MRS. MCCARTHY
- Teaser before the introduction: Yes
- Spoken words (computed): 1541
- Already set (do not supply): none

### Source block (context only)

```text
Author: Barbara Robinson
ISBN: 978-0573617454
Publisher: Samuel French, Inc.
Date (Month/Year): Aug 2009
```

### Introduction (context only: never use it for content warnings)

```text
Actor 2: The Best Christmas Pageant Ever Actor 1: by Barbara Robinson.
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles:

ACTOR 1: Beth, Mother, Leroy, Elmer, Mrs. Armstrong, Claude, Ralph, Ollie, Maxine, Mrs. McCarthy

ACTOR 2: Charlie, Father, Imogene, Gladys, Narrator, Mrs. Slocum, Alice, Rev. Hopkins

BETH: (Pg 1-3) The Herdmans were the worst kids in the whole history of the world. They lied and stole and cussed their teachers and took the name of the Lord in vain. There were six of them - Ralph, Imogene, Leroy, Claude, Ollie and Gladys - and they went through the Woodrow Wilson school like those South American fish that strip your bones clean . . . Stealing things and whamming kids . . . it was hard to get away from them. There was only one safe place.

CHARLIE: (offstage, singing happily and at a fast upbeat pace) Sweet hour of prayer, sweet hour of prayer, Because there are no Herdmans there. And Jesus loves us, as they say, Because he keeps them miles away. *

BETH: That's my little brother, Charlie.

MOTHER: It's a very practical sentiment. Charlie was black and blue all last year because he had to sit next to Leroy Herdman in school.

FATHER: Is he the worst one? Leroy? CHARLIE. They're all the worst one. Gladys isn't big, but she's fast, and she's mean, and she bites. Stay away from them. Go to church.

MOTHER: I'm glad to hear you feel that way. No arguments this year about the Christmas pageant.

CHARLIE. I don't want to be in it! Nobody wants to be in it!

BETH: (Pg 5) Our Christmas pageant isn't what you'd call four-star entertainment. It's always the same old Christmas story with the same old Mary and Joseph . . . The Herdmans . . . That was Charlie’s fault.

CHARLIE: (Pg 8-9) Hey, Leroy, you give me back my lunch!

LEROY: Sure, kid, here. (hands him a lunch bag)

CHARLIE: (looks inside) You stole my dessert again! You know what? I don't care if you steal my dessert. I get all the dessert I want in Sunday school.

LEROY: (interested in this) Oh, yeah? What kind of dessert?

CHARLIE: All kinds. Chocolate cake and candy bars and cookies . . .

LEROY: You're a liar.

CHARLIE: . . . and ice cream, and doughnuts and cupcakes!

LEROY: (pause) ... Sunday school, huh?

NARRATOR: That was the wrong thing to tell Herdmans . . . and, sure enough, the very next Sunday there they were in Sunday school, just in time to hear about the Christmas pageant...

MOTHER: Today we're going to decide who will play the main roles in our Christmas pageant. (Pg 11-12) Now I want you to think about Mary . . . She was quiet and gentle and kind. The girl who plays Mary should be that kind of person. Who would like to volunteer for that part? (Imogene raises her hand) Did you have a question, Imogene?

IMOGENE: No, I want to be Mary . . . and Ralph, over there, he wants to be Joseph.

MOTHER: (taken aback) Oh. Well . . . I’ll just make a list of volunteers and then we’ll all decide who it should be. Now, who else would like to be Joseph? Raise your hands . . . please . . . any volunteers . . . (silence) Very well. Ralph Herdman will be our Joseph. Imogene has volunteered to be . . . (tiny break here, as if she can hardly bear to connect Imogene with Mary) . . . Mary. Janet? . . . Roberta? . . . . Alice? (silence)

GLADYS: What’s left?

MOTHER: (reluctantly) The Angel of the Lord . . .

GLADYS: I’ll be that. What is it?

MOTHER: (Pg 18-19) (Quoting scripture) And lo, the Angel of the Lord came upon them, and the Glory of

GLADYS: (Flinging her arms out) Shazam! . . . Out of the black night, with horrible vengeance, the Mighty Marvo . . .

MOTHER: This is the Angel of the Lord, who comes to the shepherds . . .

GLADYS: Out of nowhere, right? In the black night, right? Shazam!

ELMER: (Pg 13) (raising his hand) I don’t want to be a shepherd . . . Gladys Herdman hits too hard! ***** (phone conversations) ******

MRS. SLOCUM: (Pg 14-15) Vera? Irma Slocum. I just heard that Imogene Herdman is going to be Mary in the Christmas pageant, and I ... all six of them? MRS. ARMSTRONG. Imogene Herdman! ... What kind of a child is that to be Mary the Mother of Jesus? If I’d been around this never would have happened!

MRS. SLOCUM: . . . better nail down the church and lock up the silver service and hide the collection plates before they clean them out . . . *****

MOTHER: (mimicking Mrs. Armstrong) “If I’d been around, this never would have happened!” I'm going to make this the best Christmas pageant ever, and I'm going to do it with the Herdmans! After all, they raised their hands and nobody else did . . . ***** (pageant practice) *****

MOTHER: (Pg 24-25) . . . Music . . . . Shepherds . . . Music . . . Wise Men! (3 Herdmans slouch aimlessly down the aisle and up to the manger)

IMOGENE: (Pg 19) Well, it's about time somebody important showed up! If they're kings, they can get the baby out of the barn, and tell the innkeeper where to get off!

MOTHER: (ignoring this turn of plot) ... They were sent by Herod, who was ... well, he was the main king, and he wanted to find Jesus and have him put to death.

IMOGENE: My God! He just got born! They're gonna kill a baby?

MOTHER: Herod isn't in the play.

LEROY: He’s out to kill the baby, and he isn’t even in the play?

CLAUDE: (Pg 20) (warming to this scenario) No . . . I know ... Joseph gets the shepherds together and they go wipe out Herod! (He makes a machine gun gesture.)

IMOGENE: And I run away with the baby till the fight's over!

RALPH: Somebody ought to fix the innkeeper . . . Gladys, you wipe out the innkeeper!

GLADYS: (Pg 21) (happily) Yeh! ... Zap!

OLLIE: What's the name of this play?

GLADYS: I know a name! . . . I know a name! I'd call it . . . Revenge at Bethlehem!

BETH: Revenge at Bethlehem! The Herdmans thought the Christmas story came right out of the F.B.I. files! At least they picked out the right villain- it was Herod they wanted to gang up on and not the baby Jesus. (As the Wisemen approach IMOGENE holds up the doll by the back of the neck, waving it in the air.)

IMOGENE: (Pg 25) I've got the baby here . . . don't touch him! I named him Jesus!

MOTHER: (hurrying on stage) No, no, no! You don't say ... (nerves fraying away) ... anything! Mary doesn't say anything. No one says anything! Mary and Joseph make a lovely picture for us to look at while we think about Christmas and what it means! ... Now, put the doll back.

IMOGENE: (disgruntled) I don't get to say anything . . . some angel tells me what to call the baby . . . I would have named him Bill.

GLADYS: (Pg 26) (yells at the Shepherds) Unto you [Bill] is born!

IMOGENE: Unto me! Not them, me! I'm the one that had the baby!

RALPH: (Pg 17) (Not so much trying to shock, as he is pleased to understand something.) Pregnant! She was pregnant! (There is much giggling and tittering.)

ALICE: It's better to say 'great with child'. I'm not supposed to talk about people being pregnant, especially in church. ****** Scene ******

REV. HOPKINS: (Pg 28-29) The whole church is in an uproar. Jesus said, "Suffer the little children to come unto me", but I'm not sure he meant the Herdmans . . . Don't you think we should cancel the pageant? Every one seems to think it's going to be a . . . a . . .

MOTHER: Disaster? (Obviously, that's the word he had in mind.) Well, they're wrong! ... It's going to be the best Christmas pageant we ever had!

REV. HOPKINS: But . . . I don't think anyone will come to see it!

BETH: I didn't think so, either, and neither did Charlie . . . but we were wrong. On Christmas Eve the church was jammed full. Everybody came . . . to see what the Herdmans would do. ***** (the night of the pageant) *****

MOTHER: Oh, I don't have any idea what's going to happen tonight! We've never once gone through the whole thing, and the Herdmans still think it's some kind of spy story. It may be the first Christmas pageant in history where Joseph and the Wise Men get in a fight and Mary runs away with the baby.

BETH: (Pg 30) It's just going to be awful, you know. They look like trick or treat- all dirty and fastened together with safety pins and wearing their mouldy old sneakers . . . Mary and Joseph, I mean. They look like refugees or something.

FATHER: Well . . . that's what they were . . . Mary and Joseph. They were refugees, in a way. They were a long way from home, didn't have any place to stay, didn't know anybody. They were probably cold and hungry and tired . . . and messy. (Beth is struck by the sense of this new idea) **** Cut to the actual performance already in progress *****

MAXINE: (Pg 33-36) (Narrating) . . . And in that region, there were shepherds in the field, keeping watch over their flocks by night. And an Angel of the Lord appears to them and said . . . (Gladys roars on stage with her message)

GLADYS: Hey! Hey! Unto you a child is born! . . . It’s Jesus, and he’s in the barn . . . Go see him! (the Shepherds hesitate) Go on , he’s over there . . . Go on!

MAXINE: There came Wise Men from the East to worship him.

LEROY: (singing) We Three Kings of Orient Are . . .

ALICE: They look awful, too. And what’s that Leroy’s got?

BETH: (craning her neck to see) It’s . . . it’s a ham!

ALICE: Bet they stole it!

BETH: No . . . I think it’s the ham from their welfare basket. It’s the only thing they ever gave away in their whole life.

MAXINE: The Wise Men and the Sheperds departed, praising God for all they had seen and heard. But Mary kept all these things and pondered them in her heart. (Imogene takes the doll from the manger and holds it. She puts it up on her shoulder, as if to burp it. She is crying)

ALICE: (in reverent awe) Look . . . Mary’s crying. ****** After the pageant *****

MRS. MCCARTHY: Could you believe that was Imogene Herdman? And all the rest of them? This was the best Christmas pageant we ever had, and I'm not sure why, but I think it was them. There was just something . . . different.

MRS. SLOCUM: Well, the Angel of the Lord was different!

MRS. MCCARTHY: Yes, but you know, I liked that! Had lots of spirit. Sometimes you can't even hear the Angel of the Lord.

MRS. SLOCUM: Well... it did seem . . . real. (They exit.)

BETH: It did seem real, as if it might have happened just that way. We all thought the pageant was about Jesus, but that was only part of it. It was about a new baby, and his mother and father who were in a whole lot of trouble - no money, no place to go, nobody they knew. Because of the Herdmans, it was a whole new story - Imogene, burping the baby, and the Wise Men bringing such a sensible present. After all, they couldn't eat frankincense! And even Gladys-"He's in the barn. Go see him" But I guess it wasn't like that for Imogene. For her, the Christmas pageant turned out to be all wonder and mystery, as if she just caught on to what Christmas was all about.

GLADYS: (Pg 38) (offstage) Heyl . . . (She runs on stage and points at the audience.) Hey, unto you a child is born!
```

---

## IC-0725: The Best Daddy

- Title: The Best Daddy
- Author (byline): Shel Silverstein
- Work: An Adult Evening of Shel Silverstein
- Publisher: Dramatists Play Service
- Publication date as stated: March 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: LISA, DAD
- Teaser before the introduction: Yes
- Spoken words (computed): 908
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shel Silverstein
Book: An Adult Evening of Shel Silverstein
ISBN: 978-0822218739
Publisher: Dramatists Play Service
Date (Month/Year): March 2003
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Sarcasm is an interesting verbal technique, often lost on the young . . . In this scene we meet Lisa and her father on one of the most exciting days of the year for any child . . . her birthday.

ACTOR: Unfortunately, this birthday surprise is a little more than little Lisa has bargained for.

TOGETHER: Shel Silverstein’s The Best Daddy

ACTRESS: (whispers) But you can decide for yourself.
```

### Performance text (classify this)

```text
LISA: Okay?

DAD: A little further.

LISA: Here? Can I open my eyes?

DAD: Hold my arm.

LISA: I’m going to bump into it.

DAD: You won’t bump into anything. Keep your eyes closed. Now hold my arm, a couple more steps here.

LISA: Can I look now?

DAD: All right. . .open your eyes right. . . now.

LISA: Is that him, there?

DAD: That’s right.

LISA: Why is he covered with a blanket?

DAD: Well, he. . .

LISA: He doesn’t look like a pony.

DAD: Well, he is -- a thoroughbred gelding 350-dollar Shetland pony.

LISA: Is he laying down?

DAD: Um yes.

LISA: Why is he laying down? Is he sick?

DAD: Pure strain Kentucky-bred Shetland

LISA: Why is he laying down?

DAD: Lisa. . .I didn’t want to tell you this. . .

LISA: Why is he laying down? He is sick, he is.

DAD: He’s dead.

LISA: He. . .he’s dead?

DAD: It’s a helluva thing to have to tell your daughter on her birthday.

LISA: Dead? A dead pony?

DAD: We’ve got to face the facts.

LISA: You. . .you got me a dead pony for my birthday?

DAD: I didn’t get you a dead pony for your birth. . .

LISA: What happened to him?

DAD: Lisa, I’m going to be honest with you. . .

LISA: What happened to my pony?

DAD: You’re thirteen years old now and I’m going to talk to you like an adult.

LISA: What happened to my pony?

DAD: I shot him.

LISA: Y-you shot him?

DAD: About an hour ago, but hear me out.

LISA: Y-you shot my pony? You. . .you shot my birthday pony?

DAD: I told you not to get excited, didn’t I? Answer me, did I or didn’t I not say, “Don’t get too excited. . .”

LISA: Why did you shoot my pony?

DAD: I did not shoot your pony. He wasn’t your pony when I shot him. You didn’t even know he existed. He was a pony.

LISA: Why did you shoot my pony?

DAD: He bit me.

LISA: But you didn’t have to shoot him. You didn’t have to. . .he’s only a little pony. He didn’t know what he was doing.

DAD: You weren’t there, you don’t know the situation.

LISA: My pony is dead. I’m thirteen years old today and you gave me a dead pony for my birthday.

DAD: I told you, he bit me.

LISA: But you gave him to me anyway. You took me out here to show me a dead pony?

DAD: Well, I thought about that. I thought, well, if I take her out here and show her a dead pony that will upset her, but if I don’t give her anything she’ll think I forgot her birthday.

LISA: What could be worse than getting a dead pony for your birthday?

DAD: Listen now, someday you’ll have children of your own. I never shot a pony before. I want you to believe that, never in my life before today.

LISA: You hated my pony, you always hated him.

DAD: I didn’t always hate him, I never even. . .

LISA: You did. You hated him because you knew I love him.

DAD: When I saw him I liked him, he was cute.

LISA: You knew he loved me and he could show his feelings and you couldn’t stand that. Oh no ‘cause you could never love anyone. You’re all bottled up. You keep all your feeling all bottled up. And he could show his love. He could swish his tail and toss his head, and lick my hand when I gave him sugar. And late at night when I’d ride him bareback through the gray mountains. . .

DAD: You never rode him – I just bought him. . .

LISA: You didn’t know. I used to sneak out late at night when you thought I was sleeping. I’d climb out of my bedroom window and I’d run to the pasture. . .

DAD: Pasture? What pasture?

LISA: And he’d smell my scent and come galloping toward me, and I’d leap onto his back, and we’d go galloping over the moonlit moor. . .

DAD: Moonlit moor?

LISA: . . .with the wind in my hair. And now he’s dead. You killed my pony. You killed Black Thunder.

DAD: Black Thunder?

LISA: You killed the only thing I ever loved.

DAD: I didn’t.

LISA: You did.

DAD: I didn’t

LISA: You did. You said you did.

DAD: APRIL FOOL!

LISA: April Fool? But, but it’s not April, it’s my birthday.

DAD: BIRTHDAY FOOL!

LISA: You mean Black Thunder’s not dead? Then who is under that blanket?

DAD: Not “who” but “what.”

LISA: Wh-what? Wh-what’s under there?

DAD: Three guesses.

LISA: I. . . I don’t know. You’re cruel. You’re the cruelest daddy in the whole world.

DAD: Three guesses.

LISA: A. . .a candy bar?

DAD: Uh-uh

LISA: A. . .a turtle, a bit gigantic turtle?

DAD: Nope, two down, one to go.

LISA: A. . .a. . .a rubber raft?

DAD: No. . .

LISA: What then, what is it?

DAD: It’s your sister!

LISA: What?

DAD: It’s your big fat sister!

LISA: Cathy? It’s Cathy?

DAD: Big fat Cathy!

LISA: Why is she hiding under there? And you said it was a what, not a who, Cathy is a who.

DAD: Not exactly.

LISA: Not exactly? Cathy? Ca-Cathy?

DAD: It’s a. . .what. . . it’s Cathy’s body.

LISA: Cathy’s body?

DAD: She’s the one that bit me.

LISA: You shot Cathy?

DAD: Teeth like a damn wild grizzly.

LISA: You gave me my dead sister’s body for a birthday present? First you tell me my pony is dead, and now you tell me you shot my favorite sister? You are the cruelest meanest most vicious. . .

DAD: DOUBLE APRIL FOOL!!

LISA: Double April Fool?

DAD: It’s not your sister. I wouldn’t shoot your fat little sister. Three more guesses!

LISA: (Crying) I’m not guessing anymore. You ruined my birthday. You’re a mean, cruel --

DAD: It’s the motorcycle you wanted!

LISA: The Honda?

DAD: Uh-huh.

LISA: The red one?

DAD: Uh-huh.

LISA: Really and truly?

DAD: Mmm-hmmm.

LISA: Oh Daddy. Daddy, you’re the bestest daddy in the whole wide world!
```

---

## IC-0726: The Best Medicine

- Title: The Best Medicine
- Author (byline): Joshua Sands
- Work: Turning Points (Pg 51-54)
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: RYAN, KRISTEN
- Teaser before the introduction: No
- Spoken words (computed): 1080
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joshua Sands
Book: Turning Points (Pg 51-54)
ISBN: 978-0742117013
Publisher: Tichenor Publishing
Date (Month/Year): 2001
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: When Kristen learned she had cancer, she was desperate for the friendship and advice of patients her age. Young adults with cancer slip into a lonely no-man's land. Too old for the instant community of a children's hospital, they still don't fit in with the over-50 community that overwhelmingly populates adult cancer wards.

ACTRESS: I figured there was nobody else out there. I was so isolated, I didn't even realize how lonely I was.

TOGETHER: Welcome to Planet Cancer.

ACTRESS: No, we didn't choose to come here. But we ended up as honorary natives of this terrible and wonderful world. Like other planets, Planet Cancer rotates regularly between the dark side of night and the brightness of day.

ACTOR: All too often, we lose ourselves on the dark side, forgetting that where there is night, day must follow; and where there is life, there is the light of hope and laughter.

TOGETHER: The Best Medicine by Joshua Sands
```

### Performance text (classify this)

```text
RYAN: (Pg 51-54) You’d think they’d find a new way to give us this spiel.

KRISTEN: Quiet – I’m trying to hear.

RYAN: Basically I think what he is trying to tell us is that we all have cancer –

KRISTEN: Shoosh!

RYAN: So you’re a shoosher. Don’t worry. This diatribe ends the meeting. I’m surprised they don’t break out into a chorus of “I Will Survive!”

KRISTEN: Shoosh!

RYAN: You know, your lips are kinda sexy when you—

KRISTEN: Look, I know you’re just trying to make a friend, but I need these meetings. Don’t you?

RYAN: Sure. But, I need to talk to humans sometimes, too.

KRISTEN: Yeah, I guess this disease can be kinda lonely.

RYAN: You understate yourself. I think I’m gonna like you. . . So, what’s your name?

KRISTEN: Kristen.

RYAN: I’m surprised you didn’t say “Cancer Victim #3647B.”

KRISTEN: What’s yours?

RYAN: Ryan. Sorry if I’m too sarcastic tonight. Whenever Mark runs the meetings –

KRISTEN: You come here a lot.

RYAN: A couple times a week. You?

KRISTEN: Just starting. I’m not so sure if I like it.

RYAN: Listen, why don’t we go out and do something fun?

KRISTEN: I don’t know.

RYAN: Two dates. That’s all I ask.

KRISTEN: Two? Most guys settle for just one.

RYAN: Yeah, but I like variety. You can’t tell anything in one date. Say we go ice-skating. Should that be the only test if we’re compatible?

KRISTEN: I don’t know.

RYAN: Two dates. One goofy, high-schoolish date. One romantic date. If you hate them both you can go back to sitting at these meetings in peace and quiet. (a beat). So? Don’t tell me your dance card is already full?

KRISTEN: No. I’ll try it. Be spontaneous, right? What can it hurt? *****Scene break*****

RYAN: You missed!

KRISTEN: When you said goofy and high-schoolish, I had no clue we’d end up at the fair. but, it fits the category.

RYAN: Now follow through with the arm. You can knock em’ all over if you have the right precision and force.

KRISTEN: You sound like an expert . . .

RYAN: Sure. Did this a lot when I was goofy and high-schoolish.

KRISTEN: (laughs) I was too busy going to cheerleading camp. And tennis camp. And—

RYAN: (laughs) Oh, an overachiever. Well, listen. We’re just cancer victims now. No more strenuous effort to try and make our future brighter. Just focus on today. This softball. Those bottles.

KRISTEN: That’s all?

RYAN: Yeah, focus on what you can control. Your mind. Your heart. Your way of getting through the day with a chuckle or two. It helps.

KRISTEN: You learn that from Mark?

RYAN: Hell, no. I learned that the hard way. Practice.

KRISTEN: Hey, nice throw. *****Scene Break*****

RYAN: Hi, Kristen? It’s Ryan. Just wanted to make plans for date #2

KRISTEN: You were serious about this pair of dates thing?

RYAN: Yeah, were you?

KRISTEN: Sure. What did you have in mind?

RYAN: Romance. That’s what I promised, right? Wear a cocktail dress and I’ll pick you up at 7:00. No wait -- gotta stop and talk to the witch doctor about the cancerous Pacman eating my liver.

KRISTEN: What?

RYAN: Pick you up at 7:30. Bye. *****Scene Break*****

KRISTEN: So. . . a boat. . . champagne. . . dancing . . .

RYAN: Might think I’m trying to show off, huh?

KRISTEN: I might think that.

RYAN: You enjoying yourself?

KRISTEN: Yeah, it amazes me how I forget everything with you. Do you even think about dying?

RYAN: Dying? Why? When I can be dancing with you?

KRISTEN: Really, do you?

RYAN: You know the champagne is great – (loses balance, almost falls)

KRISTEN: You OK?

RYAN: Yeah, must be the champagne. Maybe it’s the ocean. I’m fine.

KRISTEN: Let’s take a breather.

RYAN: Well . . . (sigh) okay deal. *****Scene Break*****

RYAN: See, now this is the part when Mark asks for prayer requests.

KRISTEN: Very nice Nostradamus.

RYAN: Then one by one, everyone eventually stands up and says “Yea, umm, You see I’ve got this cancer thing…”

KRISTEN: Ryan, I don’t think I’m coming to the meetings anymore.

RYAN: What? You have to.

KRISTEN: Why? You don’t like them and I’d rather be with Ryan my boyfriend rather than Ryan the cancer meeting smart-alick.

RYAN: So you don’t like my jokes?

KRISTEN: No—I just want to separate this from our relationship.

RYAN: Kris, it’s not a good idea. Promise you’ll come on Friday?

KRISTEN: Fine. Promise. *****Scene Break*****

KRISTEN: (on answering machine) Ryan? Hi. It’s Kristen. I showed up last night. It was the one at St. Andrew’s, right? Where were you? Give me a call, OK? Bye. *****Scene Break*****

RYAN: It was nothing!

KRISTEN: Ryan, you had me so worried!

RYAN: I just got a little queasy at work and fell asleep. They thought I had passed out!

KRISTEN: Ryan, you spent the whole weekend in the hospital.

RYAN: I know. But don’t worry. Cancer is like this great ballgame. I haven’t struck out. This weekend is like the seventh inning stretch.

KRISTEN: Are you sure you’re alright?

RYAN: Fine. Got a green tongue. Wanna see?

KRISTEN: Ryan, really. It’s time to stop the jokes.

RYAN: I know. I missed the meeting. I’ll pull a double on Tuesday.

KRISTEN: Ryan—

RYAN: Kristen, let’s go out on another pair of dates. Let’s see—how about snowboarding and a show this time?

KRISTEN: Damn it, Ryan! Talk to me! Don’t give me one-liners. Don’t try out for a cancer comedy troupe. Talk to me! We’re dying here! We have a couple months to fit everything in, and you’re wasting it with all this bullshit!

RYAN: Is that what you think? This is all bulls***. The fair? The dancing? The lunches at the bistro? If that’s bull***, what the hell is the real stuff? What’s real, Kris?

KRISTEN: I don’t know . . .

RYAN: I’ll tell you what’s real. You and me. Spending time together. Laughing together. Playing Monopoly. Watching Conan on TV. That’s what’s real. That’s what’s real Kris.

KRISTEN: (pause) But your cancer is real, too.

RYAN: Yeah, and it’ll consume you if you let it. Don’t. Don’t let it consume you. Please don’t. *****Scene Break*****

KRISTEN: Hi, my name is Kristen. I’ve got colon cancer. God, I don’t know how to do this. See—I met my boyfriend in here. Now it’s just me. And I don’t know how to do this on my own. He always helped me laugh, but now—

RYAN: No more strenuous effort to try and make our future brighter. Just focus on today.

KRISTEN: I mean, I hear him speaking to me.

RYAN: Focus on what you can control. Your mind. Your heart. Your way of getting through the day with a chuckle or two. It helps.

KRISTEN: And he makes sense. But it’s so hard to keep the words living when he’s gone. All I can think of saying here are jokes about how this’ll make our tongue green. But see, you’re not laughing. Guess you had to be there.

RYAN: I’ll tell you what’s real. You and me. Kristen, you and me.
```

---

## IC-0727: The BFG

- Title: The BFG
- Author (byline): Roald Dahl (Adapted by David Wood)
- Work: Not specified
- Publisher: Puffin Books
- Publication date as stated: Feb 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 2, NARRATOR 1, NARRATOR 2, MRS. CLONKERS, BFG, BOTH, SOPHIE, BLOODBOTTLER, BONECRUNCHER, CHILDCHEWER, GIZZARDGULPER, QUEEN, HO AIR FORCE, HO ARMY, HO AIRFORCE
- Teaser before the introduction: Yes
- Spoken words (computed): 1320
- Already set (do not supply): none

### Source block (context only)

```text
Author: Roald Dahl (adapted by David Wood)
ISBN: 978-0142407929
Publisher: Puffin Books
Date (Month/Year): Feb 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Sophie’s life as an orphan is not exactly what dreams are made of.

ACTOR 2: That is until one night when a big friendly giant makes his way into town during the witching hour to blow dreams into the minds of sleeping children.

ACTOR 1: He whisks Sophie away to Giant Country. Why? Because humans can’t know that Giants exist.

ACTOR 2: And it’s there that the adventures begin.

ACTOR 1: The BFG isn’t like the other Giants, who are not at all friendly.

ACTOR 2: Ultimately our hero, Sophie, with the help of the BFG and the Queen, saves the day and the children of England too!

TOGETHER: The BFG by Roald Dahl adapted by David Wood
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: ACTOR 1: Narrator 1, Sophie, Bonecruncher, Gizzardgulper, Head of Air Force

ACTOR 2: Narrator 2; Mrs. Clonkers, BFG, Bloodbottler, Childchewer, Queen, Head of Army

NARRATOR 1: (Pg 17-20) It was late at night. . .

NARRATOR 2: (makes an owl hooting noise)

NARRATOR 1: . . . in the orphanage dormitory, Sophie couldn't sleep. (acting out the story as she tells it) A brilliant moonbeam was shining right on to her pillow. She slipped out of bed to get a drink of water.

MRS. CLONKERS: Sophie! Back to bed this instant. You know the rules.

NARRATOR 1: Mrs Clonkers! Sophie went back to bed. She tried very hard to doze off. The time ticked by.

NARRATOR 2: (makes the tick-tock noise)

NARRATOR 1: The house was absolutely silent. Perhaps, thought Sophie, this is what they call the witching hour, that special moment in the middle of the night when everyone is in a deep, deep sleep, all the dark things come out from hiding and have the world to them-selves. She crept to the window. And suddenly she saw. . . a giant. (BFG enters in a cloak and carries a suitcase; he acts out the narration) He stopped at the house opposite, bent down to look in a bedroom window and then . . .

BFG: (BFG opens a suitcase, take out a jar and pour its contents into the end of a horn-like trumpet. Blows through it into an imaginary window. Turns and notices Sophie - Gasps)

NARRATOR 1: He saw Sophie. (acting out the story as she tells it) She pulled back from the window, flew across the dormitory and jumped into her bed and hid under the blanket, tingling all over.

BFG: (Peeps in the window and with a growl, pushes a hand through and snatches SOPHIE, holding her up high)

BOTH: Aaaaaaaah!

BFG: (Begins slow-motion, on-the-spot running)

NARRATOR 1: Running, striding, leaping through the night. Over fields, over hedges, over rivers, each stride as long as a tennis court. Faster, faster, feet scarcely touching the ground. Over oceans, over forests, over mountains . . .To a land unknown to human beings.

BFG: (Pg 27-32) (Standing over SOPHIE) Ha! What has us got here? (He looks carefully at SOPHIE. At first, he should not appear very friendly)

SOPHIE: (Nervously) Where am I?

BFG: This is my cave.

SOPHIE: Why did you snatch me and bring me here?

BFG: Because you saw me. If anyone is ever seeing a giant, he or she must be taken away hipswitch.

SOPHIE: Why?

BFG: Human beans is not believing in giants, is they? Human beans is not thinking giants exist.

SOPHIE: I do.

BFG: Ah, but that is because you has seen me. If I hadn't snitched you, you would be scuddling around yodelling the news on the telly-telly bunkum box that you were actually seeing a giant, and then a great giant-hunt, a mighty giant look-see, would be starting up all over the world, and human beans would be trying to catch me and put me in the zoo with all those squiggling hippodumplings and crocadowndillies.

SOPHIE: So what's going to happen to me now? (Gasping) Please don't eat me!

BFG: (Bellowing with laughter) Just because I is a giant, you think I is a man-gobbling cannybull! No! You is lucky. If one of the other giants is snitching you, they is crunching you up for sure. Bones crackety-crackety-cracking. Gobble, gobbledy, gone!

SOPHIE: Other giants? You mean there are more of you?

BFG: Of course! This is Giant Country! (He picks up SOPHIE) Be peeping out over there, little girl, and be seeing a brain bogglingsome sight. (They peep outside)

SOPHIE: What on earth are they doing?

BFG: Nothing. They is just waiting for the night to come. Then they will be galloping off to places where human beans is living to find chiddlers to guzzle for their suppers.

SOPHIE: Where?

BFG: All over the world. That's the Bonecruncher. He is thinking Turkish chiddlers is juiciest chiddlers. They is tasting of Turkish delight!

SOPHIE: Of course. Who's that big, fierce one?

BFG: That's the Fleshlumpeater. He’s fancying getting his chompers round a handful of chiddlers from Wellington! That’s the Bloodbottler. He is thinking the English chiddlers is tasting ever so wonderfully of crodscollop.

SOPHIE: I'm not sure I know what that means.

BFG: Meanings is not important. You will be coming to an ucky-mucky end if any of them should ever be getting his gogglers upon you. You would be swallowed up like a piece of frumpkin pie, all in one dollop. (They return inside the cave) There. You is safe in here.

SOPHIE: (Pg 33-35) I think eating children is horrible.

BFG: I has told you. I is not eating chiddlers. Not I! I is a freaky giant! I is a nice and jumbly giant! I is the BFG.

SOPHIE: The BFG?

BFG: The Big Friendly Giant! What is your name?

SOPHIE: My name is Sophie.

BFG: How is you doing, Sophie? (He gently shakes hands with SOPHIE) Your poor mother and father. By now they must be jipping and skumping all over the house shouting, 'Hallo, hallo, where is Sophie gone?'

SOPHIE: I don't have a mother and father. They died when I was a baby.

BFG: You is a norphan? Oh you poor little scrumplet. You is making me sad.

SOPHIE: Don't be sad. No one at the orphanage will be worrying much about me.

BFG: Was you happy there?

SOPHIE: I hated it. Mrs Clonkers locked me in the cellar once for not folding up my clothes.

BFG: The filthy old fizzwiggler! You is making me sadder than ever. (he sobs)

SOPHIE: Don't cry, BFG. Please. (The BFG recovers a little) Listen, we can't just sit here and let any more children be eaten. We've got to stop those brutes. It’s up to us! We’ve got to save the children of the world!

BFG: Us? Redunculus and umpossible. (He takes out a bottle of liquid)

SOPHIE: (Pg 52-55) (Reading from the bottle) Frobscottle?

BFG: I drink it lots. Delumptious, fizzy frobscottle! (He removes the stopper. There is a fizzing sound)

SOPHIE: Hey, look! It's fizzing the wrong way! In our fizzy drinks, like Coke and Pepsi, the bubbles go upwards.

BFG: Flushbunking rubbsquash! Upgoing bubbles is a catasterous disastrophe.

SOPHIE: But why?

BFG: Listen. When you is drinking this cokey drink of yours, it is going straight down into your tummy. And the bubbles is going also into your tummy. If the bubbles is fizzing upwards, they will all come swishwiffing up your throat and out of your mouth and make a foulsome belchy burp!

SOPHIE: That's often true. But what's wrong with a little burp now and again? It's sort of fun.

BFG: Burping is filthsome. Us giants is never doing it.

SOPHIE: But with your drink. . .

BFG: Frobscottle.

SOPHIE: With frobscottle, the bubbles in your tummy will be going downwards and that could have a far nastier result. They'll be coming out some where else with an even louder and ruder noise.

BFG: A whizzpopper! Us giants is making whizzpoppers all the time! Whizzpopping is a sign of happiness. It is music in our ears!

SOPHIE: But it's. . . it's rude!

BFG: But you is whizzpopping, is you not, now and again?

SOPHIE: Everyone is . . . whizzpopping. Kings and queens, even little babies. But where I come from, it's not polite to talk about it.

BFG: Redunculous! If everyone is making whizzpoppers, then why not talk about it? Now, let's be having a swiggle and seeing the result! (The BFG drinks from the bottle. Pauses. Then ecstasy fills his face. A very loud whizzpopper nearly shoots him in the air) Whoopee! (And another) Wheeeeeeee! (SOPHIE laughs, in spite of herself) Have some. Go on. It's gloriumptious!

SOPHIE: It's lovely. (Suddenly a succession of whizzpoppers – Sophie giggles) Wheee! Wheeeeee! (suddenly a roar of the other giants startles them)

BLOODBOTTLER: (Pg 76-78) ‘Tis the witchy hour. And I is starveling!

BONECRUNCHER: Let us go guzzle human beans! (Both cheer)

CHILDCHEWER: Let us fluchbunk to England!

GIZZARDGULPER: I is fancying a few nice little English chiddlers! (Both cheer)

SOPHIE: We’ve got to stop them. We must warn everyone in England they’re coming!

BFG: Redunculus and um-possiple. I is never showing myself to human beans. They will be putting me in the zoo with all the jiggyraffes and cattypiddlers. And they will be sending you straight back to the norpahage. Grown-ups is all squifflerotters and grinksludgers.

SOPHIE: (thinking) I’ve got it! Listen, BFG, we’ll go to the Queen and tell her about the giants. She’ll do something, I know she will. ******Buckingham Palace*******

QUEEN: (Pg 107) (Fanfare. Enter the Queen) It’s been a rough morning. (Pg 106) Sophie, you have told me of your visit to Giant Country and of the giants’ ghastly night-time children-eating raids. (she claps her hands) (Pg 108-109) Summon the Head of the Army and the Head of the Air Force immediately! (they enter) Good morning, gentleman. You’ve read about the disappearing children? (pause) They were eaten. (pause) By giants.

HO AIR FORCE: Giants?

HO ARMY: No such fellas, Your Majesty.

HO AIRFORCE: Except in fairy-tales. (Both laugh)

QUEEN: (Pg 110-112) Gentleman, allow me to present the Big Friendly Giant. (she indicates behind them)

BOTH: (turn; see the BFG) Aaaaaah! (cling to one another in terror) A giant!

QUEEN: Indeed. Luckily a friendly one. His colleagues are not. Tonight those bloodthirsty brutes will be galloping off to gobble up [more] unfortunate wretches. They have to be stopped. Fast. They must be brought back. Alive.

HO AIR FORCE: Alive? They’d knock us down like ninepins!

BFG: Keep your skirts on! I has the answer. Every afternoon all these giants is lying on the ground snoozling in the Land of Noddy. All you has to do is creep up on them and tie them up.

HO AIR FORCE: But how do we get the brutes back here?

BFG: You is having belly poppers, is you not?

HO AIR FORCE: Are you being rude? (BFG lets loose with a wizzpopper)

SOPHIE: (with a disapproving look to BFG) He means helicopters.
```

---

## IC-0728: Black Paintings

- Title: Black Paintings
- Author (byline): Neil Olson
- Work: 2006: The Best Ten-Minute Plays for Two Actors
- Publisher: Smith & Kraus, Inc.
- Publication date as stated: Nov 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ERIC, DIANE
- Teaser before the introduction: No
- Spoken words (computed): 1757
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Olson
Book: 2006: The Best Ten-Minute Plays for Two Actors
ISBN: 978-1575255637
Publisher: Smith & Kraus, Inc.
Date (Month/Year): Nov 2007
```

### Introduction (context only: never use it for content warnings)

```text
ERIC: Artists capture reality, truth, beauty in their paintings

DIANE: And agents display and sell these paintings. These bits of reality, truth and beauty.

ERIC: But when the reality and truth are death, what is left to paint?

DIANE: Is death beautiful? Will death sell?

ERIC: When art is death, a painter is left creating

BOTH: “Black Paintings”

DIANE: By Neil Olson
```

### Performance text (classify this)

```text
Diane sits center stage at a table upon which there is a small cardboard box. Eric stands stage right at a set of open French doors, looking out.

ERIC: Can you see the ocean from here?

DIANE: Yes.

ERIC: Where do I look?

DIANE: South.

ERIC: Which way is that?

DIANE: The way you're facing.

ERIC: I'm not seeing it.

DIANE: That's right. (He turns and looks at her in confusion.) You asked if I could see the ocean. There are lovely views from the bedrooms upstairs, but since you will never see those bedrooms, you will never see the ocean from here.

ERIC: Diane.

DIANE: You shouldn't even be in this house.

ERIC: The door was open.

DIANE: There is an acre of private property between the road and that door.

ERIC: And very handsome property it is. Your apple trees are still in bloom, they've all gone by in the city. Nice house, too.

DIANE: SO glad you approve.

ERIC: Strange that I've never seen it. I guess Henry only had his top-tier artists out to visit.

DIANE: No.

ERIC: No?

DIANE: This was his refuge. This is where he went to escape the whole crazy, needy lot of you.

ERIC: Sam's been here. He described the place to me.

DIANE: He's a neighbor, that's different.

ERIC: SO just your rich clients, then.

DIANE: Maybe just the loyal ones.

ERIC: Loyal.

DIANE: I'm sorry, did I use an unfamiliar word? Loyal, L-O-Y

ERIC: Loyalty can't afford to be blind. It's earned by good service.

DIANE: You were very well taken care of.

ERIC: Where would I be now if I'd stayed, with Henry ... I'm sorry, by the way. I'm sorry about Henry. Truly.

DIANE: SO sorry they were the first words out of your mouth.

ERIC: I sent a note, you never replied.

DIANE: Why are you here, Eric?

ERIC: You know damn well, why. If you didn't want me here, you could have avoided it with one phone call.

DIANE: I had nothing to say to you.

ERIC: Fine. Then you could simply have packed the pieces up and shipped them to me.

DIANE: Anything belonging to you was returned long ago.

ERIC: Not the four black paintings.

DIANE: The portraits, you mean?

ERIC: They're not portraits.

DIANE: Funny, they used to be. Odd how much a work can change, years after being completed.

ERIC: Just because a work is inspired by a living subject does not make it a portrait. Don't pretend to such simple-minded ideas.

DIANE: They don't belong to you.

ERIC: I made them.

DIANE: You made many things which no longer belong to you.

ERIC: For which I was compensated.

DIANE: You want money?

ERIC: I want what's mine. Your father knew those works were only for safe-keeping.

DIANE: You didn't give them to Henry. You gave them to me.

ERIC: Never. You invented that and now you've convinced yourself it's true, but I never said it. We've been through all of this.

DIANE: That's right, we have. That's why I didn't return your calls.

ERIC: And the facts haven't changed. What do you think, that I'm just going to give up, that you can outlast me? The next step is lawyers. You understand that, I hope.

DIANE: I'd be pretty stupid if I didn't, since you've threatened it in every message.

ERIC: Is that what you want?

DIANE: You're too cheap to hire a lawyer.

ERIC: Helen's already found me one.

DIANE: Helen, of course. You just go from one nursemaid to another. Tell me, now that it doesn't matter anymore: Were you already sleeping with her before you left us?

ERIC: I am not sleeping with her.

DIANE: Really? And here I thought she slept with all her clients. She's clearly not the full-service provider you expected.

ERIC: Do you really want to be throwing rocks in that particular neighborhood?

DIANE: Oh, I assure you I have nothing on Helen. You were my sole mistake in that area. And my last.

ERIC: Why do you have to make it like this?

DIANE: Me? Why do I have to -

ERIC: People have affairs, they end, they move on.

DIANE: This is not about that.

ERIC: Then what the hell is it about?

DIANE: What you did to my father.

ERIC: I did not do anything to your father.

DIANE: Just broke his heart, that's all. Just destroyed his will to fight.

ERIC: I made a business decision. An artist has the right to make a change when his gallery can no longer place his work.

DIANE: An artist has a duty to know when his work has become inferior and repetitive, and to take a hard look inside himself.

ERIC: Interesting that you never made those critiques when they might have mattered.

DIANE: As if you would have listened.

ERIC: That's not the point, is it?

DIANE: You're right. I could see it happening and I said nothing. I was a coward. I didn't want to scare you away. Sue me.

ERIC: Give me my Goddamn paintings, Diane. (He slams his hand down on the box, then sees it for the first time.) What is this?

DIANE: Ashes.

ERIC: (Backing away.) That's not Henry, is it?

DIANE: He wanted to be scattered on the beach, at sunrise. Sunrises are beautiful out here, not that I've seen many. But he was always up before dawn, city or country. Drinking coffee while the world slept, calling his pals in London. Thinking about what he could do that day to help his artists.

ERIC: He did me a lot of good, I'd never say otherwise. He loved painters, not these idiots with their videos and shellacked cow intestines. I've missed him this past year. Missed both of you.

DIANE: How sweet.

ERIC: But he'd lost his touch, or maybe he was just tired. He only had time for Sam, Masako, fucking Reinhardt. I barely spoke to him those last few months.

DIANE: Because he knew I was taking care of you. Who sold your last half dozen pieces?

ERIC: It was his gallery.

DIANE: I did.

ERIC: I needed his attention, his approval.

DIANE: And I would have continued to look after you long after Henry was gone.

ERIC: It wasn't the same. I mean, I'm grateful, especially since it turns out you were selling work you clearly hated.

DIANE: That's not what I said.

ERIC: But how long ago were those sales?

DIANE: How many pieces has Helen sold for you?

ERIC: I hear Reinhardt left. Went to Gagosian.

DIANE: Good riddance.

ERIC: And Sam's thinking about it.

DIANE: Not that he's told me. But if it's true, at least he had the decency to wait until Henry died.

ERIC: SO if I'd waited a year I'd be off the hook?

DIANE: No.

ERIC: Why?

DIANE: You don't listen. Because I was the one taking care of you.

ERIC: You see, this is about you and me. You're lying to yourself, using Henry as a shield.

DIANE: Get out of my house, Eric.

ERIC: Look, we all loved you, loved having you involved in our business. You were the strong right hand the old guy needed. But Henry ... Henry was irreplaceable.

DIANE: Apparently not.

ERIC: (Long pause.) One piece.

DIANE: One piece of what?

ERIC: What you asked before. Helen sold one piece from the last show. And I haven't even been paid for it.

DIANE: Poor you.

ERIC: Made me wonder about leaving Henry, leaving you. It's always easier to blame someone else. I really thought this was strong stuff. I got rid of all of that blue and yellow I was using, all those bright colors and geometric shapes. Went back to the black and white, the semi-abstract forms.

DIANE: I saw the show.

ERIC: You did? Then you know where I'm going with this. Simple, rigorous, tough, it just poured out of me. Best work in years. And nobody bought it. Got three small, mediocre reviews. I was in a rage, you remember my rages?

DIANE: Yes.

ERIC: And then I walked through the gallery, right before they took the show down. Really looked at each piece. And it was all garbage. Empty canvases. At best, a memory of something good I'd once done, but not the thing itself.

That's why I need the black paintings back. I haven't done anything like those since, but maybe they'll help me remember how.

DIANE: It doesn't work like that.

ERIC: How the hell would you know?

DIANE: They're creatures of the time in which you created them. They're dead to you now. What's good, what's real, lives in your fingers, in your muscle memory. In your instinct, if you could clear away all the expectations and bullshit.

ERIC: Maybe you're right.

DIANE: The paintings themselves would only be a burden to you.

ERIC: I still want them.

DIANE: Do you really? Is that really why you came?

ERIC: Why else?

DIANE: Maybe to say you were sorry, or that you made a mistake, or that you still ...

ERIC: I'm sorry I hurt you. And I probably did make a mistake, but it's one I plan to live with.

DIANE: Well good for you.

ERIC: Can I have my paintings?

DIANE: Sure.

ERIC: Thank you. Thank you, Diane. This may sound inappropriate, but I'm going to ask anyway. I want to be there when you scatter Henry's ashes. It would mean a lot to me.

DIANE: Sorry. We scattered them yesterday morning. Just my sister, me, and Sam. It was a lovely moment.

ERIC: T hen what's in the box?

DIANE: Your paintings. Your four black paintings. There's a note, too, I was about to send them to you.

ERIC: This is not even funny.

DIANE: They burned beautifully. You were the one to tell me there's no such thing as black paint, the artist chooses his dark pigments, and you can see it if you look closely. Black may be the absence of all light, but it's the presence of all color, yes? And I could see all of those colors in the flames, a jet of blue, of purple, a sudden burst of green. I know they're not portraits, but I could see my face in every one, black becoming rainbow ore, becoming ash. It was cleansing. I did it right out there on the patio, last night. You can still see the scorch marks.

ERIC: (Rushing to the door and then stopping.) You're lying. You would never do that to art, it's not in you.

DIANE: There's a bottom corner of one that survived. It's right on top, just open the flaps and see. Go ahead. A little courage is required in this life.

ERIC: No.

DIANE: Take the box, then. Open it at your leisure.

ERIC: I'll take everything you own. The gallery will collapse overnight when people hear about this.

DIANE: I'm closing the gallery, and moving back to London. My lawyers will know where to find me.

ERIC: How can you possibly justify this?

DIANE: Besides your killing my father? To set myself free. To set us both free. Someday you'll thank me.

ERIC: Someday you'll understand what you've done, and why.

DIANE: Don't forget your paintings.

ERIC: Keep them. They really do resemble you now. (Exits)

DIANE: (Staring at the box.) Don't look at me like that. I had a right. He'll get over it. He gets over everything, that's his problem. Me, I can't let anything go, or anyone. (Placing her hand on the box.) But I will. Tomorrow, at sunrise.
```

---

## IC-0729: Blue in the Face

- Title: Blue in the Face
- Author (byline): Kayla Cagan
- Work: The Best Ten-Minute Plays for Two Actors 2006
- Publisher: Smith & Kraus Inc.
- Publication date as stated: November 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ANDREW, MARION, ANDREW AND MARION
- Teaser before the introduction: Yes
- Spoken words (computed): 836
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kayla Cagan
Book: The Best Ten-Minute Plays for Two Actors 2006
ISBN: 978-1575255637
Publisher: Smith & Kraus Inc.
Date (Month/Year): November 2007
```

### Introduction (context only: never use it for content warnings)

```text
ANDREW: Not the temperature changing as you go North.

MARION: Not the water as you get further out to sea.

BOTH: A relationship.

ANDREW: After it’s over…

MARION: You can only talk about it for so long before you’re both…

BOTH: “Blue in the Face”

MARION: by Kayla Cagan
```

### Performance text (classify this)

```text
ANDREW: Cold.

MARION: Colder.

ANDREW: Freezing.

MARION: Iceberg.

ANDREW: Well, if it isn't the patron saint of [jerks].

MARION: Guess what I did today.

ANDREW: You sat and pondered your next great masterpiece.

MARION: Guess again.

ANDREW: Man, I never guess right. Hhmmm...

MARION: Never. You're not even close to warm.

ANDREW: Cold.

MARION: Colder.

ANDREW: Freezing.

MARION: You are an iceberg. (Long pause.)

ANDREW: Thanks for the keys.

MARION: You're all set.

ANDREW: I appreciate you lending me your place.

MARION: My space.

ANDREW: You mind if I get a brewski?

MARION: Why should I mind now? I'll get it for you. (She exits. As she re-enters, she holds the cans behind her back.) Guess.

ANDREW: Right hand.

MARION: Guess again.

ANDREW: Other right hand.

MARION: Guess again.

ANDREW: Left foot.

MARION: Guess again. (Andrew moves toward Marion. They are close to kissing, but don't.)

ANDREW: I don't think I need to guess anymore.

MARION: You never figured out what I did today. (He takes the beer from her and begins to drink.)

ANDREW: (Sighs.) Did not.

MARION: So ...

ANDREW: So.

MARION: Aren't you the least bit--

ANDREW: Why should I care what you do anymore? You kicked me out!

MARION: Out of the apartment.

ANDREW AND MARION: But not out of your/my life. (Pause)

MARION: I'll tell you what I did today.

ANDREW: I've got Beannie in the car, if this is going to be a while. I just came by to get the--

MARION: You have Beannie in the car? Why didn't you tell me? Why didn't you bring her in?

ANDREW: I didn't want to confuse her.

MARION: I'll bring her some water.

ANDREW: She has water, and her chew, and her bone. She's fine. You'll see her on the weekend.

MARION: I'm still her mommy.

ANDREW: No, you aren't. You are her "weekends only" mommy, her "only when things are fun" mommy. I'm the one who walks her every morning. I'm the one cleaning up her crap.

MARION: Yeah, I'm really glad she doesn't crap on Saturday and Sunday. That would suck.

ANDREW: Well, thanks for the keys and letting me use the place. I should be--

MARION: What? Before this turns ugly?

ANDREW: Thank God we were never married. (Pause)

MARION: Do you hate me yet?

ANDREW: How am I supposed to answer that?

MARION: Well, I have an answer for you. (She raises her shirt to show off a new, swelling belly ring.) How's this? (She prances.)

ANDREW: Oh.

MARION: That's all you can say?

ANDREW: Yes.

MARION: I thought…

ANDREW: You thought what? I'd appreciate that!

MARION: I thought it would make you laugh.

ANDREW: For three years I asked you to get it pierced. Two months after we break up--

MARION: I finally followed your advice! Irony! Get it?!?!

ANDREW: You must be pleased.

MARION: No, I'm just a bitch.

ANDREW: Yes, you are. (Pause') Can I touch it? (She nods. He goes to her and touches her belly.)

MARION: Be careful! It hurts like hell. It stings. Your hands are cold!

ANDREW: It's turning blue, kind of pinkish blue/

MARION: A bruise.

ANDREW: So, why'd you do it? You want to tell me anyway, right, so ...

MARION: Listen, I'm letting you borrow this place of ours and I'm letting you have the extra keys again, so--

ANDREW: (He grabs her by the hips.) What the hell is this, Marion? (Long pause.)

MARION: Do you want to hear how it happened or don't you?

ANDREW: What choice do I have?

MARION: I didn't go to Bloomingdale's to get it done. I went to a little cosme-tology school down in the Bowery. I thought they would be careful, clean, cautious, considerate…

ANDREW: Catatonic!

MARION: I was held down in this barber chair. My jeans were unbuttoned, my shirt was untied, and I felt four clumsy hands on me, all students, push-ing and pulling my skin and then there was this little plastic gun. I told them I was changing my mind, I was frightened, there wasn't even any ice, I thought there would be ice.

ANDREW: You weren't, raped, you know.

MARION: I did this for you.

ANDREW: Did you rehearse this? You're really being weird. (Marion stares at Andrew.)

MARION: I saw myself hanging upside down in a mirror on the wall behind the students. I turned blue for you. My eyes turned purple and my cheeks filled like plums and my lips were numb and cold and greenish and when I thought I was going to be sick! (Marion runs to the sink and throws up. Andrew flinches.)

MARION: I went cold.

ANDREW: Colder.

MARION: Freezing.

ANDREW: You were an iceberg.

MARION: I went numb because of you, I went cold, I went blue.

ANDREW: But you are here now. And your stomach looks so ...

MARION: I don't feel well.

ANDREW: Let me see your stomach again.

MARION: Be careful. (She lifts her shirt.)

ANDREW: For Christ's sakes, Marion, it's turning gray.

MARION: They said I had to clean it with peroxide twice daily, like when you get your ears pierced.

ANDREW: I've never had my ears pierced.

MARION: Not now, please.

ANDREW: You need to get this thing out of you. Go in the bathroom and get a cold rag.

MARION: It's Florence Nightingale!

ANDREW: I'm trying to help you! I'm not the one puking my guts out while my abdomen is bloating into the Good Year Blimp. Now shut your mouth and help me!

MARION: No way.

ANDREW: Same old Marion.

MARION: I want it now! I'm not taking it out.

ANDREW: Yeah, Marion, you are.

MARION: No, I'm not! (Andrew grabs Marion and throws her on the couch. He straddles her, trying to pin her down so that he can reach her stomach without a fight. Marion scratches him.)

ANDREW: Let me!

MARION: Get your hands--

ANDREW: What? What is it? WHAT THE HELL DO YOU WANT, MARION?

(Andrew gets off of her. They sit on the couch, panting.)

ANDREW: I came to get the keys. That's all I wanted.

MARION: Well, you got what you wanted the minute you walked in the door. Why did you stay?

ANDREW: Why do I always stay, Marion?

MARION: You should go.

ANDREW: I should. (Pause)

ANDREW: Beannie needs me. Beannie is out in the car.

MARION: I know she is!

ANDREW: I'm sorry you are so…

MARION: Cold?

ANDREW: I'll bring Beannie by on

ANDREW AND MARION: Friday. (Andrew takes one last sip of beer and exits. Marion picks up her beer, takes a swig. She starts to pull at her ring, but it hurts too much. She lightly taps the can against her belly, softly repeating "Cold, colder, freezing, iceberg." Lights fade as Marion passes out on the couch.)
```

---

## IC-0730: Boy Gets Girl

- Title: Boy Gets Girl
- Author (byline): Rebecca Gilman
- Work: Not specified
- Publisher: Faber and Faber, Inc
- Publication date as stated: May 2000
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: THERESA'S VOICE, TONY, THERESA, ACTRESS, ACTOR, MERCER, BECK
- Teaser before the introduction: Yes
- Spoken words (computed): 2127
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rebecca Gilman
ISBN: 978-0571199839
Publisher: Faber and Faber, Inc
Date (Month/Year): May 2000
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Theresa agrees to go on a brief blind date with Tony, a man who knows a friend of a friend. Over a drink, the two engage in stilted small talk . . . But when he asks for a follow up dinner date shortly into their conversation, the first red flag emerges.

ACTOR: Theresa is careful to maintain boundaries however, refusing to give out her home phone number and shrugging off his hug in favor of a handshake.

ACTRESS: At the following dinner date she calmly informs him that there will not be a third date. End of experience. Or not . . . Tony’s phone calls become constant and an endless succession of flower bouquets come to her office. He eventually sneaks his way up to her office, asking her to lunch. Theresa assertively tells Tony to leave her alone and never contact her again.

ACTOR: She assumes that she’s seen the last of him, but she’s not so lucky . . .

TOGETHER: Boy Gets Girl by Rebecca Gilman

Theresa's apartment: a small apartment with a futon couch/bed, desk, and lots of bookshelves. It is late Saturday night. THERESA is fully dressed, sitting up in bed, working on a laptop. The phone rings, but she makes no move to answer it. After a couple of rings her machine picks up. Theresa's voice comes on.
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NOTE: ACTOR should play the roles of Tony, Mercer and Beck (in the play Beck is a female officer, but this cutting does not reference a gender)

THERESA'S VOICE: You've reached my machine. Leave a message. (Tony’s voice comes on)

TONY: Hi, it's me again. It's past one and it's too late for you to be out by yourself, I think. I know you don't really want to talk to me or anything, but I'm just worried about you. I'm wondering if you've gone out of town or something. You haven't answered your phone all night. I did what you asked, and I stopped sending you flowers. But anyway, I know you've been working hard lately and I want to do something for you, but you won't let me send you flowers, so I was just thinking, maybe you'd let me cook you dinner? Maybe tomorrow night? I mean, you haven't even seen my place yet. So give me a call when you get in, because I'll be up. Okay? . . . Okay. Bye.

(The machine clicks. THERESA, who has stopped working in the middle of it, starts again. Pause. The phone rings again. Her voice comes on)

THERESA'S VOICE: You've reached my machine. Leave a message.

TONY: It's me again. I just . . . I left that message to call me when you got in and then I just had a thought: maybe you're not getting in. Maybe you're sleeping with somebody else right now. And the thought of that just made me feel like I wanted to throw up. If you're seeing somebody else I just want to know. I don't want you to think you have to spare my feelings, because if you think that, then you must think I'm some pathetic jerk. Which would make me very angry, Theresa, because I don't need your pity. I'm not asking for your pity for one ***** second. I just think that you owe me the truth. (THERESA, who has been staring at her computer through this, suddenly loses it and makes a grab for the phone.)

THERESA: (Snatching up the receiver) Stop calling me! Don't send me things, don't try to see me. Don't ever speak to me again! (She hangs up) Jesus Christ!

(Beat. The phone rings again. Furious, she tries to unplug it, can't get the plug out, then rips the cord from the wall. Silence. She goes back to the bed, sits down. She is shaking. She looks toward the window. She sits for a moment and thinks, then she quickly turns off the lights. In the dark she gets up, goes to the door, and checks it. It's locked. Then she gets a chair and pushes it up under the handle.)

TRANSITION

ACTRESS: According to the National Center for Victims of Crime, 6.6 million people are stalked in each in the United States.

ACTOR: But to go even further . . . 54% of female murder victims had reported stalking to police before they were killed by their stalkers.

ACTRESS: Anyone can be a victim of stalking.

Theresa’s office, the following Monday. She is sitting, looking tired, staring into space. MERCER enters.

MERCER: Hey.

THERESA: Hey, [Mercer].

MERCER: Do you mind if I close the door?

THERESA: No. Go ahead. (Mercer closes the door, sits. - Beat) Is there something wrong?

THERESA: My voice mail was completely full this morning.

MERCER: You're really busy.

THERESA: No, it was full of messages from someone I didn't want to hear from. From over the weekend.

MERCER: Who?

THERESA: Can I . . . if I tell you something, do you promise not to tell anybody?

MERCER: Of course. What's up?

THERESA: Do you remember that guy that came into the office that day?

MERCER: That kind of goofy-looking guy?

THERESA: Yes.

MERCER: Is he the flower guy?

THERESA: Yes.

MERCER: Is he bugging you?

THERESA: He's stalking me. I think. I mean, I don't know what constitutes stalking legally, but if he's not, then he's coming awfully close. I know now he's following me. I mean, he called me all night, Saturday night, before I . . . Well, I ended up ripping the phone out of the wall. Then I turned the light off because I had the feeling he was watching me somehow. And then the first message here was . . . you know there's that time and date stamp, on the messages . . .

MERCER: Yeah.

THERESA: The first message was after that, after two in the morning on Sunday, and he said, "I saw your light was off." So he was watching. I live on the second floor. You can't really see in, I don't think. But it's not that high up.

MERCER: What did he say?

THERESA: Well, I had been screening my calls all night and he had been calling and calling, and I finally picked up the phone and yelled at him, which I shouldn't have done. But then he knew I had been home, so he called here to tell me how angry he was, and every message just gets . . .

MERCER: What?

THERESA: Angrier and angrier. He keeps saying over and over that he wants to hurt me. That he wants me to suffer, like him. That he wants . . . he wants to hurt me.

MERCER: Did you save them?

THERESA: Yes.

MERCER: Can I hear one?

THERESA: (Picks up the phone, punches in a code. Hands the receiver to Mercer.) That's the first one. They go on. (Mercer listens. The message ends and he punches a button for the next one. He listens a while longer, then he looks at Theresa) Do you think I should be scared?

MERCER: How many of these are there?

THERESA: Twenty.

MERCER: I think you should call the police. *********

BECK: (Holding the receiver out) That's the last one. How do I get out of here? (Theresa takes the phone, punches buttons, hangs up.) Don't erase those. Do you have any other messages or letters or anything?

THERESA: There are messages on my machine at home. And he sent me some e-mails, but I deleted them all.

BECK: If he sends you anything else, keep it. And from now on keep a diary of any time he calls, any time you see him. Any contact at all. Write it down, and write down the date and time. The more specific the better.

THERESA: What am I doing this for?

BECK: Well, we can get the restraining order, but I'll tell you up front, it's hard to enforce it. If he doesn't want to be seen, he won't be. I ran a check on him when you called, and he doesn't have any priors, so if all he does is call you again, then we couldn't hold him for that. But if he builds up a record of consistent abuse, then we could definitely charge him.

THERESA: Consistent abuse?

BECK: Abuse of the restraining order. Not of you, necessarily.

THERESA: Great.

BECK: In the meantime, you can take some precautions. Get an unlisted phone number.

THERESA: I had one, he got it.

BECK: Get a new one, and don't give it to anybody except your closest circle. And since he knows where you live, you should go ahead and move.

THERESA: Move?

BECK: Do you have a doorman?

THERESA: No.

BECK: Well, when you move, move to a building with a doorman and get an alarm for your apartment. Also, before you move, I'd go ahead and change your name. Then put the apartment and the phone and everything in your new name.

THERESA: Okay. I don't want to change my name. I'm a writer. I write under this name.

BECK: You'll have to decide that one yourself. Okay, what else. Okay, make sure you vary your route to work and back. Never take the same route two days in a row, but don't fall into a pattern either. And vary your routine as well. If you go to the health club after work, start going before work or during lunch. If you go to church on Sundays, think about changing churches. Some people feel safer buying a gun, but I can't in good conscience recommend that. I've seen too many people shot with their own guns. (Pause) I don't know. This escalated quickly, and I'll be honest, that concerns me.

THERESA: I guess I should have called you sooner.

BECK: Well, you could have called, but honestly, I couldn't have done anything, because he didn't threaten you until now. (Beat) Don't beat yourself up, okay? I tell all my complainants that. You don't know. You think you can handle him yourself and then all of a sudden he's whacked out on you.

THERESA: I guess I did think I could handle it myself.

BECK: Unfortunately though, the very things you did to try and stop him from bothering you were probably the very things that egged him on.

THERESA: How's that?

BECK: Well, like if you pick up the phone and say, "Don't ever call me again," you think you're being clear, but all he's hearing is "She's talking to me. I still have a chance." And I don't know how you broke up with him-

THERESA: I didn't break up with him. You have to have a relationship before you can break up, and there was none.

BECK: Right. I just meant, I don't know how you left it. If you gave any kind of excuse, or left it open in any way, then he didn't hear you saying "No." He heard you saying "Yes, once this one thing changes, then we can be together." Like if you said you were still hung up on some other guy, or you weren't ready for a relationship. Any of those things you say.

THERESA: I said it was my work.

BECK: See? What you should have said was "I thought it over and I don't want to see you again," and not given a reason even if he asked.

THERESA: This isn't doing me much good right now.

BECK: No, I'm just saying . . . for future reference. (Beat.) Okay. I can't think of anything else right now. The restraining order may very well scare him off. But you should be prepared for the opposite reaction, too.

THERESA: Which is what?

BECK: Well, that it pisses him off and he comes back at you even harder. That happens and it's another reason to take precautions.

THERESA: What if none of this works, then what? I mean, what's the worst that can happen? What's the worst thing you've ever seen?

BECK: You don't want to know.

THERESA: Have you seen people killed?

BECK: I've seen that.

THERESA: That wasn't the worst thing? (Beat) Detective? (Pause)

BECK: You don't want to know. (Handing her a card) That's got a 1-800 number on it, so you can reach me from wherever. **********

MERCER: When you look at Tony, he looks like a normal guy. And in a lot of ways, he is a normal guy. Or at least he's doing what normal guys do in movies. It's a classic romantic plot. First the guy sees the girl. He thinks she's beautiful; she has long brown hair and big brown eyes, she's just the sort of woman he's dreamed about, so bang-he falls in love with her. But there's some obstacle to his love. Like the woman's dating some jerk who's completely wrong for her. So our guy has to prove himself to her. And to do that, he starts following her around. He spies on her, and as he watches her, he becomes convinced that if they could only be together, she would love him. So he gets aggressive. He bombards her with flowers and rents a billboard to declare his love, then bursts in on her wedding and tells her she's making a terrible mistake. And she comes around. She dumps the jerk and at the end of the story she's kissing the guy. Even though the guy has basically been stalking her, his perseverance pays off. He gets the girl. So this Tony guy is probably wondering, Why don't I get the girl? A lot of guys are out there wondering, Why don't I get the girl?

********** Theresa's office, the next day. She and Mercer are talking.

THERESA: They found another letter in my apartment. In the medicine cabinet. They think he wanted me to find it when I was alone. He said he wants to put a wire around my throat and pull it until it . . . until it slices through my throat.

MERCER: Jesus.

THERESA: There were other details, but I chose not to hear them.

MERCER: Well, what are they going to do?

THERESA: They'll put out a warrant for his arrest, but they probably won't find him unless he messes up somehow and draws attention to himself.

MERCER: Unless he tries to attack you.

THERESA: Pretty much, yeah.

MERCER: Jesus.

THERESA: He's already won. Whatever it was he wanted me to feel, I feel it.

MERCER: You're terrified.

THERESA: No, it's more than that (Beat) It's like when I go running in the park . . . if I still could . . . every week or so, not every day, but every week or two some guy drives by or walks by and says something to me. You know, "Nice ass" or "I want to jog with you." It's been happening since I was twelve, so I know how to ignore it. But every tenth time or so, I still feel it. I feel reduced. I feel like everything that I know about myself-that I'm a good writer and I've read a lot of books, and . . . I like fall better than spring or . . . I haven't had many friends really since my parents died, even though that was a long time ago-everything I know about myself, just gets wiped out. It's like I'm just this thing running down the sidewalk. I'm not me anymore. I'm just this thing. (Beat) And that's how I feel now. All the time. (Long pause)

MERCER: Well, one thing I can tell you . . . I'm your friend. I see you and I know it's you. I know you're there. I do.

THERESA: I know. (small beat) It's not enough.
```

---

## IC-0731: Bridge to Terabithia (The Book)

- Title: Bridge to Terabithia (The Book)
- Author (byline): Katherine Paterson
- Work: Not specified
- Publisher: Harper Trophy
- Publication date as stated: June 1987
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS, JESSE, NARRATOR 1, LESLIE, NARRATOR 2, TOGETHER, MAY BELLE, JESSE’S FATHER, LESLIE’S FATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1750
- Already set (do not supply): none

### Source block (context only)

```text
Author: Katherine Paterson
ISBN: 978-0064401845
Publisher: Harper Trophy
Date (Month/Year): June 1987
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Jesse Aaron's greatest ambition is to be the fastest runner in the fifth grade.

ACTRESS: But on the first day of school, a new kid, a girl, boldly crosses over to the boy's side of the playground and outruns everyone.

ACTOR: That's not a very promising beginning for a friendship, but Jesse Aarons and Leslie Burke become inseparable.

ACTRESS: It doesn't matter to Jesse that Leslie dresses funny, or that her family has a lot of money -- but no TV. Leslie has imagination and she is fearless!

ACTOR: For Jesse, who is afraid of everything . . . Leslie was everything he wanted to be.

ACTOR: Together, they create Terabithia, a magical kingdom in the woods where they reign and the only limits are their imaginations.

TOGETHER: Bridge to Terabithia by Katherine Paterson
```

### Performance text (classify this)

```text
Suggested Roles: ACTOR: Jesse, Narrator 2, Leslie’s Father

ACTRESS: Narrator 1, Leslie, May Belle, Jesse’s Father

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

JESSE: (Pg 2) (while running) I get up early every day to run. I figure if I work at it, I could be the fastest runner in the fifth grade when school opens up. I have to be the fastest. . . not one of the fastest or next to the fastest, but the fastest. The very best. (Pg 20) Watch out Wayne Pettis. . . I’ll get you. You can’t beat me.

NARRATOR 1: (Pg 5) Wayne Pettis would be in the sixth grade with the rest of the big guys. [But] anybody had a chance to be the fastest runner, and by Miss Bessie, this year it was going to be Jesse Oliver Aarons, Jr.!

LESLIE: (Pg 49-50) Do you know what we need? We need a place. . . just for us. It might be a whole secret country and you and I would be the rulers of it.

JESSE: Ok. . . Where would we have it?

LESLIE: Over there in the woods where nobody would come and mess it up. (getting excited) I know. . . it could be a magic country like Narnia, and the only way you can get in is by swinging across on this enchanted rope. Come on. . . let’s find a place to build our castle stronghold. . . (searching) How about right here?

JESSE: (Pg 51) (nodding vigorously and catching Leslie’s excitement) Sure! This will be a good place to build. . .

NARRATOR 2: Leslie named their secret land “Terabithia,” and she loaned Jess all of her books about Narnia, so he would know how things went in a magic kingdom.

LESLIE: (Pg 52) You should draw a picture of Terabithia for us to hang in the castle.

JESSE: (gazing in wonder at their surroundings) I can’t . . . I just can’t get the poetry of the trees.

LESLIE: Don’t worry. You will someday!

NARRATOR 2: He believed her because, there in the shadowy light of the stronghold, everything seemed possible. They owned the world and no enemy could ever defeat them.

JESSE: (Pg 60) I used to think this place was haunted.

LESLIE: Oh, it is. But you don't have to be scared. It's not haunted with evil things.

JESSE: How do you know?

LESLIE: You can just feel it. Listen. (they close their eyes, then Leslie continues solemnly) This is not an ordinary place. Even the rulers of Terabithia come into it only at times of greatest sorrow or of greatest joy. We must strive to keep it sacred. It would not do to disturb the Spirits. *****Scene change *****

LESLIE: (Pg 103) I’ve never been to a church before . . . do you think your parents would let me go with you?

JESSE: You’d hate it. It’s boring (then skeptically) You can’t wear pants

LESLIE: (indignantly) I’ve got some dresses, Jess Aarons!

TOGETHER: (holding a hymn book; they sing a few lines – pick your favorite hymn (Jesse is bored; Leslie is enthralled)

LESLIE: (Pg 107-109) (after church) I’m really glad I came. (Jess looks at Leslie in unbelief) It was better than a movie!

JESSE: You’re kidding.

LESLIE: No, I’m not. That whole Jesus thing is really interesting isn’t it? All those people wanting to kill him when he hadn’t done anything to hurt them. It’s really kind of a beautiful story – like Aslan.

MAY BELLE: It ain’t beautiful. It’s scary, nailing holes right through somebody’s hand.

JESSE: May Belle’s right. It’s because we’re all vile sinners God made Jesus die.

LESLIE: Do you think that’s true?

JESSE: It’s in the Bible, Leslie.

LESLIE: (looks like she’s going to argue, then shakes her head) It’s crazy isn’t it? You have to believe it, but you hate it. I don’t have to believe it and I think it’s beautiful.

MAY BELLE: You gotta believe the Bible, Leslie.

LESLIE: (a genuine question) Why?

MAY BELLE: (eyes huge) ‘Cause if you don’t believe the Bible, God’ll damn you to hell when you die.

LESLIE: I don’t believe it. (turns to Jesse) I don’t even think you’ve read the Bible.

JESSE: I’ve read most of it. (grinning) S’bout the only book we got around our place.

LESLIE: OK, but I still don’t think God goes around damning people to hell.

MAY BELLE: But Leslie. . . What if you die? What’s going to happen to you? *****Scene change *****

NARRATOR 2: (Pg 110) On Easter Monday, the rain began in earnest. (Pg 112) When they got to the bank of the creek, they stopped.

NARRATOR 1: It was an awesome sight. Like in The Ten Commandments on TV when the water came rushing into the dry path Moses had made and swept all the Egyptians away . . .

NARRATOR 2: The creek was a roaring eight-foot-wide sea, sweeping before it great branches and logs swirling them about like Egyptian chariots, the hungry waters sometimes leaping the banks, daring them to try to confine it. (Pg 115-118) For Jess the fear of crossing rose with the height of the creek [but] Leslie never seemed to hesitate.

LESLIE: (playing the role of Queen of Terabithia) Dost know what is in my mind, O King? Methinks some evil being has put a curse on our beloved kingdom.

JESSE: Damn weather bureau.

LESLIE: (not wanting to kid) Let us go into the sacred grove and inquire of the Spirits what this evil might be and how we must combat it. For I perceive that this is no ordinary rain that is falling upon our kingdom. (lifting her arms and face toward the green canopy above) O, Spirits of the grove, we come on behalf of our beloved kingdom which lies even now under the spell of some evil, unknown force. Give us, we beseech thee, wisdom to discern this evil, and power to overcome it.

JESSE: (also raising his arms) Um. Uh. Um. Yes. Please listen, thou Spirits. *****Scene change *****

NARRATOR 1: (Pg 119) It had seemed to Jess when he went to bed Wednesday night that he could relax, that everything was going to be all right, but he awoke in the middle of the night with the horrible realization that it was still raining.

NARRATOR 2: He would have to tell Leslie that he wouldn't go to Terabithia. He was obviously not worthy to be king of Terabithia. It wasn’t so much that he minded telling Leslie that he was afraid to go; it was that he minded being afraid.

NARRATOR 1: (Pg 118) He was obviously not worthy to be king of Terabithia. Whoever heard of a king who was scared of tall trees and a little bit of water?

JESSE: (to himself) All I gotta do is say, “Leslie, I don’t wanta go over there today.” Just like that. Easy as Pie.

NARRATOR 1: (Pg 119) He hardly slept the rest of the night, listening to the horrid rain and knowing that no matter how high the creek came, Leslie would still want to cross it. *****Scene change *****

NARRATOR 2: (Pg 130) He was all the way into the kitchen before he realized something was wrong.

JESSE’S FATHER: (Pg 131-132) (quietly) I’m real sorry, boy. They found the Burke girl this morning down in the creek.

JESSE: No. Leslie wouldn’t drown. She could swim real good.

JESSE’S FATHER: That old rope you kids been swinging on broke.

JESSE: (shaking his head) No. No! I don’t believe you. You’re lying to me!

MAY BELLE: (echoing) But, Leslie, what if you die?

JESSE: (looking about wildly) No. It’s a lie. Leslie ain’t dead.

JESSE’S FATHER: They think she musta hit her head on something when she fell. I’m really sorry, son. (Jesse begins to cry) (Pg 139) Your mother and I thought we ought to go down to the neighbors and pay respects. (clears his throat) I think it would be fitting for you to come, too. Seeing's you was the one that really knowed the little girl.

JESSE: (talks to Leslie in his mind) You know something weird?

LESLIE: What?

JESSE: I was scared to come to Terabithia this morning. (angrily) You think it's so great to die and make everyone cry and carry on. Well, it ain't. *****

NARRATOR 1: (Pg 144-146) He heard his father ask quietly over his head about “the service.”

LESLIE’S FATHER: [We] decided to have the body cremated and are going to take the ashes to the family home in Pennsylvania tomorrow.

NARRATOR 1: Cremated. Something clicked inside Jess's head. That meant Leslie was gone. Turned to ashes. He would never see her again. Not even dead. Never. How could they dare? Leslie belonged to him. More to him than anyone in the world. No one had even asked him.

JESSE: (anguished, to the audience) I was the only one who really cared for Leslie. But she went and died just when I needed her the most. She went and left me. She went swinging on that rope just to show me that she was no coward.

LESLIE: (laughing) So there, Jess Aarons!

JESSE: (sadly) She tricked me. She made me leave my old self behind and come into her world, and then before I was really at home in it but too late to go back, she left me stranded there -- like an astronaut wandering about the moon. Alone.

NARRATOR 1: He was never sure just when he left, but he remembered running up the hill to his own house with angry tears streaming down his face. He raced into his bedroom and retrieved the papers and paint that Leslie had given him at Christmastime.

NARRATOR 2: He ran out the kitchen door and down to the stream without looking back. Above the crab apple tree, the frayed end of the rope swung gently.

LESLIE: (Pg 60) (echoing) Even the rulers of Terabithia come only at times of greatest sorrow or of greatest joy. . .

JESSE: (Pg 146-147) (screaming something without words, he flings the papers and paints into the water)

NARRATOR 2: There was nowhere to go. Nowhere. Ever again.

JESSE’S FATHER: (who had followed Jesse) That was a damn fool thing to do.

JESSE: (crying hard, barely able to breathe) I don’t care! I don’t care! I hate her. I wish I’d never seen her in my whole life.

JESSE’S FATHER: (pulling him close, comforting) There. There. Sssh. . . Hell ain’t it?

JESSE: Do you believe people go to hell, really go to hell, I mean?

JESSE’S FATHER: Lord, boy, don’t be a fool. God ain’t gonna send any little girls to hell.

JESSE: (softly) She wouldn't have been eleven until November. . . *****The next day *****

NARRATOR 1: (Pg 150) He woke up Saturday morning with a dull headache. (Pg 160) Before Leslie came, he had been a nothing – a stupid, weird little kid trying to act big – trying to hide a whole mob of foolish little fears.

NARRATOR 2: It was Leslie who had taken him into Terabithia and turned him into a king. [He felt called to Terabithia] (Pg 151-152) If was still Terabithia . . .

NARRATOR 1: The castle stronghold was dark and damp, but there was no evidence there to suggest that the queen had died. He felt the need to do something fitting. But Leslie was not there to tell him what it was. The anger which had possessed him yesterday flared up again.

JESSE: Leslie, I’m just a dumb dodo and you know it. What am I supposed to do? (his voice catches) Leslie, were you scared? Did you know you were dying? Were you scared like me?

NARRATOR 1: A picture of Leslie being sucked into the cold water flashed across his brain. (Pg 160-161) She wasn’t there. . . It was up to him to pay back the world in beauty and caring what Leslie had loaned him.

JESSE: (takes a deep breath) Well, you just have to stand up to your fear and not let it squeeze you white. Right, Leslie?

LESLIE: Right.

JESSE: (Pg 152-153) (a sudden idea) A funeral wreath for the queen…

NARRATOR 1: He sat in the clear space between the bank and the first line of trees and bent a pine bough into a circle, tying it with a piece of wet string from the castle. He picked spring beauties from the forest floor and wove them among the needles.

JESSE: (reverently he kneels and offers up the wreath to the Spirts) Father, into Thy hands I commend her spirit.

NARRATOR 1: Leslie would have liked those words. They had the ring of the sacred grove - - the grove in Terabithia.
```

---

## IC-0732: The Brothers Grimm Spectaculathon

- Title: The Brothers Grimm Spectaculathon
- Author (byline): Don Zolidis
- Work: Random Acts of Comedy, Pg 303
- Publisher: Playscripts, Inc.
- Publication date as stated: Aug 2011
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR 1, NARRATOR 2, GIRL, DIRT MERCHANT, ENCHANTRESS, THE DEVIL, PRINCE, RAPUNZEL, DWARF 1, DWARF 2, SNOW WHITE, WITCH, MIRROR, CINDERELLA, ACTOR, STEPSISTER 1, STEPSISTER 2, HERALD, PRINCE CHARMING
- Teaser before the introduction: Yes
- Spoken words (computed): 1648
- Already set (do not supply): none

### Source block (context only)

```text
Author: Don Zolidis
Book: Random Acts of Comedy, Pg 303
ISBN: 978-0981909974
Publisher: Playscripts, Inc.
Date (Month/Year): Aug 2011
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: So . . . (looks at an imaginary pocket watch) I don’t have time today to present all 209 stories. (sad face) – But I do have time for Rapunzel!

ACTRESS: (Sings: Ah, ah, ah, ah, ah, ah, ah, ah)

ACTOR: Snow White ACTRESS: (Mirror Mirror on the wall . . . )

ACTOR: and Cinderella ACTRESS: (Bippity, boppity boo!)

ACTOR: Hold onto your seats . . .

ACTRESS: This is going to be one wild ride!

TOGETHER: The Brothers Grimm Spectaculathon by Don Zolidis
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actor: Narrator 2, Dirt Merchant, Enchantress, The Devil, Prince, Witch, Actor, Stepsister 1 and 2

Actress: Narrator 1, Girl, Rapunzel, Dwarf 1 and 2, Snow White. Mirror, Cinderella, Herald, Prince Charming

NARRATOR 1: (Pg 307-308) Hello and welcome to the Brothers Grimm Spectaculathon!

NARRATOR 2: (Exploding onto the stage) Sunday Sunday Sunday! It's EXTREME! See! Monster slaying action as the three-headed pig battles the wolfo-bot in a bone-crushing cage match of death. They'll huff and they'll puff, and they'll kick some iron! Aaaaaaahh!

NARRATOR 1: Okay, stop. We're not doing that. NARRATOR 2: Flames! Flames!

NARRATOR 1: Enough, [actor's name]. You're weirding them out.

NARRATOR 2: I'm EXTREME.

NARRATOR 1: No you're not. Can we just do the show?

NARRATOR 2: (pouts then assumes a more reserved demeanor)The Brothers Grimm were brothers named Grimm. They are dead. But in the period before they died the Brothers Grimm wrote 209 fairy tales

NARRATOR 1: These stories have become extremely popular. We all know them today.

NARRATOR 1: (Pg 309-310) So . . . Once upon a time there was a girl

NARRATOR 2: And she was beautiful-

NARRATOR 1: Because no one cares about ugly people.

NARRATOR 2: I care about ugly people.

NARRATOR 1: Well no one cares about you. Anyway, there was a girl . . . (GIRL enters in dramatic fashion.)

NARRATOR 2: And she was poor.

GIRL: Oh I am poor.

NARRATOR 2: Dirt poor.

NARRATOR 1: She couldn't even afford dirt. (DIRT MERCHANT enters.)

DIRT MERCHANT: Dirt for sale! Dirt for sale! Hey, you! Get off the merchandise! (He exits.)

GIRL: (Crying) (An ENCHANTRESS enters.)

ENCHANTRESS: Excuse me-but I couldn't help overhearing your tale of misery and woe. Tell you what-I will grant you your heart's desire if you give me one small thing.

GIRL: That sounds like a great bargain. I won't even ask what the small thing is because I'm so innocent and trusting!

ENCHANTRESS: Excellent. (She makes a magical signal and vanishes)

GIRL: What a nice lady. (THE DEVIL enters.)

THE DEVIL: Hey there hot stuff. Oh wait, that's me. Ha ha ha ha! Now, I happened to overhear your tale of misery and woe and I'm here to help.

GIRL: Well actually I just-

THE DEVIL: Just sign this one small contract and you shall conceive a daughter so beautiful the very earth will want to kiss her. But in a platonic way.

GIRL: That sounds like a great idea. (She signs the contract.)

THE DEVIL: Moo ah ha ha ha ha ha! (He looks around. Then runs off)

NARRATOR 1: (Pg 311- It was a good day for the girl. She fell in love with a prince.

PRINCE: (PRINCE enters.) Hey, you're hot!

GIRL: I am hot.

PRINCE: Let's get married!

GIRL: Score!

NARRATOR 2: She grew very rich.

GIRL: Ha ha! Score!

NARRATOR 2: And she conceived a child.

GIRL: Whoah! How did that happen?

NARRATOR 2: Well, you see kids, when a prince and a princess love each other very much-

NARRATOR 1: Through magic. The magic of The Devil. That’s where babies come from!

NARRATOR 2: (Pg 312-313) Years passed. And she grew into a beautiful young teenager, Rapunzel.

GIRL: Darling, we're going to have dinner so wash your hands.

RAPUNZEL: You can't tell me what to do!

PRINCE: Don't talk to your mother that way. She sold her soul to the Devil just to have you-

RAPUNZEL: I don't care! I didn't ask to be born!

NARRATOR 1: And just then.

ENCHANTRESS: I have returned.

THE DEVIL: Your time is up.

GIRL: What do you want?

ENCHANTRESS: (as they fight over Rapunzel) Your child.

THE DEVIL: Your child.

RAPUNZEL: STOP!! Mom!? How many deals did you make?

ENCHANTRESS: (Pg 314) I will take Rapunzel. (She grabs RAPUNZEL)

THE DEVIL: Um ... excuse me? I'm The Devil (He grabs RAPUNZEL.) Lord of darkness? All that? I think I've got a little bit more claim to this girl than some stupid little witch.

ENCHANTRESS: I curse you!

THE DEVIL: I curse you right back! You know what, this is stupid. Tell ya what, if you sign this contract here, I will let you take Rapunzel.

ENCHANTRESS: That sounds like a plan. (She signs the contract.)

THE DEVIL: Moo ah ha ha ha! And I disappear in a cloud of brimstone!

ENCHANTRESS: Well, come along Rapunzel.

RAPUNZEL: Where are we going?

ENCHANTRESS: I built this great tower for you.

GIRL: Run along dear.

RAPUNZEL: But Mom. I don't want to go with the evil Enchantress

GIRL: Yeah and I didn't want to raise a spoiled brat. But sometimes you don't always get what you want. Unless you make a deal with The Devil. See ya.

NARRATOR 2: So the Enchantress took Rapunzel and locked her in a high tower without stairs or door. *******

NARRATOR 2: (Pg 320-321) Once upon a time. There was a dwarf.

DWARF 1: I prefer little person.

NARRATOR 1: In fact, two dwarves. And these dwarves worked all day in the mines.

DWARF 2: (Singing) Whistle while you work

NARRATOR 1: We can't use that song.

DWARF 2: I do what I want.

NARRATOR 1: No it's like copyrighted, we can't use it. The Mouse will sue us. So the dwarves worked in the mines, they sang their little song and then one day they came home to find- (Enter SNOW WHITE. She falls asleep.)

DWARF 1: What the heck is that thing? (menacingly) I'm going to chop you up and eat you.

NARRATOR 1: Time out. Time out.

DWARF 1: What? I'm just going with what my character wants.

NARRATOR 1: You do not get to eat Snow White. You're not the villain of the story. We are going to do this story as written. Snow White cleans house for the dwarves, then she gets poisoned by an apple, then a prince shows up-

SNOW WHITE: (Waking up) Why do I have to clean the house? Is it because I'm a woman?

DWARF 1: Yes.

NARRATOR 1: No it's because you feel sorry for the little dwarves because they're messy and you have OCD and want to make everything nice.

SNOW WHITE: I don't see why I have to be a maid! I'm the princess here, they should be cleaning up for me.

DWARF 1: All right, she's become too much trouble, let's eat her.

NARRATOR 1: (Pg 323) And moving on.

SNOW WHITE: (Pg 309) Once upon a time there was a beautiful girl. (Pg 323) She was the most beautiful girl in the entire kingdom. But her stepmother was jealous. (WITCH enters)

WITCH: Snow White.

SNOW WHITE: Stepmother.

WITCH: I do believe you're putting on weight.

SNOW WHITE: Not on this body, sister. These curves are tight and streamlined

WITCH: I think you might need to tweeze your eyebrows.

SNOW WHITE: My eyebrows are sculpted like a block of clay in the hands of a blind god of sculpting eyebrows. . . . (looks concerned) Who writes this stuff? (Snow exits)

WITCH: Mirror, mirror, on the wall. Who's the fairest of them all

MIRROR: (A drawn-out ghostly voice) Well it's certainly not you.

WITCH: Curses!

MIRROR: Hey that's a good idea. You should try that

WITCH: (Pg 324) Snow White.

SNOW WHITE: Stepmother.

WITCH: How about an apple as a peace offering?

SNOW WHITE: When are you going to learn Stepmother, that we women shouldn't be judged by our surface beauty but rather by the contents of our brains?

WITCH: Um ... that's just stupid.

PRINCE: Hey I was just in the neighborhood looking for a girl in a coma to make out with (Snow White grabs PRINCE and bends him over backward for a kiss) Whoah! You're very forward.

SNOW WHITE: I'm a modern woman. Come on, let's get married.

NARRATOR 2: And they all lived happily ever after and avoided traditional gender roles. And the seven little dwarves cooked for them, cleaned the house, and did all that other junk that Snow White was supposed to do in the story. The end. ******

NARRATOR 2: (Pg 309) Once upon a time. (Pg 330) [Cinderella’s] mother died and her father remarried.

CINDERELLA: (Pg 329) (enters, overacting) I am orphaned! Oh I am sad!

ACTOR: (Pg 330-332) (An ACTOR enter.) Hold on! We [can’t] do this one

NARRATOR 2: Well, I guess we can skip it then.

CINDERELLA: (CINDERELLA stops acting) NO WE ARE NOT SKIPPING IT. We are going to tell my story, OR I WILL TEAR OUT YOUR TINY HEART, GOT IT?

ACTOR: Yes, Ma'am.

CINDERELLA: Thank you.

NARRATOR 2: Okay, so, her mother died and her father remarried

CINDERELLA: (Overlapping) Mother? Where are you mother? Are you dead?

NARRATOR 2: Now, Cinderella's stepmother had two daughters, both equally beautiful-

CINDERELLA: (CINDERELLA raises her hand) I'm sorry. I think you've got that wrong. I'm the pretty one. They're quite hideous.

NARRATOR 2: Says here they're beautiful too.

CINDERELLA: I think I know my story, thank you. Oh they are so mean . . . so mean.

STEPSISTER 1: (The two WICKED STEPSISTERS enter) Look what the cat dragged in.

STEPSISTER 2: Does it smell in here, or is it just her?

STEPSISTER 1: Oh Cinderella. I need to get ready for the ball

CINDERELLA: What ball?

STEPSISTER 1: The ball being thrown by Prince Charming.

STEPSISTER 2: He's so charming. When I see him I just want to grab his little tights-wearing bottom

CINDERELLA: Can I come?

STEPSISTER 1: Of course you can ... NOT! I'm so hot.

STEPSISTER 2: I'm gorgeous. (Stepsisters exit)

CINDERELLA: (Overacting) Life. So unfair. The room is spinning. Why, God, why? Why am I just a servant - a slave! Lower than the dust. I shall now cry myself to sleep as I do every night. (She cries)

NARRATOR 2: (To the audience) She thinks the Oscar committee is watching.

CINDERELLA: (Pg 333) How can life be so cruel! WHY?!!!! (She hears a sound) What's that? My fairy godmother?

NARRATOR 2: Nope. We're going by the original. There's no fairy godmother.

CINDERELLA: Well, I can't do this without a fairy godmother. Who's going to turn the pumpkin into a coach?

NARRATOR 2: You walk there.

CINDERELLA: What?! I'm Cinderella! (She stomps off)

NARRATOR 2: (Pg 335) Just then Cinderella's two wicked stepsisters arrive [at the ball]

STEPSISTER 1: Cinderella! What are you doing here?

STEPSISTER 2: You suck!

HERALD: (Pg 336-338) (Blowing imaginary horn) Dun de dun dun! His royal highness, the Prince! (The stepsisters go wild)

PRINCE CHARMING: (with a British accent for no apparent reason) 'Ello there. We're having a nice time, are we? Blimey. She's gorgeous. Who's that minx?

CINDERELLA: My name's Cinderella.

PRINCE CHARMING: Right-o. Come here and give us a taste, love. (PRINCE CHARMING and CINDERELLA begin to dance – He is REALLY bad)

CINDERELLA: Oh Prince. Stop. You're embarrassing me.

NARRATOR 2: And they danced all night long. (Stepsister wail and stomp off)

CINDERELLA: What are these feelings? Could it be . . . love? (Clock begins to strike, Cinderella panics and runs off, losing her shoe in the process, the prince picks it up, has an idea and exits)

ACTOR: Can we skip to that part please?

NARRATOR 2: You know what? Fine. A little of this, a little of that, the prince stops by with a shoe looking for a girl who fits it.

PRINCE CHARMING: 'Ello then. Any of you darlings lost a shoe?

STEPSISTER 1: Oh I did. I did! Let me see that! (She takes the shoe.)

NARRATOR 2: And of course, her foot was too big, so she chopped off her big toe.

STEPSISTER 1: (Blood-curdling scream) Aarrrrrrrrr- rrrrrrrrrgghghgghghg! (She limps) It . . . fits . . .

PRINCE CHARMING: Say, what's all this then? There's blood everywhere. (He wrestles the shoe off her foot)

STEPSISTER 1: I popped a zit. On my foot.

PRINCE CHARMING: You chopped off your toe, you did!

STEPSISTER 2: May I please try the shoe. (Prince shrugs and hand over the shoe)

NARRATOR 2: The shoe didn't fit either. So she did the only sensible thing and chopped off her heel.

(Blood-curdling scream)

STEPSISTER 2: Arrghgghghffhfhgh! I'm . . . fine! (She limps See. . .it fits.

PRINCE CHARMING: Is that blood on your foot?

STEPSISTER 2: I cut myself shaving. I have hairy feet. Like a hobbit.

PRINCE CHARMING: You cut off your heel you daft wench!

STEPSISTER 2: I did it for you! (Prince takes the show from Stepsister 2)

PRINCE CHARMING: 'Ello there. I realize several of the ladies in this here house have chopped off body parts to fit in this here shoe, but I was just wondering if anyone else fit in it. You see, I'm not very smart, but I make up for it by being very persistent. It makes me ideal to run the government. (CINDERELLA runs to him.)

CINDERELLA: I will try the shoe.

PRINCE CHARMING: It fits!

CINDERELLA: My love!

PRINCE CHARMING: It is you!

CINDERELLA: It is I!

NARRATOR 2: And they lived. Happily. Ever. After.
```

---

## IC-0733: Bullet Always Wins

- Title: Bullet Always Wins
- Author (byline): Erik Christian Hanson
- Work: The Best New Ten-Minute Plays 2021, Pg 51-58
- Publisher: Applause
- Publication date as stated: Nov 2021
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TIME, AUTHOR'S NOTE, TEACHER, BULLET
- Teaser before the introduction: Yes
- Spoken words (computed): 862
- Already set (do not supply): none

### Source block (context only)

```text
Author: Erik Christian Hanson
Book: The Best New Ten-Minute Plays 2021, Pg 51-58
ISBN: 978-1493060450
Publisher: Applause
Date (Month/Year): Nov 2021
Sources for information contained in the Introduction
NOTE: This information will need to be updated for currency.
* School Shootings This Year: How Many and Where
https://www.edweek.org/leadership/school-shootings-this-year-how-many-and-where/2023/01
** School shootings in the US: Fast facts by Alex Leeds Matthews, CNN
https://www.cnn.com/2023/09/22/us/school-shootings-fast-facts-dg/index.html
```

### Introduction (context only: never use it for content warnings)

```text
According to an Education Week analysis, in 2022 fifty-one school shootings took place on K-12 campuses -- the most in a single year since 2018. The tragedy at Robb Elementary School in Uvalde, Texas, was the deadliest school shooting since Sandy Hook in 2012 -- 19 children and two teachers were killed. Since then, President Joe Biden signed into law the first major federal gun legislation in nearly 30 years. The bipartisan bill includes measures to keep weapons out of the hands of dangerous people as well as hundreds of millions of dollars in additional funding for school safety and mental health resources.*

Fast forward to 2023. With the new law and additional funding, the situation has improved, right? No. According to the most recent data compiled by CNN, as of October 3, 2023, at least 39 school shootings have occurred at America’s K-12 schools so far this year.** It is clear that more must be done. Until we pass comprehensive gun control in the US the . . .

Bullet Always Wins by Erik Christian Hanson
```

### Performance text (classify this)

```text
CHARACTERS • TEACHER -- any age, female, any race. • BULLET -- any age, any gender, any race.

TIME: A few days after yet another school shooting.

AUTHOR'S NOTE: Teacher is rambling due to her mental state. She never acknowledges the presence of Bullet.

Lights up. A dark room. A TEACHER stares off into space. A BULLET, shiny and lethal, is in the corner.

TEACHER: The bullet missed my face by a hair.

BULLET: I was closer than that.

TEACHER: I can still hear the ringing. (A prolonged ringing sound comes from BULLET's direction.)

BULLET: That was me, sorry. (He laughs.)

TEACHER: Why can't I get it out of my head?!

BULLET: It is my intention to haunt you.

TEACHER: I . . .

BULLET: And every other breathing person.

TEACHER: I . . .

BULLET: Spit it out.

TEACHER: I don't think I should set foot inside a school again.

BULLET: I second that notion.

TEACHER: I can't set foot inside a school again.

BULLET: That was my goal.

TEACHER: But I have to.

BULLET: You are not ready.

TEACHER: I cannot let this win.

BULLET: I always win.

TEACHER: My coworkers . . .

BULLET: Plenty of them are dead.

TEACHER: . . . would want me . . .

BULLET: I got nine of them.

TEACHER: . . . the students would want . . .

BULLET: And sixteen of those little buggers.

TEACHER: . . . me. . .

BULLET: They would want you to quit.

TEACHER: I need to be strong.

BULLET: Strong is overrated.

TEACHER: I need to . . .

BULLET: Quit.

TEACHER: I . . .

BULLET: QUIT.

TEACHER: I . . .

BULLET: Three of your coworkers did.

TEACHER: . . . need to be a symbol of . . .

BULLET: They left the field of education for good.

TEACHER: . . . strength.

BULLET: What strength exists in that choice?

TEACHER: I . . .

BULLET: Because of me, the school is bringing in extra counselors and therapy dogs.

TEACHER: This is what teachers do.

BULLET: Teachers are going to leave their profession in droves.

TEACHER: Teachers keep going amidst all odds.

BULLET: Perhaps, but most teachers now live with the daily fear that I provide. All schools will be shut down after my work is done.

TEACHER: I have to join a group that says, "No, this will not continue.

BULLET: (Amused) Is there a group out there that says that?

TEACHER: This cannot continue.

BULLET: Oh, but it will.

TEACHER: We can't let it.

BULLET: You and others are no match.

TEACHER: We . . .

BULLET: Should retire.

TEACHER: . . . must find ways to . . .

BULLET: There are no ways. There is only surrender.

TEACHER: . . . protect our children's futures.

BULLET: They have no futures.

TEACHER: That is all that matters.

BULLET: Self-preservation is what matters, honey.

TEACHER: They are all that matter.

BULLET: They are not worth your sacrifice.

TEACHER: They . . .

BULLET: Mean nothing.

TEACHER: . . . are. . .

BULLET: Ants in the overall scheme of things.

TEACHER: I have to do something!

BULLET: You have to do something? You must do something? I'll tell you what to do. You do this: buy a plane ticket in three days. My next shooting will occur 1,211 miles from here. Do your best to stop it. (Laughs) If you fail, do not fret because the shooting after that will be 379 miles from here. Are you willing to travel to stop me? Are you that committed to this cause? Short of that, you should take early retirement and reserve a stool at the local bar. Current happy hour prices are mind-blowing.

TEACHER: I will be strong. . .

BULLET: Waste of your energy.

TEACHER: I will take a more active role in the lives of my students . . .

BULLET: Waste of your time.

TEACHER: I will. . .

BULLET: Go through life thinking you can change a force as strong as I am, but you will be proven wrong in the end and you know it. Deep down, you know it.

TEACHER: I . . .

BULLET: Know it.

TEACHER: I don't know!

BULLET: You do know.

TEACHER: What can I do?

BULLET: Nothing.

TEACHER: What should I do?

BULLET: Ab-solutely nothing.

TEACHER: Why?

BULLET: Because I always win and you always lose.

TEACHER: The world isn't fair.

BULLET: Duh.

TEACHER: The world . . .

BULLET: Is a series of stories made up of people's daily suffering.

TEACHER: . . . needs a makeover.

BULLET: I am in the process of giving it said makeover. Want to hear how many I will take at the next shooting?

TEACHER: The second amendment . . .

BULLET: Is a thing of freaking beauty.

TEACHER: . . . needs . . .

BULLET: Spoiler alert: it will never be modified.

TEACHER: . . . to be amended . . .

BULLET: The powers that be will never allow it.

TEACHER: . . . the psychiatric field needs . . .

BULLET: Even with better and more timely evaluations, I will be victorious. Have you seen what these counselors do with the kids?

TEACHER: They'll . . .

BULLET: Talk about emotions. Tell the little kiddos not to get stuck on their emotions, play a social-slash-board game, and then send them back to class with a sticker.

TEACHER: But counselors are not the problem.

BULLET: They're part of it.

TEACHER: It has to change. Everything needs to change.

BULLET: Be a part of the so-called change all you like, the results will be the same.

TEACHER: I am going to lead that change.

BULLET: Lead away.

TEACHER: I am that change.

BULLET: All righty . . .

TEACHER: I hope I am that change.

BULLET: You won't be, but it's fun to dream.

TEACHER: Maybe this has all been a dream.

BULLET: I am sorry to report that it is all quite real, and that it is going to get much worse from here on out. More tears. More bloodshed. More confusion. More chaos. More rage.

TEACHER: A dream that I will emerge from and . . .

BULLET: You may have emerged, but you have entered a nightmare, dear. There are no exit doors for this one because I tossed out all the keys.

TEACHER: I can . . . conquer this.

BULLET: Humans don't defeat bullets.

TEACHER: I . . .

BULLET: will earn an "A" for trying.

TEACHER: can do this. I will do this.

BULLET: I wish you luck. Truly. The best of luck.

(He snorts. TEACHER scans her surroundings, hoping a positive answer will come.)

(Blackout.)
```

---

## IC-0734: Bullshot Crummond

- Title: Bullshot Crummond
- Author (byline): Ron House, Dix White, Jake Neville-Andrews, Alex
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: 1974
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SUGGESTED ROLES, ACTRESS, ACTOR, OTTO, LENYA, FENTON, CRUMMOND, ALGY, POLICEMAN, ROSEMARY
- Teaser before the introduction: Yes
- Spoken words (computed): 1680
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ron House, Dix White, Jake Neville-Andrews, Alex Shearman, and Derek
Cunningham
ISBN: 978-0573606458
Publisher: Samuel French, Inc.
Date (Month/Year): 1974
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: The dashing Captain Hugh "Bullshot" Crummond - WWI ace fighter pilot, Olympic athlete, racing driver, part-time sleuth and all-round spiffing chap.

ACTOR: (in character) Men want to be like me and women want to be with me!

ACTRESS: Or, at least, that is the public perception. Whilst he is, indeed, a remarkable man, he is also a bumbling buffoon.

ACTOR: (in character) And it is I who must save the world from the dastardly Count Otto van Bruno, my wartime adversary.

ACTRESS: This parody of low budget 30s detective movies typifies British heroism.

ACTOR: Don't miss the next thrilling installment of this dastardly tale of

TOGETHER: Bullshot Crummond by (alternate authors names) Ron House, Dix White, Jake Neville-Andrews, Alex Shearman, and Derek Cunningham
```

### Performance text (classify this)

```text
Shearman, and Derek Cunningham

SUGGESTED ROLES: Both actors provide sound effects as necessary. Otto and Lenya have pronounced, over-done German accents; All others have pronounced, over-done British accents.

ACTRESS: Lenya, Rosemary, Algy, Policeman (Otto in scene with Crummond)

ACTOR: Otto, Fenton, Crummond, (Lenya in scene with Rosemary)

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Dramatic music begins. The sound of an aircraft engine is heard. The engine begins to splutter. The loud crash of the plane is heard. Heavy music swells.

OTTO: (unrolling a map) We seem to have crashed in the right location. Over there is Netherington Abbey, and there is the town of Tunbridge Wells. And that light over there is from the home of one Professor Rupert Fenton!

LENYA: The famous British scientist?

OTTO: Yes! Who has just made a rather interesting discovery!

FENTON: (The voice of PROFESSOR RUPERT FENTON is heard Off stage.) Hello! Is anybody there?

OTTO: As I planned. The noise of our crash has attracted his attention.

FENTON: (He enters. He is carrying a flashlight.) Hello. Well thank goodness you're safe. I saw your flying machine crash with a deuced big bang.

OTTO: Professor Fenton!!

FENTON: That's strange. How did you know my name?

LENYA: My father and I know many things about you, Professor

OTTO: Including your recent discovery OTTO and LENYA: Ha! Ha! Ha! Ha! Ha! (They hustle FENTON off Right. Sound cross-fades to quiet dawn music.)

CRUMMOND: Wait a moment. What's this? (He bends down and picks up an "imaginary" blade of grass from Center Stage.)

ALGY: It's a blade of grass, Crummond

CRUMMOND: (Examining the grass.) Yes, Algy. But there's a smudge of petroleum on it

ALGY: Well a tractor probably passed this way.

CRUMMOND: Since when have tractors been using high octane aviation fuel? (Music sting.) Look. A footprint. And another. A man's and a woman's. There's been a scuffle round here by the look of things. But why, Algy? Why? I smell intrigue! (He strides manfully off Left. Two sections of the bush Upstage swing apart and OTTO peers out from behind it.)

OTTO: So! Crummond is on to us. Meddling fool of an Englishman-still with a nose for intrigue. But this time, Captain Crummond, you will be nipped in the bud!l (Blackout. Music swells.) [Later that day] CRUMMOND in dressing gown and pajamas posed in silhouette. He is smoking his pipe. Lights build as he opens the door and enters. Moving in time to the music he picks up a letter from the breakfast tray, opens it and glances through it. As the music ends he folds up the letter and strikes a pose with his leg on the chair Center.

CRUMMOND: Extraordinary! (Reading the letter.) "My dear Captain Crummond. I am in terrible trouble, and need your help desperately. My father has recently disappeared, following a mysterious airplane crash!" Mmm! Yours in distress," (He examines the letter.) No name! No address! (Smells letter.) Scented notepaper! (Holds letter up to the light.) Family crest watermark! (Reads.) "In Libris Fentonium Sempere Sum"-In Liberty I Am Always Fenton! Fenton! Now there was a Willy Fenton who served under me in France, and he used to write to his sister named Rosemary. Must be her! But I wonder what the deuced sort of trouble she'd be in?. . . Which makes me wonder what our old friend [Otto] Von Brunno is up to at this very moment. (Turning front.) Hmmmmmmml (Blackout. Dramatic music swells. End of Scene) *****

OTTO: (Into radio.) Black Baron to Iron Fish ... over! Black Baron to Iron Fish come in ... This is Count von Brunno. I am pleased to report that we have captured the British professor Fenton and will rendezvous at Smuggler's Cove at 0300 hours as arranged ... Good ... Over and out Now nothing can interfere with my plans for my conquest of the whole world. (A figure wanders across the stage with a flashlight –her back to OTTO – searching nervously . . . . does not see Otto until she backs into him). Can I help you?

POLICEMAN: Ooh. You gave me quite a turn. Sorry to disturb you sir! We've had reports of radio signals being transmitted to a German submarine from this area.

OTTO: (In a thick German accent.) What! Here on the British coast?

POLICEMAN: I'm afraid so, sir. Looks like spies. You didn't happen to see any foreign looking types pass this way did you?

OTTO: No, I have seen no one.

POLICEMAN: Well, don't worry sir, I'm sure we'll have them by morning ... (OTTO yawns.) Oh, I must have got you out of bed. Well - goodnight …

OTTO: Gute nacht (Clicks his heels.) (OTTO crosses and looks off after POLICEMAN. LENYA enters)

OTTO: (Still looking off.) You see how easy it is to deal with the British police.

LENYA: Otto! This whole scheme is ludicrous! I want to go back to Germany! I want to go to my favorite nightclub- I want to wear furs- I want to wear diamonds ...

OTTO: (Producing an enormous diamond from his pocket.) Like this, Lenya? I

LENYA: Otto! From where did you get such a beautiful diamond?

OTTO: They were not so difficult to-MANUFACTURE! (Music sting.)

LENYA: Manufacture?

OTTO: Yes, Lenya! Although flawless in every way they are synthetic. (He pronounces it "sinsetic.")

LENYA: (Same pronunciation.) Synthetic!? Ah . . . It is all beginning to make sense.

OTTO: With these jewels, we will be able to ruin the international diamond market -

LENYA: Thus causing mass unemployment -

OTTO: Starvation!

LENYA: Hunger!

OTTO: Poverty!

LENYA: And death to thousands of innocent people. (Crossing to OTTO.) Ohl Otto - I'm so happyl When can we begin?

OTTO: (Hesitating.) There are some formalities. Crummond is on to us! (End of scene – Music swells as they exit) ***** After a few moments the music fades and high frequency electronic sounds are heard. Seconds later FENTON is heard screaming in agony and writhing in pain. Over his head is a silver wired dome which is attached to the back of the chair. OTTO stands Upstage Center at the controls of a large electronic panel. LENYA stands Left of the chair. After a few moments the lights stop flashing as OTTO switches off the controls.

OTTO: Well, Professor? Will you manufacture the diamonds?

FENTON: No! Never! I'll never agree!

OTTO: No, Professor? (He switches on the machine and the lights flash even more. FENTON screams. After a few moments FENTON passes out.)

LENYA: Stop, Otto! He's unconscious!

OTTO: (He switches off the machine and the lights stop flashing. Lights fade up to a brighter level.) If he will not manufacture the diamonds, then we must obtain the formula from him!

LENYA: Yes! Then we can manufacture them ourselves. But we will need a new approach.

OTTO: Precisely! (He picks up a syringe from the control desk.)

LENYA: Ah! Cranial Stimulant X!

OTTO: Yes! The most effective truth serum known to man!

FENTON: Do you realize that even the smallest overdose will cause brain stagnation?

OTTO: (Smiling menacingly.) Of course, Professor! (OTTO gives FENTON a shot in the arm. He becomes still for a few moments then starts writhing about jerkily.)

LENYA: It's taking effect!

OTTO: He can no longer resist answering our questions!

LENYA: Professor! Where is your formula!?

FENTON: (Meekly.) In-my-desk-at-The Larches.

OTTO: (Sigh of success.) Aaaah! I must go to "The Larches" immediately, and get the formula.

LENYA: No, Otto! You may be recognized. It is better that entice Miss Fenton here with the formula!

OTTO: But Crummond will surely follow her

LENYA: No! Because the Professor is going to make a little telephone call (Crossing Left.) Professor! We want you to telephone your daughter-inform her that you're safe and send Crummond back to London.

FENTON: No! I won't do it-and you can't make me!

OTTO: We won't have to professor! Because I happen to be an expert at Vocal Re-Iteration. (He picks up a telephone from the control desk.) Hello! Give me ze Larches, please! (Taunting FENTON.) It's ringing! (Otto fakes Fenton’s voice) Hello, Rosemary! It's me, your father. Nol I'm alright. Staying with friends at Netherington Abbey. I want you to London Hugh Crummond send. What? No! Bad line! Goodbye! (Turning to FENTON.) Well, Professor! You made the 'phone call af .. (Reverting to his own voice.) ter all, didn't you? (OTTO laughs. Blackout. Music swells.) ****** As the music fades and lights come up ROSEMARY is speaking on the telephone to whom she believes to be her father.

ROSEMARY: Daddy, where are you? Oh, you're safe. Yes, I will. Goodbye. (to Crummond)

Hugh! It was all a false alarm. Daddy's safe at Netherington Abbey. I'm so happy. And Daddy said you should go back to London. I'm sorry to have wasted your time.

CRUMMOND: Just a minute, Rosemary. Your father didn't know I was here. What were his exact words?

ROSEMARY: His exact words were, "I want you to London Hugh Crummond send."

CRUMMOND: A split infinitive! Now, there's only one language that uses that with such annoying regularity - GERMAN.

ROSEMARY: But Daddy doesn't speak German.

CRUMMOND: He didn't have to, Rosemary, because it wasn't your father who telephoned. Von Brunno! Using vocal reiteration. Don't you see, Rosemary, your father is being held prisoner at Netherington Abbey.

ROSEMARY: What are we going to do now?

CRUMMOND: We'll have to rescue him, but we'll need a plan of attack. Now, there's not a moment to lose. The Von Brunnos want you to take the formula to Netherington Abbey. So that's exactly what you're going to do. ****** The Dungeons of Netherington Abbey. Sabers on wall. As the lights come up LENYA enters fol-lowed by an apparently frightened ROSEMARY.

LENYA: (Actor assumes the persona of Lenya for this scene) Ah! Come this way, Miss Fenton. Did you come alone?

ROSEMARY: Yes! Captain Crummond isn't with me. He's gone in his Bentley to London, and won't be back until next week.

LENYA: So! Give me the formula!

ROSEMARY: No! I won't!

LENYA: Ah! So you do have it?

ROSEMARY: Yes! And you have Daddy! Against his will, no doubt!

LENYA: Don't be silly! He's our guest-and perfectly safe. (PROFESSOR FENTON screams from offstage.)

ROSEMARY: That sounds like Daddy-and you're hurting him ! You're perfectly beastly!

LENYA: Just give me the formula.

ROSEMARY: Very well-here it is! But you must promise to stop hurting Daddy!

LENYA: (Bored.) I promise! (Takes formula.) Now I will get your father! Take a seat until I return!

(LENYA exits Upstage Center. ROSEMARY feigns crying for a few moments. She stops and. looks around. Moves Right and makes strange bird call. An even stranger call replies from offstage followed by CRUMMOND'S entrance)

CRUMMOND: Well done, Rosemary! They've swallowed the bait, hook, line and sinker!

ROSEMARY: What will happen when they discover the formula isn't genuine?

CRUMMOND: Mayhem, Rosemary! Well, you've done your part famously, but from now on, it's man's work! There's not a moment to lose-take off your clothes!

ROSEMARY: I beg your pardon Hugh!

CRUMMOND: I need them as a disguise, the Von Brunnos will be back at any moment.

(Rosemary and Crummond transition off stage)

LENYA: (She enters with FENTON.) In there, Professor. Miss Fenton, here is . . . Miss Fenton! Miss Fenton, it's no use trying to hide. (CRUMMOND emerges from behind screen dressed in ROSEMARY'S clothes.)

CRUMMOND: (In ROSEMARY'S voice.) Are you alright, Daddy? (Lenya rolls her eyes and leaves)

FENTON: Rosemary! Thank goodness you're safe. But what are you doing smoking a pipe?

CRUMMOND: It's not Rosemary, sir, I'm Hugh Crummond.

FENTON: Another of Von Brunno's henchmen I suppose-and you've taken Rosemary's clothing you perverse swine. (He tries to wrestle with CRUMMOND but faints.)

CRUMMOND: No sir, you don't understand ... hang it, he's fainted. Rosemary I must get your father out of here immediately. I'll be back as quick as a wink. Come along Professor, homeward bound for you. (Pantomimes picking up FENTON in a fireman's lift and carries him out.) (Music. OTTO and ROSEMARY enter. Music fades.) OTTO. (angrily) Miss Fenton! I want the genuine formula . . . (ROSEMARY and OTTO circle the table. She picks up her handbag and throws it at him.)

ROSEMARY: You beast!! Captain Crummond!!

CRUMMOND: (Off.) I'm on my way, Rosemary! (He dashes in) Von Brunno! Sly as ever

OTTO: (actress assumes the persona or Otto for the remainder of the scene) Yes, indeed, Captain! (He draws a sword from the panel Left.)

CRUMMOND: Oh, come now! Surely even you would give me a fighting chance?

OTTO: Very well, Captain. Defend yourself. (Throws him a sword.)

CRUMMOND: Now stand clear, Rosemary. This may be bloody! (ROSEMARY runs out.) I do feel I should warn you, Von Brunno, that I was varsity champion at Cambridge. (They fight across the Stage.)

OTTO: I think not, Captain! (He knocks CRUMMOND to the ground, takes his saber and points his own at CRUMMOND'S throat.)

CRUMMOND: A classic example of German honor-running a man through when he's down!

OTTO: Well, I could hardly deny a dying man his last request. Very well, Captain. Stand up!

CRUMMOND: Alright, Von Brunno. (He raises his hands.) You've got me this time-I will admit it!

OTTO: (Takes luger out.) You have a reputation for cunning, Captain Crummond-so I warn you-no tricks!

CRUMMOND: But there is just one small thing you seem to have forgotten. . . .

OTTO: What is that, Captain? ... (CRUMMOND dives for the gun. They wrestle. Otto is shot – actress reassumes the persona of Rosemary).

ROSEMARY: Oh Hugh, you've finished off the Von Brunnos. You've rescued Daddy and you've saved the formula! And you did it all for me ... Hugh, you're wonderful.

CRUMMOND: Not wonderful, Rosemary .... Just BRITISH!
```

---

## IC-0735: Bunny Bunny

- Title: Bunny Bunny
- Author (byline): Alan Zweibel
- Work: Not specified
- Publisher: Villard
- Publication date as stated: Aug 1994
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GILDA, ALAN, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1096
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alan Zweibel
ISBN: 978-0679430858
Publisher: Villard
Date (Month/Year): Aug 1994
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Gilda Radner exploded on television and into American homes every Saturday night, stealing the hearts of millions with her host of brilliantly eccentric characters, now indelibly etched into modern memory,

ACTRESS: (assuming each character’s qualities as they are introduced) like Lisa Loopner

(nerdy snort), Emily Litella, (“Nevermind”) and the ornery Italian news commentator Roseanne Roseannadanna, (It’s always something!”)

ACTOR: That final something for Gilda began in 1986 when she started experiencing fatigue and sharp pains in her upper thighs. 10 months later, she was given the diagnosis – Stage IV ovarian cancer.

ACTRESS: Alan Zweibel, one of the first writers for Saturday Night Live, and Gilda Radner shared a 15-year friendship. A friendship that survived marriages to other people, career changes and cancer.

ACTOR: In this selection, he pays tribute to his best friend who died on his birthday, May 20, 1989, at the age of 42.

TOGETHER: Bunny Bunny
```

### Performance text (classify this)

```text
GILDA: (Pg 1-2) (July 1975) Can you help me be a parakeet

ALAN: Excuse me?

GILDA: I think it could be funny if I stood on a big perch and squished up my face, like this . . .

ALAN: Uh-huh . . . .

GILDA: But I need a writer to help me figure out what the parakeet should say. Could you help me?

ALAN: Sure.

GILDA: I’m Gilda (sticks out her hand)

ALAN: I’m Alan (handshake)

GILDA: I know.

ALAN: How do you know?

GILDA: I took the liberty of asking one of the other writers if he knew the name of the big, nervous-looking guy who’s trying to keep a low profile by sitting in the corner behind the huge potted tree, and he said your name was Alan . . .

ALAN: (Pg 105 – 107) (Gilda looks very sad) Hey . . . what’s the matter?

GILDA: I’m becoming a cliché. One of those show business cliché’s who’s popular with strangers but has no personal life

ALAN: But you were real happy when I spoke to you from Europe.

GILDA: I know.

ALAN: You’re not with that guy anymore? (shakes her head) What happened?

GILDA: He didn’t take me seriously. Look, it’s probably just as much my fault as his. People tell me that I confuse guys, and maybe I do. They see me one way, but then they get to know me and they’re disappointed. I have enough trouble being strong for myself, let alone for someone who gets paranoid when I’m quiet or gets threated when I say “Bunny Bunny.”

ALAN: What’s that?

GILDA: Oh, nothing really . . . it’s silly.

ALAN: Tell me.

GILDA: When I was a little girl, I used to be afraid of the dark. We lived in this big house and at night, there’d be these scary shadows on my bedroom walls. So, what I’d do, was get under the covers and say the words “Bunny Bunny” to protect me from the shadows while I was sleeping.

ALAN: Why “Bunny Bunny?”

GILDA: I really don’t remember. Except that it worked. When I started getting older, I cut back and only had to say it once a week, and finally, once a month – just to be on the safe side. On the first day of every month, the first words I say when I wake up are “Bunny Bunny” to make sure it’s going to be a good month and keep me safe from anything bad that could happen.

ALAN: I understand. It’s not silly. You were a kid, and you . . .

GILDA: I still say it. Does that sound stupid?

ALAN: No.

GILDA: But I’m in my thirties.

ALAN: So?

GILDA: And it still doesn’t sound stupid?

ALAN: No, not at all. **********

GILDA: (Pg 76-77) Could you do me a favor, Zweibel?

ALAN: Sure

GILDA: Promise you won’t get upset? Or hurt . . . because I mean this in a good way.

ALAN: What, Gilda?

GILDA: Could you please not call me Gilda anymore?

ALAN: Excuse me?

GILDA: I mean it.

ALAN: Why don’t you want me to call you Gilda anymore?

GILDA: Because everyone does.

ALAN: Well, isn’t that your name?

GILDA: I’m scared, Zweibel. I’m real excited about *Saturday Night Live.* It’s what I’ve always wanted and it’s fun, but I don’t trust it. It’s a weird feeling having strangers call me by my name and knowing all sorts of things about my life that I never told them. (mimics fans) (Pg 71) “Hey, Gilda, you’re really funny.” “Hey Gilda, my birthday’s also in June.” “Hey Gilda, I also used to be real fat.” (Pg 77) So it would make me feel better if you didn’t call me what everyone else did.

ALAN: . . . Sure.

GILDA: Thanks.

ALAN: Any thoughts about what I should call you?

GILDA: . . . Gilbert.

ALAN: Gilbert?

GILDA: Yeah. Gilbert *************

GILDA: (Pg 165-166) (on the phone) Hello?

ALAN: Robin said that we should talk. . .

GILDA: (interrupts) Hi, Zweibel.

ALAN: She said you weren’t feeling well.

GILDA: And she told me you didn’t believe it.

ALAN: Look, all I know is that I was out there in Los Angeles for two months doing that pilot, and we didn’t see each other, not even once.

GILDA: I know.

ALAN: We made all these lunch plans and dinner plans and we were even supposed to go to that movie premier and I’m supposed to be the one who’s the flake, but you’re the one who broke these dates off every single time.

GILDA: Look, Zweibel, the truth is, I haven’t been feeling well . . .

ALAN: For two months? What’s wrong with you?

GILDA: I have no strength. And I’m tired all of the time. I swear to you, Zweibel, every time you and I made plans I really wanted to see you, but then I ended up going to bed early or going to some doctor and that’s what my whole life has been lately.

ALAN: And what do the doctors say?

GILDA: That I have Epstein-Bar virus. It’s horrible. My mind wants to do everything I always do, but my body is just too tired to do it.

ALAN: Look, honey, I’m sorry if I misread the situation.

GILDA: You wouldn’t be you if you didn’t. ***************

GILDA: (Pg 168-169) (on the phone) Hi, Zweibel

ALAN: Gilbert! What a great surprise! How did you get this number?

GILDA: I called *wife* in New York and she gave it to me. How long are you out here for?

ALAN: Well, the network ordered six episodes of the show. And I’ll be flying back East to be with Robin and the kids on the weekends, *but* there’ll still be plenty of time for you and me to get together, whenever you feel up to it.

GILDA: Good

ALAN: No pressure, and I promise I won’t get mad even if you have to break . . .

GILDA: No, I really want to see you.

ALAN: Great, so you’re feeling better?

GILDA: Zweibel?

ALAN: Yeah?

GILDA: I just found out I don’t have Epstein-Barr virus.

ALAN: Hey, that’s great!

GILDA: I have cancer.

ALAN: . . . Gilda?

GILDA: I have ovarian cancer, Zweibel, and I need you to help me get through this part of my life.

ALAN: I will.

GILDA: You promise?

ALAN: I promise. What should I do first?

GILDA: Make me laugh. **********

ALAN: (Pg 189) (June 1, 1989) About 14 years ago, I was hiding behind a potted plant and this girl asked if I could help her be a parakeet, and I’ve been smitten with Gilda ever since. And now? Well, I haven’t mourned, and I haven’t even cried yet, because even though she’s dead, I just don’t want her to die. I don’t know why God makes people and then takes them back. Just like I don’t know if I’m supposed to celebrate the fact that Gilda was in my life or feel cheated that she’s not here anymore. But even though her body grew to betray her, spirits just don’t die. And that’s what Gilda was. Even as an adult, she was still a little girl who believed in fairy tales, and that if she said “Bunny Bunny” on the first of every month, it would bring her love, laughter and peace. Well Gilda, today is June 1st, and if you’re in a place where you can’t say it, I’ll say it for you.

TOGETHER: Bunny Bunny
```

---

## IC-0736: Cabbie from Calcutta

- Title: Cabbie from Calcutta
- Author (byline): Robert Mauro
- Work: Two-Character Plays for Student Actors
- Publisher: Meriwether Publishing Ltd
- Publication date as stated: March 1988
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: RAGGI, MRS. HARTFORD
- Teaser before the introduction: No
- Spoken words (computed): 1932
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Mauro
Book: Two-Character Plays for Student Actors
ISBN: 0916260534
Publisher: Meriwether Publishing Ltd
Date (Month/Year): March 1988
```

### Introduction (context only: never use it for content warnings)

```text
RAGGIE: Immigration: Noun: (with enthusiasm) the act of coming to a foreign country in order to settle there.

MRS. HARTFORD: Foreigner: Noun: One who is from a foreign country or place;

(scathingly) an outsider.

RAGGIE: Calcutta: the largest city in India; (sadly) suffers from poverty and overcrowding.

MRS. HARTFORD: Cabbie: Noun: an informal name for a (with distaste) taxi driver.

BOTH: “The Cabbie from Calcutta” by Robert Mauro
```

### Performance text (classify this)

```text
Four chairs facing audience form the front and rear seats of RAGGI's cab. RAGGI sits reading The WALL STREET JOURNAL as he waits for a fare.

RAGGI: Look at this. Once more Polaroid and IBM are up. This is up, that is up. Good, great America. The land of much wondrous opportunity. Raggi, the cabbie from Calcutta, will be a very, very rich man someday. I don't spend all my life driving this hick. . . or is it hack? Well, whatever it is, it's a necessity for Raggi now. True, it is also one big pain in the buttock, but then so was riding that blinkin' water buffalo back in Bombay. At least here you get paid. There all I got was bites by that infernal beast. (Paging through paper) And does Raggi see any water buffalo stock in this wondrous paper of the great American dream? No. Thank the great lord Rama. But Raggi sees much stock in many interesting things. Many. My heavens! Look at Sony. Sony is truly no baloney. (Just then MRS. HARTFORD enters.)

MRS. HARTFORD: (She walks up to RAGGl's cab and peeks in.) Cabbie? Yoo-hoo. Hello.

(Annoyed, she shouts) Cabbie!

RAGGI: (Jumps and puts down his paper quickly) Oh, yes, dear lady. That is my middle name.

MRS. HARTFORD: Cabbie is your middle name?

RAGGI: Well, actually my middle name, it is Gandhi, after the great one. But in America, dear lady, it is Cabbie. You can call me Fred, you can call me Red - but when you need a cabbie, please, dear lady, call me anytime cabbie.

MRS. HARTFORD: (In a hurry, bored) Yes, yes. How nice. (Shakes her head) Another alien. Good lord, the country is full of them.

RAGGI: You telling, Raggi. In India we have your basic Indian. But not in America. Here one person can never tell from where the other is coming or to where he or she is going. It's a very curious place America, but very great. I am proud to be an alien in this great, wondrous land of America. God bless the Grand Canyon and Bruce Springsteen, who I hear was born in the U.S.A.

MRS. HARTFORD: Yes, well some seem to think so. As for me, I'd just like to get this trip over with as soon as possible. Do you understand my meaning, cabbie?

RAGGI: Oh,yes. Very well, misses. Yes, dear lady. And where can Raggi take you?

MRS. HARTFORD: I'm on my way to Wall Street

RAGGI: Good golly! Ah! Yes! Oh, how wonderful. The great Wall Street. (Holds up paper) It is all here in black and write.

MRS. HARTFORD: That's black and white.

RAGGI: Oh, yes, to be sure. That, too. Is it not amazing how IBM and Polaroid are always up? (Holds up the paper)

MRS. HARTFORD: Oh, good heavens, not another one.

RAGGI: (As he starts up his cab, we hear sound of engine revving up.) Another what?

MRS. HARTFORD: Another dirt-poor alien overly impressed by our capitalistic system.

RAGGI: Oh. Well, one is truly amazed by such things when one's family and friends live on a very few rupees a year, and who must eat - but who have no money to buy food. Slow, fast, or microwaved. And, dear lady, as a result, you don't want to know what we poor folk must eat. It is not a pretty sight, I assure you.

MRS. HARTFORD: I'll bet.

RAGGI: This would be a good bet. Truly our daily bread, it is not what you call your microwave gourmet variety.

MRS. HARTFORD: Yes, yes. Well, so you've picked yourself up by the proverbial bootstraps and have come to America for our microwave TV dinners and our (Fans herself) non-air-conditioned taxi cabs? Is that it?

RAGGI: Oh, the air conditioner is on full bust, but it's as hot as buzzards out there. New York is worse than Calcutta in summer.

MRS. HARTFORD: I'll agree with you there. So you've come to America to make your fortune? Is that part of your great American dream? Besides the TV dinners.

RAGGI: That is, indeed, part of what you call it, my American dream. But there is also McDonald's and the Great Cornell.

MRS. HARTFORD: The Great Cornell? What Cornell is that?

RAGGI: Cornell Sanders.

MRS. HARTFORD: I should have guessed.

RAGGI: Finger lickin' good, you know. Yes, indeed. And in two very pleasant styles - regular and crispy. Truly remarkable. And one is also entitled to a creamy rich mashed potato treat and one amazingly good biscuit. Is this not truly amazing?

MRS. HARTFORD: If you're into fast food.

RAGGI: Oh, yes. In India there is only fast food.

MRS. HARTFORD: There is? Really?

RAGGI: Oh, truly. One must run very fast to catch it, or one has no fast food. Here the Cornell catches it for you.

MRS. HARTFORD: How interesting. Are we almost there? (She mumbles the next words.) I hope.

RAGGI: Look!

MRS. HARTFORD: (Braces herself in a panic, thinking she's about to be in a tremendous crash - we hear brakes screech and horns blow) WHAT?

RAGGI: Foot-long dogs sold right in the street!

MRS. HARTFORD: Foot-long dogs? Oh, you mean the Sabret stand there?

RAGGI: Yes, yes. They even have a truly wonderful umbrella for the monsoons. In India we have many monsoons, but no truly delicious foot-long sabret dogs with chili, mustard, relish, sauerkraut and such wonderful umbrellas.

MRS. HARTFORD: It's a darn shame.

RAGGI: Yes, yes. Did I tell you about my trip to see the lady?

MRS. HARTFORD: What lady is that?

RAGGI: The great lady. The statue.

MRS. HARTFORD: In the Metropolitan Museum of Art?

RAGGI: No, no. In the truly wonderful harbor of the great metropolis. The lady Liberty.

MRS. HARTFORD: Oh, that lady.

RAGGI: Yes, that lady. (Long pause, then) So aren't you going to ask me about my trip to see the lady?

MRS. HARTFORD: I wasn't planning to. But if you insist... So how was your trip to see the lady, cabbie?

RAGGI: I'm glad you asked. and please call me Raggi.

MRS. HARTFORD: Ragoo?

RAGGI: No. Raggeeee. (Spells it) R-A-G-G-I. The good old boys down at the garage, at the pepper mine

MRS. HARTFORD: Salt mine.

RAGGI: Huh?

MRS. HARTFORD: You mean salt mine. It's salt mine, not pepper mine.

RAGGI: It is?

MRS. HARTFORD: It is.

RAGGI: This English is a very big pain in the buttock.

MRS. HARTFORD: Butt.

RAGGI: But what?

MRS. HARTFORD: Butt. (Spells it) B-U-T-T. Butt. The idiom is not pain in the buttock, but rather pain in the butt. Another bit of America's gift to the free world.

RAGGI: So that's what it is . . .

MRS. HARTFORD: That's what what is?

RAGGI: An idiom. I know many of America's great idioms.

MRS. HARTFORD: I know many of America's great idiots.

RAGGI: You do?

MRS. HARTFORD: You're darn tootin'.

RAGGI: (Turns and points to her) Yes!

MRS. HARTFORD: (Bracing herself-as we hear brakes screech and horns blow.) Look where you're going! You're not driving an ox cart now!

RAGGI: (Looking at the road ahead, dodges a truck - loud screech of brakes and horns) Hit the dock!

MRS. HARTFORD: You mean hit the deck!

RAGGI: Deck, dock. Here one has a wondrous variety of possible obstacles to hit. In India the only thing you hit is a sacred cow or a water buffalo.

MRS. HARTFORD: Don't they have any cars?

RAGGI: Oh, yes. But in my little village outside of Calcutta we have no cars, no roads. We barely have any villagers. Fortunately we are very lucky to be in walking distance of the great city.

MRS. HARTFORD: Just a few blocks out of town, are you?

RAGGI: No, walking distance.

MRS. HARTFORD: That's what I meant. Walking distance. A few blocks.

RAGGI: Oh, no, dear lady. In India walking distance is any distance one can walk and not get trampled by a sacred cow or eaten by a man-eating tiger. I lived thirty-seven miles out of town.

MRS. HARTFORD: Good heavens! What do you do if you run out of milk in the middle of the night?

RAGGI: Yes, telling me about flit.

MRS. HARTFORD: Not flit, it. Tell me about it.

RAGGI: I'm telling you already. Hold your haunches. This could be a real boomer.

MRS. HARTFORD: I think you mean it could be a real bummer.

RAGGI: Truly.

MRS. HARTFORD: Very dangerous walking in the India jungle at night for a container of milk, huh?

RAGGI: No. Very dangerous milking a sleeping water buffalo.

MRS. HARTFORD: You're serious.

RAGGI: I'm joking, dear lady. But we manage.

MRS. HARTFORD: I guess. But to be perfectly honest, I am not at all happy by all you foreigners coming to my country to rip us off.

RAGGI: Raggi rips no one. I keep this cab clean, and not even one lady has ever torn or ripped her famous, fabulous Leggs or silky soft, sheer

MRS. HARTFORD: That's not what I mean! I was not talking about pantyhose!

RAGGI: You said Raggi rip off people.

MRS. HARTFORD: I meant cheat them! As in take their money unfairly and illegally! Cheat!

RAGGI: (A bit annoyed) Cheat? Raggi never cheat a single person. I am an honest man! My father was an honest man and his father before him. We are good people. We are not cheats.

MRS. HARTFORD: Then you're not much of an American. Here it's dog eat dog.

RAGGI: In India it's man eat dog, occasionally lizard. Now that is very fast food.

MRS. HARTFORD: I think I'm going to be sick. :

RAGGI: If you have to eat dog, you'd be very sick. :

MRS. HARTFORD: Stop talking about food!

RAGGI: OK. What do you want me to talk about? Perhaps the future of pork belly options on Wall Street? Maybe margin buying and selling? Securities and Muni Bonds are good. Or, perhaps, we can rap right on about. . . my favorite. .. insider trading scandals. Very shifty, you Americans. You do that in Calcutta, they cut off more than your credit.

MRS. HARTFORD: Look, Rummie or Ronnie, or whatever your name is, just get me to Wall Street. OK?

RAGGI: It's Raggi. With two g's.

MRS. HARTFORD: Just get me to Wall Street!

RAGGI: In a gypsy!

MRS. HARTFORD: What? This is a gypsy cab?

RAGGI: No. A fast cab. You know: in a gypsy. Pronto.

MRS. HARTFORD: Good gracious! You mean in a jiffy, not gypsy.

RAGGI: Oh. I see. A jiffy. Like peanut butter? Is Jiffy peanut butter fast food?

MRS. HARTFORD: I have no idea.

RAGGI: It sounds like a fast food.

MRS. HARTFORD: You're kidding, of course. Tell me you're kidding.

RAGGI: Of course.

MRS. HARTFORD: Another bit of Indian humor?

RAGGI: Another bit of Raggi's humor.

MRS. HARTFORD: So Raggi, how does an immigrant from Calcutta make his fortune in the Big Apple?

RAGGI: One works his B-U-T-T off. It is no picnic this Big Apple.

MRS. HARTFORD: I'm sure. Do you plan the cabbie business as your life's work?

RAGGI: No, no. I am enrolled at Columbia University. I am some day becoming a system analyst.

MRS. HARTFORD: YOU... you mean you're a computer programmer?

RAGGI: You bet! Yes. I am very well knowing of Cobol, Fortran, APL and Focus. I'm even good at Space Invaders.

MRS. HARTFORD: I didn't even think they had computers in India - let alone video games.

RAGGI: Of course we do. And here, too. I'm not going to be driving this hick

MRS. HARTFORD: Hick?

RAGGI: This cab.

MRS. HARTFORD: You mean hack-H-A-C-K.

RAGGI: I knew it. Hack. Anyhow, someday I'll be working on Wall Street in the electronic data processing section of Whitney, Wainwright, Wagner and Hartford.

MRS. HARTFORD: My ex-husband's company?

RAGGI: (Ironic) No?

MRS. HARTFORD: YES!

RAGGI: Imagine that. Only in America. Small world, huh?

MRS. HARTFORD: Too small.

RAGGI: They say it's a global village. Soon we'll all be one. ,

MRS. HARTFORD: How thrilling.

RAGGI: Yes. Soon I'll be raking in the big shmucks.

MRS. HARTFORD: I think you mean big bucks.

RAGGI: Yes, that, too.

MRS. HARTFORD: You couldn't do that in India?

RAGGI: In India a person of my cast can do only two things.

MRS. HARTFORD: And what are they?

RAGGI: Milk the water buffalo and feed the water buffalo. It is a very limited job market with no IRA fund, no major medical and absolutely no dental plan.

MRS. HARTFORD: Good heavens! What if you should get kicked by a water buffalo? What do you do?

RAGGI: You kick him back.

MRS. HARTFORD: In America if you get kicked by a water buffalo, you sue the owner and buy a condo in Beverly Hills on the settlement.

RAGGI: Is this not truly the land of opportunity?

MRS. HARTFORD: Truly.

RAGGI: God bless America.

MRS. HARTFORD: Yes. I, too, love America. In my own way.

RAGGI: Well, here we are, dear lady.

MRS. HARTFORD: (Getting out, hands RAGGI money and a quarter tip) My fare, and here's a quarter tip for you.

RAGGI: Truly God bless America. A whole two butts!

MRS. HARTFORD: That's two bits.

RAGGI: Right, no butt's about it.

MRS. HARTFORD: You mean you're not offended by such a small tip?

RAGGI: Small? Listen, this is better than what you get for driving a rajah on an elephant to Delhi.

MRS. HARTFORD: You're all right, Rags old boy. (She exits.)

RAGGI: (Puts the quarter in his pocket, then opens the paper.) Now let's see how many penny stocks I can buy for a quarter. Good golly. That last penny stock I bought took a real flying leap. Bought this cab company on that one. (Curtain falls as RAGGI laughs and reads the WALL STREET JOURNAL.)
```

---

## IC-0737: Careless Love

- Title: Careless Love
- Author (byline): John Olive
- Work: Not specified
- Publisher: Samuel French, Inc
- Publication date as stated: 1988
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JACK, MARTHA
- Teaser before the introduction: No
- Spoken words (computed): 765
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Olive
ISBN: 978-0573690693
Publisher: Samuel French, Inc
Date (Month/Year): 1988
AWARD RECORDS
2002 National Qualifier
2006 National Qualifier
IL State Qualifier
```

### Introduction (context only: never use it for content warnings)

```text
Actor #1 (F): Abortion is one of the most divisive issues in modern US history, perhaps even more so than homosexuality. The sharp divisions cut through politics, religion and even families themselves.

Actor #2 (M): Mother Teresa once said: It is a poverty to decide that a child must die so that you may live as you wish. The choice to abort, however, is never an easy one. The mother must deal with feelings of guilt. The choice will burden her conscience in life; it will burden her soul in death.

Actor #1 (F): The mother? The mother? Why is the father exempt from responsibility in the decision? Listen closely as Martha and Jack attempt to resolve this issue in

Actor #2 (M): Careless Love by John Olive
```

### Performance text (classify this)

```text
JACK: (slightly startled) Oh, hi. I thought you weren't coming.

MARTHA: Birthday party started drinking champagne, and, well, you know...

JACK: Champagne drinkers.

MARTHA: Yeah.

JACK: Animals. (short beat) Well, I'm glad you came. Sit down.

MARTHA: Well, okay. (SHE sits, and takes the script, opens it.) This the new play?

JACK: Yeah.

MARTHA: "Little Criminals." (pages through the script) Which are you?

JACK: Andrew.

MARTHA: (reads) "Gone to seed attorney. Less intelligent than he thinks. Drinks." (starts paging through the script)

JACK: (watches her for a short moment) The first act is very weak. I’m not in it. (pauses) Page forty eight. (MARTHA reads.) I could recite it.

MARTHA: No.

JACK: Want a beer? (reads from a card on the table) Molson, Moosehead, Dab, Harp, Guiness, Bass, Dos Equis, Carta Blanca and please stop me,

MARTHA: No, thanks, Jack, I don't want any beer.

JACK: Okay. (reads again) Inglenook, Blue Nun, Gallo. Marty.

MARTHA: Nothing.

JACK: Perrier? Virgin Mary? Coke?

MARTHA: Nothing.

(Beat. MARTHA continues to read. JACK gently takes the script from her hands, and sets it aside. MARTHA looks away; suddenly, looks lonely, upset.)

JACK: Are you okay, Marty?

MARTHA: I'm fine.

JACK: Are you...sick at all? In the mornings or something?

MARTHA: Little bit. Mainly, I'm tired.

JACK: Do you feel like there's really something...I don't know, weird, going on with your body? Something basic?

MARTHA: I'm pregnant.

JACK: Oh, okay, right. (takes a pull of his beer) How 'bout those Cubbies? (beat) Marty. I'm sorry about the other day, if I behaved badly.

MARTHA: When?

JACK: The other day. At the theater. You remember the little scene at the theater?

MARTHA: Scene?

JACK: Well, whatever you want to call it, it was a scene. The folks at rehearsal were all moved.

MARTHA: You're a very good actor.

JACK: (stares at her, shocked, then laughs) Look, this is hard. I mean, normally this is something that happens between people who know each other pretty well.

MARTHA: I'm sorry this is hard for you.

JACK: Do you really hate me?

MARTHA: Not at all. You were a very good lover.

JACK: (after a slight pause) Okay. Do you need some money?

MARTHA: Money?

JACK: For...an abortion? All I wanna do is whatever's the right thing. (quick beat) You know Stuart, the guy I was talking to at rehearsal when you came in? After you...left, he said, "Well, Jack, are you going to do the right thing by that girl?" And I said, "Marry her?” He looks at me, big dramatic pause, and says, "Pay for her abortion!” (pause) Well, anyway, do you need some money? I...got my checkbook.

MARTHA: (not looking at JACK) I made an appointment today, at Planned Parenthood.

JACK: Oh? They have abortions there? It's not just...pills and rubbers?

MARTHA: They have referrals to abortionists. They send you someplace else, to get the abortion. All they do is, they advise you.

JACK: (after a slight pause) When's the-?

MARTHA: (overlapping JACK) And if you need- (stops)

JACK: Go ahead.

MARTHA: And if you need money or something, they can advise you about that.

JACK: Well, I can pay for... I can help you pay for the --

MARTHA: It happens really fast. They stretch your vagina open, with a...thing. Then there's this long needle, they showed me one, they use it to inject Novacaine into your cervix. That part hurts. Then they stretch your cervix open, and then they.. .suck the baby out, with a vacuum. Then they scrape the rest of it out, then they suck it all clean, and that's it. Easy. (pauses) Then you have a lot of emotional problems afterwards, lots of...anxiety, because of all the... Well, I guess you lose a lot of hormones.

JACK: Do you want me to go down there with you? (MARTHA laughs, abruptly and rather shrilly.) What's so funny?

MARTHA: That's not what you're supposed to say!

JACK: Tell me what I'm supposed to say! Tell me what to do! This is hard! You feel like a total stranger to me, and you wouldn't believe the load of Irish Catholic guilt I'm carrying about this.

MARTHA: You get guilty, I get pregnant.

JACK: (Now JACK bursts out laughing. Then an abrupt beat: He covers his face with his hands, weeping. Finally:) Well, @#$% you. You have as much responsibility in this as I do.

MARTHA: I don't expect anything from you. If all you want is for this to be over, then okay, it's over. I won't bother you any more. The guilt is your problem, I'm sure you can take care of that alone, I’m sure you've had lots of practice.

JACK: (staring at her) Jesus Christ.

MARTHA: I only told you because I thought you had a right to know.

JACK: As the father.

MARTHA: Yes.

JACK: You know, Marty, I was given to understand that your sex life was pretty varied and active, as they say.

MARTHA: Who gave you to understand that?

JACK: Persons who would, at this point, I'm sure, prefer to remain anonymous.

MARTHA: Well, they were wrong! You're the first person I've made love with since I left school.

JACK: Since...?

MARTHA: Almost three years.

JACK: That's great! Luck'o the Irish, eh? Your first time out in three years and you get zapped!

MARTHA: I'm not Irish.

JACK: But I am! (stands abruptly) Well, you're not getting @#$% from me, the price of an abortion, and that's it. (brandishes his script) I got work to do! Gotta go fake my way through another piece of @#$% play, the ole crazed Celtic charm strikes again. I should thank you, I'll be able to use all this in Act Three! (starts to exit, then turns, in a fake-theatrical voice) Good-bye, darling!
```

---

## IC-0738: Charlotte’s Web

- Title: Charlotte’s Web
- Author (byline): E.B. White
- Work: Not specified
- Publisher: HarperCollins
- Publication date as stated: April 2012
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TOGETHER, FERN, MR. ARABLE, CHARLOTTE, MR. ZUCKERMAN, NARRATOR 1, WILBUR, GOOSE, LAMB, TEMPLETON, SHEEP, MRS. ARABLE, NARRATOR 2, GANDER, LOUDSPEAKER, FAIR OFFICIAL
- Teaser before the introduction: Yes
- Spoken words (computed): 1329
- Already set (do not supply): none

### Source block (context only)

```text
Author: E.B. White
ISBN: 978-0061232916
Publisher: HarperCollins
Date (Month/Year): April 2012
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Charlotte’s Web by E.B White is one of the all-time great classics of children's literature.

ACTRESS: It’s gentle story with its kindly wisdom about friendship and love has survived and prospered for decades.

ACTOR: Why? Because its themes are universal and timeless:

ACTRESS: Growing up,

ACTOR: Death . . .

ACTRESS: And most importantly the power of friendship.

ACTOR: In the words of E.B. White, “Friendship is one of the most satisfying things in the world.”

TOGETHER: Charlotte’s Web by E.B. White
```

### Performance text (classify this)

```text
Suggested Roles:

Actor: Mr. Arable, Mr. Zuckerman, Narrator 1, Charlotte, Goose/Gander, Lamb, Templeton

(the rat), Sheep, Fly, Mrs. Arable, Loudspeaker, Fair Official

Actress: Fern, Wilbur, Charlotte Narrator 2

NOTE: The role of Charlotte should be some combination of the 2 performers in both lines and physicality

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

TOGETHER: (Pg 164) After all, what’s a life, anyway? We’re born, we live a little while, we die. *****

FERN: (Pg 2-4) Please don’t kill it! It’s unfair!

MR. ARABLE: (Holding a very small pig) Fern, you will have to learn to control yourself.

FERN: (Yelling) Control myself? This is a matter of life and death, and you talk about controlling myself.

MR. ARABLE: I know more about raising pigs than you do. A weakling makes trouble.

FERN: The pig couldn’t help being born small, could it? If I had been very small at birth, would you have killed me?

MR. ARABLE: This is different.

FERN: I see no difference. This is the most terrible case of injustice I ever heard of.

MR. ARABLE: (reconsidering) All right, he’s yours. (Hands the pig over to Fern) Start it on a bottle, like a baby. You’ll see what trouble a pig can be. (Strides off)

FERN: (Petting the little pig) He’s absolutely perfect! (thinking) (Pg 7) Wilbur . . . it’s name is Wilbur!

*****

CHARLOTTE: (Enters via her web) Salutations! (Pg 101) (She spins some web, obviously writing something)

MR. ZUCKERMAN: (Pg 115) (looks in awe as the spiderweb) That pig is radiant! *****

TOGETHER: (Pg 164) After all, what’s a life, anyway?

MR. ARABLE: (Pg 12) He’s got to go, Fern. (attempts to lift Wilbur and cannot) You have had your fun, but Wilbur is not a baby any longer. (he drops him with a thump) Tell your Uncle Homer you’ve got a pig you’ll sell and see what he says.

NARRATOR 1: The next day Wilbur was taken from his home and went to live in a manure pile in the cellar of Zuckerman’s barn.

WILBUR: (Pg 16) (wandering outside; lonely and bored – he oinks) There’s never anything to do around here. (Pg 28-29) (to the goose) Will you play with me?

GOOSE: (clucking and speaking rapidly and repetitively) Sorry, sonny, sorry. I’m sitting on my eggs.

WILBUR: (to the lamb) Will you please play with me?

LAMB: (Baa’s disdainfully) Certainly not. I don’t play with pigs! Go play by yourself!

WILBUR: (to Templeton, the rat) Will you play with me, Templeton?

TEMPLETON: Play? I hardly know the meaning of the word.

WILBUR: Well, it means to have fun, to frolic, to run and skip and make merry. (he demonstrates)

TEMPLETON: I never do those things! I prefer to spend my time eating, spying and hiding.

WILBUR: (Heavy sigh and dejected oinking) (Pg 16) I’m less than two months old and I’m tired of living. (he sobs in an oinking manner)

CHARLOTTE: (Pg 31) Do you want a friend, Wilbur? I’ll be a friend to you. I’ve watched you all day and I like you!

WILBUR: (sobbing subsides) But I can’t see you. Where are you? And who are you?

CHARLOTTE: I’m right up here. (she descends, spinning her web) (Pg 35) Salutations!

WILBUR: Salu-what?

CHARLOTTE: Salutations! It’s my fancy way of saying hello! (Pg 36-39) Look up here in the corner of the doorway! I’m waving! (she waves) See me now?

WILBUR: Salutations! May I have your name?

CHARLOTTE: My name? My name is Charlotte.

WILBUR: I think you’re beautiful.

CHARLOTTE: Well, I am pretty. There’s no denying that. All spiders are rather nice-looking.

(she notices a fly trapped in her web) Watch me wrap up this fly! (Fly beats its wings furiously, buzzing) First, I dive at him. (She plunges on a silken thread) Next, I wrap him up (She does so and the buzzing becomes muffled) Now I knock him out, so he’ll be more comfortable. (She bites the fly) He’ll make a perfect breakfast for me.

WILBUR: (gasping) You mean you eat flies! . . . Do they taste good?

CHARLOTTE: Delicious. I don’t really eat them. I drink them. Drink their blood. I love blood!

SHEEP: (Pg 49-51) (entering) Hello! Seems to me you’re putting on weight. You know why they’re fattening you up, don’t you?

WILBUR: No

SHEEP: Well, I don’t like to spread baaaaad news, but they’re going to kill you.

WILBUR: They’re going to what?

SHEEP: Kill you. Turn you into smoked bacon. All young pigs get murdered by the farmer as soon as the cold weather sets in. Christmastime . . . pig . . . ham . . . Kill you!

WILBUR: (squealing and crying) I don’t want to be killed. I don’t want to die! Is it true, Charlotte? Are they going to kill me when the cold weather comes?

CHARLOTTE: Well, the old sheep has been around this barn a long time. If she says they plan to kill you, I’m sure it’s true. (Wilbur wails) Stop your crying! I can’t stand hysterics. You shall not die.

WILBUR: What? Really? Who’s going to save me?

CHARLOTTE: I am!

WILBUR: (suspicious) [But] how?

CHARLOTTE: That remains to be seen. (Pg 63) (Deep in thought) I’m working on it! ******

FERN: (Pg 105) Charlotte is the best storyteller I ever heard

MRS. ARABLE: Fern, you know spiders don’t tell stories. Spiders can’t talk.

FERN: Charlotte can. She doesn’t talk very loud, but she talks!

MRS. ARABLE: (Pg 106-107) Fern, I wish you would play outdoors instead of going to Uncle Home’s barn. You’re spending too much time in that barn. It isn’t good for you to be alone so much.

FERN: Alone? My best friends are in the barn cellar! (Pg 71) I’m going to visit Wilbur! ******

CHARLOTTE: (Pg 75-76) (moodily thinking, then she comes up with an idea. She descends to the center of her web and begins to cut some of her lines. She starts weaving a message, snipping lines and repositioning others . . . as she works to create her masterpiece she hums or sings) (Pg 94) Up we go! Attach! Descend! Whoa! Good! Now right and down and swing that loop around and around! Now in to the left! Attach! Climb! Repeat! O.K.! Good girl!

(When she is finished she celebrates and then exhausted, sleeps) ******

MR. ZUCKERMAN: (Pg 78-80) (He and Fern are bringing food for the animals, he notices the web and stops dead in his tracks. He sets down his pail and rums his eyes – Fern stands in awe, unable to speak) I’m seeing things! Some Pig! (stares for a long time at Wilbur then drops to his knees in awe) We have received a sign– a mysterious sign. A miracle has happened on this farm! We have no ordinary pig! SOME PIG!

NARRATOR 2: (Pg 84) The news of the wonderful pig spread clear up to the hills and farmers came down in buggies to stand at Wilbur’s pen, admiring the miraculous animal. They had never seen such a pig in their lives!

MR. ZUCKERMAN: (Pg 96) Lurvy! Phone the reporter on the Weekly Chronical and tell him what has happened. He may want to bring a photographer . . . There is to be no more cow manure thrown down into that pigpen. I want that pig to have clean, bright straw every day! Start building a crate for Wilbur. I have decided to take [him] to the County Fair! Zuckerman’s Famous Pig! *****

CHARLOTTE: (Pg 86-87) (calls a meeting of all the animals) I shall begin by calling the roll. Wilbur?

WILBUR: Here!

CHARLOTTE: Gander

GANDER: Here, here, here!

CHARLOTTE: Why do you have to repeat everything?

GANDER: It’s my idio-idio-idosyncrasy!

CHARLOTTE: Sheep?

SHEEP: He-aa-aa!

CHARLOTTE: Templeton? (no answer) Templeton? (no answer) Well, I guess we can proceed without the rat. (With great fanfare) The message I wrote in my web, praising Wilbur has been received. The Zuckermans and everybody else has fallen for it. Zuckerman thinks Wilbur is an unusual pig and therefore he won’t want to kill him and eat him. My trick will work and Wilbur’s life can be saved.

WILBUR: Hurray! *****

WILBUR: (Pg 115-116) You’re going with me, aren’t you, Charlotte? I need you, Charlotte. You’ve just got to come!

CHARLOTTE: No, I believe I’d better stay home and get some egg laying done.

WILBUR: (amazed) I didn’t know you could lay eggs. Why don’t you come with me to the Fair Grounds and lay your eggs there?

CHARLOTTE: (Pg 122) [Then] I shall go, too. We can’t tell what may happen at the Fair Grounds. Somebody’s got to go along who know how to write. Pg 127 (the geese cheer) ****** at the fair ******

LOUDSPEAKER: (Pg 130) Attention, please! Will the owner of a Pontiac license number H-2439 please move your car away from the fireworks shed!

WILBUR: (Pg 134-135) (Charlotte climbs to the rafters at the fair) What do you see?

CHARLOTTE: There’s a pig in the next pen and he’s enormous! Much bigger than you are.

WILBUR: (whimpers as tears come to his eyes)

CHARLOTTE: He’s not anywhere near as clean as you are, nor as pleasant. He’s going to be a hard pig to beat, though, Wilbur, on account of his size and weight. But with me helping you, it can be done!

WILBUR: When are you going to spin a web?

CHARLOTTE: I shall be writing tonight for the last time. (She starts weaving a message, snipping lines and repositioning others . . . as she works to create a new word, she hums or sings) (Pg 141) Humble!

WILBUR: (Pg 142) (humbly) Charlotte, do you really thing Zuckerman will not keel me when the cold weather comes? Do you really think so?

CHARLOTTE: (exhausted) Of course. Tomorrow you will probably win a prize. The whole world will hear about you. You have nothing to fear, Wilbur. *****

FAIR OFFICIAL: (Pg 158) Ladeez and gentlemen! On behalf of the Fair, I have the honor of awarding a special prize of 25 dollars and a handsome bronze medal to this pig. This radiant, this terrific, this humble pig. (Pg 160) (he places the medal around Wilbur’s neck. Wilber snorts and grins) *****

WILBUR: (Pg 163-164) (after everyone had gone) Charlotte! Charlotte! (he’s taken aback by the silence) Do you feel alright?

CHARLOTTE: A little tired, perhaps. But peaceful . . . Nothing can harm you now.

WILBUR: (with tears in his eyes) Oh, Charlotte. Why did you do all this for me? I don’t deserve it. I’ve never done anything for you.

CHARLOTTE: You have been my friend, Wilbur . . . this lovely world, these precious days. After all, what’s a life anyway? We’re born, we live a little while, we die.

WILBUR: (Pg 165) Charlotte, what are you talking about?

CHARLOTTE: I’m done for. In a day or two I’ll be dead.

WILBUR: (Pg 164) Well, I’m no good at making speeches. I haven’t got your gift for words. (sadly) But you have saved me, Charlotte, and I would gladly give my life for you – I really would.

CHARLOTTE: (Pg 165) I’m sure you would. And I thank you . . . (Pg 171) (whispers) Good-bye

(Charlotte dies)

WILBUR: Charlotte? (no response; Wilbur oinks sadly) ******

NARRATOR 2: (Pg 184) It’s not often that someone comes along who is a true friend and a good writer. Charlotte was both.
```

---

## IC-0739: Check, Please

- Title: Check, Please
- Author (byline): Jonathan Rand
- Work: Laugh Lines: Short Comic Plays, Pg 301-334
- Publisher: Vintage
- Publication date as stated: April 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GUY, MELANIE, TOGETHER, ACTOR, ACTRESS, MIMI, LINDA
- Teaser before the introduction: Yes
- Spoken words (computed): 956
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jonathan Rand
Book: Laugh Lines: Short Comic Plays, Pg 301-334
ISBN: 978-0307277138
Publisher: Vintage
Date (Month/Year): April 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Let’s face it . . .The dating landscape is a minefield.

ACTRESS: You have that right . . . and let’s not even talk about blind dates!

ACTOR: The concept of a blind date to me, even in its simplest most casual form just has “disaster” written all over it.
```

### Performance text (classify this)

```text
NOTE: This cutting asks the female student to portray multiple characters, (ie a different character for each “scene” - which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments. NOTE: The original script was written for two actors to play all roles.

GUY: (Pg 301-334) Hi. It's so great to finally meet you.

MELANIE: (MELANIE is truly sweet and adorable when she's focused on the date.) Hi. Same here!

GUY: SO ... What do you-

MELANIE: Wait, before you ... sorry. (Meekly.) This is so rude, but the Bears game is on right now? You don't mind if I check the score ...

GUY: Oh, sure. Totally.

TOGETHER: ARGHHH!

ACTOR: You say to yourself: But surely my loved ones and trusted acquaintances can help navigate this treacherous world and find me a suitable mate amongst their social networks.

ACTRESS: You are wrong. So, soooooo wrong

ACTOR: Some blind dates take it from bad to horrific.

ACTRESS: Let us show you . . .

ACTOR: Check, Please

ACTRESS: by Jonathan Rand

MELANIE: (As she pulls out her cell phone to check her web browser.) I know this is such an awful thing to do on a first date, but it's late in the fourth quarter, and it's do-or-die if we wanna make the playoffs.

GUY: It's no problem at all. Really.

MELANIE: Thanks. (As she checks.) I love the Bears. They're really strong this season. (Sees score; reacts a little.) Okay, I'm done. (Cheerily.) That wasn't so bad, was it?

GUY: What's the score?

MELANIE: Packers by seven. It's no big deal. It's just a game, right? So, c'mon, enough about football. Let's hear about "Mister Mystery." Harriet's told me tons about you.

GUY: Man ... The pressure's on now. (They laugh together genuinely. MELANIE laughs then fades directly into her next line, which is suddenly serious.)

MELANIE: I'm just gonna check on the game one more time. (She digs into her purse.) Is it all right with you if I put on this little earpiece thingy? It won't be distracting, I promise. (As she puts the earpiece in her ear.) I'm making the worst first impression, aren't I?

GUY: Not at all.

MELANIE: It's just because it's for the playoffs. I'm usually pretty normal. (Throws her hands up.) Ah! The line gives A-Train this huge running lane, but he fumbles after two yards. The ball rolled out of bounds, so we're cool, but come on-it's for the playoffs. You don't just drop the ball like that, you know? Now you're third and long, and the whole season is riding on one play. PASS THE BALL!!

GUY: What's wrong?

MELANIE: Miller! He doesn't pass it. It's third and long-who hands it off on third and long? Is he suddenly AFRAID OF HIS RECEIVERS?! (GUY looks around subtly at the other patrons.) Oh my God, I'm sorry. I'm being loud, aren't I. PASS THE BALL!! Jesus, people! This is FOOTBALL, not FREEZE TAG. It's FOURTH DOWN pass the FRIGGING BALL!

GUY: Listen, we could go to a bar or something if you want to watch the game on TV.

MELANIE: Oh please, no. I wouldn't do that to you. The game's basically over. (She takes a deep breath and is now very calm.) Okay. I'm done. I got a little carried away there, didn't I? Let's order. (They peruse for a moment, as if nothing has happened.)

(Downtrodden.) They lost ... (Starting to tear up.) They lost. (MELANIE breaks down. GUY takes out a handkerchief and offers it to MELANIE. She uses it to blow her nose.)

GUY: I'm so sorry. Can I do anything to help?

MELANIE: (Still weepy.) The Bears suck ...

GUY: Aww, no. They don't suck. They're probably just having a bad season- (MELANIE grabs his collar, pulls him extremely close, and speaks in a horrifying, monstrous, deep voice.)

MELANIE: THE BEARS SUCK.

GUY: Check, please. **********

(GUY is sitting across the table from a fully outfitted mime, MIMI, who throughout the scene is extremely over-the-top and exuberant. The scene begins with MIMI "leaning" on "something." Mimed actions in this scene will be indicated with brackets. A few moments pass as we get a feel for the ridiculousness of the scenario.)

GUY: So what do you do for a living? (Beat.)

MIMI: [Pulling something heavy with a rope.]

GUY: You pull rope. (Pause.) Look ... I respect your profession and all? I think it's noble what you do .... The world needs more people who ... climb invisible ladders and pull imaginary ropes. But I really don't see how it's appropriate to bring your work to a date.

MIMI: [Battling against harsh winds.]

GUY: Oh, yeah, quite a storm in here. Listen, I'm gonna go ahead and order.

(GUY opens his menu and reads. MIMI gets past the storm and mimes picking up an imaginary menu, proceeding to peruse, turning page after page. GUY looks up. There is silence as he watches MIMI do her thing.) Hey, I'm gonna go ... use the restroom. (GUY gets up, takes his jacket from the back of the chair.)

MIMI: [You're leaving? Driving away? Far? Bye-bye?]

GUY: No, I'm not leaving. I'm taking my jacket with me because ... it might get cold in the men's room.

MIMI: [Cold like me in this wild blizzard?]

GUY: Yeah, exactly like that. (GUY starts to leave. MIMI follows close behind, maybe as an airplane pilot or a bus driver.)

GUY: No, you stay here. You-

MIMI: [Let me feed some chickens. Awww, those chicks are adorable. I love petting these lovely animals.]

GUY: I don't know what that is .... Look, I have to- (An idea dawns on GUY. The following is an extremely loud and animated sequence of events-very frantic for MIMI; sarcastically frantic for GUY.) (Looking up.) Oh my God! A BOX!

MIMI: [Where? Where?]

GUY: A huge glass box, falling from the sky!

MIMI: [Oh no! Oh no! I can't see it! What in heaven's name will I do? Help me, Lord!]

GUY: Noooooooo! (GUY follows "the box" with his finger as it plops directly on the frantic MIMI, who is now very much "trapped.") Check, please. **********

LINDA: Hi. I've been looking forward to this for a while.

GUY: Me, too. Sorry about all the rescheduling.

LINDA: Pssh, whatever, it's cool. Oh, shoot. Hold on. I forgot to (She starts rummaging through her purse, and after a couple if seconds, starts removing objects: compact, lipstick, etc.)

GUY: What's up? What's wrong?

LINDA: Oh, it's this silly thing. I've got this pill I need to take or else I get all weird. (Back to her purse.) I know I brought them. They've gotta be-- You know, whatever. I'll be fine.

GUY: You sure? I could drive you to a pharmacy or something.

LINDA: Nah, it's no big deal. It's just a precautionary drug, you know? It won't kill me if I don't take it for one night. I just may be a little out of whack. You probably won't even be able to tell. Whatever. So-anyway . . . It's nice to finally meet you.

GUY: The feeling's mutual.

LINDA: (Suddenly sarcastic, morose, in a monotone voice.) Oh, yes. It's so wonderful to finally put a name with a face. How wonderfully fascinating.

GUY: Heh. Yeah. Seriously.

LINDA: (Giggly/bubbly.) Hee hee hee. You're funny. You're cute. (Gruff.) He's not cute. You just haven't been out in a while. (Snobby.) That is NOT TRUE. He is GOOD-LOOKING. (Bashful.) No ... No ... He's- (Sensual.) Oh, you are absolutely right. He is a hunk of man. (Jittery.) Shhhhhhhh ... You're embarrassing yourself ... (Gruff.) Quit freaking out, man. (Easily offended.) Wha? Wha? Why are you jumping all over me? (Little girl.) She started it! (Motherly.) Girls, please don't fight.

GUY: Excuse me. Are you gonna be okay?

LINDA: (Pissy, to GUY.) You stay out of this! (Reasonable.) Hey, leave him alone. You just met him. (Gruff.) Oh, he can take care of himself (Sarcastic.) Way to ruin a magical evening. (Sensual.) Mmmmm ... The evening's about to get a lot more magical. (Motherly.) You'd better behave yourself, young lady, or you're grounded.

GUY: (GUY notices a bottle under a napkin and shows it to LINDA.) Hey, are these the pills?

LINDA: (Cheery.) There they are! (Pissy.) Yeah, too little too late. (Sensual.) You are so sweet to find them! (Peppy.) Yeah! YEAH! (Sarcastic monotone.) Whoop-dee-doo. (LINDA swallows the pill.)

GUY: Is everything all right?

LINDA: (Mostly back to normal, but woozy.) Whoa. Uh. Okay. Okay. It's starting to kick in. In a couple of seconds, the medicine'll take effect and I'll settle into a single personality. But don't worry-like, ninety-nine times out of a hundred, it's one of the normal ones. (LINDA suddenly lets out a shriek, grabs some bread from the table, sniffs it voraciously, stuffs it in her mouth, and lumbers offstage. Pause.)

GUY: Check, please.

(Note: LINDA's personality switches should be fast. Each personality should be a different level-her voice and demeanor should be changing dramatically throughout.)
```

---

## IC-0740: Children of a Lesser God

- Title: Children of a Lesser God
- Author (byline): Mark Medoff
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NOTE 2, SARAH, JAMES, ACTRESS, SARAH AND JAMES, ACTOR
- Teaser before the introduction: Yes
- Spoken words (computed): 2250
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
ACTOR: Welcome to the world of Sarah Norman, now in her mid-twenties, who has been deaf from birth.

ACTRESS: In this selection, Children of a Lesser God by Mark Medoff, you’ll get to witness for yourself what happens when two worlds collide.

ACTOR: The world of sound

ACTRESS: and the world of silence

TOGETHER: Children of a Lesser God by Mark Medoff
```

### Performance text (classify this)

```text
NOTE: The actress in this selection should sign using ASL. The actor will interpret for the actress and should use spoken English and ASL where indicated. A good on-line resource for ASL is http://www.aslpro.com/cgi-bin/aslpro/aslpro.cgi A completely free online dictionary of over 7200 ASL Signs

NOTE 2: This teaser opening should be both signed using ASL and spoken English by the actress. For an example of the spoken word of the deaf, check out the video at this link: http://www.youtube.com/watch?v=uKKpjvPd6Xo The following ALS speech, translated into standard English would have SARAH speaking . . . “I have nothing; no hearing, no speech, no intelligence, no language. I have only you. I don’t need you. I have me alone. I don’t want anything. I don’t need what you want to give me. My language is just as good as yours”

SARAH: (Signing) Me have nothing. Me defy. Speech inept. Intelligence – tiny blockhead. English – blow away. Left one you (point to audience) Depend – no. Think myself enough. What do I want? Nothing. I don’t need what you want to give me. I have a language that’s just as good as yours!

JAMES: She went away from me. Or did I drive her away? I don’t know. If I did it was because . . . I seem to be having trouble stringing together a complete . . . I mean, a speech therapist shouldn’t be having difficulty with the language. Start in the beginning. In the beginning there was silence and out of that silence there could come only one thing: Speech. That’s right Human speech. TRANSITION

ACTRESS: They meet

JAMES: (Sarah enters) Well, Sarah. Could you look at me, please. Excuse me, if you don’t look at me, I can’t . . .

SARAH: You deaf?

JAMES: Am I deaf? No. Why? (She stares curiously at his mouth) I can’t help detecting a certain reluctance to communicate with me. Is that because you’re afraid you’ll be embarrassed by the sounds you make? (She stares at his mouth) Are you reading my lips? I don’t think you’re reading my lips. (Signing) Gee, that was quick of me. Okay . . .

SARAH: Faster. Move it. Fly. Speed.

JAMES: I didn’t understand that.

SARAH: (In slow signed English) If you do not sign faster, the hour will be over before you finish your opening speech.

JAMES: Oh, if! If. I. Do. Not. Sign. Fast. Er. The hour will be over before I finish my opening speech. (It takes him a moment to comprehend “If” – she’s doing it very slowly. As she goes on, her signing becomes faster, ending in a blur. James’ voice trailing behind. ) Are you doing this because I’m not deaf? I used to pretend to be deaf, if that counts . . . . (no response) Well – good—okay. Why don’t you come back and see me sometime and we’ll have the same fun again.

SARAH: You give up easier than most.

JAMES: I give up easier than most?

SARAH: That’s smart.

JAMES: Smart. Thank you TRANSITION

ACTRESS: Time passes and then . . . Dinner in an Italian restaurant

SARAH: Why are you trying to be different from the other hearing teachers?

JAMES: Why am I trying to be different from the other hearing teachers? Why did I have to bring you to an Italian restaurant to get you to talk to a hearing person?

SARAH: I don’t need what you want to give me. I have a language that’s just as good as yours!

JAMES: You don’t need what I want to give you. Your language is just as good as mine – among the deaf, Sarah. Wouldn’t you like to be able to function in the hearing world?

SARAH: No.

JAMES: No, I mean to be able to speak and lip read. (she makes a grotesque face of a deaf person speaking – spitting, mouth contorted) People who are born deaf look like that sometimes.

SARAH: Always.

JAMES: Always? Oh yes, I know: Very difficult to teach someone born deaf like you to speak and lip read, because you’ve never heard the sound of a human voice. But it can be done. (Sarah looks away. James gets her attention) I mean it. Al right, look you and I can start with lip reading, whudduya say? (Sarah turns away) TRANSITION

ACTRESS: Time again passes

JAMES: I haven’t seen you for days. You’ve been avoiding me. I even ate lunch in the cafeteria, thinking I’d see you.

SARAH: I’ve been eating in the kitchen so you wouldn’t see me.

JAMES: You’ve been eating in the kitchen so I wouldn’t see you. Well, I didn’t see you. You know, I hate to say this, but you’re the most mysterious, attractive, angry person I’ve ever met. (Sarah become conscious of another student who has moved in to feed the ducks too).

SARAH: Go! Get out of here!

JAMES: (Calling after the student) Wait. Oh, that’s all right, Lydia. Wait a . . . Come back . . . (She’s gone) That was a bit rough, wasn’t it?

SARAH: Should I treat her like she’s handicapped?

JAMES: You think the only alternative to treating someone like they’re handicapped is to treat them like that?

SARAH: Yes!

JAMES: You should give some seminars on interpersonal relationships.

SARAH: She’s going to become dependent on you.

JAMES: Would that be so terrible if she became dependent on me?

SARAH: She’ll fall in love with you.

JAMES: She’s gonna fall in love with me. You know, all students don’t automatically – Jesus Christ, that’s quite a little leap you made there; from helping someone to learn something to dependency because of it, to falling in love as a result of the dependency. That’s very nice, but it happens to be bullshit. You have a sign for b-u-l-l shit?

SARAH: Bullshit. (a bull’s horns with one hand; at the other end, a closed fist with the other hand; the closed fist springs open in James’ face) You’re trying to con everyone.

JAMES: Excuse me, I’m trying to what everybody.

SARAH: C-o-n everybody.

JAMES: C-o-n. No, not everybody – only you. Wait a second, I’m going to invent a little sign here. Deaf-bullshit (The same sign as above with one horn stuck in his ear).

SARAH: I have to go.

JAMES: You have to go? Fine, take your deaf-bullshit and go. (Sarah leaves) Oh, come on, Sarah! Sarah . . . . ! TRANSITION

ACTRESS: The next day in a school hallway

Sarah is pushing a maid’s cleaning cart and doing her assigned jobs

JAMES: Hello. I’m sorry to interrupt your work.

SARAH: What do you want now?

JAMES: What do I want now? Okay, I want to know if you think you can’t learn to speak, that you’re not capable?

SARAH: Not speech talk again.

JAMES: Yeah, speech talk again. You’re not retarded – you know that?

SARAH: Since I was twelve (begins to sweep the floor)

JAMES: Since you were twelve-right. But do you really believe it? Did not going home anymore after you were eighteen – did that have anything to do with your sister’s friends? The boys you were going out with? (She is silent) Let me help you, damn it!

SARAH: You don’t know what you’re talking about!

JAMES: All right, you tell it to me right so I will know what I’m talking about!

SARAH: You’re so . . .

JAMES: I’m so what? What am I? Nosy? Stupid? Misguided? Come on – whatever it is, I can take it. (She lets him have it)

SARAH and JAMES: (Signing as James speaks the lines) I have more than enough communication skills. You don’t. They never did.

JAMES: They? Who’s they?

SARAH AND JAMES: (James translates now in the first person) Hearing boys. They could never be bothered learning my language. No - that was too difficult. I was always expected to learn to speak. Well, I don’t speak! I don’t do things I can’t do well. The boys who did try to communicate with me got about as far as: How are you, I am fine. (Pause) At first I let them have me because they would. Sex was something I could do as well as hearing girls. Better! It got to be that when I went home, the boys would be lined up on a waiting list my sister kept for me. Most of them didn't even take me for a Coke first. No introductions. No conversations. We just went straight to a dark place. But I liked that communication. I loved it. It made me feel a lot better than this bullshit talk you make. (Finishes sweeping)

SARAH: That’s all you’re going to find out.

JAMES: No. that’s not all I’m going to find out.

SARAH: I live in a place you can’t enter. It’s out of reach. Deafness isn’t the opposite of hearing, as you think. It’s a silence full of sound.

JAMES: You live in a place I can’t enter. Out of reach? Deafness isn’t the opposite of hearing, as I think. It’s a silence full of sound. Really? A silence full of sound?

SARAH: The sound of spring breaking up through the death of winter.

JAMES: The sound of . . . what does that mean? (He doesn’t understand the juxtaposition of winter, earth, broken, growth – which is how she beings the line; yet he is moved by it – Suddenly there is a softness, a closeness between them)

SARAH: My secret. No hearing person has ever gotten in here to find out . . . No person, period.

JAMES: Your secret. No hearing person has ever gotten in there to find out . . . No person, period. (Sarah runs from him)

TRANSITION

ACTRESS: But Sarah does let James in to find out. In this next scene, James and Sarah have married

ACTOR: And after many struggles between the deaf and the hearing world, Sarah has decided to be a complainant in a legal action against the school where she and James met.

ACTRESS: Against James’ wishes, she plans to present a speech in front of the state commission to demand that deaf teachers be hired at the school and to end the discrimination against the deaf population.

JAMES: (Sarah is practicing her speech in sign language while James addresses the audience) Sarah Norman Leeds. My wife. Sarah Norman Leeds is deaf. She suffers a sensory-neutral deficit of unknown etiology. She has no residual hearing, derives no benefit from amplification. Sarah Norman Leeds’ deafness is not correctable by surgery. It is incurable . . . but Sarah has decided that no is ever going to speak for her again. What I’m a bit confused about is how we got here. We met, we fought, we fell in love, we got married, I was happy, I thought [she] was happy. But now we’re kicking each other’s teeth in. (To Sarah) Explain it to me.

SARAH: You think it’s my fault and that you’re perfect.

JAMES: I think it’s your fault and that I’m perfect. What a crock of . . . (reigning in anger) (long pause) When we go before the commission – do you want me to translate the speech exactly?

SARAH: Do you think you’re going to translate for me?

JAMES: Yes. I’ll tell you a little secret. They won’t understand it if I don’t translate it. . . . Look, if you’re really going to go through with this, I’d like to share the experience with you.

SARAH: I can’t say what I feel about being deaf through a hearing person.

JAMES: You can’t say what you feel about being deaf through . . . . through a hearing person.

SARAH: Does that make you angry?

JAMES: Angry . . . . and hurt. Let me see the speech, okay? Show me.

SARAH AND JAMES: (Sarah steps forward and James back so we see Sarah, but hear James’ voice) For all my life I have been the creation of other people. The first thing I was ever able to understand was that everyone was supposed to hear but I couldn't and that was bad. Then they told me everyone was supposed to be smart but I was dumb. Then they said, oh no, I wasn't permanently dumb, only temporarily, but to be smart I had to become an imitation of the people who had from birth everything a person has to have to be good: ears that hear, mouth that speaks, eyes that read, brain that understands. Well, my brain understands a lot, and my eyes are my ears; and my hands are my voice; and my language, my speech, my ability to communicate is as great as yours. Greater, maybe, because I can communicate to you in one image an idea more complex than you can speak to each other in fifty words. For example, the sign "to connect," is a simple sign--but it means so much more when it is moved between us like this. Now it means to be joined in a shared relationship, to be individual yet as one. A whole concept just like that. Well, I want to be joined to other people, but for all my life people have spoken for me. She says; she means; she wants. As if there were no I. As if there were no one in here who could understand. (When you say in here, motion to your chest or head). Until you let me be an individual, an I, just as you are, you will never truly be able to come inside my silence and know me. And until you can do that, I will never let myself know you. Until that time, we cannot be joined. We cannot share a relationship.

(Silence---Long pause).

JAMES: (re-enters scene with building anger) Well, you . . . That’s all very . . . That’s moving – it is, but . . . .You . . . . yyou think they’e really . . . that we’re really going to – we insensitive and inarticulate hearing people – that we’re really going to be able to – that one out of a million is going to care enough to even try to come inside your silence, to bend to you . . . .

SARAH: Didn’t you listen to anything I just said?

JAMES: Yes I did. I heard every word you just said and I’m going to tell you something you’re not gonna like.

SARAH: Give it to me!

JAMES: I think your real bitch is that you are deaf and you wish you could hear. I don’t think you think being deaf is so goddamn wonderful.

SARAH: Because of people like you.

JAMES: No! Not because of people like me. The administrators in ninety percent of the schools in the country would never hire you. You’re dreaming a dream that can’t come true. You’re going nowhere, you’re achieving nothing, you’re changing nothing until you change.

SARAH: Until I speak!

JAMES: Until you speak – Okay, you wanna play that one – fine with me. Goddamn right! You want to be independent of me, you want people not to pity you, then you learn to read my lips and you learn to use that little mouth of yours for something besides eating. Come on! Read my lips! What am I saying? Say what I’m saying! What. Am. I. Saying? (Sarah starts to sign something but he cuts her off. The rest of this speech is unsigned) Shut up! You want to talk to me, then you learn my language! You will always be dependent on someone until you learn to speak. Now I want you to speak to me. Let me hear it. Speak! Speak! Speak!

SARAH: (erupts like a volcano in speech - She doesn’t sign) Speech! Speech! Is that it? No! You want me to be your child. You want me to be like you. How do you like my voice? AM I beautiful? Am I what you want me to be? What about me? What I want? What I want? (Silence. James reaches to touch her but she bolts away. Returns to signing softly but also speaks as she signs): The following ALS speech, translated into standard English would have SARAH speaking . . . “I have nothing; no hearing, no speech, no intelligence, no language. I have only you. I don’t need you. I have me alone. Joined . . . unjoined”

SARAH: (Signing) Me have nothing. Me defy. Speech inept. Intelligence – tiny blockhead. English – blow away. Left one you Depend – no. Think myself enough. Join. Unjoined. (Sarah exits)

JAMES: (silence . . . . drops head in defeat)
```

---

## IC-0741: Church and State

- Title: Church and State
- Author (byline): Jason Odell Williams
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: 2017
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: COMMERCIAL VOICE, ALEX, CHARLIE, SARA, MARSHALL, SARAH, VOICE OVER, FROM THE CROWD, REPORTER 2, REPORTER
- Teaser before the introduction: Yes
- Spoken words (computed): 1900
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jason Odell Williams
ISBN: 978-0822237624
Publisher: Dramatists Play Service
Date (Month/Year): 2017
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: In politics, image is everything. Faith is currency. And silence can be just as loud as belief.

ACTRESS: Meet Charlie Whitmore, a U.S. Senator who has spent his life saying the right words,

ACTOR: Praising the right values and defending the right laws.

ACTRESS: But when a tragedy strikes close to home and shatters the talking points he’s stood behind for years, he begins to question:

ACTOR: What is the cost of belief when it’s used only as armor?

ACTRESS: What is the cost of power when it refuses to change?

ACTOR: And what happens when one man dares to speak his heart to a system that survives on applause instead of truth.

TOGETHER: Church and State by Jason Odell Williams
```

### Performance text (classify this)

```text
Suggested Roles: ACTOR: Charlie, Reporter ACTRESS: All Other Roles

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

CHARLIE (VO): (Pg 9) (on TV) I'm Charles Whitmore and I approve this message. (Lights rise as the campaign commercial continues)

COMMERCIAL VOICE: He's been hailed as "a compassionate conservative," and "just the kind of leadership from 'The Right' that Washington needs." As senator, he championed the biggest welfare reform bill in our nation's history, voted to extend benefits for seniors and veterans, and protected our Second Amendment Rights by helping to block a restrictive ban on firearms. (After a beat, Charlie enters quietly a little unsure of himself) He's a family man who believes in good Christian values. The kind of values on which this country was founded. This Tuesday, help continue the grand tradition of Whitmores in North Carolina politics, and re-elect Senator Charles Whitmore. (Charlie watches his commercial, mouthing along with the final catchphrase "the right leadership for a bold state" looking pleased and dissatisfied at the same time) The right leadership for a bold state.

Alex darts by the door, phone to her ear, spots Charlie and enters.

ALEX: (Pg 10-11) (into phone) Never mind, I found him. Tell Security to stand down. (hangs up) Senator, what are you doing in here? You’re due on stage in 15 minutes. (He shuts off the TV. Paces, nervous) You have no reason to be nervous, sir. It’s the same speech you gave last week.

CHARLIE: Oh, I’m not nervous – I could do this speech without any teleprompters, one arm behind my back.

ALEX: Security said you were mumbling to yourself . . . acting strange, then just disappeared without a word. We circled the building five times looking for you.

CHARLIE: (Pg 12) Well, it's no big deal really, I was just - after this morning, at the thing there, it got me thinking again -- about the events of last week. . .

SARA: (rushes in, all in one breath) There you are baby we’ve been looking all over for you.

CHARLIE: . . . and it just occurred to me that maybe I shouldn’t deliver the speech as written, ya know. Word for word. But speak from the heart. About everything that’s happened. And u . . . Yeah. That. (beat)

ALEX: (Pg 13) You don't change the speech that got you this far three days before the election.

CHARLIE: (Pg 14-15) (to Alex and Sara) Well, there's a, uh. Slight chance a story may come out about me on ... Twitter or somewhere on the Internet and quote me sayin’ some stuff about how, maybe, I don’t quite uh . . . believe in God anymore.

SARA: You son of a . . . ! (hits Charlie on the arm on each bold and italicized word) Turning your back on Jesus!? He's the one that helped get you elected in the first place! YOUR CAMPAIGN SONG IS "JESUS IS MY RUNNING MATE!!!

CHARLIE: Would you please stop hitting me! And you're the one who picked that song, said donations would increase if we used it.

ALEX: (Pg 18) (with a deadly smile) Mrs. Whitmore, we've been thrilled to have your support throughout this campaign, but if you can’t let your husband explain this possible crisis, I will seriously call security and have you escorted out of the building. . . (Sara sarcastically “zips her lips while Alex gestures for Charlie to continue) Senator . . .

CHARLIE: (Pg 19) Well, this morning, after the, uh . . . funeral. I’m standing out of the way and some guy comes up to me . . . *****Flashback scene*****

MARSHALL: Beautiful service. (offers hand to shake) I’m Marshall, by the way. I’m an independent reporter.

ALEX: (interjects) Code for blogger . . .

MARSHALL: Mind if I . . . ask you a few questions? (points a small digital recorder at Charlie, then launches into rapid fire questioning) (Pg 20) Were you saddened by the news? Did you think about your own sons? Did you turn to prayer in your time of need?

CHARLIE: (to audience) And I don't know why. But it struck me as such a ... peculiar question. "Did I turn to prayer in my time of need." I mean, asking something so personal. At a funeral. And something in me just. . . snapped. So, I told the truth. (to Marshall) No. I did not. I did not turn to prayer . . .

SARA: (interjects) Oh, sweet Jesus.

CHARLIE: . . . These families don’t need my prayers right now, son, they need my action. I’m a politician. And it's my duty to honor the victims by doing everything in my power to make sure this never happens again.

MARSHALL: (Pg 21-22) Do you . . . believe in God?

CHARLIE: What?

MARSHALL: If you don't think prayers/will help the victims, I'm just wondering if you believe in God at all? (Charlie pauses thoughtfully)

ALEX: (interjects) Did you or did you not say you don’t believe in God?!

CHARLIE: (blurts to Alex) I SAID, "HOW CAN YOU BELIEVE IN A GOD THAT WOULD ALLOW SOMETHING LIKE THIS TO HAPPEN?! (pause, back to Marshall) And continue to happen - over and over and over again! And I'm sorry, son, if I seem upset, but this was at a school. The school our boys go to. And it could have just as easily been their classroom that . . . (growing incensed) Some hotshot decided he’d make a name for himself by shooting up a classroom with an AR-15. So no, at this moment, I do not believe in a god that would allow something like this to happen, and I will not waste my time with prayers when there is TOO MUCH WORK TO BE DONE! *****End Flashback*****

SARA: (panicking) Oh my god oh my god oh my god. (to Charlie) If you're sayin' you wanna change your speech so you can tell all those decent, hardworkin', God-fearing people that their prayers are nothing but a "waste of time," then you will not only lose this election, but you'll be laughed out of politics.

CHARLIE: Okay, honey, calm down. It's no big deal.

ALEX: (Pg 23-24) (looking at her phone) Your new best friend tweeted "Senator Whitmore Speaks Out Against Guns, God and Prayer." And there are already twenty re-tweets, plus a dozen or so comments. This was posted two minutes ago. We need to walk this back, say you were grieving, the kid took your words out of context. If we don’t get ahead of it, you’re not only jeopardizing this election, but your entire future in politics!

CHARLIE: And what if I don’t want to limit the damage?! (beat) (Pg 27-28) I was ... watching our friend throw dirt into his sons' graves. And we're all bowing our heads in prayer and I thought ... How's our prayer going to prevent another senseless shooting? And just when the pastor's saying "ashes to ashes," it hit me: what if this is it? Dust to dust, nothing waiting for us on the other side. Would that be any crazier then some man in the clouds "listening to our prayers"? What if God, the concept of God, was just created by us to cope with the pain and randomness and heartache of his miracle we call life? Wouldn't that mean we shouldn't be so hung up about what it says in my book versus your book, or feel the need to hold on to our outdated laws and ideals, especially the one that got us into this mess in the first place: our "God given right to bear arms?!”

ALEX: Whoa! Sir. All due respect, talking about God is one thing . . . but you cannot take on the 2nd Amendment. This story's bad enough. If you compound it by saying "your guns are bad," that'll be it for us! (to Sara) Please try to talk some sense into your husband. (leaves)

CHARLIE: (Pg 29) (to Sara) I thought the whole point of this country was to keep religion out of politics. It’s in the first damn amendment.

SARA: We both know what’s important to your voters: faith, family and football. Same values they want to see in their politicians. (takes a deep breath) (Pg 31-32) Is what happened at our school wrong? Of course. It's horrifying and sick and impossible to live with -- which is why we need our Faith to help us through. Do we need to do something about guns? (shrugs) I don't know. Personally, I believe in my right to bear arms, and sure as heck don't want to give up my Baby Glock. But when you start talkin’ all this craziness about there being no God, or prayer is useless then you have gone too far, Charlie Whitmore! So go splash some water on your face, give the speech you always give, and knock off this insanity!

CHARLIE: (softly) I saw it Sara. First-hand . . . the blood splattered around that classroom. On the chalkboard and the American flag. A group of crying 1st graders standing in a baseball field. Frightened parents sprinting under the yellow caution tape to find and hug their scared little children. No one should have to know that fear. No one. (beat) And that’s my fault. Like it or not, my actions as Senator played a role in this tragedy. And the ones that came before it. How long and fiercely I fought to protect our “God-given right” to bear arms. (beat) This has to be addressed. Now.

SARA: You are not responsible for the 29 deaths last week. That was not your fault.

CHARLIE: Oh yeah, whose was it then?

SARA: That boy who went crazy!

CHARLIE: “Guns don’t kill people,” right?

SARAH: If it wasn’t a gun at a school, it would have been a bomb at a hospital. You can’t stop every single lunatic without taking away our freedoms. You can’t just change your mind and expect me to support you. (long beat)

CHARLIE: (Pg 33-34) When did you start believing in God?

SARA: I’ve always believed, what are you talking . . .

CHARLIE: No, we don’t come out of the womb “believing in Jesus.” It’s not instinct; we have to be taught. I learned about God when I was 6 years old at my daddy’s funeral. They told me God had taken my daddy because “Heaven needed another angel.” And I believed that. Church gave [us] structure and security . . . and hope. But you know what else I believed in when I was 6 . . ? Santa Claus and the Easter Bunny.

SARA: Okay. I get it. I GET IT!

CHARLIE: (continues over her with growing vehemence) But then you realize that God is always watching, except when some hothead shoots up an elementary school. That was just ALL PART OF GOD’S MASTER PLAN, RIGHT?!! (deep calming breath, then sadly) That just makes me feel helpless. (exits) ****** Scene******

VOICE OVER: (Pg 38-39) So now, without further ado. Here he is. . . Raleigh’s own . . . Senator Charles Whitmore!

CHARLIE: (taking the stage) Thank you for that warm introduction. (to the crowd) How are my fellow North Carolinians doing tonight? And don’t tell me the score of the game, okay? I’m gonna watch it later and want to be surprised. (then silence) You all know me, right? You don’t need to hear this same old speech again. (rips his talking points in half) You trust that I have your best interests at heart and would never steer you wrong.

FROM THE CROWD: AMEN!

CHARLIE: Ha, yes. “Amen.” I’m glad you said that, because . . . Well. That’s exactly what I wanna talk about tonight. (pause) God -- ****** Scene******

REPORTER 2: (upbeat) In what can only be described as a landslide, Senator Whitmore will walk away with 71% of the popular vote. A roller-coaster weekend for the campaign: first a story that appeared on Twitter. Then that now-famous speech that stunned a packed auditorium who gave the senator very little applause when he left the stage. But the speech went viral, 2 million views in the first 24 hours alone. And that of course led to tonight, with the campaign celebrating! Turnout to be over 10,000! *****Scene*****

ALEX: (Pg 45) (ecstatic and celebratory) . . . Senator, you did something unheard of: you got people on both sides to vote for you. The liberals want you to take on the gun lobby, the conservatives want to help you find your way back to God! They realized you were more interested in principles than towing the party line. Voting for your idea: that living without fear is more important than religion or guns or antiquated laws. (Pg 47) [Now] deliver your acceptance speech as written – with confidence, humility and no specifics – Just a few bland platitudes about a brighter future.

CHARLIE: (Pg 52) (on TV) Thank you! Thank you all so much! And thank you for believing in me – believing that we all can make a difference . . . (three distinct gunshots ring out and Charlie responds to being hit – long beat)

REPORTER 2: (solemnly) At 7:52 PM while Senator Charles Whitmore was delivering his acceptance speech to a packed crowd, an unidentified gunman fired three shots at the Senator who was rushed to the hospital and pronounced dead on arrival.

REPORTER: The gunman, who used a TEC-22 semi-automatic handgun was apprehended by police . . .

REPORTER 2: The shooter has been identified as a 19-year-old student with no history of mental illness. . .
```

---

## IC-0742: Confrontation

- Title: Confrontation
- Author (byline): Mary Krell-Oishi
- Work: Perspectives: Relevant Scenes for Teens
- Publisher: Meriwether Publishing
- Publication date as stated: March 1997
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: LEANNA, BRANDON
- Teaser before the introduction: Yes
- Spoken words (computed): 2135
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mary Krell- Oishi
Book: Perspectives: Relevant Scenes for Teens
ISBN: 1566080304
Publisher: Meriwether Publishing
Date(Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
Actor: Brandon and Leanna had a brief relationship in high school.
Actress: Meeting each other at a party five-years later was the last thing that either one
expected.
Actor: High school memories of football games, dances and crushes are, for some, the best
memories of our lives.
Actress: For others the memories are much less pleasant.
Together: And therein lies the basis for this Confrontation by Mary Krell-Oishi.
```

### Performance text (classify this)

```text
LEANNA: Well, this is fun. What ever possessed me to come to this party is a mystery to me. (She pulls a small compact from her purse.) So glad I took the time to have my roots done so I could impress all these people I don't give a damn about. (Yelling) I hate everyone here!

BRANDON: (He enters on her last line.) Oops, sorry...Leanna? Is that you?

LEANNA: Brandon. Of course. Why wouldn't it be you? It's been a lousy party, a lousy day, and now, to add insult to injury, you come in. Thank you, God. You're a funny guy.

BRANDON: Ah. Carrying around some unresolved conflicts from your past?

LEANNA: And you're talking to me because...?

BRANDON: Sorry, I just poked my head in for a minute.

LEANNA: Well, then, why don't you just poke it back out.

BRANDON: It's been a long time.

LEANNA: Not nearly long enough.

BRANDON: Uh-huh. Well, I'm glad we had this chance to talk, to renew old friendships. I'll just be going.

LEANNA: Go to hell, Brandon.

BRANDON: Ah, still thinking of opening the Leanna MacDonald school of how to win friends and influence people?

LEANNA: Please, sit down, stay a while. I need more crap in my life.

BRANDON: What is with you? This is a party, lots of people you haven't seen in a long time, good food, good music, nice memories. It's supposed to be a fun thing, you know?

LEANNA: Go to hell, Brandon.

BRANDON: You are a piece of work, aren't you?

LEANNA: Look who's talking. Why don't you get the hell out of here?

BRANDON: You invited me to stay.

LEANNA: You can't hear sarcasm?

BRANDON: Hey, I just came in to find my fiancee. I can see she's not here, so I'll just be on my way.

LEANNA: Your fiancee? You're getting married?

BRANDON: That surprises you? I'm over twenty-one.

LEANNA: But to make that kind of commitment. To actually be there for someone other than yourself.

BRANDON: Listen, you've obviously got some unresolved problems that have nothing to do with me and everything to do with your own screwed-up mind. I haven't seen you in years, I said hello, you said go to hell,I think our conversation has run its course.

LEANNA: Witty as you always were. Quite the little wordsmith, aren't you? Of course, I don't remember us doing that much talking 10 those many years ago.

BRANDON: Jeez, Leanna, that was how long ago?

LEANNA: Five years, seven months, two weeks and three days.

BRANDON: (Uncomfortably taken aback) Oh...I didn't realize...

LEANNA: Please, I made that up. It's been about five years. I haven't been counting the days since last we touched, trust me.

BRANDON: Oh. I didn't think you had. I mean...never mind.

LEANNA: God, there is just no end to your ego, is there? Your name should be Axis, you seem to think the world revolves around you.

BRANDON: You seemed to think it did, way back when.

LEANNA: Brandon, I was barely fifteen. I was stupid. Only someone as stupid as a fifteen-year-old would get that wrapped up in someone as shallow and superficial as you. Most women grow up and expect to marry a man, not a worm. So did you meet your fiancee on the playground? Still cruising around looking for innocents?

BRANDON: I want to know what your problem with me is. We haven't seen each other in years, yet you act like I murdered your family yesterday. So, we made love a long time ago...

LEANNA: We didn't make love. I made love, you had sex...

BRANDON: OK, it was sex.

LEANNA: What surprises me is that I actually thought it was love. It's what you told me.

BRANDON: I was a kid myself. I would have said anything to get what I wanted. What are you still so upset about?

LEANNA: It meant something to me. It still does.

BRANDON: Well, get past it.

LEANNA: I can't.

BRANDON: What do you want from me? You want me to lie to you and say it meant something special? I was in high school. I'm sorry that you got caught in the fallout. Accept my apologies and move on.

LEANNA: That's all it was to you. You are pathetic. You take a little girl and use her. That, no doubt, is what you're going to end up doing to that poor girl you intend on marrying.

BRANDON: I love Sarah.

LEANNA: You told me you loved me, as I recall.

BRANDON: I never told anyone else I loved you. Hey, when you're a kid you say what you have to say to get what you want. I'm sorry. What do you want from me?

LEANNA: Nothing. You've got nothing to give me that can change anything.

BRANDON: If I could take it back, I would. But that was a long time ago.

LEANNA: You never even think about it, do you?

BRANDON: Honestly? No.

LEANNA: Hardly a day goes by that I don't.

BRANDON: It wasn't that big a deal, trust me.

LEANNA: It was for me. I thought I was someone important to you, that you cared. Obviously I was wrong. People, I've discovered, are only interested in what they want and everyone else be damned. And that is the basic fact of life.

BRANDON: (Beginning to become angry) No, sweetheart! The basic fact of life is if you don't talk, you can't expect anyone to know what's going on. And here's something else for you to think about. I didn't force you to do anything you didn't want to do. You were a more than willing accomplice, if memory serves.

LEANNA: Wrong! I was a child. What you did was practically rape.

BRANDON: Take some responsibility for your own actions. You were fifteen, I was seventeen. You could have said no.

LEANNA: So could you.

BRANDON: Oh, right. You invite me over to your house, your parents are gone for the night, and we end up in your room "watching TV." You know why I didn't call you? Because you were a little too easy. Ijust wasn't interested in a girl that would be so willing to give herself away.

LEANNA: That's a horrible thing to say.

BRANDON: Sometimes the truth is pretty ugly. Deal with it and get on with your life.

LEANNA: Get on with my life?! You have no idea how hard it has been to just "get on with my life!"

BRANDON: It was one time. One crummy time. My God, let it go.

LEANNA: That's so easy for you to say.

BRANDON: Yeah, it is. Why are you holding on to this? What is the big deal?

LEANNA: I got pregnant.

BRANDON: (Pause) What?

LEANNA: That one time, I got pregnant. That's what the big deal is.

BRANDON: You got pregnant? How? Never mind, stupid question. Why didn't you tell me?

LEANNA: I tried to. You wouldn't listen.

BRANDON: When? When did you try?

LEANNA: I came over to your house, I looked for you outside the school after your classes, I would wait for you in the parking lot. Hell, I even came to football practice and stood at the sidelines hoping to talk to you.

BRANDON: Why didn't you say something?

LEANNA: It's hard to talk to the back of a head. You would never look at me. You know as well as I do that you wanted nothing to do with me after you accomplished your goal of bedding me. I was a number to you. Well, my number got called.

BRANDON: What happened?

LEANNA: Now you're interested?

BRANDON: Yes, now I'm interested. I would have been then, too, if you'd given me a chance.

LEANNA: Oh no you don't. I tried to talk to you, dammit, I tried.

BRANDON: I was a kid, too. A male kid. You think I needed to have some cow-eyed girl follow me around making me feel guilty for taking her virginity?

LEANNA: You could have asked. But you didn't. Completely wrapped up in yourself. But even if you did and I told you, what would you have done?

BRANDON: Done?

LEANNA: Yeah, done. You know, a course of action, a plan? What would you have done?

BRANDON: I don't know.

LEANNA: Typical.

BRANDON: Dammit, Leanna. You spring this on me years and years after the fact and I'm supposed to come up with instant answers.

LEANNA: I knew then. You would think only of yourself and anyone who got in your way was simply a roadblock to be pushed through. You would have turned your back on me, admit it.

BRANDON: Would you have wanted me to marry you? With you at fifteen? And me on my way to college?

LEANNA: At least I would have had an option.

BRANDON: So would have I, but you took those away. What did you do?

LEANNA: What the hell do you think I did? I was alone, I had no choices. I had an abortion.

BRANDON: By yourself? You went through that by yourself?

LEANNA: Not completely.

BRANDON: Did you tell your parents?

LEANNA: No. Only one other person knows, the person that took me to have it. . . taken care of.

BRANDON: I should have been that person.

LEANNA: You're saying you would have been there for me? Don't make me laugh. I was so low on your list of priorities that I didn't exist.

BRANDON: Why do you think I'm such an ass? You might have been surprised.I can't guess what I would have done. I'd like to say that I would have been a good father and supported you both financially as best I could...

LEANNA: But...

BRANDON: But I honestly don't know. I was a high school jerk, one of those guys that they write as the fool on TV sitcoms. But I honestly don't think I would have let you go through it alone.

LEANNA: It's been my experience that we all end up alone when it comes time to count on someone. You proved that.

BRANDON: I proved nothing! I wasn't given a chance to prove myself. You could have tried. So you made all the choices, for me, about me, and without me.

LEANNA: Listen, I said what I had to say. I've carried it around for a long time, and now that it's out I guess I can let it go.

BRANDON: Yeah, you've carried it around for a long time. You just dumped this on me. I need to deal with it.

LEANNA: What's there to deal with? It happened to me, not to you.

BRANDON: It happened to both of us. You just didn't bother to share it.

LEANNA: I'm going to say this once, OK, and I don't want to go over it again. You made me pregnant when I was fifteen, you ignored me right after it happened, treating me as if I didn't exist. It was a problem I had to deal with in the best way a fifteen-year-old knows how. Maybe I should have had more faith in your nature, but I didn't. But basically, the facts are I carried this anger and hostility around for a long time and directed it at everyone I dealt with and everything I tried. My attitude was that I was alone and you reinforced that, directly or indirectly, it doesn't matter. And, yeah, maybe I should have tried harder to tell you, and maybe, just maybe, you would have been warm and compassionate. I doubt it, but we'll never know. The great thing is, I told you. You wanted me to get past it, to let it go? Well, maybe now I can.

BRANDON: So you dump this on me?

LEANNA: Dump what? That you impregnated some stupid little girl who had a mad crush on you? I took care of the problem, Brandon. It's done with. And frankly, a day doesn't go by that I don't think about it and have more than a few regrets. But I have to tell you what an ass I always thought you were and finally the reason why. I've waited a long time to do this. God, I feel great.

BRANDON: I feel like crap.

LEANNA: Then my work here is done.

BRANDON: You don't feel the slightest remorse?

LEANNA: About the abortion? Yeah. But, from my point of view, I had no choice. I was fifteen and had to make some grown-up choices on my own.

BRANDON: What about the way you told me, the way you just screwed up my mind with your news?

LEANNA: Hello! This isn't about you. This is about me.

BRANDON: You could have counted on me, I'm sure of that. You could have.

LEANNA: Well, I'm sure you can't count on anyone except yourself, Brandon. I learned it early and remembered my lesson well.

BRANDON: You never gave me an opportunity to prove you wrong.

LEANNA: You're a funny guy. It's so easy for you to say this now, from a safe distance from the reality of the situation I actually dealt with. Trust me, you have no idea what you would have done. Or maybe you do..,and you can't face the fact of it. Maybe you're not the great compassionate guy you'd like to believe. Think about that one in about fifteen years or so when you and your little wifey have a daughter and she starts dating some cute seventeen-year-old guy who reminds you of yourself. Think about that, my friend. (She begins to exit)
```

---

## IC-0743: Constellations

- Title: Constellations
- Author (byline): Nick Payne
- Work: Not specified
- Publisher: Farrar, Straus and Giroux
- Publication date as stated: Dec 2014
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MARIANNE, ROLAND, ACTOR, ACTRESS, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1523
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nick Payne
ISBN: 978-0865477711
Publisher: Farrar, Straus and Giroux
Date (Month/Year): Dec 2014
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Marianne, a physicist, and Roland, a beekeeper, meet at a party. They hit it off and their relationship blossoms.

ACTRESS: It’s incredible to be in love – but it’s even more incredible when that love turns into something more . . .

TOGETHER: Commitment . . . Constellations by Nick Payne
```

### Performance text (classify this)

```text
Note: Marianne works at Sussex University, indicating that both characters could/should be performed with British accents.

MARIANNE: (Pg 9-12) Do you know why it's impossible to lick the tips of your elbows? They hold the secret to immortality, so if you could lick them, there's a chance you'd be able to live forever. But if everyone did it, then there'd be chaos. Because you can't just go on living and living and living. . . Try it. Your elbows, try licking them. (Marianne attempts to lick her elbows, demonstrating the difficulty. Roland, initially hesitant, also attempts to lick his elbows.)

ROLAND: See what you mean. I'm Roland.

MARIANNE: Marianne.

ROLAND: So what do you, what do you do? For a living.

MARIANNE: I work at Sussex University. (Pg 21) Quantum cosmology. (Pg 12) Yourself?

ROLAND: I'm a beekeeper.

MARIANNE: Really?

ROLAND: Yeah, yeah. I'm really a beekeeper.

MARIANNE: I [absolutely] love honey.

MARIANNE: (Pg 48-49) This is a surprise. It's the middle of the afternoon.

ROLAND: Are you busy? . . . There's something I'd like to say. To you. (Roland takes a piece of A4 paper from a pocket and nervously reads.) There are three different kinds of bees. The drones, the workers and a single, solitary queen. The workers are all women. Their job is to forage for honey, pollen, etcetera. Their lifespan is potentially anywhere between five weeks and six months. And then they die. Drones exist solely to have sex with the queen. Each hive tends to have around a hundred drones. Honeybees have an unfailing clarity of purpose. Their lives are often intensely short. If only our existence were that simple. If only we could understand why it is that we're here and what it is that we're meant to spend our lives doing. I am uncertain when it comes to a great many things. But there is now one thing I am defiantly certain of. (Roland folds up the piece of paper, puts it back in his pocket and - from another pocket - takes out a small black box.)

MARIANNE: Roland, please. (Roland kneels and opens the small black box.) Roland, get up, come on.

ROLAND: Marianne Aubele, will you marry me? (Beat -- Roland slowly gets to his feet)

MARIANNE: Roland, we talked about this . . . (she is hesitant, but then quickly makes up her mind) (Pg 52) Okay

ROLAND: (Astounded) Really?

MARIANNE: (giggling and excited) Yeah, really. (Marianne kisses Roland. Roland slides the engagement ring on to the appropriate finger. Marianne kisses Roland again.) TRANSITION

ACTOR: And so marital bliss descended on the happy couple.

ACTRESS: For a few years they shared everything. An apartment, meals, clothes . . .

ACTOR: Until one day, Marianne started having headaches and other unexplained symptoms. She decided to go to her doctor for a routine check-up.

ACTRESS: It was then that the Constellations shifted . . .

Marianne enters - The spark has gone out of her eyes and she appears extremely tired and stunned. Roland immediately recognizes from her appearance that something is drastically wrong. Marianne’s speech is obviously impaired. She searches for the right word for nouns especially.

ROLAND: (Pg 54) -How bad is it? Mary

MARIANNE: It's pretty bad. They said being under forty might help, but –

ROLAND: Mary, how bad is pretty bad?

MARIANNE: I'm not sure I want to talk about it right away. I'm not sure I can talk about it.

ROLAND: Do you want something to drink, do you want some water?

MARIANNE: No thank you. . . (Beat) He said, I think, something like a third, a third of people live for a year. (Pg 59) It's called a glioblastoma multiforme. (Pg 56) He said I might have trouble selecting the right words. (Pg 59) Which is why I've been having trouble . . .

ROLAND: Speaking.

MARIANNE: (Pg 55-56) He said they can operate. Try and remove it, remove as much of it as they can. Then they said radiotherapy but if I'm too weak for radiotherapy, they said chemo. . . . It's right at the front.

ROLAND: The front?

MARIANNE: It's all over the frontal lobe. (gesturing to her forehead)

ROLAND: I don't know what that means.

MARIANNE: He said I should expect seizures.

ROLAND: Jesus Christ.

MARIANNE: It's palliative. Whatever they do. It's not - They can't.

ROLAND: Okay.

MARIANNE: They said this is it.

ROLAND: Okay.

MARIANNE: This is it, they said.

ROLAND: Okay. Okay. . . I would have come with you if you'd told me, you know. I would've cancelled –

MARIANNE: I know.

TRANSITION

ACTOR: Cancer – One of the constellations of the zodiac

ACTRESS: Glioblastoma multiforme is the most aggressive type of brain cancer.

ACTOR: People suffering from this form of cancer live on average less than 15 months, even with radiation and chemotherapy treatments.

ACTRESS: Symptoms progress rapidly as the brain literally begins to die.

ACTOR: Blurred vision, vomiting, loss of appetite and decreased ability to read, write and speak . . . Until . . .

MARIANNE: (Pg 70-71) Roland, I don't think that I can go back to work.

ROLAND: You've told them then?

MARIANNE: Not yet.

ROLAND: So what about part-time?

MARIANNE: I don't know the point. . . . Either I’m walking (she means working, but can’t find the right word) or I’m . . . (She tries again) Either I’m . . . . walker. (Gives up on the word working) I either do it or I don't. Scares me.

ROLAND: Work?

MARIANNE: Stopping.

ROLAND: Stopping work scares you?

MARIANNE: What will I do?

ROLAND: We'll go away. We can do whatever we want.

MARIANNE: I don't - I don't -

ROLAND: I mean it.

MARIANNE: I . . . . I don't. We can't. I have to . . . have to . . . make a (can’t find the word “decision”) I have to have a choice . . . Control. (Marianne begins using sign language and Roland voices her words aloud. An occasional word or phase can be voiced together by both Marianne and Roland)

MARIANNE: (Pg 68-69) I keep thinking of Mum. Before she died.

ROLAND: Right.

MARIANNE: When she said she didn't want any more food. Do you remember?

ROLAND: I'm not sure we ever really talked about it?

MARIANNE: She said she wanted them to stop the IV, did we talk about that? (confused)

ROLAND: I think maybe we did yeah.

MARIANNE: They asked me to leave. I went back the next day and she was starting to look like a ghost. It takes an enormous amount of strength. When you're like that. To keep going. I’m not sure I have it.

ROLAND: You don't know. You don't know that.

MARIANNE: Sinking feeling. Mum wasn't scared of dying, she was scared of being kept alive. You know?

(Marianne goes to cry, but stops herself)

TRANSITION

ACTOR: And Marianne faced a similar fear. Because the rest of her body was young and healthy, she was worried that life support efforts would leave her in a vegetative state; wasting away for weeks or even months.

ACTRESS: Despite radiation and chemotherapy treatments, Marianne was dying. Her research skills couldn’t find a cure . . . but they did provide her with an option.

TOGETHER: Death with dignity

MARIANNE: (Pg 64-67) (severe struggling with her words) I think I’d like to go abroad. I’m not . . . I’m not sure how much of a difference the chemo is really making.

ROLAND: D'you mean you're not sure or they're not sure?

MARIANNE: I mean me. I mean I’m not sure.

ROLAND: Why? What aren't you sure about?

MARIANNE: It's ganging . . . It's . . . It's . . . (can’t find the words anymore and resorts back to sign language. Roland voices this passage and Marianne is silent, we can see the strong emotions in her facial expressions) I was on the train and I was coming home. A group of men got on. A group of thirty-year-old men. They started, they started winding me up. I put my laptop in my bag and I tried to move to a different seat. But they blocked me, they wouldn't let me past. I couldn't speak. I couldn't find the right words and they started laughing. They howled with laughter. I started to cry and finally one of them said that's enough.

ROLAND: You should have said, you should have told me.

MARIANNE: I went on to campus. (in sign language only)

ROLAND: What do you mean [“I went on to campus”], what for?

MARIANNE: (she struggles to speak these words aloud) To have lunch with Melisa. I had a seizure.

ROLAND: What? When? Mary.

MARIANNE: A couple of weeks ago. (in sign language only)

ROLAND: A couple of weeks ago? (Marianne nods) Why didn't you tell me?

MARIANNE: (she struggles to speak these words aloud) It's the words, Roland. It's exhibit (can’t find the word for “exhausting”) It's ex . . . . It's becoming more and more tiring.

ROLAND: You mean speaking to me, the two of us, is tiring, or you mean everything?

MARIANNE: (aloud) Everything.

ROLAND: I didn't realise. . . I’m sorry. . . I don't know what to do . . . So when you say abroad, you mean abroad and not come back? (Marianne nods, we see the resignation in her face)

ROLAND: How does it work?

MARIANNE: You become a member. (sign language only)

ROLAND: A member?

MARIANNE: (Marianne signs and Roland voices) Pay some money.

ROLAND: Then what?

MARIANNE: (Marianne signs and Roland voices) If you're serious you write to them. Outline why they ought to be taking you seriously.

ROLAND: And if they do?

MARIANNE: (Marianne again tries to speak aloud) You meet someone. . . . Out there. You . . . You . . . You have to meet them a couple of times.

ROLAND: Then what?

MARIANNE: (aloud) Then it's up to you.

ROLAND: How do they do it, how does it work?

MARIANNE: (aloud with growing frustration) They use something called a Bar Abar . . . A . . . A

ROLAND: It's okay.

MARIANNE: (aloud) They mix it with water.

ROLAND: (angry, sad, exasperated) I don't really know what to say -- I want to know what to say to you.

MARIANNE: (aloud) A lot of people apparently never go through with it. A lot of people, once they've been given the green night (searching for the word “light”) . . . Night . . . Once they've . . .

(she gives up, frustrated – may pound her head or pull her hair)

ROLAND: It's okay.

MARIANNE: (reverts to signing as Roland voices) They're, they're happy enough knowing it's there . . . . (Marianne speaks aloud) Safety net. For a lot of people.

ROLAND: And is that how you're feeling about it?

MARIANNE: I don't know. (Beat, then Marianne slowly nods. Beat) (pg 68-70) I'm so tired, Roland. It's not just the speaking. Reading. I'm having trouble - Numbers, words, on the page. I know the word . . . I know the word. But I don't know the letters. None of the letters seem right.

(Gets stuck on the word “reading” again) Rea . . . Rea . . . Rea

ROLAND: You don't need to finish. I think I know what you're trying to say.

MARIANNE: (in anguish) How? . . . How can you know what I'm trying to say? . . . Mmm . . . . Most of the time I don't even know what I'm trying to say.

(Both characters exit – scene change) – In silent pantomime we should see Marianne enter, and retrieve the medicine she’s gotten to end her own life. She mixes it with water, perhaps pens a note to Roland and then drinks it. She should sit as the medicine takes affect and we should see her pass from life. Roland enters – finds Marianne’s lifeless form on the floor and reacts. (Both characters exit)

Roland re-enters, perhaps silently reading the note left for him by Marianne, then focuses in the distance as if he can hear Marianne’s voice)

MARIANNE: (Pg 9) (only a voice off-stage, in Roland’s memory-she speaks clearly and there is great energy in her voice) Do you know why it's impossible to lick the tips of your elbows? They hold the secret to immortality, so if you could lick them, there's a chance you'd be able to live forever. But if everyone did it, then there'd be chaos. Because you can't just go on living and living and living. Try it. Your elbows, try licking them.

ROLAND: [I] See what you mean. . . . (Roland breaks down to tears)
```

---

## IC-0744: Controlling Interest

- Title: Controlling Interest
- Author (byline): Wayne Rawley
- Work: Laugh Lines, Pgs 337-348
- Publisher: Vintage
- Publication date as stated: April 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JACK, BRAD, DAVID, STEVEN, ASHLEY, BETHANY
- Teaser before the introduction: Yes
- Spoken words (computed): 1248
- Already set (do not supply): none

### Source block (context only)

```text
Author: Wayne Rawley
Book: Laugh Lines, Pgs 337-348
ISBN: 978-0307277138
Publisher: Vintage
Date (Month/Year): April 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: (Raise right hand and left foot – solemnly) "Do you promise never to trade your bubble gum cards with a girl? Never lend your best fishing worms to a girl? And never let a girl carry your books home from school?"

ACTRESS: Ever since Spanky, the President of the He-Man Woman-Hater’s Club in the 1980’s version of “Our Gang” attempted to swear in new recruits with this oath, little boys have been having a difficult time understanding and having relationships with little girls.

ACTOR: The saga continues with a modern-day boardroom negotiation in . . .

TOGHETHER: Controlling Interest by Wayne Rawley.
```

### Performance text (classify this)

```text
Suggested Roles Actor: Jack, David, Steven

Actress: Brad, Ashley, Bethany,

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

At rise, JACK sits at his desk wearing a telephone headset. The phone rings. JACK answers.

JACK: (Pg 337-348) This is Jack. Yeah ... Yeah, what can I do for you, Fred? I've got a meeting starting like right now. Uh-huh. Uh-huh. Fred, Fred - honestly, let me stop you right there, I don't know if you're ready. Uh-huh. Well, we're gonna swing. Yes, Fred, on the swings -That's what I'm talking about - Well, let me ask you this: Can you pump? (BRAD enters)

BRAD: Jack, we're getting creamed out there. (JACK holds up his hand as if to say "I'm on the phone") Oh, sorry.

JACK: (To BRAD) It's okay, have a seat. (To FRED.) Yes, Fred, pump. Can you propel the swing back and forth under your own power without having to be pushed by a second party? (Motions to BRAD "Can you believe this guy?") Okay, look, Fred, I have to go. You come around lunch recess, we'll give you a go, but I don't want to see you eating your boogers because we're not doing that anymore. We're eight now. Okay, well, okay. See you then. (He hangs up. To BRAD.) Dude still eats his boogers.

BRAD: Gross.

JACK: What's up?

BRAD: We're getting cremated out there, Jack. They got ghost runners on every base, and they keep changing where second is. One minute it's the garage door, the next it's the side hedge. They're just making it up as they go along.

JACK: They're Big Kids, Brad, it's important we give them the impression that we are happy they're even letting us play. (DAVID and STEVEN enter.)

DAVID: I'm telling you, Steven. Ask Jack.

STEVEN: Jack, I'm sorry, I missed last week. Is it true we aren't eating our boogers anymore?

JACK: It's true, we're not. If you want a voice, come to the meetings.

STEVEN: SO what are we supposed to do with them?

BRAD: We don't know yet. For now, just leave them in there.

DAVID: We're looking into it. I'm talking to an eleven-year-old, says you can flick them on people.

JACK: Gentlemen, enough. We aren't here to discuss old business. I have something very important I need to discuss with you. I've been thinking about this since, like, this morning.

DAVID: I'm sorry, um, wasn't this morning, like, a bazillion years ago?

JACK: I know. Yes, it was. That's why I asked you guys to come over to play today. I've been thinking - I've been thinking about this and . . . I want to discuss the possibility of . . . of us . . . liking girls.

BRAD: NO WAY!

DAVID: GROSS!

STEVEN: (Pointing at JACK.) [SISSY! SISSY! SISSY!]

JACK: Hey now. We don't need that kind of insensitive talk around here, Steven. Please.

Let's be kids about this. Besides, I think I will have the support of the membership here when I say, you're the [sissy].

STEVEN: You're the [sissy].

JACK: You are the [sissy].

STEVEN: Nuh-uhh.

JACK: Yes-huh.

BRAD: Gentlemen, please. You know, we've run around this pole before and I have a feeling we aren't going to come to any real concrete decisions about it today. While you both make excellent points on the other person being the [sissy], I think we should stick to the issue on the table - namely, Jack's proposal that we somehow stop hating girls and begin, what? Liking them?

DAVID: Okay, umm, I'm uncomfortable with this and I'll tell you why. Number one, there is the whole size thing. I mean, they are just bigger than we are, and that's new, okay, that's a recent thing and it frightens me. And number two, they seem to be - what's the word? - smarter than we are.

STEVEN: Not to mention the whole cootie issue.

JACK: Look, I know this is new territory for all of us, but David, look at it this way, okay? Your mommy. You know your mommy?

DAVID: (Not sure where this line of questioning is headed.) Yes, Jack, I know my mommy.

JACK: Okay, well, your mommy is a girl, right?

DAVID: (Cornered.) What's your point, Jack?

JACK: My point is that I have a feeling they may have something to offer us. And I think we ought to hear them out. They've sent two representatives to discuss what would be involved. They are in the outer playroom right now.

DAVID: I am very uncomfortable with this.

BRAD: Guys, come on. We can do this. I believe in Jack. This is the guy who taught us how to make a shadow on the ceiling that looks like a butt - using only a flashlight and our knuckles. We can do this. Come on. (Pause - JACK speaks into a speaker on his desk.)

JACK: Send them in. (ASHLEY and BETHANY enter)

ASHLEY: Good afternoon, gentlemen.

JACK: Afternoon, ladies, please come in, welcome to the playroom. Can I get you some Legos or something?

ASHLEY: Thank you, no. My name is Ashley with an e-y, my daddy's a policeman, and I'm nine. This is my associate, Bethany.

BETHANY: I can do short division.

JACK: Please sit down.

ASHLEY: We understand you are interested in liking us?

JACK: We are interested in exploring that possibility, yes.

ASHLEY: And you are ready to discuss terms? Excellent. Bethany?

BETHANY: (Pulling a document from her clipboard.) I know how to type. (Ashley takes the document.) And I speak French. [Frère Jacques]

JACK: So what do you want?

ASHLEY: Your complete and undivided attention.

JACK: Well, you've got it.

ASHLEY: (Smiling.) Ah, yes, of course I do. Um, no. I mean your complete and undivided attention until the end of time.

JACK: Excuse me?

ASHLEY: In accordance with the terms of the agreement, we will be occupying your every thought, motivation, and decision-making process from the moment you wake up in the morning until the moment you fall asleep at night, at which point we will play a major role in nine out of ten of your dreams. We do allow one wild-card dream, usually a sports dream or flying dream of some type. That is completely up to you, of course. But everything else becomes, for all intents and purposes, about us. (Stunned silence) Bethany, am I missing anything?

BETHANY: (checks her clipboard) Stop doing stupid stuff.

ASHLEY: Right. And you will have to stop doing stupid stuff. Like playing Star Wars and making laser-beam noises with your mouths.

STEVEN: (Scared.) Okay, so what if I don't even care? I mean, like, what if I don't want to stop playing Star Wars? What if I don't even care if I think about you or not, like if say, like, I don't even care?

ASHLEY: I'm afraid that won't be possible.

BRAD: All right then, so what's in it for us? Right? I mean I'm just thinking out loud here at this point, but it seems like you're asking a lot, with all that thought time and no Star Wars and everything, so, like, what is in it for us? Exactly?

ASHLEY: Knowledge, mostly.

BRAD: But we already know everything.

ASHLEY: Right.

BETHANY: (Looking right into their very souls.) We know where babies come from. (The boys are stunned.)

DAVID: (Defiant but timid.) Y-yeah? S-so? So what? Everyone knows where babies come from. They . . . they come from the Garden. With the morning dew. Jack, I'm very uncomfortable with this.

STEVEN: This is out of control, man. This is out of control!

JACK: Yeah, ladies, I think we are going to need some time. To think. This is a lot to consider. And wow, we really do appreciate you coming by-

ASHLEY: Yes, well, gentlemen, thank you for your time. We will definitely be in touch.

BETHANY: I can write cursive. (ASHLEY and BETHANY exit. The boys stare vacantly for a beat. Then suddenly, as if slowly waking from a daze.)

DAVID: Um, Jack? Say, if it is all the same to you, I think I'm going to skip smashing that anthill today.

JACK: Um, yeah. Yeah, David, that would be fine. Take the rest of the day off.

DAVID: Good thing we stopped eating our boogers, huh?

JACK: Yeah, yeah. Good timing on that.

STEVEN: Um, I have to go home and comb my hair. And lose some weight.

BRAD: Jack, how long do you think it will be? Before we . . . you know . . .

JACK: I don’t know, Brad. I wish I could tell you. But I just don’t know.

BRAD: Yeah, I don’t even care. (STEVEN, BRAD and DAVID exit.)

JACK: I know. Me neither. (JACK stands at his desk for a beat, then brings his hand up to his mouth to check his breath. Lights down.)
```

---

## IC-0745: Dani Girl

- Title: Dani Girl
- Author (byline): Chris Dimond and Michael Kooman
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: June 2014
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR, ACTRESS, FATHER, MOTHER, BOTH, DANI, RAPH, RAPHAEL, MARTY, DARTH CANCER, CANCER POSING AS RAPH, CANCER, GOD
- Teaser before the introduction: Yes
- Spoken words (computed): 1321
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chris Dimond and Michael Kooman
ISBN: 978-0573701450
Publisher: Samuel French, Inc.
Date (Month/Year): June 2014
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Dani was beautiful -- and they tried so hard to live happily ever after -- but when Dani was diagnosed with childhood leukemia, the whole world changed.

ACTOR: Before she was even 5 years old, Dani created an imaginary friend, Raph, to help her through the procedures, the sickness, the grief, and the pain.

ACTRESS: See, Raph is short for St. Raphael, the patron saint of healing. Dani and her mom fought the cancer head on and won; and for three glorious years, Dani was cancer free. But then . . .

TOGETHER: Dani Girl by Chris Dimond and Michael Kooman.
```

### Performance text (classify this)

```text
Suggested Roles:

ACTOR: Father, Raph (imaginary friend), Darth Cancer, Marty (age 10), Cancer, God

ACTRESS: Dani (age 9), Chandrelle, Mother

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

FATHER: (Pg 13) Once upon a time. In the Kingdom of Blue Skies

MOTHER: There lived a noble king, King William the Lionheart.

FATHER: With his elegant bride, Queen Katharine, the Compassionate. And one day,

MOTHER: As the sun rose high over their castle . . .

FATHER: They were blessed with a radiant. . .

MOTHER: A beautiful . . .

FATHER: A perfect . . .

BOTH: Daughter . . . And they all lived happily ever after.

DANI: (Pg 14) It's back again, isn't it? (beat) (Pg 15-20) I thought I was done.

RAPH: Hey, kid. It's not the end of the world.

DANI: I hate this place, Raph. It reeks of disease.

RAPH: Think of the games we can play. (becomes flamboyant French hairdresser RAPHAEL)

RAPHAEL: Bonjour! Et welcome to Raphael's Spa de Beauty. Oh la la. Zis must be mademoiselle Danica, ze most belle femme in ze world.

DANI: Well, perhaps one game.

RAPHAEL: Bonne. Zut alors! What is zis collection de stringy fungus on top of your 'ead?

DANI: My hair? I like my hair.

RAPHAEL: Mais non. Zis will not do at all. But, never fear, mademoiselle. Nozing is too great a miracle for Raphael, 'airdresser to ze stars. (He shaves her head.) Sacre bleu. C'est magnifique.

DANI: What? Let me see.

RAPHAEL: (hands her a mirror) C'est belle, non?

DANI: (sees herself and reacts) No. No.

RAPHAEL: It say beauty. It say strength.

DANI: It says sick. I don't want to play anymore!

RAPH: Kid, there are some games you can't exactly quit.

DANI: Give me my hair back.

RAPH: That's not the way it works. (pause) You know how this goes. (pause) Alright. Fine. You win. New game. (becomes WINK WINKENDALE, a game show host) WINK. Good evening, ladies and gentlemen. I'm Wink Winkendale, and this is Trivial Pursuit . . . of Death. Our first contestant. All the way from pediatric oncology, Danica Lyons. (Danica waves to the studio audience and takes her position) Now Danica, here's how our game works: I'm going to ask you the questions on this card. If you can answer correctly . . . Tell her what she wins, Chandrelle. CHANDRELLE. Her hair, Wink. She’s playing for her hair. WINK. And if she loses? CHANDRELLE. It's gonna be a long and drawn-out treatment period full of pain and suffering, followed by almost certain death. WINK. Alright, our first category is geography. Are you ready, Danica?

DANI: I suppose so.

WINK. Your question is . . . which constellation is named for the Latin word for crab?

DANI: Cancer? WINK. Correct! Next question . . . Osteosarcoma and medulloblastoma are types of what disease?

DANI: Cancer. WINK. Correct again. Only one question stands between you and your hair. Are you ready?

DANI: Yes, I am, Wink. WINK. For a lifetime supply of your own hair. Your question is . . . why is cancer?

DANI: What? That's not fair. WINK. Why is cancer?

DANI: I . . . I don't know. WINK. Ooh. I'm sorry, that is incorrect. "I don't know" is not why cancer is.

DANI: Raph! It's not even a real question.

RAPH: Hey, how are you supposed to get rid of something when you don't know why it's there?

DANI: But I don't know.

RAPH: Then I guess you'd better find out. TRANSITION

ACTRESS: The next day Raph takes a back seat to a new friend: Marty Merriweather is moved into Dani’s room in the pediatric oncology ward, and they talk late into the night. Maybe Marty would know the answer to the question: “Why is Cancer?”

MARTY: (Pg 28-29) I vomited nine times last night. It was orange.

DANI: So? Big deal. One night I threw up ten times. And it was green with little purple chunks. (pause) Look, what kind of cancer do you have anyways?

MARTY: Hodgkin's.

DANI: Oh, please. Hodgkin's is a sissy cancer. I'm going to find out why cancer is and then everything will be back to normal. Once I figure out why it is I'll get my hair back.

MARTY: That doesn't make sense.

DANI: But it's true. You're just jealous because I'm going to get my hair back and you'll still be looking all Captain Kirk.

MARTY: It's Picard. Picard is bald. Captain Kirk has a bountiful head of hair. (Pg 37) Do you think this getting your hair back thing would work for me too?

DANI: Probably.

MARTY: Cause I think I know why cancer is. I think you must've done something to deserve it.

DANI: Merriweather, there is no evidence to suggest –

MARTY: Yuh-huh. Cause I broke the bishop in my father's chess set and then I had to come into the hospital . . . What did you do?

DANI: I don't know. I'm fairly certain I'm perfect. *****

BOTH: (Pg 37-38) Once upon a time.

FATHER: In the Kingdom of Blue Skies.

MOTHER: There lived a noble king.

FATHER: And a compassionate queen. They were blessed with a fearless...

MOTHER: A beautiful...

FATHER: A perfect - (He turns away) My Queen, I must leave you and the princess.

MOTHER: What? What are you talking about, Will? You cannot do this to us.

FATHER: Tell her I went on a long journey, to a land far away.

MOTHER: And when she's old enough to ask why?

FATHER: M'lady, by then she will know the truth. What other reason could there be? ***** Dream Sequences*****

(Darth Cancer appears – Words in all CAPS are spoken in the evil voice of Darth Vader)

DARTH CANCER: (Pg 47-48) AND SO WE MEET AGAIN, DANICAN

DANI: Cancer.

DARTH CANCER: That's Darth Cancer to you. THERE WILL BE NO ESCAPE THIS TIME.

DANI: I’ll teach you to stand between a girl and her hair. (She unleashes her light saber; He does the same. They fight)

DARTH CANCER: YOU’LL NEVER WIN FOOLISH CHILD. DON'T YOU REALIZE I'M INSIDE? SEARCH YOUR FEELINGS, IT’S THE TRUTH. Your mother never told you the truth about your father. She never told you why he left.

DANI: He went on a long journey, to a land far, far away.

DARTH CANCER: THAT IS WHAT SHE'D HAVE YOU BELIEVE. BUT YOU KNOW WHAT MADE HIM LEAVE. YOUR FATHER LEFT BECAUSE OF YOU.

DANI: No! (She charges passionately)

DARTH CANCER: (knocks her to the ground) Now, feel the true power of the dark side. (He stretches out his hand.

DANI: (coughs violently and the dream changes again, back to her father) *****

FATHER: (Pg 56) (throughout this speech, Dani reacts in her sleep . . . murmuring “no,” shaking her head, crying, etc) Once upon a time there lived a noble king and a compassionate queen. They lived happily in their blue-sky kingdom. Until one day, along came a princess. Seemingly perfect, the princess was cursed. Before their eyes the beautiful baby transformed into a hideous monster! (DANI opens her mouth, but no sound comes out) The monster banished the king and left the queen a shadow of herself. No one lived happy ever after, because no matter how she tried, the princess could never, ever set things right! *****

DANI: (DANI wakes with a start and gasps for breath.) Noooo! (Pg 64) It’s all my fault.

CANCER POSING AS RAPH: (Pg 68) Why don’t we play a game? It would make all of your pain go away. Forever.

DANI: What is it?

CANCER POSING AS RAPH: (singing) BLUE COTTON CANDY SKIES. / FUNNEL CAKES, ICE CREAM CONES, CURLY FRIES. / THE MUSIC OF CHILDREN'S MELODIC SQUEALS, / GIGANTIC MAGICAL FERRIS WHEELS. IN COMALAND! *

DANI: Comaland?

CANCER POSING AS RAPH: Yeah, Comaland. It's like Disneyland. But not.

DANI: (Pg 69) Will I need needles, or shots or pills?

CANCER POSING AS RAPH: Not in Comaland.

DANI: Okay. I'll play.

CANCER POSING AS RAPH: (turning evil and abrasive) Shut your mouth.

DANI: What did you say?

CANCER POSING AS RAPH: (mocking) What did you say?

DANI: You're not Raph! Cancer! What have you done with Raph?

CANCER: What do you think?

DANI: You killed him? You killed Raph! (tries to attack but is unable to move)

CANCER: You can't win now, stupid. You're in a coma. (laughs maniacally and exits)

DANI: Wait! You can't . . . you can't . . . *****

DANI: (Pg 71-75) (wakes up abruptly. GOD enters.) Who are you? God?

GOD: Sometimes, Dani, you just have to believe.

DANI: (thinking) God? Why is cancer? I'm sorry, but it's urgent.

GOD: I don't have an answer for you, Dani. What I know is this: Everything exists. Good and bad, courage and fear, joy and pain. They all are. Trouble is, they sometimes get all mixed up in the same wrapper.

DANI: But, why?

GOD: Just because things are, doesn't mean they have a knowable reason. Why is love, Dani? Why is candy?

DANI: . . .Then . . . all the hospitals, and the treatments, everything . . . it’s all for nothing. (long pause) I don't want to die.

GOD: I know you don't. But death is another one of those things that just. . . is.

DANI: But you're God. Can't you just take the cancer out of my life completely?

GOD: I could. Like it never happened. But, if I do, you'll lose everything that came with it.

DANI: I think I'd be okay with that.

GOD: Are you sure? Not everybody spends life living, Dani. You have.

DANI: Yeah, but not because of cancer.

GOD: What do you think sparked your incredible imagination?

DANI: Really? (beat) I don't think [it’s] quite worth cancer.

GOD: Then I guess you're right. It was all for nothing. I can give you life without cancer. It just won't be this one. But, if that's what you want . . .

DANI: Wait. Will I get to see my mom?

GOD: Anytime you want. (long pause while she comes to terms with death)

DANI: I'm ready. (holds ups her arms as if bathing in a white light)

GOD: The world is cruel . . . unfair. But hope lives everywhere. Beneath the grief and despair. Now pain shall cease.
```

---

## IC-0746: Date with a Stranger

- Title: Date with a Stranger
- Author (byline): Cherie Vogelstein
- Work: Best American Short Plays 1993-1994
- Publisher: Applause Books
- Publication date as stated: May 2000
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: PAULA, CLARK
- Teaser before the introduction: Yes
- Spoken words (computed): 2462
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cherie Vogelstein
Book: Best American Short Plays 1993-1994
ISBN: 1557831998
Publisher: Applause Books
Date(Month/Year): May 2000
```

### Introduction (context only: never use it for content warnings)

```text
Actress: Let’s face it . . . meeting members of the opposite sex is difficult. Actor: The growing number of internet “MATCH” sites proves that fact. It’s crazy, Actress: It’s dangerous, and you never know what to expect. Together: Date with a Stanger by Cherie Vogelstein
```

### Performance text (classify this)

```text
A typical Manhattan diner. PAULA, 29, nibbles at a muffin as she furtively glances over at CLARK, 31, seated two stools away. CLARK self-consciously reads MY MOTHER, MY SELF, steals a look at PAULA whenever he can. Note: PAULA and CLARK must swing furiously from emotion to emotion without missing a beat. They experience life as it is: fast, big, and uncensored.

PAULA: [Reaches across CLARK for sugar.] Sorry.

CLARK: [Smiles graciously, slides it to her.] No, no, please.

PAULA: [Giggles, pours sugar steadily into cup.] I really, really like sugar in my coffee.

CLARK: [Explodes in laughter.] HAHAHAHA! Hello!

PAULA: [Also laughs nervously as she continues to pour.] And now I'm ruining it!

CLARK: [This is even funnier.] OH WOW...

PAULA: Anyway...

CLARK: Hmm... yeah... {Beat. He reluctantly returns to book.]

PAULA: [plunges back in.] You know, I was watching you turn those pages. And I was wondering to myself, "Is he really reading the words of that book?" I was wondering that so much.

CLARK: Oh, well, what I always say is, when you're reading... why fake it, right? . . . Well, I really like the way you took the initiative with me

PAULA: [Horrified.] What?! Is that what you thought I was doing?

CLARK: Oh well I uh... isn't that what you meant to be doing? [Nervous laugh.]

PAULA: Not so that it would seem like I was doing it

CLARK: Oh, well it didn't. That was just my women's intuition talking.

PAULA: [Suspicious.] What are you doing with women's intuition, Mister?

CLARK: [Quickly.] Nothing. I just meant... I have a strong feminine side to my personality.

PAULA: [Relieved and happy.] Hey! So do I!

CLARK: Which is not to say I'm not all man which I am [Flexes muscle.] but I still read books like MY MOTHER, MY SELF [Beat.] because I care.

PAULA: [Staring deep into his eyes.] Are you... are you attracted to me?

CLARK: Why? Are you attracted to me?

PAULA: I asked you first.

CLARK: But I asked you right after, very quickly.

PAULA: Yes but it's very important for you to perceive yourself as the pursuer, otherwise-puh, puh, puh-God I love p's and things that begin with P. Can you think of some? Porch, ping-pong, pumpkin . . . I'm stalling-I feel vulnerable because of the attractive issue you didn't answer me you don't want to answer me-police, pigeon, PVTZ

CLARK: Look, I do want to answer you, and believe me, I will, but before I do, I first want to say, and I'll say it now-there are a lot of things I perceive myself as, but not being the pursuer is definitely not one of them, okay?

PAULA: [Great sigh of relief] Thanks, that really helped. [She swallows some pills, smiles.]

CLARK: You look pretty when you smile.

PAULA: [Unsmiling.] And when I don't smile?

CLARK: You still look pretty.

PAULA: [Sweet smile.] How pretty?

CLARK: Very pretty.

PAULA: [Still playful.] Prettier than say, your last girlfriend?

CLARK: Hmm, yeah, I'd say that.

PAULA: [Dead serious.] Say it.

CLARK: Uh, you're prettier than my last girlfriend.

PAULA: [playful again.] Oh, you're just saying that. {Bashful beat.] Anyway, it's not like I think my looks are the most important thing in the world, you know.

CLARK: Good for you!

PAULA: How so?

CLARK: Well, beauty is only skin deep.

PAULA: Swear on your mother's life I'm prettier.

CLARK: Gladly. I hate my mother.

PAULA: Just what are you trying to say?

CLARK: That she really knows how to get me mad-you know, in a funny way, you kind of remind me of her.

PAULA: [Horrified.] Your mother?

CLARK: [Thinking he's off the hook.] No, no, my ex-girlfriend.

PAULA: [With relief] Oh! [Ferocious.] That's even worse!

CLARK: Wh-why?

PAULA: Well I mean did you want to marry this woman? I don't get it

CLARK: Not really.

PAULA: [Shaking with fury.] Not really?

CLARK: Well...

PAULA: Look: did you break up with her or did she break up with you?

CLARK: I don't know how to put it really

PAULA: How about she dumped you?

CLARK: Yeah! That's it exactly!

PAULA: Terrific. Just terrific.

CLARK: What-I don't understand!

PAULA: [Starts to sob.] How am I supposed to feel here? You're still carrying this torch, for Christ's sake

CLARK: No, no, no

PAULA: I hate feeling like second best. Like if she had wanted you, you'd still be with her instead of me. I mean, THIS IS ALL I NEED!

CLARK: Listen, please, don't worry about that, really-I was dying to break up with her myself, I mean... her rates were going through the roof!

PAULA: Her rates?

CLARK: [Nods.] She was my therapist.

PAULA: You had sex with your therapist?

CLARK: Well sure. I mean, eventually you run out of things to say, right?

PAULA: [Turning indignantly away.] I'm certain I don't know.

CLARK: [Trying to recover.] Oh, oh of course not, how could you? Because the truth is, you're really not like her at all-you're... you're much prettier and... you never look at your watch, and you're really special! I promise!

PAULA: [Mollified.] And when you first saw me, you got the jolt?

CLARK: Oh yeah, I got that. I'm still getting it. {Beat, moves in closer.] Hi, I'm Clark.

PAULA: That's your name? Clark? I LOVE IT - "Clark." I never met a Clark before. That's so wild. [Sips.] "Clark." I love saying it: "Clark, Clark." It's like wearing dentures in a beautiful kind of way. "Clark." I could just go on saying it all day. "Clark, Clark, Clark, Clark, Clark, Clark-"

CLARK: Yeah, you've really got it down-but listen, can I be frank with you for a second?

PAULA: Oh God, I was so enjoying you as Clark

CLARK: No, no I mean about the coffee-you... you've got to give it up.

PAULA: [Wide-eyed.} I do? [He nods, she makes a decision.} Alright. [She throws cup over her shoulder.}

CLARK: [Shakes his fist in victory.] Now that's what it's all about-sacrifice!

PAULA: [Intensely.] Yes! Are you Jewish?

CLARK: Now you ask? No. Are you?

PAULA: [Haughty.} As a matter of fact, I am. And a pretty committed one at that.

CLARK: [Happy.} Oh! How committed are you?

PAULA: Well, I'm so committed that I would never marry out of the faith.

CLARK: [Deeply disappointed.} Really? That's too bad.

PAULA: Alright look. Maybe I would. I'm not a fanatic, you know.

CLARK: Good for you!

PAULA: Oh Clark, wouldn't it be great if we could just skip all the formalities and automatically be living in the same apartment, really committed to making it work?

CLARK: Yes, but you never told me your name.

PAULA: Guess.

CLARK: Hmm. I like it. It's different.

PAULA: No, I mean guess my name.

CLARK: Oh okay. [Thinks hard.] Debbie?

PAULA: Right!

CLARK: Really? That's right? I can't believe I guessed it on the first guess, that's amazing! But I knew it, you know? [She nods.} You look like a Debbie, I just knew you had to be a Debbie.

PAULA: That's funny because I'm not. I was just testing you. My name's Paula.

CLARK: Wow. You're a very complicated person, aren't you Paula?

PAULA: Stop it! I'm so mad at myself. I mean this is how I destroy all of my relationships-why? Why do I have to protect myself at your expense, Ken?

CLARK: Clark.

PAULA: Exactly! Why am I so terrified of committment, you know? I mean, why can't I just let my hair down with you and love you, my God, body and soul?

CLARK: [Thinks.} You're asking some good questions. Okay, look: I sell health club memberships at the Paris. That's what I do.

PAULA: Oh.

CLARK: That turned you off.

PAULA: Oh, now you're going to say we Jewish girls only care about money and success, aren't you? It's just like my mother warned, that's always what it comes down to in the end, isn't it? Oh Clark, tell me all of your faults.

CLARK: Why?

PAULA: So I can feel superior to you.

CLARK: [Angry.} Is that really what you want?

PAULA: More than anything, [They laugh.}

CLARK: Our first fight! It was inevitable!

PAULA: I enjoyed it!

CLARK: [He moves in close.] It brought us closer together.

PAULA: [She moves back.] You have something in your nose.

CLARK: [Shaking his finger at her.] Unh uh uh, you're trying to distance yourself-you're not being who you are, Paula.

PAULA: Clark! New Yark is so scary! Here we are, intimate as two poppyseeds and you might be plotting my murder as we speak.

CLARK: Believe me, that's not what I'm plotting.

PAULA: Then tell me.

CLARK: I've been fantasizing about you in this soft, billowing white gown.

PAULA: [Worried.] A hospital gown?

CLARK: No, it's a... a wedding gown.

PAULA: Oh, Clarky, yes! Go on.

CLARK: That's as far as I got.

PAULA: Oh well please try not to do that anymore, it really hurts my feelings. [pouting.] I mean, here we are on the threshhold of marriage and Clark, wait! Are you circumicized?

CLARK: (Embarrassed smile.] Well...

PAULA: [Horrified.] You mean you still have your foreskin?!

CLARK: Not with me.

PAULA: Then convert! Convert for me!

CLARK: Wow. That's a big step.

PAULA: Then do it for the baby.

CLARK: The baby?

PAULA: I'm pregnant.

CLARK: [Whispers.] Really?

PAULA: [Also whispers.] In the fantasy.

CLARK: [Whispers.] Is it my child?

PAULA: [Indignant, loud.] Of course, my God, what do you think I am?

CLARK: Look. I'm not good with children. You might as well know that.

PAULA: I don't believe you. How do you know?

CLARK: [Angry.] I just know, Paula, I don't want to discuss it!

PAULA: Hey! I think this merits a little conversation, don't you? I mean it's not some insignificant, little matter you just brought up, Clark, you dropped a bombshell on me-I think I have a right to know!

CLARK: O.K., O.K., O.K., O.K.. I'm not good at hiding things. Ten years of therapy, seven days a week, including holidays, has destroyed my capacity to hide things. I can't hide it from you. It seems I can't hide anything from you. I'm sterile, Paula. I'm half a man. Not even. Three sevenths.

PAULA: Oh my God, Clark. I'm shocked. I'm so sorry. I didn't mean to

CLARK: [A pressure cooker.] To what? To get turned off? To look at me differently? To stop loving me? Is that what you're trying to say? Then just say it. Let's not play games. Let's not beat around the bush. Let's not NOT tell it like it is, Paula, shall we not? You just lost your jolt, now didn't you? Didn't you? [He leans close to her face.] DIDN'T YOU? [He pulls back with a disgusted meer.]

PAULA: [Quickly covers her mouth.] Is my breath bad?

CLARK: [Also covers his.) Why? Is mine?

PAULA: [Shaking her head, sympathetically.] Listen, I'm sorry about your... impotency.

CLARK: [Shouts.] I'm not impotent, I'm sterile! [Deeply morose.] And I'm not really sterile... I was just kidding.

PAULA: [Reaches out to him.] Oh Clark

CLARK: [Grabs her hand.] Oh Paula! Most people are so bitter-but not me, I can't be. I sit here listening to so many sob stories, I can't help but feel my life is better than it really is. Much better. [Beat.] God! I wish it was half that good. [Beat.] Because it stinks, my life stinks! Oh, it's not so bad, it's really

PAULA: -I know how you feel. My husband treats alot of people like you.

CLARK: Your husband?! You're married?

PAULA: To a doctor!

CLARK: My God... well... good for you.

PAULA: What's so good about it?

CLARK: If you're happy then it's good. It's great

PAULA: Do I seem happy?

CLARK: I've discovered that people are not always what they seem. For instance, you seemed single.

PAULA: Now what does that mean?

CLARK: Why did you go on and on about what I thought of your looks if you're married?

PAULA: I still treasure your opinion, Clark. You're a very important person in my life.

CLARK: Why did you let me go on and on about our marriage? Why did you tell me you were pregnant with our child?

PAULA: I was making small talk.

CLARK: My God, I thought... I thought... I feel used. I feel foolish.

PAULA: I feel bad, I feel rotten.

CLARK: Do you?

PAULA: Not really. I feel powerful, I feel sexy. I feel like I got you to love me so fast.

CLARK: [Notices her hand.]-hey! If you're married, where's your ring?!

PAULA: I'm not married.

CLARK: Oh thank God!

PAULA: I only said that because I thought it would be less painful for you than being rejected for your sterility.

CLARK: Paula, I lied.

PAULA: [Hopeful.] You mean... you're really not sterile?

CLARK: No I lied when I said I was kidding. I am sterile. THAT'S RIGHT, ALRIGHT?- I'M STERILE! I'M STERILE, I'M STERILE, I'M STERILE!

PAULA: (Tries to quiet CLARK) Well don't brag about it. Look: I need children. I can't live my life with a man who... [Warming to him.]... but then I look into your dilated pupils and I think... he deserves more.

CLARK: SO then maybe you could live with a sterile man?

PAULA: No. [She hangs her head.]

CLARK: [In agony.] My God, my God, I feel like I'm seeing you for the first time.

PAULA: And what do you see?

CLARK: I see that your nose is big

PAULA: Clark! [She rises, he rises with her.]

CLARK: -and you're overweight

PAULA: [Big gasp.]

CLARK: There she is so high and mighty downing the sugar from her muffin and the fat from her cheesecake and the cholesterol from her butter my God! I thought I had problems, but I'm a model of health compared to you!

PAULA: [Indignant.] Name somebody who isn't.

CLARK: And to think... I thought...

PAULA: It was just the jolt.

CLARK: [Bangs fist on table.] NO! I thought it was MORE than the jolt! Much more!

PAULA: [Relenting.] Alright, there's that, but still

CLARK: No, no I'll do the but-stilling, lady, because I've learned a lot about myself through you. I've learned that I don't need women who only need children, and I don't need children who only need those kind of women and I don't need Prozac but most of all, Paula, I don't need you!

PAULA: Oh! So you're telling me it's over?

CLARK: [Venomously.] Don't be stupid. We never had anything to begin with.

PAULA: [Goes to him.] Oh Clark, we had some good times, didn't we?

CLARK: [Nods, sits broken-hearted.] It just goes to show you. You never know somebody till...

PAULA: Till what?

CLARK: Till after you meet 'em. [He holds his head in his hands.]

PAULA: [Softly, painfully.] 1... I can't believe this is happening to us.

CLARK: [Agonized.] I know. [Beat.] I know.

PAULA: We're like... strangers-[CLARK looks up at her with desperate love.]

CLARK: [Reaching out to her.] Oh Paula

PAULA: [Completely recovered, she turns to man with newspaper.] Excuse me, are you reading that paper?

CLARK: [To PAULA, shocked.] What are you doing?

PAULA: [To MAN.] Yes, I was wondering if

CLARK: [Approaches.] What are you trying to pull here?

PAULA: [Through clenched teeth.] Do you mind? [To MAN.] I was won dering –

CLARK: You're acting like you don't even know me.

PAULA: [To MAN.]-ifI might borrow a section of

CLARK: [Incredulous.] In front of me? You do this right in front of me?

PAULA: [Hisses to CLARK] I'm trying to get on with my life! [To MAN, adorably.] Could you please pass the salt?

CLARK: [Muttering to himself] That's the same way we-[To MAN.] Don't do it, man, don't do it! She'll take your heart and

PAULA: [To CLARK, furious.] STAY OUT OF MY LIFE!
```

---

## IC-0747: The Day I Swapped My Dad for Two Goldfish

- Title: The Day I Swapped My Dad for Two Goldfish
- Author (byline): Neil Gaiman
- Work: Not specified
- Publisher: HarperCollins
- Publication date as stated: May 1997
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BOY, NATHAN, SISTER, MOTHER, VASHTI, BLINKY, PATTI, DAD
- Teaser before the introduction: Yes
- Spoken words (computed): 1438
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Gaiman
ISBN: 978-0060587017
Publisher: HarperCollins
Date (Month/Year): May 1997
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: When a boy swaps his dad for two goldfish, he doesn’t really think about the consequences . . . BOY: (Interrupting) Did so!

ACTOR 1: After all, who would have suspected that other kids would go around swapping stuff too.

BOY: Okay . . . maybe I didn’t think about that!

ACTOR 1: And when his mom finds out . . .

BOY: Who knew he’d be that valuable anyway??

TOGETHER: The Day I Swapped My Dad for Two Goldfish by Neil Gaiman
```

### Performance text (classify this)

```text
Suggested Roles Actor 1: Speaker Actor 2: Everyone else

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

BOY: One day my mom went out and left me at home with just my little sister and my dad. My dad sat in front of the television, reading his newspaper. My dad doesn’t pay much attention to anything, when he’s reading his newspaper. My little sister and I played in the garden. My sister played with her Barbie dolls, and I played at putting mud down my sister’s neck. My friend Nathan came over to my house. He had a glass bowl with him. There was something in the glass bowl. (to Nathan) “What’s that?”

NATHAN: Two goldfish. They are called Sawney and Beaney. Aren’t they neat?

BOY: They were pretty neat. (to Nathan) I’ll swap you them.

NATHAN: What for?

BOY: We went up to my bedroom. My little sister tagged along. I showed Nathan my old transformer robots and my baseball cards and my books. I showed him my old punching bag and my penny whistle that Mommy said made her head ache when I blew it. I showed him my old spaceship that didn’t float in the bath anymore, and the puppet with the tangled strings, and I even shoed him Clownie, my clown that I sleep with. And every time I showed him something, Nathan said, “No.” We went downstairs. (to Nathan) Isn’t there anything you would swap for the goldfish? (to audience) They were very nice goldfish. They were reddy-gold, and they swam backwards and forwards in their bowl.

NATHAN: No, not transformer robots or baseball cards or books or a punching bag., or a penny whistle, even if it does make your mom’s head ache, or a spaceship or a puppet or even that old Clownie.

BOY: I thought for a bit. Some people have great ideas maybe once or twice in their life, and then they discover electricity or fire or outer space or something. I mean, the kind of brilliant ideas that change the whole world. Some people never have them at all. I get them two or three times a week. (to Nathan) I’ll swap you my dad.

SISTER: Oh-oh!

NATHAN: That’s not a fair swap. I’ve got two goldfish and you’ve only got one dad.

BOY: He’s bigger than your goldfish, though. He’s as big as a hundred goldfish.

NATHAN: Can he swim?

BOY: Better than a goldfish.

SISTER: Liar. He splashes and splashes at the swimming pool.

NATHAN: Okay.

BOY: He gave me the two goldfish in the goldfish bowl, and took my dad away with him. I watched the goldfish for a while.

SISTER: You’ll get into big trouble when Mommy gets home. You’ll see.

BOY: When my mother came home I said . . . Mom, can we buy some gold fish food?

MOTHER: If we have to, dear. Where’s your father?

BOY: (to mother) Come and see my goldfish. Aren’t they pretty? (to audience) She shouted up the stairs. She knocked on the door of the bathroom. She called out into the garden. My father didn’t reply.

SISTER: Mumf, mumf, mumf!

BOY: (to mother) Don’t pay any attention to her. Come and look at my goldfish. (to audience) But my mother untied my little sister and took the sock out of her mouth.

MOTHER: Do you know where your father is?

SISTER: (pointing at the speaker) He swapped him to his friend Nathan for those two goldfish.

MOTHER: (sharply) Young man, is this true?

BOY: (to audience) She only calls me young man if she’s very, very mad. (to mother) Yes.

MOTHER: Right. (picking up the bowl of goldfish and handing it to speaker) You can take these goldfish over to Nathan this minute, and don’t you come back without your father.

SISTER: I told you so!

MOTHER: And you can go with him. Fancy allowing your brother to swap your father for two goldfish and a bowl. The very idea.

BOY: So we went to Nathan’s house. He only lives over the road. I knocked on the door. Nathan’s mother came out. (to Nathan’s mother) Is Nathan here?

N’s MOM: Where did you get those goldfish?They were a present to Nathan from his Aunt Violet.

BOY: I swapped them. And now I have to swap them back again. (to audience) She sent Nathan out to talk to me. (to Nathan) Here are your gold fish. Now can I have my dad back, please?

NATHAN: Well, yes and no.

SISTER: Oh-oh!

BOY: We went upstairs to Nathan’s bedroom. It was even messier than my bedroom. Nathan had an electric guitar, a big white one.

NATHAN: I swapped this electric guitar with Vashti Singh.

BOY: Nathan, what did you swap to Vashti, so she would give you her electric guitar?”

NATHAN: If you get off me, I will tell you . . . I swapped her your dad. Well, he wasn’t very exciting. All he did was read the paper.

BOY: I took the guitar and we walked over to Vashti’s house. (to sister) I could be a rock and roll star!

SISTER: You could be an idiot.

BOY: I rang Vashti’s doorbell. (to Vashti) I’ve got your guitar for you. (to audience) Vashti giggled. All Vashti’s sisters giggled too. (to Vashti) Can I have my dad back, please? (to audience) They giggled again.

VASHTI: (shrugging her shoulders) Wait here.

BOY: She took the guitar away from me. When she came back she was carrying a gorilla mask.

(to Vashti) Oh, no.

VASHTI: I swapped your dad with Blinky. Blinky had this really good gorilla mask “

BOY: Where’s Blinky’s house?” (to audience) She told me how to get there. It was going to be a long walk. We set off.

SISTER: Can I put on the gorilla mask?

BOY: She put on the gorilla mask. (to sister - laughing) When are you going to put it on? When are you going to put on the gorilla mask? (to audience) My little sister took off the gorilla mask. We walked some more. I put on the gorilla mask. My sister went over to a policeman.

SISTER: Help! Quick! That gorilla is escaping from the zoo!

BOY: The policeman ran over and caught me. He made me take off the mask. Then he told me off. He would have told my sister off, only she did her innocent little girl face so he didn’t. It’s not fair. (sister giggles) (to sister) Watch it. Just watch it that’s all. (to audience) Blinky had a very big house. We went up to the front and rang the bell. The butler came out. (to butler) Can we speak to Blinky? (to audience) Blinky came down the big stairs. He looked very pleased to see the gorilla mask.

BLINKY: Are you bringing it back?

BOY: Yes, we are. (to audience) Blinky made the butler give us ginger beer. I liked it even though the bubbles tickled my nose. My sister made a face. (to Blinky after drinking the ginger beer) Now, where’s my dad? (to audience) He went away again around the side of the house.

BLINKY: (returning) This is Galveston.

BOY: Galveston was a fat white rabbit with one black ear.

BLINKY: Galveston’s what I swapped your father for.

BOY: I gave him the gorilla mask. He gave me Galveston and a map he drew of how to get to Patti’s house. I’d never walked so far in my whole life.

SISTER: I think ginger beer is the most horrible thing in the whole world.

BOY: Worse than boiled beets?

SISTER: No, not that bad.

BOY: While we walked, Galveston the Rabbit sat in my arms and made its nose go woffly. My sister tried to make her nose go as woffly as Galveston’s, but she couldn’t do it. I knocked on the door of Patti’s house.

PATTI: Galveston!

BOY: [She] took the rabbit away from us and fussed over it and gave it some lettuce, [then she] took my hand. We walked into the back garden. There was a little rabbit hutch there and next to the rabbit hutch was a little run with chicken wire all around it. My dad sat on the grass, in the chicken wire run reading his newspaper and eating a carrot. He looked a bit lonely, and he had grass all over his trousers. (to Dad – opening the gate) Come on, Dad. (to audience) My dad crawled through the gate on his hands and knees.

PATTI: He’s not a very good rabbit.

BOY: He’s not meant to be. He’s a very good daddy.

PATTI: He can keep the carrot. Thanks for bringing back Galveston.

BOY: No problem. Seeya.

SISTER: You like her. I can tell. I’m going to tell everyone at school.

BOY: Last week my little sister told everyone at school that I was adopted. The week before she told everyone at school that I was a space alien pretending to be me.

SISTER: If you do, I’ll tell everyone that you’re secretly fat.

DAD: Children.

BOY: And he carried on eating his carrot and reading his paper until we go home. When we got home my mother said things like, “Just look at the state of him!” and she made him go and have a bath and she put all his clothes into the washing. While Dad was in the bath, my mother told me off. And when she’d finished telling me off, she made me promise, cross my heart, that I would never – ever – swap my dad for anything ever, ever again. And I promised. So I won’t. But I never promised anything about my little sister . . . . .
```

---

## IC-0748: The Days of Wine and Roses

- Title: The Days of Wine and Roses
- Author (byline): J.P. Miller
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: KIRSTEN, JOE
- Teaser before the introduction: Yes
- Spoken words (computed): 1123
- Already set (do not supply): none

### Source block (context only)

```text
Author: J.P. Miller
ISBN: 0822202816
Publisher: Dramatists Play Service
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: In the fast-moving milieu of Madison Avenue, social drinking is almost an occupational necessity, and one that fast-rising young Joe Clay adopts with too ready ease.

ACTOR: Unfortunately the girl he meets and marries shares his proclivity, and while they continue to tell themselves that they drink because they choose to, it is soon apparent that their habit has become a serious problem.

ACTRESS: But their failure to acknowledge this plunges them headlong into shattering events— a career in shambles, a marriage destroyed, the esteem of friends and family lost, and a child who has become the innocent victim of their obsession.

ACTOR: In this scene the drama begins on their first date in . . . .

TOGETHER: The Days of Wine and Roses by J.P. Miller
```

### Performance text (classify this)

```text
The Characters: Joe Clay (30-40), an alcoholic and Kirsten Arnesen (20's), a young woman attracted to Joe.

The Setting: A walk along the east bank of the Hudson River, 1960's

The Scene: On their first date, Joe and Kirsten walk by the ri ver and share details of their lives. (Joe and Kirsten enter up left. River and city sounds in the background. Kirsten is dreamy. Joe is still full of the day's emotions, but several drinks have helped him to look at things - at least for now - - in a rosier light.)

KIRSTEN: Isn't it beautiful down here? Like another world.

JOE: (Chuckles) To you, maybe. To me it looks like the same world where I made an ass of myself last night.

KIRSTEN: You did, didn't you? But that seems like a long time ago somehow. Joe - - I enjoyed our dinner very much.

JOE: On, me, too. It was great. And no matter what happens to me tomorrow when I go to the office, meeting you has made it all worth it.

KIRSTEN: Thank you. But nothing bad's going to happen. I know Rad Leland. He has no moral principles of his own, but he respects people who do. (They have arrived down left, where there is a short length of rail running left to right. They lean against the rail, facing down. Joe takes a flat pint of amber liquid out of his jacket pocket and offers it to her. She shakes her head. He takes a drink. )

JOE: Are you on the wagon? Or you just don't drink?

KIRSTEN: I just don't drink.

JOE: Not at all?

KIRSTEN: I don't see the point of it.

JOE: It makes you feel good!

KIRSTEN: I already feel good.

JOE: Maybe it'll make you feel better! Oh, I'm not pushing booze, but have you ever tried it?

KIRSTEN: Once.

JOE: Well?

KIRSTEN: Senior prom. Spiked punch. I hung around the punch bowl all night, didn't even dance, fell down, had to be carried to my date's father's car, threw up all over his rented tuxedo and my borrowed prom gown, and the car, inside and out, and had a monster hangover for two days. It was wonderful.

JOE: And you never tried again. A real quitter, huh?

KIRSTEN: I guess so. You drink like this often?

JOE: (Bursts out laughing.) Can't afford it! Oh, I do like to drink, but not to excess, you know. Not often, anyhow. Oh, I tie one on once in a while. Everybody has his little quirk. What do you like?

KIRSTEN: Books. (Pulls book partway out of shoulder bag, drops it back.) And chocolate. (Takes chocolate bar out of bag, breaks off piece, pops it in her mouth.)

JOE: Sugar. If you eat that stuff you probably get sugar highs.

KIRSTEN: (Thinks about it.) Maybe. I never thought about that.

JOE: See? Stick with me, kid. An encyclopedia of trivia.

KIRSTEN: You're funny. I like being here with you. Look- you can see the Prince's yacht. Aren't the lights beautiful? You know what Mr. Trayner told me? Two of the girls stayed with the Prince after the party.

JOE: I guess I oughta be pretty proud, huh? I'm sort of responsible for a menage a trois. (He takes a drink.)

KIRSTEN: Sometimes I wish I could be like those girls. They don't have to be anywhere except where they are. They're like -- I don't know -- hummingbirds. They just stand in the air wherever the nectar is. The world's just one big honeysuckle vine.

JOE: As opposed to one big skunk cabbage, for some people -

KIRSTEN: You know what? It's after midnight, and I feel wonderful!

JOE: (Without conviction) Me, too. (He takes a drink.)

KIRSTEN: (Dreamily) It's funny about the river. If you look close it's filthy. I watch the middle where it's clean. You know what I think? I think I watch the water because I expect a sea monster to come up out of there someday and carry me down to the ocean caves...

(Joe stares at her, then shakes his head at such an incongruous thought. )

JOE: Midnight, huh? Show time. My Mom and Pop are a club act. You know, songs, dances, snappy patter - - old time vaudeville. They're working some loud joint in Vegas right this minute. Show biz baby. Three years old, right out there with 'em. (Does a little soft shoe, singing:) "Me and my shadow..." (Stops suddenly)

KIRSTEN: (Applauds) More! More!

JOE: I retired at seventeen, joined the Navy. Mom and Pop are still at it.

KIRSTEN: Are they good?

JOE: (Shrugs) You know. Oh, they were on TV, couple times.

KIRSTEN: But you didn't like that kind of life.

JOE: I 'wanted something steady, something with a little class. Like this Trayner account - - class.

KIRSTEN: Joe -- don't hate yourself. We all have to do things we don't like. That's part of your job.

JOE: (Explodes) No! It's not! I want to be a public relations man, not a pimp! (Seething, he tries to control his anger.) Classy guy, huh? Meets a beautiful girl, a girl who believes in things in spite of the dirty people all around her, a girl who reads books, and dreams nice dreams. And what does this bum do? He gets half -schnockered and tells her what a tough life he leads.

KIRSTEN: Actually, I'm proud that you confided in me.

JOE: The great lover.

KIRSTEN: And you did me a favor, too.

JOE: I did?

KIRSTEN: I love it down here, but I usually have to come alone.

JOE: Alone? You come down here alone? Kirsten, this place is crawling with all kinds of odd balls! You can't come down here by yourself at night!

KIRSTEN: They walk by me real slow sometimes, and stare, but they never do anything. I don't know why.

JOE: Jesus Christ, Kirsten!

KIRSTEN: I dreamed one time they murdered me in those bushes over there, and my dad drove all the way in from the Island and took my body home in his pickup truck. I could see my body stretched out in the bed of the truck on all the little clods and leaves from all the trees and shrubs he'd been delivering. And all the way home he kept talking to my body. The back window of the cab was broken out, and he talked over his shoulder through that broken window, talked a blue streak all the way home. But I was dead and couldn't answer him. The strange thing is, my father never talks. Oh, he used to talk to my mother. They had a very private love affair. Their favorite toast to each other was "Til samen e himlin." In Norwegian that means "Together in heaven."

JOE: Til samen e himlin.

KIRSTEN: (Corrects his pronunciation.) Til samen e himlin. You've got to get the lilt.

JOE: Til samen e himlin.

KIRSTEN: Together in heaven. They meant it, too. After Mama died, he was more silent than ever, almost as though he'd gone with her. (She suddenly makes an effort to throw off her gloom.) Well, "gather ye rosebuds while ye may, Old Time is still a-flying."

JOE: You get that out of that book?

KIRSTEN: (Pulls book out of shoulder bag.) No, that's Herrick. He's in Go-Ja. (She pronounces it "Gojay".) This is Le-Na ("Lenay"). Dad gave me these for my high school graduation. He said if I read all the way through from Ab-Bu to Ya-Zu I'd have the equivalent of a college education.

JOE: Hey, you're about halfway through your sophomore year, here. (Hands her the book. She drops it in her bag. He lifts his bottle in a toast.) Here's to your BA degree. And after that?

KIRSTEN: My dream, you mean? You won't laugh? I hope to get a real degree someday, and be an English teacher.

JOE: English teacher. Great. You want it, you'll get it. (Flourishes bottle) Here goes the coup de grace. (Drains bottle)

KIRSTEN: Well, it's just about time to get back to the real world.

JOE: (Finally has the glow he's been looking for.) Time does not exist on the river. (He caps the bottle and leans over the rail.) I ought to put a message in this bottle. But what?

KIRSTEN: (She leans over the rail with him as he holds the bottle out and drops it. We hear a splash. They watch it float away, right to left.) "They are not long, the days of wine and roses. Out of a misty dream Our path emerges for awhile, then closes Within a dream."

(They turn away from the rail and walk toward up left. At Center they stop and look at each other. He puts his arm around her, and they continue off left as lights fade to black.)
```

---

## IC-0749: A Death in Bethany

- Title: A Death in Bethany
- Author (byline): Garry Williams
- Work: The Play’s the Thing: Ten-Minute Plays in the Classroom
- Publisher: Systime
- Publication date as stated: 2006
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: HENRY, ROZ
- Teaser before the introduction: Yes
- Spoken words (computed): 1117
- Already set (do not supply): none

### Source block (context only)

```text
Author: Garry Williams
Book: The Play’s the Thing: Ten-Minute Plays in the Classroom
ISBN: 978-8761610003
Publisher: Systime
Date (Month/Year): 2006
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Experiencing the death of a parent is a traumatic experience for anyone.

ACTRESS: For men, though, the death of a father is uniquely and deeply traumatic.

ACTOR: Whether or not a father and son are close in life, they are undeniably connected— and this is acutely evident to a man when his father dies.

ACTRESS: At that moment, a man realizes how much of his identity has been defined by his father.

ACTOR: The powerful emotions and life adjustments that follow Dad’s passing catch most men completely off guard.

ACTRESS: This is true for Henry– he has lost his wife, his children and tonight his father. How he copes is the focus of . . .

TOGETHER: A Death in Bethany by Garry Williams.
```

### Performance text (classify this)

```text
It is night. In the dim light of streetlamps we can see a small living room, cheaply furnished. It is tidy, but very little money went into the place. There is a knocking at the offstage front door. It comes again, louder. Then again, louder.

HENRY: (Offstage) Roz? Roz, open the door A woman of twenty-five or so comes out from the wings – or an onstage door – wrapping a robe tightly around her body. She moves silently toward the front door and stands in the darkness.

HENRY: (Offstage) Roz, I know you’re in there, open the door! (After a beat, roaring) You want me through the picture window?

ROZ: Go away, Henry.

HENRY: (Offstage) Bullshit. I want to see my kids, Roz. I’m not goin’ away till I see my kids. I won’t even wake ‘em up.

ROZ: You’da woke ‘em already if they were here. They’re not here.

HENRY: (Offstage) Bullshit.

ROZ: They’re not, Henry. They’re at my mom’s. Go to a phone booth and call her, She’ll tell you.

HENRY: Yeah, I know what she’d tell me.

(There is a sadness in Henry’s voice; a resignation of sorts that belies the bravado of his words. Consciously or unconsciously, Roz reacts to it.)

ROZ: Go home. Sleep it off, you can see ‘em tomorrow.

HENRY: I wanta see ‘em now!

ROZ: No, Henry. You’re drunk, just go home.

HENRY: I am home. And I’m not drunk. Now, you let me in or I’m comin’ through a window. I mean it, Roz. You know I’ll do it.

ROZ: I’ll call the cops.

HENRY: Weasel and Billy are doin’ nights this month. And they’ll just tell you to let me in.

(There must be truth to this, because she goes to the door and unlocks it. Henry is a young man, mid-twenties, dressed in factory overalls and steel-toed black shoes. He looks around at the darkened living room)

HENRY: You sleepin’?

ROZ: It’s night, isn’t it? Yeah I was sleepin’. How come you’re not at work?

HENRY: I was. You sure the kids aren’t here?

ROZ: If they were here I’d let you see ‘em, okay?

HENRY: Why they at your mom’s?

ROZ: Hank’s been havin’ his nightmares again. He thinks he won’t have ‘em if he’s over there.

HENRY: How often’s he havin’ ‘em?

ROZ: They come and go, like before. (Henry sighs)

HENRY: Damn. Damn. Hey, can we turn on some lights here, or what?

ROZ: Henry, I can’t be staying up talking, okay, I have to work in the morning.

HENRY: (turns on a lamp anyway and slumps on the couch). You got any coffee?

ROZ: I’m not your maid, either.

HENRY: Oh, come on, Roz, gimme a break, willya?

ROZ: You want coffee, you know who can make it for you.

(Henry sags. He puts his face in his hands, then runs them aimlessly through his hair. Then he slumps sideways onto the couch, curling into a loose fetal position.)

HENRY: You still got that blanket in the closet there? The one with the ducks on it?

ROZ: No.

HENRY: Oh, come on, you know you do.

ROZ: You’re not gonna sleep here.

HENRY: I wanta be here when the kids come.

ROZ: In your work clothes on the couch. They’ll think you were drunk.

HENRY: No they won’t.

ROZ: What else would they think?

HENRY: (Sitting up, with emphasis) That I missed them. That I needed to see them. That maybe I’m not such a terrible guy.

ROZ: (A beat) They’ll think you were drunk.

HENRY: (Laying back down) Thanks, Roz. I really needed that.

ROZ: Henry, I’m not kidding, now, get up.

HENRY: You won’t even know I’m here. Just go back to bed. I won’t come in or nothin’, I swear.

ROZ: What’d she do, kick you out?

HENRY: I’m so tired, Roz. I feel like I’m melting somewhere, way down inside.

ROZ: Henry . . .

HENRY: My dad died, Roz.

ROZ: (A whisper) What?

HENRY: Heart attack, they think. Just died, right there at the punch press.

ROZ: Oh, God, Henry.

HENRY: They called me on the loud speaker. Told me to get to section four real quick. I knew it as I ran.

ROZ: I’m so sorry.

HENRY: I never saw a dead person before. I mean, just dead, right there in the real world, you know? I mean, I’ve seen those wax-lookin’ bodies in caskets, but I’ve never seen anyone dead in the real world. And it was my dad. (Roz kneels tentatively beside him. She reaches a hand out and strokes his hair) I think somethin’ melted inside me, Roz. Somethin’ scary and important. I thought it was gonna run all over the floor, like blood or pee or somethin’.

That it was gonna mess my dad up. He was all clean and dead, you know, and somethin’ was gonna come out of me and mess him all up. (Roz keeps stroking his hair, gently and softly as she would a child.) I’ll never ask you for nothin’ else, Roz, if you’ll just let me sleep here and wait for the kids.

ROZ: Henry . . .

HENRY: Please, Roz.

ROZ: (Quietly) Henry. Henry, don’t. Six months ago. You left me six . . . months ago!

(The primal urgency of her voice seems to Henry in place. Struck by the truth of her words Henry breaks away. Then he sits on a coffee table, his back to the audience. Roz walks around and posts herself right in front of him. She lifts his face roughly and locks eyes with him)

ROZ: I’m a real person, Henry. I am a real person. ( Roz hold Henry’s gaze a moment longer, then steps back. Speaks quietly) I’m, um . . . I’m gonna go take a shower. You be okay for a minute? (She starts to go but Henry’s voice stops her)

HENRY: Hank’s nightmares . . . ?

ROZ: Yeah?

HENRY: I’d take ‘em away if I could. I’d take ‘em on myself.

ROZ: I know. (He reaches out and holds a corner of her robe)

HENRY: I came over here to ask if I could come back.

ROZ: I know.

HENRY: Were you gonna let me?

ROZ: No.

HENRY: Because of Monty?

ROZ: No.

HENRY: Because of Alicia?

ROZ: No.

HENRY: Then why?

ROZ: I don’t know. I wanted to hate you and I hadn’t started hating you yet. I figured I deserved a while of that. (He nods. She tries to go but he holds tightly to her robe)

HENRY: My mom gave herself twenty years of it. You figure it’ll take you that long.

ROZ: I don’t know. I’m not your mom.

HENRY: And I’m not my dad. Hell of a way to realize you’re not somebody else, look at ‘em dead on a floor. I just kept lookin’ at him layin’ there, sayin’, “Can’t we do something’? Can’t we do somethin’?” And Al Johnson said, “He don’t need nothin’ now, Henry.” And I thought, he never did need nothin’. You know it, Roz? He never needed nothin’. Not me or Johnny or Mitzi or mom or nothin’. Him dead on the floor was no different than him alive standin’ at that punch press, ‘cause he didn’t need nothin’ either way. (Starting to cry) The son of a bitch has been dead for twenty years. I shoulda known it back then. I shoulda known it when he left home. I spent my whole life tryin’ to be a dead man. A dead man who lived across town. (Now the tears can’t be stopped) Goddammit. Goddammit, I didn’t want to do this.

ROZ: It’s okay.

HENRY: No, it isn’t. I didn’t want to do this. (He stands, wiping madly at the tears, but they keep coming) I just wanted to see the kids. I just wanted to look at ‘em while they were sleepin’. (Pacing now, looking for something) I’ll get out of here in a minute, I just gotta find my jacket.

ROZ: Stay, Henry.

HENRY: Look, I’m gonna get my jacket and get outta here. I’ll see the kids tomorrow.

ROZ: Stay, Henry.

HENRY: Just help me find my jacket.

ROZ: You didn’t have one, honey.

HENRY: (Crying harder) Oh, God, look at me. This shit’s melting inside me and it’s gonna get all over the place. It’s gonna come out and mess everything up.

ROZ: It’s all right.

HENRY: No, it’s not. It’s comin’ out al over the place. Jesus God, let it stay inside me . . . (She goes to him and holds him)

ROZ: We’ll get in the shower, okay? We’ll get in the shower and it can all come out. It can all come out and won’t mess up a thing.

HENRY: I’m scared.

ROZ: I know.

HENRY: I never needed nothin’ before.

ROZ: I know.

HENRY: I don’t know how to do it.

ROZ: Sure you do, Henry. Sure you do. The kids’ll be home tomorrow. The sun’ll come up and the kids’ll be home.
```

---

## IC-0750: Death of Bliss

- Title: Death of Bliss
- Author (byline): Jules Tasca
- Work: The Best American Short Plays 2003-2004
- Publisher: Applause Theatre Books
- Publication date as stated: 2006
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: KAHLID, SANA
- Teaser before the introduction: Yes
- Spoken words (computed): 2336
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jules Tasca
Book: The Best American Short Plays 2003-2004
ISBN: 1557836957
Publisher: Applause Theatre Books
Date(Month/Year): 2006
```

### Introduction (context only: never use it for content warnings)

```text
What brings a young Palestinian man to detonate himself amidst a crowd of unsuspecting citizens? Is it a religious upbringing with promises of paradise in reward for acts of martyrdom? Is it the parental and family support he receives for his convictions? Is it brainwashing, or rather encouragement from a Palestinian society with no other means of fighting back against oppression and humiliation? Regardless of the motivation for this type of self-sacrificing terrorism, the results are the same: loss of life, increase in fear and The Death of Bliss by Jules Tasca..
```

### Performance text (classify this)

```text
[Lights come up on KAHLID: Akka, a young Palestinian man. KAHLID: paces. He looks at his watch.]

KAHLID: [To himself] Why isn't she home? Sana Sana... Sana...where are you? [He looks at his watch. He paces some more.] Where could she have gone? [Khalid lifts a coat from a chair. There is a vest under the coat. The vest is packed with explosives and held together with duct tape. He puts on the vest and looks in the mirror. He is proud of what he sees.] Praise the name of Khalid Akka! Yes...yes...God is great. [He removes the vest-bomb and replaces it on the chair. He steps back and regards it. He hears footsteps. Quickly, he covers the vest-bomb with his coat. His wife, Sana, a young Palestinian woman, enters. She wears a head scarf and carries a small knapsack.] Sana, where have you been?!

SANA: What's the matter?

KAHLID: What's the matter? I am waiting for you.

SANA: I had an errand to run.

KAHLID: Errand?

SANA: Yes, an errand. So? Usually, you spend your lunch hour with the men drinking tea and smoking and going on and on about the Jews.

KAHLID: Going on and on about the Jews...

SANA: Well, you do.

KAHLID: Is that how you see me, your husband? As some kind of kiosk attendant who fills his free time with empty talk, going on and on about the Jews?

SANA: I didn't say...

KAHLID: You said on and on...on and on about the Jews...as though your husband is nothing but a tea shop talker.

SANA: It's not just you. Khalid, I didn't mean just you.

KAHLID: You meant what then?

SANA: It's all of us. Who talks of anything but them? That's our lives now. The Jews and what they do to us.

KAHLID: The Jews are our oppressors. The Jews are our occupiers. The Jews stole our land. The Jews give us pain. People...people talk about what pains them, Sana.

SANA: I know.

KAHLID: So until the Jews are gone, there will be no other topic but the Jews! Understood? [A beat of silence.]

SANA: Khalid, I'm tired. I don't feel so good. I don't want to talk about the Jews right now.

KAHLID: Sana, you have to talk about them now.

SANA: Right now? Why?

KAHLID: Because... because Jews are an infection in the land of Palestine. You fight an infection before it kills everyone.

SANA: I've heard it all before. Why at this moment.. .Will you stop pacing back and forth.

KAHLID: Sana...

SANA: What?

KAHLID: My brother...he...he...

SANA: Your brother what?

KAHLID: He came to me at the kiosk today. Then we came here.

SANA: Your brother, Ibrahim, he was here today?

KAHLID: Yes and he...he...

SANA: Khalid, what?

KAHLID: Sana, I am being honored.

SANA: You are being...

KAHLID: Honored. Yes, I am.

SANA: What're you talking about? [A beat of silence. Khalid looks at her] Khalid, what honor?. .Husband?

KAHLID: He, Ibrahim, he dropped off the vest.

SANA: The vest... you mean.. . Khalid, you mean one of those vests that. ..

KAHLID: Yes.

SANA: A bomb?

KAHLID: Yes.

SANA: No... [Khalid crosses and removes the coat from the chair, revealing the vest-bomb. Sana slowly crosses to it.]

KAHLID: Don't touch it.

SANA: You...you know about these...these vests.

KAHLID: They trained me and Ibrahim both. Showed us how to.. .how to detonate it.

SANA: When did you...

KAHLID: We took training.

SANA: Secretly.

KAHLID: Secretly. Yes. Sure. From the authority. Yes, I did. See there are two metal pieces here in the pocket covered with tape. Once you remove the tape from each strip of metal, you.. .you touch the strips together and...

SANA: And you are dead.. .you don't need much training to be dead.

KAHLID: It is an honor to be selected.

SANA: I didn't...

KAHLID: You didn't what, Sana?

SANA: Know. I didn't know that...

KAHLID: That I had placed the name of Khalid Akka on the list of those willing. No, you didn't know. I couldn't tell.

SANA: Couldn't tell me? Couldn't tell your own wife that you took training.

KAHLID: I told no one. The handlers told us to tell no one. There are those among us who for Israeli money would turn us in.

SANA: And Ibrahim, his name is on the list too?

KAHLID: Sure.

SANA: Why then you?

KAHLID: The authority chooses...

SANA: Why you and not Ibrahim?

KAHLID: I think...I think because... because I work the kiosk at the Grand Market, no one would suspect me. It'll be crowded tonight, because of the start of the Jewish holiday and I...

SANA: And you're going back to work with this vest under your coat to... to...

KAHLID: My loving wife...I knew this would be hard for us.

SANA: But your loving wife has nothing to say about it.

KAHLID: Why would a wife or mother or any woman have a right to keep me from...from...from meting out punishment to the infidels?

SANA: No. How could any woman keep you from such an honor.

KAHLID: It is an honor, a high honor.

SANA: Khalid, we stand in our apartment and we talk of your death as if you were going out for cigarettes.

KAHLID: No. I...I am on edge. My palms are wet. My nerves are all out of their pockets. But.. .you.. .you are supposed to hold your head up high, my loving wife. There is... underneath the tension. .. there is a pride...

SANA: Pride.

KAHLID: Don't you feel it?

SANA: I'm to be proud also?

KAHLID: You're not? You're not proud?

SANA: I am just...just shocked...

KAHLID: I know.

SANA: You took training...you're serious...

KAHLID: I think we must battle the occupation. That fight is the marrow in these bones.

SANA: I just feel numb.. .numbness.. .

KAHLID: My wife, you must understand. My brother told me-no promised me, vowed to me-that you would be taken care of. You will stay in the apartment. You will receive money regularly. You will be celebrated as the wife...

SANA: Who lost her husband.

KAHLID: As the wife of a martyr. Thousands will march through the streets for my funeral. Our men will carry my coffin draped with the flag. The shots they fire in salute of me shall be my voice from the grave...and you... Sana...will march with me and wear my honor like a queen's crown.

SANA: Khalid.. . Khalid.. .how full the pride that overflows those eyes, eyes more precious to me than all the martyrs in heaven.

KAHLID: Sana...

SANA: You can strike me if you will, but no, I will not lie to you. I do not respect this anymore.

KAHLID: Wife...

SANA: For the Jews we are destroying ourselves. For the Jews we rupture our families. In my bones there is only sorrow.

KAHLID: You dishonor your own brother by saying this. Your brother, Hanni, honored your family by...

SANA: Driving a car of explosives into a restaurant. Don't let me remember. My Hanni...

KAHLID: He killed eight Jews and injured over twenty more.

SANA: And killed three Palestinians on the wait staff. Our hate bites its own tail.

KAHLID: It's a war of sacrifice.

SANA: I know. I grew up without a brother.

KAHLID: He was a warrior, the same as Ibrahim and I are. Oh, Sana, I know that life is bliss, but it is the bliss of a moment. After such a sacrifice is the bliss of forever. The bliss of God. Your brother, Hanni, is with Allah. He is a hero. I always wanted to live up to your brother's name.

SANA: When Hanni died it was the death of bliss for me. And now...now...husband, how can a wife be happy?

KAHLID: It is not a time to be happy. It is a time to be strong. I..I will miss you too. So much. But look, I go to God and His paradise.

SANA: And so you do. You go to God and I, your wife, go to the funeral.

KAHLID: Sana.. . Sana, I...I never thought you'd have this attitude.

SANA: How could you? How could I? We don't know the burn until the lightning hits.

KAHLID: We're at war. These are the acts of war. We're all soldiers, all of us, all of our people. I'm just waiting for you to say something that makes me know you understand...Wife? Sana? I...I thought...I mean to say, I saw this time as us holding each other as tight as love can grip two people and I thought...

SANA: I don't feel that way. I'm sorry.

KAHLID: This stance you've taken...

SANA: What stance?

KAHLID: This wall you're putting up. One could interpret this as being against the uprising.

SANA: We live the uprising. We breathe the uprising. Today I'm breathing uprising instead of air. It's choking me that you. . . that you...

KAHLID: You would talk me out of it. ..

SANA: I love you. In the eye of the uprising I love you.

KAHLID: I know you do. And 1...1 am...I am afraid, Sana. I am. But my...my duty to my country...

SANA: What about your duty to the living. Your...your family...your...

KAHLID: My mother knows. I stopped there already. Oh, yes, she was upset, but Ibrahim and I soothed her with the pride that will come after...

SANA: Pride. What are we to do with this pride. How can we love pride more than life? [Khalid crosses to the chair holding the vest.]

KAHLID: I have no more time for women's hysterics. I am leaving. Say something to me, Sana. Say something to me that will last me forever.. . Sana?

SANA: I am going to have a child. [A beat of silence. He crosses from the chair to Sana]

KAHLID: Are you saying this because...

SANA: I am going to have a child.

KAHLID: Sweet heaven...oh, Sana...you are... [He embraces her]

SANA: Yes... I was at the clinic this morning.

KAHLID: You were at...

SANA: Yes, the clinic. That's why I was late.

KAHLID: And the doctor confirms that...

SANA: Yes. Two months.

KAHLID: Pregnant...

SANA: I am two months...

KAHLID: Two months along. Oh, my Sana...oh, my dear wife...

SANA: I came home today to tell you of this honor. [Sana moves away from him.] But now there is...there is an ache in my stomach. Today, when the doctor told me, in my womb I felt a beautiful sensation, a tingle of joy. Now.. .now, there is discomfort there...a gnawing, as if what's inside me recoils with a little startle of grief...

KAHLID: Now, after almost two years.. .now. ..now you become...

SANA: If I...If I had known...Oh God if only I had known...

KAHLID: There was no way to know that I would be selected.

SANA: No. No. I know that. But surely now you...you can...

KAHLID: I can what?

SANA: You can...you can call Ibrahim. You can call your brother and you.. .

KAHLID: I can do what? Call it off? Back out?

SANA: You must...

KAHLID: How? How can I call it off? The leadership. They're expecting the Grand Market of Jerusalem to be a windstorm of shrapnel. They expect Jewish flesh and oppressors' mouths to foam blood. They expect the air as thick as cream with their cries and moans...

SANA: And what about your own flesh, husband?

KAHLID: It doesn't matter. I swore during training by Almighty God who holds the heavens above our heads, Sana, that the Jews will never live secure until they leave the land of Mohammed.

SANA: And what about this child who sits here in the limbo of life and waits for the world to pull him out? [A beat of silence. Khalid stares at her. Then he crosses away.]

KAHLID: I...I...I never...I never counted on such a thing. You-my wife. I made Ibrahim promise to Allah that you would be taken care of. But I never counted on.. .on...

SANA: You know what it would be like, Khalid, for a child to call you father? Do you know how it will feel to have him or her run to the door when you come home? To have a bouquet of kisses flood your face? And there would be more pride in that than having your picture in your mother's front window dressed in carna-tions and draped with a flag dripping with honor.

KAHLID: Oh, my Sana, how much I love you. Your words are still electric to me. Sana... Sana, love of my life, you are trying to change the world with your love of me.

SANA: I won't say I'm sorry if...if what I say changes your mind.

KAHLID: But it's not so simple. Women. Wake up. Everything's so easy for women.

SANA: Only men say that.

KAHLID: Sana, it's not possible for me to...

SANA: Why not? Call Ibrahim. Tell him what happened.

KAHLID: Sweet woman...

SANA: Please.. .If you love me... please... [Sana crosses to the table and picks up a cell phone. She crosses back to Khalid with it. She hands it to him.] Please.. . [Khalid sits.]

KAHLID: I...I will be called a coward. Sana, the leadership doesn't care about your baby.

SANA: Our baby.

KAHLID: That baby.. .my son... will be told of this if I back out. You know how a reputation gotten is a brand forever here. Khalid Akka, they'll say, he was chosen to sacrifice for his people, for Palestine, for our children's future and he.. .he...

SANA: We can go away.

KAHLID: [Rising.] They'd still all know. My family, my friends. My brother and mother disgraced. Wherever we went, we'd trail my wobbly reputation behind me.

SANA: I want my husband with me. If that makes me a traitor so be it.

KAHLID: Don't say that. Ever...you are not a traitor. You are the wife of Khalid Akka. My son will never be disgraced by his father. I...I...I leave to you and him a legacy of honor... [Khalid embraces her. Then he crosses to the chair and puts on the vest, next his coat to mask the vest. Sana stares away. Khalid crosses back to her.] Sana...I love you... Sana...But I must. It is impossible to do otherwise...God is great. He has seen fit to leave me alive in you... [Khalid kneels and kisses Sana’s stomach.] God is great, Sana... Sana . . .

SANA: [Softly.] God.. .is.. .great... [Khalid rises and kisses her.]

KAHLID: Pray for me... [Khalid exits.]

SANA: [As lights fade.] I pray...I pray...I pray that-boy or girl-I pray that I lose it...I pray that I never have it...!...I pray...I pray...I pray...
```

---

## IC-0751: Deus-X

- Title: Deus-X
- Author (byline): Jules Tasca
- Work: The Best American Short Plays 1998-1999
- Publisher: Applause Theatre Books
- Publication date as stated: May 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: FANNY, ALBERT, MALE VOICE, FEMALE VOICE, WILD MAN, ALBERT AS GERALD
- Teaser before the introduction: Yes
- Spoken words (computed): 1823
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jules Tasca
Book: The Best American Short Plays 1998-1999
ISBN: 1557834253
Publisher: Applause Theatre Books
Date(Month/Year): May 2001
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Why are some people extremely religious, others are “luke-warm” or “born-again” believers and still others fall into the categories of agnostic, atheist, or religious fanatic?

ACTOR: Wars are fought, people die in the battle over religious superiority. Muslims, Jews, Christians . . . . In the name of God . . . . when will it end?

ACTRESS: Or where does it start? Is belief in God a learned personality trait, or are we somehow genetically predisposed to our faith. Do we inherit it like we inherit our risk of diabetes or cancer?

ACTOR: And if so . . . the scientific mind asks . . . can religiosity be treated, be cured, even . . . . . eliminated? No wars, no terrorist bombings, no radiation, no chemotherapy . . . perhaps just a simple pill. . . A pill called Deus-X by Jules Tasca.
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Lights come up on FANNY MAE SPIELER, a conservatively dressed woman. She addresses the audience.

FANNY: I've come here today to the laboratory of my brother-in-law, Doctor Albert Spieler, in order to save my marriage. [ALBERT SPIELER, a man in a lab coat, appears.] This man, this tool of all that is evil in the world, has ruined my marriage...

ALBERT: At least let me tell my own side, Fanny Mae. Fanny Mae is married to my brother.

FANNY: The Reverend Gerald Spieler...

ALBERT: Gerry... my brother and I were brought up in the same home. We had the same upbringing. [ALBERT mimics his parents]

MALE VOICE: One more report card from school like this and I'm gonna take my strap off!

FEMALE VOICE: No more giggling in there, Albert! Gerry! It's 11 o'clock.

MALE VOICE: Put that dog out or I'll put you out!

FEMALE VOICE: I don't care if you do hate his guts. He's your brother, so shake hands!

ALBERT: You get the idea. It was a typical American family. Gerry and I were both loved and beaten equally. The mystery is how Gerry grew up to be ...The Reverend Gerald Spieler, Jesus' four-star general here on earth. . .

FANNY: An evangelist to all mankind.

ALBERT: And I, Albert Spieler, grew up to be ...

FANNY: A little liberal, atheistic, materialistic, anti-Christ, medical doctor!

ALBERT: It astounded me that I went off to college to become a scientist and Gerry...

FANNY: Graduated with honors from the Midwest Theological Seminary in Nebraska.

ALBERT: Then he started a church...And married adorable her, a minister's daughter.

FANNY: What a team we made. Gerald went on to become the leading Televangelist in America. "Jesus', General" the program was called. We were seen in all 50 states and were ready to go world wide until. . .

ALBERT: I began this special research. Why, I thought, do some people become so ensconced in religion, while in others, religion simply, as in the case of vaccination, does not take. Regardless of how bombarded I was with religious teaching - from Noah's ark to Lazarus' double dip at living - I could never regard religion as anything more than bunkum and scarum and hocum. But my brother...

FANNY: Gerald actually spoke with Jesus! Why, Gerald and Jesus were like Mutt and Jeff.

ALBERT: While Gerry took production meetings with Jesus, I studied over 100 families where some of the members of a family were religious, but had brothers or sisters who were not. Ergo, I postulated a theory that, since no environmental factors could account for religion taking in one sibling and not taking in another, there must be some biochemical entity in the brain stem that is different in the religious and the non-religious. It took years of dissection and investigatory surgery. I autopsied over 300 brains whose histories I could verify. I knew which brains were religious and which were not. What I found was this. [He pulls down a medical chart of the brain.]

FANNY: It is disgusting to show something like this in public!

ALBERT: There is a heretofore undiscovered gland the size of a pinhead under the hypothalamus here. In those who are bound by religion, it is visible to the human eye. In those who go to church on high holidays, or, say, only for funerals or a feel-good Christmas experience, it is visible with magnification. In the non-religious, the gland is almost non-existent.

FANNY: Who would believe this?! God is not a gland! He is the Lord!

ALBERT: Everybody said... But I worked with several other leading brain surgeons who corroborated my findings. More years of study and research and I discovered a powerful drug that would shrink this Deus or God gland, as I did so call it. [He holds up a small red pill.] I call the drug... Deus-X.

FANNY: Oh, it's wrong. It is so wrong.

ALBERT: Deus-X is a substance that eliminates the small pin-head gland that makes one's emotions susceptible to religiosity. It impedes the bio-chemicals that make the gland thrive. With Deus-X, the gland just withers away and drops off. One dose. One hundred milligrams. That's all it takes.

FANNY: Moral castration! That's what it is, moral castration.

ALBERT: Fanny thinks I developed Deus-X because I hated what my brother Gerry became.

FANNY: Why was one of the first human tests done on a death row prisoner whom Gerald had brought back to Jesus?

ALBERT: Wild Man Cody had killed his whole family of eight with knives and a gun, before the police captured him. Only his grandmother, Granny Lucy, was unscathed that day, because she was having a hip operation. When Wild Man Cody found out that he missed one member of his family... he escaped from jail, went to the hospital, and strangled Granny Lucy in the intensive care unit. Then, his life's work done, he gave himself up.

FANNY: Gerald spent hundreds of hours praying with Mr. Cody...until... poooof! Jesus flamed in his heart. Mr. Cody became born again and allowed Jesus to spin the wheel of his destiny. He said so freely.

ALBERT: Yes. The other death-row prisoners got so sick of listening to Wild Man that they all petitioned to have their execution dates pushed up. [Albert mimics the jailhouse conversation]

WILD MAN: I am not afraid to die and neither should any of you others!

MALE VOICE: Give it a rest, Cody!

WILD MAN: I love those I stabbed. I love those I shot. I love Granny Lucy who I choked. I love the police who arrested me. I love the warden here. I love the press reporters who wrote I should die. Also, I love the executioner who will pop the lethal injection into my arm. I want to be executed. I really crave it. I do. You all know why? Because I want to repose with the Lord Jesus for eternity. I'm coming, Jesus! I'm coming! Won't be long!

MALE VOICE: Somebody shut him up! This is cruel and unusual punishment!

ALBERT: In this same spirit of love, Wild Man Cody allowed me, under the prisoner medication testing program, to administer 100 milligrams of Deus-X to him.

FANNY: Gerald and I, as Mr. Cody's spiritual advisors, had no objection. We believed the drug would do nothing to diminish the purification that Gerald had wrought.

ALBERT: But minutes after taking the dosage of Deus-X. . . [ALBERT plays the role of WILDMAN] [Standing and rattling his bars.] I'm glad I killed my whole family! I hated them! They hated me! We hated each other! On Christmas morning, we spat on each other! The Codys were always honest! You know the thrill of seein' your loved ones gunned down? Huh? Killing Granny Lucy was best of all! She couldn't cook! Couldn't sew! And when you went near her, she stunk of old age! I hadda hold my friggin' breath when I strangled her! I hated her! I hate you! All of you!

FANNY: Was it really the effect of Deus-X?

ALBERT: Yes. But one more illustration lest you think that Wild Man Cody was an anomalous fluke.

FANNY: At that time, Gerald and I still didn't believe in Deus-X.

ALBERT: It was science and religion head to head. And Fanny and Gerry were looking bad. While all the medical men and women in the world rushed to lionize me, religious groups, one after another, challenged me. Challenged Deus-X. I turned a whole seminary into circus performers. Large convents were left abandoned, habits strewn on the floors. Synagogues were converted into supermarkets. Muslims tried to kill me for transforming one of their holy men into a jockey. .. I made the cover of Newsweek twice!

FANNY: It was sibling rivalry, that's all! You were trying to out-do a more famous brother. Gerald had planned to run for the Presidency of the United States, until... until...

ALBERT: One night on his T.V. program, when Gerry was half crazed with belief in his powers to invoke the aid of the deity, my brother voiced before the whole nation...

FANNY: Ladies and Gentlemen, please welcome Jesus' General here on earth, The Reverend Gerald Spieler!

ALBERT AS GERALD: [Entering with his Bible to loud applause.] Welcome! Welcome, Brothers and Sisters in Christ! Praise God! And welcome to the Lord's very own T.V. program. You all know why we're here tonight. I hold in my right hand the Book of Light, and in my left hand I hold 100 milligrams of the substance that my devil-driven brother calls Deus-X. Yes, it is the real thing. I asked him to come here tonight and place the pill in this hand, so he could not say we substituted an M & M for this... this X .. . Yes, X. Ex. Extinguish. Expunge. Extirpate. Exclude. All the"Ex's" that his kind would like to do with all that you and I hold sacred. . . Well, this pill might've spooked some of those others whose faith was weak, Brothers and Sisters. But Jesus' General is made of Christian stuff! [GERALD pops the pill. FANNY leads more applause.]

ALBERT: My brother, Gerry, had an unusually large and hard Deus gland.. The Deus pill took its time. ..

FANNY: What is it, Gerald?

ALBERT AS GERALD: It just dawned on me, Fanny Mae ...How... how... illogical - no, irrational that this all. . . IS ... praying ... Praying is illogical and irrational anytime. .. It is in the same category as speaking to a chair or a shoe... Nobody ever answers a prayer! Ever!

ALBERT: Don't look at me. He insisted on pitting the pill against prayer. I even tried to talk him out of it. I did.

FANNY: ... and that's why I came here today... to save my marriage. After the incident on TV., in front of millions, our whole audience changed... Our program changed.. . Now it's a talk show. Instead of "Jesus" General, it's called "General Mayhem". The guests are gays, transexuals, former convicts, authors, actors, in short, all the rot in the world...

ALBERT: Gerry wants Fanny Mae to loosen up. He wants her to dress up in a garter belt and stockings. He wants her to take her first taste of white wine. He wants her to start watching videos with him.

FANNY: I'm a minister's daughter! I can't do any of those things! They're sinful. They're vulgar. They're cheap. They're beneath me and I ... I ... I ... [ALBERT hands her a Deus-X pill and a glass of water.] But Gerald Spieler is my husband. He's all I had, and now I'm lonely... so lonely that... may God have mercy on my soul. [FANNY takes the pill.]

ALBERT: It didn't take too long before Deus-X shrank Fanny Mae's Deus gland. Fanny Mae now administers to her husband's needs. They invite me for dinner. My brother, Gerry, and I have become best friends. We enjoy good wine and conversation and ... We're attending the Cody execution tonight.

In a nutshell . . . Today I travel all over the world... [He holds up the red Deus-X pill.] I leave it everywhere. As you exit tonight, there'll be a bowl of them in the lobby. Take one. They're free. Good night ... Good night and God leave you...
```

---

## IC-0752: The Dining Room

- Title: The Dining Room
- Author (byline): A. R. Gurney
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MEG, JIM, MEG'S VOICE
- Teaser before the introduction: Yes
- Spoken words (computed): 1142
- Already set (do not supply): none

### Source block (context only)

```text
Author: A.R. Gurney
ISBN: 0822203103
Publisher: Dramatists Play Service
Date(Month/Year): Jan 1998
PA State Champion
```

### Introduction (context only: never use it for content warnings)

```text
Actor: Over 80 million adult children who have left home have returned to live with their

parents. They call them “boomerang kids.” Actress: And the reasons are as varied as the grown children themselves. . . financial hardships,

failed marriages, Actor: In this scene, Meg broaches the very serious prospect of returning to her parents home

with her three small children. The discussion takes place in Actress: The Dining Room by AR Gurney.
```

### Performance text (classify this)

```text
JIM, comes in from the hall, followed by his daughter, MEG. He is in his late sixties, she is about thirty.

MEG: Where are you going now, Daddy?

JIM: I think your mother might want a drink.

MEG: She's reading to the children.

JIM: That's why she might want one.

MEG: She wants no such thing, Dad.

JIM: Then I want one.

MEG: Now? It's not even five.

JIM: Well then let's go see how the Red Sox are doing. (He starts back out, R.)

MEG: Daddy, stop!

JIM: Stop what?

MEG: Avoiding me. Ever since I arrived, we haven't been able to talk.

JIM: Good Lord, what do you mean? Seems to me everybody's been talking continuously and simultaneously from the moment you got off the plane.

MEG: Alone, Daddy. I mean alone. And you know I mean alone. . .

JIM: All right. We'll talk. (Sits down.) Right here in the dining room. Good place to talk. Why not? Matter of fact, I'm kind of tired. It's been a long day. .

MEG: I love this room. I've always loved it. Always.

JIM: Your mother and I still use it. Now and then. Once a week. Mrs. Robinson still comes in and cooks us a nice dinner and we have it in here. Still. Lamb chops. Broilers

MEG: (Suddenly.) I’ve left him, Daddy.

JIM: Oh well now, a little vacation. . .

MEG: I've left him permanently.

JIM: Yes, well, permanently is a very long word. . .

MEG: I can't live with him, Dad. We don't get along at all.

JIM: Oh well, you may think that now. . . .

MEG: Could we live here, Dad?

JIM: Here?

MEG: For a few months.

JIM: With three small children?

MEG: While I work out my life. (Pause. JIM takes out a pocket watch and looks at it.)

JIM: What time is it? A little after five. I think the sun is over the yardarm, don't you? Or if it isn't, it should be. I think it's almost permissible for you and me to have a little drink, Meg.

MEG: Can we stay here, Dad?

JIM: Make us a drink, Meggie.

MEG: All right. (She goes into the kitchen; the door, of course, remains open.)

JIM: (Calling to her.) I'd like Scotch, sweetheart. Make it reasonably strong. You'll find the silver measuring gizmo in the drawer by the trays. I want two shots and a splash of water. And I like to use that big glass with the pheasant on it. And not too much ice. (He gets up and moves around the table.)

MEG'S VOICE: (Within.) All right.

JIM: I saw Mimi Mott the other day. . . Can you hear me?

MEG's VOICE: (Within.) I can hear you, Dad.

JIM: There she was, being a very good sport with her third husband. Her third. Who's deaf as a post and extremely disagreeable. So I took her aside-can you hear me?

MEG's VOICE: (Within.) I'm listening, Dad.

JIM: I took her aside, and I said, "Now Mimi; tell me the truth. If you had made half as much effort with your first husband as you've made with the last two, don't you think you'd still be wed to him?" I asked her that. Point blank. And you know what Mimi said? She said, "Maybe." That's I exactly what she said. "Maybe." If she had made the effort. (MEG returns with two glasses. She gives one to JIM.)

MEG: That's your generation, Dad.

JIM: That's every generation.

MEG: It's not mine.

JIM: Every generation has to make an effort.

MEG: I won't go back to him, Dad. I want to be here.

JIM: (Looking at his glass.) I wanted the glass with the pheasant on it.

MEG: I think the kids used it.

JIM: Oh. (Pause. He drinks; moves away from her.)

MEG: SO can we stay, Dad? ,

JIM: I sleep in your room now. Your mother kicked me out because I snore. And we use the boys' room now to watch TV.

MEG: I'll use the guest room.

JIM: And the children?

MEG: They can sleep on the third floor. In the maid's rooms.

JIM: We closed them off. Because of the oil bills.

MEG: I don't care, Dad. We'll work it out. Please. (Pause. He sits down at the other end of the table.)

JIM: Give it another try first.

MEG: No.

JIM: Another try.

MEG: He's got someone else now, Dad. She's living there right now. She's moved in.

JIM: Then fly back and kick her out.

MEG: Oh, Dad. . .

JIM: I'm serious. You don't know this, but that's what your mother did. One time I became romantically involved with Mrs. Shoemaker. We took a little trip together. To Ashland. Your mother got wind of it, and came right down. . . told Betty Shoemaker to get on the next train. That’s all there was to it. Now why don't you do that? Go tell that woman to peddle her papers elsewhere. We'll sit with the children while you do.

MEG: I've got someone too, Dad. (Pause.)

JIM: You mean you've had a little fling.

MEG: I've been going with someone.

JIM: A little fling.

MEG: I've been living with him.

JIM: Where was your husband?

MEG: He stayed with his girl.

JIM: And your children?

MEG: Oh they. . . came and went.

JIM: It sounds a little. . . complicated.

MEG: It is, Dad. That's why I needed to come home. (Pause. He drinks.)

JIM: Now let's review the bidding, may we? Do you plan to marry this new man?

MEG: No.

JIM: You're not in love with him?

MEG: No. He's already married, anyway.

JIM: And he's decided he loves his wife.

MEG: No.

JIM: But you've decided you don't love him.

MEG: Yes.

JIM: Or your husband.

MEG: Yes.

JIM: And your husband's fallen in love with someone else.

MEG: He lives with someone else.

JIM: And your children. . . my grandchildren... come and go among these various households.

MEG: Yes. Sort of. Yes.

JIM: Sounds extremely complicated. . .

MEG: It is, Dad. It really is. (Pause. He drinks. thinks, gets up, paces.)

JIM: Well then it seems to me the first thing you do is simplify things. That's the first thing. You ask the man you're living with to leave, you sue your husband for divorce, you hold onto your house, you keep the children in their present schools, you . . .

MEG: There's someone else, Dad. (Pause.)

JIM: Someone else?

MEG: Someone else entirely.

JIM: A third person.

MEG: Yes.

JIM: What was that movie your mother and I liked so much? The Third Man? (He sits)

MEG: It's not a man, Dad. (Pause.)

JIM: Not a man.

MEG: It's a woman.

JIM: A woman.

MEG: I've been involved with a woman, Dad, but it's not working, and I don't know who I am, and I've got to touch base, Daddy. I want to be here. (She kneels at his feet. Pause. JIM gets slowly to his feet. He points to his glass.)

JIM: I think I'll get a repair. Would you like a repair? I'll take your glass. I'll get us both repairs. (He takes her glass and goes out to the kitchen, leaving the door open.)

MEG: (Moving around the dining room.) I'm all mixed up, Dad. I'm all over the ball park. I've been seeing a Crisis Counselor, and I've taken a part-time job, and I've been jogging two miles a day, and none of it's working, Dad. I want to come home. I want to take my children to the Zoo, and the Park Lake, and the Art Gallery, and do all those things you and Mother used to do with all of us. I want to start again, Dad. I want to start all over again. (JIM comes out from the kitchen, now carrying three glasses.)

JIM: I made one for your mother. And I found the glass with the pheasant on it. In the trash. Somebody broke it. (He crosses for the doorway, R.) So let's have a nice cocktail with your mother, and see if we can get the children to sit quietly while we do.

MEG: You don't want us here, do you, Dad?

JIM: (Stopping.) Of course we do, darling. A week, ten days. You're most welcome.

MEG: (Desperately.) I can't go back, Dad!

JIM: (Quietly.) Neither can I, sweetheart. Neither can I. (He shuffles on out. MEG stands for a moment in the dining room, then hurries out after him.)
```

---

## IC-0753: Distracted

- Title: Distracted
- Author (byline): Lisa Loomer
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Jan 2010
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SUGGESTED ROLES, MAMA, JESSE, DR. ZAVALA, MRS. HOLLY, DAD, DR. JINKS
- Teaser before the introduction: Yes
- Spoken words (computed): 2642
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lisa Loomer
ISBN: 978-0822222989
Publisher: Dramatists Play Service
Date (Month/Year): Jan 2010
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: What's wrong with nine-year-old Jesse? He can't sit still, he curses, he raps, and you can't get him into-or out of-pajamas.

ACTOR: His teacher thinks it's Attention Deficit Disorder.

ACTRESS: Dad says, "He's just a boy!" And Mama's on a quest for answers.

ACTOR: Is Jesse dysfunctional, or just different?

ACTRESS: Don't we all have ADD, to some degree?

ACTOR: It seems that everyone today is

TOGETHER: Distracted by Lisa Loomer
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! See note from the author about “Casting” below. This may be considered an exception for some tournaments. Be sure to check your STATE rules before performing at local tournaments.

NOTE: from the Author: The actors can play multiple roles. Feel free to use accents for the various doctors the actors portray.

SUGGESTED ROLES: Actor: Jesse, Dad, Dr. Zavala, Dr. Jinks Actress: Mama, Mrs. Holly

MAMA: (calls offstage; optimistic) Morning, Jess! Are you dressed? (No answer) Are you getting dressed, baby?

JESSE: I'm dressed!

MAMA: Get dressed, Jesse- (to audience) He's nine. (We continue to hear Jesse's voice offstage for the remainder of this cutting – Jesse never is seen . . only heard)

JESSE: Where the hell are my rocket balloons?

MAMA: (embarrassed) Don't say hell, Jess. And they're your toys, babe, you find 'em. What do you want for breakfast?

JESSE: Candy.

MAMA: (laughs - to audience) Sure, I'd love a couple of Almond Joys myself! (calls) Well, you can't, 'cause it's not good for you. (beat) So what do you want?

JESSE: (shouts) Poached eggs! Whatever!

MAMA: (to audience) And when they're done, he changes his mind. He gets Coca Crispies, and after he has filled it too high with milk, and spilled it on the floor, he finds a rocket balloon, and, instead of eating, he gets . . . distracted.

JESSE: I gotta find the pump for the rocket balloons!

MAMA: We're not setting off rocket balloons!

JESSE: (explodes) I don't want to set them off! I just want to find the fucking pump! (A pause. Mama smiles at the audience, embarrassed by the word.)

MAMA: All right, find it. And then get dressed and eat-or eat and get dressed, whatever. (to audience) I know. I should have given one simple command. I should have given a "time out" for the [F-word]. [But] I've just read a book called THE EXPLOSIVE CHILD which says you should pick your battles. You should have an A basket for issues of safety, a C basket for issues that are not important right now, and a B basket for the negotiables. . . . He's a little . . . anxious. At least that's what the psychologist who observed him last week at school thought. (Dr. Zavala enters. - Note that Dr. Zavala might be played by a male. In that case, all references to "her" become "he" or "him")

DR. ZAVALA: Well, let's see . . . I spent about three hours observing him at school . . . I watched him in class, in P.E . . . at lunch . . . I also spoke with his teacher - And from what I observed . . . He is a pretty anxious child. And he seems to try to compensate for the anxiety by being funny-

MAMA: (pleased} Really? He was funny?

DR. ZAVALA: Well-sometimes. He uses physical humor quite a lot, falling off a chair, falling off his desk, running into a wall in an effort to engage the other children-

MAMA: (hopeful) Did they laugh?

DR. ZAVALA: Well-sometimes. But he really can't rely on this as a way to connect to other kids.

And often, he'd just go off on his own. (looks at notes; sadly) He ate his lunch alone. I'm sorry. And, like his teacher told you at your Conference, he does seem to be easily . . . distracted. (actor exits scene and actress plays both Mama and Mrs. Holly for the next section – DI style)

MAMA: (to audience) Our parent-teacher conference was a month ago. Which is what clued us in there was a problem,

MRS. HOLLY: Well, one of the problems is that he doesn't want to do the work. He says he hates reading, he hates writing, and he hates math. You might want to get him tested for Attention Deficit Disorder-

MAMA: Are you saying our child has ADD!?

MRS. HOLLY: No- (to audience) I'm not allowed to say that. (to Mama) I'm just saying that I've been teaching for twenty-two years and I think testing for ADD might be a good idea. He cannot – cannot - stay on task. You know, Thomas Edison Elementary has the best test scores in the city- MAMA But Thomas Edison never would have made it through Thomas Edison-because Thomas Edison had ADD! You know, some amazing people have had ADD. Mozart had it, Einstein . . . Tom Sawyer, Huck Finn . . .

MRS. HOLLY: Mrs. Cara. A child with ADD is going to have trouble paying attention in any educational setting. How's he going to get through the next ten years?

MAMA: (after a beat) I don't know, Mrs. Holly. . . . Great! (sighs; to audience) Nine weeks from [then]. I head for my weekly appointment with Dr. Zavala. (Dr. Zavala enters scene)

DR. ZAVALA: So how are things going?

MAMA: Well, I guess you could say I had a little trouble with the basket system this morning in terms of the word "fucking."

DR. ZAVALA: (Dr. Zavala has a lot of enthusiasm for the basket system.) I understand. Let's see if I can help. Now, kicking, for example, is a matter of safety and definitely goes in the A basket. With the [F-word] . . . I'd say B or C basket, depending on the family. [The F-word] doesn't literally hurt anyone, but could get him suspended from school... And if you're churchgoers, [the F-wrd] could be a problem for all of you. So I'd say we leave it for the C basket-for the moment. And, in the meantime, I'm going to give you the name and number of an excellent psychiatrist.

MAMA: A psychiatrist!? Wait a minute. Psychiatrists prescribe drugs! I'm not putting my child on drugs. In no universe am I putting my child on drugs. (Dr. Zavala leaves) On the way home, I stop at Border's and pick up a few books on ADD. ************New Scene – Night. Mama is reading in her living room. ************

JESSE: (exuberantly insistent – off stage) I'm watching "Fast And Furious!"

MAMA: (reading) No you are not.

JESSE: Well, I'm having a snack.

MAMA: As soon as you're in your pajamas. Are you in your pajamas?

JESSE: (screaming) Why do I always have to get into my stupid pajamas? I'm just going to get out of them again! It's so stupid! It's such a waste of time!

MAMA: Do it or no snack! (to audience) He gets his pajamas on after doing a little dance in his underwear pretending to be a rapper . . . and checking off the date on his calendar and counting the days till Fourth of July . . . and playing earthquake . . .

DAD: (Dad enters.) Well, he is in bed. And it's only ten thirteen. What're all those books?

MAMA: Oh, I'm just doing a little reading on ADD.

DAD: Jesse doesn't have ADD. He's just a boy. Can't a boy be a boy anymore? I was the same when I was a kid. Worse. All the boys in my neighborhood were pretty wild. They stole. They tortured animals. They're cops and lawyers and businessmen now.

MAMA: Can I just read you a check list of symptoms of ADD? Short attention span. Distractibility. lmpulsivity. Other symptoms include . . . Disorganized thinking, poor judgment, risk taking and conflict seeking. (closes book)

DAD: lmpulsivity, short attention span, risk taking, getting distracted? Those are symptoms-of childhood! Is childhood a disorder now?

MAMA: Well . . . At least we've got a diagnosis . . . (to audience) I call Dr. Zavala. (Actor morphs into Dr. Zavala - Mama sighs)

DR. ZAVALA: Have you thought about calling a psychiatrist?

MAMA: Look, I know what a psychiatrist does-a psychiatrist prescribes drugs! For a nine year old child!

DR. ZAVALA: I understand. I think you're right to try everything else first, every conceivable good option.

MAMA: Sorry. So what other conceivable good option can we try?

DR. ZAVALA: Well, a good behavior modification program is essential with or without medication.

MAMA: Okay. Let's do it.

DR. ZAVALA: Terrific. First, you're going to buy a set of poker chips. (Dr. Zavala delineates the following with great enthusiasm.) Then. You're going to make a chart of all the behaviors you want to see from Jesse, and you'll decide how many points each is worth. For instance: If he gets into his pajamas on the first request-you'll give him five poker chips. If he does not get into pajamas . . . you'll take away five poker chips as a consequence. Next, you're going to ask his teacher to make a list of behaviors she wants to see in class. Then, you're going to make two more charts. One for Daily Rewards. And one for Future Rewards. Daily Rewards might be watching TV, having dessert, riding his bike . . . And you'll decide how many poker chips each of these will cost. Then, each day, you'll tally up the chips he's earned at home and at school . . . He has to spend the chips for Daily Rewards that day.

MAMA: Shouldn't there be some perks that just come with childhood?

DR. ZAVALA: Unfortunately, it's not easy to motivate the ADHD child to comply, and that's causing enormous difficulties . . . Shall we make an appointment for next week to see how it's going?

MAMA: Sure. (to audience) Why even *pretend a week’s gone by*? (They don't) DR. ZAVALA (brightly) So how's it going?

MAMA: Well, my husband didn't think it was fair that Jesse had to earn points to ride his bike because exercise is necessary for a child. He also felt Jesse should get some warnings before losing points . . . There was also a little problem with Jesse's teacher.

MRS. HOLLY: (resentful) He forgets to give me the Daily Rewards Sheet so I can fill it out and give him his chips. And when he remembers, he forgets to bring it home.

DR. ZAVALA: Well, I can certainly understand your frustration

MAMA: (to audience) But if he could remember the Daily Rewards Sheet, he wouldn't need the Daily Rewards Sheet because he wouldn't have ADD!

MRS. HOLLY: I heard that! You know the other mothers are whispering about you.

DR. ZAVALA: Look. I think we're all here because we care. About Jesse. So how about this. Could you ask him for the Daily Rewards Sheet and fill it out and put it in his book bag?

MRS. HOLLY: If I didn't have twenty-seven other children in my class, I could! And I could follow him into the bathroom so he doesn't get into wet paper towel fights! And while I'm there, maybe even help him wipe his little-

MAMA: (to audience) You know she didn't say that. But what she did say was much worse.

MRS. HOLLY: I'm going to recommend he be sent to Special Ed. (Mrs. Holly exits)

DR. ZAVALA: (to Mama) Clearly we are at a crisis point . . . where Jesse's self-esteem is at stake. So what I am going to say . . . And you know I don't say this lightly . . . But we've tried a number of approaches . . . And, at this point, I'd be terribly negligent if I did not say

MAMA: (to audience) Is there some way to not have to hear this!?

DR. ZAVALA: Ritalin.

MAMA: What kind of mother drugs a nine-year-old!?

DR. ZAVALA: One who leaves no stone unturned when she's trying to help her child. (pause.) When Ritalin works, it can seem like a miracle. (Dr. Zavala morphs into Dr. Jinks)

DR. JINKS: Dr. David Jinks . . . Giving a child with ADHD Ritalin is like giving a child with diabetes insulin. Or giving a child with astigmatism glasses. The world comes into focus for the first time. Before Ritalin, you can give a child the same instruction day in, day out, and no matter how clear you are, how strict you are, what a good parent you are . . . it simply may not stick. With Ritalin, he simply cannot not pay attention.

MAMA: Why? What does it do?

DR. JINKS: It's a stimulant. Which the ADD brain needs. Are you with me? Am I going too fast?

MAMA: Not at all. (He begins to speak louder or more insistently . . . or so it seems to her.)

DR. JINKS: ADD is a life span disorder. Thirty-five percent of kids with ADD never finish high school. Forty-five percent of males with ADD are arrested for a felony before the age of sixteen, and fifty to seventy-five percent of the prison population has some form of ADD. The divorce rate for people with ADD is two times the average, they're five times as likely to get into car accidents- And people with untreated ADD are three times more likely to abuse drugs.

MAMA: But isn't Ritalin a Class 2 Restricted drug for its potential for addiction and abuse? Isn't it speed?

DR. JINKS: As I said, it is a stimulant.

MAMA: And [this] drug - sorry, medication - can cure ADD?

DR. JINKS: The patient is able to concentrate while the drug is active in the system.

MAMA: And when it wears off?

DR. JINKS: He is himself again.

MAMA: Oh terrific. So Ritalin doesn't cure? You can take it for the rest of your life and it doesn't cure a thing? What about side effects?

DR. JINKS: The most common are loss of appetite, delayed growth, and insomnia, but we can always add another drug like Clonidine to help the insomnia. Some children develop tics, but we can add a little Tenex to control that. (Mama nods as Dr. Jinks morphs into Dad) *****Scene change*****

DAD: So you want to put Jesse on drugs.

MAMA: (quietly) No. Just . . . trying to keep an open mind. DAD (keeping a lid on) Cause, see, where I come from, "drugs" is kind of a bad word. (ironic but deadly) I also have a problem with the idea of somebody giving my son drugs to keep him nice and quiet. Maybe I don't think nice and quiet is such a good thing. . . . But, just like you, I'm trying to keep an open mind. So . . . what are you thinking?

MAMA: I'm thinking he has another ten years in school. Some school. He has to show up someplace between eight and three o'clock. For the next ten years.

DAD: School's a bore! Especially for a kid like Jesse who can't stand to sit there putting commas in sentences that don't mean anything to him or anybody else. "Who was the twenty-sixth president?" "Attention Deficit?" Teach them something worth paying attention to!

MAMA: I agree. But even if we could afford private school - the private schools don't want him. I mean, they say they want "diversity," but that just means they want different colored kids who know how to sit still and be quiet. They don't want different kinds of minds!

DAD: Well, too bad, they got 'em. Kids' minds are different now. Anything they're asked to memorize, they can get on the computer faster-so what do they need a bunch of meaningless facts stored in their heads for? So they can get a good grade on a test? "No Child Left Behind?" The whole country's being left behind!

MAMA: I know, honey, but our child is the one being "recommended" for Special Ed!

DAD: Special Ed? Special Ed is like preschool for jail!

MAMA: Well, either the school system has to change. Or Jesse does. (with great difficulty) What's worse? Giving a child a drug? Or having him go to school day after day, year after year, hearing his name called out like a curse, seeing the smiles on teachers' faces turn to frowns. Do you think he's falling off desks to make people laugh because he's having a good time?

DAD: So you would drug our child to fit into a school system that is not only outdated but unkind? I love that child! That's-my boy! (breaks into tears) I love- (crying) I don't know what to do . . . I just want him to be . . . a happy kid . . .

MAMA: I know. I know. So do I . . . (Dad exits – Mama to audience) The next week, l . . . try Ritalin in the form of a drug called Concerta which is designed to last ten to twelve hours. The first week, Jesse doesn't eat lunch, picks at dinner, and doesn't fall asleep till one a.m. At eight p.m., when the drug starts to wear off, I ask him to get into his pajamas.

JESSE: (bursts into tears) Leave me alone! Just leave me alone! Why are you always bothering me? Why can't you leave me alone! I'm trying to be good! I'm trying to be good so we can be a happy family!

MAMA: (to audience) Dr. Jinks increases the dosage. Twice. And soon, by seven-thirty p.m., Jesse's in his pajamas. By seven-thirty a.m., he's dressed. Even on Saturday. (calls to Jesse) Jesse? (beat) Jesse?

JESSE: Yeah? (Jesse sounds rather like . . . a zombie.)

MAMA: What are you doing, sweetie?

JESSE: (flatly) Watching TV.

MAMA: Do you want to do a watercolor with me? (beat) Do you want to make hors d'oeuvres?

(beat) Jess? (Dad crosses through the living room.) (Mama to Dad) He's still not eating. He's pretty much been sitting there all weekend-

DAD: Nice and quiet? (Mama nods. He exits. Mama heads toward Jesse's room.

MAMA: Jesse? It's time for your pill, Jess.

JESSE: (enraged) I hate it, Mom! I hate it! It makes me feel like I've got bugs inside!

MAMA: Well, the doctor says you have to give it a little time. Then you'll feel fine.

JESSE: I hate it! I hate you!

MAMA: (to audience) He begins to pant. I tell him to take a deep breath, but he can't. His breathing gets faster and faster. He flings the towels in the linen closet on the floor - and then he does something which scares the shit out of me, breaks my heart, and makes me know I am unfit to have a child. (beat) He hides. In the linen closet.

DAD: (Dad enters and is dead calm) If you continue to give my son drugs, I will divorce you, and I will fight for custody. My son is not crazy. He's not a danger to anyone, and he wasn't a danger to himself till you gave him speed. He'll get through school . . . like I did. He'll be the black sheep. The freak. The weirdo. But he'll survive. (Mama is about to burst into tears. Dad just looks at her and leaves. We hear Jesse crying softly from the closet offstage.)

MAMA: (long silence, then . . .repeats with even great difficulty) What's worse? Giving a child a drug? Or having him go to school day after day, year after year, hearing his name called out like a curse.

JESSE: (softly off stage in a zombie like voice) I'm trying to be good! I'm trying to be good so we can be a happy family . . .
```

---

## IC-0754: Disturbed

- Title: Disturbed
- Author (byline): Brad Bosen
- Work: Millennium Monologs: 95 Contemporary Characterizations for Young Actors, ed. Gerald Lee Ratliff - Daphne’s Monologue Only, Pgs 147-149
- Publisher: Meriwether Publishing
- Publication date as stated: Nov 2002
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BOB, DAPHNE
- Teaser before the introduction: Yes
- Spoken words (computed): 2490
- Already set (do not supply): none

### Source block (context only)

```text
Author: Brad Bosen
Book: Millennium Monologs: 95 Contemporary Characterizations for Young Actors, ed.
Gerald Lee Ratliff - Daphne’s Monologue Only, Pgs 147-149
ISBN: 978-1566080828
Publisher: Meriwether Publishing
Date (Month/Year): Nov 2002
Full play can be found here: https://www.geocities.ws/quietharry/pboese02.html
A note from the playwright: Monologues may be used at no cost and without prior permission for
classes, competitions and auditions, as may small scenes used strictly for classroom or competition
purposes. If you do use any of my stuff for auditions, classes and such, though, please e-mail me
and tell me how it went for you at mulberries@bjboesen.com
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Emotional scars, although they may heal over time or are invisible to the world at large, never really disappear.

ACTRESS: But we develop coping mechanisms to deal with the pain and to protect ourselves.

ACTOR: We build walls – much like this imaginary wall dividing Daphne and Bob from the babies on the other side.

ACTRESS: An invisible glass wall built for safety.

ACTOR: But these coping mechanisms – these walls – are they healthy

ACTRESS: Or are they merely survival techniques to cover up the fact that we are all,

ACTOR: in our own way . . .

TOGETHER: Disturbed by Brad Boesen

DAPHNE: [a bit hesitant] Are you alright? [Silence. Bob continues to stare ahead] Sir? [growing

more concerned. Agonizing over whether to help or leave him alone, she softly touches his

elbow. He looks at her and she quickly pulls her hand back] I'm sorry. . . Are you alright? You
```

### Performance text (classify this)

```text
The nursery of a city hospital. The audience is where the babies would be. The actors are on the other side of the "glass" Daphne is peering out at the audience happily cooing and making faces at the "babies. Bob enters. About the same age as Daphne, he is obviously in a very dark mood. He stares blankly at the babies, seemingly oblivious to Daphne's continued antics. Daphne, sensing Bob's depression, begins to include him -- pointing him out to the babies, making grouchy faces, trying to improve his mood until a long, mournful sigh from Bob stops her.

look. . .

BOB: Yeah. [he looks at the babies, senses she's not convinced, turns back] I'm fine. [flashes an unconvincing smile and turns back towards the babies]

DAPHNE: [playing along] Oh. . . ok. . . well, good. [uncomfortable with the silence, but not wanting to leave, she decides to fill it] I love babies. I come here almost every day to look at them. I work right across the street. At that little diner. By the time lunch break rolls around I'm so tired of all that food I just don't even want to think about eating, so I come over here and look at them. [one of the babies does something cute] Ahhhhhh! Look at him! [laughing, rattling a box of tic tacs, and talking to the baby] Hellooooo. Hello in there.

BOB: [watching her this time. More incredulous than angry or annoyed] Are you always this cheerful? [she pauses, uncertain how to react] I mean you just keep babbling at them like. . .

DAPHNE: They're cute! Don't you think they're cute? [Bob considers the babies for a moment, shrugs as if to say "sure, if you say so. Daphne begins replacing items in her purse she has been using to amuse the babies. One of the items is a pack of gum, sensing a possible conversation starter, she offers some to him] Gum?

BOB: No, thanks.

DAPHNE: It's Juicy Fruit. [Bob shakes his head "no"] It's alright, really, I've got plenty. I've got kind of a sweet tooth. A whole mouth full of them actually. [beat. Daphne senses Bob’s depression] My mom always used to say that all you have to do to chase away the blues is look at a sunset. . . or a flower. [pause] The beauty of God's creation. [pause] Then she'd down another fifth of vodka and pass out on the couch. [She laughs. Bob walks downstage closer to the babies. Daphne watches him] It's a valid concept, though, when you think about it. . . the sunset, not the vodka. Although, I suppose. . .

BOB: My wife died today. [silence] In childbirth. . . She and the baby both.

DAPHNE: [softly] Oh, my. . . Oh my God, I'm. . . Really? I mean. . . I'm sorry. [pause. Bob turns, sees her expression and bursts out laughing. Daphne is frozen in confusion] What?

BOB: [laughs even more hysterically at this reaction] I'm sorry. [still laughing] You just kept yammering.

DAPHNE: You were joking?

BOB: [nods his head, wiping tears from his eyes] I'm not even married! [more laughter]

DAPHNE: That was. . . HORRIBLE! How COULD you. . .

BOB: [laughter finally dying down a bit] Oh, come on. What? [Daphne turns away] It was a joke! Come on! If you could have seen the look on your face. [He bursts into laughter again] I'm Bob, by the way. [he reaches out as if to shake hands]

DAPHNE: I have to go now, Bob. [she turns to leave, Bob moves with her, blocking her path]

BOB: What? Come on! It was a joke. I was making conversation.

DAPHNE: CONVERSATION! THAT is NOT "making conversation"! THAT was. . . sick!

BOB: Oh, please. . . come on! You were boring yourself with all that crap about babies and the "beauty of God's creation"!

DAPHNE: Ok. Fine. But I really need to leave.

BOB: I'm sorry, ok? I'm sorry. I may have been slightly. . . inappropriate, but at least it got us talking. Right? Lunch break can't be over yet, you just got here. We'll talk. [Daphne clutches her purse to her chest and looks around for another way out] You can look at the babies. You Look at them. Aren't they cute? [she looks at the babies, smiles] My sense of humor takes a little getting used to. Ever since I was a kid. Drove my teachers crazy.

DAPHNE: Well. . . [polite smile-still wary] Well, I'm glad I could help you out of your mood. When you came in, you seemed so. . .

BOB: Oh, That. It's nothing, really. I think too much. You can loosen your grip on that purse if you want.

DAPHNE: Oh! I was just. . . I'm sorry. I, um. . .

BOB: Relax. You're perfectly safe. I'm weird, not violent.

DAPHNE: Well. . . [she tries to relax, without much success]

BOB: There you go. [long, uncomfortable pause]

DAPHNE: So. . . Um. . . Where are you from, Bob?

BOB: Here. Well, not here. I mean not from this hospital. [nervous laugh. Daphne nods politely] I just meant here in town. I've been in that diner you work at. You probably don't remember me.

DAPHNE: Well, I. . .

BOB: No, no, I understand. It's a busy place. [she nods] You're cheerful there, too. I mean, you have to be, right? You're grouchy, you don't get tips. But it's like you enjoy it or something. [she smiles] I mean it can get on your nerves after a while. . . Always cheerful. Always. . . up. Like with the babies before. [she smiles and looks at the babies. She can't resist a little wave. Bob shakes his head] Years from now they'll probably all be in therapy. [she looks at him] Recurring dreams of a huge lady rattling tic tacs in their face. [sees her reaction--quickly] I couldn't do it. Be cheerful all the time. So, where are you from, Daphne?

DAPHNE: [surprised, slightly wary] You know my name? [Bob points to the name tag on her chest. She's still dressed for work] Oh! Oh, of course, [my name tag]. [laughing] I'm sorry. I'm from Nebraska.

BOB: Nebraska. Wow. I bet they're all like you in Nebraska. Happy, smiling. . . riding horses, milking cows.

DAPHNE: I've never been on a horse in my life. And I've never touched a cow.

BOB: Sure, sure, I believe you. [small pause -- smiling]

DAPHNE: You've never been to Nebraska, have you?

BOB: No. But I've read about it. -- Stephen King. "Children of the Corn." And "The Stand". . . that old lady that talked to God. She was from Nebraska.

DAPHNE: [joking] If you went by those books, you'd expect everyone in Nebraska to be like you.

BOB: What do you mean?

DAPHNE: [slight pause--unsure if she's insulted him or if he's kidding] I don't know.

BOB: What am I like?

DAPHNE: I don't know. Nothing.

BOB: No, really, I want to know.

DAPHNE: I'm sorry. I didn't mean anything. You're just. . . dark, you know [very uncomfortable, struggling for words that won't insult him] somber. . . spooky.

BOB: What do you mean, "spooky"? And somber? What's somber?

DAPHNE: [throughout the following lines, Daphne becomes increasingly anxious and uncomfortable] I don't even know you. . .

BOB: What kind of word is "Somber"?

DAPHNE: I'm sorry, I just. . .

BOB: Calling a guy "spooky" and "somber"

DAPHNE: LOOK! YOU ASKED! [silence] I mean, I'm sorry if I insulted you. [pause] What are you doing here, anyway? Why are you bothering me?

BOB: I didn't know I was bothering you.

DAPHNE: I was having a perfectly good time, and then you come in here. . .

BOB: [overlapping slightly--interrupting] I'm visiting someone. [small pause]

DAPHNE: Oh, right, your dead wife and child. I'm so sorry.

BOB: I'm visiting my father.

DAPHNE: [not believing him] Your father.

BOB: He's. . . not doing well. I thought, maybe if I came down here, maybe the kids would cheer me up or something.

DAPHNE: Uh huh.

BOB: Look, I'm sorry I said that before, about my wife and kid, it's just. . . well, I knew you were going to ask, sooner or later, why I was here, and I didn't want to talk about it. Ok?

DAPHNE: [still skeptical, but what if he's telling the truth?] What's he got? [pause -- Bob looks at the babies] I'm sorry. You don't want to talk about it. I'll just. . . [turns to leave]

BOB: He shot himself. [silence] I found him this morning. [long pause--Bob stares ahead, expressionless]

DAPHNE: Oh, Bob. . . Um, you probably want to be alone. [turns again to go]

BOB: [when she's almost out the door] He left a note. [she stops] They always do that in books, you know. In movies. They always have some big message. . . something meaningful. You wanna know what his said? It said, "Bobby, you're the man of the family now. Take care of mother, and always remember [pause] people from Nebraska will believe anything you tell them." [pause]

DAPHNE: No. [Bob turns and smiles at her] Oh, no. [Bob bursts out in laughter. Daphne is shaken and enraged] You are SICK!

BOB: Oh, come on! You wanted spooky.

DAPHNE: I did not WANT spooky!

BOB: [still laughing] Look, I'm sorry. [she turns away] I couldn't resist. It was a joke.

DAPHNE: How could you say something like that? About your father?

BOB: What's the big deal? You never told a joke about your father? Come on. [she turns to face him]

DAPHNE: You want to hear a joke about my father? One night, when I was twelve years old, my father decided to decorate the house for Christmas. About a week before Christmas, dad went out and bought up all of the lights and decorations he could find. There wasn't much left, but he still got a lot. One store owner was so glad to get rid of everything so close to Christmas, that he threw in an old mannequin and Santa costume that had been cluttering up his storeroom. Dad built his whole display around it. [pause--smiles at the memory]

We didn't have a big chimney like you see in movies, so he put Santa on the roof of the porch, peering into the window of my parents' bedroom. Around all of the windows, he put red lights. Green lights around the edge of the roof. And combinations criss-crossed up and down in all the bushes and trees. . . It was beautiful.

I remember it was really cold that year, so he did all this with these gloves and a huge coat. I couldn't imagine how, with all those heavy clothes on, he could climb up that ladder and hang all those lights, but he did. And in between each string of lights, he would come down the ladder, pick me up off the ground, spin me around, and sit me up on his shoulders to get a better look. It took almost a week to finish it, but when he finally lit it all up, the whole town came out to see it. Everyone! I was so happy. I was sure that this was going to be the best Christmas in the history of Christmases; living in this. . . cocoon of color and light, with the rest of the world lining up outside to admire it.

On Christmas eve, dad went downtown to this bar that he used to hang out in. He liked to spend Christmas eve with his buddies, because, on Christmas, all the aunts and uncles would be over, and I guess being hungover gave him an excuse not to be a good host. [small pause] By the time he got home, it was past midnight. Mom had turned out all the Christmas lights for the night--she couldn't sleep when they were on, because they would shine in through her window--so the only light was from the streetlight at the end of the block, and, I guess, in the darkness, after drinking all night, dad forgot about the Santa mannequin. . . mistook it for a burglar or something because I woke up to hear shouting on the lawn. . . gunshots. . . breaking glass.

I ran into mom and dad's room, because I didn't know what was happening, but mom and dad weren't in bed. And it was cold, like someone had left the window open, so I looked. . . and there was my mother, just lying there on the floor, in the middle of all this shattered glass and blood. She must have been standing at the window when. . . [pause--Bob is frozen. Daphne stands staring into space--reliving the story] and I just stood there. . . I couldn't move. It was like a dream.

But then I heard the front door open, and footsteps running up the stairs. I was terrified. I thought that whoever had been shouting on the lawn must be coming to get me now, and there was no place to hide. The only thing I could think to do was lay down beside my mother and play dead. I thought whoever it was wouldn't hurt me if they thought I was already dead. So, when dad got to the door of the bedroom, he saw me and my mother and all that blood, and. . . he said. . . something. . . it didn't register at first, I was so scared, and concentrating so hard on not moving. . . and then he stumbled backwards out of the room, and I heard him crying and saying, "No, no, no,". . . over and over again. "No, no. . ." [pause] and I recognized his voice. It was dad. But before I could say anything there was another gunshot. [pause] And then he wasn't crying anymore. [pause] I guess he didn't have time to leave a funny note like your dad.

BOB: Oh, God I'm. . . I'm so sorry.

DAPHNE: Well, thank you, Bob, but right now I just really would like to be alone with the babies if you don't mind.

BOB: No. No, of course. I'll just. . . um. . . [he begins to exit; turns back, can't think of anything to say. Exits.]

DAPHNE: [doesn't watch him go, but stares ahead at the babies. She stands expressionless for a moment then smiles at something one of the babies has done. She laughs and waves with her index finger] Hello. Hello in there. Ahhhhhhhh! [laughs again -- still speaking to the baby] Try and ruin my day, will he? Well, that'll teach him teach him, won't it. Yes it will. [continues to coo, wave to the babies as the lights slowly fade to black]

Acting notes from the playwright: Though it would seem to be the easy assumption to make (and EVERYONE seems to make it), I think it's much more interesting if Daphne's story *isn't* just a joke. In other words, her story is true, but she still uses it to get back at Bob for what he's done to her. The original inspiration for the piece was my belief that people who are always extremely cheerful and "up" all the time are often the most screwed up people you could ever meet. I think Daphne is the most "disturbed" person in this play, not Bob.

That being said, I still leave it completely up to the director and/or performer to decide on whether her story is true or not. Either way, the audience and Bob must believe every moment of it. My goal was for the audience to leave the performance still wondering if she (or Bob) was actually lying. Whether or not YOU believe Daphne's story, the audience should still be wondering when they leave your performance.
```

---

## IC-0755: DMV Tyrant

- Title: DMV Tyrant
- Author (byline): Christopher Durang
- Work: Naomi In the Living Room and Other Short Plays
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Oct 1988
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CUSTOMER, DMV LADY
- Teaser before the introduction: Yes
- Spoken words (computed): 1039
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christopher Durang
Book: Naomi In the Living Room and Other Short Plays
ISBN: 978-0822214489
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Oct 1988
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Probably the most frightening phrase you can hear at the DMV is, “It’s a clerical error.”

ACTRESS: This phrase can mean almost any imaginable horrible thing you can conjure up. It can mean that you’ll have to come back and waste another day.

ACTOR: It can mean that you’ll have to retake the road test you already passed because your records have been misplaced.

ACTRESS: Or it can mean that due to a misspelling of your name, you’re now on the FBI’s most wanted list.

ACTOR: And it’s not even proper decorum to get angry about such things.

ACTRESS: You see, it’s not really their fault — making errors is part of the system.

TOGETHER: DMV Tyrant by Christopher Durang
```

### Performance text (classify this)

```text
Scene: A window at the Division of Motor Vehicles. A woman at a window is approached by a customer.

CUSTOMER: Is this window 7?

DMV LADY: Yes?

CUSTOMER: I’m afraid something rather complicated has happened with my driver’s license.

DMV LADY: I’m sorry to hear that. What happened? (With great disinterest he/she begins to read a book).

CUSTOMER: Well, you see, I moved here from another state, and I let my driver’s license lapse . . . and . . . . (Waits).

DMV LADY: (Looks up) Yes?

CUSTOMER: Should I wait until you finish?

DMV LADY: I don’t think so. It’s a very long book,

CUSTOMER: But . . . are you listening to my problem?

DMV LADY: I can read and listen at the same time. Go on. (Goes back to reading).

CUSTOMER: Oh. Well. Uh, anyway, I took the driving test again, and I passed it and got this temporary license, which has now expired, and I’ve never gotten my permanent one, and when I called about it, they said they had lost me in the computer, and they had no record of my taking the test, and so they couldn’t send me my license even though I did take and pass the test. (Pause) Your turn to say something.

DMV LADY: Wait a minute. (Reads some more. Looks up.) I wanted to finish the paragraph. Now what seems to be the matter?

CUSTOMER: Well . . .

DMV LADY: In one sentence.

CUSTOMER: I haven’t received my driver’s license.

DMV LADY: Let me see if you’re on the computer.

CUSTOMER: I’m not on the computer.

DMV LADY: What is your name?

CUSTOMER: I’m not there.

DMV LADY: How do you spell that?

CUSTOMER: I’m not on the computer. I went to Window 3 and they told me there was no record of me on the computer.

DMV LADY: I am not Window 3, I am Window 7, and I need to know your name.

CUSTOMER: James Agnes.

DMV LADY: Is that A as in aardvark, g as in gesundheit, n as in nincompoop, e as in excruciating, s as in seltzer water, pause pause, j as in Jupiter, a as in Agnes, m as in Mary, e as in excruciating, and s as in slow, lingering death?

CUSTOMER: Yes.

DMV LADY: (Types into computer; looks) Well, you’re not on the computer.

CUSTOMER: I told you I wasn’t.

DMV LADY: Fine. I will give you an award at the end of the day. How else may I help you?

CUSTOMER: I . . . I would like to get my permanent license.

DMV LADY: I’m sorry. There is no record of you on the computer.

CUSTOMER: Yes, but I have my temporary license. (Hands it to her)

DMV LADY: This temporary license has expired.

CUSTOMER: Yes, I know it’s expired.

DMV LADY: It is no longer a valid license.

CUSTOMER: I know that. That’s why I want my permanent one. I hadn’t noticed it hadn’t come in the mail until this one had already expired. I had presumed everything was alright.

DMV LADY: What a funny thing to do. (Suspicious) If you do not have a valid driver’s license, how did you get here to the Division of Motor Vehicles?

CUSTOMER: I took a taxi.

DMV LADY: Can you prove that to me?

CUSTOMER: What?

DMV LADY: Did you keep a receipt from the taxi?

CUSTOMER: No, I didn’t.

DMV LADY: I trust you did not drive here yourself, did you, Mr. James Agnes?

CUSTOMER: No, no, I realize my license is not valid.

DMV LADY: That is correct. You have an invalid license. Good morning.

CUSTOMER: But you’re not helping me.

DMV LADY: (Pleasantly) How may I help you?

CUSTOMER: I want my driver’s license.

DMV LADY: You must take the driving test.

CUSTOMER: But I took the driving test.

DMV LADY: I have no record of that.

CUSTOMER: I know you have no record of it, some schmuck lost it in the computer . . .

DMV LADY: Kindly do not speak Yiddish to me. If you wish to make an appointment to take the driving test, go to Window 4. (Goes back to reading).

CUSTOMER: I DON’T WANT TO TAKE THE TEST AGAIN!

DMV LADY: (Irritated) Well, when did you take the test before?

CUSTOMER: It’s the same date as that on my temporary license.

DMV LADY: February 3, 1894. The Division of Motor Vehicles did not exist in 1894.

CUSTOMER: Let me see that. (Looks) Alright, it’s a type. It’s clearly meant to be 1994.

DMV LADY: I am willing to agree with you that it is more likely a typo. You see, I don’t stick to the rules on everything. I am human. What is your name again?

CUSTOMER: James Agnes.

DMV LADY: Is that a as in aardvark, g as in gesundheit . . . .

CUSTOMER: James Agnes!

DMV LADY: Let me see if we have a record of you in the computer (Types into computer)

CUSTOMER: You don’t, you don’t, I told you you don’t!

DMV LADY: Why are you shouting at me? When I am shouted at, I do not feel like cooperating.

CUSTOMER: But you haven’t been cooperating.

DMV LADY: I have been cooperating. If I had not been cooperating, you would have been shouting at me much earlier than this.

CUSTOMER: I want my license.

DMV LADY: Well, you can’t have it. You’re not on the computer.

CUSTOMER: But that’s not my fault.

DMV LADY: And it’s not my fault. We are both blameless. Isn’t it a nice feeling?

CUSTOMER: You are not helping me.

DMV LADY: I am doing everything in my power.

CUSTOMER: But don’t you have more power than you’re using? Can’t you for instance, type me into the computer, and then send me my license?

DMV LADY: No. Only the secretary at the driving test site can do that.

CUSTOMER: But when she forgets to do that at the time of the driving test, can’t someone else do it then?

DMV LADY: If the secretary at the driving test site is willing to write a note admitting that she had forgotten to type in your name, then I can enter your name into the computer. And then we will fire her. Do you want her to lose her job?

CUSTOMER: No I don’t. I want you to lose your job.

DMV LADY: I don’t see how you can expect me to help you if you’re going to be hostile.

CUSTOMER: Isn’t there anything you can suggest to solve my problem?

DMV LADY: (Thinks) If you could re-live the initial driving test, when it was finished, you could ask to watch the secretary type in your name and your test result into the computer.

CUSTOMER: Your suggestion is that I re-live the initial driving test?

DMV LADY: It is a hypothetical suggestion, I admit, but it is the limit of what I can think of to assist you.

CUSTOMER: Could I see your supervisor, please?

DMV LADY: My supervisor is shredding documents in the other room, and cannot be disturbed.

CUSTOMER: (Angry) Look into my eyes. I want you to tell me what I should do that will solve my problem, and I want you to tell me right now!

DMV LADY: Move out of New York.

CUSTOMER: (Taken aback, but it might be worth it). That’s a good suggestion. Thank you. (He storms out)

DMV LADY: (Calling after him) Ohio’s nice. (She goes back to reading)
```

---

## IC-0756: Don’t Listen to What it Sounds Like

- Title: Don’t Listen to What it Sounds Like
- Author (byline): Mark Borkowski
- Work: 2006: The Best Ten-Minute Plays for 2 Actors
- Publisher: Smith and Kraus
- Publication date as stated: September 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GRETCHEN, FLOYD, RETCHEN
- Teaser before the introduction: Yes
- Spoken words (computed): 1325
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mark Borkowski
Book: 2006: The Best Ten-Minute Plays for 2 Actors
ISBN: 978-1575255637
Publisher: Smith and Kraus
Date (Month/Year): September 2007
```

### Introduction (context only: never use it for content warnings)

```text
GRETCHEN: Recent studies have shown that only seven percent of the meaning of speech is what is literally said.

FLOYD: The other ninety-three percent is implied communication.

GRETCHEN: Body language,

FLOYD: Tone.

GRETCHEN: This is why children are chastised for having an attitude while answering “yes ma’am”

FLOYD: and why a wife can communicate great sorrow while claiming things are “fine.”

GRETCHEN: Two former mental patients explore the detriments of tone in

BOTH: “Don’t Listen to What it Sounds Like”

FLOYD: by Mark Borkowski
```

### Performance text (classify this)

```text
GRETCHEN: You sound like -

FLOYD: - what, I sound like what?

GRETCHEN: Like ... you're upset.

FLOYD: That's not true.

GRETCHEN: That's what it sounds like.

FLOYD: Don't listen to what it sounds like!

GRETCHEN: What d'ya mean don't listen to -

FLOYD: Because I didn't mean it that way.

(Floyd is already ranting at Gretchen. She sits in a chair politely listening ...)

FLOYD: My blood flowing from open wounds. My body hanging from a barbed wire fence. My meat tearing from its thorns. Slipping onto the subway tracks and the subway car ravaging my body to pieces. Animals attacking me from all sides, ripping me apart. My tongue pulled out of my mouth. Decapitation. Castration. Fingers caught in table saws. My own personal apocalypse. Why am I haunted with these images?

GRETCHEN: It's ... good to see you again, Floyd.

FLOYD: You asked me what was on my mind.

GRETCHEN: I asked you. .. how you were doing. I'm sorry.

FLOYD: Why are you sorry? What have you got to be sorry for? For asking me?

GRETCHEN: No, not at all.

FLOYD: Well, that's that. It's off my chest ... for the moment. It's part of you now.

GRETCHEN: It's been a while.

FLOYD: Should be glad.

GRETCHEN: No.

FLOYD: Should count your lucky stars –

GRETCHEN: I missed you.

FLOYD: Missed me ? You know what it's been like - what I had to go through since I last saw you?

GRETCHEN: I'd like to know.

FLOYD: No you don't. I'm lucky I'm alive. Is that luck? Sometimes I wonder.

GRETCHEN: You look good.

FLOYD: Look, Gretch, you don't have to do that.

GRETCHEN: Do what?

FLOYD: You look good.

RETCHEN: I moved back.

FLOYD: Why?

GRETCHEN: Variety of reasons. My mother's sick.

FLOYD: Sounds like the main reason.

GRETCHEN: It's up there.

FLOYD: She's a good woman. She was always good to me. She always brought me something. She came to see you every day.

GRETCHEN: SO did your mom.

FLOYD: Not every day. Christ, I been institutionalized so much the novelty wore off for her long before that.

GRETCHEN: She'd always bring cokes. You had a vanilla and I had--

FLOYD: Cherry coke. You hated vanilla.

GRETCHEN: Until I finally tried it.

FLOYD: Then you loved it.

GRETCHEN: I seem to be like that with everything.

FLOYD: Good woman, your mother.

GRETCHEN: In fact, I think I have some vanilla. I'm sure I have coke. I could make-

FLOYD: You really look good, Gretch.

GRETCHEN: I feel good.

FLOYD: Really. (Pause, disappointed.) That's good. (Pause)

GRETCHEN: Yeah, it's her heart. Mother always had problems with her heart.

FLOYD: She has a good heart, your mother.

GRETCHEN: Physically, I mean.

FLOYD: She was always good to me.

GRETCHEN: Can I offer you anything?

FLOYD: Your mind...

GRETCHEN: What?

FLOYD: ... it feels ... OK?

GRETCHEN: My mind? It's a ... nice place these days.

FLOYD: How did you do it?

GRETCHEN: Do what?

FLOYD: Get yourself together.

GRETCHEN: Time.

FLOYD: Time? Don't make me laugh.

GRETCHEN: Why?

FLOYD: Time. (Facetiously.) I don't know, maybe we have different concepts of time. Maybe there's no space in my time. Too crowded to move so therefore it doesn't move at all - because that's what it feels like!

GRETCHEN: Floyd -

FLOYD: We were in the same place at the same time. One equally as fucked up as the other. We were on the same medications.

GRETCHEN: We had different illnesses.

FLOYD: We were diagnosed with the same thing. That's how we bonded or don't you remember? Our illnesses brought us together. Time. I've been in and out of institutions for the past fifteen years. Have you?

(Pause, no response from her.) Well, have you?

GRETCHEN: No.

FLOYD: No. Still taking your medication? Answer me, are you? Or did they up it - did they up your dosage?

GRETCHEN: No, they didn't.

FLOYD: And why didn't they?

GRETCHEN: Because I'm not taking medication anymore.

FLOYD: Right. So then, tell me, how-did-you-do-it? Your mind's "such a nice place these days," such a…resort area.

GRETCHEN: Look, I'm sorry if you're upset-

FLOYD: I'm just talking loudly - I'm not as upset as I sound.

GRETCHEN: You sound like -

FLOYD: - what, I sound like what?

GRETCHEN: Like ... you're upset, because...

FLOYD: Because why?

GRETCHEN: Because ... I'm better.

FLOYD: That's not true.

GRETCHEN: That's what it sounds like.

FLOYD: Don't listen to what it sounds like!

GRETCHEN: What d'ya mean don't listen to -

FLOYD: Because I didn't mean it that way. My God, you even have that look on your face.

GRETCHEN: What look?

FLOYD: That they do.

GRETCHEN: Who? Who the hell are you talking about?

FLOYD: They'd have that look on their face - we use to imitate that look, we use to make fun of them. And now you got that look on your face, in your eyes, in the tone of your voice.

GRETCHEN: My voice?

FLOYD: That condescending voice.

GRETCHEN: I'm sorry, Floyd - I'm sorry you feel that –

FLOYD: What are you sorry for?

GRETCHEN: I'm allowed to be sorry! I'm allowed to be sorry for anything I wanna be sorry for!

FLOYD: I shouldn't be acting this way with you.

GRETCHEN: I understand.

FLOYD: You don't have to say that.

GRETCHEN: I'm not being condescending, I mean it - I understand. You think I don't remember how it feels?

FLOYD: Do you? Then why are you sorry? You have nothing to be sorry for. You look great, you sound great. Is that why you're sorry?

GRETCHEN: And I'm sorry I left.

FLOYD: Well...

GRETCHEN: And that I never wrote or called you ...

FLOYD: Wherever you went ... did you good. Maybe I should go there. Listen to me, as if there's actually a place you can fix things. Hotel Sanity. It's gotten really bad, Gretch. It's to the point where I can't go on a subway platform. I can't look at knives without my imagination using them. I see traffic-- I can't cross the street. Sometimes I run the other way. You know what it's like to not be able to cross the street? To stand there and watch old people, little kids, animals cross and there I am, paralyzed. Some days I can't even leave the house.

GRETCHEN: What does the doctor say?

FLOYD: He's sick of hearing it. You know how they get when you go on with something, over and over, for so long. They get bored, they look right through you.

GRETCHEN: I don't know what to say.

FLOYD: You always used to know what to say. You used to be so happy that somebody else felt the same way you did. We used to help each other.

GRETCHEN: God, I'm - I'm so removed from that state of mind then - then you'll say something and I'll ... I'll remember. Like what you just said. How I use to get excited when we'd talk? I felt so much comfort knowing I wasn't the only one.

FLOYD: I miss that.

GRETCHEN: I'm afraid of the things you say.

FLOYD: You didn't used to be.

GRETCHEN: I've put it behind me. I never wanna go back there again.

FLOYD: You were slicing your wrists every other week.

GRETCHEN: Horizontally, not vertically.

FLOYD: They were always repainting your room.

GRETCHEN: I always conveniently missed my pulse.

FLOYD: You attempted it - you telling me you didn't?

GRETCHEN: It doesn't matter anymore.

FLOYD: For posterity sake.

GRETCHEN: Yes, I attempted it, but -

FLOYD: No buts! I don't wanna hear any buts! There are no buts! So ... you don't see things anymore? 'Member the little people? They used to get into your head and tell you to do things?

GRETCHEN: I don't hear them anymore.

FLOYD: You still see the hands, right? The hands that would come out from under your bed?

GRETCHEN: They stopped.

FLOYD: You still forget to breathe?

GRETCHEN: No.

FLOYD: Sometimes you do, right?

GRETCHEN: Not at all.

FLOYD: Do you at least still make yourself throw up after you eat?

GRETCHEN: I'm sorry.

FLOYD: I remember how we used to comfort each other. Do you forget that too?

GRETCHEN: Of course not.

FLOYD: We were sick together.

GRETCHEN: 'Member how we thought we were aliens?

FLOYD: And we just couldn't fit.

GRETCHEN: I fit now, Floyd.

FLOYD: Despite how I'm behaving I'm ... actually very happy for you. (She hugs him.)

GRETCHEN: Let me make you that vanilla coke. We have a lot of catching up to do!

(Gretchen exits into the kitchen and fixes the drinks. Offstage) I hope I have vanilla. Yes! You're in luck. You know I drink these all the time now. Can't believe I was so stubborn, never trying it, as much as you bugged and bugged me. Then I finally try it and I'm addicted to it. (At some point Floyd quietly exits. She continues talking, oblivious that he is gone.) I swear, I'm like that with everything. Avocados. Yogurt. I'm like "no-no-no," then I can't stop eating it. (She enters, carrying the vanilla cokes.) When I think of how many things I hate that I never tried - (She suddenly stops, wondering where he is.) Floyd? (She walks across the room, looking for him.) Floyd? (She stops, realizing he is gone. She sits, still holding the vanilla cokes).
```

---

## IC-0757: Double D

- Title: Double D
- Author (byline): Jim Dalglish
- Work: 2006: The Best Ten-Minute Plays for 2 Actors
- Publisher: Smith & Kraus
- Publication date as stated: Sept 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MARY, NIGEL
- Teaser before the introduction: Yes
- Spoken words (computed): 1799
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jim Dalglish
Book: 2006: The Best Ten-Minute Plays for 2 Actors
ISBN: 978-1575255637
Publisher: Smith & Kraus
Date (Month/Year): Sept 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Tolerance is the capacity to accept and understand people who are different from you. As you become tolerant of others, you will be better able to learn from and work with a wide variety of people. This is a crucial strength of mature people, and it is essential in a healthy community.

ACTOR: At one time or another, most of us have been stereotyped -- labeled by others as dumb jocks, weird computer geeks, or flaky theater folk, for example. These stereotyped views can lead to intolerance. Many people of color or members of different religions frequently feel the cold shoulder and distant stares of intolerance from others.

ACTRESS: When this happens to you, you have a few options. You can turn the negativity inward and feel bad about yourself. You can turn it outward and be angry and bitter. Or you can try to grow.

ACTOR: In Double D by Jim Dalglish Mary and Nigel, discover the peace that can be discover through just such growth.

TOGETHER: Double D by Jim Dalglish
```

### Performance text (classify this)

```text
Lights up. N&N Women’s Shoes, an ancient, rather rundown shoe store on a neglected side street of Manhattan. The shoes displayed are top-notch, but the stores fixtures look like they had their heyday in the early 70s. Nigel, a slightly effeminate man who looks like his heyday was also in the early 70s, can be seen standing behind the cash register, reading a men’s fashion magazine - He is tall and his hair is receding. He is humming "These Boots Were Made for Walking." He glances at his watch and notices that it’s time to close. He then grabs a box of shoes from the floor and exits offstage right. He moves briskly with a bit of bounce in his step. Mary enters the shop. She is a big girl - big bones, big hair, big breasts, big ... everything. She is wearing a very fashionable, stylish dress. It looks like hell on her. She walks cautiously, like her feet hurt. As Mary enters, the lights go out - as though Nigel has turned out the lights from the back room.

MARY: Hello? (Nigel re-enters. He sees Mary and stops.)

NIGEL: Oh, boy.

MARY: Are you closed?

NIGEL: Uh-huh. (Mary begins to lose her composure.)

MARY: Oh ... uh ... Really?

NIGEL: Uh-huh.

MARY: Yes ... well ... I'm ... Oh ... (Mary begins to exit. Her feet are killing her and she’s on the verge of tears)

NIGEL: Wait a minute. (Mary turns expectantly) Is that a Galliano?

MARY: What?

NIGEL: Your dress. Is it a knockoff or did I see Naomi Campbell wear it in Bryant Park last fall?

MARY: My mother picked it out.

NIGEL: Expensive taste.

MARY: If you knew how many fittings I had to endure.

NIGEL: What's a girl like you doing in Dior? (Mary is thrown by the comment. She begins to cry hysterically)

NIGEL: What? . . . (Realizing:) Oh . . . I guess that wasn't . . . I shouldn't have ... Oh, boy.

MARY: You're right. I look like a knocked-up sow in a silk parry dress. .. Like a whole hog stuffed into in a pink satin sausage.

NIGEL: ... no ...

MARY: That's what she my mother said.

NIGEL: Then she's going blind. Because what I see before me is ...

MARY: What?

NIGEL: A very lovely woman.

MARY: I'll get out of here so you can close.

NIGEL: Wait. Can't go out like that. (He hands her a tissue. She uses it to dab her eyes.) Take a load off your ... (Regretting his word choice.) Sit down. Go ahead.

I've got nowhere to go. Believe me. That's why I'm open so late. Nowhere to go.

MARY: Thanks, (She sits) Nice shop. (Nigel looks around and smiles sadly at the irony.) Not many open this late. Believe me. I've checked.

NIGEL: Shoe emergency? (Mary plops her feet up on the Ledge in front of her chair. Her feet are enormous. This is the first time Nigel has seen her feet.) Jesus Christ!

MARY: That's what they all say.

NIGEL: What size are they?

MARY: 12 Double D ... if I'm not retaining water and I elevate my feet for an hour before I go out ...

NIGEL: Oh, boy.

MARY: My shoes are so tight they're killing me. This strap ... It's like a knife. I swear I'd be bleeding to death, if these damn things didn't completely cut off my circulation.

NIGEL: How did you manage to get them on?

MARY: My mother ... I don't even know why I call her that. She's not my mother really. She's married to my father. She did this to me.

NIGEL: How?

MARY: A tub of ice for an hour.

NIGEL: Mother of God!

MARY: There's no way you're going to my Crystal's engagement party wearing those Goddamned Birkenstocks!

NIGEL: Not with that dress –

MARY: (Renewed tears.) Ohhhh ...

NIGEL: I'm sorry ... I ...

MARY: You don't know what it's like. You don't. To be trapped ... Completely trapped by your body. I want to be pretty. Just like my stepsister. The belle of the ball.

Hell, I'm not greedy. I'll settle for just being presentable. Ahhhhhhh!!!!

NIGEL: (Struggling to take off her shoe.) The buckles are stuck.

MARY: Inside ... inside I'm beautiful, and smart, and glamorous. I feel all that. But then I look at myself in the mirror and ...

NIGEL: When does the party begin? (Nigel continues to try pull the shoes off)

MARY: I'm an hour late already. There wasn't any room for me in the limousine. But in the cab on the way to The Four Seasons, they started to throb so desperately I didn't think I could take it. I've been to every store in Midtown. One look at my feet and they all showed me the door. They're killing me. (Nigel takes out a box cutter from his back pocket in his hand.)

MARY: What are you going to do with that?

NIGEL: We'll have to cut them off.

MARY: She'll kill me!! (Nigel cuts the straps with the box cutter. He delicately removes her feet from the shoes. At first Mary is relieved)) .. . Oh ... Oh ...

NIGEL: You're free.

MARY: My feet ... the feeling is come back into my ... (Screaming:) Ahhhhhhhhh!! (He begins to rub her feet.)

NIGEL: Deep breaths ... Deep breaths ...

MARY: Ahhhhhhhhh!

NIGEL: Don't fight it. Accept the pain.

MARY: What have you done? Now what am I going to do? In twenty minutes I have to be standing in a reception line as the fat ugly stepsister of the most beautiful bride in the world.

MARY: (Beginning to enjoy the foot rub.) Oh ... oh ... oh ...

NIGEL: What's your name?

MARY: Mary.

NIGEL: I can help you, Mary.

MARY: How? Have you studied the art of Japanese foot binding or something? NIGEL:

(Irish brogue:) A little magic. (Nigel disappears into the storage room.) MARY: What?

NIGEL: I'll be right back. (Nigel disappears into the storage room.)

MARY: I'm usually not like this. I'm not. My father's wife ... I don't fit into her perfect picture of perfection. You know - thirty-five, morbidly obese, unmarried. If she could just see what I'm really like. In court during my final arguments. Or cross-examining a hostile witness. We don't get much of that in property law ... but I can be damn effective. (Nigel reappears with boxes of shoes.) And that daughter ... Can you be a size zero? Is that even possible?

NIGEL: The biggest sizes of the most fabulous shoes on Earth. (He pulls the shoes out of their boxes and presents them to Mary one at a time. It is like a religious experience for him.) Manolo Blahnik . . . Jimmy Choo . . . Ferragamo . . . Gucci . . . Pucci ... Givenchy ... Givenchy ... GIVENCHY!!

MARY: They're gorgeous! What sizes?

NIGEL: Mostly 10s and 11s ...

MARY: Won't work.

NIGEL: They're open-toed sandals.

MARY: No.

NIGEL: Come on ...

MARY: You don't know what I've been through .

NIGEL: Try. (Nigel struggles to put the sandal on Mary's foot. It doesn't fit. He tries another. It doesn't fit. He tries another.)

MARY: Oh, God ... oh God ...

NIGEL: It's not over yet. (He tries a bunch more ... to no avail. One pair left. He picks it up reverently.) The largest Ferragamo in the Western Hemisphere. (He shoves it on her foot. She cries out. She looks down at her foot. It's hopeless.)

MARY: Like trying to stuff a hippo into a thimble.

NIGEL: It's the largest shoe in the shop.

MARY: What?!

NIGEL: ... The open toes and strap extenders ...

MARY: (Picking up her sliced shoes.) My shoes!

NIGEL: ... I thought it would work. But your feet!

MARY: They're ruined! What am I going to do? She'll kill me!

NIGEL: I'm sorry.

MARY: I have nothing. I can't even get home now. What am I going to do? (She begins to cry again. He sprints into the back room.) He'll forgive me, won't he? He's always said he loves me no matter how big I am. And I've been bigger ... If you can believe that. He still loves me. She hasn't ruined that too has she? Oh, Daddy ... (Nigel re-enters, carrying a pile of old, dusty shoe boxes.) What are those?

NIGEL: Shoes. (He blows dust off the top of one of the boxes.)

MARY: They're kind of dusty, aren't they?

NIGEL: They've been in storage for a few years.

MARY: Decades? (She takes a shoe out of one of the boxes. It's a sequined pump.) Good lord.

NIGEL: A classic.

MARY: They're huge and used.

NIGEL: Very gently, very respectfully.

MARY: Whose are they?

NIGEL: A friend of mine.

MARY: She stores her shoes here?

NIGEL: A very good friend.

MARY: Why doesn't she keep them in her closet?

NIGEL: She left town ... suddenly ... about fifteen years ago. And hasn't come back since.

MARY: Is she OK?

NIGEL: A new part of her life ... afraid to look back. You get to be a certain age and your youth is just a little too hard to keep up.

MARY: It's very nice of you to keep them for her.

NIGEL: It makes me feel close to her.

MARY: That's sweet ... What's your name?

NIGEL: Nigel.

MARY: That's sweet, Nigel.

NIGEL: Shall we?

MARY: What size?

NIGEL: 14 C.

MARY: She must be very tall.

NIGEL: About my height ... in flats.

MARY: 14 C?

NIGEL: (He removes a pair from a box. It's the exact shade as Mary's dress - or they can be made out of clear vinyl.) Oh, Mary. My God, we have a perfect match!

MARY: (Clapping.) Oh! (Suddenly concerned.) But the heel!

NIGEL: What about it?

MARY: I can't. I've never worn a heel over an inch high.

NIGEL: What?!

MARY: I can't.

NIGEL: That's absurd! (He slides the shoes onto Mary's feet.)

MARY: Ahhhh ...

NIGEL: Eureka! (She tries to stand. But is very wobbly.)

NIGEL: Steady now ... (She takes a few tentative steps.)

MARY: It's like I'm walking a tightrope. (She takes a tumble.) Oh ... Oh ...

NIGEL: Are you OK?

MARY: It's impossible!

NIGEL: Nonsense. You just need to practice.

MARY: Practice? I can't even get up. (Nigel tries to help Mary stand. But she is very heavy.) I live in constant fear that I'll fall and break my hip or I won't be able to get back up. That's the worst fear ... I won't be able to get back up ... (Nigel summons some reserve of super-human strength and is able to hoist Mary up.) Thank God ... thank God. And thank you, Nigel. (She almost tumbles backward again. Nigel runs behind her and hoists her back onto her feet. Mary is very distraught.) I can't ..

NIGEL: I don't want to hear it. You just need to find that woman inside. The woman you were telling me about. That powerful, confident woman who is so strong and brave ...

MARY: ... who wears Birkenstocks every day?

NIGEL: A big, beautiful powerful woman who doesn't take shit from anyone.

MARY: Right.

NIGEL: Shut up and listen to me, Mary. (This leaves Mary dumbstruck.) You can hide behind your little property law practice and your bad eating habits and your insecurities and self-pity until you grow old and lonely or die young. Or you can take this opportunity to finally be proud of who you are. Not the woman you see in the mirror with the big hair and bigger ass ... but the woman you are inside. The powerful, brilliant, creative, audacious, fun-loving woman who takes the world by the balls and gives them a little twist.

MARY: Excuse me?

NIGEL: A woman who doesn't let anyone tell her what to do, what to eat, what to wear. A woman who is sexy and glamorous ... who's got a lot to give and knows how to give it. Whose appetite for life is as big as her heart. I want to see that woman ... that big, bold, beautiful woman. High heels? Please! That woman could strap on snowshoes for an audience with the pope and be able to pull it off in high style. Give me that woman, Mary!

MARY: OK ... (She takes a few tentative steps.)

NIGEL: Let it go, girl! You got a stick up your ass. Let it all hang out! (She moves more .freely.) Give it to me. You own this room. Let me see you own it! (She laughs and begins to strut a little) That's it, honey. Make me feel it. Give me that power. Let me feel it. Give it to me! (She really starts to get into it. She bobbles a little ... ) Just a speed bump. Nothing to worry about. (As she struts up and down the store, Mary gradually transforms into a vivacious woman ... )

NIGEL: Let me see you shake those va va's and wiggle that voom! Yeah, baby! Yeah! My bodacious baby!

MARY: (Joyfully:} My feet!

NIGEL: Feel the power? The thrill of three-inch spikes. There's a reason they're called spikes, Mary. Because they're weapons. Like two 45-caliber pistols strapped to each ankle. Power, Mary. Power. (As she struts across the room in full stride. She's beautiful.)

MARY: I can do it! I can do it! (She laughs joyfully.)

NIGEL: Piece of cake. (She looks at her watch.)

MARY: I'm late! What do I owe you?

NIGEL: What? Nothing.

MARY: But the shoes ...

NIGEL: She'll understand.

MARY: Could you thank her for me? You never told me her name ...

NIGEL: Nelly. Nelly Forbush.

MARY: That name sounds familiar.

NIGEL: A musical star ... of sorts.

MARY: Really?

NIGEL: Mostly cabaret. A few select venues down on Greenwich.

MARY: I might have seen her perform.

NIGEL: Doubt it. Long time ago. Different life. Before she got old ... and tired.

MARY: I hope she's OK.

NIGEL: She's fine. She writes occasionally.

MARY: I have to give you something ... for the shoes.

NIGEL: Nelly's an old trooper. She'd understand.

MARY: She sounds like an amazing woman.

NIGEL: Nelly? She's a sassy old broad.

MARY: (She smiles at Nigel with a twinkle in her eye.) (Directly to NIGEL:) Thank you, Nelly. (He blushes.)

NIGEL: Come back tomorrow and tell me how it goes.

MARY: (Suddenly nervous.) Oh ...

NIGEL: You can do it. They're magic shoes. They'll get you through this.

MARY: I'm a powerful woman. I'm a powerful woman. I'm a powerful woman ... (She repeats the mantra as she exits the shop.)

NIGEL: You go, girl! (After she leaves, Nigel crosses back into the room. He sees the red-sequined stiletto pumps. He holds them reverently. He removes his shoes and slowly puts them on. He revels in the act of buckling them on. He rises to his feet and poses.) (He crosses to center stage and turns his back to the audience)

(He takes off his glasses. The song "J Will Survive" plays. He turns and lip-synchs the lyrics. He has a completely choreographed routine. He's amazing. This goes on for a while.) Nelly, girl. You still got it! (He stops in front of the mirror. He squints to see himself in the mirror. He puts his glasses back on. Then he sees his reflection in the mirror and freezes. He slowly loses his posture, his poise, his presence. His shoulders droop and he looks awkward in the heels. He is back to being Nigel. He looks closer. And then he discovers Nigel again. He is surprised to discover that he likes what he sees after all.) Hello there, Nigel. (He smiles a beautiful smile.) (Lights fade.)
```

---

## IC-0758: Dr. Fritz

- Title: Dr. Fritz
- Author (byline): David Ives
- Work: Mere Mortals
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Dec 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MARIA, TOM, MARIA/DR. FRITZ
- Teaser before the introduction: Yes
- Spoken words (computed): 1359
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Ives
Book: Mere Mortals
ISBN: 0822216329
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Dec 1998
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
MARIA: is sitting behind a crude plank table made from an old door – she channels the persona of Dr. Fritz in this selection, so the actress is not playing 2 characters.

TOM: enters, bent over at the waist, holding his side and gasping in pain.

TOM: Eugh. Eugh. Eugh.

MARIA: Bendio, sinhors! Comari ta? How you are feeling todays?

TOM: Eugh.

MARIA: You want to buy a souvenirs? One of a kinds

TOM: Eugh. I'm looking for Dr. Fritz.

MARIA: Ah, Dr. Fritz can cure everything. You have a troothache?

TOM: No. Poison.

MARIA: You have been poisoned? Tsk, tsk, tsk, tsk.

TOM: Food poisoning.

MARIA: Oh, the food poisonings. But no troothache? I was foretold of a man named Pablo corning with a troothache.

TOM: I'm not Pablo.

MARIA: This is why you have no troothache.

TOM: Look. . . My name is Tom Sanders. At the hotel I talked to this man, Pedro. . . Pedro said come here and ask for Dr. Fritz.

MARIA: Ah, Dr. Fritz can cure everything. Broken bone, bullet hole, burn, amputation, housemaid's knee.

TOM: But

MARIA: Terminal diseases is more difficult.

TOM: But

MARIA: This is why they are called terminal.

TOM: But

MARIA: Ah, but are they terminal? A case for Dr. Fritz.

TOM: But-doesn't the sign say "BUTCHER"?

MARIA: You speak the languages so good.

TOM: Eugh.

MARIA: Now this is the souvenir shop of Maria and the offices of Dr. Fritz.

TOM: (pain) Jesus Christ. . . ! Is he here?

MARIA: Jesus are everywhere.

TOM: Dr. Fritz.

MARIA: Oh, Dr. Fritz.

TOM: Wait a minute. You're not Dr. Fritz. . . ?

MARIA: I am the assistant of Dr. Fritz. (laughs madly; then calm again) At the moment.

TOM: Oh God. ..

MARIA: Good! You believe in God.

TOM: No I don't believe in God.

MARIA: But sinhors, you called on God, you said, Oh God,oh God.

TOM: It was a figure of speech, okay?

MARIA: Just checking. [We hear a ringing, like a telephone.]

TOM: What's that?

MARIA: What is what, sinhors? [RING.] I hear nothings. [RING.] Maybe the food poisoning make you a little lococo. [RING.]

TOM: Don't you hear that bell?

MARIA: Oh, the bells. (picks up a souvenir doll and speaks into it like a telephone) Mushi mushi . . . Si . . . Si . . . Si . . . - Dosveedonyeh. (hangs up the doll) This was Pedro. He say you are on the way. [Tom picks up the doll and looks at it.] There is always more meat than meets the eyes meat, no?

TOM: I must have fever.

MARIA: Are you shvitzing?

TOM: I am shvitzing. Look, if I die, tell them this.

MARIA: We all will die, sinhors-God willing.

TOM: Last night I ate supper at the hotel. Middle of the night I thought I was going to die.

MARIA: You know I think this every day, but here I am. God willing.

TOM: Maria. I don't want Dr. Fritz anymore.

MARIA: No?

TOM: No. I just want to die.

MARIA: No, no, no, no, sinhors. Don't you see, the world are a great battle between the forces of the light, and the forces of the darkness. You must always stay on the side of the forces of light.

TOM: I need a doctor! [RING.]

MARIA: (picks up the doll and speaks into it) Bonjour. Si. Si. Si. Si. No. Ciao. (hangs up) This was God. He say you should believe in him.

TOM: Where is he?

MARIA: God? Upstairs.

TOM: I'm getting out of here. (starts out, but is stopped by pain) Eugh.

MARIA: Ah, but where will you go, sinhors? And how will you get there in your present conditions? [Tom sinks down and lies on the floor.]

TOM: So this is where I'm going to die. I'm going to die here, I'm going to die here, I'm going to die-!

MARIA/DR. FRITZ: (German accent) Quiet! You miserable dog! You spineless beast!"

TOM: What...?

MARIA/DR. FRITZ: Shut up, you confounded worm! Or else die! Go ahead! Die! What does it matter to me?

TOM: What's going on here. . . ?

MARIA/DR. FRITZ: (German accent) "I am dying, I am dying!" Ja, ja, perhaps you are dying. If I can shtop this dying I vill shtop it. I am not a magician. I am a physician. But you must listen, ja? You are listening? Ja?

TOM: Ja.

MARIA/DR. FRITZ: Gut. I am Dr. Fritz Ringsvwant'l. How do you do. So. Get up.

TOM: What?

MARIA/DR. FRITZ: Shtand up on your footses.

TOM: I-I can't. . .

MARIA/DR. FRITZ: Get up, you lazy pig! Move! Move!" [Tom gets up.] I can't get up! You people. Too many Coca-Colas, it has eaten your brains. You haff no will anymore. Too much of ze French fries nut ketchup at ze Golden Arches von McDonald's. (looks in each of Tom’s eyes quickly) Zoo You haffze conztipation zometimes, ja?

TOM: I do have the constipation sometimes.

MARIA/DR. FRITZ: Und zometimes maybe you get a little prickly shtinging pain just behind ze Ellenbogen, hier, hmm? (“Ellenbogen" is "elbow.")

TOM: I do get a little prickly pain right there.

MARIA/DR. FRITZ: Und you haff ze very ugly dandruff. You must use Head und Shoulders. Giff me your hand! Schnell! (takes Tom’s hand and feels the pulse) Your pulse is normal.

TOM: You're not wearing a watch.

MARIA/DR. FRITZ: Your eyesight is excellent. Open your mouth. Stick out your tongue. Go like this. [He makes a raspberry. Tom does too.]

No, like this. [Another raspberry. Tom does too.] Better. Now put your fingers in your ears. Can you hear me?

TOM: What?

MARIA/DR. FRITZ: Good. (slaps him on the top of the head)

TOM: Ow!

MARIA/DR. FRITZ: Ziss is a poor country, Meine Herren. I haff nothing here! Nothing! (feels Tom's forehead quickly) Besidesyou haff no fever. You are sure you haff no troothache!

TOM: I DON'T HAVE A TROOTHACHE!

MARIA/DR. FRITZ: Just checking. But at four you had ze rheumatic fever. Ja?

TOM: I did have rheumatic fever. . .

MARIA/DR. FRITZ: At fifteen you had a rash on your butttocks in ze shape of Santa Claus. At twenty you had rhinitis, bronchitis, conjunctivitis, and gonorrhea-a busy year for you. At twenty-two you had ze doppel pneumonia and you thought you were going to die.

TOM: Wow.

MARIA/DR. FRITZ: VOW indeed. You zleep every day from 12:34 to T 38 in the morning. You eat usually eggs and toast mit raspberry shmier for breakfast, ze garbage fast food for lunch, maybe ze wiener made from pig balls or a slice of Scheisse you call pizza. At ze nighttimes you eat in a restaurant, sometimes Chinese, sometimes Italian, you haff ze gnorchis mit mushrooms und ze shmall green zalat.

TOM: Amazing.

MARIA/DR. FRITZ: Ziss is your entire shtupid life.

TOM: So what's wrong with me?

MARIA/DR. FRITZ: (Dr. Fritz straps Tom to the table.) I haff no idea. Lie down.

TOM: How do you know all these things about me?

MARIA/DR. FRITZ: I am a highly qualified sturgeon.

MARIA/DR. FRITZ: Zympathetic reaction. You vant to buy a zoovenirs?

TOM: No.

MARIA/DR. FRITZ: Vun ofa kinds. (Maria/Dr. Fritz lays the doll on Tom's sternum.)

TOM: OWW!

MARIA/DR. FRITZ: Your case is not so complicated. You need an operation.

TOM: An operation. . . ?

MARIA/DR. FRITZ: Immediately.

TOM: You're kidding. Not here. Not in this town.

MARIA/DR. FRITZ: You zee another town? (produces some ugly-looking butcher knives) Unfortunately, I haff not the proper tools. . .

TOM: (struggling in the bands) No. No ...!

MARIA/DR. FRITZ: I haff no anaesthetic; ziss could be quite painful. (starts sharpening one of the knives)

TOM: But I'm fine! I'm fine!

MARIA/DR. FRITZ: Fine? Nein.

TOM: Put that thing down!

MARIA/DR. FRITZ: Okay. You are fine? Then good. (undoes the straps) Go. You are free. I am not a torturer, I am a doctor. So go. Go! Tom gets up, turns and starts to go, but is stopped by a sudden pain that drops him to his knees.

TOM: Eugh. Eugh. Oh God. . . !

MARIA/DR. FRITZ: You believe in God? Do you not realize the place you have come to? The forces arrayed vhich could crush you like a peanut? Tom whimpers. Thunderclap. You have finished your good works, I hope.

TOM: No! I haven't done anything! I've eaten hot dogs made from pig balls and I had a rash on my butt and that’s it.

MARIA/DR. FRITZ: This is not very much. Alas, now ze great battle is joined, Meine Herren, and you are in the middle of the field. Ze forces of light and ze forces of darkness are fighting for you. I only hope zatt you vill find your way to the forces of light very very soon.

TOM: But how?

MARIA/DR. FRITZ: Good kvestion. RING Ogh. Ziss doll has been ringing off ze hook all day. (picks up the doll and speaks into it:) Pronto. Si. Si. Si. Si. (to Tom) It is for you.

TOM: For me . . . ?

MARIA/DR. FRITZ: Ja. God vants to talk to you. [Tom makes a gesture to say: "I'm not here."] Here. Take it. Be nice. Ziss iss God.

TOM: (takes the doll and speaks into it:) Hello...? Yes, this is he . . . Fine. Actually, I'm not feeling so fine, I have a pain in my . . . (realizing the pain is gone:) Well, I thought I had a pain. . . But you know, it's kind of amazing talking to you like this, so listen, urn, God, while I've got you on the line-no, no, no, I understand, you've got other things. I just thought I'd get in a few questions. You know-meaning of life, your general take on things, etcetera. So great. I'll see you later-much later. I hope. Nice talking to you. 'Bye. (puts the doll down)

MARIA: (Hispanic again, knitting) You are feeling better? How you are feeling, sinhors?

TOM: I feel fantastic. . . !

MARIA: That so nice. (holds up doll) Souvenirs?
```

---

## IC-0759: Dr. Horrible’s Sing-Along Blog (The Book)

- Title: Dr. Horrible’s Sing-Along Blog (The Book)
- Author (byline): Joss Whedon, Maurissa Tanchareon, Jed Whedon and Zack Whedon
- Work: Not specified
- Publisher: Titan Books
- Publication date as stated: March 2011
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: DR. HORRIBLE, MOIST, DR. HORRIBLE & CAPTAIN HAMMER, CAPTAIN HAMMER, PENNY, BAD HORSE CHORUS, MALE ANCHOR, FEMALE ANCHOR, MAYOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1266
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joss Whedon Maurissa Tanchareon, Jed Whedon and Zack Whedon
ISBN: 978-1848568624
Publisher: Titan Books
Date (Month/Year): March 2011
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Wait. . . Wait . . . Wait . . . Before we get going, think about something. Just what is it that makes a superhero “SUPER”? Is it their powers?

ACTOR: If that was the case, Batman wouldn’t be considered much of a superhero, would he? No!

ACTRESS: The key to every great superhero is an equally great, yet undeniably evil, supervillain.

ACTOR: Batman and . . . the Joker!

ACTRESS: Superman and . . . Lex Luthor!

ACTOR: Exactly! And the bottom line is that unless you can fly on your own or shoot webs out of your hands, gadgets are a key component to being a superhero or supervillain.

ACTRESS: Gadgets can mean the difference between saving the world,

ACTOR: Achieving world domination, (evil maniacal laugh)

ACTRESS: Or simply winning the affection of the girl with the big heart and wonderful hair.

ACTOR: Dr. Horrible’s Sing-Along Blog (The Book)

ACTRESS: Featuring the script and songs by Joss Whedon, Maurissa Tanchareon, Jed Whedon and Zack Whedon Dr. Horrible is in the lab working on The Freeze Ray (played by Actress). He adjusts various levels and dials, and powers the system up. It appears that it will work, but then abruptly powers down with a message synthesized message [INSUFFICIENT WONDERFLONIUM] *words not in original script, used for transition purposes*
```

### Performance text (classify this)

```text
Suggested Roles: Actress: Moist, Captain Hammer, The Freeze Ray, Penny, Bad Horse Chorus, Female Anchor

Actor: Dr. Horrible / Billy, Male Anchor, Mayor

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Dr. Horrible’s Lab – Moist is setting up the camera for Dr. Horrible’s taping. She counts down to LIVE . . . 3, 2, 1 . . . and exits. Dr. Horrible dons a lab coat, gloves and goggles that rest on his forehead.

DR. HORRIBLE: (Pg 16) (laughs an evil, maniacal laugh into the camera) AH-ah-ha-ha-ha-ha!!! Ah – HAH-haha-ha . . . (pause) So that’s, you know, coming along . . . You don’t get into the Evil League of Evil without a memorable laugh. No response BTW from the League yet, but fingers crossed . . . (Pg 16) This world is a mess and I just need to rule it. (shuffles through schematics and disassembled electronic devices) The Freeze Ray is almost up! This is the one. Stops time. Freeze Ray. Heard it here first! (MOIST enters) (Pg 19) Moist! My evil moisture . . . buddy. What’s going on?

MOIST: (Pg 19) Hey Doc. Got your mail.

DR. HORRIBLE: (Pg 16) (takes mail from Moist, which leaves a long trail of icky moisture. He leafs through it and rips open a letter – to camera) Oh, great. Our old friend Johnny Snow. “Doctor Horrible, I see you are once again afraid to do battle with your nemesis . . .” Dude. You’re not my nemesis. My nemesis is

DR. HORRIBLE & CAPTAIN HAMMER: Captain Hammer.

CAPTAIN HAMMER: (Poses in standard Superhero pose) (Pg 27) A man’s gotta do what a man’s gotta do! Captain Hammer’s here, hair blowing in the breeze. (the classic hair flip)

DR. HORRIBLE: (Pg 16) Corporate tool. Dislocated my shoulder – again – last week.

MOIST: (Pg 21) You need anything. . . dampened, or made soggy?

DR. HORRIBLE: (Pg 16) Thanks, but . . . (opens another letter) DeadNotSleeping writes “ . . . You always say in your blog that you will show her the way. Who is ‘her’ and does she even know that you’re . . . “ (He falls silent, mouthing the beginning of a response . . .) ***** SCENE CHANGE – LAUNDROMAT *****

(Pg 18-19) (Cut to scene with Dr. Horrible in street clothes, obviously the same guy, but goes by the name Billy, enters a laundromat with a bunch of laundry. He sees Penny, vocalizing while doing her laundry clearly “the girl.”)

DR. HORRIBLE: (lyrically to the same tune Penny is vocalizing as he begins to do his laundry – both should continue pantomime laundry activities in coordination through this sequence) Laundry day. See you there. Wanna say . . . Love your hair. Here I go . . . (Mumbling an awkward introduction, then returns to lyrical monologuing) With my freeze ray I will find the time to find the words to . . . What’s the phrase . . . (to Penny) Love your hair!

PENNY: What?

DR. HORRIBLE: (embarrassed) No – I just . . . love the . . . the . . . AIR . . .

DR. HORRIBLE: (Pg 21) Are you kidding? (Dr. Horrible is frustrated, he rapidly flips through a sheaf of papers and his frustration turns to excitement) This is great! I’m about to pull a major heist. The Wonderflonium I need for my Freeze Ray? It’s being transported tomorrow.

***** SCENE CHANGE – STREET ON THE DAY OF THE HEIST *****

Penny is handing out flyers for the Caring Hands Homeless Shelter. Dr. Horrible has just hijacked the Wonderflonium and is carrying it in a small duffle-bag.

PENNY: (Pg 22) (lyrically) Will you lend a caring hand to shelter those who need it? (She reacts to a negative response) No? How about you? (she approaches Dr. Horrible from behind . . . lyrically) Will you lend a . . .

DR. HORRIBLE: AHH! (realizes it is Penny and tries to play it cool) (Pg 24-26) Ahh. Hah. What?

PENNY: Hey, I know you.

DR. HORRIBLE: You know me? Cool. I mean, yeah. Do you?

PENNY: From the laundromat.

DR. HORRIBLE: (nodding) Wednesdays and Saturdays, if that was you. It could be someone else, I mean I’ve seen you. Billy is my name.

PENNY: I’m Penny. I’m out here volunteering for the Caring Hands Homeless Shelter. Can you spare a minute?

DR. HORRIBLE: (peers over his shoulder stealthily, then reluctantly) Okay. Go.

PENNY: If we get enough signatures (motions with her clipboard) There’s a great building nearby that the city’s just going to demolish and turn into a parking lot.

DR. HORRIBLE: (disparagingly) Signatures.

PENNY: Yeah. We’d be able to get people off the streets and into job-training. (Doc’s attention has wandered to his Wonderflonium) You’re not really interested in the homeless are you?

DR. HORRIBLE: (dismissively) They’re a symptom. (his speech turns progressively more sinister) The disease consumes the human race while you’re getting signatures. I’m talking about an overhaul of the system. Putting the power in . . . (starts his maniacal laugh while wringing his hands, but turns it into a cough, then speaks more softly while opening his hands beseechingly) DIFFERENT hands.

PENNY: (beat) This petition is about the building.

DR. HORRIBLE: I’m sorry. I come on strong. I’d love to sign (he does so) Can’t turn my back on a fellow laundry person.

PENNY: (moving off) I’ll probably see you there . . . (Dr. Horrible deflates as he realizes he’s blown his meeting with Penny)

DR. HORRIBLE: Why did she talk to me NOW? ***** SCENE CHANGE – DR. HORRIBLE’S LAIR / WEB BLOG *****

Dr. Horrible’s Lab – Moist is setting up the camera for Dr. Horrible’s taping. She counts down to LIVE . . . 3, 2, 1 . . . and exits.

DR. HORRIBLE: (Pg 40-41) (Actress portrays the Freeze Ray) All right. The wait is over. With the addition of Wonderflonium, which I obtained at my famously successful heist, this, my friends, is my Freeze Ray. As of tonight, if all goes according to plan, I am in the Evil League of Evil. (evil laugh as he exits)

(Pantomime sequence of a battle between Dr. Horrible and Captain Hammer. The Freeze Ray doesn’t work properly and Dr. Horrible is defeated)

DR. HORRIBLE: (turns on webcam again. He is limping, is battered and bruised and a little emotionally fragile. He clears his throat) The Freeze Ray needs work. I also need to be more careful about what I say on this blog. Apparently the LAPD and Captain Hammer are among our viewers. They were waiting for me at the Mayor’s dedication of the Superhero Memorial Bridge. The Freeze Ray takes a few seconds to warm up and I wasn’t . . . Captain Hammer threw a car at my head. (Cell phone rings, he answers)

BAD HORSE CHORUS: He saw the operation you tried to pull today. Your humiliation means he still votes “neigh.” Go kill someone. Signed: Bad Horse.

MOIST: (who has been eavesdropping) Kill someone?

DR. HORRIBLE: Would you do it, to get into the Evil League of Evil?

MOIST: (Pg 42) Look at me. I’m Moist. I make people feel like they want to take a show. I’m not E.L.E. material.

DR. HORRIBLE: Killing’s not elegant or creative. It’s not my style.

MOIST: You’ve got more than enough evil hours to get into the henchman’s union.

DR. HORRIBLE: (waves off the idea) I’m not a henchman. I’m Dr. Horrible. I’ve got a PhD in horribleness.

MOIST: (beat) Is that the new catch-phrase?

DR. HORRIBLE: I deserve to get in. You know I do . . . but killing? Really? ***** SCENE CHANGE – LAUNDROMAT ***** As they do routine laundry activities . . .

DR. HORRIBLE: (Pg 39-40) So how was your weekend? Did you spend the whole time hunting wild signatures?

PENNY: Actually, I went on a date.

DR. HORRIBLE: (smiling through it) Get outta town. How was it?

PENNY: (hoping to make him jealous) Unexpected. He’s a really good-looking guy. (Pg 44-46) He’s nice. I’ll be interested to know what you think of him. He said he might stop by.

DR. HORRIBLE: (sudden panic) Stop by here?! (he checks the time on his bare wrist) Wow. Goodness. Look at my wrist. I have to go. (Starts to exit)

PENNY: What about your clothes?

DR. HORRIBLE: (quickly spins to check a washer, lifts the lid and looks in) I don’t love these. See ya! (He spins and walks face first into . . )

CAPTAIN HAMMER: Billy, the laundry buddy. You look Horribly familiar. Have I seen you at the gym. (Flexing his muscles)

DR. HORRIBLE: (of course!) At the gym!

CAPTAIN HAMMER: Who wants to know what the Mayor is doing? He is signing over a certain building to a Caring Hands group as a new homeless shelter.

DR. HORRIBLE: (to Penny, sincerely, but defeated) Congratulations.

PENNY: I can’t Believe it! Thank you. THANK YOU! (washer buzzes and Penny moves away)

DR. HORRIBLE: Well, this is great. I wish I could stay and chit-chat.

CAPTAIN HAMMER: (he knows exactly who “Billy” is) You’ve got a little crush, don’t you, DOC? That’s gonna make it hard to hear this. Later on, I’m going to take little Penny back to my place. I’m gonna give her the night of her life just because you want her. And I get what you want. See, Penny’s with Captain Hammer. And these (holds up his fists) are not the hammer. (Gives Dr. Horrible a suggestive look) The Hammer is . . . (Dr. Horrible reacts with revulsion as The Hammer exits)

***** SCENE CHANGE – DR. HORRIBLE’S LAIR *****

Moist is working in the lair and is shocked when Dr. Horrible arrives. His responses are comedic, but wordless.

DR. HORRIBLE: (Pg 47-48) (he is beside himself with anger – ranting against Captain Hamme) All the times that you beat me unconscious. All the crimes incomplete! Mr. Cool. Mr. Right. Mr. Know-It-All is through! I’m gonna shock the world. Gonna show Bad Horse. [TRANSITION

(these words are not in the script: Moist, Bring my Freeze Ray] (Dr. Horrible and Moist get to work, furiously modifying the FREEZE RAY to a DEATH RAY. Once the modification are complete, Dr. Horrible motions Moist to stand a few steps away. He tests the new Deah Ray. Moist dies and Dr. Horrible laughs maniacally) It’s a brand new day. And Penny will see the evil me. Not a joke, not a dork, not a failure. Captain Hammer . . . You’re gonna die! (he exits)

***** SCENE CHANGE – DEDICATION OF THE NEW HOMELESS SHELTER *****

MALE ANCHOR: (Pg 52) The mayor himself will be on hand to dedicate the new homeless shelter and unveil the statue of Captain Hammer.

FEMALE ANCHOR: (laughing) It’s a good day to be homeless! (cut to Mayor)

MAYOR: (Pg 58) Ladies and Gentlemen, your hero.

CAPTAIN HAMMER: (leaps onto stage, arms extended wide) Thank you, Mayor for those kind words. (reading from index cards) I hate the homeless (next card) –ness that plagues our city.

Everyone should have . . You know what? I don’t need tiny cue cards (tosses them on the ground)

DR. HORRIBLE: (Pg 60) (suddenly appears from the crowds, he lets out his perfected, evil maniacal laugh) (Pg 62) Heros are over with. It’s Doctor Horrible’s turn. (He powers up his Death Ray, then hesitates) Here goes – No mercy. (the device powers up, then suddenly runs out of power – audible energy-drain) Thaaat’s not a good sound . . . (Captain Hammer punches him on the jaw, sending his Death Ray flying out of his hands – a fist fight ensues, with Captain Hammer easily beating Dr. Horrible. The fight should be comical. Once Dr. Horrible is defeated, Hammer retrieves the Death Ray and returns to lord it over Dr. H.)

CAPTAIN HAMMER: A Death Ray? Dr. Horrible’s moving up. Let’s see if this one works any better than your others. (He points it toward Dr. Horrible’s head) (Pg 64) Give my regards to St. Peter. Or whoever has his job, but in Hell.

DR. HORRIBLE: Don’t!!! (the Ray explodes sending shrapnel everywhere)

PENNY: (Pg 65) (is hit by the shrapnel, she takes one piece to her chest and one to her stomach, she is having trouble breathing)

DR. HORRIBLE: (moves quickly to Penny) Penny. No. No. Hold on. Hold on –

PENNY: It’s okay. It’s okay, Billy. Are you all right? (trying to smile) Captain Hammer will save us. (she dies)

DR. HORRIBLE: Penny?!? (long pause as he realizes what he has done) Here lies everything. The world I wanted at my feet . . . (Pg 41) (echo of a memory) As of tonight, if all goes according to plan, I am in the Evil League of Evil. (Pg 42) I deserve to get in. You know I do . . . (sad evil laugh) (Pg 65) Well, we all have a choice . . . (with fake bravado) and I am fine.
```

---

## IC-0760: Dr. Seuss' The Lorax - Screenplay

- Title: Dr. Seuss' The Lorax - Screenplay
- Author (byline): Paul Cinco and Ken Daurio
- Work: Not specified
- Publisher: Dr. Seuss Enterprises, L.P. Original screenplay can be purchased from Scriptfly.com
- Publication date as stated: 2012
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS, ACTOR, LORAX, MAN, WESLEY, DELIVERY MAN, WOMAN, SUNBATHER, SUNBATHER 2, TOGETHER, TED, AUDREY, MOM, GRAN, MARKETING GUY 1, MARKETING GUY 2, O’HARE, ONCE-LER, YOUNG ONCE-LER, TEEN GIRL, BOY, FAT GUY, MARIE, DAN, ROSE
- Teaser before the introduction: Yes
- Spoken words (computed): 1535
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paul Cinco and Ken Dario
ISBN: N/A
Publisher: Dr. Seuss Enterprises, L.P.
Original screenplay can be purchased from Scriptfly.com
Date (Month/Year): 2012
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: In 1971, one year after the US Environmental Protection Agency was established, Theodore Geisel, aka Dr. Seuss published The Lorax as a cautionary fable.

ACTRESS: In 2012 that fable was re-imagined for film, reaching a new generation of children with a very dire message.

ACTOR: Now it is 2025, and it seems our leaders have forgotten the message yet again.

ACTRESS: This year, the Trump administration has moved to rescind longstanding forest protections, opening nearly 59 million acres of national forest to logging.1

ACTOR: And his executive orders have reduced environmental oversight and relaxed endangered-species safeguards.2

ACTRESS: Today with this performance, we speak for our trees, our environment and our planet.

ACTOR: Dr. Seuss' The Lorax Screenplay

ACTRESS: By Paul Cinco and Ken Daurio
```

### Performance text (classify this)

```text
(based on the book by Dr. Seuss, aka Theodore Geisel)

Suggested Roles:

ACTRESS: Lorax, Wesley, Woman, Sunbather, Audery, Mom, Gran, Marketing Guy; Once-Ler, Teen Girl, Marie, Rose

ACTOR: Man, Delivery Man, Sunbather 2, Ted, Marketing Guy 1, O’Hare, Young Once-Ler, Boy, Fat Guy, Dan

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

LORAX: (Pg 2) (clears his throat and reads from a card) I am the Lorax. I speak for the trees. Regarding the story that you're about to see: it actually happened, just take it from me. We open in Thneedville, a city they say that was plastic and fake, and they liked it that way! A town without nature, not one living tree.

Busy activity in Thneedville as its citizens start the day.

MAN: (Pg 2) (using a bike pump to inflate plastic trees/bushes) FLOOSH! FLOOSH! POP! FLOOSH! FLOOSH! POP!

WESLEY: (Pg 4) (swimming, he climbs out and dries off) I went swimming and now I glow!

DELIVERY MAN: (Pg 3-4) (carrying a large air tank on his shoulder) In Theedville the air’s not so clean. (knocks on door) O’Hare Air!

WOMAN: (opens the door; she looks like she’s smelled something rancid) So we buy it fresh!

(puts on oxygen mask attached to the air tank and takes a whiff) Aaaaaah!

DELIVERY MAN: We don’t want to know where the smog and trash and chemicals go!

SUNBATHER: (Pg 5-6) We thank the Lord for all we’ve got--including this new parking lot!

SUNBATHER 2: Parking lot! Parking lot!

WOMAN: (excited as if she’s seen a celebrity) It’s him! (squeals) It’s Aloysius O’Hare, the man who found a way to sell air (takes another hit from her oxygen mask) and became a zillionaire! (O’Hare waves to crowd from a massive TV screen; think Times Square)

TOGETHER: Hip-hip-hooray! Hip-hip-hooray! *****

TED: (Pg 7-9) (rings the doorbell of his neighbor, Audrey’s house – multiple times. While he waits for her to answer, sprays breath freshener into his mouth, and tries to tame his unruly hair)

AUDREY: (opens the door) Oh, hi, Ted. Did your ball land in my backyard again?

TED: (playing it cool) Oh, hey, Audrey. Hi. No. Model airplane this time.

AUDREY: Hey, do you want to see something cool? Come on. (leads him to look at a massive mural she is painting of a valley filled with Truffula trees)

TED: (staring up in awe) Whoa! Did you... Did you paint this? This is amazing! What are those? (pointing to the trees)

AUDREY: (smiling) Those are trees. Real ones. They used to grow all around here. People said the touch of their tufts was softer than anything, even silk. And they smelled like butterfly milk! (beat) What I want more than anything is to see a real living tree!

TED: So if... I'm just thinking out loud here. If a guy somehow got you one...

AUDREY: I'd probably marry him on the spot! (Ted smiles to the audience – he has a plan)

***** Ted’s House *****

TED: (Pg 10-13) So, Mom, do you happen to know if there's any place where I could get a real tree? -- one that grows out of the ground or whatever.

MOM: We already have a tree. It’s the latest model. (makes a face) You would rather have some dirty, messy lump of wood that just sticks out of the ground? I don't even know what it does. (proudly as she turns the lights on a fake tree in their yard) We've got the Oak-amatic. (commercial-style) The only tree with its own remote! (clicking the remote) Summer . . . Winter . . . and DISCO!! (sings and dances to *“The Hustle”) Doot doot doot doo-doot doo-doot doot doot!

TED: (mortified) Mom! Stop!!! (mom clicks the remote and stops, disappointed) Let's just say I need a tree. Where would I go?

GRAN: You need to find the Once-ler. [He] is the man who knows what happened to the trees. People used to say if you brought him 15 cents, a nail and the shell of a snail, he’d tell you everything . . . ****** O’Hare Air Offices *****

MARKETING GUY 1: (Pg 14-16) Mr. O’Hare, we’ve got something that is going to take O’Hare Air to the next level.

MARKETING GUY 2: I know what you’re thinking. 1) I’ve gotten rich selling people air that’s fresher than the stinky stuff outside. 2) How could I possibly make even more money? (laughs) We can tell you, sir!

MARKETING GUY 1: (holding up a plastic bottle) O’Hare Purified Air! (both open bottles and blow air into their mouths) Oh, yeah!

MARKETING GUY 2: Oh, yeah! Freshness to go!

TOGETHER: (taps bottles together, then as if in a commercial) Please breathe responsibly.

O’HARE: (beat) You gotta be kidding me! You really think people are stupid enough to buy this?!

MARKETING GUY 1: Our research shows if you put something in a plastic bottle, people will buy it. And when we build a new factory to make plastic bottles, the air quality’s going to get worse.

MARKETING GUY 2: Which will make people want our air even more and drive sales through the roof! ****** The home of the Once-ler***** (Pg 18-24) Ominous sound effects. The wind whistles. Someone is watching him from inside through a boarded up window.

TED: (getting more nervous with each step, arrives at the door, takes a deep breath and moves his shaking finger toward the doorbell)

ONCE-LER: (throwing open a window) Who are you?!! And what are you doing here?!

TED: (startled) Aaaaahhhhhh! I’m Ted. I’m Ted! (out of breath) Oh, can’t breathe. Are you – are you . . .the Once-ler? Oh, man.

ONCE-LER: No one is supposed to come here! Leave me alone!

TED: (regaining some composure, he holds out his hands full of change, a nail and a snail) Listen, people say that if someone brings you this stuff, you’ll tell them about trees. Real ones that grow out of the ground!

ONCE-LER: (long beat) Sorry, it’s just . . . well, I didn’t think anyone still cared about trees.

TED: Well, that's me. The guy who still cares. I'm here.

ONCE-LER: Do you want to know about trees? Why they're all gone? It's because of me. And my invention, the **Thneed. (holds up a Thneed) It all started a long time ago . . . *****flashback story*****

YOUNG ONCE-LER: Well, here I go, Mom. Off to change the world with my Thneed!

ONCE-LER: So there I was, searching the globe, obsessed with finding the perfect material.

YOUNG ONCE-LER: (singing) Na na nana na na, Oh bop-bah-da-da-do-do-do, Thneed – Thneed – Thneed, La-la-la-la-la . . .

ONCE-LER: One day I found paradise.

YOUNG ONCE-LER: Whoa! (looks around in awe) This is the most beautiful place I have ever seen. This is the place! These Truffula Trees are just what I need! (puts on work gloves and grabs a large axe) Gonna chop one down and make my Thneed! (Pg 28) About to change the world! (the phrase is echoed multiple times by both actors as he begins chopping down the tree)

ONCE-LER: Little did I know that by chopping down that tree I had summoned a mystical creature as old as time itself. The legendary – slightly annoying – guardian of the forest (beat) The Lorax!

LORAX: (Pg 29-30) (appears in a hail of lightning and thunder in disbelief and anger) What the – Who the – Oh! Hey! Did you chop down this tree? Leave! Take your axe and get out!

YOUNG ONCE-LER: Who are you?

LORAX: I’m – I’m the Lorax! I speak for the trees. You didn’t see me magically appear out of that stump? (Pg 32) (to audience) Behold the intruder and his violent ways! (to Once-ler) Shame on you!

YOUNG ONCE-LER: Listen to me, you furry meatloaf. I’m gonna chop down as many tress as I need. News flash, not going anywhere! (sticks his tongue out and does raspberries) (Pg 53) (packing up for town the next day) Oh, yeah. I got a little jingle, gonna sell some Thneeds! (put one on his head, one around his shoulders, one on a pair of pants and swings the others around his head like a lasso) (now he’s at a makeshift booth in the center of town, hawking his Thneeds) (Pg 52) This will change the world as we know it! It’s a swimsuit! Hup-hey-oh! It’s a hat! (Pg 53) (singing) Everybody needs a Thneed; a fine thing that all people need. (taking money and handing out product)

TEEN GIRL: (Pg 55) Oh my gosh, I totally want one!

BOY: (Pg 57) It’s a net for catching butterflies! (demonstrates)

FAT GUY: A thing you use for exercise! (demonstrates)

TOGETHER: (chanting) The Thneed is good! The Thneed is great!

YOUNG ONCE-LER: (Pg 58) (on the phone) Mom! I told you I was gonna be a success. We’re gonna be rich! (to audience) (Pg 74-75) All the customers are buying! Who cares if a few trees are dying? (Pg 77) I intend to keep on turning Truffula trees into Thneeds! And nothing is going to stop me!

ONCE-LER: (long beat . . . then sadly) (Pg 61) It was all downhill from there . . . *****End Once-Ler’s Fashback****

TED: (Pg 79) So this is really all your fault. You destroyed everything!

ONCE-LER: Yes. And each day I’ve sat here regretting everything I’ve done. But now I’m thinking . . . (he rummages around and tosses something to Ted) The last Truffula Seed. (beat) You need to plant it, Ted. ****Flashback to town earlier that day****

O’HARE: (Pg 39) (broadly) Oh, Teddy. I hear you’ve become interested in trees.

TED: (nervously) Where’d you hear that?

O’HARE: (smiling) There’s not much that goes on in Thneedville that I don’t know about. (beat) Here’s the deal. I make a living selling fresh air to people. Trees, they make it for free. So, when I hear people talking about them, I consider it a threat to my business. (growls) Listen to me, boy. Don’t go poking around in things you don’t understand. ****End Ted’s Flashback****

TED: (Pg 79) But nobody cares about trees anymore. TOGETHER as TOWNSPEOPLE: (Pg 6) Parking lot! Parking lot!

ONCE-LER: (Pg 79-80) Then make them care. Plant the seed in the middle of town where everyone can see. Change the way things are.

TED: (dials Audrey’s number frantically) (Pg 86-87) Audrey! [I have] the last Truffula seed. And you’re going to help me plant it right in the middle of town. Where everyone can see it. Let’s go!! (he rushes off to the town center) (Pg 93) Okay, we have to get this in the ground.

AUDREY: But where? There’s no dirt anywhere! (stomps on the pavement)

TOGETHER as TOWNSPEOPLE: (Pg 6) Parking lot! Parking lot!

WOMAN: (Pg 93-96) What do you think you’re doing, kid?

TED: Um . . . I’m looking for a place to plan a tree. A real one!

WOMAN: (takes a whiff from her air tank) Why would we need a tree?

O’HARE: (enters) Exactly! Folks, the last thing you want around here is trees. They’re filthy, spewing that sticky, nasty sap all over the place. They bring poisonous ants and stinging bees. And . . . I just thought of, you know, they make leaves! I mean, you know that right?! And these leaves, they just fall. They just fall wherever they want.

AUDREY: (loudly) Oh, come on! We know why you’re REALLY against trees! Because they produce fresh air!

TED: For free!

O’HARE: (gasps) I am wounded! You have lied!

AUDREY: It is not a lie! It’s called photosynthesis!

O’HARE: She’s making that up! That’s a made up word, people! We don’t need trees! (points at Ted) That boy has a seed! We need to stop him! Who’s with me?

DELIVERY MAN: O’Hare’s right! Seeds will ruin us all!

WOMAN: (takes a whiff from her air tank) Yeah! Grab him!

TED: (Pg 97-99) (climbs to the top of a wall) I am Tedd Wiggins. (beat) I speak for the trees. (beat) And the fact is things aren’t perfect here in Thneedville and they’re only going to get worse unless we do something about it. And we can start by planting this!

(holds up the seed)

MARIE: (undeniable cuteness) My name’s Marie, and I am three. I would really like to see a tree! I say let it grow!

TOGETHER: (reacts to her cuteness) Awwwwwww!

DAN: My name is Dan

ROSE: And my name’s Rose

TOGETHER: Our son Wesley kind of glows. And that’s not good, so we suppose we should let it grow!

GRAN: I’m Granny Norma, I’m old and I’ve got gray hair, but I remember when trees were everywhere. And no one had to pay for air. So I say let it grow!

O’HARE: My name’s O’Hare, I’m one of you. The things you say just might be true. It could be time to start anew . . . . Naw! I say let it Die! (chanting) Let it die! Let it die!

WOMAN: (Pg 101) (takes a whiff from her air tank) It’s time to banish all your greed!

DELIVERY MAN: Imagine Thneedville flowered and treed! Let it grow!

TOGETHER: (Cheering) (long beat)

AUDREY: (utter seriousness) Unless someone like you cares a whole awful lot . . .

TED: Nothing is going to get better.

TOGETHER: It’s not!
```
