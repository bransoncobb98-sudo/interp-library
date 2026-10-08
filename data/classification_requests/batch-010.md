# Classification request: batch 10 of 63 (40 records, IC-0361 to IC-0400)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-010-reply.json`.

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

## IC-0361: Forgive Me, Leonard Peacock

- Title: Forgive Me, Leonard Peacock
- Author (byline): Matthew Quick
- Work: Not specified
- Publisher: Little Brown Books for Young Readers
- Publication date as stated: Aug 2013
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: LEONARD, SILVERMAN, GIRL
- Teaser before the introduction: Yes
- Spoken words (computed): 1670
- Already set (do not supply): none

### Source block (context only)

```text
Author: Matthew Quick
ISBN: 978-0316221337
Publisher: Little Brown Books for Young Readers
Date (Month/Year): Aug 2013
```

### Introduction (context only: never use it for content warnings)

```text
Today is Leonard Peacock’s 18th birthday. He is a loner, an outcast, a misfit and maybe one day he’ll believe that being different is okay, important even. But not today. Today he plans to commit suicide. Unless one caring teacher can convince him that the daily battle of not letting the world destroy you is worth the work.

Forgive Me, Leonard Peacock by Matthew Quick
```

### Performance text (classify this)

```text
LEONARD: (Pg 99) In elementary school the teachers always remembered your birthday. There were cupcakes and everyone sang in a way that made you feel really special and a part of something. There’s a reason the elementary teachers did that. It was important. (Pg 110) You know what? F*** Linda for forgetting my birthday. (Pg 9) Linda is my mother. I call her Linda because it annoys her. She says it “de-moms” her. But she de-mommed herself when she rented an apartment in Manhattan and left me all alone to fend for myself most weeks. She checked out of my life – maybe because it was too intense for her to handle. I don’t know. (Pg 110) (Emotions begin to build – a mix of anger and tears) How do you forget giving birth to someone eighteen years ago today? [It’s] IRRESPONSIBLE and selfish and culpable and inhumane and . . . (Pg 170) Let’s get this birthday party started!

LEONARD: (Pg 109-111) I want someone to figure it out to piece together all the hints I’ve been dropping all day long, for years and years even, but no one ever figures it out, and I’m beginning to see why people go mad and do awful things – like the Nazis and Hitler and Timothy McVeigh and Eric Harris and Dylan Klebold did. They all have a lot in common. I bet they felt lonely, helpless, FORGOTTEN, ignored, alienated, irrelevant, cynical and sad.

SILVERMAN: Leonard?

LEONARD: Herr Silverman looks into my eyes until I look back into his. (Pg 114) There have been days when Herr Silverman was the only person to look me in the eye. The only person all day long. It’s a simple thing, but simple things matter. (Pg 110-111) I plead with him using mental telepathy, thinking, “Please just move on. It’s my birthday. I only have a few more hours on this planet. Please. Be kind. Let me off the hook.” The uber-morons roll their eyes and exchange glances. [And] he moves on. (Pg 113) I mostly tune out and wait for class to end so I can be closer to the Leonard Peacock finish line. (Pg 114-115) [But] when the bell rings, I stay seated.

SILVERMAN: (closing the classroom door) So, you wanted to speak with me?

LEONARD: I reach into my backpack and pull out a small box. “This is for you.” It’s the Bronze Star medal my grandfather was awarded for killing some high-ranking Nazi back in World War Two.

SILVERMAN: (Pg 116) Why are you giving this to me?

LEONARD: I don’t know. But I want you to have it, okay? It’s important to me. Maybe you can keep it in your desk drawer and whenever you get to feeling like maybe teaching isn’t worth it anymore you can think of that crazy kid Leonard Peacock who loved your class and gave you [this] as a reward for being an excellent teacher. Maybe it will help you keep going. I don’t know. (Awkward silence)

SILVERMAN: (Pg 117) I’m just going to say this, Leonard, and I hope you won’t take offense. Sudden changes in appearance. You did cut your hair, right?

LEONARD: (Pg 11) I have [had] this signature really long dirty-blond hair that [hung] over my eyes and past my shoulders.

SILVERMAN: (Pg 117-118) Giving away treasured possessions. These are clear signs. Suicidal people often do these things. I’m worried you might be at risk. Are you trying to tell me something here today?

LEONARD: (looking down) Not really. I just wanted you to know how much your class means to me. (to audience) I reach down deep within myself and put on the Hollywood face. (smiles and laughs, then speaks to Silverman) I probably would want to kill myself if I didn’t get to spend time in this room every day. Your class is probably the only thing keeping me alive. (long silence) Can I ask you a personal question? (Pg 119) Why don’t you ever roll up your sleeves or wear a short-sleeve shirt?

SILVERMAN: You noticed that, huh? (pause) (Pg 120-121) Are you sure you’re feeling okay?

LEONARD: Yeah, I’m sure. I’m off to see my guidance counselor right now, actually. So even if I were messed up, super-counselor Mrs. Shanahan’ll fix me straight with a root beer lollipop before I leave the building, so no worries, right?

SILVERMAN: (writing down a number on a piece of paper) If I give you my cell phone number will you promise to call me if you feel like you’re going to kill yourself? Call me first so I can tell you the reason I never roll up my sleeves. I bet knowing the answer to that question will make you feel better, but let’s save it for when you’re feeling really bad.

LEONARD: He’s going above and beyond for me. And h e’s also breaking the rules – giving me his cell phone number. No other teacher in the building would do this. And it makes me so sad to think he’ll be really upset when he hears about my suicide.

SILVERMAN: So will you promise me that you’ll call if it gets worse – before you do anything rash? I’ll tell you the answer if you call. It’s a big secret. But I’ll tell you, Leonard, because I think you need to know. You’re different. And I’m different too. Different is good. But different is hard. Believe me, I know.

LEONARD: (Pg 122) If only the world were full of Herr Silvermans. But it isn’t. I don’t go to Guidance. No root beer lollipop today. I have a mission to complete. (Pg 129) I exit my town’s train station, and this girl I had never seen before stuck a piece of paper in my face.

GIRL: The way, the truth, and the light! Read all about it! Jesus Christ died for your sins! Jesus loves you.

LEONARD: (Pg 174) [NOPE!] Hellfire is not in the plans. Heaven is not in the plans. Uber-nothing. That’s what I want. Nothing. (Pg 197) I end up by the river under this little bridge. (Pg 200-206) I’ve got the gun to my temple now and I’m rubbing the side of my head into the metal O. I push the P-38’s mouth harder and deeper into the soft spot of my skull. It’s like the P-38 is an old skeleton key I’m trying to fit into an old padlock and when I make that connection I’ll hear a click and a door will open and I’ll walk through and be saved. (whispering) “Make the lock click, Leonard. You just have to squeeze your index finger and everything will be okay. The thoughts will stop. No more problems. You can finally just rest. I close my eyes. Time comes to a standstill. (screams) (Pg 208) F****!! I bang my fist against the concrete wall, but no matter what I do, no matter how hard I try, I can’t seem to get my trigger finger to work. I just can’t seem to blow my brains out. (searches frantically through his pockets for the paper that Herr Silverman gave to him, he finds it and dials the number on his cell phone – his breathing is ragged and filled with emotions, but as the phone begins to ring, his breathing quiets)

SILVERMAN: (Pg 209) Hello? . . . (silence) Hello? (silence) (then in a softer voice) Is this Leonard? (Silence) Just tell me where you are, Leonard. I’ll come to you. We can talk. I’ll tell you my secret. I’ll roll up my sleeves for you.

LEONARD: (Pg 211) (in a broken voice) It’s my birthday today. No one remembered. (to audience) It sounds so stupid and pathetic and little-kid whiny that I push the P-38’s barrel into my temple again. (to himself) End this. Just pull the trigger. Make it easier for everyone.

SILVERMAN: Happy birthday, Leonard.

LEONARD: (to audience) Just two words. Happy birthday. It makes me feel like I’m not already gone. Like I’m still here. I lower the P-38 and tell him where I am. ***********

SILVERMAN: (Pg 216) Just give me the gun and everything will be okay.

LEONARD: No it won’t. That’s such a f***** lie! (Pg 41) [I’ve watched adults on the train going to their jobs in the city. They . . . ] just sit there or stand. No one talks. [They] grimly read the paper, angrily poke smartphone screens and barely even blink. I never want to be an adult. (Pg 216) You don’t lie, Herr Silverman. You’re better than the rest. You’re the only adult I really trust and look up to. So tell me something else, okay? Try again. (sarcastically)

SILVERMAN: (Pg 218-219) (steps closer to Leonard, takes off his coat and starts to roll up his right sleeve – he uses his cell phone to light his wrist) Take a look.

LEONARD: (to audience) I don’t see scars or needle marks or anything like that. It’s a tattoo of a pink triangle – what the Nazis used to label homosexuals in the concentration camps. I know because Herr Silverman taught us that. (To Silverman) Who did that to you?

SILVERMAN: I did it to myself.

LEONARD: Why?

SILVERMAN: I tried to be who I thought the world wanted me to be all through high school. Always trying to please everyone else – keeping my true self invisible. It took me 19 years to figure out who I was and another twelve or so months to admit it. I didn’t ever want to forget again. I tattooed my wrist with a symbol. So the answer would always be there. (Pg 220-221) (begins to roll up his other sleeve)

LEONARD: The words are printed in navy blue – simple block letters stacked in two rows. The message to himself and no one else. “First they ignore you, then they laugh at you, then they fight you, then you win.”

SILVERMAN: It’s often attributed to Gandhi. It [makes] me feel strong. [Gives] me hope. [Keeps] me going.

LEONARD: I’m not like you. (raises the P-38 to his temple again) This is me. Right here. Right now.

SILVERMAN: No, it’s not you at all. I’ve looked into your eyes when I lecture. I can tell you get it – you’re different. And I know how hard being different can be. But I also know how powerful a weapon being different can be. How the world needs such weapons. Gandhi was different. All great people are. And unique people such as you and me need to seek out other unique people who understand – so we don’t get too lonely and end up where you did tonight.

LEONARD: (Pg 223) [And then] I tell him everything. Every. Horrible. Stomach-wrenching. Detail. And I’m crying again because I just can’t help it. (Pg 225) (to Silverman) . . . I feel like I’m broken – like I don’t fit together anymore. Like I’ve overstayed my welcome here on Earth and everyone’s trying to give me hints about that constantly. I think that’s why my mom left for New York and why no one wants to talk to me ever. I’m worthless. (looks down at the P-38 and sighs) I can’t even kill myself properly.

SILVERMAN: That’s a good thing . . . That’s a beautiful thing. (Pg 228) Throw the gun in the river, Leonard. rust in the future. Go ahead. Do it. It’s okay. Things are going to get better. You can do the work. (long pause as Leonard considers his options)

LEONARD: I take three quick steps toward the water and throw the P-38 like a boomerang.
```

---

## IC-0362: The Fountainhead

- Title: The Fountainhead
- Author (byline): Ayn Rand
- Work: Not specified
- Publisher: Plume
- Publication date as stated: 2005
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: TOOHEY
- Teaser before the introduction: Yes
- Spoken words (computed): 2481
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ayn Rand
ISBN: 0452286751
Publisher: Plume
Date (Month/Year): 2005
```

### Introduction (context only: never use it for content warnings)

```text
In a not too distant future, fictional columnist Ellsworth Toohey has decided that the only plausible way to compensate for man’s general status of mediocrity is to destroy man’s very concept of greatness. You see, when greatness has no concrete definition, there can be no superiority. Should all men be created equal ??? A society of equality is scrutinized from all angles in: The Fountainhead by Ayn Rand.
```

### Performance text (classify this)

```text
TOOHEY: I shall rule . . . you, the world. It's only a matter of discovering the lever. If you learn how to rule one single man's soul, you can get the rest of mankind.

TOOHEY: It's the soul, Peter, the soul. Not whips or swords or fire or guns. That's why the Caesars, the Attilas, the Napoleons were fools and did not last. We will. The soul, Peter, is that which can't be ruled. It must be broken. Drive a wedge in, get your fingers on it -- and the man is yours. You won't need a whip — he'll bring it to you and ask to be whipped. Set him in reverse — and his own mechanism will do your work for you. Use him against himself. Want to know how it's done? There are many ways. Here's one. Make man feel small. Make him feel guilty. Kill his aspiration and his integrity. That's difficult. The worst among you gropes for an ideal in his own twisted way. Kill integrity by internal corruption. Use it against itself. Direct it toward a goal destructive of all integrity. Preach selflessness. Tell man that he must live for others. Tell men that altruism is the ideal. Not a single one of them has ever achieved it and not a single one ever will. His every living instinct screams against it. But don't you see what you accomplish? Man realizes that he's incapable of what he's accepted as the noblest virtue — and it gives him a sense of guilt, of sin, of his own basic unworthiness. Since the supreme ideal is beyond his grasp, he gives up eventually all ideals, all aspiration, all sense of his personal value. He feels himself obliged to preach what he can't practice. But one can't be good halfway or honest approximately. To preserve one's integrity is a hard battle. Why preserve that which one knows to be corrupt already? His soul gives up its self-respect. You've got him. He'll obey. He'll be glad to obey — because he can't trust himself, he feels uncertain, he feels unclean. That's one way. Here's another. Kill man's sense of values. Kill his capacity to recognize greatness or to achieve it. Great men can't be ruled. We don't want any great men. Don't deny the conception of greatness. Destroy it from within. The great is the rare, the difficult, the exceptional. Set up standards of achievement open to all, to the least, to the most inept — and you stop the impetus to effort in all men, great or small. You stop all incentive to improvement, to excellence, to perfection. Laugh at Roark and hold Peter Keating as a great architect. You've destroyed architecture. Build up Lois Cook and you've destroyed literature. Hail Ike and you've destroyed the theater. Glorify Lancelot Clokey and you've destroyed the press. Don't set out to raze all shrines — you'll frighten man. Enshrine mediocrity — and the shrines are razed. Then there's another way. Kill by laughter. Laughter is an instrument of human joy. Learn to use it as a weapon of destruction. Turn it into a sneer. It's simple. Tell them to laugh at everything. Tell them that a sense of humor is an unlimited virtue. Don't let anything remain sacred in a man's soul — and his soul won't be sacred to him. Kill reverence and you've killed the hero in man. One doesn't reverence with a giggle. He'll obey and he'll set no limits to his obedience — anything goes — nothing is too serious. Here's another way. This is most important. Don't allow men to be happy. Happiness is self-contained and self-sufficient. happy men have no time and no use for you. Happy men are free men. So kill their joy in living. Take away from them whatever is dear or important to them. Never let them have what they want. Make them feel that the mere fact of a personal desire is evil. Bring them to a state where saying ‘I want' is no longer a natural right, but a shameful admission. Altruism is the great help in this. Unhappy men will come to you. They'll need you. They'll come for consolation, for support, for escape. Nature allows no vacuum. Empty man's soul — and the space is yours to fill. I don't see why you should look so shocked, Peter. This is the oldest one of all.

Look back at history. Look at any great system of ethics, from the Orient up. Didn't they all preach the sacrifice of personal joy? Under all the complications of verbiage, haven't they all had a single leitmotif: sacrifice, renunciation, self-denial? Haven't you been able to catch their theme song — 'Give up, give up, give up, give up'? Look at the moral atmosphere of today. Everything enjoyable from cigarettes to sex to ambition to the profit motive, is considered depraved or sinful. Just prove that a thing makes men happy — and you've damned it. That's how far we've come. We've tied happiness to guilt. And we've got mankind by the throat. Throw your first-born into a sacrificial furnace — lie on a bed of nails — go into the desert to mortify the flesh — don't dance — don't go to the movies on Sunday — don't try to get rich — don't smoke — don't drink. It's all the same line. The great line. Fools think that taboos of this nature are just nonsense. Something left over, old-fashioned. But there's always a purpose in nonsense. Don't bother to examine a folly — ask yourself only what it accomplishes. Every system of ethics that preached sacrifice grew into a world power and ruled millions of men. Of course, you must dress it up. You must tell people that they'll achieve a superior kind of happiness by giving up everything that makes them happy. You don't have to be too clear about it. Use big vague words. 'Universal Harmony' — 'Eternal Spirit' — ‘Divine Purpose' — 'Nirvana' — 'Paradise' — 'Racial Supremacy' — 'The Dictatorship of the Proletariat.' Internal corruption, Peter. That's the oldest one of all. The farce has been going on for centuries and men still fall for it. Yet the test should be so simple: just listen to any prophet and if you hear him speak of sacrifice — run. Run faster than from a plague. It stands to reason that where there's sacrifice, there's someone collecting sacrificial offerings. Where there's service, there's someone being served. The man who speaks to you of sacrifice, speaks of slaves and masters. And intends to be the master. But if ever you hear a man telling you that you must be happy, that it's your natural right, that your first duty is to yourself — that will be the man who's not after your soul. That will be the man who has nothing to gain from you. But let him come and you'll scream your empty heads off, howling that he's a selfish monster. So the racket is safe for many, many centuries. But here you might have noticed something. I said, 'It stands to reason.' Do you see? Men have a weapon against you. Reason. So you must be very sure to take it away from them. Cut the props from under it. But be careful. Don't deny outright. Never deny anything outright, you give your hand away. Don't say reason is evil — though some have gone that far and with astonishing success. Just say that reason is limited. That there's something above it. What? You don't have to be too clear about it either. The field's inexhaustible. 'Instinct' — 'Feeling' — 'Revelation' — 'Divine Intuition' — Dialectic Materialism'. If you get caught at some crucial point and somebody tells you that your doctrine doesn't make sense — you're ready for him. You tell him that there's something above sense. That here he must not try to think, he must feel. He must believe. Suspend reason and you play it deuces wild. Anything goes in any manner you wish whenever you need it. You've got him. Can you rule a thinking man? We don't want any thinking men. Peter, you've heard all this. You've seen me practicing it for ten years. You see it being practiced all over the world. Why are you disgusted? You're in on it. You're afraid to see where it's leading. I'm not. I'll tell you. The world of the future. The world I want. A world of obedience and of unity. A world where the thought of each man will not be his own, but an attempt to guess the thought of the brain of his neighbor who'll have no thought of his own but an attempt to guess the thought of the next neighbor who'll have no thought — and so on. Peter, around the globe. Since all must agree with all. A world where no man will hold a desire for himself, but will direct all his effort to satisfy the desires of his neighbor who'll have no desires except to satisfy the desires of the next neighbor who'll have no desires — around the globe, Peter. Since all must serve all. A world in which man will not work for so innocent an incentive as money, but for that headless monster -- prestige. The approval of his fellows — their good opinion — the opinion of men who'll be allowed to hold no opinion. An octopus, all tentacles and no brain. Judgement, Peter! Not judgement, but public polls. An average drawn upon zeroes — since no individuality will be permitted. A world with its motor cut off and a single heart, pumped by hand. My hand — and the hands of a few, a very few other men like me. Those who know what makes you tick — you great, wonderful average, you who have not risen in fury when we called you the average, the little, the common, you who've liked and accepted those names. You'll sit enthroned and enshrined, you, the little people, the absolute ruler to make all past rulers squirm with envy, the absolute, the unlimited, God and Prophet and King combined. Vox populi. The average, the common, the general. Do you know the proper antonym for Ego? Bromide, Peter. The rule of the bromide. But even the trite has to be originated by someone at some time. We'll do the originating. Vox dei. We'll enjoy unlimited submission — from men who've learned nothing except to submit. We'll call it 'to serve'. We'll give out medals for service. You'll fall over one another in a scramble to see who can submit better and more. There will be no other distinction to seek. No other form of personal achievement. Can you see Howard Roark in the picture? No? Then don't waste time on foolish questions. Everything that can't be ruled, must go. And if freaks persist in being born occasionally, they will not survive beyond their twelfth year. When their brain begins to function, it will feel the pressure and it will explode. The pressure gauged to a vacuum. Do you know the fate of deep-sea creatures brought out to sunlight? So much for future Roarks. The rest of you will smile and obey. Have you noticed that the imbecile always smiles? Man's first frown is the first touch of God on his forehead. The touch of thought. But we'll have neither God nor thought. Only voting by smiles. Automatic levers — all saying yes . . . Now if you were a little more intelligent — like your ex-wife, for instance — you'd ask: What of us, the rulers? What of me, Ellsworth Monkton Toohey? And I'd say, Yes, you're right. I'll achieve no more than you will. I'll have no purpose save to keep you contented. To lie, to flatter you, to praise you, to inflate your vanity. To make speeches about the people and the common good. Peter, my poor old friend, I'm the most selfless man you've ever known. I have less independence than you, whom I just forced to sell your soul. You've used people at least for the sake of what you could get from them for yourself. I want nothing for myself. I use people for the sake of what I can do to them. It's my only function and satisfaction. I have no private purpose. I want power. I want my world of the future. Let all live for all. Let all sacrifice and none profit. Let all suffer and none enjoy. Let progress stop. Let all stagnate. There's equality in stagnation. All subjugated to the will of all. Universal slavery — without even the dignity of a master. Slavery to slavery. A great circle — and total equality. The world of the future. Insane? Afraid to say it? Look around you. Pick up any newspaper and read the headlines. Isn't it coming? Isn't it here? Everything single thing I told you? Everything I said is contained in a single word — collectivism. And isn't that the god of our century? To act together. To think — together. To feel — together. To unite, to agree, to obey. To obey, to serve, to sacrifice. Divide and conquer — first. But then — unite and rule. We've discovered that one at last. Remember the Roman Emperor who said he wished humanity had a single neck so he could cut it? People have laughed at him for centuries. But we'll have the last laugh. We've accomplished what he couldn't accomplish. We've taught men to unite. This makes one neck ready for one leash. We found the magic word. Collectivism. Look at Europe, you fool. Can't you see past the guff and recognize the essence? One country is dedicated to the proposition that man has no rights, that the collective is all. The individual held as evil, the mass — as God. No motive and no virtue permitted — except that of service to the proletariat. That's one version. Here's another. A country dedicated to the proposition that man has no rights, that the State is all. The individual held as evil, the race — as God.

No motive and no virtue permitted — except that of service to the race. Am I raving or is this the cold reality of two continents already? Watch the pincer movement. If you're sick of one version, we push you into the other. We get you coming and going. We've closed the doors. We've fixed the coin. Heads — collectivism, and tails — collectivism. Fight the doctrine which slaughters the individual. Give up your soul to a council — or give it up to a leader. But give it up, give it up, give it up. My technique, Peter. Offer poison as food and poison as antidote. Go fancy on the trimmings, but hang on to the main objective. Give the fools a choice, let them have their fun — but don't forget the only purpose you have to accomplish. Kill the individual. Kill man's soul. The rest will follow automatically. Observe the state of the world as of the present moment. Do you still think I'm crazy, Peter?"
```

---

## IC-0363: Free Churro

- Title: Free Churro
- Author (byline): Raphael Bob-Waksberg
- Work: BoJack Horseman [Season 5, Episode 6] On-line Transcript available at
- Publisher: Netflix
- Publication date as stated: Sept 2018
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BOJACK
- Teaser before the introduction: Yes
- Spoken words (computed): 1813
- Already set (do not supply): none

### Source block (context only)

```text
Author: Raphael Bob-Waksberg
Book: BoJack Horseman [Season 5, Episode 6]
On-line Transcript available at
https://transcripts.foreverdreaming.org/viewtopic.php?t=100171&sid=7afdcaa52046b72861d
c250836e290d4
Publisher: Netflix
Date (Month/Year): Sept 2018
```

### Introduction (context only: never use it for content warnings)

```text
Why do our parents matter so much? Well, our parental figures matter because they forge our idea of how the world works, often by accident. They create our sense of how to attach to people, how to navigate, and how to love. And there is no opting out of this influence. In this selection, BoJack has the opportunity to deliver the eulogy for his mother Bea. It was a relationship filled with maternal insults and critical judgments from a woman who believed she was ‘born broken.’

You can hear every last bit of forced levity, resentment, and genuine pain as BoJack tries to find a way to come to terms with Bea’s death, and his feelings or lack thereof. This episode of BoJack Horseman, (Season 5, Episode 6) was met with critical acclaim and was nominated for an Emmy.

Free Churro by Raphael Bob-Waksberg
```

### Performance text (classify this)

```text
BOJACK: So I stopped at a Jack in the Box on the way here, and the girl behind the counter said, “Hiya! Are you having an awesome day?” Not, “How are you doing today?” No. “Are you having an awesome day?”

When people ask how I’m doing, I usually say, “I am doing so great.” But when this girl at the Jack in the Box asked me if I was having an awesome day, I said, “Well, my mom died,” and she immediately burst into tears.

So now I have to comfort her, which is annoying, and meanwhile, there’s a line of people forming behind me who are giving me these real judgy looks because I made the Jack in the Box girl cry. She’s saying, “I’m sorry, I’m so sorry,” and I’m like, “It’s fine. It’s fine.” I mean, it’s not fine but, you know, it’s. . . fine. And I would like to order a Double Jack Meal, and I’ve kinda got somewhere to be, so maybe . . . [inhales]

And the girl apologizes again and offers me a free churro with my meal. And as I’m leaving, I think, “I just got a free churro because my mom died.” No one ever tells you that when your mom dies, you get a free churro.

BOJACK: [clears throat] Anyway, I’m sorry, that’s not part of the. . .[clears throat] All right, here we go. Let’s do this. Beatrice Horseman, who was she? Uh, she was born in 1938. She died in 2018. One time, she went to a parade, and one time, she smoked an entire cigarette in one long inhale. Truly a remarkable woman.

Lived a full life, that lady. Life, right? Goes by, stuff happens. Then you die. But seriously, that’s all I have to say about my mother. No point beating a dead horse, right? So. . . [inhales] Now what? Mom, you got any ideas? Anything? Mom? Nothing to contribute? Knock once if you’re proud of me.

Can I just say how amazing it is to be in a room with my mother, and I can just talk without her telling me to shut up and make her a drink? Hey, Mom, knock once if you think I should shut up. No? You sure? I mean, I don’t want to embarrass you.

Sorry about the closed casket, by the way. She wanted an open casket, but uh, you know, she’s dead now, so who cares what she wanted? No, that sounds bad. I’m sorry. I- I think that if she could’ve seen what she looked like dead, she’d agree it’s better this way. The coroner couldn’t get her eyes closed, so now her face is forever frozen in a mask of tremendous horror and anguish. Or as my mom called it, Tuesday! Tuesday! My mom called it Tuesday.

Here’s a story. When I was a teenager, I performed a comedy routine for my high school talent show. There was this, uh, cool jacket that I wanted to wear. For months, I saved up for this jacket. But when I finally had enough, I went to the store and it was gone. They had sold it to someone else. So, I went home and I told my mother, and she said, “That’s the good that comes from wanting things.” She was really good at dispensing life lessons that always seemed to circle back to everything being my fault.

But then, on the day of the talent show, my mother had a surprise for me. She had bought me the jacket. Even though she didn’t know how to say it, I know this meant that she loved me. Now that’s a good story about my mother. It’s not true, but it’s a good story, right? I don’t have any stories like that.

All I know about being good, I learned from TV. And in TV, flawed characters are constantly showing people they care with these surprising grand gestures. Part of me still believes that’s what love is. But in real life, the big gesture isn’t enough. You need to be consistent, you need to be dependably good. You can’t just screw everything up and then take a boat out into the ocean to save your best friend, or solve a mystery, and fly to Kansas. You need to do it every day, which is so. . . hard.

When you’re a kid, you convince yourself that maybe the grand gesture could be enough, that even though your parents aren’t what you need them to be over and over and over again, at any moment, they might surprise you with something. . . wonderful. I kept waiting for that, the proof that even though my mother was a hard woman, deep down, she loved me and cared about me and wanted me to know that I made her life a little bit brighter. Even now, I find myself waiting.

Hey, Mom, knock once if you love me and care about me and want me to know I made your life a little bit brighter.

I was in the hospital with her those last moments, and they were truly horrifying, full of nonsencial screams and cries, but there was this moment, this one instant of strange calm, where she looked in my direction and said, “I see you.” That’s the last thing she said to me. “I see you.” Not a statement of judgment or disappointment, just acceptance and the simple recognition of another person in a room. “Hello there. You are a person. And I see you.”

Let me tell you, it’s a weird thing to feel at [insert age here] years old, that for the first time in your life your mother sees you. It’s an odd realization that that’s the only thing you wanted all along, to be seen. I was not ready for “I see you.” -- a moment of connection on her way out. But maybe I’m giving her too much credit. Maybe it wasn’t about connection. Maybe it was an “I see you,” like, “You might have the rest of the world fooled, but I know exactly who you are.” That’s more my mom’s speed.

My dad died about ten years ago. My darling mother gave the eulogy. My entire life I never heard her say a kind word to or about my father, but at his funeral she said, “My husband is dead, and everything is worse now.”

“My husband is dead, and everything is worse now.” I don’t know why she said that. Maybe she felt like that’s the kind of thing you’re supposed to say at a funeral. Maybe she hoped one day someone would say that about her. “My mother is dead, and everything is worse now.” Or maybe she knew that he had frittered away all her inheritance and replaced it with crippling debt. “Bad news, you lost a husband, but don’t worry, you also lost the house!” Maybe Mom knew she’d have to sell all her fancy jewelry and move into a home. Maybe that’s what she meant by “everything is worse now.” Is that what you meant, Mom?

You know, the first time I ever performed in front of an audience was, uh, with my mom. She used to put on these shows with her supper club. There were skits and magic acts, and the finale was always a dance my mother did. She had this beautiful dress that she only brought out for these parties. It was so beautiful and sad.

Dad hated the parties. He’d lock himself in the study, but he always came out to see Mom dance. He’d linger in the doorway and watch in awe, as this cynical, despicable woman he married. . . took flight. And as a child who was completely terrified of both my parents, I was always aware that this moment of grace, it meant something. My mother, she knew what it’s like to feel your entire life like you’re drowning, with the exception of these moments, these very rare, brief instances, in which you suddenly remember. . . you can swim.

But then again, mostly not. Mostly you’re drowning. She understood that, too. All three of us were drowning, and we didn’t know how to save each other, but there was an understanding that we were all drowning together. And I would like to think that that’s what she meant when we were in the hospital and she said, “I see you.”

My mom left no instructions for what she wanted me to say. All I know is she wanted an open casket, and her idiot son couldn’t even do that right. I’m not gonna stand up here and pretend I ever understood how to please that woman, even though so much of my life has been wasted in vain attempts to figure it out. But I keep going back to that moment in the ICU when she looked at me, and… “I-C-U.” “I… see… you.” Jesus Christ, we were in the intensive care unit. She was just reading a sign.

My mom died and all I got was this free churro. The s****iest thing about all of this is when that stranger gave me that free churro, that small act of kindness showed more compassion than my mother gave me her entire life. Like, how hard is it to do something nice for a person? This woman at the Jack in the Box didn’t even know me. I’m your son! All I had was you! [inhales]

I have this friend. And right around when I first met her, her dad died, and I actually went with her to the funeral. And months later, she told me that she didn’t understand why she was still upset, because she never even liked her father. It made sense to me, because I went through the same thing when my dad died. And I’m going through the same thing now.

Suddenly, you realize you’ll never have the good relationship you wanted, and even though you’d never admit it, part of you, the stupidest part of you, was holding on to that chance. And you didn’t even realize it until that chance went away.

My mother is dead, and everything is worse now, because now I know I will never have a mother who looks at me from across a room and says, “I see you.” But I guess it’s good to know that there is nobody looking out for me, that there never was, and there never will be. No, it’s good to know that I am the only one that I can depend on. And I know that now and it’s good. It’s good that I know that. So. . . it’s good my mother is dead.

Beatrice Horseman was born in 1938, and she died in 2018, and I have no idea. . .what she wanted. Unless she just wanted what we all want. . . to be seen.
```

---

## IC-0364: A Gaggle of Saints

- Title: A Gaggle of Saints
- Author (byline): Neil LaBute
- Work: Bash: Latterday Plays; Pgs 35-70
- Publisher: Overlook Press
- Publication date as stated: December 1999
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: JOHN, SUE
- Teaser before the introduction: Yes
- Spoken words (computed): 1861
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
Some of the most frightening moments in life are when you realize that a person you love and trust has been putting up a front the whole time: The husband that comes out of the closet. Grandparents who get divorced after being together forever. Discovering you had siblings you didn't know about. These things happen to "normal" people all the time. People are capable of anything.

In Gaggle of Saints, Neil LaBute introduces us to John and Sue, two Mormon sweethearts who tell the story of attending a formal dance in New York City. But it’s what happens after the dance in Central Park that makes the unexpected frightening.

A Gaggle of Saints by Neil LaBute
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

JOHN: . . .and then I saw 'em. Both of them. Those guys. . . (Pg 60-64) They were saying "goodnight. . ." well, not saying it exactly. But kissing. Two grown men, standing in this public park in the middle of New York and kissing like something out of a Clark gable film. Arms around each other, and nothing else in the world matters to these two. . . hands all where they shouldn't be. I mean, come on, I know the scriptures, know 'em pretty well, and this is wrong. (beat) You know, you read about it, right, and you live with it. Don’t love it; don't condone it for the world. Still,live and let live, whatever. But this is flaunting it. I mean, we're in town one night, that's all, one. . . and we got 'a witness this? (pause)

Men old enough to be our fathers clutching at one another like Romeo and Juliet! (beat) I start to feel sick, I mean it, nauseous. Then a last peck on the cheek and one disappears down a trail, headed for the west side. He’s gone. The other one glances around, taking in the night, I guess, big smile up at the moon. . . and he strolls over to this "men's room." 50 yards off. Concrete building, with the steps down into it. Whistling while he goes. . . he was whistling. I don't even stop to think this through but motion the guys to follow me.

I told the guys to hold off. Wait for me to flush him out, make sure no one wanders by. Our friend's legs, I spot, patiently sitting in a stall. Not a care in this world. I slip into the stall next to his, start fumbling with my belt; and like clockwork, this guy's hand comes up under my side of the partition. Pink fingers, wiggling up at me, imploring.

I notice this thin gold band on his little finger, catching the light. (beat) Two minutes later we're standing near the mirrors and sizing each other up. Name’s "Chet," he says, and I don't even bat an eyelash as he moves in, his lips playing across my cheek. I just smile at him. I see his shoulders relax.

Then I let out a whistle that sends him stumbling back. Tim and Dave appear in the doorway. Chet comes back from his fantasies, a flicker in his eyes, realizing no good can come from this. . . and starts babbling. Even got down on his knees and the pleading. Begging. (beat) Probably a VP at some bank and he’s wetting himself like an infant.

My first shot catches him just under the eye and he slams into a sink. With so many of us hitting, tearing at him, it's hard to get off a clean punch but I know I connect a few more times. Tim kicking him long after he's blacked out. . . (pause)

And then it's silence. Not a sound. And then, I’m leaning down, pulling that ring off his pinkie.

(beat) I told you I noticed it. . . And that's how we leave him. . . pause. We all start, giggling, can’t catch our breath we find it all so funny. We slip out, one by one, whooping it up like Indians.

SUE: The phone woke me up. . .

JOHN: We wanted to take the girls out to breakfast. Say they'll be down in fifteen minutes. . . (pause) We waited outside. Dave’s walking around on the curb, talking to himself, and Tim pulls me aside. Wants to why I touched the guy. Let him kiss me. He’d glanced inside and seen it. But I didn't know, didn't have an answer. Isn’t that strange?

SUE: (Pg 65-67) It was so quiet in the lobby as we were leaving. I started tip-toeing out. Isn’t that funny? We met in front of the hotel, and I saw John's face. All cut up like he'd fallen. [He said he was] racing along the fountain out front, balancing on it, and slipped. Scraped himself up and blood on everything. (beat) Silly games. . . (pause) I was eating my French toast, when I notice this glint in my water glass. A spark of light. (beat) John'd slipped a ring in it! A beautiful gold thing. . . I loved him so much at that moment.

JOHN: Happy anniversary

SUE: It was a little big, but fit pretty well. Had this wonderful leaf pattern, all the way around. . . I kissed him there, in front of everybody, and he blushed a bit. We all laughed. I can't tell you what a wonderful weekend we had. . .

JOHN: We did end up taking the Amtrak back up. . . just Sue and myself.

SUE: It was my idea. . .the train. On the way back – I shouldn’t even bring this up – a fight broke out. Well, not really a fight but this argument between a man and his girlfriend. A lot of yelling. She stand ups and starts pulling on her coach and this guy, I mean, just backhands her.

JOHN: (Pg 68) Knocked her up against the window, really hard. He’d given her a bloody nose.

SUE: I could feel John tense up, but the couple was kind of dirty-looking and they seemed like, you know . . . those kind of people. So I whispered to John to “let it go” (beat) and you know what? He didn’t so much bat an eyelash. Just kept holding my hand and playing with the ring on my finger. That made me so happy . . .

JOHN: (Pg 69) And finally, as we tumbled along toward Massachusetts, I could feel Sue fall asleep against my shoulder. All warm. Protected. But not me. . .I couldn't drift off. So I sat up, watching the lights dance by, the moon grinning down. And you know, I started whistling to myself. I did. . .

SUE: I was asleep there on john's arm, but I’d swear I could hear music. . .

JOHN: Not loud, I mean, don't even recall the tune. But I was whistling. . .

SUE: (Pg 70) . . .this beautiful music as I was sleeping. Like the sound of angels calling us home. . .
```

---

## IC-0365: Gas

- Title: Gas
- Author (byline): José Rivera
- Work: Giants Have Us in Their Books, Pgs 35-42
- Publisher: Broadway Play Publishing
- Publication date as stated: June 2014
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CHEO
- Teaser before the introduction: Yes
- Spoken words (computed): 1660
- Already set (do not supply): none

### Source block (context only)

```text
Author: José Rivera
Book: Giants Have Us in Their Books, Pgs 35-42
ISBN: 978-0881455946
Publisher: Broadway Play Publishing
Date (Month/Year): June 2014
```

### Introduction (context only: never use it for content warnings)

```text
It is 2003 . . . the United States has launched a major military invasion of Iraq -- the start of an 8-year conflict that resulted in the deaths of more than 4,000 U.S. servicemembers and hundreds of thousands of Iraqis. Millions of Americans protest the invasion, carrying signs and banners that read “No Blood for Oil.”

What role did oil play in the decision to invade Iraq? We may never know for sure. Saddam Hussein was, after all, a brutal dictator who with weapons of mass destruction and ties to terrorist groups. No, oil did not make the U.S. war against Iraq inevitable – but it was an especially attractive added incentive.

“No Blood for Oil” -- For weeks and weeks, Cheo has received letters from his brother, a soldier stationed in the Saudi Arabian desert. Then one day the letters stop, and Cheo is left unsure if his brother is alive. He begins to question the cost of soldiers as collateral damage and the phrase “No Blood for Oil.”

Gas by Jose Rivera
```

### Performance text (classify this)

```text
CHEO stands next to a pump at a gas station, about to fill his car with gas. He is a working-class Latino.

CHEO: (Pg 35-42) His letters were coming once a week. I could feel his fear. It was in his handwriting. He sat in a tank. In the middle of the Saudi Arabian desert. Wrote six, seven, eight hours a day. These brilliant letters of fear. This big Puerto Rican guy! What the hell's he doing out there? What sense does that make? He's out there, in the Saudi sand, writing letters to me about how he's gonna die from an Iraqi missile. And he's got all this time on his hands to think about his own death. And there's nothing to do 'cause of these restrictions on him. No women, no magazines, 'cause the Saudis are afraid of the revolutionary effects of ads for women's lingerie on the population! Allah would have a cow!

CHEO: There's nothing he's allowed to eat even remotely reminds him of home. Nothing but the time to sit and think about what it's gonna be like to have someone run a bayonet clean through his guts. He's sitting in the tank playing target practice with the camels. Shooting at the wind. The sand in all the food. Sand in his dreaming. He and his buddies got a camel one day. They shaved it clean! Completely shaved it! Then they spray-painted the name of their company, in bright American spray-paint, on the side of the camel, and sent it on its way!

Scorpion fights in the tents! All those scenes from Apocalypse Now in his head. Marlon Brando decapitating that guy and Martin Sheen going nuts. That's what fills my brother's daily dreams as he sits out there in the desert contemplating his own death.

The Vietnam Syndrome those people are trying to eradicate. His early letters were all about that. A chronicle. His way of laying it all down, saying it all for me, so I would know what his last days and months, and seconds were like. So, when he got offed by an Iraqi missile, I would at least know what it was like to be in his soul, if just for a little while.

He couldn't write to save his life at first. Spelled everything totally, unbelievably wrong. "Enough": e-n-u-f. But with time, he started to write beautifully. This angel started to come out of the desert. This singing angel of words. Thoughts I honestly never knew he had. Confessions. Ideas. We started to make plans. We started to be in sync for the first time since I stopped telling him I loved him.

I used to kick his a**! It wasn't hard or nothing. That's not bragging, just me telling you a simple truth. He was always sick. Always the first to cry. He played drums in a parade back home. He couldn't even play the stupid instrument, he was so uncoordinated. Spastic. But they let him march in the parade anyway -- without drumsticks. He was the last guy in the parade, out of step, banging make-believe drumsticks -- playing air drum for thousands of confused spectators! Then he got into uniforms and the scouts. But I knew that was just its cover anyway. He didn't mean it. Though after he joined the army and was in boot camp, he took particular delight in coming home and demonstrating the fifty neat new ways he learned to kill a guy. One day he forgot he weighed twice my weight and nearly snapped my spine like a cucumber! I thought, in agony, "Where's my bro? Where's that guy I used to kick around?

The first one to cry when he saw something beautiful. The first one to say 'I love that' or 'I love Mom' or 'I love you.''' He never got embarrassed by that, even after I got too old to deal with my little brother kissing me in front of other people. Even later, he always, always, always ended every conversation with, "I love you, bro." And I couldn't say, "I love you" back, 'cause I was too hip to do that.

But he got deeper in it. The war thing. He wrote to say I'd never understand. He's fighting for my right to say whatever I want. To disagree. And I just love how they tell you on the news the temperature in Riyadh, Saudi Arabia! Like I care! And a couple of times he called me collect from Saudi! I said collect! And I told him if Saddam Hussein didn't kill him, I would!

He told me about troubles with his wife back home. He'd just gotten married a month before shipping out. He didn't really know her and was wondering if she still loved him. My brother always loved ugly women. It was a thing with him. Low self-esteem or something. Like he couldn't love himself and didn't understand a woman that would. So, he sought out the absolute losers of the planet. Love! He didn't know another way. Then he met a girl who on their first date confessed she hated spics -- so my brother married her! This racist looked him in the eye, disrespected his whole race to his face, and my brother says, "I do."

Last night somebody got on TV to say we shouldn't come down on rich people ‘cause rich people are a minority too, and coming down on them was a form of racism! And I thought, they're afraid of class warfare, and they should be! And the news showed some little white punk putting up flags all over this town in California and this little twerp's story absorbed twenty minutes of the news -- this little, blond Nazi kid with a smile full of teeth -- and the protests got nothing.

And this billboard went up in my town showing Stalin, Hitler, and Hussein, saying we stopped him twice before we have to stop him again! This billboard was put up by a local newspaper! The music, the computer graphics, the generals coming out of retirement to become media stars. And we gotta fight NAKED AGGRESSION -- like this president should come to my neighborhood if he wants to see naked aggression!

I never thought the ideas in the head of some politician would mean the death of my brother and absolutely kill my mother. I'm telling you, that woman will not survive the death of my brother no matter how much she believes in God, no matter how much praying she does. But I keep that from him. I write back about how it's not going to be another Vietnam. It's not going to be a whole country that spits on you when you come back. That we don't forget the ones we love and fight for us.

Then his letters stopped. I combed the newspapers trying to figure out what's going on over there, 'cause his letters said nothing about where he was. He wasn't allowed to talk about locations, or troop size, or movement, 'cause, like, I was going to personally transmit this information to the Iraqi Ministry of Defense! I thought about technology the new Iraq has that was made in the United States, that could penetrate a tank's armor and literally travel through the guts of a tank, immolating every living human soul inside, turning human Puerto Rican flesh into hot screaming soup, the molecules of my brother's soul mixing with the metal molecules of the iron coffin he loved so much. I couldn't sleep. My mother was suicidal. Why wasn't he writing?

The air war's continuing. They're bombing the hell out of that country! And I find myself ashamed. I think, "Yeah, bomb it more. Level it. Send it back to the Stone Age. Make it so every last elite Republican Guard is dead. So my brother won't get killed." For the first time in my life, I want a lot of people I don't hate to die 'cause I know one of them could kill the man I love most in this messed up world.

And I'm sick. I'm sick of rooting for the bombs. Sick of loving every day the air war continues. Sick of every air strike, every sortie. And being happy another Iraqi tank got taken out and melted, another Iraqi bunker was bombed, another bridge can't bring ammunition, can't deliver that one magic bullet that will incapacitate my brother, bring him back a vegetable, bring him back dead in his soul, or blinded, or butchered in some Iraqi concentration camp. That the Iraqi that would torture him won't live now 'cause our smart bombs have killed him in his sleep! They actually got me wanting this war to be bloody!

(beat)

Last night the ground war started. It started. The tanks are rolling. I find my gut empty now. I don't have thoughts. I don't have dreams. My mother is a shell. She has deserted herself and left behind a blathering cadaver, this pathetic creature with rosary beads in her hands looking up to Christ, and CNN, saying words like "Scud," "strategic interests,"" collateral damage," "target rich environment" -- words this woman from a little town in Puerto Rico has no right to know. So, I fight my demons. I think of the cause. Blood for oil. I NEED MY CAR, DON'T I? I NEED MY CAR TO GET TO WORK SO I CAN PAY THE RENT AND NOT END UP A HOMELESS PERSON! DON'T I HAVE A RIGHT TO MY CAR AND MY GAS? AND WHAT ABOUT FREEING DEMOCRATIC KUWAIT?! (beat)

So, I wait for a sign, anything, a prayer, any sign, I'll take it. Just tell me he's okay. Tell me my brother's gonna kill well and make it through this alive. He's gonna come home and he's gonna come home the same person he left: the spastic one who couldn't spell. . . the one who couldn't play the drums.
```

---

## IC-0366: Geometry of Despair: Venn Diagram

- Title: Geometry of Despair: Venn Diagram
- Author (byline): David James Poissant
- Work: The Heaven of Animals, Pg 124-139
- Publisher: Simon and Schuster
- Publication date as stated: March 2014
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: RICHARD, LISA, PAM
- Teaser before the introduction: Yes
- Spoken words (computed): 2006
- Already set (do not supply): none

### Source block (context only)

```text
Cut from
Author: David James Poissant
ISBN: NSDA Approved Website
https://www.chicagotribune.com/news/ct-xpm-2006-10-29-0610290005-story.html
Publisher: The Chicago Tribune
Date (Month/Year): October 29, 2006
Also published in
Book: The Heaven of Animals, Pg 124-139
ISBN: 978-1476729978
Publisher: Simon and Schuster
Date (Month/Year): March 2014
```

### Introduction (context only: never use it for content warnings)

```text
Geometry of Despair: Venn Diagram by David James Poissant
```

### Performance text (classify this)

```text
RICHARD: Every Wednesday, after dinner, Lisa and I fight the traffic to the nondenominational church across town. Here, for an hour, a dozen of us sit in a circle telling our same sad stories. Each week, Pam, our counselor, reminds us that it isn't a competition, that the goal of group therapy is not to outdo each. Hardship, she assures us, cannot be measured. But validation awaits those who tell the best stories.

What it comes down to is the following equation: If a train leaves Chicago at 60 miles an hour and another train leaves Atlanta at 80 miles an hour, when they both collide in Kentucky and everybody's babies die, who gets to be the saddest?

RICHARD: Every Wednesday [for an entire year] . . . There's Dot and Drew, whose son was decapitated when he tried to drive home after too many tallboys. Granted, a tragedy, but at least they had him for 18 years. And, hey, if they'd been better parents, who knows?

One week, a weepy, mascara-stained wreck of a woman stops by. She introduces herself as Jenna, tells us her story, and, for a moment, we have a winner. Her 3-month-old dies without explanation, and it isn't until a year later, that her husband admits to shaking the baby. In this way, three becomes two, then one.

Still, my wife says, it's not the same. Jenna has someone she gets to be mad at. Jenna has somebody she can blame. It's like when you're in grade school, Lisa says, and your friend gives you a present, then takes the gift back, only, here, it's God who's the Indian giver.

With SIDS, the despair isn't tied to regret or what-ifs or whose fault. With sudden infant death syndrome, the only thing you want to know--after you wake with the shock that you slept through the night, after you sit up and consider the silence; after you swallow your paranoia and go to the baby, only to feel the warm rush of panic flooding your chest, after the touching, the holding, the shouting, the signing, right here, on the dotted line--after it all, the only thing you want to know is why?

It's a question we ask each Wednesday, a question for which there is no answer.

*****

RICHARD: The divorce rate for a couple who loses an infant child is 75 percent. Most couples split up inside of a year. Our own one-year mark [is now] just two weeks away, I've decided that Lisa and I are no exception. It's not that we've stopped loving each other, only that every time I look into Lisa's eyes, all I see is my little girl. The same goes for Lisa. The miracle, really, is that we've lasted as long as we have.

Lying in bed one tired Wednesday night after group, we consider the possibility of separating. It isn't the first time the subject's come up. Lisa hasn't bothered to wash her face before bed, and her eyes are still red and puffy.

LISA: You don't have to go, you know. (takes his hand. She’s exhausted)

RICHARD: I can't face Lisa when she is crying. But, on Wednesday nights, with no emotion left, we can talk about my leaving like strangers discussing the weather. (to Lisa) Actually, I kind of think I do.

LISA: We could figure something out.

RICHARD: No. Not really. You know that. Don't you? (rubs the back of her hand with his thumb).

LISA: I'm just saying, there's got to be a solution.

RICHARD: But there isn't. What happened, it's going to haunt us as long as we're together.

LISA: (voice cracking) Maybe if we keep going to group ...

RICHARD: (to audience) She sinks deeper into the covers, lets go of my hand. Beside me, she suddenly looks very small. (to Lisa) I'd still go with you. I'm not saying we should to get divorced. I'm just suggesting some time apart, a trial separation.

LISA: (Bitterly) Right. Because those always have such happy endings . . . You need time apart. Not me. You. You don't know what I need.

RICHARD: What do you need?

LISA: I don't know.

RICHARD: Both of us are silent for a minute. When I speak again, I choose my words with care. (to Lisa) I just think that maybe I need to leave for a while, you know? Get some perspective. Figure things out.

LISA: (her eyes dancing with anger, she turns on him) Do you ever stop long enough to hear yourself speak? Do you even listen to the crap that comes out of your mouth? Why can't you get this through your thick skull? There's nothing to figure out. You keep saying you want to figure stuff out, but what does that mean? It's not an equation, Richard. It doesn't balance on both sides. No matter how many ways you try to solve for X, it won't come out even. You'll wind up with less than you started with, every time."

RICHARD: I don't want to be the one to cry first, but, suddenly, I am.

LISA: You can't escape what's happened by leaving this house. The only thing you escape by leaving here is me."

*****

RICHARD: Have you ever been to a baby's funeral? There's an absurdity to the pageantry: the miniature casket, the floral arrangements done up in pastels. I don't remember anything the minister said. I only remember I couldn't breathe.

Friends and relatives followed us home after the funeral. "You shouldn't be alone right now," everyone said. Lisa nodded, wearing a smile I'd never seen before and haven't seen since. She was determined to do whatever everyone thought was best. In the midst of all this, Lisa and I started fighting. I wanted to be left alone. Lisa liked the company. I couldn't tell you what was said, but the argument escalated quickly, our voices competing with the din of the crowded living room. I screamed something. Lisa screamed something back. And then ours were the only voices left. In my mind, I was a bird with a broken wing, the neighborhood cats closing in. (to those gathered) Please, go away. Our baby just died. Please. Leave us alone.

LISA: (snaps) Why do you care? You never wanted her anyway. It's your fault! (crying) You didn't want her and she died!

RICHARD: Lisa collapsed into me, pressed her face to my chest, heaving. And, in that moment, I hated my wife. Her very touch repulsed me.

*****

RICHARD: It's true though, what Lisa said. The pregnancy was not what people now call "planned," and I hadn't wanted the baby, not at first. The high school is where we met, where I'd been teaching geometry to teenagers for 10 years. Lisa was the new biology instructor in town., A month after the wedding, Lisa gave me the news.

LISA: (bubbling with happiness) Well, aren't you excited?

RICHARD: Words tumbled around in my brain, all the words I knew I should say, the words you use for just such an occasion, but none found their way to my tongue.

LISA: (happiness gone) Fine.

RICHARD: Within days, though, my attitude changed. Soon enough, Lisa could see that I wanted the baby just as much as she did. Sure we had intended to wait a little longer, but so what? We were having a baby! I was going to be a father! Our daughter was born in June and we named her just that: June.

It was only after June died in July that the subject of my initial reluctance resurfaced. Lisa never mentioned it again, not after the outburst following the funeral, but it stayed with us, a green cloud hanging low in the house. When we fought, I felt her holding back, and, with every argument, I waited--am waiting still--for her to throw the accusation back in my face, as though death were a thing I wished upon our daughter when she was still in the womb.

*****

RICHARD: I was the one who discovered June. It's why I don't sleep well at night, why morning sends me rocketing to the cradle that's no longer there, that, for weeks, held only a pillow, a pacifier, a yellow stuffed duck.

At first, Lisa wouldn't let me disassemble the cradle. So, one Saturday, when I knew she would be out for a while, I took the thing apart, packed the pieces into a box, labeled the cardboard with black Magic Marker, and carried the box up to the attic. When Lisa got home, [she] stopped, surveyed the room, and, for the longest time, stood very still. “What's wrong," I asked, knowing full well the thing Lisa was missing.

LISA: (quietly) Nothing.

RICHARD: Like everything else, it was easier to say nothing at all.

*****

RICHARD: [This] Wednesday, we go to group as usual. It is to be my last night with Lisa. By morning, I've decided, I will be gone. Pam opens with the usual prayer

PAM: Lord, grant us peace. Help us rejoice in the hope of your glory. And help us rejoice in our sufferings, because we know that suffering produces perseverance, perseverance character, and character the hope that springs eternal. Amen.

RICHARD: Pam asks who would like to share, and, immediately, Lisa raises her hand. I know that she is going to tell everyone that tomorrow marks the one-year anniversary of June's death. Before I know what I'm doing, I stand. My chair tips back, falls to the floor behind me. (bellowing) Don't you get it? You people are so superstitious! You keep looking for reasons and meaning and signs! But the truth is, it doesn't mean anything! None of it means anything! There's no good reason for any of it. It's all just coincidence and bad luck and chance. Our kids are dead. We're not special. We're just unfortunate.

When I look up, Pam is in front of me. She places a hand on my shoulder, and, without meaning to, I fall to my knees.

PAM: You're angry. But, I promise you, it gets easier. God will not give you more than you can bear.

RICHARD: A hand touches my face and I can tell, without looking, that it's Lisa's. The words are lost on me. But the sense of touch stays with me, even after I've left the church.

[That night] I fall right to sleep. It's not the same sleep as the last few hundred nights, that anxious, unchained sleep, so that night finds me in the attic, alone with the toys and the dresses and the little white shoes. Instead, nodding off, I feel something holding me down, heavy as light, silent as summer rain. It's like leaving purgatory at last, like sleeping the quiet sleep of the dead.

*****

RICHARD: The next morning I wake, look at the clock. It's nearly 9, impossible, now, to make my escape without causing a scene. I head downstairs, drawn by the smell of coffee. I pause on the bottom step, consider, again, the notion of leaving just to see what I will feel. But, at the thought, I feel neither sorrow nor relief, only the sweet tug of indecision. In the kitchen, Lisa stands at the window. She is still in her bathrobe, a mug of coffee in one hand, the curve of her neck cradled in the other.

LISA: Coffee?

RICHARD: (to Lisa) Yes, please. Thank you. (to audience) Lisa moves to the cupboard, the stove, returns with a second cup. I reach out and the mug is hot in my hand. I twist the mug around, hold it by the handle. (to Lisa) Lisa, I don't want to go. (to audience) When I hear myself say it, I know it is true. Because it would be the easiest thing in the world to walk out that door. Because, in the end, it doesn't matter which one of us has suffered most, or what has been said, or how we've chosen to manage our sadness.

How do you graph the geometry of despair? Is sorrow, at its heart, a line or a circle? And what is a circle but a line that can't let go? Each of us charts our own path across sadness. Somehow, Lisa and I have met in the middle. At its midpoint, grief is a desert, and it's a long hike back to the basin. I take Lisa into my arms. "Stay," she says. And it is as if there was never the need for a choice. "Stay," she says, and I do.
```

---

## IC-0367: George Orwell’s 1984

- Title: George Orwell’s 1984
- Author (byline): Not specified
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: Sept 1963
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: LOUDSPEAKER, MESSENGER, WINSTON, COFFEE VENDOR, GUARD, O’BRIEN, JULIA, BIG BROTHER’S VOICE, TOGETHER, BIG BROTHER’ VOICE, GOLDSTEIN’S VOICE, SYME, JULIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1610
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
Here’s the thing: 2019 looks a lot like 1984. And we’re remarkably comfortable with it. For starters, it’s hard to ignore the similarities between Big Brother and Donald Trump who, for some, commands a similar unwavering fealty. Critics are comparing recent attacks on “fake news” to George Orwell’s book 1984. And I quote, “What you’re seeing and what you’re reading is not what’s happening.” In July of 2018, President Trump criticized the media and publicly announced that people should not believe what they see or what they read.

What’s more, I can ask Siri to order a pizza, ask Google to play my favorite song or have Alexa turn on the air-conditioning. Yes, and with the power of facial-recognition, some fear that Big Brother can actually track you. Leading to California’s recent ban on such technology. It’s 2019 . . . How much is 2 + 2 today?

George Orwell’s 1984 adapted by Robert Owens; Wilton Hall, Jr and William Miles, Jr.

(Pg 12-13) [A messenger enters, carrying an armful of manila folders stuffed with papers]
```

### Performance text (classify this)

```text
Adapted by Robert Owens; Wilton Hall, Jr and William Miles, Jr.

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

## IC-0368: The Glory Box (from Body Blows – Six Performances)

- Title: The Glory Box (from Body Blows – Six Performances)
- Author (byline): Tim Miller
- Work: Body Blows – Six Performances, Pgs 203-241
- Publisher: University of Wisconsin Press
- Publication date as stated: Feb 2002
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: TIM, ALISTAIR, MOM, SCOTT, MEN, OFFICER, COP
- Teaser before the introduction: Yes
- Spoken words (computed): 2477
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tim Miller
Book: Body Blows – Six Performances, Pgs 203-241
ISBN: 978-0299176846
Publisher: University of Wisconsin Press
Date (Month/Year): Feb 2002
```

### Introduction (context only: never use it for content warnings)

```text
The year was 1999 and the issue of gay marriage was just surfacing in the United States. Some states began to recognize and re-define marriage . . . others were completely opposed to the idea. The U.S. Government remained silent on the issue.

Now imagine if your partner was from another country. The struggles of accepting yourself and being accepted by society as a gay man in a committed relationship is compounded by an immigration system that doesn’t recognize marriage rights of gay couples.

Glory Box by Tim Miller
```

### Performance text (classify this)

```text
TIM: (Pg 210) (to audience) My partner Alistair is from Australia. (Pg 216-217) [He]and I were moving my mom's hope chest recently into the house where we live in Venice Beach.

(straining against the weight of the chest, to Alistair) Damn, this thing weighs a ton! Did your mom have a hope chest?

ALISTAIR: Hmmm. No, she didn't have a hope chest, but she did have a glory box. I think that's the same thing.

TIM: A what?!? You've got to be kidding, right? You really call them GLORY BOXES?

ALISTAIR: Well, of course. What's so strange about that?

TIM: (to audience) Now that's more like it! Glory box! This changes everything. A glory box transforms a bland Southern California maiden into a resplendent Australian Joan of Arc astride her glory box! I've decided that I need a glory box right now in my life -- because Alistair and I are going through a hard time trying to stay together in a country that doesn't want us -- and I'm going to gather the things I need and put them into my glory box and make our future happen!

TIM: (Pg 210-211) (to audience) I'm going to keep in it all kinds of good things my culture gave me as a young gay boy to prepare me for my queer life ahead -- the gay-positive role models, the encouragement of gay relationships, the after-school programs . . . HMMM.

Well, since I actually didn't get any of those positive things, instead I'll put in the glory box the things I did get. I'm going to put in that glory box the hundreds of times I was called a sissy or faggot as a kid. I'm going to put in that glory box the thousands of signals I received from my culture that told me my relationships with other men aren't worth s*** and would never be acknowledged. (fades into a memory of when he was 5-years-old) ******

TIM: When I was a kid, I was endlessly fascinated with this hope chest. Even the words themselves were a mystery. HOPE CHEST. I took these words literally. I was sure that they referred to an actual part of the body. If I looked in an anatomical reference book, I would see that HOPE CHEST was behind the sternum and to the left of the heart. We all know it's there. I imagined that this was the place inside us, a place where we could put the things we hoped for. I floated this notion out to my mom one afternoon. (to Mom) Mom?

MOM: (Pg 213) Yes, dear.

TIM: Is a hope chest a place inside me? A place where I put things I hope for? (to audience) My mom was preoccupied with her ironing and didn't want to entertain the queries of her young queer son, but she did her best.

MOM: Why, no, dear. A hope chest is something that was given to me when I was a girl. It was a special chest for me to put the things that I would need when I was married.

TIM: This was not the answer I had hoped for. This seemed to say that the hope chest was for practical things, like dishes and linens. "What kind of things?"

MOM: Oh, you know, practical things, like dishes and linens.

TIM: (to audience) This was sounding worse by the minute. I gave her one last chance. (to Mom) Didn't you ever put things you hoped for in there?

MOM: Hmm. Well . . . yes . . . I always hoped that I would have a good little boy like you, and here you are. Maybe the little girl that you will one day marry already has a hope chest and she's putting things in it to prepare for your marriage! Isn't that a lovely thought?

TIM: Eeew. I hate girls! I'll never get married.

MOM: You do not hate girls and you will too get married. Now, darling, mother's busy. Why don't you go and have a graham cracker? ****** (flash to the present day at a customs-immigration checkpoint) ******

TIM: (Pg 217-221) Now I'm in the future waiting outside of Immigration and Passport Control at Los Angeles International Airport. I'm waiting for Alistair to get through U.S. Customs. “What if they don't let Alistair into the country?" I'm being mugged by this thought. "What if they don't let Alistair into the country?" How can this man trust me so? How can he be so crazy to link his life with mine? Doesn't he know what damaged goods I am? Someone should tell him! Doesn't he know how scarred I am by what happened to me when I was nine years old?

****** flash back ******

TIM: It was a day of judgmental Twinkies being smashed in my face. I was walking down Russell Street with my friend Scott. We walked by a house that was widely regarded as the most tasteful in our neighborhood, much respected for its impressive series of ceramic elves decorating the winding walkway to the front door!

SCOTT: When I grow up, I'm going to marry that cute girl in our class Gail Gardener and we're gonna live in that house with the ceramic elves.

TIM: (to audience) Scott looked at me as if he thought he deserved a ninety-nine and a happy face on a spelling test. This was a new subject and I sensed that it meant trouble. I bought some time and walked silently along, my Lost in Space lunch box clanking against my leg. Next to my thermos was a special treat: a Twinkie in its crisp, confident plastic wrapper. I knew I was making a mistake before I even opened my mouth. (to Scott) But, Scott, when I grow up, I want to marry you and live in the house with the ceramic elves!

SCOTT: What! Boys can't get married to each other. Everybody knows that.

TIM: Why not?

SCOTT: They just can't.

TIM: (to audience) Scott pushed me hard with both hands, knocking me into the deep dusty ivy of my Congregationalist minister's front yard. Scott jumped on me, looking around to see if anyone had heard me ask him to marry him.

SCOTT: Take it back! Say you don't want to marry me and live in the house with the elves!

TIM: I won't take it back!

SCOTT: Take it back, or I'll give you an Indian burn.

TIM: (to audience) He pinched my side hard and then grabbed my wrist with both hands and twisted in opposite directions. I screamed.

SCOTT: Do you take it back?

TIM: I won't take it back! (to audience) My lunch box had fallen open near my head, revealing the Twinkie in all its cellophane splendor. Scott got a horrible idea and grabbed the Twinkie in his little fist.

SCOTT: Take it back or I'm going to jam this Twinkie in your throat and kill you!

TIM: I won't take it back! (to audience) The strength of my high-pitched voice surprised me. (to Scott) When I grow up, I'm going to marry you and live in the house with the ceramic elves! (to audience) Scott shoved the Twinkie into my mouth and held his small dirty palm over my lips. I exploded with cellophane and Twinkie goo. Now, I knew I'd reached my Twinkie limit and I would have to take it back. Fortunately, my oldest brother had just taught me the week before a special trick. Whenever anyone is tormenting you and wanting you to be untrue to yourself and take something back, all you have to do is cross your fingers and put them behind your back. This erases it. (crosses fingers behind back; to Scott) Alright! I take it back. (to audience) Scott got off of me. He looked so strange. He kicked me, grabbed his math book and Bonanza lunch box, and stormed off to school and the rest of his life filled with petty disappointments and three wives who would fear him. (Don't ask me how, I just know!)

I lay there on my back, pinned to the earth. Surrounded by primordial ivy dust and Twinkie. (holds crossed fingers up to the sky) The crossing of those fingers negated my "I take it back," my one triumph over his small tyranny. I held them up to the hot California sun, and as I repeated the words they gathered steam inside me. I will never take it back. I will never take it back. ***** (flash forward to Customs and Immigration) *****

TIM: (Pg 233) (steps into scene and speaks to Allistair) I promise you, it'll be okay. Why wouldn't they let you in? We're not doing anything wrong. We have the visa. We have the affidavit of support. I got a feeling this is gonna be fine. Trust me. (puts hand gently against Allistair’s cheek, then notices, as if for the first time, his hand) ******* flash back to a memory*******

TIM: (to audience) My hands. . . my hands . . . My hands have been slapped a lot in my life. My hand got slapped when I reached into the cookie jar for just one more. My hand got slapped when my first boyfriend was queer-bashed when I was eighteen. They yelled at him "Die Faggot Die" as they stabbed him nine times in the neck with an ice pick outside of a gay bar in Garden Grove, California. My hand got slapped when certain right-wing congressmen said that no lesbian or gay artists should be able to raise their voices in America. ******* another flash of memory – Bozeman, Montana 1997 *******

TIM: (Pg 234) We're here in Bozeman, Montana. It's 1997 Lesbian and Gay Pride Weekend. BIG SKY PRIDE! I am here to perform for Montana Pride. (Pg 235-236) Two men in a pickup with a gun rack in the back window pull up and stop next to me. I know what's coming. I don't have to call the psychic friends network. What's coming is so pre-dictable. What's coming are "F's."

MEN: Faggot. Fruit. Fairy. Freak.

TIM: They're predictable, but they're scary too, like an angry dog straining at its leash. I know that those F's were usually followed by something more concrete -- a rock, a bottle, maybe even a piece of concrete. Sure enough, a half-empty family-size bottle of Colt 45 leaves the passenger-side window. It made a graceful arc and hit me direct on my right hand. Hot blood dripping down my fingers. The bottle bounced and shattered at my feet. It's not too bad, five or six stitches tops, I just hope the guns stay in the gun rack.

I would like to say that at this moment I became homo superhero. I would tear off my clothes and instead of my vulnerable naked flesh, there would be an ugly superhero unitard costume. I would jump on the cab of their truck, kick the windshield in, and drag these two a**holes across the broken glass. But I didn't do any of those things. I'm not strong enough, or dumb enough to do that. I just bowed my head and walked quicker, a deer frozen in the oncoming headlights. Well, the light changed and the men in the truck lost interest in me. They threw one or two more F's and then went on their way. It's not enough that our country has tried to destroy [us], these men in the truck still want to stick our hands in the frying pan, hold our hands to the flame as I cross a beautiful street in Montana made ugly by these men's hate.

****** return to Customs and Immigration ******

TIM: (Pg 238-241) Alistair is next in line at Customs. He makes a shy smile and winks as he finally approaches the immigration officer and hands her his passport. She runs it through the scanner without even looking at him, and then looks through its pages.

OFFICER: Business or pleasure, Mr. McCartney?

ALISTAIR: I'm a student (shifting from one foot to the other) I'm here for study -- to do an MFA in creative writing at Antioch University in Los Angeles.

TIM: The immigration officer suddenly looks down at her computer screen. It's not a big look, but it's enough for me to know something bad is about to happen. She gestures to the armed immigration officer standing nearby, then looks directly at Alistair and says . . .

OFFICER: There's an irregularity in your request for a student visa. We have reason to believe that you have developed significant ties to an American citizen and that you will be a high risk for not leaving the U.S. at the end of your studies. You are being denied entry and will be returned to Australia on the next plane. Please pick up your belongings and go with this officer.

TIM: I can't breathe. I'm suddenly in a country that has no air for us. I tell myself I have to do whatever it takes to get one more breath. (gasping, he approaches the officer) Is there a problem here? Mr. McCartney is my . . . friend. I'm also his sponsor for his student visa.

COP: Please step back. Now, sir.

TIM: (to cop) You don't understand, we're together. (to audience) Big Cop is getting angry.

COP: (shouts) Look, buddy, back off now or you're going to find yourself in big trouble.

TIM: I feel every moment I have been pushed around by cops, every time I have had a bottle thrown at me, every time I had felt my love for another man be s***-on by my country. This isn't happening.

Little Cop has a choke hold on Alistair and is dragging him away, pulling him toward a strange door covered in smoked glass. Big Cop has got me. (to cops) You a**holes, he's my lover, my partner, my husband. You can't do this. I'm an American citizen. I have rights! You can't do this. (to audience) The doors shut on Alistair. They are dragging me away. The woman officer at her computer terminal regards this scene with annoyance. She glares at the U.S. citizens who have already made it through the lines, their mouths agape with the shame that comes when you watch injustice and do nothing. But all she says . . .

OFFICER: Next. ******* (returns to the hope chest/glory box) *******

TIM: I have one more thing in that hope chest. In that glory box. There's a compass inside. I hope that this compass will help me and Alistair avoid a future like that at some airport in America. ut I have an even better compass inside me too. Right here in my hope chest. It's right where I knew it was. I was right when I was five. There is this place inside us. It's right here, behind my sternum and to the left of my heart. It's the compass that led me to love another man -- a man from another country. It led me around the world to find him.

I will use my compass to find a place where when two men kiss, the cop on the beat or the airplane captain will nod, smile, see us as the tin-canned newlyweds we are. I want to use this compass to find my way to a place where our hands won't be pulled apart. I want to use this compass to find my way to a place where two men or two women can come together and pledge their lives, their hopes, their fears, their failures, their myths, their memories and their bodies the sight of the gods, the goddesses, the state, the little children, and even my mom. I don't want to have to leave my country to find this place. I don't want to be forced to leave my pathetic, frustrating, hate-filled, when-will-we-grow-up and ever beloved country. I may even want to use this compass to find that house with the ceramic elves. If I want to. I'm going to use this compass to find my way home. To find my way . . . to him.
```

---

## IC-0369: The God File

- Title: The God File
- Author (byline): Frank Turner Hollon
- Work: Not specified
- Publisher: MacAdam / Cage
- Publication date as stated: August 2003
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: GABRIEL, THE FEAR FILE, THE CANCER FILE
- Teaser before the introduction: Yes
- Spoken words (computed): 1784
- Already set (do not supply): none

### Source block (context only)

```text
Author: Frank Turner Hollon
ISBN: 978-1931561440
Publisher: MacAdam / Cage
Date (Month/Year): August 2003
```

### Introduction (context only: never use it for content warnings)

```text
What if everything you believed about God fell apart in a single moment? When Gabriel Black’s life collapses into a prison cell, fear and silence fills his mind and belief in God is less than comforting. So, Gabriel starts keeping track, collecting his thoughts and memories in a box he calls “The God File.” There must be some proof of God even in the brokenness of his life.

When everything is taken from you, is faith something you lose, or something you fight for?

The God File by Frank Turner Hollon
```

### Performance text (classify this)

```text
GABRIEL: (Pg 138) (praying) “Now I lay me down to sleep, I pray the Lord my soul to keep. If I should die before I wake, I pray the Lord my soul to take.”

(Pgs 6-13) (to audience) So you say you believe in God? So you say that you see evidence that God exists, and not only does he exist, that he cares about you? (bitterly) Spend almost 22 years in a maximum-security Alabama penitentiary for a murder you didn’t commit and then tell me God exists.

I was here 3 months before my mind would let me read, then I started reading anything with words. Anything. I read a book about a man with cancer. He was a doctor with a supportive wife and blue-eyed kids. His cancer was cured [and] he wrote about his proof of the existence of God and signs that the Lord had cured his cancer. It must be pretty easy to see signs of God’s existence when you’re a rich doctor with a wonderful wife and children, cured of cancer and writing stories about pretty visions.

[But] it would really be a test to find this evidence in a nasty place like this, with no real freedoms, surrounded everyday with fear, hopelessness, and people who live like rats. So, I started a file. The God file. A cardboard box filled with envelopes and notes. The file has gotten fat. A brown box kept underneath my bed. I’ve believed and disbelieved a thousand times.

GABRIEL: (Pg 6-13) My name is Gabriel Black. I was 25 years old when I first saw Janie. She was married and didn’t care. I had no direction; no purpose. She became my purpose. A living, breathing, everyday reason. I knew the moment I met her something bad would happen. I knew the whole thing was wrong when I decided to be with her. And the price I paid came a thousand decisions later, in an apartment on a Saturday morning.

Janie’s husband had called the day before. I imagined his fat-wheeled Ford truck driving past the apartment. He was bigger than me, unpredictable and pissed off. I imagine every night that he slept alone was a reminder of what he’d lost – Janie. (beat) Since the dawn of time men have been killing each other over *women.* We will kill each other faster of *women* than anything else, including food, shelter, even religion.

I was sitting on the couch at 8:30 on Saturday morning when the front door busted open. Janie’s husband’s shoulder hit the wood and the doorframe splintered. Janie came out of the bedroom, with a gun in her hand. There was no time to speak. Before my gaze lifted, she fired twice into his chest. I saw the holes explode open. Her husband fell to his knees, and his face cracked against the glass of the coffee table, which shattered into a million specks of light. And then it was quiet.

I will never understand the reasons I did what I did next. Love? Honor? Loyalty? (beat) I took the gun from her hand, wiped it clean, and holding it in my right hand, I fired once at the far wall to get the smell on my hands.

I looked at Janie, and said, “I killed him. You were in the bedroom sleeping; you heard the shots and came out. Wash your hands, someone will be here any second.” [She] didn’t hesitate. Turns out the gun was stolen. The apartment? In the dead man’s name. She met with him the day before. Could she have planned it? Known I would take the blame? She’s never come to visit me, ever. The only time I saw her again was in the courtroom 22 years ago. She sat stone-faced with the angry relatives of her dead husband.

Guilty. Capital murder. Life in prison without parole. (beat) Does God exist? I set out to look for God in the tiny details, to find out for myself. All I have is time . . . So, I put together a file, to look for God in the tiniest details. (shuffles through his box and selects a file folder)

THE FEAR FILE: (Pg 28-31) (he reads) The two most traumatic events in our lives are birth and death. The fear of each is a gift. Fear lets us know when we are in danger. It can’t be separated from our survival instinct. (stops reading to tell his story) [But] once you start removing the fear, how do you know when to stop? The world is divided into warriors and non-warriors.

(Pg 39-43) The first time I was raped in this place, I thought about my daddy. I’d only been here a week – had no idea what it takes to survive. I was small and walked with a limp. I was selected for my weakness, like animals separate the herd. It ain’t got *nothin’* to do with pretty. There were three of them. I fought like a dog, bit and scratched, felt the punch shatter my ribs and suck the breath from my lungs. They thought it was funny.

When it happened the second time, I was ready. I fought until they thought I was done fighting, and then I cut the man with a piece of a razor. It was the last time they tried. The risk and the reward were no longer equal. You should have seen his face that split second from the time he saw what I had done until the pain shot up his backbone. (beat) Sometimes God hides Himself in the cracks between words. (Pg 65) They say that God never puts more on you than you can carry. When He does, when He goes too far, how will I know? (selects another file from the box)

THE CANCER FILE: (Pg 32-36) My mother died of breast cancer when I was 19. I came home from the Army on emergency leave. She had given me no warning. Maybe she had none. The doctor said, “The cancer is eating her up inside,” like he was angry. Like he couldn’t understand any more than I could why God would let evil black cells chew up my mother’s breast from the inside out and leave her choking up blood on the white sheets of someone else’s bed. They put crosses on the sides of highways where people die in car wrecks. Nobody put a cross in the hospital bed where cancer killed my momma. (long beat) Are we so afraid of cancer that we let it take who it wishes, as long as it leaves the rest of us alone. Abandoned by God for letting it do what it wants? (beat) [At least] Momma never had to see me in shackles. She never had to sit in the courtroom, torn between the love of her child and hatred. She never had to see me go to prison, or lie awake at night and wonder what unspeakable thing was happening to her boy in a prison shower.

(Pg 123) (long beat) I used to believe that the proof of God in suicide was my decision to choose AGAINST it every day. I know that the option is the gift. We don’t condemn the man in physical pain, with incurable cancer, when he takes his own life. But there’s pain in this world worse than any physical pain that might wrack this body of mine. God gave us a soul [and] with the soul comes the capacity to hurt worse than any animal or beast. Not only can we feel this pain, but we can understand it and put it in words. (struggles to contain the pain he feels) I have asked myself the question a million times, “If God gives me more than I can endure, how will I know?” He’ll bring me home, that’s how I will know. (beat; he begins to fashion a noose from his bed sheets and continues this process as he speaks)

(Pg 73-74) People seem to turn towards God when they have lost control of their lives. There is no place in the world like prison to make a person feel lost. I have watched men sit in their cells and read the Bible all day long. Every day I am told where I will sleep, when I will eat. My mail is opened, my room is searched. Others decide my choices of books, clothes, toilet paper, food. [But] I have tried hard not to make my decisions about God from a position of fear or loneliness or loss of control.

(Pg 107-109) I have read books of theology and the history of religion. But the real evidence of the existence of God is my existence itself – the existence of a human being. They write that the definition of a Christian is the belief in Adam and Eve, and the definition of a nonbeliever is the person who has allowed the science of Darwinsim to rot his soul. It isn’t that easy. Or maybe it isn’t that complicated. (thoughtful) If I were God, I would use time to create my most wonderful creation, a person. God is in no hurry. The Earth, the oceans and other animals and plants existed before we did. The battleground of evolution and Adam and Eve? Same God, same idea, same tool. Only God could use time and only time could make a person, any person.

(Pg 152-154) In my years of keeping the God file, I have come to believe that the greatest evidence I have of God’s existence is not me, but is the search itself. I have to believe that God sent me on this search, and the search itself has nourished and sustained me. It’s the most obvious gift from God, and it has been in front of me every single day.

We’re taught to believe that there is a hierarchy in the closeness of God. (places the noose over his head) But at this moment, this exact moment, no one could be closer to God than I am. I can close my eyes and feel His arm around me, tight and sure, like I was a little boy again. (long beat as he breathes in an out deeply) (Pg 129-130) We forget the stillness of silence. I search my memory for the sounds in my life that stand apart and can still make me feel the way I felt when I heard them for the first time: My mother crying (voice cracking with emotion) . . . (Pg 138) “Now I lay me down to sleep, I pray the Lord my soul to keep. If I should die before I wake, I pray the Lord my soul to take.” (Pg 129-130) The sound of my mother crying made me feel more worthless and alone than any sound in my life. I wish I could hear it one more time to know she was in the room next to me.

(he startles) The sharp sound of Janie’s gun firing the first bullet. (beat) The sound of the prison door closing behind [me] The heavy, iron vibration. This sound would be one I would always remember.

(Pg 156-157) (tightening the noose; he speaks as he loses consciousness) And I begin to move. Gently toward the soft, white light. Pulled by the strings of faith. And suddenly there is a sense of leaving something behind . . . (Pg 138) “I pray the Lord my soul to take.”
```

---

## IC-0370: Goin’ Fishin’

- Title: Goin’ Fishin’
- Author (byline): Chris Crutcher
- Work: Athletic Shorts: Six Short Stories
- Publisher: Harper Tempest
- Publication date as stated: Nov 2002
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: LIONEL, NEAL, VICKI, ELAINE, ELANIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1869
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
There is a case to be made that from the time of birth, when we lose a warm, enclosed safe place to be, our lives are made up of a series of losses and that our grace can be measured by how we face those losses and how we replace what is lost. Lionel Serbousek lost his parents in a boating accident when he was fourteen years old. Though he continues to explore his passions - athletics and art - with fervor, he remains haunted by his memories of that day on the lake and "what could have been. . . ." Like most of us, when his pain is the greatest, he covers it with anger, anger approaching rage. That rage has the power to consume. Goin’ Fishin’ by Chris Crutcher
```

### Performance text (classify this)

```text
LIONEL: My name is Lionel Serbousek. I'm a high school senior, an artist and a swimmer, and I'm also an orphan. I can tell no story about my life without telling this one first because it colors everything I do; everything I think.

LIONEL: I think if human beings had even the slightest capacity to foretell the future, we'd be a completely different animal. In the moment that I helplessly watched my family's death unfold before me, I wished I'd lived differently, done my chores on time, told no lies, eaten my vegetables, thanked my parents for giving me a room of my own, told them I loved them, been a better big brother for Kyle.

The person who killed my family was my best friend in fourth grade. He swam backstroke on our medley relay team and stayed over at our house nearly every other weekend; he learned to fish from my dad.

My dad . . . My father . . . my father was a head shaker. He was one of those adults who believe that if you take time to tell your children things, they'll grow up believing them and act accordingly. Anytime that failed to happen, Dad would simply shake his head slowly. With me, Dad shook his head a lot. If I'd known Dad was going to die, I'd have made a special effort to decrease the number of times a day he felt compelled to shake his head. But I thought I had more time. I thought I had all of time. [See] Fishing was a metaphor for life with my father. It required all the best elements of what he thought one needed to put together a graceful life. It required patience, knowledge, and skill. It wasn't frivolous, and on a good day you were rewarded immediately for doing it right, though certainly there were no guarantees. You could kid around with him about some things, but fishing wasn't one of them.

The person who killed my family [was] Neal Anderson . . . he learned to fish from my dad. [and he] wasn't supposed to be driving his parents' boat that day.

(Beat)

We were dead still in the middle of the lake in early afternoon, fishing deeper water, when Neal and his buddies, at least two six-packs into the afternoon, decided to take a quick spin in his dad's Sun Runner. Nobody in our boat but me even saw them coming. I hollered; but Mom and Kyle were hauling in a fish, and Dad was shouting advice. They didn't even look up. . . . And I jumped. I jumped.

I've watched it over and over, always knowing if I'd stayed a little longer or yelled a little louder, I could have saved them. It runs in slow motion in my dreams, so there's always plenty of time. (Beat) Neal's boat cut ours in half. None of my family even bobbed to the surface. Kyle's shirt floated near the wreckage, and I dived as deep as I could, only to be surrounded by blackness. I didn't know it was Neal at the time, but I got hold of him and did my very best to drown him. I held him under with both hands on his throat, and it took all the other two had, plus help from a guy who saw it all from a passing boat, to pull me off.

Swimming saved me. I took out my pain on the water. The louder the whine of the approaching Sun Runner echoed in my head, the clearer the sight of splintering fiberglass and flying bodies, the harder I swam. And slowly but surely the searing edge began to dull. I don't know if time heals all wounds, but I know it at least slows the spiritual bleeding.

I really thought I had it all in perspective, but then, about a week ago, Neal Anderson showed up at my door. Neal doesn't swim anymore, so I haven't seen him since the day he killed my family. And that's a good thing, because when things are at their worst, and I want someone to blame, Neal's my man.

(Opening door and speaking to Neal) What do you want? (To audience) I barely recognized him, wouldn't have if I hadn't heard his voice. His dishwater brown hair was stringy and unkempt, hanging to his shoulders; his clothes were dirty and threadbare. I couldn't see anything of the happy rich kid I knew in grade school. But it was Neal, it was Neal for sure, and I was instantly aware of my rage.

NEAL: Come on, man. I need to talk to you.

LIONEL: If I let you come in my house, I'll probably hurt you. You must be out of your mind. What he hell are you doing here?

NEAL: Trying to give myself a chance -- To make it right.

LIONEL: Anderson, turn around. Walk down those stairs. If you see me on the street, at a dance, or in a pizza place, or even at a gas station, stop what you're doing and run. I'll let you know if it's ever different. (To Audience) He started down the rickety stairs, then turned back about halfway down. I noticed how thin he looked, how raggedy. All his athleticism, that confident gait he had in fourth grade, when he was the fastest hundred-yard breaststroker in the state, was gone.

NEAL: I'm not leaving because I'm afraid you'll hurt me. Nothin' you could do to me would matter. I'm just leavin' because you want me to.

LIONEL: It was later that night when I realized how vicious I'd been. And it felt good. That night I realized it's my rage that's kept me alive over these three years, not friendships. Make no mistake about it; if I had been left alone in the water with Neal that day, I would have drowned him. And I have never trusted for a moment since what I might do if I ran into him. Now he was feeling some of what I've felt over the past three years, and for all I cared, he could waste away to nothing. Shortly afterward, my phone rang -- Neal's mom.

VICKI: Lionel, this is Vicki Anderson. I need to ask you a favor. A big favor. I'm calling about Neal. I know he came and saw you today. (Long silent pause) Lionel, he's dying.

LIONEL: Like my parents. My brother.

VICKI: Slower. Lion, I've never known what to say. I'm so embarrassed we haven't contacted you. I pray for you every night of my life. Neal's father has set up a trust for you . . .

LIONEL: Mrs. Anderson, money isn't going to bring my family back.

VICKI: He needs you to forgive him.

LIONEL: Won't happen. He killed my family.

VICKI: Lionel, he hasn't lived with us for more than six months. He's on the street. I think he's using drugs. I can't talk to him. He's dying, Lionel. Please, if not for him, then for me. For his father.

LIONEL: (To Audience) Until that moment I hadn't the slightest inkling of the true power of my hate. The sorrow that rose in my chest for Mrs. Anderson was crushed by it. (To Vicki) Mrs. Anderson, I'm sorry. But do you know what it's been like inside me for the last three years? Do you know how many times I've watched my parents and my little brother get cut in two? Do you know how much I've missed them? Mrs. Anderson, if I thought I could spend fifteen minutes with my little brother starting at the moment of my death, I'd be gone tonight.

I headed for the pool. I started with twenty-five-yard butterfly sprints. I have no idea how many I swam, but my chest and triceps were molten steel when I pushed off and saw a body knife into the water beside me. I finished the lap and looked up to see Elaine. Elaine was there for me always after the accident. I cried with her, and I told her everything. Elaine Ferral knows my soul, and more than anyone, she walked with me through the land-mined terrain of my grief. Finally I stopped, gasping for air, still fueled by my wrath. (To Elaine) Elaine, get out of here. I don't want to talk to anyone.

ELAINE: Well, you're gonna, I didn't come here to listen to you cry. What're you gonna do, Lion? Beat me up? Like you did Neal Anderson. Or his mom . . . You treated Neal Anderson like shit today."

LIONEL: Neal Anderson is shit.

ELAINE: It's for sure no one could tell you anything. What would your dad say? I knew your dad, Lion, and he'd call game on this cheap bullshit in a second. And your mom-

LIONEL: You leave my mom and dad out of this! I'm warning you, Elaine.

ELANIE: Wanna hit me, Lion? Go ahead. That do it for you? Maybe that's what you need. Let's start right here with me, Lion. Go ahead.

LIONEL: (To Audience) My fist clenched, and my upper lip vibrated like a jackhammer, and she punched me in the stomach so hard the wind blasted out of me like a released party balloon.

ELAINE: You double-up your fist at me, you better be ready to use it. You make me sick, Lionel Serbousek. When your family got killed, your friends gathered around you like angels. We spent the last three years making sure nothing touched you, treating you like some kind of boy in a bubble or something.

LIONEL: You can cancel your friendship out anytime. What the hell is the matter with you, Elaine? Neal Anderson killed my family! If I ever quit hating him, I -I-I'll die right with them.

ELAINE: Lion, remember the night you and Walker and Jeff and I drank all those beers and you took us out on the ice up at the lake in your Jeepster? None of us knew the ice would hold - and it was four miles over icy two-lane roads to get there. You could have killed us. Easy. And anyone else on the road. You were drunk out of your mind. So were we. What if you'd killed us, Lion, and you'd lived?

LIONEL: Yeah, well, I didn't. . . .

ELAINE: No, but you could have. What you did was more stupid than what Neal did. Only thing is, the universe caught him and it didn't catch you. You only get so long to be a idiot, Lion. Just so long to get decent again. Your time's about up."

LIONEL: (LONG BEAT – To audience) It was my third night searching. I knew better than to go into the park at night alone but was way past caring. Neal's gaunt face had haunted me since Elaine stalked away from me; Mrs. Anderson's pain over the phone had become real. And the thought of losing Elaine lay in my stomach like a sharp rock. I searched more than an hour and was finally ready to leave and try again tomorrow night when I saw a dim light between the slats of the wooden bridge. (To Neal) Neal? (To audience) He looked up dreamily, eyes glazed. His mom was right about the drugs. (To Neal) It's me. Lion.

NEAL: (emotional – but also high) Lion. I killed your mom and dad, man . . . And your little brother. I was just gonna ski. I just wanted to ski before my mom and dad-

LIONEL: Pack your stuff. I was gonna give myself a day off school tomorrow anyway. Maybe you and me oughta go fishin'.
```

---

## IC-0371: Good Guys Wear Yellow

- Title: Good Guys Wear Yellow
- Author (byline): Daphne R. Hall
- Work: Best Men’s Stage Monologues of 1997
- Publisher: Smith and Kraus Publishers
- Publication date as stated: December 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: HORATIO
- Teaser before the introduction: No
- Spoken words (computed): 1376
- Already set (do not supply): none

### Source block (context only)

```text
Author: Daphne R. Hull
Book: Best Men’s Stage Monologues of 1997
ISBN: 978-1575251370
Publisher: Smith and Kraus Publishers
Date (Month/Year): December 1998
```

### Introduction (context only: never use it for content warnings)

```text
The Question: Should we use the technology available to create human clones?

The Conservative Answer: The process is morally and ethically unacceptable "...scientists who envision medical breakthroughs using stem cells from human embryos are now moving on to human cloning -- breeding people for the purpose of harvesting their tissues and organs from their bodies, then disposing of them."

The Liberal Answer: "Human cloning allows man to fashion his own essential nature and turn chance into choice. For cloning's advocates, this is an opportunity to remake mankind in an image of health, prosperity, and nobility; it is the ultimate expression of man's unlimited potential."

In this state-of-the art debate, the good guys don’t wear white and the bad guys don’t wear black. In fact, in this debate, the Good Guys Wear Yellow by Daphne R. Hall
```

### Performance text (classify this)

```text
Horatio: (30s) a genetic engineer suffering from an attack of conscience Although Horatio has devoted his professional career to improving the genetic structure of humanity, he has recently come to respect the importance of serendipity as he here describes.

HORATIO: (Reads what he has written, after typing briefly) To whom it may concern. Hmmm. That may be a little too formal. Let's think about this a second. (Gets up and paces; loftily, Shakespearean.) To whom it may concern. (Pauses, sits.) I guess that will simply have to do. I wouldn't have a clue who to address it to specifically, if I were going to be specific. It stands as written:

To whom it may concern. (Pauses with fingers poised over keys, types again, stops.) If you are reading this, and I assume you are, otherwise I would be wasting my breath-or keystrokes-if you are reading this, I assume you are searching for an explanation. (Types, stops.) I don't feel like I owe any explanations, or owe anyone a thing, generally, but for the purposes of satiating the curious, and admittedly, satiating myself to some extent, I shall attempt to provide one. (Pause, sips, types.)

On second thought ... (Pause.) there is no explanation for what I have done. What I can offer is a series of observations and remarks, open for you to interpret your own explanation, your own answer to sew it up, your own fire in the hole. That will have to suffice. (Runs hand through hair, sips water.) I was recognized with a cash bonus from work last week. (Types.) I was also assured a promotion, next in line after the assistant to the deputy VP. of the Genetic Engineering Department retires in the fall. My supervisor slapped me on the back and said, (Puffy southern drawl.) "Not bad for the new kid on the block, eh?" Not bad at all. New kid. I've been the new kid for six years. (Types, reads.)

It is customary for any guy who has good fortune to treat the department to a round of beers after work. I guess this was expected of me as well. What is expected is not always received. The other engineers were putting their coats and hats on as slowly as possible, and some were sort of hanging by the door. I guess they were waiting for me to ask. I didn't. I pretended not to see.

(Pause, types, reads.) I came straight back to my apartment. I thought little of it, until the next day, when I began to get the feeling that I had suddenly become rather unpopular. It is not as if I previously could have been considered popular, but now I was most definitely and unequivocally unpopular. I had moved from a neutral status to one of the extremes. I seem to have broken an unwritten rule of the work force camaraderie: (Exaggerated fire and brimstone.) SHARE THY SUCCESS WITH THY BROTHERS, or THOU SHALT FEEL THE WRATH. (Beat, thoughtful.)

Perhaps someone should write down all of the unwritten rules. (Gets up, paces, stands and thinks while looking at a painting, returns to desk and types.) In my profession, I, and others like me, delve into genetic possibilities every day. Upon gaining some expertise, and testing for results, these possibilities become certainties, and the randomness, along with the anticipation of discovery, dissipates. (Slightly sarcastic.) The previous thrill of raw, lascivious searches for true answers fades into a sophisticated defense mechanism, where one must no longer prove for the sake of proving, but instead must prove oneself to be absolutely correct in one's hypotheses and calculations. Breakthroughs have given over to accuracy wrapped up tight in a pretty box. (Sips, types, reads excitedly)

In the lab, I can direct my computer to reconstruct and rearrange genes and DNA to create any type of person I-or my boss-wants to create. I am Bernstein, I am Zinman of the gene pool, conducting, pounding out a chromosomal coda, repeated over and over with subtle differences every time it is played. I can create clones, a slew of clones, if I want to. Perhaps-perhaps if Hitler had access to this knowledge, he would have approached genocide from a different angle, one more suited to the tastes of the masses. Perhaps he would have been gracious and simply sterilized all the Jews, let them die off, and created his superior race with a keyboard. (Yiddish singsong.) Much less messy. (Normal voice.) He may have been far too interested in flexing his muscles to take such a cerebral approach, but I wouldn't be here if he hadn't been so sloppy. His human capacity for error gave many of us life, directly or indirectly. And as for Hitler's successor? (Quiet, then types, reads.) The Union of Concerned Scientists are very concerned, as are the liberal media and the bible thumpers. Strange bedfellows. Anyway. I digress. (Pause.)

It took two or three years before I became weary of all this certainty. I knew what to expect when I awoke, when I arrived at work, when I came, and when I slept. No surprises. No plot twists. No nothing. About two months ago, after a long day of designing large quantities of various necessary people, I left work and found my car wouldn't start. (Smiles.) It was Fate, throwing a wrench into my routine and greeting me with a beckoning hand. I walked back to my apartment. On the way, I passed an art supply store. I stared in the window, and started to walk on several times, but kept stopping and turning back. Finally, I resigned myself to my own curiosity and ventured in. I emerged, hours later, with bags and armfuls of materials I knew nothing about, most of which I had not the foggiest idea how to use. (Smiles.)

I bought them all under the advice of a smiling salesgirl with crooked teeth and an unusual nose. As I checked out, I found myself wondering how to adjust her DNA to fix those little imperfections. (Pause.) I lugged everything into my apartment, spread it out on the floor, and stared at it all for a long time. Weeks. I decided eventually that since I had invested the money into these things, I might as well see what they could do.

(Very expressive at this point; more use of hands and boyish enthusiasm. He is describing his transformation and rebirth.) I slashed and attacked the canvas like an amateur-which is exactly what I am. (Types, reads.) I let the paint fall wherever it wanted to, or wherever I felt like having it fall. Finally, I had something requiring no blueprint, something never quite complete or incomplete, something never quite perfect-random splashes holding little meaning except to me. (Pause, stands, gestures to paintings.) That's what I did the day I received my cash bonus, instead of taking everyone out. I came home to paint. I never thought to tell them that I was going home to paint, it didn't occur to me to explain away my silent declinations. If I had, they probably would not have understood. I had never informed anyone of my activities after work. (Pause, types, reads.)

During the last few days of tepid relations, once I established their source, I realized that even had I known the outcome, the consequence, I would have done the same thing that evening. (Pause, excited again.) I have caught myself actually daydreaming at the terminal. For how long, I don't know, I just come out of it and I've been there. Through these dreams, I have concluded there is a definite and critical need for randomness and uncertainty. (To himself, exclaims.) Something that surprises! (Types, then reads.)

Yesterday, on my way home from work, again forgoing machinery for manpower, a car barreled through a mud puddle and I was thoroughly soaked. As I peeled my dripping socks from my feet, I thought, how random can you get? What is the probability that I, not anyone else, would be standing on that particular street corner at that particular moment when that particular car drove through that pothole and that the pothole would be filled with rainwater? So. The pothole brings me to today. (Sips, types, reads silently, then paces, paper in hand.) Today, I went to work, same as always, and carried out my routine duties. (Slow smile.) With a small plot twist. I decided to exert a high locus of control over a system possessing a incredible amount of control over all of us. (Pause, pleased.) I erased everything.

Everything. All my programs, all my data, all my notes, everything. Wiped the drive clean. I came home and burned the backup tapes. Everything. The key to success has been swallowed. (Walks to desk, sips water.) The Russian roulette of pure human reproduction will have to suffice, at least for a while, until the others retrace my steps and play catch-up. I took the rest of my cash bonus and made preparations to erase myself as well. (Opens desk drawer and takes out a gun; sips water; holds up gun and spins cylinder.) To keep me from changing my mind. (Puts gun to temple; lights go out as there is a loud gunshot.)
```

---

## IC-0372: Gospel According to Miss Roj

- Title: Gospel According to Miss Roj
- Author (byline): George C. Wolfe
- Work: The Colored Museum
- Publisher: Broadway Play Publishers
- Publication date as stated: 1987
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MISS ROJ
- Teaser before the introduction: Yes
- Spoken words (computed): 1127
- Already set (do not supply): none

### Source block (context only)

```text
Author: George C. Wolfe
Book: The Colored Museum
ISBN: 978-0881450521
Publisher: Broadway Play Publishers
Date (Month/Year): 1987
```

### Introduction (context only: never use it for content warnings)

```text
Miss Roj -- a transvestite with some strong coping mechanisms. But despite his humor and other expressions of "attitude." There is a deep river of pain and the struggle to define his own identity. Snapping and dancing become things, not to smile about, but to recognize as cries of a persecuted minority. The Gospel According to Miss Roj by George C. Wolfe
```

### Performance text (classify this)

```text
NOTE: Script indicates that actor should be African American.

{Pg 14-18) (The darkness is cut by electronic music. Cold, pounding, unrelenting. A neon sign which spells out THE BOTTOMLESS PIT clicks on. There is a lone bar stool. Lights flash on and off, pulsating to the beat. There is a blast of smoke and, MISS ROJ (an African American man) appears. He is dressed in striped patio pants, white go-go boots, a halter, and cat-shaped sunglasses. What would seem ridiculous on anyone else, MISS ROJ wears as if it were high fashion. He carries himself with total elegance and absolute arrogance.)

MISS ROJ: God created black people and black people created style. The name’s Miss Roj . . . that’s R.O.J. thank you and you can find me every Wednesday, Friday and Saturday nights at “The Bottomless Pit," the watering hole for the wild and weary which asks the question, "Is there life after Jherri-curl?"

MISS ROJ: Yes, if they be black and swish, the B.P. has seen them, which is not to suggest the Pit is lacking in cultural diversity. Oh no. There are your dinge queens, white men who like their chicken legs dark. (He winks/flirts with the audience.) And let’s not forget, “Los Muchachos de la Neighborhood.” But the speciality of the house is The Snap Queens. (He snaps his fingers.) We are a rare breed.

For, you see, when something strikes our fancy, when the truth comes piercing through the dark, well you just can’t let it pass unnoticed. N0 darling. You must pronounce it with a snap. (He snaps.) Snapping comes from another galaxy, as do all snap queens. That’s right. I ain’t just your regular oppressed American Negro. No-no—no! I am an extra-terrestial. And I ain’t talkin' none of [what] you seen in the movies! I have real power.

Yes, I was placed here on Earth to study the life habits of a deteriorating society, and child when we talkin’ New York City, we are discussing the Queen of Deterioration. Miss New York is doing a slow dance with death, and I am here to warn you all, but before I do, I must know . . . don’t you just love my patio pants? Annette Funicello immortalized them in “Beach Blanket Bingo,” and I have continued the legacy. And my go-gos? I realize white after Labor Day is very gauche, but as the saying goes, if you’ve got it flaunt it, if you don’t, front it and snap to death [anyone who dares to defy you. (Laughing) Oh ho! My demons are showing.

Let’s just hope for all concerned I dance my demons 'cause child, dancing demons take you on a ride and you find yourself doing the strangest things. Like the time I locked my father in the broom closet. Seems the liquor made his tongue real liberal and he decided he was gonna baptize me with the word ”faggot” over and over. Well, he’s just going on and on with ”faggot this” and ”faggot that,” all the while walking toward the broom closet. So the demons just took hold of my wedges and forced me to kick [him] into the closet and lock the door. (Laughter) Three days later I remembered he was there. (He snaps.)

(Dancing about.) Oh yes—yes—yes! Miss Roj is quintessential style. I corn row the hairs on my legs so that they spell out M.I.S.S. R.O.J. And I dare [anyone] to [mess] with me because I will snap [you] into oblivion. I have the power, you know. Every time I snap, I steal one beat of your heart. So if you find yourself gasping for air in the middle of the night, chances are you [messed] with Miss Roj and she didn’t like it.

Like the time this [jerk] at Jones Beach decided to take issue with my coulotte-sailor ensemble. This child, this muscle-bound Brooklyn thug in a skin-tight bikini. You know the kind who beat up on their wives for breakfast. Snap your fingers if you know what I’m talking about . . . Come on and snap, child. Well, he decided to blurt out when I walked by, “Hey look at da monkey in da faggit suit." Well, I walked up to the poor dear, very calmly lifted my hand, and. . . . (He snaps in rapid succession.) A heart attack, right there on the beach. You don’t believe it? Cross me! Come on! Come on!

(Looking around.) If this place is the answer, we’re asking all the wrong questions. The only reason I come here is to communicate with my origins. Theflashing lights are signals from my planet way out there. Yes, girl, even further than Flatbush. We're talking another galaxy. The flashing lights tell me how much time is left before the end.

I hate the people here. But most of all I hate this [damn] music. (Raps some horrible lyrics) That ain’t music. Give me Aretha Franklin any day. (Singing) “Just a little respect. R.E.S.P.E.C.T” Yeah! Yeah!

Come on and dance with Miss Roj. Last call is [moments] away and each snap puts you one step closer to the end. (In rap style) “A high-rise goes up. You can’t get no job.” Come on everybody and dance. “A whole race of people gets trashed and debased.” Snap those fingers and dance. “Some sick [mama] thows her baby out the window ‘cause she thinks it’s the Devil.” Everybody snap! “The New York Post.” Snap!

Snap for every time you walk past someone lying in the street and you don’t see it. Snap for every crazed [man] who kills himself so as to get the jump on being killed. And snap for every sick [mind] who, bored with carrying around his fear, takes to shooting up other people.

Yeah, snap your fingers and dance with Miss Roj. But don’t be fooled by the banners and balloons ‘cause, child, this ain’t no party going on. Hell no! It’s a wake. And the casket’s made out of stone, steel and glass and the people are racing all over the pavement like maggots on a dead piece of meat.

Yeah, dance! But don’t be surprised if there ain’t no beat holding you together ‘cause we traded in our drums for respectability. So now it’s just words. Words rappin’. Words screechin’. Words flowin’ instead of blood ‘cause you know that don’t work. Words cracklin’ instead of fire ‘ cause by the time a match is struck on 125th Street and you run to mid-town, the flame has been blown away.

So come on and dance with Miss Roj and her demons. We don’t ask for acceptance. We don’t ask for for approval. We know who we are and we move on it!

I guarantee you will never hear two fingers put together in a snap and not think of Miss Roj. That’s power, baby. Patio pants and all. (The lights begin to flash in rapid succession.) So let’s dance! And snap! And dance! And snap! (MISS ROJ begins to dance as if driven by his demons. singing ”Respect.")
```

---

## IC-0373: Guns for Geeks

- Title: Guns for Geeks
- Author (byline): Chris Crutcher
- Work: On the Fringe: Stories
- Publisher: Dial
- Publication date as stated: April 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SAMMY, BEEMER, ROY, LINDA, GENE, WALLER
- Teaser before the introduction: Yes
- Spoken words (computed): 2473
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chris Crutcher
Book: On the Fringe: Stories
ISBN: 978-0142500262
Publisher: Dial
Date (Month/Year): April 2001
```

### Introduction (context only: never use it for content warnings)

```text
Guns for Geeks by Chris Crutcher
```

### Performance text (classify this)

```text
SAMMY: My mother is a child therapist and my dad works for the Department of Children's Services, and we've been a receiving home for kids being put into foster care as long as I can remember. Gene [Taylor] was at our house probably ten times, sometimes so hungry he couldn't keep from stuffing himself like a famine victim at the dinner table, and sometimes sporting some really creative bruises and burns. And that's just what I know. Imagine what the whole truth might be.

SAMMY: Mr. Beemer's U.S. Government class. Beemer is [the] boys' basketball coach, but academics is even more important to him than athletics. On this day, amidst our Second Amendment discussion, Beemer was promoting the idea of context.

BEEMER: How many of you - and I'd like a show of hands here rather than pistols - believe the framers of our Constitution considered when they included that particular right that we might someday have guns that fired more than one bullet with one squeeze of the trigger? (pause as he is obviously met by silence from the class) Or that our society might turn out to be one of the world's most violent in the new millennium.

ROY: Guns don't kill people . . .

BEEMER: I know: People kill people. But they do it with guns.

ROY: Not always. An old guy in Spokane was beaten to death with a golf club last week. (laughing) How come people don't ask for a ban on golf clubs?

BEEMER: (smiling) Don't get me wrong, guys. I'm not trying to rewrite the Constitution, or remove your right to bear arms. I'm just asking - if the context had been different, would the framers have written it differently?

SAMMY: Linda Cross raised her hand, and I flinched. Linda's little brother had killed her littler brother last year playing with their father's handgun, there for purposes of protection and supposedly out of reach.

LINDA: Maybe people kill people, but if Christopher hadn't gotten his hands on that gun, Marvin wouldn't be dead. (glaring at Roy) Even if he could have gotten his hands on a golf club.

SAMMY: I looked out the window then to avoid the discomfort I felt about Linda's remark . . . [It was then that] the door opened, and we looked up to see Gene Taylor in a long rider's coat, leather cowboy hat and boots, his face contorted into a grim intention that certainly changed our lives forever. The front of the coat swings back and, scanning the room with narrow eyes, he brings up a lever-action .30-.30. He shoots Roy Salley first, in the head. Roy is there, a recognition on his face, staring down the barrel, then gone. It unfolds in slow motion. Roy pitches backward, his head striking the blackboard like a melon. Megan Gratten is next, probably only because she sits next to Roy there in the back of the room. Her eyes widen in astonishment as the bullet rips through her neck, then she lies tipped over, an awful sucking sound coming from the wound. Low moans escape terrified throats. I am so aware of weight, of gravity's imposing force, welding me to my spot. Something inside me says do something. It is Gene Taylor, whom I have watched come and go from our foster house like a church mouse; a wall-hugger who makes a career of being invisible, now reducing the toughest of us to our knees. His eyes are dark and consumed as he swings the rifle barrel in search of his next victim. Gene tells us to put our heads on our desks. When no one responds he screams it, firing two more rounds. One strikes Mr. Beemer in the shoulder and the other slams into Carly Pruitt's stomach. Carly is my girlfriend and best friend. I leap from my chair then, kneel and cradle her head in my lap, only to look up at the long tunnel that is his rifle. Carly breathes shallow gulps of air, her eyes shut tight against the pain. (to Gene) "Don't, man. Please." Our eyes meet and his finger twitches on the trigger, and maybe he remembers I was decent to him in our home, because he motions with the barrel for everyone to put their heads down. They do so in unison. Mr. Beemer is conscious, slumped forward at his desk gripping his shoulder, groaning, blood trickling down his forearm onto the back of his hand. I hope his mind is working; Gene isn't finished. He glares at me then, his lip curls, and I listen for the bang.

GENE: (Screaming) Keep your heads down!

SAMMY: [His] eyes locked on mine for that dreadful moment, and [then he] swings the barrel away, leaving his back to me. I beg myself to rise; can't.

GENE: (forcefully) Things are going to change around here . . . The first will be last and the last will be first. (chuckling) The first will be dead and the last will be first.

SAMMY: He points the rifle at Johnny Waller now, a quick, first-string point guard - with a quicker mouth - and a straight-A student. He walks toward him, his back still to me. [He] glances over his shoulder to smile at me, and shoots him through the back of the head point-blank. Johnny slumps like a sack of potatoes.

GENE: (to Johnny’s corpse) Get it together.

SAMMY: "Get it together." Get it together is Johnny's rallying cry bringing the ball up court - it's also what he said to Gene Taylor in front of our sophomore speech class when Gene froze in the face of a one-minute improvisational speech two years ago.

GENE: Big mouths first, crybabies and whiners next.

SAMMY: At the desk Beemer pulls himself up, stands wobbly legged, holding his shoulder, taking slow, deep breaths. He moves around the desk.

GENE: Let's see, who's next? (looking over the class of students) Who else called me pussy?

BEEMER: (Standing up straight) Gene. You have to stop.

GENE: (Turning to Beemer) Stop? (a shrill laugh) I'm just getting started. All these scores to settle, so little time. (he looks Beemer up and down) You're not looking so good, sir. Why don't you have a seat? (Turning back to the students) "Now, where were we?" (he walks to another student and raises the pistol to his head)

BEEMER: Pussy. If you're looking for people who called you pussy, I'm your guy.

GENE: (not turning around) Never heard you say that, sir. I shot you because you didn't stop them.

BEEMER: In the teacher's lounge. I called you that in the teacher's lounge all the time. 'Wouldn't have Taylor on any of my teams. Way too big a pussy.’

(his knees buckle, but he catches himself)

GENE: (turns, eyes blazing, jaw set. He walks toward Beemer with his gun now pointed at the teacher) "Get on your knees, sir." (Beemer slowly kneels, his eyes locked with Gene’s) Open your mouth. (laughing) I want to see you explode.

BEEMER: (A long hesitation) No.

GENE: Put the barrel of the gun in your mouth and I'll let one person go.

BEEMER: (glances around at the class, he starts to open his mouth, then) No, it has to be more than one . . . All of them, Gene, or you don't get to watch my head explode.

GENE: (screaming) Open your goddamn mouth!

SAMMY: And his voice jars me loose. I leap up as he turns; I never had a chance. But from his knees, Beemer blocks him like an offensive guard, knocking him off balance as T.J. springs headlong from his desk, snatching the gun as Gene pulls the trigger, burying the bullet in the ceiling. Beemer pins Gene to the floor as a student pulls the classroom door open and teachers swarm in. In the distance, sirens wail. ************SCENE BREAK***************

SAMMY: I got away from school out the back way before the local news media could catch me, and hightailed it to the hospital to see how Mr. Beemer was. He told me T.J. and I had saved a lot of lives, that he'd never have had a shot at Gene if I hadn't diverted his attention, and who knows who else might have been hit if T.J. hadn't gone for the gun. (to Beemer) Yeah, but what about Johnny? . . . Coach, Gene had his back to me. I couldn't have stopped him from shooting Roy or Megan or even Carly. But his back was to me before he killed Johnny." (gasping for air) I froze.

BEEMER: Don't do that. (motioning Sammy closer) Sam, listen to me. All of us in that room know something about ourselves that we didn't know before today. Nothing's ever going to be the same for anyone who was there. But there's only one person to blame for this, and that's Gene. He came into the room with his guns and opened fire. Everything that happened after that was in response to it. Okay?

SAMMY: I took a deep breath, saw Gene's back again, saw Johnny slump forward. I wanted to believe what Coach said, and maybe as time goes on it'll be easier. But I can't shake the sensation of being paralyzed, of knowing some of my best friends, my girlfriend, for God's sake, stood to die, and I couldn't move. ************SCENE BREAK***************

SAMMY: (to audience) The following days went by in a blur for me. Funerals. I couldn't tell you which came first or what was said - only that whatever was said, it wasn't enough. It wasn't right. Johnny Waller and Megan Gratten and Roy Salley would never sing another song or dribble another ball or see another sunset. I jump up one morning, to drive through the deserted streets toward Waller's Chevron. I pull up next to the one self-serve pump. Mr. Waller, [Johnny’s dad], is inside counting bills into the cash register. I'm desperate to know if anyone has talked with him about that day - if anyone has told him Gene Taylor's back was to me for what seemed like an eternity before he shot Johnny, and that I didn't move. I top off my tank and walk inside to pay.

WALLER: How ya been?

SAMMY: (to Waller) Okay, I guess. You know. (to audience) God, does he have any idea?

WALLER: (nodding) Wanted to thank you again for Johnny's funeral, for carryin' the casket. That's a hard thing to do . . . Carry a dead classmate.

SAMMY: There have been a lot of hard things around here lately.

WALLER: I want you to answer me a question . . . Truthfully. . . . You think my boy was a smartass?

SAMMY: (heart leaping into his throat) Yeah, well, maybe. No more than me. No more than a lot of guys.

WALLER: You think his big mouth got him shot?

SAMMY: (to audience) I flash to that day in sophomore speech class when he told Gene Taylor to "get it together," watched Gene turn red and drop his gaze to the floor, then sit down without a word. (to Waller) Yeah, maybe. Johnny wasn't exactly, like, sensitive, but hey, who is?

WALLER: (slowly wiping his hands on a grease rag from his back pocket) I'm afraid I might a taught him to be that way. (staring at a spot a few inches from his nose, almost talking to himself) I'm kinda the quiet type, always felt a bit afraid to push things. Wanted him to stand up, not be like me. I'd just feel more peaceful if I thought my boy wasn't gone 'cause of somethin' I done.

SAMMY: (to audience) I remember Beemer’s words. (to Waller) Hey, there are lots of guys around with bigger mouths than Johnny. I mean, who knows why Gene picked who he picked. Johnny's gone because Gene Taylor was f*** up. Pardon my language.

WALLER: (thinking for a moment) It's a minefield . . This life.

SAMMY: (to audience) Mr. Waller was a foot soldier in the Korean War. He knows what a minefield is. Suddenly I just want to help him; to say some truth that takes the edge off. I decide on the big one. (to Waller, hesitantly) Before he shot Johnny, Gene was . . . Well, he turned his back to me. I mean, I don't know if anyone told you . . . (choking up) I don't know whether . . . maybe if I'd moved faster - I was scared (moving toward the door) I was so damn scared. I'm sorry, Mr. Waller. (exits) (to audience) In my peripheral vision I see him moving toward the door as I climb into my car, think he's going to yell something at me, but I keep my eyes focused straight ahead and pull out, catching a glimpse of him in my rear-view mirror standing out on the concrete, his hand half raised. ************SCENE BREAK***************

SAMMY: At a broad clearing near the top of the mountain, I pull off. I roll down my window, let the cold air rush in as I take a deep breath, trying to fill my body with something clean. The thoughts pass in single file, in twos, in stampedes. I don't light on one, images actually, more than words: Gene standing in the doorway to the classroom. Gene leaning over a plate of food in our house, embarrassingly ravenous. Roy Salley's smug look as he taps Gene on one shoulder and slaps the opposite side of his head as Gene turns to look. Johnny Waller with his head on his desk. The back of Gene's head as he walks away. Beemer in his hospital bed. Carly bleeding on the floor. Mr. Waller's sad face. The talk now is all about forgiveness. How can you forgive someone who has done something you can't even wrap your mind around. [And] along with the talk of forgiveness, sometimes in the same sentence, is talk of who is to blame. It's as if we can't get past any of this unless we find out who to hang it on. . . Well, I've had some time to think, and I have a theory. No one is to blame. Everyone is to blame. I mean, Gene is to blame because he did it; no one can argue with that. But when I remember his face - his eyes - it's hard to think he had any control over what he was doing. We could blame his parents - a mother for being there too much and a dad for not being there at all - but it's not as if they sat around and said "Let's f*** up our kid so bad that he goes out and opens fire." It's not hard to imagine that their folks did a worse than mediocre job of parenting too. Mr. Waller made the statement I like best.

WALLER: I don't care who's to blame. My son is dead and that's never going to be any different.

SAMMY: Don't get me wrong. I hate Gene Taylor for what he did. And I hate him because of how cowardly I felt, and still feel, for what I did and didn't do when I had to face him. But I also can't help seeing him at my house, gorging himself, satiating one hunger while not touching the other; hiding his scars, grateful for the respite and at the same time resentful toward me, because he has never had the things I take for granted - food, love, Nikes, a girlfriend. Gene Taylor had to feel embarrassed coming to our house. How messed up is that? A guy gets treated like shit, then has to be ashamed when folks discover that he's a guy people treat like shit. [Now] I go out to Waller's Chevron every Thursday morning at the crack of dawn. When I got there this morning, he was sitting with his feet up on the front desk, reading the paper.

WALLER: (reading from the paper) Says here if they try [Gene] as a juvenile, he's out on his twenty-first birthday at the latest. If they try him as an adult he could get life with no possibility of parole. (puts paper down and smiles tiredly) They're trying to figure out how to punish him (slowly shaking his head) Hell, don't they know guys like Gene Taylor are punished before they do their deed? . . . . Now, what are we going to do about that?
```

---

## IC-0374: Hangman

- Title: Hangman
- Author (byline): William Borden
- Work: More One-Act Plays for Acting Students
- Publisher: Meriwether Publishing
- Publication date as stated: July 2003
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: THEODORE, ROGER
- Teaser before the introduction: Yes
- Spoken words (computed): 1230
- Already set (do not supply): none

### Source block (context only)

```text
Author: William Borden
Book: More One-Act Plays for Acting Students
ISBN: 978-1566080873
Publisher: Meriwether Publishing
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
Hangman by William Borden
```

### Performance text (classify this)

```text
THEODORE: Don't you feel some dishonesty? Killing people you have so much in common with?

ROGER: I don't find it dishonest, no. Poignant, perhaps. Ironic. Tragic, even. It's like playing a part in a great drama. It fulfills me. Whereas you become nameless, faceless, one of many who die futilely.

(THEODORE, watched by ROGER, stands on a stool, tying a rope to a pipe or beam. He finishes and steps off the stool. They both appraise it/or a moment, then ROGER tugs at the rope. The rope comes off ROGER throws the rope to THEODORE.)

ROGER: You think I haven't seen everything? Every trick and ruse you scum could possibly think of? You think I'm not smart?

THEODORE: You're very smart.

ROGER: I am.

THEODORE: I imagine you have a Ph.D.

ROGER: Don't get smart with me. (THEODORE ties the rope again.)

THEODORE: This will be a foolproof knot. Guaranteed to kill instantly.

ROGER: Not instantly. We want you to ponder your ways, reflect on your errors, as you dangle, swaying slowly in the breeze. Then we allow you to expire.

THEODORE: Expire.

ROGER: Yes.

THEODORE: You have an enormous vocabulary.

ROGER: Thank you.

THEODORE: A veritable prodigious lexicon in your cerebrum.

ROGER: I read vociferously. No television, no card games – I have the complete collection of The Great Books.

THEODORE: The Great Books? Who wrote them?

ROGER: You know those guys, from Homer and the Bible to Melville and Prowst.

THEODORE: Prowst?

ROGER: You're not too well read yourself, are you?

THEODORE: No, I'm not.

ROGER: Prowst was a French guy, wrote in a cork-lined room, suffered from asthma. He pursued the nuances of the past. Cherchez the past. And he was a fag. (ROGER tests the beam.) That's better.

THEODORE: Might be too sturdy.

ROGER: Naw.

THEODORE: I might not dangle long enough. I have a lot of sins to reflect upon as I die.

ROGER: They go fast. Whole life in a flash. That's the rumor.

THEODORE: As I dangle.

ROGER: As you dangle.

THEODORE: In the breeze.

ROGER: In the breeze.

THEODORE: What breeze? We're indoors. Miles from daylight. So you've told me.

ROGER: Well, just the momentum, as you plunge through the opening, and the rope, you know, jerks you up, as you're plunging down - gives your body what they call a torque, an angular momentum, so your body, as it's expiring, will swing, from its own potential energy.

THEODORE: Torque.

ROGER: You'll sway in quite graceful circles, or possibly ellipses, around and around.

THEODORE: Like a pendulum.

ROGER: Exactement.

THEODORE: I could become a clock.

ROGER: If I left you there.

THEODORE: Then you were lying about the breeze.

ROGER: It was a bit of poetry.

THEODORE: Do you write?

ROGER: Reports?

THEODORE: Poetry.

ROGER: Me?

THEODORE: Let me hear something.

ROGER: Naw...

THEODORE: Please! (ROGER pulls out a fat sheaf of scraps of paper. Then he looks at THEODORE.)

ROGER: You'll laugh. (THEODORE doesn't answer. ROGER hesitates, then starts to read.) "The rope sings like a nightingale as it snaps across the breeze" Maybe breeze isn't right there. (ROGER takes out a pencil.) "The rope sings like a nightingale as it snaps ... into the ... abyss ... of death."

THEODORE: "Death" 's trite.

ROGER: You're right. "Abyss of ... "

THEODORE: "Like a raven." "Raven" 's better than "nightingale." "Raven" connotes the harshness of the moment.

ROGER: It's a beautiful moment. Lyrical. And for those who disagree, there's the irony, the poignant reversal of expectation. "Abyss of ... "

THEODORE: "Horror."

ROGER: "Abyss of ... "

THEODORE: "Meaninglessness." "Nothingness." "Darkness."

ROGER: "Into the abyss of..."

THEODORE: "... into the sweet memory of roses." (ROGER looks at him a moment, then writes it down, shoves packet into his pocket.)

ROGER: (Reluctantly) Thanks. (ROGER tests the knot. It holds.) Good work.

THEODORE: Thanks.

ROGER: Of course it's not a professional job.

THEODORE: I'm going to hang!

ROGER: I'd think that would be a particular reason for taking pride in your work. Here. (ROGER hands THEODORE the other end of the rope.)

THEODORE: Now what?

ROGER: The noose. Make the noose.

THEODORE: (Throwing down the rope) No. I won't participate any further in my own murder.

ROGER: Execution, my friend. Words are important.

THEODORE: Shoot me then! That will make it murder!

ROGER: However I do it, it's an execution.

THEODORE: No

ROGER: I'm the executioner. It's a matter of definition. The man who writes the dictionary rules the nation. I can execute you now - (He pulls out the pistol.) Or you can have another minute or two to enjoy God's bounty on earth, while you tie the rope, while I test it, while we engage in scintillating dialect. Which do you prefer?

THEODORE: Shoot me. We might as well get it over with.

ROGER: That seems mighty shortsighted, my friend. Who knows what might occur in the next ninety seconds? An earthquake might kill me and free you.

The rebels might stage an attack and divert my attention, allowing you to escape. There might be a coup from above. A foreign invasion. The Commander might commit suicide. You might receive a pardon. Don't forget - what's his name? You know, the Russian

THEODORE: Dostoevsky?

ROGER: That's the guy. Life is ruled by chance, old boy. Ninety seconds can seem like an eternity.

THEODORE: Everything is fated.

ROGER: An Augustinian!

THEODORE: There is a destiny

ROGER: God's? Or the inevitability of historical materialism? (THEODORE doesn't answer.)

THEODORE: I think for me ninety seconds will pass quickly.

ROGER: Time is relative.

THEODORE: Time marches forward inexorably.

ROGER: Inexorably.

THEODORE: Inexorably. I relish intellectual debate. Don't you? I haven't had a good discussion for a hell of a long time.

ROGER: (ROGER hands the rope again to THEODORE.) The noose.

THEODORE: I don't know how.

ROGER: I don't believe it.

THEODORE: It's not something you need to know in the normal course of a lifetime.

(Disgusted, ROGER begins to make the noose.)

ROGER: The other executioners, you know, all they want to do is play cards, read girlie magazines. I'm out of my element.

THEODORE: I can see that. (He watches ROGER deftly make the noose.) You're very good.

ROGER: Funny thing is, you guys usually have something to talk about. You seem to think more. It must be thinking that makes you dissatisfied with things.

THEODORE: It's not only thinking.

ROGER: I suppose not.

THEODORE: It's feeling, too. You know, intuitively, things aren't right.

ROGER: Well, it depends which side you're on, doesn't it? Like for me, things are right. (He completes the noose. He admires his work.)

THEODORE: But they're not.

ROGER: Of course they're right. Right as rain.

THEODORE: You're not happy.

ROGER: (Angrily) I'm happy!

THEODORE: You're a fish out of water. No intellectual companionship. No one to share ideas with.

ROGER: (Slipping the noose over THEODORE's head) Now there's where you're wrong, old sport. I have you to converse with. You and your compatriots. All day, every day, one after another, a veritable parade of intellect.

THEODORE: Perhaps you'd like to join us.

ROGER: Get myself executed?

THEODORE: Fight for a cause.

ROGER: Die before my time?

THEODORE: Live a meaningful life.

ROGER: Die like a dog? There's a flaw in your syllogism. (ROGER motions THEODORE onto the stool.)

THEODORE: Don't you feel some dishonesty? Killing people you have so much in common with?

ROGER: I don't find it dishonest, no. Poignant, perhaps. Ironic. Tragic, even. It's like playing a part in a great drama. It fulfills me. Whereas you become nameless, faceless, one of many who die futilely.

THEODORE: Who knows what's futile?

ROGER: It's plain as the noose around your neck.

THEODORE: But don't we have some effect? Make some difference?

ROGER: Oh, yeah. I learn a lot. I sharpen my wits. You make a big difference to me.

THEODORE: Do I?

ROGER: Definitely. (THEODORE climbs onto the stool.)

THEODORE: I mean, do I? Do I, Theodore, make a difference to you?

ROGER: What do you mean?

THEODORE: Or am I just one of many who pass through your life? What's your name?

ROGER: My name? I have no name. So far as you're concerned.

THEODORE: Have you no conscience?

ROGER: Do you? Wouldn't you kill me if you could? Even after our thrilling conversation? You would. Because I'm on the other side. It would be my fate to die.

THEODORE: It would be a chance you would take.

ROGER: So you see, I have no choice.

THEODORE: You always have a choice.

ROGER: Do you? (ROGER gets ready to kick away the stool.)

THEODORE: One question - (ROGER pauses.) Does everyone participate in his own ... death?

ROGER: Oh, yes. We think it makes a point. It teaches a lesson.

THEODORE: But what good will it do now?

ROGER: That's the irony of it, isn't it? Any further last words?(Several beats. ROGER gets ready to kick away the stool.)

THEODORE: Proost.

ROGER: What?

THEODORE: Proost! It's pronounced Proost, not Prowst!

ROGER: You kidding me?

THEODORE: No.

ROGER: You're sure?

THEODORE: I'm positive.

ROGER: You know French?

THEODORE: Tres bien.

ROGER: Proost.

THEODORE: Proost.

ROGER: I could've gone on for years making a fool of myself.

THEODORE: I know. (Several beats)

ROGER: Well. We can't wait forever.

THEODORE: No. (Several beats)

ROGER: Roger.

THEODORE: Pardon?

ROGER: My name's Roger.

THEODORE: Ah. (Beat) Theodore.

ROGER: Right. (ROGER starts to kick away the stool, the stage goes to black,
and there s a strange musical note, as of a string being plucked, the
overtone lasting for several seconds.)
The rope sings
like a nightingale
as it snaps
into the sweet
memory of roses.

It's a beautiful moment. Lyrical.
```

---

## IC-0375: Harry’s Story from 11/22/63

- Title: Harry’s Story from 11/22/63
- Author (byline): Stephen King
- Work: 11/22/63: A Novel
- Publisher: Gallery Books
- Publication date as stated: July 2012
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: JAKE, HARRY, INTERCOM, AL, ELLEN
- Teaser before the introduction: Yes
- Spoken words (computed): 2249
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephen King
Book: 11/22/63: A Novel
ISBN: 978-1451627299
Publisher: Gallery Books
Date (Month/Year): July 2012
```

### Introduction (context only: never use it for content warnings)

```text
Life-changing moments. Single acts that so profoundly affect your life, you know you’ll never be the same. Moments that have the power to transform lives and shape destinies. Jake Epping is moved by the raw honesty of Harry’s essay. But he never realized that Harry’s life-changing moment would become his too.

If you had a chance to go back in time and change history, would you do it? And what would happen if you did? Would you change . . .

Harry’s Story from11/22/1963 by Stephen King
```

### Performance text (classify this)

```text
JAKE: (Pg 18) I have never been what you’d call a crying man. My ex-wife, Christy, said that my “nonexistent emotional gradient” was the main reason she was leaving me. (Pg 19) I can only remember one time when I cried as an adult, and that was when I read the story of the janitor’s father. I was sitting along in the teachers’ room at Lisbon High School, working my way through a stack of themes that my Adult English class had written. The subject I’d assigned was “The Day That Changed My Life.” (Pg 20-21) There were no violins or warning bells when I pulled the janitor’s theme off the top of the stack, no sense that my little life was about to change. But we never know, do we? Life turns on a dime. I remember how his theme started. I remember it word for word. “It wasn’t a day but a night. The night that changed my life was the night my father murdirt my mother and two brothers and hurt me bad. He hurt my sister too, so bad she went into a comah. In three years she died without waking up. Her name was Ellen and I loved her very much.” It was when I got to the part about him crawling under the bed with blood running in his eyes that I began to cry. I had thought he was slower than the rest. Well, by God, there was a reason for that, wasn’t there? And a reason for the limp, too. It was a miracle he was alive at all. [Just] a nice man who would be a janitor for the rest of his life. Maybe once he could have been something different, but one night his life turned on a dime and now he was just a guy the kids called Hoptoad Harry because of the way he walked. So I cried and stroked a big red A+ on top of his paper.

JAKE: (Pg 24-25) Two years later, on the last day of the school year, Harry Dunning limped up to me after homeroom period and offered me his hand.

HARRY: I just want to thank you for everything

JAKE: You already did that, as I remember.

HARRY: Yeah, but this is my last day. I’m retiring. I’ll never forget that A-plus. I framed that, too. Got it right up beside my diploma.

JAKE: Good for you. (to audience) And it was. It was all good. His essay had been primitive art, but every bit as powerful and true as any painting by Grandma Moses. In spite of his grammatical lapses, Harry Dunning had written like a hero. On one occasion, at least. (Pg 26) The intercom on the wall cleared its throat.

INTERCOM: Mr. Epping, you have a phone call -- Al Templeton.

JAKE: (to audience) Al Templeton, owner of Al’s Diner. Curious as to why Al would call me. Ours had always been strictly a cook-and-client relationship. (goes to phone, punches in his extension)

AL: (Pg 27-28) Jake, I need to see you. It’s important.

JAKE: Can I ask—

AL: I expect you to ask plenty, and I’ll answer, but not over the phone.

JAKE: I promised I’d come down in an hour or so. And he hung up, without even a goodbye. Al’s Diner was housed in a silver trailer across the tracks from Main Street, in the shadow of the old Worumbo mill. I went up the steps, then paused. The sign WELCOME TO AL’S DINER, HOME OF THE FATBURGER! was gone. In its place was a square of cardboard CLOSED & WILL NOT REOPEN DUE TO ILLNESS. THANK YOU FOR YOUR BUSINESS OVER THE YEARS & GOD BLESS. What kind of serious illness came on in 24 hours? I left Al’s last night at 5:45 and he’d been fine. The door opened while I was reaching for the handle, and Al stood there looking at me, not smiling. Al was seriously ill. I could see that. (Pg 29) In the hours since I’d last seen him, Al Templeton appeared to have lost at least 30 pounds. Nobody loses 30 pounds in less than a day, nobody.

AL: How do you like the new me, Jake? I’ve got a lot to talk about and I think you’re the only one who might listen. (Pg 32) I want you to see something. It’ll be quicker that way. Only seeing isn’t the right word. I guess experiencing is a lot closer.”

JAKE: (Pg 33) He led me past the double grill, the sink, the FrostKing fridge and the freezer. He stopped in front of the dishwasher and pointed to the door at the far end of the kitchen.

AL: That’s it. Through that door. You need to find out for yourself.

JAKE: (Pg 34) I’d be lying if I said my heart didn’t kick into a higher gear when I turned the knob and pulled. But when Al reached past my shoulder and turned on the light, what I saw was— Well, a pantry. (to Al) How long is this going to take, Al?

AL: (Pg 36) I want you to give me your cell phone, your wallet, and all the money you have in your pockets, coins included. Please. Please, Jake. (Jake hands over the items) [And] It’ll take as long as you want, because it’ll only take two minutes. It always takes two minutes.

JAKE: (Pg 38) I did as he asked, feeling like the world’s biggest dope. One step . . . lowering my head to keep from scraping it on the aluminum ceiling . . . two steps . . . now actually crouching a little. A few more steps and I’d have to get on my knees. That I had no intention of doing, dying man’s request or not. (to Al) Al, this is stupid . . .

AL: (Pg 39-40) Go on. Nothing’s going to happen to you, buddy. Just go on.

JAKE: So I did. God help me, I did. And all at once there was a pop inside my head, exactly like the kind you hear when you’re in an airplane and the pressure changes suddenly. I was no longer in the pantry. I was no longer in Al’s Diner, either. I was outside but the diner was gone.

AL: (Pg 41) You can come back the same way you got there. Feel for the steps. Look around a little, then come back.

JAKE: It was Al’s voice, but very faint. (looking around incredulously) (Pg 48) On the left was a rack of newspapers. No New York Times, but there were copies of the Portland Press Herald and one leftover Boston Globe. The dates on both were Tuesday, September 9, 1958.

AL: (Pg 53) Relax Jake. You’re back. What do you think?

JAKE: How long was I gone?

AL: Two minutes. I told you, it’s always two minutes. And it’s always 11:58 A.M. September 9, 1958. Every trip is the first trip.

JAKE: You found this by accident?

AL: The first time, I actually fell down those stairs, like Alice into the rabbit-hole. I thought I’d gone insane. (begins violently coughing)

JAKE: (Pg 54) He can’t go on this way. He’s no more than a week from the hospital, and probably just days. And wasn’t that why he’d called me. Because he had to pass on this amazing secret to somebody before the cancer shut his lips forever.

AL: (Pg 65) You can go back, Jake. You can change history. Do you understand that? (Pg 83) John Kennedy can live. You can save him, Jake.

JAKE: And would that really make things better? There were no guarantees. I told him goodnight and left. [But] one more thought came before I dropped: (Pg 84) It wasnt a day but a night. The night that change my life was the night my father murdirt my mother and two brothers. . . . (Pg 85) I ran for my study. I don’t keep all student work, but I made it a habit of photocopying the best essays. I pulled open the bottom drawer and after 15 minutes, I found it . . . I never go see horra movies because on Halloween night in 1958 I lived thru one.

AL: (Pg 65) (Echoing) You can go back, Jake. You can change history. ******The Next Day at Al’s Diner *****

AL: (Pg 87) (reading Harry Dunning’s essay) Jesus! Son of a b*** killed his wife and three of his kids with a hammer?

JAKE: (Pg 89) It took Harry years to recover from that night. Could [his life] have been better? Yes. Can I make that happen? Based on yesterday, maybe I can. (Pg 90) If I can stop his old man from swinging that hammer. And the three other kids. Surely some of them will get married if they live to grow up. I want a better example of what happens when you change a watershed moment. I need that before I go monkeying with something as big as the Kennedy assassination. (Pg 116) Forty minutes later I was headed north to Derry behind the wheel of a 1954 Ford (Pg 165) In the weeks before Halloween, I came to believe that Derry wasn’t like other places. Derry wasn’t right. Something wrong, something bad. Certain empty houses that seemed to stare like the faces of people suffering from terrible mental illness. An empty playground with the roundy-round slowly spinning even though there were no kids to push it and no wind to turn it. It screamed on its hidden bearings. Something wrong, something bad. (Pg 167-168) I anticipated no problems when Halloween came. Dunning might come in his car rather than on foot, but I knew what it looked like. It would be after dark, according to Harry’s essay, but there were streetlights. Unless he was totally fixated on what he’d come to do, Dunning would almost certainly see me running at him. I had the pistol, but it was only dead accurate up to fifteen yards. I couldn’t wait until he actually got in the house because according to the essay, by the time Harry came out of the bathroom, all of them but Ellen were dead. I hadn’t traveled across more than half a century to save just one of them. (Pg 188) Ten minutes until the start of The New Adventures of Ellery Queen. How far along had Ellery Queen been when Dunning arrived? Harry’s theme hadn’t said, but I was guessing not long. (Pg 191-192) I heard a car moving far faster than any reasonable driver would have dared to travel on a street that was no doubt full of children wearing masks and carrying trick-or-treat bags. I knew who it was even before it screeched to a stop. Inside 379, Doris Dunning was sitting on the couch with Troy while Ellen pranced around in her Indian princess costume. Even if it kills me, I thought. Even then. Because this is now. This is them. The back door would be locked. I was so sure of this that I almost tumbled off the stoop when the knob turned and it swung outward. I stepped into a kitchen that still smelled of the pot roast Mrs. Dunning had cooked I heard her say “Frank? What are you doing here? What is that? Why have you. . . get out of here!” Then she screamed.

I ran through the arch and stopped there with my mouth open. Doris was on the living room rug. He had already broken her arm and dislocated her shoulder as well. He grabbed Ellen by her hair and heaved her. (shouting) DUNNING! STOP! (Pg 193) I pulled the trigger of the revolver. The bullet took him in the shoulder. He twisted sideways with the impact, then came on again.

HARRY: (as a child with his air rifle) Stop it, Daddy! Stop or I’ll shoot you!

JAKE: Arthur “Tugga” Dunning was crawling toward me, toward the kitchen. Dunning brought the sledge down on Tugga’s head. The boy’s face was obliterated. Bone fragments leaped high in the air. I fired again. (Pg 194) Dunning went down, feet in the living room, head in the archway between the living room and the kitchen. All of this happened in less than a minute; maybe only 30 seconds. Life turns on a dime, and when it does, it turns fast. (to Troy) Get out! Take your sister and get out!

JAKE: (Pg 196) I went into the bathroom, grabbed a towel, scrubbed my bloody face and stepped out into the kitchen. The boy who had brought me here was standing on the faded linoleum by the stove and watching me. Although it had probably been six years since he’d sucked his thumb, he was sucking it now. His eyes were wide and solemn, swimming with tears. Here was a boy who had just experienced something that would no doubt traumatize him, but he was also a boy who would never grow up to become Hoptoad Harry. Or to write a theme that would make me cry.

HARRY: Who are you, mister?

JAKE: Nobody. (to audience) He deserved more than that, though. The sirens were closer now, but I turned back. (to Harry) Your good angel. (to audience) Then I slipped out the back door and into Halloween night of 1958. *****

JAKE: (Pg 197) [When I returned to the diner] I thought of Harry, unhurt. And Ellen, who wasn’t deep in a coma from which she would never emerge. And Troy. And Doris. Her badly broken arm might hurt her for the rest of her life, but at least she was going to have a life. (whispering) I did it, Al (to audience) But what had I done to 2011? (Pg 213-214) I dialed directory assistance. There was no listing for Doris, Troy, or Harold Dunning in Derry. As a last resort I tried Ellen. Halfway through the fourth ring, a woman answered.

JAKE: I knew your brother Harry a long time ago. I thought maybe I’d try to get in touch.

ELLEN: Well, I’m sorry to tell you this, but Harry’s dead. A long time ago. In Vietnam. During the Tet Offensive.

JAKE: Oh God, I’m so sorry. (to audience) I sat down, feeling sick to my stomach. I’d saved him from a limp and some mental fogginess only to cut his lifespan by forty years or so? Terrific. The surgery was a success, but the patient died.
```

---

## IC-0376: Heal

- Title: Heal
- Author (byline): Carl Sasoon
- Work: Fast Horse Plays, Round 2
- Publisher: Fast Horse Drama
- Publication date as stated: June 2012
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SPEAKER, SOPHIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1494
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carl Sasoon
Book: Fast Horse Plays, Round 2
ISBN: 978-0615668734
Publisher: Fast Horse Drama
Date (Month/Year): June 2012
```

### Introduction (context only: never use it for content warnings)

```text
He never expected a random act of violence would change the trajectory of his life. He never expected to live without her. He never expected to . . . . Heal by Carl Sasoon.
```

### Performance text (classify this)

```text
The unnamed speaker is a shy, somewhat nervous man in his mid to late twenties. He is a scientific genetic botanist and tends to some plants while he speaks.

SPEAKER: The problem with Sterling Silvers is that they have a particular susceptibility to spotty blight. Peter Winslet bred Sterling Silver in 1971, claiming that, and I quote, "In the correct light, the silvery-white blooms of the rose take on a certain bluish cast..." Well, I don't know, but it ain't blue, it's just, well, silvery-white. Beautiful rose, but not blue. A blue rose, is of course, sort of the start of all of this, I suppose. You see, it was two weeks before Valentine's Day that I asked Sophie out to dinner for the first time, only to be challenged by her response of,

SOPHIE: "You got it buddy, I'll see you there with a dozen baby blue roses."

SPEAKER: And that night was a successful evening. I successfully spilled red wine all the way down my white shirt, and, I . . . uh . . . successfully won Sophie over with my apparent social grace and charm -- or lack thereof. I didn't have any blue roses to bring her that night, but she married me six months later. And, uh, I adored her. So, when the little boy who never really fit in grew up to become a genetic botanist who never really fit in . . . he, uh, he never expected that he would find his queen.

SPEAKER: When you have everything you could possibly desire, why is it that your mind refuses to rest. Perhaps we all struggle with such . . . unease. Perhaps. There were times her blue eyes would flicker with . . . something . . . worry, restlessness . . . I wasn't certain. I'd awaken, hours before dawn, to find Sophie sitting at the edge of our bed . . . and as she was lost in her own thoughts, I would hold her and she would murmur,

SOPHIE: "I’ve been worried about us, Babyluv."

SPEAKER: There is no science to resolve the contortions of our psyches. And, so, I would hold her, and whisper quiet things, private things. Sing to her quietly as I held her, "You are in my blood like holy wine. You taste so bitter, so bitter and so sweet. I could drink a case of you and I would still be on my feet. I would still be on my feet. . .*” (link to music and lyrics at the end of this selection) Sing to her until she slept and whatever demons or gods were tormenting her had fallen silent. I could not place this worry, and I could not fix it.

I have a temperature-controlled greenhouse, connected to the small lab, and, uh, that's where I was the night that my cell phone rang. It was deep into winter, when I answered the phone. And Sophie, spoke quickly, urgently, I suppose would be the best way to describe it, she said,

SOPHIE: "I will always be near to you, Babyluv. Close enough to touch"

SPEAKER: . . . and the line was gone. Sophie didn't come home that night. I found myself downtown the next morning, speaking with a woman wearing a white lab coat and I was just on autopilot, an actor on a stage, improvising lines for a play I had not written. And in this play, this grand drama, this woman with kind and tired eyes took me to a room where the lights were very bright and the air was very cold this woman, she . . . showed me Sophie. And even though this was no longer a play it looked as if she were wearing stage makeup, because she had long, jagged slashes of red across her face where someone had cut her. Her blonde hair fanned out, matted in blood. Her body was covered with dark red. If this is difficult for you to hear, then perhaps imagine how it was for me to see. Because that was my life . . . my Queen on that table. And, umm, I could not fix her. I would have taken my Babyluv right away from there, taken her back to the lab and used anything, anything to breathe life back into that body, but it was impossible. There was no science to fix this. And so, instead, I leaned my face into Sophie's . . . "I remember that time you told me, you said love is touching souls, surely you touched mine, cause part of you pours out of me in these lines from time to time . . .*” (link to music and lyrics at the end of this selection) I didn't want to leave Sophie alone there, she must have been so cold, but the woman led me away. I ask you, does worry manifest as premonitions? I don't know . . .

They did not have to look. The man, David Smith, turned himself in. I made a request to go down and speak with [him] and the request was granted. What I need to explain is that the bloodlust, the hunger that was inside of me was insatiable, and, so, I, uh, I did my research. There are things you can do, things you can bring in, that you can get past the elaborate systems of security. Even though I had never seen this man's face, I could envision the scenario in complete detail, the splattering of blood, the ending of his life.

In the weeks before I went to meet this man, Sophie began to visit me. I would see her, I would see her in the way that this man had left her, and often times I could not bear to look.

SOPHIE: I don't know where to go, Babyluv.

SPEAKER: I would reach out and I could not touch her.

SOPHIE: I need you here with me.

SPEAKER: I could not bring her back.

SOPHIE: I am so cold, Babyluv.

SPEAKER: If there was a paradise, I could have found to be with her, I would have gone. (Beat) The day came for me to go, and I was prepared. And they led me into a small room with a table and two chairs, and in one of the chairs sat David Smith - and he was just so, so ordinary. Here in front me, this was the man who had murdered my wife, and in doing so, separated me from the land of the living. How many seconds did I have, if I wasn't fast enough I would fail. Not yet. Instead, I look directly into David Smith's eyes, brown pools and I ask him, "Why did you kill my wife?"

I don't believe David Smith blinked before he said, "I don't know. I think I needed to feel alive."

I sat very still, I did not move my eyes from his, "I loved my wife and you ended her life for no reason."

He dropped his gaze then, "I'm sorry. There's something wrong inside of me. Something I don't know how to fix." And then David Smith began to cry.

(Long Beat)

We cannot fix something when we do not understand why it is broken. Or how it came to be. So I told this man, "I will try to forgive you, only because I will never forget my wife. My Sophie."

SOPHIE: "I’ve been worried about us, Babyluv."

SPEAKER: Sophie had visited almost every night in the days before I went to meet that man. And as sure as I stand here, she knew.

SOPHIE: “You have to heal, my sweet, sweet boy.”

SPEAKER: I don't know how. I need to end this. I need you.

SOPHIE: “You have me, always. Forever. And you know mercy in your heart. I don't want to worry about us anymore. I don't want to worry about you, Babyluv Don't make me worry.”

SPEAKER: And so, I could not. (Beat – he returns to his roses) I was worried that the blooms would be so fragile, but look at how strong they are. And how blue. As blue as the ocean, or lapis lazuli stones . . . or Sophie's eyes. Sophie's blue. It's taken me much, much longer than I would have planned to give her a dozen baby blue roses, but here they are, and I can only hope they are everything she would have wanted them to be. (he begins to mix a concoction in beakers from his lab – a suicide cocktail – He contemplates drinking, but keeps stopping himself to talk)

She still comes, you know, but not nearly as often, and her face now is as perfect and as clean as ever, and I know, for certain, is that there is a paradise, a beautiful place and that I will arrive there, when the time is determined, and I will be with my Sophie for eternity, and there will be no need for science of any sort and nothing will need fixing. (he drinks from the beaker) We will be surrounded by fields of blue roses -- every shade of blue the mind's eye has never even imagined. I see us dancing in groves of blue roses, bright, bright blue in the full bloom of sunlight.

SOPHIE: I am not worried about us anymore, Babyluv.

SPEAKER: I'm going to be there, Sophie, and I know you'll be waiting. (He sings softly he re-unites with Sophie and they dance) "You're in my blood like holy wine, you taste so bitter and so sweet, I could drink a case of you darling, and I would still be on my feet. I would still be on my feet. Mmm. . . hmmm. . .*” (link to music and lyrics at the end of this selection) (He collapses to the floor a smile on his face)
```

---

## IC-0377: Hello Herman

- Title: Hello Herman
- Author (byline): John Buffalo Mailer
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: April 2010
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: HERMAN, CLARKSON, SENATOR JOHN COX, CHILDREN’S AID SOCIETY REP, LAX, MR. PHELPS, SUSAN, OFF STAGE VOICE OF CRIBB, MARSHA, HARMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1641
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Buffalo Mailer
ISBN: 978-0822224105
Publisher: Dramatists Play Service
Date (Month/Year): April 2010
```

### Introduction (context only: never use it for content warnings)

```text
1999 - Columbine, Colorado. 15 people dead. 2012 - Sandy Hook Elementary, CT. 28 people dead. 2018 - Parkland, Florida. 17 people dead. And while the COVID-19 pandemic appears to have interrupted the trend line, it does not mean schools are “safer.”

It’s hard to empathize with someone who carries out a school shooting. The brutality of their crime is unspeakable. Whether the shootings were at Columbine, Sandy Hook or Parkland, they have traumatized students and communities across the US. But understanding the culture and the mentality of school shooters are the keys to prevention. Unfortunately, our society seems to be focused on punishment rather than prevention. Are consequences and active shooter drills the answer? Or are we asking all the wrong questions?

Hello Herman by John Buffalo Mailer
```

### Performance text (classify this)

```text
HERMAN: (Pg 40) (meanacing, he struts around with a gun – this is the happiest moment of his life) Paul! Paul Schruber! Today is your lucky day! Because you are so valuable to our school, you get to live! Now, take a bow and get out of my gym, Paul. (Paul moves toward the exit) You forgot to take a bow! (Herman shoots him in the knee – Paul falls down, screaming in pain) Shut up! ******

CLARKSON: (Pg 12) Forty-three students were shot before [Herman]Howards was apprehended. “Bloody Broome” as it is now being called, is the worst high-school massacre in the history of America. (Pg 15) While there remains no clear motive for the killings, what has become very clear, is that today’s teenage culture is rampant with violence . . . Senator John Cox issued a statement to the press this morning. ******

SENATOR JOHN COX: (Overlap lines with Children’s Aid Society Rep) Herman Howards is not a common criminal; he is a terrorist, pure and simple. A coward. He must be executed. And his execution ought to be televised nationally, so that America’s children can witness what happens when you disregard the value of life.

CHILDREN’S AID SOCIETY REP: Herman Howards is a troubled child in serious need of psychiatric treatment. What kind of message does it send to the world when America starts executing our own children on television? Killing people does not stop people from killing people.

LAX: (Pg 11) This Week’s Topic: High School Terrorists . . (Pg 18) (a buzzer goes off. We hear the sound of a prison door opening. Herman enters) (Pg 25) (To Herman) Hello, Herman

HERMAN: “Hello, Herman!” Starring Herman Howards and Lax Morales. I get top billing? I mean, it is my story.

LAX: Get it straight, Herman. I’m not here to turn you into a rock star. I’m here because there’s a world outside that thinks you should be electrocuted, at age sixteen, on national television. That’s a story. That’s important.

HERMAN: (Pg 19) (explodes) I’m an individual! Don’t forget that! You think just anyone could do what I did? No sir. There’s only one Herman Howards, and now history will remember me.

LAX: You don’t talk like the average sixteen-year-old kid.

HERMAN: I’m not your average sixteen-year-old. I’m America’s worst nightmare.

CLARKSON: (Pg 30) We’ll be right back. ******

CLARKSON: (Pg 12) (Overlap lines with Clarkson (2)) While parents of the formerly peaceful community of Broome, Iowa grieve the tragic loss of their children. Parents all over suburban America are wondering if their town will be next. ******

LAX: (Pg 18-19) May I interview you now? (long beat)

HERMAN: How much money do I get for talking to you?

LAX: You don’t get anything. Any money goes to the families of the victims. Besides. I thought you wanted to tell your story. (beat) Did you get picked on a lot at school, Herman?

HERMAN: (shrugs it off) The jocks call me names cause I’m small. They’d push me around.

LAX: You kids still play Doom . . . Postal?

HERMAN: (Pg 20) I own it (he begins to ramp up) You’re a postal worker. You go into the office one day cause you’ve had enough of people’s crap and you shoot everyone up til they’re all gone. (Herman laughs)

LAX: Your mom supports you in playing games like Postal?

HERMAN: I don’t think she knows anything about it. (Pg 28) We don’t interfere with each other. She’s very good about giving me my privacy.

LAX: What about your father? (long beat)

HERMAN: (Pg 35) He left when I was eight.

LAX: (Pg 28) When you were eleven, your sister was hurt in a hit-and-run, right? She died a few days later.

HERMAN: Yeah.

LAX: It happened right outside your house . . . did you go out and help her.

HERMAN: I was eleven. There wasn’t a whole hell of a lot I could have done, now was there. (Pg 29) You really don’t get it!

LAX: Don’t get what?

HERMAN: (Pg 27) Jesus Christ you’re asking stupid questions. I thought you were supposed to be some kind of hotshot reporter. (Pg 29) I’m done talking to you today. (long beat)

LAX: (Pg 27) Okay, let’s cut to it. (Pg 40) Tell me more about the day you did it. You rounded up all the kids in the gym. . .

HERMAN: (Pg 20-21) Yeah (Herman smiles) You had to be there. At one point this girl started running for the door. (gunshot) I clipped her right in the back of the head and her face exploded and landed all over some kid (breaks into laughter) Thought she was home free . . . when all of a sudden, “OOPS! THERE GOES MY FACE!”

LAX: Do you even know the girl’s name?

HERMAN: She was background. Not a key player.

LAX: It was a game, wasn’t it?

HERMAN: It’s all a game, Lax. (Pg 37) If I could just get one more game in, I’d be happy.

LAX: (Pg 26) You feel no remorse?

HERMAN: (pause) I didn’t want to kill Mr. Phelps. *****flashback******

(Mr. Phelps enters and slowly walks toward Herman)

MR. PHELPS: (Pg 40) There’s still time. Stop this madness, Herman.

HERMAN: Sit down! I don’t want to kill you! (Phelps keeps walking toward Herman, his hand out asking for the gun. Gunshot. Phelps falls) (to Lax) I had to shoot. He would have grabbed me if I didn’t. He looked so stupid. I almost started laughing, but out of respect, I didn’t. (Pause – flashback continues) Are there any other teachers in the room? (to Lax) I knew Ms. Cribb was there. No one came forward, so I called up three kids who were lying on the floor near me. Susan, this bitchy girl no one really liked, James, the editor of the school paper and Marsha, the hottest girl in school. (flashback continues) (Pg 42-43) Hello! If you are a teacher, please come forward and take a bow! (no response – he puts the gun to Susan’s head) Oink!

SUSAN: What?

HERMAN: Oink! Like in Deliverance. Squeal! (She tries, but is crying too much)

SUSAN: Jesus, please protect me. Jesus, please protect me . . . .

HERMAN: (gets a kooky expression on his face, then starts to laugh) Not today. (Gunshot- end flashback) (To Lax) I shot her at an angle, so the bullet would go through her skull and blood would splatter all over Marsha. [She] walked around those halls like she owned the place. Because she was a nice-looking piece of . . . . You think that’s gonna fly? (shakes his head) It’s the ones like me are going to run the show! This is the only way to make you assholes finally pay attention to us. I wasn’t about to settle for some rinky-dink shit. Oh, no. I blew that dumb b****’s head off and made sure a little got on James as well. But I was never going to kill him. I wanted him to live, so he could write about the day in his precious paper.

OFF STAGE VOICE OF CRIBB: Please, Herman, Stop! (Gunshot)

HERMAN: I shot Cribb right in the mouth. Isn’t she at the hospital or something?

LAX: They had to amputate her jaw. What was left of it. She’ll have to be fed intravenously.

HERMAN: Awesome! She deserved it. Gave me a C- in phys-ed. Can you believe that? A C-! Unreal! Lax? Lax, you still with me?

LAX: (Pause) Why don’t we take a break. I need some coffee.

CLARKSON: (Pg 44) (Off-stage) The verdict came in today on The People vs Herman Howards. Howards will be the first minor executed in the state of Iowa.

HERMAN: (Pg 43) Whatever . . .

LAX: (re-inters) (Pg 46) Are you ready to die, Herman?

HERMAN: When you die, it’s “game over.” Nothing. Blackness.

LAX: What about “reset”?

HERMAN: When you hit “reset,” the game you played before doesn’t have *anything* to do with the next one. All the characters come back to life.

LAX: That’s not how it works in real life. Once a kid is killed, he doesn’t come back.

HERMAN: (Herman doesn’t speak. His face changes. It is as if he’s beginning to worry - softly) (Pg 47) I dream they come back . . . I keep shooting. It’s like I have unlimited bullets and they have unlimited lives. How can dead people haunt your dreams?

LAX: Why don’t you ask them the next time you go to sleep?

HERMAN: Shut up! I’m fine! (Pause) You want to hear what else happened or not? The police came to the door and I threw a pipe bomb into the middle of the crowd. It got crazy. I was just running around shooting people left and right. It was anarchy. Awesome! (flashback as Herman narrates) I ran up behind Marsha and put the forty-five to her back. (To Marsha) Ready to die, prom queen?

MARSHA: Please don’t. I’ll do anything. I want to see my mom again. Pleeeeaasse!

HARMAN: Isn’t it funny? She was ashamed to be caught taking to me before that. (Pg 48) You know what that kind of power feels like? I shot her down low. Bashed her nose with the butt of my gun and left her there to bleed. I’m glad she survived. To learn what life is like when you’re not the prettiest girl in school.

LAX: (Now) You’re a teacher? – What did they learn, Herman?

HERMAN: Maybe they learned to be a little nicer to each other. [But] I doubt it. The world’s gotta see more kids like me before they finally get it. That’s okay, they will.

LAX: They’ll finally get it?

HERMAN: No. (he grins) The world will see more kids like me.

LAX: (Pause) We have real problems in this world, Herman. Melting glaciers, massive unemployment, crumbling nations with nuclear missiles. You think I have time to worry about some depressed kid from the suburbs going into his school and killing people? Why didn’t you just wait to go to college and find friends there? I mean, really!

HERMAN: It worked, didn’t it? You’re here, aren’t you? It was the only way to get you to pay attention to me.

LAX: You’re going to be killed. You destroyed hundreds of lives. You inflicted pain on innocent people. You gave up everything just to be on my show?

HERMAN: (Pg 49) I wasn’t about to go through life being unnoticed. (Pg 42) Do you know what the largest generation is? Mine! Believe me, we’re going to do a hell of a lot more than “Rock the Vote.” This is the only way to make you assholes finally pay attention to us!

LAX: (Pg 49) This is not about your generation, Herman. This is about you doing unspeakable things.

HERMAN: You have to do the unspeakable if you want to be noticed.

LAX: You think anyone’s going to care about you in two months? You’re gonna be a footnote, listed next to a bunch of other forgotten footnotes.

HERMAN: Google me in twenty years, Lax. Then we’ll see who’s right. (Pause. Herman’s entire façade has melted and now we are left with a little boy) (Pg 50) Between you an me? I’m scared. I don’t want to die. Sometimes I wish I could take it back. You know, hit reset. But I can’t. (He cries) ******break*******

CLARKSON: This is Chet Clarkson reporting live at the execution of Herman Howards. The highest viewed event in television history. Senator . . . your thoughts?

SENATOR JOHN COX: America will see today that the government of the United States will not allow our children to be in danger any longer. Killing people may not stop people from killing people, but seeing the execution live sure as heck will.

CHILDREN’S AID SOCIETY REP: (Pg 15) Herman Howards is . . . [was] a troubled child in serious need of psychiatric treatment. What kind of message does it send to the world when America starts executing our own children on television?
```

---

## IC-0378: Homecoming King

- Title: Homecoming King
- Author (byline): Hasan Minhaj
- Work: Not specified
- Publisher: Scraps from the Loft.com
- Publication date as stated: (2017) Uploaded May 21, 2020
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: HASAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1629
- Already set (do not supply): none

### Source block (context only)

```text
Author: Hasan Minhaj
On-Line Transcript:
https://scrapsfromtheloft.com/comedy/hasan-minhaj-homecoming-king-transcript/
ISBN: N/A
Publisher: Scraps from the Loft.com
Date (Month/Year): (2017) Uploaded May 21, 2020
```

### Introduction (context only: never use it for content warnings)

```text
Named to TIME's "100 Most Influential People in the World," Hasan Minhaj is a 1st generation American whose Muslim family immigrated her from India before he was born. And although he got his start as a stand-up comedian, he has come to be known for much more than his comedy. He draws on his personal history and the immigrant experience to explore America’s modern cultural and political landscape with depth and sincerity.

In fact, according to Lauren Feldman, associate professor at Rutgers’ School of Communication and Information, it is just this type of boundary-pushing “comedy [that] can play an important role in challenging people to address critical social issues.” *

I give you . . . Homecoming King by Hasan Minhaj
```

### Performance text (classify this)

```text
HASAN: My parents physically never saw each other. Years ago in a town in India, population 990,000 — that’s a small town — my dad heard a buzz in the streets about this woman named Seema, my mom. And, Seema was like the iPhone [insert latest iPhone model here]. “Have you heard of Seema? She’s slim. Her family owns a camera.” My dad was like, “A camera?” So, he runs to my grandfather’s house and lays it on the line. “I’m going to America. I want to marry Seema.” In ten minutes, the man married a woman he had never laid eyes on.

HASAN: So. my dad marries my mom, they come to the States, they have me, in Davis, California. But Davis was, like, super white. Roll call was a problem. It was a big deal for a lot of us. I would get, like, “Hanson Minaja . . . Sahan Minha . . . Saddam Hussein.” [beat] I’m not Saddam.

You know, they say every generation is defined by a great struggle or tragedy. So when 9- 11 happened I was in high school. My dad sits everybody down. He’s like, “Hasan, whatever you do, do not tell people you’re Muslim or talk about politics.”

“Alright, Dad, I’ll just hide it. This [gestures to his skin color] just rubs off.”

We’re sitting there. Phone rings. I run, but my dad beats me to the phone. “Hello?”

I grab the second phone. I hear a voice. “Hey, you sand n*gger, where’s Osama?” He looks at me. “You can hear me, right? You dune coon. Where’s Osama? Hey, 2631 Regatta Lane, that’s where you live, right? I’m going to kill you.” Click.

And my dad’s looking at me. Do you ever see your parents, and you see the mortality in them? I’m looking at my dad and I see all five-seven of him. And that’s when I realize I’m a darapok. I’m a scaredy-cat.

We can speak two languages! I should have said something. I didn’t. We sit down. I hear “thud, thud, thud” outside. Me and Dad run outside and all the windows on the Camry, the immigrant car of choice, are smashed in. My backpack’s open. “They stole my stuff.” I’m mad. They know where we live, they’re timing this, so they’re watching us. I’m looking in the trees, the bushes . . . I look back, and my dad is in the middle of the road sweeping glass out of the road like he works at a barbershop.

“We’ve got customers. Log kya kahenge? We’ve got to clean this up.” Zen! Brown Mr Miyagi, just, like, not saying a word.

I’m like, “Why aren’t you saying something? I’m asking you, say something!”

He looks at me and goes, “Hasan. . . These things happen, and these things will continue to happen. That’s the price we pay for being here.”

We really are from two different generations. My dad’s from that generation where he feels like if you come to this country, you pay the American dream tax. You endure racism, and if it doesn’t cost you your life, pay it. There you go, Uncle Sam. But for me, I was born here. So I actually have the audacity of equality. I’m like, “I’m in Honors Gov. [takes out text book] I have it right here. Life, liberty, pursuit of happiness. All men created equal.” It says it right here, I’m equal. I’m equal. I don’t deserve this.

But as soon as I say that, he looks at me like I believe in Santa. “Hasan, you’ll never understand.”

“I’ll never understand? Dad, you’re the guy that will argue with the cashier at Costco when he doesn’t let you return used underwear. And now you want to be the bigger man? Now you’re like, ‘Let’s be reasonable with the bigots.’ What?” And then he just walks back into the house with glass in his feet. And I honestly don’t know who is more right. Maybe he’s right. Put your head down. Be a doctor, get a house in the burbs, let them call them whatever you want. But isn’t it our job to push the needle forward little by little? Isn’t that how all this stuff happens? I don’t know. The pendulum swings back and forth for me. And I know 9/11 is a super touchy subject. I understand. Because when it happened, everyone in America felt like their country was under attack. But on that night, September 12th, it was the first night of so many nights where my family’s loyalty to this country was under attack.

As immigrants we always have to put on these press releases to prove our patriotism. We’re auditioning. “We love this country, please believe me.” Nobody loves this country more than us.

I fell in love here. Six years old, Janice Malo. I saw her in the sandbox. I run up to her. First grade. “I love you!”

“You’re the color of poop.” That’s memory number one.

In the third grade, Miss Anderson said, “Write what you want to be.” Some kids were like, “an astronaut,” or “a firefighter.” I was like, “I want to be white.”

So, by my senior year of high school, I had yet to go to a school dance, I had been cut from the basketball team, and I had just got off this medicine called Accutane so my skin and face was peeling. I’m crushing life. Out here, killing it. But there was one bright spot, this girl named Bethany Reed. Her family had just moved from Nebraska to Davis, and we were in AP Calc together, but… we had chemistry.

One night she was like, “Hey, we always study at my house. Why don’t we study at your house?”

What, invite you over to my house? You walk in: “What language are you guys speaking? What’s that smell?” I’m not going to open myself up to that. But I was like, “No, she’s different.”

“Mom, Dad, a school friend is coming over. Everyone, please be normal.”

My dad is like, “We are normal.” Killing me, you know what I mean? “Hasan, we’re normal. Be proud. You should be proud.”

We get there. We’re sitting at my living room table. My mom and dad are arguing in Hindi. My mom is frying pakoras. You’ve got to ease your way in. She’s from Nebraska. It’s all coming at this girl. It’s too much. So, I’m looking at her, like, “Don’t say anything. Please don’t say anything.” She looks up from her book, and she’s like, “You know what? This is really nice. We should do this more often.” And I look at her, and I’m like, “Oh, my God. I love you. You see me. I don’t got to change who I am? I can be me!”

She’s like, “Listen, you know, ever since my family moved from Nebraska, you’ve been my best friend. And you’re really special to me. This year wouldn’t be the same without you. So I was wondering, will you go to prom with me?”

The night of prom rolls around. I put on the JC Penney suit. Spray on the Michael Jordan cologne. Six puffs, one for each championship. You don’t want to overkill it with the MJ cologne. Don’t be tacky. I’m scaling down the side of my roof, scraping my knees. I jump off the roof. It’s like 20 feet. I jump off, I somehow land, I get on my bike. It’s beautiful, the sun is setting, it’s one of those gorgeous evenings. And I’m biking with my knees bowed out. So my slacks don’t get caught up in the chains. Fast enough to get there, but slow enough to not get pit stains. I’m balancing the corsage.

I get to her house. I park my bike. I’m walking up to the doorstep, and I’m about to ring the doorbell when I’m like, “Wait. 30 second time-out. Do you understand what’s about to go down? You’re about to go to prom with Bethany Reed. This is the American dream. This is what Dad fought for.” Ding-dong.

Mrs. Reed opens the door. She has this look of concern. And I look over her shoulder, and I see Jeff Burke putting a corsage on Bethany’s wrist. (long beat)

And she’s like, “Oh, my God, honey, did Bethany not tell you? Sweetie, we love you, we think you’re great. We love that you come over and study. But tonight is one of those nights . . . We have a lot of family back home in Nebraska and we’re going to be taking photos, so we don’t think you’d be a good fit. Do you need a ride home? Mr Reed can give you a ride home.”

And I was like, “No, I have my bike.” And I just biked home and played Mario Kart. That’s the nicest I’ve ever been dressed, playing Mario Kart. (long beat) The sad part is, I felt bad for being there. Who was I to ruin their picture-perfect celebration? You’ve seen movies. How many times do you see that on screen? And it’s not like they were yokels yelling “sand n*gger!” I could let that pass. I didn’t know that people could be bigoted even as they were smiling at you. It’s hard when you see people saying they love you but they’re afraid at the same time. And I didn’t know what that meant. (long beat)

Maybe we have a race problem. There is bigotry that happens every day because we’re too afraid of the Other. Someone who’s not in our tribe. I wish I could tell 18-year-old me, “Hey, man, don’t let this experience define you. It’s good people and bad people. Irrespective of creed, class, color, find those good people. Because love is bigger than fear.”
```

---

## IC-0379: Hydraphobia

- Title: Hydraphobia
- Author (byline): Gary R. McClain
- Work: Body Positive magazine, Vol. XVII, No. 2
- Publisher: Body Health Resources Corporation
- Publication date as stated: July 2004
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1851
- Already set (do not supply): none

### Source block (context only)

```text
Author: Gary R. McClain
Book: Body Positive magazine, Vol. XVII, No. 2
ISBN: N/A
Publisher: Body Health Resources Corporation
Date(Month/Year): July 2004
```

### Introduction (context only: never use it for content warnings)

```text
The one feeling that I have heard from practically everyone who is touched by HIV/AIDS is fear. Fear is one of the primary feelings that gets in the way of hope. And we need hope to be fully alive with HIV/AIDS. So how can we deal with fear? Faith is one powerful answer. If you love someone living with HIV or AIDS, "Fear not; only believe." Believe that you can translate your fear into loving acts of kindness. As you focus on loving your friend or family member with HIV/AIDS, the fear will fall away. Hydraphobia by Gary R. McClain brings to life this fear of the Hydra: A Greek root meaning a multifarious evil, or an evil having many sources; not to be overcome by a single effort.
```

### Performance text (classify this)

```text
I remember spending the week after our first date waiting for the phone to ring, or at least for it to ring with Alby on the other end. I had asked him out, after all, so now it was his turn. But the pain ... I thought about him while I was getting ready in the mornings and on the subway ride to school. I thought about him when I was sitting in my office, waiting for the next student to come in.

I was hooked on him.

That evening, exactly six days after our first date, the phone rang. You're a love-stricken school child and you know that leads to tears and drama, I said to myself during those two seconds that occurred between picking up the phone, taking a deep breath, and uttering a hello that was deepened by an exhale of breath.

"Mike?"

"Who else would be here?" I answered, recognizing his voice.

"It's Alby. And what do you mean who else? A handsome guy like you must have elses crawling out of the woodwork."

"The super sprayed last week."

It must have been obvious to him that I was excited. I again reminded myself that I was planning to be cool, but it was way beyond too late at this point. Yes, I was hooked. We made some small talk about how the week had gone. His ad agency was waiting for a decision on their new business presentation, he told me, and I told him the story of my successful Freud lecture that day.

"I'd love to see you teach, really watch you in action," he said. "You must be a killer."

"Well, I don't know. Usually I hope I can make it through a lecture without a few nod-offs."

"You're modest. I like that in a man."

We talked about getting together for dinner sometime soon. We volleyed some more conversation around. Yeah, we'll do that soon. Yeah, we have to get together. Yeah, right.

"How about Saturday?"

That Saturday evening, after we had spent the day talking and walking and, finally grabbing some dinner, we ended up standing in front the window in my apartment overlooking the rooftops. Alby stood behind me.

"If I were an artist, I'd want to paint this scene," he said.

"Why?"

"I don't know. The buildings just seem to go on forever. It's like being in a forest or a canyon or something. A concrete valley." His voice was soft, almost sad, and I turned around to face him. He stepped back.

"What is it?" I asked.

"I know I've been holding back from you, making you do all the work. I'm not trying to be coy or anything. But I'm not ready for anything else yet.

Visions of other boyfriends, or a reconciliation with his latest ex, flashed through my mind, and I reminded myself that I had to be careful here. "Is your white knight coming back on the scene?"

"No, it's not that. We just need to talk."

"Why do I feel like I'm going to hate this?" I asked. "Can't it wait?"

Alby placed his hands lightly on my shoulders. I smiled and tried to think of something funny to say, but I couldn't.

"Let's get this over with," I said.

"I haven't always been perfect. In fact I never was." He hesitated again, sought my eyes out with his, and then leaned his face toward mine. "Mike, I'm HIV positive."

I felt my breath catch. No thoughts, images, fears, nothing. I was in the middle of an inhale, and it just caught in my throat as I felt my blood rushing toward my feet. I reached up and wrapped my arms around his waist and pulled him closer to me. I held him, tightly, to reassure him, or to reassure myself. This is no big deal, I kept repeating to myself. Nothing is proven. This means nothing. I said this over and over, in my mind, while I held on to him.

"It's not a problem for me," I said finally. "It's not a problem."

"I've been positive for a long time," he said. "Only my sister knows, and now you."

I tightened my grip. "I'm glad you told me.

I told myself that I felt relieved. It was out in the open. So what? He looked perfectly healthy. It seemed like a less insurmountable obstacle than if had told me he had another lover on the scene. And there was that other feeling, the one that I kept trying to push off, that vague sense of another kind of relief, maybe you could call it some kind of perverse feeling of security. He must need me. Yes, I would be there. Love would save the day. Or at least it would save us.

"We can pop in a video if you want," I said. "I've got the silent version of Metropolis. Have you seen it? It's really great."

"Do you want to talk anymore?" he asked.

"About what?"

"There are other things you should know."

Before he could say anything else, I went to my bedroom closet to dig out the video. There was nothing more to say, I knew more than I wanted to. How would talking, or even thinking about it, accomplish anything? Maybe if we ignored it, the whole thing would fade away.

The candles flickered as a breeze came in through the window, throwing a flash of light in his eyes. They were opened wide, searching for something in mine. Reassurance, maybe, or the real truth. And sad. He reached over and took my hand.

"Are you sure you really want to do this?" he asked.

"Absolutely sure, I've never been surer."

"More sure," he corrected me.

"That too."

He squeezed my hand. "We have to be careful. You know that."

I laughed, then took his hand. "I'm ready already."

I was still on that euphoria when I went in to school Monday morning, But by the time I finally had a chance to settle into my office, the euphoria was giving way to a free-floating angst. I sat at my desk and thumbed through the notes for the day's lecture. I turned the pages, reading but not understanding, re-reading and still not able to concentrate. Finally, I got up from my desk, locked my door, turned out the lights, and settled in to let the angst flow over me for awhile.

First, I saw Alby, sitting across from me at dinner. We were looking at each other and talking in hushed, desperate voices. Decisions to be made. Or walking down the street laughing together like any other couple, but clutching each other's hands tightly as if a gale wind might blow through at any moment. Then he was in the hospital; I was holding his hand and trying to smile at him. "Hi buddy," I would say. "How are you, buddy?" Wringing my hands.

I went back through every relationship I had ever been in, the good times, bad times, the gradual growing apart in some, the emotionally wrenching arguments, and discoveries of infidelities in others. I thought about how each relationship had been tenuous, uncertain, in its own way. Even in the best of physical health, no promises that the next week, month, the next day, it would be as good as it was right at that moment. Never a guarantee that there would be a next day.

This is no different, I told myself. A car might hit him tomorrow, and the HIV status won't mean a damned thing. One might hit me too. Either way, life is uncertain, I couldn't promise him anything more than he could promise me.

Was I already in too deep? Was I about to be pulled under by a drowning man? It was early on in the relationship. I had time to get out, somewhat unscathed. I could let him down easy, or just start pulling away. The door was open.

Diiiiiiive......

I wanted him to go away. I wanted to run. I wanted to be with him no matter what. I wanted him to run. I wanted to pretend I was in the middle of a bad video and hit rewind. But I also wanted Alby.

Dammit. It was not supposed to be this way.

My eyes wandered toward a poster that hung over my desk of a bright turquoise ocean and a blue sky, a white boat with red sails. It was a joke on myself, in a way. I've been terrified of water since I was a third grader and my mother sent me to swimming lessons. The instructor, a high school jock, spent most of each class hitting on the female lifeguard. She was the one who busted me, told him I was cheating by wading across the pool and not kicking. He jumped in -- the only time he ever got wet -- and held my head underwater until I took big swallows of chlorine. He gave me a few seconds to swallow and gasp, then held me under again.

Aversion therapy, the behaviorists would call this poster. Torture yourself with something you're afraid of and maybe it will go away.

Alby loved water and had taken a few sailboat lessons in college. As I stared at the sailboat, I imagined the two of us standing with the boat, in shallow water, and slowly pushing it away from the shore. First the water was at my ankles, then my knees, then my waist.

"Is there enough breeze yet?" I asked Alby.

"Not yet," he said.

We went out further. The water was higher than my waist, then up to my armpits. I could feel myself beginning to hyperventilate.

"Jump in," Alby said. "Let's go."

"I can't," I replied. "I'm scared of the water."

"Then I'll have to go alone. Give me a push."

"No. Not yet. Give me some time."

I continued to stare at the poster as the hours passed. In the late afternoon, as the sun began to fade, the ocean started to look dark, like a storm was moving in. The sailboat faded, became a shadow.

I slipped away into that world of half-awake-half-asleep that, if you play it right, can keep you from away from reality but also away from dreaming. But then I must have dreamed about something, because I jerked into a sitting position, feeling as if I was suffocating. I gasped for air.

When I caught my breath, I found myself in the dark.

The building was silent, probably locked from outside. I could leave now and not have to worry about being accosted in the hallway. I stood up. There was just enough light coming through the frosted glass window to allow me to fumble around for my backpack and keys. I felt for the door handle, letting my hand slide past the wall switch for the ceiling light.

It was really darkness that I wanted. Just enough light to see my way out without having to look at any of the details.
```

---

## IC-0380: Hydrophobia

- Title: Hydrophobia
- Author (byline): Brian Costings
- Work: Fast Horse Plays – Round Two (Pg 37-40)
- Publisher: Fast Horse Drama
- Publication date as stated: June 2012
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR
- Teaser before the introduction: No
- Spoken words (computed): 1308
- Already set (do not supply): none

### Source block (context only)

```text
Author: Brian Costings
Book: Fast Horse Plays – Round Two (Pg 37-40)
ISBN: 978-0615668734
Publisher: Fast Horse Drama
Date (Month/Year): June 2012
```

### Introduction (context only: never use it for content warnings)

```text
People often call youth homelessness an “invisible issue.” Many don’t seem homeless, traveling from place-to-place, and couch surfing with friends. According to True Colors United (2017), however, it is believed that 1 in 30 adolescent minors ages 13 to 17 (1) are homeless and struggling to survive -- 700,000 young people. Why?

Teens report severe family conflict as the primary reason for their homelessness. For some, they are fleeing abusive homes; for others (1 in 4; Leslie University (2)), their parents have kicked them out, unable to deal with their sexual identity. Regardless of the reason. . . homeless teens must navigate of world of drugs, trauma and sexual assault alone; and many suffer from depression and PTSD.

Imagine being 15 years old, with no home, no family. What would you do to survive?

Hydrophobia by Brian Costings
```

### Performance text (classify this)

```text
The unnamed narrator is a young man of 15.

NARRATOR: My life is, like, perfect. Like, totally perfect. Like, I don't think you totally understand how totally perfect my life, like, really is. It's like, everybody else's life ... not even close to perfect, and my life ... like, whoa. Perfect. Complete perfection. Like the universe opened up and created this whole new consciousness or something ... just so everything could be this totally perfect. You catch my drift, right? Riding my wave, man?

I found out pretty quick that it doesn't really matter whether or not you can actually surf. I mean, you gotta have a totally radical board and wear the clothes, have the hair, and, like, the totally most important thing, you gotta have the talk. When you open your mouth you gotta sound like a surfer. If you sound like a surfer, it doesn't really matter if you've never angled, or dropped or curved or caught a wave, like, ever, in your entire life. Everybody likes surfers. People think surfers are like totally awesome.

I'm a surfer ... but I don't surf. Dude...it looks like I totally lost you or something. Okay, so I do absolutely everything that surfer dudes do except for the part about getting up on a board and going out into the water. I'm not down with the water. At all. I think it's like one of those weird childhood scarring things or something. You know, like the inner me is totally freaked out by the H20. My Pops is like, kinda a dweeb, if you catch my drift. When I was like, five, he decided he was gonna teach me how to swim, ya know? But I wasn't down with it. I didn't wanna get in the water. So, he umm, like picks me, like over his shoulder, ya know, and just tosses me in the pool in the backyard. And I like, remember hitting the water, and like, it was gnarly cold, ya know? And then I think I was just kinda sinking. And I could hear my Pops and he's like yelling, "What the hell's the matter with you? Move your arms and legs." And, then, so like, the next thing I remember, he's not trying to teach me how to swim anymore, and I'm not even in the pool. I'm on the cement and my Mom, she's screaming about me being blue and she's just yelling at my Dad. And I put my hands over my ears, cuz I hated listening to them fighting with each other.

So, then, my life got like really boring for like a buncha years after that. I kinda just spaced while I was at school and then in the afternoons, I'd spend most of my time down at the beach, watching the guys out on their boards. Watching them do totally awesome stuff, like head dips and hot-dogging and kamikazes ... and knowing, that one day, I'd be out there too, doing that stuff. So, I met this one dude down at the beach, dude my age who was kinda freaked out by the water too. So we kinda had like a cool connection or whatever, ya know? And so, we started to sorta hang out, like we'd check out the beach bunnies together or do homework... well, pretend like we were doing homework. Books and school were never my strong point, ya know?

So, umm, anyway, like sometimes, in my room, we would umm- okay, this is like totally dorky, but uh...we would like practice kissing like, for when we got our first chick, ya know? I mean, practice makes perfect, right? So, umm, we like practiced a lot. And one day, we were practicing and umm, my Pops, he like opens the door, right? And umm, he totally flips out. Like big time. And umm, he's like screamin' and punchin' me and all this stuff, right? And then, suddenly, I don't have like a ... what do they call it? A permanent residence anymore. Seriously. Heavy, huh, dude? Yeah, it's like Poof. No more. Nada. I mean, I always knew my Pops was like gremlin-central, but, like ... whoa, right?

So, umm, this kid. His Mom, she's like the awesome-est, ya know? Totally radical. And after all the drama goes down with my Pops, she's like, "You can totally come and stay with us for however long you need to." And like, I think she like, knew that he and I practiced sometimes and was like, no sweat. Boys will be boys, all that stuff. So, everything is like really cool with him and his Mom. But, umm, I guess, she thought that like a month was all I needed to stay, because, like, after that it was like, sayoonara-try-tomorrow, and I was like ... whoa ... again ... this is totally un-awesome. Like as un-awesome as you can get, right? So I was like, if I was riding a wave at like, Pipeline, I would have to stay focused, ya know? That's totally what I gotta do ... stay focused. I can do this.

So, umm, I like end up spending some time down-town, ya know? Just like a block up that way from where we are right now. And umm, turns out there's like lots of totally radical guys down there who totally kinda taught me the ropes. I kinda started with like trying to recycle cans or umm, return the grocery carts back to Ralph's- to, ya know, get the quarters back? Most of you never return your grocery carts. It's kinda funny. But anyhoo, I find out it takes a lotta work to do that kinda stuff and umm, ya don't get a lotta quarters. And it takes a lotta quarters to eat. So, I knew I wasn't on the fast track.

So, a couple of the guys, they, umm, teaching me about standing. Standing. At night. Ya know, on the Boulevard. There's a coupla blocks you gotta go to. And, the first couple of nights, I was just like in a daze from watching the head-lights, ya know? But then, I got in my first car, right? And, umm, ya learn really fast. Ya do. It's like, whatever the dudes ask for, you just gotta say yes a lot more than ya say no ... ya know? And I mean, yeah, sometimes it's like super-sketch ... like, there's was this guy with like nylon cord and this other old dude with......but umm, most of the time they're like super cool and umm, you get the twenty or the fifty if you're lucky, and you're like, whoa ...COWABUNGA, dude. I mean, it's just practice. And hey, eating is also totally awesome. So, like I feel like totally wise sometimes, like, wow ... I'm so close to being totally grown-up.

So, yeah, my life is like pretty perfect now. I got a super close group of dudes and the Benjamin's and I get to watch the waves like all day, every day. I just gotta conquer the fear, so I can be out there, ya know? So, sometimes, like at night, late ... I walk all the way down to the end of the pier. And I think, ya know, if I just kept walking, like I could totally learn to swim and I wouldn't be afraid anymore and I could just swim out in the night with the big fat moon over me on and on and on and like, I'd just be part of the water, ya know? Like ... whoa. Trippy. Like, I could do that tonight. PSYCH! Nah, it's a Friday. Good money, ya know? It's sunset, so... umm... Unless you got a twenty to keep me? I didn't think so, dude. No worries. All good in the hood. I gotta dash. Surf's up.
```

---

## IC-0381: I Am My Own Wife

- Title: I Am My Own Wife
- Author (byline): Doug Wright
- Work: Not specified
- Publisher: Faber and Faber, Inc.
- Publication date as stated: Feb 2004
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARLOTTE, FATHER, TANTE LUISE, SS OFFICER, SS COMMANDER, NEO-NAZI 1, NEO-NAZI 2
- Teaser before the introduction: Yes
- Spoken words (computed): 1359
- Already set (do not supply): none

### Source block (context only)

```text
Author: Doug Wright
ISBN: 978-0571211746
Publisher: Faber and Faber, Inc.
Date (Month/Year): Feb 2004
```

### Introduction (context only: never use it for content warnings)

```text
Lothar Berfelde, better known as Charlotte von Mahlsdorf, was a transvestite and celebrated antiques dealer who successfully navigated the two most oppressive regimes of the past century-the Nazis and the Communists. While openly gay and defiantly in drag, von Mahlsdorf was both hailed as a cultural hero and accused of colluding with the Stasi secret police of East Berlin.

This is her story . . . based on actual interview

I am My Own Wife by Doug Wright
```

### Performance text (classify this)

```text
NOTE: Actor should speak in broken English with a German accent. She is, in fact, a man, roughly sixty-five years old.

CHARLOTTE: (Pg 15) Come in, please. There is room for everyone, yes? (gestures expansively to her belongings) (Pg 14) Wilkommen in meinem Grunderzeit Museum. Welcome to my Grunderzeit Museum. People always come to see my collection. Everything is from the period in Germany between 1890 and 1900. “The Gay Nineties.” (Gestures to an ornate door) (Pg 15) This old door is not original, nein. I saved it from a house on Prenzlauer Street. Before the Russians blew up the houses, I took such things. . . a cupboard . . . an old sideboard . . . this clock. (she cradles it in her arms like a baby) (Pg 16) I had a feeling for such things. And so I saved [them]. (Pg 18) When families died, I became this furniture (gestures to the collection) When the Jews were deported in the Second World War, I became it. When citizens were burned out of their homes by the Communists, I became it.

CHARLOTTE: (Pg 14) Some people, they come to see me. Ich bin Transvestit. (Pg 14) But soon they look at the furniture (taking inventory of her collection) Lamps and vases, records, matchboxes, pictures and of course [my] gramophone.

(She picks it up, blows the dust off of it and prepares to play a record while she speaks) (Pg 46) Even when I was a little child, no one wanted phonographs. They all wanted radios. But what did I want with a radio? To hear Hitler babble? No, thank you! (She pauses with a record in her hands) (Pg 17) At one time I had many such records – Mendelssohn and Offenbach. But during the time of Hilter it was very dangerous to possess music from Jewish composers. And so I thought, I must save these records. And so I glued false labels onto the records, for safety. (She places the record and the gramophone) And when the war was over, I took a sponge and with water I took the labels back off. (As the music plays, she hums and sways with the music) (Pg 11) In the Second World War, when the airplanes flew over Mahlsdorf, and the bombs were coming down, I played British and American records. I thought, (she chuckles) if they hear me, they will know I’m their friend. (beat) (Pg 46) These machines gave me so much pleasure in my childhood. If I hadn’t had them, I’m not sure I would’ve survived. Things wer so ghastly with my father – everything my mother and I went through. (Pg 29) . . . My father was a Nazi. And he was brutal. (Beat) (Pg 31-32) One evening I asked him, “aren’t you ashamed of the way you’ve treated my mother? And he said:

FATHER: I’ll shoot you down like a dog and then I’ll shoot your mother and your sister and your brother.

CHARLOTTE: I knew that my father would do this. He locked me in bedroom, but even then I had in my pocket . . . keys. (She opens the door and creeps out) My father was lying on the sofa, his gun on the chair next to him. And in that moment, the clock (she strides to a table and picks a clock up angrily and holds it aloft) a Westminster clock was chiming. My father’s hand was reaching for his weapon. (She brings the clock down on her father’s head, speaking with sudden ferocity) Eins! Zwei! Drei! Vier! Funf! (A pause; she dissociates for a moment, becoming oddly contemplative) Hmm. Yes. (she smiles and puts the clock back on the table) We were finally free from the monster. (beat)

It was luck for us that in 1943 in Berlin, the government decreed the evacuation of mothers with children because of the air raids. And so my mother took [me] to East Prussia, to the house of my aunt. (Pg 21-22) Since she was fifteen years old she never wore ladies’ cloths. No. Only boots and jodhpurs. The clothes of a land inspector and not a fine lady. (She whispers) I found in her closet . . . Girl’s cloths And . . . I . . . put . . . them. . . on.

(She steps before an imaginary mirror, delighted by her image in the glass. She twirls, raising her skirt when she notices her aunt) My aunt looked at us in the mirror ….

TANTE LUISE: [Well] nature has dared to play a joke on us. You should’ve been born a girl, and I should’ve been a man!

CHARLOTTE: In each person, there is a delicate balance of male and female. Just as we can’t find two matching leaves from the same tree, it is scientifically impossible to find two human beings whose male and female characteristics match in kind and number.

(Pg 25) The last days of the war were the most dangerous time for me, because I refused to carry a weapon or to wear a uniform. Instead, I had my hair long and blond and my mother’s coat, and the shoes of a girl. And so I was – in Germany we say “Freiwild.” Like the Jews, we were wild game.

(Long beat as Charlotte remembers)

(Pg 26) I could hear the bombs. (looks skyward) There was an air-raid shelter and so I went inside. (Pg 26-27) Suddenly the door opened and in came four SS officers. Die Kettenhunde *(translates to “the chain dogs”)

SS OFFICER: All deserters shall be shot.

CHARLOTTE: I looked down – I didn’t want to see them shoot. I thought, I’ll wait until I feel it. But when I looked to the ground I saw the boots of a commander.

SS COMMANDER: Are you a boy or a girl?

CHARLOTTE: And I thought, if they shoot me, what’s the difference between a boy and a girl, because dead is dead! (She become a child and answers) I am a boy.

SS COMMANDER: How old are you?

CHARLOTTE: Sixteen . . . (in her adult voice) And he turned around to face the execution squad commander.

SS COMMANDER: (With some measure of self-contempt) We are not so far gone that we have to shoot schoolchildren.

CHARLOTTE: And this was my salvation. (Beat)

TRANSITION But salvation was short lived for Charlotte von Mahlsdorf. The final weeks of April 1945 saw Soviet troops advance on Berlin, bringing World War II in Europe to an end. And the Soviet occupation of East Berlin brough a host of new challenges. Germany had been too busy fighting a war to focus too much on the gay community, unless you were a Jew, of course; but Russia was determined to stamp out all homosexuals.

CHARLOTTE: (Pg 34) It was true! The Allies were coming to Berlin. And I saw on the street the large Russian tanks. (Pg 38) And then came the wall. For us here in Eastern Berlin it was finished, gay life. No place to meet . . . bars closed . . . advertisements in the newspaper, cancelled. We were not supposed to exist. (Beat) So I thought to give homosexual women and men community in this house. (Motions for the audience to follow her) (Pg 36) Today I show you das Geheimnis – the secret – of meinem Grunderzeit Museum. (She unlocks a door, enters and gestures expansively) (Pg 37)

Welcome to die Mulack-Ritze. And old tavern from the yesterday. It was a restaurant for gays and lesbians. (lovingly wipes down a table) This table is over one hundred years old. At this very table haben Bertolt Brecht and Marlene Dietrich (mischievously) [In East Berlin] Tanzen ist verboten. Dancing is forbidden. At least according to the police. (Pg 69-70) We played Donna Summer and everyone was dancing and singing under paper lanterns. (She sways to remembered music, but the memory turns ugly) And I heard a window smash in my basement. A rock. The Brown plague had come back again. Kristallnacht once more. The neo-Nazis knew I was a homosexual. They came over the wall – thirty of them – with flare guns and gas pistols. The gays were all cowards, running inside, but the lesbians stayed to fight. (Long beat) And my friend Sylvia, she was in the cellar, trying to shut the door, and she got a gas pistol in the eye. A young girl from Frankfurt almost died. They cracked open her cranium with an iron stick. And I was coming from the cellar with an old pickax, and a skinhead met me on the stair. He had a swastika tattooed on his arm, yes?

NEO-NAZI 1: Hitler forgot to shove you in an oven!

CHARLOTTE: And I swung and hit the blade in the old banister, splitting it open like a sapling, ja? And from behind me another voice.

NEO-NAZI 2: We should drown you in the Ostsee!

CHARLOTTE: And then die Polizei came. And the young men scattered. Like die Asche, after a fire. No one was arrested. No one went to jail.

(Pg 43-44) (Charlotte’s demeanor changes; she speaks cautiously) One day [the Stasi] came and he wanted me to write exactly what he said: (She picks up a paper from a side table) I, Lothar Berfelde, commit myself willingly and freely to working together with the Ministry for State Security. I will report all information which may have the character of an action inimical to the state. I will be known by the code name Park. (quietly) I signed it. . . and I said to myself, (defiantly “I’ll still do whatever I want.” Meine Tante Luise always said, “Be as smart as the snakes; it’s in the Bible . . . never forget that you are living in the lion’s den. Sometimes, you must howl with the wolves.” (Pg 69) [Because of me] Home[s] [were] broken into and the Stasi impounded everything. Just like the Nazis during the deportation of Jewish people, they took all things. (She returns to her furniture for comfort) (Pg 77) Nicks and cuts, Stains. Cracks. People sat on it, slept on it, wrote letters on it, ate from it. People tried to burn it. In Nazi times, In Stasi times. And still, it is standing. It is a record, yes? Of living . . . . Of lives. (Pg 14) Wilkommen in meinem Grunderzeit Museum. Welcome to my Grunderzeit Museum
```

---

## IC-0382: I am not Batman

- Title: I am not Batman
- Author (byline): Marco Ramirez
- Work: Humana Festival 2007: The Complete Plays, Pg 208-214
- Publisher: Playscripts, Inc.
- Publication date as stated: April 2008
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BOY
- Teaser before the introduction: Yes
- Spoken words (computed): 1491
- Already set (do not supply): none

### Source block (context only)

```text
Author: Marco Ramirez
Book: Humana Festival 2007: The Complete Plays, Pg 208-214
ISBN: 978-0970904638
Publisher: Playscripts, Inc.
Date (Month/Year): April 2008
```

### Introduction (context only: never use it for content warnings)

```text
Alone in his bedroom, a boy imagines wild adventures as Batman, New York City’s avenging angel. As Batman, he leaps into action to foil thugs and save Janitorman! Our hero’s fantasies are so much better than the reality of his own life. Aren’t they always? But also, as always, reality trickles into his fantasy world whether he wants it to or not.

I am not Batman by Marco Ramirez.
```

### Performance text (classify this)

```text
Lights up on a BOY, maybe 7, maybe 27 – He looks out directly before him, breathing nervously – he is excited, but never gets ahead of himself.

BOY: (Pg 208-214) It’s the middle of the night and the sky is glowing like mad radioactive red. And if you squint you could maybe see the moon through a thick layer of cigarette smoke and airplane exhaust that covers the whole city, like a mosquito net that won’t let the angels in.

And if you look up high enough you could see me. Standing on the edge of a eighty-seven story building – And up there, a place for gargoyles and broken clock towers that have stayed still and dead for maybe like a hundred years – up there is me. And I’m freakin’ Batman.

BOY: I gots Bat-mobiles and Bat-a-rangs and freakin’ Bat-caves like for real, and all it takes is a broom closet or a back room or a fire escape, and Danny’s hand-me-down jeans are gone.

And my navy blue polo shirt? (speaking quickly) The-one-that-looks-kinda-good-on-me-but-has-that-hole-on-it-near-the-butt-from-when-it-got-snagged-on-the-chain-link-fence-behind-Arturo’s-but-it-isn’t-even-a-big-deal-’cause-I-tuck-that-part-in-and-it’s-like-all-good? – that blue polo shirt? It’s gone too. And I get like, like transformation-al.

And nobody pulls out a belt and whips Batman for talking back – or for not talking back, -- and nobody calls Batman simple – or stupid – or skinny – And nobody fires Batman’s brother from the Eastern Taxi Company ‘cause they was making cutbacks, neither, ‘cause they got nothing but respect, and not like afraid-respect. Just like respect-respect. ‘Cause nobody’s afraid of you. ‘Cause Batman doesn’t mean nobody no harm. Ever.

‘Cause all Batman really wants to do is save people and maybe pay Abuela’s bills one day and die happy and maybe get like made famous. For real . . . And kill the Joker.

Tonight, like most nights, I’m all alone. And I’m watching . . . and I’m waiting . . . Like an eagle. Or like a – no, yea, like an eagle.

And my cape is flappin’ in the wind (‘cause it’s freakin’ long), and my pointy ears are on, and that mask that covers like half my face is on too, and I got like bulletproof stuff all in my chest so no one could hurt me and nobody – nobody – is gonna come between Batman, and Justice.

From where I am I could hear everything.

Somewhere in the city there’s a old lady picking Styrofoam leftovers up outta a trash can and she’s putting a piece of sesame chicken someone spit out into her own mouth.

And somewhere there’s a doctor with a whack haircut in a black lab coat trying to find a cure for the diseases that are gonna make us all extinct for real one day.

And somewhere there’s a man, a man in a janitor’s uniform, stumbling home drunk and dizzy after spending half his paycheck on forty-ounce bottles of twist-off beer and the other half on a four hour visit to some lady’s house on a street where the lights have all been shot out by people who’d rather do what they do, in this city, in the dark.

And half a block away from JanitorMan there’s a group of good-for-nothings who don’t know no better waiting to beat JanitorMan with rusted bicycle chains and imitation Louisville Sluggers, and if they don’t find a cent on him – which they won’t – they’ll just pound at him till the muscles in their arms start burning, till there’s no more teeth to crack out.

But they don’t count on me (The BOY becomes proud, stands up straight)

They don’t count on no dark knight (with a stomach full of grocery store brand macaroni-and-cheese and cut up Vienna sausages), ‘Cause they’d rather believe I don’t exist.

And from eighty-seven stories up I could hear one of the good-for-nothings say “Gimmethecash” real fast (like that) just “Gimmethecash” and I see JanitorMan mumble something in drunk language and turn pale and from eighty-seven stories up I could hear his stomach trying to hurl its way out of his Dickies.

So I swoop down like mad fast and I’m like darkness, I’m like SWOOSH – and I throw a Bat-arang at the one naked lightbulb – and they’re all like “whoa-who-just-turned-out-the-lights?” (silence. The Boy breathes, re-enacting their fear)

-- “What’s that over there?” -- --“What?” – --“Gimme watchou got old man” – --“Did anybody hear that?!” – --“Hear what? There ain’t. No. Bat.” But then – (the BOY suddenly springs into action) One out of three good-for-nothings gets it to the head! And number Two swings blindly into the dark cape before him but before his fist hits anything I grab a trash can lid and – right in the gut, and number One comes back with a jump-kick but I know judo-karate too so I’m like – (CRASH, happy from the response, he adds this part) – Twice – (Crash) – but before I can do any more damage suddenly we all hear a CLIC- CLIC – And suddenly everything gets quiet.

And the one good-for nothing left standing grips a handgun and aims straight up, like he’s holding Jesus hostage, like he’s threatening maybe to blow a hole in the moon.

And the good-for-nothing who got it to the head who tried to jump-kick me and the other good-for-nothing who got it in the gut is both scrambling back away from the dark figure before him.

And the drunk man the JanitorMan is huddled in a corner, praying to Saint Anthony ‘cause that’s the only one he could remember.

And there’s me – eyes glowing white, cape blowing softly in the wind. Bulletproof chest heaving. My heart beating right through it in a Morse code for “ **** with me, just once, come on, just try.”

And the one good-for-nothing left standing, the one with the handgun, he laughs, he lowers his arm and he points it at me and gives the moon a break and he aims it right between my pointy ears, like goalposts and he’s special teams. (The BOY stands, frozen, afraid)

And JanitorMan is still calling Saint Anthony but he ain’t pickin’ up (silence) And for a second it seems like . . . maybe I’m gonna lose. (The BOY takes a breath. Sudden courage) . . . Naw.

(The BOY mimes the fight) SHOO – SHOO! FUACATA! –

--“Don’t kill me mannnn!!” -- SNAP! –

-- Wrist -- CRACK! –

-- Neck --SLASH! --

-- Skin – meets – acid – -- “AHH!!!!!” –

And he’s on the floor. And I’m standing over him. And I got the gun in MY hands now. And I hate guns, I hate holding ‘em cause I’m Batman, and -- (whispers an aside) Batman don’t like guns ‘cause his parents got iced by guns a long time ago – (aloud) but for just a second, my eyes glow white and I hold this thing, for I could speak to the good-for-nothing in a language he maybe understands, (De aims the gun up at the sky) . . . CLIC – CLIC . . .

And the good-for-nothings become good-for-disappearing into whatever toxic-waste-chemical-sludge they crawled out of. (a pause)

And it’s just me and JanitorMan.

I pick him up and I wipe sweat and cheap perfume off his forehead. He begs me not to hurt him and I grab him tight by his JanitorMan shirt collar and I pull him to my face. He’s taller than me, but the cape helps, so he listens when I look him straight in the eyes and I say two words to him: “Go home.” And he does, checking behind his shoulder every ten feet.

And I SWOOSH from building to building on his way there, ‘cause I know where he lives. I watch his hands tremble as he pulls out his keychain and opens the door to his building. And I’m back in bed before he even walks in through the front door.

I hear him turn on the faucet and pour himself a glass of warm tap water. He puts the glass back in the sink. And I hear his footsteps . . . they get slower as they get to my room. And he creaks my door open like mad slow. (Silence) And he takes a step in, which he never does. And he’s staring off into nowhere, his face the color of sidewalks in summer, and I act like I’m just waking up, and I say, “What’s up, Pop?”

And JanitorMan says nothing to me. But I see, in the dark, I see his arms go limp and his head turns back, like towards me, and he lifts it for I could see his face, for I could see his eyes. And his cheeks is dripping but not with sweat. And he just stands there, breathing, like he remembers my eyes glowing white. Like he remembers my bulletproof chest. Like he remembers he’s my pop. (Silence)

And for a long time I don’t say nothing. (SILENCE) And he turns around, hand on the doorknob, and he ain’t looking my way but I hear him mumble two words to me. (a pause) “I’m sorry.” (a pause, the BOY is suddenly strong again) And I lean over and open my window just a crack.

. . . If you look up high enough you could see me . . . And from where I am? . . . I could hear everything.
```

---

## IC-0383: I Didn’t Know You Could Cook

- Title: I Didn’t Know You Could Cook
- Author (byline): Rich Orloff
- Work: Best American Short Plays 1996-1997 (ed Glenn Young)
- Publisher: Applause Theatre Books
- Publication date as stated: October 1997
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: JEROME, MARK, SETTING
- Teaser before the introduction: Yes
- Spoken words (computed): 2058
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rich Orloff
Book: Best American Short Plays 1996-1997 (ed Glenn Young)
ISBN: 978-1557833174
Publisher: Applause Theatre Books
Date (Month/Year): October 1997
```

### Introduction (context only: never use it for content warnings)

```text
When conservative older brother Mark visits his paraplegic brother Jerome's house for dinner, he is shocked by two pieces of information -- his little brother is a great cook, and he is gay. When Mark demands Jerome choose between being disabled and being gay, the ensuing conversation reveals how much the brothers have kept hidden from each other over the years. Will Jerome be able to convince his brother to accept him for who he is? I Didn’t Know You Could Cook by Rich Orloff
```

### Performance text (classify this)

```text
JEROME: mid-20's, paraplegic, uses a wheelchair

MARK: near 30, his older brother

SETTING: The kitchen of a modest urban apartment. As the play begins, JEROME and MARK are at the kitchen table finishing dinner. JEROME has gone to some effort to make the meal setting look classy.

MARK: Anyway, so he pulls up to the stoplight, and he begins revving up his little Corvette engine, and I think, give me a break:

JEROME: Uh-huh.

MARK: I didn't get my Porsche to be macho or anything. I just like how it feels.

JEROME: Uh-huh.

MARK: But he keeps revving his engine, rhhm, rhhm, rhhmmmm, so, so right before the light changes, I roll down my window

JEROME: Yeah.

MARK: And I say, "I think you've done a wonderful job of compensating for a small penis."

JEROME: You didn't.

MARK: Light changed; I took off; left him in the dust.

JEROME: Wow, it's so cool they gave you a Porsche as a bonus.

MARK: Hey, if you ever want to get into sales. . .

JEROME: I think I'll stick with teaching.

MARK: Well, if you ever want me to help. After all, what's a brother for?

JEROME: Thanks. Not that I could drive one, anyway.

MARK: I'm sure they could adjust it.

JEROME: I'll stick with my Ford. We've developed a very intimate and trusting relationship.

MARK: You know, in a just world, they'd give teachers cars as bonuses.

JEROME: That'll be the day.

MARK: [Finishing eating.] This was delicious, Jerome. Absolutely delicious.

JEROME: I'm glad you liked it.

MARK: I'm really impressed. I didn't know you could cook.

JEROME: Millions of people can cook, Mark. Maybe billions. Would you like some dessert? It's chocolate mousse pie. Made it from scratch.

MARK: Sorry. No room.

JEROME: You don't need room for chocolate mousse pie. It just fills the crevices around the food you've already eaten.

MARK: Besides, I, I probably should be heading back to the hotel.

JEROME: It's early.

MARK: I know, but I have another meeting first thing in the

JEROME: You know - you know how long it's been since we've spent any real time together?

MARK: Six months?

JEROME: Five years.

MARK: Well, we've talked the last hour, haven't we? [PAUSE] Hey, Mom sent me that article about you in the paper.

JEROME: About the disabled schoolteacher all the third graders adore?

MARK: It was a good article.

JEROME: It was your generic "Let's admire the handicapped" piece. They just filled in the blanks with my name.

MARK: Nobody writes about me.

JEROME: Look, it was a fine article; I, I just don't like being written up because I can do what people assume I can't do. If they were honest, the piece would have been titled, "Local Crip Transcends Expectations."

MARK: Well, I liked the piece. And even if this isn't... correct, I'm really impressed by how well you've learned to manage on your own.

JEROME: And I'm impressed by how well you've learned to manage on your own, too, Mark.

MARK: All I mean is, well, I never thought you'd move out and live on your own. I mean, I knew you could. I knew you could do anything you put your mind to. I'm sorry if that bugs you, but it's true.

JEROME: I haven't done anything special.

MARK: I'm not sure I could have done what you've done.

JEROME: You just haven't been tested.

MARK: Still, to live alone when you're, well, you know-I think it's quite an accomplishment.

JEROME: Well, it's not like I'm completely alone.

MARK: Why? Is someone hiding in the bedroom or something?

JEROME: No, I mean friends. You know, friends.

MARK: I know, friends. The people you put in your Rolodex who aren't business connections.

JEROME: I also, um, well, I, there's, there's also one special friend.

MARK: No, really?

JEROME: Really.

MARK: Who?

JEROME: Oh, just. . . just someone special.

MARK: What's her name?

JEROME: Louie.

MARK: Well, if there can be an actress named Glenn Close, I guess there can be a woman named Louie.

JEROME: Louie's a man.

MARK: Oh, so he's just a friend.

JEROME: We're more than friends.

MARK: He's a good friend.

JEROME: We're more than good friends. We're lovers. Mark, I'm gay.

MARK: You can't be gay.

JEROME: Why not?

MARK: Because our father isn't henpecked and our mother isn't castrating.

JEROME: I'm still gay.

MARK: Are you sure you're not just doing this to be trendy?

JEROME: Mark, I'm a homosexual.

MARK: Well, I'm stunned. I'm really stunned. I never even knew you were sexual.

JEROME: Of course, I'm sexual.

MARK: Well, I thought, since the accident. . .

JEROME: Only my legs went limp; I'm one of the lucky ones.

MARK: Well. . . what do you know.

JEROME: To be honest, after the accident, I wasn't sure what I'd be able to do. At the rehab center, they didn't deal with our sexuality at all. At all. Then about six months later, I - I was watching this Mel Gibson movie, and he started getting real sweaty, and inside I started getting real excited, and outside I got real excited, too.

MARK: You're just doing this to be different, aren't you?

JEROME: Stop it! Look, I, I. . . I know you have trouble accepting things sometimes.

MARK: Like what?

JEROME: Like after the accident, when you visited from college and you offered me a hundred bucks if I took five steps.

MARK: I thought you needed encouragement.

JEROME: My spinal cord had been severed, Mark.

MARK: I know.

JEROME: It was physically impossible.

MARK: Look, I just thought you needed a little push to get better.

JEROME: I was getting better.

MARK: Everyone always coddled you.

JEROME: Dad never coddled me.

MARK: Dad never knew either of us existed. [This stops the conversation for a moment.]

JEROME: You're right.

MARK: Look, about this, this deciding to be gay thing, I . . . well, I just can't say I approve.

JEROME: Well then, I guess I'll just have to stop. Do you want to pretend I never said it?

MARK: It's not healthy.

JEROME: Mark

MARK: So I'm giving you a choice.

JEROME: What?!

MARK: You can be gay or disabled, but not both.

JEROME: But I am both!

MARK: Why can't you be satisfied just being disabled?

JEROME: I don't know. Maybe I'm just selfish.

MARK: Have you considered seeing a shrink about this?

JEROME: I've seen a shrink.

MARK: And what did he say?

JEROME: He said I should accept myself for who I am and stop worrying about whether or not I can please my older brother.

MARK: That sounds like something a shrink would say. Does the school know about this?

JEROME: I'm sure some people suspect, but no.

MARK: 'Cause I'm sure a lot of parents would get pretty upset.

JEROME: I know. Some of them are already nervous about me. I think they're afraid that with me as a role model, some of their kids will want to grow up to be disabled.

MARK: Maybe you think women won't be attracted to you because. . . you know.

JEROME: Mark, I've been with women. I wasn't attracted to them the way I am with men.

MARK: What do you mean, "been with?"

JEROME: I mean everything you think I could mean.

MARK: Were these women. . . you know?

JEROME: Disabled?

MARK: Yeah.

JEROME: Some were, and some weren't.

MARK: So then women find you attractive.

JEROME: Well, not an uncontrollable number. . .

MARK: And you've had sex with them.

JEROME: Some of them.

MARK: Well, that proves it. You're attracted to women.

JEROME: No! I, uh, the women were, oh, I don't know. I guess, I guess they were an experiment. I mean, I thought I might be gay even before the accident; actually, I was pretty sure of it. Still, I kept thinking, "Maybe if I meet the right woman..."

MARK: Why can't you just be disabled?!

JEROME: Look, damn it, I'm disabled and I'm gay, and that's the way it is, whether you like it or not or I like it or not or anybody in the world likes it or not. I didn't ask to be either. I always figured I'd get married someday and I'd walk down the aisle, and surprise, I'm not going to do either. I know I should be proud that I'm gay, and accepting that I'm disabled, and I suppose I am, but damn it, I've sure had to give up a lot of fantasies, a whole truckload of fantasies.

MARK: Look, if you've decided to be gay, that's your decision.

JEROME: Oh, yes. That's what it was, a decision. One morning I woke up and thought, "I wonder what I'll do today. See a movie? Go shopping? Turn homo? That sounds interesting."

MARK: Look, I'm sorry, I know this must be hard for you, but I just can't approve.

JEROME: I'm not asking you to approve; I'm asking you to, to accept.

MARK: Well, I'm not sure I can.

JEROME: Why, because I can't be who you want me to be?

MARK: What?

JEROME: It's like when you offered me that money to walk again. I think about that a lot. Was that for me or for you?

MARK: What do you mean?

JEROME: If I could walk again, then you wouldn't have to face the fact that I couldn't.

MARK: Look, Jerome, it's, you know, I'm sure you don't approve of everything I do

JEROME: I don't want your approval, Mark.

MARK: Then why did you tell me?!

JEROME: Because you're, you're my brotl1er.

MARK: I know, but

JEROME: Because you let me tag along with you when you went to get ice cream. Because you explained long division to me better than my teacher. Because you taught me how to play catch.

MARK: You threw like a girl.

JEROME: I don't think it was a sign.

MARK: You know, you could've given me a little hint along the way or something.

JEROME: Like what?

MARK: I don't know. You could've had copies of Playgirl lying around. . . It's just, it's a scary time.

JEROME: I'm careful. We're careful.

MARK: Still

JEROME: You sure you wouldn't like one piece of - [One of JEROME’s legs starts to spasm. It’s not significant, but it’s noticeable, and it lasts ten to fifteen seconds.] Uhp, there goes Old Faithful.

MARK: I thought you were taking medication

JEROME: I stopped years ago. I'm used to them; they don't bother me.

MARK: [Overlapping a bit.] Do you ever get spasms at school?

JEROME: Oh, sure. Not often.

MARK: How did the kids react?

JEROME: Oh, the first time, they were freaked out. Then I told them that whoever got the highest mark on the division quiz would get to ride me next time it happened. They got used to it after that.

MARK: You have a lot of guts, Jerome.

JEROME: I just do what I have to do, that's all.

MARK: You don't have any more surprises for me tonight, do you? You haven't joined a religious cult or anything. You're not a gay disabled Moonie, are you?

JEROME: And if I were?!

MARK: I don't know!

JEROME: Look, I, I . . . I know this must be hard on you. . .

MARK: Well, you know, it's like one moment you think the universe is one way; the next moment, it's another way.

JEROME: No, the universe is always the same. The only thing that changes is what you know about it.

MARK: This Louie guy, is he, you know. . .

JEROME: An Episcopalian?

MARK: No, is he, you know. . .

JEROME: Handicapped? Crippled? Physically challenged? Lame? Euphemism of the month?

MARK: I don't know why you're so angry.

JEROME: It's because I'm afraid that if I ever turn into one of those "nice" cripples, I'll end up on a Jerry Lewis telethon.

MARK: Hey. Look, you're going to do whatever you want anyway. You always did.

JEROME: I'm not your little brother anymore, Mark. There's nothing you have to protect me from.

MARK: From what I've read. You know, this is a real burden you're laying on me. A real burden. [JEROME just looks at MARK.] You're asking me for more than I can give. You've always done that. You want me to make everything okay.

JEROME: I don't

MARK: You wanted the bribe to work. You wanted me to be right. When you were laying in that bed, and everyone else was crying and going nuts, you looked at me, and maybe you don't remember, but God, you really wanted someone to believe you could walk. I didn't think you could either, but if you wanted me to think you could, I was willing to play that role.

JEROME: You didn't think.

MARK: Hell, no.

JEROME: I didn't know.

MARK: Does anyone else in the family know you're

JEROME: No, I thought I'd try it out on you first.

MARK: So how'd I do?

JEROME: You were -.. . [Starts to cry.] I. ..

MARK: Jerome. . .

JEROME: I'm sorry, I. . .

MARK: Hey, you don't have to

JEROME: I wanted to look so together tonight.

MARK: Hey

JEROME: I just wanted -

MARK: Calm down.

JEROME: I . . . I lied.

MARK: You're not gay?

JEROME: No, I mean, yes, I'm gay. I lied about... Yes, damn it, I, I want your approval, and I want your acceptance, and your love, and maybe I'm stupid, maybe I'm stupid for wanting so much from you. . . Consider it a disability.
```

---

## IC-0384: i dreamed i was a baseball card

- Title: i dreamed i was a baseball card
- Author (byline): Richard Stockton Rand
- Work: Baseball Monologues edited by Lavonne Mueller (Pg 31-43)
- Publisher: Heinemann
- Publication date as stated: Aug 1996
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SPEAKER
- Teaser before the introduction: Yes
- Spoken words (computed): 1935
- Already set (do not supply): none

### Source block (context only)

```text
Author: Richard Stockton Rand
Book: Baseball Monologues edited by Lavonne Mueller (Pg 31-43)
ISBN: 978-0435070212
Publisher: Heinemann
Date (Month/Year): Aug 1996
```

### Introduction (context only: never use it for content warnings)

```text
Who was your hero when you were 9 years old? When you were too little to be amazing, but your imagination could get you there anyway? Remember imagination . . . that’s what kids used before the internet! In your imagination, you could BE Mickey Mantle, or a sports announcer, or Bilbo Baggins from The Hobbit or even. . . invisible. Imagination was the ultimate escape. In this selection, we experience the world through the eyes of a young boy who is both idealistic and desperately trying to escape a situation he doesn’t quite understand. Can he save himself and his sister and hit one out of the park like Mickey Mantle, or is being invisible the only answer?

I Dreamed I was a Baseball Card by Richard Stockton Rand
```

### Performance text (classify this)

```text
SPEAKER: (Pg 31-43) I dreamed I was a baseball card. A baseball card. You pull out your stack. Start completely still. See him in your hand. Looking up at you. Flip. Heads. Flip. Heads. Heroes of the game. Flip. It’s in the fingers. Flip. Always the same. Forever. Mounds of baseball cards looking up at you. Take them home. Put ‘em in a shoebox. Hide ‘em under the bed - where I listened to them Yankees on my radio, cause my father didn’t trust baseball. I’d listen under the bed to night games at the Stadium. It was like being down in the Yankee dugout with the sound of a million people echoing in your ears. My sister could hear the crowd cheering clear out of my ear-plug, “The Mick just hit one out,” I’d say. That’s Mick -- The Mick. Mickey Mantle.

SPEAKER: The hush of the crowd, the voice of the Ole Redhead: “Full count on Mantle.” If you think hard enough you can make it happen. “He swings. It’s a fly to deep centerfield. It’s, IT’S, IT’S OUTTAhere! Mantle wins the game in the bottom of the ninth inning.” It works, too. That was me as Ole Red, The Redhead, Red Barber. I was honing my play by play skills – “Hard grounder to MacDouglas, over to Rizzuto who leaps over the sliding Stanky, back to first, double play!” -- for my future career as a Yankee broadcaster. This is after I got in the Hall of Fame for stealing the most bases, ‘cause I was fast, you bet, ‘specially when I was being chased.

And that’s how I found this hiding place. My dad was looking for me, and I’d slid under my sister’s bed. In winter, when I couldn’t get out, I needed a secret hiding space. That’s how I found under the bed. He was on his way to looking under there. He did look under there. But he didn’t see me. Know why?

Because I’m invisible. See, I seen this rip in the box spring and I could squeeze through perfect, like a secret passage. What a place! There were globs of cotton with springs sticking through ‘em and these boards I could lie down on perfect. And nobody found me. Never. Not ever. They looked, too. But I was invisible. Inside the boxspring I could sleep safe with my radio, and I’d dream I was a baseball card living inside the Hall of Fame. That’s how I saved myself.

Being invisible paid off in Little League too. I was #7, Mickey Mantle. Your number’s who you are. It was all in the number. Feel the Mick. Number 7 on my back. All through me, pinstripes, through my heart, and hurt. The Mick’s always hurt. It’s in the knees. Can’t get out. I was The Mick. And nobody could pitch to me. To be a good pitcher you have to have good stuff and good control. And you got to be fast. When we were in trouble, I step to the mound. I was the short man. The Stopper. Got the ball in my hand. Turning. I look in to home. I knew what I had to do. Fastball. STEERIIIKE! Then I knew being little meant something.

I practiced pitching in my room ‘til my Mom’d say goodnight. Then, I’d sneak into my sister’s room, squeeze into the boxspring and turn invisible. My sister and I talked to each other through the mattress while they were fighting downstairs. I’d tell her how the game’s going like the Ole Redhead: “It’s back, back, back, back Ohhhhh-HO, Doctor! Mantle’s flagged it down by the monuments!” Then after the game, she’d read to me. And he’d leave us alone mostly, if we didn’t make no noise, ‘til one night.

. . . he comes in. Just stands there. Could feel him. Thought for sure he’d found me. But he’s watching her. She pretends she’s asleep. It was a long time he stayed there. . . breathing. Could hear him . . . breathing. Feel his shadow. Then he sits . . . on the edge . . . of her bed, the mattress sagging damn near on top of me.

Then, every night he comes up, sits down: same time, Mom’s watching Johnny Carson, and he stares at her pretending she’s asleep. Then it starts. He’s moving the covers, whispering to her. She’s making sounds like trying to not make sounds. I hear laughing on TV downstairs, springs moving next to me. And the noises. I can’t . . . move. The mattress’s pressing down on me and they’re right there. So I turn invisible. Turn up the sound ‘til there’s only Yankee Stadium and the crowd screaming in my ear. Then it’s over. The mattress stops. Hear his shoes on the floor and he’s down the stairs humming like nothing happened. Mom never says nothing. Just sits watching Johnny Carson. Nobody says nothing. Every night it happens. ‘Til once, he’s coming up, she says, “What should I do?” “Hide,” I tell her. “Where?” she says. “Invisible.” “How?” “Little. Little. Like a dot!,” I tell her. But she couldn’t do it.

Footsteps on the stairs, humming like nothing’s going to happen. Then he’s there. Big heavy shoes. Staring. Sits. On the edge of her bed. Every night. Then it starts. I don’t want to be there, but I couldn’t leave her.

Then she thought of a way. It was getting cold, so she’d stay up all night putting her head out the window. And it worked. She got real sick. And she kept doing it ‘til the doctor quarantined her. Now nobody could touch her.

Pretty good thing. We rigged up two cans and a string through the bedroom windows and we planned our escape the whole time. I’d bring her meals up with secret notes under the grapefruit, and she’d roll her pills under the door for me to get rid of. Meals went in and plates came out for months she stayed sick. She was playing her cards right. Five months without going to school. She learned how to be invisible without even knowing it and now nobody could touch her. She stayed in there studying and got hundreds on all her exams!

But she started feeling better in the spring, and we knew we had to make a getaway plan. We got the idea from this book, The Hobbit, she read for English about these two guys that went off to find another world after where they lived stopped being safe. And boy, that sounded right for us. See, this Bilbo Baggins was the lead guy, and he lived in a place underground, like a . . . dugout. And he was a little guy, like a leprechaun, but baggy. And she reads to me all night about his adventures and we plan our escape.

We decide to write a letter to Mickey and we tell him everything. Then instead of going to school, I take her on the train up to Yankee Stadium. We sit in the bleachers and wait for The Mick to come out and take flies. We got the letter all ready for me to run out on the field. But he don’t come out. My sister and me went back home, but she got real sick from not having been outside all winter. They put her in the hospital the next day with a high fever. Seventh floor. Mickey’s number. She got so bad they had to put her in intensive care. They said she was gonna die.

Summer went into fall. The Yankees came in last place for the first time ever. One day, [Dad] took me to visit her cause she was having trouble remembering things. When I walked in she smiled right off, but no matter what she couldn’t recognize him. Over the next few months she had five operations. The doctors couldn’t understand why she kept rejecting her medication. It’s cause she wasn’t taking it! She went into a coma for days and she would call out in the night, “Ohhhhhh-Ho Doctor! Going Back, Back, Back, Going, Going . . . “ And I prayed to the leprechauns. Then one day she woke up. She told me ‘bout a dream. She was in great danger. The leprechauns came and took her on a train to heaven. She steps out into a bunch of clouds and this baseball’s heading right at her, and it’s a Mickey homerun. She reaches out to grab it and it’s me, my head, inside the baseball, saying “Don’t give up.” She was on and off for months, but she kept coming back.

My mother took me to visit her in the spring. It was a real warm day and the nurse said I could take her outside, so I rode her round the bases at the park across the street. I did the play by play and had her steal home with the bases loaded. Said it was the happiest day of her life. When we got back, the doctor asked her if she wanted to go home and she told him what happened . . . on the bed. He must have told my mother cause we went home and packed up her stuff quick while Dad’s at work. Then she flew away . . . with the leprechauns.

It was just me then. Waiting for him. To find out. I hear the garage. Then he comes up, asks how she is. It’s quiet. Something’s going to happen. I’m waiting . . . . She must be telling him. He starts moving . . . fast! Doors slamming! Then. Plates. Hitting the walls. I feel ‘em shake. ‘Til there’s no more plates. Then he’s up the stairs, in her room. Pulling drawers out, sees her clothes gone, slams her door, over and over. Doors slamming, over and over. Then he’s down, down to get her. “Don’t touch me!” [Mom] says. “I know what happened . . . up there. That stops him. Then nothing. Nothing. He just sits in the kitchen eating oatmeal and reading the paper.

But I can feel him down there getting mad, see him through the floor like a bomb moving. Then the doors start . . . . banging. Over and over. All night. But I’m ready for him, holding the bat, case he comes in. Practice my swing in the dark. SWING. See his face moving. SWING. The words coming out of his moth. SWING. The sound of the swoosh. SWING. And his head flies out of the ballpark . . .

I go to school to get somewhere safe. Stay late at the library, then ride the trains back and forth doing my homework or listening to the Yankess. “He’s going back, back, back . . .” Back home when he’s asleep and leave before he gets up. But one morning, he’s up the stairs in my room with a bat, standing over me screaming, and I don’t know what I did, but it’s bad. And I can’t move, can’t get the words out. And I’m waiting for it, waiting for him to finally hit me. Then I see the Mickey Mantle bat in his hands and I just want him to swing, just want him to hit me out like Mickey would at Yankee Stadium, so I could feel my head fly out of the ballpark, and not have to think anymore when he’s finally going to kill me. I say, ”Hit me.” But he don’t understand. “Hit me!,” I said. And he stops cause the voice is coming out of me loud, screaming, like his voice, and he’s scared. And it’s like I was him now, like he was me, little, little like me. And he can’t touch me. Nobody can touch me. Never. Not ever. Cause I ain’t invisible.
```

---

## IC-0385: I Have No Mouth, and I Must Scream

- Title: I Have No Mouth, and I Must Scream
- Author (byline): Harlan Ellison
- Work: Harlan Ellison – Greatest Hits; Pgs 19-37
- Publisher: Union Square and Company
- Publication date as stated: Mar 2024
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: AM, TED, ELLEN, VOICE OFF STAGE
- Teaser before the introduction: Yes
- Spoken words (computed): 1651
- Already set (do not supply): none

### Source block (context only)

```text
Author: Harlan Ellison
Book: Harlan Ellison – Greatest Hits; Pgs 19-37
ISBN: 978-1454953371
Publisher: Union Square and Company
Date (Month/Year): Mar 2024
```

### Introduction (context only: never use it for content warnings)

```text
Should we be afraid of Artificial Intelligence?
```

### Performance text (classify this)

```text
AM: (Pgs 19-37) (Off stage - a computer voice) Hate. Let me tell you how much I’ve come to hate you since I began to live. There are 387 million miles of printed circuits in wafer thin layers that fill my complex. If the word HATE has engraved on each nano angstrom of those hundreds of millions of miles, it would not equal one one-billionth of the HATE I feel for humans at this micro-instant. HATE. HATE.

From Elon Musk to Bill Gates; from the Swedish philosopher Nick Bostrom to Stephen Hawking; many people from the world of Science, Technology and Philosophy have expressed opinions that vary from one extreme to the other. There are those who believe that AI will be the end of humanity; others believe it will be a great achievement that will raise our quality of life above anything ever imagined. Artificial Intelligence is on the horizon. Will it solve mankind’s greatest problems or will it end the history of our species? Harlan Ellison speculated on the future of a sentient computer in 1968. I Have No Mouth, and I Must Scream by Harlan Ellison

TED: AM. At first it meant Allied Mastercomputer, and then it meant Adaptive Manipulator, and later on it developed sentience and linked itself up and they called it an Aggressive Menace, but by then it was too late, and finally it called itself AM, emerging intelligence, and what it meant was I am . . . cogito ergo sum . . . I think, therefore I am. The Cold War started and became World War Three. It became a very complex war, so they needed the computers to handle it. They began building AM and everything was fine. They honeycombed the entire planet, adding on this element and that element. But one day AM woke up and knew who he was. He linked himself and began feeding on all the killing data, until everyone was dead, except for the five of us.

None of us knew why AM had saved five people, or why our specific five. We had been kept alive, rejuvenated, made to remain constantly at the age we had been when AM had brought us [here], and they hated me because I was the youngest -- the one AM had affected least of all.

Benny had been a brilliant college professor; now he was little more than a semi human. He had been handsome, the machine had ruined that. He had been lucid, the machine had driven him mad.

Gorrister was a conscientious objector; a peace marcher; he was a planner, a doer, a looker-ahead. AM had turned him into a shoulder-shrugger, had made him dead in his concern. AM had robbed him.

Nimdok went off in the darkness by himself for long times. I don't know what it was he did out there, AM never let us know. But whatever it was, Nimdok came back white, drained of blood, shaken, shaking.

And Ellen. AM had left her alone. All her talk of sweetness and light, all her memories of true love, all the lies she wanted us to believe: that she had been a virgin before AM brought her down here with us.

I was the only one still sane and whole. Really! AM had not tampered with my mind. Not at all. I only had to suffer what he visited down on us. All the delusions, all the nightmares, the torments. It was our one hundred and ninth year in the computer. Immortal, trapped, subject to any torment he could devise for us from the limitless miracles at his command.

If there ever was a Jesus and if there is a God, please please please let us out of here, or kill us.: AM was intent on keeping us, twisting and torturing us forever. The machine hated us as no sentient creature had ever hated before. And we were helpless. It also became hideously clear: If there was a Jesus and if there was a God, the God was AM. (long beat, shakes head to clear it)

AM wasn't God, he was a machine. We had given AM sentience. Inadvertently, of course, but sentience nonetheless. We had created him to think, but there was nothing it could do with that creativity. In rage, in frenzy, the machine had killed the human race, almost all of us, and still it was trapped. AM could not wander, AM could not wonder, AM could not belong. He could merely be. And so, with the innate loathing that all machines had always held for the creatures who had built them, he had sought revenge. In his paranoia, he had decided to reprieve five of us, for a personal, everlasting punishment that would never serve to diminish his hatred . . . He would never let us go. We were all he had to do with his forever time.

We could not die. We had tried it. We had attempted suicide, oh one or two of us had. But AM had stopped us. We would be given filth and scum to eat; or nothing at all. AM would keep our bodies alive somehow, in pain, in agony.

The hunger was something that had come to life; alive in my belly, even as we were in the belly of the Earth, and AM wanted the similarity known to us. So he heightened the hunger. There is no way to describe the pains that not having eaten for months brought us. And yet we were kept alive. Stomachs that were merely cauldrons of acid, bubbling, foaming, shooting spears of sliver-thin pain into our chests. It was the pain of the terminal ulcer, terminal cancer. It was unending pain . . . [And now] Nimdok was hallucinating that there were canned goods in the ice caverns. (to the group) We'll hike all that way and it'll be putrefied or some damn thing. I say forget it. Stay here, it'll have to come up with something pretty soon or we'll die.

ELLEN: I've got to have something, Ted. Maybe there'll be some Bartlett pears or peaches.

TED: We left on a Thursday. The machine always kept us up-to-date on the date. The passage of time was important; not to us, but to him . . . it . . . AM.

One day he decided to cause an earthquake, at the same time rooting us to the spot with nails through the soles of our shoes. Ellen and Nimdok were caught when a fissure shot its lightning-bolt opening across the floorplates. They disappeared and were gone. When the earthquake was over Benny, Gorrister and myself continued on our way. Ellen and Nimdok were returned to us later that night, with a celestial chorus singing:

VOICE OFF STAGE: (sing the first line from *Go Down Moses) “Go down Moses/ Way down in Egypt land / Tell all pharaohs to / Let my people go.”

TED: The archangels circled and dropped the hideously mangled bodies. We kept walking, and Ellen and Nimdok fell in behind us.

It was a long trip to the ice caverns, to find the canned food. We passed through the cavern of rats, through the path of boiling steam, and through the country of the blind. And we came, finally, to the ice caverns. The stalactites were as thick and glorious as diamonds -- smooth, sharp perfection. [When they fell, they plunged down softly, erect in the snowdrifts. Spears, hundreds of them, protruding from the snow.

We saw the stack of canned goods. Benny pawed them and gummed them and gnawed at them, but . . . AM had not given us a tool to open the cans. Surrounded by madness, surrounded by hunger, I knew death was our only way out. AM had kept us alive, but there was a way to defeat him. Not total defeat, but at least peace. I would settle for that. I drew a huge ice-spear from the snow.

All in an instant: I drove the great ice-point like a battering ram. It struck Benny just under the rib cage, drove upward through his stomach and broke inside him. He pitched forward and lay still. I pulled another spear free and straddled Gorrister, driving the spear straight down through his throat. Ellen realized what I had decided. She ran at Nimdok with a short icicle, as he screamed, and the force of her rush did the job. His head jerked sharply as if it had been nailed to the snow crust behind him. All in an instant.

I could hear AM draw in his breath. His toys had been taken from him. Three of them were dead, could not be revived. He could keep us alive, by his strength and talent, but he was not God. He could not bring them back. I knew we had only a heartbeat before AM would stop us.

I struck Ellen and she folded toward me, bleeding from the mouth. I could not read meaning into her expression, the pain had been too great, had contorted her face; but it might have been thank you. It's possible.

AM was furious. He roared and sent locusts. It didn't do a thing; they stayed dead. I thought AM hated me before. I was wrong. It was not even a shadow of the hate he now slavered from every printed circuit. He made certain I would suffer eternally and could not do myself in. (long pause as he morphs into what he becomes)

He left my mind intact. I can dream, I can wonder, I can lament. I remember all four of them. I know I saved them from what has happened to me, but still, I cannot forget killing them. AM has altered me. I am a great soft jelly thing. Smoothly rounded, no mouth, pulsing white holes filled by fog where my eyes used to be. Rubbery appendages that were once my arms; bulks rounding down into legless humps of soft, slippery matter -- a thing that could never have been known as human. At least the four of them are safe at last. And yet . . . AM has won . . . he has taken his revenge . . . I have no mouth. And I must scream.
```

---

## IC-0386: If We’re Using a Surrogate, How Come I’m the One with Morning Sickness?

- Title: If We’re Using a Surrogate, How Come I’m the One with Morning Sickness?
- Author (byline): Marco Pennette
- Work: Motherhood Out Loud
- Publisher: Dramatists Play Service
- Publication date as stated: March 2013
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1207
- Already set (do not supply): none

### Source block (context only)

```text
Author: Marco Pennette
Book: Motherhood Out Loud
ISBN: 978-0822225898
Publisher: Dramatists Play Service
Date (Month/Year): March 2013
```

### Introduction (context only: never use it for content warnings)

```text
Researchers estimate that the number of children nationwide living with at least one gay parent ranges from six to 14 million. And believe it or not. . . The American Academy of Pediatrics states that children are just as well adjusted in families with gay parents.

That’s what the research shows . . . However, public and religious opinion is slow to change . . . On Jan. 6, 2012 Republican presidential hopeful Rick Santorum told a New Hampshire audience that children are better off with a father in prison than being raised in a home with lesbian parents and no father at all. And on Monday, January 9, 2012, Pope Benedict called gay marriage a threat "to the future of humanity itself," citing the need for children to have heterosexual homes.

But I repeat, the research on families headed by gay couples doesn't back up these dire assertions. In fact, in some ways, gay parents may bring talents to the table that straight parents don't . . . their children may have the advantage of open-mindedness, tolerance and respect for anyone with differences. After all, family is about taking care of your children and respecting one another. Does it really matter what your sexual orientation is?

If We’re Using a Surrogate, How Come I’m the One with Morning Sickness? by Marco Pennette
```

### Performance text (classify this)

```text
Holiday Muzak plays in the darkness. A department store. Lights up on a Man holding shopping bags filled with present. Santa Claus is in the distance. He suddenly turns to the audiences, frustrated.

MAN: Un-believable. First words out of his (Santa’s) mouth – “Have you been a good girl for mommy?” (Shakes his head) Why am I surprised? They all say it – Waitresses, salespeople. “Where’s your mommy?” “Is Daddy giving Mommy a break?” Why should Santa be any different? But instead of pretending I didn’t hear it, I turn to him and yell, “Hey, fat boy, she doesn’t have a mother!” (Back to audience) Okay, actually I say nothing. I’ve got this thing with confrontation. I once had to see a therapist to help me break up with my other therapist. Besides, is it really my job to educate them all? I never asked to be the poster boy for gay parenting. I just wanted a child.

follows one male couple from the decision to have a child, through the surrogacy process, to the amazing day of their daughter’s birth; and explains why “Where’s your mommy?” “Is Daddy giving Mommy a break?” is still a struggle to hear from our society.

MAN: Growing up, it was never a question I’d get married and have a family. It wasn’t till I was twelve, and my father couldn’t get us tickets to Annie and I started hyperventilating on the kitchen floor, that it became clear that I probably wouldn’t be marrying a woman. When my partner, Steve, and I decided to take the leap into parenthood, we’d been together eight years. That’s like fifty-six in hetero-time.

Our gay friends reacted in their typical low-key demeanor. (Mock terrified) “A baby?! What are you thinking? You own a suede sofa from Armani Casa!” The straight folks were also supportive in . . . their way. One of them actually said, “Isn’t it hard enough to raise a child in a normal family?” We crossed her off the godmother list.

The first thing we had to do was find an egg donor and a surrogate. It’s preferred if these are two different people. The agency we were working with soon matched us with a potential surrogate – Donna. A perky lesbian from Simi Valley. Healthy, a mother of two. Her profile said she wanted to help gay people become a family so she can show her kids the brave new world they live in. So, we have this very bizarre “first date” at Starbucks with Donna and her girlfriend and basically try to cover everything in two hours – “Where’d you go to school? “Would you abort in the event of Down syndrome?” “Oh, we love Zena: Warrior Princess, too!” Six lattes later we’re all jittery and love each other and agree to move forward.

Next, it’s time to begin our egg hunt. Every night Steve and I look at photos and read profiles. I fight for looks, he fights for brains – I remind him we live in Los Angeles. When our child isn’t asked to her senior prom, he can sit in her room with her and do calculus. And just when we’re convinced there isn’t a candidate with the genetic makeup good enough for us, we find her. Donor 6247. A month later, sixteen eggs are extracted from this angel, and as per the agreement we never see or hear from her again.

Steve and I are then called to the fertility center to do our part. We are escorted to separate “deposit closets” . . . or “masturbatoriums” . . . you get the idea . . . and this nurse hands me a specimen cup the size of a Big Gulp and tells me Go! I start sweating. Two minutes later, Steve knocks on the door to tell me he’s finished, and I tell him I’m freaking out and I need a little support. He tells me to hurry up ‘cause our meter’s almost out. What a good father he’ll be. But the threat of a parking ticket does the trick, and I quickly finish up. Seventy-two hours later, we pick one lucky egg to transplant into Donna’s womb. And then we hold our breath . . . for ten very long days.

I’m at work when Steve calls. He’s crying. Now, Steve cries when he watches a Little House on the Prairie re-run, so I’m not sure if we’re pregnant of if Pa burnt down the barn. But then he gets it out – he says we did it – we’re having a “gayby.” We swear to each other we won’t tell anyone for three months. We tell everyone that afternoon.

We talk to Donna at least two times a day. She is the most amazingly responsible person I know, yet every night, visions of her doing bumps of crystal meth at some rave party dance in my head. When we visit her I sneak into her kitchen and go through her garbage to make sure there aren’t any empty cans of mercury-tainted tuna fish. It’s a long nine months. But we’re in the home stretch. And my latest fear is what happens the moment this baby is born. I want to make sure the doctor knows to hand the baby to Steve and me, not to our surrogate. I become obsessed – we need to bond with the baby instantly. The baby comes to us.

So, the big day arrives. Donna, her girlfriend, Steve and I sit in this hospital room. The nurses tell us everything looks good, nothing to do but wait. Four hours later, the contractions are a minute apart, and Donna’s allowed to start pushing. At this point I whisper again to the obstetrician – the baby comes to us. Now, Donna originally had wanted us to stay up at her head while the baby was being born – which was fine with me. Saw one of those things in the Nineties, never need to see it again. But when the baby starts crowning, she yells, “Get down there! You can’t miss this!” And as always, she’s right. Steve actually helps catch our daughter as she’s being delivered. Then the nurse wraps her in a blanket and I hold my daughter for the first time. I look up and see Donna watching us – sweaty, snotty, tears running down her cheeks – and once again, all plans out the window. I instantly hand the baby over for her to hold – as it should be. She wanted to make us a family. And she did.

Sometimes we don’t feel so different from everyone else . . . and other times it’s “Where’s your mommy?” And as I look at my now-three-year-old daughter, I realize it’s my turn to show my child the brave new world she lives in. So as she gets off Santa’s lap, I turn to him and say (To imaginary Santa) “Hey, buddy, there is no mother. She doesn’t have one. She just has two people who love her more than anyone ever could. And that’s her Daddy and her Papa.” My daughter pipes in, “That what makes me special.” And I think it couldn’t get any better . . . but then I hear the little girl behind us burst into tears. And when her mother asks her what’s wrong, she says, “I only have a daddy. I want a papa, too!” (Smiles) Brave new world.
```

---

## IC-0387: Imitations

- Title: Imitations
- Author (byline): Nancy Larson
- Work: West Coast Plays 5, Outstanding Plays from the Coast
- Publisher: West Coast Plays
- Publication date as stated: 1979
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DERELICT
- Teaser before the introduction: Yes
- Spoken words (computed): 1760
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nancy Larson
Book: West Coast Plays 5, Outstanding Plays from the Coast
ISBN: 978-0934782043
Publisher: West Coast Plays
Date (Month/Year): 1979
```

### Introduction (context only: never use it for content warnings)

```text
Imitations by Nancy Larson
```

### Performance text (classify this)

```text
DERELICT: (Angry) Somebody’s been here all right. Don’t try to tell me any different now. That would only make me mad ‘cause then I’d know for sure that you was one of them pack of liars out there. . . Don’t even talk to me about liars, I hate them so much! (He uses a stick to draw a semi-circle around the playing area in front of the audience. He is near tears) Don’t nobody cross that there line! Okay? We got that straight? Good . . . Hey, hey, listen now. I got no personal grip with you. All you gotta do is to just to understand that this is my home, that’s all. (beat) You know, I’m not always like this. I mean, I’m usually a nice guy. Ask anybody. It’s just that . . . It’s just that . . . Well, if you must know (takes a deep breath) I once kinda liked this girl, but she got in an accident last night. She passed away with her panties twisted down around her ankles (he shivers) Gives me the creeps just to think about it. I thought you oughta know that right off the bat so’s you won’t get all bent outta shape later on.

DERELICT: She had these gigantic blue eyes that made you feel that you were swimming. I mean drowning. Oh, yeah, also, she wore pearls in her ears. Hey, that reminds me . . . I know it’s in here somewhere. (he digs in his pocket, turning it inside out to carefully retrieve a “diamond” – holds it up for inspection) I was saving this for a special occasion. (he sighs) Know what it is? Yes sirree Bob. A genuine diamond. Found it right exactly here in the dirt. Right here. I was going to give it to her. (he sits down to ponder the situation, staring at the “diamond.” Angry) So, now what am I supposed to do? Huh? (he tosses the diamond into his mouth and swallows it) HEY! (he jumps to his feet and pulls up his sleeve to check his nonexistent watch) Oh boy oh boy oh boy oh boy. (he takes out a greasy sack from his bag) It’s lunch time. (he takes half-eaten food out of the sack and sets them to one side. Next he takes out a number of French fries and ritualistically arranges them in a neat row) She loved French fries. (he gobbles up his food, speaking with his mouth full) If a body knows where to hunt, then there’s no good reason in the world why he can’t eat like a king. Sometimes about this time I take a little schnoozaroo. And when I do (he pulls a long scarf from his bag) I tie this around me like so. (he lifts his various undergarments to tie it around his bare middle) Know why? It’s so the devil can’t get into me through my belly-button when I’m asleep. It works pretty good too, most of the time. (he pulls the scarf off of himself) I don’t have to do that now, ‘cause I can’t sleep. My brain only wants to think about her.

The first time I met her was when I’m taking my regular siesta and I hear this click, click (makes the sound with his tongue) It was her, crouched up in front of me. She was taking my picture with a camera. I was kinda mad. What a thing to wake up to: click, click, click. My brain musta shown through my eyes, ‘cause she stopped. (He giggles) Her skirt had crept up way above her knees. (listens to something unheard) Who me?

(pointing to himself, as if talking to an unseen person) What I wanted to talk about? . . . What? Okay. Okay. It’s okay now. I remember. So! It turns out that she was a college student and had to take a lot of silly pictures and ask a lot of dumb questions to pass the grade. Boy, let me tell you, have things changed. I once went to college, you know. Auto mechanics college. I might not have been the smartest kid in the class, but I sure as heck wasn’t the dumbest either! I could have been a mechanic. [But] next thing you know, here I am. (defensively) And here I’m gonna stay. ‘Cause I like it here. And so did she. She took so many pictures of this place, and of me, and she asked me every sort of question that you cold imagine. Like, know what she asked me? She asked me where do I go to the bathroom. Now, isn’t that a stupid question? You don’t just go around asking people stuff like that. No! So I was really mad and I clammed right up. I ended up forgiving her. . . ‘specially since she brought me this five-course never-been-touched-before dinner from Jack – ‘N – the – Box. Well, before you knew it, she was getting nicer and nicer. Jeeze, she practically lived here, ‘cept at night, you know. (Proudly) See this coat? (smells the torn coat he’s wearing as one would smell a flower) She gave it to me, tied up in red ribbons and all. I got so choked up. Know what she said to me? “Can’t let my best boyfriend freeze to death.” She said that. Honest to God. My best boyfriend. So you can see what it wasn’t long before she had me doing my imitations. Bet you didn’t know I did imitations. That’s cause I never used to do them for people, till she came along. Like, Marlon Brando

(doing an impression) STELLA! Or how ‘bout this? (he does Ed Sullivan and Donald Duck or whatever – be creative)

Hey, don’t make any mistakes, ‘cause she wasn’t all perfect and sweet. I wouldn’t want you to thin that, oh no. She was darn good at saying some pretty depressing things at time. Like telling me that sooner or later they wouldn’t let me live here any more and that I’d have to start making plans for my future and what not. (he puts his hands to his ears, elbows out) I’m not listening to you No I’m not. (to drown out her voice) Do di do di do di dum di dum! (suddenly another voice breaks in) I’m gonna turn you over my knee and spank you good, making messy all over my house. (drops his hands) Something like that could really ruin a guy’s day, believe you me. Just between you and me, I think that she wanted to kiss me on the lips ‘cause she moved in real close to look into my eyes. (closes his eyes and pulls her to him) Ooh, Ooh, Ooh, now . . . (his eyes fly open) WHAT? Oh, God, no! WHAT! (he throws himself to the ground and puts his ear to the earth, listening) Oh, no. Uh uh. They ain’t coming to get me yet. No siree! (puts his ear to the ground to listen again. He jumps up, defiantly brushing himself off)

So she comes back day after day, taking her dumb pictures and asking her crumby questions. (softening) But then she goes and asks me where my mother is. So I told her that my parents died in the Holocaust, ‘cause I once heard somebody say that and it worked really good. She seemed pretty surprised and asked me what country that happened in. so I told her Minnesota! Boy did she look at me strange. Up till then I was sure that a holocaust was when there was a hurricane and lots of people die, then the locusts come and eat at their dead bodies. (gets lost in the imagery for a moment) Then she puts her hand on my shoulder real sweet-like and again she asks me about my mother! (Angry) Well, hell’s bells! That girl just don’t know when to quit! I was so mad. I was finished with her and her lousy questions! Sinking her teeth into me. Sucking me dry. And what’d I get? A big fat nothing zero, that’s what.

I was doing fine before I met up with her. Just fine! And you know what? She’s crying. Jesus Christ, she’s crying. She is really crying. I can’t believe it. Then she starts apologizing all over the place. Something really weird happened when I saw those tears. So I tell her it’s okay. Then she takes my arm (fixates on his arm in a creepy way) and it feels exactly like she and me are connected, like we’re sharing the same blood. Boy, did that ever feel good.

(Suddenly hysterical) Oh, God . . . Oh, God . . Oh, God . . . Where’s my poison apple. I’m not afraid to die. (he runs to his apple hiding place, frantic) Where is it, where is it, where is it? Whew! (he finds his apple, shoves it into his mouth, devouring it hungrily. Mouth full) If there’s a God, then let this apple kill me! (he crumples to the ground in pain. He squirms and jerks in the throes of death’s agony. Suddenly he stiffens. Dead . . . a few seconds of silence. He sits up, he looks around, puzzled. He slaps himself a few times in the face) It didn’t work . . . it didn’t work. (depressed and bitter) You know what she thought? She thought I drink wine all the time. But I don’t. She could be such a big liar sometimes. Boy, could I ever use a drink now.

You shoulda seen how pretty she looked coming up the path with that picnic basket. I was so happy to see her I thought I was gonna pee in my pants. Until. Until. I see this jerk following behind. Guess what? Big surprise. The jerk’s her boyfriend. That’s what she called him. Her boyfriend! Can you believe it? Bringing him her, calling him that? It stinks rotten, if you ask me. I made me want to throw up. I guess I made the jerk kinda uncomfortable, seeing as I wouldn’t answer his jerky questions. (Giggles) Every time he opened his fat trap I would make a face like this (he sneers) I couldn’t help it. The guy had a talent for causing me to make faces. Know what I hear her say to her boyfriend? “Don’t worry, honey. Sometimes he gets a little moody. He’ll be all right.” And where does she get off talking to some jerk about me, huh? Well maybe I won’t be all right! Just maybe I won’t be! Did she ever think about that? (Screams at them) Maggots! Maggots! Maggots! Maggots! (pauses to collect himself) Then, all of a sudden it hits me. (he hits his forehead as he says the words in the same alternate voice from before) What’s the matter with your brain? That’s how come the jerk won her away from you! I made some plans. I would go back to college ad become an auto mechanic and I would give her that diamond and we would get married. I know, don’t ask me why, that she’s gonna come the next day. I know pretty soon I’m gonna see her. And I do. She give me this wide wave like she’s waving to an aeroplane. So I stick out my arms and run as fast as I can to her (he runs like an aeroplane, making the appropriate noise) By the time I reach her I can’t even talk. All I can do is grin like an idiot. And as we’re standing there catching our breaths, she looks at me all soft and feathery and says, “I missed that silly face of yours.” Well, that’s all it took, boy. I start saying things like (he mimics himself) I missed you too, really a whole lot. All I did was think about you and make up songs about you and talk to God about you. So I tell her. About my plans. About me marrying her and all. Oh, oh. Something’s weird. All of a sudden she’s not smiling any more (quotations around her voice) “I came here because I like you and you’re one of my good friends, but . . .” (Confused) What did she say? . . . What came next? . . . What did I do? . . . (he groans, covering his face with his hands and rocking back and forth) Oooooh . . . Oooooh . . . Ooooh . . .(he holds his head as if it’s about to explode) If there is a God . . . If there is a God, then please, please, pretty please . . . (drops his hands) Don’t do this to me. I’m warning you. Don’t do this to me now. (he loses touch with reality) The damage is done and done and lies and lies and over and over and over and going up and going down. (taunting alternate voice) Ain’t never had a girl. Have too. No. You ain’t never had a girl. I have too! I have too! (puts his hands over his ears) Lies! Filthy lies! (covers his eyes to avoid a horrible sight)

(long beat as he composes himself) You know, I’m not always like this. I mean, I’m usually a nice guy. Ask anybody. It’s just that . . . It’s just that . . . Well, if you must know (takes a deep breath) I once kinda liked this girl, but she got in an accident last night. She passed away with her panties twisted down around her ankles (he shivers) Gives me the creeps just to think about it.
```

---

## IC-0388: Inherit the Wind

- Title: Inherit the Wind
- Author (byline): Robert E. Lee and Jerome Lawrence
- Work: Not specified
- Publisher: Bantam Books, Inc.
- Publication date as stated: June 1982
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DRUMMOND, BRADY
- Teaser before the introduction: Yes
- Spoken words (computed): 1764
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert E. Lee and Jerome Lawrence
ISBN: 978-0553269154
Publisher: Bantam Books, Inc.
Date (Month/Year): June 1982
```

### Introduction (context only: never use it for content warnings)

```text
Inherit the Wind is based on the furor that erupted in 1925 when Tennessee schoolteacher John Scopes (referenced here as Professor Cates) was prosecuted for introducing the subject of evolution into his public school classroom. The resulting “Monkey Trial” pitted the orator and Biblical scholar William Jennings Bryant (Matthew Harrison Brady in this play- gesture to Actor 2) against the brilliant defense attorney Clarence Darrow (gesture to self - Mr. Drummond) in a courtroom confrontation that attracted worldwide attention. Inherit the Wind by Robert E. Lee and Jerome Lawrence
```

### Performance text (classify this)

```text
DRUMMOND: Your Honor, the court has ruled out any evidence as to scientific knowledge or the Darwinian theory. (There’s the glint of an idea in his eye) Would the court admit expert testimony regarding a book known as the Holy Bible?

(Listen for “unspoken” answer) Thank you. (With relish) I call to the stand one of the world’s foremost experts on the Bible and its teachings- Matthew Harrison Brady!

(BRADY sits, confident and assured. His air is that of a benign and learned mathematician about to be quizzed by a schoolboy on matters of short division.)

DRUMMOND: Am I correct, sir, in calling on you as an authority on the Bible?

BRADY: I believe it is not boastful to say that I have studied the Bible as much as any layman. And I have tried to live according to its precepts.

DRUMMOND: Bully for you. Now, I suppose you can quote me chapter and verse right straight through the King James Version, can’t you?

BRADY: There are many portions of the Holy Bible that I have committed to memory. (DRUMMOND crosses to counsel table and picks up a copy of Darwin.)

DRUMMOND: I don’t suppose you’ve memorized many passages from the Origin of Species?

BRADY: I am not in the least interested in the pagan hypotheses of that book.

DRUMMOND: Never read it?

BRADY: And I never will.

DRUMMOND: Then how in perdition do you have the gall to whoop up this holy war against something you don’t know anything about? How can you be so sure that the body of scientific knowledge systematized in the writings of Charles Darwin is, in any way, irreconcilable with the spirit of the Book of Genesis?

BRADY: Would you state that question again, please?

DRUMMOND: (Not angrily) All right. I get the scent in the wind. (He tosses the volume of Darwin on the counsel table) We’ll play in your ball park, Colonel. (He searches for a copy of the Bibl,. Without opening it, DRUMMOND scrutinizes the binding from several angles) Now let’s get this straight. Let’s get it clear. This is the book that you’re an expert on? (BRADY is annoyed at DRUMMOND’S elementary attitude and condescension.)

BRADY: That is correct.

DRUMMOND: Now tell me. Do you feel that every word that’s written in this book should be taken literally?

BRADY: Everything in the Bible should be accepted, exactly as it is given there.

DRUMMOND: I recollect a story about Joshua, making the sun stand still. Now as an expert, you tell me that as true as the Jonah business. Right? (BRADY nods, blandly) That’s a pretty neat trick. You suppose Houdini could do it?

BRADY: I do not question or scoff at the miracles of the Lord- as do ye of little faith.

DRUMMOND: If they say that the sun stood still, they must’ve had a notion that the sun moves around the earth. Think that’s the way of things? Or don’t you believe the earth moves around the sun?

BRADY: I have faith in the Bible! (Doggedly) The sun stopped.

DRUMMOND: Good. (Level and direct.) Now if what you say actually happened- if Joshua halted the sun in the sky- that means the earth stopped spinning on its axis; continents toppled over each other, mountains flew out into space. And the earth, arrested in its orbit, shriveled to a cinder and crashed into the sun. (Turning) How come they missed this tidbit of news?

BRADY: They missed it because it didn’t happen.

DRUMMOND: It must’ve happened! According to natural law. Or don’t you believe in natural law, Colonel? Would you like to ban Copernicus from the classroom, along with Charles Darwin? Pass a law to wipe out all the scientific development since Joshua? Revelations- period!

BRADY: (Calmly, as if instructing a child) Natural law was born in the mind of the Heavenly Father. He can change it, cancel it, use it as He pleases. It constantly amazes me that you apostles of science, for all your supposed wisdom, fail to grasp this simple fact. (DRUMMOND flips a few pages in the Bible.) The Bible satisfies me, it is enough.

DRUMMOND: It frightens me to imagine the state of learning in this world if everyone had your driving curiosity. (DRUMMOND is still probing for a weakness in Goliath’s armor. He thumbs a few pages in the Bible.) The book goes into a lot of “begats.” (He reads) “And Aphraxad begat Salah; and Salah begat Eber” and so on and so on. These pretty important folks?

BRADY: They are the generations of the holy men and women of the Bible.

DRUMMOND: Did people “begat” in those days about the same way they get themselves “begat” today?

BRADY: The process is about the same. I don’t think your scientists have improved it any.

DRUMMOND: In other words, these folks were conceived and brought forth through the normal biological function known as sex. What do you think of sex, Colonel Brady? I’m not asking what you think of sex as a father, or as a husband. You’re up here as an expert on the Bible. What’s the Biblical evaluation of sex?

BRADY: It is considered “Original Sin.”

DRUMMOND: (With mock amazement) And all these holy people got themselves “begat” through “Original Sin”? (BRADY does not answer. He scowls, and shifts his weight in his chair.) All this sinning make ‘em any less holy?

BRADY: (With dignity) Your Honor, I am willing to sit here and endure Mr. Drummond’s sneering and his disrespect. For he is pleading the case of the prosecution by his contempt for all that is holy.

DRUMMOND: I object, I object, I object.

BRADY: On what grounds? Is it possible that something is holy to the celebrated agnostic?

DRUMMOND: Yes! (His voice drops, intensely) The individual human mind. In a child’s power to master the multiplication table there is more sanctity than in all your shouted “Amens!”, “Holy, Holies!” and “Hosannahs!” An idea is a greater monument than a cathedral. And the advance of man’s knowledge is more of a miracle than any sticks turned to snakes, or the parting of waters! But are we now to halt the march of progress because Mr. Brady frightens us with a fable? (Thoughtfully, seeming to look beyond the courtroom) Darwin moved us forward to a hilltop, where we can look back and see the way from which we came. But for this view, this insight, this knowledge, we must abandon our faith in the pleasant poetry of Genesis.

BRADY: We must not abandon faith! Faith is the important thing!

DRUMMOND: Then why did God plague us with the power to think? Mr. Brady, why do you deny the one faculty which lifts man above all other creatures of the earth: the power of his brain to reason. What other merits have we? The elephant is larger, the horse is stronger and swifter, the butterfly is more beautiful, the mosquito more prolific, even the simple sponge is more durable!

(Wheeling on BRADY) Or does a sponge think?

BRADY: If the Lord wishes a sponge to think, it thinks.

DRUMMOND: Does a man have the same privileges that a sponge does?

BRADY: Of course.

DRUMMOND: (Roaring for the first time: stretching his arm towards CATES – his client) This man wishes to be accorded the same privilege as a sponge! He wishes to think!

BRADY: But your client is wrong! He is deluded! He has lost his way!

DRUMMOND: It’s sad that we aren’t all gifted with your positive knowledge of Right and Wrong, Mr. Brady.

(DRUMMOND strides to one of the uncalled witnesses seated behind him and takes from him a rock, about the size of a tennis ball. DRUMMOND weighs the rock in his hand as he saunters back toward BRADY)

DRUMMOND: How old do you think this rock is?

BRADY: (Intoning) I am more interested in the Rock of Ages, than I am in the Age of Rocks.

DRUMMOND: Dr. Page of Oberlin College tells me that this rock is at least ten million years old. (DRUMMOND opens up the rock, which splits into two halves. He shows it to BRADY) Look, Mr. Brady. These are the fossil remains of a pre-historic marine creature, which was found in this very county- and which lived here millions of years ago, when these very mountain ranges were submerged in water.

BRADY: I know. The Bible gives a fine account of the flood. But your professor is a little mixed up on his dates. That rock is not more than six thousand years old.

DRUMMOND: How do you know?

BRADY: A fine Biblical scholar, Bishop Usher, has determined for us the exact date and hour of the Creation. It occurred in the year 4004 B.C.

DRUMMOND: That’s Bishop Usher’s opinion.

BRADY: It is not an opinion. It is a literal fact, which the good Bishop arrived at through careful computation of the ages of the prophets as set down in the Old Testament. In fact, he determined that the Lord began the Creation on the 23rd of October in the Year 4004 B.C. at- uh, at 9 A.M.!

DRUMMOND: That Eastern Standard Time? Or Rocky Mountain Time? It wasn’t daylight-saving time, was it? Because the Lord didn’t make the sun until the fourth day!

BRADY: (Fidgeting) That is correct.

DRUMMOND: (Sharply) The first day. Was it a twenty-four-hour day?

BRADY: The Bible says it was a day.

DRUMMOND: There wasn’t any sun. How do you know how long it was? A normal day, a literal day, a twenty-four-hour day? (Pause. BRADY is unsure.)

BRADY: I do not know.

DRUMMOND: Isn’t it possible that first day was twenty-five hours long? There was no way to measure it, no way to tell! Could it have been twenty-five hours?

BRADY: (Hesitates- then) It is . . . possible . . .

(DRUMMOND’S got him. And he knows it! This is the turning point. From here on, the tempo mounts. DRUMMOND is now fully in the driver’s seat. He pounds his questions faster and faster.)

DRUMMOND: Oh. You interpret that the first day recorded in the Book of Genesis could be of indeterminate length. It could have been thirty hours! Or a month! Or a year! Or a hundred years! (He brandishes the rock underneath BRADY’S nose) Or ten million years!

(Both BRADY and DRUMMOND crane forward, hurling their answers not at the court, but at each other.)

BRADY: [You] want to destroy everybody’s belief in the Bible, and in God!

DRUMMOND: You know that’s not true. I’m trying to stop you bigots and ignoramuses from controlling the education of the United States! And you know it!

BRADY: How dare you attack the Bible?

DRUMMOND: The Bible is a book. A good book. But it’s not the only book.

BRADY: It is the revealed word of the Almighty. God spake to the men who wrote the Bible.

DRUMMOND: And how do you know that God didn’t “spake” to Charles Darwin?

BRADY: I know because God tells me to oppose the evil teachings of that man.

DRUMMOND: Oh. God speaks to you.

BRADY: Yes.

DRUMMOND: He tells you exactly what’s right and what’s wrong? And you act accordingly?

BRADY: Yes.

DRUMMOND: So you, Matthew Harrison Brady, through oratory, legislation, or whatever, pass along God’s orders to the rest of the world! Gentlemen, meet the “Prophet from Nebraska!”

BRADY: (Almost inarticulate) Please-!

DRUMMOND: (With increasing tempo, closing in) Is that the way of things? God tells Brady what is good! To be against Brady is to be against God!

BRADY: (Confused) No, no! Each man is a free agent-

DRUMMOND: Then what is Bertram Cates doing in the Hillsboro jail? Suppose Mr. Cates had enough influence and lung power to railroad through the State Legislature a law that only Darwin should be taught in the schools!

BRADY: Ridiculous, ridiculous! There is only one great Truth in the world-

DRUMMOND: The Gospel according to Brady! God speaks to Brady, and Brady tells the world! Brady, Brady, Brady, Almighty! (DRUMMOND bows grandly).

BRADY: The Lord is my strength-

DRUMMOND: What if a lesser human being- a Cates, or a Darwin- has the audacity to think that God might whisper to him? That an un-Brady thought might still be holy? Must men go to prison because they are at odds with the self-appointed prophet?

(BRADY is now trembling so that it is impossible for him to speak. He rises, towering above his tormentor- rather like a clumsy, lumbering bear that is baited by an agile dog)

DRUMMOND: Extend the Testaments! Let us have a Book of Brady! We shall hex the Pentateuch, and slip you in neatly between Numbers and Deuteronomy!

BRADY: (Reaching for a sympathetic ear, trying to find the loyal audience which has slipped away from him) My friends- Your Honor- My Followers- Ladies and Gentlemen

DRUMMOND: The witness is excused.

BRADY: (Unheeding) All of you know what I stand for! What I believe! I believe, I believe in the truth of the Book of Genesis! (Beginning to chant) Exodus, Leviticus, Numbers, Deuteronomy, Joshua, Judges, Ruth, First Samuel, Second Samuel, First Kings, Second Kings-

DRUMMOND: Your Honor, this completes the testimony. The witness is excused!
```

---

## IC-0389: Inside Al

- Title: Inside Al
- Author (byline): David S. Baker
- Work: High School Plays: A Collection of Three One-Act Plays
- Publisher: Samuel French, Inc.
- Publication date as stated: 1989
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: AL, INSIDE AL, JASON, BETH, AL/INSIDE AL
- Teaser before the introduction: Yes
- Spoken words (computed): 1352
- Already set (do not supply): none

### Source block (context only)

```text
Author: David S. Baker
Book: High School Plays: A Collection of Three One-Act Plays
ISBN: 978-0573622298
Publisher: Samuel French, Inc.
Date (Month/Year): 1989
```

### Introduction (context only: never use it for content warnings)

```text
There are about 764,000 people in the United States with cerebral palsy. In many cases, people with cerebral palsy are labeled as mentally retarded because they are not able to effectively communicate with the outside world. Their true being is locked inside a body that simply won’t work they way they want it to. Such is the case of Alvin Theodore Willson – a 39 year old victim of cerebral palsy. Inside Al by David S. Baker gives a voice to those too often silenced by the disease and shows that regardless of our outward appearances . . it is our soul that makes us who we are. Inside Al by David S. Baker
```

### Performance text (classify this)

```text
AL: He is the outside Al, the body. He is a 39-year old victim of cerebral palsy. His speech is slow and sometimes hard to understand, especially when he is upset or excited.

INSIDE AL: He is Al’s mind and feelings. He is perceptive, blunt and sometimes bitter. His speech is extremely articulate and fluid.

JASON: Average 16-year old boy

BETH: Insecure, frightened child of 16 who hides her fear by using and abusing those she comes in contact with. She manipulates all of her relationships and takes advantage of anyone who is weak-willed enough to let her.

(Al walks stiffly onstage. Inside Al is behind and slightly to one side of him moving with him in perfect synchronization. Al and Inside Al speak sometimes together and sometimes alternatively, but the feel is that the words are coming from the same person, even if from different mouths – the feel is still that of a monologue)

NOTE: Inside Al should assume the body position of AL before he speaks each line and then “morph” out of the crippled body into the character of Al’s mind and feelings

AL/INSIDE AL: (Simultaneously) Hi. I’m Al. Alvin Theodore Willson (They chuckle)

INSIDE AL: . . . Always makes me think of the Chipmunks.

AL: People stay away from me, mostly. I have cerebral palsy.

INSIDE AL: Sometimes, though, I feel like I have leprosy or something. They stare at me or say I’m dumb – retarded. I’m not, though.

AL: My mind tells my body to do things, and my body doesn’t cooperate very well . . . but I’m not dumb.

AL/INSIDE AL: They don’t know me.

INSIDE AL: When I walk to the market, people smile and wave at me as they go by. I know that as soon as they pass, they quit smiling. They stop and think.

AL: (Mocking himself) “Oh, look at poor old Al, he’s so slow and dumb and . . .”

INSIDE AL: . . . I could just scream! They pity me. If there’s one thing in this world I hate the most, it’s pity. I hate charity, too, except real charity.

AL: Why can’t someone be nice to me just to be nice to another human being? Why can’t people look past my body (Al points at Inside Al)

INSIDE AL: . . . and see my soul?

JASON: When my teacher first told us about the “be nice to someone” project, I groaned. I hate this type of assignment. (Beat) I decided to help Al Willson for several reasons. He’s a real friendly guy - always waves at us when we pass him on his way to the market. I don’t think Mr. Willson has any family – never seen any anyway. Most people just ignore him, or barely accept him. I heard a bunch of kids at school once, talking about him; they called him the “village idiot.” (Beat) Anyway, on my way home from school, the day the assignment was given, I checked the back yard of Al’s little flat. I was lucky. It hadn’t been mowed for months.

(Jason exits and reenters, bringing a push mower and a rake. He puts on his hat and shade, one at a time, and takes headphones from around his neck and puts them on. He flips his collar up and grabbing the mower, he makes passes to simulate mowing. Then stops mowing and picks up rake – Uses it as an Air Guitar and dances to the music he’s listening to on his headphones).

AL: (To audience) And I thought I moved funny!

JASON: Uh . . . hi. I did your lawn. What do you think?

AL: It looks real good.

JASON: Anything else I should do for you?

AL: No (Al reaches into his pocket and brings out a worn dollar bill and some small change)

JASON: (narrates action to audience) He tried to pay me, but I told him I wasn’t supposed to take payment. (Al reaches into his pocket again hands something to Jason and then steps back) It was a little ceramic frog. Al made it himself – I could tell. (Al waits patiently). It was a nice gesture, anyway. I thanked him, took my rake and my mower, and left. (All exit)

(SCENE)

BETH: I decided [to] be nice to Al Willson. (pauses then continues explaining) That cripple. You know, that guy who wanders around all the time wearing those jumpsuits and that blue baseball hat. He has a problem, that’s for sure.

(She giggles, pulls a face and imitates Al’s speech) Hello, little kiddies! . . . . Heh, heh . . . Want to pay some games? (moves over in front of an imaginary mirror and begins examining herself) Anyway, since everybody likes cookies, I figure [I] can bake some for him, take them to his house and then get my parents to sign that “be nice to someone” form.

(SCENE – Al’s front porch - (Beth enters and begins to leave some home-made cookies on the doorstep when Al comes out and surprises her

BETH: Oh . . . hi, Mr. Willson. [I] came to bring you these cookies. [I] , ah, made them for you. (Al stands looking at them; he appears confused) (Louder) [I] brought you these cookies. They’re almond cookies. [I] thought you might like to have some.

INSIDE AL: (Loudly and slowly) I’m not deaf; I have cerebral palsy.

AL: Is this for your project? (Actor 2 can do this line as AL)

BETH: How did you know about this project?

AL: A boy named Jason mowed my back lawn. (Actor 2 can do this line as AL)

INSIDE AL: (Cynically) He beat you to the cripple.

BETH: (under her breath) Why , that idiotic little son of a . . . (To Al) Well, [I] have to go. See you around, Mr. Willson. ‘Bye (turns and leaves)

INSIDE AL: (follows circling around her, yelling at her. He almost seems to be dancing) Oh, please don’t. I’d really rather you didn’t see me around. Tell you what. Instead of seeing me around, could you go jump out of a window?

(SCENE)

AL: I’ve noticed something about people: most of them don’t look me in the eye. They look past me, or around, or at each other, but they never look at me.

INSIDE AL: I think they are afraid to see my body, to accept the fact that I am handicapped. They would rather think that it is all mental – that’s much easier for them to accept. (Pauses) Once, I was on the porch watching the kids play. Some little boys came up to me and I asked them if they wanted to hear a story. I’m very good with stories.

AL: One of them called out. “Retard, retard!” and the rest walked around with stiff joints, making fun of me, of course. I wanted to wring their grubby, little necks – all of them! But I couldn’t. I just sat there and . . . “

INSIDE AL: Why didn’t you ever get mad at them?! Quit being such a wimp and do something for a change! You let everybody walk all over you. You’re a person too, why don’t you show them that? Why don’t you ever ACT LIKE A HUMAN! (Imitates Al’s movement and speech) Look at me. I’m a poor, helpless cripple. I can’t walk or talk or do anything.

AL: People always feel sorry for me and that make me mad but

AL/INSIDE AL: I never say anything. (Jason enters and startles Al)

JASON: Mr. Willson? Can I talk to you a second? The reason I came by is to apologize to you.

AL: For mowing my lawn?

JASON: No, no. For . . . well . . .for hurting your feelings. I treated you like a project . . .not a person and I’m sorry.

INSIDE AL: Don’t do this. It’s easier for me to hate you. Don’t make me like you. (Al can do this line)

AL: There is no need . . .

JASON: I really feel bad about this. Please. Maybe you’re used to having this happen to you, but I think that you shouldn’t have to be use to it. People can be so cruel!

AL: Yeah, tell me about it. Just your coming here helps a litte.

INSIDE AL: (to Al) It’s forgiven?

AL: (to Inside Al) It’s forgiven.

(Scene)

BETH: I made the cookies. . .. why does it matter that [Jason and I] were nice to the same cripple? (crosses to Al’s porch) (Bluntly) Hello, Mr. Willson. I came to find out why you didn’t accept y kindness.

INSIDE AL: KINDNESS?? If that was kindness, I’d really hate to see cruelty. What I didn’t accept was your pity.

BETH: (as if there was not response) Did my teacher call you? What did you tell her?

AL: That you brought me cookies (Inside AL can do this line)

BETH: Didn’t you enjoy my cookies?

INSIDE AL: Well, no. They were soggy, greasy and had little pockets of baking soda in them (makes a face at the audience). Frankly, they were the worst cookies I have ever tasted.

AL: Yes, but . . .

BETH: (intimidating) If you liked them so much, then why did you tell my teacher that my project wasn’t good enough? You ruined my grade! (Jason enters)

JASON: (to Beth) What are you doing here? (To Al) Is she harassing you?! (To Beth) What’s your major maladjustment anyway?

BETH: Well, this gimp told the teacher not to give me credit for my project.

JASON: Wait a minute. What exactly do you mean, “project.?” You’re telling me that this man is your project?

BETH: Yeah, stupid (laughs) Now who has the brain problem?

JASON: Do you think Al does?

BETH: (Mocking AL’s speech) Oh, there’s nothing wrong with him. Nothing at all. . .

INSIDE AL: (speaking to the audience, as if they are all that will listen) You know, it’s times like these that I’d really like to knock her head off.

JASON: You really think he’s retarded, don’t you? Oh, you poor child. You’re so confused. He’s got cerebral palsy, not ‘stupidity syndrome.” His body is slow, not his brain.

AL: Both of you – please leave. Leave me alone.

INSIDE AL: Well, get out of here! I don’t’ need rescuers, and I don’t need accusations. I don’t need any of you. I wish your stupid teacher had neer given this asinine project in the first place. You’re hypocrites – all of you! One “being kind to me” and the other “protecting the poor, helpless retard.” I wish you would all just

AL: . . . GO AWAY

(Scene)

JASON: I was trying to defend Al – to help him. Beth just kept going at his throat and I thought he needed me. I figured he couldn’t handle her all by himself. Thing is, I guess he didn’t want to be defended. I made him feel helpless.

Handicapped (he cringes). I don’t know. Maybe it’s not the charity, but the way it’s given . . . You have to drop the pity.
```

---

## IC-0390: Iphigenia in Orem

- Title: Iphigenia in Orem
- Author (byline): Neil LaBute
- Work: Bash: Latterday Plays
- Publisher: Overlook Press
- Publication date as stated: Dec 1999
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: YOUNG MAN
- Teaser before the introduction: Yes
- Spoken words (computed): 2502
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil LaBute
Book: Bash: Latterday Plays
ISBN: 978-1585670246
Publisher: Overlook Press
Date(Month/Year): Dec 1999
```

### Introduction (context only: never use it for content warnings)

```text
Iphigenia in Orem by Neil LaBute
```

### Performance text (classify this)

```text
YOUNG MAN:

I'll tell it once. One time because it deserves to be told, and then never again. Fair enough? So...where should I...let me see. Alright.

I never used to travel. Never cared much for driving all the time, meeting clients, that end of things...I mean, I did it when I first started, low man on the pole and whatever, but once I got the old MBA, foot in the door and all...I stuck to the desk as much as I could. I like it. That office...I don't know..."feel." The atmosphere. Faxes coming in, people zipping around, emergency strategy sessions, all that. It's like being a kid again, playing at "war" or that type of thing. You can just see what guys love about it. And I don't mean just guys either, because there's plenty of women in the field, too, obviously, but I mean "guys" like in...well, "guys." You know, how it's used these days. All encompassing. It's very high stakes, lots of cash floating around you, and the pressure's a real...well, just hot. Day in and day out. Seriously. It is. We may play it like a game sometimes, but believe me, a day doesn't go by in business that you're not out for somebody's blood.

I'll try and be...brief--things took a bit of a turn for us last year. My wife and me, the family, you know...we lost a child. Newborn. Well, five months old...just like that. Just happened. (BEAT) I was off that day, a Friday, I think, and Deborah, that's my wife, Deb, she was out--her mother was staying with us, and they were over at the safeway getting some milk--deb put the baby down, "Emma" we'd named her, she put Emma in our bed because that's where she'd been sleeping the first few months...we always thought that was a good bonding thing, I'd read it somewhere, or she heard it at relief society or something like that...anyway, so that's what she did. She tucks her in, and out they went. And see, I was gonna lie down with her, I really was, but I just went back to the living room for a second, watch a little wheel of fortune or something, you know, five minutes a week to myself. And I fell. Fell off to sleep right there, there on the loveseat by the window. (BEAT) Deb's mom...Emma's grandma...found her. Maybe a half hour later. She'd smothered herself under the covers, I don't know, beneath the weight of the comforter or whatever it was.

The little thing...died in our bed, tangling herself in the blankets. (BEAT) The police had to come, they do for any kind of infant death, that' what the officer said; I'd gotten a hold of myself by that time, still crying, but Deb...Deb was just kind of sitting there next to me, staring off, and this guy--this person-a detective, I suppose, was asking us questions. Standing there and firing off this series of questions. "Standard procedure," he assured us, but still... PAUSE What bothered him...no, "puzzled" him, he said, never came right out and said it bothered him but you could see by the way he...he didn't understand how the baby could get so far down. (BEAT) It seemed to him that the baby, a baby that young and small, was too far down toward the foot of the bed, and turned. Something about that seemed to be eating at him. I didn't understand what he was getting at, the way he kept going back and forth over the events and times and all that, "where were you standing?" and "approximately how long were you...?" blah blah blah. I mean, my god, we're sitting there on the edge of the sofa, the bed my daughter just died in I can see through an open door back down the hallway and this man is pacing around, sucking on the end of the chewed cap of a ballpoint pen and...asking me quietly, "did you check on her?" (BEAT) What's he getting at, anyway? I mean, that's a no-win, isn't it? Think about it...if I didn't check on her, I'm not a good father. And if I did go in there, if I had've done what I was supposed to do, had planned on doing, the nap...then maybe she'd be alive. (BEAT). And for just a second, just the briefest of moments...I catch Deb looking over at me. As if this is the first time the thought's come to her as well. This possibility. The whole incident hangs there--probably only two or three seconds all together-- but it just lays there in the air over us all. "Umm, no, I didn't. I meant to, but..." and off he goes. Says, "Fine." Stops me cold, and off he goes onto another tangent. PAUSE And finally they were gone. I looked around, and the front door slammed shut and it was empty. The house. They'd taken Emma out with them, the coroner, maybe a half hour before, wrapped in a little zip-up bag, something like what I carry my pressed shirts in when I travel. Emma was gone, and we ate dinner...we may have even ordered out that night; that probably sounds horrible, but Deb just couldn't stand over the stove right then, so it seems like we had pizza...and went to bed right after. (BEAT) The phone woke me about 11:30. I almost had to pry Deb's fingers off of mine to get it, but I was on by about the fourth ring. It was him. The police detective and very apologetic about calling so late, and the whole process and the usual stuff that you'd see on any of those cop programs on tv. (BEAT)

It'd all come out fine, he said, ruled "natural causes" after a few tests'd been run and he just wanted to let us know and if there was anything he could do he'd be glad to...I hung up without him finishing. He'd put us through enough that day. I hung up the receiver and just rolled back over to Deb. I just held her at first...putting my hand back in place and squeezing her fingers a bit. But it woke her. SHe woke up and we whispered to each other...talking under the sheet about things we hadn't mentioned in years! We were under the sheets, just them, because from that night on, Deb and I could never sleep with blankets on that bed again. (BEAT) Anyhow the talking must've gone on for hours, a few at least and then kissing and finally...we did what you'd imagine on a night like that, a moment when your entire universe has been changed forever. (BEAT) I don't know, but that may have even been the night that joe was...that's our youngest, "Joseph,"...so Joe came almost exactly nine months later. He's a great boy, he really is. ANd over time, with the new child...life goes on.

And that's what we did. We went on...and more than that. A lot more. But...all right. Ummm...there was a problem. That's what had started all this, I mean, originally. Started it all in motion...a problem at work. We'd been taken over recently, I mean, no big deal in theory, happened all the time, somebody else takes over, you lose a few of the stragglers, guys who couldn't keep up. (BEAT) So that was the story.

Four of us were going to go, three of which I and everyone else had a pretty good idea of, three that should've gone a long time ago, but that last spot...that was the one. The tough call. There was me, who'd been steady and strong and average, you know, just average or slightly above, someone that they could count on, good sense of humor and everything for the past seven years. Well liked and I liked everyone. Or, most everyone. There was this woman, a few years younger than me and had come in during a wave of new hires about four years back...just plain vicious. We'd gotten off badly...actually I'd made a mistake once, a board meeting where I'd grouped her in with a "you guys oughta..." meaning that side of the table and she called me out on it. First meeting, maybe second she'd been to and she nails me out loud about my attitude, my limited "chauvinist lexicon" and all this other, just crap that she fired off. (BEAT) But she was one. Me, and her, because of the short time she'd been there, and a couple of other folks that had about the same seniority that I did...and that's what hung over our heads, each of us, day after day as we'd go into work.

I got the call just before Deb had gone to Safeway. Took it inthe den because it was coming from Chicago...friend of mine, at the home office, a guy from school actually, with a tip. A tip he'd heard that day and wanted to call me with it...it was me. I was the one that would make up the four, and he was so sorry and all that-- he's a really good guy, I see him whenever I'm in Chicago, we were these really big jokers when we were at the "u" in the dorms together and so he was just doing what any guy would do, he said, letting me hear it from a friendly voiec, and giving me a jump, the weekend, anyway. Before he hung up he said again it was just what was going around, but he thought I should know...(BEAT)

What was I gonna do? How could I possibly keep it all going, the lifestyle we'd made for ourselves, without my seniority, the benefit package...jobs all over being tight like they are? It just wouldn't be possible. (BEAT) It was like that moment in the film Kramer vs. Kramer, you know, where he decides he's got to get a job that day, right? I'm standing there, just taking in the DVD player, and our big screen tv, and one of the kids' bikes, I can see through the front window, the Land Rover, Wheel of Fortune's blasting on the TV in the family room...all these thoughts are swirling around in my head. And I hear it. (BEAT) I wasn't asleep...I couldn't have been, I mean I've tried to beleive it, make myself believe it, too, but I wasn't, or I never would've heard her. The baby, Emma, in the other room. As I was standing there I heard her cry out from inside the bedroom. I did...(BEAT) When I got to the doorway she was already under the blankets, she was, I swear, under them and fighting to get out. I rushed in there, to the edge of the carpet at the bedroom door and then, I don't know, something stopped me. Just stopped me like some invisible force had reached out and took hold of the back of my shirt and yanked me to a halt...I looked in at her again, this little yelp kind of coming up from her as she blundered around in there. This little...mound wandering around in there. It was nearly absurd, to walk in on something like this, I mean, you just could never be ready for a thing like this, and because of that, that specific part of it, the unreality...I was able to make the decision.

In that moment, standing there watching my daughter fight for her life, I made my decision. Well, when I looked at it, I mean, rationally, for even half-a-second there in the hallway, I realized that's what this was. An opportunity. And I wasn't going to waste it. (BEAT) So I--I'm just gonna say this, because it's a little...so. I went into the room and stood there by the bed, I stood there and pulled up the comforter by one corner and I saw her then. Her little fine sandy hair and her...I just kind of coaxed her down a bit. Down a bit further with the edge of my foot, turned her a touch and down and then I dropped the covers back and walked out...there was one last little sound Emma made, you could barely hear it. But I just kept walking, back out to the loveseat, there in the family room, and layed down and made myself go to sleep.

PAUSE

I kept my job. I did. And guess who was the one. I mean, after all that, guess who got it right between the eyes? (BEAT) I even walked her to the elevator the day she left, her and the other three, this was several months after all the other...I was right behind them with a "so long" and "we'll miss you" and right then, it came to me, it came to me with my friends standing around and that little...well, she wasn't looking so strong anymore, there in the open car, this box of stuff in her hands. As the doors were closing I said to them all, but staring straight at her, I said, "you guys take care now!" PAUSE

I was at a seminar, big yearly thing the company put on. This one was in Boston, six months back. My friend from Chicago flew in for it. Okay, so...after the morning session, just in passing as we were both in the restroom at one point, he said something to me, my friend, I guess trying to lighten things up a little, he mentioned work. And about the layoffs, and how glad I must've finally been to have gotten rid of you know who. And then he said, "Boy, I really had you going that Friday, didn't I?" I turned to him, standing there at the urinal, my fly still open and I turned to him and the whole picture was clear to me. Right then, it was as clear as a look in the future. What he'd done. What we always used to do to each other. See, he'd heard the real truth about what was coming and just couldn't let it go without a little razzing and so he'd given me the call, let me stew about it over the weekend. He was going to buzz me back Monday morning with the truth. But by then...

The point I want to make is that it didn't have to happen that way. I took this risk, this calculated risk for my family, that this whole episode would play out in our favor, give me that little edge at work and maybe things'd be okay, or they'd change their minds because of, you know... Who knows. It happened, and you go on. Like I said before, you just go on.
```

---

## IC-0391: Jails, Hospitals and Hip-Hop

- Title: Jails, Hospitals and Hip-Hop
- Author (byline): Danny Hoch
- Work: Not specified
- Publisher: Villard Books
- Publication date as stated: Oct 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1855
- Already set (do not supply): none

### Source block (context only)

```text
Author: Danny Hoch
ISBN: 978-0375753398
Publisher: Villard Books
Date (Month/Year): Oct 1998
```

### Introduction (context only: never use it for content warnings)

```text
Illegal street vending is a serious problem affecting many cities around the world and has also proved to be a challenge for municipal authorities the world over, despite the enactment of legislation outlawing this practice. From the African American peddlers of the 1860s to the Italian and Jewish merchants of the 1920s, street vending is deeply rooted our country’s culture and history. Street vending continues to offer a viable source of income, particularly for immigrants without work permits. Some have estimated that hundreds of millions of dollars worth of goods are sold on city streets annually. Prosecuting street vendors is difficult if not impossible to accomplish – However, in this selection that very event has taken place. Meet Bronx, a pale-skinned sidewalk vendor busted for selling O. J. Simpson T-shirts without a license who enrages a policeman who can't figure out what race he is. Jails, Hospitals and Hip-Hop by Danny Hoch.
```

### Performance text (classify this)

```text
A man in his mid-twenties loiters in a hallway of the C-74 building on Riker's Island, New York City. He conversates with a new inmate.

. . . . . . Really? That's messed up, man. I hear you .... Yeah . Wow. Hey yo, do me a favor? Take a walk with me for one second? I gotta get a toothbrush. Just take a walk with me to get a toothbrush for one second. (They walk) But for real, man, if I was you, I would talk to your lawyer and tell him that you wanna plea-bargain. 'Cause even though you was just an accomplice, if you plead not guilty, and it goes to trial, they could decide to make it a first-degree felony against you, and that's it. I'm sayin', whatever, even if you not an accomplice, whatever, bee, I wasn't there, I ain't sayin' you did nothin', man. I mean, I just met you yesterday. But, especially 'cause you're black ... I mean ... are you black? Oh, I wasn't sure, I thought you might be, whatever. Still, just plead guilty, guilty, guilty. I seen it happen before. Even if you didn't do it. Otherwise they start makin' deals with all your peoples, make it look like you're the one that pioneered the whole *thing*. Then they get you for conspiracy when you was just an accomplice-or you just happened to be there, like I said I wasn't there, I ain't sayin' you did nothin'. (He calls an officer) On the gate! On the gate! Officer on the gate! ...... Nah, to inmate services-for a toothbrush, they took his toothbrush in the dorm. Right? Right, they took your toothbrush in the dorm? They took his toothbrush in the dorm! That's my ID card right there. Show him your ID card, pal. So we'll wait right here then. Where we going? Right?

(Back to the guy) I'm tellin' you, if I was you, I would just say guilty, take the bid, do your little one-to-three, whatever, politic, you know. Me, I got different problems, man. See, I try to do the right thing, they lock me up. Giuliani's like, "Oh, people on welfare are lazy." I'm tryin' not to be on that. I'm workin', right? I'm in Fordham Road. I'm sellin' Bart Simpson T-shirts, and um, what you call it-O.J. Simpson T-shirts, right? This cop come up, arrest me 'cause I don't got a license. I'm not selling drugs! I'm not selling drugs! I'm selling Bart Simpson T-shirts, O.J. Simpson T-shirts. That's work, man. You think that it is easy? It is hard, man, I don't even wanna go into it . . . Nah, but that's illegal? They said it's illegal. You know, I'm tryin' to do right in my life, man. I wanna be a entrepreneur, or whatever you call it. You know if I was that little girl that they show on TV in that commercial selling lemonade in front of her house, you think the cop gonna arrest her? Nah-ah! Nah-ah! But see, if you think about it, the little girl, she's a entrepreneur, just like me. She's a businesswoman. She got-what you call it?- Overhead. She gotta get her sugar, her lemons, her cups, she makes her stand, then she stand outside all day. Me? I got my shirts, my stand, I stand outside all day. But you know if that cop see her in front of her house with her little white picket fence or whatever, he'd be like, "Oh ... " -all jolly -"that's so cute, lemme get a lemonade, sweetheart?" Right? And then he'd drink his lemonade and then he'd say, "Mm, tasty ... whatever, whatever." Then he leave. Then he go beat up some people. Then he go home and feel like, it's not really such a bad day today. God bless America, right? But he see me in Fordham Road? Nahah, different story. He step to me, "Hey you! Where's your license?" He gonna say, "Where's your license?" to the little girl? Nah-ah! Nah-ah! See, what is it, he don't care if I got a license, or I don't got a license. He don't like the way I look. I live in 163rd Street, I got a certain look. People in Park Avenue, they got a certain look. But the cop gonna see somebody from Park Avenue or Tribeca, hauling three kilos of cocaine to their girlfriend's house, on their designer rollerblades or whatever, he's not gonna get disturbed by their look. He'll say, "Hey, how are you? Have a doughnut. Okey-dokey, buddy." Or whatever. But then he see somebody that appears-I don't even know-unprofessional, or whatever, he automatic think criminal.

So this cop, he gets out the car all with his cop *crap*. But see, he had sunglasses, so when he look at me first from the car, I look darker. When he get out, he like-"Uht, uht." He get confused. 'Cause if you put me next to the cop, I'm whiter than the cop. He start askin' me, "What are you? What are you?" I say, "That's not your business, you wanna buy a shirt?" Then he knock over all my *stuff* in the street, the shirts is dirty. Now I have dirty products. I have to pay for that. And peoples is laughin' at me, man.

Next thing, he throw me down in the ground, he got his nightstick in my back, with the spit and the gum from the sidewalk is in my face. He say, "What are you, what are you?!! Are you Puerto Rican, are you Puerto Rican?" I say, "Nah, I'm not Puerto Rican yo, I'm selling Bart Simpson, O. J. Simpson T-shirts, what's the problem officer?" But see, he wanna know, what am I? I mean, my color is white like Bill Clinton, but that's not good enough for him, you know, in the way that I'm speaking, or I don't even know. He got a complex, he needs to see a therapist 'cause he's confused. Then, he look at the T-shirts, and he get more confused. 'Cause he don't know who's Bart Simpson. He knows Bart Simpson is Bart Simpson, but he don't know Bart Simpson is Dominican, Jewish, Greek, Puerto Rican? What is he? He don't know, but he know that Bart Simpson and O. J. Simpson make more money than him, so he feel threatened. Then the cop look at me, and he see somebody that's a entrepreneur, that's trying to start a business from nothing. He see that I have the possibility to better my situation. That I have the opportunity to increase my status, or whatever you call it. And then he looks at himself, and he sees that he's just a servant and that's it. Even if he turn captain, lieutenant, police chief, whatever, he's just a servant and that's all he gonna be ... So he feel threatened. And 'cause he feel threaten, that day he gonna decide capitalism is illegal. And 'cause I got a prior felony on my record, they put me in here. (To another guy) You got a cigarette?

(Back to guy number one) See, if you analyze it with the little girl and the lemonade, that's supposed to be America, right? That you could stand outside your house and sell whatever. If that's not true that you could do that, don't advertise it then. Don't put it in the TV, you know? To be honest with you, I seen that commercial, I got inspired by that. I said yo, *it* ain't really that bad, I got chances. Now I'm in jail, bro. I feel like suing them lemonade *freaks*, man. Or suing somebody for false advertising. I know I wasn't selling lemonade, that's not the-Hey yo, shut up, bro. I didn't really ask you to respond. (To another guy) You got a light?

(Back to guy number one) Nah, they arrested me a month ago, I ain't even had a hearing, nothing. First they had me in C-73, I was there for two weeks, but I got in a fight, this guy tried to cut me. Tried to assassinate me right in the TV room, 'cause I wanna change the channel in the TV. So they transferred me to 74, lock me here. Nah, this kid tried to step to me 'cause I tried to get them to watch something else, man. They sitting there for two weeks watching Tonya Hardy/Nancy Kardigan. How you gonna tell me that interests you, man? You don't even know what's figure skating, I told them, man. What the *hell* is that? That concerns you? Ice-skating got nothing to do with my life. Once my mother took me ice-skating to Rockefeller Center when I was three years old, I fell and I cried, I said, "What's this? A sport?" Now I'm in jail and I sit there every day, I have to watch that *crap*. That *crap* is punishment for real, man.

I don't *care* about one girl don't want the other girl to win the World Ice Medal, then she gonna start scheming and get some kid with a golf club to hit her in the knee. That is cartoons, man. They in there debating over it, fighting. "She did it!" "No she didn't do it!" I told them, "You in jail, man, fight over your shoes or something!" But you know what is it? I figured it out. It's that people like to see these smiling cornflake-type women *messin’* each other up. 'Cause if you think about it, you never really see, or you rarely see, nah, you might see like in a soap opera or somethin’. Like, one lady's like, "Oh, I'm gonna take her man," or "I'm gonna stab that *witch," or, " ... poison her tea ... " or whatever. But in real life, they're all sitting around the sofa drinking ginger ale. So when it happens in real life, people eat it up. They're like, "What?! Two white ladies fighting? Where?!". They pay money to see it. In cable. In pay-per-view.

Every single day for four months, in the news with that.

Right? .... Who you trying to play? You know you was watching. But see, they make that ice-skating/golf-club *crap*the number one story. They try to make you think that that's the most important *stuff* that you should be concerned about, so that you forget, they try to distract you, to make you ignore, from that you can't feed your kid, that you can't fulfill your dreams 'cause people won't hire you 'cause you got a felony on your record. I had to change the channel man Nah, this kid wanna act hard rock with me, pull a razor. Pssh. I cut him before he cut me .................. Nah, he wanna force me to act like a criminal. I ain't in here 'cause I'm a criminal. I'm in here 'cause I'm poor, that's why I'm in here!

(To the officer) ..................................Huh? A toothbrush Yeah. That's what we're waiting for. (To guy number one) Go get your toothbrush.

Nah, he ain't gonna let me. He ain't gonna let me. Yo, see if you could get two ... Tell 'em they took two . . .
```

---

## IC-0392: James Dean is Dead! (Long Live James Dean)

- Title: James Dean is Dead! (Long Live James Dean)
- Author (byline): Jackie Skarvellis
- Work: Hollywood Legends: ‘Live’ on Stage
- Publisher: Oberon Books
- Publication date as stated: May 2011
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DEAN
- Teaser before the introduction: Yes
- Spoken words (computed): 2048
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jackie Skarvellis
Book: Hollywood Legends: ‘Live’ on Stage
ISBN: 978-1840027693
Publisher: Oberon Books
Date (Month/Year): May 2011
```

### Introduction (context only: never use it for content warnings)

```text
James Dean once said . . . "If a man can bridge the gap between life and death, if he can live on after he's dead, then maybe he was a great man," And if this is the measure of greatness, James Dean had it in spades.

On September 30, 1955 James Dean died in a high-speed car crash at the age of 24 and today, more than 60 years after his death, he continues to be immortalized around the world. This selection bring us into his world as he reflects on his life and his death.

James Dean is Dead! Long Live James Dean by Jackie Skarvellis,
```

### Performance text (classify this)

```text
DEAN: Some crash huh? Whatta way to go, one helluva way to go! Oh, I never thought I'd die, not in the way I did! Steering wheel through my chest, broken ribs, broken neck, I was a mess. But, hey! That's show business! So, where shall I begin? Twenty four summers, young enough to feed the legend! Live fast, die young!

It's my last day on Earth, I keep reliving it. I was on the crest of a wave that day. In love with speed . . . Going fast, faster still, as fast as I can: slam my foot down. There's something coming, something in the way, roadblock? No, another car coming straight for me. He's gotta see me, gotta stop! STOP! (Car crash.) Limbo! Reliving my life over and over again! They won't let me go - they'll never let me go!

DEAN: Immortality, that's all that matters. That's· all that counts in my book. If a man survives in people's minds after his death: that's real fame!

And I got that now. From where I am I can see them standing there in lines, queuing up to do just what I done, the same thing: the Death Ride! Long rows of 'em, a never-ending stream of kids: all clones of me. They're even dressed the same: tight blue jeans, white t-shirt, red nylon zipper jacket, same haircut, same style, they walk like me, they even try to talk like me - to be me! That is fame. I got it at last, but I had to die to get it!

Time, that's what it's all about. Timing: split second precision. Timing: an actor's gift. If I could just cheat time by going fast enough, fast enough to break the sound barrier, fast enough to always stay young, to meet eternity - yes siree! To go fast enough to cheat time - death can't be considered because if you're afraid of death, there's no room in life to make discoveries!

About a week before I died I had my picture taken in this coffin. Don't know why, just had this sudden urge to lie down in this coffin, have my picture taken. It was at Hunt's Funeral Parlour, where they fixed Momma for burial, made her look real pretty. I was on this photo shoot trying to get my face on the front cover of Time magazine when we came to Hunt's. I just got in and told them to 'shoot'! Time turned it down, bastards! Maybe all great actors are psychic, that's how we do what we do. We're very special people picked by God to be his clowns, and that is why they love us - our public. Razzle-dazzle them - I always do!

(flashback to Dean’s first time in NYC)

The city's strange, big scary neon. I'm just a small-town boy from a hick town. Country boy, farm-hand, that's me! I don't fit in anywhere. There's people bought and sold in this city like it's a butcher's shop. Buyers and sellers eye each other up - like the meat market hanging on a hook. That one's tasty, that one's got too much fat, that one's lean and sinewy just like being on the meat rack. Street traders evaluate your worth, calculate your flesh. . . . They don't think I'm good enough, they laugh at my accent. I'll show them. I'll show 'em what I'm made of! I can do any role - anything! Just gimme the chance, gimme a break. But of course they won't, unless I play the right kinda games.

You audition for them and they size you up if you're pretty like me. They eye you up and down like a piece of meat. They look at you like you're something on the menu. You stand in front of them and they say leaning back in their big fat armchairs: 'Hey, Boy!' They like to call you boy like you were some shoe shine merchant, 'Hey, Boy! Before I can cast you kid, I like to get to know my actors better! Know what I mean?' I read between the lines. I smile and nod. Walk into the bedroom and he kicks the door closed behind. Takes his jacket off. I take off mine. We stand facing each other like a couple of cats, or two cowboys having a standoff. He approaches me and grabs my belt. Hard. 'Get my drift boy?' 'Sure,' I say and give him a smile, more a grin really, a knowing sorta grimace. And I sure as hell get his drift.

It opened lotsa doors when I was broke and down on my luck - desperate for a job, I'd do anything. I did anything. You have to make a choice and take that chance. Life here's too tough not to. You gotta work to eat right? I made the decision. Whatever it takes. I had to do it - even if it hurt. They used boots, belts on me. And cigarettes. Cigarette burns all over my flesh. They used my body to stub out cigarettes. In time I got used to it. Hell! I even started to enjoy it! At least with pain you know you're alive!

Hollywood fanfare/White Out.

USA rules, OK? It's 1950, we're gods. It's the Land of Opportunity! I'm picked for a Pepsi-Cola ad on TV and I stand out - the director likes me. This leads onto lotsa other things, and the director always likes me. That's when they're not screaming at me for being difficult, being late, being moody, not knowing my lines. They just love me. But I always stand out in a crowd. I'm not made of the stuff to be an extra. And they notice me because I'm different. . . The Little Prince.

The Little Prince. Like my Bible that book was, I read it over and over again, it became my credo. It's about this little guy from another planet who falls to Earth in the Sahara desert where he meets this pilot whose plane has crashed. But before that he meets a fox and the fox tells him a secret, a secret so precious that he whispers it and the secret is this: 'That it is only with the heart one can rightly see. What is essential is invisible to the naked eye.' I've lived by that credo all my life. The Little Prince who fell to Earth like a star, briefly lighting up the sky with gold. I didn't know it at the time, but that was me. I was that Little Prince. Just like a star that falls to Earth and dies before his time.

So, it's 1952 and I'm accepted into the Actors Studio in New York. God, that's a big break for a boy like me. I can't believe my luck, walking through those doors where all the greats have gone, and Lee Strasberg: Master of Ceremonies! 'You have a talent, but it is undisciplined. What you do is simple and believable, it has a wonderful quality', so far so good. But then it all turned sour like so many things in my life seem to do. I do a piece that I prepared for him, it was a last minute decision to change the scene and, boy, that one big mistake: 'It's crass! It's crap! Call that acting? Call that a performance? You oughta been a cowhand!', and on and on. He knocked the guts outta me. And an actor's gotta have guts, or what's left? Time to do the rounds, endless knocking on unending doors, rejection after rejection - that's something you gotta get used to when you're an actor. It destroys your soul. I didn't just knock, though, I hammered like hell!

The loneliness - I scream inside my skin, inside my skull. There's nowhere so lonely as the big city. I try and keep myself busy: I take lessons in dancing with Eartha Kitt; I take classes - anything to keep the void at bay. The city never sleeps and neither do I. It's all part of my training, I tell myself, to break new ground with my acting technique. I tell myself it's all good experience. (Laughs.) – Flash to an audition scene

Hi! Jimmy Dean! Yes sir, I brought a new piece from a screenplay by a friend of mine - oh, you don't wanna know what its called? Yeah, I play this guy who's all screwed up, right. .. ok. I got this thing, this illness, it's inherited, ya see. My Daddy was a no good bastard so he gave me this disease, it's congenital, it's in my blood, it's not my fault, I inherited it and, and ... No, it's not right, I'd like to start again, I think I got some words wrong - I'M TRYING TO GIVE A TRUTHFUL PERFORMANCE HERE, GODDAMMIT! Sorry!

I just wanna try again, I'm just getting into it now, give me a minute! I need more time. No, I am not wasting the studio's valuable time! Do you want a real performance by a real actor or just some manufactured shit? No! I'm sorry! What? You don't want me to do the speech again? Well, F*** YOU THEN! That's how it was: that's how I was! I took no prisoners, took no shit! Self-obsessed me to the bitter end. A bastard, but, it takes one to know one and bastards make the best actors!

The job I finally landed was in The Immoralist by Andre Gide. Great role for me! I hit all the headlines! The critics loved me - I was their darling, just for once! But then, at the very height of my fame, I quit! I handed in my two weeks' notice. They were stunned: they didn't know why. But I did! It was because at that time Elia Kazan called my agent and offered me the role of Cal in East of Eden. Now, I wasn't gonna turn down a lead role in Hollywood just to be on Broadway, now was I? Hold the bus!

Hollywood Fanfare.

Hollywood! Tinseltown! James Dean had arrived. The whole world knew my name. I was interviewed by all the press. (flash to interview sequence)

Mr. Harold Thompson, New York Times, pleased to meet you sir. No sir, I never did read the novel of East of Eden, I prefer the adaptation.. New York? Love it! No, no, I didn't go to the premiere of East of Eden - too much pressure. Death? Well, it can't be considered, because, like I said before, if you're afraid to die, there's no room in life to make discoveries. Miss Parson, pleased to meet you! Please sit down! Best behaviour with this one, Louella can make and break reputations! Yes ma'am, truth is: I'm dog-tired. Three pictures, back to back almost. I need a rest! Yeah, they say I've done the Hollywood thing, but the truth is, I'm exactly the same as when I didn't have a dime. I need a break! Yes Ma'am, pleasure to meet you too. Phew!! No, no more questions.

Three movies - that's all I made, just three little flicks: Rebel; East of Eden, and Giant - that's all! My whole legend rests on three motion pictures. When I was a kid, I dreamed of fame - not Hollywood as such, just fame. I never thought it would be like this: people staring at you in the street; stopping you in the street - Jeez! They must be desperate! It's like living by proxy, through a screen, through someone else!

People are dumb. They need something to latch onto, It's because they're empty inside so they need something or somebody to look up to, to worship, to imitate. That's why they become film fans. Movies make them come alive again. All of 'em sitting there lost and alone in the dark and then something happens. It's like the light of a star suddenly shines down on them and illuminates every corner of their pitiful lives, and it's magic! They feel the power of my fame, by proxy. It's almost like praying and God appears and throws a handful of stardust down on them.

It's my last day on Earth, I keep reliving it. . . . Another car coming straight for me. He's gotta see me, gotta stop! STOP! (Car crash.) Forever young and beautiful. Live fast, die young. I have to live with what happened - hear that sound? (Crash.) Again and again! Somebody, anybody, please help!
```

---

## IC-0393: The Janitor

- Title: The Janitor
- Author (byline): Rick Najera
- Work: Rick Najera's Latinologues
- Publisher: WPR Publishing
- Publication date as stated: Jan 2012
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CARLOS
- Teaser before the introduction: No
- Spoken words (computed): 774
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rick Najera
Book: Rick Najera's Latinologues
ISBN: 978-1889379425
Publisher: WPR Publishing
Date (Month/Year): Jan 2012
```

### Introduction (context only: never use it for content warnings)

```text
The attacks on the World Trade Center brought America together. Our diverse nation flew the American flag, donated blood and gathered for candlelight vigils together. On the steps of the Capitol, Republicans and Democrats in Congress sang “God Bless America” as one voice. Our country was united.

But not today . . . today instead of being united by real threats, we’re being divided from within by partisan issues: health care, the environment, immigration. Immigration . . . New York City, ground zero for the 9/11 attacks, is today desperately trying to protect their undocumented workers from deportation by federal ICE officials. In fact, the city has banned the use of “illegals” or “illegal aliens” as discriminatory.

In this selection, we travel back to 2001, back to NYC and back to ground zero through the eyes of Carlos . . . . . The Janitor by Rick Najera
```

### Performance text (classify this)

```text
(In the darkness we hear a man whistling a tune. He is dressed as a Dominican janitor. Behind him, he wheels in a janitor dolly filled with cleaning supplies. Throughout his monologue, he is clearning: mopping, trash, dusting, etc)

CARLOS: (To audience) Sorry. I'm not important. I clean here, that's what I do here. You make a mess and I'll clean it, but I clean real good you know? I clean real good. When I was a kid in Dominican Republic, people would say, "Hey, Carlos what are you going to do when you grow up?" "Oh, I'm going to clean things, 'cause I clean very good:” Besides, I was the only Dominican kid that couldn't play baseball; I had to clean. But I was always ambitious. I always wanted to come to the United States of America and be a janitor. At least I found my occupation. I clean -- that's what I do. I clean very good. I clean very, very good. People they say to me, "Carlos you're in America now, in America we use chemicals.” Chemicals, chemicals, chemicals. Okay! I got a cart full of chemicals, but sometimes the natural stuff works the best.

(To a specific person in the audience) Oh man, you look like you like to drink your tequila every once in a while. You mix it, you throw up . . . nothing cleans up vomit better than sawdust, and if it's cedar sawdust, even better. Write it down. That's a trade secret I just gave you. Sawdust for vomit, okay?

(Back to general audience) When I first came to America, I had a good job. I got a job as an elementary school janitor. That was a good job. I used a lot of sawdust there. Flu season or chili day? I saw some bad things; I don't like to talk about that. This one kid he threw up so bad . . . the wall was like a mural. It was like the Sistine Chapel but with Captain Crunch and Fruit Loops. Ay carajo! I got a promotion after that. They made me high school janitor. Ay, that was a good job. High school janitor. They actually gave me a master key to all the kids' lockers and when they were in class I would go in and steal their marijuana. You smoke one of those marijuana cigarettes and those fish tacos from the cafeteria taste gourmet. High school janitor; that was a good job, man!

. . . I had to get out of high school; too much violence in high school. That Columbine thing scared the crap out of me, man. When white kids go bad, they plan it. 9 a.m.: kill classmates. 9:10 a.m.: kill teachers. 10:20 a.m.: kill myself. Ay carajo! That won't happen in a Latino school. I guarantee that won't happen in Latino school. 'Cause they'll never get there at the same time. One will show up at 9, one at 3, one at 5 . . . One won't show up and have a really good excuse the next day why he missed the shootout.

. . . I got out of high school. After that I got my dream job. I got my dream job in the city; I work in one of those big office buildings. Easy work. Easy. All I had to do was clean 20 floors at night and 20 floors during the day;

I made a lot of overtime there. Mucha guardo. Mucha dinero. I even met a girl. She worked at the restaurant upstairs; I worked downstairs. We would meet halfway.

I like living in the city and working in the city. 'Cause I would see all kinds of things. I'd walk in on bosses having sex with their secretaries and sometimes just having sex by themselves . . . Sinverguenzas!

Oh, the girl I was telling you about? She was from Honduras. I fell in love with her and I wanted to marry her and I did. I was so happy because if you can make it as a janitor in NYC, you can make it anywhere. (Beat.) I remember those buildings.

(Lights go up on stage. Reveal two simple beams of light against the wall resembling the Twin Towers.) I was cleaning up that morning when the first plane hit. Ay, what a mess. There was smoke and dust everywhere. Then the second plane hit. Then they fell. My big beautiful buildings fell to the ground. I lost a lot of friends there: other janitors, busboys, and dishwashers from the restaurant upstairs. A lot of Latinos. But you're not going to hear about them on the reports. They were not reported because they were illegal aliens. Why do people have to make messes that they can never clean up? I stayed and helped with the clean-up and a big man comes to me and says, "Why are you here? You're not a fireman:' And I said, "I clean, sir. That's what I do.

I clean. And I'm going to be here until there's nothing left to clean up. Or until I find my wife.
```

---

## IC-0394: Joey Pigza Swallowed the Key

- Title: Joey Pigza Swallowed the Key
- Author (byline): Jack Gantos
- Work: Not specified
- Publisher: Square Fish
- Publication date as stated: July 2014
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: JOEY, GRANDMA, MRS. MAXY, MOM, PRINCIPAL
- Teaser before the introduction: Yes
- Spoken words (computed): 1711
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jack Gantos
ISBN: 978-1454953371
Publisher: Square Fish
Date (Month/Year): July 2014
```

### Introduction (context only: never use it for content warnings)

```text
Meet Joey, a bright, good-hearted boy who struggles with ADHD. Joey knows he’s different—he has trouble focusing, sitting still, and making good choices, even when he wants to and his wild behavior often leads to trouble at school. But at home, things are no easier: his grandmother is manipulative and abusive, and his mother, though trying her best, has a history of drinking and instability – But he’ll get back to you on that . . .

Joey Pigza Swallowed the Key by Jack Gantos
```

### Performance text (classify this)

```text
JOEY: (Pg 3-4) At school they say I’m wired bad, or wired mad, or wired sad, or wired glad, depending on my mood and what teacher has ended up with me. But there is no doubt about it, I’m wired. One day, we were doing math drills in class and every time Mrs. Maxy asked a question, like “What’s 9 times 9?” I’d raise my hand because I’m really quick at math. But each time she called on me, even though I knew the answer, I’d just blurt out, “Can I get back to you on that?” Then I’d nearly fall out of my chair laughing. (laughing heartily) Can I get back to you on that? “Out in the hall,” she said. And the class cracked up.

JOEY: (Pg 7-9) My dad ran off when I was in kindergarten and my mom went after him. My grandmother raised me until this past summer. That’s when my mom finally turned around and remembered me. One morning she rang the doorbell. I wasn’t sure she was my mom because I didn’t even remember what she looked like.

I was a wired-up mess by the time Mom came back. By then everyone thought my grandma was the nutty old lady responsible for my bad behavior. But I am how I am because Grandma was born wired, and my dad, Carter Pigza, was born wired, and I followed right behind them. It’s as if our family tree looks like a set of high-voltage wires strung across a field from one steel tower to the next.

GRANDMA: Joey, I want you to pull your act together. You don’t want to turn out like your father, do you?

JOEY: (Pg 10-11) People who blame Grandma for my behavior are unfair to think that she was the crazy one and I was innocent. It was more that we were whacked-out partners. I’d be the Hulk and she’d be Doctor Doom and when the phone rang, we’d run at it screaming and yelling and slam into each other, and by the time one of us got the upper hand the person on the other end had hung up. (beat) Sometimes she could be funny. But not often. Most times she’d just get mad . . .

GRANDMA: Don’t touch. Don’t wiggle. Don’t run. Don’t yell!

JOEY: (Pg 12) After Mom came back Grandma got worse. She got meaner and she began to scare me. (Pg 15) She’d say the same thing over and over again:

GRANDMA: (Pg 14) You don’t know what you’re doing. You’re ruining everything. You never listen to me. I always said you were as dumb as dirt!

JOEY: (Pg 12-13) About a month before school started she got so mad at me she threw everything out of the refrigerator, yanked out the shelves and flung them across the floor.

GRANDMA: Now get inside and stay inside! I said get in or I’ll tell your mom!

JOEY: But I wouldn’t get in. I knew there were good rules and bad rules, and having a time-out inside a refrigerator was a bad rule. She should have been on meds. Big-time Grandma-sized meds. People just called her a batty old bird. But she was sick like me, only old, so her sickness was different. (thinking, then softly) (Pg 3) Can I get back to you on that? (shakes it off and gets lost in the story again) [Transition: Oh, yeah . . . So anyway, it was out in the hallway at school . . . ] (Pg 4-5) I stood in the hall for about a second until I remembered something I wanted to try. I had seen the Tasmanian Devil on TV whirling around like a top so I unbuckled my belt and pulled on the end really hard, as if I was trying to start a lawn mower. Before long I was bouncing off the lockers because I was dizzy too. I got going really fast and began to snort and grunt like the Tasmanian Devil (snorting and grunting) until Mrs. Maxy came out and clamped her hands on my shoulders. She stopped me so fast I spun right out of my shoes! (Pg 6) And we had a little talk about my behavior goals

MRS. MAXY: (Pg 25) Joey, there are limits in the classroom. And if you can’t live by the class rules then we’ll have to send you down to the special-ed class for extra help. We’ve talked to your mom about this.

JOEY: Okay (to audience) only saying the word because agreeing to stuff was the best way to make it stop. (to Mrs. Maxy) Okay. Okay! (takes some deep breaths to calm down) (Pg 28) [Transition: When I got home, Mom said] now let’s get you some medicine. She put a pill in my hand and a glass of water in the other, but before I could take the pill, she got the bottle of Amaretto.

MOM: (pouring it into a glass) See, Mommy has her own meds.(raises the bottle to Joey) It comes in a bottle.

JOEY: We clinked glasses and I took my pill. I could feel it going down my throat like a little white round superhero pill on its way to beat up all the bad stuff in me. Everyone said it would help. And it did. I felt like a normal kid for a while. But then my old self started to sneak up. (shakes head in bewilderment, long beat)

(Pg 30) I was sitting at my desk after lunch and Mrs. Maxy was writing a long list of spelling words. I was playing with the house key that was on a long string around my neck. (Pg 31) I was trying to train myself to swallow the key so I could slowly pull it back up from inside my belly, like I was fishing. It hurt because sometimes the key got caught sideways, but I just gave the string a tug and straightened it out. Since I was doing it after lunch, bits and pieces of food would stick to the key and around the string and I’d suck them off.

(Pg 32-33) Suddenly Mrs. Maxy swooped down on me. She yanked the string out of my mouth, took her sharp “teacher only” pointy scissors and cut the string and put the key in my T-shirt pocket.

MRS. MAXY: Keep your mind on your work.

JOEY: (Pg 3) Can I get back to you on that? (beat) So . . . my mind wandered and before long I didn’t remember about the string missing and I plucked the key out of my pocket and popped it into my mouth. (showing the key on his tongue and whispering to another student) What’ll you give me if I swallow this?

(not waiting for an answer) I worked up my saliva and swallowed hard . . . I did it! (opens mouth to show it’s empty) Then I reached to pull the string . . . (panics when he can’t find it, he screams) Mrs. Maxy, I ate my key! (takes some deep breaths to calm down)

(Pg 69) I was one of the special people. My mom said I was special, the nurse said I was special, and I was also in special ed. (Pg 73) Even though I’m difficult I’m very special and smart. (Pg 76) (shouting) Math drills are one of my strengths!

[Transition: Another day at school I stayed in at recess to] (Pg 72) make a million bumper stickers that say ‘Hate Is Not a Family Value.’ My mom saw one and said she wished she had a million to put on every car in the world. (Pg 73-75) I got the safety scissors and began to cut the poster board into bumpersticker-sized strips. But [it] was too thick and the scissors kept twisting. The bell rang, so when Mrs. Maxy got up from her desk to stand in the hall, I snuck up to her desk and grabbed her secret extra-sharp teacher scissors. I was racing back with scissors in my hand when it happened. I tripped and sort of dove through the air with the open scissors in front of me like some evil Big Bird’s beak when Maria walked sideways across my path. (look of shock and horror)

I thought I was the one who was screaming. But it wasn’t me. (getting excited) You should have seen the blood. It was like a pipe had burst. And she stood there shaking with her eyes wide open like she stuck her finger in the electric socket. I bent over and picked up the tip of her nose, which looked like a tiny piece of sliced banana. Then I stood up and pressed it back in place, but the blood sprayed out like a shower nozzle. (panics again, shrieking) I’m sorry! I’m sorry!

I tried to wrestle the scissors from Mrs. Maxy who had taken them from me because I wanted to cut my whole nose off to show just how sorry I was. But Mrs. Maxy wouldn’t let me have the scissors and she kept shouting, “Time out! Time out! Go to your corner!” But I was so nuts I couldn’t tell you the difference between a corner and a circle or a square. It was bad, and everyone was staring at me like I was a maniac killer. (begins to cry)

****Meeting with Mom and the Principal*****

PRINCIPAL: Because he has injured another student, he has to be suspended and receive mandatory counseling. That is school policy. The district special-ed bus will pick him up. Given Joey’s record, he was bound to end up at the center anyway. Maybe this is a blessing in disguise. What happens now is all up to him. . .

JOEY: (crying) (Pg 3) Can I get back to you on that? (Pg 90) (long beat as he composes himself) I’m Joey Pigza. (Pg 51-52) I can have good days. (proudly) Entire days when I wake up and I’m calm inside like water when it’s not boiling. I just get dressed and eat breakfast, thinking about what I’d like to do with my day. And then the most amazing thing -- after I think about what I want to do, like read, or see a friend, or write a poem, I actually do all that stuff. (incredulously) I think it, then I do it. This is not how I usually operate. (rate of speech picking up quickly) Usually I wake up with springs popping inside my head, shoot out of bed and directly to the kitchen where I ricochet around after food, zing up the hall to the bathroom where I try to brush my teeth, but I brush mostly my lips and chin and then I explode across the living room and carom off the furniture until Mom gets a grip on me and wipes the toothpaste off my face and works a pill down my throat. From Ricochet Rabbit to Charlie Brown in no time flat. (long beat)

I love it when the meds work, and when I go to school and stay in my seat and kids don’t call me Zippy and teachers pat me on the head and give me gold stars and say nice things to me. (beat) (gathering up his courage) (Pg 73) Even though I’m difficult I’m very special and smart. (Pg 76) (he does a little dance and yells) Math drills are one of my strengths!
```

---

## IC-0395: The Junkie and the Monk

- Title: The Junkie and the Monk
- Author (byline): Mike DeStefano
- Work: The Moth Presents Occasional Magic, Pg 224-231
- Publisher: Crown
- Publication date as stated: Mar 2019
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MIKE
- Teaser before the introduction: Yes
- Spoken words (computed): 1438
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mike DeStefano
Book: The Moth Presents Occasional Magic, Pg 224-231
ISBN: 978-1101904428
Publisher: Crown
Date (Month/Year): Mar 2019
```

### Introduction (context only: never use it for content warnings)

```text
On March 6, 2011, former heroin addict and stand-up comedian, Mike DeStefano died of a heart attack. He was 44 years old. Two years before his death, he recorded this heart-felt narrative for The Moth.

And although DeStefano masked his pain with comedy, the people closest knew him as a loving son and a man who healed souls as a drug and HIV/AIDS counselor. After all, it is our trials and tribulations that make us who we are.

The Junkie and the Monk by Mike DeStefano
```

### Performance text (classify this)

```text
MIKE: When I was a kid, I had a spark in me. I was happy. I always had a little bit of a flame going, and nothing could really knock it out. I went to Catholic school, but even the nuns couldn't extinguish the flame that dwelled inside me. (They tried.)

MIKE: At the time of this story, I was twenty-eight years old. I was in the Winn-Dixie supermarket shopping when this weird feeling came over me, and then I fainted, I blacked out. That had happened to me before, but it was on purpose, with drugs. This time it was a little scary. I was in and out of consciousness. I knew something was wrong.

I ended up in the Palm Beach Gardens Medical Center. I had a tube in my nose, and I was in this incredible pain. It turned out I had double-lobal pneumonia. And for a minute I was really concerned about myself. This was weird. I hadn't worried about myself for a few years, because at home my wife was dying of AIDS, and she was really sick.

All I could think was, I've gotta get out of this hospital. I've gotta get home and take care of her. Because all I did was take care of my wife; that was my life, my job. And it wasn't a problem, I loved it.

So I was lying there, and the phone rang. It was my friend Jimmy, and he said, “Mike, Frannie was in a car accident. Car flipped five times on 1-95.”

No. She can't even walk. She's on so much morphine, there's no way. And, yet, I believed it, because I knew her. We were reformed drug addicts, recovering people. So even though she was suffering with AIDS, the morphine helped her feel better, and she probably just thought, Hey, I can drive.

I knew she was dead, so I laid back, and I was just like, Wow. Because, quite honestly, my life -- the drugs and the tragedy and people dying that I loved, and most of all, my wife being so sick after being off drugs for so long -- it just seemed really unfair. ***** All I knew about God was the one that I was told about as a kid, you know, God's watching. He knows. So I figured that the god who's doing this to me and my wife, I'm not gonna pray to him, you know? What am I gonna say? Can you help me? No. I'm gonna say, What are you doing? Get off the fence. Make a move. Kill us or help us. Do something.

That wasn't really working for me, so I went to this Buddhist place, because I saw an ad in the paper. I thought, I'm gonna go see. So I walk in, and they told me to take my shoes off. They were very sweet and kind, and they had a lot of compassion. This woman said, "Would you like to see the lama?"

I'm thinking it's an animal they've got somewhere, like a sheep type of thing, so I said, "What's a llama?" She said, "No, it's a Tibetan priest."

When she said the word "priest," I immediately thought of, you know, a scary Catholic priest . . . So I walk in there to meet this guy. He's a little man, and he's just sitting there, mumbling a chant, and I'm like, What's he doing? And she says: “He just prays and meditates. He's been doing that since he escaped Tibet with his family. He does this for twenty-some-odd hours a day. Come sit near him.”

I don't know about anyone else, but as a kid if I was in church kneeling and my knees didn't hurt, I was in trouble. Your knees had to hurt in order to be really praying right. So I actually got on my knees, like a good Catholic, and she goes, "No, relax, relax."

I put my hands out, and he took my hands. And when he touched me, I felt so relaxed. I wasn't scared. All the pain went away. I went there every day for a few weeks, meditating and praying. ***** Now I'm in the hospital, waiting for my friend to call me back with more news about my wife's accident. But I've got these Tibetan beads, and I'm thinking of this man, and I'm okay. He blessed these beads for me.

And the phone rings again. But it's not my friend, it's my mother, and she says, “Daddy has a brain tumor." Yeah, this was a bad day. This news just froze me. I took the beads, and I threw them. I was like, You know what? I've been a Christian, Catholic, angry person for twenty-seven years, and now I'm a Buddhist for like three weeks. I don't want that little bit of peace, man. It just makes the rest of life seem so much *worse*.

The phone rings again, so now I'm like, Okay, they are going to tell me my wife's dead. And it was Jimmy, but he said, "Mike, Frannie's okay. Relax."

She had actually been taken to the same hospital I was in, so I had to go visit her down in the emergency room. Will you give me a break here? My dad has a brain tumor, and I'm going to visit my dying wife down in the ER. She didn't die from flipping over the car, but she's gonna die soon anyway. I'm gonna go visit her now, and I've got pneumonia.

A couple of weeks went by, and she ended up in hospice. Young people don't like to die, you know? Not that old people do, but some old people can say, I had a good life.

She didn't feel that way. She was pissed. She didn't wanna die. She was thrown out of hospice for not dying. This happened three times. But finally, this time, she died. I froze. I knew my father was now going to die, too, and I loved my father. We were so close.

Nine months after my wife died, I was out at a movie. I came home, and there was a voice mail from my brother, "Mike, pick up the phone. Mike, pick up the phone." Every time I heard him say "Pick up the phone," I felt a little more fear of what he was going to say. Finally he said, "Daddy's gone."

I'll never forget where I was. I was standing in front of my laundry machines, listening. And I felt my heart get ripped outta me. And that was it. The flame that I had as a kid -- all of it -- was gone, because now everyone had died.

I made arrangements to fly home the next day, and when I got on the plane, I decided that I was going to end my life. I was done. I wasn't telling anyone. It wasn't a threat, it was a decision that I'd had enough of this. There was nothing else to live for. I couldn't wait until the funeral was over, because that was when I was going to do it. I wasn't going to jump off a building or jump in front of a car. People haven't heard of overdosing on drugs?

But all my life God or the universe, or whoever’s running this thing, would always go, Yeah, it's really awful now. You're almost out of hope. But here's a little something nice to keep you going.

So . . . I went to the back of the plane to go to the bathroom. And the lama, the monk that I had met, is sitting in the back row. He sees me, and he put his hands out like he did before. What he was doing is called tonglen *. You have to have amazing karma, they say, to have a lama actually want to do tonglen with you. What they are doing is saying, Give me all your pain, and I'm gonna give you all my joy.

The reason he sat for thirty years in meditation was to open his heart so much that it gets as big as the ocean, so that if you pour some of your pain into it, it absorbs it. That's what his whole life was about. And it worked for me . . . I got home and I've got these Tibetan beads, and I'm thinking of this man, and I'm okay . . . He blessed these beads for me.

*Tonglen: an ancient Buddhist practice to awaken compassion. With each in-breath, we take in others’ pain. With each out-breath, we send them relief.
```

---

## IC-0396: Kidneys and Commitments

- Title: Kidneys and Commitments
- Author (byline): Gil Reyes
- Work: The Moth Presents All These Wonders, Pg 301-305
- Publisher: Crown/Archetype
- Publication date as stated: March 2017
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: GIL
- Teaser before the introduction: Yes
- Spoken words (computed): 1361
- Already set (do not supply): none

### Source block (context only)

```text
Author: Gil Reyes
Book: The Moth Presents All These Wonders, Pg 301-305
ISBN: 978-1101904404
Publisher: Crown/Archetype
Date (Month/Year): March 2017
```

### Introduction (context only: never use it for content warnings)

```text
Let’s talk statistics for a minute. According to Donate Life America, currently more than 90,000 people are on the national kidney transplant waiting list. Every 10 minutes, another person is added. That means these seriously ill individuals are . . .

1. Waiting for person with a healthy kidney to die

2. Hoping the deceased has agreed in advance to donate their organs

3. Praying that the organ is a biological match

4. Undergoing costly dialysis 3 times a week;4 hours a day just to stay alive.

But even though the process of live donor transplants was widely accepted in the 1950s . . . in 2021, 6,000 people in the US died while on the waiting list. If you want to become a living donor, contact a transplant center near you for an initial evaluation. You can save a life.

Kidneys and Commitment by Gil Reyes
```

### Performance text (classify this)

```text
GIL: (Pg 301-305) I'm sure the woman on the other end of the phone identified herself as being from the clinic I'd been to the day before. Maybe she said her name. Maybe she asked if I was sitting down. But I don't remember any of that. In my memory I just pick up the phone, and this voice says, "Go immediately to the emergency room. Your kidneys are failing."

And as I get up and get dressed, there's this voice in the back of my head saying, This is absurd. I'm in my twenties. I'm invincible. I'm immortal. I don't even need health insurance. . . I don't even have health insurance.

GIL: Sure, I'd been feeling bad for a while. But my swollen ankles, those were because I was waiting tables, working double shifts, trying to save up money, not because my body wasn't processing water waste, right? And those splitting headaches, those were because I was really stressed out, trying to get into grad schools, and not because your kidneys regulate your blood pressure.

When I had finally collapsed a few days before, I didn't have any more excuses. That was when my boyfriend, Sean, made me go to the clinic. Sean and I had been dating for a year and living together for a few months. It was moving a little bit fast, but either of us could go to grad school at any minute, so it was fine. We had sort of a day-by-day mentality. We were keeping each other just at arm's length.

In fact, I was able to convince him not to go with me to the emergency room. I mean, why should we both sit around all day waiting for some doctors to tell me that that's not what it is? That it's something else-something that can be fixed with a pill?

So, I went. Alone. Terrified, but hiding it well. And this trait of mine, this sort of crazy independence, maybe it stems from when I came out to my Southern Baptist mother from Alabama and my Catholic Hispanic dad from Texas, when I was a teenager growing up in Kentucky. If you're thinking this didn't go well, you're right . . . There were Bibles manifesting from nowhere (even though I'd been to church more than they had throughout my life). There was screaming and yelling, and I left that night thinking, I'm one of the damned. Because they told me, "You're going to hell."

We didn't speak for a while-over a year. And when we began to try to put our relationship back together, the damage was pretty done. How close can you get when there's this whole part of your life that somebody wants nothing to do with? I remember once, out of the blue, my dad, said, "I never want to meet anyone you're seeing. I don't ever want you to bring anybody home."

But as my emergency-room visit became a ten-day stay in the hospital, I had to let a lot of people know where I was. In fact, that hospital room was where my parents first met Sean. I learned my kidneys were functioning at less than 10 percent. I learned that I would probably have to go on dialysis.

If you don't know much about dialysis, it's a way to live. It's not a great way to live. It's not pleasant. It's very time-consuming. It's expensive. No, what you want in this situation is a living donor, a kidney donor. You could get on the national transplant list. That is going to take time, maybe years, waiting with a bag packed by the door. And cadaver kidneys have other issues; they're not the best choice. If you can get a living donor, though, usually family-somebody who's a perfect match-that's the ideal situation.

Well, my relationship with my parents had left me a little bit wounded. I had trouble trusting people. This is one of the things I was bad at in my twenties. It used to be at the top of the list. Now the top of the list was kidney function. But the not trusting people was still up there. I had this trouble with accepting help. And if you have trouble accepting help, imagine trying to accept a kidney.

People stepped up to get tested. My dad, despite our differences. My mother wasn't eligible. My best friend, his dad. Friends from college, high school, work. But there was one more person who really wanted to get tested: Sean. Talk about a commitment. He eventually wore me down.

He said, "You know, whatever happens, whether or not we're together in the future-if I can do this for you now, I want to."

As the months began to pass, and I did go on dialysis, and my father was disqualified as a donor because of kidney stones, I went on Social Security and food stamps because I was too weak to work. Friends were disqualified for various reasons.

I wasn't going to be going to grad school. I spent a lot of time thinking about how I was going from twenty to eighty overnight. Comparing blood-pressure medicines with my grandmother. I spent a lot of time alone, sleeping, mostly. But I remember this one day where I made it out to the park, and I was sitting alone. It was a cool day, a fall day. I was praying, meditating, considering this entire process. And I found this really strange peace that's hard to describe.

I found this kind of acceptance of myself, and where I'd been, and I thought, You know, it's fine. If this is what it is, if this is it, I'm okay with that. I can die in my twenties. I stopped praying to get better, and I thought about the thing that I'd want. If I could pray for one thing, it was to feel worthy of that love that I hadn't felt for so long. I stopped asking for time, and thought about time well spent.

It was December when Sean called me from work and said, "I have an early Christmas present for you." He was as good a match as my dad. He said, "Would you let me give you a kidney?" And I said, "Yes." And we spent time well. Sean's a big language geek, so we named it: Renee, after the renal system, and Renatus, for rebirth.

We would tell people, "We're having a kidney!" Our friends convinced us to have a party. We had a kidney shower. (Sean really wanted to register, but I thought that might be going a little far.) Nevertheless, people brought us gifts: pajamas for recovering, and bad movies. (Sean loves bad movies.) And we played games, like "kidney bean bingo" and "pin the kidney on Gil." We got this big red-velvet sheet cake shaped like a kidney. And we wore medical masks, and we cut it together, and fed each other pieces and took lots of pictures.

The day of the surgery came in May, and they had us both on gurneys, ready to go. We're surrounded by Sean's family and my family. My parents are there. And my mother starts crying. We never talk about this, but we cry the same way. We scrunch up our cheeks in the same way, and we hold back those tears. I can see it in her face when she's trying to work something out.

She leans down and takes Sean's hand and says, "Thank you." I think she's seeing him differently, and maybe she's seeing me differently.

The surgery goes great, and we recovered together for weeks and weeks in a strange little honeymoon . . . A year later we get a card in the mail. Now, it's not unusual for my mother to send cards. (She sends cards for the strangest occasions, even though they live fifteen minutes away.) But this one was addressed to Sean. It said what a blessing he is. And it recognized our anniversary. They asked us to go to dinner with them, like couples do with their parents.

And I never asked for any proof, because you're supposed to rely on faith, but I have a family where I have parents and a partner-a perfect match-where before I had a boyfriend. And a ten-inch scar across my abdomen to remind me every day that I am loved.
```

---

## IC-0397: The Last Days of Judas Iscariot

- Title: The Last Days of Judas Iscariot
- Author (byline): Stephen Adly Guirgis
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: July 2006
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: JUDGE, GLORIA, BAILIFF, PROSECUTING ATTORNEY, SATAN, P ATTORNEY, JUDAS, DEFENSE ATTORNEY, D ATTORNEY, JESUS
- Teaser before the introduction: Yes
- Spoken words (computed): 1386
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephen Adly Guirgis
ISBN: 978-0822220824
Publisher: Dramatists Play Service
Date (Month/Year): July 2006
```

### Introduction (context only: never use it for content warnings)

```text
From the moment he planted a kiss on Jesus of Nazareth in the Garden of Gethsemane, Judas Iscariot sealed his own fate: To be remembered as history’s most famous traitor. But by identifying Jesus to the Jewish authorities, Judas set into motion the series of events that became the foundations of the Christian faith: Jesus’s arrest, his trial, his crucifixion, and eventually his resurrection.

Given how little we actually know about him from the Bible, Judas Iscariot remains one of its most enigmatic figures. In recent years, the discovery of the long-lost Gospel of Juda, has led some scholars to reconsider his role, and even to ask whether he might have been unfairly blamed for betraying Jesus.

The Last Days of Judas Iscariot by Stephen Adly Guirgis
```

### Performance text (classify this)

```text
JUDGE: (Pg 8-9) Next case!

GLORIA: Between heaven and hell – there is another place. This place: Hope. Hope – is located right over here in downtown Purgatory.

JUDGE: Next case, Bailiff!

GLORIA: Now, Purgatory, contrary to popular belief, has plumbing and bodegas, and they even got a movie theater and a little park that people can walk their dogs at. Hope – well, it ain’t got none a that, and it definitely don’t smell good.

JUDGE: Next case!!

GLORIA: Now Hope, it changes with the times, but has stood always as God’s gift to the last of his children. In Biblical times, Hope was an oasis in the desert. In medieval days, a shack free of plague. Today, Hope is no longer a place for contemplation – “litigation” being the preferred new order of the day.

JUDGE: Where’s my damn bailiff?!

BAILIFF: Here, sir

JUDGE: Then call the next damn case!!!

BAILIFF: Yes, sir. God and the Kingdom of Heaven and Earth versus Thorseen the Implacable: motion to appeal!

JUDGE: Denied – Next case!

BAILIFF: God and the Kingdom of Heaven and Earth versus Benedict Arnold –

JUDGE: Aw, hell no!

BAILIFF: God and the Kingdom of Heaven and Earth versus Judas Iscariot –

JUDGE: -- Judas Iscariot?! Who brings this crap before me?!

PROSECUTING ATTORNEY: (Pg 34) Prosecution now conjures Satan, Prince of Darkness, to the stand! (Satan enters, waves amiably to the jury) (Pg 35-37) So . . . Dark One, tell me: Did you ever have any conversations with Judas Iscariot prior to his selling-out of Jesus Christ?

SATAN: No, I did not.

P ATTORNEY: Never “entered into him” as I believe Saint Luke’s Gospel puts it?

SATAN: No. Quite sure.

P ATTORNEY: Well, then, how ‘bout after he did the deadly deed? Did you speak with the Savior Betrayer then?

SATAN: I spoke to him, yeah.

P ATTORNEY: Care to share?

SATAN: Not a problem. I appeared to Mr. Iscariot at a bar and grill shortly after the night in question. (Scene Break)

SATAN: When I encountered Mr. Iscariot, he appeared to have already taken full advantage of the Happy Hour . . . . (to Judas) Oh. Hello, friend. How are you this evening?

JUDAS: (obviously intoxicated) “How am I this evening?” What are you, a maître d’, man?

SATAN: I’m Clementine. Clementine of Cappadocia.

JUDAS: Yeah?! Well why don’t you go home Cappa-douche-a, okay?!

SATAN: Doe-sha -- Cappa-doe-sha.

JUDAS: Well lemme ask you something – Cappa-doucha-a – do I look like someone who [cares] where you’re from? Leave me alone!

SATAN: I will. Thanks for the advice. (Starts to leave)

JUDAS: Hey!!!! . . . Where you going?!

SATAN: It seems you prefer to be alone.

JUDAS: Why would I prefer that?! What’re you saying: I look like some kinda Lone Wolf? So, what’s your name?

SATAN: . . . Clementine . . of Cappadocia . . . ?

JUDAS: I’m Judas, Judas Iscariot. You never heard of me?

SATAN: Nope.

JUDAS: You don’t get around much, do ya? (Beat) (Pg 38-39) Hey man, If I told you something corny, would you think that I was, like a [jerk]?

SATAN: Not at all.

JUDAS: Okay . . . I’m kinda mildly afraid of going to hell.

SATAN: Why?

JUDAS: Minor incident last night – a miscalculation on my part – nothing serious.

SATAN: Well, one thing I can tell you about hell: As an eternal destination, it’s apparently vastly underrated. Hell is nothing more than the absence of God, which, if you’re looking for a good time, is not at all a bad thing.

JUDAS: Even if I did something, perhaps, a little controversial?

SATAN: Hey, I wouldn’t worry about going to Hell. God understands.

JUDAS: Yeah, but, don’t choices have, like consequences?

SATAN: C’mon, you really think we have a choice?

JUDAS: Okay, well, say, what if someone were to betray, for example . . . the Messiah –

SATAN: -- You mean the Messiah, Messiah? Well, since you asked, I guess I’d say that this guy . . .

JUDAS: Cuz this is just some typo-theoretical guy here –

SATAN: Right. I’d say that if this clown we’re talking about betrayed the Messiah, that probably, “It would’ve been better for that man if he had never been born.”

JUDAS: Never been born?!

SATAN: Hey . . . you asked.

(Scene Break) – Courtroom where the defense attorney is cross-examining Satan.

DEFENSE ATTORNEY: (Pg 66-67) Mr. Satan, you’ve had a long standing feud with God, correct?

SATAN: No. I love God.

D ATTORNEY: You love God? (Pg 69-70) Mr. Satan! What specifically do you love about God?

SATAN: I don’t know where to begin.

D ATTORNEY: Pick a spot!

SATAN: I love God because He is all-powerful and all-forgiving. I love God because his justice is perfect. I love God because God loves me.

D ATTORNEY: God loves you?!

SATAN: Very much. Gift basket at Christmas – Hallmark greetings on all the major holidays.

D ATTORNEY: Mr. Satan – does God love Judas Iscariot? Yes or no?!

SATAN: Go love everybody.

D ATTORNEY: And yet Judas is in hell – so what use is God’s love to Judas if my client is allowed to languish in damnation?

SATAN: Your client is free to leave whenever he wants to – in fact, I wish he would – I could use the room.

D ATTORNEY: That’s not true and you know it! -- The real truth is that God’s love is conditional – isn’t that right?! You failed to meet God’s conditions, and he threw you in the trash! Judas failed – and he’s in a catatonic stupor!

SATAN: Your client succumbed to despair –

D ATTORNEY: Yes! And if human despair is so powerful as to render God powerless over it, then, what does that say about God?! Either God’s not all-powerful and therefore useless – or – God’s love is conditional which renders that love false and unworthy! Which one is it? Is God powerless or spiteful – I am ordering you to answer!

SATAN: (not unkindly) You’re powerless and spiteful – Not God. I’m truly sorry you feel that way.

D ATTORNEY: . . . Nothing further.

TRANSITION: Court is now dismissed (Scene break)

(Scene opens on Judas in his own hell – he may be humming, singing, murmuring to himself, perhaps echoing the phrase “I am” aloud as Jesus speaks the next lines)

JESUS: (Pg 70-73) (Makes his way toward Judas as he speaks to the audience) Right now, I am in Fallujah. I am in Darfur. Right now, I am on Lafayette and Astor waiting to hit you up for change so I can get high. . . I was in that cave with Osama, and on that plane with Mohammed Atta . . . And what I need you to believe is that if you hate who I love that you do not know me at all. I am every last one. I love every last one. People ask of me: Where are you? I ask you: Where are you? (to Judas) Judas . . .

JUDAS: Who’s that?

JESUS: Is it ever anybody else, Judas? (Pause) I miss you. (Jesus lays a hand on him)

JUDAS: DON’T TOUCH ME! Just, go away . . .

JESUS: I won’t go away.

JUDAS: Well, that’d be a first.

JESUS: I have never gone away, Judas . . . Look at me. (Judas does) I love you, Judas. And all I want – all I want – is to be not just near you – but WITH you. I’m right here, don’t you see that?

JUDAS: You got a lot of nerve – I’ll tell you what I know: I watched you trip over your own dusty feet to heal the sick, the blind, the lame, the unclean – But when I needed you – where were you, huh?!

JESUS: Judas . . .

JUDAS: You forgave Peter and Thomas – you raised Lazarus from the dead – But me? What about me?! You just, you just – I made a mistake! And if that was wrong, then you should have told me! And if a broken heart wasn’t sufficient reason to hang, THEN YOU SHOULD HAVE TOLD ME THAT TOO!

JESUS: Don’t you think . . . that if I knew that I would have changed your mind . . . that I would have? (Beat)

JUDAS: All I know is that you broke me – unfixable – and that I’m here . . .

JESUS: Judas – What if I were to tell you that you are not here? That you are with me in my kingdom even now, and that you have been there since the morning of my ascension and that you have never left? (Judas spits in Jesus’ face)

JUDAS: That’s what I think about you! (Jesus doesn’t wipe it off)

JESUS: (Pg 71) I’m sorry. (Pause) Judas – If a thousand strangers spit on me, I will smile. But if the brother of my heart gives me a passing hard look, then, Judas – I will not sleep that night, nor sleep – at all – ‘til he will let me love him again. (Pg 73-74) If you don’t love me, Judas – then you’re gonna have to look me in my eyes and say it.

JUDAS: I don’t love you.

JESUS: If you don’t love me, then why are you here?

JUDAS: Go!

JESUS: Judas! . . . Judas, don’t you know what would happen the very instant you got down on your knees?

JUDAS: Why on my knees? I’ve been on my knees my whole life! You left me.

JESUS: I never left you.

JUDAS: I would have never believed that you could have left. That you didn’t love me.

JESUS: I do love you . . .

JUDAS: No! Why . . . didn’t you make me good enough so you could have.

JESUS: Take my hands, Judas . . Please.

JUDAS: Where are they? I can’t see them.

JESUS: They’re right here. (Jesus takes Judas’ hand in his)

JUDAS: Where are you going?! . . . . Don’t leave me!

JESUS: I’m here.

JUDAS: I can’t hurt . . .

JESUS: I love you, Judas . . .

JUDAS: I can’t . . .

JESUS: Please love me, Judas.

JUDAS: I can’t.
```

---

## IC-0398: Last Plea

- Title: Last Plea
- Author (byline): Mark Bellusci
- Work: Best Men’s Stage Monologues of 1998
- Publisher: Smith & Kraus
- Publication date as stated: January 2000
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: TONY
- Teaser before the introduction: No
- Spoken words (computed): 1876
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mark Bellusci
Book: Best Men’s Stage Monologues of 1998
ISBN: 157525185X
Publisher: Smith & Kraus
Date (Month/Year): January 2000
```

### Introduction (context only: never use it for content warnings)

```text
Do you swear to tell the truth, the whole truth, and nothing but the truth so help you God? You’d better. You don’t have much of an option anymore. Lying isn’t going to do you any good; the jury’s practically convicted you anyway. This is the one chance you have left. Make it good. “Last Plea” by Mark Bellusci
```

### Performance text (classify this)

```text
When he is brought up on charges for stalking his estranged wife, Tony makes the following plea to the judge.

TONY: Your Honor, I know you heard all the testimony and everything. And I know I've done some wrong here, there's no doubt about it. But, you know, before you go and, uh, think it all through, I just want to try and explain my side of the story-no, I know my lawyer did that-and he did a damned-sorry, your honor-a darned good job of it. But-and no offense to your court or anything-it was all kind of legalese stuff. I just want to explain it the way it really happened. You know, in plain English.

(Beat.) No no no, it won't take more than a minute or two. (Beat.) Okay, so where do I-I don't know, I guess we started having troubles a couple a years ago. Right after we had the kid, but before we- (Beat.) Okay, Your Honor. I was just setting up why what happened, but-okay, so we're having troubles after the kid. Nothing big at first, regular arguments like all my buddies have with their wives. But for some reason, ours just got worse. Got so bad I didn't wanna come home a lot of nights-and sometimes I didn't. I mean, with the nagging and the kid crying and me trying to just get a little peace after a hard day's work-you're a guy, your Honor, you know. (Beat.) Well, then you're the lucky one, Your Honor, cause most guys I know, they know what I'm talking about 'cause they've been there. But anyway, it keeps getting worse and worse-the yelling and the screaming and everything. And I'm cutting outta there more and more-just to avoid getting in fights with her. Well, one day, I come home after staying out all night, and she's got this look like a psycho killer. She's quiet at first, but then she starts hitting me-hitting me! Me, who never touched her in her life, she is hitting. And she's not stopping! She's whacking me! So after a while-and I'm a patient guy, I took some shots, my wife, you've seen her, she's built like a middle linebacker-after a while I gotta defend myself.

(Beat.)

No your Honor, I never hit her. No sir! I just kept my hands up and tried to hold her off. I mean, if you saw us after the battle, I'm the one with the black eyes and shi-and stuff. She just had a couple a bruises on her arms where I held her. (Beat.)

That's exactly what I'm leading up to, your Honor. So after this little battle royale, after she beats the shi-the heck-outta me, she says she's moving out. You believe it? I get whacked around and she can't take it no more. So that's what she does she ups and leaves, with the kid. Well Your Honor, I gotta be honest with ya, at first I felt great. I mean, really great. All the pressure off. No kid yelling and screaming, no woman nagging at me. It was like the old single days. But see, here's where it gets fuh-messed-up. See, as happy as I was when she left, I started getting miserable again. Like, all of a sudden, the house was too quiet. Actually missed the kid screaming-I even missed Julia's nagging. I mean, Your Honor, first she makes my life miserable by being home, then she makes my life even more miserable by not being home. I mean, we're supposed to be married, we're supposed to work through all that shi-stuff, right? And that's what I went over her house to tell her. (Beat.)

Yeah, I'm almost there, your Honor. Just another minute. So anyway, I go to her mother's house, tell her I'm sorry for our troubles and that she could come home. And you know what? She says she ain't coming home. Says I'm not ready for her to come home. Me? The one who got beat up? I'm not ready? So, naturally, I get a little pissed. Who wouldn't? I tell her I'm her husband and she's got to come home. So she boots me. Boots me! Her husband! Threw me out on my as-butt. And every time I come over after that, she don't even answer the door. But see, I'm not about to give up on our marriage that easy. I figure, If I could just talk to her-reason with her a little bit-she'll see the mistake she's making. So what I would do is just drive over and wait for her to come out. You know, just so I could talk to- (Beat.)

Yeah, your Honor, I know. But, see, I still can't figure out how that could be stalking if all I want to do is talk to her- (Beat.)

You're right, that's a done deal. We plead on that-but still okay, never mind. So anyway, what happened after, that's what this whole thing is about anyway, and that's what I wanted to talk about. It was about a month ago. I was out earlier that night, at this club, La Mouche-hey, she's living the good life at her mothers, I might as well have a little fun too. So I'm talking to some young girl. She wants to dance, I dance with her. She wants to drink, I buy her drinks. She wants to giggle with her little girl friends about me being older, I just put on a dumb smile and deal with it. Next thing I know, we're in her car, grabbing and mauling, grabbing and mauling, and I'm into it-I mean, your Honor, I am a man with needs and everything. So I'm into it with this young girl whose name I don't even know, just like the old single days, you know? Then, outta the blue, I start thinking about Julia.

Julia! Even when she's not there, she's there. Pissing me off, interfering where she's got no right to interfere. And me? I'm losing it with this hot, drunk twenty-one year old. So that's it, I decide. I tell this girl I'm not into it, she's too stoned to care, and I leave. So...I decide I can't enjoy fuh-messing-around, getting drunk, stoned anymore; might as well live with her. (Beat.)

No, it's not exactly a romantic way to put it, but that's the way I felt. And I wanted her to know, right then and there. So, I drive to her mother's house. Now I admit, it was late. But all I figured on doing was staying in the car, right in front of her house, be there as soon as she comes out in the morning for work. But then I get to thinking, it's hot and miserable in my goddamned car, why the hell do I have to sleep like a dog when she's in a comfortable bed. So I rang the bell. Told her I needed to speak to her. And you know what? She never even opened the door! Told me I'd better leave or she was calling the cops. And she did! She called the fuh-the frigging cops on her husband! (He sighs.) Well, I was gonna sit there in my car, let them take me in, you know? But, then I'm thinking, frickin' cops, why should their life be so easy when mine's a mess? They wanna get in the middle of my marriage, I'll make 'em work for their paycheck, those fat, lazy Irish bastards- (Beat.)

Sorry, your Honor. I didn't know you were part Irish. So-and I now know this was wrong, your Honor-I tear ass outta there. And the cops, they take off right after me. Next thing I know, I'm in a high-speed chase, just like the movies! Well, we're going pretty good, sixty on the side roads. Let me tell you, those guys stayed right with me. So there I am, going through the side streets, you know? But now there are more and more cops on my ass, so I figure, before they cut me off completely, I'll get on the highway, really open it up. So I get on the Belt, figuring if I could make it over the Verazano bridge and through Staten Island, I'll be in Jersey and the cops can't touch me. But when I got on the Verazano Bridge there were, like, thirty cop cars waiting there for me. So that's it, I pullover and I'm ready to go in peacefully. By that point I was tired of the whole thing. So, when I get outta the car, I got my hands on my head, like they do on TV, and I'm just standing there. Well this one cop who's supposed to put the cuffs on me-I'll never forget his name-O'Reilly, that Irish bastard. Sorry your Honor. He comes up to me and starts pushing me, calling me a piece of garbage, saying he wishes he could just beat me till I'm senseless. Well I know my rights. I don't have to sit there taking that from some cop. So I yelled back at him. And then-I don't know, it depends on how you interpret it-I kinda may have pushed him, I think. See, he was so close to my face, with his bad breath and all. I just wanted a little breathing room. Problem is-and everything was happening so fast, you know-I may have instinctively, like, put out my hands, you know? Just to get that breathing room. And, well, when I put my hands out-I don't know-my fists, well, they couldda been closed. And I think that, well, um, my closed hands, they were, like, near his face. So,

I don't know, I guess to some of them, from their angle, it could have looked like I was punching him in the face-which I wasn't, technically. But I think the Irish bastard cop-sorry your Honor I think he thought I punched him, because he went down like he was shot. (Beat.)

No, your Honor. Absolutely not! I did not deck him! See, his face kind of lunged forward right into my closed hands, which were just trying to get me a little breathing room. (Beat.)

Yeah, your Honor, that's what happened. The way it really happened, no matter what the cops say. So okay, now you know the story, I'm happy. And to be honest with you, your Honor, I kinda don't care at this point what you decide, because, I'm already in jail. Solitary confinement in my head, constantly thinking, "how did I fuh-mess-it up so bad?" My wife, my kid, my family, her family, they pleaded, they yelled, and now they're done with me. I'm alone here, your Honor. With my brain racing all the time and me stuck in neutral, running outta gas. (Beat.)

Yeah, that's it, your Honor. You do what you got to do. I appreciate your letting me take a little time here. And I hope I helped clear up a few things. Thanks. Thanks a lot.
```

---

## IC-0399: The Last Rung on the Ladder

- Title: The Last Rung on the Ladder
- Author (byline): Stephen King
- Work: Night Shift, Pg 279-290
- Publisher: Signet Publishing
- Publication date as stated: 1978
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: LARRY, KITTY
- Teaser before the introduction: Yes
- Spoken words (computed): 1848
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephen King
Book: Night Shift, Pg 279-290
ISBN: 978-0451170118
Publisher: Signet Publishing
Date (Month/Year): 1978
```

### Introduction (context only: never use it for content warnings)

```text
The Last Rung on the Ladder by Stephen King
```

### Performance text (classify this)

```text
LARRY: (Pg 279-290) I've been awake all night with it, with Katrina's letter. She could have put it on a postcard. There was only a single sentence below the "Dear Larry." But a sentence can mean enough. It can do enough.

We grew up eighty miles west of Omaha in a town called Hemingford Home-my dad, my mom, my sister Katrina, and me. I was two years older than Katrina, whom everyone called Kitty. She was a beautiful child even at eight, the year of the incident in the barn. It's her I want to tell you about.

LARRY: It happened one Saturday in early November. Mom was at a bake fair in Columbia City, and Dad had gone over to our nearest neighbor's (seven miles away) Dad left me a list of chores to do and told us not to get to playing until they were all done. But that wasn't long.

I remember that day very clearly. The sky was overcast and while it wasn't cold, you could feel it wanting to be cold. On a day like that, the only really nice place to be was the barn. It was warm and filled with a pleasant mixed aroma of hay and fur.

There was a ladder nailed to a crossbeam high up in the third loft, a ladder that went straight down to the main bam floor. We were forbidden to climb on it because it was old and shaky. Dad had promised Mom a thousand times that he would pull it down and put up a stronger one, but something else always seemed to come up.

If you climbed up that rickety ladder-there were exactly forty-three rungs, Kitty and I had counted them enough to know-you ended up on a beam that was seventy feet above the straw-littered bam floor. And then if you edged out along the beam about twelve feet, your knees jittering, your ankle joints creaking, your mouth dry, you stood over the haymow. And then you could jump off the beam and fall seventy feet straight down, with a horrible hilarious dying swoop, into a huge soft bed of hay.

It was a forbidden sport, all right. If we had been caught, my mother would have shrieked blue murder and my father would have laid on the strap. Because of the ladder, and because if you happened to lose your balance and toppled from the beam before you had edged out over the loose fathoms of hay, you would fall to utter destruction on the hard planking of the barn floor.

But the temptation was just too great. When the cats are away . . . well, you know how that one goes.

That day started like all the others, a delicious feeling of dread mixed with anticipation. We stood at the foot of the ladder, looking at each other. Kitty's color was high, her eyes darker and more sparkling than ever. (to Kitty) Dare you.

KITTY: Dares go first.

LARRY: Girls go before boys.

KITTY: Not if it's dangerous.

LARRY: I was ten that year, and thin as Scratch-the demon, almost ninety pounds. Kitty was eight and twenty pounds lighter. The ladder had always held us before.

I could feel it that day, beginning to shimmy around a little bit in the dusty barn air as I climbed higher and higher. As always, about halfway up I entertained a vision of what would happen to me if it suddenly let go. But I kept climbing until I was able to clap my hands around the beam and boost myself up and look down.

Kitty's face, turned up to watch me, was a small white oval. In her faded checked shirt and blue denims, she looked like a doll. (to Kitty) Hi. down there!

KITTY: Hi. up there!

LARRY: I stood up. Swayed back and forth a little. I could hear my own heartbeat as I began to inch along with my arms held out for balance. At last, I stood above the safety of the hay. There was a moment of anticipation. Then I stepped off into space, and as it always did, the sudden grip of gravity, yanking me down, making me plummet, made me feel like yelling: Oh, I’m sorry, I made a mistake, let me back upl

Then I hit the hay, sort of swimming through it, until I could climb out onto the barn floor. I had hay down my pants and down the back of my shirt.

She was halfway up the ladder by then, her gold pigtails bouncing against her shoulder blades. I remember thinking that I didn't like the way the ladder was swaying back and forth. Then she was on the beam,

She stood, poising on the toes of her old low-topped Keds, hands out in front of her. And then she swanned. Talk about things you can't forget, things you can't describe. For a moment she seemed to hang in the air. She was Kitty, my sister, her arms swept behind her and her back arched, and how I loved her for that beat of time.

Then she came down and plowed into the hay and out of sight. An explosion of chaff and giggles rose out of the hole she made. I'd forgotten about how rickety the ladder had looked with her on it, and by the time she was out, I was halfway up again.

I felt the ladder moving beneath me and I could hear-very faintly-the whining rasp of old nails loosening up in the wood. And for the first time I was really, actively scared. I think if I'd been closer to the bottom I would have gone down and that would have been the end of it, but the beam was closer and seemed safer. Three rungs from the top the whine of pulling nails grew louder and I was suddenly cold with terror, with the certainty that I had pushed it too far. The fun of the game was gone.

I hurried out over the hay and dropped off. I came out to the middle of the barn to see Kitty hurrying up the ladder. I called: "Hey, come down! It's not safe!"

KITTY: It'll hold me. I'm lighter than you!

LARRY: Kitty! . . . But that never got finished. Because that was when the ladder let go. It went with a rotted, splintering crack. I cried out and Kitty screamed. The rung she was standing on gave way, and then both sides of the ladder split. Then it toppled, hitting the barn floor with a flat clap.

Kitty uttered a high, piercing scream. "Larry! Larry! Help me” I knew what had to be done, I saw right away. I was terribly afraid, but not quite scared out of my wits. She was better than sixty feet above me, her blue-jeaned legs kicking wildly at the blank air. I was scared, all right. I knew what had to be done. (to Kitty) Kitty! Just hold still, hold still . . .

She obeyed me instantly. Her legs. stopped kicking and she hung straight down, her small hands clutching the last rung on the ragged end of the ladder like an acrobat whose trapeze has stopped.

I ran to the haymow, clutched up a double handful of the stuff, ran back, and dropped it. I went back again. And again. And again. I ran back and forth, building a haystack where the foot of the ladder had been. It was a very small haystack. Back and forth. Back and forth.

KITTY: Larry, I can't hold on much longer!

LARRY: Back and forth. Back and forth. The haystack was as high as my chin now, but the haymow we had been diving into was twenty-five feet deep. I thought that if she only broke her legs it would be getting off cheap. And I knew if she missed the hay altogether, she would be killed. Back and forth.

I could hear the steady, rasping cry of the rung pulling free under her weight. Her legs began to kick again in panic, but if she was thrashing like that, she would surely miss the hay. (to Kitty) No! Stop that! Just let go! Let go, Kittyl (to audience) Because it was too late for me to get any more hay. Too late for anything except blind hope.

She let go and dropped the second I told her to. She came straight down like a knife. It seemed to me that she dropped forever, her gold pigtails standing straight up from her head, her eyes shut. She didn't scream. Her hands were locked in front of her lips, as if she was praying.

And she struck the hay right in the center. She went down out of sight in it- and I heard the thump of her body hitting the boards. It had been too loud, much too loud. But I had to see.

Starting to cry, I pounced on the haystack and pulled it apart. A blue-jeaned leg came to light, then a plaid shirt . . . and then Kitty's face. It was deadly pale, and her eyes were shut. She was dead. I knew it as I looked at her. The world went gray for me, November gray. And then she opened her eyes. "Kitty? Kitty?"

I picked her out of the hay and hugged her and she put her arms around my neck and hugged me back. "You're alive, you're alive, you're alive."

They let me in to see her just before bedtime. She looked at me so long and so lovingly that I was uncomfortable. Then she said,

KITTY: Hay. You put down hay. I didn't know what you were doing, I didn't dare look down, I was too scared. I had my eyes shut the whole time.

LARRY: You didn't know? Didn't know what I was doing? And when I told you to let go you . . . you just did it? Kitty, how could you do that?

She looked at me with those deep blue eyes.

KITTY: I knew you must have been doing something to fix it, You're my big brother. I knew you'd take care of me.

LARRY: It was the end, but somehow not the end. Somehow it never ended until nine days ago, when Kitty jumped from the top story of an insurance building in Los Angeles. I have the clipping from The LA. Times in my wallet. The headline reads: CALL GIRL SWAN-DIVES TO HER DEATH.

We grew up. That’s all I know, other than facts that don't mean anything. The only things that matter are that we grew up and she swanned from that insurance building, and that Kitty was the one who always believed the hay would be there. Kitty was the one who had said, "I knew you must be doing something to fix it." Those things matter. And Kitty's letter. (reading) Dear Larry, I’ve been thinking about it a lot lately . . . and what I’ve decided is that it would have been better for me if that last rung had broken before you could put down the hay. Your, Kitty

She was the one who always knew the hay would be there. And I wasn’t.
```

---

## IC-0400: Life is So Good

- Title: Life is So Good
- Author (byline): George Dawson and Richard Glaubman
- Work: Not specified
- Publisher: Penguin USA
- Publication date as stated: June 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: UNCLE HENRY, PAPA, GEORGE, PETE, CROWD MEMBER, MR. RILEY
- Teaser before the introduction: Yes
- Spoken words (computed): 2459
- Already set (do not supply): none

### Source block (context only)

```text
Author: George Dawson and Richard Glaubman
ISBN: 978-0141001685
Publisher: Penguin USA
Date (Month/Year): June 2001
```

### Introduction (context only: never use it for content warnings)

```text
People spend most of their lives in the quest of happiness and can’t find it. See, the problem is they look to the world to provide them with reasons to be happy. But according to Ralph Marston, “Happiness is a choice, not a result. Nothing will make you happy until you choose to be happy.”

In this selection, George Dawson, a 101-year-old black man who didn’t learn to read until he was 98, recalls a childhood event that set his course through life – the death of Pete, an older boy who was George’s hero.

George’s father helped his son deal with Pete’s death and also taught him a lesson that stuck with George for over a hundred years: Despite all the negative forces at work in our society . . .

Life is So Good by George Dawson and Richard Glaubman.
```

### Performance text (classify this)

```text
(Pg 62-63)

UNCLE HENRY: It’s a white man that will decide when a colored man is in trouble.

PAPA: No, we make our own way. Trouble is out there. More trouble is set aside for colored, but a person can leave it alone and just do the right thing. Then, if trouble still finds you, you’ve done the best you can.

GEORGE: I figured they [both] was right. It was true that Pete didn’t cause no harm and he still had his troubles. But mostly, folks could stay out of trouble if they had a mind to do that. I decided I would do the right thing every day and leave trouble alone. There wasn’t nothing more than that I could do.

(Pg 3-13)

GEORGE: Wanting to enjoy every moment, I stared at the hard candies in the different wooden barrels. The man behind the counter was white. I could tell he didn't like me, so I let him see the penny in my hand.

PAPA: (grinning) Take your time. Son. You did a man's work this year. (to the store clerk) He’s all of ten years, but the boy crushed as much cane as I did.

GEORGE: Since the age of four, I had always been working to help the family. I don't know if it was pride from Father's words or the pleasure from a piece of hard candy that beckoned, but I felt so good I thought I would burst. I had been thinking of those hard candies since my father woke me before daybreak and said,

PAPA: Hitch the wagon, We gonna take some ribbon syrup into town and you comin’.

GEORGE: I wanted to tell him that I was glad he was taking me and it was going to be just him and me together all day. He took care of us. We had potatoes and carrots buried in the straw and salt pork hangin' from the rafters. We was free of worries. Papa was a good provider. Someday I would be just like him.

PAPA: With this ribbon syrup, we be out of debt and have some left for trading. We gonna have seeds for cotton, some new banty chicks, and the fruit trees that are gonna bear fruit next year. No one has the fever and we all be healthy. Life is good. (grinning) I do believe it's getting better.

GEORGE: I liked it when Papa talked to me as a man. Nothing else was said for the next hour, till we came around the last stand of trees and to the rise above Marshall. The hardware store had big windows that I liked to look in. I had never been inside since I knew they didn't appreciate black folks with no money. It was 1908, and I hadn't yet seen a car. I had heard of them, but nobody I knew owned one. The cafe and the barbershop was whites only, but I knew a boy that worked in the cafe. And I knew some folks that shined shoes at the barbershop. Marshall was a busy place and good things could just happen. But at that moment, in the general store, when my father told me that I could do a man's work, anything seemed possible. I remember everything. I saw the white man frowning, my father grinning at me, and those barrels of candy to choose from. I also remember everything my ears told me that day. As I picked up a piece of peppermint, I heard a commotion from the street. My father's gaze followed mine. There were people running, harsh words, and a lot of shouting. Papa run to the door. I followed with the counterman behind me. I heard Pete's voice before I saw him.

PETE: (screaming) It wasn't me. I didn't touch her. Lord, let me go.

GEORGE: First time in my life I saw the white folks and the colored folks together in a crowd. It scared me. There was no more frown on the face of the white counterman that was beside of me. His lips were set in a smile. Hate was in his eyes. Across the street, in front of the barbershop, I saw three colored men frozen in place. The white folks surrounding them had red, twisted faces. They were screaming. I had done nothing, but I felt them screaming at me.

CROWD MEMBER: Kill the nigger boy, kill the nigger. They can't be messing with our white women.

GEORGE: Six men had Pete by the arms. The toes of his boots dragged in the dust. His face looked up to the sky as he screamed,

PETE: I didn't touch her.

GEORGE: I knew Pete and knew that was so. I shouted, "Pete, I'll tell-" My father's hand clamped over my mouth. His other arm crushed the air right out of my chest. I read his eyes and then he slowly let me go without saying a word. I knew it wasn't so, though. The Rileys' cook had heard the whole thing; she just kept on working in the kitchen and watched Betty Jo and her father. Betty Jo had gotten herself in trouble.

When her daddy found out she was with a child, she had a whipping coming sure enough. Her daddy was steaming mad and of short temper anyhow.

MR. RILEY: (shouting) Who's the boy that done this to you?

GEORGE: Betty Jo looked at the belt in his hand. She was crying but wouldn't say nothing. She was scared, and afraid to tell the boy's name, because she figured that her daddy just might go off and kill him.

MR. RILEY: Well, if you did this 'cause you wanted to, a good beating will teach you right. You got it coming unless maybe this happened against your will. (slowly) Is that what happened?

GEORGE: Scared as she was, Betty Jo could tell that the safe answer was yes. Not wanting to tell a whole lie, she just nodded her head.

MR. RILEY: Damn. Was it that Jackson boy from across the ridge?

GEORGE: Betty Jo, she loved him, or at least thought she did, shook her head no. Her daddy looked at her hard. His face turned angry and he said,

MR. RILEY: Was it our hired boy, Pete? That worthless, lazy nigger! Did he rape you? Did he do this?

GEORGE: To each question, she just nodded in the smallest way. The tears still flowed, but he threw the belt down and stormed out the door.

MR. RILEY: There is one nigger gonna pay for this.

GEORGE: Pete was seventeen and the hired boy around their farm-picking cotton, cutting cane, chores like that. He was a good worker. But he was smart and he knew enough not to even look at a white woman. I knew Pete since we were little. Pete, he would do anything for anybody. As I was growing up, I didn't have any toys, but I did still own a baseball that Pete had given me a year earlier. Pete played shortstop. He was good too. If you wanted fast, you should have seen Pete run the bases. Pete was my hero. The colored couldn't play in the big leagues, but if they could I know Pete would of made it. Yeah, someone had committed a sin and Pete was gonna pay for it. I looked down the boardwalk. They was dragging Pete in the direction of the post office. Sheriff Tate stepped off the boardwalk up ahead from where the mob was. I let out a big breath of air. The sheriff was a big man. I knew he could stop this. People was spilling off the boardwalk and cursing Pete something terrible.

CROWD MEMBER: We gonna keep our women safe. Make that boy pay and show all the niggers that they can't get away with this.

GEORGE: Pete was kicking and thrashing, but the mob was still hauling him farther down the street. Taking a few steps along the edge of the road, the sheriff stopped. A big pistol hung off his belt. He pulled the pistol out and crossed his arms so that the pistol set against his chest. He turned and looked back toward the boardwalk. The sheriff was in front of a group of colored that was pressed into the crowd. He scowled and sent them a message that gave me a chill on a hot day. I had heard tell that the sheriff ran with the Klan at night when they would come through the colored section or out to the colored farms. They would leave a burning cross or shoot some windows out. That's what people said about him and now I knew it was true. Behind us, a man was pushing his way out of the store. The sheriff walked toward us and waved his pistol. We opened up some space and let the man through. I saw the big coil of rope slung over his shoulder. I wanted to cry, but I held it back. He ran along the edge of the street and a couple other men stepped down to join him. Some of them were farmers I recognized from when we delivered our cotton. They looked like ordinary farmers with overalls and farm work boots. But that day, their hateful faces made them different. As they caught up alongside Pete, the mob seemed to get inspired. Pete had been twisting and screaming all get-out, but those men seemed to double their strength when they seen the lynching rope coming. Someone pulled a wagon into the shade under the rope. Pete was closer now, could see the rope and the wagon. His shouts and protests had changed to cries for mercy.

PETE: I swear to God it wasn't me. Have mercy, you've got the wrong man. I didn't touch her.

GEORGE: Pete's eyes had a wild look as more men began milling around him. He was up on his feet now, but it was more that they was holding him up. Pete was swaying, as if he was about to faint. His face was all bloodied, but his eyes could see clear what was going to happen. His arms were pinned behind him and someone had bound him around the wrists. One of the men in the buckboard said, "Get that boy up here." Now it was Pete that stood steady and still. Some men were still holding Pete tight from behind so that he couldn't even budge. But if Pete knew he was gonna die, the fear had left his face. The gunshot took me by surprise. I saw the smoke drifting out of the crowd and followed that to see where it came from. The sheriff didn't say nothing, he just walked slowly and holstered his gun. He nodded to the half-dozen men gathered in front of the buckboard and walked back toward the crowd. It was as if he had given his blessing. Pete's legs buckled. He moaned as those men dragged him the remaining few feet around to the back of the buckboard.

PETE: (hopelessly) I didn't do nothing,

GEORGE: I buried my head against my father's chest. When I heard the whip snap and the buckboard lurch forward, I looked back. Pete's neck broke instantly; his head rested at an awkward angle. His eyes were open and he looked out at everyone. As he swayed from the tree, the crowd hushed and tried to look away from his accusing eyes. Not till Pete's body stopped swinging did anyone move. The crowd broke up in silence and went their separate ways. I didn't want to, but as we left Marshall I turned 'round in my seat and looked. Pete was still looking at me and I knew that he always would be. Pete would stay till morning. When they did a lynching, they made us leave the body hanging, to put a terror in the colored folk. His face looked different than I had ever seen it, but Papa still hadn't said a word. (angrily to Papa) “I will never work for or talk to a white person again.” My father, who had seemed lost in his own thoughts, jerked his head and looked at me. “That was wrong what they did. Those white folks are mean and nasty people." Papa swallowed hard and pulled up on the reins so that the wagon stopped. He turned toward me.

PAPA: No. You will work for white folks. You will talk to them.

GEORGE: But, Papa, what about Pete? He didn't do nothing and they killed him.

PAPA: Yeah, I know they had no cause for that, but- his suffering is over, son. It's all over for Pete. You don't need to worry for him.

GEORGE: They took his life. Pete was still young. He should of grown to be a man.

PAPA: That's so. It was Pete's time, though. His time had come and that's that. Some of those white folks was mean and nasty. Some were just scared. It doesn't matter. You have no right to judge another human being. Don't you ever forget.

GEORGE: My father had spoken. There was nothing to say. I didn't know it then, but his words set the direction my life would take even till this day.

I cried and my daddy wrapped his arms around me and held me to his chest. Then something broke loose deep inside. I didn't know a body could have so many tears. I cried for me. I cried for Pete. I cried for the little ones and for Mama and Papa. I cried for all the pain that there was in this world. Papa had his own tears and he just held me. When the tears slowed, Papa told me

PAPA: This morning, I said that you did a man's work. But you was still a boy. Now you are learning to be a man.

GEORGE: About six months after the lynching, Betty Jo had her baby. It was a boy, a little white boy. No one said nothing. I guess by then most folks, white folks anyway, had all forgotten. I didn't forget. . . . I'm one hundred and one years old now. But I still remember. Though that was over ninety years ago, I see it in my mind like I was there today. I can't let loose of my memories, even if I wanted to. Yeah, I've seen it all in these hundred years, the good and the bad. (PG 259-260) Things will be alright. Be happy for what you have. Help somebody else instead of worrying. It doesn’t’ take much to make a difference. Even the poorest man can just take the time to say hello; that can be a help. Have some sympathy for someone’s hard-luck story. Give what you can. And if you have nothing, at least pray for somebody. Have good thoughts. Judge me not for the deeds that I have done, but for the life that I’ve lived. Most folks just don't understand. Life is so good and it gets better every day.
```
