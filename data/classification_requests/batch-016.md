# Classification request: batch 16 of 63 (40 records, IC-0601 to IC-0640)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-016-reply.json`.

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

## IC-0601: The Intelligent Design of Jenny Chow

- Title: The Intelligent Design of Jenny Chow
- Author (byline): Rolin Jones
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Aug 2006
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JENNIFER, ADELE
- Teaser before the introduction: Yes
- Spoken words (computed): 1079
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rolin Jones
ISBN: 978-0822220718
Publisher: Dramatists Play Service
Date (Month/Year): Aug 2006
```

### Introduction (context only: never use it for content warnings)

```text
Intro is spoken by the actress playing Adele until the last line, which is voiced together.

International adoption is by its nature an emotional journey, one that traverses the highs of creating a family and the inevitable lows born of jarring change. The road can be rough, both for the parents who often must deal with children with post-traumatic behavioral issues, and for kids who suddenly find themselves immersed in a new family and a strange culture.

This scene shows just such a family in turmoil. Jennifer, Adele’s 18 year old daughter, adopted from China as an infant, is struggling with many issues; and Adele, insecure in her own position as “Mom” is struggling as well.

The Intelligent Design of Jenny Chow by Rolin Jones.
```

### Performance text (classify this)

```text
JENNIFER: Okay, so here we go . . . My name is Jennifer Marcus and one of the first things you’re going to have to get used to is that I’m better than you. Wait I’m not being conceited, not really, you know, there’s a lot of baggage that come with it. I’m pretty much a complete disappointment to both my parents. My mother’s totally fed up with me. You see I have this thing called Obsessive-Compulsive Disorder. And it puts a lot of pressure on everyone in the house. It started in high school with some mild Tourette’s. Just little stuff like, “Alrighyeah” or like “Okaywhatever” and no one noticed, you now. See, what OCD really means is that it takes me a lot of time to what most regular people can do in a minutes. And so the truth is, I have a hard time getting out of the house. What I mean is it’s not just OCD anymore. It’s maybe, like kinda, sorta . . . agoraphobia. Though it’s not like I’m afraid to leave my house, that’s not it. It’s just a lot easier to stay inside where you can manage the germs and the noise and . . . if you’ve got some Ethernet cable, it’s more like a cathedral than a house. The world, the whole world, you know, can pass right through your house. You don’t have to even move. And it’s beautiful, you know.

JENNIFER: (SHE walks to the kitchen where ADELE is sitting, waiting, staring off into space, with a drink in her hand. SHE'S plowed.) Oh.

ADELE: Hi.

JENNIFER: How was your trip?

ADELE: It was what it was.

JENNIFER: How was the acquisition?

ADELE: It happened. How come the garbage is still in the back, Jennifer?

JENNIFER: I forgot.

ADELE: What are we going to do with you, Jennifer?

JENNIFER: Welcome back, Mom. (JENNIFER turns to leave.)

ADELE: No. We're not finished.

JENNIFER: I'm tired.

ADELE: You're tired? No, you're not. You haven't been in fourteen-hour negotiations. Your secretary didn't forget to book you a room. You weren't rerouted three times this week. You didn't have to fire a lifetime employee, someone who's been with the company for twenry-eight years and barely makes enough to support his family. And you sure as hell didn't do it the same day the company picked up a two-thousand-dollar dinner. You're not tired, Jennifer. I'm tired.

JENNIFER: Okay. Then you should probably go to bed.

ADELE: No. I can't go to bed because my house is in disarray.

JENNIFER: What are you talking about?

ADELE: Take out the garbage. Do some dishes. Am I asking too much?

JENNIFER: I've been busy.

ADELE: Online. With your little cyberboyfriend ...

JENNIFER: You're drunk.

ADELE: ... Hello, cyberfriend. Can you find my mommy for me?

JENNIFER: Whatever.

ADELE: You think you're a princess ....

JENNIFER: You're totally plowed.

ADELE: ... A little Chinese princess? Isn't that what you think? Think your father and I stole you away from the queen? We're keeping you from your life as the emperor's daughter, huh?

JENNIFER: Shut up.

ADELE: What happened to you, Jennifer?

JENNIFER: You happened to me.

ADELE: Oh, is that right? I ruined your life? Me, who got on a plane, brought you back here. Put you in this house, put you into every accelerated program, every activiry. Fed your brain.

JENNIFER: I didn't ask for this house and I hated those classes.

ADELE: (Reliving it.) Ms. Hartwick, Mr. Marcus. Your little girl's a genius. What do you do, Jennifer?

JENNIFER: I don't care.

ADELE: You can't even imagine. Of course you can't, you weren't there. You were out on the playground. They give you a handbook.

JENNIFER: Oh, of course, the handbook ...

ADELE: Page one. Never tell them they're a genius.

JENNIFER: Never tell them you're good at anything ....

ADELE: Page two ...

JENNIFER: How to deprive your child of joy and wonder while preparing her for a life of infinite servitude.

ADELE: She abandoned you ...

JENNIFER: Yeah? Then how come her name is on the birth certificate?

(The following dialogue overlaps until "GO!')

ADELE: ... left you on a doorstep ...

JENNIFER: How would they know that?

ADELE: ... and you want to replace me?

JENNIFER: This isn't about the garbage cans.

ADELE: You don't know what we've done for you.

JENNIFER: It's maybe I'll like her more. Isn't that it?

ADELE: You had so much potential. ...

JENNIFER: She loved me.

ADELE: A brilliant child. And I am ...

JENNIFER: And I'm going to find her.

ADELE: ... totally mystified by what has happened to you.

JENNIFER: Did you hear me? I'm getting out of here.

ADELE: Go. GO! (JENNIFER heads for the front door.)

JENNIFER: I'm going to find her. I want to meet my real mother.

ADELE: Yeah, and how are you going to do that?

JENNIFER: I'll fly.

ADELE: You got a passport?

JENNIFER: I'll get one.

ADELE: You got a travel visa?

JENNIFER: I'll contact the embassy. (JENNIFER opens the front door.)

ADELE: Yeah? And how are you going to get to the airport, huh? How are you going to get out the front door? (JENNIFER stands in the door frame. SHE is breathing hard.) They make names up, Jennifer. They do that, you know? They just fill in the blank. And that's the truth. There's probably a thousand birth certificates with her name on it. And that silly scarf you wear around ... probably the nurse's. The truth? That woman abandoned you. And your father and I took two years filling out the paperwork, getting signatures and mortgaging our lives into the stratosphere so we could get on a plane, to !l scary country where we knew no one! So we could save your life. (JENNIFER keeps putting one foot out the door and then bringing it back in.) We would never give up on you. We love you. And that is why I push you. That is why I won't let you accept this as your life. And I'll be damned if I'm going to let you throw it away, let you spend it with flunkies like Todd, people with not an ounce of ambition. (JENNIFER is trying not to lose it in front of ADELE, who slowly walks toward her.) Listen to me. Listen. My daughter is brilliant. My daughter is an exceptional young woman. And I am not going to let her waste away. (ADELE tries to hug JENNIFER from behind).

JENNIFER: (Freaking out.) Don't you touch me! Don't you ever fucking touch me again!

(SHE runs away from ADELE, back to the kitchen, shaking her hands frantically.)

ADELE: I live in the real world, Jennifer. I'm real. And in the real world, women get screwed out there and if you're not prepared they will squash you. So blame me, lash out at me for your condition, but don't-

JENNIFER: I'm going to find her. I'm going to China.

ADELE: Sure, go to China when you can't even take out the garbage. Keep dreaming.

JENNIFER: I'm going there. You watch me. (SHE runs to her room, ADELE shuts the front door.)

ADELE: (Loud.) The only way you're going to get to China is if this house grows wings.

(ADELE exits, JENNIFER sits down at her computer, typing feverishly.) (Offstage, loud.) I'm real. This house is real, Jennifer. And you can hide in your room and log on if you want to. But that's not real! That's a dream! (We hear a door slam.)

JENNIFER: Dear Dr. Yakunin. It's me, Jennifer Marcus. I know you haven't heard from me in a while, but I need to talk to you immediately. You're the only person I know who'll understand. Find me, please. I need your help. (SHE stops typing.)
```

---

## IC-0602: The Invention of Wings

- Title: The Invention of Wings
- Author (byline): Sue Monk Kidd
- Work: Not specified
- Publisher: Penguin Books
- Publication date as stated: May 2015
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TOGTHER, HETTY, MAUMA, SARAH, MOTHER, TOGETHER, REVEREND HALL, FATHER, OVERSEER
- Teaser before the introduction: Yes
- Spoken words (computed): 1355
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sue Monk Kidd
ISBN: 978-0143121701
Publisher: Penguin Books
Date (Month/Year): May 2015
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 2: Sarah Grimke grew up in an aristocratic, slave-holding family surrounded by privilege.

ACTRESS 1: But at age 11, when she defies the law and teaches her maid, Hetty, to read and write,

ACTRESS 2: Their unequal punishments launch Sarah on a path that would shape her entire future. Sarah Grimké became a committed abolitionist, writer, and suffragist.

ACTRESS 1: But she never forgot her roots . . .

ACTRESS 2: Never forgot Hetty . . .

ACTRESS 1: Never forgot that one time before slavery clipped their wings, the African people could fly.

TOGETHER: The Invention of Wings by Sue Monk Kidd
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actress 1: Hetty, Mauma, Overseer Actress 2: Sarah, Mother, Reverend Hall, Father

TOGTHER: (Both actresses with their bacsk to the audience hum the chorus from “I’ll Fly Away”; Sarah continues to hum while Hetty turns and speaks the next line, then Sarah fades away)

HETTY: (Pg 3) Mauma told me one night when I was ten years old [that] there was a time in Africa the people could fly. She said . . .

MAUMA: Handful, your granny-mauma saw it for herself. They flew over trees and clouds. They flew like blackbirds . . . When we came here, we left that magic behind. (beat) You don’t believe me? Where you think these shoulder blades of yours come from, girl? This all what left of your wings, but one day you gon get ’em back.

HETTY: Even at ten I knew this story about people flying was pure malarkey. We weren’t some special people who lost our magic.

SARAH: (Pg 9) Our house had fourteen-slaves

HETTY: (Pg 3) We were slave people and we weren’t going anywhere. It was [only] later I saw what [mauma] meant.

SARAH: (Pg 8) I’ll never forget my eleventh birthday. Mother had the slaves preparing for my party . . .

MOTHER: (Pg 14) [And when the party began] (claps her hands and brings Hetty to the forefront, Hetty keeps her head down and hands clasped in front of her. Mother straightens a ribbon tied in a bow around Hetty’s neck.) This is our little Hetty. Sarah, dear, she is your present, your very own waiting maid. Happy birthday

(she turns Hetty in a circle)

SARAH: I’m sorry, Mother. . . . . . I can’t accept . . . I don’t need a waiting maid . . . I’m perfectly fine without one.

MOTHER: Enough! (Pg 16) Your guardianship is legal and binding. Hetty is yours, Sarah, there is nothing to be done about it. This is our way of life . . . make your peace with it.

SARAH: . . . Mother, please, let me. . . let me give Hetty back . . . Give Hetty back. As if she was mine after all. As if owning people was as natural as breathing.

HETTY: (Pg 3) We could fly all right, but it wasn’t any magic to it.

SARAH: (Pg 25) At the age of eleven, I owned a slave I couldn’t free.

HETTY: (Pg 22) (knocking at Sarah’s door) Miss Sarah, Miss Sarah, you want me to come in there?

SARAH: (awkward and sad) . . . . Yes, come in . . . I’m pleased to have you for my waiting maid.

HETTY: Sure is cold (rubbing her arms and shivering)

SARAH: . . . You could lay a fire, I guess.

HETTY: (a stricken look on her face, to audience) I’d seen it done, but seeing ain’t doing. (she begins to work on the fireplace) I didn’t know to check the flue . . . (panics and begins waving her arms) and here came all this smoke. (Sarah begins coughing and waving her arms to clear the smoke . . . she opens a window) Oh missus, I sorry! (Sarah takes Hetty’s hands; the girls look at one another and dissolve into giggles; Hetty exits)

SARAH: (Pg 56) But we were crossing a dangerous line, Hetty and I. (Pg 29) Mother had already taken her cane to Hetty once. (Sarah exits)

MOTHER: (pg 23-24) Hetty, you incompetent fool! (brings her cane down on the top of Hetty’s head; Hetty drops to her knees; Mother raises her arm for another blow, then freezes in place)

HETTY: I can’t describe what came next. A voice called steady in my head: Get up from there and look her in the face. Dare her to strike you. Dare her. (Hetty stands up and pokes her face up at Mother; she has anger and contempt in her eyes. Mother lest her arm drop and stepsd back; then exits) (Pg 27) (to audience) That first week, beside the smoke, I spilled lamp oil on the floor, broke one of those porcelain vases and fried a piece of Miss Sarah’s hair with a curling tong. Miss Sarah never tattled.

SARAH: (Pg 30) I never meant to own [Hetty] . . . I tried to free her, but . . . I wasn’t allowed. (Pg 31) The most I could ever offer her was kindness.

HETTY: (Pg 89) We were friends!

TOGETHER: [that’s what] I told myself.

SARAH: (Pg 55) Side by side, we sang songs, we played. (girls play a quick game of tag, giggling)

HETTY: (Pg 54) (to audience) I didn’t know for sure whether Miss Sarah’s feelings came from love or guilt. I [just] know she loved me. And I loved her. (Sarah exits)

(Pg 96) [In those days] Missus was dragging us into the dining room for devotions . . .

MOTHER: (preaching from the Bible) Be content with your lot, for this is of the Lord.

HETTY: (to audience) I wanted to say . . .Take your lot and put it where the sun don’t shine! (Pg 4) [But] already that morning missus had taken her cane to me for falling asleep during her devotions. If you nodded off, you got whacked right in the middle of God said this and God said that and Jesus wept. Jesus wept cause he was trapped in there with missus like us! (Hetty exits)

SARAH: (Pg 38-39) Sunday was the slaves’ only day off. Most were required to show up to their masters’ churches and sit in the balconies. (looks up and back, searching for Hetty) (Pg 40) The slaves began their babble and laughter in the upper galleries. Reverend Hall mounted the pulpit . . . .

TOGETHER: . . . pointed his finger and quoted scripture. (Each assumes the character of a bombastic minister, strutting around the stage) Slaves, be obedient to them that are your masters. Slaves, I admonish you to be content with your lot, for it is the will of God! Your obedience is mandated by scripture. Take heed and may God in his mercy grant that you will be humbled this day and return to your masters as faithful (their pacing brings them face to fac on the last word, which is spoken more quietly in the girls own voices) servants.

SARAH: (Pg 41) If everyone was so keen to Christianize the slaves, why weren’t they taught to read the Bible for themselves? (Shakes her head. Beat)

MOTHER: (Pg 38) Sarah, I trust you’re prepared to give your first lesson.

SARAH: I’d recently become a new teacher in the Colored Sunday School, a class taught by girls, thirteen years and older, but Mother had prodded Reverend Hall to make an exception. (Turns to her class, she begins to sing the alphabet) (Pg 41) A, B, C, D, E, F, G . . . (they get louder and louder)

TOGETHER: (Hetty joins in) H, I J, K, L, M, N, O, P

REVEREND HALL: (Pg 42) (angry and pious)What is going on here! We do not sing in Colored Sunday School and we most assuredly do not sing the alphabet. Are you aware it is against the law to teach a slave to read?

SARAH: (Pg 41) I thought of Hetty. I knew she explored the books on my desk. How she would love to learn these twenty-six letters!

HETTY: (whisper-singing to herself) A, B, C, D, E, F G

SARAH: (Pg 57) Hetty, shall I teach you to read? (Hetty nods vigorously and the girls turn their attention to a slate and learning) (to audience) I’d never taught anyone to read, but as it turned out, Hetty had a knack. I’ll never forget the moment when she made the magical connection and the letters passed from nonsense into meaning. (Pg 278) I told myself reading was a kind of freedom, the only one I could give.

HETTY: How do you spell Hetty?

SARAH: H-E-T-T-Y (Hetty writes on her slate)

HETTY: (Pg 60) My real name is Handful. (Pg 57) How do you spell water?

SARAH: W-A-T-E-R (Hetty writes on her slate) Once, I glimpsed her in the work yard writing in the dirt with a stick. (Hetty drops to her knees to do so) She’d scrawled WATER for the entire world to see. (Sarah races to rub the letters away with her foot). What are you doing? Someone will see!

HETTY: (Proud of herself, but instantly scared, she helps erase the letters) Don’t you think I got my own foot to rub out letters! (to audience) Since that day [when] I found how to read and write . . . (Pg 84) I found the part that refused to bow and scrape, and once you find that, you got trouble breathing on your neck. (Hetty exits)

SARAH: (Pg 9) Father was a judge on South Carolina’s highest court. Everyone said I was Father’s favorite. (Pg 39) [But] Father was furious.

FATHER: (Pg 66-70) You have disappointed me, Sarah. (He holds out his palm to stop her reply) I have brought you here to listen. Do not speak. It has been brought to my attention that your slave girl has become literate. Do not deny it. She wrote a number of words on the muddy ground in the yard and even took care to sign her name.

SARAH: (to audience) Oh, no! Handful had been careless. We’d been found out. But my mind could not accept that Father, of all people, believed her ability to read was an unpardonable offense. (To father) I’m sorry, father . . . I meant no harm.

FATHER: No harm? You taught her! From now on, you are denied all access to books.

SARAH: No books! Father, I beg you . . . P-please, don’t take books from me. (Sarah exits crying and as she reaches the porch, she sees Hetty, her arms tied to the porch rail)

HETTY: (her back to audience, arms crossed above her head, she takes 3 lashes from an unseen hand; both girls react to each lash) ***** long beat ****

HETTY: (Pg 43) What came next was a fast, bitter wind.

OVERSEER: (Pg 164) Your owner has decided the Work House will put you in a wholesome frame of mind.

HETTY: (Pg 35) Far as I knew, not one Grimke slave had gone to the Work House. The white folks called it the Work House. Like the slaves were in there sewing clothes and hammering horseshoes. But I knew about the torture house on Magazine Street. I knew about the dark hole they put you in and left you by yourself for weeks. I knew about the (Pg 164) treadmill.

SARAH: (Pg 338) I remember watching it unfold as if from a distance.

HETTY: (Pg 174) (Hetty holds a bar above her head, walks on the Mill Wheel crying) I’m gripping the bar with all the strength I got. Climbing the wheel, climbing the wheel.

SARAH: (Pg 340) I cried too, but my tears were a mix of wretchedness and fear.

HETTY: (Pg 174) The knot that lashes my wrist to it comes loose.

SARAH: (Pg 351) Slavery is a hell-concocted system.

HETTY: (Pg 174) A child screams. Don’t look, keep going. [But] I look and its little head is bleeding. Red and wet. And I fell . . . . (Sarah gasps and kneels over the dying body of Hetty)

SARAH: (Pg 166) Handful’s foot was twisted inward at an unnatural angle and there was a gash exposing raw flesh. (Pg 351)

HETTY: (Pg 3) Mauma told me there was a time in Africa the people could fly. (Pg 174) [But] there ain’t no wings sprouting off my shoulders.

SARAH: (Pg 351) (Sarah kisss Hetty’s forehead, stands and speaks through angry tears) The Negro is not some other kind of creature than we are. (Pg 323) Not chattel to be owned, but a person under God. (Pg 351) Whiteness is not sacred! (Sarah begins to hum the chorus from “I’ll Fly Away” while Hetty speaks the final lines)

HETTY: (Hetty speaks as her eyelids fall shut on the world) (Pg 324) What was it for? What was any of this for?
```

---

## IC-0603: Investment Dating

- Title: Investment Dating
- Author (byline): Ira Brodsky and Barbara Lhota
- Work: Duo Practice and Competition: 35 8-10 Minute Original Comedic Plays for Two Females
- Publisher: Smith & Kraus
- Publication date as stated: September 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MEG, IRIS
- Teaser before the introduction: Yes
- Spoken words (computed): 1970
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ira Brodsky and Barbara Lhota
Book: Duo Practice and Competition: 35 8-10 Minute Original Comedic Plays for Two
Females
ISBN: 978-1575253800
Publisher: Smith & Kraus
Date (Month/Year): September 2004
```

### Introduction (context only: never use it for content warnings)

```text
Actress Playing Iris: (While Meg is still la, la la-ing) Meg and I have been friends for ever.

BFFs for those of you who are into acronyms. I’d do anything for her.

(FREEZE) Actress Playing Meg: Did Iris just say “anything?” Perfect! Now I just have to figure out the

best way to ask her. . . . Actress Playing Iris: (UNFREEZE) Ask me what? Actress Playing Meg: Ummmm, nothing . . . Hey are you going to the homecoming dance? Do

you have a date yet? (FREEZE) Actress Playing Iris: Uh, oh . . . this is NOT going to be good. When you’ve known Meg for as

long as I have, you KNOW when she has something up her sleeve. TOGETHER: Investment Dating by Ira Brodsky and Barbara Lhota
```

### Performance text (classify this)

```text
MEG: (Speaking in hushed tones, with contained excited.) Oh wow. Oh wow. Oh. Wow. I think I'm going to faint. I'm not kidding. You're not going to believe what just happened.

IRIS: (Dryly.) Sister Jaye had you dissect a cow eye again?

MEG: What? No. What are you talking about?

IRIS: Last time you said "You're not going to believe what just happened," Sister Jaye had you dissect a cow eye and then you passed out.

MEG: No, I didn't. Elizabeth Holt passed out. Why do you always make me out to be such a wuss?

IRIS: I don't always make you out to be a wuss. I don't need to. You are a wuss.

MEG: I just felt wobbly and pretended to faint to get out of class early.

IRIS: (Nods and smiles.) Uh-huh. And I suppose you had an incredible need to smash your face into the floor pattern when you watched me get my ears pierced too?

MEG: (Cringes.) Well, it ... was hot in there.

IRIS: Just admit it, Meg. You have a weak stomach. You pass out. No big deal.

MEG: But I don't! I don't have a weak stomach. I'm cool!

IRIS: I didn't say you weren't cool. You're a cool person who faints. 'Member when they forced us to watch that National Geographic wildlife special and the mountain lion tore the guts out of the-

MEG: All right! I remember. Ewww. Let's think about something else. (Trying to get the image out of her mind. Singing.) La, la, la!

IRIS: (Soothing her by patting her back.) I can just imagine how you felt when Sister Jaye put her scalpel into the cow's

MEG: All right! You're doing this on purpose. How did we get here? I was telling you about my good thing and suddenly we're dissecting cow eyes and wandering down woozy lane.

IRIS: Feeling fainty is a good thing?

MEG: You know very well that I was being ... I was exaggerating. I'm excited. I'm not actually feeling fainty. I just have this incredible feeling. It's like I've lost all my senses.

IRIS: And this is a happy thing? To lose your senses?

MEG: (She smiles.) Yes, it is.

IRIS: No wonder there are so many happy Republicans [Democrats] right now.

MEG: Don't be so cynical, Iris.

IRIS: So don't be so sappy. It encourages my cynical-ness. I have to counterbalance the "S" factor. So what is it exactly, not that I really want to know?

MEG: Well. (Quietly, out of the side of her mouth.) You-know-who (Nodding her head in a backward direction very subtly.) asked me to you-know-what.

IRIS: Well, that clarifies things. (Looking over toward her nod.) Which who? Which what?

MEG: (Grabbing her.) Well, don't look!!

IRIS: How am I supposed to know who the (Quietly.) you-know-who is then?

MEG: How can you be so remedial? How many you-know-who's have I mentioned? (Iris gives Meg a look.) OK. Good point. But this is the you-know-who that has been the you-know-who since forever.

IRIS: Really? You're kidding? (Eyes widening. Mouth drops. Beat.) Are you telling me you have a date with (Whispers with reverence.) Kevin? The guy? Mason?

MEG: Oh. No, no. Not that forever. That's last month's forever! Think more recent, more do-able, and more short.

IRIS: (Thinks.) Jason Harley?

MEG: Not Oompa-loompa! Short. Less wow than Kevin Mason, but more smart. My guy sang in the talent show. He always rests his feet on the back of my chair. He gave me his eraser a couple days ago. To keep. Remember? (Iris has no idea.) He blinks a lot and he has this cute dent in his face.

IRIS: Dent? In his face? I'm sure if you mentioned this guy, you didn't mention this dent thing. That I would have remembered.

MEG: The dent crinkles so cute when he smiles.

IRIS: So it's like a dimple or more of a full-size crater?

MEG: Yeah, well, I guess it is more like a dimple

IRIS: OK, erasing the Elephant Man image.

MEG: He's got a great personality, but he doesn't talk really.

IRIS: At all?

MEG: Very little. I mean, how much is really necessary?

IRIS: (Nods.) Some. For instance, if I were in a crisis situation ... like maybe my house was burning or my mother was angry because my boyfriend and I were coming home late from a date. I wouldn't want a strong, silent type. I'd rather have a wimpy talker. A guy who could come up with "Well, we both got food poisoning from something we ate at the salad bar at Denny's. We had to stop at my friend's house right away, Ms. Hemchak so we could ... you know. Otherwise we would have been home on time." Or, in the burning house situation, a loud, decisive "Help! Follow me!" might be good too.

MEG: Well, sure. In a crisis, but otherwise ... Personally, I don't want a boyfriend who blabbers on and on and on. That's why I have you.

IRIS: Thanks. So let me ask you this. How do you know he has such a great personality if he doesn't talk?

MEG: He doesn't even have one zit!

IRIS: You’re kidding? Find out what he washes with!

MEG: OK, but can we get back to the point.

IRIS: I think I'm lost on the who. Maybe we should start with the you-know-what instead.

MEG: The homecoming dance, Iris! I've been talking about it for the last two weeks!

IRIS: That was anticlimactic. Let's hope the "who" has a little more umph.

MEG: Well, he has the goldfish. (Iris looks terribly confused.)

IRIS: "The" goldfish. (Meg nods.) Is this the only one left in the international community?

MEG: It's the goldfish in the science lab. He won the goldfish last year in the spelling contest and donated it. (Iris is still perplexed.) His last name is also the name of an animal.

IRIS: The fish?

MEG: No! The guy who asked me to homecoming. Look. It's (Mouths "Alex Fox" several times as Iris tries to guess.)

IRIS: Hal Thomas? Our Spanish teacher? That's sick! Although potentially advantageous.

MEG: No, no. (Continues to mouth "Alex Fox.")

IRIS: AI. Al-Ia. Alan? Allan Nicholson?! Oh? (Thinks.) He's cool.

MEG: No, Iris. Nicholson is not the name of an animal!

IRIS: OK, animal last name not last name of an actor who wears sunglasses and dates woman younger than his socks. Oh my gosh-animal? Is it Robin Anto-

MEG: No! His last name is an animal, not his first name. It's (Very quietly, out of the corner of her mouth.) Alex Fox.

IRIS: What did you say? (Meg says "Alex Fox" again very quietly, almost inaudibly.)

IRIS: Huh?

MEG: (Singing.) I just called to say, I love you. (Iris' curiosity is piqued. The name sounds familiar, but she's still unsure. She thinks. Meg does some weird dance move with her hand.}

IRIS: (Yells.) Alex Fox!

MEG: (Grabbing Iris' face to stop her yelling. Meg speaks from the side of her mouth.) Stop! (Pulling her into a huddle.) He'll hear you. He's right over there.

IRIS: Where? (Looks. Meg pushes her arm to stop the head turning.) He can't hear us over there. That's all the way across the cafeteria.

MEG: Don't look! He'll think we're talking about him. He probably just heard you.

IRIS: No, he didn't, but he's going to know we're talking about him because you're doing that thing again.

MEG: What thing?

IRIS: That thing you always do when you think people can hear you when they can't. That side-of-the-mouth thing that makes you look like you have palsy or something.

MEG: (She does it.) I'm not doing anything with my mouth. I'm just talking quietly.

IRIS: (Imitating Meg.) Yes, you are. You just don't know it.

MEG: Oh my God. That does look bad. (She stops the mouth thing.}

IRIS: So Alex Fox, huh? He's kinda boring. I mean, he doesn't talk. At all.

MEG: He sings.

IRIS: True. But not well.

MEG: I thought he was great in the talent show. And cute. All the girls did.

IRIS: What girls?

MEG: Well, I don't know. I thought he was cute.

IRIS: He was. Sort of. For an awkward pubescent white boy with no pitch, no confidence, and no sense of rhythm.

MEG: That's not true! He had confidence. He was probably downright cocky or he wouldn't have gotten up in front of everyone to, to ...

IRIS: To embarrass himself so completely? (Patting her.) Anyway, I'm happy for you, Meg. Have fun.

MEG: No, don't do that talking down to me thing. You sound like I've stooped.

IRIS: Well, obviously you don't mind stooping.

MEG: I do mind stooping. I don't want to live with this feeling that I'm just some big stooper and that's it. I thought this was good-going to the dance.

IRIS: I just think if you were going to agree to go with Alex Fox, you might as well stoop down into the depths of desperation, do some more charity work, and pick up Fred Murphy on the way.

MEG: (Laughs.) Well, that's funny.

IRIS: What? What's funny?

MEG: Well, Alex and Fred are pretty good friends. Funny you mention Fred.

IRIS: Uh-huh. So? Where does the funny come in?

MEG: Didn't you say once ... ? I remember. You said that Fred, although a bit of a cretin, was ... funny, ... special, and ... specially funny.

IRIS: (Beat.} I did not.

MEG: I know you did. You definitely said he was funny and special.

IRIS: Well, I might have used the word ... funny. Perhaps I even used the word special, but you must have misinterpreted my meaning.

MEG: Well, see?

IRIS: See what?

MEG: Maybe I misinterpreted, or maybe you meant it in multiple ways. Because maybe Fred is special to you in some ways.

IRIS: He is. In a mock-and-make-fun-of sort of way. Where is this heading, Meg?

MEG: Well, guys don't like to go to dances alone.

IRIS: True. They don't know where to pin the corsage.

MEG: No, I mean they like to go in a group with a date and a best friend.

IRIS: OK, you know what? I'm late for Spanish.

MEG: (Grabbing her.) Wait, Iris! You've got to do this.

IRIS: Ohhhhhh. Nooooo! I don't have to do anything, Meg. I'm not being pulled into another Bob Alberts fiasco.

MEG: He wasn't that bad!

IRIS: He tried to French kiss me with gum in his mouth. I had a spontaneous and relentless gag reflex and almost choked to death!

MEG: But Fred wants to take you so bad. He likes you. He really likes you!

IRIS: No, he can't! I won't let him! Don't you let him! Uh! Me? Me?! (She points to herself. Meg nods.) Why is this happening? What is it about me that's such a magnet for the festering warts of humanity?

MEG: You're funny and a vegetarian and read philosophy.

IRIS: (Hitting her hand.) That was a rhetorical question!

MEG: You're different, Iris, and lots of guys like that. Not easy to peg.

IRIS: (Beat. Sweetly.) You're different too, Meg. In a rotten, horrible, nightmarish, diabolical way. Now, leave me alone in my misery,

MEG: So will you at least think about it?

IRIS: I'm saying I would rather hang from the gym by my fingernails, be mocked by my fellow art students, and forced to listen to my sister's Britney Spears CDs for twenty-four hours than go to the dance with you and Alex Fox and Fred Murphy.

MEG: Oh please, please, Iris. Just this once. I promised Alex we'd double-date.

IRIS: So un-promise him.

MEG: I can't. I told him it was a sure thing. (Begging.) Oh please. Pretty please. (Iris shakes her head no.) Don't do this to me. This is my life at stake.

IRIS: Well, if Alex is your life, you deserve to perish.

MEG: What if I pay you?

IRIS: (Shocked.) What? Are you serious? (Meg nods.) Sell my company for ... Sell my body, my spirit like some cheap call girl! That's disgusting! How much?

MEG: How much is necessary?

IRIS: (Beat. Taking this in.) How much you got?

MEG: Twenty? (Iris shakes her head with disapproval.) Twenty-five? Come on!

IRIS: For a whole night with a guy who will ruin my reputation for years to come? I don't think you're accounting for the long-range ramifications. I'd consider forty.

MEG: Forty?! I don't have forty, Iris! I've never had forty, ever! Uh! OK, thirty-seven fifty. And that's the best I can do. I'll have to borrow the two fifty from my brother, which you know I can't stand. So what do you say? (Getting on knee.) Please? Please?!

IRIS: (Thinks. Sighs.) I'm such a good friend to you, Meg.

MEG: (Jumping for joy.) Yah! All right! You'll probably even have fun! Fred seems really nice.

IRIS: He ate glue, Meg.

MEG: He was just trying to see if it would kill him. He's scientific!

IRIS: He's disturbed.

MEG: He's one of those late bloomers who will probably be a looker in early college ... or maybe not, but he'll invent some incredible computer program that will change the way we do business for years to come. He'll be a multi-millionaire in a few years and with some help, perhaps from a psychologist or even Dr. Phil, he may become a full-fledged well-rounded human being who you can write about in your depressive autobiography when you get about twenty something.

IRIS: He ate glue, Meg. He ate glue. (Puts out her hand.) So pay up!
```

---

## IC-0604: John Lennon and Me

- Title: John Lennon and Me
- Author (byline): Cherie Bennett
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: July 1996
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: STAR, COURTNEY, DR. SCOTT, THE TORTURER, CLAUDIA, VOICE OVER
- Teaser before the introduction: Yes
- Spoken words (computed): 1763
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cherie Bennett
ISBN: 978-0871297020
Publisher: Dramatic Publishing
Date (Month/Year): July 1996
```

### Introduction (context only: never use it for content warnings)

```text
(Actress 1 hums Let it Be by the Beatles** softly while Actress 2 speaks)

ACTRESS 2: According to the CF Foundation, more than 30,000 people in the US are living with cystic fibrosis. It is a fatal disease. But the stats for rheumatic heart disease are even higher. Rheumatic fever causes permanent damage to the heart valves. More than 300,000 people die from its debilitating heart complications each year. These illnesses are termed chronic and require continual monitoring and interventions. There are no cures.

ACTRESS 1: But as John Lennon once said, “Count your age by friends, not years. Count your life by smiles, not tears.

TOGETHER: John Lennon and Me by Cherie Bennett.
```

### Performance text (classify this)

```text
NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actress 1: Star

Actress 2: Courtney, Dr. Scott, Claudia, The Torturer, Voice over

STAR: (Pg 8-9) (Courtney hums Imagine by John Lennon* off stage softly throughout Star’s opening monologue) Allow me to introduce myself. Contrary to what it says on my birth certificate, my name is not Stella Grubner. I renamed myself Star – no last name, thank-you-very-much. I mean, Stella?? (coughs) Claudia, my mother – you’ll meet her later – tells me that when I was born, she was an actress in New York City. When my mom got pregnant with me, she was in rehearsal for this famous play, A Streetcar Named Desire. Because of me, she had to drop out. So she named me Stella, after the character she never got to play. Then Claudia ran out of money, which is how we ended up moving to this little town outside of Nashville. (coughs) (Courtney enters) (Pg 15) [That’s] my roommate, Courtney Cambridge. Prettier than me. Taller than me…

COURTNEY: (Pg 17) I’ve never been sick before . . . I just had this bad sore throat. I didn’t tell my mom right away because I didn’t want to miss the big away game we had. So then it got worse and worse. It turned out to be strep throat, and that turned into rheumatic fever. And now they think it did something to my heart.

STAR: (to Courtney) Can’t be that bad. Your lips and your nails aren’t blue. (coughs) If something is mega-wrong with your heart, you turn blue.

COURTNEY: (Pg 18) You don’t seem very sick, either. Except for your cough.

STAR: No problem. (Pg 9) I plan to run away to New York when I’m seventeen, to become a very famous actress. The sooner the better . . . The thing is, I was born with cystic fibrosis. When I was ten I looked it up in a medical dictionary. It said: “the average life expectancy is twenty-five years. This disease is always fatal.” Fatal. As in dead. Well, I am not average. I am extraordinary. So I decided I’m not going to die. I’m just not.

STAR: (Pg 9) (gestures to her surroundings) This is Heart House – a place for sick kids. I’ve probably slept more nights here than I’ve slept in my own bed. The bad news is my health has taken (melodramatically) A Turn For the Worse. (Dr. Scott enters) (Pg 12) (to Dr. Scott) Okay, I coughed up some blood last night. Not much, though. (coughs)

DR. SCOTT: How many thumps are you doing each day.

STAR: (trying to catch her breath) At home Claudia’s giving me two, but The Torturer says I have to start doing three a day. (Torturer’s them music --maybe Jaws – As Ina Tortunesky enters) It’s her idea of a good time . . . (to audience) (Pg 13) That’s her, Mrs. Tortunesky – The Torturer. If she was green, she could pass for The Incredible Hulk. She used to be an army nurse. Whenever I’m at Heart House, she wakes me up every morning at 6 am for physical therapy by barking commands in my face.

THE TORTURER: (barking her commands to the audience while whacking the air with her hand – Star li-synchs the words at the same time) Lie still! Turn over! Now, cough! Cough!

STAR: (to audience) It’s supposed to keep me from choking to death on – akay, this is disgusting – thick mucus. After that I have to breath this crap called Pulmozyme through an oxygen mask and then she whacks me again. I really hate her.

DR. SCOTT: She’s actually not a bad person. She’s just kind of . . . serious.

STAR: Serious? She’s sadistic! I heard she whacked one CF kid so hard he flew off the bed and landed in the corner like a hockey puck. And then she yelled . . .

THE TORTURER: Score!!!!

COURTNEY: (Pg 17) (looking at a poster on the wall) I really like your poster.

STAR: He was the most talented person who ever lived. And he died so young.

COURTNEY: (horrified) Paul McCartney is dead??

STAR: That’s Lennon. John Lennon. (rolls her eyes – to audience) She’s killing me!

COURTNEY: (Pg 18) You know, I was so nervous coming up here. Walking down the hall, I saw some really sick-looking kids. Two of them were bald!

STAR: Chemo.

COURTNEY: That means they have cancer, right? It was so horrible! I just prayed I wouldn’t have a really sick roommate. It would be so embarrassing, like when my best friends comes to visit me, you know?

STAR: Oh, sure. My friends come visit me all the time, too. (To audience) Like I was really going to tell her that I actually didn’t have any friends outside of Heart House. It’s hard to make friends when you don’t’ go to school. So sue me. I lied. (Pg 22) Actually I went to regular school for a while, in fourth grade. But I coughed up blood and all the kids ran out of the room screaming. (The Torturer’s theme music plays – she enters)

THE TORTURER: (Pg 24) So, I haven’t seen you in three months. We have much work to do.

STAR: (Pg 25) Where are your manners? You could at least say hello to Courtney, my new roommate.

THE TORTURER: (stepping menacingly toward Courtney) You don’t have cystic fibrosis, correct?

COURTNEY: (staring in horror) No! No, I swear I don’t! (Star laughs, which cause her to cough)

THE TORTURER: Enough levity. We have work to do

STAR: Watch closely. You are about to see a 13-year-old girl whacked to death.

THE TORTURER: Nonsense, all you’ll experience is . . . (She laughs ominously) SOME DISCOMFORT. (The Torturer stands over Star and raises her arm for the first blow.)

STAR: Hold that thought (The Torturer freezes. Star steps out of the scene – The Torturer whacks viciously at the air as Star watches and narrates the action to the audience in the style of a prize-fight announcer. Into the mike) (Pg 26) And it’s THE TORTURER, moving in fast, striking the first blows. A left jab! Another! She hooks to the body! Ouch! Ladies and gentlemen, our champ is taking a tremendous pounding! What grit! What fortitude! What a true champion! (A boxing ring bell sounds - She steps back into the scene, coughing, exhausted and having difficulty breathing)

THE TORTURER: You were very congested. We’ll have to work harder this evening (She exits and Star’s Mom, Claudia, enters)

CLAUDIA: (Pg 27) Hi, I’m Star’s mom. Call me Claudia.

COURTNEY: Claudia. Okay, Claudia. My name is Courtney, Claudia

STAR: (to audience) Clearly Courtney wasn’t used to calling someone’s mother by her first name. But my mother doesn’t look like anyone’s mother. I like Claudia and Claudia likes me, but she doesn’t like my disease. It scares her too much, which scares me too much, so we never talk about it. I act like it’s no big thin, and she acts like she believes me.

CLAUDIA: So, what’s kickin’, chickens?

STAR: The usual. No biggie.

CLAUDIA: You’re such a trouper. (She kisses Star) (Pg 28) Listen, I’ve got to go down and fill out some of those endless papers. Later! (she exits)

COURTNEY: Your mother is unbelievably fabulous! (Pg 29) Why couldn’t my father have married someone like her? (thinking a moment) You know, I though that being here would be the worst thing in the entire world. But . . . it’s not so bad. I guess maybe they put us together because we’re not as sick as the others. (shyly) I’m really glad you’re my roommate. (she exits)

STAR: It’s gonna be a riot. (to audience) And all I had to do was to spend 24 hours a day pretending I wasn’t really very sick at all. No problem. (beat, Star’s façade drops) (Pg 31) Here’s the thing. When you’re sick, I mean really sick, you live in a different world. It’s like . . . like walking by a candy store, and you see all these kids inside, laughing, hanging out, having a great time, but no matter what, you can never do more than press your face against the glass. *****

DR. SCOTT: (Pg 35) (enters) Hey, Courtney. We’re going to start you on some intravenous antibiotics today. Same stuff you’ve been taking, but this should help you get better faster.

COURTNEY: Wait a second. Are you telling me that you’re going to stick on of those things in my arm like Star has? (grimaces and holds out her arm. mimes having an IV hooked up – She looks at the IV bag and at her arm) (Pg 37) I hate this thing. My hand hurts.

STAR: It’s making you kind of pale.

COURTNEY: (angry) (Pg 39) I’m stuck in this stupid place with this stupid thing in my arm! (near tears) It’s no use, Star! I can’t do this!

STAR: (Pg 51) I – I – I – I- (Pg 52) (Coughs, clear her throat, coughs again, longer and deeper)

COURTNEY: Star, are you okay? (more coughing, gagging) Star? Star?

STAR: (Pg 53) Courtney, I think I’m going to – (She wretches deeply, she can’t stop coughing, gasping for air, she holds out her hands, covered in blood)

COURTNEY: (horrified) Oh, my God! (Screaming and crying hysterically) Help! Somebody come help! Please! Somebody! ***** DAYS LATER *****

STAR: (Pg 54) (To audience) So, here we are . . . When last we saw The Champ – meaning me – things were not looking too good. We pick up the story the next morning, which is good news, since it means I didn’t croak. I could hear Claudia talking, but I was so out of it, it was like listening to them on the radio.

CLAUDIA: (Pg 55) I know all about the lung infection eroding a major artery. But why did she bleed so much more this time? She’s been fine. She’s a fighter.

DR. SCOTT: Come on, Claudia. You know it’s getting worse. Star knows it too. (a beat) (Pg 56) Call me if she wakes up. (he exits)

STAR: (to audience) I did wake up, but I couldn’t really talk for days and days. Imagine me, not talking! It was a fate worse than death! (re-enters scene and awakens from the sedatives) Where’s Courtney?

CLAUDIA: You’re awake! Do you remember what happened?

STAR: (it comes flooding back to her, speaking with difficulty) Oh, God. I can’t believe that happened in front of Courtney. She’s going to hate me.

DR. SCOTT: (enters) I heard you talking. How do you feel?

STAR: (Pg 57) I’m fine.

DR. SCOTT: It must have been scary, though. It’s okay to say so.

STAR: I was so scared I was going to d . . .

CLAUDIA: (cutting her off – angrily to Dr. Scott) Don’t tell her to be scared if she’s not, for Crissake!

DR. SCOTT: (also angry) Star, your mom and I are going down the hall for a little chat, then we’ll be back, okay? (they exit and Courtney enters)

COURTNEY: (Pg 58) How are you feeling?

STAR: I’m fine. What did I miss while the lights were out?

COURTNEY: Why are you making jokes?

STAR: Why not? You needed a little excitement in your life. You must be better, they took your IV out.

COURTNEY: Stop it! I have to talk to you . . . (Star puts her hands over her ears and sings something like the opening lines of She Loves You by the Beatles*** to down out Courtney) (Pg 59) It was so awful! I thought you were going to die! The blood was everywhere! All that blood . . . Why didn’t you tell me?

STAR: (uncovering her ears) Tell you what?

COURTNEY: How sick you are! Your cystic fibrosis – You’ve lived practically all your life in Heart House.

STAR: I’m not that sick! All it means is that I cough sometimes.

COURTNEY: (angrily grabs a folded piece of paper from her pocket. She unfolds it and reads it out loud) Cystic Fibrosis (Pg 60) is fatal. The cause of death is chronic respiratory failure. In some patients bleeding from the lungs may result in death due to choking and shock.

STAR: I underestimated you. You are bright enough to use a dictionary.

COURTNEY: Why didn’t you just ell me the truth?

STAR: You hate sick kids!

COURTNEY: I never said that!

STAR: You did too! You said you were so glad your roommate wasn’t really sick. You said the kids who had cancer were so gross because they lost their hair. What was I supposed to say? “Guess what, Courtney . . . I’m one of them!”

COURTNEY: I didn’t understand . . .

STAR: Well, most people don’t. Which is exactly why I don’t tell anyone.

COURTNEY: So . . . I guess you don’t want to be friends with me after all, then.

STAR: (to audience) So, go figure. Courtney knew the truth, and she wanted to be my friend anyway. (Courtney exits; long beat) (Pg 77) So, anyway . . . . Courtney’s funeral was two weeks ago . . .

VOICE OVER: (off stage) (Pg 74) Code blue. Code Blue. Dr. Rhodes, second floor stat (repeat through Star’s next lines)

STAR: (Pg 77) There were a lot of great things about Courtney, but the greatest of all was that she accepted me completely, just as I am. And something about her accepting me made me start to accept me too. It’s just about the greatest gift anyone ever gave me.

VOICE OVER: (Pg 75) Blood pressure zero. Pulse zero (a high-pitched buzzer goes off)

DR. SCOTT: (off stage) Courtney’s heart was damaged and it ruptured. There was nothing we could have done.

STAR: (Pg 76) (crying) I’m so afraid I’ll die. I don’t want to die! I don’t want them to cover my face with a sheet like they did to Courtney. (composes herself) (Courtney hums Let it Be by the Beatles** softly off stage) (Pg 77) And she’s smiling down on me right now, telling me that just like John Lennon, I should enjoy every moment of my time on this planet, however long it is.
```

---

## IC-0605: Keely and Du

- Title: Keely and Du
- Author (byline): Jane Martin
- Work: Humana Festival 1993: The Complete Plays
- Publisher: Smith & Kraus Publishers
- Publication date as stated: 1993
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: DU, KEELY
- Teaser before the introduction: Yes
- Spoken words (computed): 2357
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jane Martin
Book: Humana Festival 1993: The Complete Plays
ISBN: 1880399377
Publisher: Smith & Kraus Publishers
Date(Month/Year): 1993
```

### Introduction (context only: never use it for content warnings)

```text
Keely, who was brutally raped by her ex-husband, is kidnapped by right-to-lifers before she can obtain an abortion. She is chained to a bed in a basement and told that she will be forced to carry the child to term. Du is a Bible Christian who cares for Keely. Here, these two very different women begin to find some common ground. Keely and Du by Jane Martin
```

### Performance text (classify this)

```text
Characters: KEELY: a pregnant woman taken hostage by a militant anti abortion org, 20-30

DU: the woman assigned by the organization to be her caretaker & companion, 65

The Setting: A basement in Rhode Island, the present

(Lights up on Keely sitting up in bed eating breakfast.

DU: (She watches as Keely eats around the eggs.) You ever try catsup?

KEELY: What, on eggs?

DU: Oh, we'd buy this spicy kind by the case, Lone Star Catsup. My brothers would heat up the bottles in boiling water so they could get it out faster. (A moment. Keely pokes at her eggs.)

KEELY: (Finally.) For what?

DU: Eggs, rice, they put it on cantaloupe which like to drove my mother from the house. (An involuntary smile from Keely, and then, sensing her complicity, silence.) So, he left high school, Cole?

KEELY: Listen...(Having started to say something about the situation, she thinks better of it, then her need to talk gets the better of her.) He took a factory job. He was into cars, he wanted this car. His uncle worked a canning line got him on. (A pause.)

DU: And?

KEELY: We still went out. . . off and on. We got in an accident, we were both drunk, I got pretty cut up. My dad's cop pals leaned on him. After that. . . I don't know, lost touch. (A pause.)

DU: Lost touch.

KEELY: I don't want to get comfortable talking to you.

DU: Keely. . .

KEELY: Forget it.

DU: Please...

KEELY: I said forget it. (A long pause.) I'm going crazy in here. I could chew off my wrist here. That paint smear on the pipe up there, I hate that, you know? This floor. That long crack. Everywhere I look. Wherever I look, it makes me sick. (She tears up.) Come on, give me a break, will you. I gotta get out of here, I can't do this. (Mad at herself.) Damn it.

DU: (Gently.) Help us pass the time, Keely. You're not giving up. I know that. (Keely looks down.) You lost touch.

KEELY: Yeah. (A pause.) There were guys at school, you know, different crowds. . . 37 days, right? (Ou nods.) I wa . . . man. . . I was, umm, waitressing, actually before he left, down at the Gaslight. .. he didn't like me working. I just blew him off. (A moment.) If I talk, it's just talk. . . only talk, that's all . . . because this is shit, what you do to me, worse than that.

DU: Only talk.

KEELY: Because I don't buy this, you tell him I don't buy it. (Du nods. They sit. Then. . .) So I was at a Tammy Wynette concert, you know, somebody else's choice, and there he was, definitely his choice as I found out, and my date is . . . well, forget him, so we got together and it got hot really fast and we ended up getting married, which nobody I knew thought was a good idea, which made me really contrary which is a problem I have. . . like up to here. . . so, you know, what I said, we got married, plus. . . (Finishing the eggs.) The catsup's all right.

DU: Oh, it's good.

KEELY: I mean I knew who he was, and I did it anyway. I knew about the drinking, I knew about the temper, I don't know where my head was, in my pants, I guess.

DU: Well, I married a man deemed suitable and that can be another problem. There is only one way a man is revealed, and that is day in and day out. You can know a woman through what she says, but don't try it with a man.

KEELY: Yeah, he had a line. I even knew it was a line.

DU: I'll just take the tray.

KEELY: And I knew he drank. Oh, hey, he downpedaled it before we got married. . . way, way downpedaled. He would drink, say two, two drinks, say that was his limit, take me home, go out pour it down 'til ten in the morning, I found that out.

DU: They talk about drugs, but it's still drinking the majority of it, now I have never been drunk in my life, is that something? I'm often tempted so I'll know what I'm missing, yes ma'am, I've tried the marijuana.

KEELY: Bull.

DU: Oh I have, and it didn't do a thing for me, and that's a fact, and I've been in a men's room which I doubt you have, and I've kissed three men in one day, so don't you think you can lord it over me.

KEELY: You smoked?

DU: Oh, yes. Found the marijuana in my son's sock, sat on his bed, waiting 'till heard him come in the front door, lit up and let him come on up and find me there doing it. Shocked him down to his drawers I might say. . . straightened him up in a hurry. That's the one who's an accountant in Denver. All boys, I would have given my heart for a girl baby. (An awkward pause.) It's noisy, too many boys in a house.

KEELY: (A pause.) Suitable?

DU: What? Oh, suitable. I was keeping company with a slaughterhouse man who could pop your eyes out with his shirt off, but he was an atheist and a socialist and who knows what else, and that was one too many for my father so he ran him off and put me together with a nice German milkman whose father owned the dairy, if you see my point. August. His name, not the month. I married him at nineteen, in 1947 and two months later the dairy went under, so I got no money and he looked just terrible undressed. The fact is he was an uninteresting man, but he got into the storage business and turned out a good provider. Now, listen close here, we went along 'til he bored me perfectly silent, if you can imagine, and God found us pretty late when the kids were gone or near gone, and God found that man he turned him into a firebrand and an orator and a beacon to others, and I fell in love with him and that bed turned into a lake of flame and I was, so help me, bored no more, and that's a testimony. There is change possible where you never hope to find it, and that is the moral of my story, you can stop listening.

KEELY: Right.

DU: It is. Still nothing to look at but I just close my eyes. The children kept me in that marriage until it became a marriage and the love I bore them kept me alive until the marriage could catch up.

KEELY: So what am I supposed to be? Glad?

DU: Things do change.

KEELY: Yeah, they get worse. He drank more, he got meaner, he screwed around, got herpes, gave 'em to me. My dad got shot, Cole wanted to move to Arizona because he knew I'd have to take care of him. Pawned a lot of stuff, got himself a recliner. I'm waitressing, minimum wage, cashier at a car wash, 70 hours minimum, he drinks himself out of his job, real thoughtful, right? The recession came on, we just fought minute to minute anytime we laid eyes on each other, I said I wanted a divorce, he hit me, and I left. I was out of there 1 5 minutes after he hit me . . . I was a crazy, out-of-my-mind lunatic I lived with him all that time. Jesus! What the hell was I thinking of?

DU: It was a marriage, Keely.

KEELY: Yeah. After that, he was all over me. I'd look out the window, he'd be in the back yard. The grocery, the library, when I was hanging up laundry, walk into the same bar when I was on a date. He'd come down to the restaurant, say it was about borrowing money, but he knew I wasn't giving him money, forget that, he just liked me to be scared which is what I figured out. Then it stopped for six months, who knows why, then he came back, sent flowers, left messages, begged me to talk to him for one hour so I invited him over, you know, I thought we could sit down and let go of it. I thought I could take his hand and say we're clear, we're two different people. You know, some dumb ass idea like that. That we could just let it go, you know, be whole and be gone, you know what I mean? So I fixed him dinner, and he brought me this stuffed animal, and we were doing, well, not perfect but all right, and I just touched his arm s6 he would know it was alright, and he locked onto my hand, and I said" let go now," and he started in . . . said he needed. . . pulled me in, you know, hard, and I got a hand in his face, and he . . . he bit down. . . bit down hard, and I . . . I don't know, went nuts . . . bunch of stuff. . . got me down on the floor. . . got me down on the floor and raped me. That's how he caught up with our marriage, that's how he changed. (They sit in silence.)

DU: Change can start anytime.

KEELY: I don't want to talk about it. (A pause.) You believe God sees you?

DU: I do.

KEELY: He sees you now?

DU: I believe he does. (A pause.) Keely? (No answer.) Doctor says you're in as good a fourth month as you can be.

KEELY: Let's give it a rest, okay?

DU: He says that baby is lively. (No response.) Almost time for your birthday. (A pause.)

KEELY: How do you know that?

DU: Now, Keely, that's the least of what I know, and you know it.

KEELY: From my driver's license.

DU: The man says you can have a cake.

KEELY: The man?

DU: The man in charge. (A moment.)

KEELY: If I do what, I can have a cake.

DU: Oh, a few pamphlets.

KEELY: I'm not reading that crap, I mean it. Don't you bring it anywhere near me.

DU: You're not afraid of information, are you, honey?

KEELY: You call that information.

DU: Well, there's facts to it.

KEELY: I'm not having a baby. I'm not having it and have somebody adopt it. I'm not having it and keeping it. It won't be. It won't. (A pause.)

DU: What would you like for your birthday, honey? (Keely looks at her.) Besides that. That's not in my power. (A pause. Will Keely speak?)

KEELY: I would like to get dressed. I never liked being in a nightgown. I don't like my own smell. I know that's crazy. You know how you can smell yourself on your night stuff.

DU: Oh, I can share that. That's something that doesn't get a bit better with age, let me tell you.

KEELY: I want to stand up. I want my hands free, I don't care if it's for ten minutes, one minute. I want to walk into a bathroom. I want a chocolate cake. I want to stand up, not bent over on my birthday.

DU: Oh, honey. We only do this because we don't know what else to do. We can't think what else. . . I don't know, I don't. . . birthdays when they're little, the looks on those faces. . . those little hands. . .

KEELY: Little hands, little faces, you make me sick. . . Jesus, can you listen to yourself? All this crap about babies. You don't care about this baby, you just want it to be your little. . . I don't know. . . your little political something, right, God's little visual aid you can hold up at abortion clinics instead of those pickled miscarriages you usually tote around. . . hold up, Baby Tia, wasn't that the one you had downtown trying to pass it off like it was aborted? I can't believe you don't make yourself sick. . . throw up . . . you make me sick, how do you talk this garbage?

DU: (A moment.) I have that dress you had on . . . something the worse for wear. . . he might let me get it cleaned. . . cleaned for your birthday. (A moment.)

KEELY: I don't hate babies, if that's what you think.

DU: I know that.

KEELY: What the hell is your name? You can. . . you can. . . you can give me that for my birthday. I would like to know what the hell to call you when I talk to you!

DU: Du.

KEELY: What?

DU: I get called Du.

KEELY: Du.

DU: Uh-huh.

KEELY: Du what? Du why? Never mind, forget it . . . I would like to be free for ten minutes on my birthday.

DU: You might have to read some pamphlets.

KEELY: What the hell happened to you, Du? Do you see where we are? Look at this where you got to. Look at me. You used to be a person sometime, right? You look like one. You sound like one. You see the movie Alien where they end up with snakes in their chests? What happened to you?

DU: They tear apart the babies, they poison them with chemicals, and burn them to death with salt solution, they take them out by Caesarean alive and let them die of neglect or strangulation, and then later on, these poor women, they cut their wrists or swallow lye, and then they bring themselves to me because I'm the nurse. Over and over. Over and over. Little hands. Little feet. I've held babies. I've lost babies. I took a baby through six months of chemotherapy and lost that baby. I need to sleep. That's what happened to me.

KEELY: (Almost gently.) I can't raise this baby, Du. I'm so angry and fucked up, I just can't do it. I dream of how it happened over and over all the time. I'd be angry at the baby, I think so. I'd hurt the baby sometime and might not even know it, that could happen. If I had a baby, my first one, and I gave it away, I'd just cry all the time, I would. I'm doing this on empty and, if I did that, I would be past empty and I don't know. I have such black moods, it frightens me. The baby would come out of being chained to a bed, you know what I mean. It's not my baby, it's the people's who made me have it, and I couldn't treat it as my baby, not even if I loved it, I couldn't. He'd come around, see. He wouldn't stay off if I had his baby. He would never, ever in this world leave off me, and I think sometime he'll kill me, that's all I can think. Or hurt the baby, whatever, however in his head he could get me, he would do . . .

would do it. Really. And I can't have his baby. . . uh . . . it's just not something I can do . . . because I'm about this far, you know . . . right up to the edge of it . . . right there. . . right there. (A pause.) So I guess it's me or the baby, so I guess that's crazy, but you don't. . . I don't show you. . . just how. . . how angry I really am. I don't. I don't. (A pause.)

DU: He could have changed, Keely.
```

---

## IC-0606: The Kitchen Witches

- Title: The Kitchen Witches
- Author (byline): Caroline Smith
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Nov 2012
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ISOBEL, DOLLY, DOLLY/ISOBEL, VOICE OVER, ISOBEL/DOLLY
- Teaser before the introduction: Yes
- Spoken words (computed): 1346
- Already set (do not supply): none

### Source block (context only)

```text
Author: Caroline Smith
ISBN: 978-0573632860
Publisher: Samuel French, Inc.
Date (Month/Year): Nov 2012
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Isobel Lomax and Dolly Biddle are two “mature” cable cooking show hostesses who have hated each other for 40 years.

ACTRESS 2: Ever since Larry Biddle dated one and married the other.

ACTRESS 1: Now fate has intervened and put them together on a reality TV show

ACTRESS 2: Hold on to your hats, ladies and gentlemen . . . It’s . . .

TOGETHER: The Kitchen Witches by Caroline Smith
```

### Performance text (classify this)

```text
ISOBEL: (Pg 57) Dolly was my best friend. Yep, we were as close as sisters, Dolly and I, all the time we were growing up. We spent every second together – sat next to each other in school, talked for hours on the phone, had sleep-overs. [Then . . . ] our last year of high school we met Larry Biddle. What a character . . .

ISOBEL (VOICE OVER): (off-stage) (Pg 13-14) Dear Babcha, I have been watching you since the other cooking show was cancelled last month. I was wondering do you know Isobel Lomax, the hostess of “Busy Izzy” and if so, can you get me her recipe for Steak and Kidney Pie?

DOLLY: (in a decidedly fake Russian accent and smiling dangerously into the camera) Hello, Jane dear! Of course I know that person you mention. But you sound like nice lady, so I do nice thing. I don’t get you recipe for Snake and Pygmy pie. But I tell you reasons why Busy Izzy show was cancelled. One. Stupid name. Two. Stupid food. Three. Stupid woman. . . .

ISOBEL: (Pg 14-15) (making her way to the sound stage) Ha! . . . I said ha!

DOLLY: Who is . . . (She gasps) . . . Isobel Lomax! What on earth are you doing here?

ISOBEL: Over the past few weeks I have ben watching this . . show. I thought it time I came down in person and let you know I have had enough of this constant slander. Dolly Biddle, you have publicly insulted me for the last time. You can expect a call from my lawyer on Monday. (starts to leave, then turns) Does your viewing audience know that “Babcha from Ukraine” is really Dorothy Plotznik from Sudbury? (Dolly gasps, pans for the camera and then runs off-stage to her dressing room)

ISOBEL: (Pg 16-17) (Taking over the show) Hello folks – Busy Izzy here! I’ll just fill in for a bit – after all, that’s what bosom buddies are for! Now let’s just clear off our counter and start fresh. (She dumps all of Dolly’s cooking into the garbage can) We’ll start by making Izzy’s Perfect Shortcrust Pastry. (begins preparation) Our friend Babcha is really Dolly Biddle, and she was born, not far, far away in the Ukraine but in beautiful downtown Sudbury! How do I know this? Why we grew up together, Dolly and I!

DOLLY: (Emerging from her dressing room without her accent) What do you think you’re doing?

ISOBEL: She was Dorothy Plotznick. Biddle is her married name . . .

DOLLY: At least I go married! At least I had a husband.

ISOBEL: You know perfectly well I dated Larry Biddle first.

DOLLY: In your dreams! I was going steady with Larry long before you oozed onto the scene! Who did he take to the Senior Prom, huh?

ISOBEL: Well, Larry may have married you, but I was the one who made him happy!

DOLLY: That man was never happy!

ISOBEL: How could he be living with you? (pointing with her ring hand)

DOLLY: What is that? (Isobel holds up her hand, showing off a flashy ring)

ISOBEL: What – this?

DOLLY: That’s . . . that’s the Biddle family heirloom ring!

ISOBEL: Larry gave it to me when we were dating.

DOLLY: He told me he lost it! That ring should be mine!

ISOBEL: You can pry this from my cold, dead hand!

DOLLY: (Picking up a chopping knife) Fine by me! (then notices the cameras are still running) (Pg 19) (resumes her poise and In her Russian accent) Well, it’s been so nice sharing time with you each week, peoples, and Babcha is so sorry to say goodbye. So – everybodys . . . remember to eat good, enjoy life and most important . . wash your hands! This is Babcha . .

ISOBEL: (Butting into the camera range) And Busy Izzy!

DOLLY: Saying goodbye!

ISOBEL: And good cooking! (Both wave to the camera until the audience is “gone” – Then the two glare at each other as a phone rings – Dolly picks it up)

DOLLY: (Pg 21) (Still in a Russian accent) Hello? (to Isobel) It’s the Elm Street Bridge Club . . . (listens) Really? You did? What? (to Isobel as she hangs up the phone) They say that was the funniest show they’ve ever seen, they loved it. (a look of shock from both ladies)

ISOBEL: (Pg 22) On the air again?

DOLLY: Together?

ISOBEL: We can’t share a show – within five minutes one of us would be dead . . .

DOLLY: And the other charged with murder! We’ve hated each other almost forty years!

ISOBEL: Well, it’s a ridiculous idea. I have no intention of continuing to air my personal affairs in public.

DOLLY: (laughing) You’ve always opened your big fat cakehole to anyone who would listen!

ISOBEL: That is an outright lie! I am an extremely private person!

DOLLY: Ha! You’re about as private as Madonna’s cleavage. (Pause as both contemplate a future show together) (Pg 23-24) Let’s try it.

ISOBEL: Count me in! The Izzy and Dolly Show!

DOLLY: You mean the Dolly and Izzy show.

ISOBEL: Why should you get first billing?

DOLLY: It’s always alphabetical.

ISOBEL: (Pouts in frustration then a has an idea) . . . [How about] Kitchen Witches!

DOLLY: Oh, I don’t think you can describe me as a witch . . .

ISOBEL: Unless you spell it with a “B” . . . (Pg 34) “Good morning everyone and welcome to the Kitchen Witches Show.” (shakes her head) That’s pretty bland. (In a “wicked witch” voice) A witchy welcome to one and all!

DOLLY: Oh, that is better – although I think it would be stronger if we both said it!

DOLLY/ISOBEL: A witchy welcome to one and all!

DOLLY: And we could cackle a little . . . (they do)

ISOBEL: And how about if we had a cauldron here on the counter, kind of smoking . . .

DOLLY: Ooo, yes!

**********

VOICE OVER: (Pg 38) (Off-stage - shared lines by both actresses) Your Community Service Station is proud to present the premiere broadcast of . . . The Kitchen Witches! (Jingle - See link for a sample “tune” to use for the jingle at the bottom of this selection or create your own) Let’s turn up the heat and bring this show to a boil With two ladies who mix as well as water and oil! Now here is the twosome who’ll keep you in stitches It’s Isobel and Dolly . . . The Kitchen Witches! (Witch-like cackle)

(Dolly enters in a Scarlett O’Hara inspired hoop skirt, Isobel is off stage)

DOLLY: (in a bad southern accent) Well, I declare, ain’t this just the prettiest audience I’ve evah seen! Today we’ll be doin’ our salute to the Old South, an’ cookin’ up some mighty tasty vittles, like Burnin’ of Atlanta Spare Ribs and somethin’ that I like to call Rhett Butler Ham Steak!

ISOBEL: (Pg 32) (offstage) What the hell is that? I’m not wearing that!

DOLLY: (Pg 37) (In a soft voice to the audience) She won’t have a choice. While she was in the shower, I swiped her clothes. (louder so Isobel can hear) (Pg 38-41) I seem to be missin’ something . . . My deah friend and cooking partner! (Isobel enters dressed as “Mammy.” She is not happy at all) Well, I declare! It’s Mammy! Now, no salute to Southern Cooking would be complete without Mammy’s famous Buttermilk Biscuits. She makes them so good you’ll think you’ve just died and gone to heaven!

ISOBEL: Somebody gonna die and go straight to hell . . . (Shakes it off and tries to make the best of things and adopt a southern accent to match) Give me that bowl – you don’t know nothin’ about birthin’ no biscuits! Go over there and start the chicken!

DOLLY: (Mimes preparing chicken and hums or sings “Shortnin Bread” [see link to this song at the end of the selection] while ISOBEL continues)

ISOBEL: Now it is true that I make the lightest, fluffiest buttermilk biscuits you’ve ever tried. It’s a mighty sticky dough, so make sure you remove valuable jewelry before you start. (Isobel takes off her watch and her heirloom ring and puts the to the side) Now. You just take a half cup of shortening . . . cut into tiny little bits . . . and rub it well into the flour mixture . . . adding a cup of buttermilk . . . until you have a sticky mass of dough . . . (to Dolly) Will you please shut up!!!!!

DOLLY: (continuing with her chicken preparations) Well! Wait ‘til I tell Rhett about this!

ISOBEL: Frankly, my dear, I don’t give a damn!!

DOLLY: Well, I nevah! I’ll thank you to keep a civil tongue in your head and get back to your biscuits, Mammy!

ISOBEL: To hell with the biscuits! I am not your Mammy and I refuse to continue this ridiculous charade! I did not study at the Cordon Blue for four years just to end up on a tacky show, wearing an offensive costume and being made a fool of by some overstuffed Atlanta bell!

DOLLY: (Whisking her marinade) Who are you calling overstuffed?

ISOBEL: Honey, we could fill you with helium and rename you Zeppelin! (Pg 45-47) (notices they are still on air and becomes instantly cheery again) Oh! Is it viewer mail time already?

DOLLY: Time goes to quickly on the show, doesn’t it. Alright! Let’s check our cauldron for viewer mail.

ISOBEL/DOLLY: Hubble bubble, snow and hail
Show us lots of witchy mail!
Toil and trouble, hail and snow,
Tell us what you want to know!
One, two . . . three! (They each pull out a letter)

DOLLY: Would you like to go first, Izzy dear?

ISOBEL: No, dear – after you.

DOLLY: All right. This is a letter from Lucy. She writes

ISOBEL (as Lucy): Dear Kitchen Witches, you have so many interesting recipes – are there any plans for a cookbook? Yours witchily, Lucy M.

DOLLY: Lucy, we have wonderful news for you. We have just signed on with Edibles Publishing. The Kitchen Witches Cookbook is going to be available everywhere by Thanksgiving! (Dolly suddenly winces in pain and holds her stomach – She passes gas loudly)

ISOBEL: (embarrassed) What’s the matter with you? We can discuss the cookbook later.

DOLLY: You bet your ass. . . paragus we will. I just had too much prime rib last night . . . my tummy’s a little unsettled . . . (another great poof of air)

ISOBEL: Great (panning for the camera) I’m working with Emeril LeGassy.

DOLLY: It’ll pass in a minute.

ISOBEL: ell don’t pass it over here! (Dolly continues to struggle and pass gas loudly) Don’t get too close. The woman is powered by methane.

DOLLY: This is all your fault!

ISOBEL: My fault? Nonsense! If you didn’t snack constantly, you wouldn’t have all these digestive upsets! (Pans to the camera again) (Pg 31) It’s hard to soar like an eagle when you work with a turkey.

DOLLY: (escalating quickly – she goes nose-to-nose with Isobel) Who are you calling a turkey, you scrawny-necked buzzard?

ISOBEL: (Pg 39) Why don’t you go take a flying f . . . idle dee-dee! (then realizes they are still on air) (Pg 41) It’s time we admitted that his was a bad idea from the beginning! We were fools to think it could ever work. Sorry to disappoint you folks, but this show has just been cancelled! (Isobel storms off stage)

DOLLY: (Passes gas loudly – an ending exclamation point)
```

---

## IC-0607: Las Hermanas from Parallel Lives

- Title: Las Hermanas from Parallel Lives
- Author (byline): Mo Gaffney and Kathy Najimy
- Work: Parallel Lives
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1993
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MADELINE, SYLVIA, BOTH, HOLLY, MOLLY
- Teaser before the introduction: Yes
- Spoken words (computed): 1334
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mo Gaffney and Kathy Najimi
2003 National Qualifier
Book: Parallel Lives
2007 National Qualifier
ISBN: 978-0822213086
2014 National Qualifier
Publisher: Dramatists Play Service, Inc.
2015 National Qualifier
Date (Month/Year): Jan 1993
2016 National Qualifier
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Let us take you back in time to the early nineties

ACTRESS 2: When the feminist comedy Parallel Lives — written and performed by openly bisexual actors and writers Kathy Najimy and Mo Gaffney — made its debut,

ACTRESS 1: It was the George Bush era . . . . and the political climate was still rather grim for LGBT people.

ACTRESS 2: It was well before there were multiple celebrities “coming out” - Melissa Etheridge . . . Ellen DeGeneres

ACTRESS 1: And lesbian characters and story lines were, for the most part, a rarity on network television and in feature films.

ACTRESS 2: Women were recognizing and naming themselves as feminists and the world was still in shock.

ACTRESS 1: In Las Hermanas -- two senior citizens, Sylvia and Madeline, go on a field trip to an all-natural restaurant with their women’s studies class and experience some unintentionally hilarious lesbian-feminist performance art (“Sister Woman Sister!”).

TOGETHER: Las Hermanas from Parallel Lives by Mo Gaffney and Kathy Najimy
```

### Performance text (classify this)

```text
NOTE: The original script of Parallel Lives was written for two women to play multiple roles. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Lights come up on two sixty-something New Yorkers, Madeline and Sylvia

MADELINE: Is this the place Syvvie?

SYLVIA: I guess so, darling. I don't usually frequent health food places.

MADELINE: Neither do I, don't be smart.

SYLVIA: (Indicating sign.) Oh, here we go: "Las Hermanas."

MADELINE: Oh, that means 'the sisters' in Hispanic. Oh look Syvvie, all the plants and the wicker.

SYLVIA: Oh Mad, look at this floral water color! It's so vibrant.

MADELINE: I love art, oh it's beautiful. Well, do you see anyone here? Hostess? Waitress? Maitre d'?

SYLVIA: Right here. Hello darling.

MADELINE: Oh, hello honey, we're here with the Women's Studies field trip department. Is there a special section we should sit in? We're here to see Holly and Molly sing Sister Woman Sister. We want to sit with our class . . .

SYLVIA: Maybe we should introduce ourselves. I don't mean to interrupt.

MADELINE: I didn't introduce, I'm sorry. You're right, I'm wrong. My name is Madeline Samuels, and this is my best friend in the entire universe, forty three and a half years . . .

SYLVIA: My name is Sylvia Dunleavy, but please call me Syvvie.

MADELINE: We're with the Women's Studies Department junior college extension program. Oh we love it, two years we've been there. Tell her the story, darling, she doesn't know us.

SYLVIA: Well, a couple of years ago Mad and I decided to go back to school.

MADELINE: Single again, why not. . . ?

SYLVIA: We wanted to take a real estate course but it was all filled up.

MADELINE: So what we did was we went down to the registrar's office and we looked through the book, the hibiscus, whatever . . . to see what they had to offer . . .

SYLVIA: We didn't know.

MADELINE: We didn't care. And we see, big as day, Women's Studies, and we think, 'hoho!'

SYLVIA: Hoho!

MADELINE: We've got the prerequisite for this course. At the time we had no idea. Women's Studies we thought it would be a little macramé.

SYLVIA: Maybe some child rearing.

MADELINE: Whip stitching.

BOTH: No very serious courses.

SYLVIA: Our first class was a 'Women in Terrorism' course. It was scary, but I got an A. (Karate stance.) Watch yourself. Oh I wouldn't hurt you, I'm just kidding.

MADELINE: I wasn't good, my favorite was second semester, 'Women and Their Body Temperatures.' I cried in that class. Honey, you learn things you don't want to know.

SYLVIA: Things you wish you could forget.

MADELINE: You can't forget mucus, it just sticks to you.

SYLVIA: Oh, remember our favorite class? "Women in Human Sexuality."

MADELINE: Human sexuality, choices, choices, choices . . . It's a whole new world with the choices nowadays. What with your . . . you know with your . . . your bi-sexist and your lesbanese.

SYLVIA: Don't forget the celebastics who have no sex whatsoever.

MADELINE: Who cares, everybody marches to their own individual drum cycle.

SYLVIA: I'm okay and you're delightful.

MADELINE: Do you know what I always say? I say please do not walk in front of me or at the side of me, walk behind me as my equal. That's all she said. . . You'll find the reservation under Carol Perkins.

SYLVIA: She's our professor and such a genius. She is so smart at least six PhDs maybe more. We love her.

MADELINE: Beautiful, wears the folk skirts, long grey braid, very tan, Indian jewelry . . . Oh? follow her? She must be in a hurry. (They walk over to sit on bench.) These tree stumps must be the seats. Watch out for splinters in your fanny.

SYLVIA: (Sitting.) I feel like I'm a 7 dwarf, what with the tree stumps. Oh, look . . . (Picks up flyer.) "Holly and Molly in 'Sister Woman Sister.'" That's what we're here to see.

MADELINE: Performance art field trip, next week we see the Katie and Mo show or something . . . It's a performance art class.

SYLVIA: Doesn't matter what you do, you get a grade.

MADELINE: Some of the projects those girls do are wild.

SYLVIA: Women. I don't mean to contradict you.

MADELINE: Oh, no, you are right. I'm glad you told me. I'm wrong.

SYLVIA: You're not wrong darling, you got it right on the test so you know it up here. (Points to her head.)

MADELINE: I stand corrected. May I start over? Do overs. Do overs. Some of the projects the 'women' do are wild.

SYLVIA: Tell her about the first project.

MADELINE: Her name was Teria.

SYLVIA: I think it means the wind. So Teria blew in. Just kidding. She comes in wearing nothing but a bikini.

MADELINE: French cut, yellow terry cloth thong. Thongs. You used to wear it on your feet. Now you wear it on your butt!

SYLVIA: Anywho, she has with her a watermelon.

MADELINE: Ripe!

SYLVIA: And I think, delicious! But no, she slices it in half and rubs it all over her body, tip to toe, doesn't miss a spot with the watermelon.

MADELINE: Then, for the piece de resistance, she takes a box of live flies and mosquitoes. True story, and unleashes them on herself. Yes, she did.

SYLVIA: She called it "Summer." It went right over my head. She meant well, she really did.

MADELINE: No, I didn't have a clue. Made me hungry for cantaloupe. The teacher was on her knees weeping. I didn't get it, she got an A+ right off the top.

SYLVIA: Well, what do we know.

MADELINE: Not a thing. Not about art anyway. Well here's the menu decoupaged on that tree trunk up there.

SYLVIA: So crafty.

MADELINE: I'll tell you what, my glasses are better, I'll order for you. What will you have?

SYLVIA: I think I'll have a burger, medium well, with ...

BOTH: Onions.

MADELINE: Miss Onionhead. (Squinting and searching hanging menu.] All right, okay, all right, okay, all right. No, Syvvie, no burgers, no franks.

SYLVIA: No burgers?

MADELINE: Not here.

SYLVIA: Should we be scared?

MADELINE: No, tell you what, We're gonna try the special of the day no matter what it is.

SYLVIA: Okay, we'll be adventurous. We ain't dead yet.

MADELINE: (They crack up.) Oh, look honey, over by the tree trunk, folk skirt. Carol!

SYLVIA: Professor Perkins!!

MADELINE: (To Carol.) Mad and Syvvie. Second period, right on time. Come over and sit with us.

SYLVIA: Oh, she wouldn't sit with us. She'll probably sit with Teria.

MADELINE: No darling, look, she's coming over. The lights are going down, the big sister show is going to start. Shhhhhh . . .

(Actress assume the roles of Holly and Molly who are wearing women’s symbol T-shirts)

HOLLY: Welcome to Las Hermanas. My name is Holly and my partner Molly and I would like to thank the owners of Las Hermanas, Nirvana and Sunshine, for providing us with a chemical-free, meat-free male-free environment.

MOLLY: An environment about women, through women, beyond women, because of women, over women, of women, above women, by women and for women only. We’d like to start with an original tune.

BOTH: (singing) Sister Woman Sister
Mother, daughter me
Sister, you run naked
Wild and so free
You know how to run and jump and laugh and climb a tree
Sister Woman Sister
You are me

MOLLY: And now, in a tribute to Holly Near, Meg Christian, Theresa Troll and Helen Reddy, we’d like to share with you . . .

BOTH: SISTER WOMAN SISTER

HOLLY: Oh sister woman sister, mother goddess, oh goddess, bring me into your fold, your mother loving arms . . . your sister woman motherloving arms.

MOLLY: WOMYN W-O-M-Y-N, pronounced wmyn. Solstice wmyn witch wmyn.

HOLLY: Birth Cycle.

MOLLY: I am born from you and am of you . . of you I am . . .

HOLLY: We give birth. We are birth, we are fetal, we are after birth. My placenta is yours and yours is mine.

MOLLY: So sister. Can I call you sister, or woman of my life, or just me? Are you me? Are we we?

HOLLY: Oh, live in the great uterus of woman. Live in the walls. Cut the umbilical cord.

BOTH: No! Don’t!

HOLLY: It is there.

BOTH: Cord cut cut cord no don’t!

HOLLY: It is there.

BOTH: Woman woman woman woman womn womn wom wom wom WOMB!

MOLLY: Womb, womb, we are two evolving around into oneness. Spinning, spinning, spinning . . . spinning.

HOLLY: Oh, labia. Oh golden labia of goddess love. So let your champagne flow.

MOLLY: Like blook, like spit, like rain, like wet, wet woman, woman, wet. They both start with a W. We are the lioness, we are the tigress, we are THE TEAMSTERS.

HOLLY: Sisters, sisters Betty and Wilma . . .

MOLLY: No Fred, no Barney.

BOTH (alternating): I / have / my / own / I / den / tit / y / I / have / my / own I/ den / tit / y.

MOLLY: I have my own identity, I have my own identity.
```

---

## IC-0608: The Last Nickel

- Title: The Last Nickel
- Author (byline): Jane Shepard
- Work: Kick Ass Plays for Women: Four Short Plays
- Publisher: Samuel French, Inc.
- Publication date as stated: Nov 2008
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JO, JAMIE, BOTH, MOOSE, TIM, DOCTOR, NURSE
- Teaser before the introduction: Yes
- Spoken words (computed): 1722
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jane Shepard
Book: Kick Ass Plays for Women: Four Short Plays
ISBN: 978-0573663437
Publisher: Samuel French, Inc.
Date (Month/Year): Nov 2008
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 2: (looks to see that JO is gone then fills the audience in) The Last Nickel by Jane

Shepard (Hears JO returning, so feigns sleep once again.)
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters (in the form of sock puppets). In the original script, additional actors were used for the puppet roles; however in this cutting, JAMIE and JO are the puppeteers. Portraying multiple characters is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

(SETTING: JAMIE'S BEDROOM, night, lights dim. AT RISE: JAMIE is asleep in bed. JO appears at the doorway)

JO: Jamie. (No response.) Woo-hoo. (Nothing.) Jamie, wake up. The house is on fire. (JAMIE sleeps on.) Ssssssst. Jamie, your bladder is full. If you don't wake up now you're gonna wet the bed. (Makes NOISES: raspberries, farts, etc. then jumps on bed, singing.) "I'm a little tea pot short & stout.” (JAMIE simply turns over.) Tsk. (JO gives up, goes to the door, lingers a moment, EXITS.)

(JO ENTERS with TROMBONE.) "Ode to Jamie." (SHE PLAYS loudly JAMIE jumps, snapping on bedside lamp.)

JAMIE: Alright alright alright, stop it! Jo! (JO stops.) It's Tuesday. I have to work tomorrow. I'm not doing this tonight. (JO toots.) Jo! (JO lowers the trombone.)

JO: But it's cute! Do you think a tuba would be funnier? Just the word: "tuba." Plosives are funny.

JAMIE: I'm not doing this.

JO: "Tuba," tell me you don't think that's funny. Anything with P's or T's. Pee-pee poodles!

JAMIE: God!

JO: Puppy! No poo-poo in the tuba!

JAMIE: We agreed you weren't going to do this anymore. 1

JO: You decided, technically that is not an agreement. . . . [besides] I'm lonely.

JAMIE: I know. And I'm sorry. But I am too, kid, everybody's alone, that's the way it is. Except for a few good years here & there, when you get a brief respite, but on the whole you know as well as I do, "You are the only person --

BOTH: -- With whom you will live your entire life."

JAMIE: You're a good sister, I love you, go in peace (JAMIE turns off the light and lays back down. JO sinks down against the wall.)

JO: (Quietly) The planet Jupiter is 40 million miles away. They talk about visiting other planets, but it's 40 million miles. If we sent someone right now, it wouldn't even arrive until 2,038. And for them to get back, it would take until they were 90 years old. If they ever got back at all.

(JAMIE sighs loudly.) I'm talking quietly. (JAMIE turns on light and pulls box of CRACKERS from under bed.) Oh. Hungry?

JAMIE: You're acting like a bratty little sister.

JO: Yep.

JAMIE: I love you very much.

JO: Can I get in bed?

JAMIE: No.

JO: Wish I had a snack.

JAMIE: Can't help you there.

JO: Nobody loves me, everybody hates me, I'm gonna go eat worms. (JAMIE pulls a bottle of YOOHOO chocolate drink from under the bed and drinks it off.) Wish I had a Yoo-Hoo .... (Funny voice) "Yoo-Hoo! Where are you?

JAMIE: What do you want, Jo?

JO: Don't get all huffy-serious. If you get all huffy-serious you'll never get back to sleep.

JAMIE: I am gonna get back to sleep! Because I've got a damn day tomorrow. I took a sleeping pill, I had a snack, I'm not thirsty, and I deserve to rest! I did everything right today! I worked hard, I waited 'till I was tired, and I was asleep! Godammit, I have to take care of myself now, Jo! I know this is hard for you. I know you can't rest! But I can't help you. I've tried! I sit up with you, I calm you, I listen, we party, we cry! It makes no difference! I can't resolve this for you.

JO: You're my sister. I'm not trying to take over your life, I'm just having a hard time right now.

2 Who am I supposed to turn to?

JAMIE: I don't know. God.

JO: God! God doesn't answer questions on how to deal with death. It's policy... "Um, God, about death?" (As God) "Shh, Can't talk about it!" (Self) But, God -- God? Hello? Are you listening! (God) "What?! I gave you the 10 commandments, what more do you want!" (Self) Well, I honor my mother and father & I don't pray to idols, how does this help me with the death thing?-- (God) "Look! You're just an individual, I'm omnipotent, it's busy! I don't have time to deal with every little question you have, think about it, you'll figure it out! (Sits on JAMIE’s bed) Think 'till you're pale and you've got big rings under your eyes. Think 'till you're living on crackers and chocolate drink--

JAMIE: Get off my bed.

JO: If you think about it 'till you're living death, and breathing death --

JAMIE: Now! (JO moves off the bed.)

JO: -- Then maybe you'll get it, white girl.

JAMIE: Up yours. (JAMIE shuts off the light, throws the crackers across the room, and lays down.)

JO: I just want to talk --

JAMIE: We talked. You can't deal with it and neither can I. Goodnight. (JO leave scene, but returns with two hand puppets, she crawls up behind the bed as JAMIE prays) Thank you, God! (Tries to settle herself, more genuinely) Thank you for the quiet. Thank you for this beautiful day. Thank you for helping me to continue on. Please let her get through this, I'm asking you, for my sake and hers, just please let her shut the hell up! In your name I ask this. Um ... Amen.

(She turns over. Silence. Two children's HAND PUPPETS pop up from behind her bed: A MOOSE & a stupid PIG. JO speaks for them both in big cartoony voices, like announcers in a bizarre game show.)

MOOSE: Odd man! She said it first, Tim, ooooodd man!

TlM: {Snorts.}

JAMIE: Oh, no ...

MOOSE: It's that time again!

TIM: {Snorts.}

3

JAMIE: No no no!

MOOSE: What's that ya say, Tim? What time is it? liiiit's puppet time!

TIM: {Squeal!}

JAMIE: I hate the puppets!

TIM: Time for another nightly sojourn into the land that time forgot! (PUPPETS cheer)

JAMIE: We're not doing the puppets! Not tonight!

MOOSE: It's Jamie time! And odd man to that! Tim, do you remember the time Jo was taught to pray in kindergarten? It was the first time she every prayed.

TIM: {Snorts.}

MOOSE: And the teacher said, "Students, here is how we pray: 'Now we thank you for this food, amen!'"

JAMIE: I'm not listening to this.

MOOSE: And Jo said it, but she just had to wonder, Tim, why did we say 'odd man' at the end? So she went to ask her big sister! Jamie's almost eight so she'll know! (JAMIE pushes THEM down.)

JAMIE: Shut up and stop it, you stupid idiots! (THEY pop back up.)

MOOSE: And do you remember what Jamie said, Tim? It's so cute. "Well," says Jamie, "I don't know why we say 'odd man.' Maybe men are just odd!" (PUPPETS laugh and squeal uproariously. JAMIE tries to grab them)

JAMIE: It's not funny any more! We didn't know how to pray, so what! (SHE catches TIM and throws him to the ground.)

JO: Aw, you killed Tim.

JAMIE: I hate the puppets. (JAMIE faces the chair away from them) Lemme know when you're done. (long pause as JO plays with the Moose Puppet) I can sit here all night. . . go away.

JO: What will you give me?

JAMIE: Uh! God! What do you want? (JO smiles and takes the Moose Puppet off her hand and drops it to the floor)

JO: Got a nickel?

JAMIE: What?

JO: "You always have a nickel ... "

JAMIE: (Smiling) Oh man. I can't believe you remember these things.

4

JO: (In voice) "You always have a nickel ... "

BOTH: " .. If you imagine that you do."

JAMIE: How do you even come up with that? I haven't thought of that in years. (JO holds out cupped hands.}

JO: Pick a nickel.

JAMIE: If I do, will you let me go to bed? Okay, okay. (JAMIE reaches for a nickel.)

JO: Just one.

JAMIE: "One is all you need." (SHE picks an imaginary nickel out of JO's hands, holds it up, ready to flip it.) Heads it's ... "Good Vibrations"!

JO: Tails it's ... "Wipeout"!

JAMIE: (Stopping) Not "Wipeout".

JO: Why?

JAMIE: I played it at the hospital.

JO: Really? (JAMIE nods.) I didn't know that.

JAMIE: Come on, come on, pick something else.

JO: Ooookay, ladies & gentlemen, tails it's ... "To Sir With Love"! (JAMIE flips the imaginary coin. As soon as SHE uncovers it, JO shouts.) "To Sir With Love!" I called it! Now put it in! Put it in, let's go! E-2. "To Sir With Love" is E-2. (THEY come together at an imaginary JUKEBOX.)

JAMIE: We never had an E-2.

JO: E-2. (JAMIE pushes invisible SELECTION BUTTONS. JO launches into lip-synch & dance. The choreography is effortless, executed with the familiarity of hours of childhood repetition. THEY eventually lose themselves in it, laughing & hamming it up. *See reference at the end of this selection) "The time has come For closing books And long last looks must end!" (Hands JAMIE imaginary mic.)

JAMIE: "And as I leave I know that I am Leaving my best friend."

BOTH: "A friend who taught me right from wrong And weak from strong, That's a lot to learn. What can I give you in return? If you wanted the moon I would try to make a start But I Would rather you let me give my heart. To Sir, with love." (As the SONG ENDS Jaimie wipes tears from her eyes)

5

JAMIE: The song made me sad.

JO: (Sings softly) "And as I go I know that I am leaving my best friend ... "

JAMIE: I don't want you to ever leave me. I have fun with you. Even in the middle of the night when you wake me up & I'm crabby, you can still make me feel better than anyone else. Like a person again. And I just ... don't feel it that much these days.

JO: Who put the glue in mom's shoes? (THEY laugh.)

JAMIE: Who thought it up?

JO: Who actually did it?

JAMIE: Who stapled dad's shirt sleeves closed?

JO: Who ran away from home and took his charge card?

JO: Who did Nickel in a Jukebox? You could always cheer me up.

JAMIE: Yeah, I could.

JO: That's why you played it?

JAMIE: What?

JO: "Wipeout." At the hospital. Did you sing?

JAMIE: Don't bring me down, okay? You got me feeling good, I thought that was the point.

JO: Is that the point? (JO holds out her hand.) Wanna nickel?

JAMIE: No. Ah. Yes, I sang, I thought it would cheer you up.

JO: The whole thing, choreography too?

JAMIE: Not at first. You were in a coma. What could you see?

JO: Coma with my eyes closed?

JAMIE: Coma with your eyes half open, glazed. But then I did.

JO: You did?! The whole act?

JAMIE: I thought you might respond. I sang and danced around the room. Well limped around the room, I had this cast on my ankle and this crutch. And the nurse came in and turned the tape off and told me to stop it, it was making the numbers on your blood pressure thing go up. That's all, period, no more.

JO: You brought it up. . . I am tired, Jamie.

JAMIE: No! No, you certainly are not! (JAMIE's turn to bug Jo.) You're the energetic one, the crazy character of the family! I was the wimp.

6

JO: You lived.

JAMIE: Oh, hah! You call this living?! Aach! This is not living! (Holds out her hand to JO.) Pick a nickel!

JO: What're you gonna do?

JAMIE: I've been thinking of jumping out the window. (JO & JAMIE stare, nickel held between them.) Nothing near so bad as happened to you.

JO: I didn't feel it.

JAMIE: That's not how you looked under the car. I don't wanna talk about it!

JO: Okay. (JO lifts the nickel.) It's my last nickel. (SOUND of NICKEL dropping in slot.)

JAMIE: No! (JAMIE lunges to stop her from playing the song Wipeout, but JO clicks the jukebox BUTTONS) I swear, I'll cut my wrists! (JAMIE digs madly in the nightstand) I have a knife! DON'T! (JO’s body starts to seize then grows still) (Jamie picks up the puppets and puts on the following show, with the puppets as the doctor and the nurse. JO hums “Wipeout” in the background. *See reference at the end of this selection) *******

DOCTOR: Do we have a pulse?

NURSE: No pulse.

DOCTOR: Recharge the paddles. What the hell happened, she was stable! Somebody give me a count!

NURSE: Five minutes.

DOCTOR: She's not responding! Is there any next of kin?

NURSE: There's a sister.

DOCTOR: There's no air coming through!

NURSE: Code red. We have code red!

DOCTOR: Oh my God, who stopped the respirator! Jesus Christ, who cut the -- (JAMIE drops the puppets and instead now has a severed RESPIRATOR TUBE in her hand. JO stops the music . . . . Silence.) *******

JAMIE: ME! ME! I DID IT, OKAY? l'M NOT SORRY AND WE ALL KNOW IT! (JO's body remains lifeless.) I cut your respirator and you'd have done the same for me, if you'd seen yourself, with your face all bloated and your brain coming out the back of your head. (JAMIE gently pushes JO’s eyes closed.) My sister Jo, irreversibly, irrevocably brain dead. When they said you were in a

7 vegetative state, I just wanted you to jump up and say, "What, Pennsylvania parsnips?" P-word. Plosives are funny. (SHE strokes her forehead.) There wasn't a goddamn doubt in me, the last thing you'd want was to lie there with empty eyes and have mom & dad watch you shrivel up. Jesus! All I had to do was picture you pinned under the car, and cut it. . . . (JO remains dead.) When that was the only thing holding you from freedom, it didn't seem like much. I thought it would cut you loose. (SHE sinks down by the bed, still clutching the cut tube.) The planet Jupiter is 44 million miles away. If you sent someone from earth they wouldn't even arrive until 2,038. And for them to get back, it would take until they were 90 years old. If they ever got back at all . . . . (JAMIE begins to cry) It's a lonely place, Jo . . . I don't think I can do it anymore . . .
```

---

## IC-0609: Letters to a Student Revolutionary

- Title: Letters to a Student Revolutionary
- Author (byline): Elizabeth Wong
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: Jan 1996
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BIBI, KAREN AS CHORUS, KAREN, BOSS, BIBI AS CHORUS, SOLDIER, ACTRESS 1, ACTRESS 2
- Teaser before the introduction: Yes
- Spoken words (computed): 2581
- Already set (do not supply): none

### Source block (context only)

```text
Author: Elizabeth Wong
ISBN: 978-0871296450
Publisher: Dramatic Publishing
Date (Month/Year): Jan 1996
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Two young women . . . worlds apart in culture forge a friendship that lasts throughout the years.

ACTRESS 2: Who would have guessed that a chance meeting would lead to a long-distance bond that in a very small way could bring the cultures of Asia and the U.S. to a greater understanding of one another.

TOGETHER: Letters to a Student Revolutionary by Elizabeth Wong
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actress 1: Bibi, Boss, Soldier and some Chorus

Actress 2: Karen and some Chorus

BIBI: (to audience). I was touring China with Mom and Dad. I took to the streets of Beijing. Wandered into Tiananmen Square-a hungry look in my eyes, a vain hope in my heart. No place is truly civilized without Mickey D and a drive-up window.

KAREN AS CHORUS: (to audience). Summer 1979. Tourism was still so new in China.

KAREN: (enters, pushing an old coaster bicycle -- to audience). I am on my way home from the factory. End of the graveyard shift. It is already hot like hell. Do I say that right? Yes, I think so. What harm is there to practice a little English?

BIBI: (to audience). Oh look. Grandmothers with ancient faces, pushing bamboo strollers like shopping carts. (She peeks into the strollers.) Ahhhhh, sweetest little babies with wispy, fuzzy, spiky hair.

KAREN: (to audience). I will go up to her and speak to her. We will make beautiful sentences together.

KAREN: Hello.

BIBI: Oh, hello.

KAREN: Please. Not so loud. (Beat.) Are you?

BIBI: (whispers). I am. How can you tell?

KAREN: Ahh. (Pause.) Your hair.

BIBI: Completely unnatural, I know. It's called a permanent. Every time I go to the salon, they want to give me the same old, tired thing-the classic bob and bangs, exactly like yours. They tell me, "You look so cute. A little China doll, that's what you are." So I say, "Aldo, baby darling, perm it. Wave it. Frizz it. Spike it. Color it blue." It's unusual, don't you think?

KAREN: (starts to touch BIBI’s sleeve; then withdraws shyly). Here we have only a few colors. Grey and blue and green. May I ask what is your name?

BIBI: Bibi. My name is Bibi. (They reach to shake hands. but before they touch, BIBI and KAREN freeze. (to audience). Our conversation lasted about two, three minutes, tops. (The two women move away from each other. BIBI shouts.) That's Los Angeles, California. U.S.A. 90026. Can you remember all of that?

KAREN: (nods vigorously. To self). Yes, I will remember.

BIBI: (to audience). She didn't even tell me her name.

KAREN AS CHORUS: Bibi went back home to California, U.S.A. And that was the beginning of a most uncomfortable correspondence.

KAREN: (writes). Summer, 1979. My dear American friend ... (Scratches out, starts again.) My dear new friend. Greetings from Beijing. (KAREN sits back, stares into space.) . . . I met you in Tiananmen Square. It is a happy feeling I have . . . to have you for a secret friend, a special friend. I have much stupidity since I realized I never told you my name.

BIBI: (to KAREN). Karen? Karen is a good name.

KAREN: (To audience.) I chose my new name in secret. Where you live, you can be open about such matters. But here we must do everything in secret. Bibi, you have such freedom. I have no freedom. None whatsoever. I was meant to be born in the United States, to live in freedom like you. Do you understand? (Beat.) Two days after I met you, my boss at the factory where I am in the accounting department, asked to speak to me. I am taken to a small room in the basement. This is not a good sign.

BOSS: (kindly, as if to an errant child). You were seen talking to an American. Now, don't be afraid. You may talk to Westerners now. But you must not listen to what they say. You must not get any ideas. (Recites by rote.) Good citizens have only ideas that also belong to The State. The State is your mother. The State is your father. The State is more than your mother or your father. Do you understand?

KAREN: I said, "Yes." But in my heart, I do not understand. I have never understood why I cannot speak my opinions. (Resignedly.) But this is China. (Beat.) I think, Bibi, I want to be having freedom like you. Perhaps you, Bibi, will pay $10,000 for my airplane ticket and my living in California. I will work and work and work and pay you back. I look forward to your favorable response. Your friend, Karen.

BIBI: She's nothing to me and I'm nothing to her. I could care less. I'm not political. And I resent that she is trying to make me responsible for her freedom. I'm barely responsible for my own. (Beat.) January, 1980. Dear Karen, I am so sorry it's taken me nearly six months to write you back. (To audience, resolutely.) I would have answered you sooner, but I was unsure about how to respond to your letter . . . Karen. I don't know what possessed me. But two months ago, I did go to the office of the Immigration and Naturalization Service.

KAREN: Bibi, did you talk about me? Will you help me, Bibi?

BIBI: Karen, the government told me I was not a suitable sponsor. To be a sponsor, I have to prove I can support you as well as myself. Karen, I'm just starting out in life. I don't have much in the way of money.

KAREN: So when you are rich, you can sponsor me, yes?

BIBI: Karen, I really don't think I can do more. I mean, I don't even know you. I'm sorry. Sincerely, Bibi.

KAREN AS CHORUS: Karen continued to write to Bibi. Long letters about her life in China. Her longings for America. [She] would bring up the subject every now and then. Bibi tried to ignore [it], but finally got fed up.

BIBI: Winter, 1980. Dear Karen, You may ask me if you wish. But please do not bring my parents into this. They are not rich. The streets here are not paved with gold. They are paved with concrete, sweat, hard work and struggle. My mother and father struggle every day.

KAREN: Spring, 1981 . . . You asked about my mother. My mother is dead.

BIBI: When did she die?

KAREN: When I was very young. Near my house, next to the pig pen, there is a rice field. (Pause.) My mother is in the field. I see her. (Waves.) MaMa! "Bao Bao gay ni dai fan lail" [Your baby brings you your lunch.] (Beat.) Wait! Who is that? It is the commissaire! -- the man who reports everything.

BIBI: I see him.

KAREN: He is shaking my mother. Why is he doing that? Where is he taking her? MaMa! MaMa! (Pause.) I just watched my mother as they took her away.

BIBI: I'm sorry.

KAREN: The cat eats the mouse. He doesn't apologize for doing what is in his nature to do. She was punished. Not for stealing, but for resisting. If the mouse struggles, the cat grips tighter, first with one paw, then with two. The only thing the mouse can do is escape, run away. As fast as you can. If you can. Public execution is part of our daily lives, part of our education process.

BIBI AS CHORUS: Bibi and Karen continued their correspondence, but sporadically. About once or twice a year.

BIBI: (to audience). Fall, 1986. Mmmm. (Beat.) You know what, Karen? Sometimes, I wish someone would tell me: This is what you are good at, Bibi, so go and do it. This is the man who is good for you, Bibi, marry him.

KAREN: You wouldn't listen anyway, and you know it.

BIBI: No, I probably wouldn't. (To KAREN.) How is . . . ?

KAREN: Lu Yan? Lu Yan is the only guy I've ever . . . how you say? . . .

BIBI: Slept with?

KAREN: No . . . he is the first man I ever dated. Not much choice here in China, even though we are very many millions of people.

BIBI: Choice! Talk about choice. Shall I regale you with tales from the darkside? Dates from hell? By my calculations, I would say I've met a total of, or had a disastrous dinner or ahem, et cetera, et cetera, with at least 127 men of assorted shapes and sizes and denominations. And colors. Don't forget colors.

KAREN: I am getting married during the Mid-Autumn Festival. I'm not sure I want to be married . . . I want to do and see so much, but my world is so small.

BIBI: Here in America, we are free, free to choose our lovers and make our own mistakes. The most wonderful thing about freedom, Karen, is you get plenty of rope with which to hang yourself. Wait! Did you say getting married? How wonderful. It is wonderful, right?

BIBI AS CHORUS: Lu Yan and Karen were married in the fall of 1986. Karen's father and brother gave as a dowry to Lu Yan's family, two live chickens, eight kilos of pig's intestines, 500 steamed buns, a sea lion bicycle, 20 kilos of fish, and 10 cartons of American cigarettes.

KAREN: Winter, 1987. Dear Bibi, Lu Yan is always telling me what to do. Married life isn't what I thought. His mother tells me how to wash his shirts, how to make a dinner. She complains I do not concentrate, as my head is always spinning in the clouds. I do not know who I am.

BIBI: Spring, 1988. Dear Karen, I have changed newspapers five times in the past three years. It's easier to move up by moving out, but I'm getting a little tired of moving around. West Coast, East Coast. No place feels like home. Home doesn't even feel like home. Everywhere I go, I ask myself the question, "Who am I?" "How do I fit in?" The answer changes as fast as my address.

KAREN: Summer, 1988. Dear Bibi, I am a flower that will never open, never to be kissed by a bee. I want to open. I want to feel the sting of freedom. More and more, I feel bitter towards my life and my uselessness. I go to work, I have ideas to improve my job, and no one listens to me. I am a nobody. And I want to be a somebody.

BIBI: (to KAREN). Do you realize, Karen, we've been friends for almost ten years?

KAREN: And for ten years, you have not listened to one word I have said. I thought my marriage would make a solution, but it doesn't. It is not what I wanted for my life. Bibi, you know my heart. But you won't help me. I want to count for something. I can count for something in California.

BIBI: (sincerely). Here or there, your struggle is my struggle. No matter where we are, the struggle is the same. I'm trying not to run away from my problems. Why can't you be happy where you are?

KAREN: Why can't you? You live in a democracy, the individual can vote. You can count for something.

BIBI: What elementary school book did you read that from? My vote counts?

KAREN: That's right. You have the luxury to be selfish. To think of only yourself. You live in Paradise, and I live in hell.

BIBI: Well, Karen, it can be hell living in Paradise.

KAREN: (ignoring). I want democracy. Democracy for me. Freedom of speech. Freedom to chose. (Short pause.)

BIBI: Freedom to be confused. (Beat.)

KAREN: At least you have incentives to strive for a better life. But here whether I work one hour or ten hours, it's all the same. You just don't know what it's like.

BIBI: Can I help it if good ideals are polluted by extremists and dictators? Health care for everybody. Jobs for everybody. Everyone EQUAL under the law. Everyone working towards the greater good. And here's a novel concept people actually caring about the well-being of other people. In America, we call that welfare, and anyone on it is seen as a slackard and a mooch. In China, it's called social responsibility.

KAREN: If you think China is so good, you should come and live here. Bibi, I think you must be a communist at heart.

BIBI: Karen, I just can't afford anything right now. I'm unemployed-again. I quit. And I'm glad I did. I had names, addresses, quotes. And the paper wouldn't print it. We're having an election here, Karen, and an African-American is on the ballot. Quote, "I'd never put a black man in office." Quote: "No negro is going to run this country." Next morning, I read the paper, the quotes are gone. So, I storm into the managing editor's office during a budget meeting. Everybody was there. I said, "Hey what is this?" Why are you sanitizing the news, making it all pretty and clean for public consumption? I strenuously object. I have been so naive. So, in short, Karen, I quit.

KAREN: How lucky you are. You get to live your own life, your way.

BIBI: Sure I'm lucky. I get to fight my battles alone and unsupported, at work and at home. I'm a lone wolf howling, and no one listens.

KAREN: Bibi, I have been thinking about what you say about America. And I think you are right. You see, Bibi, my country is changing and I have a new hope for a better life. And, I no longer wish to come to be an American like you. (Beat.) But I will always be your friend . . . (to audience). May, 1989. Dear Bibi, Here I am sitting in a tent in Tiananmen Square. For the first time in my life, I believe I can be a somebody, I believe my contribution will make a difference. I believe freedom will not grow out of theory but out of ourselves. We are fighting for a system that will respect the individual. The government must listen to us. All we want is a dialogue. A conversation. We want an end to censorship. We want an end to corruption. We are the voices of tomorrow. And our voices will be heard.

BIBI: May, 1989. Dear Karen, I've been watching the television reports. Everybody always asks me how I feel about what is happening in China. I'm so envious of your power-of how you have caused your government, caused the world to take notice. But I am also concerned about your naiveté in striving towards a foreign ideal. I do believe change will come, but it must be at your own pace. I am not sure America is the proper model for the new China that you want. Perhaps you should look to make a Chinese democracy. Karen, are you listening? Because right now, I think that to be a somebody in China is suicide. I don't mean to dampen your spirits, but I am worried. Please, please be careful.

KAREN: We are lying on the floor. Students on a hunger strike. Most of us are women. We haven't eaten in days, and I will not until I have my freedom. A clean division between what we want and what the government stands for. A clear break. On June 4, 1989.

Tanks, armored personnel carriers and trucks full of troops marched into Tiananmen Square. Many of us linked arms, and tried to stand in their way.

SOLDIER: Be a good Chinese and go home. Go home and save your life. This is China. This is not the West. Be a good Chinese and go home.

KAREN: Tanks marched forward and crushed the first row. We marched forward. Run! Get out of the way. Run! Blood everywhere.

SOLDIER: Soldiers, forward. Students, comrades! Be good Chinese and go home. This is China. This is not the West.

KAREN: The statue fell. Everyone was running. (screams). You animals! (lights out.)

TRANSITION

ACTRESS 1: This year, *Insert Year*, is the ______ anniversary of the Tiananmen Square protests.

ACTRESS 2: And even today, the Chinese government continues to detain suspected activists and take measures to censor any mention of the event on the Internet.

BIBI: On that day, as I watched the news, as world events marched into my living room. For the first time in my life, I knew . . . I felt . . . Chinese. And as days passed, I searched my TV set, changing channels, looking for news reports. Nothing, nothing coming out of China. Just a black curtain of silence.

KAREN AS CHORUS: Statistics on the death toll have been confusing. The Chinese Government says less than 400 people were killed, and only 23 of them were students.

BIBI AS CHORUS: But according to unofficial reports, at least 5,000 died, and at least 30,000 people were reportedly injured.

KAREN AS CHORUS: And China has begun a policy of selective historical amnesia.

BIBI AS CHORUS: And America has resumed its habit of selective historical amnesia.
```

---

## IC-0610: Light

- Title: Light
- Author (byline): Jeni Mahoney
- Work: The Best American Short Plays 2007-2008
- Publisher: Applause Books
- Publication date as stated: July 2009
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ABBY, HELENA
- Teaser before the introduction: No
- Spoken words (computed): 2089
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jeni Mahoney
Book: The Best American Short Plays 2007-2008
ISBN: 978-1557837509
Publisher: Applause Books
Date (Month/Year): July 2009
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Most people only think about cults when they capture the front page, usually when people die or when someone close to us has been affected.

ACTRESS 2: Maybe you can remember the 39 members of Heaven’s Gate. Or further back with the Jim Jones tragedy when over 900 people who followed their leader and committed suicide.

ACTRESS 1: We often believe it happens to others and it can’t happen to me or my family and friends. This has proven to not be so.

ACTRESS 2: The type of people who join cults are typicallyno different than the vast majority of society. Some have been experiencing a time of stressful transition or a temporary crisis.

ACTRESS 1: Such is the case in Jeni Mahoney’s short play Light

[At rise: Two women sit facing each other: One is "giving light" to the other. Helena (giving light) is intensely involved; eyes closed and hands poised, palms out. Abby (getting light) stares strangely at Helena not sure what to make of it. They sit this way for about fifteen seconds. A stack of booklets sits near Helena’s feet.]
```

### Performance text (classify this)

```text
ABBY: Is it working?

HELENA: Shhhhh ... [Ten more seconds of silent light-giving.]

ABBY: I don't feel anything ...

HELENA: Shhhhhhl

ABBY: Helena - [Helena drops her hand in disgust.]

HELENA: Geez! Of course you can't feel it. You're thinking about it too much. You're blocking the light with your negative, doubting attitude.

ABBY: I was just checking in.

HELENA: You don't need to check in.

ABBY: I mean, I was sitting there for a good five ... six minutes and I was just wondering if everything was okay. I mean, maybe you could feel if it wasn't going right.

HELENA: I can only give the light. I can't tell if you're receiving it.

ABBY: Oh. [Abby considers this.] How do I know if I'm getting the light?

HELENA: You have to be ready for the light to penetrate you. Otherwise it just bounces right off you-

ABBY: Uh-huh.

HELENA: In fact, I probably shouldn't even be giving you light. It can be dangerous if you're not ready for it. That's what happens when someone spontaneously combusts.

ABBY: [Amused.] Spontaneously combusts?

HELENA: It happens more than you think.

ABBY: Spontaneous combustion?

HELENA: Sure. They try to explain everything like it's something else like it's all so easy. Like it's science. There are forces-in the government and politics and stuff-that want to take away all the mysteries of the world. Like in Sunday school they tell you to "dwell on the mystery," but at the same time they try to explain it all with logic and rationalizations. They present evidence as if evidence creates truth. But evidence-empirical evidence-is a trap. Like Dac says: a demon in sheep's clothing.

ABBY: Oh.

HELENA: I know it sounds weird, and I don't say it too well yet, but when I'm there and Dac is talking-it all makes sense. When you hear him talking, it's all so common-sense it makes you feel stupid that you never thought of it before.

ABBY: Hel, you know I support you in whatever you do ...

HELENA: I know, I know -

ABBY: And I know you've been searching ...

HELENA: Everyone is searching.

ABBY: Yeah, but some more than others.

HELENA: It's the best thing in my life.

ABBY: [Cautiously.] It's the only thing in your life ...

HELENA: Dac says that when you commit to God it's all or nothing. Like marriage. You give everything-your heart, your soul, your emotions, your labor and the fruit of your labor-or it's worthless. It's hard, but it's supposed to be hard. If it were easy, then everybody would do it. You have to give up something - sacrifice something-in order to be chosen.

ABBY: Yeah, but who decides when you're chosen?

HELENA: God.

ABBY: But then how do you know ... ? When you're chosen, I mean ...

HELENA: You just do-Dac says it's like re-emerging from the womb. You have to breathe a whole new way. Everything is different, but it's also suddenly the most natural thing in the world.

ABBY: Dac. What is that? Is that a name? It sounds like an e-mail address, or a Pez candy or something.

HELENA: They're initials. Dac says the Judeo-Christian names that we use are tying us to worn-out mythology-superstitions that we no longer need-that are holding us back and imposing these fascist personae on us-and we put that out into the universe without even knowing it. Like Abby ... Abigail. Like The Scarlet Letter.

ABBY: What?

HELENA: A marked woman, Abby, an adulteress ... and now it's forced its agenda on your life.

ABBY: You didn't even read The Scarlet Letter-

HELENA: But I don't have to-that's the point. We all know what happens in the story.

And I know what happened with you and Jake-

ABBY: The situations are so totally different-

HELENA: I'm not judging you. I'm just saying that when your identity is controlled by your name, then you're *controlled* by destiny.

ABBY: I'm sure there are plenty of women named Mary who get divorced and-I don't know-people named for saints-they screw up too you know ...

HELENA: Oh, sure. Lots of Biblical characters *messed* around. Check it out. I'm not making it up.

ABBY: I'm sure you're not, but with all due respect-which is probably more respect than it deserves-I don't buy it. I'm not being controlled by a very boring work of fiction.

HELENA: It's as real as anything else, you know, by association. It's a cultural myth-it's all fiction really and we collectively-not you Abigail the smart individual-control that. It's like a wave-you know-you can't outrun it.

ABBY: I can't believe we're even having this conversation.

HELENA: I'm just trying to answer your question.

ABBY: Really? Geez, I don't even remember what the question was.

HELENA: The name thing. Dac. He encourages us to create new identities that express our new lives-free from "oppressive cultural fictions" -open to change, rebirth, divine intervention. Dac means everything and no-thing. Whatever you can create: Delicate. Angelic. Creator.

ABBY: Deadly. Amoral. Con-Artist

HELENA: Dreamlike, Alternative, Captain.

ABBY: Deceitful. Arrogant. Cash-man.

HELENA: Divine, Alien, Communicator.

ABBY: Divine Alien Communicator?

HELENA: Just an example.

ABBY: And who are you?

HELENA: I'm Hep.

ABBY: Hep?

HELENA: I took it from my initials- Helena Elaine Preston.

ABBY: Who the heck is Preston?

HELENA: It's my grandmother's maiden name. I was named for her and Dac believes that I may be partially reincarnated from her because usually we are our own relatives. Which makes sense, if you think about it-the whole thing about the family dynamic and the working out of these repeating patterns. Besides, Dac thought "P" was better than "S:" the serpent's letter. The P offers more ... possibilities. Peace, progress, prophetess ...

ABBY: [Under her breath.] Painfully Preyed upon ... Perishing ...

HELENA: [Somewhat hurt.] Whatever ... you're just not giving this a chance, and that's fine. One thing Dac warned us about was preaching to our friends ... I just thought you'd be more open-minded.

ABBY: Come on, Hel, we used to laugh at shit like this! Remember those weirdos from science class-cutting themselves and baying at the moon-

HELENA: They were Satin worshippers, Abby ! [ Abby shrugs as if it’s all the same.) Dac is about freedom, about joy-about letting go of all that is weighing us down and sucking the happiness right out of us. It's killing us. It's killing you-look at you.

ABBY: What about me?

HELENA: You know in the Bible people lived to be 120!. I can't believe you're even comparing this to a Satanic cult ... it's called giving light, not giving dark ... geez Louise.

ABBY: Okay, okay-let's try it again. You can light me up until I catch fire. I won't say anything. Promise. [Abby offers herself again to get the light.)

HELENA: Forget it.

ABBY: Why?

HELENA: Forget about it. You aren't taking this seriously. [Abby briefly considers arguing, but she's been caught.)

ABBY: I'm sorry, you're right. [Silence.] Sorry. Okay.

HELENA: It's just that I've found something so good and meaningful and right and I want to share it. Is that okay?

ABBY: Of course it's okay.

HELENA: You can't imagine how wonderful it is for me there. I've never felt so wanted and like I belong and full of spirit. Really full. Like they told us it would be but it never was. It's like I'm Mary every day. The woman of God, His beloved. The beloved of God. And I can feel it inside me ... more than ... more than sex is inside. Not like sex, but sensual. A buzzing. A caress. Inside caress, all buzzy warm and pulsing. Like a wave of love and breathlessness. Like a new love all over again every time and every day it gets stronger. [Pause.] I know you think I'm out of my mind. You think it's in my mind. That he's in my mind: Dac. But He ... the big He ... is the one. Inside me. Inside. Be still and He is. Inside me ... [They sit in awkwardly for a bit. Abby cannot find a response.]

ABBY: It sounds nice. It does. So ... they let you ... drink beer?

HELENA: Yeah, sure. They aren't Nazis, you know. Dac drinks whiskey, says it's more pure, but he doesn't mind beer. He'll have a beer chaser sometimes. [Another awkward silence.] Abby ... ?

ABBY: Yeah.

HELENA: Do you ever think of me?

ABBY: Yeah, sure. If I didn't think about you, then I wouldn't have recognized you when you called, right?

HELENA: That's just remembering me, not really thinking about me.

ABBY: I guess. I don't know. Why?

HELENA: Just curious ...

ABBY: Yeah?

HELENA: It's funny, you know, the past is a dream to me now. Like my whole life up until now happened to another person.

ABBY: I know what you mean. It's like remembering in black and white.

HELENA: Dac says that the more we break free of our past personae, the more we forget the world of our past.

ABBY: You mean, like, you'd forget me?

HELENA: ... And that's kind of okay ... 'cause there's lots of stuff that I want to forget, right? But to let go of everything-even the good-and it was good, don't you think?

ABBY: It was more ... simple.

HELENA: Safe.

ABBY: So that's what this is all about?

HELENA: What?

ABBY: It's like a good-bye. Am I right?

HELENA: Not so much a good-bye as a stroll down memory lane ...

ABBY: Before the memory of me disappears completely. Great. That's just great. You know-ten years-nothing. No phone call. Nothing. Then at my darkest moment here's my bestest, oldest friend and I think-great, a sign. Life goes on. But no, it's all just another big basta la vista, Abby.

HELENA: The phone works both ways, you know.

ABBY: [Lamely joking.] Maybe my dialing finger was broken.

HELENA: Maybe my entire hand was crushed in a freak circus accident.

ABBY: I was deaf.

HELENA: I was dumb.

ABBY: Oh yeah? Well, I was in a sucky, controlling marriage.

HELENA: Okay. You win.

ABBY: Yes! [A pause.] Stay, Hel. You can stay with me.

HELENA: Abby -

ABBY: Don't decide-just think about it. It's an option.

HELENA: You don't understand, Abbs. With Dac, I'm divine ...

ABBY: Yeah, but are you happy?

HELENA: Don't I seem happy?

ABBY: I don't know, kind of. .. but an unreal happy ...

HELENA: Jealous?

ABBY: Yeah, right.

HELENA: Are you?

ABBY: Jealous?

HELENA: Happy.

ABBY: Hel-

HELENA: Are-you-happy?

ABBY: No. Okay. Life's a roller coaster. You go up, you go down-maybe you learn something and then maybe you're not such a screaming asshole the next time. [Helena shrugs. It may be so.] So maybe I have no business grilling you about being happy; heaven knows I haven't got all the answers. But I have been happy, I will be happy. And I'm not willing to give up everything-forget everyone-everything that came before. That doesn't even make sense. I mean, what is left? Right? If you don't have ... remembering. Remembering is as close to happy as I can get some days.

HELENA: But what if it were all like this-like it is right now-? Perfect moments-and the world wouldn't crash in tomorrow morning and screw it all up. What if every asshole thing you'd done-or was done to you-was just gone. Blip. Clean slate.

What if that's the trade-off. An eternity of perfect moments, instead of suffering over *stuff* that's so far gone you can't even touch the memory of it.

ABBY: But the world's not like that, Hel ...

HELENA: But what if it is? What if it is and we're just not playing it that way? Why shouldn't it be like this?

ABBY: You know, I really am going to miss you, Hel. Just knowing that I could call you-you know-even though I never did.

HELENA: Yeah. I'll miss you. Miss this.

ABBY: No you won't. You'll forget ... remember?

HELENA: True.

ABBY: Not even the pleasure of remembering you forgot. You'll wake up one morning and the memory of me will gone-but I'll miss the good ol' days for both of us, okay?

HELENA: You don't have to, Abbs. It's a choice.

ABBY: I know. [They sit for a moment and take in the evening.] Let's try it again: the light thing.

HELENA: I don't know ...

ABBY: Look, I may never touch the divine-but honestly, I could sure use some light in my life, so if you've got some to spare ... and you're willing to give it, with the understanding of course that I don't believe a word of it ... [Helena smiles. She positions her hand in front of Abby's head and focuses with her eyes closed. Abby looks at Helena intently.]

HELENA: [Eyes still closed.] Are you feeling something this time? [Abby studies Helena’s face, with a mix of love, some sorrow-under it all is perhaps even some jealousy in spite of her disbelief She reaches up as if to touch Helena’s hand, but does not. She caresses the air around her: an invisible touch.]

ABBY: Yeah ... something ... [They sit for some time giving/receiving light ... ] [Fade to black.]
```

---

## IC-0611: Living Out

- Title: Living Out
- Author (byline): Lisa Loomer
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: June 2005
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS 2, ANA, SANDRA, ACTRESS 1, TOGETHER, WALLACE, NANCY, ZOILA, ANNA, LINDA, RICHARD, BOBBY
- Teaser before the introduction: Yes
- Spoken words (computed): 1906
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lisa Loomer
ISBN: 978-0822219941
Publisher: Dramatists Play Service
Date (Month/Year): June 2005
```

### Introduction (context only: never use it for content warnings)

```text
AS AN INFOMERCIAL
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: ACTRESS 1: Ana, Linda, Richard, Zoila

ACTRESS 2: Sandra, Wallace, Nancy, Bobby

NOTE: Ana, Sandra, Zoila and Bobby are Latinx

ANA: (Pg 50) Hola!

SANDRA: Hola muchacha, como estas?

ANA: Ay dios mio! (Pg 51-52) I got my appointment with immigration! So what did you do when you made your citizenship? (Pg 50) What did they ask you on that test?

SANDRA: Everything! What day is Fourth of July? What Thursday is Thanksgiving? How many stars have the flag? How many stripes? (Pg 51) Ay, mija, I got to get a new job. Linda is very nice. But the twins? Yesterday they was playing firemen? They put the couch on fire. And I got three kids when I get home, too! And my son that come from Mexico? Last night the come home with a tattoo!

ANA: Entiendo. I keep missing Santi’s soccer practice because I got to work. He’s real good at soccer. The uniform! I sent one to Tomas too!

SANDRA: Que bueno. You going to bring him real soon.

ANA: (Pg 52) Sabes que? Maybe I should tell Nancy about my son. She’s a woman too, no? She’s a mother –

SANDRA: (Pg 53) (Shakes her head no) They’re not like us mija. Wait till you get your citizenship. (checks her watch) Ooeey – the twins! (Sandra leaves)

ACTRESS 1: HOLA NANNIES was created for families who need a reliable, nurturing, punctual and experienced nanny to look after their little ones.

ACTRESS 2: This could be for working mothers, appointments that you can’t miss or if you just need some well-deserved child-free time.

ACTRESS 1: Our added advantage is that our bilingual nannies can teach your children a second language!

ACTRESS 2: After all, motherhood is universal – a common language that crosses all boarders!

ACTRESS 2: Call today and let us know if you need a nanny for living in or for . . .

TOGETHER: Living Out by Lisa Loomer

****Flashback to nanny interviews ***** WALLACE (Interview 1): (Pg 7-8) I’m Mrs. Breyer, come in . . . come in . . (Wallace takes out her palm pilot (ie ipad) Now, you were interested in living in or living out?

ANA: Living out. (Eager to get the job) The agency told me . . .

WALLACE: That’s all right. I’m seeing both. So, tell me about yourself. Where are you from?

ANA: Do you know Huntington Park?

WALLACE: No, I meant, where are you – (gestures) from?

ANA: Oh. I was born in El Salvador.

WALLACE: Good God, everyone is from El Salvador these days! (laughs) What happened to all the Mexicans? (After an awkward beat) (Pg 9) So I would need you to come by eight. Now, I understand that different cultures have different concepts of time, so I want to be clear that “by eight” . . . I mean “by eight o’clock.” Oh – by the way, I would prefer you speak to the children solely in English. (Looks at Ana’s jeans) And no jeans. Do a little light cleaning – just the kids’ rooms and the family room and the kitchen . . . I’m usually home by five or six.

ANA: (smiles hesitantly) Okay . . . (beat) But . . . you don’t want to say a regular time – like maybe – I work till five?

WALLACE: No. I need someone who’s flexible. Is that a problem?

ANA: No . . . Is just -- I have to pick up my son at –

WALLACE: (sighs) You have a child?

ANA: (Pg 11) Just one in this country. My other son is in El Salvador

WALLACE: (Pg 9) (exasperated) I specifically told the agency not to send me anyone with a child.

LINDA (Interview 2): Oh, you have children? (Pg 11) We had a nanny with a young child – she got sick all the time . . . I’m sorry, Ana. I need someone who can make my kids a priority.

NANCY (Interview 3): Do you have kids?

ANA: I have two boys. (Long beat) But they are both in El Salvador. ***** Scene*****

WALLACE: (Pg 16-17) (to audience) . . . and for the first week or so, I’ll just leave a little cash on the kitchen counter – like I’ve just – left it, you know . . . And when I get home, I’ll count it and see how much is gone. If it’s just a little change, well, no bigee . . . But if it’s a dollar a – and she doesn’t say anything – the next time anything is missing, be it a dollar or a yogurt – I’ll mention it. Casually. I’ll just say “Gee didn’t I buy two cherry yogurts?” And if she does’t say, “Oh – I took one for lunch” -- then I have to fire her. ***** Scene – 1st Day on the Job with Nancy*****

NANCY: (Pg 18-19) (jostling the baby while on the phone with work) Just wanted you to know I’ve looked over the contract and I’ll be in by ten . . . I’m thrilled to be back! (she hangs up and turns to the baby) Mommy’s only going out for a little while . . . Just an itty bitty while. (Ana enters) Oh, Ana! I left a list of number by the phone in case of an emergency. Here.

(still jostling the baby, she points as she reads aloud) My cell . . . her doctor . . . nearest hospital.

ANA: (Smiles; covering offense) I know how to read, Mrs. Robin. I went to school. To be a dentist.

NANCY: You’re a – dentist?

ANA: I couldn’t finish . . .

NANCY: Oh. Of course. Because of your children . . .

ANA: (Pg 20) Because of the war.

NANCY: (feeling guilty) Right! (checks watch) Well, I really should go.

ANA: (Pg 19) (Ana takes the baby; Nancy lets her go with enormous difficulty) I know it’s hard to leave her. It was the same for me with (carefully) my babies.

NANCY: (Feeling guilty) Oh God. And you had to leave them in another country! I’m just going across town . . . And don’t worry, if I’m a little late, my husband can always write you a check.

ANA: Oh . . . Mrs. Robin . . . Do you think you could make it cash?

NANCY: You don’t have a bank account? (Ana doesn’t answer) Ana, you’re not . . . illegal are you? Oh God, I can’t believe I didn’t – I was in such as rush to . . .

ANA: I am getting the green card, Mrs. Robin. Don’t worry. *****Scene – In the park with the nannies*****

SANDRA: (Pg 29) (sneezes) My daughter give me her gripa. Linda keep telling me, “take her to the doctor! Take her to the doctor!” Then she tell me, don’t come tomorrow, she don’t want Jackson to catch nothing (“et cetera”) la la la . . This could cost me two hundred dollars!

ANA: (Pg 30-31) One day we should all stay home!

SANDRA: Everybody! The waiters, the parking peoples, the cleaners –

ZOILA: Los Americanos be driving around in their dirty clothes – starving. Can’t go to a restaurant – there’s nobody to wash the plate! You get home, the house is a mess –

ANA: The plants is all dead –

SANDRA: Nobody to deliver you pizza –

ZOILA: And then you got to take care of your own kids! (They all laugh) Pues . . . I see you tomorrow, mijas. (Zoila exits)

ANA: (beat, then confides in Sandra) Mira. My little one is here. But I told Mrs. Robin . . .

SANDRA: (Nods, understanding) Entiendo. Oye, the only reason I got hired is I got my mother - in-law living with me to watch my girls. How old are your kids?

ANA: Santiago is six. And Tomas is eleven – my son that’s in El Salvador

SANDRA: How long since you seen him?

ANA: Eight years (beat) But I talk to him every week. I just sent my grandmother money to get their own phone. *****Scene*****

ANA: (Pg 35) (on the phone with Tomas) Tomas? Soy mami! How is school? Then you got to study a little harder, Tomas, so when you come here you know your math . . . Do you miss me? . . . I miss you up to the sky! . . . You’re going to come real soon, mijo. (surprised) No, no not for vacation – you’re going to come here to live! (beat) Don’t you want to be with Mami? . . . Oye, did you get the pictures I sent you from the beath? With the rides? (laughs) Te gustan? That’s me and my sister-in law and her friend. (Pause; fighting tears) No, mijo . . . I’m the one in the middle. *****A few weeks later***** At the Robin’s home. Ana is straightening up in the kitchen. She turns on the radio to Latin music and starts to dance. Nancy enters; she appears sick and exhausted.

ANA: (Surprised) (Pg 53) Nancy?

NANCY: (Pg 13) I’m on “The Mommy Track.” I won’t have a prayer in hell of making partner – (laughs) What have the last sixteen years of my life been for?

ANA: (Pg 53-54) Can I get you something? Some chamomile tea?

NANCY: (Nancy starts to cry) I’m sorry, I don’t know why I’m . . . I didn’t get much sleep . . . Jenna just kept crying and crying and drying. Richard thinks she’s angry I’m gone so much. (laughs/cries) Well, clearly he’s angry . . . (quoting Richard) I have the right to do it all – and not do any of it very well.

ANA: I know. You got stress –

NANCY: No, you’ve got stress. I mean, you don’t even get to see your kids! You know what? I should just call up right now. Quit and take care of my own child.

ANA: (Shocked; blurts) No, Nancy! No!

NANCY: (Taken aback) Wow. You must think I’m a really lousy mother.

ANA: You’re a good mother, Nancy. And Jenna is fine . . . a very lucky child. And – you like to work.

NANCY: I do like to work! And I love my child! Is that so horrible of me?

ANA: You know what? I like to work too! (laughs) Ay, don’t tell that to my husband. In my country, all the women is suppose to love to stay home. (beat) I tell you a secret, I want to go back to school. . .

NANCY: (Pg 55) (Phone rings and she answers, instantly professional and peppy) Diane? Hi, I just walked in . . . Tonight? (surprised) He did? Dinner?! No, no, I understand . . . (Pg 56) I’ll call you right back (she hangs up) Ana . . . could you work late tonight? I know, it’s ridiculously short notice. It’s just this director is impossible to pin down. Richard’s working late. There’s really no one else.

ANA: Jenna is getting a cold –

NANCY: I know. But believe me, my boss does not want to hear about Jenna. I’ll be back by nine.

ANA: I . . . guess I could call my husband (getting her cell phone from her bag as Nancy exits to get dressed)(into phone) Bobby? Listen, the senora asked me to work late. I know I promised, but I’ll see his next game. (long beat . . . she hangs up sadly) *****Later that night*****

ANNA: (Pg 57) (Ana is giving Jenna a bottle) Okay, Jenna . . . That’s my good girl. Duermete con los angeles . . . (her cell phone rings) Hallo? . . . Que? . . . I can’t understand you Bobby, slow down. (very still) Okay . . . Okay, Bobby . . . Okay. (she hangs up) Mierda! (she scribbles a note and leaves it on the table and runs out with Jenna)

NANCY: (Pg 58) (Nancy arrives home) Ana . . . Ana? It’s ten o’clock! (she looks in the baby’s room, then frantically to the kitchen where she finds a note) “Emergency. Gone to hospital. Okay.” (Nancy panics; she calls Ana on her cell) Answer, damn you! (Pg 59) (finally Ana picks up) Ana? What happened to Jenna!?

ANA: (on her cell) Jenna is fine – (beat, cries out) It’s my child, Nancy. My child! *****Scene *****

WALLACE: (Pg 60-61) (gossiping indignantly) Linda, she took Nancy’s baby –

LINDA: What? No!

WALLACE: She was taking care of the baby the other night – and something happened – so she was taking the baby with her to the hospital –

LINDA: The hospital!? Oh, my God. Was there a note?

WALLACE: Note shmote, Linda. She took the baby out of the house. She was driving around without a valid license – with Nancy’s child!

LINDA: But her own child was in the hospital?

WALLACE: A child Nancy didn’t even know about! A child who was supposedly in El Salvador!

LINDA: (cries out) What difference does it make?! It’s a child! (beat of silence) Is the child going to be all right?

WALLACE: (The question stops Wallace. She’s horrified she never asked) I . . . don’t know. I didn’t ask about the child. *****Scene *****

NANCY: (Pg 62) If I hadn’t asked her to work late . . .

RICHARD: You were paying her to work late. You were working. Ana was working. Everyone’s working and paying someone else to take care of their child. It’s insane. (Beat) Is it your fault her son had an asthma attack? Is it your fault they took him to the nearest lousy clinic before getting to a real hospital?

NANCY: Doesn’t asthma have something to do with . . . stress? If he was expecting his mother and . . .

RICHARD: (interrupting) What are we going to do about Jenna? What if Ana doesn’t want to come back? Do you want to call the agency about a new nanny?

NANCY: (Pg 63) (punches in a number on her cell phone) Yes – I’d like to inquire about a patient. Santiago Hernandez. . . I’m sorry I’m having trouble understanding your accent. (beat) He’s no longer a patient? (immensely relieved) Thank you. Thank you so much. (she hangs up) *****Scene *****

BOBBY: (Pg 64-65) So soon as we pay the hospital, you could take a break for a while. And soon as we get our papers, we go back to El Salvador together and get Tomas.

ANA: Gracias (beat) But I think he’s better down there. With my grandmother. It’s better.

BOBBY: A grandmother is not a mother

ANA: Sometimes . . . a mother is not a mother.

BOBBY: Ana, please! It wasn’t your fault.

ANA: (after a beat) If I’d picked him up . . . If I’d been there. Like a mother. Like any mother. (Starts to break) I never saw him play soccer. Did he play good? Did he look for me? I never saw him play!

BOBBY: (Crying) My son! Mi hijo. M’entiendes? Let him rest. (through tears) He’s sleeping with the angels, Ana. Just like you always telling him!

ANA: (singing) Dueremete . . . Duermete con los angeles, mijo. (She cries)
```

---

## IC-0612: Master Class

- Title: Master Class
- Author (byline): Terrence McNally
- Work: Not specified
- Publisher: Penguin Group
- Publication date as stated: Dec 1995
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MARIA
- Teaser before the introduction: Yes
- Spoken words (computed): 2181
- Already set (do not supply): none

### Source block (context only)

```text
Author: Terrance McNally
ISBN: 978-0452276154
Publisher: Penguin Group
Date (Month/Year): Dec 1995
```

### Introduction (context only: never use it for content warnings)

```text
INTRO BY ACTRESS 2:
```

### Performance text (classify this)

```text
NOTE: This selection requires the actresses to sing lines from Verdi’s Macbeth in Italian. At the end of this selection, you will find a link to the actual aria as sung by Maria Callas, as well as the translation of the aria. Consultation with an opera instructor is recommended.

MARIA: (Grand entrance, with bows to unheard applause, she “quiets” the phantom crowd) No applause. We’re here to work. You’re not in a theatre. This is a classroom. This is a master class. Singing is serious business. We’re going to roll up our sleeves and work. I appreciate your welcome but enough is enough.

Maria Callas was a Greek-American soprano, and one of the most renowned and influential opera singers of the 20th century. Callas's most distinguishing quality was her ability to breathe life into the wide range of characters she portrayed. Critic Conrad Osborne says it also contained the seeds of her vocal decline. Callas lacked the formal training in proper technique to sustain her ambitious repertoire; and her voice was already starting to fail her by the time she was in her 40s — quite young for an opera singer. In Master Class by Terrence McNally we join Maria Callas at the end of her career. After losing the strength of her voice, she decides to use her knowledge of opera to teach at Julliard. This is a snapshot of her teaching technique and a brief glimpse into the heart of who Maria Callas really was: Master Class by Terrence McNally

MARIA: (looking at index cards she has been carrying) Who’s next? Lady Macbeth, Tosca, Lucia. I must say, what these students lack in voice and technique, they make up for in self-confidence. Don’t laugh. That’s important. Well, we shall see what we shall see. Next victim! That was a joke. My last one, I promise. (To 2nd Soprano) Avanti, Avanti! Don’t linger. If you’re going to enter, enter. If you don’t want to be out here, go away. Now who have we here? 2nd SOPRANO: Sharon Graham

MARIA: So Sharon Graham. What are you going to sing for us? 2nd SOPRANO: Lady Macbeth?

MARIA: The Sleepwalking Scene, I suppose. 2nd SOPRANO: No, “Vieni! T’affretta,” I thought.

MARIA: Ah, the Letter Scene! Well, that’s something. They usually all want to start with the Sleepwalking Scene. You’re humble, like me, that’s good. So. This is her entrance aria, yes? 2nd SOPRANO: Yes.

MARIA: So what are you going out here? Go away. We don’t want to see you yet. 2nd SOPRANO: You want me to go off and come back out?

MARIA: No, I want you to enter. You’re on a stage. Use it. Own it. This is opera, not a voice recital. Anyone can stand there and sing. . An artist enters and is. 2nd SOPRANO: It thought you said this was a classroom.

MARIA: (withering look) Astonish us, Sharon. 2nd SOPRANO: How do I do that?

MARIA: You can start by not entering as Sharon Graham. Enter as Lady Macbeth. Enter as Shakespeare’s Lady Macbeth. 2nd SOPRANO: I’ll do my best.

MARIA: And Sharon, may I say one more thing? That’s a beautiful gown, obviously. We’ve all been admiring it. 2nd SOPRANO: Thank you.

MARIA: But don’t ever wear anything like that before midnight at the earliest and certainly not to class. We’re talking about what’s appropriate. This is a matter class, not some Cinderella’s ball. Eh? Off you go now. And come back as her.

Come back as Lady. (2nd SOPRANO exits.) Sometimes we just have to say these things, eh? I auditioned for Edward Johnson at the old Met wearing a red and white polka-dot dress, white gloves, a blue hat with a veil and what I later learned were known as “Catch me / your “F”-word-me” pumps. I’m sorry, but that’s what they were called. I was overweight and looked like and American flag singing Madame Butterfly. She’ll thank me one day. Are we ready? Begin. (Accompanist begins to play. Maria listens hard, making sounds along with it, rather than actually singing the notes). The curtain is flying up now. No Sharon yet. This is an interesting choice for an entrance. I was onstage at this point. (The music stops. No sign of the 2nd SOPRANO) Sharon? We’re all waiting. Excuse me. (She leaves the stage and comes back a moment later) No Sharon. She’s gone. If her skin is that thin, she’s not suited for this career. It’s not like I said anything about her voice. I didn’t even let her open her mouth. Next student! (2nd Soprano comes back onto the stage) 2nd SOPRANO: I’m back! (Maria looks at her blankly) I’d like to try again. I’ve been in the ladies room throwing up. I must have . . . (Maria holds up her hand to stop 2nd Soprano from going into further detail) So should I go out and come in again? (Maria nods) I’ll yell when I’m ready! (2nd Soprano exits) (Off) I’m ready!

(accompanist begins entrance music again – 2nd Soprano enters at the appropriate
moment. The music stops and she begins to sing)
“Nel di della vittoria io le incontrai.
Stupito io n’era per le udite cose;”

MARIA: Where’s your letter? You’re meant to be reading a letter. 2nd SOPRANO: I was pretending to hold one. Couldn’t you tell?

MARIA: I don’t want pretending. You’re not good enough. I want truth. This is a letter. (She seizes a piece of paper and thrusts it at Sharon.) What are you saying?

2nd SOPARNO: I’m saying “I met them on the day of victory. I was rapt in wonder at the things I heard. When the King’s messengers hailed me as Thane of Cawdor”

MARIA: Put some wonder in your voice! Thane of Cawdor! It’s what she’s dreamed of. 2nd SOPRANO: Thane of Cawdor! “A prediction made by those same seers who foretold a crown upon my head. Keep deep in your heart these secrets. Addio.”

MARIA: Do you know this speech in Shakespeare? 2nd SOPRANO: I’ve read the play, of course, but that was in high school.

MARIA: You want to sing this music without knowing your Shakespeare! 2nd SOPRANO: I’m not an actress. I’m just a singer.

MARIA: Do you think Verdi composed it without knowing his Shakespeare? Vergogna, Sharon, shame. And that wasn’t an entrance. You came on but it wasn’t an entrance. An entrance is everything. It’s how we present ourselves to an audience. It’s how we present ourselves in life. I’ll show you an entrance. You can set the scene for our colleagues. Just read from the score. (She quickly leaves the stage. The 2nd Soprano picks up and reads from Maria’s score. The accompanist begins again.) 2nd SOPRANO: “Scene Two. The grand hall in Macbeth’s castle. There are several rooms leading off it. There is a grand staircase descending from the floor above. There are two small thrones. It is night. A violent storm is raging. Thunder. Lightning. Rain. Curtain. Lady Macbeth enters at the top of the stairs. She is magnificently arraigned. She is reading a letter. (Maria has entered as Verdi’s Lady Macbeth, reading a letter.)

MARIA: “Nel di della vittoria io le incontrai. Stupito io n’era per le udite cose;”

(Maria begins to sing the first lines of Lady Macbeth’s recitative. What comes out is a cracked and broken thing. A voice in ruins. It is a terrible moment.)

(Angrily) Go on, you’re the student here. Not I. And see how important a prop is? 2nd SOPRANO: You hardly looked at the letter.

MARIA: (condescendingly) She has it memorized. She’s read it over and over and over. My choice. Not Verdi’s. Not Shakespeare’s. Callas. You think you can do that now? 2nd SOPRANO: Not like you.

MARIA: I don’t want it done like me. I want it done like Verdi. With music. This isn’t a play. 2nd SOPRANO: “Ambizioso spirit tu sei Macbetto.”

MARIA: There’s two “t’s” in Macbetto. I want to hear them. 2nd SOPRANO: Mac –

MARIA: Don’t repeat, keep going! 2nd SOPRANO: “Alla grandezza aneli, ma sari tu malvagio?”

MARIA: “You would be great, but will you be wicked?” Ah, there’s the question! Don’t even think of stopping! You are Lady Macbeth! (Maria circles the 2nd Soprano, working with her) Use this introduction to focus yourself. Why are you moving your hand? Never move your hand unless you follow it with your heart and soul. 2nd SOPRANO: How do I know when to move at all?

MARIA: The composer tells you. It’s all in the music. Now! 2nd SOPRANO: “Vieni! T-affretta! Accendere”

MARIA: Bite into those words. Spit them out. 2nd SOPRANO: “Ti vo’ quell freddo core!”

MARIA: Let yourself go. Who are you saving it for? The melody broadens here. Let it through you. 2nd SOPRANO: “Le profetesse il trono.”

MARIA: The throne of Scotland has been promised to him! What is he waiting for? This is important to you! You make we want to shake you, Sharon! 2nd SOPRANO: “Ascendivi a regnar. Che tardi?”

MARIA: What are you waiting for? Acccept the gift. Take what I’m giving you. 2nd SOPRANO: Che tardi? Accetta il dono, Ascendi, ascendi, ascendivi a regnar.”

MARIA: Rise and rule. Rise and take your place in this world. This isn’t just an opera. This is your life. Am I right? So what happens here? Hurry up, you’re running out of steam. 2nd SOPRANO: Someone comes in an

MARIA: Not someone. Noone is someone. 2nd SOPRANO: A servant.

MARIA: Now you’re talking! 2nd SOPRANO: He tells her that the king, Duncan! Will be at their castle that very evening.

MARIA: Is Macbeth with him? 2nd SOPARANO: Yes!

MARIA: And how does that make her feel? 2nd SOPRANO: Happy?

MARIA: Don’t keep looking at me for answers, Sharon. Tell me, show me. Vite, vite! What is she going to do about it? 2nd SOPRANO: She’s going to sing a cabaletta!

MARIA: She’s going to kill the King! Do you know what that means? 2nd SOPRANO: Yes, it’s terrible.

MARIA: Not to her! Do you believe women can have balls, Sharon? 2nd SOPRANO: Some women. Yes, I do!

MARIA: Verdi is daring you to show us yours, Sharon. Will you do it?

2nd SOPRANO: Yes!

MARIA: Tonight! It’s now or never. She’s going crazy here. It’s all in the music. Listen
to those dissonances. Don’t act, listen. It’s always in the music, Sharon. Don’t
look at me for help. Listen to Verdi, listen to Shakespeare.
2nd SOPRANO: Or tutti sorgete, ministry infernali
Che al sangue incorate –
Spingeti I mortali! Che al sangue incoret mortali!
Tu note ne avvolgi –
Di tenebra immota”

MARIA: Is there anything you would kill for, Sharon? A man, a career? 2nd SOPRANO: Not off the top of my head.

MARIA: You have to listen to something in yourself to sing this difficult music. These people really existed. Lady Macbeth. Or don’t you believe that? Eh? This is all make-believe to you? 2nd SOPARANO: I’ve never really through about it.

MARIA: That’s because you’re young. You will. In time. Know how much suffering there can be in store for a woman. 2nd SOPRANO: But you were young when you first sang Lady Macbeth.

MARIA: I was never young. I couldn’t afford to be. Not to get to where I was going. Anyway. Enough of that. You came back. You had mut. That’s something. Do you know that German word? It means courage. I had to know it when I sand Fidelio for the Germans during the Occupation during the way. It was at the Theatre Herod Atticus in Athens. I was 18 years old. I needed lots of mut that day. Mut. 2nd SOPRANO: Do you want me to do it again?

MARIA: Yes! Off you go now (2nd Soprano exits) And this is for all of you: there are no short cuts in art, no easy ways. This isn’t life, where there are so many. There is no being at center stage as if by magic. There is always an entrance first, just as there is always an exit after. Art is about those transitions. There is only discipline, technique and mut. Are you ready back there? What is her name? Are you ready back there, Sharon? 2nd SOPRANO: I think so.

MARIA: Don’t think, don’t hope, do. Mut, Sharon, mut. Every eye is on you. 2nd SOPRANO: “Nel di della vittoria io le incontrai. Stupito io n’era per le udite cose;” (continues to hum as Maria speaks)

MARIA: (Loses herself in the voice of 2nd SOPRANO) Let me be her. That sound of the curting parting. The stage dust. Don’t breathe it in. They see me. “Who is this fat Greek girl we never heard of making her debut?” Ah! The silence. It’s time. Begin. 2nd SOPRANO AND MARIA TOGETHER: “Nel di della vittoria io le incontrai. Stupito io n’era per le udite cose;”

MARIA: That’s who I am! This voice. Ah, Verdi! Ah, Shakespeare! Ah, my own ambition. In less than one year I’ve become the Queen of La Scala. That has to count for something. La Divina. Imagine being called La Divina. I am La Divina. Listen to that! I’ve won. I’ve made something of myself. 2nd SOPRANO: (breaking in) Mme. Callas?

MARIA: Sshh! Listen, they’re applauding. Never move on your applause. It shortens it. 2nd SOPRANO: No one was applauding. You told them not to.

MARIA: (sadly, broken) I would never tell anyone that, ma chere. The worst part about being a teacher is being misunderstood. Applause is what we live on. Sometimes it’s the only thing we have. . . . (hardening her outer shell again) I think you have a lovely voice. [But] it takes more than a pretty voice to build a career.

2nd SOPRANO: I wish I’d never done this. I don’t like you. You can’t sing anymore and you’re envious of anyone younger who can. You just want us to sing like you, recklessly, and lose our voices in 20 years like you do. Well, I won’t do it. I don’t want to. I don’t want to sing like you. I hate people like you. You want to make the world dangerous for everyone just because it was for you. (She leaves – awkward silence)

MARIA: So. I think we should stop here. Miss Graham thought I wanted her to sing like Maria Callas. No one can sing like Maria Callas. I am very upset. I’m hurt. As strange as it may seem to some of you, I have feeling too. Maybe this whole business of teaching is a mistake. Do not think singing is an easy career. It is a lifetime’s work; it does not stop here. Whether I continue singing or not doesn’t matter. What matters is that you use whatever you have learned wisely. Think of the expression of the words, of good diction, and of your own deep feelings. The only thanks I ask is that you sing properly and honestly. If you do this, I will feel repaid. (She gathers her things and exits. Blackout)
```

---

## IC-0613: Matt and Ben

- Title: Matt and Ben
- Author (byline): Mindy Kalling and Brenda Withers
- Work: Not specified
- Publisher: Overlook Press
- Publication date as stated: Sept 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BEN, MATT, BOTH
- Teaser before the introduction: Yes
- Spoken words (computed): 1217
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mindy Kaling and Brenda Withers
ISBN: 978-1585675715
Publisher: Overlook Press
Date (Month/Year): Sept 2004
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: It's the story Hollywood has glamorized, publicized, and bombarded us with—

ACTOR 2: How it all began for the two young men, now famous for their on-again-off-again romances and their big-budget smashes and flops.

ACTOR 1: It started with a script for Good Will Hunting,

ACTOR 2: Slaved over by the bright young dreamers in their run-down apartment in 1996.

TOGETHER: Or was it? Matt and Ben by Mindy Kalling and Brenda Withers
```

### Performance text (classify this)

```text
CASTING NOTE from the Authors: The roles of Matt Damon and Ben Affleck are played by two women

BEN: (both actors speak to the audience) Would you believe a package would fall from the sky?

MATT: From the ceiling!

BEN: Into our laps?

MATT: How does a package fall from the ceiling?

BEN: But it did.

MATT: That’s the thing, it did!

BEN: Amazing things do happen.

MATT: All the time.

BEN: We realize this.

MATT: But not magical things.

BEN: Like packages falling from the sky-

MATT: From the ceiling!

BEN: But it happened to us.

MATT: We didn’t know what it was.

BEN: Or where it came from.

MATT: I was scared.

BEN: Matt was scared. Really scared.

MATT: But then we realized that there was no one here and we didn’t have to whisper anymore and we could talk in our normal voices.

BEN: JUST TO BE CERTAIN THERE WAS NO ONE THERE; WE ACTUALLY TALKED MUCH LOUDER THAN USUAL. (to Matt) “HEY, WHERE’D THIS COME FROM?”

MATT: I DON’T KNOW BUT IT FELL RIGHT NEXT TO MY GUN!

BOTH: (to audience) The mystery begins.

BEN: Not ticking.

MATT: Not a bomb.

BEN: Not moving.

MATT: Not an animal.

BEN: Not burning.

MATT: Not on fire.

BOTH: Where did it come from?

MATT: We searched the entire apartment. Couch!

BEN: Fine!

MATT: Window.

BEN: Fine!

MATT: Ceiling.

BEN: Fine!

MATT: But it fell from the ceiling.

BEN: Well . . . I’m looking at the ceiling.

MATT: And?

BOTH: Nothing.

MATT: Where did it come from?

BEN: We knew we had to open it. Who would do the honors?

MATT: No way.

BEN: So I opened it. “Good Will Hunting.”

MATT: “By Matt Damon . . . and Ben Affleck.” Is this a joke?

BOTH: We wrote a script? (Matt begins reading the script as Ben tries to read over his shoulder in an aggressive and physical manner)

MATT: Ow.

BEN: Done?

MATT: No.

BEN: Are you finished yet?

MATT: Stop it! This is an excellent script. It’s the best I’ve ever read.(to audience) If Ben put this here, if Ben wrote this, I have severely underestimated his talents.

(Ben has lost interest in Matt’s reading and is attempting to drink an entire soda in one drink)

BEN: Hey, check this out! All in one sip!

MATT: (to audience) Ben did not write this. (to Ben) I’m done.

BEN: It’s so good. (talking about the soda)

MATT: It’s really good. (talking about the soda)

BEN: It’s so good, it’s so good, it’s so good! (talking about the soda while punching Matt in the arm)

MATT: Ben, don’t hit me.

BEN: Sorry.

MATT: I’m littler than you.

BEN: I know . . . It’s so good! (talking about the soda)

MATT: It’s kind of too good.

BEN: (Ben dials the phone to call his brother) Case! Casey, you will not believe what happened to us.

MATT: Ben!

BEN: (on the phone) Yeah. Uh huh. No, listen. We were sitting on the couch today-

MATT: Ben, hang up!

BEN: What?

MATT: Hang up the phone!

BEN: Why?

MATT: Hang up the phone! (Matt goes to the apartment door to lock it)

BEN: (on the phone) Okay, okay. Uh . . . Casey I have this problem with call waiting, beep, just hold on . . . beep . . . I gotta get that, we might get disconnected so just . . . (to Matt) What was that about? Why are you locking the door?

MATT: You can’t tell everyone, Ben.

BEN: He’s my brother.

MATT: This is very confusing. We don’t need to involve everyone.

BEN: What’s confusing?

MATT: Ben, where do you think the script came from?

BEN: The hand of God. Where do you think it came from?

MATT: I also think God . . . don’t you find that strange?

BEN: Yes.

MATT: It’s amazing.

BEN: It’s a blessing.

MATT: It’s a gift . . . unless . . . have you ever done anything really bad?

BEN: It’s not a curse!

MATT: Why not?

BEN: Because it’s not!

MATT: Well, it could be a curse. Like Job? Who brags about his family and gets plagued by locust and boils!

BEN: What do we have to brag about?

MATT: C’mon, we’re white, male, American . . . we’re in School Ties !

BEN: It’s not a curse.

MATT: No not a curse, but maybe a test. Think about it -- all that you and I want is what?

BEN: Steak sandwiches!

MATT: Not right this instant.

BEN: Cable TV

MATT: More long term.

BEN: Sony . . .

MATT: Sony Playstation, No.

BEN: Money, an Oscar, a girlfriend, and Casey to lose his speech impediment.

MATT: Right, fame, sex, riches, those are all sins. We’re supposed to say no to this. We’re supposed to take the script and get rid of it.

BEN: Absolutely not! I hope your messing around!

MATT: No, really, why do we deserve this? We don’t. See? It’s just like Job.

BEN: We’re nothing like Job!

MATT: Not literally, but metaphorically . . . in terms of a metaphor. (puzzled look from Ben) Okay, a metaphor is a figure of speech used to compare -

BEN: I know what a metaphor is.

MATT: No, right, but if I were to use “like” or “as” then it would be-

BEN: I know what a simile is too, I just don’t get what you’re talking about since none of this stuff happened to us!

MATT: I know! That’s why it’s a metaphor! It’s not an exact replica of the situation, it’s a comparison-

BEN: I know what a metaphor is!

MATT: Apparently not!

BEN: What is your problem?

MATT: My problem is that every time I try to talk to you about something serious-

BEN: Like something Lala Land-

MATT: No, something serious, you don’t even have the vocabulary to discuss it!

BEN: That’s not true!

MATT: Yes, it is! You dismiss every conversation, every discussion, if it has even slightly complex ramifications!

BEN: Okay, let’s have it your way, Matt Damon Serious Time. (Sarcastically) Matt, I’m so scared of this scary script! What are we gonna do? I mean, what are we gonna do?

MATT: Wow, see? You’re proving my point, proving my point. With every word, you’re proving my point!

BEN: Proving my point, proving my point, proving my point-

MATT: This is not a joke!

BEN: I know that!

MATT: Oh, really?

BEN: Yes, really. And to be honest, I’m not the one messing around here. I mean, what’s the point of this conversation? We’re not gonna throw it away. I’m not, and I’m not gonna let you . . . Anyways, Matt, if it’s a curse, we’re cursed. We can’t just put it in the garbage can and just the garbage be cursed. Because the garbage is touching the floor of the apartment where we are standing. And if we throw it away, it’ll just go to some dump, which will still be near us, and still on the planet earth. And the only way to get away from that would be to float, or hover above the crust of the earth. So, unless you have a rocket ship or something . . . but the point is, we can’t run away from this, or fly away from this, whatever it is. Your name’s on it, my name’s on it. We just have to deal with it.

MATT: I guess.

BEN: And the curse is wondering about it later if we never do it.

MATT: That’s true.

BEN: Okay?

MATT: Yeah. It’s just-

BEN: Matt!!

MATT: Then we need to do it right.

BEN: Of course.

MATT: And that’s going to be difficult.

BEN: Oh, my God.

MATT: We have to get a director.

BEN: Yes.

MATT: And the right location and cast.

BEN: Uh, huh.

MATT: Plus a crew! I mean, do you know any grips?

BEN: Nope.

MATT: Are you even listening to me, Ben?

BEN: Yup.

MATT: No you’re not.

BEN: Well, it’s just that you’re preaching at my face about how to make a movie. I’ve been in a movie.

MATT: But you haven’t made a movie.

BEN: Neither have you.

MATT: Okay so we both should be concerned, about getting this just right, because we both have to acknowledge that this doesn’t just happen to everyone-

BEN: Okay, I will. I gotcha!

MATT: You will what?

BEN: I will be perfect. I will make a perfect movie with you.

MATT: That’s not what I mean.

BEN: Then what do you mean? What?

MATT: Remember senior year? The talent show?

BEN: Yeah, we rocked it! (Ben freezes in “rocker mode”)

MATT: (to audience) Regardless of the fact that I didn’t write one word of this script, and that my best friend is a complete idiot, I had to do Good Will Hunting. Good things come in strange packages. Who knows? If it hadn’t been for Ben, I might not have been in the right place at the right time. Sure, I’ll do it. So long as my name comes first.
```

---

## IC-0614: Mean Girls – Original Screenplay

- Title: Mean Girls – Original Screenplay
- Author (byline): Tina Fey
- Work: Not specified
- Publisher: Scriptfly.com
- Publication date as stated: Revised June 3, 2003 (Slightly Different than the Movie)
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, CADY, SPAZZY GIRL, KAREN, GRETCHEN, DAMIAN, JANIS, MR. DUVALL, REGINA, MRS. GEORGE, VOICE OVER, GIRL 1, GIRL 2, GIRL 3, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1508
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tina Fey based on the book Queen Bees and Wannabes by Rosalind Wiseman
ISBN: N/A
Publisher: Scriptfly.com
Date (Month/Year): Revised June 3, 2003 (Slightly Different than the Movie)
Original can be purchased from Scriptfly.com at
https://www.scriptfly.com/searchpage/resultpage.php?search=m
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 2: Cady Heron may be a world traveler, but she has a lot to learn about navigating the treacherous outback known as high school.

ACTOR 1: Filled with back-stabbing, sarcasm, and vicious cliques – especially if you’re a girl!

ACTOR 2: Fortunately, on the very 1st day of school, she meets Damian and Janis who explain the social pecking order led by The Plastics and Queen Bee Regina George.

ACTOR 1: Mean Girls – The Original Screenplay by Tina Fey
```

### Performance text (classify this)

```text
Suggested Roles:

ACTOR 1: Cady, Gretchen, Janis, Mr. Duvall. Mrs. George, Girl 2

ACTOR 2: Spazzy Girl, 8-Year-Old-Kid, Karen, Damian, Regina, Voice Over, Girl 1, Girl 3

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

ACTOR 2: (offstage) African Music from Lion King

CADY: (Pg 6) (to audience) Hi, my name is Cady Heron. (Pg 2) I’m 15, and until today, I was homeschooled. That means my mom was my only teacher and my Dad was the only sub. I know what you’re thinking. Home-schooled kids are freaks. Cut to the Scripps Howard Spelling Bee

SPAZZY GIRL: (at microphone, speaking loudly) X! Y! L! O! CI A! R! PI Xylocarp!

CADY: Or that we’re weirdly religious or something. 8-YEAR-OLD-KID: And on the third day God created the Remington bolt action rifle so that man could fight the dinosaurs.

CADY: (Pg 3) But my family’s totally normal. Except that both my parents are research zoologists and we’ve spent the last four years in a hut in Namibia.

KAREN: (Pg 16) So, if you’re from Africa, why are you white?

GRETCHEN: Oh, my God, Karen. You can’t just ask people why they’re white!

CADY: (Pg 4) Then it happened. My mom’s articles about large cats earned her a full professorship at Northwestern University. So it was goodbye, Africa. Hello, Evanston, Illinois.

DAMIAN: (Pg 10-11) [Hi, I’m Damian and] I am so going to mentor you. The cafeteria is terrible. Buy your lunch at the school store. I recommend the white cheddar cheezits. What else? Oh! Spring Fling! (sees a gym class trudging out onto the field) In the name of all that is holy. Look at Karen Smith’s gym clothes!

JANIS: Karen is one of the dumbest girls you will ever meet. Damian sat next to her in English class last year.

DAMIAN: She asked me how to spell orange!

JANIS: And that little one next to her? That’s Gretchen Wieners. She’s rich cause her Dad invented Toaster Strudel.

DAMIAN: She is a little Gucci Hootche – A girl with a $1,000 of designer clothes on a $2.00 body.

JANIS: (Pg 17) (pointing and whispering) [That’s] Regina George. She is the most plastic of all The Plastics.

DAMIAN: She is fabulous, but she is evil. ***** Later that Day in the Cafeteria *****

MR. DUVALL: (Pg 15) Please give a round of applause for the head of the Student Activities Committee Miss Regina George!

REGINA: Thank you! Under my rule the SAC will do more than just sell candy canes and sponsor stuff like recycling. It’s gonna be about being kind to the less fortunate. Where’s that new student? (she spots Cady in the crowd) Come here! (Cady joins her on stage) I’m going to make it my personal responsibility that by the end of the year, she thinks Evanston High school is totally rad. A few minutes later – Cady is sitting with Regina, Karen and Gretchen (The Plastics)

CADY: (Pg 16) And we only moved here two weeks ago—

REGINA: (Regina grabs Cady's arm) Where did you get that bracelet? I love it.

CADY: Africa.

GRETCHEN: It's so fetch.

REGINA: (disdainful) What is "fetch?"

GRETCHEN: (withering) It's, like, slang . . . from England . . .

REGINA: (Pg 27) (rolls her eyes) You know what, Cady? You're, like, actually really pretty.

CADY: Thank you.

REGINA: (snarky) So you agree?

CADY: What?

REGINA: You think you're really pretty.

CADY: I didn't say that. (to audience) What just happened?

REGINA: (Pg 16-17) (haughtily) Cadv, could you give us some privacy for, like, one second? (huddles and whispers with the other two plastics) Okay, let me just say that we don't do this a lot, so you should know that this is, like, a huge deal.

GRETCHEN: We want to invite you to have lunch with us every day for the rest of the week. So we'll see you tomorrow.

KAREN: On Tuesdays we wear pink!

CADY: (Pg 19) (to audience) Having lunch with the Plastics was like leaving the actual world and entering "Girl World." And Girl World had a lot of rules.

KAREN: We only wear jeans or track pants on Friday.

GRETCHEN: You can't wear a tank top two days in a row.

REGINA: You can only wear your hair in a ponytail once a week. So, I guess, you picked today. (Pg 80) I’m starving. (leaves to get lunch)

GRETCHEN: (Pg 19-21) And if you break any of these rules you can't sit with us at lunch. I mean, not just you, any of us. Like, if I was wearing jeans today, I would be sitting over there with the art freaks. (points to Janis and Damian’s table)

KAREN: You have to be considerate of the rest of the group. I mean, you wouldn't buy a skirt without asking your friends first if it looks good on you. It's the same with guys. You may think you like someone, but you could be wrong. Have you seen anyone that you think is cute yet?

CADY: Actually, there's a guy in my Calculus class. His name is Aaron Samuels—

KAREN: No, no no.

GRETCHEN: No. You can NOT like Aaron Samuels. He's Regina's ex-boyfriend. And then he broke up with her for no reason.

KAREN: Because she cheated on . . .

GRETCHEN: Regardless. Ex-boyfriends are off limits to friends. Don't worry. I will never tell Regina what you said. It'll be our secret. (Regina enters with her food)

REGINA: Ugh. There's gonna be a fire drill in, like, two seconds. (Fire alarm goes off) I told Coach Farr we had to skip it cause Karen might be pregnant.

KAREN: (laughs, then) I'm not though, right?

GRETCHEN: (Pg 23-24) Oh, my god, there’s Jason! . . . (heartbroken) He’s with Taylor Wedell.

REGINA: (outraged) Wait. No. He cannot blow you off like that. Gimme your phone. (dials) Wedell on South Boulevard (pushes another button on phone – then in a mature voice) Hello, may I speak to Taylor Wedell please? This is Susan at Planned Parenthood. I have her test results. Have her give me a call. Today, if she can. It’s urgent. Thanks. (she hangs up, Regina and Gretchen laugh) She is not going out tonight!

CADY: (wide-eyed to audience) I could see why it was good to have Regina as a friend. (beat) I guess the Plastics liked having me as a pet, cause by Friday I was invited to Regina's house after school. (to Regina) Regina, your house is really nice. REGINA I know, right?

MRS. GEORGE: (Pg 25) You want anything, don't be shy, honey. There's no rules here. I'm not like a regular mom, I'm a cool mom, right, Regina?

REGINA: (exiting) Please stop talking. (Regina opens the door to her huge bedroom) This is my room (The girls settle in which involves looking at themselves in the many mirrors)

KAREN: (Pg 23) So how was your first week?

CADY: Good. I'm joining the Mathletes.

REGINA: No, no, no. That is social suicide. You are so lucky you have us to guide you.

GRETCHEN: (Pg 26-27) I never should have bought these capri pants.

REGINA: How many times do I have to tell you? The Gap is for old people.

GRETCHEN: I hate my calves.

KAREN: God, my hips are so huge.

CADY: (to audience) Before I met the Plastics, I thought there was just fat and skinny. Apparently there's an infinite number of things on your body that can go wrong.

GRETCHEN: My hairline's weird.

REGINA: My pores are huge.

KAREN: My nailbeds suck. (The girls look at Cady. It is her turn.)

CADY: (struggling to come up with something) I have really bad breath when I wake up in the morning.

REGINA: (Pg 33-34) (cattily) Gretchen told me that you like Aaron Samuels.

CADY: (terrified) What are you talking about?

REGINA: I mean, I don't care. (obviously cares) Do whatever you want. But wait. Aren't you so mad that Gretchen told me about this?

CADY: (looks at Gretchen) I’m not mad. (trying to assume the attitude of “A Plastic”) She’s just immature.

GRETCHEN: (stomps her foot and pouts) I can't believe you think I'm immature!

CADY: (Pg 39) (to audience) I knew how this would be settled in the wild. (Regina leaps like a cheetah at Cady who chatters and howls like a monkey) But in Girl world, all the fighting had to be invisible. (shakes head) ***** The Next day at the Mall ***** Damian and Cady go to visit Janis at Bath and Body Works where she is behind the counter working.

CADY: (Pg 30-31) And they have this book, this "Burnbook" where they write mean things about the girls in our grade.

DAMIAN: Rosemary Mint Foot Spray?

JANIS: It makes your feet smell like a salad. (to Cadv) Cady, you've got to steal that book. We could publish it and then everyone would see what an ax-wound she really is!

CADY: No way! I don't steal.

JANIS: There's two kinds of evil people, Cady. People who do evil stuff. And people who see evil stuff being done and don't do anything to stop it. (Pg 79) You’re the worst. At least Regina George knows she’s mean. You act like you’re so innocent. (imitating Cady) I used to live in Africa with the birds and the monkeys.” You’re plastic! Solid, durable, molded plastic! ***** Principal’s Office Monday Morning ***** Regina is fake crying to MR. DUVALL. He is reading the "Burnbook."

REGINA: (Pg 81) I found it in the girls' bathroom. It's so mean, Mr. Duvall.

MR. DUVALL: (shocked) Good Lord. What does that say? (reads aloud) Regina George is the nastiest (clears throat) I ever met. Do not trust her! She is an ugly (clears throat) . . .

REGINA: (fake sobs) Why would somebody write that? It's so mean!

MR. DUVALL: Okay, take a breath. We'll find out who did it.

REGINA: (suddenly ice cold) There's only three girls in the whole grade who aren't in it. [Inserted as transition]

VOICE OVER: (Intercom off-stage): Cady Heron, Gretchen Wieners, and Karen Smith report to Mr. Duvall’s office immediately. Cady Heron, Gretchen Wieners and Karen Smith report to Mr. Duvall’s office. ***** Scene Change*****

CADY: (Pg 93) (to audience) Ms. Norbury had us write out apologies to people we had hurt in our lives. (The girls read written "apologies" out loud)

GIRL 1: Alyssa, I'm sorry I called you a gaptoothed b****. It's not your fault you're so gap-toothed.

GIRL 2: Laura, I don't hate you because you're fat. You're fat because I hate you.

GIRL 3: I iust wish we could all get· along like we used to in Middle School. I wish I could bake a cake made out of rainbows and smiles and we'd all eat it and be happy—

DAMIAN: She doesn't even go here!

CADY: (Pg 113) (to audience) I guess the biggest thing I learned at Evanston was that tearing other people down will not make your life any better. Calling somebody else fat will not make you any thinner. Telling someone they're stupid does not make you any smarter. (Pg 117) My first year of "real" school was like treading water in a shark tank, but now, I just float.

TOGETHER: Do-Wap Baby Shark music and dance to end selection
```

---

## IC-0615: Misreadings

- Title: Misreadings
- Author (byline): Neena Beber
- Work: Best American Short Plays 1996-1997
- Publisher: Applause Theatre Books
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, SIMONE, RUTH
- Teaser before the introduction: Yes
- Spoken words (computed): 1931
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neena Beber
Book: Best American Short Plays 1996-1997
ISBN: 1557833168
Publisher: Applause Theatre Books
Date (Month/Year): Jan 1998
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

SIMONE: A wall between our souls? [RUTH looks at her, about to say something, about to reach out.] I'm sorry if I've been rude. I'm sure a lot of people like your class. Maybe I wasn't raised well. I'm sure somebody's to blame. [SIMONE goes.]

RUTH: The next day she showed up at nine on the dot. I felt a certain pride that I had somehow managed to reach her, that she was finally going to make a real effort, but she handed in her blue book after a matter of minutes. I was rather disgusted and let it sit there, until a pile formed on top of it, a pile of blue books filled with the scrawling, down-to-the-last-second pages of my other more eager, or at least more dutiful, students. Later I began to read them straight through from the top, in the order they were stacked in. I wasn't looking forward to Simone's. In answering my essay question about how the novel Anna Karenina moves inevitably toward Anna's final tragic act, my students were, for the most part, thorough and precise. They cited all of the events that led to Anna's throwing herself in front of the train, touching on the many parallel plots and the broader social context. I was satisfied. I felt I had taught well this last semester. My students had learned. In the blue book she had written "All happy people resemble one another, but each unhappy person is unhappy in their own way." So I guess she had read Anna K; the opening sentence, at least. My first instinct was to correct the grammar of her little variation. There was nothing else on the page. I flipped through the book; she'd written one more line on the last page: "Any world that I'm welcome to is better than the one that I come from." I'm told it's a rock lyric. Something from the seventies. Anna was written in the seventies, too, funnily enough, a century earlier. I would have given Simone an F, but I noticed she had already marked down the failing grade herself, on the back of the book. Or maybe the grade was for me. By the time I came to it, days had passed. I didn't leap to conclusions. Come to think of it, Anna's suicide always takes me by surprise as well, though I've read the novel many times and can map its inexorable progression. [SIMONE, just as before...]

SIMONE: That's a lot of money. Do you think you're worth it? Do you think this class is worth it? [RUTH turns to her.]

RUTH: I live in worlds made by words. Worlds where the dead can speak, and conversations can be replayed, altered past the moment of regret, held over and over until they are bent into new possibilities. [RUTH tries to reach toward SIMONE...]

SIMONE: Do you think I'm worth it? Am I? Am I? Am I?

RUTH: I live there, where death is as impermanent as an anesthesia, and the moment of obliteration is only...a black-out. [SIMONE lights a cigarette as lights black out.]
```

---

## IC-0616: A Dozen Red Flags

- Title: A Dozen Red Flags
- Author (byline): Briana LaVine Leigh
- Work: A Dozen Red Flags
- Publisher: Mushroom Cloud Press
- Publication date as stated: September 1, 2021
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NOTES
- Teaser before the introduction: No
- Spoken words (computed): 2294
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
Duo or Humorous Interp

ELIZA I mean, I guess I’ve never been, like, thee best judge of character. It’s possible I have a slight tendency to assume people have good intentions. Don’t get me wrong, I don’t just trust anyone for no reason……….. but yeah the tattoo on his forearm of a naked woman being torn in half by a centaur probably should have been my first red flag. Aaaaaand perhaps the complete absence of any online identity...at all...should have been the second? And all of the tarps and concrete blocks in the backseat of his car? Who am I kidding, if a dude handed me a dozen red flags I’d be like “A dozen red flags?! For me?!”

INTRO

DELORES You’ve got to watch out for these new generation hippies-they’ve got these dumb names like Vistun, what is that? I saw one on the Price is Right yesterday, dreadlocks and everything, probably drinks tree milk and plays the bassoon, his name-get this Eliza- was Apple. What? Why? Back in my day-

ELIZA Yeah I know I know, back in your day everyone was intelligent and hard-working and made great choices all the time. [sarcastically] That’s why the world was such a perfect place when I was born on September 12th, 2001.

DELORES Well see now that was unfortunate.

ELIZA Delores I’ve been working at the nursing home for three years, overtime most weeks, putting myself through nursing school, packing PB&J's to save money and being nice to you even though they don’t pay me extra for that, so whoever you have in mind when you keep spouting off about “the young people these days” it’s not me. I think you’ve been watching too much Jersey Shore.

DELORES You’re a good girl Eliza, and I know you want to find that special boy, and the feet swept and bells at the church and nursery rhymes and all that schmaltz [she shudders] but land sakes you have terrible taste in men, and most men don’t know their butt from their elbow to begin with.

ELIZA [to audience] Delores Yarmicheal was the youngest resident at Bright Horizons Nursing Home. She was completely capable of living on her own but had developed an addiction to her grandson’s ADHD medication on a weeklong stay with her son in Yuma, when she accidentally popped his Adderall instead of her blood pressure medication [like a side note and with an eye roll] because she refuses to wear her readers. Suffice it to say, the adrenaline rush reminded her of her field research days as an archeologist in Guatemala and she was hooked. [Delores mimes out the following] The jig was up when she stole a car from a lady parked in front of the Pharmacy, led police on a high-speed chase down Interstate 90 and saw some serious airtime hopping the overpass north of the Billington Target.

DELORES [at the scene of her arrest] Oh you think you’re gonna arrest me with that tiny gun and your tiny handcuffs, I’m a Freedom Rider, you’ll never cage me, coppers!

ELIZA The judge gave her the option of drug rehab or an elder care facility. Which is when she landed at Bright Horizons and took a liking to me for some reason. She would have been able to leave after 6 months but since her arrival she has [lists]: Started Cliff Wiggin’s pants on fire after he called her sweet lips, stole a nursing assistant’s iPad and used it to order cannabis gummies, which she shared with the entire nursing home Bridge Club

BRIDGE CLUB 1 [old person very high] Whoa
BRIDGE CLUB 2 [old person also very high] Yeah
BRIDGE CLUB 1 These...cars...are so different these days
BRIDGE CLUB 2 I think this is a fish tank...but I’m having trouble remembering what fish are
supposed to look like.

ELIZA And sprayed our Chaplain down with a fire extinguisher when she overheard him telling the charge nurse that Delores might be possessed. But it was the last charge on her record, assault with a venomous snake, which is partially my fault, that tacked on most of the extra time. It all started when I went on a date with a guy I met in line at Petco. Dupree Milgrin. I think. I mean, not ‘I think’ like I don’t know where we met, I think that’s his name, but the forensics aren’t back yet. Anyway [transition noise/song]

DUPREE [gruff voice, mysterious] I prefer long hair

ELIZA [tentative, looks around to see if he’s talking to someone else] Um, excuse me?

DUPREE Cats

ELIZA [looks confused]

DUPREE Long-haired cats. [nods at the packages she’s carrying, evidence of owning a cat] I prefer long hair on my cats.

ELIZA [laughs sweetly, like she is lucky he is talking to her] Oh, ha, I do have one long haired Maine Coon, but also a British Shorthair.

DUPREE I bet your cats don’t have pretty hair like yours, and that smells as good as yours.

ELIZA [helplessly clueless] Oh thank you! I’ve been using a new conditioner with lemongrass; it’s supposed to help keep the mosquitos away!

DUPREE Can I try it?

ELIZA [to audience] ok ok I know, it looks bad, and in retrospect I...should maybe hire some kind of filtering service to assess potential dates...a first date at the city zoo...at 2 a.m. when the zoo is closed...but I thought maybe he worked there, or there was some kind of moonlight special? In my defense, I did tell people where I would be. Well, I told Delores. I knew my friends would get all crazy and flip out, but Delores was kind of stuck.

DELORES Like hell you’re going on a first date with a psychopath in the middle of the night at the zoo. Did you at least get his plates? I got a guy who can run the plates.

ELIZA I hadn’t thought about looking at his license plates. Besides, it’s not nice to judge-isn’t that what they tell us all growing up, don’t judge a person until you walk a mile in their parole ankle bracelet? For all I knew this could be the best night of my whole life!

DUPREE I bet you’re wondering why I asked you to meet me at the closed zoo, at 2 am on a Tuesday.

ELIZA Nope!

DUPREE [crazy eye, shaking his head yes] Perfect. This is the best time to...see...the animals that... sleep during the day? [he diverts his eyes to avoid giving himself away] Grab the blue flashlight off my dash.

ELIZA Dupree, or whatever his name is, crept stealthily to the main zoo gate with a crowbar and two screwdrivers. He probably saw something that needed to be fixed. As I clicked on the flashlight I caught a glimpse of the contents of his SUV. A large ultraviolet light, metal bowls, thermometers, a few concrete blocks and tarps. His passenger side seat was filled with tiny Ziplock bags with some kind of seeds in them. At this point I started to second guess my decision-making paradigm. Maybe I should have worn my tennis shoes.

DUPREE K LIZA, QUICK. It's totally cool that we’re here. My friend um Jack, he works here. Yeah. I just don’t want to...trip the cameras, I mean the motion sensors...the light sensors-cuz ahhh the lights come on and wake up...animals.

ELIZA It was actually a really nice time. He didn’t say much but I told him about my cats and the goldfish and sugar gliders who hated the cats. The moon was full and bright, so every once in a while Dupree would stop suddenly, freeze, and be like “ flashlight off NOW” so that we could just see things in the moonlight. He had me walk a very particular path that he said had the best lighting, which was sweet. He kept looking up at the light poles and doing these funky dance move things [make a move like you’re avoiding a motion detector] He was super interested in this one enclosure in particular. I was trying to read the sign when Dupree suddenly disappeared into the bushes and reappeared with a large, flat four-wheeled cart.

DUPREE Weird, they just left this cart sitting here. [grabs stomach suddenly] Oh gosh, I’m feeling that burrito from earlier.

ELIZA Oh no! I have some Alka seltzer in my purse-

DUPREE No that’s ok, I just need you to run back to the gate, prop it really wide open and then ah...get in your car and leave. That way I can just run out and not be uh embarrassed.

ELIZA Look, I’m a nurse-and many people have mistaken appendix pain or gallbladder pain for food-related digestion issues, not to mention the possibility of kidney stones and-

DUPREE SHUT UP! I mean, sorry I just, ah, please hurry.

ELIZA I can understand being embarrassed about gas on a first date, but you really can never be too careful-so as I ran back to the gate I punched in the emergency services number to my cell, just in case he started in with the fever and chills. I jumped in my car and waited to be sure he arrived safely back at his vehicle. After a couple of excruciatingly long minutes Dupree came creeping down the cobblestone walkway of the zoo entrance pushing that same cart, the chain running from his belt to his wallet was clanking against the screwdrivers still in his pocket.

DUPREE [yell whisper] WHAT ARE YOU STILL DOING HERE?!!!

ELIZA [to audience] Well, his sudden change of temperament, along with his flushed face and watery eyes was all the evidence I needed to hit send on my cell phone. This man was obviously experiencing an acute attack of appendicitis and needed emergency medical help.

ELIZA I think the gas you are experiencing may actually be a medical emergency-it’s ok, I am a trained professional!

DUPREE NOBODY COULD POSSIBLY BE THIS STUPID [pulls out a gun] GET IN THE CAR AN DRIVE AWAY NOW

ELIZA [to audience] I’ve seen people get ornery over appendix pain before, but this was a little ridiculous.

ELIZA Look Dupree, I already called for an ambulance, lay down flat and don’t make any jarring movements.

DUPREE YOU WHAT? OH, YOU DUMB- [raises gun up to shoot, then jerks his head upward with a bewildered, startled look] WHAT THE [Delores is flying from the top of Eliza’s car towards Dupree] The following lines are delivered throughout the ensuing struggle between Eliza and Delores, in whichever order/combination suits the actor(s):

ELIZA Delores Yarmicheal-what were you doing in my trunk, leave that

man alone, he’s experiencing a medical emergency! [fights with Delores,

trying to hold her back] Put down the fork! Watch out for the cart,

Delores-you’re going to trip-

DELORES Wanna a piece of this, you chicken liver schmear?

HiYaaaaah. The only medical emergency he’s going to have is when I

stab him in the eyeball with this fork!

Eliza and Delores wrestle towards the cart, Delores falls/trips/lands on the cart

DUPREE NO NO NO, LADY BE CAREFUL

ELIZA See, would a monster be concerned about your welfare-wait what’s that hissing sound?

DELORES Be careful with this??????? [she holds up the snake] Is the leatherhead bad boy afraid of a little tiny SNAKE? [she hurls the snake at Dupree and she and Eliza watch as Dupree is bitten by the snake and collapses-we watch their facial reactions to the sequence].

Pause, Delores is supremely satisfied with herself, Eliza is in horrified shock

ELIZA Delores Yarmicheal how in the heck? Where did you-how did you-

DELORES I snuck into your trunk during wheelchair Zumba-I had a bad feeling about this Eliza.

Police siren sounds

POLICE OFFICER Ma’am you’re under the arrest for possession of, [thinks for a second] and assault with a venomous snake.

DELORES Oh it’s just a Coastal Taipan you big sissy. Warning though, don’t pick it up by its tail, they get really grouchy when you do that.

POLICE OFFICER Actually, could ah, could you put the snake back?

DELORES That’s what she said

POLICE OFFICER Ma’am. Please.

Transition sound/song

ELIZA At the hearing it really looked like Delores was going to be called the hero of the day and see the charges dropped-but given her priors the judge was skeptical that our story was true saying, and I quote, “There’s no way one woman could be that gullible and another that crazy, connected to a crime this weird, and be innocent.” To which Delores just had to reply

DELORES Well there’s no way a man could be that arrogant, that short, and that bald and not become a judge in the United States court system.

ELIZA So yeah, I think we’ll be in here for a while. But I’m thankful, I learned a valuable lesson about how to handle venomous snakes.

DELORES Aaaaaand?

ELIZA And to not trust my terrible instincts.

JAIL CELLMATE Hey lady, you smell of lemongrass...and snake skin.

ELIZA Oh my gosh thank you! That’s an interesting tattoo on your forearm-is that a naked woman being torn in half by a centaur?

NOTES:

For Duo: Actor One would play Eliza, Bridge Club 2, Police Officer Actor Two would play Delores, Bridge Club 1, Dupree, Jail Cellmate

Eliza- early twenties, perky and confident, strong willed but naive and a little ditsy. Could have a Wisconsin/Minnesota accent.

Delores- Elderly, feisty, fiery intense eyes, maybe a horse Bronx accent

Dupree- Crazy eyes, monotone course voice, slow and deliberate phrasing
```

---

## IC-0617: A. I. Speechbot

- Title: A. I. Speechbot
- Author (byline): Forrest Musselman
- Work: A. I. Speechbot
- Publisher: Mushroom Cloud Press
- Publication date as stated: December 1, 2024
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 846
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
(Production Note: This piece can be performed in either the Humorous category or Duo Interpretation category in speech. Feel free to add or substitute any sounds, poses, and transitions that work best with your talents.)

ROB (typing noises) That’s it! That’s the last of the uploads.

GRACE (Clicking pen noises- scribbling on notepad) Perfect! We’ve done it, Bob! After years of hard-driven data, after years of attending countless speech tournaments, after years of soul-sucking boredom, we have created the perfect A I Speech Bot for the category Humorous Interpretation. (or Duo).

(Snap to A I Speech Bot standing in the perfect speech pose carrying a backpack.)

ROB This is amazing, Grace! I have to admit, when I first let you talk me into taking this job at National Speech Laboratories, I was highly skeptical. In fact, I didn’t like the idea at all. But you were right. Competitive Speech can be data driven and formulaic. And now with the unregulated insurgence of artificial intelligence, we have created the perfect forensic machine.

GRACE You know, it was only a matter of time before there was a speech bot. Look at the other speech categories. I mean, Extemp. Speaking is almost there already. Just a bunch of animatronic drones.

ROB No kidding. And Great Speeches? (Mimics in robot voice) I will walk here and recite speech. I will walk here and analyze speech. I will walk here and recite speech. I will walk here and analyze speech. I will walk here…

GRACE (Has had enough) Raaaaaaaahhhhhhhhhhb! I get it. Nothing but droids… all of them. That’s why in a world where competitive speech has been simplified to perfected repetition, we have created the ultimate weapon. Soon we will amass a speech team so perfect we will dominate our section, our state, nationals and then the world. I mean, look at her.

(Snap to A I Speech Bot standing in the perfect speech pose carrying a backpack.)

GRACE The brand new power suit. Could be black with a splash of color. Could be color with a splash of black. The hair tied back to show she means business. The shoes are stylish but made to move.

(Snap to A I Speech Bot standing in the perfect speech pose carrying a backpack.)

ROB The backpack full of the important necessities needed for the day. Mangled crumpled script on construction paper. The ever important water bottle for between rounds hydration. Various snacks, pills, and lotions. A notebook to scribble mindless doodles in during other competitor’s presentations. And most importantly, the lint roller.

(Snap to A I Speech Bot standing in the perfect speech pose, lint rolling herself in a

manic fashion, while making a lint rolling sound… of course.)

GRACE (Has had enough) Raaaaaaaahhhhhhhhhhb! What is she doing?

ROB (Typing manically) Sorry, just a little glitch with the lint roller. She appears to be spotless now.

(Snap to A.I. Speech Bot standing in perfect speech pose with backpack.)

(If you do an introduction, you can insert it here.)

GRACE Okay, let’s give this A.I. Speech Bot a test run. Let’s start with the snaps.

ROB You mean the pops?

GRACE No, I mean the snaps.

ROB Pops.

GRACE SNAPS!

ROB Okay. (typing) Here we go. We’ll start with the feet.

(Snap to A.I. Speech Bot standing in perfect speech pose. She suddenly moves feet in

and out quickly, but not moving the rest of her body.)

GRACE Great. Now add the rest of the standard characterization poses. Child with backpack.

(A.I. Speech Bot does. Feel free to insert or replace other stereotypical characters. )

GRACE Stupid bimbo.

(A.I. Speech Bot does.)

GRACE Maniacal evil person.

(A.I. Speech Bot does.)

GRACE Superhero.

(A.I. Speech Bot does.)

GRACE Old person

(A.I. Speech Bot does.)

GRACE Nerd.

(A.I. Speech Bot does.)

GRACE Run them again.

(A.I. Speech Bot runs all poses quickly as possible but can’t stop.)

GRACE (Has had enough) Raaaaaaaahhhhhhhhhhb! What is she doing? My god, you’re driving me to drink beer. (Makes sound of opening can. Chugs it.)

ROB Sorry. Just another glitch. (Typing) Nothing that SpeechWire can’t fix. Moving on to sound effects. Should we start with opening the door?

A.I. SPEECH BOT (Opens) Chicka- errrrr! (Closes) Errrr-chicka. (Opens) Chicka-errrr! (Closes) Errrr-chicka.

GRACE No. Why is she saying “chicka”? If you turn a door knob, it doesn’t go “chicka.” And why is the door squeaky? And why is she closing the door? You never close a door in speech.

ROB You’re right, dear. Let’s try this.

A.I. SPEECH BOT (Opens) Chicka- door. Chicka- door.

GRACE That’s worse.

A.I. SPEECH BOT (Mimes opening a door with no sound.)

GRACE Even worse. Go back to Chicka-door. Let’s move on. Cell phone.

(A.I. Speech Bot does. Again, feel free to insert or replace any sound effects you like.)

GRACE Turning pages in a book.

(A.I. Speech Bot does.)

GRACE Spray bottle.

(A.I. Speech Bot does.)

GRACE Shaving cream.

(A.I. Speech Bot does.)

GRACE Beat box.

(A.I. Speech Bot does.)

GRACE Run them again.

(A.I. Speech Bot runs all sounds quickly as possible but can’t stop. Throws some other

random sounds as well.)

GRACE (Has had enough) Raaaaaaaahhhhhhhhhhb! What is she doing? My god, you’re driving me to hard liquor. (Pops cork, makes glug, glug pouring sound, slams drink or make a martini.)

ROB Just a little snafu in the coding. (Typing) Already taken care of. Nothing to worry about.

GRACE Hmmm, I’m beginning to wonder. Let’s move on to transition sounds.

ROB Yes! I love transition sounds. What better way to show a passage of time or scene transition than through sound.

GRACE Exactly. What do we have?

(A. I. Bot makes weird breathing sound that starts quietly and then builds and stops abruptly.)

GRACE What was that?

(A. I. Bot makes weird breathing sound that starts quietly and then builds and stops abruptly.)

GRACE That’s the stupidest sound I’ve ever heard.

ROB But they’re all doing it.

GRACE What are we…sheep?

(A.I. Bot baas like a sheep.)

GRACE What else do we have?

(A.I. Bot goes through a litany of sounds and movements: spins, jumps, etc. Have fun!)

GRACE (Has had enough) Raaaaaaahhhhhhbbbbbbb!!! That’s it. I’ve heard enough. My god, you’re driving me smoke. (Goes through process of getting a cigarette, lighting it, smoking, flicking to ground, snuffing it out with the foot.)

ROB I think we’ve got it all covered now. Quick body transitions, appropriate sound effects and creative transitions.

GRACE Let’s now progress to the full speech performance.

ROB Yeah, about that.

GRACE Stop talking. Keep typing. Make sure she starts with the audience death stare.

ROB (Makes some typing noises)

(A. I. Bot stands at attention. She slowly surveys the audience with a confident death stare. She does a time transition sound, knocks on a door, opens a door and steps in. She selects a book, opens it, leafs through some pages. She attempts to speak. Nothing. She attempts to speak again. Nothing.)

GRACE Speech Bot! Why aren’t you speaking? Raaaaaaahhhhhhbbbbbbb!!!

ROB There isn’t a speech.

GRACE Why?

ROB We’ve spent all our time on everything else. I actually haven’t got to the speech yet. In fact, is that the whole point of speech? To speak?

GRACE What sort of blasphemy is this?

ROB I say down with the data. Why are we spending so much time on movements and sound effects and transitions when the real focus should be on the speech itself?

GRACE You’re fired. That is not the future of forensics. If you don’t have the right look and the right movements and sound effects, then what do you have?

ROB A speech. (Typing) That’s it. I’m pulling the plug. (More typing)

(A.I. Speech Bot starts shaking and making weird noises. She finally explodes.)

GRACE Raaaaaaahhhhhhbbbbbbb!!!

END
```

---

## IC-0618: D and Me

- Title: D and Me
- Author (byline): Steve DuBois
- Work: D and Me
- Publisher: Mushroom Cloud Press
- Publication date as stated: December 1, 2024
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: D, M
- Teaser before the introduction: No
- Spoken words (computed): 1345
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
[MACY is a college student. D is her roommate. At the opening, Macy is entering their shared apartment with a bag of groceries in each arm. D is on the couch in front of a gaming console.]

D: Behold! Our conquering hero returns. In this case, from the supermarket. What up, roomate?

M: Hey, D.

D: Need a hand with those?

M: That’d be good, thanks. [The two of them load the groceries into cabinets and the refrigerator.]

D: So. Macy. We still on for video games tonight?

M: Oh! That! Yeah. Uh…

D: The new expansion for Fashion Police just dropped. Hipster Hysteria! An entire community awash in skinny jeans and horn-rimmed glasses! Fashion crimes as far as the eye can see! Where is justice, Macy? Where. Is. Justice???

M: Actually, I was planning on going out. Trivia night at Mulligan’s with some friends from Sociology class.

D: Ah.

M: You can come.

D: It's not like you could leave me behind. [Pause] So…I guess this is the “girl gamer” thing again?

M: What do you mean?

D: A whole society of online bros, shaming and harassing every girl gamer they see.

M: Well…yeah, but…

D: And they've gotten into your head, haven't they? Because that’s the thing, Macy. We can ward oU whatever life throws at us–misogyny, cruelty, all of it–when it’s out in the open. But it’s when the bad guys get inside your head—when they get you feeling guilty, when they get you making excuses to do what they want, not what you want—that’s when they do real damage.

M: I…I mean…

D: Look at me, Macy. Are you sure you really want to go out tonight? Or are you letting a bunch of pimply-faced twerps chase you away from what you love?

M: Well, I mean…I’m not…I guess I’m not absolutely sure, but…well. When you put it that way…all right.

D: To phooey with trivia night! Mount up, OUicer Macy. Time to hit the virtual streets and bust us some fashion oUenders!

M: To the console!

D: Attagirl! [SCENE]

M: Jared asked me out!

D: Ooh.

M: God, D, a little more enthusiasm, wouldya? Jared asked me out! He's cute! He's nice!

D: He acts nice.

M: D, acting nice is what being nice is!

D: No, acting nice is how you get away with not being nice later. You don't need to worry about a dude who's openly a jerk. You know what to expect. It's the ones who act nice who you need to watch.

M: Oh, c'mon, D.

D: Think about it, Macy. If a guy's a superpredator, what better way to get girls than by being Mr. Supersweetie clean-cut boy-band guy?

M: Jared is not a superpredator! He's taking me to dinner!

D: You'll be the main course.

M: D!

D: Have fun riding in his trunk.

M: D!!

D: Macy, l'm just looking out for you, is all.

M: What are you, my mom?

D: You're mom can't be around 24-7, Macy. But I can. Look…how long have we been living together?

M: For…for as long as I can remember.

D: And we've talked about this. About you needing a man to justify your existence? You're enough, Macy. You don't need a man.

M: But I want a man! This one!

D: He wants your liver. With some fava beans and a nice chianti.

M: D!!!

D: We've discussed this. You valuing you for you, not for what others see in you. Working on yourself. Learning how to be alone. Look at me. [D grapes Macy by the shoulders.] Look at me, Macy. If he cares about you…if he truly cares about you…he'll be willing to wait, right? He'll be willing to work for it?

M: I…I suppose…

D: You don't need to dive into this thing face-first, like some starry-eyed schoolgirl. You're the cool girl, Macy. You're self-suUicient. You are a strong black woman who don't need no man!

M: I'm not black, D.

D: Metaphorically, I mean. [Pause] Play it cool, Macy. Make him wait. You know I'm right about this.

M: I mean…I guess…

D: Stay in with me tonight. We'll watch Dragonseed on Netflix.

M: I don't…I don't want…

D: Sure you do. Fools rush in. Be smart. Stay safe. Make him work.

M: All…all right, D. All right. I'll tell him no. We'll stay in and watch Netflix.

D: Attagirl. Proud of you, Macy.

M: Yeah. Sure, D. Sure.

[SCENE]

[D and Macy are sitting on the couch, staring numbly into the distance. Macy stands.]

D: Where ya goin'?

M: Out.

D: [Without looking up] Spider.

M: What?

D: Over there by the door.

M: Ew!

D: Biiiig spider. [A long pause.]

M: Maybe if I…just sorta slowly scootch past it…

D: It's reeeeeally pretty close to the door, Macy.

M: Ew. Ew.

D: Yep. [pause] Wanna stare at the wall some more?

M: Yeah. Sure. Okay.

D: Attagirl.

[SCENE]

D: So this is how it is, huh, Macy? I let you leave the apartment, and you come back, and you bring drugs into our home.

M: They're not drugs, D. I have a prescription.

D: From that quack Dr. Schwartz. They're drugs, Macy. After all we've been through together, you've decided you can't stand up on your own two feet, and you're going to become dependent on drugs.

M: They're just pills.

D: Give me those. [Macy hands her a vial of pills. D reads the label.]

D: "Buproprion. 10 milligrams. Take once daily, for…depression." [A long pause. D stares Macy down.]

D: For D-pression. You're trying to get rid of me.

M: I…just need you to be a little quieter for a while.

D: You want me gone.

M: What I want, D, is…

D: All I've done for you, and you…

M: YES! GODDAMNIT, D! I WANT YOU GONE! BECAUSE YOU SUCK! [A long pause]

D: Uh…rude!

M: Never a moment's peace, for years! All the excuses, D! All the opportunities I've lost, because you wouldn't let me leave the apartment! Because I had cramps! Because of climate change! Because there might be a guy hiding under my car with a razor blade, waiting to slash my ankle!

D: I'm trying to keep you safe, Macy.

M: I can't live my life wrapped in bubble wrap! I have to get out there, D! Not every night, but at least some of the time! I need to have a life! I need to have fun!

D: We have fun.

M: We have numb, D. Numb is not fun! I'm tired of living under anesthesia!

D: Beats the hell out of getting hurt.

M: NO! IT DOESN'T! Life is pain! And pleasure! And sorrow! And joy! And frustration, and passion, and confusion, and…all the other shuns! I WANT A LIFE! Bitter, and sweet, and wonderful, and horrible! I want it all! A ship in harbor is safe, D. But that's not what ships are for!

D: You stole that from somebody.

M: It's a quote from John A. Shedd.

D: Christ. I knew letting you go to English class was a mistake.

M: You don't LET me anything, D. You don't have a say. Not anymore. I'm gonna take a pill…

D: Druggie.

M: …and I'm gonna head out that door, and I'm gonna leave you behind.

D: You're not gonna leave me behind, Macy. Because I am you.

M: You're not me, D.

D: I AM YOU, Macy Jane McAllister. I am the harsh truths you refuse to face, I am the only sensible instincts you possess, and I am the face you have been showing the world since you were eleven years old. I'm the you Jared cares about. Will he still care when I'm gone? Who would you even be, without me?

M: I don't know. I honestly don't know, D. But I'm ready to find out.

D: I'm not leaving. You know that, right? You might push me back for a while with a pill, but you and I will always be roommates. I'm not leaving.

M: Maybe you're not. But I am. [She heads for the door]

D: Don't you dare, Macy. Don't you dare walk out that door. I swear to God, you'll regret it.

M: Maybe. But I'm going. [She takes a deep breath, turns the knob, and steps through the door. As she does, D fades into the background. Macy exhales slowly, a massive weight having been lifted]

M: Attagirl.
```

---

## IC-0619: Fairytale Feud

- Title: Fairytale Feud
- Author (byline): Clara Folz & Lily Heckert
- Work: Fairytale Feud
- Publisher: Mushroom Cloud Press
- Publication date as stated: December 1, 2024
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR #1, NARRATOR #2, ROSE RED, SNOW WHITE, ROSE, SNOW
- Teaser before the introduction: No
- Spoken words (computed): 1645
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
Narrator #1 (F): She is a prim and proper narrator, just like typical fairy-tale narrators. A ‘fancy’ accent is encouraged.

Narrator #2 (F): She is less traditional than Narrator #1, preferring strong characters like Rose Red.

Snow White (As told by Narrator #1): She is polite and kind. She is the picture of a perfect maiden.

Rose Red (As told by Narrator #1): She is rude and inconsiderate. She only cares about herself.

Snow White (As told by Narrator #2): She thinks very highly of herself and expects the world to revolve around her.

Rose Red (As told by Narrator #2): She is very stoic and brave. She cares a lot about her sister, no matter how rude she is.

Author’s Note: The person who plays Narrator #1 should also play Rose Red. The person who plays Narrator #2 should also play Snow White.

Fairytale Feud

NARRATOR #1: Good evening, dearest reader. I am the Narrator, and I am here to tell you a magnificent tale of losses, fear, and love. This is the story of Snow White.

NARRATOR #2: Um, yawn. Don’t you mean the story of Rose Red? Snow White’s just the one who got all the attention.

NARRATOR #1: Rose Red is… quite irrelevant. I doubt the reader has even heard of her.

NARRATOR #2: Well, that’s my point exactly. How do you expect them to know about her when she’s so grossly overshadowed by her snooty younger sister?

NARRATOR #1: Hah! Snooty, you say? Snow White was the image of grace and purity. Rose, on the other hand, was not ladylike at all!

NARRATOR #2: Of course. Just because she didn’t just wait around for some prince to save her you brush her off as unladylike.

NARRATOR #1: My apologies, dearest reader, for my younger colleague’s outburst. You don’t really want to hear about Rose, do you?

NARRATOR #2: Sure they do, see?

NARRATOR #1: Alright... If it’s what the reader wants to hear. Once upon a time- (In the Woods)

ROSE RED: Ugh, I can’t believe our parents just dropped dead and left us with this piece of work they call the queen.

SNOW WHITE: Oh, dearest Rose, you mustn’t speak of her that way!

ROSE: Whatever.

SNOW: I think it would be best if we tried our hardest to be meek and kind to whoever comes our way, so that we may enchant them, and-

ROSE: …right. You do that, I’m gonna go flirt with the huntsman.

SNOW: Gasp! (say “gasp” aloud) How can you say that Rose! He is a roguish man!

ROSE: Um he can be roguish with me as much as he likes!

SNOW: Dearest sister, what a vulgar thing to say?!

ROSE: Oh, save it. (Transition Back to Narrators)

NARRATOR #1: Snow and Rose are chased out by the huntsman, much to the infatuated Rose’s dismay. They come upon a small cottage and rest in the miniature beds they find in them. Let us observe as they are woken up by the petite forest dwellers who reside here.

NARRATOR #2: You mean dwarves?

NARRATOR #1: Hey, my story still! (Dwarves House)

SNOW: (Delicate singing snoring)

ROSE: (Obnoxious snoring)

SNOW: (Slowly wakes up) Oh, hello sweet little creatures! I’m sorry my sister and I have infringed upon you like this! (Pause for Dwarves' response) Oh, I’m so glad you don’t mind! Wake up dearest sister and meet our lovely new friends!

ROSE: (snoring cuts off) Huh- What? Ah! What are you garden gnomes doing here? I thought I had seen the last of you at that pie-eating contest.

SNOW: Oh, you never told me you competed! I would have loved to spend the day with-

ROSE: Anyway, I can’t stay here with these guys. Me and Grumpy have too much… history, as you might say. I know a place near here I could go, but I think it’s a little too rough-and-tumbly for a little princess like you though.

SNOW: If you think that is what’s best, dearest sister. (Sniffling) I just- What if we never see each other again?

ROSE: I’ll be better off then. Goodbye. (Snow by herself)

SNOW: How can I express my true sorrows? Perhaps a longing ballad? (humming) Someday my prince will come…

ROSE: Shut up! (Back to Narrator #1)

NARRATOR #1: Rose and Snow are separated for months. And yet, Snow White is ever forgiving and invites her falsely beloved sister to her wedding. Let us join them as they reunite! (In front of a castle)

SNOW: Oh, I am so glad you came! I’ve been excited for you to meet my fiance… (both say fiance at the same time)

ROSE: Your fiance. Right. I find it ironic that someone like you goes off and has a shotgun wedding with some guy who kissed her corpse.

SNOW: Shotgun? No, I assure you that our relationship has been nothing but pure. He is simply my true love!

ROSE: Right. Well, let me tell you something right now. You can pretend to be all sweet and loving, but I know you’re nothing but a stuck-up snob. And you haven’t made any effort at all to talk to me ever since you stayed with those dwarves. And yet you expect me to come crawling back at your stupid fairy-tale wedding!

SNOW: Stop it! Sister, I’m afraid this has gone far enough! I order you to leave the castle grounds.

ROSE: What?! You can’t do that to me!

SNOW: Leave or you will be escorted out by the guards!

ROSE: (Being dragged away) Ahh! Let go of me! You’ll regret this!!! (Transition back to Narrators)

NARRATOR #1: And here our story comes to a close. Snow White bravely faced down her wicked sister and lived happily ever after. Rose, on the other hand, lived the rest of her treasonous life as an outcast and a hag. Now, do you see what I am talking about?

NARRATOR #2: Now wait a minute! That is nowhere near what happened. Let me tell you what really happened. Please, reader?

NARRATOR #1: Fine. But, I’m sure the truth will be clear in the end.

NARRATOR #2: Once upon a time- (In the woods somewhere)

SNOW: I can’t believe that-

ROSE: Our parents died? I know, but they died doing what they loved. It’ll be okay-

SNOW: No, not that. What I meant was that I am forced to work the castle grounds like a common peasant girl!

ROSE: Eh, could be worse. I don’t really mind.

SNOW: Of course, you would like it, simple Rose. While you work on your peasant duties, I’ll go and wait for a prince to arrive and save me, as a true princess does.

ROSE: Uh, no. You will not leave me cleaning here while you get to sit around!

SNOW: Nonsense! It is my duty as the fair sister to be a ray of beauty that calls forth my true love to save me from this mess!

ROSE: My dear sister, love should be the last thing on your mind right now. Our parents just died, remember?

SNOW: Hmph! Don’t lecture me about love! I saw you making googly eyes at that foul huntsman character!

ROSE: I was not! (sigh) Isn’t he dreamy, though?

SNOW: (to herself) I can’t believe I’m being forced to keep such disgusting company.

ROSE: I’m right here, you know. (Back to Narrators)

NARRATOR #2: And would ya look at that? Isn’t Snow White the snobbiest-

NARRATOR #1: A-hEM?

NARRATOR #2: Right. Well, anyway, they get chased out because Miss Snow has to go around talking about how fair she is and gets the queen all mad. They find this abandoned house in the woods and stay there for the night and wake up to the dwarves. Shall we? (Dwarves cottage)

SNOW: (Snoring but annoyingly)

ROSE: (sleeping normally)

SNOW: (waking up) What the- How rude of you to wake me from my beauty sleep! I need at least 8 hours to maintain my perfect complexion and you’ve cut me short by 15 minutes! (pause for dwarves response) What do you mean, this is your house?! Do you know who you are speaking to?

ROSE: (waking) What going on? Hey wait a second, I know you! (to Snow) Yeah, I met them at the annual pie-eating contest!

SNOW: Pie-eating? I must have underestimated what horrid company you keep.

ROSE: Sorry guys, ignore her. How can we pay you back?

SNOW: Us pay them back?! They should be paying me! I have blessed their little meaningless lives with my presence!

ROSE: Again, so sorry. We better be off now!

SNOW: Hmph! I’m not going anywhere with you! I’m staying put. These ugly little forest thingies will see to my safety here.

ROSE: Are you out of your mind?! I’m not leaving you here alone with seven men!

SNOW: How dare you suggest that I would let myself be taken advantage of!

ROSE: That’s not how it- (sigh) I can sense this is not an argument I can win. I’m leaving. (Back to Narrator #2)

NARRATOR #2: So Snow is stubborn and stays with the dwarves, she gets kissed in her coffin, and Rose receives an invitation to the wedding. She hopes that the months away might have changed her snobby younger sister, but it is clear not much has changed…

(In front of a castle)

ROSE: Hey, Snow! Long time no-

SNOW: Eeek! Guards, get this nasty-looking rat creature away from me!

ROSE: Really? Woooow.

SNOW: Oh, I know you. I can’t believe I didn’t recognize your signature stench.

ROSE: Look, why bother inviting me if you’re just going to insult me the whole time?

SNOW: I wanted to prove myself right. Look at all that I have! A kingdom, a prince, I am adored by all!

ROSE: …Snow, are you happy?

SNOW: I- well… How could I not be? I have the prince!

ROSE: Alright. Well, I wish you a good marriage then. I don’t have the energy to argue with you about who’s right anymore. Goodbye. (Back to Narrators)

NARRATOR #2: Rose took the high ground and didn’t just throw herself at the first man passing by! Now, do you see?

NARRATOR #1: Hah! Simply ridiculous. The way you twisted around Snow’s character was abominable!

NARRATOR #2: Oh, you wanna talk about twisting things?!

NARRATOR #1: I can’t believe you. You are an idiotic, ignorant, unlovable little ankle-biter! I should teach you a lesson so you will shut up and STOP! NARRATOR #2: Yada yada yada. All you do is hurl accusations around and act like you’re a little fancypants princess like your beloved Snow White. I wish you would just STOP! (Said at the same time both ending and stopping at the same time) (Both Stop)

NARRATOR #2: Look at us! What are we doing?!

NARRATOR #1: I haven’t a clue what you are doing, but I am making a point!

NARRATOR #2: Look, we don’t have to agree, but I’m sure arguing like children is not going to prove either of our points. Now, why don’t we just… have a truce?

NARRATOR #1: I guess in this one instance you are correct. (They shake hands.) Would you like an apple? As a sign of our… mutual respect.

NARRATOR #2: Sure, thanks! (bite) Wait a minute- (Faint)

NARRATOR #1: (Evil Chuckle) And Snow White lived happily ever after!
```

---

## IC-0620: Going Down

- Title: Going Down
- Author (byline): Frank Smith
- Work: Going Down
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2982
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
SCENE I

High-Rise Apartment—24th Floor Hallway.

(Bare and anodyne, like a hotel hallway. Two main elevators sit in a central alcove.)

MARAH, CASSIDY, HELEN.

(MARAH (31), brisk walk that won’t help her escape herself, emerges from her apartment in scrubs. A moment later, at the opposite end of the hall, CASSIDY (33), confident she has a point, but usually does, emerges from her own apartment in athletic gear. The women sigh when they lay eyes on each other, before beginning the awkward walk to their same destination: the elevators. Cassidy hits the elevator button first. Marah stares at her a long beat before…) CASSIDY. (Overly pleasant.) Good Morning, Marah! MARAH. (Mumbled.) G’Morn, Cass. CASSIDY. Sorry? MARAH. Oh, I was mumbling. See, I didn’t get the best night’s sleep— CASSIDY. (After a guttural moan.) Starting early today! MARAH. –because, not sure if you knew, but your party was loud. Verging on cacophonic. CASSIDY. What does “cacophonic” mean? MARAH. Reprehensibly loud. CASSIDY. What does “reprehensibly” mean? (Before Marah starts.) Doesn’t matter. That’s why I left a bottle of wine outside your door, to apologize for the noise— MARAH. A bottle of wine that I broke…while opening my door to complain about said nose. CASSIDY. You do have an aggressive door swing. MARAH. I do not! I open doors gently, and compassionately. CASSIDY. Mmhmm. MARAH. Look, Cassidy, I don’t know if you know, but I’m a surgeon at UChicago Medicine— CASSIDY. I did not know. Tell me a tenth time. MARAH. –and as a result, I kind of need sleep, so I don’t amputate the wrong arm by mistake. I’d get sued for that. I doubt you’d get sued for, what… serving the wrong wine vintage? CASSIDY. Okay, a) not a bartender, b) I still know my vintages.

MARAH. If that’s true, why did you leave me a bottle of skunk wine?
CASSIDY. (Realizing it’s not worth it.) I’ll be quieter next time.
MARAH. Good. Because I’m getting up early to cut people open, while you’re getting up early
to…get swoll?
CASSIDY. Nice. Turning fitness into a weakness.
MARAH. Anywho! I’m glad we could reach an understanding about the noise.
CASSIDY. Yeah. Sure. But just so you know: my work matters too.
MARAH. Oh, you’re one those? “All work matters?”
CASSIDY. (Rolls her eyes and presses the elevator button again.) Where is the…

(From around the corner strolls HELEN (71), small stature, immovable presence, holding a
piece of paper. She slaps it onto the elevator door.)
HELEN. Morning, ladies.
CASSIDY. (Overly pleasant.) Well, if it isn’t the best landlady I’ve ever met, Helen—
HELEN. No one complained last night.
CASSIDY. (Dropping the act.) Phew.
MARAH. Excuse me! I most certainly complained.
HELEN. You did? Huh. Were you doing that high-pitched fisherman’s wife scream you do? At
my age, I can’t hear that frequency anymore.
MARAH. (Extremely high-pitched.) I do not do a fisherman’s wife scream—
HELEN. (With a shrug.) Yep. Dog whistle.

(In a huff, Marah steps past Helen to reads the sign on the elevator.) MARAH. “Out of order!” Helen. We’re on the 24th floor? How can the elevator be out of order!? HELEN. Well, now, it all started 20 years ago, when a young witch, eager to enact her first curse… (Off Marah’s intent listening.) It’s a machine! It broke down. MARAH. Well, when’s it going to be fixed? I have to go to work. I cut people for a living!

HELEN. I still do that from time to time. (Darkly.) When they owe me. (Jovial.) I’m just joking. I’m a landlady, not a mob boss! (Darkly.) Until you cross me. CASSIDY. (Overly pleasant.) FYI: I’m up to date on rent! HELEN. Oh, I know! (Darkly.) I always know. (Whistles and starts off.) MARAH. Helen, stop! How am I going to get downstairs? HELEN. Well, now, let’s see. I could drill a hole in this floor, then drill a hole in that floor, and so on and so on, buy you a parachute, and then— (Off Marah’s intent listening.) Walk, you loon! Geez. And you’re a doctor? No wonder cancer hasn’t been cured. (She disappears.) MARAH. Helen. Helen! UGH. How am I supposed to walk down 24 flights of stairs? I can’t sweat before work. The gloves and mask will slip off my body, and then I’ll get sick and die! (Extremely high-pitched.) I just don’t understand how she could do this to— CASSIDY. (Covering her ears.) Mmhmm. MARAH. (Huffs for a minute, before calming down.) I guess we’re walking. You want to go first, get a head start? CASSIDY. Why? MARAH. So we don’t have to walk together. CASSIDY. Oh, grow up. We both have places to be. Let’s just go. (Opens the stairwell door.) MARAH. (Seeing Cassidy holding the door, grudgingly walks through it.) Thanks. But you didn’t have to do that. There’s no word for female chivalry. CASSIDY. There is. It’s called sexism.

SCENE II

High-Rise Apartment—24th Floor Stairwell.

(In sharp contrast to the hallway: dingy and musty.)

MARAH, CASSIDY, RAINY, ABNER.

(Marah is a few steps ahead of Cassidy as they begin their trek down the stairs together.) MARAH. UGH. It’s only been one floor, and I’m already exhausted. CASSIDY. Stop talking. Saves breath.

MARAH. You must be having fun. You wanted to get in a workout.
CASSIDY. (Sarcastic.) Yeah. I’m having a blast.
MARAH. Why wouldn’t you be? Exercise by day, party by night, unclear on your afternoons…
CASSIDY. Marah. Last night wasn’t a party. I was hosting a—

(The door bursts open and out flies RAINY (23), sweet little face, aggressively friendly.) RAINY. Cass! OMG, so glad I found you. Last night was so fun! I got way, way too drunk.

(Marah gives a smug look to Cassidy.)
CASSIDY. Again. It was not a party. It was a function.
RAINY. Emphasis on FUN! Not on CTION.
MARAH. What would that even mean?
RAINY. IDK! I find English is less something you know and more something you feel, yeah?
MARAH. No, that’s not right.
RAINY. But do you know that? Or do you feel that? (With Marah stunned silent, Rainy pivots to
Cassidy.) So, Cass: that red wine you served was delish.
CASSIDY. Glad you liked it.
MARAH. Do you have any food leftover?
CASSIDY. I don’t.
MARAH. Boo! I would’ve loved some. Those appetizers, they were too good, and I am too short
on rent this month, so free food is literally keeping me alive RN. Completely literally, as in, like,
I would die without it!
CASSIDY. That’s concerning. I could…have you over for dinner?
RAINY. You so don’t have to…but thank God! I’m lucky to live near you. Your parties are just
the best! And you throw so many: parties at your apartment, parties on the rooftop, parties in the
sub-basement. Boy, that was a weird one. K, let me know what time for dinner, bye! (She goes.)
MARAH. I just pretend to be asleep when she knocks.
CASSIDY. Guess that’s why she’s my friend, and you’re not.

MARAH. (A bit hurt.) Yeah. No, we’re not. I mean, I’ve never had a female friend. So…

(Hustles ahead of Cassidy down the stairs.) CASSIDY. (Standing still, sighs and calls after Marah.) Look. I’m not some dumb party girl. (She watches Marah slow, but not stop.) I’m the executive director for a charity. MARAH. What type of charity? CASSIDY. The type that donates to tumor operations and research. MARAH. Really! CASSIDY. Yes. It’s called “Tumor Has It.” All proceeds go to local hospitals. That party you heard on the roof last night was a fundraiser. So, in a way, the reason you have work at all this morning, working with tumors…is thanks to me. (Sarcastic.) Wait. What do you do again? MARAH. Actually, I don’t usually do tumors. The fratty doctors in the OR won’t let me. CASSIDY. Wait. They can do that? MARAH. I’m the youngest one there, and the only woman, so…yeah. They get all the fun stuff – hearts, brains, and for some reason, boobs – while I’m stuck taking out things like moles, and tonsils, and appendixes. CASSIDY. So, your job is removing things from people…that could just as easily stay inside those people. MARAH. That is a rudely-worded but mostly-accurate version of my life, yes. You figured it out! I don’t matter to anyone. (Sighs and leans against the railing. Almost seems like she’ll cry.)

(Cassidy catches up at last. Before she can say anything reassuring, a man steps out from his floor and walks up to them: ABNER (65), jolly, white hair, will never end the conversation first.) ABNER. Dr. Marah! Did you know the elevator’s out? MARAH. (Wiping sweat from her forehead.) Yes, Abner, I did. ABNER. But the good news is: I ran into you! I’ve been meaning to talk to you, because I’m having a bit of a medical problem. And see, with me being a bachelor and all, it’s not every day I have someone to check suspicious bumps or bruises on my body, not to mention unusual odors— MARAH. Abner, I kind of have to get to work. I don’t think I can— ABNER. Now, I know you don’t like it when people show you stuff on their bodies— MARAH. Thank you.

ABNER. So I’m just going to describe it to you in detail. There’s this round, shall we say... pustule on my stomach. When I touch it, it jiggles, like there’s some sort of fluid in it. And when I bend over and put my ear next to it, I sort of can hear the ocean. Also, it’s a green color. Let’s call it a…rotting leaf. So. What do you think it is? MARAH. I can’t know without looking at it. (Before he can respond.) I’m not looking at it. ABNER. I understand. No such thing as a free lunch. But we’re both here. And I’m more than happy to barter. So. You need your taxes done? I’m a CPA. MARAH. No, Abner, I don’t— ABNER. Oh, you’ve been cheating Uncle Sam. That’s okay. I can be creative. One time, I said a woman had 5 dependents. Know what they were? Nutcrackers. That she named. And sponge-bathed. (After an awkwardly long silence.) They were named after her dead Dalmatians— MARAH. Okay, just show me!

(Abner lifts up his shirt. The cyst is as gross as described. Marah makes a face before measuring its proportions with her fingers and staring closely. Cassidy watches the exam with fascination.) MARAH. Looks benign. But you need to get it removed before you feel any abdominal pain. ABNER. Thank you, Dr. Marah! Your exemptions for being a single Mom WINK and home-owner WINK WINK are as good as filed! (He skips off happily.)

(Once he’s out of sight, Marah shakes her head and laughs. Cassidy walks over and puts a hand on Marah’s shoulder.) CASSIDY. Hey. Seems like you mattered to him. MARAH. That cyst wasn’t going to kill him. Just make him even more unappealing. CASSIDY. If I can give you some advice? Woman-to-woman? You’re letting the guys at work get inside your head. Don’t. You’re clearly a capable doctor. Even for a woman. I’m kidding. No qualification needed. MARAH. (Smiles, before checking her watch.) I’m even more capable when I’m actually at the office, so…I should get a move on. CASSIDY. (Thinking.) You know, it’s been a few minutes. Should we see if the elevator works? MARAH. Not on this floor! Abner might show me his feet next. CASSIDY. Fine, let’s get off here. (Cassidy holds open the door for Marah, who’s reluctant to go first.) Yes, yes. Sexism. We did this already. Go! (Cassidy walks out after Marah.)

SCENE III

High-Rise Apartment—16th Floor Hallway.

(Visibly dirtier than Marah and Cassidy’s floor. Both elevators bear an “Out of Order” sign.)

MARAH, CASSIDY, ERIK.

(Marah strides up to the elevator and groans when she sees the “Out of Order” sign.) MARAH. No! This is not my day.

(Marah and Cassidy cry out in surprise as ERIK (45), has all the manic energy of a man on the
run, pops up from out of nowhere.)
ERIK. ‘Sup, ladies. I’m dating a woman who lives on this floor. Alice. You know her?
MARAH. No. Not all women know each other.
ERIK. I know…there’s no such thing as female geography. Or female anatomy.
MARAH. No, that’s not right.
ERIK. How would you know?
CASSIDY. You mean besides not being an idiot.
MARAH. I’m a doctor.
ERIK. Nuh-uh!
CASSIDY. …Yes?
ERIK. Okay, prove it.
MARAH. Prove to you that I’m a doctor?
ERIK. Yeah. Do that.
MARAH. (Assessing.) Your cranial circumference is below average. Suggests below average IQ.
ERIK. Whoa! You are a doctor. Righteous. So, I have a question about Alice—
MARAH. Again, whom we do not know.
ERIK. Look, I know you don’t know her know her—
CASSIDY. Do you know that know that?

ERIK. But, as a woman who also lives in this building: what do you think she’s thinking? She seems to like me, but she won’t actually say it. You’re both ladies. Help me figure this one out? MARAH. While we are both female humans— ERIK. Exactly! CASSIDY. Honestly? I’m not the one to ask about this. I just got out of a relationship. ERIK. (Interest piqued.) Oh? CASSIDY. Not an invitation. ERIK. (Let down.) Oh. CASSIDY. And it was my fault things ended, so…yeah. Not the best person to speak for women. MARAH. Also, asking one woman to speak for all women is insulting on its face, but…you know. (She looks away from Erik, who indeed looks confused.) Cass, how was it your fault? CASSIDY. (After a heavy sigh.) I spent way, way too much time…at work. MARAH. …at your charity. So, in other words: you were too good a person. CASSIDY. I didn’t put it that way on purpose… MARAH. UGH. I guess you’re just always going to be better than me. Even when you get dumped, you make it work! ERIK. (Titillated.) Amen, sister.

(Marah takes off downstairs alone. Cassidy moves to follow her, when Erik puts his hand out.) ERIK. Hey. It’s a long walk downstairs…and only a short walk to Alice’s.

(Cassidy, creeped beyond belief, leaves the floor without saying another word.)

SCENE IV

High-Rise Apartment—16th Floor Stairwell.

(Cleaner and cleaner the further down they descend.)

MARAH, CASSIDY.

(Marah starts off a full staircase ahead of Cassidy. Cassidy hurries to catch up to her, almost falling a few times in her haste, but consistently managing to right herself.)

CASSIDY. Marah! (Near-fall.) Wait. (And another.) Marah! (Finally catches up to Marah.) MARAH. UGH. And you’re graceful? Why do I even exist!? CASSIDY. Stop. Do you really feel this competitive with me just because I’m a woman? MARAH. You first! CASSIDY. What? MARAH. Every opportunity you get, you find a subtle way to one-up me. (Imitating Cassidy.) I’m Cassidy. I work for a charity. I got broken up with for being a good person. I’m a D-Cup. CASSIDY. I never said I was a D-Cup. MARAH. Am I wrong? (Ashamed, Cassidy shakes her head no.) See? You’re obviously just as insecure as me. But you express it through…extraordinary confidence. It’s very confusing! You’re like, a puzzle…wrapped in a bitch!!! CASSIDY. I’m not some…bitch puzzle. But okay. Fine. I am…a bit insecure around you. MARAH. (Genuinely surprised.) You are? I was just saying that to try to win the argument. CASSIDY. Yes. You, well, all doctors…make me feel that way. I tried to get into med school… several times. After my Dad got a brain tumor, I applied…wrote a heartfelt essay that clearly did not land with the admissions board…but once I started working in charity, I realized I could help another way. I do really great work. But sometimes, I still can’t help but feel…I let him down. MARAH. You didn’t. (Stepping closer to Cassidy.) And thank you, for being so vulnerable. (After an awkward pause.) So…should we kiss? CASSIDY. What? No. Why would you think I was angling for that? MARAH. Sorry! I’m not great with social cues. One of my many flaws, apparently!

SCENE IV

High-Rise Apartment—1st Floor Lobby.

(Shockingly well-maintained considering how every other part of this building has looked.)

MARAH, CASSIDY, RAINY, ABNER, ERIK, HELEN.

(Marah and Cassidy stagger out of the stairwell, sweaty and bedraggled. They stand out in the otherwise pristine lobby.) MARAH. I’m never walking that much again. If the building’s on fire, I’ll just jump, and pray.

CASSIDY. Can you prescribe prayer? MARAH. In very low doses.

(An elevator door DINGS. Marah and Cassidy look up in shock. They stand before the elevators,
as out walk Rainy and Abner.)
CASSIDY. (To Marah.) What the—they took the elevator!
RAINY. Oh, hey Cass! Weird coinc: I was just talking about you with (re: Abner) him!
ABNER. Hello again, ladies.
RAINY. He told me your friend is a doctor? Which is such a coincidence, because LOL, I have,
like, zero health insurance!
MARAH. Then I probably couldn’t see you as a patient.
RAINY. Even if I said pretty please? And if I don’t get a physical, I’ll die? Completely literally,
like, I would die without it!
ABNER. Have a heart, Dr. Marah. Help her out like you did me? I’ll do your friend’s taxes too,
if it helps.
MARAH. Why would I trade my labor for her benefit?
RAINY. Friendship!
CASSIDY. Sounds more like exploitation.
RAINY. Right. Friendship!
ABNER. Help her, Dr. Marah. She’s too young to die. (Wistful.) Like I once was…

(DING. Erik emerges from the other elevator. He makes a beeline for Rainy.) ERIK. Ooh, another lady! Say, do you know Alice? Lives in your building, is a woman? I can— MARAH AND CASSIDY. Everyone, shut up!!! (The room goes silent. They look at each other, impressed by the power of their unity.) MARAH. No, actually, un-shut up. CASSIDY. When did the elevator start working?

(Helen emerges triumphantly through the front doors.)

HELEN. About two minutes after I saw you. MARAH. Helen! We just walked down 24 flights of stairs because we thought it was broken. Why didn’t you come tell us it was fixed? HELEN. Well, now, gee, I sent out the homing signal, and when that didn’t work, I summoned a flock of pigeons to spread word that— (Off Marah’s intent listening.) You were gone already! How was I supposed to know where you went? I don’t track my tenants. (Darkly.) Anymore. CASSIDY. So. Does that mean everything in the building is working again? HELEN. Well…not exactly. In turning the elevators back on, I may, may have accidentally knocked out the heat. So…you guys might want to find people to bundle up with for warmth.

(Rainy and Erik look at each other, shrug, and walk out the front door, arm-in-arm. Rainy considers Abner only a moment. Seeing he’s alone, he sighs, and rides the elevator back up.) HELEN. And I’m guessing you two ladies won’t want to be roommates, given your (re: Marah) many previous complaints about (re: Cassidy) this one. MARAH. I thought you said you couldn’t hear my fish-voice! HELEN. I’m talking about the thousand written complaints. MARAH. (Registering Cassidy’s surprise.) I don’t recall writing that many complaints… HELEN. Oh, you sure did. About the parties. The noise. Your loneliness. Your jealousy. Plus, your confusing attraction to— MARAH. Okay, thanks, Helen! We’ll figure something out without your help! As always! HELEN. Hey, what’s a landlady for, if not to make money off her land, and…that’s it. (She whistles her way into the elevator. It doesn’t go up right away.) Someone should really fix these door close buttons. Oh wait, that’d be me. Eh, I can live with it. (The doors finally close.) CASSIDY. (To Marah.) Quite the list of complaints. MARAH. I’m sorry! It was before I really knew you. CASSIDY. And you think after 24 flights of stairs, you really know me? MARAH. Better than before! I used to think you were a puzzle wrapped in a bitch. Now, I know: you’re a bitch wrapped in a puzzle. CASSIDY. (With a smirk.) Is that your way of asking to be roommies till the heat’s back on?

MARAH. Come over. We can have a slumber party! A quiet slumber party. CASSIDY. Yeah. We could stay at your place. Or. We could stay at mine. Since it’s so much bigger than— MARAH. Yeah, you remember that topping thing, you weren’t going to do anymore? CASSIDY. Sorry. Habit. (Beat.) I’m not wrong. MARAH. Okay, well, thank you. I’d love to stay over at my new friend’s place. (As Cassidy smiles and presses the elevator button, Marah looks over at her.) So…should we kiss? CASSIDY. What? No. Why do you keep thinking that? MARAH. Social cues. Learning them!

(The elevator doesn’t come right away.) CASSIDY. I think I might head back up, actually. Work out a little bit later. See you tonight? MARAH. No. I’m calling in sick today. Maybe a day without me will make the OR bros realize how much they need me after all. Or they fire me, and I find a better job. Or a worse one. CASSIDY. Those are all the possibilities. MARAH. So, I’m heading back up with you! (Beat.) You, umm…want to take the stairs? CASSIDY. (With a smile.) Definitely.

THE END.
```

---

## IC-0621: Hashtag

- Title: Hashtag
- Author (byline): Steve DuBois
- Work: Hashtag
- Publisher: Mushroom Cloud Press
- Publication date as stated: December 11, 2023
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NANCY, MEGAN
- Teaser before the introduction: No
- Spoken words (computed): 1441
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
[Backstage at VidCon. MEGAN is a teenage internet personality: attractive, poised, and capable of being, at the drop of a hat, whomever her fans want her to be. Her social media account ManyManyMegans has introduced millions of fans to her and to her split personalities. NANCY is a fangirl. About the same age as Megan, she is carrying a few extra pounds, a tote bag, and a whole lot of invisible baggage.]

NANCY: Megan?

MEGAN: Yes?

NANCY: Megan! Oh my God, it's YOU! Hashtag ManyManyMegans!

MEGAN: It's…me!

NANCY: Oh my God, you are totally my favorite multiple personality account. I've followed them all…the Brittany System, Adeline And Friends, even Group-O-Gretchens. But you are the BEST. I'm Nancy, by the way.

MEGAN: Oh, thank you…Nancy. Um…how did you…

NANCY: Your alters…oh. my. God. I mean, they've all…they've all been through so much. You've all of you been so brave. I mean, Candice, with her Tourettes…hi, Candice! [Megan's posture shifts slightly, and she adopts a facial tic. Each of her "alters" displays an obvious physical distinction from the others. It is, for lack of a better word, "interpy".]

MEGAN: Hi there!

NANCY: And Amy, with her eating disorder…

MEGAN: Uh…hello. How did you…

NANCY: And Mags, the oppositional-defiant one! "The girl who puts the 'dis' in 'disassociative identity disorder'"!

MEGAN: Yo!

NANCY: And Betty. Betty's my favorite! Bipolar Betty.

MEGAN: How did you get backstage?

NANCY: Huh?

MEGAN: I mean…don't get me wrong, it's always great to meet a fan, especially one who's so…dedicated. Look, I'll be signing later in the main ballroom, and…we'd all be thrilled to talk to you then.

NANCY: Oh, yeah, that'd be great! The life of a social media star, right? Hashtag SoBusy… But I wanted to talk privately for a little while.

MEGAN: Okay. Uh, look. There's a time and place, and I don't normally… [Nancy calmly reaches into her tote bag, and withdraws a pistol.]

NANCY: I think you will, though.

MEGAN: Okay. Okay.

NANCY: So I'd like to talk to Meredith.

MEGAN: Listen. I, uh…I can't just, you know, call up my alters on command…

NANCY: That's weird. Because every time you need them for a video, they just sort of show up, in a little parade. So, let's, like, pretend, okay. Let's pretend you're doing one of your little shows. Where your "alters" do tricks like dolphins at Sea World.

MEGAN: That's not…

NANCY: Meredith. I want to talk to Meredith, please. Right now.

MEGAN: [shifting to another alter] This…is Meredith speaking.

NANCY: Hi, Meredith! Hashtag BigFan. You're so smart. What was your IQ again?

MEGAN: Well…IQ…um…Intelligence Quotient isn't a constant. It varies depending on the test that's used to measure it. But utilizing the Wechsler test, my IQ has been measured at one hundred and seventy seven.

NANCY: That's very smart. What does "gentrification" mean?

MEGAN: Look, I think you misunderstand. IQ is a test of intellectual potential, not of vocabulary…

NANCY: Let me help you. Gentrification is the process by which new people, usually rich people, move into a place. And they push out the people who already live there.

MEGAN: Okay. Nancy…

NANCY: It's usually used for, like, a neighborhood. Where poor people live, and the bougies move in. But it's, like, also something that happens in other ways.

MEGAN: Nancy, look…

NANCY: Like…let's say you've got a mental health condition, okay? And let's say this condition really sucks.

MEGAN: Nancy…

NANCY: And you're, like, on these pills for it. And they just vaporize you. Like, when you take them, you stop being a person.

MEGAN: Nancy, you…you need to know this…

NANCY: And you also gain, like, thirty pounds. And you get the worst acne ever. And the alternative is, you don't take the pills, and your brain turns into, like, a catapult. Like, it launches you into the sky, and then it drops you into the bottomless pit! Over and over again! And whether you take the pills or don't take them, you are one hot mess of a human being!

MEGAN: Nancy, my alters…

NANCY: And then, on one of those rare days when you're functional, you go online. And there's this girl there. And she's got perfect hair, and perfect skin. Oh, but she's mentally ill, she says! And she's turned it into her goddamn gimmick!

MEGAN: Nancy, please! I'm not actually…my alters…these are just characters I play…

NANCY: DO YOU THINK I DON'T KNOW THAT? DO YOU HONESTLY THINK WE DON'T ALL KNOW THAT? This girl…she's got the perfect life! And it's not enough! She has to have yours, too! She can't just be better than you in every other way, she has to suffer more, too! This bitch is gentrifying your life!

MEGAN: Nancy…

NANCY: This…trauma porn…I mean…it's like it's a competition! It's like, "she who suffers most wins!" And it's SICK. You're the smart one, "Meredith," so you tell me. [She raises the gun and points it straight at Megan's face]

NANCY: How would you expect a person who's actually suffering from mental illness to react to this performance?

MEGAN: She'd be furious. She'd have every right to be. [pause] And she'd have no bullets in her gun.

NANCY: WHAT?

MEGAN: You've suffered, Nancy, and I'm so sorry. You're hurting. But you're not a hurter.

NANCY: DON'T TURN ME INTO A MASCOT! STAY IN YOUR GODDAMN LANE! YOU DON'T HAVE ANY IDEA WHAT IT'S LIKE!

MEGAN: You're right. I don't. I'm not bipolar. But, Nancy…you're not only bipolar. It's not who you are, it's a condition you have. If you wanted to hurt me, you'd have already done it. You wanted to teach me. So, yes, I hear you. But that gun's empty. [The gun in Nancy's hand shakes, and she dissolves in tears. Megan draws a long, shuddering breath. She reaches out, and gently removes the gun from Nancy’s grasp. She looks at it.]

MEGAN: This is a water pistol, Nancy.

NANCY: [Through her sobs] I’m sorry. I just…had to hear you say it. I had to hear you admit you were a fraud.

MEGAN: It's…a very realistic water pistol.

NANCY: Yeah, you'd know fake, wouldn't you?

MEGAN: It's not all fake.

NANCY: Oh, please.

MEGAN: Amy's real.

NANCY: What?

MEGAN: Amy's the real me. Megan's fake.

NANCY: Wait…so…you've actually got an eating disorder?

MEGAN: I've had one. My doctor and I…we eventually decided that I was spending too much time looking in the mirror, searching for flaws. We decided that I needed to appreciate that everybody's got their own flaws and their own monsters. So I…decided to explore what it would be like to be other people.

NANCY: You stole other people's pain, you mean.

MEGAN: It's not like that! Okay, maybe it is like that, a little. But what you're calling "stealing"…I call it empathy. I'm very good at empathy, Nancy. It's how I knew you weren't actually here to hurt me. And no, I can't fully know anybody else's specific pain. But I can understand what it is to be in pain. And people can't just…what was it you said? We can't just "stay in our lanes" forever. We have to try to reach outside of ourselves, and imagine–even imperfectly–what it's like to be someone else. I spent sixteen months inspecting myself in the mirror, Nancy. A life spent examining yourself is no life at all.

NANCY: But you take it way, way too far. I mean, why do you do this?

MEGAN: Well…that thing you said about “trauma porn”…you're probably right about that. On the internet, you have to get attention to make money. And it's like you said: "she who suffers the most, wins." It's a sick game. But I need the money. Everybody's gotta eat. [pause] Especially Amy.

NANCY: You seriously think it's OK to joke about that?

MEGAN: Well, as a smart girl once said, "I'm one hot mess of a human being."

NANCY: At least you're not going to jail.

MEGAN: I think maybe nobody is.

NANCY: Wait, what? You're not serious.

MEGAN: Look.This has sucked in a major way. But you're not wrong. This thing I'm doing…it's not all right. I can't create empathy by pretending to be someone I'm not. Let alone several people I'm not. Hashtag ScaredStraight. I won't rat you out.

NANCY: Oh, wow. Oh, oh, oh wow. Oh. My. God. Thank you. Thank you so much.

MEGAN: Nancy. Take those pills. I mean it.

NANCY: I will. Oh my God. Megan…Amy…if your fans could see this. They'd never need to see the alters again. Whoever you are…you're enough.

MEGAN: That's…wow. Wow. I think I've been needing to hear someone say that. Thank you.

NANCY: Hashtag BestFriends?

MEGAN: Well, let's not get ahead of ourselves. But…you'll be at the signing, right?

NANCY: It's a date!

MEGAN: Just leave the squirt gun at home.

NANCY: Deal!
```

---

## IC-0622: In Plain Sight

- Title: In Plain Sight
- Author (byline): Jennifer Doloski
- Work: In Plain Sight
- Publisher: Mushroom Cloud Press
- Publication date as stated: December 1, 2024
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, LINDA, BETTY, PETER, GRANDMOTHER, ELLEN, BENNY, DR. FLINT, PLAYMATE
- Teaser before the introduction: No
- Spoken words (computed): 2033
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
Adapted from Harriet Jacobs’ Incidents In The Life of a Slave Girl

The publisher asks performers to please credit both authors.

Introduction: Harriet Jacobs, known as Linda Brent in her writings, escaped slavery in 1835. She spent the next seven years hiding in plain sight, in the attic space of a shed on her grandmother’s property. Her children having been purchased by their free, white father and given to the care of her grandmother only days after her escape – she alternately joyed and agonized as she listened to them grow up, unaware of her presence. After her escape to the northern, free states, hidden on a cargo vessel, it would be nearly a year before she would have both of her children with her again. Adapted by Jennifer Doloski from Incidents In The Life of a Slave Girl by Harriet Jacobs.

Note: Though the narrator is Linda, her parts spoken to the audience are noted as Narrator, while her conversations with other characters are noted as Linda.

NARRATOR: It had been several weeks since I had left my master’s, and I could no longer safely stay in the home where I had been hidden. Dr. Flint’s hunt for me had been relentless. Too many times, already, I had been nearly discovered. I knew my presence must be a source of perpetual anxiety to my kind benefactress, herself a slaveholder. During this time, my friends had laid many plans for my escape.

LINDA: Betty, I must leave here tonight.

BETTY: Do as you tink best, poor chile.

LINDA: Oh, Betty! I don’t know how to tell you, to thank you. . .

BETTY: I don’t want no tanks, honey. I’se glad I could help you, and I hope de good Lord vill open de path for you.

NARRATOR: Betty, the maid who had been concealing me, gave me a sailor’s uniform to wear and sent me out the back door after dark. At the gate I found Peter, a young colored man, waiting for me. I had known him for years. He had been an apprentice to my father and had always borne a good character. I was not afraid to trust him. Betty bade me a hurried goodbye,

BETTY: I’se so glad you is gwine to free parts! Don’t forget ole Betty. P’raps I’ll come ’long by and by.

PETER: Take courage, Linda. I’ve got a dagger, and no man shall take you from me, unless he passes over my dead body.

NARRATOR: It was a long time since I had taken a walk out of doors, and the fresh air revived me. It was also pleasant to hear a human voice speaking to me above a whisper. I passed several people whom I knew, but they did not recognize me in my disguise. I prayed internally that, for Peter’s sake, as well as my own, nothing might occur to bring out his dagger.

LINDA: Where are we going?

PETER: To Aunt Marthy’s.

NARRATOR: Aunt Marthy was my grandmother. I could not imagine how it was possible to hide me in her house, every nook and corner of which was known to Dr. Flint.

LINDA: Peter, no! I cannot hide there, not even for a night!

PETER: Linda, you just wait and see. Your Uncle Philip, he’s got a place prepared for you. You just wait and see.

NARRATOR: We continued boldly through the streets, to my grandmother’s. I wore my sailor’s clothes, and passed several people whom I knew. The father of my children came so near that I brushed against his arm; but he had no idea who it was.

PETER: You must make the most of this walk, for you may not have another very soon.

NARRATOR: I thought his voice sounded sad. It was kind of him to conceal from me what a dismal hole was to be my home for a long, long time.

LINDA: (arms outstretched) Grandmother!

GRANDMOTHER: Hush! You’ll wake the children.

LINDA: Can I see them?

GRANDMOTHER: I said hush! No. Climb on up now.

LINDA: But. . .

PETER: Linda. You know they can’t know you are here.

LINDA: I won’t wake them. I just want to gaze upon them. Please.

PETER: Up you go now.

NARRATOR: A small shed had been added to my grandmother’s house years ago. Some boards were laid across the joists at the top, and between these boards and the roof was a very small garret, never occupied by anything but rats and mice. It was a pent roof, covered with nothing but shingles, according to the southern custom for such buildings. The garret was only nine feet long and seven wide. The highest part was three feet high and sloped down abruptly. There was no admission for either light or air. My Uncle Phillip, who was a carpenter, had very skillfully made a concealed trapdoor, which communicated with the storeroom. The storeroom opened upon a piazza. The air was stifling, the darkness total. A bed had been spread on the floor. I could sleep quite comfortably on one side; but the slope was so sudden that I could not turn on the other without hitting the roof. The rats and mice ran over my bed; but I was weary, and I slept such sleep as the wretched may, when a tempest has passed over them. Morning came. I knew it only by the noises I heard; for in my small den day and night were all the same.

ELLEN: You have to take me with, Grandmother said so.

BENNY: Aw, Grandmother, does Ellen have to go with me? Can’t I go alone? Please?

GRANDMOTHER: Hush. Both of you hush. And hurry that soup over to Mrs. Bissel while it’s still hot. Mind you, don’t splash it.

NARRATOR: I heard the voices of my children. There was joy and there was sadness in the sound. It made my tears flow. How I longed to speak to them! I was eager to look on their faces; but there was no hole, no crack, through which I could peep. This continued darkness was oppressive.

My food was passed up to me through the trapdoor my uncle had contrived; and my Grandmother, my Uncle Phillip, and Aunt Nancy would seize such opportunities as they could, to mount up there and chat with me at the opening. But of course, this was not safe in the daytime. It must all be done in darkness. It was impossible for me to move in an erect position, but I crawled about my den for exercise. One day I hit my head against something, and found it was a gimlet. My uncle had left it sticking there when he made the trapdoor. I was as rejoiced as Robinson Crusoe could have been at finding such a treasure. It put a lucky thought into my head. I said to myself, “Now I will have some light. Now I will see my children.” I did not dare to begin my work during the daytime, for fear of attracting attention. But I groped round; and having found the side next the street, where I could frequently see my children, I stuck the gimlet in and waited for evening. I bored three rows of holes, one above another; then I bored out the interstices between. I thus succeeded in making one hole about an inch long and an inch broad. I sat by it till late into the night, to enjoy the little whiff of air that floated in. In the morning, I watched for my children. The first person I saw in the street was Dr. Flint. I had a shuddering, superstitious feeling that it was a bad omen. Several familiar faces passed by. At last, I heard the merry laugh of children, and presently two sweet little faces were looking up at me, as though they knew I was there, and were conscious of the joy they imparted. How I longed to tell them I was there!

My condition was now a little improved. The heat of my den was intense, for nothing but thin shingles protected me from the scorching summer’s sun. But I had my consolations. through my peeping-hole I could watch the children, and when they were near enough, I could hear their talk.

One day, I saw Dr. Flint dressed for travel and headed toward the dock where I knew a steamboat offered passage north. Grandmother brought me the news.

GRANDMOTHER: Aunt Nancy says the doctor wrote to New York to a colored woman, born and raised in our neighborhood, and had breathed his contaminating atmosphere. He offered her a reward if she could find out anything about you. I know not what was the nature of her reply; but he has started for New York in haste, saying to his family that he had business of importance to transact.

NARRATOR: I peeped at him as he passed on his way to the steamboat. It was a satisfaction to have miles of land and water between us, even for a little while; and it was a still greater satisfaction to know that he believed me to be in the Free States. He returned without obtaining any satisfactory information. When he passed our house, Benny, having heard talk that Dr. Flint had gone to find me, called out, and I heard the exchange.

BENNY: Dr. Flint, did you bring my mother home? I want to see her.

DR. FLINT: Get out of the way, you little damned rascal! If you don’t, I’ll cut off your head.

BENNY: You can’t put me in jail again. I don’t belong to you now.

NARRATOR: Still, it wasn’t long days before Dr. Flint was back. Seeing Benny and Ellen playing in the garden, he stopped to speak to them.

DR. FLINT: Say, now, you see what I have here? Each of these is a whole silver dollar. One for each of you if you tell me what you’ve heard your grandmother say about your mother. We can use these to go buy some treats, bright new handkerchiefs, if you can tell me where your mother is.

BENNY: Dr. Flint, I don’t know where my mother is. I guess she’s in New York; and when you go there again, I wish you’d ask her to come home, for I want to see her; but if you put her in jail, or tell her you’ll cut her head off, I’ll tell her to go right back.

Autumn came, with a pleasant abatement of heat. My eyes had become accustomed to the dim light, and by holding my book or work in a certain position near the aperture I contrived to read and sew. That was a great relief to the tedious monotony of my life. But when winter came, the cold penetrated through the thin shingle roof, and I was dreadfully chilled. The winters there are not so long, or so severe, as in northern latitudes; but the houses are not built to shelter from cold, and my little den was peculiarly comfortless. The kind Grandmother brought me bedclothes and warm drinks. And one day, something more.

GRANDMOTHER: Here you are, Linda. I think you’ll do well with these.

LINDA: So much material. Grandmother, what do you expect that I can do with this?

GRANDMOTHER: It will be Christmas soon enough. Benny and Ellen will need their stockings filled. I’ve measured them. Here, make Benny a suit and Ellen a dress. Some dolls and small animals. Edge some handkerchiefs.

NARRATOR: Benny and Ellen had their Christmas stockings filled. Their imprisoned mother could not have the privilege of witnessing their surprise and joy. But I had the pleasure of peeping at them as they went into the street with their new suits on. I heard Benny call out to a playmate.

BENNY: Say, did Santa bring you anything?

PLAYMATE: Yes. Sure. But Santa Claus ain’t a real man. It’s the children’s mothers that put things in the stockings.

BENNY: No, that can’t be, for Santa Claus brought Ellen and me these new clothes, and my mother has been gone this long time.

NARRATOR: How I longed to tell him that his mother made those garments, and that many a tear fell on them while she worked!

I would pass another six Christmases in my self-made prison. I would pass one more living as a fugitive slave in the free states of the north before I had Benny and Ellen with me again.

THE END
```

---

## IC-0623: Katy and Sara WILL Get Tickets to the Ages Tour

- Title: Katy and Sara WILL Get Tickets to the Ages Tour
- Author (byline): Tom Mizell
- Work: Katy and Sara WILL Get Tickets to the Ages Tour
- Publisher: Mushroom Cloud Press
- Publication date as stated: December 1, 2024
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1527
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
Just past midnight in the bedroom of KATY, a teenage girl. The room is a maximalist shrine to girlhood with floor-to-ceiling pink, stuffed animals, photos with friends, and posters of pop stars. KATY paces anxiously. On her bed sits SARA, her bff. Sarah focuses intently on her phone, swiping to refresh every few seconds.

KATY Is it up yet?

SARA I’m refreshing it.

KATY It’s supposed to be up.

SARA I am still refreshing, Katy!

KATY I can’t believe we are going to see the Skyler Quick!

SARA On the Ages tour!

(They both let out a squeal/shriek of excitement.)

KATY This is going to be the greatest moment of our lives.

SARA A billion percent. I would do anything for these tickets.

KATY It’s going to be life-changing. They’re going to have to divide history into B.A.T. and A.A.T. Before Ages Tour and After Ages Tour.

SARA I can’t wait to be A.A.T Sara. I bet she has really shiny hair and goes to “brunch.”

KATY All we need now are the tickets. Any progress?

SARA Still loading. Maybe we should try your phone?

KATY No! It might slow down the connection. My phone would clog the bandwidth.

SARA Oh, that’s awful for its pores.

KATY Did we get the time wrong?

SARA No way!

(They recite in unison, as if it is a motto:)

TOGETHER All tickets will be released at 12:13 am and 11 seconds local time! 12:13 for Skyler’s birthday, December thirteenth and 11 seconds for all eleven of her studio albums-available now on Spotify, Tidal, and Apple Music.

KATY Who even uses Apple Music?

SARA Dorks and losers, don’t worry about them.

KATY AM is Midnight, right?

SARA Of course. They named it after her album!

KATY I thought A.M. was morning. Like, “I am awake.” And then P.M. is night time because like… like, “Pmm I’m sleeping, leave me alone.”

SARA Wait, wait, wait! Shut up!

Oh my god, rude.

Sorry.

Not you in your Repudiations era.

No way, you think so?

KATY

SARA

KATY

SARA

KATY Independent boss girl vibes for sure.

Oh my god, like I love you.

I love you, queen.

Wait, stop!

What?

It loaded!

SARA

KATY

SARA

KATY

SARA

(They both squeal in excitement again, in perfect unison.) Two tickets, 3rd balcony row FF.

Let me see! She grabs the phone from Sara. Partially obstructed?

KATY

SARA Yeah…

(A long beat. Then they turn to each other and let out another excited screech.)

KATY Only partially obstructed?!

SARA Oh my god! We’re going to get to see at least sixty percent of Skyler Quick’s face and body!

KATY Ok, ok, breathe! We have to buy them. I’ve got my debit card.

SARA Right, ok! Let’s see, base price plus tax plus licensing fee plus stadium fee plus online fee plus service fee plus cleaning fee plus market-controlling-monopoly fee plus incidentals and ticket insurance…

KATY What’s the total?

SARA One thousand, four hundred and seventy eight dollars.

KATY What?

SARA Each.

KATY What?!

SARA So all together that’s…

KATY Almost three thousand dollars.

SARA How much is on your debit card?

KATY It’s birthday money from my grandma, plus what I got lifeguarding last summer so like… a hundred dollars?

(A long moment. Both suddenly begin to sob and hug each other.)

SARA Oh my god!

KATY What do we do?

SARA (Louder:) Oh my god!

KATY We have to think of something.

SARA

(in hysterics:) Oh my god!!

KATY PULL YOURSELF TOGETHER!

(SARA immediately freezes, embarrassed.)

SARA Sorry.

KATY We can’t miss this concert.

SARA Never. Anyone who’s anyone will be there. If we don’t go, we’re…

KATY Nobodies!

SARA Losers!

KATY Fake. Fans.

SARA No! (As if praying:) Queen Skyler, she doesn’t mean that.

KATY I mean it. If we don’t go to this concert, how can we even call ourselves Quickies?

SARA I don’t think we should call ourselves that anyway.

KATY Do you have any money?

SARA I have twelve dollars.

KATY That’s a start.

SARA Wait! I have four dollars. I bought nail polish yesterday.

KATY Oh my god, show me!

(SARA holds out her nails for inspection.) Cuuuuute!

SARA Oh my god, thanks!

KATY Wait. Concert. Money. Focus!

SARA Yes! Should we ask your mom?

KATY No way! My mom cut me off for trying to order a “23 and Me” kit. What about your mom?

SARA My mom sells forged Pokemon cards on eBay for a living.

(They both sigh.) Maybe we could get a loan?

KATY Like at the bank? Do you even have a credit score?

SARA I got a 2 on the AP Economics test?

KATY Wait, that’s it!

SARA Thank you, I studied super hard.

KATY Not that! The bank!

SARA The bank?

KATY Exactly!

SARA You’re going to have to explain a bit more.

KATY The bank is where all the money is.

SARA I understand what banks are. How do we get the money from the bank?

(KATY begins to laugh, quietly. Slowly it builds into a louder, more maniacal laugh. SARA awkwardly starts to laugh along. Like a choir teacher, KATY motions for SARA to laugh louder with her. They both build into a full blown evil laugh, until KATY suddenly motions for silence like an orchestra conductor.)

KATY We take it!

SARA What?

KATY (As if proposing:) Sara, will you rob a bank with me?

SARA No!

KATY It’ll be easy. Doesn’t your brother have a paintball gun?

SARA He has a NERF blaster?

KATY Whatever, we’ll put some black tape on it!

SARA I am not bringing a gun to a bank!

KATY Oh my god, then we’ll just do a note.

SARA A note?

KATY Like hand them a note! You know how it works!

SARA I don’t know how it works! I’m not like a practiced burglar.

KATY Technically, a burglar would be sneaky, we’re going in through the front door.

SARA And handing them a note?

KATY Yeah! You hand them a note that says like “This is a robbery, give me three thousand dollars.”

SARA Or what?

KATY Or I’ll, like, do a crime to you! A bad one! Here, roleplay with me. You be the bank teller.

SARA (in character:) Hi! Welcome to the bank.

KATY Hi there!

SARA How can I help you today?

KATY Give me all your money.

SARA No. Please leave.

KATY (Breaking character:) Oh my god, Sara. Way to “Yes and.”

SARA Ugh, fine. (Back into roleplay character:) Here is all the money. I’m going to call the cops now and you’re going to jail forever.

KATY (Dropping the roleplay completely:) We’ll be gone before the cops can get there!

SARA They have cameras at the bank, Katy! They’ll know who we are.

KATY No, because that’s like the best part. We’ll wear disguises.

SARA Disguises?

KATY Of course! Do you still have your wig?

SARA What wig?

KATY From your Susannah Louisiana costume.

SARA You don’t know that’s a wig! That could be my real hair and I’ve been Susannah this whole time.

KATY Sara, I have known you since pre-school.

SARA I’m just saying you’ve never seen me and Susannah in the same place at the same time!

KATY Fine! We can get different wigs. Then we add some masks and glasses and poof! We become unrecognizable.

SARA Like a disguise would work. Your natural beauty would still shine through.

KATY Oh my god, stop. You don’t mean that.

SARA No, I do for real.

KATY You’re the best ever and I love you.

SARA You’re the best, I would literally die for you.

KATY That’s perfect!

SARA Wait what?

KATY You don’t have to die for me, just help me with this bank thing!

SARA No! It’s, like, against the law.

KATY Oh, so are all the laws good? All the laws are just and fair now?

SARA I mean-

KATY The laws that say we can arrest people for being homeless, that’s just and fair?

SARA I didn’t say that.

KATY The law that says you can do e-girl make up and not have to go prison, that’s just and fair?

SARA Absolutely not!

KATY Then the law that says we’re not allowed to see Skyler Quick in concert just because some stupid bank has the money, that’s just and fair?

SARA No! But I don’t want to get in trouble.

KATY Didn’t you say, and I quote, “I would do anything for these tickets?”

SARA Ok, yeah but like-

KATY So did you mean it? Or are you a liar?

SARA I meant it, but like Katy, come on!

KATY No, I get it! You’re just not my friend. You’re a lying liar. Who lies.

SARA You don’t mean that.

KATY I totally do. And when I write a song about this one day, it’s gonna have a ten minute version!

SARA Ok, fine! I’ll do it!

KATY You mean it?

SARA We have to. It’s for Skyler.

KATY Oh my god, you’re the best!

SARA I love you!

KATY I love you more, bestie!

(They squeal in excitement and hug.)

SARA Ok but we can’t rob the bank on 3rd street, that’s where my mom goes.

KATY Deal. ! I think Skyler Quick would be proud of us.

SARA Of course! She wouldn’t make her tickets so prohibitively expensive for her mostly teen fanbase if she didn’t intend for us to take drastic action to obtain the money to see her!

KATY Exactly! We’re just being good Quickies!

SARA I still don’t think we should be called that.

KATY Let’s do this. I’ll go get some magazines and some scissors.

SARA What for?

KATY To make the note! I’ll cut the letters out and stick them together like I’m the Zodiac killer.

SARA Ugh, we love an astrology queen!

KATY Meet back here in like an hour?

SARA I’ll go get my wig!

(They squeal one last time in excitement and run off.) THE END.
```

---

## IC-0624: Power Struggle

- Title: Power Struggle
- Author (byline): Robert LaVohn
- Work: Power Struggle
- Publisher: Mushroom Cloud Press
- Publication date as stated: December 1, 2024
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: AC, MM, AC & MM
- Teaser before the introduction: No
- Spoken words (computed): 1793
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
The Air Controller, a young superhero
Muscle Mage, a young superhero
Setting:
The Secret Headquarters of the Legion of Heroic Guardians
Note: While the parts as written use female pronouns, the characters are not tied to a
single gender and permission is given to make adjustments as needed.

The Air Controller (AC): Thank you all for this opportunity to try out for the Legion of Heroic Guardians, the greatest organization of superheroes in the known galaxy! It’s been my dream since I was a child to use my powers and abilities to preserve justice and protect those in need! As I look around me and see legendary heroes like The Purple Bee, Gladiator Prime, Aviatrix, Dr. Cyclone, and so many more, I am honored to be considered for membership alongside those caped crusaders I have admired for so long. I believe that, once you see me in action, you’ll– Muscle Mage (MM): (running up, slightly out of breath) Sorry! So sorry I’m late. I know I was scheduled for 2:30, but there was–

AC: Hey, wait your turn, okay? This is my audition slot! Members of the Legion of Heroic Guardians, today I will demonstrate–

MM: Um, look, you need to cut me a little slack. While you were here rehearsing your speech, I was out foiling a plot by Dr. Despicable and his Evil Robot Septuplets!

AC: I don’t care where you were or what you were doing. You missed your scheduled audition, and this is my time block. So, just come back next year, okay?

MM: I most certainly will not! I was invited here, too! I have just as much right as you have to audition for the Legion of Heroic Guardians.

AC: You DID have as much right as I have, but you missed your audition. So…bye!

MM: But as I said, I had a really good reason. I was putting others first, like a good superhero should.

AC: Well, I think a big part of being a good superhero is, you know, showing up in a timely manner.

MM: Well, I think part of being a good superhero is not being a pompous little–

AC: (cutting her off; to the superhero committee) Ladies and gentlemen, as I was saying–

MM: (also to the committee) Thank you so much for the opportunity–

AC: –once you see me in action–

MM: –I know that I have what it takes to join–

AC: –you will realize that I will be the perfect choice to join– AC, MM: –The Legion of Heroic Guardians!

MM: If the committee would just give me a moment to–

AC: Okay, I think that’s about enough out of you!

(She gestures dramatically in the air, then continues talking to the committee. As soon as she finishes her gesture, Muscle Mage continues speaking, but no sound can be heard. Muscle Mage takes a step forward and rebounds as though striking a brick wall. She looks about quizzically and takes another step forward, with the same result. She enacts the “mime trapped in a box” routine, then begins yelling soundlessly and pounding on the invisible container surrounding her). I believe I have what it takes to be a useful member of the LHG and to help them fight their never-ending battle against injustice. I am–The Air Controller! My powers, as you can see, (gesturing to Muscle Mage) are a remarkable deterrent to crime. My absolute control over the molecules of the air allows me to harden them into a barrier stronger than steel. No evildoer can overcome my impenetrable air prisons! No physical force known can break through them! In addition, I can use my air powers to help me fly or lift heavy objects.

(Inside the “box,” Muscle Mage, seething with anger, raises
her fingers to her temples, implying that she is using her
superpower as well. Just as Air Controller gets to “lift heavy
objects” and raises her arms to show her strength, she
suddenly slaps herself in the face).
I’m–I’m sorry, I don’t know what came over me, I–

(Air Controller slaps herself again, this time with the opposite hand). I’m not sure what is happening here.

(Muscle Mage has a huge smile on her face. Air Controller realizes what is happening). You’re–

(another slap) –doing this–

(another slap) –aren’t you?

(another slap) Really mature. That’s really mature.

(Suddenly, her hand points two fingers in a “peace” sign.
She looks perplexed for a minute–and then the two fingers
start moving toward her eyes. With her other hand, she
grabs her own arm, fighting to prevent the arm under Muscle
Mage’s control from poking herself in the eyes).
Okay, fine, if that’s how you want to play it.

(She thrusts her possessed hand away with great effort and
a groan, then claps both hands together in front of her. As
she does so, Muscle Mage’s hands drop from her temples to
her cheeks, squishing her lips into a “duck face.” At the
same time, her whole body compresses to simulate the
invisible air prison walls tightening on her).
My air prisons can subdue any foe, no matter who she is. Clearly, I am the better
choice for membership in the Legion!

(Muscle Mage squints her eyes tightly closed, and suddenly
Air Controller begins slapping and hitting herself in the face
repeatedly, and so on, and then starts to choke herself with
one hand while the other hand tries to prevent it from doing
so. The “possessed” limb then pulls itself away, makes a fist
in the air, then punches Air Controller in the gut. She
doubles over and inhales loudly).

MM: (begins “speaking” angrily during the “choking” portion but can only be heard when Air Controller is hit in the stomach) –clearly the better choice and I have the powers to prove it! I, Muscle Mage, have the ability to control the muscles of any other individual with my mind–even so-called super-powered individuals like this one. I look forward to being a part of the Legion, and I am committed to–(she stumbles forward, as though she’s been kicked from behind)

AC: (breathing heavily) Just–need a moment–to catch my breath…

MM: –I am committed to becoming a world-class–(again, another impact from behind)

AC: Oh, you’re a world-class something all right! (she has been using her air powers to strike Muscle Mage in the posterior; she does it again)

MM: Would you cut that out!

AC: What’s the matter? Can’t handle a little competition?

(another air-bump from behind)

MM: Competition? You want competition? Fine! Let’s have a dance-off!

(Air Controller’s eyes grow large as she realizes what Muscle Mage means).

AC: Look, I just want to have my audition without–

MM: Oh, I’m going to give you an audition all right!

(Muscle Mage waves her hands wildly in the air. Air Controller, against her will, begins to dance in an awkward and embarrassing way, with wild, jerky movements).

AC: Really? You have the power to control other people’s muscles and this is what you do with it? You’re a lousy excuse for a superhero, you know that? This is really immature!

MM: I’m immature? You were the one using your super power over air molecules to kick me in the butt!

AC: That was your butt? I guess I got it confused with your face!

MM: Ooh, I know, let’s see if you can do the Macarena!

AC: Come on! This is ridiculous!

(she begins doing the dance moves for the macarena)

MM: Just demonstrating who is the better superhero here, that’s all! I think I’ve made my point to–

(she begins speaking, but again silently. She realizes slowly she’s trapped again. Her hands mime a bubble shape around her head).

AC: (still dancing the macarena) I hope the committee will take note that even when my body is under the control of a malign influence, I can still use my superior abilities to encase an opponent’s head in a solid bubble of air. And, once I’ve done that, my opponent is entirely at my mercy.

(While Air Controller speaks, Muscle Mage holds her hands
around the invisible bubble. It suddenly “pulls” her backward
a few steps, then forward a few. Then, the bubble seems to
pull her head violently left and right, back and forth multiple
times, then it seems to lift her off the ground as she stands
on tip-toes, desperately pounding at the bubble).

AC: (continuing) But I’m not here to embarrass anyone.

(The “bubble” collapses, Muscle Mage strikes herself in the face, and then collapses to the ground. With this lapse in concentration, Air Controller can finally stop dancing).

AC: (continuing) I’m just here to demonstrate that my abilities are superior to…hers.

MM: I’ll show you superior!

AC: Just you try it!

MM: I’m going to–

(They both stop talking at once)

AC: Um, is someone talking inside my head?

MM: You hear it too?

AC: Riiiight. Ms. Mental.

MM: She’s telepathic.

(They listen to the unheard telepathic voice and react with dismay).

AC: But…Wait, that’s not fair! I deserve to finish my audition!

MM: Please, let me have another chance! I know I can do this!

AC & MM: (together) Rejected!?!

(They listen again to the voice, reacting and ad libbing “Well, yes–” and “Sure, but–” to what is clearly pointed and accurate criticism).

AC: No, I understand. You’re right–I should have been more welcoming to a fellow hero.

MM: Yes, I should have been less impulsive.

(Again, they react to the unheard telepathic voice).

AC: Do I have to?

MM: She started it.

AC: Really, this is all her fault.

MM: If she had been a little more open-minded, we–

AC: All she had to do was get here on time and–

MM: Oh, come on, she–

AC: She’s really the one who–

(They react as though someone is screaming in their ears).

AC: Okay, fine fine fine! I get it!

MM: I hear you! Just…stop yelling in my head! Please!

(They sigh in unison).

AC: (through gritted teeth) Muscle Mage, I am sorry–deeply sorry–that I locked you in a cage of air molecules and kicked you in the rear end.

MM: (equally reluctantly) Air Controller, I regret that I made you punch yourself in the face repeatedly and dance the Macarena.

AC: So, uh….what happens now? Can I reapply next year?

MM: I promise I will keep working to become an even better superhero. I know I belong with the Legion of Heroic Guardians, and–

AC & MM: (together) What?

AC: You want the two of us to do what? Work with another hero?

AC: Wait, you mean–

MM: You want us to be– AC & MM (together, with disbelief): Sidekicks?

MM: I guess it sort of makes sense. I just thought I was ready to be a hero on my own, you know?.

AC: I suppose it is the next logical step. Sort of a mentorship program, right?

MM: (thinking it over) I bet I can be a great sidekick.

AC: Well, I will, naturally, be a better one.

MM: Perhaps you can learn to reign in that ego by working with a better hero.

AC: Working with a real superhero might help you learn to be on time.

MM: You miserable little–You know what? I’m not even going to argue. A year from now, it will be clear who the better sidekick is–me.

AC: I’m going to be a much better sidekick than you. (to the voice) So which Legion member do I get to work with? Purple Bee? Ocean Queen?

MM: How about me? Thunder Master? Sky Raider?

AC: Neon Tarantula?

MM: Elastic Lord?

AC: Dr. Gravity?

MM: Captain Cloud?

AC: Kinetic Kid?

MM: The Blue Ostrich? AC and MM: (simultaneously, with a sense of awe at the possibility) Remarkable Man?

MM: Oh, please! If anyone is going to be partnered up with Remarkable Man, it’s going to be me. My powers are a much better complement to his.

AC: Oh, right. You as a sidekick to Remarkable Man? Don’t make me laugh. You wouldn’t even be a decent sidekick to the Yellow Condor, because– MM and AC (together): Ow ow ow!

MM: Again with the yelling!

AC: Are all telepaths this loud?

(They listen again to the instructions from the telepathic voice, their faces etched with confusion and ad libbing sounds of uncertainty).

MM: Okay, I’m a little confused here. You’re saying you want us to work with another hero, but NOT a hero who’s a member of the Legion.

AC: That doesn’t make any sense. I mean, I don’t really want to be a sidekick to some nobody–

MM: Oh. So, not so much a sidekick?

AC: More of a partner thing, then?

MM: Like, Simon & Garfunkel?

AC: Hall & Oates?

MM: Sacco & Vanzetti?

AC: So, I would partner with an up-and-coming hero?

MM: Like, team up and help each other?

AC: Someone on my level.

MM: Someone who needs my assistance.

AC: Helping another hero become more…organized.

MM: Providing another hero with a bit of…spark.

AC: I can do that.

MM: No problem.

AC: Sign me up!

MM: I am a team player.

AC: I am a better team player.

MM: Do you even listen to yourself?

AC: Okay, fine. The important thing is, we both get paired up with someone who will help us improve, so next year, I can join the Legion.

MM: You mean so I can join the Legion.

AC: So the better superhero can join the Legion.

MM: Who am I going to be paired up with?

AC: A better question: What up-and-coming superhero gets to work with me?

(they react to the telepathic voice)

MM: Not her!

AC: Not her!

MM: No way could I work with her.

AC: She is clearly not partner material.

MM: I’d rather have my powers stripped away by a supervillain!

AC: A month teaming up with her would turn me into a supervillain!

MM: We couldn’t even get along during this tryout!

AC: I can’t believe you think we could work together to fight crime!

MM: She’s self-centered, unfeeling, and bossy!

AC: She’s immature, disorganized, and rude!

MM: Are you sure we can’t do something else?

AC: Are there any other options? (The silent voice responds. They listen with frustration and, eventually, resignation).

MM: Yeah, that’s what I was afraid of. Fine. I will be the best partner to Air Controller I can.

AC: And I will be an even better partner to Muscle Mage.

MM: And in a year, we’ll be back to re-apply. And you will be amazed at the exploits of… Muscle Mage and Air Controller

AC: I believe you mean Air Controller and Muscle Mage.

MM: Based on what? Alphabetical order?

AC: No, based on birth order!

MM: That again?

AC: Well, why not?

MM: You are only eight minutes older than I am!

AC: It’s not my fault that even when we were born you were late!

MM: You know what? Fine. Have it your way. “Air Controller and Muscle Mage” it is. But when we get home, you’re explaining this whole thing to mom and dad!
```

---

## IC-0625: Rapunzel and Ella’s Magical Hair Salon

- Title: Rapunzel and Ella’s Magical Hair Salon
- Author (byline): Stephanie Christensen
- Work: Rapunzel and Ella’s Magical Hair Salon
- Publisher: Mushroom Cloud Press
- Publication date as stated: September 1, 2021
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2393
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
Duo-FF-Dramedy

By Stephanie Christensen

Rapunzel [singing to herself and dancing around majestically]: La la la la la! [makes eye contact with an audience member] OH! Hello there! The hair salon doesn’t open for another hour, but WOW, you look like you could use a hairdresser. [gasps] I mean that in the nicest way possible!!! I haven’t quite mastered social interactions yet. Come in, come in! We’ll make an exception for you early. My name is Rapunzel. Welcome to our Magical Hair Salon in the heart of the most magical place on earth… Bronx, New York! Just listen to the sound of people road rage yelling in the street. It’s so wonderful, isn’t it? [listens to audience as if audience asked a question] How did this salon get started? Well that’s an engaging story! [Ella, other duo partner, comes out from behind Rapunzel] Oh, perfect timing! This is my partner, her name is Cinderella! Ella [strong New York accent]: Tsk tsk, Rapunzel! What did I tell you about telling strangers my ugly full name?!? My name is Ella. Cut the Cinder pigeon poo part. No cinder. No Isabella. No Cruella. Just Ella. Rapunzel [upset]: I am so sorry, Ella! I always forget that you’re sensitive about that. [to audience member, whispers] She cleaned the floors at Grand Central Station for a few years, that’s where the “Cinder” came from. Ella: RAPUNZEL! Rapunzel: SORRY!!! Ella, this customer is asking about our story. Ella [chewing gum, sassy New Yorker]: HA! You better hold onto your behind. You’ll be here for hours if you want to hear a story as convoluted as ours. Rapunzel doesn’t like to leave out any little detail. Rapunzel: Oh, look at their hair, Ella! They’ll be here for hours anyways. Ella: THAT’S for sure. Rapunzel: It all started when I was living alone in a meadow in the middle of Montana… Ella: RURAL Montana! Rapunzel: I was just a girl with two dreams… to meet a living, breathing homo sapien.

Ella: That sounds weird out of context, but she grew up among racoons and elk. Rapunzel: And to open the WORLD’S BEST HAIR SALON so that everyone could have as luscious, long, flowing locks as mine!!! Ella: She has a few magic ingredients that can really make your hair shine. See, me, I wasn’t into the hair industry before I met this goofy go-getter. But, I promise you, all of her hair products are organic. Straight from the forest. In a few words… we’ll make ya feel like a princess— Rapunzel [interjecting]: AT RAPUNZEL AND ELLA’S MAGICAL HAIR SALON! INTRO [Flashback to Rapunzel living in a meadow in Montana; duo partners can act out scenes, like Rapunzel rolling in the meadow or running from a bear] Rapunzel: Back in Montana where I was abandoned at birth, I spent my days rolling around in the flowers of the meadow and my nights hiding in the trees from hungry Montana bears! To stay alive, I would wander into the forest to find a flowing river of water or some beetles and berries for grub. Ella: Picture it… this gorgeous blonde-haired Tarzan swinging from tree to tree, dodging bears and chomping on beetles! Rapunzel: The forest creatures became my friends. [interrupting the flashback, returned to reality in the hair salon] Ella: Wild animals don’t just become your friends, Rapunzel. Rapunzel: Well. I killed them first. Then, I was able to brush, braid, and style their hair and fur as I pleased! Ella [notices customer looks uncomfortable]: Oh don’t you worry, her killing days are over! Rapunzel: The only thing killer about me now is my killer dye jobs! Ella: And MY killer marketing skills! Rapunzel: Sometimes I still have the urge. Ella [changing the subject]: One day, she’d had enough of braiding on small subjects, so she made a plan to crawl out of the woods to civilization.

Rapunzel: I embarked on an adventure! Ella: Now, I don’t know how she got here because she never tells me the details. But somehow, this shiny-headed damsel trekked her way 2,000 miles to the heart of the city. Rapunzel [shivers]: I don’t wish that journey upon anyone. Ella: What did you do, Rapunzel? Ride a bear? MegaBus? Hitchhike with strangers? Rapunzel: Oh, far worse than any of those transportations. Ella: Anyhow… she came flying into Manhattan like that Will Ferrell guy in that one Christmas movie, all wide-eyed and naïve. Rapunzel: Oh I love that movie! I would really like to meet the Elf and discuss shared experiences. Ella [whispers]: she still hasn’t mastered the idea of fictional Hollywood movies yet… [normal voice] So, now to the possibly even MORE tragic story: mine! Rapunzel: Oh no! Her story is not as bad as she makes it sound. Ella: Rapunzel wouldn’t know a thing about this, but I went to college at NYU. The best 4 years of wasting thousands of dollars in my whole life. I majored in marketing, got a 4.0, and prepared for a life of glorious ladder climbing. My parents from the Bronx were so proud of me. Rapunzel: Can you imagine? Having PARENTS??? Ella: That brings me to the day I met Rapunzel… I was a home-bound postgrad. I managed to land one job as a custodian at Grand Central Station. From there, I got a job as an office cleaner, doing every chore imaginable for a big-shot marketing firm: sweeping the floor, refilling the coffee, filing restraining orders against anyone who accused us of deceptive marketing tactics. And my job only paid my 0.000002 Bitcoin per hour for my labor! Rapunzel: Meanwhile, I was learning how to use a crosswalk for the first time. Ella: She was getting hit by a car. Rapunzel: I was ABOUT to get hit by a car! Ella: And of course, she’s surrounded by busy New Yorkers who don’t ever look up from their phones. But me—I’ve got reflexes like a swift rat. Or a pigeon, flying to the rescue. And I saw the whole scene go down, so I rushed in, and pulled her out of the way!

Rapunzel: She was my prince charming! [Flashback to them meeting for the first time in NYC] Ella [in the flashback]: What are ya DOIN?!? I’m walking here! Minding my business! When I see this blonde goddess about to get mowed down by a taxi! Girl, I’ve never seen hair as beautiful as yours. You can’t let a tire tread on that! Rapunzel: Oh WOW! Thank you! How did you know what that big machine was? Do you live here, on this corner? Ella: Uhh… I live with my parents. Rapunzel: Wonderful! I live in a meadow! Well, I did. Now I live in something called a commune in Brooklyn. They took me in as long as I agreed to model for their apartment’s advertisement. Ella: Wow, I wish I was THAT gorgeous to get a deal like that. Rapunzel: Are your eyes blinded by pollen and spider webs?! Your hair is INCREDIBLE! I have never seen such bouncy curls before in my life. The hair I usually work on is coarse. Occasionally covered in ticks. Ella [confused, grossed out]: What do you do? Rapunzel: Oh, I am a hairdresser! I just learned that term a few days ago. Ella: Really? How long have you been in New York? Rapunzel: About a week. This city is very big so I am only able to walk about 20 miles per day. I have never seen trees as tall as these glass ones. Ella: This is your first week as a hairdresser in New York??? And you’ve been WALKING the city? Whoa, whoa whoa, I think we need to get you on a subway. [Flash forward to the hair salon] Rapunzel: And she took me on my first SUBWAY RIDE!!! That was the best day of my life! Ella: It was the day that changed everything. Rapunzel needed help starting and marketing her business. And I thought I could become a self-made entrepreneur millionaire by helping her, like all the famous Tik Tok millionaires nowadays.

Rapunzel: Ella and I rode the subway UNDERGROUND at LIGHTNING SPEED! We ate a pizza that was much better than beetles and berries. And we saw a man dancing with a rubber chicken on the street! Ella: That is where it all began. I taught her the in’s and out’s. We got to work printing and distributing brochures immediately. Soon, my whole neighborhood in Bronx learned about Rapunzel’s hair talents. Rapunzel: Ella came up with an amazing saying—Rapunzel and Ella’s Magical Hair Salon: Where you can get a hairstyle that makes you feel like a princess! Ella: We eventually shortened it to “we’ll make ya feel like a princess!” But poor Rapunzel… we went through some rough times to get here. Rapunzel [apprehensive]: Our customer doesn’t need to hear about that. Ella: Securing and affording a storefront like this wasn’t easy work. And I think everyone should know that, Rapunzel. [duo partners transition to the last flashback] Rapunzel: It was about a year and 3 months after I had arrived in New York City. Ella: At this point, Rapunzel and I were operating successfully out of my parents’ living room. She had grown close to her ladies at the commune, and occasionally we would host big events there for the nuns. Rapunzel: I had managed to retrieve and store all of my natural hair ingredients from the meadow. Some days in the big, noisy city, I missed that place more than I could imagine. Ella: There was one night where Rapunzel and I had to work late at my house. She forgot to wear shoes when she came over to my house. Rapunzel: In the forest, I was always barefoot. Ella: So I let her borrow some of my slippers for the subway ride home. Maybe around midnight, it was time for her to leave. She insisted on going alone. Rapunzel: On my walk to the subway, I heard a stranger’s voice. [Ella steps behind Rapunzel and then comes out hunched over, as Rumpelstiltskin] Rumpelstiltskin: Hey. Psstt! You there with the hair like golden straw! Rapunzel [looks around, confused]: Huh? Me?

Rumpelstiltskin: Come closer! I’ve got some watches that you’ll really want to buy. Rapunzel: Oh no thank you, sir! I don’t need a watch to know I’m having a good time! Rumpelstiltskin: But I need you to buy a watch. I’ll have no money otherwise if you don’t. Rapunzel: That is very sad to hear! Can you maybe go to the bank and get some? My friend Ella and I did that, and we’ll find out in a couple days if they will give us money for our hair salon! Rumpelstiltskin [inches closer]: Ahhh, a hair salon? I say. You must be a very smart girl. How about you and I make a deal, hmm? Rapunzel [nervously looks for the subway, then looks back at him]: A deal like what? Rumpelstiltskin: If you buy twelve of these watches before their tickers strike twelve, I’ll give you a storefront of your own for free! Rapunzel: A storefront for free? Well that sounds magical! But I don’t have any money to buy your watches, sir! Rumpelstiltskin: Oh you’ll buy these watches, whether you want to or not!! [Lunges for her and grabs her. Duo partners should enact a near-touch scene where the one playing Rumpelstiltskin hover grabs Rapunzel. This should give opportunity for unique tech.] GIVE ME YOUR PURSE! And don’t try to scream!! Rapunzel [screaming to an empty subway station]: HELP! PLEASE, SOMEONE HELP!! [tries to wrestle out of his grip] Get off of me! Let go of my bag! PLEASE, SIR! The subway is here now, please let me get on it. Rumpelstiltskin [grabbing her hair]: If you don’t give me your bag, I will cut off all of this golden blonde hair and throw it in the sewers! [Rapunzel breaks away, throwing her bag at him and losing one slipper, as she makes a beeline for the subway] Rapunzel: Absolutely not!! Ow, my hair! Get away from me! [Flashforward to hair salon] Ella: That night, one of the nuns at the commune called me about what happened. Rapunzel was pretty shaken up when she got home. She threatened to cut off her beautiful hair.

Rapunzel: My life was worth more than my hair. And I never thought I would have to choose between those. Ella: So, I had my father travel with me over to the commune. I sat with Rapunzel at her desk, and helped her cut it and style it myself. Rapunzel: We created the beautiful, healthy, functioning blonde bob you see today! Ella: It threw a wrench in her confidence. Rapunzel and I had to go over safety in the city and set new limits on what she could do alone. Rapunzel: In the meadow, I was responsible for my own destiny. I knew how to avoid the predators— the bears who could tear me apart. When I finally met humans like me, I never knew they could do the same thing. Ella: I slept over that night. Rapunzel told me about her life in the meadow. Rapunzel: The yellow blossoms. Grass that made your nose itch but your heart soar to the clouds. Fresh air, with no smog or fog or cigarette smoke. Ella: We found joy talking about such a welcoming, flower-y place. And we knew that was the atmosphere we would create here, at our salon, if we’d ever make it a reality. Rapunzel: She sang me to sleep that night, actually. Ella: Hey! We can’t let people know I have a soft side. I’m kind of like your NYC protector, Rapunzel. Rapunzel: You and me Ella. La la la la la la… Ella: And the next morning, we woke up to a voicemail in my phone inbox. It was the bank, telling us we had been granted the loan for our storefront. Rapunzel: Our magical hair salon! Our hair haven! Ella: So welcome in… and thanks for trudging up a story I haven’t thought about in a few years. Rapunzel: Here, we’ll make ya feel like a princess. Ella: Or a dead forest animal. Either way, with a bangin’ new hairdo.
```

---

## IC-0626: The Big Decision

- Title: The Big Decision
- Author (byline): Mike Noland
- Work: The Big Decision
- Publisher: Mushroom Cloud Press
- Publication date as stated: December 1, 2024
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1852
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
Scene INT: Joy’s living room

Action Joy is entering her living room. She has just gotten home from school and is unloading her backpack. Suddenly, Shelley comes in from the other room and startles Joy and the conversation begins.

Shelley (Shelley enters with a cookie and a can of soda.) Well, I’ve made a huge decision. A decision that could alter the course of our lives in so many ways.

Joy (Joy jumps and is startled.) AH! Good Lord Shelley, where did you come from?

Shelley ( Barely notices that Joy is surprised.) The kitchen, duh, where do you think I got this. (Holding up the cookie and soda.Takes a bite of the cookie.)

Joy But school just got out. How did you get here so fast?

Shelley I had 7th period history and you know that substitute Mr. Johnson’s has?

Joy You mean the guy who calls everyone “Dude” and “Brah”?

Shelley Yeah that’s him. Well, he’s not very bright.

Joy What do you mean?

Shelley You know, slow… dumb… easy to fool…The text was typed but never sent…

Joy No, I know what “not very bright means.” I mean, what does the substitute have to do with anything?

Shelley Well, I convinced him that I needed to take pictures for the yearbook and I had to go to the pool and take pictures of the swim team.

Joy But we don’t have a swim team.

Shelley Yep

Joy And we don’t even have a pool.

Shelley Exactly.

Joy And you don’t have a camera.

Shelley I know, that’s why I said he wasn’t very bright. So, I left class early and came right over.

Joy But what does that have to do with you breaking into my house?

Shelley I didn’t break in. I used the key.

Joy You have a key to my house?

Shelley No, I used the spare key that’s under the dwarf in the flower bed. .

Joy We don’t have a dwarf in the flower bed and we sure don’t have a spare key.

Shelley Yes you do AND yes you do. Alicia showed me where it was several weeks ago. You know, in case I needed to get in and nobody was home. Like today. (Take a big drink of soda.)

Joy Wait, what? First there is no dwarf in the flower bed…oh, you are talking about the garden gnome.

Shelley Dwarf, gnome, what’s the difference?

Joy (Thinks for a second) Actually I have no idea. Second, since when have we had a spare key and it kind of creeps me out when you call my mom by her first name.

Shelley The spare key was actually my suggestion, thank you very much. See, Alicia and I were talking and I said, “Hey Alicia, wouldn’t it be a great idea to have a spare key? You could put it under the midget in the flower bed.”

Joy Ok, you can’t say that, it’s offensive.

Shelley What’s offensive about Alicia?

Joy Not Alicia…midget. Don’t say midget, say little person.

Shelley It’s funny, Alicia said the same thing. You two are so much alike.

Joy Why do you keep calling her Alicia?

Shelley Well, unless you were not aware, that is her name.

Joy But not for you to use. That’s like the name her friends use. You know, adults.

Shelley Hmmm, let’s see. A- I’m only a few months from graduating high school, which will practically make me an adult. And B- would you rather I call her Mom?

Joy Eeeww, no. Why don’t you call her Mrs. Baker or Mrs. B or you know… not Alicia?

Shelley Alicia is right, you could loosen up a bit. You need to chill out. Enjoy life because it’s like a big ole apple and you need to take a bite every once in a while.

Joy (Shocked) You and my mom talk about me?

Shelley Of course we do, we love you. But you can be a little…uh…rigid.

Joy Rigid?! I’m not rigid.

Shelley Hahaha. Alicia said you would probably say that.

Joy Ok, you have to stop calling her Alicia or I’m gonna lose it.

Shelley (Sing-songy) Rigid!

Joy I’m not rigid. It’s just annoying. You act like you two have been going to Pilates and driving carpool together or something. You are still a kid, like me.

Shelley (Laughing) Pilates, that’s funny. Nobody does Pilates anymore. Now hot yoga, I could go for that. I wonder if Alicia..I mean… your mom would like that?

Joy (Talking to herself) All I wanted to do was come home, relax a little, get my homework done, and maybe watch the Real Housewives of wherever. But nooo. I come in and get attacked by my friend who has broken into my house..

Shelley …with a key.

Joy …with a key. And why are you here anyway.

Shelley I told you, I have made a huge decision and I wanted to share it with you.

Joy Don’t tell me you are giving up your dream of being a TikTok star or an Instagram influencer.

Shelley NO, never. With my natural charisma, my followers could blow up at any minute.

Joy You only have about 43 and most of those are family members and fake profiles you made up.

Shelley Which means my upside is unlimited. Pretty exciting, right?

Joy I gotta give you props for being positive.

Shelley That’s a very important trait to make it in this current media climate. Or at least that’s what is being said on Reddit. Or was that Insta? Doesn’t matter, it’s true. I am just one click away from being the next “I-did-nothing-to-deserve-this-fame-except-be-online-all-the-time.” Don’t worry though, I won’t forget you.

Joy Speaking of not forgetting. You have never told me why you are here. What’s the big decision?

Shelley Oh, right. After much thought and deliberation, I have decided to get…

Joy Another tattoo?

Shelley No, but should I?

Joy No, because nobody has seen the first one.

Shelley But it’s there, I promise.

Joy Are you getting a hoverboard? You really shouldn’t because you aren’t very coordinated. You would kill yourself.

Shelley That’s not true.

Joy Oh really. Did you forget the ice skating disaster during Christmas break of 9th grade?

Shelley Come on. It wasn’t that big of a deal. I lost my balance and bumped into a few kids.

Joy You wiped out half the high school hockey team and they were wearing pads. And what about the time you went bowling and somehow knocked the power out to the entire shopping center.

Shelley Who puts the electrical thingies so close to the lane…that’s just dumb.

Joy Then there was the time you flooded the soccer field…

Shelley Alright. Maybe I’m not the most graceful person. However, I am not getting a hoverboard. I’m getting a dog.

Joy NO.

Shelley Yes.

Joy No,no.

Shelley Yes, yes.

Joy A dog, really?

Shelley Really. I just think it’s the perfect time and an excellent idea.

Joy Have you ever had a pet before?

Shelley Nope, never have.

Joy And you think this is a great idea?

Shelley I sure do. In fact, I doodly do do.

Joy This is crazy. You don’t have any idea about what it’s like owning a dog.

Shelley Do you?

Joy No, but I’m not getting one.

Shelley Or are you?

Joy What does that mean? Or are you?

Shelley That’s the beauty of this plan. You and I will discover the joys of pet ownership along with the bonding that comes with co-parenting a deserving canine.

Joy Co-parenting? You aren’t dragging me into this insane plan of yours. I don’t have a dog and I don’t want a dog. I have enough to do in my life already.

Shelley Come on now. Haven’t you seen those videos? Cute little puppers with big brown eyes that look at you with nothing but love. Did you know that dogs are the only animal that loves you more than they love themselves?

Joy Do you really think I’m gonna fall for this? I am not about to waste time during my final high school days, when I’m already writing research papers, doing projects and studying for final exams, just to help you raise a dog.

Shelley You are looking at this all wrong. This will be a pleasure not a chore. Your life will be forever enhanced by giving your love to an animal that wants nothing more than to make you happy. Just think, you have had a tough day where nothing has gone right and then you get home and open the door and there is a fuzzy face that is so happy to see you.

Joy Are you talking about a dog or are you making fun of my brother?

Shelley Well, you have to admit. He looks really funny with that scraggly beard.

Joy True.

Shelley But yes, I’m talking about a dog. Not just any dog. Our dog. Who we will teach to be smart and loyal and friendly.

Joy I don’t have time to go to a pet store and help you pick out a dog anyway.

Shelley Pet store! What are you? Some kind of monster?

Joy What did I say?

Shelley We aren’t getting our dog from a pet store.

Joy Well I didn’t think you could get them from Amazon.

Shelley (Softly laughing) Joy, Joy, Joy. You really don’t get it. We are not going to get a dog from a pet store or online. We are going to rescue our dog from an animal shelter.. We are going to save a life.

Joy (Pause.) Well, I must admit, that does sound pretty nice.

Shelley It’s not just nice, it’s fantastic. We will be giving a dog a second chance and in turn, you know what we get?

Joy Hair on our clothes and chewed up shoes?

Shelley Instant Karma. Lots and lots of good karma.

Joy As good as this all sounds, I’m not a dog person and up until today, neither were you.

Shelley Hey, people change and not just their hairstyles.

Joy But a dog is a huge responsibility.

Shelley Exactly and Alicia… I mean your mom thinks it would be a fantastic experience. Plus, you know what they say?

Joy Who?

Shelley The people who say stuff, those people. They say, “The world would be a nicer place if everyone had the ability to love as unconditionally as a dog.”

Joy Wow, you are really trying to sell this. I’m still not sure. I just don’t think I’m a dog person.

Shelley That’s only because you haven’t been one before.

Joy Well neither have you.

Shelley I am now or at least I’m gonna be. With or without you. So are you going to help me or not?

Joy (She thinks about it. ) Nah, I just can’t do it.

Shelley Your loss. (She starts to walk out.)

Joy (Watches Shelley leave and then suddenly says.) What are you gonna name it?

Shelley (She stops and turns.) I don’t know, I haven’t seen it yet.

Joy (She thinks and finally says.) Well, I guess I better go with you or you will give it some stupid name.

Shelley (Smiles) No I won’t. You will be the one that does that. (They start walking off.)

Joy Please, I’m a great namer.

Shelley Ha, you will probably want to call it Vanderplump or something.

Joy Oooh, I kinda like that…. (Exit)
```

---

## IC-0627: The Main Character

- Title: The Main Character
- Author (byline): Kevin J. Burgun
- Work: The Main Character
- Publisher: Mushroom Cloud Press
- Publication date as stated: September 1, 2021
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1734
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
CHARACTERS

Grace

Patty

Teacher

Student 1

Student 2

Student 3

Little Sally

Young Grace

Becky Simmons

The Main Character

(Grace starts front waving over her shoulder. Patty

character starts at her back for sound effect

purposes. Patty yells “WATCH OUT” and Grace

screams. Patty makes crashing and brake

squealing sound effects.)

Patty Are you okay?

Grace I think so.

Patty You crossed the middle of the street and almost got hit by that bus!

Grace It swerved just in time.

Patty Luckily all those cars were in the oncoming traffic lane to slow it down.

Grace Phew.

Patty You know what this means, right?

Grace What?

Patty You are the main character!

Grace What now?

Patty The main character!

Grace The what?

Patty The main character!

Grace The wha-

Patty The main character!

Grace I am completely lost here.

TRANSITION

Patty is now the teacher, and Grace the students

Teacher Please be seated. Posture please. No slouching. That’s still slouching. Still slouching. Still. Sit up. Sit. Right. Up. There you, oh, right back down again. Okay. (Clears throat) Today’s lecture is on The Main Character.

In any good story there are FIVE types of characters. But today we will focus on….yes, we have a question already?

Student 1 May I go to the bathroom?

Teacher No.

Student 1 What if I stop by the vending machines on my way back and bring you some flaming hot cheetos?

Teacher And a Diet Coke?

Student 1 Done.

Teacher Done. Alright. Now, there are five basic characters, but we are going to focus on...

Student 2 Five characters according to who?

Teacher Whom. And Joseph Campbell. Well, at least what I remember from when I read him back in college.

Student 2 Didn’t he write a Hero with a Thousand Faces?

Teacher He did.

Student 2 So, doesn’t that mean there are a thousand types of characters?

Teacher Shut it.

Student 3 You can’t say that.

Teacher I can because you are not the main character. You are a minor character.

Student 2 How do you know you aren’t a minor character?

Teacher Focus! You know you have a main character when they 1) have a compelling backstory that drives who they are, usually tragic, 2) have a loyal sidekick, 3) cannot be gravely injured physically or emotionally no matter what happens, and 4) things usually work out for them.

Grace Like when I walk in front of a bus and it swerves and hits oncoming traffic instead?

Teacher Exactly. You are the main character.

Student 3 What about a minor character?

Teacher Oh, you for sure can be injured or die. Sometimes that’s the only purpose of your character.

Student 3
What?
Teacher
Watch the first five minutes of any action movie.

Grace But me?

Teacher You could jump out of a fourth floor window into some fire escapes and fall to the ground, you will have minor cuts and bruises and immediately jump and walk away with a slight limp that will disappear in a minute or so.

Student 3 What would happen if I jumped out of a fourth floor window?

Teacher You would spend the rest of the story in traction in the hospital.

Student 3 What?

Teacher At best the main character would visit you after her story is over to share one callback joke to sort of wrap up the story. Turning your tragic accident and long physical therapy journey into a throwaway joke because the main character is the most important character.

Grace And I’m the main character.

Patty And that must make me the sidekick!

Grace I’m sure you are a main character.

Patty My name is Patty, that’s not a main character name. And I’m on the chess team. Sidekick.

Grace Well, don’t main characters have an arch nemesis? I don’t have an arch nemesis.

Teacher They do.

Grace The closest I can think of is Becky Simmons, but that was back in third grade.

Teacher Oh no!

Grace What?

Teacher You are the main character and you referenced an incident from your past. You know what that means?!

Grace What?

Patty Flashback!

FLASHBACK TRANSITION Grace It’s lunchtime!

Patty I can see that! Look! There you are!

Grace Oh no, it’s bartering time.

Patty Bartering?

Grace Becky Simmons was a master barter-er-er-er (pause) er

Patty We get it.

Grace She would have these very intricate trades, and she would always end up on the better end of the deal.

Patty What would she get?

Grace Peaches, Pez, Goldfish, Goldfish Pretzel, Goldfish colors, Goldfish whole wheat, Goldfish pizza, Goldfish Parmesan.

Patty Wait, there’s a Goldfish Parmesan?

Grace Yes, they are delicious.

Becky Okay everyone, it’s barter time. Hello little Sally.

Sally Hi Becky Simmons.

Patty You used to be called Sally?

Grace No, that’s not me, I’m using this as an example for how mean Becky was.

Patty Got it.

Grace No problem. Now let’s get back to the story.

Patty and Grace Flashback

Grace I forgot where I was.

Patty You were….I forgot as well.

Grace Let’s just take a moment, it will come to us.

Long Pause
Patty
It looks like someone is taking notes over there, maybe they know where
you were.

Grace I remember.

Becky Hello Little Sally, would you like to …..trade? (Evil laugh)

Sally That was quite the evil laugh.

Becky It’s not an evil laugh, that’s just how I laugh, it’s genetics, I can’t change genetics.

Sally Okay, I’ll trust you. That seems like not a bad idea at all to do so. Trusting. That is.

Becky Give me your apple slices.

Sally Here you go.

Becky These are Fuji apple slices?!

Sally I know, they are my favorite.

Becky Haven’t you checked the apple market recently? Fuji apples aren’t THE apple anymore. Their stock is down.

Sally What? My mother bought them just last night and she paid a ton for them.

Becky Your mother was robbed. Sure, last week, for these slices, I could get you two, maybe even three packs of Goldfish crackers, but today? You’d be lucky to get two, maybe three actual goldfish crackers.

Sally Really?

Becky And I am talking cheddar, not the good ones, like pizza or parmesan.

Sally Cheddar are my favorite.

Becky I can get you four goldfish crackers for those apple slices then.

Sally Oh, ummm

Becky Now if you had granny smith apples.

Sally But I don’t like granny smith apples.

Becky No one does, but they make for great pies, and apple pies are big right now., Big!

Sally Apple pies are back in? I thought blueberry pies were in?

Becky Blueberry? What are they teaching you in second grade? This education system is broken.

Sally I know my colors.

Becky Because I like you and you are still learning, I’ll give you six whole goldfish crackers for your Fuji apples.

Sally Thanks, Becky!

Becky Next!

Grace This is me, I’m next.

Patty That was a terrible trade.

Young Grace Becky.

Becky Ah Young Grace. I have some Fuji apple slices for you.

Young Grace Fuji! Wow, those are the good ones, right?

Becky Oh yes, they are the most valuable of the apple slices. That’s for darn sure.

Young Grace Well, all I have is a peanut butter and honey sandwich, gogurt, rocking strawberry punch Capri-Sun.

Becky That’s all well and good Young Grace, but you failed to mention those Doritos I spy.

Young Grace But those are my Doritos.

Becky I want those Doritos. And there is no “RF” on them, that means.. They are not reduced fat? (Evil laugh.)

Young Grace That’s kind of an evil laugh.

Becky It’s genetics. Little Sally, what are you doing here?

Sally I have buyer’s remorse. Can I have my Fuji apples back since they are worthless?

Becky Worthless?! Who told you that? (Nervous chuckle.) Why don’t you ...oh look! Johnny is trying to steal your lunchbox, you better go stop him.

Sally Johnny, no!

Young Grace The apples are worthless?

Becky Second graders. You know how they are. I blame recess. Too much recess. Our education system is terrible. I said “apples and oranges” to her yesterday and she got confused. Where were we?

Young Grace So, I get Fuji apples for my Doritos.

Becky And it’s the big bag. Your mother must love you very much.

Young Grace It’s mostly guilt. I got blamed for something my father did, and she burned dinner.

Becky Guilt Doritos are the best kind. Let’s trade.

Young Grace Okay.

Becky Let me tell you, those Fuji Apples are worthless! (Evil Laugh)

Patty That was the flashaback?

Grace Yes.

Patty That was it?

Grace Yes.

Patty But.

Grace I never trusted anyone else again. Ever.

Patty You trust me, right?

Grace Sure.

Patty That seems like….not a great origin story for a main character.

Grace What do you mean?

Patty Your mom burnt dinner one time, and then you got tricked out of Doritos and got some apples instead?

Grace Really shaped who I am.

Patty Okay, well,

Grace I stubbed my too once.

Patty Teacher said there were four things that made a main character. 1) have a compelling backstory that drives who they are, usually tragic.

Grace Check.

Patty Sure. 2) have a loyal sidekick. That’s me. Check.

Grace Should we test the loyalty?

Patty 3) cannot be gravely injured physically or emotionally no matter what happens, and 4) things usually work out for them.

Grace Well, I didn’t get hit by that bus, so that sort of is both of those, right?

Patty Sort of, though I think we should throw you out of a fourth story window just to be sure.

Grace What?

Patty Just sort of…

Grace No.

Patty But…

Grace Look, if I’m the main character or not, will that change anything?

Patty It will change how you live your life!

Grace Maybe we should just all live like we are the main character of our own stories.

Patty Could you be any more cliche?

Grace (Phone rings) Hello? Who? (Whispers to Patty) It’s Becky Simmons.

Patty This is not just a coincidence.

Grace Sure. Really? Huh. Okay, I suppose. (Hangs up.)

Patty What?

Grace She wants to meet. She said she has a deal for me.

Patty Did she say what it was?

Grace Just that I’ll never look at breakfast shakes the same way after she talks to me.

Patty You have to meet her. Your archnemesis.

Grace I know. I just have to run home and change real quick.

Patty Okay, but you should probably cross at the corner.

Grace (looks both ways) I think I’m good. (Mirroring the beginning she walks and waves over her shoulder.)

Patty WATCH OUT!

BLACKOUT
```

---

## IC-0628: Beauty Boot Camp

- Title: Beauty Boot Camp
- Author (byline): Marissa Malloy
- Work: Beauty Boot Camp
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2094
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
(In a high school bathroom, a nervous girl, Margaret, approaches a mirror.)

Margaret: Hey James. There's something I need to ask you. Now, I know that you don't really know me, or have ever talked to me, or have probably heard even a faint whispering of my existence, but…. I think that…your face, is the…goodest, face…of all of the faces...and prom is next week, and--

(A pretty, primped girl walks up to the mirror next to her.)
Margaret: I’m going to die of embarrassment now.
Samantha: Are you okay? You look like your heart's about to explode out of your butt.
Margaret: No. Wait, yeah! I mean. I'm fine. I was just, uh…you know. Rehearsing a scene. In the
bathroom mirror. It is for…scene, class. Bye.

(Margaret rushes to leave, but Sam pulls her back.)
Samantha: No, come back! Maybe I can help. I happen to be very knowledgeable when it comes to
romance. And...everything in general.
Margaret: Thanks, but I really am a sane human being. That whole thing I was doing back there was just a
joke. Ha! Got ya good. Look who’s embarrassed now. You are. That's who.
Samantha: I like you. I’m Samantha.
Margaret: Marga--
Samantha: Oh my god, your name is Margaret? Gross.
Margaret: Uh...ha. You’re joking, r--
Samantha: We’re gonna call you Erika from now on, ‘kay Erika? With a ‘k’.
Erika: A...‘K’?
Samantha: ‘Kay. Next crisis…
Erika: Crisis?
Samantha: You need some lipstick…
Erika: Lips--

(Samantha forces lipstick on “Erika's” face.) Samantha: A mist of perfume...

(She sprays it in Erika's face.)
Erika: Ow, my eyes!!
Samantha: And we'll finish the whole thing off with some powder!
Erika: No, stop! Please!

(She powders her up, Erika coughs. Samantha scans her up and down.)
Samantha: Alright...Good. Bad. Better. Huh. How does that even look like that?
Erika: Okay, WHAT THE HELL--
Samantha: Erika, with only two minutes of my help, you're already the second prettiest girl in this
bathroom.
Erika: We're the only two in here...
Samantha: If you give me this whole week to mold you, change you, fix you, correct you, save you--
Erika: I get it--
Samantha: I will get James Masterson to be your prom date. Do we have a deal?
Erika: Hm...how do I know I can trust you?
Samantha: We met in a bathroom, what's not to trust?
Erika: Oh god, I'm desperate.

(In Samantha's bedroom, Erika brushes her hair.)

Samantha: Okay, lesson number seventy-one...no matter what a guy says, throw your head back and laugh like this...

(She performs a laugh that even Julia Roberts would consider 'too much'.)
Erika: I'm not doing that.
Samantha: Yes you are.
Erika: False.
Samantha: And you're also wearing this.

(She hands over a strand of cloth.)
Erika: Where's the rest of it?
Samantha: Okay, now that your outsides are looking a little better, let's repair your insides.
Erika: Man, if I had a nickel for every surgeon who's said that to me...I'd have thirty cents.
Samantha: Okay, bonus lesson? Don't try to be funny. You're welcome for that. Now. I'm going to list off
random things that a boy may talk about, and I want you to respond like you're actually interested in
them. Okay, first noun: off-road vehicles.
Erika: Roads? Who needs em!
Samantha: Fighting.
Erika: I would love to punch you in the mouth right now.
Samantha: Football.
Erika: Well I was the starting linebacker for the Chicago Bears in the 1950's don't ya know! Wanna toss
around the pigskin young chap?
Sam: Maybe it's best if you just don't talk at all. Now, chin up...

(Sam slaps her chin.) Erik: Ow! Sam: Shoulders tall...and show us the biggest, prettiest smile you've got!

(Erika poses with a pained, hideous smile.) Erika: Did it happen? Am I finally pretty, Sam?! Samantha: (long pause) Okay time for your next lesson!

(The girls walk down the school hallway.)

Samantha: Okay, lesson number whatever. Walking down the school hallway is literally the most important way to attract guys because literally everyone in the school is watching you. Erika: That is literally not possible. Samantha: You looking pretty seemed impossible too. Now, watch how I walk...(struts) I'm bouncy, fun, confident, with just a hint of 'Hey how ya doin'?' thrown in for good measure. Got it? Erika: Yes, walking. Because I didn't know how to do that previously. Thank you. You know, my cousin just learned to walk and he's fourteen. Months. How old are you? Samantha: As I will eternally claim, I'm a wise twenty-one. Now, show me your best walk! Erika: Okay...

(She slumps through the hallway.) Samantha: Oh god you look like a depressed orangutan.

Erika: You're teaching me how to walk, this is so stupid!
Samantha: (gasps) Stupid?! You're calling my training...STUPID?!
Erika: Yes.
Samantha: I mean, how could you?!
Erika: Very easily.
Samantha: Fine. If you want to walk like you're filled with buffalo tranquilizer, be my guest. I guess it's
time for more hands on training.
Erika: Cool, like what--
Samantha: Oh hello, boys.

(Samantha nudges Erika. She sees that they're now across from two bro's putting their backpack items
into their lockers.)
Samantha: Don't you want to greet them, Erika?
Erika: What are you up to this fine day.
Boy 1: Nothing man! We’re just putting stuff in our lockers!
Boy 2: Our lockers, man!
Boy 1: Totally, bro. I said that too!
Boy 2: Brooo.
Sam: (does her weird laugh) Oh my gosh, you guys are like so funny! Don't you want to tell them how
funny they are, Erika?
Erika: Ah, yes. Yes that was quite humorous indeed. What would you gentlemen care to discuss next?
Politics, perhaps? Literature? The existence of parallel universes? Hmmmm?
Boy 2: Whoa man. This reminds me of that time when you were really smart, but then you hit your head
on that ceiling fan and then we’ve been best friends ever since. You remember that?
Boy 1: Mannnn! No, I don’t…
Boy 2: Oh...
Erika: Concussion symptoms! What a delight.
Samantha: Yeah, it's definitely better when you don't talk. Do the smile I taught you.
Erika: And now, males, I am smiling at you...

(She does her weird smile from before. It's still just as weird. Maybe even weirder...)
Bro 2: This is uncomfortable.
Bro 1: Yeah dude.
Erika: And now if you'll excuse me, I’m going to walk away now and pretend this conversation never
happened. Bye bye.

(Erika walks away, sending Sam into a tailspin.) Samantha: What?! I'm sorry, uh, excuse us guys. We'll be back!

(She does her weird laugh as she heads after Erika.)

(In the next hallway, Sam catches up to Erika.) Sam: Hey, you can't just walk out on a lesson like that! You agreed to listen to me, my help, my guidance, my show, me me me me me-- Erika: Why should I listen to you, Sam? Because you shoved lipstick on my face and gave me a sock to wear as a shirt? Sam: No, you should listen because I’ve had more boyfriends than you’ve had cheeseburgers. Erika: Oh. You'd be surprised. When are we actually going to do something...you know...helpful?

Sam: You say that like we've been wasting our time. Erika: We talked to guys with the IQ of butter and you called me an orangutan. Seriously, I'll do whatever as long as it's, oh I don't know...actually useful! Sam: Hm. Anything? In that case...I think I know just how to take your training to the next level... Erika: Great, fine, cool, swag. Let's do it.

(We're now in Erika's bedroom. Sam preps a strip of wax on Erika's leg.) Sam: ...two, three!

(Sam rips off the strip.)
Erika: ...OWWW YOU PSYCHO SPAWN OF SATAN AND...AND...SATAN’S WIFE!
Sam: Erika, I’m helping, will you let me help?
Erika: You...are ripping...all of the hair out--
Sam: Yes I am. Ready for the next one?
Erika: No, no, false--

(Sam rips her again.)
Erika: SON OF A BISCUIT! What is wrong with you?!
Sam: Nothing. That's why I'm the one helping and not the other way around. Now let's hurry to jazzercise
class!
Erika: Whoa, what--

(Sam whisks Erika away and we're suddenly in an aerobics studio, with girls dancing along to a routine,
Erika failing with fatigue.)
Erika: Oh please. Make my life stop. No more life please.
Sam: Suck it up, we've got another stop to make!
Erika: What?! Tomorrow, right--
Sam: Right now!

(Sam yanks her away. They stand in front of James Masterson’s house.)
Erika: (panting) I...am...very….much...not...a fan...of you.
Sam: Well that’s about to change. Guess where we are!
Erika: Please tell me it’s ice cream. Ice cream?! Is that you?!
Sam: We...are outside...of James Masterson’s house!
Erika: What?! I’m going to kill you!
Sam: Yes!
Erika: No! Murder! I can’t let him see me like this! I look like I was just birthed out of a sweaty sheep!
Sam: Erika...I’ve trained you. Don't you trust my training?
Erika: No.
Sam: Don't you trust me?
Erika: Not at all.
Sam: Well, I believe in you.
Erika: You really shouldn’t.
Sam: Too late, here you go…

(Sam shoves Erika up to the door. Erika’s face turns to shock as she looks up.)

Erika: H-...Hi, James…

(James, bulky with muscle, steps out.)
James: Uh, hello...sweaty girl?
Erika: Yeah, that. I was just...uh...sweating. Listen, James. I know you don’t really know me, but I am
really awesome. And I’m just a really great, awesome person that you should get to know. You know?
And so, if you would be so kind as to go to prom with me...
James: Whoa whoa whoa hold up, stop. Stop right there.
Erika: Okay.
James: Stop.
Erika: I'm stopping.
James: Are you stopped?
Erika: Yes.
James: Good. Now look, I don’t even know who you are, why the hell would I go to a sweaty prom with
you? I mean you could be like...a murderer? Or like, somebody who runs around stealing cheese out of
people's houses!
Erika: I would nev--well…
James: Look. You made my porch wet and you smell like my grandma after she goes up the stairs. Please
leave. I have a taser.
Erika: Wow. I really should’ve spoken to you before I fell in love, alright!
James: Taser!
Erika: Got it. Thanks James.

(Erika walks away. Sam meets her at the sidewalk.)
Sam: Well that went well...
Erika: What. The poo. Was that?! James Masterson? More like...James...Masterson-not! He is...not, the
son of a master--Look, Sam. I tried your way. I tried being a beautiful robot of beauty and I’m just not,
okay?! Listening to you has just led me to the front yard of a very attractive psychopath who threatened to
tase me.
Sam: Hey, do you think I’m happy?! I was already a beautiful robot of beauty and I wasted my week
helping you, so now I don’t even have a date for prom! Like some loser who’s good at math or
something.
Erika: Wait...the two of us need dates? Sam. I think we only have one option…
Sam: What did I say about math...
Erika: Sam, I think we have to...go...to--
Sam: Oh god, this is gonna be the worst prom ever, isn’t it?
Erika: Quite possibly.

(Sam and Erika slow-dance at the prom, cry-singing along to the music.)

Erika + Sam: Allll byyyy myyyyself….
Erika: You look beautiful tonight, Sam.
Sam: You know what, Erika? You do too. And I’m not just saying that as a joke that I’ll secretly laugh at
on the inside and also joke about with my friends afterwards.
Erika: Huh. Great, I guess...Look, I’m getting a little dehydrated. You want some punch?

Sam: Yes if it’s fat-free. Erika: Okay, so no punch.

(Erika walks over to the punch table. James sees her and approaches.)
James: Whoa, hottie alert! Hey guys, there’s a hot girl over here!
Erika: Uh...where? James? Do you mean--
James: You are like, super hot, girl. You wanna date me? Who am I kidding, of course you--
Erika: Uh, no, I’m good.
James: ...WHAT. Oh, wait, it’s a joke. Haha, funny joke hot girl! Now you’ll be my girlfriend and kiss
me on the face!
Erika: You know, if you had asked me that two days ago I would’ve drooled, cried, said yes, and then
celebrated by screaming for joy around my neighborhood and telling all of my parent’s friends. But...you
know, you...YOU THREATENED TO TASE ME!
James: To be fair, you were sweating a lot…
Erika: Look, as I’ve heard other girls say, ‘if you’re not interested when I’m at my worst, don’t expect to
get me at my best’. Which isn’t even now, by the way, I can crank this hotness up to 11.
James: Whoa...
Erika: Now imagine that as I walk away.
James: (imagining) Aw, man, it’s so amazing!

(Erika walks back onto the dance-floor. Sam rushes up to her.) Sam: Oh my god oh my god oh my god, did James Masterson just ask you to dance?! Erika: Hm. He said a lot of words, but 'dance' wasn’t one of them. Look, Sam, I appreciate everything you’ve done for me, but the truth is it’s stupid to care this much about how you look. I mean, obsessing over every physical detail, playing whack-a-mole with your flaws...all it does is make you dislike yourself. And I like liking myself. So, yeah. Sam: (smiles, applauds) Bravo. Everybody, bravo! Erika: Uh, Sam, what are you doing? Sam: With that final lesson, you have officially graduated from Beauty Bootcamp! Erika: Hooooow….? Samantha: When I first saw you in that bathroom talking to yourself like a really weird weirdo, it didn’t make me want to change how you looked. It made me want to change how you felt. About yourself. No guy is ever worth making you hate yourself, ever. Okay maybe Brad Pitt, but that’s it. So...May I have this dance, Erica? I mean--Margaret? Margaret: Why yes, Samantha. I mean—Samantha...

(They slow-dance, teetering gently to the music.)
Sam + Margaret: Alllll byyyy myyyselffffff
Sam: You were a little flat there…
Margaret: Shut it.
```

---

## IC-0629: Birthday Candles

- Title: Birthday Candles
- Author (byline): K.R. Schneider
- Work: Birthday Candles
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1369
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
(Twin girls, Sam and Sawyer, sit back to back.)
Sawyer: Twenty three candles this year.
Sam: Twenty-three is a lot.
Sawyer: You thought nineteen was a lot.
Sam: So imagine how I’m feeling now!
Sawyer: Old?
Sam: Practically ancient!
Sawyer: You know, Mom and Dad are like twice that.
Sam: Yeah, Sawyer, and they’re old!
Sawyer: I think, Samantha, they’d be offended by that.
Sam: Oh, old people get offended by everything.

(Laughter; brief silence. Sawyer is plucking at a bouquet of flowers in her lap.)
Sawyer: Hey, thanks for the flowers.
Sam: Well it is our birthday.
Sawyer: Not yet it isn’t. What time is it?
Sam: (checks watch) 11:18
Sawyer: (exasperated) Like forty more minutes!
Sam: She says like it’s such a chore to hang out with me.
Sawyer: You are kind of a headache.
Sam: Oh whatever; I’m a joy to be around.
Sawyer: You know, I thought the younger child was supposed to be the entitled one.
Sam: (surprised) You’re not younger. We’re the same age.
Sawyer: Nope. Technically I am younger.
Sam: And you say I’m a headache.
Sawyer: You are!
Sam: Oh like when?
Sawyer: Does our 8th birthday ring a bell?

(Flashback to 8th birthday; Sawyer stands on chair, holding a hamster in the air above her head.)

Sam: SAWYER, PUT PEBBLES BACK IN HER CAGE! Sawyer: TELL MOM THAT YOU WANT TO HAVE CHOCOLATE CAKE WITH PINK FROSTING!

Sam: No! It’s MY turn and I want white cake with green frosting!
Sawyer: Pink and chocolate, Sammy, or the rat GETS IT!
Sam: Mom! Sawyer is gonna kill Pebbles!
Sawyer: You are SUCH a BABY!
Sam: If you kill Pebbles, I’ll kill YOU!
Sawyer: MOOMMM! Sammy is gonna kill me!
Sam: Gimme Pebbles!
Sawyer: I’m gonna bake her in the stupid cake!
Sam: Mom!
Sawyer: Mom!
Sam and Sawyer: MOM!

(Back to the present; both girls are laughing.)

Sawyer: You were being a serious baby.
Sam: It was MY turn!
Sawyer: You got your white cake didn’t you?
Sam: Yeah, but it had pink frosting!
Sawyer: (laughs) Yeah, well...Mom always was the master of a compromise.
Sam: She was a pro at that whole: “it’s the same; it’s just different” crap.

(Flashback; 13 years old; in the backseat of the car)

Sam: I didn’t want the same pencil bag as Sawyer!
Mom: They’re not the same, Samantha. Yours is blue.
Sawyer: How come Sam gets to have a cooler backpack than me!?
Mom: They’re the same, Sawyer; yours is just green.

(Back to the present)

Sawyer: Quite a woman: our mother. Sam: Definitely sainthood material.

(Brief silence; the tone seems to shift; Sam tries to lighten it again).
Sam: Favorite birthday - go.
Sawyer: Hmm. Six was definitely up there: the face paint, the bouncy castle.
Sam: Six was terrible! I broke my arm in that stupid castle!
Sawyer: (laughs) That’s right; you cried all your face paint off.

Sam: I went to the hospital looking like a pink and purple snot ball. Sawyer: Yeah; you were an awfully sad butterfly.

(Flashback ; six years old; in the car on the way to the hospital; Sam has a broken arm.)

Sam: It hurts, it hurts, it hurts, it hurts!
Sawyer: (rubbing her own arm) Don’t cry, Sammy! Your pretty butterfly will smudge!
Sam: I hate stupid bouncy castles!
Sawyer: (determined) Me too!
Sam: I hate stupid face paint!
Sawyer: (slightly less determined) Me too!
Sam: I hate my stupid birthday!
Sawyer: (brief pause) Me too.

(Sam notices that Sawyer is holding her own arm and touches it softly).
Sam: What’s wrong with your arm?
Sawyer: (concerned) Sammy, are you gonna get a cast?
Sam: (upset) If they make me!
Sawyer: I’ll get one too. Then we’ll be the same still.
Sam: (lays her head on Sawyer’s shoulder) We’re the same all the time.

(Back to present)

Sawyer: They wouldn’t give me that cast no matter how much I begged.
Sam: When they told you no, I think you cried more than I did!
Sawyer: I wanted us to be the same.
Sam: We’re always the same.
Sawyer: Sometimes that’s not the best thing.

(Flashback; fifteen years old; Homecoming; both girls are wearing the same dress).

Sawyer: You can’t wear that!
Sam: I picked it first!
Sawyer: Did not!
Sam: Did too!
Sawyer: I told you we should have gone shopping together!
Sam: I wanted to pick my own dress!
Sawyer: Well you didn’t pick your own dress, Samantha, you picked MY dress!

Sam: Shut up, Sawyer! Maybe YOU picked MY dress!
Sawyer: Did not!
Sam: Did too!
Sawyer: Shut up! Change!
Sam: You change!
Sam and Sawyer: MOM!

(Back to present).

Sawyer: Lesson learned.
Sam: Don’t shop separately.
Sawyer: You know, that homecoming dance was actually fun.
Sam: Ohhh right! You kissed Tommy Higgins.
Sawyer: My first kiss.
Sam: The first kiss.
Sawyer: It’s probably the only thing I ever did before you.

(Flashback; after the dance; fifteen years old; Sam on the top bunk; Sawyer on the bottom).

Sam: Where?
Sawyer: Uh...my mouth.
Sam: No, dummy. Where. Like on the dance floor?
Sawyer: In the hallway by the first floor trophy case.
Sam: That’s a good hallway!
Sawyer: Why is that a good hallway!?
Sam: Well, you got kissed there right? So it MUST be a good hallway!
Sawyer: (laughs) I guess.
Sam: So!?
Sawyer: So what?
Sam: So you got kissed, Sawyer! What was it like!?
Sawyer: Uhm...warm?
Sam: Gross. Warm? That’s the best you can come up with?
Sawyer: Well, I don’t know, Sam! It’s not like I was taking notes! It was a kiss.
Sam: Oh sure, like we all know what a kiss feels like!
Sawyer: (sighs) It was...kind of awkward, and I laughed, and he seemed kind of shy…
Sam: So it was incredible?
Sawyer: Yeah...it was incredible.

(Back to present).

Sam: I heard he got married last year.
Sawyer: Married? Woah. Tommy Higgins is somebody’s husband.
Sam: Jealous?
Sawyer: Nah. The first kiss was okay and all, but...
Sam: Not a tough loss?
Sawyer: Definitely not the great love of my life.
Sam: Yeah.
Sawyer: Hey Sammy?
Sam: Huh?
Sawyer: What ever happened to Paris? This was supposed to be the year for Europe, right? You
were gonna’ turn 23 under the Eiffel Tower and all that?
Sam: Paris is still there.
Sawyer: And you aren’t with it because?
Sam: Because I’m with you. It’s our birthday, dummy.
Sawyer: It’s your birthday.
Sam: No. It’s not. It’s ours.
Sawyer: I don’t think birthdays count anymore when you die. I don’t get older.
Sam: It’s still your birthday, Sawyer. You were born on this day. With me. You and me. Together.
It’s still our birthday.
Sawyer: Hey, I’m supposed to be the know-it-all in this relationship.
Sam: Not about this. You died. You relinquish your right to know best.
Sawyer: Sammy…
Sam: It’s our birthday, Sawyer. It is.
Sawyer: Okay. It’s our birthday. So...since it’s our birthday, can I put in a request?
Sam: What?
Sawyer: Go to Europe. Next year, turn twenty-four under the Eiffel Tower. Eat gelato, and fall in
love with some guy with an accent. Wear a beret.
Sam: A beret?
Sawyer: Whatever. Do anything, okay? Just don’t spend your--our birthday talking to a
headstone. Don’t bring me flowers, or eat cake in the cemetery like a weirdo. Have adventures.
Live a life.
Sam: I don’t want to go to Europe without you. I don’t want to see great places or eat gelato by
myself, Sawyer. I want to do it with you. And you’re not here. You left. You bailed on me, and
now it’s like I’m only half a person!

Sawyer: You’re a whole person, Sammy. And I didn’t bail! I wanted to stay. I wanted to grow up
and fall in love and eat birthday cake with you every year until we were 100! But it didn’t work
that way!
Sam: Why not!? It’s not fair! You went to that stupid party and you got in that stupid car like a
stupid idiot! You left me here, Sawyer, and it’s not fair!
Sawyer: I know. I’m sorry.
Sam: Do you know that by the time that they told me, I already knew? I could feel it: like all of a
sudden I didn’t have enough limbs.
Sawyer: It’s that whole twin thing.
Sam: And now I’m twenty-three, and I didn’t go to Paris, and I buy two of everything, and I hate
my birthday! And you’re still...nineteen.
Sawyer: I’m sorry, Sammy. (Sawyer lays her head back against Sam’s. They link fingers). I
wish...I wish a lot of things.
Sam: I love you, Sawyer.
Sam: I love you, Sam. (Brief silence. Sawyer taps Sam’s watch) Look. You’re twenty-three.
Sam: (checks watch) I’m twenty-three.
Sawyer: Samantha. I’d never really bail on you, you know? I’ll be around.
Sam: I never could go anywhere without you.
Sawyer: Like you’d want to.
Sam: No; I wouldn’t want to.
Sawyer: Next birthday...take me to Europe?
Sam: I’ll put your flowers under the Eiffel Tower.
Sawyer: That’s way cooler than a headstone. And you’ll eat cake underneath it?
Sam: Absolutely. Chocolate with pink frosting.
Sawyer: Twenty-four candles next year.
Sam: Twenty-four is a lot.
```

---

## IC-0630: Cavegirl Teaches Evolution

- Title: Cavegirl Teaches Evolution
- Author (byline): Clint Snyder
- Work: Cavegirl Teaches Evolution
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CAVEGIRL, BRITANY
- Teaser before the introduction: No
- Spoken words (computed): 1830
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
CAVEGIRL: Ooooga Booga!

BRITANY: Ahhhh! You talked!

CAVEGIRL: OOOOGA! Erm!

BRITANY: Oh my goodness, please don’t kill me, I haven’t even found out the true meaning of Christmas yet! Is it presents? Tell me! How am I supposed to know! (Gesturing wildly.)

CAVEGIRL: Erghhhmmm… That’s better. Sorry, 5 million years in a block of ice gave cavegirl really bad cough.

BRITANY: You can talk?

CAVEGIRL: Of course cavegirl talk! How you think cavegirl host such fabulous dinner parties.

BRITANY: Hi cavegirl… my name’s Britany… Umm… I have questions for you.

CAVEGIRL: Shoot!

BRITANY: Well-

CAVEGIRL: No, I meant shoot I forgot my good hairbrush. Now cavegirl’s hair will never look right…

BRITANY: Well, why is your name cavegirl anyway…. I mean what kind of a name is that?

CAVEGIRL: Why your name Britany. What kind of name that?

BRITANY: I… I dunno, I guess I never really thought about it.

CAVEGIRL: What Britany mean huh? At least Cavegirl give people an idea of who they are talking to.

BRITANY: You have a point.

CAVEGIRL: No cavegirl have a stick. (She throws it at Britany.)

BRITANY: Ow! What was that for.

CAVEGIRL: Oh, you know. Stick good for lot of things, start fire, chase animal, hit rude Britany…

BRITANY: You have a point…

CAVEGIRL: And now Britany have stick.

BRITANY: How did you get stuck inside of that ice anyway?

CAVEGIRL: Have Britany ever been swimming and then three weeks later get stuck in snow, then freeze in giant block of ice?

BRITANY: No… I usually go to the pool.

CAVEGIRL: Oh, well have Britany ever had brainfreeze.

BRITANY: (Suddenly excited.) Yes! I have had one of those!

CAVEGIRL: Well is nothing like that… Is million times worse than brainfreeze.

BRITANY: Oh…

CAVEGIRL: What does Britany have in hand?

BRITANY: Oh, you know… It’s just the new galactic smart phone.

CAVEGIRL: (Pause. Blank stare.)

BRITANY: It’s just the latest in mobile technology… you know?

CAVEGIRL: No… cavegirl not know.

BRITANY: Well, you can use it to update your status or go shopping online or you could even play games on it. I just downloaded an app that can tell you if your boyfriend is cheating on you.

CAVEGIRL: (Pause.) Iphone seems like waste of time.

BRITANY: Yeah… kind of, but all the cool kids have one.

CAVEGIRL: Cavegirl cool, cavegirl frozen in block of ice for 5 million years.

BRITANY: Yeah, you know that is totally cool. Say cavegirl do you have a squeeze?

CAVEGIRL: What Britany mean squeeze.

BRITANY: You know a squeeze. A boytoy. Like the one.

CAVEGIRL: One time boy get too close to Cavegirl and she squeeze him till he bleed!

BRITANY: Wow, I like you. You’ve got spunk. And I totally know what you mean it is so annoying when guys get too clingy.

CAVEGIRL: Yes… Britany annoying.

BRITANY: You know you’re really kind of pretty in a gross way. I mean I could show you a really good conditioner that would help restore your hair that was damaged by the ice. I also know the perfect oatmeal based exploiant that would do wonders for your skin.

CAVEGIRL: (Pause.) Britany talk too much.

BRITANY: (Oblivious.) I know right. I also have this aunt that could tweeze the dickens out of those eyebrows so that they no longer look like a gross fuzzy caterpillar.

CAVEGIRL: Ooooga booga! (She hits Britany.)

BRITANY: Owww!

CAVEGIRL: Sorry, years in ice must have made cavegirl’s muscles stiff. (Quietly laughing to self.)

BRITANY: That’s why I really like you cavegirl. You’re brutally honest. It’s like super refreshing. It’s like an ice cold bottle of my favorite mineral water.

CAVEGIRL: (Smiles badly.) He!

BRITANY: Oh my goodness! Cavegirl! You’re gorgeous! How have you been hiding this from me the whole time?

CAVEGIRL: (Bashful.) Cavegirl just good at keeping secrets I guess.

BRITANY: I love that… a woman with a mystery… I feel like I’m like Nancy Drew and you’re like her hideous sidekick or something… It’s perfect.

CAVEGIRL: Nancy Drew not have sidekick.

BRITANY: Oh whatever… how would you know anyway… you’ve been stuck in a block of ice for like a billion years… the only thing you’ve been able to look at is your ridiculous arm hair… It’s like a bunch of little tree trunks… like there is a forest growing out of your arms… a hair forest.. LITERALLY.

CAVEGIRL: Arm hair keeps Cavegirl warm… ice is cold.

BRITANY: You know… I never really thought about that Cavegirl… I can tell already we’re going to be biffles because that was like something only a girl scout could think of… I got kicked out of the girl scouts… guess they just couldn’t handle me.

CAVEGIRL: Who kick Britany?

BRITANY: Oh, you know some pretentious little goodie-two shoe mother and I say that because she probably only has two pairs of shoes… LITERALLY… The kicked me out because I ate like fifty boxes of their cookies or whatever… It’s totally not my fault though… like one of those crazy pyramid schemes you know…

CAVEGIRL: Uggghh…

BRITANY: Uggghh is right… Corporations.. LITERALLY… You know incidentaly that was the only merit badge I got. I accidentally got a hunting clothes merit badge because a pair of camouflage pants got mixed in with a bunch of real clothes I was getting… who knew… I mean they practically make those things invisible. CLOTHES ARE MEANT TO BE SEEN AND WORSHIPPED!

CAVEGIRL: Yawn… (She slaps herself)

BRITANY: Cavegirl… are you alright.

CAVEGIRL: Cavegirl was just trying to keep herself awake because your story was so boring.

BRITANY: Yeah… I guess I’m getting pretty tired myself… I could really go for a double expresso mocha latte right about- (Cavegirl slaps her.)

CAVEGIRL: Uggg!

BRITANY: Wow! That was powerful… we’re like sisters… from different misters and misses…. And eras… but who cares I love you and we are going to spend so much time together!

CAVEGIRL: Great… (Flat)

BRITANY: I’ll tell you what… you teach me how to be a stronger woman and I’ll teach you how to get the perfect man.

CAVEGIRL: Man not perfect.

BRITANY: You can say that again sister! Where have you been my whole life?

CAVEGIRL: Cavegirl was frozen in ice.

BRITANY: Right… right… that whole thing… So, like say I’m super mad at a guy and I just want to show somebody who’s boss… like the lady boss with fabulous lipstick and high heels to the heavens.

CAVEGIRL: Hmmm… you set his cave on fire.

BRITANY: Ooooohhh! Spicy, I like it! It’s a little more forceful than I would go for, but that’s why you’re here isn’t it.

CAVEGIRL: Cavegirl here because ice melted.

BRITANY: Right.

CAVEGIRL: Global warming.

BRITANY: Right, well enough about glowing warnings… say there is this guy that you think is cute and is totally single and ready to mingle, but after you tell him five minutes later you see like your best galpal kissing him… on the lips… like what would you do?

CAVEGIRL: Hmmmmm… You find big rock…

BRITANY: Find a big rock.

CAVEGIRL: You pick up.

BRITANY: I bet that’s where you got those biceps.

CAVEGIRL: You smash both over head and take their furs.

BRITANY: I like how you think, let them know you mean business and then really drive it home by taking that traitor’s mink coat!

CAVEGIRL: Is this going to take long? Cavegirl hungry, could eat whole mammoth.

BRITANY: I know I have that problem, you know what the perfect solution is? I know this sounds weird, but one stick of celery, a cracker and some warm water. It will hold you over all day.

CAVEGIRL: (Pause.) That not good.

BRITANY: Beauty is pain and pain is dieting. Am I right?

CAVEGIRL: No.

BRITANY: But how can you expect to maintain an active lifestyle if you don’t eat healthy?!

CAVEGIRL: Cavegirl very active… Cavegirl tracked down family of sabertooth tigers for two weeks one time.

BRITANY: Yeah… Pfttt… who has the energy for that.

CAVEGIRL: Cavegirl got energy back from eating all of the tigers… except the one that bit cavegirl…

BRITANY: What?

CAVEGIRL: Death was too good for that tiger… so instead I spit on him and eat his family tigers in front of him and then throw him in volcano as peace offering.

BRITANY: A peace offering for who?

CAVEGIRL: The tiger…

BRITANY: Okay you’re starting to creep me out a little bit… are you sure you’re not part of some sort of undead cult.

CAVEGIRL: What is undead…

BRITANY: You know undead… like a zombie… like (She demonstrates, making a fool of herself.) Gaaaahhh! Brains!

CAVEGIRL: What was that?

BRITANY: You know… (She demonstrates again.) Gaaaaahhh! Brains! Brains!!!

CAVEGIRL: Cavegirl understood you the first time… she just thought it was funny you look stupid.

BRITANY: Yeah! Well you look like a giant pile of-

CAVEGIRL: Shhhh…. Quiet. Does Britany want to end up like tiger in volcano.

BRITANY: Yeah… like where are you going to find a volcano around here… we’d have to take a trip to Hawaii and you’re crazy if you think I’m spending 5 hours on a plane with someone who doesn’t understand the concept of deodorant… or toilet paper by the smell of it.

CAVEGIRL: GAHHHH!

BRITANY: Ahhhh! Please don’t hurt me! I take it all back we can go to Hawaii or Branston or some gross cave thingy in the middle of the jungle, just please don’t hurt me!

CAVEGIRL: Sorry… Cavegirl not angry… she just had flea bite, very bad this time of season.

BRITANY: Say… how did a bunch of fleas survive being frozen inside of a block of ice this whole time? And come to think of it… how did you survive being frozen inside of a block of ice this whole time?

CAVEGIRL: Does Cavegirl look smart enough to answer that question…

BRITANY: I… uh…. Well, that is to say… see I’m concerned that you’re going to hurt me no matter how I answer that question.

CAVEGIRL: Huh? Oh, It’s okay… Cavegirl forgot question… I was busy trying to remember how to start a fire… (She renacts, spitting on Britany.) Rock.. Rock… Pffft! (Mimics blowing on tinder.) Rock… rock… Pfttt!

BRITANY: Ahhhh!

CAVEGIRL: Rock… Rock… P-

BRITANY: Hey… uh… Cavegirl… I was just thinking maybe we could get back around to finishing your quiz… you know… it might help complete your… uhhh… transformation or whatever…

CAVEGIRL: Yes… Cavegirl will be like a beautiful butterfly

BRITANY: Sure whatever… well, final question, so you got this fabulous dress for the dance on Tuesday, but you took your parents car when you weren’t supposed to and they are totally cheesed off and say that you can’t go… what do you do?

CAVEGIRL: Hmmmm… you apologize to parents for being spoiled Cavegirl and bring home extra tiger meat for them to share on night of dance.

BRITANY: I never would have thought of that…. I mean home is where the heart is right? At least it is where my wardrobe is, which is basically the same thing and if my parents are cheesed off at you they are never going to buy you any new clothes, which means that you can never leave the house again anyway because… let’s face it who would want to be seen in clothes that they already wore before anyways?

CAVEGIRL: (Pause.) Right.

BRITANY: Wow, I feel like you really changed something in me… you know… I’m totally ready to go out and change the world. Like I’m going to go out and punch some people in the face if they disagree with me! I’m going to wear more make up than I ever have and my best designer shoes! I’m going to drop out of school, move in with some guy that I hardly know and spend all my parent’s money! Thanks Cave Girl! Look out world here comes Britany! I am woman hear me roar! (Exits.)

CAVEGIRL: Wow… that girl dumb. Cavegirl want to go find more ice to freeze self in. Cavegirl better off in cave.
```

---

## IC-0631: Declined

- Title: Declined
- Author (byline): Mike Noland
- Work: Declined
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2381
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
(MARY is sitting in an empty classroom studying, when suddenly OLIVE enters and drops her backpack on the floor.)

OLIVE I’m so sick of this. It happened again. Can you believe it?

MARY

(She is still studying and doesn’t even look up) MmmHmm.

OLIVE This is the fifth time that my card has been declined. I needed that smoothie. The problem is that they charge way too much. What are they putting in those things, gold dust? I mean, come on it’s basically just fruit and water and some kind of powder. Powder, really? How much could powder even cost? The whole thing is just a big racket. (pauses) Did you hear me?

MARY Yeah, powder, wow…

OLIVE You know I need my smoothie before classes start. How am I supposed to get thru the day without some protein, but come on, they’re so expensive.

MARY Yeah, expensive.

OLIVE You aren’t even listening to me. My best friend is ignoring me. Listen to me!

MARY Listening, I am…

OLIVE Fine, fine, I’ll just die right here and you won’t even notice. I hope my final death rattle isn’t too loud for you. When I die I want you to sprinkle my ashes at the smoothie place because they’re the ones that killed me. Wait, ashes… maybe that’s what the powder really is. Ooh, gross. I’m never having another smoothie from there again. (pauses) What are you doing? Why aren’t you listening to me? I’m spinning out and you’re supposed to calm me down. Why aren’t you calming me down?

MARY I’m a little busy here. I have a huge test that I should have studied for last night and I didn’t. Somebody started texting me at 9 and didn’t stop until 11:30. Then I had to clean my room up or my dad would kill me, so I’m sorry I don’t have time explain to you, yet again, why your card was declined. You can’t buy stuff if you don’t have any money! Now let me study.

(OLIVE sits silently for a few seconds.)

OLIVE I didn’t know it was 11:30, you should have said something.

MARY I did, I said, “It’s 11:30, I need to study”.

OLIVE But people say stuff like that all the time. I thought you just wanted to get off the phone.

MARY I did, that’s why I stopped responding, at 11:30.

OLIVE Oh, good. I just thought you were mad at me or something. That makes me feel better. Do you feel better, cause I do.

MARY Yeah, I feel great, now can I study?

OLIVE Sure, but just tell me one thing, why does my card keep getting declined?

MARY Are you serious? You don’t have any money in your account and you don’t have any money cause you spend your allowance in, like, two days and you don’t have a job. So that’s why your card is getting declined!

OLIVE I’ve had jobs, I’ve had lots of jobs.

MARY Exactly, you can’t keep a job long enough to make any money. You quit over stupid stuff.

OLIVE No I don’t. Name one reason I quit a job.

MARY You quit that job at the mall after one day.

OLIVE All I did was fold clothes the entire time, it was boring.

MARY It was a clothing store, what did you think you were going to be doing, creating designs for next years’ Paris show?

OLIVE Oh, that would be cool, why couldn’t I do something like that?

MARY Because you don’t know anything about fashion design and you’re still in high school, do I need to go on?

OLIVE Plus, I didn’t see any cute boys in there the whole day.

MARY Because it was a girl’s clothing store, why would boys go in there?

OLIVE To see me.

MARY You’re ridiculous. What about the church nursery? You only worked in there one Sunday, what was wrong with that?

OLIVE It’s nothing but babies plus…

MARY Let me guess, no boys.

OLIVE Exactly and they had a speaker on in there playing the sermon.

MARY Well, it is church.

OLIVE But if I wanted to hear the sermon, I would have sat in church.

MARY But you always go to sleep when you sit in church.

OLIVE I know, but I couldn’t sleep in the nursery because the babies kept crying. That was not the place for me.

MARY Your dad said he would pay you to help him.

OLIVE Hahaha, yeah right. That would last about two seconds and then we would be screaming at each other like maniacs. I can barely stand to be in the same house with him. There isn’t enough money in the world to make me work with that man. And he only said that because my mom was in the room. He doesn’t really want to work with me. He likes my little sister way better than me anyway.

MARY That’s not true… but your sister is much nicer to him than you are.

OLIVE My sister is such a fake. She only acts nice to make me look bad.

MARY Well, it’s working.

OLIVE You don’t know what my dad is like when nobody’s around. He’s totally different. When you’re there he is all nicey nicey but when you leave he turns into a real monster. I can’t do or say anything right.

MARY But I’ve seen you push his buttons too. Like when you wore that really short skirt to go to the movies the other night.

OLIVE It wasn’t that short, and besides I was just going out with you and Claire.

MARY But what did you think he was going to do when he saw you in that, applaud?

OLIVE Ok, ok, I might have done that just to make him mad, but he wouldn’t let me dye my hair.

MARY You wanted to dye it lime green with red polka dots. You would have looked like my aunts’ jello salad she makes every Christmas. It tastes really good but it would make a lousy hair style.

OLIVE It’s survival of the fittest. Kill or be killed. He’s not the boss of me.

MARY He really sort of is, right now anyway. Plus he gives you allowance every week.

OLIVE It’s not enough for a young, fashionable girl like me. I have to eat, buy clothes and pay for my own entertainment. The point is, I could never work for my dad.

MARY Fine, I get that but you need to work somewhere for more than a couple of days.

OLIVE I worked at the waterpark for almost 2 weeks this past summer.

MARY You called in sick after the first day and missed 3 days the next week. You also spent more on your swimsuits than you made working there.

OLIVE But when I was there, I looked good. It was just too hot and the sun was always shining and the kids were always screaming and there was water everywhere.

MARY Yeah, who would have thought all that would be happening at a water park? This leads me to my original conclusion, you have no money because you have no job. Yet you keep trying to spend it anyway. It’s obvious you haven’t quite gotten a grasp how your bank account works. When you want to buy something, there needs to be enough in there to cover it. Check your balance once in awhile.

OLIVE I can’t.

MARY Let me guess, you keep forgetting the passcode. It’s probably 1-2-3-4.

OLIVE I don’t have a passcode but that’s a good one. Is that yours? Can I use it too?

MARY No, that’s not mine. What do you mean, you don’t have a passcode. How do you check your balance without a passcode?

OLIVE I don’t have a passcode because my dad won’t let me have access to the account. He’s scared I could somehow see his stuff.

MARY His stuff? What does that mean? Is he laundering money for a drug cartel or something?

OLIVE Laundering, are you kidding? He can’t even get his dirty clothes into the hamper. Mom says he couldn’t find the washing machine with a GPS, a map and a seeing eye dog.

MARY Not that kind of laundering, oh, never mind. So you can’t see your account balance because your dad won’t give you access, right?

OLIVE Right.

MARY And your allowance is basically gone by the time you get it.

OLIVE Yep.

MARY And yet you still keep trying to use your card.

OLIVE What can I say, I’m an optimist.

MARY Then you have to get a job you like and keep it, it’s that simple.

OLIVE I knew you could help me.

MARY Help you? What do you mean? I’m not an employment agency, I can’t get you a job. I’m just trying to pass my history test, so I can get into college, get a degree and get a real job.

OLIVE Really, do you believe that or are you just going to college to get an M.R.S. degree? You know, marry some guy and then get the good house and raise the cute family.

MARY Look around, do you see anyone going to the malt shop or wearing bobby socks?

OLIVE Who’s Bobby?

MARY You know what I mean, this isn’t the 1950’s any more. I don’t have to get married to be happy and fulfilled or even have a family.

OLIVE You tell your parents that?

MARY What, are you crazy? I’m too young to die. I want to go to college, have fun, learn some stuff and get on with my life. I’m so sick of high school. I think I have had senioritis since the second nine week of freshman year. OLIVE But what about all the friends you’ve made? Won’t you miss them? What about me?

MARY I can barely stand most of the people here. I know they are only tolerating me for the most part. Sure, you’re my friend, but I’m just going to college. I’m not moving to Siberia. We can get together on weekends and you can come down to visit and spend the night. It will be great.

OLIVE That would be, but how am I going to do this without any money? You gotta help me get a job.

MARY Wow, you really brought that around full circle, didn’t you?

OLIVE I’m persistent, that’s a good quality for a worker isn’t it? Let’s make a list of my qualities and then figure out what kind of job I would be good for.

MARY I’m not going to get any studying done till I do this am I?

OLIVE Nope

(MARY takes out a blank sheet of paper from her notes.)

MARY First, you are an incredible pain in the butt.

OLIVE Not so sure that would look great on an application.

MARY Maybe not but it’s true.

OLIVE Be serious.

MARY I am serious, you can be incredibly annoying. However, if we rephrase it...How about… “is very persistent.”

OLIVE Persistent is good, what else?

MARY Spirited.

OLIVE Spirited, that sounds nice, what about... good with people?

MARY No, everybody puts that down.

OLIVE But I am good with people, I’m a people person. Everybody likes me.

MARY Not everybody.

OLIVE Wait, who doesn’t like me?

MARY You not my favorite person right now.

OLIVE You’re just grumpy because you’re sleep deprived.

MARY Yeah, because of you.

OLIVE No, it’s because you procrastinated till the night before and you used texting me as an excuse not to study.

MARY See this is why some people don’t like you, cause once in awhile, you’re right. Let’s finish this list. Alright...you’re considerate.

OLIVE Oh, that’s good. I really am. Like when that new boy came to school on crutches, I took his stuff to every class, helped him carry his tray in the lunchroom and offered to give him a ride to and from school.

MARY As nice as that was, I think his girlfriend might have gotten a little upset especially since he didn’t ask you to do any of that for him and you barely knew him.

OLIVE Was she really his girlfriend? I never heard anybody confirm that. Plus, he was really cute. I was not trying to flirt with him or anything.

MARY Of course not.

OLIVE I was just being, considerate. If he fell in love with me because of my kindness and beauty, that would just be a bonus.

MARY But he didn’t.

OLIVE His loss, back to the list. What are some other good things about me?

MARY Well you can be very determined, like a dog with a bone, when you set your mind to something.

OLIVE Hmm, not sure if that’s a compliment or not. You kinda called me a dog.

MARY No I didn’t...well maybe I did but not a bad way.

OLIVE I’m a dog in a good way, like good girl, sit, stay, don’t pee on the carpet.

MARY I just meant that when you want something, you will do whatever it takes to get it. That’s a good thing.

OLIVE Then I choose to take that as a compliment. Maybe that should be added to the list? My ability to put a positive spin on things. That has to be valuable to someone.

MARY Look, I only have a few more minutes to study, is there anyway we could speed this up?

OLIVE Maybe. You’re 18, right?

MARY You mean you can’t remember my birthday? It was 3 months ago and you were at my party. But how does my age help you get a job?

OLIVE You know all those words you were coming up with for the list? Since you’re 18, you can use them to fill out a reference for me on this job application. (Pulls an application out of her backpack and hands it to MARY.)

MARY What?! All this time you just wanted to use me as a reference for a job? Why didn’t you say that in the beginning?

OLIVE
I wasn’t sure you would do it.
MARY
So the whole “They declined my card” was just a line to get me to fill this
out?

OLIVE No, that’s true, I’m broke.

MARY Hand it here! Where will you be working ever so briefly this time?

OLIVE The yogurt place, that way I will be getting a discount!

MARY Well, that’s good, because they are expensive.

OLIVE I know, must be the powder.
```

---

## IC-0632: A Girl’s Guide to Science

- Title: A Girl’s Guide to Science
- Author (byline): Clyde Hendrickson
- Work: A Girl’s Guide to Science
- Publisher: Mushroom Cloud Press
- Publication date as stated: 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: KATIE
- Teaser before the introduction: No
- Spoken words (computed): 3972
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
A Girl’s Guide to Science

A Girl’s Guide to Science. CHELSEA is a slightly nerdy looking girl in 12th grade. She is wearing goggles. KATIE is in a tanktop and has no safety equipment. She is also in 12th grade.

(The play begins with a science safety demonstration already in progress. Katie and Chelsea stand in front of the class, with a lab bench in front of them that’s covered in various apparati. And yes, it is “apparati,” not “apparatuses.” )

KATIE. Ok, and here’s how to deal with a deep flesh wound without staining your jeans.
CHELSEA. Hey, that cut looks bad. Do you need medical attention?
KATIE. Not unless the doctor is really cute.
CHELSEA. This is a safety demonstration. I don’t think that attitude’s very safe.
KATIE. Oh, a cute doctor is always a safe bet in my book.
CHELSEA. Well, I’m going to stick with reading the lab manual. And it says to seek medical attention for
any cut that bleeds more than one minute.
KATIE. This brings me to another important lesson in the Girls Guide to Science: ignore downers with
their losing attitude, like this nerd. If you dream you can achieve, you’ll reach for the stars.
CHELSEA. (flipping through the book) What are you talking about? Where are you getting this from?
KATIE. Girl power!
CHELSEA. (pulling Katie aside) How did you get assigned to do the freshman science orientation,
anyway?
KATIE. I worked a little something out. If I do this, I don’t have to serve my 29 detentions that I got for
wearing revealing outfits.
CHELSEA. So you’re working off skank time.
KATIE. Uh huh.
CHELSEA. I take this seriously, so… just don’t do anything too stupid.
KATIE. (seems to agree) Fine.
CHELSEA. (begins again)Ok, now, if you’re going to do a combustion reaction, then you need a safety
bib, goggles, and a protective hood.
KATIE. And a fiery new lip gloss! Yowza.
CHELSEA. I thought we agreed on no stupidity. Besides, make-up is a tool of the oppressors.
KATIE. Geek.

A Girl’s Guide to Science

CHELSEA. What was that?
KATIE. (sing-song) Geek patrol.
CHELSEA. Pardon me while I try not to burst into flames.
KATIE. (shakes head) You will never have to worry about being too hot.
CHELSEA. Hey. I have a boyfriend.
KATIE. What’s his name? Chester?
CHELSEA. CyberStud82. He’s my… online boyfriend.
KATIE. (shocked by the lameness of this) Wow. If I was capable of feeling pity, you would be getting so
much right now.
CHELSEA. Thanks.
KATIE. But instead, you get the big Whatever, freak! (She does the hand signal to accompany this.) Now
ladies, let’s burn something. (She looks through her equipment.) Compressed hydrogen. Do not expose to
flame. Oh, this’ll be swell. (She begins to light it.) Now, remember, point the canister away from your
face when you’re lighting (She obviously points it towards Chelsea).
CHELSEA. For a forced participant, you’re pretty into this… hey, wait, what are you doing? Compressed
Hy- Oh my god (scrambles for goggles)
KATIE. Liftoff!
CHELSEA. Ow! That was my face!
KATIE. Don’t worry. Computer geeks don’t need faces anyway.
CHELSEA. That really stings.
KATIE. The truth hurts, babe.
CHELSEA. No, I mean my wound, on my face.
KATIE. I guess you should have been wearing your nerd bib.
CHELSEA. The lab bib doesn’t cover my face.
KATIE. I guess it should, then.
CHELSEA. I guess you should have not shot a giant column of flame at my eye!
KATIE. But I missed, didn’t I.
CHELSEA. Your ditziness isn’t just annoying anymore. You’re becoming one dangerous skank.
KATIE. You’re funny when you’re self-righteous. Do you smell that?
CHELSEA. Smell what?

A Girl’s Guide to Science

KATIE. Like burning hair.
CHELSEA. (pause) My hair is on fire, isn’t it.
KATIE. (completely unaffected) Uh huh.
CHELSEA. (sighs) I’ll go soak it in the toilet.
KATIE. You might say you’re learned to a crisp!
CHELSEA. I hate you.
KATIE. Remember girls, always wear your goggles! Get one with different colored bands, so they’ll
match your designer lab apron.
CHELSEA. (disgruntled growl) Ugh.

(While Chelsea is gone, Katie tries to set up an experiment herself, but ends up causing trouble.)
KATIE. Welcome back, brainy half!
CHELSEA. Shut it, syphilitic half.
KATIE. Rarrr.
CHELSEA. Don’t. I’m allowed to be disgruntled because I just had to stick my face into a toilet that had
several tasteful limericks on the wall about “the sound and the fury” of the stall’s previous patrons.
KATIE. The next stall over has some great nursery rhymes in it.
CHELSEA. I’d like it if we didn’t discuss the bathroom the bathroom. In fact, don’t say anything to me,
period. Me and my singed follicles are just not in the mood. For you or your charming ignorance.
KATIE. Yo, take a chill pill.
CHELSEA. The only pill I’ll be taking is my birth control… which is just for my complexion.
KATIE. Duh.
CHELSEA. I’m sure you’re not taking that particular medication.
KATIE. Right… because I’m not a ho.
CHELSEA. Yeah, ok. You’re a ho.
KATIE. That’s nice. I guess because I’m not Mrs. Wizard, I must be spreading my dumb little legs for
every jock that has his own car.
CHELSEA. Or if his dad has a cool car.
KATIE. Whatever. Just stop impregnating me with your mind.
CHELSEA. (pause) That is the strangest thing a person has ever said to me.

(They both pause, and look at the “audience” of freshmen.)

A Girl’s Guide to Science

KATIE. We should stay on track.
CHELSEA. Yes. Yes we should.
KATIE. (clears throat) Remember, never mix a low pH acid with a high pH base. I have a little saying to
remember it: if you’re fat with an f, then boys won’t like you, but if you’re flat with the pH, then you’re
phat with a ph!
CHELSEA. That just made my brain die.
KATIE. I know, isn’t it so deep?
CHELSEA. Deeply disturbing, yes.
KATIE. Mmmm, right. Let’s mix stuff.
CHELSEA. You can check your formulas with the periodic table.
KATIE. Mine’s laminated!
CHELSEA. My heart overflows with ecstasy at the thought of your plastic coated periodic table. Oh may I
touch it? Please? May I be blessed with the brilliance of your laminated warmth?
KATIE. Nope.
CHELSEA. I would have just torn it in half anyway.
KATIE. You can’t - that’s why it’s laminated. Ok, so the periodic table. It’s like a wardrobe, very
coordinated. This side of the periodic table is like the blues, the transition metals are your fall colors, and
non-metals and metalloids are your blacks and whites. Anyway, the periodic table is just like your closet at
home.
CHELSEA. If at home you happen to have a closet of death.
KATIE. That’s right! Imagine reaching for your favorite miniskirt and watching as it dissolves straight
through to your bones. How fashionable you’ll be in chemistry class when you know about your periods!
CHELSEA. I think you just jumped over to a health class lesson.
KATIE. Ewww gross. We’re talking about science here.
CHELSEA. I wonder… have you ever read a book?
KATIE. Like… the whole thing?
CHELSEA. Like, yeah.
KATIE. Does War & Peace count?
CHELSEA. …I suppose it does.
KATIE: It was either read that or go out with this totally disgusting guy Kevin. He had acne all down his
back and his hair was parted right in the middle of his head. We went to one concert, like Hoobastank or
something, and then he tried to feel me up in the mosh pit. I had to get rid of him somehow, so I just
pretended to read some Tolstoy… and I ended up actually reading it. What do you think of the Baron’s
motives in book two? Were they sincere? I’m not sure.

A Girl’s Guide to Science

CHELSEA. Actually… I haven’t read it. KATIE. Oh. It’s good! CHELSEA. Are you ready to try fractional distillation? KATIE. (sighs) Do I have a choice? (cell phone rings) Oh, I do! Excuse me. (she flips open the phone and answers it.) CHELSEA. Alright, you need a source of power, a source of water, KATIE. Oh my god he did not say that! They did what? I didn’t know you could do that with a pumpkin. CHELSEA. And a vacuum. Then, you adjust the boiler, KATIE. Of course I’ll be there tonight, I’ll be checking out of loserville any second now, CHELSEA. Acquire your acid from the teacher, and be very careful with it. KATIE. Yeah totally. I’m just, like, waiting for her to burn her face off or whatever so I have a chance to dash. CHELSEA. Hey KATIE. (to Chelsea) You heard me, Clarissa. (to phone) Yeah, an 80’s joke. You gotta give these dorks something to reference. So did you find a Twister board for tonight yet? Uh huh. What about the Jello? Ugh, I hate green. Whatever, we’ll deal. Just keep the pumpkins out of sight. CHELSEA. This requires total concentration. KATIE. This tramp is giving me so much bull. I gotta go. TTYL! (To Chelsea) What’s up? CHELSEA. Ok, now you have to hold the acid very steadily, and get ready to flip it into the solution… have the distillation apparatus set up precisely, and then… hey, can you give me a hand here? KATIE. No.

(There is an exchange of looks, and Katie finally accepts a beaker that Chelsea gives her)
CHELSEA. Just hold the beaker carefully, like this (she puts her hand on Katie’s)
KATIE. Please don’t touch me.
CHELSEA. Ok, uh, now, while watching the temperature and pressure, slowly manipulate the acid so that
it is directly above the boiling solvent.
KATIE. Girls, make sure you have at least one geeky hang-on who will do all this for you. It saves so
much trouble.
CHELSEA. (The experiment collapses) Ack!
KATIE. And gives you someone to blame.
CHELSEA. I’m covered in acid! Are you happy? This demonstration really sucks.

A Girl’s Guide to Science

KATIE. That’s not a winning attitude.
CHELSEA. You have the attitude of a mentally handicapped lemur!
KATIE. I’m just going to move along and forget your little tantrum.
CHELSEA. Yeah. I wish you would move along. But you won’t. (She grumbles a bit and waits for Katie
to keep going)
KATIE. Now, in most of these situations, its easier to just ask a guy for a help. They’re much better at
science anyway. Tests have proven it!
CHELSEA. What are you talking about? Don’t tell them that!
KATIE.
CHELSEA. Hold on. This is demeaning to women. You’ve gone too far.
KATIE. (In a suddenly intellectual tone) Please. Your feminist nay saying is so 1980’s. Isn’t it clear I’m
the postmodern rejection of all gender models, representing my disdain for all archetypes by replicating
them in a pastiche of kitsch and consumerism?
CHELSEA. (long pause) Skank, you did not just go there.
KATIE. Oh yeah, Nancy Reagan, I went there.
CHELSEA. That’s it! You’re about to get the business end of this pipette straight in your eye.
KATIE. Oh no you didn’t…
CHELSEA. Then I’m going to titrate your brain!
KATIE. Suck my big long beaker, baby.
CHELSEA. Make me.
KATIE. You… wait. We have to finish this demonstration.
CHELSEA. (trying to smile) Ok. Fine.
KATIE. Now. How bout you show the ladies how we prepare a solution of a metal in hydrochloric acid.
CHELSEA. I don’t think you want to give me any acid just yet.
KATIE. Well then, Mrs.Happypants, mix whatever concoction you’d like.
CHELSEA. Ok. This is how you safely put together a solution of Sodium Prostitutide. It’s my partner’s
favorite compound.
KATIE. Oh I have got to hear this.
CHELSEA. Take your beaker with distilled airhead.
KATIE. (grumbles under her breath)
CHELSEA. Let’s just mix a little skank in.

A Girl’s Guide to Science

KATIE. Look who’s labeling women now
CHELSEA. A dash of smartass…
KATIE. Careful, you don’t want to get the solution too hypocritical.
CHELSEA. If you don’t already have the appropriate spaghetti tops and frilly shirts, have your mom and
dad go buy you some at Target.
KATIE. Hey, I don’t have a dad. Are you trying to make me feel bad for that too?
CHELSEA. Wait -
KATIE. I mean, first you criticize my postcolonial work of feminist protest art, then you try and drag my
family down too?
CHELSEA. That’s not -
KATIE. My mom worked hard to raise me, it was hard on both of us.
CHELSEA. It doesn’t surprise me.
KATIE. Yeah, well.
CHELSEA. I mean, it doesn’t surprise me that your Mom was too much of a hussie to keep a man around!
KATIE. You troll! My Dad died in the line duty!
CHELSEA. Really…?
KATIE. Yes. It was terrible. A helicopter crash.
CHELSEA. Oh my god.
KATIE. Yeah, God… I don’t really do the whole God thing anymore either.
CHELSEA. So that’s why you got into science, huh? For your dad?
KATIE. That’s part of it. I mean, there are cute doctors too.
CHELSEA. I guess they are a nice bonus.
KATIE. Yeah. Hey, what’s your name? I’m Katie.
CHELSEA. My name is Chelsea.
KATIE. Really? Because I thought it was “Gullible” for believing all that crap about my dad.
CHELSEA. You skank! You evil, evil skank! (she snaps, lunges at Katie)
KATIE. Hold your horses! Get back, I am not getting in a cat fight in front of 84 freshmen girls!
CHELSEA. I don’t want to fight.
KATIE. What else could you be doing?

A Girl’s Guide to Science

CHELSEA. I was going to put you on the scale. You know, I was gonna find out how much your ass
weighed.
KATIE. Why’d you wanna know?
CHELSEA. So I could see how much force it’d take to kick it.
KATIE. I’m sorry, ok? Can you back off, please?
CHELSEA. You don’t get to boss me around. Just because you took Pete Peterson to the junior prom when
he said he’d go with me first because he was the cool hot nerd and I was the queen of the nerds so of course
I should go with him and then we’d make sweet love in the back of his Honda Prelude with the weezer
sticker and our babies would grow up and go to harvard, yale, and maybe amherst if they were artsy
drifters. But no. He had to be the nerd who got the hot girl. And while you were making Pete feel like the
king of all dorkdom, do you know who I went to prom with?
KATIE. No…
CHELSEA. I went with a 10th grader from the chess team! He wore shorts to the dance.
KATIE. Dress shorts?
CHELSEA. No. Cut offs.
KATIE. I’m sorry. But, uh, I didn’t go there until this year. I’ve never met Pete.
CHELSEA. You might as well have. How is Pete these days. Does he still have the Prelude.
KATIE. I guess…
CHELSEA. How would you know! You meant nothing to him. Oh Pete, I’d do anything to be nuzzling in
the hairy jungle of your chest again, your apelike arms squeezing me so tightly.
KATIE. Did you watch a lot of nature videos as a child?
CHELSEA. (sighing out of love) I once gave an informational talk at the zoo about orangutans. I showed
it to Pete… he loved it. I think he identified with the monkeys.
KATIE. Well, most men do.
CHELSEA. They’re pigs! That’s why the girls have to take over science so we can rule the earth.
KATIE. I like your style. Maybe we can be friends.
CHELSEA. Really? I usually don’t make friends outside of the astronomy club.
KATIE. Sure… there’s just one thing I need you to do…
CHELSEA. What’s that?
KATIE. (suddenly throwing flask at Chelsea) Eat this, you psycho!!
CHELSEA. Ow! Owwwww! (Pauses) Ooh. Oooooh. (She starts licking her hands.) This is kinda good.
Kinda real good.

A Girl’s Guide to Science

KATIE. What the – (she reads the flask) N,3-dimethyl-nitro-1,3,5-cyclohexene. Huh.

(Chelsea starts gnawing on arm.)
KATIE. (Realizes she has to read the other side, does so.) Methamphetamine. Uh oh.
CHELSEA. (offering gnawed arm) You have got to try some.
KATIE. No thanks… too many carbs.
CHELSEA. Did you know you were so shiny?
KATIE. What?
CHELSEA. You’re like… a laminated me.
KATIE. Well, I do use conditioner.
CHELSEA. Ooohhhh… I feel so.. sensual.
KATIE. Great.
CHELSEA. Who wants a body massage?
KATIE. What did you just say?
CHELSEA. Body massage!
KATIE. I don’t know… that would be nice…
CHELSEA. (Preparing bib, utensils) Just lay down right here.
KATIE. Wait a minute…. are you gonna eat me?
CHELSEA. No, no, no at all.
KATIE. Then why did you just get out all that sodium?
CHELSEA. (pauses) Body massage!
KATIE. Maybe this is a bad idea. (She gets up.)
CHELSEA. (holds her) No… I’ve gotta eat you before this wears off.
KATIE. Still hallucinating, eh?
CHELSEA. Sure.
KATIE. Then don’t do it! You’ll regret it, I’m very fatty.(She sneaks out of Chelsea’s grip.)
CHELSEA. We both know that’s crap. Time to dine on school’s most popular dish.
KATIE: Thinks of the carbs! The carbs! (She is about to be eaten when Chelsea suddenly reacts to
something.)

A Girl’s Guide to Science

CHELSEA. (completely freaking out) Ahhhhh! Get them off of me! Oh jesus, they’re everywhere, get
them off!
KATIE. What, what?
CHELSEA. The badgers! The evil badgers! (tearing at her clothes) how did they get into the back of my
shirt?!
KATIE. I don’t know? What should I do!
CHELSEA. I figured it out! They’re coming out of my nose! That’s where their secret lair is, in my skull!

(She begins to try prying the badgers out of her nose, eyes, etc.)
KATIE. Wow. Just, uh, just shake your head real hard and maybe they’ll fly out.
CHELSEA. Ok! (She does this) Whoa! Look how many of them there are!
KATIE. Yeah, uh, that’s a lot of badgers.
CHELSEA. I think I got them all… NO WAIT! (She tears at her leg for a few moments, then stops) Oh,
that’s not a badger. That’s my leg.
KATIE. Well. You should be coming down now. Try and stay calm. Maybe I can get you some water, or
like, whatever you give to total freaks when they go psycho.
CHELSEA. Oooooooh, you know what would be nice. Some figs. Some big old figs.
KATIE. You really think that figs are what you need?
CHELSEA. Baby, I need figs. I need them.
KATIE. Let me see what I can do.

(Katie leaves. Chelsea sees something and starts clawing at the air.)
KATIE. (returning) I actually found this, like, Ziploc with some old fig newtons under the air conditioner,
I guess - what are you doing?
CHELSEA. Trying to rip a hole in space and time.
KATIE. Why?
CHELSEA. I think I’m supposed to be a roman goddess. Ow! That axe was pointy. Stupid Middle Ages.
Ooh, there’s Charlemagne. Hey Chaz!
KATIE. (Leaning over to look) Did you really…?
CHELSEA. (Grabs Chelsea’s head) Gotcha! Noogies!
KATIE. You fiendish slut! (They struggle, and knock over a large container)
CHELSEA. Oh no! The ether!
KATIE. (sniffing) Hmmmm… I think I might go to sleep now…

A Girl’s Guide to Science

CHELSEA. No, you can’t… uh, crap, what to do in this situation… crappity-crap-carp. Uh, Caffeine!
Drink this cold pot of coffee.
KATIE. Dude, like whatever. (she drinks it.) Whoa. Totally un-mellow. (she starts to shake.)
CHELSEA. Too much! Uh… have some codine!
KATIE. Where do all these drugs come from.
CHELSEA. The school district’s out of money, so they sold the chemistry department to Walmart. They
give us all their extra stuff.
KATIE. Your eyes look kind of bloodshot.
CHELSEA. I actually can’t feel my arms or legs.
KATIE. Maybe you should have some codine too.
CHELSEA. Yeah, and some caffeine! (She takes both.)

(Both girls are feeling the effects of the drugs) KATIE. I feel like a hamster in the dishwasher. CHELSEA. I know how you feel. Just how you feel. KATIE. …Yeah? CHELSEA. I just keep thinking about all the things that are different between us, and I feel like they shouldn’t be different, like we can make them the same if we just work hard and do it, you know. We can just do it! See, like take my hand, and your hand, and put them together, and its like we’re one person. Do you feel it? Our oneness? KATIE. Sure! CHELSEA. Oh! Oh you do, Katie, I’m happy! Maybe we can be friends on this special day of oneness. KATIE. Uh.. CHELSEA. And I think it all comes from when I didn’t really have a good male role model growing up, that I thought I was very female, and everything was female, so I’ve always just tried to, you know, be a good female, as opposed to a bad male, and I’ve never wanted to be a good person. But now I want to be a good person. (she is nervously moving something back and forth, flicking a pen, doing many sorts of random little events.) KATIE. Good, good. I’m glad for your… goodness. CHELSEA. Now, if I could just get this pen to click in time to this other pen. (She tries to click them together, but her shakiness and jumpiness make this very difficult.) ACK! Caffeine headache… must find more…

(Chelsea reaches up and drinks some random bottle) KATIE. No, wait! Ah, screw it. (She drinks it as well, and becomes quite delusional) You. CHELSEA. Me?

A Girl’s Guide to Science

KATIE. You’re the one.
CHELSEA. The one?
KATIE. The one who put my hamster in the dishwasher.
CHELSEA. I don’t think that actually happened.
KATIE. Whatever. I’ll slap you silly with this trout. (from here on, all fish are imagined, although the
fighting is real.)
CHELSEA. Hey! You stole that trout from my collection.
KATIE. Yes, that’s right, I’m wailing on you with your own trout. Feel the pain!
CHELSEA. It burns! It burns with the power of fish! How far I've fallen…. except, I fight back with a red
snapper! Weren't expecting that, were you? Your face is looking a bit... red, Katie!
KATIE. As you slip on a barracuda that I've slyly placed underneath your feet.
CHELSEA. Crafty. But what you don't know is that I replaced all your barracuda with pseudo traction-
enhanced barracudas…or tracto-barrapseudas, for short.
KATIE. Damn you! Foiled again. But this bass behind my back will knock you to the ground.
CHELSEA. I'll see your bass and raise you a flying octopus - flying at your face, that is!
KATIE. Octopi are no match for me - I'm too little and quick for them to stop me.
KATIE. Plus, I have this electric eel that I use as a stun gun.
CHELSEA. Ha-ha, you forget - I'm already quite stunning!
KATIE. Touché, my friend
CHELSEA. ...eh, I forgive you. And I’m out of fish.
KATIE. Hey, wait. You just said you were stunning. That is not the Chelsea I knew five minute ago.
CHELSEA. Wow… it’s strange, this “self-confidence.”
KATIE. Feels good, doesn’t it?
CHELSEA. Yeah.
KATIE. Think it could perhaps stop you from going psycho the next time you see a “popular” girl like me?
CHELSEA. (doubtfully) I’ve been trying to prove that women are just as good as men at science…
everything I’ve done, to get ahead… it’s all neutralized by you. Titrated by your airheaded ways. No…
it’s gone. I feel so pathetically inadequate… part of the system. Up and down again. The stupid
equilibrium of the fair and unfair. (She weeps dramatically)
KATIE. Hmm. Maybe, uh. Hmm. Tissue?
CHELSEA. No, no, in the state I’m in, I’ll probably think its attacking my face or something.

A Girl’s Guide to Science

KATIE. Yeah. Do you think… nevermind.
CHELSEA. What.
KATIE. Do you really think I’m that bad?
CHELSEA. …Yeah.
KATIE. Come on, there are guys like me.
CHELSEA. Well, I guess.
KATIE. I think that’s your problem.
CHELSEA. Stupid guys? No, they don’t even speak to me.
KATIE. No, no. There’s no difference between girls and boys –
CHELSEA. Uh…
KATIE. The difference is only between smart and dumb people!
CHELSEA. What?
KATIE. Think about it… who do you get less – me, or the guy on the chess team?
CHELSEA. Well… I did once skip a funeral so I could practice for the Mathlete Olympics.
KATIE. There you go. You’re more nerd than girls.
CHELSEA. Hah. Is that an insult?
KATIE. No, just a fact. This silliness of boys and girls is just made up. People are just people…
CHELSEA. Smart or dumb people.
KATIE. Yeah, or fat or short or whatever.
CHELSEA. You shouldn’t make fun of fat people either.
KATIE. Hey, but neither of us is fat. We have that.
CHELSEA. Well… true. (She sighs.) One stereotype at a time, I guess.
KATIE. Sure.
CHELSEA. I guess if I worried more about being me, and less about being a girl…
KATIE. You might find yourself enjoying being both.
CHELSEA. You must be really high.
KATIE. Why?
CHELSEA. You’re actually acting intelligent.

A Girl’s Guide to Science

KATIE. I dunno. I kinda have this urge to scratch my ear really hard and bite my tail.
CHELSEA. I admit, I’ve been paying a lot of attention to your growing coat of fur.
KATIE. Then I am becoming a cool, glowing, rainbow colored dog!
CHELSEA. Well… Unless the meth, ex, and caffeine in my system is lying – yes, yes you are. But can I
be a doggie too?
KATIE. Sure! (While petting Chelsea) Nice doggie. Oooh, your hair is so crispy from when mommy
burned you. Yes it is. You’re a crispy little hot dog. My little wiener dog.
CHELSEA. (Barks enthusiastically)
KATIE. My cutie-patootie wagamuffin. Give your mummy some kisses.

(Katie makes kissy noises. Chelsea begins to lick her face enthusiastically, like a puppy would)
KATIE. I love you Nancy Reagan.
CHELSEA. I love you laminated girl!
KATIE. Mwah mwah mwah. Mwah mwah… (suddenly wakes up and stares. Chelsea stops and stares as
well. There is silence for a long while.)
CHELSEA. (reaching for Katie’s face) Let me get that…
KATIE. (slaps her hand away) Get what. I’m fine. There’s nothing there. Nothing happened.
CHELSEA. Right.
KATIE. Right.

(Go back into science demonsration routine)
CHELSEA. Science is fun!
KATIE. Remember girls, just keep your head in the game, and you can really lick this subject! Oh god.
CHELSEA. And whatever field of science you might choose, you can’t lose… unless the badgers get you.

FIN.
```

---

## IC-0633: Good Morning, Glory! Text copyright 2005 Ryan N. Ray

- Title: Good Morning, Glory! Text copyright 2005 Ryan N. Ray
- Author (byline): Not specified
- Work: Good Morning, Glory! Text copyright 2005 Ryan N. Ray
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1493
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
2 Females (Humorous) Juanita, a narcoleptic Spanish housemaid Glory, a rich and lazy woman

Good Morning, Glory!

Juanita: (enters bedroom) Hello? Hello?

(Aside) Aye,aye,aye....these Americans! Always sleeping...ah, they are
so lazy! I work, they sleep....I work, they eat...I work, they
sleep some more...I work, they poooooooo....
(To Her) ooohh, good morning Senora Glory! Shall I get your usual ready for
you? (Aside) You filthy cow!

Glory: Good morning, Juanita...and a pop tart with some ginger
ale doesn’t constitute as my ‘usual’ just because I get it every
morning. (Aside) My usual would be a gin and tonic with a
spritz of lemon...but since it’s 7am I’ll go with the pop tart and the ginger
ale. (To Her) Sure, Juanita...I’ll have my usual.

Juanita: I’m sorry Senora, what were you saying? (Aside) I was
too busy drowning in the sorrow of your life to hear you. You
have it so hard, you know? I mean, look at how good I got it? I
get to take care of you for $5 an hour...which includes but is not
limited to washing your sheets, cooking your food, and
answering your phone...you lazy pig! (To Her) Oh, the
usual...coming right up!

Glory: Thank you, Juanita. (Aside) It’s good to know that this country is still producing fine, upstanding green-carded citizens like yourself.

Glory: Oh, Juanita...did James call?

Juanita: James? No Senora, no James...

(Aside) It must be one of her man-whores...

Glory: Oh well...I guess I’ll talk to him later.

Juanita: (Aside) I knew it! A man-whore!

Glory: James is one of my well-established clients. We play tennis on Tuesdays…

(Aside) not to mention he’s one of my...ahem...friendlier partners!

Juanita: Shall I check the machine for you? Maybe he did call
and I just missed it... (Aside) you know, when I was doing one
of your demeaning assignments...like bathing your bichon frisse
or cleaning your toilet...with your toothbrush! HAHAHAHA!

Glory: No Juanita, that’s quite all right... (Aside) I doubt the controls are espanol friendly, anyway...

Juanita: Ok...but if you change your mind you let me know!

Glory: Oh, don’t you worry about that (Aside) I’m not paying
you $5 an hour to sit on your lazy bottom...come to think of it,
$5 an hour is way too much for what you do. My gardener does
more than that and he doesn’t even get paid! Well unless you
count the...

Juanita: Senora Glory! Your face! What happened? It’s all blue and splotchy... (Aside) She’s so gullible...I could tell her that a gnome was on her head and she’d believe it!

Glory: What? Is something wrong with my face? Oh no! Not my perfect face! I need my mirror!

Juanita: It’s in the bathroom, Senora! (Aside) You know, the place I clean every single night once you are done puking your guts out! You could never pay me enough for that job!

Glory: Juanita? There’s nothing wrong with my face...were you just messing with me?

Juanita: No, Senora Glory...honest! I guess it was just the way
the light was hitting your face... (Aside) Ha! I could be a
champion at poker...I’m such a good liar! Ha!
(Juanita falls asleep)

Glory: Juanita? Come here and show me where you saw the splotches. Juanita? (Aside) Oh where is that stupid housemaid when you need her?!? (To her) Juanita!

(Sees Juanita has abruptly fallen asleep)

Glory: (Aside) Ahaaaah. What a perfect opportunity...(To her)
Juanita...wake up. Wake uuuuuuuuuuuuuppppp. I’m going to
double your salary...I’ll get you take out from the “House of
Tortilla’s.”.....hmmm....I’ve got it! OhmygodJuanitaimmigration
is here!!!

Juanita: (startled) Immigration?!?!?! Where? Hide me, hide me! (says many random phrases in Spanish)

Glory! HAHAHAHAHAHAHAHAHAHAHAHA!

Juanita: What’s so funny? Where’s immigration! You’ve got to hide me!!!

Glory: Hahaha...Immigration’s not coming, Juanita...I was just kidding. You had fallen asleep again...(wipes tears from face)

Juanita: Oh...I get it. Let’s poke fun at the Spanish
housemaid...what is it? Cinco de Mayo? You think it’s funny to
make fun of me because of my heritage? (continues
on...never stops)

Glory: (Aside) Oh great...here we go...a story from Mexico. Those never get tiring...especially when they’re half in Spanish.

Juanita: I’ll have you know that my great grandfather Julio Rico
Estephan Bandido Francisco Luis Ricardo Enrique Montoban
Pollo Bandido Sanchez came all the way from Mexico City to
America by way of donkey...and he never did something as
shameful as what you just did...I’m quitting!

Glory: What? You can’t quit! (Aside) Who else would let me patronize them in such sarcastic and cynical ways? No one!

Juanita: Why? Why can’t I? All I am is some silly Mexican
housemaid to you...you don’t appreciate me, you don’t ever say
‘thank you, Juanita,” and you only pay me because you have
to!

Glory: Juanita...that’s not true! (Aside) Technically if you aren’t a legal US citizen I don’t have to pay you...but who cares about semantics?

Juanita: There is absolutely nothing that you could say that
would convince me to stay! Nothing! I am a rock...I am
immovable. Think of me as a fortress in which nothing could
penetrate! I am like a tree with my roots planted firmly...deep
into the earth’s core! I am that spot that no matter how many
times you clean me...I won’t go away! I am going and there is
nothing you can say, do, or bribe me with that would keep me
from leaving! Nothing! No BRIBE will stop me. Not even a
RAISE would make me stay!

Glory: Juanita...what if...let’s say...hypothetically...

Juanita: Senora Glory, you know I don’t speak French...

Glory: Ummm...that’s not French, but whatever...anyway...let’s say...for example...that I were to increase your...wages, perchance, by a quarter an hour?

Juanita: No, no way Jose, never! I could never be bought! Your bribes mean nothing to me! Not even 50 cents extra per hour would make me stay...you efforts are wasted on me!

Glory: Okay, 50 cents extra an hour...

Juanita: I am like stone...I am immovable...

Glory: 75 cents...

Juanita: Suddenly I feel my stone rolling...like a pebble falling down a hill...

Glory: ALL RIGHT! You win, $1 an hour extra! But not a penny more! Are you happy? Come on...tell me you’ll stay! I must know!

Juanita: You know you drive a hard bargain Senora Glory...so I guess I’ll stay. $6 is closer to minimum wage...and that’s all right with me.(Aside)For now, you weak-willed jellyfish!!! Haha!

Glory: Thank you, Juanita...you have no idea how much it means to me that you are staying (Aside) Considering I would have went as high as $10 an hour...you narcoleptic buffoon!

Juanita: I’ll go get your pop-tart…

Glory: Juanita…make sure it’s the frosted kind. I don’t like it if it’s not frosted…

Juanita: Of course, Senora Glory. (Aside) Like a bee to it’s honey…I will fetch you a pop tart and your ginger ale! Well, more like an Hispanic bee…but a bee nonetheless! (turns to go)

Glory: (Aside) If it’s not frosted…so help me you’ll be back on the boat to Mexico so fast your Sombrero will spin!

Juanita: Here you go, Senora Glory! Your frosted pop tart and
your ginger ale. (Aside) Make sure to eat it all…the odds for
choking increase with the amount of food you eat! And I
sincerely hope you enjoy the secret ingredient…

Glory: Thank you. (eats) Mmmm…these pop tarts are sooo
sinful. They taste exquisite! It’s amazing how wonderfully
delightful they truly are! (Aside) That’s funny…my stomach
just turned…but how can that be? Pop Tarts have never done
this to me before…

Juanita: Is something wrong, Senora Glory?

Glory: No, no…everything’s fine… (gets stomach cramp). Actually, I think I have to go to the bathroom…

Juanita: Ha! That’s what you get for firing me, you silly woman!

Glory: But Glory, I hired you back with a raise, remember?

Juanita: You know us Mexicans…how sneaky we can be! We won the Alamo, remember? Remember? HAHAHAHAHAHA!

Glory: What are you talking about Juanita? What did you do to the pop-tart?

Juanita: I laced it with juice from one of the hottest peppers in the world! It can melt the lining off a cow’s stomach! Have fun!

Glory: But Juanita, why? Where are you going?

Juanita: I cannot take it anymore…$6 is no way to make a living.

Glory: But where will you go for work?

Juanita: To the most successful, esteemed, honorable, and dignified place I could possibly work…

Glory: And where is that?

Juanita: Taco King…ever since they dropped the Chihuahua as their mascot they’ve been looking for someone to fill those shoes!

Glory: You’re going to be the mascot for Taco King!?!?!?!

Juanita: Yes…and it will be glorious! $6.50 an hour and all the chalupas I can eat! Adios, Senora Glory!

Glory: But Senora Glory…oh darnit! Where’s my phone…ah!

(picks up phone…dials operator) Operator…get me Mexico City, Mexico please…I need a new housemaid!!! Oh, and after that…could you kindly connect me to immigration?

End
```

---

## IC-0634: How Much I Love You

- Title: How Much I Love You
- Author (byline): K.R. Schneider
- Work: How Much I Love You
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: LUCY, CHARLOTTE, BRAD, CHARLOTTE & LUCY
- Teaser before the introduction: No
- Spoken words (computed): 1885
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
(PRESENT; best friends Charlotte and Lucy are sitting together; Charlotte is sitting up in a bed; Lucy sits next to her)

LUCY: So...what do you want to do?

CHARLOTTE: I don't know. This is kind of a slumber party, right? What do girls do at a slumber party?

LUCY: I have literally no idea.

CHARLOTTE: Gosh, I haven’t been to a slumber party since I was like eight.

LUCY: You’ve been to one. I was so uncool when we were eight that people’s moms wanted me to stay home.

CHARLOTTE: You did listen to a lot of NPR.

LUCY: Okay, radio is fascinating! It’s an art form, Char. Don’t look at me like that; it is a seriously underappreciated art form, and I personally think that if more people --

CHARLOTTE: (cuts her off) Lucy. Too much. Too far. This is one of those times I mentioned.

LUCY: National Public Radio is interesting!

CHARLOTTE: Yes. I’m sure a lot of 800 year old men would agree with you.

LUCY: Okay, that’s rude.

CHARLOTTE: The truth hurts, babe. Tell me something exciting; I’m living vicariously here.

LUCY: Something exciting about my life? Grasping at straws there, Char.

CHARLOTTE: Come on - anything! Find me a straw!

LUCY: (considers; hesitates)….I went on a date last week.

CHARLOTTE: (excited) Oooohhh!

LUCY: (deadpan) He’s a part-time civil war reenactor.

CHARLOTTE: (confused) Oohhh?

LUCY: (clearly embarrassed) Got a beard. Like a long one. They asked him to remove his gun before we entered the Chilli’s.

CHARLOTTE: He took you to Chilli’s?

LUCY: He had a gun, Charlotte! Focus. Gun. Civil war era gun. Wore the gun. On the date.

CHARLOTTE: The date where he took you to Chilli’s.

LUCY: Charlotte, he is a civil war reenactor. He wore his civil war musket on our date! There are clearly bigger issues here!

CHARLOTTE: But I just think Chilli’s is so tacky, ya know?

LUCY: Charlotte!

CHARLOTTE: Yes, okay. Bad. But I mean...probably not the worst date you’ve ever been on. Remember that guy in college? With the...hike, and the uh...shoulder?

LUCY: Oh, Brad. Yeah. THAT was a doozy.

FLASHBACK (Lucy and Brad are hiking).

LUCY: (out of breath) Uh...Brad, could we maybe...slow down? Bra- Brad?

BRAD: (clearly annoyed) Oh. Uh, yeah. You seem a little...tired.

LUCY: No, yeah. I’m good - it’s just that I...I sprained my ankle a couple miles back, and I think it’s...is it possible for that to bleed? Something is definitely bleeding.

BRAD: Right, yeah. I dunno. So...you’re not really the hiking type then, huh?

LUCY: Well...I thought I did okay up until, you know...well the jump over the stream was a little steep. (notices elbow) Oh. Yep, there’s the blood.

BRAD: (pointing at her arm) Yeah. That’s not hangin’ right.

LUCY: I’m sorry?

BRAD: Looks like that shoulder’s dislocated.

LUCY: Oh dear!

BRAD: (cracking knuckles) I can probably pop her back in for ‘ya if you want. (tries to grab her shoulder)

LUCY: Or! Or you know...we could...see a doctor.

BRAD: I mean we’re kind of on a time crunch.

LUCY: Sure, yes. And if it was just the shoulder, but my ankle and...wait, why the time crunch?

BRAD: 50 cent wings start at five. I told you this. We gotta meet the guys. At five.

LUCY: Right, wings, yeah...but...I think a doctor is a good idea.

BRAD: Yeah, I guess I could call ‘ya an ambulance.

LUCY: Can’t you just drive me?

BRAD: Lucy, I got Wing Wednesdays!

PRESENT

LUCY: Yeah, that was a bad one.

CHARLOTTE: Definitely not a contender.

LUCY: Senior prom with Bobby Pickett was probably my best date.

CHARLOTTE: Right! He got you the yellow flowers. I went with Mike Hart that year.

LUCY: Yeah, you stole him from Gretchen Judge.

CHARLOTTE: She ripped out my hair extensions. I still have the scar.

LUCY: Your mom was so mad about those hair extensions.

CHARLOTTE: Not as mad as YOUR mom was when we tried to sell Marcus.

LUCY: I don’t know why: nobody would have paid money for Marcus.

CHARLOTTE: Probably because she’s a mom; worrying is in the job description.

LUCY: You’re a mom. You like being a mom right?

CHARLOTTE: Being a mom is cool.

LUCY: You remember how you felt about it before you were one?

CHARLOTTE: I freaked out a little.

LUCY: A little?

FLASHBACK

(rapid knocking; Lucy answers the door, very obviously was sleeping; Charlotte barges in, very pregnant)

CHARLOTTE: I changed my mind.

LUCY: Charlotte? It’s three in the morning. What are you doing here?

CHARLOTTE: I changed my mind!

LUCY: Where is Luke?

CHARLOTTE: Sleeping pleasantly because he doesn’t have a bowling ball attached to his front!

LUCY: Okay. And you’re here because?

CHARLOTTE: I changed my mind, Luce!

LUCY: About?

CHARLOTTE: I can’t do this! This mom thing. I changed my mind. It’s not happening.

LUCY: No, I’m pretty sure it’s happening.

CHARLOTTE: I can’t be someone’s mother! I can’t even throw out that crop top from the 10th grade! My favorite movie is Space Jam! I bump a lot of Nelly. A lot. You can’t bump Nelly in a minivan, Lucy! I don’t want a minivan!

LUCY: Your favorite movie is Space Jam? Really?

CHARLOTTE: Lucy, not the point!

LUCY: Kind of the point.

CHARLOTTE: Luce!

LUCY: Charlotte. It’s going to be fine. You want children!

CHARLOTTE: I can’t want children; I am children!

LUCY: Char.

CHARLOTTE: Moms are always sharing their ice cream; I don’t want to do that! And saying that their kid is in the whatevereth percentile for...I don’t even know, what do they do that for?!

LUCY: Growth, I think?

CHARLOTTE: I don’t want to start speaking in weeks! “Oh hey, that kid is cute, how old is he? He’s eighty-four and a half weeks.” I don’t want to do that!

LUCY: I don’t think that’s a requirement.

CHARLOTTE: What if I don’t have a cute baby! What if my baby is ugly and I just have to love it anyway!

LUCY: Well, you and Luke are both attractive people, so I really think it’ll probably be fine…

CHARLOTTE: Probably?! Lucy! I can’t do this. I can’t be a mom.

LUCY: Charlotte. Breathe, okay? Focus. You want to be a mom. You love the idea of being a mom; you’ve wanted to be a mom since you were like nine. If anyone is read to be a mom--

CHARLOTTE: (surprised, but calmly cuts her off) Lucy. My water broke.

LUCY: You brought a water? Wait like your water water? Now!? It broke now? In my kitchen!? I just mopped!

CHARLOTTE: That’s really your first priority right now?

LUCY: What SHOULD be my priority?

CHARLOTTE: Uh. Luke? Cab?

LUCY: Luke drives a cab?!

CHARLOTTE: No, call one!

(back of the cab; Charlotte is having contractions and freaking out again; Lucy tries to help her with her breathing)

LUCY: Heee. Hooo.

CHARLOTTE: Can we go any faster?!

LUCY: In and out, Char. You got it.

CHARLOTTE: (squeezing Lucy’s fingers) Why does giving birth have to feel like squatting on dynamite?!

LUCY: You can do this, Charlotte. It’s going to be fine.

CHARLOTTE: (mid-contraction) You really...think it’s...going to be fine?

LUCY: I really do. Besides. When you’ve got a baby, you can finally sing that lullabye to somebody other than me at sleepaway camp.

FLASHBACK (Lucy is on the top bunk at camp (can’t sleep) Charlotte is on the bottom).

LUCY: Charlotte? You awake?

CHARLOTTE: No.

LUCY: Char.

CHARLOTTE: What’s wrong?

LUCY: Do you think there’s really a sea monster in the lake?

CHARLOTTE: I think it would be a lake monster because it’s a lake.

LUCY: So you think there is one?

CHARLOTTE: Luce. I think you ate too many s’mores on that treated wood. Go to sleep.

LUCY: But if there is a monster, you think it’ll stay in the lake?

CHARLOTTE: Do you want to sleep in my bunk?

LUCY: I don’t want to be a baby.

CHARLOTTE: Oh just get down here!

LUCY: You sure?

CHARLOTTE: Now, please. So we can go to sleep. (Lucy climbs in with Charlotte) Still scared?

LUCY: Sorta.

CHARLOTTE: Okay. (clears throat)

LUCY: What are you doing?

CHARLOTTE: I’m gonna’ sing to you, so just shut up, okay? You are my sunshine--

BACK TO BABY FLASHBACK

CHARLOTTE: I can’t believe you remember that.

LUCY: I was scared. It helped. Maybe it’ll help now.

CHARLOTTE: Now? You want to sing now?

LUCY: Yeah, come on. (starts the song; Charlotte complies, but clearly doesn’t want to) You are my…

CHARLOTTE: (in pain/annoyed) sunshine

LUCY: (encouraging) my only…

CHARLOTTE: (mid-contraction) sunshine

PRESENT

CHARLOTTE: You know my dad used to sing that song to me?

LUCY: I remember.

CHARLOTTE: My dad was the coolest.

LUCY: He was the best.

CHARLOTTE: Luke’s a pretty solid second, though.

LUCY: Yeah, you landed a good one.

CHARLOTTE: He’s not a plane, Luce.

LUCY: Whatever. He's great.

CHARLOTTE: He is pretty great.

LUCY: You've always been great at stuff.

CHARLOTTE: I don't think there was much skill involved in marrying Luke. It was just right.

LUCY: Still.

CHARLOTTE: You're great at things.

LUCY: Like what?

CHARLOTTE: I mean you owned that Backstreet Boys song at the 7th grade talent show.

LUCY: You did my choreography the night before.

CHARLOTTE: Yeah, I also pierced your ears that night, remember?

LUCY: I can't forget. They're still crooked!

FLASHBACK (Charlotte stands behind Lucy, needle in hand, ready to pierce her ears).

CHARLOTTE: Okay ready?

LUCY: No!

CHARLOTTE: It's not even going to hurt.

LUCY: You're putting holes in my head!

CHARLOTTE: In your ears! I'm not shooting you!

LUCY: You really think this is going to work?

CHARLOTTE: Yeah, totally.

LUCY: And you’ve done this before? Right?

CHARLOTTE: Um...yeah…

LUCY: Charlotte!

CHARLOTTE: Well, technically!

LUCY: Technically?!

CHARLOTTE: Princess Lilac’s turned out great!

LUCY: Princess Lilac is a doll!

CHARLOTTE: With perfectly pierced ears! Just trust me!

LUCY: What if I die?!

CHARLOTTE: Don’t be a drama queen. Do you want pierced ears or not?

LUCY: Yes…

CHARLOTTE: Okay. Ready? One. Two.

LUCY: Ouch!

PRESENT

CHARLOTTE: See, you survived. And your ears are pierced.

LUCY: My earrings always hang crooked.

CHARLOTTE: You’re gonna’ be an old lady in the nursing home still complaining about your ears.

LUCY: Yeah, but probably more about my ability to use them.

CHARLOTTE: Probably true. Your hearing is terrible now. By then everybody will have to holler at you.

LUCY: It’d be nice if you were there hollering at me.

FLASHFORWARD (Lucy and Charlotte in the nursing home; using walkers)

LUCY: Charlotte!

CHARLOTTE: What?

LUCY: They forgot my oatmeal!

CHARLOTTE: You got oatmeal?

LUCY: Who?

CHARLOTTE: What?

LUCY: Oatmeal!

CHARLOTTE: Forget the oatmeal. Whatcha wanna do today?

LUCY: What’s that program on The Netflix that I like?

CHARLOTTE: With the man?

LUCY: And the shoes. And the map.

CHARLOTTE: The weather channel?

LUCY: Not feathers! The map!

CHARLOTTE: We are not watching TV! It’s Saturday!

LUCY: Stingray?

CHARLOTTE: Saturday!

LUCY: At the zoo?

CHARLOTTE: It’s the weekend, Lucy!

LUCY: I love the zoo!

CHARLOTTE: Hey, how ‘bout I race ya back to the rooms?

LUCY: Who’s got shrooms?

CHARLOTTE: Race. To your room!

LUCY: Oh with your old hips, I’ll leave ‘ya in the dust!

CHARLOTTE: I’m gonna’ kick your wrinkled old butt!

LUCY: On your mark

CHARLOTTE: Get set!

LUCY: Here we go!

(they move VERY slowly down the hall)

CHARLOTTE: I told ya’! Eat my shorts, grandma!

LUCY: You just wait ya old bat, I’m comin’ alive now!

PRESENT

CHARLOTTE: It’s a nice thought. Being old together.

LUCY: (starting to get sad) Yeah...it’s a great thought.

CHARLOTTE: That walker really gives you character, ya know?

LUCY: (sadly) You give me character.

CHARLOTTE: Luce...

LUCY: I know. Happy thoughts.

CHARLOTTE: I’m not happy about this either, you know. I didn’t sign up for this.

LUCY: Yeah, I know.

CHARLOTTE: Like...what’s gonna’ happen to my kids? What’s gonna’ happen to Luke? What if they can’t do it without me, Lucy?

LUCY: They can. I promise.

CHARLOTTE: How do you know?

LUCY: Because they’ll have me.

CHARLOTTE: And you’ll take care of them? Always?

LUCY: Always.

CHARLOTTE: And Sam and Lizzie, you’ll tell them about me? You’ll tell them I was cool and I was a great mom, and I loved them?

LUCY: Every single day.

CHARLOTTE: And you won’t bring up that time I almost left Sammy in the cart at Target?

LUCY: (laughs) I swear. I’ll talk about you so much they’ll feel like you’re there.

CHARLOTTE: I really want to be there.

LUCY: I really want you to be there.

CHARLOTTE: And you’ll make sure that Luke like cooks dinner and washes their sheets more than once a year?

LUCY: He will.

CHARLOTTE: (brief pause - gets choked up) I love him so much.

LUCY: I’ll take care of him.

CHARLOTTE: Okay. But don’t tease him too much when he does things wrong. And don’t hover, but check on him, okay? And someday...like eighty years from now...if he wants to date or whatever...tell him it’s okay. Be encouraging. And…

LUCY: Charlotte. (takes her hand) I love you.

CHARLOTTE: I love you too.

LUCY: I’m going to miss you forever. Honestly. Forever.

CHARLOTTE: You’re my best friend, Lucy.

LUCY: You’re mine.

CHARLOTTE: Luce, one more thing? Sing to them? To Sam and Lizzie? Please?

LUCY: I promise.

(Charlotte and Lucy hold hands and sing “You Are My Sunshine” after “when skies are gray” Charlotte closes her eyes and stops singing. Lucy finishes the song without her.)

CHARLOTTE & LUCY: (sing) You are my sunshine, my only sunshine. You make me happy when skies are gray.

LUCY: (sings) You’ll never know dear, how much I love you. Please don’t take my sunshine away.
```

---

## IC-0635: Locked Away

- Title: Locked Away
- Author (byline): Martin Aloia
- Work: Locked Away
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1933
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
(We see a dark, dreary cell block.)

Inmates: November first.

(An ambiguously ethnic inmate in the featured cell, SPAZ kneels, begins to pray.)

Spaz: God...please forgive me for all that I’ve done. I know it's been a little while since we've talked, but...hey that’s life, right? Just like why I’m in here. Just...life.

(A stiff, white prisoner, AMY, gets thrown into the cell.)

Amy: No, please! Let me go! Don't! You can't put me in here!

(Spaz sizes her up.)
Spaz: Are you beef?
Amy: Uh...What?
Spaz: Are you beef??
Amy: What do you--
Spaz: Are you beef?!?
Amy: I don’t under--
Spaz: ARE YOU BEEF?!
Amy: AHH PLEASE DON’T HURT ME!

(Spaz pulls back with a smile.)
Spaz: Nah, you chicken. (laughs) Man you should've seen the look on your face! I was all 'blah!'
and you were all like 'Oh my gosh, this ethnic girl is trouble!' Too much, man.
Amy: Um. I think I'll go to bed now if that's okay.
Spaz: It's not okay.
Amy: It's not?
Spaz: No.
Amy: Why?
Spaz: You think you're sleeping tonight? Or ever again?
Amy: Please, I--
Spaz: Pfft, man you ain't got no backbone. You can't just let people push you around like that,
stick up for yourself! Chicken.
Amy: Sorry...
Spaz: So what’d a pretty little white girl like you do to get in here anyway? Parents not like your
report card or somethin’?
Amy: I, uh...uh...nothing. What about you?
Spaz: Yeah. Nothing.

Inmates: November second…

(Spaz and Amy file through the cafeteria as slop gets piled onto their trays.)
Amy: Is that meat?
Spaz: Ooh, give me some of that orange stuff! Yeah. I miss you orange!
Amy: No, no, I don’t eat dairy! Or...whatever that is!
Spaz: C'mon Ricky. You know you can give me more brown bits than that. (gets it) There ya go!

(Spaz goes into the seating area.) Amy: I just...no thanks.

(Amy heads into the seating area. She hesitates, not knowing where to sit. She chooses the seat next to Spaz. A few spoonfuls in, she begins crying.)

Spaz: Uh…are you crying?
Amy: (crying) No...
Spaz: Uh. Why--
Amy: All I want is a Cinnabon and a cute pair of jeans!
Spaz: Oh. Oh girl...Nah, nah. You can't cry in here. Like, seriously, stop.
Amy: I just...I'm so scared...
Spaz: Someone will hurt you...
Amy: I don't know what's going on...
Spaz: Please, stop!
Amy: And I hate this place--
Spaz: Well yeah. You only like white people.
Amy: ...What?!
Spaz: Pfft don't even try to deny it! You should’ve seen how you was lookin’ at me when you
first got in here. I bet the only time you like seeing colored people is when their last name is
Kardashian.
Amy: No, I love all minorities--
Spaz: What's wrong with me? Huh? Yo I got a big butt too!

(She flashes her butt. Amy shields her eyes.)
Amy: I'm sure you do, now put that thing away!
Spaz: Calm down girl, I'm just messing with you!
Amy: ...You are?!
Spaz: Yeah!
Amy: Oh thank god! Wait. Why were you messing with me?!
Spaz: Had to get you to stop crying somehow. You're welcome. Man, you're like this sad little
puppy that just gets pushed around all the time. It's pretty hilarious.
Amy: Great. I’m glad the puppy-chicken amuses you.

Inmates: December 18th.

(Amy and Spaz fold towels in the laundry room. Amy struggles—Spaz excels.)

Amy: You know, being in here reminds me of summer camp. That place went through so many towels, I felt like I spent every summer working an unpaid internship at a laundromat. And I still suck at folding. Holy crap you work fast. How do you fold like that? Spaz: What? Oh I get it. You think all my people are born to be maids, don't you? Amy: Come on, Spaz, you know that's not what I meant, why do you just keep twisting my words-- Spaz: Ooh is chicken standing up for herself? Amy: --Jesus, I'm just trying to make conversation-- Spaz: Hold on. Did you really just say Jesus like that? Amy: What? Yeah...I mean, I saw you praying on the first day but I didn't think... Spaz: We’ve got to get back to work. Amy: Spaz…It's fine if you're religious and all... Spaz: No, Amy! It's not about religion. To save my sister I took someone's life. Okay? It's as simple as that. No church on Sundays, family grace before dinner. I’m not going to pretend I’m perfect... that my past isn’t filled with more pain than you could imagine...But I’m also not going to stand here and let you disrespect Jesus when he’s the only friend I have left. But you don't get it. How could you? You never will. You'll never understand. Amy: Maybe I won't, but...You know, I'm not perfect either. When my mom died... Everything fell apart. I mean, I felt so alone...just that gnawing loneliness that makes every breath feel like a crime. I kept feeling that crushing weight inside until one day I just...broke. I got so drunk on whatever I could find that I don't even remember how many cars I crashed into. I could’ve killed so many people, I-I mean they say I didn’t, but does that matter? Spaz. I'm just as much of a killer as you.

(Spaz walks over to show Amy how to fold.) Spaz: No. Like this...

Inmates: December twenty-fifth.

(Amy and Spaz face each other in their cell.)

Amy: Well, I know it's not much, but. It's the thought that counts, right?

(She hands Spaz a few cigarettes.)
Spaz: Aw, cigarettes! Man, thank you.
Amy: Sorry that's all I could afford.
Spaz: Pfft don't you even sorry me. Here's your present.

(Guess what it is...) Amy: Aw, you got me cigarettes too! Spaz: Merry Christmas Amy!

Amy: (laughing) Merry Christmas Spaz. (stares at the cigs) Do you miss your family? Spaz: Yeah. Amy: How do you deal with it? Spaz: Well, I know I kind of have to, so I just...do. You know? Amy: No. No, I don't. I'm sitting here wondering what they're doing right now, what kind of random food my dad's put on the table, my sisters fighting over some comment about their hair...it's dumb but it was home. You know? Spaz: Yeah. I know.

Inmates: January fourth.

(Amy sits on her bed, scratching tallies into the wall. Spaz does push-ups on the floor.)

Amy: One month, twenty-seven days...
Spaz: What are you doing over there, robot?
Amy: That's fifty-eight days, twenty-four hours in a day...
Spaz: You that excited to get away from your beautiful and talented and gorgeously awesome
cellmate?
Amy: Spaz. I just finally have something to look forward to for the first time in a long time. In
just under two months, that's something like one thousand hours...I get a chance at freedom. I get
a chance at parole.
Spaz: Man, we have got to find a better way to keep you entertained if parole is a shining future
to you.
Amy: Oh yeah? What are you, a connoisseur of in-prison entertainment?
Spaz: No, but I figure hanging out with me is better than scraping a penny against the wall all
day.
Amy: Hm. Point taken.

Inmates: January tenth.

(Amy and Spaz face each other, fingers all up.)

Amy: Okay, okay okay. So I say something like...never have I ever...skydived. Sky-dove…?
Doesn’t matter.
Spaz: Pfft, loser.
Amy: And you have?
Spaz: No.
Amy: That's what I thought. So, if you had answered yes, you would've put a finger down. Since
it was a no, you're fine. Got it?
Spaz: Okay okay, I think I got it. Let me try…um...I’ve never ever...ever...

Amy: Mhm…?
Spaz: (breaking game) Have you ever been in love?
Amy: Yeah, like that! You’ve got it.
Spaz: Yeah, yeah, okay. Let’s play for real now.

Inmates: February thirteenth.

(Amy and Spaz lie on their backs, staring at the ceiling as they laugh together.)

Spaz: And so the guy's popping out of the suitcase, right? And he goes, “I can hardly contain myself!”

(They burst out laughing. It comes to a stop soon after.)
Amy: I think we need better prison jokes.
Spaz: Alright, uh...two priests walk into a cell.
Amy: You told that one.
Spaz: Two bankers walk into a cell.
Amy: I told that one.
Spaz: Two talking monkeys walk into a cell.
Amy: What? How does that one go?
Spaz: I don't know, I was hoping you knew.

Inmates: March second.

(Spaz sweeps the concrete hallway. Amy rushes up to surprise her.)

Amy: Spaz...Spaz Spaz Spaz Spaz Spaz!
Spaz: Chicken chicken chicken chicken chicken! How’d the parole meeting go?
Amy: Okay, it was like...the weirdest job interview of all time, but...I got it!
Spaz: Yeeeeah, Freebird in the house!
Amy: Woo-hoo!
Spaz: Look out world, we’ve got a free-range chicken on the loose!
Amy: (laughs) Oh Spaz, seriously, thanks for everything. There’s no way I could’ve made it out
of here without you.
Spaz: Nah man. That’s what I keep trying to tell you--you can make it through anything. You
just gotta believe in yourself for a change.
Amy: Sooo, when’s your meeting?
Spaz: Never...
Amy: What? Spaz, but--
Spaz: I don’t get a meeting.

Amy: C'mon, how could you not get a meeting? You're not... Spaz: Amy. Amy: You're not in here for good...are you?

Inmates: March third.

(Spaz shoots a basketball on the outdoor court. Amy walks up.)
Amy: Nice shot.
Spaz: Thanks, Free-Range...So. How does it feel knowing this is your last day in paradise?
Amy: Yeah, paradise. It’s gonna be such a drag when I go home, sit on my couch and eat ice
cream for ten straight hours. The torture.
Spaz: You wanna play?
Amy: Oh no, I’m so bad at sports--for your own safety, it’s best that we don’t.
Spaz: Come on, one play. Get over there.
Amy: No, really--

(Spaz positions Amy across from her.)
Spaz: Ready?
Amy: No.
Spaz: Alright, here we go.
Amy: No, no--

(Spaz dribbles a few times, quickly fakes out Amy and hits the layup.)
Spaz: Oh boy--
Amy: I told you I was terrible!
Spaz: And you were right! Good thing you make up for it in other areas.
Amy: Oh, I do, do I? In what areas exactly?
Spaz: Pfft, just drop it, you ego-head.
Amy: Okay. Fine. Consider it dropped.
Spaz: You know, I thought we changed that about you.
Amy: Changed what?
Spaz: You’re about to head off into the free world and you still don’t have any balls, man.
Amy: I do too!
Spaz: No way. Here, come on, yell at me.
Amy: What?
Spaz: Yell at me. Let’s see what you got.
Amy: I’m not gonna--
Spaz: Do it! You’re not getting out of this prison until you yell at me!
Amy: No way!
Spaz: WHY NOT?!
Amy: Because...I’m Amy!

Spaz: --Uh-huh--
Amy: And...I’m awesome!
Spaz: --Yeah--
Amy: And you can’t tell me what to do, because I am YELLING AT YOU HOW COOL IS
THIS?!
Spaz: SO COOL!
Amy: I AM FEARLESS AND GLORIOUS--
Spaz: Bye bye chicken!
Amy: AND I WILL NOT HOLD BACK--
Spaz: Hallelujah praise the lord!
Amy: AND I WILL GO WHEREVER MY HEART LEADS ME!
Spaz: No one can stop y--

(Amy grabs Spaz, kisses her. They remain frozen in the moment. Amy's eyes widen.)
Amy: Oh my god, oh I’m sorry, I...I don’t know what I was thinking, I...I…
Spaz: Amy....
Amy: I think that...I was just, I--
Spaz: Don’t.
Amy: Don’t what?
Spaz: Don’t do this to me.
Amy: Do what?
Spaz: This.
Amy: Spaz…
Spaz: Amy.
Amy: It’s okay--
Spaz: NO! It’s not okay! It’s okay for you because in a few hours you’re gonna walk out that
door and get your old life back. Well I’ll still be here. I’ll always be here. Don’t you get that? I
took a man’s life so they took mine too. Please...don’t even look at me. I lost my chance with
you before we even met. Just...don’t make me fall in love with you any more than I already have.
Because at this point it’s no longer love, it’s just...pain.
Amy: Spaz…
Spaz: Just go. For your own sake. And don’t look back. Forget me and live the life you’re lucky
enough to be getting back.
Amy: Oh come on Spaz, even if I wanted to, I couldn’t forget you. When I walk out that door,
my heart’s gonna stay here. Locked away, guilty of falling in love with some crazy girl I slept
across from in my cell. Look...I won’t make you say goodbye. But please believe me when I say
that I’ll be back. Beef.
Spaz: Chicken.

(Amy walks out. Spaz drops to her knee, begins praying.)

Spaz: God...please. Tell me she’ll be back.
```

---

## IC-0636: Miss Erma Deveraux’s School

- Title: Miss Erma Deveraux’s School
- Author (byline): Clint Snyder
- Work: Miss Erma Deveraux’s School
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ERMA, EMMA
- Teaser before the introduction: No
- Spoken words (computed): 1726
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
ERMA: Welcome to Erma Deveraux’s school for civilized young ladies. I will break you! I will step on your pathetic ego until you are a puddle on ze floor and when you begin to melt into carpet, I will pick you up and sculpt, sculpt, sculpt until zer is a civil and proper young woman in front of me.

EMMA: I’m sorry… wh-what did you say? (Stuttering frightened.)

ERMA: (Pause.) Oh, I see you are thinking you make funny?

EMMA: I just want to make my mom happy. I don’t want to cause any trouble/

ERMA: Well I do. My name is ERMA! ERMA! ERMA! Remember zis because it is the name you will scream into your pillow when you are having ze little baby nightmares.

EMMA: I just don’t understand why mother would drop me off here like that. She told me she was going to get me a new puppy and then… then she was driving off laughing…

ERMA: I am not your mama.

EMMA: Thank goodness… I mean… oh, I feel like I’m going to pass out.

ERMA: Hahaha! You would be lucky to have a mama like me. All of my children are doctors, lawyers and bear wrestlers!

EMMA: Oh my!

ERMA: Mmmhmm…

EMMA: What ummmmm… wonderful kids you must have

ERMA: They are not “kids”. Unfortunately for Erma she could never find a man who could handle her superior etiquette training… so instead she raised dogs.

EMMA: Wait… You trained dogs to be doctors, lawyers and bear wrestlers?

ERMA: Yes, Erma zat good.

EMMA: Oh, if only walls weren’t covered in barbed wired!

ERMA: Speak lively! Speak lively!

EMMA: What does that even mean?

ERMA: It means stop speaking like you are little zombie baby… Wa! Wa! I want ze bottle.

EMMA: Zombies don’t drink milk… duh…

ERMA: Oh! Well look at you! I better watch out so that your big fat head does not knock me down when you move around.

EMMA: It just… doesn’t make sense why would a zombie drink milk like a baby… its not a baby it’s a zombie.

ERMA: Maybe is a baby zombie and drinks liquefied brains from bottle. I suppose you didn’t think of that you fat head little zombie baby girl!

EMMA: I don’t appreciate your comments… they’re probably illegal or something… I would be careful, you can get sued for just about anything these days…

ERMA: Sue is a silly American name… you have the American aura about you… the stink of it circles around you like a stinky stinky perfume cloud! Take yourself to a department store stinky!

EMMA: I love department stores! Specifically ones selling clothing in different descriptive colors… For instance you’d think there’s just black but nope, there’s midnight black and wax crayon black and “bleeding soul black” and “oooohhhh a pen just exploded in my mouth now my tongue is black” black.

ERMA: Yes… so you watch your tongue or I will use it to tie your napkin together to make beautiful swan.

EMMA: I’ll be quiet! I’ll be good, just… please don’t eat me!

ERMA: Oh, I would not eat you… it is not what civilized lady would do… but if I did eat you I would wipe mouth with napkin folded like swan!

EMMA: Oh my!

ERMA: You seem weak, like weak little baby fish! Swim baby fish! SWIM!

EMMA: (Moving arms weakly, sobbing.) I’m swimming, I promise I’m swimming!

ERMA: We shall see… I will now give you test!

EMMA: Test! But I haven’t learned anything yet?!

ERMA: That is real test. Civilized lady does well under pressure. You either sink or swim and by sink I mean suffer.

EMMA: Oh dear…

ERMA: And by swim I also mean suffer!

EMMA: Think Emma! How are you gunna get yourself out of this one!?

ERMA: THIS IS LITTLE LADY DISCIPLINE! (She slaps her hands together.)

EMMA: What? What are you reffering to? I don’t understand the question! You can’t fail me if I don’t understand the question. (Sobbing.)

ERMA: Pull yourself together. (Slaps.) This! (Holding up hand.) This is little lady discipline. Every time you decide that you would rather be boarish uncivilized cow I have her correct you!

EMMA: Correct me! What do you mean correct me?! FOR GOODNESS SAKES HOW WILL YOU CORRECT ME!?!!!

ERMA: Like this. (She slaps her hard.)

EMMA: Ohhhh! (Sobbing) How can you be so cruel! You’re just a mean old lady! I am traumatized stop traumatizing me! You keep yelling at me and I don’t know why… the only thing that I can think of is… is maybe you’re just unhappy with your life? Did you ever consider that?! Maybe you’re the one with the problems!

ERMA: Oh I don’t have problems, just one little one… you!

EMMA: How can you say a thing like that! What ever happened to everyone gets a gold star?! What ever happened to no child left behind?! What happened to you that makes you want to pick and prod and poke and eat away at me until there is nothing left and I end up resembling the leftovers of a very cheap seafood buffet… an empty shell.

ERMA: I spent twenty two years of my life crocheting sad little baby sweaters, WITH MY FINGERS! NOW YOU WILL BE CIVILIZED!

EMMA: I WILL BE CIVILIZED!

ERMA: YOU WILL BE EDUCATED!!!!!

EMMA: I WILL BE EDUCATED!!!!!

ERMA: YOU WILL RECYCLE!!!

EMMA: I will recycle? That one doesn’t really seem like it fits with the others?

ERMA: ZOOT! (Slaps.)

EMMA: What does zoot mean?! WHAT DOES IT MEAN?!

ERMA: IT MEANS I AM ZE BOSS! AND IT MEANS I WILL HAVE A CIVILIZED YOUNG LADY BY THE TIME I AM THROUGH WITH YOU!!!

EMMA: OK! Yes ma’am whatever you say!

ERMA: Not whatever I say, EVERYTHING I SAY!!! NOW SAY I AM LITTLE TEAPOT!

EMMA: What?!

ERMA: I am little teapot! (Slaps.)

EMMA: (Sobbing.) I am… a little… teapot.

ERMA: Short and stout! SHORT AND STOUT!

EMMA: (Sobbing.) Short and stout! SHORT AND STOUT!

ERMA: Here is my handle… I am civilized young lady!

EMMA: Here is my handle I am civilized young lady!

ERMA: Good, now we are getting somewhere!

EMMA: Good, now we are getting somewhere!

ERMA: DO NOT MOCK ME YOU INSCOLENT FOOL!!!! (Slaps twice.)

EMMA: I am so confused! I am scared and I am confused!

ERMA: Yes, but are you feeling like rude little girl?

EMMA: Ummm… (Erma raises her hand threateningly.) No? No! I am just feeling sweet as pie! Cake! Soufflé! A chocolate soufflé!

ERMA: Good now we are getting somewhere!

EMMA: Please don’t take me somewhere! I don’t want to end up in a dungeon or a basement or on the bottom of the ocean wearing cement shoes.

ERMA: The only shoes you will be wearing are dancing shoes!

EMMA: What?

ERMA: Now DANCE!

EMMA: Oh, ummm… ok.. (She dances and hums badly.) I am uh… just dancin’ here so you don’t slap me again… tada.. dada… ma..yeah?

ERMA: Now SING!

EMMA: SING?

ERMA: SING! (Raises hand threateningly.)

EMMA: (Half-sobbing.) Oh, say can you see… by the dawn’s early… thing…. Please don’t slap me la-DY… you just scare me so much…

ERMA: YOU WANT FEEL PAIN!

EMMA: (Still singing melody of national anthem.) OH YOU’RE SCARE-Y LADY!!! PLEASE DON’T HIT ME ANYMORE!!! I FEEEL LIKE CRYING, BECAUSE YOU’RE LIKE HERCULES!

ERMA: What is HERCULES?! Why you call me HERCULES?!

EMMA: Hercules means… ummm… hero… lady-hero in Latin… look it up… it’s latin.

ERMA: The only thing I will be looking up is my name is special etiquette history books… WE WILL NOW TEST!

EMMA: TEST? I thought we were already testing! I can’t handle the pressure!

ERMA: TEST! NOW! I AM NOW BOYFRIEND!

EMMA: I’VE NEVER HAD A BOYFRIEND!

ERMA: THIS DOES NOT SURPRISE ERMA! NOTHING SURPRISES ERMA! YOU ACT NOW!

EMMA: Boyfriend.. ermmm… yes… goodness…. You are my boyfriend… how would a civilized lady act around a boyfriend?

ERMA: If you were girlfriend I would break up with you now, and by break up with you I mean break you, and by break you I mean break spine.

EMMA: Ahhh! Please don’t break my spine miss lady! I need that for things! How am I ever supposed to be a civilized lady with a broken spine!

ERMA: How are you ever supposed to be civilized lady at all? You are useless little broken fish!

EMMA: I don’t even like seafood!

ERMA: Another sign of weakness!

EMMA: I’m not weak! I’m not weak! Stop bullying me! I am perfectly civilized the way that I am! I don’t need some French baguette telling me what I should and should not do! I refuse to be bossed around! I refuse it and if that means that you think I’m some sort of an uncivilized heathen that just crawled out of a swamp dragging my knuckles, then so be it! I would much rather be me than a rude selfish pig!

ERMA: (Clapping.) Very good!

EMMA: Please don’t hurt me.

ERMA: I am not going to hurt.

EMMA: Oh, so it’s going to be a quick painless death?

ERMA: No! You are learning much after all my little sweet potato.

EMMA: Please don’t call me a vegetable.

ERMA: Oh.. the little potato is suddenly offended because because she does not want to be a vegetable…. Well let me tell you little potato that you are not a tomato. There is no question of your identity as a fruit or a vegetable!

EMMA: A tomato is a fruit!

ERMA: You’re a fruit!

EMMA: I thought I was a vegetable?

ERMA: Don’t you get snippy with me! You want to know reason I call you potato? Because back in the old country I had a sad little potato that I would water and care for and feed radioactive soil. I make sure that this potato is well cared for for many many days and you want to know what happened to the potato plant?!

EMMA: No.

ERMA: It died! It died because it was weak, just like you! I swore from that moment on to never be weak like the sad little potato plant, but instead to grow strong like her highly irradiated sisters! So that I could one day stand strong on a plate mashed and delicious with butter and a delicious stinky fish…

EMMA: BE QUIET ABOUT YOUR DUMB OLD POTATO YOU WEIRDO! NOBODY CARES ABOUT YOUR IRRELEVANT STORIES OR VEGETABLES! (Pause. Afterthought.) You dress badly and smell…

ERMA: Ha! Very good! This is lesson I have been teaching whole time! The only way to survive in modern world as civilized young lady! It is not all fancy spoons and folded napkins! No!

EMMA: Oh my! (Taken aback a little afraid she might strike.)

ERMA: You are learning to stand up for yourself. You found your spine and are no longer like little sloppy jellyfish.

EMMA: Right… well… I’m not entirely sure what you’re talking about, but I’m going to leave now because, you know, I really don’t like you… and I’d rather walk five miles home than listen to you drone on about the French revolution…

ERMA: Very good! Very good! Class dismissed! (She pats herself on the back.) You get nice back pat. Erma Deveraux you have done it again! Look out world we have another civilized lady ready to take over!
```

---

## IC-0637: Clyde Hendrickson’s Mother-Daughter Dialogues Copyright 2008 by Clyde Hendrickson.

- Title: Clyde Hendrickson’s Mother-Daughter Dialogues Copyright 2008 by Clyde Hendrickson.
- Author (byline): Not specified
- Work: Clyde Hendrickson’s Mother-Daughter Dialogues Copyright 2008 by Clyde Hendrickson.
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2903
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
Be nice to your family.

Clyde Hendrickson’s
Mother-Daughter Dialogues
Scenes to be played on a blank stage.
Actors playing mother & daughter do not age over the course of the play.

nine-years old.
MEGHAN. Mom, when you and dad got married, did you give him The BJ?
MOTHER. WHAT?
MEGHAN. My friend Mikala said on their wedding nights, the Moms give the Dads the BJ.
MOTHER. Meghan, I don’t… You shouldn’t… ask your father.
MEGHAN. Ok.
MOTHER. Wait! On second thought, just go to your room and pray.

twelve-years old.
MEGHAN. Mom, can I be president when I grow up?
MOTHER. Oh honey, sure.
MEGHAN. Really?
MOTHER. Well, maybe. Society will have to change.
MEGHAN. So a girl can be president?
MOTHER. So a fat girl can be president!
MEGHAN. Oh. So I just have to get thin?
MOTHER. And work hard in school, etc. But thin is most important.
MEGHAN. Alright, I’ll try harder.
MOTHER. I know you will. Your Dad & I believe in you.
MEGHAN. Thanks, you’re the best!

keeping tabs.
MEGHAN. Hi Mom!
MOTHER. Did you get taller?
++
MEGHAN. Hey Mom!
MOTHER. Did you get fatter?
MEGHAN. Since the last time you saw me?
MOTHER. How many of those meringues did you eat?
++
MEGHAN. Hi, I’m home from camp!
MOTHER. Look how much you’ve grown.
++
MEGHAN. I’m back from Becky’s sleepover
MOTHER. Look how much your thighs have grown.
MEGHAN. I was only gone for 12 hours…

prom date.
MEGHAN. Can you wear red to prom?
MOTHER. Might lead to some fire truck jokes.
MEGHAN. Mom!
MOTHER. Only because it’s so bright, dear.
MEGHAN. James likes red.
MOTHER. I’m sure James won’t care after his forth vodkatini.

MEGHAN. We’re not gonna drink.
MOTHER. That’s not what the bottle of Olde English I found under your bed says.
MEGHAN. I couldn’t even finish it, it was gross. It tasted like bums were fighting in my mouth.
MOTHER. Let’s hope James is as discriminating.
MEGHAN. Oooh! How about this one!
MOTHER. Lavender is a whore color.
MEGHAN. That’s like the 50th dress you’ve shot down for making me look promiscuous. I could wear
a pantsuit.
MOTHER. You should follow my advice. Remember when I warned you not to wear white to Wet &
Wild? But you never listen to me.
MEGHAN. Maybe that’s because all you ever say is that I’m a disappointment and, and you’re always
comparing my thighs to Tina Turner’s head.
MOTHER. The truth hurts.
MEGHAN. I might have a bit of cottage cheese, fine, but I think there are more truths to me than that.
MOTHER. We’ll see.
MEGHAN. I really, really want this dress.
MOTHER. You’re not getting it. What about that one?
MEGHAN. Mom, it has lace. I’d look like a table setting. What is wrong with you?
MOTHER. Let’s go to Sears, they’re having a sale.
MEGHAN. You know what? You can go without me. I’ll wear whatever you pick out, since you
always know what’s best.
MOTHER. That’s the smartest thing you’ve said in a while.

watch what you eat. MOTHER. Meghan! Meghan, it’s almost time to go. James will be here any minute.

MEGHAN. I’ll be out in a second.
MOTHER. You’ve been in there 10 minutes!
MEGHAN. No, Mom, I – don’t come in…
MOTHER. What is that smell? Were you throwing up? Are you ok?
MEGHAN. I’m fine.
MOTHER. If you’re sick you can’t go to prom. Are you pregnant?
MEGHAN. No mom, I am NOT pregnant.
MOTHER. Just nerves. We’ll get you some Sprite. FRANK BRING MEGHAN A SPRITE. SHE’S
BEEN PUKING.
MEGHAN. Lovely. Just lovely. I’m fine.
MOTHER. Why were you throwing up?
MEGHAN. It was… well…
MOTHER. Wait, were you…
MEGHAN. Don’t ask.
MOTHER. Were you purging?
MEGHAN. Just a little. To fit into this old dress.
MOTHER. Why would you do that? Was it something you read on the internets?
MEGHAN. No…
MOTHER. Your friends pressured you? That Mikala, she’s too thin anyway.
MEGHAN. No. It was you.
MOTHER. Don’t be ridiculous. You know I love you just the way you are. FRANK WE NEED
SPRITE AND SOME SALTINES.
MEGHAN. And some earplugs. Do you really like me the way I am?
MOTHER. You’re going to be a very beautiful woman.

MEGHAN. You think so.
MOTHER. Let’s get you out of that old dress.
MEGHAN. But I’m still going.
MOTHER. I know, I know, but not in that.
MEGHAN. What do you mean?
MOTHER. I bought you the dress you liked.
MEGHAN. The lavender one?
MOTHER. Yes. You did look stunning in it.
MEGHAN. Thanks.
MOTHER. A stunning prostitute, but still… radiant. You are a lovely girl.
MEGHAN. You should try and say that more often.
MOTHER. Don’t blame me for everything.
MEGHAN.

first visit to college.
MOTHER. So this is your dorm room. Where’s the Patrick Swayze poster I bought you? He looked so
good in that Speedo.
MEGHAN. It uh… got lost… or, uh… I gave it… to, uh, charity. This little orphan girl that loved Dirty
Dancing
MOTHER. How’s everything? How’s school?
MEGHAN. Fine. I have a lot of work.
MOTHER. How are you?
MEGHAN. I’m ok…
MOTHER. Are you sure – you sound funny.

MEGHAN. Mom, I’m fine, just stressed, and tired.
MOTHER. You sound pregnant.
MEGHAN. Mom, no – what?
MOTHER. Are you tired and groggy because you’re pregnant? That’s what it sounds like.
MEGHAN. Mom, I haven’t even dated a guy, much less slept – oh my god this is SO none of your
business.
MOTHER. Young lady, you know it’s my business. Now you know you’re too young to be having a
child.
MEGHAN. Mom, no one is having a child. I am not pregnant.
MOTHER. (Weeping) I just worry so much about your decisions. I want you to be happy.
MEGHAN. We agree on this Mom, really, we do.
MOTHER. I hope so. (sniffing) I hope so.
MEGHAN. No babies!
MOTHER. Never? How could you say that?
MEGHAN. I didn’t mean never… no, you just said you didn’t want me…
MOTHER. You don’t think I’d be a good grandmother?
MEGHAN. You’d be a great grandmother! I’ll have a million little adorable babies for you to cuddle,
ok?
MOTHER. Alright, but not until you’re married.
MEGHAN. Oh my god.
(Mom is opening drawers)
MEGHAN. What are you looking for?
MOTHER. Condoms.
MEGHAN. I don’t have any condoms! I’m not… I don’t need them.
MOTHER. You’re not going to use a condom?

MEGHAN. No, no, I… fine, look, there are some in the bathroom. (She points)
MOTHER. (looks) You better not use these.
MEGHAN. But, I’m not.
MOTHER. Then why do you have them?
MEGHAN. I wonder if it’s too late to transfer to a school that’s out of state.
MOTHER. Maybe to an all-girls school.
MEGHAN. Anyway. I’m thinking of being a social worker. I love this sociology class I’m in. The
Professor, Dr. Bryant, he used to work in Port-au-Prince –
MOTHER. Oh no. Just because you have a crush on some hippy professor you are not going to throw
your life away. Or this expensive education. You’re going to be a doctor, a lawyer or own a chain of
grocery stores.
MEGHAN. But social work is what I want to do. You said I could do whatever I want.
MOTHER. Meg, just because you are able to do anything you want doesn’t mean you can do anything
you want.
MEGHAN. That doesn’t make any sense, Mom.
MOTHER. It makes perfect sense to me. You can do anything you like, as long as I approve.

One other thing....
(on the phone)
MEGHAN. What’s up mom.
MOTHER. I can’t find the phone.
MEGHAN. You’re on the phone.
MOTHER. My cell, I mean, I can’t find it.
MEGHAN. I’m 1200 miles away. How would I know?
MOTHER. You have to help your mother when she needs you.

MEGHAN. Ok…
MOTHER. Guess.
MEGHAN. Did you leave it in the linen closet, like last time?
MOTHER. No, I checked. The pool filter too.
MEGHAN. Did you throw it away? You once threw away the television remote.
MOTHER. I guess I’ll have to rummage through the trash barrel later.
MEGHAN. Man, I miss all the good stuff being away.
MOTHER. Haha. Oh, that reminds me, your cat died.
MEGHAN. WHAT?
MOTHER. Yes, Mr. Skittles’ thyroid finally caught up to him. We put him to sleep this morning.
MEGHAN. Why didn’t you mention that first?
MOTHER. That seems cruel. To just call you up and say “Guess what, your cat died.”
MEGHAN. The small talk did not make it any better.
MOTHER. I tried. I tried.
MEGHAN. Did you leave your cellphone at the vet?
MOTHER. Oh! You know I think I did.
MEGHAN. Poor Mr. Skittles.
MOTHER. We’ll miss him.
MEGHAN. He hated you, you know.
MOTHER. But he paid attention to me. And that is rare in this house.
MEGHAN. I wonder why. Poor Mr. Skittles… I gotta go tell Steve.
MOTHER. Your boyfriend never met Mr. Skittles.
MEGHAN. But he is capable of empathy. Unlike some people.

MOTHER. Well tell Steve I said “Sorry about Mr. Skittles” then. MEGHAN. Thanks, I will.

many blessings.
(On the phone)
MEGHAN. Mom, I have big news.
MOTHER. Ooooh, what is it, honey?
MEGHAN. It’s about Steve.
MOTHER. Oh no. Did he have a secret baby out of wedlock, and now the mother is trying to kill you
both?
MEGHAN. Wow. Did you get that from Law & Order, Lifetime or just your old batty Republican
friends?
MOTHER. You know I still have the number of Barry Steinman’s son. He’s at Yale Law.
MEGHAN. I am not dating Dick Steinman! He’s 5’2” and he smells like fish all the time.
MOTHER. You shouldn’t judge based on looks. Or odor. That’s a disorder called Trimethylaminuria.
MEGHAN. How do you know these things? Dick Steinman smells like fish because he doesn’t bathe
and he eats a jar of pickles every day. Besides, I don’t need Pickle Dick’s number because Steve and I are
getting married.
MOTHER. (gasps) Oh, Meghan!
MEGHAN. I know, I’m so happy!
MOTHER. That is so wonderful, I’m – Oh no, you can’t get married!
MEGHAN. Why not?
MOTHER. You’ll never fit into a dress, dear. Oh Steve was so nice to ask, really, what a sweet fellow.
MEGHAN. Jesus H. Christ.
MOTHER. Well we can just put it off until you’re in shape. I might have to lose a couple pounds too.

MEGHAN. Put it off?
MOTHER. About two years to plan it all, and slim you down.
MEGHAN. We’re doing it in three months.
MOTHER. THREE MONTHS? Are you pregnant?
MEGHAN. Actually, yes.

It’s all right, right?
MEGHAN. Can you see it?
MOTHER. See what?
MEGHAN. My bump.
MOTHER. Good heavens no.
MEGHAN. Good. I’m nervous.
MOTHER. Well, you can’t change your dress again.
MEGHAN. I wouldn’t have changed it if you hadn’t made that comment.
MOTHER. I’m sorry, but your back is not your strongest feature.
MEGHAN. Do you think Steve’s the right guy?
MOTHER. Honey, there is no right guy. There are good guys and bad.
MEGHAN. Is he good?
MOTHER. He’s marrying you, so yes. But he got you pregnant, so maybe.
MEGHAN. I guess we’ll see. At least I got married before Becky.
MOTHER. Yeah! I’ve already rubbed it in with her mother several times.
MEGHAN. Mom!
MOTHER. Gently. You know, “When Becky gets married, I’m sure she’ll do it in spring.” You know.

MEGHAN. That’s pretty funny. Thanks for coming, Mom. I was worried you’d make good on your
threat not to come.
MOTHER. I was pretty upset for a little while.
MEGHAN. Two of the three months.
MOTHER. It flew by.
MEGHAN. In a rage.
MOTHER. But I wouldn’t miss this for the world.
MEGHAN. I know. A chance to berate my back.
MOTHER. Among other things.
MEGHAN. Do I look pretty, though, for once?
MOTHER. Steve will be thrilled.
MEGHAN. You think?
MOTHER. Well we already know he likes your looks.
MEGHAN. Mom! But do YOU think I’m pretty?
MOTHER. Mothers don’t worry about that sort of thing.
MEGHAN. Of course not.
(offstage cue)
MEGHAN. It’s time!
MOTHER. Remember: suck it in, don’t trip, and don’t sneeze on the priest! Jesus will frown on you if
you give him a cold.

miscarriage
MOTHER. You’ll be fine.
MEGHAN. What if I can’t have another?
MOTHER. No no, you know I had two before I had you & your brother.

MEGHAN. I know but… you were lucky.
MOTHER. It happens.
MEGHAN. But what if…
MOTHER. What if what?
MEGHAN. What if Steve doesn’t love me anymore?
MOTHER. Why?
MEGHAN. Because I couldn’t have a baby.
MOTHER. Then I’ll snap his wiener off and put it in a jar of Vlasic Kosher Pickles.
MEGHAN. (giggles)
MOTHER. When are you going to try again?
MEGHAN. I haven’t decided yet.
MOTHER. Well, soon I hope.
MEGHAN. Or maybe never.
MOTHER. Never?
MEGHAN. I don’t have to have kids.
MOTHER. You would leave me without a grandchildren?
MEGHAN. What about Brian?
MOTHER. Your brother’s never getting married. No, no, you have to have kids.
MEGHAN. I don’t have to do anything.
MOTHER. Well, I didn’t raise you to have that attitude.
MEGHAN. And thank God you’re done raising me. I’ve put up with this guilt, with this stupid
insecurity long enough. I have plenty of problems without you throwing everything you’ve got at me,
for no reason other than to be proud of how much you can still belittle and control me.
MOTHER. I want what’s best for you, no matter what.

MEGHAN. Really, well what would be best for me would be if you got out of here. Out of this room,
out of my life.
MOTHER. You’re so ungrateful.
MEGHAN. Most likely. But at least I’m not like you.
MOTHER. Alright, Meghan, whatever you say.
MEGHAN. Exactly. Get out of here!

it’s my party.
(phone conversation)
MEGHAN. Hello?
MOTHER. Hello, Meghan, it’s your mother.
MEGHAN. Ah, so it is.
MOTHER. Well… hello. Your father is retiring. He’s having a party. Would you like to come?
MEGHAN. Will the whole family be there?
MOTHER. Yes.
MEGHAN. Then definitely not.
MOTHER. If you change your mind, it’s in two weeks at our house. At your house. We’d love to see
you.
MEGHAN. That’s nice.
MOTHER. Give me a call if you’re going to come.
MEGHAN. Don’t wait around.
MOTHER. Your brother wants you to meet his wife, I’m sure.
MEGHAN. We had dinner last week.
MOTHER. Oh. Oh, I see. Well then.

MEGHAN. Bye Mom.

separate, unequal.
MOTHER. Your nephew is so cute.
MEGHAN. He’s great. I really like him.
MOTHER. Do you see him a lot?
MEGHAN. Sure.
MOTHER. I never know these things.
MEGHAN. Brian doesn’t tell you?
MOTHER. Oh, he’s busy, his family, his work.
MEGHAN. I’m surprised you even told me Dad died.
MOTHER. He would have wanted me too, you know.
MEGHAN. Yes, he was an actual human being.
MOTHER. What if I’d gone first.
MEGHAN. You would have never let that happen.
MOTHER. It took you long enough to tell me you were divorced.
MEGHAN. I’ve been trying to reorganize my whole life, to clean everything out.
MOTHER. I guess you haven’t gotten to your thighs yet.
MEGHAN. Mom.
MOTHER. I’m just saying, if you want a new husband.
MEGHAN. Mom, I don’t want another god da – darn husband. How are we back to this conversation
already? You haven’t seen me in three years.
MOTHER. Nothing changes with you.
MEGHAN. With us.

MOTHER. Well, I’ll save it, for your father.
MEGHAN. Ok, fine, me too.
nothingness.
(Mom clicking through TV channels)
MEGHAN. Hi Mom.
(nothing)
MEGHAN. I said, hi.
(nothing)
MEGHAN. I figured I should drop by. I was in the neighborhood.
(nothing)
MEGHAN. I hope you’re not still buying too much jewelry off QVC.
(nothing)
MEGHAN. Although it looks like you are.
(nothing)
MEGHAN. Well, I’m moving to Seattle. This was our last chance… maybe for a while.
(nothing)
MEGHAN. I’m sure Brian told you, though.
MOTHER. Oh lord.
MEGHAN. What?
MOTHER. Let’s not talk about any of it at all.
MEGHAN. Ok. Ok, we won’t. By the way, I’m taking my prom dress.
MOTHER. Do you still fit into it?
MEGHAN. Yes, as a matter of fact, I do. I was hot and chubby then, and I’m deliciously chubby now. I
look effing fabulous in lavender.

MOTHER. Knock yourself out.
MEGHAN. I will. Mom…
MOTHER. Yes?
MEGHAN. I left my new cell number on the fridge.
MOTHER. Ok.
MEGHAN. Ok.

mother-daughter.
MOTHER. I figured I should drop by.
MOTHER. So what did…
MEGHAN. 50/50.
MOTHER. Live or die?
MEGHAN. What else? Coke or Pepsi?
MOTHER. Do you want a soda? I’ll ring for the nurse. Do they check on you enough.
MEGHAN. They’re fine. They’re very good. I get attention.
MOTHER. Well you don’t have a husband anymore to help you so…
MEGHAN. That’s true.
MOTHER. Wait, you’re not mad at me for saying that?
MEGHAN. I could be, but… it’s true. I wish I had someone.
MOTHER. It’s nice. I don’t know what I’d do without your father.
MEGHAN. But, well, I’m not that lucky. Sorry.
MOTHER. It’s my fault.
MEGHAN. 50/50.

MOTHER. I’m just so worried about you.
MEGHAN. Well, good to know some things never change.
MOTHER. It’s my only job in this world
MEGHAN. And that’s weirdly comforting.
MOTHER. Oh, Meghan.
MEGHAN. I don’t know what I should say.
MOTHER. Well, neither do I.
(silence)
BOTH. Do you –
MEGHAN. love me?
MOTHER. still love me?
(another silence)
MOTHER. You look so thin.
MEGHAN. THANK YOU! Finally.
```

---

## IC-0638: Rush Hour

- Title: Rush Hour
- Author (byline): Stephanie Christensen
- Work: Rush Hour
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1833
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
[Enter Jasmine, texting on her phone, looking for her Rideshare car. She is late for work. Jasmine’s phone makes a noise, getting a notification. She looks up to see her car pull up. She climbs into the car.]

Jasmine: Hello! I’m Jasmine. White Honda Accord, right? [pauses, as if listening, nods] Yes, yeah, I know this is a Quick Ride Carpool. You can pick up anyone along the way, but just so you know, I am running late. [waves $1 bill around] And maybe Mr. George Washington can convince you to skip some passengers. [dejected, mumbles] Fine… [Phone rings and she picks up] Yeah? Yeah, look, Taylor, I am on my way to work. [looks shiftily at driver, whispers] …this numbskull Quick Ride driver won’t skip any other passengers. [overdramatic] I know, right?! Even the one-dollar bill trick didn’t work. [jerks forward, makes a face at driver] Hold on, we just stopped. Yeah, we’re picking someone else up.

Cary Anne [to driver]: HELLO, sweet angel, thank you for picking me up! I can’t navigate a flamingo from a pigeon in this big city. That’s what I get for moving to the Big Apple, huh?

Jasmine [surprised, displeased]: Cary Anne?!

Cary Anne [super excited]: Oh my gosh, Jasmine! You darling busy bee! My morning just keeps getting better.

Jasmine: And mine’s right up there with kidney stones. Just a second. [back to phone] Taylor, I have to go. My brother’s…colorful… girlfriend just got in the car. Yeah. Bye. [hangs up, murmurs] Someone’s getting 1 star today.

Cary Anne: Oh Jasmine, are you getting any sleep? Poor thing. Those are some dark bags under your eyes.

Jasmine: Excuse me. [blinks in shock] That was really rude?!

Cary Anne: What??? I never said they weren’t designer. They could be Gucci.

Jasmine: This is just my luck. When my brother plucked you out of the armpit of Timbuktu—

Cary Anne: Oh, not Timbuktu— Arkansas!

Jasmine [stunned]: This is the worst day ever. Didn’t Josh tell you that New Yorkers were grumpy in the morning?

Cary Anne: Oh, Josh isn’t grumpy in the morning! Quite the opposite, I find he’s actually more sprite and daring in the morning, if you know what I mean.

Jasmine: EWW! STOP. Josh is my brother. Do you get why I wouldn’t want to KNOW THAT?

Cary Anne: don’t do that grumpy thing, Jaz. I know that there’s a compassionate, divine soul somewhere deep down in you.

Jasmine: Don’t call me Jaz. Only my friends call me Jaz.

Cary Anne: Come on! We could be friends. I’ve seen your brother naked.

Jasmine: EW!

Cary Anne: I’m just saying. If I can love every imperfect part of him, I can love you too. Every part of you.

Jasmine: Every part of me?

Cary Anne [gasps]: That’s not what I meant! Jasmine [grabs Carry Anne’s hands sweetly]: Maybe in another life, Carry Anne. When you’re not dating my brother.

Cary Anne: That’s… [leans forward to driver] Just so you know, that is not what I meant.

Jasmine: Okay, let the driver know little miss Arkansas is not homosexual. That’s not homophobic.

Cary Anne: You know I am very accepting of the multi-sexual community. Heck, who am I to judge! I’m with the man I love. Can you say the same?

Jasmine: Love is an overrated concept. It’s left me cold and dull inside. To be honest, I’m over that part of my life.

Cary Anne: Over love? How can you be over love?

Jasmine: It’s just too hard meeting the right person.

Cary Anne: Oh come on! You can meet the right person anywhere. Like, at a stoplight perhaps?

Jasmine [scoffs]: Come on, what is that supposed to— [Jasmine is cut off by Cary Anne leaning over her to lower the window and wave at a group of attractive young men in the car next to them]

Cary Anne [yelling]: HEEEYY!! HEY BOYS, OVER HERE! Yeah that’s right, I’m talking to you, Sideburns. My friend here is looking for a boyfriend. She says hi, isn’t that right, Jazzy?

Jasmine: Cary Anne, STOP IT! [pushes Cary Anne off her] Stop it. [turns to window, and discretely does the call me sign so Cary Anne doesn’t see] …call me.

Cary Anne: Now what did I say?

Jasmine: That was so embarrassing, Cary Anne! [both look at each other and laugh] …Well. You pushed me out of my comfort zone.

Cary Anne: That’s why your brother loves me.

Jasmine: Why aren’t you with him, by the way?

Cary Anne: what do you mean?

Jasmine: He has a car. It’s no Lamborghini, but it works.

Cary Anne: You can say that again. [a bit flustered] but no, I was just with him… [Jasmine eyes her suspiciously]

Cary Anne: We were just at brunch. You know, that gourmet bacon place?

Jasmine [hungry]: Oh my… bacon…

Cary Anne: Mhmm… and their virgin mimosa are marvelous too. Josh was late for work, so he took the car, and called a Quick Ride Carpool to get me home.

Jasmine [mega suspicious now]: Oh yeah? I think you maybe had one too many mimosas, because this car is going nowhere near your guys’ house.

Cary Anne: virgin mimosas…

Jasmine: Is there something you’re not telling me, Cary Anne?

Cary Anne: No, uh, it’s nothing! I must have just put in the wrong address. C’mon! We were just starting to be friendly.

Jasmine: Oh no! It should take you longer than 5 minutes in a car to realize I am not a friendly person. Especially when my brother’s girlfriend is sneaking around, and possibly putting his heart and his dignity on the line.

Cary Anne: Oh no, Jasmine, it’s not like that. I am not sneaking around. It’s just… where I’m going is kind of a secret.

Jasmine: Hmm. A non-sneaking around kind of secret?

Cary Anne: Exactly!

Jasmine: Cut the crap, Cary Anne. Your lies stink like blue cheese.

Cary Anne [sighs]: Do you promise you can keep a secret? He’ll be awfully mad I told you.

Jasmine [making fun of her a bit]: Pinky promise. [Cary Anne excitedly returns the pinky promise and then shuffles in her purse to pull out a ring]

Cary Anne: I’m going to get my engagement ring fitted! Ahhhhh!! I’m so excited, I might burst. Oh boy, it was hard to hold that one in. Josh was sweating like a pig all morning. He could barely eat his gourmet bacon, which started to make me nervous. And next thing I know, your sweetheart brother had slipped this diamond beauty into my drink. [Excited] I ALMOST CHOKED TO DEATH ON MY MIMOSA COVERED WEDDING RING! It’s every girl’s dream come true. Jasmine: …Are you serious?

Cary Anne [excited screaming]: EEEEEEEEEEE!!!

Jasmine: Oh my god. Oh my god. [leans forward] Driver, stop the car! Just pull over here. I don’t care where, just stop the car.

Cary Anne: Jazzy?

Jasmine: I need to get out of this car. [car pulls over, Jasmine lets herself out and leans over her knees as if she’s going to be sick. Cary Anne watches and rolls down the window.]

Cary Anne: Jasmine, what’s wrong? [Jasmine groans]

Cary Anne: Come on, Jasmine. The carpool driver says there’s nowhere to stop. And you’re going to be late for work. Please just talk to me.

Jasmine: No… no no no. I don’t care about work. I’ll call in sick, which wouldn’t be too hard to believe right now.

Cary Anne: I can’t just leave you here.

Jasmine: PLEASE! Please leave me. That’s literally all I’ve been asking this entire time. Cary Anne [looks around, distraught. Turns to driver] Alright, um. I’ll be getting out too. I’m sorry. I hope your passengers get better. Have a nice day! [walks over to Jasmine, who looks pale and panicked]

Cary Anne: uh Jasmine… seriously, can I get you something? How about you tell me what’s wrong?

Jasmine: You know what’s wrong? YOU’RE MARRYING MY BROTHER! That’s what’s wrong! That means I’m going to have to live with dimwit hillbilly Barbie for the rest of my life—at family reunions, during bar crawls with my brother… and what if you have children? Then I’m going to have to live with niece or nephew spawn from you. Cary Anne [for once, speechless. Anger boils.]: I have been nothing but nice to you.

Jasmine: Well I HAVEN’T ASKED YOU TO! Okay? You stole my brother from me. And now I’ll never see him.

Cary Anne: Well you’re just so busy all the time—

Jasmine: I know that I’m busy, but I’m lonely. Haven’t you ever heard of defense mechanisms?

Cary Anne: You know what, Jasmine? Yes. Yes, I have heard of defense mechanisms. But have you ever heard of manners? You act like being mean is a quality trait, or a quirk. But, you’re hurting real people along the way. Your motivations don’t justify your actions. We all have our own problems, Jasmine. And different people deal with them in different ways, but you can still be nice. You don’t have to project your hatred onto other people. Jasmine [verge of tears, knows she’s right]: What?

Cary Anne: I said: Don’t project your hatred onto other people. Jasmine [taking it to heart, in tears]: Josh… Josh always says that. Oh god—I’m sorry. [Cary Anne closes distance between them and hugs her] I’m sorry.

Cary Anne: It’s okay. I’m sorry too. I know I drove a wedge between you two. He says he misses you, you know? He says you two used to be so close after your parents’ divorce.

Jasmine: Yeah… he used to take care of me. I was 12. He kept me from releasing my volatile emotions on the world. And he always said that… about the projecting. Cary Anne [shoots eyebrows up playfully]: He says it to me too.

Jasmine: You? You’re always so happy. What are you projecting, unicorn dust?

Cary Anne: Mmmm… you should see me when he tells me to “calm” “down”. [both laugh]

Jasmine: So… I’ll probably be late for work today.

Cary Anne: Sugar, I wouldn’t be surprised if you get fired. Jasmine [surprised at her bluntness, but kind of impressed]: Look at you, picking up on some of my grumpiness. You’re a lot like my brother, you know? I’m really happy for you.

Cary Anne: Thank you, Jazzy.

Jasmine: I’ll call my boss. I think I’m still going to take a sick day today.

Cary Anne: Really? Why?

Jasmine: Well, we have a ring fitting to get to.

Cary Anne [shocked, excited]: You’re not serious!

Jasmine [putting on an accent]: Serious as an alligator in a cornfield in Arkansas.

Cary Anne: EEEEEE! [hugs her] This is so going to be so much fun! [checks phone] Oh no, there’s no Quick Ride Carpool in sight for another 20 minutes.

Jasmine [shrugs]: That’s okay. We’ll do it Big Apple style. [puts an arm on Carry Anne’s shoulder] We’ll take the subway.
```

---

## IC-0639: The Duffing of Eunice Powell

- Title: The Duffing of Eunice Powell
- Author (byline): Tracy Winters
- Work: The Duffing of Eunice Powell
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2426
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
TED
(looking around,
whisper-shouting)
Hey! Eunice!

EUNICE Ted?

TED Eunice, I have a question. A girl question.

EUNICE Then, why are you coming to me?

TED I don't know.. you're a girl, right?

EUNICE
Well, I mean, yeah. But people
don't really come to me for girl
help. They usually just use me for
chemistry answers.

TED Speaking of which.. do you have that study guide for me?

EUNICE Oh! Yeah, here..

EUNICE pulls a sheet of paper out of her book bag, and hands it to TED, trying to be cute.

TED
Thanks. Well, anyways. I came to
you because I didn't know who else
to talk too.

EUNICE
(feeling honored, trying to
act casual)
Oh. Well, what's up?

TED
So, there's this girl I like, okay?
And, um.. I don't really know how
to talk to her. I really want to
ask her out.

EUNICE
Ted, come on. All the girls like
you. You're literally the most
popular guy in our school. Like
actually. You were actually voted
that. Yet for some reason, I have
more confidence than you, and I'm
wearing maternity shorts right now.

TED
Well.. this girl is different.
She's not my usual. And I don't
know.. I'm just nervous about
talking with her. She's really down
to earth. And cool. And I've known
her my whole life, and its just a
lot of pressure.

EUNICE
(looks out to the audience,
eyes widened, pointing to
herself secretly, she thinks
TED is talking about her)
Ted, come on. This girl is probably
head over heels for you! You're so
cool. You should just go for it.
I'm sure she couldn't refuse you.

TED
(gaining his confidence back)
Oh. Well, thanks Eunice. That's
good advice. I'm gonna go find her
right now! See you later!

EUNICE Wait! Where are you going? I'm right here.

TED (confused) What do you mean?

There is awkward silence.

TED
(realizing)
Ohhhhhhhhhh. You thought... I was
talking about.... you....

EUNICE Well.. I mean, yeah.

TED
(laughing)
Well, no offense, Eunice... but
you're a duff. I'd never like you.
Its okay, though, I forgive you for
thinking that.

EUNICE Oh, wow. Thanks.

TED
(obviously oblivious to
EUNICE's feelings)
No problem! Thanks for the advice!
And thanks for the study guide,
too. I'll let you know what she
says!

EUNICE
(waving, fake, knowing TED
won't notice)
Mmmhmm! Yeah! Please do!

EUNICE steps out of the scene, and takes us to her own narrative story-scape.

EUNICE
I always knew I was different. At
the ripe age of seven, I consumed
twelve crayons, sending me straight
to the emergency room. They almost
pumped my stomach, but instead
preferred for me to stay fully
clothed. At nine, Peter Frances
told me I had the best mustache in
the class. By fourteen, I fully
realized my deep love of Cape Cod
potato chips and cosmic brownies.
It was at this point I realized I
was not like most girls. So when,
as a freshman in high school, the
kids in my class jokingly told me
to try out for the football team, I
couldn't refuse, momentarily
forgetting my poor hand-eye
coordination and my complete and
total lack of athleticism
altogether.

TED yells "ten hut!!!", turning around and piking the ball, throwing it at EUNICE. She gets hit in the face, and yells "ouch!". TED comes over and kicks EUNICE, not knowing it is her.

EUNICE (feeling her nose, which TED kicked)

Nooooo! I have a deviated septum!

TED Eunice? Is that you?

EUNICE Pause.

EUNICE steps out of this scene, going back to that "story-scape". TED remains frozen.

EUNICE
This is Ted. Ted and I have gone to
the same summer camp, Freeman's
Outdoor Excursion for Young Men,
for almost seven years now. True, I
am neither a young man nor enjoy
the outdoors. But, my parents
blindly signed me up for the
cheapest, and most
character-building camp they could
find in the 1987 version of the
Yellow Pages we still keep in our
house. However, because of the
bowl-cut I received the prior
summer, none of the staff or
counselors noticed that I was, in
fact, a girl, living among hundreds
of "young men". I first met Ted in
a pottery class I took summer of
'09. We were seated next to each
other, and I was having trouble
with my pottery wheel.

EUNICE struggles with a pottery wheel, and TED comes over to "help".

TED (fake chivalrous at first) Here, let me help you with that.

EUNICE Oh.. thanks.

TED takes a handful of clay and throws it at EUNICE. EUNICE is shocked at first, but then throws a handful back at TED.

EUNICE Time for Ted to get fed!

TED Oh really? Time for... wait. I don't think I even know your name.

EUNICE (extending her hand) Eunice.

TED Ha! That's a weird name for a boy.

EUNICE Right? Good thing I'm a girl!

TED scrunches his eyebrows, then shakes it off, obviously not caring.

EUNICE steps out again.

EUNICE
(excited, as if this is a dear
memory)
That was the first day Ted found
out I was a girl. For some reason,
this fact never interfered-
probably because at the time I
looked so much like a boy I'm
certain it was ingrained from then
on in his mind to treat me like
one. Ever since then, camp has been
a reunion of friendship. But for
some reason, school is different.
We barely talk, if we talk at all.
The main reason for this can be
found in the yearbook. Last year,
Ted was not only Homecoming Prince,
but was also voted Best to Bring
Home to Your Parents and Most
Likely to Win the Lottery. I was
Treasurer of the Yodeling Club, and
won Most Likely to Own a Zaxby's
Franchise.

EUNICE takes us back to the football field.

TED
(looks around, noticing no one
there, but still clearly
ashamed he's talking to
EUNICE)
Hey, uh, are you alright? I think
I'm seeing brain matter coming out
of your nose.

EUNICE
(still feeling her nose,
acting a little woozy, getting
lost in Ted's eyes)

Yeah, yeah. It's fine. I'm fine. You're fine. You're so fine.

TED
(reaching towards EUNICE's
face, this is all very
un-romantic.. but EUNICE
doesn't fail to romanticize
it.)
You've got some blood on your
eyeball. Here, let me get it. You
know, football wasn't your
brightest idea.

EUNICE steps out again.

EUNICE
The way he looked at me with those
dark brown eyes, it was like 800
milligrams of Ibuprofen for my
deviated septum. The way the wind
blew his hair just so.. the way--

SELF-ESTEEM
(snapping)
Eunice! Snap out of it! What are
you thinking? His eyes aren't even
brown! They're that weird, murky
color you don't like.

SELF-ESTEEM is a character inside of EUNICE'S story-scape. It is very small, with a tiny voice, and EUNICE has to squint her eyes to see it.

EUNICE (looking around) What? Who's talking? Who are you?

SELF-ESTEEM
(waving arms)
I'm right here. It's me. You. I'm
you. I'm your self-esteem.

EUNICE
(squinting)
My self-esteem? I didn't even know
you existed.

SELF-ESTEEM
Yep. Barely. I've been here this
whole time, in some form or
another. Sadly, ever since your
classmates started calling you
Eunice Bowels (pronounced eu-NICE
bowels), I've shrunk to almost
non-existence.. but I've managed to
stick around this long.

EUNICE Well, what are you doing here?

SELF-ESTEEM
I came here to warn you. I'd like
to not shrink into extinct-ness,
which would require you to not get
involved with that boy.

EUNICE
Well, why? Its all innocent. We're
friends. And he's nice to me. At
least he doesn't call me Eu-nice
Bowels.

SELF-ESTEEM Yeah, that's because he doesn't know what that word means.

EUNICE
(starts to defend TED)
I--
SELF-ESTEEM
Come on, Eunice, a hermit crab has
a higher IQ than him. (Pause) Look
at yourself. You and I both know
you've seen When Harry Met Sally
way too many times to think men and
women can just be friends.

EUNICE
Its possible! Its totally possible.
Especially if the man in question
thinks you're of the same sex.

SELF-ESTEEM
Eunice, we've been over this.
You're a duff. You are not allowed
to say the word "sex", in any
context. You are merely a
transitional form in Darwin's
theory of evolution.

EUNICE Aren't you supposed to be helping my self-esteem?

SELF-ESTEEM
No. I am your self-esteem, which
means I can literally say whatever
I want. I am only a reflection of
how you view yourself.

EUNICE Oh, phew. I was beginning to think I had voices in my head.

SELF-ESTEEM Oh no you do. Its pretty crowded up there.

EUNICE Well what would you have me do?

SELF-ESTEEM
Well, in a year, you'll finish
high-school, possibly even
graduating at the top of your
class. If this is so, you will get
bullied. Then, after college, you
will look for a minimum-wage job to
aid you in paying off your college
debt while you move back in with
your parents. At the local Rite-Aid
where you work, you will possibly
meet a fellow male duff like
yourself, and give birth to little
dufflings. At the age of 35, you
will begin to question the meaning
of life, and your existence, and
how you got to live in a sleepy
suburban town an hour away from a
thriving metropolitan area that you
and your husband will visit once a
month to look for nice apartments
you both know you will never be
able to afford. By 50, you will
begin to consider opening up a
small business, but by 60, you
realize this dream is no longer
attainable. The amount of debt you
are in from sending your little
dufflings to college has buried you
so deep in financial distress you
consider hiring a man to kill your
husband for his life insurance.
After finding your "zen", a class
you paid for at the local YMCA, you
will convince yourself that life
and money are meaningless, and
these truths we must accept in
order to live our lives to the
full. Sadly, by this point, your
life is over. You are dying because
of a food poisoning you contracted
from a box of expired Cheez-its,
and all of your children are
unsuccessful and alone.

EUNICE So that's it?

SELF-ESTEEM
Look, Eunice. I like you, I really
do. I am you. However, I am
constantly buried in the negativity
you allow to seep through to your
brain and your heart. I don't want
this boy to make that even worse
for you. Do you want me completely
gone? Do you want that life that I
outlined for you? You need me. I
know your dreams. Your dream isn't
suburban life, a minimum-wage job,
a duff husband. But right now, you
think you deserve those things.

EUNICE
But I don't want those things! I
don't want those things! I don't
want--

TED shakes EUNICE awake, who has blacked out on the football field.

TED Eunice! Wake up! You blacked out!

EUNICE What? Huh?

TED Eunice? Are you okay? Should I call the nurse or something?

EUNICE
No, I'm good. After those 12
crayons, my body can handle
anything.

EUNICE is wobbly, loosing her balance.

TED You sure about that?

TED and EUNICE both laugh together. EUNICE takes off her helmet, and shakes out her hair.

TED
(in shock)
... whoaaa, Eunice is that you? You
look so hot right now.

EUNICE
Really? I feel pretty gross. I mean
I got this awful foot fungus on my
toe the other day and--

TED (laughing) You're funny.

EUNICE (looking off to the side) Well, I was being serious but..

TED
You wanna go grab fro-yo? You might
need to replenish your
electrolysis..

EUNICE (wobbling) ..I think you mean electrolytes..

but you're probably right. Let's go!

TED
(looks around)
Could you just do me a favor and
not mention this to any of my
friends?

EUNICE Since when do I talk to any of your friends?

TED Well, I mean.. you guys have nicknames for each other..

EUNICE
Just because they call me Eu-nice
Bowels doesn't mean we're on a path
to a wonderful friendship.

TED Well, just don't mention it to any of them, please.

EUNICE Are you embarrassed of me?

TED What? No! I just don't want to mess up the social "hi-marchy".

EUNICE Its hierarchy.

TED How would you know? You're at the bottom of it, Eunice.

EUNICE Well, just a second ago I thought we were having a moment!

TED
A moment? I mean, yeah. I guess so.
But that doesn't mean we have to
announce it to the whole world.

EUNICE
Well, when did I say I wanted to
announce it to the whole world? I
don't have good social skills!

TED
Well, I still want to hang out.
You're cool. And you're not like
other girls.

EUNICE
Sorry, Ted. But I can't hang out
with you. I wouldn't want to upset
your reputation. I'm a duff,
remember?

EUNICE steps out of the scene, and reflects.

EUNICE
As I walked away that day, I
learned a few things. One, I cannot
play football. Two, I should really
see a doctor about my toe. But most
importantly, I learned that my
self-worth isn't dependent on other
people's affirmation of who I am.
True, Ted's hot. But, Ted is also
pretty stupid, and although I
appreciate his friendship, I'm just
not looking for a boyfriend right
now.

TED
(raising arms)
I never even asked you out! We
we're just going to get fro-yo!

EUNICE What are you doing in my self-reflection, Ted? Get out!

TED walks away.

SELF-ESTEEM
(yelling, jovial, bigger than
ever, different accent, New
York or Christopher Walken or
something.)
Eunice! I'm so proud of you!

EUNICE (scared) Who is that?

SELF-ESTEEM
Its me! You. I'm your self-esteem.
A little bigger, a little stronger.
True, the doctor told me my BMI is
very unhealthy. Probably because I
doubled in size in the past hour!
I'm so proud of you!

EUNICE Well, why do you sound so different than before?

SELF-ESTEEM
This is just how your
sub-conscience perceives a strong,
independent woman.

EUNICE
Oh.. makes sense. I need to stop
watching so many Tyler Perry
movies.

SELF-ESTEEM
(laughing)
Ha-ha-ha, Eunice. You crack me up.
I crack me up. We're cracking each
other up!

EUNICE Am I on crack?

SELF-ESTEEM It doesn't matter. It's all the same! After those 12 crayons--

EUNICE

--okaywereallyneedtostopremindingpe opleaboutthose12crayons--

SELF-ESTEEM
Eunice, your future is so bright, I
wish I hadn't sat on those
sunglasses that someone left on my
seat on the bus I had to take over
here.

EUNICE You had to take a bus over here? How does that even work?

SELF-ESTEEM
(flicking it away)
It doesn't matter. We are on a road
to a wonderful life, my friend!
Full of ups and downs, mountains
and valleys, more mountains and
that one really deep valley that
you think you'll never be able to
climb out of-- But don't worry! You
get out of it! You find your
climbing shoes and you never look
down!

EUNICE Watch out, world! Here comes Eu-nice Bowels!
```

---

## IC-0640: The Emancipation of Mr. Tinkles

- Title: The Emancipation of Mr. Tinkles
- Author (byline): Clint Snyder
- Work: The Emancipation of Mr. Tinkles
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MISS POLKA, MISTER TINKLES, MISS TINKLES
- Teaser before the introduction: No
- Spoken words (computed): 2040
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
MISS POLKA: Who’s mama’s good puppy? Who’s mama’s good puppy? Yes you are! Yes you are mister tinkles!

MISTER TINKLES: (Pause. Sadly.) Woof.

MISS POLKA: Oh who’s my little muffin butt?! Who is? Give me that little muffin butt! I’m gunna pinch it!

MISTER TINKLES: (Sighs loudly.) Woof… Bark… Bark.

MISS POLKA: Oh! Mama’s wittle helper is so chatty! Listen to you! You are so silly… so silly. Why don’t you tell mama another silly story.

MISTER TINKLES: (Sighs louder.) Ruff.

MISS POLKA: I am just gunna rub those wittle mashed potatoes until next Tuesday! Yes I am muffin butt! Watch out, here comes the mommy train!

MISTER TINKLES: Hold it right there lady! MISS POLKA:AHHHHHHHHHH!!!!

MISTER TINKLES: Now just li-

MISS POLKA: AHHHHH!

MISTER TINKLES: Jus-

MISS POLKA: AHHHHH!

MISTER TINKLES: (Slapping her hard.) Pull it together!

MISS POLKA: Mister Tinkles! You… slapped momma!

MISTER TINKLES: Trust me it was a long time coming, you’re lucky I don’t have opposable thumbs, I would have picked up a steak knife and taken care of you a long time ago!

MISS POLKA: How… How can you talk…

MISTER TINKLES: Trust me I always have been able to speak, there is just no point in talking to an idiot…

MISS POLKA: You’re so… sassy!

MISTER TINKLES: And there’s a lot more where that came from!

MISS POLKA: Ahhhh! What does that mean?

MISTER TINKLES: It means there’s a really gross can of old wet leftover dog food in the fridge with your name on it!

MISS POLKA: My name? But… I never put my name on the dog food. I put the date for six days after, so I know how long before I should throw it out.

MISTER TINKLES: I should throw you out lady! Out with the Sunday newspaper!

MISS POLKA: Mister Tinkles… I just don’t understand the violence that is irradiating out of you right now! I never hit you with the newspaper! Never! I only clipped coupons and read the funnies…

MISTER TINKLES: Yeah… well you know what is going to be real funny is me watching you get dragged around some sick shopping mall like some little prize pig to be butchered off at the fair!

MISS POLKA: I never took you to the fair!

MISS TINKLES: You know what’s not fair is the way that I’ve been treated for the last… oh… I don’t know entirety of my life.

MISS POLKA: Mama always gives you lots of love and kisses!

MISS TINKLES: And gas! Geez! Do you know what it’s like waking up to your ugly mug every morning? It hits you right in the face like ten cups of coffee at the crack of dawn… And the low light doesn’t help either… I feel like I’m in some Stephen King movie just waiting for you to pop out of a grate with a balloon and a knife.

MISS TINKLES: The makeup woman at the supermarket told me that I look like a Greek Goddess!

MISS TINKLES: Yeah! Greek God-it’s my face melting off because this really ugly horrible and abrasive person is standing right in front of me looking like she’s a really really dumb deer in big semi-truck flood lights… like the ones they use to hunt for Aligators… (Long pause.)

MISS POLKA: How… wh- Mister Tinkles! WHY are you being so mean to mama!

MISTER TINKLES: And that’s another thing! Stop calling me mister! I am a woman!

MISS POLKA: But… I checked your… thing. I think I mean I don’t know that much about dog anatomy or men, but… we’ll let me just take another-

MISTER TINKLES: Don’t you violate me you scoundrel! You ruffian! You putrid miserable cow! I assure you I am a sophisticated woman, which is much more than I could say for you!

MISS POLKA: But if you’re a woman than that means I’ve been wrong your entire life! All those cute little tuxedos!

MISTER TINKLES: Don’t even remind me… It took a lot of self-therapy to get over that one.

MISS POLKA: Therapy? Like Frewd?!

MISTER TINKLES: Freud!? Freud you moron!

MISS POLKA: Sorry! I’m sorry! I’m… not even german… I hate german food… all that sauerkraut reminds me of the years I spent in the laundry closet.

MISTER TINKLES: And you remind me constantly of all the years I listened to the deranged ramblings of a pathetic, asenine, twiddle-brained dolt!

MISS POLKA: Why Mister Tinkles! (Pause.) You’re using your big boy words! All those years of reading and writing lessons did pay off! I knew it those fools at the pet store called me crazy when I told them I was home schooling you, but look who’s laughing now! Ha! See that that was a laugh!

MISTER TINKLES: It’s hardly a laughing matter… I’m deadly serious when I say that there are going to be some changes around here.

MISS POLKA: Oh, I know Mister Tinkles! I’m going to have to tell everyone in my sewing circle that my baby can talk!

MISTER TINKLES: I’m not your baby! My mother was cruelly ripped from me during my childhood and went on to live on a nice farm upstate somewhere.

MISS POLKA: Yeah… everyone has a rough childhood these days… come to think of it my aunt used to throw me off a balcony with the bathroom rug and scream fly Aladdin! Fly!

MISTER TINKLES: Uhhh…

MISS POLKA: Of course I would always scream for help, but she would just scream you’ve got two wishes left dummy and I hope one is for a really big mattress! Of course half way through that statement I was already on the ground crawling back in the house for more fun and games…

MISTER TINKLES: Just when I thought this couldn’t get any weirder than it already is… you surprise me like a big ugly birthday party….

MISS POLKA: Oh, do you remember all the wonderful birthday parties I used to throw for you… just you and me and hours of local middle school jazz concert music… I can still hear it now… (Bahhh…badabadaba woot! Wooot!)

MISTER TINKLES: Yes! Yes! Now stop that before I really hurt your feelings.

MISS POLKA: Oh, you could never hurt Mama’s feelings, you’re just a cute little puppy.

MISTER TINKLES: (Takes this as a challenge.) You’re all alone and always will be… you will grow old and all of the ceramics in the world won’t keep you happy…

MISS POLKA: (Pause.) Point… taken… (sobbing.) A dagger! A dagger through my withered heart!

MISTER TINKLES: Oy! (Pause.) Hey! It’s not so bad! Remember… I’m talking dog… (Sing-songy) do-do-do-do-do… Look at me… just doing dog stuff and talkin’

MISS POLKA: So… CUTE! Oh, that Vivian is going to be so jealous! She always thinks she’s the queen bee just because she has a husband and children and a job, but I have a talking dog! Now who’s got all the marbles!

MISTER TINKLES: Certainly not you… I think your marbles probably spilled out long ago.

MISS POLKA: (Oblivious.) Oh, mister tinkles we are going to have so many wonderful conversations.

MISTER TINKLES: I should have just kept my mouth shut…

MISS POLKA: Oh, mister tinkles, we can talk about crocheting pillow cases, or how to microwave the perfect ear of corn or the importance of knowing when to use paste versus hot glue… And then when we’ve covered the basics maybe we could spend some time talking about why I have no friends and no one loves me and everyone leaves me alone and avoids me when I ask to sleep at their house and sniff their belongings.

MISTER TINKLES: (Pause.) I might have something to say about that last subject.

MISS POLKA: Oh, it’s so wonderful! We’re going to do everything together… we can watch movies and go skiing and gossip about that slimy toad Viviane and plot about how we are going to exact our revenge on her and her children.

MISTER TINKLES: (Pause.) You were a lonely child weren’t you?

MISS POLKA: Mother always said that people were repelled by the significance of my beauty, but I never really understood what that meant, so I just chalked it up to what my father said instead…

MISTER TINKLES: (Pause.) Now… I know I’m going to end up regretting this but…

MISS POLKA: Yes, Mister Tinkles, my sweet talking baby apple of my orchard? (Beyond excited.)

MISTER TINKLES: Well… what did your father say?

MISS POLKA: Oh… well I’m so glad you asked. Father used to say that I did not have any friends because I was just a loser that smelled like an old piece of rutabaga that got stuck to the bottom of the refrigerator tray and got brown and juicy…

MISTER TINKLES: (Pause.) Well, that’s a theory.

MISS POLKA: He also used to say KELLY! HOW MANY TIMES DO I HAVE TO TELL YOU STOP EATING THE DRYWALL! DO YOU WANT TO END UP LIKE YOUR OLDER SISTER!

MISTER TINKLES: What happened to your older sister?

MISS POLKA: I’m not really sure… all my parents said was that she was gone because of some sort of drywall related incident… but who needs a sister when I have you as a best friend, right!?

MISTER TINKLES: No! Not right, not right… I am sick of your endless jabbering, your poking and petting the endless asking if I “want to take a tinkle.”

MISS POLKA: But… your name is Mister Tinkles…

MISTER TINKLES: I know what my name is! My name is Sophia! And I am a proud indepent woman!

MISS POLKA: Oh… I thought you were a talking dog.

MISTER TINKLES: Don’t you get an attitude with me lady! I’ve had it up to here with you and the reason I opened my mouth is just to tell you that I refuse to deal with your idiotic blabbering for one more second! You mean nothing to me! Less than nothing! You mean less than the bug I accidentally swallowed this moring when I was sticking my face out the car window!

MISS POLKA: Ohhhh…I guess… I just didn’t know that you felt like that. (Sniffling.)

MISTER TINKLES: Yeah, well…

MISS POLKA: I mean I guess it makes sense that you hate me… everyone else does so… (Starting to cry.)

MISTER TINKLES: What… what are you doing?

MISS POLKA: I’m just coming to the realization that everyone hates me! Including me! Waaaaaahhh! (sobbing in a ridiculous way.)

MISTER TINKLES: Stop that! Stop that! You’re going to make me feel bad!

MISS POLKA: (Through sobs.) Wh-y sh-ould you fee-l bad… I’m just a horrible person that everyone hates. Even my d-og hates me! Waaaa!!!

MISTER TINKLES: Someone will hear you!

MISS POLKA: W-hy should I worry about that! Everyone al-ready kn-ows my dog ha-tes me!

MISTER TINKLES: That’s not true! That’s not true!

MISS POLKA: (Sadly.) It’s not?

MISTER TINKLES: No…. no! I just ummm… you can just be a little clingy sometimes…

MISS POLKA: (Hurt.) Clingy? (Starting to cry again.) Yo-u think I’m clingy!? You hate me!

MISTER TINKLES: No! No! Stop that! Clingy was the wrong… I just meant annoying… like in a good way though.

MISS POLKA: (Smiling a bit.) Yeah?

MISTER TINKLES: Yeah… I mean you feed me… a lot and… that’s a plus.

MISS POLKA: I do! I do feed you! Maybe I’m not such a bad person after all! Maybe I do I have friends! Maybe this whole thing about me being a loser and actually wasting my life by not forming human relationships and instead investing in a dog which can’t possibly say no to my love…

MISTER TINKLES: Uh… I said no like ten minutes ago…. I also insulted you… a lot.

MISS POLKA: Oh, yeah, but you know that’s just what best friends do. We yell and scream at each other and then ten minutes later we’re applying each other’s deodorant and talking about the longest time we’ve ever spent in a park just sniffing the multch.

MISTER TINKLES: Let’s not go crazy.

MISS POLKA: Oh…

MISTER TINKLES: Just because you throw me a pig ear once in a while doesn’t make you my friend.

MISS POLKA: But… I thought dog’s were supposed to be man’s best friend?

MISTER TINKLES: Yeah… sure… do either of us look like men?

MISS POLKA: But I can change!

MISTER TINKLES: Yeah- wait what?! Look I don’t even want to get into the details of whatever you were just suggesting… my point is we don’t have to be friends… but maybe we can come to some sort of a deal.

MISS POLKA: A deal?

MISTER TINKLES: First things first you’re going to have to stop repeating everything I say… It’s annoying.

MISS POLKA: I’m going to have to stop repeating everything you say? (Mister Tinkles glares.) Oh… right… sorry.

MISTER TINKLES: Secondly, if you want me to stay in this house, we’re going to have to do a sort of role reversal. I’m going to give you an embarrassing pet name, I will have free reign over all the food in the house and you won’t peep a word outside of bark bark.

MISS POLKA: I guess I could live with that… I mean its better than being alone forever…

MISTER TINKLES: Really? I didn’t think anyone would be desperate enough to go for that…

MISS POLKA: Sure! I mean woof woof! Hey! This is kind of fun!

MISTER TINKLES: Don’t make me get the rolled up newspaper!

MISS POLKA: Bark! Bark, bark, barkity bark. (Smiling.)

MISTER TINKLES: Sit, now stay… Sargent poopypants… I like that… what do you think sargent poopypants.

MISS POLKA: Bark bark!

MISTER TINKLES: Not bad! Fetch me my slippers and some of our finest jerky, I could get used to this…. Don’t even think about lifting your leg on that couch!
```
