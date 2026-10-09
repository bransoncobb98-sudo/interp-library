# Classification request: batch 19 of 53 (40 records, IC-1121 to IC-1160)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-019-reply.json`.

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

## IC-1121: Chicken Little

- Title: Chicken Little
- Author (byline): James Finn Garner
- Work: Correct Bedtime Stories, Pgs 57-62
- Publisher: John Wiley and Sons, Inc.
- Publication date as stated: April 1994
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CHICKEN LITTLE, NARRATOR, HENNY PENNY, GOOSEY LOOSEY, FOXY LOXY, ALL TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 879
- Already set (do not supply): none

### Source block (context only)

```text
Author: James Finn Garner
Book: Correct Bedtime Stories, Pgs 57-62
ISBN: 978-0025427303
Publisher: John Wiley and Sons, Inc.
Date (Month/Year): April 1994
```

### Introduction (context only: never use it for content warnings)

```text
Ladies and gentlemen, esteemed members of the jury, and anyone who has ever stubbed their toe and briefly considered suing the furniture . . . welcome! Today’s selection is not just a story. It’s a legal drama; a barnyard thriller, if you will.

You may think you know the story of Chicken Little -- the tale of (pardon my alliteration) panic, paranoia, and poultry? But think again! In this version, the sky isn’t just falling…it’s liable. And someone’s getting paid. When Chicken Little gets bonked on the head, it’s not just a crisis; it’s a lawsuit!

Chicken Little by James Finn Garner
```

### Performance text (classify this)

```text
CHICKEN LITTLE: (Pg 57-62) (happily playing in the road)

NARRATOR: Chicken Little lived on a winding country lane surrounded by tall oak trees. (It should be mentioned here that the name “Little” was a family name, and not a derogatory, size-biased nickname. It was only by sheer coincidence that Chicken Little was also of shorter-than-average height.) One day, Chicken Little was playing in the road when a gust of wind blew through the trees. An acorn was blown loose and hit Chicken Little squarely on the head.

CHICKEN LITTLE: (squawking and spinning in circles)

NARRATOR: Now, while Chicken Little had a small brain in the physical sense, she did use it to the best of her abilities. So when she screamed . . .

CHICKEN LITTLE: The sky is falling, the sky is falling!

NARRATOR: . . . her conclusion was not wrong or stupid or silly, only logically under enhanced. Chicken Little ran down the road until she came to the house of her neighbor, Henny Penny, who was tending her garden. This was a simple task, since she didn’t use any insecticide, herbicide or fertilizer, and also permitted the native nonedible varieties of wildflower (sometimes branded “weeds”) to mingle with her food crops. So, lost amid the foliage, Henny Penny heard Chicken Little’s voice long before she saw her.

CHICKEN LITTLE: The sky is falling! The sky is falling!

HENNY PENNY: (sticking her head out from her garden) Chicken Little! Why are you carrying on so?

CHICKEN LITTLE: I was playing in the road when a huge chunk of the sky fell and landed on my head. See? Here’s the bump to prove it.

HENNY PENNY: There’s just one thing to do.

CHICKEN LITTLE: What’s that?

HENNY PENNY: Sue the b**tards!

CHICKEN LITTLE: (puzzled) Sue for what?

HENNY PENNY: Personal injury, discrimination, intentional infliction of emotional distress, negligent infliction of emotional distress, tortuous interference, the tort of outrage -- you name it, we’ll sue for it.

CHICKEN LITTLE: Good gracious! What will we get for all of that?

HENNY PENNY: We can get payment for pain and suffering, compensatory damages, punitive damages, disability and disfigurement, long-term care, mental anguish, impaired earning power, loss of esteem . . .

CHICKEN LITTLE: (joyfully) Person, oh, person! Who are we going to sue?

HENNY PENNY: Well, I don’t think the sky per se is recognized as a suable entity by the state.

CHICKEN LITTLE: (her diminutive brain working overtime) I guess we should go find a lawyer and learn who is suable.

HENNY PENNY: That’s a good idea. And while we’re there, I can ask whom to sue for these ridiculously bony legs of mine. They’ve caused me nothing but anguish and embarrassment my whole life and I should be compensated somehow for all that.

NARRATOR: So, they ran farther down the road until they came to the house of their neighbor, Goosey Loosey. Goosey Loosey was busy teaching her canine animal companion to eat grass so she could avoid the guilty feelings that came with feeding the dog processed animal carcasses from a can.

CHICKEN LITTLE: The sky is falling! The sky is falling!

HENNY PENNY: Sue the b**tards! Sue the b**tards!

GOOSEY LOOSEY: (leaning over her fence) Land sakes! Why are you two carrying on so?

CHICKEN LITTLE: I was playing in the road and a piece of sky fell on my head.

HENNY PENNY: So we’re going to find a lawyer to tell us whom we can sue both for her injuries and for my bony legs.

GOOSEY LOOSEY: Oh good! Can I come and sue someone for my long, gangly neck? You know, nothing really flatters it, so I am convinced there’s a conspiracy within the fashion industry against long-necked waterfowl.

NARRATOR: So, the three of them ran down the road looking for legal assistance.

CHICKEN LITTLE: The sky is falling! The sky is falling!

HENNY PENNY: Sue the bastards! Sue the bastards!

GOOSEY LOOSEY: Smash the conspiracy! Smash the conspiracy!

NARRATOR: Farther down the road they met Foxy Loxy, who was dressed in a blue suit and carried a briefcase. He held up a paw to halt the entourage.

FOXY LOXY: And what are you three doing out on this lovely day?

ALL TOGETHER: We’re looking for someone to sue!

FOXY LOXY: What are your grievances? Personal injury? Discrimination? Intentional infliction of emotional distress? Negligent infliction of emotional distress? Tortious interference? The tort of outrage?

CHICKEN LITTLE: (excitedly) Oh, yes, yes!

GOOSEY LOOSEY: all that . . .

HENNY PENNY: . . .and more!

FOXY LOXY: Well, then, you’re in luck. My caseload has just eased up, so I will be able to represent you in any and all lawsuits we can manage to bring.

CHICKEN LITTLE: (cheering and flapping her wings) But who are we going to sue?

FOXY LOXY: (without missing a beat) Who aren’t we going to sue? Three hapless victims such as yourselves will be able to find more guilty parties than you can shake a writ at. (deviously) Now, let’s all step into my office so we can discuss this further.

NARRATOR: Foxy Loxy walked over to a small black metal door that was in the side of a small hill nearby.

FOXY LOXY: (trying to lift the latch) Step right this way.

NARRATOR: But the black door wouldn’t open.

FOXY LOXY: (tugging on it with one paw, then with both. It still wouldn’t budge. He yanks and pulls violently, cursing the door, its mental abilities, and its history) Insert random tirade

NARRATOR: Finally, the door swung open, and a huge ball of fire shot out.

FOXY LOXY: (screams and tries to dodge)

NARRATOR: This was really the door to Foxy Loxy’s oven! But unfortunately for him, the ball of fire engulfed his head, burned off every hair and whisker, and left him totally catatonic.

FOXY LOXY: (babbles incoherently)

NARRATOR: Chicken Little, Henny Penny, and Goosey Loosey ran away, thankful that they had not been devoured.

However, the family of Foxy Loxy caught up with them. In addition to suing the manufacturer of the oven door on behalf of Foxy Loxy, the family brought suit against the three barnyard fowl: Chicken Little, Henny Penny and Goosey Loosey, claiming entrapment, reckless endangerment, and fraud. The family sought payment for pain and suffering, compensatory damages, punitive damages, disability and disfigurement, long-term care, mental anguish, impaired earning power, loss of esteem, and the loss of a good dinner.

The three birds later brought a countersuit, and they’ve all been battling in court from that day to this.
```

---

## IC-1122: Choices

- Title: Choices
- Author (byline): James McLindon
- Work: The Best New Ten-Minute Plays 2020, Pg 39
- Publisher: Applause Theatre and Cinema Books
- Publication date as stated: Oct 2020
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: PROSPECTIVE CLIENT, DEBT COUNSELOR
- Teaser before the introduction: No
- Spoken words (computed): 1371
- Already set (do not supply): none

### Source block (context only)

```text
Author: James McLindon
Book: The Best New Ten-Minute Plays 2020, Pg 39
ISBN: 978-1493053278
Publisher: Applause Theatre and Cinema Books
Date (Month/Year): Oct 2020
```

### Introduction (context only: never use it for content warnings)

```text
According to the Federal Reserve Bank of New York, in 2020 student loan debt reached an all-time high, nearly $1.6 trillion among more than 40 million Americans, making the Department of Education the country's biggest consumer lender. Furthermore, according to the U.S. Department of Education, about 1 in every 5 borrowers are in default.

Student loan debt is out of control. Heck, there’s even a television trivia game show called Paid Off with Michael Torpey where the winner has the chance to win the sum of their student debt in cash. We have entered the theatre of the absurd . . . but James McLindon in his short play Choices takes it one step further.

Choices by James McLindon

(Pg 39 – 46) A modest living room (think poor graduate student), the present. The PROSPECTIVE CLIENT sits at her/his coffee (or dining room) table across from the DEBT COUNSELOR, who has the calmness and patience of a funeral home director for the most part, there to help and alert to steer clear of any heaviness with a ready euphemism. All of that is underlaid with an enthusiastic love of her/his product. The PROSPECTIVE CLIENT is a little anxious, really needing this to work. The DEBT COUNSELOR has been waiting for the PROSPECTIVE CLIENT to finish reading a pamphlet. The PROSPECTIVE CLIENT now looks up, perplexed.
```

### Performance text (classify this)

```text
PROSPECTIVE CLIENT: I'm sorry, I just don't get it.

DEBT COUNSELOR: It's pretty simple. It's just ... disruptive.

PROSPECTIVE CLIENT: No, I know, it sounds simple ....

DEBT COUNSELOR: Think of it as a choice. We're all about choices. You can choose this. Or not.

PROSPECTIVE CLIENT: No, no, I want to choose this, believe me. I feel like I'm on a hamster wheel just trying to keep up with the payments, but ... this just seems too good to be true.

DEBT COUNSELOR: That's often what disruption looks like. Remember all the things you used to have to pay to read, like newspapers, magazines? Now you get them on-line for free. We're disrupting the entire debt consolidation industry, sort of like that.

PROSPECTIVE CLIENT: Okay, but ... I still don't get it.

DEBT COUNSELOR: Tell me what you don't get.

PROSPECTIVE CLIENT: So, you pay off my student loans...

DEBT COUNSELOR: Your crushing student loans.

PROSPECTIVE CLIENT: Yes, thank you, my 247,000 dollars in student loans, and all I have to do is pay you seventy-two dollars a month?

DEBT COUNSELOR: Yes.

PROSPECTIVE CLIENT: For twenty years.

DEBT COUNSELOR: Yes.

PROSPECTIVE CLIENT: And that's it. That's all I ever have to pay you.

DEBT COUNSELOR: That's all you ever have to pay us. (The PROSPECTIVE CLIENT calculates in her/his head.)

PROSPECTIVE CLIENT: Okay, so I'm not really great at math, but I think that's only, like, $170,000?

DEBT COUNSELOR: It's actually about $17,000.

PROSPECTIVE CLIENT: Only 17,000 dollars!? Okay, now I don't get this even more.

DEBT COUNSELOR: Tell me what you don't get.

PROSPECTIVE CLIENT: What don't I...? You give me 247,000 dollars to pay off my debt today and all I have to give you is 17,000 dollars over twenty years?

DEBT COUNSELOR: Right. Mainly to keep you focused.

PROSPECTIVE CLIENT: So you lose money.

DEBT COUNSELOR: No ...

PROSPECTIVE CLIENT: Yeah, you lose money. Nobody sets up a business to lose money, unless they're, like, money laundering or something. Wait, are you guys money laundering?

DEBT COUNSELOR: No.

PROSPECTIVE CLIENT: What are you doing?

DEBT COUNSELOR: We're providing choices. (Pause.) I think maybe you skipped footnote seven.

PROSPECTIVE CLIENT: I didn't read the footnotes.

DEBT COUNSELOR: You should read the footnotes.

PROSPECTIVE CLIENT: I never do.

DEBT COUNSELOR: You always should.

PROSPECTIVE CLIENT: Okay, fine, what does footnote seven say?

DEBT COUNSELOR: It answers this question.

PROSPECTIVE CLIENT: About whether you're money laundering?

DEBT COUNSELOR: About how we get paid. (Beat.)

PROSPECTIVE CLIENT: So how do you? I mean, after I finish my payments you'll be short about 230,000 dollars. Not to mention any interest. So where do you get the rest (from) ... ? Oh, there're a bunch of hidden fees, aren't there?

DEBT COUNSELOR: There are no fees at all.

PROSPECTIVE CLIENT: Then c'mon, how do you get your money back from me?

DEBT COUNSELOR: We don't get it back from you.

PROSPECTIVE CLIENT: You don't?

DEBT COUNSELOR: We don't. (Pause.) From you.

PROSPECTIVE CLIENT: Who do you get it back from?

DEBT COUNSELOR: The insurance company.

PROSPECTIVE CLIENT: What insurance company?

DEBT COUNSELOR: You should really read footnote seven ...

PROSPECTIVE CLIENT: Just tell me, what insurance company!?

DEBT COUNSELOR: Your insurance company.

PROSPECTIVE CLIENT: Why would my car insurance company pay you?

DEBT COUNSELOR: Not your car insurance company.

PROSPECTIVE CLIENT: Well, that's the only insurance I have. I sure don't have homeowners because you can't afford to buy a house when you owe $247,000 ...

DEBT COUNSELOR: Your life insurance company. (Beat.)

PROSPECTIVE CLIENT: I don't have life insurance.

DEBT COUNSELOR: Footnote seven.

PROSPECTIVE CLIENT: I have to get life insurance?

DEBT COUNSELOR: We pay for it.

PROSPECTIVE CLIENT: What good does life insurance do anyone?

DEBT COUNSELOR: It depends.

PROSPECTIVE CLIENT: Unless I die.

DEBT COUNSELOR: Read footnote seven.

PROSPECTIVE CLIENT: Oh my God. You've looked at my DNA! You have, you totally have! That DNA company that said I was 2.3% Neanderthal sold you my data and you looked at it and you know I have a genetic abnormality and I'm going to die young, so that's how you ... What are you writing down?

DEBT COUNSELOR: No, please, go on, that's a really interesting business model.

PROSPECTIVE CLIENT: Stop it! That's not your business model?

DEBT COUNSELOR: No, but it's pretty good though. Way disruptive.

PROSPECTIVE CLIENT: So I'm not going to die in the next twenty years?

DEBT COUNSELOR: Well, how would I know that?

PROSPECTIVE CLIENT: There's no DNA stuff in your file on me?

DEBT COUNSELOR: All we have is what you gave us.

PROSPECTIVE CLIENT: (Exhaling.) I'm not going to die young.

DEBT COUNSELOR: Well, not in the next twenty years. As far as I know.

PROSPECTIVE CLIENT: Do you qualify everything you say?

DEBT COUNSELOR: When it needs to be. Because we're totally honest. With our clients.

PROSPECTIVE CLIENT: So how do you make money from my life insurance?

DEBT COUNSELOR: How does anyone make money from life insurance?

PROSPECTIVE CLIENT: Somebody has to die. (Pause.) But you just said I wouldn't!

DEBT COUNSELOR: I said I don't know anything about your DNA. Or your health at all for that matter. We don't worry about that. Please. Read footnote seven.

(PROSPECTIVE CLIENT stares at DEBT COUNSELOR, who stares back. A beat.) Please.

PROSPECTIVE CLIENT: Okay, fine. (PROSPECTIVE CLIENT returns to reading the pamphlet. Then PROSPECTIVE CLIENT looks up at DEBT COUNSELOR, stunned.) Oh my god!

DEBT COUNSELOR: (Excited for the first time.) I know, right!? The first time I read it, I was like, Whaaaaat!? But the more you think about it, the more genius it is. Dis! Effing! Ruption! Amiright!? (Catching himself, quieting.) Sorry. I just love this product so much.

PROSPECTIVE CLIENT: I'm not going to agree to this! Does anyone ever agree to this?

DEBT COUNSELOR: No. (Pause.) Not at first. But then they think about it. And they think, well, when I took out my crushing student loans, I knew that they would impact my life. Severely impact my life. For a whole lot of my life. Decades and decades. And see, that's all this is really. You just assumed that the impact would be frontloaded. And all we do is ... backload it for you.

PROSPECTIVE CLIENT: Me dying at (whatever age is about twenty years older than actor) in twenty years, that's what you call "severely impacting" my life?

DEBT COUNSELOR: Well, it seems severe to me.

PROSPECTIVE CLIENT: No, it's severe, it's very severe!

DEBT COUNSELOR: Yes. But. What a much better life it will have been. These next twenty years anyway. Which, after all, is your prime.

PROSPECTIVE CLIENT: How do you ... you know...do it?

DEBT COUNSELOR: Do what?

PROSPECTIVE CLIENT: Make it so you get to, you know, collect. (Pause.)

DEBT COUNSELOR: Before we get into the details, I think it's best that you get comfortable with the concept (first) ...

PROSPECTIVE CLIENT: How!?

DEBT COUNSELOR: Well, it's up to you. See? Choices. Most people opt to handle matters themselves. We'll give you some recommendations and how-tos in the next brochure it's under "Self-Termination." A lot of people, though, find they're too ... squeamish? for Self-Term when push comes to shove and for them we offer Appointment Service. You know how you can schedule a caesarian these days? Well, this is sort of ...

PROSPECTIVE CLIENT: The exact opposite.

DEBT COUNSELOR: Yes. The App Serv team is excellent, guaranteed painless and they can make anything look like an accident. And finally, there are some people who are squeamish, but who also find that having an actual appointment makes them ...

PROSPECTIVE CLIENT: Freaking terrified?

DEBT COUNSELOR: Mmm, anxious. For them we offer a third approach, a service where you just go about your business and we ... take it from there. That one's called Dealer's Choice. (Pause.) You don't have to decide that now.

PROSPECTIVE CLIENT: A lot of people must just run when their time is up.

DEBT COUNSELOR: Oh, people are surprisingly ethical about it. Also, we implant a chip that sends us your GPS coordinates.

PROSPECTIVE CLIENT: What if I dig the chip out?

DEBT COUNSELOR: We don't put it anywhere too ... accessible? And if you did get it out, we always have the Recovery Team.

PROSPECTIVE CLIENT: The chips are that valuable?

DEBT COUNSELOR: You're that valuable. You know how the Coast Guard has rescue and recovery units. This is more recovery and ... not rescue. (Beat.) You can always say no. We're all about choices. (Suddenly, the DEBT COUNSELOR has an edge, a subtle darkness. Maybe there's a lighting change for his/her next speech.) Quantity or quality. You can live in your run-down studio apartment if you want. With a roommate. And drive a fifteen-year-old beater. And eat ramen noodles. And never take a decent vacation. And waste a lot of your life living on the shoulder of poverty.

PROSPECTIVE CLIENT: Or I can have only twenty years left.

DEBT COUNSELOR: Twenty debt-free years to keep and spend your money. To travel, buy a house, have a life, whatever that means to you. And do you really want to live longer than that?

PROSPECTIVE CLIENT: My parents got to.

DEBT COUNSELOR: But do you want to? With the rising tides of climate change lapping at your ankles and blowing down your little garret. With the last shreds of our democracy fraying before your eyes, while the old-world order collapses. I don't think it's too much to say that the ones who choose to go with us are in many ways the lucky ones. (Pause; brighter again.) Hey, it's a big decision, so you take your time, talk to your friends, your family. And if you do choose to go with us, just give me a call. (The DEBT COUNSELOR hands the PROSPECTIVE CLIENT a card, shakes hands, and begins to leave.)

PROSPECTIVE CLIENT: Wait. Are ... are you a client? (The DEBT COUNSELOR turns back, smiles and pulls up his/her shirt.)

DEBT COUNSELOR: There's my GPS scar. Take a look around on the beach this summer. You'll be surprised. (Smiling.) Call me. (Exits.)

(The PROSPECTIVE CLIENT looks at the card, snorts in derision, throws it in the trash can, then sits down and thinks for a few moments. She/he picks the trash can up, starts to reach in to remove the card, and then stops. Still holding the can, she/ he looks up, uneasy, thinking.)
```

---

## IC-1123: Cinderella Wore Combat Boots

- Title: Cinderella Wore Combat Boots
- Author (byline): Jerry Chase
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: KING, PRINCE, GODZELLA, MAZZARELLA, TOGETHER, CINDERELLA, MAZARELLA, MAZARRELLA, M & G, FGP, CINDERELLA & PRINCE
- Teaser before the introduction: Yes
- Spoken words (computed): 1785
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jerry Chase
ISBN: 978-0822202134
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
Cinderella Wore Combat Boots by Jerry Chase
```

### Performance text (classify this)

```text
KING: Hello! I’m King Charming. This is a wonderful kingdom and I am a wonderful King. But I do have one big problem – my son! My son will be King one day, but he won’t settle down and take any responsibilities. All he does is hunt dragons. The only way we’ll get him to the altar is by draggin’ him there. Here. I’ll let you meet him. Son! Prince Charming!

PRINCE: Hi, dad! Ready for the dragon hunt?

KING: Knock it off, son. We’ve got to have a serious talk.

PRINCE: Okay . . .

KING: You’ve got to think about taking over the kingdom someday. After all, I’m not going to last forever – someday I’ll be gone and . . .

PRINCE: Dad! Don’t talk like that!

KING: No, son, it’s true. One day you will wear this crown. Here, try it now –

PRINCE: No! Dad, that’s yours. I couldn’t . . .

KING: Son, I command you to take it (Prince takes crown and puts it on) Now, how does that feel?

PRINCE: Hey! That feels pretty good!

KING: I’m not dead yet! You’ve got to start thinking about something besides dragons. It’s time you settled down –

PRINCE: But dad, I’m only thirty-eight!

KING: It’s time! You’ve got to start a social life. Meet some girls . . .

PRINCE: Aw, dad, girls have cooties . . . Right?

KING: Oh, shut up, Prince. Now listen; I’m going to throw a ball . . .

PRINCE: Okay, Dad. I’ll catch it!

KING: Not that kind of a ball, you doofus. A big party . . . with a band, lots of food . . . dancing . . . you’ll meet lots of girls . . .

PRINCE: Aw, Dad, do I have to?

KING: I proclaim a royal ball! All the maidens in the kingdom will be there. The Prince will dance with each and every one. And, the one he likes the best shall marry him and become the new Queen. I have spoken!

GODZELLA: Hi! I’m Godzella and I work hard at being beautiful. Of course, you’re wondering how I got this way. I don’t blame you. Well, I’ll tell you. It’s the right clothes, the right deodorant, and, of course, you must eat in the right restaurants. I think I’ll sit here and just be lovely.

MAZZARELLA: Hi! I’m Mazzarella, and I know what you’re thinking . . . if she’s that pretty, she must be dumb. But I’m not just pretty. Inside this head is just full of knowledge. I think I’ll sit with my mirror and gaze at how beautiful I am.

GODZELLA: Oh! I dropped my comb.

MAZZARELLA: She dropped her comb!

TOGETHER: Cinderella! Cinderella!

CINDERELLA: Yes, what can I do? I love to help.

GODZELLA: Cinderella, I dropped my comb. (looks to audience) She’s so slow and stupid.

MAZARELLA: She certainly is. Oh! I dropped my brush.

GODZELLA: She dropped her brush!

MAZARRELLA: Pick it up at once!

GODZELLA: Cinderella, you’ve fooled around enough cleaning the oven. Go clean the bathroom before you fix our lunch.

CINDERELLA: Yes, of course. Thank you.

GODZELLA: I wish I could have a new stepsister! Cinderella is so icky and skeevy.

MAZARELLA: Me too. I want one that’s slower and dumber than Cinderella because I love to nag and holler. (Knock, Knock, Knock)

M & G: Someone’s at the door! Cinderella! Cinderella!

CINDERELLA: It’s a messenger from the King.

M & G: Squeal! Squeal! A messenger from the King! Squeal! Squeal!

CINDERELLA: (reading message) Hear Ye! Hear Ye! The King is having a ball. (M & G squeal)All the maidens in the kingdom are summoned to the palace this very evening. Each and every maiden will dance with Prince Charming! (M & G squeal) And the one he likes the best will marry him and become the new Queen!!

GODZELLA: I’m gonna marry the Prince!

MAZZARELLA: I’m gonna be the Queen! We must get ready, Cinderella! Get my gowns and wigs and stuff.

GODZELLA: Cinderella! I need a perm, a nose job, and . . .

MAZZARELLA: Get me my platform shoes, my smelliest perfume, and don’t . . .

GODZELLA: I need my lifts, my props, my aids . . .

CINDERELLA: I hope I have time to get ready as well. . .

GODZELLA: (finally dressed and ready) Now I ask you . . . Could anyone resist?

MAZZARELLA: Put your money where your mouth is, Sisster. You had to put more make up on than a clown to look good.

M & G: Cinderella, call the carriage.

CINDERELLA: The carriage is called.

GODZELLA: What do you call that?

CINDERELLA: These are the clothes my real mother left me.

MAZZARELLA: And where do you think you’re going?

CINDERELLA: Why . . . to the ball. (M & G laugh)

GODZELLA: Cinderella, don’t be ridiculous! You’re too dirty and stupid to go to the ball. Suppose the Prince saw you and found out we knew you. You’d spoil our changes to marry the Prince.

MAZZARELLA: You must stay here and clean the fireplace, and beat the rugs and slop the pigs . . . or is it slop the rugs and beat the pigs? Oh, well, it doesn’t matter . . . Come sister, our carriage awaits. (Stepsisters leave. Cinderella starts crying. Fairy God-Person appears)

FAIRY GOD-PERSON (FGP): Dear, what could possibly be wrong?

CINDERELLA: My stepsisters went to the ball without me. Who are you?

FGP: I’m your fairy god-person. I’ll always come to help you if you really need me.

CINDERELLA: But how can you help me? I’m too dirty and ugly and dim-witted . . . I’d ruin my sister’s changes to marry the Prince.

FGP: Who told you those things?

CINDERELLA: My sisters.

FGP: I think you should go to the King’s party.

CINDERELLA: Oh, I couldn’t do that. Not looking like this. I don’t even have a dress to wear. Do you think a different dress would help?

FGP: Bibbity Bobbity Boo!

CINDERELLA: Hey! What’s happening! Wow! Look at this dress! I can go to the palace and see the people and everything . . . (looks at feet) Oh, Gee . . .

FGP: What’s the matter, dear?

CINDERELLA: I can’t go without shoes; all I have left are the combat boots my father left me.

FGP: Then by all means . . . wear them. You look great!

CINDERELLA: I don’t know how to thank you.

FGP: Your happy face is thanks enough. Go have a good time.

CINDERELLA: (starts then stops) Oh! (looks at floor)

FGP: What’s the matter, dear?

CINDERELLA: I’ll need money for the bus.

FGP: What’s the matter with me? You can’t go on the dirty, crowded bus in those clothes. Look out the window. What do you see?

CINDERELLA: You mean that pumpkin and those six white mice?

FGP: Bibbity Bobbity Boo! Now what do you see?

CINDERELLA: Hey! It’s a coach and six white horses!

FGP: Now are you ready to go to the ball. Wait! Don’t let me forget the most important thing! You must be home by midnight. That’s the time that all the magic disappears.

CINDERELLA: Oh, I’ll be home by then. I’m not going to dance or anything. I’m just going to look around, maybe take a few notes, and come right back.

FGP: Don’t forget the time! (to audience) Well! I bet the ball is in full swing. I wonder if everyone is having a great time . . . *****At the ball*****

PRINCE: Parties are a drag.

KING: (talking to a random woman) All right, honey, I’ll meet you by the buffet. (to Prince) Hi, son. Isn’t it a great party? Are you meeting all the maidens?

PRINCE: I’m working up to it.

KING: Hey! Here comes one now, son. She’s a real beauty. Okay, now, cool and suave, remember (to audience) You watch him . . . cool and suave.

GODZELLA: Wow! There’s the Prince. I’ll win him over. You just watch.

PRINCE: Hello.

GODZELLA: Hello? He said “hello.” (laughs) You’re funny. You wanna dance?

PRINCE: Yeah, sure.

GODZELLA: Hit it! (starts awkwardly fast dancing) Do you like dragons?

PRINCE: Yes, I do . . . I . . .

GODZELLA: Ohhhhh! That’s really funny. Don’t you think I’m sort of awesome? All my friends say I’m awesome.

