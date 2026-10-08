# Classification request: batch 34 of 63 (40 records, IC-1321 to IC-1360)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-034-reply.json`.

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

## IC-1321: Barrel Fever

- Title: Barrel Fever
- Author (byline): David Sedaris
- Work: Barrel Fever: Stories and Essays, Pgs 126-150
- Publisher: Back Bay Books
- Publication date as stated: June 1995
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ADOLPH, MOTHER, FAITH, HOPE, JOY, TRUDY
- Teaser before the introduction: Yes
- Spoken words (computed): 1934
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Sedaris
Book: Barrel Fever: Stories and Essays, Pgs 126-150
ISBN: 978-0316779425
Publisher: Back Bay Books
Date (Month/Year): June 1995
```

### Introduction (context only: never use it for content warnings)

```text
In Adolph’s world, family bonding looks a lot like emotional dodgeball—everyone lobbing sarcasm, guilt, and questionable gifts at each other just to see who flinches first. His mother, a woman powered almost entirely by complaints and cafeteria Jell-O, turns her hospital room into a full-volume comedy special, starring herself and co-starring anyone unlucky enough to wander in. Mom . . . the gift that keeps on giving – may she rest in . . . well, never mind.

Barrel Fever by David Sedaris
```

### Performance text (classify this)

```text
ADOLPH: (Pg 126-150) My mother was in the hospital, recovering from surgery to remove cancerous lymph nodes. The cancer was nothing compared to the punishment she endured from her roommate, Mrs. Gails. The woman never said a word but watched television constantly at top volume.

MOTHER: (loudly, fidgeting with a bracelet on her wrist) You got any questions about the grazing habits of the North American bull moose? I complained to the nurses about the volume but all they do is point to their ears and whisper that she’s got a hearing problem. If she’s got such a hearing problem then why are they whispering about her? She can hear the food cart from down the hall. (perks up and rubs her hands together) I want that woman dead. (changing the subject) Did I tell you that your sister Charity called me? I hardly recognized her voice because it’s been, what, three years since she’s phoned me. It seems she lost her job at the suicide hot line and is looking to borrow some money. I said, “Hold on just a few seconds, darling. It’s a bit difficult to reach my purse with this IV in my arm.”

MOTHER: (on the phone) Did I tell you what your sister Hope sent me for my birthday? A poncho. Who does she think I am that I might want a poncho? I’ve written her back saying I’m sure it will come in very handy the next time I mount my burro for the three-day journey over the mountains to the neighboring village. I’ve thrown it into the garage-sale box along with the pepper grinder Joy sent me. The thing is two feet long, black and shiny – what do I need with a thing like that? It doesn’t take a psychiatrist to recognize the pepper grinder for what it truly is. I bet she spent weeks knocking that one around with her therapist. But that’s Joy for you, thinking she can impress people with the money she makes ‘consulting.’ That’s what she calls herself now, a consultant, as if that means anything. Anyone who answers questions can call themselves a consultant. A telephone operator is a consultant, a palm reader: they’re all consultants. I thought I’d seen it all but then Faith sent me a subscription to that trade paper she’s working for. She calls it a magazine. Why would anyone subscribe to a magazine devoted to adobe? Is this a big trend? I’ve got a house made of bricks but who wants to read about it every month? Adobe? She circled her name on the first page where she’s listed as ‘Features Editor.’ When people ask what she’s up to I always tell them she’s a secretary – it sounds better. So then, a week after my birthday I got a call from your sister Charity . . .

ADOLPH: Faith, Hope, Joy, Charity, and me, Adolph. See, she just couldn’t help herself. *****

ADOLPH: On the afternoon of my last visit, my mother handed me a check for forty thousand dollars and warned me to cash it fast. Mrs. Gails’s television was blaring a rerun of a vile situation comedy in which a pleasant-looking, vapid teenaged boy acts as the game-keeper of four terminally precocious children.

MOTHER: Leave. (pointing to the door) And on your way out I want you to shut off her television. It’ll take the nurses a good twenty minutes to turn it back on. Give me the gift of peace. It’s worth the forty thousand dollars, believe me.

ADOLPH: As I left the room she offered to double the money if I smothered Mrs. Gails.

MOTHER: Use the pillow . . . The pillow. *****

ADOLPH: [And then she died] Three days after the memorial service we met with her lawyer, an energetic woman with very long fingernails painted to resemble American flags. She informed us that my mother’s house, car, and personal possessions were to be sold at their current market value. That money would be added to her life insurance, pension plan, and bank holdings and, according to her will, would be donated to her specified charitable organization, The National Rifle Association.

After the initial shock had worn off, my sisters found themselves [with] plenty more to talk about. I didn’t mention the money (the 40 thousand dollars) . . . like my mother, I may be mean but I’m not stupid.

Shortly after my mother died, my sisters and I found ourselves rummaging through a cabinet of papers marked “POISON,” and it was there, tucked between the pages of a well-worn copy of Mein Kampf, that I discovered fifteen years’ worth of her annual New Year’s resolutions. She took up the practice the same year she bought her first rifle. Every Christmas afternoon, after placing the artificial tree back into its box, she would grow reflective.

MOTHER: Was it wrong of me to spit on that Jehovah’s Witness girl? Tell me the truth here. I need a second opinion.

ADOLPH: On New Year’s Eve she would sit with her notes and a coffee cup of champagne, glancing at her watch and tapping a pencil against the legs of her chair. She would write something on an index card and, moments later, shake her head and erase it. The process was repeated until she wore a hole through the card and was forced to start fresh on another. The next morning I would ask, “So, what was on your list, Mom?”

MOTHER: Smother those homely teenagers who call themselves my children is at the top.

ADOLPH: I always got a great kick out of my mother, but my sisters, for one reason or another, failed to get the joke. They have grown to be humorless and clinically sensitive: the sorts of people who overuse the words “rage” and “empowerment” and constantly ask, “What do you really mean by that?” While I would often call and visit our mother, they kept their distance, limiting their postal or telephone contact to the holidays.

Following her death my sisters were horrified to discover, sealed in boxes, every gift they had given her.

FAITH: How could she not want a first edition by M. Scott Peck?

HOPE: I made these wind chimes with my own two hands. Didn’t that count for anything?

JOY: What did she have against pepper grinders?

ADOLPH: Aside from a few stiff wallets fashioned in summer camp, there was nothing of mine in those boxes as, at an early age, I discovered that postage stamps, cartons of cigarettes, light bulbs, and mail-order steaks are the gifts that keep giving.

“How could she possibly be so cruel?” my sisters asked, coming upon the unmailed notes and letters stored in the “POISON” file.

JOY: (holding a draft of her graduation card) I am not the ‘missing link,’ I am not, I am not. I am not ‘God’s gift to fraternity beer baths,’ I am not, I am not, I am not.

ADOLPH: Charity and Faith gathered round and the three of them embraced in a circle of healing. There were letters to me, but in all honesty it really didn’t bother me too much. We all entertain hateful thoughts every now and then. My mother hadn’t mailed those letters; she simply left them to be discovered after her death. Hey, at least she was thinking about us.

The most shocking discovery in the box marked “POISON” were not her letters, but the stack of New Year’s resolutions she’d spent so long composing. Each of the fifteen cards was dated in the left-hand corner and, in her slanted, childlike writing, each one read the same: “Be good.” It shook me up as, in the three years that I myself have been making such lists, mine say the same thing, relatively. I have taken to softening my approach as a safeguard against failure. The last one reads: “Try to think about maybe being good.” “Try” and “maybe” give me the confidence I need in order to maintain the casual approach best suited to my ever-changing circumstances.

[So here I was looking] at my telephone and [telling] myself that I would (wait) until someone called, at which point I would answer and redirect my life. Whoever they were and whatever they wanted, I would take it as a sign. (beat) The phone didn’t ring until sometime around ten in the evening. It was a woman’s voice and she started in immediately saying. . .

TRUDY: All right now, I realize you probably don’t remember who I am, do you? It’s me, Trudy Chase. I used to be Trudy Cousins. Chase is my married name even though I’m no longer married if that makes any sense! Anyway, I read the obituary on your mother. I know it’s been a while but I just wanted to tell you that I’m very sorry to hear about it.

ADOLPH: I didn’t know how to respond.

TRUDY: You really don’t remember me, do you? It’s me, crazy Trudy who used to sit beside you in Mr. Pope’s senior English class. Remember me? I was the crazy one. I was the one who wrote ‘Don’t follow me – I’m lost too’ on the back of her graduation gown. It’s me, crazy Trudy.

ADOLPH: (to audience) Suddenly I remembered her perfectly. Even at eighteen she struck me as hopeless. (to Trudy) So, Trudy, what’s going on?

TRUDY: Oh, you know me. I’m just as crazy as ever. No, I take that back – I’m probably crazier if you can believe that!

ADOLPH: (to audience) Trudy went on to tell me that she’s lived in Manhattan for three months, having been transferred from the home office in Piedmont. She chuckled, adding that the people here think she’s just about the craziest person they’ve ever met. She’s so crazy that she planned an office party for Lincoln’s birthday and petitioned her boss to free the slaves in the accounting department. And she even wore a tall hat and a fake beard! The members of her tenant’s association thought she should be committed after she hosted the last meeting . . . by candlelight! (to Trudy) Ha, ha. That sounds pretty scary.

TRUDY: Nothing scares me. That’s how crazy I am.

ADOLPH: Nothing?

TRUDY: Not a damned thing. Nada. Othing-nay.

ADOLPH: The very idea that, out of nowhere, a member of my 1975 graduating class would call me and speak pig Latin created a mixed sense of repulsion and endless possibilities.

Trudy spoke of her involvement in any number of organizations. She is, for example, volunteering to walk the dogs of recent stroke victims.

TRUDY: I usually walk with a woman named Marcie, and, Jesus, if you think I’m crazy, you should meet her! We call ourselves the Poop Troop, and next week we’re getting our uniforms. You should join us sometime.

ADOLPH: I pictured myself wearing an “I brake for hydrants” T-shirt and a baseball cap decorated with a synthetic stool.

On top of everything else Trudy also finds the time to play on her company volleyball team, iron for her crazy arthritic neighbor, and teach underprivileged children to make fudge. She didn’t say it in a boastful way. She wasn’t looking for a medal or trying to make me feel selfish. She invited me over to her apartment for a get-together, but I bowed out, claiming I had a business meeting to attend.

TRUDY: Well, if your meetings are half as crazy as mine you’re going to need all the luck you can get,” she said.

ADOLPH: She asked if she could call me after my meeting and I told her to hold a moment as I had another call coming in. She’s been holding for fifteen minutes now and I still can’t make up my mind. I look over at my mother’s card on the refrigerator. BE GOOD. But she never specified: Be good to whom? If I’m good to Trudy Chase, I’ll tell her never to call me again. If I’m good to myself, I’ll wind up making fudge and walking the dogs of stroke victims. Which is worse?
```

---

## IC-1322: Birdcage: The Shooting Script

- Title: Birdcage: The Shooting Script
- Author (byline): Elaine May
- Work: Not specified
- Publisher: Newmarket Press
- Publication date as stated: June 1999
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, ALBERT, ARMAND, AGADOR, MAN, AS ALBERT
- Teaser before the introduction: Yes
- Spoken words (computed): 890
- Already set (do not supply): none

### Source block (context only)

```text
Author: Elaine May
ISBN: 978-1557042774
Publisher: Newmarket Press
Date (Month/Year): June 1999
```

### Introduction (context only: never use it for content warnings)

```text
Armand and Albert are in a committed, although un-conventional, relationship. 95 percent of the time they don’t worry about how they are viewed by the world. They are comfortable as the owner and star of the Birdcage, a drag club with a fantastic stage show! But when Armand's son springs wedding plans on them, their unconventional life must suddenly appear to be quite conventional. The potential in-laws are the ultraconservative Republican Senator Kevin Keeley and his wife Louise. In this selection Albert tries his best to vanquish his inner drag queen. Birdcage: The Shooting Script by Elaine May.
```

### Performance text (classify this)

```text
CHARACTERS:

• Armand Goldman: The openly gay owner of a drag club called The Birdcage • Albert: An extremely effeminate and flamboyant man, the star attraction of the club. • Agador: Their flamboyant Guatemalan housekeeper. • Man: Generic man on the street – tough and ready to fight (The atypical New Yorker)

*************************************************************************

Open with Albert singing the beginning of "Little Dream" by Stephen Sondheim on the Birdcage Stage . . . . (listen to the lyrics as https://www.youtube.com/watch?v=WiybXEgwTCQ )

ALBERT: (singing) What is this dream I see? Why does it seems so real to me? What if this dream turns out to be, more than a dream . . . . (stops singing to complain to Armand about one of the backup dancers) Well this is impossible, either I’m an artist, or I’m just some cheap drag queen - playing it straight so he can get laughs. I mean he’s chewing gum! (p. 29, scene 36)

ARMAND: Let’s just try and get through it . . . (p. 29, scene 36)

ALBERT: Armand, you always ask so much of me. I have to understand every nuance of a song. I have to rehearse in full costume. But everyone else can just get through it. (p. 29, scene 36)

ARMAND: All right, let’s take it from the top . . . no more talking . . . from anyone. (p. 29, scene 36)

ALBERT: Armand, did you see what he did? He blew a bubble with his gum. While I was singing. He can’t do that while I’m singing. (p. 30, scene 36) (storms off stage to the dressing room)

AGADOR: (walks into room…holds out high heels and stockings). Just put these on. Please.

(p. 3, scene 6)

ALBERT: No, Agador. (Albert) will not dance the dance of the red shoes tonight. Or any other night. (p. 3, scene 6)

AGADOR: Just the stockings. (p. 3, scene 6)

ALBERT: (Albert) is dead. (p. 3, scene 6)

AGADOR: Just this stocking? (p. 3, scene 6)

ALBERT: Do you know how she died? Alone. Weeping for her lover. For each man kills the thing he loves . . . (p. 4, scene 6) (Armand knocks insistently on the door)

AGADOR: Let’s open the door for (Armand), shall we? Let’s be nice. (p. 4, scene 8)

ALBERT: No. I don’t want him to see me. I’m hideous. (p. 4, scene 8) Fat and hideous. (p. 5, scene 8)

AGADOR: I know. (p. 5, scene 8)

ALBERT: Oh, Agador I’m in such pain . . . (p. 5, scene 8)

AGADOR: I know. It will pass . . . (p. 5, scene 8)

ALBERT: It will never pass. I hate my life . . . (p. 5, scene 8) Whatever I am he made me. I was adorable once. Young and full of hope. Now I’m this short, fat, middle aged, insecure thing. (p. 6, scene 8)

ARMAND: (suddenly appearing in the doorway) I made you short? Do I send Carmen on (to do your number)? (p. 6, scene 8)

ALBERT: No! How dare you! (p. 6, scene 8)

ARMAND: Yes! (p. 6, scene 8)

ALBERT: Please! I’ll go on. Don’t give my number away! I’ll be good. (p. 6, scene 8)

ARMAND: All right! (p. 7, scene 8)

ALBERT: My hands are shaking. Agador I need some Pirin tablets. Quickly. (p. 7, scene 8)

AGADOR: Here. One before the show and one after. But no more. (p. 7, scene 8)

ALBERT: Thank you, my darling Agador. (p. 7, scene 8)

ARMAND: (pulling Agador to the side) What are you doing? Why are you giving him drugs? What the hell are Pirin tablets? (p. 7, scene 9)

AGADOR: They’re Aspirin with the “a” and the “s” scraped off. (p. 7, scene 9)

ARMAND: My God! What a brilliant idea. (p. 7, scene 9)
TRANSITION
And as if the pressure of the nightly drag-extravaganza isn’t enough . . . Armand soon reveals
some new news. News that only adds to Albert’s stress level . . .

ARMAND: (Albert, my sons’) fiancée is coming tonight -- with her parents. And we . . . we thought . . . it would be better if you weren't here. (p. 43, scene 55) This is not because of you. This is because this girl’s parents are a**h****. (p. 45, scene 56)

ALBERT: Oh. I understand. It's just while people are here. It's nothing. It's painful, but it's not important. I'm leaving. The monster is leaving. I’m leaving. You're safe. (walks out) (turn) (p. 44, scene 55) (Oh, Armand,) My heart is breaking (turn left)

(p. 44, scene 56)

ARMAND: (puts hand on ALBERT’S shoulder) Oh, God. Please. Don't cry. It's all right. You can stay. (p. 44, scene 56)

ALBERT: Maybe . . . (picks up a teacup and takes a sip, pinky up in proper British form) maybe it is too much to introduce me as his mother on the first visit. (sip) Could you tell them I was his uncle? Uncle Al? (p. 46, scene 56)

ARMAND: (Big pause and sigh) Oh, f*** 'em! Of course, you can pass as an uncle. You're a great performer. And I'm a great director! Together we can do . . . almost anything. We have (looks at watch) five hours. First - your pinky. It's up again. Get it down. And stand up straight. (p. 46, scene 56)

ALBERT: (jumps) Oh! My God! What are you doing? (p. 47, scene 56)

ARMAND: I'm teaching you to be a man. Now this is a dinner party so let's work with the food. Spread some mustard on that bread. Not with the spoon. Don't dribble little dots of mustard on. Take the knife and smear. Men smear. (p. 47, scene 56)

ALBERT: (smear mustard on bread with tongue out) Oh, God! I've pierced the toast! (p. 47, scene 56)

ARMAND: So what? The important thing is not to go to pieces when that happens. React the way a man would. Calmly. Just say to yourself, "Albert, you pierced the toast. So what? Your life isn't over." Try another one. (hands ALBERT another piece of toast) (p. 47, scene 56)

ALBERT: (takes toast) You're right, you're right. There's no need to get hysterical. All I have to remember is that I can always get more toast. (p. 47, scene 56)

ARMAND: That's the spirit. Now let's see you walk. (p. 47,scene 56) (Albert walks)

ALBERT: Holding the sandwich? (p. 47, scene 56)

ARMAND: It doesn’t matter, just walk. (p. 47, scene 56) ALBERT (turn) Too swishy? (p. 47 scene 56)

ARMAND: Let me give you an image. John Wayne. (p. 47, scene 56) He had a very distinctive walk and if anyone was a man . . . Just get off your horse and head for the saloon. (p. 48, scene 56) (Albert walks “John Wayne” style back to center)

ALBERT: No good? (p. 48, scene 56)

ARMAND: Actually . . . it's perfect. I just never realized John Wayne walked that way. (p. 48, scene 56) Take it from the top. (p. 49, scene 59) (Armand bumps into Man)

MAN: Take it easy. (p. 49, scene 59)

ARMAND: You take it easy pilgrim. (p. 50, scene 59)

MAN: Well, (you) bumped into me. (p. 50, scene 59)

ARMAND: Well, tough gazongas. (p. 50, scene 59)

MAN: Why are you being such a pr***? (p. 50, scene 59)

ARMAND: Why are you being such an a**h***? (p. 50, scene 59)

MAN: (Standing – he is very large) Did you just call me an a**h***, a**h***? (p. 50, scene 59)

ARMAND: No actually I was talking to the a**h*** behind you. (p. 50, scene 59) Pantomime fight scene ensues between Armand and “the Man” TRANSITION

AS ALBERT: Well . . . who would have expected that! These MEN . . . they think that fighting is the answer to everything! (Heavy sigh)

ALBERT: See the swelling’s already gone down. It’s nothing. Very masculine. That big idiot looked so ridiculous when he sat on you and banged your head into the ground. He didn’t even know how to box. Are you all right? (p. 50, scene 60)

ARMAND: I hurt my thumb. (p. 9, scene 10)

ALBERT: Oh, my god! Forgive me? (p. 9, scene 10)

ARMAND: No, no forgive me, my little roundness. My teddy bear. (p. 9, scene 10)

ALBERT: My king! (p. 9, scene 10)

ARMAND: My queen! (p. 9, scene 10)
```

---

## IC-1323: The Blundered Buss

- Title: The Blundered Buss
- Author (byline): Patrick F. McManus
- Work: The Good Samaritan Strikes Again
- Publisher: Henry Holt & Company, Inc.
- Publication date as stated: Sept 1993
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1254
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patrick F McManus
Book: The Good Samaritan Strikes Again
ISBN: 0805029222
Publisher: Henry Holt & Company, Inc.
Date(Month/Year): Sept 1993
```

### Introduction (context only: never use it for content warnings)

```text
The questions are as old as time: Where do your noses go? Eyes open or closed? Which side should I tilt my head to? Open lips, closed lips? And if you are really nervous you spend time practicing on inanimate objects: Your hand, your little sisters Raggedy Ann Doll, or heaven forbid . . . .The Mirror. All in the vain attempt to make your First Kiss one that will launch fireworks into the sky and cause the angels to break into a rousing chorus of Hallelujah. Unfortunately, the perfect first kiss only happens on take 37 of most movies, and the rest of us are left to suffer through The Blundered Buss by Patrick McManus.
```

### Performance text (classify this)

```text
Having pretty well exhausted my interest in quantum physics, which took the better part of three minutes, I recently turned to a much more fascinating subject for pondering: the firsts of my life, such as first kiss or first fish. Oddly, I haven't been able to extract my first fish from the mists of time, but memory of my first kiss leaped forth with agonizing clarity.

Perhaps what makes my first kiss so memorable is that it was conducted more as a scientific experiment than as an act of adolescent lust. I simply wanted to determine what kissing a girl felt like, nothing more. My interests at the time centered mostly on guns and hunting, and I tried to transfer my knowledge of shooting to the act of kissing, the similarity in these activities being that in each there is a target you're supposed to hit.

The situation was this. My cousin Buck showed up at my house to request a favor of me. Buck was several years older than I and possessed a driver's license along with, and more importantly, a car. He would on occasion interrupt the car's basic purpose as a vehicle for his amorous pursuits and use it to take me hunting and fishing. The car was his main hold on my loyalties, other than brute force. The reason he had singled me out for the favor was that someone-I didn't know who-had started a rumor that I was quite a ladies' man and that most of the girls in my freshman class at Delmore Blight High were absolutely crazy about me. The person who had contrived this mischief had even suggested that I was a great lover. He had even invented numerous fictional anecdotes in support of that reputation. I realized, of course, that the person who had started the rumor was probably a shy and insecure boy totally lacking in experience with the opposite sex, a lad not unlike myself. I could only sympathize with the rumormonger, and saw no reason to cause him embarrassment by denying the rumor, much as I would have liked to when I heard the favor Buck requested.

'Hey, lover boy," he greeted me. "Guess what you’re doing Saturday night."

"Going to a movie," I said. "A Randolph Scott Western. I can't miss it."

"Yeah, you can. Listen, I got a big favor I need to ask you. You know my new girl, Velveeta? Well, her cousin, who's about your age, maybe a little older, is coming to town, and Vel insists that she hang out with us. So I need you for the cousin. I figure I'll take 'em out for Cokes and burgers, and then I'll pick you up on the way out to the gravel pit."

No, not the gravel pit! For years I had lived in terror of one night finding myself lured to that infamous hole. The gravel pit was the local lovers' lane, or in this case, lovers' pit.

Hey, the gravel pit," I yelped. "You don't have to twist my arm to get me to go to the gravel pit!"

"That's better," Buck growled. "If you'd just said so first, I wouldn’t have had to twist it.

Thus it was that the following Saturday night I found myself on the opposite side of a back seat from a girl who looked like a movie star. She had blue eyes and tawny hair and an actual figure, and she was darting glances at me that sophisticated young women reserve only for freshly squashed worms on a wet sidewalk. The small part of my mind unparalyzed by terror deduced that this was going to be a long and harrowing evening at the old gravel pit. I made a mental note to mention to Buck the next day the anguish he had caused me. Then I'd kill him.

Scarcely had we arrived at the gravel pit than Buck and Velveeta began exchanging passionate kisses. I made a quick study of Buck's technique, never before having had the opportunity to observe passionate kisses at close range, so close in fact that the sounds emanating from the front seat reminded me of those made by toothless Old Man Crawford slurping up a bowl of noodles. Never before had I put Old Man Crawford and romance in the same thought, which says something about the stress of the evening. Although I appeared outwardly calm and casual, despite the loss of all feeling in my extremities, my mind had recovered from its paralysis and now ricocheted about the inside of my skull in wild panic. To rein it in, I started to pretend to myself that this girl was merely another quarry to stalk. I would simply apply the same psychology I used to fend off buck fever, or in this case, doe fever. I was by no means totally opposed to kissing the girl, because I had long wondered what it would be like. It would be interesting to analyze the sensations, coldly and objectively, as a scientist would do with any experiment.

Despite my painful ignorance about all matters related to the opposite sex, I nevertheless realized that it would be uncouth of me to treat a girl as a mere science project. Before attempting to conduct the experiment, I thought I should first get to know something about her as a person, such as her name, for instance. My attempt at engaging her in preliminary casual conversation was not helped by the noodle-slurping sounds emanating from the front seat.

"By the way, what's your name?" I inched across the seat toward her, beginning my stalk. From the front seat: slurp smack slurp slurp smack.

"Opal."

"So, how about them Yankees, Opal? Won three in a row." Inch inch. Slurp smack slurp slurp smack.

"Yeah." Slurp smack ...

"Uh, hot lunches at our school are really terrible. I bet they are at yours, too. You like noodles?" Inch inch. Slurp smack

"Yeah."

As I drew within firing range of her moist scarlet pouting lips, Opal suddenly tilted back her head and closed her eyes. For a moment I thought she had dropped off to sleep, but then realized she had somehow divined my intent, and even approved of it, if only as a means of killing time. Cold sweat gushing from every pore, I took a deep breath and poised myself for the shot, finger tightening on the trigger, so to speak. Then I made a stupid error: I shut my eyes! Blindly I went for the target, only to discover too late that I had miscalculated the trajectory. My dry, puckered, quivering lips closed not on a soft, more or less receptive mouth but on a hard, unyielding protuberance. Startled by the unexpected sensation, I popped open my eyes to reorient myself and discovered I was kissing the bridge of Opal's nose! Cripes! Two wide and indignant blue eyes stared directly into mine from an inch away, rather disconcerting, I must say.

So back to witty conversation. Presently, Opal closed her eyes and tilted back her head once more. As I pondered whether to run the experiment again, with my eyes open, a tiny snore escaped her lips. I knew then that I had no great talent as a lover, or as a witty conversationalist either, for that matter, and in the future would concentrate only on stalking game possessed of either four legs or feathers. Still, a first kiss is a first kiss, even a blundered buss.
```

---

## IC-1324: The Book of Mormon (PG-13 Version)

- Title: The Book of Mormon (PG-13 Version)
- Author (byline): Trey Parker, Robert Lopez and Matt Stone
- Work: Not specified
- Publisher: Newmarket Press
- Publication date as stated: June 2011
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MORMON, JESUS, MORONI, ELDER PRICE, ELDER CUNNINGHAM, VOICE, PRICE AND CUNNINGHAM, LION KING CHARACTER, MAFALA, UGANDAN, NABULUNGI, KALIMBA, JOSEPH SMITH, MIDDALA, SADAKA, MISSION PRESIDENT, THE GENERAL, MUTUMBO, UGANDAN 1, UGANDAN 2, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1765
- Already set (do not supply): none

### Source block (context only)

```text
Author: Trey Parker, Robert Lopez and Matt Stone
ISBN: 978-1557049933
Publisher: Newmarket Press
Date (Month/Year): June 2011
```

### Introduction (context only: never use it for content warnings)

```text
The Book of Mormon by Trey Parker, Robert Lopez and Matt Stone
```

### Performance text (classify this)

```text
NARRATOR: (Pg 1) Long ago, in the year of our Lord 326 AD, a great prophet is leader of the Nephite people in ancient Upstate New York. His name . . . is Mormon.

MORMON: I am Mormon. My people sailed here from Israel to create a new civilization. These golden plates tell of our people and how we met . . . with Jesus Christ. (Christ appears to Mormon)

JESUS: I am Jesus. Take care of your golden plates, Mormon, for soon, your entire civilization will be gone and nobody will remember you. (Christ leaves)

NARRATOR: Just before the Nephite people were wiped out, Mormon gave the plates to his son, Moroni.

MORONI: I am Moroni, the last of my kind. I shall bury the golden plates, father, and perhaps one day, someone very special will find them . . .

NARRATOR: And lo, Moroni buried the golden plates high on a hill. Centuries later the golden plates were found, giving birth to the fastest growing religion today! A church that sends missionaries out . . . All over the world . . . Elder Price, a young missionary in a white shirt and black tie, holding the book of Mormon pantomimes ringing a doorbell (Ding Dong)

ELDER PRICE: Hello! My Name is Elder Price, and I would like to share with you the most amazing book.

ELDER CUNNINGHAM: (Pg 4) Hello! My Name is Elder Cunningham. Would you like to change religions, I have a free book written by Jesus!

VOICE: No, No, Elder Cunningham! That’s NOT how we do it. You’re making things up again. Just stick to the approved dialogue.

ELDER CUNNINGHAM: Hello! My Name is Elder Cunningham, and we would like to share with you this book of Jesus Christ.

PRICE AND CUNNINGHAM: You simply won’t believe how much this book will change your life!

VOICE: (Pg 5) Elders, you have been training for three months and you are now . . READY TO GO OUT AND SPREAD THE WORD! In a moment you will be assigned your mission companions and locations!

ELDER PRICE: (to audience) The most important time of a Mormon kid’s life is his mission. I know my mission will be something incredible.

VOICE: (Pg 9-10) Elder Price? Your brother will be . . . Elder Cunningham!

ELDER CUNNINGHAM: That’s! That’s ME! (He struts to Price and gives a big dorky wave) HELLO!!!!! (Price is less than enthused)

VOICE: And your mission location is . . . UGANDA!!!!! (Price looks visibly upset.)

ELDER CUNNINGHAM: UGANDA! COOL! WHERE IS THAT?!

VOICE: AFRICA!

ELDER CUNNINGHAM: Oh BOY – Like Lion King!

LION KING CHARACTER: (Pg 13) Hey Na Da Hey Na! Aya Bubbu Taya Tayaaaaaaaaa!

VOICE: (Pg 11) Alright Elders, go home and pack your things! Tomorrow, your missions begin!

(Price looks a little uncomfortable. Cunningham looks thrilled) ***** The boys arrive in Uganda ***** The boys enter. They look around in horror at the poverty they see.

MAFALA: (Pg 17-18) (Big and happy) AHHH! There you are! I have been looking for you! I am Mafala Hatimbi. I’ve been hired to show you to your building.

ELDER PRICE: Oh, thank goodness! Some men took our bags!

MAFALA: In this part of Africa, we ALL have a saying – whenever something bad happens, we just throw our hands up to the sky and say HASA DIGA EEBOWAI!

ELDER CUNNINGHAM: Hasa Diga Eebowai?

MAFALA: It’s the only way to get through all these troubled times. There’s war, famine . . . but having a saying makes it all seem better . . . . There’s isn’t enough food to eat.

UGANDAN: Hasa Diga Eebowai!

MAFALA: People are starving in the street.

UGANDAN: Hasa Diga Eebowai!

ELDER CUNNINGHAM: Does it mean no worries for the rest of our days?

MAFALA: Kind of! We’ve had no rain in several days.

UGANDAN: Hasa Diga Eebowai!

MAFALA: And eighty percent of us have aids.

UGANDAN: Hasa Diga Eebowai!

ELDER PRICE: (Pg 19) Excuse me, what EXACTLY does that phrase mean?

MAFALA: Well, let’s see . . “Eebowai” means “God”, and “Hasa Diga” means (whispers behind a closed hand)

ELDER PRICE: WHAT???

ELDER CUNNINGHAM: (chanting and dancing) Hasa diga Eebowai! Hasa diga Eebowai! Hasa diga Eebowai! (continues)

ELDER PRICE: (Pg 22) (overlapping) Elder Cunningham. Elder Cunningham. Stop – Don’t say it! It means something very bad. (whispers behind a closed hand)

ELDER CUNNINGHAM: Holy Moly! I said it like thirteen times! **** Mafala’s daughter takes the boys to their living quarters *****

NABULUNGI: (Pg 22-23) This is where my father asked me to bring you. The others like you should be inside.

ELDER CUNNINGHAM: Thank you, Jon Bon Jovi.

ELDER PRICE: (giving Cunningham a look) We appreciate your help, Nabulungi. Look, uh, maybe sometime, Elder Cunningham and I could . . . Sort of tell you a little about the Church of Jesus Christ of Latter-Day Saints.

NABULUNGI: I have to get back to the village. But I am always there – if you want to talk to me. (She turns to go but then turns back) Just one piece of advice. No matter how hot you get at night, keep your windows closed. It is the only way to protect against the scorpions. And the mosquitoes. And the lions. And the murderers and the AIDS and the safari ants which plant their eggs under your skin and eat you from the inside out. (She walks away-the boys respond non-verbally)

ELDER PRICE: (big sigh, wipes his brow) Oh, man, can you believe this? (Pg 31) This is going to be a whole lot harder than we thought. ***** (Scene change - Later that week in a session with the tribespeople) *****

ELDER PRICE: (Pg 34-35) We would like to tell you all about a very special book.

UGANDAN: (major disappointment) Awww. . .

NABULUNGI: We all have heard of the Bible. People come and tell us about Jesus and him dying for our sins once a year!

KALIMBA: They come, tell us the story and then leave. Nothing gets better. Your bible doesn’t work.

ELDER PRICE: Those were Christian missionaries. We’re Mormons!

NABULUNGI: What’s the difference?

ELDER PRICE: I’m gonna take you back to Biblical times, 1823. An American man named Joe livin’ on a farm in the Holy Land of Rochester New York! (Cunningham steps forward like he’s doing an infomercial, over-acting)

ELDER CUNNINGHAM: You mean the Mormon prophet Joseph Smith?

ELDER PRICE: That’s right, that young man spoke to God.

ELDER CUNNINGHAM: He spoke to God?

ELDER PRICE: And God said, “Joe, people really need to know that the Bible isn’t two parts. There’s a part three to the Bible, Joe! And I, God, have anointed you to dig up this part three, which is buried by a tree on the hill in your backyard.”

ELDER CUNNINGHAM: Wow, God says, “Go to your backyard and start digging”? That makes perfect sense! (Pg 36) Wow! The Bible is actually a trilogy, and Book of Mormon is Return of the Jedi?! I’m interested.

ELDER PRICE: Now, many people didn’t believe the prophet Joseph Smith.

JOSEPH SMITH: (Pg 37) I speak to God all the time and he’s told me to head west! So I’ll take my part three to the Promised Land. Paradise! On the west coast.

ELDER PRICE: Now, on the way to the Promised Land, Joseph was shot by an angry mob. (Pg 40) The Prophet Joseph Smith died. But his followers, they kept heading west. And Brigham Young led them to a sparkling land in Utah they named SALT LAKE CITY. And there the Mormons multiplied! And made big Mormon families!! Alright, now who would like their very own copy of the Book of Mormon?? (All the Ugandan people look at each other for a beat and then walk away making groans and “blow off” gestures.”)

ELDER CUNNINGHAM: If you order now, we’ll also throw in a set of steak knives!

ELDER PRICE: What were you doing?! There’s nothing in the Book of Mormon about steak knives!

ELDER CUNNINGHAM: I’m sorry. I actually never read it. It’s so boring!

ELDER PRICE: (Pg 44) Africa is nothing like The Lion King. (dejected) There is nothing I can accomplish here! (Price walks away. Cunningham is not sure what to do or where to go).

NABULUNGI: (Pg 46) There you are! Thank goodness I found you! Where is your friend?

ELDER CUNNINGHAM: (sadly) I don’t have any friends.

NABULUNGI: Please come back to the village. We are ready! We’re ready to listen. YOU can lead us. Teach us everything about the Book of Mormon. ***** Scene change – Elder Cunningham is alone, preaching to the Ugandans*****

(Cunningham is reading from the book of Mormon. He is trying to be a preacher, but really doesn’t have what it takes)

ELDER CUNNINGHAM: (Pg 53) (reading with vigor) And it came to pass that the NEPHITES had gathered together a great number of men! And they did have a number of battles, in which the Nephites did beat the Lamanites and did slay many of them! (Cunningham seems to finish – the Ugandans just stare at him) Uh . . . that MEANS . . you know . . . You should . . be NICE to each other or something. (Pg 54) Let’s skip to another part . . .

(Cunningham turns and flips through the pages)

MIDDALA: THREE HOURS we been listening to him talk about STUPID [STUFF] that happened on the other side of the Earth thousands of years ago! IT has nothing to do with US!

SADAKA: That’s right! Those “NEPHITES” probably didn’t even have AIDS to deal with!

ELDER CUNNINGHAM: UH, SURE THEY DID! SURE THEY DID!! People back then had even WORSE AIDS! (Everyone quiets down and listens to him) Yeah! (Cunningham pretends to look through the Book of Mormon, and then pretends to read from it) And LO! The Lord said unto the Nephites – I know you’re really depressed, with all your AIDS and everything . . . But there is an answer in Christ! (The Ugandans look surprised, but they are now paying attention)

NABULUNGI: You see?! This book CAN help us! NARRATOR (CHORUS): (Pg 58) You’re making things up again, Arnold. You’re recklessly warping the words of Jesus!

ELDER CUNNINGHAM: (Pg 71) (with more confidence) And so, yeah, so then Christ said to the Nephites, “Be strong!” You know?! “Just because Lamanites got big Death Star weapons and stuff doesn’t mean they should ruin your lives! There’s more of you than there are of them, you know? You should always . . . stand up for yourselves,” Christ said.

MIDDALA: Jut like the way the Hobbits all stood up to Bringham Young’s killers! ******

MISSION PRESIDENT: (Pg 75) (reading a letter) Dear Mission President, it is my HONOR to inform you that the elders of Uganda District 9 have brought TWENTY NEW MEMBERS into the church . . . and our numbers continue to grow! (No longer reading) This is outstanding! [Elder Cunningham] has converted more Africans than any district in the COUNTRY! *******

ELDER CUNNINGHAM: (Pg 77) (reading a letter) It’s AMAZING. The mission president wants to meet ME personally! He’s going to give me a MEDAL!

ELDER PRICE: (Pg 80) Well, well . . If it isn’t the SUPER MORMON. Tell me how it is that YOU converted ALL those people into Mormons. (Pg 89-90) Joseph Smith dying of dysentery? Moroni from the Starship Enterprise? A bunch of made-up stuff (beat)

ELDER CUNNINGHAM: (about to cry) Boy . . . I really did it this time, huh? I mean . . . I’ve always been a screw up, but THIS –

ELDER PRICE: Wait a minute . . . You little SNEAK!

ELDER CUNNINGHAM: (confused) What?

ELDER PRICE: I thought I could fly in here and change everything. But I made it all about ME. While I was losing faith, you went and did something incredible. . . for a people who were unreachable – but then they were happy and hopeful . . . It doesn’t matter if the stories are true or not. That isn’t the point . . . ******

THE GENERAL: There have been RUMORS that the people in this village are uniting to oppose me!

MUTUMBO: (Pg 91-92) Yes, we have been shown another way!

THE GENERAL: There is ONE LAW you will obey here, and it is MINE!

MIDDALA: We believe in something ELSE!

ELDER CUNNINGHAM: Excuse me, everyone . . .

ELDER PRICE: You might as well PUT THAT GUN DOWN BECAUSE IT WILL NOT WORK. And if you do not get out of this village he WILL command the angel Moroni, on the death Star, to unleash the Kraken! Which will then . . . . Uh . .

ELDER CUNNINGHAM: Which will then – fire Joseph Smith torpedoes from its mouth of Christ!

ELDER PRICE: Oh – don’t think he can’t do it! (The General runs off) We are Latter-Day Saints. ALL of us. Even if we change some things, or break the rules, or doubt that God exists . . . We can still work together to make THIS our paradise. ***** The Ugandans pair up and go door to door spreading the word of Arnold ***** The Ugandans appear wearing white shirts and black ties

MUTUMBO: (Pg 97-98) Hello! My name is elder Mutumbo! And I would like to share with you the most amazing book!

UGANDAN 1: You’ve read the book of Mormon . . . Did you know there’s more?

UGANDAN 2: Part four! Have you heard the story of our prophet Arnold Cunningham?

ELDER CUNNINGHAM: Hello! We can fully guarantee you that . . . .

TOGETHER: This book will change your life. This book will change your life. This book will change your life. The book of ARNOLD. Hello!

LION KING CHARACTER: (Pg 13) Hey Na Da Hey Na! Aya Bubbu Taya Tayaaaaaaaaa!
```

---

## IC-1325: Born to Be Blue

- Title: Born to Be Blue
- Author (byline): Mark Bellusci
- Work: Off-Off Broadway Festival Plays – Series No. 27
- Publisher: Samuel French, Inc.
- Publication date as stated: 2003
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: RON, SAL, ASHLEY, GLORIA
- Teaser before the introduction: Yes
- Spoken words (computed): 1626
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mark Bellusci
Book: Off-Off Broadway Festival Plays – Series No. 27
ISBN: 978-0573629075
Publisher: Samuel French, Inc.
Date (Month/Year): 2003
```

### Introduction (context only: never use it for content warnings)

```text
Almost every parent has a master plan for their offspring – they call it the American Dream: Go to college. Find a career you can commit to – doctor, lawyer, businessman. Get married, have kids, buy a house, retire, then watch your kids perform the same feats, in the same order. But what you belong to a family with a different master plan?

Get ready to turn parental guidance on its head. Ron's parents want him to succeed...at underachieving. They do everything in their power to keep him away from libraries, books and intelligent, motivated young women like his girlfriend Ashley. Instead they encourage him to spend his time at monster truck rallies, playing pool, and applying to technical college. Born to Be Blue by Mark Bellusci
```

### Performance text (classify this)

```text
RON: Look, I'm not trying to spite anyone. I just --

SAL: No? What do you call it when you crush your parents' dreams?

RON: I call it the truth.

SAL: Truth?

RON: Because it's what I want to do. It's my life.

SAL: So you're going to [throw] it away--

RON: [Throw] it away? You call going to (hesitates to say the word) . . . . I know what I'm doing.

SAL: You can't know. Don't you understand? You're too young to see-

RON: Look, this isn't permanent or anything. It's a four-year stint

SAL: Take it, and you're stuck for life.

RON: But I can do anything I want--

SAL: Anything you want. That's a laugh.

ASHLEY: Excuse me, I’m sorry for jumping in, but ... what are we talking about here?

RON: It's okay--

ASHLEY: No, it's not okay. I mean, Ronnie has done something you should be proud of, and you're treating him like he killed someone.

SAL: Himself, if he takes this stint.

ASHLEY: "Stint?" It's four years at--

RON: Shhhh. They don't like to use its name in the house.

ASHLEY: They don't want to hear the word, “Harvard?”

GLORIA: Ohhhh! (Sal makes a disgusted face.)

ASHLEY: What could you possibly have against Harvard?

RON: Harvard, Yale, Princeton, they hate them all.

ASHLEY: Is ... is this one of those undercover video shows? Sure, you're a couple of out-of-work actors, right? (Looking around.) Come on, where’s the camera? Where’s the hack comedian host? I mean, Harvard! The best college in the world!

GLORIA: That's what they want you to believe.

ASHLEY: Do you know how many people would die for that scholarship?

GLORIA: How could a kid with a D-plus average get into Harvard on a full scholarship?

RON: I, uh, I doctored my report cards to make A's look like D's.

ASHLEY: (Proudly.) Ronnie scored the highest on the state aptitude test.

SAL: Did you at least cheat?

RON: I tried, but everyone else was putting in wrong answers.

GLORIA: That's because everyone else was listening to their parents, not sneaking around libraries.

ASHLEY: This is crazy. Absolutely--

GLORIA: What do you think happens when you go to Harvard?

ASHLEY: (Sarcastic and rhetorical.) You get a ... great education? Then, youuuu ... start your career.

SAL: Ugggh. (Gloria winces.)

ASHLEY: (To Ron) That's another word I can’t say? (Ron shakes his head no.) Okay, like, so what are you supposed to do after college?

GLORIA: Get a job.

ASHLEY: Job, career. What's the difference?

SAL: The difference is, a job, you do your eight hours and go home.

GLORIA: A career, you sacrifice your family, your leisure, your life, to "achieve" something.

SAL: A job you [complain] about, a career you see a therapist about.

ASHLEY: All right, so Ronnie will choose a job instead of a career. Fine. It's still--

GLORIA: This job he'll choose--you think it'll be high paying?

ASHLEY: It will if he comes out of Harvard.

GLORIA: And what color you think his collar will be?

ASHLEY: I don't know, shirts come in a lot of colors--

SAL: You think he's going to push paper or a broom?

ASHLEY: Paper!

SAL: Ah ha!

ASHLEY: Ah ha?

SAL: A white collar waste.

GLORIA: Headaches, ulcers, and a down-size away from a pink slip.

RON: Yeah, but the pay--

GLORIA: Less than minimum wage when you consider unpaid overtime.

SAL: Never mind the costs for a therapist . . . stress management sessions--

ASHLEY: Soooooo .... you want Ronnie toooooo .... not work?

GLORIA: Of course he'll work.

SAL: This country was built on work. Blue collar work.

ASHLEY: O ... kay. (Sarcastically.) So Ronnie should just forget about college.

GLORIA: Absolutely not.

SAL: We've got a good school picked out for him. (Clearing his throat, then intimidating a bad TV actor.) "How did I get this wonderful job?" (Continuing the TV actor imitation.) "It all started the day I enrolled at Technical Career Institute."

GLORIA: Where Ronnie can learn to drive a dump truck.

SAL: Walk on to any construction site, and you’ll be driving a dump truck in minutes.

GLORIA: Now that's a skill nobody can take away from you.

ASHLEY: What kind of life is that?

SAL: Are you kidding me? Best life there is.

GLORIA: Start at nine, home by five.

SAL: Talking sports with the guys.

GLORIA: Plenty of coffee breaks.

ASHLEY: But where’s the challenge?

SAL: "Challenge?"

GLORIA: (To Sal) It’s the high school counselors. They brainwash them.

ASHLEY: So instead of having a comfortable career in a nice office, you want him struggling to make money--

SAL: Struggling? You know what a good dump truck driver gets?

RON: Peanuts. I looked up their salary range.

GLORIA: You look at their overtime? Doubles the salary,

SAL: Now when was the last time some Harvard guy got overtime?

RON: Hey, with their salaries, they don't need it.

SAL: Oh yeah? And you think that Harvard guy gets to see any of that money?

GLORIA: (Delivered fast and in monotone.) Harvard guy pays for Harvard cars, parked in four-car Harvard garages, attached to thirty-two-room Harvard mansions, housing Harvard-to-be kids and a Harvard-kept wife.

SAL: So at the end of the week, this rich Harvard guy's got just enough money left to buy a hot dog for lunch, and save the bun for dinner.

RON: And what, the blue collar guy doesn't have money problems?

GLORIA: Absolutely not.

SAL: He goes home, has dinner, goes to the kid's ball game, goes to Dairy Queen, goes to bed.

GLORIA: Clean, simple, affordable.

SAL: It's not too late, son. Classes that start Thursday could have you driving by Friday.

RON: What about the boredom? The same old thing, day in and day out?

SAL: No no no. See, you only get bored if you overdevelop your brain and start expecting more.

GLORIA: So many lost. What does it say for our country? (Pause.)

ASHLEY: Tell them. You tell them, or I will

RON: (Sighing.) This summer-- I'm going to-- I took a job.

SAL: You took a job. (He takes out his pocket knife and holds it out to Ron) Here. Just insert it between the third and fourth vertebrae.

GLORIA: I don't understand. We had your summer all planned. Get up at noon, hang on a street corner, go to the video arcade, see cheap horror movies, then shoot pool all night.

RON: I know, ma, but-- It's just that, I want to do something with my life.

SAL: You want to "do" something? Breathe in, breathe out, eat, sleep, [have] babies. Just let it happen.

ASHLEY: But you can’t just let a career "happen." You’ve got to prepare for it, go to school for it.

GLORIA: (To Sal) Told you we should've done home education.

SAL: All right, all right. (Beat. He sighs.) So what's this wonder job you got? Bartending, cutting lawns, what?

ASHLEY: (Proud and defiant.) Ron has been awarded one of only two internships at the city’s largest law firm, Huff, Puff and Blowdon.

SAL: It's all over.

GLORIA: Don't you understand? They get their claws into you, they’ll never let go.

RON: It’s a great paying job, and I get credits towards college.

SAL: (Offering his head to Ron) Here, hit me in the temple. Make it fast and hard, and I’ll be out of my misery in seconds.

RON: Pop, try to understand--

ASHLEY: (Angry.) How could two parents hold their son back from a chance of a lifetime? Aren’t you supposed to want more for your son? Why should he settle for a blue collar job like yours?

RON: See, that’s the thing. They’re not blue collar people. My father’s a college professor, and my mom’s a senior vice president at IBM. (Beat.)

ASHLEY: What--? I don’t-- Then why won’t you let Ronnie have what you had?

SAL: Have what we?-- you know what we had?

GLORIA: Anxiety. Between his trying to get tenure.

SAL: And her never-ending trip up the corporate ladder. Barely saw each other the first ten years of marriage--and when we did, we didn't know what to do with ourselves.

GLORIA: Probably would've gotten divorced.

SAL: If we had the time.

GLORIA: Driven by our “careers”

SAL: Wanted to “do something” with our lives.

GLORIA: By the time we looked up, we weren’t kids anymore. Then, out of the blue, the baby clock kicked in.

SAL: We figured, have a few, hire a nanny, see the kids on weekends.

GLORIA: Be a good career move -- kids make a great impression at corporate outings. We scheduled a procreation appointment once a month.

SAL: That’s when we learned, some things you can’t plan for.

GLORIA: Like trying to create a kid on a deadline.

SAL: Our estimate for [a] baby was off.

GLORIA: Eight years off.

SAL: Well, eight years of trying does things to a couple. Because it-- it made us stop. And look at the way we were living. Constantly maneuvering to see what the next career move would be. And constantly looking over our shoulders to see who was gaining on us. (Pause.) So, we decided. [Forget] the career crap.

GLORIA: And [forget] the baby crap.

SAL: We were going to start living. Quit the jobs, sell the condo -- See the country.

GLORIA: We had enough saved. At least for a while. Then, after a few years, if the money got tight--

SAL: We’d take jobs. Job jobs.

GLORIA: Pay-the-bills jobs. Secretary.

SAL: (Dreamily.) Night watchman. Look at a few closed circuit cameras, sip some coffee, read my books -- and get paid for it? Man.

GLORIA: So that was our plan. And suddenly, everything was fun. We figured, if we wanted kids, we'd adopt. We were finally in control.

SAL: (Chuckling.) Yeah, for about a month. See, acting like teenagers did for us what eight years of planning couldn't do. (ruffles Ron’s hair – Ron was the product of less stress and more time)

GLORIA: (shrugs her shoulders) And all those fun, new plans, out the door. So, I stayed at IBM.

SAL: And I kept on at the college.

GLORIA: I was going to quit my job [but] your father got [caught up] in a politics game and wasn't granted tenure. (To Ron) Then you came along. And that sealed it, we were playing house for keeps.

SAL: So we put up with the long hours, the political backstabbing, the mind-numbing nonsense of white collardom-- But our children don't [have to].

GLORIA: Because a simpler life starts with a simpler job.

RON: It's -- It's too late, mom. I’ve already accepted the scholarship.

SAL: You raise them, you try to teach them--

RON: Pop, I -- I have to try this. But if it doesn't work – If it doesn’t work . . . I’m – I’m still wearing . . . the belt. (Ron lifts his shirt to reveal a carpenter belt filled with tools –)

SAL: (Sal and Gloria burst into smiles) [His carpenter’s belt!] He’s till our boy, Gloria. (Pause while Sal thinks, then he walks to the door and ushers Ron and Ashley out with these words) Go ahead, see what the "career life" is all about. And when you're sick of it, we'll be here for you. (Closes door, leans against it and sighs)

GLORIA: It's just a phase, dear. He'll be back. And when he does, he'll be that much farther up the union apprentice list.
```

---

## IC-1326: The Boss Baby

- Title: The Boss Baby
- Author (byline): Not specified
- Work: Not specified
- Publisher: Simon Spotlight
- Publication date as stated: Feb 2017
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: TIM, DAD, BOSS BABY, MOM, FRANCIS
- Teaser before the introduction: Yes
- Spoken words (computed): 1929
- Already set (do not supply): none

### Source block (context only)

```text
Author: Adapted by Tracey West – based on the DreamWorks Animation movie written by
Michael McCullers
ISBN: 978-1481470063
Publisher: Simon Spotlight
Date (Month/Year): Feb 2017
```

### Introduction (context only: never use it for content warnings)

```text
Boss Baby adapted by Tracey West – based on the DreamWorks Animation movie written by Michael McCullers
```

### Performance text (classify this)

```text
Adapted by Tracey West based on the DreamWorks Animation movie written by Michael McCullers.

TIM: (Pg 1-3) My name is Tim, and this is my story. It starts when I was seven years old. It was just the three of us – the Templetons. Me, Mom, and Dad. I was the star of the Templeton family show and I had the greatest parents ever. They had the coolest jobs! They worked for Puppy Co. and got to test out all the new products for puppies. Every night, we had our special bedtime ritual. Three stories. Five hugs. They would tuck me in and I would drift off to sleep, perfectly content. Then one night something different happened. Mom and Dad read me three stories. They gave me five hugs . . . Then . . .

DAD: Hey, Tim, how would you like to have a baby brother?

TIM: That’s when everything changed . . .

TIM: (Pg 4-5) The day I got a brother started out like any other day, but little did I know that my life would never be the same. My parents always said that I had an overactive imagination, but I clearly remember that he was delivered in a taxi. (Tim peers out his bedroom window in shock) He walked past my bicycle and kicked it over. Then he strutted excitedly up to the front door. I ran downstairs. Mom was holding Boss Baby in her arms, just like he was a normal baby.

DAD: (smiling) Tim, meet your new baby brother.

TIM: Baby brother? Who is this guy? Why is he so fat? Why’s he staring at me? What’s going on? But before I could ask any of them.

BOSS BABY: (crying loudly in a rather fake adult voice)

TIM: Right from the start he was yelling at people, ordering everyone around. One thing was clear, he was the boss. ****** dinner time a few months later the parents are feeding the baby ******

MOM: (Pg 7-10) Who’s Mommy’s little cutie?

DAD: No, he’s Daddy’s little tough guy, right?

TIM: (to audience) I couldn’t take it anymore! (to parents) Ugh! We need to talk. In private!

DAD: About what, bud?

TIM: About the B-A-B-E-E.

MOM: Y, Tim.

TIM: Why? Because he came out of nowhere. We don’t even know him. How can we trust him? Seriously, am I the only one who thinks there’s something weird about this guy? Look at him! He wears a suit!

MOM: I know. Isn’t it cute. He’s like a little man.

TIM: He carries a briefcase. Doesn’t anyone else think that’s a little freaky?

DAD: (smiling) Well, you carried about Lam-Lam until you were like . .

TIM: This is not about Lam-Lam! He’s taking over the whole house!

MOM: (To baby) Are you taking over the whole house? Yes, you are! Yes, you are!

BOSS BABY: (Giggles and coos until Mom looks away, then turns to stare at Tim and nods deliberately with an evil look on his face)

TIM: I knew it! He DID understand everything we were saying . . . (Pg 11-13) That night [after] Mom and Dad were already asleep I heard a phone ring. (Tim tiptoes to the baby’s room and peeks around the door frame)

BOSS BABY: (in a deep adult voice talking on a toy phone) I’m making great progress with the parents already. Sleep deprivation, hunger strikes. They’re very disoriented. I’ve got them eating out of the palm of my hand. But I think the kid might be onto me . . . No, I can handle him. You got the right baby for this job.

TIM: (flipping on the light switch and jumping into the room) Hands up!

BOSS BABY: (drops the phone and in a baby’s voice) Fart! Poop! Doodie!

TIM: You can talk!

BOSS BABY: Uh, goo-goo ga-ga.

TIM: No. You can really talk. I heard you!

BOSS BABY: (in his adult voice again) Fine. I can talk. (Pg 38) The truth is, I’m no ordinary baby. I’m on a mission from above. I’m middle management for the company.

TIM: The company? What company?

BOSS BABY: (Pg 40-41) Baby Corp.

TIM: Where babies come from?

BOSS BABY: Of course. What did you think? The stork? Magic fairies? If people knew where babies really came from they’d never have one. Same thing with hot dogs, by the way. . . After normal babies get their pacifiers taken away, the forget all about Baby Corp. A few of us are selected for the ultimate honor . . . Upper management! We drink a super secret baby formula that keeps us babies forever. (Pg 13-14) Let’s just say . . . I’m the boss

TIM: But you’re a baby. You wear diapers.

BOSS BABY: (he walks over to the closet, pushes aside a box of diapers, revealing a safe. He spins the combination, and takes out a bottle) SUPER SECRET BABY FORMULA (he mixes himself a bottle and takes a long drink, wipes his mouth and speaks again) You know who else wears diapers? Astronauts and race-car drivers, that’s who. It’s called efficiency, Templeton. The average toddler spends what – 45 hours a year on the potty? I’m the boss. I don’t have that kind of spare time.

TIM: Well, you’re not the boss of me!

BOSS BABY: I AM the boss of you.

TIM: Are not

BOSS BABY: Am too

TIM: Are not

BOSS BABY: Am too

TIM: Are not! I was here first. Just wait till Mom and Dad find out about this.

BOSS BABY: (pointing his finger in Tim’s face) Oh yeah? You think they’d pick you over me? With your track record? (Takes out a clipboard from under his blanket) Says here your grades are mostly C’s. You can’t ride a bike without training wheels. Even bears can ride bikes without training wheels. . . . Date of birth says you’re seven. You’re old. It’s time to make way for the next generation. It’s the way of the world.

TIM: Mom and Dad don’t even know you. They love me!

BOSS BABY: Oh yeah? Do the math, kid. There’s only so much love to go around. There’s not enough love for the two of us. There’s no place for Tim! Tim doesn’t fit anymore. So keep quiet, stay out of my way, or there’s gonna be cutbacks.

TIM: (uncertainly) You can’t be fired from your own family. (to audience) I left Boss Baby’s room and went back to bed. I fell asleep with no stories and no hugs. What if you could be fired from your family? ********** The Baby meeting (aka play date) *********

TIM: (Pg 19-24) The next morning, I felt a whole lot better. I had a plan! All I had to do was prove to my parents that Boss Baby wasn’t a real baby. Then they would send him back to the baby store (or whatever they called that weird place he came from). I jumped out of bed, grabbed a microphone and recorder, put on my spy gear, complete with spy glasses, a mask, and mittens and made my way down the hallway. Everything was going smoothly until I stepped on one of the baby’s toys and tumbled down the stairs. (Tim looks around him in shock) I was surrounded by babies! Mom? Dad? What’s going on? It’s an invasion!

MOM: It’s a play date! (Mom exits to the kitchen to join the other parents)

BOSS BABY: (in his adult voice) It’s a meeting . . . and you won’t be attending. (to the other babies) Thank you for coming here on such short notice. We babies are having a crisis. Teddy, if you please. (He picks up a teddy bear and tilts its head back revealing a projector) (as the film rolls) You see, babies aren’t getting as much love as we used to. Behold, our mortal enemy: puppies! Throughout history, people have loved babies more than anything in the world. Puppies were merely . . accessories. But that all changed when the puppies began coming out in designer models. Remember the Labradoodle? The Peekapoo? And things are getting even worse. Francis Francis, the CEO of Puppy Co made this announcement. Teddy, roll the clip.

FRANCIS: Puppy Co is about to release the most adorable puppy ever. (Pg 69) The Forever Puppy! Imagine a puppy that never gets old. Never grows up. A puppy that stays a puppy forever. It’ll be sooooo adorable! (Pg 24) It’s going to crush the competition!

BOSS BABY: NO! We are the competition. This is war! Puppies are winning and babies are losing. And if this puppy is as cute as we fear, it could put the baby business out of business, baby. ***** later that night – Tim and Boss Baby are alone in the nursery****

BOSS BABY: (Pg 46-51) The Pet Convention is in two days and I’ve got nothing . . . I could get fired!

TIM: Hey, relax. I’m sure there’s other cool jobs for babies, right. Meanwhile, two days goes by like that. You’d better start packing.

BOSS BABY: You don’t get it Templeton! If I’m fired, they’ll take away my formula! I’ll turn into a normal baby and then live here forever with you. Every morning you wake up, I’ll be there. Every night at dinner, I’ll be there. Every birthday party. Every Christmas. I’ll be there. Year after year. We’ll grow old together. We’ll be brothers. Always!

TIM: Noooooo! You can’t stay here. We have to fix this. We have to make sure you don’t get fired. I will help you. But just to get rid of you. Deal?

BOSS BABY: Deal. Here’s to never seeing you again. Now let’s get to work.

TIM: (to audience) We had to move fast. I carried Boss Baby down to the living room. Both my parents had fallen asleep on the couch, in the middle of doing work stuff. Their Puppy Co files were scattered on the coffee table. PERFECT! (They begin to search through files.) Wait a second. This is it! (Tim holds up a flyer) Check it out. It’s for Puppy Co’s Take Your Kid to Work Day! [TOMORROW!] We can get inside Puppy Co! TRANSITION The next day Mom and Dad take Tim and Boss Baby to work with them. And while Mom and Dad are busy working . . . they find the office of FRANCIS FRANCIS for the ultimate confrontation!

FRANCIS: (Pg 69) (evil laugh) Once I launch my Forever Puppies, no one will ever love a baby ever again! The end of babies . . . the end of Baby Corp!

BOSS BABY: (Pg 67-69) (Boss baby stops sucking on his bottle and recognizes Francis) Super Colossal Big Fat Boss Baby? How did you end up here?

FRANCIS: A long, long time ago, I was a hot-shot executive, headed straight to the top! They gave me a promotion . . the corner office . . . my very own

BOSS BABY: Personal potty?

FRANCIS: Everyone loved me. I had it all. It thought they loved me. But I was wrong. They fired me and took away my special formula. Then they sent me down to live with a f-family. Baby Corp stole all the love from me, and now I’m going to take it back with . . . the Forever Puppy.

BOSS BABY: (Pg 70-71) Ha! A puppy that never grows up is impossible.

FRANCIS: You’re right. Why, you’d need some sort of . . . youth formula. (Francis grabs Boss Baby’s bottle)

BOSS BABY: My super secret baby formula! You’ll never get away with this.

FRANCIS: (Pg 93) Baby Corp is through! I win! Ha!

BOSS BABY: Wrong!

TIM: Boss Baby grabbed [his SUPER SECRET BABY FORMULA] from Francis Francis and handed it to me. I knew just what to do with it. I shoved it into Francis’s mouth. For the first time in many years, that big baby was back! (Pg 100) He wasn’t a businessman anymore. The formula had turned him back into a fat little baby again.

FRANCIS: (sucking his thumb) You ruined everything! It’s not fair! It’s not fair! ********

TIM: (Pg 102-103) Boss Baby and I had done it. We had saved Baby Corp. So we both should have been pretty happy right? But I really wasn’t. Because it was time for Boss Baby to go back to Baby Corp. (to Boss Baby) Congratulations on your promotion. The corner office, the private potty, all that stuff.

BOSS BABY: But hey, how about you? You have your parents all to yourself.

TIM: So, what am I gonna tell Mom and Dad after you leave?

BOSS BABY: Don’t worry. Baby Corp has a procedure for situations like this. It’ll be like, uh . . . I was never born.

TIM: (Pg 105-1068) (to audience) A bunch of Baby Corp. workers came and got rid of everything that was Boss Baby’s. Every toy, every pacifier. They used a wand to erase my parents’ memories. They offered it to me, but I refused. I wanted to remember Boss Baby. I missed him like crazy. The cute way he drooled. Our adventures together. I wrote him a letter. Dear Boss Baby, It turns out there’s plenty of love to go around. And to prove it to you, I would like to offer you a job. It will be hard work and there will be no pay. But I promise you this: Every morning when you wake up, I will be there. Every night at dinner, I will be there. Every birthday party, every Christmas morning, I will be there. Year after year after year. We will grow old together. And you and I will always be brothers. I sent the letter to Baby Corp . . . I didn’t hear anything . . . then one morning . . . . a taxi cab turned down my street.

MOM: Tim, look who’s here!

DAD: It’s your new baby . . .

TIM: BROTHER! (to audience) I stared into the eyes of my baby brother. I knew he was going to take over the whole house and boss everyone around, day and night . . . and I wouldn’t have wanted it any other way.
```

---

## IC-1327: The Boy Who Fell into a Book

- Title: The Boy Who Fell into a Book
- Author (byline): Alan Ayckbourn
- Work: Not specified
- Publisher: Faber and Faber
- Publication date as stated: Mar 2001
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: KEVIN, DAD, VOICE, ROCK, MONIQUE, LITTLE MAN, WOMAN, BOTH, WOLF, R-HOOD
- Teaser before the introduction: Yes
- Spoken words (computed): 1197
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alan Ayckbourn
ISBN: 978-0571203345
Publisher: Faber and Faber
Date (Month/Year): Mar 2001
```

### Introduction (context only: never use it for content warnings)

```text
I admit it. I love to read. Getting lost in a good book is one of my favorite things. But in this selection, if you are lost in a story, bookmarks are useless and page numbers become portals. Buckle up, because Kevin’s literary shenanigans are about to begin. Can he and Rockfist Slim save the world one story at a time?

The Boy Who Fell into a Book by Alan Ayckbourn
```

### Performance text (classify this)

```text
Kevin’s bedroom – Kevin is in bed, reading aloud.

KEVIN: (Pg 1-3) . . . Rockfist Slim, ace detective, fought like a crazed tiger. Whap! One evil-looking opponent crashed to the ground. Aaargggh! Another thug flew helplessly through the air, victim to our hero’s well-oiled combat skills. But still they kept coming. The underworld leader known only as the Green Shark was taking no chances. Eventually, sheer numbers bore Rockfist to the ground (gasp) Semi-conscious but still struggling, Rockfist was dragged across the concrete floor. A door clanged behind him. (clang) Rockfist found himself in deep, impenetrable darkness . . .

DAD: (off stage) Kevin! It’s half past ten. Go to sleep. I’ve told you before, if you want to read, read in the daytime.

KEVIN: (disgruntled) Yes, Dad. (turns off the light, waits a few seconds then switches it on again)

DAD: (immediately) Kevin!

KEVIN: (swiftly switches off the light, grumbling) How can I sleep till I know what happens to Rockfist? He’s trapped. He could be dying! (he ponders as he drifts off to sleep) The trouble with a book . . . a good book . . . it’s inside your head . . . and you’re like inside the book . . . it becomes (yawn) . . . part of you . . . (yawn) really real . . .

KEVIN: (Pg 3-7) (clearly dreaming of falling; he awakes suddenly when he hits the ground)

VOICE: (from the darkness) Hold it right there, kid.

KEVIN: (jumping) Who’s that?

VOICE: (lying) I’ve got a .45 pointing straight at you. Put up your hands and throw down your gun.

KEVIN: I can’t. I haven’t got a gun. (he holds up his arms and show his empty hands)

VOICE: Who are you? What are you doing here?

KEVIN: My name is Kevin Carter and this is my bedroom. (suddenly doubtful) At least it was a minute ago. Who are you and what are you doing here?

ROCK: (click of a cigarette lighter; Rockfist steps onstage) The name’s Rockfist Slim, kid.

KEVIN: (in wonder) You’re Rockfist Slim? Rockfist Slim? (quickly figuring it out) You’ve been shut in here by the Green Shark’s men, haven’t you?

ROCK: (menacingly) How do you know about the Green Shark?

KEVIN: (rapidly) I was in bed reading a book called Rockfist Slim and the Case of the Green Shark and dad told me to turn out the light, and then suddenly I was falling, and the next minute I ended up here. I seem to have – fallen in. (excited) We’re both in a book!

ROCK: Listen. I have less than 72 hours before the Green Shark destroys half the planet. (Pg 8-9) and I’m trapped in here with a lunatic kid. I don’t even like kids. I hate kids. Get off my planet.

KEVIN: I’ll do a deal with you. If you help me get home – I’ll help you solve your case. I have your book. I could skip on ahead – find out what happens.

ROCK: Could you find out the identity of the Green Shark? If I knew his identity I could stop him.

KEVIN: (Pg 10) Is it a deal?

ROCK: (reluctantly) It’s a deal. (they shake hands) Now stand back. I’m going to charge that door. (he rushes the door, bounces off and returns clutching his shoulder) Let’s start looking for another way out. (Pg 15-16) (they start to move off. Monique appears and blocks their path)

MONIQUE: (French, beautiful, with a gun) Monsieur Rockfist Slim, quel pleasant surprise.

KEVIN: (under his breath) It’s Monique La Sleek, deadly #1 henchperson of the Green Shark - blackmailer, thief and murderer. (ominous sound effect)

ROCK: Run for it, kid! (Pg 20) (they rush out – a whirl of sound and we are in a new location – a forest – they look around bewildered) (Pg 39-40) Is this your bedroom?

KEVIN: I don’t have trees growing in my bedroom. Do you think Monique’s following us?

ROCK: I wouldn’t be surprised. . . (Pg 43) I know too much. (Pg 40) What books have you got with forests in them?

KEVIN: I don’t know. Dozens.

ROCK: Dozens? (looking at his watch) I can’t spend time going through dozens of books! (Pg 41) I mean we could be anywhere from Huckleberry Finn to The Boys’ Book of Nature Walks.

LITTLE MAN: (Pg 42) (hopping on one leg, gleefully) Today I back, tomorrow I brew,
The next I’ll have the young Queen’s child.
Ha! Glad I am that no one knew,
That Rumpelstiltskin I am styled. (he hops off)

ROCK: What in the heck -- ?

KEVIN: That’s where we are! Grimm’s Fairy Tales. (beat) Look! Through the trees. It’s a cottage. In the clearing. (Pg 44-45) (They reach the cottage – Kevin knocks – no answer – he tries the door handle – CREAK – the door swings open) Hallo! Anyone home? (to Rock) Come on. Let’s look inside! (Rock follows Kevin inside)

ROCK: Kid, listen. I might not read much, but I know this. No good comes of pushing your way into cottages in the middle of deep woods. In my experience, 20 minutes later 3 angry bears show up.

KEVIN: I wonder if there’s any food. I’m hungry.

ROCK: Don’t touch the food! You eat it, you’ll turn into something. Or you’ll shrink. You’ll be 2 inches high, going through little doors and meet caterpillars . . .

KEVIN: That’s Alice in Wonderland.

ROCK: These are dangerous places, kid. Before you know it, you’re kissing frogs, dogs are singing, and giants aren’t far away.

WOMAN: (Pg 46-47) (appears behind Rock, stands watching him until he turns in fear)

Hallo, my friends, please have no fear, For you are very welcome here.

ROCK: (out of the corner of his mouth) Kid . . . hey, kid. Hey! (to woman, clearly unnerved) All we really want are some directions, ma’am.

WOMAN: (silence creepy staring)

ROCK: Why don’t she answer me?

KEVIN: I’ve just remembered. Grimm’s fairy tales is in verse. That may be the only way she’ll understand us.

WOMAN: Do come inside and take a seat. My granddaughter you soon can meet. (She goes out)

KEVIN: (Pg 49-50) Only to talk to her. If we don’t talk in rhyme, she won’t know what we’re saying.

ROCK: Who is she? Any clues? There’s no sign of a bear and she certainly ain’t Snow White.

KEVIN: She’s not the witch from Hansel and Gretel. Otherwise this house would be made of gingerbread.

ROCK: Didn’t she say something about meeting a granddaughter?

BOTH: (simultaneously) Little Red Riding Hood!

WOMAN: (returns with a tray and 2 glasses of lemonade) The larder’s empty I’m afraid. Just biscuits and some lemonade.

ROCK: Don’t touch the drink! She’s spiked it!

KEVIN: What do we do? (to Woman) Much as we’d really like to stay . . . (looks to Rock)

ROCK: I guess we must be on our way . . .

WOMAN: No, no, this lemon drink is yours. I squeezed them with my own two . . . hands. (a unsuppressed snarl, she pushes back her bonnet to reveal two large ears)

ROCK: (Pg 51) Here come the ears! (to Kevin) Let’s go!

KEVIN: She’s a wolf! (a loud knock on the door)

WOLF: (Pg 52-53) (drops the disguise completely) Now, not one word from you or him--
Or I will tear you limb from limb. (moves to the door)
(in a Granny voice) My dear, you’re just in time for tea,
Your granny has come company.

R-HOOD: Oh Grandmama, you’ve such big ears,
I never noticed, all these years.
And great big hands and, oh, good grief,
You’ve also got enormous teeth!

ROCK: (Pg 55) This girl’s beyond belief (rushing to R-Hood) This ain’t your gran, kid, it’s not her, Unless she’s grown a coat of fur!

KEVIN: (Pg 51) She’s a wolf! (Pg 56) Granny’s dead.

ROCK: (quickly rhyming so R-Hood can hear) He ate her whilst she lay in bed.

(R-HOOD runs away frightened and screaming as the WOLF turns on Rock and Kevin snarling furiously)

ROCK: (Pg 57-58) Let’s get out of this place, I’m running out of rhymes. Take my arm here, friend, Your bedroom’s just around that bend. (They exit in a rush as a clap of thunder echoes – they find themselves in an old dark house - spooky)

KEVIN: (Pg 85) (looking around cautiously) I wonder where Monique is? We may have lost her.

ROCK: Possibly. But knowing her, she’s gone on ahead of us. She’s waiting for us in the next chapter. (wind whistles through a broken window) (Pg 91) Where are we now? Break it to me gently. Frankenstein’s castle? Edgar Allen Poe land. The Addams Family Home? (thunderclap)

KEVIN: I think it’s my book of ghost stories!

BOTH: Wah! (crying out they both race off in opposite directions)

KEVIN: (Pg 99-100) (racing back on stage – we are back in his bedroom) I don’t believe it. It’s my room! I’m home. I’m home! The book. I need the book. (he grabs it from his nightstand and quickly leafs through the pages) Rockfist Slim and the Case of the Green Shark.

MONIQUE: Welcome home, Kevin.

KEVIN: (freezing) Monique! (conceals the book) What are you doing here? What do you want?

MONIQUE: (Pg 101-102) I want you to take that book and burn it, Kevin.

KEVIN: If I destroy the book, won’t it destroy everything in it. Rockfist? You? The Green Shark. I’ll destroy everyone.

MONIQUE: If you finish the book, you will find that I, Monique, die anyway. Killed by the indestructible Rockfist. How do you think it feels to be this superior being, moi, brought down by this gum-chewing little troll? This time, if I die – he will also die!

KEVIN: (throwing the book at Monique’s feet) You want him dead, you kill him. (Monique hesitates) (Pg 103) You can’t, can you? You can’t even pick it up. You can’t touch anything here, can you? Not in my world. You don’t belong here. You belong in the book. In the real world, you can’t hurt me at all. You can’t hurt anyone.

MONIQUE: I warn you, Kevin, I will –

KEVIN: Don’t threaten me! Get out of my room! Get out of this house!

MONIQUE: (as she goes) Keviiiinnnnn! (shifts to another voice)

DAD: (Pg 107) Kevin! Kevin! Is that light of yours still on!
```

---

## IC-1328: Breast Men

- Title: Breast Men
- Author (byline): Bill Bozzone and Joe DiPietro
- Work: Act One '95: The Complete Plays, Pgs 27-40
- Publisher: Smith and Kraus
- Publication date as stated: June 1996
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: LLOYD, STUART
- Teaser before the introduction: No
- Spoken words (computed): 1872
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bill Bozzone and Joe DiPietro
Book: Act One '95: The Complete Plays, Pgs 27-40
ISBN: 978-1880399972
Publisher: Smith and Kraus
Date (Month/Year): June 1996
```

### Introduction (context only: never use it for content warnings)

```text
Stuart and Lloyd are lifelong best friends who've gone away for a men's weekend to help Lloyd

(a beefy fireman) get over his recent breakup with a busty girlfriend. A travel agent mistakenly booked them into a room at Love Acres, a romantic retreat in the Poconos, and their original plans to drink beer, watch old movies, hang out by the pool and do guy things are disrupted when Stuart (a lonely fire dispatcher) makes a confession. A medical condition has caused Stuart to grow womanly breasts and he needs money for an operation to fix it.

Breast Men by Bill Bozzone and Joe DiPietro
```

### Performance text (classify this)

```text
LLOYD: God, this is so perfect. Oh! It's better than the brochure even! You'd have to be made of stone not to lose your heart in a place like this. (Stuart enters, He looks around, astonished)

STUART: You've got to be kidding. This is somebody's idea of romantic?

LLOYD: I think it's spectacular!

STUART: What kind of sick female came up with this place?

LLOYD: Leave it to you, a man, not to appreciate a love shrine like this! Oh God, if only Sara was here . . . (Lloyd moves to the phone, dials.)

STUART: Lloyd, she left you three and a half weeks ago, and since then you've done nothing but whine and grovel . . .

LLOYD: (Into phone.) Sara, I know you're checking messages!

STUART: Lloyd, don't!

LLOYD: Guess where I am?! Does the name Love Acres mean anything to you? That's right! I came up here without you! Yeah, I carne up with a big, fat waitress I picked up at Stuckey's! She looks just like Sally Struthers in those Feed the Children commercials! She's beautiful! I'm lying! It's me and Stuart! You can imagine how much fun that is! (Stuart starts to pull the phone away from Lloyd.) - call me! I'm dying here! (Stuart manages to grab it and hang up.)

STUART: Lloyd, I will not allow you to do this to yourself! Pull it together! Listen, I know women, I've been through plenty of' em!

LLOYD: You haven't had a date in eighteen months.

STUART: Hey! That's because I'm choosy! And let me tell ya, a woman's like a bus - you miss one, another comes along in five minutes.

LLOYD: Sara and I used to ride buses all the time.

STUART: Lloyd, I'm trying to be supportive, you're getting to be annoying. Why can't it be like the old days? Remember? No women! We used to sit up all night drinking Peppermint Schnapps and just being buds. Face facts: she's gone, life goes on, get over it! God, it's hot in here! (Stuart goes to air conditioner, fiddles with it.)

LLOYD: You know what I miss about Sara? I say this with the utmost respect: her breasts.

STUART: (Banging on the air conditioner.) Not working! (Stuart goes to phone.)

LLOYD: I know it's not profound or anything, but they were shaped like balled-up, perfect little kittens. They weren't too big, they weren't too small.

STUART: (Into phone.) I'll hold - (To Lloyd.) Lloyd look, I know what you're going through. I'm a breast man! But you can't let a couple of mammary glands run your life -

LLOYD: Yes, I can - .

STUART: (Into phone.) No, not you, sir. Look, we're in cottage . . . (Stuart looks over to Lloyd.)

LLOYD: Cupid II.

STUART: (Into phone.) We're in the Cupid II and the air conditioner won't turn on. Can you make it quick? Okay, thanks. (He hangs up.)

LLOYD: Why don't you take off your sweater if you're hot?

STUART: Who said I'm hot?

LLOYD: How can you not be hot? It's gotta be ninety-five degrees in here.(Lloyd peels off his shirt.)

STUART: We're firemen, Lloyd. To a fireman ninety-five degrees isn't that hot.

LLOYD: You're not a fireman. You're a dispatcher.

STUART: Hey, don't go down that road!

LLOYD: I just think it's important to be dear who fights the fires and who sits in the cage and talks on the phone . . .

STUART: Hey! Who do you think is responsible for everything? Like the night you were driving and you couldn't find City Hall. Who had the entire map of Bayonne committed to mind?

LLOYD: By the time you got us there, it was burnt to the ground.

STUART: At least you got there. You made an appearance.

LLOYD: Fine. Now would you please take that sweater off. It's July - in the Poconos.

STUART: Why are you so obsessed with me and my sweater? It's my lucky sweater! You got a problem with that?

LLOYD: You know, I had a lucky sweater. Sara took it. She probably gave it to her new boyfriend. I followed them. He weighs over 300 pounds. A 300-pound man is stretching out my lucky sweater! (beat) I'm sorry. I don't mean to continuously talk about my wife. My ex-wife. She's gone, dammit. It's only been three and a half weeks. And those have been the best three and a half weeks of my life. What am I saying? I wish I were dead. We should have gone hunting. You could have shot me. My life is over! I need a hug.

STUART: No hugging! Lloyd, get a grip! We're in Cupid II. There will be no hugging this weekend.

LLOYD: You know what I even did for that woman: I even wrote her a poem - me! It was like - like giving birth! I don't suppose you want to hear it?

STUART: No Lloyd, I'd hate to.

LLOYD: Okay, here goes. It's to the tune of Gilligan's Island. Just sit right back and you'll hear a tale / A tale of this crazy guy / Who met the woman of his dreams / My oh my oh my. / The girl was a mighty poem of love / Her breasts were firm as mountains / And every time I held her tight /We erupted like love fountains.

STUART: Good poem,

LLOYD: If someone wrote that for me, I'd be theirs.

LLOYD: Thanks, buddy. Hey, but you're more than my buddy: we're the two musketeers! (They gesture)

LLOYD: I love you coming on this trip with me. I love you going in half with me.

STUART: Half? I'm going in half?

LLOYD: Well, sure. I just thought it was understood. (A beat)

STUART: Well - fine. Okay. One shipmate throwing a life preserver to his best amigo. I'll write you a check because I know if I were in trouble, you'd write me an even bigger check.

LLOYD: Hey, c'mon! We're here to have a good time no matter how awful my life is! No more moping! Put on your swim trunks! Let's cruise the pool! (Lloyd thrusts off his shorts)

STUART: No! Uh, swimming - no, I, uh - not possible.

LLOYD: C'mon, we'll sit pool-side, meet some babes, show off our chests-

STUART: No swimming. Lloyd - we've got to talk.

LLOYD: I'll talk about anything but Sara. . . . God I miss her! The way she would eat a cheeseburger - she'd wolf it down in one bite, no chewing! The woman was a saint!

STUART: Listen, I know you're going through a really bad time right now- And I sympathize. But there are worse problems in the world to have, much worse, and I have one of them now.

LLOYD: What're you talking about? .

STUART: Okay, I didn't want to mention this back home, cause I wanted your full attention. Here goes - I need an operation. I have a terrible medical problem.

LLOYD: Sara once had a terrible medical problem . . .

STUART: Could we please get off of Sara?! I have a terrible medical problem. I need an operation. And it costs about five grand. And firemen don't make that kind of money.

LLOYD: You're not a fireman. You don't even have the red hat.

STUART: Look, I need an operation! Can I have the money or not?

LLOYD: What's the matter?

STUART: I - I can't reveal that. It's personal.

LLOYD: We're the two musketeers. (They gesture) How personal can it be?

STUART: Look, it's private and I just need you to trust me.

LLOYD: I told you about my swollen testicle.

STUART: I know, and I love you for that, but this is - even more personal. This surgery, our medical insurance doesn't cover it. It's considered - cosmetic.

LLOYD: Like a nose job?

STUART: It's not exactly a nose job. It's what the doctors call a suction-assisted lipectomy - or a gynocostomy.

LLOYD: Sounds like a woman thing-

STUART: Me? A woman thing? Right! That's a laugh! You're out of your mind! C'mon, punch me in the stomach as hard as you can! (Lloyd prepares to) No, forget it! Okay, it's a condition that affects men - the more manly, the more it affects them - and it involves a swelling of the pectoral area to unnatural, mammalian proportions.

LLOYD: Help me out, Stu, in English.

STUART: I've grown breasts. (Pause)

LLOYD: That's not funny. I'm very vulnerable right now, and you're playing jokes.

STUART: It's no joke. My doctor says it’s a common condition.

LLOYD: (After a moment) You have breasts. (Pause) So how come I don't see them?

STUART: They're not huge, and, well, the sweater is hiding them. (A beat. Lloyd stares)

LLOYD: Well, let me see' em.

STUART: I rather you didn't.

LLOYD: Then let me feel them.

STUART: That's not going to happen. Lloyd, if you had breasts, would you show them to me?

LLOYD: We're the two musketeers. (They gesture)

STUART: Lloyd, as my sidekick, I'm asking you to trust me and give me the money!

LLOYD: You know what I think this is? I think this is you attempting to divert all the attention. My heart is in two, on the floor, I'm a melted pile of agony, and you come in here, trying to steal my thunder -

STUART: Look, Lloyd, lots of men get divorced, not lots of men grow breasts!

LLOYD: You do not have breasts! (Lloyd lunges for Stuart and feels his chest. - Stuart tries to stop him, but it is too late. A frozen moment, as Lloyd has his hands on his buddy's chest. Lloyd quickly reels back. Stuart steps away, very embarrassed.)

LLOYD: Oh my God . . .

STUART: Happy now?

LLOYD: Those are - those are - You have breasts. Breasts! It's just so amazing . . .

STUART: So you now understand the severity of the problem. Write me a check.

LLOYD: Well- ya know, I, uh, I could do that. But something like this doesn't come along every day.

STUART: What're you talking about?

LLOYD: - well, I've always been curious about breasts. I'm a breast man, too! And I have a lot of questions - questions that I'm too embarrassed to ever ask a real woman.

STUART: You want to ask me questions? (Lloyd nods)

STUART: Then you'll give me the money?

LLOYD: Absolutely.

STUART: I feel like a prostitute, but go ahead, ask your questions.

LLOYD: Okay. Do you wear a brassiere?

STUART: No, but I do-wear an elastic support garment.

LLOYD: That's a brassiere!

STUART: Next question!

LLOYD: All right. (Beat.) When you rub them, do you get a warm, glow-y sensation? .

STUART: I have no idea. I haven't tried.

LLOYD: No time like the present.

STUART: I'm not gonna try it in front of you!

LLOYD: Stuart, come on. We're as close as any two guys can be. We've seen each other in the basest of situations. (A beat. Stuart softly rubs one of his breasts)

STUART: Yeah, it feels nice.

LLOYD: You want me to do the other one?

STUART: Get away from me! That's it! Questions are over! The check!

LLOYD: Look, this is an awful, awful problem. And of course I'll give. you the money - well, I would, if I had it.

STUART: You don't have it?

LLOYD: Sara took our checkbook. But hey, I'm gonna help you get the money!

STUART: How?

LLOYD: Top of my head - we sell your story to television.

STUART: What?!

LLOYD: Just hear me out. We go on Oprah. My Best Buddy Has Breasts. You cry like a baby. We run over to Richard Bey. You're wearing a halter top. The audience goes nuts! TV movies, Broadway! We make a mint! You can have all the operations you want!

STUART: Lloyd look - we're not going on television. The last thing in the world I want is for anyone else to know about this.

LLOYD: Okay, pisano, okay. Right now, you're the only person in the world who means anything to me. Nothing will ever come between us. I want you to know that. My God, my brain is on overload! I'm here in this fabulous love nest I was supposed to be sharing with my beloved Sara. Instead, my wife's gone, my money's gone, I'm a broken shell of a man, and my best friend has breasts.

STUART: Hey, we're the two musketeers (They gesture, Lloyd still sobbing) We'll pull through this! How about tonight, it's just you and me.

LLOYD: Really?

STUART: Yeah, why don't you run out and rent a movie - a guy movie!

LLOYD: I love guy movies!

STUART: Yeah, like Lethal Weapon! And pick up a bunch of guy stuff!

LLOYD: Yeah, guy stuff! (Stuart leads Lloyd to the door)

STUART: And we'll just be here for each other, we'll get through it, we'll do what we have to, wives or no wives, breasts or no breasts! We're a tag team!

LLOYD: You're right, you're right! Who needs women, dammit! We're men! All we need is men! Men, men and more men!
```

---

## IC-1329: Bruce Almighty - Screenplay

- Title: Bruce Almighty - Screenplay
- Author (byline): Steve Koren, Mark O’Keefe and Steve Oedekerk
- Work: Not specified
- Publisher: Shady Acres Entertainment
- Publication date as stated: June 2002
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: BRUCE, ALLY, GUSTOV, GRACE, PHONE VOICE, GOD, OLD LADY, BYSTANDERS, OFF STAGE VOICE, COMPUTER VOICE, HEAVY WOMAN, NEWSCASTER #1, NEWSANCHOR #2, NEWSCASTER
- Teaser before the introduction: Yes
- Spoken words (computed): 1725
- Already set (do not supply): none

### Source block (context only)

```text
Author: Steve Koren, Mark O’Keefe and Steve Oedekerk
ISBN: N/A
Publisher: Shady Acres Entertainment
Date (Month/Year): June 2002
Original screenplay can be purchased at https://www.scriptfly.com/
```

### Introduction (context only: never use it for content warnings)

```text
But when Bruce is not only passed over for the News Anchor position he’s been vying for, and is instead fired, his faith is pushed to the breaking point. Even his long-time girlfriend, Grace, can’t lift his spirits. Bruce Almighty by Steve Koren, Mark O’Keefe and Steve Oedekerk.
```

### Performance text (classify this)

```text
Kowolski’s Bakery: A news crew shuttles around a gigantic cookie. News reporter BRUCE NOLAN looks into a mirror, desperately trying to place a large segment of wayward hair.

BRUCE: (Pg 2-3) Oh, God, no! The hair's wrong. This is a bad sign.

ALLY: Not to worry, you’re going to look great in this (holds out a hair net)

BRUCE: A hair net? I’m not wearing a hair net! You should tell me this beforehand, this is like a huge waste of moose.

ALLY: Health code. Around the cookie, you gotta have it.

BRUCE: (Dons the hairnet, looking ridiculous and disgruntled)

ALLY: (laughing) A thing of beauty. In 3 . . . 2 . . . 1 . . .

BRUCE: (snaps from disgruntled to charismatic TV newsman) For three decades the Kowolski Family Bakery has been a mainstay in downtown Buffalo. Today, in honor of their 30-year anniversary, Momma Kowolski and her sons decided to do something a little bit different. Tell me guys, how did this idea come about?

GUSTOV: Well, Vol said to me, 'Gustov, why don't we make the biggest chocolate chip cookie in Buffalo?' And I said, 'Yeah, sure.'

BRUCE: The previous Buffalo cookie record was 3 feet, 17 inches baked by Gladys Pelsnick. But this behemoth cookie clearly proves that Gustov and Vol have much more free time . . . And that's the way the cookie crumbles. I'm Bruce Nolan, Eyewitness News. (off camera, he drops his newscaster persona) (sighs) I'm never going to get anchor doing these kind of assignments. It's a story about a cookie! It sucks! People with eating disorders will be riveted! (goes into huge pathetic fan character) Dear Bruce, love the bakery piece. I can't wait to vomit so I can make room for more cookies. (beat) I want my work to matter.

BRUCE: (Pg 28-29) Thanks for everything, Lord. I am so honored that my horrible demise is a part of your loving and mysterious plan.

GRACE: Bruce, don't talk like that.

BRUCE: Oh, don't worry, he's not listening. If he is he doesn't care. Have you seen the news lately? We got gangs, we got drugs, we got corruption. What kind of God lets that happen? Every time we cure a disease he comes up with a new one! (as God) Yeah, is this the lab? Yeah, it's God. They've just come up with a treatment for syphilis down there. I think it's time to release the tainted monkey. Oh, and there's a guy in Ohio who's praying for strength and wisdom, blind him and cut off his legs. Think about it, Grace. God is all powerful. He could fix everything in five minutes if he wanted to. But he doesn't want to. He doesn't like me.

GRACE: Bruce, please. This isn't his fault.

BRUCE: Of course not. (hushed tone) It's part of the mysterious plan. (growing in volume; he looks heavenward, challenging the Infinite) News flash: I'm not okay with a mediocre job. I'm not okay with a mediocre LIFE! The gloves are off, pal! Let me see a little wrath! Smite me, oh mighty smiter! What, no pestilence, boils? Come on, you got me on the ropes, don't you want to finish me off?! You're the one who should be fired! The only one around here not doing his job is YOU! (Phone rings, Bruce answers)

PHONE VOICE: (Pg 33) Denied that promotion at work? Is life unfair? Everywhere you turn is there someone less talented than you reaping all the benefits? Is your name Bruce? Then do we have the job for you. We're located at 77256 23rd Street . . . So come on down, or we'll just keep beepin' ya. ***** 77256 23rd Street***** Bruce enters and checks the building directory GOD as JANITOR: (Pg 33-39) (mopping the floor) You’re looking for Room 7. That’d be on the seventh floor. Stairs are right over there.

BRUCE: (takes the stairs; at the top he sees a man on a ladder) Excuse me. Hello. I'm, ah, looking for whoever runs this joint. . .

GOD as ELECTRICIAN: Be right with ya, just fixin' a light. Tell me if it's working? (click -- an insanely bright white light shines down, blinding Bruce)

BRUCE: Yep, seems to be. (wiping his eyes) Kinda bright, though.

GOD as ELECTRICIAN: Yeah, it is for most people. They spend their lives in the dark. . . thinkin' they can hide from me. The boss'll be right out. (Janitor unzips his uniform, revealing a very nice suit. He extends his hand to Bruce) You must be Bruce. I've been expecting you. (He steps behind a desk)

BRUCE: Oh, this is hilarious. So, you're the boss and the electrician and the janitor. How did you get my number?

GOD: Oh, I know a lot about you Bruce. Everything you've ever said, done or thought about doin' (picks up a file) Now this last entry was a little disturbing. (scanning) “Thanks for everything, Lord. The gloves are off, pal . . . Smite me, oh mighty smiter. (aside) I'm not much for blaspheming but that one made me laugh.

BRUCE: (dazed) Who are you?

GOD: I'm the creator of the heavens and the earth. I'm the Alpha & Omega.

BRUCE: Sorry, it's not ringing a bell.

GOD: I'm God, Bruce.

BRUCE: Oh, you're God. Well, that explains everything! That's how you got up to the seventh floor so quickly. (placating) Well, it's really nice to meet you. Thanks for the Grand Canyon and, ah, good luck with the apocalypse. (turns to leave, but finds himself walking right toward God and his desk. He tries again, and again) Okay. That's good. That's a good one.

GOD: You've been doing a lot of complaining about me, Bruce. And quite frankly, I'm tired of it... I brought you here to offer you a job. My job. You think you can do it better, so here's your chance. When you leave this building, you will be endowed with all my powers. All the power of God.

BRUCE: Sure, whatever you say, Pal. (a beat, then Bruce sprints out of the room) ***** A Diner, Later the Same Day *****

BRUCE: (Pg 40-45) (talking to himself) I'm having a breakdown. That's what it is. Just a normal, everyday psychotic episode, brought on by tumor or brain lesion . . . (laughs) Okay, just relax here. I did not meet God and I do not have his powers. (to waitress, embarrassed) Oh, hi, ah, coffee please.

(She pours him a cup and heads off. Bruce looks at the sugar at the end of the table, holds out his hand and the sugar slides across the table right into it. The creamer slides into his other hand. He is half scared; half thrilled. He pours cream and sugar into his cup, then looks around the table)

BRUCE: Excuse me I need a spoooo. . . (a spoon appears in his hand, he wipes it off with his napkin) That's alright, I found one.

GOD: (suddenly appears beside the booth) Havin’ fun? (Bruce is now awestruck) Okay, let me explain the rules. you left in such a rush I didn't get a chance to explain.

BRUCE: Well [it] freaked me out a little bit.

GOD: I did the same thing to Ghandi, he couldn't eat for three weeks. Now, here's the deal. There are only two rules. You can't tell anyone you're God. Believe me you don't want that kind of attention. And you can't mess with free will.

BRUCE: Uh huh. Can I - ask why?

GOD: (excited) Yes you can. That's the beauty it. I'll be seein' ya. (God begins to walk away) I'm taking a vacation.

BRUCE: God can't take a vacation. Can he? Can you?

GOD: Ever hear of the Dark Ages? Besides, I'm covered. You can fix everything in five minutes if you want to, right?

BRUCE: (Pg 50) (strikes a God-like pose and proclaims) I AM THE LORD, THY BRUCE ALMIGHTY. MY WILL BE DONE! (a new, confident Bruce) [Now] (Pg 56) to get my job back! *****Scene***** ON a TV, DAN RATHER: (Pg 58-59) The body of Jimmy Hoffa was uncovered in a field today outside of a canine training center in Buffalo New York. Local Buffalo freelance field reporter Bruce Nolan was the first on the scene . . .

BRUCE: . . . As you can see behind us, the body is being carefully exhumed and will be transported to a hospital facility where DNA testing will confirm the identity. That, of course, only a formality as in a bizarre twist, the body was found buried with a birth certificate and complete set of dental records . . . (Pg 3) And that's the way the cookie crumbles. JACK (Bruce’s Former Boss): (Pg 62-63) Look, I'll be straight. We want you back, Bruce. Look, it's not in my power to give you anchor, but as far as field reporting goes . . .

BRUCE: Jack, don't worry about that. Just give me a camera and a crew and I'll give you the news. (Bruce interviewing an old lady at the Mark Twain chili cook off)

OLD LADY: (Pg 66) My secret is I let the jalapeno's marinade in a spicy sauce . . .

BRUCE: (gets an idea, then suddenly) . . . Hold that thought, Hazel! It seems some type of meteor or asteroid has, by chance, hit the earth right behind the Mark Twain Chili Cook Off. . . (Pg 3) And that's the way the cookie crumbles. (cut to Bruce free-falling in a sky diving uniform) (Pg 66-67) . . . So remember, it's sky diving season at Old Pete's airfield (grabs the ripcord) This is Bruce Nolan. . . (gives it a tug) My rip cord appears to be stuck. This is very unfortunate. I'm heading toward the earth at a very precarious speed . . . (he falls into a wooded area)

BYSTANDERS: (running to his aid) He's okay! What's that? It's Bigfoot! Bigfoot broke his fall!

BRUCE: (stands groggy, points to a dazed Bigfoot) Ah ha! You are real!. . . (Pg 69) And that's the way the cookie crumbles. (standing casually with his arm around Bigfoot) (Pg 3) I'm Bruce Nolan, Eyewitness News. *****Scene*****

(Bruce reacts to voices he hears in his head, voices only he can hear. He shakes his head, covers his ears, looks around for where the sounds may be coming from, he is perplexed)

OFF STAGE VOICE: (Pg 75-76) (louder) Please! Help me! Please!

GOD: Really something isn’t it?

BRUCE: Those voices . . .

GOD: They're prayers, Bruce. You keep ignoring them and they're going to build up on. you like that. You didn't think being God was going to be all fun and games did you? You've had my powers for over a week now and how many people have you helped? (the whispers start again, and Bruce reacts)

BRUCE: (Pg 78-79) (hands over his ears) Not now!

GOD: You wanted the job, Bruce. I suggest you get to it. *****Next Day, Bruce’s Apartment*****

BRUCE: (Pg 79-80) Okay, first off, this creepy whisper thing has got to go. (paces) Organization and management. I need a system. Something concrete . . . (an idea – Bruce waves his hand and now stands before a high-tech computer, he taps some keys) Welcome to the information super highway. No mess, full bless!

COMPUTER VOICE: Downloading Prayers . . . 1,567,432 unread messages.

BRUCE: (Pg 85) (cracks his knuckles and begins answering prayers, his fingers move faster and faster) He reads out loud the prayers and responses) I’ve got to find a better job . . . Promotion with a 15% raise. Come on light, turn . . . It’s green. God, I wish I were thinner . . Donuts are now healthy.

COMPUTER VOICE: (Ding) 3 million unread messages.

BRUCE: Oh, come on. What a bunch of whiners. This is going to suck up my whole life. (he gets an idea, taps a few keys) Answer all . . . Yes. And Enter (he hits the Enter key with a flourish) ****Scene****

GRACE: (Pg 87) Oh, you’ll never believe it. Debbie won the lottery. But get this, there were like 433 thousand other winners, so it only paid out 17 dollars. Can you believe the odds of that? BUSINESSMAN (Pg 91) My tech stocks tripled in five days!

HEAVY WOMAN: I lost 47 lbs on the Krispy Kreme diet. *****Scene*****

NEWSCASTER #1: (Pg 101) The Dow skyrocketed again today and with a new influx of paper millionaires, analysts are warning of a potential run on banks. . .

NEWSANCHOR #2: The scene nearly turned violent when hundreds of disgruntled Buffalo residents protested the results of last week’s fluke lottery results. . .

***** 77256 23rd Street*****

(Bruce stands there, sees God as he originally found him, mopping.)

BRUCE: (Pg 106-107) They're all out of control. I don't know what to do.

GOD: (not surprised to see Bruce) You mind giving me a hand with this floor first? (Bruce rolls up his sleeves and grabs a mop; God sings) *"Poor man wanna be rich, Rich man wanna be king, And a king ain’t satisfied, ‘Til he rules everything . . . " (to Bruce) Springsteen. I like a little Boss in my head while I'm workin' . . . (they finish and survey the sparkling floor) There we go. Wonderful thing. No matter how filthy something gets, it can always be cleaned right up.

BRUCE: What happened? I gave everyone what they wanted.

GOD: Since when does anyone have a clue about what they want? Have you seen the news lately? (takes a remote from his pocket and clicks, a projection appears)

NEWSCASTER: (Pg 108-109) Scientists believe last week’s asteroid may have knocked the earth off its axis resulting in the rapid acceleration of the melting of the polar caps. . .

GOD: (to Bruce, again using Bruce's words) Now what kind of a God let's that happen? Not as easy as it looks, is it? This God business. Everybody wants a miracle, Bruce. Want me to do everything for ‘em. But what they don’t understand is, they’re the one’s holding the power. That’s everybody’s problem. You keep looking up . . .
```

---

## IC-1330: Brussels Sprouts

- Title: Brussels Sprouts
- Author (byline): Andy Griffiths
- Work: Just Disgusting!
- Publisher: Scholastic, Inc.
- Publication date as stated: Feb 2005
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ANDY, MOM, DAD, JEN
- Teaser before the introduction: Yes
- Spoken words (computed): 1870
- Already set (do not supply): none

### Source block (context only)

```text
Author: Andy Griffiths
Book: Just Disgusting!
ISBN: 978-0439549547
Publisher: Scholastic, Inc.
Date (Month/Year): Feb 2005
```

### Introduction (context only: never use it for content warnings)

```text
Despite its faithful appearance on holidays, the brussels sprout is the American vegetable villain. This role used to be played by spinach, until Popeye rescued it in the 1930s. A 2008 survey by Heinz shows that brussels sprouts now take the most-hated prize for Americans in general and they consistently make it to the top five in surveys of the most-hated vegetables around the world. Brussels Sprouts by Andy Griffiths
```

### Performance text (classify this)

```text
(Pg 16 -34)

ANDY: I’m sitting at the kitchen table with Dad and Jen. Mom is serving dinner. She puts a plate down in front of me. I look at it. Roast chicken. Good. Gravy. Good. Roast potatoes. Good. Brussels sprouts. Bad. FIVE OF THEM! Bad. Bad. Bad. Bad. Bad. I hate brussels sprouts.

And when I say I hate brussels sprouts, I don’t just mean I hate brussels sprouts. I mean I REALLY hate brussels sprouts. And when I say I REALLY hate brussels sprouts, I mean I really, really, really, REALLY, REALLY, REALLY hate Brussel sprouts.

Who wouldn’t hate them? They’re green. They’re slimy. They’re moldy. They’re horrible. They’re putrid. They’re foul. Apart from that, I love them.

No. I don’t. That was just a joke. There’s absolutely NOTHING to love about brussels sprouts. Nothing at all. They’re disgusting. So why did my mom have to go and spoil a perfectly good roast chicken dinner by giving me FIVE?? Surely she can’t possibly expect me to EAT them.

MOM: Come on, Andy. Don’t just sit there looking at your dinner. Eat up.

ANDY: All of it?

MOM: (firmly) All of it.

ANDY: Even the brussels sprouts?

MOM: Even the brussels spouts.

ANDY: I can’t believe it. She DOES expect me to eat them. (To Mom) But I HATE brussels sprouts.

MOM: Okay. Suit yourself. But if you don’t eat all of your brussels sprouts, you won’t get any dessert.

ANDY: Huh? No dessert? If there’s one thing I love, it’s dessert. And when I say I love dessert, I don’t just mean I love dessert. I mean I REALLY love dessert. And no pile of brussels sprouts is going to stop me from getting it, that’s for sure. (To Mom) But that’s not fair!

DAD: If you don’t eat your dinner, you don’t get dessert. That’s the deal. You know that.

ANDY: Some deal. I never had a say in it. As if I’d agree to a stupid deal like that. Jen snickers. She pokes her fork into a brussels sprout and raises it to her lips.

JEN: Mmmmmmmm! (Puts the sprout into her mouth and acts like it’s the most beautiful thing she’s ever tasted) You don’t know what you’re missing, Andy.

ANDY: (to audience) I know she’s just trying to annoy me, but it gives me an idea. (to family) OH NO! (Pointing out the kitchen window) I DON’T BELIEVE IT!

MOM: What is it? Is that cat back again?

DAD: Are the birds on my new lawn?

JEN: Is it Craig? But he said he wasn’t coming until later! I can’t let him see me like this!

ANDY: (to audience and in pantomime) While they’re all staring out of the window trying to figure out what I’ve seen, I take one of my sprouts and slip it onto Jen’s p lat. It’s too easy, really. (to family) Just kidding! (to audience) Mom sighs and Dad shakes his head.

JEN: Are you going to be an idiot all your life?

ANDY: Probably. The pay’s a little low, but the hours are good . . . and you can pretty much work whenever you want. (To audience) She ignores my reply, stabs the sprout I just put on her plate, and puts it into her mouth. Do I feel ay pity for her? No. I do not. She deserves it. One down. For to go.

DAD: Excuse me, funny boy. Would you mind passing me the pepper?

ANDY: I look at the pepper grinder. I hate pepper. It always makes me sneeze. (suddenly gets an idea) Of course! Pepper! Sneezing! The oldest trick in the book! Why didn’t I think of it sooner? (to Dad) Sure (quickly putting a brussels sprout into his mouth then launching a fake sneeze) Ah . . . . (grabs a tissue out of his pocket) AH . . . . (holds the tissue up to his face) AH-CHOOO! (Spits the brussels sprout into the tissue and quickly puts the whole thing back in his pocket)

MOM: Bless you.

ANDY: Thanks. I think some pepper got up my nose. (to audience) I got away with it again. I quickly shovel some chicken, gravy and potato into my mouth to get rid of the taste of the sprout. Two down. Three to go. I feel something nudge my foot. Sooty! He’s not supposed to be in the kitchen while we’re eating, but he’s managed to sneak in and hide underneath the table anyway. Which is fantastic, because Sooty eats anything. Even brussels sprouts. (in words and pantomime) I hunch forward over my plate, conceal one of the sprouts in the palm of my hand and sneak it uner the table to Sooty’s waiting wet mouth. Yes! He’s eating it! Good dog! He’ll be able to eat the other two for me as well. (reacts to smell) Suddenly the most disgusting, eye-watering smell fills the kitchen. Mom looks at dad (Give a Mom look). Dad looks at me (Give a Dad look). I look at Jen (maybe points) We all shrug. (Shrug) Dad looks under the table.

DAD: How did that dog get in her?

ANDY: Dad chases him and shoes him out the back door. Darn. Just when I was so close!

JEN: I bed Andy let him in. He’s probably been giving him food under the table.

ANDY: Yeah, right. As if!

DAD: You haven’t been wasting good food on that mongrel, have you?

ANDY: (to Dad) No. (to audience) I’m not lying, either. Whatever brussels sprouts are, they are definitely NOT good food. I eat the rest of my dinner and try to figure out how to get rid of the two remaining sprouts. I can’t put any more on Jen’s plat because she’s already finished hers. She’d be sure to notice. And I can’t sneeze again because my one tissue is already full. And how’s going to help me now that Sooty’s gone? (thinking for a beat) I know! The X-Men. My X-Men undies, that is. It’s going to take a little skill to do it without anybody seeing me, but I think it’s possible. (in words and pantomime) I tab the next-to-last sprout with my fork, and as I bring it up to my mouth, I stretch open the front of my pants with my other hand. Then, just as I’m about to put the sprout into my mouth, I ease it off the end of my fork with my thumb. It drops down, straight into my undies. A direct hit!

Sure, it feels disgusting, but I’d rather have a brussels sprout squishing around in my undies than squishing around in my stomach. For down, one to go. But this one’s not going to be a problem. There’s a pile of chicken bones on my plate. I can just hit it under there. Then all I have to do is scrape the sprout off my plate and into the mulch can and the nightmare will be over. Here goes. (to Mom) Thanks, Mom. That was delicious. I’ll just clear the table.

(Starting to do so)

JEN: What? You NEVER clear the table.

MOM: Not so fast, Andy. You haven’t quite finished.

ANDY: (innocently after shooting Jen a drop dead look) What do you mean? I’ve only got bones left. You can’t expect me to eat bones.

MOM: It’s not the bones I’m talking about. It’s the brussels sprout underneath them.

ANDY: What brussels sprout? Ohhhh (acting surprised) THAT brussels sprout! I didn’t see it there.

MOM: (tilts head and raises eyebrows) Do I look like I was born yesterday?

ANDY: Well, actually, you do look very young for someone so old.

MOM: Nice try, Andy. Sit down and finish your dinner.

ANDY: But I can’t eat any more. You gave me too many brussels sprouts.

MOM: I gave you the same as everyone else.

ANDY: But everyone else is bigger than me. I should get less!

DAD: No, you should get more. (flexing his muscles) Don’t you want to grow up to be as big and strong as me?

ANDY: I AM big and strong. (family laughs) What’s so funny?

JEN: Your arms are like toothpicks and your legs are like broomsticks. If the wind blows too hard, you fall over. You’re a WEED!

ANDY: And you’re a pig!

JEN: Than you. You just called me a P-I-G. That stands for Pretty Intelligent Girl.

ANDY: No it doesn’t. I stands for Putrid Idiotic Geek!

DAD: Ignore him, Jen. Andy, just shut up and eat your sprout.

ANDY: I can’t. I’m full.

MOM: What a shame. You won’t be able to hae any dessert.

ANDY: No dessert. But I LOVE dessert! She’s got me in a bind. I get the sprout out from underneath the pile of chicken bones. It sits there – taunting me. One horrible, disgusting, moldy, old, slimy, green, putrid brussels sprout. And to make things even worse, it’s cold. Mom is watching me like a hawk. So is Dad. And Jen.

JEN: Come on, Andy. Just hurry up and eat it and then we can have dessert!

ANDY: (to Jen) All right, all right! (to audience) There’s only one thing to do. I’m going to have to put it in my mouth, go to the bathroom, and spit it out. And while I’m there I’ll be able to get the other one out of my undies (shifts uncomfortably) I stab the sprout with my fork and hold it up in front of my face. Nothing is going to stop me from getting to my dessert. I put it in my mouth. (Look of utter disgust) YUCK! I stand up.

DAD: Where do you think you’re going?

ANDY: (with mouth full) To the bathroom.

JEN: Don’t leet him. He’s not going to eat it. It’s a trick! He’s going to spit it out!

ANDY: (still with a full mouth) No, I’m not.

MOM: You can go to the bathroom AFTER you’ve swallowed the brussels sprout.

ANDY: But I’m BURSTING!

JEN: You mean your’e DISGUSTING!

DAD: Swallow the sprout. THEN you can go to the bathroom. That’s the deal.

ANDY: (still with mouth full) What kind of deal is that? I eat a sprout, and I’m rewarded with a trip to the bathroom? Your deals are getting worse. I’m going to get myself a lawyer.

JEN: You don’t need a lawyer. You need a psychiatrist!

DAD: He’ll need a doctor if he doesn’t sit down and eat that brussels sprout.

ANDY: I sit down. All eyes are on me. My escape route has been blocked. I’ve got the world’s most disgusting brussels spout in my mouth and there’s nothing I can do about it. I can’t flush it down the toilet. I can’t feed it to Sooty. I can’t put it down my undies. There’s only one thing I CAN do. It’s sick! It’s twisted! It’s desperate! But I’m just sick, twisted and desperate enough to try it. I’m going to swallow the brussels sprout. (look of utter disgust) Do it or die. Okay . . . here goes. (Straightens his spine, grips the table with both hands, closes his eyes and takes a deep breath; and another then bites down) A watery slime oozes into my mouth. Don’t think about it . . . Don’t think about it. Think about nice things like sunny days . . picnics. (Bites down again) MORE SLIME! MORE OOZE! (shakes head violently) Nice things . . . like kittens and puppies . . and ponies and GIANT MASHING AND PULVERIZING MACHINES mashing them into guts and ooze and slime . . . green slime. It’s probably safer to think about nothing at all. I put my mind in neutral and chew . . . (makes the most horrible faces possible) I can’t do it . . . but I’ve got to. Otherwise, I don’t get dessert. I might miss out on something amazing! (continues to chew . . .then) HEY! Wait . . . Something’s happened . . . Something amazing! My mouth is no longer full. It’s gone . . I must have swallowed it. I’ve done it! I’ve really done it! (to family) FINISHED! (opening mouth wide to prove it is gone)

MOM: Good job, Andy. That wasn’t so bad now, was it?

ANDY: I smile and nod and try not to think about what I just did. I’ll think about dessert instead. I close my eyes. I want it to be a surprise. (so excited he can’t hold still) Maybe tonight it will be upside-down cake . . no, wait . . . pecan pie. That’s my absolute favorite! No . . maybe Mom will surprise everyone and do her famous cherry pie . . . or Maybe it’s chocolate fudge! Or Twinkies! Or . . . I hear Dad get something out of the fridge and put it down on the table.

JEN: Yum! My favorite!

DAD: Mmmmmm! Delicious!

MOM: I just hope it was worth the wait.

ANDY: I can’t stand the suspense a moment longer. (in words and pantomime) I open my eyes and look down at the bowl in front of me. (excited expression turns to shock and horror) Oh no! Oh no! I don’t believe it! This can’t be happening. Custard – cold, horrible, disgusting, moldy, old, slimy, lumpy, yellow, putrid, vomity custard. I HATE CUSTARD!
```

---

## IC-1331: Bullshot Crummond

- Title: Bullshot Crummond
- Author (byline): Ron House, Dix White, Jake Neville-Andrews, Alex
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: 1974
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: OTTO, LENYA, FENTON, CRUMMOND, ALGY, POLICEMAN, ROSEMARY
- Teaser before the introduction: Yes
- Spoken words (computed): 1649
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
The dashing Captain Hugh "Bullshot" Crummond - WWI ace fighter pilot, Olympic athlete, racing driver, part-time sleuth and all-round spiffing chap. Men want to be like him and women want to be with him! Or, at least, that is the public perception. Whilst he is, indeed, a remarkable man, he is also a bumbling buffoon. But Bullshot must save the world from the dastardly Count Otto van Bruno, his wartime adversary. This parody of low budget 30s detective movies typifies British heroism. Don't miss the next thrilling installment of this dastardly tale of. . .

Bullshot Crummond by Ron House, Dix White, Jake Neville-Andrews, Alex Shearman, and Derek Cunningham
```

### Performance text (classify this)

```text
Shearman, and Derek Cunningham

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

ROSEMARY: Daddy, where are you? Oh, you're safe. Yes, I will. Goodbye. (to Crummond) Hugh! It was all a false alarm. Daddy's safe at Netherington Abbey. I'm so happy. And Daddy said you should go back to London. I'm sorry to have wasted your time.

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

## IC-1332: Bursting

- Title: Bursting
- Author (byline): Andy Griffiths
- Work: Just Stupid!, Pgs 1-16
- Publisher: Scholastic Paperbacks
- Publication date as stated: 2004
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ANDY, OLD GUY, SM, MAN, HIPPIE, FIREMAN, CHIEF
- Teaser before the introduction: Yes
- Spoken words (computed): 1535
- Already set (do not supply): none

### Source block (context only)

```text
Author: Andy Griffiths
Book: Just Stupid!, Pgs 1-16
ISBN: 978-0439424745
Publisher: Scholastic Paperbacks
Date (Month/Year): 2004
```

### Introduction (context only: never use it for content warnings)

```text
Diapers ruined us. They made us lazy from a very young age. The moment we make our flying exit from the womb our butts are wrapped in cloth. Babies and toddlers don’t realize how good they have it! They can pee anywhere, anytime, without interrupting their various activities. And babies are busy! But it’s not so easy for us. In fact, it’s (insert time) on a (insert day). You could be (insert some activity), but instead . . . you are judging a speech tournament. Thank you, by the way. And, thanks to the judge’s lounge, you’ve probably downed at least two cups of coffee and a giant-sized Diet Coke by now. You have to be . . .

Bursting by Andy Griffiths
```

### Performance text (classify this)

```text
NOTE: The humor of this piece comes from the characterizations and the pantomimes. Go really, really big! Think of how many ways you can physically show that ANDY has to go to the bathroom really badly.

ANDY: (Pg 1-16) I’m in the supermarket trying to remember what groceries Mom wanted me to pick up, but I can’t think. I can’t breathe. I can’t do anything. I’m bursting. And I don’t mean bursting. I mean BURSTING! I’ve got to find a toilet. Fast. Then I can come back and think about the shopping with a clear head. Or not so much a clear head as an empty bladder.

ANDY: I haven’t got a second to lose. I run down the aisle and skid around the corner. WHAM! Straight into an old guy with a walker. He staggers forward and crashes into a stack of cans. They go rolling all over the floor.

OLD GUY: Well, don’t just stand there -- Help me up!

ANDY: (Pantomime helping the Old Guy up and helping him with his walker) The store manager appears. I can tell he’s the store manager because his pants are too tight. Plus he’s wearing a badge that says STORE MANAGER.

SM: What happened?

OLD GUY: This silly young boy knocked me over. When I was young we respected our elders.

ANDY: It was an accident!

SM: Were you running? There’s no excuse. I think you owe this gentleman an apology. Then you can pick up all the cans.

ANDY: But I’m bursting! (to audience) I get the feeling that I’m going to get out of here quicker if I just do what he says. (to the Old Man) I’m sorry, I shouldn’t have been running, and I hope you’re not hurt. (to audience, pantomiming picking up cans) I start picking up the cans. I can’t believe how far they’ve rolled. By the time I’ve finished, I’m seriously bursting. But I know better than to run out of the store. This time, I just walk very quickly. I get outside the supermarket and into the main shopping mall. I’m looking for a sign pointing to the toilet. There is a man selling pencils outside the supermarket.

MAN: Excuse me, want to buy a pencil? They’re cheap – twenty cents each.

ANDY: No, thank you. I haven’t got time!

MAN: Just one. One lousy pencil!

ANDY: How many times do I have to say it? I don’t want – or need – a pencil. What I need is a toilet. I’m bursting! (to audience) His shoulders drop. He sighs heavily. He looks like he’s going to cry. If he’s trying to make me feel bad, he’s succeeding. (to man) Okay, (fumbling for change). I’ll buy a pencil. (to audience) All I can find is a dollar. (to man) Have you got change? No? Keep the change then.

MAN: No, that wouldn’t be right. I’m not looking for charity.

ANDY: Fine, give me five pencils! (to audience) He counts the pencils out really slowly, one by one. (shifting from foot to foot impatiently). Finally, he hands me the pencils. I run off before figures out another way to waste my time. I’m running as fast as I can, but this shopping mall is too big. There are too many levels. (running then tripping and stumbling -- looking down at shoes) My shoelaces have come undone. I hate my shoelaces. Now I have to stop and waste valuable toilet-searching seconds retying them. (kneeling down painfully to tie the shoes) It’s putting pressure on a part of my body that’s already under too much strain. I don’t have much time. (noticing a sign overhead) Suddenly, I find the sign I’ve been looking for. A picture of a man, a woman, a wheelchair, and an arrow pointing to the left. (running toward the toilets) I can see the toilets up ahead of me. Oh, no. I don’t believe it. Closed for cleaning! Should I try to find another toilet or just wait? I’ll wait. But I’m bursting. I can’t wait. But I can’t not wait. I have to go. Right now . . . Hang on! The handicapped toilet is not closed. Can you go to jail for using a handicapped person’s toilet when you’re not really handicapped?

(hobbling to the door and slowly pushing it open) It’s vacant. I want to go in but something is stopping me. It would be so easy to just slip in here, and yet, so wrong. If I get away with using this toilet, who’s to say where or when it will stop? I can’t do it. I let go of the door. I might be bursting, but I’m not a criminal.

OLD GUY: Hey! You can’t use that toilet! You’re not handicapped! Tearing around the supermarket and knocking people over. Using the handicapped people’s toilets and stopping the truly handicapped from using them. You’re a menace to society. I’m going to call a security guard! Help! Guards! Arrest this boy!

ANDY: He’s crazy. I’ve got to get out of here. He’s creating such a racket, you’d think he was being murdered or something. (running back through the shopping mall) I pass a shop with an enormous poster of a river in the front window. I can’t hold out much longer. I can hear splashing. It’s coming from the indoor fountain. Maybe I could go in the fountain. I could get in, stand in the middle, and pretend to be a statue. I could squirt water out of my mouth at the same time. Nobody would even realize . . . But hang on! In front of the fountain is a map of the shopping mall. Fantastic! (hobbling over to the map) Hmmmm. And the sound of all that splashing is not making it any easier to concentrate. It doesn’t help that the front of the map is suddenly smeared with water. (turning around quickly) Two little kids are squirting each other with water pistols. (to kids) Quit it! (reacting to the kids spraying the front of his pants; then to audience) Right in the front of my pants! There’s a guy wearing a rainbow-colored shirt standing next to me. He looks like a hippie but I’ll ask him anyway. (to hippie) Excuse me, can you help me find the toilet?”

HIPPIE: (with his eyes half-closed and in a slow voice) Looks like it’s a bit late. (pointing at the front of Andy’s pants)

ANDY: That’s not what you think it is. But it will be if you don’t help me find the toilet.

HIPPIE: Chill out, man. (studying map) Says there the toilets are at M sixteen on level two. Ummmmm, level three . . . No, hang on . . . level one . . . oops – make that level four.

ANDY: Level four? There’s no such level!

HIPPIE: Hey, man, open your mind. There are many levels. More levels than you ever dreamed of. Relax. Take it easy.

ANDY: I can’t! I’m bursting! I’ve got to get to a toilet! Quick!

HIPPIE: No, man, you’re missing the point. The destination’s not important. The journey is where it’s at.

ANDY: Not when you’re bursting it’s not! I can’t stand still any longer. (running again) I see an escalator going up. (jumping on) I don’t believe it. It’s almost too good to be true. At the top of the escalator is a sign. A man, a woman, and a wheelchair. I bound up the last few steps and leap off the escalator. (bounding and leaping, but then his leg is jerked backward) My shoelace is caught in the top of the escalator! (trying to pull foot away and trying to unlace the shoe which traps his finger) The laces are being pulled tighter and tighter. My finger is turning bright red. It’s throbbing. Great! Now I’m bursting and I’ve got my shoelace stuck in an escalator and my finger stuck in my shoe. (using other hand to pry his heel from the shoe and getting it stuck too - He should be in an awkward “twister” position by now, bent over double, looking upside down through his legs) Oh, no. I don’t believe it. There’s nothing I can do, apart from chew my foot off. That’s it! Chewing! Only I don’t have to chew through my ankle . . . just my shoelace. (trying to chew through his shoelace and getting his hair caught) This is like the most impossible and painful game of Twister ever. (seeing the Old Guy) Oh, no . . . The old man is coming up the escalator. He’s coming right for me. (being hit by the Old guy and falling over, snapping his shoelace and ripping a chuck of his hair out) I’m free!

OLD GUY: (shouting) Now we’re even!

ANDY: (to Old Guy) No, we’re not. (scrambling to his feet) You just did me a big favor! I start running. Only a few feet more. Something is stabbing me in the leg. What is that? I put my hand into my pocket. Aaaggh! Something jabs me in the thumb. It’s those stupid pencils. (pulling pencils out of his pocket and dropping them on the ground in front of him as he is running, he should slip and fall on the pencils, whacking his head on the ground)(long beat as he lies unconscious, then coming to) Next thing I know I’m being shaken awake. (opening his eyes) A fireman is kneeling beside me. The corridor is filled with smoke and I can hear sirens.

FIREMAN: Wake up! Are you okay? You have to get out of here. Fire!

ANDY: He lifts me up again and starts steering me toward the exit. Away from the toilet! I try to head back toward the toilet but he grabs me.(being grabbed by the arm) (to fireman) But I have to use the toilet. I’m bursting!

FIREMAN: You’ll have to wait. It’s not safe! You have to get out of the building.

ANDY: Not safe?! If I don’t get to the toilet soon, nobody will be safe. This shopping mall will be flooded! (to audience) But he’s not listening. He’s escorting me to the exit. Outside, there are four fire trucks in a row. The firemen are spraying enormous arcs of water onto the building. I overhear the fire chief talking on his walkie-talkie:

CHIEF: All we know is that the fire appears to have started in one of the escalators. Some foreign material may have got in there and shorted the system. Until we can put out the fire, we can’t be sure. But to do that, we’re going to need backup units . . . as many as you’ve got. (wiping sweat from his brow)

ANDY: Suddenly, I know what I have to do. I can solve my problem and be a hero at the same time. (to Chief) Excuse me, you’re not going to need those backup units. You’ve got me! Watch this!

(urinating on the burning building – your back should be to the audience) Ahhhhhhhhhhhhh! (to audience, over your shoulder) Relief! Beautiful relief! The fire is powerless against me. It disappears in clouds of steam. People are gathered around and applauding. The supermarket manager is there. And the pencil seller. And the hippie. Even the old man. Cheering. (crowd cheering) I roll over and snuggle down deeper into my blankets. My blankets? What are my blankets doing here? And why am I wearing pajamas? (blinking, rubbing his eyes as he slowly comes awake) There’s no shopping mall. There are no fire trucks. No people. I’m in my bedroom. In my bed. Wrapped in my blankets. Putting out a fire. Only there’s no fire, either (realizing that he has seriously wet the bed) . . . I hate that.
```

---

## IC-1333: Butterflies are Free

- Title: Butterflies are Free
- Author (byline): Leonard Gershe
- Work: Not specified
- Publisher: Samuel French, Inc
- Publication date as stated: November 2010
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: DON, MRS. BAKER
- Teaser before the introduction: Yes
- Spoken words (computed): 1280
- Already set (do not supply): none

### Source block (context only)

```text
Author: Leonard Gershe
ISBN: 978-0573606441
Publisher: Samuel French, Inc
Date (Month/Year): November 2010
```

### Introduction (context only: never use it for content warnings)

```text
Young Don Baker, hero of his mother's children's book series, "Donny Dark" has been blind since birth. Don finally decides to take his own apartment in Manhattan and pursue his songwriting ambitions. But that’s just when Mrs. Baker's controlling instincts go into overdrive. Butterflies are Free by Leonard Gershe
```

### Performance text (classify this)

```text
DON: (Phone rings) (Pg 6-7) (Donny answers) Hello, Mother . . . I’m fine, thank you. How are you? The apartment is great. I love it. Last night? I didn’t do anything last night. I mean I didn’t go out. I had some friends in – a little party . . . I don’t know how many people were here. Do you have to have a number? Twelve and a half, how’s that? When? No! We agreed to two months, didn’t we? What? I can hardly hear you . . . What? We’ll talk tomorrow. Goodbye.

DON: (To audience) (pg 10) She didn’t want me to leave home. She thinks I can’t make it on my own. Finally, we agreed to letting me try it for two months. She’s to keep away from me for two months. I’ve got a month to go . . . I always tell her I’ve had a party . . or went to one. She wouldn’t understand why I’d rather be here alone than keeping her and the cook company. She’ll hate this place. She’ll walk in and the first thing she’ll say is, “I could absolutely cry!” As far as my mother’s concerned, I’m still eleven . . . going on ten. (pg 14) [Oh, yeah, and] I’m blind. I’ve always been blind. (Pg 15) Please don’t feel sorry for me. The one thing that drives me up the wall is pity. (Pg 24-25) You may have heard of [my mother]. She wrote a series of children’s books. Guess what they were about? (Beat) A kid named little Donny Dark. It’s true, I swear. I hate the name Donny. Donny is twelve years old and was born blind like me only it’s no handicap to Little Donny Dark. He can drive cars and fly planes, ‘cause, you see, his other faculties are so highly developed that he can hear a bank being robbed a mile away and he can smell the Communists cooking up a plot to overthrow the government. And at the end of every book, as he is being given a medal from the police or the C.I.A., he always says, “There are none so blind as those who will not see!” (Pg 26) I guess the books were sort of a projection of what my mother hoped I’d be – a sightless superman. (Pg 38)

(Don notices a change in the atmosphere, turns and says) Mom . . . what are you doing here? We had an agreement.

MRS. BAKER: I was in the neighborhood. I bought you some shirts and I thought you’d have them sooner if I brought them myself.

DON: I don’t need any shirts. You just brought them as an excuse to come down here.

MRS. BAKER: (looking around the tiny apartment) And this is what you left home for? It isn’t Buckingham Palace, is it?

DON: (Pg 41) (to audience) I was so sure she’d walk in and say, “I could absolutely cry.” She let me down.

MRS. BAKER: We’ll there’s only one thing to say. . . Perhaps it’s a blessing that you can’t see what you’re living in.

DON: Right, Mom. I count that blessing every time I come in the door.

MRS. BAKER: Donny, can I be honest? . . . I am shocked and appalled. I could absolutely cry! (Donny reacts with a “I won” gesture) (Pg 42) I am not just talking about this rat hole, Donny, I am talking about you, too. You’re so thin. You’ve lost weight.

DON: I haven’t lost anything. I’m exactly the right weight for my height – and my age – eleven.

MRS. BAKER: (Crossing to the refrigerator) I’d like to see what you’re eating. (Opens the refrigerator and looks in) There’s nothing in here but lettuce . . . and an apple!

DON: (Pg 45) You’re not supposed to be here for another month. Why did you have to come today, huh?

MRS. BAKER: (Steps toward Don) Since when do you speak to me like this?

DON: Since when do you come sneaking into my room like this?

MRS. BAKER: I didn’t come sneaking in. The door was unlocked.

DON: You could have knocked. I thought it was a raid.

MRS. BAKER: It should have been. (Pg 46) I thought my coming here would be a pleasant surprise for you. Had I known I’d be treated like . . .

DON: (Don cuts her off) You’d’ve come anyway.

MRS. BAKER: And I’m glad I did. My worst fears have been realized. Did you have to choose such a sordid neighborhood?

DON: Thank heaven! My worst fear was that your worst fears wouldn’t be realized. Can you imagine if you came here and liked it? We’d have nothing to talk about.

MRS. BAKER: (Pg 47) You don’t know what you’re talking about. You’ve never been exposed to life.

DON: Whose fault is that? Whose fault is it I didn’t go to school with other kids?! (to audience) (Pg 15) I was six years old before I found out everyone else wasn’t blind. . . (Pg 48) (back to Mom) There are schools for blind children.

MRS. BAKER: We could afford to have you taught at home. I thought that was better than sending you off with a bunch of blind children like . . a leper.

DON: Is that how you see me – like a leper? Come on, Mom, deep, deep down haven’t you always been just a little ashamed of producing a blind child? (beat)

MRS. BAKER: (avoids the question – she turns to Don enthusiastically) Donny, I have a wonderful idea! You come home with me. (Don shakes his head) (Pg 49) If you insist on staying here, I will not support you. I’m serious, Donny! What are you going to do for money?

DON: I can always walk along the street with a tin cup . . . Don’t worry, Mom. (beat) [Fine] I’m going to sing and play the guitar. I’m pretty good. You’ve said so yourself.

MRS. BAKER: I didn’t know you were planning to make a career of it. May I ask how you arrived at this brilliant decision?

DON: My dear mother – by the process of elimination. I made a list of all the things I couldn’t do . . . like commercial pilot. (Pg 50) Photographer? A definite out – along with ball player and cab driver. I half considered becoming an eye doctor, but that would just be a case of the blind leading the blind. That was a joke, Mom. (Mrs. Baker finds Don’s suitcase and starts packing his clothes) What are you doing?

MRS. BAKER: What I should have done long ago. I’m taking you home. You cannot stay here alone!

DON: (Pg 51) Mom, please stop worrying about me. (Don takes the suitcase away from his mother, who relinquishes it with resignation) I’m going to be all right. If the music doesn’t work out, I can always study law or technology. There are lots of things blind people can do now . . . (Pg 50) [and] I have friends. I’m not alone.

MRS. BAKER: Oh, don’t think you’ve fooled me with all your parties. There are no parties! You have no friends, Donny!

DON: (Pg 62) Don! . . . Donald! You can call me Sebastian or Irving. I don’t care. Anything but Donny! (Pg 61) It reminds me of Little Donny Dark.

MRS. BAKER: (Pg 70) Do you remember the first Donny Dark story? You were five years old. We were spending the summer on [the] lake. It was the first time you’d been in any water deeper than a bathtub. You were terrified. They could hear you screaming all over New Hampshire. Dad brought you in and I told you a story about a little blind boy who could swim the seven seas and could talk to the dolphins.

DON: (remembering, bitterly) Yeah . . . and the dolphins told him about enemy submarines on their way to destroy the United States Navy and Donny Dark swam home in time to save them. What a lot of crap.

MRS. BAKER: The next day you learned to swim! (Pg 71) I didn’t write those stories hoping for a Pulitzer prize. I wrote them because I found a way to help you. Whenever you felt discouraged or defeated, I told you a Donny Dark story . . . and you tried a little harder and you did a little better. (beat - considering) You’re not the boy who left home a month ago. I came down here today hoping you were. It’s hard to adjust to not being needed anymore. But I can do it . . . you get on with your own life. I love you, Don. (Mrs. Baker leaves)

DON: (picks up his guitar and plays/sings) * I knew the day you met me, I could love you if you let me, though you touched my check and said, How easy you’d forget me . . . You said . . . (he now has the words) (Pg 20 ) Butterflies are free and so are we . . . (to audience) [You like it?] I wrote it . . . I’ve been working on it, but I could never get those last lines right. (sings again) Butterflies are free and so are we . .
```

---

## IC-1334: Chomp

- Title: Chomp
- Author (byline): Carl Hiaasen
- Work: Not specified
- Publisher: Yearling
- Publication date as stated: March 2020
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: RAVEN, NARRATOR, DEREK, WAHOO, MICKEY, DIRECTOR, FROM THE TAPE, SECRETARY, SICKLER, CATERER
- Teaser before the introduction: Yes
- Spoken words (computed): 1251
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carl Hiaasen
ISBN: 978-0593177662
Publisher: Yearling
Date (Month/Year): March 2020
```

### Introduction (context only: never use it for content warnings)

```text
Are you a fan of survival-skills TV or wildlife documentaries? Shows like Naked and Afraid and Steve Irwin’s Crocodile Hunter have nothing on this reality TV show - Expedition Survival! Wahoo Cray and his father Mickey, a professional animal wrangler, are hired to manage the wildlife. Filming begins in Mickey’s homemade swamp, where the reckless Badger ignores Mickey’s warnings and ends up atop a thrashing, angry alligator. When the footage turns out better than anyone expects, Badger orders filming moved to the Everglades to put the real back in reality TV.

Chomp by Carl Hiaasen
```

### Performance text (classify this)

```text
RAVEN: (knocks on door, it is opened by Wahoo – freeze frame)

NARRATOR: (Pg 12) [That woman] with a shining stack of red hair is Raven Stark.

RAVEN: (with a strong accent) I’m Derek Badger’s production assistant. I brought your contract. (Pg 14) One thousand a day, plus location fees and animal rentals. (Pg 15) Where are your pythons? Derek wants a beast. (Derek steps in)

NARRATOR: (Pg 11) Derek Badger - the star of Expedition Survival! (Derek fist pumps to the audience) Every week, Derek parachutes into some gnarly wilderness teeming with fierce animals, venomous snakes and disease-carrying insects. Armed with only a Swiss army knife and a straw, he hikes, climbs, crawls, paddles or swims back to civilization. Along the way, he eats bugs, rodents, even worms—the grosser it looks, the happier Derek Badger is to stuff it into his cheeks. (Derek smiles winningly at the audience, then picks a bug leg from his teeth)

DEREK: (Pg 31) (with an obviously fake Australian accent) Take me to your alligator. Chop Chop!

RAVEN: (Pg 16) (whistles) That’s a monster, eh?

WAHOO: Twelve feet

MICKEY: (Pg 33) (proudly) Six hundred and twenty pounds. (Pg 75) Alice is her name.

DEREK: (Pg 32) She’s perfect! (to Raven) (Pg 38-39) But we can’t stage our biggest scene in some nitwit’s backyard.

RAVEN: It looks like a real-life swamp. You’ll be impressed.

DEREK: No, they’ll be impressed when they see me jump that monster gator.

RAVEN: Not happening. The insurance company says no way.

DEREK: They said the same thing about the cobra dance, but I did it anyway.

NARRATOR: They had been shooting Expedition Survival! in Cambodia when Derek decided to play snake charmer with a spitting cobra that had been rented from a local handler. Mr. Na leaped between Derek and the dangerous reptile just as it released a jet of deadly poison. A few drops landed in Mr. Na’s hair, and as a precaution he rushed off to take a shower. Upon returning to the set was dismayed to learn that Derek had chopped up his pet snake with a rusty machete and eaten it in the program’s final scene. *******

NARRATOR: (Pg 43-44) [The next day] Wahoo and his father uncoiled the python, Beulah and laid her out at full length. The script called for Derek to creep up and seize Beulah behind her head, instigating a fake life-or-death struggle.

DIRECTOR: (airhorn blows) Episode 103 – Expedition Survival! Action!

DEREK: (Pg 44-46) (whispering dramatically into a microphone on his shirt collar as he sneaks up on Beulah) “As if the Everglades weren’t dangerous enough, in recent years this tropical river of grass has been invaded by lethal predators from another continent— Burmese pythons! They can swallow a whole deer, a panther and, yes, even a human being. Look! There she is!” (pounces with a triumphant cry and grabs Beulah 2 feet below her head) “I’ve got her! I’ve caught the beast! (grunting and huffing he ‘struggles’ with the docile Beulah – it’s like fluffing a pillow)

DIRECTOR: Cut! Cut!

DEREK: (Pg 47) (lurching to his feet – he slams the python to the ground and confronts Mickey) That’s the worst excuse for a python I ever saw! You call that a snake? Ha! I call it an overstuffed earthworm. (disgusted with this scene, he moves on) What about the gator?

WAHOO: (Pg 52) Showtime!

DIRECTOR: (Pg 44) (airhorn blows) Episode 103 – Expedition Survival! Action!

NARRATOR: (Pg 60) Wahoo and his father peeked over the cameraman’s shoulder. The screen showed a view from the submerged camera. And there was Alice.

MICKEY: She won’t touch him. Not on a full belly.

DEREK: (Pg 58-59) (to crew) No mistakes! (he slips into the pond up to his neck - to camera) “Soon the sun will be setting over the Everglades. I must swim across this deep, murky pond to reach dry ground. Getting across this water is absolutely crucial to my survival but I’ve discovered fresh signs of an extremely large alligator, and I mean HUGE, lurking close by! If that monster were to attack me right now, the only chance I’d have of escaping alive would be to fight back ferociously, desperately, and gouge it in the eyes.”

WAHOO: (Pg 65) She’s coming up! Don’t move!

NARRATOR: (Pg 64) Slowly but surely, Alice was rising from the bottom of the pool.

DEREK: (Alice comes up underneath Derek; suddenly he is straddling her like a tipsy cowboy on a bronco) (Pg 66) Wooo-hooo! (hollering idiotically – he grabs her scales to hold on)

RAVEN: Oh, Lord. (Pg 68) (shrieking) Shoot it! Shoot it! Shoot that thing!

DEREK: (Pg 66) Wooo-hooo!

NARRATOR: (Pg 67) Members of the Crocodilia order of reptiles don’t buck like horses do when shedding an unwanted rider. Instead, they thrash and spin. Derek managed to hang on for three full revolutions before being launched airborne. (watch Derek’s arc through the air -- Splash!) *****later that night*****

DIRECTOR: (Pg 71) I brought something to show you (holding up a disk) The pond scene.

(puts the disk into a DVD player)

RAVEN: Let’s get this over with. (They watch becoming more excited)

FROM THE TAPE: (Pg 66) Wooo-hooo!

DIRECTOR: (Pg 72) Well?

DEREK: That was bloody. . . brilliant! (punches the air jubilantly with both fists) I almost died, didn’t I? That vicious monster almost killed me! (Pg 75-76) The most extraordinary 33 seconds of footage in the history of Expedition Survival! (Pg 86) (dreamily) The rest of the show must all build up to this incredible, heart-stopping moment. We’ll spare no expense!

MICKEY: (Pg 76) But you almost got drowned.

DEREK: Exactly! And the best part is it was real! We’re hiring you to lead us into the Everglades to put finishing touches on this masterpiece!

MICKEY: (disappointed) (Pg 134) All due respect, Mr. Beaver, this ain’t my first rodeo. (Pg 76) You’re gonna fake the rest of it, same as you always do.

RAVEN: In our line of work, it’s known as ‘re-creating’ events for the camera.

DEREK: (Pg 87) No more faking it, mate. (Pg 86) No tame animals. This time we’re going totally raw and wild. (Pg 87) We’re putting the ‘real’ back in ‘reality.’ *****

NARRATOR: (Pg 89) Mickey Cray was surprised to learn that Derek Badger didn’t want any of his captive critters on location.

MICKEY: Seriously. The man almost got killed by the world’s laziest alligator!

RAVEN: (Pg 97-98) We cannot have a repeat of what happened with your alligator. We need Derek in one piece. He’s the whole franchise.

NARRATOR: (Pg 103) But Raven Stark’s request to base the program in Everglades National Park had been rejected. [They] informed Raven that, because of the earlier egg-robbing incident at Yellowstone, Derek Badger had been blackballed from the entire federal park system.

RAVEN: (on the phone) For how long?

SECRETARY: Eternity.

NARRATOR: The crew of Expedition Survival! was using Sickler’s Jungle Outpost and Juice Bar.

SICKLER: (waves to audience, thumbs up) (Pg 95) I just repainted the place!

(PG 40) [a rumpled assistant begins spraying Derek’s arms and legs. Derek cooperates, then closes his eyes and holds his breath as the assistant mists his face]

WAHOO: What is that stuff?

RAVEN: Spray-on tan.

MICKEY: What a poser!

DEREK: (Pg 52-53) So what am I supposed to eat to survive. For the show, I mean.

RAVEN: (applying make-up to Derek) The script calls for bullfrogs and crawdads.

DEREK: (dismissively) What else? I want something truly disgusting.

RAVEN: How about maggots?

CATERER: (Pg 149) (Off stage a piercing scream)

NARRATOR: One of the catering staff was hopping frenetically and pointing at a furry, twitching intruder that lay quivering on the cake platter.

DEREK: (strides over to the table to examine it – he grins) Just as I suspected – a bat! (he licks his lips) Let’s do this! Set up some lights!

DIRECTOR: (Pg 44) (with little enthusiasm) Episode 103 – Expedition Survival! (Pg 133) Action!

DEREK: (Pg 155-157) (to camera) Deep in the Everglades, the swamp is unforgiving and food is scarce. Survival means eating whatever you can get your hands on. But by sheer luck, the violent weather has literally dropped on my platter a tasty morsel that will provide enough nutrition to get me through another brutal day in this tropical wilderness. Look! (dangles the bat by its tail) Unfortunately, the rain has soaked all the tinder, so I can’t make a fire for cooking. That leaves me only one choice. Now, please don’t try this yourself—wild bats can be vicious, and their teeth are needle sharp. Remember, I’m an experienced survivalist. I know how to handle these unpredictable rascals. . . (he tilts his head back and dramatically begins to lower the bat into his mouth)

NARRATOR: (as Derek pantomimes) The bat wasn’t vicious. She simply didn’t want to be eaten. She reacted defensively and without hesitation and chomped down on the first chompable target. (Derek screams) Which happened to be Derek’s plump tongue.

DIRECTOR: (Pg 159) Zoom in for a close-up! Hurry! (but Derek runs, still screaming into the swamp) ****** days later Derek hiding in the swamp*****

DEREK: (Pg 266) (Using his cell phone to film himself – his speech is distorted due to a swollen tongue) My harrowing Everglades adventure is finally drawing to an end, and not a moment too soon. I’m completely out of food, out of water and dangerously weak after being attacked by a rare but deadly vampire bat. Its savage bite left me dazed and delirious, racked with fever. Why, at times I even imagined myself morphing into a real-life vampire!

NARRATOR: (Pg 168) It would be a humongous night for the show’s TV ratings if Derek Badger failed to survive one of his survival expeditions!

RAVEN: (to audience, almost cheerfully) It’s possible the bat had rabies. Derek could be losing his mind.

DEREK: (Pg 115) (desperately paranoid and scared) Time is running out. [When] the sun goes down, the predators come out – alligators, panthers, bears, pythons. (Pg 186) My only hope is that somebody finds me way out here before it’s too late . . .

NARRATOR: [*Turn in next time for the chilling conclusion of] Episode 103 – Expedition Survival!] (*bracketed words have been added as a transitional ending – not in the original novel)
```

---

## IC-1335: Coming Attractions

- Title: Coming Attractions
- Author (byline): Ted Tally, Jack Feldman and Bruce Sussman
- Work: Plays from Playwrights Horizons, Pgs 273 - 326
- Publisher: Broadway Play Publishers
- Publication date as stated: May 1987
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: COP 1, LONNIE, MANNY, COP 2, NEWSMAN, TV REPORTER, CHIEF BRADDOCK, TV NEWSMAN, MISTER X, MISS AMERICA, SHRINK, SAMMY
- Teaser before the introduction: Yes
- Spoken words (computed): 1712
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ted Tally, Jack Feldman and Bruce Sussman
Book: Plays from Playwrights Horizons, Pgs 273 - 326
ISBN: 978-0881450477
Publisher: Broadway Play Publishers
Date (Month/Year): May 1987
```

### Introduction (context only: never use it for content warnings)

```text
Small-time crook Lonnie Wayne Burke is a born loser when it comes to crime. But with the help of streetwise theatre agent Manny Alter, he becomes the next media sensation following in the footsteps of . . . Charles Manson, David Berkowitz and Ted Bundy. This selection looks at our celebrity-obsessed society and the lengths to which some will go for fame and fortune.

Coming Attractions by Ted Tally, Jack Feldman and Bruce Sussman
```

### Performance text (classify this)

```text
(Lights rising slowly on LONNIE WAYNE BURKE. He is perhaps 25 and is holding a revolver. Nearby are his Four HOSTAGES… Their hands are tied; they are gagged.)

COP 1: (Pg 278-279) Give up, kid! You haven't got a chance.

LONNIE: (shouts through a window) Come in and get me, you scumbags! (3 gun shots. He ducks)

MANNY: (Cut to Manny who narrates. He has a tape recorder slung over one shoulder by a strap. to the audience) The first time I met Lonnie, he was just a scared punk with a two-dollar handgun.

LONNIE: (shouts) Hey! Send a reporter in here! I got a list of demands.

MANNY: He was trying to knock over a laundromat when the owner tripped an alarm. Lonnie ended up with four hostages, and a year's supply of clean socks.

LONNIE: (shouts) I'll blow [them] away, I swear to God. Now gimme a reporter.

MANNY: (enters scene) Hey! I'll talk to him.

COP 2: Are you a reporter?

MANNY: (evasively) I got a tape recorder.

COP 2: Well, get in there and see what he wants. But don't try to be a hero.

LONNIE: (Pg 279-282) Hold it right there. (Manny freezes) Get your hands up. Up! (Manny raises his hands) What's in the box?

MANNY: Tape recorder. See for yourself. (Lonnie looks at the case, then steps back.) You mentioned a list of demands?

LONNIE: Yeah, that's right. Turn that thing on. (Manny pushes a button on the recorder, holds out the mic) Okay. This is the guy with the gun. I got four hostages and I'm gonna waste 'em if I don't get [what] I ask for. I want a camera crew in here. I want the story of my life to be shown on Sixty Minutes. Over and out! (to Manny) What network are you from?

MANNY: Network? You gotta be kidding. For four lousy hostages? There's a woman barricaded in the shoe department at Bloomingdale's, and she's got a hundred and fifty. Forget it, kid. For four lousy hostages, no reporter's gonna cross the street. (Lonnie looks dejected) My name's Manny Alter -- I'm a theatrical agent!

LONNIE: You mean like -- actors? That kinda agent?

MANNY: Actors, magicians, dog acts. I was walking by - got curious. I went in the five-and-dime and stole this tape recorder -- thought you and me might have a little chat. (Lonnie edges to "window," peeks out) There's no reporters out there, kid. Not a single one.

LONNIE: (miserable) I'm a failure. I can't even make the six o'clock news. What's WRONG with me?

MANNY: You're vicious, but you got no vision. Nowadays, everybody's into crime. That makes it tough on a kid just starting out. You need a gimmick. See this? (holds up left hand) This is crime. And this is show biz. (holds up right hand) Now watch closely. (claps) That's money, kid. Get the picture?

LONNIE: I can't get in show biz. I got no talent.

MANNY: Don't ever say that again. You got a special gift. How many guys can put a gun up to somebody's head and blow their brains out?

LONNIE: Millions.

MANNY: Sure . . . But how many know how to market that talent?

LONNIE: You really think I could be a star?

MANNY: Kid, I know it! One thing I got, it's a great eye for potential. (offers his hand)

LONNIE: Okay, it's a deal! (shakes his hand.) But, what do I do now? (indicates the hostages)

MANNY: Ever been arrested before?

LONNIE: Plenty of times.

MANNY: You'll be back on the streets in 24 hours. (yells to police outside) He’s coming out!

Don’t shoot! (to audience as Lonnie exits with his hands up) Tell you the truth, I had doubts. I mean, he wasn't exactly another Manson or a Berkowitz. He lacked your true weirdness factor, if you know what I mean. But I figured with training and a little luck, we could simulate some craziness. ********* SCENE ********

LONNIE: (Pg 282-284) (enters wearing a child's Halloween costume. A skeleton with a skull mask. He carries a "trick or treat" bag) I feel ridiculous.

MANNY: Put your mask down. Flap your arms. Do something freaky. (Lonnie obeys, with obvious disinterest) Oh, is that ever scary! Now, I'm the guy in the house. C'mon, c'mon, I'm the guy. You ring the doorbell.

LONNIE: Ding dong!

MANNY: I come to the door. It's pitch black outside, and nobody's there! Ooooh, I got chills already! Then suddenly you jump out, and you say . . .

LONNIE: Trick or treat, you bourgeois pig.

MANNY: You gotta say it like you mean it. Say it scary.

LONNIE: Trick or treat; you bourgeois pig!

MANNY: (in character) “Oh my God, it's him! It's that hot new psychopath!” And you take your gun out of your bag and blast me, right between the eyes! (Lonnie takes gun out of "trick or treat" bag and pretends to fire several rounds) Big headlines all over the place! (pause) What's the matter? I thought we agreed on this.

LONNIE: You agreed. How do you expect me to murder people when I feel ridiculous? Why can't I just march up to the door and blast 'em?

MANNY: Because that's not gonna sell any newspapers.

LONNIE: Well, I don't like it. It ain't my style of crime.

MANNY: Crime shmime. I'm talking about journalism. (Lonnie is unconvinced) Look, just wear the suit for the first three or four murders. That's all I'm asking. . .

LONNIE: That's just publicity. How much you think some editor's gonna pay to put my face on his cover? Hell with publicity, Manny! When do I start getting some bucks?

MANNY: You want bucks? For starters let's talk non-fiction book rights. The True Story of Mad Dog Lonnie! Still not enough? Let's talk film sale! And kids' toys, for Chrissake. Little plastic psychopath and victim dolls! And your face on everything -- tee shirts, posters, candy bars! (Pg 286) (to audience) After that, things happened quickly.

NEWSMAN: (Pg 285) [This just in] Metropolitan police denied any link between yesterday's brutal midtown slaying and an identical murder last week in the suburbs. In each case, eyewitnesses report the killer wore a child's skeleton costume and shouted political slogans.

TV REPORTER: (Pg 286) (News theme music) Newsflash! The Halloween Killer struck again, claiming his fourth, fifth, and sixth victims.

CHIEF BRADDOCK: We're looking for a man between 20 and 45 years of age, between four-foot-eight and six-foot-five, and weighing 135 to 250 pounds. If anybody should see such a man, contact this department immediately!

MANNY: (Pg 287) (to audience) The kid was sensational beyond my wildest dreams.

LONNIE: (Pg 289) I feel terrific, Manny. It’s like I’m in the movies.

MANNY: (Pg 290) Keep it up and you soon will be. We couldn’t buy the kinda publicity you’re getting. (Pg 291) (to audience) Things were going so great that I began to worry. It seemed like every fruitcake in the country was trying to get a piece of the action.

TV NEWSMAN: (Pg 292) (news theme music) With me in our studio is a man who claims to be the Halloween Killer. Mister X, in the last two weeks, more than a hundred crackpots have turned themselves in, all claiming to be the Halloween Killer.

MISTER X: (with a horrible French accent) You want proof? (points finger like a gun) Bang! Bang! Trick or treat, you bourgeois pig!

MANNY: (Pg 293) (to audience) When I saw that, I knew I either turned Lonnie in, or the cops would never get him. So I gave Chief Braddock a call. (on phone.) Chief Braddock? Word is, the Halloween Killer is planning a big finale for Atlantic City Saturday night. Network TV -- the works. Be there and you got him. ********* SCENE BREAK ******** We see Lonnie in a long gown, heels, a wig and a sash. He fixes his breasts, applies lipstick and prepares to go on-stage while Manny narrates the following

MANNY: (Pg 293-295) (to audience) Call it irresponsible ... but I wanted the kid to be captured while a national spotlight was on him. So we disguised him as Miss Wyoming, and he got all the way through swimsuit without anybody noticing. (Lonnie plays to the audience)

(Music. Miss America has just been crowned. She carries a scepter and a bouquet of long-stemmed roses. MUSIC fades)

MISS AMERICA: (In stilted poetic language) What does America mean to me? A Lady with her torch on the shining sea / A Golden Bridge near a redwood tree . . . (Lonnie takes gun from his sash and interrupts her acceptance speech)

LONNIE: (In a fake woman’s pageant voice) Trick or treat, you bourgeois pigs! (Miss America screams and Lonnie fires his gun randomly)

MANNY: (to audience) As luck would have it, some of Lonnie's shots hit the judges' table. (pause) And that's how they finally caught the dreaded Halloween Killer. . . The newspapers? Well, lemmee put it this way -- if the Second Coming had happened that same day, you woulda read about it on page ten. The courts? They turned the kid over to the headshrinker. And Lonnie was ready for 'em. ********* SCENE ********

(LONNIE speaks in his natural voice, not attempting to sound like a woman.)

SHRINK: (Pg 296-297) State capital? LONNIE: Cheyenne.

SHRINK: State bird? LONNIE: The meadow lark.

SHRINK: Principal industries?

LONNIE: Cattle, oil, and tourism. (slips into his woman’s persona as if on stage answering an interview question) I'm especially proud to represent Wyoming in this year's pageant because my state was the first to ratify women's right to vote. (curtsies -- in his own voice again) This is part of my personality interview, isn't it?

SHRINK: (pause) Miss Wyoming, you're wearing a dress . . . And yet, before you came here, you used to dress up in a skeleton costume. Can you tell me why that was?

LONNIE: (in his woman’s persona) That was the ceremonial garb of the Arapaho Ghost Dance, which is still held on reservations throughout our state. The Ghost Dance comes before a large tribal hunt.

SHRINK: I see . . . So all those people that you shot . . .

LONNIE: (in his own voice again) You mean the buffalo?

SHRINK: (to audience) Lonnie Wayne Burke is convinced that he is Miss Wyoming -- a psychic trauma of profound dimensions. We must set him free to atone for our crimes against his psyche. ********* SCENE ********

MANNY: (Pg 298) Well, kid? Huh? Huh? Did I tell you?

LONNIE: It happened just like you promised. "Small crime, serve time. Big crime-gold mine!"

(both whoop with laughter)

MANNY: I knew you'd never spend one second in the slammer, not after you passed your whacko test. Now all we gotta do is rake it in! (Pg 300) (to audience) I shoulda smelled trouble. You tell some two-bit punk that he’s a star enough times, and pretty soon he’ll start believing it. He worked day and night on his new club act. [And] when the time came for his TV debut, all I could do was cross my fingers and hope we were ready. . . ********* SCENE ********

SAMMY: (intro music for talk show) (Pg 304-307) AWRIGHT! I know you're all anxious to meet tonight's special guest. He's a Megadiscovery. Ladies and gentlemen, welcome my new best friend - the "Singin' Psychopath" – Mister. Lonnie. Wayne. Burke! (gestures broadly)

LONNIE: (Singing) JUST LOOK AT ME NOW! / I SET MY SIGHTS AND TOOK A SHOT AT DESTINY. / I KNEW THAT I COULD HIT THE MARK SOMEHOW. (Spoken as music continues) Me? I was always the shy kid, the one who got beat up at recess. But even then I had a dream! I'll never forget telling my favorite teacher about it. "Mrs. Von Zell" She smiled at me and said. "Lonnie Wayne, sweetheart . . . go see the school nurse." (Singing) WELL, WELL, MRS. VON ZELL, / JUST LOOK AT ME NOW! / JUST LOOK AT ME NOW! (bows)

SAMMY: Hey, Lonnie -- come over here and talk to me! I just gotta ask ya. You've gunned down 27 people, you've appeared on my show. Which was the bigger thrill?

LONNIE: Gotta be your show, Sam. No contest.

SAMMY: Now you're still under indictment, izzat right? Out on bail . . .

LONNIE: Out on bail, right.

SAMMY: Lonnie, now tell the truth. Somewhere down the line, you have to go on trial. What if - long shot, Lon, but stay with me here - WHAT IF you're actually convicted?

LONNIE: (humbly) Sammy, my lawyers tell me this thing could drag through the Appellate Courts for ten years. Until it's finally settled, I just can't let it affect how I perform. I owe that much to my fans.

SAMMY: Thank GOD for America, ladies and gentlemen, where everyone is entitled to all the justice he can afford. Ladies and Gentlemen- LONNIE WAYNE BURKE!

LONNIE: (Singing as he exits) JUST LOOK AT ME NOW! / I SET MY SIGHTS AND TOOK A SHOT AT DESTINY. / I KNEW THAT I COULD HIT THE MARK SOMEHOW. / JUST LOOK AT ME NOW!
```

---

## IC-1336: Commercial Break

- Title: Commercial Break
- Author (byline): Augusten Burroughs
- Work: Magical Thinking: True Stories, Pgs 1-16
- Publisher: St. Martin's Press
- Publication date as stated: Oct 2004
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: AB, MRS. AMES, MAN 1, DAD, DIRECTOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1612
- Already set (do not supply): none

### Source block (context only)

```text
Author: Augusten Burroughs
Book: Magical Thinking: True Stories, Pgs 1-16
ISBN: 978-0312315948
Publisher: St. Martin's Press
Date (Month/Year): Oct 2004
```

### Introduction (context only: never use it for content warnings)

```text
TV VOICE:
```

### Performance text (classify this)

```text
AB: (Pgs 1-16) When I was seven, I was plucked out of an uneventful life deep in darkest Massachusetts and dropped into a Tang Instant Breakfast Drink commercial. It was exactly like being abducted by aliens. I was a lonely kid with entirely imaginary friends. I played with trees. Then, one day during penmanship class, a white van pulled up in front of our little gray schoolhouse, and the men from Tang climbed out.

Enjoyed by consumers in more than 60 countries, Tang is one of Kraft’s most global brands and one of our largest. Kraft holds the number one position in powdered beverages in the world and our Tang brand is an important part of that portfolio. The combination of the great fruit taste of Tang, its nutritional benefits, convenience and affordable price has made it a favorite among millions. Since the early '80s, Tang has been launched in approximately 30 countries. And now back to your regular programming. . . Thanks for your attention during this Commercial Break by Augusten Burroughs.

AB: I was sitting in Mrs. Ames's tedious penmanship class looking out the window when the white van pulled into the circular driveway. Mrs. Ames noticed, too, because she paused in the middle of looping a “D”. Visitors were uncommon at our school. Especially visitors dressed in dark suits, wearing sunglasses, and carrying black briefcases. When [Mrs. Ames] turned her ancient neck to the window, my mind added the sound effect of a branch creaking under the weight of snow before it snaps. I was quite sure that Mrs. Ames was one of the original settlers of the town. She once said that television was (imitating Ames) "nonsense, just a fad like radio."

MRS. AMES: (glaring at the class) Remain seated and do not talk. I shall return in a moment.

AB: A moment later, Mrs, Ames joined the men outside and, to my horror, smiled. I'd never seen Mrs. Ames smile before, and the thought had never occurred to me that such an act was even possible. But there it was, her mouth open in the white daylight, her teeth exposed. (smile as Mrs. Ames) One of the men stepped forward, removed his sunglasses, and said something to her. She touched her hair with her hand and laughed. I was horrified to see Mrs. Ames laugh. And then blush. To see her in such a state of obvious bliss was un-bearable. I had to look away.

Eventually, Mrs. Ames walked back into the room, and I watched her legs, all plump and plastic-looking through her support hose. She wore high heels of an unfashionable style that made a sharp, angry sklack against the tile floor when she walked.

MRS. AMES: Children, children, may I have your attention please? (clapping her hands) "We have some very special surprise guests here today. These men are here to make a television commercial.

AB: Well, I almost peed. She might as well have told me that I never had to come to school again and I was free to hit anybody I wanted to, without being punished. I loved television commercials. The only reason I watched TV was so that I could see the commercials. Faberge Organics Shampoo: (imitating the commercial) "I told two friends. And they told two friends. And so on. . . and so on. . . and so on." Or my current favorite: (imitating the commercial) "Gee, your hair smells terrific!" I was also fond of the commercial with little dog chasing the chuck wagon underneath the kitchen sink.

MRS. AMES: (to the class) These men would like to put our schoolhouse in a commercial for Tang. Do any of you know Tang?"

AB: There were gasps in the room. Of course, we knew Tang, the orange crystalline powder that the astronauts brought with them to outer space. I loved Tang and would sometimes eat it by the teaspoon, straight from the jar. I loved the green label, the orange lid. The way the lid was extra wide and easy to unscrew. I even liked the paper eardrum that was over the mouth of the lid when you first opened the jar. You had to puncture the eardrum with a spoon, and printed on top was "Tang, Tang, Tang."

Mrs. Ames told us that the men wanted to use some of us in their commercial. Instantly, the students began raising their hands. Except for me. Some voice inside me said, "Don't do it. It's beneath you." Instead, I sat politely at my desk with my hands clasped firmly together. One thing was certain: I would be in their Tang commercial.

The interviews began in groups of three. When it was finally my turn, the men were tired, as evidenced by their loosened ties and the large wet spots that spread under their arms. They'd spoken to thirty kids and had notes piled on the table in front of them.

MAN 1: Hi guys. So do any of you want to be in a commercial? (AB nods vigorously) Good. So, I'm gonna tell a joke, and I want to see what it sounds like when you laugh. Ready? Okay. (raises voice and makes a comical face) Your mother wears army boots!

AB: (looks left, then right) Neither of the other kids laughed. (laughs hysterically, then proudly) I was able to bring tears to my eyes. My face was flushed, my hands dripping with sweat.

MAN 1: Wow, you really liked that joke, did you? Do you kids like Tang?

AB: The other two kids nodded grimly. (to man, gushing) I love Tang! Only I like to make it with an extra scoop. Plus, you can put it in ice cube trays and then freeze it! (to audience) Where had that come from? I'd never in my life frozen Tang.

MAN 1: That's great! What's your name?

AB: Augusten?

MAN 1: Augusten. You were great. We want you.

AB: As soon as I got home, I sprinted up our gravel driveway and threw open the front door, screaming "I'm gonna be in a Tang commercial! I'm gonna be in a Tang commercial!" In preparation for my television acting debut, I watched commercials incessantly, committing them to memory and reciting phrases endlessly. (as if on camera. . .) (in a high-pitched girl’s voice) Can I help you fry the chicken?

(different southern girl’s voice) I want to help! (imitating their mother) I don't fry chicken anymore. I use new Shake 'N Bake. (mimicking another commercial) Let's get Mikey to try it. He won't eat it; he hates everything!

I loved to sing jingles. (singing) * “That great Pepsi taste. Diet Pepsi won't go to your waist. Now you see it. Now you don't. Oh, Diet Pepsi one small calorie. Now you see it. Now you don't.”

DAD: Son, what's the matter with you? If you don't stop that noise, you won't be in any commercial. You'll be back in your room practicing penmanship.

AB: Oh, Diet Pepsi one small calorie. Now you see it. Now you don't . . . (trailing off) This muted me, briefly. Long enough to contemplate his sudden death and wonder how I would ever be able to produce convincing tears. Onions, I'd heard, could do the trick if you applied just a small bit of the juice under your eye. I tried this myself, thrilled with the weepy, sincere results: (dramatically) Oh Dad! Boo-hoo-hoo. *****The next day at filming****

DIRECTOR: (angrily) CUT! Why is this so hard for you? All you have to do is say 'Hey, Mark, where are you going?' That’s all you have to say. Why are you having so much trouble with this?

AB: I don't know. Something is throwing me out of character.

DIRECTOR: What are you talking about You’re a kid in a school. . . playing a kid in a school!

AB: We’d been shooting for over an hour. It was a simple setup: I was walking behind a group of other kids when I suddenly see my friend, Mark. I pause, turn toward the camera without looking at it and say, "Hey, Mark, where are you going?" But I just couldn't do it. Each time I spoke my line, my voice sounded forced, pretentious, dishonest. These were concepts I'd gleaned from a copy of Acting: A Handbook of the Stanislavski Method, which I'd found on my mother's bookshelf.

The other problem was that I didn't feel I had found my character. Why was I walking down the hall? Was I going to class? Or coming from class? These were essential questions, and the director refused to provide answers.

DIRECTOR: Will you shut up and just walk! ACTION!

AB: And I began my walk down the hallway, fully aware of the camera trained on my every move. I concentrated hard on being normal. But I could feel it happening. Like being the passenger in a car speeding out of control, I was unable to stop myself. (in a high-pitched and overly rehearsed tone of voice) "Hey, Mark, where are you going?"

I waited for the director to again scream "Cut!" but instead there was silence. And then I felt a rush. Had I done it? Had I accidentally done it exactly right? (biting his lip to repress the smile)

DIRECTOR: Forget it. We'll fix it in the edit. This is a wrap! *****Scene change*****

AB: Finally the day arrived. My mother turned on the Today Show, and we watched for nearly an hour before it came on. I saw myself for a split second, in back of a bunch of kids. One girl said, "Hey, let's go get some!" and the scene cut to Mrs. Ames at home serving Tang to her grandchildren for the rest of the commercial. My line had been cut! Mrs. Ames hijacked the commercial!

Depressed, I walked down the hall to my room. (in a natural voice) “Hey, Mark, where are you going?" I realized at once that this is what the director had wanted all along. He didn't want passion, meaning, and nuance. He wanted an ordinary kid who would say six words. I decided, right there. I won't be a child actor for television commercials. Instead, I will be the one who thinks up the commercials in the first place. And then I will hire the director myself, and when he can't make the kid give me a passionate, meaningful, and nuanced performance, I'll fire him.
```

---

## IC-1337: Confessions of a Burglar

- Title: Confessions of a Burglar
- Author (byline): Woody Allen
- Work: The Complete Prose of Woody Allen, from Side Effects, Pgs 469-473
- Publisher: Wings Books
- Publication date as stated: March 1991
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: VIRGIL
- Teaser before the introduction: No
- Spoken words (computed): 1626
- Already set (do not supply): none

### Source block (context only)

```text
Author: Woody Allen
Book: The Complete Prose of Woody Allen,
from Side Effects, Pgs 469-473
ISBN: 978-0517072295
Publisher: Wings Books
Date (Month/Year): March 1991
KS State Qualifier
```

### Introduction (context only: never use it for content warnings)

```text
The following are excerpts from the soon to be published memoirs of Virgil Ives, who is currently serving the first of four consecutive ninety-nine-year sentences for various felonies. Mr. Ives plans on working with children when he gets out.

Confessions of a Burglar by Woody Allen
```

### Performance text (classify this)

```text
VIRGIL: (from Side Effects, Pg 469-473) Sure I stole. Why not? Where I grew up, you had to steal to eat. Then you had to steal to tip. Lots of guys stole fifteen per cent, but I always stole twenty, which made me a big favorite among the waiters. On the way home from a heist, I’d steal some pajamas to sleep in. Or if it was a hot night, I’d steal underwear. It was a way of life. I had a bad upbringing, you might say. My dad was always on the run from the cops and I never saw him out of disguise till I was twenty-two. For years, I thought he was a short, bearded man with dark glasses and a limp; actually, he was tall and blonde and resembled Lindbergh. He was a professional bank robber, but sixty-five was the mandatory retirement age, so he had to get out. Spent his last few years in mail fraud, but the postal rates went up and he lost everything.

Mom was wanted, too. Of course in those day s it wasn’t the way it is now, with women demanding equal rights, and all. Back then, if a woman turned to crime the only opportunities open to her were blackmail and, once in a while, arson. Women were used in Chicago to drive get-away cars, but only during the driver’s strike, in 1926. Terrible strike. It lasted eight weeks, and whenever a gang pulled a job and ran out with the money they were forced to walk or take a cab.

I had a sister and two brothers. Jenny married money. Not an actual human being -- it was a pile of singles. My brother Vic got in with a gang of plagiarists. He was in the middle of signing his name to “The Waste Land” when the feds surrounded the house. He got ten years. Some rich kid from a highfalutin family who signed Pound’s “Cantos” got off on probation. That’s the law for you. Charlie -- that’s my youngest brother -- he’s been a numbers runner, a fence, and a loan shark. Never could find himself. Eventually he was arrested for loitering. He loitered for seven years, till he realized it was not the kind of crime that brought in any money.

The first thing I ever stole was a loaf of bread. I was working for Rifkin’s Bakery, where my job was to remove the jelly from doughnuts that had gone stale and transfer it to fresh goods. It was very exacting work, done with a rubber tube and a scalpel. If your hands shook, the jelly went on the floor and the old man Rifkin would pull your hair. Arnold Rothstein, who we all looked up to, came in one day and said he wanted to get his hands on a loaf of bread but he absolutely refused to pay for it. He hinted that this was a chance for some smart kid to get into the rackets. I took that as a cue, and each day when I left I put one slice of rye under my coat, until after three weeks I had accumulated a whole loaf. On the way to Rothstein’s office, I began to feel remorse, because even though I hated Rifkin his wife had once let me take home two seeds from a roll when my uncle was dying. I tried to return the bread, but I got caught while I was trying to figure out which loaf each slice belonged to. The next thing I knew I was in Elmira Reformatory.

Elmira was a tough joint. I escaped five times. Once I tried to sneak out in the back of a laundry truck. The guards got suspicious, and one of them poked me with his stick and asked me what the hell I was doing lying around in a hamper. I looked him right in the eye and said, “I’m some shirts.” I could tell he was dubious. He kept pacing back and forth and staring at me. I guess I got a little panicky. “I’m some shirts,” I told him. “Some denim works shirts -- blue ones.” Before I could say another word, my arms and legs were manacled and I was back in stir.

I learned everything I knew about crime at Elmira: how to pick pockets, how to crack a safe, how to cut glass -- all the fine points of the trade. For instance, I learned (and not even all professional criminals know this) that in the event of a shootout with the cops, the cops are always allowed the first two shots. It’s just the way it’s done. Then you return fire. And if a cop says, “We have the house surrounded, come out with your hands up,” you don’t just shoot wildly. You say, “I’d prefer not to,” or “I’d rather not at this particular time.” There’s a right way to do these things, but today . . . well, why go into all that?

For the next few years of my life I was the best damn burglar you ever saw. People talk about Raffles, but Raffles had his style and I had mine. I had lunch with Raffles’ son once. Nice guy. We ate at the old Lindy’s. He stole the pepper mill. I stole the silverware and napkins. Then he took the ketchup bottle. I took his hat. He got my umbrella and tiepin. When we left we kidnapped a waiter. It was quite a haul. The original Raffles began as a cat burglar. (I couldn’t do that, because the whiskers make me sneeze.) He’d dress up in this best-up cat suit and dart over rooftops. In the end, he was caught by two guys from Scotland Yard dressed as dogs. I suppose you’ve heard of Kissing Bandit? He’d break into a joint and rob the victim, and if it was a woman he’d kiss her. It was sad the way the law finally nailed him. He had two old dowagers tied up and he was prancing in front of them singing “Gimme a Little Kiss, Will Ya, Huh ?” when he slipped on a footstool and fractured his pelvis.

Those boys made all the headlines, but I pulled off some capers that the police never did figure out. Once, I entered a mansion, blew the safe, and removed six thousand dollars while a couple slept in the same room. The husband woke up when the dynamite went off, but when I assured him that the entire proceeds would go to the Boys’ Clubs of America he went back to sleep. Cleverly, I left behind some fingerprints of Franklin D. Roosevelt, who was President then. Another time, at a big diplomatic cocktail party, I stole a woman’s diamond necklace while we were shaking hands. Used a vacuum cleaner on her -- an old Hoover. Got her a necklace and earrings. Later, when I opened the bag I found some false teeth there, which belonged to the Dutch Ambassador.

My most beautiful job, though, was when I broke into the British Museum. I knew that the entire floor of the Rare Gems Room was wired and the slightest pressure on it would set off an alarm. I was lowered in upside down by a rope from the skylight, so I wouldn’t touch the ground. I came through neat as you please, and in a minute I was hovering over the famous Kittridge Diamond in their display case. As I pulled out my glass cutter a little sparrow flew in through the skylight and landed on the floor. The alarm sounded and eight squad cars arrived. I got ten years. The sparrow got twenty to life. The bird was out in six months, on probation. A year later, he was picked up in Fort Worth for pecking Rabbi Morris Klugfein into a state of semi consciousness.

What advice would I give the average homeowner to protect himself against burglars? Well, the first thing is to keep a light on in the house when you go out. It must be at least a sixty-watt bulb; anything less and the burglar will ransack the house, out of contempt for the wattage. Another good idea is to keep a dog, but this is not foolproof. Whenever I was about to rob a house with a dog in it, I threw in some dog food mixed with Seconal. If that didn’t work, I’d grind up equal parts of chopped meat and a novel by Theodore Dreiser. If it happens that you are going out of town and must leave your house unguarded, it’s a good idea to put a cardboard silhouette of yourself in the window. A Bronx man once placed a cardboard silhouette of Montgomery Clift in his window and then went to Kutsher’s for the weekend. Later, Montgomery Clift himself happened to walk by and saw the silhouette, which caused him great anxiety. He attempted to strike up a conversation, and when it failed to answer for seven hours Clift returned to California and told his friends that New Yorkers were snobbish.

If you surprise an intruder in the act of burglarizing your home, do not panic. Remember, he is as frightened as you are. One good device is to rob him. Seize the initiative and relieve the burglar of his watch and wallet. Then he can get into your bed while you make a getaway. Trapped by this defense, I once wound up living in Des Moines for six years with another man’s wife and three children, and only left when I was fortunate enough to surprise another burglar, who took my place. The six years I lived with that family were very happy ones, and I often look back on them with affection, although there is also much to be said for working on a chain gang.
```

---

## IC-1338: Controlling Interest

- Title: Controlling Interest
- Author (byline): Wayne Rawley
- Work: Laugh Lines, Pgs 337-348
- Publisher: Vintage
- Publication date as stated: April 2007
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: JACK, BRAD, DAVID, STEVEN, ASHLEY, BETHANY
- Teaser before the introduction: No
- Spoken words (computed): 1238
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
(Raise right hand and left foot – solemnly) "Do you promise never to trade your bubble gum cards with a girl? Never lend your best fishing worms to a girl? And never let a girl carry your books home from school?"

Ever since Spanky, the President of the He-Man Woman-Hater’s Club in the 1980’s version of “Our Gang” attempted to swear in new recruits with this oath, little boys have been having a difficult time understanding and having relationships with little girls.

The saga continues with a modern-day boardroom negotiation in Controlling Interest by Wayne Rawley.
```

### Performance text (classify this)

```text
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

JACK: Hey now. We don't need that kind of insensitive talk around here, Steven. Please. Let's be kids about this. Besides, I think I will have the support of the membership here when I say, you're the [sissy].

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

## IC-1339: Conversations with my Father

- Title: Conversations with my Father
- Author (byline): Herb Gardner
- Work: Not specified
- Publisher: New Fireside Theatre
- Publication date as stated: 1993
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: EDDIE, JOEY
- Teaser before the introduction: Yes
- Spoken words (computed): 1105
- Already set (do not supply): none

### Source block (context only)

```text
Author: Herb Gardner
ISBN: 1568650701
Publisher: New Fireside Theatre
Date(Month/Year): 1993
```

### Introduction (context only: never use it for content warnings)

```text
Fighting never solved anything . . . . use your words, not your fists. . . . Mothers just don’t get it. Sometimes you have no choice but to fight. It’s a matter of pride. And defending your heritage. The year is 1936 and in this scene, Jewish born Eddie Goldberg has escaped to America and made a new life for his family in New York. Out of the frying pan and into the proverbial fire for 10 year old Joey, who is being harassed by another boy in the neighborhood. Fortunately, his father has a better answer to the dilemma than his mother.

Conversations with My Father by Herb Gardner.
```

### Performance text (classify this)

```text
EDDIE: A Russian Jew determined to make it in America, 20-30

JOEY: His 10-year-old son

JOEY: (Entering, thoughtfully, with stack of mail.) Pop, the sign outside, it says "Ross" on it . . .

EDDIE: That's our new name, you're gonna love it; honor o'Barney himself. (Takes mail, starts going through it.)

JOEY: You mean not just for the place, but actually our new name?

EDDIE: All done; legit and legal, kid. AI Gladstone presidin' (Takes envelope from mail.) Son of a bitch, The Sons of Moses, Pop's yahrzeit again. . .

JOEY: So my name is Joe Ross? That's my name now? Joe Ross? Very. . . brief, that name. . .

EDDIE: (Studying blue card from envelope.) Fifteen years, they find me every time, it's the Royal Mounted Rabbis. . .

JOEY: Joe Ross, it starts - it's over. . .

EDDIE: Hey, Hebrew School

JOEY: (Suddenly alarmed.) Jeez, went right outta my mind (Grabs Hebrew-texts, races for door, slapping yarmulkeh on his head.)

EDDIE: Wait a minute - (Points to yarmulkeh.) Where ya goin' with that on your head? What're ya, crazy? Ya gonna go eight blocks through Little Italy and Irishtown, passin' right through Goddamn Polack Street, with that on your head? How many times I gotta tell ya, kid - that is not an outdoor garment. That is an indoor garment only. Why don't ya wear a sign on your head says, "Please come kick the shit outa me?" You put it on in Hebrew School, where it belongs.

JOEY: Pop, I don't

EDDIE: I'm tellin' ya once more - stow the yammy, kid. Stow it.

JOEY: (Whips yarmulkeh off, shoves it in a pocket.) O.K., O.K. (Starts toward door.) I just don't see why I gotta be ashamed.

EDDIE: I'm not askin' ya to be ashamed. I'm askin' ya to be smart. (Sees something in the mail as Joey opens door; sharply) Hold it

JOEY: Gotta go, Pop

EDDIE: Hold it right it there

JOEY: Pop, this Tannenbaum, he's a killer

EDDIE: (Looking down at mail, solemnly) I got information here says you ain't seein' Tannenbaum this morning. I got information here says you ain't even headed for Hebrew School right now. (Silence for a moment. Joey remains in doorway) Cmere, we gotta talk.

JOEY: (Approaching cautiously, keeping at a safe distance.) Hey. . . no whackin', Pop. . .

EDDIE: I got this note here; says - (Takes small piece of cardboard from mail, reads.) "Dear Sheenie Bastard. Back of Carmine's, Remind you, Jewshit Joe, Eight o'clock A.M., Be there. Going to make Hamburger out of Goldberger - S.D." Bastard is spelled here B-A-S-T-I-D; this and the humorous remarks I figure the fine mind of the wop, DeSapio. (After a moment, looks up, slaps bar.) And I wanna tell ya good luck, glad you're goin', you're gonna nail 'im, you're gonna finish 'im, you're gonna murder 'im.

JOEY: Wait a minute - it's O.K.? Really?

EDDIE: - and here's a couple pointers how to do so.

JOEY: Pointers? Pointers? - I need a shot-gun, Pop; DeSapio's near twice my size, fourteen years old

EDDIE: Hey, far be it! Far be it from me to give pointers - a guy got twenty six bouts under his belt, twelve professional

JOEY: Yeah, but this DeSapio, he really hates me, this kid; he hated me the minute he saw me. He says we killed Christ, us Jews.

EDDIE: They was all Jews there, kid, everybody; Christ, His mother, His whole crowd - you tell him there was a buncha Romans there too, makes him directly related to the guys done the actual hit!

JOEY: I told him that Pop - that's when he whacked me.

EDDIE: And I bet you whacked him back, which is appropriate; no shit from nobody, ya stuck to your guns, kid

JOEY: So why're we hidin' then? How come we're "Ross" all of a sudden? (With an edge.) Or maybe Ross is just our outdoor name, and Goldberg's still our indoor name.

EDDIE: Hey

JOEY: I don't get it, this mean we're not Jewish anymore?

EDDIE: Of course we're still Jewish; we're just not gonna push it.

JOEY: (Checking watch.) Jeez - three minutes to eight, Pop, takes five to get there, he's gonna think I'm chicken - (Starts toward door.)

EDDIE: One minute for two pointers; let 'em wait, he'll get anxious

JOEY: He's not anxious, Pop, I promise ya

EDDIE: Now, these pointers is based on my observations o' your natural talents; the bounce,the eye, the smarts

JOEY: (Protesting.) Pop

EDDIE: C'mon, I seen you take out Itchy Halloran with one shot in fronta the Texaco Station; who're we kiddin' here? Hey, I was O.K., but you got potential I never had.

JOEY: But Itchy Halloran's my height, DeSapio's twice my size

EDDIE: (Ignoring him.) O.K., first blow; your instinct is go for the belly, right?

JOEY: Instinct? His belly is as high as I can reach, Pop

EDDIE: Wrong: first blow, forget the belly. Pointer Number One - ya listenin'?

JOEY: Yeah.

EDDIE: (Demonstrating, precisely.) Considerin' the size, you gotta rock this boy early. . . gotta take the first one up from the ground, vertical, so your full body-weight's in the shot. Now, start of the fight, right away, immediate, you hunk down, move outa range; then he's gotta come to you - and you meet him with a right fist up off the ground; picture a spot in the middle of his chin and aim for it - (Demonstrates blow, Joey copies.) then comes the important part

JOEY: What's that?

EDDIE: Jump back.

JOEY: Jump back?

EDDIE: Yeah, ya jump back so when he falls he don't hurt ya.

JOEY: When he falls? Murder, he's gonna murder me. Pop, Pop, this is an execution I'm goin' to here! I'm only goin' so I won't be ashamed!

EDDIE: There's only one thing you gotta watch out for

JOEY: Death, I gotta watch out for death

EDDIE: Not death. . . but there could be some damage. Could turn out to be more than one guy there, you're gettin' ganged up on, somethin' special- this happens, kid - O.K., we got a weapon here - (Takes framed photo of boxer from wall.) we got a weapon here, guaranteed. (Hands photo to Joey.) What's it say there?

JOEY: (Reading.) "Anybody gives you trouble, give me trouble. I love you. Love, Vince."

EDDIE: O.K.; June Four, Nineteen Twenty-one, I come into the ring against Vince DiGangi, they bill him "The Ghetto Gorilla," - a shrimp with a moustache, nothin', I figure an easy win. Five seconds into Round One comes a chamalia from this little Eye-tie - I'm out, I'm on the canvas, your Pop is furniture, Joey. I open one eye, there's DiGangi on his knees next to me, he's got me in his arms, he's huggin' me, he's kissin' my face, he loves me. I give him his first big win, his first knockout. I made him, he says, he's gonna love me forever. And he does. That's the nice thing about these Telanas, they love ya or they hate ya, but it's forever; so, remember - (Leans towards him.) things get outa hand, you got a group situation, somethin' you holler "DiGangi e mio fratello, chiamalo!" (Grips his shoulder.) "DiGangi e mio fratello, chiamalo!" Say it.

JOEY: "DiGangi e mio fratello, chi. . . amalo!"

EDDIE: That's: "DiGangi's my brother, call him!" (Softly, awestruck, imitating their response.) Whoa. . . "DiGangi" 's the magic word down there, biggest hit since Columbus, lotta power with the mob. Perhaps you noticed, Big Vito don't come around here pushin' protection, whatever. This is the result of one word from Mr. Vincent DiGangi. (Pats Joey's hand.) Very heavy ticket there, kid, you don't want to use it unless the straits is completely dire. (Slaps bar.) O.K., ya got all that?

JOEY: (Starting towards front door without much spirit.) Yeah. (As he passes stroller; softly, sighing.) Well. . . here I go.
```

---

## IC-1340: Count Dracula

- Title: Count Dracula
- Author (byline): Woody Allen
- Work: The Complete Prose of Woody Allen (Pg 238-244)
- Publisher: Wings Books
- Publication date as stated: March 1991
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, BAKER’S WIFE, BAKER, DRACULA, MAYOR, KATIA
- Teaser before the introduction: Yes
- Spoken words (computed): 990
- Already set (do not supply): none

### Source block (context only)

```text
Author: Woody Allen
Book: The Complete Prose of Woody Allen (Pg 238-244)
ISBN: 978-0517072295
Publisher: Wings Books
Date (Month/Year): March 1991
```

### Introduction (context only: never use it for content warnings)

```text
Now and then, everybody has a bad day. I bet even Mother Theresa felt cross sometimes. It happens to everyone.

You know you’re having a bad day when . . .

• You call your wife and tell her that you would like to eat out tonight and when you get home there is a sandwich on the front porch. • Your 4-year-old tells you that it's almost impossible to flush a grapefruit down the toilet. • Today’s the day of the total eclipse, and no one reminded you . . . What’s wrong with that you ask? Nothing unless you are

Count Dracula by Woody Allen
```

### Performance text (classify this)

```text
NARRATOR: (Pg 238-244) Somewhere in Transylvania, Dracula the monster is sleeping in his coffin, waiting for night to fall. As exposure to the sun’s rays would surely cause him to perish, he stays protected in the satin-lined chamber bearing his family name in silver. Then the moment of darkness comes, and through some miraculous instinct the fiend emerges from the safety of his hiding place and, assuming the hideous forms of the bat or the wolf, he prowls the countryside, drinking the blood of his victims. Finally, before the first rays of his archenemy, the sun, announce a new day, he hurries back to the safety of his hidden coffin and sleeps, as the cycle begins anew.

NARRATOR: (simultaneously pantomime the narration as Dracula) Now he starts to stir. The fluttering of his eyelids are a response to some age-old, unexplainable instinct that the sun is nearly down and his time is near. Tonight, he is particularly hungry as he lies there, fully awake now, in red-lined Inverness cape and tails, waiting to feel with uncanny perception the precise moment of darkness before opening the lid and emerging, he decides who this evening’s victims will be. The baker and his wife, he thinks to himself. Succulent, available, and unsuspecting. The thought of the unwary couple whose trust he has carefully cultivated excites his blood lust to a fever pitch, and he can barely hold back these last seconds before climbing out of the coffin to seek his prey.

Suddenly he knows the sun is down. Like an angel of hell, he rises swiftly, and changing into a bat, flies pell-mell to the cottage of his tantalizing victims.

BAKER’S WIFE: (opening the door) Why, Count Dracula, what a nice surprise.

NARRATOR: He has once again assumed human form, charmingly concealing his rapacious goal.

BAKER: What brings you here so early?

DRACULA: Our dinner date. I hope I haven’t made an error. You did invite for tonight, didn’t you?

BAKER: Yes, tonight, but that’s not for seven hours.

DRACULA: (looking around the room puzzled) Pardon me?

BAKER: Or did you come to watch the eclipse with us?

DRACULA: Eclipse?

BAKER: Yes. Today’s the total eclipse.

DRACULA: What?

BAKER: A few moments of darkness from noon until two minutes after. Look out the window.

DRACULA: (with rising panic that he tries to mask) Uh-oh. I’m in big trouble.

BAKER: Eh?

DRACULA: And now if you’ll excuse me . . .

BAKER: What, Count Dracula?

DRACULA: (Frantically fumbling for the doorknob) Must be going-aha-oh god . . .

BAKER: Going? You just came.

DRACULA: Yes-but-I think I blew it very badly . . .

BAKER: Count Dracula, you’re pale.

DRACULA: Am I? I need a little fresh air. It was nice seeing you . .

BAKER: Come. Sit down. We’ll have a drink.

DRACULA: Drink? No, I must run. Er-you’re stepping on my cape.

BAKER: Sure. Relax. Some wine.

DRACULA: Wine? Oh no, gave it up-liver and all that, you know. And now I really must buzz off. I just remembered, I left the lights on in the castle -- bills’ll be enormous. . .

BAKER: (putting his arm around the Count in friendship) You’re not intruding. Don’t be so polite. So you’re early.

DRACULA: Really, I’d like to stay but there’s a meeting of old Romanian counts across town and I’m responsible for the cold cuts.

BAKER: Rush, rush, rush. It’s a wonder you don’t get a heart attack.

DRACULA: Yes, right-and now-

BAKER’S WIFE: I’m making chicken pilaf tonight. I hope you like it.

DRACULA: (smiling and pushing her aside) Wonderful, wonderful. (opens a closet door by mistake and walks in) Christ. Where’s the front door?

BAKER’S WIFE: (laughing) Ach, such a funny man, the count.

DRACULA: (forcing a chuckle) I knew you’d like that. Now get out of my way. (opens the front door and panics at the sunlight)

BAKER: Oh, look, the eclipse must be over. The sun is coming out again.

DRACULA: (slamming the front door) Right. I’ve decided to stay. Pull down the window shades quickly-quickly! Let’s move it!

BAKER: What window shades?

DRACULA: There are none, right? Figures. You got a basement?

BAKER’S WIFE: (affably) No, I’m always telling Jarslov to build one but he never listens. That’s some husband, my Jarslov.

DRACULA: I’m all choked up. Where’s the closet?

BAKER: You did that one already, Count Dracula. Unt mama and I laughed at it.

BAKER’S WIFE: Ach-such a funny man, the Count.

DRACULA: Look, I’ll be in the closet. Knock at seven-thirty. (he steps in the closet and slams the door)

BAKER’S WIFE: Hee-hee--he is so funny, Jarslov.

BAKER: Oh, count. Come out of the closet. Stop being a big silly.

DRACULA: (from inside the closet comes the muffled voice of Dracula) Can’t. Please. Take my word for it. Just let me stay here. I’m fine. Really.

BAKER: Count Dracula, stop the fooling. We’re already helpless with laughter.

DRACULA: Can I tell you, I love this closet.

BAKER: Yes, but . . .

DRACULA: I know, I know . . . It seems strange, and yet here I am, having a ball. I was just saying to Mrs. Hess the other day, give me a good closet and I can stand in it for hours. Sweet woman, Mrs. Hess. Fat, but sweet . . . Now, why don’t you run along and check back with me at sunset.

NARRATOR: Now the mayor and his wife, Katia, arrive. They are passing by and have decided to pay a call on their good friends, the baker and his wife.

MAYOR: Hello, Jarslov. I hope Katia and I are not intruding?

BAKER: Of course not, Mr. Mayor. Come out, Count Dracula. We have company!

MAYOR: (surprised) Is the count here?

BAKER’S WIFE: Yes, and you’ll never guess where.

MAYOR: It’s so rare to see him around this early. In fact, I can’t ever remember seeing him around in the daytime.

BAKER’S WIFE: Well, he’s here. Come out, Count Dracula!

KATIA: Where is he?

BAKER’S WIFE: (impatiently) Come on out now! Let’s go!

BAKER: (apologetically) He’s in the closet. (knocking on the door) Let’s go. Enough is enough. The mayor’s here.

MAYOR: Come on out, Dracula. Let’s have a drink.

DRACULA: No, go ahead. I have business in here.

MAYOR: In the closet?

DRACULA: Yes, don’t let me spoil your day. I can hear what you’re saying. I’ll join in if I have anything to add.

NARRATOR: Everyone looks at one another and shrugs. Wine is poured and they all drink.

MAYOR: Some eclipse today.

BAKER: Yes. Incredible.

DRACULA: Yeah. Thrilling.

BAKER: What, Dracula?

DRACULA: Nothing, nothing. Let it go.

NARRATOR: And so some time passes, until the mayor can stand it no longer.

MAYOR: (forcing open the door to the closet, he shouts) Come on, Dracula. I always thought you were a mature man. Stop this craziness.

NARRATOR: The daylight streams in, causing the evil monster to shriek and slowly dissolve to a skeleton and then to dust before the eyes of the people present.

MAYOR: (Leaning down to the pile of white ash on the closet floor) Does this mean dinner is cancelled?
```

---

## IC-1341: Cubs

- Title: Cubs
- Author (byline): Patrick F. McManus
- Work: The Good Samaritan Strikes Again, Pgs 61-74
- Publisher: MacMillan
- Publication date as stated: Aug 1993
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: PATRICK, MR. TIDDLE, SCOUTS, ATTILA, PORKY, DANNY, TONY, LUCIFER, PEEWEE, GROVER, MRS. SLOCUM
- Teaser before the introduction: Yes
- Spoken words (computed): 1866
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patrick F. McManus
Book: The Good Samaritan Strikes Again, Pgs 61-74
ISBN: 978-0805029222
Publisher: MacMillan
Date (Month/Year): Aug 1993
```

### Introduction (context only: never use it for content warnings)

```text
Scouting has come a long way over the years. Today, the Boy Scouts has made strides to become more inclusive. Cub Scouts is, and I quote, “a program for children (both boys and girls) in kindergarten through fifth grade and their families that encourages learning, friendship—and most of all—getting out and having fun!”

But when Patrick McManus was a cub scout, it was boys ONLY and they used the word FUN too! Those were the days when FUN may have been more loosely defined. But seriously: a 5- mile hike with a backpack that weighed more than you and skinny-dipping in a frozen lake does not fit the FUN definition!

Cubs by Patrick F. McManus
```

### Performance text (classify this)

```text
PATRICK: (Pg 61-74) I like to think I was just as good a Cub Scout as the next guy, the next guy being Grover Finch, who was about as miserable a Cub Scout as ever tied a granny knot and called it square. Our den could boast of boys clearly cut out for the scouting life, but I wasn’t one of them. Neither was Grover. He dropped out of Cubs shortly after the strange incident at Camp Muskrat. I think he may have received a dishonorable discharge, but I don’t know for sure.

PATRICK: One day in early spring, the scoutmaster of the local troop showed up at our [cub scout] meeting. Mr. Tiddle was a robust outdoorsman, shaped something like a barrel, but all bone and muscle. He lifted weights and did calisthenics just for the fun of it, but the strangest thing was that every New Year’s Day he would chop a big hole in the ice and plunge into the frigid water of Lake Blight.

MR. TIDDLE: (booming) Boys, I’ve got great news for you. A couple of the scouts from Troop Nine-oh-seven and I are going to take you Cubs on an overnight outing to Camp Muskrat this Saturday. How does that sound?”

PATRICK: We broke into cheers, with Grover cheering the loudest of all.

MR. TIDDLE: You all show up at the school at eight o’clock Saturday, and we’ll issue you sleeping bags and packs. For supper, we’ll treat you to a wiener roast.

SCOUTS: Yayyyyyyyy!

PATRICK: The next Saturday morning, about fifteen of us Cubs assembled at the grade school. Several station wagons were parked nearby. We assumed they were there to transport us to Camp Muskrat, located on a small lake five miles from town. Then we noticed that volunteered fathers were loading the station wagons with tents and other gear and supplies. We watched as the station wagons departed one by one, until none were left for us. Mr. Tiddle and two Boy Scouts, all three in their starched tan uniforms, strode briskly over to us.

MR. TIDDLE: (bellowing enthusiastically) Listen up, Cubs! We have a real treat for you. Scouts Lucifer and Attila have volunteered to serve as your leaders on the campout, and they have come up with a marvelous idea. Instead of riding to Camp Muskrat, you get to practice your hiking skills all the way out to the camp. Let’s have a big hand for these fine scouts.

PATRICK: (less than enthusiastic clapping) We stared up at the towering scouts, both of whom smiled benevolently down on us.

MR. TIDDLE: I leave you in their care. See you all at Camp Muskrat.

PATRICK: He got into his car and drove away. The two scouts watched his car until it disappeared around a corner. When they turned back to us, we were shocked. They had gown fangs and claws and their eyes glowed red with fiery light! We could tell from their gleefully evil expressions this was an opportunity they had waited for all their lives.

ATTILA: (mean and threatening) Hoist your packs and line up according to height, shrimps! No talking! Move it! Move it!

PATRICK: Startled, we hoisted our packs and scrambled into a ragged line.

PORKY: Hey, I just remembered. I’m supposed to go to the dentist today! See you guys later.

DANNY: I have to go to the bathroom. Be right back.

TONY: Me too. Be gone just a second.

LUCIFER: (snarling) Shut up, shrimps! Back in formation!

PATRICK: The would-be deserters shrank back into line.

LUCIFER: (screaming) Left face!

ATTILA: (bellowing) Forwarrrrrd! March! Hut two three four, hut . . .

PATRICK: Attila brought up the rear, apparently for the purpose of harrying the stragglers and shooting the wounded.

PEEWEE: (croaking) How much farther is it?

LUCIFER: (shouting) Four miles to go! Now close up that line! Hut two three four . . .

PATRICK: The hot spots of blisters began to glow inside our tennis shoes. Pack straps gnawed at our shoulders.

GROVER: (muttering) This ain’t a hike. It’s a death march

PATRICK: (to Grover) Somebody is going to pay for this. (to audience) Hours later we limped into Camp Muskrat and dropped to the frozen, snow-blotched ground. The fathers had set up the tents and then vanished with the blinding speed common to fathers volunteered for Cub Scout outings. Mr. Tiddle and the two scouts were now left alone with fifteen exhausted but surly Cubs, who sprawled in ominous silence, sullenly watching Attila, Lucifer, and Mr. Tiddle job about gathering wood for the evening campfire. The scouts and scoutmaster joked and laughed as if they hadn’t a care in the world. The air, however, was heavy with suspense, dark with foreboding. I crawled over to the remains of Grover and Peewee. (to Grover) Come up with anything for Lucifer and Attila yet?

GROVER: I’m thinking, I’m thinking. Everything I come up with is either too kind or too complicated. We need something simple but mean. I suppose we could steal their clothes so they would have to run around naked in the cold and maybe catch pneumonia and suffer horribly for a long time and then die terrible agonizing deaths.

PATRICK: The sun sank behind Muskrat Mountain, and a breeze wafted in off Muskrat Lake, chilled by rafts of sludgy ice still drifting about the surface. We put on sweaters and even coats and gathered around the fire that Lucifer and Attila had built into a small inferno. This was more like it.

PEEWEE: Are we camping yet?

PATRICK: Suddenly, Mr. Tiddle erupted from his tent with a towel thrown over his shoulder.

MR. TIDDLE: Any of you Cubs like to join me for a dip in the lake? What, no takers? (to Lucifer and Attila) How about you scouts? Like to refresh yourselves with a dip before supper? There’s a nice sandy beach down the shore a ways, and we don’t even have to chop through the ice. Just shove it out of the way.”

ATTILA: (shuddering) Why, we’d sure like to Mr. Tiddle. Sounds wonderful. But darn it all, we didn’t bring our bathing trunks.

MR. TIDDLE: (bellowing) Me neither. Ever hear of skinny-dipping? C’mon, lads. Race you out to the floating dock!

LUCIFER: (whining) Wow, okay then, Mr. Tiddle. Attila and I’ll be right there, as soon as we grab some towels. Hope we can find you in the dark.

PATRICK: The two scouts slouched off. We Cubs edged closer to the toasty campfire.

GROVER: This is too good to be true. Be back in a bit.

PATRICK: And [he] slipped off into the shadows. Scarcely had Grover vanished when the plot thickened. The headlights of a car illuminated the Camp Muskrat parking area for a moment, and soon Mrs. Slocum (our den mother) and another lady came picking their way down a trail to the campfire.

MRS. SLOCUM: Good evening, Cubs! You look like you’re having a wonderful time. I’m so glad! I think you all know my good friend Mrs. Teasdale. We thought we would join you for the wiener roast. Brought you a treat – marshmallows!

SCOUTS: Yayyyyyyy!

PATRICK: We pulled up a log for the ladies to sit on next to the fire. Just then Grover emerged from the woods, slapping his way through a cloud of mosquitoes.

GROVER: (whispering to Patrick) Snatched only one set of clothes and a towel. Was all I could find in the dark. I could hear them splashing around not too far from shore and thought they might spot me. Slipped the clothes into their tent. But either Lucifer or Attila is going to be in for a big surprise!

PATRICK: We sat around the fire telling ghost stories, but nothing compared to the horror that awaited us. Sooner than expected, Lucifer came rushing into the light of the fire.

LUCIFER: Wow, you guys are smarter than you look. That water is liquid ice. Just lucky I had the good sense to test it with my toe first– why, hello there, Mrs. Slocum, Mrs. Teasdale. Didn’t know you were coming for a visit.

GROVER: (whispering to Patrick and snickering) Attila’s the one. This could be good.

PATRICK: A minute later, Attila bounded into camp – fully clothed!

ATTILA: Wheweeee, that water’s cold! Chickening out is the better part of valor, I always say. I don’t know how Mr. Tiddle can stand it.

PATRICK: Grover stared grimly at Lucifer and Attila. Minutes dragged by. We sang a camp song. Mrs. Slocum and Mrs. Teasdale told about when they were little girls and had picked huckleberries in the hills above Camp Muskrat. And then . . . The monster roared out of the darkness so suddenly that several Cubs almost inhaled flaming marshmallows. For a moment I thought it was a Sasquatch, but it turned out to be Mr. Tiddle. He was stark naked, except for a little cedar bough he had twisted off a tree.

MR. TIDDLE: (booming) So, the old steal-the-clothes trick!

GROVER: (whispering to Patrick) I thought this might happen. You can have my bike and baseball glove if you want them.

PATRICK: (to Grover) Thanks, Grover. Hey, it’s been fun knowing you. (to audience) Then a surprising thing happened. Mr. Tiddle grabbed Lucifer and Attila by the hair, one with each hand.

MR. TIDDLE: Ha! Just as I suspected – hair’s not even wet! Well, I’ll just have to see what I can do about that.

ATTILA: Wait! LUCIFER: It wasn’t . . !

MR. TIDDLE: Oh, it wasn’t, was it? Well, we’ll just check your tent and see if we don’t find my clothes there.

PATRICK: Mr. Tiddle dragged the two scouts over to check their tent.

LUCIFER: See, your clothes aren’t . . . . NOOOOOOOO!

MR. TIDDLE: Aha! You two scalawags thought you could pull a fast one on me, did you?

PATRICK: He snatched up each of the scouts by the back of the belt and charged off toward the lake, one in each meaty hand. The screams were among the best and most satisfying I’ve ever heard, starting low and quavering but then rising in pitch and volume while still conveying great feeling and intensity right up to the moment of total immersion. We Cubs all agreed the performance was highly entertaining, spiritually enriching, and well worth a forced march. Recovering his little cedar branch, Mr. Tiddle strolled back to the fire chortling.

MR. TIDDLE: Please excuse my nudity for a minute, boys. I just wanted to make a point about practical jokes – oh, nice to see you, Mrs. Slocum, Mrs. Teasdale. Didn’t expect you ladies out this evening. The point I was making to the Cubs here is that people can play their little pranks, but in the end they have to pay the pipe – Ladies?

PATRICK: His lips froze in a grotesque smile over his big white teeth. He hunched over and tried to conceal himself behind the little bough. I sure would have felt embarrassed if I’d been standing there naked except for a little cedar bough and suddenly realized two ladies were sitting not ten feet away.

PEEWEE: Yeah. Then, as if that wasn’t bad enough, dumb ol’ Terry accidentally flicks his flaming marshmallow onto the cedar bough. That ol’ bough must have been dry as gunpowder, to flare up like that. Poor Mr. Tiddle,

PATRICK: I think both Mrs. Slocum and Mrs. Teasdale handled it pretty well. It was nice how they pretended not to notice Mr. Tiddle because of concentrating so hard on twirling their sticks over the coals, just as if roasting wieners was the most important thing in the world to them.

PEEWEE: It would have been better if they hadn’t let their wieners burn off and fall in the fire, though. They didn’t even seem to notice. Just sat there twirling them empty sticks round and round, an all the while Mr. Tiddle’s roaring and darting about like a madman.

PATRICK: Well, I guess that’s camping!
```

---

## IC-1342: The Cult

- Title: The Cult
- Author (byline): Jon Stewart
- Work: Naked Pictures of Famous People, Pg 81-92
- Publisher: Harper Collins
- Publication date as stated: Oct 1999
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ME, LT JOHNSON, LT MCSHANE, LIEUTENANT JOHNSON, OTHER ROOM, FOLLOWER #1, FOLLOWER #3, FOLLOWER #4, FOLLOWER #2
- Teaser before the introduction: Yes
- Spoken words (computed): 1287
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jon Stewart
Book: Naked Pictures of Famous People, Pg 81-92
ISBN: 978-0688171629
Publisher: Harper Collins
Date (Month/Year): Oct 1999
```

### Introduction (context only: never use it for content warnings)

```text
The Cult by Jon Stewart
```

### Performance text (classify this)

```text
ME: (PG 81-92) (to audience) Considering the many feats of leadership in the twentieth century, from Churchill's morale-rallying speeches in World War II to Martin Luther King Jr.'s marches for racial equality during the sixties, the ones that I find most impressive are the Jonestown Massacre and Heaven's Gate. While Churchill and King inspired loyalty and devotion, they had the benefit of real issues and problems to play on. Getting people to buckle down during World War II or walk a couple of blocks with you on a sunny day in Alabama are impressive indeed, but getting people to kill themselves for no reason other than you think you saw something about it in a dream? (makes an impressed and wonder-filled “humph”)

Me . . . persuasive leader of a messianic cult? Would I have the strength? Would I be able to overcome my fear of death, zealous crowds and death by zealous crowds? Would I understand the intricacies of forming a tax-exempt organization?

ME: (to audience) We begin in the back room of my cult's compound – also known as my rent-controlled one-bedroom. My subjects have congregated on this day to witness our salvation. I have foretold a vision of the Rapture. At 4:00 P.M., Captain Crunch will spring to life from his resting place on the back of a cereal box and deliver us to our eternal bliss. It is 3:56 P.M.

LT JOHNSON: Leader . . . What a glorious day for our deliverance!

ME: (distracted by the time) Yes, yes. The day is glorious, although they say tomorrow's pollen count will be moderate to heavy.

LT JOHNSON: What care we of tomorrow, when salvation is but four minutes away.

ME: I'm just saying I would hate to go to our salvation with red itching eyes.

LT MCSHANE: But the Captain will deliver us from our earthly afflictions. You said!

LT JOHNSON: He knows what he said. Why must you always nag? He knows we --

ME: Fellas, please. With the air conditioning out, the last thing I need is the two of you making a ruckus.

LIEUTENANT JOHNSON: Tell us again, for the last time, the story of Captain.

ME: All right. But then you both have to finish unloading the dishwasher like I asked you yesterday.

LT JOHNSON: We're sorry, Leader. We just thought that with the Captain coming . . .

LT MCSHANE: We would have no more use for earthly dishes.

ME: So you want the Captain to eat off dirty dishes. Our savior of saviors, and you can't take the time?

LT MCSHANE: Were sorry, Leader. Please forgive our sinful ways. (They begin to kiss his feet)

ME: All right, fine . . . get up. C'mon. You're embarrassing me, you . . . (they get up) Anyhoo. (preaching) The Captain was an all-powerful, benevolent leader. His people lived in a state of constant bliss, with a little sugar rush thrown in for good measure. One day, while his followers were being sinful and lazy and arguing with each other, a mean leprechaun accused the Captain of stealing his Lucky Charms. The leprechaun put a spell on the Captain, confining him until the righteous among us could pull the sword from the rock, showing the Captain we were worthy of receiving his good graces.

LT JOHNSON: Leader? I have a question. If the Captain is all-powerful . . . How could the leprechaun put a spell on him?

LT MCSHANE: And what of the sword? I mean, I don't want to nitpick, but you never mentioned the sword before.

ME: You're gonna do this now? Huh? Three . . . two minutes to salvation and you're gonna do this now? Maybe you guys should have thought of this before you signed up, because if you're gonna nitpick, I got a living room filled with believers that would love to be lieutenants. Remember, at Salvation, the lieutenants get to carry the Captain's hat.

LT MCSHANE: No, Leader. Please don't be angry. It's just . . . I had never heard that thing about the sword before.

ME: Well, I just remembered it. Besides, you had no trouble swallowing the cereal box come to life part.

LT MCSHANE: That's true.

LT JOHNSON: And when the Captain comes he will relieve our earthly afflictions?

ME: Bingo.

LT JOHNSON: This cursed cleft chin will finally be gone.

ME: I keep telling you. That's considered a positive feature.

LT MCSHANE: And what of my leprosy?

ME: Your what? I thought that was dermatitis.

LT MCSHANE: (Showing his arms) This is dermatitis. (Lifting up his shirt) This is leprosy.

ME: Oh, my God (furiously rubbing his exposed skin). I hugged you in the Circle of Knowledge yesterday! Please get off the chair, nothing personal. I just had them redone and it cost a fortune . . . and I'll take the drinking glass, please . . . thank you.

OTHER ROOM: (From the other room a group chant begins.) CAPTAIN, WE ARE READY. 10 – 9 – 8. . .

ME: My watch still says 3:58. Imitation Rolex. (bangs watch on the table and puts it to his ear)

LT JOHNSON: Come, Leader, let us join the others so the Captain will see our solidarity.

ME: You guys go. I still have that . . . thing . . . in the oven. Wouldn't want the Captain's chicken to get dry.

LT MCSHANE: All right. See you in Nirvana. (They exit)

OTHER ROOM: (The chant goes on) 3 – 2 – 1 . . . (Then all is silent. The silence endures ... and then the Lieutenants re-enter the room)

LT JOHNSON: Uhh, Leader . . . can we have a word with you, please?

ME: Huh. Oh! Hey, how's the Captain?

LT MCSHANE: Everyone would like a word with you in the front . . . now.

ME: Sure, sure. (he is dragged into the front room) Hey, everybody! What can I do you for?

FOLLOWER #1: It is 4:02. And still the Captain remains on the box. Smirking at us.

ME: 4:02. Right. (frantically thinking of an explanation) Right . . . Oh my God. It's Daylight Saving Time, isn't it? In the Land of Plenty it's still 3:02. Silly mistake. I can't believe I --

FOLLOWER #1: You lied to us, Leader. You took advantage of us.

ME: Now let's not start hurling accusations. I mean, who among us can really cast the first stone? Lying, taking advantage. Those are serious allega . . . (A clamor arises from the followers) All right now, settle down, people. Remember, I'm still the one making up the seating chart for the rocket ship (They quiet) Heh, heh. Well. (beat) Are we out of onion dip? Let me run out and grab some quick, because the Captain's going to be here in about (checking watch) fifty-five minutes and you know he'll be hungry and . . . (They surround him ominously) Hey, c'mon. Why the long faces? The Captain's a little late. Christ. The guy's been on a box for . . .

FOLLOWER #3: You took all I had in the world. You destroyed my family. All I did was ask you for directions and before I knew what hit me, you had ruined me with your lies of a promised land of Crunchberries and honey . . .

FOLLOWER #4: Get him!! (General mayhem ensues. Lamps break, feelings are hurt.)

ME: People, please! Settle down! Now listen. I know you're disappointed that the Captain didn't show us the way to eternal salvation, but we still have cable till the end of the month, so let's show a little restraint here.

LT JOHNSON: Perhaps the Captain knew there were skeptics among us. Perhaps this is why he has forsaken us.

ME: Boom! Exactly. Couldn't have put it better myself. Damn skeptics. Maybe if you people hadn't balked at the bathroom tax none of this would . . .

LT MCSHANE: A suicide pact will convince the Captain of our sincerity. A suicide pact led by our leader. The Leader will die and we shall follow!

ME: Whoa. Whoa. Slow down there, chief. I mean, suicide . . . we could get in a lot of trouble for that.

LT JOHNSON: Suicide is the only Way!

ME: You never heard of a letter-writing campaign? Stop. This is madness! (The crowd hushes at his fervor)

FOLLOWER #1: You're stalling.

FOLLOWER #2: You're a staller and a liar.

ME: Look. You're all really mad at me, but . . . You wanted this. You needed this. It was your weakness that made this all possible. You didn't want to take responsibility for your own lives. You had to look to a savior to make it all better for you. I didn't do this to you, you did it to yourselves. You wanted to believe in an easy solution to the complex stresses and anxieties of your lives. I saved you from yourselves. (All is quiet in the room, then a warlike shriek goes up and the mob attacks)

Wait! Stop! Ow! Don't pull, it's not a toupee! . . . (suddenly pointing to the cereal box) Oh my God! It's THE CAPTAIN! (The room goes silent as all eyes shift to the cereal box – a long beat; then he speaks with conviction) See? Do you see! The Captain hasn't moved, but for that one brief moment, we all believed again. We all believed in the possibility of our salvation. (Heads nodding, the believers are contemplating – He begins to back away toward the exit) Remember those days. The believing days. Those were good times. . . (He runs out with the crowd in hot pursuit)
```

---

## IC-1343: Cyclops

- Title: Cyclops
- Author (byline): David Sedaris
- Work: Naked
- Publisher: Little Brown and Company
- Publication date as stated: March 1997
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2105
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Sedaris
Book: Naked
ISBN: 03I6779490
Publisher: Little Brown and Company
Date(Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
This is going to hurt me more than it hurts you. Just tell me the truth and you won't get in trouble. When I was your age I walked 10 miles to school, up hill both ways, in the snow. I am sure most of us grew up thinking some of the things that our parents said were actually true. In reality, many were white lies that they told us to trick us into doing or believing something or better yet, to stop us from doing something! David Sedaris’ father was no different . . . . . but the parental phrase “You’ll put your eye out!” became a much more involved story entitled Cyclops by David Sedaris.
```

### Performance text (classify this)

```text
When he was young my father shot out his best friend's eye with a BB gun. That is what he told us. "One foolish moment and, Jesus, if I could take it back, I would." He winced, shaking his fist as if it held a rattle. "It eats me alive," he said. "I mean to tell you that it absolutely tears me apart."

On one of our summer visits to his hometown, my father took us to meet this guy; a shoe salesman whose milky pupil hugged the corner of his mangled socket. I watched the two men shake hands and turned away, sickened and ashamed by what my father had done.

Our next-door neighbor received a BB gun for his twelfth birthday and accepted it as a personal challenge to stalk and maim any living creature: sunbathing cats, sparrows, slugs, and squirrels - if it moved, he shot it. I thought this was an excellent idea, but every time I raised the gun to my shoulder, I saw my father's half-blind friend stumbling forth with an armload of Capezios. What would it be like to live with that sort of guilt? How could my father look himself in the mirror without throwing up?

While watching television one afternoon my sister Tiffany stabbed me in the eye with a freshly sharpened pencil. The blood was copious, and I rode to the hospital knowing that if I was blinded, my sister would be my slave for the rest of her life. Never for one moment would I let her forget what she'd done to me. There would be no swinging cocktail parties in her future, no poolside barbeques or episodes of carefree laughter, not one moment of joy - I would make sure of that. I'd planned my vengeance so thoroughly that I was almost disappointed when the doctor announced that this was nothing but a minor puncture wound, located not on but beneath the eye.

"Take a look at your brother's face," my father said, pointing to my Band- Aid. "You could have blinded him for life! Your own brother, a Cyclops, is that what you want?" Tiffany's suffering eased my pain for an hour or two, but then I began to feel sorry for her. "Every time you reach for a pencil, I want you to think about what you've done to your brother," my father said. "I want you to get on your knees and beg him to forgive you."

There are only so many times a person can apologize before it becomes annoying. I lost interest long before the bandage was removed, but not my father. By the time he was finished, Tiffany couldn't lift a dull crayon without breaking into tears. Her pretty, suntanned face assumed the characteristics of a wrinkled, grease-stained bag. Six years old and the girl was broken.

Danger was everywhere and it was our father's lifelong duty to warn us. Attending the country club's Fourth of July celebration, we were told how one of his Navy buddies had been disfigured for life when a cherry bomb exploded in his lap. "Blew his balls right off the map," he said. "Take a second and imagine what that must have felt like!" Racing to the farthest edge of the golf course, I watched the remainder of the display with my hands between my legs.

Fireworks were hazardous, but thunderstorms were even worse. "I had a friend, used to be a very bright, good-looking guy. He was on top of the world until the day he got struck by lightning. It caught him right between the eyes while he was trout fishing and cooked his brain just like you'd roast a chicken. Now he's got a metal plate in his forehead and can't even chew his own food; everything has to be put in a blender and taken through a straw."

If the lightning was going to get me, it would have to penetrate walls. At the first hint of a storm I ran to the basement, crouching beneath a table and covering my head with a blanket. Those who watched from their front porches were fools. "The lightning can be attracted by a wedding ring or even the fillings in your teeth," my father said. "The moment you let down your guard is guaranteed to be the day it strikes."

In junior high I signed up for shop class, and our first assignment was to build a napkin holder. "You're not going to be using a table saw, are you?" my father asked. "I knew a guy; a kid about your size, who was using a table saw when the blade came loose, flew out of the machine, and sliced his face right in half." Using his index finger, my father drew an imaginary line from his forehead to his chin. "The guy survived, but nobody wanted anything to do with him. He turned into an alcoholic and wound up marrying a Chinese woman he'd ordered through a catalog. Think about it." I did.

My napkin holder was made from found boards and, once finished, weighed in at close to seven pounds. My bookshelves were even worse. "The problem with a hammer," I was told, "is that the head can fly off at any moment and, boy, let me tell you, you've never imagined pain like that."

After a while we began to wonder if my father had any friends who could still tie their own shoes or breathe without the aid of a respirator. With the exception of the shoe salesman, we'd never seen any of these people, only heard about them whenever one of us attempted to deep-fry chicken or operate the garbage disposal. "I've got a friend who buys a set of gloves and throws one of them away. He lost his right hand doing the exact same thing you're doing. He had his arm down the drain when the cat rubbed against the switch to the garbage disposal. Now he's wearing clip-on ties and having the restaurant waiters cut up his steak. Is that the kind of life you want for yourself?"

He allowed me to mow the lawn only because he was too cheap to pay a landscaper and didn't want to do it himself. "What happened," he said, "is that the guy slipped, probably on a pile of crap, and his leg got caught up in the blade. He found his foot, carried it to the hospital, but it was too late to sew it back on. Can you imagine that? The guy drove fifteen, twenty miles with his foot in his lap."

Regardless of the heat, I mowed the lawn wearing long pants, knee-high boots, a football helmet, and a pair of goggles. Before starting, I scouted the lawn for rocks and dog feces, slowly combing the area as if it were mined. Even then I pushed the mower haltingly, always fearing that this next step might be my last. Nothing bad ever happened, and within a few years I was mowing in shorts and sneakers, thinking of the supposed friend my father had used to illustrate his warning. I imagined this man jumping into his car and pressing on the accelerator with his bloody stump, a warm foot settled in his lap like a sleeping puppy. Why hadn't he just called an ambulance to come pick him up? How, in his shock, had he thought to search the weeds for his missing foot? It didn't add up.

I waited until my junior year of high school to sign up for driver's education. Before taking to the road, we sat in the darkened classroom, watching films that might have been written and directed by my father. Don't do it, I thought, watching the prom couple attempt to pass a lumbering dump truck. Every excursion ended with the young driver wrapped around a telephone pole or burned beyond recognition, the camera focusing in on a bloody corsage littering the side of the highway.

I drove a car no faster than I pushed the lawn mower, and the instructor soon lost patience.

"That license is going to be your death warrant," my father said on the day I received my learner's permit. "You're going to get out there and kill someone, and the guilt is going to tear your heart out."

The thought of killing myself had slowed me down to five miles per hour. The thought of killing someone else stopped me completely.

My mother had picked me up from a play rehearsal one rainy night when, cresting a hill, the car ran over something it shouldn't have. This was not a brick or a misplaced boot but some living creature that cried out when caught beneath the tire. "Shit," my mother whispered, tapping her forehead against the steering wheel. "Shit, shit shit." We covered our heads against the rain and searched the darkened street until we found an orange cat coughing up blood into the gutter. "You killed me," the cat said, pointing at my mother with its flattened paw. "Here I had so much to live for, but now it's over, my whole life wiped out just like that." The cat wheezed rhythmically before closing its eyes and dying.

"Shit," my mother repeated. We walked door to door until finding the cat's owner, a kind and understanding woman whose young daughter shared none of her qualities. "You killed my cat," she screamed, sobbing into her mother's skirt. "You're mean and you're ugly and you killed my cat."

"She's at that age," the woman said, stroking the child's hair.

My mother felt bad enough without the lecture that awaited her at home. "That could have been a child!" my father shouted. "Think about that the next time you're tearing down the street searching for kicks." He made it sound as if my mother ran down cats for sport. "You think this is funny," he said, "but we'll see who's laughing when you're behind bars awaiting trial for manslaughter." I received a variation on the same speech after sideswiping a mailbox. Despite my mother's encouragement, I surrendered my permit and never drove again. My nerves just couldn't take it. It seemed much safer to hitchhike.

My father objected when I moved to Chicago, and waged a full-fledged campaign of terror when I announced I would be moving to New York. "New York! Are you out of your mind? You might as well take a razor to your throat because, let me tell you something, those New Yorkers are going to eat you alive." He spoke of friends who had been robbed and bludgeoned by packs of roving gangs and sent me newspaper clippings detailing the tragic slayings of joggers and vacationing tourists. "This could be you!" he wrote in the margin.

I'd lived in New York for several years when, traveling upstate to attend a wedding, I stopped in my father's hometown. We hadn't visited since our grandmother moved in with us, and I felt my way around with a creepy familiarity. I found my father's old apartment, but his friend's shoe store had been converted into a pool hall. When I called to tell him about it, my father said, "What shoe store? What are you talking about?"

"The place where your friend worked," I said. "You remember, the guy whose eye you shot out."

"Frank?" he said. "I didn't shoot his eye out; the guy was born that way."

My father visits me now in New York. We'll walk through Washington Square, where he'll yell, "Get a look at the ugly mug on that one!" referring to a three-hundred-pound biker with grinning skulls tattooed like a choker around his neck. A young man in Central Park is photographing his girlfriend, and my father races to throw himself into the picture. "All right, sweetheart," he says, placing his arm around the startled victim, "it's time to get comfortable." r cower as he marches into posh grocery stores, demanding to speak to the manager. "Back home r can get this exact same cantaloupe for less than half this price," he says. The managers invariably suggest that he do just that. He screams at waiters and cuts in line at tony restaurants. "I have a friend," I tell him, "who lost his right arm snapping his fingers at a waiter."

"Oh, you kids," he says. "Not a one of you has got so much as a teaspoon of gumption. I don't know where you got it from, but in the end, it's going to kill you."
```

---

## IC-1344: Dangerous Pie

- Title: Dangerous Pie
- Author (byline): Jordan Sonnenblick
- Work: Drums, Girls and Dangerous Pie
- Publisher: DayBue Publishing
- Publication date as stated: May 2004
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1677
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jordan Sonnenblick
Book: Drums, Girls and Dangerous Pie
ISBN: 096689409X
Publisher: DayBue Publishing
Date (Month/Year): May 2004
```

### Introduction (context only: never use it for content warnings)

```text
Children have been taught since the beginning of time to love their siblings. Those “only children” out there, count yourselves lucky because loving a sibling is hard. Especially when you have a brother like Jeffery: the cutest, sweetest, most embarrassing, and annoying child to ever walk the planet. “Dangerous Pie” by Jordan Sonnenblick
```

### Performance text (classify this)

```text
I guess a good starting point would be the longest journal I've ever written in English class. This was back in September, when I was pretty sure about life. The topic was "The Most Annoying Thing in the World," and we were supposed to write the usual one-page response to it. I sat there for a few minutes, staring at the back of Renee Albert, who's the hottest girl in the eighth grade, trying to concentrate. Unfortunately, all I could concentrate on was Renee Albert. Did I mention she's the hottest girl in the eighth grade? Miss Palma is always going on and on about brainstorming and lists and "prewriting," so I started a list of truly annoying things: .Journal assignments . Dull pencils . The pencil sharpener smell . Miss Palma's perfume . Why doesn't Renee Albert ever look at me? Hot girls who never look at skinny geeks . Being a skinny geek . Being a skinny geek named Steven

Just then I realized that Miss Palma was standing behind me, reading over my shoulder (I guess that's why I was being asphyxiated by her perfume). Thinking fast, I covered up my list, turned to her, and asked, "Miss Palma, can the journal be longer than a page?"

Sure Steven. Why? What are you thinking about creating here?

("Creating here." She actually said that. Don't English teachers just slay you? My mom is actually an English teacher, but that doesn't mean I don't find my own English teachers a bit odd.)

Well, I’m having trouble crafting my prose. (Yeah, "crafting my prose." Two can play this game. . .)

What;' your topic! Remember what I always say; “F.F.F!” (Stands for "Form Follows Function," don't you know.)

Hmm…I want to write about a good topic…I want to write about…(And then it hit me. The most annoying thing in my

world is . . .)

My little brother Jeffery! Anyway, here's what I wrote:

Having a brother is horrible. Having any brother would be horrible, I suppose, but having my particular brother, Jeffrey, is an unrelenting nightmare. It's not because he's eight years younger than I am, although that's part of it. How would you like to be King of the Planet for eight glorious years, and then suddenly get demoted to "Vice-King?" It's not because he's cuter than I am, although that's part of it too. I have mouse-brown cowlick-y hair, glasses that are about an inch thick and braces that look like I tried to swallow a train wreck. He has those perfect little-kid Chiclet-white teeth, 20-20 vision, and little blond ringlets like the ones on the angels you see on the posters in art class. It's not even because he hates me - he doesn't. The truth is that he idolizes me. And that's the problem: the kid follows me around like I'm Elvis or something. And while he's being much too cute and following me around, he also destroys all of my stuff, including my self-esteem and my sanity.

Take, for example, the "Dangerous Pie" incident. Jeffrey has known from an early age that the worst possible thing he can do to me is to touch my drum stuff. I have some rules about this: he may not PLAY the drums, he may not pretend the cymbals are shields and he is a knight, he may not hide IN the bass drum, and pretty much any Jeffrey-to-drumsticks contact is a massive no-no. But on one fateful afternoon last year, Jeffrey threw the rules out the window.

On the tragic day, I came home, said hi to Mom, glugged down some milk, and headed down to the basement to practice. I was in a particularly good mood, I remember, because Renee Albert had told me in P.M. homeroom that she liked my shirt. As this was such a grand occasion, I decided to take the Special Sticks down from their sacred perch and use them for my practice-pad warm-up. In case you didn't know this, a practice pad is a thick, dense, flat piece of rubber. Usually it's glued onto a piece of wood. You practice playing drums on it, because it feels a lot like playing on a real drumhead. Anyhow, the Special Sticks would be just an ordinary pair of my favorite sticks - Regal Tip 51’s with nylon tips - except that they have been autographed by my all-time drum hero, Carter Beauford of the Dave Matthews Band. I once saved up all my babysitting money for a couple of months, got two tickets to a drum clinic Carter Beauford was giving an hour and a half away in Philadelphia, and begged my Dad to take me for two weeks until he finally gave in. At the clinic, during what I like to think of as "The Two Glorious Minutes," Carter Beauford himself called me up front to demonstrate a double-stroke roll. After I did it, he said I had "nice technique," and signed my sticks, right there in front of a roomful of drummers! So I had spent quite a bit of blood, toil, tears, and sweat in order to get the Special Sticks. But the Special Sticks weren't on their shelf. Jeffrey!

I ran upstairs at top speed, hoping I would be in time, but knowing that the odds were stacked against me. I burst into the kitchen and found Jeffrey doing his 'cooking' thing on the floor. Pots and pans were everywhere-don't ask me how I had somehow not noticed this on my way downstairs the first time-and Jeffrey was stirring some pretend concoction in the deepest pot of all. With my Special Sticks.

I advanced toward him, with what must have been a disturbing gleam of violence in my eye.

Jeffrey! Give-me-the-sticks.

But I'm just COOKING.

Give-me-the-sticks.

But the Dangerous Pie isn’t ready yet!

I don't care about your stupid four-year-old make-believe food.

Give-me-the-sticks!

But it’s REAL food!

And it was. Jeffrey's Dangerous Pie was a zesty blend of coffee grounds, raw eggs and their smashed shells, Coke, uncooked bacon, and three Matchbox racing cars.

The Special Sticks STILL smell funny.

Or maybe I should tell you about the "Please kill me Mom" affair. This fiasco happened after my All-City High School Jazz Band concert last June. Getting into the All-City band is a big, big deal, especially for a drummer - because there are six trumpeters, five saxes, four trombones, et cetera, but only two drummers. It was even a bigger deal for me last year, because I was the first seventh grade drummer EVER admitted into the All-City high school band. They even had to send a special van to the middle school just to get me and this girl named Annette Watson, who's the backup piano player. She's actually really good, but there's this twelfth grade guy who's been the main pianist since he was a freshman, and he's not about to get booted by a middle school girl in his senior year. She's funny, and she may be the only kid in the middle school who cares about music the way I do, but she's also kind of weird. It's like she's figured out how to play Beethoven and Thelonious Monk, but hasn't quite mastered the art of being a girl yet.

It's not easy being the youngest guy in the band, by the way. They make fun of me all the time about my age, my size, my braces, and the way I stick out my tongue when I play.

Anyway, my whole family came to the concert, and it was AWESOME. I had this huge drum feature in this Brian Setzer song called "Jump Jive an' Wail" and I nailed the whole thing. I usually practice at least an hour a day on my practice pad and another half hour on my drum set, plus I play in the marching band and the jazz group in school, AND we had been rehearsing twice a week for All City for a couple of months, AND I used to take lessons once a week, so I was playing great that night. So after the concert, my parents and Jeffrey came to the band room. They were all excited and everything, but Jeffrey was bouncing off the ceiling:

You’re a rock star Steven.

No, I'm a JAZZ drummer Jeffy.

MY BROTHER IS A ROCK STAR! MY BROTHER IS A ROCK STAR!

Just then, Renee Albert stopped right next to us to congratulate her boyfriend (we'll just call him Biff), a sophomore guitarist with an alarmingly perfect complexion and muscles like Sammy Sosa. Jeffrey saw Renee, and started to whirl toward her-she lives around the corner from us, and I guess not even four-year-olds are immune to her charms and wiles. It seemed to happen in slow motion; events were just crawling. Yet still I knew I would never have time to run across town to the local zoo, steal an elephant tranquilizer gun, run back, and fire it into Jeffrey's buttock before he could blurt out something that would mortify me and destroy my social status forever.

Life snapped back into full-speed, and Jeffrey shouted: Hey, Renee! MY
BROTHER IS A ROCK STAR!
As Biff looked on with a sneer, Renee replied:
Really? I didn’t know that.
Yup, did you see his arms zooming around on the drums? It’s just like when he
practices in the mirror.
Steven practices in front of a mirror?
Yeah! He does it in his underwear. The blue ones. Right Steven?
I sagged against my mom's shoulder and muttered: Please kill me, Mom.

My dad tried at that point to control the situation, but by now Jeffrey had drawn a little crowd of my band mates, who were just waiting to see what else he would reveal.

My brother is GREAT! Hey, Renee, do you want to hear a JOKE? What does I- C-U-P spell?

I give up.

Close the bathroom door! GET IT?

Dear Reader: Are you starting to see a pattern here?

Miss Palma gave me an "A" on the journal entry-she called it "droll" -so I guess I actually managed to get some use out of Jeffrey's antics before the chaos of this year started. Looking back on those days now, I'd have eaten the Dangerous Pie if I could have stopped October from coming.
```

---

## IC-1345: The Day I Swapped My Dad for Two Goldfish

- Title: The Day I Swapped My Dad for Two Goldfish
- Author (byline): Neil Gaiman
- Work: Not specified
- Publisher: HarperCollins
- Publication date as stated: May 1997
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: BOY, NATHAN, SISTER, MOTHER, VASHTI, BLINKY, PATTI, DAD
- Teaser before the introduction: Yes
- Spoken words (computed): 1429
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
When a boy swaps his dad for two goldfish, he doesn’t really think about the consequences . . .

BOY: Did so! After all, who would have suspected that other kids would go around swapping stuff too.

BOY: Okay . . . maybe I didn’t think about that! And when his mom finds out . . .

BOY: Who knew he’d be that valuable anyway??

The Day I Swapped My Dad for Two Goldfish by Neil Gaiman
```

### Performance text (classify this)

```text
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

## IC-1346: Degas, C’est Moi

- Title: Degas, C’est Moi
- Author (byline): David Ives
- Work: Time Flies and Other Short Plays, Pgs 19-32
- Publisher: Grove Press Inc.
- Publication date as stated: March 2001
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ED, DORIS, DRY CLEANER, NEWSGUY, UNEMPLOYMENT WORKER, LIBRARIAN, YOUNG WOMAN, MUSEUM GOER, MUSEUM GUARD
- Teaser before the introduction: No
- Spoken words (computed): 1435
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Ives
Book: Time Flies and Other Short Plays, Pgs 19-32
ISBN: 978-0802137586
Publisher: Grove Press Inc.
Date (Month/Year): March 2001
```

### Introduction (context only: never use it for content warnings)

```text
Edgar Degas once explained his talent: "It's one thing to copy what one sees, but it's much better to draw what can only be seen in one's memory. It's a transformation during which the imagination collaborates with the memory . . . there your recollections and fantasies are freed from the tyranny exerted by nature."

Today, you’ll be witness to Ed’s transformation . . . from mild-mannered unemployed Nothing to a world-of-his-own creation in which he becomes Degas for the day.

Degas, C’est Moi by David Ives.
```

### Performance text (classify this)

```text
ED is asleep. An alarm clock goes off. He doesn't move. Then, he is suddenly awake.

ED: (Pg 19-32) A stroke of genius. I decide to be Degas for a day. Edgar Degas. Why Degas? says a pesky little voice at the back of my head. Well, why not Degas? Pourquoi, pas Degas? Maybe the prismatic bars of color on my ceiling have inspired me. Maybe the creamy white light spreading on my walls has moved me. Maybe it's all this cheap French wine I been drinking. (He finds a wine bottle in his bed) Anyway I don't have to explain myself Yes! Today, I will be Edgar Degas! -- Is it Edgar, or Edouard? Okay, so I don't know much about Degas. Let's see. 'Dead, French, impressionist painter of jockeys, ballerinas, flowers, that kinda thing. And okay granted, I'm not French, dead, or a painter of any kind. Not a lotta common ground. And yet, and yet -- are Degas and I not united by our shared humanity? By our common need for love, coffee, and deodorant? (DORIS enters.) Doris breaks in on my inspiration.

DORIS: Oh God, oh God, oh God. Have you seen my glasses? I can't find my glasses.

ED: Doris, I say to Doris, I'm going to be Degas today. Doris doesn't see the brilliance of the idea.

DORIS: This is a tragedy.

ED: Doris -- I am Degas!

DORIS: You're what?

ED: Is it Edgar or Edward? It's Edgar, isn't it.

DORIS: Don't forget the dry cleaning. (Doris kisses him.) 'Bye. (Doris exits.)

ED: Alas, poor Doris. Distracted by the banal. No matter. I start my day and brush my teeth as Degas. (Ed hops out of bed and produces a green toothbrush. The bed disappears.) Oh man. This is wonderful! In the bathroom, everything seems transformed, yet nothing has changed. Will you look at the lustre of that toilet? And the light on that green plastic! The bristles are disgusting, but the light is fantastic! (French accent) Per'aps I wed paint you later. How did I become such a genius? I, who flunked woodshop in high school? Well, something must've happened. Because now I'm great. I'm brilliant. My name will live forever! (He considers that a second) Whoo. Wow. This is too big for even me to contemplate. I go out into the world with dry cleaning. (He grabs some clothing as we hear city noises, car horns) O, glorious polychromatic city! Gone the dreary daily deja vu. Today- Degas vu! At the dry cleaner's I notice something strange. . .

DRY CLEANER: (taking the dry cleaning) Jacket, one shirt, one skirt, one

ED: My dry cleaner acts exactly the same.

DRY CLEANER: You know you need some serious reweaving?

ED: Madam, how I would love to capture you in charcoal.

DRY CLEANER: My husband already caught me in puce. (Tears a sheet off the pad.) After five.

(exits with the clothing)

ED: She gives not a flutter of recognition. Then on the corner, the newsguy tries to sell me my paper just like always.

NEWSGUY: Daily Noose?

ED: Actually, have you got anything en Jranfaise?

NEWSGUY: Let's see, I got Le Monde, Le Reve, La Chasse, and Mademoiselle Boom Boom.

ED: I'll just take the News.

NEWSGUY: Change. (He flips an invisible coin, which Ed "catches," then the Newsguy exits)

ED: Still not a blink of recognition. Then as I head down Broadway, people pass me by without a second glance. I might as well be invisible. I, Edgar Degas! And then I realize with a shock: It makes no difference to be Degas. To all these people, I could be anyone! And yet. . . And yet maybe the other Degas walked this invisibly through Paris. (We hear a French accordion and the clip-clop if horses) Maybe he too was rudely bumped into by the bourgeoisie on the upper Left Bank. . . And you know, there's a kind of comfort in this. Completely anonymous, I'm free to appreciate the gray cloud of pigeons overhead. . . The impasto at Ray's Pizza. . . Nobody knows it, but I am walking down this street with a jewel cupped in my hands. The secret precious jewel of my talent.

UNEMPLOYMENT WORKER: Next!

ED: My delicious anonymity continues at Unemployment.

UNEMPLOYMENT WORKER: Sign your claim at the bottom, please.

ED: Do you notice the name I signed in the bottom right corner?

UNEMPLOYMENT WORKER: Edgar Day-hass. Edgar Deejis. Edgar De Gas. Edgar De What?

ED: Edgar Degas. And-?

UNEMPLOYMENT WORKER: And -- this name at the bottom does not match the name at the top of the form.

ED: No, no, no, no . . .

UNEMPLOYMENT WORKER: Are you not the same person as the person at the top of the form?

ED: I am a person at the top of my form. I am Edgar. Degas.

UNEMPLOYMENT WORKER: The dead French painter?

ED: The same. UNEMPLOYMENT WORKER Next!

ED: Oh -- the library. Maybe I should look myself up.

LIBRARIAN: Shhhhhh!

ED: Excuse me. Have you got anything on Degas?

LIBRARIAN: Degas. You mean the crassly conservative counterfeminist patriarchal pedophile painter?

ED: No, I mean the colorist who chronicled his age and who continues to inspire through countless posters, postcards and T-shirts.

LIBRARIAN: Section D, aisle two.

ED: Patriarchal pedoph . . . LIBRARIANQUIET! (Librarian exits)

ED: But who needs the carping of critics, the lies of biographers? I know who I am. Famished by creativity, I stop at Twin Donut. (Two tables appear. A YOUNG WOMAN sits at one, writing in a journal. Ed sits at the other) So there I am, scribbling a priceless doodle on my napkin, when I notice someone staring at me. A young woman writing in a journal. Has she recognized me? She smiles slightly. Yes. She knows I am Degas. Not only that. She loves Degas. That one look has redeemed all my years of effort. My work has given meaning to someone's life. (A schmaltzy-romantic violin is heard)

YOUNG WOMAN: (writing) "April six. Twin Donut. Just saw Edgar Degas two tables over. So he likes vanilla crullers too! Suddenly this day is glorious and memorable. Would love to lie in bed all afternoon and make l' amour with Degas. . ."

ED: But no. I'd only cast her off, break her heart. Not to mention what it would do to Doris. But isn't it my duty as an artist to experience life to the fullest. . . ?

YOUNG WOMAN: (writing) "Dwayne would kill me."

ED: Too late. Whoa, whoa, whoa, just for a picosecond there, I forget who I am! Just for a moment -- I seem to be nobody. The labor of hanging onto one's identity! At the museum I am simply amazed to find how much I accomplished -- even without television. (A Degas self-portrait appears) What's this. . . Ah. A self-portrait. Not a great likeness, maybe. But so full of. . . what? . . . feeling. I stare into my fathomless eyes. (A MUSEUM GOER stands beside him looking at the portrait)

MUSEUM GOER: Mmm. Bit smudgy, isn't it?

ED: "Smudgy"?

MUSEUM GOER: This area in here.

ED: Yeah, but what about this area over here?

MUSEUM GOER: No, but look at this area here. This is smudge.

ED: Okay. So I had an off day.

MUSEUM GOER: An "off day" . . . ?

ED: Not all my work was perfect. Philistine. Probably headed for van Gogh. To kneel in adoration at the sunflowers. I couldn't believe it, the day he started signing his paintings "Vincent." "Vince," we called him. What a jerk.

Ah yes. Woman with Chrysanthemums. A personal favorite among my masterworks. God, when I remember that morning over a century ago. . . Can it be that long now? This was an empty canvas and I stood in front it paralyzed by its whiteness. Then I reached for my brush. . . He produces a paintbrush. . . . and the picture crystallized. In a moment I saw it all. This pensive woman, oblivious of the transcendent burst of color right at her shoulder. The natural exuberance of the flowers alongside her human sorrow. Yes. Yes! Our blindness to the beautiful! Our insensibility to the splendor right there within our reach!

MUSEUM GUARD: Step back, please.

ED: Excuse me?

MUSEUM GUARD: The painting. You have to step back, sir. You're too close to

ED: I'm too dose to this painting. . . ?

MUSEUM GUARD: Do you copy?

ED: No, I don't copy. I am an original! I step back. (Guard exits) But the glow of my exaltation stays with me all the way to the Akropolis Diner. . . where Doris meets me for dinner.

DORIS: What a day.

ED: What a fabulous day. Epic!

DORIS: Six hours of xeroxing.

ED: No, listen. Degas. Remember? I've been Degas all day.

DORIS: The toilets erupted again. The women's room was like Vesuvius.

ED: I am Degas.

DORIS: They were going to fix those toilets last week.

ED: As Doris dilates on toilets, I begin to feel Degas slip away a little. . . like a second skin I'm shedding. . . leaving nothing behind.

People say they have a voice inside their heads. The voice that tells themselves the story of their lives. I too have always had a voice like that in my head. But now, tonight, no one is listening. The story of my life is going on unwatched. Unheard. I am alone. I find myself upstairs, sprawled on the bed while Doris runs the bathwater. Degas is dust. All my glory, all my fame, all my achievements are utterly forgotten. Immortality? A cruel joke. Then I find myself looking through the doorway into the bathroom and I see Doris standing with her foot up on the edge of the old lion-footed tub, drying herself. The overhead light is dim, but Doris is fluorescent-radiant-luminous-with pinks and lavenders and vermilions playing over her skin. The frayed towel she's wrapped in gleams like a rose. She turns and looks back at me and smiles.

Degas? Who needs him?
```

---

## IC-1347: Don’t Encourage Him

- Title: Don’t Encourage Him
- Author (byline): Jason Taylor
- Work: Kennedy Center American College Theater Festival Best Student One Acts, Vol. 5
- Publisher: Dramatic Publishing Company
- Publication date as stated: Jan 1999
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: JASON, CHRIS, TOBY, DAD
- Teaser before the introduction: Yes
- Spoken words (computed): 1945
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jason Taylor
Book: Kennedy Center American College Theater Festival Best Student One Acts, Vol. 5
ISBN: 978-1583420003
Publisher: Dramatic Publishing Company
Date (Month/Year): Jan 1999
```

### Introduction (context only: never use it for content warnings)

```text
Who is the person you'll probably know the longest in your life? Yep, it's your sister or your brother. You live together, play together, party together, eat together, laugh together and fight together. Some brothers have terrific, sharing relationships with each other and are the closest of friends. On the other hand, some brothers can infuriate each other.

Don’t Encourage Him by Jason Taylor
```

### Performance text (classify this)

```text
JASON: (Pg 123-142) When I was six years old, I was walking through the woods behind my parents’ house, when I came across this tiny lump of fur. (kneels) When I bend down to take a real good look, I can see that it’s a tiny baby rabbit. Just lookin’ up at me. Then my father’s voice went off in my head: “If you find a baby animal in the wild, don’t touch it. You’ll leave human scent on it, and its mother will smell it and won’t take care of it anymore, and it’ll die.” But I was only six and I thought, “Maybe if I just touch him once . . . just real quick, maybe I won’t leave any scent on him.” So I reached down and touched him once . . . just a quick stroke across the back . . . and I realize he’s just as soft as I thought.

So, before I know it, I’m holding him, cradled in my arms, stroking him across the back . . . and I suddenly get this horrible, deep, remorseful feeling in my stomach because I realize that I probably just killed him. At six years old that’s pretty hard to deal with. I took him home and looked for anywhere on the farm where I could hide him. . . when I saw the chicken coop. For the next month I volunteered to do all the chicken chores in hopes that no one would find my stupid mistake. And the most amazing thing happened.

My rabbit stopped sleeping in the corner by himself and started sleeping with the hens. Then, he started playing with the chicks. He even started eating chicken feed and I thought, “Wow! Maybe he’s not going to die because of my stupid mistake.” But as soon as it started, it stopped. He stopped playing and he stopped eating, and he started sleeping in the corner again . . . alone . . . growing skinnier and skinnier. He was going to die for sure.

My mother took one look at him and said, “Jason, you have to let him go.” That sick feeling in the pit of my stomach told me that she was right. So I gathered up my rabbit and took him to the exact spot where I’d found him. That sick feeling in my stomach was replaced by pride – pride that I’d done the right thing by letting him go. And just when I was feeling my proudest, I see my brother coming back from a hunting trip. He’s got a gun in his right hand and in his left . . . by his hind legs . . . he’s got my rabbit!

CHRIS: Jason! Come here! Today you’re going to be a man . . . today, I’m gonna show you how to skin and clean and cook a rabbit.

JASON: That night at the dinner table I didn’t say a word, didn’t shed a tear. I didn’t want my family to think I couldn’t handle it. So, I sat there with my family and I helped them eat the one I loved. And you know what? (Sour look is replaced with a grin) It tasted just like chicken!

JASON: A lot of people tell me about their horrible upbringings. How they grew up in Chicago, or Detroit or New York, and I have to think that I’m right up there with them . . . because I grew up on a farm with brothers -- [which] gives you a slightly better survival rate that growing up in England during the plague.

I had two brothers, Jon and Chris. Jon was too young to get into the battles that my older brother and I got into. My older brother was the master. He’d developed his strategy into two different personalities. On the one hand, he was Chris! My Brother! My Blood! My best friend in the entire world! But that was countered with, (evil grin) Chris! The Assassin! The man who would do anything to make sure I didn’t reach eighteen! This one time, I was watching television, when I hear my brother’s voice from upstairs.

CHRIS: Jason! Come upstairs! I want to play with you!

JASON: (clasps hands with a boyish grin) Wow! My brother wants to play with me? I must be the luckiest guy in the world! So I was halfway up the stairs when all of a sudden, Chris – my brother, my blood, my best friend -- disappears (evil grin) And Chris the assassin is waiting for me with one of those great big, five-pound, nine-volt batteries. You know what I’m talking about? And he drops it -- BANG! Right on my head (smacks his hand against his head and falls to the floor) Knocking me out instantly. I woke up a few minutes later (groggily rises) I’m not sure how long it was, I couldn’t tell time yet – and I see the battery on the floor and it has a dent in it this big. (shows measurement with hand, then holds measurement up to his head) And my head has a bump on it just the size of the dent.

So I pick up the battery and run to my mom. “Mom! Mom! Chris took this battery and threw it off the top of the stairs and it hit me in the head and made this huge dent!” My mom takes the battery, takes one look at the dent . . . and I swear to God on a stack of Bibles, she says, “If your head had made a dent that big, you’d be dead right now.”

But the worst thing my brother ever did to me wasn’t physical. It was mental. And it happened one morning [on the bus]. Out of the corner of my eye [I saw him] -- Toby Cartwright, the dumbest fifth-grader in the history of fifth-graders, already has his lunch open and he’s eating it at seven-thirty in the morning. But before I can look away, Toby sees me looking at him.

TOBY: (Leans over chewing open-mouthed and holding an imaginary sandwich) What did you bring for lunch?

JASON: So I look to my brother for help. MY BROTHER – MY BLOOD – MY ONLY FRIEND ON THIS TRAVELING FREAK SHOW (to Chris) Chris! What do I do? Toby’s talking to me! (to audience) But suddenly he’s not Chris my brother anymore . . . SUDDENLY he’s CHRIS THE STRANGER who just happened to get on the bus with me and now stares out the window blankly, basically telling me that if anything does down, I’m on my own. So I look back at Toby

TOBY: What did you bring for lunch?

JASON: I’m not allowed to open my lunch till lunchtime.

TOBY: Says who?

JASON: Says the teacher, I guess.

TOBY: So who is she to tell you when you can or can’t eat your own lunch?

JASON: (cocks head and looks out over audience as if deep in thought) And the was the deepest thing I’d ever heard my entire life. I was only like eight. I hadn’t heard very many things. Don’t run with scissors, don’t play with fire, pants before shoes . . . and “Who is she to tell you when you can or can’t eat your own lunch?” So I ate it! Oh, yeah! I opened it up and scarfed the sandwich and the chips and sucked down my juice box, and I thought, “THIS TASTES BETTER AT 8 AM THAN IT EVER TASTED AT NOON!”

Of course, noon rolled around and I was hungrier than *anything*! And Toby Cartwright was fine because he’d probably spent the whole morning eating paste and crayons! So I go to my brother. (to Chris with sad, forlorn look) Chris, can I have a carrot stick? I ate my lunch on the bus today.

CHRIS: You stupid idiot! [You listened to] Toby Cartwright? He’s 16 and still in the fifth-grade! He wears a stocking cap 365 days a year! No, you can’t have a carrot stick! Get away from me!

JASON: You know what? I wouldn’t have eaten my lunch today if you’d just said something. If you’d just sitck up for me like a brother’s supposed to. If you’d just told Toby to leave me alone. But you didn’t. You didn’t say a word. You abandoned me on the bus. You abandoned me, Chris. And I’m gonna get you back. (looks to audience with the evil grin) You wanna know what I did? Do you wanna? Well, one morning while I was watching Pee Wee’s Playhouse . . . I cut his finger off! (laughs demonically)

I used to run downstairs every Saturday morning and turn the TV on and just go crazy. I thought Pee Wee Herman was a genius! But one morning, just before Pee Wee’s Playhouse started, Chris hit me with a pillow. (as if he’s just been hit) BANG!

CHRIS: If you were in the army, you’d be dead right now!

JASON: Knock it off! Pee Wee’s about to start! (to audience) But he does it again – BANG! (to Chris) If you don’t knock it off, I’m gonna kick your butt. (to audience) But just when I turn my head to watch, he hits me for the third time . . . BANG! So I grab a pillow of my own and chase him up the stairs. [I turn to get back to my show] and with every ounce of my tiny muscles, I slammed the door as hard as I could – (slams imaginary door) WHAM! (walks away smiling)

CHRIS: (blood curdling scream) I open the door and Chris is holding his bloody hand (demonstrates) And I think, “That’s odd. I wonder why Chris’ hand is all bloody.” So I look down and mashed to the door frame (holds up index finger) is the index finger of his left hand . . . pointing at ME! (moves finger as if it’s talking) “Jason . . . Jason . . . why did you sever me, Jason? (to finger) I don’t know, Chris’ finger. I’m sorry. I didn’t mean to. (to audience) My dad burst through the door. He sees the finger and says

DAD: WHAT THE HELL ARE YOU PLAYIN’ IN HERE?

JASON: Dad, Dad! I’m sorry. I slammed Chris’ finger in the door and accidentally cut it off! (to audience) So he grabs my brother by the collar . . . and he PEELS the finger off the door frame and shoves it in his pocket with some ice and he drives to the hospital where they finally sewed it back on after four hours of surgery. (examines finger) And it grew back kind of funny. The nail’s all crooked, but it looks pretty good considering (evil assassin grin) Considering it was slammed in a doorway and separated from his body for four hours! Ha! Ha! Ha! Jason the assassin strikes back!

It may have been the greatest mistake I ever made. For the rest of my life and I’ll never be able to admit any minor discomfort without being reminded about how bad that finger hurt. I could be on my deathbed with malaria and say, “Chris . . . could you get me a glass of water?” And he’d say,

CHRIS: Boy! That malaria looks pretty bad. But I bet it doesn’t hurt as bad as the time you cut my finger off! Get your own water! Malaria boy!

JASON: This one time, Chris is building his model airplane kit and he needs to solder the engine together, which entails dripping molten metal onto solid metal in order to attach the pieces, and he says -

CHRIS: Jason! Come here! (places the engine in Jason’s hands) Hold this. And don’t move, ‘cause if you move and I drip some on the propeller, it’ll be ruined and I’ll kick your butt.

JASON: So he starts to solder and I think, “Maybe this will make up for the time I cut his finger off.” And he stops soldering . . .

CHRIS: This isn’t gonna make up for the time you cut my finger off!

JASON: So, I’m standing there holding it, and the metal starts dripping down on my fingers. (bounces up and down as if holding something hot) Chris! Chris! The metal’s dripping down on my fingers and it hurts!

CHRIS: Oh! The metal’s dripping on your fingers huh? (vehemently points at his bad finger)

JASON: So I held it. For an hour I held it, and for an hour it dripped down off the engine and ran down the knuckles on my left hand. Now, I have liquid metal scars on the knuckles of every finger. (points at scars and studies them) Scarred and marred for the rest of my life. And my only consolation is it doesn’t look as bad as that big piece of meat he’s got on the end of his left hand, you know? And then I thought, “Hey! He sleeps with his door unlocked . . . and he’s got nine more good fingers, baby!” (slams imaginary door) WAM!
```

---

## IC-1348: Don’t Fear the Reaper

- Title: Don’t Fear the Reaper
- Author (byline): Eddie Zipperer
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: Sept 2008
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ANNOUNCER, DONNIE, STEVE, SATAN, GOD, DEATH, BILL, BIL, JEREMY, CONCEPTION, TV ANCHORMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 2121
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eddie Zipperer
ISBN: 978-1583425954
Publisher: Dramatic Publishing
Date (Month/Year): Sept 2008
```

### Introduction (context only: never use it for content warnings)

```text
Steve fell asleep with chips in his mouth. What a horrible way to die. It’s called sloth and it’s one of the deadly sins. But when Death arrives to take his immortal soul, he finds that Steve has achieved a perfect balance upon the scales of good and evil. Mediocrity to the highest degree! So, going against protocol, Death gives Steve the opportunity to decide for himself if he will be sent to heaven or hell by playing THE FATING GAME.

Don’t Fear the Reaper by Eddie Zipperer
```

### Performance text (classify this)

```text
ANNOUNCER: (excited) Welcome to the game show where chance and circumstance determine your final dance. Time to find out if Steve, a gamer and television connoisseur, will be put to rest with the blessed or the stressed. It’s time for . . . THE FATING GAME! Now here’s your host, Donnie Destiny! (Donnie enters. He is enthusiastic, like all game-show hosts)

DONNIE: Howdy all! I’m Donnie Destiny! You all know how the show works. Our contestant asks questions that the King of Kings and the Dark Lord have to answer, then based on those answers the contestant chooses a fate. You ready Steve? Great! Then without further ado let’s meet your fates.

ANNOUNCER: Our first fate has been the dark ruler of hell since the dawn of good and evil. You may know him as Beelzebub, Lucifer, or the Prince of Darkness. Let’s welcome, from the Hebrew for accuser, Satan! (Satan enters. He waves at the studio audience) Fate number two is arriving straight from heaven where he enjoys having his name praised, hymns of thanksgiving and long walks on the clouds. Give it up for notorious G-O-D! (God glides in and stands next to Satan)

DONNIE: All right now that everyone’s present and accounted for, let’s play . . . THE FATING GAME!

STEVE: Fate number one: if you could give me one gift, and it could be anything, what would it be?

SATAN: I’m glad you asked me that, Stevie – I like your voice. It’s kind of manly and sexy. I bet you’re tall. If I could give you one gift, Stevie, it would be the perfect day. We’d wake up at noon, watch a little Star Trek. We’d eat all the junk food we could get our hands on and . . .

GOD: This is disgusting! Really! If I could give you one gift right now, Steve, it would be the gift to see this Satan in his true form. I mean, honestly, do you think Satan really sounds like that?

STEVE: Fate number two, how much responsibility would you expect of me?

GOD: A great deal, and yet none at the same time. For when you take joy in your responsibility, you will want to be accountable for it.

SATAN: (Bursts out laughing) I’m sorry. Seriously? Look Steve, choose me, and if you consider playing video games, and watching TV, and doing whatever you want whenever you want responsibility – then you can expect a lot.

GOD: Think of how that worked out for you in life, Steve. I will help you be a happier more satisfied soul, not enable you to destroy yourself. That is why you should choose me.

SATAN: (Getting more angry) No, you will choose me, Steve, because you don’t want to be better! You want to be a disgusting slob who chokes on potato chips!

STEVE: Um, I think I’ve made my choice . . .

DONNIE: Congratulations, Steve! This is Donnie Destiny, and I’ll see you next time on . . . THE FATING GAME!

DEATH: Very well, then (begins to exit)

STEVE: Where are you going? I’ve made up my mind.

DEATH: That’s good, but now you have to resume your life and earn that choice.

STEVE: I get to live again?

DEATH: (Death’s pager goes off loudly – He looks at it and sees that it is GOD who is summoning
him. Flustered) For a while, but don’t worry, I’ll be back soon.
****** Scene Break ********
Setting: God is in an office, working. Death enters in his classical form, black cloak and scythe.

NOTE: Death is referred to as Bill for the rest of the play

BILL: You wanted to see me?

GOD: Yes. Death, do you know why I asked to see you today?

BILL: No.

GOD: Well, I want to start by sharing with you some of the letters I’ve been getting. (God opens a drawer of the desk, pulls out a stack of papers and begins reading one) “Dear God, all my life I feared death, but now I understand that it was an irrational fear, and a waste of much of my life. I wish I would have known this soon. This information, together with the meaning of life, which is obviously –blah . . . blah . . . blah. This part gets a little long-winded. Here we go. “When I first awoke and found that my body and soul had been torn from each other, I felt an uncontrollable fear of the unknown path ahead. This fear grew exponentially when the Reaper showed up, but it turned out the Blue Oyster Cult was right. There was no need to fear him. (Bill slumps as God gives him a quick stern look.) He sat me down, and he explained to me that everything was going to be okay, and that I was safe. He asked me if I thought I had led a good life, and when I answered yes, he told me that that would be enough to get me into heaven.” Here’s another. “Dear God, that Reaper of yours is the bomb. I was totally freaked out to be dead and stuff, but he was all, “chill, bro. It’ll be all good.” I have about a thousand more like this. Do I need to keep going?

BILL: No.

GOD: Let me see if I have this right. You’ve been telling anyone and everyone who dies that they’re going to heaven, and that everything will be okay, and that there’s nothing to be afraid of anymore. Is that about right?

BILL: I ask them if they’ve led a good life first.

GOD: So people are deciding the afterlife for themselves now.

BILL: You don’t understand. They’re completely hysterical when I show up. If I don’t show a little compassion –

GOD: A little compassion! A little compassion? Tell me, what’s the number one rule of reaping souls?

BILL: Death can’t be biased, but –

GOD: And why must Death remain unbiased?

BILL: Because otherwise people end up in the wrong place.

GOD: And wouldn’t you agree that people ending up in the wrong place is a monumental error.

BILL: Yes.

GOD: Or do I need to remind you of the three days after you sent Jesus to hell?

BIL: He told me he was responsible for all the sin in the world! What was I supposed to think.

GOD: That’s the point I’m getting at. You are not supposed to be thinking at all. You go by the book. I don’t want to go into the bureaucratic nightmare of getting Jesus back. Let’s just say I’m not interested in dealing with that problem again.

BILL: I’m sorry. It just started to become painful for me. All this sorting people into Heaven souls or Hell souls. People are scared enough when they’ve just died. It was easy when I first got started, but as I got older and sorted more souls, I started to realize that Heaven and Hell is a black and white idea. There’s no middle ground. Someone who’s just a little evil goes to the same place as Hitler? That doesn’t make sense. I’m sorry. It got difficult and stressful for me because it’s kind of dumb, but I’ll go by the book from now on.

GOD: I’m sorry, but unfortunately, I have no choice but to replace you. You’re fired, Bill.

BILL: What! For a little compassion? For trying to do the right thing? I just want people to have a good death. A painless transition from Earth to afterlife

GOD: I know you do. Unfortunately, that’s not the way it works. The afterlife is supposed to be all scary and Biblical. I wish it did work like that, Bill, but it doesn’t.

BILL: Surely, you can appreciate the connotations of this outfit. People see it as evil. They’re scared of me when they see it. They need to be consoled. (Another Reaper, Jeremy, enters)

GOD: I’m going to need you to turn over your scythe to the new Death. (Indicates the Reaper who just walked in).

BILL: What! You gave my job to Jeremy? Jeremy?

JEREMY: The name Jeremy no longer holds any meaning for me. I am . . . Death.

BILL: No, I am . . . Death.

JEREMY: No, you’re Bill now.

GOD: Death is right, Bill.

BILL: Quit calling Jeremy “Death”! He is not Death! He’s not qualified.

JEREMY: Excuse me? Not qualified? I’ll have you know that I have been the reaper of insects for over forth million years, and I have taken many a confused bug from the Earth to eternity without passion or prejudice.

BILL: They’re bugs! Do you know how many bugs there are on Earth right at this moment! Ten quintillion! That’s a one with nineteen zeroes! Have you ever stepped on a bug, Jeremy? God? They’re freakin’ immortal. Where you been, Jeremy? Where you been, huh?

JEREMY: Death needs his scythe, Bill. People need to be able to die. Give me the scythe so I can do my job. I can’t be Death without the scythe. Hand it over.

BILL: Okay. Okay. You win. Just give me a few seconds to – Look over there! (Bill runs from the room as fast as he can and takes the scythe with him. Jeremy and God stand silent and awkward for a moment.)

JEREMY: He took the scythe. That can’t be good. (God gives him a scathing look) I’ll go find him. (Jeremy exits) ****** Scene Break ********

(Bill enters his home in a panic. He is still dressed in the death cloak. He starts looking for a place to hide the scythe, but they all seem too obvious.)

CONCEPTION: (From off stage) Bill, is that you?

BILL: Yes, honey. I’m just – don’t come in here. (He finally hides the scythe under the couch cushions just as his wife, Conception, enters. She wears a white cloak)

CONCEPTION: How was your day at work? What’s wrong? You look awfully sad. Did you have a yucky day? (Bill sits on the couch. He looks very nervous)

BILL: Conception, I have to tell you something. I – How was your day?

CONCEPTION: It was as wonderful and life affirming as usual. I spread many seeds today and gave life to a great many souls. It’s a very fulfilling job, and I feel so blessed, like a bee who has found a flower with very yummy hones, and every day the little bee gets to go eat from that special yummy honey flower. That’s how I feel.

BILL: God. I’m glad you feel like that. That’s good.

CONCEPTION: I think somebody needs a great big love hug. Am I right? Here comes the love hug. (She squeezes him hard and makes a big sigh. She does not let go)

BILL: Conception. Conception. I have to tell you something. Do you have a minute?

CONCEPTION: Hold on. Let me check my little schedule. Thing always start to get busy when it gets dark out. (Checks her schedule) Well, this is strange. I’ve never –

BILL: What is it?

CONCEPTION: My schedule is completely empty. I’ve been Conception for thousands of years, and I’ve never had an empty schedule before. This scares me, Bill. What’s happening out there?

BILL: Don’t worry. Everything is fin. It’s just that, I did something today. I did something bad.

CONCEPTION: There. There. It can’t be all that bad. Just tell me what happened

BILL: Well, I guess, I – (Bill tries very hard to say it. He takes some deep breaths. Finally he picks up the remote control and turns on the TV.)

TV ANCHORMAN: Riots are breaking out everywhere! In just a few short minutes, they have become a staple of every major city in the world. Stores and homes are being ravenously looted and decimated as the rioters unite under the ominous chant, “Hooray, hooray, we’re invincible.” Our in-studio guest today is Reverend Steve. Good evening, Reverend.

STEVE: Good evening, brother.

TV ANCHORMAN: I think what people want to know is, what’s going on? Do the rules of death no longer apply?

STEVE: I think the answer is obvious, my brother. The lord God hath come down from his heavenly throne, and he is testing us. He is testing us like he tested Noah with pain and destruction. Like he tested Job with pain and destruction. Like he tested Master Chief* with pain and destruction -- (*Master Chief is the protagonist of the popular Halo video games. Feel free to replace Master Chief with any video game or television reference: Suggested . . . Donald Trump or Hilary Clinton) (Bill turns off the TV)

BILL: I got fired today.

CONCEPTION: So . . . there’s no more death. They didn’t replace you? I mean, I’m sad you lost your job, but . . .

BILL: Well, they – (There is a sudden banging on the door. Bill jumps to the floor. Conception is confused) Who is it?!

GOD: (off) It’s the King of Kings! The Lord your God!

SATAN: (off) And the prince of Darkness!

JEREMY: (off) And Jeremy. I mean . . . Death.

BILL: It’s not fair! (Bill pulls the scythe out from the couch cushions.) I’m holding the scythe right now. IF you come in, I’m going to bust it in half! Then no one can ever die again.

GOD: You’re going to destroy the world to save yourself, Bill? I thought you knew right from wrong.

BILL: I do, but this is the only way. I don’t have a choice.

SATAN: Do it, Bill! Break it! What? Oh, yeah, sorry. Don’t break it. It would be a totally awesome thing to do, but it really would screw up everything.

GOD: Look, Bill. I know it’s hard, and that things don’t always make sense, and that sometimes right and wrong get confusing, but if Satan and I agree on something, don’t you think you should listen?

BILL: No!

CONCEPTION: They’re right, Bill.

BILL: What? You’re my wife! The most ridiculously compassionate, touchy-feely person I know. You’re supposed to be defending me.

CONCEPTION: If no one . . . finishes living, then no new souls can have a turn to experience life. You don’t want that. I know you, Bill. You aren’t the type to destroy the world. That’s no compassion. Give me the scythe, Bill. I know you want to be a good person. Give it to me.

BILL: But, it’s everything that I am. Death is my entire existence.

CONCEPTION: Don’t be afraid, Bill. This is not the end for you. It’s just something new. You’re not afraid of something new, are you? (Bill pauses for a moment. Then he hands the scythe over.)

BILL: It’s over. You can come in now. (God, Satan and Jeremy enter. Conception gives Jeremy the scythe.)

JEREMY: You are Conception? My new wife? (Conception nods. Jeremy looks at her for a second) Nice! (To Bill) Are you ready to come peacefully?

BILL: I -- I guess I don’t really have a choice.

JEREMY: Don’t worry. I’ll take good care of her. Or do worry. It makes no difference to me. For I am . . . Death. (He takes Bill by the arm)

BILL: (scared) Jeremy, can you tell me what’s – what’s going to happen to me now?

JEREMY: I can tell you what’s going to happen to you if you call me Jeremy one more time.

BILL: (Singing and dancing – Audio for this song, Don’t Fear the Reaper can be found at the link
provided at the end of this selection)
Come on baby, don't fear the reaper
Baby take my hand, don't fear the reaper
We'll be able to fly, don't fear the reaper
Baby I'm your man
La, la, la, la, la / La, la, la, la, la
```

---

## IC-1349: Dr. Fritz

- Title: Dr. Fritz
- Author (byline): David Ives
- Work: Mere Mortals
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Dec 1998
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: MARIA, TOM, MARIA/DR. FRITZ
- Teaser before the introduction: Yes
- Spoken words (computed): 1341
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Ives
Book: Mere Mortals
ISBN: 0822216329
Publisher: Dramatists Play Service, Inc.
Date(Month/Year): Dec 1998
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
MARIA: is sitting behind a crude plank table made from an old door

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

MARIA/DR. FRITZ: Your eyesight is excellent. Open your mouth. Stick out your tongue. Go like this. [He makes a raspberry. Tom does too.] No, like this. [Another raspberry. Tom does too.] Better. Now put your fingers in your ears. Can you hear me?

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

## IC-1350: Dr. Horrible’s Sing-Along Blog (The Book)

- Title: Dr. Horrible’s Sing-Along Blog (The Book)
- Author (byline): Joss Whedon, Maurissa Tanchareon, Jed Whedon and Zack Whedon
- Work: Not specified
- Publisher: Titan Books
- Publication date as stated: March 2011
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: DR. HORRIBLE, MOIST, DR. HORRIBLE & CAPTAIN HAMMER, CAPTAIN HAMMER, PENNY, BAD HORSE CHORUS, MALE ANCHOR, FEMALE ANCHOR, MAYOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1244
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
Wait. . . Wait . . . Wait . . . Before we get going, think about something. Just what is it that makes a superhero “SUPER”? Is it their powers? If that was the case, Batman wouldn’t be considered much of a superhero, would he? No! The key to every great superhero is an equally great, yet undeniably evil, supervillain. Batman and . . . the Joker! Superman and . . . Lex Luthor! Exactly! And the bottom line is that unless you can fly on your own or shoot webs out of your hands, gadgets are a key component to being a superhero or supervillain. Gadgets can mean the difference between saving the world, achieving world domination, (evil maniacal laugh) or simply winning the affection of the girl with the big heart and wonderful hair.

Dr. Horrible’s Sing-Along Blog (The Book) featuring the script and songs by Joss Whedon, Maurissa Tanchareon, Jed Whedon and Zack Whedon

Dr. Horrible is in the lab working on The Freeze Ray (played by Actress). He adjusts various levels and dials, and powers the system up. It appears that it will work, but then abruptly powers down with a message synthesized message [INSUFFICIENT WONDERFLONIUM] *words not in original script, used for transition purposes*
```

### Performance text (classify this)

```text
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

DR. HORRIBLE: Why did she talk to me NOW?

***** SCENE CHANGE – DR. HORRIBLE’S LAIR / WEB BLOG *****

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

***** SCENE CHANGE – DR. HORRIBLE’S LAIR ***** Moist is working in the lair and is shocked when Dr. Horrible arrives. His responses are comedic, but wordless.

DR. HORRIBLE: (Pg 47-48) (he is beside himself with anger – ranting against Captain Hamme) All the times that you beat me unconscious. All the crimes incomplete! Mr. Cool. Mr. Right. Mr. Know-It-All is through! I’m gonna shock the world. Gonna show Bad Horse. [TRANSITION

(these words are not in the script: Moist, Bring my Freeze Ray] (Dr. Horrible and Moist get to work, furiously modifying the FREEZE RAY to a DEATH RAY. Once the modification are complete, Dr. Horrible motions Moist to stand a few steps away. He tests the new Deah Ray. Moist dies and Dr. Horrible laughs maniacally) It’s a brand new day. And Penny will see the evil me. Not a joke, not a dork, not a failure. Captain Hammer . . . You’re gonna die! (he exits)

***** SCENE CHANGE – DEDICATION OF THE NEW HOMELESS SHELTER *****

MALE ANCHOR: (Pg 52) The mayor himself will be on hand to dedicate the new homeless shelter and unveil the statue of Captain Hammer.

FEMALE ANCHOR: (laughing) It’s a good day to be homeless! (cut to Mayor)

MAYOR: (Pg 58) Ladies and Gentlemen, your hero.

CAPTAIN HAMMER: (leaps onto stage, arms extended wide) Thank you, Mayor for those kind words. (reading from index cards) I hate the homeless (next card) –ness that plagues our city. Everyone should have . . You know what? I don’t need tiny cue cards (tosses them on the ground)

DR. HORRIBLE: (Pg 60) (suddenly appears from the crowds, he lets out his perfected, evil maniacal laugh) (Pg 62) Heros are over with. It’s Doctor Horrible’s turn. (He powers up his Death Ray, then hesitates) Here goes – No mercy. (the device powers up, then suddenly runs out of power – audible energy-drain) Thaaat’s not a good sound . . . (Captain Hammer punches him on the jaw, sending his Death Ray flying out of his hands – a fist fight ensues, with Captain Hammer easily beating Dr. Horrible. The fight should be comical. Once Dr. Horrible is defeated, Hammer retrieves the Death Ray and returns to lord it over Dr. H.)

CAPTAIN HAMMER: A Death Ray? Dr. Horrible’s moving up. Let’s see if this one works any better than your others. (He points it toward Dr. Horrible’s head) (Pg 64) Give my regards to St. Peter. Or whoever has his job, but in Hell.

DR. HORRIBLE: Don’t!!! (the Ray explodes sending shrapnel everywhere)

PENNY: (Pg 65) (is hit by the shrapnel, she takes one piece to her chest and one to her stomach, she is having trouble breathing)

DR. HORRIBLE: (moves quickly to Penny) Penny. No. No. Hold on. Hold on –

PENNY: It’s okay. It’s okay, Billy. Are you all right? (trying to smile) Captain Hammer will save us. (she dies)

DR. HORRIBLE: Penny?!? (long pause as he realizes what he has done) Here lies everything. The world I wanted at my feet . . . (Pg 41) (echo of a memory) As of tonight, if all goes according to plan, I am in the Evil League of Evil. (Pg 42) I deserve to get in. You know I do . . . (sad evil laugh) (Pg 65) Well, we all have a choice . . . (with fake bravado) and I am fine.
```

---

## IC-1351: The Drama Bug

- Title: The Drama Bug
- Author (byline): David Sedaris
- Work: Naked
- Publisher: Back Bay Books
- Publication date as stated: June 1998
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1997
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Sedaris
Book: Naked
ISBN: 978-0316777735
Publisher: Back Bay Books
Date (Month/Year): June 1998
```

### Introduction (context only: never use it for content warnings)

```text
You’ve never been bitten until you’ve been bitten by the Drama Bug by David Sedaris
```

### Performance text (classify this)

```text
The man was sent to our class to inspire us, and personally speaking, I thought he did an excellent job. After introducing himself in a relaxed and genial manner, he started toward the back of the room, only to be stopped midway by what we came to know as "the invisible wall," that transparent barrier realized only by psychotics, drug fiends, and other members of the show business community.

I sat enthralled as he righted himself and investigated the imaginary wall with his open palms, running his hands over the seemingly hard surface in hopes of finding a way out. You know you're living in a small town when you can reach the ninth grade without ever having seen a mime. As far as I was concerned, this man was a prophet, a genius, a pioneer in the field of entertainment — and here he was in Raleigh, North Carolina!

The visiting actor returned to our classroom a few months later, removing his topcoat to reveal a black body stocking worn with a putty-colored neck brace, the result of a recent automobile accident. This afternoon's task was to introduce us to the works of William Shakespeare, and once again I was completely captivated by his charm and skill. When the words became confusing, you needed only to pay attention to the actor's face and hands to understand that this particular character was not just angry, but vengeful. I loved the undercurrent of hostility that lay beneath the surface of this deceptively beautiful language and I undertook a campaign to reintroduce Elizabethan English to the citizens of North Carolina.

"Perchance, fair lady, thou dost think me unduly vexed by the sorrowful state of thine quarters," I said to my mother as I ran the vacuum cleaner over the living-room carpet she was inherently too lazy to bother with. "These foul specks, the evidence of life itself, have sullied not only thine shag-tempered mat but also thine character. Be ye mad, woman? Were it a punishable crime to neglect thine dwellings, you, my feeble-spirited mistress, would hang from the tallest tree in penitence for your shameful ways. Be there not garments to launder and iron free of turbulence. Go now, wastrel, and get to it!"

My mother reacted as if I had whipped her with a short length of yarn. I could tell by the state of my room that she spent the next day searching my dresser for drugs. The clothes I took pride in neatly folding were crammed tight into their drawers with no regard for color or category. Tying a feather to the shaft of my ballpoint pen, I quilled her a letter. "The thing that ye search for so desperately," I wrote, "resideth not in mine well-ordered chamber, but in the questionable content of thine own character." I slipped the note into her purse, folded twice and sealed with wax from the candles I now used to light my room.

I took to brooding, refusing to let up until I received a copy of Shakespeare's collected plays. Once they were acquired, I discovered them dense and difficult to follow. Reading the words made me feel dull and stupid, but speaking them made me feel powerful. I found it best to simply carry the book from room to room, occasionally skimming for fun words I might toss into my ever fragrant vocabulary. The dinner hour became either unbearable or excruciating, depending on my mood.

"Methinks, kind sir, most gentle lady, fellow siblings all, that this barnyard fowl be most tasty and succulent, having simmered in its own sweet juices for such a time as it might take the sun to pass, rosy and full-fingered, across the plum-colored sky for the course of a twilight hour. 'Tis crisp yet juicy, this plump bird, satisfied in the company of such finely roasted neighbors.”

My enthusiasm knew no limits. Soon my mother was literally begging me to wait in the car while she stepped into the bank or grocery store. Mom had done some asking around and concluded I'd been bitten by what her sister referred to as "the drama bug." My mother was convinced that this was a phase, just like all the others. A few weeks of fanfare and I'd drop show business, just like I had the guitar and my private detective agency. I hated having my life's ambition reduced to the level of a common cold. This wasn't a bug, but a full-fledged virus. It might lay low for a year or two, but this little germ would never go away. It had nothing to do with talent or initiative. Rejection couldn't weaken it, and no amount of success would ever satisfy it. Once diagnosed, the prognosis was terminal.

The drama bug seemed to strike hardest with Jews, homosexuals, and portly girls, whose faces were caked with acne medication. These were individuals who, for one reason or another, desperately craved attention. I would later discover it was a bad idea to gather more than two of these people in an enclosed area for any length of time. The stage was not only a physical place but also a state of mind, and the word audience was defined as anyone forced to suffer your company. We young actors were a string of lightbulbs left burning twenty-four hours a day, exhausting ourselves and others with our self-proclaimed brilliance.

I had the drama bug and my friend Lois had a car. I called her the moment I learned the visiting actor had scheduled a production of Hamlet set to take place in the amphitheater of the Raleigh Rose Garden. He himself would direct and play the title role, but the other parts were up for grabs. We auditioned, and because we were the youngest and least experienced, Lois and I were assigned the roles of the traveling players Hamlet uses to bait his uncle Claudius. It wasn't the part I was hoping for, but I accepted my role with quiet dignity. I had a few decent speeches and planned to work them to the best of my ability.

Our fellow cast members were in their twenties and thirties and had wet their feet in such long-running outdoor dramas as The Lost Colony and Tender Is the Lamb. These were professionals, and I hoped to benefit from their experience, sitting literally at their feet as the director paced the lip of the stage addressing his clenched fist as "poor Yorick."

It was decided that as traveling players, Lois and I would make our entrance tumbling onto the outdoor stage. When she complained that the grass was irritating her skin, the director examined the wee pimples on her back and decided that, from this point on, the players would enter skipping. I had rehearsed my tumble until my brain lost its mooring and could be heard rattling inside my skull, and now, on the basis of one complaint, we were skipping? He'd already cut all my speeches, leaving me with the one line "Aye, my lord." That was it, three lousy syllables. A person could wrench more emotion out of a sneeze than all my dialogue put together.

The less I had to do, the more my fellow actors used me as a personal slave. I would have been happy to help them run lines, but instead, they wanted me to polish their crowns or trot over to a car, searching the backseat for a misplaced dagger.

"Looking for something to do? You can help Doogan glow-tape the props," the director said. "You can chase the spiders out of the dressing room, or better yet, why don't you run down to the store and get us some drinks."

For the most part, Lois sat in the shade doing nothing. When it came time for our big scene, Lois recited her lines as if she were reading the words from the surface of some distant billboard. She squinted and paused between syllables, punctuating each word with a question mark. "Who this? Has seen with tongue? In venom steeped?"

If the director had a problem with her performance, he kept it to himself. I, on the other hand, was instructed to remove the sweater from around my neck, walk slower, and drop the accent. It might have been easier to accept the criticism had he spread it around a little, but that seemed unlikely. She could enter the scene wearing sunglasses and eating pizza and that was "Fine, Lois. Great work, babe."

"Are we vexed?" my mother would ask, pulling her station wagon into the parking lot.

"We are indeed," I answered. "And highly so."

"Let it go," she said. "Ten years from now I guarantee you won't remember any of these people. Time passes, you'll see." She frowned, studying her face in the rearview mirror. "Enough liquor, and people can forget anything. Don't let it get to you."

We were in dress rehearsal when the director approached Lois regarding a new production he hoped to stage that coming fall. It was to be a musical based on the lives of roving Gypsies. "And you," he said, "shall be my lusty bandit queen."

Lois couldn't sing; everyone knew that. Neither could she act or play the tambourine. "Yours is the heart of a Gypsy," he said, kneeling in the grass. "The vibrant soul of a nomad."

When I expressed an interest, he suggested I might enjoy working behind the scenes. He meant for me to hang lights or lug scenery, to become one of those guys with the low-riding pants, their tool belts burdened with heavy wrenches and thick rolls of gaffer tape. Anyone thinking I might be trusted with electrical wiring had to be a complete idiot, and that's what this man was. I looked at him clearly then, noticing the way his tights made a mockery of his slack calves and dumpy little basket. Vibrant soul of a nomad, indeed. If he were such a big stinking deal, what was he doing in Raleigh? His blow-dried hair, the cheap Cuban-heeled shoes, and rainbow-striped suspenders — it was all a sham. And acting? The man performed as if the audience were deaf. He shouted his lines, grinning like a jack-o'-lantern and flailing his arms as if his sleeves were on fire. His was a form of acting that never fails to embarrass me. Watching him was like opening the door to a singing telegram: you know it's supposed to be entertaining, but you can't get beyond the sad fact that this person actually thinks he's bringing some joy into your life.

I finally saw Hamlet for who he really was and recognized myself as the witless Yorick who had blindly followed along behind him.

My mother attended the opening-night performance. Following my leaden "Aye, my lord," I lay upon the grassy stage as Lois poured a false vial of poison into my ear. As I lay dying, I opened my eyes just a crack, catching sight of my mother stretched out on her hard, stone pew, fighting off the moths that, along with a few dozen seniors, had been attracted by the light.

"You were the best in the whole show," my mother said, stopping for frozen pizza on our way home. "I mean it, you walked onto that stage and all eyes went right to you."

It occurred to me then that my mother was a better actor than I could ever hope to be. Acting is different than posing or pretending. When done with precision, it bears a striking resemblance to lying. Stripped of the costumes and grand gestures, it presents itself as an unquestionable truth. I didn't envy my mother's skill, neither did I contradict her. That's how convincing she was. It seemed best, sitting beside her with a frozen pizza thawing on my lap, to simply sit back and learn.
```

---

## IC-1352: Dutch Treat

- Title: Dutch Treat
- Author (byline): Martha Kind De Silva
- Work: Best Men’s Stage Monologues of 1998
- Publisher: Smith & Kraus
- Publication date as stated: Sept 1999
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: EMMETT
- Teaser before the introduction: No
- Spoken words (computed): 1398
- Already set (do not supply): none

### Source block (context only)

```text
Author: Martha King De Silva
Book: Best Men’s Stage Monologues of 1998
ISSN: 1067134X
Publisher: Smith & Kraus
Date (Month/Year): Sept 1999
```

### Introduction (context only: never use it for content warnings)

```text
Chivalry is dead. It’s true, really, I mean, I can admit it. The only reason guys do nice things anymore is for the….uh…..physical benefits. Don’t get me wrong, I respect women. I respect them for their ability to control men. But man, am I fed up with all this give and no receive. A dinner here flowers and chocolates there- to apologize for food poisoning at dinner- it adds up. To hell with chivalry, I’m ready for a “Dutch Treat” by Martha Kind De Silva.
```

### Performance text (classify this)

```text
(Emmett is seated at a table in a restaurant with his date.)

EMMETT: Shall we get the check? (He looks to the waiter) When you're ready, we'll take the check. (He reaches over to grab the hand of his date.) Geez. Our six month anniversary, huh? It's hard to believe. Where does the time go, you know? It's funny. (He sips his drink.) When you get to that point, it's not just dates anymore. (He nods.) Right. It's a relationship. (He bites his lip.) I mean I'm not seeing anybody else and you're not seeing anybody else. (He sips his drink again.) And, frankly, I start thinking about what I'm getting out of the 'relationship' versus what I'm putting into it. Well, I don't mean it exactly that way, of course. God, that sounds horrible. (Pause.) But lately, Barbara, well, I've been thinking. And what I've been thinking is that I'm putting much, much more into this 'relationship' than what I'm getting out of it. And, well, frankly, if we're going to go on with the relationship, and that's something I want, well, I think some things need to change. Oh, no honey. It's nothing that can't be fixed. I've just been mulling over things that I might change, if I could change them and.

Okay. Here's what I mean. (He puts his briefcase on the table.) I came across all these receipts the other day and it hit me. Hang on a sec and you'll see what I'm talking about. (He pulls out a stack of papers.) I put together a spreadsheet of our relationship. Now before you get all. Just have a look. Here's where I started from. Column A is a list of the dates that we've gone on and what they have cost. Let's start with October 3rd, our first date. I thoroughly enjoyed that by the way. We went to the movies and then out for coffee afterward. It was $7.50 apiece for the movie; $5.50 for your Kahlua and Coffee; $4.75 for my Nutty Irishman. I have the receipts here if you want to check. Okay. The total which I paid for on that date was $25.25. That's not including the gas and depreciation on my car. Okay. The total which you paid on that date was O. All right, It's a first date. Kind of what I expected. And we had a nice time. Now if you look closely, you'll see that Column A-my column-continues to be full of numbers throughout the relationship. The dinner at L' Auberge Chez Francois, the weekend at the beach, the sailing trip in Annapolis. In fact, when you consider the total it's quite astounding. I had no idea I had spent so much. $2,242. Wow. Over six months. That comes out to... (He pulls out a calculator) over $373 per month. That's a lot of cash. All right. Let's go to your column-Column B. $24 in column B for the night that you had me over for dinner. If I'm underestimating the dinner, I'm happy to be corrected on this point. But as I recall it was a meatloaf, some potatoes, and a bottle of wine. $24 is probably about right. $24 over six months. That means you spent, well, $4 a month on me since the relationship began. [She begins to object.] Now just wait a minute. Let's have a look at column C. I've put checks in Column C on the number of times that there was sex associated with the date. Okay. This is very important, I think. Let's go back to the first date. $25.25. Movies and coffee. No sex. That's fine. I didn't expect it, really. It was a first date. [She gets angry] No, no, you're absolutely right. There was no discussion of sex at all. It was a kiss at your front door. Let's move down Column A a bit-my column-and see what happens. Date number two on October 11th, total for the date $47.61, no sex. Date number three on October 15th, total for the date $38.97, still no sex, what's this note I made, ah, some heavy petting, 3rd base. Ah-hah! Date number four. Dinner at Filomena's, $101.33. Sex. All right. But here's the point. I spent $213 .16 before we even had sex once. And, well, I think that's, well, that's not insignificant to me. Now let's compare Column C with Column A and I think you'll see what I'm getting at. With the exception of the meatloaf on December 2nd, Column A-my column-is completely full. But Column C is not so full. I know. We don't have to have sex every time we have a date. On January 3rd you lost your job and were upset, and of course I didn't expect you to have sex. February 19th is another case. It was the weekend we visited your parents. We talked about it and that counts for something, but we didn't actually do it because you felt uncomfortable having sex in your parents' house. Now I think I could have found a way to sneak into your bedroom to have sex with you quietly without your parents ever knowing but I didn't. I respected your wishes. There are a number of occasions here, however, when it seems as though we could have had sex and we didn't and we didn't because you didn't want to. What complicates this even more is Column D. Column D relates directly to Column C. And it's more or less my evaluation of, well, how good the sex was. Would you please sit down a minute and listen? Let's go back to date number four. Dinner at Filomena's. The dinner that I paid for that cost $101.33. A great dinner. And it was the first time we had sex. But, truth be told, the sex was not outstanding. And I think you'd agree with me on this. You had a little too much to drink, I think, and on a scale of one to five, with five being out of this world, it got a two. A sex score of two for a dinner costing $101.33 at Filomena's. All right. So, here's the deal. I am perfectly happy for Column A-my column-to continue as before. And I'm perfectly happy as well for Column B-your column-to continue as before. If that's the case, however, we have to talk about substantive, meaningful changes to Column C. And we've got to take a long look at Column D. Lots of twos and threes in Column D and frankly, I'd like for that to change as well. I don't think it's too much to ask for a couple fours and maybe a five once in a while. Now I could get ridiculous with this thing and add another column-Column E. Opportunity costs for me. Women that I could be having sex with but am not because I'm dating you. But that would be absurd. I know that. And, if you would let me finish, please don't interrupt me Barbara, of course, What I also haven't included on this spreadsheet are the-uh, the intangibles. The non-quantifiabies. The sort of psychic rewards to the relationship. And there are some. It's great not having to worry about what to do on a Friday night. You're a good listener. And when people ask me If I have a girlfriend, well, it's pretty terrific to say that, yes, I, Emmett Jones, have a girlfriend. But do those psychic rewards equal $2,2427 I don't think so. The point is not to point fingers at what's wrong with the relationship and who's responsible. Though I think the evidence shows, that you are probably more responsible than I. The point IS. [She interrupts.] Sure we can talk about Column B, but actually, Barbara, I'm more concerned with Column-What do you mean your expenses? (He indulges her) Like what? (He listens.) Your prescription for? Ortho-what? I don't know what that is. [She shouts the answer} Oh, that. Oh. (He is embarrassed; under his breath.) I agree. I don't want to take any chances either. Better safe than. (He speaks sotto voce.) How often do you have to get that filled? And how much does it cost? (He yells.) FOR THOSE TINY PILLS? [She says something else.} $100 for waxing. Waxing? Oh, they were very smooth. Yes, of course. It's just that. (Meekly) You don't think you could have used a razor for that? Okay, okay. A $200 bill from Victoria's Secret? For that flimsy black thing? The one with the? No, I just meant. . . What else? All right. $60. A French manicure. (He sighs.) $148. Cocktail dress at Ann Taylor. $37. In quarters. Washing your sheets.
```

---

## IC-1353: Elvis of Nazareth

- Title: Elvis of Nazareth
- Author (byline): Jay Huling
- Work: The Best American Short Plays 2007-2008
- Publisher: Applause Books
- Publication date as stated: July 2009
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ELVIS, MARION, MOSES, SOLOMON, CENTURION, JESUS
- Teaser before the introduction: No
- Spoken words (computed): 2579
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jay Huling
Book: The Best American Short Plays 2007-2008
ISBN: 978-1557837509
Publisher: Applause Books
Date (Month/Year): July 2009
```

### Introduction (context only: never use it for content warnings)

```text
The yet-to-be-discovered Elvis Presley has an inexplicable foreknowledge of his future life events. As he waits to make a personal recording for his mama's birthday at Sun Record's famed Memphis Recording Studio, he ponders the meaning of his life. And he's torn between making the record or traveling down another road. -- Whether it’s “hunka hunk burning love” or a burning bush. To his rescue come historic figures from the Bible -- Moses, King Solomon, a Roman centurion, and Jesus himself. Elvis of Nazareth by Jay Huling.
```

### Performance text (classify this)

```text
[THE YOUNG ELVIS about as nervous as a man can get, is seated on a long couch in the receptionist area. A sign above his head reads: "Memphis Recording Studio. Make Your Own Personal Records." He fidgets with his gum]

ELVIS: I'm gonna record a song for my mama. Kind of a present.

MARION: That's nice. [She tries to continue her work, but Elvis starts fidgeting again. She stares him down.]

ELVIS: Sorry ... Mr. Phillips is gonna discover me and not give you any of the credit.

MARION: I beg your pardon?

ELVIS: They're gonna call me the King.

MARION: Look, I want credit where credit is due. What am I not getting credit for?

ELVIS: I'm gonna record a song for my mama. Kind of a present. You're gonna discover me; Mr. Phillips is gonna get the credit, and I'm gonna go on to be the king of roll and rock.

MARION: Roll and rock?

ELVIS: It's a little gospel and rhythm and blues thing I put together.

MARION: Roll and rock doesn't quite "roll" off the tongue. Why don't you call it rock and roll? [A buzzer sounds at the door. Marion presses a button on the intercom system at her desk.] Come in! [Moses, who's come directly from Mount Sinai, circa 1225, enters, staff in hand, and approaches Marion’s desk.] May I help you?

MOSES: Let my people go!

MARION: Let who go?

MOSES: Art thou deaf? Am I not enunciating my consonants? Let my people go!

MARION: If you could just have a seat, Mr. Phillips will be with you in a moment.

MOSES: So that ye may know that the Lord-the God of Abraham, Isaac, and Jacob-hath sent me, this miraculous sign I now perform ... [Moses throws down his staff, and it lands near Marion’s desk with a thud. There is an awkward silence.]

MARION: That was supposed to turn into a snake, wasn't it?

MOSES: Uh-huh.

MARION: Do you need a moment?

MOSES: 'Preciate it. [He takes up his staff and ponders over it, perplexed as to why it didn't work.]

ELVIS: You okay?

MOSES: I was told-cast down thy rod and it will become a serpent! Did you see me cast down my rod?

ELVIS: Yes.

MOSES: Did it become a serpent?

ELVIS: No. Pleasure to meet you. My name's Elvis.

MOSES: I am Moses, discovered by Pharaoh's daughter hidden in a basket among the reeds near the river's bank. I received my call from the great bush which burned-yet was not consumed. I have come to lead my people out from bondage.

ELVIS: I'm gonna record a song for my mama. Kind of a present.

MOSES: Honoring thy father and mother. That's good. I should write that down.

ELVIS: They're gonna put me on The Ed Sullivan Show and shoot me from the waist up. Won't be able to see me wiggle.

MOSES: Thou wiggles? Are you taking anything for that?

ELVIS: I do it on purpose. It's how I express the song.

MOSES: I always wanted to be a singer. Never worked out. The material I was given! [Quoting.] "The horse and his rider hath he thrown into the sea." [Then.] What can you do with that?

ELVIS: I never knew you wanted to be a singer. But your life's purpose is so extraordinary.

MOSES: I wandered in the desert for forty years. I was willing to stop and ask for directions-but no!

ELVIS: I've always wished for a higher calling.

MOSES: It ain't what it's cracked up to be. Trust me, kid, stick to singing and wiggling.

ELVIS: You don't understand. Somewhere deep inside me there's an empty space. What's it gonna take to fill that up? I gotta find something. I'm not sure gyratin' like a jackhammer is it.

MOSES: Thou must choose. The pleasures of sin for a season, or an eternity of never getting past second base.

ELVIS: But what is that compared to a life making disciples for the Kingdom?

MOSES: My son, I gotta do what I gotta do. You don't. Thou understandeth? Think about it. Excuse me. [Crossing to Marion.] Let me let you in on a little secret.

MOSES: Frogs. Big green juicy amphibians. On your bed, down your drawers, in your chicken potpie. Frogs the size of baseball mitts. Everywhere! Unless thou hearken unto me.

MARION: And you're telling me this because ... ?

MOSES: Because thus saith the Lord-LET MY PEOPLE GO!-that they may serve me.

MARION: Mr. Phillips is the only one who can approve such a request. [Moses returns to his seat.]

ELVIS: You okay?

MOSES: To tell you the truth, I knew it wouldn't work. Can't do something cool like make fire rain down from heaven. Gotta make locusts swarm! Ever seen a swarm of locusts? Looks like a flying blob of pork and beans coming smack at you.

ELVIS: [To Marion] I don't think I can go through with this.

MARION: You're not about to chicken out, are you? Mr. Phillips will be with you any moment. Your future is waiting.

ELVIS: You don't know what I know. They're gonna have me singing to a dog, man. Then I get drafted. And then come the Beatles.

MARION: The who?

ELVIS: No, not the Who, the Beatles.

MARION: Beetles and locusts. Why don't we just let the people go?

ELVIS: No-they're four lads from Liverpool. Lots of mediocre stuff that's hailed as genius.

MARION: Will I get any credit for them?

ELVIS: I should just go home. [The door buzzer sounds again.]

MARION: Come in! [The door opens and King Solomon enters, in all his splendor. He approaches Marion] May I help you?

SOLOMON: Behold, thou art fair, my beloved, yea, pleasant: also our bed is green.

MARION: Come again?

SOLOMON: Thy two breasts are like two young roes that are twins, which feed among the lilies. Thou art all fair, my love; there is no spot in thee. MARlON That's really very sweet of you. But not very office appropriate. If you'll just have a seat, Mr. Phillips will be with you as soon as possible.

SOLOMON: For you, I will be a young stag upon the mountains of spices. [Solomon turns and sits next to Elvis] Gets 'em every time.

ELVIS: That was some smooth talking. My name's Elvis. It's a pleasure to meet you.

SOLOMON: I am Solomon, the third and last king of united Israel. The son of David, son of Jesse.

ELVIS: I had a twin brother named Jesse.

SOLOMON: I had some seven hundred wives and three hundred concubines.

ELVIS: I'm gonna earn more than a hundred and fifty gold records.

SOLOMON: Oh, yeah, well, I wrote three thousand proverbs.

ELVIS: I'm gonna sell more than a billion records worldwide.

SOLOMON: I have written more than one thousand songs. Including Song of Solomon-the greatest love song of all.

ELVIS: Did any of them go to number one?

SOLOMON: Art thou challenging me?

ELVIS: I just asked a question.

SOLOMON: [takes some sheet music out of his pocket and hands it to Elvis.) Hast thou anything as artful and lovely as this-?

ELVIS: [Reading.) "Except the Lord build the house, They labour in vain that build it: Except the Lord keep the city, The watchman waketh but in vain." [Elvis pulls a piece of paper from his pocket and hands it to Solomon.)

ELVIS: Try this on for size. From one of my movies.

SOLOMON: [Reading.) "I feel it in my leg, I feel it in my shoe, Tell me pretty baby, If you think you feel it too." [Then.] How profound. [Handing Elvis more lyrics.] But surely you are no match for me.

ELVIS: [Reading.) "It is vain for you to rise up early, To sit up late, To eat the bread of sorrows: For so he giveth his beloved sleep." [Then.] Well played. [Handing lyrics to Solomon.] But, as well as this-?

SOLOMON: [Reading.] "Some people like to rock, Some people like to roll, But movin' and a-groovin', Gonna satisfy my soul." [Then.] Satisfaction of soul? Intriguing. Thou art a worthy adversary. Wilt thou teach me to be artful in song as thou?

ELVIS: Me? Teach you? You have written some of the most beautiful verses of the holy Scriptures.

SOLOMON: But I want something different. I want a pop song!

ELVIS: And I want to be wise like you.

SOLOMON: Look, if you're talking about that cutting-the-baby-in-half thing-I was bluffing. I can't believe they fell for that baloney!

ELVIS: But your life as a man of God is so important.

SOLOMON: Ever heard of a King Solomon impersonator? Huh? No one's ever won a karaoke contest doing me.

ELVIS: I'm just not so sure it's right for me anymore.

SOLOMON: Thou fool. The only thing that is right is to fear God and keep his commandments. Now teach me to rock my fanny off. [Elvis stands up, begins to demonstrate]

ELVIS: You kinda got to let the rhythm ooze out of you.

SOLOMON: Showest thou me this ooze.

ELVIS: [Shaking his leg in rhythm.] This is ooze. With a beat. Four-four time. [Snapping his fingers.] Some people snap their fingers. [Tapping his toe.] Some people tap their toes. [Swaying back and forth.] And some people sway back and forth. I kinda put 'em all together, I guess. That's how the blues is born.

SOLOMON: [Pleased.] A time to be born. Yes.

ELVIS: Then you just rock till you drop.

SOLOMON: [Writing something down.] A time to be rocked. And a time to be dropped. I like this. It's almost like there's a time for every season under Heaven. Cease! A handful of quietness, please. [Crossing to a chair on the other side of the room.] I'm on a roll! And I'm not going to give you any of the credit. [Solomon begins writing furiously.] [The door buzzer sounds again. ]

MARION: Come in! [The door opens and a Roman Centurion enters with his prisoner; Jesus of Nazareth.] May I help you?

CENTURION: Your Excellency, this man claims to be the Christ, the king of the Jews!

MARION: [To Elvis.] I thought you said you were the King.

ELVIS: No, I'm the king of roll and rock.

CENTURION: The people want him crucified.

MARION: His singing can't be that bad.

CENTURION: Not him! [Pushing Jesus forward.] Him!

MARION: [To Jesus.] Oh. I'm sorry, what was your name? [JESUS is silent.]

CENTURION: He is called Jesus of Nazareth.

MARION: Well, have a seat. Mr. Phillips will be with you as soon as possible.

CENTURION: I beseech you, say the word to Lord Phillips. For I also am a man set under authority, having under me soldiers, and I say unto one, Go, and he goeth; and to another, Come, and he cometh.

MARION: And I say unto you, siteth.

ELVIS: [to Centurion] My name's Elvis. Pleasure to meet you. This here is Moses; that's Marion- And that's Solomon, son of David. I didn't quite catch your name, sir,

CENTURION: I really have no desire to make nice with you people.

ELVIS: [I'm gonna record a song for my mama. Kind of a present. Mr. Phillips says if he can find a white man with the Negro sound and feel, he could make a billion dollars.

CENTURION: Pontius Pilate says the same thing-the nerve! Woman, when will Lord Phillips prepare himself to meet us?

MARION: First of all, I'm not your woman. Second, I wouldn't be your woman if you were the last of the Mohicans. And thirdly- the one with the jumpin' beans in his jeans was here before you.

ELVIS: Well, that's all right, ma'am. [To Jesus.] Just doesn't seem proper that I come before you.

JESUS: Suffer it to be so for now.

CENTURION: What's wrong with you? Sideburns here says we can go first. The boy's letting us cut in line. Don't you know that I have the power to crucify you!

JESUS: Thou couldest have no power at all against me, except it were given thee from above.

CENTURION: [Sitting down.] My bad.

ELVIS: Are you really Jesus of Nazareth, the Christ, the king of the Jews?

JESUS: I am. [Elvis is awestruck.]

MOSES: [To Jesus] Jesus Christ. You've always been such a mystery to me. Just exactly what does the "H." stand for?

MARION: Would any of you care for anything to drink?

JESUS: If any man thirst, let him come unto me, and drink.

CENTURION: What are you-running a concession?

ELVIS: You're talking about living water, aren't you?

JESUS: I am the bread of life.

MOSES: You guys are making me hungry.

CENTURION: [To Elvis.] Kid, can I have a word with you? No fraternizing with the accused on my watch, kapeech? This man maketh himself a king, the Son of God.

ELVIS: But he is the Son of God.

CENTURION: [Beat.] Get outta here. He is a friend with publicans, tax collectors, and sinners.

ELVIS: That's because they are the ones who need him.

CENTURION: Thou hast proof?

ELVIS: He fed a whole crowd with only five loaves of Wonder bread. He healed the sick, made the blind see, raised the dead.

CENTURION: I thought he was just some freaky long-haired weirdo.

ELVIS: Hardly. [They return to their seats near Jesus]

CENTURION: Dude, that crown of thorns thing-sorry.

JESUS: Man, thy sins are forgiven thee.

CENTURION: You're gonna forgive my sins? Lordy, lordy, truly, this man is the Son of God. [Solomon stands, excited, clutching his latest manuscript.]

SOLOMON: Hearken unto me! I hath made me a great work! I gave my heart to know wisdom, and I hath found it!

ELVIS: Found what?

SOLOMON: The answer! The answer, my friend. It was blowing in the wind!

MOSES: Oh, if only I had lyrics like that!

ELVIS: Hang loose, man. Let's hear the words of the preacher.

SOLOMON: [Reading.] "To every thing there is a season, and a time to every purpose under the heaven. A time to be born, and a time to die. A time to plant, and a time to pluck up that which is planted. A time to kill, and a time to heal; a time to break down, and a time to build up. A time to weep, and a time to laugh; a time to mourn, and a time to dance. A time to cast away stones, and a time to gather stones together [Then, to Elvis.] How do you like them apples?

ELVIS: Now, that's a pop song!

SOLOMON: You really think so?

ELVIS: I know so. The Byrds will take it to number one.

MOSES: Frogs, flies, pestilence, beetles-now birds!-is there no end!? [they are inter-rupted by the buzzer on Marion’s phone. She picks up the receiver.] Yes, Mr. Phillips. Yes, I'll send him in right away. [Then.] Mr. Phillips will see you now.

ELVIS: No! Lord, I want to follow you wherever you go.

MARION: Mr. Phillips is waiting. Your whole future is waiting.

ELVIS: [To Jesus.] What should I do?

JESUS: Peace be unto you. As my Father hath sent me, even so send I you.

ELVIS: But you're sending me to do what? What is my purpose? Solomon, I need wisdom.

SOLOMON: Rejoice, 0 young man, in thy youth; and walk in the ways of thine heart.

ELVIS: Mo?

MOSES: I have set before you life and death, blessing and cursing: therefore choose life.

ELVIS: I guess "Love thy neighbor" isn't too far off from "Don't Be Cruel." [Elvis takes his guitar, straps it on, and strolls toward center stage. He bows his head for" a moment, then looks back at Jesus.] [Elvis strums the intra and sings the song "Dear Jesus" (Words and music by Jay Huling.)]

ELVIS: Dear Jesus, I don't understand, Why did you have to go away? You were a friend to hoodlums, harlots, and thieves, Sinners just like me. To the poor and the meek, The humble and weak, You opened up your loving arms. You gave a damn for the damned; Every woman and man, Sinners just like me. [CHORUS]

When all the finger-pointers were pointing at you, You said forgive-they know not what they do. Love your enemies, And learn to turn the cheek; Give and it will be given you.
```

---

## IC-1354: Encyclopedia Brown and the Case of the Barefoot Thieves

- Title: Encyclopedia Brown and the Case of the Barefoot Thieves
- Author (byline): Donald J. Sobol
- Work: Encyclopedia Brown Takes the Case
- Publisher: Penguin
- Publication date as stated: 2008
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, TYRONE, ENCYCLOPEDIA, MR. BROWN
- Teaser before the introduction: Yes
- Spoken words (computed): 1121
- Already set (do not supply): none

### Source block (context only)

```text
Author: Donald J. Sobol
Book: Encyclopedia Brown Takes the Case
ISBN: 978-0142410851
Publisher: Penguin
Date (Month/Year): 2008
```

### Introduction (context only: never use it for content warnings)

```text
Encyclopedia Brown and the Case of the Barefoot Thieves by Donald J. Sobol
```

### Performance text (classify this)

```text
Police officers across America were asking the same question. Why did everyone who broke the law in Idaville get caught? Idaville looked like many seaside towns its size. It had delicatessens, three movie theatres, and four banks. It had churches, a synagogue, and lovely white beaches. And it had a certain Red Brick house on Rover Avenue. In the house lived Idaville’s secret weapon against law breakers—ten year old Encyclopedia Brown. Mr. Brown was the chief of the Idaville police force. He was proud of his men. But he was not too proud to get them help. Whenever Chief Brown came up against a case that no on the force could solve, he knew what to do. He went home and ate dinner. Before the meal was over, Encyclopedia had solved the case for him. Chief Brown wanted to tell the world about his only child—to announce over satellite television “my son is the greatest detective who ever shot a water pistol!” But what good would it do? Who would believe that the mastermind behind Idaville’s spotless police record was only a fifth-grader? Encyclopedia never let slip a work about the help he gave his father. He didn’t want to seem different from other boys his age. But there was nothing he could do about his nickname. Only his parents and teachers called him by his real name, Leroy. Everyone else called him Encyclopedia. An Encyclopedia is a book or set of books filled with facts from A to Z—just like Encyclopedia’s head. He had read more books that anyone in Idaville, and he never forgot what he read. All this knowledge gave him the ability to start his very own, Brown Detective Agency.

NARRATOR: Tyrone Taylor knew how to treat the fair sex. He was the only boy in Idaville who got up to give a girl his seat- even when they were the only two passengers on the bus. The other fifth grade boys called him Sir Galahad. Monday afternoon Tyrone came into the Brown Detective Agency. He looked sick as a horse.

TYRONE: (sadly) Don’t call me Sir Galahad . . . call me Sir Had-a-Gal.

ENCYCLOPEDIA: Who was it this time?

TYRONE: Betty Holden. Just when I figured I had a chance with her, what happens? She goes out with Stingy Stenson!

ENCYCLOPEDIA: Don’t worry. Stingy is so tight that if he blinks his eyes, his knuckles crack. When he dates a girl, the money flows like glue

TYRONE: That’s what I thought. But last night I saw them together in Mr. O’Hara’s drugstore. Stingy bought her the Idaville Special with three scoops of ice cream!

ENCYCLOPEDIA: Wow! That costs twenty cents extra!

TYRONE: I want to hire you. (slams a quarter on the gasoline can beside Encyclopedia). Find out where Stingy stole the money he’s spending.

ENCYCLOPEDIA: Just a minute. You can’t go around accusing him of stealing --

TYRONE: (snapping) What was he doing outside the Medical Building yesterday morning? It was Sunday. The building was closed. And you should have seen his crazy walk.

ENCYCLOPEDIA: (scratching his head) You better show me.

NARRATOR: The two boys biked to the Medical building. It was after five o’clock when they arrived. The doctors had all gone home. The parking lot was empty.

TYRONE: Sunday was a hot day. So I sat under that shade tree while I thought about Betty. Suddenly I saw Stingy and his big brother Pete. They were walking in the parking lot, one behind the other. Crazy!

ENCYCLOPEDIA: Crazy?

TYRONE: They walked as if they couldn’t keep their balance. Then they jumped into a red truck that had “Mac’s Service Station” written on the door. They drove away, zoom!

ENCYCLOPEDIA: Sit under the same tree. I’ll do what they did

NARRATOR: He went down to the parking lot, which was enclosed by a seven-foot stonewall. He walked across the blacktop surface till he could see Tyrone over the wall.

TYRONE: Stingy and Pete were farther back. I can see only your head above the wall. I saw them down to the waist. (Encyclopedia moved back a few steps.) Stop! That’s where they were

NARRATOR: Encyclopedia had halted on a long, narrow white line. Branching out on either side of it were short white lines to mark spaces for cars to park.

ENCYCLOPEDIA: Stingy and Pete were walking a narrow white line you can’t see from there! They were having fun keeping their balance

TYRONE: Fun, nothing. They were celebrating. They probably just robbed some doctor’s office.

NARRATOR: Tyrone refused to believe anything but the worst about Stingy. He made Encyclopedia promise to ask his father if the medical building had been robbed yesterday. At dinner, Encyclopedia put the question to his father.

MR. BROWN: Why yes, Officer Clancy handled the case. I learned about it this morning. Thieves took about two hundred dollars altogether from the petty-cash boxes in several offices.

ENCYCLOPEDIA: Isn’t the medical building locked on Sunday?

MR. BROWN: The front door lock was broken Saturday. A watchman was hired till it could be repaired today

ENCYCLOPEDIA: Where was the watchman during the robbery?

MR. BROWN: He was drinking at the water fountain when he glimpsed two pairs of bare feet disappearing us the stairs. He chased them. As he turned a corner, he was struck and knocked out. He awoke to see Mac’s red service truck leave the parking lot. The watchman telephoned Mac immediately. Sundays, the truck is driven by Pete Stetson. Sometimes he takes his younger brother, the one everyone calls Stingy, along on service calls. When they returned to the station, both boys had on shoes

ENCYCLOPEDIA: What were the Stetson boys doing at the parking lot?

MR. BROWN: Pete says he was looking for a key, which he thought he dropped Saturday after visiting Dr. Marshall. He did see the doctor. We checked on that. No doubt the thieves removed their shoes in order to walk more quietly. Pete and Stingy may have robbed the offices. But we can’t shake their alibi.

ENCYCLOPEDIA: You mean, you need a clue to prove they had their shoes off when they entered the building?

MR. BROWN: One clue will do, but we don’t even have one!

ENCYCLOPEDIA: (grinning) I have!

NARRATOR: Pete and Stingy had taken off their shoes and socks in the truck in order to walk quietly. They had entered and left the building by walking along the white stripes of the parking lot. As they left, Tyrone Taylor had sat down under the tree. The brothers did not see him. But he saw them, from the waist up, walking back to the truck. Encyclopedia realized the brothers had not walked along the sidewalk just for fun. It was a hot day, remember? The blacktop burned their feet. So they had walked along the white strip— which was cooler. Faced with proof revealed by Tyrone’s sharp eyes and Encyclopedia’s sharp brain, the Stetson brothers confessed. Thanks to Encyclopedia, the money was returned and Tyrone—I mean, Sir Galahad, got the girl.
```

---

## IC-1355: Episode 26

- Title: Episode 26
- Author (byline): Howard Korder
- Work: Not specified
- Publisher: Samuel French, Inc
- Publication date as stated: 1985
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 689
- Already set (do not supply): none

### Source block (context only)

```text
Author: Howard Korder
ISBN: 0573619905
Publisher: Samuel French, Inc
Date (Month/Year): 1985
```

### Introduction (context only: never use it for content warnings)

```text
Deco: Oh no we are going to crash!

Buzz: Deco you idiot!

Hillen: Oh Buzz, hold me tight! The heroic Buzz Gatecrasher, the brainy Doctor Deco Gatecrasher, and the lovely Hillen Dale travel beyond the orbit of their planet earth, and face more danger than they ever expected. Episode 26 by Howard Korder
```

### Performance text (classify this)

```text
SCENE 1

Hillen: Buzz! Behind you!

Zugdish: (Gasping for air, and after a couple long breaths he pulls out a breathing inhaler) You all follow me to Lord Vaknor's palace. Get a move on it.

SCENE 2

(Zugdish escorts Deco, Hillen, and Buzz into the castle)

Deco: Quit your shoving you hoodlum. Don't touch the temple?

Hillen: Buzz, I'm scared.

(Vaknor enters with right arm across his chest representing a slash)

Vaknor: Dr. Deco. The lovely Miss Dale. And the headstrong Gatecrasher. I finally have then chance to meet you, and now your world shall crumble beneath my fist.

Deco: But why destroy Earth?

Vaknor: Why not? Doctor Deco? I find you to be a man of excellence.

Deco: You're just saying that. You must say that to everyone.

Vaknor: No really. Doctor Deco, have you heard of the Jewel of the Black Hand? I captured you because you are the only one who can figure out how to use it.

Deco: I've heard it mentioned. It's supposed to make you extremely powerful and extremely evil blah, blah, blah?

Vaknor: Correct, you may begin your work immediately doctor. Zugdish, take doctor deco to my laboratory for him to begin his work, take the lovely Miss Dale to my chambers, and take out my favorite pink pajamas.

Zugdish: The ones with the footies?

Vaknor: (out to audience) Yes, the ones with the footies! Mr. Gatecrasher, I have a proposition for you.

Buzz: I don't help ugly people.

Vaknor: oooooothat was hurtful, and unnecessary. Let's cut to the cheese. (sniffs air a bit) If you help us figure out how to use the Jewel of the Black Hand, I will spare your life.

Buzz: I don't help crooks.

Vaknor: Your lossZugdish, take Mr. Gatecrasher to the dungeon and eat him.

Zugdish: Yes, Your Smelly One. (to Buzz) Get a move on it

(pushes Buzz, ties him up, and puts on a bib)

CUT TO SCENE 5

Zugdish: Chow time.

Buzz: You don't want to eat me.

Zugdish: Yes I do.

Buzz: No you don't. You only think you do, now, what do you really want?

Zugdish: Earth woman Hillen. She makes me feel funny inside.

Buzz: Really, well, I could set you up

Zugdish: Me really hungry, but ok. (Releases Buzz)

Buzz: Now what are you going to say to her as a pick up line?

Zugdish: I don't know. . . Get down on the floor.

Buzz: Noooo, say "Say, kewpie doll, how about you and me make a little heaven on earth?" (Zugdish does so)

Zugdish: Say, kewpie doll how about you and me make a little heaven on earth. Get down on the floor! (Buzz hits his head and knocks him out) (Zugdish moans, then birds fly over Zugdish, then Zugdish passes out)

Buzz: Have a nice nap, beetle-brain! (imitates Zugdish) Now you get down on the floor. Now to rescue Hillen!

SCENE 6

(Hillen is alone in a room eating candy)

Buzz: Hillen, you're alone (looks surprised)

Hillen: Oh, Buzz you've come to rescue me

Buzz: No offense Hillen, but I expected to find you being tortured or something. Instead I see you stuffing your face with bon-bons.

Hillen: It's just that Richard offered me them.

Buzz: Richard?

Hillen: Lord Vaknor and I are on a first name basis now. Oh Dickey, he's really a nice guy, once you get to know him, but I want to go home with you. Please rescue me Buzz

Buzz: Oh alright, how do you propose we escape?

Hillen: Well, Dr. Deco gave me these pills in case of an emergency. (Reads bottle) Warning may change you into primitive life form blah, blah . .

Keep out of reach of children. Well, we don't have any children yet. It says to take one capsule.

Buzz: Well, we don't have time for one capsule. Give me the bottle. (Turns whole bottle over his mouth and eats the pills.)

(Waits a moment for a reaction, then starts doing the 3 Amigos dance. First 5 counts he makes small swallowing noises. On 6th count he makes a huge cough noise.)

Hillen: Anything happening (Buzz starts having seizures, and then turns into jelly)

Hillen: (screams) You're a horrible looking lump of jelly! Let's get out of here.

(moans)

CUT TO SCENE 8

Vaknor: Doctor Deco, give me the Jewel.

Deco: No!

Vaknor: Fine. (pulls out a gun and shoots. Gun makes a cell phone ringing sound)

Hillen: Is that my cell phone?

Vaknor: That isn't your cell phone honey, that's my weapon of mass destruction.

(Sexually growls to her, and she sexually growls back)(Buzz enters)

Buzz: (makes jelly noise, and then coughs) Lord Vaknor!

Vaknor: Ah Buzz Gate Crasher, I finally have the power to crush you like a bug!

Buzz: You're not going to use that Jewel are you?

Vaknor: You bet I am!

Buzz: This should be interesting

Vaknor: (holds up jewel, and the jewel makes a noise) Oh no, the jewel doesn't give power

Buzz: That's right, it takes away life.

(Vaknor freezes in place w/the jewel making noises. He quickly dies)

Buzz: (opens his arms) Hillen, my love, you’re safe, at last. You can come over here now

Hillen: Actually, about that whole "love" thing I'm sort of seeing someone.

Buzz: (shocked) Seeing someone? Who?

Zugdish: (waving) Hey, (thumbs up) kewpie doll
```

---

## IC-1356: Escape from Camp Boring

- Title: Escape from Camp Boring
- Author (byline): Tom Mitchell
- Work: Not specified
- Publisher: Harper Collins Children's Books
- Publication date as stated: Jan 2022
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: MUM, WILL, FAULKNER, LILY, NOAH, ALEXA, ELLIE, ZED, BUS DRIVER
- Teaser before the introduction: Yes
- Spoken words (computed): 1409
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tom Mitchell
ISBN: 978-0008403508
Publisher: Harper Collins Children's Books
Date (Month/Year): Jan 2022
```

### Introduction (context only: never use it for content warnings)

```text
After Will is caught listening to music on his phone in class again, his mum has had enough. Will is sent to a ‘rewilding’ camp in the middle of the woods for kids addicted to tech . . . Disaster! The camp is a screen-free snooze-fest; so, Will and his three new friends, bound by a tech deficiency, plot to escape in the middle of the night.

Escape from Camp Boring by Tom Mitchell
```

### Performance text (classify this)

```text
(Will is jamming out to his favorite song, which we can’t hear because it’s playing through his earphones)

MUM: (Pg 11-13) (motioning to Will, she’s angry) Take your earphones out and explain yourself!

WILL: (taking out one earphone, whiny) Dr. Andrews doesn’t teach us . . . He does this evil stare!

MUM: We’re not talking about your teacher. We’re talking about you having your earphone in during a test and scoring 17%. Meaning either your bad at biology or really bad at cheating. Were you listening to music again, Will? Honestly? It’s not the music; it’s your phone addiction. (She holds out her hand and speaks in slow-motion) Give. Me. Your. Phone.

WILL: (gasps – to audience) Four words to strike terror into the heart of anyone under the age of 80! (to Mum) I’m so not addicted!

MUM: Will, I’m sending you to Lonesome Pine Rewild Your Child Camp. I suggest you Google it.

WILL: (keying a Google search in his phone)‘Rewilding’ sounded painful. Eating nuts and doing yoga, that kind of thing. (he finds it and reads aloud) (Pg 17) . . . a 4-night camp . . . 11 to 16- year-olds . . . tech addiction. (Pg 20) (to audience) [And] a video from the camp leader Lieutenant Marvin Faulkner.

(At Camp – Day 1 – A clearing in the woods – Lieutenant Marvin Faulkner is locking up all electronic devices in a safe. He and 2 young counselors are wearing some type of camp uniform with shorts that show too much leg – it is obvious Faulkner is ex-military)

FAULKNER: (Pg 30) (presenting to the group of campers) We don’t return here, to what I like to call the “safe space” until the graduation ceremony.

LILY: (Pg 27-28) (checking her clipboard - to Will) I’m Lily and you’re late to the induction ceremony.

WILL: (to audience) What if Lonesome Pine Rewild Your Child Camp ((Pg 23) the most boring camp that has ever existed in the history of camps) were a cult? Cults always end badly. I’ve read Wikipedia entries and can share links if you’re interested!

NOAH: (Pg 28) Lieutenant Faulkner, sir? (pointing to Will)

FAULKNER: (Pg 30-32) (to Will, motioning him forward) Who’s this? What’s your name?

WILL: Will. Will Walker.

FAULKNER: I hate latecomers! It’s rude. Do you know what I do to rude people, Walker?

WILL: (voice cracking) Kill them?

FAULKNER: I re-educate them. Give me your devices. On the double! (Will hands him the phone. Faulkner crouches to unlock the safe and puts his phone inside, then stands to address the campers) One final thing campers: don’t go wandering off. The woods are nightmarishly deep in every direction. Without a car it’s a dangerous trek to town. Nobody know what lives in the forest. Wolves, they say. Okay. Let’s get going. “Screen time is mean time!”

ALEXA: (following Faulkner, she her eyes vigorously, then nudging Will) ‘Screen time is mean time?’ What the frog?

WILL: (Pg 33-34) Are you okay?

ALEXA: (motioning to her red and puffy eyes) Oh, it’s nothing. I think I’m allergic to trees. (cursing) “Shitake mushrooms!” (in a canned recitation voice) My name is Alexa and I’m addicted to sending email complaints. I also have a problem with swearing. I’ve learned to say alternatives. “Fudge nuggets” “son of a monkey”

WILL: (Pg 165) Alexa, what will the weather be like tomorrow? (cracks himself up laughing)

ALEXA: (not amused) You know what you are? You’re a shazbot . . . A smogging smurfle!

FAULKNER: (Pg 42) (exposing his philosophy as he leads the campers) Addiction is a terrible thing. I know. I used to be over 280 pounds. You hear of Twinkies? They cost me my military career. Twinkies! I don’t want the same thing happening to you! (Pg 34) (motioning to his right) The bunkhouse. You’ve got 20 minutes. Unpack. Visit the bathroom, whatever. (Pg 41) [Then] Whittling!

ALEXA: Fudge nuggets!

ELLIE: (Pg 46) (raising her hand) There’s been a terrible mistake. I don’t want to whittle. My parents thought this was a tennis camp!

WILL: (to audience) She was blonde and looked like her parents owned at least one Range Rover

FAULKNER: (in a no-nonsense tone) Listen up, All of you. You’re homesick. I get it. You’ll all want to call home.

ZED: Zed isn’t homesick. Zed was wondering if we get to build treehouses. There was a picture on the website of kids building tree houses.

FAULKNER: (Pg 47) ‘Website’ is a banned word. And let me be very clear to anyone thinking they might use the camp phone. Nobody is using it. Period. I’m not having parents demanding refunds because I let you call your boyfriends. Again . . .

WILL: (Pg 49) The second day . . . and apart from Alexa and me, the two kids that stood out were Ellie and Zed. Zed kept to himself. He wasn’t silent though.

ZED: (yelling to anyone who will listen) Zed is thirsty. Zed is tired of trees.

WILL: At the river, we were told to make model boats and race them on the water. Fun in theory, but majorly sucked in reality. (rolls his eyes and begins gathering sticks)

LILY: (Reading instructions) You can use any of the material you find in the crates.

ZED: Zed sees no crates.

NOAH: (panicked for a moment, then he improvises) Just use whatever you find. I don’t know – it’s like a scavenging challenge?

LILY: (Pg 74) [How about] an optional activity called ‘pinecone yoga’? It’s yoga but with a pinecone balanced on part of your body!

ALEXA: (Pg 50) (hissing another non-swearing swear) William Shatner! Can you believe our parents paid for this experience. Wait until I get on Tripadvisor!

ELLIE: (Pg 79) What will they have us doing tomorrow? Squashing bugs on a piece of paper and calling it art? Making a cowboy hat out of acorns? No way. Let’s get out of here! *****Day 2 – Our Escape*****

WILL: (Pg 122) The fantasy of a solo escape was long deleted. (Pg 78) [There were] 4 of us. Four ((Pg 71) Zed gives a secret thumbs up and a wink) (Pg 53-54) The moon reflected silver light across the campsite. The lack of sound, the lack of movement, gave the scene horror-film feels. But it didn’t matter; it wasn’t like I was going to get attacked by a hungry tree demon. OR SO I THOUGHT. (I wasn’t attacked by a hungry tree demon) NOT THAT NIGHT. (Sorry. I’m joking) OR AM I? The only thing the plan lacked was a soundtrack. (soundtrack music, like Mission Impossible) (Pg 80) Maybe, just maybe I was pleased that I wasn’t escaping on my own. (wolf howl) (Pg 88-89) (to friends) We just need to follow the river and we’ll get to town before sunrise. Easy.

ELLIE: (Pg 94-95) Lead the way. It’s not like we’ve brought a . . . a . . . the thing that points north -- a weathervane!

WILL: (Pg 100) (whispering) Did you hear that? (to audience) Every one of my muscles tensed. Literally every one. Name a muscle. It tensed. (to friends) It’s probably a (Pg 102) squirrel. (to audience) The last thing I wanted to be dealing with was a supernatural squirrel monster with magic powers like being able to throw acorns with super-strength, for instance. (Pg 103-104) Where’d Ellie go? (in a loud whisper) Elllllllll-ieeeeee!!! (beat, then to audience) Ellie was gone.

ALEXA: (Pg 106) Flipping sherbets! Son of a frog!

ELLIE: Help!

WILL: Ellie? She was definitely calling from the other side of the path.

ELLIE: Above you! There are flappy things, people! (Ellie falls from the tree)

WILL: BATS! (the friends take cover from a flurry of bats flying out of the forest)

ZED: (Pg 176) You gotta be careful with bats.

ALEXA: (Pg 106) Oh, Ellie. You’re not hurt, are you? Are you hurt?

WILL: Why were you even up there?

ELLIE: I was on lookout. For the town lights. (shudders) (Pg 115) That bat. Straight in the face. It was so gross!

ALEXA: (Pg 143) Let’s all sneak back together. It’s early. Everyone will still be sleeping. We’ll hide in our bunks everyone will never know what’s happened! It’ll just be our thing. And nobody gets in any trouble! Right, Will?

WILL: (Pg 111) Look! (pointing at the sky) Light! We need to get going! (to audience) The morning was coming.

ELLIE: (Pg 146) We need to get back before breakfast. They take the breakfast register at eight!

WILL: (Pg 131-133) (to audience) And so we kept in a straight line, one after the other: Me, Ellie, Zed, Alexa (#WEZA) I don’t think I’d ever been at the head of a line before. Or the head of anything. But I led the group. It wasn’t long before we passed the final tree. There’d been no warning of the forest ending – it just did. (to friends) Wait! (pointing) What’s that? (to audience) There was a bus! (Pg 147) The very vehicle that would be our ride back to camp, our white stallion. (they race to the bus)

ALEXA: (Pg 140) (banging her palms against the bus door) Wait! (the doors opened)

BUS DRIVER: I don’t have time for this.

WILL: (Pg 139) (to audience) It’s worth taking a moment to consider what we looked like: dishevelled, ripped jackets, and huddled round Alexa as she tried her best to explain to the driver why she really, honestly, should let us on.

ALEXA: (Pg 140) But maybe your supervisor will be interested in your abandonment of four lost, cold, innocent children.

BUS DRIVER: You don’t know my supervisor. He couldn’t care less, to be fair. Horrible man.

ALEXA: But I know the customer services email address. It’s printed on the side of the bus. And I know you’ve a responsibility to ensure our safety.

WILL: (Pg 141) (to audience) Five minutes later we were on board, the bus was moving, and we were all giving Alexa silent, subtle high-fives, mouthing ‘wow’, our eyes wide with amazement. (beat) (Pg 156) [But] we didn’t make the breakfast register. (Pg 158) It was a few minutes past eight. But we were here, and that was a miracle in itself. (Pg 159) We stood under the Lonesome Pine signpost. Its stern wood and smart lettering gave the impression of an organized camp. You can make anything seem professional with the correct font.

ELLIE: What now?

WILL: (Pg 160) Exercise! (to audience) Because I had a plan. All wasn’t lost yet. It wasn’t over until the fat man rang home. (to friends) We find a clearing and we get caught exercising. We’ll say we didn’t know the time because we didn’t have phone. What about pinecone yoga? We could do that! (Pg 161-162) (to Ellie) Shout out instructions!

ELLIE: Bakasana! (they each put a pinecone on their head and assume a yoga position)

ZED: (downward facing dog) ALEXA: (crouching with one leg in the air) WILL: (warrior’s pose)

WILL: Ellie, really shout – we need the camp to hear!

ELLIE: Bakasana!

WILL: (to audience) It took three positions before Noah came crashing through the trees . . .

NOAH: What are you doing? Have you been eating the forest mushrooms?

WILL: (Pg 163) And so, for possibly the first time ever, a plan of mine actually worked out the way I intended. Faulkner was so impressed we’d got up early to do yoga, we didn’t even get in trouble for being late to breakfast. Especially when Ellie said that she was going to tell ALL her school friends how great the camp had been and also that her dad was a rich lawyer.
```

---

## IC-1357: The Explorers Club

- Title: The Explorers Club
- Author (byline): Nell Benjamin
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Oct 2014
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: LUCIUS, COPE, WALLING, ALL, PHYLLIDA, LUIGI, SLOANE, PERCY, HUMPHRIES
- Teaser before the introduction: Yes
- Spoken words (computed): 1403
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

## IC-1358: Fake Mustache

- Title: Fake Mustache
- Author (byline): Tom Angleberger
- Work: Not specified
- Publisher: Amulet Books
- Publication date as stated: July 2013
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: LENNY, CASPER, RED, SVEN, REPORTER, RECORDED VOICE, DIRECTOR DROPBAG, MAN, LADY, CROWD, GOVERNOR, REPORTER 2, STRANGE MAN, DR. HEIDELBERG
- Teaser before the introduction: Yes
- Spoken words (computed): 1667
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tom Angleberger
ISBN: 978-1419711633
Publisher: Amulet Books
Date (Month/Year): July 2013
```

### Introduction (context only: never use it for content warnings)

```text
And that’s when things started to turn out bad in a huge, earthshaking, TV-news-special-report kind of way. But don’t worry . . . a few days later, our hero -- mild-mannered 7th grader Lenny Flem saved the world!

Fake Mustache by Tom Angleberger
```

### Performance text (classify this)

```text
LENNY: (Pg 2-3) Don’t ever buy a fake mustache at Sven’s Fair Price Store in downtown Hairsprinkle. I recommend it if you want to buy fake teeth, fake gum, fake dog poop, or fake people poop. But the fake mustaches are just too good. Apparently, there are men in Belgium who grow their mustaches for a year, then cut them off and sell them to the Heidelberg Novelty Company. (beat) I didn’t buy one. My friend Casper Bengue bought one.

CASPER: (Pg 4-5) Look at this, Lenny. My nana Nookums gave me four hundred dollars! I’m going to buy a fake mustache. The Heidelberg Handlebar #7 - $129.00 at Sven’s. I’m going to use the rest to get a first-class man-about-town suit.

LENNY: (Pg 7) [So] the first place Casper wanted to go that fateful day was Chauncey’s Big & Small, Short & Tall

(Lenny and Casper enter the store)

RED: (Pg 8-9) Are you boys selling candy bars for your GottDangled school? No more candy bars! Get the Helchfitz out of here!

CASPER: (whispering) Don’t worry. When you’ve got four hundred dollars to spend, you get treated differently. (Casper fans out the cash and speaks with bravado) I’d like a man-about-town suit. And I’ve got cash!

RED: (Red pulls out a measuring tape and proceeds to measure Casper) (Pg 11) I’ve got just what you need, sir. The Statesman Deluxe. (He grabs a suit) It won’t even need tailoring.

(Casper dons the suit and preens in front of the mirror) A perfect fit. Just $249.99.

CASPER: Perfect. Even with tax, I’ll still have enough left to buy the Heidelberg Handlebar #7.

(the boys exit the store and head to Sven’s)

LENNY: (Pg 12) Casper did look a little bit more like a short man-about-town than a slightly tall nerdy seventh grader. (To Casper) (Pg 13) Why are you holding your hand over your face?

CASPER: (masking his upper lip with his hand) There are people who shouldn’t see me without the mustache. *****

LENNY: (Pg 16-19) (Lenny and Casper enter Sven’s) The manager [of Sven’s] turned out to be a very, very angry-looking lady.

SVEN: (text-messaging, she doesn’t even look up)

CASPER: (Clearing his throat and speaking in a fake adult voice) I’m interested in the Heidelberg Handlebar #7.

SVEN: (Looking Casper up and down, she tosses her cell phone and comes to attention) I beg your pardon, sir. (She unlocks a cabinet and punches a code to the alarm) WHOOSH! (the door to the case opens and she removes the mustache as if it were a priceless heirloom) One formality. The Heidelberg Novelty Company requires me to ask the purpose of your purchase.

CASPER: Our school is putting on a musical adaptation of The Hoboken Chicken Emergency, and I’ve been chosen to play the mayor.

LENNY: (aside to the audience) This was a complete and total lie.

SVEN: Impressive! Here, take a complimentary year’s supply of spirit gum. It will keep the mustache on your lip through thick and thin. (Casper attaches the mustache to his upper lip and the boys exit the shop)

CASPER: (Pg 20) (to Lenny, while shaking his hand and patting him on the shoulder) Good-bye, Lenny. Wherever fate leads us, remember that we have walked far in friendship. (Casper walks away, leaving Lenny with a perplexed look on his face) *****

LENNY: (Pg 26-27) The next morning on the Good Morning Hairsprinkle Show.

REPORTER: This is Giorgio ‘Jim’ McPunklett, reporting live from Hairsprinkle, where the first-ever billion-dollar bank robbery was carried out by a gang of strolling accordion players. The bank’s security cameras caught the robbery on film, and as you can see, the ringleader appears to be a short, well-dressed man-about-town sporting a spectacular handlebar mustache.

LENNY: (Pg 30) They closed school. The FBI was worried that the leader of the gang might be dangerous. He had instantly become the 2nd-most wanted criminal in the United States, behind that lady who stole the president’s underpants last year. (pantomime of a lady “pantsing” the president) SQUEAL! Could Casper really be a bank robber? (Pg 34) After supper, I convinced my dad to let me go to Casper’s house. (He was in his room, putting on the suit)

CASPER: (Pg 35-38) How do you like the pinstripes, Lenny?

LENNY: I couldn’t think of anything to say, because his bed was piled high with gold bricks and bundles of ten-thousand-dollar bills. (to Casper) Did you rob the Federal Gold Reserve? It’s all over the news!

CASPER: Huh, well, we don’t have a TV, so I didn’t see the news. Sorry, I don’t have more time to talk. I’ve got to get to (grasping for an acceptable location) School Skate Night down at the roller rink.

LENNY: The roller rink closed last year. Did you do it or not?!?

CASPER: Wish me luck! (he adjusts his mustache and exits) (Lenny dials 911 on his cell phone)

RECORDED VOICE: Hairsprinkle Dispatch. The FBI is searching for a short man with a handlebar mustache. Please rat them out at the tone. BEEP

LENNY: I know who the bank robber is. His name is Casper Bengue and he lives at 3414 Sprinkle Street. He’s got all this money and gold in his bedroom . . . *****

LENNY: (Pg 40-42) I worried about it all night. At 5 am I went downstairs and turned on Happy Weekend Hairsprinkle . . .

REPORTER: Hairsprinkle breathes more easily after a quiet night. No more banks have been robbed. We have FBI director Marcie Dropbag with us live from Hairsprinkle. You must be relieved, Director Dropbag.

DIRECTOR DROPBAG: Frustrated. We spent the evening following up on false tips. Can you believe one caller tried to turn in an actual seventh-grade student. The caller claimed he had a bedroom full of ‘money and gold.’ We checked it out and found a typical messy bedroom full of smelly clothes, but no gold or money.

REPORTER: Did the 7th grader even have a mustache, Director Dropbag?

DIRECTOR DROPBAG: Of course not.

LENNY: (Pg 43) Outrageous. What DID happen to all the money Casper had in his room? It was billions of dollars. Where could it have all gone?

REPORTER: In other big news, the Heidelberg Novelty Company has been purchased in a cash transaction for 2.4 billion dollars. The new owner is billionaire businessman Fako Mustacho.

LENNY: And they showed a picture of Casper wearing his mustache! The picture looked exactly like the one of the bank robber they were just talking about. And that name: Fako Mustacho? He was practically spelling it out for them!

REPORTER: (Pg 44) I’m sure we’ll be hearing a lot more from him in the coming days. The Heidelberg Novelty Company is the world’s largest manufacturer of voting machines, and the presidential election is just a few days away.

LENNY: (Pg 53) What exactly was Casper – aka the billion-dollar bank robber, aka Fako Mustacho doing? How did he get this power to make ordinary accordion players turn into his henchmen? Brainwashing? Some kind of zombie-mind-power magic? Whatever it was, that mustache must be the key! (Pg 63-64) I got on the trolley, and everybody had this weird hypnotized look.

MAN: Have you seen the Evil One?

LADY: If you do, you must capture him and take him to Fako Mustacho. He’s a desperate bank-robbing mastermind disguised as a boy named Lenny.

LENNY: (Pg 64) I couldn’t believe it! Casper had somehow convinced everybody that I was the bad guy! (Pg 71)

REPORTER: (Pg 66) Heidelberg CEO Fako Mustacho is on his way to address the governor and state lawmakers about the Lenny crisis.

*****

CASPER: (Pg 80) (waves the legislator off and take his place at the podium, he speaks in a deep voice) Greetings, my friends! (Pg 83-85) I know every piece of evidence points to Lenny Flem being guilty of the string of crimes that has [now] wiped out banks, companies and governments. Every reasonable person believes that Lenny Flem is guilty.

CROWD: (chanting as a hypnotized collective) Evil One . . Evil One . . Evil One . .

CASPER: But not I. In this great country no one is truly guilty until they have been convicted in a court of law. Now, the governor is a close friend of mine. However, she hasn’t been able to catch Lenny Flem. (to Governor) Would you mind resigning?

GOVERNOR: (in a hypnotized manger, she takes the microphone) I hereby resign as governor . .

CROWD: Quit hogging the mic! Let Fako talk!

LENNY: So, Fako was appointed governor by a unanimous vote. Now it wasn’t just my word against his; it would be my word against the governor’s! (Pg 111) Fake Mustacho seemed to have taken over the whole town. No, the whole state!

CROWD: CHEERING

LENNY: TRANSITION ADDED: [That’s when I knew I had to break into Governor Mustacho’s office] (Pg 107-108) I looked at a few of the papers on the desk: INAUGURATION PLANNING was written on one folder. (he leafs through the folder; an astonished look appears on his face) And then I understood. It wasn’t about his swearing in as governor, it was about his swearing in as the President of the United States of America! He bought the Heidelberg Novelty Company, but not for the mustaches – it was for the voting machines.

REPORTER: (echoing voice) (Pg 44) The Heidelberg Novelty Company is the world’s largest manufacturer of voting machines

LENNY: (Pg 108) Election Day was three days away. And somehow Fako Mustacho was going to get himself elected president! *****

REPORTER: (Pg 166-168) Let’s take a look at our electoral map. It shows that Fako Mustacho has received 100% of the vote so far.

REPORTER 2: Truly amazing. Just a few weeks ago no one had even heard of Fako Mustacho. We all thought that a Republican or a Democrat would win . . .

REPORTER: We were fools back then. We, the people, have seen the light.

CROWD: (Pg 171) FAKO FAKO FAKO FAKO ***** [a few days later] ******

CASPER: (Pg 171-173) (entering his office) Well, that’s that. I’m the next president of the USA!

LENNY: You stole their votes!

CASPER: (smirking) Look, it’s over. I won. All I have to do is say the word and the CIA ships you off to Antarctica with all the other wackos who are a danger to this fine country. But I’m going to give you another option . . . Admit that I’m the new president and I’ll let you walk out the door. I’ll make my speech and tell everyone that you’re not the Evil One, Lenny. No one will ever bother you again. (Lenny opens his mouth to say something but Casper cuts him off) I can’t tolerate treason or threats against our democratic process. If you say anything other than ‘OK, Mr. President,’ you’ll be silenced and taken away and that will be it.

LENNY: (with complete sarcasm) OK . . . Mr. President. *****

REPORTER: (Pg 185) And now let’s go live to Fako Mustacho’s victory speech . . . (Casper takes the stage in a grandiose manner waving and pumping his fist in victory)

STRANGE MAN: (Pg 56) (bursts in yelling in a European accent) Where is the Heidelberg Handlebar #7!

DR. HEIDELBERG: (echoing voice from the past) (Pg 101, 103) 72 years ago, my brother, Tito made the Heidelberg Handlebar #7. It was woven from the hairs of a very bad man who gave up his mustache unwillingly.

STRANGE MAN: (Pg 56) I am here to retrieve what belongs to me and only me! Even if it means spilling the blood of another! (He whips out a weapon)

DR. HEIDELBERG: (echoing voice from the past) (Pg 103-104) He was a professional assassin, famous in the European underworld for his record of 300 kills and his perfect mustache. He was betrayed by a woman and arrested. When he arrived at prison, they shaved his mustache.

[And now] the Heidelberg Handlebar #7 is too powerful, especially if it falls into the wrong hands. *****

LENNY: (Pg 186) Here’s what happened . . . I have a glimpse of Fako standing on the stage with his arms raised. (Casper and Lenny pantomimes the events while Lenny narrates) The French guy is squeezing the trigger . . . (Pg 188-189) and I am in motion . . . I land on the stage, grab the mustache, put it between my teeth and rip it in two. The mustache is dead! (Pg 191) And the platoon of Secret Service agents that rushed the stage found only two local Hairsprinkle schoolkids. No one saw what happened to Fako . . . and no one ever saw him again. (Pg 2) I saved the world and it all started with me and my friend Casper going to Sven’s Fair Price Store in downtown Hairsprinkle. (stage whisper) Don’t ever buy a fake mustache at Sven’s!
```

---

## IC-1359: Family 2.0

- Title: Family 2.0
- Author (byline): Walter Wykes
- Work: Ten 10-Minute Plays: Volume II
- Publisher: Black Box Press
- Publication date as stated: July 2008
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: HUSBAND, WIFE, SON, DAUGHTER, FIRST HUSBAND, FIRST HUSBAND/DOG
- Teaser before the introduction: No
- Spoken words (computed): 1150
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
How many times have we heard the cliche, “The grass is always greener on the other side?” While the overuse of this phrase has mostly dulled its impact, people who experience the “grass is greener syndrome” endure a significant struggle. They truly believe that there is always something better what they have. Whether it’s with relationships, careers, where they live, or their family, they always have one foot out the door.

Absurd? You have no idea! Meet Family 2.0 by Walter Wykes.
```

### Performance text (classify this)

```text
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

WIFE: Go play in your room, kids. Your father and I need some time alone.

DAUGHTER: Sure thing, Mom.

SON: See ya later, Dad. [Exit kids.]

WIFE: [Seductively.] Now where were we? [They kiss passionately. Enter FIRST HUSBAND]

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

## IC-1360: Fat Boy vs the Cheerleaders

- Title: Fat Boy vs the Cheerleaders
- Author (byline): Geoff Herbach
- Work: Not specified
- Publisher: Sourcebooks Fire
- Publication date as stated: May 2014
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CRIME REPORTER, GABE, JUSTIN, DEEVERS, MR. DEEVERS, CHEERLEADERS, SHAVER, GABE’S ATTORNEY, KAILEY, OFF STAGE VOICE, OFFICER MCCOY, REPORTER
- Teaser before the introduction: Yes
- Spoken words (computed): 1569
- Already set (do not supply): none

### Source block (context only)

```text
Author: Geoff Herbach
ISBN: 978-1402291418
Publisher: Sourcebooks Fire
Date (Month/Year): May 2014
```

### Introduction (context only: never use it for content warnings)

```text
(sound effect from the opening of Law and Order, Special Victims Unit; “chuk, chuk”) In the juvenile justice system soda-based crimes are considered especially heinous. At Minnekota Lake High School, the purchasers of these sodas are members of a rhythmically challenged squad known as the Marching Band. Their leader? Gabriel Johnson (aka Chunk). This is his story. (“chuk, chuk”)

Fat Boy vs the Cheerleaders by Geoff Herbach
```

### Performance text (classify this)

```text
CRIME REPORTER: (Pg v) Shortly before midnight on June 15th Gabriel Johnson, a sixteen-year-old from Minnekota, MN was apprehended outside Cub Foods. Johnson possessed $17.75 in small bills and change, which he confirmed had been removed from the vending machine at Minnekota Lake High School. Police suggested the alleged robbery was related to a larger conflict involving assault, vandalism, and defamation of character that has come to be known as the Spunk River War.

GABE: (Pg 1) (speaking to his attorney; very nervous) Ripping off the pop machine last night wasn’t meant to be funny. It was my duty to all the geeks, burners and oddballs in this school because that machine sucks. Why are you laughing? I robbed the machine all my myself. It was eighteen dollars, but I lost a quarter when Officer McCoy roughed me up. Look at my chin! I have scrapes all over my stomach and knees too. (Pg 2) Stupid Pop machine. Stupid pop.

(Pg 7) Hey. Shouldn’t we be talking about how . . . how you're going to keep me from going to jail or something? I’m a little nervous about my crime. (listens for a moment) The whole story, huh? Okay. You asked for it . . .

GABE: (Pg 4-5) Here's the scoop, sir: Purchasers a pop at the Minnekota Lake High School are fat a**es, trailer park kids, addicted gamers and chicks who eat cigarettes for breakfast. Dozens of these kids went back for seconds. Some for thirds (me for instance). Two cheerleaders purchased from the machine, but they both bought diet. That diet stuff will kill you but not make you fat.

JUSTIN: (to Gabe) You drink a lot of pop, Chunk! I’m just sayin’. (indicating Gabe’s size)

GABE: Yeah. Really. I drank a ton of Code Red Mountain Dew every day – 4, 5 bottles – and the only pants that fit me were stretchy pants – elastic waistband, sir. (demonstrates the stretchiness of his waistband) Kids call me fat, butter ball, Eight-Butt Johnson. (Pg 39) Justin was the first person to call me Chunk. He said I looked like this fat kid in an 80s movie. (Pg 5) I knew pop was part of my issue. But see, I also thought it was part of my success. All the vending machine money went to fund the band! I love band! I love band so much . . . I'm a trombone player. That’s one awesome instrument, right? (mimes playing the trombone and marching with pizzazz) I was winning by buying all that pop!

(Pg 13) Okay. So Wednesday morning -- totally evil surprise. Parched, ready for my first Dew of the day, I strolled into the cafeteria and discovered that all pops had been jacked from a buck fifty to $2.25! No longer did I have the proper coinage for three Code Reds. I only had enough for 2. I couldn’t make it through a day on 2 Code Reds! Oh, no, no –

(Pg 17-18) After school Justin and I walked into the principal's office. Without my minimum 3 Code Reds, I was totally wiped and a bit confused and my muscles felt like bags of sand. Mr. Deevers wasn’t happy to see us. Maybe because he’s a central figure in a scheme to defraud students out of their hard-earned dollars?

DEEVERS: What do you guys want?

GABE: Justice!

JUSTIN: (raising his eyebrows, laughing) We're just curious about the sudden steep price increase on the pop machine.

MR. DEEVERS: Come on. Times are tough for education. We’re depending on those proceeds to fund a lot.

JUSTIN: Fund more than just the band?

DEEVERS: (fake smile) Well, ha, ha, there will be an announcement tomorrow. Ha-ha.

GABE: (squinting and possibly hopped up on Code Red) Ha-ha? Ha-ha? Are you taking my money? Are you running away to Mexico? (shouting) I don’t have enough money to live! (beat while he gains composure)

(Pg 19) Why didn’t I say something about poor kids who don’t eat breakfast at all, who need caffeine even to have a fighting chance? Instead, I accused the principal of running away to Mexico. I was an idiot.

(Pg 20-21) The next day I tried to hold it together by overdosing on the Dew. I robbed Grandpa of 20 bucks. Plucked four 5-dollar bills from his wallet while he fried eggs. Part of the reason my grandpa lives with us is because he's poor. He invested all his money in this power drink called Tiger Lightning. It supposedly had the essence of tiger testicles in it. But the secret ingredient was actually a steroid. Tiger Lightning was sued by the government. Grandpa lost just about everything.

I poured Code Red down my throat all morning. At lunch, I was sweating, probably on the edge of overdosing. I could barely talk. (Pg 23) (bitterly, but with tremors) Turns out that money wasn't even going to my band!

Justin, me and a few others sat at a table in the cafeteria just as Kailey Kaus and the rest of the cheerleaders streamed into the room to put up posters all over.

CHEERLEADERS: [insert your favorite cheer here]

GABE: (Pg 25-26) (reading the poster) YES, THE RUMORS ARE TRUE! THANK YOU FOR SUPPORTING THE NEW DANCE SQUAD WITH YOUR POP PURCHASE! All around they had drawn hearts and stars and smiley faces. It made me want to puke!

(Pg 24) I stared at Kailey Kaus. Let me admit this right now, sir: I used to love her. Used to. Back in elementary school we were more than best friends. We were like a little husband and wife. I was Luke Skywalker and she was Princess Leia. I had a toy light saber (wields it for a moment, then enacts his memories) We attacked the Death Star – We can do it! We raised her dolls together – (in Kailey’s voice) Juniper has a runny nose, Luke, get a Kleenex!

(embarrassed, the returns to the present) I hate her now. She is my enemy. (Pg 25) Those girls laugh behind my back. I’m Eight-Butt Johnson, man. I’m a fat, stupid joke to them.

(Pg 26) (re-living his outrage) This is fraud! We've been bamboozled! Kailey Kaus!

JUSTIN: Don’t be so dramatic. Nobody’s hiding anything. Just relax.

GABE: Bamboozled! (Pg 33) My hands were shaking by that point. (calms himself) (Pg 32) We all got to the band room and Mr. Shaver told us not to take our instruments out.

SHAVER: (Pg 33) (takes a deep breath) I’m very sorry to say there will be no marching camp this summer.

GABE: (audible gasp) (Pg 95) Band has been my life. Who would I even be? Nobody. My horn playing is the only claim to any kind of excellence I’ve got. I really don’t do anything else. (Pg 35) (his worst imaginings begin to build) Maybe the marching band is losing its funding for next year . . . (Pg 154) Maybe the school’s replaced band camp with this, this, this, stripper camp for cheerleaders! (Pg 37) This means war! (launches his pretend light saber again) (Pg 130) Why are you laughing?

(Pg 64) Firstly, all funding for marching camp comes from the pop machine. Secondly, Shaver wouldn’t cancel it unless the money was gone. And thirdly, why cheerleaders? The same week the pop price goes up, the new dance squad is announced. (Pg 96) Who needs music at football games if there’s a bunch of girls in skirts jumping around.

GABE’S ATTORNEY: (Pg 161) (interrupting) Okay, okay, okay. Let’s talk about Kailey. That’s easier.

GABE: It’s the whole notion of Kailey Kaus, you know? Her hair smells like lilacs because she puts s*** in her hair that smells like lilacs. It isn’t like her hair grows from her head smelling like a spring morning. (realizes his been pacified) (Pg 265) I'm getting our money back. I decided to redistribute all the money back to the people, just like Robin Hood, man! (beat)

(Pg 282) It was a terrible plan, sir – going to waltz into the school, take that money and leave without anyone knowing about it. (Pg 270) Then Kailey showed up. (brief cut to Kailey flipping her lavender scented hair) (Pg 271) Was Kailey going to bring the whole Minnekota jock establishment down on my head? Was she setting up an ambush?

(breaths in deeply, then squeaks) (Pg 280) Hi, there.

KAILEY: Gabe, I am the worst best friend you’ve ever had. I get pushed around by my mom. I get pushed around by [the cheerleaders] I’m so tired of all of these people, Gabe. I don’t want to take your band away (holding back tears) I want to be in your band.

GABE: I really don’t think she wants to be in the band, but that’s pretty sweet of her to say. (to Kailey, starstruck) (Pg 288) You’re pretty cool.

KAILEY: Not really. But now I’m with the leader of the rebellion. Gabe Skywalker, (Pg 281-282) I have a key and codes to the pop machine, we can use the force.

GABE: (Pg 289) (hums Star Wars music) We were Luke and Leia opening a security door in the Death Star. (beat) Of course, we’re stupid. We didn’t have a bag to put the money in. Luckily the change only contained quarters – 18 bucks. (Pg 293) The quarters jingled in my stretch pants pocket. (Pg 292) I took off. I ran! You can do this! I thought. (Pg 130) Why are you laughing?

OFF STAGE VOICE: (Pg 293) Gabe Johnston! Stop where you are! Stop running!

GABE: (skids to a breathless stop one hand in the air, the other holding up his stretchy pants) I stole the money! I stole the money!

OFFICER MCCOY: (Pg 295) (on his shoulder radio mic) Send a car. We got ourselves a little Spunk River ruckus going on. Gabe Johnson. Apprehended.

GABE: (Pg 296) [Turns out] McCoy was looking for me. Not because of the pop machine. Dad realized I was missing – didn’t even try to find me himself – called the cops! They were all looking for me because of Dad.

(Pg 299) Yeah, I'm grounded. I got arrested for robbing a pop machine. That’s a highly ground able business. (Pg 306) I had reporters grab me right away. They knew all about the Spunk River War. (Pg 300) Did you see the front page of the paper? “Fat Boy vs the Cheerleaders.” Better laugh than cry in this case because fat boy is a sexy headline.

(Pg 306) (softer and a bit sad) I was tired of being called names and I’d learned how crappy it is to call people names in general. (Pg 154) (echoing voice) “this, this, this, stripper camp for cheerleaders!” Even if you think those people don't care, they care and it hurts and robs people of their dignity.

REPORTER: (Pg 310-311) Because of Gabriel Johnson’s activism, the offending pop machine has been removed from the high school cafeteria. An increase in county property taxes will be on the ballot in the fall – to fund summer marching camp, a dance team, and most importantly, a healthy breakfast program for all schools.
```
