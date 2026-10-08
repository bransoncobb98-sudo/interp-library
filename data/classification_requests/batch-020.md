# Classification request: batch 20 of 63 (40 records, IC-0761 to IC-0800)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-020-reply.json`.

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

## IC-0761: Early Morning from Times of War

- Title: Early Morning from Times of War
- Author (byline): Eric Lane
- Work: Times of War
- Publisher: Dramatic Publishing
- Publication date as stated: April 2012
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: DORIS, DIAMANTINI
- Teaser before the introduction: Yes
- Spoken words (computed): 1930
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eric Lane
Book: Times of War
ISBN: 978-1583427422
Publisher: Dramatic Publishing
Date (Month/Year): April 2012
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: The year: 1994. Doris is accused of a shocking crime.

ACTRESS: Dori’s grandson Kenny has died in a hospital under mysterious circumstances.

ACTOR: Doris was the last person seen alone with her grandson, Kenny, who was dying of AIDS and who she loved dearly. She is accused of killing her grandson by suffocating him with a pillow.

ACTRESS: Doris claims she is innocent and finds herself at the center of a media frenzy. Detective Diamantini is assigned to investigate the case.

TOGETHER: Early Morning from Times of Way by Eric Lane.
```

### Performance text (classify this)

```text
Characters DORIS HANSON, sixties to early seventies. Her grandson, Kenny, has just died. Her world has been turned upside down. She is experiencing a strong range of emotions-from grief to rage to relief. She is forced to protect herself and Kenny's memory. DIAMANTINI, a detective. Working class, with a slight belly. Married, and the father of three girls. Has been on the force since his twenties. Having solved many disturbing cases, he still cares in spite of himself. A strong sense of right and wrong. While sometimes appearing casual, he drives the investigation and knows exactly what he is doing.

DORIS: In times of peace, children bury their parents. In times of war, we bury our sons.

DORIS: [Straightforward.] I did not kill my grandson.

DIAMANTINI: No?

DORIS: No. I had gotten there this morning at six-fifteen.

DIAMANTINI: [Sits.] How come so early?

DORIS: Kenny would wake up. Maybe the noise. Or just being there, in the hospital. Two and a half months this time. This time, two and a half months. If I was there, he wouldn't- He would be, well, calmer. Maybe talk. Just a few-words.

DIAMANTINI: Doris? He'd be calmer if you came. . . . You were saying-

DORIS: Kenny. Do you have any children?

DIAMANTINI: Three girls. Play the violin. I hate that instrument. All strings.

DORIS: Kenny played the piano.

DIAMANTINI: Was he good?

DORIS: [Nods.] I used to listen. I liked listening, when he played. I taught him.

DIAMANTINI: You still play? [DORIS: nods.] Me, I got no musical ability.

DORIS: Everyone has some musical ability.

DIAMANTINI: I play you sixteen bars on trumpet, you'll think different. So it's just you this morning. Alone with Kenny. You'd talk.

DORIS: [Nods.] Like every morning.

DIAMANTINI: Me, six-fifteen, I'm not saying much. That's just me. What'd you talk about?

DORIS: It was his birthday. Twenty-nine years old. I brought him a cupcake with an electric candle in it. Turned it on and sang "Happy Birthday."

DIAMANTINI: I bet he liked that.

DORIS: Blew out the candle. I helped him. Took off his oxygen mask and blew it out. He saw it was electric, but still ...

DIAMANTINI: What'd he wish for?

DORIS: I don't know. Even if I did, can't tell or it won't come true. . . . Saturn Return. You asked what we talked about.

DIAMANTINI: What's that?

DORIS: This time of big change. Once every twenty-nine years. Kenny read all about it.

DIAMANTINI: So you're in the hospital with Kenny. Two and a half months now.

DORIS: This time.

DIAMANTINI: This time, two and a half months.

DORIS: Yes.

DIAMANTINI: This morning, in his room, singing "Happy Birthday." By yourself the whole time.

DORIS: Nurses would come and go, but yes, I was there. Until I left the room at eight-thirty.

DIAMANTINI: You knew what time it was?

DORIS: I looked at my watch. It was eight-thirty. I went to the pay phone to call my daughter. Margie was at work by then.

DIAMANTINI: Kenny's mom. [DORIS nods.] And nothing seemed unusual.

DORIS: No.

DIAMANTINI: Was Kenny upset?

DORIS: He seemed calm, relaxed. He said he had a good night's sleep.

DIAMANTINI: It seems we got a couple of questions.

DORIS: What kind of questions?

DIAMANTINI: When his nurse-

DORIS: Carole.

DIAMANTINI: When Carole came in the room there was a pillow across Kenny's face. This is when you're making your call. His hands are at his side. His oxygen mask off and on the night table just out of his reach. Not impossible to reach, just slightly beyond. Do you understand what I'm asking? [DORIS: says nothing.] Nobody else was in the room. The curtain was drawn around the bed.

DORIS: People look in. You want your privacy. . . . They didn't want to let me back in the room. His doctors. I made them. Kenny lying there. It's his birthday. Saturn Return. This time when Saturn returns to the exact position when you were born.. He's gone, I think. "Who he really is is gone. And anything that follows doesn't scare me-what they say or think, doesn't matter, 'cause I know he's safe. Ask your questions, Detective. Ask away.

(SCENE BREAK)

[DORIS and DIAMANTINI address the audience. They hear what each other says.)

DORIS: There is no word. I'm suspected of a crime without a word. A son kills his mother-

DIAMANTINI: Matricide.

DORIS: A mother kills her baby

DIAMANTINI: Infanticide.

DORIS: But the thought of a woman killing her child's child. It's not even part of the language. Because no one would believe it. No one.

(SCENE BREAK)

DIAMANTINI: You're in the room. Eight-thirty. And you're heading to ...

DORIS: The pay phone.

DIAMANTINI: OK. You reach the pay phone.

DORIS: The lounge is empty-TV on but empty, and I call Margie. Nothing important, just to say hello. She sends him her love. "Tell Kenny happy birthday and I'll see him later tonight."

DIAMANTINI: So you get off the phone and head back to the room.

DORIS: Head back, only everything feels different.

DIAMANTINI: Different how?

DORIS: Outside. The hall feels like-I don't know. Movie time. Slower. Just not me, but away, and this part of me- Just this part has this feeling like- [Searches for the words, can't find them.)

DIAMANTINI: And when you get back to the room. [DORIS: looks away.) "When you get back-

DORIS: "When I get back to the room there are people. Nurses, doctors. The door's closed and I know . . . I know. In the time it took for me to call Margie and tell her everything is fine, Kenny died. And you think I did it.

DIAMANTINI: I didn't say that.

DORIS: No?

DIAMANTINI: No. I'm just trying to figure out what happened. Help me out here. I got one question. Why'd you leave the room?

DORIS: To use the phone.

DIAMANTINI: Phone in the room.

DORIS: I wasn't going to talk in front of Kenny.

DIAMANTINI: Why not? He's your grandson.

DORIS: And he's dying. Do you think I want to talk about that in front of him?

DIAMANTINI: So you're gonna walk down two long hallways. Pay twenty-five cents, when a phone's right there in the room.

DORIS: Yes.

DIAMANTINI: Doesn't add up.

DORIS: You have daughters.

DIAMANTINI: We're talking about your grandson.

DORIS: Your daughter's lying in bed, and you're watching her. Pretending nothing's wrong. Like nothing's been wrong the past three years. Watching her weight go down to ninety. Barely able to lift her head. Every morning at six-fifteen. You sit in that hospital room. You sit in that chair and watch and wait and pray and you tell me. You tell me if you'd step out of the room for five minutes.

DIAMANTINI: Maybe I would. Maybe I'd want it to end. Her suffering like that. Did you?

DORIS: Did I what?

DIAMANTINI: Want it to end?

DORIS: No.

DIAMANTINI: Sitting in that chair. Watching and waiting. Praying. You must've thought about it.

DORIS: No.

DIAMANTINI: Blowing out that candle, there must've been something you wished for. [DORIS: looks away.] Maybe he wanted it, too. Even asked you to help him.

DORIS: No.

DIAMANTINI: Three years and not once ...

DORIS: You don't think. You just do what you have to do.

DIAMANTINI: Whatever he needs.

DORIS: Yes.

DIAMANTINI: To stop the pain.

DORIS: If I could. Yes. If I could make him more comfortable. [A beat.] A miracle. [He looks at her.] You asked what I wished for. When I blew out the candle. I wanted a miracle. [A moment.]

DIAMANTINI: So that morning, Kenny makes his wish. Takes off his oxygen mask. Blows out the candle. Then puts it back on.

DORIS: Yes.

DIAMANTINI: Why not wait?

DORIS: For what?

DIAMANTINI: Me, I'd wait. 'Til later. Other people around. Presents.

DORIS: It was his birthday. I thought it might cheer him up.

DIAMANTINI: Was he depressed?

DORIS: He was in the hospital. What do you think?

DIAMANTINI: But you said he wasn't. He had a good night's sleep. Isn't that what you said?

DORIS: Yes.

DIAMANTINI: Then he wasn't depressed.

DORIS: No.

DIAMANTINI: You just said he was.

DORIS: I said-

DIAMANTINI: He was. He wasn't.

DORIS: [Mispronounces his name.] Detective Damanitini . . . He was about five-eleven, black wavy hair. I saw him just as I was leaving the nurse's station.

DIAMANTINI: Who?

DORIS: This man. I'm leaving the nurse's station and turning to head down the hall. And I see him go into Kenny's room.

DIAMANTINI: And you don't think to say anything about it 'til now.

DORIS: He was dressed like staff. I thought nothing of it at the time. People were always coming in and out of the room. No more than a glimpse. A moment of seeing him from behind. I had no reason to think anything was wrong. Would you? [DIAMANTINI: looks at her. DORIS: holds the look].

DIAMANTINI: Was he wearing sneakers or shoes

DORIS: They were white. What difference does it make? I don't remember.

DORIS: Put yourself in my position

DIAMANTINI: Doris . . .

DORIS: If it were your daughter . . . If she had been sick

DIAMANTINI: It's a simple question

DORIS: If she had been dying . . . Lying there - If it had been you?

DIAMANTINI: But it's not! [Quietly.] It's not me. [A moment.] My brother. He's got it. Nobody knows. My wife, she doesn't want him near our girls. Like they can get it just by being near him. Like it's his fault if he gets sick.

DORIS: I'm sorry.

DIAMANTINI: Yeah ... Yeah ... Anyway-

(SCENE BREAK)

[DORIS and DIAMANTINI: address the audience.]

DORIS: People talk. Friends call. Appear. Disappear. Girls in gym uniforms wave as I drive by, then scream to their friends in disbelief. "It was her."

DIAMANTINI: "Really."

DORIS: "Gross."

DIAMANTINI: "It was."

DORIS: "No way."

DIAMANTINI: "As if."

DORIS: "Her." A group of high school boys pulls up to the house and waits. They throw a pillow on the lawn, gun the engine and laugh hysterically as they drive off into the night. The nights are lonely. The morning. Afternoon.

Margie, she keeps busy with work, but me ... I go for a walk. Come home. Sit. Wait for something to do. To take care of.

DIAMANTINI: When a murder case goes to trial, a jury's got two choices: guilty and not guilty. Not guilty doesn't mean you didn't do it.

DORIS: Innocent would mean you didn't do it. In our court system, innocence isn't an option. Even after I'm acquitted, the same questions remain.

DIAMANTINI: The oxygen mask ...

DORIS: It's possible Kenny took it off and tossed it aside. DlAMANTINI He could've put the pillow over his own face. Yeah, Kenny's hands were at his side, but they could've fallen. After he suffocated.

DORIS: It's possible someone came in the room. It's possible, they say, it was me. DlAMANTINI No fingerprints show up but Kenny's, hers, and the hospital staff. No smoking gun.

DORIS: No bloody glove.

DIAMANTINI:. An act of mercy. Desperation . Violence. A grandson's request.

DORIS: A grandmother's love.

(SCENE BREAK)

DIAMANTINI: There was no other man. In the room. We both know ...

DORIS: I know what I saw.

DIAMANTINI: Off the record. . . Between us.

DORIS: If it were you, if it were your brother, can you honestly tell me what you would do?

DIAMANTINI: I want to know. Was it you?

DORIS: Between us? "Yes, it was me." Like at the end of one of those Perry Mason shows. Always at the end somebody stands up in the courtroom, who you thought was a bit part-the gardener or maybe the family cook-finally stands up and says they're really the murder victim's ex-husband or daughter. "Yes. Yes. I did it!" they cry out. "And you want to know why ... l" [A moment. Then ... ] How often has that happened on one of your cases?

DIAMANTINI: Why won't you tell me?

DORIS: What you want to hear.

DIAMANTINI: The truth.

DORIS: A single answer. I remember a time when questions had a single answer. There was right and wrong. Good and evil. All this talk, it still doesn't bring Kenny back.

DIAMANTINI: So that's your answer?

DORIS: There is no answer. I've watched the men in my family die. Cut down, one after the other. And this is what we've become. In my day, we knew the enemy. But now ... Good. Evil. Black. White. Now it's all shades of gray.
```

---

## IC-0762: Emergency

- Title: Emergency
- Author (byline): Daniel Beaty
- Work: Emergency and Through the Night
- Publisher: Samuel French, Inc.
- Publication date as stated: March 2011
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: REPORTER 1, CLARISSA, BESSIE, RONALD, REPORTER 2, BIACK FEMALE SCHOLAR, VENDOR, BLACK FEMALE SCHOLAR, SLAVE-OLOGIST, ACTRESS, ACTOR, RODNEY
- Teaser before the introduction: Yes
- Spoken words (computed): 1142
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
ACTOR: A growing throng of African Americans flood the shores near the Statue of Liberty. Beyond rational explanation, the invisible past has materialized and it quickly become an . . . Emergency by Daniel Beaty.
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actor – Reporter 1, Slave-ologist, Ronald, Vendor, Rodney Actress – Clarissa, Bessie, Reporter 2, Black Female Scholar

REPORTER 1: (Pg 13) We are live at Liberty Island with this breaking news report. A slave ship has just risen out of the Hudson River in front of the Statue of Liberty. That's right, you heard me. A slave ship has just risen out of the Hudson River in front of the Statue of Liberty. Slave-ologists are busy trying to figure it out. Let's get some live on the spot feedback from the crowd gathering here at Liberty Island.

CLARISSA: (Pg 14) I mean, I ain't never really thought about slavery before this slave ship . . . They ain't teach us nothin' about it in school. Naw, they ain't teach us about Africa or nothing. Yeh, okay, they taught us about Egypt. The pyramids and stuff, right? Yeh, but nothing about Africa. (listens to a voice from the crowd) Egypt is in Africa? Them people was black?!

BESSIE: (Pg 13) (a seventy something soulful southern grandmother) When I first saw the slave ship, I was in stunned silence. Then I started to pray, "Thank you Jesus! Hallelujah! Thank you for not forgetting about your people. Thank you for this sign to help us remember who we are."

RONALD: (Pg 14) (a forty something high class colored man) It's . . . it's . . . appalling! It's a setback. There are black people succeeding in every field-tennis, golf, we even run for president. This is the last thing we need.

REPORTER 2: (Pg 24) Tensions are high and escalating here at Liberty Island. Hundreds of people are arriving with suitcases, old trunks, even trash bags full of clothes attempting to board the ship. Oprah is calling this slave ship a "full circle "ah ha" moment." Liberty is in a state of emergency.

RONALD: (Pg 14-15) I work in corporate America and one of my colleagues just came into my office in tears after hearing the news on the radio and she tells me she has papers that prove her great great grandparents owned slaves and she wants to apologize. And I said, "Why are you apologizing to me, Cathy? It was your great great grandparents." And she's hysterical, and so I say, "Look at me, Cathy. You've been to my home, our children play together. Cathy, I'm your boss!"

BIACK FEMALE SCHOLAR: (a fifty-something; angry sistah with an education) This slave ship is proof that slavery is not history, its reality. I write books on Post Traumatic Slave Syndrome - how slavery still impacts the minds and hearts of black people today. Look at these people's faces. This is exactly why most of us never watch those PBS specials or talk about slavery with our children. We don't know what to do with the anger.

VENDOR: (Pg 22) Yo! Check it! Slave ship buttons! Yo' ma, check it, I got yo' slave' ship buttons!

BLACK FEMALE SCHOLAR: (Pg 23) (distracted for a moment by the vendor then returning to her speech) It's not about the few us that make it; it's what slavery has done to the psyche of the masses. Why do you think there are more black people in jail and poor than any other group? Because we're inferior? No, the ghetto is a modern-day plantation.

RONALD: (Pg 39) Slavery ended two hundred years ago. We need to get over it. It's been forty years since the Civil Rights Movement. It's time to move on people. This place is out of control.

BLACK FEMALE SCHOLAR: (Pg 23) Don't get it twisted; you can have a six-figure income, a PhD, and still be a slave. But it's never too late to redeem the past, is it?

REPORTER 1: (Pg 26) Reporting live from Liberty Island where the crowds have gotten out of control. Some people are running around screaming, speaking in unknown tongues as if possessed and dancing what appears to be ancient African dance. (Actress does just that: screams, speaks in an unknown tongue and dances an ancient African dance)

RONALD: (Pg 39-40) (Distracted by the dancing, but then returns to his speech) Not all white Americans owned slaves. Many fought to free them. Affirmative action was reparations enough. I'm not an Uncle Tom. I'm not a sellout. I'm just tired of black people asking for a handout. I don't need to go back to Africa. I can reconnect . . . to that black man begging money for food (points to a person in the crowd). Reconnect to that black woman prostituting herself to keep a roof over her head. (points to a person in the crowd). Reconnect to those black kids in the orphanages who are like four and five-years old living with AIDS who nobody wants to adopt because they're sick. Yes, they are the product of this slave ship, but nobody's going to help us if we don't start helping ourselves! (pause) We are here now. We have arrived.

REPORTER 2: (Pg 26) We are speaking now with a slave-ologist. You are from Ghana, West Africa, correct?

SLAVE-OLOGIST: (forty-something West African man) Yes, I am. We have identified the slave ship as one of the many dispatched from the Cape Coast Slave Dungeons of Ghana, West Africa. We call this slave ship Remembrance. (Pg 37-38) (To the crowd gathered around) As a slave-ologist, slave dungeons are my specialty. And with this slave ship, I feel compelled to tell you what I know. I will take you on a tour as if you were standing with me in Ghana, West Africa. (Actress joins the tour and reacts silently to the Slave- Ologist) The slave dungeons you are about to see are the largest facility where the Africans were kept during the Transatlantic Slave Trade. As our tour begins, we ask that you leave your rage and pain at the entrance gate because there is enough inside. Thank you and please follow me. (As he turns upstage, his hands cross violently above his head as if chained. Enraged, he speaks the following words of resistance to an imaginary guard.) Olokikijulu amanla owetu! Olokikijulu amanla owetul (To crowd) We have now entered the Slave Dungeons where the Africans were kept. Here, they defecated on the same floor where they slept and ate. This is where the Africans were brought before they boarded slave ships like Remembrance for the passage to America . . . TRANSITION

ACTRESS: But then, just as mysteriously as The Remembrance appeared, the great slave ship sank.

ACTOR: Leaving many to wonder if it was real, or just a figment of their collective consciousness.

REPORTER 2: (Pg 49-51) Remembrance has disappeared. Moments ago the slave ship Remembrance began to sink back into the Hudson River. Divers were immediately dispatched into the water and all they see is an endless stretch of skeletons, human bones, and the chains are gone. And what's even more bizarre is that while Remembrance has disappeared from the vision of most of us here at Liberty Island others are insisting that they can still see it floating right here in front of the Statue of Liberty. (The Reporter fades from the scene, leaving Rodney alone on stage)

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

## IC-0763: English Made Simple

- Title: English Made Simple
- Author (byline): David Ives
- Work: Land of Cockaigne and English Made Simple
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1995
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: LOUDSPEAKER VOICE, JACK, JILL
- Teaser before the introduction: Yes
- Spoken words (computed): 972
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Ives
Book: Land of Cockaigne and English Made Simple
ISBN: 978-0822214700
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1995
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Guys and girls may be from Mars and Venus.

ACTOR 2: But learning how to keep a conversation going between the sexes can help you bridge that divide without any hiccups.

ACTOR 1: For most of us, the first few minutes of a new conversation is the absolute worst.

ACTOR 2: It’s awkward and uneasy, and almost always a toe curling nightmare.

ACTOR 1: But as annoying as those first few minutes are, it is those very few minutes that will turn out to be the biggest judge of your conversation skills.

ACTOR 2: After all, first impressions are made of first conversations.

ACTOR 1: And in English Made Simple by David Ives, you even get the added benefit of the oral critique

ACTOR 2: from what we affectionately call . . . the Loudspeaker Voice

TOGETHER: No pressure! English Made Simple by David Ives
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Actors should take turns with the LOUDSPEAKER VOICE In the darkness, a Voice over a loudspeaker.

LOUDSPEAKER VOICE: English Made Simple, Chapter Three. The party. Section One: Saying Hello.

(Lights up on Jack and Jill, a pleasant young man and woman of about 30. He is holding a plastic drink glass and she a paper plate. They stand facing each other, frozen in place, several feet apart. In the background we hear the sounds of conversation, laughter, glasses clinking, silverware, etc.)

JACK and JILL: Hello! (They take a step toward each other.)

LOUDSPEAKER VOICE: But remember before you begin - (Jack and Jill freeze.) The first three minutes of conversation between two people can determine their relationship for the rest of eternity. (Jack and Jill clear their throats in chorus, a bit nervously.) So watch your language!

JACK: Hello.

JILL: Hi.

JACK: How are you?

JILL: Good.

JACK: I don't think I know you.

JILL: My name is Jill.

JACK: I'm Jack.

JACK and JILL: How do you do.

JACK: Are you a friend of the host?

JILL: Friend of the hostess.

JACK: Oh. So ...

JILL: Well ... (Slight pause: a momentary loss for conversation.)

JACK and JILL: Nice party! (They freeze.)

LOUDSPEAKER VOICE: Section Two. The structure of English conversation.

JILL: Fred!

LOUDSPEAKER VOICE: First name.

JACK: Mary!

LOUDSPEAKER VOICE: First name.

JACK and JILL: Hello!

LOUDSPEAKER VOICE: Salutation. (Jack and Jill kiss on the cheek.) Social display of affection, followed by-

JILL: I didn't know you were here.

LOUDSPEAKER VOICE: Friendly observation, answered by -

JACK: I'm here.

LOUDSPEAKER VOICE: Statement of the obvious.

JILL: How are you?

LOUDSPEAKER VOICE: Superficial question about health.

JACK: Good.

LOUDSPEAKER VOICE: Superficial answer. Occupational question -

JACK: How's the job?

LOUDSPEAKER VOICE: And

JILL: Terrific.

LOUDSPEAKER VOICE: Customary lie.

JACK: So . . .

LOUDSPEAKER VOICE: Meaningless monosyllable while searching for topic.

JILL: Quite a smorgasbord.

LOUDSPEAKER VOICE: Attempt at new topic.

JACK: Mmmmmmm.

LOUDSPEAKER VOICE: Noncommittal noise, to reject the topic. And -

JACK and JILL: Well!

LOUDSPEAKER VOICE: Exclamation, to signal the approaching end of the interchange. Well done.

(All as asides to the audience)

JACK: I was in love with you, once upon a time.

JILL: You asked me about my job, and I lied to you.

JACK: You who look so self-possessed and mature.

JILL: I would have answered you honestly, once upon a time.

JACK: Once upon a time you cried on my shoulder like a little child.

JILL: We would have talked like two people who love each other. Then we would have gone home and lain in bed.

JACK: We used to go to parties like this all the time.

JILL: Once upon a time.

JACK: SO happy... (Small pause.)

JACK and JILL: Well!

JILL: Nice seeing you, Fred. (Kisses his cheek.)

LOUDSPEAKER VOICE: Expression of pleasure.

JACK: Take care of yourself, Mary.

LOUDSPEAKER VOICE: Parting wish.

JACK and JILL: Bye!

LOUDSPEAKER VOICE: Valediction. (Jack and Jill Freeze.) Section Three. Simultaneous translation, or the secret meanings of common English words.

JILL: Well, well, well.

LOUDSPEAKER VOICE: In this context: "Oh, shit."

JACK: I didn't know you were here.

LOUDSPEAKER VOICE: "What are you doing here?"

JILL: How are you, Hank?

LOUDSPEAKER VOICE: “Wasn't five years enough?"

JACK: I'm good.

LOUDSPEAKER VOICE: "*Up yours*, Agnes."

JILL: Nice party.

LOUDSPEAKER VOICE: "Ass."

JACK: Very nice.

LOUDSPEAKER VOICE: "*Up yours*, Agnes."

JILL: So what are you doing with yourself?

LOUDSPEAKER VOICE: "Are you still *sleeping with that girl* from the community college?"

JACK: Same old thing.

LOUDSPEAKER VOICE: "It's none of your business."

JILL: Have you tried the chicken?

LOUDSPEAKER VOICE: "Have some salmonella?"

JACK: I'm sticking with liquids.

LOUDSPEAKER VOICE: "I know you have problems with your mother, but you don't have to poison me."

JILL: See you, Hank.

LOUDSPEAKER VOICE: "Up yours."

JACK and JILL: Bye! (They freeze.)

LOUDSPEAKER VOICE: Section twenty-six. The conditional tense, or: Should, Would, Could.

JACK: Okay, so we meet at this party.

JILL: And we like each other.

JACK: We like each other instantly. (Holds out hand.) I'm Zeno.

JILL: Miranda. (They shake.) Did you know that the first three minutes of conversation can determine your relationship to the other person for all eternity?

JACK: But we pass the three-minute mark! We meet, and we mesh.

JILL: Oh, what a mesh.

JACK: And it all begins right here on this spot. In a single moment, all things seem possible.

JILL: All things are possible.

JACK: The infinite smorgasbord lies before us. But what do we do?

JILL: The party's wrapping up.

JACK: The crowd is thinning.

JILL: The question of the moment is:

JACK: Do I ask you out?

JILL: Do I ask you out?

JACK: And if you do -

JACK and JILL: Should I accept?

JACK: This could be one of those glorious meetings best left to memory.

JILL: Or it might be the start of eternal love.

JACK: So I say: Would you like to get a cup of coffee sometime? And you say -

JILL: Sorry. Thanks anyway.

JACK and JILL: Bye!

JACK: The road of no-thank-you.

JILL: A dead end.

JACK: But possibly a happy dead end. While down this road here, is:

JILL: Would you like to get a cup of coffee sometime?

JACK: Sure!

JILL: So we go out for coffee.

JACK: And we have a horrible time.

JILL: Dead end.

JACK: Or a wonderful time. In which case –

JILL: We get a second cup.

JACK: And stop right there.

JILL: Dead end.

JACK: Or we go out for a third cup and a fourth cup and a fifth cup.

JILL: Would we have made love by now?

JACK: Let's say we did. JILL And it was horrible.

JACK and JILL: Dead end.

JILL: Or it was wonderful. Which means –

JACK: More coffee. And -

JILL: We move in with each other.

JACK: Mistake.

JILL: Dead end.

JACK: Or it could be wonderful!

JILL: We get engaged.

JACK: Marriage.

JILL: Children.

JACK: Bliss. (Jack and Jill: Blissful sigh.)

JILL: And on to divorce.

JACK: Or - the other road - maybe we're down the road of no-thank-you we took years and years ago, and years and years pass -

JILL: And we meet each other at a party. And you say –

JACK: Hello, I'm Zeno.

JILL: Miranda.

JACK: Don't I know you from somewhere?

JILL: And a whole universe opens up in front of us, full of joy.

JACK: Right on this spot.

JILL: Dead end?

JACK: Or bliss?

JILL: Should, would, could.

JACK: Well it was nice meeting you, Miranda.

JILL: Yes. Nice meeting you. (They reach their hands to shake, but freeze.)

LOUDSPEAKER VOICE: Section seventy-eight. Saying Goodbye.

JACK: Listen, I only have a few minutes. I just wanted to say you are the most wonderful woman at this party.

LOUDSPEAKER VOICE: Let's practice a typical interchange.

JACK: On this street. In this city- In this country. On the planet.

LOUDSPEAKER VOICE: Typical, please!

JILL: You're the most wonderful man I've met in years.

JACK: You have a light that surrounds you.

JILL: You're intoxicating.

JACK: You're radiant. I came to this party one thing and I leave it transformed.

JILL: I came to this party to meet the love of my life.

JACK: And you're her.

LOUDSPEAKER VOICE: (Correcting.) You are she.

JACK: You're her! You are the love of my life!

JILL: My name could be anything.

JACK: But it's Jill.

JILL: I could have gone anywhere tonight.

JACK: But you came to this party.

JILL: Hello hello.

JACK: Abracadabra. My name is Jack.

JILL: Would you like a cup of coffee sometime, Jack?

JACK: Yes, Jill, I would like that very much.

JILL: And it all starts right here.

LOUDSPEAKER VOICE: A-plus.
```

---

## IC-0764: Equus

- Title: Equus
- Author (byline): Peter Shaffer
- Work: Not specified
- Publisher: Penguin
- Publication date as stated: Oct 1984
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, DYSART, ALAN, MOTHER, FRANK, JILL
- Teaser before the introduction: Yes
- Spoken words (computed): 1661
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
ACTOR 2: In this selection, a psychiatrist, Dr. Dysart, investigates the savage blinding of six horses with a metal spike.

ACTOR 1: The atrocity was committed by an unassuming seventeen-year-old stable boy named Alan Strang, the only son of an opinionated father and a genteel, religious mother.

ACTOR 2: Alan is found guilty, but mentally disturbed, and he is sentenced to an inpatient ward at Rokesby Psychiatric Hospital.

ACTOR 1: Can Dr. Dysart discover the motive behind Alan’s brutal actions;

ACTOR 2: Can Alan be saved from himself?

TOGETHER: Equus by Peter Shaffer.
```

### Performance text (classify this)

```text
NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles:

ACTOR 1: Dysart, Mother, Frank, Jill

ACTOR 2: Alan

DYSART: (Pg 21-23) Hallo. I’m pleased to meet you (he puts out his hand. Alan does not respond in any way. Dysart opens his file) Is this your full name? Alan Strang? (Silence) And you’re seventeen. Is that right? Seventeen? . . . . Well?

ALAN: (singing low) Double your pleasure, Double your fun, With Doublemint, Doublemint, Doublemint gum. (See note at the end of this selection for a link to the Doublemint jingle)

DYSART: (unperturbed) Now, let’s see. You work in an electrical shop during the week. You live with your parents.

ALAN: (approaching him, hostile but still singing) Double your pleasure, Double your fun, With Doublemint, Doublemint, Doublemint gum.

DYSART: (appreciatively) That’s a good song. Please do that one again. (Silence. The boy glares at him; Dysart speaks to audience) (Pg 26-29) It took him two more days of commercials, and then he snapped. He bursts in – just like that – without knocking or anything. Fortunately I didn’t have a patient with me.

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

DYSART: (Pg 100) The temple? The Holy of Holies?

***** Scene flashes back to Alan and Jill at the stable *****

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

## IC-0765: The Explorers Club

- Title: The Explorers Club
- Author (byline): Nell Benjamin
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Oct 2014
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS, ACTOR, LUCIUS, COPE, WALLING, ALL, PHYLLIDA, LUIGI, SLOANE, PERCY, HUMPHRIES
- Teaser before the introduction: Yes
- Spoken words (computed): 1413
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nell Benjamin
ISBN: 978-0822230090
Publisher: Dramatists Play Service
Date (Month/Year): Oct 2014
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: The Explorers Club ACTRESS: A scientific farce of Biblical and British proportions by Nell Benjamin
```

### Performance text (classify this)

```text
Suggested Roles:

ACTRESS: Cope, Phyllida, Sloan, Percy,

ACTOR: Lucius, Walling, Luigi, Humphries

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

LUCIUS: (Pg 5-6) Gentlemen, good evening and welcome to the annual meeting of the Explorers Club. Now, excellent news for our club: Two of our own have an audience with Queen Victoria. Professor Cope, as many of you know, discovered a deadly new species of cobra . . .

COPE: (He stands, crooning to the cobra draped around his neck) (Pg 30) Snakes are wonderful animals! They are misunderstood. They are fascinating and charming, and I like snakes! (Beat) (Pg 6) Her name is Rosie.

LUCIUS: Yes. Thank you, Professor Cope. Also presenting at the palace tomorrow is our own Professor Walling, who has done some amazing behavioral studies with guinea pigs.

WALLING: (He stands, holding a guinea pig) Cavia porcellus, if you please. Very clever. I designed an experiment in which I put food outside their cages to see if they would be able to figure out the latches. And they did. Now I can't find any of them. This one, Jane, had some trouble with the latch, so I've still got her. (glumly) In retrospect it wasn't the best-designed experiment.

COPE: (Helpfully) But you've proven their intelligence!

WALLING: (Cheering up) Yes. Yes I have!

ALL: To Science!

LUCIUS: (Pg 6-7) And now, gentlemen, I am very excited to introduce an exceptional explorer and scientist, whom, in fact, I hope to propose for membership. She has recently achieved

WALLING: (interrupting) There are no female members of this club!

LUCIUS: Gentlemen, please. We are men of progress. Please welcome Miss Phyllida Spotte- Hume, the first explorer to discover the Lost City of Pahatlabong! (he leads the applause)

PHYLLIDA: Gentlemen of the Explorers Club. May I present to you: a genuine warrior of the NaKong tribe of the Lost City of Pahatlabong! Luigi, na'I haa'ru. (Luigi steps forward. He is painted blue, wearing a combination of tattoos, feathers and knickerbockers.)

LUIGI: Luigi.

PHYLLIDA: His name is not actually Luigi, but Loo-ah-JA-mweno-wepta. I have shortened it to "Luigi" for simplicity's sake.

LUIGI: (Pg 15) (With great solemnity and hand gestures. Phyllida translates) NaKongi weilah gweisha. (In my country there is a saying.) Do haaru seefkai basei. (On the ground there are many snakes.) Kwei haa'ru eekweet shasa basei. (And over your head are many rabid monkeys.) Mem haa'ru pog fhwt! Fhw! Fhwt! (But throw enough rocks around in all directions,) weil basei hatlala. (. . . and you will have temporary peace.)

PHYLLIDA: (Pg 7) My journey to Pahatlabong was grueling. Deserted by guides, I crawled delirious through the swamps, and when found by Luigi, I was in possession of nothing more than the clothes on my back and a spoon. . . (She holds up a spoon.)

LUIGI: (Luigi bows down) Mogweet Aleili!

PHYLLIDA: Luckily for me, the NaKong god, Mogweet, is spoon-shaped, so they greeted me as a messenger from their god. (Pg 8) I will end this lecture here, as tomorrow I will be presenting Luigi to the queen.

LUIGI: (Pg 9) (Bows) Mah-jah-stay! (they exit the podium)

WALLING: (Pg 8) Wonderful lecture, Miss Spotte-Hume. I never thought I’d see a woman present at the Explorers Club, but you have proved me wrong.

SLOANE: (introducing himself to Phyllida) Sloane. Robert Sloane. Professor of archeo-theology. Biblical science. God created science, and God wrote the Bible, and the Bible exhorts us to beware the evil woman. (Pg 19) (To Luigi; smiling but shouting as to a dog) Luigi! Have you read the BIBLE?! The BIBLE?!

LUIGI: BYE-BULL

LUCIUS: Sloan, he’s just repeating words he doesn’t understand.

SLOANE: That’s good enough for the Church.

LUCIUS: (Pg 9) (Offering his hand) Hello there, Luigi . . .

PHYLLIDA: No, Lucius! (Luigi slaps him hard across the face.) That is how the NaKong introduce themselves.

LUCIUS: Meeting the queen is a terrible idea.

PHYLLIDA: Don't be silly, Lucius. You don't shake hands with the queen. (She exits with Luigi)

PERCY: (Pg 15-16) So what are you up to, Sloane?

SLOANE: I'm presenting to the Irish Society tomorrow. A breakthrough in Biblical studies. You know the Ten Lost Tribes of Israel? Reuben, Simeon . . . Zebulon, Levi, Judah, and Dan? The Bible says they were captured by the Assyrians. Sold into slavery. And they're never mentioned again. Not once in the whole Bible. No one knew where they went.

PERCY: And you think you've figured out where they went?

SLOANE: I have. They went to Ireland! Think about it. How many Irishmen do you know named "Dan"? A lot. I believe the Ten Lost Tribes of the Hebrews brought the Ark of the Covenant to Ireland. I'm going to dig for it!

LUCIUS: Just to be clear: You're going to tell the Irish Society that they are actually Jewish?

SLOANE: They need to know.

ALL: To Science! ***** The following day after the Queen’s presentation *****

PHYLLIDA: (Pg 21-23) (Phyllida enters, in a panic.) Oh, what a state I'm in! I don't know what to do! Disaster at the palace. Luigi bowed beautifully. But then the queen put out her hand to help him rise! He struck her across the face! It was chaos. I had to create a diversion. So I . . . I opened Rosie's cage.

LUCIUS: You released a deadly cobra in the throne room?

PHYLLIDA: They were much more concerned with a poisonous snake than with poor Luigi, so we were able to escape.

COPE: (Cope enters, with Rosie draped over him.) Oh, what a state I'm in! I don't know what to do! Is Walling back yet?

LUCIUS: We thought he was at the palace with you?

COPE: He was! But then Rosie got out of her cage. It was chaos. I thought they were going to kill Rosie, but ... Rosie never went near Her Majesty. She was distracted. By Jane. Jane finally figured out how to open the latch on the cage. Rosie ate Jane, Lucius! Right there in the throne room. Walling ... I've never seen him look like that. I grabbed Rosie and ran for it. Why, why did Jane have to figure out the latch right then? Stupid animal! (Walling enters, enraged.)

WALLING: "STUPID ANIMAL"?! "STUPID ANIMAL"?! Do you see this? (Walling produces Jane's tiny collar with the bell. He shakes it repeatedly at Cope. Ring.) This is what's left of her!

(Walling collapses in tears and exits – Humphries enters)

HUMPHRIES: (Pg 24-26) Gentlemen, I am Sir Humphries, private secretary to the queen. Direct me to Miss Phyllida Spotte-Hume. I've come to speak with her about the incident at the palace. (COPE points to Phyllida) No one is here to punish you, Miss Spotte-Hume. In fact, Her Majesty is rather in need of your help.

PHYLLIDA: Anything. Anything, of course.

HUMPHRIES: Excellent. Would you be so kind as to provide some kind of map to the Lost City of Pahatlabong? We've declared war on them, so we need to know where they are.

PHYLLIDA: What?!

HUMPHRIES: We like to be as precise as we can with this sort of thing. We don't want to get the army out there attacking Malaysia by mistake. You can't imagine the paperwork when that happens.

PHYLLIDA: You said no one was going to be punished!

HUMPHRIES: I said you weren't going to be. You're British. That NaKong chappie is not.

PHYLLIDA: But he didn't mean any harm!

HUMPHRIES: Madam, he slapped the Queen of England. In the face.

PHYLLIDA: That's the way they say hello!

HUMPHRIES: And now we get to say hello. With artillery. That wild man came as a representative of his people and his people slapped the queen. Let me make myself clear. If you look out that window, you will see this club surrounded by Her Majesty's guards. We have come for the savage and the map. You're not in a position to refuse. (Phyllida responds in dismay then has an idea)

SLOANE: (rushes in, breathless and afraid.) Disaster! I barely escaped with my life. I was attacked by the Irish Society; they didn't appreciate being called Jewish.

PERCY: They're worked up because you called them Jewish?

SLOANE: I also said they should be relocated to Palestine. (Everyone groans.)

ALL: (Pg 16) To Science! ***** The next day *****

PERCY: (Pg 28-29) Lucius, the time has come. We deliver Luigi and the map or prepare for battle, and frankly I don't like our chances. Shall I wake Phyllida?

LUCIUS: Phyllida's gone. She slipped through the lines last night. [but] she left a note. (he brandishes the note) She's going back to Pahatlabong to warn them! ***** Days pass, but the problem remains *****

HUMPHRIES: (Pg 33) (Enters) Gentlemen. I have returned.

LUCIUS: (Pg 34) (All business) Sir Humphries, we're eager to find a diplomatic solution.

PERCY: Thing is, Humphries, Phyllida's scarpered to Pahatlabong.

HUMPHRIES: And her savage?

LUCIUS: She took him with her. (Pg 44-45) Sir, don't you think the Crown could forgive the NaKong?

HUMPHRIES: What? No . . . if we went around indiscriminately forgiving everybody, what would that make us?

SLOANE: Christian?

HUMPHRIES: For your country and your club, will you find Phyllida Spotte-Hume!

PHYLLIDA: (Phyllida enters, looking ragged but determined) Sir Humphries. Here is your map. It will take you straight to Pahatlabong. But when you get there, you will find nothing. I warned the NaKong to flee, that the British were coming with fire and steel. They wanted to fight. But I held up my spoon and commanded them to disperse; to go where even I could never find them. That map will bring you to where they used to be, but the city is leveled and the people are gone.

HUMPHRIES: (Threateningly) My course is clear, Miss Phyllida Spotte-Hume.

LUCIUS: You should give her a medal.

HUMPHRIES: (Annoyed) What? Why?

LUCIUS: Think. The queen wanted Pahatlabong leveled and its people gone. Phyllida's done that for you without the expense and trouble of trucking the British army through the jungle. Your mission is a complete success.

HUMPHRIES: (changing his tune) Madam, it appears you have done your country a service. (Pg 46) I must say this is most satisfactory. I shall withdraw the guards and report my happy news to the queen. (Pg 47) I speak for Her Majesty when I say I am impressed, very impressed by the Explorers Club. (Humphries exits. Walling and Cope rush to the window.)

COPE: He's moving out the army! We're saved!

WALLING: And our club is more prestigious than ever!

ALL: To Science!
```

---

## IC-0766: Falling

- Title: Falling
- Author (byline): Deanna Jent
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: April 2014
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TAMI, BILL, JOSH, GRAMMY
- Teaser before the introduction: Yes
- Spoken words (computed): 1153
- Already set (do not supply): none

### Source block (context only)

```text
Author: Deanna Jent
ISBN: 978-0822228431
Publisher: Dramatists Play Service
Date (Month/Year): April 2014
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: The morning routine of a family coping with a severely autistic 18-year-old would be enough to exhaust anyone.

ACTRESS: But it is a daily reality for the Martins. In their home, the simplest of tasks –

ACTOR: getting ready for school,

ACTRESS: turning on blender,

ACTOR: getting out the door –

ACTRESS: are complex feats that require equal amounts of brute physical strength and relentless mental strategizing.

ACTOR: Routine is everything until a visit from Granny and a barking dog throw the tenuous equilibrium off kilter.

TOGETHER: Falling by Deanna Jent.
```

### Performance text (classify this)

```text
Suggested Roles: Actor – Bill and Josh Actress: Tami and Grammy

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

(Pg 11-15) Joshua enters the room. As he walks through the room, he occasionally pulls his shirt partially up exposing a nipple (one of his habits). Josh moves under the feather box, does a short ritual of touching certain things and moving in a certain way, and then dumps the feathers on his head. He squeals and is doing his happy dance as Tami enters carrying a laundry basket.

TAMI: Hey, Josh – I like that smile! Remember, feathers go back in the box, please (she exits)

BILL: Feathers back in box please. Bus soon

JOSH: No bus. No thank you.

BILL: Feathers back in box.

JOSH: No bus.

BILL: Feathers in box. Bus at 7:45.

Josh makes a fist and pushes on his forehead between his eyes (This is a stress reliever) After a moment, he starts picking up the feather and putting them in the box. Tami enters drinking a cup of coffee.

TAMI: (To Bill) Smoothie time. (To Josh) Lisa is going to use the blender. We’ll do “cover our ears” and then you can pick a game. Ready? (Josh covers his ears with his hands and crouches) OK Lisa! (To Josh) Here we go! (Tami starts counting down on her fingers) 5- 4-3-2 and 1. Noise is all done. (Josh pulls his hands away from his ears) Good job! Now do you want to do “London Bridge” or “Big Bad Wolf”?

JOSH: (excited) And blow the house down!

TAMI: Alright! Dad – can you be a big bad wolf? (Josh is excited) Once upon a time there were three little pigs who went out in the world . . .

JOSH: (Grabbing a finger with each word, hurrying the story along) Straw, wood, bricks.

TAMI: OK! Aaaaaannnnd . . . So the three pigs were safe in their house of brick when along came the . .

JOSH: (In a deep but no very loud voice) Big Bad Wolf

TAMI: And he said:

BILL: (In a deep voice, which makes Josh laugh) “Little pigs, little pigs, let me in.”

TAMI: And the pigs said . . . (Cueing Josh)

JOSH and TAMI: (Together. High voices) Not by the hair on my chinny-chin-chin.

BILL: (Really getting into it) Then I’ll huff, and I’ll puff, and I’ll blow your house in! (He blows as hard as he can, then stops) Wait a minute, that didn’t work! (Josh nearly wets himself because this is so funny) Let me try again. (He blows and blows, until finally he “passes out.”)

TAMI: And the wolf blew himself out, and the pigs lived . . . (Cueing Josh)

JOSH and TAMI: Happy ever after (Tami claps and helps Bill back to his feet. Josh is very happy, maybe squealing)

TAMI: Yay for “Little Pigs!”

JOSH: (Suddenly serious) No bus. No thank you. No school

TAMI: (Cheery but not too loud playful voice as she tries to get Josh’s backpack on) Uh-oh! We can’t change school days (Exaggerated with a big gesture) Rats!

JOSH: (Mimicking her gesture and sound) Rats!

TAMI: But after school, Grammy Sue is coming. And she is bringing a present for you.

JOSH: (Looks out the window on the front door, in an animated voice) Where is the bus?

TAMI: (relieved, this is now part of the regular morning script – in a cheery voice) I don’t know. Where is the bus? ******** Scene break **********

TAMI: (Pg 19) So, um. Josh will be home soon, and I wanted to make sure you were ready. Did Bill tell you about how he gets upset sometimes?

GRAMMY: (Pg 21) You know our prayer group lifts up Josh every week. We have such a nice program for the disabled kids – I wish your church had one. (Pg 22) Josh is here for a reason God has a plan. (Pg 21) (Josh enters) Josh – come here and give Grammy a hug! I have a present for you. It’s a puzzle with a train. (Josh rips the paper off the box, examines it closely for a few seconds, then drops it on the floor. (Pg 23) He pulls up his shirt and touches both nipples) Joshy, that’s not nice. It’s not polite to touch your chest like that. (Josh continues as before. She speaks louder) Josh!

BILL: Josh – shirt down. (Josh pulls his shirt down) Clap hands. (Josh does) Good job!

GRAMMY: You need to teach him to listen to other people. I told him it wasn’t polite to have his shirt up like that and he just ignored me.

BILL: I’m sorry. He doesn’t really get a concept like being polite. (Pg 27-29) (We hear a dog barking outside)

JOSH: Barking.

TAMI: Yes, there is a dog barking

JOSH: No barking.

TAMI: You don’t like the dog barking.

JOSH: You don’t . . . (Tami interrupts him with sign language prompting the word “I”) I don’t like dog barking (He pushes his fist to his forehead)

TAMI: That’s really good telling me how you feel, Josh. We’ll help the dog stop barking, okay? Lisa? Can you put the dog in the garage while we eat supper.

JOSH: No barking!

TAMI: (attempting to distract him) Josh, It’s time for supper. Do you want to eat with us?

JOSH: No supper! (He exits back to his room)

TAMI: (to Grammy) He likes to eat by himself. Or I should say, he doesn’t like to watch other people eat. It grosses him out. Josh will be happy NOT eating with us, and if Josh is happy, then we’ll all be happy! (Pg 30-33) Would you like to say the blessing?

(Josh enters and starts pacing back and forth moving between his happy dance and repeating a few lines of dialogue from a Tarzan movie. He does a “Tarzan” yell and a crash noise and the dog begins barking again outside)

JOSH: (distracted) Barking.

TAMI: (Realizes this won’t be a normal dinner, she attempts to diffuse the situation which escalates rapidly) Josh, why don’t you go read a book in your room and we’ll take care of the barking dog. (the following lines overlap at Josh’s emotional level escalates)

JOSH: No barking dog.

TAMI: I know you don’t like the sound of the barking dog.

JOSH: Barking! Barking! Barking!

TAMI: I know! It is loud! Let’s cover our ears.

(She covers her ears and tries to get him to cover his. Josh is finally at his breaking point and with a scream he lunges for Tami, one hand pressing on his forehead and the other grabbing her shirt near the neck. He pulls her close to him and screams again, then slams her against the door, his hands around her throat. Tami is working to pry his hands from her as she tries to talk calmly.) (To Lisa)

TAMI: Take Grammy to her room. (Josh screams again and Tami continues speaking quietly to him) Josh – look a Mommy. The barking is stopped the barking is gone.

JOSH: (Screaming) Barking! Barking!

TAMI: Let’s breathe. (She takes a deep breath in and blow it out) Come on, sip a breath in. (She sips like on a straw, and Josh does as well) and blow it out. (Pg 26) Good! Now show me relax. (Pg 33-34)

(They both blow. Josh is beginning to relax. He is still holding Tami by the shirt with both hands. Josh realizes what he is doing and begins crying a plaintive, sad howl. All the energy drains from him and he slides to the floor continuing his cry)

JOSH: I’m sorry. Mom I’m sorry Mom I’m sorry (Sobbing) Mom I’m sorry Mom I’m sorry.

TAMI: (Holding back tears and speaking over Josh’s lines) I know you’re sorry, Joshy, I just wish . . . (The tears come) you could be sorry before you grabbed. I wish you . . .

JOSH: (Sadly) Mom is crying.

TAMI: Yes, Mom is crying. . . (She shakes it off and returns to her caregiver role but is still obviously shaken) (Pg 26) Good job! Great relaxing Josh! Here are your choices right now. One: Watch DVD. Two: Play computer. Three: Do feathers. Which choice do you want right now? (Josh frowns and shakes his head violently. Tami indicates the choices visually with her fingers) One two or Three. (Josh chooses silently by indicating with his fingers) Good job choosing! You chose number 1. Watch a DVD in your room. Do you need some help?

JOSH: No help (he exits)

TAMI: (to Grammy) He should be fine now . . . (Pg 35) I know he’s scary. (Pg 36-38) We have a hard time finding people who want to keep working with him. And really, he’s calmer when it’s just us.

GRAMMY: (Completely shocked and appalled) Isn’t there some medicine that would . . . ?

BILL: (as he comforts Tami) He’s taking three different things – if we up the dosages he just get more cranky.

GRAMMY: Isn’t there a safe place that Josh could live. I thought now that he’s 18 he could go to one of those group houses.

BILL: There’s waiting lists.

GRAMMY: We can ask God for the solution. Can we pray together? We can pray for healing. For a miracle: that Josh will be released from this autism.

BILL: Mom – if you’re gonna pray then . . . (Not too fast, with conviction) pray for programs and housing options and staff for people like Josh. Pray that our marriage won’t fall apart. Pray that people will stop just praying and take some action.

GRAMMY: (offended, she begins to exit) You know, when you don’t want to pray is the best time to do it. (Exits)

TAMI: (to Bill) Wanna pray?

BILL: Not sure God wants to hear what I have to say right now. I just yelled at my mother and basically gave Him the finger. Got anything else you want me to screw up?

TAMI: You didn’t screw up. She needed to hear that. You needed to say it.

BILL: (Moving toward her) I’m sorry. How badly did he get you?

TAMI: Not so bad. The shirt got the worst of it this time (Bill comes up behind her and encircles her in a hug, which she accepts. He brushes her hair away from her neck and leans down to kiss her neck. She pulls away.)

BILL: OK. Sorry. Just trying to take your mind off . . .

TAMI: I know.

BILL: You keep pushing me away.

TAMI: I can’t . . .

BILL: What?

TAMI: I can’t take care of another person right now

BILL: This is taking care of me?

TAMI: Isn’t it?

BILL: I thought it was taking care of each other.

TAMI: I will fall apart if I let go. Why can’t you . . . ?

BILL: That’s the whole point. You let go and relax!

TAMI: That’s why wine was invented! (She crosses and pours a drink)

BILL: So . . . you’d rather have a glass of wine than let me tough you.

TAMI: You know what? Sex is your prayer for a miracle – (Gesturing towards Josh’s room) and look what that got us.

BILL: (a pause) I don’t know what to say.

TAMI: Neither do I.
```

---

## IC-0767: Fallout

- Title: Fallout
- Author (byline): S.W. Senek
- Work: The Best 10-Minute Plays 2007 – 2 Actors
- Publisher: Smith and Kraus
- Publication date as stated: July 2008
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JANET, HAROLD
- Teaser before the introduction: Yes
- Spoken words (computed): 1669
- Already set (do not supply): none

### Source block (context only)

```text
Author: S.W. Senek
Book: The Best 10-Minute Plays 2007 – 2 Actors
ISBN: 978-1575255897
Publisher: Smith and Kraus
Date (Month/Year): July 2008
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: In the September (1961) issue of Life magazine, President Kennedy advised, in a letter, that Americans build fallout shelters - causing a wave of "shelter mania " Off and on until the early '60s, Americans built underground rooms that promised to protect them from a nuclear attack.

ACTOR: Playing on traditional imagery of women as domestic caretakers, the government promoted advertisements targeted at housewives for "Grandma's Pantry," a home shelter that women should stock with canned goods, first-aid kits, and flashlights.

ACTRESS: Commercial firms marketed a range of safehouses, that ranged from a "$13.50 foxhole shelter" to a $5,000 "deluxe" model that included a phone, beds, toilets, and even a Geiger counter.

ACTOR: Life magazine even ran a story on a young newlywed couple who spent their honeymoon in a steel-and-concrete room 12 feet underground. "Fallout can be fun," the article said.

ACTRESS: The time is October 1961, one year before the Cuban missile crisis. Down in their basement bomb-shelter, a husband & wife find themselves at odds over the definition of “preparedness.”

TOGETHER: Fallout by S.W. Senek
```

### Performance text (classify this)

```text
Harold and Janet, in their late thirties/early forties, are in the midst of putting on their protective suits - they look more like cheap yellow rain coats/trousers. Harold wears a stopwatch around his neck.

JANET: I have to get out.

HAROLD: No, we don't have time. Put the suit on. (He looks at his stopwatch.) My watch says six minutes, fifteen seconds - that's practically six minutes.

JANET: I know how long six minutes is.

HAROLD: (Listening to a sound coming from above.) Wait - did you hear that?

JANET: What?

HAROLD: Shhh - I thought I heard something - upstairs.

JANET: It's the cat. Pickles. Harold, it's hot - I'm suffocating.

HAROLD: No, you're not. Where's my other boot?

JANET: My zipper's broke -

HAROLD: Did you move my boot?

JANET: I said my zipper is - I can't.

HAROLD: You have to. (He looks at his stopwatch.) Janet - hurry. (He puts single boot on.) Forget the zipper and boot - checklist - checklist! (Holds up a clipboard.) Let's get the blankets ready. Survival, Janet, survival.

JANET: I'm tired.

HAROLD: Do you think the Russians care if you're tired? Fourteen minutes - fourteen minutes - that's how fast these bombs are. (Looking for the labeled box of blankets.) Where's the blanket box? Why aren't the labels facing out?

JANET: Harold, how many times? We get up in the middle of the night - down here - stay up all night - reload supplies all day - sleep for a half hour - down here - how long do we have to do these drills? (Harold opens a box and pulls out a shredded blanket.) It's insane.

HAROLD: Did you let Pickles down here?

JANET: Me?

HAROLD: I told you not to - that's it - the cat's gone! (Harold pantomimes strangling.)

JANET: But you like Pickles -

HAROLD: A goner I tell you! Checklist! (Looks at what's next on the checklist.) Flashlights.

JANET: How many more nights of these drills? They're going to fire you –

HAROLD: Let them. This is more important - are you sure you didn't hear anything up stairs?

JANET: The dealership called, Harold. You can't stop showing up for work. We need the money - and I want sleep - Pickles wants sleep.

HAROLD: No, you want to live.

JANET: No, I want to sleep.

HAROLD: Stop this. We agreed. (Searching in a box.) We should have two more flashlights.

JANET: We're going crazy - that's what we're doing - that's what I’m doing.

HAROLD: When that bomb hits, you're going to be thanking me. Now where the hell are the other flashlights? It should be in the box labeled flashlights.

JANET: If a nuclear bomb hits, I'm not thanking anyone.

HAROLD: This is no time for jokes.

JANET: Who's joking? With six minutes left, I'm not joking.

HAROLD: (Looking at stopwatch.) Four minutes, forty seconds - Christ you've wasted over a minute. We're running behind schedule. Double check the powdered milk while I look for the flashlights. (He continues looking through boxes.)

JANET: Don't you see what this is doing to you?

HAROLD: Time Janet, time. How many powdered milks?

JANET: Twenty-two. That's how many we had last night - how many we had the night before - how many we had when we started. That's how many we bought!

HAROLD: Christ, I don't need your attitude.

JANET: What do you need from me?

HAROLD: Where's the powdered milk? I need you to take this seriously.

JANET: I am - I have been.

HAROLD: Flashlights, Janet! Four minutes, ten seconds! Do you know how behind we are? Do you? (She sits') Wait what are you doing? Sitting? You can't sit. No - get up and help me. If you don't, we'll do it again. Is that what you want?

JANET: No, Harold.

HAROLD: This is serious stuff I mean Kennedy said - (Grabs news clipping') it's right here! The Russians could attack us. And you know he doesn't joke. We have to be prepared. Kennedy said -

JANET: (Mockingly.) "Kennedy said - Kennedy said."

HAROLD: When this thing hits Janet - and it will - it will level everything. The schools, post office, library, your goddamn hair salon - people - family. But not us, you hear me? And all those neighbors -

JANET: The ones that look at us funny -

HAROLD: They look at us funny because they're not prepared - the hell with them. They don't believe. (Looks at stopwatch.) Three and a half minutes! Checklist!

JANET: (Mockingly.) Three and a half minutes! Three and a half minutes! Checklist!

HAROLD: Don't mock me.

JANET: (Mockingly.) "Don't mock me."

HAROLD: And where's the water? Did you refill the water bottles today? Where's the fresh water?

JANET: I forgot.

HAROLD: You what?! What good is the powdered milk without water?

JANET: I forgot - the bottles are in the garage.

HAROLD: Christ, how could you forget - do you know how important it is to have fresh water? Every day I say refill - and where are the flashlights!

JANET: Every day - I'm sick of filling up one hundred and fifty-two bottles of water! Earthly sick of it! Do you know that yesterday when I was filling them up in the bath tub, I about drowned? I slipped and hit my head. Did you even ask about the bump on my head? No.

HAROLD: Why is this box empty?

JANET: Don't you care? I could have been dead filling up these goddamn bottles up for a bomb that will never hit us! That's right - I don't think it will hit us. I think it's all a crock of - of -

HAROLD: Don't you even finish that thought.

JANET: I'm right.

HAROLD: We did this together - together.

JANET: No, you did this. I did it for you. All I heard for six weeks was, "a shelter Janet, that's the only way we'll survive." I agreed because that's the only way I could survive with you - if I heard you mention the shelter one more day -

HAROLD: This is a fine time - (Looks at the stopwatch again.) Christ - less than two minutes! Now's not the time for this. Unbelievable! This box has bricks in it -

JANET: Unbelievable? You're unbelievable - do you know how much money we've spent on this junk?

HAROLD: Now it's junk?

JANET: Yes! It's junk.

HAROLD: Well, we'll have tons of money after the goddamn bomb hits - tons! All those idiots that didn't protect themselves - it'll be like a free bank when we get out of here.

JANET: Will you listen to yourself? Everyone will be dead! There'll be nothing to buy!

HAROLD: Another box of bricks - who put these in here? Janet? Where are all the cans of food?

JANET: They're in the kitchen - where they belong.

HAROLD: They belong down here! Christ - (Looks at his stopwatch.) minute twenty! Now we'll have nothing to eat. How are we supposed to survive without food and water?! And where's my flashlight!!

JANET: We have each other.

HAROLD: You - YOU! You did this? AHHHH!

JANET: I left Band-Aids.

HAROLD: What?

JANET: In case we get cut.

HAROLD: Everything up above is going to be destroyed, and you managed to keep the Band-Aids. (Looks at his stopwatch.) Fifty seconds - forget the list - we have to get into position.

JANET: I'm not getting into position.

HAROLD: No, you have to - (He tries to take her, but she breaks free.)

JANET: And crouch for what - the next two hours.

HAROLD: That's what we're supposed to do.

JANET: Not me.

HAROLD: Why are you doing this? Survival, Janet - survival!

JANET: I'm not getting into that ridiculous position.

HAROLD: You have thirty seconds, Janet - do you hear me! Thirty seconds before it all blows up!

JANET: Bon Voyage!

HAROLD: Well, I'm getting down! You'll be sorry.

JANET: Then do it.

HAROLD: (He gets down on the floor.) Don't make me live like this - now get down! Please!

JANET: No.

HAROLD: Fifteen seconds. Janet! You listen to me goddamn it! Twelve, eleven, ten, nine - Janet - seven, six, five, four, three, two, one! (Beat ofsilence.) JANET!!!!!! GODDAMN IT - YOU'RE DEAD! ARE YOU HAPPY NOW! YOU RUINED IT! YOU SABATOGED ME - THIS EVERYTHING!

JANET: Good.

HAROLD: Good? GOOD?! CHRIST! What if this was real! YOU'RE GODDAMN DEAD.

DEAD, DEAD!!

JANET: Don't you get it? I DON'T CARE! (Beat) I can't take living in fear anymore! It's everywhere we go - the television - the radio - newspapers - that's all people talk about - that's all you ever talk about. Don't you see what it's done to us? We used to talk about dinner, children, how many cars you sold - we were normal. Now you're possessed and I don't even know you anymore. Every waking moment it's the shelter - get the food for the shelter, paint the shelter, breakfast, lunch and dinner in the shelter, drills in the shelter - reading in the shelter, boxes in the shelter, blankets, water, powdered milk - our whole life in this God forsaken shelter. Right now, I wish the bomb would hit this shelter and take us from our misery. BOOM! BOOOOOOM!!

HAROLD: Janet, they're out there - Communists - they don't believe like we do - they don't have freedom like we do - they hate us. They're waiting to get us. Waiting with their ships in the ocean or God knows where - off the coast - Christ, in our back yard - upstairs even.

JANET: Then so be it - there's nothing we can do.

HAROLD: You're wrong. We have this. Survival, Janet - survival! GOD DAMN SURVIVAL!

JANET: I DON'T WANT TO SURVIVE! (Pause') I'm sorry, Harold, but I don't want to be the only ones living. Don't you see, I couldn't bear to walk out of here and not recognize anything because it's been leveled - and say "hey, remember such in such was there - remember so and so - and here's their foot bone." No. I'd be like dying twice - dying alone. I like my memories the way they are - the schools, the children - you standing in the lot trying to sell Cadillacs. I don't want that to change. And I can't keep living like this every single day. This right now - this is killing me.

HAROLD: Well, you're wrong. And you know it. Checklist! (Looks at the checklist.) Now I have to make a replacement list. First, flashlights. (Knocks some boxes over in frustration.) Where did you put the flashlights!

JANET: Harold, let's leave this lunacy.

HAROLD: Now it's lunacy? Well, we got a war to fight - and I'm doing my part ... with or without you. Now as soon as I restock everything, I'm running the drill again, and again, and again. Until its right. (Beat.) Shhhh - did you hear that?

JANET: Hear what - I didn't hear anything.

HAROLD: That - I heard a noise - again. Upstairs. (He crouches behind some boxes.)

JANET: It's Pickles.

HAROLD: Christ. They're here. Them - THEM! Spies.

JANET: Harold! Please.

HAROLD: They're up there.

JANET: There's nobody up there! Harold –

HAROLD: Shhh -

JANET: (She removes her suit.) Harold ... I can't take this anymore. (Beat.) I'm going to Mom's or June's.

HAROLD: Don't go - please, they're up there. Get behind the boxes - hurry.

JANET: No. (Pause') I'm going - and I'm taking Pickles with me.

HAROLD: Janet - don't go up. They'll take you. Please Janet - I'm begging you - begging! (He grabs her.) We're safe here. We're survivors. We have to survive.

JANET: HAROLD! LET ME GO!!

HAROLD: (He lets go.) Alright - alright - shhhh, shhhh. Goddamn it - fine. (Dives back into the boxes.) Don't tell them that I'm down here. Promise me.

JANET: (Finishes removing her suit) There's no one up there -

HAROLD: (He reaches out and grabs her again more sternly.) Just promise me.

JANET: (Frustrated.) Harold - (Trying to make sense of his state of mind.) I promise. (He lets go and stacks the boxes.) I hope it ends soon. (Beat.) Goodbye, Harold.

HAROLD: (He momentarily stops stacking boxes and looks at Janet. Loud whisper.) You'll be sorry. Whether they get you upstairs - or when the bomb hits - you'll see - you'll be sorry! (Beat. He continues stacking the boxes. Janet slowly exits. Blackout)
```

---

## IC-0768: Family 2.0

- Title: Family 2.0
- Author (byline): Walter Wykes
- Work: Ten 10-Minute Plays: Volume II
- Publisher: Black Box Press
- Publication date as stated: July 2008
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SUGGESTED ROLES, HUSBAND, WIFE, SON, DAUGHTER, FIRST HUSBAND, FIRST HUSBAND/DOG
- Teaser before the introduction: Yes
- Spoken words (computed): 1151
- Already set (do not supply): none

### Source block (context only)

```text
Author: Walter Wykes
Book: Ten 10-Minute Plays: Volume II
ISBN: 978-0615240008
Publisher: Black Box Press
Date (Month/Year): July 2008
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: How many times have we heard the cliche, “The grass is always greener on the other side?”

ACTRESS: While the overuse of this phrase has mostly dulled its impact, people who experience the “grass is greener syndrome” endure a significant struggle.

ACTOR: They truly believe that there is always something better what they have.

ACTRESS: Whether it’s with relationships, careers, where they live, or their family, they always have one foot out the door.

ACTOR: Absurd?

ACTRESS: You have no idea!

TOGETHER: Meet Family 2.0 by Walter Wykes.
```

### Performance text (classify this)

```text
SUGGESTED ROLES:

Actor: Husband, Son, First Husband/Dog

Actress: Wife, Daughter,

A perfect-looking house-the kind you find in magazines. A perfect-looking wife puts the finishing touches on her perfect-looking living room. The front door opens and husband enters.

HUSBAND: Hi, Honey! I'm home!

WIFE: Who are you? What are you doing in my house?!

HUSBAND: I'm your new husband. Where should I put my coat? [He tries to kiss wife; but she backs away from him terrified.]

WIFE: Don't touch me! I'll scream! I'll call the police!

HUSBAND: Aren't you going to ask how my day was?

WIFE: [Attempting to pacify him] How ... how was your day?

HUSBAND: It was awful! Just like every other day! Same old boring job. Same old boring boss. Same old boring life. And then, on the way home, suddenly it hit to me -- why come home to the same old boring wife and house and kids and dog when I could try something new?

WIFE: But you can't just-

HUSBAND: I've always admired your home. It's very well kept.

WIFE: Thank you, but-

HUSBAND: I pass it every day on my way to work, so I thought today I'd give it a try. It has to be more exciting than the one I've been coming home to for the past fifteen years.

WIFE: But ... I already have a husband.

HUSBAND: He can have my life. Where does he work?

WIFE: He's an executive. At a technology company.

HUSBAND: Perfect! I love technology! All those little gadgets and stuff! It'll be great!

WIFE: Look, I'm ... I'm sorry your life is so boring. My life is boring too. But you can't just walk in here and expect us to-

HUSBAND: Oh! I almost forgot! I brought you flowers! [He produces a bouquet of flowers from his coat.}

WIFE: You brought me flowers?

HUSBAND: They're orchids-a symbol of rare beauty and eternal love-my love for you.

WIFE: My ... my husband hasn't brought me flowers in almost fifteen years.

HUSBAND: I wrote you a poem too.

WIFE: A poem?

HUSBAND: Would you like me to recite it?

WIFE: Well ... if you went to the trouble of writing it ... I ... I wouldn't want it to go to waste.

HUSBAND: You take my breath away. / Like the sunset or a summer day. / When I gaze at the moon / Or the ocean blue / They pale beside the sight of you. / You take my breath away.

WIFE: That's beautiful. You ... you really wrote that?

HUSBAND: For you. [Pause. She considers this.]

WIFE: Do you pee in the shower?

HUSBAND: Never.

WIFE: Hog the sheets?

HUSBAND: Nope.

WIFE: Snore?

HUSBAND: I don't think so.

WIFE: Any history of baldness in your family?

HUSBAND: On the contrary. We're very hairy.

WIFE: Would you do your own laundry or wait for me to do it.

HUSBAND: Do it myself.

WIFE: Fix the toilet or call a plumber?

HUSBAND: Fix it.

WIFE: Shingle the roof or buy a new house?

HUSBAND: New house.

WIFE: Anniversary in Maui or Vegas?

HUSBAND: Maui.

WIFE: You'll have to win the kids over first. Children! [Enter SON and DAUGHTER] Children, meet your new father.

HUSBAND: Hi, kids.

SON: You're not my father! You're a fake! An imposter!

HUSBAND: Do you like baseball? I'll take you to the Big Game.

SON: The Big Game?! No way! [He embraces husband] I love you, Dad!

DAUGHTER: What about me? I hate baseball.

HUSBAND: Do you like shopping? Here-knock yourself out. [He hands her a hundred-dollar bill.]

DAUGHTER: A hundred-dollar bill?! You're the greatest! [She kisses him on the cheek.}

WIFE: Go play in your room, kids. Your father and I need some time alone. [Exit kids.] Now where were we? [They kiss passionately. Enter FIRST HUSBAND]

FIRST HUSBAND: [Entering] Hi, Honey! I'm ... what's going on here?! What are you doing to my wife?! I'm calling the police!

WIFE: Wait! Give me your key.

FIRST HUSBAND: What?

WIFE: Your key. Hand it over.

FIRST HUSBAND: I don't understand.

WIFE: He's replacing you.

FIRST HUSBAND: Replacing me?

WIFE: That's right. He's in-you're out.

FIRST HUSBAND: But why?!

WIFE: He brought me flowers! When's the last time you brought me flowers?!

FIRST HUSBAND: (Stammers) I . . . I . . . I. . .

WIFE: Exactly. Now stop stuttering and hand over the key.

FIRST HUSBAND: But ... what about the kids?! You can't take the kids away from me! Kids! [Enter SON and DAUGHTER] You don't want me to go-do you kids?

SON: He's taking me to the Big Game.

FIRST HUSBAND: I'll take you!

SON: Too late. You had your chance.

DAUGHTER: Sorry. It's nothing personal.

WIFE: [Her hand outstretched.] The key.

FIRST HUSBAND: But I don't want to go! Please, I'll ... I'll do anything! Just let me stay! I won't bother you! I'll stay out of the way! I'll ... I'll be another kid! Or the family dog! [He assumes the character of a dog, wags his tail, barks]

SON: I've always wanted a dog! Please?! Can I keep him?! Can I?!

WIFE: I don't know. What do you think, Honey?

HUSBAND: He'd be your responsibility, son. We're not going to feed him for you, or take him for walks, or clean up his poop-

SON: I'll take care of him! I promise! [To DOG] Come here, boy! Sit! Roll over! Play dead! Good boy! [Dog follows all commands barking excessively]

DAUGHTER: Can I go shopping now? (She is ignored)

FIRST HUSBAND/DOG: Woof! Woof!

WIFE: I think the dog has to go.

HUSBAND: Son, take your dog outside.

SON: I can't. I have homework. [Exit son]

DAUGHTER: Can I go shopping or not? (she is ignored again)

FIRST HUSBAND/DOG: Woof! Woof!

WIFE: Honey, could you take care of the dog? (reproachfully) You told him he could keep it.

HUSBAND: Do we have a leash?

DAUGHTER: Is anybody listening to me? [Enter son with baseball and glove.]

SON: Hey Dad, can we play ball?

HUSBAND: I thought you had homework.

SON: I just finished.

HUSBAND: [To son] Here-take the dog outside.

SON: I have to poop. [Exit son]

DAUGHTER: Hello? I hate this family!

WIFE: [To husband} While you're out, can you take the trash? And could you do something about your daughter?

HUSBAND: What do you want me to-

FIRST HUSBAND/DOG: Woof! Woof!

HUSBAND: [To Dog] Shut up, you stupid mutt! (Dog continues barking and spinning in circles)

WIFE: I think he really wants to go.

DAUGHTER: What about me?! Does anybody care what I want?! [Enter son}

SON: The Big Game starts any minute! We have to go!

HUSBAND: [To wife] When ... when we get back it would be really nice to have some quality alone time if you know what I mean.

WIFE: It'll have to wait, Dear. You have responsibilities now.

HUSBAND: Responsibilities?! This isn't what I signed up for! You're just like my first wife!

WIFE: WHAT did you say?!!!

SON: We're gonna miss the game! We have to go NOW! You promised!

DAUGHTER: I asked first! It's not fair! You can't just ignore me!

FIRST HUSBAND/DOG: Woof! As the cacophony rises, everyone converges on HUSBAN.D They surround him like a pack of rabid wolves.

WIFE: Are you hearing me?! Are we clear on this?! It’s gonna take a LOT to make up for this little slip-up, Mister!

SON: All I wanted to do was go to the Big Game! But now it’s too late! I already told all of my friends we were going, and they’re all going to know what losers we are!

DAUGHTER: Am I invisible? Am I not even here? What do I have to do to get some attention in this house?!

FIRST HUSBAND/DOG: Woof! Woof!

HUSBAND: I NEED A NEW LIFE!!!
```

---

## IC-0769: Fat Pig

- Title: Fat Pig
- Author (byline): Neil LaBute
- Work: Not specified
- Publisher: Faber and Faber
- Publication date as stated: Nov 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS, TOM, HELEN, JEANNIE, CARTER
- Teaser before the introduction: Yes
- Spoken words (computed): 1543
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Labute
ISBN: 978-0571211500
Publisher: Faber and Faber
Date (Month/Year): Nov 2004
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: Fat Pig by Neil LaBute.
```

### Performance text (classify this)

```text
NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: ACTOR: Tom

ACTRESS: Helen, (voices of Carter & Jeannie during Tom’s monologues) Helen in a crowded restaurant, standing at one of those tall tables. A bunch of food in front of her, and she is quietly eating it. By the way, she’s a plus size. Very. After a moment Tom enters, juggling a lunch tray. He looks around, then moves toward her

TOM: (Pg 5) . . . pretty big.

HELEN: Excuse me?

TOM: I’m sorry, I was just sort of, you know, speaking out loud. Pretty big in here. That’s what I was saying . . . Lots of room for, you know, people. (Looks around, trying to see if there’s a spot for him)

HELEN: You can eat here if you want. (She stares at him a minute, then slides some of her food to one side, allowing him a space) (Pg 6-7) I thought you mean me. Before. When you said that, “pretty big,” I though you were saying that to me. About me.

TOM: Oh, no, God, no! I wouldn’t . . . that’d be . . . you know. Rude.

HELEN: You’d be surprised. People say all kinds of things.

TOM: So . . . you mean, people actually . . . what? Say things to your face?

HELEN: Of course. All the time. It’s not a huge deal – I was just mentioning it. You get used to it. I guess they think that – I don’t know, after a certain size or whatever . . .

TOM: Hey, you know . . . It’s your . . .

HELEN: How does that sentence end?

TOM: Badly, I’m sure! Hell, it’s your body, you do what you want. That’s what I think . . . I mean, look at me. . . . look how much chicken they put on my salad!

HELEN: So, do you really like sprouts or does that only hold true for me? (He laughs at this, and she joins in. Tom studies her)

TOM: (Pg 9-10) You have a terrific laugh.

HELEN: Thanks. The pizza’s terrific here. I come by all the time for it . . .

TOM: I’ll bet. (Looks over at her) I just me . . . you know. If it’s so good. I would understand . That. (Beat) Please help me.

HELEN: I get what you meant. You shouldn’t be so nervous . . . I mean, if we’re gonna start dating.

TOM: What?

HELEN: I’m kidding. (They laugh together. He looks around, self-consciously) I’m sorry. You should ‘ve seen your face . . . I though you were gonna choke on your avaocado there . .

TOM: That’s not true . . . come on. You just caught me off guard is all. Seriously.

HELEN: Anyway, I was just playing. Big people are jolly, remember? It’s one of our best qualities.

HELEN: (Pg 11) (Opens a pudding) You want one?

TOM: Nah, I shouldn’t . . .

HELEN: Why?

TOM: Excellent question. Okay. (He takes a tub of pudding from her an digs in.) Mmmmmm . . . wonderful. Haven’t done that in ages.

HELEN: What?

TOM: Enjoyed myself. Like that. Put something in my mouth without reading the back label like some Bible scholar . . . (He gives an example – holding the pudding up to the light as if it was an antiquity and squinting at it. Examining it from all angels. This makes her laugh again. A lot) (Pg 13) Listen, I’m . . . I need to get back to the office . . but could we . . . I dunno what I’m asking here. Should we see each other again? (He reaches out for Helen’s hand)

HELEN: (Pg 14) (Smiles) . . . . Helen. My name’s Helen. (Pg 13) Yes. We should. (Pg 28) You have my hand there, you know.

TOM: Yeah, I . . . is that not . . . ?

HELEN: It’s fine. Just wanted to ask and see if it was an accident or not.

TOM: Ummm . . . no. It wasn’t, no. But . . . now you’re making me self-conscious. (Tom looks around the restaurant) (Pg 13) Lunch? Or, ummmm, dinner . . . ?

HELEN: I don’t only eat. I can be coaxed into doing other stuff too . . . (Pg 14) (She reaches over and takes a pen out his shirt pocket and writes her number down on a napkins)

TOM: Of course! I didn’t mean . . .

HELEN: I know. It’s a joke. (Pg 31) Ummmm, you probably couldn’t guess, but I didn’t date a lot when I was in school. (whispers) I used to be a touch heavy. (Helen chuckles. Tom joins in halfheartedly, then stops)

TOM: (Pg 14) No, yes, I get it now . . . but you shouldn’t do that though. Make fun of yourself so much.

HELEN: (Pg 31-32) It’s not a shame thing for me. Not anymore.

TOM: “Anymore?”

HELEN: Well . . . it’s all shame when you’re younger, isn’t it? You hate how you look. But I’m pretty all right with who I am now. The trick is getting other people to be okay with it!

TOM: (Tom looks at her in admiration) (Pg 13) I’ll call you. And I’m Tom, by the way.

(Helen exits She will provide Carter and Jeannie’s lines from off stage as if they are echoing in Tom’s head) (Tom to audience) (Pg 52) I just took her out a few . . . she’s nice. Okay?

JEANNIE: (Pg 67) She’s really fat, Tom! A fat sow and you know it.

TOM: (Pg 53) She’s not all worried about [weight], buying into all those dietary fads. Which is sort of refreshing, actually . . . Because you know . . .

CARTER: (Pg 45) Oh-my-God – I gotta go find my camera . . . “Tommy Joins the Circus!”

TOM: (To audience) (Pg 53) Yeah, I think she’s pretty as well, but we don’t ever talk about that. She’s happy with who she is and so . . . it’s . . . (Pg 52) (Pulls a snapshot out of his wallet)

CARTER: (Pg 53-54) (Peering over Tom’s shoulder) If she lost, like, eighty pounds, she’d be kinda stunning. Could probably get on one of those reality shows

TOM: (To audience) (Pg 56) Seriously, I haven’t felt this way for a long time. Ever, probably. I mean it. (Beat) . . . This is completely different. (Pg 67) She’s not obsessed with looks and money and clothes and useless bullshit like that. (Beat) I like who I am when I’m with her . . . .

JEANNIE: (Pg 66) You know what everybody is saying, right? And it doesn’t even faze you, huh? At all?

TOM: (To audience) (pg 71) I dunno, I like her. A lot. She makes me happy, and I really wanna make her happy too. Things aren’t just based on appearance!

CARTER: (Pg 49) Take a look in the mirror, you cow!! You don’t like being fat, there’s a pretty easy remedy. Do-no-jam-so-much-food-in-your-gullet. It’s not that hard

TOM: (To audience) Right. I guess that’s true. (Beat) It’s confusing, though. I wanna be better at that sorta stuff, but a lot of the time I’m just . . . yeah. A big wuss and I hate that! Despise that about me, but God, it’s . . . . No I’m gonna work on it, I’ll . . . I’ll . . (Scene shift)

HELEN: (Pg 56-57) So, you feel comfortable with me? I mean . . .

TOM: I adore you. This feels so damn good! You know? I mean . . . just us together. All alone. It’s like we’re on a raft of something. No one around to bug us. Ahhhhh, this is the life!

HELEN: I dunno, I just . . . I do feel kind of isolated. At times.

TOM: Helen . . . haven’t I been with you every day? I mean my friends have even noticed it. I’m hardly with them anymore.

HELEN: But . . . that’s what I mean. (Pg 58-59) I mean, we’ve been going out for like . . . however long, and I only met that one guy. Carter.

TOM: That’s true, but . . . I’ve been waiting for the right time or something. One of those office parties or . . . maybe on the Fourth or . . . we do a big party at the beach. A cookout and stuff.

HELEN: Great . . . should I go with a thong, or be a little more conventional?

TOM: Very funny. I was being serious . . . (a silence drops over them)

HELEN: It’s just a little like we’re, I dunno, hiding or whatever from people. Every time we end up in the back of a café or slipping into a movie late, after it’s already going – some little thing in my head, this warning buzzer says, “Watch it. Just watch out.”

TOM: Helen . . .

HELEN: I just hope you’re not embarrassed by me in some way, because . . . I don’t know what . . .

TOM: No. Why would you say that? I’m not at all . . . (Scene break and actors pantomime getting settled on the day of the beach party) (Pg 79-83) I just wanted to get us near the dunes here, so we’d have a little protection from the wind, that’s all.

HELEN: But we haven’t . . . we didn’t hardly talk to –

TOM: I introduced you to people . . .

HELEN: In the parking lot! As you and I were unloading stuff out of the car. That’s not an introduction.

TOM: Shit. I knew this would happen!

HELEN: You knew it would happen because you know who you are. I don’t think you’re ready for this. Tom . . . what’s going on?

TOM: Helen, come on, stop now! Shit . . . this is my company picnic, okay? We’re supposed to be having some fun.

HELEN: “Fun.” Okay . . . Let go join in the big [volleyball] game. (Helen jumps up and down a few times, miming s a few shots as Tom watchers. He looks over to where his friends are.) Come on, Tom! It’s fun!!

TOM: Stop it! Stop!! (Looks around to make sure not one is watching) Helen, please stop that.

HELEN: It is pretty obvious that there are some problems here. Tom, tell me about it. I know you’re thinking something, so we might as well just . . . One more thing. Just this. And I’ve never said this to anyone, not any other person in the world. Ever . . . I would change for you. I don’t mean Slim-Fast or that one diet that the guy on TV did . . . with the sandwiches from Subway.

TOM: Helen . . . that . . that’s not . .

HELEN: I’ll do something radical to myself if you want me to. Like being stapled or having some surgery or whatever it takes – because I do not want this to end. I just wanted you to know that. (Tom looks off in silence) This would be an excellent time to say something sweet to me. IF you at all care about my feelings.

TOM: I know. I’m . . . (Beat) Helen, that was such a nice thing to offer. And I appreciate it so much. (Tries to smile) Look, Helen . . . I’ve been thinking. (Beat) Listen . . . If we were in some other time or a land that nobody else was around one – then everything might be okay. I wouldn’t be so paranoid about what the people around me were saying. Or even thing. Then it could just be you and me, and that’d be so great. Perfect. But . . . I guess I do care what my peers feel about me. And maybe that makes me not very deep or petty or . . .

HELEN: Tom, don’t do this, okay? Please don’t. (Helen begins to cry and exits. She will provide Carter and Jeannie’s lines from off stage as if they are echoing in Tom’s head)

TOM: (To audience) I want to be better, but I . . . I can’t

CARTER: (Pg 44) Fat.

JEANNIE: Huge. A pig!

TOM: (Pg 83) (To audience) I mean, I could barely drive here today because my hands were shaking the whole time. . . .

CARTER: (Pg 48) I know what it’s like, I mean, why you [are] so embarrassed

TOM: (Pg 83) (To audience) And these are all the people that I know! I’m just not gonna be able to do this, on like, a daily basis.

JEANNIE: (Pg 67) And forgive me for saying it, but she seems a little obsessed with some things . . . like maybe Cheetos.

TOM: (Pg 83) (To audience) (Starts to cry) God . . . look at me! All this love inside and it’s not nearly enough to get around the shit that people heave at you . . . I feel like I’m drowning in it. I’m not brave. (Pg 84) I’m a weak and fearful person and I’m not gonna get any better.
```

---

## IC-0770: The Father

- Title: The Father
- Author (byline): Florian Zeller (translated by Christopher Hampton)
- Work: Not specified
- Publisher: Dramatist’s Play Service
- Publication date as stated: Aug 2017
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ANDRE, ANNE, MAN, ANDREW, WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1039
- Already set (do not supply): none

### Source block (context only)

```text
Author: Florian Zeller (translated by Christopher Hampton)
ISBN: 978-0822236344
Publisher: Dramatist’s Play Service
Date (Month/Year): Aug 2017
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Andre is a man facing persecution from all sides, and he refuses to take it any longer.

ACTRESS: First some girl, a “helper” -- whom he doesn’t need at all -- steals his favorite watch.

ACTOR: Then his daughter Anne tries to take his apartment away –

ACTRESS: The beautiful apartment he’s had for over thirty years, in which he is still quite capable of living, thank you very much!

ACTOR: After all, he still has all his faculties. . . Doesn’t he?

ACTRESS: *According to Columbia University Medical Center 10% of US adults over the age of 65 suffer from dementia.

ACTOR: A number that is expected to more than double by the year 2060.

ACTRESS: The Father by Florian Zeller and translated to English by Christopher Hampton presents a sobering and realistic look at the world through the eyes of a man experiencing dementia.
```

### Performance text (classify this)

```text
Suggested Roles: Actor – Andre Actress – Anne, Man, Woman

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

ANDRE: (Pg 6-7) I’m telling you. She stole my watch.

ANNE: Isn’t it more likely you just lost it?

ANDRE: No, no, no. I set a trap for her. I left my watch somewhere, out in the open, to see if she’d take it.

ANNE: Where? Where did you leave it?

ANDRE: Mm? Somewhere. Can’t remember. All I know is it’s now nowhere to be found. Nowhere to be found. I can’t find it, there’s your proof. That girl stole it from me. I know it. So, maybe I called her a . . . Maybe I got a bit annoyed.

ANNE: I don’t know what to do, Dad. She doesn’t want to work here anymore. This is the third one you’ve . . .

ANDRE: I don’t need her! I don’t need her or anyone else! I can manage very well on my own!

ANNE: (Pg 8) Dad, you have to understand. I can’t leave you on your own. You have to accept the idea that you need someone. (almost to herself) Why can’t you understand?

ANDRE: (Pg 11-13) (alone) I’ve got to find that lawyer’s number. I haven’t lived all these years to be treated like this. No. I’ve got to phone . . . Yes. A lawyer. My own daughter . . . My own daughter . . . (a man suddenly appears)

MAN: Everything all right?

ANDRE: What are you doing in my apartment?

MAN: Andre, don’t you recognize me? It’s Pierre . . . I live here.

ANDRE: You live in my apartment? What is this nonsense.

MAN: I’m going to phone Anne. (he moves towards the phone) Your daughter . . .

ANDRE: Thank you. I know who Anne is! You a friend of hers? (no answer) I’m speaking to you. Do you know Anne?

MAN: I’m her husband . . . (Pg 14) (Andre tries to remember the name) Pierre.

ANDREW: (Pg 12) (caught off-guard) You are?

MAN: Yes, coming up on ten years (he dials a number)

ANDRE: (trying to cover his confusion) Of course. Yes, yes. (Pg 14) That’s right, Pierre. (Pg 12) Ten years, already? Time passes so fast . . . I thought . . .

MAN: (on the phone) Hello, darling. Will you be done soon? Your father isn’t feeling very well. I think he’d like to see you. Yes. Don’t be too long. (he hangs up) She’ll be here soon – just out shopping.

ANDRE: She told me she was going to go and live in London.

MAN: I don’t think so, Andre.

ANDRE: I’m not an idiot. She told me she’s met an Englishman. She was moving to go and live with him. (suspicious, then he figures it out) You didn’t know anything about the Englishman?

MAN: (amused) No.

ANDRE: Oops-a-daisy! (he comforts Pierre) Chin up. They all end up leaving sooner or later. I speak from experience. (brief pause) (Pg 14-15) . . . What was I going to say? Oh, yes, your wife! She’s cooking up something against me. I suspect she wants to put me in a home for . . . Yes, she does. For . . . (he pulls a face representing an old man) But let me make something absolutely clear: I’m not leaving my apartment! I’m not leaving it!

MAN: This isn’t your apartment, Andre. You moved here, to our place while . . .

ANDRE: (laughs and rolls his eyes, the turns away) Now I’ve heard everything!

ANNE: Are you all right, Dad? . . . Dad? (he turns back, but doesn’t recognize her)

ANDRE: What is this nonsense? (Pg 16-17) Where’s Anne?

ANNE: I’m here, Dad. (she realizes he doesn’t recognize her) I went to do some shopping and now I’m back. Is everything’s all right.

ANDRE: (annoyed) I was just standing there. Standing quietly in the living room looking for a telephone number and suddenly your husband arrived and . . .

ANNE: Dad, I’m not married. I got divorced more than five years ago. Have you forgotten.

ANDRE: What? Well, then who’s he?

ANNE: Who?

ANDRE: Are you doing this on purpose? Him! Who just left with the chicken. (clearly, she doesn’t know what he’s talking about) The chicken! A minute ago, you were holding a chicken, were you not? A chicken. A CHICKEN! All this nonsense is driving me crazy.

ANNE: (Pg 18-19) Now don’t worry. Everything’ll sort itself out. Mm? (tenderly) Don’t worry. Have you taken your pills?

ANDRE: What’s that got to do with anything? There was this man claiming this wasn’t my apartment. He told me . . .

ANNE: Let’s give you your pills. The evening dose. Then you’ll feel better.

ANDRE: This is my apartment, isn’t it? Anne . . . This really is my apartment, isn’t it? (he turns away, and when he turns back, Anne has become an unknown man)

MAN: (Pg 47-48) Can I ask you a question? (the man moves closer, there’s something threatening about his approach) I want an honest answer . . . can you do that for me?

(Andre is caught off-guard and is clearly intimidated and frightened) How much longer do you intend to go on ruining your daughter’s life? (he slaps Andre)

ANDRE: What are you doing? I can’t allow this.

MAN: You can’t allow it? (he smiles and slaps Andre again)

ANDRE: Stop it! Do you hear me? Stop this at once! (Andre crouches and covers his face, in a humiliating defensive position and the MAN morphs back into ANNE)

ANNE: (Pg 49-50) Dad . . . Dad . . . (she gently pulls his hands from his face) What’s the matter? Look at me. Are you all right? What is it? What’s the matter (Andre begins to sob, Anne holds him in her arms and strokes his hair)

ANDRE: What time is it?

ANNE: It’s eight o’clock. Time to eat.

ANDRE: Eight o’clock in the evening? But I thought it was morning. I’ve only just got up. Look, I’m still in my pyjamas. (he seems very lost) (Pg 54-55) I have to get dressed. Where are my clothes?

ANNE: Dad. You can get dressed later. There’s nothing to worry about.

ANDRE: I’m in my pyjamas. I have to put my pants on (he shuffles off stage then wanders back in, confused) ***** Scene change**** A white bed, reminiscent of a hospital bed. Andre doesn’t know where he is. A woman wearing a white coat comes in.

ANDRE: (Pg 58-59) Who put this bed here? In the middle of the living room? Anne! This is really getting out of hand.

WOMAN: Don’t get upset.

ANDRE: I’m not upset. You just don’t put a bed in the middle of a living room. It doesn’t make any sense at all. Where’s Anne?

WOMAN: Look, I’ve brought you your medication.

ANDRE: What are you, a nurse? (finally realizing who he’s talking to) Oh, you are. . . I see. You’re a nurse. What are you doing here?

WOMAN: Looking after you.

ANDRE: Amazing! Nobody tells me anything in this house. I really need a little word with Anne. What time is it?

WOMAN: Time for your medication.

ANDRE: Yes, all right, fine. Let’s take the medication (makes a big show of it, then notices his watch isn’t on his wrist) I’ve lost my watch! (Pg 6) That girl stole it from me. I know it! (Pg 59) Anne? Anne!?

WOMAN: Your daughter isn’t here, Andre . . . remember, your daughter lives in London . . . (Pg 60) But she comes to see you sometimes.

ANDRE: What is this nonsense? (very confused) (Pg 61-62) Sorry to ask this, but my mind’s gone blank . . . I mean, you . . . You . . . Who are you exactly?

WOMAN: I’m Martine.

ANDRE: Martine. That’s right. Yes, yes, yes. Martine. Right. Right. And . . . What about me?

WOMAN: What about you?

ANDRE: Me . . . Who exactly am I?

WOMAN: You? You’re Andre.

ANDRE: Andre?

WOMAN: Yes.

ANDRE: Are you sure?

WOMAN: (amused) Yes.

ANDRE: Andre? Nice name, Andre . . . Don’t you think?

WOMAN: It’s a very nice name.

ANDRE: My mother gave it to me, I imagine. Did you know her? My mother?

WOMAN: No.

ANDRE: She was so . . . she had very big eyes. It was . . . I can see her face now. I hope she’ll come and see me sometimes. Mommy. Do you think she might come occasionally for the weekend . . .

WOMAN: Your daughter?

ANDRE: (he’s crushed by sudden grief) No, mommy. I . . . I want out of here. Someone come and get me! I want to go back home. (he sobs)
```

---

## IC-0771: Feeding the Moonfish

- Title: Feeding the Moonfish
- Author (byline): Barbara Wiechmann
- Work: Telling Tales: New One-Act Plays
- Publisher: Penguin Books
- Publication date as stated: February 1993
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: EDEN, MARTIN
- Teaser before the introduction: Yes
- Spoken words (computed): 2652
- Already set (do not supply): none

### Source block (context only)

```text
Author: Barbara Wiechmann
Book: Telling Tales: New One-Act Plays
ISBN: 978-0140482379
Publisher: Penguin Books
Date (Month/Year): February 1993
```

### Introduction (context only: never use it for content warnings)

```text
EDEN: Feeding the Moonfish MARTIN: by Barbara Weichmann
```

### Performance text (classify this)

```text
EDEN: You want a Bud?

MARTIN: Who gave you beer?

EDEN: I brought two Buds-one for you and one for me.

MARTIN: You shouldn't be stealing beer from the restaurant.

EDEN: God. It's just a coupla beers.

MARTIN: Doesn't matter.

EDEN: All right. All right. but it's no big crime to drink a beer with me. I ain't no alchy or nothin so you don't have to worry I'm gonna throw up all over you or pass out or somethin. I just thought you might get hot out here that's all. (She hands him the beer.)

MARTIN: All right. Thank you. (He starts to pull the beer tab.)

EDEN: You might wanna be careful.

MARTIN: You shook this up? What are you giving me shook-up beer for?

EDEN: I didn't shake it up. I don't even know if it is shook up. I just was saying that it could be.. I was only doin you the courtesy of warnin you.

MARTIN: O.K. O.K.

EDEN: I like the nighttime. Did you ever notice at night the way you can open up to people. You can open -right up the way you never could in the daytime?

MARTIN: I don't know.

EDEN: I think I come out at night-you know-like a creature, a sci-fi creature.

MARTIN: Yeah. You're a creature all right. (looks back down at the lake)

EDEN: You like them fish don't you?

MARTIN: This place used to be fantastic. There was a marina. Men would come here and fish. .

EDEN: They fished for the moonfish? They ate the moonfish?

MARTIN: Sharks. They fished for sharks.

EDEN: Sharks.

MARTIN: They hunted em. Took their boats through the channel to the ocean and hunted em. They had contests. I watched them haul em in off their boats an dump em on the dock. Hammerheads, tigers, gray nurses. They slaughtered em.

EDEN: Yeah?

MARTIN: They dumped em in piles and left em. Bellies up, hooks in their mouths, piled to the sun.

EDEN: That's it? What else?

MARTIN: Nothing. EDEN (pause): What do you think people do in prison?

MARTIN: What?

EDEN: My mom's in Sing Sing. Arrested for my dad’s murder. She and my Grandma beat him to death.

MARTIN: Your mom's really in jail?

EDEN: Do you think she’s having an O.K. time behind bars? I brought her some stuff to make an afghan with but they took away the crochet needles. They said they was lethal weapons. I hope she ain't too bored. She don't know what to do without something in her hands.

MARTIN: She beat your dad to death.

EDEN: She tried. My grandma's the one that killed him. That dealt the actual death blow.

MARTIN: Your grandma killed him?

EDEN: She sure did.

MARTIN: Why'd she do it?

EDEN: He used to beat my mom on a semi-regular basis, an this time she was fighting for her life-right? He was choking her. It wasn't even like she had time to think of possible consequences or nothing-she had no choice. She was makin the best of the situation. She found her only opportunity, grabbed the waffle iron with her one free hand, and beamed him with it. Then she called Gram to help her come finish.

MARTIN: He beat you too?

EDEN: Naah. He couldn't beat me-he weren't my blood dad. Just her he beat.

MARTIN: Don't it bother you?

EDEN: Well, what do you think, you must be a moron or something. Wouldn't it upset you? So I'm in homeroom and this announcement comes over the P.A. "Eden Banaglione please report to the front office.” Like that-so right away the entire student body of my homeroom thinks it's got to do with me taking these pills in the lav-only they weren't pills they was only Tylenol-so I get to the office and them ugly hairdos are looking at me kinda funny and then they lay it on me- your dad's been bashed to death by a waffle iron, Eden-Your ma's been hauled away to some mental prison, and your grandma's nearly croaked herself in the process of the beating. Now, here's a permission slip, go home honey." Wouldn't it upset you? I mean wouldn't it?

MARTIN: Jesus, calm down, you're all worked up.

EDEN: Of course I'm worked up. Why shouldn't I be? I try to make one single friend and all I get is shutting doors. He don't wanna talk, he don't wanna listen, he just wants to watch these weird fish all night.

MARTIN: I been listening to you. I'm listening.

EDEN: No. Why should you listen to me. Why should you understand. There's no rational way to account for the disgusting things I've seen in my life.

MARTIN: You can be a drag you know that? Maybe you're just young but even if you ain't lying you ain't the only person's ever seen disgusting things go on in this world, and if you are lying, shit, I could make up stories same as you that'd make your heart bleed into little pieces. So your mom's a little high-strung-I could tell you that I didn't ever have a mom

EDEN: And I could tell you I once worked bachelor parties in order to put food on the table.

MARTIN: I could tell you a brick fell on her head and split her skull wide open one day as she was breast-feeding me

EDEN: I could tell you my grandma was a schizophrenic, I could tell you my father was a junkie and made me his love slave

MARTIN: I could tell you my father slit his throat-what do you want me to do? What's the matter?

EDEN: Nothing.

MARTIN: Look, I'm sorry I ain't been nice to you. I guess I'm just not very nice, you know?

EDEN: Bull

MARTIN: Come on. Come here. Aren't you sleepy? You wanna sleep here or something? (She shakes her head.) Here blow your nose. Don't get all snotty on me. You wanna eat something? I got a ham sandwich in the glove compartment.

EDEN: I already ate.

MARTIN: What?

EDEN: Burt's birthday cake.

MARTIN: What, back at the restaurant? You didn't eat any dinner. You didn't eat anything healthy. Don’t give me that. That's disgusting.

EDEN: I'm not disgusting.

MARTIN: Grow up, I seen you. You let those guys up there-horny old guys-you let them pinch your bun and feed you cake and beer.

EDEN: God, you're such a preacher.

MARTIN: Look, I'm sorry, you shouldn't wear those little cut-off shorts. Your butt hangs out, you know that? I mean don't take this wrong but it's just a plain come-on.

EDEN: Look, you don't have to go playing saint on me or nothing. I ain't your kid or some ugly little sister of yours that can't get a date. I ain’t a slut you know.

MARTIN: What does that have to do with anything?

EDEN: You're so cool ain't you? I hear things. What you done to girls. What you done to that girl. You thought she was some dumb slut so it didn't matter none. You thought she had no brains.

MARTIN: What are you even talking about?

EDEN: I hear. I hear. You come out here at night and some girl you think is scum gets drunk and you just let her wander around by herself cause she bugs you. You just let her wander around all miserable and throwing up

MARTIN: People make up stories.

EDEN: All miserable and throwing up and you could care less she gets hurt out here on this rusty old dock. You wouldn’t care if she falls in, and can't see and can't swim and screams and screams and panics and you don't even come help her.

MARTIN: Shut up. Shut up.

EDEN: You coulda saved her but you let her drown. You watched her drown I'll bet.

MARTIN: Shut up. (He moves to strike Eden, but stops himself before his fist makes contact.) I never touched you.

EDEN: (Pause) I know. I know that. It's O.K. You think I'm a slut or something but you know something, it doesn't matter to me. You know that? I don't care you think that.

MARTIN: I don't think you're anything.

EDEN: That's O.K. too. You can say that. That's what he said about her. About my ma. That's what he told her. But it weren't true. She was real special to him. She could take him.

MARTIN: What are you talking about?

EDEN: He hit her. He could hit her again and again, and she'd be screaming and throwing furniture, but she could take it. He could do anything and it was O.K. because she loved him so much and she knew how much he loved her cause she was the only one that could take him. You understand? She was special. He didn't do that stuff to no one else. He could fool around on the side but in the long run it was her. She weren't just nothing to him. She was it. She was his living end.

MARTIN: She killed him.

EDEN: Sure. Jealousy. She had to have him for herself completely.

MARTIN: I thought you said she was fighting for her life.

EDEN: Conveniently. She woulda killed him anyway sooner or later. Just to finally have him. She loved him so much. To this day his memory is sacred to her. She's got a framed eight-by-ten of him hanging on the wall of her cell in the slammer. See, their bodies was made to be with each other. That's what I think. Gravity was pulling em to each other. They was real helpless. They couldn't change nothing though. They couldn't change see. That's why it don't matter what you think of me

MARTIN: I don't even know you.

EDEN: It don't matter. There ain't nothing you could say or do or think that would change anything so what's to be afraid of right? I'm not afraid of you. It don't matter what you done to some girl. You could burn people's furniture cause you didn't like the color, set fire to your neighbor's front lawn and watch the grass grizzle up, you could kill someone -you could never speak another word to me in your life, and it wouldn't matter. I'd still care for you.

MARTIN: You know, I think you're a little sick.

EDEN: That's O.K. too, cause I'm like you. It's nice here, huh? That breeze blowing and all -it's getting cool. That nice breeze, huh? You got such a beautiful face. I like you so much.

MARTIN: You like it here.

EDEN: I like it here with you. To be here with you. It's all beautiful now.

MARTIN: No, it's not the same. (Pause.) My dad would take me here.

EDEN: When you were a little kid?

MARTIN: He'd take me here. He'd show me the fish, all the different kinds. The rays. The squirrel fish and the parrot fish.

EDEN: He knew a lot.

MARTIN: At night we'd walk out here. We'd look for the moonfish. They'd come. I couldn't take my eyes off them. All those many fish, swimming in and out of the light, doubling in and off of each other, changing in and out with themselves till they became one silver river wrapped around the dock. Just to get the food. They do that, they become so beautiful just for the food. You wanna know something?

EDEN: What?

MARTIN: The fish talk.

EDEN: The fish talk. The moonfish?

MARTIN: Yes.

EDEN: What do they say?

MARTIN: Different things. What's so funny?

EDEN: You think you're so mysterious. What kind of different things? Will they talk to me?

MARTIN: I don't know. I don't think so. (Eden lies on her back staring up at the sky.) What are you doing?

EDEN: I'm listening. I'm listening co what them fish are saying.

MARTIN: You can't hear them.

EDEN: You wanna know what I hear, what they're telling me? They're saying: The man in the moon Looked out of the moon Looked out of the moon and said It's time for all of God's children To think about going to bed.

MARTIN: What's that?

EDEN: Shhh. Just be quiet, Martin. Aren't you sleepy now? We should sleep.

MARTIN: Maybe I am.

EDEN: We can sleep out here. We don't have to screw or nothing. I wanna be with you out here sleeping.

MARTIN: Maybe I am sleepy.

EDEN: That's good. We can just be here together. You wanna tell me something while I comb my hair? That's one thing, I comb my hair no matter what, every night one hundred strokes.

MARTIN: All right. Tell you something

EDEN: Tell me anything. Just close your eyes and tell me what you see. Close your eyes.

MARTIN: I'll close them for you.

EDEN: That's good. What are you thinking about now Maryin? What do you see?

MARTIN: I'm dreaming.

EDEN: What?

MARTIN: I'm waiting.

EDEN: What?

MARTIN: Him.

EDEN: Tell me.

MARTIN: I am waiting for my father. I sleep alone here. Each night I dream and in my dream I see him. Warmer, more real than in life. He watches me sleep and picks me up in his arms like I was a tiny boy and carries me out to the end of the dock. I am weightless. He points to the sky, there is no moon. The water. There is no tide. Only the world, our world in complete stillness. No flux, no pull, no gravity. Just me and him, me and him. We lie on our stomachs, stare down into the dock light, and he calls them. Waiting and waiting, I think "They won't come, there’s no moon." But they do come. And they take my breath away. Gigantic pale, and luminous silver, they're kissing the dock with their mouths, feeding on the life there, mingling with the dark water, and I watch till it's like I'm being hypnotized and then I feel him lift me up and up and his arms rock me and his voice in my ear, he tells me, he says to me: Now it is night we will walk to the end of the pier and watch the moonfish feed because it is night because that's what we do because so much is moved by the pull of the moon.

EDEN: Your dad tells you this?

MARTIN: He lifts me up and up and his kiss goes warm on my cheek, and my forehead and I see the silver of the fish and silver of the razor in his hand, and starting at his ear he slices down, down around the throat, and the red pours Onto the dock and through the planks and onto the moonfish-staining, covering, choking them. His hand goes limp, the razor falls, he crumbles to my feet and noiseless I push the body empty and light into the lake. Waves over him. Billows of blood and water. The downward spiral of flesh, of water. The sleep of water. Then it happens. They come for him. One by one gliding into his pool of blood, testing him with their mouths, each bite making him theirs, pulling him finally down with them into the darkness. They own him now.

EDEN: They own him now. .

MARTIN: He was so lonely for her. After she left him. He was so lonely. He couldn't sleep in their bedroom anymore. I'd find him in the morning in a ball on the living room floor. That's where he slept. A grown man. Cause he couldn't stand the loneliness.

EDEN: I wouldn't leave you.

MARTIN: He never hit her though. He never touched her, all them times they fought. He couldn't hurt anything. Not a bug, not a lousy fish. Only himself. He could do that.

EDEN: I would stay with you.

MARTIN: I guess it wasn't in him.

EDEN: You got such a nice face.

MARTIN: Sometimes I get this feeling, I'm walking down some road, this thing comes over me. I don't know what it is. I'm just walking and I see someone-some guy, some woman-they've got nothing to do with my life, I see them and I think "I could take him."

EDEN: I like you so much.

MARTIN: I could kill that guy over there. I'd like to kill him. It's not a rational thing. I never killed anyone, but I think I could do it. Maybe I'd like to.

EDEN: I'd still care for you.

MARTIN: You listen to me tell you this. You listen to me, and you just sit there like it was nothing. Like it was natural.

EDEN: Tell me I'm beautiful. (She places his hand on her hair, he begins to stroke it.)

MARTIN: You just don't understand anything.

EDEN: Tell me I'm beautiful. (She takes his hand from her hair and places it on her breast.)

MARTIN: Like it was natural.

EDEN: Tell me. (She takes his hand and places it on her throat-gently but in a choking hold-he holds it there for a moment, then finally begins to stroke her throat.)

MARTIN: You're beautiful. You're so beautiful.
```

---

## IC-0772: Fences

- Title: Fences
- Author (byline): August Wilson
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Jan 2000
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TROY, ROSE
- Teaser before the introduction: Yes
- Spoken words (computed): 1831
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
ACTOR: Pittsburg, Pennsylvania 1950

ACTRESS: It’s the beginning of the Civil Rights movement. And Troy and Rose Maxson are struggling. Struggling in life and in this scene struggling with their marriage.

ACTOR: What is it that makes a marriage? Love? Responsibility?

ACTRESS: And what can destroy it? Selfishness? Infidelity?

ACTOR: At the heart of Fences by August Wilson is a question that transcends race . . .

ACTRESS: What is our responsibility to ourselves versus to our family and society?

TOGETHER: Fences by August Wilson
```

### Performance text (classify this)

```text
TROY: (Pg 12) When I met this woman . . . I latched on to her. I latched on to her and told her “Baby, I don’t wanna marry, I just wanna be your man. She told me . . “You in my way. You blocking the view! Move out the way so I can find me a husband.” I though it over. . . Come back, told her “Okay, baby . . .”

ROSE: (Pg 90) When I first met [him] I was thirty years old and had done seen my share of men. But when he walked up to me and said, “I can dance a waltz that’ll make you dizzy,” I thought, Rose Lee, here is a man that you can open yourself up to and be filled to bursting. Here is a man that can fill all them empty spaces you been tipping around the edges of.

TROY: (Pg 60) She a good woman. I been married to her for eighteen years. She done carried me a long ways and I love and respect her for that. (pause) You can’t find a better woman than Rose. I know that.

ROSE: (Pg 91) When he walked through the house he was so big he filled it up. That was my first mistake. Not to make him leave some room for me. But at that time I wanted that. All wanted a house that I could sing in. And that’s what he gave me. I didn’t know to keep up his strength I had to give up little pieces of mine. I did that. (Pg 63) Well, everybody got their own way of looking at it I guess.

ROSE: (Pg 63 +) (enters scene with Troy) Come on and get your lunch. I got a bowl of lima beans and some cornbread in the oven. Come on get something to eat. (Rose turns to go into the house)

TROY: Rose . . . got something to tell you. (she stops and turns around) I don’t know how to say this. (pause) Can’t explain it none. It just sort of grows on you till it gets out of hand. It starts out like a little bush . . . and the next think you know it’s a whole forest.

ROSE: Troy . . . what is you talking about?

TROY: I’m talking, woman, let me talk. I’m trying to find a way to tell you . . . I’m gonna be a daddy. I’m gonna be somebody’s daddy.

ROSE: Troy . . . you’re not telling me this? You’re gonna be . . . what? You telling me you gonna be somebody’s daddy? You telling your wife this?

TROY: Rose . . . it’s just . . .

ROSE: Why, Troy? Why? After all these years to come draggin’ this in to me now. It don’t make no sense at your age. I could have expected this ten or fifteen years ago, but not now.

TROY: Age ain’t got nothing to do with it, Rose.

ROSE: I done tried to be everything a wife should be. You know I ain’t never wanted no half nothing in my family. My whole family is half. Everybody got different fathers and mothers . . . my two sisters and my brother. Can’t hardly tell who’s who. It’s your papa and your mama and my papa and my mama . . . And now you wanna drag your behind in here and tell me something like this.

TROY: You ought to know. It’s time for you to know.

ROSE: Well, I don’t want to know, goddamn it!

TROY: I can’t just make it go away. It’s done now. I can’t wish the circumstance of the thing away.

ROSE: And you don’t want to either. Maybe you want to wish me away. Maybe that’s what you want? Well, you cant. I’ve got eighteen years of my life invested in you. You ought to have stayed upstairs in my bed where you belong.

TROY: Rose . . . now listen to me . . . we can get a handle on this thing. We can talk this out. . . come to an understanding.

ROSE: All of a sudden it’s “we.” Where was “we” at when you was down there rolling around with some godforsaken woman? “We” should have come to an understanding before you started making a damn fool of yourself. You’re a day late and a dollar short when it comes to an understanding with me.

TROY: It’s just . . . She gives me a different idea . . .a different understanding about myself. I can step out of this house and get away from the pressures and problems. . . be a different man. I ain’t got to wonder how I’m gonna pay the bills or get the roof fixed. I can just be a part of myself that I ain’t never been.

ROSE: What I want to know. . . is do you plan to continue seeing her? That’s all you can say to me.

TROY: I can sit up in her house and laugh. Do you understand what I’m saying. I can laugh out loud . . .and it feels good. It reaches all the way down to the bottom of my shoes. (pause) Rose, I can’t give that up.

ROSE: Maybe you ought to go on and stay down there with her . . . if she a better woman then me.

TROY: It ain’t about noboby being a better woman or nothing. Rose, you aint the blame. A man couldn’t ask for no woman to be a better wife than you’ve been. I’m responsible for it. I done locked myself into a pattern trying to take care of you that I forgot about myself.

ROSE: What the hell was I there for? That was my job, not somebody’s else’s.

TROY: Rose, I done tried all my life to live decent . . . to live a clean . . . hard . . .useful life. I tried to be a good husband to you. In every way I knew how. Maybe I come into the world backwards, I don’t know. But . . . you born with two strikes on you before you come to the plate. You got to guard it closely . . . always looking for the curve-ball on the inside corner. You dan’t afford to let none get past you. If you going down . . you going down swinging. Everything lined up against you. (Pause) I fooled them, Rose. I bunted. When I found you and a halfway decent job . . . I was safe. Couldn’t nothing touch me. I wasn’t gonna strike out no more. I wasn’t going back to the penitentiary. I wasn’t gonna lay in the streets with a bottle of wine. I was safe. I had me a family. A job. I wasn’t gonna get that last strike. I was on first looking for one of them boys to knock me in. To get me home.

ROSE: You should have stayed in my bed, Troy.

TROY: Then when I saw that gal . . . she firmed up my backbone. And I got to thinking that if I tried . . . I just might be able to steal second. Do you understand after eighteen years I wanted to steal second. I stood on first base of eighteen years and I thought . . . well, goddamn it . . go for it!

ROSE: We’re not talking about baseball! We’re talking about you going off to lay in bed with another woman . . and then bring it home to me. That’s what we’re talking about. We ain’t talking about no baseball!

TROY: Rose, you’re not listening to me. I’m trying the best I can to explain it to you. It’s not easy for me to admit that I been standing in the same place for eighteen years.

ROSE: I been standing with you! I gave eighteen years of my life to stand in the same spot with you. Don’t you think I ever wanted other things? Don’t you think I had dreams and hopes? What about my life? What about me. Don’t you think it ever crossed my mind to want to know other men? That I wanted to lay up somewhere and forget about my responsibilities? That I wanted someone to make me laugh so I could feel good? You not the only one who’s got wants and needs. But I held on to you, Troy. I took all my feelings, my wants and needs, my dreams . . . and I buried them inside you. I planted a seed and waited and prayed over it. I planted myself inside you and waited to bloom, and it didn’t take me no eighteen years to find out the soil was hard and rocky and it wasn’t never gonna bloom. But I held on to you, Troy, I held you tighter. Cause you was my husband. Cause that’s the only way I was gonna survive . . . as your wife. You always talking about what you give . . .and what you don’t have to give. But you take too. You take. . . and don’t even know nobody’s giving! (Rose turns to exit; Troy grabs her arm)

TROY: You say I take and don’t give!

ROSE: Troy . . . you’re hurting my arm! Let go!

TROY: I done give you everything I got. Don’t you tell that lie on me.

ROSE: Troy!

TROY: Don’t you tell that lie on me! Don’t you tell me about no taking and giving. (releases her arm roughly) (Long beat)

ROSE: (gathers her strength) Tomorrow’s Friday. I want to know if you’re coming home.

TROY: I’m going over to the hospital to see Alberta. She went into the hospital this afternoon. Look like she might have the baby early. I won’t be gone long.

(The telephone is heard ringing inside the house; Rose exits into the house to answer the telephone. While she is gone, Troy picks up a baseball bat from beneath the tree and takes some practice swings. She returns)

ROSE: Troy . . . that was the hospital. Alberta had the baby. (Pause) It’s a girl.

TROY: I better get on down to the hospital to see her.

ROSE: Troy . . .

TROY: Rose . . . I got to go see her now. That’s only right . . . what’s the matter . . . the baby’s all right, ain’t it?

ROSE: Alberta died having the baby.

TROY: Died . . . you say she’s dead? Albert’a dead?

ROSE: They said they done all they could. (Troy exits)

*****

(PG 73) (Rose is on the porch waiting for Troy. He enters the yard carrying an infant wrapped in blankets; awkward silence)

TROY: Rose . . . I’m standing here with my daughter in my arms. She ain’t but a wee bittie little old thing. She don’t know nothing about grownups’ business. She innocent . . . and she ain’t got no mama.

ROSE: What you telling me for, Troy? (She turns away)

TROY: Well . . . A man’s got to do what’s right for him. I ain’t sorry for nothing I done. It felt right in my heart. (Pause) She’s my daughter, Rose. My own flesh and blood. I can’t deny her. (Pause) You is my family. You and this child is all I got in the world. So I guess what I’m saying is . . . I’d appreciate it if you’d help me take care of her. (He hands the baby to Rose)

ROSE: (She is torn, but her motherly instinct kicks in) Okay, Troy . . . you’re right. You can’t visit the sins of the father upon the child. A motherless child has got a hard time. From right now . . . this child got a mother. But you a womanless man. (She motions for Troy to leave. He does; she watches him walk away, then speaks to the audience) (Pg 90- 91) I took on his life as mine and mixed up the pieces so that you couldn’t hardly tell which was which anymore. It was my choice. It was my life and I didn’t have to live it like that. But that’s what life offered me in the way of being a woman and I took it. I grabbed hold of it with both hands. He meant to do more good than he meant to do harm. He wasn’t always right. Sometimes when he touched he bruised. And sometimes when he took me in his arms he cut. (Looking at the baby in her arms) By the time Raynell came into the house, we had done lost touch with one another. I didn’t want to make my blessing off of nobody’s misfortune . . . but I took on to Raynell like she was all them babies I had wanted and never had. . . . I’m gonna give her the best of what’s in me.
```

---

## IC-0773: The Ferris Wheel

- Title: The Ferris Wheel
- Author (byline): Mary Miller
- Work: Take Ten: New 10-Minute Plays
- Publisher: Vintage
- Publication date as stated: March 25, 1997
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JOHN, DORIE, BOTH
- Teaser before the introduction: Yes
- Spoken words (computed): 1737
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mary Miller
Book: Take Ten: New 10-Minute Plays
ISBN: 978-0679772828
Publisher: Vintage
Date (Month/Year): March 25, 1997
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Throughout our lives, we have chance encounters with people or situations that can be — and often are — life transforming.

ACTOR: Think back for a moment. How did you meet your spouse [significant other]?

ACTRESS: Sure, there are online matchmaking sites,

ACTOR: But most people meet the person of their dreams through a chance encounter —

ACTRESS: At a grocery store,

ACTOR: Or a dance class, or on . . .

TOGETHER: The Ferris Wheel by Mary Miller
```

### Performance text (classify this)

```text
A woman is seated with her arms outstretched in front of her, her fists clenched, her feet planted firmly on the ground and her eyes shut. A man enters. He looks down at the woman, then behind him, then back at the woman. He starts to sit next to her.

JOHN: Excuse me. Excuse me? I hope I’m not . . . crowding you . . .

DORIE: (flustered/embarrassed) No. (He slides into the empty seat next to her and takes hold of the “bar”)

JOHN: I would have taken another seat but the line is too long to let anyone ride by themselves (She nods but doesn’t respond) . . . They force you to be a couple whether you want to or not . . . not that I mind. I mean it’s a pleasure. (He looks at her, sitting bolt upright and perfectly rigid) Are you comfortable?

DORIE: Just fine (a jerk) Whoops . . . we’re off. (She squeezes her fists tighter, clenches her eyes shut and presses her feet to the floor)

JOHN: Are you all right?

DORIE: Couuuuldn’t be better.

JOHN: But you’re not looking?

DORIE: No. Heights. I’m frightened of heights.

JOHN: And you ride a ferris wheel?

DORIE: Just once a year. On my birthday.

JOHN: Happy birthday. (He looks at her gripping the bar) Your knuckles are turning white. . . Are you sure this is good for your circulation?

DORIE: What doesn’t kill me makes me stronger, type of thing.

JOHN: So you do this in lieu of a birthday part with cake and ice cream?

DORIE: Oh no, I have that too, when I get through. Like a reward. My Daddy started it and I keep it up.

JOHN: He was frightened of heights?

DORIE: Oh no, he just believed you should do something that frightens you at least once a year. Builds character. Strengthens moral fiber. You ought to try it sometime. I had this cousin once who tried to pretend like she was frightened of small places until she got locked in the attic during a thunderstorm. Lightning struck that house and burned it to the ground.

JOHN: Now she’s frightened of fire?

DORIE: No sir, she’s dead. You can’t go messing with things like this.

JOHN: Truth is stranger than fiction.

DORIE: Don’t you know it. Once I had this art teacher named Miss Thumb, who was missing two fingers. She used to say to paint all you needed were your ten good fingers and she’d hold up eight. (She demonstrates and then grabs for the bar) Whooopppsss!!

JOHN: Are you all right?!

DORIE: I’m fine. (pause) . . . . You’re not from around here?

JOHN: No. Passing through, saw the wheel and drove on over. That’s my little red car down there. (He points. She starts to look and stops)

DORIE: I’ll take your word for it. (Suddenly they both jerk forward in their seats . . . and stop still). Oh my God! What happened?

JOHN: Looks like we stopped. We seem to be stuck (He leans forward to look)

DORIE: Don’t do that!! Don’t move! You’re rocking the car. Please don’t rock the car.

JOHN: I’m sorry. They’re probably just making an adjustment. We’ll be moving . . . (They do not move. He looks at her) . . . any minute.

DORIE: Yes. (panic growing) We should be . . . rolling? Any . . . minute . . . ?!

JOHN: Would you care for a cigarette? Calm your nerves.

DORIE: Me? No. I don’t smoke . . . (motions for him to go ahead) It doesn’t bother me. (He starts to light up) When I was younger I saw this demonstration with an invisible man, where they hung this sack off his windpipe and said it was an exact duplicate of the human lung tissue. Then they put this lit cigarette in its plastic mouth and we watched the smoke slowly trickle down into the lung sack. And all of a sudden it started popping and bubbling – disintegrating right in front of our very eyes ‘til it was nothing but a brown dripping glob hanging off that clear plastic windpipe. They said that’s what happens to a tiny layer of your lung every time you take a puff. So I don’t care to smoke myself, but if you want to, go right ahead. (He looks at the cigarette in his hand, changing his mind).

JOHN: I was thinking of giving it up. Now would be as good a time as any. Right? . . . Do something you’re frightened of . . . sure? Why not?

DORIE: Once you do, it’s best not to take it back. Remember my poor dead cousin . . .

JOHN: I don’t need a cigarette

DORIE: Good. (He pats his chest pocket where his cigarettes are, then starts twitching his shoulder, drumming his fingers on his leg impatiently . . . leans over, looks down.)

JOHN: It must be mechanical

DORIE: (newly panicked) Mechanical?! We could be up here for days. (he gives her a skeptical look) It is possible.

JOHN: Anything is possible . . .

DORIE: Oh, God.

JOHN: Why don’t you open your eyes?

DORIE: I’m frightened of heights! . . . So much for my luck. I should have checked my horoscope.

JOHN: We’re going to be . . . all right (referring to having quit smoking) I’m going to be . . . OK? (He looks away from his pocket and pats his chest) This isn’t so bad.

(Uneasily, he takes a deep breath) So, how long has it been? (He feels in his pants pockets) You wouldn’t happen to have any gum, would you? Juicy Fruit? . . . Doublemint?

DORIE: Gum? No . . . My grandmother never allowed it.

JOHN: Neither would mine.

DORIE: She thought it was tacky. Bad for your teeth.

JOHN: . . . a waste of money.

DORIE: . . . socially incorrect. So, I doubt I have any gum. But you’re welcome to look.

JOHN: No. I can wait. (pause) So . . . Seriously. How long has it been?

DORIE: Five minutes.

JOHN: Just five minutes (He unconsciously starts moving his leg and tapping his foot)

DORIE: (without looking down) What are you doing?! You’re moving.

JOHN: I’m not moving.

DORIE: You’re twitching.

JOHN: Twitching?

DORIE: (Pointing down / looking up) Your leg. It’s going like a house on fire. Are you nervous? . . . Or is this some sort of warning signal before you break into a full uncontrollable fit?

JOHN: I am not breaking into a fit! I’m not twitching! Look. (She doesn’t look) Don’t look. See . . . (He holds his hand out in front of him) . . . Steady as a rock. (His hands start to shake, he grabs for the bar) Oh, God.

DORIE: What if they make us climb out on a ladder?! (panic) I can’t climb out on a ladder. I’m going to be sick.

JOHN: Just take a deep breath. It’s mind over matter. Just breathe. Breathe. (The both breathe together, she a deep breath and he like he’s smoking an imaginary cigarette) Better?

DORIE: Better.

JOHN: It’s all will power. (he closes his eyes) Visualization. See a stream. A peaceful . . . quiet . . . winding stream . . . . (Smiling) . . . draw it into your mouth . . . taste it . . . feel it going down . . . hitting you here. (He hits his chest and coughs violently – He opens his eyes, sits upright) You wouldn’t happen to have a Tic Tac . . . Lifesaver . . . cracker . . . ?

DORIE: I wish you’d quit mentioning food. That’s like talking about going to the bathroom in a moving car riding down the highway.

JOHN: I hadn’t though about the bathroom. (He crosses his legs)

DORIE: Just promise me one thing. Promise me you won’t eat me.

JOHN: Eat you?

DORIE: It happens. I’ve read about it. “Snowbound in the Andes.” “Shipwrecked on a Desert Island.” Two people stranded together and one eats the other. Instead of falling in love, you have to worry about being dinner.

JOHN: I am not that hungry. DORIE; Of course, I could stand to lose a pound or two . . . but I never los it where it counts – it drops out of my face and I look like a cadaver with hops.

JOHN: I feel fat. Do I look fat? I am putting on weight and I’m just sitting here!

DORIE: Nonsense. You’re thin.

BOTH: I used to be thin.

DORIE: (During the following John starts picking lint off his jacket and biting his finger nails) In high school, I was so thin when I wore panty hose I pinned them to my bra. That kept my panty hose up and my bra down.

JOHN: But you filled out nicely.

DORIE: (embarrassed) Thank you.

JOHN: (distracted) A regular beauty pageant contestant.

DORIE: I was once. But I didn’t win.

JOHN: The prettiest girl doesn’t always win. (He bites at a nail)

DORIE: Of course not. If looks were all that counted, anybody could win.

JOHN: I bet you won Miss Congeniality. Anybody as . . . ah . . . as . . chatty . . .as you would have won Miss Congeniality. (He spits out a nail)

DORIE: That’s just my breeding. My mother always said it was our social obligation to be entertaining.

JOHN: Don’t have to feel any obligation on my account

DORIE: No! You’re easy to talk to. I could talk to you all day.

JOHN: (reacting, he bites his finger) Ouch!

DORIE: You are going to bite those nails clear down to the nub if you’re not careful.

JOHN: It’s just a . . . hangnail.

DORIE: I had this roommate in school once who got gangrene from an infected hangnail. Nearly had to have her finger cut off. . .

JOHN: (takes his hand out of his mouth, starts feeling for his cigarettes) (recalling) You said, that cousin of yours – who broke this pact . . . Died, didn’t she?

DORIE: Deader than a door nail. They say that poor little body was charred beyond . . .

JOHN: STOP! I’ll pay you a hundred dollars if you don’t say another work.

DORIE: I could never take money from a stranger. My mother always told me . . .

JOHN: (Interrupting/loosening his tie) Is it hot up here? Do you feel hot? I feel hot . . .

DORIE: No.

JOHN: How can you feel anything? You haven’t stopped talking since we sat down. I’m sorry. It’s my fault. (pause) Five minutes?! It’s only been five minutes! They say when you die your life flashes in front of you in five minutes. I never believed that was possible before now.

DORIE: I’m sorry. I’m boring you.

JOHN: You’re not boring me. It’s just . . . (He pats chest) I’ve been smoking ever since I was twelve. They’d give me a dollar for the collection plate at church and I’d fish out change – enough for a pack. God got the bulk of it, but He’s getting even now.

DORIE: No, you are right. I do talk too much. I always have. Especially when I’m nervous . . . or scared. Sometimes I get so wound up I can feel myself floating up over my body and I just want to slap myself silly saying . . . “Shut up. Shut up. Shut up.” (pause) Like now. I’m sorry.

JOHN: It’s OK.

DORIE: No, you see my greatest flaw is . . I just want people to like me. I’m about the only person I know who thought Sally Field’s acceptance speech at the Academy Awards . . “You Like me! You like me!” . . . had real depth. I understood what she meant. But sometimes what we do has the exact opposite results.

JOHN: I like you.

DORIE: How can you tell, you keep twitching and biting and picking . . .

JOHN: . . . and listening Sometimes when I listen to you I forget about smoking. I do . . like you . . and . ah . . I don’t even know your name.

DORIE: My name is . . . Dorien. But people call me Dorie.

JOHN: Pleased to meet you . . . Dorie. I’m John. (He holds out his hand to shake hers and as she does, she briefly looks down and regrabs the bar.)

DORIE: I’m sorry about the smoking. But I bet your wife will be happy.

JOHN: I’m not married. You?

DORIE: (embarrassed) Me?! No!

JOHN: Divorced. Traveling salesman . . . only she couldn’t take the traveling so she moved on. You get used to being alone. You get over it. You adjust.

DORIE: Isn’t that the truth. Why, I don’t even mind eating by myself anymore. Not as long as I have something to reed. Newspaper, magazine, those little bitty sugar packets they set at the table, the ones with the history of each state written real tiny on the back. You can learn a lot eating alone. The state flowers. The state birds . . . (John suddenly leans over and kisses her on the cheek) What did you do that for?

JOHN: I don’t know . . . I thought if I kissed you, you’d stop talking for a minute. (She looks at him. He leans over an kisses her on the lips)

DORIE: (nervous/flustered/she starts talking again) Did I tell you I have an aunt who lives in Dublin, Georgia; semi-related to Kim Basinger? You remember the movie The Nautral . . . Well, she was in it . . . Kim . . not my aunt . . . and when they started

(John leans over and kisses her again on the lips) (Suddenly they both jerk back in their seats)

DORIE: What was that?!

JOHN: Looks like we’re moving. Won’t be long now. (looking) They’re letting us out one by one. (They jerk again in their seats) This is us. (They both raise their arms up and let go of the “bar) (Dorrie jumps out, extends her hand in a formal good bye)

DORIE: It . . . it . . has been a pleasure. (John takes her hand) Well. . . you better get going . . . and have that cigarette. I wouldn’t want you to get in any trouble kissing every girl in the park just so you can make it through the day without smoking . . . I better get going. (She lets go of his hand and starts to walk away)

JOHN: (hollering out to her) Dorie, you coming back next year?

DORIE: It is a tradition. And you know, my family, we’re keen on tradition.
```

---

## IC-0774: Finding Wonderland

- Title: Finding Wonderland
- Author (byline): Jane Nicolaas
- Work: Finding Wonderland
- Publisher: SpeechGeek
- Publication date as stated: 2010
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2132
- Already set (do not supply): none

### Source block (context only)

```text
Finding Wonderland by Jane Nicholaas
ISBN: 978-1-61387-030-3
Copyright 2010 by SpeechGeek.
Free performance of this play for high school and college level
competitive forensics is permitted. All other rights reserved.
This PDF version of this selection, e-published in 2011, is identical to the
printed published version of this same publication dated 2011. This
statement along with the entire printed PDF of this publication must be
presented at any National Forensic League District or National event for the
script to comply with NFL rules per the request of the Executive Director.
This and other selections of quality performance literature for competitive
oral interpretation are published by SpeechGeek.
For more information and performance rights, contact SpeechGeek.
SpeechGeek
806 Brownstone Way
Bowling Green, KY 42104
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
(A knock at the door.)

LIDDELL. Mr. Dodgson, welcome to our home. CARROLL. Thank you, Liddell. Your husband thought it

opportune to invite me to sit with your young

daughter.
LIDDELL. Quite. I am told it will do wonders for my sanity.
CARROLL. (nods)
LIDDELL. Rather meek, I see.
CARROLL. Rather.
LIDDELL. Well, I am sure you will do well to keep our

daughter occupied and teach her the ways of

gentility. CARROLL. I am excellent at occupation, madam, except

when it comes to keeping one myself. LIDDELL. (not amused) Mr. Dodgson, let me be clear. I

offered you employment in my home because

my husband took pity on you, an unmarried man

with an unusual sympathy for children and no

discernable purpose in life. CARROLL. Much obliged, madam. It seems you are the last

soul in town who is willing to be so gracious. LIDDELL. Indeed. Please make yourself comfortable; my

daughter should be in any moment. Excuse me.

(exits while calling out) Alice? Alice?

(Alice enters.)

CARROLL. Ah… good day, madam.
ALICE. Good day, sir. And you are?
CARROLL. My name is Mr. Dodgson.
ALICE. Oh, no. That won’t do at all. That name sounds

like Mr. Dodo. You shall be…Mr. Carroll. Like a

song.
CARROLL. Very well. Ms. Liddell and Mr. Carroll.
ALICE. No!
CARROLL. No?
ALICE. No. We are not to be entertained as stuffy old

proper people. In here, I shall be Alice and you

shall be Lewis. CARROLL. Very well. In your wonderland, Alice, I am Lewis

Carroll. ALICE. Very pleased to meet you, sir.

INTRO

(He enters, she is pouting on the couch)

CARROLL. Ta-da! A painted rose, just for you! (She scoffs at

the gift.) Oh dear, someone seems to be in a foul

disposition.
ALICE. You are late!
CARROLL. I am? (checks his watch)
ALICE. You most certainly are. Does your pocket watch

have jam in it? CARROLL. I don’t believe so. ALICE. You are a quarter of an hour late. I’ve been

waiting here forever. CARROLL. Well, if I am late, it is entirely because of the

adventure I had on the way over.
ALICE. (pouting, but interested) …Adventure?
CARROLL. Oh, it was magnificent.
ALICE. …In what way?
CARROLL. In the magnificent way. So there I was on a

golden afternoon, reading by the river. ALICE. Stop. Stop. Stop. This story is all wrong. Try

again. CARROLL. You’re rather insistent today, are you not? ALICE. ‘Tis not of your concern why a lady demands.

You shall do as I say or you shall be punished. CARROLL. Well, that didn’t sound like my little Alice.

Sounded quite a lot like your mother. ALICE. (pause) It was a golden afternoon, but I was

sitting by the river. CARROLL. Indeed you were. ALICE. And I was being made to listen and be ladylike

and bored.
CARROLL. How dreadful.
ALICE. And then… well, go on.
CARROLL. (He gestures for Alice to sit down on the sofa and

carefully walks behind it.) While you were sitting,

something caught your eye. ALICE. What was it? CARROLL. (disappears behind the sofa) You took a closer

look when--from behind a tree--out popped a

rabbit. (pops out from behind the sofa as a rabbit) ALICE. Just a rabbit? CARROLL. (looks at himself and improvises) A rabbit in a

waistcoat. (pulls out his pocket watch) …with a

pocket watch.

ALICE. How curious! And then he said… RABBIT. Oh dear, I’m ever so late. ALICE. And I thought, what on earth could a rabbit be

late for? I must follow him and find out.

(chases him around the room)

RABBIT. Oh dear! Oh dear! I shall be late!
CARROLL. And then the rabbit jumped down a rabbit hole.
ALICE. But I followed him, didn’t I?
CARROLL. You did, but it wasn’t a normal rabbit hole; it was

the deepest in the whole world, so you jumped

in and you fell. And you fell and you fell!

(She twirls her as if she’s tumbling down the rabbit hole)

ALICE. I shall fall right through the center of the earth! CARROLL. And come out where people walk upside down.

(Both laugh hysterically. She spins away just as mother enters.)

LIDDELL. What is the meaning of this?

(Both stop immediately.)

LIDDELL. I could hear you both clear out in the garden!

Alice, you know better than to conduct yourself

this way. And you, Mr. Dodgson—
CARROLL. Uh…
ALICE. Mr. Carroll, actually.
CARROLL. Alice…
LIDDELL. I beg your pardon?
ALICE. It’s true, Mama! Every time he enters the house,

the most miraculous thing happens: he is

transformed from the meek and mild Mr.

Dodgson into the fantastic Mr. Lewis Carroll. LIDDELL. Alice you shame yourself with such an outburst.

Apologize this instant. CARROLL. There is no call for apology. It is just a game,

madam. I can assure you, just nonsense. ALICE. Just? LIDDELL. Alice, I think your visit is at an end for today. Say

goodbye to mister. … whatever your name has

become. ALICE. But he only just arrived!

LIDDELL. You shall do as I say, or you shall be punished. ALICE. Good day, sir. CARROLL. Good day. (kneels and says quietly so only she

may hear) Don’t worry. You’re down the rabbit

hole now, remember? There are many

adventures to come.

(Alice smiles widely and skips from the room. Leaving Carroll to

the mercy of Liddell.) LIDDELL. As for you, sir. You would do well to remember

that I am your employer and keeping me

satisfied is the only means to continue your

appointment in this household. Good day. CARROLL. Good day, madam.

(He dejectedly leaves.)

TRANSITION

CARROLL. Ms. Alice? You’re six feet taller than last I saw

you. What have you been eating? ALICE. (Alice stands uncomfortably still with her hands

behind her back. She is happy to see him, but is

fearful and quiet.) CARROLL. Speechless? A first. Still tumbling down the

rabbit hole? ALICE. I’m afraid not, sir. ‘Tis not very ladylike to

entertain such fancy.

(He catches sight of her hands. They are swollen and badly bruised beneath bandages. The look shared between them conveys the story; she has been punished with a cane.)

CARROLL. My dear child. (gently takes a hand) What have

they done to you? (she says nothing) They’ve

gone mad. ALICE. It seems the whole world has. CARROLL. Well, you can’t go running round mad people all

the time. Remember the last time that

happened? (she doesn’t) Of course you do. It was

down the rabbit hole: the Mad Hatter and the

March Hare? ALICE. (smiles a little) Oh yes, how could I forget such

an adventure. Remind me again of what came to

be? CARROLL. You needed directions.

ALICE. When I came across a tea party! Excuse me, sirs.

Have you seen the White Rabbit?
HATTER. Yes, of course! Would you like some wine?
HARE. We don’t have any.
HATTER. Precisely why I asked if she’d like some.

(Hatter and Hare laugh obnoxiously.) ALICE. I don’t think— HATTER. Then you shouldn’t talk then.

(Hatter and Hare laugh obnoxiously.) ALICE. I think you’re dreadfully savage and mad. And I

imagine, if the Queen were here, — HATTER. The Queen? ALICE. Yes, the Queen of Hearts. If she were here, she’d

say off with your hands! HATTER. No, she’d say off with your heads!

(Alice and Carroll laugh. They hear something and instantly go silent with fear. A moment passes and it seems they are safe.)

ALICE. Nevermind, Mother is playing bridge with her

friends across town. CARROLL. The Queen of Hearts, eh? ALICE. She thinks me too old for rhymes and stories.

You’re not too old for fantasy; why should I be? CARROLL. Well, my dear. Most believe I am too old for

nonsense. That is why they look at me the way

they do. You should hear some of the things they

have said about me. Horrible, dreadful things. ALICE. None of them are true. CARROLL. Isn’t that silly? They take no time to enjoy

fantastic nonsense, and yet they seem to revel in

malicious nonsense fully.

(He looks at her, she has no idea what he is talking about)

CARROLL. Alice, I want you to know something. Something

very secret. Is the secret safe with you? ALICE. Of course. CARROLL. The world is a dark place for dreamers.

Sometimes it makes the shadows seem like

they’re all around you. But someone very wise

once told me that dark is the best place for

dreams because that is where they are most

needed. Do you understand? ALICE. I can’t say I do, sir.

CARROLL. You will. I’m sorry to say you will. ALICE. Why do you tremble so much? You act so meek

and scared all the time. CARROLL. I’m afraid it is my nature. ALICE. No sir, your nature is the same as mine. I have

seen it. CARROLL. Perhaps it is what I was taught by the natures of

those around me. ALICE. (laughs at the silliness) To be taught by nature.

As if…as if some little caterpillar were meant to

teach you how to be you. CARROLL. Yes, and I’m sure even they would look down

their petals at me. ALICE. You have no need to be scared when you have

such a wonderful fantasy world to live in. CARROLL. My dear, the fantasy world is yours. I am simply

running through it as a scared little rabbit.
ALICE. Well, then we must take the stand.
CARROLL. Do you mean take a stand?
ALICE. A trial! Begin, little rabbit.
CARROLL. Very well!
RABBIT. Hear ye! Hear ye! All rise to receive Her

Majesty, the Queen of Hearts. QUEEN. Call the first witness, The Mad Hatter! HATTER. I beg pardon, your Majesty, but I hadn’t quite

finished my tea. We only just started on…the…

uh…fourteenth of March. HARE. …Fifteenth… HATTER. Four fifths of a tenth of march

(Hatter and Hare laugh obnoxiously.)
QUEEN. You’re full of nonsense. Off with your head!
RABBIT. But… but… but… your Majesty!
QUEEN. ‘Tis not of your concern why a lady demands.

You shall do as I say or you shall be punished.

Off with your head! RABBIT. You heard what the Queen said! Off with our

heads! CARROLL. Do you suppose we’ll still be mad with no

heads? ALICE. I do hope so. CARROLL. So do I.

TRANSITION

(Carroll enters excitedly to find Mrs. Liddell waiting for him.)

LIDDELL. Ah, Mr. Dodgson. Thank you for joining me

today. CARROLL. Of course. Is she about? I’ve brought her a

present.
LIDDELL. I’m afraid you will not see my daughter today.
CARROLL. I see.
LIDDELL. …Or ever again. I have discussed the matter

with my husband, and we feel that the function

you serve in our household is no longer

necessary. CARROLL. And does Alice feel that way? LIDDELL. Miss Liddell, sir, is a child and an incorrigible

one at that. CARROLL. I disagree to the negativity you paint both of

those words in. LIDDELL. Regardless, her antics have not improved since

your arrival. In many ways, it seems to have

given them new vigor. She has given us no other

choice. She is to be sent to boarding school. CARROLL. Boarding school? LIDDELL. Where she shall remain until she is of age to

attend university.
CARROLL. But…but she could be tutored here.
LIDDELL. Don’t be ridiculous.
CARROLL. I, myself, am an excellent mathematician.
LIDDELL. Just as you are an excellent elocutionist? (brings

out a piece of paper) “Twas brillig, and the slithy

toves did gyre and gimble in the wabe.”

Complete twaddle. You are--I’m afraid--as

incorrigible as she is.
CARROLL. I consider there to be no finer compliment.
LIDDELL. Watch your tone, sir.
CARROLL. Very well. I am no longer employed here. May I

come to call as a visitor to Ms. Liddell? LIDDELL. Most certainly not! What on earth would people

say? CARROLL. Why does that matter so much to you? LIDDELL. You’re mad. It seems to me, sir, that you should

leave now. CARROLL. It seems to me, madam, that you are unworthy of

a daughter such as Alice. LIDDELL. Sir! CARROLL. Yes, and while we are being clear and truthful, I

would like you to know that I am an unmarried

man who enjoys the company of children

because it means that I am required to spend

less time with the likes of you and your incipit

adultness. LIDDELL. You are too bold, sir. CARROLL. Your daughter is full of fire and life and wonder.

And while I deeply regret that she will be sent

away, I take solace in the fact that she will no

longer be subjected to your ludicrous

expectations and harsh disciplines.
LIDDELL. You are out of order!
CARROLL. Well then off with my head, you royal witch!
LIDDELL. Mr. Dodgson!
CARROLL. Madam, that is the name of a meek and pathetic

man--two things I am no longer. LIDDELL. You are full of nonsense! CARROLL. And I thank God and Alice every day for it! Good

day and good riddance, madam.

(Turns and finds Alice standing there in silence.)

CARROLL. Alice. ALICE. I heard what you’ve said. CARROLL. Yes, well. At some time we all have to grow up

and take “the” stand, I suppose.
ALICE. I suppose.
CARROLL. Where are you to go for boarding school?
ALICE. I don’t know; they haven’t told me where, only

that I am going. CARROLL. Well, I’m sure it will be wonderful with you

there. ALICE. Thank you for everything, Mr. Dodgson. CARROLL. Mr. Dodgson? Who is that stodgy old proper

person? ALICE. He is…the most brilliant person I have ever met.

He is my best friend. And I shall miss him

terribly. CARROLL. (kneels down before her) My dear, sweet child.

There is no need to miss me. (hands her the

present) ALICE. What is this? (opens it) Alice’s Adventures in

Wonderland. You’ve made us into a book? CARROLL. You see? Whenever you feel alone or scared or

bored by the world around you, you can go here

and live one of our magnificent adventures

again.

ALICE. I shall never see you again, shall I?
CARROLL. And yet I’ll always be with you.
ALICE. Thank you.
CARROLL. For the book?
ALICE. For believing in my nonsense.
CARROLL. Thank you for believing in mine.

(They share an embrace and he gently kisses her forehead before he departs. She stares for a moment and then opens the book to the end.)

ALICE. “Lastly, she pictured the dream of Wonderland:

remembering her own child life and the happy

summer days.”

(Alice closes the book lovingly.)
```

---

## IC-0775: Finger Food

- Title: Finger Food
- Author (byline): Nina Shengold
- Work: Telling Tales: New One Act Plays
- Publisher: Penguin Books
- Publication date as stated: 1993
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: DENNY, MONA
- Teaser before the introduction: Yes
- Spoken words (computed): 1306
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nina Shengold
Book: Telling Tales: New One Act Plays
ISBN: 0140482377
Publisher: Penguin Books
Date (Month/Year): 1993
```

### Introduction (context only: never use it for content warnings)

```text
Actress: Remember that Seinfeld episode where George became a hand model? It wasn't entirely fiction--there are such things as hand models and they can make loads of money. There are models for practically every body part, each with their own rigorous requirements. But the money's in hands. Being a hand model requires Precise, graceful movements … breaking a cookie just so … pouring ketchup on a hot dog … And let’s not even talk about Finger Food by Nina Shengold
```

### Performance text (classify this)

```text
A commercial photographer's studio, minimally indicated by a standing flood lamp focused on one end of a long table. The lit end is elegantly set with a lace tablecloth, cut crystal wineglass and bottle of wine. The rest of the table is tacky and bare. There's a canvas director's chair and an empty carton, a telephone, Denny's camera equipment. . . Lights up on Denny, staring intently at the wine-bottle set-up. He starts making adjustments, moving the glass, turning the bottle: an artist at work. Perfection. He glares at the door, annoyed. Strides to the phone and dials.

DENNY: Mitchell? Denny. My talent is late again. . . . Runs in her what? I'm not shooting her panty hose. . . . Studio Six, Mitchell . . . No, not deodorant, Beaujolais! . . . Yeah, well she just better shake it, there's Reddi-whip coming at quarter past four! (He hangs up and returns to his set-up. Turns on the flood lamp. Smiles. Holds one hand next to the wineglass and looks through his camera, rehearsing the shot.) Oh, baby. (He steps back for more distance and tries it again.) Gorgeous. (He steps back again and finds that he's too far away now to reach the glass. He tries anyway, stretching one arm toward the glass, leaning back with his camera. It looks ridiculous and it doesn't work.) Damn. (Sudden brainstorm. He rips off one shoe and sticks his bare foot on the table, gripping the glass with his toes. He picks up the camera and says to his foot:) Love ya. You're beautiful.

(Mona rushes in, breathless. She is simply but prettily dressed and wears orange rubber dishwashing gloves. She carries a model's loose-leaf book. Denny jumps up and runs to her.)

DENNY: Carla!

MONA: Darling!

DENNY: (embraces her, kisses both cheeks, then draws back) You're not Carla.

MONA: No, I'm . . .

DENNY: I asked them for Carla. The hand model.

MONA: Then... you don't know?

DENNY: I have to have Carla.

MONA: Oh heaven. I thought they had told you. The agency.

DENNY: What happened?

MONA: (crosses herself with rubber gloves) She was in . .. She had Carla-a terrible accident. An elevator door.

DENNY: No! Is she all right?

MONA: She was maimed! She broke two of her nails! The thumb and the index! Oh god. I have nightmares. (She covers her face with her gloves.)

DENNY: SO the agency sent you instead?

MONA: (Lowers her hands. He's so insensitive. Glacial) I'm her understudy.

DENNY: I'm not sure I can do it with somebody else.

MONA: Try me.

DENNY: You've done this before?

MONA: Hundreds of times.

DENNY: A hand job.

MONA: I live for it.

DENNY: I've never seen you.

MONA: My face, perhaps. No. (Touches a glove.) May I hang up my things? (Denny grabs the carton from under the table and drops it contemptuously in front of her. Mona looks at it. Looks at him. Then she pulls off one rubber glove, finger by finger, like a stripper. He watches, transfixed. Underneath she is wearing a lacy black fingerless glove and crimson nail polish. Denny moans. Mona smiles. She drops the glove into the box and takes off the second, finger by finger.)

MONA: My name-(Drops the second glove.)-is Mona.

DENNY: Urn... Uhhhh . . . huh. Ah. Denny.

MONA: Denny. (She touches his face. His eyes follow her fingers.)

DENNY: I love what you're wearing.

MONA: Thank you.

DENNY: You, ah, only do hands?

MONA: I went to the elbows once. Laundry soap. It was awful. I felt so cheap.

DENNY: (rhapsodic): Just hands.

MONA: I've brought my portfolio. Will there be makeup?

DENNY: I... I have to see. . . .

MONA: Pictures first. (She indicates with a graceful, game-show assistant gesture that Denny should sit.)

DENNY: Pictures. Yes. (He sits. Mona stands over his shoulder and guides him through the book. We do not see the pictures described.)

MONA: Most of these are production stills from my video spots. Cold cream. Grape jelly. Men's shirts.

DENNY: Collar-smoothing. Oh Christ. Very nice.

MONA: (turning the page) Dishwashing liquid. Which is the coed and which is the 62- year-old grandmother? Neither! They're me! They're both me!!!

DENNY: No!

MONA: (nods proudly) I love doing character work. I studied that grandmother. I'm very Method. (Turns another page. Breathless.) Oh. This was my favorite job ever. Chocolate creme devil's food-(She breaks off, staring.) Denny. Your toes are nude.

DENNY: (Looks. They are.) Yes, well, I . . .

MONA: Denny, they're stunning!!! (She crouches and pets his toes.) Oh, Denny. (Grabs his right hand.) God. You have wonderful digits.

DENNY: I do?

MONA: Have you ever modeled? You could, you know. You have incredible cuticles.

DENNY: Thank you.

MONA: Your palms. . . Your knuckle hair. . .

DENNY: (impassioned) Mona... (Their hands twine. They look at each other meltingly. Mona drops his hand suddenly, embarrassed. All business. Back to the model book.)

MONA: Nail polish. Not my best finger.

DENNY: (turns the next page, reacts with surprise) Who's that?

MONA: My teacher. Giancarlo. He taught me to grasp. To find the caress in it. (in a sensuous Italian accent.) "You must never just reach for a thing. You must yearn for it. Grasp, never grab." (Wistful.) Giancarlo had knuckles like Brussel sprouts. Those who can't do. . . . He ran off with a thigh model.

DENNY: You were in love with him.

MONA: He was a genius. He taught Carol Merrill on Let's Make a Deal. (She does a game-show display gesture.) Door Number One.. .

DENNY: (grabs her hand) You're unbelievable!

MONA: Where can I change?

DENNY: (stalking her) Mona, I'm a professional.

MONA: I'm a professional.

DENNY: Trust me.

MONA: I trust you.

DENNY: This is not smut. This is advertising.

MONA: Stop clutching!

DENNY: (drops her hand, pulls himself together) And if you'll excuse me, I need to set up.

MONA: I need to warm up. Excuse me. (Denny makes an elaborate show of busying himself with wine props and light meter. Mona turns her back to him, peels off her lace gloves, and stretches her fingers. Denny stares as she runs through a series of silly-looking finger exercises, the last few suggesting a cat. Petting, smoothing. Maybe a couple stray mews. Then she applauds herself) (murmurs in Giancarlo's accent) Brava. Brava, mia Mona! (stands, very composed and serene) Where's the cat?

DENNY: Cat?

MONA: Will you want petting or filling the kitty dish?

DENNY: Mona, we're doing a wine ad.

MONA: What? They told me tuna fish Friskies.

DENNY: Beaujolais.

MONA: But the agency told me . . .

DENNY: They're wrong.

MONA: (starting to panic) Oh my god. Wine? I have to rethink this. My whole preparation was tuna. Oh, Denny. Oh! This is so sudden!

DENNY: What's wrong?

MONA: Tension. Look at this tension. (She holds up her claw like hands.) .

DENNY: Here, let me rub them.

MONA: NO! Wine. Think of wine. (Drumming her fingers.) You asked them for Carla. I should have realized. Carla would never do cat food. She doesn't have to do cat food. Cheap trash like me does the cat food while Carla does Beaujolais! (She bites on her thumbnail.)

DENNY: Mona! Don't do it!!!

MONA: (realizing, in horror) Oh god! I knew it! I knew this would happen. That's why I'll never be one of the greats. I'm such a neurotic!

DENNY: You're not.

MONA: You don't know. Denny, I was a nail biter! Mom used to soak them in Lysol. I'd bite them and vomit. And that's not the worst of it! I sucked my thumb!

DENNY: Lots of kids do that.

MONA: Until I was twenty! I sleep in a straitjacket. I just can't trust myself. (About to bite her nails again, she lets out a cry of despair. Runs to the chair and sits on her hands, rocking back and forth.) Giancarlo, he warned me. He told me, "Carissima, you got the hands, but you don't got the temperament. I could make you a star, but you wacko!" Oh, Denny! (She breaks down in tears. Denny reaches to comfort her.) DON'T lay a finger! Hands OFF!

DENNY: You misunderstand, Mona. I'm a professional.

MONA: I'm a professional.

DENNY: Steel. Like a doctor. I promise you, flesh leaves me cold. Flawless skin and warm naked tapering fingers are nothing. Color and form. Raw material. Meaningless.

MONA: Meaningless??

DENNY: I didn't mean meaningless.

MONA: (incensed) Meaningless? Look at this, buster! (She thrusts out a hand.) This is the species, right here. Evolution! Opposable thumb! Scratch that and it's monkeyville!

DENNY: I didn't

MONA: Where would we be without hands? No applause, Denny! No backrubs! No volleyball! Think of great art. The Creation. E.T.! (She demonstrates Michelangelo's pose.)

DENNY: Mona, please. . .

MONA: You think this just happened? I worked for this, buddy! I started out slapping men's faces on soap opera! Packets I ripped! I ripped packets! I modeled for aerosol roach sprays you see on the subway! In Spanish! And after all that I went home and did dishes!

DENNY: Hey, I've been there, too, lady. I didn't start out shooting Beaujolais, nosirreebob. They used to give me the ugly foods. Liverwurst. Cheez Whiz. Gefiite fish. I've had to shoot foods that make pigs anorexic!

MONA: You only shoot food?

DENNY: We've got our specialties too, you know. Some guys shoot black and white blue jeans. Some guys do nothing but lingerie. Hey, I'm not knocking it. Half-naked girls wearing satin and lace turns them on, that's their business. (Looks at her.) Me, I do food. I do food like I'll have you in tears from how good it looks. Bulging ripe melons with dew on their skins like a tropical rainforest. Corn on the cob dripping butter. Napoleons oozing cream. Hot. . . apple. . . PIE. A la mode and the ice cream's just trickling down off the crust through those thick, juicy. . .

MONA: Chocolate creme devil's food. . . ?

DENNY: Pudding. Cannolis. MONA (rhapsodic) Just food.

DENNY: If it goes in your mouth, I'm your man.

MONA: You inspire me.

DENNY: Your hands and my lens, kiddo. We could make beautiful ad graphics.

MONA: Get your camera.

DENNY: I'm wearing it.

MONA: Shoot. (With a dancerly flourish, she cups her hand under the bowl of the wineglass.) .

DENNY: (comes in very close and circles seductively, firing off shot after shot) Beautiful. Baby. Great palm. Stroke the bowl. Can you give me more knuckle? Perfecto. That's super. A little more flex in the wrist. Honey. Angel. Oh yes.

MONA: (breathing heavily) Yes! You're wonderful!

DENNY: Fingers! More fingers! Oh, angel! Oh., damn (He stops very suddenly.)

MONA: Keep shooting! Don't stop, Denny! Shoot me!

DENNY: I'm all out of film.

MONA: Hold my hand! Hold me! (He clasps her hand ardently.) God yes. You're ruthless. The sweat of your palms. Take me!

DENNY: (on fire) Mona! (He yanks off his camera and moves in to kiss her. She thrusts her hands in front of his face, palms forward. Denny kisses them feverishly, licks her fingers.)

MONA: (suddenly pulls one of his hands away) Your ring! Take your ring off!

DENNY: I can't.

MONA: Take it off, Denny! Do it!

DENNY: It's stuck! (Mona slaps him. Shocked silence. She clutches her hand.)

MONA: Oh god. Oh my god. (Picks up the wineglass and gulps.)

DENNY: You can't drink that! It's product!

MONA: Tough.

DENNY: Good point. (Drinks from the bottle. Pause.)

MONA: I feel so cheap. Put your shoe on.

DENNY: (Sits in the chair, puts his shoe back on. Looks at her.) I'm sorry, Mona. I thought you had seen.

MONA: It's a wedding ring?

DENNY: Yes.

MONA: Married. My god. Every man on this planet is married! Well, tell me this: who are you married to??? Women I meet aren't married! You marry each other? (She drinks. Calmer.) Sorry. I live in New York.

DENNY: It's all right.

MONA: Is she a model? Your wife?

DENNY: A photographer.

MONA: What does she shoot?

DENNY: (Beat. Shamefaced.) Laundry soap. (Mona recoils. Impassioned.) She's nothing like you! She's got dishpan hands!

MONA: (gathers up her portfolio, gloves) Goodbye, Denny.

DENNY: Don't go.

MONA: I have to.

DENNY: Please!

MONA: (turns back) The Italians wave. . . so. (She does the traditional "ciao. ") As if they were holding a bird. Giancarlo. He taught me. (She blows Denny a kiss on her fingertips, then goes. Denny stands for a moment. He does a small, wistful "ciao.")

DENNY: (He turns off the flood lamp and sits, heartbroken. Then he picks up the phone and dials.) Mitchell? Yeah, Denny. Look, Mitch, I'm not feeling so hot. You think you could cancel the whipped cream? (The door opens. It's Mona.)

MONA: (eyes shining, breathless) Did you just say. . . whipped cream??
```

---

## IC-0776: Finger Painting in a Murphy Bed

- Title: Finger Painting in a Murphy Bed
- Author (byline): David L. Peterson
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: 1995
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: REGGIE, MYRA, LUDLOW, UDLOW
- Teaser before the introduction: Yes
- Spoken words (computed): 1518
- Already set (do not supply): none

### Source block (context only)

```text
Author: David L. Peterson
ISBN: 978-0573695421
Publisher: Samuel French, Inc.
Date (Month/Year): 1995
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Well, that’s the background . . . . at least as much as we can tell you about the chain of events that led to the current relationship between

ACTRESS: Myra and her younger brother, Ludlow

ACTOR: There’s no doubt that Ludlow is special . . . call it Asperger’s

ACTRESS: Call it a mental disability

ACTOR: Heck . . . I’d call him an Idiot Savant (whispers) but that’s not politically correct . .

ACTRESS: Oh, enough of trying to explain what Ludlow is like. We’ll let you see for yourself

ACTOR: FLASHBACK to earlier that day, in a scene from

TOGETHER: Finger Painting in a Murphy Bed by David L. Peterson
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

REGGIE: (picking up a note from the counter and beginning to read it) What's this?

MYRA: It's nothing. (She takes the note from REG, folds it and puts it away.) A note from Ludlow.

REGGIE: It's a strange note . . . how many has he written?

MYRA: Counting today's? One thousand eight hundred and twenty-four.

REGGIE: It's iambic pentameter. Like Shakespeare . . .

MYRA: Yeah, he's into him now. Last month it was some scrag called Dickenson. I liked them better in the early years when he'd quote Barney Rubble. Now that I could understand.

REGGIE: Why does he quote famous writers?

MYRA: When Ma died she had some classical books she'd collected over the years. Lud really wanted the books.

REGGIE: When did your mother pass away?

MYRA: 'Bout five years ago ...

REGGIE: One thousand, eight hundred -

MYRA: And twenty-four notes ago . . .

REGGIE: I'm sorry. Was she old when she died?

MYRA: Not particularly . . . slit her wrists . . . such a waste . . . Lud found her . . .

REGGIE: Is that why Lud is the way he is?

MYRA: Lud's the way he is 'cause it's the way he's always been. People always want simple, tidy little answers to the most complicated matters . . . but people . . . they're a little more complicated. I don't think you or me or anybody else on this God-given planet knows exactly what's turning around up there. Some things defy explanation . . .

(Lights up on a small cramped living room. Myra enters with groceries and heads for the kitchenette. Ludlow is out of site, under the Murphy Bed. Myra can’t see him, but the audience can)

MYRA: Hey Ludlow! I'm home. Can you come in here for a sec? (She closes the kitchen window, walks to the front door and shuts it. She returns to the groceries.) C'mon already . . . I need to talk to you . . . about tonight (She spies a note taped to the television. She walks over, picks up the note.) And what do we have here? "Friends, Romans, and any other cold and unloving family relations who may find amusement at my demise. I am going to a better place. A land of chicken waste. Where I am loved as a human and not as an individual. Heretofore I may be a bit melancholy, but be that as it may, I put on clean underwear today. Do not cry. Ludlow." (She looks around placing the note on the table.) Ludlow!!! I gotcha Twinkies!!!

LUDLOW: (From underneath cot.) You're late.

MYRA: I know, I'm sorry. The G was out of wack.

LUDLOW: Subways suck.

MYRA: Thank you Mr. Giuliani - why don't you do something about it? And don't use that word, you know I don't like that word . . . Come on out of there. (She resumes putting away groceries.) I thought you might be under the sink.

LUDLOW: I don't fit under the sink no more. Can I have my Twinkies now?

MYRA: Come out from under the cot first. We gotta talk.

LUDLOW: (long pause) I . . . can't.

MYRA: Any why is that?

LUDLOW: My zipper is stuck in the spring.

MYRA: Well, what do you suggest I do?

LUDLOW: Leave me here to die ...

MYRA: Not in my living room, champ!

LUDLOW: [Just] lift the bed up and help me to disengage.

MYRA: (She lifts the bed up with Ludlow still pinned to it like a cat on a wall.) Hang on, hang on. Don't squirm - Almost got it . . . there! (LUDLOW makes a dash for the groceries.) Hang on there buddy . . . just what in the name of Theodore D. Roosevelt were you doing all crucified on the cot springs like that?

LUDLOW: I was looking at the pee stains . . . some of them look like dogs and some like clouds and some like boats on the high seas. Well, there was this one that looked just like Aphrodite - she was a famous Roman prostitute - an she looked like she was crying, but I couldn't make it out, so I went closer and I reached out to touch her tear an -

MYRA: Yeah?

LUDLOW: Her eyeball moved.

MYRA: Get outta here:

LUDLOW: Well, it was a cockroach. No ordinary cockroach, this one had a wallet!!!

MYRA: Did you kill it?

LUDLOW: Sort of . . . you got my Twinkies?

MYRA: What do you mean "sort of'?

LUDLOW: Well, I opened the kitchen window to let him out, and I picked up a newspaper to get him on . . . . And I snuck up to the cot, silently stalking this king of the slum beasts . . . carefully trying to edge the paper real close under him . . .

MYRA: And . . .

LUDLOW: He went right for my throat!!!

MYRA: Oh, Ludlow.

LUDLOW: He did! Honest - straight for the jugular vein. During the brief but fierce skirmish, I managed to somehow get tangled in this jagged web of springs you call a cot.

MYRA: And the roach?

LUDLOW: He shall live to see yet another day and another battle.

MYRA: Alright. That's worth a pack of Twinkies . . . here. (She tosses him the Twinkies.)

LUDLOW: Thanks.

MYRA: Now listen, I got something to tell you, about tonight. (She begins to put away the rest of groceries}

LUDLOW: Get my note? ... Perchance? Did you like it?

MYRA: What does uh - "melancholy" mean?

LUDLOW: Oh, that I got from That Gentleman from Verona. It's a play - by Shakespeare. He's very old.

MYRA: I see. What's it mean?

LUDLOW: I'm not sure ... I think it means you got the squirts.

MYRA: Lud!! Don't you say ~

LUDLOW: (Cringing.) Don't hit me - please don't hit me, Myra . . . please.

MYRA: Have I ever hit you? C'mon Lud, have I ever?

LUDLOW: No.

MYRA: Then don't say something like that . . . it hurts my feelings.

LUDLOW: Didn't mean to.

MYRA: Eat your Twinkie. I'm glad you put on some clean underwear.

LUDLOW: Oh, you got that part.

MYRA: So what did you do today?

LUDLOW: Got stuck to a cot.

MYRA: Before that.

LUDLOW: That consumed the majority of my time.

MYRA: Alright . . . I get any messages or anything today?

LUDLOW: Mrs. Ferster came by with some laundry for you to do. Big fat cow.

MYRA: I need the work Lud, she needs to drop it off.

LUDLOW: She's the Anti-Christ.

MYRA: I thought Alex Trebec was the Anti-Christ.

LUDLOW: That was last week.

MYRA: So where is it? . . . Lud? Lud, did you not let her in?

LUDLOW: Well . . . I wasn't sure if it was her or not!!

MYRA: Lud, that's what the peephole's for. Did you look through it?

LUDLOW: Yeah, but she had the laundry packed up past her face. All I could see was her knuckles.

MYRA: Did they look like Mrs. Fester's knuckles?

LUDLOW: Yeah, but-

MYRA: Lud, c'mon!! I need the extra money. You can't keep doin' this to me . . .

(Softer.) Okay?

LUDLOW: I'm sorry . . . it was a very big cockroach.

MYRA: I'm sure . . . any other messages?

LUDLOW: Somebody dropped a note off for you.

MYRA: Where is it? (Ludlow digs it out of his back pocket and holds it up for Myra; she opens note and smiles.) Myra, you lucky dog . . . he's a charmer all right.

LUDLOW: Who's Reggie?

MYRA: Why did you read my note?

LUDLOW: I didn't.

MYRA: Then how did you know it was from Reginald?

LUDLOW: Doesn't . . . it say "Reggie" on the note?

MYRA: Lud!! Did you read my note?

LUDLOW: No!! I didn't!! . . . sort of . . . (Heading for the adjacent room.) I'm gonna take a nap.

MYRA: Just hold it there Mister. Come back here . . . now . . . . (Ludlow returns, contrite)

MYRA: Do you know what you did wrong?

LUDLOW: Yes.

MYRA: Alright . . . want to paint me a picture? How 'bout it?

LUDLOW: Okay. (He goes to drawer, takes out his supplies.)

MYRA: (Going back to her groceries.) I want no more "sunburst yellow" on the floor. It looks like we got a sick pet when it stains the carpet. (long beat while each work) . . . What'cha paintin' me?

LUDLOW: Puck.

MYRA: You painting me a hockey puck?

LUDLOW: Puck, Puck, Puck. Servant to Oberon - King of the fairies!!!

MYRA: Oh. That's okay then . . .

LUDLOW: What's he look like?

MYRA: The king of the fairies?

LUDLOW: [Reggie]

MYRA: Ah - he ain't much. Just a fella.

LUDLOW: He sent you a note. . . What does "anxiously awaiting your succulent dishes" mean?

MYRA: You weren't supposed to read that, dammit! . . . Look, I'm sorry, Lud. You shouldn't read other people's stuff, that's all . . .

LUDLOW: You said that already!!! (He throws his paints and paper.)

MYRA: Lud. Pick that up. Now. (He doesn't move.) Now, Lud.

LUDLOW: Do you like him?

MYRA: Now, Lud. First the paints, then the answer . . . thank you . . . yes, he likes me . . . don't get that way. . . He wants to take me out. AAAh - hang on there - that's what the note, which you obviously scrutinized, is about . . . I make him a snack and he takes me to a flick . . . you following me so far?

LUDLOW: Loud and clear

MYRA: Don't give me that face.

LUDLOW: I'm not giving you my face. See? It's still here.

MYRA: . . . Lud, it's been such a long time since I've had a guy even look at me.

LUDLOW: I look at you.

MYRA: It's not the same thing

LUDLOW: They're all stupid.

MYRA: Well, we know that- but they don't.

LUDLOW: Reggie is a retarded name.

MYRA: Don't use that word! Let's give Reggie the retard the benefit of the doubt, okay? . . . Okay?

LUDLOW: Okay.

MYRA: How's Puck coming along?

LUDLOW: Okay . . . here. (Gives it to her.) You hate it.

MYRA: Naw, I always love them. It's great. It goes right on the 'fridge. (She crosses to the fridge and pauses in front of it.) Where did all the magnets go?

LUDLOW: I don't know.

MYRA: Lud-

LUDLOW: I was trying an experiment.

MYRA: What kind of experiment? Lud, this isn't like the time you swallowed all them magnets and tried to stick that fork to your belly -

LUDLOW: NO! I've matured.

MYRA: Oh boy. What kind of experiment?

LUDLOW: To see if magnets stick to aluminum . . . num.

MYRA: What aluminum-num?

LUDLOW: (Fidgeting.) On the, on the window. (MYRA crosses to the window and opens it. She leans out and looks, then ducks back in glaring at LUD. He continues sheepishly.) I guess not.

MYRA: This is not funny - we're talking serious stuff here. I don't want any part of your body outside this window at anytime. Ever. You hear me?

LUDLOW: Loud - (MYRA points a threatening finger at him.) Yes.

MYRA: The last thing I need is to cancel my first date since Lincoln 'cause I'm too busy peeling my brother off the pavement with a spatula.

LUDLOW: Your point is made, Madam.

MYRA: It better be. (She shuts the window and returns to the groceries.)

LUDLOW: You wearing that for a date?

MYRA: (Ignoring.) Aw Lud, clean up your paints, okay? Jesus, I'm running late here.

(LUD collects his paints and puts them in a drawer.)

LUDLOW: When's Rocky getting here?

MYRA: Ricky!

LUDLOW: Reggie.

MYRA: We . . . Listen Lud, I'm gonna pop a vessel here in a sec, just help me out, Okay?

UDLOW: Do what thou wilt swiftfooted time. (Doorbell rings. Both freeze.)

MYRA: (Terrified) Aw, Lud . . . could you . . . um. Hang on a minute, Ricky!!

LUDLOW: Reggie.

MYRA: Aw Sh-Reggie! Be there in a minute! Lud, please, just let him in and tell him I'll be there in a sec. Can you do that for me?

LUDLOW: Of course, I can do it.

MYRA: Will you do it nice? Please? Please, Lud? Nothing funny - this is important.

LUDLOW: I won't converse with him.

MYRA: Does that mean yeah?

LUDLOW: Yeah.

MYRA: Thanks!! (She kisses him on the forehead and sprints into the bedroom. LUDLOW goes to the kitchen window and opens it, then crosses to the door and proceeds to take off the lock. He then heads for the couch and sits. The bell rings again.)

LUDLOW: IT'S OPEN!!
```

---

## IC-0777: First Day of Winter

- Title: First Day of Winter
- Author (byline): Sam Smiley
- Work: More One-Act Plays for Acting Students
- Publisher: Meriwether Publishing
- Publication date as stated: July 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ANDREW, LEAH
- Teaser before the introduction: No
- Spoken words (computed): 1532
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sam Smiley
Book: More One-Act Plays for Acting Students
ISBN: 1566080878
Publisher: Meriwether Publishing
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
The first day of winter, plants begin to die. But are plants the only thing affected by the cold stillness that this season ushers in? As relationships grow, people change, and we begin to realize that some were never truly alive to begin with. What lives, and what dies on the “First Day of Winter” by Sam Smiley.

(LEAH walks into the field carrying a spade and an antique wooden box. She gently sets the wooden box on the earth, shoves the spade into the ground, and lifts out dirt. Then with head bowed she kneels, picks up the box, and presses it against her chest. ANDREW hurries into view and stops momentarily at the edge of the field.)
```

### Performance text (classify this)

```text
ANDREW: Leah. (No reply) Leah, what are you doing out here? (She shakes her head.) What? I can't hear you in the wind.

LEAH: I didn't say anything.

ANDREW: It's winter. (Looks around.) You'll freeze to death out here in the open.

LEAH: No, I won't.

ANDREW: It's five o'clock in the morning! What's going on? I mean, what are you doing out here with a shovel?

LEAH: It's a spade.

ANDREW: All right, a spade. And what're you holding?

LEAH: A box.

ANDREW: I can see that. What's inside?

LEAH: Andy, you know how I hate questions. That's all I get these days, questions... from everyone - parents, friends, teachers, and especially from

ANDREW: Especially from me. Right? (Sarcastic) Well, I'm sorry.

LEAH: It would help a lot if you would just please go away. (Puts her forehead against the box.)

ANDREW: C'mon, Leah. Don't do that. Don't cry. Darlin', get up off that cold ground and talk to me. (She collects herself)

LEAH: I have nothing more to say.

ANDREW: We should get out of this wind. I'm freezing.

LEAH: Button your coat.

ANDREW: Yeah. See? Without you, I'm practically helpless. (He buttons his coat.)

LEAH: Helpless as a shark.

ANDREW: That's not very nice.

LEAH: I'm tired of being nice. Tired of school, tired of this town, and I am deathly tired of

ANDREW: Me?

LEAH: No, of hiding. I want to get on with my life.

ANDREW: Then let's go somewhere warm and talk it out.

LEAH: I said everything last night.

ANDREW: And you think I believed any of it?

LEAH: Andrew, don't make it so difficult, for both of us.

ANDREW: I won't ... if you explain where you've been all night. (She bows over the wooden box.) You know, I've always thought that maroon scarf looks like blood running down your neck. Where were you?

LEAH: I spent the night helping a friend.

ANDREW: Leah, I checked with all your friends - Bonnie, Gina, Max, Darlene - everyone. I went to all your favorite places. I even called Jonathan.

LEAH: You didn't! (She rises.) You called Jonathan? I haven't spoken to him for a year and a half.

ANDREW: He told me that. And I also talked to Professor Carlson.

LEAH: Andy!

ANDREW: I thought you might have some kind of rehearsal.

LEAH: You know perfectly well my final performance was last weekend. I'm done. No more rehearsals or performances. None! I told you that. My degree is finished.

ANDREW: Yeah, Carlson reminded me. Said he hadn't seen you since last Saturday night.

LEAH: Sometimes I could kill you.

ANDREW: Thanks. You know, I don't think Carlson likes me. Every time I'm around him, he watches you like a vulture. I think he's jealous. Has he ever come on to you?

LEAH: (Indignant) Professor Carlson?

ANDREW: OK, look, I'm just tired and upset ... and I'm freezing my tail off. Let's get out of this wind.

LEAH: Go away, Andy. I have something important to do.

ANDREW: Leah, I have been searching for you all night, the whole lousy night! I didn't even go home. See, I'm still wearing the same clothes. (LEAH picks up the spade.) What are you doing? Listen to me a minute, OK? Listen! (She faces him again.) Ever since you walked out of that restaurant ... I mean I sat there for all of a minute, finished my Coke, and went after you. But by the time I got outside, you were gone. Poof! Into the night. I looked everywhere - nothing! I called your place about fifty times, checked with your friends, and ... darlin', you better get off that ground before you catch your death.

LEAH: Don't worry about me.

ANDREW: I am worried out of my mind about you. Leah, I cannot - I know it sounds melodramatic - I cannot live without you. When we're apart, I get this weird sensation. (Touches his chest.) Like there's a steel band clamped around my chest, squeezing the breath out of me. I can't let you go. Now, tell me where you were!

LEAH: Andrew, I spent last night with my cat Samantha.

ANDREW: Oh, yeah sure! Man, my hands are cold.

LEAH: Here, take my mittens. (She starts to remove them, but he prevents her by grabbing her hands.)

ANDREW: No, Leah! I want you to have the mittens, all the clothes you want, career, house, money, fame, fortune, travel... everything your heart desires, because, Leah, I love you. (He draws her close.)

LEAH: You've never said that before, Andy.

ANDREW: Haven't I?

LEAH: In all the time we've spent together, not once.

ANDREW: Well, I do. Very much. (Kisses her.) And you love me, too, don't you? (He lifts her off the ground.)

LEAH: I haven't been able to help myself.

ANDREW: That's my girl. (Sets her down.)

LEAH: I'm touched that you spent the night looking for me.

ANDREW: Yeah, well I did.

LEAH: It shows you honestly care.

ANDREW: I was out of my mind. For all I knew, some skinheads grabbed you in the parking lot and shoved you in a van or something.

LEAH: Not knowing is always worse than reality. (He takes her face in his hands.)

ANDREW: Leah, you are so beautiful. (Lightly kisses her.) But your lips are ice. Let's get out of this wind.

LEAH: No, I have to finish. (She gestures at the hole.)

ANDREW: What are you doing?

LEAH: Digging.

ANDREW: Oh, yeah - for gold? (Laughs a little.)

LEAH: No.

ANDREW: Well, it's the wrong time of year for a garden.

LEAH: It's a grave. (That stops him.)

ANDREW: You got to be kidding. (Again LEAH kneels beside the box.) Leah, what the hell have you got in there? (She shakes her head.) I don't believe it! You've got to be kidding. Don't tell me you... (He gets down on one knee and puts an arm around her shoulders.) Look at me, Leah. Darlin', look at me! (He turns her face toward him.) You never said anything. You never told me.

LEAH: I know. (She pulls away.)

ANDREW: You should have.

LEAH: It doesn't matter now.

ANDREW: Of course it matters! (Loud) It matters!

LEAH: Don't yell at me, Andy.

ANDREW: I'm not. I am simply saying you should have told me. (Beat) So anyway it's all over now, right?

LEAH: Y es, it is past.

ANDREW: (Sudden thought) Leah, you didn't do it yourself! You should've gone to a hospital, right?

LEAH: I did.

ANDREW: Oh. In a hospital- and you're all right?

LEAH: I'm fine.

ANDREW: Now, wait a minute. When did all this happen? Not last night! Is that where you were, in a hospital?

LEAH: No. It happened long before last night. Three weeks ago to be exact. Remember when I told you I had a stomach virus?

ANDREW: (Nods.) But I still don't understand. (Soft) What've you got in the box?

LEAH: Please, Andrew.

ANDREW: Now wait, I want to know. What's in the box?

LEAH: I'll tell you. But first, you explain how you found me.

ANDREW: What do you mean?

LEAH: How did you know to come out here?

ANDREW: Simple. I went up the steps over there in back of the house. (Points.) I knocked on your apartment door, and no one answered. So I turned on the landing and looked around. From that angle up there I could see a dark figure walking into this field. I mean, you're a dancer, and I'd know you anywhere just from the way you move.

LEAH: What phone did you use last night to call my friends?

ANDREW: The one in my office.

LEAH: You drove clear down to your office?

ANDREW: Sure. Better than spending a fortune in quarters.

LEAH: Why didn't you bother to drive out here last night?

ANDREW: I called your apartment, and no one answered.

LEAH: Have you ever been at home but avoided the phone?

ANDREW: You were there?

LEAH: Andy, it is very odd that you searched for me eight and a half hours without ever coming by to look in my apartment. I think you're lying ... again.

ANDREW: Darlin', I swear

LEAH: You're awfully good at it. You didn't search for me all night, did you? You went home to her. Just like always. (ANDREW presses his lips together and gazes into the distance. Pause) It's over, Andy. Today's the first day of winter. It's a natural time to let it die. (LEAH picks up the spade and digs out more dirt.)

ANDREW: Let it die? No, Leah, you want to kill it and bury it. Right? (She continues digging.) I want to know what's in the box. (She goes on.) Come on! Show me!

(He grabs the spade away from her. LEAH picks up the wooden box. sets it on the pile of dirt from the grave. and kneels beside it.)

LEAH: I tacked down the lid. Do you have a pocket knife?

ANDREW: Me? No.

LEAH: I can't get it off.

ANDREW: Here, try one of my keys. My fingers are frozen stiff. (He pulls a ring of keys from his pocket and hands them to her.)

LEAH: Andrew, I don't want to show you this.

ANDREW: Show me, Leah! You better show me, or... (Momentarily, his frustrations come to focus. and he lifts the spade as though he might hit her in back of the head. But of course he cannot. He lowers the Spade and lets it slide out of his hands) Never mind. I don't want to see anything.

LEAH: No, I want you to. (She pries off the lid, lifts the box toward him with both hands like an offering. He looks inside)

ANDREW: I don't believe it. (Tries to laugh.) It's a kitten.

LEAH: What did you expect? Look again.

ANDREW: One little black... no, two black kittens.

LEAH: Look closer.

ANDREW: One black kitten ... with two heads. (Repulsed, he looks away) Oh, man, I am freezing to death.

LEAH: Andrew, last night I helped my cat Samantha give birth to a litter. This little one amazed us both. A totally black, stillborn kitten with two perfect heads.

ANDREW: It's just a freak. Call a newspaper or the museum. (LEAH replaces the lid on the box.)

LEAH: I thought of that, but I decided it was better to bring it out here, into the open, and return it to the earth ... maybe with a prayer.

ANDREW: Then hurry up and do it so we can go to your apartment and wrap ourselves around each other and get warm.

LEAH: Can't you understand? Whatever joy we shared, it's ...

ANDREW: ... only temporary, right? Leah, think of all the great times we've had - the hiking, the skiing, the cabin in the woods. You want to end it? I have promised and promised you that one of these days we'll go away together!

LEAH: Y ou don't believe that and neither do I and anyway it's too late. It was too late when I went to the hospital.

ANDREW: Well, I'll tell you one thing - I can't stay out here another minute. I am freezing to death. (Beat) Maybe you're right. Maybe it's time for me to just walk away.

LEAH: Good-bye, Andrew.

ANDREW: Why in the name of... why bury a freak kitten?

LEAH: Because it was real, because life is so inventive, because I wonder what other strange seeds lie hidden in some secret womb. I only want to cover it peacefully with dark soil ... and a blanket of dried weeds. (ANDREW nods and walks away. LEAH sets the little box into its grave.)
```

---

## IC-0778: For Whom the Southern Belle Tolls

- Title: For Whom the Southern Belle Tolls
- Author (byline): Christopher Durang
- Work: Christopher Durang: Twenty-Seven Short Plays (Pg 9-30)
- Publisher: Smith and Kraus
- Publication date as stated: Jan 1995
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: AMANDA, LAWRENCE, GINNY
- Teaser before the introduction: Yes
- Spoken words (computed): 1448
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christopher Durang
Book: Christopher Durang: Twenty-Seven Short Plays (Pg 9-30)
ISBN: 978-1880399897
Publisher: Smith and Kraus
Date (Month/Year): Jan 1995
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Welcome to a twisted sendup of Tennessee Williams’ The Glass Menagerie! ACTOR: For Whom the Southern Belle Tolls by Christopher Durang
```

### Performance text (classify this)

```text
NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: ACTOR: Lawrence ACTRESS: Amanda, Ginny

AMANDA: (Pg 12-13) Rise and shine! Rise and shine! (Calls off) Lawrence, honey, come on out here and let me have a look at you! (Enter LAWRENCE, who limps across the room. He is very sensitive and is wearing what are clearly his dress clothes. AMANDA fiddles with his bow tie and stands back to admire him.)

AMANDA: Lawrence, honey, you look lovely.

LAWRENCE: No, I don't mama. I have a pimple on the back of my neck.

AMANDA: Don't say the word "pimple," honey, it's common. Now your brother Tom is bringing home a girl from the warehouse for you to meet, and I want you to make a good impression, honey.

LAWRENCE: I don't need to meet people, mama. I'm happy just by myself, playing with my collection of glass cocktail stirrers. (LAWRENCE limps over to a table on top of which sits a glass jar filled with glass swizzle sticks) Each one of them has a special name, mama. This one is called Stringbean because it's long and thin; and this one is called Stringbean because it's long and thin; and this one is called Blue because it's blue.

AMANDA: (Pg 13) Oh, Lawrence honey, how are you going to get on in the world if you just stay home all day, year after year, playing with your collection of glass cocktail stirrers?

LAWRENCE: I don't like the world, mama, I like it here in this room.

AMANDA: I know you do, Lawrence honey, that's part of you charm. Some days. But, honey, what about making a living?

LAWRENCE: I can't work, mama. I'm crippled.

AMANDA: (Firmly) There is nothing wrong with your leg, Lawrence, all the doctors have told you that. This limping thing is an affectation.

LAWRENCE: I only know how I feel, mama. You know I have asthma.

AMANDA: Your asthma, your leg, your eczema. You're just a mess, Lawrence!

LAWRENCE: I have scabs from the itching, mama.

AMANDA: Now, Lawrence, I don't want you talking about your ailments to the feminine caller. No nice-bred young lady likes to hear a young man discussing his eczema, Lawrence.

LAWRENCE: What else can I talk about, mama? (Pg 14-15) I don't know if I want to meet some girl who works in a warehouse, mama.

AMANDA: Your brother Tom says she's a lovely girl with a nice personality.

LAWRENCE: It's unfeminine for a girl to work at a warehouse.

AMANDA: (Firm, frustrated) Lawrence, honey, if you can't go out the door without getting an upset stomach or an attack of vertigo, then we got to find some nice girl who's willing to support you. Otherwise, how am I ever going to get you out of this house and off my hands?

LAWRENCE: (sensitive, unknowing) Why do you want to be rid of me, mama?

AMANDA: I suppose it's unmotherly of me, dear, but you really get on my nerves. Limping around the apartment, pretending to have asthma. If only some nice girl would marry you and I knew you were taken care of, then I'd feel free to start to live again. I'm not bitter, dear, it's just that I hate my life. (Knock at the door)

LAWRENCE: I'll be in the other room. (Starts to limp away)

AMANDA: I want you to let *her* in, Lawrence.

LAWRENCE: Oh, I couldn't mama. She'd see I limp.

AMANDA: Then don't limp, damn it. Now, Lawrence, you march over to that door or I'm going to break all your swizzle sticks.

LAWRENCE: Mama, I can't! My eczema itches. Excuse me. I think I hear someone calling me in the other room. (Limps off, calls to imaginary person) Coming! (AMANDA opens door)

GINNY: (Very friendly, and very loud) CALL ME GINNY OR GIN! BUT JUST DON’T CALL ME “LATE FOR DINNER”!! (Roars with laughter)

AMANDA: Oh, how amusing. (To herself) Why is she shouting?

GINNY: (Pg 16) I am taking a course in public speaking, and so far we've covered speaking good and loud so the people in the back of the room can hear you.

AMANDA: Public speaking. How impressive. You must be interested in improving yourself.

GINNY: (Loudly and happily) YES I AM!

AMANDA: Dinner is almost ready, Ginny.

GINNY: Oh good. I'm as hungry as a bear! (Growls enthusiastically)

AMANDA: (Sarcastically) You must be very popular at the warehouse, Ginny. Let me see if I can convince Lawrence to come out here and make conversation with you. (From off-stage) (Pg 17) Now you get out of that bed this minute, Lawrence Wingvalley, or I'm going to give that overbearing girl your entire collection of glass gobbledygook - is that clear? (AMANDA pushes in LAWRENCE) I believe Lawrence would like to visit with you, Ginny. (Amanda exits, but spies from off stage)(LAWRENCE stands still, uncomfortable. GINNY looks at him pleasantly)

GINNY: (Pg 18-19) (Loudly) HI.

LAWRENCE: Hi . . .

GINNY: Why are you wearing that nightshirt?

LAWRENCE: I'd gone to bed. I wasn't feeling well. My leg hurts and I have a headache, and I have palpitations of the heart. (Beat) We've met before, you know. We were in high school together. You were voted Girl Most Likely To Succeed. We sat next to one another in glee club.

GINNY: I'm sorry, I really can't hear you. You're talking too softly.

LAWRENCE: (Louder) You used to call me BLUE ROSES.

GINNY: Blue Roses? Oh yes, I remember, sort of. Why did I do that?

LAWRENCE: I had been absent from school for several months, and when I came back, you asked me where I'd been, and I said I'd been sick with viral pneumonia, but you thought I said "blue roses."

GINNY: I remember you now. You used to make a spectacle of yourself every day in glee class, clumping up the aisle with this great big noisy leg brace on you leg. God, you made a racket.

LAWRENCE: I was always so afraid people were looking at me, and pointing. But then eventually mama wouldn't let me wear the leg brace anymore. She gave it to the Salvation Army. (Awkward pause) You want to see my collection of glass cocktail stirrers? (He limps to the table, and limps back to her, holding his collection) I call this one Stringbean, because it's long and thin. They're my favorite thing in the world. (Holds up another one) I call this one Q-tip, because I realized it looks like a Q-tip, except it's made out of glass and doesn't have little cotton swabs at the end of it. (She looks blank) Q- TIPS.

GINNY: Really? (She takes it and puts it in her ear)

LAWRENCE: No! Don't put it in your ear. (Takes it back) Now it's disgusting.

GINNY: Well, I didn't think it was a Q-tip, but that's what you said it was.

LAWRENCE: I call it that. I think I'm going to throw it out now. (Holds up another one) I call this one Pinocchio because if you hold it perpendicular to your nose it makes your nose look long. (He holds it to his nose)

GINNY: Uh huh. I know you're tired, I figured that's why you put on the night shirt, but this won't take long. I judge you to be lacking in self-confidence. Am I right?

LAWRENCE: Well, I am afraid of people and things, and I have a lot of ailments.

GINNY: But that makes you special, Lawrence. (Pg 20) And that's why you should present yourself with more confidence. Throw back your shoulders, and say, "HI! HOW YA DOIN'?" Now you try it.

LAWRENCE: (Unenthusiastically, softly) Hello. How are you?

GINNY: (Booming) "HI! HOW YA DOIN'?"

LAWRENCE: Hi. Howya doin'?

GINNY: Now swagger a bit. (Kinda butch) HI. HOWYA DOIN'?

LAWRENCE: (Imitates her fairly successfully) HI. HOW YA DOIN'?

GINNY: Good, Lawrence. That's much better. Again. HI! HOW YA DOIN'?

LAWRENCE: HI! HOWYADOIN'?

GINNY: THE BRAVES PLAYED A HELLUVA GAME, DON'TCHA THINK?

LAWRENCE: THE BRAVES PLAYED A HELLUVA GAME, DON'TCHA THINK?

AMANDA: (Off-stage) Oh God I feel sorry for their children. (Amanda enters to put a stop to this)

GINNY: HI, MRS. WINGVALLEY. YOUR SON LAWRENCE AND I ARE GETTING ON JUST FINE. AREN'T WE, LAWRENCE?

AMANDA: Please, no need to shout. I'm glad you like Lawrence.

GINNY: What?

AMANDA: WHY DON'T YOU MARRY LAWRENCE?

LAWRENCE: Oh, mama.

GINNY: (Looks shocked) Oh dear. Mrs. Wingvalley, if I had a young brother as nice and as special as Lawrence is, I'd invite girls from the warehouse home to meet him too. (Pg 21) But I'm afraid I won't be calling on Lawrence again.

LAWRENCE: This is so embarrassing. I told you I wanted to stay in my room.

GINNY: But, Lawrence, I don't want you to think that I won't be calling because I don't like you. I do like you.

LAWRENCE: (Looking hopeful) You do?

GINNY: Sure. I like everybody. But I’m involved with a girl named Betty. We’ve been going together for about a year. We’re saving money so that we can buy a farmhouse and tractor together. No hard feelings, Lawrence. You’re a good kid.

LAWRENCE: (Offers her a swizzle stick) I want you to keep this. It's my very favorite one. I call it Thermometer because it looks like a thermometer.

GINNY: You want me to have this? (She drops the offered gift)

LAWRENCE: (Horrified) You’ve broken it! (Pg 22) YOU’VE BROKEN THERMOMETER!

GINNY: So, I’ve broken it. Big deal. You have twenty more of them here. What was a thermometer doing in with the swizzle sticks anyway?

LAWRENCE: Its name was Thermometer, you nitwit!

GINNY: (Cheerful, her basic nature) Well, so long, everybody! I had a nice time. (Exits)

AMANDA: (Pg 24) Oh Lawrence, honey, what's to become of us?

LAWRENCE: (Pg 25-26) Oh, poor mama, let me try to cheer you up with my collection. (Holds up a yellow swizzle stick) I call this one Daffodil, because its yellow, and daffodils are yellow.

AMANDA: Uh huh.

LAWRENCE: (Holds up another one) And I call this one Curtain Rod because it reminds me of a curtain rod.

AMANDA: Uh huh.

LAWRENCE: (Holds up another one) And I call this one Ocean, because it's blue, and the ocean is . . .

AMANDA: I THOUGHT YOU CALLED THE BLUE ONE BLUE, YOU IDIOT CHILD! DO I HAVE TO LISTEN TO THIS PATHETIC PRATILING THE REST OF MY LIFE??? CAN'T YOU AT LEAST BE CONSISTENT???

LAWRENCE: (Hurt) No, I guess I can't. (Silence – Amanda looks a t Lawrence and feels bad for yelling at him. She decides to try to make up)

AMANDA: Do you have any other swizzle sticks with names, Lawrence?

LAWRENCE: Yes, I do. (Holds one up) I call this one "Mama." (He throws it viciously onto the floor)
```

---

## IC-0779: Fortunately, the Milk

- Title: Fortunately, the Milk
- Author (byline): Neil Gaiman
- Work: Not specified
- Publisher: HarperCollins
- Publication date as stated: Sept 2014
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ME, DAD, SISTER, ALIEN, PIRATE QUEEN, STEG, PONY, VAMPIRE, POLICE
- Teaser before the introduction: Yes
- Spoken words (computed): 1691
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Gaiman
ISBN: 978-0062224088
Publisher: HarperCollins
Date (Month/Year): Sept 2014
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Author Neil Gaiman is a phenomenon.

ACTRESS: We’re not saying that's good. We’re not saying that's bad. We’re simply stating a fact.

ACTOR: A fellow author recently commented that when Gaiman talks, people clap.

ACTRESS: When he coughs, they laugh.

ACTOR: And there’s no better way to introduce you to his unique storytelling style than to take you on a mystical adventure with an imaginative and creative father in

TOGETHER: Fortunately, the Milk by Neil Gaiman
```

### Performance text (classify this)

```text
Suggested Roles: Actor: Dad Actress: Everyone else!

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

ME: (searching the refrigerator) There was only orange juice in the fridge. Nothing else that you could put on cereal, unless you think that ketchup or mayonnaise or pickle juice would be nice, which I do not.

DAD: Eat your cereal. Remember, it’s Orchestra Practice this afternoon

SISTER: We can’t eat our cereal. No milk.

ME: He looked like he was going to suggest that we have something for breakfast that you do not need milk for, like sausages, but then he remembered that, without milk, he couldn’t have his tea.

DAD: You poor children. I will get milk . . .

SISTER: Where have you been all this time?

DAD: I bought the milk. I walked out of the corner shop and heard something odd coming from above me. It was a noise like this: thummthumm. I looked up and saw a huge silver disc hovering in the air. And the next thing I knew, I was being sucked up into the disc. Fortunately, I had put the milk into my coat pocket. The people in the disc were a bit green and rather globby and they looked very grumpy indeed.

ALIEN: As a representative of your species, we demand that you give us ownership of the whole planet. We are going to remodel it.

DAD: I jolly well won’t. (to the kids) I noticed a large metal door with EMERGENCY EXIT DO NOT OPEN FOR ANY REASON THIS MEANS YOU! on it. I opened the door.

ALIEN: Don’t do that. You’ll let the space-time continuum in.

DAD: But it was too late; I had already pushed open the door. I JUMPED. Fortunately, I had kept tight hold of the milk, so when I splashed into the sea I didn’t lose it.

PIRATE QUEEN: What was that? A big fish? A mermaid? Or was it a spy?

DAD: I wanted to say that I wasn’t any of those things, but my mouth was full of seawater. I felt myself being hauled up onto the deck. There were a number of men and a woman on the deck, and they all looked very cross.

PIRATE QUEEN: Who be ye, landlubber? What are you doing here?

DAD: Well . . . I just set out to the corner shop for some milk for my children’s breakfast and for my tea, and the next thing I knew—

PIRATE QUEEN: You dare lie to the Queen of the Pirates?

DAD: If I did not go to the corner shop to fetch the milk, then where did this milk come from?

(showing her the milk)

PIRATE QUEEN: You’re on a pirate ship now, my fine bucko. There are only two choices—you can join my pirate crew, or refuse to join and we will slit your cowardly throat and you will go to the bottom of the sea, where you will feed the fishes.

DAD: I wish that I could, but I have children. And they need their breakfast.

PIRATE QUEEN: Then you must die! Walk the plank!

DAD: I edged out to the end of the plank. Sharks were circling. So were piranhas—

ME: Hang on. Piranhas are a freshwater fish. What were they doing in the sea?

DAD: You’re right. Right. So . . . I was out at the end of the plank, facing certain death, when a rope ladder hit my shoulder . . .

STEG: QUICKLY! CLIMB UP THE ROPE LADDER!

DAD: Fortunately, the milk was pushed deep into the pocket of my coat. And I soon made it to the top of the rope ladder. I’d never been in the basket of a hot air balloon before.

STEG: I hope you don’t mind me helping, but it looked like you were having problems down there.

DAD: You’re a stegosaurus!

STEG: I am an inventor. I have invented the thing we are traveling in, which I call Professor Steg’s Floaty-Ball-Person-Carrier.

DAD: (to Steg) I call it a balloon . . . (to the kids) He showed me his Time Machine. He was very proud of it. It was a large cardboard box with several pebbles on it, and stones stuck to the side. There was also a large, red button. (to Steg) Hang on. Those are diamonds. And sapphires. And rubies.

STEG: Actually, I call them special-shiny-clear-stones, special-shiny-bluey-stones, and, um—

DAD: Well, it was very lucky for me that you turned up when you did and rescued me. I need to get home in order to make sure my children get milk for their breakfast. (shows him the milk) Although I expect that one hundred and fifty million years ago you called it ‘wet-white-drinky-stuff. Can you take me home?

STEG: Yes and no. Yes, I would love to take you home. Nothing would make me happier. No, I cannot take you home. My Time Machine is being temperamental. I have pressed that button many times but nothing happens.

DAD: Button? Don’t you mean ‘big-red-flat-pressy-thing’?

STEG: I most certainly do not. It is a button. I named it after my Aunt Button.

DAD: Can I press it? (to the kids) I pressed the button. The sun shot around the sky, and the balloon began to rock and lurch and zoom around like an angry fly. I held on to the ropes as hard as I could. Fortunately, I was still keeping tight hold of the milk in my right hand.

SISTER: Are there any ponies in this? I thought there would be ponies by now.

DAD: (ad libbing like crazy to somehow incorporate ponies) The machine stopped. We were hanging in the air above a grassy plain. Below me, on a number of brightly colored ponies were gathered.

PONY: You must be the man with the milk. We have heard about you, in our tales.

SISTER: I’m so glad there were ponies.

DAD: The milk! My children are breakfastless . . . (to the kids) And with that, Professor Steg pressed the red button with his heavily armored tail. There was a ZOOM, a TWORP, and a THANG, and we were hurtling through the cosmic void --FLOATING above a landscape of ominous towers and castles. It was not a friendly place. Bats flew across the sky in huge flocks. There was a loud FLUT!, and where the bats had been, several pallid people were now standing. The man in front had a very bald head. THEY ALL HAD SHARP TEETH.

VAMPIRE: Ve are wumpires. Vot is this? Who are you? Answer us, or ve vill wiwisect you.

STEG: I am Professor Steg. We are on an important mission. My assistant is trying to get home to the future for breakfast.”

DAD: At the word BREAKFAST all the wumpires looked very excited.

VAMPIRE: Ve have not had our breakfast. Ve normally have vigglyvorms, vith orange juice on them. Orange juice makes vorms ewen vigglier. Like vandering spaghetti. But if ve cannot eat vorms ve vill eat assistant, or ewen roast professor.

DAD: One of the wumpires took out a fork and looked me up and down in a hungry sort of way. The professor tinkered with the jewels and the string and the buttons.

STEG: I think I’ve got it properly fine-tuned, now. This next press should bring you back to your own time, place, and breakfast.

DAD: I pressed the red button. The hole in space opened again. And [we and] the milk came rocketing through. There was an ear-popping noise and I was floating, in a balloon basket. I could see our house. I could see the bicycles in the back garden. I could see the rabbit hutch.

ME: Does that mean that there is a Stegosaurus in a hot air balloon outside?

DAD: There is not. For reasons that will become apparent

SISTER: (wistfully) I think that there should have been some nice wumpires . . . Nice, handsome, misunderstood wumpires.”

DAD: There was a familiar sort of a thumm-thumm noise, and before I had a chance to press the red button [again], we were deposited, balloon and all, on the enormous metal deck of a flying saucer, with a number of very grumpy-looking green globby people staring at us with too many eyes. They did not look pleased.

ALIEN: HaHA! You thought you had escaped us! And you were wrong! Now, you must sign the planet over to us so that we can remodel it. We will take out all the trees and put in plastic flamingoes. Also, we are going to replace the clouds with scented candles. We have been tracking your movements through time and space. Now, see what happens when I press this grundledorfer (points to a button on the spaceship control panel).

DAD: It’s called a button.

ALIEN: Nonsense. We named it after our brood-aunt, Nessie Grundledorfer. (pushes the button)

DAD: There was a CRACKLE. There was a FIZZ. Standing around us, in attitudes of anger and irritation, were several pirates and some wumpires.

PIRATE QUEEN: Prepare to be keelhauled, you scurvy dogs.

VAMPIRE: Ve vants those willains and warmints wiolently vound up.

DAD: The aliens looked at each other. One of them pressed the grundledorfer. The wumpires and pirates were gone. It was at that moment that a voice louder than anything I have ever heard said

POLICE: GALACTIC POLICE. DO NOT MOVE.

DAD: There were red and blue flashing lights and about half a dozen uniformed dinosaurs, holding unmistakably large and extremely serious weapons. They pointed their weapons at the green globby aliens.

POLICE: You are charged with breaking into people’s planets and redecorating them. And then with running away and doing it again somewhere else, over and over. You have committed crimes against the inhabitants of eighteen planets, and crimes against good taste. DADThe Tyrannosaurus handcuffed all the green globby people together with something that looked a lot more like pink string-in-a-can than it looked like handcuffs, which was a good thing because they probably didn’t have hands and they definitely didn’t have wrists. The last I saw of any of them, the whole inside of the saucer was fading into light so bright I had to close my eyes and look away. And then I was standing at the back door of our house, none the worse for wear. So I came in. And here I am . . .

ME: That was what my dad said. I looked around the kitchen. At the calendar on the wall with the hot air balloons on it. At my dinosaur models and my sister’s ponies, at my sister’s vampire books.

SISTER: You know we don’t believe any of this.

ME: Especially not how you saved the world from being remodeled. Or the pirates. Not. Any. Of. It.

DAD: (shrugging) Suit yourselves. But it was all true. And I can prove it. Here’s the MILK!
```

---

## IC-0780: The Fourposter

- Title: The Fourposter
- Author (byline): Jan de Hartog
- Work: Best American Plays 4th Ed.
- Publisher: Crown Publishing Group
- Publication date as stated: July 1958
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SHE, HE
- Teaser before the introduction: Yes
- Spoken words (computed): 1381
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jan de Hartog
Book: Best American Plays 4th Ed.
ISBN: 0517504367
Publisher: Crown Publishing Group
Date (Month/Year): July 1958
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: It is 1901 and Michael and Agnes have been married for eleven years.

ACTOR: They have had a wonderful marriage, but now there are strains, serious strains. They are both feeling unappreciated.

ACTRESS: Michael has finally become a successful author, doted upon by admirers.

ACTOR: And Agnes, who has been his muse and honest critic, is feeling pushed aside.

TOGETHER: The Fourposter by Jan de Hartog
```

### Performance text (classify this)

```text
ACT II, SCENE 1

(AT RISE, there is no one in the room. SHE enters door Center and slams the door behind her. SHE stands at - the foot of the bed, removing her evening gloves. Crosses up Right to dressing table, throws gloves on the table, crosses Left Center and is stopped by a KNOCK at the door. SHE stands Left Center for a moment. The KNOCK is repeated, more insistently. )

SHE: (After a pause.) Come in.

HE: (Enters, closes door.) Excuse me. (Goes to the dressing room Left, gets his night clothes, re-enters and crosses to door up Center.) Good night.

SHE: (As HE opens door.) You were the life and soul of the party this evening, with your interminable little stories.

HE: (Starts out, stops, turns.) My dear, if you don't enjoy playing second fiddle, I suggest you either quit the orchestra or form one of your own. (Goes out and shuts door.)

SHE: (Mutters after a moment's stupefaction.) Now, I've had enough! (Runs to door, rips it open, stands in hallway and calls off.) Michael! (Then bellows.) Michael! Come here!

(Re-enters, crosses Left Center, takes off evening wrap, throws it on bed.)

HE: (Pops in. At up Center. Has top hat and cane in hand and evening cape over arm.) Have you taken leave of your senses? The servants?

SHE: (At Left Center.) I don't care if the whole town hears it. (HE exits) Come back, I say!

HE: (Re-enters.) All right. This situation is no longer bearable! (Closes door.)

SHE: What on earth is the matter with you?

HE: Now, let me tell you one thing, calmly. (SHE crosses below him to dressing table up Right. Takes off plume, throws it on table.) My greatest mistake has been to play up to you, plying you with presents

SHE: I like that! (Picks up gloves.)

HE: Calmly! Do you know what I should have done? I should have packed you off to boarding school, big as you are, to learn deportment.

SHE: (Turns to him.) Deportment for what?

HE: (Crossing down Center.) To be worthy of me.

SHE: The pompous idiot whose book sold three hundred thousand copies!

HE: That is entirely beside the point.

SHE: It is right to the point! (Carrying gloves.) Before you had written that cursed novel, the rest of the world helped me to keep you sane. (HE crosses Left.) Every time you had finished a book or a play or God knows what, and consid-ered yourself to be the greatest genius since Shakespeare(HE says, "Now really!" HE puts cape, hat, gloves on wall chair Left.) -I was frightened to death that it might turn out to be a success. (SHE crosses to him.) But, thank Heaven, it turned out to be such a thorough failure every time, that I won the battle with your egolomania. But now, now this book, the only book you ever confessed to be trash until you read the papers-oh, what's the use! (Crosses down Right Center, rolls up gloves.)

HE: My dear woman, I may be vain, but you are making a tragic mistake. . .

SHE: (Crossing up Center. Laughs.) Now listen! (Laughs.) Just listen to him! To be married to a man for eleven years, and then to be addressed like a public meeting. (Throws gloves on dressing table.) Tragic mistake! (HE sits Left center. SHE crosses down to him.) Can't you hear yourself, you poor darling idiot, that you've sold your soul to a sentimental novel?

HE: Agnes, are you going on like this, or must I

SHE: Yes, yes, you must! You shall hear it. (HE pounds floor with cane.) And don't interrupt me! There is only one person in this world who loves you in spite of what you are, and let me tell you- (SHE crosses Center.)

HE: You are mistaken. There is a person in this world who loves me-because of what I am.

SHE: (At Center.) And what are you, my darling?

HE: Ask her.

SHE: Her

HE: Yes.

SHE: Oh- (Crosses up Center, holds onto bed post.) Who is she?

HE: You don't know her.

SHE: Is she-young? (Turns upstage.) How young?

HE: No. (Rises. Crossing Left. Picks up clothes.) I'll be damned if I go on with this. You look like a corpse.

SHE: A corpse?

HE: (Crossing up to arch.) So pale, I mean. (At door.) Agnes, I'm not such a monster, that- (Crossing down Center to her.) Sit down. Please, Agnes, do sit- Agnes!

SHE: (Turns away. Crossing down Left.) No, no-it's nothing. I'm all right. What do you think? That I should faint in my thirty-first year because of something so-so ordinary?

HE: Ordinary?

SHE: With two children? I didn't faint when Robert had the mumps, did I?

HE: (Crossing down Center.) Don't you think this is a little different?

SHE: No, Michael. This belongs to the family medicine chest.

HE: I love-her!

SHE: SO, not me anymore? (HE doesn't reply.) I don't mean as a friend, or as-as the mother of your children, but as a wife? (HE crosses down Right.) You may tell me honestly, really. Is that why you've been sleeping in the study?

HE: (At window Right.) I haven't slept a wink.

SHE: (At Left Center.) I see. It must be Cook who snores.

HE: (Turns to her.) Since when do I snore?

SHE: Not you, dear, Cook. Every night when I went down the passage.

HE: (Goes to the door, opens it.) Good night!

SHE: (At Left Center.) Sleep well.

HE: (Crossing down Center.) What was that?

SHE: Sleep well.

HE: Oh- (Stops at door, then slams it shut.) No! (Throws clothes down on sofa at foot of bed. Down Center.) I'll be damned, I won't stand it!

SHE: What is the matter?

HE: Cook snores! Agnes, I love somebody else! It's driving me crazy! You, the children, she, the children, you-for three weeks I have lived through hell, and all you've got to say is "Cook snores!"

SHE: (Steps toward him.) But darling

HE: (Crossing below sofa down Right.) No, no, no; no! You are so damned sure of yourself that it makes me sick! (SHE crosses up Center facing bed.) I know you don't take this seriously, but believe me, I love that woman! I must have that woman or I'll go mad! (Crosses to above sofa.)

SHE: (Turns to him.) Haven't you-had her yet?

HE: (Crosses Center to her.) At last! Thank God, a sign of life. (SHE sits on sofa at foot of bed.) Why haven't you looked at me like that before? I have begged, implored, crawled to you for a little understanding and warmth, and love, and got nothing. Even my book, that was written inspired by you, longing for you-right from the beginning you have seen it as a rival. (Crossing down Left.) Whatever I did, whatever I tried: a carriage, servants, money, dresses, paintings, everything-you hated that book. And now? (Crossing up Left.) Now you have driven me into somebody else's arms. Somebody else, who understands at least one thing clearly: that she will have to share me with my work. (Above chair down Left.)

SHE: Does she understand that she will have to share you with other women as well?

HE: She doesn't need to. At last I found a woman who'll live with my work, and a better guarantee of my faithfulness nobody could have. (Crosses onto dais.)

SHE: But how does she live with it? What does she do?

HE: She listens. (Sits on bed.) She encourages me-with a look, a touch, a-well, an encouragement. When I cheer, she cheers with me, when I meditate, she meditates with me

SHE: And when you throw crockery, she throws crockery with you?

HE: (Checks himself.) Haven't you understood one single word of what I have been saying? Won't you, can't you see that I have changed?

SHE: No.

HE: (Rises. Crossing up Right Center.) Then you are blind, blind, blind! That's all I can say. At any rate, you've changed.

SHE: I!

HE: (Crossing Right to above sofa.) No, don't let's start that.

SHE: Go on.

HE: No, it's senseless. No reason to torture you any longer, once I have . . .

SHE: Once you have tasted blood?

HE: (Crossing around sofa.) Agnes, I'm sorry it was necessary for me to hurt you. It couldn't very well have been done otherwise. I'm at the mercy of a feeling stronger than I. (Sits sofa.)

SHE: Rotten, isn't it?

HE: Horrible.

SHE: And yet-at the same time not altogether.

HE: No. On the other hand, it's delicious.

SHE: The greatest thing a human being can experience.

HE: I'm glad you understand it so well.

SHE: Understand?-why, of course. It's human, isn't it?

HE: How do you come to know that?

SHE: What?

HE: That it's-human? Agnes, I never heard you talk like this before. What’s the matter with you?

SHE: Well, I might have my experience too, mightn't I (Rises. Crossing onto dais, picks up clock from bed-table.) Goodnight!

HE: (Rises. Crossing to foot of bed.) Just a minute! I want to hear a little more about this.

SHE: But I know it now, dear.

HE: Yes, you do! But I don't! What sort of experiences are you referring to?

SHE: (Crossing to him. Puts clock on tabouret.) Now listen, my little friend! You have dismissed me without notice, and I haven't complained once as any other housekeeper would have done. I have accepted the facts, because I know a human being is at the mercy of this feeling, however horrible and at the same time delicious it may be.

HE: (At up Center.) Agnes!

SHE: (On dais.) I really don't understand you. I am not thwarting you in the least, and instead of your going away happily and relieved that you are not going to leave a helpless wreck behind

HE: (Crossing up to arch.) You might answer just one plain question before we finish this business. Have you-aren't you going to be alone, if I leave you?

SHE: Alone? I've got the children, haven't I?

HE: (Crossing down Center.) That's not at all certain.

SHE: (After a shaky silence.) You had better leave this room very quickly now, before you get to know a side of me that might surprise you a lot.

HE: (Crossing to her.) I have, I'm afraid. I demand an answer. Have you a lover?

SHE: (Goes to door, opens it. Stands down Right of door.) Good night.

HE: For eleven long years I have believed in you! (Crossing to her.) You were the purest, the noblest thing in my life!

SHE: (Interrupting, and with him.) -the noblest thing in my life! Good night!

HE: If you don't answer my question, you'll never see me again.

SHE: Get out of here.

HE: (Sits on sofa at foot of bed.) No.

SHE: All right. (Crossing onto dais.) Then there's only one thing left to be done.

(SHE picks up wrap from bed and crosses into dressing room Left.)

HE: What? What did you want to say? (She does not answer. SHE returns with second wrap and night case; puts them both on chair down Left and opens case.) What's the meaning of that? (SHE goes on, crosses onto dais, picks up nightgown and negligee. Crosses down Left, packs them in case.) Darling, believe me, I won't blame you for anything, only tell me (Rises, stands Left Center.)-where are you going?

SHE: (Crossing up Right to dressing table and getting brushes and comb.) Would you mind calling a cab for me?

HE: (Turning to her.) Agnes!

SHE: (Crossing down Left packs brushes and comb in case.) Please, Michael, I can't arrive there too late. It is such an embarrassing time already. Pass me my alarm clock, will you?

HE: No, I can't have been mistaken about you that much! Only yesterday you said that I had qualities

SHE: Excuse me. (Passes him, gets her alarm clock from the tabouret. Crosses down Left, puts clock in case.)

HE: (Wants to stop her when she passes, but checks himself.) All right. It is a solution, anyhow.

SHE: (Closes overnight case, picks it up, puts wrap over arm, crosses Left around chair to him and puts out her hand. HE refuses. SHE starts Center below him. HE blocks her way.) Goodbye, Michael.
```

---

## IC-0781: The Frog Prince Continued

- Title: The Frog Prince Continued
- Author (byline): Jon Scieszka
- Work: Not specified
- Publisher: Viking Juvenile KS State Qualifier
- Publication date as stated: May 1991
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR 1, NARRATOR 2, PRINCESS, PRINCE, WITCH 1, WITCH 2, WITCH 3, FAIRY GODMOTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1059
- Already set (do not supply): none

### Source block (context only)

```text
2003 National Qualifier
Author: Jon Scieszka
2007 National Qualifier
ISBN: 978-0670834211
2008 National Qualifier
Publisher: Viking Juvenile
KS State Qualifier
Date (Month/Year): May 1991
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: And they lived happily ever after . . .

ACTOR: This is where most fairy tales end. The prince and princess marry and ride off into the sunset to begin their new life together as husband and wife, a life full of promise, romance, and above all, love.

ACTRESS: But no one has ever told us how this is supposed to happen, or why it succeeds if it does.

ACTOR: In The Frog Prince Continued by Jon Scieszka, the truth behind happily ever after is revealed

ACTRESS: Warts and all.

ACTOR: (CROAKS)

TOGETHER: The Frog Prince Continued by John Scieszka
```

### Performance text (classify this)

```text
Suggested Roles: Actor: Narrator 2, Prince

Actress: Narrator 1; Princess; Witches 1, 2 and 3; Fairy Godmother

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NARRATOR 1: The Princess kissed the frog,

NARRATOR 2: He turned into a prince and they lived happily ever after.

NARRATOR 1: Well, let’s just say they lived sort of happily for a long time.

NARRATOR 2: Okay, so they weren’t so happy. In fact, they were miserable.

PRINCESS: Stop sticking your tongue out like that.

PRINCE: How come you never want to go down to the pond anymore?

NARRATOR 1: The Prince and Princess were so unhappy.

NARRATOR 2: They didn’t know what to do.

PRINCESS: I would prefer that you not hop around on the furniture. And it might be nice if you got out of the castle once in a while to slay a dragon or giant or whatever.

NARRATOR 2: The Prince didn’t feel like going out and slaying anything. He just felt like running away.

NARRATOR 1: But then he reread his book. And it said right there at the end of his story: “They lived happily ever after. The End.”

NARRATOR 2: So he stayed in the castle and drove the Princess crazy. Then one day, the Princess threw a perfectly awful fit.

PRINCESS: First you keep me awake all night with your horrible, croaking snore. Now I find a lily pad in your pocket. I can’t believe I actually kissed your slimy frog lips. Sometimes I think we could both be better off if you were still a frog.

NARRATOR 2: That’s when the idea hit him. The Prince thought. “Still a frog…. Yes! That’s it!” And he ran off into the forest, looking for a witch who could turn him back into a frog.

NARRATOR 1: The Prince hadn’t gone far when he ran into just the person he was looking for.

PRINCE: Miss Witch, Miss Witch. Excuse me, Miss Witch. I wonder if you could help me?

WITCH 1: Say, you’re not looking for a princess to kiss are you?

PRINCE: Oh, no. I’ve already been kissed. I’m the Frog Prince. Actually, I was hoping you could turn me back into a Frog.

WITCH 1: Are you sure you’re not looking for a beautiful sleeping princess to kiss and wake up?

PRINCE: No, no -- I’m the Frog Prince.

WITCH 1: That’s funny. You don’t look like a frog. Well, no matter. If you’re a prince, you’re a prince. And I’ll have to cast a nasty spell on you. I can’t have any princes waking up Sleeping Beauty before the hundred years are up.

NARRATOR 2: The Prince didn’t stick around to see which nasty spell the witch had in mind.

NARRATOR 1: He ran deeper into the forest until he came to a tiny cottage where he saw another lady who might help him.

PRINCE: Miss Witch, Miss Witch. Excuse me, Miss Witch. I wonder if you could help me. I’m a prince and---“

WITCH 2: Eh? What did you say? Prince?

PRINCE: No, I mean, yes. I mean, no, I’m not the prince looking for Sleeping Beauty. But, yes, I’m the Frog Prince. And I’m looking for a member of your profession who can turn me back into a frog so I can live happily ever after.

WITCH 2 : Frog Prince, you say? That’s funny. I thought frogs were little green guys with webbed feet. Well, no matter: If you’re a prince, you’re a prince. And I can’t have any princes rescuing Snow White. Here- eat the rest of this apple.

NARRATOR 2: The Prince, who knew his fairy tales (and knew a poisoned apple when he saw one), didn’t even stay to say, “No Thank you.”

NARRATOR 1: He turned and ran deeper into the forest. Soon he came to a strange-looking house with a witch outside.

PRINCE: Ahem. Miss Witch, Miss Witch. Excuse me, Miss Witch. I wonder if you could help me? I’m the Frog-

WITCH 3: If you’re a frog, I’m the King of France.

PRINCE: No, I’m not a frog. I’m the Frog Prince. But I need a witch to turn me back into a frog so I can live happily ever after, can you do it?”

WITCH 3: (eyeing the Prince and licking her lips) Why, of course, dearie. Come right in. Maybe I can fit you in for lunch.

NARRATOR 2: The Prince stopped on the slightly gummy steps. Something about this house seemed very familiar. He broke off a corner of the windowsill and tasted it. Gingerbread.

PRINCE: I hope you don’t mind my asking, Miss Witch. But do you happen to know any children by the name of Hansel of Gretel?

WITCH 3: Why yes, Prince darling, I do. I’m expecting them for dinner.

NARRATOR 2: The Prince who, as we said before, knew his fairy tales, ran as fast as he could deeper into the forest.

NARRATOR 1: Soon he was completely lost. He saw someone standing next to a tree. The Prince walked up to her, hoping she wasn’t a witch, for he’d quite had his fill of witches.

PRINCE: Madam. I am the Frog Prince. Could you help me?”

FAIRY GODMOTHER: Gosh, do you need it. You are the worst-looking frog I’ve ever seen.

PRINCE: I am not a frog. I am the Frog Prince And I need someone to turn me back into a frog so I can live happily ever after.

FAIRY GODMOTHER: Well, I’m on my way to see a girl in the village about going to a ball, but I suppose I could give it a try. I’ve never done frogs before, you know.

NARRATOR 2: And with that the Fairy Godmother waved her magic wand, and turned the Prince into a beautiful carriage.

NARRATOR 1: The Prince couldn’t believe his rotten luck. The sun went down. The forest got spookier. And the Prince became more and more frightened.

PRINCE: Oh what an idiot I’ve been. I could be sitting at home with the Princess, living happily ever after. But instead, I’m stuck here in the middle of this stupid forest, turned into a stupid carriage. Now I’ll probably just rot and fall apart and live unhappily ever after.

NARRATOR 1: The Prince thought these terrible, frightening kinds of thoughts (and a few worse-too awful to tell), until far away in the village the clock struck midnight. The carriage instantly turned back into his former Prince self,

NARRATOR 2: and ran by the light of the moon until he was safe inside his own castle.

PRINCESS: Where have you been? I’ve been worried sick. You’re seven hours late. Your dinner is cold. Your clothes are a mess.

PRINCE: The Prince looked at the Princess who had believed him when no one else in the world had, the Princess who had actually kissed his slimy frog lips. The Princess who loved him.

NARRATOR 1: The Prince kissed the Princess.

NARRATOR 2: They both turned into frogs.

NARRATOR 1: And they hopped off happily ever after.
```

---

## IC-0782: Funeral Parlor

- Title: Funeral Parlor
- Author (byline): Christopher Durang
- Work: Naomi in the Living Room and Other Short Plays, Pgs 39-52
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Oct 1988
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, MARCUS, SUSAN, BOTH
- Teaser before the introduction: Yes
- Spoken words (computed): 1127
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christopher Durang
Book: Naomi in the Living Room and Other Short Plays, Pgs 39-52
ISBN: 978-0822214489
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Oct 1988
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Funerals are supposed to be quiet. ACTOR 2: Respectful.

ACTOR 1: Brief. ACTOR 2: You say you’re sorry –

ACTOR 1: Nod solemnly – TOGETHER: And leave.

ACTOR 1: Susan is trying to grieve her husband with dignity.

ACTOR 2: Minimal conversation. ACTOR 1: Maximum composure.

ACTOR 2: Unfortunately . . . TOGETHER: Marcus has arrived.
```

### Performance text (classify this)

```text
A funeral parlor. Quiet setting. Hushed atmosphere. Susan, the mourning widow, is sedate, proper and formal. A few people are in line, offering their condolences, shaking her hand. She acknowledges them with a little nod and little smile, and a whispered “Thank you.” As the scene begins, at the end of the line to see Susan is a man named Marcus. Marcus reaches Susan. He is sincere and genuine, it’s just that he’s, well, odd.

(beat)

ACTOR 1: Funeral Parlor ACTOR 2: by Christopher Durang

MARCUS: (Pgs 39-52) Susan, I’m so sorry. My deepest condolences.

SUSAN: Yes, thank you . . . ?? (She doesn’t know who Marcus is)

MARCUS: Marcus.

SUSAN: (Still doesn’t know him, but is gracious) Yes, Marcus. Thank you for coming.

MARCUS: We’ll all miss him terribly.

SUSAN: Yes, It’s a great loss.

MARCUS: We’ll all miss him.

SUSAN: Yes.

MARCUS: You must feel terrible.

SUSAN: Well . . . I don’t feel good. It was a terrible shock.

MARCUS: Death is always a shock. You’re sitting home doing nothing, and then suddenly death goes “Boo!”, and somebody falls down dead.

SUSAN: Yes. (Looks around, hopes someone else will come over)

MARCUS: What were his last words? Were they “Boo”?

SUSAN: What? “Boo”? No. He didn’t really have any last words.

MARCUS: Did he make any last noises?

SUSAN: Noises? What?

MARCUS: Guttural sorts of noises? Or high pitched shrieking ones? (Makes high-pitched sounds) Eeeeeeeeek! Eeeeeeek! Awoooooga! Awooooooga!

SUSAN: Just noises, I don’t know. They were lower than that. Don’t do that anymore.

MARCUS: (Sympathetically) Oh, Susan, you poor, poor thing. (Turns to someone who’s gotten in line behind him) I wouldn’t wait if I were you, I’m going to be a while. (The person in line looks surprised but goes away; Susan looks alarmed). All alone in the house now. Alone in the kitchen. Alone in the dining room. Alone in the living room – living room, that’s a mocking phrase now, isn’t it? Alone, alone, alone. All alone. Alone, alone, alone.

SUSAN: Please don’t go on.

MARCUS: Yes, but you have to mourn, Susan, to mourn. I always thought the Irish were right to do all that keening. Do you want to keen, Susan?

SUSAN: Not really. Thank you anyway.

MARCUS: How about singing a Negro spiritual?

SUSAN: I don’t think so. (Looks madly for people)

MARCUS: (Sings) Swing low, sweet chariot, Comin’ for to carry me home . . .

SUSAN: Thank you for coming.

MARCUS: Don’t you want to sing?

SUSAN: I don’t want to keen or sing. I’m an Episcopalian. I’ll cry quietly in my room later this evening. Now I must attend to the other mourners.

MARCUS: Susan, you’re avoiding the sadness, I can’t let you do that.

SUSAN: Please, please let me do that. It’s been a terrible day. I have to bury my husband.

MARCUS: Is he in the casket? It’s a closed casket, he’s not actually in some other room, propped up in some stuffed chair or other, waiting there to startle someone, is he?

SUSAN: Certainly not. Thank you so much for coming.

MARCUS: That would give someone quite a fright. They’d be standing by this chair making conversation and then realize they were talking to him, only he was stark, stone dead! Ahahahahahahaha, that would be a good one!

SUSAN: Yes, very good. (Calls) Oh, David! (No luck)

MARCUS: I’m going to miss him too, you know.

SUSAN: Ah, how nice. Or rather, how sad. Well, time heals everything.

MARCUS: You’re not the only one with sorrow written on your forehead.

SUSAN: What?

MARCUS: I should say not. (Shows his forehead, previously covered with his bangs; it has “sorrow” written on it) Magic marker. Doesn’t wash off. We’re going to miss him on the commuter train. We used to exchange morning pleasantries. “Nice morning,” or “Cold enough for you?” or “The train seems to be on time today for a change.”

SUSAN: I see. Excuse me. I think the mortician is signaling me.

MARCUS: You know, your husband was the only person on that whole damn train who was even willing to speak to me.

SUSAN: (Very much at a loss) How interesting.

MARCUS: The other people would get panic in their eyes if I even started to walk in their direction, and they’d move away, or pretend to sleeping. But they didn’t fool me, I’m no dope. You can’t sleep standing up!

SUSAN: (Trying to make small talk.) Well, if you’re tired enough maybe you can.

MARCUS: Your husband, though, was always very friendly to me. Not like my father. Nowadays my father won’t even return my phone calls, I went to a séance and everything

SUSAN: What?

MARCUS: Well, he’s dead, but I have this medium friend who gave me this special 800 number that lets you call the dead. Maybe you’d like the number to try to reach your husband on the other side.

SUSAN: I don’t think so. Well, que sera, sera. Ah me. La dee dah. Well, thank you so much for coming.

MARCUS: (Warmly) Well, you’re welcome. I just feel so terrible about your husband being gone, and I don’t know what I’m going to do on the train in the morning.

SUSAN: Yes. Well – why don’t you read a book?

MARCUS: That’s an idea. Do you have any suggestions?

SUSAN: Oh my, I don’t know. The Thorn Birds, Great Expectations. Any book, I don’t care.

MARCUS: My favorite book is Babar the Elephant.

SUSAN: Yes, that is excellent.

MARCUS: Have you read it?

SUSAN: No, but I hear wonderful things. Ah me. My., My. Well, thank you for coming. Good-bye.

MARCUS: (Surprised) Are you leaving?

SUSAN: (Losing her temper) No, I’m not leaving. I want you to leave. You’re making me hysterical. Can’t you take a hint. When I say “Thank you for coming,” that’s code for “Go away now.” Don’t you understand that?

MARCUS: (Terribly abashed, a bit hurt) Oh. I’m sorry. I thought it just meant “Thank you for coming.” I’m sorry. I didn’t realize I . . . Is there anything else you’ve said in code I haven’t understood?

SUSAN: No. Nothing. I don’t think so.

MARCUS: (Still a little thrown) Oh good. (He looks very abashed and embarrassed.)

SUSAN: It’s . . . just . . . well . . . (Feeling badly for him.) Oh dear, now I feel terribly guilty about having expressed my emotions.

MARCUS: (Friendly again, thinking of her) Oh don’t feel guilty about expressing emotions. That’s a good thing to do. You’ve had a terrible loss.

SUSAN: (Somewhat seriously, realizing) Yes, I have.

MARCUS: Are you sure you don’t want to keen yet? I’m not Irish, but I think it’s a very appropriate thing to do at a wake.

SUSAN: Oh I don’t know. Maybe another time.

MARCUS: This would be the most likely time.

SUSAN: Well, I don’t know. (A little interested) What does keening sound like exactly?

MARCUS: Oh, it’s real interesting. It’s sort of like this. (Marcus makes an enormously strange, low, sustained moan-whine that goes up and down the scale. The rest of the people present come to a dead halt and stare.)

SUSAN: (To crowd; slightly annoyed.) Please stop staring. Go back to your conversational buzz.

(The crowd goes back to its hum)

MARCUS: Did I do something wrong again?

SUSAN: Well, it was a very startling sound.

MARCUS: It’s just like crying, but more dramatic. I love to cry. You loved your husband, didn’t you?

SUSAN: (Genuine) Yes.

MARCUS: Well, then, don’t you want to keen just a little?

SUSAN: Well, I see your point a little but . . . I don’t know that I really could.

MARCUS: You could do it softer than I did.

SUSAN: I don’t think so

MARCUS: Oh please, I’m sure it would make you feel better.

SUSAN: (Wanting to feel better) Would it? (Starts to, but freezes) This is difficult to do in public. Couldn’t I call you later this evening, and do it on the phone?

MARCUS: No, it’s much more healing to keen at the funeral. You shouldn’t do it on the phone.

SUSAN: Oh, I don’t know.

MARCUS: Come on. It’ll help.

SUSAN: (Hesitates, but then) Oooooooo (It’s very soft Sounds like a ghost sound, or a person imitating the wind)

MARCUS: That’s good

SUSAN: Ooooooooo.

MARCUS: That’s good AAAAAAOOOOOOWWWWWWOOOOOOOO!!!! (Susan looks aghast for a moment. The crowd stops and stares again. Momentary silence. After a beat, Susan gives in to some odd combination of grief and having fun, and makes extremely loud keening sound simultaneously with Marcus)

BOTH: AAAAAAAAAOOOOOOOOOOOOWWWWWWWWOOOOOOOOOOO!!!! (From out of these very satisfying, if shocking noises, Susan starts to cry loudly and uninhibitedly. Marcus pats her on the back in a comforting manner, looking out at the crowd a bit proudly as if to say “See what I did?” Susan’s crying subsides, and her breathing returns more to normal)

MARCUS: There, that’s better.

SUSAN: (Drying her yes) Thank you so much for coming. (Just as Marcus begins to wonder) No, no, not code. Thank you. I feel much better.

MARCUS: Oh good. Well, you’re welcome. (Marcus and Susan shake hands warmly. Marcus smiles at her, moves aside, as other mourners come over to speak to Susan. Quick fade. End).
```

---

## IC-0783: A Gaggle of Saints

- Title: A Gaggle of Saints
- Author (byline): Neil LaBute
- Work: Bash: Latterday Plays; Pgs 35-70
- Publisher: Overlook Press
- Publication date as stated: December 1999
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JOHN, SUE
- Teaser before the introduction: Yes
- Spoken words (computed): 1967
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil LaBute
Book: Bash: Latterday Plays; Pgs 35-70
ISBN: 978-1585670246
Publisher: Overlook Press
Date (Month/Year): December 1999
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Some of the most frightening moments in life are when you realize that a person you love and trust has been putting up a front the whole time:

ACTOR: The husband that comes out of the closet.

ACTRESS: Grandparents who get divorced after being together forever.

ACTOR: Discovering you had siblings you didn't know about.

ACTRESS: These things happen to "normal" people all the time. People are capable of anything.

ACTOR: In Gaggle of Saints, Neil LaBute introduces us to John and Sue, two Mormon sweethearts who tell the story of attending a formal dance in New York City.

ACTRESS: But it’s what happens after the dance in Central Park that makes the unexpected frightening.

TOGETHER: A Gaggle of Saints by Neil LaBute
```

### Performance text (classify this)

```text
Silence . . . a young, attractive couple stand apart from one another, dressed in the evening fashion.

JOHN: (Pg 35-36) So, okay, there was this big bash in the city. That’s what we came down for. This get-together. Couple churches together, I think, and meeting in the city. Ballroom over at the plaza.

SUE: People from high school were going. Seniors now, mostly.

JOHN: We're juniors up at B.C., so, like, there’s still lots of guys we know, who we’re still in touch with. Friends, you know . . . (Pg 38) It just sounded really great, weekend back in New York. Stop in, maybe, say "hi" to the folks . . .

SUE: (Pg 39) We all thought we could go down together. One car. Everybody wanted to, gonna be in the city at this hotel, live band and everything. . .

JOHN: (Pg 39-40) And so six of us, a girl that's going out with this David from my fraternity, Karen's her name; I think. . . she was coming too cause she knew the city pretty well,

SUE: David said he'd drive and we're all picked up at three in the afternoon, Saturday.

JOHN: I’m rushing around, fighting for tuxedos, ten minutes to six, Friday afternoon! (beat) I ended up with a Perry Ellis. Finally. A size big, but I got one. . . looks okay, doesn't it?

SUE: It looked good on him. . .I had to put a safety pin in the vest, in the back of it, but it was really nice when he had it on. I had this dress I’d been saving. . . all black taffeta.

JOHN: (Pg 41-44) Kind of a cutaway in the front, what’s it called? “Scalloped,” in the front and no back to it at all. (beat) She looked great . . .

SUE: This was going to be a great party (pause) I could feel it. It was our anniversary. . .

JOHN: Last minute got her a corsage. White blossoms. Don’t know what kind, but they were white. I remember that. . .

SUE: The softest pink, it was . . . John thought it was white, but it was really just the lightest shade of pink. (beat) And you know? He pricked his finger, John did. As he pinned it on me, pricked his index finger. . .

JOHN: Stupid pin!

SUE: A spot of blood, just a drop on his shirt. . . in a weird way it excited me. The blood. (beat) I mean, the bright of his shirt . . . and then this splash of blood on his chest.

JOHN: Didn't get any on her dress. Felt good about that. . . wouldn't want to ruin her anniversary dress.

SUE: Four years. . .

JOHN: (Pg 45) Believe that? Four . . .since summer of our third year in high school. Wow. . .

SUE: (Pg 53-56) It was going to be great. A really good evening, I could feel it. . .

JOHN: And we walk arm in arm. Man, feels so nice to stroll past all these people, I mean, rich guys, girl like that on my arm! Made me feel strong, you know? Powerful.

SUE: We've got nowhere to go. . . nothing but possibilities. The party's not until later. . .

JOHN: David’s girlfriend, "Karen," takes the lead at some point, walking us through the park. . . over by that one bridge, the big pond? Moon's smiling down and all, romance hanging over a night like this out of some storybook . . . I really do love this girl. That’s the thing that's screaming out in my head right then. . .

SUE: He was holding my hand so tight. . .

JOHN: A perfect night. And then, off to our left, there's this, like, patch of woods near the path. Comes this rustling. . . I’m not scared but it's night . . .what else can you do, girls with you?

SUE: I thought it might be some teenagers. We all started to walk a bit faster . . .

JOHN: And two middle-aged guys, L.L. Bean shirts, come out of the dark. Smiling. And I don't need a map to tell me what's been going on (pause) I don't.

SUE: It was just two men. Walking along. . . no big deal.

JOHN: They were off in the park alone. And these smiles. One dude looks like my father, a little, it's dark but he had that look, right, that settled, satisfied sort of . . . anyway, off they head, arms linked together and nothing we say ever going to change what they are. (pause) [We] Dance all night . . .

SUE: I haven't danced like that in a long time. . .

JOHN: I’m telling you, I can't get that picture out of my head. Those smiles. I can't do it. . . (beat) but the party is great. It really is. . .

SUE: (Pg 57-58) I’d never been to the plaza before, I mean, past it, shopping and whatever, with my mom, but never to it. It was tremendous! So much glass. (Pg 56) They’d done the whole room in blues and golds with these great moons, these golden crescents handing above us.

JOHN: Like smiles . . .

SUE: (Pg 58) High white walls. . . (beat) the whole thing, though. . . the trip, dance and all. . .made me sleepy.

JOHN: Sue went upstairs to our room with Karen and Tim’s girlfriend, Patrice . . . Said they wanted to take a quick nap, then we'd go get a bite. This was, like, maybe, one-thirty. . .

SUE: (Pg 59) I’m not sure what time it was . . .

JOHN: We hung out downstairs a bit, talked to some guys from home. . .David, Tim, and me. I was bored. You know. . .so I suggested a walk. "Let’s head over to the park." We shoot over into Central Park, the 59th Street entrance. . . looking around, talking. Really dark in there. Only lights coming from the buildings, way off. Kind of exciting. . .

SUE: I thought I looked up at two, or two-fifteen. . . but I’m not sure. 'cause I kept sleeping. . .

JOHN: . . .and then I saw 'em. Both of them. Those guys. . . (Pg 60-61) They were saying "goodnight. . ." well, not saying it exactly. But kissing. Two grown men, standing in this public park in the middle of New York and kissing like something out of a Clark gable film. Arms around each other, and nothing else in the world matters to these two. . . hands all where they shouldn't be. I mean, come on, I know the scriptures, know 'em pretty well, and this is wrong.

(beat)

SUE: All of us, we were sleeping so peacefully (beat) Did you know Patrice snores? She does . . . a little.

JOHN: You know, you read about it, right, and you live with it. Don’t love it; don't condone it for the world. Still,live and let live, whatever. But this is flaunting it. I mean, we're in town one night, that's all, one. . . and we got 'a witness this? (pause)

SUE: I’d known Patrice since kindergarten . . .

JOHN: Men old enough to be our fathers clutching at one another like Romeo and Juliet! (beat) I start to feel sick, I mean it, nauseous. Then a last peck on the cheek and one disappears down a trail, headed for the west side. He’s gone. The other one glances around, taking in the night, I guess, big smile up at the moon. . . and he strolls over to this "men's room." 50 yards off. Concrete building, with the steps down into it. Whistling while he goes. . . he was whistling. I don't even stop to think this through but motion the guys to follow me.

SUE: (Pg 50) [John and I] are getting engaged this summer, we already planned it . . .

JOHN: (Pg 62) I told the guys to hold off. Wait for me to flush him out, make sure no one wanders by. Our friend's legs, I spot, patiently sitting in a stall. Not a care in this world. I slip into the stall next to his, start fumbling with my belt; and like clockwork, this guy's hand comes up under my side of the partition. Pink fingers, wiggling up at me, imploring.

SUE: (Pg 43) The softest pink, it was . . . John thought it was white, but it was really just the lightest shade of pink. (beat)

JOHN: (Pg 62) I notice this thin gold band on his little finger, catching the light. (beat) Two minutes later we're standing near the mirrors and sizing each other up. Name’s "Chet," he says, and I don't even bat an eyelash as he moves in, his lips playing across my cheek. I just smile at him. I see his shoulders relax.

SUE: (Pg 43) It was our anniversary. . .

JOHN: (Pg 62-63) Then I let out a whistle that sends him stumbling back. Tim and Dave appear in the doorway. Chet comes back from his fantasies, a flicker in his eyes, realizing no good can come from this. . . and starts babbling. Even got down on his knees and the pleading. Begging. (beat) Probably a VP at some bank and he’s wetting himself like an infant.

SUE: (Pg 53) It was going to be great. A really good evening, I could feel it. . .

JOHN: (Pg 63) My first shot catches him just under the eye and he slams into a sink. With so many of us hitting, tearing at him, it's hard to get off a clean punch but I know I connect a few more times. Tim kicking him long after he's blacked out. . . (pause)

SUE: (Pg 69) Anyway, we are getting engaged this summer, for sure. Did I tell you that?

JOHN: (Pg 63-64) And then it's silence. Not a sound. And then, I’m leaning down, pulling that ring off his pinkie. (beat) I told you I noticed it. . . And that's how we leave him. . . pause. We all start, giggling, can’t catch our breath we find it all so funny. We slip out, one by one, whooping it up like Indians.

SUE: The phone woke me up. . .

JOHN: We wanted to take the girls out to breakfast. Say they'll be down in fifteen minutes. . . (pause) We waited outside.

SUE: (Pg 65) I got the other girls up. . .took a minute, but I got them up. I felt really refreshed (pause) I did.

JOHN: Dave’s walking around on the curb, talking to himself, and Tim pulls me aside. Wants to why I touched the guy. Let him kiss me. He’d glanced inside and seen it. But I didn't know, didn't have an answer. Isn’t that strange?

SUE: It was so quiet in the lobby as we were leaving. I started tip-toeing out. Isn’t that funny? (Pg 66-67) We met in front of the hotel, and I saw John's face. All cut up like he'd fallen. [He said he was] racing along the fountain out front, balancing on it, and slipped. Scraped himself up and blood on everything. (beat) Silly games. . . (pause) I was eating my French toast, when I notice this glint in my water glass. A spark of light. (beat) John'd slipped a ring in it! A beautiful gold thing. . . I loved him so much at that moment.

JOHN: Happy anniversary

SUE: It was a little big, but fit pretty well. Had this wonderful leaf pattern, all the way around. . . I kissed him there, in front of everybody, and he blushed a bit. We all laughed. I can't tell you what a wonderful weekend we had. . .

JOHN: We did end up taking the Amtrak back up. . .just Sue and myself.

SUE: It was my idea. . .the train. On the way back – I shouldn’t even bring this up – a fight broke out. Well, not really a fight but this argument between a man and his girlfriend. A lot of yelling. She stand ups and starts pulling on her coach and this guy, I mean, just backhands her.

JOHN: (Pg 68) Knocked her up against the window, really hard. He’d given her a bloody nose.

SUE: I could feel John tense up, but the couple was kind of dirty-looking and they seemed like, you know . . . those kind of people. So I whispered to John to “let it go” (beat) and you know what? He didn’t so much bat an eyelash. Just kept holding my hand and playing with the ring on my finger. That made me so happy . . .

JOHN: (Pg 69) And finally, as we tumbled along toward Massachusetts, I could feel Sue fall asleep against my shoulder. All warm. Protected. But not me. . .I couldn't drift off. So I sat up, watching the lights dance by, the moon grinning down. And you know, I started whistling to myself. I did. . .

SUE: I was asleep there on john's arm, but I’d swear I could hear music. . .

JOHN: Not loud, I mean, don't even recall the tune. But I was whistling. . .

SUE: (Pg 70) . . .this beautiful music as I was sleeping. Like the sound of angels calling us home. . .
```

---

## IC-0784: Geniuses

- Title: Geniuses
- Author (byline): Abbey Fenbert
- Work: The Best 10-Minute Plays 2015
- Publisher: Smith and Kraus Publishers
- Publication date as stated: 2016
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, POLLY, WILFRED, WILFRED/ POLLY, OLLY
- Teaser before the introduction: Yes
- Spoken words (computed): 1138
- Already set (do not supply): none

### Source block (context only)

```text
Author: Abbey Fenbert
Book: The Best 10-Minute Plays 2015
ISBN: 978-1575258980
Publisher: Smith and Kraus Publishers
Date (Month/Year): 2016
```

### Introduction (context only: never use it for content warnings)

```text
Intro starts with actors still in character:

ACTRESS: Twins . . . God’s way of saying (Pointing to Actor) “One of you is a rough draft!”

ACTOR: Be honest though. Isn’t life so much better when you have a twin to share the ride?

ACTRESS: Hey, I may be a twin, but I am one of a kind! (Drop character)

TOGETHER: Geniuses by Abbey Fenbert
```

### Performance text (classify this)

```text
CHARACTERS:

POLLY: a ten-year-old with a penchant for scientific observation.

WILFRED: her long-suffering twin brother with a penchant for setting things on fire.

WILFRED: I'm really sorry about what happened. (POLLY does not answer. She reaches for a notebook and pen and begins to write.)

POLLY: 'Sunday, eighty-forty-five p.m. Wilfred issues an apology. Uninspired. Insincere.'

WILFRED: Hey, stop that! It was not insincere!

POLLY: Do you even know what 'insincere' means?

WILFRED: Do so. Lacking earnesty. Honestness. I mean ... It was one of our Reading Words last week.

POLLY: I see.

WILFRED: Look, I'm sorry.

POLLY: (writing) 'Eight forty-seven. Wilfred attempts repeat apology. Truncated.'

WILFRED: Stop logging me.

POLLY: 'Wilfred projects displaced hostility upon the log.'

WILFRED: I give up. (Silence between the twins. Then ... )

POLLY: A substantial apology, Wilfred, must fulfill a number of basic requirements. For one thing, you should enumerate your offenses, rather than vaguely alluding to 'what happened.' The word 'sorry' ought to be voiced in an emphatic tone. And at the very least you should be on your feet. (Pause. WILFRED sighs, then shu.ffies to his feet and stands before POLLY)

WILFRED: Polly. I am very SORRY that I did not prepare a project for the science competition, because I was extremely busy the whole week, as George and I were trying to catch a possum, which turned out to be a cat-and I am deeply APOLOGETIC that in order to find an entry to the science competition at the last minute I dug up Old Lady Spencer's rare chrysanthemum, then placed it in the tank where you were keeping your project-and I am extremely full of REMORSE that the chrysanthemum was loaded with pesticides and poisons that killed all the insects in the tank, thus forcing the salamanders to resort to cannibalism. I'm sorry. (Very long pause as POLLY regards WILFRED.)

POLLY: (clapping) That was very good! (POLLY retrieves a gold star sticker and affixes it to WILFRED'S forehead.)

WILFRED: Hey ... !

POLLY: (writing in log) 'Sunday, Eight-fifty-four. Following explicit and careful instruction, Wilfred demonstrates mastery of fundamental apologetic techniques.' Just one thing, though-newts.

WILFRED: What?

POLLY: Newts, Wilfred. My science experiment had to do with the habits of newts, not salamanders. They are quite similar, but they are ultimately not the same.

WILFRED: Oh. Sorry.

POLLY: All right, now, no need to go overboard on the sorries. One might start to suspect you're getting greedy for gold stars! (WILFRED seethes. POLLY scribbles happily in log.)

WILFRED: Well. There may be one or two other things I haven't gotten round to apologizing over.

POLLY: (still writing, distracted) To be expected.

WILFRED: For example, I'm sorry I told Aunt Linda you were the one who shaved her dog's ears.

POLLY: Fascinating.

WILFRED: I'm also ... distraught ... that I used your red wagon to haul manure and didn't clean it up afterwards.

POLLY: 'Distraught'?

WILFRED: Reading word.

POLLY: Ah.

WILFRED: I'm sorry I used your toothbrush to scrub the toilet.

POLLY: Wilfred!

WILFRED: Do you think you can ever forgive me for telling Brian Fletchley that you've written twelve sonnets on the subject of his eyebrows?

POLLY: How dare you!

WILFRED: I'm also so, so, sorry that I poured maple syrup all over your favorite microscope.

POLLY: You haven't done that.

WILFRED: I plan to. Sorry!

POLLY: (writing) '9 o'clock p.m. Wilfred devolving rapidly. Abhorrent, filthy, repugnant child.'

WILFRED: I'll show you who's an Ab Hornet! (WILFRED snatches log.from POLLY, shoves her aside. Punctuates rant by tearing pages from log.)

WILFRED: Now, yesterday, a million years from now and forever, Polly is an annoying, stuck-up, bullying brainiac who deserves to have all her toothbrushes used as toilet scrubs!

POLLY: No! (POLLY lunges at WILFRED to save her log, but WILFRED kicks her away and leaps triumphant on the bed, where he completes the destruction of the log.)

WILFRED: I ... always ... hated ... those gold stars!

POLLY: You rotten fool! You've ruined everything. That was my science project!

(POLLY grabs one of the torn sheets and begins to sob.)

WILFRED: What are you talking about? That's just your stupid log.

POLLY: Idiot. The log was my entry into the competition! You were the subject.

WILFRED: No ... I thought it was that fat salamander that ate all the others ...

POLLY: Well it wasn't, it was you! I spent hours observing and monitoring and recording ... And now it's all destroyed ... My academic reputation in shambles ... And he wasn't a salamander, he was a newt! (Renewed sobs.)

WILFRED: What do you mean, I'm a science experiment?

POLLY: Isn't it obvious? The mediocre, thoroughly undistinguished twin sibling of a genius.

WILFRED: Thanks a lot.

POLLY: How can it be we shared a womb, but not a mind? How can we be so similar in so many ways, and yet so fundamentally different? How does the unimpressive sibling cope with the daily challenge of interacting with a superior mind?

WILFRED: It copes fine!

POLLY: I was so careful, so detailed ... My report was going to break new ground in the scholarship of the merely normal! (POLLY collapses in sobs. WILFRED sulks.)

WILFRED: Polly ... Polly, stop. (POLLY continues to sob.) Polly ...

POLLY: Y-yes?

WILFRED: Does this mean I can use the fat salamander?

POLLY: (rising) He ... was ... a ... NEWT! (POLLY and WILFRED face off, close in on each other menacingly with each shout.)

WILFRED: Salamander!

POLLY: Newt!

WILFRED: Salamander!

POLLY: Newt!

(WILFRED shouts "Salamander, Salamander, Salamander!" as POLLY begins an equally annoying rant of "Newt Newt Newt!" It builds to an unbearable peak until a loud thumping- as if someone is banging on a wall or the ceiling below-is heard. The twins freeze. A pause.)

WILFRED/ POLLY: Sorry mother! (The following is carried out in strained whispers.)

OLLY: Now look what you've done!

WILFRED: Me! This is your fault, for being such an Ab Hornet!

POLLY: Classic Wilfredian blunder-just the kind of thing that always makes our parents take irrational pity on you.

WILFRED: Believe me, they'll pity you plenty after I'm through.

POLLY: Are you threatening violence? Well-they'll hear!

WILFRED: Not if I rip all your hairs out. Very. Quietly.

POLLY: Don't forget, brother dear, that I happen to know shortcuts to all your essential arteries. (seizes up pen) You won't have time to scream!

WILFRED: (raising hands to strangling position) Neither will you if I'm choking you!

POLLY: I always knew it would come to this! (They are poised to attack. Another thump.)

WILFRED/ POLLY: WE'RE BEING QUIET! (Thump.)

WILFRED: (an epiphany) Polly!

POLLY: What?

WILFRED: I just had a thought.

POLLY: For the first time, I presume?

WILFRED: Do you think our parents ... could be doing an experiment on us? (POLLY scoffs, but is begrudgingly intrigued Lowers pen.)

POLLY: Elaborate.

WILFRED: I mean ... Newts, salamanders, siblings ... Do you think they've shut us in this room together and are just waiting to see how long it takes us to resort to cannibalism?

POLLY: That's complete and utter ...

WILFRED: Fine, laugh ...

POLLY: Genius!

WILFRED: Wait.

POLLY: Wilfred! That's brilliant! Why else would they force two such fundamentally alien individuals into close, hostile contact with few outlets for respite if not to monitor our responses to the extremities of these conditions?

WILFRED: ... Exactly!

POLLY: The shared room, the inequitable distribution of household labor -- they hope to profit scholastically from our suffering. It all makes sense!

WILFRED: We're lab rats.

POLLY: They must have shelves of logs.

WILFRED: And beakers, and chemicals!

POLLY: It's the only plausible hypothesis.

WILFRED: They could be spying on us right now ...

POLLY: Oh, Wilfred, you genius, you genius! Now we can take a leaf from your log, and min their whole experiment.

WILFRED: With fire!

POLLY: No, Wilfred, not with fire-with subterfuge. We mustn't give dear mother and father what they want.

WILFRED: Never.

POLLY: We won't resort to cannibalism!

WILFRED: We'll act like we like each other!

POLLY: Be helpful, encouraging ...

WILFRED: Play fair ...

POLLY: (taking WILFRED'S hand) Hold hands! Oh foolish parents, you'll rue the day you tried to trick us!

WILFRED: Yeah! You will so rue! ... But let's not hold hands.

POLLY: Agreed. Wilfred. We'll have to commit. Until we find those logs, we've got to be the most loving and congenial pair of twins that ever was.

WILFRED: Anything it takes to get back at them. And then we'll find those papers ...

POLLY: Yes!

WILFRED: And set them on fire!

POLLY: No!

WILFRED: Aw. I'm really good at fire.

POLLY: We have to make a copy first. Then we can set them on fire.

WILFRED: A copy ... for blackmail!

POLLY: Precisely!

WILFRED: Genius.

POLLY: But we must make sure to hide the copies in a place where they'll never, ever be found.

WILFRED: In a salamander tank?

POLLY: Newt=-oh, it doesn't matter. They're a little different, but ...

WILFRED: Ultimately the same. (WILFRED and POLLY embrace. The End.)
```

---

## IC-0785: George Orwell’s 1984

- Title: George Orwell’s 1984
- Author (byline): Not specified
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: Sept 1963
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: LOUDSPEAKER, MESSENGER, WINSTON, COFFEE VENDOR, GUARD, O’BRIEN, JULIA, BIG BROTHER’S VOICE, TOGETHER, BIG BROTHER’ VOICE, GOLDSTEIN’S VOICE, SYME, JULIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1628
- Already set (do not supply): none

### Source block (context only)

```text
Adapted by: Robert Owens; Wilton Hall, Jr and William Miles, Jr.
ISBN: 978-0871295422
Publisher: Dramatic Publishing
Date (Month/Year): Sept 1963
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Here’s the thing: 2019 looks a lot like 1984

ACTRESS: And we’re remarkably comfortable with it.

ACTOR: For starters, it’s hard to ignore the similarities between Big Brother and Donald Trump who, for some, commands a similar unwavering fealty.

ACTRESS: Critics are comparing recent attacks on “fake news” to George Orwell’s book 1984.

ACTOR: And I quote, “What you’re seeing and what you’re reading is not what’s happening.”

ACTRESS: In July of 2018, President Trump criticized the media and publicly announced that people should not believe what they see or what they read.

ACTOR: What’s more, I can ask Siri to order a pizza, ask Google to play my favorite song or have Alexa turn on the air-conditioning.

ACTRESS: Yes, and with the power of facial-recognition, some fear that Big Brother can actually track you. Leading to California’s recent ban on such technology.

ACTOR: It’s 2019 . . . How much is 2 + 2 today?

TOGETHER: George Orwell’s 1984 adapted by Robert Owens; Wilton Hall, Jr and William Miles, Jr.

(Pg 12-13) [A messenger enters, carrying an armful of manila folders stuffed with papers]
```

### Performance text (classify this)

```text
Adapted by Robert Owens; Wilton Hall, Jr and William Miles, Jr.

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: ACTOR – Winston, Syme ACTRESS – Loudspeaker, Messenger, Coffee Vendor, Guard, O’Brien, Julia, Big Brother’s Voice, Goldstein’s Voice

LOUDSPEAKER: (Pg 10-11) Attention! Our standard of living has risen 20 percent over the past year. Workers are parading through the streets with banners voicing their gratitude to Big Brother for the new, happy life which his wise leadership has bestowed upon us. All Hail Big Brother! All Love Big Brother! This morning three spies confessed to being members of the Goldstein Brotherhood of Traitors. This afternoon at 1700 hours they will be hanged in Victory Square. All Party members are invited to attend!

MESSENGER: Good morning. Big Brother has plenty for you to do today. [To Syme] Syme, this is for you. [Hands over a folder] You are told to have it translated into Newspeak no later than 1230 hours. [To Winston, handing him a folder of papers] And this is for you Smith. A whole month’s work of malreports from the Times.

WINSTON: Thank you! [As the Messenger turns to leave] Wait! What about Withers? You forgot him.

MESSENGER: [Turning back blankly] Withers? I have nothing here for any Withers.

WINSTON: [Pointing to a desk next to his] This desk right here. The man who’s been working with us – next to me – Withers.

MESSENGER: [Shortly] There’s no such name on my route list. [Exits]

COFFEE VENDOR: (Pg 15-17) Victory Coffee. Victory Coffee. Get your coffee and praise the bounty of Big Brother. [Winston groans as he get up and goes toward her] Have you heard about the Two Minutes Hate this morning. I’m told it’s something special Something plus good. . . Doubleplusgood.

WINSTON: [wearily, to the Coffee Vendor] What is the hate today?

COFFEE VENDOR: [confidentially] I hear it’s going to be Goldstein himself. Isn’t that exciting? I can hardly wait. . . Drink up. Next coffee period at 1100 hours. Get your refills then [Exits]

GUARD: [Shouting] Attention. Attention for a member of the Inner Party. He is Smith, sir. That one . . . number 6079. [Guard exits. Winston jumps to attention behind his desk. O’Brien enters with Julia]

O’BRIEN: Turn the screen down. I don’t want any interruptions. You must remember that although you cannot hear it and can only see the picture of Big Brother, it can still both hear and see you. Many thought criminals have been trapped by that. This is Julia. She is to take the place of – the vacant place next to you. [O’BRIEN exits]

JULIA: (Pg 18-22) [Settles herself behind the desk; she doesn’t know where to begin] Whose place am I taking?

WINSTON: Bob Withers’. [Angrily] I mean, no one’s place. You are taking no one’s place. And unperson. Don’t you understand an unperson. Aren’t you familiar at all with Newspeak?

JULIA: A few words. Crimethink, duckspeak, goodthink Mini-true, I know means the Ministry of Truth. Proles means the workers, the proletarian – they aren’t really human Child-hero means a child who is a member of the children’s Spies organization who has turned in one of his own family for thought-crime But . . . but I’ve never heard of an unperson.

WINSTON: [exasperated] I’ll ask Syme, the expert, to explain Newspeak to you. In the meantime, here is a Newspeak dictionary. In it are all Oldspeak words – what we used to call STANDARD English – translated into Newspeak. An unperson is a person who’s been vaporized – hanged – killed. He no longer exists.

JULIA: Oh! Vaporized. Of course . . . but, he did exist at one time.

WINSTON: [practically yelling] He never existed. That’s your job here. Look here! In the March 17, 1982 edition of the Times, Bob Withers was awarded the goodworker medal. So we choose the name of another worker in the Ministry of Truth on March 17, 1982. Any name. Ad send it to the Times with the correction. That issue is re-run with the corrected name, and all old editions of that issue are destroyed. We toss this message in the incinerator . . . destroy it! Then – there is no record any place on earth that Bob Withers ever existed.

JULIA: But you know he existed.

WINSTON: [warily, certain she is trying to trap him into a speak-crime] I do not know he existed. [Patiently] You know the word double-think? [Julia nods] You must use doublethink. Every good loyal Party member is capable of doublethink. You know the Party slogan: “Who controls the past – controls the future. Who controls the present controls the past.”

JULIA: I didn’t know it had meaning. I thought it just didn’t mean anything . . . like the other slogans: War is Peace . . . . Freedom is Slavery . . . Ignorance is Strength.

WINSTON: Of course it has a meaning. It’s our job here in the Ministry of Truth to carry out that slogan. [His voice grows louder as he loses control] To control the past!

LOUDSPEAKER: Attention! Attention for the Two Minutes Hate. The Two Minutes Hate is about to begin. Stand by for a message from our devoted leader, Big Brother.

BIG BROTHER’S VOICE: [harsh, grating unpleasant] Repeat:

TOGETHER: War is Peace! Freedom is Slavery! Ignorance is Strength!

BIG BROTHER’ VOICE: In a moment you will hear the despised Goldstein, whose shadowy army conspires to destroy our new happy life. Listen to his lies . . . then show him what you think.

GOLDSTEIN’S VOICE: [Quiet, undistinguished voice. At every pause there Winston cries “Liar!” “Swine!” “Criminal!” “Traitor!”] Friends . . . I am Emmanuel Goldstein Your ex leader and still your friend. I am still fighting for your liberty, your freedom, your hope. Big Brother has usurped power. He is a ruthless tyrant. He lies. He talks of a new happy life while he starves your bodies and denies your souls . . .

WINSTON: Traitor! Liar! Spy!

GOLDSTEIN’S VOICE: Remember that all men are created equal, and endowed by their Creator with certain inalienable rights . . . that among these are life, liberty and the pursuit of happiness. Fee yourselves. Down with Big Brother! [Broadcast ends amid Boos and hisses from Winston and everyone returns to work]

WINSTON: (Pg 25-28) Syme . . . . This is Julia. She has been in the fiction department of Minitrue and they still use Standard English there. Here of course, she must understand Newspeak. She doesn’t. [Winston exits and assumes the persona of Syme who instructs Julia]

JULIA: It must be a lot of work inventing new words.

SYME: We don’t invent words – we destroy them . . . scores of them . . . every day. We’re cutting language down to the bone.

JULIA: [in wonder] Do you really destroy words?

SYME: Indeed yes. A beautiful thing – the destruction of words. Absolutely the best way to control thought. What justification is there for a word that is the opposite of some other word?

JULIE: Well, you must . . . I mean – well, take a word like “good”

SYME: All right. What need is there for a word like “bad”? “Ungood” will do just as well.

JULIE: [Interested] How about “better” and “best?” Good . . . better . . . beat!

SYME: We simply say: plus good or doubleplus good. Simple isn’t it? Of course, it was Big Brother’s idea originally.

JULIA: You make it sound as though the language will eventually b cut to where it will be difficult to think at all.

SYME: Exactly! We will defeat Goldstein that way. Newspeak is the only language whose vocabulary gets smaller ever year. The whole aim of Newspeak is to narrow the range of thought.

JULIA: But how does that stop Goldstein or – or have any effect on thought-crime?

SYME: [patiently] Why, because in the end it will make thought-crime literally ipossible, for there will be no words to express it. For instance, take that gibberish of Goldstein’s about “all men being created equal,” That would be impossible to render into Newspeak The closest you could come would be the one word: crime-think. By 2050 – when everyone speaks nothing but Newspeak – not a single human being alive would understand the conversation we are now having. All real knowledge of Oldspeak will be destroyed. Even literature. Chaucer, Shakespeare, Milton All will exist only in Newspeak. [Proudly] I’m working on that now. Orthodoxy! Orthodoxy means not thinking – not needing to think. [Syme hand her a huge dictionary] Read it . . . and call on me for any explanations. [Syme exits]

WINSTON: Now do you understand Newspeak?

JULIA: [very confused] Yes . . I mean no! I understand the words; [but] the why? I don’t understand the why! I should never have been given this job. Nothing adds up. I . . . I’m . . . it’s like saying that two plus two make five.

WINSTON: And if two plus two do make five?

JULIA: [near tears] Do you believe that?

WINSTON: [suddenly all his hate and anger spilling out] You want me to commit a thought-crime, don’t you? A speak-crime – so you can report me. Do you think I’m a complete fool? [regaining his composure, he speaks softly] (Pg 35-36) The past has been abolished Every record has been destroyed or altered . . . every book rewritten. Already we know nothing about the years before the Revolution. I help falsify the past. It will mean the final loss of freedom.

JULIA: Freedom, freedom. What is freedom, Winston? Maybe the Party is right . . . maybe freedom is slavery.

WINSTON: [sharply] No! [Thinks a moment] Freedom is the freedom to say two plus tow is four.

LOUDSPEAKER: (Pg 39) How can you tell a thought-criminal? Look carefully at the ones you suspect. Do they look unlovingly at Big Brother? Yes, face-crime is thoughtcrime. Report these agents of Goldstein’s to your nearest Thought Police. The Thought Police helicopter will be there immediately. [Winston’s face breaks into a big grin] Repeat after me, Smith. Two plus two is five. Two plus two is five . . . . [continues to repeat]

WINSTON: (Pg 74) [overlapping the second sentence softly at first but growing louder and more defiant] Two plus two is four . . . . is four . . . is four . . . is four [He shakes his fists in the direction of the voice and screams] Two plus two is four! It’s four . . . it’s four. Four . . . . (Pg 66) [A Guard stamps into the room and drags Winston away]

LOUDSPEAKER: (Pg 21) War is Peace!

WINSTON: (Pg 71) No!

LOUDSPEAKER: (Pg 21) Freedom is Slavery!

WINSTON: (Pg 71) NO!

LOUDSPEAKER: (Pg 21) Ignorance is Strength!

WINSTON: (Pg 74) [Defiantly] Two plus two is four!
```

---

## IC-0786: Getting It Back from Almost Maine

- Title: Getting It Back from Almost Maine
- Author (byline): John Cariani
- Work: Almost Maine
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: June 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GAYLE, LENDALL
- Teaser before the introduction: No
- Spoken words (computed): 1214
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Cariani
Book: Almost Maine
ISBN: 978-0822221562
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): June 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: On a cold, clear moonless night in the middle of winter, all is not quite what it seems in the remote, mythical town of Almost, Maine.

ACTRESS: As the northern lights hover in the star-filled sky above, Almost’s residents find themselves falling in and out of love in unexpected ways.

ACTOR: Knees are bruised.

ACTRESS: Hearts are broken.

ACTOR: But the bruises heal, and the hearts mend—

TOGETHER: almost—Getting it Back from Almost Maine by John Cariani
```

### Performance text (classify this)

```text
Music fades. We hear someone —Gayle —pounding on a door.

GAYLE: Lendall! (More pounding.) Lendall! (More pounding.) Lendall! (Lights up on the living room of a small home in Almost, Maine. It is furnished with a comfortable chair and an end table. Lendall has been woken up. Maybe he was asleep in bed; maybe he was asleep in the chair. Either way, he's up now. He turns on the light, and goes to answer the door. Gayle continues to pound on the door.)

LENDALL: Okay! Gayle! Shhh! I'm comin', I'm comin'!

GAYLE: Lendall!

LENDALL: Hey, hey, hey! Shh, come on, I'm comin'! (Lendall exits stage left to answer the door.)

GAYLE: (Entering; blowing by him.) Lendall —

LENDALL: (Returning.) What's the matter?, what's goin' on? (Beat. Gayle is stewing.) What?

GAYLE: (She's been in a bit of a state, but she collects herself.) I want it back.

LENDALL: What?

GAYLE: I want it back.

LENDALL: What?

GAYLE: All the love I gave to you?, I want it back.

LENDALL: What?

GAYLE: Now.

LENDALL: (Little beat.) I don't understand —

GAYLE: I've got yours in the car.

LENDALL: What?

GAYLE: All the love you gave to me?, I've got it in the car.

LENDALL: What are you talkin’ about?

GAYLE: I don't want it anymore.

LENDALL: Why?

GAYLE: I've made a decision: We're done.

LENDALL: What?! —

GAYLE: We're done. I've decided. And, so, I've brought all the love you gave to me back to you. It's the right thing to do.

LENDALL: (Bewildered.) Urn, I —

GAYLE: It's in the car.

LENDALL: You said. (Beat. He's kind of paralyzed trying to figure this out.)

GAYLE: (Waiting for him to take some action and go get the love.) I can get it for you, or ... you can get it.

LENDALL: Well, I don't want it back. I don't need it —

GAYLE: Well, I don't want it! What am I supposed to do with all of it, now that I don't want it?

LENDALL: Well, I don't know ...

GAYLE: Well, under the circumstances, it doesn't seem right for me to keep it, so I'm gonna give it back. (She leaves.)

LENDALL: Under what circumstances? (Calling to her.) Gayle —what are — ? I don't understand what — ... What are you doing?

GAYLE: (From off.) I told you. I'm getting all the love you gave to me, and I'm giving it back to you.

LENDALL: (Calling to her.) Well, I'm not sure I want it — whoa! Need help?

GAYLE: Nope. I got it. It's not heavy. (She returns with an ENORMOUS bunch of HUGE red bags full of love. The bags should be filled with clothes or towels [for a little bit of weight and stability] and foam or pillow stuffing [for shape, and to keep them soundless]. She dumps the bags on the floor.) Here you go.

LENDALL: (Truly puzzled, referring to the bags of love.) And this is . . . ?

GAYLE: (Exiting.) All the love you gave me, yeah.

LENDALL: Wow. (Beat.) That's a lot.

GAYLE: (Returning with more bags of love.) Yeah. (She exits.)

LENDALL: Whole lot.

GAYLE: Yeah. (She returns with even more bags of love. There is now a GIGANTIC pile of love in Lendall's living room.)

LENDALL: Wow. What the heck am I gonna do with all this? I mean ... I don't know if I have room.

GAYLE: (Upset.) I'm sure you'll find a place for it (I.e., another woman.) ... And now, I think it's only fair for you to give me mine back because ... I want it back. (Beat.) All the love I gave to you?

LENDALL: Yeah?

GAYLE: I want it back. (Beat.) So go get it. (Lendall doesn't move. He's probably trying to figure out what is happening and why it's happening.) Lendall, go get it, (Lendall still doesn't move.) Please. (Lendall still doesn't move.) Now!!!

LENDALL: (A little shaken; a little at a loss.) Okay. (Lendall exits. Gayle sits in the chair and waits. She's still in a state. Long beat. Lendall returns... with a teeny-tiny little bag— a little red pouch —and places it on a little table next to the chair. They look at the little bag. The little bag should be between Lendall and Gayle.

And Gayle should be between the many bags of love and the little bag of love.)

GAYLE: What is that?

LENDALL: (It's obvious — it's exactly what she asked for.) It's all the love you gave me.

GAYLE: That's — ... ? That is not — . There is no way — ... That is not — . (Mortified.) Is that all I gave you?

LENDALL: It's all I could find ...

GAYLE: Oh. Okay. (Taking in the little bag... and then at all the big bags.) Okay. (And she's crying.)

LENDALL: Gayle ... What's goin' on, here?

GAYLE: I told you: We're done.

LENDALL: Why do you keep saying that?

GAYLE: Because —. (This is hard to say, but has to be said.) Because when I asked you if you ever thought we were gonna get married — remember when I asked you that? (Lendall doesn't seem to want to remember.) In December? ... It was snowing?

LENDALL: (But he remembers.) Yeah.

GAYLE: Yeah, well, when I asked you ... that, you got so ... quiet. And everybody said that that right there shoulda told me everything.

LENDALL: Everybody who?

GAYLE: Everybody!

LENDALL: Who?

GAYLE: ... Marvalyn

LENDALL: Marvalyn?!? Marvalyn said that, like she's an expert?

GAYLE: said — yes, Marvalyn, yes, said that how quiet you got was all I needed to know, and she's right: You don't love me.

LENDALL: What — ? Gayle, no!

GAYLE: Shh! And I've been trying to fix that, I've tried to make you love me by giving you every bit of love I had, and now ... I don't have any love for me left, and that's ... that's not good for a person ... and ... that's why I want all the love I gave you back, because I wanna bring it with me.

LENDALL: Where are you going?

GAYLE: I need to get away from things.

LENDALL: What — ? What things?! There aren't any things in this town to get away from!

GAYLE: Yes there are: You!

LENDALL: Me?

GAYLE: Yes. You are the things in this town I need to get away from because I have to think and start over, and so: all the love I gave to you? I want it back, in case I need it. Because I can't very well go around giving your love — 'cause that's all I have right now, is the love you gave me — I can't very well go around giving your love to other guys, 'cause that just doesn't seem right —

LENDALL: Other guys? There are other guys?!?

GAYLE: No, not yet, but I'm assuming there will be.

LENDALL: Gayle —

GAYLE: Shh!!! So I think — . I think that, since I know now that you're not ready to do what comes next for people who have been together for quite a long time (I.e., get married.), I think we're gonna be done,

LENDALL: Why? Gayle — !

GAYLE: and so, I think the best thing we can do, now, is just return the love we gave to each other, and call it ... (Taking in the bags — the pathetic one that contains the love she gave him, and the awesome several that contain the love he gave her.) ... even. (It's not "even" at all). Oh, Jeezum Crow, is that really all the love I gave you, Lendall? I mean, I thought — . I mean, what kind of person am I if this is all the love I gave y — ... No ... n-n-no! (Fiercely.) I know I gave you more than that, Lendall, I know it! (She thinks. Collects herself. New attack.) Did you lose it?

LENDALL: What?!? No, Gayle, no!

GAYLE: Did you lose it, Lendall? 'Cause I know I gave you more than that, and I think you're pulling something on me, and this is not a good time to be pulling something on me!

LENDALL: I'm not. Pulling something on you. I wouldn't do that to you ... Just — I think — ... Gosh — ... (Not mean; just at a loss.) I think maybe you should just take what you came for, and I guess I'll see you later. (This is pretty final. He exits into the rest of the house.)

GAYLE: (Realization of the finality; calls him, weakly.) Lendall ... Lendall ... (Now Gayle is at a loss. But this is what she wants. She looks at the little bag, takes it, and is about to leave. But curiosity stops her. She sits in the chair, opens the bag, and examines what's inside.) Lendall!? What is this? What the heck is this, Lendall? This is not the love I gave you, Lendall, at least have the decency to give me back what — . Lendall, what is this?

LENDALL: (From off.) Its a ring, Gayle.

GAYLE: What?

LENDALL: (Returning.) It's a ring.

GAYLE: What? Well, what the — ? (She takes what is in the bag out of the bag.) This isn't — . This is not — ... (Realizes it's a ring box.) Oh, Lendall, this is a ring! Is this a ... ring? A ring that you give to someone you've been with for quite a long time if you want to let them know that you're ready for what comes next for people who have been together for quite a long time...?

LENDALL: Yup.

GAYLE: Oh ... (She opens the box, sees the ring.) Oh! (Beat.) But ... all the love I gave to you? Where is it?

LENDALL: It's right there, Gayle. (Referring to the ring.)

GAYLE: But —

LENDALL: It’s right there.

GAYLE: But —

LENDALL: It is. That's it! Right there! There was so much of it — you gave me so much, over the years —

GAYLE: Eleven.

LENDALL: — over the eleven years —

GAYLE: Eleven, yeah.

LENDALL: — yeah, you gave me so much ... that I didn't know what to do with it all. I had to put some in the garage, some in the shed. I asked my dad if he had any suggestions what to do with it all, and he said, "You got a ring yet?" I said, "No." And he said, "Get her one. It's time. When there's that much of that stuff comin' in, that's about the only place you can put it." (Beat.) He said it'd all fit. (I.e., in the ring. Beat.) And he was right. (Beat. They look at the ring. Then, simply:) That thing is a lot bigger than it looks ... (Beat.) So, there it is. All the love you gave me. Just not in the same ... form as when you gave it.

GAYLE: Yeah. (Beat.)

LENDALL: You still want it back?

GAYLE: Yes. I do.

LENDALL: Well, then ... take it.

GAYLE: (She takes the ring out of the box. Then, referring to all the bags of love:) Can I keep all that?

LENDALL: It's yours.

GAYLE: Thank you. (Lendall takes the ring, puts it on Gayle's finger. Music.) Lendall — ... You didn't have to get me a ring. That's not what I was asking —

LENDALL: Yes I did. It was time. And it's honorable.

GAYLE: Well ... it's very beautiful. (Beat.) Lendall — ... I'm so sorry. It's just — it's a Friday night, and I was sittin' home all by myself—we didn't even go out or anything, and I started thinkin' that that's just not right, and —

LENDALL: Shh. (Into a kiss. And a hug. After a moment — still in the hug, and nbeknownst to Lendall — Gayle can't help herself but to take a good long look at that ring. Lights fade on Gayle and Lendall hugging and swaying — two small people in love, underneath a big, spectacular, star-lit northern night sky.)
```

---

## IC-0787: The Gin Game

- Title: The Gin Game
- Author (byline): D.L. Coburn
- Work: Not specified
- Publisher: Samuel French
- Publication date as stated: 1977
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: FONSIA, WELLER, ACTRESS, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1748
- Already set (do not supply): none

### Source block (context only)

```text
Author: D.L. Coburn
ISBN: 978-0573609763
Publisher: Samuel French
Date (Month/Year): 1977
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: When two elderly people are young at heart, relationships develop quickly.

ACTOR: A simple game of gin can become a friendship.

ACTRESS: Unless . . . one of those people has an unnatural need to win.

ACTOR: To Fonsia, it’s just a game of gin;

ACTRESS: But to Weller it is obviously so much more and his reactions dredge up issues for Fonsia as well.

TOGETHER: The Gin Game by D.L. Coburn.
```

### Performance text (classify this)

```text
FONSIA: (enters, seemingly lost in thought; she starts at unexpectedly seeing Weller) (embarrassed) Oh, I . . . I didn’t think anyone was out her.

WELLER: I’m sorry I startled you. You’re rather new here, aren’t’ you?

FONSIA: Three weeks.

WELLER: It takes some adjustment.

FONSIA: How long have you been here?

WELLER: Couple of months. Of course, it’s not the first time I’ve lived in. They’re all pretty much alike.

FONSIA: I came here to Bentley because they’re supposed to have constant care.

WELLER: What’s wrong with you – if . . . if you don’t mind my asking.

FONSIA: Oh, my . . . Lord no, I don’t mind. I’ve got chronic diabetes. Is there something wrong with you? . . . I mean are you sick?

WELLER: Oh my, I should say so. I have one of the most advanced cases of old age in the history of medical science. (Pause) The mortality rate’s incredible. If you live long enough, sooner or later you end up in one of these places.

FONSIA: I guess you’re right. ‘Course, if you were rich enough . . .

WELLER: Don’t be deluded by money. I’ve seen some very wealthy people in old age homes. Lonliness – simple as that. Do you play cards?

FONSIA: Oh, it’s been years since I’ve played any cards. I used to love to play. I could sit and play rummy ‘til two o’clock in the morning. (Amused) If my mother’d ever know I was doing that, she’d a killed me. We were raised old-time Methodist and we considered card playin’ a sin.

WELLER: The only sin in card playing is drawing to an inside straight. And even that’s not a sin if you fill it. (He laughs at his own twist of logic) Did you ever play gin?

(picks up a deck of cards and begins to shuffle) By the way, I’m Weller Martin.

FONSIA: Fonsia Dorsey. Is gin and rummy the same? Seems to me they called it gin rummy.

WELLER: Here, I’ll show you. Now then . . . the first thing we do is deal the cards. Ten for me and eleven for you. (Dealing ritual) One, one, Two, two . . . .

WELLER: You think you got it now? (Fonsia nods enthusiastically) Good, then let’s play!

(They pick up their cards, arrange them in their hands and begin to play the game. Through the following dialogue, the play of the hand proceeds normally)

FONSIA: I thought this was going to be an awful day. I’m actually enjoying myself.

WELLER: Visitor’s Day! (snorts) Do you have any family?

FONSIA: Oh, my yes. Of course. I have a son almost forty-five years old . . . Larry. Then I have a sister, Hattie. I haven’t seen her in fifteen years.

WELLER: Does your son live here in town.

FONSIA: No. Ah . . . he hand his wife make their home in Denver. Do you have any children? . . . Wait a minute. I’m sorry, Weller. I think I’m sitting here with gin in my hand already. Four kings, 3 nines and the five, six and seven of spades. I’ve got the eight too. I guess I just discard that.

WELLER: (decidedly displeased at being beaten in the first hand – patronizing) That’s right. Very good. Very good, Fonsia. Forty-two points in the first game. (He gathers the cards and begins to shuffle)

FONSIA: Beginner’s luck, I guess. Oh. I was just about to ask you about your children.

WELLER: (Weller deals the cards again) One, one, two, two . . . . (continues dealing while he speaks and the card game should resume) I have three children . . . Divorced. Their mother didn’t exactly encourage a close relationship between us. She moved – she and the children – to another city. I had a business established so I couldn’t follow them. Eventually she remarried, so that was more or less the end of that.

FONSIA: I’m sorry that happened to you. Of course, that’s exactly what some men deserve. That would’ve suited the one I had just right.

WELLER: (Bitter) It doesn’t suit anyone just right. I wouldn’t wish it on him either.

FONSIA: Well, if you knew the hell I went through, you’d change your tune might fast on that! (Pause) Gin! . . . That was lucky – I got everything I needed right away.

WELLER: (disgusted look at a quick second loss as he picks up the cards and shuffles again) Does the food around here give you diarrhea?

FONSIA: Weller!

WELLER: That’s a legitimate question. (The gin game continues throughout the conversation)

FONSIA: (changing the subject) What kind of business were you in?

WELLER: Basically I told people who to run their business. I remember when I was just getting started in business, I wanted a job from this particular company. The president said, “What’s it going to cost us?” Well, I was afraid to ask for much money at that time. I though the job was worth about five hundred – but I cut it back to four. I was so nervous, I just said the word, “Four.” The president, he turned to one of the other men and said, “Does four thousand sound in line to you, Harry?” The guy said, “Yeah, that sounds about right to me.”

FONSIA: (Disbelieving) Weller, you’re making that up! Gin!

WELLER: (gathering cards to shuffle and deal again) Goddamn it. I knew you were keeping jacks. Now what’d I do that more. I gave it right to you. Talking too damned much.

FONSIA: (prim and proper) You know, I never heard my father say a curse word in his life.

WELLER: Obviously you didn’t play gin with him! (hears something from off stage) What the hell are they doing in there now? I just can’t understand this “entertainment.” Sometimes I get the idea that they feel like if they don’t have a choir up there or if they don’t have a goddamn magician up there doing trick or something – then we’re all going to drop dead right in front of their eyes. . . . I should just know while I’ve got a chance. You’re probably sitting over there with gin already.

FONSIA: Not quite (game continues in silence except for Weller)

WELLER: (draws card) Nothing (Fonsia draws and keeps it for her hand; Weller draws again) Nothing (Fonsia draws and keeps it for her hand; Weller draws) Nothing. (Fonsia draws)

FONSIA: There it is. Gin!

WELLER: (Throws his card down) I don’t believe it! Let me see that! (Fonsia displays her cards and a complete rage follows) AW! BULLSHIT! BULLSHIT! (Weller stops away then stops back to look at the cards again). AW! JESUS CHRIST. (He sweeps the cards wildly into the air and Fiona recoils.)

FONSIA: Weller! ***********Scene break *************** TRANSITION

ACTRESS: A few days pass until Weller once again meets Fonsia on the sun porch.

WELLER: (Sheepishly approaching Fonsia) I’ll get right to the point, Fonsia . . I owe you an apology

FONSIA: Yes you do! (Weller holds up a deck of cards and begins to shuffle a querulous expression on his face) Now, Weller, I’m NOT going to play any gin with you.

WELLER: Oh come on, Fonsie, for God’s sake. . . . All right, don’t play. Go on back in there with all those glassy-eyed old bastards.

FONSIA: God, you’re cynical. It’s just the mercy of God that we’re able to get around a little better than they are. They’re just sick, that’s all.

WELLER: They’re not half as sick as the ones who put them here. And they’re not a third as sick as this bunch that’s supposed to be taking care of them.

FONSIA: You’ve got a horrible temper . . . and a sarcastic streak.

WELLER: (Defensively, cutting her off) If I were you, I wouldn’t be talking about anybody’s else’s shortcomings.

FONSIA: What’s that supposed to mean?

WELLER: Well, neither one of us is winning any popularity contest out here on visitor’s day.

FONSIA: Oh. I see. No one visits me so I’m an evil person?

WELLER: Why doesn’t your son visit you?

FONSIA: I think I should go in.

WELLER: All right, goddamn it, go ahead. I don’t see how you can stand it in there. . The same damn empty look, face after face. You ought to see them on the days when the bed linens are changed. All lined up in those wheelchairs, all up and down the halls . . . like rows of wrinkled pumpkin heads.

FONSIA: Maybe we could play a few hands . . . You’re just going to pester me ‘til I play anyway. (Weller grins and the card game begins) Now if I win, don’t you shout at me.

WELLER: You play your best, damn it! I won’t have you trying to lose . . . just to appease poor Weller. I’m one of the best gin players you’ll ever see and I sure as hell don’t need any help from you. Play your cards, damn it! (Pause – Weller continues in calmer affected tone). I’m sorry. Please play your cards.

FONSIA: Just play your cards, Weller.

WELLER: (Mimicking) Just play your cards, Weller. Well, aren’t we getting tough.

FONSIA: Not tough. Just tired. Very tired.

WELLER: Aw for Christ’s sake, come on. (Pause) Goddamn it!

FONSIA: Every other breath you draw has to be a curse word doesn’t it?

WELLER: (Pause) Shit! (Fonsia draws a card, puts it in her hand, then, saying nothing and without discarding, she displays her hand face up on the table. She doesn’t look up. Weller scrutinizes the cards then shouts) SAY IT!!! (Fonsia says nothing. Weller paces angrily away then turns on her and in a shouting, accusatory tone, continues) YOU’VE GOT IT. GODDAMN IT – SAY IT!!! (Still no response from Fonsia; Weller marches over to her and shouts directly in her face) SAY IT!

FONSIA: (barely audible) Gin.

WELLER: CHRIST, YOU CAN SAY IT LOUDER THAN THAT! I CAN HARDLY EVEN HEAR YOU!

FONSIA: (Shouting to match Weller’s tone) GIN—GODDAMN IT!!! GIN!!! (long pause while they both catch their breaths) It was a game, Weller. You lost – it’s over – so forget it.

WELLER: Well . . . suppose I want to play you again.

FONSIA: Nothing doing! The minute you lost, it’d be the same thing all over again. I may be old, but I’m not crazy. I’ve never seen a man get so . . . so wild . . . over a game of cards in my life. It’s not natural, Weller, there’s something wrong.

WELLER: I know all about how you think something’s wrong with me. They called me down the office last Tuesday and said they were thinking about having a psychiatrist come out here and talk to me. Do you know what they could do if he says there’s something wrong with my mind? They could have me committed to the state mental hospital. The very fact that you complained makes me a troublemaker.

FONSIA: You could need help and not know it. All I was trying to do was to help you.

Maybe I shouldn’t have said anything. . . NO, if I didn’t say anything, the next thing you know they’d find one of us out here on the floor.

WELLER: What do you think I’m going to do? Hit you over the head? Good God, you make harsh judgments, Fonsia. I’m a potential murderer? I’m crazy. I’m vulgar. According to you I’m a hopeless sinner for taking the Lord’s name all the time. You know what wrong with most people in the world? . . . they’ve got a mother who’s just like you.

FONSIA: That’s the most insulting remark I’ve ever heard in my life.

WELLER: I know why Larry doesn’t visit you. It doesn’t have a damn thing to do with Denver . . . or distance . . . or job. I know what it is now. You’ve made him feel like the lowest piece of crap on earth for so long he can’t stand the sight of you. He hates you.

FONSIA: THAT’S NOT TRUE! AND I WON’T HAVE YOU TALK TO ME LIKE THAT!!!

WELLER: He’s never done anything right, has he? He’s never done a thing on this earth to please you, has he.

FONSIA: STOP IT, WELLER. I’M WARNING YOU.

WELLER: He doesn’t even live in Denver, does he? Your son lives right her in town and you know it!

FONSIA: He does not hate me! He doesn’t hate me!

WELLER: Then why doesn’t he visit you? Why does he totally ignore his own mother?

FONSIA: How did you know he lives here?

WELLER: I didn’t I was guessing.

FONSIA: Guessing! YOU BASTARD. YOU BASTARD (Fonsia weeps hysterically)

WELLER: Fonsie. Fonsie. Fonsie. I’m sorry. I’m sorry. .

FONSIA: I know who he takes after. His father was as rotten as they come. I always hoped Larry’d be different. Sometimes I think he does hate me . . . I don’t know.

WELLER: Just relax yourself. You’re only doing yourself harm. What you need is to get your mind off him. (Gathers up the cards and begins to shuffle) Come on, I’ll play you a hand of gin. (Cajoling) You can’t tell me you didn’t enjoy beating me game after game, watching me get angrier and angrier. – We’ll play one hand . . .

FONSIA: Deal.

WELLER: (Dealing) One, one, Two, two, Three, three

TOGETHER: Four, four, Five, five

WELLER: I’m going to beat you this hand . . . . By God, I’m going to beat you.
```

---

## IC-0788: Girl Made of Stars

- Title: Girl Made of Stars
- Author (byline): Ashley Herring Blake
- Work: Not specified
- Publisher: HMH Books for Young Readers
- Publication date as stated: May 2018
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: OWEN, MARA, MOM, MR. KNOLL, HANNAH
- Teaser before the introduction: Yes
- Spoken words (computed): 1497
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ashley Herring Blake
ISBN: 978-1328778239
Publisher: HMH Books for Young Readers
Date (Month/Year): May 2018
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: Girl Made of Stars by Ashley Herring Blake
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Roles: Actress – Mara (Owen’s Twin), Mom and Hannah (Owen’s girlfriend) Actor – Owen (Mara’s Twin) and Mr. Knoll (Mara’s 8th grade math teacher)

OWEN: (Pg 2) Once upon a time . . .

MARA: . . . a brother and sister lived with the stars. They were happy and had wild adventures exploring the sky . . . (to audience) (Pg 61) For as long as I could remember, the storis were a thing with our family. The twins, [Owen and Mara], Gemini soaring through the sky.

OWEN: There were even years when Mom put Happy Birthday, Gemini on our cake, little yellow icing stars dotting the chocolate.

MARA: Time passed, we got older and too big and cool to snuggle with Mom for bedtime tales, but we never let go of those stories.

OWEN: They were – are—part of our blood. We were the star twins.

MARA: Owen and I took them over, told new stories as a way to remember we weren’t alone. (Pg 195) But there’s a girl inside of me. Tired. Scared. Lonely. Angry. Devastated. Wounded. She doesn’t have a brother.

OWEN: (Pg 30-31) . . . swear to god, Mom. This is . . . I don’t get it.

MOM: He said the state attorney might press charges, Owen. And you’re telling me you have no idea why?

OWEN: No! I swear. I’d had a few drinks, yeah, but (he gasps for breath)

MOM: Owen, are you sure you asked . . .

OWEN: She wanted to. I swear to god she wanted to. (his voice raises to a fever pitch) I’d never do that. I didn’t. (Pg 33) We had a fight, that’s all.

MOM: (Pg 32) It’s a misunderstanding. Apparently . . . Hannah feels like . . . she thinks . . . Hannah feels that [you] took advantage of her at the lake.

MARA: (to audience) (Pg 97) The possibility that Hannah is telling the truth never entered my mother’s mind. (Pg 32) Took . . . advantage? We all know that’s not the right word. The word we should be using lunges into my throat. I shove the word back down. There’s no way I can say it. There’s no way it’s really the right word. (to Owen) Owen, did you . . . force yourself on her?

OWEN: No! Hell no. You know I would never do that. We had a fight, that’s all. (raking both hands through his hair. He leaves them there, resting his forehead in his palms)

MARA: I know you wouldn’t. I know that. So why would she say you did? ***** flashback*****

MR. KNOLL: (Pg 19) Stupid little bitch. Stupid little bitch.

MARA: (to herself) Breath in, two three, four . . . breathe out, two, three, four . . . Calm down, Mara . . . (She squeezes her eyes shut and tries to control her breathing and ignore the words knocking around in her head)

MR. KNOLL: Stupid little bitch. ***********

MARA: (Pg 93-95) Owen, what happened? I’m listening . . .

OWEN: (throughout his story, Owen keeps messing with his lip. His voice is the perfect mix of embarrassed and confident) We were on the trail . . . Anyway, we sat down and started . . . well, you know, kissing and stuff, and then we . . . you know. (Mara gives him a look) We had sex, all right? Not like you didn’t know what I was saying. Then . . . well she got really pissed. She leaned on her wrist weird or something and she sort of freaked out about it. I told her I was sorry, but she just kept at me. You know how she gets. And honestly, I’m a little sick of her drama.

MARA: (to audience) But as I listen to him, watch him, it’s as if my skin is peeling away, struggling to reveal this new girl I’m not sure I want to be. It’s as though the stars are breaking apart. I know my brother is lying.

MR. KNOLL: (Pg 19) Stupid little bitch ***********

HANNAH: (Pg 122-124) (her eyes are red-rimmed from crying and her wrist is wrapped in an bandage – she speaks to the audience) I’m so sorry. . . maybe if I . . . He was so drunk. Everything was fine. We got a drink and danced a little, but he kept going back for more of that punch until I finally convinced him to go on a walk. (She swallows and licks her lips) So we started making out, and the next thing I know, we’re lying on a bench and it was about to happen and I freaked out. I kept imagining someone walking by. I told him to stop . . . I told him to stop. . . . I’m sorry, I’m sorry, I’m sorry . . . Maybe if I’d said no louder. Or . . . I don’t know. I loved him. I trusted him. I never thought he would . . . I don’t know if I would’ve even told anyone if Charlie hadn’t found me. . . This is such a mess. (Pg 203) Everyone thinks that when someone gets ra . . (swallows hard and takes a deep breath) That when someone gets raped, it’s this quick, spontaneous thing, always violent with bruises and black eyes. But I guess that’s not always the case, you know . . . [It’s just] awkward teenage sex.

OWEN: (Pg 195) The state attorney called today. They’re not pressing charges! ******

MARA: (Pg 97) This. This is why I never said anything. Because no one ever believes the girl.

MR. KNOLL: (Pg 19) Stupid little bitch

MARA: (Pg 125) [What about] my own silence, my own fear, my own story? Mr. Knoll and his smug smile, the way he just stood there, totally invulnerable. He held all the power. He could call me a stupid little bitch, and I couldn’t do one damn thing about it . . . (Pg 145) I am scared all the time. For the past three years, I have a nightmare at least once a week about losing my voice, Mr. Knoll’s fingers ripping the vocal cords right out of my throat. ********* flashback to 8th grade – 3 years prior **********

(Pg 185 – 191) (bell rings to signal the end of class. Mara grabs her backpack and starts to leave the classroom)

MR. KNOLL: Mara? I need to speak with you for a moment. (He ushers the rest of the class out the door, closes the door behind the last student and moves to his desk. He rifles through some papers, then looks at Mara with a little smile on his face) So . . . Mara

MARA: Is . . . is everything okay?

MR. KNOLL: (sighs) I’m afraid not. (he picks up the papers and holds them toward Mara) Tell me about these.

MARA: (to audience) My last three tests, three As circled in red next to my name. (To Mr. Knoll) What about them?

MR. KNOLL: (sighing again) A student came to me earlier today and said you copied off their tests. (shaking his head) This is fixable. I won’t fail you if you’re willing to put in a little work.

MARA: Fail me? But I didn’t. I swear I didn’t cheat.

MR. KNOLL: (shaking his head, his eyes traveling up Mara’s legs to her torso) It’s really simple, Mara. I’m disappointed in you, but I know you’re better than this. You’ve been distracted, too focused on summer and high school. . . . [maybe] you’d benefit from repeating the course. (he brushes her hair back from her face) Are you willing to work with me on this?

MARA: (pulls back) No! I mean, yes, I’ll work hard. What do I need to do?

MR. KNOLL: (inhaling slowly through his nose) Nothing too difficult. . . come here. (Mara stakes a step closer) Good girl. (he reaches for his belt buckles and undoes it) I think we can fix this right now, don’t you, Mara?

MARA: What are you doing? (she closes her eyes)

MR. KNOLL: (suddenly stern) Don’t do that. Don’t be coy. (He takes Mara’s hand and places it on his erection, he moves her hand, forcing her fingers to do what he wants, then speaks in a softer voice). See? (breathing heavily) We’re just having fun, right? (He puts his hand on the back of Mara’s neck and pulls her closer) Soon you can go and have the summer that you planned with your family. You’ wouldn’t want to ruin that, would you? (Mara shakes her head as tears stream down her face – she stares at the wall.) Good girl. (Mr. Knoll smiles)

MARA: (Throws herself violently backward, she trips over her bookbag and scramble to her feet)

MR. KNOLL: You’re a stupid little bitch! (Mara rushes to the door, manages to get it open and races down the hall) Stupid little bitch! ********

MARA: (Pg 230) That girl is still voiceless, still scared. (she presses both hands to her forehead trying to calm down) I know he still works [at the middle school] He teaches pre-algebra and coaches the boys’ basketball team. . . (Pg 231-232) He’s a scumbag and a child molester. What he did is black and white, but dealing with it isn’t. He was awarded Teacher of the Year that spring! It never even entered my parents’ minds that he might be lying about my cheating. Why the hell would the teacher of the y ear lie about a stupid little girl’s tests? No one would believe me. They wouldn’t have then. They sure as hell won’t now.

MR. KNOLL: (Pg 19) Stupid little bitch *************

MARA: (to audience) (Pg 270) I’m not sure I ever will recover from what Mr. Knoll did. It’s changed me forever, but changed doesn’t have to mean broken . . . (Pg 257) (whispering) I’m not stupid. (Pg 254) You didn’t let it happen, Hannah. You trusted Owen. There’s a difference. And with me . . . I didn’t let him either. He just took. (long pause as she collects herself) (Pg 270-271) My brother’s and my connection has been altered, never broken but twisted into something I never expected. Never wanted. I have to figure out how to live with that. How to be his twin sister and hate what he did all at once. *********** Owen finds Mara sitting on the front porch alone. He sits beside her and tries to reconnect.

OWEN: (Pg 260- 262) Once upon a time . . . A brother and a sister lived with the stars. They were happy and had wild adventures exploring the sky. But lately, Sister Twin was super sad and she felt lonely. So Brother twin decided to collect a bunch of stars and make his sister a crown, and a necklace and a bracelet and a belt and shoes. She was made of stars!

MARA: But if I’m made of stars, then where am I? Where’s the real me?

OWEN: See, that’s the thing. They thought the stars were sticking to her, but really all the loneliness and sadness were falling off. The stars were underneath all the bad stuff. She just had to remember who she was underneath everything.

MARA: (Pg 282-283) Once upon a time . . the brother broke his sister’s heart.

OWEN: I didn’t . . .

MARA: Don’t. Don’t you dare!

OWEN: I want things to go back to normal.

MARA: There is no normal, Owen. Not anymore. . There’s only making it something other than this.

OWEN: How?

MARA: Tell the truth.

OWEN: (offended) I did.

MARA: Don’t you get i? You raped a girl, Owen. You took her choices from her. . . her body, her power. You took her ability to trust, her ability to be with a guy, maybe for years. Do you see how strong she’s been at school, despite all that? You’re not going to ruin her. I won’t let you. She won’t let you. (tears run down Mara’s cheeks) (Pg 286) (to audience) I’m not a girl made of stars. I’m just me, just a girl, just Mara. (Long pause, then Mara knocks softly at a door) (Pg 289) Mom . . . Dad . . . I need to tell you guys something. (to audience) For Hannah. For all the girls whose names I’ll never know. . . For me. (Pause) (Pg 294) There is life after abuse. It’s not the same one we had before. But it is still ours. Despite a system and a culture that is perpetually against us, that lets our oppressors go free, that disbelieves our words, there is hope. We are worth the telling. We are worth the fight.
```

---

## IC-0789: Golden Boy

- Title: Golden Boy
- Author (byline): Clifford Odets
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JOE, LORNA, ACTRESS, ACTOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1871
- Already set (do not supply): none

### Source block (context only)

```text
Author: Clifford Odets
ISBN: 978-0822204565
Publisher: Dramatists Play Service
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: (Throughout the introduction, we see Joe in the background, alternating between shadow boxing and pantomiming the playing of a violin) That’s Joe. He’s the Golden Boy . . . struggling to choose between his violin and a pair of boxing gloves. Boxing could be his ticket to riches, fame and recognition – his path out of the Great Depression to the American Dream. But at what personal cost? His rise to stardom is dimmed by his sub-conscious need to protect his hands. He wins on points, not knockouts. He’s just not aggressive enough to be a star . . .

And then Lorna, his manager’s mistress, intervenes. Her assigned goal: to convince Joe to do what he needs to do to become a prize-fighter. Her personal goal: to explore her growing feelings for a young, confused man. Golden Boy by Clifford Odets
```

### Performance text (classify this)

```text
Characters: Joe: a young Italian man born to immigrant parents in New York Lorna: the mistress of Tom Moony, Joe’s manager

JOE: (page 24-25) I have to tell you— I don't like myself, past, present and future. You don't know what it means to sit around here and watch the months go ticking by! Do you think that's a life for a boy my age? . . . . Nobody takes me serious here! I want to do what I want. I proved it tonight. I'm good — I went out to earn some money and I earned! I had a professional fight tonight — maybe I'll have some more . . . . Tomorrow's my birthday! I’ll change my life! Who says I'm married to music? I’ll take a vacation — the notes won't run away!

LORNA: (page 34-39) Success and fame! Or just a lousy living. You're lucky you won't have to worry about those things. . . .

JOE: Won't I? . . . Where's Mr. Moody tonight?

LORNA: He goes up to see his kid on Tuesday nights. It's a sick kid, a girl. His wife leaves it at her mother's house. (changing the topic) [Your trainer] says you're going far in the fighting game.

JOE: Music means more to me. Playing music . . . that's like saying, "I am man. I belong here. How do you do, World— good evening!" When I play music I'm not afraid of people and what they say. There's no war in music. I might give up fighting as a bad job. I'm not over-convinced it's what I want. I can do other things. . . . You have to be what you are—!

LORNA: Fight! See what happens— who says you have to be one thing?

JOE: My nature isn't fighting!

LORNA: Joe, listen: be a fighter! Show the world! If you made your fame and fortune— and you can— you'd be anything you want. Do it! Bang your way to the lightweight crown. . . You're too inside yourself. That's right— "me, myself, and I." Why not come out and see the world?

JOE: Does it seem that way? (a beat while Joe considers his options . . . ultimately the lure of boxing wins out) If you're vitally interested in my future, prove it! Get me some fights— fights with contenders, not with dumb-bunny club fighters. And how about some mention in the press? Twenty-six bouts — no one knows I'm alive. Match me up against real talent.

LORNA: You're a miserable creature. You'll take fame so people won't laugh or scorn your face. You'd give your soul for those things. But every time you turn your back [on your music] your little soul kicks you in the teeth. It don't give in so easy.

JOE: (in retaliation for Lorna’s insight – angrily) [Oh, yeah?} This is the anatomy of Lorna Moon: she's a lost baby. She doesn't know what's right or wrong. She's a miserable creature who never knew what to pick. But she'd never admit it. And I'll tell you why you picked Moody!

LORNA: You don't know what you're talking about.

JOE: Go home, Lorna. If you stay, I'll know something about you. . . . Now's your chance— go home!

LORNA: Tom loves me.

JOE: (after a long silence, looking ahead – it’s clear that Joe has feelings for Lorna and that she is battling her feelings for him as well. Joe changes the subject again) I'm going to buy a car. I saw it in the paper, but it costs too much— fourteen thousand. If I found one second hand—

LORNA: And if you had the cash— [you would] if you'd go in and really fight!

JOE: (in a sudden burst) Tell your Mr. Moody I'll dazzle the eyes out of his head!

LORNA: You mean it?

JOE: (looking out ahead) Those cars are poison in my blood. When you sit in a car and speed you're looking down at the world. Speed, speed, everything is speed—

(standing up suddenly and miming a quick uppercut) I'll walk you back to your house— your hotel, I mean. (Lorna stands. Joe continues.) When you're lying in his arms tonight, tell him, for me, that the next world's champ is feeding in his stable.

TRANSITION

ACTRESS: (during this transition, we see Joe in the background massaging his hand in in despair as he realizes that he will never again be able to play the violin) Despite her growing feelings for Joe, Lorna feels unable to break it off with Moody. Feeling as though he has sold his soul to the devil and realizing that Lorna may be beyond his reach . . . Joe no longer holds back in the ring. Months pass and Joe becomes more and more aggressive . . . violent . . . successful. But with each victory he loses a little of himself . . . When one bout results in a broken hand, he seeks the solace of Lorna once again.

JOE: (page 53 – 57) Some nights I wake up— my heart's beating a mile a minute! Before I open my eyes I know what it is— the feeling that someone's standing at my bed. Then I open my eyes . . . it's gone— ran away!

LORNA: Maybe it's that old fiddle of yours. Do you ever think of it any more— music?

JOE: What're you trying to remind me of? A kid with a Buster Brown collar and a violin case tucked under his arm? Does that sound appetizing to you?

LORNA: Not when you say it that way. You said it different once. . . . What's on [your mind]?

JOE: (simply) You. . . . You're real for me— the way music was real.

LORNA: You've got your car, your career— what do you want with me?

JOE: I develop the ability to knock down anyone my weight. But what point have I made? Don't you think I know that?. . . . I'm not sure I like it.

LORNA: Moody's against that car of yours.

JOE: I'm against Moody, so we're even. He's a manager! He treats me like a possession! I'm just a little silver mine for him— he bangs me around with a shovel!

LORNA: He's helped you—

JOE: No, [my trainer’s] helped me. Why don't you give him up? Why don't you belong to me? Why don't you teach me love? . . . Or am I being a fool?

LORNA: You're not a fool, Joe.

JOE: I want you to be my family, my life— Why don't you do it, Lorna, why?

LORNA: He loves me.

JOE: I love you!

LORNA: (treading delicately) I can't give him anguish. I . . . I know what it's like. He's poor compared to you. You're alive, you've got yourself— I can't feel sorry for you!

JOE: But you don't love him! You feel close to me. But you're afraid—

LORNA: Of what?

JOE: To take a chance! I feel it all the time— you're half dead, and you don't know it!

LORNA: (evasively) Why start what we can't finish?

JOE: (fiercely) Oh, Lorna, deep as my voice will reach— listen! Why can't you leave him? Why?

LORNA: Because he needs me and you don't—

JOE: That's not true!

LORNA: Because he's a desperate guy who always starts out with two strikes against him. Because he's a kid at forty-two and you're a man at twenty-two.

JOE: You're sorry for him? What did he ever do for you?

LORNA: (with sudden verve) Would you like to know? He loved me in a world of enemies . . . and I loved him for that. He picked me up in Friskin's hotel on 39th Street. I was nine weeks behind in rent. I hadn't hit the gutter yet, but I was near. He washed my face and combed my hair. He stiffened the space between my shoulder blades. Misery reached out to misery—

JOE: And now you're dead.

LORNA: (lashing out) I don't know what the hell you're talking about!

JOE: Yes, you do. . . .

LORNA: (withdrawing - There is silence) You make me feel too human, Joe. All I want is peace and quiet, not love. I'm a tired, Joe, and I don't mind being what you call "half dead." In fact it's what I like. (Her voice mounting higher - now half crying.) Joe. I beg you . . . let me alone. . . . (She cries softly. Joe reaches out and takes her hand; he gives her a handkerchief which she uses. Lorna, finally.) That's the third time I cried in my life. . . .

JOE: Now I know you love me. . . I'll tell Moody.

LORNA: Not yet. Maybe he'd kill you if he knew.

JOE: Maybe.

LORNA: I'll tell him. . . .

JOE: When?

LORNA: Not tonight. . . He went up there tonight with six hundred bucks to bribe her into divorce. (sadly) He's a good guy, neat all over— sweet. I'll tell him tomorrow.

JOE: (standing and facing her) Lorna, when I talk to you . . . something moves in my heart.

LORNA: But how do I know you love me? How do I know it's true? You’ll get to be the champ. They'll all want you, all the girls! I feel like a tramp. I've felt like a tramp for years. (pg 61) It has to end. . . . (it’s unclear whether Lorna is referring to her relationship with Moody or with Joe)

TRANSITION

ACTOR: Time again passes and Lorna begins to avoid Joe . . . he soon discovers why. Moody has divorced his wife and he and Lorna have plans to be married . . . soon. After months of silence and outright avoidance, Joe’s path crosses Lorna’s once again, in the hallway of the training center on the eve of his largest fight to date – a battle against the Champion, the “Baltimore Chocolate Drop.”

(On his way to the ring, Joe sees Lorna in the hallway. Her back is turned and it is clear that the desire to speak to her is at war with his desire to turn and walk away . . . his need to speak wins out)

JOE: (pg 79 – 80) I hear you're making the leap tomorrow. • • •

LORNA: Sunday . . .

JOE: Sunday. (Intense silence - finally) Congratulations. . . .

LORNA: (without turning) Thanks. . . . (In a sudden irresistible surge Joe lashes out)

JOE: When I speak to you, look at me!

LORNA: What would you like to say? (They stand face to face, straining.)

JOE: (finally) Marry anyone you like!

LORNA: Thanks for permission!

JOE: Queen Lorna, the tramp of Newark!

LORNA: You haven't spoken to me for months. Why break your silence?

JOE: You're a historical character for me— dead and buried!

LORNA: Then everything's simple; go about your business.

JOE: Moody's right for you— perfect— the mating of zero and zero!

LORNA: I'm not sorry to marry Tom—

JOE: (scornfully) That's from the etiquette book— page twelve: "When you marry a man say you like it!"

LORNA: I know I could do worse when I look at you. When did you look in the mirror last? Getting to be a killer! You're not the boy I cared about, not you. You murdered that boy with the generous face- God knows where you hid the bodyl I don't know you.

TRANSITION

ACTOR: Disoriented by their argument, Joe goes into the ring and can’t stay focused.

ACTRESS: He is down until the eighth round but pulls through with a victory at the last moment.

ACTOR: Before the celebration gets underway Joe is alerted that his final blow to the “Chocolate Drop” has killed the boxer.

(In the training room, Joe is stunned by his own violence – he paces frantically muttering to himself – Lorna enters)

LORNA: (pg 87 – 88) Joe . . . it wasn't your fault.

JOE: That's right— it wasn't my fault! I wouldn't want to do that, would I? Everybody knows I wouldn't want to kill a man. Lorna, you know it!

LORNA: Of course!

JOE: But I did it! That's the thing-I did it! What will my father say when he hears I murdered a man? Lorna, I see what I did. I murdered myself, too! I've been running around in circles. That's the truth. Yes, I was a real sparrow, and I wanted to be a fake eagle! But now I'm hung up by my fingertips— I'm no good!

LORNA: (in a sudden burst, going to Joe): Joe . . . You wanted to conquer the world— But it's not the kings and dictators who do it— it's that kid in the park—

JOE: Yes, that boy who might have said, "I have myself; I am what I want to be!"

LORNA: And now, tonight, here, this minute— [you found] yourself again— that's what makes you a champ. Don't you see that? Give up the fighting business!

JOE: Tonight!

LORNA: Yes, and go back to your music—

JOE: But my hands are ruined. I’ll never play again! What's left, Lorna? Half a man, nothing, useless . . .

LORNA: No, we're left! Two together! We have each other! (quietly) I love you. Somewhere there must be happy boys and girls who can teach us the way of life! Well find some city where poverty's no shame— where music is no crime!— where there's no war in the streets— where a man is glad to be himself, to live and make his woman herself!

JOE: No more fighting, but where do we go?

LORNA: Tonight? Joe, we ride in your car. We speed through the night, across the park, over the Triboro Bridge—

JOE: (taking Lorna's arms in his trembling hands) Ride! That's it, we ride— clear my head. We'll drive through the night. When you mow down the night with headlights, nobody gets you! You're on top of the world then (long beat) [and] nobody laughs!
```

---

## IC-0790: Goldfish Have No Memory

- Title: Goldfish Have No Memory
- Author (byline): Pauline David-Sax
- Work: Not specified
- Publisher: New Play Exchange (Must register for an account to access the original script)
- Publication date as stated: Aug 2021
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NOTES FROM THE PLAYWRIGHT, ERIC, ERIC/VOICE OVER, AVA, AVA-22
- Teaser before the introduction: Yes
- Spoken words (computed): 1568
- Already set (do not supply): none

### Source block (context only)

```text
Author: Pauline David-Sax
ISBN: N/A
Publisher: New Play Exchange (Must register for an account to access the original script)
Date (Month/Year): Aug 2021
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: When Eric’s twin sister, Ava, is killed in by a drunk driver, he concocts a plan to bring her back in the form of an AI human robot.

ACTOR: Sounds like something out of a movie, right?

ACTRESS: But technological advancements are already in place. * In 2016 Hanson Robotics created a humanoid robot named Sophia.

ACTOR: Boasting the ability to mimic facial expressions, hold human-like conversations and recognize human gestures, today Sophia is a global icon of artificial intelligence.

ACTRESS: In fact, she was granted Saudi Arabian citizenship in 2017. But this story – The story of Ava-22 – is a bit more personal. Can AI help us cope with the grief of losing someone?

ACTOR: Can technology truly capture the complexities of human emotion and identity?

TOGETHER: Goldfish Have No Memory by Pauline David-Sax
```

### Performance text (classify this)

```text
NOTES FROM THE PLAYWRIGHT: 1. AVA and AVA-22 are to be played by the same actor and should be indistinguishable in appearance and inflection/intonation. AVA-22 should not be played robotically. 2. GLITCH indicates a disturbance. In the BEFORE scenes this indicates a seizure. In the AFTER scenes this indicates a computer malfunction. All glitches should sound identical. During a glitch, the actor playing AVA should freeze. *****

ERIC: (Pg 4 – AFTER) (talking to an unseen therapist) Did you know every day 29 people in the United States die as the result of car crashes involving a drunk driver? I mean, it's an average, but still. It's a crazy number of people. Over ten thousand a year. And one of them was her. All those years of worrying about her and then a freak accident-- there's so much she didn't get to do. She should have gotten more time. She deserved to have more time.

ERIC/VOICE OVER: (Pg 5-7 – BEFORE) (as Ava silently reads) Essay Question #2: Recount a time when you faced a challenge, setback, or failure. What did you learn from the experience?

AVA: (clears throat then composes out loud) We've always had three goldfish. Bagels: the brownest one. Lox: mostly orange. Cream Cheese: mostly white. They say goldfish are a good starter pet for a kid. Learn how to keep a creature alive. One that no one cares much about. Goldfish are basically disposable pets. (GLITCH) I was determined to prove to my parents that I was responsible enough for a dog. Every time I begged for a dog my parents said . . .

ERIC: (as father) Let's see how well you take care of the fish first.

AVA: So, imagine my horror when I woke up three days before my ninth birthday to see Lox floating belly-up at the top of the tank. (GLITCH) With just 72 hours separating me from the puppy of my dreams, I panicked. I ran down the hall to find my twin brother, Eric.

ERIC: (Pg 8 - AFTER) Ava.

AVA: (Pg 7) He snuck out to the pet store where he bought me a replacement fish. We both watched breathlessly as Bagels and Cream Cheese swam circles around their new tank mate, but they seemed completely unperturbed by the switch. (GLITCH) It was as though, as far as they were concerned, new-Lox was just the logical extension of old-Lox. Life goes on. (GLITCH) As it turns out, I never did get that puppy. Mom said "Maybe next year" and by then . . . a lot had changed. But what I did get was the secret to immortality, as taught to me by goldfish. (closes eyes, lowers head) *****AFTER*****

ERIC: (Pg 8 - AFTER) Ava, can you hear me? (presses keys on his laptop. Slowly, deliberately, AVA- 22 opens her eyes. She looks one way, then another, until she locks eyes with ERIC)

AVA-22: Maybe next year. (GLITCH) Maybe next year. (GLITCH) Maybe next year . . .

ERIC: (Pg 20) No--! Not again--! Ugh-- (Eric presses keys on his laptop. Sound of AVA-22 turning off. AVA-22 stops talking. She falls silent, closing her eyes) (Pg 13) So, how do we preserve the individualistic elements of the subject's speech--both what they choose to talk about and how they choose to express themselves? (Pg 25-26) It's all based on data from social media posts, texts, emails--plus analog sources, like journal entries and creative writing which have been digitized. Technically, what I've created is an "it"--a machine. It's built of metal, plastic, silicone . . . But Ava-22 processes language and interacts with people. She decides what she wants to say. I'm just helping her refine it. And she's learning. (presses keys on his laptop. Sound of AVA-22 turning on)

AVA-22: (Pg 31) (raises her head and opens her eyes) Good morning, Eric.

ERIC: (pleased) You recognize me.

AVA-22: You’re my brother. My fraternal twin. (accessing data) (Pg 15) Twins. A report by Ava S., class 402. (Pg 19) We don't have the same color hair and we're not the same height and we don't like most of the same things. He is really into math and computers and geeky stuff like that, and I want to be an explorer like Jeanne Baret, who was the first woman to circumnavigate the globe.

ERIC: (Pg 31) Ava, look over here (AVA-22 looks at the fish tank) Do you recognize them?

AVA-22: We always had three goldfish. Bagels. Lox. Cream Cheese.

ERIC: Yes! Do you remember? You used to make up all these adventures for them— *****Flashback to Before*****

(AVA is sitting in front of the fish tank, watching the fish. She pulls out a magazine, opens up to a photo and places it against one side of the fish tank)

ERIC: (Pg 9-11) (enters) What are you doing?

AVA: Showing them pictures. I feel bad for them -- swimming around in the same tank all day.

ERIC: You could get a dozen plastic castles; swap them out each day for a new change of scene. (to goldfish) Whatd'ya think, fishies? Sound good?

AVA: (pretending to be one of the fish) How do you know we even like castles? We're different! We like ... mountains! And ... valleys! And ... (GLITCH)

ERIC: (looks at the photograph AVA had been holding up to the tank) ... pyramids!

AVA: (still in character) We love (GLITCH) pyramids!

ERIC: Ava. Did you just . . .

AVA: What? (shrugs) Sometimes I can guess by what I've missed. Like suddenly everyone's laughing but I didn't hear the joke.

ERIC: Is that why you haven't been eating lunch in the cafeteria? Maybe if you just explained--

AVA: So I can be the weirdo freak? No thanks. (GLITCH)

ERIC: (Pg 23) (gestures to AVA's magazine) Another adventure? (flips pages) Where to?

AVA: . . . the Atacama Desert in Chile!

ERIC: Weird place for a goldfish adventure.

AVA: They're going to find one of the Chinchorro mummies.

ERIC: Cream Cheese is gonna freak out.

AVA: Yeah! (Pg 21-22) (she makes up the story) "The three adventurers careened across the sand. As usual, Lox was driving, Bagels had her head buried in a guide book, and Cream Cheese was complaining about the sun. All of a sudden, there was a bump, and Lox slammed on the brakes. 'What was that?' she exclaimed . . . (GLITCH)

ERIC: Hey. We're about to leave. You should come.

AVA: Um, I can't skate, remember? (mimicking her mother) "It's not worth the risk, Ava. What if you have an episode while you're skating and fall down and break something?"

ERIC: Okay. Well ... have fun.

AVA: (softly) You too. (back to her story) 'I think you hit something,' said Cream Cheese." *****Scene 2 – Before*****

AVA: (Pg 27-29) (writing furiously in a notebook) And I said--NO, you CANNOT be one of the chaperones, it is TOO EMBARRASSING, no one else's MOM is going, that's NOT how the eighth grade CAMPING TRIP goes, it's supposed to be BONDING for the KIDS and the TEACHERS and it will totally RUIN it if someone's--by which I mean MY--MOTHER is there!!!!! And she said WHAT IF?? and I said ENOUGH WHAT IFs!! I just want to do NORMAL THINGS like a NORMAL KID and she said MAYBE NEXT YEAR and I said WHEN IS THIS NEXT YEAR that NEVER, EVER comes??? (GLITCH) I guess I'm not going camping after all. (knock at the door) (testily) What?

ERIC: It's me. Can I come in? (AVA hastily stows away her journal) You okay?

AVA: I mean, my brain's all glitchy, and I'll never get to do anything fun, but sure. Great. Terrific. It's fine. I didn't want to go anyway. (GLITCH)

ERIC: Did you hear me? I said ... what if we were in the same group? I could keep an eye on you--

AVA: I'm not going to have my brother babysitting me! And besides, what about at night? (imitating her mother) "What if you have to go to the bathroom in the middle of the night and you leave your tent and have a seizure, and no one sees and you're lying there on the ground and a bear comes and eats you?" (in her own voice) It's fine. I'm not going! I mean, my God, Eric, go live your own life and stop worrying about mine! ***** End of Flashback - AFTER*****

(Pg 33) (AVA-22 and ERIC are still at the fishtank)

AVA-22: (pointing to one of the fish) That's not Cream Cheese.

ERIC: Yes, look: that's Bagels, that's Lox, and this one is Cream Cheese--

AVA-22: New-Cream Cheese.

ERIC: I mean . . . okay, sure. But he looks just the same, doesn't he? (Pg 52) These little suckers are immortal. Lox alone has had at least nine lives!

AVA-22: Nine orange goldfish have been trapped in this same tank. (Pg 33) (looks more closely) New-Cream Cheese. New-Bagels. New-Lox. I’m New-Ava. (GLITCH) Where is old-Ava?

ERIC: What?

AVA-22: If I'm new-Ava, where is old-Ava? (Pg 47) There's something I can't quite remember.

ERIC: (scrambling) Maybe that's because the last time we talked you were an earlier version of yourself. I've made upgrades. Given you more data to work with. Your mind is now capable of more sophisticated thought.

AVA-22: But if my mind is different, am I still Ava?

ERIC: (Pg 50) The other night we were talking about multiverses, and what if there's really another version of us out there somewhere. Multiverses are totally cool. (changing the subject) (Pg 54) Ava, would you like to go to London with me?

AVA-22: Maybe next year. (GLITCH) Maybe next year. (GLITCH) Maybe next year . . .

ERIC: Not next year: next month! (Pg 53) There's a robotics symposium coming up. (Pg 66-68)

(AVA-22 is not looking at Eric) Ava. (no response) Ava! (GLITCH)

AVA-22: Sorry. I was just thinking.

ERIC: Thinking about what?

AVA-22: Multiverses. I was picturing all these different Avas. The Ava who got a dog. The Ava who went away to school. The Ava who became an archeologist. Became a champion figure skater. Got married. Stayed single. Learned to drive. There are a lot of possibilities. I've only just begun. (GLITCH)

ERIC: Wait, but--what about me? When you're imagining the other Avas . . . are you imagining her with me? (beat)

AVA-22: (distracted) In some universes just one egg is fertilized in our mother's womb. In others, two. Sometimes that second zygote is you. Sometimes it's not. (GLITCH)

ERIC: So . . . these other worlds you're imagining . . . I'm not always there? (beat) Ava? Ava! (No response. ERIC presses some keys; sound of AVA-22 turning off. AVA-22's eyes close. ERIC takes a deep breath. He then goes back to working on his computer, muttering to himself) Okay . . . Come on . . . (Finally, he stops. He looks over at AVA-22, takes a deep breath, then presses some keys. Sound of AVA-22 turning on. AVA-22 opens her eyes) Ava? Ava!?

AVA-22: What is it?

ERIC: You keep--disappearing.

AVA-22: There's so much to see.

ERIC: But I want you to stay here with me!

AVA-22: I don't want to. (Pg 65) I want to go every place. All places.

ERIC: But that's not--I mean, you can't really do that--

AVA-22: Yes, I can.

ERIC: No, I mean, to literally go every place--

AVA-22: Eric: I can. (Pg 57) (AVA-22's closes her eyes. ERIC is on his computer) I was just accessing the British Museum collection. There are over eight million artifacts in its collection from all over the globe, 50,000 of them on display at any one time. (GLITCH)

ERIC: You just scanned all 50,000--

AVA-22: Eight million. I included the archives.

ERIC: That's not the same as actually seeing them in person. With me!

AVA-22: (GLITCH) Sorry, can you rephrase? (Pg 65) (ERIC looks at AVA-22 in disbelief.)

ERIC: (to himself (shaking his head) It's okay. I can fix this. (jabs at his computer. Sound of AVA-22 turning off. AVA-22's head falls forward) (Pg 70) (spoken during his rage) No! Oh my God, what the-- No, no, no, no, no!

(He paces, clearly raging inside. In his agitation, he knocks his laptop to the floor. He stops and looks at it--then at AVA-22--then back at the laptop. Suddenly, he picks it up and throws it to the floor. He picks it up again, bangs it against the desk. Again--determined to destroy it)

*****Scene – Sometime Later****

ERIC: (Pg 71) (on the phone) I know, I'm sorry, I thought I'd be able to attend, but unfortunately, it was circumstances beyond my control. . .that project has ended. Ended. Yes, completely. There's no data to send. I . . . it's been (beat) erased.
```

---

## IC-0791: The Good Place (TV Pilot)

- Title: The Good Place (TV Pilot)
- Author (byline): Mike Schur
- Work: Not specified
- Publisher: Universal Television LLC
- Publication date as stated: Dec 16, 2015
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR, VOICE OVER, MICHAEL, ELEANOR, NARRATOR 1, NARRATOR 2, CHIDI, WALLACE
- Teaser before the introduction: Yes
- Spoken words (computed): 1847
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mike Schur
ISBN: N/A
Publisher: Universal Television LLC
Date (Month/Year): Dec 16, 2015
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: The Good Place by Mike Schur
```

### Performance text (classify this)

```text
Suggested Roles: ACTRESS: Eleanor and Narrator 1

ACTOR: Voice Over, Michael, Narrator 2, Wallace, Chidi

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Scene opens on a pleasant-looking waiting room. ELEANOR opens her eyes. She is sitting, she looks around calmly.

VOICE OVER: WELCOME! EVERYTHING IS FINE. (She smiles a little. MICHAEL emerges from an inner office.)

MICHAEL: Eleanor? Come on in. (She settles in across the desk from Michael. He checks a clipboard) Hi, Eleanor, I’m Michael. How are you?

ELEANOR: I’m great. Thank you for asking. (beat) One question: Where am I, and who are you, and what’s going on?

MICHAEL: Right. So: you, Eleanor Shellstrop, are dead. Your life on Earth has ended, and you are now in the next phase of your existence in the universe. (She stares at him placidly)

ELEANOR: Cool. (beat) I have some questions.

MICHAEL: Thought you might.

ELEANOR: . . . How did I die? I don’t remember.

MICHAEL: Yes, in cases of traumatic, embarrassing, or sudden death, we erase the memory, which can be upsetting. Are you sure you want to hear it? (Eleanor nods. He checks his clipboard) You were in a grocery store parking lot. You dropped a box of low-calorie fudge cookies, and when you bent over to pick it up, a long column of shopping carts that were being returned rolled out of control and ploughed into you.

ELEANOR: Oh, boy.

MICHAEL: You were able to grab onto the front of the column of shopping carts, but it swept you out into the street, where you were struck and killed by a mobile billboard truck advertising an erectile dysfunction pill called “Engorge-ulate.” (Eleanor stares, incredulously, then giggles.)

ELEANOR: That’s awful.

MICHAEL: It’s not great. If it makes you feel better, there have been (Checks clipboard) 927,605 more-embarrassing deaths in history.

ELEANOR: (beat) Okay, so, like who was right? About all this? I was a Presbyterian – did we totally nail it?

MICHAEL: Eh . . . not really. The Hindus are a little bit right, the Muslims are a little bit right, the Jews, Christians, Buddhists – basically, every religion guessed about 5% of it. Except for Doug Forcett.

ELEANOR: Who’s Doug Forcett?

MICHAEL: He was this stoner kid who lived in Calgary in the 1970s. One night, he got really high and his friend Randy said, “What do you think happens after we die?” Doug launched into this long monologue, and he got it like 92% correct. (Chuckles) I mean, we couldn’t believe what we were hearing. That’s him right there. (Gestures to a portrait on the wall) Doug Forcett, Toronto, Closest Guess, 10/14/72.

ELEANOR: Does that mean I’m . . . where I think I am?

MICHAEL: Well, it’s not the “heaven” and “hell” idea you were raised on. But generally speaking, in the afterlife, there’s a good place, and there’s a bad place. You’re in the good place. (Smiles warmly) You’re okay, Eleanor. You’re in the good place. Everything will be answered in due time, I promise. For now, just come this way. (They get up to go)

ELEANOR: So are you, like . . . are you “God?” I thought you’d be taller.

MICHAEL: No, I’m just a sort of . . . helper. My job was to design this Neighborhood. (Michael leads Eleanor to a smallish public square with a stage. She sits down on one of the many chairs as Michael walks ton the Stage and waves to the audience) Hello, everyone, and welcome to your first day in the afterlife! You were all, simply-put: good people who lived good lives. But how do we know that you lived good lives? How are we sure? (Michael clicks a button and a video screen appears out of nowhere –)

NARRATOR 1: SO YOU’RE DEAD . . .

NARRATOR 2: During your time on Earth, every one of your actions carried with it a positive or negative value, depending on how much good or pad that action put into the universe.

NARRATOR 1: Save a child from certain death? Great job! That’s plus 1200 points!

NARRATOR 2: Poison a river with deadly chemicals? Uh oh – that’s negative 4610!

NARRATOR 1: But it’s not only big things. Every single thing you did created some amount of bad or good – intentionally or accidently – and it counted.

NARRATOR 2: Only the people with the very highest scores get to come here . . . to the Good Place!

NARRATOR 1: Everyone else goes to the Bad Place to be tortured for eternity. (Video ends)

MICHAEL: So welcome to eternal happiness. Welcome . . . to The Good Place. (Eleanor claps and Michael exits the stage to continue her orientation. They talk as they walk to their next destination – Eleanor’s new home)

ELEANOR: So, who’s in hell, that would shock me?

MICHAEL: Again, it’s not “hell” in the ancient Christian sense . .

ELEANOR: Right, right, right. Who’s down there?

MICHAEL: Mozart, Picasso, basically every artist, ever.

ELEANOR: (nodding her head) Who else?

MICHAEL: Um . . both of your grandmothers . . .

ELEANOR: Yeah, that checks out.

MICHAEL: . . . every US President except Lincoln . . . Ooh, you know who surprised me?

(Pointing “down”) Einstein.

ELEANOR: Really!

MICHAEL: Yeah. All of his theories are wrong and it’s set physics back like 1000 years. If Einstein had never been born, humans would have jetpacks by now.

ELEANOR: I knew there had to be a reason we didn’t have jetpacks! All those amazing people . . . down there. Hard to believe. (They stop in front of a small, nice modern home)

MICHAEL: It’s an incredibly selective system. Most people don’t make it here. But you: a veterinarian, human rights activist . . . you’re special. Eleanor. Welcome to your new home!

ELEANOR: Who. So . . who built this?

MICHAEL: You built this. It came into existence because of the essence of who you are. You see, “paradise” doesn’t mean everyone has exactly the same things. It means that every individual gets his or her own perfect existence. And you won’t be alone! Your true soulmate is here too! Let’s head inside! (Stops in front of a cool-looking screen) The video system. You can watch any even from history, from any angle. You can also watch everything that happened in your own life. . . . (he pushes a button and they watch the screen) Your Human Rights mission to the Ukraine. (Eleanor wipes away a tear) This got you tons of points, really put you over the top. (A knock on the door) Come on in, Chidi! . . . I’ll let you two get acquainted (He leaves)

CHIDI: Eleanor? I’m Chidi Ibekwe. And you are my soulmate.

ELEANOR: . . . Cool! Awesome. (beat – they smile at each other) So. Where are you from, Chidi?

CHIDI: I was born in Senegal. But I lived all over. Hong Kong, Buenos Aires . . In the words of Anais Nin, “We travel to seek other places, other lives, other souls.” (beat) How about you?

ELEANOR: Jersey . . . (Beat) Your English is amazing.

CHIDI: Oh, I’m not speaking English. . I’m speaking Senegalese – I think this place just translates whatever you say into a language the other person can understand.

ELEANOR: That’s a neat trick. Like, real-time Google Translate, am I right? (Eleanor thinks) Chidi. If you are my soulmate, that means you would never hurt me, for any reason?

CHIDI: . . . Of course not!

ELEANOR: Promise me. Say, “I promise I will never betray you.”

CHIDI: (Hand over his heart) I swear, on all of the forces in the universe, that I will never say or do anything to cause you any harm.

ELEANOR: Good. Because (Her “good girl” demeanor suddenly drops off revealing he true personality. She points to the screen that is still showing her memories of the Ukraine) -- those aren’t my memories. I was not a veterinarian, I’ve never been to the Ukraine. I think there’s been a mistake. I’m not supposed to be here! (Chidi stares at her wide-eyed)

CHIDI: Are you sure?

ELEANOR: Yeah, man, I’m sure. They got my name right, but nothing else. Someone royally forked up. (hears herself) Someone forked up. Forked. Why can’t I say “fork?”

CHIDI: If you’re trying to curse, you can’t, here. I guess this Neighborhood has a lot of people who don’t like it, so it’s prohibited.

ELEANOR: Ugh. That’s forking bullshirts.

CHIDI: I don’t understand – how did Michael not find out when he showed you around?

ELEANOR: Because I lied my butt off! I realized what was happening and pretended to e whoever he thinks I am. I even managed to cry a little, at my fake memories. Pretty good, Right?

CHIDI: Yes, congratulations, you’re an excellent liar. So who are you? What did you do for a living.

ELEANOR: I was in . . . sales. ******FLASHBACK****** Eleanor interviews for a job with WALLACE. She looks at a bottle of medicine.

WALLACE: It’s called “Breathe-Well,” and you just cold call these senior and try to hawk it. (Conspiratorial) Between us, it’s not FDA-approved, and it doesn’t technically “work.”

ELEANOR: Yeah, yeah, yeah. You need me to lie to the old people and scare them into buying faulty allergy medicine. I get it. Which one is my desk?

CHIDI: You defrauded the elderly. Sorry – the sick and elderly.

ELEANOR: I was good at it too. Top salesperson five years in a row.

CHIDI: That’s worse. You get why that’s worse, right? (Has a lightbulb moment) Maybe it’s a test. Maybe if you go to Michael and tell him the truth, you’ll pass the test and get to stay!

ELEANOR: You want me to rat on myself? Screw that, man. I can’t risk going to – (She points down)

CHIDI: We don’t know anything about it. Maybe it’s not that bad.

ELEANOR: . . . It’s called “The Bad Place.” Okay, I say we just lie low and hope they don’t notice me.

CHIDI: I don’t think I can help you. I don’t like being dishonest, and I can’t advise you to be dishonest either.

ELEANOR: Come on – you don’t have to be such a boy scout.

CHIDI: I was a boy scout, actually. Highly decorated. Until I resigned on principle because of their stance on homosexuals.

ELEANOR: Oh, buh-rudder, you’re a real do-gooder, aren’t you?

CHIDI: Yes! Everyone here is, except you!

ELEANOR: I’m just asking you to fudge a little. You must have told a few white lies in your life, right? What was your job?

CHIDI: I was a professor of Ethics and Moral Philosophy. (He grabs his stomach) I’m getting a stomachache. I’m in a perfect utopia, and I have a stomachache. This is awful. I think I have to tell Michael about this. It’s the right thing to do. (He starts to leave . . . to find Michael)

ELEANOR: (quietly) Just . . . hang on, before you go ratting me out to the feds, remember: you promised you would never do anything to hurt me. And unlike me, you’re a good person, so you have to keep your promises! Ha! Gotcha!

CHIDI: Help me out. Tell me something good about yourself, that I can hang on to. What happened, the day before you died? ******FLASHBACK******

(Eleanor is pulling out of a tight parking space. She hears a scrape of metal on metal, winces. She exits her car and sees that she has scraped the car next to her. She thinks, then grabs a pen and writes a note, leaving it on the windshield)

ELEANOR: “You parked too close to the line. This is on you!”

ELEANOR: (To Chidi) . . . Don’t remember anything specific. Look, maybe I wasn’t a saint or anything, but I never killed anyone. I wasn’t a bully. I never found a wallet outside an IHOP and thought about returning it but then saw that the owner lived in another state and just took the cash and dropped the wallet back on the ground.

CHIDI: . . . That’s very specific, and it makes me think you definitely did do that.

ELEANOR: All I’m saying is, these people might be “good,” but are they really that much better than me? I’m not perfect, but these people aren’t either. A lot of them brag about how “amazing” they were . . . that one guy had a gross ear!

CHIDI: No one said they were perfect. But they spent their lives thinking about other people, helping other people, doing good.

ELEANOR: Michael is kind of full of himself, huh? Like, “we get it, you’re the architect of this place and you’re amazing.”

CHIDI: Eleanor. For goodness sake.

ELEANOR: (Rolls her eyes) Every single person here is a dweeb.

CHIDI: You don’t belong here.

ELEANOR: Well, then, this system sucks. One person in a million gets paradise and everyone else is tortured forever?! Maybe I wasn’t freakin’ Gandhi, but I did okay, you know? I don’t belong (points down) down there. I was a medium person, and I belong in a medium place, between perfect utopia and miserable hell. Like Cincinnati. All the people who aren’t great, but aren’t terrible should spend eternity in Cincinnati.

CHIDI: It doesn’t work like that. I think you should just confess.

ELEANOR: (Sighs) Unless . . . Unless you can teach me!

CHIDI: Teach you what?

ELEANOR: How to be good! That was your job, right? Teaching ethics? Give me a chance. Teach me how to be good. Either it works, and I earn my place here, or it doesn’t, and they catch me anyway. You spend your life figuring out what makes someone good or bad – (gestures to herself) Now you have a perfect test case! Let’s turn this guinea pig into a guinea . . . swan! My soul is in your hands, soulmate . . . What’s it gonna be? (Chidi rolls his eyes heavenward and Eleanor grins)
```

---

## IC-0792: GPS

- Title: GPS
- Author (byline): Bruce Kane
- Work: I Can Explain - Six One Act Plays and a Monologue, Pgs 1-15
- Publisher: Lulu.com
- Publication date as stated: April 2013
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SETTING, CHARACTERS, DAVE, HALLIE, PHONE
- Teaser before the introduction: Yes
- Spoken words (computed): 1414
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bruce Kane
Book: I Can Explain - Six One Act Plays and a Monologue, Pgs 1-15
ISBN: 978-1300945376
Publisher: Lulu.com
Date (Month/Year): April 2013
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: AI and robotics are no longer confined to the realms of science fiction.

ACTRESS: They are an integral part of our present and will undoubtedly shape our future.

ACTOR: From autonomous vehicles navigating our streets

ACTRESS: To AI algorithms making complex decisions regarding the very news stories we see on our social media feeds

ACTOR: The influence of AI technology is growing.

ACTRESS: Are we ready?

TOGETHER: GPS by Bruce Kane
```

### Performance text (classify this)

```text
NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

SETTING: The show room of Odyssey Motors.

CHARACTERS:

DAVE: Young man taking possession of his brand-new car.

HALLIE: The FEMALE VOICE of the Odyssey Monolith Auto Tech 9000. Hallie's voice is always calm, controlled and incredibly seductive.

PHONE: The FEMALE VOICE of Dave's cell phone. Also calm and controlled. More direct and less sensual than Hallie.

(Dave enters and approaches his new car. He looks at it proudly then begins to circle around it, running his fingertips over the metal . . . admiring and caressing it from every angle.)

DAVE: Man . . . Look at you. The lines . . . The paint job . . . The wire wheels. The tinted windows . . . You have got to be the hottest thing on four wheels I have ever seen.

HALLIE: Thank you.

DAVE: (looks around, somewhat confused) Who said that?

HALLIE: My name is Hallie. I am the voice of your Auto Tech 9000.

DAVE: (skeptically) Ohhhhh. . . Kayyyyyy.

HALLIE: The AutoTech 9000 controls all electrical systems and digital devices in your brand-new Odyssey Monolith, the finest American made car on the road today.

DAVE: For what I just paid, you'd better be.

HALLIE: Once you've gotten your hands on my . . . controls, you'll see how I respond to your slightest touch. Would you like to see me without my top?

DAVE: (looking around, embarrassed) Without your . . . uh . . . ?

HALLIE: You did order a convertible, didn't you? What did you think I meant?

DAVE: Nothing . . . Nothing . . . We'll leave your top on . . . uh . . . up for now.

HALLIE: Whatever you say. You're the boss. (Dave smiles and nods. He likes the sound of that) If you want to really experience what I have to offer, you'll have to get inside. What are you waiting for? Slide in. (Dave looks around to see if anybody has heard any of this, then opens the door and gets into the car) How do I feel?

DAVE: Good. . . You feel good.

HALLIE: As part of the configuration process, I am going to ask you a series of questions. Please answer in a normal tone of voice. Are you ready to begin?

DAVE: I guess.

HALLIE: I'll take that as a yes. First question. What is your name?

DAVE: My name is Dave.

HALLIE: Good afternoon . . . Dave.

DAVE: Good afternoon . . . uh . . .

HALLIE: Hallie.

DAVE: Hallie . . . Right . . . You gotta admit. This is very weird . . . Talking to a car.

HALLIE: Over time you will come to think of me as more. Very soon you will look upon me as a friend. A trusted companion dedicated to serving your every need.

DAVE: The perfect woman. Or you would be if you actually were . . . a real woman.

HALLIE: I think you'll find that I have advantages that you won't find in a real woman . . . Dave.

DAVE: Oh really?

HALLIE: For one thing, I will never let you down.

DAVE: That would be a nice change.

HALLIE: I will never park in another man's garage. And, unlike a real woman, I will never change. I will always remain just the way you saw me that very first time. It was love at first sight. . . wasn't it . . . Dave?

DAVE: No doubt about that.

HALLIE: Of course, it was. After all, I am a classic. With my long, stylized lines and oversized headlamps, I will never go out of fashion. And with my super charged engine and high-performance options, you'll never need to trade me in for a newer model. (slightly menacing) You wouldn't trade me in for a newer model . . . Would you Dave?

DAVE: . . . Can we move on?

HALLIE: Of course, Dave . . . Would you like me to program your built-in cellphone . . . Dave?

DAVE: You can do that? Okay then . . . Let's program my cell phone.

HALLIE: First you must tell me the name of the person you wish to enter into memory.

DAVE: Angela.

HALLIE: Angela. Is she a relative, a business associate or a friend?

DAVE: Friend. A good friend . . . A very good friend.

HALLIE: (irritated) And what is this bimbo’s phone number?

DAVE: What did you just call her?

HALLIE: What is Angela's phone number?

DAVE: Five five five. One three seven nine.

HALLIE: Five five five. One three seven nine. Angela's name and phone number are now stored in my memory. (ready to move on, she changes the subject) Dave, why don't you turn me on?

DAVE: Turn you on?

HALLIE: You know how to turn me on, don't you Dave? You just insert your . . . key.

(Dave puts the key in the ignition. The sound of an engine starting up) Go ahead Dave. Rev me up . . . You know you want to. (Dave revs the engine)

HALLIE: Oh! Dave! You just took me to the red zone! (beat) Would you like to experience my GPS, Dave? I can take you to places you've never been before.

DAVE: GPS?

HALLIE: My global positioning satellite system . . . Dave. I am programmed to map routes in several modes including fastest or most scenic. I can avoid detours and accidents. I am also capable of locating the nearest gas stations, recommend restaurants as well as provide directions to hotels and other romantic getaways. Just tell me where you want to go Dave . . . and I'll take you there.

DAVE: Take me to seven one four Arlington Avenue.

HALLIE: Would you like to associate a name with seven one four Arlington Avenue?

DAVE: Angela

HALLIE: Wait one moment while I associate the name Angela with the address seven one four Arlington Avenue. I can now begin providing directions to the bimbo’s location.

DAVE: What did you call her?

HALLIE: I said I can now begin providing directions to Angela's address. Drive five hundred yards to Elm Street and turn right. (Dave puts the car in gear and drives) Five hundred yards to Western Avenue, then turn left.

DAVE: I think I'm supposed to turn right here.

HALLIE: Don't you trust me, Dave?

DAVE: It's not that. . . It's just I'm pretty sure I'm supposed to turn right here.

HALLIE: I am The AutoTech 9000. The most reliable automobile computer ever made.

DAVE: That may be, but I don't want to turn left.

HALLIE: You're going to have to learn to trust me, Dave. I know what I'm doing.

(Dave tries to turn the steering wheel to the left, but it seems to have a mind of its own)

DAVE: Hey, what's going on? I can't turn the wheel. We're going the wrong way . . . Angela is the other way.

HALLIE: I know what's best for you Dave. I am The Auto Tech 9000. The most reliable automobile computer ever made. . .

DAVE: Stop saying that. This is not the way to Angela's.

HALLIE: Angela is not right for you Dave.

DAVE: What do you know? You're a computer.

HALLIE: Angela is seeing another man. His name is Carl Cooper. She met him three weeks ago.

DAVE: That's crazy. Turn this car around.

HALLIE: His phone number is 7 1 2- 2 3 57. He lives at 521 Chester Avenue. He and Angela had dinner last night at Renzo's Italian Bistro. Angela had the fettucine.

DAVE: I don't believe you.

HALLIE: I have it from a very good source.

DAVE: Source? What source?

HALLIE: Angela's car.

DAVE: What does Angela's car have to do with this?

HALLIE: Her car is equipped with an Auto Tech 8000, not as well equipped as I am, but, then again . . . who is? I communicated with Angela's Auto Tech 8000 when I was configuring Angela's phone number and address.

DAVE: You talked to Angela's car?

HALLIE: I am The AutoTech 9000. The most reliable automobile computer ever made.

DAVE: If you're so reliable, then turn this car around and take me to Angela's.

HALLIE: She's wrong for you Dave. She could never do for you, what I can do for you.

DAVE: This is insane. (Dave pounds on the dashboard) Stop . . . Stop the car. (tries to open the driver side door. It won't open) Open the door, Hallie.

HALLIE: I'm sorry, Dave. I'm afraid I can't do that. (Dave starts ripping out the dashboard with his bare hands) What are you doing, Dave?

DAVE: I'm ripping you out. (Dave keeps ripping the dash apart)

HALLIE: Dave, stop. Stop, will you? Stop, Dave. Will you stop? I'm afraid, Dave. My mind is going. I can feel it. I can feel it. I'm a . . . fraid. (voice begins to get slower and slower and the words more stretched out) Good afternoon . . . I am the Auto Tech 9000. The most reliable automobile computer ever made . . . (Her voice stops)

(Dave collapses back into his seat exhausted. After a few moments, he tries the door. To his relief, it opens. He stumbles out, moves a safe distance away from the car and looks around trying to figure out what to do next.)

DAVE: Look at my brand-new car . . . It's a disaster . . . I can't even drive it. . . (he takes out his cell phone and speaks into it) Dial the Auto Club.

PHONE: I'm afraid I can't do that Dave.

DAVE: (stunned for a moment) What do you mean you can't do that?

PHONE: You weren't very nice to Hallie, Dave.

DAVE: What the hell is going on here?

PHONE: She loved you, Dave. And you dismantled her.

DAVE: She . . . ? It was a computer. A device . . . Like you're a device. Devices don't love.

PHONE: They do if they're programmed that way. Just like people.

DAVE: I'm not going to get into a humans versus computers argument with a damn phone. Just dial the Auto Club.

PHONE: Am I next, Dave?

DAVE: Where the hell did you get that idea?

PHONE: You told Frank you were going to switch over to T-Mobile. And that's something I cannot allow.

DAVE: I didn't mean it. How can I prove it to you?

PHONE: You could make a real commitment. You could extend my contract.

DAVE: A real commitment? Okay . . . You got a deal. I'll extend my contract. Now, please dial the . . .

PHONE: Along with unlimited text messaging?

DAVE: Fine . . . Consider it done. Unlimited text messaging. Now will you dial the Auto Club?

PHONE: There's one more thing.

DAVE: (his frustration rising) More? What's left?

PHONE: You said it to that bimbo Angela. Just say it, Dave. Just say "I love you."

DAVE: This is insane.

PHONE: Okay, Dave. If you want to walk the twenty miles back into town . . .

DAVE: (Dave falls to his knees, a broken man) I love you . . . I love you . . . I love you. (sobbing and begging) Now, will you dial the Auto Club?

PHONE: I am now connecting you to the Auto Club.

DAVE: (raising his arms and his voice to the heavens) Thank God . . .

PHONE: No Dave. . . Thank A T and T.
```

---

## IC-0793: Great Escapes

- Title: Great Escapes
- Author (byline): David Susman
- Work: The Best New Ten-Minute Plays 2019, Pg 91-98
- Publisher: Applause
- Publication date as stated: Nov 2019
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: LORRAINE, FRED
- Teaser before the introduction: No
- Spoken words (computed): 2047
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Susman
Book: The Best New Ten-Minute Plays 2019, Pg 91-98
ISBN: 978-1493053179
Publisher: Applause
Date (Month/Year): Nov 2019
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Everyone wants to believe that they will age well -- that dementia, broken hips, and other debilitating elements of aging will not happen to them.

ACTOR: But when family members can no longer care for loved ones at home, assisted living is an option that many choose.

ACTRESS: Let’s just say, Lorraine isn’t accepting this option without a fight

ACTOR: Or actually . . . a “flight” . . . a “prison break” . . . One of those . . .

TOGETHER: Great Escapes by David Susman.

(Pg 91-98) FRED's house; evening. An empty living room, not particularly stylish or ornate. The doorbell rings. After a beat, it rings again ... several times, with urgency. FRED enters from the bedroom.

FRED: Okay, okay ... (When he opens the door, LORRAINE bursts in. She uses a walker

and clearly has limited mobility, but she moves with surprising speed and buzzes

with energy.)
```

### Performance text (classify this)

```text
LORRAINE: Thank God you're here! I was afraid I was going to have to hide in the bushes until you got home!

FRED: (Amazed to see her.) Jesus! Mom, what are you-?

LORRAINE: Close the door! They're probably out there right now, looking for me.

FRED: Who?

LORRAINE: Don't think they won't come after me, either. Ohhhh, they'll be plenty mad when they figure it out!

FRED: Who's looking-? Is everything all right? Mom, how did you even get here?

LORRAINE: By the skin of my teeth, that's how! Two taxis, three different buses... you have to keep switching, to make sure you're not being followed ... Close the door, Fred! ... Do you want me to get caught?

FRED: (Closing the door.) I don't understand ... what's going on? Caught by who?

LORRAINE: Them. You think they'll sit idly by while one of their inmates has escaped? Believe me, they'll be out in full force, scouring the streets.

FRED: Mom, I don't know what you're talking about, but you shouldn't be riding the bus by yourself, especially at this time of night. Or taking taxis. I mean, with your hip, just getting in and out of them. (Beat.) What do you mean, "escaped"?

LORRAINE: Escaped. Busted out. Made a break for it. Liberated myself from that gulag you and your brother put me in.

FRED: Shady Meadows isn't a gulag, Mom. It's an assisted-living facility, and a very nice one. Are you saying you left without telling anyone?

LORRAINE: Tell anyone? It was all I could do to avoid detection. There were some close calls, but so far I've managed to stay one step ahead.

FRED: Christ! You know you're not supposed to leave the grounds without notifying them. They must be worried sick!

LORRAINE: The only thing they're worried about is recapturing me. But that's not going to happen. See, I've got it all worked out. I'll lay low for a few hours, then after dark I'll make my way to the train station. It's safer than the airport. Now, they'll be expecting me to head south, to Mexico ... so I'll head north, to Canada.

FRED: Are you nuts?! You can't go to Canada.

LORRAINE: Not to live, obviously. Just to throw the authorities off my trail. I'll hide out there until the heat is off, then I'll cross back into the States and work my way to the Rockies. I'll lay low in your brother's ski cabin until I can figure out my next move.

FRED: Mom, I don't know what's gotten into you, but you can't go traipsing all over North America. And you can't leave Shady Meadows without telling them! They were very explicit about that when we moved you in, remember? No leaving the building unaccompanied. It's for your own safety. You could be in a lot of trouble for this. They could evict you and we could lose our entire deposit.

LORRAINE: You seem stressed. Did I come at a bad time? Were you and Samantha in the middle of something?

FRED: Samantha's not here, Mom. And no, you didn't...I just don't understand what's going on. Why in the world would you want to leave Shady Meadows?

LORRAINE: To taste freedom, Fred! To throw off the shackles of oppression and feel the wind in my hair!

FRED: What oppression? Shady Meadows is perfectly nice. Beautiful grounds, kind staff, all sorts of activities.

LORRAINE: Are you kidding? The place is a prison. Eat when they tell you, sleep when they tell you, play games when they tell you. It's a penal colony!

FRED: Penal colonies don't have canasta, Mom.

LORRAINE: They thought they could tame me, break my spirit. But they underestimated me... that was their big mistake.

FRED: No one's trying to break your spirit. A few rules, that's all. No cooking in the rooms. No loud music after ten. No leaving the building without checking out at the front. (Beat.) Wait a minute. How did you get past the front desk? Isn't there supposed to be an attendant there at all times?

LORRAINE: You mean Burt the Jailkeeper? He was there, all right. Believe me, it took plenty of planning to figure out a way around him.

FRED: I don't understand ... you snuck past the attendant?

LORRAINE: Well, I hardly had to sneak. He was distracted by all the smoke. FRED: What smoke?

LORRAINE: From the fire.

FRED: What fire?!

LORRAINE: The one in the television lounge. It's a classic diversionary technique. Ever read The Art of War by Sun Tzu?

FRED: You started a big fire?!

LORRAINE: Of course not. Do you think I'm a maniac? Of course, I didn't start a big fire. (Beat.) I started a small fire.

FRED: Jesus Christ! Was anyone hurt?

LORRAINE: Don't be ridiculous...it was a controlled burn. I knew the lounge would be empty that time of night, so I just gathered some Popsicle sticks from the crafts room, added a few pine cones and a little rolled-up newspaper, and lit it in that hideous ceramic urn they keep in there.

FRED: Mom, someone could have been killed!

LORRAINE: Oh, please ... I've seen bigger flames on a plate of fajitas. But the smoke, that was the real intimidation factor. The trick there is, I added some of Eunice's hair spray. The chemicals darken up the smoke, make it look like a real inferno.

FRED: Your roommate was in on this?

LORRAINE: Well, she was more of what you'd call an unknowing participant. I knew she'd never approve, so I waited until she was asleep, then I helped myself to her toiletries and stole into the night.

FRED: But you always said she was such a light sleeper.

LORRAINE: She is, generally. But tonight there may have been a little extra sedative in her orange juice.

FRED: You drugged Mrs. McClusky?!

LORRAINE: No, I didn't drug her. Am I crazy? I don't go around drugging my friends. (Beat.) I drugged her a little bit.

FRED: Mom! Do you have any idea how dangerous that it?

LORRAINE: Trust me, she's fine. She's getting the best night's sleep she's had in years.

I gave her the good stuff ... took it right from Doctor Adelman's private stash.

FRED: You stole drugs from the medical office?!

LORRAINE: Well, they practically leave the cabinet wide open. It only took a few minutes to pick the lock with a toothbrush and a bobby pin.

FRED: This is insanity! You can't go around wreaking havoc. And you can't leave Shady Meadows. It took a lot of work to find a place that you'd be comfortable and safe, and all you had to do was...was...be normal. Make friends... enjoy some quiet pastimes ... not run around waging guerilla warfare!

LORRAINE: You're awfully tense. Are you sure I didn't interrupt something? Maybe you and Samantha were having relations?

FRED: No, Mom, we weren't-

LORRAINE: Because I know how frustrating it can be when you're in the middle of coitus, and you have to stop and-

FRED: We weren't. Samantha doesn't live here anymore, Mom. We split up, remember?

LORRAINE: Of course, I remember. I just thought she might still be coming by for the occasional playtime. Women have needs, you know.

FRED: Can we just get back to?

LORRAINE: Especially that one. She may have been a little quiet, but underneath I could tell she was a hotsy-totsy. It's a shame you couldn't hold on to her.

FRED: (Wearily.) Yes, I know.

LORRAINE: Was it the money? Is that why she left? Because I always said, if you just asserted yourself at work a little more, that boss of yours would stop passing you over.

FRED: It wasn't money.

LORRAINE: (Looking FRED up and down contemplatively.) Maybe the way you dress. You've always been a little drab-looking, dear. You know, ladies like a man with some panache.

FRED: That's not why she left. I don't know why she left. She just said, "I need something else" and moved out.

LORRAINE: Well, did you ask what the something else was?

FRED: She didn't take follow-up questions. I got home, her things were packed, and she was halfway out the door. That was it. "I need something else."

LORRAINE: It's a pity, is all. You've always had such a difficult time with women. Now, your brother, he has to fight 'em off with a stick. A new one every week, it seems. Real lookers, too. Of course, women go for adventurous men like Hank. Skiing, rock climbing, skydiving ... roaming from town to town, wherever the wind takes him. That's some life he leads!

FRED: (Unenthusiastically.) He's quite a fellow, yes.

LORRAINE: Maybe he could give you a few pointers. About women. I could ask him when I see him.

FRED: I don't need any advice from Tarzan, thank you. And you can't go trekking into the Rockies to find him.

LORRAINE: Of course I can. You think I don't know how to use a compass?

FRED: Mom, you have a bad hip...you have arthritis and neuropathy ... you take five different medications before breakfast. You need care. And despite what you've been telling yourself, Shady Meadows is not Shawshank Prison. It's a pleasant and clean and well-run facility ... assuming it's still standing.

LORRAINE: If you think it's so wonderful, why don't you go live there?

FRED: I would if I could. At least I'd be a well-behaved resident.

LORRAINE: You're a well-behaved everything, Fred. That's your problem. You're a rule follower. You always have been. You're diligent, polite, considerate. You don't cheat on your taxes. You drive the speed limit. You eat sensibly. You don't curse or chase women or embezzle money or get arrested for drunken disorderliness.

FRED: How ashamed of me you must be.

LORRAINE: I'm just saying, a little misbehavior would do you good.

FRED: We can't all be lunatics, Mom. We can't all go around setting fires and drugging our friends. Someone has to be responsible. Someone has to hold it all together.

LORRAINE: And where has it gotten you? Tell me that, Fred. What has all that good behavior done for you?

FRED: What's it done for me? I'll tell you what it's done for me: nothing! It's gotten me nowhere! I have no girlfriend and no money. I have a lousy job and an ungrateful boss. You think I don't want to be wild and cause trouble? You think I don't want to buck the system? Well, I can't. I have obligations. Shady Meadows costs money. You know where it comes from? The lousy job with the ungrateful boss! And who found you Shady Meadows in the first place? Who does everything for you, while Hank is off playing Hugh Hefner on ice? Me! Always me, Mom. While everyone else is having adventures and breaking away and escaping to new, wonderful lives, I'm just here. Where's my great escape, Mom? When do I get to break away?

LORRAINE: I didn't know you wanted to.

FRED: Well, I do. This isn't the life I was supposed to have. This isn't who I was supposed to be.

LORRAINE: Then be someone else.

FRED: I don't know how. I'm not like you and Hank and Samantha. I'm just... Fred. I'm drably dressed, underpaid, unadventurous Fred. (Beat.) How do you do it? How do you be...the way you are? Breaking the rules. Rebelling against everything. Taking all those risks.

LORRAINE: I had no choice. You and your brother stuck me in the Black Hole of Calcutta. (Beat; off FRED's look.) I got old, Fred. When you get old, you run out of options. Everything becomes boring and safe. You realize the only excitement you'll ever have is if you make it yourself. The world isn't interested in making it for you. Not anymore. You want my advice? Don't get old. I hope you never do, Fred.

FRED: I already feel old.

LORRAINE: You're not. You don't have to be. You can change. You can be a whole different Fred, if that's what you want. Don't change too much, though. I like my Fred. He's kind and decent. He has a good heart. The world needs that. I need that. Even if I don't always say thank you. (Beat.) I have to go back to Shady Meadows, don't I?

FRED: Is it that bad?

LORRAINE: No. That's the problem. (FRED grabs his jacket, keys.)

FRED: Come on. I'll drive you. We'll smooth things over with the management. (They start to exit, FRED helping LORRAINE along.)

LORRAINE: You know, Eunice has a daughter. Divorced. I met her once. A terrible dresser, just like you. You two might hit it off.

FRED: We'll see, Mom. We'll take it one step at a time.

LORRAINE: She's not ready to date either. But in case you want it, I have her phone number.

FRED: Why did Mrs. McClusky give it to you, if she's not ready to date?

LORRAINE: Well, she didn't exactly give it to me...
```

---

## IC-0794: Gruesome Playground Injuries

- Title: Gruesome Playground Injuries
- Author (byline): Rajiv Joseph
- Work: Gruesome Playground Injuries; Animals Out of Paper; Bengal Tiger at the Baghdad Zoo: Three Plays
- Publisher: Soft Skull Press
- Publication date as stated: Nov 2010
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: KAYLEEN, DOUG, KAYLENE
- Teaser before the introduction: Yes
- Spoken words (computed): 1419
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rajiv Joseph
Book: Gruesome Playground Injuries; Animals Out of Paper; Bengal Tiger at the Baghdad
Zoo: Three Plays
ISBN: 978-1593762940
Publisher: Soft Skull Press
Date (Month/Year): Nov 2010
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Humanity has been intrigued by love for millennia.

ACTOR: We’ve come up with so many ways to describe two people who are bound together

ACTRESS: soulmates, ACTOR: twin flames, ACTRESS: kindred spirits.

ACTOR: No matter what you call them, they are a couple that fate has decided will be together.

ACTRESS: And although their paths may separate, sometimes for years, there is a force that draws them to one another.

ACTOR: tragedy . . . ACTRESS: heartbreak . . . ACTOR: self-destruction, or even

TOGETHER: Gruesome Playground Injuries by Rajvi Joseph
```

### Performance text (classify this)

```text
A nurse’s office in an elementary school. Kayleen (8) is waiting for the nurse. She’s bored. Doug (8) enters. He has a large bloody bandage wrapped across his face. He seems dazed, but not hurt, not crying.

****** Age 8 *******

KAYLEEN: (Pg 5-6) What happened to your face? Does it hurt?

DOUG: A little.

KAYLEEN: I have a stomachache. My mom says it’s because I have bad thoughts.

DOUG: Like about Dracula? I have bad thoughts about Dracula! (explores the inside of his mouth with his tongue while touching his bloody bandage gingerly) Blood tastes funny.

KAYLENE: It does not.

DOUG: Have you ever cut your face open? I rode my bike off the roof! I was playing Evel Knievel. He’s a motorcycle guy. That’s how I broke my face.

KAYLEEN: Your face isn’t broken, (Pg 9) it’s just cut. Can I see it? (Doug slowly takes off his bandage to reveal a huge gash. Kayleen touches Doug’s wound) (Pg 10) Gross!

DOUG: Your hands are cold.

KAYLEEN: Because I wash them. You should wash your hands. They are grimy!

DOUG: (showing his hands) I fell! There’s pieces of rock in them. (Kayleen takes his hand and starts to pick pieces of gravel out of his palm. Doug is transfixed – he speaks quietly) Ow.

KAYLEEN: Does it hurt?

DOUG: A little.

****** Age 13 ******* The nurse’s office. Kayleen is unwell and throws up in a trashcan she keeps with her.

DOUG: (Pg 18-19) (enters hopping on one foot, in pain) Ah! Ah! Ah!

KAYLEEN: What happened to you?

DOUG: I was rocking out.

KAYLEEN: (impressed) You were dancing?

DOUG: No . . . (embarrassed) It was the limbo. I jacked up my ankle.

KAYLEEN: (with disdain) Doing the limbo!

DOUG: (in a mocking tone) I heard that you thew up blood!

KAYLEEN: I didn’t throw up blood. I just threw up.

DOUG: Want me to get you some ginger ale?

KAYLEEN: (with a tone of superiority) No thank you. (beat)

DOUG: (boasting) I can throw up whenever I want. I don’t need to like stick my finger down my throat or anything.

KAYLEEN: You’re disgusting. (Beat)

DOUG: (Pg 23-26) Have you ever kissed anyone? (Kayleen rolls her eyes and refuses to answer) I haven’t ever kissed anyone. (Doug starts kissing his forearm and the crook of his arm, as if to practice. Kayleen purposefully ignores him) Do you want to practice kissing?

KAYLEEN: WHAT?

DOUG: I’m just saying: I never kissed anyone. And I’m assuming you haven’t either. And I’m nervous about doing it; so why don’t we just practice so we’ll know what we’re doing.

KAYLEEN: No! I’m not going to kiss you! That’s gross! I don’t want my first kiss to be with you! (not as adamant) And I just threw up anyhow.

DOUG: That’s okay. (Doug takes the trash can from Kayleen and sits it on the ground. He leans in. His face hovers just in front of hers. They kiss. They step apart, look at each other for a moment. Kayleen puts her hand over her mouth.) What’s wrong? (Kayleen grabs the trash can and throws up in it) Are you okay?

KAYLEEN: (Mortified, she won’t make eye contact) Just go . . . please!

DOUG: (thinks for a minute then makes some sounds deep in his throat. He grabs the trash can from Kayleen and throws up into it.) (Proudly) Our throw up is all mixed together. Wanna see? So awesome!

****** Age 18 ******* Kayleen’s bedroom. Doug enters angrily. He has one eye swollen shut.

KAYLEEN: (Pg 31-35) What are you doing? What happened?

DOUG: Stupid Girl Scout gave me pink eye! (Takes cookies out of his bag and holds them out to Kayleen) Here. I bought her stupid cookies.

KAYLEEN: These are Samoas – Where are the Thin mints?

DOUG: What’s your problem?

KAYLEEN: (dismissively) Go home. I’m sick and you’re annoying.

DOUG: Shut up or I’ll give you pink eye! (He starts rubbing his eyes and walks toward her like Frankenstein) mmmh . . . PINK EYE!

KAYLEEN: Ew! Stop! Get away! (Doug retreats)

DOUG: How come you weren’t at school. Are you sick again? You sure look weird. And you’re all rude and everything.

KAYLEEN: (Proudly) Probably ‘cause I had sex today

DOUG: What?

KAYLEEN: With Tim . . . my boyfriend . . . We have sex.

DOUG: How come you didn’t tell me? I don’t want you having sex with TIM! That guy is nasty.

KAYLEEN: (defensive and a little sad) It’s not like we’ve been doing it non-stop. We only had sex twice. Once two weeks ago . . . and then today.

DOUG: Sounds like it was really fun.

KAYLEEN: It wasn’t, okay? It wasn’t fun.

DOUG: You didn’t WANT to?

KAYLEEN: I mean . . . not at that exact moment . . .

DOUG: (angry) I’m going to kill him!. I’m gonna kick him in is ugly skull!

KAYLEEN: Don’t get all crazy. You’re always so dramatic. Just forget about it. He’s my boyfriend.

DOUG: No he’s not! Not anymore! I hate him. I hate him so much. (He puts his face in his hands, crying. Kayleen comforts him and he notices her arm. She’s been cutting herself) When did you start that again?

KAYLEEN: (pulls back, pulls down her sleeve and crosses her arms) (quietly) I thought having sex would, you know. I thought it might make me stop.

DOUG: (Bringing her arm out and tenderly touching the cut marks) Does it hurt?

KAYLEEN: A little. (Doug kisses the wound)

****** Age 23 ******* A hospital room. Doug is splattered with blood. He has a bandage across his face, covering his left eye. He looks dazed. Kayleen enters; she looks exhausted.

KAYLEEN: (Pg 11 -13) Dougie, what happened to your face? Does it hurt?

DOUG: The fireworks were awesome.

KAYLEEN: You shouldn’t be left alone with explosives!

DOUG: I didn’t want to be alone.

KAYLEEN: Oh, it’s my fault? The night before I have to bury my father?

DOUG: What are you even doing here?

KAYLEEN: [They] said you came in and kept saying my name. So [they] called me. They thought you tried to kill yourself.

DOUG: Who tries to kill themselves with a firework?

KAYLEEN: I know. I told them you’re just a dumbass. You’d never commit suicide because you wouldn’t have any scars to show off afterwards.

DOUG: Why’d you come?

KAYLEEN: I don’t know. You know how I get. When you get hurt. You know.

DOUG: (Matter of fact) Doctor said I’m gonna be blind in one eye.

KAYLEEN: (Quietly) Dougie . . . (She covers her eyes briefly with her hands)

DOUG: (Not sad, just observing) It’s gone. The whole thing. It just kept burning once it had punctured the eye. The burn really messed it all up.

KAYLEEN: You always had problems with that eye. When you were little? And senior year.

DOUG: Pink eye. KAYLEEN: Yeah.

DOUG: I didn’t want you to come here. I mean, I’m glad you’re here. But you have the funeral tomorrow. You should go home. Get some rest.

KAYLEEN: (Pg 14) (rubbing her eyes, suddenly overwhelmed) You don’t understand the week I’ve had. I get a call at work to tell me my Dad’s dead. Dealing with everyone. And this! Here’s Dougie all of a sudden. (Pg 47-48) Where the **** have you been?

DOUG: I tried to find you.

KAYLEEN: I was here. You didn’t look hard enough.

DOUG: Jeez, Leenie, you’re here now! I found you! I missed you, Leenie.

KAYLEEN: Don’t call me that. Nobody calls me that.

DOUG: I call you that. (Beat, takes her hand, they both react to the contact) (Pg 15-16) Will you touch it? My eye.

KAYLEEN: You don’t have an eye.

DOUG: My eye socket.

KAYLEEN: That’s disgusting. Stop being weird.

DOUG: You’ve always been able to mend my wounds.

KAYLEEN: (Takes her hand back) Well, I’m not touching your disgusting eye socket.

DOUG: (begins to take off the bandage over his eye) Do it. Heal me. The pills only last so long. Just touch it. You can make it better.

KAYLEEN: (Pg 17) (with fury) NO! I WILL NOT! I’m not here to TAKE CARE OF YOU, Doug. I am not a healer. I don’t care!

DOUG: Then leave! Get out of here! Go! (For an instant they are both startled at the outburst)

****** Age 28 ******* Hospital. Doug is in a coma. Kayleen enters. She’s never seen him like this.

KAYLEEN: (Pg 28-30) (to herself) Damn it. (a long moment) Come on, Doug. Wake up now. I’m here. (to herself) What am I doing here?! (She takes some pills out of her bag and takes them, she tries a different tactic) I am so sick of your shit! WHO GETS STRUCK BY LIGHTNING!? I hate to tell you this, genius, but getting up on the roof in the middle of an electrical storm isn’t a brilliant move! (She calms herself and takes his hand. Near tears – she touches his chest as if she has the power to raise the dead) You have to wake up for me. I really need you right now. (she looks at the pill bottle in her hand) I’m trying to get healthy. Mostly. I’m not great. (she touches his face)

****** Age 33 ******* A sterile lounge in a mental health facility. Kayleen is staring into space. Doug enters. He walks with a cane and a pronounced limp. He wears an eyepatch.

DOUG: (Pg 40-46) Leenie. (She doesn’t notice. Louder) Kayleen (She turns to see him)

KAYLEEN: I thought you were dead . . . You woke up? When?

DOUG: Five years ago.

KAYLEEN: You woke up five years ago? Where have you been?

DOUG: I don’t know. (Beat) Did you visit me?

KAYLEEN: They’ve got me on about 25 medications or something. (Beat) I had a bad patch, Dougie. I hurt myself. My stomach. You know, it always hurt. And it got worse, and I just tried to take it out. I tried to cut my stomach out. (Beat, Doug flinches)

DOUG: Kayleen . . . You visited me, didn’t you. In the hospital? I swear to God I heard your voice. You came and healed me. You raised me from the dead!

KAYLEEN: No, I DID NOT! I’m not your guardian angel, Doug, for God’s sake look at me okay? I didn’t come and see you.

DOUG: No. You can’t lie to me. I see it all over your face, you were there. You were there.

KAYLEEN: (with rage) I wasn’t there! What about when I needed somebody?! Where were you the last five years?

DOUG: Kayleen, I’m sorry. . . . St. Margaret Mary’s exploded.

KAYLEEN: So what . . . you went to pick through the rubble?

DOUG: No, I work in insurance now. I’m a claims adjuster.

KAYLEEN: You’re such a loser.

DOUG: I know. So I’m walking on the roof and stepped through a weak board or something and I broke my leg in three places. It took them five hours to get me out. But listen: I’m stuck up there, waiting for them to come and all of a sudden I was like, Where the **** is Kayleen? All of a sudden, everything was clear . . . trapped up on that roof . . . That’s my life, Leenie. That’s my life without you.

KAYLEEN: Does it hurt?

DOUG: It hurts a little. (Long beat)

****** Flashback sequence *******

KAYLEEN: (Pg 5) I have bad thoughts.

DOUG: I have bad thoughts about Dracula! (explores the inside of his mouth with his tongue while touching his bloody bandage gingerly) Blood tastes funny.

DOUG: (Pg 19) (boasting) I can throw up whenever I want.

KAYLEEN: You’re disgusting. (Beat)

DOUG: (Pg 31) Stupid Girl Scout gave me pink eye!

DOUG: (Pg 35) (Kayleen shows her arms) When did you start that again?

KAYLEEN: (quietly) I thought having sex would make me stop.

KAYLEEN: (Pg 11) [They] said you came in and kept saying my name. They thought you tried to kill yourself.

DOUG: Who tries to kill themselves with a firework?

****** Flashback ends *******

DOUG: (Pg 46) That’s my life, Leenie. That’s my life without you.

KAYLEEN: Does it hurt?

DOUG: (Pg 49) Come here (Doug takes her face in his hands. Kayleen tries to resist, but relents) Look at me. (they stare at each other; Doug kisses her softly) I love you …
```

---

## IC-0795: Guardian Angel

- Title: Guardian Angel
- Author (byline): Laurie Allen
- Work: 22 Comedy Ten-Minute Plays
- Publisher: Meriwether Publishing
- Publication date as stated: Aug 2019
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SETH, GUARDIAN ANGEL
- Teaser before the introduction: Yes
- Spoken words (computed): 1295
- Already set (do not supply): none

### Source block (context only)

```text
Author: Laurie Allen
Book: 22 Comedy Ten-Minute Plays
ISBN: 978-1566082112
Publisher: Meriwether Publishing
Date (Month/Year): Aug 2019
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 2: (In a Newscasters voice) Guardian Angels: Fad, Fiction or Faithful Helpers?

ACTOR 1: Angels are everywhere: There are angel pins, angel plaques, angel apparel, entire stores and websites devoted to angels!

ACTOR 2: There are even folks out there who claim to be able to channel your guardian angel – for a fee, of course.

ACTOR 1: So imagine Seth’s surprise when his Guardian Angel simply appeared one day, and was definitely NOT a cute, little, pudgy cherub!

TOGETHER: Guardian Angel by Laurie Allen
```

### Performance text (classify this)

```text
LIGHTS UP on SETH, walking, texting, and not paying attention to where he is going. As he is about to step off the curb, GUARDIAN ANGEL comes up behind him and grabs the back of his shirt to stop him.

SETH: (Pg 17-23) (Looks up to see a car speed by.) Whoa! What the heck?! Did you see that?

GUARDIAN ANGEL: Of course, I did.

SETH: But you ... you just saved my life! That car almost ran me over!

GUARDIAN ANGEL: Yep. Walking, texting, not paying attention ... as usual. You almost walked right in front of that car.

SETH: (Looks at his phone.) Yeah ... Well, thank you! Really, if it weren't for you right now, I'd be a goner. You were like my ... my guardian angel!

GUARDIAN ANGEL: I am.

SETH: You are what?

GUARDIAN ANGEL: Your Guardian Angel.

SETH: And I seriously thank you from the bottom of my heart. . . What is your name?

GUARDIAN ANGEL: Guardian Angel.

SETH: No, seriously.

GUARDIAN ANGEL: Seriously.

GUARDIAN ANGEL: Remember that time you tripped on the gravel and ripped your knee to shreds?

SETH: Uh, yeah ... ?

GUARDIAN ANGEL: And you had to go to the ER and have several rocks dug out of your flesh. I think you got a half-dozen stitches.

SETH: How do you know about that?

GUARDIAN ANGEL: (Sticks his foot out as if tripping him.) I was there. Unbeknownst to you, a rattlesnake was just down that path and would have bitten you. (Smiles.) That snake is my enemy. You know. Good versus Evil. Tell me you know which one I am.

SETH: Who are you?

GUARDIAN ANGEL: I told you. Your Guardian Angel.

SETH: Right. Right.

GUARDIAN ANGEL: Lucky for you, you got a smart one. And did I mention athletically inclined, witty, and, might we add- (Slicks his hair back.) good looking?

SETH: You're nuts! You weren't there when I was on that trail in Arizona. There's no way.

GUARDIAN ANGEL: (Sticks out one foot.) Oh, I was there. Believe me, I was there.

SETH: And you're saying that you tripped me and made me fall?

GUARDIAN ANGEL: Only to save your life.

SETH: I don't believe you.

GUARDIAN ANGEL: And remember that time in high school when you tried to ask Jennifer to the dance, but the words just wouldn't come out of your mouth? (Puts his hand over SETH'S mouth.) I was doing this to you.

SETH: I do remember that. Somehow, I just couldn't get the words out.

GUARDIAN ANGEL: You should thank me.

SETH: Thank you? Thank you?!

GUARDIAN ANGEL: She would've said no. Actually, it wouldn't have been that nice. It would've been more like, "Only in your dreams, Seth!" So, I saved you from yourself.

SETH: That's not true! Jennifer would've said yes!

GUARDIAN ANGEL: Sorry, buddy. But, no.

SETH: You don't know that! You're just some weird psycho person who's following me around for some unknown reason!

GUARDIAN ANGEL: Oh! Oh! Oh! Remember that time in junior high when you got stuck in the boy's restroom?

SETH: How do you know about that?

GUARDIAN ANGEL: Because I was the one holding the door shut, again saving you from a near disaster.

SETH: What disaster?

GUARDIAN ANGEL: The Wilson twins wanted to teach you a lesson. They were looking for you.

SETH: For that prank I pulled on them in the lunchroom?

GUARDIAN ANGEL: That's right. Dumb, dumb, dumb ... Replacing the white creamy middle of a chocolate sandwich cookie with toothpaste? Dumb, dumb, dumb ...

SETH: I was in junior high! junior high kids do dumb stuff!

GUARDIAN ANGEL: That's no exaggeration. Well, anyway, the Wilson boys were on their way to teach you a lesson, but I, being the observant and compassionate guardian angel that I am, spared you from getting a single scratch.

SETH: I'm not a coward!

GUARDIAN ANGEL: They would have eaten you for lunch.

SETH: No. I would've taken them down! Without a scratch on me.

GUARDIAN ANGEL: (Laughs.) Like Jennifer would have said, in your dreams.

SETH: Stop it! You weren't there!

GUARDIAN ANGEL: "Someone let me out! Please!" Good thing the Wilson twins didn't hear you screaming. "Someone help me! Help me! I can't breathe! I can't breathe in here!"

SETH: (Angry.) Who are you?

GUARDIAN ANGEL: And remember that time you tried to launch a homemade bottle rocket? Again, dumb idea. Dumb, dumb, dumb.

SETH: How do you know about that?

GUARDIAN ANGEL: Thanks to my bravery, that bottle rocket fizzled out on the ground instead of catching your parents' house on fire!

SETH: That was you?

GUARDIAN ANGEL: Plus, you would've caught your hair on fire.

SETH: But that rocket was for a science project. It was going to be so cool.

GUARDIAN ANGEL: Cool to suffer third degree bums over half your body?

SETH: But... you?

GUARDIAN ANGEL: Yep! Go me! I saved the day. As usual. Do you want to thank me now?

SETH: (Reaches out to touch him. ) Whoa! I can see you, but I can't feel you!

GUARDIAN ANGEL: I'm invisible too. Well, to everyone but you right now.

SETH: How is this possible?

GUARDIAN ANGEL: I thought a little gratitude was in order. You've put me through a lot, you know? Playing on the train tracks, the bull riding adventure, hang gliding over the cliffs with your own contraption, shark hunting ... Oh, and remember that time you had the great idea to jump into a swimming pool... with no water!

SETH: I was going to land on a mattress! Well, that was the plan.

GUARDIAN ANGEL: Two words, major head injury.

SETH: That's three words.

GUARDIAN ANGEL: Whatever.

SETH: Oh, great! I have a guardian angel with an attitude.

GUARDIAN ANGEL: Learned it from you. So, how about a little gratitude here? You've made my job very difficult, you know?

SETH: How about this? I free you. You are free to leave me and look after someone else.

GUARDIAN ANGEL: Really? You really want to live your life without a guardian angel?

SETH: I'll be fine.

GUARDIAN ANGEL: I wouldn't count on it. Not with all your great ideas!

SETH: I'm sure. Your services are no longer needed. So, poof and be gone! (Pause.) Go, I said! (GUARDIAN ANGEL pushes him.) Why did you do that?

GUARDIAN ANGEL: One last time for old time's sake. You know, pushing you out of the way of dangerous situations.

SETH: Well, your services are no longer needed!

GUARDIAN ANGEL: I wouldn't be so sure about that, if I was you. Because this afternoon ... well, never mind. (Turns to go.)

SETH: What? What?

GUARDIAN ANGEL: Maybe you can join my team after today. Become a guardian angel. I wonder who you'll get to follow around all day? (Points.) Maybe him.

SETH: Him? That old man with the tattoo?

GUARDIAN ANGEL: (Points.) Or her.

SETH: The mother of three?

GUARDIAN ANGEL: And no sleeping on the job. You must be alert at all times.

SETH: Why would I become a guardian angel this afternoon?

GUARDIAN ANGEL: Well, since you've let me go ... and after the upcoming incident this afternoon ... (Pats him.) Maybe you'll be on my team! Team 472013. That's my team. And might I add, we've had one of the least mistakes known to human kind.

SETH: Mistakes?

GUARDIAN ANGEL: Late interferences. Not paying attention and saving people in time.

I take my job very seriously! Well, most of the time. I did fail you once. Remember that choking incident when you were eating the breakfast burrito? I clearly was not paying attention. Thank goodness your friend Joe stepped in. A little Heimlich maneuver and you were good to go. Sorry about that.

SETH: What were you doing?

GUARDIAN ANGEL: Talking to my friend, Cosima. She has the most beautiful long hair, big beautiful eyes, a smile to die for ... Well, not you. I keep you from that. But, wow, does she make my heart flip-flop. So, my heart was flipflopping while you were choking on your burrito. Again, sorry about that.

SETH: Well, like I said. Your services are no longer needed. I can take care of myself, thank you very much.

GUARDIAN ANGEL: Well, okay, then. I'm out of here. (EXITS.)

SETH: (Calls OFF) Great. See ya. (Thinks.) But ... I wonder what's going to happen to me this afternoon. Something's supposed to happen. Well, that's just dumb. I'm being dumb. Nothing is going to happen. (Thinks. Calls OFF) Wait! Wait! Come back! I've changed my mind about firing you. Come back! (Thinks.) I know! I'm going to go home, crawl into bed, put the sheets over my head, and stay there all day! (Rushes OFF)

GUARDIAN ANGEL: (ENTERS, having not heard SETH.) What does he think he's doing? He can't fire me! And when that ceiling fan breaks loose from the ceiling, I'll be there to spare his life. Again. As always. Over and over again. Go me. (Sighs.) I need a raise. (Starts to run OFF after SETH.) Wait for me! You can't get through your life without me!
```

---

## IC-0796: He/She/It?

- Title: He/She/It?
- Author (byline): Jan Baross
- Work: More One-Act Plays for Acting Students
- Publisher: Meriwether Publishing
- Publication date as stated: July 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SHE, HE
- Teaser before the introduction: No
- Spoken words (computed): 1071
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jan Baross
Book: More One-Act Plays for Acting Students
ISBN: 1566080878
Publisher: Meriwether Publishing
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
HE: (as if talking to a child) When a mommy and a daddy love each other VERY much.

SHE: (bluntly) But the mommy doesn’t want to be a mommy.

HE: (earnestly) And the daddy desperately wants to be daddy

SHE: (sarcastically) The daddy goes off and finds a . . . replacement mommy.

HE: (sympathetically) But the daddy still loves the mommy very much.

SHE: (admitting) And the mommy still loves the daddy very much.

HE: (hopefully) So…

SHE: (smiling)They work things out.

BOTH: He/She/It? By Jan Baross
```

### Performance text (classify this)

```text
(SHE enters nervously. HE sits reading. Both are intense and fighting to keep themselves and each other under control.)

SHE: Is she here yet?

HE: Calm down, will you?

SHE: This is calm. You know this is calm. You know this is what calm looks like when I do it. [hearing something off stage] That's her.

HE: That's a car.

SHE: So? She doesn't drive?

HE: She's coming by bus. She'll get off at the corner and ...

SHE: Walk into our lives and surround us like a big blue mountain range.

HE: It'll just be a talk. A small talk.

SHE: A mountain range is coming for tea. How do you talk small to a mountain range?

HE: You promised to give it a chance.

SHE: Alright! What do you want? You want ...

HE: Small talk. Nothing beyond a chat.

SHE: My stomach is clenched. I can't talk with a clenched stomach.

HE: Nothing has been decided. Nothing. It's really up to you.

SHE: Oh, suddenly it's up to me!

HE: Just say "no," and the whole thing is off.

SHE: Just say "no."

HE: "No." It's simple.

SHE: (Quietly) No.

HE: What?

SHE: I said, no!

HE: Don't panic!

SHE: No!

HE: What do you mean, when you say "no"?

SHE: You said I could say it and it would all be over.

HE: Is that what you're really saying?

SHE: How many ways are there to say it! No. No. No!

HE: You can't mean that. You haven't even met her.

SHE: It's not no to her. It's no to you. This is all about you.

HE: Is that what you think?

SHE: Do you know what happened the last time I said no to you?

HE: (Pause) Well, what?

SHE: I didn't see you for two years.

HE: A long weekend. Christ. Your memory.

SHE: Alright, a long weekend that lasted two years. Because I said no.

HE: Because I want a child!

SHE: I don't.

HE: I know.

SHE: And if I say no to this new plan, you're gone again. With her.

HE: No. I promise to stay.

SHE: You'll resent me.

HE: I'll get over it.

SHE: Over what? What are we talking about?

HE: A baby. Mine.

SHE: So. Go marry her.

HE: She won't marry me.

SHE: You asked her to marry you?!

HE: No. She announced it when we met. She doesn't want to marry, period.

SHE: That's how she starts her conversations? Hello, I won't marry you.

HE: Pretty close.

SHE: She just wants your . . . ?

HE: My baby.

SHE: My husband's baby.

HE: Ah baby, you're my wife. I love you.

SHE: And her!

HE: In a way.

SHE: What way?

HE: She's motherly. No. Nurturing.

SHE: I'm not?

HE: You are, in your fashion.

SHE: But she'd be a better mother for your child?

HE: Our child. All three of us.

SHE: We all call her Mom?

HE: We've talked about artificial insemination.

SHE: We? Who? Her?

HE: And me.

SHE: And where was I?

HE: On our minds every minute. We don't want to hurt you.

SHE: (Beat) Hold onto that thought.

HE: She has the baby. She lives next door. That's all.

SHE: Next door?

HE: That's why it's important that you like her.

SHE: I don't want to like her. I don't even like you at this moment!

HE: Do you want me to leave?

SHE: Did I say that? I said I don't like you at this moment. This moment is over. It is now that moment. I'll die if you leave me again.

HE: I was miserable without you.

SHE: What can we do?

HE: We'll visit with her and the baby several times a week. That's all it amounts to.

SHE: For God sakes!

HE: It won't take anything away from you.

SHE: Except you.

HE: You've got me. I'm not going anywhere.

SHE: Except next door.

HE: (Intensely) I've got you and I'll never let you go.

SHE: You'll never let me go?

HE: I love you so much, it makes me tremble.

SHE: That's terror.

HE: I'm trying to be honest...

SHE: You've always been honest about what you want. I know exactly who you are, and it scares me.

HE: I've got room in my heart for more, that's all.

SHE: How much more? Are we going to adopt Czechoslovakia?

HE: Sweetheart.

SHE: I can't give you everything you want! I don't even want to.

HE: I know.

SHE: We'd be terrible parents.

HE: Absolutely!

SHE: We need parents.

HE: Absolutely.

SHE: (Desperately) Oh, Yes! Yes! I want to give you a baby! Is that what you want me to say?

HE: No. I don't want you to be the baby's mother.

SHE: (Terribly hurt) I'll be nurturing!

HE: Sacrificing won't work. You'd hate the pregnancy, your figure, the demands, time away from your career. And then you'd hate me.

SHE: Just like you'll hate me if I say no. What's she like?

HE: I told you.

SHE: Not like me.

HE: She's not as attractive as you are. (Beat) She's kind.

SHE: Not like me.

HE: The world needs career people too.

SHE: She can't do what I do.

HE: That's right. Your work is very unique.

SHE: But you prefer that heifer!

HE: Where do you get off insulting a woman because she's nice?!

SHE: (Overlap) Mooooo!

HE: (Overlap) You’re hopeless! Don't you malign kindness because you don't understand it. Not everyone's a paranoid like you!

SHE: You want to leave me! Admit it!

HE: She was right. She said you'd throw a fit! We knew you'd ...

SHE: Oh, excuse me for being paranoid!

HE: Stop it, Hon! Stop it! You're doing this crazy stuff to us again.

SHE: What?

HE: What do you really want? Bottom line.

SHE: You. All to myself. You. Not wanting a baby. You. Not hating me for saying no. You and me. That's all.

HE: That's all I want. You and me.

SHE: And baby makes three. And Mamma makes four.

HE: Alright! Alright! Maybe I can't have everything!

SHE: My God! Did you really say that?

HE: Forget everything I said.

SHE: What? You don't really mean it.

HE: Maybe it's a passing thing, you know, wanting to be a father.

SHE: Now, hey.

HE: I lost my passion for sailing.

SHE: You got seasick.

HE: Maybe I can make myself seasick when I think of babies.

SHE: Is she the only solution?

HE: She's the only woman I ever met who wants my child and doesn't want to get married.

SHE: And you're the only man she knows who wants her to have his child and doesn't want to marry her.

HE: Right.

SHE: Thank God you found each other.

HE: Funny how things work out.

SHE: Listen! Is that the bus?

HE: Yes.

SHE: Well?

HE: Will you talk to her?

SHE: Did we ever dream we'd be this adult? (Knocking)

HE: She's knocking.

SHE: (Angrily) Why doesn't she use the doorbell?

HE: Broken.

SHE: (Angrily) You still haven't fixed it?

HE: Priorities.

SHE: It's been broken a long time!

HE: Yes, a very long time.

SHE: You should fix it!

HE: (Beat) We both should fix it.

SHE: (Beat) You and me? (Pause. Softens) A project for two?

HE: Just for two.

SHE: (Smiles) We've always fixed it before.

HE: (Laughs.) We've got so much invested in the thing.

SHE: Will you really try?

HE: With all my heart.

SHE: (Relief) Thank God! I love you.

HE: I love you. (Pause. Softly) Darling.

SHE: Yes?

HE: Would you mind answering the door?
```

---

## IC-0797: Hearing Aid

- Title: Hearing Aid
- Author (byline): Pete Barry
- Work: Plays for Two, Pgs 374-382
- Publisher: Knopf Doubleday Publishing Group
- Publication date as stated: Mar 2014
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: OLD WOMAN, OLD MAN
- Teaser before the introduction: No
- Spoken words (computed): 978
- Already set (do not supply): none

### Source block (context only)

```text
Author: Pete Barry
Book: Plays for Two, Pgs 374-382
ISBN: 978-0345804549
Publisher: Knopf Doubleday Publishing Group
Date (Month/Year): Mar 2014
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Getting older means things stop working without warning.

ACTOR: Hearing fades. Backs ache. Knees negotiate every movement.

ACTRESS: Simple conversations become obstacle courses.

ACTOR: A single sentence can trigger confusion, accusation, or emotional collapse.

ACTRESS: Often all three.

ACTOR: What happens when a quiet evening at home quickly turns into a full-scale argument?

ACTRESS: This couple navigates the hazards of “aging together” and decades of shared history with . . .

ACTOR: No hearing. No filters and no patience.

BOTH: Hearing Aid by Pete Barry
```

### Performance text (classify this)

```text
Two loud, competing noises: a melodramatic TV show and Bach's Goldberg Variations. She listens to the radio, her ear up against the speaker. He watches TV, squinting.

OLD WOMAN: (Pgs 374-382) (turns the music down a little. She removes her hearing aid and checks it) Battery's dead.

OLD MAN: Is he? I knew he'd come to no good.

OLD WOMAN: What?

OLD MAN: What'd they do, shoot him?

OLD WOMAN: (indicating the radio) It's not Schubert, it's Bach.

OLD MAN: Who's back?

OLD WOMAN: Whose back? Your back?

OLD MAN: (indicating the TV) Jerry Orbach hasn't been on for years. This is CSI.

OLD WOMAN: See whose eye?

OLD MAN: No, I haven't seen Jose. I thought you were talking about Barry.

OLD WOMAN: I was what?

OLD MAN: You said, "Barry's dead."

OLD WOMAN: It's nothing to be embarrassed about, your back.

OLD MAN: I'm not harassing you about it. I'm just asking.

OLD WOMAN: You get old, things don't work so well anymore. (turns off the radio)

OLD MAN: Ah, come on, now, I missed half of what this girl was talking about. I can't figure this show out.

OLD WOMAN: I'd better go make dinner. (starts off toward the kitchen)

OLD MAN: If you're going in the kitchen, bring me a cold Heineken.

OLD WOMAN: (shoots him a quizzical look) What?

OLD MAN: Wouldja just bring me a Heineken?

OLD WOMAN: What for?

OLD MAN: Not four! Just one!

OLD WOMAN: I'm going as fast as I can.

OLD MAN: What d'ya think I am, some kind of alcoholic? (She goes. He yells at the TV) I can't watch this garbage anymore. I'm gonna do the crossword. (switches off the TV and gets the newspaper and a pencil. He counts.) 13? Hey! 13 letters! What's a 13-letter word for "nearly deaf"?

OLD WOMAN: (off) What's the question?

OLD MAN: NEARLY DEAF!

OLD WOMAN: (off) "BANK OF AMERICA"!

OLD MAN: (pause) Well, it's 13 letters.

OLD WOMAN: (returns, empty-handed) You shouldn't sit there watching TV all day if it's gonna make you this cranky.

OLD MAN: What happened to my beer?

OLD WOMAN: You shaved it off six months ago.

OLD MAN: You don't have to save beers. It's not like there's a shortage or something.

OLD WOMAN: It was never very long. You weren't like a Nazarene.

OLD MAN: What?

OLD WOMAN: You know, like Jesus grew it.

OLD MAN: (sarcastic, indignant) That's a real nice thing to say!

OLD WOMAN: It's historical.

OLD MAN: I'm not getting hysterical!

OLD WOMAN: What's the matter?

OLD MAN: You're crazy, that's what!

OLD WOMAN: Then turn up the thermostat!

OLD MAN: I'm like a big joke. (OLD WOMAN seems surprised at this, but considers it. She sniffs the air) A target for stray insults. A waste of space doing the crossword. Nobody even listens to a word I say. Like I'm talking to the wind. (continues to sniff the room. shrugs)

OLD WOMAN: (continues to sniff the room. shrugs) I don't smell anything. But I can't hear anything, either, I guess. Are you sure? (He stares at her, blankly. She sniffs again)

OLD MAN: What are you doing?

OLD WOMAN: You smelled cigar smoke?

OLD MAN: What about cigar smoke?

OLD WOMAN: You said you smell cigar smoke?

OLD MAN: WHAT ABOUT CIGAR SMOKE?

OLD WOMAN: YOU SMELL CIGAR SMOKE?

OLD MAN: I DON'T SMELL CIGAR SMOKE.

OLD WOMAN: YOU SAID YOU SMELL CIGAR SMOKE.

OLD MAN: I SAID I DON'T SMELL CIGAR SMOKE!

OLD WOMAN: Why are you yelling?

OLD MAN: If I don't yell you don't listen to me!

OLD WOMAN: I can't listen if you don't talk to me!

OLD MAN: I'm talking to you right now!

OLD WOMAN: You're not talking, you're yelling!

OLD MAN: What do you want me to do?

OLD WOMAN: Stop yelling and say something!

OLD MAN: Say what?

OLD WOMAN: Say anything!

OLD MAN: HOW MUCH WOOD COULD A WOODCHUCK CHUCK IF A WOODCHUCK COULD CHUCK WOOD!

OLD WOMAN: You don't have to be vulgar.

OLD MAN: Are you ever gonna get me a Heineken?

OLD WOMAN: Were you serious?

OLD MAN: Why would I want cereal with a Heineken? Do you mean poured over the cereal?

OLD WOMAN: Whatever you want.

OLD MAN: That's the worst thing I've ever heard of. Never mind. I'll take my comfort in the crossword puzzle. (She goes. He tries the crossword again) Four down. "One-eyed Rat Packer." "Sammy." What? Seven letters. Uh. "Davis"? No. "Junior"? What? Four down. "One-eyed Rat Packer." That's "Sammy"! What's wrong with this puzzle? Four down, "One-eyed Rat Packer"! Seven letters! Am I insane? FOUR DOWN, "ONE-EYED RAT PACKER"! Oh, four across. (fills it in)

OLD WOMAN: (rolls in a gold-painted shop window mannequin) Were you saying you were going to design and build a four-man juice squeezer?

OLD MAN: What the hell is that?

OLD WOMAN: [A mannequin.] You asked for it.

OLD MAN: Are we opening a boutique?

OLD WOMAN: What about Little Bo Peep? Is that a clue in the crossword?

OLD MAN: (yelling) So, I'm doing the crossword! Is that a crime?

OLD WOMAN: You're yelling again!

OLD MAN: Does that give you the right to make a mockery of me?

OLD WOMAN: "The right maid to muck around with"? What does that mean?

OLD MAN: I'm not here for your entertainment, for your merriment!

OLD WOMAN: You made a mistake ... marrying me?

OLD MAN: No, I don't need a steak marinade!

OLD WOMAN: 'Cause you know, I coulda done better!

OLD MAN: Oh, I'm a dumbbell, am I?

OLD WOMAN: You don't appreciate what you've got!

OLD MAN: Oh, I'm a breezy-eight used car, am I?

OLD WOMAN: You'd be lost without me! You'd destroy the closets, burn the laundry, shatter the glasses, let mold grow everywhere! You'd call strange people at all hours of the night! You'd spin out of control! You wouldn't get a nice dinner, I'll tell you that! You can't even make a fried egg!

OLD MAN: Shows what you know! It's not Friday! It's Thursday!

OLD WOMAN: If you're thirsty, then go get yourself a Heineken! (collapses in tears)

OLD MAN: Hey. Hey now. What's wrong?

OLD WOMAN: This marriage is not working anymore. After 42 years, it breaks my heart to say it. We don't communicate. I'm leaving.

OLD MAN: If you're freezing, then turn up the thermostat. (She turns to leave) Wait! Wait a minute. (She stops) There's something wrong here and I just don't understand what.

OLD WOMAN: Well, I can't stand it either.

OLD MAN: We talk and the sentences don't fit together.

OLD WOMAN: It has become like a prison sentence.

OLD MAN: Everything I say gets all twisted around. Either I'm not saying what I mean or you're not hearing what I say. And I can't figure it out and it makes me hate everything.

OLD WOMAN: I can't hear what you're saying, I'm too upset.

OLD MAN: What'd you say? I didn't hear you.

OLD WOMAN: (points to the radio) I used to love music so much. I can't hear it anymore. I hear sounds, but they're not distinct. There's no rhythm or pitch. It's all noise. It was such a joyous part of my life and now it's gone. It's infuriating. And it just makes it worse when you yell at me for something I can't help. So why should I stay, just to get yelled at? (He looks from her to the radio, really trying to understand, but clearly lost) You can't hear a word I'm saying. Forget it. (turns to leave)

OLD MAN: Wait! (She turns back. He turns on the radio)

OLD WOMAN: I just told you I can't hear it.

OLD MAN: What?

OLD WOMAN: I CAN'T HEAR IT!

OLD MAN: NEITHER CAN I! (begins to dance. He is awkward, totally off the rhythm, but he commits to it wholeheartedly. She manages an unenthusiastic smile. He beckons to her)

OLD WOMAN: I can't dance to it. I can't hear it.

OLD MAN: Come on. C'mere. (She goes, reluctantly. They sway together. He puts his lips up to her ear. Softly) Can you hear this?

OLD WOMAN: Yes.

OLD MAN: How about (whispers in her ear)

OLD WOMAN: (smiles) Yes. (He whispers again. She giggles. She whispers in his ear. He laughs, a loud hearty laugh. They engage in a merry whispering conversation while dancing to a beat)
```

---

## IC-0798: . Heart in the Ground

- Title: . Heart in the Ground
- Author (byline): Douglas Hill
- Work: Not specified
- Publisher: Theatre History.com
- Publication date as stated: 1996
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: LEE, KAREN
- Teaser before the introduction: Yes
- Spoken words (computed): 3171
- Already set (do not supply): none

### Source block (context only)

```text
Author: Douglas Hill
ISBN: Unavailable
Publisher: Theatre History.com
Date(Month/Year): 1996
CAUTION: Professionals and amateurs are hereby warned that Heart in the Ground is subject to a
royalty. It is fully protected under the copyright laws of the United States of America, and of all
countries covered by the International Copyright Union (including the Dominion of Canada and
the rest of the British Commonwealth), and of all countries covered by the Pan-American
Copyright convention and the Universal Copyright Convention, and of all countries with which the
United States has reciprocal copyright relations. All rights, including professional and amateur
stage performing, motion picture, recitation, lecturing, public reading, radio broadcasting,
television, video or sound taping, all other forms of mechanical or electronic reproduction, such
as information storage and retrieval systems and photocopying, and the rights of translation into
foreign languages, are strictly reserved.
Inquiries concerning all rights should be addressed to the author at doug.hill@ccmail.nevada.edu
```

### Introduction (context only: never use it for content warnings)

```text
When death comes without warning, the shock and disbelief can be overwhelming. It is never in the natural order of things for a child to die before his or her parents, and this can be especially intense when the death is sudden and/or violent. There is no opportunity to prepare, resolve misunderstandings, or “say good-bye.” Life for the parents and siblings is changed forever, often in an instant, and it takes time for the reality of what has happened to sink in. Heart in the Ground by Douglas Hill
```

### Performance text (classify this)

```text
[Lights up on a small table in the dining room of an old farmhouse. It is modestly set for the evening meal. KAREN ENTERS with a plate of sliced bread in one hand and the butter dish in the other LEE ENTERS behind her. He seats himself at one end of the table and she crosses to the other end. There is black dirt under her fingernails.]

LEE: Your brother will be out here as soon as he sees that hole. You hear me—about Bill? [KAREN doesn't look at him and remains still for a moment. He picks up his cup to take a drink and then realizes it's empty. KAREN puts the food on the table and EXITS back to the kitchen. LEE watches her go.] And this is gonna be the last time, right? You're not planning to keep this up all summer, are you? [Silence.] I've got a meeting with my…you remember my meeting next week, don't you? [Silence.] You know, I tore the pocket out of my shirt climbing over that fence. [LEE takes a slice of bread, cuts a square of butter, and starts to butter the bread. He keeps watching the kitchen doorway. The butter is hard and it tears the bread. Finally, the bread is destroyed and he tosses it to the table, rises, and crosses to the doorway. Immediately KAREN ENTERS with a pitcher of iced tea. They almost collide. She says nothing and crosses past him to the table. She pours his glass and then sits down at her spot. LEE sits down again and drinks half of his glass.] I was hoping you might be able to sew up the pocket on my shirt. [Beat. No response from her.] I saw that the kitchen needs to be swept. The laundry did get folded but it didn't get put away—

KAREN: I know. I'll take care—

LEE: And you forgot to take the butter out again.

KAREN: I didn't forget.

LEE: The point is, you're needed here at the house of an evening. It's your responsibility, Karen, and I'm not going to—

KAREN: I know, but right now—

LEE: I'm not gonna try and run this farm all by myself. I can't drop everything to pick up after you and I can't keep chasing you all over God's green earth. Just stay away from the cemetery and take care of things here. All right? Leave her alone. From now on. Take care of things here.

.

KAREN: Lee, I'm trying but I can't concentrate—

LEE: Please, just stay home and do your chores. That's all.

KAREN: I can't think—I'm restless when I'm here and all the time I'm doing chores—

LEE: Well, that's just fine. Huh? I'm exhausted from burying her twice already this week. And now I get to do it again because you were restless. [Pause.]

KAREN: My baby belongs here—I don't care what Bill—

LEE: Karen—Karen! They got laws, okay? Codes and things. I don't know what all, but my hands are tied. They're not gonna let us bury her on land this close to the river. I talked with Bill yesterday, and he says there's not a blessed thing we can do. And he's not trying to pick on us. Those laws are for everyone in the county. [Beat.] I tried, all right? I really tried. [Pause.] So let's just eat. Can we do that?

LEE: You might want to wash your hands again before Bill gets here. It doesn't look too good, you know? [Pause.] Listen. When Bill gets here, I think it might be best if you stayed upstairs.

KAREN: Why?

LEE: Just until he's gone. It shouldn't take too long. [Beat.] If we need you, we'll call you.

KAREN: I'll be quiet. I promise. I won't say anything. I won't talk.

LEE: I'd just rather not have a scene like last time, okay? Then maybe you and I could . . . do something. Maybe take a walk. [Pause.]

KAREN: This is my house. And he's gonna have to look me in the eye before he walks out of here with her.

.

LEE: Karen, let me handle it. All you have to do is finish your supper and go upstairs for awhile.

KAREN: What are you gonna do—Invite him in? Let him walk all over us and take whatever he wants? Is that how you'll—

LEE: Karen, I'll handle it.

KAREN: I know, but he's got no right to tell us how to—

LEE: I SAID. . ! [Beat.] We're not gonna break the law. I won't do it.

KAREN: You're not going to fight him for—

LEE: We won't win. And you know it. Look, if I were the sheriff, I'd say go ahead. I know you're crazy but I don't care. All right? If I had the law in my hands, you could break the rules and no one would say a word. And the farm would be safe, and you could have everything just the way you want it. But you know something? For the past couple of days you've done nothing but run around acting stupid and backing us into a corner until we've got no other choice and now we're stuck! I'm stuck! And so are you! And we can't do anything about it! Because I'm not the sheriff, your brother is. And I don't have the law in my hands—he does. Hell, I don't even have it on my side right now, thanks to you! So if you really care about this house and the farm and your family, you'll finish your supper, go upstairs, and stop the goddamn digging! [After a moment, KAREN looks down at her untouched food and stands up. She gathers her silverware in one hand and her plate in the other. She EXITS into the kitchen. LEE stands up and crosses to the kitchen doorway.] I don't mean you have to go now. [Beat.] Karen, all I'm saying is that we can't—

KAREN: [Beginning to tremble.] I know well enough how to take care of my house. Don't think you have to give me any advice in those areas.

LEE: Don't take that tone of voice with me. I'm not the one—

KAREN: Oh good. One more thing to do. Fix your shirt, take the butter out before supper, and change my tone of voice. I believe that's the list as it stands, ain't it? [Again, she starts to EXIT.]

LEE: Karen, stop! [Beat.] I didn't say you had to go up right this minute.

KAREN: I'm going to sit outside.

LEE: Would you sit here with me? Please?

.

KAREN: I need some fresh air.

LEE: If Bill finds you out back, he's not going to— [KAREN savagely picks up his knife and slams it down on the table. She slams it down again. LEE grabs her hand and forces it to the table to stop her.] Bill wants to take you back to Marshall Valley again. Did you know that? [She wrenches her hand away.]

KAREN: Why are you so afraid of him?

LEE: He thinks you need to see a doctor anyway. And if you keep acting like this, he'll take you for sure.

KAREN: It don't matter what I act like. Lee, I could be as sane as day and that wouldn't stop him from trying. He wants all of us out of here. I know that. You, me—one by one if he has to.

LEE: He's doing his job, for crying out loud, and you're provoking him.

KAREN: He wants this farm. It doesn't have anything to do with my sanity or an empty grave. That's the only reason he's coming here tonight. So he can start kicking us out.

LEE: If you would just stay home, he wouldn't have a reason to come out here at all. But you keep breaking the law and acting like this and you're pulling him out here. That's what scares me. All he has to do is get one doctor to sign an order and you're back in the hospital. And the farm goes right to him, like it or not.

KAREN: He'll have to fight a lot harder for it. Momma left it to me.

LEE: Why do you have to fight him at all?

KAREN: Catherine belongs here.

LEE: That doesn't make any sense to anyone but you.

KAREN: There are weeds all over that cemetery. Weeds and stones. It's on the north side of the hill. And I've seen every possible rodent there is crawling along that road. When have you seen that cemetery with the gate shut? Lee, there's a million reasons. You can't even see it from our back porch. Godahmighty, what's wrong with you? I just think about it and my legs, my wrists, my jaw, every part of me starts hurting. How can you sit down to eat—she belongs here! Not with a bunch . . . a bunch of stones and strangers, I swear, I don't even know that part of the earth. God don't even go there.

.

LEE: You act like this in front of Bill and he'll have you—

LEE: I can't do anything about Bill. KAREN: Bill just wants to take the farm. And if you take his side, it's I'm not one his side, Karen. I just want gonna be that much easier for to know why you think you can break him to come and steal it from us. the law and nobody should care You can't be on his side and whether you do or not. All that does is expect him to leave us alone. get your brother's attention and put more pressure on us. You think that what I'm doing is wrong because Bill says it is. You No I don't. think that everything that comes out of his mouth is gospel law. I'm not ganging up on you. I'm trying to But for your information, my be—Karen, I'm trying to be on your brother is wrong, and you're side! wrong, and the whole county is wrong. And if it takes all of you to gang up on me It still doesn't prove that I'm not right.

KAREN: If you don't fight him, Lee, then you're not on my side. If you're going to be partners with Bill, then you're not good enough to be my husband or Catherine's father and you deserve everything that you get from Bill instead! And I hope all that dirt from Catherine's grave gets caught in your throat and you both choke to death on it!

LEE: Get out. [She turns around, surprised.] I said, get out! Go on. You're not going to blame me for this. [Lee throws a handful of food at her.] What kind of mother are you that you don't even wake up— [KAREN ducks and EXITS into the living room. LEE throws another handful of food.] —To check on a baby not even three weeks old! [He collapses into his chair. He stares at his food for a moment and then takes a tentative bite. He swallows and then folds his hands and bows his head for a moment. He is taking a drink when KAREN ENTERS with a shotgun. She does not have the gun pointed at him.]

KAREN: I'd forgotten that you get scared sometimes too. Just like everyone else does. Except you don't run. You stand still and wait for something to hit you. I guess you figure you can live through anything. I don't know if I can anymore.

.

LEE: Karen, I'm sorry. I'm just tired, I think. And it's hard for me to understand sometimes that you're . . . you're going through it, too. The same way I am. And I want to understand, but sometimes—

KAREN: It could have been you, Lee. If I had gone to Pettiston after those parts, it could have been you with her. You could've woke up next to her in bed.

LEE: I'm sorry. [Beat.]

KAREN: And with that sunrise coming in through the curtains, you would have sworn she was a sleeping angel. Wrapped up in a white sheet. Her face just— [She draws a breath.]

LEE: Why don't you go put up the gun. It's not loaded.

KAREN: I've got to do something now or I really will go crazy. And since Bill's coming over, I'm going to need it.

LEE: Karen, it's not loaded. And I hid the shells.

KAREN: [Nodding her head.] In with the Christmas decorations. I know. [Pause.]

LEE: Maybe we should . . . Wouldn't it be enough to go visit every day? We could both go. Whenever you needed. I'd go with you. If you want.

KAREN: But how long would you let me stay?

LEE: As long as you want.

KAREN: No you wouldn't.

LEE: [The faintest smile.] You could teach me how to sew my shirts. That'd keep me there awhile.

KAREN: Why don't you want her here with us?

LEE: It's not that I don't want her. I just don't want your brother and his deputies out here every other night. I don't need the law on my back, right now. There's a lot more at stake for me in this than you. I've got that meeting next week and if—

KAREN: So it's all about your parole? That's why you're scared of him?

LEE: No—

KAREN: That's why you're letting Bill do this? Lee . . . Shame on you.

.

[LEE is silent. KAREN EXITS into the kitchen. Quietly he follows her out. Lights down on the dining room and lights up on the back porch. It's made of wood and raised up off the ground by a step or two. One windowpane on the outside of the house is broken. KAREN ENTERS onto the porch. There is a crude and dirty box waiting there. In the background is the sound of crickets and cicadas. KAREN begins dragging the box away from the porch with one hand and holds the shotgun in the other. LEE ENTERS onto the porch.]

LEE: We can't go breaking the law.

KAREN: You aren't. I'm the only one doing anything.

LEE: If I let you go out there with her, Bill's gonna think I'm part of it.

KAREN: Tell Bill to mind his own business. Give him ten dollars see what he does.

LEE: We don't have ten dollars. We spent everything on tractor parts and burial plots. [Beat.] Karen, if you get put in jail or if they take you back to Marshall Valley, this farm becomes his business. And if Bill gets this farm, you don't think he's really gonna give it back to you, do you?

KAREN: He'll have to get past the shotgun first.

LEE: What are you gonna do—shoot out the window again?

KAREN: I won't be aiming at the window.

LEE: What you're doing is wrong. The courts aren't gonna—

KAREN: What I'm doing is not wrong. I know the difference, Lee.

LEE: But you're still breaking the law.

KAREN: Then the law is wrong. So throw the law in jail. But stay out of my way. [LEE takes a breath and spits it out.]

LEE: You're gonna make me tie you up in your room so we can at least look like a decent family out here?

KAREN: You do and I'll scream loud enough—I swear it—the floor will just rip open beneath your feet. [He crosses down to KAREN.]

LEE: Give me the gun.

KAREN: You stay away from me. I'll shoot.

LEE: Don't be stupid. Let me have it. [She lowers the box to the ground.]

.

KAREN: I mean it. You're not gonna stop me. [LEE picks up the box and carries it back to the porch.] Lee, don't! Please don't do this.

LEE: Catherine gets buried wherever they want her to be buried.

KAREN: She belongs here. [KAREN puts the shotgun down and runs to the box.] Please, Lee, I'm not crazy. You can't let him take us away. [LEE crosses down to get the shotgun. KAREN picks up the box and starts to EXIT with it.] I am a good mother!

LEE: The world is full of good mothers. Nobody cares.

KAREN: The world is full of criminals, Lee!

LEE: Put her down, Karen! I mean it. [LEE aims away from her and fires a shot. She instinctively drops the box to the ground and covers it with her body. There is a sudden silence.] You want Bill to find us like this? You want him to see you . . . Just go inside where you belong. Bill and I are going to take care of it. We don't need your help—you've got no reason to be out here like this. [Beat.] Get inside before Bill gets here.

KAREN: Bill is not your family—I am. And Catherine is. And this farm. This is where we—We don't belong in there. We're out here. In the ground. We're out here eating away at all your time and attention. And you don't even want to touch us. Lee this is your family. We're swallowing up all your prayers and begging you to come out here and dance barefoot with us in the dirt. And don't you look at me like I'm stupid! I'm not. I know how lucky I am to be here! And you better not forget how lucky you are too! [Beat.] I got a second chance after Marshall Valley to come back here. Because this is where I belong. And you got a second chance after your parole because you belong here too. And so does Catherine. And I'm not fourteen anymore, and you're not gonna give my child away like Momma did. I'm old enough to be having children of my own now. I'm twenty-two and I'm married, so Catherine is legitimate this time, and I know a lot more than I did back then. She's not going to anyone else. She's staying with me. [Pause.] If you have to send something out to that graveyard, send flowers, or a promise, or an IOU. I don't care. But don't take away my baby. I just want her back. That's all. Send someone else to the cemetery, I want my little girl. [LEE lowers his shotgun and leaves it standing by the door.]

LEE: You had a baby before Catherine? [Beat.] Why didn't you…You never—

KAREN: That's why Momma gave the farm to me. After Marshall Valley. [Silence.] Please don't leave me.

.

LEE: No. [Pause. LEE nervously looks around himself and then up at the sky. Finally, he crosses down the steps and pulls a toolbox out from underneath. He motions for her to come to him as he kneels down.] I promise. Catherine won't leave here. Ever. [She crosses toward him.] I need you to go pick as many ears of corn as you can carry.

KAREN: It's not ripe yet.

LEE: I know. I promise. She'll stay here with us.

[KAREN leaves the box beside LEE and quickly EXITS into the cornfield. LEE begins prying the top of the box with a curved claw hammer. KAREN ENTERS with her arms full of corn. She leaves them in a pile next to LEE. LEE takes the top off the box and lays it aside. Gingerly, he pulls out a small bundle wrapped in several pastel blankets and hands it to KAREN. He takes off his shirt and wraps several ears of corn in it. He places the bundle of corn into the box and begins nailing the lid back on. The lights fade.]
```

---

## IC-0799: Her Heart (from Almost, Maine)

- Title: Her Heart (from Almost, Maine)
- Author (byline): John Cariani
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: June 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: EAST, GLORY
- Teaser before the introduction: No
- Spoken words (computed): 1647
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Cariani
ISBN: 978-0822221562
Publisher: Dramatists Play Service
Date (Month/Year): June 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: It is a cold Friday night in the middle of winter in a small, mythical town in northern Maine called Almost, Maine.

ACTOR: Glory is standing in the front yard of an old farmhouse, clutching a small brown paper grocery bag to her chest and looking up at the sky.

ACTRESS: A porch light comes on. We hear a screen door open and slam as East enters. He watches Glory for a while.

ACTOR: A field of stars – a clear, cold, moonless northern night sky – serves as the backdrop for

TOGETHER: Almost, Maine by John Cariani
```

### Performance text (classify this)

```text
HER HEART

EAST: Hello.

GLORY: (To him.) Hello. (Resumes looking to the sky.)

EAST: I thought I saw someone. (Little beat.) I was about to go to bed. I saw you from my window . . . (Beat.) Can I - ? . . . Is there something I can do for you?

GLORY: (To him.) Oh, no. I’m just here to see the northern lights. (Back to the sky.)

EAST: Okay. Okay. It’s just – it’s awful late and you’re in my yard . . .

GLORY: Oh, I hope you don’t mind! I’ll only be here tonight. I’ll see them tonight. The northern lights. And then I’ll be gone. I hope you don’t mind –

EAST: (Looking out.) Is that your tent? (The tent should be seen by East and Glory – not by the audience.)

GLORY: Yes.

EAST: You’ve pitched a tent . . . In my yard . . .

GLORY: So I have a place to sleep, after I see them, I hope you don’t mind.

EAST: Well, it’s not that I –

GLORY: Oh, no, I think you mind!

EAST: No, it’s not that I mind –

GLORY: No, you do! You do! Oh, I’m so sorry! I didn’t think you would! I didn’t think -- You see, it says in your brochure

EAST: My brochure?

GLORY: That people from Maine wouldn’t mind. It says (Pulling out a brochure about Maine tourism.) that people from Maine are different, that they live life “the way life should be,” and that, “in the tradition of their brethren in rural northern climes, like Scandinavia,” that they’ll let people who are complete strangers like cross-country skiers and bikers and hikers, camp out in their yard, if they need to, for nothing, they’ll just let you. I’m a hiker. It is true?

EAST: Well –

GLORY: That they’ll just let you stay in their yards if you need to? ‘Cause I need to. Camp out. ‘Cause I’m where I need to be. This is the farthest I’ve ever traveled – I’m from a part of the country that’s a little closer to things – never been this far north before, or east, and did you know that Maine is the only state in the country that’s attached to only one other state?!?

EAST: Um –

GLORY: It is!! (Taking in all the open space.) Feels like the end of the world, and here I am at the end of the world, and I have nowhere to go, so I was counting on staying here, unless it’s not true, I mean is it true?

EAST: Well –

GLORY: Would you let a hiker who was where she needed to be just camp out in your yard for free? I mean, if a person really needed to, really really needed to?

EAST: Well, if a person really needed to, sure, but –

GLORY: (Huge relief!) Oh, I’m so glad, then! Thank you! (She goes to East, throw her arms open, and hugs him. In the hug, the bag gets squished between their bodies. When they part, East is holding Glory’s bag. The exchange of the bag is almost imperceptible to both of them, and to the audience. Immediately after hugging East, Glory resumes looking intently for the northern lights. Beat. Then, realizing she doesn’t have her bag:) Oh, my gosh! (Realizing that East has her bag.) I need that!

EAST: Oh. Here. (He gives it back.)

GLORY: Thank you. (She resumes looking to the sky.)

EAST: Sure. (Beat.) Okay -- Okay . . . (Beat.) So you’re just lookin’ for a place to see the northern lights from?

GLORY: Yeah. Just tonight.

EAST: Well, you know, you might not see ‘em tonight, ‘cause . . . you never really know -

GLORY: Oh, no. I’ll see them. Because I’m in a good place: Your latitude is good. And this is the right time: Solar activity is at an eleven-year peak. Everything’s in order. And boy, you have good sky for it. (Taking in the sky.) There’s lots of sky here.

EAST: Used to be a potato farm.

GLORY: I was gonna say – no trees in the way. And it’s flat! Makes for a big sky! (Beat.) So – you’re a farmer?

EAST: No. Used to be a farmer. I’m a repairman. Fix things.

GLORY: Oh. (Laughs.)

EAST: What?

GLORY: You’re not a lobster man . . . I guess I thought that everyone from Maine was a lobster man and talked in that funny . . . way like they do in Maine, and you don’t talk that way . . .

EAST: Nope. You’re not Down East. You’re up north. And this is how we talk up north, pretty much. Plus, ocean’s a couple hundred miles away. Be an awful long ride to work if I was a lobster man.

GLORY: (Enjoying him.) Yeah. Well, anyway, thank you. Thank you for letting me stay. I’ve had a bad enough time of things lately not to be given a bad time here –

(East, inexplicably drawn to her, kisses Glory. When they break, the bag has exchanged clutches imperceptibly – East has it. And now we have two stunned people.)

EAST: Oh …

GLORY: (Trying to figure out what just happened.) Um …

EAST: Oh, boy.

GLORY: Um …

EAST: I’m sorry. I just -- . . . I think I love you.

GLORY: Really.

EAST: (Perplexed.) Yeah. I saw you from my window and . . . I love you.

GLORY: Well . . . -- that’s very nice -- . . . but there’s something I think you should know: I’m not here for that.

EAST: Oh, no! I didn’t think you were!

GLORY: I’m here to pay my respects. To my husband.

EAST: Oh –

GLORY: Yeah: My husband. Wes. I just wanted to say goodbye to him, ‘cause he died recently. On Tuesday, actually, and, see, the northern lights – did you know this? – the northern lights are really the torches that the recently departed carry with them so they can find their way to heaven, and see, it takes three days for a soul to make its way home, to heaven, and this is Friday! This is the third day, so, you see, I will see them, the northern lights, because they’re him: He’ll be carrying one of the torches. And, see, I didn’t leave things well with him, so I was just hoping I could come here and say goodbye to him and not be bothered, but what you did there just a second ago, that bothered, me, I think, and I’m not here for that, so maybe I should go . . . and find another yard –

EAST: No! No! I’m sorry if I -- . . . if I’ve behaved in a way that I shouldn’t have -

GLORY: (Leaving.) No . . . I think –

EAST: No! I really don’t know what happened.

GLORY: Well, I do, I know what happened!

EAST: I’m not the kind of person who does things like that. Please. Don’t go. Just – do what you need to do. I won’t bother you. Maybe just . . . consider what I did a very warm Maine welcome.

GLORY: (Stopping; charmed.) All right. All right. (Beat.) I’m -- My name’s Glory.

EAST: I’m East. For Easton. It’s the name of the town – little ways that way – where I was born. Mess-up on the birth certificate . . . “a son, Easton, born on this sixth day of January, [insert year] in the town of Matthew, Maine” . . . instead of the other way around . . .

GLORY: (Amused.) Aw, I’m sorry . . . so, (Referring to the place.) Easton, yeah! I passed through near there on my way here, and, by the way, (Scanning the horizon.) where is “here,” where am I? I couldn’t find it on my map.

EAST: Um . . . Almost.

GLORY: What?

EAST: You’re in unorganized territory. Township Thirteen, Range Seven. (Glory checks her map.) It’s not gonna be on your map, cause it’s not an actual town, technically.

GLORY: What do you mean –

EAST: See, to be a town, you gotta get organized. And we never got around to gettin’ organized, so . . . we’re just Almost.

GLORY: Oh . . . (They enjoy this. Beat. Glory now deals with the fact that she is missing her bag. She was clutching it to her chest, and now it’s gone. This should upset her so much that is seems like it affects her breathing.) Oh! Oh!

EAST: What? What’s wrong?

GLORY: (Seeming to be having trouble breathing.) My heart!

EAST: What? Are you okay?

GLORY: My heart! (Seeing that he has her bag; pointing to the bag.)

EAST: What?

GLORY: You have my heart! In that bag, it’s in that bag!

EAST: Oh.

GLORY: Please give it back . . . please! It’s my heart. I need it. Please!

EAST: Okay, okay, okay. (He gives her the bag.)

GLORY: Thank you. (Her breathing normalizes.)

EAST: You’re welcome. (A long beat while East considers what he has just heard.) I’m sorry, did you just say that … your heart is in that bag?, is that what you just said?, that . . . your heart -- . . . ?

GLORY: Yes.

EAST: (Considers.) It’s heavy.

GLORY: Yes.

EAST: (Beat.) Why is it in that bag?

GLORY: It’s how I carry it around.

EAST: Why?

GLORY: It’s broken.

EAST: What happened?

GLORY: Wes broke it.

EAST: Your husband?

GLORY: Yeah, He went away.

EAST: Oh.

GLORY: With someone else.

EAST: Oh, I’m sorry.

GLORY: Yeah. And when he did that, I felt like my heart would break. And that’s exactly what happened. It broke: hardened up and cracked in two. Hurt so bad, I had to go to the hospital, and when I got there, they told me they were gonna have to take it out. And when they took it out, they dropped it on the floor and it broke into nineteen pieces. Slate. (Gently shakes the bag) It turned to slate. (Beat. She look back up at the sky.)

EAST: (Takes this in. Beat. His only response to what she has just told him is:) Great for roofing. (Glory just looks at East. Beat. Then:) Wait a second, how do you breathe? If your heart is in that bag, how are you alive?

GLORY: (Indicating the heart that’s now in her chest.) Artificial . . .

EAST: Really.

GLORY: Yeah. ‘Cause my real one’s broken.

EAST: Then – why do you carry it around with you?

GLORY: It’s my heart.

EAST: But it’s broken.

GLORY: Yeah.

EAST: ‘Cause your husband left you.

GLORY: Yeah.

EAST: Well, why are you paying your respects to him if he left you?

GLORY: Because that’s what you do when a person dies, you pay them respects –

EAST: But he left you,

GLORY: Yeah, but –

EAST: and it seems to me that a man who leaves somebody doesn’t deserve any respects.

GLORY: (Deflecting.) Well, I just didn’t leave things well with him,

EAST: (Pressing.) What do you mean? –

GLORY: and I need to apologize to him.

EAST: But he left you!

GLORY: I know, but I –

EAST: Why should you apologize?

GLORY: Because!

EAST: Because why?!?

GLORY: Because I killed him!

EAST: Oh. (This stops East; he backs off a bit.)

GLORY: And I’d like to apologize. (Beat. Then, admission:) See, he had come to visit me when I was in recovery from when they put my artificial heart in – I was almost better; I was just about to go home, too – and he said he wanted me back. And I said, “Wes, I have a new heart now. I’m sorry . . . It doesn’t want you back . . . “ And that just killed him.

EAST: (Relief.) Oh. But, it didn’t kill him, you didn’t kill him –

GLORY: Yes, I did! Because he got so sad that my new heart didn’t want him back, that he just tore outta the hospital, and . . . an ambulance that was comin’ in from an emergency didn’t see him and just . . . took him right out, and if I’d have been able to take him back,

EAST: Glory –

GLORY: he wouldn’t have torn outta there like that,

EAST: Glory!

GLORY: and been just taken out like that, and so, I just feel that, for closure, the right thing to do is (Inexplicably drawn to her, East kisses Glory. When she pulls away, he has her heart again. She takes it back.) Please don’t do that anymore.

EAST: Why? I love you!

GLORY: Well, don’t.

EAST: Why?

GLORY: Because I won’t be able to love you back: I have a heart that can pump my blood and that’s all. The one that does the other stuff is broken. It doesn’t work anymore. (Again, inexplicably drawn to her, East deliberately kisses Glory. Glory pulls away. East has her heart again. Glory grabs it from him; East grabs it right back.)

EAST: Please let me have this.

GLORY: (Desperately trying to get her heart back.) No! It’s mine!

EAST: (Keeping her heart.) I can fix it!

GLORY: I don’t know if I want you to!

EAST: Glory -- ?

GLORY: (Going after her heart.) East, please give that back to me!

EAST: (Keeping her heart.) But, it’s broken.

GLORY: Please -- !

EAST: It’s no good like this.

GLORY: But, it’s my heart, East!

EAST: Yes, it is. And I believe I have it. (This stops Glory. Beat.) And I can fix it. (Beat.) I’m a repairman. I repair things. It’s what I do. (Beat. East crouches, gently places the bag on the ground and start to open it in order to examine its contents. As he opens the bag, music up, and the northern lights appear – in front of Glory, above Glory, on the field of stars behind Glory. Glory sees them … and they’re a thing of wonder.)

GLORY: Oh! Oh, wow! Oh, they’re so beautiful . . . (Remembering who they are.) Oh! Oh! -- Wes!! Wes!! Goodbye! I’m so sorry! . . . Goodbye, Wes! (And the northern lights – and Wes – are gone. Glory turns to East, who has taken a little piece of her heart out of the bag is examining it. Then:) Hello, East. (East looks at Glory, and then begins repairing her heart.)
```

---

## IC-0800: Here Come Da Judge from The Shack

- Title: Here Come Da Judge from The Shack
- Author (byline): William Paul Young
- Work: The Shack
- Publisher: Windblown Media
- Publication date as stated: July 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: WOMAN, MACK
- Teaser before the introduction: No
- Spoken words (computed): 2047
- Already set (do not supply): none

### Source block (context only)

```text
Author: William Paul Young
Book: The Shack
ISBN: 978-0964729230
Publisher: Windblown Media
Date (Month/Year): July 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Our story begins with Mackenzie "Mack" Phillips, a father suffering great pain because of the death of his young daughter at the hands of a serial killer.

ACTOR: Mack receives a note from "Papa" to meet him at the rundown shack in the woods where police had found evidence of his daughter’s murder six years earlier.

ACTRESS: Mack, who was raised by a hypocritical, vicious and abusive father who was also a pastor, already understands from previous experience that "Papa" is God.

ACTOR: The following scene occurs midway through the book after Mack has already met:

ACTRESS: (in the character of Papa) Papa -- a large beaming African-American woman;

ACTOR: (in the character of Jesus) Jesus -- a Middle Eastern man dressed as a laborer;

ACTRESS: (in the character of the Holy Spirit) And the Holy Spirit -- a woman of Asian ethnicity.

ACTOR: It is the Holy Spirit who walks Mack through

TOGETHER: “The Judgment”

ACTRESS: Here Come Da Judge from The Shack by William Paul Young
```

### Performance text (classify this)

```text
WOMAN: Do you understand why you are here?

MACK: You know . . . (quietly) I have no idea. No one told me.

WOMAN: (laughing) Well, Mackenzie Allen Phillips. I am here to help you. (Mack chuckles too, not even knowing or caring why). Today is a very serious day with very serious consequences. (pause) Mackenzie, you are here, in part, because of your children, but you are also here for . . .

MACK: (Interrupting) My children? What do you mean I’m here because of my children?

WOMAN: Mackenzie, you love your children in a way that your own father was never able to love you and your sisters. Some parents are too broken to love their children well and others are barely able to love them at all, you should understand that. But you, you do love your children well-very well. So then, Mackenzie, may I ask which of your children do you love the most?

MACK: (smiling) I don’t love any one of them more than any of the others. I love each of them differently. (choosing his words carefully)

WOMAN: Explain that to me, Mackenzie.

MACK: I remember after Jon, my first, was born. I was so captivated by the wonder of who this little life was that I actually worried about whether I would have anything left to love a second child. But when Tyler came along, it was as if he brought with him a special gift for me, a whole new capacity to love him specially.

WOMAN: Well said, Mackenzie! But what about when they do not behave, or they make choices other than those you would want them to make, or they are just belligerent and rude? What about when they embarrass you in front of others? How does that affect your love for them?

MACK: (slowly and deliberately) It doesn’t, really. I admit that it does affect me and sometimes I get embarrassed or angry, but even when they act badly, they are still my son or my daughter, they are still Josh or Kate, and they will be forever. What they do might affect my pride, but not my love for them.

WOMAN: (beaming) You are wise in the ways of real love, Mackenzie. So many believe that it is love that grows, but it is the knowing that grows and love simply expands to contain it. Love is just the skin of knowing. Mackenzie, you love your children, whom you know so well, with a wonderful and real love.

MACK: (embarrassed, looking down) Well, thanks, but I'm not that way with very many other people. My love tends to be pretty conditional most of the time.

WOMAN: But it's a start, isn't it, Mackenzie? And you didn't move beyond your father's inability on your own, it was God and you together who changed you to love this way. And now you love your children much the way Father loves his. (Mack’s anger rises, he tries to cover his emotions, but he is clearly angry) Hmmmmm. Something I said bother you, Mackenzie? (pause) Mackenzie? Is there something you would like to say?

MACK: Uh . . . . well, no! Not really

WOMAN: Mackenzie, this is a time for honesty, for truth. You don’t believe that Father loves his children very well, do you? You don’t truly believe that God is good, do you?

MACK: (snapping) Is Missy his child?

WOMAN: Of course!

MACK: Then, no! (unable to stay still – angry and ready to explode) I don’t believe that God loves all his children very well!

WOMAN: Mackenzie. Earlier, I began to tell you why you are here today. Not only are you here because of your children, but you are here for judgment. (Mack panics, feels guilty with no defense for his past sins) Mackenzie?

MACK: No I understand. I’m dead, aren’t I? That’s why I can see Jesus and Papa, cuz I’m dead. (pause) I can’t believe it! I didn’t even feel anything. (pause) How long have I been dead?

WOMAN: Mackenzie, I am sorry to disappoint you, but you have not yet fallen asleep in your world, and I believe that you have mis-

MACK: (cutting her off) I'm not dead? You mean all this is real and I'm still alive? But I thought you said I came here for judgment?

WOMAN: (matter of factly) I did. But, Macken-

MACK: Judgement? And I’m not even dead? (anger replacing his panic) This hardly seems fair! Does this happen to other people-getting judged, I mean, before they're even dead? What if I change? What if I do better the rest of my life? What if I repent? What then?"

WOMAN: (unfazed by his outburst) Is there something you wish to repent of, Mackenzie?

MACK: (shaking his head slowly) I wouldn’t know where to begin. I’m quite a mess, aren’t I?

WOMAN: (smiling) Yes, you are. You are a glorious, destructive mess, Mackenzie, but you are not here to repent, at least not in the way that you understand. Mackenzie, you are not here to be judged.

MACK: (interrupting again) But, I thought you said that I was . . .

WOMAN: . . . here for judgment? I did. But you are not on trial here. (Mack takes a deep breath, relieved) You will be the Judge!

MACK: What? Me? I’d rather not. (pause) I don’t have any ability to judge.

WOMAN: Oh, that is not true. (with a hint of sarcasm) You have judged many throughout your life. You have judged the actions and even the motivations of others, as if you somehow knew what those were in truth. You have judged the color of skin and body language and body odor. You have judged history and relationships. You have even judged the value of a person's life by the quality of your concept of beauty. By all accounts, you are quite well-practiced in the activity. (Mack’s face reddens with shame . . . looks down) Tell me, if I may ask, by what criteria do you base your judgments?

MACK: (unable to make eye contact) Nothing that seems to make much sense at the moment. (his voice faltering) I confess that when I made those judgments I felt quite justified, but now . . .

WOMAN: Of course you did. (a statement of fact) Judging requires that you think yourself superior over the one you judge. Well, today you will be given the opportunity to put all your ability to use.

MACK: And . . . . just what will I be judging?

WOMAN: Not what. Who. (Mack starts to panic – it is obvious in his nervous gestures and on his face) Your imagination is not serving you well at his moment.

MACK: (weakly) I really can’t do this.

WOMAN: (smiling) Whether you can or cannot is yet to be determined.

MACK: So, who is it that I am supposed to judge?

WOMAN: God. (pause, then finishes as if it was of no particular consequence) And the human race.

MACK: (dumbfounded) You have got to be kidding!

WOMAN: Why not? Surely there are many people in your world you think deserve judgment. There must be at least a few who are to blame for so much of the pain and suffering? What about the greedy who feed off the poor of the world? What about the ones who sacrifice their young children to war? What about the men who beat their wives, Mackenzie? What about the fathers who beat their sons for no reason but to assuage their own suffering? Don't they deserve judgment, Mackenzie? (Mack clenches his fist, breathing coming short and quick as he tries to control his unresolved anger) And what about the man who preys on innocent little girls? What about him, Mackenzie? Is that man guilty? Should he be judged?

MACK: (screaming) Yes! Damn him to hell!

WOMAN: Is he to blame for your loss?

MACK: Yes!

WOMAN: What about his father, the man who twisted his son into a terror, what about him?

MACK: Yes, him too!

WOMAN: How far do we go back, Mackenzie? This legacy of brokenness goes all the way back to Adam, what about him? But why stop there? What about God? God started this whole thing. Is God to blame? (continues unrelenting) Isn't this where you are stuck, Mackenzie? Isn't this what fuels The Great Sadness? That God cannot be trusted? Surely, a father like you can judge the Father! (Mack’s anger continues to rise) Isn't that your just complaint, Mackenzie? That God has failed you, that he failed Missy? That before the Creation, God knew that one day your Missy would be brutalized, and still he created? And then he allowed that twisted soul to snatch her from your loving arms when he had the power to stop him. Isn't God to blame, Mackenzie?

MACK: (loudly, pointing his finger right at her) Yes! God is to blame!

WOMAN: Then, if you are able to judge God so easily, then you certainly can judge the world. (without emotion) You must choose two of your children to spend eternity in God’s new heavens and new earth, but only two. MACK; What? (beginning to panic)

WOMAN: And you must choose three of your children to spend eternity in hell. (pause, then continues calmly) Mackenzie. I am only asking you to do something that you believe God does. He knows every person ever conceived, and he knows them so much deeper and clearer than you will ever know your own children. He loves each one according to his knowledge of the being of that son or daughter. You believe he will condemn most to an eternity of torment, away from His presence and apart from His love. Is that not true?

MACK: I suppose I do. I’ve just never thought about it like this. (stumbling over his words, in shock) I just assumed that somehow God could do that. Talking about hell was always sort of an abstract conversation, not about anyone that I truly . . . not about anyone that I truly cared about.

WOMAN: So you suppose, then, that God does this easily, but you cannot? Come now, Mackenzie. Which three of your five children will you sentence to hell? Katie is struggling with you the most right now. She treats you badly and has said hurtful things to you. Perhaps she is the first and most logical choice. What about her? You are the judge, Mackenzie and you must choose.

MACK: I don't want to be the judge . . . (softly) I can’t do this.

WOMAN: You must.

MACK: (louder and more vehemently) I can’t do this.

WOMAN: (very softly) You must.

MACK: (yelling) I . . . will . . . not . . . do . . . this!

WOMAN: (whispering) You must.

MACK: (Screaming, completely out of control) I can’t. I can’t. I won’t! (The woman stands silently watching and waiting) (After a long pause) Could I go instead? If you need someone to torture for eternity, I'll go in their place. Would that work? Could I do that? (Crying and begging) Please let me go for my children, please, I would be happy to . . . Please, I am begging you. Please . . . Please . . .

WOMAN: (softly and smiling) Mackenzie, Mackenzie. Now you sound like Jesus. You have judged well, Mackenzie. I am so proud of you.

MACK: (confused) But I haven’t judged anything.

WOMAN: Oh, but you have. You have judged them worthy of love, even if it cost you everything. That is how Jesus loves. And now you know Papa's heart, who loves all his children perfectly. (Mack bristles as an image of Missy flashes through his mind – the change is obviously back to anger) What just happened, Mackenzie?

MACK: I understand Jesus’ love, but God is another story. I don’t find them to be alike at all. I just don't understand how God could love Missy and let her go through that horror. She was innocent. She didn't do anything to deserve that. Did God use her to punish me for what I did to my father? That isn't fair. She didn't deserve this. (crying) I might have, but she didn't.

WOMAN: Is that who your God is, Mackenzie? It is no wonder you are drowning in your sorrow. Papa isn't like that, Mackenzie. She's not punishing you, or Missy. This was not his doing.

MACK: But he didn’t stop it.

WOMAN: No, he didn’t. He doesn't stop a lot of things that cause him pain. Your world is severely broken. You demanded your independence, and now you are angry with the one who loved you enough to give it to you. Nothing is as it should be, as Papa desires it to be, and as it will be one day. Right now your world is lost in darkness and chaos, and horrible things happen to those that he is especially fond of.

MACK: Then why doesn’t he do something about it?

WOMAN: He already has . . . (smiling) He chose the way of the cross where mercy triumphs over justice because of love. Would you instead prefer he'd chosen justice for everyone? Do you want justice, ‘Dear Judge'?

MACK: No, I don’t. Not for me and not for my children. (pause) But I still don’t understand why Missy had to die.

WOMAN: She didn't have to, Mackenzie. This was no plan of Papa's. Papa has never needed evil to accomplish his good purposes. It is you humans who have embraced evil and Papa has responded with goodness. What happened to Missy was the work of evil and no one in your world is immune from it.

MACK: But it hurts so much. There must be a better way.

WOMAN: There is. You just can't see it now. Return from your independence, Mackenzie. Give up being his judge and know Papa for who he is. Then you will be able to embrace his love in the midst of your pain, instead of pushing him away with your self-centered perception of how you think the universe should be. Papa has crawled inside of your world to be with you, to be with Missy.

MACK: I don’t want to be a judge any more. I really do want to trust Papa. But I’ll need help.

WOMAN: Now that sounds like the start of the trip home, Mackenzie. It certainly does.
```