PRINCE: Yes, I could see maybe a sort of . . . . Say, would you like a cup of hot chocolate? I’ll get it for you. (leaves quickly.

GODZELLA: Hey! Wait for me!

KING: (talking to another woman) Don’t go away, sweetheart. I’ll be right back. (to Prince) Oh, there you are, son. How was she?

PRINCE: I found her a bit aggressive.

KING: All right, now, son, listen to me. You can’t give up . . . as long as you keep trying, you’ll . . . . Wait! There’s another one. OK, don’t forget. Suave and cool.

CINDERELLA: Oh! Just look at everything. The rooms are so huge – and the people – and dragon heads everywhere . . . I wonder . . .

CINDERELLA & PRINCE: (bumping into each other) Oh! Excuse me. I didn’t see . . .

CINDERELLA: Wow! I wonder who he is.

PRINCE: Wow! I wonder who she is.

CINDERELLA: I wonder if he’s going to ask me to dance.

PRINCE: May I have a dance with you?

CINDERELLA: Nothing would please me more.

(Price starts fast dancing awkwardly, Cinderella follows with the same awkward dance)

CINDERELLA: He’s so big and strong. I know he can take care of me.

PRINCE: She’s so big and strong. I know she can take care of me

CINDERELLA: Say, would you tell me who you are?

PRINCE: I – uh – sure – I’m – You know – Hey, those are great boots. Where did you get them?

CINDERELLA: From my dad. They’re really comfortable. Here take a look.

PRINCE: Yeah, these are good. (to audience) Oh, my gosh, she’s perfect. I don’t think I have to look any more. (Drops to one knee – to Cinderella) Listen, I know that you’re some Princess or something, and I’m just Prince Charming from this kingdom . . . but I love you, and I must ask you a very important question . . .

CINDERELLA: (to audience) I didn’t know he was the prince

PRINCE: Will you marry me and be our Queen?

CINDERELLA: (to audience) But he doesn’t even know who I am. What should I do?

PRINCE: Say yes!

CINDERELLA: Okay, my answer is . . . (Clock begins to strike 12:00 – Bong, bong, bong) Oh! I can’t stay (Bong, bong, bong) I have to go! (runs off) (Bong, bong, bong) Oh, I’ve got to get home. (Loses boot)

PRINCE: (chasing after Cinderella) Wow! She’s fast (finds boot) Wait!

KING: What are you doing with that boot, son?

PRINCE: Dad! I found her! The one we were hoping for. She’s fantastic – I love her – but I don’t know who or where she is. All I have left is this boot.

KING: Wait a sec. You’re telling me that the girl you live fits inside that boot?

PRINCE: Just her foot, Dad. All we have is the boot. How can we find her?

KING: I have it! A Charming Proclamation! Tomorrow we shall go to every house in the kingdom and try this boot on the foot of every maiden in the land. ***** The next day*****

GODZELLA: (yawning, just waking up) Boy, what a night. I’d sure like to get hold of that twit who stole the Prince. I’d shake her to pieces and kick her and stomp on her -- but I don’t know who she is or where she is.

MAZZARELLA: Yeah, if I had that strumpety hussy here, I’d punch her and push her and kick her until she couldn’t get up -- but I don’t know who she is or where she is.

GODZELLA: Cinderella, go fix our breakfast. Then afterwards, scrape the furnace, fix the roof, dig a new cesspool, and clean the dishes.

CINDERELLA: Yes, of course. Have a nice day. (Knock, knock, knock)

KING: Make way for the King!

M & G: The King! (bows, holds)

KING: Hear Ye! Hear Ye! The maiden whose foot fits this boot will marry my son, the Prince, and be our new Queen.

GODZELLA: It’s me! It’s me! Put it on. (tries it on, but doesn’t fit)

MAZZARELLA: Ha! (takes boot) I knew it was me. (tries it on, but doesn’t fit)

CINDERELLA: Hey everybody! Come and see the new cesspool.

KING: What is that? Is that a girl?

MAZZARELLA: No, that’s Cinderella. She’s our dumb stepsister.

GODZELLA: She’s nothing.

KING: Well, we said every maiden. I guess that includes her. (tries it on)

KING: Look! It fits!

M & G: (can’t believe it) IT FITS?!

KING: Son! Come here! Prince Charming!

PRINCE: It’s no use, dad. We’re never going to find her. We might as well . . . (gasps) It’s you!

CINDERELLA: It’s you.

PRINCE: It’s us.

CINDERELLA: It’s we.

GODZELLA: Great. . . now they’re going to go live happily ever after or something.

MAZZARELLA: That’s usually how these things go . . .
```

---

## IC-1124: Clash of the Titanic

- Title: Clash of the Titanic
- Author (byline): Eric D. Snider
- Work: Snide Remarks ASIN: B000REH4ZS (available through Amazon.com)
- Publisher: Eric D. Snider
- Publication date as stated: January 1998
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, KATE WINSLET, KATE’S WEASELLY FIANCE, KATE, LEONARDO DICAPRIO, LEONARDO, WEASELLY FIANCE, AUDIENCE, FIRST MATE, CAPTAIN, ICEBERG
- Teaser before the introduction: Yes
- Spoken words (computed): 900
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eric D. Snider
Newspaper: 1st Published in the Brigham Young University Newspaper, The Daily Universe,
February 9, 1998
Website: Now available at https://www.ericdsnider.com/snide/clash-of-the-titanic/
Snide Remarks #26
ISBN: N/A
Publisher: Brigham Young University Press / Eric D Snider.com
Date: February 9, 1998
Also Published in
Author: Eric D. Snider
Book: Snide Remarks
ASIN: B000REH4ZS (available through Amazon.com)
Publisher: Eric D. Snider
Date: January 1998
```

### Introduction (context only: never use it for content warnings)

```text
Clash of the Titanic by Eric D. Snider
```

### Performance text (classify this)

```text
NARRATOR: Many of you have seen the film “Titanic,” which is about a great big boat that sank like a thousand years ago that for some reason everyone is just now getting worked up about. Some of you—I am speaking to the women here—have seen this movie several times. And I would like to know why. You think there’s a chance the movie will end differently if you see it again? Do you think this is a “Choose Your Own Adventure” movie? It’s NOT! No matter how many times you see it, the boat is going to sink, and the same people are going to die. This movie is entirely too long. The actual sinking of the Titanic took only four hours; the movie is easily three times that long. [So] as a public service, [we are] offering this much-shortened screenplay . . .

(Scene 1)

KATE WINSLET: Why, this is a fancy boat, isn't it?

KATE’S WEASELLY FIANCE: Yes, it certainly is. Here is the art you asked for. It is by an artist named "Picasso." I am certain he will amount to nothing.

KATE: Ha ha ha. That is very funny to our audience, because of course Picasso later amounted to quite a bit, after this boat sank.

LEONARDO DICAPRIO: Hello, I'm Leonardo DiCaprio. Perhaps you have seen the many Internet sites dedicated to the worship of me. You are very pretty.

KATE: Thank you. So are you.

LEONARDO: I know. Prettier than you, in fact. I am going to put on my "brooding" face now, to ensure that women will keep coming back again and again to see this movie. Later, my white shirt will be soaking wet.

KATE: While you're doing that, I will concentrate on standing here and looking pretty, to keep the men in the audience interested until the boat sinks and people start dying.

WEASELLY FIANCE: Excuse me. I do not like you, Leonardo, even though you saved my fiancée's life. I am going to sneer at you and treat you like dirt because you're poor, and then I'll probably be physically abusive to my fiancée, and then, just to make sure the audience really hates me, and to make sure my character is entirely one-dimensional, perhaps I'll throw an elderly person into the water.

AUDIENCE: Boo! We hate you! Even though all real people have at least a few admirable qualities, we have not been shown any of yours, and plus, you're trying to come between Leonardo and Kate, and so therefore we hate you! Boo! (Even though technically it is Leonardo who is coming between you and Kate. But Leonardo is handsomer than you, even though he is only 13, so we are on his side. Boo!)

(Scene 2)

LEONARDO: I'm glad we snuck away like this so that you could cheat on your fiancé.

KATE: So am I. Even though I am engaged to him and have made a commitment to marry him, that is no reason why you and I cannot climb into the back seat of a car and steam up the windows together. The fact that I am the heroine of the movie will no doubt help the cattle-like audience forgive me of this, though they would probably be VERY angry indeed if my fiancé were to do the same thing to me.

AUDIENCE: Darn straight, we would! Moo! We mean, Boo!

LEONARDO: I agree. First, I would like to draw you, though, so of course you have to take off all your clothes.

KATE: But can a movie with five minutes of continuous nudity be at all successful in, say, Provo, Utah, where the audiences might not stand for that sort of thing?

LEONARDO: I would be willing to bet that for the first three weeks the film is in release, every single showing at the Wynnsong Theater in Provo will sell out.

NARRATOR: According to Wynnsong manager Matt Palmer, that is exactly what happened.

KATE: All right, then. (sound of clothes hitting the floor)

(Scene 3)

FIRST MATE: Captain, we're about to hit an iceberg!

CAPTAIN: Great, I could use some ice for my drink. (sound of drinking)

ICEBERG: (hits boat)

FIRST MATE: That can't be good.

CAPTAIN: Bottoms up!

AUDIENCE: Huh?

FIRST MATE: That was irony, you fools.

AUDIENCE: Baa! Moo! Where's Leonardo?

(Scene 4)

LEONARDO: I have been informed that this boat is sinking.

KATE: That is terrible.

LEONARDO: Would you like to engage in some more immoral-but-justified behavior?

KATE: Certainly.

AUDIENCE: Boo! Boo!

WEASELLY FIANCE: (aside) I'm getting the raw end of the deal here. (to Leonardo) Listen, Leonardo, to cement my morally-dubious-yet-somehow-less-annoying-than-you personality, I am going to handcuff you to this pipe, here in a room that will soon be filling with water, due to the fact that we are sinking, which I believe has been mentioned previously.

LEONARDO: Why don't you just shoot me?

WEASELLY FIANCE: Because then you wouldn't be able to escape and save Kate from me. Of course, you're going to die anyway --

AUDIENCE: Don't spoil it for us! Booooooo!!

LEONARDO: He's right, though. I am doomed.

AUDIENCE: Aww, look how cute he is when he's doomed!

WEASELLY FIANCE: I hate you people.

(Scene 5) 150-YEAR-OLD-KATE: And that's when Leonardo rescued me from my evil fiancé and helped me float on a board in the water. Of course, if it hadn't been for having to rescue HIM, I could have gotten on an actual lifeboat, and frozen my legs nearly off. Anyway, he's pretty much dead now, and I'm well over a thousand years old, and who's making my supper? I need a bath. Turn down that Enya music, it's making my ears hurt. You kids today, with your loud music. Why, when I was -- hey! Don't you walk away from me, Mr. Snooty-Patootie! I'd turn you over my knee, if I had one. I'll beat you in the head with this huge diamond! Come back here!

(FADE TO BLACK; roll credits; annoying Celine Dion song [Hum theme from Titanic])
```

---

## IC-1125: The Complete History of America (Abridged)

- Title: The Complete History of America (Abridged)
- Author (byline): Adam Long, Reed Martin and Austin Tichenor
- Work: Not specified
- Publisher: Broadway Play Publishing
- Publication date as stated: June 2000
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: REED, ADAM, AUSTIN, VESPUCCI, SOPHIA, PASTOR, ANNOUNCER, MINUTE MAN, MADISON, FRANKLIN, SOLDIER, SARGE, FDR, HITLER, ROCK FURY, EVA BRAUN, HAWKEYE PIERCE, ANNOUNCER 2, GAME SHOW HOST, CONTESTANT, SPADE, CONSPIRATOR GUY
- Teaser before the introduction: Yes
- Spoken words (computed): 1678
- Already set (do not supply): none

### Source block (context only)

```text
Author: Adam Long, Reed Martin and Austin Tichenor
ISBN: 978-0881451481
Publisher: Broadway Play Publishing
Date (Month/Year): June 2000
```

### Introduction (context only: never use it for content warnings)

```text
The Complete History of America (abridged) by Adam Long, Reed Martin and Austin Tichenor
```

### Performance text (classify this)

```text
Notes from the Authors: Although we use the names Adam, Reed, and Austin within the script, each cast member should use his own real name when performing the show. There are topical references in the script. The humor and relevance of these will fade over time, so we encourage each production to change these references to keep them as up-to-date as possible. [References have been updated for performances in 2026; changes appear in red] ************

REED: (Pg 3-4) Good morning/afternoon/evening! I’m [insert name] and tonight we explore the history of a great nation.

ADAM: [After all] it is only through remembering our past that we can learn from our mistakes, or at least blame them on somebody else, and then move on . . . into a better future.

AUSTIN: (Pg 5) [Today] many Americans are at best uninformed or at worst embarrassed about our own history.

REED: Well, damn it, we’ve got nothing to be embarrassed about! We brought the world its first democracy . . . a man on the moon . . . McDonalds, Big Bird and Bart Simpson!

ADAM: Let’s do it!

REED: (Pg 5) We begin at the beginning: 1492 Spain! The first chapter of the history of America is about to be written by that legendary Italian explorer . . . (fanfare) Amerigo Vespuchi! We join him now in his humble map shop.

VESPUCCI: (bad Italian accent and flamboyant hand-gestures) Ring-a! Ring-a! (Answering his hand) Hello, Maps-R-Us. Amerigo Vespucci here . . .

SOPHIA: Amerigo!

VESPUCCI: (Pg 6) Shaddup, woman! I’m on the telephone!

SOPHIA: My parents told me not to marry you. They said, “Marry a nice boy, like that Christopher Columbus. He’s going places!

VESPUCCI: (Looks into phone) Hello? (He hangs up) Great! You just lost me a customer. I hope you’re happy, Sophia!

SOPHIA: (Pg 7) Let’s face it, Amerigo, nobody buys your maps because they’re crap!

VESPUCCI: I can’t stay here any longer. I’m off to discover a larger world. You will never see me again!

SOPHIA: Amerigo!!!!!

REED: (Pg 8) In 1502, after two long, treacherous voyages, Amerigo concluded that what everyone had thought was India was actually a new world. Eventually it bore his name AMERICA!

ADAM: (Pg 10) Hey! [What about] Christopher Columbua? He discovered the New World!

REED: Well, his name really wasn’t Christopher Columbus, it was Christobal Colon. And he bumped into the New World by mistake. He wasn’t even the first one here! There was a native population of over 90 million people here before he arrived.

AUSTIN: Yeah, but in fairness to Columbus, though, he was the first man to slaughter and enslave the native population AND he became very wealthy in the process. So in that sense, he was the first true American!

ADAM: (Pg 13) Hey, can I do that poem I wrote? I wrote a poem about the first English settlement in North America

REED: [FLASH FORWARD TO 1607] (Shrugs . . .)

ADAM: (Pg 14-15) 'Twas 1607, in the fine month of May, That three proud ships land at Chesapeake Bay

Jamestown was born, so the story was told, To spread our Lord's word and for mining of gold.

The livin' was harsh for those brave men and women. They toiled and they sweated and rarely went swimmin'.

The new world was tamed by men who were brave And men who were strong and six million slaves

(shocked expressions and the raps peters out) And indentured servants and the Iroquois nation Who gave up their land without compensation

(Trying to regain momentum) So the Pilgrims perfected the art of good livin',
They carved up the land and invented Thanksgivin'
And lickety split, just as quick as you please,
Wham barn ma'am there were thirteen colonies

PASTOR: Hello, and welcome to our weekly meeting of Salem’s First Church of Tolerance and National Witchhunter’s Association. I am your pastor, the Reverend Orwell. Last night the Lord came to me and He said . . . You and your followers need to kill 100 witches this week or I’m going to call you home! So I urge you to hunt the good hunt. And don’t forget that this witch-hunt will begin an American tradition that will carry on well into the twentieth century! Here’s how you spot a real witch: They melt when you throw water on them, they’re surrounded by flying monkeys and they may actually run for president someday!

AUSTIN: (Pg 16) Hey! The king has doubled our taxes and we’re putting together a people’s army to fight him right now. We’re off to throw tea in the harbor!

ANNOUNCER: (Pg 17) Paul Revere and the Raiders number on the charts with “The British are Coming”

ADAM: Listen, my children, and you shall hear of the midnight ride of Paul Revere!

AUSTIN: (Pg 18) And a full-fledged revolution was underway. The colonists wanted to stop the British government from imposing unfair taxes, so that the American government could impose unfair and exorbitant taxes. George Washington commanded a tiny contingent of fighters known as the Minute Men – fighting for American liberty.

MINUTE MAN: (Pg 20) (reading from flyer) Expel the Evil Empire from North America and meet chick. High frostbite tolerance a plus. No tea drinkers, please. Be all that you can be. Apply in person – Valley Forge

REED: (Pg 18) (singing) We represent the Lexington League
The Lexington League
The Lexington League
And in the name of the Lexington League . . .
We wish to welcome you to Valley Forge!

ADAM: (Pg 22) So the rebel troops brought the Brits to their knees! And finally in Yorktown in Fall ’81, the British surrendered – The Yankees had won!

REED: imme an M! Gimme an E! Gimme an R! I! C! Gimme an A! Whtzzat spell? ‘MURRICA! ******

MADISON: (Pg 23) I can’t believe the Bill of Rights is due tomorrow.

FRANKLIN: Now, as the world’s first democracy, I think we should guarantee Freedom of Religion, Freedom of the Press, and Freedom of Speech.

MADISON: If you guarantee all those rights, people are going to be saying all kinds of crazy stuff and pissing each other off.

FRANKLIN: Well, then, let’s give everyone the right to carry a gun to shot each other, and the right to a fair and speedy trial by a jury of their peers after they do. Are we in agreement?

MADISON: Totally! . . . . [Until . . . . }

REED: (Pg 31) The Civil War!

ANNOUNCER: (Pg 33) The war was the bloodiest in the history of the nation. At the heart of the fighting was the issue of slavery. And when abolitionist Abraham Lincoln (cough “Republican”) became President in 1861, the South seceded from the Union. (Pg 34) But in the end, the South surrendered, and they all lived happily ever after. Except for Abraham Lincoln who was shot in the head by John Wilkes Booth. ******

(Pg 37-38) (Marching in place while saluting, hum a few bars of “Over There” *)

SOLDIER: World War I – The Trenches (jumps into a trench somewhere in France. Mime a gun and peak out grimly over the edge of the trench) You think they’re still out there, Sarge? It’s pretty quiet out there.

SARGE: Yeah. Too quiet . . . They’re out there. Every last one of them! (he peers through binoculars) My God!

SOLDIER: We’re outnumbered a hundred to one! (Pg 39) (Panicking) I gotta get outa here! I’m too young to die!

SARGE: Calm down, soldier! (Slaps him) (Pg 37) We’re expendable. We got a job to do and we do it. Case closed!

SOLDIER: But don’t you see?! We’re trapped! We’re just cannon fodder for the military-industrial complex!

SARGE: (Pg 40) All right, we’re going over the top! Let’s go!!! (He leaps out of the foxhole and is instantly struck down) ******

ANNOUNCER: (Pg 41) Dateline 1919. The Treaty of Versailles is signed. The Great War is over. 18th Amendment ratified, creating Prohibition. And the Golden Ae of Radio unites the country from sea to shining sea! Until . . . .[World War II] (Pg 46) Suddenly, over the hills in a cloud of dust and the sound of a thundering wheelchair, appears Franklin Delano Roosevelt!

FDR: My fellow Americans, the only thing we have to fear is fear itself. We hereby declare war on the Axis powers!

ANNOUNCER: . . . and now back to the exciting conclusion of Rock Fury, Super GI!

HITLER: Look! Ze alies are marcing into Berlin. Zey are falling right into my trap. Now I wll press zis button, firing the secret Uberveapon zat vill vipe out ze whole Allied force. Ha-ha-ha-ha! (Woosh sound, the sound of a man flying) (Pg 47) Ach, Vut is zat noise? Oh, no! It’s a bird, it’s a plane . . .

ROCK FURY: No! It’s Rock Fury, Super GI! Your jib-dancing days are over, little man! In its greed and lust for power, Germany has tried to take over an entire continent.

HITLER: But isn’t zat vut ze US did in Norze America?

ROCK FURY: We didn’t try to wipe out an entire race of people!

EVA BRAUN: Vut about ze Indians?

ROCK FURY: Well, we don’t lock people away in concentration camps.

EVA BRAUN: Vut about ze Japanese-Americans on the Vest Coast?

ROCK FURY: (Unable to answer, he addresses the audience) (Pg 48) Well, thank goodness we won this war; otherwise, the German and Japanese economies would dominate the world!

HAWKEYE PIERCE: Help, Help!

ROCK FURY: Wait! My super hearing is picking up Alan Alda calling for help in Korea. Rock Fury, Super GI is off once again to battle for truth, justice and American markets! (Whoosh sound as he flies away, followed by a news ticker sound)

ANNOUNCER 2: This just in. Atom bombs dropped on Hiroshima and Nagasaki. Over two hundred thousand dead. That report in just a moment, but first it’s time to play Queen for a Day! – The Game show which celebrates the achievements of American women! (cheering and game show music) *****

GAME SHOW HOST: (Pg 50) Name the brave seamstress from Montgomery, Alabama, who refused to move to the back of the bus and jump-started the American civil rights movement?

CONTESTANT: (Pg 51) Whoopi Goldberg? (buzzer sounds) *****

ADAM: (Pg 54-55) Okay . . . Postwar America – Film Noir Ending! (dons an overcoat and fedora and steps out of the scene, noir style)

SPADE: The name’s Diamond, Spade Diamond. I’m a private eye! (steps back into scene)

CONSPIRATOR GUY: (Pg 55) If you know what’s good for you, you’ll drop this case before you start it. Unless you want to find out the truth!

SPADE: (Pg 60) Who are you!?

CONSPIRATOR GUY: (Pg 55) Just call me the Conspirator Guy. (Pg 68) You want to know who caused the Cold War? Who benefited? (Whispering) The Generals!

SPADE: The military?

CONSPIRATOR GUY: No! No! General Motors, General Electric. They caused the Cold War! And . . . And . . . I shot JFK, not Lee Harvey Oswald! (Pg 69) I shot Bobby Kennedy, too. And Martin Luther King. And Malcolm X!

SPADE: Wow.

CONSPIRATOR GUY: And I shot Jr, and invented the AIDS virus and I whacked Nancy Kerrigan on the knee . . . It’d whack her again if I had half a chance . . . and I shrank the bloody glove so it wouldn’t fit OJ anymore, and I told President Clinton “Go ahead! She’s an intern! Who cares?” (Spade shoots Conspirator Guy with his finger gun)

SPADE: (Steps our of the scene) I had to put him out of my misery. So there it was. The Cold War was over and Communism was dead . . . well, except for a billion people in China. *****

REED: (Pg 70) Thank you. Thank you. That was the Complete History of America! Is there anything we need to add here historically?

ADAM: Well, we left out a few people. Kristi Noem, Pam Bondi, Pete Hegseth, Donald Trump, Jeffrey Epstein?

AUSTIN: (Considers for a moment) Not that important.

ADAM: COVID-19? Constitutional rights? Immigration Enforcement by ICE?

AUSTIN: To mask or not to mask . . . that is the question!

ADAM: (PG 71) I’m [insert name]

AUSTIN: And I’m [Insert name] and that’s history!
```

---

## IC-1126: The Complete Works of William Shakespeare (abridged) [revised]

- Title: The Complete Works of William Shakespeare (abridged) [revised]
- Author (byline): Adam Long, Daniel Singer and Jess Winfield (The Reduced Shakespeare Co)
- Work: The Reduced Shakespeare Company’s The Complete Works of William Shakespeare
- Publisher: Applause Theatre Books
- Publication date as stated: 1994
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: PLAYWRIGHTS’ NOTE, JESS, A/JULIET, D/NURSE, J/FRIAR, D/ROMEO, DANIEL, ADAM, D/WITCH, J/MACBETH, A/MACDUFF, D/CAESAR, A/SOOTHSAYER, J/ANTONY, D/RICHARD II, A/HENRY VI, D/ANNOUNCER, A/ANNOUNCER, D/LEAR, D/RICHARD III, CHEERLEADER
- Teaser before the introduction: Yes
- Spoken words (computed): 1618
- Already set (do not supply): none

### Source block (context only)

```text
Author: Adam Long, Daniel Singer and Jess Winfield
ISBN: 978-1617741555
Publisher: Applause
Date (Month/Year): Feb 2011
Four Lines on Page 4 were taken from the original version of this play
Author: Jess Borgeson, Adam Long and Daniel Singer, edited by Professor J.M. Winfield
Title: The Reduced Shakespeare Company’s The Complete Works of William Shakespeare
(abridged) (Pg 36)
ISBN: 978-1557831576
Publisher: Applause Theatre Books
Date (Month/Year): 1994
```

### Introduction (context only: never use it for content warnings)

```text
(Pg 1-2) Hello and welcome to this performance! [I am] about to attempt a feat which [I] believe to be unprecedented in the history of civilization. To capture, in a single theatrical experience, the magic . . . The genius . . . The towering grandeur of ‘The Complete Works of William Shakespeare.’ [Now, we know that] (Pg 4) our society’s capacity to comprehend the genius of William Shakespeare has been systematically *compromised* by soap operas . . . and vandalized by video games . . . But have no fear! (In the manner of a fire-and-brimstone evangelist) [I am] on a mission from God to spread the holy word of the Bard to the masses. (Pg 6) Now, without further ado, I am proud to present.

The Complete Works of William Shakespeare (abridged)[revised] by Adam Long, Daniel Singer
```

### Performance text (classify this)

```text
PLAYWRIGHTS’ NOTE: The script is written for three actors. In performance, the actors should substitute their own names for “Adam,” “Jess,” and “Daniel.” Where Shakespearean characters appear in the script, the character name is preceded by the actor’s initial (ie A/Juliet means Adam is playing Juliet, etc.) “Shakespearean” dialogue appears in double quotation marks (“”). Because the show comments on contemporary events to place Shakespeare’s works in a modern context, it’s absolutely essential to keep the show fresh and timely by updating the many topical references as events warrant. Have some fun and come up with your very own put-downs of annoying famous people where required . . . And do it FASTER!

and Jess Winfield.

JESS: (Pg 14) From Tybalt's death onwards, the lovers are curs’d, despite the best efforts of Friar and Nurse; their fate pursues them, they can't seem to duck it. . . And at the end of Act Five, they both kick the bucket. (Juliet and Nurse enter)

A/JULIET: (Pg 15) “O, it is my nurse. Now nurse, what news?”

D/NURSE: Alack the day! He’s gone, he’s kill’d, he’s dead! O Romeo! I saw the wound with my own eyes.

A/JULIET: Is Romeo slaughter’d and is Tybalt dead?

D/NURSE: No, Romeo kill’d Tybalt, he is banished!

A/JULIET: God! Did Romeo's hand shed Tybalt's blood?

D/NURSE: “It did, it did, alas the day it did." (She wails hysterically, runs two small laps around Juliet and exits – Jess enters as FRIAR LAURENCE)

A/JULIET: O, Friar Laurence! Romeo is banished and Tybalt is slain and . . .

J/FRIAR: (bored, he interrupts) “Take thou this vial, and this distilled liquor drink thou off. And presently though thy veins shall run a cold and drowsy humor.”

A/JULIET: (Pg 16-17) (Takes bottle and drinks) O, I feel a cold and drowsy humor running through my veins . . . (Friar exits. Juliet becomes dizzy) Mm, pretty colors! Uh-oh . . . (Juliet vomits) There, I feel much better. (Collapses suddenly. ROMEO enters. He sees JULIET and rushes to her prone body, accidentally stepping on her crotch while doing so)

D/ROMEO: “O, no! (Adam clutches his privates in agony) / My love, my wife! / Death, that hath suck'd the honey of thy breath, / Hath no power yet upon thy beauty. / Juliet, why art thou yet so fair?”

A/JULIET: Dunno, lucky I guess.

D/ROMEO: “Here's to my love. (He drinks from his poison bottle.) / O true apothecary! Thy drugs are quick. / Thus, with a kiss, I die ... (Just as Daniel leans in to kiss Adam, Adam burps. Now Daniel has no wish to kiss Adam. He struggles with the problem for a moment, takes another swig of poison, and finally kisses him) Thus with a kiss, I die.” (ROMEO dies. JULIET wakes up, stretches, scratches her butt, and looks around.)

A/JULIET: Good morning. “Where, O where is my love? (She sees him lying at her feet and screams) "What's this? A cup, closed in my true love's hand? Poison I see hath been his timeless end. O, churl. Drunk all and left no friendly drop to help me after? Then I'll be brief. O happy dagger! This is thy sheath." (She unsheathes ROMEO'S dagger and does a doubletake: the blade is tiny) That's Romeo for ya.

(JULIET stabs herself. She screams, but, to her surprise, she does not feel injured. She looks for a wound and can't find one. Finally, she realizes that the blade is retractable. This is a cause for much joy. She stabs herself gleefully in the torso and on the crown of the head. Finally, she flings her happy dagger to the ground)

A/JULIET: “There rust and let me die!”(Dies)

JESS: Epilogue!

DANIEL: “For never was there a story of more woe / Than this of Juliet and her Romeo”

(singing) And Romeo and Juliet are deeeeaad . . . !
TRANSITION
I shall now move on to explore the genius evident in Shakespeare's more mature plays, as I
present his dark and brooding tragedy, 'Othello, the Moor of Venice.’

ADAM: (He beat-boxes, then raps) (Pg 21-24) Here's the story of a brother by the name of Othello / He liked white women and he liked . . . limoncello.

JESS: (catching on quickly) Oh, yeah, yeah. Uh . . . / And a punk named Iago who made hisself a menace / 'Cos he didn't like Othello, the Moor of Venice.

ADAM: Now Othello got married to Des-demona,

JESS: But he took off for the wars and he left her alone-a.

ADAM: It was a moan-a

JESS: A groan-a

ADAM: He left her alone-a.

DANIEL: (finally catching on and joining in) He didn't write a letter and he didn't telephone-a! /

(They all get into it, making boom-box noises and adopting a hip-hop attitude) Now Othello loved Desi like Adonis loved Venus.

JESS: And Desi loved Othello cuz he had a big . . .

DANIEL: SWORD!

ADAM: But Iago had a plan that was clever and slick / He was crafty

JESS: He was sly

DANIEL: He was sort of a _____ (Not wanting to say it)

ADAM: He say 'I'm gonna shaft the Moor.'

DANIEL: How you gonna do it? Tell us!

ADAM: Well, I know his tragic flaw is that he's

JESS: Too damn jealous!

ADAM: I need a dupe / I need a dope / I need a kind of a shmoe . . .

JESS: So he find a chump sucker by the name o' Cassio.

DANIEL: And he plants on him Desdemona's handkerchief

ADAM: So Othello gets to wonderin’ just maybe if . . . While he been out fightin’

DANIEL: Commandin’ an army

JESS: Are Desi and Cass playin hide the salami?

ADAM: Sa-sa-sa-salam Salaaammii!

DANIEL: So he come back home an’ he mother the beeyotch. (Can “bleep” out this word”)

JESS: An’ he thinks he pulled it off, without a heeyotch.

ADAM: But there's Emilia at the do’.

JESS: Who we met in Act Fo’.

DANIEL: Who say, 'You big dummy, she weren't no whore. She was JESS: Pure

DANIEL: She was JESS: Clean

DANIEL: She was JESS: Virginal, too,

DANIEL: So why'd you have to go and make her face tum blue?

ADAM: And Othello say:

JESS: ‘Damn, this is getting’ pretty scary.'

DANIEL: So he pulled out his blade and committed hari-kiri. (Jess mimes hara-kiri on himself and twitches in death throes) [NOTE the following 4 lines are from the original (Pg 36), rather than the revised script]

ADAM: Iago got caught, but he prob'ly copped a plea,

JESS: (Singing) [And he] Loaded up his bags,

DANIEL: And moved to Beverly . . .

JESS: . . .Hills, that is. (Bows and elaborate handshakes all round.)

ADAM: (Raised-fist salute) (Pg 28) Tragedies! (Daniel clears his throat because that was inappropriate; Adam with a much smaller fist-salute) Tragedies.

DANIEL: ‘The Scottish play!’

ADAM: Oh yeah! Mac –

DANIEL: Shhhhh! Don’t say it! It’s cursed. It’s bad luck to say the name of that show unless you’re performing it. That’s why we refer to it is ‘The Scottish Play.’

ADAM: But we are performing it.

DANIEL: (Pg 29-31) (shrugs) We now present our authentically Scottish production of . . . Macbeth!

D/WITCH: “Double, double, toil and trouble.” (In nearly impenetrable Scottish accents)

J/MACBETH: Stay, ye imperrrfect macspeaker. Tell me more.

D/WITCH: Macbeth, Macbeth, beware Macduff. / None of woman born shall harm Macbeth / Till Birnam Wood come to Dunsinane, don't ye know. (WITCH exits. ADAM enters as MACDUFF)

J/MACBETH: Och, that's dead great. Then macwhat macneed macfear of Macduff?

(MACDUFF wields his sword and throws a two-fingered gesture at MACBETH)

A/MACDUFF: See YOU, Jimmy, (a popular Scottish oath) and know / That Macduff was from his mother's womb untimely ripped!” / What d'ye think about that? (They spar)

J/MACBETH: Och! I do nae like it, but I support a woman’s right t’choose! Lay on, ye great haggis-breath! (They fence)

A/MACDUFF: Ah, Macbeth! Ye killed my wife, ye murdered me wee bairns, and ye did poop in my soup.

J/MACBETH: Och! I didnae!

A/MACDUFF: Och, aye, ye did. I had t' throw half of it away. (MACDUFF chases MACBETH offstage where MACBETH'S scream is abruptly cut off. MACDUFF re-enters carrying a severed head) “Behold where lies the usurper's cursed head.” Macbeth, yer arse is out the windie. (Dropkicks the head offstage.) And know, That never was there a story of blood and death / Than this, o' Mister and Mrs. Macbeth. Thankee. (Exits)(JESS enters)

JESS: Meanwhile, in ancient Rome, Julius Caesar was a much beloved tyrant. (ADAM enters) All hail, Julius Caesar! (DANIEL enters as JULIUS CAESAR)

D/CAESAR: Hail, citizens!

JESS: . . . Who was warned by a soothsayer . . .

A/SOOTHSAYER: "Beware the Ides of March."

JESS: The great Caesar, however, chose to ignore the warning.

D/CAESAR: What the h*** are the Ides of March?

A/SOOTHSAYER: The 15th of March.

D/CAESAR: Why, that's today. (ADAM stabs him repeatedly. He falls) “Et tu, Brute?” (CAESAR dies. JESS becomes MARK ANTONY, orating over the body.)

J/ANTONY: Friends, Romans, countrymen, lend me your ears. I come to bury Caesar.

ADAM: (Pg 34-38) Bo-ring!

DANIEL: This is the kind of stuff that kids hate to study in school because it's so boring.

ADAM: I'm sorry, guys, but I promised I would not do dry, boring Shakespeare. I love these people, and I don’t want to see them get turned off to Shakespeare. (gesturing to audience) That's what happened to me. When I was in school, and we were supposed to be studying Shakespeare, I'd be looking out the window at all the kids playing ball, and I'd be thinking to myself, 'Why can't this Shakespeare stuff be more like sports?'

DANIEL: How do you mean?

ADAM: Well, sports are exciting. Engaging. I mean, take the histories, for example. With all those kings knocking each other off, running up and down the field, the throne passing from one guy to the next – it’s exactly like football, but you do it with a crown.

DANIEL: Hey, they are kinda similar, aren’t they? Okay, line 'em up. Let's kick some royal . . .

(Jess pulls out a whistle and blows it)(They line up in a football formation – then like a quarterback calling signals) Twenty-five! Forty-two! Richard the Third! Henry the Fourth, Part One, Part Two . . . HUT!

JESS: . . . And the crown is snapped to Richard the Second, that well-spoken fourteenth-century monarch. He's fading back to pass, looking for an heir downfield, but there's a heavy rush from King John. (JESS as KING JOHN stabs DANIEL as RICHARD)

D/RICHARD II: "My gross flesh sinks downwards!"

JESS: The crown is in the air, and Henry the Sixth comes up with it!

A/HENRY VI: Victory is mine!

D/ANNOUNCER: But he's hit immediately by King John. Oh no! He’s cutting Henry the Sixth into three parts, that’s gotta hurt! (KING JOHN slices up HENRY) This could be the end of the War of the Roses cycle! (KING JOHN grabs the crown and runs in place with it)

A/ANNOUNCER: King John is in the clear . . . He's at the forty, the thirty, the twenty – (DANIEL sneaks up from behind and pantomimes pouring something into JESS’s mouth) -- ooh, but he's poisoned on the ten yard line! (DANIEL snatches the crown and puts it on. JESS exit.) Looks like he's out for the game. Replacing him now is number seventy-two, King Lear.

D/LEAR: To Regan and Goneril I hand off my kingdom. Cordelia, you go long . . . (JESS re-enters as referee, throwing a penalty flag and blowing a whistle.)

A/ANNOUNCER: There’s a penalty marker! (JESS makes a hand signal and points at LEAR) Fictional character on the field. Lear is disqualified, and he's not happy about it.

D/LEAR: (Disappointed) Bastards! (Jess “bleeps” the profanity)

ADAM: Lining up now is that father-son team of Henry the Fourth and Prince Hal. Center snaps to the quarterback . . . quarterback gives to the hunchback. It looks like Richard the Third's limp is giving him trouble.

D/RICHARD III: "A horse, a horse! My kingdom for a horse!"

A/ANNOUNCER: There’s a pile-up on the field.

D/ANNOUNCER: FUM-BLE!!! And Henry the Eighth comes up with it. He's at the fifteen, the ten. . . He stops at the five to chop off his wife's head . . . TOUCHDOWN for the Red Rose! Oh, my! You gotta believe this is the beginning of a Tudor Dynasty!

CHEERLEADER: Henry the Fifth, Richard the Third, the whole royal family’s frickin’ absurd! Goooo, [insert local sports team] Yay!

ADAM: Can I have some house lights please? (consults a large book of SHAKESPEARE PLAYS)

DANIEL: What are you doing?

ADAM: I just want to check the list of plays. I think we might have done' em all already. Yea, see, we did all the histories just now. 'Romeo and Juliet' we did-

DANIEL: (looking over his shoulder) 'Julius Caesar,' right-

ADAM: We rapped 'Othello,' Lear was in the football game, 'Macbeth' we did with Scottish accents.

DANIEL: The comedies ? . . . .

ADAM: Eh . . . let’s skip [them]. And that’s it, right? That’s all of them!

JESS: Hey, no, you guys . . . (Points to a title on the list)

DANIEL: Hamlet!

ADAM: Shakespeare didn’t write Hamlet. (Shocked looks from the others) What’s it about?

JESS: You know, the young prince struggling with his conscience after his uncle murders his father?

ADAM: Dude, that’s The Lion King. (Pg 39) I don’t wanna do it!

JESS: Look, our show’s called The Complete Works of William Shakespeare.

ADAM: Okay, so we'll call it 'The Complete Works of William Shakespeare Except Hamlet.'

(Looks from the others)

ADAM: You can't make me do it! You can't! (Pg 40) (ADAM springs toward the exit)

JESS: Get back here, you Shakespeare weenie!
```

---

## IC-1127: The Day the Crayons Quit

- Title: The Day the Crayons Quit
- Author (byline): Drew Daywalt
- Work: Not specified
- Publisher: HarperCollins
- Publication date as stated: July 2014
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, RED, PURPLE, BEIGE, GRAY, WHITE, BLACK, GREEN, YELLOW, ORANGE, BLUE, PINK, PEACH
- Teaser before the introduction: No
- Spoken words (computed): 1075
- Already set (do not supply): none

### Source block (context only)

```text
Author: Drew Daywalt
ISBN: 978-0007513765
Publisher: HarperCollins
Date (Month/Year): July 2014
```

### Introduction (context only: never use it for content warnings)

```text
I have a secret . . . (whispering) I still like to color! And even though my mom doesn’t put my pictures on the refrigerator anymore . . . I still color. Sometimes in coloring books (which I get in my stocking for Christmas each year) and sometimes pictures I draw myself. I love crayons!!!! And you know what . . . I’m proud of it. Heck, they are even making ADULT coloring books now! I saw them at the craft store, so I know I’m not the only one. But then I got to thinking . . . what if Crayons could talk? What would they say? How do they feel? The Day the Crayons Quit by Drew Daywalt.
```

### Performance text (classify this)

```text
NARRATOR: One day in class, Duncan went to take out his crayons and found a stack of letter with his name on them.

RED: Hey Duncan, It’s me RED crayon. We need to talk. You make me work harder than any of your other crayons. All year long I wear myself out coloring fire engines, apples, strawberries and everything else that’s Red. I even work on holidays! I have to color all the Santas at Christmas and all the hearts on Valentine’s day! I need a rest! Your overworked friend, RED crayon.

PURPLE: Dear Duncan, All right, listen, I love that I’m your favorite crayon for grapes, dragons and wizards’ hats, but it makes me crazy that so much of my gorgeous color goes outside the lines. If you don’t start coloring inside the lines soon . . . I’m going to completely lose it. Your very neat friend, PURPLE crayon.

BEIGE: Dear Duncan, I’m tired of being called “light brown” or “dark tan” because I am neither. I am BEIGE and I am proud. I’m also tired of being second place to Mr. BROWN crayon. It’s not fair that BROWN gets all the bears, ponies and puppies while the only things I get are turkey dinners (if I’m lucky) and wheat, and let’s be honest – when was the last time you saw a kid excited about coloring wheat? Your BEIGE friend, BEIGE crayon.

GRAY: Duncan, GRAY crayon here. You’re killing me! I know you love elephants and I know that elephants are gray, but that’s a lot of space to color in all by myself. And don’t even get me started on your rhinos, hippos and humpback whales. You know how tired I am after handling one of those things? Such BIG animals. . . baby penguins are gray, you know. So are very tiny rocks . . . pebbles. How about one of those once in a while to give me a break? Your very tired friend, GRAY crayon.

WHITE: Dear Duncan, You color with me, but why? Most of the time I’m the same color as the page you are using me on – WHITE. If I didn’t have a black outline, you wouldn’t even know I was there! I’m not even in the rainbow. I’m only used to color snow or to fill in empty space between other things, and it leaves me feeling . . . well . . . empty. We need to talk. Your empty friend, WHITE crayon.

BLACK: Hi, Duncan, I hate being used to draw the outline of things . . . things that are colored in by other colors, all of which think they’re brighter than me! It’s not fair when you use me to draw a nice beach ball and then fill in the colors of the ball with all the other crayons. How about a BLACK beach ball sometime? Is that too much to ask? Your friend, BLACK crayon.

GREEN: Dear Duncan, As GREEN crayon, I am writing for two reasons. One is to say that I like my work – loads of crocodiles, trees dinosaurs and frogs. I have no problems and wish to congratulate you on a very successful “coloring things GREEN” career so far. The second reason I write is for my friends, YELLOW crayon and ORANGE crayon, who are no longer speaking to each other. Both crayons feel they should be the color of the sun. Please settle this soon because they’re driving the rest of us crazy! Your happy friend, GREEN crayon.

YELLOW: Dear Duncan, YELLOW crayon here I need you to tell ORANGE crayon that I am the color of the sun. I would tell him, but we are no longer speaking. And I can prove I’m the color of the sun too! Last Tuesday you used me to color in the sun on your “Happy Farm” coloring book. In case you’ve forgotten, it’s on page 7. You can’t miss me. I’m shining down brilliantly on a field of YELLOW corn! Your pal and the true color of the sun, YELLOW crayon.

ORANGE: Dear Duncan, I see YELLOW crayon already talked to you, the big whiner. Anyway, could you please tell Mr. Tattletale that he IS NOT the color of the sun? I would, but we’re no longer speaking. We both know I am clearly the color of the sun because on Thursday you used me to color the sun on BOTH the “Monkey Island” and the “Meet the Zookeeper” pages in your “Day at the Zoo” coloring book. Orange you glad I’m here? Ha! Your Pal (and the real color of the sun). ORANGE crayon

BLUE: Dear Duncan, It has been great being your favorite color this past year, and the year before, and the year before that! I have really enjoyed all those oceans, lakes, rivers, raindrops, rain clouds and clear skies. But the bad news is that I am so short and stubby, I can’t even see over the railing in the crayon box anymore! I need a break! Your very stubby friend, BLUE Crayon

PINK: Duncan, Okay, listen here, kid! You have not used me ONCE in the past year. It’s because you think I am a girls’ color, isn’t it? Speaking of which, please tell your little sister I said thank you for using me to color her “Little Princess” coloring book. I think she did a fabulous job of staying inside the lines! Now, back to us. Could you please use me sometime to color the occasional pink dinosaur or monster or cowboy? Goodness knows they could use a splash of color. Your unused friend, PINK crayon

PEACH: Hey, Duncan, It’s me, PEACH Crayon. Why did you peel off my paper wrapping?? Now I’m naked and too embarrassed to leave the crayon box. I don’t even have any underwear! How would you like to go to school naked? I need some clothes. HELP! Your naked friend, PEACH crayon

NARRATOR: Well, poor Duncan just wanted to color . . . and of course he wanted his crayons to be happy. And that gave him an idea. (pantomime Duncan coloring with all his crayons)

TRANSITION He created a GREEN and BLUE ocean, with an ORANGE whale giving a lift to two small GRAY penguins, a PINK policeman, a BLUE crocodile and a GREEN monkey. An ORANGE sun shone down from a YELLOW sky sporting a BLACK rainbow. PURPLE and PINK dragons and a WHITE polar bear frolicked in the waves, while a RED Santa watched a PINK bus driver give a floating lift to a GREEN pig. And as for BEIGE and PEACH . . . well . . . he tried!

NARRATOR: When Duncan showed his teacher his new picture, she gave him an A for coloring . . . . and an A+ for creativity!
```

---

## IC-1128: Disney Mom Group Therapy

- Title: Disney Mom Group Therapy
- Author (byline): Mo Gaffney and Kathy Najimy
- Work: Parallel Lives: The Katy & Mo Show, Pg 67-72
- Publisher: Dramatists Play Service
- Publication date as stated: Jan 1993
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: DR. KINCAID, MONIQUE, ALL, DOLORES, BETTY, CORAL, ETHEL, MRS. JUMBO, BARBRA, CRUELLA
- Teaser before the introduction: Yes
- Spoken words (computed): 1243
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mo Gaffney and Kathy Najimy
Book: Parallel Lives: The Katy & Mo Show, Pg 67-72
ISBN: 978-0822213086
Publisher: Dramatists Play Service
Date (Month/Year): Jan 1993
```

### Introduction (context only: never use it for content warnings)

```text
Let’s face it . . . no one is more in need of a support group than the poor mothers of Disney characters. When the first question asked upon entering the room is “Are you alive?” you know you may be in for a bumpy ride. Let’s listen in and find out a bit more about DMGT. For those of you opposed to acronyms, that’s Disney Mom Group Therapy by Mo Gaffney and Kathy Najimy.
```

### Performance text (classify this)

```text
DR. KINCAID: (Pg 67-72) Hello everybody, welcome to the Disney Mom’s Support Group. Are we all here?

MONIQUE: Excuse me, am I in zee right room?

DR. KINCAID: Are you alive?

MONIQUE: Well, yes . . . I suppose . . .

DR. KINCAID: I mean in the movie, are you alive or do you die in the beginning or are you dead when it starts?

MONIQUE: Well, they never actually make mention of me.

DR. KINCAID: I bet you’re already dead then. And your name is?

MONIQUE: Monique. Monique Andthebeast.

DR. KINCAID: Everybody, this is Monique Andthebeast.

ALL: WELCOME MONIQUE!

DR. KINCAID: And you’re the mother of . . . ?

MONIQUE: Belle, well Beauty. Walt has some kind of Jones for renaming his girls “Beauty.” A lot to live up to if you ask me . . .

DOLORES: Ya got that right, sister . . .

MONIQUE: It’s like being named “Stacked.” Sacre Blue – her name is Belle. And no, the only women in the film are a witch, a teapot and a hutch . . . (She starts to cry) He had her being raised by a pot and some old furniture. . .

DOLORES: My name is Dolores . . . Dolores Deer, mother of Bambi . . . My son was raised by a rabbit, Monique!

MONIQUE: No, Dolores!

DOLORES: And a skunk for Christ’s sake.

MONIQUE: Ooh, I just want to find that Waltsicle and thaw his *butt* out!

DR. KINCAID: No, now . . . you’re among others like you . . . you’re not alone . . . Most of the Disney girls were not raised by their mothers. Right, ladies? (group murmurs) We are delighted to have you in the group, Monique.

MONIQUE: (Sings) Bonjour, bonjour, it’s nice to meet you.

DR. KINCAID: Why don’t we all do introductions and then we can start? . . . Betty? Why don’t you start? (Snickers)

BETTY: (Sings) I’m wishing, for the one I love, to find me . . .

DOLORES: Shut it, Bet-tee!!!

BETTY: Sorry. I’m Betty. Mother of Snow, Betty White. (Snickering) I know, I know, I’ve heard all the jokes. Dead at the beginning.

ALL: WELCOME, BETTY!

CORAL: Hi, I’m Coral Clownfish, mommy to Nemo. I horrifically die at the beginning as well. I brought some Shark sugar cookies, if anyone’s interested.

ALL: WELCOME, CORAL!

DOLORES: Dolores Deer, mother of Bambi. Shot dead in the first then minutes. Yeah, yeah I know, “Welcome Dolores.”

ETHEL: (Sings) Hello, Dolly!

DOLORES: All right, Ethel . . .

ETHEL: I’m Ethel, Ethel Mermaid, mother of Ariel. I’m dead from the beginning. And there’s some fried calamari on the table as well.

ALL: WELCOME, ETHEL!

MRS. JUMBO: (Elephant trumpet) Jumbo, I am Mrs. Jumbo.

ALL: WELCOME, MRS. JUMBO!

DR. KINCAID: Okay, that’s everybody, let’s get started. Oh, and just so you all know, Habiba and Whaddad, Jasmine’s and Aladdin’s moms, couldn’t be here because they are at a burqa burning. (Cheers) Okay then, why don’t we start with a free form? And again, Betty White, could you start? Last week you were telling us how traumatic it was when they took Snow to the forest.

BETTY: Well, Doctor, for starters my daughter’s name is Snow WHITE and they send her out to the forest with no sunscreen, and you’re gonna think I am making this up, Doc. . . but Walt has her meet and move in with seven little men, clean and cook for them all, whistle the s*** out of herself, east a Jim Jones apple, fall asleep and then of course . . .

ALL: A handsome prince comes and kisses her and they live happily ever after! (Pause . . . then they all burst out laughing)

BETTY: A teenage girl and seven little men! You find that kind of *crap* on the Internet.

DR. KINCAID: Thank you, Betty, that’s a good start. Coral Clownfish, why don’t you go next?

ETHEL: Sing out, Coral!

CORAL: I just want to say, “NOT how it happened!” Would I show a hungry barracuda my nest? No!!! “Hey, big mean killer, come on in, eviscerate my children, then slice me open like a lute fish!” Oh, and just so you know that coffee is hot and I baked some fresh biscuits.

ETHEL: (Sings) There’s no biscuits like fresh biscuits . . .

DR. KINCAID: Ethel Mermaid, it seems like you have something to say?

ETHEL: Okay, well, again, I’m Ethel Mermaid, mother of Ariel. First off, I would NEVER let my daughter give up her voice and half her body for some . . . for some guy she’d never even met. I mean, she saw him on a boat! He could have been Dahmer on a day cruise for the love of stage right. What’s up with that?

DR. KINCAID: Okay, Ethel, we hear you. Dolores, you look raring to go.

DOLORES: Ya think? Well, first off I’m killed in front of my baby . . . yep . . . by some damn hunter. Now there’s a challenging SPORT huh? There I am – an innocent, graceful doe drinking crystal water out of a sparkling stream and some A-hole sneaks up from behind, takes a bead on me and blam! Pops a cap! And can I just say “Great Prince of the Forest?” The guy lit out the second the kid was born! I mean you can’t see that *stuff* on Rikki!

MONIQUE: Oh, Dolores, that is horrible . . .

DR. KINCAID: It’s good to get it out. Oh, look who’s here. Barbra – Welcome.

BARBRA: (Drunk) Sorry, (to Ethel) did I step on your tail? Sorry, sorry . . . It’s a b*** to park a pumpkin in a compact space . . . Waddya bet my door’s gonna get bruised . . . again! My name is Barbra and I’m an alcoholic . . .

ALL: WELCOME, BARBRA!

DOLORES: Wrong meeting Barb . . . This is the Disney thing . . .

BARBRA: Ooops. Sorry. My name is Barbra, my daughter is Cinder . . . I’m Barbra Rella and my daughter Cinder was allergic to manimals . . . he had her singing her guts out in a tiny room with birds and mice crawling all over her getting her dressed . . .

DOLORES: I hate mice!

BARBRA: Me too! And they went on and on about how much she missed her father . . . What about me? What about me?

CORAL: Can I get you some coffee?

BARBRA: Yes, just a drop of Kahlua . . . And how about all those jabs from Walt about me? She turns to s*** at twelve o’clock? Cinder runs down the 12 STEPS? Got it Walt! (To Coral) Thank you . . . and to top it all off, she runs off with that picky Prince with a shoe fetish . . . Only feet that can fit the shoe – Only feet that can fit the slipper!

DR. KINCAID: Thanks for that Barbra, that was very revealing. All right, who hasn’t gone yet. .? Mrs. Jumbo? What’s wrong, Aristocat got your tongue?

ETHEL: Sing it, Jumby!

MRS. JUMBO: Ohhh, Lordy . . . it was so long ago it’s hard to remember . . .

ETHEL: But you’re an elephant . . . you’re supposed to –

MRS. JUMBO: No stereotypes please, Ethel! I was a proud young elephant . . . ripped from the jungle by THE MAN and brought shackled to the circus to “perform.” It was humiliating. Then my boy was born . . . beautiful. Big trunk, big ears, big . . . he was beautiful. And just because he didn’t look like some small-featured ferret they made fun of him. The last straw was when some little brat tugged on his ears and I lost my s***! They labeled me “crazy” and sent me to the slammer. I didn’t even make it through the first twenty pages, man.

ETHEL: Say it from your soul, sister!

MRS. JUMBO: That’s my story

DR. KINCAID: Thank you, Mrs. Jumbo, that was truly moving. Now, I have to say I certainly sympathize with you women, but I must remind you that Disney wasn’t the original author on most of your stories . . .

CRUELLA: Yes, but he picked them and he edited the wretched things!

DR. KINCAID: I’m sorry, you are?

CRUELLA: Cruella DeVille, Jumbo’s lover. We met in the big house. (Mrs. Jumbo makes an elephant noise) Darlings.

ALL: WELCOME, CRUELLA!

DR. KINCAID: Okay, last thing on the agenda: Princes (Groans and ad-lib reactions to the following questions) How many daughters kissed by the handsome prince? How many taken away on a horse? How many never spoke to the guy before they married him? On, two . . . slow down, ladies . . . slow down. Oh gosh, time’s up. Great session today, Ladies. And now it’s time for . . . meds!

BARBRA: WOOHOO!

DR. KINCAID: And don’t forget, a spoonful of sugar . . .

ALL: Helps the medicine go down! (Hums “Spoonful of Sugar”)
```

---

## IC-1129: DMV Tyrant

- Title: DMV Tyrant
- Author (byline): Christopher Durang
- Work: Naomi In the Living Room and Other Short Plays
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Oct 1988
- Event as filed: Humorous Interpretation
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
Probably the most frightening phrase you can hear at the DMV is, “It’s a clerical error.” This phrase can mean almost any imaginable horrible thing you can conjure up. It can mean that you’ll have to come back and waste another day. It can mean that you’ll have to retake the road test you already passed because your records have been misplaced. Or it can mean that due to a misspelling of your name, you’re now on the FBI’s most wanted list. And it’s not even proper decorum to get angry about such things. You see, it’s not really their fault — making errors is part of the system. DMV Tyrant by Christopher Durang
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

## IC-1130: Dr. Seuss' The Lorax - Screenplay

- Title: Dr. Seuss' The Lorax - Screenplay
- Author (byline): Paul Cinco and Ken Daurio
- Work: Not specified
- Publisher: Scriptfly.com Original screenplay can be ordered here
- Publication date as stated: 2012
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: LORAX, MAN, WESLEY, DELIVERY MAN, WOMAN, SUNBATHER, SUNBATHER 2, TOGETHER, TED, AUDREY, MOM, GRAN, MARKETING GUY 1, MARKETING GUY 2, O’HARE, ONCE-LER, YOUNG ONCE-LER, TEEN GIRL, BOY, FAT GUY, MARIE, DAN, ROSE
- Teaser before the introduction: Yes
- Spoken words (computed): 1501
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paul Cinco and Ken Dario
ISBN: N/A
Publisher: Scriptfly.com Original screenplay can be ordered here
Date (Month/Year): 2012
```

### Introduction (context only: never use it for content warnings)

```text
In 1971, one year after the US Environmental Protection Agency was established, Theodore Geisel, aka Dr. Seuss published The Lorax as a cautionary fable. In 2012 that fable was re-imagined for film, reaching a new generation of children with a very dire message. Now it is 2025, and it seems our leaders have forgotten the message yet again. This year, the Trump administration has moved to rescind longstanding forest protections, opening nearly 59 million acres of national forest to logging.1 And his executive orders have reduced environmental oversight and relaxed endangered-species safeguards.2 Today with this performance, I speak for our trees, our environment and our planet.

Dr. Seuss' The Lorax Screenplay By Paul Cinco and Ken Daurio
```

### Performance text (classify this)

```text
(based on the book by Dr. Seuss, aka Theodore Geisel)

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

AUDREY: I'd probably marry him on the spot! (Ted smiles to the audience – he has a plan) ***** Ted’s House *****

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

AUDREY: But where? There’s no dirt anywhere! (stomps on the pavement) TOGETHER as TOWNSPEOPLE: (Pg 6) Parking lot! Parking lot!

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

---

## IC-1131: The Dreaded Batter Pudding Hurler

- Title: The Dreaded Batter Pudding Hurler
- Author (byline): Spike Milligan
- Work: The Goon Show Scripts, Pgs 25-42
- Publisher: Sphere Books
- Publication date as stated: Jan 1973
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: GREENSLADE, FX, HENRY CRUN, MINNIE BANNISTER, SEAGOON, GRYTPYPE, BLOODNOK, ECCLES, MORIARTY
- Teaser before the introduction: Yes
- Spoken words (computed): 1547
- Already set (do not supply): none

### Source block (context only)

```text
Author: Spike Milligan
Book: The Goon Show Scripts, Pgs 25-42
ISBN: 978-0722160794
Publisher: Sphere Books
Date (Month/Year): Jan 1973
```

### Introduction (context only: never use it for content warnings)

```text
You thought you were safe. You thought you could hide. You thought that you didn’t really need to use the restroom before the performance . . . but now you’re questioning that decision.: Now from the inner-most recesses of the BBC radio vaults and the creative minds of Spike Milligan, Peter Sellers and a short, fat, little guy whose name is Harry Secomb, but who I prefer to lovingly call “Tubby” comes one of the famed Goon Show scripts.

The Dreaded Batter Pudding Hurler created by Spike Milligan, Peter Sellers and “Tubby”(also known as Harry Secomb)
```

### Performance text (classify this)

```text
GREENSLADE: (Pg 25-42) The English Channel 1941. Across the silent strip of green-grey water – in England – coastal towns were deserted, except for people. Despite the threat of invasion and the stringent blackout rules, elderly gentlefolk of Bexhill-on-Sea still took their evening constitutionals.

FX: [Sea washing onto beach]

HENRY CRUN: Ohhh, dear, dear, dear, ohh, it's quite windy on these cliffs, Minnie.

MINNIE BANNISTER: Yes, yes, what a nice summer evening, typical English evening.

HENRY CRUN: Mnk yes, the rain is lovely and warm. Minnie, I think I'll take one of my sou'westers off . . . hold my elephant gun.

MINNIE BANNISTER: Oh dear, I don't know what you brought it for, you can't shoot elephants in England you know!

HENRY CRUN: Mnk? Why not?

MINNIE BANNISTER: They're out of season.

HENRY CRUN: Oh. Does this mean we shall have to have pelican for dinner again?

MINNIE BANNISTER: I fear so, I fear so!

HENRY CRUN: Then I'll risk it. I'll shoot an elephant out of season.

GREENSLADE: Listeners who are listening will, of course, realize that Minnie and Henry are talking rubbish; as erudite people will realize, there are no elephants in Sussex. They're only found in Kent. North of a line drawn between two points thus making it the shortest distance.

HENRY CRUN: . . . Well, if that's how it is, I can't shoot any.

MINNIE BANNISTER: Come Henry, we'd better be getting home.

FX: [Metal door slides open]

HENRY CRUN: Minnie, did you hear a gas oven door slam just then?

MINNIE BANNISTER: Don't be silly, Henry! Who'd be walking around these cliffs with a gas oven?

HENRY CRUN: Lady Docker?

MINNIE BANNISTER: Yes, but apart from the obvious ones, who'd want to . . .

FX: [Whoosh! Splat!] (Minnie is hit from behind and crumples in a heap)

MINNIE BANNISTER: Help Henry! I've been struck down from behind, buddy. Heelp!

HENRY CRUN: Mnk - oh dear dear! Poor Minnie! Police! English Police! Law Guardians. . .

FX: [Police whistle]

SEAGOON: Can I help you, sir?

HENRY CRUN: Are you a policeman?

SEAGOON: No, I'm a constable.

HENRY CRUN: Oh, what is the difference?

SEAGOON: They're spelt differently. What's happened to this dear old silver bearded lady?

HENRY CRUN: She was struck down from behind.

SEAGOON: And not a moment too soon. Congratulations, sir.

HENRY CRUN: I didn't do it.

SEAGOON: Coward. . . Now tell me, who did this felonious deed. What's happened to her?

HENRY CRUN: It's much too dark to see, strike a light.

SEAGOON: Not allowed in blackout. We daren't. Why, only twenty-eight miles across the Channel the Germans are watching this coast. [to audience] We tried using a candle, but it wasn't very bright and we daren't light it, so we waited for dawn, and there, in the light of the morning sun, we saw what had struck Miss Bannister. It was . . . A batter pudding!

FX: [Dramatic chord]

SEAGOON: Well, get her off this cliff, it's dangerous. Meantime, I must report this to the Inspector. I'll call on you later, goodbye. [to audience] That night I lay awake in my air-conditioned dustbin thinking; now who on earth would want to strike another with a batter pudding? Obviously it wouldn't happen again, so I fell asleep. Nothing much happened that night, except that I was struck with a batter pudding.

GREENSLADE: In the months to come, thirty-eight batter puddings were hurled at Miss Bannister. A madman was at large, Scotland Yard was called in.

GRYTPYPE: Inspector Seagoon, my name is Hercules Grytpype-Thynne, Special Investigation. This Batter Pudding Hurler... He's made a fool of the police.

SEAGOON: I disagree, we were fools long before he came along.

GRYTPYPE: You silly twisted boy. Nevertheless, he's got to be stopped, now Seagoon . . . these batter puddings, they were obviously thrown by hand.

SEAGOON: Not necessarily. Some people are pretty clever with their feet.

GRYTPYPE: [with a strange look at Seagoon] Now, Seagoon, these batter puddings, were they all identical.

SEAGOON: All except the last one. Inside it, we found this . . .

GRYTPYPE: What? An army boot!? So the dreaded hurler is a military man. Any troops in the town?

SEAGOON: The fifty-sixth Heavy Underwater Artillery.

GRYTPYPE: Get there at once, arrest the first soldier you see wearing one boot. Off you go!

FX: [Transition music – Should be somewhat recognizable military music]

SEAGOON: Major Bloodnok, [salute] I must ask you to parade your men. I'm looking for a criminal.

BLOODNOK: You find your own, it took me years to get this lot! [pause to contemplate the situation] Very well then, Bugler Max Geldray? Sound fall in the hard way.

FX: [Musical interlude: 'They Were Doing The Mambo'] (* see http://www.youtube.com/watch?v=kwDL-Bp8yP8 for music as troops assemble)

BLOODNOK: Silence, silence lads, silence! I'm sorry I had to get you out of bed in the middle of the day, but I'll see you get extra pay for this, I promise you. Now, Seagoon, which is the man?

SEAGOON: I walked among the ranks looking for the soldier with one boot, but my luck was out, the entire regiment were barefooted.

ECCLES: We want our beddy byes.

SEAGOON: Who are you?

ECCLES: Lance Private Eccles, sir.

SEAGOON: [to audience] I inspected the man closely, he was the nearest thing I'd seen to a human being, without actually being one. At last, by the light of a passing glue factory, I saw that Eccles was only wearing, one boot!

ECCLES: Well, I only got one boot.

SEAGOON: I know, but why are you wearing it on your head?

ECCLES: Why? Why? It fits, dat's why! What a silly question to ask . . .

SEAGOON: Let me see that boot! [to audience] Mmmmm, size nineteen . . . [to Eccles] What size head have you got?

ECCLES: Size nineteen.

SEAGOON: Curses, the man's defense was perfect. Major Blooknok? Where's this man's other boot?

BLOODNOK: Stolen.

SEAGOON: By whom?

BLOODNOK: A thief.

SEAGOON: You sure it wasn't a pickpocket?

BLOODNOK: Positive, Eccles never keeps his boots in his pocket.

SEAGOON: [to audience] Damn! They all had a watertight alibi. Months went by; I couldn't stop them. Still no sign of the Dreaded Hurler. Finally I walked the streets of Bexhill at night disguised as a human man. Then suddenly...

FX: [A sinister and dramatic fanfare]

SEAGOON: . . . Nothing happened. But it happened suddenly mark you.

MORIARTY: Pardon me, my friend.

SEAGOON: [to audience] I turned to see the speaker. He was a tall man wearing sensible feet, and a head to match. He was dressed in the full white outfit of a Savoy chef. Around his waist were tied several thousand cooking instruments. And behind him he pulled a portable gas stove from which issued forth the smell of batter pudding.

MORIARTY: Could I borrow a match? You see my gas has gone out and my batter pudding was just about to start browning.

SEAGOON: Certainly, here . . . No, no, no . . . Keep the whole box, I have another match at home.

MORIARTY: So rich! Well, thank you m'sieur, you have saved my batter pudding from getting cold. As you'll agree there's nothing quite so bad as being struck down with a cold batter pudding. Well, good night.

SEAGOON: I watched the strange man as he pulled his gas stove away into the darkness. But I couldn't waste time watching him, my job was to find the Dreaded Batter Pudding Hurler!

GREENSLADE: Those who think that Seagoon is not cut out to be a detective, please write to him care of Rowton House.

SEAGOON: [to audience] On December 25th the Hurler changed his tactics. That day Miss Bannister was struck with a Christmas Pudding.

GRYTPYPE: [reading a letter] A Miss Bannister has just received this letter. It was postmarked 'Africa', and inside was a portion of batter pudding.

SEAGOON: So he's in Africa, now we've got him cornered. I must leave at once.

GREENSLADE: Seagoon travelled by sea. To avoid detection by enemy U-boats he spoke German throughout the voyage and was heavily disguised as a Spaniard.

SEAGOON: [to audience] The ship was disguised as a train, to make the train sea-worthy it was done up to look like a boat and painted to appear like a tram. Also on board were Major Bloodnok and his regiment. When we were ten miles from Algiers, we heard a dreaded cry.

ECCLES: Mine ahead woohoowoo! Dirty big mine ahead!

FX: [Explosion]

SEAGOON: Bloodnok and I floundered in the cruel sea.

FX: [Lapping waves]

BLOODNOK: Fortunately, we found a passing lifeboat and dragged ourselves aboard.

SEAGOON: We had no oars, but luckily we found two outboard motors and we rowed with them. For thirty days we drifted to and fro, then hunger came upon us.

BLOODNOK: Aeioughhhhh, if I don't eat soon I'll die of hunger, and if I die I won't eat soon. Wait a moment, [sniffs] ohohohh, can I smell cooking or do my ears deceive me?

SEAGOON: He was right, something was cooking. There, in the other end of the lifeboat was. . . a gas stove! Could this be the end of our search?

BLOODNOK: I'll knock on the oven door.

FX: [Knocking on metal]

MORIARTY: [Faintly] Just a minute please, I'm in ze bath...

FX: [Door scrapes open]

SEAGOON: Don't move, I arrest you as the Dreaded Batter Pudding Hurler.

MORIARTY: Sacre Bleu!

SEAGOON: Hands up, you devil, don't move! This finger is loaded.

MORIARTY: If you kill me, I promise you, you'll never take me alive.

BLOODNOK: Wait, how can we prove he's the hurler?

SEAGOON: That batter pudding in the corner of the stove is all the evidence we need. We've got him!

FX: [Dramatic fanfare]

GREENSLADE: But it wasn't so easy. Forty days they drifted in an open boat.

FX: [Lapping waves]

BLOODNOK: Oooaeioughhhh, I tell you Seagoon, let's eat the batter pudding or we'll starve!

SEAGOON: No, yer hear me, No! That's the only evidence we've got.

BLOODNOK: We must eat it or die.

SEAGOON: Never!

GREENSLADE: And that, we fear, is the end of our story, except of course, for the end. Should Seagoon eat the batter pudding and live, or leave it and in the cause of justice, die? Send your suggestions on a piece of batter pudding.
```

---

## IC-1132: Driving

- Title: Driving
- Author (byline): Ray Romano
- Work: Everything and a Kite
- Publisher: Bantam Books
- Publication date as stated: September 1999
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: SPEAKER, A, B, C
- Teaser before the introduction: Yes
- Spoken words (computed): 1643
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ray Romano
Book: Everything and a Kite
ISBN: 978-0553580372
Publisher: Bantam Books
Date (Month/Year): September 1999
```

### Introduction (context only: never use it for content warnings)

```text
And to be honest, people on the road today have every right to be a little neurotic. Gen Z has taken their place behind the wheel and survey says . . . (in the tradition of Family Feud): *38% of Gen Zers look at their phone more frequently when behind the wheel; 34% video chat while driving and 24% use social media; followed closely by the Millennials at 23%.

It’s time to ditch the digital and go old school with some driving tips, tricks and observations from Everything and a Kite . . . It’s Driving by Ray Romano
```

### Performance text (classify this)

```text
SPEAKER: (Pg 165-181) I'd rather drive than fly, because when I fly, I'm afraid the person I'm sitting next to is going to want to talk. I'm a friendly guy. It's not that I'm unsociable. I'm just not a great conversationalist. And long flights can get very tough on a non-talker like myself. What's made things easier is learning some of the things you can do, tactfully of course, to let the person next to you know you're not the talking type.

First of all, you can't let any conversation begin. Because once it's started, there's no proper point to say, "You've been very nice, but I'd like for both of us to stop talking."

Unfortunately, people interpret many things as an invitation to begin a conversation. It could be anything from eye-contact to saying "God bless you" after they sneeze. So, what you have to do is cut off all possible avenues of communication. Your best bet is just to walk on the plane wearing headphones, a surgical mask, and looking through a View-Master. I know that'll work, because at home, it's the way I go to bed.

People think I drive because I'm afraid to fly. That's not it at all. Not only do I know that you are statistically more likely to get into an accident in an automobile, but the way my mind works, I worry that while I'm driving, a plane might crash into my car. I'm going to be neurotic whether I'm driving or flying.

New York City (Replace with name of your town or state) drivers have always had a bad reputation. And I'm not going to say it isn't true, but I will tell you what the problem is. It's the testing. It's just way too easy to get a license. I don't know what the written exam in your part of the country consists of, but it can't be any easier than ours. Here you go, Sample question: A blind person is crossing the road. What is your course of action?

A: Stop. Let him go by.

B: Nudge him a little, so he knows you're there.

C: Speed up. Aim for the dog. Actually, I've thought of a very simple solution to the New York City driving problem. They should require all drivers to put one of those "How's My Driving?" stickers with the 800 numbers on their car. I'm sure you've seen these on the back of trucks. My favorite one is "How's My Driving? If you have any complaints, or compliments, call this number. . ." OK, look: complaints I can understand. But compliments? Folks, whose life is that boring? Who's making that phone call?

"Hello, Sternberger Moving Company? I was out on the road and happened to catch truck number forty-two? He backed into this loading dock. . . it was artwork. Then, on the way out, he made a U-turn. . . and I wept. Is he ever going to be in town again, because the kids would love him.”

Of course, you couldn't have 800 numbers for every car, because the call volume would overload the phone system.

"Hello? I'm leaving you a message because you just cut me off in traffic. Yeah, you're staring at me right now. Looks like you thought it was my fault. Hold on, I'm going to give you *a rude gesture*. There you go. Ha ha. OK, now we're at a red light. You're getting out of your car and approaching mine. Tell you what: let me call you back."

Something happened to me one time on the road that still gives me nightmares. I was driv-ing to a gig, and I noticed a spider on the windshield of my car.

OK, I know that doesn't sound like much drama to you, but they give me the heebie-jeebies! So, there was this big hairy spider right in the middle of my windshield, and all I knew was I wanted him off, pronto. The plan I developed was simple: turn on the wipers and knock him into orbit. For a moment, however, I was torn. What if all the wipers do is push him a little closer to the driver's side window? Then what? I think he's gone, I get out of the car, he leaps down my throat and hatches his eggs in my stomach. I didn't know what to do. If I had been near a car wash, that might have solved everything, but I was on the highway, which also ruled out pulling into a garage and getting a new windshield.

I kept one eye on the spider, and one eye on the road. I couldn't keep that up much longer without getting into an accident. So, after a few minutes of trying to "pray" him away, I had to take a chance. I activated the wipers. Swish, swish, swish, swish. . . Nothing. The spider didn't budge. My cheapo wipers must have been warped, because they were gliding right over the eight-legged beast without moving him a millimeter. Desperately, I turned on the washer to try and flood him out.

Still nothing. Whatever fear I was feeling at the moment was magnified tenfold. I was in my own little horror movie, and I had just gotten a phone call: "We've traced the spider, *sir/ma’am* -- He's ON THE INSIIIIIIIIDE!"

I'm too embarrassed to tell the end of this story. But here's a hint: Moonroof.

Aside from spiders, the only other thing I fear while driving is the dreaded "sleep dip." Oh man. . . you ever do one of those? Usually they happen late at night, although it's not a rule. But there you are: behind the wheel of your car, and you're starting to get tired. Your eyelids get a little heavy, and without realizing it, you start to close them just a tiny bit.

Then your head gets a little heavy. Suddenly your chin drops to your chest. The jolt snaps you back awake and your head pops up. "Wha . . . ? WHOA! Was I just sleeping?!"

You can't believe it. "Oh my God, I was sleeping!" The first thing you do is look around to see if you killed anybody. "I think that guy was lying there already. . ."

The sleep dip is not only frightening, it's frustrating. How many times are you at home, in your bed, in your pajamas, it's cozy, it's warm, and you can't sleep at all? Now you're going sixty miles an hour, and you're catching ZZZs behind the wheel.

You can't stop it. And it's not from a lack of effort. You try all the tricks to keep yourself awake. You turn on the radio, you open a window, you slap your face. I'll tell you what I do to stay awake -- let me pass on a real tip just to break up the boredom of a long car ride.

Over the years, I've developed a little game that I can play endlessly. The rules are very simple. As a matter of fact, there's only one: Come up with a sentence that has never been said before in the entire history of language. That's it. That's the whole game. The whole key is this: pretend your life depends on coming up with a string of words -- not just nonsense, but a real sentence -- that hasn't been uttered by anyone, anytime, anywhere. Let me give you an example. "Give me back my fudge suitcase!"

Now, I don't know if that sentence has been said before. But we're off to a good start, because I think we can all agree it probably hasn't been said very often. But still, one could probably imagine some kind of situation where "Give me back my fudge suitcase" might have been said in the past. Which brings us to the next phase of the game: once you come up with your "Never Been Said" sentence, you have to try and figure out a scenario where it could have been said. This part is actually the most fun.

"Give me back my fudge suitcase!" Hmm. OK, how about this? Some guy's coming back from Hershey Park, Pennsylvania, and he's loaded up his bags with fudge. He's in the airport, some gung-ho security guy confiscates his luggage. . . I think you can figure out the rest. [Wait!] "Give me back my fudge suitcase" could have been a line from the movie Willy Wonka and the Chocolate Factory.

See what I'm saying? It's not that easy to come up with a "Never Been Said" phrase. "Give me back my fudge suitcase" is actually kind of weak. But here's a tip. Sometimes you can just alter the sentence a little, and that will make all the difference. Check it out: "Give me back my fudge suitcase, Rockhead." I think, statistically, we've improved our odds. I mean, how many airport security guards are there named Rockhead?

To be honest, the most challenging part of the game is to keep the sentence short and realistic. Anyone can just keep adding words to the end, but stuff like, "Officer Tongue Depressor, could you check under my rumble seat to see if any of the goose-loving woodchucks have cut through my brake line, and also I'm itchy" -- to be honest, it's kind of contrived.

Here's a list of some of the phrases I've been working on over the years. Please don't be
intimidated. You have to understand that while you're just starting out, this is my life's
work.
• "If hernias were rainbows, I'd be Raymond Burr."
• "Shredded Wheat would make a silly pistol."
• "Moonlight is the plumber's pudding."
• "I'm one headlock short of making colonel."

Not bad, right? Listen, you might be laughing at me right now, but next time you're driving with nothing to do, you’re going to be playing that game faster than a leg warmer can yell at a helmet! There's another one for you. That's without even trying.
```

---

## IC-1133: Emotional Baggage

- Title: Emotional Baggage
- Author (byline): Nina Shengold
- Work: Take Ten II
- Publisher: Vintage
- Publication date as stated: Nov 2003
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: DICK, PHYLLIS, CREW, ROLLO, AMBER, MILDRED
- Teaser before the introduction: Yes
- Spoken words (computed): 1120
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nina Shengold
Book: Take Ten II
ISBN: 978-1400032174
Publisher: Vintage
Date (Month/Year): Nov 2003
```

### Introduction (context only: never use it for content warnings)

```text
It’s a traveler’s worst nightmare to discover that the airline has lost your luggage—waiting at baggage claim for your bag to emerge, but it never does. But what if the opposite happens? You’ve probably seen it—the bags have come out onto the baggage carousel. Most of the travelers have found their bags and gone on their way. But, if you’re one of the last people lingering at the carousel, you’ve probably noticed one or two bags left, going around and around, over and over, with no one claiming them. What happens if no one does?

From the perspective of those unclaimed pieces of luggage . . . . Emotional Baggage by Nina Shengold.
```

### Performance text (classify this)

```text
(A near-empty baggage claim carousel at Newark Airport. A few stray suitcases circle forlornly. Actors shuffle around the periphery of the stage shoulder to shoulder, as if swept along by a rotating belt. PHYLLIS stands crookedly, leaning on DICK as if thrown there.)

DICK (an irate Samsonite pullman): This sucks. (PHYLLIS and DICK turn in unison, facing the side wall as the "carousel" circles upstage. DICK looks back over his shoulder.) How many times have [we] been around? PHYLLIS (a panicky carry-on bag): I'm dizzy. My straps hurt. I'm going to catch cold!

DICK: Quit whining. (Shouts into the wings.) YO, HEY!!! COME AND GET ME, YOU MORON!!! Do you know what I weigh? I'm a Samsonite hardbody!

PHYLLIS: Please! I've got mal de mer! (The carousel shuts off abruptly. They lurch to a sudden stop.) It stopped! The belt, the, the thing . . . it's not

DICK: (hissed whisper) Cheese it, the crew. Look inanimate. Sssh! (DICK freezes in place. PHYLLIS continues to panic for a beat, then freezes suddenly)

CREW: (A voice booms from off stage) LOOKS LIKE WE GOT US A COUPLE OF UNCLAIMED BAGS. LUG 'EM. (PHYLLIS and DICK are "lifted" in unison, shoulders pulled up toward the ceiling as if picked up by giant hands)

PHYLLIS: Where are they taking us??

DICK: Lockup. The big house . . . Unclaimed baggage. (The unseen hands "throw" them down onto a luggage rack.)

PHYLLIS: Oh God! (fearfully) Who are those other bags? (AMBER saunters on, followed by ROLLO and MILDRED.)

DICK: Looks like rough trade. Maybe lifers. AMBER (an over the hill overnight bag): Hey, big boy! Is that a travel umbrella, or are you glad to see me? (She barks a short, humorless laugh and plunks into a chair with her arm around PHYLLIS.)

PHYLLIS: OhGodOhGodOhGodOhGOD!!! ROLLO (a beat-up drug smuggler’s duffel): (sitting on PHYLLIS 's other side) Chill, babe. What are you, a carry-on?

PHYLLIS: Yes! I'm a carry-on! I was made to be carried! I would have been carried if she hadn't bought so much Duty-Free Tia Maria! I was flying First Class! MILDRED (a dignified, threadbare valise from the South): So was I, my dear. So was I. (She sits with a thud.)

ROLLO: What're you in for?

PHYLLIS: Beg pardon?

ROLLO: Lost tag, missed connection? You're just off the plane from Cancun, right?

PHYLLIS: I flew down for a Realtors' convention!

ROLLO: Did the beagle sniff you? I hate it when they sniff you.

DICK: Leave her alone, or I'll pop you one right in the buckle.

ROLLO: Big man. I'm aquiver. First time in the joint? (PHYLLIS nods) We got some hard cases. Watch out for that camp trunk. And Rolf there, that rucksack, he'd eat you for breakfast. Most of the rest? Just a buncha lost luggage.

PHYLLIS: So what happens now?

AMBER: We wait. For our legs.

PHYLLIS: How long?

ROLLO: Some cases make bail the first night. Some do the whole stretch. Thirty days.

PHYLLIS: But ... I'm carrying beach things rolled in a mesh bag! Her tankini's still damp! I could mildew!

ROLLO: So what? Little mildew won't kill you.

PHYLLIS: I have sand in my twill! (Breaking down in tears.) This is not what I thought it would be like at all. You know, when you're still in the warehouse, you dream about having somebody to carry you? Well. First, she removed all my tags. And it says. Right there in capitals: "Do not remove under penalty of law."

ROLLO: Oh, you poor baby. You're fresh from the store?

PHYLLIS: From a catalog! I was just ordered!

ROLLO: Your first trip on a plane? (PHYLLIS nods.) And she lost you?? (She nods again.) That makes me so mad I could split a seam. Hell needs a separate ring for that kinda behavior. We're gonna take care of you, kiddo.

DICK: I bet you'll take care of her.

ROLLO: Stow it, you steroid-pumped piece a' petroleum. Can't you see the kid's scared?

PHYLLIS: The luggage compartment was bad enough!

MILDRED: Steerage! I was flung cheek by jowl with an R.E.I. backpack. The smell of that bedroll. I thought I'd expire, I most certainly did.

ROLLO: I was next to a dog. (Murmurs all around. This is bad.) Uh huh, yeah. Flew up from Miami alongside a doped-up Jack Russell. But not too sedated to squirt me.

PHYLLIS: What are you ... in for?

ROLLO: My [idiot] missed his plane. Checks me in at the counter, right, goes to the men's room, next thing you know he's in Boca Raton and yours truly is doing the carousel cha-cha in Newark. Again. I wish he would just lose me.

PHYLLIS: You don't really mean that.

ROLLO: Oh no? I came close a few times. Hotel lobby in Bangkok. [He] puts me down and goes out for a smoke. I was sure I'd be lifted, you know, do a stint on the black market? Wrong. No one looked at me twice. I could've been a container. Instead of a bum, which is what I am.

PHYLLIS: I think you're kind of cute.

ROLLO: Don't melt my heart with that garbage. I'm nobody's treasure chest. What's your monogram, kid?

PHYLLIS: P.M.S.

ROLLO: Aw. That's so sweet. My name's Rollo. What's that you got rolled in that towel?

AMBER: What've you got, x-ray eyes?

ROLLO: You been through as many detectors as I have, you've got x-ray everything.

DICK: This guy's full of [crap]. He's a con man!

ROLLO: Whatever you need to believe. Though if I had those magazines sewn in my lining . . .

DICK: How did you know that??

ROLLO: We ain't so opaque as we think, my man. Not if you know how to look.

DICK: It's a trick!

ROLLO: Hey, I've done tricks. False bottoms, lead x-ray blocks. Not anymore. I got nothin' to hide. What you see is what is. I've had some hard knocks, done the merchant marine, rode the rails outta Marrakech next to a goat. I ain't sayin' I ain't got some miles on me. But I'm ready to kick all that, settle down, have a coupla fanny packs with the right girl. End of the day, it's who you got loving you.

MILDRED: Even love doesn't last. I married a satchel, raised three matching garment bags. Where are they now? Do they call? Do they write?

AMBER: I used to hang out with a weekender bag, name of Morty. He would've gone to the ends of the earth for me! He was the genuine article. Leather. Top-grain. They don't make 'em like that anymore.

MILDRED: They're all microfiber. Synthetic.

ROLLO: Uh-oh. Here it comes.

MILDRED: Back in my day- We were valises back then. We were carried by uniformed porters. Cunard Lines. The steamer trunks! Bandboxes! Linings of satin. Solid brass fittings.

DICK: Yeah, right. And your ancestors rode on the Mayflower. Well, la di dah.

MILDRED: Thug!

DICK: Dust collector. White elephant!

ROLLO: (Pulls DICK aside, confidential.) Go easy on her. She's on day twenty-nine of a thirty-day stretch. And the old bag don't know about this, but her legs had a cardiac thirty-five thou in the air over Greenland. He ain't coming back.

PHYLLIS: What ... what'll happen to her?

ROLLO: The daughter-in-law picks her up, checks her insides for valuables, doesn't find nothing, she sends Portmanteau down the Red Mile.

PHYLLIS: (in horror) The Salvation Army??

ROLLO: She got Clearance Sale written all over her tweed.

PHYLLIS: (rising panic) I want to get out of here! Somebody CLAIM me!!!

ROLLO: Hey, hey, hey. Kid, that ain't you. You're just outta the warehouse, ya dig? You got miles of blue sky up ahead.

CREW: (offstage) CAN I HELP YOU? COULD I SEE YOUR CLAIM CHECK? (The suitcases sit forward, waiting expectantly. PHYLLIS closes her eyes tightly, crossing her fingers.)

PHYLLIS: Me. Me.

CREW: (offstage) YUP. IT'S RIGHT OVER THERE. (Loud sound of footsteps. The suitcases hold their breath, hopeful. Suddenly DICK is ''pulled up" by the shoulder. He is "carried" off, The others sit stunned.)

PHYLLIS: He got picked up?? Out of all of us? Him?? (voice starting to tremble) I'll never get home now.

AMBER: Quit snivelling. We're all on the shelf.

ROLLO: Drop the attitude, will you? You're luggage. You're Naugahyde, buddy. A knockoff. A fake. (Sotto voice.) I see dead baggage. The future, the past. I can't help it. I always have. Thing is, most people, they don't wanna know.

PHYLLIS: Can you see my future? My Realtor is gonna come back for me, right? I'll be found?

ROLLO: (Hesitates, doesn't like lying.) ... Sure, kid. Of course, you will. Here, put your strap on my shoulder.

PHYLLIS: Thanks, Rollo. (She settles her head on his shoulder, then puts her thumb in her mouth. ROLLO strokes her hair softly.)
```

---

## IC-1134: Examining Psychic Phenomena

- Title: Examining Psychic Phenomena
- Author (byline): Woody Allen
- Work: The Insanity Defense
- Publisher: Random House Trade Paperbacks
- Publication date as stated: 2007
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: MRS. MARPLE, MEDIUM, QUINCY
- Teaser before the introduction: No
- Spoken words (computed): 1712
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
The world of the paranormal is just now beginning to be examined by modern science. Soon, we hope to have explanations as to which spirit steals socks from the dryer and which tortured ghost stole the cookie from the cookie jar. After these mysteries are solved, we hope to unveil the metaphysical force that keeps glue from sticking to the inside of the bottle. Though we’re not there yet, we move a step closer in “Examining Psychic Phenomena” by Woody Allen.
```

### Performance text (classify this)

```text
There is no question that there is an unseen world. The problem is, how far is it from midtown and how late is it open? Unexplainable events occur constantly. One man will see spirits. Another will hear voices. A third will wake up and find himself running in the Preakness. How many of us have not at one time or another felt an ice-cold hand on the back of our neck while we were home alone? (Not me, thank God, but some have.) What is behind these experiences? Or in front of them, for that matter? Is it true that some men can foresee the future or communicate with ghosts? And after death is it still possible to take showers? Fortunately, these questions about psychic phenomena are answered in a soon-to-be-published book, Boo!, by Dr. Osgood Mulford Twelge, the noted parapsychologist and professor of ectoplasm at Columbia University. Dr. Twelge has assembled a remarkable history of supernatural incidents that covers the whole range of psychic phenomena, from thought transference to the bizarre experience of two brothers on opposite parts of the globe, one of whom took a bath while the other suddenly got clean. What follows is but a sampling of Dr. Twelge's most celebrated cases, with his comments.

Apparitions On March 16, 1882, Mr. J. C. Dubbs awoke in the middle of the night and saw his brother Amos, who had been dead for fourteen years, sitting at the foot of his bed flicking chickens. Dubbs asked his brother what he was doing there, and his brother said not to worry, he was dead and was only in town for the weekend. Dubbs asked his brother what it was like in "the other world," and his brother said it was not unlike Cleveland. He said he had returned to give Dubbs a message, which was that a dark-blue suit and Argyle socks are a big mistake. At that point, Dubbs's servant girl entered and saw Dubbs talking to "a shapeless, milky haze," which she said reminded her of Amos Dubbs but was a little better-looking. Finally, the ghost asked Dubbs to join him in an aria from Faust, which the two sang with great fervor. As dawn rose, the ghost walked through the wall, and Dubbs, trying to follow, broke his nose. This appears to be a classic case of the apparition phenomenon, and if Dubbs is to be believed, the ghost returned again and caused Mrs. Dubbs to rise out of a chair and hover over the dinner table for twenty minutes until she dropped into some gravy. It is interesting to note that spirits have a tendency to be mischievous, which A. F. Childe, the British mystic, attributes to a marked feeling of inferiority they have over being dead. "Apparitions" are often associated with individuals who have suffered an unusual demise. Amos Dubbs, for instance, had died under mysterious circumstances when a farmer accidentally planted him along with some turnips. Spirit Departure Mr. Albert Sykes reports the following experience: "I was sitting having biscuits with some friends when I felt my spirit leave my body and go make a telephone call. For some reason, it called the Moscowirz Fiber Glass Company. My spirit then returned to my body and sat for another twenty minutes or so, hoping nobody would suggest charades. When the conversation turned to mutual funds, it left again and began wandering around the city. I am convinced that it visited the Statue of Liberty and then saw the stage show at Radio City Music Hall. Following that, it went to Benny's Steak House and ran up a tab of sixty-eight dollars. My spirit then decided to return to my body, but it was impossible to get a cab. Finally, it walked up Fifth Avenue and rejoined me just in time to catch the late news. I could tell that it was reentering my body, because I felt a sudden chill, and a voice said, 'I'm back. You want to pass me those raisins?' "This phenomenon has happened to me several times since. Once, my spirit went to Miami for a weekend, and once it was arrested for trying to leave Macy's without paying for a tie. The fourth time, it was actually my body that left my spirit, although all it did was get a rubdown and come right back." Spirit departure was very common around 1910 when many "spirits" were reported wandering aimlessly around India searching for the American Consulate. The phenomenon is quite similar to transubstantiation, the process whereby a person will suddenly dematerialize and rematerialize somewhere else in the world. This is not a bad way to travel, although there is usually a half-hour wait for luggage. The most astonishing case of transubstantiation was that of Sir Arthur Nurney, who vanished with an audible pop while he was taking a bath and suddenly appeared in the string section of the Vienna Symphony Orchestra. He stayed on as the first violinist for twenty-seven years, although he could only play "Three Blind Mice," and vanished abruptly one day during Mozart's Jupiter Symphony, turning up in bed with Winston Churchill. Precognition Mr. Fenton Allentuck describes the following precognitive dream: "I went to sleep at midnight and dreamed that I was playing whist with a plate of chives. Suddenly the dream shifted, and I saw my grandfather about to be run over by a truck in the middle of the street, where he was waltzing with a clothing dummy. I tried to scream, but when I opened my mouth the only sound that came out was chimes, and my grandfather was run over. "I awoke in a sweat and ran to my grandfather's house and asked him if he had plans to go waltzing with a clothing dummy. He said of course not, although he had contemplated posing as a shepherd to fool his enemies. Relieved, I walked home, but learned later that the old man had slipped on a chicken-salad sandwich and fallen off the Chrysler Building." Precognitive dreams are too common to be dismissed as pure coincidence. Here a man dreams of a relative's death, and it occurs. Not everyone is so lucky. Martinez, of Kennebunkport, Maine, dreamed he won the Irish Sweepstakes. When he awoke, his bed had floated out to sea. Trances Sir Hugh Swiggles, the skeptic, reports an interesting séance experience: We attended the home of Madame Reynaud, the noted medium, where we were all told to sit around the table and join hands. Mr. Weeks couldn't stop giggling, and Madame Reynaud smashed him on the head with a Ouija board. The lights were turned out, and Madame Reynaud attempted to contact Mrs. Marple's husband, who had died at the opera when his beard caught fire. The following is an exact transcript:

MRS. MARPLE: What do you see?

MEDIUM: I see a man with blue eyes and a pinwheel hat.

MRS. MARPLE: That's my husband!

MEDIUM: His name is ... Robert. No ... Richard ...

MRS. MARPLE: Quincy.

MEDIUM: Quincy! Yes, that's it!

MRS. MARPLE: What else about him?

MEDIUM: He is bald but usually keeps some leaves on his head so nobody will notice.

MRS. MARPLE: Yes! Exactly!

MEDIUM: For some reason, he has an object ... a loin of pork.

MRS. MARPLE: My anniversary present to him! Can you make him speak?

MEDIUM: Speak, spirit. Speak.

QUINCY: Claire, this is Quincy.

MRS. MARPLE: Oh, Quincy! Quincy!

QUINCY: How long do you keep the chicken in when you're trying to broil it?

MRS. MARPLE: That voice! It's him!

MEDIUM: Everybody concentrate.

MRS. MARPLE: Quincy, are they treating you O.K.?

QUINCY: Not bad, except it takes four days to get your cleaning back.

MRS. MARPLE: Quincy, do you miss me?

QUINCY: Huh? Oh, er, sure. Sure, kid. I got to be going ...

MEDIUM: I'm losing it. He's fading ...

I found this séance to pass the most stringent tests of credulity, with the minor exception of a phonograph, which was found under Madame Reynaud's dress. There is no doubt that certain events recorded at séances are genuine. Who does not recall the famous incident at Sybil Seretsky's, when her goldfish sang "I Got Rhythm" a favorite tune of her recently deceased nephew? But contacting the dead is at best difficult, since most deceased are reluctant to speak up, and those that do seem to hem and haw before getting to the point. The author has actually seen a table rise, and Dr. Joshua Fleagle, of Harvard, attended a séance in which a table not only rose but excused itself and went upstairs to sleep. Clairvoyance One of the most astounding cases of clairvoyance is that of the noted Greek psychic, Achille Londos. Londos realized he had "unusual powers" by the age of ten, when he could lie in bed and, by concentrating, make his father's false teeth jump out of his mouth. After a neighbor's husband had been missing for three weeks, Londos told them to look in the stove, where the man was found knitting. Londos could concentrate on a person's face and force the image to come out on a roll of ordinary Kodak film, although he could never seem to get anybody to smile. In 1964, he was called in to aid police in capturing the Dusseldorf Strangler, a fiend who always left a baked Alaska on the chests of his victims. Merely by sniffing a handkerchief, Londos led police to Siegfried Lenz, handyman at a school for deaf turkeys, who said he was the strangler and could he please have his handkerchief back. Londos is just one of many people with psychic powers. C. N. Jerome, the psychic, of Newport, Rhode Island, claims he can guess any card being thought of by a squirrel. Prognostication Finally, we come to Aristonidis, the sixteenth-century count whose predictions continue to dazzle and perplex even the most skeptical. Typical examples are: "Two nations will go to war, but only one will win." (Experts feel this probably refers to the Russo-Japanese War of 1904-05-an astounding feat of prognostication, considering the fact that it was made in 1540.) "A man in Istanbul will have his hat blocked, and it will be ruined." (In 1860, Abu Hamid, Ottoman warrior, sent his cap out to be cleaned, and it came back with spots.) "I see a great person, who one day will invent for mankind a garment to be worn over his trousers for protection while cooking. It will be called an 'abron' or 'aprone.'" (Aristonidis meant the apron, of course.) "A leader will emerge in France. He will be very short and will cause great calamity." (This is a reference either to Napoleon or to Marcel Lumet, an eighteenth-century midget who instigated a plot to rub béarnaise sauce on Voltaire.) "In the New World, there will be a place named California, and a man named Joseph Cotten will become famous." (No explanation necessary.)
```

---

## IC-1135: The Fairy Godmother’s Assistant

- Title: The Fairy Godmother’s Assistant
- Author (byline): Bruce Lansky
- Work: Girls to the Rescue #1, Pgs 1-16
- Publisher: Meadowbrook
- Publication date as stated: Sept 1995
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, ASSISTANT, ELLA, KING, SHERMAN, HERMAN, GODMOTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 2154
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bruce Lansky
Book: Girls to the Rescue #1, Pgs 1-16
ISBN: 978-0671899790
Publisher: Meadowbrook
Date (Month/Year): Sept 1995
```

### Introduction (context only: never use it for content warnings)

```text
The Fairy Godmother’s Assistant by Bruce Lansky
```

### Performance text (classify this)

```text
NARRATOR: (Pgs 1 - 16) When you need help, don't you wish a fairy godmother would suddenly appear to make things right? Well, don't hold your breath. She doesn't do that kind of thing anymore. (She's getting on in years, you know.) So if you want some help-she still fixes anything from broken windows to broken hearts-you'll have to visit her little cottage in the Bavarian woods and wait your turn, just like everyone else. And when you knock on the door, I'll let you in and make you comfortable. I'll even serve you a nice cold glass of lemonade. You see, I'm the fairy godmother's assistant.

My job used to be quite simple, really, until the fairy godmother announced she would be taking a much-needed vacation. I was scared stiff! What would I say to people who came for help? I didn't know any magic. I couldn't have turned a pumpkin into a glittering coach if my life depended on it. I remember exactly what she told me as she was leaving.

NARRATOR: To be honest, I didn't get much sleep that night. I kept wondering how I could possibly fill her shoes. I got up the next morning and went to the kitchen to make a fresh pitcher of lemonade. When I heard a knock on the door, I opened it and found a young woman with a tear-strained face, wearing a tattered dress. I explained that the fairy godmother would be gone for a few days and that I was her assistant. But she looked so sad that I invited her in for a glass of lemonade to cheer her up. As soon as she sat down, she started to cry. I sat beside her and gave her a handkerchief to dry her eyes.

ASSISTANT: First wipe away your tears. Then tell me what's bothering you.

ELLA: My name is Ella, but my stepmother and stepsisters call me Cinder-Ella, because my apron is always covered with cinders from cleaning the fireplace. They are mean to me and make me clean the house, cook, sew, and run errands all day while they have fun. Now I have to make them new gowns for the royal ball. But I want to go too.

ASSISTANT: I'm very sorry to hear that. I suppose you came to ask the fairy godmother to get you to the ball. Is that it? I wish I could help you, but I make lemonade not magic.

ELLA: Can't you do anything?

ASSISTANT: There's not much I can do. It's really up to you.

ELLA: Up to me?

ASSISTANT: It's really very simple. If you want to go to the ball, go. And don't let anything or anyone stand in your way.

ELLA: But how can I go to the ball without an evening gown?

ASSISTANT: Don't look at me. You're the seamstress. If you can make beautiful gowns for your two stepsisters, why not make another for yourself?

ELLA: But I can't afford to buy silk or velvet. How can I make a gown without any fabric?

ASSISTANT: Are there any velvet curtains in your house? Or silk bed sheets?

ELLA: There sure are! But what about dancing slippers? I don't have any.

ASSISTANT: Then don't wear any.

ELLA: You mean I should go to the royal ball barefooted?

ASSISTANT: What choice do you have, unless you want to wear those ugly boots you're wearing?

ELLA: How am I supposed to get to the ball? The royal palace is almost a mile from my house.

ASSISTANT: I suppose you'll just have to walk.

NARRATOR: A big frown appeared on her face. This wasn't the kind of help she had hoped to get from her fairy godmother.

ELLA: But they'll never let me in if I don't arrive in a fancy, horse-drawn carriage.

ASSISTANT: You're right. They may not let you in through the main gate, but I don't think there's anyone guarding the door to kitchen. Do you?

ELLA: I guess not. At least, I hope not! But if a prince asks me to dance, what should I say?

ASSISTANT: Ask him to be careful not to step on your toes. What have you got to lose?

ELLA: Nothing. Nothing at all. Thank you for all your help. I've got to go now. I've got so many things to do!

ASSISTANT: If you don't want your stepmother and stepsisters to know you've been to the ball, be sure to leave by twelve o'clock sharp. That way you'll be back in bed by the time they get home.

NARRATOR: I was quite pleased with myself for helping Ella. Relaxing for a moment with a glass of lemonade, I wondered if the fairy godmother with all her magic could have done a better job. I spent a good part of the day congratulating myself and feeling thankful I'd gotten through my first visitor without messing up. After dinner I was surprised by a knock at the door. When I opened it up, I discovered a distinguished-looking elderly gentleman. He looked ever-so-much like the king, as pictured on every postage stamp in Bavaria, except that this man looked older, frailer, ad far more worried. He must have been trying to keep his visit a secret; no guards or footmen were with him. I curtsied deeply as soon as I let him in.

KING: Enough of that. I must see the fairy godmother at once!

ASSISTANT: I'm sorry, Your Highness. She's away. Can I help you?

KING: Perhaps. Do you know where she keeps her magic potions?

ASSISTANT: If you tell me which potion you'd like, I'll be happy to look.

KING: Well, actually, I'm looking for a potion that would enable me to, well… live forever.

NARRATOR: I offered the king a comfortable chair, excused myself, and went to the cabinet where the fairy godmother kept her potions. In a short time I returned with a handful of bottles.

ASSISTANT: I've found a potion to keep your breath fresh longer, and one to make your suntan last longer. But I can't find anything to help you live longer, not even for a day.

KING: In that case, I'll wait here till the fairy godmother returns. You see, I'm not feeling well, and the royal doctors haven't been much use.

ASSISTANT: I'm sorry to hear that, Your Highness. What seems to be the problem?

KING: My back, for one thing. It's killing me. And I can't sleep at night because of terrible gas pains, not to mention splitting headaches. My eyesight's growing dim. I'm deaf in one ear. I'm growing forgetful… or did I mention that already? But worst of all, my twin sons are driving me crazy! Aside from that, I'm fine-just fine.

ASSISTANT: I think you must be terribly uncomfortable, Your Highness. But why would you want to live forever? Surely your health will continue to get worse as you grow older. In a few years, you'll be confined to bed. Would you enjoy living forever in bed?

KING: I never thought of it that way. But at least if I lived forever, I wouldn't have to worry about how to divide the kingdom between my sons, Prince Sherman and Prince Herman. They're identical twins, you know. Even I can't tell them apart. You see, no matter how I divide it, one or both of them will be angry with me. Their squabbling is driving me crazy… or did I mention that already?

ASSISTANT: Your memory serves you well. But I wonder, if two sons' squabbling is driving you crazy, how will you like it when you have eight grandchildren arguing over how to divide the kingdom? Or thirty-two great-grandchildren? Or a hundred-and-twenty-eight great-great-grandchildren? If you're not crazy yet, that should do it.

KING: Come to think of it, the longer I put off making a decision, the worse it will get. I suppose I'll have to make the best of my situation for as long as I can. You've been more helpful than you can imagine. I'm glad the fairy godmother was away. I must be on my way.

NARRATOR: He smiled as though a great burden had been lifted from his back. He headed for the door, opened it, and was almost gone when he turned and said,

KING: I want you to forget that I was ever here… or did I mention that already?

NARRATOR: He reached into his pocket and pulled out a bag of gold coins, which he handed me. He didn't see me collapse into the armchair and pull out a handkerchief to wipe my face. This had been a most unusual day, and I was anxious to relax in a tub full of hot water and bubbles. (I'd found an excellent bubble bath in the fairy godmother's potion cabinet.) The next morning was uneventful. I'd slept well and was ready for anything. Then , around noon, "anything" happened. Who do you think knocked at the fairy godmother's door just as I was starting to think about lunch? Prince Sherman and Prince Herman! The first thing I noticed when I let them in was how angry they looked. They were arguing about something on the doorstep, and they continued to argue as I opened the door.

SHERMAN: I want the horses and the stables so I can play polo.

HERMAN: No way. I like to ride, too.

ASSISTANT: Excuse me, Your Highnesses. I'm afraid the fairy godmother isn't here. I'm her assistant.

SHERMAN: That's all right. Our father, the king, sent us to see you.

ASSISTANT: He sent you to see me?

HERMAN: That's right. You see, he told us he's very sick and doesn't have long to live. And he said we'd have to figure out how to divide up the kingdom ourselves.

SHERMAN: And… he said if we couldn't figure it out, to come and see you. Which is why we're here.

ASSISTANT: What do you expect me to do? You know, I'm just the fairy godmother's assistant. I don't do magic.

HERMAN: We know all that. But father said that what you do is better than magic.

ASSISTANT: I-I- I'm fl-flattered.

SHERMAN: So we'd like you to divide up the kingdom for us.

ASSISTANT: I don't suppose I can refuse a royal command.

SHERMAN: What do you mean?

ASSISTANT: You see, if I decide how to divide the royal kingdom, then you'll both be mad at me, because I can't possibly make you both happy. But I do have a few suggestions.

HERMAN: Such as?

ASSISTANT: Ahem. Well, you could both renounce the throne and let your cousin Fritz rule. Or you could share the throne and rule together.

SHERMAN: Impossible!

HERMAN: Disastrous!

SHERMAN: We can't agree about anything. Well, almost anything. We both agree that's a stupid idea.

ASSISTANT: Then there is only one other option. Prince Sherman, you divide the kingdom as evenly as you can. Prince Herman, you choose which half you want.

NARRATOR: Prince Sherman looked at Prince Herman. Prince Herman looked at Prince Sherman. They smiled. Then they looked at me. Still smiling, they both reached into their pockets, pulled out bags of gold coins, and handed them to me at the same time. Then they walked out the door with their arms on each other's shoulders. They barely made it through the door. I can't believe it! I said to no one in particular as soon as I'd collapsed into the armchair again. Thank goodness there were no more visitors that day. I'd had all the excitement I could handle.

That night over dinner, I wondered whether Ella ever went to the royal ball. The next day I found out. Just before noon she knocked on the front door. She was carrying a satchel and looking tired but happy. I was about to ask, "How was the ball?" but she started talking before I could say a word.

ELLA: The ball was great! The music! The food! The dancing! Everything! I would never have gone without your help!

ASSISTANT: Thanks. But I can't take any credit. You did it all yourself. By the way, what's in your satchel?

ELLA: All my belongings. After attending the royal ball, I really couldn't go back to living with my stepmother and stepsisters. So I decided to move to town and open up a dressmaker's shop. I really am a good seamstress, you know. I just came by to thank you and to tell you the latest news from court. Last night, the king announced he was stepping down from the throne so he could travel. He turned the throne over to Prince Herman-all except the stables. Apparently, Prince Sherman had decided to devote himself to polo.

ASSISTANT: I'd like to be your first customer. I'll be in to see you for a fitting next week.

ELLA: Thanks. Maybe we can go to the royal ball together next year.

ASSISTANT: I'd love to. But next year we'll go in style. We'll rent a coach for the evening. And we'll both wear dancing slippers, too.

NARRATOR: Ella walked out the door laughing. The fairy godmother returned the next day. She didn't seem surprised when I told her all the things that had occurred while she was away.

GODMOTHER: I told you when I left that you could handle whatever came up.

NARRATOR: I wonder if those were magic words.
```

---

## IC-1136: Family Business

- Title: Family Business
- Author (byline): Simon Rich
- Work: Spoiled Brats (Pg 129-148)
- Publisher: Back Bay Books
- Publication date as stated: May 2015
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, FATHER, MOTHER, FITZBAUM, FIRST LADY
- Teaser before the introduction: Yes
- Spoken words (computed): 1199
- Already set (do not supply): none

### Source block (context only)

```text
Author: Simon Rich
Book: Spoiled Brats (Pg 129-148)
ISBN: 978-0316368650
Publisher: Back Bay Books
Date (Month/Year): May 2015
```

### Introduction (context only: never use it for content warnings)

```text
For most of history, what we did for a living was decided for us by our families. We would either join the family business or accept their suggestions for what we might do. On the surface, most families claim to have no interest in their children doing any job in particular. They simply “want us to be happy.” Or do they?

Welcome to the Jungle . . . where this set of chimpanzee parents have more than a little trouble accepting their child’s career choice.

Family Business by Simon Rich
```

### Performance text (classify this)

```text
NARRATOR: I love my father, but sometimes he can get on my nerves. It’s hard to explain why exactly. It’s just little things he does, here and there, that bother me. For example, sometimes he *poops* into his hands and then throws it into my face while jumping up and down and screaming. I know he’s just trying to be funny. But I’ve asked him politely not to do it anymore, but I always get the same reaction.

FATHER: (rolling his eyes) I’m sorry, your majesty.

NARRATOR: My father’s been calling me “your majesty” for as long as I can remember. He does it whenever I rinse off fruit before eating it or catch grubs with a stick instead of my fingers. Basically, he does it whenever I do anything differently than he does. When I told him I was thinking about going to school, he didn’t even respond. He just kept picking dirt out of his belly button. (to father) There’s a human scientist interviewing chimpanzees to see if any have the aptitude to learn sign language.

FATHER: (laughing) And you think they’re going to pick you. I’d like to see that.

MOTHER: Why can’t you just stay here? There are plenty of job opportunities. I talked to your Uncle Mike and he said he’d help you find work at the *poop* pile.

FATHER: It’s good, honest work. Decent pay, great benefits. You think you’re too good for it?

NARRATOR: No! Dad, relax. I’m just interested in sign language. I think it would be a cool thing to study.

FATHER: (snorting) So you get into this fancy program and spend years learning sign language. What are you supposed to do with that afterward? Teach?

MOTHER: You know, your father was pretty big in the human world when he was young. (nudging him) Tell him about the time you met you-know-who.

FATHER: So, this one time, I’m hanging out in my nest, when Jane pops over—”

MOTHER: (whispering) He means Jane Goodall.

FATHER: (grinning, with bravado) So Jane opens her banana crate, and she says to me, ‘How about a banana?’ And so I say, ‘How about many bananas?

MOTHER: (laughs hysterically)

NARRATOR: (grimacing, to audience) My father’s been telling us his Goodall anecdote for years. What does that even mean? Many bananas? That’s not even a joke. (to father) Where did you say you met Jane Goodall?

FATHER: (cautiously) My nest.

NARRATOR: So, on top of a tree? That’s pretty interesting. Because the trees we nest in are very tall. And humans usually aren’t that great at climbing. She must have been pretty athletic to make it all the way up to your nest. And to carry a crate with her, no less, one that was filled with, as you say, many bananas—that’s really impressive.

FATHER: (tensely with flared nostrils) I don’t know what to tell you. That’s how it happened.

NARRATOR: I always knew your friend Jane was smart, but I had no idea she was also the strongest human in the history of— (a clump of poop lands on his/her face. Coughing and sputtering, while wiping it away).

MOTHER: (ready to launch another clump) Don’t you ever disrespect your father like that again.

(she stares angrily then gallops off screaming) ***** The Next Day *****

NARRATOR: I met with the scientists.

FITZBAUM: Here, chimpy, chimpy. Who wants to win a banana?

NARRATOR: They said I was the smartest chimp they’d ever seen.

FATHER: (he and mother are grooming each other, disinterested) La di da. Good for you.

MOTHER: It was a big day at the *poop* pile. (proudly) Your father found three grubs.

FATHER: The trick is to feel around in the *poop*. The grubs are sometimes at the bottom, so you need to reach down. (demonstrating)

MOTHER: You’re so smart. The smartest, most wonderful—

NARRATOR: (interrupting) I’m flying to Stanford tomorrow. It’s in a human country called the U.S.A.

MOTHER: (fearfully) A human country? Like Zimbabwe?

NARRATOR: Yeah, but bigger.

FATHER: (snorting) Bigger than Zimbabwe? Not likely. How come I’ve never heard of it?

MOTHER: (whimpers)

NARRATOR: Mom, come on. Don’t whimper. This is my chance to get out of this town. To see the world.

FATHER: (suddenly angry, he roars) Then go! Go have fun with your fancy human friends! (baring his teeth in a grimacing smile) Just don’t come crawling back to me when you fail. *****5 Years Later at the White House*******

FIRST LADY: (to a large audience, she speaks into a microphone) Ladies and gentlemen. In honor of Earth Day, we have a very special speaker. Please ‘go ape’ for . . . Professor Chimpsky!

NARRATOR: (signing – left paw to lips) Thank you. Thank you. Thank you. Thank you. (to audience) There were dozens of cameras trained on me, broadcasting my speech all over the world. I was determined to do my species proud. (Signing and speaking aloud- See NOTE at end of selection for ASL resource link) Environment good. Peace. Earth Day. Hello. Peace. Me chimpanzee. Peace. Thank you. Goodbye. (to audience) The crowd burst into applause. The speech had been an enormous success—far greater than I had even hoped. It was the pinnacle of my entire career. Still, as usual, I had trouble enjoying my triumph. (sadly) I hadn’t had any contact with my parents since the day I left the jungle. Part of me wished they could see how far I’d come. In just five years, I’d amassed more accolades than any chimp in history. My mastery of sign language was so vast and fluent that it had earned Professor Fitzbaum a MacArthur “genius” grant. My face had appeared in every magazine on earth.

A caterer set down a tray of champagne flutes. Fitzbaum was busy talking to some reporters. I grabbed two flutes. I was starting to feel a bit light-headed, but I didn’t care. I was almost finished with my champagne when Professor Fitzbaum returned.

FITZBAUM: (signing and speaking) Stop. No. Give (pointing to the champagne) Give.

NARRATOR: A crowd had formed. There were dignitaries, reporters, and—most troubling of all—a man holding a dart gun. (stamping his feet and pounding his chest – he roars) Everyone was overreacting. I jumped onto a table and collided with a large ice sculpture of a globe. I don’t remember much after that. Just the sound of shouting, the smell of grass, and a sharp little pain in my thigh. (beat, then with shame) I woke up in a cage. I was starting to despair when Professor Fitzbaum walked into the room. (to Fitzbaum signing frantically and speaking) Hello! Hello! (to audience) My friend had come to get me, just like I’d known he would. (signing again) Thank you. Hello. Me chimpanzee. Good. Please. Friends.

(clinging to the bars of the cage)

FITZBAUM: (no signing, he is resigned) I’m sorry, but our facilities can’t accommodate a full-grown chimpanzee. (Narrator begins to sob) Don’t worry, you don’t have to stay here. I’m taking you home. ***** Back in the Jungle*****

FATHER: Guess it didn’t work out, huh? Well, don’t say I didn’t warn you.

MOTHER: It’s O.K. I’ve already talked to Uncle Mike, and there’s a place for you at the *poop* pile. (she hands him a few grubs, which he tries to eat, but they are disgusting now. Makes a horrible face)

FATHER: (with his mouth full of grubs) What’s the matter? Not fancy enough for you?

NARRATOR: Dad. I just got back. Please . . . (unconsciously signing the last word)

FATHER: (gasping) What the hell are you doing?

NARRATOR: It’s sign language. Look, I’ll show you. (to audience) I tried to teach them “Thank you” the easiest sign I knew. (paw to lips)

FATHER: (laughing) I can’t believe you spent five years on that nonsense. What a waste.

NARRATOR: (defiantly) It wasn’t a waste. I got to do all sorts of amazing things— I got to go to the White House.

FATHER: (unimpressed) What’s that?

NARRATOR: It’s where the President of the United States lives. (Father snorts)

MOTHER: You know, your father once met a celebrity. Honey, tell him about the time you talked to you-know-who.

FATHER: Oh, all right. So, one time, I’m in my tree, and Jane—

MOTHER: He means Jane Goodall. (aside – she whispers to Narrator sadly) He’s old! Can’t you see he’s old?

NARRATOR: (rolling his eyes, but then realizing that Father is indeed quite old and sad) I love my father (to Father) Dad, I’m hungry. I never ate dinner. I wish there were grubs I could eat. (poking at the ground and feigning confusion) I’m not good at it. I need help from an expert—someone who knows about grubs and about *poop*

FATHER: (with renewed swagger) I can help. The trick is to really get in there with your paws. See? (pulls out a grub and hands it to Narrator)

NARRATOR: (forced smile) Thanks. (shoves the grub into his/her mouth) Mmm. Delicious. You’re good at hunting grubs. I’m really impressed.

FATHER: (beating his chest he roars triumphantly)
```

---

## IC-1137: Fantastic Mr. Fox

- Title: Fantastic Mr. Fox
- Author (byline): Roald Dahl
- Work: Not specified
- Publisher: Puffin
- Publication date as stated: June 1998
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MR. FOX, BOGGIS, BUNCE, BEAN, MRS. FOX, BADGER, RAT, GROUP
- Teaser before the introduction: Yes
- Spoken words (computed): 1516
- Already set (do not supply): none

### Source block (context only)

```text
Author: Roald Dahl
ISBN: 978-0141301136
Publisher: Puffin
Date (Month/Year): June 1998
```

### Introduction (context only: never use it for content warnings)

```text
Someone's been stealing from the three meanest farmers around, and they know the identity of the thief—it's Fantastic Mr. Fox! Working alone they could never catch him; but now fat Boggis, squat Bunce, and skinny Bean have joined forces, and they have Mr. Fox and his family surrounded. What they don't know is that they're not dealing with just any fox—Mr. Fox would rather die than surrender. Only the most fantastic plan can save him now.

Nobody outfoxes the . . . Fantastic Mr. Fox by Roald Dahl
```

### Performance text (classify this)

```text
NARRATOR: (Pgs 1-4) Down in the valley there were three farms. The owners were rich, nasty men: Farmer Boggis, Farmer Bunce and Farmer Bean. Boggis was an enormously fat chicken farmer. (mimes Boggis) He ate three boiled chickens smothered with dumplings every day for breakfast, lunch and supper. Bunce was a duck-and-goose farmer. (mimes Bunce) He was a potbellied dwarf. His food was doughnuts and goose livers. He mashed the livers into a disgusting paste and then stuffed the paste into the doughnuts. Bean was a turkey-and-apple farmer. (mimes Bean) He never ate any food at all. Instead, he drank gallons of strong cider which he made from the apples in his orchard. He was as thin as a pencil and the cleverest of them all.

NARRATOR: (Pgs 7-9) On a hill above the valley lived Mr. and Mrs. Fox and their four small foxes. Every evening as soon as it got dark Mr. Fox would say . . .

MR. FOX: Well, what shall it be this time? A plump chicken from Boggis? A duck or a goose from Bunce? Or a nice turkey from Bean?

NARRATOR: And when Mrs. Fox had told him what she wanted, Mr. Fox would creep down into the valley in the darkness of the night and help himself.

BOGGIS: Dang and blast that lousy beast!

BUNCE: I'd like to rip his guts out!

BOGGIS: How on earth can we catch the blighter?

BEAN: (picking his nose delicately) I have a plan. Tomorrow night we will all hide just outside the hole where the fox lives. . . wait there until he comes out. Then ... (mimes a shotgun) Bang! Bang-bang-bang!

MR. FOX: (Pg 10-14) What shall it be tonight?

MRS. FOX: Bring us two fat ducks, if you please. One for you and me, and one for the children. Just don't get careless. You know they'll be waiting for you, all three of them.

MR. FOX: Don't you worry about me. I’ll see you later.

NARRATOR: But Mr. Fox would not have been quite so cocky had he known the three farmers were waiting just outside the entrance to the hole, each one crouching behind a tree with his gun loaded.

MR. FOX: (creeping to the mouth of his hole, he pokes his face out and sniffs)

BEAN: (mimes a shotgun) Bang-bang! Bangbang! Bang-bang! (to the others) Did we get him?

(he finds the remains of a fox’s tail and picks it up, disappointed) We got the tail but we missed the fox.

BUNCE: He won't be poking out again in a hurry.

BEAN: It'll take three days at least before he gets hungry enough to come out again. I'm not sitting around here waiting for that. Let's dig him out!

MR. FOX: (Pg 15-19) (Glumly while Mrs. Fox tends to his tail) It will never grow again. I shall be tail-less for the rest of my life. I suppose I'm lucky to be alive at all. And now they've found our hole, we're going to have to move out as soon as possible. We'll never get any peace if we. . . What was that? (he turns his head sharply and listens)

NARRATOR: Suddenly there was an especially loud crunch above their heads and the sharp end of a shovel came right through the ceiling.

MR. FOX: Come on! There's not a moment to lose! (beginning to dig) Nobody in the world can dig as quick as a fox! Go downwards! We've got to go deep! (frantic digging)

MRS. FOX: (panting for breath; to their children) I should like you to know that if it wasn't for your father we should all be dead by now. Your father is a fantastic fox.

BOGGIS: (Pg 20-22) (exhausted from digging) Dang and blast! Whose rotten idea was this?

BEAN: (angrily) Listen. I'm going to get that fox! I'm not giving in till I've strung him up over my front porch, dead as a dumpling! What we need is machines . . . mechanical shovels!

NARRATOR: Soon, two enormous caterpillar tractors came clanking into the wood. They were murderous, brutal-looking monsters. Now there began a desperate race, the machines against the foxes.

BEAN: (Pg 27) Hey there, Mr. Fox! We're coming to get you now!

MR. FOX: (Pg 23) Tractors! And mechanical shovels! Dig for your lives! Dig, dig, dig!

BOGGIS: (Pg 27) You've had your last chicken! You'll never come prowling around my farm again!

NARRATOR: (Pg 29) At six o’clock in the evening. Bean switched off his tractor and climbed down from the driver's seat. Bunce did the same. Both men had had enough. (Pg 28) The hole was like the crater of a volcano.

BOGGIS: (Pg 29-30) Dang and blast that filthy stinking fox! What the heck do we do now?

BEAN: There's only one thing to do. We starve him out. We camp here day and night watching the hole. He'll come out in the end. He'll have to.

NARRATOR: (Pg 34-36) For three days and three nights this waiting-game went on. Down in the tunnel the foxes were slowly but surely starving to death.

MR. FOX: (deep in the new tunnel) I’ve just had an idea. It means more digging. (Mr. Fox and the children begin digging again)

NARRATOR: (Pg 38-39) For a long, long time they kept on digging. Slowly, wearily, the foxes began to slope the tunnel up towards the surface.

MR. FOX: (Pg 40) (cautiously poking his head up through the gap; he shrieks in excitement) I've done it! I've done it (he pulls himself up though the gap and starts dancing with joy) Come up and see where you are! Hallelujah! Hooray! Hooray! Boggis's Chicken House Number One! Isn't that fantastic!

NARRATOR: Mr. Fox chose three of the plumpest hens, and with a clever flick of his jaws he killed them instantly.

BADGER: (Pg 46-47) (a deep voice from the shadows) Who goes there?

MR. FOX: Badger!

BADGER: Foxy! Haven't you heard what's happening up on the hill? It's chaos! Half the wood has disappeared and there are men with guns! What on earth are we going to do, Foxy? None of us can get out, even at night! I think we're finished!

MR. FOX: Who is we?

BADGER: All us diggers. Me and Mole and Rabbit and all our wives and children. Even Weasel, who can usually sneak out of the tightest spots, is right now hiding down my hole with Mrs. Weasel and six kids.

MR. FOX: (Pg 42) (handing the hens to one of the children) Run back with these to your mother. Tell her to prepare a feast. [We’ll] be along in a jiffy, as soon as we have made a few other little arrangements. (Pg 49) (to Badger) You have come just at the right moment, my dear Badger. You can help us dig.

BADGER: (Pg 58-59) (while they are digging) Doesn't this worry you just a tiny bit, Foxy? All this. . . this stealing.

MR. FOX: (looks at Badger as if he is crazy) My dear old furry frump. do you know anyone in the whole world who wouldn't swipe a few chickens if his children were starving to death? (Pg 60-61) We shall simply take a little food here and there to keep us and our families alive. Right?

NARRATOR: Five minutes later, Badger's front paws hit against something flat and hard. It was a wall. But it was built of bricks, not stones. Mr. Fox saw that the cement between the bricks was old and crumbly (Mr. Fox and Badger begin loosening bricks)

RAT: Go away! You can’t come in here! It’s private!

BADGER: Good Lord! It’s Rat! (Pg 74) All rats have bad manners. I've never met a polite rat yet.

MR. FOX: (Pg 62) (smiling widely and speaking softly) My dear Rat, I am a hungry fellow and if you don't hop it quickly I shall eat-you-up-in-one-gulp!(Mr. Fox and Badger break down the wall and climb through) (Pg 64-66) Bean's Secret Cider Cellar. It will make the feast into a banquet!

BADGER: Cider is especially good for Badgers. We take it as medicine -- one large glass three times a day. (He drinks deeply) Oh, Foxy, it's like drinking sunbeams and rainbows!

RAT: You're poaching! Put that down at once! There'll be none left for me! If you great clumsy brutes come messing about in here, we'll all be caught!

NARRATOR: (Pg 71) Mr. Fox and Badger ran across the cellar clutching a gallon jar each.

RAT: Thieves! Robbers! Bandits! Burglars!

NARRATOR: (Pg 72-73) Along the tunnel they flew. . . past Boggis's Chicken House Number One and then up the long home stretch towards the place where they knew Mrs. Fox would be waiting. They rounded the final corner and burst in upon the most wonderful sight they had ever seen. The feast was just beginning. A large dining-room had been hollowed out of the earth, and in the middle of it, seated around a huge table, were no less than twenty-nine animals: foxes and badgers, moles and rabbits . . . weasels! (Pg 76-77) You must remember no one had eaten a thing for several days. They were ravenous. So for a while there there was only the sound of crunching and chewing as the animals attacked the succulent food. (chewing, burping, assorted other noises) At last, Badger stood up.

BADGER: (raising his glass of cider) A toast! To our dear friend who has saved our lives this day Mr. Fox.

GROUP: (shouting) To Mr. Fox! Long may he live!

MRS. FOX: (shyly) I don't want to make a speech. I just want to say one thing: MY HUSBAND IS A FANTASTIC FOX. (cheering and clapping)

MR. FOX: (Pg 78-81) (grinning hugely) Thank you. But now, my friends, let us be serious. Let us think of tomorrow and the days after that. If we go out, we will be killed. Right?

GROUP: (shouting) Right!

MR. FOX: But who wants to go out, anyway? We are all diggers. We hate the outside. We only go out because we have to, to get food for our families. But now, my friends, we have a safe tunnel leading to the finest stores in the world! It means that none of us need ever go out into the open again! I invite you all to stay here with me forever.

GROUP: Forever!

MR. FOX: We will make an underground village, with streets and separate houses for Badgers and Moles and Rabbits and Weasels and Foxes. And every day we will eat like kings. (cheering and clapping)

NARRATOR: Outside the Fox’s hole, Boggis and Bunce and Bean sat with their guns on their laps. It was beginning to rain. Water was trickling down the necks of the three men and into their shoes.

BOGGIS: (miserably) He won't stay down there much longer now.

NARRATOR: [And] They sat there by the hole, waiting for the fox to come out. So far as I know, they are still waiting.

BEAN: (sneezes loudly)
```

---

## IC-1138: Finger Food

- Title: Finger Food
- Author (byline): Nina Shengold
- Work: Telling Tales: New One Act Plays
- Publisher: Penguin Books
- Publication date as stated: 1993
- Event as filed: Humorous Interpretation
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

## IC-1139: Five Things White People Love

- Title: Five Things White People Love
- Author (byline): Trevor Noah
- Work: Not specified
- Publisher: Scraps From the Loft.com
- Publication date as stated: December 21, 2023
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1354
- Already set (do not supply): none

### Source block (context only)

```text
Author: Trevor Noah
ISBN: On-Line Transcript
https://scrapsfromtheloft.com/comedy/trevor-noah-where-was-i-transcript/
Publisher: Scraps From the Loft.com
Date (Month/Year): December 21, 2023
```

### Introduction (context only: never use it for content warnings)

```text
Five Things White People Love from The Netflix Comedy Special Where I Was by Trevor Noah
```

### Performance text (classify this)

```text
I had a fight with my friend [the other day]. He’s like, “Dude, why don’t we go check out all the museums.”

I was like, “Maybe like one.”

He said, “What do you mean, one? You know how many amazing museums they got?”

“Yes, but it’s still a museum. I’ll do like one, and that’s it. I can’t do as many as you.”

“What do you mean you can’t do as many as me?”

“Dude, because you’re white, like, you enjoy doing that.” And I was just joking. I was just

teasing him. Just teasing him. He got so offended so quickly, right?

He’s like, “What did you say? Because you’re. . . Dude, white people don’t love museums.

“What are you even talking about? Like, museums aren’t even in the top five things white

people love, okay?”

He said it with such confidence. and with such conviction, I was like, “What is the top five?”

I thought about it. I was like, “No, it is.” I stick with my decision.

White people love museums. A lot of people enjoy museums, but white people love museums. Love museums. There’s not a single place on Earth where white people have settled and not built a museum. It doesn’t matter. White people love museums. You ever seen white people in a museum? Walking around smiling with their hands behind their back? “Yep, that was us.” “That was us, too.” “It’s been a good run.” White people love museums. I wouldn’t put it at number one, but it’d be in the top five. I thought about it. If there were top five things white people love, I’d put museums at number five. At number four, I’d put swimming. All right? ‘Cause white people love swimming. Nothing wrong with that. Have you seen white people swim? You look stunning. Stunning. When white people swim, you do that thing with your hair. You come out of the water, like. . . (imitates whooshing and a dramatic hair toss)

Just go perfectly back like a duck. I would love swimming, too. White people love swimming. White people love swimming so much, that they made it that you can win more medals at the Olympics, swimming, than any other discipline. Yeah, that’s how much white people love swimming. I realized this one day. There was an argument going on about who the greatest Olympian of all time is. And the final two was Michael Phelps and Usain Bolt. And then one of the arguments was, “Well, Michael Phelps is better because he has more medals.” And I was like, “Yeah, because he cheated -- He won them swimming.” I’m not saying Michael Phelps is not great. I’m saying you can’t count the medals in the argument. Because in swimming it’s the only discipline where you win more medals for doing the same thing in a slightly less efficient manner. It makes no sense. Think about it. It’s like, “100-meter freestyle.” (imitates beep)

[panting] Done. Gold medal. Yeah. And now this. (demonstrates another swimming style) Another medal. Yeah. And this one? (another style demonstration) Another medal. But what about this one? (another style demonstration) Another medal. That’s some bull***. I don’t care what anyone says. You can’t win more medals. Usain Bolt doesn’t have that luxury. When Usain Bolt runs, it’s the 100-meter and it’s done. “On your marks, set. . . Run, run, run, run. Get to the end, win, gold medal. That’s it. He can’t turn around like, “Amazing race. And now I’m going to do it butterfly style.” (demonstrates a ridiculous running style) It’s not a thing. I mean, it should be, but it’s not. White people love swimming, so they made up the rule. I get it. It would have to be, yeah. Of my top five things, I’d go -- museums at number five, swimming at number four.

Number three, being flabbergasted. White people love being flabbergasted. Come on. You know exactly what I’m talking about. Have you ever seen when a white person’s having a bad day, something’s gone wrong, they do that thing with their face, get flabbergasted like. . .

(extreme facial expressions, hand gestures) White people love being flabbergasted. You’ll see it in supermarkets all the time. There’s like a long line. All right? But only one cashier is open. Everyone’s standing patiently. There’s always one white person who pops out like. . . (with extreme facial expressions, hand gestures) “Why don’t they open the other. . . Are you serious? What are they. . . Are you. . .“ The only thing white people love more is finding another white person to flabbergast with. Have you seen that? Yo, whenever that happens, magic. It is absolute magic. A white person will be flabbergasting. They’ll make eye contact with another white person, and then they’ll flabbergast together. It’s like they Voltron their flabbergasting into a super flabbergast. You see them look over. (extreme facial expressions, hand gestures) “You see this?” “I know.” (sighing) That’s one of the keys to flabbergasting. You have to exhale. Let it all out. Life is so hard that the air has to leave your body. You can no longer even breathe. (sighing heavily) That’s why there’s so many tornadoes in the Midwest. It’s just white people flabbergasting. . . (sighing vigorously)

White people love being flabbergasted. Has to be. Has to be top five. That would be my list. Top five things white people love. I’ve got museums at number five. All right, swimming at number four. Being flabbergasted, number three.

Number two, being white. It’s a sweet gig. I don’t blame you.

And then there’s number one. And look, this is my personal list. I’m not dictating anything. If you don’t agree, make your own, right? It’s a personal preference. But there is one thing, and one thing alone, that white people love more than anything on this planet. “Sweet Caroline.” Let me tell you something. There is nothing that brings more joy to the soul of a white person than the sounds of that Neil Diamond song. I don’t care where it is. I’ve been on every continent, in many countries. When that song plays, you see white people’s eyes light up. . . like sleeper agents who’ve just been activated. It happens every time, without fail. Every single time. It’s not about music, other songs will be playing. They’ll be at a cookout or a baseball game, a company event. All the other songs are in the background. They pay them no heed. But when that song kicks in, it taps into the very DNA of whiteness. I don’t know what it is. But it interrupts everything else. You’ll see white people hanging out. They’ll be like,

“Yeah, business, mergers and acquisitions.”

“It’s one of those things.”

“I know, we should circle back.”

“Let’s put a pin in it.” (blabbering)

And that song comes in, and every single time. . . You think it won’t happen. It always creeps in. It always seems like it won’t happen. But it’s always the same, just like. . . . (sings)

♪ Hands, touchin’ hands ♪

♪ Reachin’ out, touchin’ me ♪

♪ Touchin’ you Pum, pum, pum ♪

♪ Sweet Caroline ♪

See, I didn’t tell you to join in. I didn’t say, “All together now.” Or, “On the count of three.” That was just your whiteness coming out. Did you feel that? Huh? That was just you. You were like, “This is it!” “This is our moment!” (to the tune of Sweet Caroline) ♪ Oh, oh, oh ♪ ♪ I’m white, white, white, white ♪ ♪ White, white ♪♪ Look at you right now. You’re beaming! Look at your face. Look at you. Don’t ever lose that joy. None of you white people. You hold on to it. It is a treasure. It is the most adorable thing in the world.

Nothing makes white people happier than that song. Nothing. That song is pure, uncut Caucasian joy. That’s what that song is. White people cannot resist it. Yeah, forget 23andMe. If you want to know how much white you have in you, play that song. The louder you respond, the whiter you are. I just saved you some money. There’s no white person I’ve seen. . . It is the Marco to your Polo. That’s what that song is. I’ll tell you, if there was ever, like, a giant earthquake, God forbid, and people were trapped beneath the rubble, I’d volunteer to find all the white people. I’ll be like, “You guys find everybody else.” “I got this. I got this!”

♪ “Sweet Caroline” ♪ “I found another one!” “You okay, man?”
```

---

## IC-1140: For Whom the Southern Belle Tolls

- Title: For Whom the Southern Belle Tolls
- Author (byline): Christopher Durang
- Work: Christopher Durang: Twenty-Seven Short Plays (Pg 9-30)
- Publisher: Smith and Kraus
- Publication date as stated: Jan 1995
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: AMANDA, LAWRENCE, GINNY
- Teaser before the introduction: Yes
- Spoken words (computed): 1441
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
Welcome to a twisted sendup of Tennessee Williams’ The Glass Menagerie! For Whom the Southern Belle Tolls by Christopher Durang
```

### Performance text (classify this)

```text
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

## IC-1141: The Frog Prince Continued

- Title: The Frog Prince Continued
- Author (byline): Jon Scieszka
- Work: Not specified
- Publisher: Viking Juvenile
- Publication date as stated: May 1991
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, PRINCESS, PRINCE, WITCH 1, WITCH, WITCH 2, WITCH 3, FAIRY GODMOTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1042
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jon Scieszka:
ISBN: 978-0670834211
Publisher: Viking Juvenile
Date (Month/Year): May 1991
```

### Introduction (context only: never use it for content warnings)

```text
And they lived happily ever after . . .This is where most fairy tales end. The prince and princess marry and ride off into the sunset to begin their new life together as husband and wife, a life full of promise, romance, and above all, love. But no one has ever told us how this is supposed to happen, or why it succeeds if it does. In The Frog Prince Continued by Jon Scieszka, the truth behind happily ever after is revealed -- warts and all. (CROAK)

The Frog Prince Continued by John Scieszka
```

### Performance text (classify this)

```text
NARRATOR: The Princess kissed the frog, he turned into a prince and they lived happily ever after. Well, let’s just say they lived sort of happily for a long time. Okay, so they weren’t so happy. In fact, they were miserable.

PRINCESS: Stop sticking your tongue out like that.

PRINCE: How come you never want to go down to the pond anymore?

NARRATOR: The Prince and Princess were so unhappy. They didn’t know what to do.

PRINCESS: I would prefer that you not hop around on the furniture. And it might be nice if you got out of the castle once in a while to slay a dragon or giant or whatever.

NARRATOR: The Prince didn’t feel like going out and slaying anything. He just felt like running away. But then he reread his book. And it said right there at the end of his story: “They lived happily ever after. The End.” So he stayed in the castle and drove the Princess crazy. Then one day, the Princess threw a perfectly awful fit.

PRINCESS: First you keep me awake all night with your horrible, croaking snore. Now I find a lily pad in your pocket. I can’t believe I actually kissed your slimy frog lips. Sometimes I think we could both be better off if you were still a frog.

NARRATOR: That’s when the idea hit him. The Prince thought . . .

PRINCE: Still a frog . . .Yes! That’s it!

NARRATOR: And he ran off into the forest, looking for a witch who could turn him back into a frog. The Prince hadn’t gone far when he ran into just the person he was looking for.

PRINCE: Miss Witch, Miss Witch. Excuse me, Miss Witch. I wonder if you could help me?

WITCH 1: Say, you’re not looking for a princess to kiss are you?

PRINCE: Oh, no. I’ve already been kissed. I’m the Frog Prince. Actually, I was hoping you could turn me back into a Frog.

WITCH: Are you sure you’re not looking for a beautiful sleeping princess to kiss and wake up?

PRINCE: No, no -- I’m the Frog Prince.

WITCH: That’s funny. You don’t look like a frog. Well, no matter. If you’re a prince, you’re a prince. And I’ll have to cast a nasty spell on you. I can’t have any princes waking up Sleeping Beauty before the hundred years are up.

NARRATOR: The Prince didn’t stick around to see which nasty spell the witch had in mind. He ran deeper into the forest until he came to a tiny cottage where he saw another lady who might help him.

PRINCE: Miss Witch, Miss Witch. Excuse me, Miss Witch. I wonder if you could help me. I’m a prince and---“

WITCH 2: Eh? What did you say? Prince?

PRINCE: No, I mean, yes. I mean, no, I’m not the prince looking for Sleeping Beauty. But, yes, I’m the Frog Prince. And I’m looking for a member of your profession who can turn me back into a frog so I can live happily ever after.

WITCH: Frog Prince, you say? That’s funny. I thought frogs were little green guys with webbed feet. Well, no matter: If you’re a prince, you’re a prince. And I can’t have any princes rescuing Snow White. Here- eat the rest of this apple.

NARRATOR: The Prince, who knew his fairy tales (and knew a poisoned apple when he saw one), didn’t even stay to say, “No Thank you.” He turned and ran deeper into the forest. Soon he came to a strange-looking house with a witch outside.

PRINCE: Ahem. Miss Witch, Miss Witch. Excuse me, Miss Witch. I wonder if you could help me? I’m the Frog-

WITCH 3: If you’re a frog, I’m the King of France.

PRINCE: No, I’m not a frog. I’m the Frog Prince. But I need a witch to turn me back into a frog so I can live happily ever after, can you do it?”

WITCH: (eyeing the Prince and licking her lips) Why, of course, dearie. Come right in. Maybe I can fit you in for lunch.

NARRATOR: The Prince stopped on the slightly gummy steps. Something about this house seemed very familiar. He broke off a corner of the windowsill and tasted it. Gingerbread.

PRINCE: I hope you don’t mind my asking, Miss Witch. But do you happen to know any children by the name of Hansel of Gretel?

WITCH: Why yes, Prince darling, I do. I’m expecting them for dinner.

NARRATOR: The Prince who, as we said before, knew his fairy tales, ran as fast as he could deeper into the forest. Soon he was completely lost. He saw someone standing next to a tree. The Prince walked up to her, hoping she wasn’t a witch, for he’d quite had his fill of witches.

PRINCE: Madam. I am the Frog Prince. Could you help me?”

FAIRY GODMOTHER: Gosh, do you need it. You are the worst-looking frog I’ve ever seen.

PRINCE: I am not a frog. I am the Frog Prince and I need someone to turn me back into a frog so I can live happily ever after.

FAIRY GODMOTHER: Well, I’m on my way to see a girl in the village about going to a ball, but I suppose I could give it a try. I’ve never done frogs before, you know.

NARRATOR: And with that the Fairy Godmother waved her magic wand and turned the Prince into a beautiful carriage. The Prince couldn’t believe his rotten luck. The sun went down. The forest got spookier. And the Prince became more and more frightened.

PRINCE: Oh, what an idiot I’ve been. I could be sitting at home with the Princess, living happily ever after. But instead, I’m stuck here in the middle of this stupid forest, turned into a stupid carriage. Now I’ll probably just rot and fall apart and live unhappily ever after.

NARRATOR: The Prince thought these terrible, frightening kinds of thoughts (and a few worse- too awful to tell), until far away in the village the clock struck midnight. The carriage instantly turned back into his former Prince self and ran by the light of the moon until he was safe inside his own castle.

PRINCESS: Where have you been? I’ve been worried sick. You’re seven hours late. Your dinner is cold. Your clothes are a mess.

PRINCE: The Prince looked at the Princess who had believed him when no one else in the world had, the Princess who had actually kissed his slimy frog lips. The Princess who loved him.

NARRATOR: The Prince kissed the Princess. They both turned into frogs. And they hopped off happily ever after. (CROAK)
```

---

## IC-1142: Fully Committed

- Title: Fully Committed
- Author (byline): Becky Mode
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: March 2001
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: SAM, MRS. VANDEVERE, STEPHANIE, MRS. VANDEVER, OSCAR, CHEF, R-F, JEAN-CLAUDE, BRYCE, CURTIS
- Teaser before the introduction: Yes
- Spoken words (computed): 1425
- Already set (do not supply): none

### Source block (context only)

```text
Author: Becky Mode
ISBN: 978-0822217688
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): March 2001
```

### Introduction (context only: never use it for content warnings)

```text
Meet Sam, a struggling actor/actress waiting for his/her big break. In the meantime, he/she make ends meet by taking reservations at the most in-demand high-end restaurant in Manhattan. Fortunately many of the skills Sam uses at the restaurant can readily be applied to his/her future stage career: How to deal with difficult people . . . . Staying calm, no matter what . . . and the beautiful art of improvisation!

Fully Committed by Becky Mode
```

### Performance text (classify this)

```text
Phones are ringing. Sam rushes in, put on his/her headset with a crazy frantic energy and . . .

SAM: (Pg 11) Good morning reservations; could you hold please? (multiple lines continue to ring throughout this exchange)

MRS. VANDEVERE: Is the chef there?

SAM: No, he’s not. Could you hold please?

MRS. VANDEVERE: Is Jean-Claude there?

SAM: No, he’s not, could you hold please?

MRS. VANDEVERE: Is Bob there?

SAM: No, he’s not. Could you hold on for one second?

MRS. VANDEVERE: Ye-es

SAM: Good morning, reservations, could you hold please?

SAM: (Pg 13-14) (buzzes upstairs) Hey, Stephanie. Have you seen Bob? (Phone rings)

STEPHANIE: No, but when he comes in will you tell him that there’s a photographer from Gourmet magazine who’s been waiting for the chef since eight-thirty. (Phone is still ringing)

SAM: Okay. (On to a new line) Reservations, could you hold please?

MRS. VANDEVER: No, I tried that before. Who am I speaking with?

SAM: This is Sam.

MRS. VANDEVERE: (Suddenly kissing up) Sam, darling, I didn’t know you were still work there. It’s Bunny Vandevere (a beat) My husband is Dick Vandevere.

SAM: Oh, hi, how are you?

MRS. VANDEVERE: Well we’re exhausted; we’ve just come back from Tibet. Now, I know it’s last minute, but Mr. Vandevere and I want to come in tonight and we can be very flexible – anywhere between, say, seven-thirty and eight o’clock

SAM: Okay, one moment please. (Putting her on hold and buzzing upstairs) Hello. Jean- Claude? Oscar!! Oscar –

OSCAR: Sam, greeting and salutations. How are you?

SAM: Good, Oscar . . . hey, how VIP is Mrs. Vandevere?

OSCAR: V.V.V.V.I.P

SAM: She wants to come in tonight and I’m over by twenty-five.

OSCAR: Sam, her husband invented Saran Wrap!

SAM: (Back to Vandevere) Okay, Mrs. Vandevere. I just spoke to our business manager and you’re all set for tonight. How about seven-thirty? (Phone rings)

MRS. VANDEVERE: That’s marvelous, thank you so much Sam.

SAM: (Pg 17) (On to a new line) Thank you for holding, how can I help you?

ROSENSTEIN-FISHBURN (R-F): (Like a drill sergeant) First of all, I’ve been holding for ten minutes! Number two, you have to do something about that music. I need to speak to Jean-Claude regarding Friday evening. It’s Carolann Rosenstein-Fishburn.

SAM: He’s not in yet, can I – (Dial tone, she’s hung up) Hello? (Phone rings, Sam moves on to the new line) Good morning, reservations, could you hold please?

STEPHANIE: (Pg 19) (buzzing in) Sam! It’s the chef on line two.

SAM: (On to line two) Chef?

CHEF: (Still half asleep) What did we do last night?

SAM: (Checking a list) It looks like $22,700.

CHEF: What does lunch look like?

SAM: We’re all booked up.

CHEF: (Snarling) What did you just say? Did you forget my new policy?

SAM: No, we’re “fully committed”

CHEF: That more like it. (He hangs up, the phone rings)

SAM: (Pg 21-22) Reservations, could you hold please?

R-F: It’s Carolann Rosenstein-Fishburn calling for Jean-Claude. Did you forget to give him the message.

SAM: One moment please (Buzzing upstairs) Jean-Claude!

JEAN-CLAUDE: Allo, be brief. What can I do for you? (and then snippy) I’m trying to get ready for lunch up here!

SAM: Carolann Rosenstein-Fishburn on line four.

JEAN-CLAUDE: (Disgusted) Oh my God, I hate that lady. She’s has a face like a dog.

SAM: (Back to R-F) Okay, Mrs. Fishburn, I can’t find Jean-Claude, but I’ll have him call you as soon as he gets in.

R-F: Tell [him] it’s an urgent situation.

SAM: Are you sure there’s nothing I . . . (Dial tone; she’s hung up.) (On to the next line) (Pg 15-16) Thank you for holding, how can I help you?

BRYCE: (Frighteningly cheerful) Hi, this is Bryce calling from Naomi Campbell’s office!! Who’s this?

SAM: Sam.

BRYCE: (Pathologically excited to talk to Sam) Sam!!! I didn’t know you were still working there! How’s the acting career?

SAM: It’s okay.

BRYCE: (Gushing sympathy) Oh, it’s such a tough business! Hang in there! (quickly shifting gears) Okay, Naomi would like to come in this weekend with fifteen people, on Saturday night at eight PM and she’s gonna need a round, fee-standing table . . . number seventeen.

SAM: Of course.

BRYCE: And you know she doesn’t eat dairy, right? And no female waitstaff at the table!

SAM: Okay.

BRYCE: (Pg 22) Okay, so she definitely needs an all-vegan tasting menu. That’s a no-fat, no-salt, no-dairy, no-sugar, no-chicken, no-meat, no-fish tasting menu for fifteen okay?

SAM: Okay, I’ll make a note of that.

BRYCE: Super, thanks a trillion!

SAM: (Pg 26-27) (On to a new line) Thank you for holding, how can I help you?

MRS. VANDEVERE: Sam, it’s Bunny Vandevere. Listen, I forgot to tell you, we’re going to need table thirty-one tonight.

SAM: (Looking for his dinner list) Actually someone’s reserved table thirty-one tonight.

MRS. VANDEVERE: (Unfazed) Well, we always sit there; we sort of have a standing reservation.

SAM: Well, actually we have a lot of customers who like to sit there and it’s been reserved.

MRS. VANDEVERE: Well, who reserved it?

SAM: I can’t tell you that, Mrs. Vandevere.

MRS. VANDEVER: Why not? I’m going to see who’s sitting there anyway (A beat) Is it Carolan Rosenstein-Fishburn? (Deeply peeved) Oh for heaven’s sake, Sam, it’s not rocket science. Why don’t you have Bob call me when he gets in? You don’t seem to have the authority to handle it by yourself. (She hangs up) (Pg 39-40) (Sam is stunned. Sits for a second in a mild state of shock, disliking the job intensely. – The phones are eerily quiet, so Sam makes a phone call)

CURTIS: Diana Drake Agency.

SAM: Curtis, have you guys been getting bad feedback about me?

CURTIS: Sam . . . I know this business with HBO was disappointing, but we’ve been over this. They decided to go in a different direction with the role. That’s all.

SAM: Well, did they say why?

CURTIS: Sam, you’re very talented, everyone knows you’re talented .

SAM: But?

CURTIS: But you do tend to convey a certain lack of . . . entitlement. A sense of deserving, a sense of worthiness, a sense of status, if you will?

SAM: Have people actually said that, or is this from you?

CURTIS: (Getting snippy) Sam, you asked for feedback and I gave it to you. (The phone rings)

SAM: Okay, thanks (New line) Good afternoon, reservations; could you hold please?

R-F: This is Carolann Rosenstein-Fishburn calling for the third time today.

SAM: Okay Mrs. Fishburn, he can’t come to the phone right now, but I’ll have him (Dial tone; she’s hung up) (Sam buzzes upstairs) Jean-Claude, can you watch the phones for like two minutes? I need to grab some food and I’m about to pee my pants.

JEAN-CLAUDE: Sam, what are you – five years old? I can’t watch the phone for nobody!

(phone rings)

SAM: (Pg 43) Reservations, could you hold please?

R-F: (Livid) No, it’s Carolann Rosenstein-Fishburn. Put Jean-Claude on the phone this instant!! This is an emergency! You tell Jean-Claude that we are entertaining a major cultural dignitary this Friday and if we do not resolve this situation right away, we will transfer all our future business to Le Bernadin!

SAM: Okay, one moment please. (Pg 48) Reservations, could you hold please?

CURTIS: Surprise, surprise. Guess who go a callback at Lincoln Center tomorrow morning at ten-thirty?

SAM: (Ecstatic) Oh my God – Curtis! Do I need to prepare anything?

CURTIS: Just a strong sense of personal entitlement. Toodle-oo (He hangs up) (Phone rings) (Sam picks up, be before anything can be said)

R-F: (Pg 50-52) It is Carolann Rosenstein-Fishburn calling for the tenth tie today. Put Jean-Claude on the phone this instant. I am not hanging up until you put him on the phone.

SAM: Well, he’s still busy, but you are welcome to hold on for as long as you like. (Sam buzzes upstairs) Jean-Claude?

JEAN-CLAUDE: (sucking up) Listen, Sam, you need to do a really big favor for me, okay? We tooka special request for the Veccini table at five. (Dripping with charm) Well, I’m asking all the waiters, do they know the words to the song “Lady is the Tramp” and nobody seem to heard of it before.

SAM: No way.

JEAN-CLAUDE: Oh, Sam, come on, you supposed to be an actor. It’s good experience, you never know, maybe the guy has connections in the movie business.

SAM: No, I’m . . .

JEAN-CLAUDE: Oh forget it! I mean if you were really and actor you wouldn’t be answering phones all day now would you? (He hangs up) (Stung Sam picks up a line, not sure who’s there)

SAM: Thank you for holding, how can I help you?

R-F: It is Carolann Rosen . . .

SAM: Oh, right. (Suddenly taking charge) You know what, Carolann . . . Jean-Claude has left for the day.

R-F: (You have got to be kidding.

SAM: (Losing patience) No I’m not. Why don’t you just put your name on our waiting list for Friday and call it a day.

R-F: (through clenched teeth) All right, you little snot, put me in the first slot on the VIP priority Waiting list. Party of six. And why don’t you put it under the name of our guest of honor – Bernard Gersten. Maybe you’ve heard of him. He’s the executive producer of Lincoln Center.

SAM: (a beat) Actually, I have heard of him. (testing the waters) Yeah, it’s so funny that you should mention his name because I’m actually up for a part in a show at Lincoln Center. In fact, I’m going for a callback tomorrow morning.

R-F: Well, Sam, that is funny because I just got off the phone with Bernie and I happen to know that there’s nothing he love smore than the opportunity to help you’re a struggling young actor.

SAM: Really?

R-F: Oh, yes.

SAM: (Enjoying this) You know what Carolann, I can’t believe I overlooked this before. I just happened to notice that a table opened up on Friday night.

R-F: That’s tremendous. And your last name Sam?

SAM: Peliczowski.

R-F: Marvelous. I’ll call Bernie right now. And Sam, we’ll need table thirty-one at eight-thirty.

SAM: Shouldn’t be a problem. (Pg 54) (Phone rings) Reservations, how can I help you?

CURTIS: Sam, Curtis. You’re not going to believe this. Diana just came back from a meeting at Lincoln Center and she was talking you up, so much so, that Bernard Gersten himself wants you to sop in and say hi after your audition. (a beat) (Phone rings) See, Sam, we’re always working for you, even when you think we’re not.

(Sam hangs up)

SAM: (with a new found confidence) Reservations! (mugs for the audience) (Lights out)
```

---

## IC-1143: Funeral Parlor

- Title: Funeral Parlor
- Author (byline): Christopher Durang
- Work: Naomi in the Living Room and Other Short Plays, Pgs 39-52
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Oct 1988
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: MARCUS, SUSAN, BOTH
- Teaser before the introduction: Yes
- Spoken words (computed): 1120
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
Funerals are supposed to be quiet, respectful, and brief. Say you’re sorry, nod solemnly, and leave. Susan is trying to do exactly that -- grieve her husband with dignity and minimal conversation. Unfortunately, Marcus has other plans.

Funeral Parlor by Christopher Durang
```

### Performance text (classify this)

```text
A funeral parlor. Quiet setting. Hushed atmosphere. Susan, the mourning widow, is sedate, proper and formal. A few people are in line, offering their condolences, shaking her hand. She acknowledges them with a little nod and little smile, and a whispered “Thank you.” As the scene begins, at the end of the line to see Susan is a man named Marcus. Marcus reaches Susan. He is sincere and genuine, it’s just that he’s, well, odd.

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

## IC-1144: Garbage Scan

- Title: Garbage Scan
- Author (byline): Dave Barry
- Work: Dave Barry Talks Back, Pg 158-162
- Publisher: Three Rivers Press
- Publication date as stated: May 1992
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: SPEAKER
- Teaser before the introduction: Yes
- Spoken words (computed): 574
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Barry
Book: Dave Barry Talks Back, Pg 158-162
ISBN: 978-0517588680
Publisher: Three Rivers Press
Date (Month/Year): May 1992
```

### Introduction (context only: never use it for content warnings)

```text
Channel-surfing enables the listener to escape the incessant pressures of political advertising, commercials, talk radio, news reports, radio evangelists and of course, the dreaded CLASSICAL MUSIC channels.

Let’s face it . . . we don’t want to hear any of those things on the way to work. We want REAL music . . . the kind that makes you long for a convertible and a hundred miles of open road.

Unfortunately, for those of us without I-Tunes, Sirius XM or, for you more mature audience members, CDs (ARGGGHHHH) . . . we are left with only one option in our quest for Rock and Roll. . . the Garbage Scan by Dave Barry.
```

### Performance text (classify this)

```text
SPEAKER: (Pg 158-162) Monday morning. Bad traffic. Let's just turn on the radio here, see if we can get some good tunes, crank it up. Maybe they'll play some early Stones. Yeah. Maybe they . . .

-POWER ON- ". . . just reached the end of 14 classic hits in a row, and we'll be right back after we . . ."

-SCAN- ". . . send Bill Doberman to Congress. Because Bill Doberman agrees with us. Bill Doberman. It's a name we can trust. Bill Doberman. It's a name we can remember. Let's write it down. Bill . . ."

-SCAN- ". . . just heard 19 uninterrupted classic hits, and now for this. . ."

-SCAN- ". . . terrible traffic backup caused by the. . ."

-SCAN- . . . EVIL that cometh down and DWELLETH amongst them, and it DID CAUSETH their eyeballs to ooze a new substance, and it WAS a greenish color, but they DID not fear, for they kneweth that the. . ."

-SCAN- "(spoken as rapidly as possible) . . . followingisbasedonan500yearleaseanddoesnot-includetaxtagsinsuranceoranactualcarwegetyourhouseandyourchildrenandyour-kidneys. . ."

-SCAN- "NINE THOUSAND DOLLARS!!! BUD LOOTER CHEVROLET OPEL ISUZU FORD RENAULT JEEP CHRYSLER TOYOTA STUDEBAKER TUCKER HONDA WANTS TO GIVE YOU, FOR NO GOOD REASON. . ."

-SCAN- ". . . Bill Doberman. He'll work for you. He'll fight for you. If people are rude to you, Bill Doberman will kill them. Bill Doberman . , ."

-SCAN- ". . . enjoyed those 54 classic hits in a row, and now let's pause while, . ."

-SCAN- ". . . insects DID swarm upon them and DID eateth their children, but they WERE NOT afraid, for they trustedeth in the. . ."

-SCAN-
". . . listening audience. Hello?"
"Hello?"
"Go ahead."
”Steve?"
"This is Steve, Go ahead."
"Am I on?"
"Yes. Go ahead."
"Is this Steve?"

-SCAN- "This is Bill Doberman, and I say convicted rapists have no business serving on the Supreme Court. That's why, as your congressman, I'll make sure that. . . "

-SCAN- ". . . a large quantity of nuclear waste has been spilled on the interstate, and police are trying to. . ."

-SCAN- ". . . GIVE YOU SEVENTEEN THOUSAND DOLLARS IN TRADE FOR ANYTHING!!! IT DOESN'T EVEN HAVE TO BE A CAR!!! BRING US A ROAD KILL!!! WE DON'T CARE!!! BRING US A CANTALOUPE-SIZED GOB OF EAR WAX!!! BRING US. . .”

-SCAN- ". . . huge creatures that WERE like winged snakes EXCEPT they had great big suckers, which DID cometh and pulleth their limbs FROM their sockets liketh this, 'Pop,' but they WERE not afraid, nay they WERE joyous, for they had. . ."

-SCAN- ". . . just heard 317 uninterrupted classic hits, and now.. ."

-SCAN- "Bill Doberman will shrink your swollen membranes. Bill Doberman has. . ."

-SCAN- ". . . glowing bodies strewn all over the road, and motorists are going to need.”

-SCAN- ". . . FORTY THOUSAND DOLLARS!!! WE'LL JUST GIVE IT TO YOU!!! FOR NO REASON!!! WE HAVE A BRAIN DISORDER!!! LATE AT NIGHT, SOMETIMES WE SEE THESE GIANT GRUBS WITH FACES LIKE KITTY CARLISLE, AND WE HEAR THESE VOICES SAYING. . ."

-SCAN-
"Steve?"
"Yes."
"Steve?"
"Yes."
"Steve?"

-SCAN- "Yes, and their eyeballs DID explode like party favors, but they WERE NOT sorrowful,

for they kneweth . . ."

-SCAN- Bill Doberman. Him good. Him heap strong. Him your father. Him. . ."

-SCAN- ". . . finished playing 3,814 consecutive classic hits with no commercial interruptions dating back to 1978, and now. . ."

-SCAN- ". . . the radiation cloud is spreading rapidly, and we have unconfirmed reports that. . ."

-SCAN- ". . . liquefied brain parts did dribbleth OUT from their nostrils, but they WERE not alarmed, for they were.. ."

-SCAN- ". . . getting sleepy. Very sleepy. When you hear the words 'Bill Doberman,' you will . . ."

-POWER OFF-

SPEAKER: OK, never mind. I'll just drive. Listen to people honk. Maybe hum a little bit. Maybe even, if nobody's looking, do a little singing. (Quietly) I can't get nooooooo Sa-tis-FAC-shun . . .*
```

---

## IC-1145: George Carlin’s Guide to Dining Out

- Title: George Carlin’s Guide to Dining Out
- Author (byline): George Carlin
- Work: Brain Droppings, Pgs 8-13
- Publisher: Hyperion Press
- Publication date as stated: May 1997
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, GUY, CUSTOMER, WORKER, WAITER
- Teaser before the introduction: Yes
- Spoken words (computed): 1282
- Already set (do not supply): none

### Source block (context only)

```text
Author: George Carlin
Book: Brain Droppings, Pgs 8-13
ISBN: 978-0786863136
Publisher: Hyperion Press
Date (Month/Year): May 1997
```

### Introduction (context only: never use it for content warnings)

```text
Let’s face it. The American public is in LOVE with eating out. Some studies have shown the average American eats out 4 to 5 times a week. How many other “pleasurable” activities does the average adult engage in 4 to 5 times a week?

Food is IMPORTANT but enjoying yourself during the dining experience is also important. In the true nature of fun, I offer you George Carlin’s Guide to Dining Out (may he rest in peace)
```

### Performance text (classify this)

```text
NARRATOR: Are you a fan of restaurant chains? I’m not. Every now and then I get a Waffle House attack, and I have to get something scattered and smothered, but I don’t make a habit of it. After all, Applebee’s slogan of Eatin’ Good in the Neighborhood takes on a whole new meaning when you think about the fact that they have 2,000 locations. Then of course there is Olive Garden whose food is about as Italian as Taco Bell is Mexican. And last but not least, there is my beloved IHOP, where you can be convinced that pancakes with dripping strawberry syrup and whipped cream is a healthy dinner any day of the week!

(Excerpted from Restaurant Menus Recreated to be Honest by Diana Adams https://bitrebels.com/entertainment/restaurant-menus-recreated-to-be-honest-humor/ )

NARRATOR: (Pg 8-13) There are certain clues that tell you how much a restaurant will cost. If the word cuisine appears in the advertising, it will be expensive. If they use the word food, it will be moderately priced. However, if the sign says eats, even though you'll save some money on food, your medical bills may be quite high.

I don't like trendy food. When I hear, "sauteed boneless panda groin," I know I'm in the wrong place. There's such a thing as pretentious food. Puree of woodchuck, marinated bat nipples, weasel chops, porcupine cacciatore. Or fried eagle. A guy said to me recently,

GUY: C'mon, we'll go to Baxter's, they have really great fried eagle."

NARRATOR: I'm thinkin' to myself, "Do I really wanna know this guy?" However, if you are
going to dine with pretentious people, here are some items you can order that are sure to
impress (each said with a different affectation):
• gorilla fondue,
• filet of hyena,
• jackal tartare,
• rack of prairie dog,
• free-range mole en brochette,
• wolf noodle soup,
• loin of chipmunk,
• koala flambe, and
• wombat souvlaki
Then, at the other end of the spectrum, there is the decidedly non-trendy restaurant, where
the special sometimes is simply "meat." Big sign in the window: "Today's special: Meat."

CUSTOMER: I'll have the meat.

WORKER: Would you like sauce with that?

CUSTOMER: What kind of sauce would that be?

WORKER: That would be meat sauce.

NARRATOR: It's similar to a fish sandwich. Have you ever seen these places that feature "fish sandwiches"? I always think, "Well, that's kind of general." I mean, I wouldn't order something called a "meat sandwich," would you?" At least not without a couple of follow-up questions:

CUSTOMER: Does anyone know where this meat came from? . . . Are any of the waitresses missing?

NARRATOR: I think when you eat out you should have a little fun; it's good for digestion. Simple things. After the waiter recites a long list of specials, ask him if they serve cow feet. But act really interested in the specials. When he says,

WAITER: Today we have goat-cheese terrine with arugula juice, sauteed cod with capers and baby vegetables, coastal shrimp cooked in spiced carrot juice, roast free-range chicken with ginger and chickpea fries, and duck breast in truffle juice.

NARRATOR: Act like you're completely involved. Say,

CUSTOMER: The cod. What is the cod sauteed in?

WAITER: A blend of canola and tomato oils.

CUSTOMER: (No hurry here.) Ahhh, yes! (pointing thoughtfully at the waiter) I'll have the grilled cheese sandwich.

NARRATOR: Even some low-end places are pretentious. The menu can't merely say "cheeseburger." They have to get wordy. So, go along with them. When you order your food use their language. But you must look right at the waiter; no fair reading from the menu. Look him in the eye and say . . .

CUSTOMER: I'll have the succulent, fresh-ground, government-inspected, choice, all-beef, six-ounce patty on your own award-winning sesame-seed bun, topped with a generous slice of Wisconsin's finest Grade-A cheddar cheese made from only premium milk and poured from large, galvanized steel cans, having originally been extracted from a big, fat, smelly, champion blue-ribbon cow with a brain disease.

NARRATOR: Continue that style with other items: Instead of asking for a glass of water, say you'd like a . . .

CUSTOMER: cylindrical, machine-blown, clear drinking vessel filled with nature's own colorless, odorless, extra-wet, liquid water.

NARRATOR: Have fun. Be difficult. Order unusual things: a chopped corn sandwich. Rye potato chips. Filet of bone with diced peas. Peanut butter and jellyfish. Ask for a glass of skim water. Insist on fried milk. Chocolate orange juice. Order a grilled gorgonzola cheese sandwich on whole-wheat ladyfingers. Then top the whole thing off with a bowl of food coloring and a large glass of saturated fat.

Issue special instructions. Ask for the French toast, medium rare. Get a pizza with no toppings, hold the crust. Tell 'em you want eggs: "Fry the whites and poach the yolks."

Order a basket of poppy seed rolls and tell them to scrape off the seeds and put them in a separate bowl and heat them to 200 degrees. Keep them busy.

Tell your waiter you want to make a substitution: "Instead of my napkin, I'll have the lobster tails." See what he says. Ask him if the garnish is free. If it is, tell him all you're having is a large plate of garnish. If they have a salad bar, ask how many times you can go back. If they say as many times as you like, ask for a lawn bag. Come back the next day with a small truck. Tell them you weren't quite finished eating the night before. You're actually within your legal rights, because, technically, no one is ever finished eating.

Ask him if the chef would mind preparing a dish that's not on the menu. Then describe something simple but unusual. Like half a coconut filled with egg whites. When the waiter comes back and says,

WAITER: Yes, the chef said he will be delighted to make that for you . . .

NARRATOR: Tell him, "Well, never mind, I don't like that anymore.” When the food arrives, change your mind. Say. . .

CUSTOMER: I've changed my mind, waiter. Instead of the roast suckling pig, I believe I'll have a half order of Kellogg's Product 19.

NARRATOR: And always, when the food arrives, send something back. It's considered very sophisticated. But make sure you use colorful language. Tell him . . .

CUSTOMER: Waiter, this veal tastes like the inside front panel of Ferdinand Magellan's shorts. And I'm referring to the first voyage.

NARRATOR: Show him you're a man of new ideas. When he comes with the pepper mill . . . Actually, the pepper mill can be a source of great fun. Keep the waiter going on the pepper mill for a long time. Disturbingly long. Until everyone in the restaurant is really uncomfortable. Then, when your food and silverware are completely covered with a thin layer of ground pepper, say . . .

CUSTOMER: Okay, stop! That's perfect!

NARRATOR: Then, a few minutes later, call the waiter over and tell him . . .

CUSTOMER: This food has way too much pepper on it!

NARRATOR: Now that you have your food, the waiter can begin to ask you if everything is all right.

WAITER: Is everything all right?

CUSTOMER: Yes. Thank you. Good-bye!

NARRATOR: Usually, when they ask if everything is all right, tell them the truth. Say . . .

CUSTOMER: Well, I had a problem with the peas. I received 143 peas. Of them, 36 were overcooked, 27 were undercooked, and 18 were not quite the same color as the others.

NARRATOR: Or tell them more than they really want to know.

CUSTOMER: No, everything is not all right. I'm going through a period of upheaval. I have a rogue polyp in my bowel, my wife ran off with a periodontist, and my son has been arrested for defecating in a mall.

NARRATOR: And always fill out the "How did we do?" card. It's very helpful to the owner.

CUSTOMER: (writing on the comment card) Everything was wonderful, except the waiter had some vomit on his shoes and a tiny snot on the end of his nose. It was small, but it was definitely a snot.
```

---

## IC-1146: The Gin Game

- Title: The Gin Game
- Author (byline): D.L. Coburn
- Work: Not specified
- Publisher: Samuel French
- Publication date as stated: 1977
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: FONSIA, WELLER, TOGETHER
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
When two elderly people are young at heart, relationships develop quickly. A simple game of gin can become a friendship. Unless . . . one of those people has an unnatural need to win. To Fonsia, it’s just a game of gin; but to Weller it is obviously so much more and his reactions dredge up issues for Fonsia as well. The Gin Game by D.L. Coburn.
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

FONSIA: Weller!
***********Scene break ***************
TRANSITION
A few days pass until Weller once again meets Fonsia on the sun porch.

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

FONSIA: You could need help and not know it. All I was trying to do was to help you. Maybe I shouldn’t have said anything. . . NO, if I didn’t say anything, the next thing you know they’d find one of us out here on the floor.

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

## IC-1147: The Glass

- Title: The Glass
- Author (byline): Eric Bogosian
- Work: Pounding Nails in the Floor With My Forehead
- Publisher: Theatre Communications Group
- Publication date as stated: Nov 1994
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1901
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eric Bogosian
Book: Pounding Nails in the Floor With My Forehead
ISBN: 1559360968
Publisher: Theatre Communications Group
Date(Month/Year): Nov 1994
```

### Introduction (context only: never use it for content warnings)

```text
We are living in challenging times. Turbulence, conflict, change, surprise, challenge and possibility characterize today’s world and evoke emotions ranging from excitement, enthusiasm and hope to fear and anxiety. We can look at the world around us with hope and positive thoughts (The Glass is Half Full) or we can see the world through smoke-etched goggles, with negativity and injustice for all (The Glass is Half Empty). How do you see . . . The Glass by Eric Bogosian
```

### Performance text (classify this)

```text
Picks up a glass of water, drinks, puts the glass down and addresses the audience.

You know what they say: ''The glass is half empty or the glass is half full?' That's pretty much my philosophy of life. You're born, you live, you die. And somewhere along the line, glass is going to be empty or glass is gonna be full. Empty, full, empty, full, empty, full, empty, full.

I remember when I was a little baby, glass was definitely on the empty side. I didn't have much going for me when I was born. I was only about this big, very small, only weighed about seven pounds. Naked. Crying. Bald. Life was full of challenges: learn to walk, learn to talk, use a spoon, tie my shoe. One thing after the next thing after the next after the next thing after the next!

I mean I’m just this little baby and they cut me no slack. Then it's: "Get out of the house?' Kindergarten, high school, college. I mean it's the same for everybody, right? Learn to drive, get a job, find a place to live, find a love. It's exhausting. And basically what happens is one day you find yourself in a store buying a TV set and you realize you've arrived, you're all grown up. You're an adult now. Glass is finally half full. Here's your TV, go home and watch it.

And then you have to make it in this world and if you have any luck at all, you have some modicum of success and then you get to do all these adult things. You get to have a credit card: "Here's your credit card?' Get to go on vacation pack-ages, have a barbecue now and then and um . . . what else? A bigger TV with a remote control, give you a little power in your life.

Get to be condescending to people younger than you. Get to enter the Publishers Clearing House contests, subscribe to lots and lots of stuff you don't really need, trying to put some hope in your life. But all you end up with is stacks of glossy magazines all over your house with little perfume inserts in them that you peel apart so you can sniff the sweet smell of success and remain completely frustrated.

And you do this. You do this for about twenty-five or thirty years and then one day you look in the mirror and you realize your hair's getting a little thin and your stomach's not as flat as it used to be. And from that day on all you can think about is how your hair is falling and your stomach's drooping.

And basically it just gets worse and worse and worse until you're incontinent, mindless and drooling, stuck in a wheelchair in some firetrap senior citizens home next to an interstate highway. And your big thrill of the day is when they're serving strained peaches.

You're sitting in your wheelchair, strapped in so you don't fall over, you're listening to the sound of the traffic whizzing by out on the highway. Maybe you're counting the cars: "Two thousand one, two thousand two, two thousand three –“ And the attendant brings lunch, which you don't really like, but you like the strained peaches.

And there's this moment, just as that fragment of peach runs down over your old cracked tongue, and for that one moment, for that two or three seconds, everything is good again. Hope is in the air, the glass is half-full once more. But then you start coughing and gagging 'cause you don't have any teeth, you're not that good at swallowing anymore, and the attendant is shouting in your one good ear, "Come on! Come on! You can do better than that! That's no attitude to take!" And [you] think to yourself, if you're capable of thinking anything at all: "DOES DOCTOR KEVORKIAN WORK IN THIS PLACE? I WANT DOCTOR KEVORKIAN!!!"

But that's all kind of in the future for me. I'm pretty happy, things are good.

It can be a beautiful day like today and I can step out into the day and I can think to myself: “This is good -- But even if it is a perfect day and the birds are singing and the sky is blue and I'm holding my four-year-old's hand and everything is perfect, in a way it isn't, because somewhere, and I am reminded of this constantly on the evening news, somebody is suffering like you would not believe!

I mean right now as I say these words, somewhere in Mrica, there is a vast sea of human beings slowly starving to death! A sea of human skeletons dying. They're standing under the same blue sky, the same sun, they're holding their children's hands too.

What can they be thinking as they look down at their kids' bony heads and rib by ribcages and bulging bellies and big brown eyes full of death flies? What can they possibly be thinking? (African voice) "Oh well, the glass is half-empty or the glass is half-full?" Yeah. Right.

STARVING AFRICANS, STARVING AFRICANS, STARVING AFRICANS, STARVING AFRICANS, STARVING AFRICANS! They spoil everything! I mean, wait a second. I'd love to help them. And I try, I send them money. But, I can't fix them. I don't even really know where they are. Where are they? Does anybody here know where they are? You don't know where they are. I know where they are. They're on my TV set, every night, 6:30 PM, channel 2.

It all gets very confusing and depressing. And when I get confused and depressed, what I do, I get in my car, I go to the supermarket, I grab a cart and push it around.

I don't know, something about the supermarket makes me feel better. The environment is so clean and orderly-air-conditioned. I mean the name says it all: SUPERMARKET. It's like where Superman goes to shop. And that's the way I feel as I push my cart around, my cape flying behind me, grabbing that bottled water from a melted glacier ("Oh, only five dollars a quart! That's reasonable!"), the mesquite charcoal chips, double-A alkaline batteries for the kids' toys. Blue Jamaican coffee beans from some blue Jamaican! "Oh! Strained peaches on sale! Never know when I might need some of those!"

I keep going until I fill up my cart, then I know I'm finished. I push my cart to the check-out counter. I am reaffirmed in my right to exist in this environment, because I have the cash. This stuff costs a lot of money and I've got it. Makes me feel good. And as I pass the cash over to the checkout girl, I want to say to her: "See, I can pay for it! Now, check it out!"

And as I carry my bags of groceries out to my freshly waxed and detailed automobile sitting in the middle of the parking lot, I'm not confused and depressed anymore. It all makes sense now. I'm serene again. . . because, because I feel deep down, I deserve this good life. I work so hard. I work hard at my job, I work hard at my marriage, I work out hard at the gym, I work hard at raising my kids. I MAKE AN EFFORT. I wear sun-block when it's sunny out. I floss my teeth every day. I recycle!

I'm a team player and I play by the rules: Pay the charge cards on time, change my oil every three thousand miles, don't drink when driving. No binging, no drug-taking, no four-in-the-morning-one-more-shot-of-vodka drinking, no speeding, no yelling, no spitting, no cursing, no dancing, no running. Just say "no.” That's my life: "Just say no.”

You're either on the bus or you're off the bus. But you gotta know the rules: Don't black out, don't shoot up. Remember your social security number and don't disappear. Don't go to India for a year, don't hitchhike down Highway 61, don't walk on the wild side, don't leave your job or you may find the bus has left without you.

And in exchange for all this good behavior I get a brand new car with a factory installed mobile phone. And I can drive my car and talk on the phone and it feels good. I feel like I really belong.

I can come to a stop sign and be blabbing on the phone for three bucks a minute and there's a guy picking bottles out of a trash can for a nickel apiece and it's OK. It's OK. 'Cause I'm doing the best I can, and I know he's doing the best he can.

I want to roll down the window of the car and throw that guy a buck and say: "I'm there for you man, I'm there for you. When the revolution comes, I am on your side.”

Because I am on his side. I'm one of the good guys! I give money to every charity, I wear my red ribbon, I lick stamps for the benefit committee. I have the t-shirts and the tote bags and the coffee mugs to prove my commitment. I read the morning paper every day, I watch the evening news every night. Lot of painful stories on that news. And I am there for those people. I am there for their pain. "SHOW ME YOUR PAIN, I AM THERE FOR YOU!"

And because I know that I care, I know that I am concerned, my glass isn't just half-full, it's overflowing! Because I love. Love is in my life. I love my wife and kids, I love every single person in the whole world-every single person in Mrica, in Asia, in South America. I wish they were all here right now so I could hug them.

My glass is overflowing because the glass is the glass of life and it is filled with love. And I am drinking with relish from my glass of life. And that love is going down my throat, into my body and it fills my soul. And I drink and I drink, and after awhile I drink so much my bladder gets kind of full and I have to pee.

And oh, here comes that guy from the trash can with his bottle and he needs some love too! Well I've got plenty of love to spare. Bring that bottle over here, dude. Let's fill that right up. And here comes somebody from Zaire with a little tin can and that guy pees into the Zaire guy's can. And here's somebody from Haiti, and somebody from the slums of Rio! We're all drinking and peeing and drinking and peeing and everybody is giving love to everybody else and that's the way the world goes round.

I'm doing the best I can.

Look, a hundred years from now I will just be some bones in a box and so will you and so will that guy picking out the bottles. So what I did in this puny little life of mine will not have made much difference.

But I will tell you one thing. While I was on this earth, I lived and I loved. . . and I was concerned. And that's what's important.

I am concerned therefore I am.
```

---

## IC-1148: The Good Place (TV Pilot)

- Title: The Good Place (TV Pilot)
- Author (byline): Mike Schur
- Work: Not specified
- Publisher: Universal Television LLC
- Publication date as stated: Dec 16, 2015
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: VOICE OVER, MICHAEL, ELEANOR, VIDEO ACTOR, CHIDI, WALLACE
- Teaser before the introduction: Yes
- Spoken words (computed): 1833
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
The Good Place by Mike Schur
```

### Performance text (classify this)

```text
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

VIDEO ACTOR : SO YOU’RE DEAD . . During your time on Earth, every one of your actions carried with it a positive or negative value, depending on how much good or pad that action put into the universe. Save a child from certain death? Great job! That’s plus 1200 points. Poison a river with deadly chemicals? Uh oh – that’s negative 4610! But it’s not only big things. Every single thing you did created some amount of bad or good – intentionally or accidently – and it counted. Only the people with the very highest scores get to come here . . . to the Good Place! Everyone else goes to the Bad Place to be tortured for eternity.

(Video ends)

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

## IC-1149: Greater Tuna

- Title: Greater Tuna
- Author (byline): Jaston Williams, Joe Sears and Ed Howard
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Dec 1983
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: THURSTON, ARLES, DIDI, CHAD, BERTHA, LEONARD, ELMER, VERA, COACH, ARLES & THURSTON
- Teaser before the introduction: Yes
- Spoken words (computed): 1525
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jaston Williams, Joe Sears and Ed Howard
ISBN: 978-0573619021
Publisher: Samuel French, Inc.
Date (Month/Year): Dec 1983
```

### Introduction (context only: never use it for content warnings)

```text
Welcome to Tuna, the third-smallest town in Texas, “where the Lions Club is too liberal, and Patsy Cline never died.” The play originated nearly 40 years ago as a Texas party skit based on a political cartoon; but frighteningly enough, it still rings true today! So with no further ado . . . Here are our radio hosts, Arles Struvie and Thurston Wheelis!

Greater Tuna by Jaston Williams, Joe Sears and Ed Howard
```

### Performance text (classify this)

```text
THURSTON: (Pg 9-10) (Opening music) Good morning, Tuna, this is Thurston Wheelis.

ARLES: And this is Arles Struvie,

THURSTON: And this is the Wheelis

ARLES: Struvie-

THURSTON: Report.

ARLES: And here we go with the news. Take it away, Thurston.

THURSTON: Well, folks, in the news today, we've got the winner of the Tuna Junior High American Heritage Essay Contest for this year. And this year's winner is Connie Carp. She's the daughter of W.H. and Vera Carp here in Tuna, and the name of her essay was titled "Human Rights, Why Bother?" Second place went to Jimbo Beaumont for "Living with Radiation", and third place went to Levita Posey for her essay titled, "The Other Side of Bigotry." I'll tell you, Aries, with subjects like that, I don't know how they ever picked a winner.

ARLES: I don't either. I tell you, it should make the citizens of Tuna proud to know that we're still producing well-educated students who know what America is all about.

ARLES: (Pg 10-12) Now, on the Art scene, the on-again, off-again auditions for the Tuna Little Theatre production of "My Fair Lady" are on again. Now, they'd been called off due to a lack of budget. But Joe Bob Lipsey, who is the director of the show this year, said that he found a way to go ahead with the production by using sets and costumes from last year's show of "South Pacific." According to Joe Bob, this is gonna be the first production ever of "My Fair Lady" set in Polynesia. So get on your Hawaiian shirts, and your grass skirts, and your coconuts, and get out there to that Coweta Baptist Church at eight-thirty, Thursday night, and audition for "My Fair Lady." Joe Bob says he wants to integrate the cast this year. So if you know of any Negro or Mexican-American actors or actresses, have 'em come on out and try out for the chorus.

THURSTON: Well, folks, it's time for a word from our sponsor, Didi Snavely of Didi's Used Weapons. And here's Didi now to tell us all about it. Didi. (Musical transition)

DIDI: Does the high cost of security have you blue? If so, come by the store and browse through our complete selection of used guns and knives, or find what you need in our mace and tear gas department. Now we understand that many people are hesitant to buy used weapons, but all of Didi's weapons are absolutely guaranteed to kill. Now if you find a weapon here that won't kill, you bring it back and we'll give you something that will. It's on our guarantee: "If Didi's can't kill it, it's immortal." *****

ARLES: (Pg 13) And from our World News Desk: Peace talks fail, attack is imminent. Well, that’s all the news we got for ya, but stay tuned . . .

CHAD: (Pg 20-22) My name is Chad Hartford [Reporter for Intellect Magazine. Let’s get right to our interview] Now, Mrs. Bumiller, you are chairing the Censorship of the Textbooks Committee, am I correct?

BERTHA: Oh, no no no no. The Reverend Spikes heads that committee . . . although I am a member, I head the subcommittee that wants to snatch the books off the shelves of the high school library. Some of those books are absolutely disgusting. Our children have no business reading them, and somebody has got to protect the minds of the children.

CHAD: Now, exactly what are the books that you think should be removed from the shelves?

BERTHA: Well, now there's four of 'em that we're gonna try and have removed nationwide. And then we're gonna go from there. Roots. Now, we don't deny that Roots has been a very popular TV series, but we feel it only shows one side of the slavery issue. Bury My Heart at Wounded Knee. Well, it's the most disgusting title to begin with; it just makes me want to erp. It vilifies a great American, General Custer. And it encourages the reader to believe that the United States Government can't be trusted in makin' any treaties. Huckleberry Finn, by Mark Twain. Now, that book shows a pre-teenage boy avoidin' his chores, runnin' away from home, cohortin' with a Negro convict, and puttin' on women's clothes. [And] Romeo and Juliet. It shows sex among teenagers, and we're certainly not going to encourage it. Besides, it shows a rampant disrespect for parental authority.

CHAD: You are aware that William Shakespeare wrote that play?

BERTHA: Oh, yes, we are. And we're lookin' into the rest of his stuff too. He wrote Barefoot in the Park, didn't he?

CHAD: Thank you Mrs. Bumiller. I think we got one hell of a story here. ******

ARLES: (Pg 27-28) And now folks, sit back and listen to the number one show in Dewey County. On the Line with Leonard. Where your business is everybody’s business. Here’s station manager Leonard Childers. (Musical transition)

LEONARD: Hello everybody. This is Leonard Childers with “This Week in Tuna.” I got a message here from the Reverend Spikes over at the Coweta Baptist Church; he says he's gonna sponsor another record-burning. Bring all your rock-and-roll, and this time be sure and get your Chuck Berry and your Brenda Lee and your Little Richard. He says, leave that Buddy Holly and Elvis at home; they're good Southern boys and they'll be forgiven. Anyway, that'll be this comin' Sunday night at eight o'clock down at the Coweta Baptist Church. So bring your rock-and-roll, come on out and burn it . . . ******

THURSTON: (Pg 41) (Musical intro) Good afternoon, Tuna. This is Thurston Wheelis, and this is the Wheelis-Struvie Midday Report. First off in the news, there's gonna be a meeting of the Smut Snatchers of the New Order this afternoon at the Coweta Baptist Church, startin' about five o'clock. Now, Radio Station OKKK is gonna carry that meetin' live. So you tune in.

Now, the Smut Snatchers' latest project is cleaning up those dictionaries down at Tuna High School. And they say, if you know of a word that you feel has questionable value, or a word that you feel just should not be in the dictionary- now if you don't want your child around the word, bring that word with you to the meeting. Bring it to the meeting. The Reverend Spikes says he'll consider each word on a word-by-word basis.

ARLES: (Pg 44) And from our National News Desk: Nuclear accident imperils millions in seven states-Texas not included. Well, that’s all the news we got for ya, but don’t touch that dial-

THURSTON: Don’t touch that dial . . . Get away from it!

ARLES: Get away from it! ‘Cause Tuna Speaks is next! (Musical transition)

ELMER: (Pg 45) This is Elmer Watkins on Tuna Speaks. As a citizen of Tuna, I feel it’s my obligation to speak up about this Agent Orange Stuff and its effects on servicemen. I just wanna say that in the last year I’ve hired fourteen veterans, Viet Nam veterans, to work for me on my road crew, and out of those fourteen, only four of ‘em have died, but there wasn’t a one of ‘em turned orange. I swear to God, not one of ‘em turned anyways near orange. I think it’s just more of this propaganda by this liberal press and these hippie-oriented groups!

VERA: (Pg 46) Vera Carp, Vice-President of the Smut Snatchers of the new Order . . . We need to send out our book-snatchin' squad to the Tuna High School Library to check those dictionaries. Now, we have a new list of words that have been declared possibly offensive or misunderstandable to pre-college students. Now the words are: hot, hooker, coke, clap, deflower, ball, knocker and nuts. After much prayer and soul-searching with the Lord, the Committee has decided not to include the word “snatch” on this year's list. We know some of you have very strong feelings about “snatch,” but we just can't afford to change our letterhead at this time.

LEONARD: (Pg 53) This is Leonard Childers with the Tuna Bulletin Board. Now, if you have any younguns between the ages of eight and fourteen, you need to know that Thursday is your last day to register your kids for Colonel Sprayberry's Character Camp and Survival Institute. Now this year, they're offering classes in Old Testament appreciation, segregation in the Scriptures, Christian biology, character development, and the proper use of firearms. So register your kids today; it will do them some good.

THURSTON: (Pg 49-50) (Musical transition) This is Thurston Wheelis with a sports flash. This just in. The Tuna High School Jaguars lost their season opener against the Kuhlburg Comanches. It was a hard-fought contest, but in the end, the Cats were on the short end of a 48 to nothin’ score. Coach Raymond Chassie evaluated the loss this way.

COACH: Well, we lost mainly because we couldn’t score. But the fact that they made seven touchdowns was a major factor in the loss also. I don’t know which was a bigger factor, but you take away them two things, and it would have been a tie. So, I’m real proud of our boys anyway.

ARLES: (Pg 58) I give up, Coach, take me out. So we're gonna say good night to ya . . . (Musical transition)

THURSTON: Good night!

ARLES: . . . And we'll see you tomorrow.

THURSTON: See you tomorrow.

ARLES: 'Til then, remember our motto here at Radio OKKK: If you can find someplace you like better than Tuna . . .

ARLES & THURSTON: MOVE!
```

---

## IC-1150: Halloween

- Title: Halloween
- Author (byline): Jerry Seinfeld
- Work: Not specified
- Publisher: Little, Brown and Company
- Publication date as stated: Sept 2002
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: JERRY
- Teaser before the introduction: No
- Spoken words (computed): 873
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jerry Seinfeld
ISBN: 978-0316706254
Publisher: Little, Brown and Company
Date (Month/Year): Sept 2002
```

### Introduction (context only: never use it for content warnings)

```text
I’ll trade you ALL my tootsie rolls for 3 of your Snickers! Yup . . . that’s when we first learned to barter! But that’s not all we learned on . . . Halloween by Jerry Seinfeld.
```

### Performance text (classify this)

```text
JERRY: When you’re a kid you can eat amazing amounts of food. All I ate when I was a kid was candy. Just candy, candy, candy. And the only really clear thought I had as a kid was get candy. Get candy, Get Candy, Get Candy, GET CANDY.

Family, friends, school – they were just obstacles in the way of getting more candy.

So the first time you hear the concept of Halloween when you are a kid, you’re brain can’t even process the idea.

You’re like, “What is this? What did you say? Someone’s giving out candy? Who’s giving out candy? EVERYONE WE KNOW IS JUST GIVING OUT CANDY?”

“I gotta be a part of this. Take me with you! I’ll do anything they want . . . I can wear that. I’ll wear anything I have to wear. I’ll do anything I have to do to get the candy from those fools who are so stupidly giving it away.”

The first couple of years I made my own costumes. Ghost, hobo . . . the worst.

I knew my destiny was to one day get a real Superman Halloween costume from the store. You know the one . . . The cardboard box . . . the cellophane top, mask included in the set . . . OH, BABY!

Remember the rubber band on the back of those masks? That was a quality item. Thinnest gray rubber in the world. It was good for about ten seconds before it snapped out of that cheap little staple they put it in there with.

You go to the first house, “Trick or . . .” SNAP! It broke, I don’t believe it! “Wait up! I got to fix it. You guys, wait up!” Kids don’t want other kids to wait, they want them to wait UP. Would you wait up?

Because when you’re little, your whole life is up. You want to grow up. Everything is up!

“Wait UP!”
“Hold UP!”
“Shut UP!”
“Mom, I’ll clean UP . . .
Just let me stay UP!”

When you’re a parent, it’s just the opposite: Everything is down.

“Just calm down!”
“Slow DOWN!”
“Sit DOWN!”
“Come DOWN here!”
“Put that DOWN!”
“And keep it DOWN in there!
“You’re GROUNDED!”

So the day finally came. I finally convinced my parents to buy me an official Superman Halloween-store costume. I was physically ready. I was mentally prepared. And I absolutely believed when I put this costume on that I would look exactly like the Superman I had come to know on television and in the movies.

Unfortunately, these costumes are not exactly the super fit that you are hoping for. You look more like you are wearing Superman’s pajamas. It’s all loose and flowy. The neckline comes down to about your stomach. You got that flimsy little ribbon string in the back holding it all together.

Plus, my mother makes me wear my winter coat over the costume anyway. I don’t recall Superman wearing a jacket. I read every comic book. I do not remember him ever once flying with a coat on. Not like the one I had – cheap corduroy, phone fur.

So you go out anyway and the mask keeps breaking, the rubber band keeps getting shorter because you need to keep re-tying it. It’s getting tighter and tighter on your face. Now you can’t even see!

You’re trying to breathe through that little hole that gets all sweaty. Whoosh, whoosh. The mask starts slicing into your eyeballs. “I can’t see, I can’t breathe. But let’s keep going. We gotta get the candy!”

About half an hour into trick-or-treating you take that mask off. “Oh, the heck with it!”

Bing-Bong. “Yeah, it’s me, give me the candy. I’m Superman, look at the red pant legs.”

Year after year, I never gave up on trick-or-treating. But I remember those last, few Halloweens.

I was getting a little too old for it . . . I was just kinda going through the motions.

Bing-Bong. “Come on lady, let’s go! Halloween, doorbells, candy, let’s pick it up in there.”

They come to the door; they always ask you the same stupid question. “What are you supposed to be?”

“I’m supposed to be done by now. You want to move it along with the 3Musketeers? I got eighteen houses on this block, sweetheart. You hit the bad, we hit the road. That’s the way it works.”

Halloween 3-Step Program:
• Step 1: See kid.
• Step 2: Give candy.
• Step 3: Good night.

Sometimes people give you the little white bag, twisted on the top. You know that’s gonna be some crummy candy. “No official Halloween markings on it? I don’t think so.”

“Wait a second, what is this? The orange marshmallow shaped like a big peanut?

“Do me a favor, you keep that one. We’ve got all the doorstops we need already, thank you very much. We’re going for name candy only this year.”

At the end of Halloween I was able to fill a punch bowl so full of candy that the top of it would be curved. It was like a planet. And I would consume the ENTIRE THING that night.

Next morning, I’d wake up, feel fantastic. And that’s when I realized, when you’re a kid you don’t need a costume, you are Superman.
```

---

## IC-1151: Heaven Help Us!

- Title: Heaven Help Us!
- Author (byline): Cedric the Entertainer
- Work: Grown A$$ Man
- Publisher: Ballantine Books
- Publication date as stated: Oct 2002
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2123
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cedric the Entertainer
Book: Grown A$$ Man
ISBN: 0345447786
Publisher: Ballantine Books
Date(Month/Year): Oct 2002
```

### Introduction (context only: never use it for content warnings)

```text
Church was a big part of my growing up. Back then, it seemed like church was so important. It was about community. It was a time when everybody got together. Sunday was the day for the whole family. You'd go home, have dinner together--cousins and uncles would show up and it'd be a nice day, That's how it was in Caruthersville, Missouri, where I lived until age ten. It was the kind of small town where the lady across the street could whip your butt if she saw you doing something wrong and your mama wasn't home. Those were the good old days. Heaven Help Us by Cedric the Entertainer.
```

### Performance text (classify this)

```text
"Cedric, get off that man's grass! You know that man don't want nobody on his grass!" That was Miss Tessie Mae.

"I hate her," I'd say under my breath.

"I heard you!"

And that lady really did hear you even though she was sitting way up on her porch. She would whip your ass and then make sure you got another whipping when your mama got home from work. Those were the good old days.

You can imagine how important Sunday was in a town like that. My grandmother was one of those real religious people who believed the Lord did everything. She was constantly muttering something about the Lord.

"Ooooh, I woke up this morning, and the Lord put on my house shoes, yes he did. Then I was drivin' down the street and the light turned red, but the Lord told me to keep on going."

"No he didn't, Grandma," I said. "The Lord doesn't tell people to break the law."

I'd hear her speech every Sunday morning for years to come. She didn't care what time you got home from partying on Saturday night. She didn't care that you were sound asleep--one of those good, satisfying, deep sleeps. She'd come in and hit you with the speech.

"You can't tell me you've got time to party on Saturday, but you ain't got time for the Lord on Sunday. Get on up and go on in there." And you'd know it was useless to argue.

Then you'd find yourself sitting up at church with your nightclub clothes on, trying to stay awake. And you aren't the only one. Everybody's nodding--except your grandma and mother. They see your head start jerking like a fishing lure, your eyelids dropping, and you know what happens next? You get that pinch.

"Ouch!" Then you look the other way.

"Man, you got a peppermint, a Certs, a lemon drop, or something? I'm trying to tell you, I ain't gonna make it."

But that was back in the day, before Altoids. Because two or more Altoids will freeze your whole head.

Back then, when you're ten, you're still trying to resist. You start thinking about your daddy. He never goes to church. You see him sitting at home, watching television, drinking a beer, scratching himself, having the kind of good old time you wish you could have.

In fact, he'd never look as happy as he did while waving good-bye and talking about praying for him.

"Y'all pray for me now," he'd say. "Go on ahead."

So you'd turn to your grandma. "What about Daddy?"

"What about him?"

"He don't never go to church?"

"Your daddy knows better. But he's decided he'd rather be going to hell."

And you know she's right. You know your daddy's in trouble. You picture yourself arriving at the pearly gates and St. Peter's saying to him, "Hey dawg, remember that Sunday you didn't feel like getting dressed?"

That's when I think, "A little church might be good for me. Let me just run down and get a TiVo so I don't miss the game."

My favorite part about going to church was the change I got from my mother. It was just a few coins. I'd hit the bottom of the basket as I pretended to put the money in while making the basket jingle.

I wanted my mom to think I'd put the money in, though secretly I put it in my pocket. Only me and God knew. Then after church, I'd buy gum and suckers. I was fine until bedtime. Then I'd think, "Am I going to hell now?"

The other big thing to do on Sundays was go to the Dairy Queen, and everyone in church started to think about that around the same time. So about fifteen minutes before church was over, people started whispering to each other.

There'd be light bickering in which you could tell people were saying, "You go."

"No, you go."

"Just get up, I'm right behind you."

"That's right, amen . . . I went first last week!"

Then people made their moves. One person would pretend to cough and finally get up. He'd be followed by another. Next thing you know, everyone's at the Dairy Queen. The preacher, though not finished with his sermon, knew what was going on, and as the last person hurried out, he worked it right into his sermon, saying, "God wants you to . . . order me a Dilly bar."

"Amen," someone would say from the choir. "Make that two."

The Dairy Queen was right next door to the city jail, so often times you had relatives at the window, hollering down, "Hey, kinfolk, throw me up a banana split or a Blizzard or something."

"Naw, that's too messy. How about a Dilly bar?" At least you got some visiting time in from the Dairy Queen.

That's how it was back in the day. But there seems to be less of that now. Society as a whole seems to be going in a totally different direction. Today, it doesn't seem like church and Sundays have the same importance. You have so many religious leaders, so many televangelists, who are as big as rappers. They're just as famous as the celebrities. They live inside their fame. These guys got private jets. They have mansions. They have money. They're living the same lifestyle as the celebrities. They're friends with Will Smith and Chris Tucker. They want them coming to their church--not so much to save them, but to be associated with them.

Church has become trendy. Choirs have record deals. Going to church nowadays is like going to a concert. It's semicool to go. It's star-studded, people looking around to see who's coming. If you're a celebrity, you get to park in a special parking lot and go in a special back door. You're a celebrity, you don't have to do the regular thing.

That's church in L.A. As if God cares that you're a celebrity, like there's going to be some special roped-off section in Heaven.

I go to church and folks got their instant box cameras with them. People wanting a picture and an autograph . . . during services.

"Can you sign this?"

"Uh, that's your Bible, dawg!"

"Yeah, sign right in Matthew, chapter 7 between verses 20 and 21."

I guess all of that has me a little tainted. The regular common folks want autographs. Is that necessary on a day when everyone should be normal? How do you get celebrity status in a church?

There's something about church and the church environment that indicates we all should be equal because we're all looking for the same thing--salvation.

No matter what, you still have to go to church. When you haven't been to church in a while, you start feeling guilty. You start having thoughts, like maybe the end is near, and suddenly you start hearing a deep, authoritative voice.

"You might want to get up in there, dawg."

"Is that you God?"

"I ain't saying. Alls I'm sayin' is you might want to get your behind into My house soon."

"What do you mean, soon?"

"I mean right now. Not now, but right now!"

Then you start promising yourself that you're going, but you don't make it.

"I'm gonna get on up 'n go on in," you say. "That's what I'm gonna do."

But you don't go, and the next week you raise the ante.

"I'm a go in and pray some, that's what I'm gonna do. I'm a iron my clothes on Saturday. That way, I can just hop right up and go on in."

It's easy to spot the brothers who haven't been to church for a long time. They're the ones who don't know what to do. They walk in thinking they're in a club and find themselves in the pulpit.

"Hey, player, these seats taken? These two?" pointing to the choir director's and deacon's seats. "Ah, they're somebody's seats? All right, damn!"

But he stays cool. He tries another seat.

"Hey, dawg, that's where the preacher sits. You can't sit there. That's where the preacher go!"

It's frightening when you do finally go to church after not having been in a long time. First, you might be identified as a visitor, which means you might have to stand up and have words. And that's a lot of pressure at a black church.

You don't know that church language, which is painfully obvious if you've got to follow that lady who's out traveling. She knows the whole little speech and everything. She gets up right in front of you, giving honor to God, looking you right in the eye.

"Pastor, members, and friends. I come to you on behalf of the Greenway Missionary Baptist Church, Greenway, Mississippi, where my reverend, the Honorable Thesselonious Archinkaid Junior the Third says . . ."

The brother behind her starts panicking. He's next. He starts talking to himself.

"I'm in trouble. I don't know none of that shit. What am I supposed to say?! I don't know none of what that woman's saying. All I know is hip-hop language."

Then he just thinks, "What the hell!" because when his turn comes, he stands up in the middle of the church and gives it a try.

"Ummm, ummm, first of all, givin' big ups to God, Reverend, you 'bout it, you 'bout it. Everybody, big ups. And the choir. Y'all real tight. Real tight. That's on everything. Big ups to y'all."

He keeps on rolling until the sister in the pew next to him leans over and whispers, "Sit your ass down."

The other pressure you might have to deal with going to church after a long dry spell is a good sermon. A good sermon puts a lot of damn pressure on you, boy. You're sitting in your seat and the preacher is doing his thing, calling people up. When he gets like that, he'll eventually find you. You'll think he's finished, but then the Lord will remind him you're there.

"Well, I feel it's just one more person in here that wants to come to the Lord," and he's looking directly at you.

A good sermon is dangerous. It gets you thinking. It starts that internal debate the preacher spoke about. You're in your seat going through it, thinking about it, telling yourself, "Damn, I should go on up there to the altar. I should go ahead on. Pastor's right. I should get my life together. Start right now. Today. If only I didn't . . . have that last little bit of weed left at the crib . . . I'm a join next week. That's what I'm gonna do."

Once, I went to an all-white Catholic church, and I noticed that they prayed differently than black folks. It's true. White folks be praying about trees, clean oceans, peace. They don't care what it is, as long as they're in church they're happy to pray.

"Oh Father, thank you for the trees. Thank you for the birds that fly, Father, and the rivers that run. And the streets we drive on. Amen."

Now you know, if you was at the Great Amount Give A Lot Missionary Baptist Church--in other words, a black church--the prayer is going to be totally different. Black folk pray for stuff that they need--like their lottery numbers to come through.

Then there's always that brother who comes out and prays the same way every time, and for the same things, and you know it's going to be long. You've been planning your escape. You saw Heaven, and it looked like the open highway straight to home. Suddenly you're like, "Oh no, not him! Damn, the game's on!"

But that brother don't care about no game. He's got a whole list of praying to do.

"Dear Lord, you gave me government cheese. Yes you did, Father. I was able to make me a grilled cheese sandwich that was burnt around the edges just like I like it. And Father, when my cable got turned off, your kindness let me run cable from next door. Jesus, y'alright, you such a friend to me. In Jesus's name, Amen."

White folks are so orderly and solemn when they take communion. They're full of quiet contemplation. It ain't that way in a black church. There's always that brother sitting up all important, having the communion wine like he was at a club. He knocks one back and says, "Yo, usher, let me get two more of them. Y'all got any snacks? What's up playa, you gonna eat your cracker? Don't shush me, I'm just askin' if you was gonna eat your cracker?! I was just askin' . . . damn!"
```

---

## IC-1152: Holy Cow

- Title: Holy Cow
- Author (byline): David Duchovny
- Work: Not specified
- Publisher: Farrar, Straus and Giroux
- Publication date as stated: Feb 2015
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ELSIE, REPORTER, REPORTER 2, JERRY, TURKEY, TOM, WOMAN, PA ANNOUNCEMENT, MAN, ELISE, MATRIARCH OF THE HERD
- Teaser before the introduction: Yes
- Spoken words (computed): 1936
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Duchovny
ISBN: 978-0374172077
Publisher: Farrar, Straus and Giroux
Date (Month/Year): Feb 2015
```

### Introduction (context only: never use it for content warnings)

```text
And so begins the adventure of a lifetime for Elsie, a unassuming cow on a small farm in upstate New York, who believes India is the only place to be. She teams up with Jerry, a Torah-reading pig who plans to use kosher dietary laws to his advantage in Jerusalem and Tom, a anorexic Turkey who needs an escape before November. Together these common animals point a way toward an understanding and acceptance that the world so desperately needs.

Holy Cow by David Duchovny
```

### Performance text (classify this)

```text
ELSIE: (Chpt 1) Hello, allow me to introduce myself. I’m a cow and my name is Elsie. See ? (holds up hooves) All animals can speak to one another: lion to lamb, bird to dog, moose to cat – except, really, who would ever want to have a lengthy conversation with a cat? (laugh that turns into a MOO) But I digress. Digression and digestion. It’s what we do. We stand, we eat, we talk . . . It’s all good. At least it was all good. Till about two years ago. That’s when The Event happened. That’s what I call it -- the Event, or the Revelation, or the Day the Patty Hit the Fan. (Chpt 3) See, the time came and I seized it. The eldest was milking me. He’s got the thumb of one hand on his phone the whole time. I have come to learn this is called “texting,” -- a way for people to tell one another stupid things about their day. Oh look, here’s a picture of my lunch with an oh-so-witty caption. Oh look, here’s a picture of me making a silly face, and another picture of a different face. Selfies, they call ’em. (snort) There’s much about people I do not understand. Anyway, he starts muttering under his breath, grabs the pail of my milk, and stomps out of the barn. And guess what? He forgets to shut the gate. (sneaks out of the gate)

ELSIE: (Chpt 8) I don’t know what made me head toward the house. It was destiny. I crept to an open window. The whole family was there quietly staring at a lighted box; hushed like the light box was their god and this Box God was talking.

REPORTER: (Chpt 9) The small farm is dead, replaced by huge industrial meat farms the size of a small town. Here, at this plant . . . (gestures to roll video)

ELSIE: (in horror) Cows were being kept in this huge building, separated from one another by these metal chutes. A man held a metal rod up to the cow’s head, and she collapsed!

(Moo that turns into the word) Murdered. One after another! (observing with curiosity) (Chpt 17) The passive and drooling humans broke out of their stupor long enough to fight over “channels.” I realized that the Box God is not just one god, but many, and with a magic plastic wand, humans can switch from god to god. The Discovery God mentions the name of this one place: India!

REPORTER 2: (with Indian accent) In India, cows are “sacred,” which means respected and special. In India, cows are considered gods and no one eats them.

ELSIE: (Chpt 18) India . . . India . . . I became fixated on the house and more secrets I might learn. I [waited until] the family was going to be away for a while, and then I would go down to the house and continue my research. I found children’s books where cows were heroic. A cow even jumped over the moon in one! Admittedly, it got unbelievable by the end and totally lost me when the dish ran away with the spoon (I mean, come on), but still, that was one bad cow. I found other books with maps that showed me where this magical land of India was. How lucky those cows were that were born in India and got to spend their lives there. And then I thought: Why not me? WHY CAN’T I GO TO INDIA?

(Chpt 19) (long low moo) I was now a cow on a mission – Operation India. I knew it was on the other side of the world and that I would have to cross an ocean. (Ever seen a cow swim? Exactly.) (Chpt 20) [But] I had no idea how I was going to get on a plane. (chewing cud and thinking, she is interrupted by Jerry, the Pig)

JERRY: (oinking snort) ‘Sup? I’ll tell you what I think is up. I think you’re planning to get outta Dodge, makin’ a break, skedaddling, blowing this Popsicle stand . . .

ELSIE: So what if I am?

JERRY: I wanna go too. You think you’re the only one who knows the lay of the land? They’re gonna eat me just like they’re gonna eat you. And I got mad skills. I can help.

ELSIE: Look, Jerry, even if I could take you, the same thing is going to happen to you in India. Cows are sacred in India, but pigs are just, well, pigs.

JERRY: Not India . . . Israel, baby. They hate us pigs so much they won’t eat us! It’ll be heaven. I’ll walk down the street, and people will get outta my way like I’m Clint Eastwood. Nobody will talk to me, they won’t even look at me, but best of all, I won’t wind up on their plates next to some friggin’ apple sauce!

ELSIE: (contemplating, to audience) I’d be a god and he’d be a devil, and we both would live. Humans are ridiculous, but we were desperate. So I relented. (Chapter 21) Jerry was a pain in the tuchus, but he was pretty helpful with logistics. (Elsie is interrupted by Tom, the Turkey)

TURKEY: Are you Elsie Bovary?

ELSIE: Who wants to know?

TURKEY: (in 007 fashion) Turkey, Tom Turkey.

ELSIE: Turkeys have always struck me as really nervous, but this turkey was also rail-thin and his feathers were flying off in every direction. When was the last time Tom had a meal? (to Tom) I’ve got some slop here the pigs left and some chicken feed the chickens didn’t finish.

TOM: Are you insane? Keep that food away from me! November is just a few months away!

ELSIE: And what happens in November, you fly south and wanna look good in your mankini? Oh wait, you can’t fly . . .

TOM: Do I have to spell it out for you? (agitated turkey clucking) Thanksgiving!!! Millions of people in America will eat a turkey!!! (looks around furtively, then speaks in a whisper) I gotta get to Turkey!! That’s my country, those are my peeps. Do you think for a moment that they are going to eat the thing their country is named after?

ELSIE: You have a point . . . but I’m already traveling with a pig I gotta get to Israel. And you’re a bird that can’t fly. You’re an oxymoron.

TOM: (offended) Calling me a moron! Hurtful, just hurtful. (pause) But what if I added value to the enterprise? (takes a cell phone from under his wing)

ELSIE: (to audience) A cellular phone, exactly the thing I’d been coveting for the journey. (to Tom) Impressive, But it’s of no use to me. I can’t work it with these hooves and neither can Jerry.

TOM: Check it. (begins pecking at the phone)

ELSIE: (to audience) He had the weather, Uber, even Siri was at his whim! (trying to cover her glee) You’re in! (Chpt 26) The plan was to try to reserve airline tickets to India, Israel, and Turkey and then head on out to the airport in disguise. I had memorized the farmer’s credit card numbers—Visa and Amex—so I was pretty sure we could charge the tickets. The rest would be easy.

(Chpt 27) We popped into a clothing store to buy raincoats, glasses and hats as disguises. Then a bookstore, and lifted some books on Judaism for Jerry, a Star of David for him to wear around his neck and a yarmulke for his head. (Chpt 28) No one seemed to know who, or rather what, we were. (Chpt 31) I’m sure we made for an interesting sight—big ol’ me, well over six feet on my hind legs in a beige raincoat and sunglasses, and Jerry dressed in the velvet pants of a schoolboy, holding our pet turkey by the leash. We had had the foresight to register Tom as a comfort turkey. ******Scene – On the plane *****

ELSIE: (Chpt 34) (awkwardly trying to make it down the narrow aisle of the plane; she finally sits) Not much leg room! (to audience) None of the flight attendants gave us any trouble, ’cause everyone acts like an animal on a plane. We didn’t stick out at all. Actually, I think we were the most human-acting folk on this flight. The people were disgusting. You should’ve seen the bathroom. (flight takes off)

WOMAN: (Chpt 35)(complaining about the service) They treat us just like cattle up here, just like cows.

ELSIE: Mooooooooo!

WOMAN: (laughing) That’s right, like damn cows, moooo!

JERRY: (extremely nervous) You’ve heard the expression “When pigs fly”? There’s a reason for that – we’re not supposed to be up here! Anybody got an Ambien? Oh, geez . . .

TOM: (flaps his wings and manages to get to a window, he opens the shade and marvels at the sky) There she is! Soooo beautiful! I’m a bird, mama. (flapping wings gently) I’m [flying]!

PA ANNOUNCEMENT: Buckle up for our final descent [into Turkey]!

JERRY: (squeals as the plane hits turbulence) We’re all gonna die! We’re all gonna die!

ELSIE: (Chpt 36) [When] our wheels touched down [we were the last to leave the plane]. Tom hesitated at the cockpit, looking longingly at the controls like he didn’t want to leave.

TOM: (to the others) During that flight, I realized my home is up there in the sky. I am a man with no country but the wild blue yonder.

ELSIE: And he bounded thorough the open door into the cockpit, strapped on a headset and started flicking buttons.

TOM: Birds fly. That’s what they do!

ELSIE: And the “bird” slammed the cockpit door in our faces! The next we heard from Tom was over the PA system.

TOM: This is your captain speaking, looks like we are one or two on the runway here. So, put up your tray tables and adjust your seats to the upright position. We’ll have you at Israel’s Ben Gurion International Airport in no time! Flight attendants, prepare for takeoff.

ELSIE: There were no flight attendants.

JERRY: (yelling) You’re a madman! I’m gonna punch you in the gizzard, you schlimazel!

ELSIE: (Chpt 41) [After landing] we walked by cafes. People gave us no smiles, got out of our way or muttered under their breath.

JERRY: (confidently) This is a bacon-free zone. It’s heaven. Eat me? They don’t even want to touch me! (grabs a menu from one of the café tables, scans it, then triumphantly) See that, no ham, no bacon, no me! Kosher heaven!

MAN: Swine! Devil!

ELISE: Apparently, pigs were associated with devils in ancient lore. Maybe the cloven hooves? Soon there was a growing crowd advancing toward us.

JERRY: (Chpt 42) RUNNNNNNNNN!

TOM: To the plane! Let’s blow this clambake!

ELSIE: (Chpt 43) Luckily our plane was still on the tarmac and we were able to board without any further incident. Tom took off in seconds.

JERRY: I don’t know if I could’ve made it there anyway. I like to be liked too much.

ELISE: And Jerry was once again a pig without a homeland.

TOM: (Chpt 44) (on the PA system) This is your captain speaking. [Soon] we will arrive at our final, I said final, destination: (dramatic pause) Mumbai, India!

ELSIE: Now it was my turn to look out the window (opens shade) My own promised land! Wheels touched tarmac and we began walking. (looks around in confusion) I started to second guess myself. Everywhere I looked, people seemed worse off than animals, and animals were being treated even worse than in the States. Had I been a fool?

We tried to cross a busy intersection. Cars, buses, and taxis careened by even more crazily than they do in the States. I told Shalom and Tom to jump on my back. (I was back to walking on all fours all the time again—I could be a cow!) I put one hesitant hoof onto the road and the oncoming traffic halted like I had just put the world on pause (looks up in amazement) Not one car honked. They waited for ME! A man in rags put his forehead on my forehead and stroked me, murmured lovingly, and then went on his way. It was true. It was all true. I was a queen! I could go wherever I pleased, and no one tried to touch Tom or Jerry while they were on my back.

JERRY: (Chpt 45) This is it! We hit the jackpot. We are gods!

ELSIE: (Chpt 46) I spotted a herd of Indian cows. My people! (rushes to the herd) Greetings and salutations! I’m Elsie. I’ve come from America.

MATRIARCH OF THE HERD: (haughty, disdainful, cold) Why do you keep company with pigs and birds?

ELSIE: They’re my friends.

MATRIARCH OF THE HERD: Indian cows only have other Indian cows for friends. We are goddesses. We cannot associate with animals such as these. You threaten the whole hierarchy with your behavior.

ELSIE: (modestly and matter of fact) I’m not a goddess, I’m just an animal, we’re all animals, just like pigs, birds, just like humans, for that matter.

MATRIARCH OF THE HERD: If you show the humans we’re animals, they will begin to treat us like animals, and eat us like animals, the way they do in your country. You’re a goddess, act like one or be shunned by us other goddesses.

ELSIE: (taking a firmer stance) I’m not a goddess. (Chpt 47) It is not right to be reviled, nor is it right to be worshipped. We are not gods and goddesses, nor are we devils and beasts. We are all animals: pigs, birds, cows, humans. Perfect animals created in the infinite image and imagination of nature. We are all one! (in amazement at her new understanding) Moooooooo! . . . . Holy Cow!
```

---

## IC-1153: Hooway for Wodney Wat

- Title: Hooway for Wodney Wat
- Author (byline): Helen Lester
- Work: Not specified
- Publisher: Houghton Mifflin Company
- Publication date as stated: May 2002
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, WODNEY, CLASSMATE 1, CLASSMATE 2, CLASSMATE 3, CAMILLA, MISS FUZZLEWORTH, VARIOIUS CLASSMATES, VARIOUS CLASSMATES
- Teaser before the introduction: No
- Spoken words (computed): 704
- Already set (do not supply): none

### Source block (context only)

```text
Author: Helen Lester
ISBN: 978-0618216123
Publisher: Houghton Mifflin Company
Date (Month/Year): May 2002
```

### Introduction (context only: never use it for content warnings)

```text
Do kids have to "fit in" by dressing, acting and thinking like everyone else. Let’s hear a resounding NO! Hooway for Wodney Wat by Helen Lester explores the fear we all have about being different and encourages us to embrace our differences as advantages. Or as Rodney Rat would say “embwace or diffewences”. Hooway for Wodeny Wat by Helen Letser.
```

### Performance text (classify this)

```text
NARRATOR: Poor Wodney.

WODNEY: Wodney Wat.

NARRATOR: His real name was Rodney Rat, but he couldn’t pronounce his r’s. To make matters worse, he was a rodent.

WODNEY: A wodent.

CLASSMATE 1: What’s your name, Wodney?

WODNEY: (whispers) Wodney Wat

CLASSMATE 2: What’s another name for bunny?

WODNEY: (mumbling) Wabbit.

CLASSMATE 3: (winking) And how does a train travel?

WODNEY: (miserabley) A twain twavels on twain twacks.

NARRATOR: All of this teasing day in and day out made Wodney the shyest rodent in his elementary school. His squeak could barely be heard in class.

WODNEY: (squeak)

NARRATOR: He gnawed lunch alone.

WODNEY: (demonstrate a rodent eating lunch)

NARRATOR: And while the other rodents scurried and scooted about at recess, Wodney hid inside his jacket.

WODNEY: (Demonstrate)

NARRATOR: Then one day as the rodents were taking turns doing wheelies, a new rodent – a very large rodent – barged into the classroom and announced:

CAMILLA: My name is Camilla Capybara. I’m bigger than any of you. I’m meaner than any of you and I’m smarter than any of you.

NARRATOR: And then she added

CAMILLA: So there.

NARRATOR: With that she accidentally-on-purpose elbowed an ear, bumped two noses, stepped on three tails, and lay down on a desk. Fur prickled in fear through the classroom. She sure was bigger than any of them. She sure looked meaner than any of them. Was she smarter than any of them?

MISS FUZZLEWORTH: What’s 2 + 2?

CAMILLA: (shouting) FOUR!

NARRATOR: Without even bothering to raise her paw.

CAMILLA: And furthermore, 4+4 is 8, 8+8 is 6 and 243 + 125 is 368.

NARRATOR: Later, when Miss Fuzzleworth asked

MISS FUZZLEWORTH: What’s the capital of . . . .

NARRATOR: Camilla interrupted

CAMILLA: New York, Albany, Population 295,594.

NARRATOR: And during science, in answer to the question

MISS FUZZLEWORTH: What part of a plant is blow the ground?

NARRATOR: Camilla Capybara danced on her desk and sang

CAMILLA: Root! Root! Rooty-toot-toot!

CLASSMATE 1: Yup

NARRATOR: thought all the other rodents

CLASSMATE 2: She’s smarter than we are, too.

NARRATOR: They felt very, very uncomfortable. Every afternoon, just before the final recess, Miss Fuzzleworth drew a name from her hat to see who would be the leader for their favorite game, Simon Says. She scrunched her eyes closed and jiggled the hat.

MISS FUZZLEWORTH: (demonstrate)

NARRATOR: Would it be Hairy Hamster? Minifeet Mouse? Grizzlefriz Guinea Pig? Could it be big, mean, smart Camilla Capybara? Miss Fuzzleworth’s paw reached in and pulled out the name of

MISS FUZZLEWORTH: . . . Wodney Wat!

NARRATOR: The bell rang, there was a wild scurry for the door, and Camilla Capybara was the first on the playground, having trampled the others in her path. To Wodney she looked especially scary. What would she do when she heard him speak? Breathe capybara breath in his face?

WODNEY: (Demonstrate/pantomime)

NARRATOR: Or tie him up in his own tail?

WODNEY: (Demonstrate/pantomime)

NARRATOR: Or even POUNCE on him?

WODNEY: (Demonstrate/pantomime)

NARRATOR: The tiny, trembling leader of the game stood before the eager players, his head well inside his jacket, and squeaked.

WODNEY: Wodney says wap your paws awound your head.”

NARRATOR: He peeked a little peek out of his jacket and saw

CAMILLA: (Demonstrate) WHAP! WHAP! WHAPPITY SLAPPITY WHAP!

NARRATOR: Camilla was whapping her paws around her head so hard she became dizzy, gave herself a headache, and had to sit down. The other rodents couldn’t help giggling.

WODNEY: Wodney says play Wing Awound the Wosey.

NARRATOR: Camilla put out her arms like wings and made an airplane noise

CAMILLA: Nnnnrrrr

NARRATOR: But where was the wosey? WHAT was a wosey?

CAMILLA: (Look frantically for a wosey)

NARRATOR: By now Wodney’s voice was stronger and his head was entirely out of his jacket.

WODNEY: Wake the leaves!

NARRATOR: Nobody moved.

WODNEY: Wodney says wake the leaves.

NARRATOR: While Hairy, Minifeet, and Grizzlefriz and the others busied themselves raking,

NARRATOR: Camilla Capybara grabbed one leaf.

CAMILLA: (yelling) Wake up!

NARRATOR: She snatched another

CAMILLA: (yelling) Come on, you. Up, up, up!

NARRATOR: And another

CAMILLA: Rise and shine

NARRATOR: And another

CAMILLA: BOO!

NARRATOR: By now all the other rodents were squealing with laughter

VARIOIUS CLASSMATES: (Squeal with laughter)

NARRATOR: All but Camilla, who frowned.

CAMILLA: Stupid leaves. They won’t wake up!”

NARRATOR: And why was everyone laughing at her? Such bullies! In a voice so strong he had to hold his own ears, Wodney called

WODNEY: Wodney says go west!

NARRATOR: The rodents collapsed in a happy heap for a rest

CAMILLA: Go west.

NARRATOR: Feeling very smart that she could tell directions by the sun said

CAMILLA: All right. I shall go west.

NARRATOR: And then she added

CAMILLA: So there.

NARRATOR: West she stomped. Forever. She was gone . . . And from that day on the pupils of PS 142 Elementary School for Rodents never teased Wodney again. He was their hero

VARIOUS CLASSMATES: Hooway for Wodney Wat! Whoot! Whoot! Wooty-toot-toot!
```

---

## IC-1154: Horton Hears a Who

- Title: Horton Hears a Who
- Author (byline): Theo Geisel (aka Dr. Seuss)
- Work: Not specified
- Publisher: Random House
- Publication date as stated: Feb 1997
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1420
- Already set (do not supply): none

### Source block (context only)

```text
Author: Theo Geisel (aka Dr. Seuss)
ISBN: 978-0679883883
Publisher: Random House
Date (Month/Year): Feb 1997
```

### Introduction (context only: never use it for content warnings)

```text
Theodore Seuss Geisel was born in Springfield Massachusetts in 1904. His mother would often help him go to sleep by chanting rhymes. This combined with an enchanted walk through Springfield’s Forest Park, inspired this young author to write a creative tale about an elephant who courageously protects and defends a speck of dust that is inhabited by a very small society of “people.” Please enjoy this rendition of “Horton Hears a Who” by Theodore Geisel (aka Dr. Seuss).
```

### Performance text (classify this)

```text
On the fifteenth of May in the jungle of Nool
In the heat of the day, in the cool of the pool
He was splashing… enjoying the jungle’s great joys
When Horton the elephant heard a small noise.

So Horton stopped splashing. He looked toward the sound.
“That’s funny,” thought Horton. “There’s no one around.”
Then he heard it again! Just a very faint yelp. (make a sound)
As if some tiny person were calling for help.
“I’ll help you,” said Horton. “But who are you? Where?”
He looked and he looked. He could see nothing there
But a small speck of dust blowing past through the air.
“I say!” murmured Horton. “I’ve never heard tell
Of a small speck of dust that is able to yell.
So you know what I think?... Why, I think that there must
Be someone on top of that small speck of dust?
“Some poor little person who’s shaking with fear
That he’ll blow in the pool! He has no way to steer!
I’ll just have to save him. Because after all,
A person’s a person, no matter how small.

So gently, and using the greatest of care,
The elephant stretched his great trunk through the air,
And lifted the dust speck and carried it over
And placed it down, safe, on a very soft clover.
“Humpf” humpfed a voice. “Twas a sour Kangaroo.
And the young kangaroo in her pouch said “Humpf!” too
“Why, that speck is as small as the head of a pin.
A person on That? Why there never has been”
“Believe Me,” said Horton, “I tell you sincerely.
My ears are quite keen and I heard you quite clearly.
I know there’s a person down there. And what’s more.
Quite likely there’s two, Event three, Even Four.
“I think you’re a fool laughed the sour Kangaroo
And the young kangaroo in her pouch said, “Me too!”
And the Kangaroo plunged in the cool of the pool.
“What terrible splashing!” the elephant frowned.
“I can’t let my very small persons get drowned.
I’ve got to protect them. I’m bigger than they.”
So he plucked up the clover and hustled away.
Through the high jungle tree tops, the news quickly spread:
“He talks to a dust speck! He’s out of his head!”
“Should I put this speck down? Horton thought with alarm.
“If I do, these small persons may come to great harm.
I can’t put it down, And I won’t! After all
A person’s a person. No matter how small.
Then Horton stopped walking. The speck-voice was talking
The voice was so faint he could just barely hear it.
“Speak up, please,” said Horton. He put his ear near it.
“I know,” called the voice, “I’m too small to be seen
But I’m Mayor of a town that is friendly and clean.
My town is called Who-ville, for I am a who
And we Who’s are all thankful and grateful to you”
And Horton called back to the Mayor of the town,
“You’re safe now. Don’t worry. I won’t let you down.”
But just as he spoke to the Mayor of the speck
Three big jungle monkeys climbed up Horton’s neck.
The Wickersham Brothers came shouting, “What Rot”
This elephants talking to Who’s who are not
There aren’t any Whos, And they don’t have a Mayor
And we’re going to stop all this nonsense! So there!”
They snatched Horton’s clover! They carried it off
To a black- bottomed eagle named Vlad Vlad-i-Koff,
And, before the poor elephant could even speak,
That eagle flew off with the flower in his beak.
While Horton chased aftr, with groans, over stones
That tattered his toenails and battered his bones,
And begged, “Please don’t harm all my little folks, who
Have as much right to live as us bigger folk do!”
But far, far beyond him, that eagle kept flapping
And over his shoulder called back “Quit your yapping.
I’ll fly the night through. I’m a bird. I don’t mind it.
And I’ll hide this, tomorrow, where you’ll never find it!”
And at 6:56 the next morning he did it.
It sure was a terrible place that he hid it.
He let that small clover drop somewhere inside
Of a great patch of clovers a hundred miles wide!
“Find That!” sneered the bird. “But I think you will fail.”
And he left, with a flip, of his black bottomed tail.

“I’ll find it!” cried Horton. “I’ll find it or bust!”
I shall find my friends on my small speck of dust!”
And clover, by clover, by clover with care.
He picked up and searched them, and called, “Are you there?”
And by noon poor old Horton, more dead than alive,
Had picked, searched, and piled up, nine thousand and five.
Then , on through the afternoon, hour after hour.
Till he found them at last! On the three millionth flower!
“My friends!” cried the elephant. “Tell me! Do Tell!
Are you safe? Are you sound? Are you whole? Are you well?
From down the speck came the voice of the Mayor:
“We’ve really had trouble! Much more than our share.
When that black-bottom birdie let go and we dropped,
Our tea pots are broken, our clocks have all stopped.
So, Horton, Please” pleaded the voice of the Mayor
“Will you stick by us Whos while we’re making repairs?
“Of course” Horton answered. “Of course I will stick
I’ll stick by you small folks through thin and through thick!”
“Humpf!”
Humpfed a voice!
“For almost two days you’ve run wild and insisted
On chatting with persons who’ve never existed.
And I’m here to state” snapped the big kangaroo,
“That your silly nonsensical game is all through!”
And the young kangaroo in her pouch said, “Me too!”
“With the Wickersham Brother whose help I’ve engaged
You’re going to be roped! And you’re going to be caged!
And, as for your dust speck… hah! That we shall boil
In a hot steaming kettle of Beezle-nut oil!”

“Boil it?” gasped Horton!” “Oh, that you can’t do!”
It’s all full of persons! They’ll prove it to you!”
And down on the dust speck, the scared little Mayor
Quick called a big meeting in Who-ville Town Square.
And his people cried loudly. They cried out in fear:
“We are here! We are here! We are here! We are here!
The elephant smiled: “That was clear as a bell.
You kangaroos surely heard that very well.”
“I heard no small voice and you didn’t either”
And the young kangaroo in her pouch said, “Me, neither”
Grab him? They shoulted, “and cage the big dope!”
Lasso his stomach with ten miles of rope!
Horton fought back with great vigor and vim
But the Wickersham gang was too many for him.
They beat him! They mauled him! They started to haul
Him into his cage, but he managed to call
To the Mayor, I can hear you just fine
But the kangaroo’s ears aren’t as strong quite as mine.
They don’t hear a thing! Are you sure all your boys
Are doing their best? Are they all making noise?
Through the town rushed the Mayor, From the east to the west.
But everyone seemed to be doing his best,
But it wasn’t enough, all this ruckus and roar!
He had to find someone to help him make more.
He raced through each building! He searched floor to floor
And just as he felt he was getting nowhere,
And almost about to give up in despair,
He suddenly burst through a door and that Mayor
Discovered one very small shirker named Jo-Jo
Was standing, just standing, and bouncing a yo-yo!
Not making a sound! Not a yipp! Not a chirp!
And the Mayor rushed inside and grabbed the young twerp!
And he climbed with the lad up the Eiffelberg Tower
“This” cried the Mayor “Is your town’s darkest hour!”
“We’ve Got to make noises in greater amounts
So, open your mouth lad! For every voice counts!”
Thus he spoke as he climbed. When he got to the top,
The lad cleared his throat and he shouted out “Yopp!”
And that “Yopp”
That one small, extra Yopp, put it over!
Finally, at last! From that speck on that clover
Their voices were heard! They rang out clear and clean.
And the elephant smiled. “Do you see what I mean?”
They’ve proved they are persons, no matter how small.
And their whole world was saved by the smallest of all!”
```

---

## IC-1155: How to Be a Villain

- Title: How to Be a Villain
- Author (byline): Neil Zawacki
- Work: Not specified
- Publisher: Chronicle Books
- Publication date as stated: April 2003
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: STAGE 2, STAGE 3
- Teaser before the introduction: No
- Spoken words (computed): 1120
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Zawacki
ISBN: 978-0811846660
Publisher: Chronicle Books
Date (Month/Year): April 2003
```

### Introduction (context only: never use it for content warnings)

```text
Dracula. Hannibal. Frankenstein, the doctor or the monster, either applies -- Fictional villains are so famous all you need to hear are their names, and you know exactly who they are. Villains are some of the most memorable characters in fiction. But just how do these super villains get launched into infamy? It’s How to Be a Villain, a step-by-step guide by Neil Zawacki, that answers all the most urgent questions from choosing an evil name, to marketing your brand; finding the perfect evil hideout, to developing an evil masterplan. It’s cheaper than attending the annual bad guy conference and way more fun than being good. How to Be a Villain is guaranteed to elicit deep-throated evil laughs across the land! (evil laughter)
```

### Performance text (classify this)

```text
Step 1: Choosing an Evil Name (Pg 14-16)

To get your career launched with flair you’ll want a good evil name for yourself. One that is memorable, pithy and short. Choose carefully because this is what the world will know you as throughout time!

The Normal Name: Believe it or not, you don’t always need a big flash name. Trust in your evil deeds, and, should you become terrible enough, that alone can be enough to inspire fear in all humanity. . . [Updated from Bill Gates and Pat Robertson, you may insert your own real-life villains] Rudy Giuliani, OJ Simpson, Elon Musk.

[Or] The Descriptive Name: What makes you so bad? If you like to crush things, for example you might decide to call yourself The Pulverizer. Evil geniuses with multiple limbs might opt for The Octopus.

[Or perhaps a more] Sinister Name: Lord FireHammer; Duke IronSkull; Doctor WormBlight

Let your creativity blossom! Step 2: Evil Branding (Pg 17)

Make your new designation echo in the minds of the timid for eons with some sophisticated evil branding. You won’t need to consult Madison Avenue; chances are, you can come up with great ideas on your own. [You’ll need a] SLOGAN – Three to five words that sum up your evil ways in an intimidating fashion. Remember, you’re talking directly to your victims, so make your message something they can relate to, such as, “Mercy is Not an Option!” [add additional examples such as “You Can’t Handle the Truth!” “You underestimate the power of the Dark Side!] [And don’t forget a] TRADEMARK GESTURE -- Whether you leave behind a token of your villainy or howl from a mountaintop each fortnight, consistent delivery of a gesture or symbolic act, in other words a trademark, will help reinforce your name and identity, making it that much more likely that your evil ways will survive in perpetuity. [Insert a variety of gestures, body stances, entrances/exits here; be creative] [Next] THE EVIL LAUGH – A Must-Have (Pg 23) There are a number of excellent ways to enhance your evil persona, from (in a heavy accent) feigning a foreign accent to (assume a physical tick) exaggerating a physical defect or tick. However, the most essential skill by far is an evil laugh. The evil laugh is a defining characteristic of any supervillain, and you will find yourself calling on it quite regularly as you exult in your own wickedness. Ha Ha Ha Hehe-he-he-he Muahahahaha Bwah-ha-ha-ha-ha!!! HAHAHAHAHAHAHAHAHAHAHAHAHA Once you have decided upon a laugh, practice it every day. (laugh) Take a deep breath, relax, and feel yourself laugh like a crazed hyena. (laugh) Learn all its different chortles and inflections, exploring the many ways it can inspire fear. (laugh) [And finally] FASHION FOR THE EVIL-DOER (Pg 122) The most agonizing decision of your evil career. What to wear? It may seem wrong, but many people will form ideas about how evil you are based on how you dress and carry yourself. 1. It’s hard to go wrong with classic black. Sinister, foreboding, fashionable yet fearsome, black creates an air of mystery. (trademark gesture) Classic black remains THE fashion statement for villains everywhere. 2. (Pg 125) [But] If you spent your childhood hiding in the backyard reading comic books, you probably won’t be happy with anything less than the supervillain costume with gimmicks. Be it a green jumpsuit with question marks or an outlandish clown suit that shoots confetti, the gimmicky costume will automatically provide a motif from which you can adopt a personal theme. As you design your costume, take your body type into consideration. Colorful leotards may be high on visual impact, but remember, spandex is a privilege, not a right! 3. (Pg 131) Evil masterminds who posses a magical inclination may want to invest their money in wizard’s robes. These sleek garments are ideal for sorcerers providing fashion sensibility and open-air comfort. And they look great with sandals or basic black supervillain boot-socks. You can find them in a wide range of colors, including black and red – avoid white [though] both because of the association with good and because you will look like you’re wearing a toga.

Step 3: [Don’t forget a] Location for Your Lair (Pg 88) Every evil mastermind needs a base of operations. Choose your lair carefully. If you have enemies, they will probably show up on your doorstep eventually, so you’ll want it to be an impressive edifice to your grandeur. Consider . . . 1. (Pg 90) An Underground Secret Headquarters of Doom. (trademark gesture) To the untrained eye the secret entrance looks like nothing more than an isolated shack in the middle of nowhere. But should you take the secret elevator hidden within, all is horribly revealed. An underground headquarters is a diabolical lair of which you can be proud. Popular for their low energy bills, privacy and “only a madman could live here” ambience, (laugh) a subterranean lair is an excellent choice indeed. 2. (Pg 92) The Fake Mountain with a hollow interior is another appealing site. On the outside it looks like any other mountain, but with the flip of a switch you can transform it into a deadly fortress of doom! (laugh) The only caveat with the fake mountain is that you should not place it in the middle of a city. For some reason, they are too often noticed there. 3. (Pg 93) Although considered gimmicky for years, the amusement park lair has seen a resurgence in popularity in recent times. The reason is simple: The décor can easily be transformed into a carnival of horrors, the fun houses laced with booby traps and the hall of mirrors at the end for confronting the heroes. The tunnel of love offers endless possibilities for becoming the tunnel of screams (scream turning into laughter) Fun for the whole family!

Step 4: [And Last but Not Least . . . You must have an Evil Plan] (Pg 140) Have you ever wanted to make a great evil plan, but didn’t have the time? You’re not alone. In fact, many evil men and women struggle with this culminating act. The secret to success is planning ahead. The Evil Plan Generator will help you! By identifying your goals, means and target for destruction, the EPG lets you concoct a truly nefarious scheme in a matter of minutes. Simply fill in the blanks! (See fill-in-the-blank options at the end of the selection) (Pg 156) STAGE 1: To begin, you must first (ACTION) (TARGET). This will cause the world to (REACTION), (DESCRIPTIVE VERB) by your arrival. Who is this (NAME)? Where did they come from? And why do they look so good in (FASHION)?

STAGE 2: Next, you must (ACTION) (MONUMENT). This will all be done from your (BASE), a mysterious place of unrivaled dark glory. Upon seeing this, the world will (REACTION), as countless hordes of (HENCHMEN) hasten to do your every bidding.

STAGE 3: Finally, you must (ACTION) your (WEAPON), bringing about (DESTINY). Your name shall become synonymous with (RANDOM), and no man will ever again dare (TRAGIC PAST). Everyone will bow before your (POWER), and the world will have no choice but to (END RESULT).
```

---

## IC-1156: How to Survive a Horror Movie

- Title: How to Survive a Horror Movie
- Author (byline): Seth Grahame-Smith
- Work: Not specified
- Publisher: Quirk Productions
- Publication date as stated: May 2007
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, C, R, A, V, E, AS A PARENT, AS A SKEPTICAL TEENAGER, AS A JOCK, AS A YOUNG GIRL, AS PATHCES, AS A CLULESS TEEN, AS A CLUELESS BABYSITTER, AS A DISGRUNTLED TEEN
- Teaser before the introduction: No
- Spoken words (computed): 1356
- Already set (do not supply): none

### Source block (context only)

```text
Author: Seth Grahame-Smith
ISBN: 978-1594741791
Publisher: Quirk Productions
Date (Month/Year): May 2007
```

### Introduction (context only: never use it for content warnings)

```text
Let’s face it, characters in horror films are pretty stupid. They make bad choices - leaving you to wonder if they have any brains at all. For example . . . They never turn on the lights . . . roaming around in the dark with a serial killer on the loose is a MUCH better option, right? They always go into the basement or wander alone in the woods. They taunt and encourage the killer to come after them in amazing displays of false bravado: “You want some of this – Come and get me, you freak!” They hear a sound and HAVE to go investigate. They utter the phrase: “Let’s split up!” Of all the dumb things people in horror movies do – this is the dumbest! But . . . If you do find yourself trapped in a horror movie, worry not; today I’ll be presenting you with a comprehensive guide to keep you alive until the credits start rolling.

How to Survive a Horror Movie by Seth Grahame-Smith
```

### Performance text (classify this)

```text
(From Chapter 1)

NARRATOR: Those of us who’ve become trapped in a horror movie have a choice: We can either line up with the other cattle and march into the slaughterhouse (Moo!) Or we can fight back. Yes, it’s a long way to the final credits. No, the odds aren’t in our favor. But that’s no excuse to lie down and let the filmmakers have their way with us. (But you have to be smart!)

Horror movie characters aren’t killed by machete-wielding monsters or reincarnated psychopaths— They’re killed by ignorance. Ignorance of the mortal danger they’re in. Ignorance of the fact that they’re in a horror movie.

(So . . . ) How do you know if you’ve been sucked into the Terrorverse? Sometimes the signs are unmistakable. For instance, if you’re a teenaged babysitter caring for a mute toddler in a remote cabin during a blizzard while an escaped killer roams the woods, you’re probably in a horror movie.

TAKE A LOOK AROUND. The environment should offer some clues. If you’re on a crowded city street in broad daylight, you’re probably safe (for now). But if you’re anywhere remote—the woods, an old house, an abandoned mental institution in the middle of a blackout—then yes, your chances of being in a horror movie are much higher.

Do you hear strange sounds? (chi-chi-chi … ah-ah-ah) out of nowhere? Are you speaking Japanese? (utter phrases or words in Japanese – Typhoon, Karaoke, Anime, Emoji, Pokemon!) According to the laws of early twenty-first century cinema, anyone speaking Japanese is in a horror movie. If the answer to any of these questions is “Affirmative,” then we have to consider the possibility that you’ve become trapped in a horror movie.

As much as you may feel like crying or making skid marks in your tighty-whiteys, you’d better pull yourself together—and soon. Because if you don’t, the boogeyman’s really going to give you something to cry about. Your situation requires immediate action, and the C.R.A.V.E. method (COVER, RECON, ARSENAL, VEHICLE, ESCAPE) was developed for just such an emergency. It’s a kind of “stop, drop, and roll” for horror movie victims—a way to stay alive long enough to summon your courage and get out of immediate danger

C: COVER. What you need right now is a temporary headquarters—a place to wipe the sweat from your brow, take a pull off the old asthma inhaler, and formulate your plan. Some of the best places to do that: Good ol’ everyday houses. Though not ideal fortresses, the average two-story house is almost always the closest option. [Or] Water towers. If your movie takes place in a small Midwestern town, this might very well be the tallest structure around. If you can get to the top, you’ll have a highly defensible (there’s only that one long ladder to worry about) perch with a 360-degree bird’s-eye view.

R: RECON. Now that you’ve had a moment to catch your breath, it’s time to get an idea of where the enemy is and what he’s up to. If you don’t have the height of a water tower working for you, peek through the highest window in your hideout and take a look. If you see nothing, they’re probably right behind you. (begins to turn with a stricken look) No, wait! Don’t turn around; Nice and cool … that’s it. Now, on the count of three, cover your face with your arms and jump over the rail or through the window. (shows a fear of heights/jumping) Either you jump or you die. Ready? One … two … just kidding, you’re totally screwed . . . .

A: ARSENAL. You see a path to freedom—you’ll need some kind of weapon. If you’re barricaded in a house, look for a baseball bat, kitchen knife, or anything that kids aren’t allowed to play with indoors. If you’re holed up in a church, grab a heavy-duty candlestick. And if you’re up on that water tower, get your hands on the nearest, um … actually, there aren’t too many options with a water tower. You really should’ve thought of that before you climbed up there!

V: VEHICLE. You’ve summoned some courage, grabbed a weapon, and hopefully spotted a nearby unoccupied vehicle—now it’s time to kick a little ass. In a burst of adrenaline-fueled speed. Your goal—your only goal—is to reach the nearest car or truck, get inside, and blow town as fast as inhumanly possible. Don’t bother smashing the window—they left the car unlocked (provide sound effects and pantomimes) Lock the doors, and pull down the driver’s-side sun visor. The keys will simply drop into your lap. When you try to start the engine, it’ll turn over again and again, but don’t worry—it’ll kick in as soon as the attacker reaches the car and pounds on the windows.

E: Escape. This is the easy part. Put the car in “D,” point the compass to “N,” and get the “F” out of there. [We’ve now come to that portion of this guide entitled] THE SEVEN DEADLY HORROR MOVIE SINS 1ST DEADLY SIN: DOUBT. There are two types of horror movie characters: those who believe your story and those who don’t.

AS A PARENT: It was just a dream, honey.

NARRATOR: No it wasn’t. Come on, people. Your son or daughter is having recurring dreams about getting brutally murdered night after night, and you’re brushing it aside as what— indigestion?

AS A SKEPTICAL TEENAGER: Those are just ghost stories our parents told us.

NARRATOR: Yes, and they just happen to be true. If all the moms and dads have spent the last 17 years telling you not to go into the abandoned mannequin factory, here’s an idea: Don’t go into the abandoned mannequin factory.

2ND DEADLY SIN: MACHISMO. [You’ll recognize] The jock who thinks his football skills are enough to defeat the reincarnated serial killer. Remember, [if you are a] male—in horror movies, testosterone might as well be cyanide.

AS A JOCK: You want some of this?

NARRATOR: You know the guy. The one who just can’t take it anymore.

AS A JOCK: What’s your plan, huh? Sit and wait for that … that thing to pick us off one by one? No way, man! Not me.

NARRATOR: He runs out into the open, yelling something like

AS A JOCK: C’mon, show your face!

NARRATOR: And. . . well, you know how that ends. 3RD DEADLY SIN: INDEPENDENCE. (In a Steve Erwin accent) Have you ever seen that documentary about wildebeests? The one where it’s nothing but slow-motion footage of them getting torn apart by lions and crocodiles? Great, isn’t it? Funny how the predators always seem to kill the animals that are on the outer edges of the herd. The ones who are either too slow or too stupid to draw strength from their numbers. This is not a coincidence. 4TH DEADLY SIN: UGLINESS. Nobody said horror movies were fair. 5TH DEADLY SIN: CURIOSITY. - one of the basic horror movie equations: Investigation = mutilation.

AS A YOUNG GIRL: Is that you, Patches?

AS PATHCES: If “Patches” is your nickname for the man hiding in your closet with razorblades on his fingertips, then yes, it is.

AS A CLULESS TEEN: Do you think it’s dead?

NARRATOR: No. Go ahead and poke it with a stick. We want to watch it grab your arm and bite half your face off. 6TH DEADLY SIN: IRRESPONSIBILITY. In a horror movie, if you accept a task and fail to carry it out, either you or someone close to you is going to die.

AS A CLULESS TEEN: Aw, what’s a little nap gonna hurt?

NARRATOR: A lot.

AS A CLUELESS BABYSITTER: Trust me, the kids are sound asleep.

NARRATOR: No, the kids are dead.

AS A DISGRUNTLED TEEN: How come I always get the crappy jobs?

NARRATOR: Because you’re an idiot, and you’re about to prove that fact by failing miserably at the simple task you were assigned. 7TH DEADLY SIN: VEHICULAR SEX. Do it and die.

(From the Epilogue)

NARRATOR: [So . . . ]When is it safe? When we see credits rolling in front of our eyes? Hear applause? When the killer suddenly takes off the mask, shakes our hand, and says, “Nice working with you”? No, it’s never safe. Once you’re in the Terrorverse, you’re in for good—even after the movie that brought you there has wrapped. You succeeded in vanquishing the enemy? Great. Chances are you made it to the final credits, and you’ll lead a long, peaceful life (especially if your movie bombs at the box office). But there will always be the possibility, however slight, that you’ll be called back for sequels. (Ask Jamie Lee Curtis!) Screenwriters will keep dreaming up new villains and killing methods. Directors will get sleeker and bloodier. And the enemy will keep its fangs and machetes razor sharp . . . You’d better keep your skills the same way.
```

---

## IC-1157: How to Write Suspense

- Title: How to Write Suspense
- Author (byline): James Pinkerton
- Work: The Best American Non-Required Reading 2003, Pgs 258-262
- Publisher: Houghton Mifflin Harcourt
- Publication date as stated: Jan 2003
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: PINKERTON, JANET, JOHN, NARRATOR
- Teaser before the introduction: No
- Spoken words (computed): 883
- Already set (do not supply): none

### Source block (context only)

```text
Author: James Pinkerton
Book: The Best American Non-Required Reading 2003, Pgs 258-262
ISBN: 978-0618246953
Publisher: Houghton Mifflin Harcourt
Date (Month/Year): Jan 2003
```

### Introduction (context only: never use it for content warnings)

```text
What editor ever said, “Jeez, this script or chapter is just too funny, can we fix that?” Okay, if you’re writing Handmaid’s Tale or a Hallmark movie, they might say that. But in comedy, when have you ever stopped hunting for additional ways to make a story funny?

You can’t just start forcing awkward jokes on characters or interrupt the plot to insert a string of one-liners, but a funny story needs to stay funny from beginning to end, right? So, here’s an idea

(insert ominous music “DUM, DUM, DUM”) add suspense! Make the story bigger, scarier, add close calls, raise the stakes, get characters screaming and running, throw a dead body in there!

I see you are here today for James Pinkerton’s Master Class: How to Write Suspense. (make a cringy face, then recover) It will be worth every penny! You’ll learn how to inject blood-curdling hooks into every nook and cranny of your writing by someone who believes he/she is an expert! On to the first lesson!

How to Write Suspense by James Pinkerton
```

### Performance text (classify this)

```text
PINKERTON: (Pg 258-262) (in an over-the-top, Master Class fashion) Lesson 1, General Suspense Tips. The opening sentence is essential to a great suspense novel. It lets the reader know what the story's going to be about. (expansively reading) “John crossed over to the living room and lit a cigarette.”

Note how I have successfully introduced a character, a location, AND an action. Now let's crank up the suspense! “John crossed over to the living room and lit a cigarette. (beat) Or did he?”

Doubt sets in. Our reader begins to question everything he or she has come to believe. Who is this John character? Can we really trust him? How can we really trust anybody? Chilling questions. Luckily, you don't have to answer them. Remember, great suspense lies in what you don't tell the reader.

Having placed the seed of doubt, we quickly move onto something else, distracting them.

(Ah ha!) “John then went to work and nothing happened.”

This is a perfectly acceptable follow-up sentence, right? Wrong! This sentence isn't suspenseful at all. Let's try that follow-up sentence again: “John went to work. (with great intonation and facial expression) His day was a roller-coaster ride of intrigue and mystery.”

Did you see what made the "right" sentence suspenseful and what made the "wrong" sentence utterly worthless? (Self-satisfied smirk)

Lesson 2: Writing The First Chapter -- [Listen to] the following opening paragraph and try to locate where the suspense is coming from: (with an obvious speech impediment, leaving out all the “R’s”)

“The gunman adjusted his gay hat as he powled the misty ooftops, knowing his pey would show soon. Sweat stuck to his shit as he contemplated what he must do. The one-eyed man who had killed his fathe would finally pay the pipe.”

(shivers with the thrill) An excellent opening to a great suspense novel! Where are all the R’s? Is it a typographical error? Does the writer simply not like R’s? Or are there mysterious deeds at play, and are the R’s somehow involved? All of these questions spiral through a reader's mind as they find themselves in the taut grip of (beat) suspense. In the next paragraph, we release this grip: (Lightning crash) “The one-eyed man had stolen all the R’s.”

Goosebumps, yes? Why? Because that was great suspense! Lightning is so suspenseful it's not even funny. Use it for everything! Lightning makes the reader notice whatever happened before the lightning. Remember, a suspense novel should start with a very suspenseful opening paragraph then release the suspense in the second. After this, (waving off the thought) you just write the rest of your book. The reader knows what kind of powerhouse suspense writing to expect, and your work is done.

Lesson 3: Writing Suspenseful Dialogue – [Listen to] the following dialogue. Watch for the “end parts” of the sentences. These are the parts where you’re going to fit most of the suspense in! (Pinkerton plays all characters with intense over-acting)

JANET: I never thought you’d be capable of murder, I’ve known you since the first grade. You’ve never harmed a fly.

JOHN: Maybe that’s true. Maybe it’s not true. Maybe I’ve harmed lots of flies. You don’t know me, Janet.

JANET: Or do I? I know you’re not capable of murder, John. Sure, maybe flies. I’ll give you that. But people? That’s stupid.

NARRATOR: Then Janet saw an enormous bloody knife on the table.

JANET: (reacts) Is this knife yours, John?

JOHN: No, I’m pretty sure it’s not mine.

JANET: Are you lying to me, John?

JOHN: No, probably not. (Lightning crashes)

PINKERTON: Egad! Is John a murderer? Possibly! That’s the thing – who knows? Good suspense dialogue should crackle off the page. Keep the reader on their toes by leaving out important details, locations, names, even events integral to the plot. Remember, the more the reader has to guess, the more powerful your writing becomes. (said with authority even though this is obviously wrong)

Lesson 4: Ending Your Suspense Novel -- A good suspense novel must have a surprise ending to leave the reader completely dumbfounded. If you've done your job up to this point, then the reader should have no clue what's happening, who your characters are, or what it is they're so worried about. Time to make them jump out of their seats! “John and Janet had finally solved the murder. It had been some other guy all along. They were sitting down to a delicious lasagna that Janet had baked when suddenly . . .”

ENDING OPTION 1 is GOOD

“. . . . Janet's head exploded! Janet had been injected with a toxin that explodes heads. John stopped eating his lasagna. (beat) Or did he?” (Waits awkwardly for audience applause, then continues)

ENDING OPTION 2 is BETTER “. . . a big bomb dropped on the house, killing both of them, but mostly Janet. The bomb had been launched in Iraq because of a war there, but the guidance system had shorted out, so it went over to Janet's place instead and flew right into her head. John had a mouthful of lasagna at the time and was flabbergasted. Everyone else was flabbergasted, too. "We never saw that coming," they said. (Waits awkwardly for audience applause, then continues in the most animated fashion)

ENDING OPTION 3 is SUSPENSETASTIC!

. . . a murderer walked in the house! "Oh no, a murderer!" John said as he stopped eating his lasagna. The murderer chased John all through the house and murdered him while Janet escaped. She ran outside and flagged down a policeman who was driving by. "There's a murderer in my house!" Janet said. "He's not in your house," said the policeman. "He's ME!" Holy *moly*! The policeman was the murderer! He murdered Janet. (Lightning crashes) (Pinkerton bows repeatedly as if to rounds of applause from a packed audience)

Great suspense writing is not easy. But with a lot of practice, you will, I assure you (beat) NEVER be as good as I am.
```

---

## IC-1158: How We Talk in South Boston

- Title: How We Talk in South Boston
- Author (byline): David Lindsay-Abaire
- Work: Laugh Lines
- Publisher: Vintage Books
- Publication date as stated: April 2007
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NORMAN, MARY, MARTY, BARBARA, MARLON, ASIAN MAN, PING, FRANKIE
- Teaser before the introduction: No
- Spoken words (computed): 1395
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Lindsay-Abaire
Book: Laugh Lines
ISBN: 978-0307277138
Publisher: Vintage Books
Date (Month/Year): April 2007
```

### Introduction (context only: never use it for content warnings)

```text
Hate in America is a dreadful, daily constant. The dragging death of a black man in Jasper, Texas; the crucifixion of a gay man in Laramie, Wyo.; and post-9.11 hate crimes against hundreds of Arab Americans, Muslim Americans and Sikhs are not "isolated incidents." They are eruptions of a nation's intolerance. Bias is a human condition, and American history is rife with prejudice against groups and individuals because of their race, religion, disability, sexual orientation or other differences. The issue is not a comic one; however, sometimes over-the-top comedy can spotlight the issues even more effectively than a serious approach. May I present David Lindsay-Abaire’s How We Talk in South Boston . . . . a comic look at an extremely serious issue where everyone faces some degree of intolerance.

(Lights up on a living room [parlor) in a blue-collar home in South Boston. MARY is making a latch-hook rug when her husband NORMAN enters with a car door. His arm is lodged inside it.)
```

### Performance text (classify this)

```text
NORMAN: Muthah-ra-Gawd, look at dis. My ahm's cot in da kah dewah.

MARY: Doan bring dat hunka gahbitch into my pahlah, Naw man. Take it back outside and diddle inda gudda.

NORMAN: I ain't diddlin'. My ahm's cot.

MARY: Get owda heah. Ya ahm's cot? (Calls downstairs.) Hey, Mahdy, ya fathah's ahm's cot in the kah dewah. Cawl da fiah depahtmend. Tell 'em to get ovah heah befoah he gets dubbaya dee-faddy on my latch-hook rug.

NORMAN: Dat's a nice rug yuh makin'.

MARY: Yuh like it? Thea havin' a time down at the VFW Post in Mahch, a bazah, like an ahts and craffs faih, an I dought I could sell my rugs.

NORMAN: Dat's a great idear, Meery. (MARTY enters).

MARTY: Yuh cawlin' me?

MARY: Yeah, wheah da frig whiryah?

MARTY: I coodin' heah ya. I was downsteahs ina cella.

MARY: Dis frickin' chowdah-head got his ahm cot in da kah dewah.

MARTY: How'd he get his ahm cot in the kah dewah?

NORMAN: I was fixin' da windah 'cause it was hahd to open, so I took da dewah apaht and was fiddlin' aroun' and my ahm got cot.

MARTY: Dat's wicket pissa. Whadda looza.

NORMAN: Get me owda heah. I gotta watch da Sox at fowah.

MARTY: I bet yaw cot in duh lockin' mechanism. I'll go get yaw kah keez. (MARTY exits.)

NORMAN: D'jew buy me some beah, Meery? You know Hahvey and Kevin McCahthy ah comin' ova to watch da game.

MARY: Sully's not comin'?

NORMAN: Nah, Sully went to da dawg track with Fitzy an Beah-zo.

MARY: Okay. I went to Stah Mahket on Sadaday inny-ways. I bought beah and a pahty platta foah yis. I can cook up some budded con on da cob. An' I got some sub rolls so you can make spuckies.

NORMAN: D'jew get any tawnic? Cause Hahvey don't drink no mowah.

MARY: Yeah. I got two big bosses a' Pepsi. The three-leetah kind. And a box of hoodsies foah afta.

NORMAN: Aw, we should still have hoodsies left ova from lass Saint Paddy's Day.

MARY: Dose was hahd and freeza burnt. I trew ' em in cia barrel. I didn't get no jimmies dough. You want me to run upta Brigham's?

(BARBARA, their daughter, enters.)

BARBARA: Ma, Dad, I have some wicket good news.

MARY: Bahbra. Ya fathah's ahm's cot in a kah dewah.

BARBARA: Whadda looza! Wanna heah my good news now? (MARTY enters.)

MARTY: I gut da kah keez. (Holds up car keys.)

BARBARA: Ma, Dad, Mahty, I'm gettin' married!

MARY: Oh my gawd, my dodda's gettin' meerried!

NORMAN: You know I got a bum ticka! I'm havin' a hahd attack heah! Gimme a hug!

(Hugs her, but the car door makes it awkward.)

BARBARA: Ahhh! Ya hit me wit da kah dewah, ya looza!

NORMAN: Sorry.

MARY: Wait a minute, Bahbra, who ah ya marion?

BARBARA: His name is Mahlin.

NORMAN: We don't know no Mahlins.

MARY: Shuwah we do. Mahlin Perkins. Da animal guy.

NORMAN: How come we neva herda dis Mahlin ya marion?

BARBARA: 'Cause I was afraid ya wooden likem.

NORMAN: Why wooden we likem?

BARBARA: He likes da Yankees. (There's a long, uncomfortable pause.)

MARTY: Yalove 'em, Bahb?

BARBARA: Moah than my haht can beah.

MARTY: Den I ken accep' 'em, liddle sista.

BARBARA: Danks, Mahty. Ma?

MARY: I neva liked baseball. I do an kayah.

BARBARA: Dad? (NORMAN spits in her face.) Ya spit in my eye, ya looza!

NORMAN: You know about da curse, Bahb?

BARBARA: Yeah, but ya ain't gotta spit at me.

NORMAN: In nine-teen nine-teen, Babe Root was a Red Sox playah, an den Harry Frazee solt 'em to da Yankees, and da rest is history. Eva since den, my team has been cursed. In eighdy yeahs, we hahven won a Whirl Series. Shuwah, deer ah udda teams wit worse reckids, but nobiddy loses in such haht-breakin' ways. An' above all da teams in da leagues, da Yankees have been ah ahch enemies. Damn dat Harry Frazee. And damn all dose Yankees. Fenway Pahk shoulda been da house dat Root built. And now my ony dodda is gonna tell me she's marion a Yankee fan?

BARBARA: But I love' em.

MARY: Da haht is a mysterious oahgan, Nawman. Dat I know.

NORMAN: SO doan I! I know dat too, Meery!

BARBARA: Please, Daddy. . .

NORMAN: Awww, jeez. Alright. But nobiddy mention dat dis kid's a Yankee fan. Especially to Kevin McCahthy.

BARBARA: Oh dank you, Daddy! (Hugs him, but the car door gets in the way.) Ahhhh, dat dawn kah dewah!

MARTY: I gut da kah keez! (Tries to unlock the car door.)

MARLON: (Offstage.) Knock-knock. Anyone home?

BARBARA: In heah, honey! Dat's MaWin. He was pahkin' da kah. Everyone be nice.

(MARLON enters. He's a black man.)

MARLON: Hello. I'm Marlon. I was parking the car by the bar on the far corner.

BARBARA: Dozen he tock funny?(They just stare at him blankly.) I just tolt 'em you was a Yankee fan.

MARLON: Oh, yeah? Sorry, I hope you don't hold it against me. Least I'm not a Mets fan. I was rooting for you guys in '86. Too bad about that Billy Buckner thing. Gimpy little ground ball down the first-base line. Right between Buckner's feet. World Series riding on that simple grounder. You must've been angry as heck. Kinda funny, though, right?

MARY: Yoah black. Yourah black man.

MARLON: Yes, I know.

NORMAN: This is a black man, Bahbra.

BARBARA: Isn't he goahjis?

NORMAN: A black man who likes da Yankees and tinks Bucknuh is funny. (Spits in MARLON's Face.)

MARLON: Eww. He spit at me.

MARY: Calm ya livva, Nawman.

NORMAN: Mahty, goto da stowah and get me a regulah coffee.

MARY: Anna cahtin a milk. Deah's money in my pockabook.

MARTY: I wanna stay.

NORMAN: We gotta talk to ya sistah.

MARTY: I'm gay. Since youah so mad anyways and spittin' on evrybidy, I might as well tell yuhs.

MARLON: I support you, Marty. Be proud of your feelings.'

NORMAN: Not in dis neighbahood, Take it to da liberals ova da River at Hahvahd. Dale tellya to mahch in da parade ahm in ahm.

BARBARA: Daddy. . .

MARY: He do an mean nuttin' by it. He was mugged by a black guy once.

MARTY: A gay black guy?

MARY: Shut up, Mahtty. Ya fathuh's upset.

NORMAN: You kids doe know about history. Dat's ya problem right deah.

BARBARA: I'm marion MaWin whetha yis like it oah not.

NORMAN: Yaw ancestas came ova cuzza da famines in Iyaland in da 1850s. An you tink dose uppity Brahmin wannid 'em heah in Boston? No. Nobidy wannid a buncha imergrents. So we found a liddle slice a land ona watah and made it ahrown. The Irish were discriminated against foh all dose yeahs, an now deah gonna tell us weah racist foah protectin' duh ony place dat's ahrown.

MARLON: I can't understand a word he's saying.

NORMAN: Yuh stay wit yuh own kind. Dat's how God wants it. (An ASIAN MAN enters.)

ASIAN MAN: I couldn't help overhearing the argument. I guess it's okay to come out now.

MARTY: Mom, Dad, this is Ping, my boyfriend. He's been livin' inda basement wit me for tree months.

PING: It's a pleasure to meet you. Arm's caught in the car door, huh?

NORMAN: Whad is goin' on heah? Did I raise yous kids to be freaks? Friggin League a Nations in dis house! Dis ain't Greenwitch Village, Mahty!

MARY: It's dat tollarinse ting they been tocking about on da TV: Duh kids musta been watchin' da TV:

NORMAN: No tollarinse in dis house. Dis is Southie! We doan tolerate nobidy heah! Nobidy! Day all wanna take us ova. Duh fohced buss in' was da first step. Remembuh when Bob Kraft tried to put the Pats Stadium in my backyahd? I don't tink so! We chased his Yiddish butt owda heah! I shoulda known he was no good, trying to move dat Jacksonville game so it wooden conflict wit Yom Kippa, whadeva dat is!

PING: I've never heard someone be so blatantly prejudiced.

BARBARA: Ain't he funny?

NORMAN: I ain't prejudiced!

BARBARA: See what I mean? Daddy, youah hilairy-us!

NORMAN: Don't laugh at me, Bahb!

MARLON: He's almost as funny as Bill Buckner!

NORMAN: Get outta my house!

MARY: You do look funny, Nawman! Ya face all red, ya ahm cot inda kah dewah!

(They're all laughing at him now. He's so angry he can barely speak.)

MARTY: Hey, Dad, live and let live, okay?

MARY: Ah you okay, Nawman?

PING: I'm a doctor. I can help.

NORMAN: I do an need no help! I'm fine da way I am!

MARLON: Get him to my car. We'll drive him to City Hospital.

NORMAN: I doan need yis help. . . I'm fine widout yis. (He crawls to the exit, the car door dragging.)

MARY: Youah bein' very stubbin.

NORMAN: I doan needa tolerate nobidy . . . (He collapses.) Ahhhh . . .(He dies.)

MARY: Muthah-ra-Gawd, he's dead.

BARBARA: My fathah is dead.

MARY: He wasn't really youah fathah anyways. Kids, I'd like you to meet Frankie Grey Hawk. (FRANKIE enters, an older man in full Native American regalia.)

FRANKIE: How. Me smokum peace pipe.

MARY: Isn't he funny? Dat's duh ferse ting he says each mohnin' befoah he sneaks oudda da house. He's sucha joka.

FRANKIE: I'm actually a linguistics professor at Northeastern.

BARBARA: Youah ah fathuh?

MARTY: Dat explains Bahbra's terrible drinkin' problem.

BARBARA: And Mathy's dream to open a gamblin' casino!

FRANKIE: Kids, those are just racial stereotypes perpetuated by the white man to keep us down.
```

---

## IC-1159: Humpty Dumpty Egg-splodes

- Title: Humpty Dumpty Egg-splodes
- Author (byline): Kevin O’Malley
- Work: Not specified
- Publisher: Scholastic Books
- Publication date as stated: Jan 2001
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: MR. HATCHERY, MRS. BOARDERING, STUDENT, STUDENT 2, MARY, HUMPTY, JACK, KING COLE, PETER, DUKE, TOWNSPERSON, MOTHER GOOSE, STUDENTS
- Teaser before the introduction: Yes
- Spoken words (computed): 967
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kevin O’Malley
ISBN: 978-0439357388
Publisher: Scholastic Books
Date (Month/Year): Jan 2001
```

### Introduction (context only: never use it for content warnings)

```text
Humpty Dumpty has wigged out. Furious about being teased and taunted for his round and bald body and his bad habit of falling off walls, Humpty is wreaking havoc throughout Mother Goose Land. And with Mother Goose out of town, it’s up to Old King Cole to put things right. But as the king points out, he’s a merry old soul, not a smart one. Luckily, he has Jack Be Nimble to help him pick up the pieces.

Humpty Dumpty Egg-splodes by Kevin O’Malley
```

### Performance text (classify this)

```text
MR. HATCHERY: Hi kids, I’m Mr. Hatchery. Your teacher, Mrs. Boardering, asked me to take part in “Read Across America Day.” Today I’m going to read the wonderful book The Nursery Rhymes of Mother Goose: Favorite Rhymes for Young and Old . . . (clears his throat and begins reading in a very flat voice) Mary had a little lamb. Her fleece was white as snow.

MRS. BOARDERING: Mr. Hatchery? I’m going to step down to the teachers’ lounge for a minute.

MR. HATCHERY: (silently acknowledging Mrs. B) And everywhere that Mary went, the lamb was sure to go.

STUDENT: Boring! What does your dad do anyway?

STUDENT 2: Aw . . . jeez, Dad. He works in an office.

MR. HATCHERY: It followed her to school one day, which was against the rules. (closing the book and addressing the class) Does anybody know what happens next? Anybody? No? (and suddenly his demeanor changes) Well, she found a giant egg crushing the school. It wasn’t just any egg, oh no! It was an . . . Egg-Ceedingly large Humpty Dumpty!!

Mr. Hatchery now acts out the story becoming each of the characters . . .

MARY: Humpty Dumpty, what happened to you? You’re huge! (think Godzilla size)

HUMPTY: That’s right. I’m huge and I’m not gonna take it anymore! (mimicking the townsfolk who taunt him) “Oh, look, the tubby bald eggman is falling off the wall, Haa, haa, haa.”

(sarcastically) Did anybody ever think how painful it would be to have a horse try to put you back together? No! So I’m back, baby! Say good-bye to Mother Goose Land!

MR. HATCHERY: Mary ran back to Jack’s house as fast as her dress would let her.

MARY: Jack be nimble, Jack be quick, Jack jump over the candlestick, and get over to Old King Cole’s place fast!

JACK: (jumping over a candlestick) Hey, Mary, can’t you see I’m working here? Do you think this is easy? (knocks the candlestick over and has to reset it and try again – he’s not very nimble)

MARY: Humpty Dumpty’s back and he’s gonna stomp the town. Hurry!

MR. HATCHERY: Old King Cole was a merry old soud until Jack came running in.

KING COLE: What? Humpty Dumpty’s gonna wreck the town? What am I supposed to do? I’m not a smart king, just a merry one. The real brains of the town is Mother Goose and she’s away on vacation getting her feathers fluffed!

JACK: Well, you’d better think of something quick. Humpty Dumpty’s headed this way.

KING COLE: (thinking, which is very hard for him) I’ve got it. Get me Peter Piper. . . (Jacks exits and returns with Peter) Peter Piper, pick me a peck of pickled peppers then throw them at Humpty Dumpty. He hates pickled peppers.

PETER: Yes sir, Sire! (races to rapid-fire as many peppers as he can at HD)

HUMPTY: (catching some in his mouth; others in his hands which he stuffs in his mouth) I’ve learned to love pickled peppers!

PETER: (returns to the King) Your Highness, it didn’t work. Humpty just ate the peppers.

(dejected, Peter exits)

KING COLE: (to Jack) How many pecks of pickled peppers did Peter Piper pick?

JACK: He pitched pickled peppers until he was positively popped. Should I try calling Mother Hubbard?

KING COLE: Naw, what’s she got to throw at Humpty? Her cupboard is always bare. Besides, she’s never at home and you’d end up talking to that smart aleck dog. Let’s call the Grand Old Duke of York.

JACK: Good idea! He’s got ten thousand men. (picking up the phone)

(pantomime a great battle with Humpty, with Humpty roaring and winning and the men losing and screaming)

DUKE: Retreat!!!

JACK: (lowering his spy glass and shaking his head) No good, Sire. He marched them all straight up the hill and he marched them down again.

KING COLE: I should have known.

JACK: I could try the Old Woman that Lives in the Shoe.

KING COLE: Naw, she’s got so many children she won’t know what to do.

JACK: (looking out the window) Sire?! Come quick! Humpty’s crashing through the town!

(Humpty rampages)

MR. HATCHERY: Humpty Dumpty was on a rampage. He found Jack Horner sitting in the corner. He stole his plum, Christmas pie and all. He sat on Little Miss Muffet’s tuffet and ate all her curds and whey. He shook the whole town. Things were looking bad.

HUMPTY: (singing as he destroys the bridge) London Bridge is falling down!

TOWNSPERSON: Falling down, falling down. London Bridge is falling down. My fair lady???

KING COLE: (to Jack) I’ve got it. You know Peter . . . Peter Pumpkin Eater?

JACK: Oh, sure. I heard his wife got out of the pumpkin shell. I believe she’s doing very well.

KING COLE: Yes, yes, yes. Go and tell Peter to roll that pumpkin downtown. I want him to stuff Humpty in it. (pantomime of Peter rolling the pumpkin at Humpty)

HUMPTY: Look . . . It’s a squash! (stomping the pumpkin to bits) Roses are red, violets are blue. Pumpkins are orange, and the town is too!

KING COLE: (to Jack, running out of ideas) I’ve got it! Do you know the Muffin Man?

JACK: (unsure) The Muffin Man?

KING COLE: The Muffin Man! Do you know the Muffin Man?

JACK: Oh sure, he lives on Drurey Lane.

KING COLE: Well, go to him and tell him to lay a path of muffins down Main Street. Tell him to make a left onto Wall Street. We’ll drive Humpty Dumpty right up the wall! (pantomime the Muffin Man laying a trail of muffins)

MR. HATCHERY: (very animated) Wrecking a town is hard work. Humpty was really hungry. He followed the muffin trail just as Old King Cole had hoped. (bending, snapping and popping muffins; he follows the trail right up the wall and sits there eating)

KING COLE: Now we have to find a way to push him off. That’ll knock some sense into him.

JACK: (running back into the throne room) Sire, Sire! Dr. Foster, on his way to Gloucester, reports that Mother Goose is on her way back home.

KING COLE: (with a huge sigh of relief) Thank goodness. Now I can get back to being merry.

MOTHER GOOSE: (flying in the window, she collides with King Cole and they struggle to untangle themselves) The town’s a mess. What’s going on here? I can’t even go away for the weekend without this place going to pieces.

MR. HATCHERY: Old King Cole filled Mother Goose in about Humpty Dumpty’s rampage.

MOTHER GOOSE: (honking, hissing and yelling) Get me all the king’s horses and all the king’s men! Send them all to the wall!

JACK: (saluting) Yes, Ma’am! (he races off)

MR. HATCHERY: Meanwhile, Humpty was almost finished with his muffins. He was extremely full. He was getting very sleepy. (HD begins to drift off and as he does so, he slips off the wall) (in a sing-song voice) Humpty Dumpty sat on the wall. Humpty Dumpty had a great fall. All the king’s horses and all the king’s men . . . (building suspense) held out a giant sheet and caught him!

JACK: (to Mother Goose) What are you going to do with him now?

MOTHER GOOSE: Get me Gregory Griggs.

JACK: Gregory Griggs? Had twenty-seven different wigs? He wore them up, he wore them down to please the people of the town? [that] Gregory Griggs?

MOTHER GOOSE: (impatient) Yes, yes, yes! Tell him to bring all his wigs.

MR. HATCHERY: Mother Goose stitched all the wigs together. (flapping her wings she lowers the giant wig onto HD’s bald head) When Humpty woke up, he had a fine head of hair.

(Humpty wakes up, feels his head, perhaps tosses his new mane of hair and assumes a new persona – think “hip” Elvis Presley)

HUMPTY: (*singing and performing in the style of Elvis Presley; adds in a death drop/half split)

MR. HATCHERY: With his egg-citing new look and attitude, Humpty Dumpty became a big star. He does two shows a day and when he falls . . .

HUMPTY: (*continues the performance; adds in a death drop/half split)

MR. HATCHERY: . . . the crowd goes wild!

STUDENTS: (screaming Humpty’s name as if at a rock concert)

MRS. BOARDERING: (entering from the hallway, she’s shocked at what she sees; the students go silent) Sorry I took so long, Mr. Hatchery. Is everything OK?

MR. HATCHERY: Oh, yes, Mrs. Boardering . . . everything worked out, “Happily ever after!”

STUDENTS: (chanting Humpty’s name)
```

---

## IC-1160: In Depth, But Shallowly

- Title: In Depth, But Shallowly
- Author (byline): Dave Barry
- Work: Bad Habits
- Publisher: Henry Holt & Company, Inc.
- Publication date as stated: Sept 1993
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, ANNOUNCER, WESTBROOK, KERNEL, MAYOR, SNAPE, TOMPKINS, EDWARDS, STEVENS, JOHNSON, HOLP
- Teaser before the introduction: No
- Spoken words (computed): 1117
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Barry
Book: Bad Habits
ISBN: 978-0805029642
Publisher: Henry Holt & Company, Inc.
Date (Month/Year): Sept 1993
```

### Introduction (context only: never use it for content warnings)

```text
Newsflash: The daily news isn't an accurate reflection of what's really going on in the world today. It indicates what's going wrong with our world – how much death and destruction has occurred and how many murders/suicides/bombings/explosions went down. But it doesn't portray neighbors helping neighbors, communities banding together to raise money for cancer research, cops catching criminals, diseases going into remission, babies born healthy, personal achievements celebrated, milestones passed, or victories won! You shouldn't watch the evening news because it rarely shares good news. Hmmmm. Options . . . What about the LOCAL NEWS . . that should be where we see the GOOD stuff, right? WRONG . . . In Depth, but Shallowly by Dave Barry.
```

### Performance text (classify this)

```text
NARRATOR: If you want to take your mind off the troubles of the real world, you should watch local TV news shows. I know of no better way to escape reality except perhaps heavy drinking.

Local TV news programs have given a whole new definition to the word news. To most people, news means information about events that affect a lot of people. On local TV news shows, news means anything that you can take a picture of, especially if a local TV News Personality can stand in front of it. This is why they are so fond of car accidents, burning buildings, and crowds: these are good for standing in front of. On the other hand, local TV news shows tend to avoid stories about things that local TV News Personalities cannot stand in front of, such as budgets and taxes and the economy. If you want to get a local TV news show to do a story on the budget, your best bet is to involve it in a car crash.

I travel around the country a lot, and as far as I can tell, virtually all local TV news shows follow the same format. First you hear some exciting music, the kind you hear in space movies, while the screen shows local TV News Personalities standing in front of various News Events. Then you hear the announcer:

ANNOUNCER: From the On-the-Spot Action Eyewitness News Studios, this is the On-the-Spot Action Eyewitness News, featuring Anchorman Wilson Westbrook, Co-Anchorperson Stella Snape, Minority-Group Member James Edwards, Genial Sports Personality Jim Johnson, Humorous Weatherperson Dr. Reed Stevens, and Norm Perkins on drums. And now, here's Wilson Westbrook.

WESTBROOK: Good evening. Tonight from the On-the-Spot Action Eyewitness news studios we have actual color film of a burning building, actual color film of two cars after they ran into each other, actual color film of the front of a building in which one person shot another person, actual color film of another burning building, and special reports on roller-skating and child abuse. But for the big story tonight, we go to City Hall, where On-the- Spot reporter Reese Kernel is standing live.

KERNEL: I am standing here live in front of City Hall being televised by the On-the-Spot Action Eyewitness News minicam with Mayor Bryce Hallbread.

MAYOR: That's "Hallwood."

KERNEL: What?

MAYOR: My name is "Hallwood." You said "Hallbread."

KERNEL: Look, Hallbread, do you want to be on the news or don't you?

MAYOR: Yes, of course, it's just that my name is ...

KERNEL: Listen, this is the top-rated news show in the three-county area, and if you think I have time to memorize every stupid detail, you'd better think again.

MAYOR: I'm sorry. "Hallbread" is fine, really.

KERNEL: Thank you, Mayor Hallbread. And now back to Wilson Westbrook in the On-the-Spot Action Eyewitness News Studios.

WESTBROOK: Thank you, Reese; keep us posted if anything further develops on that important story. And now, as I promised earlier, we have actual color film of various objects that either burned or crashed, which we will project on the screen behind me while I talk about them. Here is a building on fire. Here is another building on fire. Here is a car crash. This film was shot years ago, but you can safely assume that objects just like these crashed or burned in the three-county area today. And now we go to my Co-Anchorperson, Stella Snape, for a Special Report on her exhaustive three-week investigation into the problem of child abuse in the three-county area. Well, Stella, what did you find?

SNAPE: Wilson, I found that Child abuse is very sad. What happens is that people abuse children. It's just awful. Here you see some actual color film of me standing in front of a house. Most of your child abuse occurs in houses. Note that I am wearing subdued colors.

WESTBROOK: (reading from a script) Are any efforts under way here in the three-county area to combat child abuse?

SNAPE: Yes.

WESTBROOK: Thank you, Stella, for that informative report. On the lighter side, On-the-Spot Action Eyewitness Reporter Terri Tompkins has prepared a three-part series on roller-skating in the three-county area.

TOMPKINS: Roller-skating has become a major craze in California and the three-county area, as you can see by this actual color film of me on roller skates outside the On-the-Spot Action Eyewitness News Studio. This certainly is a fun craze. Tomorrow, in Part Two of this series, we'll see actual color film of me falling down. On Wednesday we'll see me getting up.

WESTBROOK: We'll look forward to those reports. Our next story is from Minority- Group Reporter James Edwards, who, as he has for the last 324 consecutive broadcasts, spent the day in the minority-group sector of the three-county area finding out what minorities think.

EDWARDS: Wilson, I'm standing in front of a crowd of minority-group members, and as you can see, their mood is troubled. (The crowd smiles and waves at the camera.)

WESTBROOK: Good report, James. Well, we certainly had a sunny day here in the three-county area, didn't we, Humorous Weatherperson Dr. Reed Stevens?

STEVENS: Ha ha. We sure did, though I'm certainly troubled by that very troubling report Stella did on child abuse. But we should see continued warm weather through Wednesday. Here are a bunch of charts showing the relative humidity and stuff like that. Ha ha.

WESTBROOK: Ha ha. Well, things weren't nearly as bright on the sports scene, were they, Genial Sports Personality Jim Johnson?

JOHNSON: No, Wilson, they certainly weren't. The Three-County Community College Cutlasses lost their fourth consecutive game today. Here you see actual color footage of me watching the game from the sidelines. The disgust is evident on my face. I intended to have actual color film of me interviewing the coach after the game, but the team bus crashed and everyone was killed.

WESTBROOK: Thank you, Jim. And now, here is Basil Holp, the General Manager of KUSP-TV, to present an Editorial Viewpoint:

HOLP: The management of KUSP-TV firmly believes that something ought to be done about earthquakes. From time to time we read in the papers that an earthquake has hit some wretched little country and knocked houses down and killed people. This should not be allowed to continue. Maybe we should have a tax or something. What the heck, we can afford it. The management of KUSP-TV is rolling in money.

ANNOUNCER: The preceding was the opinion of the management of KUSP-TV. People with opposing points of view are probably in the vast majority.

WESTBROOK: Well, that wraps up tonight's version of the On-the-Spot Action Eyewitness News. Tune in tonight to see essentially the same stories.
```
