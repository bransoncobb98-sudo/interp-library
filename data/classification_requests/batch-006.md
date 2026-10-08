# Classification request: batch 6 of 63 (40 records, IC-0201 to IC-0240)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-006-reply.json`.

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

## IC-0201: The Men Who Killed Me

- Title: The Men Who Killed Me
- Author (byline): Marie Louise Niyobuhungiro
- Work: The Men Who Killed Me: Rwandan Survivors of Sexual Violence (Anne-Marie de Brouwer and Sandra Ka Hon Chu, eds) Pgs 29-34
- Publisher: Douglas and McIntyre
- Publication date as stated: Sept 2009
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MARIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1575
- Already set (do not supply): none

### Source block (context only)

```text
Author: Marie Louise Niyobuhungiro
Book: The Men Who Killed Me: Rwandan Survivors of Sexual Violence (Anne-Marie de
Brouwer and Sandra Ka Hon Chu, eds) Pgs 29-34
ISBN: 978-1553653103
Publisher: Douglas and McIntyre
Date (Month/Year): Sept 2009
```

### Introduction (context only: never use it for content warnings)

```text
In the 100 days of genocide that ravaged Rwanda in 1994, one million people were killed and as many as 500,000 women and girls were raped. No one was spared. Grandmothers were raped in front of their grandchildren; young girls witnessed their families being massacred before being taken as sex slaves. Nearly all the women who survived were victims of sexual violence or were profoundly affected by it. An astounding 70 percent are HIV-positive. In Rwanda’s social and cultural climate, survivors who speak out face discrimination and isolation.

Marie Louis Niyobuhungiro is one of the victims of Rwanda. Bear witness not only to the crimes she and her countrymen endured, but to the incredible courage that has allowed her to survive and flourish.

From The Men Who Killed Me: Rwandan Survivors of Sexual Violence edited by Anne-Marie de Brouwer and Sandra Ka Hon Chu; this is the testimony of Marie Louise Niyobuhungiro
```

### Performance text (classify this)

```text
Born:1975 (day and month unknown)

Birthplace: Shyorongi, just outside Kigali MARIE: (Pgs 29-34) People think I am crazy because I am always crying, and I do not blame them for thinking so. I am always angry, and I do not sleep at night. I hoped secretly that I would die during the genocide, but being among other survivors within a survivors’ organization has brought me comfort and hope. I feel like I have a family now, and I am very grateful for that.

MARIE: Before the genocide, we were a family of eight children—five girls and three boys. I was the fourth child in the family. My father was a teacher, and my mother was a farmer. We lived in Shyorongi, just outside Kigali. There were many Tutsi families in Shyorongi; we had only one Hutu neighbour. Although he was our neighbour, that Hutu hated us, especially my father, because we were Tutsi. In 1991, my father was poisoned, and I suspect that the Hutu neighbour who hated him so much did it. When my father started to feel sick, he went to a traditional clinic. After his death, my mother asked the people at the clinic what my father had died of, and they told her that he had been poisoned. Today, our former Hutu neighbour and all his family are in prison for crimes they committed during the genocide.

On April 6, 1994, when President Habyarimana died,. almost three hundred Tutsi had found refuge in the Catholic church of Mboza.

We arrived at the church at about ten in the morning, and a few minutes later the Interahamwe and far soldiers started shooting. They had guns and shot all the men. I fell, and some dead bodies fell on top of me. I was all covered with blood. I heard screams and babies crying, but I was unconscious for most of the time the attack was continuing.

The next day, they came back to kill those who were not yet dead. There was blood all over me, and the killers thought that I was dead, too, so they left me there, lying among those dead bodies. Once I had regained consciousness, all I could see were a lot of bodies lying around the church. The stench of blood was thick in the air. Except for one of my sisters, all my other relatives died during this attack at the church. Out of three hundred people in the church, only five had survived. I felt completely empty. I had no thoughts and felt nothing, nothing at all.

After the Interahamwe left the second time, I left the church. My sister and I went in different directions, because we felt that even if one of us was killed, the other one might have a chance to survive. I fled in the direction of a nearby forest and ran into an Interahamwe on the road, who asked me where I came from. I recognized him as a fellow churchgoer named Ntirenganya. I told him that I had lost my way and was just wandering around. He said that he had finished killing for the day, so others would kill me, not him.

After that close encounter, I spent three days hiding in the bushes. On the fourth day, I went to the house of an uncle, who had not yet had an opportunity to flee, because his wife had just given birth. He and his wife had already been warned by their neighbour, an Interahamwe, to leave their house immediately; they would not have much longer to live otherwise. Together with my uncle’s relatives, I left his house that night. But, at the gate in front of his house, we ran into a group of Interahamwe militia. They took the girls among us and brought us to a nearby roadblock in order to kill us.

Every far soldier or Interahamwe we met on the way made an insulting speech or had a rod to beat us with. One of them said that the girls should be brought to the Twa, who were often ridiculed in Rwanda and considered stupid and worthless. At some point, a far soldier picked me out of the group and took me to a nearby bush. I don’t know what happened to the other girls I was with.

This soldier raped me. After he was done with me, he took me to a house and told the owners of the house to keep me safe, so that he could rape me every time he came. He told them if anything happened to me he would kill them. Every time he came to the house after that, he took me to the forest to rape me. Over five days, I was raped five times a day. The rapist didn’t say anything to me. In the forest, the local people often saw me being raped by this man. The local people, an Interahamwe militiaman and other Hutu would watch the soldier rape me and did not even raise their little finger to stop it. They didn’t care, because I was Tutsi. They were silent. The far soldier who did this to me was so old -- about forty -- and so savage. It was the very first time I saw what a man was capable of doing.

After those five days, the old man brought me to a lady called Mukandoli, who was an Interahamwe too, and I stayed there. She didn’t care about my situation. She didn’t say anything, except when she sometimes ordered me to go out and farm. I stayed with this lady for one week. Then another far soldier came and told Mukandoli that his colonel wanted me.

When I arrived at the far camp, the colonel had the “manners” to ask me if I wanted to sleep with him. But I knew that whatever answer I gave, the outcome would be the same, and that I would end up in his bed if he had one. I said no and ran into the bushes. His soldiers spent the whole night looking for me, but they didn’t find me.

A little later, I saw a house and entered it. The house appeared to be an Interahamwe’s harem, full of Tutsi women and girls. There were about ten teenage girls in the house, all between about sixteen and twenty years old. The far soldiers who were looking for me found me there and took me back to the colonel. On the way back, they asked me to sleep with them. I told them I could do that the next day. While they were still discussing this, I managed to escape, and I walked all the way to Ruhengeri, which was already under the control of the RPF.

For two weeks, I hid myself during the day and walked during the night. I ate nothing and hid in the bushes. When the RPF went to Kigali, I followed them. I walked just behind them, back to my place of birth. I occupied a house that belonged to owners who had fled the country, because my family house had been destroyed during the genocide. To make a living, I dug the fields for a farmer. Later, a fund for survivors was established, which provided me with a bit of support. I lost four brothers and sisters during the genocide, and one sister died of kidney failure right afterwards. Before the genocide, I had never been intimate with a man, and yet now I have gotten to know many without my consent. Even after the genocide, in 2000, a neighbour came to my house, forced my door open and raped me. There was no use screaming, because no one lived close by. I became pregnant as a result of this rape, and the child died immediately upon birth. The doctors then pressured me to take an HIV test, and I discovered I am HIV positive.

I live in very bad conditions because I didn’t go to school. I have no job and am too weak now to dig the fields. I get food from an organization that helps me to survive. I have had four children since the genocide, all from different fathers. The father of one of my children is a neighbour, and the others have jobs in the neighbourhood. I never see them. I only had sex with each of them once. Luckily, my oldest three children are not HIV positive, but my youngest child has not been tested yet. I wish I could give my children some more support, including buying them school materials and clothes. I am always sick, sometimes because of HIV and other times because of the beatings I endured during the genocide. I was hit on my knees and head with a club and I suffer from severe headaches now. I don’t think I can forgive the far soldiers or the Interahamwe. I don’t want to hear about reconciliation. I accused them in the gacaca courts, including the one who raped me, those who participated in the killings in the church and those I saw at the roadblock, but now they are being released. Gacaca courts do not bring justice. I think the best punishment those men could get is the death penalty, because they killed others, too. We need justice. The génocidaires should not be released. I shared my testimony in order to help establish justice, and I hope it will do that.
```

---

## IC-0202: Millie

- Title: Millie
- Author (byline): Susan J Kander
- Work: Women Heroes: Six Short Plays from the Women’s Project
- Publisher: Hal Leonard Corporations
- Publication date as stated: 1987
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MILLIE
- Teaser before the introduction: No
- Spoken words (computed): 2258
- Already set (do not supply): none

### Source block (context only)

```text
Author: Susan J Kander
Book: Women Heroes: Six Short Plays from the Women’s Project
ISBN: 0936839228
Publisher: Hal Leonard Corporations
Date (Month/Year): 1987
```

### Introduction (context only: never use it for content warnings)

```text
When faced with a loved one’s illness, things change. Things don’t happen the way they once did, life doesn’t run as smoothly. When Millie’s husband falls ill she is no longer just a wife and mother. She is his nurse, his caretaker, his janitor and ultimately, his life support. She must strive hard to remain the same woman she was . . . . to be just “Millie” by Susan J. Kander.
```

### Performance text (classify this)

```text
(Lights up on an empty bedroom. Millie enters wearing a bright print sack of a dress and house shoes, her face the picture of fatigue. She walks around what we understand to be a bed, and blows a somewhat perfunctory kiss to the occupant of the bed.)

MILLIE: You think somebody's trying to tell me something or something? They done smashed up my car now for good and all. Can you believe it? Every car I get, somebody feel they got to smash it up for me. Now I got to find me another one, and I got to ask Mr. Lewis to help me out. God I hate that. But I got to get myself back on rubber again, and soon. You know I was thinking, while I was serving the rolls around the table for the tenth time-now why she got to go and have a sit-down brunch the one Saturday I got big night-time plans? Anyway, I was thinking, you know, about getting me a Mack Truck, so instead of peoples running my car all the time, I can get to tearing up some other peoples' cars! (laughs) Oh Honey, I am almost too tired to laugh, and you know that's serious! . . . Shoot, now I got to go out tonight in Sam's old raggedy car. And even worse, I got to let him drive. I never let him drive my car. I got no interest in passing it around for other peoples to smash it up for me, hell no. I just said a sweet word, didn't I, baby? Specially, furthermore, since Sam like his whiskey and I only drink Coca-cola, ain't that right? I have a Coke and I smile. What you bobbing your big head around for, Honey? It's the truth. Pop pop pop? Oh, okay, yeah, you right, I drink Orange Pop. Yeah, so do you, so do you. You didn't get to be over two hundred pounds sitting up in that bed drinking ice tea! You like it when I say sweet words, don't you? You like this dress? Mrs. Lewis brang it to me from Hawaii. (Crossing to vanity) She never bring me candy no more, old spoil sport. "It's for your own good, Millie; you know it." No I don't know it. Sam love me, he said, just the way I am. Yeah, and I believed him so much, I started doing his laundry for him. Like the last thing I need in the world ain't more folks' dirty clothes. (Begins to apply make-up) this morning I got to work, Mrs. Lewis look at me and said "Millie, you look like death warmed over. Did Honey keep you up all night again?" Like you had your seizures on purpose or something. "Why don't you go upstairs and take a nap?" Seem like she can tell by my face when you've had a seizure in the night, or messed in your bed. She look in my face, at the ring around my eyes, see I'm so tired I could cry. And then she says "You look like death warmed over." Dear God, is that necessary? . . . Boy, Honey, one of these days you're going to have one too many. That's how Dr. Brackett says it works. . . . Oh, she's only trying to be nice, I know. She don't sleep too good neither, sometimes. Yeah, someday I am going to say to her "Hey Mrs. Lewis, didn't you get no sleep last night? Now we both look like a corpse reheated!" (laughs) See how she did that for Good Morning. Shoot, I think if I did it once, I'd want to do it every day: drive in the driveway, walk in the door and fall into bed. Yeah, that used to be my only complaint about Sam: he may be a old raggedy man, but he never let me get my rest at night. (laughs) Now he's dumb enough to think all he's got to do is take me to see Teddy Pendergrass at the Uptown Theater and I'm going to start doing his laundry again? What kind of a dumb broad does he think I am? Sure is nice, though, have a man around, for whatever the need arise. . . . That was a long time ago, that first time: a long time. A lot more done changed in old Teddy's life, God bless his heart, than in mines. His life took a real dive: mines just stayed on the bottom of the ocean where it's been ever since you started growing that thing up in your head. Poor Teddy. I can't picture you in no wheelchair, man, not you with your beautiful voice and that beautiful body and the way you use it ooh boy! I can still see him, Honey, moving his meat to the beat ooh yeah. Teddy Teddy Teddy, put your meat on the beat boy and move it over my way. Ooh yeah. That man can do it to me any old time he want-ain't you the most stunning man I ever been in the same room with, never mind-oh never mind there's all the rest of the crowd here cause it's just you and me, Teddy, you and me. Oh yes! Ain't you... simply... stunning. . . I should have known Sam was low class right from the beginning when he offered me my choice between last row at Teddy Pendergrass and ring-side seats at All-star Wrestling. I knew he wanted me to choose wrestling, too! Almost did, too, just to make him like me. But I got hold of myself. I said "Mildred, what are you doing? He's giving you a choice: choose right." You would never have pulled that kind of stunt, I know that. You would have said "Kick off your house shoes, Sugar; we are stepping out." Like you did remember when you took me to the Mark: IV and we dined and we danced all night long-. . . . Listen to yourself, Mildred. Eleven years and listen to you. Dear God. Well, nothing stops the sand, Baby. Someday, somehow, it’ll be better, ain't that right? . . . That was the first time I ever slipped out on you, long after the first surgery. I don't think it troubled Sam none, in fact I know it didn't. But it troubled me plenty and I wasn't going to do it for no All-star Wrestling! Not even Gorgeous George versus The Stomper! Yes, I said The Stomper, Honey, he's our man, yes I know; Millie know. No, it ain't on now; You already watched it today, come on at noon, remember? You watched it with Charles, when he come by to give you your lunch. It ain't on again 'til Monday. (She has returned to vanity, and resumes with make-up and jewelry.) Perry’ll be by later on after I go. He'll sit with you watch the ball game, okay? Give you your dinner. He called me yesterday, asked could he come by and see his daddy, since he didn't feel like going out on no hot dates. (laughs) That old Perry. My baby some smart kid, ain't he? Smart? He's downright crafty. Twenty-three years old, junior college graduate, and ain't got no babies! Ain't even shacking with no one; and furthermore, ain't even looking for it. Now that's a crafty kid. Must of took a good lesson from Charles and Tony and all they babies. But imagine that, Honey: of all my boys, my baby a college graduate, working two jobs, money in his pants and ain't got no one to spend it on but his own self. And his old Mama, of course. He gave me these earrings, remember? And for no good reason, neither. Didn't even want me to feed him dinner or nothing. (Fetching shoes out of a closet) I can't believe it. I told them all three a million times, and you heard me say it: "You make babies, you keep them at your house. I’ll visit, on Sundays, after church. Put your lady on the pill; wear a raincoat; do whatever you got to do cause I ain't bringing up your children. I'm tired." Now what do I get every morning but BANG goes the screen door and "Hey Grammaw, got any chocolate cake today?" (laughs) That baby Tony is so fat already, he's just a little butterball. . . I'll never know what went right with Perry, but he's as free as an eagle that boy. I ain't been that free since I was dragging the chair up to the cupboard and reaching my dirty little hand into Mama's sugarbowl. And even that wasn't free, cause she sent me out to pick my own switch for the whipping every time! (laughs) Your mama ain't sent so much as a pair of pajamas in eleven years. She don't care if I was to put you away in a nursing home. And she sure as hell ain't about to help pay for it. (Sitting beside bed, putting on shoes) Dr. Brackett started in about a home before you was even out of the hospital the first time, all 67 pounds of you. But he dried up about it when you started gaining weight for me. Then, after the second surgery, and the strokes, couldn't nobody understand you but me, and I said to him "How's anybody going to understand him when he's asking for his orange pop, or for the channel to be switched, or trying to tell somebody he done stooled in his bed again? No thank you, he stays home with me. I got my boys to help me out. They call him Daddy, you know, ever since we got married, me and Honey. So he stays home. . . . Two major surgeries, more strokes than I got fingers, and now all these seizures: Lord, Honey, how much can a person put up with huh? Ain't you tired yet? You got nothing left hardly but a mouth, and not even one good eye. Ain't you plain tired? How many more nights like last night, Honey, huh? I can't afford enough sets of sheets for you, and I get so tired of doing laundry in the middle of the night. Dear god, when are you going to get tired? Just plain wore out? . . . .No, why would you? All you do is sit up in that bed all day, watch TV and eat up my kitchen. You're happy... You know, you don't even look like the Honey I married. ..(Rising, going back to vanity) I guess I don't look too much like the Sugar you married anymore, now, do I? These black bags under my eyes. Hair needs touching up. I don't like my roots showing like that. Honey? What do you really think about this dress? Kind of makes me look like a. . . billboard. don't it? (laughs) I want Teddy to think I'm sexy. (She puts on a belt that transforms the dress from sack to dynamite.). I got all of Saturday night just waiting for me and Teddy. And then I'll think about Sam. Old two-timing lizard. He just got to stay cool and wait for me, cause I promised myself I'm going to take myself backstage afterward and personally wish Mr. Teddy Pendergrass the best of luck and God bless him for the rest of his life. They better let me in back there" too: anybody get in my way I'll just sit on them-Boom! Cause I'm going to see my Teddy, tell him "I’ll drive your wheelchair any time you in town. You just keep singing, Mister; you keep on living, cause you can't afford to stop turn around look behind you, see how nice things used to be. You just keep your eyes going forward; look on ahead now. You keep singing your songs cause I want to hear them. I always want to keep hearing them, Teddy, you understand me? Always and always. . . " Never look behind you. Never ever. That's what I'm going to tell Mr. Teddy Pendergrass when I see him tonight backstage at the Uptown Theater (She hears something, turns abruptly to the bed; Honey is having a seizure.) Oh! Don't fallout the bed, I can't get you up off the floor!

(Runs to vanity, searches the drawer for a box of individually wrapped tongue depressors. A car horn honks loudly offstage.) Not now, Sam! Tonight! No more! (She finds the box, wrenches it from the drawer and spills it on the floor. Drops to her knees to clean up the mess and find one depressor. She is frenzied.) I can't do this no more! Too many! . . . Perry. . . Teddy. . . Teddy in your wheelchair! (Doorbell rings. Millie freezes with the stick in her hand, there on her knees. Lights change.) (Almost as If in a dream) That's what I had to tell Dr. Brackett the other night at that party I did. "I seen you leave the buffet table, Doctor. You so embarrassed to see me you going to pass up my best rack of lamb with sage dressing rather than let Millie serve you? Well here. I brought you a plate, so I can tell you straight out once and for all: I see your eyes, I know what's in your heart, and you got it all wrong. This is me, Mrs. Clinton Gladies telling you Don't you feel sorry about what you done. Now just don't. I know you said six months, but you gave me eleven years with Honey I wouldn't of had without you, and even though you had to cut out some of the best part of him, what you left was more than I would have had otherwise. So don't you ever regret operating on him. (laughing) Besides, how could you know I'd be such a miraculous nurse? And he'd be such a hard-headed man? So you see, I'm not sad; I'm happy. This is a happy face, Doctor: a very happy face." (Doorbell rings again. Millie comes back to the present, finds herself on her knees with the unused stick in her hand. She looks at the bed, then hurries to it, trembling.) Honey? . . .

Oh you made it, baby, you made it through again. . . . That's right, sleep. You sleep. (Relieved, she turns, but sees now that he has messed in the bed during the seizure.) Oh, dear God! (Doorbell rings) Sam? Sam! (Doorbell rings in response) Keep your pants on you old coot! (She finds a clean set of sheets in the closet, starts to unfold them to remake the bed. She stops. Long moment, then) Mildred, you cannot do this now. (She puts sheets down, goes to vanity, gets pencil and paper, writes.) "Dear Perry. Sorry, I had to go. Leave dirty sheets for me. . . . (Drawing smile face) Smile." (Walks back to bed with note) " You know, Honey, even if we'd of never went to see that old judge at all, you know you'd be right here, right now. Right here in this old bed, in this old room, in this old raggedy house; with this woman taking care of you. Cause you're my Honey, and I'm your Sugar. Ain't that right? (Doorbell rings long and hard) Get off my bell you old moose! I'm coming! (Putting note on sheets, she goes to vanity, checks herself again, pulls herself together, takes up pocket book, starts to exit. Stops, blows Honey a kiss, takes a deep breath, looks straight ahead, and exits.)
```

---

## IC-0203: Mirror to Her Mouth from House Arrest

- Title: Mirror to Her Mouth from House Arrest
- Author (byline): Anna Deavere Smith
- Work: House Arrest and Piano: Two Plays
- Publisher: Anchor
- Publication date as stated: April 2004
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 673
- Already set (do not supply): none

### Source block (context only)

```text
Author: Anna Deavere Smith
Book: House Arrest and Piano: Two Plays
ISBN: 978-1400033577
Publisher: Anchor
Date (Month/Year): April 2004
```

### Introduction (context only: never use it for content warnings)

```text
In 1996, The MacArthur Foundation awarded Anna Deavere Smith a prestigious fellowship, saying she “has created a new form of theatre — a blend of theatrical art, social commentary, journalism and intimate reverie.” These words of praise are epitomized by this selection: Mirror to Her Mouth from House Arrest . . . a true story of Paulette Jenkins, whose boyfriend abused her and her daughter. One night the man beat Paulette’s daughter so badly that she died. This is Paulette’s story as told to Anna Deavere Smith during an interview at the Maryland Correctional Institution for Women and brought to life on stage in Mirror to Her Mouth from House Arrest.
```

### Performance text (classify this)

```text
I began to learn how to cover it up
because I didn't want nobody to know that this was happening
In
my home.
Ya know.
I wanted everyone to think that we were a normal family
and I mean
we had all the materialistic things.
But that didn't make my children pain any less.
I ran out of excuses about how we got black eyes
and busted lips and bruises
me and the kids.
I didn't have no more excuses.

But it didn't change the fact that it was a nightmare
for my children.
It was a nightmare.
And I failed them.
Dramatically.
Because I allowed it to continue on and on and on.
And that night that she got killed,
and the intensity that grew and grew and grew.
Until one night,
we came home,
from getting drugs,
and he got angry with Myeshia
and he started beating her.
And he just continued to beat her,
he had a belt, he would use a belt.
I'm just speaking of the particular night she died.
And he beat her
and he put her in the bathtub.
And I was in the bedroom.
But before all this happened,
four months before she died,
I thought I could really fix this man
so I had a baby by him!
Insane?
Thinking that
if I gave him his own kid
he'll leave mine alone.
And it didn't work.
We wound up with three children.
But the night that Myeshia died.
I stayed in the room with the baby.
And I heard him,
just beating her,
just beating her,
like I said he had her in the bathtub,
and every time he would hit her,
she would fall.
And she would hit her head on the tub.
I could hear it.
It happened continuously,
repeatedly.
(Whispering. )
And I dared not to move.
I didn't move.
I didn't even go see what was happening.
I just sat there and listened.
And then later
(SHE sucks her teeth.)
he sat her in the hallway
and
told her just set there
and she set there for 'bout
four to five hours
and then he told her to get up
( Crying.)
and when she got up she said she couldn't see.
(Whispering, crying.)
Her face was bruised.
And she had a black eye.
All around her head was just swollen.
Her head looked like it was two sizes of its own size.
I told him to let her go to sleep and he let her go to sleep.
(Whispering. )
The next morning she was dead.
He went in and checked on her for school.
And he got very excited.
And he said
"She won't breathe!"
I knew immediately that she was dead.
'Cause I went in
I didn't even want to accept the fact that she was dead.
So I went and took a mirror to her mouth.
There
was no-thing coming out of her mouth.
Nothing.

He said
"We cannot let nobody know about this,
so you got to help me."
And I agreed.
I agreed.
I didn't dare tell anyone.
'Cause I had been keeping it a secret
for years and years.
And it just seemed like secondhand to me
to keep a secret.
That night,
we went to the mall
and we told the police
that she had been missing.
We told like the security guards of the mall
that we had like lost her.
Ya know we fabricated this story and I went along with it.
And we told him that she had been missing.
But she wasn't missing.
So after that
we left the mall
and we told them what she had on
that night.
We got her dressed in the exact same thing
that we told the police that we had put on her.

And we got the baby
and we drove like out to
(Hear her getting the slightest bit tired here.)
I-95.
I was so petrified
and so numb
all I could look
was in the rearview mirror.
And he just laid her right on the shoulder of the highway.
My own chile.
I let that happen to.
```

---

## IC-0204: Misreadings

- Title: Misreadings
- Author (byline): Neena Beber
- Work: Best American Short Plays 1996-1997
- Publisher: Applause Theatre Books
- Publication date as stated: Jan 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, SIMONE, RUTH
- Teaser before the introduction: Yes
- Spoken words (computed): 1932
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neena Beber
Book: Best American Short Plays 1996-1997
ISBN: 1557833168
Publisher: Applause Theatre Books
Date(Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
RUTH: What are the issues for which you would kill? I like to ask my students this on their first day of class. I assign novels where the hero or heroine kills, or is killed. I try to bring it home. They tell me they would kill to defend their family. They'd kill to defend their friends. I ask them if they would kill for their country. . . for their freedom. . . what would it take?

SIMONE: I'd kill for a pair of Prada velvet platforms in deep plum. Those are to die for.

RUTH: Simone. I didn't know what she was doing in my class. Neither did she, apparently.

TOGETHER: Misreadings by Neena Beber
```

### Performance text (classify this)

```text
CHARACTERS:

SIMONE: a student

RUTH: a teacher

RUTH: [TO SIMONE.] Nice segue, Simone; would we be willing to die for the same things we'd kill for? [Out.] She usually sat in the back, rarely spoke, wore too much lipstick and some costume straight out of, what, Vogue. When she did speak, it was always - disruptive.

SIMONE: I'd die for love except there ain't no Romeos, not that I've seen; I'd take a bullet for my daddy but he's already dead; I'd die of boredom if it were lethal, but I guess it isn't.

RUTH: If I couldn't inspire her, I wanted her gone. I'd asked her to come to my office hours. I asked her several times. She was failing, obviously. I would have let her drop the class, but it was too late for that. She never bothered to come see me. Not until the day before the final exam. She wanted me to give her a passing grade. [RUTH turns to SIMONE.]

RUTH: How can I do that, Simone? You haven't even read the material. Have you read any of the material?

SIMONE: I don't find it relevant.

RUTH: If you haven't read it, how do you know?

SIMONE: I read the back covers.

RUTH: You may find yourself surprised... Anna Karenina is wonderful.

SIMONE: It's long.

RUTH: Why not give it a shot?

SIMONE: The books you assign are depressing. . . I don't want to be depressed. Why read stuff that brings you down? Kafka, Jesus Christ - I started it, okay? The guy was [messed] up.

RUTH: So you were moved at least.

SIMONE: Moved to shut the book and find something more interesting to do.

RUTH: That's too bad; you might have found one of these books getting under your skin, if you stuck with it. Haven't you ever read something that's really moved you?

SIMONE: Nothing moves me, Dr. Ruth.

RUTH: I'm going to have to ask you to put out that cigarette.

SIMONE: Okay, ask. [But she puts it out.] See art or be art. I choose the latter.

RUTH: Somebody must be paying for this education of yours. I imagine they expect a certain return for their money.

SIMONE: How do you know I'm not the one paying for it?

RUTH: I don't believe someone who was spending their own money would waste it so flagrantly.

SIMONE: Okay, Dad chips in.

RUTH: Would that be the same father you said was dead?

SIMONE: That was a joke or a lie, take your pick.

RUTH: You're frustrating the hell out of me, Simone.

SIMONE: I don't consider it a waste, you know. I like the socialization part. .

RUTH: If you fail out of this school, you won't be doing any more "socialization. "

SIMONE: You assume that I'm failing the others.

RUTH: So it's just this class, then? That you have a problem with?

SIMONE: [Referring to her granznzar.] Dangling. [Beat.] Do you enjoy being a teacher?

RUTH: Yes, I do.

SIMONE: So I'm paying for your enjoyment.

RUTH: It's not a sin to enjoy one's work, Simone.

SIMONE: I just don't think you should charge me, if it's more for your pleasure than for mine.

RUTH: I didn't say that.

SIMONE: Did you ever want to teach at a real school, not some second-rate institution like this?

RUTH: I like my job. You're not going to convince me otherwise.

SIMONE: Four-thousand two-hundred and ninety-eight.

RUTH: That is-?

SIMONE: Dollars. That's a lot of money. Do you think you're worth it? Do you think this class is worth it? Because I figured it out: this is a four credit class, I broke it down. Four-thousand two hundred and ninety-eight. Big ones. Well, do you think that what you have to teach me is worth that? Come on, start talking and we'll amortize for each word.

RUTH: You're clearly a bright girl. You can't expect an education to be broken down into monetary terms.

SIMONE: You just did. That's a lot of money, right? It's, like, food for a starving family in a fifth-world country for a year at least. It's a car. Well, a used one, anyway. Minus the insurance. Suddenly this number doesn't sound so huge. It's a couple of Armani suits at most. I don't even like Armani. So hey, come on, can't you even say "Yes, Simone, I am worth two Armani suits. I have that to offer you..."

RUTH: I can't say that, no.

SIMONE: No useful skills to be had here.

RUTH: The money doesn't go into my pocket, by the way.

SIMONE: I think it should. It would be more direct that way; you'd feel more of a responsibility. To me. Personally. Don't you think, Dr. Ruth?

RUTH: I'd prefer that you not call me that.

SIMONE: Wrong kind of doctor, man. All you're interested in is a bunch of books written a hundred years ago, and the books written about those books; you're probably writing a book about a book written about a book right now, am I right?

RUTH: If you don't see the connection between books and life, you aren't reading very well. I want you to try. Can you do that? Books might even show you a way to live.

SIMONE: I'm already living, Dr. Ruth. Are you? Because it looks like you haven't changed your hair style in twenty-five years.

RUTH: Well, you weren't even born then, Simone.

SIMONE: Stuck in your best year? Because I see you in a close cropped, spiky thing.

RUTH: That's enough.

SIMONE: P.S.: You might want to do something about the way you dress.

RUTH: Have you been in therapy?

SIMONE: Don't think that's an original suggestion.

RUTH: I'm not suggesting anything. I simply want to point out that this is not therapy. I am a teacher, not your therapist. You can't just waltz into my office and say whatever hateful thing you please. .

SIMONE: I don't know how to waltz.

RUTH: I'm giving up here, Simone. You don't like my class, you don't like me, you want to fail out, I can't stop you. [RUTH goes back to her work. SIMONE doesn't budge.]

RUTH: What?

SIMONE: Drew Barrymore would move me.

RUTH: Who?

SIMONE: I think Drew would do it. Getting to meet Drew.

RUTH: Who's Drew Barrymore?

SIMONE: Damn, you really should know these things. She's extremely famous. She's been famous since she was, like, born. I saw her on TV yesterday and she was so real. She connected. You know? You really might relate to your students better if you got a little more up to date.

RUTH: You might be right. But you might not be so behind in class if you spent a little less time watching television.

SIMONE: Drew is a film star, she's in films.

RUTH: You said you saw her on television. Don't you even go to the movies? Probably only the ones that are totally L-Seven. And I know you don't know what that means. [She forms a square by making an "L" and a "7" with her hands.]

SIMONE: Square? Anyway, Drew was on TV because she was being interviewed. They have these daytime talk shows nowadays?

RUTH: I've heard of them.

SIMONE: And this chick was in the audience and she started to cry. Because she couldn't believe she was there in the same room with Drew, who's been famous forever, right? She was just, like, sitting there sobbing. And this chick, she had her bleached blond hair pasted down real flat, and she was wearing a rhinestone barrette just like Drew used to, but that whole look is so old Drew, so ten-minutes-ago Drew. The new Drew is sleek and sophisticated and coiffed and this girl, this girl who wanted to be Drew so bad, she wasn't even current.

RUTH: I don't think we're getting anywhere.

SIMONE: And that is so sad. Because the thing about Drew is, she is always changing. It's a constant thing with her, the change. And that is, like, what you've got to do. . . keep moving or you die. Drew knows that. How to invent yourself again and again so you can keep being someone that you like, the someone that you want to be. And once you're it, you've got to move on. Now where was it you were hoping we'd get to?

RUTH: The exam is tomorrow morning at 9 A.M. If you read the material, any of the material, I might actually be able to give you a passing grade. But right now I don't think we need to waste any more of each other's time.

SIMONE: [Starts to go.] You might have said that I go to the movies the way you read books. I would have pointed that out, Dr. Ruth.

RUTH: Well I suspect we don't think very much alike. [SIMONE goes, turns back.]

SIMONE: A wall between our souls? [RUTH looks at her, about to say something, about to reach out.] I'm sorry if I've been rude. I'm sure a lot of peo-ple like your class. Maybe I wasn't raised well. I'm sure somebody's to blame. [SIMONE goes.]

RUTH: The next day she showed up at nine on the dot. I felt a certain pride that I had somehow managed to reach her, that she was finally going to make a real effort, but she handed in her blue book after a matter of minutes. I was rather disgusted and let it sit there, until a pile formed on top of it, a pile of blue books filled with the scrawling, down-to-the-last-second pages of my other more eager, or at least more dutiful, students. Later I began to read them straight through from the top, in the order they were stacked in. I wasn't looking forward to Simone's. In answering my essay question about how the novel Anna Karenina moves inevitably toward Anna's final tragic act, my students were, for the most part, thorough and precise. They cited all of the events that led to Anna's throwing herself in front of the train, touching on the many parallel plots and the broader social context. I was satisfied. I felt I had taught well this last semester. My students had learned. In the blue book she had written "All happy people resemble one another, but each unhappy person is unhappy in their own way." So I guess she had read Anna K; the opening sentence, at least. My first instinct was to correct the grammar of her little variation. There was nothing else on the page. I flipped through the book; she'd written one more line on the last page: "Any world that I'm welcome to is better than the one that I come from." I'm told it's a rock lyric. Something from the seventies. Anna was written in the seventies, too, funnily enough, a century earlier. I would have given Simone an F, but I noticed she had already marked down the failing grade herself, on the back of the book. Or maybe the grade was for me. By the time I came to it, days had passed. I didn't leap to conclusions. Come to think of it, Anna's suicide always takes me by surprise as well, though I've read the novel many times and can map its inexorable progression. [SIMONE, just as before...]

SIMONE: That's a lot of money. Do you think you're worth it? Do you think this class is worth it? [RUTH turns to her.]

RUTH: I live in worlds made by words. Worlds where the dead can speak, and conversations can be replayed, altered past the moment of regret, held over and over until they are bent into new possibilities. [RUTH tries to reach toward SIMONE...]

SIMONE: Do you think I'm worth it? Am I? Am I? Am I?

RUTH: I live there, where death is as impermanent as an anesthesia, and the moment of obliteration is only...a black-out. [SIMONE lights a cigarette as lights black out.]
```

---

## IC-0205: Missing Natalie and Victim

- Title: Missing Natalie and Victim
- Author (byline): Nicole Blackman
- Work: Blood Sugar
- Publisher: Akashic Books
- Publication date as stated: May 2002
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1692
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nicole Blackman
Book: Blood Sugar
ISBN: 978-1888451344
Publisher: Akashic Books
Date (Month/Year): May 2002
```

### Introduction (context only: never use it for content warnings)

```text
Each year, more than 1 million children are reported missing. This is a staggering number, but it doesn’t take into account the trauma faced by the overlooked sisters and brothers of those abducted whose family are irrevocably changed. This selection, Missing Natalie by Nicole Blackman brings to life the struggle of one young girl to come to terms with the abduction of her twin sister. .
```

### Performance text (classify this)

```text
Missing Natalie

Most of my friends don't know I was born a twin. She was born sixty-three seconds before me. Her name was Natalie. We came here together. She left without me.

We shared a room and split it down the middle. I put all my posters up on my side, and she put hers up on the other. One day we decided to wallpaper the room with Superfriends wrapping paper and Elmer's glue. Mom wasn't too crazy about that.

She was patient, I was bossy. She wanted to be a gymnast, I wanted to be an actress. But we both liked horses and we liked to draw. We mixed up things like ketchup and cough syrup and tried to get someone to eat it. Natalie and I would climb trees in our backyard and plan the houses we would build next to each other so we could visit when we had families of our own. We picked out the names for our husbands, for our children. When you're a twin, you have a shadow.

We were in the supermarket looking at the toys. Mom was picking up some shampoo and cat food. There was a doll that I really wanted so I ran a couple aisles over to ask Mom. She told me I already had too many dolls and sent me back to get Natalie so we could leave the store. It all happened in a minute.

This is the part where I'm supposed to tell you that your life can change forever in sixty-three seconds. But you already know that, don't you?

On the surveillance camera, you can see Natalie walking out of the store with a man. He's not forcing her, but we don't know why she's going with him. She turns around for a second like she's saying goodbye. At least that's what we think it means.

We've gone over the video hundreds of times. It's burned in my mind like the Zapruder film. Even now I could draw it for you, with the time code on the bottom of the screen and everything. I'm twenty-four now. She's frozen at nine.

When she was gone a month, I put our beds together and put a blanket across them when I slept.

They sent me to a child psychologist for a long time. She made me draw my "feelings." Let's draw your feelings now. What do your feelings look like? I wanted to strangle her. Instead, I drew for an hour so she'd shut up. I used only the black markers and drew me and a burned-out hole for Natalie. That's me, and that's Natalie. The psychologist analyzed the drawings and talked to my parents. She's having a very difficult time. Losing Natalie has left a void in her life. Well, duh. You could have just asked me and saved yourself a lot of time. You want to know how I feel? You want to know what's going on? Someone stole my sister. Someone f***** stole my sister. How many drawings do you want me to make? They stopped making me go to the psychologist after that.

I never saw Dad cry, but something was sacrificed after it happened. He drinks alone now sometimes. He never used to do that.

The police give us a report every three years now or something, and tell us the case is still open, as if that's a help. They try to tell me sometimes that since they never found a body, she might be alive. Right. Like there's nowhere on earth to hide a body. If she was alive, I'd know. If anyone would know I'd know, and I haven't felt her near me in a long, long time.

They put me under hypnosis. I told them the man was wearing a navy-blue corduroy jacket, had brown work boots on, smelled of grease and never looked at me. The case is still open.

Four months after she disappeared, it was our tenth birthday. I told Mom to forget about it but she insisted ... she always had a birthday party for us ... we had to go on with a normal life.

The day of the party we hung up balloons and streamers and Mom pretended Natalie was away somewhere, like it was a surprise. I sat there and waited. I waited all day.

Nobody came. All the kids who used to come to our parties now said they couldn't. Sometimes their mothers called and cancelled, like abductions were contagious and they didn't want their kids to catch it too.

That night Mom and I sat in the kitchen and ate a box of sugar cookies and talked about Natalie. We didn't have anymore birthday parties after that. It became the birthday ritual. We would eat a whole box of sugar cookies and talk about Natalie for hours. It was our way of keeping her close. We do it every year. Dad still doesn't know.

My parents refused to move after Natalie disappeared. We need to be here when she comes back. Otherwise, how will she find us?

We just want to know what happened. It's like watching a scary movie and the film breaks in the last fifteen minutes and they try to make everyone go home. We just want to know what happened.

Most of my friends don't even know I was born a twin. She was born sixty-three seconds before me. Her name was Natalie. We came here together. She left without me. TRANSITION According to the Office of Juvenile Justice and Delinquency Prevention . . . The murder of an abducted child, particularly by a stranger, is a rare event. There are estimated to be about 100 such incidents in the United States each year. The victims are typically “average” children, leading normal lives, and growing up in normal families. Just like Natalie, the vast majority of them are girls, with the average age between 11 and 12 years old. Natalie was just a bit younger. This is her story . . . Victim by Nicole Blackman.

Victim
I feel the motion of the car before I open my eyes. The air is blue-black, brown-black, black-
black. Smell of gas, oil, animals.
I'm in the trunk.
My wrists and ankles tied. My mouth is taped
and it almost covers my nose but I can breathe barely.

I must have been here for hours, everything's stiff and my head throbs like someone's
drumming on china.
The car stops.
He turns off the motor - there are no traffic sounds. No people sounds. No wind.
What place has no wind?
I turn my head towards the sounds
like people watch radios when something terrible happens.
My palms are sweating. Where am I?
The trunk squeaks as he lifts it up and the sun blinds me. He almost looks like a faceless Jesus
surrounded by light.
He pulls me out of the trunk and bangs my head against the door. I try to cry out, but it comes
out like a hum.
He drags me, half-standing, along a dirt road into a house. I can't see any other houses and it
looks like a farm.
The screen door bangs behind me
and I feel a deep, deep pressure inside me. All the rules have changed here.
I'm dragged down a hall like a bag and I look for a phone, other doors. Nothing but bare floors
and brown boxes in small rooms.
He pulls me into the bathroom
and I almost crack my head as he pushes me onto the floor. Tilts his head to the side
and gazes at me as if I was a pet, then walks out.
I'm lying there for a long time, trying to get the tape off of me. My eyes are tearing. I don't
make a sound.
I can't get up and I keep rolling from side to side, trying not to make noise.
I've got to get him to talk to me.
If I can get this thing off my face I can talk to him. I'll tell him my name.
Have you killed other women in here?
I'm thinking that you've got hundreds of them
nailed down, hung on walls, hanging from ceiling fans and swinging dead in summer wind.
Why did you pick me?
If I had stayed to finish at the library
I would have been there 20 minutes longer maybe I'd have been OK.
Would have rushed into the house,
books piled up in my arms like a baby, and blurted explanations why I was sorry. So sorry I'm
late everyone.
Would you have waited for me anyway? Would you have picked another woman?
Would I have read about her in the paper and said Oh my god, I was there that night...
and called all my friends in a panic.
Telling them then how much I loved them
as if I'd never have the chance again.
I wonder what everyone is doing now. Putting up signs. Showing my picture on the evening
news. Calling old friends. Maybe I'm not even considered missing yet.
The family will fall apart and my parents will go crazy. Slowly.
My brother will be so quiet at the funeral and insist the casket be closed. (I never even told
anyone what kind of funeral I wanted when I died.)
Maybe years from now they'll find my skeleton on the floor here
and they'll have to use dental records to identify me.
My family will say At least we know now.
We always hoped she was alive somewhere.
We just hope she's in peace.
When I sleep my dreams are crazy - I'm flying over fields.
I don't think I sleep for more than 20 minutes and when I wake up, it feels like I'm wider a heavy
blanket. I'm still here.
As I wake up I hear a dog barking in the distance
and I think I'm in my parents' house in South Carolina.
When I open my eyes, there's a shotgun pressed between them.

I'll never get married.
I'll never have kids.
I'll never go to Europe.
I'll never learn to play piano. I'll never write a book.
The last thing I hear is a click.
```

---

## IC-0206: Mockingbird

- Title: Mockingbird
- Author (byline): Kathryn Erskine
- Work: Not specified
- Publisher: Philomel
- Publication date as stated: Apr 2010
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CAITLIN, MRS. BROOK, DOCTOR, NEWS REPORTER, LADY, MRS. BROOKS, DEVON, MRS. JOHNSON, DAD
- Teaser before the introduction: Yes
- Spoken words (computed): 2058
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kathryn Erskine
ISBN: 978-0399252648
Publisher: Philomel
Date (Month/Year): Apr 2010
```

### Introduction (context only: never use it for content warnings)

```text
In Caitlin’s world everything is black and white. Anything in between is confusing. That’s the stuff her brother, Devon, always explained. But now Devon is dead, and Caitlin’s dad cries . . . A LOT. She wants to help, but as a ten-year-old girl with Asperger’s syndrome, she doesn’t know how. Then one day, on the news, she hears the word CLOsure and her life’s goal becomes a quest to find just that.

Mockingbird by Kathryn Erskine, who’s own daughter, Fiona, has Asperger’s as well.
```

### Performance text (classify this)

```text
CAITLIN: (Pg 34) Sometimes I read the same books over and over and over. What’s great about books is that the stuff inside doesn’t change. People say you can’t judge a book by its cover but that’s not true because it says right on the cover what’s inside And no matter how many times you read that book the words and pictures don’t change You can open and close books a million times and they stay the same. They look the same. They say the same words. Books are not like people. Books are safe.

CAITLIN: (Pg 10-16) Dad says it’s time to go back to school so here I am. Back in Mrs. Brook’s room. Sitting at the little round table. Mrs Brook says people have a hard time understanding me because I have Asperger’s so I have to try extra hard to understand them and that means working on emotions.

MRS. BROOK: Hi, Caitlin. So how are you? How are you feeling? (Caitlin sighs heavily and avoids making eye contact with Mrs. Brook) I think you’d like to forget about the painful events you’ve been through. The funeral must have been very difficult.

CAITLIN: (to audience) I wonder what she means. We sat in church. It was not very difficult. Everyone spoke so quietly I could barely hear them and almost no one talked to me. No one laughed like crashing glass and there was no lightning movement and no one appeared out of nowhere and nothing happened suddenly.

MRS. BROOK: Let’s Talk About it. (Caitlin turns her head away so she can’t see Mrs. Brooks anymore) I know it’s difficult but you can’t keep it all inside. Did you cry at the funeral?

CAITLIN: (Shaking her head) Dad cried. Please stop asking me questions.

MRS. BROOK: Caitlin. Your father is sad.

CAITLIN: Why?

MRS. BROOK: He misses Devon.

CAITLIN: Oh. MISS is a strange word. There is MISS like MISS Harper the principal. There is MISS like you will MISS your bus if you don’t hurry because you have to step on every crack. And there is MISS like dead.

MRS. BROOK: You’ll miss [Devon] but he’ll always be with you. Just in a different way.

CAITLIN: (to audience) I don’t want him around in a different way. I want him around in the same way. The way he was before. When he makes me popcorn and hot chocolate. And he tells me what to say and what clothes to wear and how not to be weird so kids won’t laugh at me. That’s the Devon I want. Not one who is floating around in the air. (Pg 63) At home I think about Devon’s Heart. I close my eyes and remember some of the things that happened on The Day Our Life Fell Apart. That’s what Dad calls it. After we came home from the hospital that night – with no Devon – Dad was yelling and kicking the furniture and the walls and shouting. Why? Why? WHY? Until I screamed at him: STOP IT! STOP IT! STOP IT! I press myself against the sofa and squish my eyes tight and even though I try not to I remember being at the hospital. People dressed in green pajamas and paper slippers said to Dad:

DOCTOR: We tried but we couldn’t close your son’s chest. His Heart – there was nothing left – there was nothing we could do. Nothing we could do.

CAITLIN: (to audience) (Pg 37) A gunshot wound to the Heart is almost always fatal. (Pg 65-71) [Dad] comes back into the living room and turns on the TV and stands there looking at it.

NEWS REPORTER: (with a microphone in his hand) I’m at the courthouse where the remaining killer from the Virginia Dare Middle School shooting has just had his preliminary hearing. The hearing found that there’s enough evidence against him to be put on trial for the murders of teacher Roberta Schneider and young students Julieanne Morris and Devon Smith. That horrific shooting was a devastating blow to this small community.

CAITLIN: (to audience) Dad goes to the bathroom and throws up. The camera switches to a lady sitting inside at the news desk.

LADY: We’ll hear more about this story later but isn’t it good that we now have closure.

CAITLIN: (to audience) I don’t think there is anything good about any of it. And I wonder how CLOsure can help. And what it is. I look up CLOsure and it says: the state of experiencing an emotional conclusion to a difficult life event such as the death of a loved one. I squeeze my Dictionary tight against my chest. I can hear Dad crying, so I close my eyes and plug my ears. [The next day] I wait all morning for my Mrs. Brook time. (to Mrs. Brook) Closure. How do I find it?

MRS. BROOK: Caitlin. Is this . . . are you talking about the news? The boy from the shooting? (she clasps her hands together, takes a deep breath and lets it out. Slowly. She closes her eyes)

CAITLIN: (to audience) Is she praying? (to Mrs. Brooks) This isn’t church.

MRS. BROOKS: I know. I’m thinking. Sometimes the process of a funeral and burial and doing things like putting wreaths on grave sites help give Closure.

CAITLIN: Devon was cremated so that will not work for me.

MRS. BROOKS: Sometimes talking can help both you [and your Dad] a lot. Talking about your feelings.

CAITLIN: That will not work for me. I don’t like Let’s Talk About It. – Is there anything else? (to audience) I start shaking my hands because the world is spinning and if I shake my hands faster than the rest of the world then the world’s spinning doesn’t seem so fast.

MRS. BROOKS: It’s something you have to find for yourself because everyone is different. We all have to find our own special way.

CAITLIN: (with a big sigh.) Fine. I will figure it out myself. (to audience) (Pg 74-80) When Dad drives me home from school, I stand in front of Devon’s door. Whenever I don’t know what to do I go to Devon’s room and ask him. I REALLY want to know about Closure. Except Devon’s not here. But his room is. I haven’t been inside since Dad slammed the door on The Day Our Life Fell Apart. When I push my head into the soft blue blur of his room I can smell him and feel him. (Smiling) It’s like pure Devon in here. I see it. My hidey-hole. The best place in the world. The corner between the foot of his bed and his dresser. He even used his Boy Scout knife to carve my name underneath his dresser.

(crouching down to see the underneath side of the dresser, Caitlin runs her fingers over her name) It’s not my real name. It’s Devon’s name for me which is Scout. It’s from To Kill a Mockingbird. It has two kids in it: Jem and Scout. They are a brother and a sister. The first time we watched To Kill a Mockingbird I waited through the whole movie for the dad to shoot a mockingbird. No one shot a bird for the whole entire movie. Devon said the title makes perfect sense and this is what it means:

DEVON: It’s wrong to shoot someone who is innocent and was never going to hurt you in the first place. You shouldn’t hurt innocent people Scout. That’s what it means.

CAITLIN: (to audience) I guess the evil school shooters didn’t listen in English class because they did not Get the meaning of that book at all. (Pg 148) [A few days later] my class goes to the computer lab. Mrs. Johnson says we have free time and can look up any topic we want to learn more about as long as it’s not computer games. I remember I should be researching Closure so I look it up and this is what I find: the act of bringing to an end; a conclusion – example: They finally brought the project to closure. I see Devon’s Eagle Scout project in my head. (Pg 2) It’s the chest Dad and Devon are making so he’ll be ready to teach other Boy Scouts how to build a chest. (Pg 149) I think about how much he wanted to finish it and become an Eagle Scout. And how he was going to teach me how to do woodworking too. And then I start shaking my hands fast and my heart is pounding in my ears. (Caitlin begins moaning)

MRS. JOHNSON: Caitlin are you all right?

CAITLIN: (Screaming loud enough for Devon to hear up in Heaven) I GET IT! I GET IT! I GET IT! I GET IT! (long pause, then, to audience) Now I know how to experience an emotional conclusion to a difficult life event.

TRANSITION As excited as Caitlin is about finishing Devon’s Eagle Scout project, it’s difficult for her dad.

CAITLIN: (Pg 162-163) (to audience) Dad sighs and looks at the sheet covered chest in the corner for the first time ever and I want to start shaking my hands but I know that does not make Dad happy so I sit on them instead. (to Dad) Dad, I want to finish the chest. I want to get to Closure.

DAD: (quietly) I know

CAITLIN: You need to get to Closure too. (Dad nods) (To audience) I think about what Devon would say. (To Dad) You have to Work At It Dad. You have to try even if it’s hard and you think you can never do it and you just want to scream and hide and shake your hands over and over and over.

DAD: (wipes his eyes, as his body begins to shake with controlled sobs. He covers his face with his hands and tries to compose himself. He sniffs twice and then turns to Caitlin) How did you get to be so smart?

CAITLIN: (Shrugging) I’m really working hard on finesse.

DAD: Do you really want to do this? You think this will bring us Closure.

CAITLIN: (shaking her head) No. I know it will.

DAD: (Blowing a little air out of his nose, he nods and sighs heavily) Maybe we can make something good and strong and beautiful come out of this.

CAITLIN: (To audience) Good and strong and beautiful. I like those words. They sound like Devon.

DAD: Okay. Let’s do it.

CAITLIN: (Pg 202-204) (to Dad) Do you remember that movie?

DAD: What movie?

CAITLIN: To Kill a Mockingbird. It’s a good one isn’t it?

DAD: It’s been a long time since I’ve seen it but it was one of the best.

CAITLIN: Devon liked it too.

DAD: (clearing his throat and clenching and unclenching his hand) Yes, he did.

CAITLIN: Do you think I’m like Scout?

DAD: The little girl in the movie? (nods) Very much.

CAITLIN: You’re like Atticus. He was brave.

DAD: Thank you. (sighs again) I wish I were more like Atticus. [But] Honey . . . we have to live in the real world. I like you as Caitlin.

CAITLIN: But you said the movie was the best.

DAD: For a movie. But this is real life. A movie isn’t as good as real life. It can’t even compare.

CAITLIN: (To audience) Dad is wrong about that. A movie is better than real life because in the
movies only the bad guys die . . . .
TRANSITION
And so the work on Devon’s Eagle Scout Project – Devon’s Chest begins

CAITLIN: (Pg 187-188) What is a Dad-oh?

DAD: (smiling a half smile) Day-doe. And it’s a grove in a piece of wood.

CAITLIN: (To audience) He is staring to smile. I know what that means. Closure must be coming! . . . So I Work At It (to Dad) I like Dad-oh better. Here’s the screwdriver, Dad-oh. Would you like a glass of water, Dad-oh? Can I help you, Dad-oh? (to audience) And his lips curl up on the left side every time. Closure is a very good thing to see. After Dad-oh goes to bed, I sneak into Devon’s room and borrow his Boy Scout knife. I slide my head under the chest and look for the perfect spot. I carve in big letters on his chest, just like Devon did for me: SCOUT! (Pg 212) [We worked on it together for weeks and now] our chest is almost done. I draw what I want to carve into the top part of it. The bird is gray and black and white and has a long tail. Her head is tilted up and her beak is open like she’s singing. She is beautiful. I run to the living room to show it to Dad.

DAD: (taking the drawing with one hand and rubbing his chin with the other – puzzled) It’s not . . . It doesn’t look [like an] eagle.

CAITLIN: It’s not an eagle. It’s a mockingbird.

DAD: (tiling his head to one side) I thought it was an eagle because this is Devon’s Eagle Scout project.

CAITLIN: It’s a mockingbird . . . like in the movie. Remember? Because Devon was like Jem. And I’m like Scout. And you Dad – you’re like Atticus. (Pg 218-219) (Caitlin suddenly begins to cry and can’t stop) Dad-oh! Dad! Oh Dad!

DAD: (pushing the hair from Caitlin’s face) What is it Caitlin?

CAITLIN: (between sobs) Devon . . . . Devon.

DAD: I know. It hurts. You miss him. I miss him.

CAITLIN: But I’m not crying for ME! I’m crying for Devon! I’m crying because I feel bad for HIM!

DAD: (smiling through his own tears) Now you know what it’s like to feel for other people.

CAITLIN: (To audience) I look over at Devon’s chest and it makes me feel good. (to Dad) We did a great job on it, didn’t we Dad? We made something good and strong and beautiful.

DAD: (nodding) We sure did. Devon would be very proud.

CAITLIN: (To audience) I nod too. I think about Devon and how he would show it to all the Scouts and tell everyone how we made it and how we used it to find Closure. That’s when I feel my mouth turn into a grin and my hands start shaking so hard I have to leap off the sofa and jump around the room because just shaking my hands isn’t enough for all the excitement. . . I finally Get it! I Get It! I GET IT!
```

---

## IC-0207: Mom from Another American: Asking and Telling

- Title: Mom from Another American: Asking and Telling
- Author (byline): Marc Wolf
- Work: Political Stages: A Dramatic Anthology (Emily Man & David Roessel eds) Pgs 604-608
- Publisher: Applause Books
- Publication date as stated: May 2002
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MOM
- Teaser before the introduction: Yes
- Spoken words (computed): 1249
- Already set (do not supply): none

### Source block (context only)

```text
Author: Marc Wolf
Book: Political Stages: A Dramatic Anthology (Emily Man & David Roessel eds)
Pgs 604-608
ISBN: 978-1557834904
Publisher: Applause Books
Date (Month/Year): May 2002
```

### Introduction (context only: never use it for content warnings)

```text
On October 27, 1992, Petty Officer Allen R. Schindler, Jr., 22, was brutally beaten to death in a public restroom in Sasebo, Japan, by two of his shipmates, Terry Helvey and Charles Vins. They beat and stomped Schindler to death because Schindler was gay. Their attack was so vicious that they destroyed every organ in Schindler’s body. Allen Schindler’s mother, Mrs. Dorothy Hadjys- Holman, could identify her son only by the remains of the tattoos on his arms. The medical examiner compared Schindler’s injuries to those sustained by victims of a fatal airplane crash or a high- speed automobile accident - all but two of Schindler's ribs had been broken, his penis bore cut marks and his liver contained holes that allowed the pathologist to see straight through
```

### Performance text (classify this)

```text
MOM: (Pg 604-608) I knew that he hated it—and. . .that ship. And he wasn't-- matter of fact when he was home I think he really wanted to go AWOL but he really didn't want to get into trouble either and now I wish I would’ve never let him go to the airport. . .

it. . .

Mom from Another American: Asking and Telling by Marc Wolf

MOM: The night before Allen was killed he called me to tell me that his paperwork was gonna be there any day now and he'd be discharged and he'd be home before Christmas for good. And then 24 hours later they were at the door knocking at the door telling me he was dead.

Matter of fact, I had on one of those long night shirts? It was only 7:15 and I was home alone and I didn't expect nobody to come over so when I came home after I ate I just went and took my clothes off and put it on and was watching TV and they came to the door and any mother who has somebody in the service knows that if two guys come in dress blues that's something bad--and um they told me that Allen had been assaulted in a park in Japan and that he was dead and I sat here for about 45 minutes before I even realized I didn't have any clothes on. I was hysterical that night but compared to the night when they called me from California and told me I wouldn't want the coffin open?--that was the worst.

Until then I had no idea how he was killed you know I didn't know if he was shot or stabbed. At first I didn't even know it was Americans who killed him--shipmates. They were shipmates on the same ship—

The Navy did not tell me. Every time I would ask them they said they were looking into it. The Navy wouldn't tell me--they would never admit Allen was killed because he was gay. They they don't know why he was killed. Just that Terry Helvey was drunk. Terry Helvey kept giving different statements; everytime the wind blew he gave a different statement so they didn't know what to believe. And Charles Vins just kept his mouth shut. He wouldn't say nothing so he said that he would tell the truth if they would make a deal with him and not charge him with murder.

So that--after they made the deal...he told them you know what did happen. It wasn't until after the deal was made that he also told them that he also kil--kicked Allen three times. That he was an accomplice. I mean he served 72 days. You know I I cannot understand how someone can watch somebody get killed, even if he hadn't done anything--how he could stand there and watch happen what happened to Allen and do nothing--and then just be charged with failure to report a crime.

Terry Helvey's shoeprint was embedded in my son's face.

The whole time I waited for his body to return, I thought that um I would be able to hold him and I would be able to kiss him goodbye and then they told me that there was nothing that they could do to make him presentable and that I really should never open the coffin. My minister begged me not to open the coffin cause he had seen it and not to go in there and look at him but there was nothing that was gonna stop me from going to see him.

And I went in there and--and I couldn't hold that body. I mean it looked nothing like my Allen. It was nothing like my Allen. And then they closed the coffin and the whole day I thought how do I know it's him? I mean sure the hat's there and the uniform's there and it has his pin on it that says Schindler but how do I know it's him? And the next day during the wake that we had for him it just kept going through my mind. I'm gonna have to open up that coffin again. And I'm going I r...really I don't think I can do it. And just before the wake was over I went out in the hallway and I talked to my daughter Kathy and it was really funny cause she wanted to talk to me the same time I wanted to talk to her and we both wanted to say the same thing.

She wanted to say, "Mom, how do we knot that's Allen?" And so she agreed--her husband and her, that when everybody left they would reopen the coffin and they would roll up the sleeve and see if his tattoo was there. He had a shark on one arm and he had a tiger on the arm--other arm and he had the emblem of the USS Midway the ship that he loved on his arm but I was upset when he got the tattoo--you know, disformed his beautiful body you know but if it wasn't for that tattoo to this day I would not know that's him in that coffin...

If somebody could show me in the Bible where Jesus says--I don't mean Paul or anybody else but where Jesus says that I'm not to have anything to do with homosexuals, where I'm to condemn 'em because they're worthless and I mean that's the way I feel that a lot of these ministers make it seem like they're worthless. There's people out there like Jerry Farwell. I think if I could ever (BEAT) stand as close as I am to you with Jerry Farwell I would slap him in the face. I mean he just preaches so much hatred.

Allen's up in heaven. No matter what...those evangelical Christians think, I think Allen's in Heaven.

D'you wanna hear something really weird? OK. I have a nephew who's--he's seven years old now so like he was only two and a half, three when Allen was killed, so he really doesn't remember Allen much. I mean he remembers a little bit about him. And then he, you know, from being on the news and everything like that but he believes that when he--if he has a balloon or something and it goes off up into the air then Allen catches it.

So a couple of weeks ago was my grandson's birthday and we had bought some helium balloons and there was some--two purple ones and Allen's favorite color was purple and so James was kind of acting up so I said "Well James why don't we go get the purple balloons and then we'll release them and let Allen catch 'em up in heaven." And it was real windy out and we went outside and we—

Him and my grandson were gonna release the balloons up in the air [breath] And they went flying off so far cause it was so windy. They went really way up and finally they got to the point that we couldn't see 'em, and the minute we couldn't see 'em like a storm came and I mean it came down like buckets just like that and it only lasted for a couple of minutes and then it was gone. Anybody'd think I'm really crazy but it was like Allen saying, "I caught it Mom."
```

---

## IC-0208: The Monologue

- Title: The Monologue
- Author (byline): Marla Bentz
- Work: The Book of Monologues for Aspiring Actors
- Publisher: NTC Publishing Group
- Publication date as stated: 1995
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SARAH
- Teaser before the introduction: No
- Spoken words (computed): 2387
- Already set (do not supply): none

### Source block (context only)

```text
Author: Marla Bentz
Book: The Book of Monologues for Aspiring Actors
ISBN: 0844257710
Publisher: NTC Publishing Group
Date (Month/Year): 1995
```

### Introduction (context only: never use it for content warnings)

```text
Sometimes, when you get a girl talking, it’s difficult to get her to stop. I mean, it’s like riding a bike downhill with no brakes. Especially if it’s one of those back pedal brakes…you know, those were always easier for me than the handle ones. I think it’s something to do with my hand-eye coordination. That sounds like something a gym teacher would say. But I never really liked my gym teacher much, she was always sweaty and loud and- “The Monologue” by Marla Bentz
```

### Performance text (classify this)

```text
SARAH: Hi, I'm Sarah Walker. Why did I say that? You know that already. This is the first time I've ever auditioned. Professionally, I mean. For an actual role. School plays, church, things like that, I auditioned, but never - I'm sorry, I already said that. You want me to tell you about myself. God, I don't know what to tell you. I'm seventeen. I graduated from the School of Performing Arts last month - Oh, yeah, I guess I did audition professionally. I mean I was in the chorus of a musical. But that hardly counts, does it? Nearly everyone in my class was in the chorus of that musical. And it closed after one night. It closed after half a night. Everyone walked out. Right in the middle of a number. Like a trail of ants. They trickled right out. And there we were, singing and dancing and... I was born...I mean, this might be interesting. I was born in Liechtenstein. There aren't many foreigners born in Liechtenstein. Not many people born in Liechtenstein. See, my parents were on this trip, and I was born early, and I was born in...

I came home when I was a week old. To British Columbia. Maybe I should explain that. My dad was working in British Columbia. I mean I'm not Canadian. Not that there's anything wrong with being Canadian. I'm not a Liechtenstinian either. Is that the word? Liechtenstinian? Sorry, I'm babbling. Mom said she thought I started performing the day I was born. She was just kidding, of course, but I can't remember when I didn't want to be an actress. Oh, God, I thought. It would be so wonderful. To be someone else, to be anyone else, to be a lot of other - I didn't want to be me. Never wanted... So, anyhow, I was always singing and dancing and reciting nursery rhymes. My mom says I knew the whole "Night Before Christmas" when I was a year and a half. A year and a half old, can you imagine? I'd say it at the drop of a pin. That's not right. Drop of a hat. That's right; that's what it is. Isn't it? So, anyhow, I started singing and reciting poems and things in school and church and family reunions - I was never nervous. You might think I'm nervous. But I was never nervous. High-strung like a thoroughbred. That's what Dad said. He didn't know anything about horses. Never even saw a race. That's what he told me. You're letting me babble on here. (Laughs nervously.) So maybe I could recite something. How about it? What do you say? Can I recite something? Nah, I better not. You want to hear about my life. Well, there's nothing important. I grew up in - Oh, yeah, I used to play the accordion. Squeeze box is what Grandma called it. (Broadly pantomimes playing an accordion.) Bagpipes. That's what I thought the accordion sounded like. Don't ask me why. Same principle, I guess. Air squeezed in and out to make the sound. Bagpipes are always so, I don't know so...so mournful. Like the cry of a lonely siren (Caught up in the mood) luring sailors to deep, vast graves in the sea. (Snapping out of it) But you don't want to hear about bagpipes; you know about bagpipes. The whole world knows about bagpipes. Maybe not the whole world. (Takes a deep breath and expels it.) Where was I? Oh, yeah, so I grew up in Jersey. Newark. Can you imagine growing up in Newark? I didn't really grow up in Newark. I moved here when I was thirteen. I mean when I found out about the School of Performing Arts, and that the kids there got to audition for shows. Professional shows. Wow, you know. Anyhow, I came to stay with my grandma. And I went home weekends, except when I was in a (Exaggerated French accent) tragedie ou comedie ou a lettle chanson ou danse nombair. (Seriously) I didn't really want to go home. It was so strange going home. Back into all that - back into everything - I mean like Mom never even said any- I'm making a fool of myself up here. Isn't that what I'm doing? Making a fool of myself. Well, so what? You wanted to hear me talk; you wanted to hear me sing and act. Did you want to hear me sing? I don't have any brothers and sisters. Mom says who could put up with another one like me? She was just kidding...I think. (Laughs and points straight ahead.) Of course, she was kidding. (Seriously again) Except I know she and Dad would have been much happier if - I didn't ask them to be born, did I? And then the way he - I mean, nobody deserves to be tr- (Brightly) Say, don't I get to read or something? Oh, yeah, the paper you handed me. (She pantomimes looking at a sheet of typing paper.) When I'm done telling you about myself, I'm supposed to read it, act it. But am I done telling you about myself? I mean, I'm done telling you about myself if you want me to be done telling you about myself. But, I can...Oh, well. Yes, now. I see. It's on the paper here. You told me my audition piece was on the paper here. Nothing prepared, you said. A cold reading. Right here on the paper. OK, here we go. Here it is. (Reading from the imaginary paper, almost to herself) "To be or not to be..." Oh, sure, I know that. Everyone knows that. Doesn't everyone know that? (Reciting in broad Shakespearean tones) "To be or not to be, that is the question. Whether 'tis nobler in the mind to suffer the slings and arrows of outrageous for - " Hey! Wait a minute here. This is Hamlet. This is a boy. I mean, not a boy, but a man. A young man. Maybe not a boy; he is in college, I think. Isn't he? A college boy. Man. Isn't Hamlet in college somewhere? Sweden, Denmark, something like - Oh, yeah, of course, he's from Denmark. He's Danish. Danish? How do you get Danish out of Den - Lochtenstunian! Maybe that's what I'd be if we hadn't come home. To British Columbia. To Newark. To...Actually, I don't know why they brought me home. They never wanted - And so - anyhow, I was glad to live with Grandma. I had to get away. Oh, God. Hey, wait! Whoa! Hold everything. The fine print. I see the fine print here. (Quoting from the imaginary paper from which she'd been reading) This company was founded for the purpose of expanding gender and ethnic roles. (Puzzled) A Dane is ethnic? So what am I? Aren't I ethnic already? I mean besides the way I look. See the way I look. And you have me playing a Danish white boy? I mean, hey, like they used to say, get with it! Ooh, sorry, I didn't mean anything. Wow, if I say stuff like that - I mean, if I keep on saying stuff like that, I'm really going to blow it, aren't I? So shall we try it again? "To be or not -" Expanding our views and our roles, is that it? You know I kind of admire that. No, really, I mean I do. I really admire that. So, hey, should I try a little dance step? Why don't I try a little dance step? (Doing a chorus line step) One and a two and a one and a two and a - Remember Lawrence Welk? Oh, God, when I was a little kid, I used to sit in front of the TV set when reruns of the "Lawrence Welk Show" came on. I wanted so badto be one of those sisters, what were their names? You know, the sisters who sang and all that stuff on the "Lawrence Welk Show"? I envied them so much. And Patty Duke. Remember her as a little girl with her own TV show? And those old movies? Shirley Temple and Margaret O'Brien. I'd give anything if I could have had a life that was just a little bit like - Sorry. I'm really sorry. Oh, wow, you've just got to know how important this is to me. It's really important. More important than food and sleeping and...well, you know, don't you? Sure, you know, it's like the most important thing in the whole wor - Not really the most important.

Grandma - well both Grandmas. And Grandpa... (Mock serious) I never knew my one grandpa. Now don't get the wrong idea. He didn't die or anything. He was one of those astronauts who went to the moon. The one you never heard about, the one they all kept quiet about. It was my grandpa. Went to the moon. A young man. And he liked the moon. And so he decided to live on the moon. (Trying to keep from laughing) No, really, my grandpa's alive. Both grandmas and grandpas. It's really my uncle who lives on the moon. (Laughs.) My grandma was a singer. Mom's mom, and Grandpa played guitar. That's how they met. Isn't that romantic? Now isn't it? And it's the truth. My other grandma plays the piano. Grandpa isn't musical though. He collects stamps. So where was I? Oh, sure. A one and a - Nah! You don't want to see me dance. You want me to recite something? What? What can I recite? I know. (Very hammy) "It was many and many a year ago In a kingdom by the sea. There lived a maid whom you may know By the name of...Sara Lee?" Funny. (Almost pleading) Isn't that funny? You see, that's my name. Sarah Lee, with an "H." Sarah Lee Walker. (Parody of a western movie) So, what do you think about that, pardner? (Her normal voice) Are you just going to let me die up here? I don't mean really die. I mean die like in doing a terrible job, not knowing what to say or do. Or I got an idea. I'll tell you about my hobbies. (Long pause) I don't have any hobbies. The only thing I'm interested in is being an actress. That's my whole life's ambition. Everything else revolves around that. I'm being serious. I mean it. I know I've been kidding a lot, because, believe it or not, I didn't know what else to do. What else to say. But not now. Why do people want to be actors or actresses? Why do I want to be an actress? I don't really know. It's just the most wonderful feeling in the world. Everybody watching and listening and the house so still you can hear a hat drop. (Laughs and points.) Got you again, didn't I? (Seriously) No, but I mean it. It's not like I want to control people, or even that I feel I'm so important or special. (Pause) Even though I am. Important and special, I mean. Kidding. Just kidding. (Seriously again) It's like I'm this instrument playing a duet with...God maybe? Or the consciousness of the universe. And everything's aligned somehow. And I'm the chemical catalyst or the reed of a tenor sax or the sounding board of a piano. And if I've rehearsed and studied and am confident, well, it's like I'm playing and being played so the audience hears one pure, sweet note. Or a resounding chord. (Changing abruptly) So you heard any good jokes lately? You'd think with my wanting to perform and loving to be up here on-stage that I'd be pretty good at telling jokes. Well, I'm not. I always mess up the punch line. I forget it or something. I wonder why. I can say lines in a play just fine. Right intona-tion and emphasis. But I can't tell a joke. Maybe life itself's a joke. And we're stuck with one role. I was stuck in one role. A role I hated, till I moved in with Grandma and Grandpa. Can a person be an actress just because her life is - because she wants to get away, to escape - God, I'm seventeen years old. Why did I want to escape? Why do I still want...to...escape. (Tears in her eyes) It was like Mom didn't care. She knew what was going on. What Dad was doing to me. But she just didn't (An abrupt change) So, hey, do I have the role or don't I? I mean, I feel like I've been up here forever, and I haven't said a blessed thing. Haven't done a blessed thing. I mean I was always good at ad-libbing. When I was in junior high, before I went to the school of performing arts, I joined the speech club. You know, readings and contests and stuff. Well, I always did well with the impromptu event. Give me a subject, and whether I know anything or not about it, I can talk. I'll show you. Give me anything to talk about, any subject. Say it's... quantum physics. All right? Ahem. Ahem. Good evening, ladies and gentlemen. Quantum physics, huh? What made me think of quantum physics? I don't know what made me think of quantum physics. Black holes. That's it. Quantum physics and black holes. (Orotund tones) Ladies and gentlemen, a discourse on black holes. What is a black hole, ladies and gentlemen? It's a hole in the sky. A hole in the sky that's black. Not brown, not green, not red. But black. Yes, people, it's black. And why is it black? Well, because...it isn't really there. It's somewhere else. It's in some other universe. Ha! Didn't think I knew that, did you? A tunnel to the future or the past. Anti-matter. But you can't go through a black hole. If you tried to go through a black hole, it's hard to tell what would happen besides being crunched down so you'd cover only one billionth of a billionth of a pinhole... So thank you, ladies and gentlemen. My mother thanks you; my father thanks you; my grandmother thanks you; my grandfather thanks you. (Her voice trails off.) All of them... (Sadly) That's dumb. Mom and Dad wouldn't thank...they wouldn't care. But the big thing is that I'll be on my own, and Dad can't - (Realizing what she's saying) What am I saying?! But if I can play at being someone else, at least for a while, I really can be that person, become that person, do you see? Everything's better. Everything's different. I'm different. And Dad can't do those horrible things anymore, and Mom can't pretend she doesn't know what - (Panicky) Oh, my God, I'm sorry. I shouldn't say things like - I'm...sorry. (Brightly) SO...what else would you like to know? (Pauses as if listening to a response.) I can quit! I really can quit now. And I have the job. Oh, wow, I'll have to tell Grandma and Grandpa. And I'll tell Mo-

(Suddenly, she becomes dignified and composed, a young woman in command of her life.) Thank you. Thank you very much. (She nods and hurries Off-stage.)
```

---

## IC-0209: The Moonshot Tape

- Title: The Moonshot Tape
- Author (byline): Lanford Wilson
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DIANE
- Teaser before the introduction: Yes
- Spoken words (computed): 1626
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lanford Wilson
ISBN: 978-0822209126
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
Confession is not only good for the soul, but beneficial for the theater as well - especially when the characters spilling their secrets have been created by playwright Lanford Wilson.

In The Moonshot Tape, our confessor is Diane, a short story author, who has returned to her hometown to move her aging mother into a nursing home. During her stay, she is interviewed by a reporter from her old high school’s newspaper – after all, she’s become one of the most successful graduates of Mountain Grove High School. But memories of her childhood are brought back by the naive questioning of the student. What returns are tales of sexual abuse by her now-dead stepfather and how she tried to exorcise those experiences.

The Moonshot Tape by Lanford Wilson
```

### Performance text (classify this)

```text
DIANE is thirty-five. She has short hair, jeans and a T-shirt, socks, no shoes. When she reads, she uses dime-store reading glasses. She speaks to an interviewer, who would be sitting against the fourth wall. She is trying to be cordial, but she has a "to hell with it, let the chips fall where they may" directness that hides a natural warmth and also masks a pain and grievance of which she is only partially aware.

NOTE: [words in brackets] are not found in the original text – modified for suitability for high school performance.

DIANE: This isn't bad, this joint. As it turns out, the rooms are perfectly adequate, they're clean, the heat's a little eccentric, but there's a bathroom with at least a shower. . . The evening sessions, getting Mom to sleep, take it out of you. It was her idea to go there, insisted on it, looked forward to it almost, but. . . (Pause.) Half the inmates are insane or senile or something. The lady in Mom's room - She doesn't know if she has to go to the bathroom, if she's eaten, if she's slept. So she says, "Lady? Lady? Lady? Whatta I do now? Lady? Whatta I do now?" (Pause.) That's going to wear thin, I can tell. Even for Mom, who has the patience of the angels. (She looks at the list.) "Where do you get your ideas for stories?" (She sighs)

DIANE: "Where do you get your ideas for stories?" (She sighs, then thinks seriously.) You know, sometimes-well, it's always, unfortunately, just yourself you're writing about, but sometimes they're blatantly autobiographical. My side of the story, that's always fun. Never underestimate the power and excitement of revenge. (Without a beat she breaks off) "Where do I get my ideas?" Sometimes I start writing something, it turns into a piece that's been kicking me around forever; and I think, Oh, good, I'm finally doing that. Then I'll go months with nothing. Like if you weren't here now I might be writing a story about a girl coming home to help her mother move into a nursing home. Or just coming back for a visit and seeing the town, or someone from school, or any of the things coming back home does to you. Being invaded by those memories, those times, those voices, the pictures. And the various lies you tell of your history to protect the guilty. So. (She looks at the paper again, tired of this, exasperated, almost pissed.)

"How much of an influence has Mountain Grove been on your writing comma your life?" Buckets. Whole bucketsful. (Pause.) I'm sorry. You've caught me at low ebb, or a bad time. I have all these feelings, guilt trips, ghosts, bombarding me here. (Pause.)

For instance, my father left Mom and me when I was five. Mom didn't remarry until I was eleven: Tom and Edith and little Sam, who was three and a half and never spoke. (Pause.) Mom was frail and quite a bit older than Tom and always the peacemaker; nothing was to upset the order of the household, the sanctity of the home we hear so much about. Just put a lid on it and let it boil. And Tom was the quietly expansive, friendly type that everyone loved. Good job at the cheese factory, nothing flashy or threatening, just a good ol' Joe who started coming into my room sometime during that first year. (Pause.)

He'd stand by the side of my bed in the dark, pull the covers back and feel my breasts, rub [himself] against my cheek, turn my head over, and [well, I don’t have to spell it out for you]. Then he'd cover me up and go to the door. Stand there, very quiet, forever. . . I never knew why. . . then go back to bed. (Pause.) That was only when he drank. Maybe once every three weeks. The room would reek from him. Cigarette sweat and boilermakers. I thought, of course, that it was some sort of punishment.

You can't imagine how good I was. I'd help in the kitchen, set the table, do the dishes, wipe the counter, clean the refrigerator, do my homework for the next month, read all the elective outside-reading assignments, fall asleep, and in a few hours I'd wake up with his hand brushing my forehead and lie very still. The two or three times I tried to turn my head he yanked it back with such violence I thought he'd break my neck. So. Eleven, twelve, thirteen, fourteen, fifteen, sixteen. If you believe it. I put a lock on my door when I was fourteen; he took it off. I went to Mom, said, "Mom, at night, after you're asleep, Tom comes into my room"-and she slapped me halfway across the house. Told me never to lie again. (Pause.)

So I came back here, for our fifth high school reunion, contrived to get everyone but Tom out of the house one Sunday afternoon. Tom was very respectful. I was important, of course, and an adult now. And Tom had found God . . . . So I showed him how the police tied us up to take us off to jail - they hadn't actually, and as a matter of fact, I was never in jail, but it comes in handy from time to time to be able to tell a story.

So there he was, with his feet belted together and his hands tied behind his back, lying on the middle of the living-room floor. I wish you could have seen it gradually . . . dawn on him that he was helpless. . . . (Pause. She lights a cigarette. Maybe she pours a couple of fingers of vodka and has a belt as well.) Never underestimate the power and excitement of revenge. (Pause.)

I wandered into the kitchen, got myself a soda from the fridge. Tom started calling, "Diane? Where'd you go, honey? Diane, this ain't funny, sweetheart." I looked around the kitchen -- Mom had a regular slaughterhouse in her knife drawer. Mallets and cleavers and a collection of butcher knives that was absolutely sobering. But I selected the weapon of my trade - an indelible, permanent-ink, felt-tip pen that Mom used to mark packages of meat . . . and I went back into the room with Tom. I sat down beside him on the floor and very slowly started unbuttoning his shirt and pants, with him starting to say now, "Oh, don't do that, Diane, honey, I'm gonna tell your mother," if you can believe it.

I went back into the kitchen, got the scissors, scared him to death, but only to cut his clothes off him. I just said, "Tom, don't tell me you've forgot all our nights together."

He's yelling, "I don't know what you're talking about, you just dreamed that."

I said, "Why, Daddy, that's every little girl's dream-in the minds of men."

He's going, "Oh, God, no, oh, God forgive her." Maybe if he'd said, Oh, God, forgive me . . . and I told him, "And I'm gonna write you a little story, Tom, that I want you to treasure, 'cause I get about three thousand dollars for something like this." And I took that nice indelible pen, wiped the sweat off his pretty blank white hairless chest and wrote: "Once there was a little girl whose guardian came to see her in the night."

He's bucking around, yelling, "You're not really writin' that, don't mark me up." I said, "Oh, honey, you marked me up."

My story went something like - I'm saying it aloud, writing: "He liked to put his hands on her to excite himself, and he liked to rub himself on her red cheeks - her cheeks must have felt like flames. And when couldn't stand it any longer, he'd put it in her mouth to cool himself off. And that's how he took care of his little ward. And that's how his little ward took care of him. (Pause.)

Probably a little more Dickensian than most of my work. Of course, he was screaming and bucking. I wasn't proud of my penmanship, but under the circumstances . . . and I went slow enough to make sure it was legible. Then he was saying, "Stop it, don't do that. I don't do that anymore. I was drunk. It was the devil, darlin'," wailing like a revivalist.

So I got my overnight bag and got the car keys that had fallen out of his pocket onto the rug. And left him there, hogtied and inscribed in the middle of the floor. Naked as the day he was born-looking like the pot-gutted tattooed man. Then I stood in the doorway for a long while like he used to do. Only he wasn't pretending to be asleep; he was twisting around on the rug, yelling, "Untie me, dammit. Diane, where do you think you're a-goin'? Don't leave me here all marked up." I went out to the car, drove it to the airport, and left it there.

(Pause.)

Mother was livid. He told her it was a game, but she didn't see the fun in it. She liked everything to be peaceful. So she came to visit me, I didn't come back here. Not until Tom got so bad that she was nursing him and couldn't leave. Right toward the end I came here to see her. I was only in the room with Tom for a few minutes. Tom said he'd tried to read my stories, but they were filthy and depressing, and he told me that writing was just lying and getting away with it. And I said, "No, Tom, writing is the only place I know of where you can tell the truth and get away with it." (Pause.) He died about two weeks later. (Glancing at the list.)

Why do I write short stories instead of novels? Obviously I like ending things, that's all I've done. You can end eight or ten stories in a space that you could only end one novel. I like tying things up or I wouldn't be here now; where it's so much fun with all those memories of childhood; walking back over Mountain Grove, where everything is sweet and fine and nobody has any secrets.
```

---

## IC-0210: Most Massive Woman Wins

- Title: Most Massive Woman Wins
- Author (byline): Madeline George
- Work: The Best American Short Plays 1997-1998
- Publisher: Applause Books
- Publication date as stated: 2000
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SCENE, AT RISE, CARLY, SABINE, CEL, RENNIE
- Teaser before the introduction: Yes
- Spoken words (computed): 3387
- Already set (do not supply): none

### Source block (context only)

```text
Author: Madeline George
Book: The Best American Short Plays 1997-1998
ISBN: 978-1557834263
Publisher: Applause Books
Date(Month/Year): 2000
```

### Introduction (context only: never use it for content warnings)

```text
It takes courage to face a world where fat is equated with personal failure, lack of self-control, and lack of femininity. As four women in a liposuction clinic share their stories and childhood memories, they strive for a new understanding of beauty. Body image affects us all, and The Most Massive Woman Wins by Madeline George speaks to our closeted inadequacies and how we punish ourselves for our "imperfections."
```

### Performance text (classify this)

```text
SCENE: The play takes place in a liposuction clinic waiting room. - It is important the play be established as humorous from the outset. - A great deal of the 'dialogue' is directed out to the audience; they are often able to pick up on each others' thoughts without speaking straight at one another. - The chants are genuine hopscotch, jumprope and handclap rhymes from my own childhood and other children in Amherst, Massachusetts. - We used blocking inspired by children's games: London Bridge and Mulberry Bush for the scoliosis check, Red Rover for the thesis defense, Musical Chairs for Carly's job interviews. Monologue Notes - Carly talks hard and fast and never gets sentimental, but she loves her kid. -Sabine is extremely hard on herself and never gives herself a break; instead of getting sad she always gets angry, right through to the very last line -Rennie is perpetually panicked and jumpy; it's as if there's nothing holding her down to the floor. She laughs a lot to disguise her fear. -Cel is not crazy. Her monologue is driven by her own need to tell her story. She does not relive the moment of her self-immolation, she tells us about it (this is important). Realization and catharsis come at the very end of the monologue, not before.

AT RISE: The light is bright and sterile. SABINE, CEL, CARLY and RENNIE are seated on the chairs. For several minutes they stare at their magazines, fidget, cough, cross and recross their legs and flip magazine pages in an otherwordly, choreographed little dance.

CARLY: It starts like a tidal wave under your feet and grows and grows until you forget your name and the people you love and all you know is you have to eat.

CARLY: You sneak out of bed, you don't think he hears you, you run down the stairs to where you hid the Sugar Smacks behind the TV; you're alone at last and you're eating great fistfuls, hand over hand. It tastes like everything you never had.

CARLY: You eat and you eat until you can't fit another bite into your body, you're bloated, drowned from the inside out.

SABINE: A beached whale, you can't move an inch.

CEL: You're done.

SABINE: You're done for.

SABINE: Regain control.

CARLY: And you go back to doing what you were doing before.

SABINE: But you know you did it.

CARLY: It's your fault - you lost control.

CEL: You know better than that.

SABINE: SO it's time to make an adult decision.

CARLY: [Smacks her awn butt.] Throw out the evidence.

RENNIE: You think of every sin in your past

CEL: Every slice of pie

CARLY: Every french fry

SABINE: Every chocolate croissant

SABINE: You are responsible for your own behaviour.

RENNIE: You are guilty.

CARLY: The other night my boyfriend goes to me, he's spread eagle on the couch giving his gut some air watching Monday Night Football and during the commercial he goes, "We don't have steak anymore. How come is it we never have steak?" I'm about to say, "You want steak, buy steak. Take it out a your paycheck, if you want steak so bad," but then he says to me, like, right in the same breath he goes, "What am I saying? You're too fat for steak. Last thing you need is fatty red meat." Just like that, then he tips back his beer and the conversation's over.

It's like I can't tell him off. Then later he leaves me this liposuction ad he clipped from the classifieds on my bedside table with a signed blank check. Is the guy subtle or what? You think it doesn't make me sick? What's the matter with me that I can't tell Frank Nowak where to stick it? I'm a weenie, that's what. A big fat wimp. How am I supposed to look my own kid in the face? [Lights shift, whistle.]

CARLY: What about benefits?

RENNIE: [Strongly emphasizing the 'Mizz.'] We haven't yet decided if this is an appropriate job for you, Ms.

CARLY: Kinski.

RENNIE: Let's hold off our discussion of fine points and sundries until we are able to come to a full understanding.

CARLY: Sure thing, sir. [Whistle.]

SABINE: Let me be frank, Ms.

CARLY: Kinski.

SABINE: I don't think you have fully considered the physical taxation that is put on a person in this line of work.

CARLY: Sir, I been in food service all my life.

SABINE: The waitstaff here are part of our family. And because of the extreme demands placed on their persons I demand that every member of the family be in peak physical condition.

CARLY: Alls I'm saying sir is I can do this job and I just wanna know about the benefits you - [Whistle]

CEL: [Overlapping.] I'm afraid I'm not fully getting through to you, Ms.

CARLY: Kinski, Kinski.

CEL: Allow me to speak as plainly as possible. I really don't think the restaurant can use a woman of your stature at this time. Please don't take this personally, but with the aesthetic atmosphere I am trying to cultivate there are certain, hmmm, discrepancies that cannot be tolerated.

CARLY: I been trying to tell you [Whistle.]

RENNIE: [Cutting in.] Most of the girls I hire are eighteen, nineteen years old. [Whistle.]

SABINE: They haven't been through what you've been through I'm sure. [Whistle.]

CEL: I hope you won't be unduly upset by this. [Whistle.]

RENNIE: Not everything can be fair in this world, I'm afraid.

[Lights shift, hospital gowns fly in, the women stand behind them and undress during the next exchange, then put the gowns on.]

CARLY: My mama was - she used to say "plump and juicy.»

RENNIE: My mother said for big girls like me it was ugly to let people see the stuff you were made of. Especially legs and shoulders and the inside of your mouth.

SABINE: Our mothers all taught us the same thing.

CARLY: Hush up, Carly girl.

SABINE: Sit still till we get to grandma's and mama'll give you a cookie.

CEL: If you're good you can lick the bowl.

CARLY: Do you kiss your mother with that mouth?

RENNIE: Sit up straight and eat only what you're offered.

SABINE: Children are starving in Denmark.

CEL: Eat your peas.

SABINE: Or was it Detroit?

CARLY: Open wide!

RENNIE: What's the matter, don't you feel well?

CARLY: What's wrong, don't you want dessert?

SABINE: Here, darling, have some of mama's home baked cherry pie.

CEL: Chicken-fried steak.

RENNIE: Chocolate mousse. [They all laugh and "mmm" in agreement. ]

CARLY: Baby, you are so be-yoo-tiful, just like a calendar girl with those big brown eyes and that beautiful skin!

RENNIE: Why did everyone always tell me I had beautiful skin?

CARLY: And babes, someday you'll thank me for letting you put on that extra padding. When your airplane crashes on the highest peak of the Himalayas all those skinny passengers are gonna starve to death seven ways till Sunday and you will survive for months and months, living only off what you have stored in your tush.

SABINE: Mama's always right. You just wait.

[RENNIE, CEL and SABINE return to their corners to sit, lights up on CARLY in the center.]

CARLY: No my mama was not always right. No, you should a seen her when he'd come home nights, the whole place'd get quiet like the grave, I swear, she'd be pussyfootin' around him jumping like a sick kitten every time he made a move... all you could hear was him chewing with his mouth open and his silverware hitting the plastic plate. It's too late for my mama, it's too late for me now. But the day my kid was born I made it a promise that she was gonna know who she was. No one was gonna walk all over my kid. No one was gonna give her a goddamned blank check. Then the other day I come home from work and there she is, my stupid kid, sitting on the bathroom floor, leaning against the tub, and her long blonde hair is dyed pitch black, I swear, black as tar, and it's dripping black rivers all down her face and her neck... I could have killed her right then and there, I wanted to knock her head off of her skinny little neck. Instead of killing her I say, Jesus Christ, what the hell did you do to your hair, and she's crying and choking and she goes, Ma! and points at the counter. I looked and I swear I thought I was going to toss my cookies. She has got one of these EPT plus pregnancy tests laid out there, you know, the little stick kind? Pink, pregnant, white, not pregnant... there's that little stick leaning up against the box it came in and the end is as bright pink as an Easter egg, pink like a baby's butt is pink. Talk about history repeating itself. Suddenly I'm sixteen again with that sinking feeling in my stomach looking at the little test tube, holding it up against the light bulb in the upstairs closet.... So I'm trying to figure out what exactly the black hair has got to do with the pink stick. I say, Is that or is that not an EPT plus pregnancy test? and she nods, so I say, Is that or is that not a pink stick you got there? and she says, It's pink. I say, So you're pregnant, so you dyed your hair black? She starts sobbing and wailing and she goes, I knew you wouldn't understand, you never understand anything about me! She bangs past me and stomps down the hall and slams the bedroom door behind her. I'm thinking, what's to understand? You're totally nuts! I'm standing there alone in the bathroom. The place looks like a tornado hit, there's little bottles and vials and tubes all over, with that little pink baby-positive stick lying right in the middle like the eye of the hurricane, the evil eye, more like, still and pink and sticking its tongue out at me. Ha. You lost. You fucked up. I'm thinking, what happened? I thought only fat girls didn't know what they were doing. My kid's a beauty, gorgeous, skinny, tall, why the hell didn't she stand up for herself? How could she let this happen? She's got no goddam spine! Then I'm back to the time when she was just two years old, the first time I saw her throw a tantrum. It was in the kitchen, over a purple popsicle. I was so surprised at the force inside her little body. She stamped her bare feet on the kitchen floor and balled up her fists and bared her tiny white teeth at me, and when I said, No, and shut the refrigerator door with the toe of my shoe she looked up into my face and squinted, she wasn't three feet tall, and her mouth got tiny like the...head of a nail, and I knew I had someone to contend with then. So I go into the bedroom, sit down on the edge of the bed and pat her on the back. Stacey, sweets, hey, hey, it's alright. You gotta be strong and make your own choice, but whatever decision you want to make, I'm behind you, okay? We'll do whatever you choose. She stops sniffing. She breathes in and out. I say, So, listen, uh.. .have you talked to the guy about this yet? And she says, nasty, No, Ma, God. Boys don't like girls who boss them around.

[A flashbulb pops and RENNIE is propelled into center.]

RENNIE: The first picture of me is at my first birthday party. In this one I am screaming with laughter and holding my hands up to show the camera that I am covered with chocolate cake. My face is smeared with it, it is all over the front of my pretty pink dress. Apparently I was quite verbally advanced, and my parents were showing me off when my uncle Jake said, Oh yeah? How smart is she? She's a genius, says my mother, she understands everything. Try it. She'll do anything you say. So... Rennie, says my uncle Jake, smush that chocolate cake all over your face, sweetheart. Will you do that for me? And I did it of course because I was just that smart and I ruined my dress and they took a picture of me humiliating myself when I was twelve months old. [Flashbulb pops.] This one is my mother's favorite. It's of her and me on one of our mother-daughter days, we're on the steps of the Met looking very close and what you don't see is Mother boring her knuckles into the small of my back saying Straighten up, sweetheart, it lengthens your neck. Now glow, come on, glow. We want this one to glow. For awhile there is an absence of photos - when tummies are no longer little-girl cute. Mother hides me at family gatherings and I seem always to end up behind pieces of furniture. So we have no extant record of the long years of wanting, of wanting and wanting and being denied. Reaching for bread and peanut butter and having Slimfast thrust into my tWelve-yearold fist. Mother says No, I am putting my foot down. She is putting her foot down, I see, and I see that to want and demand things is bad. And when I finally want nothing, nothing at all, when I finally want so little I can barely get up in the morning, my head feels like a ten ton brick on my shoulders, my knees buckle walking from class to class, when I want so little the gentlest sounds scrape my ears and my skin is sore and my hair falls out, finally my mother pulls me out from behind the chaise longue and says This is my daughter Rennie! This is my wonderful, beautiful daughter. Out comes the camera! [Flashbulb pops.] The pictures reappear. All the while Mother says Sweetheart, you're beautiful. You really do glow.

[Flashbulb pops.] In this one I am standing outside my own house, in a hideous dress I do not recall choosing, it is blue and it feels like a garbage bag next to my skin. I am wearing a floppy white orchid on my wrist and man, am I glowing. I am really fucking glowing. My smile is about this wide on my face though I don't know what I am smiling about because Andrew Marino has his hand on my back. We haven't even left the house yet, my mother is still snapping pictures and there he is, slinking his hand up my dress. Later we are in the dark and he is breathing so hard he is fogging the windshield and I say to him Andrew. No. No. And he says to me Rennie, you're beautiful. Please Rennie please, will you do it for me? I am saying, No, I am saying, Stop, but he does not hear me, I am not loud enough. I am so - weak. I am just...too...weak. [Flashbulb pops.]

In this one my mother is getting remarried. She is a vision in indigo organdy, she looks half her age, her husband's in real estate. But heavens, where's Rennie? Rennie's not in this one. Rennie is wearing an attractive off-white linen pants suit, but she is not in her place at her mother's side because she is in the parish hall kitchen, devouring the three-foot-tall wedding cake meant to serve one hundred and eighty guests. It was just so pristine, floating there, with no one to guard it, no one to witness...1 ate and I ate and I ate it all up until there wasn't one crumb left, not a single frosted rosette, and I held that whole cake inside my body, I had it all to myself. And then I threw it all up on the kitchen floor and I walked out the back door into the night.

[Lights shift, up on CEL in her corner. During the course of the monologue she moves up center and then progressively further downstage. ]

CEL: It starts with a girl maybe six maybe seven, looking down at herself seeing how - horrible she was! How gross like a monster. She didn't look anything like the other kids from 4-H, they were all skinny as rats from dragging goats through the mud and bending over fields in the blazing hot sun. In summer all kids' legs were scabby - but nobody had marks on them like I did, like Cel, Cel had some scars.

The first one came when I was six. I had split open my knee climbing through barbed wire and mama drove me to the hospital to get the thing stitched up with ugly dark thread, that's how deep it was. But I took those stitches out with scissors when I got home. I told my mama they came out in the bath but I could tell by the way she looked at me sidewise frying the eggs that she didn't believe it. All that summer I worked on my knee and by the time Labor Day rolled around my leg looked like it had been caught in a thresher, maybe.

After that she just seemed to find them, Cel, these cuts in her skin, these holes. They seemed to pop up without her even noticing. Some she put in there herself with the kitchen knives for killing the chickens or shears for the garden or the awl daddy used for punching holes in saddles.

Mama didn't know what to do with her girl. At first she didn't say anything, just folded her arms like so across her chest. What's happened to the backs of your feet she asked. You're picking those cuts of yours apart aren't you? What are you doing to yourself Celie? Why do you want to do such a thing toyourself? So she started buying extra boxes of bandaids and leaving them about the house in places she thought I might be likely to come across them. But I wanted to - take myself com-pletely apart. I had dreams of my body parts spread out in the yard for everyone even the neighbors to see. All the way through high school I did it at night when no one was looking. After my shower, when the skin was still soft. It was my thing to know. Then one day my husband found me on the floor of the bathroom, busted in without knocking...After that he kept watching me, keeping track where I went. I tried to lay still. I forgot things.. .left them to burn on the stove. My husband paced around and slammed the door on his way out. He accused me of letting the heat out in winter, letting animals in, stray cats and birds. So I needed a final solution. Get rid of all of the flesh at once. I was poking a roaster chicken full of cloves getting ready for Sunday dinner and I went to light the broiler with a hard wooden match. Then it came to me. My body - I wanted to light it on fire. Hear the fat sizzle into smoke. With all the fat gone I could dance - more than that, I could run and jump and fly maybe even, just me and my bones running naked through the meadows feeling the breeze. It seemed so obvious - why hadn't I thought of this before? I struck one of the matches, stroked it smooth across the rough edge of the box and I could feel the flame sparking and growing and swallowing the match head. I held it in front of my face. It flickered in my own breath. My thighs would go up first I thought then the rest of me would catch on quick. I lifted my leg and dropped the match onto my pants. For a moment-nothing, then - warm hot my leg started to jump - my skin was on fire. I screamed without meaning to Oh my God. I reeled around to face the counter my hands out in front of me reaching - desperate - something anything. Towel potholder glass of water.. . In my mind I heard Miss Moser from in front of the black board - stop, drop and roll, she said, if you ever catch fire just stop, drop and... Later I went to the phone to call 911, shivering, numb. I caught fire, I said calmly into the phone. I was cooking a chicken. It escaped.
```

---

## IC-0211: The Mother

- Title: The Mother
- Author (byline): Richard Exley
- Work: Witness the Passion
- Publisher: White Stone Books
- Publication date as stated: 2004
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2649
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
Mary the Mother of Jesus is undoubtedly the best known of all the eyewitnesses to His death and resurrection. No human being suffered more than she did. Watching the crucifixion of her Son was nearly more than she could bear. Yet even in His death she found hope. She took refuge in all that had been promised her that day so long ago when the angel told her that she had been chosen to be the virgin mother of the savior of the world. And her faith was rewarded for the son she watched die was raised from the dead on the third day! From the mind and soul of Mary, The Mother by Richard Exley.
```

### Performance text (classify this)

```text
OPENING THE SHUTTERS I STARE, WITH UNSEEING EYES, at the city shrouded in darkness below me. Morning is still a long way off, but I cannot bear to lie in bed a moment more. All night I've tossed and turned, tormented by thoughts of my son and what's to become of him. In my mind, I've replayed Simeon's fateful prophecy again and again.

Against my better judgment, I have allowed my sister Salome, I the mother of James and John, to persuade me to join her family in Jerusalem for the Passover. Secretly I hoped to see Jesus, though if the rumors I have heard are true, it would not be wise for him to risk making an appearance. Still, I hoped I might have a few minutes with him.

By the time I arrived, late Wednesday afternoon of Passover week, the city was wild with rumors. Jesus was reported to be here, but no one knows where. Mter entering the city in triumph on Sunday, he cleansed the temple on Monday, throwing out the money changers and driving out those who were selling. On Tuesday he dared to return to the temple to teach the people. And again early Wednesday he spoke, but then he disappeared-with good reason, for the chief priests are determined to put him to death. We heard nothing all day Thursday, which was yesterday. I hope and pray he has slipped away, but in my heart I know it is not to be. The sword of which Simeon spoke is already doing its deadly work. With great effort I force myself to think of more pleasant things. Like the night my first-born son came into the world.

Behind me I hear the soft rustle of cloth. Turning from the window I discover Salome has entered my room. Placing her candle on a ledge she makes her way to me. Taking both of my hands in hers she says, "I saw your light and thought you might like some company."

She is such a dear sister. Always available, but never prying. Giving her a wan smile I say, "I was just thinking of the night Jesus was born."

"Please tell me about it," she says, drawing me out with her kindness. "It's a long story," I warn her. She just smiles and says, "We have the rest of the night." Taking a deep breath I begin. "It wasn't a difficult birth as births go. Still, I didn't have anyone to help me except Joseph, and you know how helpless men can be at times like that. It's not the primitive stable or the bitter cold that I remember, or even my fear. All of that was forgotten as soon as I heard Jesus cry.

"There wasn't any water in the stable, so I used fresh straw to wipe him clean. Then I tore strips of cloth from a nearly new blanket and wrapped him in them. Joseph made a cradle of the manger, and we laid him there. I don't think I've ever been as happy as I was that night."

Salome gives my hand a squeeze and nods knowingly, having given birth to children of her own.

"Forty days later, after the time of our purification according to the law of Moses, we took Jesus to the temple to present him to the Lord. I wish we could have afforded a lamb, but all we could manage was two young pigeons. Still, I was so proud, especially when Simeon blessed him. He began to prophesy, and my blood ran cold. 'This child,' he said, 'is destined to cause the falling and rising of many in Israel.'

"Then came the words I've never been able to forget, Words that I've lived with all these years. Turning to me, he looked deep into my eyes and said, 'A sword will pierce your own soul too.'

"I asked Joseph what he thought Simeon meant, but he just shrugged it off. ‘The irrational ramblings of a senile old man' Was his conclusion. I knew better, and it wasn't long until my fearful premonitions proved correct.

"Jesus was barely two years old when King Herod ordered all the boys his age and under in Bethlehem and the surrounding area to be put to death. "When I learned of this evil decree, I was sick with fear. The nights were the worst. Sleep would not come, and when it did., I was tormented with terrifying dreams in which baby Jesus was torn from my arms and killed. More than once I awoke. screaming, bathed in a cold sweat, the taste of fear bitter in my mouth.

"Joseph did What he could, but I would not be comforted, not as long as Jesus was in danger. Thankfully, God intervened. The angel of the Lord appeared to Joseph in a dream. 'Get up,' he said. 'Take the child and his mother and escape to Egypt.' "Though we fled Bethlehem that very night, it was__________ before I felt safe, really safe. Even in Egypt, fear was a _____ every day. "As you might guess, I became something of an overprotective mother. I wouldn't let Jesus out of my sight. I h____ over him, treasuring every smile, every slobbery kiss, ________them in my heart against that terrible day when he would be taken from me. "It was to be many years before my fears were fully ______. There were even times when I could almost forget that prophecy, so ordinary did life seem. Jesus was good "" hands and seemed at home in the carpentry shop. Still, it could not last, and as the years went by I sensed a g restlessness in him. With increasing frequency I caught him staring off in the distance with a faraway look in his eye

"One evening, just weeks before he turned thirty returning from the well, where I had gone to draw water, I saw him emerge from his shop. Turning toward the v wearily stretched his arms wide, casting the shadow of ______on the wall behind him. In that instant Simeon's sword my heart afresh. I knew that Jesus was going to die, and the way he would die. Don't ask me how. Perhaps

"I remember the day he left Nazareth as clearly as if it were yesterday. He got work started in the shop, and then he came to me. He didn't say anything. What was there to say? For a long time he held me, and no mother was ever more loved. Then he was gone, without a backward look.

"For awhile we didn't hear anything. Then news began to filter back. John, our cousin Elizabeth's son, the one people called the Baptist, had declared that Jesus was 'the Lamb of God, who takes away the sin of the world!' "Sometime later a peddler brought news of Jesus' baptism. He witnessed it with his own eyes. According to his account he saw the Holy Spirit descend on Jesus in the form of a dove when Jesus emerged from the water. At the same time a voice from heaven said: 'You are my Son, whom I love; with you I am well pleased. '

"For several weeks we didn't hear anything more. Later we learned that Jesus had fasted and prayed for forty days while doing battle with the tempter in the wilderness. Then he returned to Nazareth, and never was a mother more proud. When he stood up in the synagogue to read on the Sabbath, I thought my heart would burst with joy. He read so well. His voice was so rich, so resonant. 'The Spirit of the Lord is on me,' he read. His voice brought the words of the ancient prophet to life.

"Finally he finished the passage and rolled up the scroll. Returning it to the attendant, he sat down. Every eye was upon him, and the room was tense with anticipation.

'Today,' he said, 'this scripture is fulfilled in your hearing.'

"That was too much. To the people's way of thinking, it bordered on blasphemy. Angrily they asked each other, 'Isn't this the carpenter? Isn't this Mary's son and the brother of James, Joseph, Jude, and Simon? Aren't his sisters here with us?"

"Seizing him, they dragged him out of the synagogue and to the brow of the hill on which the town was built. They had every intention of hurling him off the cliff to his death, but he walked right through the crowd and no man laid a hand on him. ' It was the most uncanny thing I've ever seen.

Still, my relief was short-lived. Seeing their anger, I knew it was only a matter of time until they killed him." Pressing my lips together, I close my eyes. A tear escapes from the corner of my eye leaving wet tracks down my cheek. Quickly I wipe it away and force myself to give Salome a brave smile. She returns my smile and her eyes tell me she understands. "That's the last time Jesus came home. From that day he lived in Capernaum. He lived there, I believe, to spare me. He knew how I suffered when people attacked him, especially the religious leaders.

"But we cannot escape our destiny, and the sword of which Simeon spoke is mine. It will only be a matter of time until it pierces my soul to the hilt."

We sit for sometime in silence, each of us immersed in our own thoughts. I sense that Salome would like to comfort me, but she is too wise to give me false assurances. And like me, she is aware of the grave danger Jesus is in. Together we watch as the sun rises, slowly washing the darkness from the city below. Suddenly our solitude is interrupted by a frantic pounding at the door. It is John, Salome's youngest son, and he brings the worst possible news. Jesus has been arrested and is being taken to Pilate, the Roman governor. Frantically we fling on our clothes and follow John through the winding streets toward the gover-nor's palace. By the time we arrive, a crowd has gathered and their mood is ugly. Working our way through the mass of people, we manage to position ourselves near the front. We are standing directly under the governor's balcony when he leads Jesus out. At the sight of him I nearly faint. "What have they done to him?" I cry, unable to tear my eyes from his mutilated face. His lips are a bloody pulp, one eye, is swollen completely shut, and his back is ripped to raw shreds-the work of a Roman whip. On his head, thrust far down, is a cruel crown of three-inch Judeaen thorns. A discarded robe of royal purple is carelessly thrown about his shoulders, making the mockery complete. Motioning for the crowd to be silent, Pilate says, "Here is your king." At that the mob goes mad. "Crucify him!" they scream, “Crucify him!” "Shall I crucify your king?" he asks. As with one voice they shout, "We have no king but Caesar."

Seeing he cannot prevail, Pilate yields to their will and orders Jesus put to death. We watch in stunned disbelief as the soldiers lead him away. Numbly we follow them up the Via Dolorosa, and out the city gates to a skull-shaped hill called Golgotha. There they crucify him. They strip him and nail him to a cross. As the executioner swings his heavy hammer, I turn away in revulsion, burying my face in John's chest while spasms of grief rack my tortured soul. John covers my head with his arms, but there is no way to shut out the madness. Shouted orders from the soldiers mingle with the tortured screams of the condemned, and are joined in the fearful din by the grief-stricken wails of family and friends. Worst of all are the taunts of the religious leaders. "He saved others," they sneer. "Let him save himself if he is the Christ of God, the Chosen One." Others mock him saying, "You who are going to destroy the temple and build it in three days, come down from the cross and save yourselfl...Let this Christ, this King of Israel, come down now from the cross, that we may see and believe." Such cruelty, such hatred, I have never seen. It is as if hell itself has erupted and is spewing its poisonous venom over the earth. Then, in the midst of that cesspool of hatred, I hear the sound of love! "Father," His voice is raspy, hardly recognizable at all. "Father, forgive them, for they do not know what they are doing." His words are no more than a ragged whisper, but there is no mistaking them. To my knowledge, no one but Jesus dares call God "Father." Like a magnet his voice draws me. Turning my face from John's chest I look full at my firstborn son. When I do, the sword of which Simeon spoke pierces my soul anew. My grief and sorrow are unbearable, yet there is something else too. A wordless hope, an inner conviction too intangible to be defined, yet too real to be denied. Somehow I know that he is not a helpless captive, but a willing sacrifice. In a way I cannot explain, I truly understand that his execution is not simply a miscarriage of human justice, but the just decree of a holy God. For this reason was he born. He is the Lamb of God, doing what he came to do, suffering for the sins of the world. Caiaphas, Pilate, the Roman soldiers, even the bloodthirsty mob, are not his executioners. They are mere instruments in the hand of God. This crucifixion is God's doing-a terrible but vital part of His eternal plan. Knowing this does not make my grief any less, but it does give me the strength to bear it. Now I want to encourage Jesus. I want to let him know I understand what he is doing, that I support him. Breaking away from John, I run to the foot of the cross where he can see me. Looking down, his gaze finds me, and for a moment we hold each other with our eyes. I feel John put his arm around me, but I cannot tear my eyes away from Jesus. "Dear woman," he says, and there is so much love, so much compassion in his words, I think my heart will break. How can he think of me at a time like this, I ask myself Then his eyes shift to John, and he says, "Here is your son." And to John he says, "Here is your mother." Something must have passed between them then, some unspoken message perhaps, because John takes my arm and leads me away. I don't want to go; I can't bear to leave Jesus to die alone. Yet I know I can't stay. Jesus wants me to go. He wants to spare me the pain of watching him die, and I cannot deny him this final act of kindness. The sky is growing dark as I descend from Golgotha and turn toward Jerusalem. John lets me lean on him as he leads me toward the home of my sister. A good thing too, for I am nearly blind with grief. Now that Simeon's sword has finally been revealed I find it is much worse than I could ever have imagined. Still, I draw some small comfort from the knowledge that this is part of God's eternal plan. Turning to John I say, "In birth, Jesus became my son and I his mother. In death, he becomes my savior and, unworthy sinner though I am, I can now become a child of God. Through him I too can call God 'Father.'"
```

---

## IC-0212: Mr. Burp

- Title: Mr. Burp
- Author (byline): Cora Sorenson
- Work: Fast Horse Plays – Round 1, Pgs 1-8
- Publisher: Fast Horse Drama
- Publication date as stated: Sept 2011
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: STELLA
- Teaser before the introduction: Yes
- Spoken words (computed): 1668
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cora Sorenson
Book: Fast Horse Plays – Round 1, Pgs 1-8
ISBN: 978-0615603681
Publisher: Fast Horse Drama
Date (Month/Year): Sept 2011
```

### Introduction (context only: never use it for content warnings)

```text
9-year-old Stella had always been precocious, smart and fearless. But everything changed the day she was diagnosed with leukemia. Gone were perfect spelling tests, math homework and her arch-nemesis Janine Martin. Her new world was filled with doctor’s appointments, whispers, worried looks and fear. But in the midst of it all, something extraordinary happened. From the depths of her imagination came Mr. Burp, a frightened monster who lived under her bed and was not afraid to cry. No one else could see him, but Mr. Burp arrived to help her face the darkness and remind her that even in the hardest times, wonder never truly disappears.

Mr. Burp by Cora Sorenson
```

### Performance text (classify this)

```text
Stella is a verbal and bright 9-year-old. She often speaks quickly, almost to the point of stumbling over her own words.

STELLA: Gram always said, "He's just as cute as a button," and I always thought that was a really weird thing to say because I've never seen a button that was as cute as he was, but it's just a saying and sometimes sayings don't really make very much sense. Sorry.

Sometimes I talk fast when I have a lot to say. Mom says it's because my mind is going fast and my mouth is trying to catch up with it. Which I think is just a nice way of saying I should talk slower. But he was a really neat lizard. His name was George Washington and he was about this big and bright green with little yellow polka-dots.

STELLA: I came home from school one day and he was just lying there and not moving at all. He was dead. And I was really sad, but more than anything else, I wanted to know if GW was going to Heaven. And then Gram explained to me that when animals . . . die they go to a place called the Rainbow Bridge and they just play and have fun and wait for their people-owners to go with them to Heaven. It sounded really nice. So, I would pray at night and ask God, nicely, if he could just let GW go on to Heaven. I didn't think he should have to wait for me.

And that was when I started having the Really Bad Dreams. I would wake up really late at night and know that I'd just had one of them, but I couldn't remember what it was about. I knew that part of my brain knew it, but I couldn't find that part at all. Just things about being cold or a darkness so big it could swallow you up. That doesn't make any sense. It sounds like something a little kid would say, and I'm not a little kid anymore. In my dream I'd be super scared, trying to catch my breath, and I'd pinch myself and say, "Now you listen, Stella, you wake up right now!" and then I would. I'd wake up and I would go sit in the kitchen with all of the lights on until Mom or Dad would tell me I should go back to bed.

So, I was having one of these Really Bad Dreams with the big dark and the huge cold and, in my dream, I heard something coming from under my bed. In dreams, you always do the thing you should never ever do; so of course, I get down on the floor and I'm looking under the bed . . . and I’m trying to wake myself up, pinching myself, really, really hard. (pinches herself, then reacts) Holy Crud! I am awake. This isn't part of the Really Bad Dream anymore; this is a Really Bad Being Awake. My arm hurts cuz I pinched it so hard and under my bed, there's a monster.

I run as fast as I can downstairs to the kitchen and turn all of the lights on. Mom finds me there in the morning and says that maybe my bad dreams are getting worse. I do not say one word about the monster under my bed. I already have a nightmare problem, and I am not going to be the kid with the Overactive Imagination too. Or like Gram says, "Four quarters short of a dollar and headed upstream with no paddles!" I decided I was not going to think about him anymore, and anyway, he had probably gone away to hide under some other kid's bed and scare them. Like Janine Martin, because she's mean. That was on Friday, because . . . (suddenly sad) I had a doctor's appointment.

But [the monster] was still there that night and I slept in the kitchen. Mom said I needed to sleep in bed. He was there on Saturday, and I slept in the bathroom. Dad said I needed to sleep in bed. He was there on Sunday too, and I slept in my closet, where there were no monsters. I told Mom and Dad about him on Monday. They told me I had an overactive imagination and then Dad looked under the bed with a flashlight, but the monster was hiding and Dad didn't see him. And then Mom sang me to sleep, which is usually only for little kids, but I made an exception, what with the whole “I'm living with a monster under my bed” situation. (hums a little of Home on the Range)

So, I thought maybe the monster had gone away to scare Janine until I woke up in the middle of the night because this is a Very Big "Holy Crud" -- the monster was crying -- Lots of tears and snuffling crying. This was getting ridiculous! (rolls her eyes) It's hard to be afraid of a monster who's crying! I told him if he was trying to scare me, he was doing a really bad job. But he just kept crying. I was really tired and I had a math test the next day, so I did the one thing a kid should never do: tell him he might as well just sleep in bed with me. As long as he stopped crying and didn't snore. Like Gram says, "If you can't beat ‘em, join ‘em."

He was there every night. And he didn't snore at all, but he did burp sometimes. He was just a really good friend. He didn't make fun of me because I had the special classes at school for the advanced kids. He just listened . . . sometimes kids, even smart kids or strong kids, just need a friend.

I slipped up a couple of times. I did. Talked about Mr. Burp when I was eating my Captain Crunch or when Dad was helping me with my homework. And Mom and Dad would just smile and laugh. I wanted to explain that Mr. Burp wasn't like the Easter Bunny who lays chicken eggs or a fat man who breaks into your house at Christmas. He was just my friend . . . I'm not sure if he was something they could understand.

So, it wasn't very long ago, I was getting ready for bed -- and I got down tell Mr. Burp he could come to bed and um, he wasn't there. He wasn't there at all. I looked all over my room, in my closet, in my dresser, in my cupboards. And I wasn't going to say this, but I started crying because I couldn't find him. Mr. Burp told me that no matter what, he was going to stay with me. And I believed him! No matter how tough things were or how bad I was hurting or how much I just wanted to be a 9-year-old kid who was happy all the time, he would be there for me. (long pause, softly) He would be there even though I was sick.

(yelling loudly) "Mr. Burp! Mr. Burp! I won't complain anymore. I promise. Please come back!" And I guess I yelled so loud that I woke my Mom and Dad and they came running out of their room. (crying) “I can't find Mr. Burp. I think he went away.”

And you know what? My Mom started crying, and held me like I was a little baby. And she just kept saying, "I love you" and I kept saying, "I know, but I need to find Mr. Burp. If he's gone to the Rainbow Bridge already, is he going to wait for me? Am I going to the Rainbow Bridge too?" And you know what? She said he would wait for me. She told me that maybe I could make a stop at the Rainbow Bridge on my way to the other place I was going. A place with a lot of light and big pink clouds and . . . no pain. And I told her I was so scared. Scared for Mr. Burp . . . and for me. I didn't want Mr. Burp to be alone. And she told me that nobody was ever really alone. Ever. I just wish things were different sometimes. (hums a bit of Home on the Range, holding back tears; she furiously wipes her eyes)

Sorry. I promised Mr. Burp that I wouldn't get weepy. I'm not a little kid anymore. I did like going to school, though. It's hard to go to school when you're just so tired and when you have to go to so many doctor's appointments. My doctor is a really nice lady, but I don't think she's used to younger kids asking so many questions. Like when she delivered the Really Bad News to my parents and not to me. But I wanted to know what it was called. Acute Lymphoblastic Leukemia. That's a name for a really bad monster. Like the kind that probably live in closets. But it's actually the name for a Really Bad Cancer -- a cancer that kids don't get better from. I told Mom that I wasn't scared, but I was actually lying a little bit.

Mr. Burp told me it was really important for me to be strong for Mom and Dad and Gram. Gram was here yesterday and I told her that Mr. Burp had come back. That he was here with me and that he just had to go away for a little while to get things ready. And she wasn't surprised at all.

(changing the subject) Mom told me that I'm going to have a little brother. And I told her that I'm going to be watching him from Heaven and that I'll be waiting for him. And Mom said, "I know, sweetheart. I know." The cool thing is, Mr. Burp's gonna visit him too. (peeks under her bed, then whispers)

I need you to be really quiet, because Mr. Burp is sleeping right now. He told me a secret. He told me that because he's magic, he can go wherever he wants, anytime. Not like people. And so, he's going to go with me and I don't have to be afraid. (takes a deep breath and put on her brave face) I'm not. I'm just really, really tired.
```

---

## IC-0213: Mr. Marmalade

- Title: Mr. Marmalade
- Author (byline): Noah Haidle
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: January 2006
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MR. MARMALADE, LUCY, SOOKIE, EMILY, GEORGE, LARRY
- Teaser before the introduction: Yes
- Spoken words (computed): 1152
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
Lynda Barry, an American cartoonist, author and teacher once said: “We don’t create a fantasy world to escape reality, we create it to be able to stay . . . and to understand what otherwise would be intolerable.” Lucy is a young girl with a very active imagination. Her best friend is Mr. Marmalade. Who really doesn’t have too much time for her. Together they create an imaginary world that often echoes too closely the reality that Lucy is struggling to comprehend. As this selection opens, Lucy’s mom has left yet again for an evening on the town and Lucy is left in the care of Emily, the babysitter.

Mr. Marmalade by Noah Haidle
```

### Performance text (classify this)

```text
A living room in New Jersey. Lucy is playing with Ken and Barbie when Mr. Marmalade appears. He’s very well dressed. Suit, briefcase, nice shoes. Lucy hums as she plays with her dolls. (Music is a way for Lucy to cope with being alone most of the time) Suggested song: Pure Imagination from Willy Wonka & the Chocolate Factory – See link at the end of this selection for video of this song.

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

LUCY: Mr. Marmalade just got home from the office and he has to leave in like five minutes so I’d greatly appreciate it if you left us alone, [MOM]!

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

LUCY: That’s very serious. You need a heart transplant. Let’s get you that new heart! (Lucy pantomimes an elaborate heart transplant procedure – kid style based on what she’s obviously seen on television shows, complete with sound effects) How’s that new heart?

LARRY: I don’t have the chest pains anymore.

LUCY: You’ve made a complete recovery! (Pg 16) (Larry walks around the room) Hey!

LARRY: This place is pretty nice. So you live here with your parents and everything?

LUCY: It’s just me and my mom. My dad, he divorced my mom when I was two, or something. ***** Flashback in the world of pretend – a baby cries in the kitchen.***** In this flashback, Lucy plays her MOM and Mr. Marmalade plays her DAD

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

LUCY: Yeah. See you at school. ******Scene Change *****

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

MR. MARMALADE: Suit yourself. (takes another drink) You sure? This is some good *stuff*. Hey, let’s play House. “Hey honey, I’m home!

LUCY: (softly) No.

MR. MARMALADE: That’s when you say, “How was work?” And I say, “It sucked.” But somebody’s gotta provide for this family. (Silence . . . Lucy is near tears) [What?] You don’t want to play House with me?

LUCY: Not like this. Not when you’re [drunk].

MR. MARMALADE: (brandishing his flask) This is like a cup of coffee. I don’t even feel it. Hey, Lucy, I work twenty hours a day. (getting angry and reaching for Lucy) I want to play House!

LUCY: (avoiding Mr. Marmalade) I won’t play House with you.

MR. MARMALADE: (grabbing for her arm again) Then let’s play Doctor. Come here!

LUCY: Get out!

MR. MARMALADE: (calming down) Okay, okay. I’ll see you on Sunday.

LUCY: No you won’t.

MR. MARMALADE: What?

LUCY: I don’t want to see you anymore.

MR. MARMALADE: What? What the *hell” you talking about?

LUCY: I don’t want to play House with you anymore. Or Doctor.

MR. MARMALADE: (angry, yelling) What the *hell” you talking about?

LUCY: (also yelling to be heard) I don’t want to play with you at all. (long silence) You’re a bad person. (growing in intensity with each sentence) You neglect me. I deserve a lot better than you, [Dad!] (long silence – Mr. Marmalade exits) (Actor re-enters scene as Larry)

LARRY: (Pg 29) (Sees that Lucy is upset) Are you okay? (Looks offstage) Who was that guy?

LUCY: He used to be my friend. His name’s Mr. Marmalade.

LARRY: That guy was your friend?

LUCY: People change. He used to be a good guy.

LARRY: Well, he’s not anymore.

LUCY: Larry? . . . . Do you know how to play House?
```

---

## IC-0214: Babe

- Title: Babe
- Author (byline): Steve DuBois
- Work: Babe
- Publisher: Mushroom Cloud Press
- Publication date as stated: August 15, 2024
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: HELEN
- Teaser before the introduction: No
- Spoken words (computed): 1212
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
[1928. A seedy living room in a row house in Watertown, Massachusetts. HELEN WOODRUFF RUTH lives here. She is fine-featured, thirty-one years old, but looks significantly older. Her figure is willowy, her auburn hair shot with grey. Within a month, she will be dead in a house fire, the circumstances of which will never be fully explained or adequately investigated. One month after that, her former husband will re-marry.]

HELEN: Welcome to my home. Well, not my home, technically…but never mind that, for now. It’s not the house you’re here about. It’s about…him, of course. George. My husband.

I might be the last person in America who still calls him “George”. Do you know how he got that nickname of his? It was because he could never remember anyone’s name. Not even his teammates. No, with George, it was always, “Hey, babe, ya see what I did ta that pitch?” Or, “Hey, babe, we goin’ out on the town tonight?” Everyone was “babe” to him. And so, eventually, he was “Babe” to everyone. George Herman ”Babe” Ruth.

[A long pause.]

I was sixteen years old, on my own, new to Boston and without a clue as to how to live there. And I’m waitressing at Landers’ Coffee Shop, and one morning, there he is. This solitary figure, bulldog face and shoulders like a plough horse, demolishing his third stack of pancakes, and demanding more, in a voice as loud and insistent as Gabriel’s trumpet. And as I hustle them over to him, he looks up, and our eyes meet.

You should understand, he looked very, very different then. I mean, how was it that that ballplayer described George the other day? “A beer keg on stilts?” Accurate enough. Lord knows he’s got enough alcohol in him. But back then, nineteen-year-old George…he was this lean, athletic demigod. I mean, he used to steal bases, can you believe it? That was how the World Series ended, one year…he was standing on first base, in the ninth inning. And he looked down the line to second and saw something he wanted. And he went for it, and they threw him out by ten feet. And he destroyed everything that the people around him had been working for. But George wanted that base. And what George wanted, George went after.

And that day, at Landers’ Coffee Shop, what he wanted was me. Oh, God, how to describe it? He wasn’t yet the most famous man in America, but even then, he just…he had this gravity, you know? Like, to be around him was to be sucked into his orbit. When he was in the room, everything else faded into the background. You couldn’t look at anything but him. And it was me he wanted. Me! And…do you see, everyone else was “babe”, but I was Helen. My name was worth knowing!

It was madness. We were children. We courted for a grand total of three months. And we hadn’t been married a year before the whole world discovered him.

Now. I’d showed George what it was to be intimate with a woman. And here’s what you must understand about George: when George decides he loves a thing, he can’t set it aside. If it’s in front of him, he will take it, and devour it, like those pancakes. And he’ll demand seconds. Thirds. Fourths.

And then we went to New York. And George and New York…matches and gasoline.

[A long pause]

We’d wanted a family. And twice, we managed to get me…but I…I lost them, you see. And George didn’t blame me, exactly. But he was heartbroken.

And then one day, he comes to me, and he can’t meet my eye. Helen, he says, I screwed up. But it can work out for us. We can make it a good thing.

Her name was Juanita. The woman, I mean. The newborn baby girl we adopted from her, the one we told the press I’d given birth to, we named Dorothy. Even then, she had his features. She’s six now, and she looks more like him every day. [pause] Poor thing.

And being a father, you’d think it would change a man. With George, it just turned up the volume. He became…himself, only more so. His lust for life…his lust for everything. He had the total adoration of two women now. So why stop there?

And that…that, you see…was the hell of it. The pure undiluted hell of it. That I never, ever stopped feeling about him the way I did that morning in Landers’ coffee shop. And I sat home, caring for our…caring for his daughter. Reading about his…exploits. And all that time, I was praying, praying to Jesus, that I’d somehow be enough for him again! That he would stop seeing the women in front of him and recognize the woman behind him! That he could for one goddamn instant stop falling in love with every goddamn thing he saw!

And then…I came down with this…condition. And it turned out I’d picked it up from him, and he’d picked it up from…some chorus girl, I suppose. And I spent close to a month in St. Vincents, having the symptoms treated. And after I’m discharged, George comes to me. And he tells me, look. It’s been great, between us. But it’s not working out. We need some time apart.

And I ask him, what’s her name.

And he stares at the floor. And he tells me, “Her name’s Claire, babe.”

Claire’s no sixteen-year-old. Very much a woman grown. A sophisticated woman, who can put his affair–all his affairs–in order. George wanted to divorce me and marry her. So I set my terms: I wanted one hundred thousand dollars to take care of Dorothy and myself. And do you know what? I finally discovered something Babe Ruth didn’t love.

It’s all gone now. I think I mentioned, this home…it’s not mine. He’s been generous. He’s given me a place to stay. He’s even let me borrow his name. I’m going by Helen Kinder at the moment. It’s for the best. Helen Ruth…that’s not a name anyone wants to hear these days. My home, my prospects…even my name. Gone. Disappeared over the fence like some pitcher’s feeble fastball.

But I’ve still got that…condition. That’s George’s enduring gift to me, the final sign of his love.

[A long pause]

I told you about George’s…gravity. The way he has. How we all end up in his orbit. When you’re with him for long enough, I suppose, you end up becoming him.

I drink now, for one thing. Not as much as George, but who could? And…well…here I am, in this house, right? A married woman, shacking up with a man who isn’t my husband. What if the papers found out? Imagine the scandal.

And there’s this, too. Remember what I told you about how George could never be bothered to learn anyone’s name? It occurs to me…after all this time we’ve spent here chatting…I never did bother to ask for yours.

Thanks for listening…babe.
```

---

## IC-0215: My Brother’s Funerals (from The Redhead and the Slaughter King)

- Title: My Brother’s Funerals (from The Redhead and the Slaughter King)
- Author (byline): Megan Falley
- Work: The Redhead and the Slaughter King
- Publisher: Write Bloody Publishing
- Publication date as stated: Oct 2014
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1215
- Already set (do not supply): none

### Source block (context only)

```text
Author: Megan Falley
Book: The Redhead and the Slaughter King
ISBN: 978-1938912450
Publisher: Write Bloody Publishing
Date (Month/Year): Oct 2014
```

### Introduction (context only: never use it for content warnings)

```text
It has taken me a long, long time to come to the realization that when the person you love becomes an addict, they are no longer the person you love. You can spend your nights trying to understand addiction, and how somebody can transform into a person so horrific right before your own eyes, but there is no understanding it.

My Brother’s Funeral by Megan Falley
```

### Performance text (classify this)

```text
An Apology To My Brother

I'm sorry I spill your secrets / like an overfull goblet of wine.
I'm sorry I think they're mine mine mine.
I'm sorry that I love you / the way a shadow loves its body-
that I always sniff your hair.
I'm sorry that in the poems I name you Needle. / In the poems I name you Pill.
I'm sorry it's always recovering, never recovered.
That I'm still nervous when you call.
That I think it's for bail.
I'm sorry that when you say I love you, I wait for the but,
I'm sorry I always write about you as if you are dead.
It's just-
I spent so many years preparing for that funeral.
All my dresses are black.

Golden Boy My brother's hair looked like someone cooked a porridge comprised entirely of sunshine and poured the bowl over his head. It was a yellow traffic light that everyone slowed down for.

They complimented my mother, told her she was lucky. He was a dandelion of a boy . . . but when we picked him up after his first day of High School- he demanded we take him to the barbershop. This memory comes before heroin became a household name. Before I found my piggybank slaughtered -- my brother's mouth filled with more pills than teeth. He slammed the door as he stormed into the $7 barber. Alone, he growled. I was six years old and did not know what this meant, but I saw my mother's eyes in the rearview mirror -- she knew what happened when dandelion boys asked for the lawnmower. He returned to the passenger side years older than he was when he left it, switched the channel on the radio to something harder, faster, twisted the volume knob up to drown the words no one was speaking. Back in the barbershop, someone swept up that gold-spun miracle and threw it away. My mother knew a war was going to come, the way animals know before rain. The way they know, but can do nothing to stop it. TRANSITION And so I began to prepare, to plan his funeral. I wrote eulogy after eulogy, trying to find a way to deal with the ultimate oblivion of my brother’s death.

The First Ceremony
If I was the family florist, I'd be responsible for the apology of lilies.
If I was the lawyer, I'd be expected to pay for it all -- the party of black.
If I was the chef, they'd ask me to feed those who cannot imagine eating.
But I am the writer -- not the star of the funeral, but its narrator -- here to translate the
language of grief into simple, digestible metaphor.
To wield euphemisms.
Turn addiction into grip on reality.
Turn overdose into sudden, unfair.

My mother can melt like a satin witch into her corner of the pew, my father can do what men do: prove his strength, become a pallbearer. But I'm the emcee at my brother's last big party -- so I recite his eulogy to shampoo bottles, haven't sung in the shower for years. My brother bangs on the bathroom door, says, Hurry up - [what’s] taking so long? I do hurry up. I want him to love me. There's still dirt on my skin, though. There's still soap in my hair. TRANSITION

Or maybe Sean’s funeral will be like this . . .

The Second Ceremony
We bury him with his baseball cards because that's what he has left, what his life
amounted to.
The electronics sold. The house turned to soot at the whim of one cigarette.
Even the girls figured him out.
We bury him with his friends outside the funeral home, too scared to enter, sweating like
burned spoons.
We replace his face in its forever bed with each of theirs, their pockmarked arms and
rotted smiles.
We bargain with the god of too late.
We bury him in his father's suit, which was too big for him before and ridiculous now,
but nobody buys a new suit for the dead.
We leave him to lie in his potential.
I bury him with a picture of me. Don't bother to tape the jagged, toothy edge back
together. He ripped himself out on purpose -- and look how I'm smiling in the photo.
Look how I'm leaning on nothing.
TRANSITION

The images get bleaker and bleaker as Sean’s addiction worsens . . .

The Third Ceremony I am the only one at your funeral. I fill the vase with the right flowers and press my face into them, but only smell your cigarettes. I recite the obituary that I've been saving for this occasion ever since the summer you started putting fireflies on your tongue and winning contests for cruelest hands. I admit, it's a flawless performance, gifted to an empty room, but I can't help but hate you for not cracking an embalmed smirk during the funny parts. I carry your casket alone which is also an exercise I've been training for. The hearse is the only one waiting for me to finish. There will be no procession, no cars following behind. You've left no shadow. Pawned all the people who could have been here for highs even you knew weren't worth it. I am relieved -- the worst is over. I received the phone call, confirmed your body. I open a black umbrella, blame you for the rain. TRANSITION And then there’s a ray of hope . . . Rehab seems to be working and images of Sean’s funeral shift again to the way it should be . . . the way I hope it will be. My mind whispers “Please, Sean . . . let rehab work this time.”

The Last Ceremony
The widest church in town is still too small to fit everyone who has loved you through its
heavy doors, so we hold two funerals.
No one wears black.
We wear your sports jerseys from high school. We wear the t-shirts you collected
from the marathons you ran to raise awareness for addiction.
Your grandchildren wear the sheets from the forts you built with them, cut into capes.

Your wife does not cry, she feels lucky to have loved you.
You live on in every wrinkle.
You gave her those smile lines she wears like jewelry.
The men from the meetings tell stories about you saving them, yanking them from their
own syringes and vomit, they name their kids after you.
There are so many boys named Sean,
Sean.
I wish our father was here to see this, but maybe he's waiting up there with a catcher's
mitt, maybe there's a baseball whizzing through the air for you.
I know you'll catch it.
In the casket, you are older than rain, just as exquisite.
There is not a shadow of pain on your face.
You learned the science of turning it to joy.
I remember the day, decades ago, when you told me I was your best friend.
I could have died right then, but we were given the gift of years, and dinners, and holidays,
and children, and forgiveness which is sweeter than any liquor.
This is the first of your funerals where no one asks me to make the speech.
I just sit in the front row and weep, and am not sad.
I am the least sad I have ever been.
```

---

## IC-0216: My Mother with Her Hands as Knives

- Title: My Mother with Her Hands as Knives
- Author (byline): Dave Eggers
- Work: A Memory, A Monologue, A Rant and a Prayer
- Publisher: Random House Publishing Group
- Publication date as stated: May 2007
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: WOMAN
- Teaser before the introduction: No
- Spoken words (computed): 1666
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Eggers
Book: A Memory, A Monologue, A Rant and a Prayer
ISBN: 978-0345497918
Publisher: Random House Publishing Group
Date (Month/Year): May 2007
```

### Introduction (context only: never use it for content warnings)

```text
In researching WHAT IS THE WHAT, Dave Eggers book about the life of Valentino Achak Deng, one of the Lost Boys of Sudan, Mr. Eggers traveled with Valentino back to his hometown of Marial Bai, in 2003. There they located his family, whom Valentino had not seen in seventeen years. While in Sudan, Mr. Eggers interviewed many women who as young girls had been abducted by militiamen—the same militias who now plague Darfur—and who had been forced to act as servants and concubines in the households of military officers in the north of Sudan. This selection is an account from a young woman shortly after she was freed. My Mother with her Hands as Knives by Dave Eggers.
```

### Performance text (classify this)

```text
WOMAN: I was born in Wunrok, in southern Sudan. When my mother was young she was blessed by great fertility. She gave birth to twenty babies, and I was the sixteenth. Most are gone now. Our father was a successful farmer. He kept 180 head of cattle and raised groundnuts, sorghum, maize, okra, and sesame. There was plenty to feed us, and he traded the rest for luxuries like mattresses and dresses. When I was very small I had a doll made in China. You know how rare something like that is, Valentino.

In 1983 the war was on and the militias, the murahaleen, came. I was one or two years old, so I remember none of this. The Arabs killed twenty men, including my uncle, my father’s brother. They took most of my father’s cattle and kidnapped three of my siblings—two brothers, five and seven, and one sister, who was eight. I don’t really remember them, just as you said you do not remember your older siblings, Valentino.

There were four of us left, all under five except my brother Jok, who had escaped the murahaleen by hiding in the river. He had used a pole to breathe. I don’t know where he learned to do that. When he got home from the river, my mother sent him with the walking boys, like you. She wanted him to be safe and to study in Ethiopia.

Our family moved to Panthou, where there was no SPLA. My father thought we’d be safer there; for a time we were, and my mother was blessed with more children. In 1986, the murahaleen came again, this time taking my two eldest sisters. They killed another uncle, my mother’s brother, as he tried to defend the family. He threw a spear at one of the Arabs, and the Arabs cut off each of his limbs one by one, and then threw him on a fire. Everyone in the village could hear him screaming. They threw his limbs down the well, poisoning all the water for the village.

My sisters were gone and my father was furious. My father then did something unusual. He followed the murahaleen. He took his spear and all the money we had and he went north, because he knew that very often the murahaleen didn’t travel fast, because they liked to make the Dinka slaves walk.

My father spent a year in the North. He went as far as Khartoum, looking on the streets and in the peace camps for my sisters. He returned a year later, and when he did, he seemed defeated. It appeared that he had aged ten years in one. He spoke to no one. He wouldn’t eat. He had been a prominent man and now he was so skinny he looked like a boy, in his body, though his face was so very old. He died two weeks after coming home.

After my father died, there were five of us left, all girls. My mother used to lament having so many girls. We couldn’t defend ourselves. Panthou was raided four more times as we lived there. We worked the farm with help from boys in the town who had been orphaned. Then the Nuer raided. It was very strange, because we didn’t know to fear them. But they arrived one day and they raped many of the women and took all they could carry. I hid in a hole under a tree.

In 1988 the murahaleen came again. They came straight to our home, three men on horses. They wore white and approached our mother silently. We were hidden among the livestock and they entered the hut as if they knew where we were. This is how they took my sisters and me. Five of us. They told my mother that they had been told by Bashir that all Dinka girls were to be impregnated with Muslim babies and they were doing their duty. My mother asked them if they intended to rape us there and then. The man said that no, we would be impregnated on a proper bed, and that the babies would be brought up with the civilization only Islam could provide. They tied our hands and tied us to one another and we waited in a cattle pen until the next morning, when they were to take us north. My mother came to us that night as we waited with eleven other girls. “I will come to get you girls. Just be patient. I will see you soon and bring you home.”

In the morning we were walked out of the village on the main road. Most of the men had ridden ahead and we were guarded by five young men on horseback. They poked us with their swords when we walked too slowly. When we stopped to rest and for water, they insisted that we show them our genitals. They told us that we would soon be freed of the sinful parts of our genitals that made all of the Dinka licentious. Otherwise they didn’t touch us, and every hour they did not touch us I thanked God.

After four days we stopped at an Arab town, and we were brought into a building that was cool and dark. It was a school. There were desks and chalkboards. We were seated on the floor and left there for half a day. We heard the activity of the town; everything seemed very normal. Sometimes an Arab boy would peek through a window at us and hold his fist up to us or spit on the window.

Men were brought into the school, escorted by one of the young Arabs who had kidnapped us. The men would confer, and twice they left with one of the girls. We didn’t see them pay the kidnappers. But soon there were only fourteen of us. My sisters and I stayed close and argued over the best strategy. We had been told that the Arabs liked to split families, for fear that siblings would conspire against them, so we worried that they would see us together and guess we were related. In the end we split into two pairs.

At the end of the day there were no more visitors. We did not eat that day. We slept there, on the floor, with our heads rested on one another’s thighs and stomachs. In the morning we were made to walk again. There were thirteen of us now. I don’t know what happened to the youngest girl. She was taken as we slept I guess.

We walked for four hours that morning, tied together in a line, following the Arabs on their horses. It was very hot that day, and one girl was very sick, very weak. She could not walk, so she was thrown onto one of the horses and we continued. Late in the day, the Arabs began to trot their horses, to make us go faster. I think they needed to reach a certain town by nightfall, so the pace was now faster. After some time at this pace, when the day was very hot and we were feeling faint, I heard a voice. The voice said “Stop.” The voice was very distant. I turned and saw a figure running to us. It was a Dinka woman, we could tell; her face was uncovered. “Stop!” the woman said again and again, as she ran to us. The Arabs stopped and everyone turned around. The Dinka woman came closer. She ran like my mother ran, with her hands very straight like knives. She ran closer and it was her. The woman was my mother. She had been following our trail. Our stay in that trading town had allowed her to catch up. She yelled at the men. “Give me these girls!” She pointed to us and she wept. “You have taken four others. Four of my children are gone. My husband died looking for them.” The Arabs sat on their horses and said nothing. They were very young, these men. They looked at one another, and then one of them turned. Then they all turned and started their horses again. We walked again, too.

She was not finished. She walked with us. She began to walk next to my sisters and me. She said nothing; she only walked while holding our hands, becoming part of our group. She walked for an hour before the men realized she was still with us. One of them turned and saw her. Then they all began to talk loudly to one another and then to her. My mother spoke some Arabic and she told them that she would continue to walk wherever we went. She held on to the rope that bound us all and said that she was part of the rope now. She said she would walk as we walked, and would always be with us, unless they killed her.

One of the men went for his sword but he was restrained. One man, who looked like the youngest, got off his horse and cut the rope. We were the last five on the rope. He cut it and kicked my mother in the stomach. He got on his horse and spit in our direction and then the group walked on without us. They were finished with us. “Fuck them!” they all said and rode off.

We ran in the other direction. My mother led us, running with her knife hands. We got off the road and ran through the grass and we slept in holes as we traveled back to the South. We ran for two more days until we saw our village again. The day we returned, it rained heavier than I have seen in many years and this was God crying with joy. He cried and cried for us, for a full day he cried while my mother danced and sang and ran around the village like she was possessed.
```

---

## IC-0217: My Name is Rachel Corrie

- Title: My Name is Rachel Corrie
- Author (byline): Not specified
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: April 2008
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: RACHEL, REPORTER
- Teaser before the introduction: Yes
- Spoken words (computed): 1095
- Already set (do not supply): none

### Source block (context only)

```text
Author: Edited by Alan Rickman and Katharine Viner
ISBN: 978-0822222224
Publisher: Dramatists Play Service
Date (Month/Year): April 2008
```

### Introduction (context only: never use it for content warnings)

```text
In 2003, American Rachel Corrie arrived in Gaza with a small contingent of international peace activists committed to protect the homes of Palestinian families from demolition. Corrie believed that her western features and blonde hair would deter the bulldozer, but she was wrong.

Today, nearly 20 years later, the violence in Gaza continues. It is often presented as a conflict between two equal sides with irreconcilable claims to one piece of land. In reality, this is a conflict between Israel, with one of the world’s most powerful and well-funded militaries and an indigenous population of Palestinians that has been occupied, displaced and exiled for decades.

This is the first-hand account of events occurring during 2003 culled from Rachel Corrie’s diary and edited by Alan Rickman and Katharine Viner . . . My Name is Rachel Corrie

January 25, 2003 (Arriving for training)
```

### Performance text (classify this)

```text
Edited by Alan Rickman and Katharine Viner

(Taken from the Writings of Rachel Corrie)

RACHEL: (Pg 18) We are all born and someday we’ll all die. Most likely to some degree alone. What if our aloneness isn’t a tragedy? What if our aloneness is what allows us to speak the truth without being afraid? What if our aloneness is what allows us to experience the world as a dynamic presence – as a changeable, interactive thing? If I lived in Bosnia or Rwanda, needless death wouldn’t be a distant symbol to me, it wouldn’t be a metaphor, it would be a reality. I have no right to this metaphor. But I use it to console myself. To give a fraction of meaning to something enormous and needless.

RACHEL: Very little problem at the airport. The woman behind the glass appeared not to notice my shaking hands. (Pg 19) The training . . . there was noise and flashing lights outside – but it wasn’t real for me somehow because I was inside this building with these people. Everyone extending theories into the air.

Notes from Training: When talking – no hearsay. Don’t appear to judge rightness or wrongness. Non-Violence – Don’t touch those we’re confronting. Don’t run. Carry nothing that could be used as a weapon. (Pg 24) We’ve been wavering between five and six of us internationals. Clearly, we are too few.

February 7th – Rafah

(Pg 23) I have been in Palestine for two weeks now, and I have very few words to describe what I see. You just can’t imagine it unless you see it. And even then your experience is not at all the reality: (Pg 20) The West Bank and Gaza are under extremely strict curfew. You are not allowed to leave your house at all. Not for food. Nothing. The reality of curfew, of the checkpoints. People live like this . . . [at least] (Pg 23-24) I have money to buy water. I have the option of leaving.

I don’t know if many of the children here have ever existed without tank-shell holes in their walls. Can you forgive the world for years spent existing – just existing?

Rafah is a city of 140,000 people, 60 percent of whom are refugees. The Israeli army is building a wall between Rafah and the border. 602 homes have been completely bulldozed. Nowhere is invulnerable to Apache helicopters or the cameras of invisible drones we hear buzzing over the city for hours at a time.

(Pg 25) There are no rules. There is no fairness. There are no guarantees. It’s all just a shrug. And with that enormous shrug between being and not being. And I knew, the shrug would happen at the end of my life – I knew. My whole life is going to amount to one shrug and a shake of the head, so it if comes in eighty years or at 8 PM -- Who cares? Me. That’s my job.

(Pg 27) (Writing) Mom, I spent the evening and this morning with a family on the front line. The two front rooms of their house are unusable because gunshots have been fired through the walls, so the whole family sleeps in the parents’ bedroom. I sleep on the floor next to the youngest daughter. I am amazed at their strength in defending their humanity against the constant presence of death. I think the word is dignity.

March 9: (Pg 35-36) Ten greenhouses destroyed. [but] 300 people are dependent on those farms to live. 200 men arrested - Six in hospital. They don’t understand what has happened.

March 13: Intensive care unit – 12-year-old girl shot from tower in school near Nasser hospital. Shots inside hospital – three injured – nurses. Houses demolished – 41 injured.

Yesterday I watched a father lead his two tiny children out into the sight of tanks and a sniper tower and bulldozers because he thought his house was going to be exploded. This man felt it was less of a risk to walk out in view of the tanks with his kids than to stay in his house. I was scared they were all going to be shot, and I tried to stand between them and the tank.

Mom, I thought a lot about what you said about Palestinian violence not helping the situation. 60,000 people from Rafah worked in Israel two years ago. Now only 600 can go there for jobs.

The airport? No. Runways demolished, totally closed. The border for trade with Egypt has a sniper tower in the middle of the crossing. Access to the ocean – completely cut off in the last two years.

(Pg 37) So when someone says that any act of Palestinian violence justifies Israel’s actions, not only do I question that logic in light of the Geneva Convention, I question that logic on the basis of common sense.

If any of us lived with children in a place where soldiers and tanks and bulldozers could come for us at any moment. If we had no means of economic survival and our houses were demolished, don’t you think most people would defend themselves as best they could?

(Pg 38) I’m having a hard time right now. I feel sick to my stomach from being doted on by people who are facing doom. I know that from the United States it all sounds like hyperbole. The kindness of the people here, coupled with the willful destruction of their lives, makes it seem unreal to me. I can’t believe that something like this can happen in the world without a bigger outcry. It hurts me to witness how awful we can allow the world to be.

This has to stop. I still really want to dance around to Pat Benetar and have boyfriends. But I also want this to stop. Disbelief. Horror. Disappointment. I am disappointed that this is the base reality of our world and that we, in fact, participate in it. This is not what I asked for when I came into this world. This is not at all what the people here asked for. (Pg 39) Sorry for the diatribe . . . . I love you and Dad. (She leaves)

*****

(from the transcript of an eyewitness account by Tom Dale – A reporter’s voice)

REPORTER: Rachel walked to place herself in between the home and the bulldozer. It continued toward her with a mound of earth building up in front of it. And as the mound of earth reached Rachel, she had to climb to prevent being overwhelmed by it. This put her head and shoulders above the top of the bulldozer blade, clearly in the view of the driver, so he knew absolutely that she was there.

CONCLUSION Rachel Corrie was crushed to death by an Israeli bulldozer on March 16, 2003. An Israeli district court judge ruled her death an accident for which the state of Israel was not responsible.
```

---

## IC-0218: My Red Hand, My Black Hand

- Title: My Red Hand, My Black Hand
- Author (byline): Dael Orlandersmith
- Work: Not specified
- Publisher: Vintage Books
- Publication date as stated: Nov 2003
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DAUGHTER, FATHER, MOTHER, FATHER/DAUGHTER, MOTHER/DAUGHTER, FATHER/MOTHER, MOTHER/FATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1700
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dael Orlandersmith
Books: Take Ten II
ISBN: 978-1400032174
Publisher: Vintage Books
Date (Month/Year): Nov 2003
```

### Introduction (context only: never use it for content warnings)

```text
This story is of one girl's courageous search for belonging and acceptance in the two very distinct cultures that make up her heritage—African American and Native American

She tells us about the "Red" Tlingit and Lakota parentage of her father, who leaves the reservation to play blues rock in Boston . . . And the "Black" rural Virginia Background of her mother, who goes to Boston seeking the big-city life. Her parents meet at a dance and fall in love, but not without the complications of prejudice from their families

My Red Hand, My Black Hand by Dael Orlandersmith
```

### Performance text (classify this)

```text
CHARACTERS

DAUGHTER: Indian and black, aged late teens to mid-twenties.

FATHER: Native American, late fifties to mid-sixties.

MOTHER: Black, late fifties to mid-sixties.

NOTE: The reference in the script "boom, boom, boom boom!" should be spoken like the John Lee Hooker song "Boom, Boom!" Listen on YouTube at https://www.youtube.com/watch?v=X70VMrH3yBg The other reference, "Gonna shoot it right down," also should be spoken/performed in the spirit of the song.

Note that "sport highheeled shoes" and "sporting high-heeled shoes" are references to Chuck Berry's song "Sweet Little Sixteen." Listen on You Tube at https://www.youtube.com/watch?v=ZLV4NGpoy_E

DAUGHTER: My hands/ red/ black Dance to Rhythms Different / Various / similar rhythms

My Red Hand it dances to the
Rhythm of my Father's Blood I His Blood Beat / His
red
Man beat
PURE REDMAN

FATHER: My father/ his mother/ Tlingit from Alaska /

DAUGHTER: Died giving birth to him
She died/
But she still whispered to him /
My father / his father

FATHER: Santee Lakota

DAUGHTER: My father half Tlingit Half Lakota dreamer

FATHER: Transported Transported to Boston

DAUGHTER: He/ my Father crying for his
Father / Drumming up the
Rhythm of his Father Through
Pent up Angers
Wearing Eagle Feathers

FATHER: Sign of the Eagle

DAUGHTER: Sign of Scorpio-Nov. 4 / His birthday My Father/

FATHER: Eagle Born

DAUGHTER: Scorpion
beat his
hands to the rhythm of
his Father's Ghost

FATHER: His Father/ My Grandfather
Spent
Depleted
American Dreams / Stomped into the
Dirt of the Res /

DAUGHTER: His American Dream/

FATHER: to pick up
a Guitar
To be a Blues Man
To be a Red Man / Blues Man-

DAUGHTER: My Father's Father/ My Grandfather

FATHER: Ghost danced Lakota Style

DAUGHTER: to
his father / my Great Grandfather's rhythm
but he closed his eyes and also
Ghost dances with

FATHER: Robert Johnson / Mississippi John Hurt Blind Lemon Jefferson

DAUGHTER: He/ my Grandfather couldn't leave it/

FATHER: The Res-

DAUGHTER: They wouldn't let him leave it/ The Res/

FATHER: -"you're not True to your own"

DAUGHTER: -they said

FATHER: "you're not proud to be a red man"

DAUGHTER: they said-

FATHER: "If you leave/ Don't come back/

DAUGHTER: Don't come back to the Res"-they say

He / my Grandfather Looked
into my Father's Eagle eyes
A Child's eyes / knowing
eyes / an old child's eyes /
His eyes - my Grandfather's eyes
Said

FATHER: "Take the world/ make it yours / Rock the world You can Rock

DAUGHTER: Rock

FATHER: Rock

FATHER/DAUGHTER: Rock the World"

DAUGHTER: My Father Glides Eagle-eyed from the Res and the Tlingit island /

FATHER: Leather-jacketed /Eagle-eyed/

DAUGHTER: Blues and Tlingit l Lakota riffs dripping from his fingers /

FATHER: Chuck Berry /

DAUGHTER: Tlingit riffs
dripping from his fingers /
Leather-jacketed and Guitar ready
Just like Chuck Berry or

FATHER: Link Wray

DAUGHTER: -Link Wray

FATHER: -a Shawnee from North Carolina

DAUGHTER: -A RED / Blues Rock 'n' Roll man /

FATHER: -a cool man

DAUGHTER: My Father cool -Just like Link Wray

FATHER: Slick

DAUGHTER: -Just like Link Wray
Ghost dances Lakota Style / Tlingit Style
and Rock 'n' Rolled / a Steady
Rock 'n' Roll bop

and Somebody on the Res says
"How could you do that / Leave /
us / How could you? /
You're not proud of your own
kind" / Somebody on the Res says /
they say "wanna be a white
boy? / Wait till they call you a FeatherHead" /
Someone on the Res says

My Father stares straight ahead

FATHER: Eagle-eyed /

DAUGHTER: proud and Eagle-eyed Outside

FATHER: --Standing Tall

DAUGHTER: Inside-Rumbling
The voices of the Res rumbled /
inside of him but he continued to
dance/

FATHER: Ghost dance/

DAUGHTER: The Res voices Got Louder/
He continued to Blues dance /
Blues / Red / Blues / John Lee
Hooker dance / he had to
take the voices and shoot them
down / Vodka
Tequila
Bourbon
Hide himself in a woman's
Skirt / to kill the voices
Vodka
Tequila
Bourbon
Another woman's skirt / gonna shoot
it right
Down!
My Black Hand-

My Mother's hand / A Black Girl

MOTHER: Girl from Virginia/ my mother/ a Sharecropper Black Girl from Virginia /

DAUGHTER: Her mother/ my Grandmother Lynched/

MOTHER: it is Hard Time Virginia /

DAUGHTER: no Different from Hard Time Mississippi

MOTHER: "Don't walk anywhere except in Dark Town"

DAUGHTER: they told my mother

MOTHER: "Just stay in Dark Town"

DAUGHTER: -they told my mother

MOTHER: "Dark Town" was where the Dark people lived

DAUGHTER: they
weren't Black Then
They were colored then
and where they lived was
"Dark Town"

My Mother / Sharecropper Black Girl / Big Black Girl Knew about Trees

MOTHER: Knew about the Bodies that hung from those trees

DAUGHTER: and the people who wore billowing white sheets My mother's bare feet

MOTHER: were blistered from Tar and Dirt Roads /

DAUGHTER: Those feet Shifted themselves

MOTHER: into high heels/

DAUGHTER: She wanted to Chuck Berry Bop in her high heels / She wanted

MOTHER: to "Sport high-heeled shoes"

DAUGHTER: She wanted

MOTHER: her hair slicked back pressed and curled /

DAUGHTER: She wanted

MOTHER: to Lip Balm her lips-"Ruby" Red Just Like The Ray Charles Song /

DAUGHTER: She wanted

MOTHER: to snap her fingers/
Slick headed and curly sporting
high-heeled Shoes to the
rhythm of cities /

DAUGHTER: She wanted to Enter a New Rhythm Explore

MOTHER: -not just the Rhythm of Southern men Clinging to Mojo /

MOTHER/DAUGHTER: She wanted a city

DAUGHTER: She leaves Dark Town
Slick / curly headed
high heels and fingers snapping and
clicking/
She goes to Boston /
sporting high-heeled shoes

FATHER/MOTHER: There are Dances/

DAUGHTER: yes There are Dances People will always Dance

My Father sees her /
He sees her at a dance /
His Eagle eyes / connect to
her Brown / Black Girl Eyes

FATHER: Eagle-eyed RED man/

MOTHER: red-lipped high-heeled Black Girl

DAUGHTER: The Hucklebuck Dance meets The Ghost Dance

And the Colored People / Before They were Black / The Colored people said

MOTHER: -"Whachoo doin'
with him / Some Red Man /
What do you want with him /
Some Red Man / That FeatherHead
dancer / whachoo doin'
with him"

DAUGHTER: And the Skins on the Res said

FATHER: -"You didn't get
an Indian Girl / one of our
Girls / Got a Dark /
Darker/ NIGGER Girl/ not
a Girl from the Res /
What are you doing with her /
Why didn't you Get a Girl
From the Res! /
Come back to the Res!"/

DAUGHTER: They -- my Father my Mother

They both hear the voices /

FATHER: Voices from the Res/

DAUGHTER: The Tlingit Voice that whispers in his ear

MOTHER: Voices from the Virginia Fields

DAUGHTER: They—both--my Mother and Father
try to Ghost Dance / Blues Dance
Drink away the
Voices

FATHER: --Western/ Northern Red voices/

MOTHER: Southern Black voices

DAUGHTER: They dance
Snap their fingers
Guitar Lick / try to
Shoot it on Down

FATHER: Vodka

MOTHER: Tequila

DAUGHTER: Bourbon They try to shoot the voices down /

FATHER: Boom

DAUGHTER: Boom

MOTHER: Boom

DAUGHTER: Boom /
Shoot them all Down-
A year later-they marry-
A year after that
I crash through amniotic Fluid
and blood/
I crash but
silently my mother says

MOTHER: --"She's so quiet"/

DAUGHTER: my Mother says

FATHER: --"Makes no noise"'

DAUGHTER: my Father says
I hear his voice but rarely-him / he usually
Speaks through guitar fingers / his fingers speak
on his guitar I see him /
longhaired / this man/ red man who just spoke /
my father-this red man
this big red man / beautiful man
I am a part of him
My Father
I hear him
But
I can't speak But I can hear
I can't explain/ I'm a baby
But I feel it
I feel them

Turning on themselves
Turning on each other
not always with words
There's looks

MOTHER: shrugs

FATHER: silence

MOTHER/FATHER: more silence/

DAUGHTER: I feel it/
I feel them
Shooting Themselves
Down-

FATHER: Boom

MOTHER: Boom

FATHER: Boom

MOTHER: Boom

DAUGHTER: Later I'm a child not a baby / a child I see it / smell it

FATHER: Vodka

MOTHER: Tequila

DAUGHTER: Bourbon

I hear it my Mother's Black Southern voice slurry / shot-down voice

MOTHER: I love
him / He's my husband /
my man/ I'm
NEVER Gonna Leave / I love him!

DAUGHTER: The Black Southern/ voices /the
voices are now Black from
the Virginia Fields / The 1960s
and the voices are now Black
tell her / my Mother

MOTHER: -- "your child is a Nigger / FeatherHead / a Nigger Feather- Head” --

DAUGHTER: My Mother/ she Vodka

MOTHER: Tequila

DAUGHTER: Bourbon

MOTHER/DAUGHTER: Cries

DAUGHTER: I hear it in my
Father's voice-more so
in his fingers / Fingers
sliding up and down his guitar
Vodka
Tequila
Bourbon crying

FATHER: Lakota/ Tlingit guitar / Blues a shot-down
Red
Blues
Bruised
Man

DAUGHTER: His voice thundered/ sometimes there was thunder in his voice

FATHER: "She's my wife/ I love her/ Never Gonna give her up/ I love her!"

DAUGHTER: I grow up-my body
can make a
child
I Do not but I can-make a child

A child / a life / can come through me
can come crashing through amniotic
Fluid and Blood /
It can come silently
It can come thunderously

My Grandfather / Long Dead
Ghost dances in the hills /
His wife / my Grandmother
calls me -- "Dark Girl
Monkey Girl
animal/ Dark/ Monkey
Girl!/ The
elders don't want you /
WE don't want you!" She says /
my Grandmother says
My cousins on my mother's side /
My Black hand side says-

MOTHER: "You're Black/ what's this Indian / no such thing as HALF BLACK!"

DAUGHTER: They/ my cousins/ my Black hand
mother side cousins say put
down my Father's Tlingit walk / Ghost dance /
put aside sweet guitar licks and
the Red / Blues of my
Grandfather / Put aside
his slick / sleek
Rock 'n' Roll res/ Boston Bop/
Put it Down/
Shoot in on
Down

My Red hand / my Father's
hand / His mother / my
Grandmother / cousins
Don't call my name
I'm the "dark"/ Monkey Girl/
Don't have a name-
An uncle / he calls my name /
says my name/
only him / my Father's Brother /
my uncle / he says

FATHER: "Drop the
Black Blood / walk like a
Skin / Drop the Dark / Darkey
walk / You're a SKIN"

DAUGHTER: How can I drop the
walk of Southern Black
Girls / the walk heated / hip
walk of Southern high-heeled Black
Girls

MOTHER: (repeating) You're Black/ no such thing as HALF BLACK

FATHER: (repeating) Walk like a Skin

DAUGHTER: I answer to the voices
I answer to the voices in
Dark Town/
I answer to the voices in
Black Town / The Town where
Black people live
I answer to the voices My Grandmother's Tlingit voice
That whispers in my ear
I see / dance with my Grandfather /
We sing a Red man Blues
I am Tlingit / Lakota and Blues
I am an electric slider / Tlingit / Lakota Ghost Dancer
I've got Red / Black hands

I answer to all the voices

I know that Blind Lemon Jefferson
did the Ghost dance with Robert Johnson
and Robert Johnson before
selling his soul to the
devil pulled out the
Mojo and gave it to my
Grandfather who kissed it
and passed it on to my Father who
passed it to me -- I've got Red / Black hands

Don't tell me not to Ghost
dance on the Res
Call for my ancestors
on the Res/
whisper Tlingit secrets to my Grandmother /
dance/ Link Wray style
Down at the Res I
I will rock the Res

I've got

FATHER: Red /

MOTHER: Black

DAUGHTER: hands
Don't anybody expect me to
Shoot it
Shoot
Shoot
it
on Down
```

---

## IC-0219: My Sergei

- Title: My Sergei
- Author (byline): Ekaterina Gordeeva
- Work: Chicken Soup for the Couple's Soul
- Publisher: HCI
- Publication date as stated: 1999
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: EKATERINA
- Teaser before the introduction: Yes
- Spoken words (computed): 1755
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ekaterina Gordeeva
Book: Chicken Soup for the Couple's Soul
ISBN: 978-1558746466S
Publisher: HCI
Date (Month/Year): 1999
```

### Introduction (context only: never use it for content warnings)

```text
In the former Soviet Union, the sports establishment, charged with producing winners for the greater glory of the empire, had almost unlimited power over the athletically gifted. Children as young as five or six were identified, sent to special schools and given rigorous training in the sports in which they were expected to excel. Two such youngsters were Ekaterina Gordeeva and Sergei Grinkov, paired as skaters by their teachers when they were 11 and 14. As time passed and their joint career led to international championships, they fell in love and married. Their success culminated in Olympic gold medals in 1990 and 1994. And then, suddenly, Grinkov died of a heart attack in 1995 at age 28. My Sergei by Ekaterina Gordeeva
```

### Performance text (classify this)

```text
EKATERINA: Not long ago I heard someone ask a friend, “If you had to live your life over again, what would you do differently?” I’ve thought about this, and for me, I’d like to live my life over again backward. Any day I’m living now, I would exchange for any day in the past because I know that for me to find the kind of happiness I had with Sergei isn’t possible. It’s like trying to find the comet that was in the night sky last spring, which passes Earth once in seventeen thousand years. No matter what lies ahead, the best years of my life will have been with my Seriozha, and those years are now laid to rest.

EKATERINA: God took Sergei without warning – a heart attack on November 20, 1995. I lost my husband and best friend. I lost my favorite thing to do, because now I had no skating partner. It’s like I was living in a fairy tale before, and now I’ve been abandoned in a wild forest.

That is what life with Sergei was like, a fairy tale. It began the year I turned eleven. The pairs coach where I had skated since I was four, told me to come early to practice one day. He had chosen a skating partner for me. I was very excited because I knew it was going to be Sergei.

As a pairs skater, you have to learn everything you learned as a singles skater over again because you have to align your body with your partner’s. Sergei and I practiced the jumps endlessly. I was never scared of the lifts because I always felt very safe in Sergei’s arms. I’m not sure why, but once we were paired, I always believed Sergei was the only one who could skate with me.

Several years passed, we both grew up and we began preparing for the 1988 Olympics. As the games approached, everything became a little more stressful, a little more intense. In mid-November, during practice for an exhibition, Sergei caught his blade in a soft rut in the ice while holding me aloft and dropped me. The first part of my body to hit the ice was my forehead.

I didn’t feel any pain at first, then my entire head felt like it was splitting apart. I blacked out and was driven to the hospital. I ended up staying for six days. I’d suffered quite a serious concussion. I was mad at Sergei because I thought this fall was his mistake. Then, there was a knock on the door, and it was Sergei.

He was carrying a dozen roses, and he was very, very upset. Sergei continued to visit me at home every dat. When at last I could skate again, I immediately noticed a change in the way he was holding me. Something had happened in those two weeks, and I realized that his thoughts for me had changed. Before we had been like two skaters. After that, we were a pair.

I wondered, why me? Why am I so lucky? I was so young and small and shy, and Sergei could have had any nice long-legged girl. Why should he choose me? I believed he would love me just for a little while, and then it would be over.

We went on to win the gold medal at the 1988 Olympics in Calgary, Canada. And the following year Sergei and I were married, and our daughter, Daria, was born a year and a half later. Then in 1994 we won our second Olympic gold medal. The first gold medal we had won for the Soviet Union. This one we won for each other.

In 1995, we were training in Lake Placid for a fifty-five-city tour with the Stars on Ice. At the beginning of the program, I’m on one knee, and Sergei is on one knee, and we are face-to-face. I put my head on his shoulder, and I remember that his T-shirt smelled very clean. So I said, “Humm, smells good.” And he said, “Yes, it’s clean” Just that. They were to be his last words.

Then we started to skate. We did the early movements – the camel spin into a lift. The full orchestra was just coming in. Sergei was gliding on the ice, but he didn’t do the crossovers. His hand didn’t go around my waist for the lift. I thought it was his back, which had been bothering him for some time. He was bent over slightly, and I asked him, “Is it your back?” He shook his head a little. He tried to stop, but he kept gliding into the boards. He was dizzy, but he didn’t tell me what was happening. Then he bent his knees and ay down on the ice very carefully.

I kept asking what was happening. “What’s wrong, Seriozha? What’s the matter?” But he didn’t tell me. He didn’t speak at all.

Marina, our choreographer, stopped the music. When she came over to him, she knew right away it was something with his heart. It looked like he couldn’t breathe anymore. She told me to all 911, and she started doing CPR on him. I was so scared. I was screaming. I don’t know what. I forgot all the words in English. I couldn’t remember the word for help. I ran, crying, to get someone to call 911 for me.

By the time I got back, everyone was around Sergei, and the medical people were working on him, trying to get his heart going. Then the medical people were taking him in the ambulance, and I only had time to get my skates off and pick up Sergei’s bag. They had given him electric shocks. They had given him a shot of Adrenalin in the heart. But they had lost Sergei.

I can’t describe the feelings that went through me when I walked into the room where Sergei was lying, still with his skates on. It looked like he was just sleeping. I talked to him, all the time thinking: He will ever stand up. He will never take me in his arms again, never hug me again, never hold my hand again.

Then I started to take off his skates, and his feet were very cold. I tried to warm them up by rubbing them. I tried to warm his hands, too. I loved his hands very much – so big and soft. But I couldn’t make them warm.

The next morning I sat Daria down and we talked. “Your father is dead; he’s not coming back.” Daria didn’t cry or get upset. But she asked: “How can we see him?” So I told her that her father would come and see her whenever he wants and that sometimes she’d see him in her dreams. That he was like a little angel now. But that he’d never come back to her as we knew him and that it was very sad, and sometimes I would be crying, and that would be the reason.

We stayed in Moscow, living with my parents and taking one day at a time. I felt I was slowly losing myself. I had no purpose in my life, nothing to strive for. When I opened my eyes in the morning, I’d lie in bed wondering, Why do I awaken? I had nothing. No Sergei. Always the thoughts ended there. No Sergei to lead me out of the unending darkness.

I began to realize that work was what could help me heal. I still had skating. It was difficult for me to imagine myself skating in front of people without holding Sergei’s hand, without looking into Sergei’s eyes, looking only at the audience, trying to fill that huge ice surface all by myself. But if I was going to skate, that was how it would have to be. I wasn’t going to skate with another partner. Sergei’s was the only hand I had held on the ice since I was eleven years old.

The tribute night arrived. I was waiting behind the curtain, not watching for fear that I would cry and lose my composure. When I heard the music of Moonlight Sonata, so many memories came back. I found myself going through my movements for our free program from the 1994 Olympics. Here Sergei throws me. Here we spin. . . . I couldn’t stop myself. I didn’t want to stop myself. I felt Sergei’s spirit was beside me right then.

As the time neared for my solo number, a prayerful tribute to my union with Sergei, I thought about the words he used to say to me when we were getting ready to skate. We always kissed each other before we skated, we always hugged and touched each other. In the tunnel, waiting to go on the ice, I didn’t have anyone to touch or kiss. It was a terrible feeling to be standing there by myself. . . . “Just trust Sergei. He will help you.” The lights rose, the people started to applaud and I had a feeling I’d never experienced before. I’d been worried that I’d be lost out there by myself. That I’d be so small no one would see me. But I felt so much bigger than I am. I felt huge, suddenly, like I filled the entire arena.

I thought, I can’t stop or I’ll lose all this magic and power. I just listened to my legs. And I listened to Sergei. It was like I had double power. I never felt so much power in myself, so much energy. I’d start a movement, and someone would finish it for me. I didn’t have a thing in my head. It was all in my heart, all in my soul.

I’ll never be able to skate this number as well again. I don’t want to skate it again. It was such a special thing, and I don’t know if Sergei would help me a second time.

Afterward, I was supposed to say something, but as soon as I was handed the microphone, I couldn’t think of any words. Then I remembered what I wanted to say: “I don’t have enough words, but I want to wish to all of you: Try to find happiness in every day. At least one, smile to each other every day. And say just one extra time that you love the person who lives with you. Just say, ‘I love you’.

That is what Sergei taught me.
```

---

## IC-0220: Nanette

- Title: Nanette
- Author (byline): Hannah Gadsby
- Work: Not specified
- Publisher: Scraps from the Loft.com
- Publication date as stated: July 21, 2018
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2193
- Already set (do not supply): none

### Source block (context only)

```text
Author: Hannah Gadsby
ISBN: N/A
Publisher: Scraps from the Loft.com
Date (Month/Year): July 21, 2018
```

### Introduction (context only: never use it for content warnings)

```text
Hannah Gadsby is an Australian comedian and writer who got started when she entered a standup comedy contest in 2006, performing for the very first time—and winning. But comedy rose to a new level when she used the stage to speak her truth in 2017 – a message that not only spoke to the LGBTQ community, but to anyone of difference and without social status.

Nanette by Hannah Gadsby
```

### Performance text (classify this)

```text
[NOTE: Transcript published only on-line. Check publication requirements for your tournament before performing]

I first started comedy over a decade ago. My first ever show was Classic New Gay Comic 101. I told lots of cool jokes about homophobia. Really solved that problem. Tick. I told a story about the time this young man had almost beaten me up because he thought I was *coming* on to his girlfriend. Actually, that bit was true, but . . . there was a twist. It happened late at night. The pub had closed, and I was waiting at the bus stop. It was the last bus home. And I was talking to a girl, and . . . you know, you could say flirting. I don’t know. And out of nowhere, he just comes up and starts shoving me. And he goes, “Keep away from my girlfriend, you freak!” And she stepped in, going, “Whoa, stop it! It’s a girl!” And he said “Oh, sorry. I’m so sorry. I don’t hit women,” he said. What a guy! “I don’t hit women.” How about you don’t hit anyone? Good rule of thumb. And he goes, “Sorry, I got confused. I thought you were a faggot trying to *come* on to my girlfriend.” Now I understand I have a responsibility to help lead people out of ignorance at every opportunity I can, but I left him there, people. Safety first.

The main part, the centerpiece, of that 1st show, was coming out to my family, and particularly my mom. Because my mom is very funny. She lives a comedy better than I can ever write it. Her response to me coming out, was this. “Oh, Hannah. Why did you have to tell me that? That’s not something I need to know. I mean, what if I told you I was a murderer?” (self-deprecating laugh) It’s still funny. And it’s a fair call. Murderer. (grows serious and sad) Murderer. Real jokes.

I do think I have to quit comedy though. I have been questioning . . . you know, this whole comedy thing. I don’t feel very comfortable in it anymore. I built a career out of self-deprecating humor. That’s what I’ve built my career on. And . . . I don’t want to do that anymore. Because, do you understand . . . do you understand what self-deprecation means when it comes from somebody who already exists in the margins? It’s not humility. It’s humiliation. I put myself down in order to speak, in order to seek permission. . . to speak. And I simply will not do that anymore. Not to myself or anybody who identifies with me. And if that means that my comedy career is over, then so be it. I got a letter… on Facebook recently. And I say “letter,” ’cause I’m very bold. Controversial. But I call it a letter, because it said, “Dear Hannah,” comma, new line. . . “You owe it to your community to come out as transgender.” All jokes aside . . . I don’t identify as transgender. I mean, I’m clearly “gender not normal,” but. . . I don’t think even lesbian is the right identity fit for me, I really don’t. I may as well come out now. I identify. . . as tired. I’m just tired. (heavy sigh and then she jumps back in with some comedy)

Did you know men and women have more in common than they don’t? I don’t think many people do know that because we always focus on the difference between men and women. You know what’s weird? Pink headbands on bald babies! That’s weird. Of course, I understand why parents do it. Clearly, they’re sick and tired… of their beautiful baby girl… being mistaken for a boy baby because of the no hair situation. I understand that. How about this? How about we stop separating the children into opposing teams from day *one*? How about we give them, I dunno, seven to ten years to consider themselves on the same side?

I say we get rid of pink and give all babies blue. I’ve thought about this and it’s not because blue is a masculine color. ‘Cause that is false. I love that people go, “Blue, yeah, a very masculine color. Very reliable. Very rational color, blue. Yeah, you can trust blue. It’s why we’ve got it on flags. Lot of blue on flags.” Blue, if anything, is a feminine color. It really is full of contradictions. You know, blue is on the cold end of the spectrum. But the hottest part of the flame? Blue. If you’re feeling blue. . . you’re sad. But optimism? Blue skies ahead! Make up your mind. A blueprint is a plan, but if something happens not on the plan, where does that come from? Out of the blue! Blue’s a wonderful color to start life with. There’s room for every kind of human in blue. (Beat, change of subject and a more serious tone)

I don’t hate men, but I wonder how a man would feel if they’d lived my life. It was a man who sexually abused me when I was a child. It was a man who beat the shit out of me when I was 17, my prime. It was two men who raped me when I was barely in my twenties. Tell me why is that okay. Why was it okay to pick me off the pack like that and do that to me? It would have been more humane to just take me out to the back paddock and put a bullet in my head if it is that much of a crime to be different!

Laughter’s the best medicine, they say. I don’t. I reckon penicillin might give it the nudge. There is truth to it, though. Laughter is very good. When you laugh, you release tension. And when you hold tension in your body, it’s not healthy -- psychologically or physically. That’s why it’s good to laugh. It’s even better to laugh with other people. When you laugh, in a room full of people, you will release more tension because laughter is infectious.

Let me explain to you what a joke is. When you strip it back to its bare minimum, a joke is simply two things, it needs two things to work. A setup and a punch line. And it is essentially a question with a surprise answer. Right? I feel like, in a comedy show, there’s no room for the best part of the story. . . which is the ending. You know, in order to finish on a laugh, you have to end with punch lines. Like, take my coming-out story, for example. The best part of that story is the fact that Mum and I have a wonderful relationship now. More than mother and daughter, we’re friends, we trust each other. Look what I did to the room. No tension. You’re just going, “Good *for* you. Got a good relationship with your mum, have you? Can you go back to the tension? That was hilarious.”

But, yeah, last year I was home for a week. Mum and I banter if you will. I say things like, “Mum, you made my life very difficult.” And she’ll go, “Yeah, well, I don’t think I liked you very much.” And we laugh! ‘Cause you’ve got to laugh. (long beat) But not this day. She went quiet and got tense. What my mum eventually said to me is pretty much at the core of why I’m questioning comedy. She said to me, “The thing I regret is that I raised you as if you were straight. I didn’t know any different. I am so sorry. I’m so sorry. I knew… well before you did… that your life was going to be so hard. I knew that, and I wanted it more than anything in the world not to be the case. And I know I made it worse, because I wanted you to change because I knew the world wouldn’t.” And I looked at my mum in that moment and thought, “How did that happen? How did my mum get to be the hero of my story?” She evolved. I didn’t.

See I think part of my problem is comedy has suspended me in a perpetual state of adolescence. The way I’ve been telling that story is through jokes. And stories . . . unlike jokes, need three parts. A beginning, a middle, and an end. Jokes only need two parts. A beginning and a middle. And what I had done, with that comedy show about coming out, was I froze an incredibly formative experience at its trauma point and I sealed it off into jokes. And that story became a routine, and through repetition, that joke version fused with my actual memory of what happened. But unfortunately, that joke version was not nearly sophisticated enough to help me undo the damage done to me in reality. Punch lines need trauma because punch lines need tension, and tension feeds trauma.

Seventy percent of the people who raised me, who loved me, who I trusted, believed that homosexuality was a sin, that homosexuals were heinous, sub-human pedophiles. Seventy percent. By the time I identified as being gay, it was too late. I was already homophobic, and you do not get to just flick a switch on that. No, what you do is you internalize that homophobia and you learn to hate yourself. Hate yourself to the core. I sat soaking in shame. . . in the closet, for ten years. Because the closet can only stop you from being seen. It is not shame-proof.

When you soak a child in shame, they cannot develop the neurological pathways that carry carry thoughts of self-worth. They can’t do that. Self-hatred is only ever a seed planted from outside in. But when you do that to a child, it becomes a weed so thick, and it grows so fast, the child doesn’t know any different. It becomes as natural as gravity.

When I came out of the closet, I didn’t have any jokes. The only thing I knew how to do was to be invisible and hate myself. It took me ten years to understand I was allowed to take up space in the world. But, by then, I’d sealed it off into jokes like it was no big deal. I need to tell my story properly. Because I paid dearly for a lesson that nobody seems to have wanted to learn. And this is bigger than homosexuality. This is about how we conduct debate in public about sensitive things. It’s toxic, it’s juvenile, it’s destructive. We think it’s more important to be right than it is to appeal to the humanity of people we disagree with.

Do you remember that story about that young man who almost beat me up? It was a very funny story. I made a lot of people laugh about his ignorance, and the reason I could do that is because I’m very good at this job. I am pretty good at controlling the tension. And I know how to balance that to get the laugh at the right place. But in order to balance the tension in the room with that story, I couldn’t tell that story as it actually happened. Because I couldn’t tell the part of the story where that man realized his mistake. And he came back. And he said, “Oh, no, I get it. You’re a lady faggot. I’m allowed to beat the shit out of you,” and he did! He beat the shit out of me and nobody stopped him. And I didn’t . . . report that to the police, and I did not take myself to hospital, and I should have. And you know why I didn’t? It’s because I thought that was all I was worth. And that is what happens when you soak one child in shame and give permission to another to hate. And this tension, it’s yours. I am not helping you anymore. You need to learn what this feels like because this . . . this tension is what not-normals carry inside all of the time because it is dangerous to be different!

I don’t tell you this so you think of me as a victim. I am not a victim. I tell you this because my story has value. My story has value. To be rendered powerless does not destroy your humanity.

Your resilience is your humanity. The only people who lose their humanity are those who believe they have the right to render another human being powerless. They are the weak. To yield and not break, that is incredible strength. Diversity is strength. Difference is a teacher. Fear difference, you learn nothing. What I would have done to have heard a story like mine. Not for blame. Not for reputation, not for money, not for power. But to feel less alone. To feel connected. I want my story. . . heard.

The damage done to me is real and debilitating. Laughter is not our medicine. Stories hold our cure. Laughter is just the honey that sweetens the medicine. I don’t want to unite you with laughter or anger. I just needed my story heard, my story felt and understood by individuals with minds of their own. Because, like it or not, your story. . . is my story. And my story. . . is your story.
```

---

## IC-0221: Necessary Targets

- Title: Necessary Targets
- Author (byline): Eve Ensler
- Work: Not specified
- Publisher: Random House
- Publication date as stated: Jan 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: JS, MELISSA, JELENA, ZLATA, SEADA, NUNA
- Teaser before the introduction: Yes
- Spoken words (computed): 1527
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eve Ensler
ISBN: 978-0375756030
Publisher: Random House
Date (Month/Year): Jan 2001
```

### Introduction (context only: never use it for content warnings)

```text
When we think of war, we think of it as something that happens “elsewhere” – never in the United States. It happens to men in fields or jungles with hand grenades and Scud missiles. And we become voyeurs, watching the carnage like it’s some reality television show. The bombings, the explosions in the dark that keep us watching. But after the bombing, after the snipers, that’s when the real war begins. Because you see, the aftermath of war is just as devastating. It can be found in the broken-down fabric of community, in trauma and depression, poverty and homelessness and starvation. Necessary Targets is a play about women and war -- about the violence of dark memories and the enduring resilience of the human spirit.

Necessary Targets by Eve Ensler
```

### Performance text (classify this)

```text
JS: (Pg 7-10) (she speaks as she reviews paperwork) Your resume’s impressive. You come highly recommended. You’re trained as a therapist and a writer. That’s very unusual.

MELISSA: I am not a therapist. I’m trained as a trauma counselor. I only work with seriously traumatized populations.

MELISSA: Why are you going to Bosnia?

JS: For the President’s commission. It’s a huge honor. They chose a range of professions for the team. I’m the “shrink” piece. At one time it was my field, trauma.

MELISSA: Yes, eating disorders. I am familiar with your books. (beat) You have never been to a war-torn country?

JS: God, no. I mean, Bosnia. . . I read the news, but the Balkans were not next on my vacation map.

MELISSA: War is not exactly the same as anorexia.

JS: I am a psychiatrist. 26 years in private practice. Trauma is trauma.

MELISSA: In Haiti, the psychiatrists were fleeing like flies.

JS: Haiti? Weren’t you afraid?

MELISSA: Not in Haiti – in Rwanda, yes . . .

Bosnia. A refugee camp. A barracks-like room. Desolate. Emptiness - a feeling of poverty.

JS: (Pg 16-19) (enters) There are big, dirty footprints in the bathroom

MELISSA: Yes, you squat in them

JS: (appalled) You mean to . . .

MELISSA: (laughing) Poop. Yes, you squat to poop.

JS: (clearly privileged) You’ll excuse me, but I need the little comforts. I welcome a bath, clean sheet, and a place to sit to . . .

MELISSA: Poop. These women need those same comforts. They had them all before the war.

JS: I don’t think squatting in filthy footprints will make me a more effective therapist. ****Scene*****

JELENA: (Pg 29) (Introducing JS and Melissa to 2 of the refugee women) This is Seada, the gorgeous one. She is from the country. She never went outside her village before the war. And this is our Zlata, a doctor. You will have a hard time winning Zlata. (Seada holds out a wrapped little baby and giggles) Oh, yes. . . and of course, Doona.

ZLATA: (Pg 30-31) What do you want with us?

JS: I have come here . . . well (looking at Melissa), we have come here . . . to help you.

ZLATA: (sarcastically) And how do you plan to do that?

MELISSA: We are here to help you, well . . . talk.

ZLATA: There is no shortage of talking here. We are sick of talking.

SEADA: (Pg 47) (interrupting) Would you sing to me, Mama?

JS: (Pg 31) We are here to help you talk about the war, about the. . . (Zlata laughs)

ZLATA: You flew all the way here for that? Two American doctors to “help” poor Bosnian refugees talk about the war? What did you think we were talking about before you came? Our lingerie, our dinner parties . . .

MELISSA: (Pg 32-35) We are very moved by what you’ve been through. We were hoping you would tell us your stories.

ZLATA: You and everybody else. They came from everywhere at the beginning of the war to hear the gory details. They left and they never came back.

MELISSA: Exactly. It is important that people know your stories the way you want to tell them. I am working on a book composed of the stories of refuges all around the world.

ZLATA: Oh, so we’re a chapter.

MELISSA: No, no. My writing is not to exploit you. Traumatized war victims . . . Would anyone object to my recording our sessions?

ZLATA: I do not want you recording me.

SEADA: (Pg 47) (it almost seems that she is speaking to Zlata, but she is simply muttering to
herself, trapped in her world) Are you afraid, Mama? Are you afraid too?
*****Scene*****
Barracks room with two cots. J.S. is furiously packing when MELISSA enters.

JS: (Pg 37-39) I’m going home. This is ridiculous. Coming to Bosnia to help refugees talk about the war.

MELISSA: I through you were a trained psychiatrist. Trained to see through denial and well-constructed defenses.

JS: (angry) Listen. I can’t help these women. They need homes, a country, and care. I sense their rightful contempt at being patronized.

MELISSA: I’ve been in other wars. It always begins like this. These women need an outlet for their rage and despair. We are necessary target.

JS: How does it end?

MELISSA: They tell their stories.
*****Scene*****
Outside the barracks. It is early dawn. ZLATA is sitting on a chair. She has been weeping. She is
visibly disturbed. JS enters quietly. She breathes in deeply, then reacts to the rancid smell.

ZLATA: (Pg 58-59) Yes, the smells hang. Onion, Old cheese. Garbage. All hanging like a bad mistake.

JS: I am not accustomed to this.

ZLATA: Are you wealthy? (JS raises her eyebrows, but doesn’t respond) You are wearing a Christian Dior nightgown in a refugee camp. (shakes her head) I was rich like you . . . before.

My parents were very important people. I sleep now in the place of cows. (JS looks at her meaningfully and nods for her to continue) Don’t. Don’t do that psychiatrist thing with me. You only care about the gory details of the story. That’s all any of you want.

JS: (Pg 63-65) I want to be your friend.

ZLATA: (Shaking all over, she speaks with great emotion) This happened to real people. We were just like you, we weren’t ready for this – nothing in our experience prepared us – there were no signs. You want us to be different than you are so you can convince yourselves it wouldn’t happen there, where you are. That’s why you turn us into stories, into beasts, people who live in a strange country – then you can feel safe, superior. (She speaks in a mocking superior voice) “Get us one raped Bosnian woman, preferably gang-raped, preferably English speaking.”

JS: I am a doctor, Zlata.

ZLATA: (broken) I was a doctor, too, before the war. I was the head of the pediatrics unit in Prijedor’s main hospital. Now I stare off at the stars without explanation. I look out at the beet fields and weep for no reason. *****Scene***** A new day in the barracks. A Group Session with the refugees)

MELISSA: (Pg 89-91) Where is Seada?

ZLATA: (dismissively) Seada’s doing fine.

MELISSA: Because she has us – we support her fantasy world, we agree with her delusions. She’s living a lie. She’s in complete denial. It’s killing her.

ZLATA: No, Melissa. What happened to her during the war is killing her. What you call “denial” is keeping her alive.

MELISSA: Barely. She has nightmares almost every night. She’s hysterical or wildly depressed most of the time.

ZLATA: Again the assumptions – that we are sick and you know better than us what we need.

MELISSA: (Pg 93) We need to address some basic issues here.

JS: Like what?

MELISSA: Like what the hell happened to Seada? If we know what happened to Seada, we can help her being to talk about it. We can prepare her for her feelings. Otherwise, she will be consumed by what she refuses to remember . . . (Melissa turns her recorder on and one of the women, Nuna, begins to speak)

NUNA: (Pg 94-97) Seada lived with her mother and husband. They had a beautiful life in this small village, and a beautiful baby, Doona. Everyone took care of everyone. [But] when the soldiers came . . . They made the people come into the square . . . (Seada appears outside the group, holding her baby and listening)

JELENA: Seada was the most beautiful girl in the village. Her husband had heard how the soldiers had been raping the young girls, so they hid Seada in the house.

NUNA: The soldiers found them, though. They tried to take Seada. Her mother and her husband put up a fight and they shot them, both of them, right in the head. Seada saw this happen. She was holding her baby, Doona and she went mad. She started running into the night. The soldiers chased her, but she was running like the wind, for hours without stopping.

JELENA: When you are running crazy like that, You can lose your way.

NUNA: Or . . . your baby. You can lose your baby.

JS: Seada dropped her baby? Oh, my God.

NUNA: She dropped her as she was running.

SEADA: (Looks down at her bundle of rags and unfolds it. She screams) Doona! Doona! I have to find Doona! (She runs out) *****Scene*****

Outside. SEADA is on the ground, digging madly at the dirt, pulling her hair, rocking back and forth,

SEADA: (Pg 102-105) Mommy! Mommy!

JS: Approaches gently and speaks softly. No, Seada, no Mommy. I’m JS . . . I’m right here.

SEADA: (wildly anxious, she throws her arms around JS’ neck and clings) No Mommy. No Mommy.

JS: (JS wraps her in a calming hug) It’s okay, Seada. I’m right here.

SEADA: Please . . . please help me – help me find my baby. I was a good mother. Help me. (suddenly mad and panicked) Those lights, and those voices . . . l loud deep voices laughing, making fun of me. Laughing voices wearing black masks, stinking of shit and meat, tear off my blouse. One spreads my legs and the other holds my arms. (She intonates in the voice of her rapist) “We’ll show you how to make real babies. We’ll fill you with the right kind of babies.” And I can hear her suddenly, hear her crying out for her mother. (wails like her baby) I cannot get it out of my brain. (tears at her hair as she continues to wail. JS grabs her and rocks her and Seada gets quiet, confessional) Mama, I’ve lost my baby. I’ve lost our little Doona. (Silence) ***** Scene***** A few days later . . . J.S. sits outside under the stars, clearly disturbed. It is late. ZLATA comes upon her, sits and speaks softly, all sarcasm and bravado gone.

ZLATA: (Pg 111) I am impressed. Really. Doctor to doctor. You did good. (Pg 114-115) (JS begins to cry) What is it?

JS: Nothing. This is not your problem. . . it’s the . . .

ZLATA: (finishes for her) . . . beauty. Bosnia. Bosnia was beautiful. The snowy mountains, the green green hurt heart of Bosnia. (she gets lost in her own memory, her story) The kindness we shared, how we lived in each other’s warm kitchens. Gone. The ancient bridges, the mosques, the churches broken now, blown to bits and pieces. It isn’t the cruelty that broke my heart. Cruelty is easy. Cruelty, like stupidity, is quick, immediate. They break in, they wear masks, they smell bad, they have machetes, they chop off the heads of my old parents sitting on their couch. There is blood, lots of it. There is screaming. There are dead, headless bodies. We are dead – all of us – to the suffering. There is too much of it – but remind us of the beauty, the beet fields in full bloom, the redness of the fields. Remind us how we once sang, how the voices echoed as one through the landscape of night and stars. Remind us how often we laughed, how safe we felt, how easy it was to be friends. All of us. I miss everything – Bosnia was paradise.
```

---

## IC-0222: A New Home

- Title: A New Home
- Author (byline): Dori Samadzai Bonner
- Work: The Moth Presents All These Wonders, Pg 174-180
- Publisher: Crown
- Publication date as stated: Mar 2017
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DORI, DAD, OFFICER, JUDGE
- Teaser before the introduction: Yes
- Spoken words (computed): 1234
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dori Samadzai Bonner
Book: The Moth Presents All These Wonders, Pg 174-180
ISBN: 978-1101904404
Publisher: Crown
Date (Month/Year): Mar 2017
```

### Introduction (context only: never use it for content warnings)

```text
Poet Warsan Shire gave voice to refugees world-wide with her words . . . “No one leaves home unless home is the mouth of a shark. You only run for the border when you see the whole city running as well. . . No one would leave home unless home told you your survival is more important. . . No one leaves home until home is a sweaty voice in your ear saying – leave, run away from me now. I don’t know what I’ve become, but I know that anywhere is safer than here.”

Fleeing the Soviet invasion of Afghanistan, one family seeks asylum in the US. A New Home by Dori Samadzai Bonner
```

### Performance text (classify this)

```text
DORI: (Pg 174-180) I grew up in Afghanistan during the Russian occupation, and as a child I remember my dad being gone a lot. The subject of my dad's whereabouts was taboo; my mom told us never to ask about him, so we never did.

Growing up during the war was very difficult. We had bomb explosions and missile attacks on a daily basis. By the time I was ten, these explosions were getting closer and closer to the city of Kabul, where we used to live. In fact, there's a distinct whistling sound that the missile makes right before hitting its target (whistling sound . . . explosion).

DORI: There was a rumor about a regime change, which was devastating news for my dad, who was a high-ranking officer working for the current regime. Historically, the newer regime takes over by violently dismantling the old regime. My parents were desperate to get out of the country, After a daring escape in the middle of the night, my parents, my brother and I migrated to the US on forged papers and asked for political asylum. This meant that we could stay here temporarily while they reviewed our case. They gave us a work permit, driver's license, and Social Security card.

So, all of us started working. We had family in California who helped us get settled.

Fast-forward five years, I'm at my job at the Men's Wearhouse, and my dad calls me.

DAD: (excitement in his voice) You need to come home right away, because there's a letter from immigration.

DORI: I speak the best English in my household, so he wanted me to come home and translate. I rush home, and I find my dad in his security-guard uniform. My mom and my brother are home, 'cause my dad called them, too. I read the highlights really quickly. It says our appointment has been moved up to next week, and that we need to bring all of our legal documents and our family photos. This is it. This is the appointment that we've been waiting for. The day of our appointment, we drive to downtown Los Angeles, and go into a big government building. An immigration officer guides us into this room. We felt like we were in the wrong place. The people sitting there were visibly upset. Some of them were crying.

OFFICER: Just sit down until you hear your last name.

DORI: Can you tell me how long this appointment might take? My dad needs to get back to work.

OFFICER: Your dad will get back to work, all right, just not in this country.

DORI: And my heart just dropped. Going back was not an option, because we're now considered traitors, and would be arrested as soon as we got off the plane. I sat down and hesitantly told my dad this, and my dad lost all the color in his face.

After about forty-five minutes, a man walks in and says our last name, and all four of us get up. A judge is sitting there. It's an older gentleman, and he looks really intense. He won't even smile.

The judge turns his attention to my dad. After some basic questions, he asks my dad if he has a translator.

DAD: My daughter will translate for us.

DORI: I was pretty intimidated.

JUDGE: Young lady, whatever I say to you, you translate exactly what I say, nothing more, nothing less. And whatever your dad says, you tell me exactly what he says, nothing more, nothing less.

DORI: I agree. He asks my dad questions, really demeaning questions, like, "Do I understand correctly that you came here on forged papers?" And my dad starts to say, "Well, yes, but . . . " And then my dad goes into this long explanation. But the judge cuts my dad off and says, "I just want to hear yes or no. I don't care about the explanation." And so the conversation goes on like this, back and forth, and it's not going well at all.

JUDGE: You know, we here in the United States do not give citizenship to people that break the law. We can't, and I won't.

DORI: And as soon as I translate this to my dad, I put my head down, and I just start praying. (Clasp hands and pray) When I open my eyes, I see my dad rising out of his seat. He starts unbuckling his belt, at which point I'm thinking he's completely los-ing his mind. I'm not sure what he's doing.

But he lifts up his shirt on the right side and, in his native language, looks at the judge and says, "This is what the communists did to me." He's pointing to a five-inch knife scar.

Then he pushes down his pants in the back and turns around a little bit, and again says, "This is what the communists did to me," pointing at three gunshot wounds.

And he takes off his shoes, and takes off his socks, and says, "This is what the communists did to me." He's pointing at his toenails, which they had tried to pull out with pliers.

I remember thinking, I know I'm hearing what I'm hearing. But everything wasn't registering, because I am translating these horrible things and also learning for the first time about my dad's whereabouts. All those times years ago that I didn't know where he was, wondering if he cared about me, he was in prison being tortured. And in that moment, I have never felt more sorrow.

DAD: (with great pride) It's easy for you to judge me. You sit in that seat and you wear that robe. But if you came on this side, and you looked at me -- one man to another -- you will see that everything I did, I did to save my children. I had no other choice.

And you might deny it right now, but had it been you, I know you would have done the same thing. If you have to show the American public that you didn't take it easy on us, I understand. (crying) Send me back. I volunteer. But please let my children stay. Please give my children a new home.

DORI: The judge leaves. We're on a break. [He] comes back after an hour, and as soon as he enters the room, I notice he doesn't have his robe on. He goes up to his chamber and grabs something and starts walking back towards us. We're pretty nervous. The entire time his eyes are on my dad. He goes past me and stops right next to my dad.

JUDGE: Mr. Samadzai, let me see your hand.

DORI: My dad shows him his hand, and the judge puts a stamp in my dad's hand and says, "Mr. Samadzai, I would like you to be the one to stamp your children's papers." Together they stamp our papers: ASYLUM GRANTED

He then flips the page to my parents' papers and stamps it with the same stamp.

He looks down at my dad, puts his hand on his shoulder, and says, "Welcome to America."

It took us eighteen years from the day that we arrived here for me to be granted an American citizenship. On January 29, 2009, I was sworn in as an American citizen, and I pledged allegiance to my new homeland.

And it is through my children, that I will make sure that this gratitude that overflows in my heart every single day will continue to live on long after I am gone.

May God always bless our America.
```

---

## IC-0223: New York

- Title: New York
- Author (byline): David Rimmer
- Work: One on One
- Publisher: Applause Theatre and Cinema Books
- Publication date as stated: 2007
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MARY, SARAH
- Teaser before the introduction: No
- Spoken words (computed): 1258
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Rimmer
Book: One on One
ISBN: 1557837007
Publisher: Applause Theatre and Cinema Books
Date(Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
Today all that remains of the World Trade Center is a flight of battered steps, rising into an empty sky. On September 11, hundreds fled down these stairs from the flames and falling debris. "Survivor's guilt" is a term used to describe a sense of self-blame and remorse felt by a person who has experienced or witnessed a life-threatening event during which others did not survive. They begin to question, "Why them and not me?" For most Americans, the moment the airplanes crashed into the World Trade Center is burned into their memories. Collectively, we are all survivors. New York by David Rimmer is just that, a snapshot of survivors. Today I’d like to introduce you to two . . . Mary and Sarah. Mary? (by way of introduction, encouraging her to speak)
```

### Performance text (classify this)

```text
MARY: I'm unmarried. I live alone in Brooklyn, behind a Catholic church, which is lucky because it's my church. The Church means a lot to me. The priest, Father Barnes, is my friend. He helped me a lot, but I still thought I'd try you...

(Smiles.)

I'm Director of Human Resources-Personnel-for a research and development company. I've never been married. I was engaged once. Twice. Well... once and a half My mother's gone, my dad's not doing too well. I have two sisters and a brother-younger, married with kids. I guess I was just cut out to be an aunt. Those kids are a joy. I always thought I'd-I never thought I'd look at myself at this age and see someone not married.

(Shifts in her chair.)

I've been getting panic attacks. The sound of a bang brings it all back. I just-haven't felt the same. On a daily basis. Little things. I get a paper cut every day. Like clockwork. Everything I pick up I drop. I spill-constantly-I'm making my dry cleaners rich.

(Shrugs; sighs.)

It hit me a little harder over the holidays. I was with my family of course. Every time I saw my nieces and nephews run or laugh or have fun, I teared up. They shouldn't have to know about things like - The baby was a comfort though. I looked into her eyes and it was wonderful. She didn't know anything.

(Smiles.)

I have a little garden in the back of my apartment. I go there to-sit, relax, and think. And

(Lightly. )

this is a confession, Father Barnes knows it too. Every month or so, I sit there and have a cigarette. That's all. It's not the world's most shocking confession. The night of Christmas Day I came home, sat outside in my big coat, lit a cigarette, and started crying-and I couldn't stop and I burned a hole in my favorite plant. I don't go in my garden any more... All this isn't very important in the big scheme of things.

(Pause)

I feel so self-indulgent! I've never been to a-I don't know why I'm bothering you. I'm sure there're so many people much worse off than me. The young widows - I think of them and - I didn't get on the first subway that morning. It was packed and I thought who needs this? So I waited and took the next subway. I got out of the station at Cortlandt Street and saw a plane go into a building. People were running and I just ran along with them. A vendor had T-shirts and another vendor had bottled water and they were passing them out and people were putting wet T-shirts over

(Covers her mouth and nose.)

Smoke and dust everywhere. A high school ring fell out of the sky right at my feet. Then at that little park near City Hall, my cell phone rang. I didn't want to answer it-I was afraid-I hate cell phones! That stupid little ring! Not like a real phone-People answer them in the middle of the street- "Hello?!"- You think they're yelling at you! - But I answered it. It was Nina Carmichael. She was trapped in a closet in the tower-She went in there to escape the flames and she couldn't get out. She didn't know how much time she had-she just knew it wasn't much-She wasn't even a close friend. That's the thing- I barely knew Nina Carmichael-She was in my class at college but I didn't know her that well. She sent me an e-mail over the summer-I was helping her with the class reunion. We had lunch maybe once. I don't know why she called me. She said, "I can't reach my mother, Mary. I love her. I love my father and my sister. Please tell them - " She wanted to pray with me. "I love you Mary- "Then she's gone. I went and told them. They were so - Who am I? Why did she call me? So she wouldn't be.. . alone. . . when she....

TRANSITION

A lot of people talk about how their lives have changed since 9/11 or that their lives have been changed forever. And yet for 97% of people living in the United States the only thing that has really changed is that they pay a little more for gas or they have to wait a bit longer to get on a plane to fly to their favorite vacation spot.

Only those who have experienced sudden tragic loss of a loved one can truly understand the loss of the 9/11 families, and what a struggle each day is when your world is changed forever in an instant.

About 3,000 children lost a parent that day. Sarah, though she’ll deny that she had any feelings for her future step-father is one of those children Sarah?

SARAH: So, what.

(Beat)

You want my life story? I live in Queens. My mother's an idiot. She has this boyfriend, Dennis. He calls me from this bar the night before 9/11 for no reason. What a dick. No, he-He was just like tryin' too hard to reach out or something. He's marryin' my mom, y'know, so he has to suck up to me. - Hey, I got a dad!

Anyway, Dennis got a week's work in Tower One. He didn't die saving anybody or anything, he was just working maintenance.

I don't know. I guess I liked him all right. Not really. Marie-my mother-she loved him enough for two. lt was like, retarded-deranged. I come home, they're all over the couch... "Ohh! Ohh! Ohh!"... They're so stupid. She's pregnant. She's gonna walk down the aisle like this.

(Holds out her stomach, does a mock waddle.)

Nice. Same thing happened when I was born. She was 17. She doesn't learn. They've got this new thing now? Contraception? Hello? And she wanted me to take Dennis' name. I was gonna bail on that one. Now I guess I don't have to...

I was thinkin' of takin' my real dad's name, just to piss her off God, she hates him. She says, "Oh now he comes around, now." What's the difference? I don't miss him - I never knew him. He ditched her and joined the Army when she was gonna have me. I don't blame him. I mighta done it... I see him once in a while. I have to sneak out but-no problem, she's clueless.

He's a captain now. I don't think he's a hero or anything, but he looks pretty cool in his uniform. I got no problem with him - he's just a cool guy, no big thing.

Then I met his girlfriend, she's like five years older than me. Why don't these people love people their own age? I don't date twelve-year-olds. Dennis was 28. Marie said he could biologically be my dad. Yeah right, if [they had sex] when he was 11.

So my dad's been in some pretty mellow places so far-you know, Germany, Alaska. Now, I don't know, it might get a little weirder in . . . Afghanistan. So I'm gonna try not gettin' too attached. That's my thing with guys anyway. Never had a boyfriend for more than a day. Marie's different. She can't live without' em.

She cries. . .

(Beat.)

The whole thing's pretty weird, I admit it. The other day I'm in the cafeteria and this girl Lindsay comes up to me and she's like, "What're ya still bummed out for? He wasn't your real dad or anything."

(Beat.)

I beat the crap out of her.
```

---

## IC-0224: Nigger

- Title: Nigger
- Author (byline): Charlayne Woodard
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Jan 2003
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARLAYNE
- Teaser before the introduction: Yes
- Spoken words (computed): 1421
- Already set (do not supply): none

### Source block (context only)

```text
Author: Charlayne Woodard
ISBN: 978-0822219422
Publisher: Dramatists Play Service
Date (Month/Year): Jan 2003
```

### Introduction (context only: never use it for content warnings)

```text
The N-word is the word “nigger”, one of the three truly taboo words left in Standard English today. It means a black person but has behind it hundreds of years of white racist contempt, particularly when it comes out of the mouth of a white person. In this selection, I want to take you back to the 1960’s a time when de-segregation was in its infancy and a young African American girl experiences the word for the first time . . . . The words of wisdom from her mother do not excuse the racial intent behind the situation, but they do ring true for those of us who face small-minded people everywhere – based on the color of our skin, our gender, our sexual orientation or the myriad of differences that make our society unique. Stand strong, little “rabbit pellet.” Nigger by Charlayne Woodard.
```

### Performance text (classify this)

```text
"ABC Song" plays. Lights up on CHARLAYNE as she mimes jumping rope across the stage,

singing along with the music.

CHARLAYNE: " ... H-I-J-K-L-M-MINTO-P!" (Boasting.) I learned my ABC's in one night! Thanks to my Aunt Ruby, who gave me a big, beautifully illustrated ABC book, and thanks to my father, who taught them to me. One night, after dinner, Daddy said, "Charlayne, go get me that big pretty ABC book and meet me on the couch." (Moving loveseat stage left.) I did this. (Sitting on the loveseat:) I sat next to Daddy and he opened that big pretty book on both of our laps. He said "This is an A. This is a B. This is a C. This is a D. What is this, Charlayne?" (Daddy slaps her on the back of her hand. She's shocked.) "This is an A. This is a B. This is a C. This is a D. What is this, Charlayne?" "This is an A, this is a B, this' is a C, this is a D. Pay attention, Charlayne. What is this, Charlayne?"

"A?"
"Very good, Charlayne. And what is this?"
"B?"
"Very good, Charlayne. And what is this?"
"D?" (Slaps her hand, then more slaps for emphasis.)

This . . . went . . . on . . . all . . . night . . . long . . . until sunrise, when finally I could identify every letter of the alphabet, backwards, forwards, and out of sequence. Mommy was mortified, but Daddy was determined. My sister, Allie, had watched as much she could from underneath the coffee table in front of' us. Then she fell asleep and Mommy put her to bed late that night. The next morning at breakfast, Daddy said, "Allie, tonight you're gonna learn your ABC's." I teased her, I taunted her all day long. (Singsong.) "Allie's gonna learn her ABC's tonight! Allie's gonna learn her ABC's tonight!" Allie tried desperately to be brave. She said (feigning glee), "Hip, hip hooray! Hip, hip hooray!" That evening at dinner Allie hardly ate a thing. I wonder why .... After dinner, Daddy said, "Allie, go get that big, pretty ABC book and meet me on the couch." Allie took my place, right next to Daddy on the couch (sitting on loveseat) and I took her place right up under that coffee table. Daddy opened that big, pretty book on both of their laps. "This is an A, this is a B, this is a C, this is a D. What is this, Allie?" My sister wailed! My sister screamed! My sister wept crocodile tears! Then, she started peeing on the couch. (Standing.) "Get her off my couch, Woody!" Mommy screamed. "Get her off my couch!" Then Allie peed all over the living-room rug. Oooh! Mommy was furious ... but not with Allie. Oh no. "See what you did, Woody?! This is all your fault. You know . . . you know you can't put Allie under any pressure! (To Allie:) Mama's little baby Come on, Allie ... let Mama clean you up. Yes, yes It's all over, Allie.

(She glares at Daddy.) It's all over. So . . . when I entered kindergarten; I could already read. My sister Allie can't read to this day! Just kidding! But as a result of my reading ability, at the beginning of third grade, I was placed into an accelerated program. It was called the "AT." We were "academically talented!" So on the first day of school, instead of Mommy walking me and Allie up Second Street to School 6, she and Allie walked me down Second Street to the bus stop, where I'd catch the bus that was to take me all the way across town to my new school-School 20. At the bus stop my mother gave me a pep talk-of sorts. She said, "Charlayne, your job is to be smart. Your job is to do your schoolwork, do whatever your teacher tells you to do, and do it well. Now, the other kids in your class will probably have a lot of help from their parents, from their older sisters and brothers. You won't have any help. Your parents are working so hard to take care of this family, we are working round the clock to pay the bills, to give you and Allie a comfortable life. But you've got the right stuff to do this on your own, otherwise they wouldn't have chosen you. Yes?" (Thinking) "I'm gonna do it, Mommy!"

The bus came and my mother kissed me on my forehead. I boarded that bus (sitting on the loveseat, which is now the bus) and I waved to them. I waved to them until I couldn't see them anymore. I tell you, this "right stuff" was turning out to be a double-edged sword. While I was ready for the challenge, here I was being taken away from everything I knew and loved: my neighborhood, my friends, my school, and most of all, my Allie. Oh, but the difference between School 6 and School 20 was like night and day. First of all, there were only sixteen kids in my classroom! And they said it would stay this way until seventh grade. Second of all, Randy French and I were the only two negro kids in the whole school. But I looked forward to making new friends. And I did! Barbara O'Dooley, Linda Fraley, and myself, we were inseparable. I loved my teacher, Mrs. Rosenblatt. I loved all the work she gave me, and I put all my books and papers in a big red-plaid book bag that Daddy'd bought me for the first day of school. Oh ... ! One day at recess, some classmates and I were about to race across the schoolyard. Mrs. Rosenblatt stood way up at the finish line, with her arms outstretched. She yelled, "Get on your mark . . ." (CHARLA YNE gets into a starting position.) "Get set ... " Then I heard another voice ring out. (Singsong) "Run, nigger, run!" "Get set ... " (Singsong) "Run, nigger, run." This time I recognized the voice. It was Barbara O'Dooley . . . . Mrs. Rosenblatt yelled, "Charlayne, you've got to get on your mark!" And I told her, "I'm not running!"

Then Barbara yells out so everyone can hear, "Why not? My father said that all niggers. can run fast!" Well, Mrs. Rosenblatt did the running that day! She raced across that schoolyard, grabbed Barbara O'Dooley by the arm, and marched her up those stairs and into that classroom. No one had ever called me that name before! It felt as if somebody had come up behind me and punched me in my back. The other kids thought it was very funny. They were all laughing. It felt as if they were all calling me .... That day, for the first time since school started, I couldn't wait for that school bus to come and take me away from School 20. When I got home, my mother was working in the garden out by the peach tree. . (Angry to the point of tears;) .

"Mommy! Mommy, they called me a nigger today in school, Mommy! Barbara O'Dooley said, 'Run, nigger, run.'" My mother put down her tools, took off her gloves, she stood up, and she ... started laughing! She laughed and she laughed. She couldn't stop laughing! (Confused.) "Mommy! Please ... !" Finally, my mother collected herself. She looked around the yard. "Charlayne, what if I were to call you a ... rabbit pellet? (Singsong.) Run, rabbit pellet, run!" "No, Mommy! That's not what they said! They called me-" "Okay, what if I were to call you ... a stinkweed? Come on over here, stinkweed, and give Mama some sugar!" "Mommy, please, you're being silly!" "Yes. I am being silly. But if I'm silly enough to call you a stinkweed, does that make you a stinkweed . . . ? Huh . . . ? Are you a stinkweed?"

(CHARLAYNE takes this in.)

And then I looked around the yard. (Tentatively;) "You're a peach pit, Mommy!"

"And you're a rabbit pellet!"

(Circling the loveseat, which is now the peach tree, delighted.) "Peach pit!" "Rabbit pellet!" "Stinkweed!" "Froggy face!" My mother chased me round and round that peach tree as we called each other the most ridiculous names, until finally we just fell out on the grass (collapsing to the stage), exhausted. Then my mother crawled over to me. She said, "Charlayne, 'nigger' is just a word-a word that people purposely made up so they can sling it at us whenever they want to hurt us, whenever they want to stop us from doing what we should and being who we are. Now think. Why would Barbara want to hurt you?" "Because I was going to win that race ... ? Like I always do?" "Did you win?" "No, Mommy, I couldn't even run." "So . . . Barbara beat you today. And all because of that silly word." (Pause.) And then I understood. "Charlayne, if anybody wants to call you a rabbit pellet, you just let them . . . and secretly laugh to yourself: 'How silly they are!' Because you know you are not a rabbit pellet, you are not a stinkweed. . . ."

(CHARLA YNE stands with the realization;) "And, Mommy . .. I am not ... a nigger."
```

---

## IC-0225: Night Women

- Title: Night Women
- Author (byline): Edwidge Danticat
- Work: Krik? Krak!
- Publisher: Soho Press
- Publication date as stated: 1995
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1452
- Already set (do not supply): none

### Source block (context only)

```text
Author: Edwidge Danticat
Book: Krik? Krak!
ISBN: 978-1569470251
Publisher: Soho Press
Date (Month/Year): 1995
```

### Introduction (context only: never use it for content warnings)

```text
To what lengths would you go to provide for your child? What would you be willing to do . . . to sell . . . to make sure that he has a roof over his head, a warm meal to eat and a mother to love. Would you give your life, break the law, sell your soul . . . or your body? Perhaps adoption is not the ultimate sacrifice. Many labels have been used to describe mothers in positions such as this: ladies of the evening, street-walkers, hookers, whores or in Hati . . . Night Women by Edwin Danticat.
```

### Performance text (classify this)

```text
I cringe from the heat of the night on my face. I feel as bare as open flesh. Tonight I am much older than the twenty-five years that I have lived. The night is the time I dread most in my life. Yet, if I am to live, I must depend on it.

Shadows shrink and spread over the lace curtain as my son slips into bed. I watch as he stretches from a little boy into the broom-size of a man, his height mountaining the innocent fabric that splits our one-room house into two spaces, two mats, two worlds.

For a brief second, I almost mistake him for the ghost of his father, an old lover who disappeared with the night's shadows a long time ago. My son's bed stays nestled against the corner, far from the peeking jalousies. I watch as he digs furrows in the pillow with his head. He shifts his small body carefully so as not to crease his Sunday clothes. He wraps my long blood-red scarf around his neck, the one I wear myself during the day to tempt my suitors. I let him have it at night, so that he always has something of mine when my face is out of sight.

I watch his shadow resting still on the curtain. My eyes are drawn to him, like the stars peeking through the small holes in the roof that none of my suitors will fix for me, because they like to watch a scrap of the sky while lying with their naked backs on my mat.

A firefly buzzes around the room, finding him and not me. Perhaps it is a mosquito that has learned the gift of lightning itself. He always slaps the mosquitoes dead on his face without even waking. In the morning, he will have tiny blood spots on his forehead, as though he had spent the whole night kissing a woman with wide-open flesh wounds on her face.

In his sleep he squirms and groans as though he's already discovered that there is pleasure in touching himself. We have never talked about love. What would he need to know? Love is one of those lessons that you grow to learn, the way one learns that one shoe is made to fit a certain foot, lest it cause discomfort.

There are two kinds of women: day women and night women. I am stuck between the day and night in a golden amber bronze. My eyes are the color of dirt, almost copper if I am standing in the sun. I want to wear my matted tresses in braids as soon as I learn to do my whole head without numbing my arms.

Most nights I hear a slight whisper. My body freezes as I wonder how long it would take for him to cross the curtain and find me.

He says, "Mommy." I say, "Darling."

Somehow in the night, he always calls me in whispers. I hear the buzz of his transistor radio. It is shaped like a can of cola. One of my suitors gave it to him to plug into his ears so he can stay asleep while Mommy works.

There is a place in Ville Rosa where ghost women ride the crests of waves while brushing the stars out of their hair. There they woo strollers and leave the stars on the path for them. There are nights that I believe that those ghost women are with me. As much as I know that there are women who sit up through the night and undo patches of cloth that they have spent the whole day weaving. These women, they destroy their toil so that they will always have more to do. And as long as there's work, they will not have to lie next to the lifeless soul of a man whose scent still lingers in another woman's bed.

The way my son reacts to my lips stroking his cheeks decides for me if he's asleep. He is like a butterfly fluttering on a rock that stands out naked in the middle of a stream. Sometimes I see in the folds of his eyes a longing for something that's bigger than myself. We are like faraway lovers, lying to one another, under different moons.

When my smallest finger caresses the narrow cleft beneath his nose, sometimes his tongue slips out of his mouth and he licks my fingernail. He moans and turns away, perhaps thinking that this too is a part of the dream.

I whisper my mountain stories in his ear, stories of the ghost women and the stars in their hair. I tell him of the deadly snakes lying at one end of a rainbow and the hat full of gold lying at the other end. I tell him that if I cross a stream of glass-clear hibiscus, I can make myself a goddess. I blow on his long eyelashes to see if he's truly asleep. My fingers coil themselves into visions of birds on his nose. I want him to forget in a place where nothing lasts.

I know that sometimes he wonders why I take such painstaking care. Why do I draw half-moons on my sweaty forehead and spread crimson powders on the rise of my cheeks. We put on his ruffled Sunday suit and I tell him that we are expecting a sweet angel and where angels tread the hosts must be as beautiful as floating hibiscus.

In his sleep, his fingers tug his shirt ruffles loose. He licks his lips from the last piece of sugar candy stolen from my purse.

No more, no more, or your teeth will turn black. I have forgotten to make him brush the mint leaves against his teeth. He does not know that one day a woman like his mother may judge him by the whiteness of his teeth.

It doesn't take long before he is snoring softly. I listen for the shy laughter of his most pleasant dreams. Dreams of angels skipping over his head and occasionally resting their pink heels on his nose.

I hear him humming a song. One of the madrigals they still teach children on very hot afternoons in public schools. Kompe Jako, dome vous? Brother Jacques, are you asleep?

The hibiscus rustles in the night outside. I sing along to help him sink deeper into his sleep. I apply another layer of the Egyptian rouge to my cheeks. There are some sparkles in the powder, which make it easier for my visitor to find me in the dark.

Emmanuel will come tonight. He is a doctor who likes big buttocks on women, but my small ones will do. He comes on Tuesdays and Saturdays. He arrives bearing flowers as though he's come to court me. Tonight he brings me bougainvillea. It is always a surprise.

"How is your wife?" I ask.

"Not as beautiful as you."

On Mondays and Thursdays, it is an accordion player named Alexandre. He likes to make the sound of the accordion with his mouth in my ear. The rest of the night, he spends with his breadfruit head rocking on my belly button.

Should my son wake up I have prepared my fabrication. One day, he will grow too old to be told that a wandering man is a mirage and that naked flesh is a dream. I will tell him that his father has come, that an angel brought him back from Heaven for a while.

The stars slowly slip away from the hole in the roof as the doctor sinks deeper and deeper beneath my body. He throbs and pants. I cover his mouth to keep him from screaming. I see his wife's face in the beads of sweat marching down his chin. He leaves with his body soaking from the dew of our flesh. He calls me an avalanche, a waterfall, when he is satisfied.

After he leaves at dawn, I sit outside and smoke a dry tobacco leaf. I watch the piece-worker women march one another to the open market half a day's walk from where they live. I thank the stars that at least I have the days to myself.

When I walk back into the house, I hear the rise and fall of my son's breath. Quickly, I lean my face against his lips to feel the calming heat from his mouth.

"Mommy, have I missed the angels again?" he whispers softly while reaching for my neck.

I slip into the bed next to him and rock him back to sleep. "Darling, the angels have themselves a lifetime to come to us."
```

---

## IC-0226: Nuts

- Title: Nuts
- Author (byline): Tom Topor
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: June 1981
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MACMILLAN, CLAUDIA, JUDGE, LAWYER, RECORDER
- Teaser before the introduction: Yes
- Spoken words (computed): 1226
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tom Topor
ISBN: 978-0573613258
Publisher: Samuel French, Inc.
Date (Month/Year): June 1981
```

### Introduction (context only: never use it for content warnings)

```text
Claudia Draper is a white, upper middle-class white woman living in New York. She seems completely put together. Until she’s not. Claudia, in an effort to live on her own terms after her marriage ends, seeks unorthodox methods. Some would call it prostitution, she would call it gifts. However, after one of her clients is found dead, Claudia is charged with manslaughter. Her parents ask that she be committed to Bellevue, a hospital for the criminally insane. But Claudia has other plans. She wants autonomy. She wants to take responsibility for her choices. And she doesn’t want to be labeled Nuts by Tom Topor.
```

### Performance text (classify this)

```text
MACMILLAN: (Pg 11) (Rises, crosses to Judge’s bench) The defendant has been indicted in the county of New York for manslaughter in the first degree. People asked that the defendant be given a psychiatric evaluation to determine whether she had the capacity to stand trial. This is in accordance with Article seven-three-oh of the Criminal Procedure Law. The results of that evaluation were submitted to the court, and the two examining psychiatrists found that the defendant did not have the capacity to stand trial. The defendant filed a motion for a hearing to challenge and this procedure is that hearing. (Pg 64) Mrs. Draper, do you understand the charge against you?

CLAUDIA: Yes, I do.

CLAUDIA: (Pg 64) First degree manslaughter is a Class B felony--intent to cause serious physical injury to another person, causing the death of such person. (pg 66- 67) [And] if I lose today, they can lock me up in a hospital for the criminally insane, and they don’t ever have to let me have a trial.

MACMILLAN: (pg 68-70) Mrs. Draper, do you believe that you’re physically and mentally prepared to go on trial?

CLAUDIA: Yes, I do.

MACMILLAN: Mrs. Draper, how long were you married?

CLAUDIA: Nearly 10 years. Six weeks short of 10 years . . . It had its moments. [And] I love him . . . Loved him. No, I still love him. (beat) He found another woman so he could leave me. Actually, he left long before he left. A couple of years later, [his] body follow[ed him] out the door.

MACMILLAN: And you moved to a place that you could afford – where is that, Mrs. Draper? (Crosses down right)

CLAUDIA: First Avenue and 55th. (Pg 72) [I was making] a hundred a week from Peter and $75 a week from a part-time job at NYU. (pg 73) [I lived on] gifts. [From] friends. [Men] friends. (Pg 74-75) (to Judge) Is it legal to take cash gifts? If I say to you, here’s $100 just because I like you – is that legal?

JUDGE: Yes, that’s legal.

CLAUDIA: A lot of the gifts were cash.

MACMILLAN: And these cash gifts from these men friends – these cash gifts of more than $50? – were enough to pay your expenses.

CLAUDIA: All of them. And tuition at NYU Law School.

LAWYER: And what did these men expect in return for these “gifts”?

CLAUDIA: Friendship.

MACMILLAN: You talked to them? You listened to them? You did them favors? What kind of favors did you do in return for these gifts?

CLAUDIA: (Pg 76) It works like this: you call me first, we make a date. I look you over and if I like you, we make a deal. Half the cash in front, half when you leave. (Pause) Darlin’ I am worth the trouble, take my word for it. (Pg 77-78) [I lived on my own terms for] one hundred and fifty-two days. Five months.

MACMILLAN: At any time during these five months, did you ask your husband [or] your parents for money? Did you believe they would have refused to lend or give you money?

CLAUDIA: They would have given it to me. [But] it hurts less to sell your ass to strangers. (Pause) I don’t know which price is higher--either way, you pay and you pay. (Looks at her mother) -- If you ever want to listen, Mama, I can try to explain it. (Back to the lawyer) (Pg 82-83) She loves me. (Pause) When I was a little girl, I used to say to her, I love you to the moon and back again; and she used to say to me, I love you to the sun and down again and around the stars and back again. (Looks at her mother) Do you remember, Mama? (Back to the lawyer) And I used to think, wow, I love Mama, and Mama loves me and what can go wrong? (Pause) What went wrong, Mama? You see, I know she loves me and I know I love her, and--so what? So what? She’s over there and I’m over here, and she hates me because of things I’ve done to her, and I hate her because of the things she’s done to me. You stand up there asking, do you love your daughter and they say ‘yes’, and you think you’ve asked something real. You think that because you toss the word love around like a frisbee we’re all going to get warm and runny. No. Something happens with some people: they love you so much they stop noticing you’re there because they’re so busy loving you. They love you so much, their love is a gun, and they keep firing it straight into your head. They love you so much you go right into a hospital. Yes, I know she loves me. (Looks at her mother) Mama, I know you love me. And I know the one thing you learn when you grow up is that love is not enough. It’s too much and it’s not enough.

MACMILLAN: (Crosses left) Let me see if I understand you correctly, Mrs. Draper. You believe that everyone in this courtroom either wants to hurt you or will hurt you?

CLAUDIA: (Pg 83) All of you can, some of you will. (Pg 82) I don’t trust people who can hurt me; not anymore. (Pg 79) Your job is to put me in a hospital. I don’t know; I guess I’m dumb. I take that personally. (Pg 78) [You tell me I’m] a nice girl and [I] don’t belong here. (Pg 79) Whores aren’t nice white girls from nice white families. Whores are girls who hang out on Eighth Avenue and stick needles in their arms. (Pause) But what if you’re wrong? (Pg 84-85) While you’re playing with your rules, the meter is running out on my goddamn life. Can’t you get that I understand you want to help, and I don’t want your help? I know the price of your help. I know I’m supposed to be a good little girl for my mother and father, and an obedient and faithful wife to my husband, (Crosses down) and stick out my tongue for the doctor and lower my head for the judge. I know all that, I know what you expect me to do. Look, I am not just a picture in your heads. I am not just a daughter, or a wife, or a hooker, or a patient, or a defendant. Can’t you get that? You don’t understand the things I do, but I do have my reasons. They’re not your reasons, so they’re not real to you, but they’re real to me. And that’s enough. (Crosses up and looks at her mother) I know women who peddle their daughters to hang on to their husbands, so don’t judge [me]. I knew what I was doing every goddamn minute. And I am responsible for it. I lift my skirt, I am responsible; I go down on my knees, I am responsible. If I play the part you want me to play, if I play sick, I won’t be responsible. Poor, dumb sick Claudia, she’s not responsible, the poor sick things, she needs our help. I won’t play that part. I won’t give you that out. I won’t be another picture in your heads, Claudia the nut; I won’t be nuts for you? Do you get what I’m telling you? (She is near hysteria. She wipes her mouth on her sleeve and takes a step back) [The judge] can sign a piece of paper saying I’m nuts, but it’s only a piece of paper and I’m not something on a piece of paper. And no matter how many times you sign it; no matter how many times you say it, you can’t make me nuts. Get it straight, I won’t be nuts for you.

RECORDER: (Pg 88) On June 15th, 1979, Claudia Faith Draper was tried in the State Supreme Court, New York County, on a charge of manslaughter in the first degree. She was acquitted.
```

---

## IC-0227: On the Basis of Sex - Screenplay

- Title: On the Basis of Sex - Screenplay
- Author (byline): Daniel Stiepleman
- Work: Not specified
- Publisher: Scriptfly.com
- Publication date as stated: Aug 2013
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BROWN, GRISWOLD, BOZARTH, COURT CLERK, JUDGE HOLLOWAY, RBG, JUDGE DOYLE, JUDGE DAUGHERTY, VOICE OVER
- Teaser before the introduction: Yes
- Spoken words (computed): 1487
- Already set (do not supply): none

### Source block (context only)

```text
Author: Daniel Stiepleman
ISBN: N/A
Publisher: Scriptfly.com
Date (Month/Year): Aug 2013
* Hoyt v. Florida - Nov 20, 1961
https://www.oyez.org/cases/1961/31
Facts of the case
A Florida statute automatically exempted women from jury duty and did not place women on
jury lists. Women could, however, volunteer and register for jury duty. After an all-male jury
convicted Mrs. Hoyt for murdering her husband, she appealed the decision to the Florida
Supreme Court. The Florida Court upheld the conviction.
Conclusion
In a unanimous decision, the Court held that the statute was based on a reasonable
classification and was therefore constitutional. Noting that women were "still regarded as the
center of home and family life," the Court found that the states could relieve them from the
civic responsibility of jury duty unless they themselves determined that such service was
consistent with their own "special responsibilities." The Court held that the case was distinct
from other cases involving racial discrimination in jury selection, and that male-female
disproportions on jury lists carried no constitutional significance.
```

### Introduction (context only: never use it for content warnings)

```text
Ruth Bader Ginsburg was born in 1933 in Brooklyn, New York. The Notorious RBG, as she came to be known, was an outspoken champion of civil rights, especially as an advocate for women’s rights and gender equality, Ginsburg left an indelible mark on our country and our lives with her legal arguments, steadfast support of civil rights, and, of course, her words.

She was once asked, “When will there be enough women on the Supreme Court.” Her answer? “When there are nine.” People were shocked, but she replied. “There’s been nine men, and nobody’s ever raised a question about that.”

The year is 1971. This is the 1st gender-discrimination suit RBG argued in court; and it launched her legal and judicial career. And it was the first time a provision of the Internal Revenue Code had been declared unconstitutional . . .

On the Basis of Sex by Daniel Stiepleman
```

### Performance text (classify this)

```text
A preparation session by the defense prior to the court date . . .

BROWN: (Pg 80) Paint the judges a picture of the America that will exist if they rule the wrong way. Children running home from school to find . . . No one’s there. Mommy’s at the office. Or on a factory floor.

GRISWOLD: If a man and woman vie for the same job, she can work for less. What is a man without a paycheck to take care of his family?

BROWN: What woman would want him?

BOZARTH: Wages go down. Divorce rates soar. Society unravels.

BROWN: Exactly! (to Bozarth) The other side wants this to be about the Equal Protection Principle. You need to show that what’s really at stake is the American family.

GRISWOLD: What the judges are deciding is what kind of society they want their children and grandchildren to grow up in.

BOZARTH: (Pg 75) We list the laws. Every federal law that treats men and women differently so the Court sees exactly the can of worms these folks are . . . (fades out)

COURT CLERK: (Pg 102-103) All rise. The United States Court of Appeals for the 10th Circuit is now in session. Judges Doyle, Holloway, and Daugherty presiding.

JUDGE HOLLOWAY: The first case is docket number 711127. Charles Moritz v Commissioner of Internal Revenue.

JUDGE HOLLOWAY: (Pg 103) Counsel for the appellant you may proceed.

RBG: (Pg 106-117) (adjusts the microphone down) Your Honors and may it please the court. Section 214 denies Mr. Moritz a caregiver tax deduction available to similarly situated women who . . .

JUDGE HOLLOWAY: (interrupting and condescending) Mrs. Ginsburg. You are aware that the government has three co-equal branches?

RBG: Yes. Of course, Judge.

JUDGE HOLLOWAY: And that it is the Congress’s role to write law.

RBG: (sharply) Your Honor, I understand how government works.

JUDGE HOLLOWAY: (unaccustomed to being addressed impatiently) Well sometimes a law, even a law that is legal under the constitution, may not be good for every individual.

JUDGE DOYLE: I have a question. If I understand correctly, you’re concerned about men and women being pigeon-holed into certain roles based on gender.

RBG: Yes. That’s correct. Because –

JUDGE DOYLE: (sharply) Excuse me. That wasn’t my question. (Ruth shrinks) It strikes me that the caregiver deduction does the opposite. It helps women be able to work outside the home. Isn’t that a good thing?

RBG: But the law assumes it must be women who are supposed to stay at home in the first place.

JUDGE DOYLE: So it’s the assumption that’s the problem?

JUDGE DAUGHERTY: Then when can a law differentiate on the basis of sex? Never?

JUDGE HOLLOWAY: Keeping women out of combat, for example.

RBG: I’m not sure whether I agree with that example, but-

JUDGE DAUGHERTY: So you think women belong on the front lines now, too?

RBG: No. That’s not what . . (takes a deep breath, composing herself) Gender. Like Race. Is a biological, unalterable trait. There is nothing that women are inherently better at than men. Nor vice versa.

JUDGE HOLLOWAY: Growing a beard? (laughs)

JUDGE DAUGHERTY: Lactation. (more laughter)

RBG: (visually frustrated) No thinking person can possibly believe Charles Moritz’s gender relates to his ability to-

JUDGE DOYLE: (interrupting) Why can’t we, Mrs. Ginsburg? In most households, aren’t women the primary caregivers? Aren’t men the breadwinners? Doesn’t that reality suggest that it’s the natural order of things? (waves Ruth to her seat dismissively)

JUDGE HOLLOWAY: Mr. Bozarth for the appellee. You may proceed.

BOZARTH: (steps to the podium) Your Honors and may it please the court. Congress created this tax deduction to help caregivers go out and work. Folks that, if they weren’t working, would stay home. Are we meant to believe that this man would have the skills or the . . . caregiver’s instinct to do that? Widowers don’t choose to be caregivers, Judge Doyle. It’s thrust upon them. As for women. . . It doesn’t take a legal treatise to prove what a hundred thousand years of human history makes clear.

Y’honors, I’m certain there isn’t a man amongst us who wouldn’t try to ease his wife’s burdens. There is a long and honorable tradition in the Courts of supporting laws like this one. I for one would rather see my government err on the side of trying too hard to help the ladies of this country. Rather than be indifferent to their unique burdens. Now maybe Mr. Moritz disagrees. Or maybe he simply doesn’t like paying taxes. Personally, I don’t believe that. I believe Charles Moritz is a victim. Not of his government. But of lawyers who used his case to achieve their own ends -- Radical. Social. Change. We rest our case on our briefs and argument and ask that the Court uphold the Tax Court’s decision. (he sits)

JUDGE HOLLOWAY: Counsel for the appellant. You have rebuttal.

RBG: (Leaving her notes behind, Ruth approaches the podium with fiery determination) Radical social change. (sardonic laugh) When I was in law school, there was no women’s bathroom. It’s amazing to me now, but we never complained. Not because we were timid. We were just astounded that we were in law school at all.

A hundred years ago, Myra Bradwell wanted to be a lawyer. She had fulfilled the requirements for the Illinois bar but wasn’t allowed to practice because she was a woman. An injustice she asked the Supreme Court to correct. Illinois was so confident of victory, they didn’t even send a lawyer to argue their side. They were right. She lost. (this is a different Ruth. She’s confident, compelling) That was the first time someone went to court to challenge his or her prescribed gender role. A hundred years ago. Radical social change?

(clutches the podium) Sixty-five years ago. When women in Oregon wanted to work overtime, and make more money, as men could, the Court looked to the precedent in Bradwell. And said no. And then there were two precedents. Then three. Then four. And on. And on. You can draw a direct line from Myra Bradwell to Gwendolyn Hoyt - told ten years ago she was not entitled to a jury of her peers.*

(she looks the Judges directly in the eyes) That is the legacy the Government asks you to uphold today. You are being urged to protect the culture and traditions and morality of an America that no longer exists. A generation ago, my students would have been arrested for indecency wearing the clothes that they do. Sixty-five years ago, it would have been unimaginable that my daughter would aspire to a career. And a hundred years ago. I would not have had the right to stand before you.

(presses her fingers into the podium for emphasis) We are not asking you to change the country. That’s already happened without any Court’s permission. We are asking you to protect the right of the country to change. There are a hundred and seventy-eight federal laws that differentiate on the basis of sex. Count them. The Government did the favor of compiling them for you. And while you’re at it, I urge you to read them. They are obstacles to our children’s aspirations.

JUDGE DOYLE: You’re asking us to overturn nearly a century of precedent. She looks him dead in the eye. Without hesitation.

RBG: I’m asking you to set a new precedent -- As courts have done before when the law is outdated.

JUDGE DOYLE: But in those cases the courts had a clear constitutional handle. The word ‘woman’ doesn’t appear even once in the U.S. Constitution.

RBG: Nor does the word ‘freedom.’ Your honor. (Doyle looks down on her for a long time. And she returns his gaze – unflinchingly) Our sons and daughters are barred by law from opportunities based on assumptions about their abilities. How will they ever disprove these assumptions, if laws like Section 214 are allowed to stand? That is why we must take these laws on. One-by-one. For as long as it takes. You have the power to set the precedent that will get us started. You can right this wrong. The principal purpose of Section 214 is not to protect women nor to discriminate against men. It is to provide caregivers the opportunity to work outside the home. Therefore, this court should fix the law in the way most in line with the legislative intent. Extend the deduction to never-married men. Help all caregivers equally.

(she should be done. She knows that. But she lets herself linger a moment more. And no one stops her) Our client, Charles Moritz, was well raised to be the sort of man we should all hope our sons will become. He deserves our admiration. Not only has he accepted the burden of caring for his mother -- when no one would expect it of him. But in doing so, he has surpassed the limitations the rest of us -- and our laws -- try to force upon him. We rest our case on our briefs and argument and ask that you reverse the Tax Court’s decision. (Ruth returns to her seat)

VOICE OVER: (Pg 119-120) That case: Moritz v Commissioner was the first U.S. federal case to find laws unconstitutional for discriminating on the basis of sex.

RBG: (Pg 94) You don’t get to tell me when to quit.

VOICE OVER: (Pg 119-120) As Director of the ACLU’s Women’s Rights Project, Ruth Bader Ginsburg became the leading gender rights lawyer of her generation, winning several landmark cases before the U.S. Supreme Court.

RBG: (Pg 95/86) Have you seen Appendix E from the Government’s brief Laws written by men who think we’re privileged to be excused from men’s obligations. It’s not a privilege. It’s a cage. These laws are the bars. That entire comprehensive list of laws that differentiate between the sexes? We turn it into our own hit list.

VOICE OVER: (Pg 119-120) On June 14, 1993, President Bill Clinton nominated Ruth Bader Ginsburg to the U.S. Supreme Court.

RBG: (Pg 63) A court ought not be affected by the weather of the day. But will be by the climate of the era.

VOICE OVER: (Pg 119-120) On August 3, 1993, the Senate confirmed her nomination: 96-3.
```

---

## IC-0228: One Small Boat

- Title: One Small Boat
- Author (byline): Kathy Harrison
- Work: Not specified
- Publisher: Tarcher
- Publication date as stated: April 2006
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: KATHY, SOCIAL WORKER, DAISY, SOCIAL WORK, GLENNA, EVELYN, BRUCE
- Teaser before the introduction: Yes
- Spoken words (computed): 2694
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kathy Harrison
ISBN: 978-1585424658
Publisher: Tarcher
Date (Month/Year): April 2006
```

### Introduction (context only: never use it for content warnings)

```text
Daisy was five when she first entered Harrison’s bustling household. Mother of three children by birth, three by adoption and a handful of foster kids always coming and going, Harrison had ten children under her roof at any given time. But Daisy was unique. Daisy’s birth mother wasn’t poor, uneducated, or drug addicted. She just could not take care of a child, and the effects of this abandonment on Daisy were heart-wrenching. Fear and anxiety marked her every move. After two weeks in Kathy’s loving home, however, Daisy began to thrive. One Small Boat by Kathy Harrison.
```

### Performance text (classify this)

```text
KATHY: (Pg 15-16) I am fascinated by the myriad ways traumatized children learn to cope within a world that makes no sense. What looks like crazy can be the sanest thing imaginable when you know how a child has lived. I took care of kids with broken bones and cigarette burns. My children had police records and venereal disease. But my kids had other things. I have known young children willing to sacrifice their own safety in order to protect younger brothers and sisters. It made me glad every day that I had found the courage for the gritty reality of foster parenting.

SOCIAL WORKER: (PG 18-25) . . . Anyway, Tiffany is adorable. She has no special needs and no medical issues. I also have 10-year-old Carmen Santiago. Her mom just got sentenced to three months in jail. Carmen has hearing aids, but no other special needs. Then I’ve got Daisy, but I think we may need to find a hotline bed for her this weekend and look for a specialized slot next week.

KATHY: Why? What’s up with her?

SOCIAL WORKER: Only six but two prior psych hospitalizations. Anorexic. Aggressive toward her mother. Very little speech. Maybe retarded. Very depressed. She’s on a ton of medication.

KATHY: (to audience) The handwriting was on the wall for Daisy. She was headed for a residential treatment program somewhere.

SOCIAL WORKER: Hey! Are you still there?

KATHY: Sorry. (Chuckle) I’m just thinking. Tiffany and Carmen sound like they’ll be easy to place, so I guess I’d like to take Daisy. (to audience) When Daisy arrived on Saturday afternoon, she didn’t walk in the front door. She scuttled. Like a small crab, she sidled away from me, making only brief eye contact and refusing to respond. She flitted from one piece of furniture, one toy, one book to the next, examining each only briefly before moving on. Nothing held her attention for more than a moment until she spied our cat, Molly.

DAISY: (squealing and grabbing the cat, clutching her too tightly around the stomach)

KATHY: Molly struggled to get loose, but Daisy seemed oblivious of the cat’s discomfort. (To Daisy, coming down to her level) Molly doesn’t like to be held so tightly, honey. It hurts her. Put her down and pet her gently. Like this. (To audience and in pantomime) Daisy let me take Molly from her and even let me run her hand gently over the cat’s rumpled fur. (To Daisy) There you go. Molly will like you if you’re kind to her. (to audience) I took the few minutes that Daisy spent stroking Molly to get a better look at her. What struck me was how unwell she looked. Her dark hair was so thin and wispy that in places her scalp showed through. There was not an ounce of fat on her emaciated body. Thin ribbons of green mucus ran from her nose. Dark eyes were sunk deep in her skull.

SOCIAL WORKER: I’m sorry to do this to you, Kathy. Do you think you can get through the weekend?

KATHY: That shouldn’t be a problem. She looks too sick to be dangerous. What the heck is going on with this kid? I know she has some food issues, and I was told she doesn’t talk. I suppose she’s been checked out medically.

SOCIAL WORK: Every test known to man. We have a long list of what she doesn’t have, but no idea about what she does have, besides a laundry list of psychiatric problems: ADHD, Multiple phobias, Oppositional defiant disorder. Daisy’s mom, Glenna, gave me the meds and a schedule of when they need to be given.

KATHY: The directions were filled with qualifiers like, “If she’ll take it,” “If she seems to need it. (To Social Worker) I can’t do this, Evelyn. It’s not safe. It looks like she hasn’t had any of this stuff consistently for the last couple of weeks. (To audience) Medicating children for what often seems like pretty good adaptive responses to a crummy home life annoys me. Shouldn’t calm and predictable reactions to challenging behavior be the first line of treatment for an oppositional kid, or is it just easier on everyone to slip him a pill? . . . (pg 27-30) I was glad to have Evelyn leave so I could return to Daisy. . . I took both of her thin hands in mine. (To Daisy) Your nose is running, hon. Let’s wash your face, Okay? (to audience) I led Daisy to the bathroom and gently cleaned her face with a soft washcloth. Daisy flinched when I got near her face, a small movement that made me cringe. I knelt down to look at her and held up a hand mirror so she could see herself. Daisy looked at her image for a long time and then smiled. (To Daisy) You look so pretty, Daisy. Let’s put some tissue in your pocket. When your nose runs, you can wipe it with that instead of your hand. Okay? (to audience) Daisy nodded. She started to spin and flap her hands. I stood behind her, wrapped my arms around her bony frame, and whispered in her ear. (To Daisy) Take a deep breath, sweetie. Hey, did you know that I have the best job in the whole world? My job is to keep kids safe. I get to make sure things aren’t so scary. Bad things won’t happen to you here. Okay? TRANSITION And things progressed nicely for a few days . . . until Daisy’s mother, Glenna requested a home visit to see if our house met her standards.

GLENNA: (Pg 43-46) Oh, my God, I am so happy to meet you. You must be a saint or something, taking in a kid like Daisy.

KATHY: I had done my best to spiff [Daisy] up for the occasion. She was nicely dressed and her nose was wiped. It had taken a couple of days for Daisy’s psychiatrist to get back to me, and by that time it was pretty clear that Daisy could function without medication. While I couldn’t be sure that was the whole reason, Daisy looked less spacey than she had when she arrived. I think I held some hope that Glenna would see Daisy differently and consider taking her only child home. She took some effort, especially around meals, but I had rarely seen a child as anxious to please as this one. I hated to see Daisy go, but I just couldn’t come up with a reasons for her to be in foster care. I called her down. [Daisy . . . Daisy . . . can you come downstairs for a minute, please]

DAISY: [hopping into the living room, then stops dead when she sees her mother; a stricken look on her face]

GLENNA: [recited as if she has practiced this in front of a mirror] Daisy! Baby! I’ve missed you. Come give Mommy a hug.

DAISY: [a worried expression on her face] Hi, Mommy. You comin to get me? I goin home? [slowly begin to rock and flap her hands, whispering a count of one to ten]

KATHY: (Pg 47-51) Daisy began a pattern I was beginning to recognize, rocking rapidly back and forth, flapping her hands, and chanting from one to ten, over and over, all in a futile effort to wrest some control from her chaotic world.

EVELYN: Why don’t you have Kathy and Daisy show you her room, Glenna?

KATHY: Her eyes widened when she saw four beds in Daisy’s room.

GLENNA: Daisy’s used to having her own space. I’m not sure she should be sharing with other kids. Is there any way that could happen?

KATHY: [evenly] I’m afraid not, Glenna. Kids lose a lot when they come into foster care. Not just their families but their houses and schools and pets and friends. It’s hard on kids, but most of them adapt to the physical changes pretty quickly. Daisy is doing just fine. (to audience) Emotionally, this little girl had been hit by a truck, and the best her mother could come up with was to worry about her accommodations. . . Daisy fell apart. It wasn’t a gradual fall. It was a dramatic crash.

DAISY: [flapping and spinning at a rapid rate, pulling on her mother, yapping like a small puppy]

KATHY: For the first time since her arrival, I saw the hyperactivity and bizarre behavior that had been reported. The wilder Daisy got, the more anxious Glenna became.

GLENNA: [pleading] (*NOTE – The following words are not in the text . . . Daisy, baby, settle down now . . . please, Daisy.)

KATHY: The hesitancy and uncertainty in her voice was not lost on Daisy, who responded with a maniacal laugh. (Daisy laughs) I was reluctant to intervene, and I might not have had Daisy not begun pounding on Glenna’s back. It needed to stop. (in pantomime and in words) I caught Daisy from behind, wrapping my arms around her thing frame and dropping to the floor. (To Daisy firmly) Daisy, you need to stop. Can you do that by yourself, or do you need me to help you?

DAISY: (breath coming in quick, shallow gulps, panicked she speaks softly) Help.

KATHY: All right. I want you to take some deep breaths like I showed you. When you calm down, I want you to get the clay out of the art box. I want you to sit at the table and play with it until I come. Can you do that? (to audience) After a moment, Daisy nodded. I relaxed my grip and helped her up. She didn’t attempt to speak to her mother, but did as I asked, defeated.

EVELYN: Is, uh, that pretty typical behavior for Daisy?

GLENNA: Pretty much. Sometimes it’s a lot worse. You can see why I can’t take care of her. She just get out of control, and I don’t know what to do with her. I thought the hospital would help, but they seemed to think everything was my fault. Like making me take a parenting class is going to change Daisy. TRANSITION – a few months pass

KATHY: (Pg 92-93) What’s up, sweetie? Are you okay?

DAISY: I okay. Is I going home soon?

KATHY: I don’t know, Daisy, do you want to go home?

DAISY: I miss my mom sometimes, but I be a bad girl at her house. That’s why her don’t like me. She thinks I weird.

KATHY: Sometimes grown-ups have so many of their own worries to think about that they don’t have a lot left over to give to other people, even their own kids. I know your mom cares about you. I think she wants you to be happy, but she doesn’t know how to help you. (Phone rings and Kathy answers) (Pg 138-139)

EVELYN: Hey, Kathy, it’s Evelyn. Are you sitting down? Glenna just called. She is rescinding the voluntary. She would like to have Daisy packed and ready to leave on Friday.

KATHY: Can she do that? Just call and say she wants her back?

EVELYN: It’s been voluntary all along, Kathy. She can do anything she wants.

KATHY: Did I do something? Isn’t she happy with Daisy’s care?

EVELYN: Actually, I think she may be too happy with Daisy’s care. I think she would be happier if Daisy seemed a little more homesick. You’re a tough act to follow for a mother who isn’t exactly June Cleaver.

KATHY: Give me a break. So this is it. She’s done being overwhelmed and wants to be a mommy again, and we say good-bye and you bring me another kid.

EVELYN: That’s kind of the way it works, Kathy. This is foster care. Isn’t supposed to last forever because you fall in love with a kid.

KATHY: (to audience) Of course she needed to go home. It really should have happened a long time ago. Daisy had been with us for seven months.

EVELYN: Life goes on. There will be another kid, Kathy.

KATHY: There won’t be another Daisy . . . (Pg 143-150) Evelyn was right, of course. Life did go on, but the grief didn’t go away. If anything, it got worse, intensified because I had no way to check on Daisy. Two weeks went by without a word from Glenna. I called a few times, but always got the machine and my messages went unanswered. Let it go, I reminded myself over and over. You gave her what you had to give and it’s time to move on . . . and then [my phone] rang in the parking lot of the supermarket. (answering) Hello?

BRUCE: Are you coming right home after shopping?

KATHY: Is something wrong?

BRUCE: I guess that depends on your perspective. I got a call from the hotline. They just picked Daisy up at the hospital. They want to know if we’ll take her.

KATHY: What happened?

BRUCE: Her mom brought her into the emergency room. She said Daisy was out of control. I guess Daisy was hitting Glenna and climbing all over the furniture, like a madwoman.

KATHY: How did Glenna get her to the hospital?

BRUCE: In an ambulance, if you can believe it.

KATHY: (To audience) My poor Daisy, afraid of both hospitals and sirens. Fear alone would have made her look crazy by the time she got to the emergency room. . . What was I expecting when I heard the car pull into the driveway? I expected to see what I was feeling – disorganized, confused, fearful. The car had barely stopped before Daisy was out. She didn’t just run up the driveway. She flew, straight into my arms. (To Daisy) Hey, kiddo! Welcome home! I have been missing you!

DAISY: Why didn’t you never call me? You said you would. My mom said you were too busy with new kids to call me.

KATHY: (to audience) She looked terrible. She looked nearly as bad as she had when she arrived the previous winter. (To Daisy) Was I ever too busy for you, Daisy. (to audience) People wonder, I know. They think I must be crazy to choose to spend my days with kids like these: kids who smell bad and eat with their hands and tell us things we would rather not know. But I have moment like this and then I remember why I’m here. (Pg 152-153) (to Daisy) Pretty rough day, huh, Daisy? Do you want to talk about it?

DAISY: My mommy got very, very mad at me. She yelled at me and called the peoples to take me away.

KATHY: Any idea why she was so mad?

DAISY: Cause I hitted her with my slipper

KATHY: You must have been pretty mad. What do you think made you so mad at your mom? (To audience) The pause that followed my question was so long that I though Daisy was not going to answer.

DAISY: (taking a deep breath) He hurted me, you know. He hurted me every day, and she never told him to stop. Why didn’t she never come when I called her.

KATHY: (to audience) I assumed Daisy was talking about her mom’s old boyfriend, Frank. (to Daisy) Your mommy was home when Frank hurt you?

DAISY: I think she home.

KATHY: It must have made you pretty mad when that was happening, Daisy. I bet I would have felt like hitting her, too. But I think you may be wrong about this. I think your mom didn’t know what Frank was doing. As soon as she knew, she made him leave. And she sent you here so you would be safe. (to audience) Please, God, let me be right about that. Let it be true that she really didn’t know. Daisy and I talked for a while longer. She gave me details I didn’t want to know. It took every ounce of self-control I could muster to listen and respond without letting the disgust I felt come through . . . (Pg 171) Sexual abuse is a terrible thing to happen to a child. It is far worse than a beating. It brings with it shame as well as violation, and I know of few children able to believe they are not somehow at fault.

DAISY: (pg 193) Sometimes . . . Sometimes I wish you was my mom and I never had to move. I just want this to be home.

KATHY: (pg 200) This is a crazy life. (pg xviii) Every day more than seven hundred children come into care because of suspected abuse or neglect. One-third will never go home to their original families again. One-third who do go home will be back in care again before they reach adulthood. There are more than 550,000 children in the child welfare system in this country. Its enormity excuses our tendency to forget that these are not numbers but real little people. Little people who (page 200-201) tell me things that are so sad and so awful I can digest only small pieces at a time . . . [but] Sometimes there are really good days. Sometimes a mother will show up for a visit, and I can feel the love between her and this kid. She’s clean and sober, and she’s finished her parenting course. She’s getting her daughter back, and I feel like I had a small part in this wonderful thing. This is fostering life. (pg xix) Daisy? Daisy was a teacher. She taught me about strength and courage and resiliency. I also learned about loving and losing and that happy endings are often what we make for ourselves.
```

---

## IC-0229: The Orange

- Title: The Orange
- Author (byline): Joyce Carol Oates
- Work: 12 Plays, Pgs 300-303
- Publisher: Plume
- Publication date as stated: Nov 1991
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: GIRL
- Teaser before the introduction: Yes
- Spoken words (computed): 1329
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joyce Carol Oates
Book: 12 Plays, Pgs 300-303
ISBN: 978-0452267015
Publisher: Plume
Date (Month/Year): Nov 1991
```

### Introduction (context only: never use it for content warnings)

```text
In the United States today, anorexia often hides in plain sight behind discipline, perfectionism, and the quiet praise of “self-control. What begins as a simple diet can evolve into a dangerous illness, one that the National Eating Disorders Association says impacts millions. According to the National Institute of Mental Health, anorexia carries one of the highest mortality rates of any psychiatric disorder, with consequences that reach far beyond weight, including heart damage, bone loss, and profound psychological distress. Its power lies in how convincingly it disguises a self-destructive obsession with calories as strength. Would you be worried about eating a fruit that has less than 100 calories?

The Orange by Joyce Carol Oates
```

### Performance text (classify this)

```text
GIRL: (Pg 300-303) (half shielding her face, raising elbows) You're looking at me; I wish you wouldn't. Undressing me with your eyes, like on the bus after school. But say you're a woman my mother's age, or some dirty-minded guy . . . (confused) Like you think you got me trapped in a net with your eyes a net of eyes but (laughs shrilly) you don't.

GIRL: (dreamy) This . . . in fifteen minutes time precisely I'm going to peel, and eat, eat some of it, one segment to begin with, just one I'll eat it slow, slow slow I'll peel it slow been waiting all day waiting for six, eight, ten hours I know how to wait, I am practiced in waiting in solitude you can't know seeing me with just your eyes. I will peel it slow smelling that smell I love I love the rich ripe smell it's a fiery smell kind of, it's a smell goes right up your nostrils like burning wires to your brain, oh God my mouth is (wipes hurriedly at mouth) watering. That's disgusting isn't it, that's disgusting I hate that. Oh, my mouth is afire it scares me, like, sometimes even at night, asleep I'll wake up, I'm hungry I'll wake up saying Momma, Momma! — it's so alive, like it isn't even me alive bleating like a ridiculous little baby for Momma's milk but someone I don't know. (pause) I hate it, I hate that, I'm a good girl I'm a straight-A honor student I hate that, don't look at me with your eyes in judgment.

(pause, then with the air of one imparting a secret) I don't have cramps I don't bleed anymore, that's a sign of good intentions. God sees into the heart sees good intentions. I have mastered that. I have conquered that. But in swim class I was kind of . . . kind of weak . . . (she drops to knees suddenly, as if faint-headed) . . . Miss Schrieber says, "Jill, is it your period? You can be excused you know if it's your period" . . . so I lied I said yes, I said yes it was my . . . that. Or she'd send me to the school doctor and . . . (pause; then with vehemence)

I hate to lie I hate lies and liars but sometimes I have to lie, saying I ate some food I didn't, saying I didn't lose any more weight, that kind of lie I'm forced to tell to keep prying eyes away, to keep prying thoughts away, wanting to enter my head like buzzing wasps. Oh, I know it's you who own the world but inside here . . . (she draws a circle on the floor with chalk, herself in the center) . . . here it's me it's mine. You can't enter. (defiantly, childlike) I didn't tell Miss Schrieber, I haven't told Momma, I have not had a, oh I hate that, that word I hate, "period," I hate that word "menstruation." I have not had any, any of that, that kind of . . . blood . . . in eleven months. I'm counting on my calendar marking secret signs Momma can't decipher should she spy on me. I can step out of this — (she steps out of chalk circle) — but none of you can step in. (She circles the chalk circle, provocatively, tossing and catching orange.)

This . . . oh it's almost time. I will peel it I will smell it I will bite into it . . . one segment at a time . . . my teeth aching, my mouth . . . alive afire . . . tears in my eyes . . . am I trembling? (regards hands) Am I shaking? I'll hide away in a toilet stall to eat my orange, oh I don't want anybody watching, I hate that, my girl friends even I hate that, there's Cathy she hides away too but we don't talk about it, just looking at each other we know, the Kingdom of God is within is what we know, a torch inside us, God's hunger, burning throbbing aching, the saints knew but they are all dead mostly. Except . . . Mother Teresa. (Pause) But we're not Catholic. We're not anything. (pause) It used to be, I'd stick my finger down my throat — (mimes this, gagging) — now I don't need to, I'm in control. That first time it just came to me like God allowed me to know it was Thanksgiving it was nine of us at the table and Momma and Aunt Tess fussing over the food, and this, this gravy, this turkey gravy in the gravy bowl I saw how it was slick with fat I mean oily globules of fat — oh so disgusting so gross — Momma saying, "Take some gravy, take more mashed potatoes take more dressing more butter more turkey more cranberry sauce more gravy" . . . I locked myself in the bathroom I knew what to do . . . (mimes the act of vomiting; then wipes her face; relieved, refreshed, radiant) I felt so good after I knew I was saved. (pause)

So I went from 128 pounds to 120 pounds to 115 pounds to 109 . . . Then it got harder, for a while . . . seems like certain kinds of flab — (roughly pinches waist, hips; presses her small breasts flat) — are stubborn to melt away. Momma started asking what's going on? was I on a diet or something? was I trying to starve myself what's going on? One day Momma barged in my room fouling the air with her cigarette, took hold of this old ratty sweater I was wearing, my favorite old sweater I wear around the house, Momma yanked it tight seeing how thin I was she got scared then I saw it in her eyes, saying "Oh Jill oh hon oh my God what's wrong"— and I — (backs away, speaking rapidly) — I said "Momma don't touch don't touch leave me alone don't touch!"

(She mimes fending off someone; repositions herself inside the chalk circle, panting and trembling.)

Now I weigh 93 pounds . . . this morning I did . . . but I had some Diet Coke, four cans of Diet Coke, so I'm . . . heavier. Yesterday I had a 7-Grain Datebar . . . divided it into quarters 'cause it weighs four ounces I spread out eating it over four hours in my room in the dark after they'd all gone to bed I'm happiest then. At school I can be happy too in a different way inside here (indicates circle) but it's harder. I divide up the Diet Coke, the diet chocolate-cream, coffee if it doesn't make me too spaced out, what I hate's running to the restroom a dozen times a day my stomach bloating I hate that you can see it now can't you! can't you! (strikes fist against belly) Like I'm, you know, like I'm, I'm pregnant, going to have a, a baby but oh no I'm not oh no never. (trembling; on the verge of mania) I'm so happy you can't know, inside me, there's God inside me you can't trap me with your eyes, no nor Momma either with her threats and tears and coercion, no other word but COERCION but she can't get me can't touch me, they say — the doctor she made me go to, the therapist — that woman Ph. D. who came to talk to us at assembly — saying it's a medical problem an illness trying to scare us "irreversible liver damage" but it isn't, it isn't physical at all, it's here, it's God inside me, it's mine. Like you out there—you're all babbling in some foreign language. (pause; then with ecstatic certainty)

My days my nights I love how they are divided like this orange divided into segments I pick apart with my fingers, sink my teeth into slow like on the far side of my hunger those faces, voices — you — sure I see you, and I hear you, I talk with you I smile at you but . . . I don't care about you. I don't. Not a one of you. I am always thinking of . . . this. (holds orange high above her head) Always I am thinking of . . . dreaming of . . . oh it's like fire! it hurts! it's wild in a frenzy like fire the inside of my mouth alive with hunger with wanting to bite to chew to eat to EAT EAT EAT like a frenzy alive like scurrying ants! — the hunger and the food COLLIDE . . . (wincing) It's pain but it's a good pain. (pause) Sometimes, I'm not weak or sick or, I know I must conserve my strength, I'll, like, crawl up a stairs . . . (on hands and knees) . . . if nobody's around . . . (pause; flaring up angrily)

"I don't want to be touched" I said, "I don't love you or anybody love hurts my skin hurts don't touch me" I said "STAY CLEAR." (pause) Now it’s time, it’s time it's that time now I'm safe nobody can see I'm locked in this toilet stall it's the middle of the hour nobody will barge in nobody can trap me with their eyes I'm safe I can't be touched I . . . (orange rolls out her fingers, out of the chalk circle, out of reach: she strains to get it but cannot.)
```

---

## IC-0230: Oranges and Sweet Sister Boy

- Title: Oranges and Sweet Sister Boy
- Author (byline): Judy Ruiz
- Work: Motives for Writing with Student Access to Catalyst
- Publisher: The McGraw-Hill Companies
- Publication date as stated: June 2005
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 3273
- Already set (do not supply): none

### Source block (context only)

```text
Author: Judy Ruiz
Book: Motives for Writing with Student Access to Catalyst
ISBN: 0073221546
Publisher: The McGraw-Hill Companies
Date (Month/Year): June 2005
```

### Introduction (context only: never use it for content warnings)

```text
“Oranges and Sweet Sister Boy” by Judy Ruiz
```

### Performance text (classify this)

```text
I am sleeping, hard, when the telephone rings. It's my brother, and he's calling to say that he is now my sister. I feel something fry a little, deep behind my eyes. Knowing how sometimes dreams get mixed up with not-dreams, . I ask my brother to run that stuff by me again.

News can make a person stupid. It can make you think you can do something. So I ask The Blade question, thinking that if he hasn't had the operation yet that I can fly to him, rent a cabin out on Puget Sound. That we can talk. That I can get him to touch base with reality.

"Begin with an orange," I would tell him. "Because oranges are mildly intrusive by nature, put the orange somewhere so that it will not bother you - in the cupboard, in a drawer, even a pocket or a handbag will do. The orange, being a patient fruit, will wait for you much longer than say a banana or a peach."

I would hold an orange out to him. I would say, "This is the one that will save your life." And I would tell him about the woman I saw in a bus station who bit right into her orange like it was an apple. She was wild looking, as if she'd been outside for too long in a wind that blew the same way all the time. One of the dregs of humanity, our mother would have called her, the same mother who never brought fruit into the house except in cans. My children used to ask me to "start" their oranges for them. That meant to make a hole in the orange so they could peel the rind away, and their small hands weren't equipped with fingernails that were long enough or strong enough to do the job. Sometimes they would suck the juice out of the hole my thumbnail had made, leaving the orange flat and sad. In the magazine articles, you don't see this: "Well, yes. The testicles have to come out. And yes. The penis is cut off." What you get is tonsils. So-and-so has had a "sex change" operation. A sex change operation. How precious. How benign. Doctor, just what do you people do with those penises?

News can make a person a little crazy also. News like, "We regret to inform you that you have failed your sanity hearing."

The bracelet on my wrist bears the necessary information about me, but there is one small error. The receptionist typing the information asked me my religious preference. I said, "None." She typed, "Neon."

Pearl doesn't have any teeth and her tongue looks weird. She says "Pumpkin pie." That's all she says. Sometimes she runs her hands over my bed sheets and says pumpkin pie. Sometimes I am under the sheets. Marsha got stabbed in the chest, but she tells everyone she fell on a knife. Elizabeth - she's the one who thinks her shoe is a baby - hit me in the back with a tray right after one of the cooks gave me extra toast. There's a note on the bulletin board about a class for the nurses: "How Putting A Towel On Someone's Face Makes Them Stop Banging Their Spoon/OR Reduction of Disruptive Mealtime Behavior By Facial Screening - 7 P.M. - Conference Room." Another note announces the topic for re-motivation class: "cows." All the paranoid schizophrenics will be there.

Here, in the place for the permanently bewildered, I fit right in. Not because I stood at the window that first night and listened to the trains. Not because I imagined those trains were bracelets, the jewelry of earth. Not even because I imagined that one of those bracelets was on my own arm and was the Texas Zephyr where a young couple made love and conceived me. I am eighteen and beautiful and committed to the state hospital by a district court judge for a period of one day to life. Because I am a paranoid schizophrenic. I will learn about cows. So I'm being very quiet in the back of the classroom, and I'm peeling an orange. It's the smell that makes the others begin to turn around, that mildly intrusive nature. The course is called "Women and Modern Literature," and the diaries of Virginia Woolf are up for discussion except nobody has anything to say.

I, of course, am making a mess with the orange; and I'm wanting to say that my brother is now my sister. Later, with my hands still orangey, I wander in to leave something on a desk in a professor's office, and he's reading so I'm being very quiet, and then he says, sort of out of nowhere, "Emily Dickinson up there in her room making poems while her brother was making love to her best friend right downstairs on the dining room table. A regular thing. Think of it. And Walt Whitman out sniffing around the boys. Our two great American poets." And I want to grab this professor's arm and say, "Listen. My brother called me and now he's my sister, and I'm having trouble making sense out of my life right now, so would you mind not telling me any more stuff about sex." And I want my knuckles to turn white while the pressure of my fingers leaves imprints right through his jacket, little indentations he can interpret as urgent. But I don't say anything. And I don't grab his arm. I go read a magazine. I find this: "I've never found an explanation for why the human race has so many languages. When the brain became a language brain, it obviously needed to develop an intense degree of plasticity. Such plasticity allows languages to be logical, coherent systems and yet be extremely variable. The same brain that thinks in words and symbols is also a brain that has to be freed up with regard to sexual turn-on and partnering. God knows why sex attitudes have not been subject to the corresponding degrees of modification and variety as language. I suspect there's a close parallel between the two. The brain doesn't seem incredibly efficient with regard to sex."

John Money said that. The same John Money who, with surgeon Howard W. Jones, performed the first sex change operation in the United States in 1965 at Johns Hopkins University and Hospital in Baltimore.

Money also tells about the hijra of India who disgrace their families because they are too effeminate: "The ultimate stage of the hijra is to get up the courage to go through the amputation of penis and testicles. They had no anesthetic." Money also answers anyone who might think that "heartless members of the medical profession are forcing these poor darlings to go and get themselves cut up and mutilated," or who think the medical profession should leave them alone. "You'd have lots of patients willing to get a gun and blow off their own genitals if you don't do it. I've had several who got knives and cut themselves trying to get rid of their sex organs. That's their obsession!"

Perhaps better than all else, I understand obsession. It is of the mind. And it is language-bound. Sex is of the body. It has no words. I am stunned to learn that someone with an obsession of the mind can have parts of the body surgically removed. This is my brother I speak of. This is not some lunatic named Carl who becomes Carlene. This is my brother.

So while we're out in that cabin on Puget Sound, I'll tell him about LuAnn. She is the sort of woman who orders the in-season fruit and a little cottage cheese. I am the sort of woman who orders a double cheeseburger and fries. LuAnn and I are sitting in her car. She has a huge orange, and she peels it so the peel falls off in one neat strip. I have a sack of oranges, the small ones. The peel of my orange comes off in hunks about the size of a baby's nail. "Oh, you bought the juice oranges," LuAnn says, to me. Her emphasis on the word "juice" makes me want to die or something. I lack the courage to admit my ignorance, so I smile and breathe "yes," as if I know some secret, when I'm wanting to scream at her about how my mother didn't teach me about fruit and my own blood pounds in my head wanting out, out.

There is a pattern to this thought as there is a pattern for a jumpsuit. Sew the sleeve to the leg, sew the leg to the collar. Put the garment on. Sew the mouth shut. This is how I tell about being quiet because I am bad, and because I cannot stand it when he beats me or my brother.

"The first time I got caught in your clothes was when I was four years old and you were over at Sarah what's-her-name's babysitting. Dad beat me so hard I thought I was going to die. I really thought I was going to die. That was the day I made up my mind I would never get caught again. And I never got caught again." My brother goes on to say he continued to go through my things until I was hospitalized. A mystery is solved.

He wore my clothes. He played in my makeup. I kept saying, back then, that someone was going through my stuff. I kept saying it and saying it. I told the counselor at school. "Someone goes in my room when I'm not there, and I know it - goes in there and wears my clothes and goes through my stuff." I was assured by the counselor that this was not so. I was assured by my mother that this was not so. I thought my mother was doing it, snooping around for clues like mothers do. It made me a little crazy, so I started deliberately leaving things in a certain order so that I would be able to prove to myself that someone, indeed, was going through my belongings. No one, not one person, ever believed that my room was being ransacked; I was accused of just making it up. A paranoid fixation.

And all the time it was old Goldilocks.

So I tell my brother to promise me he'll see someone who counsels adult children from dysfunctional families. I tell him he needs to deal with the fact that he was physically abused on a daily basis. He tells me he doesn't remember being beaten except on three occasions. He wants me to get into a support group for families of people who are having a sex change. Support groups are people who are in the same boat. Except no one has any oars in the water.

I tell him I know how it feels to think you are in the wrong body. I tell him how I wanted my boyfriend to put a gun up inside me and blow the woman out, how I thought wearing spiked heels and low-cut dresses would somehow help my crisis, that putting on an ultra-feminine outside would mask the maleness I felt needed hiding. I tell him it's the rule, rather than the exception, that people from families like ours have very spooky sexual identity problems. He tells me that his sexuality is a birth defect. I recognize the lingo. It's support-group-for-transsexuals lingo. He tells me he sits down to pee. He told his therapist that he used to wet all over the floor. His therapist said, "You can't aim the bullets if you don't touch the gun." Lingo. My brother is hell-bent for castration, the castration that started before he had language: the castration of abuse. He will simply finish what was set in motion long ago.

I will tell my brother about the time I took ten sacks of oranges into a school so that I could teach metaphor. The school was for special students - those who were socially or intellectually impaired. I had planned to have them peel the oranges as I spoke about how much the world is like the orange. I handed out the oranges. The students refused to peel them, not because they wanted to make life difficult for me - they were enchanted with the gift. One child asked if he could have an orange to take home to his little brother. Another said he would bring me ten dollars the next day if I would give him a sack of oranges. And I knew I was at home, that these children and I shared something that makes the leap of mind the metaphor attempts. And something in me healed.

A neighbor of mine takes pantyhose and cuts them up and sews them up after stuffing them. Then she puts these things into Mason jars and sells them, you know, to put out on the mantel for conversation. They are little penises and little scrotums, complete with hair. She calls them "Pickled Peters."

A friend of mine had a sister who had a sex change operation. This young woman had her breasts removed and ran around the house with no shirt on before the stitches were taken out. She answered the door one evening. A young man had come to call on my friend. The sex-changed sister invited him in and offered him some black bean soup as if she were perfectly normal with her red surgical wounds and her black stitches. The young man left and never went back. A couple years later, my friend's sister/brother died when s/he ran a car into a concrete bridge railing. I hope for a happier ending. For my brother, for myself, for all of us.

My brother calls. He's done his toenails: Shimmering Cinnamon. And he's left his wife and children and purchased some nightgowns at a yard sale. His hair is getting longer. He wears a special bra. Most of the people he works with know about the changes in his life. His voice is not the same voice I've heard for years; he sounds happy.

My brother calls. He's always envied me, my woman's body. The same body I live in and have cursed for its softness. He asks me how I feel about myself. He says, "You know, you are really our father's first-born son." He tells me he used to want to be me because I was the only person our father almost loved.

The drama of life. After I saw that woman in the bus station eat an orange as if it were an apple, I went out into the street and smoked a joint with some guy I'd met on the bus. Then I hailed a cab and went to a tattoo parlor. The tattoo artist tried to talk me into getting a nice bird or butterfly design; I had chosen a design on his wall that appealed to me -a symbol I didn't know the meaning of. It is the Yin-Yang, and it's tattooed above my right ankle bone. I supposed my drugged, crazed consciousness knew more than I knew: that yin combines with yang to produce all that comes to be. I am drawn to androgyny. Of course there is the nagging possibility that my brother's dilemma is genetic. Our father used to dress in drag on Halloween, and he made a beautiful woman. One year, the year my mother cut my brother's blond curls off, my father taped those curls to his own head and tied a silk scarf over the tape. Even his close friends didn't know it was him. And my youngest daughter was a body builder for a while, her lean body as muscular as a man's. And my sons are beautiful, not handsome: they look androgynous.

Then there's my grandson. I saw him when he was less than an hour old. He was naked and had hiccups. I watched as he had his first bath, and I heard him cry. He had not been named yet, but his little crib had a blue card affixed to it with tape. And on the card were the words "Baby Boy." There was no doubt in me that the words were true. When my brother was born, my father was off flying jets in Korea. I went to the hospital with my grandfather to get my mother and this new brother. I remember how I wanted a sister, and I remember looking at him as my mother held him in the front seat of the car. I was certain he was a sister, certain that my mother was joking. She removed his diaper to show me that he was a boy. I still didn't believe her. Considering what has happened lately, I wonder if my child-skewed consciousness knew more than the anatomical proof suggested.

I try to make peace with myself. I try to understand his decision to alter himself. I try to think of him as her. I write his woman name, and I feel like I'm betraying myself. I try to be open-minded, but something in me shuts down. I think we humans are in big trouble, that many of us don't really have a clue as to what acceptable human behavior is. Something in me says no to all this, that this surgery business is the ultimate betrayal of the self. And yet, I want my brother to be happy.

It was in the city of San Antonio that my father had his surgery. I rode the bus from Kansas to Texas, and arrived at the hospital two days after the operation to find my father sitting in the solarium playing solitaire. He had a type of cancer that particularly thrived on testosterone. And so he was castrated in order to ease his pain and to stop the growth of tumors. He died six months later.

Back in the sleep of the large world of dreams, I have done surgeries under water in which I float my father's testicles back into him, and he -the brutal man he was - emerges from the pool a tan and smiling man, parting the surface of the water with his perfect head. He loves all the grief away.

I will tell my brother all I know of oranges, that if you squeeze the orange peel into a flame, small fires happen because of the volatile oil in the peel. Also, if you squeeze the peel and it gets into your cat's eyes, the cat will blink and blink. I will tell him there is no perfect rhyme for the word "orange," and that if we can just make up a good word we can be immortal. We will become obsessed with finding the right word, and I will be joyous at our legitimate pursuit.

I have purchased a black camisole with lace to send to my new sister. And a card. On the outside of the card there's a drawing of a woman sitting by a pond and a zebra is off to the left. Inside are these words: "The past is ended. Be happy." And I have asked my companions to hold me and I have cried. My self is wet and small. But it is not dark. Sometimes, if no one touches me, I will die.

Sister, you are the best craziness of the family. Brother, love what you love.
```

---

## IC-0231: Palace of the End - Instruments of Yearning

- Title: Palace of the End - Instruments of Yearning
- Author (byline): Judith Thompson
- Work: Palace of the End, Pg 28-40
- Publisher: Playwrights Canada Press
- Publication date as stated: Nov 2009
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NEHRJAS
- Teaser before the introduction: No
- Spoken words (computed): 1396
- Already set (do not supply): none

### Source block (context only)

```text
Author: Judith Thompson
Book: Palace of the End, Pg 28-40
ISBN: 978-0887548352
Publisher: Playwrights Canada Press
Date (Month/Year): Nov 2009
```

### Introduction (context only: never use it for content warnings)

```text
As a boy Saddam Hussein would heat an iron poker until it was white-hot, then use it to impale cats and dogs. Years later, when he had boys of his own, he would take them into prisons so they could watch — and get used to — torture and executions. The Arab world is replete with dictators, many of them ruthless. But for sheer unbridled cruelty, none of them can touch Saddam. And for hellish and sadistic brutality, no other Arab state — perhaps no other state in the world — can compare with what Saddam Hussein created in Iraq.

In this monologue, “Instruments of Yearning,” we hear from Nehrjas Al Saffarh, the wife of an Iraqi dissident and leader of the Communist party. She and her sons were tortured by Saddam’s secret police, and she alone lived to tell of the events.

Instruments of Yearning from The Palace of the End by Judith Thompson
```

### Performance text (classify this)

```text
NEHRJAS: (Pg 28-40) (a beautiful, but haunted Iraqi woman of about 50) It broke our hearts that the United States land of the free, home of the brave – liberty and justice for all – was supporting Saddam through the sixties and even the seventies. After the coup, the CIA gave a list of the names of everyone in the Communist Party; they were making his army and all his torturers all powerful. We wondered, did the people of the United States know that their taxes were paying for instruments of torture? We had to be very secretive. We had to let our babies cry at night so that their cries would cover the sound of typing. If the secret Police heard typing, they would arrest us immediately. One day they took my little brother. He was a silly boy, he like to dance with girls and drink alcohol and wear expensive clothing and he was at the University. He was taken. We did not know where he was. We got a phone call in the morning. “We are sending him home in a cab.” We waited all day. The cab arrived. The cab driver said in Arabic, “There is a God” – because my brother was, thank God, still alive –

We rushed him into the house because if the neighbors saw, they would shun us – they would be afraid of guilt by association. And he – he was so badly beaten, we couldn’t recognize his face. And he . . . he could see nothing. My other brother cried and my mother said, “It is alright. This is the way men learn to be men.” It seems harsh, but you have to understand the way we lived, and what it was to be a man. He said that his friend talked back to them – they beat him worse, but he was still breathing. And then they buried him alive. My husband, as soon as he could, he went into hiding as he, at that time, was the great, visionary leader of the Communist party.

So, the monsters we lived in fear of were the Baath secret police, “Jihaz Haneen,” if you can believe it. In English? “The Instruments of Yearning.” Can you explain that to me please?

The torture jails were two fairy tale castles, from long ago, where the King had lived – we had not liked him either. He was Saudi, but he was nothing compared to Saddam. The gardens were tended by a master gardener, a true genius of nature. And so the castle was called The Palace of Flowers. Until the Dark Age, when it became the Palace of the End. “Qasr al-Nihayah.” Iraq’s own house of horrors; our children weren’t afraid of fictional witches or monsters. Those stories are only for peaceful places; our children had nightmares about the Palace of the End.

“O, people of Iraq . . . By God, I shall strip you like bark, I shall truss you like a bundle of twigs, I shall beat you like stray camels . . . By God, what I promise, I fulfill; what I purpose, accomplish; what I measure, I cut off.” So said al-Hadjadj, the newly arrived governor of Iraq in the year 694 . . . so said Saddam . . . so said George Bush . . . and here we are. So . . .

So. They began to torture my son Fahdil. They said all we want to know is where is your father. You tell us, you can have bread and water. About six hours later, he said he would tell them. I was almost relieved. But then he told them a lie. They gave him bread and water while the others went to find my husband. He whispered to my older son that the reason he told the lie was although he knew they would keep beating him, he thought that the bread and water would give him the strength to keep the secret . . . to endure more torture. And so they came back. And beat him more. I was tied up, on my back, forced to watch, as was my older son. Well, Fahdil lied three times. Three times he got bread and water, but the third time, they were onto his trick. They were furious. Now they beat him hard, with the full strength of men. He said to my older son: “I’m dying,” he said, “I feel death around me. I want you to take care of my mother and little sister.” They thought . . . what more can we do? What can we do to break down this child and his mother? Meanwhile, they had taken away my older son, Nahdne, they had let him go.

What they did then? Do you notice I have no fan here in my apartment? There was a fan in the torture room. Right above me where I was tied. They grabbed little Fahdil by his shirt. He was able to look at me one last time. My precious boy, he looked into my eyes with his beautiful sorrowful eyes and he smiled. I said, “I love you, my son.” He did not scream. He did not even whimper. My son was more brave than many full grown men, and he was eight years old. They turned him upside down, and then they tied him to the ceiling fan – upside down. They died him to the ceiling fan and they turned it to fast. So my son is spinning He is spinning round and round I cannot put into words the feelings inside me.

I was praying and he was praying. We were in the hands of the devil, no doubt, but we had faith that we would be delivered – faith was all we had. And neither of us will speak. IF we give in, we are giving not only our lives but the lives of millions. It would be like giving up Nelson Mandela, you understand? It would be like saying, “yes; you can go and murder these million children, to save ourselves.” And I knew, I was quite certain they would not kill us because it was so deeply in my culture to never harm a pregnant woman or a child. I thought: We will survive this. My son will be known forever as the most heroic child who ever lived. He will become a great leader. But he kept spinning.

My son who loved to write stories and draw pictures of animals. Who called our black and white cat “Precious” . . . who loved geckos, gave everyone he saw a name, and you know in Iraq they are everywhere. But he had a story for each one. He always hoped to see a cheetah, for there are few cheetahs in Iraq. He would pray to Allah to see a cheetah and have a running contest, for he was a very fast runner . . . spinning upside down over my face. And still, I did not speak. The baby was turning and turning inside my belly. I fainted many, many times that day.

After hours and hours of the spinning, my son, of course, was unconscious. And they threw him on the roof. It was cold then. It was winter. He had no coat, of course. And they carried me up to an attic room, just underneath the room and tied me down. And still I did not speak. For days and days I lay there. The only thing keeping me breathing was that I could hear my son coughing on the roof. That gave me such happiness . . . to hear him cough. I knew he was sick. He probably even had pneumonia, but the coughing meant that he was alive! And as long as he was alive, when they let us go, I could nurse him to good health again. I was sure they would try to look like good-hearted men, and at the very last minute they would let us go. I was so sure, and that is why I did not speak. Every hour was like a day, every day like a year . . . his cough was stronger and louder and then it began to get weaker . . . and weaker. Why did I not speak then? . . . . And weaker still . . . . and then he did not cough anymore. (Long beat)

They came in, laughing. “We found your husband anyway, you foolish woman And, oh . . . we are sorry about your son. We were going to let him go today, but he must have had a weak constitution. He is with Allah.”

The Palace of the End . . .
```

---

## IC-0232: My Pyramids from Palace of the End

- Title: My Pyramids from Palace of the End
- Author (byline): Judith Thompson
- Work: The Palace of the End
- Publisher: Playwrights Canada Press
- Publication date as stated: Nov 2009
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: PVT. ENGLAND
- Teaser before the introduction: No
- Spoken words (computed): 1509
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
In 2004, photographs of abuses at Abu Ghraib Detention Center shocked the world. Detainees on leashes, wearing women’s undergarments and even posed naked in a human pyramid. Ultimately, seven people were charged for abusive actions, but the face of the scandal will always be Lynndie England, the 21-year-old private grinning at the camera.

Private England wasn't the only woman soldier in the photographs - but she was the most arresting looking, like a 14-year-old boy who shouldn't have been there in the first place. Her legal defense, that she was unduly influenced by Specialist Charles Graner, the father of her child and the only soldier still serving time for abuses at Abu Ghraib, was compounded outside the courtroom by assumptions about her background; that she came from a place where people didn't know better - a place called West Virginia.

This monologue is the fictionalized account of Pvt Lynndie England – her perceptions, her background and her story. My Pyramids by Judith Thompson from The Palace of the End.
```

### Performance text (classify this)

```text
PVT. ENGLAND: None of them higher ups have spoke to me since it all came crashin down on my head since they moved me here to push around paper; I been waitin on their call but the only person ever calls me is mommy. And my lawyer. He says I am a scapegoat. And he won’t let me up on the stand because I won’t act like I’m retarded, which is what he wants me to do, so I won’t be held accountable; I’ll tell the truth. And that is not what anyone wants to hear.

Wonder if I’ll be sentenced to jail for eight years like Charley. It’s funny, you know, if things had gone different for me, insteada working in an office and waitin for my trial I mighta had a t.v. movie made about me, too. She is truly a hero she is, and hey, did you know she’s from West Virginia too? Yeah, she’s a country girl, like me, and us country girls kick butt! Nobody messes with a country girl, oh no, let go! Can you imagine how scared she felt? Everybody in her company killed except her? Prisoner of the most brutal people on earth? Yeah. I reckon Jessica Lynch is America’s sweetheart. I am America’s secret that got shouted out to the world. And they is not happy about that not at all.

And that is why they gonna make an example of me. But one day, I’mona be in the history books. You wait and see. I’m ona be a War Hero; like Annie Oakley.

I was in that in high school, “Annie Get your Gun.” I was one of the chorus singing; our lead was real good, Lisa? She tried for American Idol: “Anything you can do I can do better, I can do anything better ‘n you.” “I’m just a girl who caint say no, I’m in a terrible twist.”

I am going to be remembered. But first, we gotta find a way to somehow, make them pictures disappear. Cause: The thing about those . . . pictures. I . . . look at her, me, that homely little private with the thumbs up. And the naked Iraqi men, and . . . Well, it is like a dream they are telling me I had? But I don’t remember it like that? And they are sayin: “No this is the dream you had?” Because they can doctor pictures you know. They can do anything they please. And those forces that do not want Girls in the army – wanted the world to see those pictures.

Okay, okay, I’mona be honest with you . . in the fact of it . . . That is what I did, for one second they said “give us the thumbs up, baby,” so that’s what I did. For one second of a whole year, dudes. And that is what everyone sees? How would you like your weirdest second, like, played over and over all over the world . . . for all of time, dude?

Like those dreams about yourself where ya did something WEIRD something you would never do? And ya wake up and ya feel uneasy and you are glad that noboby was lookin in your dream? And ya just wanna forget it and ya do, because dreams, they just disappear, don’t they?

(Long beat)

I’ll tell you what most people don’t know. It got a hell of a lot worse than that. So what they were naked. So? They get naked every time they have a shower. So? And as far as me laughin at – pointing at the guy’s willie? Well tie me down if that’s the worst thing that happened to ‘em in the Abu G. they be lovin it.

But that is not the style of girl I am, okay? I respect men and their privates and I do not nor have I ever laughed at a man’s willie. But these are not men, they are terrorists. And they had intelligence. They knew who was gonna blow up who and as far as I am concerned I was doin’ what had to be done, to get to the intelligence and that is, according to their culture, me laughin at their willies was worse than a beatin . . . . way worse. I was softening them up; like you might put out hard butter on the window sill. I had a smile on my face but this was SERIOUS – INTELLIGENCE – WORK.

And I am very proud to say that the naked human pyramids WAS ALL MY IDEA. Actually, it’s the first thing that came to my mind when I walked into that prison and seen all them men that look exactly alike. I know what might be fun: HUMAN PYAMID WITH NIKKID CAPTIVE MEN. Because I always did have an interest in choreography, you know?! I see people dance, I wanna go in an mould ‘em.

And they might not have liked it, but they have learned something useful. If they teach gym, in a school. Or supervise a cheerleading squad. We was not entertaining ourselves. We was breaking down the terrorists. And it worked. We did attain information.

And the other . . . Takin the guy around on a leash? Well, he called me a dog. Yes, he did. Just like all you losers on the net. He knew a little English and he called me a dog, so once in my life I could f***in’ give it to him. “You think I’m a dog? You think I’m a f***in’ dog, you monkey? Let’s go for a f***in’ walk . . . you wanna go for a walk?” And Charley and them is laughing and well, I never got laughs before. I am not a funny person, and WOW man, getting laughs is the best high. The guys was laughing, dudes, they loved it, so they go: “Put him on the leash.” And I do . . . like a sketch, like Saturday Night Live, like . . . oh, my god, it’s time to take the dog for a walk . . . Hey, Mom? Did you take the dog for a walk? Henry? Henry? Did you walk the dog? Nobody walked the damn dog. I’m walkin’ it. Her dog, ya dirty dog. No treat for you today. You been a bad dog. And I’m pullin’ him . . . I was surprised how different is a human neck from a dog neck. With dogs you can pull and pull and they keep on going. Not with humans. They necks is soft.

And . . . well . . . It is a weird feeling. It made my breathing go a little funny. Shallow. My voice kinda got full of breath. And I felt like I had walked through the looking glass. Where everything was not real and I could walk out again anytime and what was behind there would stay there.

I had that over someone else once and that was – Lee Ann Wibbey. She wanted friends so bad and she smelled and she was weird and ugly? Now she was ugly so nobody liked her. So we was bored so we axed her to come to the clubhouse and she come with her backpack and her nightie – she thought it was a sleepover birthday and we made her strip and bark like a dog, and there was a moment that I realized she would do anything we said. Anything at all. We burned her clothes? And we took her fake leg off, and chopped it up – okay, I know it sounds terrible but we didn’t chop up her flesh leg or nothing – and then we tole her to start crawlin home. And we laughed. Oh, my God, we laughed.

Once in church, we hadda think upon our sins, and I seen her there, she was in the church, and she turn around and she looked at me. And I knew then, that what all happened at the clubhouse had been more than a joke for her. Well, sir, I love God and Jesus is my Lord, so I did pray for forgivenessa about Lee Ann Wibby – but dudes, Lee Ann Wibby is an American. She was very VERY different from the APES AT ABU GHRAIB. They was monsters in the shape of human beings. They was prisoners of WAR.

So, there I was, little me, in ABU GHRAIB . . . me who’d been workin in the Dairy Queen in Fort Ashby, who had been fired from the Dairy Queen for messin up the Brownie Explosion and I was the BIG boss of the BIG DEAL TERRORISTS, guys who had KILLED AMERICANS. GUYS WHO WERE PLANNING ANOTHER 9/11, dud, AND YOU ARE UPSET THAT I laughed AT THEIR WILLIES? (Beat)

I will tell you something. We did a hell of a lot worse than what you seen. Or what you heard. What YOU seen is tiddlywinks: we made a man masturbate. Ohhhhh! So SCARY!!! SO? So WHAT? So the frick what? I’ll tell you I didn’t do nothing to them Iraqis that hadn’t been done to me many times at the clubhouse. By my friends, and they still my friends. Yeah. I’m not mad at em, it was just a little fun.
```

---

## IC-0233: Paradise, Kansas

- Title: Paradise, Kansas
- Author (byline): Cathleen Sakamai
- Work: Fast Horse Plays, Round 8; Pgs 3-7
- Publisher: CreateSpace Independent Publishing Platform
- Publication date as stated: Oct 2015
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SHE
- Teaser before the introduction: Yes
- Spoken words (computed): 1578
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cathleen Sakamai
Book: Fast Horse Plays, Round 8; Pgs 3-7
ISBN: 978-1530302246
Publisher: CreateSpace Independent Publishing Platform
Date (Month/Year): Oct 2015
```

### Introduction (context only: never use it for content warnings)

```text
In a small Kansas town where difference is something to survive rather than celebrate, a young girl watches her beloved brother Jack slowly disappear. What begins as a desperate search for belonging transforms into something darker as her brother is pulled toward extremist ideology and the seductive promise of purpose.

Religious radicalization does not arrive all at once; it seeps quietly into the cracks of loneliness and loss of identity.

Paradise, Kansas by Cathleen Sakamai is a story about grief, manipulation, and the devastating cost of losing someone to an idea that convinces them hatred is holy.
```

### Performance text (classify this)

```text
SHE: (Pg 3-7) He got this for me a couple of years ago, when I was 14. (shows a rubber bracelet on her wrist) It says, "Different is OK! and it's rainbow, and I loved rainbows. But the kids at school didn't really love rainbows and suddenly they had new, colorful names to call me. But I came home and said to my brother, "I'm different, yeah, but I’m not a lesbian. I mean, I don't think I am." And my older brother, Jack, he said it was the only one they had, and he didn't think I was gay, but he wanted to get it for me because of the words. . .but . . .

Different is not okay in Testament, Kansas. Population: 4,000. Testament, Kansas, where the cows and chickens far outnumber the people and the wheat fields aren't just a stereotype -- they're a reality, like this sea of waving golden brown that just stretches out forever. And we have lots of sorghum, soybeans and corn too, but they're not nearly as notorious as the wheat.

I was born with a really intense wheat allergy, which I like to think is this really romantic but perverse analogy for being born here, being here. And I remember thinking that if I could just put a finger on it, it would make it easier, actually. That if I was gay or a child prodigy or deaf or something, that the difference would suddenly make sense and I'd get it. But I wasn't any of those things and neither was Jack. Instead we were these people that didn't make sense to anyone around us. And that feels foreign to a kid.

SHE: Teenagers here don't talk about politics or human rights or religious freedom. They talk about McCab's field on Friday night or taking over their parents' business after high school. And saying that makes me sound like some kind of elitist -- and I'm not. I've been called that since before I understood what it really meant. And Jack would say, "maybe it's not that we're too good for Testament. Maybe Testament is too good for us." Which was like a riddle with no answer that was too big to even think about. Kids aren't supposed to have existential crises, right?

So, Jack would drive us to Topeka for art festivals and films and to hear people speak and things of that sort. And okay, so, you're laughing, "Wow, Topeka;" but, for me, it was proof. You know? Proof that there were people out there who had different ideas and could talk about them and engage. And Jack would tell me that we were going to get out of Testament and meet people who got us and that there was just so much out there. And as long as I had him, I was okay. I really was.

He drove us once, late on a Sunday night, about two hours from home out into the middle of nowhere. And we pulled into a 7-11and he came back with two lime ice bars, handed me one of them and said, "Well, you've been saying for years that you wanted to come here. Here we are." And I said, "What are you talking about?" And Jack said, "Welcome to Paris. . . Kansas. Isn't it amazing?" And it was not very amazing; but he was so pleased with himself, we took a selfie with the town sign. Population 371. And then we talked about going to the actual Paris someday.

And I closed my eyes. And I believed.

Jack found out about a year after that. The spring of his senior year. He'd applied to a bunch of really good schools. He had good grades and all of that, and, well, he didn't get into any of the schools. Not one. And he just kept saying that it was fine, and I kept saying that it wasn't. It wasn't fine at all. But he wasn't going to leave to go to school in Kansas He would just stick it out, since I only had two more years, and then would we leave together. And secretly, I was relieved, you know? I was. And I should have pushed harder. But it's easy to be selfish, and you don't even realize it. It's as natural as breathing.

And so Jack just existed for a while. I don't know how else to put it. Maybe school and routine had kept him attached to something, and now he was just floating. I just wanted him to do something. To be something. He told me, "I don't belong." And I told him that this was not some kind of revelation. We never belonged. This wasn't new. But he was distant. Hours on-line in the basement. Quiet. Away. I should have done something. Acting is hard when you don't know what it is that you're trying to fight against. I said, "I know you, Jack. I know you." And he said, "Maybe." Really. . . maybe?

But here's the crazy part. He got better. He got a job at an auto-shop in Topeka. And at first I thought we'd really got on the train to Crazytown, right? This is my brother who wanted to go to law school and become an environmental attorney and he's painting people's cars. And then I thought, "Okay, so maybe I am elitist," and I've got to keep this in check because he was happy. And so I was happy too. And he introduced me to his friends, and there was so much laughter. I guess maybe camaraderie would be the way to put it. They laughed about our red hair. They said in their country, in Syria, it was called "crusader hair." And I said I liked that much better than being called Wendy or Pippi Longstocking. And they laughed. And Jack belonged.

Jack was staying most nights in Topeka with his friends, but he had come home for dinner on Sunday. He was buttering a roll when he told us that he was converting. And the quiet was so immense that the room suddenly felt very small. My dad took a bite of pot roast, and my mother got up to get something from the kitchen. The silence was probably worse than anything they could have said. But Jack was just excited, just babbling, and I couldn't figure out the right thing amongst all the things in my head. I thought, I don't understand. I thought, I want you to belong and to be happy. I thought, Different is OK. But I didn't say any of those things. I said, "I love you." And it sounded so young and foolish.

The worst part of it for me is the guilt, I think. This guilt of not saying or doing the right thing in a hundred or a thousand different moments. As if I could have that power to bring him back to me. Jack was very busy with learning and training, and I remember thinking that this idea of becoming Muslim – converting -- was a full-time job in itself. We did not see each other and we talked on the phone less and less. It became mostly Facebook messages between Jack and I, and those became less . . . coherent. Mostly him encouraging me to stay strong. And asking me to believe in him. I wanted to. I didn't know what I was believing.

He sent mom a message asking for her blessing and talking about the crusade. And then Jack was gone. I spent hours reading everything I could and sending messages. The auto-shop in Topeka had closed and a man sent me a message saying that Jack was a crusader. And we learned that Jack wasn't in the US anymore. We learned that he wasn't supposed to be communicating with us.

Last November, I got a message from Jack on Facebook. It was just a few words, "I wish you could go with me. I hope to see you in Paradise."

On November 13, 130 people died in the attacks in Paris. Jack posted a selfie with a group of men I did not know in front of the Eiffel Tower that morning. I will never go to Paris with my brother, Jack. There is no Paradise. That's a lie. And sometimes. . . sometimes. . . (struggles to remove the rubber bracelet from her wrist) different is not OK.

Hate has its own kind of speed. On November 14, I drove to Topeka, to the mosque there, the majid. And there were many people there, a crowd, swelling in the hate, the ugliness. And I was foreign to myself then, as I stood amongst the people holding their signs, yelling. I don't know what I wanted, but a woman in a hijab stepped past me and I clutched at her arm. It was my mouth, but it was not my voice: "What did you people do to my brother?"

And I cried, and I thought I would never stop. I was afraid that the hatred would eat me from the inside. The woman's name was Afan. She lost her aunt and uncle in Paris. They were Syrian refugees living in France. She told me that she understood.

I don't understand how to reconcile this pain of being. I will never see my brother, Jack, again. And I will never be the same. Afnan forgave, but I don't know how. I don't know how to understand when there is so much that is senseless. But I want to be different, and I want to be OK.
```

---

## IC-0234: The Patient

- Title: The Patient
- Author (byline): Louise Heck-Rabi
- Work: More Monologues for Women, By Women
- Publisher: Heinemann Educational Books
- Publication date as stated: August 1996
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SUSANNAH
- Teaser before the introduction: No
- Spoken words (computed): 1884
- Already set (do not supply): none

### Source block (context only)

```text
Author: Louise Heck-Rabi
Book: More Monologues for Women, By Women
ISBN: 978-0435070229
Publisher: Heinemann Educational Books
Date (Month/Year): August 1996
```

### Introduction (context only: never use it for content warnings)

```text
Until 1968 the use of the term “race riot” in the United States referred to race riots which were often a mob action by members of the majority racial group against people of other races. In the late 1960s the term Race Riots came to describe riots involving large numbers of members of racial minority groups. Physical aggression was often aimed at neighborhood business, government representatives and law enforcement agencies perceived as unfairly targeting racial groups. The National Advisory Commission on Civil Disorders (the Kerner Commission) reported 130 separate race riots in the summer of 1967—initiated by blacks in response to police brutality, poor housing, no jobs, and exclusion from the benefits and promises of American life. It became a true revolution of rising expectations. In the Patient by Louise Heck-Rabi, a young girl, recounts the events leading up to her involvement in one such riot. Meet Susannah Lynn, who speaks to us from her room in a mental hospital. When you hear her story, you will understand why. The Patient by Louise Heck-Rabi
```

### Performance text (classify this)

```text
SUSANNAH: Miz Lydia's house looked good from the alley. Its backside better than the picture of the Courthouse downtown. White, tall up into heaven, clean and good-smelling as the laundry I delivered twice a week in my wagon. The Askew family wash was a precious cargo worth two or three dollars. Ma had a sign in front of our house: WASHING AND IRONING. She boiled the clothes and beat them with the paddle she used on us. She could iron fast! Nine white men's shirts, long sleeves, in an hour.

Miz Askew liked Ma’s work. She like me first time she saw me on the veranda off the kitchen, waiting till the housekeeper counted pieces, me wondering 'bout that smell of molasses just baked and warm. I skipped to the veranda corner finding three pans laid out to cool. Raisin-face cookies. Staring and hoping to steal-"What is your name, child?" I turned like a top, bent my knees like Ma said, and looked up at her. "Susannah Lyme. Ma'am." She was the cleanest, coolest looking lady I'd ever seen. "How many are there at home?" she asked, putting my name after it, "Susannah," like it was special. I lied. "Five," I said, looking at the cookies. The housekeeper come out the door with three dollars in her hand. "Fanny, please. You will give Susannah seven cookies to take home." Fanny gave me the dollars and a hard look, then went back in, letting the screened door slam this time.

"I am Mrs. Askew," she told me what I already suspicioned. I made half a curtsey. "Yes, Ma'am." The bag in Fanny's hands crackled with the cookies' weight. "How old are you, Susannah?" she asked next. "Twelve," I spoke up, "Miz Askew." My middle grew tight like it did before tests in school. Still, I felt good with her. We stood there awhile just looking at each other till Fanny folded the top of the bag and cleared her throat. Miz Askew thanked her. I got the cookies. And still she considered me like I was something special she could figure out with her china-blue eyes. "On Saturdays, sometimes on Sunday afternoons, I give large dinner parties. Please ask your mother if you could help at table and with Fanny in the kitchen." Even before she finished I blurted out, "Oh, Miz Askew! I'm sure it'll be alright! So long as it don't interfere with my schoolin'." She smiled then and so did I. "You will ask her permission?" Those words soft as dandelion fluff under the smile. I nodded. "Yes, Miz Askew." She turned. So did I. Almost forgot! "Thank you for the cookies, Miz Askew." She really smiled then. "Please tell your mother that you were given two instead of one, as a reward for your work in pulling the wagon." Her face didn't change. I knew we had a special understanding. And I would die if Ma didn't let me wait table for her. Ma did. But I couldn't fall behind in my homework because of my jobs. I still had to deliver laundry on weekdays. But every cent I earned went into my very own bank account. Imagine! An education fund! Ma said I was the best learner in the whole school, about as smart as Waldo, her oldest, never saw him till I was in college.

Waiting table at the Askew’s made living easier. I took home food and clothes that didn't fit. I took home memories of seven course dinners for twenty guests lasting three hours. Fanny and the rest of us could do without Mr. Askew, a red-faced ox with heavy feet and heavier voice. Miz Lydia said we could call her that. She called me Sukey, saying it suited me. We marveled at her powers of sweetness to endure him. He'd put you straight if the soup was cool! We hated him. Loved her. Those were the best years of my life, so busy I could hardly feel the seasons changing on my face. I sang in the choir, I played a maid in the Senior play. I was elected to the National Honor Society. I was cheerleader, I helped Ma wash and iron clothes, yet I treasured most my hours with Miz Lydia. I deposited my money in the bank (Ma wouldn't let me take any out). I was going to college-at least for a year. I would have to work, but I was used to it. I wanted to be somebody, wanted to raise Ma up out of that cellar, away from the copper boiler forever. But I was afraid to leave Ma and Miz Lydia. I couldn't fathom how I would live without those four o'clock Sunday dinners where the race question was discussed when I was in the pantry or the kitchen, and hushed when I came in. But I heard plenty!

Miz Lydia kept tellin' me I was tops. She wrote letters of recommendation. She said I could be anything I wanted to be, if I sought it and fought for it. She meant working, studying, praying, not messin' around on the front porch on warm spring nights. She meant not having boyfriends like Doremus and Geneva, she meant ignoring the hoot-calls of every man any color who looked you over in the street.

A leather-bound address book with the address of the Askew’s written in it, and a five dollar bill was my goingaway-to-college gift. Miz Lydia gave it to me herself. She looked confused, her eyes clouding up, but still smiling. She took both my hands. "Remember me, Sukey. This door (it had to be the back door, I knew that) is open to you, always. Write to me. Come if you need work or help. My hands are tied in many ways (that was the ox, Mr. Askew, Lord-of-the-Manor, Nigger-hater, who knew Negroes, including me, hated him). There are times when I cannot do as I choose." I mum-bled thanks, stumbled down the steps, my legs too long for the sidewalk. Too long for the undersized desks in the classrooms of Belmont College, one of those all-black little Southern institutions, trying its best, oh Lord, to educate. I worked in the Library. I lived in a room. I studied. Everything came easy. My straight A’s put me on the Dean's List. I clipped the List from the paper and mailed it home to Ma. I might get a tuition scholarship! I was lonely and homesick, but ready for new worlds.

At student mixers I chewed chips, drank beer, got absorbed in discussions of politics, pacifism, civil rights. I attended forums, rallies, symposia. I read about the riots, the Mississippi murders, I boarded the College bus one Friday to go to a sit-in at the Public Library the next two towns over, where stand-up only service was the rule for Negroes. My first taste of violence was the ice water from the firehoses aimed at us. The local jail was crowded and too small, our sentences light, all of us back to Monday classes like nothing happened. I never wrote Ma or Miz Lydia about my adven-tures, I did write about my job, my profs, about Neal, his friends who organized bus rides to march with banners in D.C. picketing Air Force bases and submarine launchings. My own participation much less-I had to work! I promised Neal I'd demonstrate at home on Easter vacation, for open housing. We heard rumors of real trouble-but Neal claimed, "Always rumors, doll. Don't believe it!" Doremus and Geneva said No when I asked them to demonstrate with us. And meet Neal. I walked alone to the Church basement, seeing the College bus in the parking lot. We got instructions. Neal's words were, "March and sing at the home of the Housing Commissioner." I held a banner and his hand.

Oh No! Not that beautiful white Georgian-style mansion I knew so well! I couldn't walk. I stumbled, swayed. The police watched us. We circled outside that tall iron fence, singing the words Neal had written to the tune of "Dixie." They say they will never know who threw the firebomb that exploded at the front door. Pow! Like that. Seems everybody was just waiting for that sound to let loose, to rampage like animals from opened cages, a signal to throw our candles toward the house, to push through the closed gates, scale the fence, to scream. More explosions-what were they?-shattered my ears. No, no, not this house, not even if old ox-faced Askew was Housing Commissioner! "What's the matter, Sukey? Get with it!" Neal yelled. He rushed me along, police closing in on us, some on horses. I smelled smoke. The house was burning! Staring, I saw servants' faces framed in the windows with flames behind them.

Oh, Miz Lydia! I am your Sukey! Do you understand? Do you know I'm not to blame? Brick throwing started. Why? Neal dragged me down. In an ocean, surging, Neal and I, in a body-pressed wave swirling to that pillared veranda double front doors, wood a-smoking, windows smashing. Miz Lydia, where are you? It was Monday. No dinner in the oval dining room for twenty guests today! Run our, Miz Lydia! Go out back! Won't see you! Let old ox-face get his due, but not you! Please, God! Not you!

Crack! A pistol shot stunned the air, stopped Time, as if the voice of God had spoken one holy word. "Look!" Neal pointed, with pride, "That white bastard's shot!" Snowflakes melted in my open mouth, my eyes stuck on old Ox-face himself, in the shrubs at the side of the house! Askew trying to run away! Like flies buzzin' a wave surged toward him, police swinging billy sticks, horses' hooves making muck of the Askew lawn. "Some screwball's got a gun!" someone shouted. I screamed. There was my Miz Lydia! Cool and clean like always, running out from that veranda side door pulling on her coat, dipping her chin against thickening snow. Did she see ox-face? Did the rage of the mob scare her? She paused as if deciding these questions, then ran. I called out to warn her, "Miz Askew! Go back! Miz Askew! Go back!" Her face turned-did she hear me?-Neal turned, angry, astonished. Crack! She fell in a heap! My arms stretched out to her, dropped from my sight by a shot from an anonymous pistol! "I've got to help her! Let me go! I've got to get to Miz Lydia!" I shouted. Neal held on to me. I wrestled him, broke free, struggled through the smell of sweaty bodies, forced myself into the ring of black bodies leaning over her, not helping. Oh God! Let me die so she can live! I struggled closer just as cops rode closer, billy sticks swinging. I held both her hands, blood from her back, when the first blow swished my head. I screamed so hard I could not close my mouth. On my knees I cradled her, the next blow hit harder, blood trickling from my chest. I'm sorry, Miz Lydia, I'm sorry, I whispered in my own echo chamber, I didn't know, I didn't know, I hurt, I hurt! Oh please God, let me die so she can live! Oh please God, let me die so she can live!
```

---

## IC-0235: Patient A

- Title: Patient A
- Author (byline): Lee Blessing
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: KIMBERLY, CDC
- Teaser before the introduction: Yes
- Spoken words (computed): 1199
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lee Blessing
ISBN: 978-0822213642
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
Out of the nearly 200,000 people who have developed AIDS in the U.S., only five are known to have been infected by a health-care worker. Epidemiologists quickly point out that all five cases can be traced to the same Florida dentist, David Acer. But the fact remains that it did happen, despite the odds and with devastating results. One of Acer's patients, Kimberly Bergalis, ultimately died of AIDS related complications. Her plight and her understandable fury have moved millions to feel insecure when they go for teeth cleaning or an annual physical exam.

Today, nearly 6,800 health-care workers in the U.S. are known to have AIDS -- including 170 dentists and dental hygienists, 730 physicians and more than 1,450 nurses. Should they tell patients? Should they get out of medicine altogether?

Patient A by Lee Blessing is based on this very real social issue as told through the eyes of Kimberly Bergalis.
```

### Performance text (classify this)

```text
KIMBERLY: For those of you who don’t know who I am- my name is. . . was. . . Kimberly Ann Mary Bergalis. I’m using the past tense by the way, out of respect for myself. The whole ordeal began quite innocently. In the middle of my junior year at the University of Florida, I had to have two back molars removed by Dr. Acer. While it was an involved appointment, I don’t remember much about it that was unusual, besides that it hurt. I did not know that less than four years later, I’d be dead.

KIMBERLY: I started to feel sick in spring of 1989. I went to a hematologist. They took blood, ran a lot of tests- no HIV test, though. I began to have problems breathing. I went to a hematologist/ oncologist, who examined me for cancer. I didn’t have cancer. The doctors wondered if I was just hyperventilating. Our local doctor diagnosed me with bilateral pneumocystis pneumonia and had me hospitalized. Oh, yes---For the first time I was tested for HIV. Five days after I turned twenty-two, the results came back positive.

The doctor gave me some time alone, before my folks came in. I began to cry. I looked out the window, and the clouds were moving against the sun, swirling. I heard a voice that said it would all be ok. That everyone in the family would be able to handle it. And I opened my eyes and no one was in the room.

My mother was the first to come in. She talked about her own parents, who’d been killed years before in a car accident and how they’d be waiting in heaven for me, along with Grandma Zebleckas and even their dog that died, too. I think if she could have put everything that ever lived into heaven for me in that moment she would have. When we’d calmed down, my father came in. That was harder. He shook and he cried.

“Oh my God, no. No, please. . . Put your head on my shoulder. . . It’s gonna be ok. We’re gonna get through this.” He kept saying it had to be a mistake, that he didn’t believe it, that it can’t be. It just can’t be.

“Dad, it is.”

My case was reported to the state agency and also to the Centers for Disease Control in Atlanta. They couldn’t figure out how I’d been infected. I didn’t have any of the usual risk factors. I hadn’t had any transfusions. I wasn’t a drug user or hemophiliac. They ended up asking about some pretty unusual things.

CDC: How many people have you had intercourse with?

KIMBERLY: None.

CDC: I’m talking about sex, now. Sexual-

KIMBERLY: None. (beat) They had a hard time believing that I’d never had intercourse. It was my mother who first thought of Dr. Acer. There’d been rumors about him. Some people thought he had AIDS. So we mentioned it to the CDC. I was never told they were investigating the dentist.

Seven months after I was diagnosed, Jane Pauley had a message for me on the evening news. A young woman in Florida had in all likelihood been infected with HIV by her dentist. No one had called to tell me this would be on. This was the first moment I realized they’d been lying to me all along- staring me right in the eye, knowing I had a disease that was going to kill me, and refusing to tell me the truth.

You don’t know what to think when you’ve got this disease. The best experts in the country can’t tell you how you got it. Meanwhile, you’re hiding it from as many people as possible, you’re going through a kind of terror you’ve never known, you feel guilty. You feel as you somehow betrayed your family, because you see their pain. And you yourself- somehow you betrayed yourself. You failed to take care of yourself. But how? How?

I was called Patient A, since my name was off-limits. Then two of Dr. Acer’s other patients tested positive and we had Patients B and C. It felt insulting. As though they’d decided never to speak my name again.

I think the insurance company really thought about going to court until the other two patients were discovered. After that, the company agreed to a million dollar settlement.

This was a relatively good time for my family. We were suddenly famous. we’d won this big settlement, and I was still to have a lot of good days physically.

I did get to do a few things I had never done before. I got to ride in a hot air balloon in Palm Springs. That was the best. Floating, for a few minutes, it seemed like a different planet. I started to imagine who might live down there. Maybe it was people who were not greedy, not vicious, not afraid. Maybe they felt pain when others suffered, joy when the others succeeded. Impossible people, walking gracefully beneath the palms, ] grateful just to be walking there at all. Then suddenly the balloon made a jump, and I looked up and thought, “Here I am suspended above my dreams by nothing more than heat.” It felt like riding in the hand of God-- that gentle, that terrifying. And somehow I knew that wherever that hand took me, frightened as I was, it would never let me go.

I called a few people bastards before I died, and frankly I don’t regret it. I resented what the dentist did, but more than that I resented the authorities who told him he had a right to keep practicing and keep his secret. After all, when you die for a public health policy, I think you have the right to question it pretty strenuously.

Not long after floating in the balloon, I took a turn for the worse. Hospital, transfusion---When I left the hospital this time, I started keeping a diary on tape. I’d lie on the coach all day making tapes. Sometimes, I’d talk to my sisters. Allison held up really well, but Sondra cried a lot. She was only eleven. I would have to think of things to cheer her up.

In the end, I was afraid to go to sleep, because I was afraid I wouldn’t wake-up.

My Mom brought up a good point. She said, “Why are you so sure that it’s not going to get any worse?” And that’s something I never thought about. I just thought how I can’t take this pain anymore, and how I want to be out of my misery before it gets worse. So that made me think. I started thinking about the cemetery where I was going to be buried, and all the names-

• And how I am going to lie right next to my Grandmother on the top of a mountain—

• And how I am going to lift up and just fly away into the heavens.

• And how God’s going to come down and take my hand---

• And how my body’s just going to be this thing I used while I was on this Earth.

• And then a peace came over me and I was finally able to sleep.
```

---

## IC-0236: People, Places and Things

- Title: People, Places and Things
- Author (byline): Duncan Macmillan
- Work: Not specified
- Publisher: Oberon Books
- Publication date as stated: March 2016
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DOCTOR, EMMA, THERAPIST, MEREDITH, TOGETHER AS GROUP, LAURA, PAUL, MARK
- Teaser before the introduction: Yes
- Spoken words (computed): 1666
- Already set (do not supply): none

### Source block (context only)

```text
Author: Duncan Macmillan
ISBN: 978-1783199099
Publisher: Oberon Books
Date (Month/Year): March 2016
```

### Introduction (context only: never use it for content warnings)

```text
Recovery from an addiction is a journey between life and death that can only be walked one day at a time. Life has to win every single day. And death only has to win once. People, Places and Things by Duncan Macmillan
```

### Performance text (classify this)

```text
DOCTOR: (Pg 24-27) Nina? Nina? (No response) Excuse me, hello.

EMMA: (jittery, nervous, obviously under the influence) Sorry. Yes, that’s me.

DOCTOR: Great. (reviews the intake form) Your name is ‘Nina” and you’re an alcoholic and drug addict.

EMMA: This was a mistake.

DOCTOR: You’re not an alcoholic and drug addict?

EMMA: I’m not saying I’m anything. I just want to get clean, get my certificate and go back to work.

DOCTOR: Certificate?

EMMA: A piece of paper or a signed whatever, something that says I can work. That I’m not a risk.

DOCTOR: Once you complete the grogram we can . . .

EMMA: (interrupting) How long will that take?

DOCTOR: It varies. First, I’ll need to see your results and take a history and psychological examination. (consulting the form) Benzodiazepine, Lorazepam.

EMMA: Valium, yeah. For anxiety. It’s a prescription.

DOCTOR: Detoxing from benzos takes about ten days. You’ll start tonight and tomorrow morning you can begin with Group.

EMMA: I don’t need that; I just need the first thing.

DOCTOR: Nina, the Group is the program. The truth is that it doesn’t take long to get everything out of your body. It’s the behavior that is the important thing to address. We can’t do that until we’ve dealt with the physical symptoms. Then it’s twenty-eight days of therapy. Ideally, it’ll be closer to ninety.

EMMA: Ninety? No, that’s not possible.

DOCTOR: Blackouts . . . Memory loss . . . It says here ‘suicide attempt.’

EMMA: Not a successful one. That’s me. Never seeing anything through. Violin lessons. Diets. Suicide attempts. I never finish what I start.

DOCTOR: Your addiction will fight any progress. It’s a parasite and it will fight for its own survival until you’re dead. But progress is possible. I just need to hear you say that you are willing and motivated to make changes.

EMMA: I know that the next time I drink or use that’ll be it. I’ll be dead. I’m not sure if I knew that until now, until I just literally just said it. But it’s true. It’s going to kill me. (She rubs her eyes) Yes. I need help. Please help me.

DOCTOR: (Pg 39-40) The program works for a lot of people. (Pg 27) Let’s start with your name shall we? Your real name.

EMMA: Emma. (cynical) (Pg 39) If it’s vital to my recovery that I come to believe in a power greater than me – to turn my will and my life over to God and have Him remove my defects of character – if all this depends on me having a spiritual awakening, then we might all just be wasting our time.

DOCTOR: You’re worried about the steps.

EMMA: I’m worried that a trained medical professional can also wear a crucifix.

DOCTOR: I don’t believe the scientific methods disproves the existence of . . .

EMMA: (bitterly interrupting) Of course it does. I really need you to be cleverer than this. Otherwise, I’m going to leave. I’m not powerless. I’m not helpless. I don’t believe addiction is a disease and I’m scared and angered by the suggestion that from now on it’s either eternal abstinence or binge to death. I can’t surrender to a higher power because there isn’t one. There just isn’t. My brother had a brain hemorrhage while reading Pinocchio to a group of five-year-olds. Mark. Hew was two years younger than me and never touched drugs or alcohol. He ran marathons. For charity. I should have died a thousand times, but it was him.

DOCTOR: When did you start using, Emma? (Pg 37) Before you join the Group I need some historical context for your using.

EMMA: (Pg 40-42) If I tell you I was sexually abused or the child of alcoholics, if I tell you I returned from back-to-back tours of Iraq and started to self-medicate; is that the kind of thing you want to hear?

DOCTOR: Is it the truth?

EMMA: No. I never had a brother. And he didn’t die in front of children. He died in his car. Or he was stillborn maybe. Or he grew up and died of old age.

DOCTOR: Do you lie to protect yourself or your addiction?

EMMA: I can’t base my survival on slogans and abstractions and vagueness. I’m not someone who can do Pilates on a beach and mistake relaxation for spirituality. I spent a year in the Far East, but I didn’t find enlightenment, I found slums and sex tourism. I need something definitive. I need to be fixed.

DOCTOR: It doesn’t work like that. It’s a long-term, daily . . .

EMMA: I don’t do long-term.

DOCTOR: You’re going to learn. The strategies you’ve been using just aren’t working. Intellectually inferior as I may be, I’m trying to save your life. Now, sit down. (Emma sits) The Twelve Steps outline the process of recovery. Have you heard the expression “powerless over nouns’?

EMMA: Nouns? As in

DOCTOR: People, places and things. It’s a rewrite of Step One of Twelve. Instead of declaring ourselves powerless over alcohol or drugs, we admit that we are powerless over people, places and things. People who make us want to relapse, places we associate with using and things that reactivate old behavior. When you’re in recovery

EMMA: Back in the real world.

DOCTOR: You’ll need to find a way to handle being in those places, with those people.

EMMA: And those things. I find reality pretty difficult. I find picking up my phone to be a mammoth struggle. The friends who won’t see me anymore. The bombings and beheadings, the moral ambivalence you have to have to just be able to carry on with your day. Drugs and alcohol have never let me down. There are substances I can put into my bloodstream that make the world perfect.

DOCTOR: I can’t force you to stay. I can’t force you to be truthful. I can tell you that the process only works if you are honest. With yourself, with me and with others. Denial is what kills you. (beat) You’ve already come so far Emma. Don’t let that be for nothing. I’d like you to meet the Group. ****** GROUP THERAPY*****

THERAPIST: (Pg 43) Hi. I’m Lydia, one of the therapists here. Why don’t you introduce yourself?

EMMA: Er, okay. Hello everyone I’m . . . Emma.

MEREDITH: (Pg 54) I’m Meredith and I’m a Heroin addict.

TOGETHER AS GROUP: Hello, Meredith.

LAURA: Hello, I’m Laura. I’m an alcoholic.

TOGETHER AS GROUP: Hello, Laura.

THERAPIST: (Pg 43-44) Emma, why don’t you tell us about yourself?

EMMA: Seriously? I have to just jump straight in? (Pg 45-47) (Suddenly the door opens and Paul enters, urgently)

PAUL: I’d like to say something to the Group please.

THERAPIST: Mr. Waverly, I’m sorry but your treatment has been terminated. You can’t be in here.

PAUL: (takes a piece of paper from his pocket and reads) I want to apologize to you all with my whole heart. I know that my behavior here was stupid and dangerous. I smuggled in some substances. Ketamine. (he lowers the paper – this is hard for him) But I don’t’ like begging. I was making progress here. I was doing well. Please. Please give me a second chance. I wouldn’t have used if what happened hadn’t happened.

EMMA: What happened?

PAUL: Robert. My fiancé. My partner of eighteen years. Dead. Heroin. I can’t go home again. It’s not real. I don’t want to die. I want it all to stop.

EMMA: (Pg 48) I’m sorry your fiancé died. My brother died too. The week before I came here. Pills. I found him in the stairwell of our building curled into a ball. He cried blood. I wish I’d died instead. I wish I’d died without having to see him dead. We’re the same.

THERAPIST: Paul, you understand you can’t simply re-join the Group.

PAUL: (looks around, laughs bitterly) None of this is real. When you’re sitting here tonight being all serious, think of me out there. I’ll be having the night of my life. (Paul leaves, beat)

THERAPIST: (Pg 55) Would you like to speak to the Group Emma?

EMMA: No.

MARK: (steps up to fill the silence) (Pg 54) [Hello, I’m Mark] I’m a drug addict. (Pg 58) Amends. That’s the hardest part of this whole thing. I can’t forgive myself for a lot of things, so I can’t expect other to. My eldest sister, she was pouring a bottle of Smirnoff down the sink. Vodka to me was like spinach to Popeye. I didn’t know my own strength. I broke her jaw then stamped on her leg, broke her ankle. She forgave me. (he is finding his hard; beat) My gran. She raised me. Cancer. She was in pain and I (big breath in an out, trying to keep his composure) I took her pain relief. I’d hear her calling out. Screaming. And I’d be like ‘sorry Nan. There’s nothing left.’ Now she’s dead so how do I amend for that?

EMMA: (Pg 60-61) (softly) Hello. I’m Emma. I’m an alcoholic and drug addict.

MARK: I’ve seen you onstage a few time. I remember thinking, she’s going to be great.

EMMA: I used to think that too. With a play you get instructions. Stage directions. Dialogue. Someone tells you where to be and when. You get to live the most intense moments of a life over and over again. You get to practice. For weeks. And you’re applauded. Then you leave through stage door. Back to real life. Audition comes in. Never hear back. You try not to take it personally. But you keep going because sometimes, if you’re really lucky, you get to be onstage and say things that are absolutely true, even if they’re mad-up. You get to do things which feel more real to you, more authentic, more meaningful than anything in your own life. You get to speak poetry . . . (From Antigone) When he shall die, take him and cut him out in little stars, and he will make the face of heaven so fine that all the world will be in love with night, and pay no worship to the garish sun. I played Antigone and every night my heart broke about her dead brother. Then my own brother died and I didn’t feel anything. I’m not avoiding talking to the Group because I’ve got something to hide. It’s the opposite. If I’m not in character, I’m not sure I’m really there. (Pg 63) I’m brilliant at being other people and totally useless at being myself. (Pg 61) I’m nothing. (long beat) (Pg 64) (with growing anger) I’d like to believe that my problems are meaningful. But they’re not. There are people dying of thirst. People living in war zones and here we are thinking about ourselves. As if we can solve everything by confronting our own defects. We’re not defective. It’s the world that’s f****ed. (She steps out of the scene and speaks to the audience) (Pg 60) (softly) Hello. I’m Emma. I’m an alcoholic and drug addict. (Pg 87) (sadly) In rehab they tell you: avoid people who make you want to relapse. Places you associate with using and objects that might be a trigger. People, places and things. That’s basically, you know. . . everything.
```

---

## IC-0237: A Perfect Ganesh

- Title: A Perfect Ganesh
- Author (byline): Terrence McNally
- Work: Love! Valour! Compassion!
- Publisher: Plume Drama
- Publication date as stated: May 1997
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: KATHERINE, MARGARET
- Teaser before the introduction: Yes
- Spoken words (computed): 938
- Already set (do not supply): none

### Source block (context only)

```text
Author: Terrence McNally
Book: Love! Valour! Compassion!
ISBN: 0452279305
Publisher: Plume Drama
Date(Month/Year): May 1997
```

### Introduction (context only: never use it for content warnings)

```text
Katherine and Margaret are both traveling to India, in search of some kind of spiritual release; Katherine from the guilt she feels over her son's death and Margaret from the fear caused by a lump she has discovered in her breast. The two go back a long way, as can be seen in this scene where Katherine does her best to combat Margaret's fear of flying. A Perfect Ganesh by Terrence McNally.
```

### Performance text (classify this)

```text
Characters: Katherine and Margaret (50s) two friends traveling together to India.

Scene: An airplane bound for India

KATHERINE: Does he remind you of Walter?

MARGARET: The steward? Not in the least.

KATHERINE: I didn't know you were afraid of flying.

MARGARET: I've flown over this part of the Atlantic this time of the year at least fifteen times and it was never like this.

KATHERINE: Actually, I like a little turbulence.

MARGARET: You're the type who would.

KATHERINE: It lets me know we're really up there. If it gets too quiet and still, I worry the engines have stopped and we're just going to plummet to the earth.

MARGARET: Can we talk about something else?

KATHERINE: Do you want to hold my hand?

MARGARET: Of course not.

KATHERINE: Do you want some gum?

MARGARET: Is it the kind that sticks to your crowns?

KATHERINE: I don't know.

MARGARET: If it's the kind that sticks I don't want it.

KATHERINE: You're out of luck. It must have been in the bag I left in the terminal.

MARGARET: What's that?

KATHERINE: A whistle. George made me take it. In case we get in any sort of trouble in India, I'm supposed to blow it so help will come. "Who?" I asked him. "Sabu on an elephant?"

MARGARET: Will you keep your voice down? (The plane heaves, extra-mightily this time.)

KATHERINE: This is ridiculous. Give me your hand.

MARGARET: We're all going to die.

KATHERINE: Just shut up and say a "Hail, Mary."

MARGARET: Methodists don't say" Hail, Mary."

KATHERINE: We're going to be all right.

MARGARET: Ow! That's too tight! (The turbulence subsides.)

KATHERINE: See?

MARGARET: I can bear anything as long as I know it's going to end.

KATHERINE: Remember the last year we went to St. Kitt's?

MARGARET: The men got sick from eating crayfish.

KATHERINE: They were langouste.

MARGARET: They looked like crayfish.

KATHERINE: That's not the reason I never wanted to go back there.

MARGARET: Alan nearly died. Besides, it was a time for a new island.

KATHERINE: It was the incident with the little plane.

MARGARET: What incident? I don't remember.

KATHERINE: Yes, you do. We were swimming in front of the hotel. A small, single-engine plane had taken off from the airport. The engine kept stalling. No one moved. It was terrifying. That little plane just floating there. No sound. No sound at all. Like a kite without a string. I don't think I've ever felt so helpless.

MARGARET: I remember.

KATHERINE: Finally, I guess the pilot made the necessary adjustments, the engine caught and stayed caught and the little plane flew away, as if nothing had happened, and we finished swimming and played tennis and after lunch you bought the Lalique vase I could still kick myself for letting you have.

MARGARET: You've envied me that piece of Lalique all these years? It's yours.

KATHERINE: I don't want it.

MARGARET: Really, I insist, Kitty. I think I only bought it because I knew you wanted it. That, and I was mad at Alan for some crack about how I looked in my new bathing suit. The plane's stopped jiggling. Smooth as glass now.

KATHERINE: I've thought about that little plane a lot. Maybe we were helpless. May be we weren't responsible. Maybe it wasn't our fault. But what kept that plane up there? God? A God? Some Benevolence? Prayer? Our prayers? I think everyone on that beach was praying that morning in their particular way. So maybe we aren't so helpless. Maybe we are responsible. Maybe it is our fault what happens. Maybe, maybe, maybe.

MARGARET: Do you want to give me my hand back?

KATHERINE: I'm sorry. Thank you. Did I do that? I was holding tight! I'm sorry. (She kisses Margaret's hand.) What happened to your liver spots? You used to have great big liver spots.

MARGARET: Will you keep your voice down? I keep begging you to come with me. The man's a genius. And it's paradise there.

KATHERINE: And it costs three thousand dollars a week. I'd rather go to India for my soul than some spa in Orange County for the backs of my hands.

MARGARET: Happily, you can afford both.

KATHERINE: I keep thinking about Walter.

MARGARET: Why would you do that to yourself?

KATHERINE: I can't help it.

MARGARET: Well, stop. Stop right now. Think about something else. Think about the Taj Mahal. Think about India.

KATHERINE: They say it's like a dream, the Taj Mahal.

MARGARET: I hope it's not like the Eiffel Tower. All your life you look at pictures of the Eiffel Tower and then when you actually see it, it looks just like the pictures of it. There's no resonance when you look at the Eiffel Tower. I'm expecting some resonance from the Taj Mahal. I'll be terribly disappointed if there isn't any. You're humming again, Kitty.

KATHERINE: I'm sorry.

MARGARET: You asked me to tell you.

KATHERINE: All of a sudden, I can't remember when it was built!

MARGARET: It was begun in 1632 and completed in 1654.

KATHERINE: All that reading up on it and for what?

MARGARET: Do you remember who it was built for?

KATHERINE: Of course I do. Someone's wife.

MARGARET: Everyone knows that, Kitty. What was her name?

KATHERINE: I knew you were going to ask me that. Marilyn? Betty? Betty Mahal? I know who built it. Shah Jahan.

MARGARET: The favorite wife was Mumtaz Mahal.

KATHERINE: Mumtaz, of course! It was on the tip of my tongue.

MARGARET: It took twenty-two years and twenty thousand workers to build.

KATHERINE: Is this going to be some sort of pop quiz?

MARGARET: I was trying to get your mind off Walter.

KATHERINE: Nothing will ever get my mind off Walter.

MARGARET: This is a wonderful start to a trip!

KATHERINE: I'm sorry. (She hums a little.)

MARGARET: Kitty, sshh!, you're doing it. It's nobody's fault. (Katherine begins to read from a travel brochure she has taken out of her purse.)

KATHERINE: Now listen to this. (She reads.) "Don't drink the water, which means absolutely no ice in your drinks or eating of washed fruits and vegetables." Sounds charming. "Above all be patient. Allow, accept, be."

MARGARET: That's what I've been telling you.
```

---

## IC-0238: Petals in the Wind

- Title: Petals in the Wind
- Author (byline): V.C. Andrews
- Work: Not specified
- Publisher: Pocket Books
- Publication date as stated: Nov 1990
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CATHY, CARRIE, CHRIS, DR. SHEFFIELD
- Teaser before the introduction: No
- Spoken words (computed): 1577
- Already set (do not supply): none

### Source block (context only)

```text
Author: V.C. Andrews
ISBN: 978-0671729417
Publisher: Pocket Books
Date (Month/Year): Nov 1990
AWARD
Utah State Finalist – DI - Female
```

### Introduction (context only: never use it for content warnings)

```text
How young we were the day we escaped. How exuberantly alive we should have felt to be freed, at last, from such a grim, lonely and stifling place. How pitifully delighted we should have been to be riding on a bus that rumbled slowly southward. But if we felt joy, we didn't show it. After all, it took the death of Cory, Carrie’s twin to give us the courage to escape. And now we sat, all three, pale, silent, staring out the windows, very frightened by all we saw.

Petals in the Wind by V.C. Andrews
```

### Performance text (classify this)

```text
CATHY: We were the youngest on the bus. Chris was seventeen years old and strikingly handsome. Curled up on my lap was my younger sister. She didn't look older than three, but she was eight years old and small, so pitifully small, and weak. In her large, shadowed blue eyes fingered more dark secrets and sufferings than a child her age should know. And me: I was fifteen and sat tense, ready to scream if one more bad thing happened.

CARRIE: Cathy, I don't feel so good. My stomach, it feels funny...."

CATHY: I was seized by fear. Her small face seemed unnaturally pale; her hair, once so bright and shining, hung in dull, lank strings. Her voice was merely a weak whisper. Violently Carrie jerked upright and began to choke and retch.

Carrie began to whimper and tremble. I felt her forehead and it was clammy, and now her face wasn't just pale, but white! I prayed that just once God would have some mercy on us. While I hesitated with the squeamish desire to vomit myself, Carrie let go again. I couldn't believe she had anything left. I sagged against Chris while Carrie went limp in his arms and looked heartbreakingly near unconsciousness.

CHRIS: I think she's going into shock. Cathy, we've got to get Carrie to a doctor, and soon!"

CATHY: "Look here, driver," yelled the meanest man on the bus. "Get that sick kid to a hospital! Damned if I paid my good money to ride on a stinking bus!"

And thank God, the driver listened. Soon we were rolling along quiet, wide streets with trees that arched gracefully overhead. Really, they didn't put medical buildings on this kind of residential street. But just as I was beginning to get worried, the bus jerked to a sudden halt in front of a big white house perched on a low, gentle hill and surrounded by spacious lawns and flower beds.

Chris very gently, and with a great deal of tenderness, lifted Carrie in his arms. We walked up the long brick walk to the front veranda and there I hesitated. To the right a small sign read DR. PAUL SHEFFIELD: FOR PATIENTS ONLY. This was obviously a doctor who had offices in his own home. I scanned the veranda to spy a man sleeping in a white wicker chair. Slowly we approached.

CHRIS: Are you Dr. Paul Sheffield?

CATHY: Carrie lay in his arms with her neck arched backwards, her eyes closed and her long golden hair waving in the soft, warm breezes. Reluctantly the doctor came awake.

DR. SHEFFIELD: Yes, I'm Dr. Sheffield.

CATHY: He rose to his feet and stepped closer to peer down into Carrie's small, white face. He parted her closed lids with forefinger and thumb.

DR. SHEFFIELD: How long has this child been unconscious?

CATHY: He then led us to the door for patients only. Full of a thousand anxieties, Chris and I backed up against a wall and watched as the doctor checked Carrie's blood pressure, her pulse, her temperature and listened to her heart, front and back. My clothes felt damp and miserable, and suddenly I remembered why. Quickly I turned to unzip and remove my filthy outer skirt.

DR. SHEFFIELD: Do you always wear more than one outfit on Sundays?

CATHY: Only on the Sundays I run away. Chris nudged me sharply, mutely signaling I was revealing too much.

DR. SHEFFIELD: Sooo, you three are running away. And just what are you running from?

CHRIS: It's a long story, Doctor, and right now all we want to hear about is Carrie.

DR. SHEFFIELD: So we'll talk about Carrie. I don't know who you are, or where you're from, or why you feel you have to run. But that little girl is very, very ill. I suggest you contact your parents immediately.

CATHY: Just the words to make me panic!

CHRIS: We're orphans. Now, tell us what you suspect is wrong with our sister, and what you can do to make her well again.

DR. SHEFFIELD: Hold up there young man. First you have to answer a few questions. First, what is your name?

CHRIS: I am Christopher, and this is my sister, Catherine, and Carrie is eight years old, whether or not you believe it!

DR. SHEFFIELD: Now look. Let's stop being suspicious of one another. If you really want to help your sister, you have to give me the truth, or else you're wasting my time and risking Carrie's life.

CATHY: We were so scared, so damned scared to speak the full truth -- for who would believe? We'd trusted those who were supposedly honorable before so how could we trust again?

DR. SHEFFIELD: All right, if it's that difficult, let me ask more questions. Tell me what all three of you ate last.

CHRIS: Our last meal was breakfast very early this morning. We all ate the same thing, hot dogs with everything, french fries dipped in catsup, and then chocolate milkshakes.

DR. SHEFFIELD: And all three of you ate exactly the very same things for breakfast? And only Carrie was nauseated? Is Carrie often nauseated?

CHRIS: Well...Carrie threw up twice last week.

CATHY: Oh, the evasive way Chris was telling about Carrie made me really furious! He would protect our mother even now, after all she'd done. Maybe it was my expression that betrayed Chris and made the doctor lean my way, as if he knew he'd hear a more complete story from me.

DR. SHEFFIELD: Look, you came to me for help, and I'm willing to do what I can, but you aren't giving me a fair chance if you don't give me all the facts. Already I know Carrie is malnourished and underdeveloped for her age. You are all pale, thin and weak looking. You sit there with gold and diamond watches, wearing rich clothes and shoddy sneakers, and tell me half-truths. So now I'm going to tell you a few full truths! I suspect your small sister is dangerously anemic. Her blood pressure is dangerously low. And there is some elusive factor I can't put my finger on.

So, tomorrow Carrie will be admitted to a hospital, whether or not you call your parents, and you can hock those wristwatches to pay for her life.

CATHY: Wait a minute! My brother isn't telling you everything! . . .and then I began to tell what must have seemed to the doctor an incredible tale. At first I could tell he thought I was lying, or at least exaggerating. Why was that when every day the newspapers told terrible tales of what loving, caring parents did to their children?

... after Daddy was in that fatal accident, Momma came and told us she was deeply in debt, and she had no way to earn a living for the five of us. She began writing letters to her parents in Virginia. She told us her parents lived in a fine, rich house called Foxworth Hall in Virginia and were fabulously wealthy, but because she had married her half-uncle she'd been disinherited. She didn't even give us time to say good-bye to our friends. That very evening we set off on a train headed for grandparents we never new and Foxworth Hall.

Our mother told us we'd have to hide away until she could win back his affections. Momma said one night only, or maybe two or three, then we could go downstairs and meet her father. He was dying of heart disease and never climbed the stairs so we were safe enough up there as long as we didn't make much noise. The grandmother gave us the attic to play in. It was huge -- and dirty, and full of spiders, mice and insects. And that's where we played and tried to make the best of it. But soon enough we found out that our grandfather was never going to forgive our mother for marrying his half-brother and we were going to remain 'Devil's issue.' We'd have to live up there until he was dead!

We soon found out our grandmother hated us too! She gave us a long list of what we could do and what we couldn't do. We were never to look out of the front windows, or even open the heavy draperies to let in some light.

Another year came, and that summer Momma didn't even visit us at all! Then, in October she showed up again to tell us she'd married a second time and had spent the summer touring Europe on her honeymoon! In that one room, Doctor, we lived three years and four months and sixteen days.

DR. SHEFFIELD: [disbelieving pause] It's a strange story, Cathy, and really, quite hard to believe.

CATHY: I haven't finished. The grandfather did die, and he did write our mother into his will so she'd inherit his tremendous fortune -- but he added a codicil that said she could never have children. If it were ever proven she'd given birth to children by her first husband, she'd have to forfeit everything she'd inherited and everything she'd bought with the money!

Now that mysterious, elusive factor you can't put your finger on -- the thing wrong with Carrie that makes her throw up, and us too sometimes. It's really very simple. You see, once our mother knew she could never claim us and keep the fortune, she decided to get rid of us. The grandmother began to add sugared doughnuts to the basket. We ate them eagerly enough, not knowing that they were coated with arsenic.

That’s our full horrible, awful truth. And regardless of what you believe, will you help us? Help Carrie? Please?
```

---

## IC-0239: A Piece of My Heart

- Title: A Piece of My Heart
- Author (byline): Shirley Lauro
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Jan 1992
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MARTHA, LEEANN, INSTRUCTOR 1, INSTRUCTOR 2, SERGEANT, OFFICER, SISSY, HEAD NURSE 1, WHITNEY, MARYJO, STEELE, SOLDIER, HEAD NURSE 2, VOICE ON INTERCOM, LEANN, LEANNE, ALL, PROTESTOR, FRIEND
- Teaser before the introduction: Yes
- Spoken words (computed): 1507
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shirley Lauro
ISBN: 978-0573693335
Publisher: Samuel French, Inc.
Date (Month/Year): Jan 1992
```

### Introduction (context only: never use it for content warnings)

```text
Elizabeth Kenny once said, “When you’re a nurse you know that every day you will touch someone’s life or someone’s life will touch yours.” In Vietnam countless lives were touched by the devoted nurses who cared around the clock for our fallen troops. In this selection, we meet a group of young women: Martha, Leann, Sissy, Whitney and MaryJo -- who dreamed of becoming military nurses for a variety of reasons, but none are prepared for the true atrocities of war.

A Piece of My Heart by Shirley Lauro
```

### Performance text (classify this)

```text
MARTHA: (Pg 14) (Smiling ruefully) I was an army brat. Martha O’Neil. Dad a career man. Mom a navy nurse. World War II. I was born at Ft. Benning, grew up at Ft. Bragg. I remember one day in junior high, a girlfriend came in crying: her dad was going to Vietnam. They sent her home . . . must’ve been around 1961. . . so I knew early on about Vietnam. Americans being killed there. Back of my mind was: I want to go there. Be a Navy nurse, serve my country and protect our men.

LEEANN: (Pg 17) I was anti-war! So [were] my friends! We were hippies – Woodstock, bell bottom jeans, headbands, the long hair . . . Then I remember Kennedy going, “What can you do for your country?” Well, I was twenty-one when an Army recruiter comes to my nursing school dressed in her uniform – showing us this wonderful film about the glamour of being an Army nurse and these gorgeous hospitals all over the world with all this modern equipment. And I was very impressed!

INSTRUCTOR 1: (Pg 22-23) Ladies! There are ways to be a young lady worthy of the Red Cross!

INSTRUCTOR 2: At all times be feminine!

INSTRUCTOR 1: Never swear!

INSTRUCTOR 2: Never be provocative with men!

INSTRUCTOR 1: Because you are a Red Cross girl!

INSTRUCTOR 2: Symbol of Purity.

INSTRUCTOR 1: Goodness, and Light!

INSTRUCTOR 2: Sister, Mother, Girl- Next-Door.

INSTRUCTOR 1: The All American Girl to every service man you meet!

SERGEANT: (Pg 26) ATTENTION!

OFFICER: All of you have orders for Southeast Asia.

SERGEANT: Dismissed!

SISSY: They wouldn’t even say Vietnam.

LEEANN: I’m going to my head nurse (shift of scene) (Pg 27) But I’m anti-war. I’ll take care of them in Hawaii.

HEAD NURSE 1: They’re overstaffed there. And you’re top of the line. You can make a real contribution in Vietnam.

WHITNEY: (to audience) (Pg 28) And they put us on an airplane in little powder blue, Red Cross uniforms and dixie cup hats and heels and stockings!

MARTHA: And off we go

MARYJO: (to audience) (Pg 29) There are just a few women on my plane – two hundred men! And everybody is trying to be sweet

SISSY: Singing, drinking, playing checkers –

LEEANN: I ask my stewardess for a pillow – she pretends she doesn’t hear me – she brings pillows to the men

MARTHA: (Pg 30) Then suddenly it all just quiets down (looking out plane windows)

MARYJO: No one talks.

SISSY: Nobody says a word.

WHITNEY: VIETNAM! Look how beautiful it is . . .

MARTHA: How can there be a war way down there? (Sound of BOOM)

STEELE: (Pg 31-32) My God!!! Tracers!

LEEANN: Puffs of smoke!

WHITNEY: (stunned) We’re being fired on!

SISSY: FIRED ON? I haven’t done anything to them!

LEEANN: I’m a nurse!

SOLDIER: There are Viet Cong on the landing fields

LEEANN: (lights go out) Night! Blackout! Can’t see the runway! Nothing! Dead silent on the plane!

SISSY: But I hear 247 souls breathing . . .

WHITNEY: The doors open –

MARTHA: Spotlights flashing --

LEEANN: Vietnamese – everywhere – screaming – shrieking –

OFFICER: (Pg 34) Attention! All new nurses report to North area at once! *****scene*****

MARTHA: (to audience) (Pg 37) The hospital is a series of Quonset huts – I’m assigned to the night shift.

HEAD NURSE 2: (initial tour of the facility) (Pg 38-39) Here on the wards you will be responsible for 300 to 350 patients. As supervisor you will care for the sickest patients yourself.

MARTHA: (staggered) 350 patients?

HEAD NURSE 2: Night duty is the hardest, of course. People die at night. And wounded people, Captain, get very frightened at night. They moan, they cry out . . .

MARTHA: (Pg 40) But there are so many injuries – and the kinds of injuries – (Pg 39) (to audience) Respirators! Catheters! Drains! I’ve never seen anything like this in my life!

HEAD NURSE 2: (interrupting) (Pg 40) Stuff it, Captain! Or you will never be of use! Your work is to patch up the soldier so he can get back to the battle field – (Pg 39) Build a psychological wall! (Pg 40) Don’t think! Stay behind your wall! *****scene*****

VOICE ON INTERCOM: (Pg 41-42) There is a mass casualty coming in. All new nurses report at once to Emergency. I repeat: Mass casualty is coming in. (a scramble, then shock as the first GI is brought in – then rapid overlapping chaos)

LEEANN: (Pg 44) Holy shit!

SISSY: He’s got no legs! Thighs down!

MARTHA: Gone!

LEEANN: So much blood! The doctors and nurses are doing then thousand things.

MARTHA: (Pg 45-46) Blood is spurting up!

SISSY: BLOOD IS SPURTING UP!

MARTHA: (to audience) I can’t move! I can’t talk! I can’t do anything! Amputations –

LEEANN: Burn cases –

MARTHA: Part of me is saying:

LEEANN: Jesus Christ! Just look at this!

SISSY: The other part says:

LEEANN: What’s your problem?

HEAD NURSE 1: Nurse, start the IV! Nurse!

LEEANN: I can’t! Doctors did it at home! I don’t know how!

HEAD NURSE 1: START THE IV!

SISSY: (to audience) And I turn, and I look at this patient

LEANN: (to audience) And half this soldier’s face is gone!

SISSY: It’s okay, I’m here – I’m right beside you – (to audience) His name is Jimmy. And he’s wide awake! Jimmy? You’re not alone – I’m here . . . (flatliner sound)

HEAD NURSE 1: Next patient! Move on!

SISSY: (Pg 73) (to audience) But we lose all GIs –

LEANNE: (to audience) And I am left with them alone – all the corpses stacked up like cordwood in a little tiny room with me – and then --

SISSY: (to audience) (Pg 78) [More] patients start coming in one after the other after the other – I’ve never seen so many patients in my life!

MARTHA: Here’s a yellow sheet of paper. Make a list. Worst ones at the top –

LEEANN: But they’re coming so fast, so fast –

MARTHA: Start using numbers instead --

LEEANN: Then someone worse comes in –

MARTHA: And I put his number at the top.

VOICE ON INTERCOM: (Pg 79) Attention! Sapper attack! The enemy is penetrating our perimeter. Attention! Be alert! Be Alert!

MARTHA: The enemy is coming in here? Oh my God! (explosion, screams) (Pg 80-81) THE WARD IS HIT! (Pg 80-81) Corpsman, lock the door! (to audience) [But there’s] shrapnel flying though his head! And he falls on me! DEAD!! Chunks of flesh – blood – all over the walls

LEEANN: Screaming – yelling – smell of burning flesh –

MARTHA: My patients!

SISSY: Killed! In their hospital beds! *****scene*****

MARTHA: (to audience) I’m heading into the operating room the fourth day? The fifth? And I see water coming out of the scrub sinks splashing on the floor – and patients lying on the floor – blood – the water mixing with the blood and running down the hall – a river! Oh God! Help me stay behind my wall!

LEEANN: (to audience) It’s an 18-year-old coming into surgery – he’s so young he doesn’t even have hair on his face – and I’m running beside his stretcher, and he’s crying – Mommy? Mommy? And I’m saying: I’m here, baby – Mommy’s right here! Only I’m just 21 myself.

SISSY: (to audience) He’s a blond kid from California looking just like your brother and screaming: I DON”T WANT TO DIE!

MARTHA: (to audience) (Pg 82) A piece of my heart goes with each of them! A PIECE OF MY HEART!

WHITNEY: (to audience) A hundred days before you leave you start filling in the short timer’s calendar – marking off each day.

MARTHA: (to audience) Wanting to go – but not wanting to go –

LEEANN: (Pg 83) I walk into the hospital to say goodbye. Strangely quiet day. Suddenly the double doors burst open and two litter bearers run in, set down their litter, run out. (looking closely at the patients) A little Vietnamese boy and girl – both with their hands chopped off. Looking at us – (she struggles with the image) gaping, dumb, numb – I walk out the door of the hospital in silence – for the last time, Vietnam. I am going home. *****scene*****

ALL: (Pg 86) American soil!

LEEANN: (Pg 93-94) (to audience) I end up on a bus to LA – In the depot I see people waving signs –

PROTESTOR: (marching and yelling) PEACE NOW! HEY, HEY, LBJ, HOW MANY KIDS DID YOU KILL TODAY? MAKE LOVE, NOT WAR!

LEEANN: My friend comes running up

FRIEND: Jesus! You got a dress in your bag? Jeans? Something else to wear?

LEANN: (proudly) It’s my uniform! It’s got all my medals on!

FRIEND: Go change! You’re a target! For God’s sake!

LEANN: Target?

PROTESTOR: (yelling in her face, spitting) MURDERER! BUTCHER! GO BACK TO NAM! WAR MONGER! GET OUT OF HERE!

LEEANN: (to audience - confused) So I run to the washroom, change out of my uniform, I run back. (to Friend) Burn it! (throws duffle on ground).

FRIEND: But your medals . . .

LEEANN: **** MY MEDALS! BURN IT, I SAID!! *****scene*****

LEEANN: (Pg 100-101) (to audience) I’m out of the service. San Francisco. Intensive care. They won’t let me hang a pint of blood without supervision. I was treated different in Nam. Trusted. They’re putting me through an Orientation Course about CPR?! I quit!

MARTHA: (Pg 100-101) (to audience) I go back into the military. The Reserves. To teach. A chance to show my skills. (To Leeann) I can’t stand these Reserve nurses! They played it safe during Nam. Why aren’t they active? All these nurses paid for practicing? Why don’t they do what they’re practicing for. I quit!

LEEANN: Job to job to job –

MARTHA: Looking – for the respect – the thrill – the challenge –

LEEANN: Homesick for the GIs of Nam.

MARTHA: “Adrenalin Junkies” that’s us.

LEEANN: (to audience) I stop putting Nam down on my application form. I demonstrate against the war! I march! I carry signs!

SISSY: (Pg 111-112) (to audience) Since I came back I’ve watched MASH. Current. Reruns. Everything. I cry. Every time. Doesn’t matter what the story is. I cry. Chopper in the sky I cry. Color khaki on the screen I cry. Sad . . . terribly sad to me – all of it . . . (starting to tear up)

LEEANN: (Pg 114-115) (anger and rage mount as she speaks) I see the hostages from Iran on TV. And this is pissing me off! They are getting into limos for this big parade with the Yellow Ribbon Welcome and what did they do? Sat around four hundred days reading coming books while I was risking my life. Getting cursed and spit at in my uniform? (Martha grabs her, tries to calm her down; she wrenches free) No! Don’t you touch me! I could kill someone, you know that? I could kill . . . me (breaks down into tears) me . . . me . . . me . . .

MARTHA: (Pg 116) (moves away, to audience) You people! Whoever you are! Who sent me over there . . . You are hiding behind so many other people you will never be brought to justice in this world! I WANT YOUR DAY OF RECKONING TO BE AT HAND! I WANT YOU TO BURN FOREVER IN THE HELL OF VIETNAM! (Long beat) I want . . .

ALL: to never fight another war. . . (Pg 124) (softly singing) America, America . . . God shed his grace on thee, and crown thy good with brotherhood, from sea to shining sea.
```

---

## IC-0240: Pink

- Title: Pink
- Author (byline): Judith Thompson
- Work: The Other Side of the Dark
- Publisher: Playwrights Canada Press
- Publication date as stated: Jan 1997
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: LUCY
- Teaser before the introduction: No
- Spoken words (computed): 975
- Already set (do not supply): none

### Source block (context only)

```text
Author: Judith Thompson
Book: The Other Side of the Dark
ISBN: 978-0887545375
Publisher: Playwrights Canada Press
Date (Month/Year): Jan 1997
```

### Introduction (context only: never use it for content warnings)

```text
In 1970s South Africa, 10-year-old Lucy's black nanny is killed during a peaceful protest march. The insidious nature of racism is put on full display as the child attempts to convince the nanny's spirit that apartheid is good for her people. Pink by Judith Thompson
```

### Performance text (classify this)

```text
LUCY, a 10-year-old white girl talking to her dead black nurse, Nellie, shot in a march, in her open coffin. 2

LUCY: NELLIE NELLIE NELLIE NELLIE NELLIE NELLIE NELLIE NELLIE NELLIE NELLIE NELLIE NELLIE NELLIE NELLIE NELLIE NELLIE NELLIE NELLIE NELLIE NELLIE NELLIE NELLIE NELLIE I want you to come back, to shampoo my hair and make a pink cake and we can sit in the back and roll mealie pap in our hands see, I told you not to go in those marches and I told you, I told you that what you guys don’t understand, what you didn’t see, is apartheid’s for YOU. IT’S FOR YOUR GUYS’ FEELINGS, see, like we got separate washrooms cause you like to spit, and if we said, Eww yucch, don’t spit, it would hurt your feelings and we got separate movies, cause you like to talk back to movie stars and say amen and that’s the way and stuff and that drives us crazy so we might tell you to shut up and then you might cry and we got separate bus stops cause you don’t like deodorant cause you say it smells worse than people and we might tell you you stink and the only thing I don’t get is how come you get paid less for the same job my Mummy says it’s because you people don’t like money anyway, you don’t like TVs and stereos and all that stuff cause what you really like to do is sing and dance. And you don’t need money to sing and dance I just … I don’t understand why you weren’t happy with us, Mummy let you eat as much sugar as you wanted, and we never said anything to you, some days, Mummy says it was up to a quarter-pound, but we know blacks like sugar so we didn’t mind, and we even let you take a silver spoon, I heard Mummy say to her friends, there goes another silver spoon to Soweto but she never called the police...

… and you had your own little room back there, and we even let your husband come once in a while, and that’s against the law, Mummy and Daddy could have gone to jail for that, so how come you weren’t grateful? How come you stopped singing those Zulu songs in the morning, those pretty songs like the one that was about love and kissing, you stopped singing, and you stopped shampooing my hair, you said I could do it myself, and and your eyes, your eyes used to look at me when I was little they would look at me like they were tickling me just tickling me all the time, like I was special, but they went out, they went out like a light does and you stopped making my cakes every Tuesday, every Tuesday morning I would ask you to make me a pink cake and you would always say, you ask your mummy and then you’d make it, but you stopped making them, you told me I was too old for pink cakes, that the pink wasn’t real, it was just food colour anyway and then, and then, you hardly ever came anymore, and when I saw you that day … when I saw you downtown with your husband and four children all … hanging off your arms, I just couldn’t stand it! I wanted to yell at your children and tell them you were mine that you were more mine than theirs because you were with me more much more so you were mine and to let go of you to get off you and I hated the way you looked without your uniform, so brown and plain, not neat and nice anymore, you looked so pretty in your uniform, so pretty, but we didn’t even mind when you didn’t want to wear it.

We didn’t mind, but you were still unhappy, and when I saw you in town looking so dusty and you didn’t even introduce me to your kids and one of them, one of them did that rude thing that ‘Amandilia’ thing that means black power I saw you slap his hand but you didn’t say anything, so you must have hated me too, I saw that you hated me too and I’d been so nice to you, I told you my nightmares and you changed my bed when I wet it and now you didn’t even like me and it wasn’t my fault it wasn’t my fault it just when I asked you why that day, you were cleaning the stove and I said Nellie why … don’t you like me anymore, and you said, you’re not a child anymore, Lucy, you’re a white person now and it wasn’t my fault I couldn’t help it I couldn’t help yelling 5

SLAVE, SLAVE, DO WHAT YOU’RE TOLD, SLAVE OR I SLAP YOUR BLACK FACE, I SLAP YOUR BLACK FACE AND I KICK YOUR BLACK BELLY I KICK YOUR BLACK BELLY AND KICK IT TILL IT CAVES RIGHT IN AND IT CAN’T HOLD MORE BABIES EVER AGAIN. NO MORE UGLY BLACK BABIES THAT YOU’LL … that you’ll like more than me. Even though I’m ten years old I made you die. I made you go in that march and I made you die. I know that forever. I said I was sorry, I’m sorry, I’m sorry, I’m sorry, I’m sorry, but you never looked at me again. You hated me. But I love you, Nellie, more than Mummy or Daddy and I want you to come back, and sing those songs, and roll mealie pap and be washing the floor in your nice uniform so I can come in and ask you to make a pink cake and your eyes will tickle me. And you will say yes.

Yes, I’ll make a pink cake …
```
