# Classification request: batch 35 of 63 (40 records, IC-1361 to IC-1400)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-035-reply.json`.

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

## IC-1361: Fools

- Title: Fools
- Author (byline): Neil Simon
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: 1981
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: LEON, SNETSKY, LENYA, DR. Z, DR.Z, SOPHIA, GREGOR, MISHKIN, MAGISTRATE
- Teaser before the introduction: Yes
- Spoken words (computed): 2120
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Simon
ISBN: 978-0573608773
Publisher: Samuel French, Inc.
Date (Month/Year): 1981
```

### Introduction (context only: never use it for content warnings)

```text
The people of Kulyenchikov are not exactly what Leon Tolchinsky had in mind when he comes to the village. He meets townspeople who seem to not have all of their marbles. He meets a father and energetic wife who want to find someone who can finally teach their daughter Sophia and break the curse that has plagued the village. Leon is running against time to break the curse before he becomes a fool himself in Fools by Neil Simon.
```

### Performance text (classify this)

```text
LEON: (Pg 9-11) Kulyenchikov, I like it! A quiet, pleasant village. The perfect place for a new schoolteacher to begin his first bona-fide, appointment as a schoolmaster. My heart is pounding with excitement. I don’t see anyone around. (looks at watch) (Pg 46) Nine o’clock. Maybe I arrived a little early. (Snetsky the shepherd enters)

SNETSKY: Elenya! Lebidoff! Marushka! Olga! Good morning. Did you happen to see two dozen sheep?

LEON: Two dozen sheep?

SNETSKY: Yes. There were fourteen of them. (He continues looking)

LEON: No, I’m sorry.

SNETSKY: Well, if you see them, would you give them a message?

LEON: A message for the sheep?

SNETSKY: Tell them the shepherd is looking for them and they should tell you where they are and I’ll come and get them.

LEON: I am Leon Steponovitch Tolchinsky, the new schoolteacher. I was hired by Dr. Zubritsky to teach his young daughter. I am, if I may say so, an excellent teacher.

SNETSKY: Oh, they all were, but not one of them lasted through the first night. We’re unteachable. We’re all stupid in Kulyenchikov. There isn’t a town or village more stupid in all of Mother Poland.

LEON: Russia. Are you telling me that every man, woman, and child -

SNETSKY: All stupid.

LEON: (Pg 11) (To the audience) Something is up here! I’m sure Dr. Zubritsky will explain it all to me. (to Snetsky) A pleasure meeting you, Citizen Snetsky. (Scene Change - Leon knocks on door)

LENYA: (Pg 16-18) Nikolai! Nikolai! He’s here. Maybe he’ll be the one. Maybe this one will finally be our salvation.

DR. Z: Calm yourself, Lenya. Who’s come? Who’ll be our salvation?

LENYA: The new - er- the new - what do you call them? They come and -er- we had one once but no more.

DR. Z: Oh, I know who you mean. They point to you and they say -er- they ask you -er-...

(Leon knocks) A knock? Open the knock. (Lenya opens the door after a struggle with pulling or pushing it open)

LENYA: Won’t you come in?

LEON: Dr. Zubritsky? Madame Zubritsky? I am Leon Steponovitch Tolchinsky.

DR. Z: So you are the new - the new –

LENYA: But you look so young to be a - to be a -

LEON: Not at all. I think you will find that I am, if I may say so, one of the best young teacher(s) in all of Russia!

DR.Z: (excited) A teacher! He’s a teacher!

LENYA: Perhaps you would like to start teaching right away, teacher?

LEON: Well, no one’s more eager than I am. (Pg 24-26) We must begin at once. Can I see Sophia?

LENYA: Not from here. She’s up in her room. (Lenya exits to get Sophia)

DR. Z: You’ll find her a most sensitive girl. She likes to do interesting things… like touching things - wood, paper, metal. She likes drinking water. (Lenya and Sophia enter)

LENYA: May I present our daughter - (looks at a piece of paper in her hand to remind her of Sophia’s name) Sophia Irena Elynya Zubritsky. Sophia, this is Leon Tolchinsky.

LEON: (aside) Is that my breath that has just been taken away? (to Sophia) Miss Zubritsky - may I call you Sophia?

SOPHIA: Sophia?

DR. Z: It’s your name, sweetheart.

SOPHIA: I would be very pleased to have you call me Sophia.

DR. Z: (Pg 18-23) (To Leon) How can we help you?

LEON: Well, there are a few questions I wanted to ask you first.

DR. Z: Questions! That’s what they ask when they point to you!

LENYA: Would you be so kind, Master Tolchinsky, to - ask us a question?

DR. Z: It’s been so long since anyone has asked a good “school question.”

LEON: Very well… What is the purpose of man’s existence?

DR. Z: What a question . . . Lenya, did you ever hear such a beautiful question?

LENYA: I’m speechless . . . To think someone would ask us a question like that.

LEON: Are you interested in the answer?

DR. Z: Not today, thank you. To be asked one question like that in a lifetime is more than we ever expected. The answer should be given to someone much more worthy than we are.

LEON: But knowledge is everyone’s birthright.

DR. Z: Everyone not born in Kylyenchikov.

LEON: I don’t understand.

LENYA: You would if you knew about the nurse.

LEON: What nurse?

DR. Z: Not the nurse, the purse.

LEON: What kind of purse?

DR. Z: The kind of purse that inflicts wrath upon all the poor souls unfortunate enough to be born in this village.

LEON: Do you mean, perhaps, a curse?

DR. Z: Curse! I knew it sounded like that.

LENYA: We were so close! So close!

LEON: What is this curse you speak of?

DR. Z: Lenya, bolt the door. Draw the curtains.

LENYA: I can’t draw curtains. I can draw a cat or a fish -

DR. Z: Never mind. Lower your voice.

LENYA: (bends knees) How low do you want my voice?

DR. Z: That’s low enough. Young man, have you ever heard of the Curse of Kulyenchikov?

LEON: I can’t say that I have.

DR. Z: You can’t say that? It’s not hard. Even Lenya can say that.

LENYA: “The Curse of Kyluenchikov!”

LEON: Doctor, I don’t believe in curses. Curses are old wives’ tales.

DR. Z: You’re thinking of Noychka. In Noychka, all the old wives have tails.

LEON: But where did the curse come from?

DR. Z: [It happened] two hundred years ago. It’s all documented in The Book of Curses. Here. (hands book to him) Read it yourself. The page is marked.

LEON: (Attempting to open the book) It’s all stuck together.

LENYA: We marked it with maple syrup. Read it to us!

LEON: (Reading) “In the year 1691, in the village of Kulyenchikov, a young, handsome but illiterate farmer name Casimir Yousekevitch fell in love with the daughter of the most learned man in the town Mickhail Zubritsky.”

LENYA: Zubritsky! I’ve heard that name before!

DR. Z: I’ve seen it! On a front door somewhere. In this neighborhood.

LEON: It’s on your front door. Your name is Zubritsky.

DR. Z: (With profound insight) Wait a minute! That means that the young man in the curse may possibly be related - to our front door.

LEON: “The young girl’s name was Sophia Zubritsky.” Sophia? Your daughter [has] the identical name of the girl in the curse over two hundred years ago.

DR. Z: I can’t believe it. Unless she has been lying about her age.

LEON: “The match was doomed. When Sophia’s educated father learned that young Casimir was illiterate, he forbade Sophia to ever see [him] again. That winter Casimir took his life by plowing his own grave and planting himself in it. Upon hearing of his son’s death, Casimir’s father, Vladimir Yousekvitch, brought all his wrath and fury down upon Kulyenchikov. (quoting Yousekvitch) A curse! May the daughter of Mikahil Zubritsky, murderer of my only son, be struck down by the ignorance that caused my son’s death! May her children [and] all who live in Kulyenchikov be cursed with ignorance and stupidity for all eternity, unable to leave this cursed village until my final vengeance has been satisfied!”

LENYA: That would explain why the train doesn’t stop here.

LEON: (aside) My initial impulse was to panic. To educate is one thing - to break curses is another.

DR. Z: Excuse me, but are you alright?

LEON: Yes. I was just thinking.

DR. Z: Lenya… he was thinking.

LENYA: He was thinking.

DR. Z: What’s it like?

LEON: You mean you don’t know what thinking is?

DR. Z: I don’t and she certainly doesn’t.

LEON: (Pg 24) Patience! We will break this curse, I promise you! By the simple, everyday, painstaking work of education.

DR. Z: Would I be able to open up jars? I have a terrible trouble opening jars.

LEON: It occurs to me that since the curse started with the young Sophia two hundred years ago, perhaps the key to ending it lies with her direct descendant. (To Sophia) (Pg 26-27) I have every reason to believe that under ordinary circumstances, you have the capability of being an extremely intelligent young woman. But someone has put a cloud over these powers and it is my intention to remove this cloud. I should like to ask you a few very simple questions to know at what point to begin. Now then, what is your favorite color?

SOPHIA: My favorite color. . . is yellow.

LEON: Yellow! Why, Sophia, is your favorite color yellow?

SOPHIA: Because it doesn’t stick to your fingers as much.

LEON: That’s a very interesting answer, Sophia. There is a certain logic to her response [even though] that logic escapes me completely.

SOPHIA: (Pg 32) I know that something happened a long time ago that prevents me from knowing what happened a long time ago. If only you knew me the way I might have been instead of the way I am.

LEON: But if you were not the way you are, then I would not have come here to help you to become the way you might have been. (Pg 28) We must begin soon. [Tomorrow.]

SOPHIA: (Pg 29-30) I think you are the most beautiful schoolteacher I have ever seen, Master Tolchinsky. I pray that you don’t despair of Kulyenchikov and that you will stay with us forever. (she leaves)

DR. Z: I think our Sophia has taken a liking to the new schoolmaster.

LEON: If it is true, then standing before you is the happiest man in the universe. Tell me, does she have any suitors?

DR. Z: There is no one. Not even him.

LEON: Him?

DR. Z: Count Gregor of Kulynechikov. He’s one of them. The ones who put the purse on us.

LEON: You mean - a Yousekevitch?

DR. Z: The last of his line. He cares only about avenging his ancestors. If a Zubritsky marries a Yousekevith, they will be satisfied and the nurse will be over.

LEON: (Pg 36) Does Sophia love him?

DR. Z: (Pg 30) She has said no for many years, but she can’t resist much longer. (thunder clap of doom as Count Gregor who has been listening at the door enters; Leon flustered attempts to make an exit)

LEON: (Pg 36) I don’t understand. I’m breaking out in a cold sweat. (Pg 31) Tomorrow the education of Sophia Zubritsky begins. Good day.

GREGOR: (Pg 38-39) Not good day. One day. [It’s a part of the curse that] if at the end of one day you have not rais[ed] Sophia’s intellect, you must be gone from our village. To remain for even one second past the allotted time means, you will fall victim to the yourself. See you tomorrow. Come, Lenya. (exits with Lenya)

LEON: I cannot believe such nonsense. Threaten me all you want, sir, but I will never leave. To be honest, I love Sophia Zubritsky.

GREGOR: Love?? There is no love in Kulyenchikov. It’s all part of the curse. (He laughs and exits)

LEON: (To audience) But is it true? If I cannot teach Sophia to think in twenty-four hours, she will never be able to love me? I must muster up the strength to break this curse. (transition - time change)

LEON: (Leon enters breathless) (Pg 46-47) We cannot lose another moment. The Count said I had only 24 hours to break the curse after I arrived. I arrived yesterday morning at exactly 9 o’clock. It’s 8 o’clock now. That means I have only one hour.. Get Sophia!

DR. Z: Listen! I hear footsteps coming down the stairs.

SOPHIA: (Sophia enters) Good morning, Mama. Good morning, Papa. Good morning, schoolmaster.

DR. Z: She got all three right! This is going to be her day, I know it! (knock – Mishkin enters)

MISHKIN: (Pg 52) I have an important letter for schoolmaster Tolchinsky. It’s marked urgent, so I only went to three wrong houses first. (hands letter to Leon)

LEON: (looks at letter then speaks an aside only to the audience) (Pg 58) I am suddenly inspired. I think I have hit upon a plan that will break this curse and save [Sophia] from [Count Gregor]. (Pg 57) You can’t be cursed unless you permit yourself to be. Kulyenchikov’s lack of intelligence is self-inflicted, caused by guilt and the fear of a tyrannical power. (Pg 58) The plan begins! (Pg 66) (back to others) It’s bad news, I’m afraid. My uncle and sole remaining relative has just died, leaving me nothing but all his debts. Before he died, he said he blamed all of his misfortunes on the selfish character of his distant relatives and that even changing his name to Tochinsky never helped him escape destiny’s finger.

DR. Z: What was his name before Tochinsky?

LEON: Yousekevitch. Do you realize what this means? (Pg 52) [Dr. Zubritsky] – I would like to ask for [Sophia’s] hand in marriage.

DR. Z: Yes . . . I’ll give my permission right now

LEON: (Pg 58) Sophia, you must marry Yousekevitch. I will be Yousekevitch. Will you marry me, Sophia? (Sophia nods and claps her hands, not really understanding) (transition as wedding music plays)

LEON: (Pg 67) (aside to the audience) [The letter] didn’t say that at all. It’s a bill from my former college saying I still owe them for last year’s tuition. [But] I have planted the bomb in their minds. I now pray God - for the explosion!

MAGISTRATE: (Pg 62) Will the groom step before me? And will the bride step forward? (Pg 67) Do you, Leon?

LEON: I do.

MAGISTRATE: And do you, Sophia?

SOPHIA: I do!

MAGISTRATE: If there is anyone here who objects . . . (silence) Going once… going twice… going three times… that’s it! I now pronounce you man and wife! (There is a loud thunderclap - everyone but Leon freezes in a trance a couple beats, then relaxes)

LENYA: (Pg 68-70) Nikolai! I - I feel funny - weak in the knees and a dizziness in my head.

DR. Z: It’s all right, my dear. Your blood is just pulsating from the excitement. Sometimes that can cause the adrenal glands to oversecrete, resulting in a sudden rush to the head.

LENYA: I never knew you were such a brilliant doctor.

DR. Z: I [just] worry about you because - I love you, my dear.

LENYA: And I love you, Nikolai. Even when I couldn’t say it, I knew it in my heart.

LEON: I adore you, Sophia.

SOPHIA: [And] I love you, Leon. It was your faith and courage that won over ignorance.

LEON: No, it was your pure heart and trusting soul that gave me that faith and courage. It was love that destroyed the curse, Sophia, not my puny efforts. (to audience) (Pg 71-72) When you think of it, it’s not such a bizarre story after all. Be honest. Haven’t you met someone in your life who came from a place like Kulyenchikov? An aunt, neighbor, your boss? Once the curse was lifted, we became like any other small town or village in any other part of the world. I remained a schoolmaster and dedicated my life to the education of the unenlightened… After all, there are so many Kulyenchikovs in the world.
```

---

## IC-1362: Fortunately, the Milk

- Title: Fortunately, the Milk
- Author (byline): Neil Gaiman
- Work: Not specified
- Publisher: HarperCollins
- Publication date as stated: Sept 2014
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ME, DAD, SISTER, ALIEN, PIRATE QUEEN, STEG, PONY, VAMPIRE, POLICE
- Teaser before the introduction: Yes
- Spoken words (computed): 1684
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
Author Neil Gaiman is a phenomenon. I'm not saying that's good. I'm not saying that's bad. I'm simply stating a fact. A fellow author recently commented that when Gaiman talks, people clap. When he coughs, they laugh. And there’s no better way to introduce you to his unique storytelling style than to take you on a mystical adventure with an imaginative and creative father in Fortunately, the Milk
```

### Performance text (classify this)

```text
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

DAD: The milk! My children are breakfastless . . . (to the kids) And with that, Professor Steg pressed the red button with his heavily armored tail. There was a ZOOM, a TWORP, and a THANG, and we were hurtling through the cosmic void --FLOATING above a landscape of ominous towers and castles. It was not a friendly place. Bats flew across the sky in huge flocks.

There was a loud FLUT!, and where the bats had been, several pallid people were now standing. The man in front had a very bald head. THEY ALL HAD SHARP TEETH.

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

## IC-1363: Freak: A Semi-Demi-Quasi-Pseudo Autobiography

- Title: Freak: A Semi-Demi-Quasi-Pseudo Autobiography
- Author (byline): John Leguizamo
- Work: Not specified
- Publisher: Random House, Inc.
- Publication date as stated: Aug 1998
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: JOHN, MOMS, DOCTOR, DAD, HINDI GUY, JAMAICAN RASTA, KOREAN NEWSTAND GUY, POOCHIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1228
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Leguizamo
ISBN: 978-1573226936
Publisher: Random House, Inc.
Date (Month/Year): Aug 1998
```

### Introduction (context only: never use it for content warnings)

```text
(Very formally) John Leguizamo was born in Bogotá, Colombia. His father Alberto was a Puerto Rican realtor when met Leguizamo's mother, Luz.
```

### Performance text (classify this)

```text
(Cutting Revised 1/29/2024)

JOHN: (interrupting) (Pg 2-3) I’ve changed my parents’ names to Fausto and Lala, to protect the innocent, namely me. And when I was born, my moms was in labor for forty-eight hours!

MOMS: Desgraciado, get this parasite out of me! Get it out of me now!!

DOCTOR: Push! MS. Liquidzamo, Mrs. Legs and amo, leg of lab . . . Just push ma’am!

DAD: I’m paying you, doctor! Why don’t you pull?

DOCTOR: I am pulling! He’s stubborn.

DAD: Then leave him in there. Get up, woman, we’re leaving,

JOHN: And they wonder why I have problems.

(Shrugs shoulders) I’ll let John tell it his way. Freak: A Semi-Demi-Quasi-Pseudo Autobiography by John Leguizamo

JOHN: (Pg 3-4) My parents left Latin American during the big plantain famine of the late sixties and when they arrived in New York City they had such thick accents they couldn’t even understand each other. My moms got all her English from watching television.

MOMS: Fausto, chock full of nuts is the heavenly coffee, they’re creepy and they’re cookie, that . . . that . . . that’s all folks!

DAD: Woman, what the hell did you just say?

MOMS: How should I know? I’m speaking English.

JOHN: (Pg 5-6) The shuttle from the airport said “Miserable and Huddled Masses” and my pops is like, “This is our bus,” so we jumped on and ended up in the present-day Ellis Island – Jackson Heights, Queens. Our tenement building was like the modern Tower of Babel. When I walked through the streets, I’d see every ethnicity under the sun.

HINDI GUY: You want curry candy?

JAMAICAN RASTA: You people multiply like roaches. Tinga linga ling. Hear the money ring.

KOREAN NEWSTAND GUY: This is not a library, You buy magazine or kick your a**!

JOHN: My parents worked twenty-eight hours a day, fourteen days a week. I’m not bad at math; it’s just that Latin people have to make the most of their time. But my pops always took time out of his busy schedule to tell us his own version of an American bedtime story.

DAD: Once upon a time there was a Little Red Riding Hood and she went into the woods and got a green card and lived happily ever after. Now shut up and go to sleep!

JOHN: (Pg 14-20) Now, our apartment was so puny it wished it were a project. It was a seventies nightmare; our walls were avocado green with brown linoleum and a nuclear orange shag rug. And the centerpiece, the piece de resistance of this mess, was our TV, my dad's pride and joy. It was sacred to him, because my pops could Latinize everybody in America; we would let the screen get real dusty so that everybody looked nice and dark and Spanish. He thought the more you watch it, the more you wear it out. Dad was operating under some kind of third-world logic.

DAD: Don't use my television and don't sit on my furniture unless we have important guests. Use the floor for sitting and the kitchen sink for eating. And we're not gonna buy any more food if you keep eating it! Food, I repeat, is for the guests and the animals. And I just brushed the dogs, so don't pet 'em! And get off the rug, I just vacuumed it. And stop sucking up all my oxygen -- I'm breathing it.

JOHN: My brother and I would be like, "Okay, Dad, okay." Every time my father had something important to say, the subway would go by. And it wouldn't have been a problem, but we shared a wall with the number 7 Train. He'd start lecturing us

DAD: I'm only gonna say this once. The most important thing I want you to do is. . .

JOHN: And sure enough the train would roar by, drowning him out

DAD: . . . or I'm gonna kick you’re a**!

JOHN: Paralyzed with fear, I'd say, "Okay, Dad-no problem." But as soon as my father was out of the house, my brother Poochie and I would be like a Navy SEAL operation. (to Poochie) Now, Poochie, it's 1800 hours, and the Prince of Darkness will be. . . (to audience) Poochie freaked out.

POOCHIE: Prince of Darkness? You didn't tell me nuttin' about no Price of Darkness. Na-ah, I'm not listening. (puts his hands over his ears and closes his eyes) Mamaku mamasa mama mamakusa . . .

JOHN: (yelling) Poochie! The Prince of Darkness is the man you know as Dad. Now you go put the bubble wrap under the rug so when Dad comes through the hall, we'll hear him. Now we're punishmentproof. We outsmarted that ignor-anus! What a maroon! What a suckerbutt! Ha ha!

(dancing) Ungawa ungawa, Dad's away for two hours. A beep beep, we're TV freaks. Get stupid. Poochie, turn the TV on. (to audience) Then we'd settle down for a TV frenzy -- Spiderman, Underdog, Gigantor the space robot. Everything was great until I messed with the antenna. (pantomime Spiderman) I'd be swinging around in time to the Spiderman theme when suddenly. . . (freeze) SNAP! The blood drained out of my body and into the ground and back to Latin America.

(wailing) Poochie, I broke the antenna! (think rabbit ear antennas on the top of the television)

MOMS: (climbing in through the window) John!

JOHN: (heavy sigh of relief) Luckily it was just my moms. Mom. Why are you climbing in through the window?

MOMS: The rent is due. What are you doing? You're sitting in the furniture. You're eating the food. Ay, dios mio, you broke the antenna!! Oh my God! I'm looking into the face of a dead boy.

JOHN: Moms had a knack for calming me down. (to Moms, hysterical begging) Mom, use me for cruel animal experimentation but don't let him get his hands on me!!!

MOMS: No, don't, don't. I'll miss you. But now I must distance myself. Come, Poochie, you're an only child now. Ciao. Get off me, John. Get off.

JOHN: Then all of a sudden, we hear the sound of snapping bubble wrap . . .

DAD: (cursing) Cono, que es toda esta mierda de bubble wrap, hijo de puta!

JOHN: So, I'm blowing and fanning the TV 'cause my pops would feel it for heat. And my moms goes into rescue mode

MOMS: (whispering) I'll take care of your father. (trying to distract Dad) Fausto, you look so ultra sexy. You look so sexy. Yes, you do. You and me. Okay?

JOHN: But my father wasn’t taking the bait.

DAD: Woman, I just wanna watch my television.

MOMS: Okay, then, why don't you go downstairs and play some pool. Hmm? Okay? Play some pool?"

JOHN: God bless my moms. We didn't have a downstairs. Pops turned on the TV.

DAD: I said no, woman. What’s all that static. I can't tell Sonny from Cher.

JOHN: I'll fix it! I'll fix it! (to audience) So I moved the good piece of antenna for all I was worth. (to Dad) Like this, Dad? Or this? Here?

DAD: Move the other one!

JOHN: (Pantomime frantically while speaking) So I pretended to move the broken antenna. I fran-tically shifted my body around while holding the broken antenna in place. (to Dad) There? Like so? Perfect?

DAD: Move away from that television. Get out of the room!

JOHN: Okay, I'm leaving the room, the neighborhood. . . (to audience) and as I head for the door, I trip. He sees the antenna came off in my hand. (to Dad, meekly) It's a spear and I'm a hunter? (to audience) I know what's coming next. My pops field-goals me with a kick across the room. Luckily, the nice hard brick wall broke my fall. And I remembered my comics and how Spiderman once said to Ironman: "To escape the pain, one must move toward the pain." And my soul thought, "Yeah, right!" and . . . BOOM . . . The first words out of my mouth said it all: (pointing) Poochie broke the antenna! Poor, slow, chubby Poochie. And I just stood there watching the only brother I had beaten with the antenna, and all I could think was, "Thank God it's not me!"
```

---

## IC-1364: A Funny Thing Happened on the Way to Fifth Period

- Title: A Funny Thing Happened on the Way to Fifth Period
- Author (byline): Jason Pizzarello
- Work: Random Acts of Comedy, Pgs 141-160
- Publisher: Playscripts, Inc.
- Publication date as stated: April 2011
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, TOMMY, BURP, BUGS, STEPHANIE, STEVE, CHAD, VERONICA, CORA, OFF STAGE VOICE
- Teaser before the introduction: Yes
- Spoken words (computed): 1882
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jason Pizzarello
Book: Random Acts of Comedy, Pgs 141-160
ISBN: 978-0981909974
Publisher: Playscripts, Inc.
Date (Month/Year): April 2011
```

### Introduction (context only: never use it for content warnings)

```text
School hallways are delicate ecosystems filled with bullies, nerds, jocks and (sings) theatre kids! So when Tommy, mild-mannered techie and professional problem-solver, gets pushed around by Burp and his not-so-bright protégé, Bugs . . . he does what any reasonable teenager would do – comes up with a solution! This selection is a fast-paced hallway comedy about survival, social hierarchy, and the power of lying with confidence. Because all teen-agers know: if you can’t be popular . . . Be convincing.

A Funny Thing Happened on the Way to Fifth Period by Jason Pizzarello
```

### Performance text (classify this)

```text
CHARACTERS: Tommy, bookworm; Burp, head bully; Bugs, aspiring bully; Steve, friendly jock; Cora, Steve’s girlfriend; Veronica, Steve’s twin and a nerd with anger issues; Stephanie, lead actress; Chad, lead actor and Stephanie’s boyfriend. ***** Before School**** At the lockers as TOMMY reorganizes his trapper keeper, a large bull of a kid, BURP, comes up behind him and politely taps him on the shoulder. TOMMY turns around and the bull lets a burp rip so loud and foul, you can almost smell yesterday's lunch. But this isn't the first time, and TOMMY handles it with grace. BURP smiles.)

TOMMY: (Pg 141-160) Lovely. (Another bully, BUGS, not quite as menacing as BURP, but still with great potential, stands next to him and claps. BURP takes a bow) Let me guess, you had a burrito and a slurpee for breakfast.

BURP: Cherry slurpee. That counts as a fruit. (burps) Well, enough chit chat. Where's my homework for first period?

TOMMY: Your homework? I don't know, where did you put it?

BURP: Where did you put it? I didn't do it. You did. You did my homework.

TOMMY: I only did my homework. (takes out the homework) See.

BURP: (he snatches it away) So you did do my homework.

TOMMY: C'mon, Burp. Give it back.

BURP: Nice chattin' with you, Tommy. See ya in class. (As he exits, BURP burps while holding his fist in the air)

TOMMY: (BUGS is about to follow, but TOMMY stops him) Hey Bugs, can you wait a second?

BUGS: For you? Three.

TOMMY: Next year, I was thinking . . . He's your mentor, everyone knows you're bound to follow in his footsteps. It's called destiny.

BUGS: It's called Burp. Maybe if you learned his name he wouldn't be so hard on you.

TOMMY: Right. What I'm trying to say is, next year, when you take over this hallway as lead bully, you don't have to be a bully like him. You can be a nice bully.

BUGS: I don't think you understand the concept of bullying.

TOMMY: This is your chance to revolutionize the field of bullying. You can be a pioneer.

BUGS: Like Davy Crocket?(excited) The other night my dad caught a raccoon --

TOMMY: Bugs, Bugs. I'm sure it was a lovely family dinner, but we're getting off topic. (bell rings) Just think about what I'm saying. Let's work together. There's gotta be something I can do for you to break this viscous cycle of bullying. (STEPHANIE walks in singing a little show tune) (BUGS is enamored with her)

STEPHANIE: Hey Tommy. Great job working the spotlight in last night's performance. You really knew how to keep it right on me. You're a peach of a techie, Tommy.

(STEPHANIE heads off)

TOMMY: (TOMMY watches BUGS watching STEPHANIE) Bugs, Bugs, you all right?

BUGS: Stephanie Mezaluna. She could make a sheep throw himself to the wolves. She could make a shark swim backwards.

TOMMY: You like her huh? You wanna marry her? You wanna have little bug children?

BUGS: No, I just wanna take her to the prom. I asked Alice the lunch lady. But apparently she doesn't leave the cafeteria.

TOMMY: Too bad you already need your tickets to the prom. Today's the deadline. End of lunch. By fifth period.

BUGS: So that's our deadline.

TOMMY: Our deadline?

BUGS: (dramatic beat) If you don't get me a date for the prom with Stephanie Mezaluna by fifth period, I will make the rest of your pathetic high school career a living nerd hell.

TOMMY: Here's your problem. You can't date Stephanie Mezaluna. She only dates actors. Lead actors. Are you a lead actor?

BUGS: Just make it happen. Your future alive self depends on it.

TOMMY: You mean "my life depends on it"? (STEPHANIE returns to her locker)

BUGS: She's right there.

TOMMY: (Tommy reluctantly approaches STEPHANIE) Ha...ha... Hi. (whispers in her ear)

STEPHANIE: You want me to go to the prom with Bugs? (they look over at BUGS and catch him eating something from his hair) Why would I do that? Unless, like, the world is ending. Or he's a famous actor or something.

TOMMY: Actually. I shouldn't really be saying this ... but he's . . . a professional actor.

STEPHANIE: Yeah right. How could he be? He's not even in any of the school plays.

TOMMY: He only acts in New York. His agent won't let him act in school plays. It might ... hurt his career. His agent is very strict when it comes to parts.

STEPHANIE: Who's his agent?

TOMMY: His agent's name? Uh ... Kris ... tooff ... Baba ... balooch. Kristoff Bababalooch. You've probably heard of him.

STEPHANIE: Yeah, totally. He’s supposed to be really strict.

TOMMY: Yeah, that's him. He's Croatian. (bell rings. STEPHANIE exits)

BUGS: (BUGS pulls TOMMY aside) So are we set?

TOMMY: Not yet. But I think she's warming to the idea. One thing though. . . and this isn't a big deal at all. . . I kinda told her you were a professional actor. So brush up on your Shakespeare.

BUGS: Shakespeare is not a problem. To not be, or to not be. . . is the same question. ***** After First Period****

TOMMY: Just be yourself. But be a professional actor from New York. (TOMMY pulls out a fedora) Here. Wear this.

BUGS: Am I an actor working for the mob?

TOMMY: It'll add a little persona, a little mystique. (They approach STEPHANIE. Suave-like, BUGS leans against her locker without saying anything)

STEPHANIE: Oh. Hi . . . Bugs.

BUGS: (BUGS tips his hat) Hiya, sweetheart.

STEPHANIE: Tommy mentioned Kristoff Bababalooch might make it to our school play.

BUGS: Chrissy Baba-who?

STEPHANIE: Kristoff Bababalooch. Your agent.

BUGS: Oh ... right, that guy. Outta sight outta mind you know? Oh sure, he'll come. If you want him to. He loves that kinda junk. I mean he loves theater. I could probably get him to come today. I mean the guy is at my beck and call, ya know?

STEPHANIE: (laughs nervously) I should go tell the rest of the cast. This is so amazing!

BUGS: Sure, whatever. (STEPHANIE runs out) (BUGS, as cool as he can, saunters quickly over to TOMMY) I need an agent!

TOMMY: You have one. Kristoff Bababalooch.

BUGS: Right. I need him. To come to school. Today. I told her he could and now she thinks he's coming here and I need him to seal this deal and this is all your fault and I can't believe I just talked to Stephanie Mezaluna for as long as I did and the hat worked perfectly.

TOMMY: Okay-just calm down. Bugs, calm down. (thinks) Go find me a suit. The nicest suit you can find.

BUGS: A suit. For your funeral?

TOMMY: Maybe. Find Shelly in the costume shop, tell her I sent you. C'mon-go! (BUGS nods and runs off) (TOMMY stops STEVE at his locker)

TOMMY: Steve, I need a favor.

STEVE: I already told you I can't make you cool. It's just impossible.

TOMMY: Forget about that. I need you to pretend you're a talent agent from New York named Kristoff Bababalooch who represents Bugs who is pretending to be a professional actor so he can get a date for the prom and you're the only person that looks over 20 in our school, so I need you to dress as Kristoff so I can win my freedom from bully tyranny next year. Okay?

STEVE: I'll do it under one condition. You get a date for my sister Veronica for the prom. If she doesn't have a date, my mom is making me take her. She wants to go with Chad Glamorville.

TOMMY: But he's dating Stephanie Mezaluna.

STEVE: That's the deal. TOMMY .... Actually this may work out. (they shake; STEVE takes off) (bell rings)

CHAD: (walking down the hall, holding a script, rehearsing his lines) And that is why, Mama, I ain't ever gonna let nothin' happen to our hogs. Nothin'!

TOMMY: Hey, I need to talk to you about something very important. You need to take Veronica Jettlebaum to prom.

CHAD: Veronica Jettlebaum? What are you, sick?

TOMMY: No ... but she is. It's Veronica's dying wish to go to the prom. But no one will go with her.

CHAD: What do you mean her dying wish? Is she really sick?

TOMMY: No, she has a rare disease. It's her ... her muscles ... are turning inside out. It's a very rare condition. She only has 3 weeks to live. It's a tragedy. A Shakespearean tragedy. You know all about those I'm sure.

CHAD: I have a background in the classics, yes.

TOMMY: Then you're the only one who can play this heroic role. It's only for lead actors.

CHAD: Like me.

TOMMY: Every great actor has their charity. Brad Pitt, Sean Penn, Keanu Reeves ... Have you found yours yet?

CHAD: No . . . I haven't. Shoot! I need a charity.

TOMMY: Make Veronica Jettlebaum your charity. Take her to the prom. (bell rings) CHAD .... Okay, I'll do it. I'm sure Stephanie will understand. It's for our craft. (TOMMY and CHAD shake and head separate ways) ***** After Third Period****

TOMMY: (bell rings. TOMMY goes immediately to STEVE) We're all set. Veronica has a date to go to the prom with Chad Glamorville.

STEVE: Well, that was easy.

TOMMY: I still need you to look and act like a believable talent agent from New York. He's from a Croatian island, okay? Shelly is waiting for you in the costume shop. I need you as Kristoff Bababalooch in this hallway by next period. (STEVE hurries off and runs into VERONICA) Veronica! Good news. We don't have to go to the prom together.

VERONICA: I told you I'd only go with Chad Glamorville.

STEVE: And you are. Talk to Tommy. (STEVE runs out. VERONICA approaches TOMMY)

VERONICA: Steve said-

TOMMY: Yes, Chad Glamorville. And you. And the prom. There's only one catch . . . you're dying. Not really dying. Just fake dying.

VERONICA: What am I dying of?

TOMMY: Here I made a list. (hands her several sheets of paper. She flips through it)

VERONICA: And if I'm dying of all these things, he agreed to go with me?

TOMMY: He has a very big heart. Now read through it. You gotta play that part.

VERONICA: Okay, if it's for Chad Glamorville, it's worth it. (VERONICA heads off) (BUGS confronts TOMMY)

BUGS: What was that all about?

TOMMY: It's all part of the plan. (STEPHANIE confronts BUGS and TOMMY)

STEPHANIE: I thought you said your agent was coming. Where is he?

BUGS: I just talked to him. He's on his way. I'll go try his cell again. (BUGS leaves)

STEPHANIE: Why would he be in town?

TOMMY: He's scouting ... for talent. If he comes here, will you go with Bugs to the prom?

STEPHANIE: If a New York agent walks down this hall, I will go to the prom with Bugs. And if he doesn't, I'll make sure you never get a date in this school again.

TOMMY: I don't get any now, so . . . it's a deal. (they shake; STEPHANIE exits) *****After 4th Period ***** (Bell rings)

CHAD: (CHAD pulls TOMMY aside) The gown Veronica wears to the prom isn't going to be like a hospital gown is it? Because I already rented my tux and we have to match.

TOMMY: Of course not. It's not like she wears a hospital gown to school. (VERONICA enters in a hospital gown. She coughs dramatically and does an exaggerated limping walk)

CHAD: Uh . . . hi . . . Veronica. Sorry to hear you're sick. Are you going to be okay?

VERONICA: Ha, ha. You're cute. All I ever wanted was to be treated ... (cough, cough) ... like a normal teenager.

STEPHANIE: (STEPHANIE enters) So guys, where's Kristoff?

STEVE: (STEVE enters as Kristoff Bababalooch, the sleazy New York super-agent. He speaks with a slightly ambiguous European accent) Bugs, baby! Be wit you in a hot minute.

BUGS: (Aside to TOMMY) Who's that?

TOMMY: (Aside) That's your agent, you nitwit.

STEVE: (to VERONICA) Who are you? You've got a great look. Sick is very "in" right now. Here's my card. (then approaches BUGS) There he is. You bug-eater-you.

BUGS: (Immediately playing the part) Kristoff! So good of you to come. (STEVE air kisses BUGS on both cheeks) Kristoff, I'd like you to meet a very talented actress... Kristoff, this is Stephanie Mezaluna.

STEPHANIE: It's a pleasure to meet you, Mr. Bababalooch. (STEVE air kisses her on both cheeks)

TOMMY: Stephanie and Bugs are going to the prom together, isn't that, right, Stephanie?

STEPHANIE: Oh...right. That's...right.

STEVE: That's great, great. Crazy kids. I remember my prom. It was inside a volcano. Because I'm from an island or something. We used to play futbol with rotten pineapples coated in pig grease. (TOMMY signals him to stop talking) Well . . . I gotta get going. Send me your headshots. (CORA enters looks at STEVE strangely)

STEVE: Bugs, why is this strange girl staring at me? Please ask her to leave.

TOMMY: (pulls CORA aside) Cora, get out of here. You're gonna ruin the whole thing.

CORA: Is that Steve?

TOMMY: Of course it is. (takes a deep breath) He's playing a talent agent, who represents Bugs who's pretending to be a famous actor to impress Stephanie in exchange for my freedom from his bullying, in exchange for me getting a date with Chad Glamorville, for Veronica who's pretending to be sick, so Steve is free to go to the prom with you.

CORA: (beat) Aw, that's sweet. (exits)

TOMMY: It worked! Looks like things may finally be looking up for me.

BURP: (enters with a vulgar burp) If I could have your attention. I have some exciting news for all of you. Due to my extraordinary lack of academic efforts, you will be delighted to know that I will be gracing you with my presence again next year.

TOMMY: You're staying back ... again?

BUGS: Looks like things are finally looking up for you.

TOMMY: Burp, maybe we can work something out. I've done wonders for the people around here. (TOMMY puts his arm around BURP and they walk out in negotiations)

OFF STAGE VOICE: Last chance for prom tickets! Last chance!
```

---

## IC-1365: A Game of Chess

- Title: A Game of Chess
- Author (byline): Garrison Keillor
- Work: Definitely Above Average (Audio Book)
- Publisher: HighBridge Audio
- Publication date as stated: Aug 2000
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CAUTION, GK, TR, SS, TK, TR BRIT LADY, SS COCKNEY, TR BRIT, TR KID, TR BRIT DOLT, TR DOLT
- Teaser before the introduction: Yes
- Spoken words (computed): 1112
- Already set (do not supply): none

### Source block (context only)

```text
Author: Garrison Keillor
Book: Definitely Above Average (Audio Book)
ISBN: 978-1565114128
Publisher: HighBridge Audio
Date(Month/Year): Aug 2000
```

### Introduction (context only: never use it for content warnings)

```text
A Game of Chess by Garrison Keillor
```

### Performance text (classify this)

```text
NOTE: Listen to Garrison Keillor’s Prairie Companion performance of this poem at the following link http://prairiehome.publicradio.org/programs/2011/10/08/videos/#video-1

CAUTION: This selection is available in audio format only - may not be suitable for competition in some states

Ledgend of Players who provide script and sound effects for performance:

GK: Garrison Keillor

TR: Tim Russell

SS: Sue Scotland

TK: Tom Keith

GK: I've lost some of life's battles,
I've known defeat and distress,
But I've not met defeat quite so grim and complete
As when I lost to Freddie at chess.
I've been dissed, dismissed, and demoted
I've even been dumped, I confess,
But never disgraced, demeaned and debased,
Until I lost to Freddie at chess.
He is eleven, my grandson,
And he's played a year or less.
And I'll never forget the day that he said:
TR (KID): Grandpa-----You want to play chess?

GK: I'm sort of busy today, I said. And then he asked me again.

And he set up the board on the living room floor And we sat down and set up our men. (SFX)

He advanced up the middle and soon my bishop
Was caught in a three-way trap. (TK BRIT: Dear me!)
I sent out a knight to join in the fight
And he got shot in the kneecap. (TR: CRY OF PAIN)
My bishop stood in confusion.

TK: Oh dear, what a pickle.

GK: he said.

TK: O Lord lift thine arm and preserve me from harm

GK: And Freddie lopped off his head. (TK: SHUDDER, LOP, PLOP)

I castled my king to protect him
And I cautiously put forth a pawn. (TK TIMOROUS PAWN)
And in rode his knight (GALLOPING) in open daylight
And my other bishop was gone. (TR BRIT CRY, SPEARING, TR FALLS)

(TK AND TR MOUTH TRUMPETS, BATTLE SFX, HORSES, BATTLE MUSIC)

We fought it out in the middle,
We fought it out on the side,
Men in the saddle rode into the battle,
One after the other they died.

The air was filled with anguish,
You could hear the bagpipes cry (BAGPIPES)
The battleground shook from the march of the rook (TR: GUTTURAL YELL)
And his knights went galloping by. (SFX)

My queen sat calmly knitting Protected by two loyal pawns,

TR BRIT LADY: What's all that shooting and shouting and hooting
Out on our royal lawns?
We do not choose to lower ourself
To engage in such crude pursuits----
I'll stay right here, and ignore them, oh dear,
Such uncouth uncivilized brutes.

TK: Excuse me, ma'am. It's me. Your left rook.

TR BRIT LADY: Yes? Pray tell, what is it? Don't pester me when it's time for my tea---

TK: It's another queen, ma'am, come to visit.

GK: The other queen rode across the board (MOTORCYCLE)
She was not what you'd call polite.
She wore a T-shirt that said, "Eat my dirt,"
Her pants were pink, sequinned, and tight.

A cigarette dangled from her lower lip,
And she carried a six-pack of beer.
An axe and two knives and two .45s
On a long leather bandolier.

She was short and fat and ugly, And she yelled with all her might:

SS COCKNEY: Come out of your tower, you big fat coward, Get your butt on the field and fight!

GK: She planted herself in my queen's face With only a pawn in between.

TR BRIT: Who is that slut on the horse, tut, tut, She certainly is no queen.

Her hair is a mess, and that fishmonger's voice!
And her manners --- my, my --- she is rough.
Go see to her, rook, and tell her I'll brook
No insults from her, no insolent---- (TR STRANGULATION)

GK: And my queen fell flat on her back,
With the other queen's foot on her neck,
And she scratched and grinned and she broke wind (SFX)
As Freddie whispered---

TR KID: Check.

GK: I looked at my king and he looked at me---

TR BRIT DOLT: Oh dear--- In check? --- oh my. Well, it doesn't look good but maybe I could Find a way to play to a tie.

TR DOLT: Or maybe that pawn could run to the end And then be promoted to queen.

I'm sure we've not lost, but at least, at all cost, One must remain serene.

GK: And he stood there serene and regal and proud
As the enemy queen stood and laughed (SS LAUGHTER)
As proud as could be, and my monarchy
Was feeling understaffed.

A lowly pawn (TK) and a miserable knight (TR) And a rook made up our crew. (TK)

TR DOLT: It looks rather gloomy, but come, rally to me, And we'll figure out what to do. (TR KING DITHERING)

GK: And he brought out his charts and studied his books And he muttered:

TR: Ahem. Let me see. The hypotenuse squared by the root of the hair Of the dog times X over 3.

And carry the two, and divide by Y----

GK: And the handsome royal face Was very concerned, as he carefully turned And moved himself back one space.

And the pawn said--- TK: Brilliant!

GK: the knight said:

TR: Superb!

GK: And the rook said...

TK: Beautiful, sir.

GK: And the king said...

TR: My boy, it's a little known ploy That is known as the Spanish spur.

It was used by grandmaster Peter O'Bleness In 1978, When it seemed he had lost----

GK: And then the King paused, And Freddie said.....

TR: Checkmate.

GK: And his queen moved four spaces back (SS: CHUCKLE)

GK: Killing the rook with one blow (KONK, TK DEATH), And the king looked around at the bloody ground And there simply was no place to go.

TR DOLT: Impossible! Why---- it cannot be. I'll escape ---- I'll find a route!

GK: And the queen said:

SS: Oh yeah? You think so? Ha! Give up, ya big galoot.

TR DOLT: If I only could think--- I must persevere--- Dear me----- a route of escape----

SS: Throw down your sword and kneel on the board And kiss my foot, ya big ape.

TR DOLT: I must not give up ---- my army is scattered --- I simply have to regroup it.

SS: Hey, king! kiss my foot---- it's over, kaput, What's wrong with you? you stupid?

GK: My head felt strangely empty
It seemed like a terrible joke.
My king was alone on his tiny throne
Awaiting the final stroke. (TR DOLT)

GK: I said, "Look--- there's a polar bear out on the lawn!"
But Freddie did not blink his eyes.
I guess he had learned you should never turn
Your back on somebody who lies.
My king was dazed----

TR DOLT: Oh well--- toodle-ooo I surrender.

GK: He said with a sigh. And the queen yelled,

SS: Whee---hoo! Boogers on you!

GK: And she looked up and spit in my eye. (SS: SPIT)

SS: Let's play again. What do you say?
You want to be black or white?
Let's play again soon ----this afternoon----
Or after supper tonight.

GK: And later my king said,

TR DOLT: I've thought of a move
I'm sure would have won the day----
Look here--- if this pawn had not stopped but gone on---
Things would have turned out okay.

GK: I've dreamed of that game over and over Of the child who says......

TR: Can we play?

GK: And the battle roar (TUMULT) and the blood and the gore (SWACK, EUUUU) As the bodies are carried away (SFX).......

A game of Parchesi is gentle and easy
Or Uno or Sorry, my, yes.
And Monopoly is okay by me
But I do not play Freddie at chess.
```

---

## IC-1366: Go To Bed

- Title: Go To Bed
- Author (byline): Andy Griffiths
- Work: Just Disgusting! Pgs 35-52
- Publisher: Scholastic, Inc.
- Publication date as stated: Feb 2005
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ANDY, MOM, DAD, MOM & DAD
- Teaser before the introduction: Yes
- Spoken words (computed): 972
- Already set (do not supply): none

### Source block (context only)

```text
Author: Andy Griffiths
Book: Just Disgusting! Pgs 35-52
ISBN: 978-0439549547
Publisher: Scholastic, Inc.
Date (Month/Year): Feb 2005
```

### Introduction (context only: never use it for content warnings)

```text
Bedtime is supposed to be calm and peaceful . . . but clearly no one told Andy. Join me on a rollicking adventure that begins as an innocent moment on the couch but explodes into a full-scale bedtime war. You’ll witness desperate negotiations, mysterious illnesses, ghost infestations, legal threats, and a highly dramatic countdown to doom. Now let the show begin!

Go to Bed by Andy Griffiths
```

### Performance text (classify this)

```text
NOTE: Items in ( ) should be presented as an aside to the audience . . .

ANDY: (Pg 35-52) I’m lying on the couch reading a book (It’s really cool. It’s about this kid who won’t go to bed) When Mom comes in and gives me THAT look (You know the one)

MOM: Andy? Did you hear what I said? Put down that book and GO TO BED!

ANDY: But there’s no way I’m going to bed. (I bet the X-Men don’t go to bed at 8:30) It’s time to stall. It’s time to beg.

ANDY: Can’t I say up for just half an hour more? “No!” says Mom, and she points at the door. (She thinks that just because she points at the door, I’m going to go through it. Boy, is she in for a surprise) Twenty minutes? Ten minutes? Five minutes? One?

(I’ve already gained at least a minute, anyway, so I’m already winning, no matter what she says.) Please can I stay up? Please can I, Mom?

MOM: Come on. Mom knows best. If you weren’t so tired, you wouldn’t protest.

ANDY: (Mom’s argument makes no sense. Because if I argue, it proves, according to her, that I’m tired and I need to go to bed. But if I don’t argue, I end up having to go to bed, anyway. What does she think I am? An idiot?)

MOM: You’ve had a good time. You’ve had a big day. Just be a good boy and do what I say.

ANDY: (stomping his feet and shaking his head) I am NOT a good boy. I will NOT go to bed!

(There’s no way I’m going to give in. Especially since Dad’s not home) But then the door opens and in walks Dad. (Uh-oh) He’s got a big frown. He looks mad.

DAD: Not in bed yet, Andy? I’ll give you to the count of three!”

ANDY: (Dad always counts to three. I think that’s because it’s as high as he can count.)

DAD: One . . . (stares at Andy) Two . . . THREE!

ANDY: (The thing is, when he says “three” he’s not kidding around anymore. Better do what he says) I leave the room. I count to ten . . . [Count to ten] And then I go back in again. (You didn’t really think I was going to give up that easily, did you?) I’ve lost my pajamas! I can’t find my teddy! (I’m just making this up, of course. As if I still need a teddy bear – they’re just for babies) I’m hungry! I’m thirsty! I’m really not ready! But Mom and Dad ignore what I said.

MOM & DAD: ANDY, JUST GO TO BED!

ANDY: (Okay, they asked for it . . .) But I’ve got a sore finger and I’ve got a sore butt. I’ve got pains in my legs and my arm has a cut . . . (None of this is true – I’m actually 100 percent healthy, but they don’t know that) Not to mention my lice and my chronic back pain. My cloudy vision! My aching brain! My teeth! My tongue! My eyes! My nose! My tonsils! My kidneys! My stomach! My toes!

(Actually, the more I think about it, the worse I feel) I can’t go to sleep. I’ll wake up dead!

DAD: You soon will be, if you DON’T go to bed!

ANDY: (Did I hear right? Did my dad just give me a death threat?) I start to cry. (Not real crying. Just pretend) I start to moan. (to Dad) How would YOU like it up there all alone? How would you like it in your lumpy old bed with the lumps in your pillow sticking into your head? How would you like it if your pajamas were too tight and you had to lie there with a wedgie all night?” (I’ve had these X-Men pajamas since I was four. I’ve asked Mom for new ones, but she says they don’t make them in my size – that they only make them for little kids. I think she’s just trying to save money)

Now Dad’s really mad. He’s pretty near blowing. (to Dad) All right, I’m going! I’m going!

I climb the stairs toward my room. I open the door (With difficulty. There’s a huge pile of clothes on the floor) and face my doom. I’m all alone. I’m full of fear. It’s cold and dark and ghosts live here! (The ghosts live in my closet. That’s why my clothes are all over the floor. I’m too scared to open it and put them away.) A thumping noise! A spooky sound! I turn around and run back down. (I want my mommy!)

Mom looks at me. Dad shakes his head. (My mom and dad shake their heads a lot. Especially around bedtime)

MOM: I thought we told you to GO TO BED!

ANDY: But I’m scared. I heard a thump. It came from the closet. Something went bump! (It wasn’t the Boogeyman either. He lives under my bed) Don’t make me go back there! Don’t make me stay! It’s cruelty to kids! I’ll tell the SPCA!” (Society for the Prevention of Cruelty to Andys)

But Mom and Dad don’t seem too scared. (Probably because they’ve heard this one before)

MOM & DAD: (shouting) WE DON’T CARE,JUST GO TO BED!

ANDY: It’s not looking good. They’re tough nuts to crack. But I WILL win. I’m NOT going back. I’m going to give it one last try. It’s time to pull out My ultimate lie . . . (to parents) But I CAN’T go to bed. I can’t go now, I’ve got homework to do!” (Well, actually, it’s not a lie. I do have homework, but I have no intention of actually doing it.)

DAD: It’s too late now.

MOM: Yes, it’s just too bad!

ANDY: (They obviously need a little more persuasion. Well, here it comes . . . ) (wailing) But if I don’t do it, I’m doomed! I’m going to fail!” (Mom and Dad hate it when I say the F-word) I’ll be expelled! I’ll be out on the street. Who knows what thugs I’m likely to meet? I’ll join a gang! I’ll commit a crime! (Not just walking when the sign says DON’T WALK, either. I mean a really bad crime. Like running across the road without even looking. And going to bed without brushing my teeth. And writing rap songs with lots of swears in them.) I’ll end up behind bars doing time!

But there isn’t a jail that could ever hold me. I’d have to break out! I’d have to bust free! Every cop in the world would be looking for me. A fugitive is what I’d be.

(They’ll probably make a movie about me and everything) Hunted like an animal. Public Enemy Number One! Is that what you want for your favorite son?

I pause and wait for my words to sink in. (They look kind of stunned) Have I convinced them? Will I win?

DAD: All right. Perhaps we were wrong. Stay up if you have to. Stay up all night long.

ANDY: (Hmmmm. This could be a trick)

DAD: Just do your homework Just get it all done. We don’t want you living a life on the run.

ANDY: (No, I don’t think it’s a trick. They’ve swallowed my story hook, line and sinker.) I look at my dad. I look at my mom. I can’t believe they’ve bought this one. This is amazing!

This is great! I got what I wanted! I’m staying up late! But then Mom and Dad get up out of their chairs, walk out of the room, And start climbing the stairs. (Huh?) (calling after parents) Hey, where are you going?

MOM: We’re tired. We’re going to bed.

ANDY: (She does look tired, actually. So does Dad. It must be awful being that ancient) But what about me, here all alone? I’ll be all by myself! I’ll be all on my own!

(Parents can be SO selfish.)

(to parents) You CAN’T go to bed! Not at THIS time of night! You’re older than me! (It doesn’t make sense. The whole point of being a grown-up is that you don’t have to go to bed early.) It just isn’t right!

DAD: (yawns heartily) Good night. Don’t forget to lock up and switch off the light.

ANDY: (This has never happened before. Never!) Hey, wait! . . . . (to audience) but they’ve disappeared. I don’t like this -- it feels kind of weird. (I mean, what’s their problem. Don’t they LIKE spending time with me?) I’m all alone. I’m full of fear. I sit on the couch. I don’t like it here. (Not anymore)

What was that noise? I heard something squeak. (No, it didn’t come from me. Or my butt) Something went bump! Something went creak! It could be a mouse . . . but it might be a bat! (A vampire bat that came to suck on my blood. Aagggghhhh!) No, I’m just being silly, it’s probably the cat. But what am I thinking? (shouting in fear) WE DON’T HAVE A CAT! This is creeping me out!

I try to calm down. I turn on the TV. But the first thing I see is a horror movie.

(Normally, I love horror movies, but it’s not what I need right now) The living room fills with horrible shrieks! It’s a film about ax-wielding blood-sucking freaks.

I get up from the couch Like a rocket I zoom – I shoot up the stairs and into my room!

Before I know it I’m cozy and calm with my favorite old teddy snuggled under my arm. (All right, I admit it. I DO have a teddy bear. In fact, I have a few. And I like to cuddle them in bed. So what? I bet you would too if you had ghosts in your closet) I pull the blanket up to my chin. I’m safe and I’m warm and I’m all tucked in.

(Sure, I know I didn’t want to go to bed before, but I’ve changed my mind, okay?)

Yes . . . I know I’m in bed. But just you wait . . . Tomorrow I’ll stay up REALLY late!

(Good night)
```

---

## IC-1367: God’s Favorite

- Title: God’s Favorite
- Author (byline): Neil Simon
- Work: The Collected Plays of Neil Simon, Volume II; Pgs 475 - 548
- Publisher: Penguin Publishing Group
- Publication date as stated: Nov 1986
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: JOE, LIPTON’S VOICE, LIPTON
- Teaser before the introduction: Yes
- Spoken words (computed): 1834
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Simon
Book: The Collected Plays of Neil Simon, Volume II; Pgs 475 - 548
ISBN: 978-0452263581
Publisher: Penguin Publishing Group
Date (Month/Year): Nov 1986
```

### Introduction (context only: never use it for content warnings)

```text
Imagine if God sent a messenger to your house, but instead of a glowing angel with wings ,you got Sidney Lipton: a twitchy, cinematic-obsessed person in a "G" sweatshirt who acts like a pizza delivery driver bringing a box full of disasters -- a cosmic intern who’s just trying to hit his plague-delivery quota so he doesn't get fired.

Will Joe renounce the Almighty or will he remain . . . God’s Favorite by Neil Simon
```

### Performance text (classify this)

```text
NOTE: Sidney Lipton could be played by either gender. Joe is forlorn and defeated. He sighs mournfully. The room is in darkness except for the moonlight shining through the French door. He looks up and speaks softly and reverently)

JOE: (Pg 494-495) Am I wrong? ... Is all of this too much for one family? If it is, then why did You give it to me? It's enough already, dear Lord. Don't give me any more. . . Just David. Give me back my David . . . If it be Your Will, dear God, that's all I ask. Amen!

LIPTON’S VOICE: (A voice from somewhere in the room itself, is heard) Amen!

JOE: (stops in his tracks, then wheels around, shocked) What? Who's there? Who said that?

LIPTON’S VOICE: Don't worry. It's not who you're thinking.

JOE: Who is it? I can't see you.

LIPTON’S VOICE: I can't see you either. I lost my glasses. Are the lights on or off? I can't see a damn thing.

JOE: Stay where you are! Don't move. I could have the police here in two minutes.

LIPTON’S VOICE: You're lucky. In my neighborhood you could wait for them all night! Would you please turn the lights on? I get very nervous in the dark.

JOE: (Pg 495-509) (turns on lights) All right, now who do you -- (But there is no one there) Where are you? ... WHERE ARE YOU? (He turns around quickly ... Silence. From behind the huge sofa, SIDNEY LIPTON appears, crawling and feeling the rug with his hands)

LIPTON: Don't get excited, I'm just looking for my glasses. (Continues to search. Not a very impressive-looking person, wearing khaki slacks, a thin raincoat, white sweat socks, Hush Puppies, a tweed cap -- a potpourri of cheap clothes) I still can't see. Where am I, on the floor?

JOE: What do you mean by breaking into my house? Who are you?

LIPTON: (Still feeling around on the floor) Oh, gorgeous rug. This is all handwoven. Must have cost a fortune. What is it, Persian?

JOE: Never mind the rug, I asked you a question. Who are you?

LIPTON: (Still on his knees) The name is Lipton. Sidney Lipton... Where am I, still on the floor?

JOE: (Takes the glasses out of his pocket) Here. Here's your glasses.

LIPTON: You found them? (Puts out his hand) Oh, good. Could you put them in my hand, please? (Joe puts the glasses into Lipton’s hand)

LIPTON: (Puts the glasses on, still on their knees) Ohh. Ohh, yes, there we are ... (looks up) Ohhh! This -- this is gorgeous! This is what I call a gorgeous room.

JOE: Is that why you broke in here?

LIPTON: Certainly not. I'm here on business. Very important business.

JOE: If you have business with me, you make an appointment like everyone else.

LIPTON: (Looking around) I'm not like everyone else. (Points to an ornate armchair) I love the chair. I don't fall in love easily, but I am in love with this chair.

JOE: Is that what you are? An antique dealer?

LIPTON: Antiques? No. Antiquity, perhaps.

JOE: What does that mean?

LIPTON: What does anything mean? What is the meaning of "meant"? What is real or unreal? What the hell are we talking about? I'm still dizzy from that fall I took.

JOE: I can't make you out. You're not a burglar, that I can tell.

LIPTON: A burglar? No. An antique dealer? No. But who am I? What am I? Why am I here? That's the mystery, isn't it? God, I love a good mystery.

JOE: If you don't tell me who you are . . .

LIPTON: Ah, ah, you're losing patience, aren't you? Mustn't lose patience, Joe. All in good time. I have cramps in the head. Did you ever get cramps in the head?

JOE: A lunatic! A lunatic wandered into my house from the snow. Why do I bother talking to you?

LIPTON: Curiosity! There is something curious about me, you've got to admit ... All right, enough chitchat. Let's get down to brass tacks, Joe Benjamin. Why, at this hour, on this night, in this year, in this house, on this rug, in these shoes, do I, Sidney Lipton stand before you? WHAT BUSINESS DO WE, STRANGERS TILL NOT FIVE MINUTES AGO, HAVE UNTO EACH OTHER?

JOE: Are you selling something? If you're a salesman, I'll kill you with my bare hands!

LIPTON: Do I look like a salesman? I am a man of flair, of fancy, a bizarre and unique guide to the world beyond our world.

JOE: A travel agent? Is that what you are, a travel agent?

LIPTON: (Yells, angrily) You have no imagination! What do I have to do to tell you who I am? Think, Joe, think!

JOE: I think you're a nut, that's what I think, and I want you out! (He grabs Lipton by the arm) Out, do you hear me? OUT!

LIPTON: Easy, easy. No rough stuff, I'm not a physical person.

JOE: Ten seconds and I throw you out that window head-first. One, two--

LIPTON: Don't force my hand. I deal a heavy hand

JOE: Three, four-

LIPTON: (Stops; points a finger) STAY! I STAY YOU! Yea, you would banish He who brings thee the gift of life and the eternal bliss? ... Forget that! Forget I said that. That was a slip. A boo-boo. Slipsies!

JOE: There's something funny going on here. You're not who you pretend to be at all, are you?

LIPTON: Aha! Aha, getting somewhere. Getting warm ...

JOE: This is all an act. A game. . . Somebody sent you, didn't they?

LIPTON: Hot! Getting hot!

JOE: Somebody sent you to get something from me!

LIPTON: Hotter! Hotter! Boiling hotter!

JOE: Somebody important who knows me sent you to get something that I have that has enormous value. Something I have that no other man on earth has.

LIPTON: Scalding! Steaming lava! Two weeks in a sauna bath!

JOE: My Bible! My Gutenberg Bible!

LIPTON: Cold. Freezing cold. Winter. A room for two in Toronto.

JOE: Damn you, what is it?

LIPTON: Hey! Hey hey hey! Calm, please. Take it easy. Let's not break our blood vessels. The last thing I want is for you to get sick. I mean, you are in good health, aren't you?

JOE: (Knocks wood) Thank God!

LIPTON: Hot! Boiling hot! Getting hot again!

JOE: (Screams) What are you saying? You're driving me crazy with these stupid games.

LIPTON: Temper, temper. And I was told you were such a patient, wonderful man.

JOE: Who told you? Who told you I was a wonderful man?

LIPTON: (Softly; side of their mouth) You know. . . He did.

JOE: Who's he?

LIPTON: He! Him! Capital "H," small "i" small "m" ... Do I have to spell it out for you? Went on and on about you. I'll tell you the truth, you're His favorite. Yes, you, Joe Benjamin, are considered to be His -- that's capital "H" again -- His absolute favorite. And that is the honest to God's truth. (makes a cross on his chest, then a circle, a square, all sorts of signs)

JOE: I can't understand what you're saying.

LIPTON: Can't understand or afraid to understand?

JOE: I'm not afraid of anything on the face of this earth except God himself.

LIPTON: BINGO! BULL'S-EYE! Ding-a-ling-a-ling-aling! Fire, fire, fire! Home run, home run! (jumps around in an excited jig)

JOE: STOP IT! I beg of you to stop it and tell me who you are, in plain, simple language. Who are you, please?

LIPTON: (stands erect, clasps his fingers together; solemnly) Very well. Forgive me, my son. I have taken this bizarre form, so that I might present myself to you in some acceptable dimension, for had I told you the truth straight on of my identity, even I could not have given you the power to accept or comprehend. Yes, Joe -- I am -- who you think I am!

JOE: Are you trying to tell me that you're -- that you're -- are you trying to tell me --

LIPTON: Say it, Joe. You will only believe if you say the words yourself.

JOE: God? Are you trying to tell me that you're God?

LIPTON: Who? . . . God? GOD? Is that what you thought? Nothing personal, but that's really crazy. Do I look like God? Would God wear glasses? I mean, if anyone's going to have good eyes, it's going to be God. No, Joe, I'm sorry to disappoint you, but I am not God.

JOE: Then who are you?

LIPTON: I'm a friend of God's. Not a close friend. We met a few times.

JOE: You met God?

LIPTON: Twice on business, once on a boat ride.

JOE: What business? What business do you have with God?

LIPTON: I deliver messages!

JOE: You're a messenger from God?

LIPTON: Important documents only; no packages.

JOE: All right, if you're who you say you are

LIPTON: I am.

JOE: Let me finish!

LIPTON: When you finish, I am!

JOE: If you're a messenger of God -- then where do you come from?

LIPTON: Oh, you mean like heaven? The Eternal Paradise? A place like that?

JOE: Yes.

LIPTON: Jackson Heights. It's in Queens, just over the Triborough Bridge.

JOE: But you said you met God.

LIPTON: Not face-to-face. There's always a big light over Him -- the glare is murder.

JOE: GOD! GOD! HAVE YOU SEEN GOD?

LIPTON: I didn't actually see Him. I heard Him. He blessed me.

JOE: God blessed you?

LIPTON: I sneezed and God blessed me -- what do you want from me? (Loudly) I cannot deliver God's message until you accept that I am God's messenger! What do I need to prove it to you, wings?

JOE: Tell me why? Then maybe I'll believe you. Why would God send a message to me, Joe Benjamin, a plain, simple, ordinary man?

LIPTON: To test your faith, that’s why! ... Strike that! You didn't hear it! Erase! I'm not supposed to tell you that.

JOE: Test my faith? My faith? Are you saying that God doesn't believe my faith in Him?

LIPTON: Oh, no. Not-Him. He believes! God's crazy about you ... It's the other one. (Softly, slyly) You know the other one. From downstairs ... Mr. Nasty … Bad, Bad Leroy Brown ... Oh, for God's sakes, you have to spell out everything for you ... Satan! Lucifer! The Devil, all right?

JOE: (Moving toward the phone) I've wasted enough time with you, I'm calling the police!

LIPTON: (Points a finger again) Stay! I stay you! I render you powerless! All right, I can't do it. I'll tell you everything . . . God and Satan were sitting around having one of those boring philosophical debates -- this was a week ago Tuesday. And Satan was sitting there in this pink suit -- gorgeous tan, little mole on his cheek ... And Satan says there is not one man on the face of the earth, who would not renounce God once the Devil put enough heat on. To which God said -- this is a quote, “one man would never renounce. And that man is ... (Makes a bugle sound) Tatum ta tum ta tum ta tum ta taaa ... JOE BENJAMIN!” Thrills, right? ... So they make a bet and the bet is, the Devil will make your life so miserable, you'll renounce God!

JOE: You think I would renounce God? You think so little of man that he would re-nounce God in the face of adversity?

LIPTON: I've seen people with a burning engine on a 747 who would sell out God in a second for a little good news from the pilot (Takes out a folded, dirty scrap of paper) You ready?

JOE: Let me see that.

LIPTON: (Pulls it away) I have to read it. It's not official unless I read it ... "To Joseph Melvin Benjamin, devoted husband and father ... if pain, calamity and disaster do not in any manner whatsoever appeal to you, then renounce your God!" That's it! Message delivered. No tip necessary, Good night, good luck, God bless you ... but I doubt it! (puts the message back in their pocket)

JOE: I will never renounce God, do you hear me? I fear Him and love Him but come hell or high water, I will never renounce Him!

LIPTON: Can I be honest? You can count on the hell and high water. Good luck, Joe. And no matter what terrible things happen to you, remember that God loves you! (a fire engine clanging in the distance)

JOE: What's that? What's going on out there?

LIPTON: (Looks out the window) Looks like a fire. Near the water ... Where's your factory?

JOE: Near the water.

LIPTON: Ohh ... Look at that burn. Like a cardboard box ... What do you make?

JOE: Cardboard boxes.

LIPTON: Ohh ... Well, I wouldn't worry unless I got a phone call. (Phone rings. They both look at it)

JOE: It's not my plant. My plant is a hundred percent fireproof. (picks up the phone) Hello? Eddie? ... What is it? ... What? ... What?

LIPTON: One more "what" and you're in trouble.

JOE: (Into the phone) WHAT?

LIPTON: What is it, a disaster or a calamity?

JOE: (Into the phone) The whole plant?

LIPTON: Oh, a catastrophe, wonderful!

JOE: Thank you, Eddie ... I know it wasn't your fault. (He hangs up)

LIPTON: How much did the insurance cover?

JOE: (Dazed) I didn't have insurance. I didn't believe in insurance ... GOD was my insurance.
```

---

## IC-1368: Goliath

- Title: Goliath
- Author (byline): Simon Rich
- Work: Glory Days, Pg 167-187
- Publisher: Little, Brown and Company
- Publication date as stated: July 2024
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, GOLIATH, REPORTER, DAVID, SHANA, JULES, SKEEBO, AUDIENCE, GOLAITH
- Teaser before the introduction: Yes
- Spoken words (computed): 1307
- Already set (do not supply): none

### Source block (context only)

```text
Author: Simon Rich
Book: Glory Days, Pg 167-187
ISBN: 978-0316569002
Publisher: Little, Brown and Company
Date (Month/Year): July 2024
```

### Introduction (context only: never use it for content warnings)

```text
ANNOUNCER’S VOICE: Ladies and gentlemen . . . Children of all ages! Welcome to the Death Match!

NORMAL VOICE: We all know the story of David and Goliath. It’s the ultimate underdog tale. The scrappy kid. The giant bully. One sling, one stone, one perfectly placed shot . . . and boom! Sunday school legend . . . But what if that’s not exactly how it went down?

ANNOUNCER’s VOICE: GOLIATH! Towering warrior! Divorced dad of a 12-year-old who needs private school. (beat) and . . .DAVID! Brave; marketable; relatable! He’s got a fragrance line!

NORMAL VOICE: This is a story about fame, privilege, public opinion and what happens when history is written by whoever has the better manager.

ANNOUNCER’S VOICE: Because in this arena, the real weapon isn’t a stone!

NORMAL VOICE: (whispers) It’s publicity. (beat) Goliath by Simon Rich
```

### Performance text (classify this)

```text
NARRATOR: (Pg 167-187) Goliath looked down at the familiar crowd of reporters. The reporters were vigorously wiping down their slates to make room for his sound bites. Goliath couldn't help but feel a tiny surge of pride. He'd been fighting people to the death for years, and somehow everybody was still interested.

GOLIATH: (calling on a reporter) You have question for Goliath?

REPORTER: What are your thoughts on fighting David?

GOLIATH: (unsure, scratching his beard) Who is David?

DAVID: (enters, floppy hair bouncing) Wow, this is so cool! A real-life press conference! So how does this even work? Do I call on people myself? Wow! Okay, I guess I'll start with ... Shana.

SHANA: The question we all want to know is, what makes you believe that a small, poor, unarmed child can defeat a well-known giant in a death match?

DAVID: I'm just grateful for the opportunity to fight at all. Growing up small, poor, and unarmed, I never imagined I'd ever get the chance to do anything noteworthy. It's all thanks to my mom. Being a single mother is no joke. If you ask me, she's the real underdog death fighter.

REPORTER: My question is about determination. Do you have it?

DAVID: (commanding the room) Great question. Yes.

GOLIATH: (baffled he’s not in the spotlight) That was two in a row for David. Usually, one question for Goliath, one for other death fighter, then Goliath speak again.

REPORTER: Okay, I've got one: How impressed are you by David?

GOLIATH: (confused) David is boy. Goliath is giant. We should not even be fighting.

SHANA: (solemnly, throwing a disapproving look at Goliath) David, how would you respond to Goliath’s hurtful statement?

DAVID: I ain't doing this for me. I'm doing it for all those kids in Bethlehem who get told every day of their lives, 'You'll never get to be a death fighter.' I'm fighting for Bethlehem, and D's always gonna rep the Beth, straight up. D's gonna be D. No fronting, no filter. Just some kid from the Beth, trying to shine. That's who I am. That's D.

GOLIATH: (saddened that no one was paying attention to him) Goliath hungry. Okay . . . Goliath go. ******

NARRATOR: Goliath ate a full-size pig (Goliath burps) It had been a long, strange day, but now he was at peace, sitting across from his 12-year-old daughter, Jules.

JULES: (in typical pre-teen giant fashion) Mom says you need to call the school. Something about tuition . . .

NARRATOR: Middle school so far had not been easy. The other kids made fun of her for the tiniest of things: her height, her width, the depth of her voice, the fullness of her unibrow, the crash of her steps, the unsettlingly audible sound of her eyeblinks. (Jules blinks awkwardly) Private school had seemed like the only option. [But] Goliath was in serious trouble. Gretchen had gotten almost everything in the divorce. His death fights paid decently, and there were some incentives built into his contract, like if he won in the first round. Even if he managed [to defeat] David, he still wouldn't be able to cover Jules's tuition. His only hope was to find an additional source of income. Luckily, he knew just where to start.

******

GOLIATH: (taking a seat in Skeebo’s office) Goliath never do endorsement before . . .

SKEEBO: Neither had David when he met me. Now the kid's hot! Signature sandal, signature tunic. They took a drop of sweat to make a fragrance and it sold out in a day. Kid's got a production company, D Street, started as a vanity label for his raps, now the Saudis want to invest. (beat) Let's get into it. I asked around town, put out a bunch of feelers with all kinds of brands. Unfortunately, there are no offers.

GOLIATH: (shaking his head in disbelief) Why not?

SKEEBO: The brands all want David. Do you realize he's gotten so popular that people are naming their kids after him? No joke. 'David' is becoming, like, a normal, common name.

GOLIATH: Why don't people like Goliath? Goliath has been winning for years.

SKEEBO: That's the problem. Audiences just don't find you appealing. They see David as way more authentic, root-able, and likable.

NARRATOR: Goliath growled in frustration. (Goliath growls) He understood why people sympathized with David. He was small and about to be murdered. But it's not like Goliath had it easy. If the public knew the pressure he was under, then surely their allegiances would change.

GOLIATH: Goliath will get endorsements. Goliath just need to show people real Goliath. ******* Shanna’s Talk Show*****

SHANA: My next guest is an undefeated death fighter who has represented Philistine for years. His next match will be against David, who represents everybody here as well as the one true God. Goliath, thanks for being with us . . . I understand there's something you would like to clear up.

GOLIATH: (clearing his throat, he has obviously prepared) People think Goliath have it easy. But really Goliath have things hard. (to audience earnestly) When Goliath was young, Goliath had to eat more food than other kids. Sometimes Goliath would have to sit at table 20 minutes longer than everybody else. So there is that. Also, it is not easy killing people. Sometimes, blood splashes onto Goliath's clothes and it is wet. And number three: it is hard for Goliath to buy pants. In conclusion: Goliath history's greatest victim.

AUDIENCE: Boo!

SHANA: Forgive me for being skeptical, because when I look at you, I don't see hardship. What I see, frankly, is a lot of privilege.

GOLAITH: (quick with a denial, he pleads to the audience) People think Goliath is rich, but Goliath is not rich. If you do not start worshipping Goliath, Goliath will not score cushy endorsement deals, and he will not even be able to send daughter to private school! He will have to send her to public school with poor people! People as poor as you!

AUDIENCE: (even louder and throwing sand) Boo!

NARRATOR: The truth was that other people decided who you were, and once they did you could never change their minds. **** The Day of the Death Match*****

(sound effects of trumpets blaring to announce the match)

GOLIATH: (flexing for the audience) Goliath have message for haters! Your beloved David is about to die! And not in a normal way! Think of craziest way you can think of! It will be crazier than that!

NARRATOR: Goliath rarely spoke before his fights, preferring to let his killing do the talking, but this time he'd screamed himself hoarse. And by the time he climbed into the ring, it was obvious his taunts had made an impact. David's normally buoyant blond bob lay flat on his head, matted down by sweat, and his bright blue eyes looked bloodshot.

DAVID: (calling to his manager) Yo Skeebo! Maybe we should postpone? (frantic breathing)

GOLIATH: (cracking his neck and stretching, he points at David) Goliath kill you soon!

DAVID: (fumbling for his slingshot, it wobbles in his hands as he slides in a pebble and feebly draws it back)

NARRATOR: The crowd fell silent; they knew this shot would be David's one chance.

GOLAITH: (in slow motion, watches as the stone drifts toward him)

NARRATOR: He thought about the trophies he had won, the belts he had hoisted. He thought about the way it felt to win a fight, the unmatchable clarity that could come only with victory, that sense, however fleeting, that you had been born for a reason. So far, his fights had all been easy. This one would be hard.

GOLIATH: (takes a deep breath as the pebble bounces harmlessly off his brow, then in an epic overacting flop . . . ) Ow! Goliath lose death fight! (he staggers to the ground)

NARRATOR: He knew it wasn't the kind of performance that would have passed muster in theater club, but the crowd seemed to buy it, screaming and crying in ecstasy.

DAVID: (celebrating his win) Yeah, bruh! All day!

NARRATOR: Goliath kept his eyes closed until the cheering faded into silence. When he finally opened them, Skeebo was smiling down at him, holding a sack of silver pieces. Their deal had been simple. In exchange for the dive, Goliath would receive an anonymous stake in D Street Productions going forward. As long as David's star continued to rise-and it assuredly would after this upset-Goliath could cover Jules's tuition indefinitely.

SKEEBO: (Holding payment out of reach as Goliath gleefully reaches for his payment) Hold up! You still gotta sign an NDA.

GOLIATH: What is NDA?

SKEEBO: (looks over his shoulder then whispers ominously) It means you can never tell anyone what happened here. Not the public, not the press, not David. Not even your own family!

NARRATOR: For the first time, Goliath pondered the full scope of what he had agreed to. This battle was the kind of thing people might remember. It was possible the public would even embellish his loss over the years, saying he'd died in the fight, or that David had cut off his head. Even Jules would grow up thinking he'd been beaten. His legacy of greatness would end, and instead, he would become a reference point for failure, an eternal symbol of humiliation. . .

GOLAITH: (contemplates for a moment, shrugs then signs with a flourish and grabs the cash; then to audience proudly, tapping his brow) Goliath have smarter idea. (winks)
```

---

## IC-1369: GPS

- Title: GPS
- Author (byline): Bruce Kane
- Work: I Can Explain - Six One Act Plays and a Monologue, Pgs 1-15
- Publisher: Lulu.com
- Publication date as stated: April 2013
- Event as filed: Humorous Interpretation
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
AI and robotics are no longer confined to the realms of science fiction; they are an integral part of our present and will undoubtedly shape our future. From autonomous vehicles navigating our streets to AI algorithms making complex decisions regarding the very news stories we see on our social media feeds, the influence of AI technology is growing. Are we ready?

GPS by Bruce Kane
```

### Performance text (classify this)

```text
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

## IC-1370: Gym Class – Worst Game in the World

- Title: Gym Class – Worst Game in the World
- Author (byline): Paul Feig
- Work: Kick Me: Adventures in Adolescence, Pgs 121-139
- Publisher: Three Rivers Press
- Publication date as stated: Sept 2002
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: FIEG, WENDELL, FEIG, NORMAN, STUDENT 1, STUDENT 2, STUDENT 3, KARL, RICK
- Teaser before the introduction: No
- Spoken words (computed): 2141
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paul Feig
Book: Kick Me: Adventures in Adolescence, Pgs 121-139
ISBN: 978-0609809433
Publisher: Three Rivers Press
Date (Month/Year): Sept 2002
```

### Introduction (context only: never use it for content warnings)

```text
Welcome to Middle School Gym Class! A time ripe with embarrassment! Admit it. You remember – Showering with a group of vicious peers -- Gym clothes that could stand on their own because no one EVER took them home to be washed. But nothing compared to Dodgeball . . . Bombardment . . . Killer . . . No matter what you call it, it is one of those games of childhood that you either loved or loathed. For the athletically superior, it was a chance to prove some semblance of macho superiority. For others, it was little more than an hour of getting mercilessly pummeled by flying rubber projectiles. Either way, it’s one of those experiences that you don’t soon forget. Let’s take a look back at this sadistic little part of physical education that left such a lasting impression on many of us.

Gym Class –Worst Game in the World from Kick Me: Adventures in Adolescence by Paul Feig
```

### Performance text (classify this)

```text
FIEG: (Pgs 121-139) There was one class that I never enjoyed, that I faced each day with stomach-twisting dread: gym class. I must admit that I didn't mind gym class as much when I was in grade school because, back then, it was literally just running around. We pretty much played easy games and never really worked up a sweat. And for that reason we were allowed to do it all in our school clothes.

When I got to junior high, however, I was confronted with something that I found quite disturbing -- gym clothes. You see, being told I had to wear gym clothes in PE class meant I had to change into them in front of my classmates. And this was not something that I wished to do. At all.

See, I was an only child, and so I never had to take my clothes off in front of anybody. Even my parents. Even when I took a bath, a thick layer of Mr. Bubble, my bath time guardian, made sure my in-tub nakedness would be hidden from any prying eyes. And then suddenly, thanks to a guy named Mr. Wendell, our new gym teacher, I was expected to show 100 percent of myself to a bunch of kids I had grown up with . . . who didn't like me. Where was Mr. Bubble when I needed him?

WENDELL: (sounding like a drill sergeant) All right, ladies. This is the locker room. You'll be changing over in this area, where the lockers are. And over here are the showers. Each of you will be required to shower after every class. No exceptions.

FEIG: I figured I must have died and gone to hell. That could be the only excuse for someone's telling me I was going to have to bathe in public. I take a shower every morning before I go to school. I shampoo and blow-dry my hair. I brush my teeth. I'm the cleanest seventh grader this school has ever seen. He can't possibly be talking to me. (to Mr. Wendell) Do we all have to shower?

NORMAN: Of course you do. What do you want to do? Stink all day?

WENDELL: All right, boys. Change into your gym clothes. We're gonna have a little fun on your first day.

FEIG: I guess I must have had an abnormal amount of hang-ups for a 12-year-old, because no sooner were the words “change into your gym clothes” out of Mr. Wendell's mouth than all my classmates just dropped their pants and changed. None of them really seemed to care that they were standing around in front of each other in their underwear. It was clear [that] I was going to have to put my modesty on hold and change in front of this group of alpha males. I let my mind remove itself to somewhere more pleasant as I took off my pants. And as soon as they were off, my face went white. I had forgotten about something. A few weeks earlier, my mother had gotten into a hobby called Cameo, which was the art of drawing designs and pictures on fabric with these special ink pens. And one of the first projects she undertook was to hijack a pair of my underwear and draw a big dark red butterfly right on the back. And that was the pair of briefs I had worn to school this day. I was frozen. Did anyone see it? My mind started to race, in full panic mode.

NORMAN: What is that?!

FEIG: The whole class was moving toward me, staring at the butterfly on the back of my underwear, all of them with stunned, incredulous looks on their faces.

NORMAN: Oh my God. It's a butterfly!

FEIG: All hell broke loose. Apparently, they'd never seen decorative underwear and the sight of it had turned them into the kids from Lord of the Flies.

WENDELL: (entering the locker room angrily) What the hell's going on in here?!

FEIG: I figured I was saved.

NORMAN: (pointing at Feig’s butt) Feig's got a butterfly on his underwear!

WENDELL: (raising an eyebrow) He does? Let's see it, Feig.

FEIG: So much for being saved. Mr. Wendell leaned over and took a good close look at my mother's handiwork.

WENDELL: A butterfly? That's lovely, Feig. Was it always there or did it use to be a cocoon? (laughing) All right, guys, all right, enough of this. Get dressed and get into the gym." (starting to exit, then turning back to Feig) Oh, and Feig? You can flutter out with the rest of them.

FEIG: Thanks, Mr. Wendell. You're really an inspiration to us all.

STUDENT 1: Hey, Feig, uh . . . nice butt-erfly

STUDENT 2: Does your dad have one on his underwear, too?

STUDENT 3: I bet that butterfly . . . uh . . . wishes that it . . . was . . . uh . . . that it didn't have to smell your butt all day.

FEIG: I was the last to finish changing, as I wondered if I could convince my parents to transfer me to an all-girls' school.

WENDELL: All right, everybody, being that this is the first official day of gym, I thought we'd do something a little different. The game I'm going to let you guys play is ... Killer.

FEIG: It was not going to be something good.

WENDELL: (pacing in front of the class) The object of the game is to be the last man left standing. Okay, in order to play Killer, you will be divided into two teams. Each team will take one side of the gym. Then, when I blow the whistle, you will throw the balls across the gym at the other team without crossing the center line. If you are hit by a ball, you're out. If you catch a ball, the person who threw the ball is out. Got it?

FEIG: Unfortunately, I did. And I realized that this was the last game in the world I wanted to play.

NORMAN: These balls are too big. (picking up a cantaloupe size rubber ball) When my brother and I play, we use tennis balls. They really hurt.

FEIG: Yes, I thought, that really does sound like more fun. Maybe if we're really good, one week Mr. Wendell will let us use golf balls and Chinese throwing stars.

WENDELL: (clapping his hands) All right, girls, grab a ball and choose a side.

NORMAN: Hey, Butterfly? You're dead!

FEIG: Oh great, I thought. I was about to be the star of my gym class's production of The Lottery. It was at this moment that I had to reflect on the question: "Exactly why do we have gym class in the first place?" Was it supposed to build morale? Self-esteem? To make us more confident about our bodies, our minds, and our abilities? That's what my father always told me, but if that was the case, then my school district was failing miserably. [One thing] was clear. Everyone in this gym wanted to see me dead. I guess putting a butterfly on your underpants was right up there with defiling the American flag.

Mr. Wendell walked out onto the floor, whistle in mouth. He took a deep breath . . . the whistle blew. And I descended into hell. BLAM! I suddenly realized that these "harmless" balls were actually lethal weapons, when thrown by my classmates. If competitive sports were supposed to inspire teamwork, then my butterfly underwear had apparently inspired this group of fun-loving lads into a lynch mob.

I knew one thing. I had to keep moving. Fast. (enacts the game as he speaks) The balls were coming in at a blinding rate. I ran back and forth with a sort of high-stepping circus-horse gait, arms and legs flailing wildly. Keep moving. Keep moving. That's all my brain could tell me to do. Life hadn't prepared me for this type of evasive action. BOOM! The next volley came in. I dodged the attack. A few of my "comrades" fell. They had been hit. Ha. I had survived the initial surge. Maybe I would be okay. BOOM! Another hit. BOOM! BOOM! I felt like I was going to puke. BOOM!. Every time I looked around, I noticed that more and more of my teammates were gone, taken out by the Playground Balls of Death. And because of this, I was quickly on my way to becoming one of the last players left, an honor I definitely didn't want. Something had to be done.

Karl Scott was throwing the large ball at our team and then letting it rebound back to him. I figured that once that ball hit the bleachers, its velocity would be decreased, and I could then step in front of it and stop it from rebounding back across the gym. So, I ran in to get it. Karl Scott saw me coming.

KARL: You're dead, big-nose!

FEIG: He heaved the ball and I ducked at the last minute. BOOM! Great. This wasn't working. BOOM! He threw again. And again I ducked and let it go by. BOOM! Karl missed again. He was definitely getting frustrated now.

KARL: Give up . . . You know you're gonna get it.

FEIG: (with a false sense of bravado) From you, Karl? Not yet. Not without a fight. (to audience) Karl got a look of determination, wound up, and heaved the ball at me again, this time as hard as he could, delivering what he knew would be the Death Blow. The ball came straight toward my face. Suddenly, the world seemed to shift into slow motion. The ball was headed toward me, too fast to dodge, right on course to take my head off. I saw Karl Scott's face over the top of the ball. He had a real smug smile, happy to be the one to bring the Butterfly Boy down.

Then, suddenly, everything went back to normal speed. In a last futile act of self-preservation, I held my hands out in front of me and closed my eyes. I felt the ball break through my fingers, skid down my arms, and explode into my chest. Is this what it's like to be shot? I wondered. The force knocked me right off my feet. I slammed onto the ground, butt first, and hit my back against the wooden beams on the wall. A hot pain ran through my chest where the ball had hit. Everything was spinning from the shock.

Then, I heard something strange. Silence. Absolute silence. I looked down and saw that the ball he threw was still lodged between my arms and chest. I had caught it. Karl was out. Because of me, Karl was OUT. Oh my God, I thought, eyes wide. I did it! All right! They gotta respect me for this.

I immediately pictured a scene in the locker room with all of them coming up to me and giving me a "We're sorry we misjudged you, you're really an okay guy" speech and then singing "For He's a Jolly Good Fellow." Maybe they'd even all get butterflies cameoed on their underwear in a show of solidarity. Because, whether they wanted to admit it or not, I had just proven myself.

BOOM BOOM! I was thrown quickly back into reality when two balls slammed into the ground on either side of me. I was now the only one left on my team. Five of the enemy remained, their eyes trained on me. Definitely not the position I had been looking to get into. GET ME OUT OF HERE! They moved closer.

Well, here goes, I figured. I'm gonna get myself out. I threw the ball high in the air, right toward Rick Jones. An easy catch, Rick. Just stick out your arms and you'll be the King of the Locker Room. Rick sidestepped out of the way, casually, right at the last moment. Then Rick looked at me and shook his head, scary calm on his face.

RICK: You ain't gettin' out that easy, Feig.

FEIG: Suddenly, I heard a whistle blow. It was Mr. Wendell. He was actually going to stop this. My persecution has ended! The man finally came through for me.

WENDELL: No borders, boys. The field is open. That means you don't have to stay on your side of the center line. So, c'mon, get in there and let's finish this game up.

FEIG: Oh, GREAT! The time had come. Life as I knew it was about to end. The five mouth-breathers surrounded me. I was dead. I looked over to the sidelines at my classmates, boys with whom I had grown up. I saw Mr. Wendell, the man put in charge of my physical development. I saw them all, the compassionless bunch. Would the sight of a trapped person, a cornered, defenseless animal, stir some sort of sympathy within them? There was nothing left to do. I officially hated these guys. I looked right at them.

(breathing heavily, nearly crying, high-pitched) "YEAH? WELL, F*** YOU ALL!

I stood there, panting, trying not to cry. I looked at the five assassins who surrounded me. Rick Jones reached out slowly . . . and lightly touched me on the arm with the ball he was holding.

RICK: (kindly) You're out, Feig.

FEIG: (gulping, chest heaving) . . . really? . . .

RICK: Uh-huh.

FEIG: (to audience) B-B-BLAM!!! The five surrounding balls exploded into my body. . . Everything went black. When I came to, Mr. Wendell told me I'd be in detention for a week. For swearing.
```

---

## IC-1371: Hidden in This Picture

- Title: Hidden in This Picture
- Author (byline): Aaron Sorkin
- Work: Best American Short Plays 1990 (Pg 141-168)
- Publisher: Applause Theatre Books
- Publication date as stated: Feb 2000
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: REUBEN, ROBERT, JEFF, CRAIG
- Teaser before the introduction: Yes
- Spoken words (computed): 1792
- Already set (do not supply): none

### Source block (context only)

```text
Author: Aaron Sorkin
Book: Best American Short Plays 1990 (Pg 141-168)
ISBN: 978-1557830852
Publisher: Applause Theatre Books
Date (Month/Year): Feb 2000
```

### Introduction (context only: never use it for content warnings)

```text
Do you know what makes a movie a movie? Think about it. A movie is pictures stitched together to make up 24 frames per second that give the illusion of motion. Photography brought to life to tell the story the artist (the director) wants to tell. It’s beautiful, messy, and beyond fascinating. But today, the director has more to worry about that creating art. Production is 3 weeks behind and 6 million over budget. The sun is setting faster than it's ever set before, and the final long-angle sequence has to be filmed NOW, before the light fades.

Hidden in This Picture by Aaron Sorkin
```

### Performance text (classify this)

```text
A small, grassy hill overlooking a massive expanse of land. ROBERT (the director) is surveying the scene before him. After a moment, REUBEN (the producer) enters. He's out of breath.

REUBEN: (Pg 141-168) The final shot, Robert, one shot, and then the crew, the cast, the six-hundred and ninety-four extras, the cameras, the lights, they all go home. There's no re-take. We can't ask the sun to come back and set again because we *messed* it up the first time. (no response) Three and a half minutes, Robert! Don't you think you should be down with the crew?

ROBERT: The crew knows what to do. (He stops gazing out in the distance. He speaks directly to REUBEN) We've been rehearsing for the past six hours. Despite the fact that this is my first film, a fact that you remind me of four times a day, I'm not an idiot. This is the most important shot in the movie, and I have no intention of *messing* it up. I have left absolutely no room for human error, Reuben. Six-hundred and ninety-four extras, already costumed and approved in their uniforms, will, in a slow, trickling theatrical stream, trot from the ridge of those trees, down past the blue flag and out of camera range. Roll credits. Together we're going to watch art being made. Jeff worked very hard on this screenplay.

REUBEN: Yeah? Well, it's lousy. I got news for you, if the audience doesn't understand what is going on, they leave. And they tell their friends. There's no sequel. And if you think I'm some kind of studio-puppet who only sees dollars and cents, you're right. That's my job.

ROBERT: (JEFF – the screenwriter enters) Reuben's in a bad mood, Jeff. He thinks I've spent too much time and money making a movie about disillusioned Marines in Guam and he thinks your screenplay is full of Yale Drama crap.

JEFF: I'm not sure I'd say the Marines are disillusioned.

ROBERT: Jeff, I've created a picture here, I've communicated with an image -- an idea, an emotion, my idea, and I've done it as succinctly as a well written sentence and as powerfully as a symphony. The rest of this film may end up looking like Beaver Goes to War, but this shot is gonna work.

JEFF: Good luck.

ROBERT: Ssh! (Pause, whispering) Action. (Pause) Oh yeah. Oh. Oh my. This is for my children, Jeff. This is for my daughter, Jennifer, who'll watch it with her friends and say "My Daddy did that." This is for my unborn son who'll look at this and say, "I want to be just like my Dad." This isn't for the actors, Jeff; this one's for me. Look at it, Jeff, look at it.

JEFF: I'm looking . . . Bobby? (Pause) Three cows have walked into the shot.

ROBERT: (Long pause. He must have heard wrong) I'm sorry, what did you say?

JEFF: Three cows have walked into the shot.

ROBERT: (ROBERT turns and looks out) There are cows in the shot. Jesus Christ Almighty. (He runs off yelling) YOU'RE IN THE SHOT! GET OUT OF THE SHOT! COWS! GET THE HELL OUT OF THE SHOT! (Long pause. ROBERT returns) Before I even begin to try and solve this problem, I want you to tell me, Jeff, you wrote the screenplay, you did months of research, you read books, tell me, are there cows on Guam?

JEFF: Not on Marine bases.

ROBERT: Never?

JEFF: No, never. There are no cows on Marine bases. Anywhere. Guam, Nicaragua, Berlin, there are no cows.

ROBERT: Don't tell me there are no cows, there are three cows standing in the middle of the shot!

JEFF: That's because we're ten miles outside of Schenectady on a farm. We're only pretending we're on a Marine base. Bobby, it's okay. Just have some guys run out there and kinda shoo away the cows -- sorta herd 'em off to the left.

ROBERT: Jeff, an entire Marine infantry unit is running toward them with machine guns. They're not moving anywhere.

JEFF: It's 'cause they're all running past them. The cows probably can't even see them. Send some people out to run right towards them and herd 'em off. You can edit this stuff out and the scene'll be nine minutes instead of eleven minutes. (Pause) Bobby, it's the only thing to do.

ROBERT: Those cows have gotta be three-quarters of a mile away. We've got eight minutes left. Do you know how long it's gonna take to get a film crew to run three-quarters of a mile, clear the cows from the shot and then clear themselves from the shot? What are they doing there?

(CRAIG – Production assistant enters)

CRAIG: Bobby, three cows have walked into the shot. I think it's pretty noticeable.

ROBERT: Oh? What makes you say that, Craig, what makes you say it's noticeable?

CRAIG: Well . . . everybody noticed.

JEFF: You might be able to salvage enough ending footage and then fudge around with the continuity on the sunset.

ROBERT: What's goin' on? God, why are you doing this to me? Please move the cows, God. Move 'em seventy-five yards to the left, God, what's the big deal? I'm not kidding, I'm really at a complete - I don't know what I'm supposed to do. Are you - Wait, wait, wait, what are they doing? They're bobbing their heads or something. What does that mean? Do you think that means they're ready to leave? Does it seem to you that they're about ready to leave?

CRAIG: I think they're about ready to leave.

JEFF: I don't - I'm not a livestock psychologist, Rob, I don't know if the cows seem ready to leave. Craig, on the other hand, has a very strong sense that the cows will be leaving soon.

ROBERT: Would you look at those guys? Just trotting by these cows like they weren't there. Doing it exactly the way we did it in rehearsal. You'd sorta think that one of 'em would say to himself "Hm, I'm an actor and I'm supposed to be imitating life. Right now I'm playing a Marine on my way back to the barracks. There's a cow. If I were a Marine, I'd probably think it was somewhat out of the ordinary to see a cow on my way back to my barracks." You'd think one of those guys would acknowledge the fact that they're running past three cows. . . (Pause as Roberts surveys the scene)(Relieved) The extras have discovered the cows. They're acting with the cows -- doing bits of business with the cows. I hate those cows! (Beat) You know what I think? It's not nearly as big a problem as we think it is.

JEFF: Truly, Robert, that's the attitude you gotta have.

ROBERT: I don't think anyone in the audience is gonna notice. I mean, sure, they're gonna notice, they're gonna see these three cows in silhouette against a sunset while 694 Marines file back to their barracks after having spent the most difficult day of their lives engaged in a war game, sure the audience is gonna see these cows, but I don't think they're gonna find that strange. Why should they? They're just cows. Everybody's seen cows.

JEFF: On a Marine compound? In Guam?

ROBERT: You think people are gonna pick that out? (Makes up his mind) Craig, call down to the deck. Get one of the policemen to shoot the cows.

JEFF: Craig, stop. Bobby, you can't tell the police to shoot the cows. You can't kill cows to make a movie.

ROBERT: We kill cows to make hamburgers, why can't I kill cows to make a movie, what's the difference?

JEFF: What's the difference between food and a movie? Are you serious?

ROBERT: They don't have to kill the cows, they don't have to shoot to kill, just drop 'em. Wound 'em for crying out loud, I'm running out of time.

JEFF: Bobby, allow me a very quick hypothetical. Let's assume for a moment that Schenectady police officers carry pistols that can fire three-quarters of a mile and that the officers are accurate at that range to be able to wound and not kill a cow. Fast forward a year. Don't you think that even the people who don't find it a little strange that three cows have wandered into Guam are gonna be a little perplexed when the cows, for no apparent reason, fall down to the ground?

ROBERT: You're right. I've been looking at this all wrong. Look at the cows. What do they look like to you?

JEFF: The cows? They look like cows.

ROBERT: Don't you think they look a little like tanks? Sherman tanks. Don't you think they look a little, off in the distance there in silhouette, like tanks? We have footage of tanks. I just keep jump cutting for half a second at a time to these shots of tanks. All the way through, just keep jump cutting to tanks, three, four frames a shot, they will be subliminally convinced that they're looking at tanks. They will be subliminally convinced!

JEFF: Because you showed them tanks every once in a while, they're gonna think those cows are tanks? Who do you think your audience is?

ROBERT: Idiots, Jeff. I think the vast majority are lazy, stupid idiots who, I believe, can be convinced by a clever director with enough footage at his disposal that three cows are in fact Sherman tanks.

JEFF: Well, you're wrong. The only person who thinks those cows are anything but cows is you.

ROBERT: We are film makers and we don't lock ourselves into conventional notions and labels. We give ourselves the freedom to explore and communicate our own surroundings and we don't file the world around us into little shoe-boxes and label them black and white.

JEFF: Those are cows, Bobby. THEY LOOK LIKE COWS! They walk like cows! They eat like cows! They're cows! Accept that fact. I wouldn't lie to you about something like this. And I think they're the best thing in the movie.

ROBERT: (Pause. quietly) You're right. You're right. They're cows. There's really no way of getting around that. They're cows. They'll have to stay cows. So fine. Okay. There are three cows standing in the last shot of the picture. (Pause) What did I mean by that? What was I trying to say? I need to examine this. What are cows? What are cows? What do cows do? Cows give milk. Milk is life. Is milk life? No, not really. Milk is milk. But it's also life in a way. Sure. Milk. Mother's milk. The milk of life. (Pause) Young, disillusioned Marines ... Young disillusioned Ma-rines . . . what? . . . Sucking the milk of life. . . the last drops of the milk of life, right? . . . Sunset? Endings? The Last Drops? (He's got it) Young disillusioned Marines sucking the last drops of life from cows . . . Because their mother's aren't there with them in Guam! (Beat)

(REUBEN enters)

REUBEN: Those cows were a pain in the a**, huh? What the hell, we'll just matte 'em out when we cut it. Hell of a sight though. I swear, I almost *peed* my pants.

ROBERT: Matte' em out? . . . . (With bravado) Why would I want to matte out the cows? I rehearsed those cows, I auditioned over four-hundred cows. Those were my first choice. You gotta admit, the camera loves 'em. It's the whole statement of the picture . . . The cows.
```

---

## IC-1372: The Hoboken Chicken Emergency

- Title: The Hoboken Chicken Emergency
- Author (byline): D. Manus Pinkwater
- Work: Not specified
- Publisher: Aladdin
- Publication date as stated: Sept 2007
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MOM, FISH GROCER, INDIAN SPICE GROCER, PROF MAZZOCCHI, ARTHUR, CHICKEN, RADIO NEWSCASTER, DR. HSU, MAYOR, TOWNSPERSON 1, TOWNSPERSON 2, TOWNSPERSON 3, HENRIETTA
- Teaser before the introduction: Yes
- Spoken words (computed): 1605
- Already set (do not supply): none

### Source block (context only)

```text
Author: D. Manus Pinkwater
ISBN: 978-1416928102
Publisher: Aladdin
Date (Month/Year): Sept 2007
```

### Introduction (context only: never use it for content warnings)

```text
The Hoboken Chicken Emergency by D. Manus Pinkwater
```

### Performance text (classify this)

```text
NARRATOR: (Pg 5) This was the first time [Arthur] had the job of getting the Thanksgiving bird, and he had messed it up. (Pg 2) Something had gone wrong at Murphy’s Meat Market. Somehow Poppa’s turkey reservation had gotten lost. Every turkey had some family’s name on it – none of them had the name Bobowicz.

MOM: (Ph4) Maybe you’d better go back and get two chickens and a duck. (smiling) I’ll explain it to your father.

NARRATOR: Things had gone even more wrong than Arthur thought. When he got back to Murphy’s Meat Market, there wasn’t a single chicken in the place – no ducks either. He went to every store in town that might possibly have a bird. He went to a few stores that probably did not have birds – just in case.

FISH GROCER: This is a fish market! What makes you think we’d have turkeys or chickens, you silly kid!

INDIAN SPICE GROCER: This is an Indian spice store. Curry powder, we’ve got; mango chutney, we’ve got – birds we do not have.

NARRATOR: Arthur was getting depressed. He didn’t want to go home and tell his mother the bad news, [when] he noticed a card stuck in the window of an apartment house door: (in amazement and awe) PROFESSOR MAZZOCCHI / INVENTOR OF THE CHICKEN SYSTEM / BY APPOINTMENT. Arthur rang the bell. What did he have to lose?

PROF MAZZOCCHI: (from off stage - upstairs) You will not get me evicted! My brother owns this building! I am a scientist! If you people don't stop bothering me, I'll let the rooster loose again.

ARTHUR: (shouting) Do you have a chicken for sale? We need one to cook for Thanksgiving.

PROF MAZZOCCHI: What? You want to buy a chicken? Come right up! I have been waiting for years for someone to come to buy a superchicken. The only people who ever come here are neighbors to complain about my chickens. They don't want me to keep them. How much money did you bring?

NARRATOR: The old man went inside the apartment with Arthur's sixteen dollars. When he opened the door, Arthur heard a clucking sound, (Clucking sound) but not like any clucking he had ever heard -it was deeper, louder. (Clucking sound again, but deeper and louder)

PROF MAZZOCCHI: (returning with a superchicken on a leash) This is the best poultry bargain on earth - a medium sized superchicken - six cents a pound - here's your two hundred and sixty-six pound chicken, on the hoof. She'll be mighty good eating. Please don't forget to return the leash and collar. (ushering Arthur out the door and closing it behind him before Arthur can change his mind)

ARTHUR: (perplexed and looking from the chicken to the door to the leash and back again – then pounds on the door)

PROF MAZZOCCHI: (shouting through the door) No refunds!

ARTHUR: Don't you have anything smaller?"

PROF MAZZOCCHI: (shouting through the door) No refunds!

NARRATOR: The chicken tamely followed Arthur down the stairs as Arthur led it home and tied the leash to the bannister. Then he went in to prepare his mother.

MOM: That took a long time. Did you get a bird?

ARTHUR: I got a chicken. It only cost six cents a pound.

MOM: That’s very cheap. Are you sure there’s nothing wrong with it. Maybe it isn’t fresh.

ARTHUR: It’s fresh. It’s alive.

MOM: You brought home a live chicken?

ARTHUR: (starting to cry) It was the only one I could find. I went to all the stores and nobody had turkeys or chicken or ducks, and finally I bought this chicken from an old man who raises them in his apartment. (Mom heads for the door) Momma, it’s a very big chicken! (She opens the door)

CHICKEN: (Shifting from foot to foot, blinking) CLUCK! (mom closes the door and stands staring at it – long pause)

MOM: (in shock) There’s a two-hundred pound chicken in the hall. It’s wearing a dog collar.

ARTHUR: I’m supposed to return that. (Mom opens the door a crack and peeks out, closed the door, looks at Arthur, opens the door all the way and looks out at the chicken.) I thought we could call her Henrietta.

MOM: Put her in the kitchen and we’ll discuss it when you father comes home.

NARRATOR: That night the family had meatloaf for Thanksgiving dinner [and even better] Poppa decided to let Arthur keep Henrietta. *****SCENE *******

NARRATOR: (Pg 11) Arthur got up early the day after Thanksgiving. The night before, while Henrietta was sleeping next to his bed, Arthur had made plans to teach her a lot of tricks.

ARTHUR: Henrietta! (no response – Arthur claps his hands) – Henrietta! Come here! (Henrietta looks at him and blinks) OK, just stay here by yourself (begins to walk away – Henrietta gallops after him, crashes into him and begins following Arthur around clucking) Heel, Henrietta, heel, girl.

NARRATOR: She was doing pretty well for a chicken who had never been trained before. Every now and then he would pat Henrietta on the back, and scratch her neck feathers. (Arthur pantomimes these actions) She liked that. [But just then] a door opened to a house across the street and Bozo bounded across the street. Bozo was a big German Shepherd and he ran straight at Arthur and Henrietta! TRANSITION To make a long story short . . . Henrietta runs away in a panic and ultimately has to be rescued from a tree by the fire department. Unwilling to deal with a giant chicken running wild through the streets, Father makes Arthur return the bird to Professor Mazzocchi. Henrietta, feeling unloved and unwanted by anyone, escapes and begins to terrorize the town. Arthur knows it is up to him to do something – after all Henrietta was his chicken even if his dad made him give her back.

NARRATOR: (Pg 34) Arthur arrived outside Professor Mazzocchi’s apartment house just in time to see the professor locking the doors of a big green truck. AUGIE'S TRUCK RENTAL, it said on the side. From the muffled clucking and screeching, Arthur could tell that all the professor's experiments were inside.

ARTHUR: Professor Mazzocchi! Are you going away?

PROF MAZZOCCHI: Do you know what happens to people when one of my experiments gets loose? They go crazy! One time they burned down my house! Burned it right to the ground!

ARTHUR: Henrietta is wandering around the streets of Hoboken, all alone. She must be frightened, and cold, and hungry. Don't you care what happens to her?

PROF MAZZOCCHI: Of course I care, but when you've been a mad scientist as long as I have, you learn that some things are more important than others. Most important, right now, is for me to get out of town with all my experiments. If the news gets around that I am responsible for a very large chicken loose in the streets, people will start acting crazy.

NARRATOR: Professor Mazzocchi started the engine, and the big green truck rumbled away. ******* SCENE *******

RADIO NEWSCASTER: (Pg 46) AND NOW, A BIZARRE NEWS STORY FROM HOBOKEN, NEW JERSEY . . . LAST NIGHT, MORE THAN FIFTY PEOPLE REPORTED GIANT CHICKEN SIGHTINGS TO THE POLICE, THE F.B.I., AND THE WHITE HOUSE . . . THE CHICKENS, WHICH STAND ABOUT FIFTEEN FEET HIGH, ARE ESTIMATED TO WEIGH ABOUT ONE THOUSAND POUNDS . . . THERE HAVE BEEN NO REPORTS OF INJURIES, OR ATTACKS ON PERSONS . . . THIS RADIO STATION WILL KEEP YOU POSTED ON THE CHICKEN CRISIS IN HOBOKEN.

NARRATOR: (Pg 51) The whole town was chicken-panicky. The police department's switchboard received thousands of calls from frightened people. The mayor's office was full of citizens demanding protection from the giant chickens. Schools were closed. People were afraid to go shopping, to go to work, to step outside their doors. Special police chicken squads were sent to cruise the streets in cars. Helicopters buzzed over the rooftops, looking for chickens. Men stayed home from work to protect their families. Neighboring towns sent fire trucks, and teams of veterinarians to help in the chicken emergency.

RADIO NEWSCASTER: THE GIANT CHICKEN WAS SEEN EMERGING FROM THE CLAM BROTHERS SEAFOOD RESTAURANT AT FOUR-FIFTY-SEVEN THIS MORNING. HOBOKEN POLICE OFFICERS SMITH AND MOONEY GAVE CHASE IN THEIR SQUAD CAR, AND CORNERED THE CHICKEN ON COURT STREET, NEAR THIRD. THE CHICKEN THEN KICKED A HUGE DENT IN THE LEFT FRONT FENDER OF THE SQUAD CAR AND RAN OFF. TRANSITION For 5 days, Henrietta terrorizes the town: She hijacks a potato chip truck, kicks over a fire-hydrant, and bends the flagpole outside the senior high school. Chicken traps are set, but there is no relief from the chicken situation. The mayor spent sixty-thousand dollars of the town's money trying to resolve the Hoboken Chicken Emergency and nothing worked. Finally, Professor Mazzocchi, feeling guilty, sends a specialist to help Hoboken: Dr. Hsu, poultry locator, arrives to meet with the Mayor.

DR. HSU: (Pg 72) Chickens are very sensitive birds. It is very easy to hurt their feelings. When their feelings are hurt, they become unpleasant, anti-social. A perfectly sweet chicken can become a bitter destructive bird, if it feels that it is unwanted.

MAYOR: Do you think Henrietta is a chicken like that? Do you think she feels unwanted, and that's why she's kicking over fire hydrants, and frightening the citizens

DR. HSU: I am sure of it. I have found out that Henrietta was, for a short time, the personal pet of a young boy in this town. His name is Arthur Bobowicz. (Arthur smiles at the audience and waves) Young Arthur and Henrietta got to be great friends. Henrietta got into a tiny bit of trouble, and Arthur's parents insisted he take Henrietta back . . . (Arthur is sad, pantomimes putting the collar and leash on Henrietta and walking her back to Prof. Mazz.) Henrietta missed Arthur, and set out to look for him. Every time people saw her, they screamed and ran away. (acts out this out and Dr. HSU responds to the screaming by putting his hands over his ears) They called the police, and the police chased her. She felt unloved. Think if it happened to you. You'd be angry too. We [have to] encourage the citizens of Hoboken to have a friendly attitude toward chickens. We will ask them to wave and smile when they see Henrietta, instead of screaming, or calling the police, or throwing things at her.

NARRATOR: The following day posters were printed. They showed a boy, looking very much like Arthur Bobowicz, with his arm around a big chicken. The Goodyear blimp was sent for, and it cruised back and forth over Hoboken, towing a large banner which read CHICKENS NEED YOUR LOVE. At night, the message was flashed in electric lights. The television stations cooperated. There were special panel discussions on the late night talk-shows, in which psychologists and guidance experts told about chickens' need for love and approval. So that they wouldn't upset Henrietta, big white chickens were painted on all the police cars.

(assumes the persona of Henrietta and responds to these townspeople with apprehension that slowly changes to a relaxed co-existence)

TOWNSPERSON 1: Nice chicken. Nice chicken. (Henrietta starts to come closer – then runs)

TOWNSPERSON 2: ice Henrietta. Nice chicken. Nobody’s going to hurt you. (Henrietta allows the townsperson to pet her beak)

TOWNSPERSON 3: Good morning, Henrietta How ya’ going? (Henrietta clucks contentedly and nuzzles the townsperson affectionately)

NARRATOR: [Soon] people couldn't remember why they had been afraid of Henrietta. She seemed to be a very pleasant, well-behaved chicken. They liked her. [The Hoboken Chicken Emergency was over]

HENRIETTA: (Pg 8) (Shifting from foot to foot, blinking) CLUCK!
```

---

## IC-1373: How to be a Supervillain

- Title: How to be a Supervillain
- Author (byline): Michael Fry
- Work: Not specified
- Publisher: Jimmy Patterson
- Publication date as stated: May 2017
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: VICTOR, DAD, MOM, THE SMEAR, DSV WORKER, DR. DEPLORABLE, NAP BOY, THE WHINER, SMELLY FEET
- Teaser before the introduction: Yes
- Spoken words (computed): 1251
- Already set (do not supply): none

### Source block (context only)

```text
Author: Michael Fry
ISBN: 978-0316318693
Publisher: Jimmy Patterson
Date (Month/Year): May 2017
```

### Introduction (context only: never use it for content warnings)

```text
How to be a Supervillain by Michael Fry
```

### Performance text (classify this)

```text
VICTOR: (Prologue) My parents fight, A LOT. (reacts to audience) Wait. No. Not each other. They fight other people . . . for a living. My parents are supers. Supervillains, to be exact. Meet Rupert . . .

DAD: (poses menacingly; squints as if shooting laser from his eyes) The Red Death Ray!

VICTOR: And Olivia Spoil

MOM: (intense karate moves)

VICTOR: Otherwise known as . . . The Spoil Sports. I know. Pretty lame. But it works for them. Not so much for me. My name is Victor Spoil. I am 12-years-old and I was raised to be bad. (hangs his head) Which is a problem... (looks up and smiles sheepishly) when you’re actually good.

VICTOR: (Chpt 2) I feel bad for Mom and Dad. They want what all supervillain parents want, (sincerely) They want me to grow up evil, with a burning desire to spread chaos and mayhem across the universe. But, instead, they got me – Tidy Boy. (Chpt 4) My parents were seriously disappointed.

MOM: (both are working on gadgets and/or firing ray guns) What are we going to do with him?

DAD: I have a plan!

MOM: Wait. You don’t mean . . .

DAD: Now that Victor’s out of school for the summer, he can take him on as an apprentice.

MOM: Seriously? He’s the only option?

DAD: The Walrus turned us down. Mr. Sour Cheeks said no. Even Infectious said “Are you kidding?” (pause) He’s our last hope. . . and he should be here any second. *Ding Dong* (door opens)

THE SMEAR: (elderly man, cubby and balding) The Smear is here!

VICTOR: (Chpt 5) (to audience) Not the Smear! Anyone but the Smear. There are hundreds of supervillains. Some are cool; some are okay; a few are seriously lame . . . but the Smear is just pathetic. He once brought a jar of grape jelly to a photon saber fight!

THE SMEAR: (uses fingers as photon sabers, the licks the jelly from them)

DAD: (Chpt 6) This is our son, Victor Spoil.

VICTOR: Seriously?! There’s no way I’m going to apprentice for you!

DAD: You want to be a civilian? Like Uncle Benny? He makes socks. For a living. Socks. All day. Every day. Socks.

THE SMEAR: (Chpt 7) Kid, you ever wonder why I am the lamest supervillain? (intensely) I stained Dr. Deplorable the most evil supervillain on the planet. We used to be partners. Until . . . the incident.

MOM: It was YOU?!

THE SMEAR: (Chpt 8) Dr. Deplorable and I worked together on a few battles against Mr. Awesome.

VICTOR: (impressed) The greatest hero on the planet!

MOM: (haughtily) I heard he has calf implants.

THE SMEAR: Dr. Deplorable had him cornered. I went in to blind him with a stain grenade... but it blew up in my hand . . .and on Dr. Deplorable’s face.

THE SMEAR: The DSV (Department of Supervillains) . . .

DSV WORKER: Number 4? Number 4!

THE SMEAR: . . . banished me for twenty years, but now I can make a comeback. I’m set to battle MegaMole in Des Moines in three days.

VICTOR: The Smear laid his hand on my shoulder. Not around my shoulder. Actually on my shoulder. It felt weird. (attitude shift) But warm.

THE SMEAR: (crouches to Victor’s eye level) It won’t be easy, kid. It won’t be glamorous and it will get messy. I can’t guarantee fame and fortune. But I can guarantee adventure. And pie.

VICTOR: Pie? I like pie. . .

THE SMEAR: Where do you think I get the base for all my smear stains?

VICTOR: (looks at shoulder, to audience) The Smear lifted his hand off my shoulder, leaving a hand-print stain. Normally, I’d freak out at something like that, but this time was different. This wasn’t a stain. This was a mark of distinction. The mark of a supervillain’s apprentice. ***** In Smear’s apartment*****

THE SMEAR: (Chpt 10) Pay attention, kid. There’s a lot to learn. (Victor takes out a notebook and pen) What are you doing?

VICTOR: Taking notes.

THE SMEAR: (grabs notebook and throws it away) First lesson: Supervillains NEVER take notes! (looking at a row of jars) First, let’s talk stains. rotten mango and tartar sauce chutney (hands jar to Victor, who is grossed out) Fizzy clamato, yak milk and Walrus Wart Frappuccino.

VICTOR: Can you pick up walrus warts at Costco? (scene shift to the garage)

THE SMEAR: Less talking, more [evil]! (opens garage door and proudly points out his equipment) Stain soakers *Splat! Splat!*

VICTOR: What about your eyes? Can you spray stains with your eyes?

THE SMEAR: (scoffing) No. That would be weird and really unsanitary. (he goes on with his list) . . . The Stain Mixer, The Flying Stain Bomber. (they get into the car)

VICTOR: (Chpt 11) Um, Mr. Smear? I was wondering about the stains. I mean, it’s just a stain. How is it going to stop a superhero?

THE SMEAR: (intense pause, then he shouts) THEY NEVER WASH OUT! My stains . . . are feared . . . across seven continents...

VICTOR: You’ve fought in Antarctica?

THE SMEAR: Don’t interrupt! My stains don’t just stain... they stick... they goo... they get in your ears, your eyes ... THEY GET IN EVERYWHERE!!!

VICTOR: Everywhere?

THE SMEAR: Everywhere! And the worst is yet to come. Batch 487B. A superstain. . .(ominously) that can stain a man’s soul. *Ker-pow!*

VICTOR: (Chpt 13) (to audience) An explosion rocked the Smearmobile like a toy! We were under attack! (to Smear) What was THAT!

THE SMEAR: GET DOWN! (smiling) Someone doesn’t want us in Des Moines.

VICTOR: Then the strangest thing happened. That dumpy, grumpy, middle-aged fake supervillain had suddenly transformed into . . . The Smear . . . (Chpt 14) pretty darn awesome!

THE SMEAR: Victor, stay down. Stain Soaker set to 11. Let’s roll! (action sequence) *BLAM! LEAP! POW!*

VICTOR: (dodging and ducking) I’d seen a lot, but I’d never seen this. . . The Smear didn’t hesitate. He took action. He was surprisingly limber for a large man.

THE SMEAR: (battle rages on) *BLAM-BLAM!* You’ll never take me alive or dead (launches rocket) Eat stain, you miserable bag of endoskeletal goo! (throws grenade)

VICTOR: (Chpt 15) It was touch and go, back and forth, until finally the smear got the upper hand...

THE SMEAR: (turns away from audience) Stain in the hole! *BOOM!* (Slow motion throws stain grenade at audience and turns to run)

DR. DEPLORABLE: (Chpt 29) (on loudspeaker) You’re done Smear! Say goodbye to this earthly coil and prepare to die (coughing and hacking)

THE SMEAR: I know that phlegm-clotted cough anywhere. That’s Dr. Deplorable! (Chpt 30) *Phew! Phew! Phew!* (bullets fly at Victor, who dodges and zigzags; the pair take cover behind a large boulder)

VICTOR: (terrified) Why is he shooting at us?!

THE SMEAR: (scared, but still The Smear) He’s mostly shooting at me! (pause) I’m the only one who knows his secret weakness. (they run to the Smear Mobile) With me out of the way, (Chpt 36) there’ll be nothing to stop [him] from TAKING OVER THE WORLD!

DR. DEPLORABLE: (Chpt 30) This isn’t over, Smear! I’ll be back! (coughing and hacking)

VICTOR: He should really have that cough checked out.

THE SMEAR: (Chpt 31) (as they drive away, he motions to audience) You see those fans over there? Their lives are predictable. No winners. No losers. Just socks. Lots and lots of socks. They need us. They need good and evil. Light and dark. Real winners and real losers. *******Transition – back in the garage preparing stain weapons*******

VICTOR: [So what’s Dr. D’s secret weakness?]

THE SMEAR: (long pause, not sure if he should share) Tickling.

VICTOR: (in disbelief) Dr. Deplorable’s secret weakness is that he’s afraid of being tickled?

THE SMEAR: It incapacitates him. And makes him laugh. He really hates to laugh.

VICTOR: I tried to keep a straight face. I failed. We both laughed. Hard. (Chpt 32) With each passing day, I felt more and more comfortable around the Smear. More comfortable than I ever felt back home.

THE SMEAR: (Chpt 35) Go get your costume on. It’s almost show time.

VICTOR: Tonight was a big night. I was excited. And nervous. Everything was going according to plan as I opened the door and discovered...

DR. DEPLORABLE: (Chpt 36) That’s it, Smear! You’re finished!

VICTOR: Dr. Deplorable was back! (races to hide behind Smear)

THE SMEAR: (circling each other) Finished?

DR. DEPLORABLE: Eliminated, erased, excised, whichever you prefer (ridiculous moves to ramp up his elbow lasers)

VICTOR: Why is he pointing his elbows at us?

THE SMEAR: (cocks gun) ELBOW LASER CATAPULTS!! Very nasty . . . (fires)

VICTOR: (Chpt 45) The battle had begun.

DR. DEPLORABLE: (Chpt 36) (Dr. D dodges then fires elbow laser, which suspends Smear in midair) *ZAP! WOOSH!*

THE SMEAR: (floating in mid-air, slow motion) WHOA!!!!

VICTOR: (to audience) This was a moment. A moment where you just had to go for it. No matter how silly, no matter how dangerous. NOW! (dives at Dr. D. and begins tickling him)

DR. DEPLORABLE: (laughing hysterically)

VICTOR: Gotcha! (more tickling)

DR. DEPLORABLE: (more laughing)

VICTOR: (rips off Dr. D’s book and tickles his foot)

DR. DEPLORABLE: (Chpt 48) (gasping dramatically) No!, Stop! This isn’t the way (breath) it’s supposed to end! (gives up in defeat)

VICTOR: (Chpt 36) Woah! It worked! (Chpt 47) SUPER TICKLING!

THE SMEAR: Who’s awesome now?!

VICTOR: (Chpt 49) His weakness turned out to be my superpower?

THE SMEAR: (sarcastically) Super-tickling! Who knew!

VICTOR: So, I’m THE TICKLER! (strikes a pose with an evil laugh)

THE SMEAR: (shrugs) You can pick your nose, but you can’t pick your superpower.

VICTOR: I still have one question. You’re a supervillain. You could have gone along with Dr. D. and taken over the world. That would have been the ultimate comeback! What stopped you?

THE SMEAR: It was you

VICTOR: Me?

THE SMEAR: You said I was awesome. Awesome people don’t take over the world. Because, they don’t need to. Because, you know, they’re awesome. I’m a supervillain. [You] helped me see it takes a hero to make a villain. (puts his hand over his mouth) Did I say that out loud?

VICTOR: You are a hero!

THE SMEAR: Language! You kiss your mom with that mouth?

VICTOR: (scene shifts alone on stage, he speaks to the audience) (Epilogue) I now battle on the Junior Super Circuit against other beginner supervillains and superheroes like Nap Boy…

NAP BOY: Is it snack time yet?

VICTOR: . . . and The Whiner

THE WHINER: Wah! I broke a nail!

VICTOR: (Chpt 34) . . . Worm Boy and Smelly Feet

SMELLY FEET: (puts his foot out to Victor’s nose and he reacts)

VICTOR: (Epilogue) But with Dr. Deplorable out of the way, the super battles are no longer winner takes all, but winner picks up the root beer!
```

---

## IC-1374: I, Freddy

- Title: I, Freddy
- Author (byline): Dietlof Reiche
- Work: Not specified
- Publisher: Scholastic Press
- Publication date as stated: May 2003
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: FREDDY, MR. JOHN, G-GRANDMOTHER, G-GRANDMOTER, SALESCLERK, MAN WITH MUSTACHE, SOPHIE, MOM, WILLIAM
- Teaser before the introduction: Yes
- Spoken words (computed): 1270
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dietlof Reiche
ISBN: 978-0439283564
Publisher: Scholastic Press
Date (Month/Year): May 2003
```

### Introduction (context only: never use it for content warnings)

```text
(As Freddy) Well, I certainly don’t want to be dissected for research purposes. . . But you all don’t look like showmen or scientists, so I guess it’s safe to tell you my story. Hi, my name is Freddy (waves) . . .

I, Freddy by Dietlof Reiche
```

### Performance text (classify this)

```text
FREDDY: (Pg 202) (Freddy – a hamster - uses his paws to type out a message on a keyboard, he voices the words as he types) My life story . . . (Freddy notices he has an audience and tries to hide or delete his message)

MR. JOHN: (Pg 198-199) (Freddy remembers Mr. John’s words) The fact that you can read and write must remain a secret between us. It wouldn’t be long before some smart showman came along, eager to make a fortune out of Fantastic Freddy, the hamster that can read and write. Either that, or you’d wind up in the hands of scientists itching to dissect your brain for research purposes.

FREDDY: (Pg 3) I was born the sixth of ten . . . (Pg 2) My birthplace was a cage . . . (Pg 129) and I can [read] and write! . . . (Pg 2) Maybe I should also mention I’m a hamster. (Cleans his hamster face and scratches behind his ears) (Pg 1) The time has come to make a start on my life story . . . A pretty bright youngster grows up in a kind of prison, is sold, eventually manages to escape, and is smart enough to gain his freedom. If that isn’t a story, what is? (Pg 3) I was born blind and naked . . . I didn’t become a genuine hamster until my eyes opened . . . (Reacts violently to the vision of Great-Grandmother in his face) (Pg 17) (then, in awe) Great-Grandmother!

G-GRANDMOTHER: (Pg 21) Now, youngsters, pay attention. [It’s time for] (Pg 17) Saga Hour! (Pg 21) Rejoice! (Freddy cheers) (Pg 18) In the beginning was the Golden Trinity: three golden hamsters . . .

FREDDY: But, Great-Grandmother, what about the . . . .

G-GRANDMOTER: (Pg 19-20) Stop your nonsense! The saga is unalterable. You don’t question it, you simply listen to it. Understand?

FREDDY: Yes, but . . .

G-GRANDMOTER: (Harsher) Hold your tongue! . . . (Pg 18) [These] three golden hamsters were abducted from the Promised Land of Assyria and carried off into captivity.

FREDDY: (Freddy raises his paw with another question)

G-GRANDMOTHER: (Pg 20) (bares her teeth and flattens her ears; she hisses at Freddy and gives him the evil eye, Freddy slowly lowers his paw) And now, I’ll tell you [about] the Promised Land . . . Assyria! (Pg 21) One wonderful day, all the golden hamsters in the world [will] be released from captivity and led back to the Promised Land.

FREDDY: (Pg 18) But, Great Grandmother . . . (Pg 21) why?

G-GRANDMOTHER: (So upset by the interruption, she can’t even speak, she hisses, spits, has a fit and dies)

FREDDY: (Pg 3) [Then] Great-Grandmother went into Eternal Hibernation. . . . (Pg 7) My thoughts went around and around in circles. I must get out of [this] cage . . . I must find (Pg 24) the Promised Land of Assyria. (Pg 7) The next golden hamster in our cage to be sold must be me! (notices that people are peering into the cage) (Pg 10-13) The fat salesclerk . . . and a man with a mustache!

SALESCLERK: How old is your little girl?

MAN WITH MUSTACHE: She’s nearly six . . . Her name’s Sophie.

FREDDY: Too young! Far too young!

MAN WITH MUSTACHE: She spends a lot of time on her own, you see.

SALESCLERK: Great, so now she’ll have a playmate.

MAN WITH MUSTACHE: She’s only just learning to read. She’s asked me to get a book about caring for golden hamsters.

FREDDY: That settled it! I launched into my routine. (rushes to the middle of the cage, stands up on his hind legs, opens eyes wide . . . cleans face with paws and then raises right paw high and waves)

MAN WITH MUSTACHE: (Looking over all the options in the cage, he notices Freddy waving and waves back) Okay. He’ll do.

FREDDY: What followed was the worst time of my life, yet it began quite pleasantly. I was shut up in a fairly small box – hamsters are fond of confined spaces. But soon the box started to move. (Freddy vibrates with the telling, loses his balance and regains it) I was shaken around until I felt thoroughly nauseous. (Freddy throws up a bit in his mouth) An eternity later, the shaking ceased. (A huge sigh of relief)

MAN WITH MUSTACHE: Sophie! I’ve got something for you!

SOPHIE: What is it, Daddy? (Sophie takes the box and peers inside) (Pg 14) Oh, Daddy! (she takes Freddy out of his box) A golden hamster! Oh, Daddy, he’s so cute. (Turns to her mother) Look, Mom! My hamster.

MOM: (Pg 15) (Recoils in disgust) You both know I wasn’t crazy about this idea. A creature like this could bring diseases into the house. He doesn’t look too chipper . . . more like he’s sick! (Mom coughs violently, blows her nose and coughs again, moaning and groaning) (Pg 29) I’m getting a migraine! I’m going to lie down for a few hours . . . (to Sophie) (Pg 28) Finish your homework before you play with [that] hamster (the last word is said in disgust) !

SOPHIE: (Pg 27) (Sophie heads solemnly off to her room with Freddy in her hands. When her mom is no longer in sight she breaks into a happy skip. She sits Freddy gently on her desk and bends down to talk directly to him) You need a name. I [think I’ll] call you Freddy.

FREDDY: Do I? In that case, why not Freddy? It sounded fresh and frisky, like me!

(Freddy wiggles his body, excited to be out of a cage and curious about his surroundings) (Pg 38-39) So there I [was] on Sophie’s desk, surrounded by pencils and schoolbooks and watched her start on . . . “homework.” She was learning to read and write . . . a few strange marks on paper, and they meant something. Fantastic! T – R – E- E referred to a picture of a tree, so TREE meant tree. Huh! Far from difficult . . . (Pg 42) It occurred to me how useful reading could be to a golden hamster in that far off place . . . (Pg 18) [the Promised Land of Assyria.] (Pg 42) So I decided to learn to read! (Pg 51) The fact was, I learned to read so quickly, much quicker than Sophie. I was astonished! **** scene break ****

FREDDY: (Pg 77-79) Morning came (Freddy yawns, stretches as he awakens, then recoils in disgust as he notices) Mom!! Her face all swollen up and the color of a tomato.

MOM: Sophie, wake up. (Coughing fit, blows nose again, more coughing)

SOPHIE: Mom! What’s the matter with you?

MOM: An allergic reaction (more coughing, sniffling, then insincerely) I’m sorry, but I’m afraid the hairs from his fur are making me ill. (hand to her forehead, dramatically)

SOPHIE: But, but . . . but MOM! No, Mom! Please don’t!

FREDDY: (Sits up on his haunches to watch the show, grooms himself a little)

MOM: Sophie . . You can’t want your mother going around in this condition. And I’m running a fever! (Pg 82) I’m going to call John! (Coughs dramatically and exits)

SOPHIE: (Pg 80) (runs to Freddy’s cage and kneels down crying)

FREDDY: I hadn’t realized she was quite so attached to me. (Pg 89) Sophie was a girl in a million! (Pg 83) (Freddy’s body is swaying during the transport and he speaks sadly) I was transported in my cage, not the box I’d arrived in. (Pg 85-86) I crept deep into my burrow, feeling utterly miserable. So this was the end. Good-bye to reading . . . Good-bye, Sophie! (The transportation movement stops . . . Freddy peeks out of his burrow and is surprised) Hey! What’s going on? Where on earth? I was at Mr. John’s place [not] the pet shop! (Pg 91) (Freddy quickly forgets Sophie and becomes more and more elated as he speaks) Looking around, I saw that my cage was on a shelf . . . to the left and right of it? BOOKS!

(Freddy easily opens the door to his cage and begins to explore) I had wound up in the land of milk and honey! What a stroke of luck! Books (Pg 115) that would take me on a fantastic journey to the Promised Land of Assyria! . . . . (Pg 91) And then I heard it . . . (Pg 90) a purring sound! (Freddy peers over his shoulder and spies a cat on the shelf. He squeaks and hides his face)

WILLIAM: (a large furry house cat who is the size of a house compared to poor Freddy. He sits down, purrs, meows and ultimately speaks) (Pg 99) You’re Freddy, I presume.

(He gestures to himself expansively) [I am] Sir William.

FREDDY: (Pg 97) (finding courage . . . he rises on his hind legs, and puffs out his cheeks in an aggressive fighting stance) Listen to me, tomcat!

WILLIAM: (Pg 99) (unsheathing his claws one by one, but speaking calmly) I find it quite absurd for a five-inch hamster to try to play the lion tamer with a cat of my size. (William chuckles) So kindly drop the act. Then, maybe we can have a civilized conversation.

FREDDY: (Pg 177-178) (Feeling safe in the fact that William was not a threat, Freddy settles down) [So] I recounted the whole story from the very beginning. I told him about Great-Grandmother and the Golden Hamster Saga; about my time with Sophie; about the way I’d learned to read . . . [and] about the far-off Promised Land of Assyria. (reverently) In short . . . A golden hamster in Assyria –

WILLIAM: (breaking in) . . . is a civilized domestic animal free to roam wherever it wants.

FREDDY: (nodding) Anyway, it’s impossible to live like that without human cooperation. (to audience) (Pg 111-112) That’s why I had to get in touch with Mr. John. Except I didn’t have the faintest idea how to do so. ***** scene break *****

FREDDY: (pg 137) I’d been living at Mr. John’s for five days [when] (Pg 112) Mr. John came into the study and sat down at the desk. (Pg 151-153) He pressed a button. A gong sounded, and some mysterious symbols and pictures appears on a screen. Mr. John was using this machine to write with!! Black letters appeared on the screen! As I watched him depressing keys with very little effort, I realized that this was the machine for me. With this machine, I could write!! (Pg 202) I made a start the very next day. To begin with, (Freddy practices pushing down keys as he speaks, it is difficult at first, but gets easier and easier) I limited myself to finger exercises – paw exercises, I mean. Before long, however, I could manipulate the keys so skillfully that I was able to type without difficulty . . . (Pg 200) “Thanks for everything . . . Freddy” (Pg 196) After that, I simply wait[ed], sitting on the desk, for Mr. John to come home. (Pg 197) Mr. John’s response when he found my message on the screen?

MR. JOHN: Humm . . . (Pg 162) That would explain a couple of things . . . like certain changes to my bookshelves. (Mr. John types and speaks aloud) (Pg 193) Hi, There! Welcome Home, Freddy.

FREDDY: (lifts a tiny paw to shake Mr. John’s hand, which Mr. John does)

MR. JOHN: (Pg 199) (speaks to Freddy) The fact that you can read and write must remain a secret between us. It wouldn’t be long before some smart showman came along, eager to make a fortune out of Fantastic Freddy. Either that, or you’d wind up in the hands of scientists itching to dissect your brain for research purposes. Does either of those prospect appeal to you?

FREDDY: (shakes his head emphatically)

MR. JOHN: So it’s a deal: strict secrecy.

FREDDY: (Freddy nods emphatically)

MR. JOHN: (He picks up the phone) Hello, Sophie . . .

FREDDY: (Pg 200-201) [Well] It wasn’t long before Sophie turned up. (Pg 61) Sophie was a girl in a million. (Freddy sits up an waves).

SOPHIE: (Pg 201) (Sophie picks him up) Freddy, [you’re] the bestest, smartest golden hamster in the world.

FREDDY: (to himself) You don’t know how right you are, Sophie. (winks at audience)

SOPHIE: So . . . you’re staying with Mr. John because you’re better off here. But I’ll come and visit you okay? (Sophie kisses Freddy on the top of his head)

FREDDY: (Looks at the audience in embarrassment) Sophie . . . [she’s my] Promised Land of Assyria . . . . (Pg 202) (Freddy turns to the keyboard) Now I knew exactly what my story would be about . . . (He speaks as he types) . . . My Life Story . . . (Pg 2) Maybe I should mention . . . I’m a hamster.
```

---

## IC-1375: I Need My Monster

- Title: I Need My Monster
- Author (byline): Amanda Knoll
- Work: Not specified
- Publisher: Flashlight Press
- Publication date as stated: 2009
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ETHAN, HERBERT, RALPH, CYNTHIA, MACK, GABE
- Teaser before the introduction: Yes
- Spoken words (computed): 1001
- Already set (do not supply): none

### Source block (context only)

```text
Author: Amanda Knoll
ISBN: 978-0979974625
Publisher: Flashlight Press
Date (Month/Year): 2009
```

### Introduction (context only: never use it for content warnings)

```text
Every night, kids across the globe worry that there’s a monster hiding under the bed. It’s a common fear that most adults can relate to—the fear of monsters isn’t new. It’s a fear that pre-dates video games and social media and has persisted throughout the generations. But for Ethan, his worry is that his monster ISN’T under his bed. I Need My Monster by Amanda Knoll
```

### Performance text (classify this)

```text
ETHAN: Tonight, when I looked under the bed for my monster, I found this note instead: “Gone Fishing. Back in a week. –Gabe” What was I going to do? I needed a monster under my bed. How was I supposed to get to sleep if my monster was gone? I tried to sleep, but it wasn’t the same with Gabe. I missed his ragged breathing

(Gabe – ragged breathing) His nose-whistling. (Gabe – nose whistles) The scrabbling of his uncut claws. (Gabe – Scrabbles his claws) How would I ever get to sleep without Gabe’s familiar scary noises and his spooky green ooze? (Gabe – plays with his ooze) It was no use. Gabe would be gone for a week and I just had to have a monster.

turns this childhood fear on its head with humor and giggles and an assortment of substitute monsters!

ETHAN: I climbed quietly out of bed so my parents wouldn’t hear me. (Grown-ups have some strange ideas about monsters under beds.) I knocked on the floorboards, then scrambled back under my covers. I waited nervously. Would a new monster appear? What would he be like? Would his snorting be as cheerful as Gabe’s?

(Creaking) When I heard some creaking under my bed, I knew that the substitute monster had arrived.

HERBERT: (a low, breathy voice) Good evening. My name is Herbert and I will be your monster for the evening.

ETHAN: Herbert? What kind of name is that for a monster?! You don’t sound scary at all. Have you ever scared a kid before?

HERBERT: Well, no, but I have read all the best books on the topic.

ETHAN: Do you have long teeth and scratchy claws?

HERBERT: No, but I have an overbite. And I’m a mouth breather. Listen (Herbert mouth breathes: hihi-huh, hih-huh, hih-huh, hih-huh)

ETHAN: (to audience) Herbert’s panting was kind of scary, but it wasn’t enough for me. (to Herbert) Listen, Herbert, I’m sorry. I just don’t think this is going to work. It’s nothing personal, but I really need a monster with claws.

HERBERT: Picky, picky! As you wish. I’ll go.

ETHAN: There was some more creaking. Then Herbert was gone. (Scratching noises) Some scratching warned me that a second monster had appeared.

RALPH: (in a high, silky voice) Good evening. My name is Ralph. I understand you need a monster with claws. If you would please lean over, I will hold out an arm for inspection.

ETHAN: I crouched on the edge of the bed, hoping to see a horrible shaggy arm with sharp, ragged nails. Instead, I was surprised to see sleekly brushed fur with smooth, shiny claws. (To Ralph) Excuse me, I don’t mean to be rude, but is that nail polish on your claws?

RALPH: Yes, it is. I believe professional monsters should always be well-groomed.

ETHAN: (Heavy sigh) I could tell that this was not going to work either. (To Ralph) I’m sorry to disappoint you, Ralph, but I need a monster with scary claws. (To audience) Like Gabe’s. (Scratching noises) I heard some more scratching and I knew Ralph was gone.

CYNTHIA: (Raspy voice) Check out these claws, kid!

ETHAN: I gather my courage and peered over the edge. The claws were impressive – jagged and dark and razor-sharp. SO far, so good. I was a little nervous. (To Cynthia in a whisper) Could you stick out your tail?

CYNTHIA: Sure, but don’t get scared!

ETHAN: I peeked through my fingers at the slimy tail slithering over the foot of my bed. That’s when I noticed the bow. (To Cynthia) Are you a girl monster???

CYNTHIA: Of course I am. (Snappishly) I’m Cynthia. Do you have a problem with that?

ETHAN: Um, yeah, I do. I definitely need a boy monster. Boy monsters are for boys and girl monsters are for girls. Everybody knows that.

CYNTHIA: (Sniffing) Well, aren’t you a picky one! (Cynthia exits – be creative)

ETHAN: And then she was gone. Was I being too picky? NO! I knew that my monster needed to be well-clawed and menacing. The whole point of having a monster, after all, was to keep me in bed, imagining all the scary stuff that could happen if I got out. (Shuffling noises and slobbering) A fourth monster was under my bed.

MACK: Hey. The name’s Mack. (Extending his claws from under the bed)

ETHAN: One look at his claws proved that Mack was a big, scruffy BOY monster. I shivered. Maybe this one would work out. (To Mack) Those are excellent claws, but do you have a long tail? (Ethan leans over the bed to see)

MACK: (Slurping) No, my tail is stumpy. But I do have an unu-u-u-usually lo-o-o-ong . . . tongue!

ETHAN: Why would I be afraid of a long tongue?

MACK: (Trying to sound terrifying) Oh, I don’t know . . . You never know when I-I-I mi-i-i-ight . . . lick you!

ETHAN: (erupts into laugher)

MACK: (Whining) Well, if you’re not even going to try-y-y- to work with me . . . (Ethan tries to stop laughing) I re-e-e-eally don’t think you should send me away. Kids who reject five monsters in one night . . .

ETHAN: (Interrupting) I did NOT reject five monsters tonight! My regular monster went fishing.

MACK: Fishing, eh? Maybe he just left because you’re SO-O-O picky. Fine. I’m out of here. But I wouldn’t expect another monster tonight if I were you. (Mack exits – be creative)

ETHAN: (looks around his room. Looks under the bed. Tries to sleep but can’t. Sits up) How was I ever going to get to sleep without my monster? I was surprised to hear more creaking under the bed. (Loud creaking and scratching) (To the monster under the bed) I – I thought no more monsters were going to appear tonight.

GABE: Sorry I’m late, kid

ETHAN: (To audience) Whew. It was Gabe.

GABE: I thought I would enjoy fishing, but I didn’t. Those fish scare too easily. No challenge at all. You, however, are challenging, my friend. You’re almost too old to be afraid of monsters. You keep me on my toes. . . Ah, toes . . . a delicious snack. (Gabe’s stomach rumbles with hunger) Now, if you don’t mind, I’d like to start the evening with an ominous puddle of drool.

ETHAN: I peeked over the edge of the bed. Green ooze spread soundlessly from underneath. Then the bed trembled as Gabe unfurled his spiked tail. He was daring me to guess where he might pop up. (Shivers)

GABE: So, you had some substitute monsters tonight. (Sharpening his claws on the bedpost) Were you . . . . scaaaaaared? (Gabe taps his claws impatiently on the bedpost)

ETHAN: When Gabe started tapping, I could tell he wanted to know if I still needed him. No other monster can scare me like you! (Giggling and diving under the covers, pulling them up tight)

GABE: (Soft, comforting snorts then growling) Ha! I knew it! We’re made for each other. (Gabe begins to pull the blanket off the bed) Now, if you could please stick out your foot . . . I’d like to nibble your pinkie.

ETHAN: (yanking the blanket back up and scrunching his feet in so Gabe can’t get them) No toes tonight, but you can have this! (pushes a pillow off the bed) (To audience) I didn’t even hear it hit the floor. Gabe was back. The ooze was perfect. Everything was back to normal. (Shivering again) I’d be asleep in no time.
```

---

## IC-1376: iDNAtity Crisis

- Title: iDNAtity Crisis
- Author (byline): John Pete
- Work: iDNAtity Crisis
- Publisher: SpeechGeek
- Publication date as stated: 2019
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1272
- Already set (do not supply): none

### Source block (context only)

```text
iDNAtity Crisis by John Pete
ISBN: 978-1-61387-119-5
Copyright 2019 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2019, is identical to the printed published
version of this same publication dated 2019. This statement along with the entire printed
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
GURU. What’s up, dudes? Welcome to couples yoga, ‘k? Let us begin

our journey by facing our partners, ‘k? PETER. June? Are you sure that this is a good idea? JUNE. Yes, Peter. You’re always talking about getting to know your true

self, plus you said you wanted to see yoga. PETER. I wanted to watch yoga. That’s different. Sometimes I feel like you

don’t get me… (bit) Ow! June, something bit me! JUNE. It was probably a spider. Just get a Band-Aid. GURU. Shhh, now move to our next pose: the intergalactic tree-frog.

Focus on your true self with this one, ‘k. PETER. True self...spider bite... (puts two and two together, realizes)

Gasp! June! Spider-Man!
JUNE. What?
PETER. I’m Spider-Man!
JUNE. You’re not Spider-Man. You’re afraid of heights. And spiders.

And also men. PETER. That was before I was genetically mutated! I can feel it in my

DNA! I’m special now. GURU. SHHH! If you cannot silently find enlightenment then, like, make

like the Buddha and peace out, ‘k?
PETER. I am Spider-Man. I’m gonna get a DNA test and prove it to you.
JUNE. A DNA test? That’s not gonna tell you who you are.
PETER. You’ll see! You’ll ALL see! Namaste!!!

According to Newsweek from April 2, 2018, nearly half of at-home DNA test turn out to be wrong. Which explains why Ancestry.com’s slogan of “Discover what makes you” recently changed to “(shrug) your guess is as good as ours.” For Peter, the heroic quest to discover his identity is plagued with the annoying reality that our genes tell us very little about who we really are...unless, of course, your jeans have rhinestones on them, then we know EXACTLY who you are. iDNAtity Crisis by Jonathan Pete

PETER. June! Guess whose DNA test came in the mail? THIS GUY (does

Spider-man—similar to “I love you” in sign language— hands

towards himself with left hand)
JUNE. Oh, great. Another $250 spent to tell you you’re an idiot.
PETER. Ha! It was $230. Jokes on you.
JUNE. Peter, you’re not Spider-Man. We’ve been through stuff like this

before, like when you thought you could speak to birds. PETER. Ok, that parrot seemed VERY conversational. JUNE. Or the time you thought you could predict the future. PETER. I knew you were gonna bring that up. JUNE. Or the time you thought you were being recruited by the CIA. PETER. That black suburban followed us for BLOCKS. Besides, this is

science so it has to be true.

JUNE. Peter, A DNA test isn’t going to tell you you’re a superhero, it’s

going to tell you your ancestry: your dad is…
PETER. …German and French.
JUNE. And your mom is...
PETER. …Dutch-Italian.
JUNE. So your DNA test is going to reveal that you’re a German, French,

Italian who wears wooden shoes. PETER. Let’s just see, shall we? JUNE. Huh… Not only are you not Spider-Man. It says you don’t share

any of the ancestry that your parents have. Which would mean… PETER. That... they are not Spider-Man. JUNE. (holding the paper) That they are not your parents. Where did

you get this from? Ancestry.com? MyHeritage?
PETER. Ah some website called Pedigree in Me.
JUNE. You got an off-brand DNA test?
PETER. Dr. Zark Muckerberg is very prestigious. He’s got a ton of

positive Facebook reviews. JUNE. Well, I think you need to challenge the results of this test. PETER. You’re right. We need to get to the bottom of this...right after a

slight costume change.

TRANSITION

PETER. (enters uncomfortably) I’m ready. JUNE. (she now has a purse) Why did you insist on wearing a lycra

unitard under your clothes? PETER. Ha! Unitard? (rotates uncomfortably) Uh, it’s called a supersuit.

You never know when trouble will strike, June. I’m just still

getting used to the way it (a little aggressive) rides up.

TRANSITION

ZARK. Welcome to Pedigree in Me. How can I help you?
JUNE. We are here to contest the results of a DNA test.
PETER. Yeah, I am Spider-Man!
JUNE. Peter.
PETER. I mean, no, I am NOT adopted. (finger to the sky) A mistake has

been made. ZARK. Impossible. Dr. Zark Muckerberg doesn’t make mistakes. I would

know, for I am Dr. Zark Muckerberg! Ooooh! PETER. Wow. It’s an honor to meet you, sir. I have seen many, many

Facebook posts about how great you are. ZARK. (smug) Yes, I wrote most of them! Now then, what seems to be the

trouble? PETER. Trouble? JUNE. No, Peter. No, Dr. Muckerberg. My boyfriend Peter took your

DNA test for… PETER. Webs, webs, webs, shoooot!

JUNE. ...obtuse reasons, and the results that came back don’t match any

of his parental ancestry.
ZARK. Aha, so you’re adopted. (nonsensically deep) Aren’t we all?
JUNE. The thing is, he’s not adopted.
ZARK. Aha, so you were switched at birth. (again, nonsensically deep)

Aren’t we all? PETER. But what if my DNA was so powerful it messed with your science

machines? Like hypothetically if I happened to be a genetically

mutated spider… ZARK. Aha, so you’re a paranoid schizophrenic with delusions of

grandeur. (again) Aren’t we all? JUNE. We’d like you to run the test again, just to...you know, double-

check? ZARK. No need. I perform all the tests myself. JUNE. Mmmhmm… (get the results out) It says he’s 70% Persian, 20%

Sub-saharan African, and varying percentages of Asian and

Babylonian. PETER. That’s not me at all! - ZARK. Well, wah wah wah. I guess you should’ve been 100% baby-

lonian. Let me call the Wah-mbulance.
PETER. I’m not being a baby!
JUNE. He’s just trying to figure out who he is.
PETER. I know who I am. I am Spider-Man! Supersuit (rips open clothes)

activate! JUNE. Oh. Peter, you...you ripped off everything... PETER. ... activate?

TRANSITION

JUNE. Well, we tried, sweetie. PETER. I know you think I’m crazy, JUNE. Well, you are standing on the street wearing a garbage bag

telling me you’re Spider-Man. PETER. Yeah, you right. But the thing is, I’m not ready to give up yet. My

spidey-sense is tingling. JUNE. Honey (goes into the purse) that’s probably chaffing from the

garbage bag. (hands him the powder) Here’s some talcum

powder. PETER. Muckerberg is hiding something. And we need to break into that

facility and find out what. JUNE. Why? PETER. Because... With great powder comes great responsibility. It’s

Spider-Man time! JUNE. (watches him run across) Peter! (watches him jump up) That

drainpipe isn’t gonna...you’re gonna… (he falls) Why don’t we

just use side door? PETER. (Peter infiltrates) This is Dr. Muckerberg’s lab? (relaxes to normal)

I thought there would be… like machines and like… smart stuff.

JUNE. Yeah, It’s just...a giant map on the wall...(picks something up) why

is there a dart on the floor?

(door opens) PETER. Quick, hide! ZARK. Very well… (looks at paper) Ms. Stephanie Smith… (unscrews and

loads) your DNA profile is (individual darts) aha! 30% South

Korean (throws another dart) and, ooooh, 40% North Korean...

(notices June and Peter) Kim Jong Uh-Oh!
PETER. That’s your secret?! You throw darts at a map!?
ZARK. Gasp! The Babylonian!
PETER. I’ve caught you red handed! Or should I say… in a WEB OF LIES!
ZARK. How dare you break into my lab and make a mockery my science

missiles! Take this and that! (throws darts)
PETER. June, look out! (gets hit with a dart)
JUNE. PETER!
PETER. He got me!
ZARK. You damned millennials and your endless nauseating desire to

“know who you are.” You cannot stop me! Me and science will

take over the world. Muaha— what are you doing?
JUNE. Live Facebook feed.
PETER. Namaste, Dork Suckerberg.
ZARK. Data breach! (runs away)

TRANSITION

PETER. Well, I guess I’m not Babylonian...or Spider-Man. JUNE. Who needs Spider-Man? I’ve got a guy who exposed a fraudulent

science empire, exposed himself, and took a dart in his rear for

me. No DNA result is ever going explain why you are the

wonderful way you are. Your true self is who you have become,

not where you came from. PETER. Aww, thanks. It’d still be cool if I was Spider-Man. (He gestures

and web shoots out of his hand and surprises him. He freezes, slow

build into shock and joy.)
```

---

## IC-1377: If the Impressionists had been Dentists

- Title: If the Impressionists had been Dentists
- Author (byline): Woody Allen
- Work: The Insanity Defense
- Publisher: Random House Trade Paperbacks
- Publication date as stated: 2007
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1459
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
The Impressionists are some of the most influential artists of all time and include such famous names as Alfred Sisley, Edgar Degas and Berthe Morisot. Dentistry (which, to some, is art) is one of the most lucrative professions in today’s society and includes such famous names as Norman W. Kingsley, Thomas Curtis and John Henry “Doc” Holiday. Now, the tie between art and dentistry may be hard to fathom at first, but it is seen clearly in “If the impressionists had been Dentists” by Woody Allen.
```

### Performance text (classify this)

```text
Dear Theo,

Will life never treat me decently? I am wracked by despair! My head is pounding! Mrs. Sol Schwimmer is suing me because I made her bridge as I felt it and not to fit her ridiculous mouth! That's right! I can't work to order like a common tradesman! I decided her bridge should be enormous and billowing, with wild, explosive teeth flaring up in every direction like fire! Now she is upset because it won't fit in her mouth! She is so bourgeois and stupid, I want to smash her! I tried forcing the false plate in but it sticks out like a starburst chandelier. Still, I find it beautiful. She claims she can't chew! What do I care whether she can chew or not! Theo, I can't go on like this much longer! I asked Cezanne if he would share an office with me, but he is old and infirm and unable to hold the instruments and they must be tied to his wrists but then he lacks accuracy and once inside a mouth, he knocks out more teeth than he saves. What to do?

Vincent

Dear Theo, I took some dental X-rays this week that I thought were good. Degas saw them and was critical. He said the composition was bad. All the cavities were bunched in the lower left corner. I explained to him that's how Mrs. Slotkins mouth looks, but he wouldn't listen! He said he hated the frames and mahogany was too heavy. When he left, I tore them to shreds! If that was not enough, I attempted some root canal work on Mrs. Wilma Zardis, but halfway through I became despondent. I realized suddenly that root canal work is not what I want to do! I grew flushed and dizzy. I ran from the office into the air where I could breathe! I blacked out for several days and woke up at the seashore. When I returned, she was still in the chair. I completed her mouth out of obligation but I couldn't bring myself to sign it.

Vincent

Dear Theo,

Once again I am in need of funds. I know what a burden I must be to you, but who can I turn to? I need money for materials! I am working almost exclusively with dental floss now, improvising as I go along, and the results are exciting. God! I have not even a penny left for Novocain! Today I pulled a tooth and had to anesthetize the patient by reading him some Dreiser. Help.

Vincent

Dear Theo,

Have decided to share offices with Gauguin. He is a fine dentist who specializes in bridgework, and he seems to like me. He was very complimentary about my work on Mr. Jay Greenglass. If you recall, I filled his lower seven, then despised the filling and tried to remove it. Greenglass was adamant and we went to court. There was a legal question of ownership, and on my lawyer's advice, I cleverly sued for the whole tooth and settled for the filling. Well, someone saw it lying in the corner of my office and he wants to put it in a show! They are already talking about a retrospective!

Vincent

Dear Theo,

I think it is a mistake to share offices with Gauguin. He is a disturbed man. He drinks Lavoris in large quantities. When I accused him, he flew into a rage and pulled my DDS off the wall. In a calmer moment, I convinced him to try filling teeth outdoors and we worked in a meadow surrounded by greens and gold. He put caps on a Miss Angela Tonnato and I gave a temporary filling to Mr. Louis Kaufman. There we were, working together in the open air! Rows of blinding white teeth in the sunlight! Then a wind came up and blew Mr. Kaufman's toupee into the bushes. He darted for it and knocked Gauguin's instruments to the ground. Gauguin blamed me and tried to strike out but pushed Mr. Kaufman by mistake, causing him to sit down on the high-speed drill. Mr. Kaufman rocketed past me on a fly, taking Miss Tonnato with him. The upshot, Theo, is that Rifkin, Rifkin, Rifkin and Meltzer have attached my earnings. Send whatever you can.

Vincent

Dear Theo, Toulouse-Lautrec is the saddest man in the world. He longs more than anything to be a great dentist, and he has real talent, but he's too short to reach his patients' mouths and too proud to stand on anything. Arms over his head, he gropes around their lips blindly, and yesterday, instead of putting caps on Mrs. Fitelson's teeth, he capped her chin. Meanwhile, my old friend Monet refuses to work on anything but very, very large mouths and Seurat, who is quite moody, has developed a method of cleaning one tooth at a time until he builds up what he calls "a full, fresh mouth." It has an architectural solidity to it, but is it dental work?

Vincent

Dear Theo,

I am in love. Claire Memling came in last week for an oral prophylaxis. (I had sent her a postcard telling her it had been six months since her last cleaning even though it had been only four days.) Theo, she drives me mad! Wild with desire! Her bite! I've never seen such a bite! Her teeth come together perfectly! Not like Mrs. Itkin's, whose lower teeth are forward of her uppers by an inch, giving her an un-derbite that resembles that of a werewolf! No! Claire's teeth close and meet! When this happens you know there is a God! And yet she's not too perfect. Not so flawless as to be uninteresting. She has a space between lower nine and eleven. Ten was lost during her adolescence. Suddenly and without warning it developed a cavity. It was removed rather easily (actually it fell out while she was talking) and was never replaced. "Nothing could replace lower ten," she told me. "It was more than a tooth; it had been my life to that point." The tooth was rarely discussed as she got older and I think she was only willing to speak of it to me because she trusts me. Oh, Theo, I love her. I was looking down into her mouth today and I was like a nervous young dental student again, dropping swabs and mirrors in there. Later I had my arms around her, showing her the proper way to brush. The sweet little fool was used to holding the brush still and moving her head from side to side. Next Thursday I will give her gas and ask her to marry me.

Vincent

Dear Theo,

Gauguin and I had another fight and he has left for Tahiti! He was in the midst of an extraction when I disturbed him. He had his knee on Mr. Nat Feldman's chest with the pliers around the man's upper right molar. There was the usual struggle and I had the misfortune to enter and ask Gauguin if he had seen my felt hat. Distracted, Gauguin lost his grip on the tooth and Feldman took advantage of the lapse to bolt from the chair and race out of the office. Gauguin flew into a frenzy! He held my head under the X-ray machine for ten straight minutes and for several hours after I could not blink my eyes in unison. Now I am lonely.

Vincent

Dear Theo,

All is lost! Today being the day I planned to ask Claire to marry me, I was a bit tense. She was magnificent in her white organdy dress, straw hat, and receding gums. As she sat in the chair, the draining hook in her mouth, my heart thundered. I tried to be romantic. I lowered the lights and tried to move the conversation to gay topics. We both took a little gas. When the moment seemed correct, I looked her directly in the eye and said, "Please rinse." And she laughed! Yes, Theo! She laughed at me and then grew angry! "Do you think I could rinse for a man like you!? What a joke!" I said, "Please, you don't understand." She said, "I understand quite well! I could never rinse with anyone but a licensed orthodontist! Why, the thought I would rinse here! Get away from me!" And with that she ran out weeping. Theo! 1 want to die! I see my face in the mirror and I want to smash it! Smash it! Hope you are well.

Vincent

Dear Theo,

Yes, it's true. The ear on sale at Fleishman Brothers Novelty Shop is mine. I guess it was a foolish thing to do but I wanted to send Claire a birthday present last Sunday and every place was closed. Oh, well. Sometimes I wish I had listened to Father and become a painter. It's not exciting but the life is regular.

Vincent
```

---

## IC-1378: Inside the Corner Office: The Real Story of The Bonker’s Candy Factory

- Title: Inside the Corner Office: The Real Story of The Bonker’s Candy Factory
- Author (byline): Mike Beyer
- Work: Exposed! Eight 10-Minute Scenes About What Really Happened, Pg 34-42
- Publisher: Heuer Publishing
- Publication date as stated: 2013
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARLES, GRANDPA, BILLY, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1546
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mike Beyer
Book: Exposed! Eight 10-Minute Scenes About What Really Happened, Pg 34-42
ISBN: 978-1600036767
Publisher: Heuer Publishing
Date (Month/Year): 2013
```

### Introduction (context only: never use it for content warnings)

```text
Inside the Corner Office: The Real Story of The Bonker’s Candy Factory by Mike Beyer
```

### Performance text (classify this)

```text
(Musical intro – hum or vocalize the melody of The Candy Man by Sammy Davis, Junior*)

An empty office. Billy Bonkers strides in briskly, approaches the desk and begins writing furiously. Charles and Grandpa stick their faces through the partially open door cautiously.

CHARLES: There he is Grandpa! There’s Willy Wonk – I mean, Billy!

GRANDPA: Huh?

CHARLES: Nothing. Stupid lawyers. The tour of his candy factory has taken us to his private office at last! All the other naughty children have met a nasty end, and we’re the only ones left. But why isn’t he inviting us in?

GRANDPA: What?

CHARLES: (Much louder) I said, we’re the only ones left on this tour, and I – never mind. I’m going in. (Charles enters the office and Grandpa cautiously follows)

CHARLES: Mr. Bonkers, sir? (No answer) Sir?

BILLY: (Unpleasant, business-like) May I help you?

CHARLES: Well, my Grandpa and I are the only ones left on the tour, so we were wondering what happens now.

BILLY: (Not looking up) Yes. Well. The exit door is down the hall, second door on your left.

CHARLES: Sir, what about the five pounds of candy per day?

BILLY: Excuse me?

CHARLES: (Taking the ticket from his pocket) It says that everyone who completes the tour gets five pounds of candy every day for the rest of their lives.

BILLY: (Snatching the ticket from Charles’ hand and inspecting it) Ah. So, it does. HOWEVER, it does NOT allow for little thieving boys and their elderly thieving grandpas!

CHARLES: We didn’t steal anything!

BILLY: Really? Then you deny going into the Belchy SugarBlast Drinks room and helping yourself to a taste? Even though such tasting is strictly forbidden?

CHARLES: (Head down) No. We drank it.

BILLY: Aha! I knew it. Well then. If there is nothing else you require, please show yourselves OUT.

CHARLES: We almost died in that room! We got such a sugar rush from that drink that I almost had a heart attack! Look what your drink did to Grandpa!

GRANDPA: (To the wall) Hello there!

BILLY: Then I trust you have both learned a valuable lesson. And that lesson is: DON’T TOUCH OTHER PEOPLE’S STUFF! You don’t get the five pounds of candy! You get NOTHING! Now goodbye!

CHARLES: But-

BILLY: I SAID GOODBYE-BYE! (Pause)

CHARLES: Let’s go. (He turns, takes GRANDPA by the hand, and together they prepare to exit)

GRANDPA: Where we going now?

CHARLES: Home, and the bread and water that waits for us. (They stop at the door, and CHARLES looks back at BILLY) Hold on a second. (He reaches into his pocket, goes back and places a piece of candy on BILLY’S desk then proceeds to leave)

BILLY: (touched) The honesty of a child. Returning that which he could have easily kept. . . (He whirls around) Charles! Don’t go. Please.

CHARLES: But you said the tour was over-

BILLY: I know what I said, but don’t you see? This was the test! You were told to get a piece of my Molarcrusher Rock Candy and give it to my main competitor.

CHARLES: Yes. Mr. Vanilla Fudgerton told me to get a piece of this candy and he would pay me a million dollars and all the chocolate bacon Slurpalicious Shakes I wanted.

BILLY: Yes, and all the other children gave the pieces to Fudgerton, who secretly works for me. But not you! Don’t you see what that means? It means you’ve won! All this will one day be yours!

CHARLES: You mean. . . I’ll be president and CEO of Bonker’s Candy Factory? Oh, my goodness! You don’t want to do that!

BILLY: Oh, but I do. A child is the only one who can truly love fantastic items like the Oreo Cookie/Ranch Dressing Cream Puffs. A child is more open to new ideas – (aside to audience) and by open, I mean he’ll run it exactly my way.

CHARLES: This is a dream come true! When do I start?

BILLY: No time like the present! (He produces a contract and signs it) Charles, when you sign this, you will be the unquestioned boss of the world-famous Bonker’s Candy Factory.

(Hands the contract and pen to CHARLES. GRANDPA leans over CHARLES’ shoulder and reads the contract. He gasps.)

GRANDPA: Do it, Charles! (Charles signs it)

BILLY: Excellent! Fantastic! Splendid! Adjectives! Let’s get into my rocket-powered elevator and grab the rest of your family!

CHARLES: (Charles’ demeanor changes) Let’s you have a seat and let the new boss do his thing!

BILLY: Excellent plan – wait a minute, what?

CHARLES: You heard me. (BILLY sits down in his old chair) You’re sitting in my seat, Mr. Bonkers.

BILLY: Haha, you’re already taking to the job! I like that. Want to go back down to my strawberry lake and eat some mango-flavored orchids?

CHARLES: No thanks. I have plans for that room! Grandpa, take a memo. (GRANDPA takes a notebook and pen from the desk)

GRANDPA: Go, Charles!

CHARLES: You know, Billy, I’m not feeling the name “Bonker’s Candy Factory.” I think a new name is needed. I think the name “Bonker’s Organic Healthy Creations Farm” has a nice ring to it, don’t you?

BILLY: Sacrilege! The name of Bonkers is known from Kalamazoo to Timbuktu! Why, children everywhere look forward to consuming my creations!

CHARLES: Yes, and thanks to your creations, obesity is at an all-time high!

BILLY: Well, that’s not MY fault! It’s the parents who are responsible! Children today are so SPOILED!

CHARLES: Yes, but I plan to change everything inside your company. For starters, your Bonker’s Cherry Cake Batter and Double Caramel Ice Cream will now become just Bonker’s Cherry Yogurt.

BILLY: (Spluttering with rage) You. . . you. . . Ridiculous! No one will eat it. This is an outrage!

CHARLES: The Bonker’s Organic Healthy Creations Farm will help children around the world reach their true nutritious potential -- through healthy snack offerings!

BILLY: My candy is nutritious! Look how fit I am! (He attempts to do jumping jacks. He fails. A beat)

CHARLES: (unimpressed) So, as I was saying, we’ll make smoothies that will cause children to do jumping jacks! Our chewing gum will actually remove plaque and whiten teeth! Our glazed donuts will contain more vitamins than *sugar*!

BILLY: You’re mad! (to audience) He’s ruining everything I’ve helped to create! I knew I should have picked the fat kid who got sucked through the tubes.

CHARLES: His Type 2 diabetes is probably irreversible. But I’ll have him work for me. He can help me convert the chocolate eggs into low-calorie egg whites. He’ll also lead the Bonker’s Marathon Training Team!

BILLY: Charles, Charles, Charles. Before you go completely crazy and send us all to ruin, let’s just talk this out first. My whole mission in life has always been to bring smiles to children’s faces! To make the world taste good!

GRANDPA: Do we even need Bonkers anymore?

CHARLES: Nah. Send him down to the old Exploding Room. We’ll make him a test taster of our Quinoa Brownie Delights.

BILLY: OK, OK, I get it! Candy equals bad! I understand now. But let me help you – I know how this factory works, and I can help you achieve your dreams!

CHARLES: I’m listening.

BILLY: OK, I promise to get rid of the High-Fructose Corn Syrup and Artificial Sweetener Room.

CHARLES: Good.

BILLY: But it helped my chocolate bars taste so delicious! Don’t you like flavor?

CHARLES: Not when kids can barely climb the stairs and develop more pimples than there are stars in the sky!

BILLY: But those candy bars keep those kids from developing bad habits in life. Parents actually DEPEND on me to keep their little brats in line.

CHARLES: I’m not sure I follow you.

BILLY: You see, children need rewards to work for. What better reward than candy? No one will clean their room or eat their broccoli if the incentive is just a stupid apple.

CHARLES: Apples are not stupid! Besides, my new orchards will produce apples as big as your head. Not only that, they give you the ability to do long division problems in your head the minute after you eat them!

BILLY: Whatever! It’s still an apple! They don’t comfort anybody! Who’s going to sit down on a lonely Saturday night for a good cry, a couple of movies, and a tub of kiwis and carrots?

CHARLES: Plenty of people, if they know they have to get up the next morning and run eight miles! We’ll have Bonker’s Nutrition Clubs set up worldwide!

BILLY: But can’t we at least give the lazy people some Bonker’s Sticky Stomach Taffy, just to give them a little break from this terrible world?

GRANDPA: Sorry, Bonkers. The jig is up.

BILLY: Grandpa? Could I perhaps interest you in a Bonker’s Nut-tastic Dark Chocolate Toffee and Peanut Butter Avalanche? A parting gift from me. You won’t be seeing these anymore.

GRANDPA: Well, thank you, Mr. Bonkers. (Takes a bite.)

CHARLES: Grandpa! DON’T EAT THAT – (They fight over the candy bar, but Grandpa is crafty and manages to pop the entire bar into his mouth)

GRANDPA: (with his mouth full) Sorry, Charles. But. . . wow! I forgot how GOOD this tastes!

CHARLES: For your information, those three bites just put about 12,000 calories on your frame, and will keep five dentists employed for at least a year scraping all that toffee from your teeth!

GRANDPA: Maybe we can have one room here in the factory for candy, and the other 7,000 for your health food and juice products!

CHARLES: I don’t believe what I’m hearing!

BILLY: Listen to your Grandpa, Charles. Maybe you should let him run the factory for now, until you get a little bit older.

CHARLES: No deals! Now, Grandpa PLEASE! Step away from the candy!

GRANDPA: But Charles, I haven’t had one of these in years! Do you know why?

CHARLES: The last of your teeth fell out?

GRANDPA: I started listening to all the fitness and nutrition do-gooders! Shouldn’t we at least still observe the time-honored tradition of dessert? In moderation?

CHARLES: We’ll have candy bars! We’re going to roll out Bonker’s Chocolate-Flavored Edamame Krispy Krunch! The youth of tomorrow will thank us!

GRANDPA: Charles, I’m stepping in. I’m appointing myself CEO of the Bonker’s Candy Factory until further notice. At first I went along with your plan, but these food creations of yours push the envelope in ways that are bad and wrong. Edamame Krispy Krunch? Gross. (He takes the contract from the desk and rips it up)

CHARLES: NO!!!

GRANDPA: We’ll split up the factory. Billy can continue to make his fantastically magical candy, and you can start on your super- healthy goodies.

CHARLES: I suppose half-ownership of Bonkers is better than a lifetime doomed to eating cabbage soup and noodles.

BILLY: [And] I get to keep this corner office.

CHARLES: (pouting again as a young child) This is so unfair! GRANDPA!

GRANDPA: Now go to your room. (CHARLES stomps out. BILLY goes to the desk and pours two glasses)

BILLY: (Giving a glass to GRANDPA) Belchy Sugar Blast?

GRANDPA: Don’t mind if I do!

TOGETHER: (Raising glass) To health! (They drink and both burp loudly)
```

---

## IC-1379: Jeremy Fink and the Meaning of Life

- Title: Jeremy Fink and the Meaning of Life
- Author (byline): Wendy Mass
- Work: Not specified
- Publisher: Little, Brown Books for Young Readers
- Publication date as stated: Nov 2006
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: JEREMY, PALM READER, LIZZY, NICK, LARRY, VENDOR, LIZZIE, SAMANTHA, RICK, LIZY, OFFICER, MOM, DAD’S VOICE
- Teaser before the introduction: Yes
- Spoken words (computed): 1472
- Already set (do not supply): none

### Source block (context only)

```text
Author: Wendy Mass
ISBN: 978-0316058292
Publisher: Little, Brown Books for Young Readers
Date (Month/Year): Nov 2006
```

### Introduction (context only: never use it for content warnings)

```text
Jeremy Fink collects mutant candy, won’t go more than four blocks from home if possible and he definitely doesn’t like surprises. But this year for his birthday he has one doozy of a surprise.

See, Jeremy is supposed to open this gift from his father on his birthday, but there’s one problem. 4 keys are required to open the box, 4 keys are needed to discover the MEANING OF LIFE. But the keys are missing. Jeremy and Lizzy set off to find the keys, but what they don’t know is that there might be other ways to find out the meaning of life.

Jeremy Fink and the Meaning of Life by Wendy Mass
```

### Performance text (classify this)

```text
JEREMY: (Preface, Pg i-iii) [Hi] I’m Jeremy Fink, a city kid born and bred, and my sweat (sniffs armpits) smells like peanut butter. I’m such a picky eater, my mother feeds me peanut butter sandwiches at every meal. So now when I sweat, it smells like peanut butter instead of B.O. (smiles proudly) My best friend, Lizzy, is a notorious troublemaker. She has a lot of opinions, usually negative. For example, she thinks my collection of mutant candy is gross. I think she’s jealous because she didn’t think of it first. The best is a peanut M&M the size of my pinky finger. I bet I could get a fortune for that one on eBay. Today is my thirteenth birthday. If my father had spen[t] his thirteenth birthday playing Little League, I would be here. Instead, all those years ago, my father wandered down the Atlantic City boardwalk and wound up in front of an old palm reader. She picked up his hand and held it to her face and said

PALM READER: (in a Russian accent) “You vil die ven you are forty years old.”

JEREMY: The prediction was wrong. My dad didn’t die when he was forty. He was only 39. But Dad must have taken the prophecy seriously, because he prepared for his death, and this box proves it. (Picks up the box from a nearby table and reads the inscription) THE MEANING OF LIFE: FOR JEREMY FINK TO OPEN ON HIS 13TH BIRTHDAY. I never would have guessed, when Lizzie and I [were] given the box a month ago, that those instructions would be so impossible to follow. *****

(Pg 4) (NICK, the mailman, enters wheeling his huge blue cart)

LIZZY: (Saluting) Howdy, Nick

NICK: (tipping his hat) Well if it isn’t Lizzy Muldoun and Jeremy Fink. Let’s see what I’ve got for you guys today. (Nick reaches into his cart and lifts out a box)

LIZZY: (Pg 7) (Takes the box from Nick, who exits) (she reads the return address label aloud to Jeremy) Folgard and Levine, Esquires.

JEREMY: (takes box from Lizzy, opens the box and finds another wooden box inside. He reads the inscription) (Preface, Pg 13) THE MEANING OF LIFE: FOR JEREMY FINK TO OPEN ON HIS 13TH BIRTHDAY? (Preface, Pg iii) (to audience) This box has come to symbolize all my hopes, all my failures. Before I do anything else, I need to go back over everything that happened this summer.

JEREMY: (Pg 32) [The first thing we do is] take the box to Larry’s Locks and Clocks to see if he can do anything. (Jeremy and Lizzy enter the shop to find Larry, a thin man in overalls wiping his hands on a napkin)

LARRY: (Pg 34-35) What can I do for you today?

LIZZY: Can you open this? (plopping the box on the counter)

JEREMY: I’ve lost the keys (Larry examines the box with furrowed brow, then rests his hands on the box, eyes closed) So . . . do you think you can open it for us?

LARRY: (Pg 36-37) (eyes snapping open) Nope. This is no ordinary box. Sorry to disappoint you, but the only way anyone is getting into this box is with the keys.

(Lizzy and Jeremy take the box and leave the store)

JEREMY: (Pg 33) (to Lizzy) Okay. If the locksmith can’t help us, we have to go to . . . the flea market! (to audience) (Pg 44) The flea market is basically two big parking lots that smells like a combination of boiled hot dogs and sweat. And not the good, peanut butter kind of sweat. (Sniffs armpits again, then they set off to find a vendor of old keys. They approach a vendor) (Pg 47) We’re looking for some old keys. Do you have any?

VENDOR: (rummages around under a table and finally finds a box) (Pg 54) You’re welcome to go through my collection and see what you can find.

JEREMY: (Pg 48) (Lizzy and Jeremy look in the box) Um, these aren’t exactly what we had in mind.

VENDOR: Huh? Why not?

LIZZIE: Well, for one thing, they aren’t keys. They’re locks.

VENDOR: Is that right (she peers into the box) Oops, sorry ‘bout that. Keys, locks, all part of the same thing, right? (She laughs a bit and then wanders off to help another customer)

LIZZY: (Pg 40) Our best bet [was] the flea market. (thinking hard and then lights on an idea) (Pg 160-161) This morning, I told Rick and Samantha about your box and how we can’t find the keys.

JEREMY: You did WHAT!??

LIZZY: Well, I’m glad I did because Samantha had a really great idea . . . . she said we should ask your dad!

JEREMY: What are you talking about? Didn’t you tell her?!

LIZZY: Of course, I told her. Samantha said we can hold a séance. She has a Ouija board and everything. It’s worth a shot. *******

(Pg 163-166) (Lizzy and Jeremy go to Samantha and Rick’s apartment (they are 14-year old twins), ring the bell and Samantha answers)

SAMANTHA: Come on. We have the Ouija board set up in the living room. (They follow Samantha to the living room where Rick is waiting)

JEREMY: (rolling his eyes as he sees Rick) Rick, [why are you] wearing a cape??

RICK: Samantha made me. She said if I didn’t wear it and we couldn’t contact your father, it would be all my fault. So . . . (turns and elaborately displays his cape) I’m wearing it.

SAMANTHA: (in a hushed tone as she lights candles) We are ready to begin. Everyone join hands. We are calling upon the spirit of. . . (Out of the corner of her mouth, she whispers) What’s your dad’s name?

JEREMY: (also whispering) Daniel Fink

SAMANTHA: . . . the spirit of Daniel Fink. Mr. Fink, (releasing hands and placing her fingers on the Ouija board pointer) if you can hear the sound of my voice, please send us a sign. (A horn honks outside, and Samantha responds enthusiastically) Thank you! O great spirit of Daniel Fink, we call upon you to answer our plea. Please tell us where we can find the keys to the box you left for (she whips her head to gaze penetratingly at Jeremy) Jeremy. (They wait expectantly for the pointer to move . . . . nothing)

LIZY: (to Jeremy in a whisper) Do you feel anything?

JEREMY: (frustrated and exasperated, he removes his hands from the pointer and stands up) Yeah . . I feel like an idiot! This is ridiculous! (changing his tone and trying to sound sincere – To Samantha) You were great. I’m not sure I really believe it’s possible to contact my dad. But thank you for trying. (He picks up his birthday box and as he exits) I know you were only trying to help. (to audience) (Pg 170) I have only myself to blame . . . and maybe Lizzy. Definitely Lizzy. ***** The next day ******

LIZZY: (Pg 158-159) (storming into Jeremy’s bedroom and yanking open the blinds) Come on. It’s eleven o’clock already. (She spies a lump in Jeremy’s bed) Is that lump next to you your dad’s box? (no answer – she reaches over and throws back the blanket) It IS the box! (She picks it up) So you’re sleeping with it now?

JEREMY: (softly and shaking his head) I need to figure out my purpose. Until I do, what’s the use of getting up. I can’t face the world until I know why I’m here.

LIZZY: You’re kidding me! You can have your existential crisis – whatever that means – once you are out of bed. I’m pretty sure you won’t find your purpose lying there. Get up! . . . (Pg 59) Our keys are hidden in the office of (Pg 7) Folgard and Levine, Esquires. We’re gonna get into that office, and we’re gonna find them.

JEREMY: (leaping out of bed and grabbing the box from Lizzy) Breaking and entering? That’s your big plan?

LIZZY: (Pg 60) (excited) That’s the spirit! *****

(Pg 86-87) (Lizzy and Jeremy cautiously enter the offices of Folgard and Levine, Esquires)

LIZZY: (in a whisper) Let’s get moving. You look in the office (pointing in that direction) and I’ll check out here in the waiting area.

JEREMY: (exploring the office, opening drawers, cabinets, etc) Hey, Lizzy (shouting as loud as he dares) I might have found something!

LIZZY: (Pg 89-90) (rushing in, to peer over Jeremy’s shoulder) See anything?

JEREMY: (disappointed) [Just] Pipes, dust and wires. (He closes the cabinet, then turns and sees a very round and re-faced policeman standing next to Lizzy – he reacts in fear and raises both hands above his head) . . . Officer? (his voice cracks on the last word)

OFFICER: (Pg 91) Would you like to tell me what you were doing? Breaking and entering is a very serious offense, you know.

JEREMY: (Pg 92-93) (to audience) Office Polansky makes us tell him our real names and addresses . . . and he types them into his computer. He is a very slow typist. (to Lizzy in a whisper) You swore we wouldn’t get arrested!

LIZZY: (to Jeremy – forgetting to whisper) We’re not getting arrested! (to the Officer) Are we?

OFFICER: No, I’m not going to arrest you. I was thinking of community service. You don’t have any big plans this summer, right?

JEREMY: (to audience) Great. How am I going to open the box if I can’t look for the keys because I will be too busy picking up garbage on the West Side Highway or planting flowers in some church garden. (Pg 265) It was hopeless . . . [but then my 13th birthday arrived and everything changed!] . . . . (Pg 258) I feel OLDER! ***** (NOTE: Original text states: Mom and Lizzy come in, singing the happy birthday song)

MOM: Happy birthday to you!

LIZZY: Happy birthday to you!

MOM: Happy birthday dear Jeremy . . .

LIZZY: Happy birthday to you.

MOM: (clapping and cheering)

LIZZY: (Pg 263-265) Are you ready for my gift now? (She pulls out a small box and hands it to Jeremy. It’s not wrapped and Jeremy opens it, reaches inside and takes out a set of keys)

JEREMY: (Eyes stretching so far open they hurt) Is this . . . Is this the . . . Is –

LIZZY: Yup! (bouncing up and down with excitement) It’s the key(s)!

JEREMY: But how did you, where did you, how . . . . (anger building) All this time I’ve been thinking it was hopeless. But you knew. You knew!

LIZZY: (uncertainly, she looks at Jeremy’s Mom. Mom winks at her encouragingly) The harder something is to acquire . . . the more satisfying it is when you finally find it . . . (sadly) I just wanted to give you a present you’d never forget. NARRATOR (Mr. Oswald): (Pg 281) It’s amazing how people will play along for a good cause. [NOTE: in the original text this line is spoken by Mr. Oswald, a character that has been cut from this selection.] ***** Flashbacks******

NICK: (Pg 4) Let’s see what I’ve got for you guys today. (Nick reaches into his cart and lifts out a box)

LARRY: (Pg 36-37) . . . the only way anyone is getting into this box is with the keys.

VENDOR: (Pg 48) Oops, sorry ‘bout that. Keys, locks, all part of the same thing, right?

OFFICER: (Pg 91) Breaking and entering is a very serious offense, you know. *****

JEREMY: (Pg 282) (to Lizzy) You did all this for me? Why would you do that?

LIZZY: (Pg 268) What are you waiting for??

JEREMY: Maybe we shouldn’t open it. Maybe we weren’t’ supposed to find the keys after all. Let’s just toss the box.

LIZZY: (shouting) Are you SERIOUS!!

JEREMY: Nah. Let’s open it! (Jeremy uses the keys to open all four locks on the box and it opens) (To audience) (Pg 269-273) [It’s] and envelope with my name on it. Trying, and failing, to keep my hands from trembling, I open it. Dear Jeremy.

(as Jeremy reads, we hear his dad’s voice)

DAD’S VOICE: As I write this you have just had your eighth birthday. I hope I am there beside you on your 13th birthday to tell you all this myself. If I’m not, I hope you can feel that I am always with you. [It’s been] 25 years since that fortune-teller in Atlantic City gave me such a dire prediction. I asked my father – your grandfather – if someone could really predict another person’s future. He said the future changes every day. He said we, not someone else, have the power to create our own lives.

[Since that day] I made sure to pay attention to everything I was doing. To be fully in the moment. Because that’s all life is, really, a string of moments that you knot together and carry with you. It is something no one can ever take away from you. It will protect you and guide you, because it IS you.

Ralph Waldo Emerson wrote: “Most of the shadows in this life are caused by our standing in our own sunshine.” Wisdom is found in the least expected places. Always keep your eyes open. Don’t block you own sunshine. Be filled with wonder. Life is all about the journey. I hope this was one you’ll never forget. I love you, Jeremy.

JEREMY: (Looks up from his letter with tears in his eyes)
```

---

## IC-1380: Jimmy vs The Velvet Hammer

- Title: Jimmy vs The Velvet Hammer
- Author (byline): Jon McGovern
- Work: Best Student One Acts: Vol. 4 (ed by Friesen, L) From Alter Egos; Pgs 15-22
- Publisher: Dramatic Publishing
- Publication date as stated: August 2000
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: JIMMY, VELVET HAMMER
- Teaser before the introduction: Yes
- Spoken words (computed): 1436
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jon McGovern
Book: Best Student One Acts: Vol. 4 (ed by Friesen, L)
From Alter Egos; Pgs 15-22
ISBN: 978-0871299123
Publisher: Dramatic Publishing
Date (Month/Year): August 2000
```

### Introduction (context only: never use it for content warnings)

```text
It is never too late (or too early) to give yourself a new identity. If there are feats you wish to accomplish in life that seem to be too out of character for your current name, perhaps it's time to give yourself a boost with an alter ego. Clark Kent had Superman, Bruce Wayne had Batman, heck; even Miley Cyrus had Hanna Montana, so why shouldn’t Jimmy have The Velvet Hammer?

Jimmy vs the Velvet Hammer from Alter Egos by Jon McGovern
```

### Performance text (classify this)

```text
JIMMY: (Pgs 15-22) Oh my head! (Looks down at his clothing) Oh, God, it’s happened again. (To the audience) I’ve got a problem . . . don‘t laugh, ‘cause it’s not funny, it’s causing me lots of mental stress. (Adjusts himself and fixes his tie). I’ve been . . . possessed! No, it’s not what you think, it’s not like I think UFO’s came down and took over my body; and I didn’t summon up the devil of anything . . . but I might as well have – Oh, I’ll start from the beginning . . .

JIMMY: See I’m pretty shy, I always have been . . . but . . . I really have always wanted to be a . . . STUD! You know, be tough, but tender, always says the right thing at the right time . . . like those guys from the seventies like Shaft and Superfly . . . But I never could be. I mean I get with a girl and my tongue would just stop – and I couldn’t even form sentences. I just turn into Dork King of the Universe . . . “yer pretty” is usually the best I can do. That’s the best of my “repertoire” . . .

Well, it had been a (Make quote marks in the air) “little while” since I was in a (Make quote marks again) “relationship.” (Sees audience might not be buying it) OK! IT HAD BEEN A REALLY LONG TIME! And I was getting a bit (Make quote mark) “lonely,” if you know what I mean . . . it got so bad there was a time when I just got – *you know* on the brain. I know you’re thinking “who doesn’t have *you know* on the brain sometimes.” SOMETIMES is the key word there. It was like some tribal beating in my head – “*girlsGIRLSgirlsGIRLSgirlsGIRLSgirls* – a girl could say “excuse me” when passing me in the hall and I would start to have visions of her saying. . . oh boy. I couldn’t do work – not even my favorite – calculus! I would just end up drawing dirty pictures and ordering *Cinemax*. I was turning into even more of a social misfit than before! It had to stop! Work was suffering, my professors were asking questions, my lab partners were getting annoyed, and my little dog Woofer was starting to look nervous. So, I used all my effort to just push it down – repress it – make it go to the back of my mind – I had a mantra –YOU MUST REPRESS YOU MUST REPRESS – I figured I would just get it off my mind, until I really met a girl who liked me and the time was right.

Oh, how wrong I was. The subconscious mind is a dangerous thing – tricky – because I thought my mantra worked. I was able to do work again – do my calculus, Woofer breathed a sigh of relief . . . But little strange things started to happen, even though they were deeply mixed into the rest of my normal life. I’d go to buy a pair of socks – sing a little tune – “Oh, I’m buyin’ a pair a socks” – and instead I’d buy a pair of super-tight leather pants, a velvet turtleneck and a wide-brim hat with a feather, or I’d find myself casually browsing for sneakers – you know, Keds . . . Nikes . . . Dockers . . . but instead I’d get a pair of black, thigh-high, high-heeled boots! I mean, it all seemed normal at the time, like I needed those things . . . but after a while I had this strange collection of stuff. Like I was preparing for something – or someone. Then one night it all came together.

I was sleeping in bed and this voice said . . .

VELVET HAMMER: (In a deep, gruff and soulful bass) Git up!

JIMMY: I was shocked someone was in my apartment! So I said in my meanest voice . . . Who’s there?

VELVET HAMMER: It’s me, boy! Git up!

JIMMY: And then . . . my butt got slapped (Slaps butt and continues to do so faster and faster) – HARD – but no one was around . . . and then I realized (Looks at his hand as the slapping stops) it was me. I was slapping my own butt! “What’s going on?” I said. There still wasn’t a light on, so I yelled . . . Who are you? Where are you?

VELVET HAMMER: I’m Velvet Hammer and I’m in you!

JIMMY: I didn’t understand. So, I jumped out of bed and flipped on the light but no one was there! I was standing in front of my mirror . . . and instead of seeing me in my froggies-making-toast PJs, I was in these tight leather pants, velvet turtleneck and wide-brim hat with a feather, and then I said to myself . . . well, my lips moved and sound came out . . . but I didn’t want to say it . . .

VELVET HAMMER: “See boy! We look good! Had to dress us up.

JIMMY: What do you mean, us? I’m ME.

VELVET HAMMER: Not anymore, baby. Yo’ you and me . . . Velvet Hammer! You brought me here yo’self! You tried to push all yer sexy suff, all yer fun desire and tried to be Mr. Nice Boy. Well, all that stuff had to go somewhere . . . and, baby, I am from that place . . . I am the silky smooth, superfly, superfine guy from the deep heart of your personality. ‘Cause tonight it’s time to party! You have been Mr. Nice Boy too long and that means the Velvet Hammer been Mr. Nice Boy too long.”

JIMMY: Look! I don’t know what you are – you, evil spirit – but I won’t let you possess me!

VELVET HAMMER: Possess you? I am you, the silky smooth, superfly fun part. And therefore, I just want us to have a little fun! Now look, you can either help out and be aware of what’s goin’ on and have the best night of your life, or I can just (Goes into a ‘70s-style kung fu fight mode.) Hutaa Hehtaa Huh huh Velvet Hamma! (Back to normal) Knock you out like I did when I was dressin’ us! The choice is yours.

JIMMY: Oh . . . I was at this horrible turning point – let this weird evil spirit take over or try to fight? Get (Does a Jimmy remix of Velvet’s kung fu) HooTa Hoo-Ha . . Ve-Vet Hammerrrr . . . knocked out? . . . or have the best night of my life? He was gonna do it anyway, so I said . . . OK

VELVET HAMMER: Good – now just relax, let it go – Velvet Hammer’s in control!

JIMMY: Then it went black . . .

VELVET HAMMER: (*theme from Shaft plays, hums, struts and does some mean dance moves – to a woman) Hey, baby, my name’s Velvet Hammer . . . ‘cause I’m smooth like velvet . . . but I *you know* like a hammah!” (Moves to another woman) Hey, girl . . . I’m industrial strength – ‘cause I work so hard– oohahhchaa!”

JIMMY: He was handing it out . . . getting phone numbers . . . getting phone numbers . . . Me! . . . as this Alter Ego was having the time of my life! But then I realized the more fun he was having, the more I felt like I was fading . . . then it hit me! If I didn’t take back control of my body – the Velvet Hammer part of me would never give me up. I had to get back control! So, I waited till things calmed down a bit and – Velvet was doing his hair in the men’s room – and then I tried to jump back in.

VELVET HAMMER: Woop! What are you tryin’ to do, boy?

JIMMY: Look, Velvet, I’m taking my body back and there’s nothing you can do about it!

VELVET HAMMER: Don’t jive me, cat! I am just about to get to the piece of resistance of the night! The part that’s gonna get us everything we want and more – I just about to strut on the dance floor!

JIMMY: Velvet, I have got control and I’m not going to give it up again.

VELVET HAMMER: That’s what you think, boy! I’m gonna dance if it kills me!

JIMMY: Then I realized Velvet had control of one half of the body and I had control of the other!

VELVET HAMMER: Hit it, Mr. DJ! (Dance music plays in the background as the battle for control over the body begins. Velvet’s half trying to bump and grind, Jimmy’s half trying to control it. As the dance continues we hear . . . )

JIMMY: Velvet! Velvet, stop it stop stop . . . Oh! Don’t do it, Velvet . . . Not the roboto, anything but that!” I didn’t even know I could do the Running Man! (He tries but only succeeds in making the dance more ridiculous . . .) There was nothing I could do . . . I was fighting it hard, but it only ended up making me look like I was doing a funkier and funkier chicken! But . . . I was also starting to like it! I was the sexy star of the dance floor – everybody wanted me. So I just started to go with it . . and Go! And GO! And GOOOOO!

(Jimmy strikes a John Travolta pose and the music stops). And then I blacked out . . . and I woke up, well, a lot like this -- I have these Velvet blackouts every weekend! Five days a week I’m nice mild-mannered bow-tie wearing, Discovery Channel watching me . . . and two days a week I’m this weird ‘70s guy – swingin’ it all over town! I thought about trying to get an exorcist to get rid of him and stuff like that, but . . . if I do that, I’d also be getting rid of the one good side effect of all this . . . THE FLASHBACKS! (Goes into a trance)

VELVET HAMMER: Oh, you’re a bad girl! Bad Girl! Oh, don’t do that . . . (Loving it) . . . don’t do that . . . (Snaps out of the trance)

JIMMY: WOW, WE SURE HAD FUN, DIDN’T WE, VELVET?”

VELVET HAMMER: We sho did.

JIMMY: But I’m tired, we gotta rest up for tonight.

VELVET HAMMER: Yeah! Why don’t we go to get some Aunt Bertha take-out. . .

JIMMY: Oh OK. Well, I’ll see you guys later. (waves to the audience like the nerd he is)

VELVET HAMMER: I’ll see you later, baby girl. Come on, Jimmy, let’s sang it. (exit, strutting/stumbling singing the 70’s tune of your choice, alternating between Velvet’s and Jimmy’s voice)
```

---

## IC-1381: The Last Supper, or the Dead Waiter

- Title: The Last Supper, or the Dead Waiter
- Author (byline): John Stewart
- Work: Naked Pictures of Famous People
- Publisher: Harper Collins
- Publication date as stated: Oct 1999
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1767
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

The virtual blackout has recently been lifted, in light of an astonishing discovery in the Sinai Peninsula. The only written account pertaining to the existence of Jesus Christ has been found. The manuscript contains explicitly reference to a dinner party Jesus had with twelve male friends. It is an eye-witness account penned by Avram the Waiter, who served the Christ party at the then-popular Jerusalem eatery, Jerry's.

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

## IC-1382: The Last Touchy Feely Drama on the American Stage

- Title: The Last Touchy Feely Drama on the American Stage
- Author (byline): Greg Gamble and Lee Howard
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: Feb 1999
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ANDY, PAT, FATHER, SON, ANDY AND PAT, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1401
- Already set (do not supply): none

### Source block (context only)

```text
Author: Greg Gamble and Lee Howard
ISBN: 978-0871298966
Publisher: Dramatic Publishing
Date (Month/Year): Feb 1999
```

### Introduction (context only: never use it for content warnings)

```text
What if theater had commentators . . . just like sports. You have to be kidding, you say? Commentators? No way! Just imagine it though . . . The Last Touchy Feely Drama on the American Stage by Greg Gamble and Lee Howard
```

### Performance text (classify this)

```text
ANDY: Hello, good evening, and welcome to the first and final performance of The Last Touchy-Feely Drama on the American Stage! I'm Andy McCunn, and I'm here with Pat O'Keefe to bring you all the passion, all the pageantry, all the gooey senti-mentalism that's sure to unfold tonight. There's a palpable feeling of anticipation in the air over this crowd as they impatiently crumple their programs and await that inevitable dimming of the houselights. Pat, give us some of your patented prognostications for the evening. What sort of strategies are you envisioning?

PAT: Pow! That's what I predict! [Emerson Tod Fudgee’s] gonna come out with both barrels blazing on the first light cue! Exaggerated walks, exaggerated accents! Lots of spray-on gray in the dad's hair -- be watching for that! And don't be surprised if we get a script loaded with family conflicts culled from actual experiences!

ANDY: Introspective creature of loneliness or just another ass with a typewriter -- you make the call! Emerson Tod Fudgee first came to the public's attention with his play Christopher Columbus: Genocidal Fruitcake. -not that the play was ever performed. But not content with accomplishing nothing, he boldly stepped forward with his next play, Queer God. It was a concept piece performed entirely in cliche. And then, hot on its heels came 1991's musical extravaganza, Victims on Parade!

PAT: A stunner!

ANDY: Certainly, Victims is what Fudgee will be remembered for; from the big, splashy, show-stopping dance number, "Compensatiable," right up to the act one finale, where the Ghost of the Dead Shoplifter descends from the heavens and grants the characters the coveted mantle of victim status.

PAT: And not just the characters, Andy, but I think everyone in that audience felt like a victim. Especially at Broadway prices. Victims is still an unfinished work, isn't it?

ANDY: No one's really sure. Its run off-Broadway was titanically short, closing after only forty-three minutes. So, it's not known if it has a second or a third act. It is, in fact, Fudgee's longest-running play! Who would've suspected an art form that began in the bold, shark-filled waters courageously charted by the nervy aplomb of Tennessee Williams, Eugene O'Neill and Arthur Miller, could have evaporated into a creatively stag-nant, mosquito-infested backwater of emotionally manipulative dreck, celebrating failure as the human experience.

PAT: But the "viva la victim" play has indeed become the "Ol' Yeller" of the art world. And somebody's gotta love it enough to take it out back and ka-pow!

ANDY: It's time for the awesome spectacle to commence! (With overly dramatic. hushed golf-announcer tones.) A hush falls over the crowd . . . a few stray coughs . . . the creaking of seats . . . (Shattering the mood.) Pat! What's the game plan for the opening? Will it be lights up with the first character already on stage, thus thrusting us into the drama? Or are we going to bring the lights up slowly and watch him enter, so we can read his history and his personality in his mannerisms, in his gait?

(PAT rushes to take his place by the huge wipe-board. During the rest of his speeches, PAT rapidly sketches out stats and stick-figures to illustrate his postulations and facts.)

PAT: Well, Fudgee 's opened three of his last five plays with the character already on stage, It's an in-your-face approach that's worked well for him. But, major event that this is, I'd look for a little risk taking tonight; possibly the first character making his entrance in an ambient half-glow of a colored gel . . . pink, purple-some emotional hue.

ANDY: And here comes our first character in the half-light dim of. . . a pink gel! Good call, Pat! (FATHER slowly lowers himself into the chair.) He . . . takes . . . his . . . seat. . . and the fuse is lit on this powder keg of performing art!

(With nothing happening. ANDY fills the void with random commentary whispered dramatically in quick bursts.) Here at 7:08 . . . on a Friday evening in June . . . Emerson Tod Fudgee's bold new work . . .The Last Touchy-Feely Drama on the American Stage . . . The tension's thick in the air . . . Fudgee needs a success here . . . . (Lights up to full.) And it's lights up! We have lights at full on Emerson Tod Fudgee's Last Touchy-Feely Drama on the American Stage! (Pregnant pause. The ANDY wait excitedly, the FATHER does nothing but read his newspaper.) (Sound fix: Knocking on a door.) It looks like the drama's under way! Pat, are we going get some blocking out of this door knock?

PAT: From any other director you might get a cross to go and answer the door . . .

(Diagrams an actor's cross to a door. As all wait breathlessly, FATHER shifts in his chair, but never rises.) But, no! Fudgee's gonna resist the predictable and keep the father stationary . . . (Draws an. X over the chair and makes a "hundred" circles around it.) . . . possibly mixing it into the character devel-opment somehow! (Sound fix: Louder knock at a door.)

ANDY: It looks like we're coming up on the opening line of The Last Touchy-Feely Drama on the American Stage!

FATHER: Come in! (The SON enters. He is dressed in ill-fitting community theatre prop-room clothes and carries a suitcase.)

SON: (stiffly). Hi . . . Dad.

ANDY: Well, there's obviously some painful memories here!

FATHER: (scoffing snort). Hmph! And what's that supposed to mean?

SON: (confrontationally). What?

FATHER: (boiling). Oh, you heard me!

SON: (like a human time bomb). I said, "Hi."

FATHER: (spitting venom). Liar!

SON: (as if he's been hassled for an hour). All right, all right! I said, "Hi, Dad!" Happy?

FATHER: Hmph! (coming apart). What, what, what would you know about happiness, anyway? Huh? Huh? Huh? What would you know about a lifetime of happiness-happy thoughts, happy memories, just one happy marriage? Hmm? Hmm? Hmm? (Takes a long cross and wrings his hands.) Goddammit! Everywhere-suffocating happiness! Tell, me, Mr. High-and-Mighty, Mr. Showboat, tooling around town shoving your precious G.E.D. in everyone's face, tell me . . .

(Right into SON's face) . . . how am I supposed to feel?

SON: . . . Happy?

FATHER: (with anomalous cruelty). What do you think? (SON pauses, showcasing his full compass of frustrated gestures and false-start mumblings.)

SON: You . . . You don't want to know!

FATHER: No! You don't want to know! (Something's eating at him.)

ANDY: Another of those masterful pauses you could drive a truck through! Pat! Are we working towards a revelation?

PAT: Bet the baby on it, Andy! No crossing to speak of, but look for a tum from profile left to profile right to milk some meaning out of it!

FATHER: (gazing off into space). I'm drinking again.

SON: (drops suitcase). Oh, my God!

ANDY: No tum, Pat! No tum, no cross and a very disappointing revelation!

PAT: The feeling of underwhelmment coming over this capacity crowd tonight is very real! They want Fudgee swingin ' for the fences! But right when he should've taken a triple toe-loop he singles out of it and two-foots the landing!

FATHER: (broken and confused). Why did you come back?

SON: I had to be here for Mom's funeral.

FATHER: That was a year ago!

SON: (ashamed of his own rage). Don't you think I know that? (Tears welling up.) You never listened to me . . . ever! Wrapped up in your own little hypocritical world, making us all eat your middle-class Spaghettios and your suburban Wonder Bread! (Lights dim.)

ANDY: The lights are dimming. Are we headed for an early curtain call?

PAT: (can't believe his eyes). No! No! Fudgee, is setting up for the monologue! What's going to happen is they'll take it all down to a single, eerie spotlight, pull an actor forward to the apron of the stage, and have him speak directly to the audience!

ANDY: So, in essence, what we're discussing here is nothing less than the destruction of the fourth wall!

PAT: The total obliteration of it!

ANDY: The father's frozen in tableau and . . . the son is up! Up and headed for the apron of the stage to express for us all the pain we carry with us but can't release without geniuses like Fudgee! (Spotlight on the SON.)

SON: Will he ever know the real me?

ANDY: A question! Perfect for portraying hope as a straw god!

SON: How do you say, "Dad, I just want you to care! I just want you to hold me"?

(Lights up to full. SON returns to his previous place. FATHER unfreezes, while) (wallowing in drama). I'm seeing a psychiatrist.

FATHER: (disgusted beyond belief). In what way?

SON: (courageously). In the only way I know how!

FATHER: I'm ... so sorry.

SON: No, I'm sorry . . . I never told you . . . I'm gay.

ANDY: Oh, my! There's magic in the air tonight! It looks like they're going for the Tony!

SON: Look at me, Dad! I'm gay! I'm gay! I'm gay! I'm gay! Gay, gay, gay, gay, gay, gay, gay! It's not your fault any more than it's not my fault, and it's nobody's fault that it's not anybody's fault!

FATHER: You're not my son!

SON: I'm begging you to accept me and Jeremy!

FATHER: No! I mean you're not my son. You made a confession, now I'm making one! (Dredging up a painful past.) Your mother . . . she had an affair . . . on the very day we were married! (Buries his head. then looks up with his mood swung to a torpid, blank expression.) It's getting dark outside.

ANDY: (golf-announcer-esque), A symbolic line.

SON: (torpid. blank expression). And it's so cold already.

ANDY: (golf-announcer-esque). And again.

FATHER: Is there something you're not telling me?

SON: You know already.

FATHER: But I need to hear you say it.

SON: And I need you to hear me say it. I'm . . . I'm . . . (SON tries and tries to pull some dark secret out of his innards. After stretching out his hands several times with "I'm . . . " he stretches them out and says nothing.)

PAT: The play-action fake!

SON: I'm . . . (SON's dreadful attempts at hauling an admission from his soul reach a fever pitch of overacting.) I'm HIV-positive!

ANDY: And there it is! They're walkin' away with this year's Tony Award!

ANDY AND PAT: Tony! Tony! Tony! Tony! Tony! Tony! Tony! Tony

ANDY: And that'll about wrap it up here for The Last Touchy-Feely Drama on the American Stage! Emerson Too Fudgee, previously known as a spectacularly unsuccessful hack, proves in the pinch to be a spectacularly successful hack, bidding farewell to an endearingly trite and delightfully derivative theatrical genre that I'm sure will be sorely missed!

PAT: [I’m] Pat O'Keefe

ANDY: [And] this is Andy McCunn saying,

TOGETHER: G'night!
```

---

## IC-1383: Laws Concerning Food and Drink; Household Principles; Lamentations of the Father

- Title: Laws Concerning Food and Drink; Household Principles; Lamentations of the Father
- Author (byline): Ian Frazier
- Work: Lamentations of the Father: Essays, Pg 8-13 [Originally published in the Feb 1997 edition of The Atlantic Magazine]
- Publisher: Farrar, Straus and Giroux
- Publication date as stated: April 2008
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: FATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1218
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ian Frazier
Book: Lamentations of the Father: Essays, Pg 8-13
[Originally published in the Feb 1997 edition of The Atlantic Magazine]
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

## IC-1384: The League of Semi-Superheroes

- Title: The League of Semi-Superheroes
- Author (byline): Val Smith and Michael Bigelow Dixon
- Work: Thirty 10-Minute Plays for 4, 5 and 6 Actors from Actors Theatre of Louisville's National Ten-Minute Play Contest
- Publisher: Smith & Kraus
- Publication date as stated: Aug 2001
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: EL GRANDE DE SAYER DE NAY, THE HUMAN PUDDLE, MASTER OF THE OBVIOUS, WABBIT WOMAN, PUSHY BOB, CAROL, EL GRANDE DE SAYER, EL GRANDE, HUMAN PUDDLE
- Teaser before the introduction: Yes
- Spoken words (computed): 1311
- Already set (do not supply): none

### Source block (context only)

```text
Author: Val Smith and Michael Bigelow Dixon
Book: Thirty 10-Minute Plays for 4, 5 and 6 Actors from Actors Theatre of Louisville's
National Ten-Minute Play Contest
ISBN: 1575252791
Publisher: Smith & Kraus
Date (Month/Year): Aug 2001
```

### Introduction (context only: never use it for content warnings)

```text
In a world of semi-terror and almost confusion, only one league of nearly-heroes can save us. Meet El Grande De Sayer De Nay, Master of the Obvious, Pushy Bob, Wabbit Woman, The Human Puddle, and Carol, the league Receptionist . . . Together they make up THE LEAGUE OF SEMI-SUPERHEROES by Val Smith and Michael Bigelow Dixon. . . If they were brave enough to answer the phone . . . Everyone would know who they are!
```

### Performance text (classify this)

```text
CAROL’S VOICE (on the answering machine): Hello. You have reached the number of the League of Semi-Superheroes. If this is an emergency, please stay on the line and an operator will pick up shortly. (pause) If this is a message for only The Human Puddle, please press “1” now. If this is a message for Wabbit Woman, please press “2” now. (pause) If this is a message for Master of the Obvious, please press “3” now. (pause) If this is a message for El Grande De Sayer DE Nay, (pause) don’t bother to press anything. If this is a message for Pushy Bob, press “4”. and get out of the way. (pause) If this is a message for the entire League, please leave it at the tone----

(The League leans in eagerly to listen. The sound of the tone. There is the sound of snorts and giggles, and then a hang-up,)

EL GRANDE DE SAYER DE NAY: Told ya.

THE HUMAN PUDDLE: It could have been something. It might have been something.

EL GRANDE DE SAYER DE NAY: They only call ’cause they think we’re a joke.

(Human Puddle bursts into tears.)

MASTER OF THE OBVIOUS: You’ve upset The Puddle.

EL GRANDE DE SAYER DE NAY: So what else is new?

WABBIT WOMAN: (she sings) “Rain Drops are Falling on My Head”

PUSHY BOB: So! Carol, whaddaya doin’? What are you working on there?

CAROL: (working on her crossword puzzle.) Oh, I don’t know, Pushy Bob. What does it look like to you?

MASTER OF THE OBVIOUS: Say, isn’t that a crossword puzzle you’ve got there?

CAROL: I’m surrounded. I give up.

PUSHY BOB: (looking over Carol’s shoulder) Oh, way-way-way-way-wait! Forty-four down, a five letter word for “screw-up”! Hold on, hold on. No, hold on now, hold on! Ahhhhhhh—

CAROL: (grabbing crossword puzzle back from Pushy Bob.) Look! Instead of working MY crossword puzzle, why don’t we deal with your bills? For instance. Here. The bank statement. Oh, my. Surprise, surprise. You’re overdrawn on all your accounts.

MASTER OF THE OBVIOUS: Ooh bummer.

CAROL: Exactly. Ooh bummer. And what is this? Why, it’s an eviction notice from the landlord. Oh dear. What should you do? Any semi-super money to take care of this? Any semi-super ideas? Any ideas at all? (an embarrassed silence among the Semi-Superheroes.) No? Well then, there’s a little matter of my salary. You are familiar with the word “salary?” Money in exchange for work provided?

MASTER OF THE OBVIOUS: Ah c’mon Carol. We know what salary means.

PUSHY BOB: Hey, we’ll write you a check!

CAROL: I’ll start clearing out my desk.

MASTER OF THE OBVIOUS: Our bank account is overdrawn. (Carol begins emptying out her desk, collecting her personal belongings in a box. Pushy Bob hovers around her, checking out her stuff.)

WABBIT WOMAN: Hizth izzth ridiculuzzz! They can’t take away our office, for cwying out wowed. How will we do ouh bidness?

EL GRANDE DE SAYER: Look around, Wabbit Woman. Don’t you see? Oh, c’mon! All of you? Any of you? Don’t you see?

WABBIT WOMAN: Well. We’re wookin’—

EL GRANDE DE SAYER: I’m speaking metaphorically!

MASTER OF THE OBVIOUS: No fair! You can’t expect me to figure that out.

WABBIT WOMAN: He’s Master of the Obvious.

EL GRANDE DE SAYER: Don’t you see, it isn’t working! We have no business! In a year, nobody has called for our services. It can’t work! It will never work! Never ,never, never!

(The Human Puddle sobs loudly.)

MASTER OF THE OBVIOUS: Geez. There goes The Puddle.

EL GRANDE: Oh what else is new!

PUSHY BOB: Look out everybody! The glass is half empty again.

EL GRANDE: This time it’s complete empty. We’re being evicted. Carol is thinking of leaving.

CAROL: Correction. Carol is leaving. (To Pushy Bob.) Will you please get out of the way!

PUSHY BOB: Okay! Have a big gigantic din-dong-cow!

EL GRANDE: I mean, who are we kidding? “Semi-Super Heroes!” Our talents make no sense!

CAROL: Finally. Thank you, God.

THE HUMAN PUDDLE: Ordinary people with “unusual” skills helping other people in need.

MASTER OF THE OBVIOUS: That was the whole idea.

EL GRANDE: Sounds good, Human Puddle. Only one problem. Who needs stupid skills?

WABBIT WOMAN: Ma skiffs ant stoofid! Can you smoke, snorkel AND smirk? I can!

EL GRANDE: Who cares?

MASTER OF THE OBVIOUS: It may not be obvious to everyone but even if it is—doesn’t it follow, El Grande de Sayer de Nay, that you also have a stupid skill? Hmmmmmmmmmmmmmmmmmm?!

EL GRANDE: NO!

CAROL: Guys, there’s one more piece of…

PUSHY BOB: Look! Right now, somebody out there might need a push guy! And if I can help by bulldozing my way in somewhere, hey—I’m there!

THE HUMAN PUDDLE: Or jus someone who likes to—who can’t help—crying—

(The Human Puddle sobs uncontrollably.)

CAROL: Guys, you’re not listening.

WABBIT WOMAN: We’re wisionaries!

EL GRANDE: We’re The League of Personality Disorders!

MASTER OF THE OBVIOUS: Some people choose not to see it that way. While others obviously do.

PUSHY BOB: I’ve always thought we could use more aggressive advertising. Loud and In Your Face.

WABBIT WOMAN: Yah! Willlwe Wowed!

PUSHY BOB: Yeah! Willlwe willlwe Wowed!

CAROL: Guys. If I could have your attention a…

PUSHY BOB: Ah! “Gaffe”! Five ltters meaning “screw-up___could work.

CAROL: Thank you, Pushy Bob! I wanted to spare everyone’s feelings, but there is one more piece of information I need to share with you. The Grant? (puzzled pause.) Remember The Grant? (puzzled pause) The last glint of rescue in an otherwise dark sea of despair?

(HUMAN PUDDLE weeps, a high-pitched sob.)

PUSHY BOB: (A flash.) Oh! Yeah! The grant! (He knocks CAROL’S box off the desk accidentally.) Helping people with our unusual skills!

CAROL: Well. You didn’t get the grant.

WABBIT WOMAN: Oooooooooooooooo

THE HUMAN PUDDLE: Oh God! How much rejection do they think we can take?

MASTER OF THE OBVIOUS: Maybe the word “semi-“ gave them a pause.

EL GRANDE DE SAYER: You heard me! Quit! We follow Carol on out of here.

CAROL: I walk alone!

MASTER OF THE OBVIOUS: You mean—give up the office.

WABBIT WOMAN: Look. We have to have faith. Faith that somehow our talents, howevah stwange, howevah cweative, howevah--- meager---- amount to something. I’m not giving up smoking for nobody. I’ll continue to smoke— and smirk— and yes!, snorkel wheorbel I foltb libit.

MASTER OF THE OBVIOUS: Smoke on, wabbit woman!

HUMAN PUDDLE: We just wanted to help people.

PUSHY BOB: Well, what the hell do people want! I mean , excuse me for illuminating the human condition but we do so have something to offer! Can’t they see that?!

MASTER OF THE OBVIOUS: Push on, Pushy Bob!

EL GRANDE DE SAYER: No! This is the end. We have to accept that. We have to be big enough to say “yes” to “no!”

(A moment while they all ponder this statement)

MASTER OF THE OBVIOUS: We didn’t get our grant.

PUSHY BOB: And who’s to blame? (pause) Carol. We’ll miss you. You’re fired.

CAROL: Thank you, Pushy Bob. Look guys. I’m sorry. But there is such a thing as appreciating the realty of a situation. (pause)

EL GRANDE DE SAYER: Exactly, Carol! Reality! When we walk out that door, We must know who we are, and always will be—unwanted, useless, distracting, irritating, unloved and unlovable strange-ohs. When we walk out that door, We’re gonna know we face a world that has no use for us and our hopeless, pathetic little lives!

(EL GRANDE has rested his case. Stunned silence. After a moment, THE HUMAN PUDDLE sobs loudly. A pause)

CAROL: Well. Let me put it this way. I’ve enjoyed my time here, but I never really understood how smoking and snorkeling and crying and being pushy and telling people what they already know—Or being negative on a continual basis—I mean , how are those qualities supposed to help other people? Huh? (pause)

WABBIT WOMAN: OK. It’s a little weird. But is that any weason to weject us?!

CAROL: Yes. Yes, it is. (Pause during which lights flicker and then go out) Well, there it is. Reality. Third and final notice from the electric company. Tell ya wha. I’ll take the answering machine in lieu of a check(CAROL disconnects the answering machine and tucks it under her arm.) Good luck to all of you. And I really mean that. (CAROL exits)

MASTER OF THE OBVIOUS: She’s gone.

EL GRANDE DE SAYER: We don’t need her.

PUSHY BOB: She left her crossword puzzle.

WABBIT WOMAN: (sings another chorus of “Raindrops” sadly)

(Long pause. The phone rings. They all look at it. It rings again.)

MASTER OF THE OBVIOUS: Phone’s ringing.

HUMAN PUDDLE: Aren’t you going to answer it?

EL GRANDE DE SAYER: No.

PUSHY BOB: Just another noxious nincompoop lookin’ for a cheap laugh prob’ly (phone rings)

HUMAN PUDDLE: But what if. . .

EL GRANDE DE SAYER: What!!

HUMAN PUDDLE: Well, what if it’s a guy in Sault Ste. Marie who’s in big trouble ‘cause he can’t accept what’s happening in his life.

MASTER OF THE OBVIOUS: He needs help hearing some hard—but obvious-- truths. (phone rings)

HUMAN PUDDLE: Or, like, what if it’s some shy kid in Cheyenne, who never gets picked when they’re choosing up teams and never gets called on in class, who always walks home alone.

PUSHY BOB: Maybe all she needs is an assertive role-model, a little jolt of brass, somebody to tell her not to be afraid to just barge in and make it happen. (phone rings)

HUMAN PUDDLE: What if it’s a guy in St. Louis who can’t say “no” to a boss who keeps making him stay late to work and that’s ruining his home life.

EL GRANDE: He needs help, he needs someone who can help him see the importance of saying “NO” emphatically. And often. (Phone rings)

HUMAN PUDDLE: Or maybe it’s –uhhh-maybe it’s---uhhhh---

WABBIT WOMAN: A synchwonized swim team!—who want a cewtain fashion nostalgia to their swimsuits!—And who despewately need to—learn to— you know— smirk for the judges! (phone rings)

HUMAN PUDDLE: Or maybe, just maybe, it’s a bunch of people right here in this city. A group of dreamers who’ve lost their way. And maybe what they need most of all, maybe they need in fact, is just a darn good— (dissolving in tears)
```

---

## IC-1385: The Legend of Spud Murphy

- Title: The Legend of Spud Murphy
- Author (byline): Eoin Colfer
- Work: Not specified
- Publisher: Miramax Books
- Publication date as stated: Sept 2004
- Event as filed: Humorous Interpretation
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

SPUD MURPHY: Oops. Wrong stamp. Sorry about that. (a glare) One more thing. Any more of your little games and I get nasty. There are worse things in this desk than rubber stamps.

(she brings out her potato shooter and cocks it with a hiss) Enjoy swimming (she laughs as the boys run for the door)
```

---

## IC-1386: The Littlest Hitler

- Title: The Littlest Hitler
- Author (byline): Ryan Boudinot
- Work: The Best American Non-Required Reading 2003
- Publisher: Houghton Mifflin, Co.
- Publication date as stated: Oct 2003
- Event as filed: Humorous Interpretation
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

## IC-1387: Los Vendidos (The Sellouts)

- Title: Los Vendidos (The Sellouts)
- Author (byline): Luis Valdez
- Work: Luis Valdez Early Works (Pg 40-52)
- Publisher: Dec 1990
- Publication date as stated: 978-1558850033
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: SANCHO, SECRETARY, FARMWORKER, JOHNNY, REVOLUCIONARIO, MEXICAN-AMERICAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1438
- Already set (do not supply): none

### Source block (context only)

```text
Author: Luis Valdez
Book: Luis Valdez Early Works (Pg 40-52)
ISBN: Arte Publico Press
Publisher: Dec 1990
Date (Month/Year): 978-1558850033
```

### Introduction (context only: never use it for content warnings)

```text
Williams.
```

### Performance text (classify this)

```text
HONEST SANCHO’s Used Mexican Lot and Mexican Curio Shop. Three models are on display in HONEST SANCHO ’s shop. HONEST SANCHO is moving among his models, dusting them off and preparing for another day of business.

SANCHO: (Pg 40-52) Bueno, bueno, mis monos, vamos a ver a quién vendemos ahora, ¿no?

(Well, well, my monkeys, let's see who we sell to now, right?) (To audience.) I’m Honest Sancho and this is my shop. All I need now is a customer. (woman enters) Ay, a customer!

SECRETARY: Good morning, I’m Miss Jimenez from. . .

SANCHO: Ah, una chicana! Welcome, welcome Señorita Jiménez.

SECRETARY: (Anglo pronunciation.) JIM-enez. My name is Miss JIM-enez. Don’t you speak English? What’s wrong with you?

SANCHO: Oh, nothing, Señorita JIM-enez. I’m here to help you.

SECRETARY: That’s better. As I was starting to say, I’m a secretary from the Governor’s office, and we’re looking for a Mexican type for the administration.

SANCHO: Well, you come to the right place, lady. This is Honest Sancho’s Used Mexican Lot, and we got all types here. Any particular type you want?

SANCHO: . . . Any particular type you want?

SECRETARY: Yes, we were looking for somebody suave … debonaire. Dark. But of course, not too dark. Perhaps, beige.

SANCHO: Beige, just the tone.

SECRETARY: One more thing. He must be hard-working.

SANCHO: That could only be one model. Step right over here, lady. This is our standard farmworker model. Take special notice of his 4-ply Goodyear huaraches, made from the rain tire. This wide-brimmed sombrero is an extra added feature; keeps off the sun, rain and dust. And our farmworker model is friendly. Muy amable. Watch. (Snaps his fingers.)

FARMWORKER: (Lifts up head.) Buenos días, señorita. (His head drops.)

SANCHO: But his most attractive feature is that he’s hardworking. Let me show you. (Snaps fingers. FARMWORKER stands.)

FARMWORKER: ¡El jale! (He begins to work.)

SANCHO: As you can see he is cutting grapes. He also picks cotton. (Snaps. FARMWORKER begins to pick cotton.) That’s his slow speed for late in the season. Here’s his fast speed. (Snap. FARMWORKER picks faster.)

SECRETARY: Chihuahua … I mean, goodness, he sure is a hard worker. But is he economical?

SANCHO: Economical? Señorita, you are looking at the Volkswagen of Mexicans. Pennies a day is all it takes. One plate of beans and tortillas will keep him going all day.

SECRETARY: What about storage?

SANCHO: No problem. You know these new farm labor camps? They were designed with our model in mind. Five, six, seven, even ten in one of those shacks will give you no trouble at all. And here’s an added feature: every year at the end of the season, this model goes back to Mexico and doesn’t return, automatically, until next Spring.

SECRETARY: How about that. But tell me, does he speak English?

SANCHO: Bueno … no, pero he has other features …

SECRETARY: No! He just won’t do!

SANCHO: Okay, okay, pues. We have other models.

SECRETARY: I hope so. What we need is something a little more sophisticated. An urban model.

SANCHO: Ah, from the city! Over here in this corner of the shop is exactly what you’re looking for. Introducing our new 1969 JOHNNY PACHUCO model! Streamlined. Built for speed, low-riding, city life. Let me just turn him on. (Snap. JOHNNY walks to stage center with a PACHUCO bounce.)

SECRETARY: What was that?

SANCHO: That, señorita, was the Chicano shuffle.

SECRETARY: Okay, what does he do?

SANCHO: Anything and everything necessary for city life. For instance, survival: he knife fights. (Snaps. JOHNNY pulls out a switchblade and swings at SECRETARY. SECRETARY screams.)

SANCHO: And here’s a feature no city model can be without. He gets arrested, but not without resisting, of course. (Snap.)

JOHNNY: En la madre, la placa. I didn’t do it! I didn’t do it! (JOHNNY turns and stands up against an imaginary wall, legs spread out, arms behind his back.)

SECRETARY: Oh no, we can’t have arrests! We must maintain law and order.

SANCHO: But he’s bilingual. He speaks English! He’s economical. Nickels and dimes. You can keep Johnny running on hamburgers, Taco Bell tacos, Lucky Lager beer . . .

SECRETARY: Mr. Sancho, I don’t think you quite understand what we need. What we need is something that will attract the women voters. Something more traditional.

SANCHO: Ah! (He smiles meaningfully.) Step right over here, señorita. Introducing our standard Revolucionario type. As you can see, he is well-built, sturdy, durable.

SECRETARY: What does he do?

SANCHO: You name it, he does it. He rides horses, stays in the mountains, crosses deserts, plains, rivers, leads revolutions, follows revolutions, kills, can be killed, serves as a martyr, hero, movie star. Listen to this. (Snap.)

REVOLUCIONARIO: (Scream.) ¡Viva Villaaaaa!

SECRETARY: That’s awfully loud.

SANCHO: He has a volume control. (He adjusts volume. Snap.)

REVOLUCIONARIO: (Mousey voice.) Viva Villa.

SANCHO: And even if you didn’t see him in the movies, perhaps you saw him on TV. He makes commercials. (Snap.)

REVOLUCIONARIO: Is there a Frito Bandito in your house?

SECRETARY: Oh yes, I’ve seen that one!

SANCHO: And finally, there is one outstanding feature about this model I know the ladies are going to love: he’s a genuine antique! He was made in Mexico in 1910!

SECRETARY: Made in Mexico? Mr. Sancho, I thought he was an American product. I’m sorry. We can’t buy anything but American made products. We need Mexican models, such as these, but it’s more important that he be American.

SANCHO: Wait a minute! Mexican but American? Mexican but … (A sudden flash.) American! Yeah, I think we’ve got exactly what you want. He just came in today! Give me a minute. (He exits and brings out the MEXICAN-AMERICAN model, a clean-shaven middle class type in a business suit, with glasses.) Introducing our new 1970 Mexican-American! Ta-ra-ra-raaaa!

SECRETARY: (Impressed.) Where have you been hiding this one?

SANCHO: He just came in this morning. Feast your eyes on him! Sturdy U.S. Steel frame, streamlined, modern. As a matter of fact, he is built exactly like our Anglo models, except that he comes in a variety of darker shades: naugahide, leather or leatherette.

SECRETARY: Naugahide.

SANCHO: Well, we’ll just write that down. Yes, señorita, this model represents the apex of American engineering! He is bilingual, college educated, ambitious! He is intelligent, well-mannered, clean. Did I say clean? (Snap. MEXICANAMERICAN raises his arm.) Smell.

SECRETARY: (Smells.) Old Sobaco, my favorite.

SANCHO: (Snap. MEXICAN-AMERICAN turns toward SANCHO.) Eric? (To SECRETARY.) We call him Eric García. (To ERIC.) I want you to meet Miss JIM-enez, Eric.

MEXICAN-AMERICAN: Miss JIM-enez, delighted to make your acquaintance. (kisses her hand.)

SECRETARY: Oh, my, how charming! How about boards, does he function on boards?

SANCHO: You name them, he is on them. Parole boards, draft boards, school boards, taco quality control boards . . .

SECRETARY: Does he function in politics?

SANCHO: Señorita, you are looking at a political machine. Have you ever heard of the WAR ON POVERTY? That’s our model! Not only that, he makes political speeches.

SECRETARY: May I hear one?

SANCHO: With pleasure. (Snap.) Eric, give us a speech.

MEXICAN-AMERICAN: Mr. Congressman, Mr. Chairman, members of the board, honored guests, ladies and gentlemen. (SANCHO and SECRETARY applaud.) Please, please. I come before you as a Mexican-American to tell you about the problems of the Mexican. The problems of the Mexican stem from one thing and one thing only: he’s stupid. He’s uneducated. He needs to stay in school. He needs to be ambitious, foward-looking, harder-working. He needs to think American, American, American! God bless America! God bless America! God bless America! (He goes out of control. SANCHO snaps frantically and the MEXICAN-AMERICAN finally slumps forward, bending at the waist.)

SECRETARY: Oh my, he’s patriotic too! What about upkeep? Is he economical?

SANCHO: Well, no, I won’t lie to you. The Mexican-American costs a little bit more, but you get what you pay for. He’s worth every extra cent. You can keep him running on dry Martinis, Langendorf bread …

SECRETARY: Apple pie?

SANCHO: Only Mom’s. Of course, he’s also programmed to eat Mexican food at ceremonial functions, but I must warn you, an overdose of beans will plug up his exhaust.

SECRETARY: How much do you want for him?

SANCHO: Well, I tell you what I’m gonna do. Today and today only, because you’ve been so sweet, I’m gonna let you drive him off the lot for $15,000.

SECRETARY: Fifteen thousand dollars? For a Mexican!!!!

SANCHO: Mexican? What are you talking about? This is a Mexican-American! You want quality, but you gotta pay for it! This is no cheap run-about. He’s got class!

SECRETARY: Okay, I’ll take him. (Hands Sancho the $$ in cash) The Governor is having a luncheon this afternoon, and we need a brown face in the crowd. How do I drive him?

SANCHO: Just snap your fingers. He’ll do anything you want. (SECRETARY snaps. MEXICAN- AMERICAN steps forward.)

MEXICAN-AMERICAN: ¡Raza querida, vamos levantando armas para liberarnos de estos desgraciados gabachos que nos explotan! (Secretary snaps and model freezes)

SECRETARY: What did he say?

SANCHO: Something about taking up arms, killing people, etc.

SECRETARY: He’s not supposed to say that!

SANCHO: Look, lady, don’t blame me for bugs from the factory. He’s your Mexican-American, you bought him, now drive him off the lot! Try snapping another finger. (SECRETARY snaps. MEXICAN-AMERICAN comes to life again.)

MEXICAN-AMERICAN: ¡Basta! ¡Basta! ¡Viva la raza! ¡Viva la causa! ¡Viva la huelga! ¡Chicano power! (The MEXICAN-AMERICAN turns toward the SECRETARY, who gasps, backs up and runs out of the shop screaming. All freeze. After a few seconds of silence, the JOHNNY PACHUCO moves and stretches. SANCHO stays frozen to his spot.)

JOHNNY: Man, that was a long one, ese. (Others agree with him.)

FARMWORKER: (moves and stretches) How did we do?

JOHNNY: Pretty good, look at all that lana, man! (He goes over to SANCHO and removes the money from his hand. SANCHO stays where he is.) We keep this up, we’re going to be rich.

FARMWORKER: They think we’re machines.

REVOLUCIONARIO: (moves and stretches) Burros.

JOHNNY: Puppets.

MEXICAN-AMERICAN: The only thing I don’t like is how come I always get to play the Mexican- American?

JOHNNY: That’s what you get for finishing high school.

FARMWORKER: How about our wages, ese?

JOHNNY: $3,000 for you, $3,000 for you, $3,000 for you and $3,000 for me. The rest we put back into the business. (Notices Sancho, still frozen) What about our salesman? I think he needs an oil job.

REVOLUCIONARIO: Leave him to me. (REVOLUCIONARIO goes over to SANCHO, removes his hat, lifts him up and throws him over his shoulder. SANCHO hangs loose, lifeless. To audience.) He’s the best model we got! ¡Ajúa!
```

---

## IC-1388: The Lunatic’s Tale

- Title: The Lunatic’s Tale
- Author (byline): Woody Allen
- Work: Side Effects
- Publisher: Ballantine Books
- Publication date as stated: Sept 1986
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: DR. FARKIS
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
DR. FARKIS: Madness is a relative state. Who can say which of us is truly insane? And while I roam through Central Park wearing moth-eaten clothes and a surgical mask, screaming revolutionary slogans and laughing hysterically, I wonder even now if what I did was really so irrational. For, I was not always what is popularly referred to as "a New York street crazy," pausing at trash cans to fill my shopping bags with bits of string and bottle caps. No, I was once a highly successful doctor living on the upper East Side, gadding about town in a brown Mercedes, and bedecked dashingly in a varied array of Ralph Lauren tweeds. Hard to believe that I, Dr. Ossip Farkis, am now sometimes seen roller skating unshaven down Broadway wearing a knapsack and a pinwheel hat.

DR. FARKIS: The dilemma that precipitated this catastrophic fall from grace was simply this. I was living with a woman, Olive Chomsky, whom I cared for very deeply and who had a winning and delightful personality and mind. But (and I curse Fate for this) she did not turn me on . . . sexually. Concurrently, I was sneaking crosstown nightly to rendezvous with a photographer's model called Tiffany Schmeederer. Undoubtedly, you have heard the expression, "a body that wouldn't quit," Well Tiffany's body would not only not quit, it wouldn't take five minutes off for a coffee break. Skin like satin, a leonine mane of chestnut hair, long willowy legs and a shape so curvaceous that to run one's hands over any portion of it was like a ride on the Cyclone. This not to say Olive was a slouch - Not at all. In fact she was a handsome woman - a charming and witty culture vulture and, crudely put, a mechanic in the sack. Perhaps it was the fact that when the light hit Olive at a certain angle she inexplicably resembled my Aunt Rifka. Not that Olive actually looked like my mother's sister. (Rifka had the appearance of a character in Yiddish folklore called the Golem) It was just that some vague similarity existed around the eyes, and then only if the shadows fell properly. Perhaps it was just that a face and body like Tiffany Schmeederer's comes along every few million years and usually heralds an ice age or the destruction of the world by fire. The point is, my needs required the best of two women.

It was Olive I met first. And this after an endless string of relationships wherein my partner invariably left something to be desired. My first wife was brilliant, but had no sense of humor. My second wife was beautiful, but lacked real passion. Sharon Pflug, whom I lived with for three months, was too hostile. Whitney Weisglass was too accommodating. Pippa Mondale, a cheerful divorcee, made the fatal mistake of defending candles shaped like Laurel and Hardy.

Well-meaning friends fixed me up with a relentless spate of blind dates, all unerringly from the pages of H.P. Lovecraft. Ads, answered out of desperation, in the New York Review of Books, proved equally futile as the "thirtyish poetess" was sixtyish, the "coed who enjoys Bach and Beowulf" looked like Grendel, and the "Bay Area bisexual" told me I didn't quite coincide with either of her desires. This is not to imply that now and again an apparent plum would not somehow emerge: a beautiful woman, sensual and wise with impressive credentials and winning ways. But, obeying some age old law, perhaps from the Old Testament or Egyptian Book of the Dead, she would reject me. And so it was that I was the most miserable of men. On the surface, apparently blessed with all the necessities for the good life. Underneath, desperately in search of a fulfilling love.

Nights of loneliness led me to ponder the esthetics of perfection. Is anything in nature actually "perfect"? Who am I to demand perfection? I, with my myriad faults, I made a list of my faults, but could not get past: 1) Sometimes forgets his hat.

Did anyone I know have a "meaningful relationship"? My parents stayed together 40 years, but that was out of spite. Greenglass, another doctor at the hospital, married a woman who looked like a Feta cheese "because she's kind." Iris Merman cheated with any man who was registered to vote in the tri-state area. Nobody's relationship could actually be called happy. Soon I began to have nightmares.

I dreamed I visited a singles bar where I was attacked by a gang of roving secretaries. My analyst counseled compromise. My rabbi said, "Settle, settle. What about a woman like Mrs. Blitzstein? She may not be a great beauty, but nobody is better at smuggling food and light firearms in and out of a ghetto." An actress I met, who assured me her real ambition was to be a waitress at a coffee house, seemed promising, but during one brief dinner her single response to everything I said was, "Oh, wow," Then one evening, in an effort to unwind after a particularly trying day at the hospital, I attended a Stravinsky concert alone. During intermission I met Olive Chomsky and my life changed.

Olive Chomsky, literate and wry, who quoted Eliot and played tennis and who never said, "Oh, wow," or wore anything marked Pucci or Gucci or listened to country and western music or dialogue radio. And incidentally, who was always willing at the drop of a hat to do the unspeakable and even initiate it. What joyful months spent with her till my sex drive (listed, I believe, in the Guinness Book of World Records) waned. Concerts, movies, dinners, weekends, endless wonderful discussions of everything from Pogo to Rig-Vheda. And never a gaffe from her lips. Insights only. Wit too! And of course the appropriate hostility toward all deserving targets: politicians, television, facelifts, the architecture of housing projects, men in leisure suits, film courses, and people who begin sentences with "basically."

Oh, curse the day that a wanton ray of light coaxed forth those ineffable facial lines bringing to mind Aunt Rifka's stolid visage. And curse the day also that at a loft party in Soho, an erotic archetype with the unlikely name of Tiffany Schmeederer adjusted the top of her plaid wool kneesock and said to me with a voice resembling that of a mouse in the animated cartoons, "What sign are you?" I felt compelled to oblige her with a brief discussion of astrology, a subject rivaling my intellectual interest with such heavy issues as ESP, alpha waves, and the ability of leprechauns to locate gold.

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

## IC-1389: Mario

- Title: Mario
- Author (byline): Simon Rich
- Work: Glory Days, Pgs 15-32
- Publisher: Little, Brown and Company
- Publication date as stated: July 2024
- Event as filed: Humorous Interpretation
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
VOICE OVER: 40 years ago, the Mushroom Kingdom was invaded by the Koopa, a tribe of turtles famous for their black magic. The peace-loving Mushroom People were turned into stones and bricks, and the Kingdom fell into ruin. The only one who could undo the magic spell was Princess Peach, daughter of the Mushroom King. Unfortunately, she was in the hands of Bowser, King of the Koopa! It was up to Mario to free Princess Peach. (chants Free Princess Peach, Free Princes Peach)

Wait . . . You don’t know who Mario is??? 2025 marks the 40th anniversary of the original Super Mario Brothers video game, but Mario isn’t just a video game character — he’s a global icon! He is so famous that even the Prime Minister of Japan dressed up as Mario for the closing ceremony of the 2016 Summer Olympics!

But I’ll give you the inside scoop. Mario’s exciting, "super-fun" life is hitting a very quiet, middle-age crisis. . . Decades of running, jumping, and smashing bricks with his head have taken a toll.

Mario by Simon Rich
```

### Performance text (classify this)

```text
MARIO: It’s-a me, Mario! I was-a working as a plumber in New York when I fell-a down a pipe and landed in the Mushroom Kingdom. Pretty soon, I was-a having all kinds of super-fun adventures, crushing Koopas, dodging hammers, and jumping through castle after castle. It’s-a like my whole life was a game. I’d-a wake up each morning shouting, “Wahoo! Yiiiiippeee! Here we go!”*

MARIO: (Pg 15-32) I’m-a 40 years old. I wasn’t-a really thinking about it much. Just another birthday, right? Then it’s-a like the reality of the thing just hit me. “Mamma mia, I’m-a going to be middle-aged.”

Turning 40 forces you to take-a stock of how you’re doing. And to be honest, I’m-a not doing so great. I guess the best way to explain it is-a to start from the beginning of last week. Basically, I wake up, and it’s-a, like, I can’t-a move my back. Like, at all. So I go to Dr. Mario (no relation) and I’m-a in this tiny room for hours, doing all kinds of tests that I’ve-a never done before, and finally Dr. Mario comes back holding some X-rays, and he says that between the jumping and the running and the smashing the bricks with my head, I’ve-a basically given myself arthritis. And he says, “We need-a to schedule the surgery, Mario. The one we’ve been-a talking about. To fuse-a your spine. Recovery’s-a going to be brutal, but the alternative is you could-a end up in a wheelchair. You could lose-a your ability to walk.”

And he gives me his card and writes his cell phone number on it, and I’m-a thinking, “Mamma mia, it must be serious if he’s-a giving me his private line.” And I walk out of his office. I check-a my phone and there’s-a, like, 20 missed calls from the Princess. (heavy sigh) I call her back and she starts-a going off on me for being out of touch all day, and I’m about to hang up when she tells me she’s-a been kidnapped by a Koopa.

(rolls his eyes)

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

MARIO: (reading aloud) Dear prospective employer, I am writing to apply for the position of plumber at your company. Plumbing is a lifelong passion of mine. After beginning my career in New York City, I took a multi-year hiatus to the Mushroom Kingdom in order to improve my knowledge of pipes. Now I am ready to jump back in the game. Sincerely, Mario

All my adventures, the entirety of my adult life, boils down to a “hiatus”? (to Luigi) Listen, I really appreciate all this great advice, but today the main thing is, I need-a to borrow some money, so I can buy this spine belt and save the Princess from the Koopa.

LUIGI: (long silence, then removes his hat and launches into a rehearsed speech) Mario, we want to help you, but we don’t-a think we’ve-a been helping you in the right way. And that’s-a why, for your sake and ours, we have-a decided to put up some financial boundaries.

MARIO: And as I’m-a hobbling out of their dumb gate, I start to think about my relationship with the Princess. Did I really want to be with her? Or was her love just a [way] to prove-a to myself that I had worth -- That, despite my immigrant background, I was-a still deserving of love? I’d-a been with the Princess for decades, but it’s not like we’d-a ever actually connected. I barely even saw her, except for a few seconds after each rescue, and even then, it’s-a not like we had deep conversations—we just stood next to each other, staring straight ahead, while some text scrolled anticlimactically over our heads, followed by Japanese names.

I pull out Dr. Mario’s card, and call-a his personal number. (on phone) “It’s-a me, Mario. I need help.” (to audience) And within thirty minutes I’m-a in his office signing consent forms for “anterior lumbar interbody fusion.”

DR. MARIO: You’re going to need someone to wash your body and help-a you use-a the bathroom. For the first 12 weeks of recovery you’re-a going to have zero mobility. Do you-a have a partner who can help you?

MARIO: And by now the Princess has straight-up blocked my number. I guess she did end up calling Devon, because she’s-a posting all these pictures on social media, tagged, like, #realhero and #waybetterthanmario. And Dr. Mario, he’s-a walking me through the different options when Luigi jumps through the window. It turns out someone from Dr. Mario’s office called them, because they were-a listed as my emergency contacts.

LUIGI: We knew how much physical pain you were-a in, but we had no idea you were suffering so much emotionally. We love you, and we’re-a with you for the long haul, no matter what it takes.

MARIO: And I’m-a looking up at these guys, because I’ve-a been playing the game for 40 years, but this is the first time that it’s-a me who’s being rescued. (wipes a tear, beat)

Now it’s-a the night before the surgery, and it’s-a gonna be a long time before I can jump or even walk. And the truth is, I’m-a never going to be “Super Mario” again. I’m-a going to just be plain regular Mario, a middle-aged guy with a slight limp.

But maybe getting older’s not all bad. My whole life I’ve-a struggled with body stuff, like my weight and how I look-a naked. It’s-a why I wear the overalls even when it makes no sense for what I’m doing. Like, why can’t a short fat guy be sexy? (does some sexy moves) I feel-a sexy, and I’m not afraid to say I feel-a sexy. Deal-a with it. (becomes self-conscious and returns to his narrative)

I’m-a ready for the challenge. Like, I really want to do a podcast. We even came up with a name for it (The Next Level with Mario). And Luigi’s going to read-a the commercials, and Kwame’s-a going to be my first guest. (long beat as he reflects) These past 40 years, I’ve-a had all kinds of ups and downs. I’ve-a won and lost, flown and fallen, jumped and been jumped on. I’m-a covered in scars and soon I’ll have some more. But I’m-a not scared. I’m-a ready. Someday, I’ll-a run out of continues, but in the meantime I’ve got plenty of lives left.

Here we go . . .
```

---

## IC-1390: Matching Wits with Inspector Ford

- Title: Matching Wits with Inspector Ford
- Author (byline): Woody Allen
- Work: The Insanity Defense
- Publisher: Ballantine Books
- Publication date as stated: 2007
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1717
- Already set (do not supply): none

### Source block (context only)

```text
Author: Woody Allen
Book: The Insanity Defense
ISBN: 978-0345336972
Publisher: Ballantine Books
Date (Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
Murder mysteries have a wonderful way of involving the audience in the plot, allowing the viewers to play detective alongside Sherlock Holmes or Encyclopedia Brown. Murder mysteries are therefore an excellent brain teaser…if you can figure them out. In most cases the deductive reasoning involved in solving these cases isn’t too difficult. But the audience will have to learn a new type of problem solving in “Matching Wits with Inspector Ford” by Woody Allen
```

### Performance text (classify this)

```text
The Case of the Murdered Socialite Inspector. Ford burst into the study. On the floor was the body of Clifford Wheel, who apparently had been struck from behind with a croquet mallet. The position of the body indicated that the victim had been surprised in the act of singing "Sorrento" to his goldfish. Evidence showed there had been a terrible struggle that had twice been interrupted by phone calls, one a wrong number and one asking if the victim was interested in dance lessons. Before Wheel had died, he had dipped his finger into the inkwell and scrawled out a message: "Fall Sale Prices Drastically Reduced-Everything Must Go!" "A businessman to the end," mused Ives, his manservant, whose elevator shoes, curiously enough, made him two inches shorter. The door to the terrace was open and footprints led from there, down the hall, and into a drawer. "Where were you when it happened, Ives?" "In the kitchen. Doing the dishes." Ives produced some suds from his wallet to corroborate his story. "Did you hear anything?"

"He was in there with some men. They were arguing over who was tallest. I thought I heard Mr. Wheel start yodeling and Mosley, his business partner, began yelling, 'My God, I'm going bald!' Next thing I knew, there was a harp glissando and Mr. Wheel's head came rolling out onto the lawn. I heard Mr. Mosley threaten him. He said if Mr. Wheel touched his grapefruit again, he would not cosign a bank loan for him. I think he killed him." "Does the terrace door open from the inside or from the outside?" Inspector Ford asked Ives. "From the outside. Why?" "Exactly as I suspected. I now realize it was you, not Mosley, who killed Clifford Wheel." HOW DID INSPECTOR FORD KNOW? Because of the layout of the house, Ives could not have sneaked up behind his employer. He would have had to sneak up in front of him, at which time Mr. Wheel would have stopped singing "Sorrento" and used the mallet on Ives, a ritual they had gone through many times. A Curious Riddle Apparently, Walker was a suicide. Overdose of sleeping pills. Still, something seemed amiss to Inspector Ford. Perhaps it was the position of the body. Inside the TV set, looking out. On the floor was a cryptic suicide note. "Dear Edna, My woolen suit itches me, and so I have decided to take my own life. See that our son finishes all his push-ups. I leave you my entire fortune, with the exception of my porkpie hat, which I hereby donate to the planetarium. Please don't feel sorry for me, as I enjoy being dead and much prefer it to paying rent. Goodbye, Henry. P.S.

This may not be the time to bring it up, but I have every reason to believe that your brother is dating a Cornish hen." Edna Walker bit her lower lip nervously. "What do you make of it, Inspector?" Inspector Ford looked at the bottle of sleeping pills on the night table. "How long had your husband been an insomniac?" "For years. It was psychological. He was afraid that if he closed his eyes, the city would paint a white line down him." "I see. Did he have any enemies?" "Not really. Except for some gypsies who ran a tearoom on the outskirts of town. He insulted them once by putting on a pair of earmuffs and hopping up and down in place on their Sabbath." Inspector Ford noticed a half-finished glass of milk on the desk. It was still warm. "Mrs. Walker, is your son away at college?" "I'm afraid not. He was expelled last week for immoral conduct. It came as quite a surprise. They caught him trying to immerse a dwarf in tartar sauce. That's one thing they won't tolerate at an Ivy League school." "And one thing I won't tolerate is murder. Your son is under arrest." WHY DID INSPECTOR FORD SUSPECT WALKER'S SON HAD KILLED HIM? Mr. Walker's body was found with cash in his pockets. A man who was going to commit suicide would be sure to take a credit card and sign for everything. The Stolen Gem The glass case was shattered and the Bellini Sapphire was missing. The only clues left behind at the museum were a blond hair and a dozen fingerprints, all pinkies.

The guard explained that he had been standing there when a black-clad figure crept up behind him and struck him over the head with some notes for a speech. Just before losing consciousness, he thought he had heard a man's voice say, "Jerry, call your mother," but he could not be sure. Apparently, the thief had entered through the skylight and walked down the wall with suction shoes, like a human fly. The museum guards always kept an enormous fly swatter for just such occasions, but this time they had been fooled. "Why would anyone want the Bellini Sapphire?" the museum curator asked. "Don't they know it's cursed?" "What's this about a curse?" Inspector Ford was quick to ask. "The sapphire was originally owned by a sultan who died under mysterious circumstances when a hand reached out of a bowl of soup he was eating and strangled him. The next owner was an English lord who was found one day by his wife growing upside down in a window box. Nothing was heard of the stone for a while; then it turned up years later in the possession of a Texas millionaire, who was brushing his teeth when he suddenly caught fire. We purchased the sapphire only last month, but the curse seemed to be working still, because shortly after we obtained it, the entire board of trustees at the museum formed a conga line and danced off a cliff." "Well," Inspector Ford said, "it may be an unlucky jewel, but it's valuable, and if you want it back, go to Handleman's Delicatessen and arrest Leonard Handleman. You'll find that the sapphire is in his pocket." HOW DID INSPECTOR FORD KNOW WHO THE JEWEL THIEF WAS? The previous day, Leonard Handleman had remarked, "Boy, if I only had a large sapphire, I could get out of the delicatessen business." The Macabre Accident "I just shot my husband," wept Cynthia Freem as she stood over the body of the burly man in the snow. "How did it happen?" asked Inspector Ford, getting right to the point. "We were hunting. Quincy loved to hunt, as did I. We got separated momentarily. The bushes were overgrown. I guess I thought he was a woodchuck. I blasted away. It was too late. As I was removing his pelt, I realized we were married." "Hmm," mused Inspector Ford, glancing at the footprints in the snow. "You must be a very good shot. You managed to plug him right between the eyebrows." "Oh, no, it was lucky. I'm really quite an amateur at that sort of thing." "I see." Inspector Ford examined the dead man's possessions. In his pocket there was some string, also an apple from 1904 and instructions on what to do if you wake up next to an Armenian. "Mrs. Freem, was this your husband's first hunting accident?" "His first fatal one, yes. Although once in the Canadian Rockies, an eagle carried off his birth certificate." "Did your husband always wear a toupee?" "Not really. He would usually carry it with him and produce it if challenged in an argument. Why?" "He sounds eccentric." "He was." "Is that why you killed him?" HOW DID INSPECTOR FORD KNOW IT WAS NO ACCIDENT? An experienced hunter like Quincy Freem would never have stalked deer in his underwear. Actually, Mrs. Freem had bludgeoned him to death at home while he was playing the spoons and had tried to make it look like a hunting accident by dragging his body to the woods and leaving a copy of Field & Stream nearby. In her haste, she had forgotten to dress him. Why he had been playing the spoons in his underwear remains a mystery. The Bizarre Kidnapping Half-starved, Kermit Kroll staggered into the living room of his parents' home, where they waited anxiously with Inspector Ford. "Thanks for paying the ransom, folks," Kermit said. "I never thought I'd get out of there alive." "Tell me about it," the inspector said. "I was on my way downtown to have my hat blocked when a sedan pulled up and two men asked me if I wanted to see a horse that could recite the Gettysburg Address. I said sure and got in. Next thing, I'm chloroformed and wake up somewhere tied to a chair and blindfolded." Inspector Ford examined the ransom note. "Dear Mom and Dad, Leave $50,000 in a bag under the bridge on Decatur Street. If there is no bridge on Decatur Street, please build one. I am being treated well, given shelter and good food, although last night the clams casino were overcooked. Send the money quickly, because if they don't hear from you within several days, the man who now makes up my bed will strangle me. Yours, Kermit. P.S. This is no joke. I am enclosing a joke so you will be able to tell the difference." "Do you have any idea at all as to where you were being held?" "No, I just kept hearing an odd noise outside the window."

"Odd?" "Yes. You know the sound a herring makes when you lie to it?" "Hmm," reflected Inspector Ford. “And how did you finally escape?" "I told them I wanted to go to the football game but I only had a single ticket. They said O.K., as long as I kept the blindfold on and promised to return by midnight. I complied, but during the third quarter, the Bears had a big lead, so I left and made my way back here." "Very interesting," Inspector Ford said. "Now I know this kidnapping was a put-up job. I believe you're in on it and are splitting the money." HOW DID INSPECTOR FORD KNOW? Although Kermit Kroll did still live with his parents, they were eighty and he was sixty. Actual kidnappers would never abduct a sixty-year-old child, as it makes no sense.
```

---

## IC-1391: Mid-Life Crisis of Dionysus

- Title: Mid-Life Crisis of Dionysus
- Author (byline): Garrison Keillor
- Work: The Best American Short Plays, 1993-1994, Pgs 87-102
- Publisher: Penguin Publishers
- Publication date as stated: 1995
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: DIONYSUS, ARIADNE, GLADYS, NYMPH, GUY
- Teaser before the introduction: No
- Spoken words (computed): 1945
- Already set (do not supply): none

### Source block (context only)

```text
Author: Garrison Keillor
Book: The Best American Short Plays, 1993-1994, Pgs 87-102
ISBN: 978-1557831996
Publisher: Penguin Publishers
Date (Month/Year): 1995
```

### Introduction (context only: never use it for content warnings)

```text
Dionysus, the god of wine and of orgies, the bastard son of Zeus and Semele. Dionysus the god of great parties- to his complete surprise one sunny afternoon suddenly became fifty years of age. He was reclining in his temple on Mount Cithaeron in Boeotia, enjoying a very fine 1925 B.C. Pinot Noir . . . when . . . it hit. . .

The Midlife Crisis of Dionysus by Garrison Keillor
```

### Performance text (classify this)

```text
DIONYSUS: (Pgs 87-102) That orgy tonight- I donno. I've laid in six gallons of extra virgin cold-pressed olive oil. You think that's too much or not enough? We'll have about fourteen nymphs and six satyrs and maybe a couple other gods, and some Macedonian guys

ARIADNE: Dionysus thought about this, and then he heard the sound of the sensible shoes of the Muse of Maturity, Gladys, coming up the steps and into his temple. [GLADYS enters]

GLADYS: Okay. Gramps, put down the beverage. I got news for you. You're fifty.

DIONYSUS: Fi-fi-fi-fi-fi-fi

GLADYS: That's right. Say it. Fifty.

DIONYSUS: Wait a minute. I'm immortal! Ageless! You can lookit up in any mythology!

GLADYS: Everybody gets just so much immortality and then it's time to grow up. You were young for thousands of years, like everybody else, and now you're fifty. What's the problem?

DIONYSUS: How can I be fifty? I'm Dionysus, the god of revels, the patron of satyrs, nymphs, Amazons, bull-roarers, madwomen in mink coats, I'm not just a wine kind of guy, I'm the guy who invented wine- I'm the god of wine, hey? I'm not ready to be fifty. I want more. Where'd she go? I'm not ready to be a geezer. I want more oysters! More wine in the wineskins! More women! Young women- slender- -long-legged. I'm not ready to sit in a sunny corner with a knitted comforter on my lap and chuckle. I want to get into trouble.

GLADYS: I got two words for you, mister. And that's grow up. Okay? Grow up. Happy birthday. [GLADYS turns to stand alongside ARIADNE]

ARIADNE: Dionysus decided to forget everything she said, and he got himself ready for the orgy that night.

GLADYS: He sat naked in the steambath, and his hands looked old, mottled, with big ropy veins, the skin wrinkly and rough, like a lizard's. DIONYSUS rises from the chair, dismayed.

ARIADNE:He looked into a pool and saw his reflection. Big tufts of hair poked from his ears, and his jawline looked very poorly defined - his chin seemed not so much to thrust forward as to be part of his neck. His neck looked poochy. His chest seemed to have descended about five inches.

DIONYSUS: Who did this to me?

NYMPH: Hey. You don't look that bad for fifty. Your back looks youthful. Sort of.

DIONYSUS: [groans and turns, agonized] Get out of here. [The NYMPH exits, grunting. DIONYSUS faces the audience and turns an invisible key in the ignition, makes a starter sound, and steers the invisible wheel]

ARIADNE: So Dionysus drove home to the suburbs of Boeotia, listening to oldies on the radio, and thinking about the terrible fate that had befallen him. When he got home, I was there waiting for him. I'm his wife. [To DIONYSUS] Hi, honey. You tired? You look beat.

DIONYSUS: Somebody else told me that too.

ARIADNE: I fixed you some poached grouper for supper, and a papyrus salad. High in fiber, honey. Time you started thinking about that sort of thing.

DIONYSUS: Oh.

ARIADNE: We need to talk about your drinking, Dionysus. You're drinking way too much. I want you to stop. Give it up. Please. For me and for the kids but most of all for yourself.

DIONYSUS: Look, I'm Dionysus. Okay? I'm the god of wine, okay? I'm not the god of iced tea, babes. [agitated, he paces]

ARIADNE: I knew you were going to say that.

DIONYSUS: I am the god of revelry, and revelry is no idle thing, it is a crucial element of the whole fertility process. The dancing and the whirling and the drinking and the shouting and the ecstatic singing and whooping- that's what makes the wheat grow, babes.

ARIADNE: I'm concerned about your health, Dionysus. I read an article that said most people drink to build up self-confidence and compensate for low self-esteem. Maybe you need to see someone.

DIONYSUS: I have no lack of self-esteem! I'm a god!

ARIADNE: Are you? You're fifty, Dionysus. To me, fifty means mortal.

DIONYSUS: C'mon. I'm the same beautiful guy with the same flowing locks, as when you married me. Look. [takes a lock of his hair and stares at it, cross-eyed, disappointed]

ARIADNE: Drinking all that wine is hard on your hair, honey. And it causes loss of memory. And it makes you flatulent. [He turns away – a loud fart. He jumps slightly]

ARIADNE: I love you, Dionysus. Go see a doctor. Please. [exits]

GUY: [enters, wearing a stethoscope and white jacket] Say Ah. [pokes a thermometer in Dionysus’ mouth]

DIONYSUS: Ahhhhhhhh-rghhhhhhhhhhhh!

GUY: [raps on his chest, listens with the stethoscope, looks in both ears, takes out thermometer and reads it] Okay. Not bad. Not bad. Your prostate's a little enlarged but you should be able to get a few more years out of it. Brain function seems fairly sound, considering. You're no gem, but you're in good shape. I'd say you ought to live well into your senility and beyond. [GUY exits. DIONYSUS turns his back to audience]

GLADYS: [enters and addresses the audience] Dionysus did not slept well that night. He dreamed terrible dreams about his mother, and he awakened four or five times to go downstairs and urinate. The next morning, he drove to the airport to fly to Mount Olympus to discuss the mortality problem with Zeus, his father, and to his great surprise, he got bumped off the first flight and put on stand-by. [exits]

DIONYSUS: What's going on here? I'm a god. I'm supposed to get the automatic upgrade, go right into first class.

NYMPH: Sorry, sir. First class is full [and] your deity card has expired. Expired yesterday.

DIONYSUS: Gods don't expire. It's an eternal thing.

NYMPH: I'm sorry, but this card is going to have to be renewed before we can upgrade you. I'll get you on the 4: 15 if I can.

DIONYSUS: Please. [turns away, pacing in frustration]

NYMPH: [comes downstage and addresses the audience ]Dionysus got on the 4: 15 flight, in tourist, a middle seat, between a man possessed of demons and a leper- it was the best we could do-- and when he finally arrived at Olympus, Zeus kept him waiting another hour. [GUY enters, wearing a crown, robe, golden slippers, and carrying a scepter]

DIONYSUS: Hi, Dad. Good to see you!

GUY: Son, I've decided to make a change. Latromis is going to become the god of wine, and you're going to be the chairman of wine. He'll do the revels and orgies and lie around with the nubile young women and you can organize wine programs, go to wine meetings. Maximize wine. And by the way, congratulations on turning fifty. I meant to send a card, but anyway, your birthday present is in there. [waves toward the wings. DIONYSUS exits and returns with a handful of ordinary things]

DIONYSUS: A sack of apples, and a pound of cheese? And what's this?

GUY: It's a souvenir photograph of me – autographed!

DIONYSUS: Dad? Why am I fifty? Why did my deity card expire? I thought I was going to be a god forever.

GUY: What? You? Fifty? Gosh. You don't look that old. Listen. I'll look into it. I'll get back to you. Okay? Great. Happy birthday. Bye. [GUY exits]

NYMPH: [to the audience] So, Dionysus went up to Mount Aesculapius where Theros, the muse of caring, ran a treatment program for gods.

GLADYS: [enters, wearing a clinical jacket] Lie down on the couch, Dionysus. Why don't we start from the beginning. Tell me about your parents.

DIONYSUS: You know about my parents. It's a famous story. My dad was Zeus, the Father of Heaven, the Head God, and he was fooling around with mortal women, and he fell in love with my Mom and then his wife Hera got jealous and- you know

GLADYS: So Hera came to your mom in disguise and said, "Hey, congratulations, but if you want a really good time, tell him to bring his thunderbolts, it's a real charge.” And while they were engaged in passionate embrace, she caught on fire, right?

DIONYSUS: Right. Exactly.

GLADYS: And your dad snatched you up from the ashes of her burning body and he sewed you up in his thigh and you spent most of your prenatal period there, in Zeus's left leg. After you were born, your mom's sister Ino tried to protect you, but Hera, your dad's wife, was still consumed with jealousy. She had you torn into shreds and boiled in a steaming cauldron.

DIONYSUS: Yes.

GLADYS: And you were rescued by your grandma, who put you back together, but you never forgot what happened, did you, Dionysus? You've never really come to terms with it, have you.

DIONYSUS: With being torn to shreds and boiled? No, I guess I haven't.

GLADYS: Maybe that's why you invented wine. Maybe it was an escape from the terrible disapproval of your wicked stepmother . . . How old are you?

DIONYSUS: I'm a god. I'm immortal.

GLADYS: I see. How long have you considered yourself a god?

DIONYSUS: Oh shut up. Would you? Just shut your mouth. You're dumber than dirt I don't "consider" myself a god. I am a god!

GLADYS: I'd like to talk about your anger right now.

DIONYSUS: I'm not angry, You are. I'm actually having a very good life. Wine and love and laughter and a certain measure of tasteless excess and sensual adventure- I've got a darned good life. Life is a celebration. And I'm one of the celebrants.

GLADYS: Oh, that's priceless. That really is. [writes in her notebook] You're the god of cliche.

DIONYSUS: Life is a celebration. Before we can create anything, we need to enjoy who we are now. Before you can get to tomorrow, you have to enjoy today. A person's most fundamental obligation in life is to enjoy it.

GLADYS: [writing rapidly] Not so fast, I want to get this down.

DIONYSUS: The great killer isn't foolishness, it's sullen lethargy and depression, that's what kills off the corn crop; but if you can bring yourself to sing, have a little wine, fix a nice dinner, tell some jokes, have a good time, spend some of your treasure on happiness, it makes the fields fertile, and we make more beer and whiskey, and life goes spinning on. [DIONYSUS exits]

GLADYS: [to audience] Dionysus did not bother to renew his deity card. He waited for Zeus to do something about it. Months and months passed and there was no word from the Father of Heaven and finally Dionysus just forgot about the whole thing. He just went on being whatever he was.

NYMPH: (to audience) His hair improved slightly, when he switched to a milder shampoo. He switched to a new brand of breakfast cereal. He bought a Nautilus machine.

ARIADNE: (to audience) He cut down on the wine and he learned to enjoy the ordinary. He learned how to take a deep breath, look at the woods, and think his own long thoughts.

GUY: (to audience) But he missed those wild orgies, those young women, the dancing, the love-making. As the chairman of wine, he'd fly off to conferences on "Meeting the Vine Needs of the Nineties" and give a long boring speech on "Maximizing the Total Wine Experience," a real stink bomb, and it only made him remember how much fun those orgies had been. He used to spend time with nymphs and satyrs, singing dirty songs and chasing virgins through the tall grass, and now he spent time with people who sat and bored the shoes right off you, complaining about traffic congestion. He thought about a swimming pool surrounded by green grass in a forest- he had swum naked there at midnight surrounded by happy women who wanted to press their skin against his.

ARIADNE: What you're thinking.

DIONYSUS: I was thinking that I've lived for thousands and thousands of years, and it's only now, since I turned fifty, that I start to get the hang of it.
```

---

## IC-1392: The Most Fabulous Story Ever Told

- Title: The Most Fabulous Story Ever Told
- Author (byline): Paul Rudnick
- Work: Not specified
- Publisher: Overlook Press CO State Qualifier
- Publication date as stated: July 2000 MN State Qualifier
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ADAM, STEVE, VIRGIN MARY, CHERYL, RABBI SHARON
- Teaser before the introduction: Yes
- Spoken words (computed): 1479
- Already set (do not supply): none

### Source block (context only)

```text
2009 National Qualifier
Author: Paul Rudnick 2010 National Qualifier
ISBN: 978-1585670529 2019 National Qualifier
Publisher: Overlook Press CO State Qualifier
Date (Month/Year): July 2000 MN State Qualifier
```

### Introduction (context only: never use it for content warnings)

```text
And that’s all the Steve knows – it’s a party to celebrate Christmas and life. But the party turns out to be much, much more. The Most Fabulous Story Ever Told by Paul Rudnick
```

### Performance text (classify this)

```text
A Christmas Celebration (and unbeknownst to Steve, a wedding). Food has been set out, along with plates, utensils, and napkins. STEVE enters carrying a punch bowl and humming a Christmas song. We hear a key in the front door, and ADAM enters. He is the ebullient Christmas fan and is bursting with excitement.

ADAM: (Pg 91-92) Wait, just wait! One second! I saw it, we need it, you'll love it! (he runs back outside and returns, carrying a nearly life-size plastic reindeer with a bright red nose)

STEVE: We don't have any more room!

ADAM: But we can't have a party without Rudolph! I was passing by Kmart, and it was the only one left; I had to wrestle it away from this woman with two screaming children! Oh, and I also got. . . (he runs back outside)

STEVE: No! You may not bring one more piece of holiday *crap* into this house!

ADAM: (returns, carrying a large, molded plastic statue of the Virgin Mary) But this is so special, this is actually sacred . . . (he places the statue on the table) It's the Virgin Mary. Only -- she speaks. (he presses a button at the base of the statue, and a perky recorded voice is heard, coming from inside the statue.

VIRGIN MARY: Merry Christmasl

ADAM: It's a miracle. A modem miracle.

STEVE: Does she say anything else?

ADAM: I think she got the same tape as Barbie. (he presses the button again)

VIRGIN MARY: Math is hard. (Steve laughs)

ADAM: (Pg 93) (gesturing to the room) All of this -- is for you. I want to make every day of your life a Christmas party, from now on.

STEVE: Adam, I don't need parties. . .

ADAM: I do. Because I have something to celebrate -- your life.

STEVE: (Pg 93-94) Okay, how did it go? Tell me. I want to hear it. I mean it.

ADAM: Okay! It was -- incredible. It was, if I do say so myself, the most fantastic, deconstructed, trans-holiday pageant in the history of the elite Preston School first grade. Because I am not just a teacher, oh no. I am a post-modem, multi-cultural genius.

STEVE: "Trans-holiday pageant"?

ADAM: Well, I wanted to be inclusive because it's the right thing to, and because the school is on the Upper West Side and the children's parents are all ultra-liberal. So, I did the entire Nativity, the Wise Men, the shepherds, even the camels, only everyone in it-was gay.

STEVE: You're kidding.

ADAM: The kids loved it. The parents loved it. This one little boy, who played Jesus, he ran over to his mother, he was just beaming. And he said, "Mommy, I'm gay!" She was thrilled. She hugged him and turned to her husband and said, "Darling, this means Yale!"

STEVE: But -- the Bible isn't gay.

ADAM: (triumphantly) It is now! (A knock at the door and Adam answers) Cheryl enters. CHERYL is a fresh-faced young woman from Utah. She is extremely perky and outgoing, and thrilled to be invited to Adam and Steve’s Christmas party (Wedding). As she enters, she is dazzled and awestruck by the loft's Christmas decor.

CHERYL: (Pg 96) It's gorgeous!

ADAM: (thrilled) Isn't it? Steve, this is Cheryl Mindle, my new teaching assistant from school. She just started. Cheryl's not going home for Christmas, so I asked her to come and help with the party.

CHERYL: (Pg 97-98) Misty Bluffs. That's where I'm from, in Utah.

STEVE: Are you -- a Mormon? (whispers) Are you aware that -- we're gay?

CHERYL: (totally sympathetic and chipper) Of course! And I am not judging you, uh-uh! Adam is a great guy, and I know that you've been together forever, I mean, way longer than most normal couples. And I know that some good Christians, like my Mom, think that gay people are sick and godless, hut I said, no, Mom, they are sensitive and artistic! (She gestures with both arms to all the Christmas decor as sincere proof of gay people's artistic glory)

STEVE: You go, girl! (CHERYL whoops in agreement and gives a fervently physical, if awkward, two snaps up.)

CHERYL: Do you know what you need? Angels. They're real, and they're everywhere, watching over us. Back home, I have fifteen different hand-painted ceramic angels, three stuffed angels, an angel poster, an angel T-shirt, oh, and two pairs of angel pajamas!

STEVE: Cheryl, are you -- seeing someone?

CHERYL: You mean, like a boyfriend?

STEVE: (after a beat) No.

ADAM: Stop itl I bet there are angels in this room, right now! I can feel it! Tonight is gonna be magical!

STEVE: (Pg 100-101) Oh no, oh no, I'm having a problem, staying Christmasy.

ADAM: (to STEVE) You can do it! For the baby Jesus!

STEVE: But Adam -- you're Jewish!

ADAM: (Pg 113) But, I love Christmas, for the decor and the spirit! And I've been changing the Bible. I've been making the stories more gay-positive, and upbeat. (The doorbell buzzes)

CHERYL: (Pg 116-117) I'll get it. CHERYL wheels in RABBI SHARON in her wheelchair. SHARON is an aggressively confident, gung-ho woman, a cable TV diva with a mission. She relishes an audience, and a challenge; she's a star.

ADAM: (going to SHARON, offering his hand) Hello. Welcome. I'm Adam. And this is Steve.

RABBI SHARON: (to STEVE, totally upbeat) The guy with AIDS, am I right? Shalom! (very excited) So, does everyone watch my show? Let's hear it! I'm Rabbi Sharon, and welcome to . . .

CHERYL: (copying SHARON's signature arm gesture, in which she points in a wide, sweeping half-circle, and then points to heaven) "Who Believes" (excitedly) (Pg 119-121) Sharon? I believe. And I'm a Mormon!

RABBI SHARON: No, come on, really?

CHERYL: I am! And I think that God is just the best thing ever!

RABBI SHARON: And Steve. I've heard you're stubborn. You say show me. You say no.

STEVE: You heard right.

RABBI SHARON: Because God did you wrong. AIDS. The homeless. The Holocaust. (beat) I still believe, because otherwise I have nothing.

STEVE: You have common sense. You have reality.

RABBI SHARON: Come off it. You think about God more than anyone else in this room.

STEVE: No, I don't!

RABBI SHARON: (physically pursuing Steve, in her wheelchair; really going after him, picking a fight) And why not? God made you sick! And not your neighbor, not some fascist dictator, not some creep.

STEVE: It’s a virus!

RABBI SHARON: (Pg 122-124) And you know something? Sometimes God delivers. Like these new drugs, these cocktails, am I right? Are you on them?

STEVE: Twenty-eight pills a day. -- That is science.

ADAM: That's God! Steve, do you remember our Christmas party last year?

STEVE: We didn't have one.

ADAM: [Because] you'd spent two weeks in the hospital, at 125 pounds, hooked up to a torture chamber, coughing up blood. And I sat in that waiting room, and I cursed God. I said, no more desperate prayers, you get down here, you fix this! (beat) All right, Sharon, you're a person of God, right?

RABBI SHARON: With a Web site and a T-shirt!

ADAM: What does it say?

RABBI SHARON: "Oy Gay."

ADAM: So maybe I can ask you-my question. The one I've been trying to get brave enough and strong enough to ask. All right! Here goes. All year long, maybe all my life, things have been-building. To this morning. When I woke up and I looked at Steve, who was curled up, snoring, and-smiling. And I looked out the window and it was snowing, just gently, just that perfect MGM snow. And I got my coffee, and I realized that, at exactly that second -- I was. . . happy.

RABBI SHARON: Mazel tov!

ADAM: No! I ducked, I shivered, I was terrified! I thought, no, don't jinx it, don't call down a flood or a thunderbolt! And ever since then, I've been in this blind panic. So -- is it okay? To say it, to feel it? To be in love, to have a party, to be -- happy?

RABBI SHARON: You're Jewish, right? (with genuine compassion, very straightforward) Sweetheart, I talk to God, all the time. And you know something? God says yes. (beat) (Pg 117-118) All right, let's get goin’! I've got two basic weddings-with God and without. (Adam can’t contain his excitement. He bounces up and down claps and then goes to Steve and links arms with him; Steve is visibly uncomfortable; but Sharon continues unabashedly) With God is non-sectarian but focused on a higher power, with a pronoun of your choice. God can be He, She, Our Mother, Our Father, Our Lavender Light, The Goddess, The Creator, The King, or Our Lord. Without is more inner, it's the union of souls, the joining of two perfect beings, let our community bless this day, you get the picture . . . . So?

STEVE: (Pg 135) (to Adam) Really? (Steve runs off stage in tears) *****Scene – Cheryl and Rabbi Sharon have left and the festive atmosphere is gone ******

ADAM: (Pg 135-137) (after they are alone) Steve? (a long beat) They’ve stopped working, haven’t they? The pills. The new ones. I noticed, all of your bottles -- they're empty.

STEVE: (after a beat) Yup.

ADAM: Were you -- were you going to tell me?

STEVE: Look, they don't work for everyone, and no one's been on them that long, and the side effects are worse than the disease, the whole thing was a crapshoot, I mean, come on.

ADAM: How long have you known?

STEVE: I don't know, a week, what difference does it make?

ADAM: It makes a difference. I said all that bulls***! I said I was happy! I said it was possible! I said that the heavens were smiling down on everyone!

STEVE: What should I have done? Stood up and said, sorry folks, party's over! Especially for me!

ADAM: Yes! Because that's the truth! And I can handle that!

STEVE: You? And the truth? Adam-you have spent your entire life lunging for answers and miracles and your little kiddie pageant! You have devoted yourself to everything but the truth!

ADAM: But you're the one who's been lying!

STEVE: Fine! You want some facts? Hard-core? (very simply, straightforward, without histrionics) I'm dying. And this could very well be our last Christmas together. (long beat)

ADAM: (going to him Steve . . .

STEVE: No! Handle it!

ADAM: Okay. You’re right. You’re absolutely right. No more – questions. You are going to die. And I am going to watch you. You win. (long beat, then sadly) (Pg 138-139) I need . . . a story.

STEVE: Central Park?

ADAM: And the day we met.

STEVE: May third. Ages ago.

ADAM: Lunch time. The first really fabulous day – (he envisions the park as he walks around the room) And I thought, I love this park. And I love this city. And I love the air and the breeze and the lake. And I'm alone. And then I turned.

STEVE: (smiling) Hey . . . Merry Christmas.

2004 National Qualifier
```

---

## IC-1393: MOTB

- Title: MOTB
- Author (byline): Robert Fulghum
- Work: All I Really Need to Know I Learned in Kindergarten
- Publisher: Dramatic Publishing
- Publication date as stated: 1999
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ED
- Teaser before the introduction: Yes
- Spoken words (computed): 1153
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Fulghum
Book: All I Really Need to Know I Learned in Kindergarten
ISBN: 978-0871299130
Publisher: Dramatic Publishing
Date (Month/Year): 1999
```

### Introduction (context only: never use it for content warnings)

```text
Usually . . . . . [in the voice of a USED CAR SALESMAN} Congratulations! Your little girl is getting married. But being the mother of the bride (or MOTB) is not an easy role – not only is it a big job, but a job that has changed significantly over the years. Once upon a time mothers of the bride did most of the wedding planning, and thus got to have their own dreams realized. These days, your daughter will probably have her own vision – which may differ drastically with yours. But, hey . . . you don’t have to let that stop you! You can be the MOTB of your dreams or maybe the one in MOTB by Richard Fulghum.
```

### Performance text (classify this)

```text
ED: Most weddings are such comedies. (long pause) Not that they are intended as such. But since weddings are high state occasions involving amateurs under pressure, everything NEVER goes right.

(He takes one chair and places it DLC as a representations of MOTB. He never moves the chair again, and uses it to refer to her throughout the story.)

The central figure in this drama was the mother of the bride, the MOTB. Not the bride, groom, or minister. Mother. Usually a polite, reasonable, intelligent, and sane human being,

ED: [The] Mother [of this wedding] was mentally unhinged by the announcement of the daughter’s betrothal. I don’t mean she was unhappy, as is often the case. To the contrary. She was overcome with joy. And just about succeeded in overcoming everyone else in her joy.

Nobody knew it, but this lady had been writing with a script for a production that would have met with Cecil B. DeMille’s approval. A royal wedding fit for a princess bride. The father of the bride began to pray for an elopement.

She had seven months to work and no detail was left to chance or human error. (He gets three other chairs and sets them up during the following, suggesting pews for the two sides of the church. One in front is for the MOTB, the other is for the mother of the groom. The other two chairs suggest pews a little further back in the church. There is a center aisle.) Everything that could be engraved was engraved. There were teas and showers and dinners. And eight-piece brass-and-wind ensemble was engaged. The bride and groom met with the minister only three times----The MOTB was in his office more than the cleaning lady. Not only were the bridesmaid’s outfits made to order, but the tuxedos for the groom and his men were bought, not rented, mind you. Bought (he is finished setting up the church) And, if all that wasn’t enough, the engagement ring was returned to the jeweler for a larger stone—quietly subsidized by the MOTB. When I say the lady came unhinged, I mean UNHINGED. (piano cue:roll)

The judgment of fate rolled down the road, and the final hour came.

(Piano music: fanfare as Ed grabs the end of a white bridal runner, which as been preset D and unfurls it so that a church aisle is established from D to U. he places the U edge of the runner on the cut-off of the musical fanfare. Piano music underscores so much of the remainder of the story.)

Guests in formal attire packed the church. Enough candles were lit to bring daylight back to the evening. In the choir loft of the orchestra gushed great music. And the mighty MOTB coasted down the aisle with the grandeur of and opera diva at a premier performance. (After the line, he imitates the MOTB walking down the aisle, strutting, sneaking waves to her friends, etc., and finally taking her seat.) Never has the mother of the bride take her seat with more satisfaction. She had done it. She glowed, beamed, smiled, and sighed.

(He rises to narrate the following as he paints a vivid picture. He helps us see all of the action and characters against the backdrop of his church set.) The music softened, and nine---count them nine----chiffon-draped bridesmaids lock stepped down the long aisle, while the groom with his men marched into place.

Finally, the wedding march thundered from the orchestra. Here comes the bride! Preceded by four enthusiastic min-princesses chucking flower petals, and two munchkin ring bearers-----one for each ring.

The congregation rose and turned in anticipation.
“Ah the bride.”
She had been dressed for hours…if not days.
No adrenaline was left in her body.

(Putting the picture on hold, and stepping out of the world of the church, he takes the audience to the receptions hall and suggests the following) Left alone with her father in the reception hall of the church while the march of the maidens went on and on, she had walked along the table leaded with gourmet goodies and absentmindedly sampled first the little pink and yellow and green mints. Then she picked through the silver bowls of mixed nuts and ate the pecans. Followed by a cheeseball or two, some black olives, a handful of glazed almonds, a little sausage with a frilly toothpick stuck in it, a couple of shrimps blanketed in bacon, and a cracker piled with liver paté. To wash it down, a glass of pink champagne. Her father gave it to her. To calm her nerves.

(He returns to the moment in the church) What you notice as the bride stood in the doorway was not her dress, but her face, white. For what was coming down the aisle was a living grenade with the pin pulled out. (pause) the bride (music stops) …threw up. (pause) just as she walked by her mother (pause) and by “threw up” I don’t mean a polite little ladylike burp into her handkerchief. (pause) “She puked. (pause) there’s just no nice word for it. I mean she hosed the front row of the chancel (pause) hitting two bridesmaids, the groom, a ring bearer, and the minister. (pause) three camera’s worth. (pause) The MOTB had thought of everything.

Having disgorged her hors d’oevres, champagne, and the last of her dignity, the bride went limp in her father’s arms, while the groom sat on the floor where he had been standing, too stunned to function. And the mother of the bride moaned, slumped over and passed out cold. (Indicates mother slumping over in rag-doll fashion.)

There was a fire drill then and there at the front of the church that only the Marx Brothers could have topped. (With quick movements suggesting the frenzy to the keystone cops.) Groomsmen rushed about heroically, mini-princess flower girls squalled, bridesmaids sobbed, and people with weak stomachs headed for the exit. (The action stops as the music slows down suggesting the wafting smell.) The smell…of fresh retch…drifted across the church.

Only two people were seen smiling. One was (Indicating the front of the pew the chair for the mother of the groom.) the mother of the groom (pause) and the other… was the father of the bride. (Indicating him standing by his wife)

What happened next? Well, we all went back to real life. Guests were invited to adjourn to the reception hall, though they did not eat or drink as much as they might have in different circumstances. The bride was consoled, cleaned up, and fitted out with a bridesmaid’s dress, and hugged and kissed a lot by the groom. She’ll always love him for that. When he said “for better or for worse” he meant it. THE CAST WAS REASSEMBLED WHERE WE LEFT OFF. A SINGLE FLUTE PLAYED A QUIET AIR, THE WORDS WERE SPOKEN AND THE DEED WAS DONE. Everybody cried, as people are supposed to do at weddings, mostly because the groom held the bride in his arms through the whole ceremony. And no groom ever kissed a bride more “tenderly” then him.

If one can hope for a wedding that it be memorable, then theirs was a raging success. NOBODY who was there will EVER forget it. (He strikes the bridal runner)

They lived happily ever after as anyone does—happier then most, in fact. They have been married for 12 years now, and have 3 lovely children.

But that’s not the end of the story. (As he talks he arranges the chairs into a living room formation of imaginary TV sets, keeping the same designated chair for the MOTB in its original spot.) On the tenth anniversary of this disastrous affair, a party was held. A feast was laid, best friends invited, and three TV sets were mustered. Remember there were 3 video cameras at the scene of the accident. All 3 tapes were shown at once. The effect. . . pretty interesting. Especially with the running commentary and the stop-action stuff that is a little gross when seen one frame at a time. The part that got cheers and toasts was when the camera focused on the grin of the father of the bride as he contemplates his wife being revived.

I really like this part of the story, not because of the party, but because of who organized it. (Gesturing to her sitting in her chair) of course. The infamous MOTB. The mother of the bride is still at it, but she’s a lot looser these days. She not only forgave her husband and everyone else for their part in the debacle, she forgave herself. And nobody laughed harder at the videotapes then she.

There’s a word for what she has. Grace. And that’s why the same grinning man has been married to her for forty years. And why her daughter loves her still.
```

---

## IC-1394: Mr. Big

- Title: Mr. Big
- Author (byline): Woody Allen
- Work: Getting Even
- Publisher: Vintage
- Publication date as stated: Aug 1978
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: KAISER, HEATHER/CLAIRE/ELLEN, WISEMAN, CHICAGO PHIL, SERGEANT REED, THE POPE
- Teaser before the introduction: Yes
- Spoken words (computed): 2170
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

KAISER: What can I do for you, sugar?

HEATHER/CLAIRE/ELLEN: I want you to find someone for me, Mr. Lupowitz.

KAISER: Call me Kaiser, sugar. All right, so what's the scam?

HEATHER/CLAIRE/ELLEN: God. The Creator, the Underlying Principle, the First Cause of Things, the All Encompassing. I want you to find Him for me.

KAISER: Why?

HEATHER/CLAIRE/ELLEN: That's my business, Kaiser. You just find Him.

KAISER: I'm sorry, sugar. You got the wrong boy . . . Unless I know all the facts.”

HEATHER/CLAIRE/ELLEN: (biting her lower lip) O.K., O.K.

KAISER: (to audience) She straightened the seam of her stocking, which was strictly for my benefit, but I wasn't buying any at the moment. (to Heather) Let's have it on the line, sugar.

HEATHER/CLAIRE/ELLEN: My name is not Heather Butkiss, either. It's Claire Rosensweig and I'm a student at Vassar. Philosophy major. History of Western Thought and all that. I have a paper due January. On Western religion. All the other kids in the course will hand in speculative papers. But I want to know. Professor Grebanier said if anyone finds out for sure, they're a cinch to pass the course. And my dad's promised me a Mercedes if I get straight Xs."

KAISER: (to audience) I opened a deck of Luckies and a pack of gum and had one of each. Her story was beginning to interest me. Spoiled coed. High IQ and a body I wanted to know better. (To Claire) What does God look like?

HEATHER/CLAIRE/ELLEN: I've never seen Him.

KAISER: "Well, how do you know He exists?

HEATHER/CLAIRE/ELLEN: That's for you to find out.

KAISER: Oh, great. Then you don't know what He looks like? Or where to begin looking?

HEATHER/CLAIRE/ELLEN: No. Not really. Although I suspect He's everywhere. In the air, in every flower, in you and I - and in this chair.

KAISER: (to audience) So she was a pantheist. I made a mental note of it and said I'd give her case a try-for a hundred bucks a day, expenses, and a dinner date. She smiled and O.K.'d the deal. We rode down in the elevator together. Outside it was getting dark. Maybe God did exist and maybe He didn't, but somewhere in that city there were sure a lot of guys who were going to try and keep me from finding out. My first lead was Rabbi Itzhak Wiseman, a local cleric who owed me a favor for finding out who was rubbing pork on his hat. I knew something was wrong when I spoke to him because he was scared. Real scared.

WISEMAN: Of course there's a you-know-what, but I'm not even allowed to say His name or He'll strike me dead, which I could never understand why someone is so touchy about having his name said.

KAISER: You ever see Him?

WISEMAN: Me? Are you kidding? I'm lucky I get to see my grandchildren.

KAISER: Then how do you know He exists?

WISEMAN: How do I know? What kind of question is that? Could I get a suit like this for fourteen dollars if there was no one up there? Here, feel a gabardine-how can you doubt?

KAISER: You got nothing more to go on?

WISEMAN: Hey-what's the Old Testament? Chopped liver? How do you think Moses got the Israelites out of Egypt? With a smile and a tap dance? Believe me, you don't part the Red Sea with some gismo from Korvette's. It takes power.

KAISER: So He's tough, eh?

WISEMAN: Yes. Very tough. You'd think with all that success He'd be a lot sweeter.

KAISER: How come you know so much?

WISEMAN: Because we're the chosen people. He takes best care of us of all His children, which I'd also like to someday discuss with Him.

KAISER: What do you pay Him for being chosen?

WISEMAN: Don't ask.

KAISER: (to audience) So that's how it was. The Jews were into God for a lot. It was the old protection racket. Take care of them in return for a price. And from the way Rabbi Wiseman was talking, He soaked them plenty. I got into a cab and made it over to Danny's Billiards on Tenth Avenue. The manager was a slimy little guy I didn't like. Chicago Phil. Forger, bank robber, strong-arm man, and avowed atheist.

CHICAGO PHIL: The guy never existed, Kaiser. This is the straight dope. It's a big hype. There's no Mr. Big. It's a syndicate. Mostly Sicilian. It's international. But there is no actual head. Except maybe the Pope.

KAISER: I want to meet the Pope.

CHICAGO PHIL: (winking) It can be arranged..

KAISER: Does the name Claire Rosensweig mean anything to you?

CHICAGO PHIL: No.

KAISER: Heather Butkiss?

CHICAGO PHIL: Oh, wait a minute. Sure. She's that peroxide job with the bazooms from Radcliffe.

KAISER: Radcliffe? She told me Vassar.

CHICAGO PHIL: Well, she's lying. She's a teacher at Radcliffe. She was mixed up with a philosopher for a while.

KAISER: Pantheist?

CHICAGO PHIL: No. Empiricist, as I remember. Bad guy. Completely rejected Hegel or any dialectical methodology.

KAISER: One of those.

CHICAGO PHIL: Yeah. He used to be a drummer with a jazz trio. Then he got hooked on logical positivism. When that didn't work, he tried pragmatism. Last I heard he stole a lot of money to take a course in Schopenhauer at Columbia. The mob would like to find him-or get their hands on his textbooks so they can resell them.

KAISER: Thanks, Phil.

CHICAGO PHIL: Take it from me, Kaiser. There's no one out there. It's a void. I couldn't pass all those bad checks or screw society the way I do if for one second I was able to recognize any authentic sense of Being. The universe is strictly phenomenological. Nothing's eternal. It's all meaningless.

KAISER: (to audience) I had a beer at O'Rourke's and tried to add it all up, but it made no sense at all. Socrates was a suicide-or so they said. Christ was murdered. Nietzsche went nuts. If there was someone out there, He sure as hell didn't want anybody to know it. And why was Claire Rosensweig lying about Vassar?

Could Descartes have been right? Was the universe dualistic? Or did Kant hit it on the head when he postulated the existence of God on moral grounds? Then the phone rang. The voice on the other end was Sergeant Reed of Homi-cide.

SERGEANT REED: You still looking for God?

KAISER: Yeah.

SERGEANT REED: An all-powerful Being? Great Oneness, Creator of the Universe? First Cause of All Things?

KAISER: That's right.

SERGEANT REED: Somebody with that description just showed up at the morgue. You better get down here right away.

KAISER: It was Him all right, and from the looks of Him it was a professional job.

SERGEANT REED: He was dead when they brought Him in.

KAISER: Where'd you find Him?

SERGEANT REED: A warehouse on Delancey Street.

KAISER: Any dues?

SERGEANT REED: It's the work of an existentialist. We're sure of that.

KAISER: How can you tell?

SERGEANT REED: Haphazard way how it was done. Doesn't seem to be any system followed. Impulse.

KAISER: A crime of passion?

SERGEANT REED: You got it. Which means you're a suspect, Kaiser.

KAISER: Why me?

SERGEANT REED: Everybody down at headquarters knows how you feel about Jaspers.

KAISER: That doesn't make me a killer.

SERGEANT REED: Not yet, but you're a suspect.

KAISER: (to audience) Outside on the street I sucked air into my lungs and tried to dear my head. I took a cab over to Newark and got out and walked a block to Giordino's Italian Restaurant. There, at a back table, was His Holiness. It was the Pope, all right. Sitting with two guys I had seen in half a dozen police line-ups. "Sit down," he said, looking up from his fettuccine. He held out a ring. I gave him my toothiest smile but didn't kiss it. It bothered him and I was glad. Point for me.

THE POPE: Would you like some fettuccine?

KAISER: No thanks, Holiness. But you go ahead.

THE POPE: Nothing? Not even a salad?

KAISER: I just ate.

THE POPE: Suit yourself, but they make a great Roquefort dressing here. Not like at the Vatican, where you can't get a decent meal.

KAISER: I'll come right to the point, Pontiff. I'm looking for God.

THE POPE: You came to the right person.

KAISER: Then He does exist? (to audience) They all found this very amusing and laughed. The hood next to me said, "Oh, that's funny. Bright boy wants to know if He exists." I shifted my chair to get comfortable and brought the leg down on his little toe. "Sorry." But he was steaming.

THE POPE: Sure He exists, Lupowitz, but I'm the only one that communicates with Him. He speaks only through me.

KAISER: Why you, pal?

THE POPE: Because I got the red suit.

KAISER: This get-up?

THE POPE: Don't knock it. Every morning I rise, put on this red suit, and suddenly I'm a big cheese. It's all in the suit. I mean, face it, if I went around in slacks and a sports jacket, I couldn't get arrested religion-wise.

KAISER: Then it's a hype. There's no God.

THE POPE: I don't know. But what's the difference? The money's good.

KAISER: You ever worry the laundry won't get your red suit back on time and you'll be like the rest of us?

THE POPE: I use the special one-day service. I figure it's worth the extra few cents to be safe.

KAISER: Name Claire Rosensweig mean anything to you?

THE POPE: Sure. She's in the science department at Bryn Mawr.

KAISER: Science, you say? Thanks.

THE POPE: For what?

KAISER: The answer, Pontiff. (to audience) I grabbed a cab and shot over the George Washington Bridge. On the way I stopped at my office and did some fast checking. Driving to Claire's apartment, I put the pieces together, and for the first time they fit. When I got there something seemed to be troubling her.

HEATHER/CLAIRE/ELLEN: God is dead. The police were here. They're looking for you. They think an existentialist did it.

KAISER: No, sugar. It was you.

HEATHER/CLAIRE/ELLEN: What? Don't make jokes, Kaiser.

KAISER: It was you that did it.

HEATHER/CLAIRE/ELLEN: What are you saying?

KAISER: You, baby. Not Heather Butkiss or Claire Rosensweig, but Dr. Ellen Shepherd.

HEATHER/CLAIRE/ELLEN: How did you know my name?

KAISER: Professor of physics at Bryn Mawr. The youngest one ever to head a department there. At the midwinter Hop you get stuck on a jazz musician who's heavily into philosophy. He's married, but that doesn't stop you. A couple of nights and it feels like love. But it doesn't work out because something comes between you. God. Y'see, sugar, he believed, or wanted to, but you, with your pretty little scientific mind, had to have absolute certainty.

HEATHER/CLAIRE/ELLEN: No, Kaiser, I swear.

KAISER: So you pretend to study philosophy because that gives you a chance to eliminate certain obstacles. You get rid of Socrates easy enough, but Descartes takes over, so you use Spinoza to get rid of Descartes, but when Kant doesn't come through you have to get rid of him too.

HEATHER/CLAIRE/ELLEN: You don't know what you're saying.

KAISER: You made mincemeat out of Leibniz, but that wasn't good enough for you because you knew if anybody believed Pascal you were dead, so he had to be gotten rid of too, but that's where you made your mistake because you trusted Martin Buber. Except, sugar, he was soft. He believed in God, so you had to get rid of God yourself.

HEATHER/CLAIRE/ELLEN: Kaiser, you're mad!

KAISER: No, baby. You posed as a pantheist and that gave you access to Him-if He existed, which he did. He went with you to Shelby's party and when Jason wasn't looking, you killed Him.

HEATHER/CLAIRE/ELLEN: Who the hell are Shelby and Jason?

KAISER: What's the difference? Life's absurd now anyway.

HEATHER/CLAIRE/ELLEN: Kaiser, you wouldn't turn me in?

KAISER: Oh yes, baby. When the Supreme Being gets knocked off, somebody's got to take the rap.

HEATHER/CLAIRE/ELLEN: Oh, Kaiser, we could go away together. Just the two of us. We could forget about philosophy. Settle down and maybe get into semantics.

KAISER: Sorry, sugar. It's no dice. (to audience) She was all tears now. A Venus whose right hand tousled my hair while her left hand had picked up a .45 and was holding it behind my back. I let go with a slug from my .38 before she could pull the trigger, and she dropped her gun and doubled over in disbelief.

HEATHER/CLAIRE/ELLEN: How could you, Kaiser?

KAISER: (to audience) She was fading fast, but I managed to get it in, in time. (to Ellen) The manifestation of the universe as a complex idea unto itself as opposed to being in or outside the true Being of itself is inherently a conceptual nothingness or Nothingness in relation to any abstract form of existing or to exist or having existed in perpetuity and not subject to laws of physicality or motion or ideas relating to non-matter or the lack of objective Being or subjective otherness. (to audience) It was a subtle concept but I think she understood before she died.
```

---

## IC-1395: Mr. Charles, Currently of Palm Beach

- Title: Mr. Charles, Currently of Palm Beach
- Author (byline): Paul Rudnick
- Work: The New Century
- Publisher: Dramatists Play Service
- Publication date as stated: 2008
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: MR. CHARLES
- Teaser before the introduction: Yes
- Spoken words (computed): 1099
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paul Rudnick
Book: The New Century
ISBN: 978-0822223153
Publisher: Dramatists Play Service
Date (Month/Year): 2008
```

### Introduction (context only: never use it for content warnings)

```text
Mr. Charles is a flaming, fashion-conscious homosexual. On the outside. But as he begins reading letters written to his show, his true self begins to shine through. Mr. Charles, Currently of Palm Beach by Paul Rudnick
```

### Performance text (classify this)

```text
MR. CHARLES: (Reads from a letter) “What causes homosexuality?” (He puts down the letter) I do. I am so deeply homosexual, that with just a glance I can actually turn someone gay. (He glances at someone in the audience) Well, that was easy. Sometimes, for a lark, I like to stroll through the maternity wards, to upset new parents. I am Mr. Charles, and I am currently residing here in Palm Beach . . . in semi-retirement. In exile. You see, I was asked to leave New York. There was a vote. As revenge, I have begun to broadcast this program on cable channel 47, a show which I call “Too Gay.” It can be found at four a.m. on alternate Thursdays, in between “Adult Interludes” and “Stretching with Sylvia.” Poor dear.

MR. CHARLES: Today’s modern homosexuals find me an embarrassment. This is because, on certain occasions, I take what I like to call—a nelly break. [By nelly break, Mr. Charles means an eruption into the sort of flaming, limp-wristed behavior that for many years was the standard American perception of gay men] For example: A few months ago, I attended an NYU conference on gay role models. And this young man stood up and said . . . (In an earnest and manly voice) “We must show the world that gay people are not just a pack of screaming queens, with eye make-up, effeminate hand gestures, and high-pitched voices.” And I just said . . . (He does a nelly break, shrieking and mincing and flapping his wrists; he might burble, “oh girl! Oh, Miss Thing! Oh, Mary!” Then he stops, instantly calm again.) It just happened. I went nelly. I just began babbling, in Gay English. You know, Shebonics.

Oh, or another time, I was attending a rally. And a woman approached me, and she said, “I would like you to donate five thousand dollars, to support our boycott of Hollywood films which portray homosexuals as socially irresponsible, promiscuous, and campy. (Another delirious nelly break.) And so I was asked to leave the city.

Since I have begun these broadcasts, I have received many letters and postcards, including this telegram, from the National Gay Task Force in Washington. (He picks up a telegram from the table) It reads . . . (Reading the telegram) “Dear Mr. Charles. Stop” (He puts down the telegram)

I would now like to answer several of the many queries I have received, regarding homosexuality: (He picks up a letter) “Dear Mr. Charles, Should gays be allowed to serve in the military?” Oh, no. Congress is absolutely right. You see, I have this military fantasy. (Mr. Charles acts out his fantasy) I’m serving in Vietnam, with my unit. And one night, I traipse into the shower tent. It’s after hours, and I’m just wearing my kimono, mules and a light moisture pack. And I hear the sound of rushing water . . . and I turn and there at the end of a row of showers stands a naked marine – Colin Powell. His flesh glistens as he lathers up. Finally, I speak. “Hello, soldier,” I murmur. “Loofah?” No, darlings, we have no place in the armed forces. Make remarks, not war.

(Picking up another letter) “Should gays be allowed to marry?” Of course, wealthy older women.

(another letter) “Dear Mr. Charles, How can I raise gay-positive children in today’s political climate?” Well, there are many politically aware children’s books, including Daddy’s Roommate and Heather Has Two Mommies. I will soon be publishing my additions to this series. My children’s books will include Uncle Patrick Has a Beautiful Apartment and Aunt Cathy ‘s Large Friend.

(Another letter) “Dear Mr. Charles, do you enjoy gay theatre?” I am gay theatre. Alright, I will now give you the entire history of American Gay theatre in sixty seconds. Go! (He free-associate rapidly, using various voices and accents) “Jimmy isn’t like the other boys -- do you know what you are? -- he’s no son of mine! I’m just so lonely and sick of my own evil! -- he was a boy, just a boy -- Skipper was my buddy, and our love was pure and strong, but those things they’re saying, they’re true about me! I’m so sick and ashamed, Karen! Do you know what you are? I am a thirty-two-year-old pockmarked Jew fairy, and that was when my father saw me backstage, in my wig and my tights, and he said, take care of my son. (Singing) I am what I am! (in a gravelly, Harvey Fierstein voice) I just wanna be loved, is that so wrong? But Doctor, what’s wrong with David, with all the Davids? Our people are dying and the mayor still won’t even say the name of the disease— (He raises his arms, as graceful wings.) Let the great work begin! (He raises his arms again) Let the great work begin, part two! When you speak of gay theatre, and you will -- be kind. Because it’s all about love, valor, baseball and gratuitous frontal male nudity. Bravo! (Mr Charles bows deeply)

Which brings us to my favorite part of the program, a forum which I call, “People I Hate.” This week’s person I hate most in the world is someone I’ve never even met. His name is Theodore DiBenedetto, and he wrote this letter to the editor of our local paper. (Mr. Charles reads aloud from a copy of the newspaper, using a butch, manly voice) “Dear Palm Beach Sentinel, I am a gay man who owns the East Bay Hardware Store.” (He looks up with a withering glance and then continues) “And I am sick and tired of gay people demanding equal rights when they keep behaving like freaks. As gay people, we must prove that we are not just stereotypes. We must demonstrate that our lives are normal and wholesome. We must show that we can hold jobs, go to church and raise children, just like anyone else. That is how we will earn our place at the table.”

(Mr. Charles puts down the paper. He is now dangerously angry, like steel) Darling, I set the table. I arranged the flowers. And I would rather have [a] knife at my throat than share even a brunch with Mr. DiBenedetto and his kind. The nice boys. The good citizens. But please, Mr. DiBenedetto, if you’d like, by all means, be normal and wholesome and responsible, get married, have children, move to the suburbs. I’ll wait here. Oh, and Mr. DiBenedetto, by the by . . .

(Mr. Charles launches into a viciously savage nelly break. He becomes a ferocious nelly whirlwind, making enormous flamboyant gestures to the audience. He might look into the camera and elaborately mime applying lipstick, and licking his forefinger and slicking each eyebrows).

Ah, I am the last of my kind. I shall perish, like the dinosaur. Unless of course, Steven Spielberg discovers some ancient DNA and makes more. But let me ask you something. Have you ever been in love? Hands? You see, I fell in love quite early. I must have been, oh, twelve? I had just been savagely beaten by . . . (He tries to remember, quite cheerfully) oh it could have been anyone. But this was at school. I came home bruised, caked with mud. I ran up to my room, and I looked in the mirror. And I thought, all right, whom would I rather be? The boys who beat me up, the boys who played baseball and caught frogs and were already losing their figures? Or would I rather be -- Mr. Charles? Who even at twelve knew how to turn his face so the tears would glisten. Who knew enough to immediately put Billie Holiday on the hi-fi, and lip-sync. Who could transform a schoolyard humiliation into an Academy Award. And that was when I fell passionately in love -- with being gay.
```

---

## IC-1396: Naked Mole Rat Gets Dressed

- Title: Naked Mole Rat Gets Dressed
- Author (byline): Mo Willems
- Work: Not specified
- Publisher: Hyperion Books for Children
- Publication date as stated: Jan 2009
- Event as filed: Humorous Interpretation
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
2021 National Qualifier
MN State Qualifier
```

### Introduction (context only: never use it for content warnings)

```text
I believe that we are NOT all meant to be the same; look the same, think the same. There is no one right way to show up in the world. Our individual, unique, varied expressions of life are beautiful.

George Bernard Shaw once said: “There are those that look at things the way they are, and ask why? I dream of things that never were, and ask why not?

Why not? Why not, indeed? Do clothes hurt anyone? In the infamous words of RuPaul: “We’re all born naked and the rest is . . .”

Naked Mole Rate Gets Dressed by Mo Willems
```

### Performance text (classify this)

```text
NARRATOR: There is so much to learn about the fascinating little creatures known as naked mole rats. But for this story you only need to know three things: 1) They are a little bit rat. 2) They are a little bit mole. 3) They are ALL naked. Well, they were, with one exception . . .

NARRATOR: Wilbur the naked mole rat who liked to get dressed. (Wilbur inspects his attire in a large floor length mirror and adjusts his tie) When the other naked mole rats saw him, they said:

MOLE RAT 1: Eeeeeeewwww!

MOLE RAT 2: Yuck!

MOLE RAT 3: What are you doing?

WILBUR: I like clothes. When I get dressed, I can be . . . fancy, or funny, or cool, or I can just be an astronaut. (Wilbur assumes the demeanor of each description)

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

NARRATOR: When Wilbur heard about Grand-pah’s proclamation, he knew it was serious. But he had no idea what to wear. (Wilbur begins trying on different outfits, hats, ties, jackets.

shoes) In the end, Wilbur decided to play it safe. (Wilbur takes off all his clothes except for his socks)

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

## IC-1397: Next

- Title: Next
- Author (byline): Terrance McNally
- Work: Terrence McNally 15 Short Plays, Pgs 61-82
- Publisher: Smith and Kraus Pub Inc
- Publication date as stated: June 1994
- Event as filed: Humorous Interpretation
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

## IC-1398: Notes from the Overfed

- Title: Notes from the Overfed
- Author (byline): Woody Allen
- Work: Getting Even
- Publisher: Vintage
- Publication date as stated: Aug 1978
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1617
- Already set (do not supply): none

### Source block (context only)

```text
Author: Woody Allen
Book: Getting Even
ISBN: 0394726405
Publisher: Vintage
Date(Month/Year): Aug 1978
```

### Introduction (context only: never use it for content warnings)

```text
Grabbing a handful of cookies off the plate, stealing a roommate's food, overeating while home alone. These could be signs of compulsive overeating. In the United States, the nation's fixation on weight is only making the disorder more prevalent, experts say. The number of support groups for people whose lives are controlled by food has grown sharply in recent years. But perhaps the problem isn’t metabolic or even psychiatric in nature. Perhaps, just perhaps the growing girth of our population is driven by a desire to be spiritually connect to God.

After all . . . . God is everywhere and in all things. Food is a thing . . . . so consuming mass quantities of food should bring us closer to God. The logic amazes . . . . . doesn’t it? Notes from the Overfed by Woody Allen.
```

### Performance text (classify this)

```text
I am fat. I am disgustingly fat. I am the fattest human I know. I have nothing but excess poundage all over my body. My fingers are fat. My wrists are fat. My eyes are fat. (Can you imagine fat eyes?) I am hundreds of pounds overweight. Flesh drips from me like hot fudge off a sundae. My girth has been an object of disbelief to everyone who's seen me. There is no question about it, I'm a regular fatty.

Now, you may ask, are there advantages or disadvantages to being built like a planet? I do not mean to be facetious or speak in paradoxes, but I must answer that fat in itself is above bourgeois morality. It is simply fat. That fat could have a value of its own, that fat could be, say, evil or pitying, is, of course, a joke. Absurd! For what is fat after all but an accumulation of pounds? And what are pounds? Simply an aggregate composite of cells. Can a cell be moral? Is a cell beyond good or evil? Who knows-they're so small. No, my friend, we must never attempt to distinguish between good fat and bad fat. We must train ourselves to confront the obese without judging, without thinking this man's fat is first-rate fat and this poor wretch's is grubby fat.

Take the case of K. This fellow was porcine to such a degree that he could not fit through the average doorframe without the aid of a crowbar. Indeed, K. would not think to pass from room to room in a conventional dwelling without first stripping completely and then buttering himself. I am no stranger to the insults K. must have borne from passing gangs of young rowdies. How frequently he must have been stung by cries of "Tubby!" and "Blimp!" How it must have hurt when the Governor of the province turned to him on the Eve of Michaelmas and said, before many dignitaries, "You hulking pot of kasha!"

Then one day, when K. could stand it no longer, he dieted. Yes, dieted! First sweets went. Then bread, alcohol, starches, sauces. In short, K. gave up the very stuff that makes a man unable to tie his shoelaces without help from the Santini Brothers. Gradually he began to slim down. Rolls of flesh fell from his arms and legs. Where once he looked roly-poly, he suddenly appeared in public with a normal build. Yes, even an attractive build. He seemed the happiest of men. I say "seemed," for eighteen years later, when he was near death and fever raged throughout his slender frame, he was heard to cry out, "My fat! Bring me my fat! Oh, please! I must have my fat! Oh, somebody lay some avoirdupois on me! What a fool I've been. To part with one's fat! I must have been in league with the Devil!" I think that the point of the story is obvious.

Now the reader is probably thinking, Why, then, if you are Lard City, have you not joined a circus? Because-and I confess this with no small embarrassment-I cannot leave the house. I cannot go out because I cannot get my pants on.

My legs are too thick to dress. They are the living result of more corned beef than there is on Second Avenue-I would say about twelve thousand sandwiches per leg. And not all lean, even though I specified. One thing is certain: If my fat could speak, it would probably speak of man's intense loneliness-with, oh, perhaps a few additional pointers on how to make a sailboat out of paper. Every pound on my body wants to be heard from, as do Chins Four through Twelve inclusive. My fat is strange fat. It has seen much. My calves alone have lived a lifetime. Mine is not happy fat, but it is real fat. It is not fake fat. Fake fat is the worst fat you can have, although I don't know if the stores still carry it.

But let me tell you how it was that I became fat. For I was not always fat. It is the Church that has made me thus. At one time I was thin-quite thin. So thin, in fact, that to call me fat would have been an error in perception. I remained thin until one day-I think it was my twentieth birthday when I was having tea and cracknels with my uncle at a fine restaurant. Suddenly my uncle put a question to me. "Do you believe in God?" he asked. "And if so, what do you think He weighs?" So saying, he took a long and luxurious draw on his cigar and, in that confident, assured manner he has cultivated, lapsed into a coughing fit so violent I thought he would hemorrhage.

"I do not believe in God," I told him. "For if there is a God, then tell me, Uncle, why is there poverty and baldness? Why do some men go through life immune to a thousand mortal enemies of the race, while others get a migraine that lasts for weeks? Why are our days numbered and not, say, lettered? Answer me, Uncle. Or have I shocked you?"

I knew I was safe in saying this, because nothing ever shocked the man. Indeed, he had seen his chess tutor's mother raped by Turks and would have found the whole incident amusing had it not taken so much time.

"Good nephew," he said, "there is a God, despite what you think, and He is everywhere. Yes! Everywhere!"

"Everywhere, Uncle? How can you say that when you don't even know for sure if we exist? True, I am touching your wart at this moment, but could that not be an illusion? Could not all life be an illusion? Indeed, are there not certain sects of holy men in the East who are convinced that nothing exists outside their minds except for the Oyster Bar at Grand Central Station? Could it not be simply that we are alone and aimless, doomed to wander in an indifferent universe, with no hope of salvation, nor any prospect except misery, death, and the empty reality of eternal nothing?"

I could see that I made a deep impression on my uncle with this, for he said to me, "You wonder why you're not invited to more parties! Jesus, you're morbid!" He accused me of being nihilistic and then said, in that cryptic way the senile have, "God is not always where one seeks Him, but I assure you, dear nephew, He is everywhere. In these cracknels, for instance." With that, he departed, leaving me his blessing and a check that read like the tab for an aircraft carrier.

I returned home wondering what it was he meant by that one simple statement "He is everywhere. In these cracknels, for instance." Drowsy by then, and out of sorts, I lay down on my bed and took a brief nap. In that time, I had a dream that was to change my life forever. In the dream, I am strolling in the country, when I suddenly notice I am hungry. Starved, if you will. I come upon a restaurant and I enter. I order the open hot-roast-beef sandwich and a side of French. The waitress, who resembles my landlady (a thoroughly insipid woman who reminds one instantly of some of the hairier lichens), tries to tempt me into ordering the chicken salad, which doesn't look fresh. As I am conversing with this woman, she turns into a twenty-four-piece starter set of silverware. I become hysterical with laughter, which suddenly turns to tears and then into a serious ear infection. The room is suffused with a radiant glow, and I see a shimmering figure approach on a white steed. It is my podiatrist, and I fall to the ground with guilt. Such was my dream. I awoke with a tremendous sense of well-being. Suddenly I was optimistic. Everything was clear.

My uncle's statement reverberated to the core of my very existence. I went to the kitchen and started to eat. I ate everything in sight. Cakes, breads, cereals, meat, fruits. Succulent chocolates, vegetables in sauce, wines, fish, creams and noodles, eclairs, and wursts totaling in excess of sixty thousand dollars. If God is everywhere, I had concluded, then He is in food. Therefore, the more I ate the godlier I would become. Impelled by this new religious fervor, I glutted myself like a fanatic. In six months, I was the holiest of holies, with a heart entirely devoted to my prayers and a stomach that crossed the state line by itself. I last saw my feet one Thursday morning in Vitebsk, although for all I know they are still down there. I ate and ate and grew and grew. To reduce would have been the greatest folly. Even a sin! For when we lose twenty pounds, we may be losing the twenty best pounds we have! We may be losing the pounds that contain our genius, our humanity, our love and honesty or, in the case of one inspector general I knew, just some unsightly flab around the hips.

Now, I know what you are saying. You are saying this is in direct contradiction to everything-yes, everything-I put forth before. Suddenly I am attributing to neuter flesh, values! Yes, and what of it? Because isn't life that very same kind of contradiction? One's opinion of fat can change in the same manner that the seasons change, that our hair changes, that life itself changes. For life is change and fat is life, and fat is also death. Don't you see? Fat is everything! Unless, of course, you're overweight.
```

---

## IC-1399: Oedi

- Title: Oedi
- Author (byline): Rich Orloff
- Work: The Best American Short Plays 1997-1998 (Edited by Glenn Young), Pgs 162-178
- Publisher: Applause Theatre Books
- Publication date as stated: May 2000
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: TOWN CRIER, OEDIPUS, CREON, JOCASTA
- Teaser before the introduction: Yes
- Spoken words (computed): 1841
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rich Orloff
Book: The Best American Short Plays 1997-1998 (Edited by Glenn Young),
Pgs 162-178
ISBN: 978-1557833655
Publisher: Applause Theatre Books
Date (Month/Year): May 2000
```

### Introduction (context only: never use it for content warnings)

```text
Welcome to Ancient Greece and the city of Thebes – the birthplace of the infamous Oedipus. Before he was even born, the oracle at Delphi (gesture in some way to the gods) told his parents that the boy would grow up to kill his father and marry his mother. (shocked gasp) So . . . his parents did what many people with unwanted children did in the past. They had the baby's feet spiked and hired a herdsman to abandon the child in the wild. (shrug) The kind-hearted herdsman just couldn’t do it. Instead, he gave baby Oedipus to a childless king and queen in Corinth and they raised Oedipus as their own. (in an ominous voice) But one cannot circumvent the will of the gods! (thunderclap) Okay, enough with the dramatic. The story opens with Oedipus as an adult finding out the news of who he truly is. This is Sophocles’ story of Oedipus from the comedic imaginings of Rich Orloff . . . Oedi! Come on down!
```

### Performance text (classify this)

```text
TOWN CRIER: (Pg 162-178) (off stage) Hear ye, hear ye! ________o’clock and all is well. For the best in dining delicacies, treat yourself to Hecuba’s House of Hummus! Try their babagonoosh!

OEDIPUS: Creon, my trusted aide, you have returned! Ever since the plague has hit our beloved Thebes, the people insist that we find the killer of their former king. They are convinced that until we punish the murderer, the plague shall continue. As their new king, I owe them the truth. Besides, the latest polls show my popularity's plummeting. I created the Creon Commission to ferret out the facts of this fearsome felony, and I demand to know what you have learned.

CREON: Well, first we visited the oracles of Delphi. They [told] us that King Laios was murdered by his own son!

OEDIPUS: But that's crazy. Laios had no son.

CREON: Actually, he did, many years ago, but the child was banished as an infant. People assumed the child died in the wilderness.

OEDIPUS: Poor child. I feel his pain, as if it were my own.

CREON: Funny you should say that. We learned the child had been rescued by a shepherd a grew up to be about your height, your weight, and according to descriptions, he looked a lot like you.

OEDIPUS: What a coincidence.

CREON: Oedipus, how to put this... You know how much I admire you. When you first came to town, it was I who encouraged the people to make you king. (beat) You never murdered anyone, did you? Say, kill anyone on your journey here?

OEDIPUS: Let me recall. I decided it was time to leave Corinth and seek my fortune in the world. So I decided to journey to Thebes. When I got to the town of Phokis, I met a hostile band of travellers. One of them called me a mama's boy, so I clubbed them all to death. Other than that, I didn't kill anyone.

CREON: For that you clubbed him to death? Well, Oedipus, I don't know how to tell you this, but we learned that King Laios was clubbed to death in the town of Phokis.

OEDIPUS: You're not suggesting I - I'd never kill a king. It's - It's inappropriate.

CREON: He was on a religious pilgrimage. . . He always dressed down for those things.

OEDIPUS: Then it's possible But Tiresias prophesied that Laios would be killed by his own son. I never even met the man before.

CREON: Oedipus, we discovered Polybus and Merope weren't your real parents. You're an orphan. We also know that the son of Laios had a birthmark in the shape of an olive on the bottom of his left foot. [Creon stares at Oedipus' left foot.]

OEDIPUS: But I hate taking off my sandals. It always takes so long to lace them back up. [Oedipus unlaces his left sandal and lifts his left foot. On the bottom of his foot is a birthmark in the shape of a huge green olive with a red pimento.] As you can see, my foot has no such mark.

CREON: Oedi, admit it. That's an olive.

OEDIPUS: I prefer to think of it as an unripe eggplant with ketchup on it.

CREON: It's an olive.

OEDIPUS: Okay, okay. Technically speaking, it's an olive. Oh, woe to me and those who dwell in my house! I've slain a king, and I promised the people I'd put the killer to death. I even said, "Read my lips." But wait! One thing isn't clear.

CREON: Here comes the messy part.

OEDIPUS: If I'm Laios' son, and if Laios was married to Jocasta, who is now my wife, that means, that means, that means - Laios must've had a previous wife, right?

CREON: I'm afraid not.

OEDIPUS: Ever fool around on the side?

CREON: Never.

OEDIPUS: Sperm donor?

CREON: Nope.

OEDIPUS: Oh my gods! Oh my gods! I've married my mother!! No wonder she always knows what I want for breakfast. Oh my gods! I've murdered my father and married my mother! Oh, wretched day! Oh, cursed life! How can I expunge the evil deed from my soul? There is only one way! I must pluck out my eyes immediately! [Oedipus tries to pluck out his eyes, but Creon holds his arms back.]

CREON: Don't do it! You'll have a moment's satisfaction, and a lifetime of wondering if your toga's on straight.

OEDIPUS: Okay, okay. Let go...Does my beloved wife know about this?

CREON: Not yet.

JOCASTA: [off stage] Yoo-hoo, oh, Oedi!

CREON: The queen approaches. [Creon exits]

OEDIPUS: [Calling out] In here, snookums! [Jocasta enters. She's easily thirty or more years older than Oedipus. If she happens to be short and speaks with a slight old world inflection, so much the better.]

OEDIPUS: Jocasta, I must tell you something most horrible, worse than the most terrible news you could imagine.

JOCASTA: You didn't like my brisket last night?

OEDIPUS: That's not it.

JOCASTA: My toga's too short, isn't it? You think a woman my age . . .

OEDIPUS: Your toga's fine.

JOCASTA: Are we having problems I'm unaware of in the horizontal department?

OEDIPUS: No, everything's fine in the - Jocasta, I just received the report of the Creon Commission.

JOCASTA: Oh, good. As soon as we name the murderer of Laios and make him drink some seltzer with a shpritz of hemlock, I know your approval rating will bounce right back.

OEDIPUS: I don't think so. Jocasta. . . The murderer of your late husband stands before you.

JOCASTA: You killed Laios? Oh, no! Horror of horrors! I suddenly feel like plucking

OEDIPUS: Don't pluck your eyes out!

JOCASTA: No, I feel like plucking a chicken. I'm so stressed. How are we going to put a spin on this so the public doesn't hate you?

OEDIPUS: Don't you hate me?

JOCASTA: How can I hate you for something I thought of doing every single day of our marriage?

OEDIPUS: I thought you loved him.

JOCASTA: What's to love? The man snored, he had bad breath, and when I think of the things he made me do . . . the news is not that bad at all.

OEDIPUS: But I have not told you all of it. Jocasta, you remember the prophecy of Tiresias that your husband would be murdered by your son?

JOCASTA: Yes, also remember he prophesied. . .The Iliad would never make it as a novel.

OEDIPUS: [Well], there's reason to believe that, by some ferocious folly of the fates, you married your own son.

JOCASTA: So? Tell me something I don't know. From the first moment you came into town. I took one look at those eyes, that smile, that - oh, wait a second, you have a little shmutz on your forehead. [Jocasta licks her fingers and begins to wipe Oedi's forehead.]

OEDIPUS: Stop that! How could you know I was your son and not tell me?

JOCASTA: I didn't think it was significant.

OEDIPUS: You married me!

JOCASTA: You asked. I would've been happy just dating; you were the one in a hurry. "Marry me, Jocasta, and I'll be the happiest man on earth." What mother could refuse such an offer?

OEDIPUS: But I killed Dad!

JOCASTA: So? He never liked you anyway. Once he heard Tiresias' prediction that you were destined to murder him, he insisted you be sent away. I said, "Can't we wait and see? Maybe he'll just wound you a little." Look, you're here and all is well, so unless there's some more news, I want to get to my belly dancercize class. I need to be in ship shape.

OEDIPUS: Don't you think we have some issues to discuss?

JOCASTA: Like what?

OEDIPUS: Like the fact that we can no longer live as husband and wife.

JOCASTA: Why not?

OEDIPUS: Because you're my mother!

JOCASTA: You say that like it's a negative.

OEDIPUS: Men cannot marry their mothers!

JOCASTA: From what I've heard, most men marry women who remind them of their mothers. Why settle for second best when you can have the real thing?

OEDIPUS: No! I want to be with a woman to whom I'm not already related. I'm a public official. I'm a role model.

JOCASTA: So? Look at the Gods. Zeus has slept with his half-sister, his quarter-sister, his sixteenth- sister. If our own gods get to boff their relatives, why can't you?

OEDIPUS: Because you're my mother!

JOCASTA: Must you make everything so complex, Oedipus? Look, Oedi, I understand this is traumatic for you. But in a healthy marriage, you work through these things.

OEDIPUS: We don't have a healthy marriage! Mom. . . I want a divorce.

JOCASTA: [breaks into hysterical crying] I never thought I'd hear such a thing from my own son. Call in your advisor. See what he says.

OEDIPUS: Get me Creon! [CREON enters]

CREON: I have been busy, my lord, making some initial inquiries into public response to the crisis: The people are confused. 85% of those polled strongly agreed with the statement, "If two people love each other, nothing else in a marriage is important." But 54% also believe that those who commit incest should be boiled alive in non-virgin olive oil.

OEDIPUS: I didn't know she was my mother, does it still fit the technical legal definition of incest?

CREON: Why don't you start a war? That's always a good distraction.

OEDIPUS: I'm not going to start a war just to boost my approval rating. There's only one answer which will prove to the people I show remorse for my sins. I must pluck out my eyes!

CREON: Wouldn't a sincere "I'm sorry" suffice?

OEDIPUS: No! Give me your golden pins. [Oedi grabs two large pins from Jocasta’s toga or hair.]

CREON: Oedipus, don't!

OEDIPUS: Silence! Stand back! [Raising the pins.] I declare myself guilty of wretchedness and sin! From this hour forth, I go in darkness! [Oedipus is about to plunge the pins into his eyes, but he stops at the last moment.] Or . . . maybe I'll just cut off the offending organ which caused the sinful deed. That's it! I'll save my sight but lose my jewels. I declare myself guilty of wretchedness and sin! From this hour forth, I go in eunuchness! [Oedipus is about to plunge the pins into his pelvic region, but stops at the last moment.] Or . . . maybe I'll just cut off my arm. It's a more visible symbol anyway. My left arm, or maybe just one of my fingers, since we're talking symbolic action!

CREON: You know, Oedipus, the more I think about it, the more I wonder, why are we driving ourselves into such a tizzy? You know how fickle the people are. Today they'll want to burn you at the stake; in a week, they'll be obsessed with the latest gossip about the gods. All we need is one good speech and a heartfelt explanation.

OEDIPUS: But how can we explain such a monstrous deed? Oh, what am I to do? If only the gods would give me a sign.

CREON: Maybe they have. Run with me a little. Tiresias saw your fate when you were born; you tried your best not to live it out, but there are powers beyond those of we poor mortals.

OEDIPUS: I get it! Any efforts to forswear malfeasance were futile; it was the fault of the fates! I'll make a speech where I'll take complete responsibility for my actions, but none of the blame.

CREON: We'll say you wanted to smite out your eyes, but you placed your sense of public duty ahead of your own desires. [Imagining the headline:] "Oedipus Rex, Tragic Hero."
```

---

## IC-1400: The Philadelphia

- Title: The Philadelphia
- Author (byline): David Ives
- Work: Take Ten: New 10-Min Plays (ed Lane & Shengold)
- Publisher: Vintage Books
- Publication date as stated: March 1997
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: WAITRESS, AL, MARK
- Teaser before the introduction: Yes
- Spoken words (computed): 1351
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Ives
Book: Take Ten: New 10-Min Plays (ed Lane & Shengold)
ISBN: 978-0679772828
Publisher: Vintage Books
Date (Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
Two guys meet in a diner in New York, but they're both in very different states of mind. Al is in a Los Angeles state of mind. Nothing can faze him . . . even if it did he would just make it a Hollywood movie. Then there's Mark who finds the whole world is against him. He can't get a newspaper at the newsstand, aspirin at the drugstore, and the diner gives him a Cheesesteak when he wants a burger. That's right. Mark's trapped in a Philadelphia state of mind. (Music – Possibly the theme from the Twilight Zone)

It could be worse. You could be stuck in a Cleveland. It's like death without the advantages. The Philadelphia by David Ives.
```

### Performance text (classify this)

```text
AL is at the restaurant table, with the WAITRESS.

WAITRESS: Can I help you?

AL: What's the soup du jour today?

WAITRESS: Soup of the day you got a choice of Polish duck blood or cream of kidney.

AL: Beautiful. Beautiful! Kick me in a kidney.

WAITRESS: (Writes it down.) You got it.

(MARK enters, looking shaken and bedraggled.)

MARK: Al!

AL: Hey there, Marcus. What's up?

MARK: Jesus! Oh man. . . !

AL: What's the matter? Sit down.

MARK: I don't get it, Al. I don't understand it.

AL: You want something? Want a drink? I'll call the waitress

MARK: (Desperate.) No! No! Don't even try. (Gets a breath.) I don't know what's going on today, Al. It's really weird. Right from the time I got up.

AL: What is it? What's the story?

MARK: Well-just for an example. This morning I stopped off at a drugstore to buy some aspirin. This is at a big drugstore, right? I go up to the counter, the guy says what can I do for you, I say, Give me a bottle of aspirin. The guy gives me this funny look and he says, "Oh we don't have that, sir." I said to him, You're a drugstore and you don't have any aspirin?

AL: Did they have Bufferin?

MARK: Yeah!

AL: Advil?

MARK: Yeah!

AL: Extra-strength Tylenol?

MARK: Yeah!

AL: But no aspirin.

MARK: No! And that's the kind of weird thing that's been happening all day. It's like, I go to a newsstand to buy the Daily News, the guy never even heard of it.

AL: Could've been a misunderstanding.

MARK: I asked everyplace-nobody had the News! I had to read the Toronto Hairdresser. Or this. I go into a deli at lunch time to buy a sandwich, the guy tells me they don't have any pastrami. How can they be a deli if they don't have pastrami?

AL: Was this a Korean deli?

MARK: This was a kosher from Jerusalem deli. "Oh we don't carry that, sir," he says to me. "Have some tongue." . . . . I just got into a cab, the guy says he doesn't go to 56th Street! He offers to take me to Newark instead! Looking at me like I'm an alien or something!

AL: Mark. Settle down.

MARK: "Oh I don't go there, sir."

AL: Settle down. Take a breath.

MARK: Do you know what this is?

AL: Sure.

MARK: What is it? What's happening to me?

AL: Don't panic. You're in a Philadelphia.

MARK: I'm in a what?

AL: You're in a Philadelphia. That's all.

MARK: But I'm in . . .

AL: Yes, physically you are in New York. But metaphysically you are in a Philadelphia. You see, inside of what we know as reality there are these pockets, these black holes called Philadelphias. If you fall into one, you run up against exactly the kinda *stuff* that's been happening to you all day.

MARK: Why?

AL: Because in a Philadelphia, no matter what you ask for, you can't get it. You ask for something, they're not gonna have it. You want to do something, it ain't gonna get done. You want to go somewhere, you can't get there from here.

MARK: Good God. So this is very serious.

AL: Just remember, Marcus. This is a condition named for the town that invented the cheese steak. Something that nobody in his right mind would willingly ask for.

MARK: And I thought I was just having a very bad day . . .

AL: Sure. Millions of people have spent entire lifetimes inside a Philadelphia and never even knew it. Look at the city of Philadelphia itself. Hopelessly trapped forever inside a Philadelphia. And do they know it?

MARK: Well what can I do? Should I just kill myself now and get it over with?

AL: You try to kill yourself in a Philadelphia, you're only gonna get hurt, babe.

MARK: SO what do I do?

AL: Best thing you can do is wait it out. Someday the great cosmic train will whisk you outa the City of Brotherly Love and off to someplace happier.

MARK: You're pretty mellow today.

AL: Yeah well. Everybody has to be someplace. (WAITRESS enters.)

WAITRESS: Is your name Allen Chase?

AL: It is indeed.

WAITRESS: There was a phone call for you. Your boss? He says you're fired.

AL: Cool! Thanks. (WAITRESS exits.) So anyway, you have this problem. . .

MARK: Did she just say you got fired?

AL: Yeah. I wonder what happened to my pigs' feet. . .

MARK: Al!? You loved your job! How can you be so calm?

AL: Easy. You're in a Philadelphia? I woke up in a Los Angeles. And life is beautiful! You know Susie packed up and left me this morning.

MARK: Susie left you?

AL: And frankly, Scarlett, I don't give a ****. I say, go and God bless and may your dating pool be Olympic-sized.

MARK: But your job? The garment district is your life!

AL: So I'll turn it into a movie script and sell it to Paramount. Toss in some sex, add a little emotional blah-blah-blah, pitch it to Jack and Dusty, you got a buddy movie with a garment background. Not relevant enough? We'll throw in the hole in the ozone, make it E.C.

MARK: E.C.?

AL: Environmentally correct. Have you heard about this hole in the ozone?

MARK: Sure.

AL: Marcus, I love this concept. I embrace this ozone. Sure, some people are gonna get hurt in the process, meantime everybody else'll tan a little faster.

MARK: (Quiet horror.) So this is a Los Angeles. . .

AL: Well. Everybody has to be someplace.

MARK: Wow . . .

AL: You want my advice? Enjoy your Philadelphia. Sit back and order yourself a beer and a burger and chill out for a while.

MARK: But I can't order anything. Life is great for you out there on your cosmic beach, but whatever I ask for, I'll get a cheese steak or something . . .

AL: No. There's a very simple rule of thumb in a Philadelphia. Ask for the opposite.

MARK: What?

AL: If you can't get what you ask for, ask for the opposite and you'll get what you want. You want the Daily News, ask for the Times. You want pastrami, ask for tongue. So. Would you like a Bud?

MARK: I sure could use a . . .

AL: No. Stop. (very deliberately.) Do you want. . . a Bud?

MARK: (Also deliberately.) No. I don't want a Bud. (WAITRESS enters and goes to the specials board.)

AL: Good. Now there's the waitress. Order yourself a Bud and a burger. But do not ask for a Bud and a burger.

MARK: Waitress!

AL: Don't call her. She won't come. You're in a Philadelphia, so just figure, who needs her.

MARK: Who needs her.

AL: You don't need that waitress.

MARK: Hey, waitress! DROP DEAD! (WAITRESS turns to him.)

WAITRESS: Can I help you, sir?

MARK: Uh-no thanks.

WAITRESS: Okay, what'll you have? (Takes out her pad.)

MARK: Well-how about some O.J.

WAITRESS: Sorry. Squeezer's broken.

MARK: A glass of milk?

WAITRESS: Cow's dry.

MARK: Cuppa coffee?

WAITRESS: Oh we don't have that, sir. (The WAITRESS has spoken the magic words.)

MARK: That's too bad. (exchanges a look and nod with the audience) How about a Heineken?

WAITRESS: Heineken? Try again.

MARK: Bud Lite?

WAITRESS: Just plain Bud is all we got.

MARK: No thanks.

WAITRESS: (Calls.) Gimme a Bud! (to MARK) Anything to eat?

MARK: Pork chops.

WAITRESS: (Writes down.) Hamburger. . .

MARK: Medium.

WAITRESS: Well done. . .

MARK: Baked potato.

WAITRESS: Fries . . . (Exits, calling.) Burn one!

AL: Excellent. You sure you've never done this before?

MARK: I've spent so much of my life asking for the wrong thing without knowing it, doing it on purpose comes easy. I could've saved myself a lot of trouble if I'd screwed up on purpose all those years. Maybe I was in a Philadelphia all along and never knew it!

AL: You might've been in a Baltimore. They're practically the same. (WAITRESS enters, with a glass of beer and a plate.)

WAITRESS: Okay. Here's your Bud. (Sets that in front of MARK.) And one cheese steak.

(She sets that in front of AL, and starts to go.)

AL: Excuse me. Hey. Wait a minute. What is that?

WAITRESS: It's a cheese steak.

AL: No. I ordered cream of kidney.

WAITRESS: Oh we don't have that, sir.

AL: I beg your pardon? (to MARK.) You son of a bitch! I'm in your Philadelphia!

MARK: I'm sorry, Al. I didn't know it was contagious.

AL: Oh God, please don't let me be in a Philadelphia! Don't let me be in a Philadelphia!

MARK: But maybe you're not really in a Philadelphia!

AL: Do you see the cheese on that steak? What do I need for proof? The Liberty Bell? Waitress, bring me a glass of water.

WAITRESS: Water? Don't have that, sir.

AL: (to MARK) "We don't have water"-? What, you think we're in a sudden drought or something? (Suddenly realizes) Holy ****, I just lost my job. . . ! Susie left me! I gotta make some phone calls! (to WAITRESS) 'Scuse me, where's the pay phone?

WAITRESS: Sorry, we don't have a pay phone

AL: Of course you don't have a pay phone, of course you don't! Oh *****, let me outa here! (Exits.)

MARK: I don't know. It's not that bad in a Philadelphia.
```
