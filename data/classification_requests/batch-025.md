# Classification request: batch 25 of 63 (40 records, IC-0961 to IC-1000)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-025-reply.json`.

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

## IC-0961: Your Mother’s Butt

- Title: Your Mother’s Butt
- Author (byline): Alan Ball
- Work: Five One Acts Plays by Alan Ball
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CLIENT, PSYCHOLOGIST
- Teaser before the introduction: No
- Spoken words (computed): 1413
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alan Ball
Book: Five One Acts Plays by Alan Ball
ISBN: 0822213680
Publisher: Dramatists Play Service, Inc.
Date(Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Without fail, just about anything that goes wrong in a child's life is the mother's fault.

ACTOR: What a good idea it would be to have child psychiatry a regular part of annual well child doctor's visits. After the vaccinations and the eye-chart test, the child could lie down on a chaise and spill for the doc all the ills he feels mom has inflicted on him.

ACTRESS: “My mom won't leave the hall light on at night and the noises outside my window scare me.”

ACTOR: We could take care of the problem right there at age 5 and avoid having the same conversation with a therapist 30 years later and deciding that mom's hall light failings are to blame for the adult child's foibles.

ACTRESS: In this selection our client seeks psychiatric attention for his increasing dissatisfaction with life and as is typical . . . .

ACTOR: His therapist attempts to trace his many idiosyncrasies directly to what she affectionately calls . . .

TOGETHER: Your Mother’s Butt by Alan Ball.
```

### Performance text (classify this)

```text
CLIENT: My life is, like, so mundane. The days come, the days go. I keep waiting, waiting, waiting, but for what? I go to work, I eat, I work out. I watch television. I'm not really depressed. Well, yeah, I guess I am depressed. I'm lonely. I'm easily irritated. But it's not the kind of overwhelming depression that feels like it's ripping me apart. It's more of a . . . blandness, an overall numbness. . . like every fiber of my being has been sucked dry of any coherent reason to exist. (Pause.) Nothing matters.

PSYCHOLOGIST: Nothing?

CLIENT: No. (Pause. The CLIENT cries.) I have- (It is too painful for him to say; takes a moment, then tries again.) I have this sweater. .

PSYCHOLOGIST: A sweater?

CLIENT: It's really nice. It's this old sweater, I think it belonged to my brother. It's just this black V-neck sweater, wool, but it's faded and soft and it fits me really well, it accentuates my shoulders, but, like, in a subtle way, and when I wear it, I feel really sexy.

PSYCHOLOGIST: You have every right to find joy in a sweater.

CLIENT: I do, that's the weird part, it's like the only thing in my life I get excited about. Sometimes I put it on just to vvalk around in it, and then sometimes I forget that I've done laundry and I go to pick out something to wear, and there it is, all clean and soft and faded just a little bit more, all folded up, and it's, like, primal, like, maybe even religious. (Pause.)

PSYCHOLOGIST: How are you feeling?

CLIENT: How do you think I'm feeling? The only significant relationship in my life is with a piece of clothing? At best, that's tremendously shallow, and at worst, it's sociopathic. I mean, if I was somebody else and I knew me, I would say look, get a life.

PSYCHOLOGIST: I think perhaps you're being a bit hard on yourself.

CLIENT: You're right. God, I am so messed up. I've got to do something about this, I can't be this messed up anymore. What can I do? Tell me what to do. You're the expert.

PSYCHOLOGIST: Well, first, I think we need to take a look at why you are so hard on yourself. (Pause.)

CLIENT: (Sighs.) Okay. (Long pause.)

PSYCHOLOGIST: How are you feeling?

CLIENT: Excited.

PSYCHOLOGIST: Excited?

CLIENT: Yeah. I'm thinking about this pair of shoes I saw yesterday.

PSYCHOLOGIST: Shoes?

CLIENT: Yeah. I've been looking for the perfect pair of black shoes for. . . well, probably for my whole life. You know, a pair of oxfords, just plain, nice leather, not too clunky, but not too Wall Street, either. The kind of shoes you can wear with a suit and look really hip, but you can also wear with blue jeans and look really. . . intelligent.

PSYCHOLOGIST: Intelligent.

CLIENT: But also approachable. And politically correct. With a sense of humor.

PSYCHOLOGIST: Shoes seem to communicate quite a lot for you.

CLIENT: Oh, yeah. Definitely. I think there's two ways to learn a lot about somebody in a short amount of time. One is their refrigerator-not only what they stick on the front of it, but what's in it, too-and the other is their shoes.

PSYCHOLOGIST: (A hunch.) What's in your refrigerator?

CLIENT: Well, nothing right now.

PSYCHOLOGIST: Ah.

CLIENT: These shoes are the greatest shoes-I think.

PSYCHOLOGIST: Let's stay with the image of the empty refrigerator for a moment.

CLIENT: Why?

PSYCHOLOGIST: I have an idea it might be significant.

CLIENT: Okay.

PSYCHOLOGIST: (Taking time, setting mood.) A cold, white, empty box. . . possibly a source of nourishment, but also a potential death trap. (Pause.)

CLIENT: Cool. (Pause.)

PSYCHOLOGIST: Perhaps we should return to the shoes.

CLIENT: Okay. (Pause.) I don't know. They might be the right ones, they might not. They're really expensive. I don't want to spend that much money and have them not be the perfect shoes! (Suddenly angry.) God, why does everything always have to be so hard?

CLIENT: Weird. I just remembered. . .oh, I had this weird dream.

PSYCHOLOGIST: Tell me about it.

CLIENT: I dreamed. . . I dreamed I was in this. . . house, it wasn't my house, but I lived there. And I was in this big room, and I was in this bathtub. This old-fashioned bathtub on pedestals. And I'm wearing clothes. This olive drab cardigan, just over a T-shirt, and these flax-colored, I guess, linen shorts. And then I hear these voices in the hall and in comes my mother. Only she's a younger version of herself, and she's wearing these 1960s hip-huggers, and she has Mary Tyler Moore hair that she's tied a bandanna around, and I think oh, she's trying to be hip, and it's really sort of sad for a moment. . . then she gets in the bathtub with me, only she won't look at me, and then she bends over and. . . she just sticks her butt in my face.

PSYCHOLOGIST: (Scribbling furiously.) This is really good.

CLIENT: And I'm thinking. . . okay. This is kind of weird. . . this is really. . . it's really not quite right. . . it's really. . .

PSYCHOLOGIST: Inappropriate?

CLIENT: It's more than that. . . Oh, God, what is it?

PSYCHOLOGIST: Visualize the dream.You're in the water. . . Is the water warm or cold?

CLIENT: Warm. But not hot.

PSYCHOLOGIST: And she comes in.

CLIENT: Yeah, and she's walking this swingy, hippy kind of walk, and I think oh, God, my mother. I'm so embarrassed.

PSYCHOLOGIST: And she gets in the tub. . .

CLIENT: You can tell she thinks she's really groovy.

PSYCHOLOGIST: Now she's in the water with you. . .

CLIENT: Yeah. And she is wearing the most hideous Barbie, like, flower power outfit and macramé belt.

PSYCHOLOGIST: She's turning around. She's bending . . .

CLIENT: Oh, wait a minute! I just realized something. Oh, wow. (Pause.)

PSYCHOLOGIST: Yes?

CLIENT: It makes such perfect sense, doesn't it.

PSYCHOLOGIST: What does?

CLIENT: I get my bad belt luck from her. It's heredity. (Long pause.)

PSYCHOLOGIST: (Just the slightest bit if tightness.) How are you feeling?

CLIENT: I feel great! If it's hereditary, then I don't have to feel guilty for it. I have no control over it, so it's not my fault. Right?

PSYCHOLOGIST: Well, not exactly, no. One of the underlying assumptions that the therapeutic process is based upon is that you do have control over your life.

CLIENT: No ,thanks. I don't want that kind of responsibility. (Pause.)

PSYCHOLOGIST: I'd like to get back to your mother's butt.

CLIENT: Please. Be my guest.

PSYCHOLOGIST: It's such a strong image, with so many potential implications. It could open many doors. So I'd like to try something a little . . . unorthodox.

CLIENT: Oh, no. You're not going to stick your butt in my face, are you?

PSYCHOLOGIST: No, no. I just want you to close your eyes, and relax. Feel the warm water in the tub. Now try to picture your mother's butt.

CLIENT: Okay.

PSYCHOLOGIST: Do you see it?

CLIENT: Plain as day.

PSYCHOLOGIST: Now speak to it.

CLIENT: I'm sorry?

PSYCHOLOGIST: Speak to your mother's butt.

CLIENT: Oh, right.

PSYCHOLOGIST: Think of it as separate from your mother. As an entity of its own. If you could communicate with it, what would you say?

CLIENT: Get out of my face.

PSYCHOLOGIST: Perhaps it would be helpful if you gave it a name.

CLIENT: What do you mean?

PSYCHOLOGIST: If it had a name, what would it be?

CLIENT: You mean like a person's name?

PSYCHOLOGIST: Possibly.

CLIENT: Like. . . Debbie?

PSYCHOLOGIST: Perhaps.

CLIENT: This is really weird.

PSYCHOLOGIST: Just try speaking to it by name.

CLIENT: Get out of my face, Debbie. Excuse me, Debbie, can you get out of my face? Thank you. Yo, Debbie. Get the heck out of my face.

PSYCHOLOGIST: Maybe you'd like to yell at it.

CLIENT: Sure, why not. (Yells.) Debbie! Get the hell out of my face, you witch! And take that hideous macramé belt with you!

PSYCHOLOGIST: Now become the butt.

CLIENT: What?

PSYCHOLOGIST: If you were the butt, what would you say in response?

CLIENT: Uhm, I'm Debbie the butt, and you better shut up. Stop telling me what to do. This is a free country and I can be wherever I want. If you don't like me being in your face, then you leave.

PSYCHOLOGIST: Now respond as yourself.

CLIENT: You stupid butt. I was here first.

PSYCHOLOGIST: Keep going.

CLIENT: Oh yeah, well. . .

PSYCHOLOGIST: Keep going.

CLIENT: I'm confused. Am I me or am I the butt?

PSYCHOLOGIST: Keep going!

CLIENT: But

PSYCHOLOGIST: Don't turn away from this! We're right on the verge of something!

CLIENT: Um

PSYCHOLOGIST: Don't hold back! Tell that butt how you are feeling!

CLIENT: (Loses it.) God! Shut up! Get out of my face, get out of my bathtub, get out of my life, you butt! I hate you, I hate you, I hate your guts! (He sobs uncontrollably. Long pause.)

PSYCHOLOGIST: How are you feeling now?

CLIENT: I feel like the biggest jerk in the universe. I'm never telling you another dream again. But. . . oh, wow. Wow. This is intense.

PSYCHOLOGIST: What?

CLIENT: Have you ever been hit with, like, this realization, it's, like, something you always knew, but it's the first time you've ever really seen it so clearly? Oh this is so weird, it's like deja vu.

PSYCHOLOGIST: What? (The CLIENT sits up and looks at her.)

CLIENT: (With great resolve.) I don't care how expensive they are, I'm buying those shoes! (Blackout.)
```

---

## IC-0962: Your Obituary is a Dance

- Title: Your Obituary is a Dance
- Author (byline): Bernard Cummings
- Work: Humana Festival 1995: The Complete Plays
- Publisher: Smith & Kraus Publishers
- Publication date as stated: 1995
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NELLA, TOMMY, BOTH
- Teaser before the introduction: No
- Spoken words (computed): 2126
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bernard Cummings
Book: Humana Festival 1995: The Complete Plays
ISBN: 188039992X
Publisher: Smith & Kraus Publishers
Date (Month/Year): 1995
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Writing your own obituary is a lesson in humility. The summary of your existence etched in words that attempt to provide an understanding of who you are,

ACTRESS: Writing your own obituary is not morbid, nor does it hasten death, it’s simply a way to make peace with your passing and to make things easier on your loved ones.

ACTOR: Returning to his Texas hometown, Tommy, a young man dying of AIDS attempts to say goodbye.

ACTRESS: Unable to overcome his own and his family’s prejudices, his pain goes unresolved until he’s reunited with Nella Rae, another outsider who was his childhood friend.

TOGETHER: Your Obituary is a Dance by Bernard Cummings
```

### Performance text (classify this)

```text
NELLA: Tommy? (She crosses to the door) Tommy, is that you?

TOMMY: Un uh ... oh no, Miss Thang ... you gotta be a little more surprised to see me than that. Start acting like you real happy to be seeing me, woman.

NELLA: Wait a minute, Negro. You know damn well I'm happy to be seeing you after all these years! Now, chill and let me create some atmosphere of suspense here. Now shut up and let me start over. (She crosses back to the kitchen table. Pause) Well, knock! (He plays along)

NELLA: Tommy?!

TOMMY: Nella Rae! I'm home!

BOTH: Aaahhh!!!!

NELLA: Look what the wind done blowed in! How you doing, baby?

TOMMY: Better now that I'm laying these tired eyes of mine on you.

NELLA: Lord, chile, it's been forever and a couple of days since I done last laid eyes on you. Not to mention heard from your triflin' self. What's the matter? Whatn't no telephones were you was? Postman didn't come by your house or something?

TOMMY: Girl, don't come for me. You know you been on my mind, and definitely with me in spirit.

NELLA: Spirit! I ain't known no such thing; so, don't you come for me either.

TOMMY: Look, Diva, don't go there. I already done been read once today, and I ain't trying for another one.

NELLA: You musta' stopped by your Mudear's house first?

TOMMY: Simple as that was, yes. She threw me so much shade that I thought I was deep in the heart of the Amazon Jungle. I could just whip my own black *butt* for stopping by there first.

NELLA: Oooooo, sister-girl read you, huh?

TOMMY: And burned down the library!

NELLA: That "holy-hallelujah-amen corner-kneel at the cross" Mu'dear of yours. Chile, please ... you don't have to tell this girl no more.

TOMMY: Girl, you still a mess. You just as country as a dozen eggs sitting on top of a bale of hay.

NELLA: You damn skippin', And proud of it. So, cock-a-doodle doo!

TOMMY: Where's your man at, Nella? Thought Otis was too jealous to ever leave you alone.

NELLA: Chile, please. Otis is way down by Galveston roughnecking on some oil rig. Wanted me to pack up and go down there with him. Huh! I told him to g' on down there by hisself and to send me the paycheck come paydays and everything would be just fine.

TOMMY: Well, now, I don't mean to be dippin' all up in ya'll's business and whatnot, but how do you know that Otis ain't doing a little "foot shakin" way down there?

NELLA: What I don't know don't concern me. 'Sides, ain't no ring on this finger. Tommy? (Long pause) Tell your girl how you doing, baby.

TOMMY: That train is pulling into that station, girlfriend. Truth is, when I consider this little ol' life that is mine, I realize that this *stuff* coursing through my veins is par for the course. Nella, I ain't gonna lay up in no hospital bed with tubes and wires coming all out of me. I have no need or desire for that. Understand?

NELLA: Baby, knowing you like I do I truly do understand. That why you home?

TOMMY: Peace to be made. Ghosts to set free. To just see this place where I grew up. To say goodbye, and to finally, finally, let go of it all. Girlfriend, this life has been one tough row to hoe. You know what I mean?

NELLA: Chile, if you told me this was a drama I'd laugh in your face and tell you it was a comedy. Yes, I know what you mean. Being a Black woman in this neck of the woods ain't been no day at the racetrack either.

TOMMY: It's a cryin' shame that I should even think about all these tongues that will be waggin' around here once they find out that ...

NELLA: Oh no no no ... you can stop that noise right there. Chile, please. Self-appointed Righteous Folks love imagining God sitting up somewhere with nothing better to do than to cause folks they don't like misery and grief. Makes 'em feel safe in believing that a God actually exists. Now, baby, look, I can understand you wanting to bury ghosts and everything. But take it from me you don't owe these folks around here a thing. See, most of them talked about me like I had a tail. As you know, I was called every 'fat', 'black', 'nappy headed', 'big nosed', 'African Ju-Ju', name there was when we were growing up ...

TOMMY: ... chile, I remember all that grief ...

NELLA: .. .I know you do. We caught hell, baby. That's why you and I was as tight as we was. But let me say this: Folks had me so wound up with hatred for myself that I became lost. You hear me? Lost. And on top of all that folks still stood righteous, telling me I was gonna' burn in hell. 'Oh yeah,' I said, 'well, your husbands, sons, and brothers gonna' be right down there with me.' Can I get an "amen?"

TOMMY: 'men!

NELLA: But, baby, when the Truth finally shined its light down on me, and I saw just how SWEET my blackness was-SWEET, do you hear me now? ..

TOMMY: ...I hear you ...

NELLA: Otis finally came into my life all them years ago ... you remember ...

TOMMY: ... sho' do ...

NELLA: I thought that he was crazy as hell. But he LOVED me, baby. And I'm still with *him* cause he showed me 'the darker the night, the brighter the day.' See ... my people, my people ... folks used to make fun of my berry-black blackness when I was growing up. And now you can't seem to turn around without Black folks acting like the last dark African on God's green earth. Folks wearing more Kenre cloth and beads than anybody from Africa wears. All of a sudden it's politically fashionable to be what they tortured me about as a child. And all of it because folks NOW talkin' 'bout some "Afro-American" identity and "reclaiming our roots" and whatnot. Makes me want to scream "Everybody knows we from Africa 'cept us!"

TOMMY: You better PREACH, girl!

NELLA: Whatchu' SAY?

TOMMY: I said PREACH!

NELLA: Whatchu' SAY now?

TOMMY: Preach ON!

NELLA: Witness then like you know how to, baby. 'Cause we may be the outcasts of an outcast race, but we dotted the 'I' and crossed the 'T' in 'identity.'

TOMMY: Oooo, you go, girl. You certainly are philosophical this evening. I stopped by the right place.

NELLA: Speaking of stopping by the right place, what on earth possessed you to stop by you Mu'dear's first? I mean, did you think things might've changed or something?

TOMMY: Well, no. 'Cause when she and Papa threw me out of the house all them years back, I was told in no uncertain terms that I had no home there anymore. But, you know, Nella Rae, in some odd way I was hoping that I'd tell Mama that I've got the 'Big A,' that she'd take me into her arms and hold me, tell me she loved me and that everything would be alright. Was I wrong in hoping for that?

NELLA: Un huh ... I see ... well, come here, Jesus. If that ain't about some of the most sentimental crap I done heard in a long time.

TOMMY: Well, it ain't over yet. I'll see her again and next time I'll just speak the Truth ... see what happens ...

NELLA: You KNOW what's gon' happen: Miss sister-girl gon' read you again and send you on your merry way ... with her proslytizing self ... sometimes she makes me just want to slap the taste out of her mouth. Forgive me for saying that, baby.

TOMMY:. (pause) Sad to see the house and to know Papa wasn't there anymore. He died about ... what was it ... five years ago, huh?

NELLA: Yeah, that's about right. I even showed up at the funeral hoping you'd surprise us all and be there.

TOMMY: No. That funeral was the last place I wanted to be ... which brings me to a point. (He opens his duffle bag and takes out a notebook and pen, and sits them on the table.)

NELLA: What's this for?

TOMMY: We gon' write my obituary together ... (Overlap dialogue)

NELLA: •.. aw, hell, Tommy ... un uh ... naw ... we'll have none of this .

TOMMY: now wait a minute, Nella Rae ...

NELLA: ......... here we is having a good time, and me up in here on a roll preaching and all like I done lost my ever-loving mind ...

TOMMY: . . . Nella Rae, hush and let me ...

NELLA: . . .and here you is wanting to bring us all down with something crazy like this. I ain't gonna' do no such thing. I don't like this-no way and no how ...

TOMMY: I don't like okra. But if I was starving I'd thank God for it and eat it. Now you listen to me: I am alive to do this. ALIVE. This way ... we let go. Let go. (Pause) C'mon my fat, black, nappy-headed, and beautiful Waitutsi woman. Me. You. And these words. (He hands her the notebook. Pause) (She finally takes it.)

NELLA: (Pause) Well, don't be lookin' at me. What you wanna say here? (Pause. They look at the paper like it's a foreign object.)

NELLA: Well, we can start by writing that 'He was once a fierce drag queen .. .'

TOMMY: . . . un uh ... don't you come for me. I never did that tired Patti LaBelle, Judy Garland thang. I personified performance art.

NELLA: Chile, please! You couldn't be Judy Garland even if you had Michael Jackson's money and plastic surgeon; and looka' here, I came to Dallas that time you was living there, and I saw that show you did at that cabaret. If that wasn't drag you was doing then I rnust've been blind, cripple and crazy.

TOMMY: Oh, girl, 'bye! I did lot's of confused things in those days 'fore I discovered that that wasn't my cup of tea.

NELLA: Cup?! You had a POT! Chile, who was it you was up there imitating?

TOMMY: .. .lipsynching ...

NELLA: ... whatever ...

TOMMY: . . . Diana Ross!

NELLA: Yea! That was it! And you had the nerve to sing ...

TOMMY: .. .lipsynch .

NELLA: ... whatever some "Sweetest Love Hangover"!

TOMMY: Wasn't that a big ol' mess!

NELLA: You know, I used to love it when we were kids and you'd put on your Mu'dear's stuff and do me a little show.

TOMMY: You reaching waaaayyy back now.

NELLA: Remember that time she caught us up in ya'll's attic? Who was you imitating?

TOMMY: Donna Summer, girl.

NELLA: That's right! That's right! "Toot toot ... ahhhh, beep beep. Bad girls, talkin' bout those bad girls ... "

TOMMY: And the look on Mama's face when she caught us!

NELLA: Yeah! She looked like she didn't know whether to cry, faint, or holler. All she could do was : "Tommy! agh ugh vvv rrr zzz what you doin? Stop that!" Miss sister-girl lost her mind.

TOMMY: Then she ran your little fat *butt* outta' there ...

NELLA: ... un huh ... accusing me of making you do that. As if she hadn't already noticed you was a big ol' sissy. Chile, please ...

TOMMY: Did I ever tell you what happened after that?

NELLA: Naw, you never did.

TOMMY: Well, honey, she whipped me right out of that page-boy wig and them hot pants. Then she said that she just had to tell Papa so that he could put a stop to my foolishness. Well, Papa came into my room that night, mad as hell, and made Mama put that wig and hot pants on me. And some eyeshadow. That's right, eyeshadow. Chile, bye. Funny, Nella Rae, but the one clear thing I remember in that moment was that Mama was putting some ugly dark purple eye shadow on me, and I was thinking that she had very little taste to be putting that dark purple on my chocolate skin. But she was crying and begging Papa not to make her do it. Now, Papa was never a violent man. Just as sweet as he could be. Didn't like me much, but a very sweet man. But he had this look in this eye like, if you don't put it on him and r-a-t now, rat now, I'm gonna slap the taste out of you and this little sissy. Mama wasn't no fool: she put it on me. Then he made me start doing whatever it was I was doing up there in the attic. And, honey, he made that belt talk across my behind. All the while he kept saying that he was beating the deviance out of me. Truth is, I never hated him for that, Nella. I felt sorry for him. (pause) But in a lot of ways that whippin' prepared me well for life: if you think I caught hell from Black folks, white folks are truly another story.

NELLA: ... chile, say no more. (Pause) So, now what do we put in this obituary?

TOMMY: Look, here it is: I have lived. I have learned. I have lost and won. Done cried. Done lied. And, yes, there were times when I witnessed the Truth. But no regrets' cause now I rest. (Pause) The end. (Pause) Funny, but me and Papa will be buried side by side. Someday Mama will join us. And finally death will let us be together like life never could.

NELLA: Amen, baby. (She puts another tape into the jam box. Closes the notebook. Cheryl Lynn's "Got To Be Real" blasts from the speakers.) Let's party, baby. Your obituary is a dance.
```

---

## IC-0963: 3:59 AM

- Title: 3:59 AM
- Author (byline): Marco Ramirez
- Work: Plays for Two, Pgs 532-547
- Publisher: Vintage Books
- Publication date as stated: Mar 2014
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: LAZ, TOGETHER, HECTOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1564
- Already set (do not supply): none

### Source block (context only)

```text
Author: Marco Ramirez
Book: Plays for Two, Pgs 532-547
ISBN: 978-0345804549
Publisher: Vintage Books
Date (Month/Year): Mar 2014
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR PLAYING HECTOR: It's summer in the city, and Laz and Hector are both on the run from something they can't quite name. Maybe the sudden need for speed has something to do with Laz's sister, who took off two weeks ago, or with Hector's wife, who just called from the hospital. Join us for this late-night portrait of two young men tearing up the open road - and themselves. It’s . . .

TOGETHER: 3:59 AM by Marco Ramirez
```

### Performance text (classify this)

```text
LAZ: (Pgs 532-547) (age 19 – speaks to audience) It's like a hundred degrees outside, and
every time I close my eyes I feel the walls closing in on me in my room.
‘Cause it’s just me in there now.
(My sister moved out like two weeks ago
And we don’t know where she is)
Even though it’s just me, I swear to god the place is getting smaller.
And my aunt is coloring her hair,
And my mom is smoking cigarettes in the kitchen,
Screaming how I'm just like my father.
But I just go.
I leave the apartment in my flip-flops and my gym shorts and my Field Day T-shirt
from the sixth grade that still fits me 'cause I was fat
I just go. And even though it’s a hundred degrees outside, I still gotta warm up my
Civic. Keys in ignition. (Pause while engine warms)
And for a minute or two I just listen to that Honda engine put-put in Japanese . . . It
comes to life, and I start driving.
And I don't remember putting my foot to the pedal
Or first gear . . . Or second gear . . . Or stoplights . . . But I'm gone.
. . . I fly.
And next thing I know I'm down a half a tank of gas
And I look at the clock, and bro,

TOGETHER: It's two o'clock

LAZ: In the morning.

HECTOR: (Late 20s – speaks to audience) And my manager's being a dick.
And not just because all managers are dicks pretty much always,
I mean, tonight he's being like a remarkable dick,
So I wave to him all nice on my way out of my job
And I take out my keys and I take out my cell phone on my way to the car-
I am SO tired . . . SO hungry
And I didn't wanna work a second shift today but my wife's three months pregnant
So that means I'm working a third and a fourth shift if I have to,
I know it's two o'clock in the morning, but I call her anyway just to let her know I'm on my
way,
And she picks up fast like the phone was already in her hand.
And the first thing she says is "How was work."
But she's not asking . . . She's stalling.
And there's this silence. . .
There's this silence but I hear monitors and machines in the background.
And I'm like "What?"
And she tells me she didn't want me to worry.
Three· months pregnant,
She didn't see the point in bothering me at work.

LAZ: But that doesn't even matter --

HECTOR: And that's when she tells me we lost him. And ten minutes later my sleeves are covered with tears and snot.

Twenty minutes later my knuckles are scraped and dented from punching the dashboard. Window's fogged . . . Empty parking lot.

LAZ: (Quiet) It's just me in there now.

HECTOR: And I'm getting calls from the hospital but I can't pick up.

LAZ: (Quiet) . . . Just me.

HECTOR: And this is the point where I realize I've memorized the geography of my Subaru:
(He takes a quick inventory) Dashboard, Turn-signal, Scooby Doo steering wheel.
It was familiar before, but now I got all of it memorized.
And I know I should . . . I know it should be the first thing I do,
But something tells me I can't see her . . . I can't.
Not 'cause of her . . . 'Cause of me.
'Cause I'm just not strong enough.
So I start the car-

LAZ: - And I don't remember putting my foot to the pedal

HECTOR: - I start that car-

LAZ: - I don't remember first gear or second gear

HECTOR: - And I just go-

LAZ: - And I'm not thinking about my sister,
Or the look on her face when she left,
Or how weird it is to sleep in that room,
Or the fact that l prayed
-- Me: the loser of all losers
To make sure she was all right.
And I'm not thinking about how I should call her
Even though my mom told me if I did I'd be a traitor and an
embarrassment to the family
And I'm like "The Family?"

HECTOR: - The seat belt light is still on with this annoying chime thing that goes ding if you don't put it on and I'm normally real safe about everything but not tonight -

LAZ: - And I turn on the radio-

HECTOR: - Tonight I don't -

LAZ: - And it’s the late-night DJs that are like not good enough for regular radio . . .

HECTOR: And the streetlights are getting dimmer

LAZ: - And it's one -

HECTOR: - After another -

LAZ: - After another -

HECTOR: - Streetlights -

LAZ: - And eventually I just settle on static

HECTOR: - I don't even know where I'm going

LAZ: - Static -

HECTOR: - I'm the kinda guy who makes his parents recycle and here I am just eating up gas streetlight after streetlight 'cause driving is just-

LAZ: - Nice with the static all up and every streetlight is like something I never seen before!-

HECTOR: - And for no reason in particular at one point in my driving, In my whatever-I'm-doing, I slam on the brakes, Put it in park. (A beat)

LAZ: And put the car in park.

HECTOR: And I look at my watch and-

LAZ: - It's three fifty-eight AM and I dunno where the hell I am.

HECTOR: But I don't care. (A beat)

LAZ: Wherever it is I've driven, everything looks like

HECTOR: - pitch-black-

LAZ: - Except a thin trail of moonlight tracing over

HECTOR: - A couple buildings in the background – . . . And normally there's someone on the street Even this late, right?

Normally there's at least a cop car or a crackhead But right now there's -

LAZ: - Nothing.

HECTOR: And I hear this stupid put-put sound coming from a car next to me.

LAZ: And in the middle of all the dark I look up and there's this [guy] I never seen before.

HECTOR: And it's just us and our steering wheels.

LAZ: And he looks me in the eyes like we're friends or [something] -

HECTOR: - Cowboys

LAZ: - In the eyes

HECTOR: - Showdown

LAZ: - Like we're friends.

HECTOR: . . . And I rev the engine

LAZ: - Oh yeah?

HECTOR: - And, you have to understand: I've never "revved" the engine before,

LAZ: - Like he's some kinda hot s*** in his Subaru . . . So I do the same-

HECTOR: (building) - And it's just me and this guy I don't know-

LAZ: - And everything is pitch-black except his headlights

HECTOR: - And I have NO idea where we are, We're in some part of the city they don't even put on maps-

LAZ: - Come on-

HECTOR: - And am I really about to race someone?

LAZ: - Come on, yo -

HECTOR: - Ohmygod-

LAZ: - COME ON-

HECTOR: - And I dunno what the hell got into me but I just go-

LAZ: - And I don't even remember putting my foot to the pedal-

HECTOR: - Or first gear

LAZ: - Or second gear

HECTOR: - Or third gear LAZ: - Or fourth-

HECTOR: - Or stoplights-

LAZ: - But it's three fifty-nine AM and we're gone - (building)

HECTOR: - Holy s***- LAZ: - And next thing I know I'm going eighty

HECTOR: - Ninety-

LAZ: - Ninety-five miles an hour down a stretch of road that's empty, that nobody's been on for like a hundred years-

HECTOR: - I fly- LAZ: - Hundred miles an hour, the road curves

HECTOR: - I curve with it-

LAZ: - Hundred-ten he catches up. And at a hundred-twenty I'm about to max out but I don't even care-

HECTOR: - I'm going a hundred-thirty miles an hour like some kind of moron-

LAZ: - HOLY S***-

HECTOR: - THE SPEEDOMETER ISN'T EVEN CLOCKING HOW FAST I'M GOING ANYMORE WHAT THE HELL AM I DOING-

LAZ: - AND I AM NOT THINKING ABOUT MY SISTER-

HECTOR: - AND SUDDENLY ALL THE DARKNESS AROUND US BECOMES LIKE SOMETHING, ELSE-

LAZ: - OUTTA NOWHERE THERE'S MAD STREAKS OF LIGHT JUST STREAMING ACROSS THE WINDSHIELD LIKE LIGHT WAS MADE INTO WATER AND IT'S RAINING BRO-

HECTOR: - IT'S RAlNING LIGHT BUT AT THIS POINT I'M EVEN SCARED TO SLOW DOWN - AND OUTTA NOWHERE THERE ARE THESE-

LAZ: - STARS SCRAPING AGAINST MY WINDSHIELD AND. I MOVE TO PUT THE WIPERS BUT I CAN'T 'CAUSE-

HECTOR: - THERE'S LIKE A G-FORCE HOLDING ME BACK AND I CAN'T MOVE -

LAZ: - LIKE ON A ROLLERCOASTER

HECTOR: - LIKE IN SPACE- AND AT THIS POINT WE'RE NOT EVEN RACING AGAINST EACH OTHER-

LAZ: - AT THIS POINT I'M LOOKIN' THROUGH THE WINDOW AND I COULD SEE THE SIDES OF THIS DUDE'S SUBARU ON FIRE BRO-

HECTOR: - AND THE STEERING WHEEL AND THE SCOOBY DOO COVER AND EVERYTHING START TORATTLE-

LAZ: - AND MY "PUT-PUT" BECOMES LIKE SHAKING-

HECTOR: - AND EVERY HINGE AND EVERY SCREW IN MY CAR FEELS LIKE IT'S ABOUT TO COME APART-

LAZ: - BUT JUST BEFORE IT DOES-

HECTOR: (to himself) - EVERYTHING'S ABOUT TO COME APART-

LAZ: - AAAAGH! -

HECTOR: - WHAT AM I DOING?! (to himself) - GROW UP-

LAZ: - JUST JUST JUST-

HECTOR: - MAN UP!! -

LAZ: - JUST BEFORE LIKE ALL OF IT

HECTOR: - EXPLODES, I HEAR-

LAZ: - NOTHING. (a beat. Silence. Just silence)

HECTOR: And there's this moment. . . This moment of . . .

LAZ: . . . nothing. (a beat. Then softer . . .)

HECTOR: And through the flames and the light and the dark and the shaking and the speed I see-

LAZ: - Pitch-black. (silence)

HECTOR: And when I wake up, my car is in the middle of an intersection.

LAZ: Streetlight, puddle, garbage cans, payphone,just . . .

HECTOR: An intersection. And I'm in one piece. And so's he.

LAZ: Yup. (shock)

HECTOR: And now everything's-

LAZ: - Normal.

HECTOR: . . . My tank's almost empty,

LAZ: And my engine's back to put-putting,

HECTOR: And I lean out my window and I can see there's a streak like a bum-mark on the side of my car, but other than that-

LAZ: - We're alive. (for the first time, they look at each other; a beat)

HECTOR: And I look at this guy and I dunno what to say

LAZ: - And neither does he -

HECTOR: - But he shoots me this little head-nod like (LAZ shoots him an alpha-male head-nod) (a beat) And that's enough. (a beat; something's changed) And I turn the key in.the ignition

LAZ: Put-put. Put-put.

HECTOR: Dashboard, Turn-signal, Scooby Doo steering wheel.

LAZ: Like normal.

HECTOR: And I put my seatbelt on.

LAZ: It's 3:59 in the morning. Still. And l don't know where the hell I am -

HECTOR: - But I got somewhere I need to go. (light out on HECTOR. LAZ looks around, taking inventory)

LAZ: Streetlight. Puddle. Garbage can. Payphone . . . Payphone.
And now I'm outta my car.
And now I'm picking up the headset.
Now I'm outta my car,
And my sister gets a call.
```

---

## IC-0964: Absolution

- Title: Absolution
- Author (byline): William Reynolds
- Work: Play it again! : more one-act plays for acting students
- Publisher: Meriwether Publishers
- Publication date as stated: 1993
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BOBBY, PRIEST
- Teaser before the introduction: No
- Spoken words (computed): 1602
- Already set (do not supply): none

### Source block (context only)

```text
Author: William Reynolds
Book: Play it again! : more one-act plays for acting students
ISBN: 0916260976
Publisher: Meriwether Publishers
Date (Month/Year): 1993
```

### Introduction (context only: never use it for content warnings)

```text
BOBBY: Thou shall not….

PRIEST: have any other Gods before me.

BOBBY: covet.

PRIEST: make a graven image.

BOBBY: take the Lord’s name in vain.

PRIEST: break the Sabbath.

BOBBY: dishonor your parents.

PRIEST: commit adultery

BOBBY: steal.

PRIEST: commit perjury.

BOBBY: Crap, there’s one more…..

PRIEST: uhh…..?

BOTH: “Absolution” by William Reynolds

(The PRIEST yawns and rubs his face in a feeble attempt to wake up. But upon hearing sounds of approaching footsteps, he sits up and puts the comic book away. BOBBY enters the other side of the box and eagerly slides the little window open. He wipes his brow, takes a deep breath, and begins to speak.)
```

### Performance text (classify this)

```text
BOBBY: Bless me, Father, for I have sinned. My last confession was a week ago. (PRIEST nods absently.) Father ... Father, are you there?

PRIEST: Hm? What? Uh, yes, my son, go ahead.

BOBBY: I mean, I've really sinned.

PRIEST: Go on. I'm listening.

BOBBY: It's too terrible. I'd better warn you.

PRIEST: Nothing is too terrible for the ears of our Lord. You go right on ahead.

BOBBY: I mean, really terrible.

PRIEST: Don't be worried, my son. I hear terrible things every day. Nature of the priesthood, you know.

BOBBY: You'll be shocked.

PRIEST: My dear boy, I will listen with the patience of Job. Only please get on with it. (He picks up his magazine and glances over the cover.)

BOBBY: I've... oh, God ... I can't even say it.

PRIEST: It's all right, my boy. Spit it out.

BOBBY: I've killed someone.

PRIEST: I see. (Sudden realization) Killed someone! ... Killed someone?

BOBBY: Yes.

PRIEST: (Breathless excitement) Goodness gracious. That is something. (He rubs his eyes roughly, leans forward.)

BOBBY: So you see, Father ... I'm a murderer.

PRIEST: Well, what do you know about that. How did you do it? I mean, how did it happen?

BOBBY: It was one of those moments. I just lost control. I can't explain why...

PRIEST: Yes, yes, yes. Only what did you do?

BOBBY: I... It was Ms. Sobel. My teacher. She's had it in for me all semester. Yesterday she kept me after school. She said I plagiarized my term paper. I told her I didn't, I told her, but she just laughed. She said she was going to keep me from graduating, and tell my parents... I was scared to go home, so I just wandered around, I didn't know what I was doing. Anyway, I saw her, out by the rear door, on her way home. And in my head, she was still laughing... and next thing I knew, I had her by the neck. She tried to yell, but she couldn't, her windpipe was shut off. Then she stopped struggling... she fell...

PRIEST: No blood, then.

BOBBY: (Thrown) What?

PRIEST: Oh, uh, I mean... (Picks up his magazine.) Strangling. Only leaves marks, you know. The only bleeding comes from burst blood vessels in the eyes.

BOBBY: (Pause) That's gross ... Where was I?

PRIEST: We'd just strangled her. So, would you say you're like the Unavoidable Felon?

BOBBY: The what?

PRIEST: (Consulting the magazine) Oh, you know. (Half reading) "You felt your back was against the wall. It was kill or be killed... "

BOBBY: Well, yes, that's what it was. Still, there's no excusing

PRIEST: Amazing! Why didn't I catch this on the evening news! Was it on TV?

BOBBY: No. I mean yes. She was. Last night. But I took it away. The body. Into the river.

PRIEST: What river?

BOBBY: Who cares what river?!

PRIEST: I'm just curious

BOBBY: I'm baring my soul and you ask me what river!

PRIEST: Fine, fine, don't get upset.

BOBBY: It doesn't matter what river!

PRIEST: You're right, I shouldn't be so nosy. Only if you're not willing to discuss the matter, then why exactly are you here?

BOBBY: Because I want to confess!

PRIEST: Are you going to the police?

BOBBY: The police! Who cares about the police? I need to clear my soul! Aren't you shocked by any of this?

PRIEST: Oh yes, terrible. (Confidentially) Only... can you tell me ... what did you feel? Looking down at that cold body, realizing what you'd done. How does that feel?

BOBBY: It... I don't know, it feels awful. Why?

PRIEST: Well, I've certainly never murdered anyone. And to actually have a chance to talk to a cold-blooded killer!

BOBBY: Father! ...

PRIEST: They say it's a thrill, you know. Murderers on talk shows, they all say that. They get this icy feeling all down their spine. Were you thrilled? You know, in an icy sort of way?

BOBBY: What in the world are you, some kind of sicko maniac?

PRIEST: (Astonished and puzzled) But ...

BOBBY: I mean, I was thrilled. Yeah, right. I was thrilled.

PRIEST: (After a pause, frowning) I see. (Slumping back in his chair) Was there anything else?

BOBBY: Anything else? What kind of priest are you? I've committed murder. Murder! I've broken the first commandment. "Thou shalt not kill." I've killed!

PRIEST: Mm-hm. Refresh my memory. How did you do it again?

BOBBY: Uh... I waited, around a corner

PRIEST: Which hand was the knife in?

BOBBY: What?

PRIEST: You don't remember, do you?

BOBBY: What ... I do! ... Left.

PRIEST: Then you stabbed her after you strangled her?

BOBBY: Hang on! You're confusing me!

PRIEST: You're confusing yourself. (Sighs.) You really should've rehearsed this a little more, you know, before trying it out. Out of respect for my intelligence if nothing else.

BOBBY: You have to believe me.

PRIEST: Oh, honestly. Any devoted reader of Detective Magazine knows that the true murderer doesn't get flustered recalling the details of his crime. (Sighs.) Well, I for one am pretty let down.

BOBBY: You don't believe me.

PRIEST: Not in the least. Now, what is it you want from me?

BOBBY: I... want to be absolved.

PRIEST: But, my son, you haven't done anything! ...

BOBBY: (Exasperated) Oh, shit! (A beat) Excuse me.

PRIEST: That's all right. Now... why are you here? Really.

BOBBY: Father... do you know who I am?

PRIEST: No. You don't have to identify yourself if you don't want to.

BOBBY: I do. I'm Robert Mackenzie.

PRIEST: Bobby Mackenzie? The kid on the track team who set the record for the

BOBBY: Yeah, yeah.

PRIEST: You're Melinda's boy, aren't you? Why, I've never heard anything but compliments about you. Why do you want to go inventing murder stories about yourself? You're a good kid ...

BOBBY: Don't say that! I'm sick of that!

PRIEST: Ah...

BOBBY: That's all I ever get. Bobby the track star. Bobby the A student.. .

PRIEST: Bobby the Good Kid.

BOBBY: Exactly! I can't do any wrong! Even when I tried to skip school. I got bored sitting at home and wrote my term paper instead. I won a prize and a scholarship.

PRIEST: Well, we all have our burdens.

BOBBY: OK, OK. Maybe it's selfish of me.

PRIEST: Maybe.

BOBBY: I'm tired of being the Good Boy. I want to be bad, feel guilty, get yelled at.

I want to rob a bank. I want to ... bite a dog.

PRIEST: Bite a dog?

BOBBY: You see? I can't even think bad! I never do anything shocking. I don't even know how. I'm so perfect. I ... I don't have a life!

PRIEST: Ah. Yes. I know how you feel.

BOBBY: You do not.

PRIEST: Not the perfection bit, of course. We're none of us qualified for that. Only I certainly do know what it's like to be bored with the same old thing. What do you think it's like sitting in this booth listening to other people's lives all day?

BOBBY: At least you get to hear what real life is about.

PRIEST: Real life. The province of the extremely bored and boring, my son. This is a very dry month for transgressions. I actually got a confession from a chronic jaywalker once. (Crossing himself) God rest his soul... Yesterday I had to listen to a woman describe her sinful thoughts about the doctor who scrapes her feet. And she was the highlight of my week. You're the only interesting confession I've had all year. And you had to make it up. What kind of excitement is that? Thanks for nothing.

BOBBY: I'm sorry.

PRIEST: Ah, well. You tried... Listen, it's my turn to make a confession to you.

BOBBY: To me?

PRIEST: I used to dream about being a secret agent. All that seat-of-the-pants stuff, you know. James Bond, marvelous stuff. I've seen Dr. No eight times. That beats Father Johnson's record.

BOBBY: Huh. From secret agent to priest.

PRIEST: I know, I know. But I ended up doing what was right for me. Not everybody can be James Bond, you know. The world needs ... well, Good Kids.

BOBBY: (A beat) It's not as much fun.

PRIEST: No. But you leave less of a mess behind you.

BOBBY: So you're saying I'm better off being me.

PRIEST: You make it sound like a curse! A lot of people would love to be Bobby Mackenzie, you know. You actually did it. Congratulate yourself.

BOBBY: Thanks. You're OK, too. I mean, you do good work.

PRIEST: Thank you.

BOBBY: I'm sorry about ... you know, trying to shock you ...

PRIEST: Oh, think nothing of it, my son! I was really awake there for a minute. Only who knows, next time it could be the real thing! Now couldn't it! A man can dream.

BOBBY: (Getting up) I guess I just wanted ... I don't know. I'm so tired of doing everything right.

PRIEST: I wish I could help you, really.

BOBBY: Oh, never mind. I'm doomed to goodness. Just plain doomed. Thanks for trying...

PRIEST: (Sudden thought, snapping his fingers,) Just a minute there. I'm not through with you.

BOBBY: What?

PRIEST: Sit down!

BOBBY: But... you said yourself, I haven't done anything.

PRIEST: You call lying to a man of the cloth nothing? Do you realize that when you lie to me, you're lying to God?

BOBBY: (Stunned) I ... I didn't think about it

PRIEST: That's right. You didn't think. Adam and Eve didn't think when they committed original sin, you know. Only that wasn't good enough. God called Adam and Eve to account, and what did they say? "We weren't thinking. It wasn't our fault. We're just having an off day." Whereupon God said, "Right! Out you go!" and stuck them out in the wasteland with barely a fig leaf to call their own. You can go to hell for this sort of thing!

BOBBY: I'm sorry,

PRIEST: (More and more excited) I'm talking hellfire, boy! Hellfire and bloody damnation! Hell has a special stinking hole for liars! The blackest, stinkingest pit in all of the underworld! Hot lava and blazing flame rains down upon their writhing bodies! And I'm not just talking about a little hopping around either! These bodies writhe!

BOBBY: (Speechless) Gosh! ...

PRIEST: You'll have to do a great deal better than that. You go away and say at least ten Hail Mary’s and ten Our Fathers and don't you set foot in this holy place again until you're properly atoned, you little heathen!

BOBBY: Y-yes, Father. (Beaming) Wow! ... (They are both glowing with satisfaction)

PRIEST: How was that for some cooking?

BOBBY: Yeah, that was great. Wow! ... (A beat) Father? ... Are you here at this time every week?

PRIEST: Where else would I be? I've got no life. (BOBBY smiles, closes the window, and leaves the box. The PRIEST sighs blankly to himself, picks up his "True Detective," and begins to read. He then reconsiders, puts the comic book away, and sits up in his chair, eagerly awaiting the next confession)
```

---

## IC-0965: The Adventures of Captain Neato-Man

- Title: The Adventures of Captain Neato-Man
- Author (byline): Timothy Scott Harris
- Work: Off-Off Broadway Festival Plays – 15th Series
- Publisher: Samuel French, Inc.
- Publication date as stated: July 2017
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: LARRY, MOTHER, CAPTAIN
- Teaser before the introduction: Yes
- Spoken words (computed): 1554
- Already set (do not supply): none

### Source block (context only)

```text
Author: Timothy Scott Harris
Book: Off-Off Broadway Festival Plays – 15th Series
ISBN: 978-0573692406
Publisher: Samuel French, Inc.
Date (Month/Year): July 2017
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: The Adventures of Captain Neato-Man by Timothy Scott Harris reminds me of the things my brothers and I would make up when we were kids

ACTOR 2: I know! Hopping from the couch to the coffee table as if we were leaping across rooftops in pursuit of dastardly criminals.

ACTOR 1: I even had my own cape made out of one of mom’s dishtowels.

ACTOR 2: Yeah, but did you wear your Superman Underoos over your jeans?

ACTOR 1: (Strange look at partner)

ACTOR 2: Yeah . . . neither did I.

TOGETHER: The Adventures of (DUH-DU-DUH!) Captain Neato-Man (echo, echo, echo) by Timothy Scott Harris
```

### Performance text (classify this)

```text
Suggested Roles: Actor 1: Larry,

Actor 2: Mother, Captain

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

LARRY: (leans through an open door as he rings the buzzer) Hello?

MOTHER: (Off -- Screaming) Who’s there?

LARRY: I’m sorry. I’ve come for . . .

MOTHER: (Enters) What?!

LARRY: (Enters cautiously, carrying a newspaper clipping in his hand) I’m sorry. I must have the wrong. . .

MOTHER: I’m an old woman. I need my rest. Are you here for the ad?

LARRY: Uh, yes.

MOTHER: Why didn’t you say so? Son! Horatio is here!

Captain Neato-Man bounds onto the stage. He wears high boots, tights, a Speedo with a belt around it that carries his special gadgets, a tight-fitting shirt, and a cape with his name on it.

CAPTAIN: Horatio, my boy, you’re alive, alive! You don’t know how long I’ve waited for this moment. Stick with me and you’ll be a man. We shall tackle the cosmos together and our names shall live as one.

LARRY: I’m sorry, my name is Larry. Larry Friedman. I . . .

CAPTAIN: Larry. Horatio. What’s the difference? You answered the ad, didn’t you? Well, there you go. What are you complaining about?

LARRY: I thought this was a typing job.

CAPTAIN: Are you a communist?

LARRY: No.

CAPTAIN: Then you’re on my side. You are perfect, Horatio. Say you’ll join my team.

LARRY: What’s going on here?

CAPTAIN: Quick. If you looked up and noticed a baby falling right towards you. What would you do?

LARRY: Catch it?

CAPTAIN: It took me two weeks to pass the baby test, and you did it on the first try!

LARRY: Aw, it was nothing.

CAPTAIN: Modest . . . a superhero’s most important virtue. Do you understand how incredible our potential can be if we band together?

LARRY: No.

CAPTAIN: The fame.

LARRY: (sarcastic) Right.

CAPTAIN: The glory.

LARRY: (sarcastic) Right.

CAPTAIN: The women.

LARRY: The women?

CAPTAIN: Yes, thousands of adoring beauties clamoring for you to write personal inscriptions on their [bodies].

LARRY: Wow.

CAPTAIN: And the monetary rewards are incredible.

LARRY: Money?

CAPTAIN: Sure. You can make a fast fifty just for saving a fat lady’s cat.

LARRY: I’m good with animals.

CAPTAIN: And if you do really well, the mayor will give you the key to the city . . . Exciting, isn’t it?

LARRY: Great. What do I have to do for all that?

CAPTAIN: Simple, just jump off a tall building. . . or walk through a blazing fire.

LARRY: But I’d burn.

CAPTAIN: Not if you’re a superhero.

LARRY: I’m not.

CAPTAIN: That’s because you don’t believe in yourself. Say you’ll do it. Say it!

LARRY: I really appreciate the offer, but I’m not the type.

CAPTAIN: Type. There is no such thing as type. It’s not what you are, but who you are. How does a caterpillar turn into a butterfly? How does a seed turn into a flower? How does a larva turn into a leech? They change from the inside. Only you can decide who you are. You can go on being Larry the Larva, or you can be “Horatio” the defender of justice and sidekick to . . . “Captain Neato Man.”

LARRY: That all sounds wonderful. It’s just that I’m not qualified.

CAPTAIN: What have you done?

LARRY: Mowed lawns, baby sat, worked at McDonald’s.

CAPTAIN: McDonald’s. The epitome of the American dream. It was fate that brought you here.

LARRY: But I liked McDonald’s. They were going to make me assistant manager soon.

CAPTAIN: Then why did you answer the ad? The ad clearly states, “Be a real life superhero.”

LARRY: Please, I thought it was time for a change, but I was wrong. I’m afraid I’ll have to . . . leave.

CAPTAIN: You can’t leave.

LARRY: Why? (pause)

CAPTAIN: Because the door is locked and only I can open it.

LARRY: Let me out or I’ll scream.

CAPTAIN: Nobody will hear you. The walls are soundproof.

LARRY: If you don’t let me out, I’ll hit you, I swear.

CAPTAIN: (laughing) With my superpowers? Besides, you’re too nice. (They face off until Larry backs down)

LARRY: Ok. Ok. I’ll give you a chance. I’ll stay . . . I’ll stay . . . (Larry picks up the phone and tries to dial, but there is no dial tone) Operator. Operator.

CAPTAIN: That’s a special phone. It only takes incoming calls. The police commissioner has the number. Whenever there is a problem he can’t handle, he calls me.

LARRY: Oh, I see. How often does he call? . . . On the average . . . how many times a week?

CAPTAIN: I can’t give that information out to just anyone.

LARRY: He never calls. Does he?

CAPTAIN: He knows I’m here. He’s just a very busy man. As a matter of fact, he sent some people over just last week to talk with me.

LARRY: He thinks you’re crazy.

CAPTAIN: You don’t know. You weren’t here. I’m a superhero!

LARRY: Then prove it to me, and I’ll stay.

CAPTAIN: Neato! You won’t be sorry, Horatio. That’s the spirit. Now try on your suit!

LARRY: You haven’t proven anything yet.

CAPTAIN: Oh, still uptight, are we? You know, without your suit, your superpowers are greatly diminished. The special fabric is a unique nylon and acrylic blend. It’s resilient to blows which would otherwise be fatal . . . Jeez. How much proof do you need?

LARRY: Anything. Show me anything.

CAPTAIN: I see. I was going to save this ‘til later, but if you insist . . . My secret weapon!

(Captain pulls two identical toy guns out of a box. They look incredibly cheap and plastic. He hands one to Larry and puts the other in his belt.)

LARRY: Where did you get these? A box of Cocoa Puffs?

CAPTAIN: I saved box tops for six months.

LARRY: You are insane.

CAPTAIN: No. You don’t understand. The shape and size of this toy gun was exactly what I needed to create the perfect weapon. With a few minor alterations it became . . . THE LAZOMATIC! This baby can shoot a laser beam accurately up to 3,000 feet, annihilating anything in its path.

LARRY: Ooohhh. Wow.

CAPTAIN: Want to test it? OK. Aim at that plant. What are you waiting for? Shoot the fern.

(Larry aims at the fern and shoots. The gun makes a funny noise. Nothing else happens. He looks at the gun and tries again. Still nothing. He shoots at his head. Same thing. Captain grabs the gun and starts fiddling with it)

LARRY: It doesn’t work. It’s a toy.

CAPTAIN: That’s because you didn’t believe

LARRY: I’m not an idiot . . .

CAPTAIN: It just needs a few adjustments, that’s all.

LARRY: I know you’re crazy, but you can do this on your own. You don’t need me. Give it a try. What are you afraid of?

CAPTAIN: I fear nothing. I’m a superhero! . . . I think it’s best to have a partner, that’s all. I mean sure I could do it myself, but I’ve been waiting for a partner.

LARRY: Then why don’t you team up with . . . Superman?

CAPTAIN: What are you? Some kind of lunatic. There is no Superman. That’s make believe. It’s only a story.

LARRY: What about Batman?

CAPTAIN: Batman’s real, but he’s getting old. He can’t do it all on his own, and you know about Robin.

LARRY: You see. I don’t care. I just don’t care.

CAPTAIN: He sold out. Went into real estate. Look, it’s up to us now. We are the world’s only hope. You can’t walk away from your duty. The crime rate is outrageous. Disney is making horror pictures, and you don’t care?

LARRY: Oh, please.

CAPTAIN: You want to believe me. Deep down you’re intrigued. Admit it. Why did you answer the ad?

LARRY: I don’t have a job.

CAPTAIN: You quit McDonald’s.

LARRY: No.

CAPTAIN: Then they fired you!

LARRY: Yes.

CAPTAIN: McDonald’s fired you? What a loser . . . No . . . It was meant to be. That’s why you’re here.

LARRY: Let me go. You don’t need me. A tough guy like you can handle this job on your own. I’m worthless. I would only get in the way.

CAPTAIN: Nonsense, Horatio. You see, every superhero needs a sidekick to share in the pure joy of his manly virtues.

LARRY: Couldn’t your Mother do that?

CAPTAIN: Of course not. In order for our duo to work at its most effective level, it is essential they share a common bond. The kind of bond only a man can experience with another man. Say you’ll bond with me and glory will be yours. History will record us as the two heroes in bondage together. Don’t be afraid of chance. Try it . . . You like doing nothing, don’t you. It’s your life. Letting time slip away. Just slip away . . .

LARRY: How dare you say that about me. Look at you. You’re a fake. A fool. Your life is no better than mine. Look at this place you live in. It’s a dump. A dump.

CAPTAIN: You’re right. It’s a dump, but it’s my dump and everything in my dump has a purpose. I’m here because I choose to be here. You’ve never chosen anything in your life. You’re taking the easy way out.

LARRY: You’re the one who’s taking the easy way out.

CAPTAIN: Easy! You think it’s easy being a superhero? You think I like walking through brick walls? Don’t let this suit fool you. It’s no picnic, and no magic fairy endowed me with superpowers, either. It took hard work and determination. You should know what that is. You worked at McDonald’s.

LARRY: But don’t you see, I even failed at that.

CAPTAIN: Horatio. I know.

LARRY: What do you know?

CAPTAIN: I know what it’s like to be nothing. I was a failure too. I’ve spent most of my life feeling alone. Wishing I were dead, or just that I could be somebody else, anybody else. And when I thought there was no hope left, something happened. All at once I came alive. I realized my whole life was a test. And at that moment, I began shaping the great man you see today. I got off my butt and started exercising. I built my body into the perfect machine and now I’m ready to save the world. Who’s the bravest in the land?

LARRY: CAPTAIN NEATO-MAN!

CAPTAIN: I know you think I’m crazy. Maybe I am, but for the first time in my life I’m happy, and I know you can’t say the same.

LARRY: But this stuff isn’t real.

CAPTAIN: Anything can be real. We create realities all the time. How can you cling so desperately to your truth without knowing what truth is.

LARRY: We could die.

CAPTAIN: Be a hero, Horatio. I need you.

LARRY: No, I’m Larry . . . Larry . . .

CAPTAIN: Let go, Horatio. We could go down in history. (he strikes his superhero pose and Larry wavers)

LARRY: (voice cracking) Horatio! My name is Horatio (Larry joins the Captain in a superhero pose)
```

---

## IC-0966: The Affair at 7, Rue de M --

- Title: The Affair at 7, Rue de M --
- Author (byline): John Steinbeck
- Work: The Dark Side: Truly Terrifying Tales
- Publisher: Kingfisher
- Publication date as stated: Sept 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: FATHER, NARRATOR, JOHN
- Teaser before the introduction: Yes
- Spoken words (computed): 1177
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Steinbeck
Book: The Dark Side: Truly Terrifying Tales
ISBN: 978-0753461433
Publisher: Kingfisher
Date (Month/Year): Sept 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 2: (In true Twilight Zone/Rod Sterling fashion) (Actor 1 provides ominous background music) It is a dimension as vast as space and as timeless as infinity. It is the middle ground between light and shadow, between science and superstition, and it lies between the pit of man's fears and the summit of his knowledge.

ACTOR 1: And in this middle ground is gum! (Actor 2 screams)

ACTOR 2: The affair at 7, Rue de M by John Steinbeck
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actor 1: Father, Gum Actor 2: Narrator, John, Gum

FATHER: (to audience) At the beginning of the summer I carried my family to Paris and took up residence in a pretty little house at 7, rue de M–, a pretty little converted stable with three floors of rooms above a well-paved courtyard. This was when the events I am about to chronicle were ushered in.

FATHER: (to audience) I can find no alternative to placing the blame on my son John who has only recently attained his eighth year, a lively child of singular beauty and buck teeth. (John smiles and picks his nose)

NARRATOR: The young man has become an aficionado of that curious American practice, the chewing of bubble gum, [thank goodness] John had neglected to bring any of the atrocious substance with him from America.

FATHER: (to audience) The child’s speech became clear and unobstructed and the hypnotized look went out of his eyes. Alas, this delightful situation was not long to continue.

NARRATOR: An old family friend traveling in Europe brought as a present to the children a more than adequate supply of this beastly gum, thinking to do them a kindness. Thereupon the old familiar situation reasserted itself. Speech fought its damp way past a huge wad of gum and emerged with the sound of a faulty water trap. The jaws were in constant motion, giving the face a look of agony while the eyes took on a glaze like those of a pig with a recently severed jugular.

FATHER: (to audience) Since I do not believe in inhibiting my children I resigned myself to a summer not quite so pleasant as I had at first hoped. (Beat while John chews disgustingly; Father is distracted then refocuses on his story) On occasion, when I am composing the material for a book or play, in a word, when the utmost of concentration is required, I establish tyrannical rules for my own comfort and effectiveness. One of these rules is that there shall be neither chewing nor bubbling while I am trying to concentrate.

NARRATOR: The rule is so thoroughly understood by John that he accepts it as one of the laws of nature and does not either complain or attempt to evade the ruling.

FATHER: (To audience as John enthusiastically chews the gum) Two weeks ago in the late afternoon I sat at my desk composing a short essay, when to my astonishment and chagrin I heard the unmistakable soft plopping sound of a bursting balloon of bubble gum (Johns pops a bubble and reacts in surprise; he continues to chew loudly and without control ) (To John, sternly) You know the rule.

JOHN: (eyes wide and tear-filled, jaws working rapidly, he blubbers around a huge wad of gum) I didn’t do it!

FATHER: (angry) What do you mean, you didn’t do it? I distinctly heard and now I distinctly see.

JOHN: (moaning) Oh, sir! I really didn’t. I’m not chewing it, sir. It’s chewing me!

FATHER: (to audience) For a moment I inspected him closely. He is an honest child, only under the greatest pressure of gain permitting himself an untruth. I had the horrible thought that the bubble gum had finally had its way and that my son’s reason was tottering.

NARRATOR: If this were so, it were better to tread softly.

FATHER: (holding out his hand and speaking kindly) Lay it here.

JOHN: (trying valiantly to pull the gum from his mouth; he is terrified) It won’t let me go!

FATHER: Open up. (Father puts his fingers in John’s mouth to forcibly remove the gum. A brief struggle ensues. He finally succeeds and he flings the ugly blob onto his desk)

NARRATOR: (Actor 1 assumes the characteristics of the gum) For a moment it seemed to shudder there on the paper and then with an easy slowness it began to undulate, to swell and recede with the exact motion of being chewed. (John looks at it in disgust and amazement)

FATHER: (to audience) For a long time we watched it while I drove through my mind for some kind of explanation. (To John) How long has it been chewing you?

JOHN: (very sincerely) Last night before I went to sleep I put it under my pillow. In the night I was awakened to find that it was in my mouth. I again placed it under my pillow and this morning it was again in my mouth, lying very quietly. When, however, I became thoroughly awakened, and I was no longer master of the gum. It had taken its head. I tried to remove it, sir, and could not. You yourself with all of your strength have seen how difficult it was to extract. Oh Daddy, what do you think has happened?

FATHER: (Studying the gum intently) I must think. This is something a little out of the ordinary, and I do not believe it should be passed over without some investigation.

NARRATOR: As [he] spoke, a change came over the gum. It ceased to chew itself and seemed to rest for a while, and then with a flowing movement like those monocellular animals of the order Paramecium, the gum slid across the desk straight in the direction of [his] son.

FATHER: (to audience) For a moment I was stricken with astonishment and for an even longer time I failed to discern its intent. (John pantomimes a response to the gum’s movements, seemingly paralyzed in fright) It dropped to his knee, climbed horribly up his shirt front. Only then did I understand. It was trying to get back into his mouth. (to the gum) Stop!

(Father grabs the gum from John’s chin, he carries it to the window and hurls it into the street below. John follows his father and watches the gum land in the street. They look at each other and smile, proud that they have solved the problem. As they turn a look of terror crosses both their faces.)

NARRATOR: (Actor 1 assumes the characteristics of the gum) Under the door there crept a paper-thin sheet which, once it had entered the room, grew to a gray blob and rested on the rug, pulsing and chewing. After a moment it moved again toward [John].

FATHER: (to audience – He pantomimes as he narrates growing more and more breathless) I fought down my panic as I rushed at it. I grabbed it up and flung it on my desk, then seizing an African war club from among the trophies on the wall, a dreadful instrument studded with brass, I beat the gum. (He pauses and reacts to the images described in the following narration)

NARRATOR: The moment [he] rested, it drew itself together and for a few moments chewed very rapidly as though it chuckled, and then inexorably it moved toward [John]. For two weeks [they] were beseiged by the monster.

FATHER: In exhaustion, with my will to fight back sapped, and after we had tried every possible method to lose or destroy the bubble gum, I placed it at last under a bell jar. I collapsed in a chair to gaze at it with weary defeated eyes.

NARRATOR: (Actor 1 assumes the characteristics of the gum) Inside the bell jar the gray tumorous lump moved restlessly about searching for some means of exit from its prison. Now and then it paused as in thought and emitted a bubble.

FATHER: I could feel the hatred it had for me. What does it think?

NARRATOR: What does it want?

FATHER: What does it need? . . . . It needs and wants to get back to its host, my son. It wants to be chewed. (snaps his fingers at he realizes the solution) It must be chewed to survive. I had the answer!

NARRATOR: Inside the bell jar the gum inserted a thin wedge of itself under the heavy glass foot and constricted so that the whole jar lifted a fraction of an inch.

FATHER: (He pantomimes as he speaks) In the dining room I procured a clear plastic plate. Then turning the bell jar over and securing the monster in its bottom, I smeared the mouth of it with a heavy plastic cement guaranteed to be water-alcohol- and acid-proof. I forced the plate over the opening and pressed it down until the glue took hold and bound the plate to the glass, making an airtight container. And last I turned the jar upright again and adjusted the reading light so that I could observe every movement of my prisoner. I have you, my beauty. I have you at last!

NARRATOR: That was a week ago. (Actor 2 assumes the characteristics of the gum ast Father watches in amusement: Tries to escape, becomes agitated and nervous; chews itself frantically).

FATHER: On the fourth day it began to weaken and I observed with joy a kind of dryness on its once slick and shiny exterior.

NARRATOR: It is almost over. (Actor 2 assumes the characteristics of the dying gum: lies quietly, heaves, sighs as Father watches solemnly)

FATHER: Its color has turned to a nasty yellow. (turns his back on the gum and speaks to the audience) It will die tonight (as Father speaks, Actor 2, as the gum gathers itself and looms menacingly behind Father, then grins and shakes its gummy head)
```

---

## IC-0967: All About Al

- Title: All About Al
- Author (byline): Cherie Vogelstein
- Work: The Best American Short Plays 1998-99
- Publisher: CreateSpace Independent Publishing Platform
- Publication date as stated: May 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: LENNY, GIL
- Teaser before the introduction: Yes
- Spoken words (computed): 2205
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cherie Vogelstein
Book: The Best American Short Plays 1998-99
ISBN: 978-1557834256
Publisher: CreateSpace Independent Publishing Platform
Date (Month/Year): May 2001
```

### Introduction (context only: never use it for content warnings)

```text
All About Al by Cherie Vogelstein
```

### Performance text (classify this)

```text
GIL, very handsome and cool, sits with his back to us in an empty coffee shop, reads the sports section. LENNY, downtrodden and uncool, enters in raincoat and galoshes, furtively looks around, spots GIL, quickly looks away, orders coffee. Nonchalantly, LENNY takes cup and saunters by GIL's table. Suddenly, he stops, pretends to notice GIL for first time. Their initial conversation should be slightly awkward: the way it is when casual friends meet after not speaking for awhile: full of sound and excitement, signifying nothing.

LENNY: Gil! [Practically spills cup.]

GIL: [Looks up, friendly.] Hey... Lenny!

LENNY: What a surprise, what a coincidence!

GIL: Yehah - how ya doin', buddy?

LENNY: How are you? You look great!

GIL: Yeah? Well I'm doin' okay, you know, hangin' in there. [Awkward pause, then with some concern.] . . . how uh . . . how are YOU doin', Len?

LENNY: [Jovially.] Me? Well, I'm fine . . . alright, you know . . . not so good - [Totally serious.] - suicidal - I'm suicidal, Gil.

GIL: [Sympathetic.] Yeah, heard about you and Cindy. I'm sorry, man, we shoulda called.

LENNY: No, no I should've called you guys . . . it's just I've been so preoccupied, you know, with death, I haven't had any time. [Cheery.] So how's Allison?

GIL: Allison? She's real good . . . yeah, she should be comin' here

LENNY: [Excited.] Really?!

GIL: Yeah.

LENNY: Here? Really? [GIL nods.] That's great, that is so great!

GIL: [Puzzled by LENNY's enthusiasm.] Yeah . . . any minute.

LENNY: [Elated.] I - I can't wait to see her, I mean what good luck . . . that is so fantastic, just terrific . . . incredible really. . .

GIL: [Beat.] You're not gettin' out much, are ya, Len?

LENNY: [Instantly sad, sits, cradles his head.] It's hopeless, Gil. I'm miserable, a wreck; all alone during allergy season with my hair falling out and my gums big and bleeding - may I join you?

GIL: [Looks around uncomfortably.] Uh

LENNY: - I mean you don't know how lucky you are - wow to have a woman like Allison, kind, darling, beautiful Al

GIL: - I think we're breakin' up.

LENNY: [Shocked.] What?

GIL: [Beat.] Yeah.

LENNY: [Devastated beat.] No.

GIL: Yeah.

LENNY: [2 Beats.] No.

GIL: [Annoyed.] LENNY!

LENNY: I'm sorry but I . . . can't believe it . . . I mean I just can't believe it - you and Allison, Allison and you . . . you're like Romeo and Juliet. . . Antony and Cleopatra . . . Lawrence Olivier and Danny Kaye

GIL: Well, listen . . . I'm just tellin' ya cuz maybe, you know, it's not such a good idea for you to be around when I tell her

LENNY: Why, Gil? I'll be very quiet

GIL: Right but uh . . . even though it's a cafe deal and I'm hopin' she'll keep the cryin' down to a minimum . . . I'll tell ya, Len, things might get pretty wacky - I mean, it's not easy breakin' a girl's heart. . . ya know?

LENNY: No . . . I don't know. . . I've dreamt about it ... [Assumes the mannerisms of a girl]

GIL: Yeah, well so anyway. . . I think that's what I'm gonna do. [Pause.] Oh! [Laughs.] No offense, Len but you make a real ugly girl.

LENNY: [Sticking to his role, falsetto.] Did you want to speak to me about something?

GIL: O.K., O.K. yeah . . . [Serious.] . . . I did . . . listen, Al, I haveta tell you something

LENNY: [Coquettishly.] I love you, Gilly

GIL: Yeah, I love you too. It's over. We have to break up.

LENNY: What?! Why?!

GIL: Why? [Thinks.] Honestly? Because . . . I have a brain tumor

LENNY: [Falsetto] Oh my God! You do?

GIL: No, no, no - seriously? We have to break up because . . . I'm not good enough for you, Al, I think you deserve better

LENNY: [Falsetto.] I do but I don't want better, I want you, YOU [Almost to himself] - moronic, greasy

GIL: [Oblivious.] Yeah, but the thing is . . . I don't think I can measure up to this . . . this IMAGE you have of me, ya know? I mean, sure we might be good today, we might be good tomorrow but ultimately, I don't have what it takes to fulfill a woman like you. And one day, one day I'm gonna look into your eyes and I'm gonna see - insteada the love - I'm gonna see somethin' else - I'm gonna see all the respect drained out and gone with only the hate left. And that's gonna break my heart, Al- [Sobs.]

LENNY: [As himself] Wow. Is that true?

GIL: No but it sounded good, right? [Beat.] I mean, you can't tell her the real stuff. . . Well it's no big deal really, just this thing she does sometimes when . . . when we're lyin' there . . . ya know, in bed . . . and I'll be gettin' all comfortable, I'll be startin' to doze off - and allofa sudden, outta nowhere, I'll feel this leg swingin' over on top of me, right over my body while I'm tryin' to sleep.

LENNY: Is it her leg?

GIL: Of course, it's her leg that's not the point - the point is while I'm tryin' to sleep, I don't need some weight pinnin' me down to the mattress, you know what I mean?

LENNY: Cindy bought a bunk bed when I moved in

GIL: I mean, I'm not sayin' I don't appreciate Al's affection - I'm not saying that at all - but there's a time and a place and [when I’m trying to sleep] . . . I do NOT like to be touched, ya know?

LENNY: Cindy said [all touching] should be kept to a minimum.

GIL: Listen, Len, can I just say? - she did you the biggest favor in the world when she dumped you

LENNY: I know, I know. That's the one favor women always want to do for me - [With sudden emotion.] - which is why I'm telling you it's lonely in New York, Gil- Allison is special-

GIL: Yeah, I know she's special but . . . but . . . it's not just the leg thing, Lenny. . . it's more than that. . .

LENNY: You mean like a leg/arm kind of thing?

GIL: I mean like. . . like - [Thinks of something.] -like the way she's so obsessed with her weight! I mean, all she ever does is ask me about it all the time: Like I won't have seen her for a day and I'll pick her up and first thing when she opens the door, she'll say, "Hi, Gil, do I look like I gained weight?"

LENNY: So?

GIL: So I'll say - No, Al, you look great - and she'll say – are you sure? - and I'll say - positive - and she'll say - no you're lying -and I'll say - why would I lie? - to make me feel good - no, no way - yes, I see it in your eyes - no, that's my contact lens Al, ya haven't gained an ounce since the day you were born - you promise? - I swear - you'd tell me if I did - of course - you promise you would tell me? – I promise - you promise you promise - I promise, I swear, I swear on my life now give me a stake to put through my head cuz I can't take it anymore, Lenny, it drives me nuts!

LENNY: Why? [GIL rolls his eyes in frustration.] You mean because she's a little insecure about her figure . . . needs a little reassurance, a little positive assessment of her weight?

GIL: Yeah, but like . . . why doesn't she just invest inna scale? Ya know what I mean? Why's it havta be such a big mystery all the time?

LENNY: Gil, Gil, YOU'RE her scale, Gil, YOU

GIL: But that's the thing - to me she looks great-so what's she so worried about?

LENNY: [Shrugging.] Maybe she's afraid if she got fat, you'd break up with her.

GIL: [Softens.] Well, yeah . . . I would - but that doesn't mean she has to like "dwell," ya know? [Guiltily.] I mean, come on, Len every guy wants his girlfriend to have a nice body, right?

LENNY: [Nodding.] Cindy gained 60 pounds while we were together.

GIL: God, I know - how'd you deal with that, man?

LENNY: I loved her for what was inside

GIL: Deep, deep inside

LENNY: [Impassioned.] Look, a good woman is hard to find

GIL: Cindy's not hard to find - [Spreads his arms wide.] [Looks around, then at his watch.] I wonder why Al's so late.

LENNY: Cindy was always late, Cindy

GIL: Cindy, Cindy, will you forget Cindy!

LENNY: It just ended last week, Gil.

GIL: Yeah, well get over it already, alright? Get over it!

LENNY: [Repeats to himself.] Get over it.

GIL: -what you need is somebody nice, somebody sweet, a girl who gives ya support, makes ya feel good, really LIKES you

LENNY: [Like a kid at a toy store.] They have that?

GIL: Yeah, yeah, ya just gotta give yourself a break, buddy, ya know what I mean? Ya gotta ... go for it, ya know? [Beat.] Just go for it! [Pause.]

LENNY: Gil?

GIL: Yeah, Len?

LENNY: When uh when Allison gets here. . .

GIL: Yeah?

LENNY: When Allison gets here . . .

GIL: [Very calm.] Finish the sentence, Len.

LENNY: Can I . . . have her?

GIL: What?

LENNY: Well not "have her," "have her" is a silly expression but you know what I mean - could I ask her out - would you mind?

GIL: Would I mind? If you asked Allison out? [Beat.] My Allison, right? You mean Allison Kramer.

LENNY: Listen, if it's a problem

GIL: No, it's no problem

LENNY: - then I won't

GIL: Lenny. I said it's not a problem, okay?

LENNY: Okay. [Beat, smiling broadly, happily.] Thanks, Gilly.

GIL: Don't call me Gilly, alright? [Beat, scowling.] But I'm just thinkin' ...

LENNY: [Serious.] Uh-huh, good, O.K.

GIL: Ya know . . . what about "Cindy?"

LENNY: Oh. Well you said to forget her.

GIL: And that's it? That's all it takes - I say forget her and you're done?

LENNY: Well, Gil, I thought you gave me some very excellent advice and so I'm trying to follow up on it, is all

GIL: Yeah, well, okay . . . good. But I haveta tell ya, Len, maybe this is sicka me an' all, but it kinda does bother me, ya know? [Annoyed and confused.] I mean you askin' Allison out! I mean cuz like . . . here you are, and and like . . . the body's still warm, ya know what I'm sayin'?

LENNY: Yes but in a way, isn't that better? [Smiles broadly.] I mean, that way she won't have time to mourn over the loss of you because I'll be right there to console her

GIL: [Getting angrier.] Yeah but what I'm sayin' is I don't really want you there to console her

LENNY: But . . . Why, Gil? I mean, do you want to see her suffer?

GIL: Not at all. But I even more don't want to see her with you

LENNY: But that's not very fair, is it? I mean, here you don't want her anymore

GIL: I never said I didn't "WANT" her, Lenny

LENNY: Well, you said you were breaking up

GIL: I said I was thinkin' of breaking up - that the little, dancin' thought had walked my mind! But I mean I didn't realize that automatically gave YOU the green light to pounce? [Rises, angry.] All your concern for the what, why, why were you just, ya know, circlin' the area till you could swoop down -like some little galosh-wearin' vulture

LENNY: [Backing away.] That's not a very flattering characterization, Gil

GIL: - and . . . and what? just feast on my leftovers?! - and . . . and I mean Allison, no less - Allison of all girls - don't you know how outta your league Allison is?

LENNY: Yes of course, but - but you said to go for it!

GIL: It. IT. Not HER, you [jerk]!

LENNY: [Summoning up his courage.] But why not? [Rises.] Why not her?

GIL: Because . . . because

LENNY: [Hitting his stride.] Because what, Gil, HUH?! All my life I've watched the Leonards of this world lose the Allisons of this world to the Gils of this world and the Gils don't even care! [He throws saucer against wall.] I'm sick of it, I tell you! I'm sick, sick, sick! It's men like you who destroy women for the rest of us; abusing and demeaning and rejecting them till they so totally lose their sense of selves they actually believe the REAL men are the men who treat them that way -- when in fact you're not real at all, you're just scared, scared of growing up, scared of yourself, scared that - just like you said in that speech - that one day you're gonna look into her eyes and see the hate because deep down you believe once Allison sees you, once she really sees Gilly for who he is, she'll see THERE'S NOTHING TO SEE!

GIL: Yeah? [Rises.] Well- [Trying to find the right words] –Shut up, Lenny! Shut up! [Screams, grabs his collar.] SHUT UP! [Silence, GIL lets go.]

LENNY: I think I've offended you Gil- [Sits.] -I'm sorry

GIL: No, don't be sorry, don't be sorry - who wants your sorry, Lenny? Allison's a GIFT, a PRIZE - who loves me! And so that's a VERY scary thing [Lenny covers his face.] - I mean, it's alotta pressure - alotta - who wants to deal with dissappointin' a girl like that, ya know? ! We're not talkin' some whale beast like Cindy - we're talkin' Allison Kramer! And so even if a part athat - if part awhat you said fear - whatever you said - even if it's something involved with that. . . so what? I mean - what does that prove? That I'm no good? Because I'm - I'm human? That I may be scared of rejection deep down? Alright! So what, ya know? Deep down everybody's scared of rejection! Everybody!

LENNY: [Puffing up his chest.] I'm not!

GIL: Yeah? Well that's just cuz you're so used to it

LENNY: Damn straight! Damn straight I am! [Rises, speaks quietly.] Take a look at a real man, Gil- a man who's not afraid of rejection, of intimacy, of commitment, the dark - well okay I am a little afraid of the dark - but I'm not afraid of love! Love I embrace unguarded - and I love Allison! I want her, Gil!

GIL: [Also rises.] Yeah, well so do I!
```

---

## IC-0968: All Hail Hurricane Gordo

- Title: All Hail Hurricane Gordo
- Author (byline): Carly Mensch
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: 2008
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GORDO, CHAZ
- Teaser before the introduction: Yes
- Spoken words (computed): 1751
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carly Mensch
ISBN: 978-0573663086
Publisher: Samuel French, Inc.
Date (Month/Year): 2008
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Two brothers . . . both in their 20s . . . living on their own.

ACTOR 2: Abandoned years ago in a parking lot by their mother, who found herself overwhelmed by life.

ACTOR 1: In order to make sure that Children’s Services does not separate them, the older brother Chaz, hides Gordo, his emotionally challenged brother.

ACTOR 2: They return to their family home and work enough to pay for basic necessities.

ACTOR 1: Chaz sells off the family possessions and struggles to be the parent, all the while searching for other family members who can help --

ACTOR 2: Chaz’ infamous “letter” campaign. --

ACTOR 1: Just what are our responsibilities to our loved ones?

ACTOR 2: And how do we find a balance when those responsibilities are in conflict with our responsibilities to ourselves.

TOGETHER: All Hail Hurricane Gordo
```

### Performance text (classify this)

```text
(A living room turned makeshift office. Two desks, one neat and organized with a typewriter and carefully arranged stacks of paper and the other a total wreck, purgatory-like, where things half-eaten and half-assed take up residence. There is a worn-out couch dead center covered with piles and piles of phone books and a lone wooden chair in the corner.) (CHAZ, late 20s, sits at the neat desk. Shirt and tie. Typing. Enter GORDO, mid 20s. In boxers and a little boys’ pajama top. CHAZ continues typing. GORDO watches for a moment.)

GORDO: Hey. (Type type. Type type.) Hey Chaz. (CHAZ doesn't respond. GORDO patiently repeats himself) Chaz. Chaz. Chaz.

CHAZ: I hear you.

GORDO: You want breakfast?

CHAZ: Already ate. (GORDO exits. CHAZ pulls out the sheet of paper from the typewriter and puts it into an envelope. He finds the appropriate address in one of the phone books open on his desk.) (GORDO returns with some old mush in Tupperware. He loiters around CHAZ's desk while he eats.) What is that?

GORDO: Stir-fry.

CHAZ: From last week? You didn't see any cereal? (GORDO shrugs.) I bought some yesterday.

GORDO: You bought the bad kind.

CHAZ: I bought Cheerios.

GORDO: You bought Shit-e-os. The kind in the plastic bag. The kind you have to crawl on the floor of the supermarket to get. They look like Cheerios but surprise - they're really Shit-e-os. Simple mistake.

GORDO: How long you been working?

CHAZ: Little over an hour.

GORDO: Jeez. That's discipline.

CHAZ: Just finished the fourth one this morning. Oh. And we need to pick up more stamps. We're running low.

GORDO: Look at you. You're like this self-guided missile. Like your brain is on autopilot.

CHAZ: It's after ten by the way. We start at nine thirty.

GORDO: Yeah ... I can't get up then. Sorry.

CHAZ: Why not?

GORDO: Because. You got rid of the IV. That's how I used to tell time - the channel guide. I used to watch the channel guide every morning until breakfast. Do you know you can basically schedule your entire life just by watching the channel guide? It tells you what's on and when and how long, and there's even a little ticking clock in the upper hand corner. But now it's just. . . nothing. Where’s my compass? Where's my best friend?

Oh yeah, Chaz sold it on eBay.

CHAZ: I didn't sell it on eBay. I sold it to Kip Bearman.

GORDO: The guy from the Y? Now what's he gonna do with a TV? Smoke it?

CHAZ: (amused) Please tell me how you smoke a television set.

GORDO: Oh he'll figure out a way. He'll probably pull out all the wires and try to snort the electricity out of them.

CHAZ: What makes you think he does drugs? We see him at the pool, that's it.

GORDO: And on the bench outside, waiting for the bus. Smoking Lucky Strikes. Every Wednesday, just sitting on the bench. Smoking.

CHAZ: Cigarettes.

GORDO: Cigarettes are a drug, man. They've got nicotine. You smoke one and Bang! your brain is a plate of scrambled eggs. Haven't you seen the commercials? Don't ever smoke, Chaz. Promise me you'll never smoke.

CHAZ: It's a little late for me to take up smoking, don't you think?

GORDO: Promise me, Chaz.

CHAZ: Fine. I promise.

GORDO: You can't die on me.

CHAZ: I'm not dying.

GORDO: I'm just saying, you better not. (a moment) I'm thinking of writing a letter. To Child Protective Services. With a note that says, "Dear Protective Services. Question: Do you really protect every child in America? Answer: No. You don't. Love, Gordon. P.S. Can you please get me a new TV?" (CHAZ just stares at him.)

CHAZ: Why don't you go get dressed.

GORDO: You don't think that's funny? Writing a letter to Child Protective Services?

CHAZ: It's not that funny anymore.

GORDO: You write letters. You write like ten a day.

CHAZ: I write inquiries. It's a different thing.

GORDO: (noticing) What's up with the tie?

CHAZ: I've got a meeting today. We both do, actually.

GORDO: Ah we're auctioning off the couch. First the TV, now the couch. Everything must go!

CHAZ: We’re not selling anything. It's - an interview.

GORDO: What kind of interview?

CHAZ: You can't get upset. Someone’s coming here to interview with us.

GORDO: Why would they do that?

CHAZ: Go get dressed and we'll talk all about it.

GORDO: No. Tell me now, Chaz.

CHAZ: Not if you're going to freak out. It's no big deal. It's just a meeting.

GORDO: I'M NOT GOING TO FREAK OUT. Just tell me already. (CHAZ composes himself)

CHAZ: A potential tenant. She's coming in at eleven.

GORDO: (GORDO processes all this.) Okay. (Beat. GORDO exits to his room. CHAZ watches the door warily. A few seconds later, GORDO re-enters wearing a football helmet. CHAZ stares at him for a moment.)

CHAZ: Gordon. (GORDO stares back.) Gordo. (GORDO lowers his head like a bull.) Don't do this. (GORDO kicks invisible dirt as if preparing to charge.) I said don't. (GORDO charges. Rams CHAZ in the stomach. CHAZ falls down.) OFF! Off. Get OFF!

GORDO: AAGGHHH!!!!

CHAZ: Jesus. (CHAZ tries to wiggle out from beneath GORDO) I said off.

GORDO: I'M GOING TO BREAK YOUR ARM.

CHAZ: I need my arm.

GORDO: NO YOU DON'T. NO. NO MORE ARM.

CHAZ: You know what time it is? I think you know what time it is.

GORDO: TIME TO EAT MY FACE! (CHAZ manages to break free. Stands up.)

CHAZ: I think it's time for a time out. Go sit in the chair.

GORDO: I don't want to sit in the chair.

CHAZ: You just head butt me in the stomach. I've probably got internal bleeding. Go have time out.

GORDO: Fine. (GORDO goes to the lone wooden chair and takes a seat.) How long?

CHAZ: Two minutes.

GORDO: One.

CHAZ: Fine. (GORDO sits in the chair. Counts quietly to himself.) I think you actually ruptured my spleen this time. (CHAZ looks at his watch.) 58 . . . 59 . . . 60. (GORDO stands up.) Are you ready to talk about this like a grown-up?

GORDO: Uh huh. I'm calm now. See? (GORDO takes off the helmet.) I don't know why I get so angry.

CHAZ: I think you've got some kind of anger management problem, maybe.

GORDO: Like elephants?

CHAZ: Yeah. Like elephants.

GORDO: Goring people in Asia, trampling entire villages in Africa. It's a worldwide epidemic you know. The whole animal kingdom's striking out. (beat) I don't want to be so angry all the time. It just comes out.

CHAZ: Well you've got to work on that. People aren't going to just accept that kind of behavior out in the real world. That's what got you into trouble, remember? You can't just do whatever you feel like. You're a human being. There are certain boundaries.

GORDO: You told me to always be myself.

CHAZ: Well. Not when your self is fiery ball of rage - okay? That's when you make an exception. (beat)

GORDO: You want me to fade into the darkness like some kind of phantasm.

CHAZ: I want you to be just a little more understanding, that's what I want.

GORDO: I'm very understanding. Trust me, I understand stuff.

CHAZ: I mean more understanding of me. Of what I need. I have needs too you know. I'm not just your babysitter. (GORDO chuckles.) I'm glad you find that so entertaining. Besides - It's not just that. It's also - money stuff.

GORDO: What happened?

CHAZ: Nothing happened. We could use the extra income, that's all.

GORDO: What about all the money I made at the airport?

CHAZ: You worked there for maybe three weeks.

GORDO: And not just that. I've had a lot of jobs, man. The library -

CHAZ: Two libraries - you've worked at two of them.

GORDO: What about when I gave people tours of the neighborhood and pretended that Amelia Earhart grew up here? I taught them all how to make paper airplanes so they'd have souvenirs to take back with them.

CHAZ: That doesn't count because you didn't charge them anything. In fact, you actually spent money because of all the paper.

GORDO: That was pretty funny though, right?

CHAZ: It was a little funny.

GORDO: What about you?

CHAZ: Oh - cause two jobs isn't bad enough.

GORDO: Do three.

CHAZ: Don't you think I'm pulling enough weight here already?

GORDO: You wake up at the crack of dawn. You're up anyway.

CHAZ: I get up early to do my personal business.

GORDO: So I'll do that stuff. What - it's just writing letters and stuffing them into envelopes, right? I can do that.

CHAZ: You can't. It's my personal - it's something I do for myself, okay? It's mine. Besides - we wouldn't be in this situation if someone hadn't gotten himself fired from maybe the easiest job on the entire planet and probably blacklisted from the entire global job market.

GORDO: Hey- Can we talk about this person now?

CHAZ: Sure.

GORDO: So this person. It's a girl? Are you going to marry her?

CHAZ: I've never even met her.

GORDO: You said she was nice.

CHAZ: I talked to her on the phone.

GORDO: You can't marry her.

CHAZ: Who said I was? She'd be our tenant. And who are you to tell me who I can and cannot marry?

GORDO: Can't. Can't do it.

CHAZ: Yeah, you've said that. But why not?

GORDO: Because. (beat) I'm disabled. I have a social disorder.

CHAZ: You do not. It's all in your head.

GORDO: I have Asperger's. I looked it up.

CHAZ: How many fingers am I holding up right now? (He holds up two fingers.)

GORDO: Four?

CHAZ: You do not have Asperger's.

GORDO: You can't just go off with some girl and leave me alone.

CHAZ: How can I go anywhere? I've got to watch you like a hawk.

GORDO: You don't have to watch me.

CHAZ: Are you kidding? What if you pull another stunt like you just did? What if you grab onto some stranger's ankles at the supermarket? What if you run away and hide out in a tool shed for the next five years eating nothing but paint chips and throwing pebbles at baby animals? Watch you? You might as well be made of cement and glued to the bottom of all my shoes the way things are. (Pause. Feels bad.) Now how bout you go change.

GORDO: I should shower first. If I'm going to put on clean clothes.

CHAZ: Great idea. Why don't you go take a shower.

GORDO: Okay. (GORDO starts to exit.) Hey, Chaz. You're a good brother. You take good care of me. (pause)

CHAZ: Gordo? Do you ever . . . Do you ever think about that whole day at the parking lot?

GORDO: Whoa. Where did that come from?

CHAZ: What do you remember? (a slight pause)

GORDO: Uh. I remember coupons. Lots and lots of coupons, all over the ground where we were sitting. I remember that.

CHAZ: Do you remember what Mom did?

GORDO: Mom?

CHAZ: Before she got in the car.

GORDO: She . . . I don't know. Tripped over a fire hydrant?

CHAZ: She put your hand in mine. She didn't say anything. She just gave me your hand.

GORDO: Yeah. I remember that. (pause)

CHAZ: You used to be pretty good at stuff, remember? You were good at English - you even got that story published in the school literary magazine - the one about me and you in the underwater castle. I don't know what happened. It's like I didn't give you the right vitamins.

GORDO: You didn't give me any vitamins.

CHAZ: You might have turned out different, that's all I'm saying.

GORDO: What are you talking about?

CHAZ: Mom and Dad. You would have been different.

GORDO: Yeah - so? I would have become some boring grown-up. I would drink coffee and talk about my taxes all the time. I'm my own person. I'm a force of nature.

CHAZ: But maybe – The way you act. I mean - what if I wasn't here? To clean up after you all the time.

GORDO: Why wouldn't you be here?

CHAZ: I might meet someone someday. I might, I don't know, get a job offer.

GORDO: No you wouldn't - don't even joke about that man.

CHAZ: Come on. You must have at least considered that I might not . . . always be here.

GORDO: Why would I consider that?

CHAZ: I'm just trying to broach the topic. To have a civil conversation with you.

GORDO: Well maybe you should try being a little less aggressive about it. Your basically mauling my soul with your so-called civil behavior. (GORDO puts his fingers in his ears.) (frantic) (a long pause) How about I take out the mail? Okay?

CHAZ: It's Sunday.

GORDO: So? Let me do my job. I'm good at that, right? (GORDO picks up the mail container.) Let's see what we've got this week (He looks at the letters inside.) Englewood, Colorado. You think we've got relatives all the way out there?

CHAZ: I don't know. Worth a shot. (pause)

GORDO: It's weird that no one ever responds.

CHAZ: Got to keep trying -

GORDO: Sure, sure. It's just interesting, that's all.

(CHAZ returns to his desk. Opens up a phone book. Begins typing a letter.) (GORDO heads outside with the mail bin. We see him debate between the trash can and the mail box, then empty the mail bin into the trash can. He turns and smiles at the audience and gives them a thumbs up – giggles. Lights out)
```

---

## IC-0969: Am I Blue?

- Title: Am I Blue?
- Author (byline): Bruce Coville
- Work: Am I Blue? Coming Out from the Silence, Pg 1-18
- Publisher: Harper Trophy
- Publication date as stated: May 1995
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: VINCENT, BUTCH, MELVIN
- Teaser before the introduction: Yes
- Spoken words (computed): 1468
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bruce Coville
Book: Am I Blue? Coming Out from the Silence, Pg 1-18
ISBN: 978-0064405874
Publisher: Harper Trophy
Date (Month/Year): May 1995
```

### Introduction (context only: never use it for content warnings)

```text
Am I Blue? by Bruce Coville
```

### Performance text (classify this)

```text
VINCENT: (Pg 1-18) It started the day Butch Carrigan decided I was interested in *him.*

BUTCH: (snarling) You little fruit. I’ll teach you to look at me!

VINCENT: A moment or two later he had given me my lesson. I was still lying face down in the puddle into which Butch had slammed me as the culminating exercise of my learning experience when I heard a clear voice exclaim . . .

MELVIN: Oh, my dear! That was nasty. Are you all right, Vince?

VINCENT: (suspiciously) Who are you?

MELVIN: Your fairy godfather -- Melvin. Come on, stand up and let’s see if we can’t do something with you. (helping Vincent to his feet)

VINCENT: Are you making fun of me?

MELVIN: Moi? (arching his eyebrows and laying a hand on his chest) Listen, honey, I have nothing but sympathy for you. I had to deal with my share of troglodytes when I was your age, and I know it’s no fun. I’m here to help. You know, like in ‘Cinderella’? Do you want your three wishes or not, Vincent? (he stalks off)

VINCENT: (catching up, embarrassed) Do you have to walk like that?

MELVIN: Like what?

VINCENT: (blushing) You know . . . So swishy.

MELVIN: Honey, I gave my life to be able to walk like this. Don’t you dare try to stop me now. (proudly) I walk and talk the way I do because I’m not going to let anyone else define me.

VINCENT: (to audience) We went to a little cafe on Morton Street called Pete’s and found a table where we could talk in private. I kept trying to figure out what this was really about—- Candid Camera, an elaborate practical joke, that kind of thing. (To Melvin as he takes a sip of coffee; he’s shocked that it changed from plain coffee to Swiss double mocha; they both continue to sip during the conversation) Okay, if you’re real, then tell me how come I never heard of fairy godfathers before.

MELVIN: Because I’m the first. It was pretty much expected that I would just opt to be an angel; tracking system, you know. But I said I didn’t want to be anyone’s guardian angel, I wanted to be a fairy godfather. (rolls his eyes) Let me tell you, that caused a hullabaloo! But I said people had been calling me a fairy all my life, and now that I was dead, that was what I wanted to be. You’re my first case.

VINCENT: (nervously) Does that mean I’m gay? (to audience) I didn’t mention that I had been trying to figure out the same thing myself for about a year now.

MELVIN: You may be, you may not. The point is, you’re getting picked on because people think you are—which is why I’ve been sent to work with you. Gay-bashing is a special issue for me. It’s how I met my maker, so to speak. I was walking down the street last year, minding my own business, when three bruisers dragged me into an alley, shouting, ‘We’ll teach you!’ They never did explain exactly what it was they were going to teach me. Last thing I remember was coming face to face with a tire iron. Next thing I knew, I was knocking at the Pearly Gates. (a silent moment, then Melvin shrugs)

VINCENT: (stunned) You’re taking this awfully casually.

MELVIN: Honey, I did a lot of screaming and shouting while it was happening. Afterwards too, for that matter. Didn’t do me a bit of good—I was still dead. Once you’ve been on the other side for a while, you get a little more zen about this kind of thing. Why don’t we just concentrate on your case for the time being?

VINCENT: Okay, do I really get three wishes?

MELVIN: Sure do. Well, two, now -- You used up the first one on that coffee.

VINCENT: I didn’t tell you to change it into Swiss double mocha!

MELVIN: You didn’t have to. You wished for it.

VINCENT: (muttering) I’m glad I didn’t wish I was dead!

MELVIN: Oh! Getting personal, are we? (glances around the room, then winks at a student)

VINCENT: (hissing) Will you stop that!

MELVIN: What’s the matter? (waves his hand) I guarantee you he wasn’t offended. He’s one of the gang.

VINCENT: What gang? (Melvin purses his lips and raises his eyebrows) How can you tell something like that just from looking at him?

MELVIN: Gaydar -- Automatic sensing systems that lets you spot people of similar persuasion. A lot of gay guys have it to some degree or other. If it was more reliable, it would life easier on us. If a guy asks a girl for a date, about the worst that can happen is that she laughs at him. If he asks another guy, he might get his face pounded in.

VINCENT: (sadly) It must be lonely.

MELVIN: (sharply) It doesn’t have to be. If gay people could just openly identify ourselves, there would be plenty of people you could ask for advice. Everybody knows gay people; they just think they don’t. Do you know the great gay fantasy? (Vincent shakes his head) Imagine what it would be like if every gay person in the country turned blue for a day. All the straights would have to stop imagining that they didn’t know any gay people. They’d have to face the fact that there are gay cops and gay farmers, gay teachers and gay soldiers, gay parents and gay kids. The hiding would finally have to stop. (beat) How would you like to have the sight? You might find it interesting.

VINCENT: (suspiciously) Does this count as a wish?

MELVIN: No, it’s education. Comes under a different category. Close your eyes. (Martin waves his hands with a flourish) Okay, open up and see what the world is really like.

VINCENT: (opens his eyes and gasps) (to audience) About a third of the people in the café were blue. Some were bright blue, some were deep blue, some just had bluish tint. (to Martin in a whisper) Are you telling all those people are gay?

MELVIN: To some degree or other.

VINCENT: But so many of them?

MELVIN: Well, this isn’t a typical place. The theater crowd hangs around in here. (waves his hand grandly) Groups like that tend to have a higher percentage of gay people, because we’re naturally artistic. (frowning) Of course, some bozos take a fact like that and decide that everyone doing theater is gay. Remember, two thirds of the people you’re seeing aren’t blue.

VINCENT: What about all the different shades?

MELVIN: It’s an indicator of degree. The lighter ones are less committed—or maybe like you, trying to make up their minds. Come on, let’s go for a walk.

VINCENT: (to audience) It was like seeing the world through new eyes. Most of the people looked just the same as always, of course. But Mr. Alwain, the guy who ran the grocery store, looked like a giant blueberry—which surprised me, because he was married and had three kids. On the other hand, Ms. Thorndyke, the librarian, who everyone knew was a lesbian, didn’t have a trace of blue on her.

MELVIN: Can’t tell without the spell. Straights are helpless at it. They’re always assuming someone is or isn’t for all the wrongs reasons.

VINCENT: (beat – to audience) All right, I suppose you’re wondering about me—as in, was I blue? The answer is, slightly. When I asked Melvin to explain, he said,

MELVIN: “The Magic Eight Ball says, ‘Signs Are Mixed.’” In other words, you are one confused puppy. That’s the way it is sometimes. You’ll figure it out after a while. (Melvin disappears)

VINCENT: (to audience) Watching the news that night was a riot. My favorite network anchor was the shade of a spring sky. So was the congressman he interviewed, who happened to be a notorious Republican homophobe. (beat) I couldn’t forget his hypocritical words: “the great crime of homosexuality” and “the gay threat to American youth.” I was brushing my teeth when I figured out what I wanted to do. . . it would probably mean another beating from Butch Carrigan. Yet if I did it, nothing would ever be the same. (whispering) Melvin?

MELVIN: At your service! Ooooh, what a tacky bathroom.

VINCENT: I want to make my second wish. . . . Gay fantasy coast to coast.

MELVIN: (a beat then he smiles) How’s midnight for a starting point?

VINCENT: Twenty-four hours should do the trick, don’t you think?

MELVIN: (rubs his hands, chuckles and disappears)

VINCENT: (to audience) I went to bed, but not to sleep. I kept thinking about what it would mean when the rest of the world could see what I could see today. I turned on the radio. It was about twelve thirty when, thanks to the wonders of modern communication, it had become obvious that people were turning blue from coast to coast. It didn’t take much longer for people to start figuring out what the blue stood for. The reaction ranged from panic to hysterical denial to dancing in the streets. National Public Radio quickly summoned a panel of experts to discuss what was going to happen when people had to go to work the next day . . . or school! Which was when I got my next idea. (shouting) Melvin!

MELVIN: You rang?

VINCENT: I just figured out my third wish. (taking a deep breath) I want you to turn Butch Carrigan blue.

MELVIN: (eyes wide) Vincent, I like the way you think. I’ll be back in a flash. (he disappears and pops back in grinning) You’ve still got one wish left, kiddo. (chuckling) Butch Carrigan was already blue as a summer sky when I got there. (he disappears)

VINCENT: (beat, then to audience) So . . . if I caused you any trouble with Blueday, I’m sorry. But not much. Because things are never going to be the same now that it happened. Never. And my third wish? I’ve decided to save it for when I really need it—maybe when I meet the girl of my dreams. Or Prince Charming. Whichever.
```

---

## IC-0970: The Arrangement

- Title: The Arrangement
- Author (byline): Neil Simon
- Work: The Good Doctor
- Publisher: Samuel French, Inc.
- Publication date as stated: 1974
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: WRITER, FATHER, BOY, GIRL
- Teaser before the introduction: Yes
- Spoken words (computed): 1510
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Simon
Book: The Good Doctor
ISBN: 978-0573609718
Publisher: Samuel French, Inc.
Date (Month/Year): 1974
```

### Introduction (context only: never use it for content warnings)

```text
The Arrangement from The Good Doctor by Neil Simon
```

### Performance text (classify this)

```text
Suggested Roles: Actor 1: Writer, Father

Actor 2: Boy, Girl

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

As the lights come up, we are on a wharf. The WRITER enters and addresses the audience.

WRITER: This one goes back a good many years ago to my youth . . . I was nineteen years old, to be exact . . . And in the ways of love, I was not only unschooled -- I hadn't even been in the classroom. I was so innocent and shy that I actually thought that, since the beginning of time, no woman had ever been completely unclothed. As for connubial bliss, I dared not think of it. And as for impregnation, I chose to believe it was caused by the husband giving the wife a most ardent handshake before retiring . . . and let it go at that. But my father was a wonderful man -- quite liberal in his thinking. And on the occasion of my nineteenth birthday, he decided to introduce me to the mysteries of love. He was, however, a frugal man, and decided to escort me himself, to see, in the matter of bargaining, that I would not be taken advantage of . . . Picture me, if you will, as my own dear father . . .

FATHER: (He calls out to the side) Antosha! Antosha! Where are you? . . . Don't stand there in the dark shaking like a puppy dog. Come here. We have some adolescence to get over with

(Young Anton appears, 19-years-old, as nervous as a puppy. He frets with his hat in his hand)

BOY: I'm not well, Father. I'm sick.

FATHER: Sick? Sick? What's wrong with you?

BOY: I haven't thought of it yet. Give me a few minutes.

FATHER: Fear. That's all it is. Pubescent fear. I was the same way when I was your age.

BOY: I never knew you were my age . . . I always thought of you as older.

FATHER: How old do you think I was when I was with my first woman?

BOY: You were with a woman, Father?

FATHER: Certainly, I was with a woman. All men who become fathers have been with a woman at some point in their life.

BOY: The same woman?

FATHER: (Yells) Certainly not the same woman! My God, don't you ever discuss these matters with your young friends?

BOY: Oh, yes. All the time. But we get too excited to listen.

FATHER: It's a man's obligation to enter a marriage experienced in the ways of love . . . otherwise valuable years are wasted in endless groping.

BOY: I don't mind wasting a few years groping, Father.

FATHER: It's all in the process of becoming a man, Antosha. First you learned to walk, then you learned to talk-and now it's time to learn this.

BOY: Are you sure, Father? I'm really not walking and talking that well.

FATHER: (Irritated) Antosha, we can't afford to delay any longer. I don't want you becoming an old man waiting to become a young man . . . Now, are you going to walk in there and have your first experience with a woman or do I have to punish you?

BOY: Father . . . I don't think we're going to find any women of high moral character around here.

FATHER: We're not looking for high-moraled women. There are too damn many high-moraled women in the world as it is . . . That's why so many high-moraled men have to come down to places like this . . . Now, let's get on with this business.

BOY: Can I hold your hand, Father?

FATHER: Certainly not! You can't go in there to become a man holding your father's hand . . . Antosha, we don't have all day. Your mother is expecting us home by nine o’clock . . . Now we have exactly an hour and ten minutes for you to mature.

BOY: You mean you told mother where we were going?

FATHER: Do you think I'm so insensitive? I told her we were going out for a walk just to get some night air.

BOY: Won't she become suspicious when she notices that I've come home all grown up?

FATHER: It doesn't show, Anton. You don't get spots like measles . . . You may possibly have a small smile on your face, that's all . . . Now, come along.

BOY: Father, aren't there other ways to become a man? I mean, couldn't I grow a moustache?

FATHER: Antosha, tell me the truth, if you'd rather not go through with it, I'll take you home.

BOY: (Nods) Take me home!

FATHER: Wait till I ask the question! Would you rather not go through with it? I'll take you home . . . ?

BOY: Take me home!

FATHER: I see! Very well, let's go home . . . You can get in your tub and play with your sailboats until you're ready.

BOY: Will you be angry with me?

FATHER: No.

BOY: Will you be disappointed with me?

FATHER: No.

BOY: Will you be proud of me?

FATHER: No.

BOY: All right, I'll do it.

FATHER: Good boy, Antosha.

BOY: If I like it, can we do it again?

FATHER: No! I didn't bring you down here with the intention of leaving you here . . . By God, it's a difficult business being a liberal father. (The GIRL enters. She has flaming red hair and a cigarette in her mouth)

GIRL: 'Evening, gentlemen!

BOY: Oh, God.

FATHER: Steady, boy, steady.

BOY: Is she . . . Is she one of the teachers?

FATHER: She looks like the principal to me. We're in luck, son. She's a charming-looking girl. I'll go over and attend to your tuition . . .

BOY: Father . . . couldn't I take a correspondence course?

FATHER: No! Stand there! Don't move! I'll be right backand don't twiddle with your hat. This is not hat-twiddling business (He goes over to the GIRL) Good evening, Madame. A lovely April night, wouldn't you say?

GIRL: Is it April already? . . . I don't get out very much.

FATHER: No, I can well understand that . . . It's, er . . . it's been a long time since I've been involved in such matters, but I would like to discuss with you a subject of some delicacy-

GIRL: Thirty rubles!

FATHER: SO much for the delicacy . . . Thirty rubles, you say. Well, speaking for myself, I would say thirty rubles was quite fair. But it's not for me. It's for my young, inexperienced son. That's him! The one with the knees buckling.

GIRL: It's still thirty rubles, sir. We don't have children's prices down here.

FATHER: No, of course not. But thirty rubles does seem a bit high for a boy of nineteen . . . Would you consider fifteen rubles?

GIRL: For fifteen rubles I read Peter Rabbitt. Sir, a Norwegian ship is due in here tonight and I have to go in and put on my blond wig.

FATHER: Wait! There is an extenuating circumstance. .. It's the boy's birthday, and I wanted to give him a nice gift . . . What do you say?

GIRL: How about an umbrella?

FATHER: See here. In my day, thirty years ago, I shared the pleasures of the most delightful girl on this street-Ilka the Milkmaid, she was called-and she cost me a mere ten rubles.

GIRL: Well, she's still here. If you want her, she's down to six rubles now.

FATHER: Certainly not, good heavens . . .

BOY: Father? Oh, Father?

FATHER: Yes?

BOY: Am I ready yet?

FATHER: In a minute. I'm still shopping . . . (To the GIRL) He's really a lovely boy - fragile and sweet. Tells the most delightful stories I'm sure you'll find him most entertaining.

GIRL: Haven't you got it the wrong way around, sir?

BOY: Father, I'm getting chilly.

FATHER: (To his son) Well, run around, jump up and down. Be patient. You've waited nineteen years, it's just another few minutes . . . (To the GIRL) Twenty rubles not a kopeck more. There's just so much I'm willing to spend on education. Please, it's for my boy.

GIRL: (Looks at him, then smiles) Settled! You're a good and loving father, sir, and I respect you for it. If I had a father like you, I would never have ended up here on the streets bargaining with fathers like you.

FATHER: (Puzzled) I'm sure there's a moral in there somewhere, I just don't see it yet . . . Settled, for twenty rubles. (Gives her the money) Oh, there's just one other request I have . . At the conclusion of the evening's festivities, I would appreciate it greatly if you would just say, "Happy Birthday from Poppa."

GIRL: (Nods) "Happy Birthday from Poppa" . . . Would you like any candles, sir?

FATHER: That's not necessary. Just be gentle and kind to him. Gentleness, that's all I ask . . . (Wipes his eye) Good heavens, a tear . . . What a thing to cry over.

GIRL: I'll wait upstairs. Two flights up, second door on the left. I'll be gentle, sir.

FATHER: Thank you. The girls nowadays seem to be so much more understanding.

GIRL: May I say, it's men like you who make me proud to serve in my profession. (She kisses his hand and goes)

FATHER: What a wonderful nurse she would have made . . . Antosha, school's in. (He turns, crosses to the BOY) Settled, my boy. Twenty rubles. You have to know how to bargain with these people. Well, off you go. Two flights up, second door on the left. I'll wait out here. Don't rush. (The BOY starts, then stops)

BOY: Father, do I say anything to her?

FATHER: Like what?

BOY: Like "Hello"?

FATHER: "Hello" would be nice . . . "Goodbye" would be good too. Go on, she's waiting.

BOY: Are there any "instructions" you want to give me?

FATHER: That's what I'm paying her good money for. The questions you ask . . . Go on, boy-before I have to pay her overtime.

BOY: Yes, Father . . . I'm going, I'm going . . . (He stops)

FATHER: What is it now?

BOY: It's funny, but when I come down those stairs and out into the street . . . I won't be your little Antosha any more . . . I'll be Anton the Man. Thank you, Father. Well, goodbye. (He gets to the door)

FATHER: Wait! (Anton stops) Wait-Antosha!

BOY: What is it, Father?

FATHER: I was just thinking . . . Wouldn't you rather have a nice umbrella? There's plenty of time next year to become a man. Plenty of time next year . . .

BOY: If you wish, Pappa. Yes, Pappa.

(The FATHER puts his arm around his son's shoulder, and they tum and walk off into the night. Music plays as the stage dims out)
```

---

## IC-0971: As Is

- Title: As Is
- Author (byline): William M. Hoffman
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Oct 1985
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SAUL, RICH, DOCTOR 1, DOCTOR 2, TV ANNOUNCER, CHET, BROTHER, PARTNER, PWA, ROBOT, ACTOR 1, HOSPICE WORKER, ACTOR 2
- Teaser before the introduction: Yes
- Spoken words (computed): 1723
- Already set (do not supply): none

### Source block (context only)

```text
Author: William M. Hoffman
ISBN: 978-0822200734
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Oct 1985
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: In 1981, the first cases of AIDS were reported.

ACTOR 2: According to the CDC, by December 31, 2000 nearly 450,000 people in the United States had died.

ACTOR 1: See . . . In the 1980’s AIDS was poorly understood by the general public.

ACTOR 2: It was a disease stigmatized as an illness impacting primarily the gay community and there was no known treatment.

ACTOR 1: This selection follows two gay men in the early 1980s dealing not only with the AIDS epidemic but also with the fear that swept through our society at the time.

TOGETHER: As Is by William M. Hoffman.
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments. Suggested Roles: ACTOR 1 – 1st Man, Saul, Chet, Brother, Partner, PWA, Hospice Worker ACTOR 2 – 2nd Man, Rich, Doctor 1, Doctor 2, TV Announcer, Robot

1st MAN: (Pg 30) The first time I heard about AIDS was in the Paradise Garage, a disco I used to go to. I won a raffle, the proceeds of which went to help people with this strange new disease. I didn’t even know what it was. 2nd MAN: I thought AIDS was like Legionnaires ’ Disease, or Toxic Shock Syndrome, or Sickle-cell Anemia, Alzheimer’s Disease – one of those rare diseases you read about in the papers.

SAUL: (Pg 16-17) I visited Teddy today at St. Vincent’s. It’s very depressing . . . He’s lying there in bed, out of it. He doesn’t even know you’re there. (Pause) Jimmy died, as you must have heard. I went out to San Francisco to be with him the last few weeks. He was in a coma for a month. Everybody wanted to pull the plug, but they were afraid of legal complications. I held his hand. He couldn’t talk, but I could see his eyelids flutter. I swear he knew I was with him. (Pause) I haven’t slept well for weeks. Every morning I examine my body for swellings, marks. I’m terrified of every pimple, every rash. If I cough I think of Teddy. I wish he would die. He is dead. He might as well be. Why can’t he die? (Beat) Say something, damn it.

RICH: I have it. (Steps out of scene as Doctor 1 and Doctor 2)

DOCTOR 1: We call it a “Pre-AIDS Condition”

DOCTOR 2: “AIDS-related Complex” (Steps back into scene as Rich)

SAUL: I don’t think that’s funny.

RICH: That’s the bad news. The good news is that I have only the swollen glands . . . and I’ve lost some weight. (Pg 18-19) I tire easily. My temperature goes up and down.

SAUL: Doctors make mistakes all the time. Remember when they told my niece she had skin cancer? It turned out to be dry skin.

TV ANNOUNCER: (Pg 20) The simple fact is, that we know very little about Acquired Immune Deficiency Syndrome. Its victims may live a normal life span, or they may have only a few weeks. Fortunately, so far this tragic disease has mainly been confined to the high-risk groups and has rarely affected people like you and me. When will science conquer this dreaded plague? We don’t know. We simply don’t know . .

SAUL: You’re my friend. You’ll stay with me till you feel better.

RICH: (Pg 21) Aren’t you afraid I’ll infect you? Paper plates, Lysol, face masks – no. I’d prefer to live alone, thank you. . . Besides, if I live with you, where am I going to bring my tricks?

SAUL: You pick up people?

RICH: (Sarcastically) I lurk in dark corners where they can’t see my lumps. I’m like a shark or a barracuda, and I snap them up and infect them.

SAUL: How can you joke about this?

RICH: I don’t care. I’m going to die! I’ll take as many as I can with me. And I’ve pissed in the Croton Reservoir. I’m going to infect the whole city! Wheee!

SAUL: (PG 22) Give me a straight answer. Do you still pick up people?

RICH: Maybe I ought to wear a sign around my neck and ring a bell. “AIDS. I’ve got AIDS, stand clear!” Would that make you happy? Or maybe I should dig a hole in the ground, douse myself with kerosene, and have a final cigarette. No muss, no fuss. Is that what you want?

SAUL: Forgive me for not trusting you. It’s just that I’m frightened of it.

RICH: How do you think I feel? My lover leaves me;

CHET: (Pg 18) If you don’t mind, I’ll sleep on the couch tonight. You’ve been sweating a lot. (Pg 19) I know I’m being paranoid. (Rich reaches out to Chet) (Pg 20) Don’t touch me!

RICH: (Pg 22) My family won’t let me near them;

BROTHER: (Pg 18) I’m not in the habit of kissing my brother. I touched him on the back when I arrived and when I left. (Pg 19) Christ, I didn’t even use the bathroom.

RICH: (Pg 22) I lose my business;

PARTNER: (Pg 18) Rich and I started [this catering] business about a year ago. But now word got out that Rich has this disease. I tried to explain: he doesn’t touch the food; I do all the cooking. But they won’t listen. I can understand what he’s going through. Myself, I’ve been wrestling with cancer for a while.

RICH: (Pg 22) I can’t pay my rent. How do you think I feel?

SAUL: You’ll stay here with me. You have nowhere to go. You’ve got to stay with me. (Pause) You were kidding about picking up people.

RICH: (PG 31) Just until I feel better. . . (Pg 32) One thing. I’m embarrassed. I’m just about broke. The doctors. Tests.

SAUL: We’ll get by. You’ll see.

RICH: I’ll keep track of every cent you spend on me. You’ll get it all back when I can work. I swear. . . . Saul, I’m frightened. (Saul takes him in his arms)

SAUL: We’ll be okay. We’ll be okay.

*********** CUT TO AIDS SUPPORT GROUP (PWA=Person with AIDS) **********

PWA: (Pg 37-38) I was part of a team trying to teach robots how to use language. (He moves and talks like a robot) “I’m Harris, your android model 3135X. I can vacuum the floors, cook cheeseburgers, play the piano.” It’s much harder to tach robots to understand. (Instructing a backward robot) Joke?

ROBOT: Noun: a clash of values or levels of reality, producing laughter. Example: Have you heard about the disease attacking Jewish American princesses? It’s called MAIDS. You die if you don’t get it. Ha. Ha.

PWA: My co-workers asked me to leave. They were afraid of contracting AIDS through the air, or by my looking at them. You see, they are scientists. My last act before I left was programming one final robot. (He behaves like a robot again) “Good morning. This is Jack – (He suddenly becomes a flamboyantly gay robot) but you can call me Jackie – your fabulous new android model 1069. If you wish to use me – and I love being used – press one of those cunning little buttons on my pecs. Go on, press one – (He switches from a campy tone to an almost angry, accusatory one) or are you afraid of me too?” That was my stab at immortality.

RICH: I’m not sure I have it anymore. I feel like somehow I’m being disloyal to the group. (but) I’m getting better, I know it. I just have these lumps, which for some reason won’t go away. I feel great. I feel the disease disappearing in me. Only a tiny percentage of those with the swollen glands come down with the rest. If I really thought that I was coming down with it . . . we all have options. . . .

TRANSITION

ACTOR 1: But Rich was not getting better. The disease progressed rapidly and soon, Saul was visiting Rich in the hospital as they tried desperately to combat the symptoms ravaging his body. Rich began to contemplate his options.

RICH: (Pg 47) Saul, I want you to do something for me. Will you do something for me? Now listen. I want you to go out of here and go to the doctor and tell him you aren’t sleeping so hot

SAUL: I’m sleeping okay.

RICH: Sh! Now listen: you tell him you want something to make you sleep and Valium doesn’t work on you, but a friend once gave you some Seconal –

SAUL: No! I won’t do it!

RICH: (Pressuring Saul relentlessly) I tried hoarding the pills here, but every night the nurse stays to watch me sallow them down.

SAUL: I can’t do that. I won’t listen.

RICH: If you love me, you’ll help me. I have something that’s eating me up. I don’t want to go on. I’m scared to go on.

SAUL: Don’t do this to me! I can’t handle it. . . I swear, don’t do this –

RICH: Don’t you see, it’s the only way. Just get the pills. Just have them around. You’ll get used to the idea. And when the lesions spread above my neck so that I don’t look the same, you’ll want me to have them. (Pg 52) What’s so hot about living when you’re covered with lesions and you’re coming down with a new infection every day? . . . . If it gets too bad, I want to be able to quietly disappear.

SAUL: I won’t argue the logic of it. I can’t do what you want me do.

RICH: I just want them around. You keep them for me – just in case.

SAUL: I won’t

RICH: Then I’ll get them myself. (Tries to get up, but is shaky) (Pg 53) Where’re my clothes? (Takes a few steps)

SAUL: Get back in bed! (Tries to help steady Rich)

RICH: I want to get out of here! (Fighting Saul) This place is a death machine! (He collapses on the floor)

SAUL: (sits beside him) You idiot . . . I want you to understand something. It’s important. Listen. (Pg 54) Don’t you see, I just don’t have the right to take your life. Maybe I’m being selfish, but I want you here. (Pg 52) Let me help you live!

RICH: My future isn’t exactly promising. (Pg 48-49) I have Kaposi’s sarcoma, a hitherto rare form of skin cancer. It’s spreading. I have just begun chemotherapy. It nauseates me. I expect my hair will fall out. I also have a fungal infection of the throat called candidiasis, or thrush. My life expectancy is . . . I have a greater chance of winning the lottery.

SAUL: (Pg 54) I’ll take you as is.

RICH: But what happens when it gets worse? It’s gonna get worse.

SAUL: I’ll be here for you no matter what happens. I promise.

RICH: Shit. You’re so goddamned noble.

SAUL: How do you want me to be?

RICH: I can’t afford to be noble. The only thing holding me together is rage. It’s not fair! Why me?

SAUL: Why not you? Maybe it’s me next. No one knows.

RICH: I reserve the right to put an end to all this shit.

SAUL: All right, but if you kill yourself they won’t bury you in hallowed ground and you’ll got to hell with all us Jews.

RICH: I bet they have a separate AIDS section in the cemetery so I don’t infect the other corpses. (Beat. Then suddenly he speaks fiercely) Do you promise to stick with me no matter what happens?

SAUL: I do.

RICH: Do you? (He searches Saul’s face for the answer) I need you. (Long silence. Rich exits scene as Hospice worker steps forward to address the audience) **********

HOSPICE WORKER: (Pg 56-57) I have a new AIDS patient, Richard. He still has a lot of denial about his condition. Which is normal. I think most of us would go crazy if we had to face our own deaths squarely. Rich will be out of the hospital again in a week or so. For a while. He’s a fighter . . . The angry phase is just about over and the bargaining phase is beginning. If he behaves like a good little boy, God will do what Rich tells Him to do . . . I certainly hope that God does.

CLOSING

ACTOR 2: In the US today; research, education and treatment options have converted AIDS from a certain death sentence to a condition that can be managed.

ACTOR 1: According to the Kaiser Family Foundation . . . over 1.2 million people in the US today are LIVING with HIV/AIDS.

ACTOR 2: We have a long way to go . . .

ACTOR 1: Minority populations and rural areas of the US are still more profoundly affected than the rest of the county. But progress is being made

ACTOR 2: The panic of the 1980’s has ended and today, people are being more readily accepted AS IS.
```

---

## IC-0972: Assassins

- Title: Assassins
- Author (byline): Stephen Sondheim and John Weidman
- Work: Not specified
- Publisher: Theatre Communications Group
- Publication date as stated: Sept 1991
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BOOTH, HEROLD, VOICE FROM OUTSIDE BARN, ACTOR 1, ACTOR 2, TOGETHER, RADIO ANNOUNCER, OSWALD
- Teaser before the introduction: Yes
- Spoken words (computed): 1940
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephen Sondheim and John Weidman
ISBN: 978-1559360388
Publisher: Theatre Communications Group
Date (Month/Year): Sept 1991
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 2: To paraphrase the words of author Blake Crouch: What if time is an illusion, a construct made of human memory?

ACTOR 1: What if there’s no such thing as the past, the present or the future? What if It’s all happening now?

ACTOR 2: What if John Wilkes Booth could come face to face with Lee Harvey Oswald, two men forever tied to the assassinations of American presidents. Booth, full of self-righteous conviction:
```

### Performance text (classify this)

```text
Suggested Roles Actor 1: Booth and Radio Announcer (shared)

Actor 2: Herold, Voice, Oswald, and Radio Announcer (shared)

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

(Pg 15) A tobacco barn in rural Virginia – middle of the night. Booth sits huddled on the floor, drinking from a brandy bottle and reading through a pile of newspapers.

BOOTH: (Pg 17-19) Damn! (takes a tattered diary out of his pocket and starts to write. The door bangs open and *David Herold rushes in)

HEROLD: They're coming! They'll be here any minute! (begins frantically gathering their things. Booth throws down his pen; his hand is trembling)

BOOTH: I need your help. I've got to write this and I can't hold the pen!

HEROLD: Johnny, they've found us! We've got to get out of here!

BOOTH: Not till I finish this. Have you seen these papers?! Do you know what they're calling me?! A common cutthroat! A hired assassin! This one says I'm mad!

HEROLD: We must have been mad to think we could kill the President and get away with it!

BOOTH: We did get away with it! He was a bloody tyrant and we brought him down! And I will not have history think I did it for a bag of gold or in some kind of rabid fit!

HEROLD: Johnny, we have to go --

BOOTH: No! I have to make my case. Take it down. (Booth holds out the diary and the pen and dictates as Herold writes) An indictment. Of the former President of the United States, Abraham Lincoln, who is herein charged with the following High Crimes and Misdemeanors- One: That you did ruthlessly provoke a war between the States which cost some six hundred thousand of my countrymen their lives. Two: That you did silence your critics in the North by hurling them into prison without benefit of charge or trial. Three-

VOICE FROM OUTSIDE BARN: Booth! I have fifty soldiers out here, Booth! Give yourselves up or we'll set fire to the barn!

HEROLD: Don't shoot! I'm coming out! (throws down the diary and rushes out the door)

BOOTH: No! (to audience) I have given up my life for one act, you understand? Do not let history rob me of its meaning. Pass on the truth! Please . . . (to soldiers outside the barn) Hunt me down, smear my name, say I did it for the fame . . . What I did was kill the man who killed my country!

ACTOR 1: (as Booth) Sic semper tyrannis!

ACTOR 2: And Oswald, who many Americans still believe did not act alone:(as Oswald) “My definition of democracy: The right to be in a minority and not be suppressed.”

ACTOR 1: What would Booth say to Oswald in the minutes leading up to . . .

ACTOR 2: (voice of radio announcer) Breaking News: Shots fired from the Texas School Book Depository.

ACTOR 1: Is history a twisted game of chance or one inevitable destiny where those who feel abandoned and disenfranchised simply find a gun.

TOGETHER: Assassins by Stephen Sondheim and John Weidman

(Pg 90 – 95) A storeroom on the sixth floor of the Texas School Book Depository in Dallas, Texas. Lee Harvey Oswald sits on a carton reading a handwritten note. On the floor beside him are a lunch pail and a long package wrapped in a blanket. An announcer comes on the radio

RADIO ANNOUNCER: That was the Blue Ridge Boys and "Heartache Serenade." And now we take you live to KTEX reporter Harry- Oswald turns off the radio as he re-reads the note. He opens the lunch pail, takes out a gun and puts it to his head. Whistling off stage. Oswald spins around. John Wilkes Booth steps onstage.

BOOTH: Oh! I'm sorry. I was just browsing. Please, carry on . . . (notices the gun. Oswald shoves it back in the lunch pail. Booth indicates a wall clock) Is that the right time? Yes? (taking out a pocket watch) I don't know what's the matter with this thing. Excuse me for a moment.

(crosses to the radio and turns it on)

RADIO ANNOUNCER: -- speaking to you from Love Field, where the President's plane has just touched down and is taxiing toward us. We understand the President intends to speak briefly at the airport before proceeding into Dallas, where- (Oswald turns it off )

BOOTH: (picks up the note, reads) Dearest Marina. Today I end my life so that your life can begin. Last night you said that I oppressed you . . .

OSWALD: (Oswald snatches the note) F*** you.

BOOTH: We seem to have gotten off on the wrong foot here. (Oswald grabs lunch pail) You're not going, are you? (Oswald heads for the door) Don't leave now. Come on, I didn't mean to . . . Alik. (Oswald stops)

OSWALD: What did you call me?

BOOTH: Alik. You used to like that nickname. Back in Minsk. Marina said Lee sounded Chinese, so she called you Alik. Of course I don't have to call you Alik. I just thought . . .

OSWALD: How do you know what Marina called me?

BOOTH: I know lots about you, Lee. Let's see. . . (rattling it off like a resume) Born, New Orleans, October 18, 1939. Father, Robert, died before your birth. Crazy mother, Marguerite. Dropped out of school at seventeen. Joined the Marines. Court-martialed twice. Defected to the Soviet Union, October, 1959. Defected back, June, 1962. Married, Marina Nikolaevna. Two children, June and Rachel. Current employment, stock boy, Texas School Book Depository, Dallas, Texas . . . Oh. And this morning, depressed over your estrangement from a wife who views you as a dismal and pathetic failure, you rose before dawn, kissed your sleeping children, put your last hundred dollars and your wedding ring into a cup which Marina's mother gave you for a wedding present, and came here to kill yourself . . .

OSWALD: Who are you?

BOOTH: I'm your friend, Lee.

OSWALD: I don't have any friends. (beat) Show me your badge.

BOOTH: My what?

OSWALD: You bastards think you're so smart. I know my rights. You try to interrogate me at my place of business I can sue you for harassment.

BOOTH: Ah! You think I'm with the FBI!

OSWALD: I have a right to see your badge.

BOOTH: (opens his coat, holds out his arms) Search me, Lee. You think I've got a badge. Come on, search me. (Oswald starts to frisk him. Booth grins) The FBI. You really love those morons, don't you? Hell, why wouldn't you? No one else cares if you live or die, those guys can't get enough of you. "How was your day, Lee? Sell any secrets to the Soviets? Sabotage any defense plants? Kick off your shoes and tell us all about it!"

OSWALD: (shoving him away) F*** you, whoever you are!

BOOTH: (smiles) I'm sorry, Lee. It's just so sad . . . I mean, it's all you ever wanted, isn't it? Someone who wants to hear about your day. Someone – anyone -- Your mother. Mother Russia. The Marines. Your wife Marina . . . (shakes his head) Attention must be paid.

OSWALD: What's that mean?

BOOTH: It's from a play. About a salesman. A man very much like you, Lee. independent, proud, a decent man who tries and tries but never gets a break. So, he does something dumb. When he realizes his whole life has been a failure built on lies, he kills himself. And when he's dead, his wife stands at his grave and says attention must be paid. She has to beg the world to pay attention to this poor, misguided nobody . . . I'm an actor, Lee; a good one. But Willy Loman is a part that I could never play. And I don't think that you should play it either.

OSWALD: (beat) I don't know what you're talking about.

BOOTH: What do you want, Lee?

OSWALD: You know so much, why don't you tell me?

BOOTH: You want what everybody wants. To be appreciated. To be valued. You want someone to love you, Lee. Right? . . . Isn't that it? . . . Lee?

OSWALD: Yes.

BOOTH: [Well], forget it. It's never going to happen. It's a fantasy. You've got to give it up.

OSWALD: I'm going to kill myself! Don't you think I've given it up?!

BOOTH: No. I think you're going to kill yourself because you think that's how to get it. "When I'm dead, then they'll be sorry! When I'm dead they'll know how much they loved me!" When you close your eyes you probably see the funeral, don't you, Lee? A gentle rain is falling. Everybody has umbrellas-

OSWALD: Shut up!

BOOTH: There's Marina, weeping quietly. Your sobbing children clutching at her skirt. Your mom, your dad. Every boss who ever fired you . . . I'm sorry, Lee. It's just so childish. It's so dumb.

OSWALD: You think it's dumb?! If I shouldn't kill myself what should I do?! Go home?! Beg her to take me back?! Plead with her?! Beat her up?!

BOOTH: You tried all that. It doesn't work.

OSWALD: I know it doesn't work! So tell me what I should do!

BOOTH: You should kill the President of the United States.

OSWALD: What?

BOOTH: He's coming into town to make a speech. His plane landed at the airport 15 minutes ago. His motorcade is going to go right past this window. When it does, you shoot him.

OSWALD: You're nuts. I didn't come here to shoot the President.

BOOTH: He didn't come here to get shot. . . All your life you've been a victim, Lee. A victim of indifference and neglect. Of your mother's scorn, your wife's contempt, of Soviet stupidity, American injustice. You've finally had enough, so how are you planning to get even?

OSWALD: I'm not a murderer.

BOOTH: Who said you were?

OSWALD: You just said I should kill the President . . .

BOOTH: Lee, when you kill a President, it isn't murder. Murder is a tawdry little crime; it's born of greed, or lust, or liquor. Adulterers and shopkeepers get murdered. But when a President gets killed, when Julius Caesar got killed . . . he was assassinated. And the man who did it

(lets the sentence hang, unfinished)

OSWALD: Brutus.

BOOTH: Ah! You know his name. Brutus assassinated Caesar 2000 years ago, and here's a high school drop-out with a dollar twenty-five an hour job in Dallas, Texas who knows who he was. And they say fame is fleeting . . . (smiles; Oswald stares at him. beat)

OSWALD: This is stupid. Up here on the sixth floor, what would I do? Throw schoolbooks at him?

BOOTH: What's in the package that you brought to work? (indicating package wrapped in blanket) What's in it?

OSWALD: Curtain rods.

BOOTH: (picking up the package) You sure?

OSWALD: Sure I'm sure. Marina wanted me to take them to the . . . (Booth tosses the package to Oswald; Oswald catches it, looks surprised. He folds back the blanket, revealing a high-powered rifle)

BOOTH: That's a Mannlicher-Carcano. 6.5 millimeter. Stopping range, nine hundred yards. The sight's already been adjusted.

OSWALD: Who are you?

BOOTH: My name is John Wilkes Booth.

OSWALD: John Wilkes Booth shot Abraham Lincoln.

BOOTH: (quietly, smiling) Attention has been paid . . . All your life you've wanted to be part of something, Lee. You're finally going to get your wish. (Oswald drops the rifle and turns to leave, Booth blocks his exit) (Pg 97) OK, OK . . . Lee, I'm sorry. I know things are happening kind of fast here. But you can't leave now. You have a responsibility here, Lee.

OSWALD: To who? To you? I'm responsible to me and no one else!

BOOTH: Not anymore, Lee. Fifty years from now they'll still be arguing about the grassy knoll, the mafia, some Cuban crouched behind a stockade fence, but right here, right now -- this is the real conspiracy. And you're a part of it.

OSWALD: Get out of my way.

BOOTH: (holding his ground) You have to do this. Now. You won't get another chance.

OSWALD: So what? I'll do something else. I'll shoot my wife. I'll shoot my kids. I won't shoot anyone! Who cares?!

BOOTH: (Exploding) I care, you stupid fool! Sorry. I'm sorry . . . (Pg 98) Take a look, Lee. (indicating scene outside) You know what that is? That's America. The Land Where Any Kid Can Grow Up to Be President. But in here (taps Lee’s chest), this is America, too. . . "The mass of men lead lives of quiet desperation." An American said that. And he was right. But let me tell you something. There are no lives of quiet desperation here. Desperation, yes. But quiet? Not today. Today we're going to make a joyful noise. You're the one that's going to sum it all up and blow it all wide open. Why, after you . . . (pauses) (Pg 99) I've seen the future, Lee. And you are it. (snaps his fingers; the radio comes on)

RADIO ANNOUNCER: -- and now the motorcade is turning into Elm Street. There's someone holding up a banner, "All the Way with JFK." The President is smiling and waving as his car heads for Dealy Plaza where it will swing past the Texas Book Depository - (Booth snaps his fingers again; the radio goes off. He opens the window, picks up the gun and holds it out)

OSWALD: People will hate me.

BOOTH: They'll hate you with a passion, Lee. Imagine people having passionate feelings about Lee Harvey Oswald . . .

OSWALD: (reaches for the gun, hesitates, then drops his hand)

BOOTH: (Pg 101) All you have to do is move your little finger -- you can close the New York Stock Exchange. You have the power of Pandora's Box, Lee. Open it . . . (holds out the gun. Oswald takes it.) I envy you . . . (Oswald turns and crouches at the window) (Pg 102) All you have to do is squeeze your finger. Squeeze your finger . . . You can change the wor -- Oswald fires. Booth exits. Oswald turns. Where did he go? Oswals lurches to his feet, grabs his lunch pail and exits. A beat, then Booth returns. He picks up Oswald's suicide note, takes matches from his pocket and burns it.)
```

---

## IC-0973: Babel’s In Arms

- Title: Babel’s In Arms
- Author (byline): David Ives
- Work: Time Flies and Other Short Plays
- Publisher: Grove Press
- Publication date as stated: March 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GORPH, CANNAPHLIT, BOTH, BSWOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1243
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Ives
Book: Time Flies and Other Short Plays
ISBN: 978-0802137586
Publisher: Grove Press
Date (Month/Year): March 2001
```

### Introduction (context only: never use it for content warnings)

```text
Babel’s in Arms by David Ives
```

### Performance text (classify this)

```text
Suggested Roles Actor 1: Gorph Actor 2: Cannaphlit and Businesswoman

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Enter two workers, GORPH and CANNAPHLIT Primitive tools hang from their belts. They are carrying between them an enormous rectangular building stone, maybe five feet long and two feet high. They inch slowly toward center with it, as . . .

GORPH: (groaning under the stone's weight) Okay. . .Okay. . . Okay. . .Stop. (A moment, as they catch their breath.)

CANNAPHLIT: Okay?

GORPH: Go.

BOTH: (ad lib, moving toward center) Okay. Okay. Okay. Okay.

GORPH: Stop. (They catch their breath a moment.) Go. (They move a few inches.) Stop. (They stop to catch their breath) Go.

CANNAPHLIT: (at center now) Stop.

GORPH: Okay. Down. (They slowly lower the stone.) Down. Down. Down. Down. Down. Stop. (looks at it.) Behold! . . . . It’s backwards. (They go in a circle.) Circle

CANNAPHLIT: Circle.

GORPH: Stop. Okay. Down. . . Down. . . Down. . . Stop. (They now have it an inch over the ground.) One. Two. Five. Go! (They drop the stone to the ground.) Behold the stone!

CANNAPHLIT: Behold the stone! Big stone. (They moan, they groan, they stretch, they wipe sweat from each other's foreheads.) But what is a "stone," O, Gorph, son of Khlekhmalekhm?

GORPH: That heavy thing there. That is a stone, O, Cannaphlit, son of Bob.

CANNAPHLIT: Ah, so that is a stone. But is this stone in the right place, O, Groph, son of Khlekhmalekhm?

GORPH: I will consult the plans, O, Cannaphlit, son of Bob. (He takes out a large parchment roll.) Behold the plans.

CANNAPHLIT: Behold the plans! (GORPH unrolls a blueprint-a large blue sheet of paper with just a single white rectangle in the middle.)

GORPH: (After inspecting the plans) The stone must move one sixteenth of an ell to the north!

CANNAPHLIT: One sixteenth of an ell! How far is that?

GORPH: About an inch.

CANNAPHLIT: (as GORPH takes out the crowbar) O my friend? What is that?

GORPH: This item has no name, for humanity is young and has not words yet for every item. Basically, it's a rigid rod that pivots about a fulcrum and is used to move an object at point A by applying force at point B. . . . I call it a lever.

CANNAPHLIT: Behold the lever!

GORPH: (With a huge grunt, he levers the stone an inch to the lift; that done, he checks, and nudges it with his toe one last small bit.) The stone is now in place.

CANNAPHLIT: The stone is in place! (They snort, high-five, shake hands, flex muscles, grab crotch, and generally male-display.) So what is the stone for, O, Gorph?

GORPH: This stone? This stone is for. . . You mean thou dost not know?

CANNAPHLIT: I dost not know. (They regard, the stone a moment.)

A BUSINESSWOMAN in a killer suit with a large sword in a scabbard, enters sets up a sign that says "FUTURE HOME OF BABEL."

GORPH: (reading the sign) "Future Home of Baybel."

BSWOMAN: Babble. It's not "Baybel." It's Babble. Now listen up, you rotten stinking men.I represent a consortium of off-desert investors who want to develop this property. Our mandate is to build a tower whose top will reach to the very heavens, indeed, into heaven, indeed, as high as God. This in order to show that we are equal to same aforesaid God.

GORPH: That we are equal to God?

BSWOMAN: No, that we, not you, are equal to same aforesaid God. You are nothing. You are scum, but you build the tower. Have you got that?

GORPH: We're scum. We build the tower.

BSWOMAN: In the event that same aforesaid God is not pleased, the consortium is not responsible for any long-term apocalyptic events. Sign here. (presents a parchment; Gorph and Cannaphlit sign and she immediately takes it away) Understood. Now. The most important thing. And this is absolutely crucial. Are you listening? (They nod.) Do not - under any circumstances - khlumnafluffa himnaflekh.

CANNAPHLIT: Do not khlumnafluffa bimbaflekh?

BSWOMAN: Himmm-naflekh.

CANNAPHLIT: Himmmmm-naflekh.

BSWOMAN: (pulls sword from its scabbard) Instructions clear? Or else you die.

GORPH: Mm-hm... Oh yeah. . . I think so . . . Very clear. . .

BSWOMAN: One last crucial thing. Did you bring the shpoont?

GORPH: Oh, the shpoont.

CANNAPHLIT: I think we have the shpoont.

GORPH: The shpoont was here a moment ago.

BSWOMAN: Do not proceed without the shpoont. (takes out the sword) Or else you die. I'll be checking in very soon. Now get to work. (Businesswoman exits.)

GORPH: Khlumnafluffa himnaflekh . . .

CANNAPHLIT: Khlumnafluffa himnaflekh. . . .

GORPH: What the heyyyyy is that?

CANNAPHLIT: That was a little vague. The other instructions were pretty clear.

GORPH: Oh yes? Repeat the instructions. Refresh my memory.

CANNAPHLIT: Build a tower whose top reaches to the very heavens, indeed, into heaven, indeed as high as God. Proving that they - not we because we are scum - that they are equal to same aforesaid God.

GORPH: That's very clear.

CANNAPHLIT: And don't khlumnafluffa himnaflekh, or you die.

GORPH: And don't forget the shpoont. (They look at each other and shrug)

CANNAPHLIT: Maybe we could put a portico on the tower, in pink, do a rich pink ceiling, maybe use that sponging technique. . .

GORPH: But consider this, O son of Bob. Putting the pink portico aside for a moment. Why? Let us nail down why. Name an attribute of God. Go ahead. Just pick an attribute, any attribute.

CANNAPHLIT: God is fairly powerful.

GORPH: Powerful. Mm-hmm . . .. Any other attributes?

CANNAPHLIT: I'd say God is eternal and infinite.

GORPH: Infinite. Let's pause there for a nanosecond. How high would a tower have to be to meet an infinite God?

CANNAPHLIT: Hmmm. (He ponders that a moment, then raises his hand like a student.)

GORPH: (teacher) Cannaphlit?

CANNAPHLIT: Infinitely high?

GORPH: Infinitely high. So you're going infinitely high – how broad would the base of same aforesaid tower would have to be? Just gimme a rough guesstimate. (Pause as Cannaphlit ponders that. Then he raises his hand again like a student.)

GORPH: (teacher) Cannaphlit?

CANNAPHLIT: Infinitely broad?

GORPH: Innnnfinitely broad. How many stones would we have to use? An innnnnnfinite number of stones. And how long did it take us to get this stone here?

CANNAPHLIT: Two years.

GORPH: So our task is to build a tower infinitely high, infinitely broad, from an infinite number of stones, shake hands with God AND - do not khlumnafluffa himnaflekh while using the shpoont.

CANNAPHLIT: It's gonna be work.

GORPH: It's gonna be work.

CANNAPHLIT: (brilliant idea) Maybe we should get out of it!

GORPH: But how, O brilliant Son of Bob? We just say no? But we need a reason. So when they ask us why we've laid down our tools, we say. . . ?

CANNAPHLIT: We could tell them God doesn't exist.

GORPH: I love it! It's simple. It's elegant.

CANNAPHLIT: What could they do?

GORPH: Cut off our heads! (They ponder the dilemma for a moment, grunting)

CANNAPHLIT: Wait a minute. Who says God is in the sky?

GORPH: Yeah! Where did this arcane idea come from?

CANNAPHLIT: Maybe God isn't up, maybe God is down.

GORPH: Oh, man, it's brilliant. Brilliant!

CANNAPHLIT: We don't have to build a tower infinitely high and infinitely broad! We just have to dig a big hole! (They celebrate, but then realize)

BOTH: An infinite hole. . .

CANNAPHLlT: Wait a minute. (tapping his head with a brilliant idea) Candlepower! Candlepower!

GORPH: What've you got? What. What. What.

CANNAPHLIT: We tell them God is everywhere. If God is everywhere, you don't have to build a tower or dig a hole or nothin' !

GORPH: Because we're already there. (They celebrate wildly for a moment, then stop suddenly.) Is it true?

CANNAPHLIT: I don't know. We could say it. (They go back to celebrating.)

BOTH: Whoo-EEEEE!

CANNAPHLIT: We're there, buddy! GORPH: We did it!

(They snort, high-five, shake hands, flex their muscles, grab their crotches, and generally male display. The Businesswoman comes in and watches them celebrate.)

BSWOMAN: So how are we doing?

GORPH: Good. Good. We're doing good. Excellent.

CANNAPHLIT: There it is.

GORPH: (arms wide over the audience) Behold!

CANNAPHLIT: (arms wide over the audience – a pause) The tower!

GORPH: Shake hands with God, baby. 'Cause we are DONE.

BSWOMAN: (draws the sword) Explain this to my trusty sword.

CANNAPHLIT: Well... You don't need a tower because God is everywhere. You see?

BSWOMAN: I see nothing. And my sword sees nothing.

CANNAPHLIT: Maybe you're not looking hard enough. (points) God is here. (points elsewhere) God is here . . .

GORPH: God's up there, God's down there. I swear to God. Who is everywhere. As you see. (Silence.)

BSWOMAN: Did you khlumnafluffa himnaflekh?

BOTH: Oh no. No, no. Uh-uh. Never. Not at all. Mmmm. Don't think of it. Nope. No way.

BSWOMAN: Did you use the shpoont?

GORPH: Constantly.

BSWOMAN: I don't believe you. Prepare to die. (She raises the sword.)

CANNAPHLIT: We saved your life! The tower you wanted would've taken an innnnnfinite number of stones which would've cost an innnnfinite number of schmootzkels. Consortium calls you in! You’re cold cuts, babe. (The Businesswoman considers that a moment.)

BSWOMAN: Gentlemen - I LOVE THIS TOWER. It's beautiful! It's got balance, it's got harmony.

GORPH: Put together an infinite number of nothing - eventually, you get this.

CANNAPHLIT: How do you like the portico?

BSWOMAN: The portico is my favorite part! Congratulations! (Now all three of them snort, Flex, shake hands, etc.) Well you guys did a terrific job and the Consortium thanks you. So as a bonus here's a bag of cow manure for you.

(Gives a dripping bag to Gorph and another to Cannaphlit) And a bag of cow manure for you.

GORPH: Golly. Thanks a lot. That's cow manure all right.

CANNAPHLIT: Nice and fresh too.

BSWOMAN: As an option you could be castrated and be sacred eunuchs.

BOTH: (ad lib) Oh, that's all right. . . I think the cow manure is enough. . .

BSWOMAN: We won't forget this. Thank you.

CANNAPHLIT: Our pleasure.

BSWOMAN: Don't spread that all in one place. (Businesswoman exits.)

GORPH: Tower to God, huh. Easier than I thought.

CANNAPHLIT: (lifting up his bag of manure) This is where thinking'll get you!

GORPH: So listen. Now we found God - you wanna invent the wheel?

CANNAPHLIT: Yeah. What's a wheel?
```

---

## IC-0974: The Ballad of George Zimmerman

- Title: The Ballad of George Zimmerman
- Author (byline): Dan O’Brien with music by Quetzal Flores
- Work: Facing Our Truth: Short Plays on Trayvon, Race and Privilege
- Publisher: Samuel French, Inc.
- Publication date as stated: July 2015
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, TIME & PLACE, ZIMMERMAN, TRAYVON, OFFICER
- Teaser before the introduction: Yes
- Spoken words (computed): 1016
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dan O’Brien with music by Quetzal Flores
Book: Facing Our Truth: Short Plays on Trayvon, Race and Privilege
ISBN: 978-0573704260
Publisher: Samuel French, Inc.
Date (Month/Year): July 2015
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: On February 26, 2012, Trayvon Martin, a Black teen walking home from a convenience store, is shot and killed by George Zimmerman, a neighborhood watch volunteer patrolling a townhouse community of Sanford, Florida.

ACTOR 2: Martin was just a teenager on the phone with a girl, carrying a bag of Skittles and an iced tea. But he was viewed by Zimmerman, whose father was white and whose mother was Hispanic, as scary, out of place, on drugs – someone who needs to be confronted, interrogated and put in his place.

ACTOR 1: This selection explores the mind of Trayvon Martin’s killer . . .

TOGETHER: The Ballad of George Zimmerman by Dan O’Brien with music by Quetzal Flores
```

### Performance text (classify this)

```text
CHARACTERS:
• ZIMMERMAN - Late 20s, would call himself Hispanic.
• TRAYVON - Late teens, would call himself Black.
• OFFICER - Would call herself White.

TIME & PLACE: Most takes place in the rain in a backyard at the Retreat at Twin Lakes in Sanford, Florida, February 26, 2012, a little after 7 p.m.- in the ten minutes or so from George Zimmerman's 911 call until Trayvon Martin's death.

ZIMMERMAN: (On the phone with 911) Hello? Hello?
We've had a few break-ins in the neighborhood,
and here comes this guy looking like he's up to no good.
Looking like he's on drugs or whatever.
It's pouring rain and he's just walking round.
What race is he? - Black.
What's he wearing? A hoodie
and blue jeans, white tennis shoes.

ZIMMERMAN: He's staring at me, at all the houses.
Why's he staring at me? Where am I?
Retreat, Retreat, Retreat, Retreat at Twin Lakes . . .
Retreat, Retreat at Twin Lakes . . .
He's coming towards me with his hand in his waistband.
He's a black guy for sure.
There's definitely something wrong with him.
He's coming back to check me out again with something in his hands.
How long till you get here?
Because these a**holes always get away.
- Now he's running.
Which way's he running?
I'm running after him.
I don't need to do that.
What's my name? George.
Last name Zimmerman.
I don't know where this kid's gone.
Hello? Hello? (ends phone call)

TRAYVON: Why you running after me?

ZIMMERMAN: Why are you here?

TRAYVON: I can't be?

ZIMMERMAN: Why aren't you running in out of the rain?

TRAYVON: I got this hoodie to keep me dry.

ZIMMERMAN: Let me see your face.

TRAYVON: Why?

ZIMMERMAN: You can see mine.

TRAYVON: Barely, barely.

ZIMMERMAN: What's that in your hand?

TRAYVON: Show me yours and I'll show you mine.

ZIMMERMAN: Punks have been stealing.

TRAYVON: What punks?

ZIMMERMAN: Black punks that look like you. It's a fact.

TRAYVON: It's a fact you look like a skinhead, or a pervert of some kind. - That earring, man!

ZIMMERMAN: I'm married, man.

TRAYVON: Not for long.

ZIMMERMAN: If it were light you'd see my face. I'm Hispanic. My mother is Peruvian. Her mother was half-black like you.

TRAYVON: I'm all black, ese.

ZIMMERMAN: Mi abuela watching Sabado Gigante, cooking Papa a la Huancaina.

TRAYVON: *What* is that?

ZIMMERMAN: Potatoes in cream sauce . . . Mmm . . .
I've protested police brutality against the homeless black guys.
I took a black girl to the prom.
I voted for Obama!
Obama, Obama, 'bama, Obama,
Obama, 'bama, Obama, Obama,
'bama, Obama, Obama, 'bama . . .

TRAYVON: Why you acting white then, Zimmerman?

ZIMMERMAN: How do you know my name?

TRAYVON: Is Zimmerman a Jewish name? Zimmerman, Zimmerman, Zimmerman . . .

ZIMMERMAN: I was an altar boy in my youth.
Once even got arrested when I was your age, for punching
this white cop who was trying to shake down
my friend.

TRAYVON: Did you do time?

ZIMMERMAN: My father was the reason.

TRAYVON: The reason?

ZIMMERMAN: The reason I got off: Judge Zimmerman.

TRAYVON: Zimmerman, Zimmerman,
Zimmerman, Judge Zimmerman . . .
Zimmerman, Zimmerman,
that's not why you're here now.

ZIMMERMAN: I had a girl I just could not let go. Came to her house when she called. When she pushed me I pushed her back harder.

TRAYVON: Zimmerman, Zimmerman, Zimmerman, Zimmerman . . . I'm scared of you.

ZIMMERMAN: That's funny. I'm afraid of people like you.

TRAYVON: If you're so afraid then why am I the one who has to run away?

ZIMMERMAN: Because I've got the gun,
because I've got the gun.
One of us is going to die tonight
because I've got the gun.

TRAYVON: Because you've got the gun,
because you've got the gun.
One of us is going to die tonight
because you've got the gun.

ZIMMERMAN: If you carried a gun legally like me, you'd be safe right now.
If you carried guns like this one.
Kel-Tec .9 mm subcompact.
Easy to hide in your underwear.

Not much fun to shoot.
Only a few feet away and I'd miss you.
But when you're on top of me
pounding my head against the stone, I bet my gun's
going to set me free.

TRAYVON: Because you've got the gun,
because you've got the gun.
One of us is going to die tonight
because you've got the gun.
But why you hate me, son?
We should be together on this.
We're both middle-class.

ZIMMERMAN: You live here?

TRAYVON: I'm visiting.

ZIMMERMAN: No, I'm nothing like you!
A hood. Drooping pants.
Been expelled five times in one year.
Jewelry in the bag at school.
Where's your mother? Where's your father?
Where's your God damned respect?
Why you smoking dope and bragging about it?
Why the golden teeth?
[TRAYVON is shot.]
Why can't you try just a bit harder to be me?

TRAYVON: Zimmerman. A wannabe white man!

ZIMMERMAN: Zimmerman, Zimmerman, Zimmerman, Zimmerman . . .

TRAYVON: Zimmerman, Zimmerman, Zimmerman, Zimmerman . . .

ZIMMERMAN: Because I've got the gun. . .

TRAYVON: Now is when I run at him. . .

ZIMMERMAN: Because I've got the gun. . .

TRAYVON: And pop his nose like a balloon . . .

ZIMMERMAN: One of us is going to die tonight. . .

TRAYVON: A punching and a kicking .

ZIMMERMAN: Because I've got the gun .

TRAYVON: Help! Help!

ZIMMERMAN: Because I've got the gun . . .

TRAYVON: Help! Help! S***! . . .

ZIMMERMAN: One of us is going to die tonight . . .

TRAYVON: Help! Help! Help! Help!

ZIMMERMAN: Because I've got the gun . . . TRAYVON. Help! Help! Help!

ZIMMERMAN: Because I've got the gun . . .

TRAYVON: Help! Help!

ZIMMERMAN: Because I've got the gun . . .

TRAYVON: Help! Help!

ZIMMERMAN: One of us is going to die tonight. . .

TRAYVON: Help . . . !

ZIMMERMAN: Because I've got the gun . . .

*****scene****** The OFFICER arrives. She carries Zimmerman’s gun. The Officer's song at the end reveals that we've been in George Zimmerman's head all along. For the literal-minded, perhaps Zimmerman is getting his gun back at the courthouse.

OFFICER: Zimmerman. Zimmerman, you're free. You're free to go. Your house arrest is over. A jury of women ruled you did your best.

It's a crazy old mixed-up world.
Hello? Hello? Zimmerman, you seem distracted.
Give us the bracelet from round your ankle, and we'll give you back this gun.
The Equalizer. This Kel-Tec . 9 mm subcompact.
Easy to hide in your underwear.
Not much fun to shoot. Only a few feet away and I'd miss you.
But when you're on top of me
pounding my head against the stone, I bet this gun would set me free .
But Zimmerman, poor innocent Zimmerman . . .
These a**holes always get away.
Not this time. Not this time, right Zimmerman?
```

---

## IC-0975: Bent

- Title: Bent
- Author (byline): Martin Sherman
- Work: Not specified
- Publisher: Applause Theatre Books
- Publication date as stated: May 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: RUDY, MAX, OFFICER, HORST, CAPTAIN
- Teaser before the introduction: Yes
- Spoken words (computed): 2367
- Already set (do not supply): none

### Source block (context only)

```text
Author: Martin Sherman
ISBN: 978-1557833365
Publisher: Applause Theatre Books
Date (Month/Year): May 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: In Bent, Martin Sherman tells a Holocaust story that no one had ever told before –

ACTOR 2: The story of the persecution of homosexuals -- the lowest of the low in the concentration camp pecking order.

ACTOR 1: The wearers of the Pink Triangle

ACTOR 2: Written in 1979 the struggle of Max to accept himself, to learn to love in the most unlikely of places, still carries meaning today.

TOGETHER: Bent by Martin Sherman

RUDY screams again as stage is set for next scene [Scream during transition to Character of Horst] MAX moves, as if to get up.

[The man wearing the pink triangle (HORST) moves toward MAX. He touches him.]

HORST: (Pg 42-43) Don't. [He removes his hand from MAX and looks straight ahead. The GUARD

walks through the circle of light.] Don't move. You can't help him. Silence. The GUARD walks

through the circle of light.]
```

### Performance text (classify this)

```text
Suggested Roles: ACTOR 1: Rudy / Horst ACTOR 2: Max / Officer / Captain

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

CUTTING NOTES are in RED; STAGE DIRECTIONS from the PLAY are in BLUE. [RUDY and MAX crouched on the ground] A prisoner transport train. A GUARD walks through the circle of light. He carries a rifle. [RUDY and MAX watch as GUARD crosses – actors should coordinate eye moment to give the illusion there is a GUARD] Silence.

RUDY: (Pg 40-41) Where do you think they're taking us? [Silence. The other prisoners look away The GUARD walks through the circle of light. Silence.] [To the PRISONER next to him] Did you have a trial? [The PRISONER doesn't answer.]

MAX: Rudy . . . I . . . . [Silence]. RUDY and MAX look at each other. They are both terrified. RUDY starts to extend his hand, then withdraws it. A scream is heard-off, beyond the circle. [Characters respond physically to the sound] RUDY and MAX look at each other, then turn away. Silence. Max assumes the role of OFFICER and walks through the circle of light. Silence. Another scream. [Rudy responds physically to the sound] Silence. The OFFICER looks at the prisoners one by one. He stops at RUDY.]

OFFICER: Glasses. [Silence.] Give me your glasses. [RUDY hands the OFFICER his glasses. The OFFICER examines them.] Horn-rimmed. Intelligensia.

RUDY: What?

OFFICER: [Smiles.] Stand up. [Pulls RUDY up.] Step on your glasses. [RUDY stands-petrified.] Step on them. [RUDY steps on the glasses.] Take him.

RUDY: Max! [RUDY looks at MAX. The OFFICER pushes RUDY off-out of the circle. The OFFICER smiles.]

OFFICER: Glasses. [He kicks the glasses away]. Exits . . . MAX resumes his original role MAX stares ahead. A scream is heard-off, beyond the circle. RUDY'S scream. MAX stiffens. Silence. RUDY screams again.

MAX: This isn't happening. Where are they taking us?

HORST: It's happening. Dachau. I've been through transport before. They took me to Cologne for a propaganda film. Pink triangle in good health. Now it's back to Dachau.

MAX: Pink triangle? What's that?

HORST: Queer. If you're queer, that's what you wear. If you're a Jew, a yellow star. Political-a red triangle. Criminal-green. Pink's the lowest. [He looks straight ahead].

MAX: This isn't happening. [Silence.] This can't be happening. [Silence.]

HORST: Listen to me. If you survive the train, you stand a chance. Here's where they break you. You can do nothing for your friend. Nothing. If you try to help him, they will kill you. If you try to care for his wounds, they will kill you. If you even see -- see what they do to him, hear -- hear what they do to him -- they will kill you. If you want to stay alive, he cannot exist. *****SCENE: At the prisoner camp, Dachau***** [A tight little corner at the end of the barracks. HORST crawls in and sits huddled with his bowl. He drinks the soup. MAX enters, crawling in next to HORST. He carries a bowl. He wears the prison uniform. On it is a yellow star.]

MAX: (Pg 50-57) Hi. [HORST looks at him; says nothing; MAX holds up his bowl.] Here.

HORST: Leave me alone.

MAX: I got extra. Some vegetables. Here. [Drops vegetables from his bowl into HORSTS]

HORST: Thanks. [They eat in silence. HORST stares at MAX'S uniform.] Yellow star? Jew?

MAX: Oh. Yeah.

HORST: I wouldn't have figured it. [Silence.] I'm sorry about your friend.

MAX: Who?

HORST: Your friend.

MAX: Oh. [Silence.] [Points to HORST'S pink triangle.] How'd you get the pink?

HORST: I signed a petition. . . for Magnus Hirschfeld.

MAX: Oh yeah. I remember him. Berlin. He wanted to. . .

HORST: Make queers legal. Looked like he would, too, for a while. It was quite a movement. Then the Nazis came in. Well. I was a nurse. They said a queer couldn't be a nurse. Suppose I had to touch a patient's penis! God forbid. They said rather than be a nurse, I should be a prisoner. A more suitable occupation. That's how I got my pink triangle. How'd you get the yellow star?

MAX: I'm Jewish.

HORST: You're not Jewish, you're a queer. [Silence.]

MAX: I didn't want one. You told me it was the lowest. So I didn't want one. I worked a deal.

HORST: A deal? With the Gestapo? You're full of shit. [Silence.]

MAX: I'm going to work a lot of deals. They can't keep us here forever. Sooner or later they'll release us. I'm only under protective custody, that's what they told me. I'm going to stay alive.

HORST: I don't doubt it. Thanks for the vegetables. [Starts to crawl away.]

MAX: Where are you going?

HORST: To sleep. We get up at four in the morning. I'm on stone detail.

MAX: Don't go. . . I'm not Jewish.

HORST: Then why are you wearing that?

MAX: You told me pink was the lowest.

HORST: It is, but only because the other prisoners hate us so much.

MAX: I got meat in my soup. You didn't. . . . You didn't think I'd make it, did you? Off the train?

HORST: I wasn't sure.

MAX: I'm going to stay alive. Because of you. You told me how.

HORST: Yes. [Pause.] I did. [Pause.] You should be wearing a pink triangle.

MAX: I made a deal. They said if I . . . I could prove . . .

HORST: What? [Silence.]

MAX: They took me . . . into that room . . . on the train. And they said. . . prove that you're not. . .

HORST: Prove that you're not what?

MAX: Queer.

HORST: How?

MAX: They said, if you. . . Made love.

HORST: Who was she?

MAX: Maybe . . . maybe only thirteen . . . she was dead. Just. Just dead, minutes [MAX indicates a gun at the temple] They said prove that you're. . . and I did. . . lots of them, watching. . . laughing. . . He's a bit bent, they said, he can't . . . but I did . . . I wanted . . .

HORST: To stay alive.

MAX: She was like an angel . . . to save my life . . . [Silence.] And I said, I'm not queer. And they laughed. And I said, give me a yellow star. And they said, sure, make him a Jew. He's not bent. And they laughed. But. . . I. . . got. . . my. . . star.

HORST: Yes. [Reaches out, touches MAX'S face.]

MAX: Don't do that! [Pulls away.] You mustn't do that. For your own sake. You mustn't touch me. I'm a rotten person. *****Scene: Max uses his “deals” to get Horst moved to rock detail*****

MAX: (Pg 63-65) You see those. . . You take one rock at a time. And move it over there. And then when the entire pile is over there, you take one rock at a time, and move it back.

HORST: [Looks at MAX. Silence.] And move it back? We move the rocks from there to there, and then back from there to there? Why?

MAX: Start moving. He's watching. [MAX continues to move rocks. HORST does the same. They do so in different rhythms, at times passing each other.] It's supposed to drive us crazy. It makes no sense. It serves no purpose. I figured it out. They do it to drive us crazy.

HORST: They probably know what they're doing.

MAX: But it doesn't work. I figured it out. It's the best job to have. That's why I got you here.

HORST: What? [Puts down his rock.]

MAX: Don't stop. Keep moving. [HORST picks up the rock and moves it.] A couple more things. That fence. It's electric. Don't touch it. You fry. And over there-that pit.

HORST: Oh yes. It smells awful.

MAX: Bodies. Sometimes we have to throw them in.

HORST: Oh. Well, it will break the routine. (Pg 68-71) Where do the bodies come from?

MAX: The fence. The hat trick. Sometimes a guard throws a prisoner's hat against the fence. He orders him to get the hat. If he doesn't get the hat, the guard will shoot him. If he does get the hat, he'll be electrocuted.

HORST: I'm really going to like it here. Thanks a lot.

MAX: I'm really doing you a favor.

HORST: Some favor! You just want someone to talk to so you won't go crazy. And I'm the only one who knows your secret.

MAX: What secret?

HORST: That you're a pink triangle.

MAX: No. I'm a Jew now.

HORST: You are not. It's a lie.

MAX: It's a smart lie. I thought you'd be grateful.

HORST: I'm not grateful. I liked cutting stones. This is insane. Twelve hours of this a day? I'll be nuts in a week.

MAX: You haven't figured out this camp, that's all. You don't know what's good for you. This is the best job to have.

HORST: Moving rocks back and forth for no reason. Next to a pit with dead bodies and a fence that can burn you to dust. The best job to have? [They both move their rocks. A long silence.]

MAX: I thought you'd be grateful. *****Scene: Same work detail . . . months later*****

HORST: (Pg 86) I'm going crazy. [Silence.] I'm going crazy. [Silence.] I'm going crazy. I dream about rocks. I close my eyes and I'm moving rocks. Rocks never end. Never end. [Silence.] I'm going crazy.

MAX: Think of something else.

HORST: I can't think. I've been up all night. Didn't you hear? Our barracks had to stand outside all night. We stood at attention all night long . . . Punishment.

MAX: What for?

HORST: Someone in our barracks killed himself.

MAX: A moslem?

HORST: (Pg 74) No. That's what they call a dead person who walks. You know, one of those guys who won't eat anymore, won't talk anymore, just wanders around waiting to really die. (Pg 86- 93) It doesn't mean anything if a moslem kills himself, but if a person who's still a person commits suicide, well . . . it's a kind of defiance, isn't it? They hate that -- it's an act of free will.

MAX: I'm sorry.

HORST: Sure. Yellow star is sorry. [Silence.] I'm going crazy.

MAX: O.K. O.K. You're going crazy. I'm sorry. It's my fault.

HORST: What do you mean your fault?

MAX: For bringing you here. Because you make me feel so guilty. And you should. This job is the worst. I figured it wrong. I'm sorry.

HORST: You should be with us, where you belong.

MAX: No. But you shouldn't be here.

HORST: I want to be here.

MAX: Why?

HORST: Because. Because I love rocks. [Pause.] Because I love you. [Silence.] I do. I love you. When I'm not dreaming about rocks, I'm dreaming about you. For the past six weeks, I've dreamed about you. It helps me get up. It helps me make sure my bed is perfectly made so I'm not punished. It helps me eat the stinking food. It helps me put up with the constant fights in the barracks. Knowing I'll see you. At least out of the corner of my eyes. In passing. It's a reason to live. So I'm glad I'm here. [MAX is at one pile of rocks, moving them into symmetrical piles.]

HORST: What are you doing?

MAX: Arranging these neatly. We've gotten sloppy. They can beat you for it. [Silence.] Don't love me.

HORST: It's my secret. And I have a signal. No one knows it. When I rub my left eyebrow at you, like this ... [Rubs his left eyebrow.] ... it means I love you. Bet you didn't know that. I can even do it in front of the guards. No one knows. It's my secret. [Starts to cough.] It's cold.

MAX: Don't love me. I don't want anybody to love me. I can't love anybody back.

HORST: Who's asking you to?

MAX: Queers aren't meant to love. I know. They don't want us to. You know who loved me? [That boy . . . on the train. ] I don't remember his name. But I killed him. See -- queers aren't meant to love. I'll kill you too. Hate me. That's better. Hate me. Don't love me. [MAX finishes arranging the rocks. He returns to moving the rocks. Silence. HORST starts to cough again. Slips. Drops the rock and falls to the ground.]

MAX: Horst! [Puts down his rock.]

HORST: Shit. [MAX starts toward him.] Don’t move! He's watching. The guard. If you help me, they'll kill you. Get back to your rock. Do you hear me, get back! [MAX returns, picks up his rock, but stands looking at HORST; HORST is coughing] Move! [MAX moves the rock.] Don't ever help me. [Pulls himself up.] I'm up. It's O.K. [Picks up his rock.]Never notice. Never watch. I love you. But I won't help you if you fall. Don't you dare help me. We save ourselves. Do you understand? Do you?

MAX: Yes. I understand.

HORST: Promise me. Come on. Promise me. We save ourselves.

MAX: (Pg 96-97) You're losing weight. You need medicine.

HORST: It doesn't matter.

MAX: You're turning into a moslem. I'm scared. *****Scene: Same work yard ***** [MAX assumes the role of CAPTAIN as HORST resumes moving rocks.] The CAPTAIN watches HORST. He paces up and down. HORST moves the rocks. The CAPTAIN paces. HORST coughs. He catches himself and tries to stifle it.]

CAPTAIN: (Pg 112-117) Ah. [HORST stops the cough.] You. Pervert.

HORST: [Stiffens, stands still.] Yes sir?

CAPTAIN: Are you ill?

HORST: No sir.

CAPTAIN: You have a cough. I heard you cough. You're not well.

HORST: I am, sir.

CAPTAIN: Put down that rock.

HORST: Yes sir. [Puts down the rock.]

CAPTAIN: Good. Now take off your hat.[A long pause.]

HORST: My hat, sir?

CAPTAIN: Yes. Your hat. [HORST removes his hat]

CAPTAIN: Throw your hat away. [HORST flings his hat on the ground.] Not there. Pick it up.

HORST: Yes sir. [Picks up his hat.]

CAPTAIN: Throw it on the fence. The fence. [HORST starts to cough.] That's all right. We'll wait. [The cough subsides.] Are you better?

HORST: Yes sir.

CAPTAIN: Nasty cough. On the fence. Now.

HORST: On the fence. Yes sir. [HORST throws his hat on the fence. The fence sparks.]

CAPTAIN: Get your hat. [The CAPTAIN points his rifle at HORST.]

HORST: [Is silent for a moment. Turns to the CAPTAIN] Yes sir.

[HORST turns left, takes his hand and rubs his left eyebrow. He turns and stares at the CAPTAIN. The CAPTAIN waits. HORST turns toward the fence. He starts to walk very slowly to his hat. He almost reaches the fence, when, suddenly- He turns and rushes at the CAPTAIN. He screams in fury. The CAPTAIN shoots HORST. He falls, dead. Silence.] *****SCENE: Max and Horst’s dead body*****

MAX stares at HORST. Silence. MAX opens his mouth to cry out. He can't. Silence. MAX walks to HORST'S body.

MAX: (Pg 119-120) Nol [He looks up-off-at the GUARD, then back at HORST. Silence.] You don't have to worry about the rocks. I'll do yours, too. I'll move twice as many each day. I'll do yours, too. You don't have to worry about them. [Silence.] You know what? [Silence.] Horst? [Silence.] You know what? [Silence.] I think I love you. [Silence.] Shh! Don't tell anyone. I love you. [Silence.] What's wrong with that? [He starts to cry.]
```

---

## IC-0976: Birdcage: The Shooting Script

- Title: Birdcage: The Shooting Script
- Author (byline): Elaine May
- Work: Not specified
- Publisher: Newmarket Press
- Publication date as stated: June 1999
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR2, ALBERT, ARMAND, AGADOR, MAN
- Teaser before the introduction: Yes
- Spoken words (computed): 914
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
ACTOR 1: Armand and Albert are in a committed,

ACTOR 2: although un-conventional,

ACTOR 1: relationship.

ACTOR 2: 95 percent of the time they don’t worry about how they are viewed by the world.

ACTOR 1: They are comfortable as the owner and star of the Birdcage,

ACTOR 2: a drag club with a fantastic stage show!

ACTOR 1: But when Armand's son springs wedding plans on them, their unconventional life must suddenly appear to be quite conventional.

ACTOR 2: The potential in-laws are the ultraconservative Republican Senator Kevin Keeley and his wife Louise.

ACTOR 1: In this selection Albert tries his best to vanquish his inner drag queen.

TOGETHER: Birdcage: The Shooting Script by Elaine May.
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

CHARACTERS – SUGGESTED ROLES:

ACTOR 1: Albert, the Man

ACTOR2: Armand, Agador

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

ARMAND: My God! What a brilliant idea. (p. 7, scene 9) TRANSITION

ACTOR 1: And as if the pressure of the nightly drag-extravaganza isn’t enough . . . Armand soon reveals some new news. News that only adds to Albert’s stress level . . .

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

ARMAND: No actually I was talking to the a**h*** behind you. (p. 50, scene 59) Pantomime fight scene ensues between Armand and “the Man” (freeze fight scene, then Actor 1 steps out for transition)

TRANSITION

ACTOR 1 as ALBERT: Well . . . who would have expected that! These MEN . . . they think that fighting is the answer to everything! (Heavy sigh)

Albert re-enters scene, with Armand the obvious loser of the fight . . .

ALBERT: See the swelling’s already gone down. It’s nothing. Very masculine. That big idiot looked so ridiculous when he sat on you and banged your head into the ground. He didn’t even know how to box. Are you all right? (p. 50, scene 60)

ARMAND: I hurt my thumb. (p. 9, scene 10)

ALBERT: Oh, my god! Forgive me? (p. 9, scene 10)

ARMAND: No, no forgive me, my little roundness. My teddy bear. (p. 9, scene 10)

ALBERT: My king! (p. 9, scene 10)

ARMAND: My queen! (p. 9, scene 10)
```

---

## IC-0977: The Book of Mormon (PG-13 Version)

- Title: The Book of Mormon (PG-13 Version)
- Author (byline): Trey Parker, Robert Lopez and Matt Stone
- Work: Not specified
- Publisher: Newmarket Press
- Publication date as stated: June 2011
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ELDER PRICE, ELDER CUNNINGHAM, PRICE AND CUNNINGHAM, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1870
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
ACTOR 1: The Book of Mormon ACTOR 2: by Trey Parker, Robert Lopez and Matt Stone
```

### Performance text (classify this)

```text
SUGGESTED BREAK DOWN OF CHARACTERS SHOWN BY (1) or (2) for characters other than Elder Price (1) and Elder Cunningham (2)

Actor 1: Narrator, Voice, Elder Price, Lion King Character, Nabulungi, Middala, Sadaka, Mutumbo, Mission President, The General, Ugandan 2

Actor 2: Mormon, Jesus, Moroni, Elder Cunningham, Mafala, Kalimba, Joseph Smith, Ugandan 1

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NARRATOR (1): (Pg 1) Long ago, in the year of our Lord 326 AD, a great prophet is leader of the Nephite people in ancient Upstate New York. His name . . . is Mormon.

MORMON (2): I am Mormon. My people sailed here from Israel to create a new civilization. These golden plates tell of our people and how we met . . . with Jesus Christ. (Christ appears to Mormon)

JESUS (2): I am Jesus. Take care of your golden plates, Mormon, for soon, your entire civilization will be gone and nobody will remember you. (Christ leaves)

NARRATOR (1): Just before the Nephite people were wiped out, Mormon gave the plates to his son, Moroni.

MORONI (2): I am Moroni, the last of my kind. I shall bury the golden plates, father, and perhaps one day, someone very special will find them . . .

NARRATOR (1): And lo, Moroni buried the golden plates high on a hill. Centuries later the golden plates were found, giving birth to the fastest growing religion today! A church that sends missionaries out . . . All over the world . . . Elder Price, a young missionary in a white shirt and black tie, holding the book of Mormon pantomimes ringing a doorbell (Ding Dong)

ELDER PRICE: Hello! My Name is Elder Price, and I would like to share with you the most amazing book.

ELDER CUNNINGHAM: (Pg 4) Hello! My Name is Elder Cunningham. Would you like to change religions, I have a free book written by Jesus!

VOICE (1): No, No, Elder Cunningham! That’s NOT how we do it. You’re making things up again. Just stick to the approved dialogue.

ELDER CUNNINGHAM: Hello! My Name is Elder Cunningham, and we would like to share with you this book of Jesus Christ.

PRICE AND CUNNINGHAM: You simply won’t believe how much this book will change your life!

VOICE (1): (Pg 5) Elders, you have been training for three months and you are now . . READY TO GO OUT AND SPREAD THE WORD! In a moment you will be assigned your mission companions and locations!

ELDER PRICE: (to audience) The most important time of a Mormon kid’s life is his mission. I know my mission will be something incredible. VOICE (1): (Pg 9-10) Elder Price? Your brother will be . . . Elder Cunningham!

ELDER CUNNINGHAM: That’s! That’s ME! (He struts to Price and gives a big dorky wave) HELLO!!!!! (Price is less than enthused)

VOICE (1): And your mission location is . . . UGANDA!!!!! (Price looks visibly upset.)

ELDER CUNNINGHAM: UGANDA! COOL! WHERE IS THAT?!

VOICE (1): AFRICA!

ELDER CUNNINGHAM: Oh BOY – Like Lion King! LION KING CHARACTER (1): (Pg 13) Hey Na Da Hey Na! Aya Bubbu Taya Tayaaaaaaaaa! VOICE (1): (Pg 11) Alright Elders, go home and pack your things! Tomorrow, your missions begin! (Price looks a little uncomfortable. Cunningham looks thrilled) ***** The boys arrive in Uganda ***** The boys enter. They look around in horror at the poverty they see. MAFALA (2): (Pg 17-18) (Big and happy) AHHH! There you are! I have been looking for you! I am Mafala Hatimbi. I’ve been hired to show you to your building.

ELDER PRICE: Oh, thank goodness! Some men took our bags!

MAFALA (2): In this part of Africa, we ALL have a saying – whenever something bad happens, we just throw our hands up to the sky and say HASA DIGA EEBOWAI!

ELDER CUNNINGHAM: Hasa Diga Eebowai?

MAFALA (2): It’s the only way to get through all these troubled times. There’s war, famine . . . but having a saying makes it all seem better . . . . There’s isn’t enough food to eat.

UGANDAN (1): Hasa Diga Eebowai!

MAFALA (2): People are starving in the street.

UGANDAN (1): Hasa Diga Eebowai!

ELDER CUNNINGHAM: Does it mean no worries for the rest of our days?

MAFALA (2): Kind of! We’ve had no rain in several days.

UGANDAN (1): Hasa Diga Eebowai!

MAFALA (2): And eighty percent of us have aids.

UGANDAN (1): Hasa Diga Eebowai!

ELDER PRICE: (Pg 19) Excuse me, what EXACTLY does that phrase mean?

MAFALA (2): Well, let’s see . . “Eebowai” means “God”, and “Hasa Diga” means (whispers behind a closed hand)

ELDER PRICE: WHAT???

ELDER CUNNINGHAM: (chanting and dancing) Hasa diga Eebowai! Hasa diga Eebowai! Hasa diga Eebowai! (continues)

ELDER PRICE: (Pg 22) (overlapping) Elder Cunningham. Elder Cunningham. Stop – Don’t say it! It means something very bad. (whispers behind a closed hand)

ELDER CUNNINGHAM: Holy Moly! I said it like thirteen times!

**** Mafala’s daughter takes the boys to their living quarters ***** NABULUNGI (1): (Pg 22-23) This is where my father asked me to bring you. The others like you should be inside.

ELDER CUNNINGHAM: Thank you, Jon Bon Jovi.

ELDER PRICE: (giving Cunningham a look) We appreciate your help, Nabulungi. Look, uh, maybe sometime, Elder Cunningham and I could . . . Sort of tell you a little about the Church of Jesus Christ of Latter-Day Saints.

NABULUNGI (1): I have to get back to the village. But I am always there – if you want to talk to me. (She turns to go but then turns back) Just one piece of advice. No matter how hot you get at night, keep your windows closed. It is the only way to protect against the scorpions. And the mosquitoes. And the lions. And the murderers and the AIDS and the safari ants which plant their eggs under your skin and eat you from the inside out. (She walks away-the boys respond non-verbally)

ELDER PRICE: (big sigh, wipes his brow) Oh, man, can you believe this? (Pg 31) This is going to be a whole lot harder than we thought. ***** (Sceen change - Later that week in a session with the tribespeople) *****

ELDER PRICE: (Pg 34-35) We would like to tell you all about a very special book.

UGANDAN (1): (major disappointment) Awww. . .

NABULUNGI (1): We all have heard of the Bible. People come and tell us about Jesus and him dying for our sins once a year!

KALIMBA (2): They come, tell us the story and then leave. Nothing gets better. Your bible doesn’t work.

ELDER PRICE: Those were Christian missionaries. We’re Mormons!

NABULUNGI (1): What’s the difference?

ELDER PRICE: I’m gonna take you back to Biblical times, 1823. An American man named Joe livin’ on a farm in the Holy Land of Rochester New York! (Cunningham steps forward like he’s doing an infomercial, over-acting)

ELDER CUNNINGHAM: You mean the Mormon prophet Joseph Smith?

ELDER PRICE: That’s right, that young man spoke to God.

ELDER CUNNINGHAM: He spoke to God?

ELDER PRICE: And God said, “Joe, people really need to know that the Bible isn’t two parts. There’s a part three to the Bible, Joe! And I, God, have anointed you to dig up this part three, which is buried by a tree on the hill in your backyard.”

ELDER CUNNINGHAM: Wow, God says, “Go to your backyard and start digging”? That makes perfect sense! (Pg 36) Wow! The Bible is actually a trilogy, and Book of Mormon is Return of the Jedi?! I’m interested.

ELDER PRICE: Now, many people didn’t believe the prophet Joseph Smith. JOSEPH SMITH (2): (Pg 37) I speak to God all the time and he’s told me to head west! So I’ll take my part three to the Promised Land. Paradise! On the west coast.

ELDER PRICE: Now, on the way to the Promised Land, Joseph was shot by an angry mob. (Pg 40) The Prophet Joseph Smith died. But his followers, they kept heading west. And Brigham Young led them to a sparkling land in Utah they named SALT LAKE CITY. And there the Mormons multiplied! And made big Mormon families!! Alright, now who would like their very own copy of the Book of Mormon?? (All the Ugandan people look at each other for a beat and then walk away making groans and “blow off” gestures.”)

ELDER CUNNINGHAM: If you order now, we’ll also throw in a set of steak knives!

ELDER PRICE: What were you doing?! There’s nothing in the Book of Mormon about steak knives!

ELDER CUNNINGHAM: I’m sorry. I actually never read it. It’s so boring!

ELDER PRICE: (Pg 44) Africa is nothing like The Lion King. (dejected) There is nothing I can accomplish here! (Price walks away. Cunningham is not sure what to do or where to go). NABULUNGI (1): (Pg 46) There you are! Thank goodness I found you! Where is your friend?

ELDER CUNNINGHAM: (sadly) I don’t have any friends.

NABULUNGI (1): Please come back to the village. We are ready! We’re ready to listen. YOU can lead us. Teach us everything about the Book of Mormon. ***** Scene change – Elder Cunningham is alone, preaching to the Ugandans*****

(Cunningham is reading from the book of Mormon. He is trying to be a preacher, but really doesn’t have what it takes)

ELDER CUNNINGHAM: (Pg 53) (reading with vigor) And it came to pass that the NEPHITES had gathered together a great number of men! And they did have a number of battles, in which the Nephites did beat the Lamanites and did slay many of them! (Cunningham seems to finish – the Ugandans just stare at him) Uh . . . that MEANS . . you know . . . You should . . be NICE to each other or something. (Pg 54) Let’s skip to another part . . .

(Cunningham turns and flips through the pages)

MIDDALA (1): THREE HOURS we been listening to him talk about STUPID [STUFF] that happened on the other side of the Earth thousands of years ago! IT has nothing to do with US!

SADAKA (1): That’s right! Those “NEPHITES” probably didn’t even have AIDS to deal with!

ELDER CUNNINGHAM: UH, SURE THEY DID! SURE THEY DID!! People back then had even WORSE AIDS! (Everyone quiets down and listens to him) Yeah! (Cunningham pretends to look through the Book of Mormon, and then pretends to read from it) And LO! The Lord said unto the Nephites – I know you’re really depressed, with all your AIDS and everything . . . But there is an answer in Christ! (The Ugandans look surprised, but they are now paying attention)

NABULUNGI (1): You see?! This book CAN help us! NARRATOR (CHORUS) (1): (Pg 58) You’re making things up again, Arnold. You’re recklessly warping the words of Jesus!

ELDER CUNNINGHAM: (Pg 71) (with more confidence) And so, yeah, so then Christ said to the Nephites, “Be strong!” You know?! “Just because Lamanites got big Death Star weapons and stuff doesn’t mean they should ruin your lives! There’s more of you than there are of them, you know? You should always . . . stand up for yourselves,” Christ said.

MIDDALA (1): Jut like the way the Hobbits all stood up to Bringham Young’s killers! ****** MISSION PRESIDENT (1): (Pg 75) (reading a letter) Dear Mission President, it is my HONOR to inform you that the elders of Uganda District 9 have brought TWENTY NEW MEMBERS into the church . . . and our numbers continue to grow! (No longer reading) This is outstanding! [Elder Cunningham] has converted more Africans than any district in the COUNTRY! *******

ELDER CUNNINGHAM: (Pg 77) (reading a letter) It’s AMAZING. The mission president wants to meet ME personally! He’s going to give me a MEDAL!

ELDER PRICE: (Pg 80) Well, well . . If it isn’t the SUPER MORMON. Tell me how it is that YOU converted ALL those people into Mormons. (Pg 89-90) Joseph Smith dying of dysentery? Moroni from the Starship Enterprise? A bunch of made-up stuff (beat)

ELDER CUNNINGHAM: (about to cry) Boy . . . I really did it this time, huh? I mean . . . I’ve always been a screw up, but THIS –

ELDER PRICE: Wait a minute . . . You little SNEAK!

ELDER CUNNINGHAM: (confused) What?

ELDER PRICE: I thought I could fly in here and change everything. But I made it all about ME. While I was losing faith, you went and did something incredible. . . for a people who were unreachable – but then they were happy and hopeful . . . It doesn’t matter if the stories are true or not. That isn’t the point . . . ******

THE GENERAL (1): There have been RUMORS that the people in this village are uniting to oppose me! MUTUMBO (1): (Pg 91-92) Yes, we have been shown another way!

THE GENERAL (1): There is ONE LAW you will obey here, and it is MINE!

MIDDALA (1): We believe in something ELSE!

ELDER CUNNINGHAM: Excuse me, everyone . . .

ELDER PRICE: You might as well PUT THAT GUN DOWN BECAUSE IT WILL NOT WORK. And if you do not get out of this village he WILL command the angel Moroni, on the death Star, to unleash the Kraken! Which will then . . . . Uh . .

ELDER CUNNINGHAM: Which will then – fire Joseph Smith torpedoes from its mouth of Christ!

ELDER PRICE: Oh – don’t think he can’t do it! (The General runs off) We are Latter-Day Saints. ALL of us. Even if we change some things, or break the rules, or doubt that God exists . . . We can still work together to make THIS our paradise. ***** The Ugandans pair up and go door to door spreading the word of Arnol ***** The Ugandans appear wearing white shirts and black ties MUTUMBO (1): (Pg 97-98) Hello! My name is elder Mutumbo! And I would like to share with you the most amazing book!

UGANDAN 1 (2): You’ve read the book of Mormon . . . Did you know there’s more?

UGANDAN 2 (1): Part four! Have you heard the story of our prophet Arnold Cunningham?

ELDER CUNNINGHAM: Hello! We can fully guarantee you that . . . .

TOGETHER: This book will change your life. This book will change your life. This book will change your life. The book of ARNOLD. Hello! LION KING CHARACTER (1): (Pg 13) Hey Na Da Hey Na! Aya Bubbu Taya Tayaaaaaaaaa!
```

---

## IC-0978: The Boy in the Striped Pajamas

- Title: The Boy in the Striped Pajamas
- Author (byline): John Boyne
- Work: Not specified
- Publisher: David Fickling Books
- Publication date as stated: Oct 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SHMUEL, BRUNO, SCHMUEL, BURNO, BRUO
- Teaser before the introduction: Yes
- Spoken words (computed): 1731
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Boyne
ISBN: 978-0385751537
Publisher: David Fickling Books
Date (Month/Year): Oct 2007
```

### Introduction (context only: never use it for content warnings)

```text
AAC CTOR 1: This is the story of an event seared into the fabric of history.

ACTOR 2: It is a fable told through the voice of a child . . . but it is not for children.

ACTOR 1: The year is 1943. Bruno is 9-years-old and is quite unaware of a place called Auschwitz and the fate of the Jews where were sent there. All he knows is that his father is a soldier.

ACTOR 2: Shmeul is also 9, but lives on the other side of the fence. They form a friendship that crosses dangerous boundaries and can only end in tragedy.

ACTOR 1: And somehow, events are all the more tragic when narrated by those who do not understand.

TOGETHER: The Boy in the Striped Pajamas by John Boyne
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

SHMUEL: (Pg 126) All I know is this. Before we came here I lived with my mother and father and my brother Josef in a small flat above the store where Papa makes his watches. Every morning while we went to school, Papa mended the watches that people brought to him and made new ones too.

SHMUEL: (Pg 126-128) And then one day things started to change. I came home from school and my mother was making armbands for us and drawing a star on each one. Like this (Draws a Star of David in the air). And every time we left the house, she told us we had to wear one of these armbands.

BRUNO: My father wears one too . . . on his uniform. It’s very nice. It’s bright red with a black-and-white design on it. (Draws a swastika in the air)

SCHMUEL: Yes, but they’re different, aren’t they?

BRUNO: No one’s ever given me an armband.

SHMUEL: But I never asked to wear one.

BRUNO: All the same, I think I’d quite like one. I don’t know which one I’d prefer though, your one or Father’s.

SCHMUEL: We wore the armbands for a few months, and then things changed again. I came home one day and Mama said we couldn’t live in our house anymore.

BRUNO: That happened to me too! The Fury came for dinner, you see, and the next thing I knew we moved here. And I hate it here. Did he come to your house and do the same thing?

SCHMUEL: No, but when we were told we couldn’t live in our house, we had to move to a different part of Cracow, where the soldiers built a big wall and my mother and father and my brother and I all had to live in one room.

BRUNO: All of you? In one room?

SCHMUEL: And not just us. There was another family there and the mother and father were always fighting with each other and one of the sons was bigger than me and he hit me even when I did nothing wrong.

BRUNO: You can’t have all lived in the one room. That doesn’t make any sense.

SCHMUEL: All of us. Eleven in total. (Pg 129-132) Then one day the soldiers all came with huge trucks and everyone was told to leave the houses. Lots of people didn’t want to and they hid, but in the end I think they caught everyone. And the trucks took us to a train and a train . . . . and the train was horrible. There were too many of us in the carriages for one thing. And there was no air to breathe. And it smelled awful.

BRUNO: That’s because you all crowded onto one train. When we came here, there was another one on the side of the platform but no one seemed to see it. That was the one we got. You should have got on it too.

SCHMUEL: I don’t think we would have been allowed. We weren’t able to get out of our carriage.

BRUNO: The doors are at the end.

SCHMUEL: There weren’t any doors.

BRUNO: Of course there were door. They’re at the end. Just past the buffet section.

SCHMUEL: There weren’t any doors. If there had been, we would all have got off. When the train finally stopped, we were in a very cold place and we all had to walk here.

BRUNO: We had a car

SCHMUEL: And Mama was taken away from us, and Papa and Josef and I were put into the huts over there and that’s where we’ve been ever since.

BRUNO: Are there many other boys over there?

SCHMUEL: Hundreds.

BRUNO: Hundreds? That’s not fair at all. There’s no one to play with on this side of the fence. Not a single person.

SCHMUEL: We don’t play. . . . . You don’t have any food on you, do you?

BRUNO: Afraid not . . . perhaps you can come to dinner with us one evening.

SCHMUEL: Perhaps

BRUNO: Or I could come to you. Perhaps I could come and meet your friends.

SCHMUEL: You’re on the wrong side of the fence though.

BRUNO: I could crawl under. (Reaches down and lifts the wire fence off the ground)

SCHMUEL: I have to go back.

BRUNO: Some other afternoon then.

SCHMUEL: I’m not supposed to be here. If they catch me, I’ll be in trouble.

BRUNO: (Pg 133) I’ll come back tomorrow.

NARRATOR (Actor playing Schmuel): (Pg 161) For several weeks the rain was on and off and on and off and Bruno and Schmuel did not see as much of each other as they would have liked.

BRUNO: (Pg 194-196) I thought you weren’t coming any more. I came yesterday and the day before and you weren’t here.

SCHMUEL: I’m sorry. Something happened. . . . Papa. We can’t find him.

BRUNO: Can’t find him? That’s very odd. You mean he’s lost?

SCHMUEL: I suppose so. He was here on Monday and then he went on work duty with some other men and none of them have come back.

BRUNO: And hasn’t he written you a letter? Or left a note to say when he’ll be coming back?

SCHMUEL: No.

BRUNO: How odd. Have you looked for him?

SCHMUEL: Of course I have.

BRUNO: And there was no sign?

SCHMUEL: None.

BRUNO: Well, that’s very strange. But I think there must be a simple explanation. I could ask Father if you wanted.

SCHMUEL: I don’t think that would be a good idea.

BRUNO: Why not? Father is very knowledgeable about life on that side of the fence.

SCHMUEL: I don’t think the soldiers like us. Well, I know they don’t like us. They hate us.

BRUNO: I’m sure they don’t hate you.

SCHMUEL: They do, but that’s all right because I hate them too. I hate them!

BRUNO: You don’t hate Father, do you? (Long pause) Anyway, I have something to tell you too. I’m going back to Berlin. We’re leaving on Saturday.

SCHMUEL: But for how long?

BRUNO: I think it’s forever. Mother doesn’t like it at Out-With (Bruno’s pronunciation of Auschwitz) – she says it’s no place to bring up children – so Father is staying here to work because the Fury has big things in mind for him, but the rest of us are going home.

SCHMUEL: So I won’t see you again?

BURNO: Well, someday, yes. You could come on a holiday to Berlin. You can’t stay here forever after all. Can you?

SCHMUEL: I suppose not. I won’t have anyone to talk to anymore when you’re gone.

BRUNO: (Pg 197-199) I wish we’d got to play together. Just once. Just to remember. We’ve been talking to each other for more than a year and we never got to play once. All this time I’ve been watching where you live from my bedroom window and I’ve never even seen for myself what it’s like

SCHMUEL: You wouldn’t like it. Yours is much nicer.

BRUNO: I’d still like to have seen it.

SCHMUEL: (putting his hand under the fence and lifting a little) Well? Why don’t you then?

BRUNO: But if I was caught I’d be in trouble.

SCHMUEL: That’s true. I suppose I’ll see you tomorrow to say goodbye then.

BRUNO: Unless . . . . Don’t you remember that you said I looked like you? Since I had my head shaved? Well, if that’s the case and if I had a pair of striped pyjamas too, then I could come over on a visit and no one would be any the wiser.

SCHMUEL: Would you do it? You could help me look for Papa.

BRUNO: Why not. The only problem is getting a spare pair of striped pyjamas.

SCHMUEL: That’s all right. There’s a hut where they keep them. I can get some in my size and bring them with me. Then you can change and we can look for Papa.

BRUNO: Wonderful. Then it’s a plan!

NARRATOR (actor playing Schmuel): [The next day, the two boys meet for the last time.] (Pg 202-203) Schmuel lifted the bottom of the fence off the ground and handed a pair of striped pyjama bottoms, a striped pyjama top and a striped cloth cap exactly like the one he was wearing, underneath to Bruno.

BRUNO: Well, turn round. I don’t want you watching me. (Schmuel turns and Bruno changes clothes) When was this last washed?

SCHMUEL: I don’t know if it’s ever been washed. (Bruno finishes changing)

BRUNO: (Pg 204) There, you can turn back now. (They wander into the camp)

NARRATOR (actor playing Schmuel): If it wasn’t for the fact that Bruno was nowhere near as skinny as the boys on [this] side of the fence, and not quite so pale either, it would have been difficult to tell them apart. It was almost as if they were all exactly the same really.

BRUNO: (Pg 205) I’m pretending to be a person from the other side of the fence.

SCHMUEL: A Jew, you mean.

BRUNO: Yes, that’s right. NARRATOR (actor playing Schmuel): (Pg 208) Everywhere [Bruno] looked, all he could see was two different types of people: either happy, laughing, shouting soldiers in their uniforms or unhappy, crying people in their striped pajamas, most of whom seemed to be staring into space as if they were actually asleep.

BRUNO: I don’t think I like it here.

SCHMUEL: Neither do I. NARRATOR (actor playing Schmuel): (Pg 209-210) The two boys spent an hour and a half searching the camp. They weren’t sure exactly what they were looking for, but they didn’t find anything at all that might give them a clue to Shmuel’s papa’s disappearance, and it started to get darker.

BRUNO: I’m sorry, Shmuel. I’m sorry we didn’t find [anything]. I think I ought to go home now. Will you walk back to the fence with me? (Actor playing Schmuel steps behind Bruno and whistles loudly – the whistle is the sound of the solders getting ready to order people on a march). What’s happening? What’s going on?

SCHMUEL: It happens sometimes. They make people go on marches.

BRUNO: Marches! I can’t go on a march. I have to be home in time for dinner. It’s roast beef tonight.

SCHMUEL: Sshhh! Don’t say anything or they get angry.

BRUNO: (Pg 211-213) Does the marching go on for long?

SCHMUEL: I don’t think so. I never see the people after they’ve gone on a march. But I wouldn’t imagine it does.

BRUNO: That’s it. I’m going to catch a cold out here. I have to go home.

NARRATOR (actor playing Schmuel): But as he said this, his feet brought him up a set of steps and into a long room that was surprisingly warm and must have been very securely built because no rain was getting in anywhere. In fact it felt completely airtight.

BRUO: Well, that’s something. I expect we’ll have to wait here till [the rain] eases off and then I’ll get to go home. I’m sorry we didn’t find your Papa. [And] I’m sorry we didn’t really get to play, but when you come to Berlin, that’s what we’ll do. You’re my best friend, Schmuel. My best friend for life!

NARRATOR (actor playing Schmuel): At that moment there was a loud gasp from all the marchers who had filled the room. The door at the front was suddenly closed and a loud metallic sound rang through from the outside.

NARRATOR (actor playing Bruno): And then the room went very dark and somehow despite the chaos that followed, Bruno found that he was holding Schmuel’s hand in his own and nothing in the world would have persuaded him to let it go.
```

---

## IC-0979: The Boy Who Fell into a Book

- Title: The Boy Who Fell into a Book
- Author (byline): Alan Ayckbourn
- Work: Not specified
- Publisher: Faber and Faber
- Publication date as stated: Mar 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, KEVIN, DAD, VOICE, ROCK, MONIQUE, LITTLE MAN, WOMAN, BOTH, WOLF, R-HOOD
- Teaser before the introduction: Yes
- Spoken words (computed): 1210
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
ACTOR 1: I admit it. I love to read. Getting lost in a good book is one of my favorite things.

ACTOR 2: But in this selection, if you are lost in a story, bookmarks are useless and page numbers become portals.

ACTOR 1: Buckle up, because Kevin’s literary shenanigans are about to begin.

ACTOR 2: Can he and Rockfist Slim save the world one story at a time?

TOGETHER: The Boy Who Fell into a Book by Alan Ayckbourn
```

### Performance text (classify this)

```text
Suggested Roles:

ACTOR 1: Kevin, Little Man, Woman/Wolf

ACTOR 2: Dad, Voice/Rock, Monique, R-Hood

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

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

WOMAN: (Pg 46-47) (appears behind Rock, stands watching him until he turns in fear) Hallo, my friends, please have no fear, For you are very welcome here.

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

## IC-0980: Breast Men

- Title: Breast Men
- Author (byline): Bill Bozzone and Joe DiPietro
- Work: Act One '95: The Complete Plays, Pgs 27-40
- Publisher: Smith and Kraus
- Publication date as stated: June 1996
- Event as filed: Duo Interpretation
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
ACTOR 1: Stuart and Lloyd are lifelong best friends who've gone away for a men's weekend to help Lloyd (a beefy fireman) get over his recent breakup with a busty girlfriend.

ACTOR 2: A travel agent mistakenly booked them into a room at Love Acres, a romantic retreat in the Poconos, and their original plans to drink beer, watch old movies, hang out by the pool and do guy things are disrupted when Stuart (a lonely fire dispatcher) makes a confession.

ACTOR 1: A medical condition has caused Stuart to grow womanly breasts and he needs money for an operation to fix it.

TOGETHER: We’re just a couple of . . . Breast Men by Bill Bozzone and Joe DiPietro
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

## IC-0981: Brushstroke

- Title: Brushstroke
- Author (byline): John Shanahan
- Work: The Best 10-Minute Plays 2007 – 2 Actors, Pgs 131-138
- Publisher: Smith and Kraus Publishers
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GAVIN, TIM
- Teaser before the introduction: Yes
- Spoken words (computed): 1391
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Shanahan
Book: The Best 10-Minute Plays 2007 – 2 Actors, Pgs 131-138
ISBN: 978-1575255897
Publisher: Smith and Kraus Publishers
Date (Month/Year):
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: How do you view art? It used to be that anything called “Art” had certain meaning attached to it. Art was assumed to be beautiful, intricate, expensive. . . crafted with care by a master. Sometimes it told a story, or marked a special day or event.

ACTOR 2: Art was universally revered, instantly recognized, and generally approached with awe, while today it is looked at much differently.

ACTOR 1: Viewers generally respond to works of art in one of the three following ways: Enjoyment, Dislike or Disinterest

ACTOR 2: Unfortunately, with art being as commonplace as it is, many artists and art experts are looking more and more for uniqueness in art above anything else. The art community tends to move from artist to artist, always searching for the cutting edge, the most daring, the strangest, even the obscene or shocking.

ACTOR 1: It is little wonder that for some artists, the mere act of completing a canvas is the cause for much trepidation as shown in

TOGETHER: Brushstroke by John Shanahan.
```

### Performance text (classify this)

```text
Scene: Gavin Taylor, a neatly dressed man in his thirties to forties, stands at C, looking with some degree of awe over a large contemporary painting. (The painting's presence at C front should only be suggested.) It's a modern piece, many bold swaths and smaller strokes across the canvas. To anyone but Timothy, it would appear quite finished. To one side is a small table holding a palette with blobs of paint on it and several brushes. Upstage, slouched in a chair rubbing his eyes, is Timothy Parsons, the artist. He can be any age from late-twenties to fifties. He's dressed in a casual, artsy style, but his clothes are not the paint-spattered kind typically used to say "artist. " He hasn't painted in so much as a dot in the last three weeks.

GAVIN: (Pg 131-138) My. Timothy, oh my.

TIM: (Without looking.) Mm hmm.

GAVIN: This is ... magnificent.

TIM: Hmm.

GAVIN: I mean it's - I hate to sound gushy, but ... it's so powerful. Stunning.

TIM: You think so, huh?

GAVIN: (Crossing back toward Tim.) I really do.

TIM: Huh.

GAVIN: Don't you think so?

TIM: I wouldn't know.

GAVIN: (Laughing.) The artist wouldn't know if his work was good?

TIM: (Flatly.) It's hard to say until it's finished. (Pause. Gavin looks at Tim, then to the painting, then back to Tim.)

GAVIN: It's not done?

TIM: (With some exhaustion.) No. It's not done.

GAVIN: Really? Because, you know, it honestly is quite –

TIM: It's not done. (A tense pause.)

GAVIN: You could have fooled me.

TIM: Apparently I did.

GAVIN: Not done.

TIM: No.

GAVIN: How much longer do you figure before it is?

TIM: Hard to say.

GAVIN: How long has it been like this? Unfinished.

TIM: Three weeks, maybe.

GAVIN: Ah. (He takes a few steps back and studies the painting.) You've made a good start.

TIM: Very funny.

GAVIN: SO what is it missing? What is it going to take to finish it?

TIM: One brushstroke. (Silence. Gavin looks at Timothy with a question on his lips.)

TIM: One brushstroke. Then it's done.

GAVIN: Are you serious?

TIM: (Crossing past him to regard the painting.) Quite.

GAVIN: So you could finish it today. Now.

TIM: No.

GAVIN: No? (Timothy looks at the painting. Cocks his head. Shakes his head and walks back to the chair and sits wearily.)

TIM: No.

GAVIN: You're beginning to worry me, Timothy.

TIM: Imagine how I feel. (Pause. Gavin regards Timothy, as if to gauge if he's serious. To some degree, Gavin [eels that he's not. He picks up a brush from the table, walks back to Timothy, and holds it out to him.)

GAVIN: Finish it. (Pause') Come on, just finish it, then we'll go have a drink to celebrate. I'm buying.

TIM: Just like that?

GAVIN: Come on. One brushstroke and be done with it!

TIM: Where does it go? (Pause') If it's so patently simple, Gavin, then help me out here. Where is it supposed to go?

GAVIN: It's not my work.

TIM: No, no, no, no - you don't back out like that. You don't just merrily tell me to pick up my brush and finish my painting and then say you don't know how.

GAVIN: But I -

TIM: Come on! Tell me where it goes! Tell me how to finish it! (He snatches the brush from Gavin and waves it at the canvas.) Does it go here? Huh? Up in this corner?

No? The middle? Where, Gavin? Show me exactly where! How long should it be? How wide? Do you know? And what color? Is it brown? Is it sort of brown? Is it blue, Gavin? Is it? What if it's not blue, Gavin? What then? WHAT IF IT'S NOT SUPPOSED TO BE BLUE? (He throws the brush down, storms across stage, and kicks the chair. He stands with his back to Gavin.) (A lengthy, tense silence.)

GAVIN: I didn't want - I meant no disrespect, Timothy.

TIM: I know.

GAVIN: Do you want to talk about it? (Timothy thinks a moment. He crosses to the brush, wherever it is, picks it up and puts it back on the table with the palette.)

TIM: Probably. And I probably should. But to tell you the truth, I'm not sure I'd know what to say.

GAVIN: Just tell me what's going on. (Timothy turns and smiles at him, but it's a sharp smile, almost a smirk.)

TIM: That's what I like about you, Gavin. You have this firm, simple belief in the absolute black and whiteness of things. You genuinely believe that whatever's happening with me not finishing this can just be drawn out somehow by you asking me what's going on. That there's got to be this one thing that constitutes the entire problem.

GAVIN: (Simply.) Isn't there? (Pause)

GAVIN: Has anyone else seen this?

TIM: No.

GAVIN: Then why is it so bothersome that I, being the first person to find out that one brushstroke has kept you from finishing a great painting, should ask what's wrong?

TIM: I never said bothersome –

GAVIN: Then what?

TIM: It's not that simple!

GAVIN: Why?

TIM: Why do you need to know? (Gavin laughs)

GAVIN: Because you're my friend, Timothy. Because I come here and I find you in this mood, with this problem, and - I'm honestly surprised that you have to ask me why I need to know! Why couldn't you have just said it's not done and left it at that? Or told me that it was done? Or hidden the damn thing in the first place? (Timothy is at a loss.)

GAVIN: Because you couldn't. Because you needed someone to know. You wanted someone to ask. Here I am.

TIM: Here you are.

GAVIN: And I'm asking.

TIM: Yes you are. (Another silence. Gavin is determined to ride it out, to have Timothy speak first. After several beats, Timothy sighs.)

TIM: Would you say, Gavin, that this is the best work I've ever done?

GAVIN: I'd have to say it's definitely on par with-

TIM: If you want to help me, Gavin, then answer the question. And it's a yes or no question. Is this the best work I've ever done?

GAVIN: You say it's not done.

TIM: You didn't know that when you first saw it. You told me it was stunning.

GAVIN: Well it is!

TIM: So is this my best work?

GAVIN: Yes. Probably.

TIM: Probably means no.

GAVIN: All right. Yes.

TIM: Exactly.

GAVIN: Exactly what?

TIM: This may very well be my best.

GAVIN: Well, then, congratulations! (Pause. A short, sad laugh .from Timothy.)

TIM: I don't know why I thought you'd see it. I don't - (He's at a loss. He throws his hands up.)

GAVIN: What? (He throws his hands up, mocking Timothy.) What is this? (A moment where Timothy's anger builds. Then he storms to the canvas.)

TIM: This is my best painting. And the minute I take up that brush and I put that one final smear of paint, that line, that dot, whatever it is that finishes it, on that canvas, I will be expected to create another one that is better than this. My best. (Calming in voice but not in mindset.) If I finish this right now, then tomorrow or the next day or a year from now there will be a blank canvas - waiting - and from the first brushstroke, the first choice of color, it has to be better than this. But it has to come from somewhere. What if I don't have anything left after this?

GAVIN: Timothy. Really. This is just not sensible. This is just some sort of artistic post-partum depression. Art is a birthing process. I know that. You carry it around, you nurture it, and when it's done you have to separate from it, and I understand that can be difficult. Timothy, you're a brilliant artist. You don't need to worry that you won't have another idea.

TIM: "Idea." Your understanding is that this is me worrying about having an idea.

GAVIN: (Smiling.) Correct me if I'm wrong. (Pause, as Timothy debates whether to go forward)

TIM: I started planning this painting eleven months ago. At the time, I thought it was simply going to be my next painting. Just my next one. But as I worked on it, I knew it was becoming something, but not like before. I became very particular about it. And I got to this point, where it is now. Really about eight months of actual work - sketching, painting, refining everything. One morning I came out to work and ... I saw something. I saw every day of those eight months, all tied together on the canvas. I saw moments. I looked into it, I touched it. I started to think about what each pass of the brush meant. I wondered. Where were the bits that I painted when I was happy? When I was pissed off? Where I was invigorated? Where I was frustrated? What parts did I paint in the day? Which were those ones where I woke up in the middle of the night just knowing that I had to paint - those ideas that just come and won't go away? Where were the things that I'd painted over? What had they meant, where had they come from? Where did all of this come from? (Pause) And then, in this one moment, I understood. In one way or another, I put everything I am (Touching the canvas.) here. Almost everything. (Without turning.) And I am scared, Gavin, scared to death to think that when I put that one final stroke on this canvas, that I will have finally given everything that I am, and that it will be all that I have. I am afraid, Gavin, that in a very real way, I will disappear.

GAVIN: Nothing left, or nothing left to give?

TIM: They're the same.

GAVIN: Don't you wonder, though?

TIM: Wonder what?

GAVIN: What comes next, of course?

TIM: Yes, I do. And it scares the shit out of me.

GAVIN: Then it must be art.

TIM: What? (Gavin picks up the palette and brusb.)

GAVIN: One brushstroke. Then there's either something or there's nothing. But either way, there's art. Which is more than most people can say. Eight months you worked on this?

TIM: Yes.

GAVIN: Then what's one more day's work? (He holds the palette out to Timothy. Pause.)

GAVIN: Not knowing will kill you. (A beat. Timothy reluctantly steps over toward Gavin. He looks at the painting, then takes the palette. He turns back to the canvas, staring intently into it)

GAVIN: Do you mind if I watch?

TIM: (Snapping his attention away.) What?

GAVIN: Can I watch you finish it?

TIM: Certainly. Yes. Please. (Timothy hesitates. He looks at the palette, the brush poised above it. Then, without turning:)

TIM: Gavin?

GAVIN: Yes?

TIM: What color is the last part of my soul?

GAVIN: (After a beat.) Timothy, you've known what color it is for the last three weeks. (Timothy turns and looks at him.) Paint it. (Timothy turns back, and looks once more at the palette. He begins mixing colors as the lights fade.)
```

---

## IC-0982: The Chalky White Substance

- Title: The Chalky White Substance
- Author (byline): Tennessee Williams
- Work: Plays InOne-Act
- Publisher: Ecco Press
- Publication date as stated: Nov 1999
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MARK, LUKE
- Teaser before the introduction: Yes
- Spoken words (computed): 2089
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tennessee Williams
Book: Plays InOne-Act
ISBN: 0880014903
Publisher: Ecco Press
Date(Month/Year): Nov 1999
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: A century or two after our time -- an almost equal time after the great thermonuclear war, a wind rises and falls, a wind that constantly blows about an earth as shriveled and desiccated as a terminally sick being.

ACTOR 2: Many picture the future of our Earth to be technologically advanced; however, Williams describes a desolate, war torn, and almost uninhabitable Earth; where women have failed to thrive. And the men battle daily for their very existence in the midst of . . .

TOGETHER: The Chalky White Substance by Tennessee Williams
```

### Performance text (classify this)

```text
LUKE about twenty years of age, sits with an air of perplexed and anxious waiting. Upstage and to the left of him is seated MARK about eight years older, watching him with an enigmatic fixity of expression. After some moments MARK rises and slides stealthily of{ his upstage perch. LUKE removes from a pocket a small metal bottle containing water and a cloth which he dampens and with which he carefully and gently cleans his face .No sooner has he returned the bottle and cloth into the pocket than MARK appears silently behind him and stoops to clasp his large, powerful hands over LUKE’s eyes.

MARK: Whooooo!

LUKE: YOU! -You can disguise your voice but not your hands. What makes you so late?

MARK: Boys are inquisitive, aren't they? What, why? I wasn't late. If you'd turned around, you'd have seen me sitting back there on that boulder behind you.

LUKE: Why?

MARK: I thought to myself, "It could be the last time I'll observe him, sitting here, waiting for me?"

LUKE: You're planning to go away? Somewhere? Without me?

MARK: Make a departure? From you? From this precipice over the Arroyo Seco, this desolation, so beautiful through the continual screen provided by the-chalky white substance? No, I'm making no departure. But how do I know that you're not?

LUKE: A secret departure? One I'd not mentioned to you?

MARK: Don't you know departures can be made without warning? You don't say you're going, you don't even know you're going, then (Snaps his fingers.) you're gone. Life's full of sudden departures; what a pity death isn't. (Mark removes his hands from the youth's eyes.)

MARK: Don't pull that cowl over your face.

LUKE: It protects my eyes from the dust always blowing, blowing constantly-from where?

MARK: The shrinking earth's a desert and barren mountains. In our part of it, the vicinity here, most of the chalky white stuff is provided by the Arroyo Seco, down there. I've heard that once, a few hundred years ago, there was a river in it-there's nothing drier and dustier than an arroyo in which there was once a river that's now dried up. (The youth lowers the cowl over his head; Mark draws it back up.)

LUKE: I thought you admired my eyes for being so clear, not inflamed?

MARK: This evening let me have a long look at your face, memorize it, as if I might never be going to see it again.

LUKE: You said you weren't going away, and I told you I wasn't, either. I still don't understand why you kept me waiting here while you were right back there all that time.

MARK: You learn a great deal about someone you care for by observing him without him knowing you are. You notice whether he waits indifferently, or with increasing concern as it gets later, oh, you learn many things you'd never know otherwise.

LUKE: What did you observe you didn't already know?

MARK: More and more tension in you as the sky started to fade.

LUKE: You know I'm afraid of the dark when I'm alone at night. If it had gotten a bit darker, I would have started home and missed our meeting.

MARK: Fear, that's a bad thing to feel.

LUKE: A natural thing to feel. Now that women are so much fewer than men, there are bands of nomads that will seize a boy after dark and . . .

MARK: I know. Ravage him. And when their lusts are satiated, they leave no witness, just the lifeless body. -Lean back. (Luke leans into his embrace.) It always amazes me, the smoothness of your skin under the robe, not granulated at all by the chalky white substance.

LUKE: I know you like the touch of smooth skin, so I keep mine smooth for your pleasure.

MARK: How do you do that?

LUKE: Before I go to meet you here, I bathe myself and then immediately I put on my robe.

MARK: You bathe once a day before you come here to meet me, not just at night, as we're ordered to do?

LUKE: I bathe twice, once for you and again at night, Mark.

MARK: Bathe twice? Did you say twice.? But that would mean that you disregard the water restrictions as if they didn't exist. -You know, this confirms my suspicions that you have another protector, one in a high position in the regime, you little-cheater, yes, you get by with violating the restrictions because you give yourself at night to someone of great power among the

LUKE: I've never had more than one protector at a time. That one protector now is you.

MARK: Before me, you had others.

LUKE: They were necessary. I hardly remember my parents. I'll tell you something that'll amuse you. On the wall at my place I have a colored picture of the lady that was called the Madonna.

MARK: Those old mythological pictures are a rarity now and could be sold to the center for special privileges, you know.

LUKE: I'd rather keep the picture on my wall.

MARK: What were you going to tell me that will amuse me? Something about the picture of the Madonna?

LUKE: Once I had a protector. When I woke up one morning, he was standing there staring at the picture. He said, "Is this your mother?"

MARK: Thought that the Madonna was your mother. . .

LUKE: The funny thing is that I said, 'Yes, that is, that was my mother." Women were a comfort. Why are they disappearing? Do they succumb more quickly to the chalk all about us now?

MARK: The earth's not able to support its shrinking population. There's little food, and even less water. I've heard that a man will use a woman awhile, and then, when she's no longer desirable to him, not as she was before, he's likely to destroy her. You see, Luke, the battle between people that happened so long ago that it's barely recorded, I understand that it had a brutalizing effect. Do you understand me?

LUKE: Brutalizing?

MARK: Opposite effect from the care of a Madonna.

LUKE: So that now we have only each other.

MARK: Have I told you that I have a woman at home?

LUKE: A mother? A Madonna? (Mark laughs harshly.)

MARK: No, what remains of a girl, the remnant of her, used too much, not able now to excite me nor even to-serve. . . only to stagger about, looking more and more frightened. I suspect she knows.

LUKE: You suspect she knows what?

MARK: That her withering, frightened look, her choking sounds at night

LUKE: From the disease? She has it?

MARK: She's breathed too much of the chalk. I think she knows that soon it will be necessary to relieve myself of her presence in my place.

LUKE: I don't think you'll do that. No, you couldn't do that.

MARK: You haven't sat for an hour observing me waiting for you, and so you know me less.

LUKE: Since I know you completely

MARK: Are you sure that you do?

LUKE: I feel secure with you, Mark. And as for the woman you've never mentioned before, have you told her about us?

MARK: I say nothing to her now but, "Oh, are you still here? Go lie down in that corner over there and don't cough and don't crawl toward me."

LUKE: You're making all this up, I know it's not true.

MARK: You know so little, boy. You know dangerously little. You don't know enough to distrust.

LUKE: Oh, I distrust them all except you, Mark.

MARK: That might be a mistake. The worn-out girl at my place, she trusted me once as you do. But when I go home tonight, if she's still there-out she'll go, I'll throw the door open, and kick her living or dead body into the wind she can't stand against, that will sweep her away and bury her in white dust. No, don't trust. So. You said you bathe twice a day, before you come here to meet me and again at night, violating the water restrictions?

LUKE: When I was very young

MARK: Younger than now?

LUKE: Little more than a child. I had a protector, my first, who was very clever, very wise, at secret, mechanical things. Did I say that right?

MARK: Perfectly. Go on.

LUKE: One day he put his ear to the earth.

MARK: In or out of the house?

LUKE: Both in and out, and he discovered that not far under the earth, running under the house, there was water, he said a stream of it, not wide, not deep, but

MARK: Ohhh...

LUKE: He was a strong man, he dug and dug down to it and built steps down with stones.

MARK: But when the house is inspected by the

LUKE: Inspectors, no. You see, the opening to the steps is covered over with an old, dry animal skin, and even if the inspectors looked under this ragged leather-you know their eyes are bad, half-blinded by the chalk-they wouldn't notice the width of the cracks.

MARK: By which you can lift the cover to the underground spring of water? -How very foolish of you!

LUKE: He did it all, not I.

MARK: But he's gone now, and you have it all to yourself, for your own private and-illegal-use. You are not at all wise.

LUKE: (Shrugging.) I must live, and to live I must please.

MARK: But you mustn't talk about it.

LUKE: Of course not. To no one but you.

MARK: No, not even to me, because by talking about it to me, you make me a conspirator with you, as criminal as you are.

LUKE: Oh, but you

MARK: Would bear the same penalty you would, knowing what you've told me and not-informing.

LUKE: Whom would you

MARK: Inform? The ones you inform to. The rulers, the authorities of the regime.

(Pause.)

LUKE: You believed that story? You didn't know that it was all made up? Just an invention, like yours about the woman and what you'll do to her tonight?

MARK: That was no invention. And neither was what you told me about the underground spring.

LUKE: You're holding me so tight it's hard to breathe.

MARK: You're a light-footed boy. You might suddenly spring up and take to your heels.

LUKE: From you?

MARK: Of course, now that you realize that you've made such a dangerous mistake. I suspected something. And now I know.

LUKE: But I know something, too.

MARK: What?

LUKE: You've told me how completely you love me.

MARK: A thing that I also told the woman when she was desirable to me.

LUKE: She doesn't still attract you. I do. Don't I? Mark?

MARK: You've put in my possession a secret that to keep from the authorities would expose me to the same penalty you're exposed to. You know what such penalties are?

LUKE: A term of imprisonment, but

MARK: A long, long term, and even if you're alive when it expires, you'd be unrecognizable, Luke.

LUKE: I'd be disfigured, you mean?

MARK: By more than time, by more than the terminal effect of the chalky white substance. (He clamps his arms tighter about Luke.)

LUKE: What are you, why are you-!

MARK: I must deliver you to them and repeat your confession and receive the bounty. Did you know there's a bounty offered for turning in a person who violates the laws, the restrictions? The authorities regard him with more respect, he's given a title, sometimes, and his licenses are extended. The inspectors pay his house a-respectful visit, they smile at him and say, "The place needs some improvements in keeping with your new position. We'll see to that right away."

LUKE: The authorities are vicious.

MARK: I understand that's always been their nature, even before the people of the earth divided into two or three hostile parts that battled for ownership and rule with the great explosive devices. Who won? Nobody. Nobody! (The italicized word is echoed, after a couple of moments, from the opposite side of the chasm.) Hear that? Know what that was? As if somebody called back? That was an echo. So many of the old words have dropped out of use and aren't known anymore.

(Pause.)

LUKE: The authorities are corrupt, but we don't have to imitate them.

MARK: To save our skins we do.

LUKE: Would they still be worth saving?

MARK: I understand that there used to be considerations called moral. And for these considerations, morality, a thing such as the betrayal of someone you love, would be held in contempt. But that was once, long before I remember. Stop struggling. I'm hard and strong. What's the use? You can't escape. Light's faded. We must get going.

LUKE: Where? The cave? Or my place?

MARK: Neither this evening, Luke. We're going to the cabildo where you will stay confined till long out-used, to the end of your time. -Time! (The pause; the echo.)

LUKE: Then kill me. Kill me, Mark!

MARK: And sacrifice the reward? (Wind rises. Luke thrashes impotently in the grasp of Mark.) Call him, the great protector called God. No breath? I'll call Him for you. Pro-tec-tor! (Pause; the echo.) What a huge creature, what an immense beast He must have been to have left such enormous white bones when He died. . . End-lessly long ago, the bones of Him now turned to powder that blows and blows about His broken-creation. . . (He bears Luke, futilely struggling, down the upstage declivity, and the stage darkens.)
```

---

## IC-0983: Chomp

- Title: Chomp
- Author (byline): Carl Hiaasen
- Work: Not specified
- Publisher: Yearling
- Publication date as stated: March 2020
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, RAVEN, NARRATOR 1, NARRATOR 2, DEREK, WAHOO, MICKEY, DIRECTOR, NARRATOR, DEREK FROM THE TAPE, SECRETARY, SICKLER, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1264
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
ACTOR 1: Are you a fan of survival-skills TV or wildlife documentaries?

ACTOR 2: Shows like Naked and Afraid and Steve Irwin’s Crocodile Hunter have nothing on this reality TV show –

TOGETHER: Expedition Survival!

ACTOR 1: Wahoo Cray and his father Mickey, a professional animal wrangler, are hired to manage the wildlife.

ACTOR 2: Filming begins in Mickey’s homemade swamp, where the reckless Badger ignores Mickey’s warnings and ends up atop a thrashing, angry alligator.

ACTOR 1: When the footage turns out better than anyone expects, Badger orders filming moved to the Everglades to put the real back in reality TV.

TOGETHER: Chomp by Carl Hiaasen
```

### Performance text (classify this)

```text
Suggested Roles:

ACTOR 1: Raven, Narrator 2, Mickey, Director, Sickler

ACTOR 2: Narrator 1, Derek, Wahoo, Secretary

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

RAVEN: (knocks on door, it is opened by Wahoo – freeze frame)

NARRATOR 1: (Pg 12) [That woman] with a shining stack of red hair is Raven Stark.

RAVEN: (with a strong accent) I’m Derek Badger’s production assistant. I brought your contract. (Pg 14) One thousand a day, plus location fees and animal rentals. (Pg 15) Where are your pythons? Derek wants a beast. (Derek steps in)

NARRATOR 2: (Pg 11) Derek Badger - the star of Expedition Survival! (Derek fist pumps to the audience)

NARRATOR 1: Every week, Derek parachutes into some gnarly wilderness teeming with fierce animals, venomous snakes and disease-carrying insects. Armed with only a Swiss army knife and a straw, he hikes, climbs, crawls, paddles or swims back to civilization.

NARRATOR 2: Along the way, he eats bugs, rodents, even worms—the grosser it looks, the happier Derek Badger is to stuff it into his cheeks. (Derek smiles winningly at the audience, then picks a bug leg from his teeth)

DEREK: (Pg 31) (with an obviously fake Australian accent) Take me to your alligator. Chop Chop!

RAVEN: (Pg 16) (whistles) That’s a monster, eh?

WAHOO: Twelve feet

MICKEY: (Pg 33) (proudly) Six hundred and twenty pounds. (Pg 75) Alice is her name.

DEREK: (Pg 32) She’s perfect! (to Raven) (Pg 38-39) But we can’t stage our biggest scene in some nitwit’s backyard.

RAVEN: It looks like a real-life swamp. You’ll be impressed.

DEREK: No, they’ll be impressed when they see me jump that monster gator.

RAVEN: Not happening. The insurance company says no way.

DEREK: They said the same thing about the cobra dance, but I did it anyway.

NARRATOR 2: They had been shooting Expedition Survival! in Cambodia when Derek decided to play snake charmer with a spitting cobra that had been rented from a local handler.

NARRATOR 1: Mr. Na leaped between Derek and the dangerous reptile just as it released a jet of deadly poison. A few drops landed in Mr. Na’s hair, and as a precaution he rushed off to take a shower.

NARRATOR 2: Upon returning to the set was dismayed to learn that Derek had chopped up his pet snake with a rusty machete and eaten it in the program’s final scene. *******

NARRATOR 1: (Pg 43-44) [The next day] Wahoo and his father uncoiled the python, Beulah and laid her out at full length. The script called for Derek to creep up and seize Beulah behind her head, instigating a fake life-or-death struggle.

DIRECTOR: (airhorn blows) Episode 103 – Expedition Survival! Action!

DEREK: (Pg 44-46) (whispering dramatically into a microphone on his shirt collar as he sneaks up on Beulah) “As if the Everglades weren’t dangerous enough, in recent years this tropical river of grass has been invaded by lethal predators from another continent— Burmese pythons! They can swallow a whole deer, a panther and, yes, even a human being. Look! There she is!” (pounces with a triumphant cry and grabs Beulah 2 feet below her head) “I’ve got her! I’ve caught the beast! (grunting and huffing he ‘struggles’ with the docile Beulah – it’s like fluffing a pillow)

DIRECTOR: Cut! Cut!

DEREK: (Pg 47) (lurching to his feet – he slams the python to the ground and confronts Mickey) That’s the worst excuse for a python I ever saw! You call that a snake? Ha! I call it an overstuffed earthworm. (disgusted with this scene, he moves on) What about the gator?

WAHOO: (Pg 52) Showtime!

DIRECTOR: (Pg 44) (airhorn blows) Episode 103 – Expedition Survival! Action!

NARRATOR 2: (Pg 60) Wahoo and his father peeked over the cameraman’s shoulder. The screen showed a view from the submerged camera. And there was Alice.

MICKEY: She won’t touch him. Not on a full belly.

DEREK: (Pg 58-59) (to crew) No mistakes! (he slips into the pond up to his neck - to camera) “Soon the sun will be setting over the Everglades. I must swim across this deep, murky pond to reach dry ground. Getting across this water is absolutely crucial to my survival but I’ve discovered fresh signs of an extremely large alligator, and I mean HUGE, lurking close by! If that monster were to attack me right now, the only chance I’d have of escaping alive would be to fight back ferociously, desperately, and gouge it in the eyes.”

WAHOO: (Pg 65) She’s coming up! Don’t move!

NARRATOR 2: (Pg 64) Slowly but surely, Alice was rising from the bottom of the pool.

DEREK: (Alice comes up underneath Derek; suddenly he is straddling her like a tipsy cowboy on a bronco) (Pg 66) Wooo-hooo! (hollering idiotically – he grabs her scales to hold on)

RAVEN: Oh, Lord. (Pg 68) (shrieking) Shoot it! Shoot it! Shoot that thing!

DEREK: (Pg 66) Wooo-hooo!

NARRATOR: (Pg 67) Members of the Crocodilia order of reptiles don’t buck like horses do when shedding an unwanted rider. Instead, they thrash and spin. Derek managed to hang on for three full revolutions before being launched airborne. (watch Derek’s arc through the air -- Splash!) *****later that night*****

DIRECTOR: (Pg 71) I brought something to show you (holding up a disk) The pond scene.

(puts the disk into a DVD player)

RAVEN: Let’s get this over with. (They watch becoming more excited)

DEREK FROM THE TAPE: (Pg 66) Wooo-hooo!

DIRECTOR: (Pg 72) Well?

DEREK: That was bloody. . . brilliant! (punches the air jubilantly with both fists) I almost died, didn’t I? That vicious monster almost killed me! (Pg 75-76) The most extraordinary 33 seconds of footage in the history of Expedition Survival! (Pg 86) (dreamily) The rest of the show must all build up to this incredible, heart-stopping moment. We’ll spare no expense!

MICKEY: (Pg 76) But you almost got drowned.

DEREK: Exactly! And the best part is it was real! We’re hiring you to lead us into the Everglades to put finishing touches on this masterpiece!

MICKEY: (disappointed) (Pg 134) All due respect, Mr. Beaver, this ain’t my first rodeo. (Pg 76) You’re gonna fake the rest of it, same as you always do.

RAVEN: In our line of work, it’s known as ‘re-creating’ events for the camera.

DEREK: (Pg 87) No more faking it, mate. (Pg 86) No tame animals. This time we’re going totally raw and wild. (Pg 87) We’re putting the ‘real’ back in ‘reality.’ *****

NARRATOR 1: (Pg 89) Mickey Cray was surprised to learn that Derek Badger didn’t want any of his captive critters on location.

MICKEY: Seriously. The man almost got killed by the world’s laziest alligator!

RAVEN: (Pg 97-98) We cannot have a repeat of what happened with your alligator. We need Derek in one piece. He’s the whole franchise.

NARRATOR 2: (Pg 103) But Raven Stark’s request to base the program in Everglades National Park had been rejected.

NARRATOR 1: [They] informed Raven that, because of the earlier egg-robbing incident at Yellowstone, Derek Badger had been blackballed from the entire federal park system.

RAVEN: (on the phone) For how long?

SECRETARY: Eternity.

NARRATOR 2: The crew of Expedition Survival! was using Sickler’s Jungle Outpost and Juice Bar.

SICKLER: (waves to audience, thumbs up) (Pg 95) I just repainted the place!

(PG 40) [a rumpled assistant begins spraying Derek’s arms and legs. Derek cooperates, then closes his eyes and holds his breath as the assistant mists his face]

WAHOO: What is that stuff?

RAVEN: Spray-on tan.

MICKEY: What a poser!

DEREK: (Pg 52-53) So what am I supposed to eat to survive. For the show, I mean.

RAVEN: (applying make-up to Derek) The script calls for bullfrogs and crawdads.

DEREK: (dismissively) What else? I want something truly disgusting.

RAVEN: How about maggots? (Pg 149) (Off stage a piercing scream)

NARRATOR 2: One of the catering staff was hopping frenetically and pointing at a furry, twitching intruder that lay quivering on the cake platter.

DEREK: (strides over to the table to examine it – he grins) Just as I suspected – a bat! (he licks his lips) Let’s do this! Set up some lights!

DIRECTOR: (Pg 44) (with little enthusiasm) Episode 103 – Expedition Survival! (Pg 133) Action!

DEREK: (Pg 155-157) (to camera) Deep in the Everglades, the swamp is unforgiving and food is scarce. Survival means eating whatever you can get your hands on. But by sheer luck, the violent weather has literally dropped on my platter a tasty morsel that will provide enough nutrition to get me through another brutal day in this tropical wilderness. Look! (dangles the bat by its tail) Unfortunately, the rain has soaked all the tinder, so I can’t make a fire for cooking. That leaves me only one choice. Now, please don’t try this yourself—wild bats can be vicious, and their teeth are needle sharp. Remember, I’m an experienced survivalist. I know how to handle these unpredictable rascals. . . (he tilts his head back and dramatically begins to lower the bat into his mouth)

NARRATOR 2: (as Derek pantomimes) The bat wasn’t vicious. She simply didn’t want to be eaten. She reacted defensively and without hesitation and chomped down on the first chompable target. (Derek screams) Which happened to be Derek’s plump tongue.

DIRECTOR: (Pg 159) Zoom in for a close-up! Hurry! (but Derek runs, still screaming into the swamp) ****** days later Derek hiding in the swamp*****

DEREK: (Pg 266) (Using his cell phone to film himself – his speech is distorted due to a swollen tongue) My harrowing Everglades adventure is finally drawing to an end, and not a moment too soon. I’m completely out of food, out of water and dangerously weak after being attacked by a rare but deadly vampire bat. Its savage bite left me dazed and delirious, racked with fever. Why, at times I even imagined myself morphing into a real-life vampire!

NARRATOR 2: (Pg 168) It would be a humongous night for the show’s TV ratings if Derek Badger failed to survive one of his survival expeditions!

RAVEN: (to audience, almost cheerfully) It’s possible the bat had rabies. Derek could be losing his mind.

DEREK: (Pg 115) (desperately paranoid and scared) Time is running out. [When] the sun goes down, the predators come out – alligators, panthers, bears, pythons. (Pg 186) My only hope is that somebody finds me way out here before it’s too late . . .

NARRATOR 1: [*Turn in next time for the chilling conclusion of]

(*bracketed words have been added as an transitional ending – not in the original novel)

TOGETHER: Episode 103 – Expedition Survival!
```

---

## IC-0984: Click-Clack the Rattlebag

- Title: Click-Clack the Rattlebag
- Author (byline): Neil Gaiman
- Work: Ghostly: A Collection of Ghost Stories
- Publisher: Scribner
- Publication date as stated: Oct 2015
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BOY, BOYFRIEND
- Teaser before the introduction: Yes
- Spoken words (computed): 1263
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Gaiman
Book: Ghostly: A Collection of Ghost Stories
ISBN: 978-1501111198
Publisher: Scribner
Date (Month/Year): Oct 2015
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Fear coils in your stomach and clutches at your heart.

ACTOR 2: It’s an unpleasant emotion we usually do our best to avoid.

ACTOR 1: Yet across the world and through time people have been drawn irresistibly to stories designed to scare them.

ACTOR 2: But we all know that these stories of vampires, werewolves and monsters aren’t really true.

ACTOR 1: Are they?

TOGETHER: Click-Clack the Rattlebag by Neil Gaiman
```

### Performance text (classify this)

```text
BOY: Before you take me up to bed, will you tell me a story?”

BOYFRIEND: (to the boy) Do you actually need me to take you up to bed?

BOY: (thinking for a moment and then with intense seriousness) Yes, actually I think you do. It’s because of, I’ve finished my homework, and so it’s my bedtime, and I am a bit scared. Not very scared. Just a bit. But it is a very big house, and lots of times the lights don’t work and it’s a sort of dark.

BOYFRIEND: (tousling the boy’s hair) I can understand that. It is a very big old house. (to audience) He nodded. We were in the kitchen, where it was light and warm. I put down my magazine on the kitchen table. (to boy) What kind of story would you like me to tell you?

BOY: (thoughtfully) Well, I don’t think it should be too scary, because then when I go up to bed, I will just be thinking about monsters the whole time. But if it isn’t just a little bit scary then I won’t be interested. And you make up scary stories, don’t you? I know she says that’s what you do.

BOYFRIEND: She exaggerates. I write stories, yes. Nothing that’s been published, yet, though. And I write lots of different kinds of stories.

BOY: But you do write scary stories?

BOYFRIEND: Yes.

BOY: (looking up at the boyfriend from the shadows by the door) Do you know any stories about Click-clack the Rattlebag?”

BOY: (looking up at the boyfriend from the shadows by the door) Do you know any stories about Click-clack the Rattlebag?”

BOYFRIEND: I don’t think so.

BOY: Those are the best sorts of stories.

BOYFRIEND: Do they tell them at your school?

BOY: (shrugging) Sometimes.

BOYFRIEND: What’s a Click-clack the Rattlebag story? (to audience) He was a precocious child, and was unimpressed by his sister’s boyfriend’s ignorance. You could see it on his face.

BOY: Everybody knows them.

BOYFRIEND: (trying not to smile) I don’t.

BOY: (trying to decide whether or not the boyfriend was pulling his leg) I think maybe you should take me up to my bedroom, and then you can tell me a story before I go to sleep, but a very not-scary story because I’ll be up in my bedroom then, and it’s actually a bit dark up there, too.

BOYFRIEND: Shall I leave a note for your sister, telling her where we are?

BOY: You can. But you’ll hear when they get back. The front door is very slammy.

BOYFRIEND: (to audience) We walked out of the warm and cozy kitchen into the hallway of the big house, where it was chilly and draughty and dark. I flicked the light-switch, but nothing happened.

BOY: The bulb’s gone. That always happens.

BOYFRIEND: (to audience) Our eyes adjusted to the shadows. The moon was almost full, and blue-white moonlight shone in through the high windows on the staircase, down into the hall. (to boy) We’ll be all right.

BOY: (soberly) Yes. I am very glad you’re here.

BOYFRIEND: (to audience) He seemed less precocious now. His hand found mine, and he held on to my fingers comfortably, trustingly, as if he’d known me all his life. I felt responsible and adult. I did not know if the feeling I had for his sister, who was my girlfriend, was love, not yet, but I liked that the child treated me as one of the family. I felt like his big brother, and I stood taller, and if there was something unsettling about the empty house I would not have admitted it for worlds. The stairs creaked beneath the threadbare stair-carpet.

BOY: Click-clacks are the best monsters ever.

BOYFRIEND: Are they from television?

BOY: I don’t think so. I don’t think any people know where they come from. Mostly they come from the dark.

BOYFRIEND: Good place for a monster to come.

BOY: Yes.

BOYFRIEND: (to audience) We walked along the upper corridor in the shadows, walking from patch of moonlight to patch of moonlight. It really was a big house. I wished I had a flashlight.

BOY: They come from the dark. I think probably they’re made of dark. And they come in when you don’t pay attention. That’s when they come in. And then they take you back to their . . . not nests. What’s a word that’s like nests, but not?”

BOYFRIEND: House?

BOY: No. It’s not a house.

BOYFRIEND: Lair?

BOY: (long pause) I think that’s the word, yes. Lair. (then a long silence)

BOYFRIEND: Right. So they take the people who don’t pay attention back to their lair. And what do they do then, your monsters? Do they suck all the blood out of you, like vampires?”

BOY: (snorting) Vampires don’t suck all the blood out of you. They only drink a little bit. Just to keep them going, and, you know, flying around. Click-clacks are much scarier than vampires.

BOYFRIEND: I’m not scared of vampires..

BOY: Me neither. I’m not scared of vampires either. Do you want to know what Click-clacks do? They drink you.

BOYFRIEND: (joking) Like a Coke?

BOY: (seriously) Coke is very bad for you. If you put a tooth in Coke, in the morning, it will be dissolved into nothing. That’s how bad coke is for you and why you must always clean your teeth, every night.

BOYFRIEND: (to audience) I’d heard the Coke story as a boy, and had been told, as an adult, that it wasn’t true, but was certain that a lie which promoted dental hygiene was a good lie, and I let it pass.

BOY: Click-clacks drink you. First they bite you, and then you go all ishy inside, and all your meat and all your brains and everything except your bones and your skin turns into a wet, milk-shakey stuff and then the Click-clack sucks it out through the holes where your eyes used to be.”

BOYFRIEND: That’s disgusting. Did you make it up? (to audience) We’d reached the last flight of stairs, all the way in to the big house.

BOY: No.

BOYFRIEND: I can’t believe you kids make up stuff like that.

BOY: You didn’t ask me about the rattlebag.

BOYFRIEND: Right. What’s the rattlebag?

BOY: (in a small, sober voice) Well, once you’re just bones and skin, they hang you up on a hook, and you rattle in the wind.

BOYFRIEND: So what do these Click-clacks look like? (to audience) Even as I asked him, I wished I could take the question back, and leave it unasked. I thought: Huge spidery creatures. Like the one in the shower that morning. I’m afraid of spiders.

BOY: They look like what you aren’t expecting. What you aren’t paying attention to.

BOYFRIEND: We were climbing wooden steps now. I held on to the railing on my left, held his hand with my right, as he walked beside me. It smelled like dust and old wood, that high in the house. The boy’s tread was certain, though, even though the moonlight was scarce.

BOY: Do you know what story you’re going to tell me, to put me to bed? It doesn’t actually have to be scary.”

BOYFRIEND: Not really.

BOY: Maybe you could tell me about this evening. Tell me what you did?

BOYFRIEND: That won’t make much of a story for you. My girlfriend just moved in to a new place on the edge of town. She inherited it from an aunt or someone. It’s very big and very old. I’m going to spend my first night with her, tonight, so I’ve been waiting for an hour or so for her and her housemates to come back with the wine and an Indian takeaway.

BOY: See? (smiling)

BOYFRIEND: (to audience) There was that precocious amusement again. But all kids can be insufferable sometimes, when they think they know something you don’t. It’s probably good for them.

BOY: You know all that. But you don’t think. You just let your brain fill in the gaps.

BOYFRIEND: (to audience) He pushed open the door to the attic room. It was perfectly dark, now, but the opening door disturbed the air, and I heard things rattle gently, like dry bones in thin bags, in the slight wind. Click. Clack. Click. Clack. Like that. I would have pulled away, then, if I could, but small, firm fingers pulled me forward, unrelentingly, into the dark.
```

---

## IC-0985: Cold Storage

- Title: Cold Storage
- Author (byline): Ronald Ribman
- Work: Not specified
- Publisher: Avon Books
- Publication date as stated: Sept 1983
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: PARMIGIAN, LANDAU
- Teaser before the introduction: Yes
- Spoken words (computed): 1738
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ronald Ribman
ISBN: 978-0380400065
Publisher: Avon Books
Date (Month/Year): Sept 1983
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: “You have cancer.”

ACTOR 2: The tragically-common, often literal death sentence no one wants to hear.

ACTOR 1: What do you do? How do you respond to those life-threatening words?

ACTOR 2: Chemotherapy, radiation?

ACTOR 1: Humor or depression . . . denial?

ACTOR 2: In Cold Storage by Ronald Ribman, we meet two men with very different responses to the diagnosis of cancer.

ACTOR 1: Some see a hopeless end, while others see an endless hope.

TOGETHER: Cold Storage by Ronald Ribman
```

### Performance text (classify this)

```text
(LANDAU takes a bite of a candy bar which is stale and tastes bad, he tries to re-wrap it and looks for a place to throw it away)

PARMIGIAN: You're squashing it. You’re squashing it!

LANDAU: What?

PARMIGIAN: If ya don't want it give it to me! (pause) There's no point in squashing something just because you don't want it! What are you saving it for Halloween?

LANDAU: I’ll throw (the candy) it away later there’s no garbage out here.

PARMIGIAN: Don’t throw it away later. Throw it away now. What are you in for anyway?

LANDAU: Exploratory surgery.

PARMIGIAN: Oh yeah? What are they exploring for? Cancer? (laugh)

LANDAU: It was just a shadow on an x-ray of my stomach, a few cells they weren’t quite sure about.

PARMIGIAN: Sure

LANDAU: Really just a small twinge. I don’t even feel it anymore.

PARMIGIAN: Whatta ya working on, Landau?

LANDAU: I don’t understand

PARMIGIAN: Sure you understand. What are you working on? An ulcer? Is that what you’re working on for yourself? I told them I had a tickle in the throat. Honest to God, that’s what I thought I had. I came through the door and told them I had a tickle in my throat!

(laughter stops) Take my word for it. On this floor, it’s never a twinge in the stomach or tickle in the throat. You got what I got.

LANDAU: What’s that?

PARMIGIAN: The big C.

PARMIGIAN: Yep, you’re going down for the count, same as me.

LANDAU: On the contrary, Mr. Parmigian, I’m just here for exploratory surgery.

PARMIGIAN: Sure, and you’re all dressed up in your Bloomingdales pajamas. You look…. Spiffy

LANDAU: Thank you.

PARMIGIAN: You know what I weighed six months ago? 252 pounds. I looked spiffy too. I was the King Kong of the fruit and vegetable business. I had a fist like two hammocks. Now I can’t even find them anymore. I tell ‘em my clothing don’t fit me anymore, they tell me the hospital laundry must be stretching them out. Can you believe such a pack of crap? You have to be a moron to believe something like that. What did you used to do for a living?

LANDAU: I didn’t used to do anything Mr. Parmigian, I’m still doing it. I’m an investment advisor in fine art.

PARMIGIAN: Oh yeah? What the hell’s an investment advisor in fine art?

LANDAU: I recommend investment purchases in fine art to investors interested in capital appreciation. I generally handle accounts in European glass and Chinese ceramics.

PARMIGIAN: Hey that’s terrific, that’s really terrific…. Listen, Do you have any recommendations for long term growth? (he laughs – starts to cough bad).

LANDAU: Are you all right, Mr. Parmigian? Mr. Parmigian. (When he doesn’t answer him, Landau starts to get nervous) I’ll get a nurse. I’ll be right back.

PARMIGIAN: (grabbing his arm) Don’t bother. (tries to gets breath back)

LANDAU: Are you sure?

PARMIGIAN: Yes, I’m sure! I’m sure! It only hurts when I try and stay alive. When I make jokes and try to stay alive. Listen, you want to do me a favor?

LANDAU: If I can yes.

PARMIGIAN: Don’t worry, it’s just a little favor. Get behind me and push me off the roof.

LANDAU: What?

PARMIGIAN: I’d do it myself but I don’t have the guts.

LANDAU: I really don’t think you ought to joke about that.

PARMIGIAN: You think it’s a joke? Come on be a sport, do it now and you’ll be just in time for the six o’clock news. “Incredible man splatters to death on pavement in front of Hope Memorial Hospital.” You’ll be famous for five or six minutes.

LANDAU: I have no desire to be famous at the cost of somebody else’s life.

PARMIGIAN: I’ll make it interesting for you. As soon as you push me off the roof I’ll go into a triple summersault fold up like a jack knife and do a swan dive through the entrance awning. You live another six months you won’t see that again.

LANDAU: I’m not going to listen to this. I don’t know whether you’re joking or not but I’m not going to listen to this.

PARMIGIAN: Alright I’ll do it myself.

LANDAU: No!

PARMIGIAN: Take your hand off me or I’ll bite it off!

LANDAU: You’re not going to bite anything off.

PARMIGIAN: I’m warning you. Aright, you win. I don’t have the energy to fight with anybody. I want a Doctor Pepper. Go inside and get me a Doctor Pepper I’m thirsty.

LANDAU: Not now.

PARMIGIAN: What’s the matter? It disturbs you?

LANDAU: Seeing somebody try to take their own life? Yes, it disturbs me. Nobody has the right to do something like that.

PARMIGIAN: Why not? Whose life is it?

LANDAU: That’s not the point. The point is… Look they’re coming up with something.

PARMIGIAN: They’re coming up with nothing.

LANDAU: Don’t say that. They’re making fantastic progress all the time. Just last Sunday I read and article in The Times about how cockroaches can’t get cancer.

PARMIGIAN: That’s wonderful news if you’re a cockroach.

LANDAU: That’s not the point. If they can’t give cockroaches cancer, maybe they can find out what it is that prevents cancer.

PARMIGIAN: You want to know what prevents cancer? Death! Death prevents cancer.

LANDAU: Well, with that attitude you might as well just give up.

PARMIGIAN: I have. Push me off the roof.

LANDAU: Look, I can’t handle this kind of thing right now! I just (catching himself then offering up hope of ending the conversation.) You’re just depressed. Tomorrow you’ll be glad you’re still alive.

PARMIGIAN: No I won’t.

LANDAU: Yes, you will, believe me.

PARMIGIAN: No, I won’t, and why should I believe you?

LANDAU: Because people SURVIVE! They go on! They live. Nobody tries to commit suicide unless they’re depressed.

PARMIGIAN: I happen to be in a very good mood Mr. Landau or hadn’t you noticed? The sun is shining; the dogs are peeing all over the side walk. The best time to commit suicide is when you’re in a good mood. I tried to commit suicide three times this month, and never once was I in a bad mood.

LANDAU: Why do you insist on involving me with this?

PARMIGIAN: To tell you the truth, the reason I asked you is that I don’t have the courage myself. What I said about not having any guts is true, literally. They took out my bladder, shaved off my prostate, and tied my bowels to my hip bone. See… Now my urine flows with my blood, and when I shake my leg, my liver drips prostatic fluid on my shoes. And that’s the good news. Want to hear some bad news? Last week I ran outta Blue Cross.

LANDAU: Oh, I’m sorry. It must be terrible watching your estate being destroyed by an illness.

PARMIGIAN: It’s not an estate; it’s a fruit and vegetable business. It’s always been my dream. I’ll tell you what, Landau. You tell me your filthy dreams and I’ll tell you mine.

LANDAU: I have no dreams that would interest anybody.

PARMIGIAN: You would be surprised at what interests me. The closer I get to death, the more everything interests me. Dreams other people throw out with the garbage I can spend a whole day living on.

LANDAU: I have no dreams of interest to anybody.

PARMIGIAN: What an absolutely marvelous quality of surface veneer you have, Mr. Landau.

LANDAU: If you’re interested in surface veneer, perhaps I might show you something in a 19th century Chinese lacquer box. You might find it interesting to see how coat upon coat of lacquer can be laid down until the box itself may be removed leaving nothing behind but the form and the lacquer – the black, brilliant, slightly poisonous lacquer. (pause) I’m sorry to disappoint you, Mr. Parmigian, but there’s nothing in me you’re going to be able to live on. I’ve got nothing to give you.

PARMIGIAN: Nothing?

LANDAU: Nothing.

PARMIGIAN: All right, I’ll accept that lie. There’s no point in being too pushy the first ten minutes you meet somebody. First you should break the ice, so I’ll give a riddle. What’s shaped like a big green football with four legs and a tail?

LANDAU: How outrageous you are.

PARMIGIAN: Not the answer.

LANDAU: I don’t know the answer.

PARMIGIAN: A watermelon.

LANDAU: A watermelon doesn’t have four legs and a tale!

PARMIGIAN: I lied. Where are you going?

LANDAU: I have an appointment down in the x-ray room this afternoon. I have to swallow something and they’re going to x-ray it.

PARMIGIAN: That’s a terrific test. You’ll like it.

LANDAU: You had that test?

PARMIGIAN: Oh sure. That’s one of the best procedures in the hospital.

LANDAU: I’ll be home in a few days. Time enough to have a few friends over for dinner.

PARMIGIAN: Oh yea, that’s right. You’re just in for an exploratory. I forgot. Tell me something, Landau. You seem to be in pretty good physical shape. You do something?

LANDAU: I play squash a couple of afternoons a week, and on the weekends some tennis if I can get away.

PARMIGIAN: Listen, your cardiovascular system stays in good shape there’s no reason why you couldn’t go on living until this time next year.

LANDAU: I wish you’d stop doing that.

PARMIGIAN: Doing what?

LANDAU: Implying that there is something wrong with me.

PARMIGIAN: Was that what I was doing?

LANDAU: YES! THAT’S ENOUGH!

PARMIGIAN: If you don’t like what I’m saying push me off the roof! You’re a pretty violent man, Mr. Landau.

LANDAU: I’m not violent. You just irritated me, that’s all. I hate violence.

PARMIGIAN: It doesn’t pay to get irritated. You’ll probably be out in two or three weeks.

LANDAU: You think so?

PARMIGIAN: No.

LANDAU: What’s the matter with you?

PARMIGIAN: That’s pretty obvious isn’t it?

LANDAU: I’m not talking about that. You don’t seem to give an ounce of thought to what you’re saying! You don’t know anything about me!

PARMIGIAN: That’s right.

LANDAU: You bet that’s right so knock it off!

PARMIGIAN: I apologize.

LANDAU: All right let’s just forget it.

PARMIGIAN: Oh, what a great liar you are.

LANDAU: What lie?

PARMIGIAN: Death is knocking on your door and still you persist in lying to yourself.

LANDAU: That’s garbage! Absolute garbage!

PARMIGIAN: You deny it?

LANDAU: Yes of course I deny it!

PARMIGIAN: Naturally, of course.

LANDAU: What the hell is that supposed to mean!

PARMIGIAN: What’s the matter I touched a nerve?

LANDAU: Forget it I don’t have time for this.

PARMIGIAN: You got at least six months.

LANDAU: STOP IT! Talking to you! Trying to talk to you… it’s… it’s

PARMIGIAN: Absurd?

LANDAU: It’s humiliating!

PARMIGIAN: Of course it’s humiliating. You know why? Because the mind’s a piece of garbage. It’s never happy with what you do for it. I once took my mind down to Barbados for two weeks and you know what it said to me? “You should have taken us to Jamaica.” The real reason Adam and Eve got thrown out of the Garden had nothing to do with fruit. Because there’s nothing wrong with a piece of fruit. It’s a good laxative. God finally got tired of waiting around for thanks from the human brain.

LANDAU: Oh god . . . I’m going inside now Mr. Parmigian. I have to go to x-ray.

PARMIGIAN: Landau?

LANDAU: Yes?

PARMIGIAN: I’ll meet you out here tomorrow?

LANDAU: Okay.

PARMIGIAN: I promise you a very interesting day.
```

---

## IC-0986: Columbinus

- Title: Columbinus
- Author (byline): Stephen Karem and P.J. Paparelli
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: Dec 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TEACHER, DYLAN, DYLAN & PREP, DYLAN & AP, DYLAN & JOCK, JOCK, ACTOR 1, TOGETHER, ERIC, DYLAN & ERIC, ACTOR 2
- Teaser before the introduction: Yes
- Spoken words (computed): 1976
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephen Karem and P.J. Paparelli
ISBN: 978-1583423929
Publisher: Dramatic Publishing
Date (Month/Year): Dec 2007
```

### Introduction (context only: never use it for content warnings)

```text
Who were Eric Harris and Dylan Klebold? Together these young men were brought to the world's attention when they laid siege to Columbine High School the morning of April 20, 1999. For months before the massacre, the two had been making plans to attack their school and the people in it. We will never know answers to all of the questions left in the wake of the tragedy but this selection is designed to explore what happened before the grim events of one of the world's worst school shootings in history. Let’s go back in time to Columbine, an average high school where the first hour of the day just happens to be CREATIVE WRITING. Columbinus by Stephen Karem and P.J. Paparelli.
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Actor 1: Dylan, Diversion Officer (spoken in unison)

Actor 2: Teacher, AP (Advanced Placement – a smart one), Prep, Jock, Eric, Diversion Officer

(spoken in unison)

TEACHER: Okay, let’s critique the last of the narrative assignments. I’ll follow along with your essay and share my comments. You’re up.

DYLAN: (uncertain, in a low voice) The town, even at 1:00AM, was still. . .

TEACHER: You need to speak a little louder.

DYLAN: (a bit more confident) The town, even at 1:00AM, was still bustling with activity as the man dressed in black walked down the empty streets.

TEACHER: Great opening.

DYLAN: The moon was barely visible, hiding under a shield of clouds, adding a chill. . .

TEACHER: . . . which added a chill. . .

DYLAN: . . . which added a chill to the atmosphere. What was most recognized about the man was the jingling of his belt chains striking not only the two visible guns, but the large bowie knife, slung in anticipation of use.

TEACHER: Great details. Well done.

DYLAN: His face was entirely in shadow, yet I could feel his anger, cutting thru the air like a razor. He noticed my presence, but paid no attention as he kept walking toward a popular bar. The Watering Hole. He stopped and waited. “For whom?” I wondered, as I saw them step out. A group of college-preps . . . the second-largest spoke up

(The students in the class become the college-preps in the story.)

DYLAN & PREP: Nice trench coat dude. That’s pretty cool.

DYLAN: The man in black said nothing but I could feel his anger growing. Other preps could be heard muttering in the background . . .

DYLAN & AP: C’mon man you wouldn’t shoot us. We’re in the middle of a public place.

DYLAN: Yet the comment I remember the most was uttered from the biggest of the group, obviously cocky . . . power hungry.

DYLAN & JOCK: Go ahead man! Shoot me!!! I want you to shoot me!!! Ha, ha. You won’t . . .

DYLAN: It was faint at first, but grew in intensity and power as I heard the man laugh. (Actor 2 starts laughing; under his laugh…) For almost half a minute this laugh, spawned from the most powerful place conceivable, filled the air, and thru the entire town, the entire world . . . (As the laugh gets unbearably intense, DYLAN pulls out his an imaginary shotgun and fires on Actor 2 who falls to the ground.) The town was utterly still. He stopped, and gave me a look I will never forget. The man smiled, and in that instant, I understood his actions.

TEACHER: Ok. Stay up there. Now, before I accept this draft, let’s open it up for discussion. Comments?

JOCK: Are you serious? It sucks. I mean, what if I wrote a little story about cleaning up the school, taking out people like him? (JOCK stands) This piece of shit writes about walking around the town shooting people for no reason, and you want me to what . . . to give constructive criticism? How about "throw this maniac out, and get him some help?" Look at him. What has he done to earn anyone’s respect? While he's home after school *watching* Lara Croft with his faggot-ass friends, I’ll still be here, serving the school. What does he do? Nothing. So, that’s what he is: nobody.

TRANSITION All through high school, Dylan was quiet, shy and a bit of a loner. But after this public humiliation things began to change. He and his friend Eric Harris began to act out; first shoplifting, then vandalism. Ultimately the pair were arrested for stealing computers from a van . . . and the court ordered them both into a diversion program. Their collective anger began to grow, and it’s difficult to understand how adults at the school, at home and in the court system were so easily duped into believing that everything was OK with these two teens.

*NOTE: TOGETHER – Actors are speaking as the collective Diversion Officer assigned to both boys’ cases.

ACTOR 1: JUVENILE DIVERSION: Session 1 - April 14, 1998

TOGETHER: State your name.

DYLAN: Dylan Bennett Klebold

ERIC: Eric David Harris

TOGETHER: And you attend Columbine High School?

DYLAN & ERIC: (not in unison) Yes.

TOGETHER: And *you’ve* lived in Littleton all your life?

ERIC: No, I moved from Plattsburgh, NY . . . actually I was born in Wichita, moved to Ohio, Michigan, then to Plattsburgh. We moved to Littleton when I was in 7th Grade.

TOGETHER: Ok, Dylan, describe what happened.

DYLAN: I broke into a van. Took stuff from it. Drove away (friend’s car). Cops discovered us. Admitted to the crime.

ERIC: I broke into a car and stole $1700 worth of equipment, was caught thirty minutes later.

TOGETHER: And what do you make of your punishment? Instead of jail time you’ll be meeting with me. I mean, you must have some reaction to that.

DYLAN: I’m hoping I can get the best I can out of it and am optimistic about it. So far it sucks.

ERIC: (suppressing anger) Looking forward to it. Hopefully it will set me straight.

TOGETHER: Now, what’s your relationship with the co-defendant?

DYLAN: Co-defendant? We’ve been friends for about 4 years. Very good friends.

ERIC: He’s my best friend . . . past and current.

TOGETHER: I want you to tell me what’s going on. Look on that sheet and tell me which of the following you are having problems or difficulty with . . .

DYLAN: (looks at the sheet and checks as he reads off) Finances and Jobs.

ERIC: Anger, anxiety, authority figures, depression, disorganized thoughts, homicidal thoughts, jealousy, loneliness, mood swings, obsessive thoughts, racing thoughts, stress, suspiciousness . . . oh, and . . . (a final check) . . . temper.

TOGETHER: Eric? Please, could you try and explain?

ERIC: I . . . (Beat. A sincere, but difficult attempt to open up) Sometimes I get angry. I punch walls.

TOGETHER: Have you ever used drugs?

DYLAN: Drugs are a waste of everything. Definitely not worth it.

ERIC: I’m on medication. Anti-depressants. I’ve had drinks, smoked pot, but I don’t need that anymore.

ACTOR 2: JUVENILE DIVERSION: Session 2 – January 14, 1999

TOGETHER: So what do you think of your Diversion classes?

ERIC: The anger management class I took was helpful in many ways. If a person does not want to control his or her anger, then it can be a problem.

DYLAN: Truthfully? It wasn’t worth my time. It was an eight-hour day of pointless review and cramped conditions. I feel that I shouldn’t have had to take that class, but I’m just trying to get out of the diversion program.

TOGETHER: If you want to get through this process, no more excuses.

DYLAN: I’m working for my next-door neighbor doing yard work and landscaping . . .

ERIC: And I’ve changed my meds . . . my mood is improving and I feel better.

TOGETHER: Good. Very good.

DYLAN: Most importantly . . . (the next two lines are spoken in unison)

ERIC: I am truly sorry for what I have done.

DYLAN: I know what I did was wrong.

TOGETHER: I placed a call to your parents to discuss early termination, and they have no problems with my decision. (DYLAN and ERIC smile.)

DYLAN AS DO’s VOICE: (Reading the final diversion report) Eric did a very nice job on Diversion. He is a very bright young man who is likely to succeed in life. Seems responsible and remorseful. He suffers from depression but has changed his meds and feels better. He impressed me as being very articulate and intelligent.

(Lights on ERIC, sitting on a table holding a video camera. This is a video journal entry.)

ERIC: Well folks, today was a very important day. Today, I got a double barrel 12 gauge shotgun, a pump action 12 gauge shotgun, and a 9mm carbine. It's all over now, this is point of no return. (beat) It's weird, I don’t feel like punching through a door anymore.

ACTOR 1: January 14, 1999: ERIC HARRIS: File Closed.

ERIC AS DO’s VOICE: Dylan is a bright young man who has a great deal of potential. If he is able to tap his potential and become self-motivated he should do well in life. All in all: Nice young man, kind of goofy, and a bizarre sense of humor, he makes me laugh. (Lights on DYLAN, sitting on a table holding a video camera. This is a video journal entry.)

DYLAN: I just got back from Arizona. Can you believe it? Touring a college with my dad. . . it was cool. But they have no clue. Days from now the judgment will begin. It’s interesting knowing I'm going to die . . . everything has a touch of triviality to it.

ACTOR 2: January 14, 1999: DYLAN KLEBOLD: File Closed.

********* SCENE CHANGE *******

(DYLAN is recording ERIC. They are in his bedroom. Dylan positions the camera on a tripod or table so it can record them both. The camera should be positioned between actors and audience so action can take place facing the audience)

ERIC: Ready?

DYLAN: Ready.

ERIC: Ok, it's about 1:30AM. Less than 48 hours to Judgment Day. We want to take you on a tour of what we've been up to over the last few months. Welcome to the arsenal of freedom. Better known as my bedroom. My parents are a bit too trusting.

DYLAN: Ah . . . they're clueless.

ERIC: Anyway, they don't come in here. I keep it clean. They stay out. Ok, here we've got a pretty awesome supply of crickets and pipe bombs. These are for the first ten minutes. Smoke 'em out. Scare 'em out. Then Molotov's if we get bored. Mix and match . . . Ok, let’s clear up a few things with you people so we’re not (does the quote fingers) “misunderstood.” We are kind of a select case here. Don't think this will happen again.

DYLAN: We're not like those kids in Arkansas. Idiots got caught.

ERIC: I hope you realize what we are implying: the most deaths in U.S. history.

DYLAN: The police, the parents, the world will be studying these videos.

ERIC: And don't blame the gun shows or Kmart for selling us shit—

DYLAN: Yeah, I don’t want no laws on buying PVC pipes.

ERIC: And don’t blame the school--

DYLAN: Yeah, the administration is doing a fine job as it is.

ERIC: (cuts him off ) And don’t blame my family; they’re the best parents I have ever known. Do NOT blame anyone but me and *Dylan*!

DYLAN: This was our choice. Our decision.

ERIC: (pushing Dylan out of the camera) It’s hatred that fuels this fire. See, even you are hating us right now. But I’ll tell you something. You made me. You made US.

(flipping an obscene gesture toward the camera.) Look at what you made. It’s war. And in war there are victims. We . . . the victims. (into the camera) But this . . . all of this is the end of that. (Close to the camera.) I have so much rage inside me. Worst than a loaded gun because you just don’t expect anything vicious from silence. Silence is deadly. The longer the silence, the more deadly. Shhhhhhh! (turns camera off - LONG BEAT)

DYLAN: Okay . . . So this is a bizarre question, but how do you really think it will end?

ERIC: Well, we're not getting out of there alive—not with all those cops out there. So, the best way to go is a shootout.

DYLAN: And then?

ERIC: Then what? We're dead. We're history . . . the greatest school shooting of all time.

DYLAN: We're going to be dead in two days. You're not scared?

ERIC: Look, we have always been set on this. We put guns to our heads and count one, two three. That is the plan. It is what I will do. And I need you to do it. Like we planned.

DYLAN: (Beat) What if I don’t?

ERIC: What did you say?

DYLAN: What if you shoot first, but I decide not to? What are you gonna do then?

ERIC: (erupts) Jesus Christ, what do you want, Dylan? You want to live this life? I'm done. Ok? I want one last memory. (beat) Go on. You can *kiss* ass until the day we throw our little caps in the air and sing “Columbine. Oh Columbine?” And Miss Valedictory gives her prize-winning speech about how wonderful it was at Columbine High School. . . I’m not going to sit there to listen to bullshit. No way. They don’t deserve one more day past Tuesday. I want them to feel they almost got away with it. One last prom. One last yearbook picture . . .

DYLAN: You’re not taking it, are you?

ERIC: What?

DYLAN: (picks up a medicine bottle) Your medicine. You’re pretty *messed* up . . .

ERIC: What . . . you’re worried cause I’m angry? We're gonna kick start a revolution. We’ll be remembered forever. Like gods man, like gods . . .

DYLAN: Think of their faces . . .

ERIC: The ones on fire, screaming for help . . .

DYLAN: The world noticing our little high school, engulfed in flames.

ERIC: The power we'll have . . . Like gods, man, like gods. (long beat)

********* SCENE CHANGE *******

ACTOR 2: To this day, the parents of Eric Harris have never spoken publically about their son or his role in the shootings. Ten years after Columbine, Oprah Magazine published an essay written by Susan Klebold. (ACTOR 1 hands ACTOR 1 a piece of paper.)

ACTOR 1: (reads with great emotion, the words of his mother) My son Dylan . . . I failed to see that he needed help. (beat) I will never be able to explain or excuse what he did. For the rest of my life, I will be haunted by the horror and anguish he caused. I cannot look at a child without thinking about how my son's schoolmates spent the last moments of their lives. Dylan changed everything I believed about love. I think I believed that if I loved someone as deeply as I loved him, I would know if he were in trouble. My maternal instincts would keep him safe. But I didn’t know, and my instincts weren't enough.
```

---

## IC-0987: Coming Attractions

- Title: Coming Attractions
- Author (byline): Ted Tally, Jack Feldman and Bruce Sussman
- Work: Plays from Playwrights Horizons, Pgs 273 - 326
- Publisher: Broadway Play Publishers
- Publication date as stated: May 1987
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: COP 1, LONNIE, MANNY, COP 2, NEWSMAN, TV REPORTER, CHIEF BRADDOCK, TV NEWSMAN, MISTER X, MISS AMERICA, SHRINK, SAMMY
- Teaser before the introduction: Yes
- Spoken words (computed): 1736
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
ACTOR 1: Small-time crook Lonnie Wayne Burke is a born loser when it comes to crime.

ACTOR 2: But with the help of streetwise theatre agent Manny Alter, he becomes the next media sensation following in the footsteps of . . .

ACTOR 1: Charles Manson ACTOR 2: David Berkowitz ACTOR 1: Ted Bundy

ACTOR 2: This selection looks at our celebrity-obsessed society and the lengths to which some will go for fame and fortune.

TOGETHER: Coming Attractions by Ted Tally, Jack Feldman and Bruce Sussman
```

### Performance text (classify this)

```text
Suggested Roles: Actor 1 – Lonnie, Cop 2, Newsman, Chief Braddock, TV Newsman Actor 2 – Manny, Cop, TV Reporter, Mister X, Miss America, Shrink, Sammy

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

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

MANNY: You'll be back on the streets in 24 hours. (yells to police outside) He’s coming out! Don’t shoot! (to audience as Lonnie exits with his hands up) Tell you the truth, I had doubts. I mean, he wasn't exactly another Manson or a Berkowitz. He lacked your true weirdness factor, if you know what I mean. But I figured with training and a little luck, we could simulate some craziness. ********* SCENE ********

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

MISTER X: (with a horrible French accent) You want proof? (points finger like a gun) Bang!

Bang! Trick or treat, you bourgeois pig!

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

## IC-0988: Conversations with my Father

- Title: Conversations with my Father
- Author (byline): Herb Gardner
- Work: Not specified
- Publisher: New Fireside Theatre
- Publication date as stated: 1993
- Event as filed: Duo Interpretation
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
ACTOR 1: Fighting never solved anything . . . . use your words, not your fists. . . . Mothers just don’t get it. Sometimes you have no choice but to fight. It’s a matter of pride.

ACTOR 2: And defending your heritage. The year is 1936 and in this scene, Jewish born Eddie Goldberg has escaped to America and made a new life for his family in New York.

ACTOR 1: Out of the frying pan and into the proverbial fire for 10 year old Joey, who is being harassed by another boy in the neighborhood. Fortunately, his father has a better answer to the dilemma than his mother.

TOGETHER: Conversations with My Father by Herb Gardner.
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

## IC-0989: Coyote on a Fence

- Title: Coyote on a Fence
- Author (byline): Bruce Graham
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Aug 2000
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BOBBY, JOHN, SAM, SHAWNA
- Teaser before the introduction: Yes
- Spoken words (computed): 1222
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bruce Graham
ISBN: 978-0822217381
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Aug 2000
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Welcome to Death Row. * This year, as of November 1, 2024, 21 prisoners have been executed in 8 US states, with over 2,200 still awaiting execution. (update as needed)

ACTOR 2: And while the number of death sentences per year have dropped dramatically since 1996, 27 States, the US Federal Government and the US Military still retain it as a sentencing option for heinous crimes.

ACTOR 1: ** President-elect Trump, during his 2024 campaign for re-election, signaled his stance on capital punishment -- indicating he would make more people eligible including child rapists, migrants who kill US citizens and those convicted of drug and human trafficking.

ACTOR 2: How do you feel? Is the death penalty warranted for these types of crimes; or are you against this form of punishment?

ACTOR 1: The State vs Robert Alvin Reyburn provides the backdrop for this drama . . .

TOGETHER: Coyote on a Fence by Bruce Graham
```

### Performance text (classify this)

```text
Suggested Roles: Actor 1: Bobby Actor 2: John, Sam and Shawna

Bobby – White Inmate on death row; late 20s, skinny, pale, damage to one of his eyes John – White inmate on death row; mid 40s; writes obituaries for “The Death Row Advocate” Sam – Reporter from the NY Times – 30’s Shawna – Prison guard, race doesn’t matter.

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

BOBBY: (Pg 44) (singing as he bounces a ball, he appears almost childlike and when he doesn’t know the words he uses “da, da”) “God rest ye Merry gentlemen, let nothing you da, da. Remember Christ our savior was born on Christmas day.

JOHN: (Pg 49) In seventy-two hours they are going to kill you.

BOBBY: And I will go to a better place. (Pg 51) That’s in the Bible, John. (returns to his ball bouncing, which he enjoys very much) (Pg 46) Dashing through the snow, in a one horse open sleigh, o’r the fields we go, laughing all the way ha-ha-ha (Bobby breaks into giggles)

JOHN: (Pg 49) If I could get that on tape and show it to a jury, they’d never kill you. You’re runnin’ around like a happy puppy or something.

BOBBY: (blank look; John has lost him, but he understood the word “puppy” and he begins to imitate one, taking the ball in his mouth and making puppy noises) I’m a happy puppy!

BOBBY: (Pg 27) (to the audience) God spoke ta me a lot. . . but that mornin' . . . I'm passin’ a church - had an old pick-up Uncle Hew gimme - and I could hear 'em in there . . . singin’ . . . Beautiful singin’.

SAM: (Pg 32) [His] mother was a transient. Did some prison time herself: prostitution, public drunkenness, assault.

BOBBY: (Pg 27) I pull over and just listen. And then God said, "Help them, Bobby. You gotta’ help those people . . . show them the way home!"

SAM: (Pg 32) Drunk all through her pregnancy. Got beat up pretty bad when she was seven months along. Between the booze and the beating, they’re pretty sure the fetus suffered a little . . . damage.

BOBBY: (Pg 28) So I went in..."Excuse me Reverend? I need to speak the word of God!"

SAM: (Pg 33) He never made it out of the seventh grade.

BOBBY: (Pg 28) Got real quiet...everybody starin’ at me. But I didn't feel no hate. (to the congregation) "God has spoken to me! He wants you all to know it is immoral for whites and n**** ta live together.”

BOBBY: (Pg 28) (shocked) They turned on me. Started clawin’ at me like animals--you believe that? I was tryin ta help them! (A deep breath).

SAM: (Pg 35) Mother had him put in the juvenile detention center for running away. He was twelve – other kids were older. Whole dorm – first night. Got a little rough, shattered his hip.

BOBBY: (Pg 28) I got in my truck, drove down the road... (Bobby laughs in God’s voice, then speaks in awe) It was God! (in God’s voice) “They mock you, Bobby, they mock me! They must be cleansed!” I turned around and headed back. They're singin’ again--real loud--so I pulled the truck right up to their door there. Parked it, got out my gas can, made a big ring. Let the circle be unbroken. (beaming) Sat under a tree and watched . . .

SAM: (Pg 33) Fire killed thirty-seven people. Fourteen of them kids. Sunday school in the basement. He didn’t just confess, he made a proclamation. Took full responsibility.

JOHN: (Pg 33-34) The trial . . . There was no medical testimony. There was no psychological testimony. He’s not competent enough to take responsibility. Bobby totally disassociates. He shouldn’t be on the row!

BOBBY: (Pg 20) Hey, I ever do my penguin for ya? Watch this (he begins to waddle around like a penguin) (Pg 23) (begins to frantically look for something – he’s suddenly in a panic) Where’s my towel? I need my towel!

JOHN: Here! Take mine if it’ll shut you up! (he shoves his towel into Bobby’s cell)

BOBBY: (Bobby grabs it desperately and holds it tightly to his chest) They done this before. They want my other eye. They got this one when I was sleepin’ but they ain’t gettin’ the other one. (whispering intently) That’s when they get ya – when you’re sleepin’. They get bleach outta’ the laundry and throw it in your face. Burns . . . Lord it burns. So I always gotta’ sleep with a towel over me.

SHAWNA: (Pg 36) They’re all bullshitters. (mocking) I’m poor, I’m black, daddy beat me, momma didn’t love me.

BOBBY: (Pg 30) Seal! (tries to balance a ball on his nose, slaps his hands and makes seal sounds)

SAM: (Pg 35) (quiet but intense) I am against the death penalty (pause) I think people like Bobby are evil. I know that’s probably . . . simplifying things a little too much. But (shrugs) I keep picturing thirty-seven people frightened out of their minds, knowing they’re going to die. Sorry – I just can’t work up a lot of sympathy over someone like him.

BOBBY: (Pg 30) Hey, I ever show ya my toad? (crouches down, makes toad sounds and mimes catching a fly, then jumps up laughing)

SHAWNA: (Pg 36) (Shakes her head) Never take responsibility. Bad family, bad neighborhood. “I’m a victim of society” I am so sick’a that. How ‘bout your victim, huh? (long pause)

*****

JOHN: (Pg 10-11) Silence for a change. (deep breath, heavy sigh, beat) They murdered Willie T. last night. That’s why it was quiet. They never announce in on the row, but we all know when it happens. We know even before the crowd outside begins to cheer. And the silence rolls in, one cell at a time. (rubs his face, tired) *****

BOBBY: (Pg 52) (to audience) They have coyotes where you grew up? . . . Nasty animals. Wipe out a whole chicken house in one night. Hate coyotes more than anything. (howls like a coyotes, then is quiet for a moment, thinking back) I know, I seen it. Just got outta’ the hospital ‘cause’a my hip

SAM: (Pg 42) (to John) Now let’s talk about the obituaries. The angle of my article is that you try to . . . undemonized these men.

BOBBY: (Pg 52) So one day, my mother--I tell her I wanna go to Uncle Hew's but she--heck--she couldn't got me there if she wanted to and this man's she with, he...so I walked—(Laughs) Well, limped. Six miles outta town. man-oh-man it hurt.

JOHN: (Pg 42) Undemonize?

BOBBY: (Pg 52) Just wanted to get to my uncle's. I can see the lights and. . . man-oh-man I almost peed myself--cause there's this. . . monster!

SAM: (Pg 42-43) Find the positive . . . whatever. But Willie T. was an animal! Mutilating a twelve-year old boy is not the act of a human being.

BOBBY: (Pg 52) And it's floatin in the air, and I can see its eyes and--- I burst in on poor Hew shaki’n and cryin’ --didn't even know I was comin,’ but he hugged me and put me in the truck and drove on out there. Coyote—that’s all it was – He’d shot it and stuck it up on the barbed wire. Beat on it too, while it was wounded.

SAM: (Pg 43) Sneer all you want, John. You people frighten us. We are not the bad guys just because we want to protect ourselves.

BOBBY: (Pg 52) He told me ‘bout coyotes bein’ evil and how it’s okay ta kill ‘em. That’s why he stuck it up onna’ fence. Let the world know -- death to predators. (simply) Then he told me all about the Jews. How Hitler knew they were predators. How they was usin’ the n***** and mud people to turn us all into animals so they can enslave us. (a beat, then to John) (Pg 49) Watcha’ gonna say ‘bout me? Inna’ paper. I mean, ya are gonna’ write somethin’ ‘bout me, right. Put my name in there.

JOHN: Wish I didn’t have to – What would you like.

BOBBY: Well . . . that I was a good Aryan soldier and upheld the code. (Pg 17) (springing to attention) I am Aryan!! If I am incarcerated I will remember at all times my duty as an Aryan!

JOHN: (Pg 49) I’m not putting that crap in my paper – (Pg 19) 70% of our readership is African- American.

BOBBY: (Pg 49-50) Then don’t write nothin’ ‘bout me.

JOHN: I don’t have a choice here. (pause) Remorse, Bobby. Give me that at least, please. That’s the one thing I can always fall back on – showing some remorse. Tell me you’re sorry you killed 37 people.

BOBBY: (Pg 51) There’s nothin’ wrong with killin’ a predator. Ol’ Hew said it. Predators must be destroyed. *****

SAM: (Pg 54) The state murdered Robert Alvin Reyburn last night. He was twenty-eight years old. Bobby was accused of a heinous crime.

JOHN: [He] never denied it. In his own unique way he was an honest man.

SAM: He did animal impressions. Forgot the words to songs. (pause) St. Francis once said, "Where there is charity and wisdom . . .

JOHN: . . . there is neither fear nor ignorance." Bobby Reyburn knew no charity or wisdom in his life. (sighs sadly) And the only person who ever loved him taught him how to hate.
```

---

## IC-0990: Daniel on a Thursday

- Title: Daniel on a Thursday
- Author (byline): Garth Wingfield
- Work: Take Ten II: More Ten-Minutes Plays
- Publisher: Vintage Books
- Publication date as stated: Nov 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: KEVIN, DANIEL
- Teaser before the introduction: Yes
- Spoken words (computed): 1779
- Already set (do not supply): none

### Source block (context only)

```text
Author: Garth Wingfield
Book: Take Ten II: More Ten-Minutes Plays
ISBN: 978-1400032174
Publisher: Vintage Books
Date (Month/Year): Nov 2003
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: My friends tell me all the time how bored they get with dating.

ACTOR 2: “It’s the same date every time.”

ACTOR 1: (mimicking) “I just go to the same place, and end up on the same date!”

ACTOR 2: “It’s like Ground Hog day … same date, different guy!”

ACTOR 1: Well, I’m here to tell you that YOU are in charge of your own dating destiny!

ACTOR 2: Things just feel so repetitive and dull . . .

ACTOR 1: Then do something different. It’s time to change things up!

TOGETHER: Daniel on a Thursday by Garth Wingfield.
```

### Performance text (classify this)

```text
(A crowded bar. ABBA’s Take a Chance on Me* plays in the background (One or both characters may be singing along with the lyrics). Two guys leaning against a wall, facing out, nursing drinks. KEVIN eyes DANIEL for a moment. Then DANIEL, sensing he's being cruised, turns, gives him a once-over.)

KEVIN: Hey.

DANIEL: (weakly, not encouraging) Hey.

KEVIN: (Extends his hand.) It's Kevin.

DANIEL: Right ... Kevin ... I don't mean to be rude. I'm sure you're a nice guy and all. It's just, I really don't feel like talking tonight.

KEVIN: Oh. That's fair. (Beat.) So that was my one chance with you, and I just blew it, right? Is it my body? Is my body this major turnoff? Or my hair?

DANIEL: Of course not! You're a perfectly nice-looking guy-not my type, as it turns out-but perfectly nice looking . . . Anyway. Good talking with you. (Beat. They both face out again.)

KEVIN: So let me get this straight. Even though I don't disgust you outright-and I don't actually disgust you, do I?

DANIEL: You don't disgust me!

KEVIN: Even so, you wouldn't shake my hand.

DANIEL: What are you talking about?

KEVIN: I held out my hand to introduce myself, and you wouldn't take it or tell me your name even. It's a handshake! A HANDSHAKE!

DANIEL: Oh my God, no-NO! I didn't mean to / insult you, believe me.

KEVIN: (cracking up) Daniel! Take it easy, man! It's Kevin . . . Kevin Carpenter. From high school. I'm just screwing with you, buddy.

DANIEL: Kevin Carpenter?

KEVIN: From history class. I saw you just now and said to myself, "Well, if it isn't little Daniel Delmonico from high school in a gay bar. I haven't seen him in years. I know what! I'm gonna go over and mess with his head."

DANIEL: No, that's . . . Wow, you know . . . I've gotta be honest here. I don't remember you at all.

KEVIN: You don't? No, that's cool. It's not like we were ever friends or anything.

DANIEL: We weren't.

KEVIN: Not at all.

DANIEL: (not sure about this) Right ... But ... it's good to finally meet you now. After all these years. (little smile) You know, this is actually very cool because ... the whole time I was in high school, I was fully convinced I was the only gay person there.

KEVIN: You may well have been. I'm straight. Hundred percent hetero.

DANIEL: But this is a gay bar ....

KEVIN: I know that.

DANIEL: So ... what are you doing here?

KEVIN: I don't know, I was walking down the street, , and I saw this place-and hey, I enjoy an old Golden Girls episode as much as the next guy. Gay people are A- OK by Kevin Carpenter. (low) Don't worry, I won't tell the old gang your little secret.

DANIEL: What secret?

KEVIN: That I saw you here.

DANIEL: Actually, that's not a secret really ... and ... what old gang?

KEVIN: Your pals from high school. Daniel's old buds.

DANIEL: But I didn't ... back then, I didn't have that many close ... (suspicious) Exactly who was in my old gang?

KEVIN: You know. (reaching) Like ... Mary ... Bill ...

DANIEL: I didn't know anyone by those names, Kevin. So I'm pretty sure you've got / the wrong guy.

KEVIN: (cracking up) GOTCHA! Two for two for the Kevinator! I totally had you going there, didn't I?

DANIEL: So you didn't go to my high school. ...

KEVIN: Negatory. I've never even seen you before tonight. But you were buying it, the whole thing, I could tell. Right up to the Bill and Mary part.

DANIEL: Look! Kevin! Why don't you just leave me alone, okay? I said I didn't want to talk to anyone, and I don't know why you 're doing this to me. So just ... let's just say ... good night.

KEVIN: Hey, I hear ya. Nighty night. (They both stare forward for a moment.)

DANIEL: (still out, low) How did you know my name?

KEVIN: (Giggles.) I knew you were gonna say that.

DANIEL: HOW THE HELL DID YOU KNOW MY NAME?!

KEVIN: (getting angry himself) Whoa ... easy there, Paco. Someone left his ATM card at the cash machine next door. With his name imprinted on it. I called out to you on the street, but you didn't hear me. That's why I followed you in here. I couldn't give a flying flapjack about The Golden Girls. (Handing him back his ATM card.) I was being Kevin Good Guy. Got it?

DANIEL: Well ... that was very nice of you. (Hates to say this.) Thank you ...

KEVIN: (still testy) Damn right about that. (Then, suddenly bright.) Say, lemme buy you a [drink]!

DANIEL: No, Kevin, please ... I just want to finish this one and go home.

KEVIN: Oh, come on! What're you drinking? Beck's? I'll bet you always drink Beck's. I bet you've been drinking Beck's for years.

DANIEL: That's ... I have.

KEVIN: Well, prepare to break new ground, my friend, because tonight you are drinking a Breezer. Voila! (He pulls bottled Breezer from the inside pocket of the jacket he's wearing, twists off the top, and hands it to DANIEL.)

DANIEL: Okay, you ... so you always bring your own ... ?

KEVIN: (insulted) Jeez, ixnay on the udgment-jay. I'll have you know I bought this legit from the bartender before I walked over here. (Significantly.) I knew I could convince you to drink it. I walked in here just as you were buying your [Beck]. And I watched as you took the change and filed it away methodically in your wallet, making sure all the bills faced in the same direction, and I said to myself, "That guy-Daniel Delmonico from the ATM machine really needs my help."

DANIEL: I don't always do that / with my money.

KEVIN: He's in a rut, and I'm gonna do my part to pull him out of it. I'm gonna make him switch drinks, if only for a Breezer. It's a baby step, but there you go."

DANIEL: (a little wounded) I'm not in a rut.

KEVIN: Please, you're here every Thursday!

DANIEL: (suspicious) How do you know that?

KEVIN: (fast) Ummmm-I'll bet. I'll bet is all I meant. You just seem like that kind of guy. If it's Thursday night, it's Daniel at this bar. Am I right? And why is that, Daniel? Is your life so empty that you feel you have to cling to these meaningless little rituals?

DANIEL: What? No ... No . . . this means nothing!

KEVIN: Oh, it means plenty, Daniel. It speaks volumes about you. On the subway platform each morning, where you do stand? Anywhere? Or always in the same exact spot because you know where the train doors will open?

DANIEL: Look, just because you bought me a drink doesn't entitle you to grill me like this!

KEVIN: Grill? Who's grilling? I'm merely observing. And asking. Observing and asking. And what's with this type thing? What's that about?

DANIEL: (Stops at this.) What ... type thing?

KEVIN: Apparently, I'm not your type. Or so you said.

DANIEL: You're NOT GAY!

KEVIN: That's not the point. What is your type? I bet I can guess it. Latin guys.

DANIEL: (startled) Why would you guess that?

KEVIN: It's Latin guys, isn't it? Isn't it? I'll bet it is. It's Latin guys. Isn't it?

DANIEL: YES! I'M INTO LATIN GUYS! SO WHAT?!

KEVIN: So what? I'll tell you so what, Daniel Delmonico from the ATM machine. You're losing out on a world of possibilities and, and experiences that have nothing whatsoever to do with Beck's or Bea Arthur and Betty White. I don't mean to crawl up on a soapbox here but you are severely limiting yourself in many aspects of your personal life.

DANIEL: (bemused) Oh, am I? Well, in my own defense, I'd like to point out that I happen to like my life exactly as I've made it. I like knowing what I'm getting.

KEVIN: Loosen up, Dan.

DANIEL: It's Daniel, Kev.

KEVIN: Right, fine. Daniel. Let's take what happened with us here tonight-and let's forget about my wife, Viveca, for the moment. And our daughter, Amber, and Helaine, our little finch bird. Let's talk theoretically.

DANIEL: Theoretically . . .

KEVIN: A guy walks up to you in a bar. Me. This stranger could hold the possibility of, I don't know, one-night that blossoms into a deep friendship involving marathon phone calls and hilarious e-mails! Or. OR! This stranger could be the man you were supposed to spend the rest of your life with. The man you've been waiting to meet ever since you had a crush on your fifth-grade math teacher.

DANIEL: I didn't realize I was gay until high school.

KEVIN: Uh-huh, and so this stranger turns to you. Me, I do that. And I say, "Hey," and you say, "Hey," but that's where it stops in your mind because my name probably isn't Hernando.

DANIEL: Kevin ...

KEVIN: That's no way to wander through the world, my friend. But ... (Glances at his watch.) Sheesh, I've gotta get going. It's Amber's birthday today. She turned four. She's gonna get her first Barbie in about half an hour.

DANIEL: Wow, really ... tell her happy birthday for me.

KEVIN: Will do. Hey, you have a good night, Daniel Delmonico. It was cool sharing a drink with you.

DANIEL: Yeah ... Yeah, it was. (KEVIN starts to go, then stops.)

KEVIN: May I ask you just one more little question? Now that we've talked, now that you know me a little ... would you give a card-carrying Caucasian guy like me a chance? (Then.) You would, wouldn't you? Wouldn't you? You would. Wouldn't you?

DANIEL: (laughing, frustrated) CHRIST, YOU DRIVE ME TOTALLY INSANE!! I don't know .... I guess you are sort of charming. In a totally psychotic kind of way. Sure, what the hell. (Little beat.)

KEVIN: AND SCORE THREE FOR THE KEVINATOR!!!

DANIEL: No way ... no way ... Hold on, so you're actually ... ?

KEVIN: Yep, full-on gay. Completely queer. I knew you were coming around! I could tell!

DANIEL: Get away from me, okay? Leave me alone forever, starting right now.

KEVIN: What are you talking about? We have a date to go on, cowboy.

DANIEL: Are you insane? No! No, we do NOT!

KEVIN: After all that WORK?! Do you have any idea how DIFFICULT that was, thinking on my feet like that? I totally forgot little Amber's name there for a full thirty seconds. ·

DANIEL: There is no way I am ever going on a date with you, Kevin ... if that is your real name.

KEVIN: It's actually Hernando, which is pretty ironic. (off DANIEL's look.) THAT WAS A JOKE!!

DANIEL: See, that's why I won't go out with you. That is my point exactly.

KEVIN: Oh, come on ...

DANIEL: Come on what? We could get to some restaurant, and you'd tell me that you're really a woman. Or that you're Vietnamese. Or that you're a VIETNAMESE WOMAN! And this whole thing would turn out to be some extended con! You lied to me repeatedly!

KEVIN: I didn't lie-fine, you want to know who I am? (DANIEL rolls his eyes.) I'm a guy who's been corning to this bar on Thursdays for months, who noticed you weeks ago and thought you were certifiably cute, only you looked right through me. So when you left your card at the ATM machine, it seemed like I was being given this chance. And ... I just wanted you to see me for a few minutes. For one conversation.

DANIEL: AND YOU COULDN'T JUST SAY, "HI, l FOUND YOUR ATM CARD?!"

KEVIN: Sure, but how unoriginal would that have been? And I didn't lie to you, for the record. I surprised you. I kept you guessing. And for a while there, near the end, you were pretty intrigued by me, I could tell.

DANIEL: ... I don't even know what I'm supposed to say to you.

KEVIN: How about we just ... let's just ... (Turns to him, anew.) Hey.

DANIEL: (after a pause) Hey.
```

---

## IC-0991: The Day the Voices Stopped

- Title: The Day the Voices Stopped
- Author (byline): Ken Steele
- Work: Not specified
- Publisher: Basic Books
- Publication date as stated: 978-0465082278
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, KEN, VOICE 1, VOICE 2, NEWSCASTER, HUGH DOWNS, BARBARA WALTERS, DAD, BABY BROTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1724
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ken Steele
ISBN: May 2002
Publisher: Basic Books
Date (Month/Year): 978-0465082278
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 2: For thirty-two years Ken Steele lived with the devastating symptoms of schizophrenia.

ACTOR 1: The voices arrived without warning on an October night in 1962 when Ken was 14 years old.

ACTOR 2 as VOICE: (unintelligible whispering)

ACTOR 1: Derisive voices that continually said derogatory things to and about him.

ACTOR 2 as VOICE: (harshly) Look how ugly you are. How can you bear to look at yourself?

ACTOR 1: For thirty-two years, destructive voices inhabited his disordered mind, teasing him,
```

### Performance text (classify this)

```text
NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles:

ACTOR 1: Ken

ACTOR 2: All Other Characters

KEN: (Pg 1-2) The voices arrived without warning on an October night in 1962. I was 14 years old.

VOICE 1: Kill yourself. . . Set yourself afire

KEN: I stirred, thinking I was having a nightmare, but I wasn’t asleep; and the voices -- low and insistent, taunting and ridiculing --continued to speak to me from the radio.

VOICE 1: Hang yourself. The world will be better off. You’re no good, no good at all.

KEN: Terrified, I turned off the radio, got out of bed, and crept down the hallway in my bare feet. But the voices would not be tuned out. They accompanied me.

VOICE 1: You should die.

VOICE 2: (shrieking)You should never have been born!

KEN: They were talking to me. . . someone or something wanted me to die. Who was doing the talking? What was going on? I turned the handle to the door of my parents’ bedroom, looking for safety, but my mom and dad were sleeping soundly, and I was afraid to wake them. I knew they had to go to work in the morning. And even if I woke them, what would I say? The voices supplied an answer.

VOICE 1: Go right in! Tell your dad you’re afraid of the dark and then tell him about us. It will only confirm what he already knows -- that you’re different, a disappointment.

KEN: The voices were right: This was not a man to whom I could confide that I was hearing things.

ACTOR 2 as VOICE: Worthless!

ACTOR 1: Mocking him

ACTOR 2 as VOICE: Sissy! Pig!

ACTOR 1: Driving him time and again to the very edge of life.

ACTOR 2 as VOICE: (eerily) This is how Ken’s story began . . .

ACTOR 1: The Day the Voices Stopped by Ken Steele

KEN: (Pg 2-5) I wandered down the stairs of our tidy Cape Cod-style house to my grandmother’s bedroom. Emma Mae, my mother’s mother, was my best friend. I could tell her anything and she would still love me. As I turned the knob to her room, the voices in my head grew shriller and louder until I felt I was drowning in sound.

VOICE 2: Die, die, die. You’re worthless, no good. Do it now, not later!

KEN: I staggered into the living room and collapsed on the floor. My mother found me lying there in the morning. “What are you doing up so early?" she asked, shaking my shoulder. I remember thinking that my mother had arrived, like a lifeguard, to rescue me. Nw I was safe. But my relief was short-lived. The voices were still there, lower in volume and chattering in the singsong cadence that children use to taunt one another.

VOICE 1: Na na na na na / We’re still he-ere / You thought you got rid of us / No such lu-uck.

KEN: I felt bombarded by the noise and terrified by the strangeness of what was happening. Act normal, I told myself. I washed and dressed hurriedly. I went down to breakfast and forced myself to eat. My parents soon left for work, and, as she did every morning, Grandma let me television before I left for school. As I sat in front of the TV, all these people began to talk about me.

NEWSCASTER: Today, Kenny Steele will kill himself.

KEN: An electric shock ran through my body. Had I heard right? (uses remote to change the channel) Seconds later, Hugh Downs spoke to me

HUGH DOWNS: (deeper voice) Don’t kill yourself, Kenny. Don’t give up. Try not to do it.

KEN: Barbara Walters conducted a posthumous interview with me.

BARBARA WALTERS: Why did you kill yourself? she asked. Did you really mean to do it?

KEN: I raced out the door. The voices were screaming at me.

VOICE 2: Run, run, run, you coward!

KEN: I turned right and ran past the school building but did not go in. Instead, I headed for the forest next to the school. I hoped to hide from the voices among the dense foliage, but they found me and continued their diatribe.

VOICE 1: You’re worthless. . .

VOICE 2: Your parents don’t want you around anymore. . .

VOICE 1: You could leave home. . .

VOICE 2: Better yet, you could kill yourself. . .

VOICE 1: Yes, that’s it. That’s the answer. . . Die.

KEN: (defeated) I don’t know how long I lingered in the forest that day. (long beat) A couple of weeks later, Dad came home from work excited.

DAD: The president will be speaking about the Cuban missile crisis tonight. I want you to hear what he has to say about the Communists.

KEN: As President Kennedy spoke to the nation, my voices spewed obscenities at me. It was impossible for me to hear and understand what was being said. The President concluded his talk, and Dad began to speak to me.

DAD: What are they teaching you in school

VOICE 2: Don’t listen to your father. He’s no good.

DAD: about Khruschev and Cuba and about those

VOICE 1: Don’t answer his questions. . .

DAD: terrible Communists and their plan to ravage the world?

VOICE 2: Turn your back on him! Turn away now!

KEN: (Pg 6-8) That evening, the voices won out. As my father quizzed me about what we had seen on TV, what I knew, what I thought, I did as the voices directed (overwhelmed, puts hands over ears and turns away) Dad became enraged. “Go to bed without dinner,” he ordered me, stalking out of the living room. It was a punishment he rarely imposed.

VOICE 1: Ungrateful boy, now see what you’ve done.

VOICE 2: You’ve disappointed your father [again]. Your parents deserve a better son than you.

KEN: Soon they would have one. Some time after the voices first visited me, my mother and father told me they were expecting a baby. If I have to have a sibling, I prayed, let it be a sister. But the voices knew better. They had decided the baby would be a boy, and on several terrifying occasions they made it seem as if “he” were speaking to me.

BABY BROTHER: (whispering menacingly) I am coming, I’m going to be born. You have to leave. Take a radio into the bathtub and electrocute yourself . . . Jump in front of a car at night on Route 69. . . Pour charcoal lighter fluid over your body and set yourself afire. . . Hang yourself in the forest.

KEN: My brother was born May 10, 1964 – Joseph Robert Steele.

VOICE 1: He’s here now (laughing maniacally) Joey is the good son. He’s the one they wanted.

VOICE 2: It’s time for you to go . . . Stop hanging around.

KEN: Only two things, reading and writing, could tone the voices down. When I read, I entered the world of Huckleberry Finn; I’d suffer the growing pains of Holden Caulfield. The voices would become muffled. And so I read voraciously. I read my way through the last year of junior high school and wrote frantically, scribbling page after page before the voices took over. For three years, I managed to cover up what was happening to me, or so I thought. (Pg 9-12) But the voices were stepping up their demands that I destroy myself.

VOICE 1: No simple death for you! Guts and gore and a big mess. . . that’s the way you must take your life.

VOICE 2: Get out that door. . . Run, run, run. You’ve got to die.

KEN: And so I ran away from home. I ran to the same forest in which I had sought refuge the first time the voices had descended on me.

VOICE 1: Get a rope, twelve feet long and two inches thick.

KEN: I’d gone to a hardware store and bought the rope.

VOICE 2: Tie the noose with a sea knot, and make sure it’s tied tight

KEN: I practiced tying knots. At the direction of the voices, I had also taken a step stool from the basement and hidden it in the forest, covering it over with branches and leaves. I’d bought lighter fluid and matches and left them in a small locker that I’d hidden in the same area. When all the preparations had been made, the voices were pleased with me.

VOICE 1: Good, your suicide kit is complete.

KEN: That night -- the night I ran away -- I made three different attempts on my life. First, I got up on the stool, then tied the noose around my neck. But even though I tossed and thrashed about, I couldn’t manage to kick the stool away. I had failed. Tears streaming down my face, I located the charcoal lighter fluid and poured it on my head. I could not bring myself to light a match. The highway, I thought, half running, half dragging myself in my disoriented state about a mile to Route 69. My plan was to leap in front of a car. I stood at the side of the road. Headlights were coming at me. Now! I told myself, but then I noticed a spotlight atop the car. What if this was a police car? What if the police were coming for me? Panicked, I ran back from the road, back toward the school that sat dark and deserted in the summer night. I crouched behind the building, clinging to its hard concrete walls for what seemed like eternity.

The following morning, I rose and headed for home. Two state trooper cars were parked outside our house. Dad stood in our front yard, talking animatedly with the troopers. I froze in my tracks. My dad turned and saw me.

VOICE 2: They’re going to shoot you. See the guns in their holsters? Your dad is arranging to have you killed.

KEN: My parents had called the troopers, reporting me as a runaway who had threatened suicide. Now the officers wanted to escort me to the hospital. Dad convinced them to let him take me to our family physician, Dr. Sullivan, instead. It was growing dark and pouring when we drove to the appointment. Dr. Sullivan asked if he could speak with me alone. I have no memory of what the doctor said or did, but I clearly recall the looks of worry and confusion on my parents’ faces when the doctor called them back in.

Mom, Dad, and I returned home. Later that night, I heard my father speaking on the telephone. He was talking about me. He was telling the person on the other end that I had a very serious mental illness. It had a long name, and I remember wanting to know how to spell it. That way, I could look it up in the library and learn how to get rid of the voices..

I walked over to my dad and asked him if he would spell the disease. Dad leaned his forehead into his hand and handed me a small slip of paper. On it, there was one word, neatly printed in capital letters: (begins spelling aloud) S C H I Z O . . .

VOICE 2: (interrupting) Schizo – Schizo - Schizophrenia! (laughter)
```

---

## IC-0992: Death Knocks

- Title: Death Knocks
- Author (byline): Woody Allen
- Work: Getting Even, Pgs 31-41
- Publisher: Vintage
- Publication date as stated: Aug 1978
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NAT, DEATH
- Teaser before the introduction: No
- Spoken words (computed): 1722
- Already set (do not supply): none

### Source block (context only)

```text
Author: Woody Allen
Book: Getting Even, Pgs 31-41
ISBN: 978-0394726403
Publisher: Vintage
Date (Month/Year): Aug 1978
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: The phrase cheating death is commonly used to describe the manner in which a person avoids a possibly fatal event or who prolongs their life in spite of considerable odds.

ACTOR 2: A person who cures themselves of cancer without chemotherapy, a person who avoids by a narrow margin falling off a cliff or building or being shot or stabbed, or a person who survives hospitalization in critical condition in spite of a poor prognosis from doctors all might be described as having "cheated death".

ACTOR 1: In this short play by Woody Allen, our main character, Nat, literally “cheats” death, but not in the traditional way.

ACTOR 2: He cheats Death in a game of cards!

TOGETHER: Death Knocks by Woody Allen

The play takes place in the bedroom of the Nat Ackermans' two-story house. Nat Ackerman, a bald, paunchy fifty-seven-year-old dress manufacturer is lying on the bed finishing off tomorrow's Daily News. He wears a bathrobe and slippers. The time is near midnight. Suddenly we hear a noise . . .
```

### Performance text (classify this)

```text
NAT: (Pg 31-41) What the hell is that?

(Climbing awkwardly through the window is a somber, caped figure. He huffs audibly and then trips over the windowsill and falls into the room.)

DEATH: Jesus Christ. I nearly broke my neck.

NAT: (watching with bewilderment) Who are you?

DEATH: Death.

NAT: Who?

DEATH: Death. Listen-can I sit down? I nearly broke my neck. I'm shaking like a leaf.

NAT: Who are you?

DEATH: Death. You got a glass of water?

NAT: Death? What do you mean, Death?

DEATH: What is wrong with you? You see the black costume and the whitened face?

NAT: Yeah.

DEATH: Is it Halloween?

NAT: No.

DEATH: Then I'm Death. Now can I get a glass of water-or a Fresca?

NAT: If this is some joke-

DEATH: What kind of joke? You're fifty-seven? Nat Ackerman? One eighteen Pacific Street? Unless I blew it -- where's that call sheet? (He fumbles through pocket, finally producing a card with an address on it. It seems to check.)

NAT: What do you want with me?

DEATH: What do I want? What do you think I want?

NAT: You must be kidding. I'm in perfect health.

DEATH: (unimpressed) Uh-huh. (Looking around) This is a nice place. You do it yourself?

NAT: We had a decorator, but we worked with her. (back to the issue) I don't want to go yet.

DEATH: You don't want to go? Please don't start in. As it is, I'm nauseous from the climb.

NAT: What climb?

DEATH: I climbed up the drainpipe. I was trying to make a dramatic entrance. I see the big windows and you're awake reading. I figure it's worth a shot. I'll climb up and enter with a little-you know ... (Snaps fingers) Meanwhile, I get my heel caught on some vines, the drainpipe breaks, and I'm hanging by a thread. Then my cape begins to tear. Look, let's just go. It's been a rough night.

NAT: You broke my drainpipe?

DEATH: Broke. It didn't break. It's a little bent. Didn't you hear anything? I slammed into the ground.

NAT: I was reading. (grabs his newspaper) I'm not finished!

DEATH: Er-I don't know how to put this to you, pal . . .

NAT: Why didn't you just ring downstairs?

DEATH: I'm telling you, I could have, but how does it look? This way I get a little drama going. Something. Did you read Faust?

NAT: What?

DEATH: And what if you had company? You're sitting there with important people. I'm Death -- I should ring the bell and traipse right in the front? Where's your thinking?

NAT: Listen, Mister, it's very late.

DEATH: Yeah. Well, you want to go?

NAT: Go where?

DEATH: Death. It. The Thing. The Happy Hunting Grounds. (Looking at his own knee) Y'know, that's a pretty bad cut. My first job, I'm liable to get gangrene yet.

NAT: Now, wait a minute. I need time. I'm not ready to go.

DEATH: I'm sorry. I can't help you. I'd like to, but it's the moment.

NAT: How can it be the moment? I just merged with Modiste Originals.

DEATH: What's the difference, a couple of bucks more or less.

NAT: Sure, what do you care? You guys probably have all your expenses paid.

DEATH: You want to come along now?

NAT: (studying him) I'm sorry, but I cannot believe you're Death.

DEATH: Why? What'd you expect -- Rock Hudson?

NAT: No, it's not that.

DEATH: I'm sorry if I disappointed you.

NAT: Don't get upset. I don't know, I always thought you'd be . . . uh . . . taller.

DEATH: I'm five seven. It's average for my weight.

NAT: You look a little like me.

DEATH: Who should I look like? I'm your death.

NAT: Give me some time. Another day.

DEATH: I can't. What do you want me to say?

NAT: One more day. Twenty-four hours.

DEATH: What do you need it for? The radio said rain tomorrow.

NAT: Can't we work out something?

DEATH: Like what?

NAT: You play chess?

DEATH: No, I don't.

NAT: I once saw a picture of you playing chess.

DEATH: Couldn't be me, because I don't play chess. Gin rummy, maybe.

NAT: You play gin rummy?

DEATH: Do I play gin rummy? Is Paris a city?

NAT: You're good, huh?

DEATH: Very good.

NAT: I'll tell you what I'll do-

DEATH: Don't make any deals with me.

NAT: I'll play you gin rummy. If you win, I'll go immediately. If I win, give me some more time. A little bit -- one more day.

DEATH: Who's got time to play gin rummy?

NAT: Come on. If you're so good.

DEATH: Although I feel like a game . . .

NAT: Come on. Be a sport. I got the cards right here. Don't make a production.

DEATH: All right. We'll play a little. It'll relax me.

NAT: (getting cards, pad, and pencil) You won't regret this.

DEATH: Don't give me a sales talk. Get the cards and give me a Fresca and put out something. For God's sake, a stranger drops in, you don't have potato chips or pretzels.

NAT: There's M&M's downstairs in a dish.

DEATH: M&M's. What if the President came? He'd get M&M's, too?

NAT: You're not the President.

DEATH: Deal. (Nat deals, turns up a five.)

NAT: You want to play a tenth of a cent a point to make it interesting?

DEATH: It's not interesting enough for you?

NAT: I play better when money's at stake.

DEATH: Whatever you say, Newt.

NAT: Nat. Nat Ackerman. You don't know my name?

DEATH: Newt, Nat -- I got such a headache.

NAT: You want that five?

DEATH: No.

NAT: So pick.

DEATH: (surveying his hand as he picks) Jesus, I got nothing here.

NAT: What's it like?

DEATH: What's what like? (Throughout the following, they pick and discard)

NAT: Death.

DEATH: What should it be like? You lay there.

NAT: Is there anything after?

DEATH: Aha, you're saving twos.

NAT: I'm asking. Is there anything after?

DEATH: (absently) You'll see.

NAT: Oh, then I will actually see something?

DEATH: Well, maybe I shouldn't have put it that way. Throw.

NAT: To get an answer from you is a big deal.

DEATH: I'm playing cards.

NAT: All right, play, play.

DEATH: Meanwhile, I'm giving you one card after another.

NAT: Don't look through the discards.

DEATH: I'm not looking. I'm straightening them up. What was the knock card?

NAT: Four. You ready to knock already?

DEATH: Who said I'm ready to knock? All I asked was what was the knock card.

NAT: And all I asked was is there anything for me to look forward to.

DEATH: Play.

NAT: Can't you tell me anything? Where do we go?

DEATH: We? To tell you the truth, you fall in a crumpled heap on the floor.

NAT: Oh, I can't wait for that! Is it going to hurt?

DEATH: Be over in a second.

NAT: Terrific. (Sighs) I needed this. A man merges with Modiste Originals . . .

DEATH: How's four points?

NAT: You're knocking?

DEATH: Four points is good?

NAT: No, I got two.

DEATH: You're kidding.

NAT: No, you lose.

DEATH: Holy Christ, and I thought you were saving Sixes.

NAT: No. Your deal. Twenty points and two boxes. Shoot. (Death deals) I must fall on the floor, eh? I can't be standing over the sofa when it happens?

DEATH: No. Play.

NAT: Why not?

DEATH: Because you fall on the floor! Leave me alone. I'm trying to concentrate.

NAT: Why must it be on the floor? That's all I'm saying! Why can't the whole thing happen and I'll stand next to the sofa?

DEATH: I'll try my best. Now can we play?

NAT: That's all I'm saying. You remind me of Moe Lefkowitz. He's also stubborn.

DEATH: I remind him of Moe Lefkowitz. I'm one of the most terrifying figures you could possibly imagine, and him I remind of Moe Lefkowitz. What is he, a furrier?

NAT: You should be such a furrier. He's good for eighty thousand a year. He's got his own factory. Two points.

DEATH: What?

NAT: Two points. I'm knocking. What have you got?

DEATH: My hand is like a basketball score.

NAT: And it's spades.

DEATH: If you didn't talk so much. (They re-deal and play on.)

NAT: What'd you mean before when you said this was your first job?

DEATH: What does it sound like?

NAT: What are you telling me -- that nobody ever went before?

DEATH: Sure they went. But I didn't take them.

NAT: So who did?

DEATH: Others.

NAT: There's others?

DEATH: Sure. Each one has his own personal way of going.

NAT: I never knew that.

DEATH: Why should you know? Who are you?

NAT: What do you mean who am I? Why -- I'm nothing?

DEATH: Not nothing. You're a dress manufacturer. Where do you come to knowledge of the eternal mysteries?

NAT: What are you talking about? I make a beautiful dollar. I sent two kids through college. One is in advertising, the other's married. I got my own home. I drive a Chrysler. My wife has whatever she wants. Maids, mink coat, vacations. Right now she's at the Eden Roc. Fifty dollars a day because she wants to be near her sister. I'm supposed to join her next week, so what do you think I am -- some guy off the street?

DEATH: All right. Don't be so touchy.

NAT: Who's touchy?

DEATH: How would you like it if I got insulted quickly?

NAT: Did I insult you?

DEATH: You didn't say you were disappointed in me?

NAT: What do you expect? You want me to throw you a block party?

DEATH: I'm not talking about that. I mean me personally. I'm too short, I'm this, I'm that.

NAT: I said you looked like me. It's like a reflection.

DEATH: All right, deal, deal.

(They continue to play as music steals in and the lights dim until all is in total darkness. The lights slowly come up again, and now it is later and their game is over. Nat tallies.)

NAT: Sixty-eight . . . one-fifty .. . ... Well, you lose.

DEATH: (dejectedly looking through the deck) I knew I shouldn't have thrown that nine. Damn it.

NAT: So I'll see you tomorrow.

DEATH: What do you mean you'll see me tomorrow?

NAT: I won the extra day. Leave me alone.

DEATH: You were serious?

NAT: We made a deal.

DEATH: Yeah, but-

NAT: Don't "but" me. I won twenty-four hours. Come back tomorrow.

DEATH: I didn't know we were actually playing for time.

NAT: That's too bad about you. You should pay attention.

DEATH: Where am I going to go for twenty-four hours?

NAT: What's the difference? The main thing is I won an extra day.

DEATH: What do you want me to do-walk the streets?

NAT: Check into a hotel and go to a movie. Take a schvitz. Don't make a federal case.

DEATH: Add the score again.

NAT: Plus you owe me twenty-eight dollars.

DEATH: What?

NAT: That's right, Buster. Here it is -- read it.

DEATH: (going through pockets) I have a few singles-not twenty-eight dollars.

NAT: I'll take a check.

DEATH: From what account?

NAT: Look who I'm dealing with.

DEATH: Sue me. Where do I keep my checking account?

NAT: All right, gimme what you got and we'll call it square.

DEATH: Listen, I need that money.

NAT: Why should you need money?

DEATH: What are you talking about? You're going to the Beyond -- You know how far that is?

NAT: So?

DEATH: So where's gas? Where's tolls?

NAT: We're going by car!

DEATH: You'll find out. (Agitatedly) Look -- I'll be back tomorrow, and you'll give me a chance to win the money back. Otherwise I'm in definite trouble.

NAT: Anything you want. Double or nothing we'll play. I'm liable to win an extra week or a month. The way you play, maybe years.

DEATH: Meantime I'm stranded.

NAT: See you tomorrow.

DEATH: (being edged to the doorway) Where's a good hotel? What am I talking about hotel, I got no money. I'll go sit in Bickford's. (He picks up the newspaper)

NAT: Out. Out. That's my paper. (He takes it back)

DEATH: (exiting) I couldn't just take him and go. I had to get involved in rummy.

NAT: (calling after him) And be careful going downstairs. On one of the steps the rug is loose. (And, on cue, we hear a terrific crash.)
```

---

## IC-0993: Dog Sees God

- Title: Dog Sees God
- Author (byline): Bert V. Royal
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: March 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CB, BEETHOVEN, ACTOR 2, ACTOR 1, MATT, TEACHER, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1805
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bert V. Royal
ISBN: 978-0822221524
Publisher: Dramatists Play Service
Date (Month/Year): March 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Even the most devoted fans of the comic strip "Peanuts" must wish that Charlie Brown would just once change out of that yellow, jagged-striped shirt.

ACTOR 2: Or shave his string of hair, kick that darn football or do something -- anything -- different.

ACTOR 1: In this selection that wish comes true for not only Charlie Brown, but for others in the original comic strip as well.

ACTOR 2: They grow up and their transformation is definitely . . . different

ACTOR 1: Pigpen has grown up into a violent, homophobic jock – You’ll see him here as Matt.

ACTOR 2: Charlie Brown, or CB, as he's called, becomes a popular kid with a mean streak who is still questioning his place in the world.

ACTOR 1: And Beethoven (think Schroeder), the artistic pianist has been long abused by the popular kids and his father.

ACTOR 2: Dog Sees God by Bert V. Royal
```

### Performance text (classify this)

```text
Suggested Roles: Actor 1: CB and Matt

Actor 2: Beethoven, Voice over for pen pal letters and Teachers

(whaa – whaa questions)

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

CB, a handsome, however sullen, teenager. (Voice over by Actor 2 as he “writes”)

CB: (Pg 7-8) Dear Pen Pal. I know it's been a few years since I last wrote you. I hope you're still there. I'm not sure you ever were. I never got any letters back from you when I was a kid. It was pretty frustrating when I was young, but now I'm glad that you won't respond. Just listen. That's what I want. (beat) My dog died. I don’t know if you remember, but I had a beagle. I went out to feed him and he didn't come bounding out like usual. I looked in the doghouse. There was blood everywhere. The blood belonged to a little yellow bird that had always been around. My dog and the bird used to play together. . . Anyway, the bird had been mangled. Ripped apart. By my dog. My parents called a center and they came and took him away. Later that day, they put him to sleep. When my dog died, that was when the rain cloud came back and everything went to hell . . .

CB: (Pg 20-24) (to audience) I was passing by the music room when I heard a song. The song was simple. Much more simple than what he usually played. (beat) Lights up on Beethoven playing the piano. He has a black eye. CB enters unseen by Beethoven. He stands and listens to the music, as if hypnotized by it. He begins to cry silently, but then accidentally lets out a sob. Beethoven abruptly stops, spins around and sees him. CB pulls himself together.

BEETHOVEN: You're not supposed to be in here. I have permission to practice during lunch. But nobody else.

CB: You've gotten really good. I mean, you always were, but - Who wrote that? Beethoven?

BEETHOVEN: Chopin.

CB: Do you mind if I just listen for a little while? (Beethoven resumes; CB cries) God. This is really embarrassing. (pause) My dog died. He got rabies. They, um, had to put him under. (beginning to ramble) Have you ever had someone close to you die and you can't stop thinking about what's happened to them? It's like you're stuck in this morbid place and there's so much death that you feel like your head is going to explode and it makes you think that maybe you're dead, too. (Beethoven slams his fist down on the keys) What?

BEETHOVEN: Well, it's just that you haven't spoken to me in years. Except to call me a "faggot" or to dislocate my shoulder and all of a sudden I get a stream-of-consciousness monologue about your dead dog while I'm trying to spend the only moments of my day that don't truly SUCK. Forgive my bluntness. But I *don’t care* about you or your morbid curiosities or your dead dog, so why don't you just leave?

CB: We were just messing with you.

BEETHOVEN: I haven't had lunch in the cafeteria in two and a half years for fear of going home with some part of it smeared across my shirt! I haven't been in a bathroom on campus since the time my head got slammed into the wall. I believe you were there. And what really kills me is that everybody wonders why kids bring guns to school. Maybe you're not the bully, but you stand idly by and watch. In my eyes that makes you even worse. So - Please. Just. Go.

CB: Maybe if you didn't act so – Well. Gay.

BEETHOVEN: And how does one act gay? (silence) By playing the piano? Maybe I'll stop carrying around a pink purse. What?! What is it?!

CB: You're being hostile and I'm just trying to talk to you like a civilized -

BEETHOVEN: I don't want to talk to you!!! I just want to be left alone!

CB: See, this is why you don't have any friends. Don’t be so melodramatic!

BEETHOVEN: You’re crying about a dead dog and I’M being melodramatic?! (Beethoven shoves CB. CB doesn't fight back. Beethoven hits him and CB begins to laugh) What's so funny?

CB: I'm sorry. It's just that I was scared of you for, like, a second. (Beethoven joins in the laughter)

BEETHOVEN: I'm sorry.

CB: No, it's okay. I deserved it. (beat) Promise me you won't bring a gun to school.

BEETHOVEN: I don't know where to get one. (silence) You were one of my best friends. You all were. I just don't get it.

CB: It's no consolation, but - well, can I be honest? (beat) No one knew what to say to you after your dad got arrested . . . I'm sorry we weren't there for you. (extends his hand) Truce?

BEETHOVEN: Okay. Truce. (shakes CB’s hand for longer than expected. CB pulls his away)

CB: Are you. . . ?

BEETHOVEN: I don't know. I've never had sex, so it would be hard to say at this point.

CB: But what about. . .?

BEETHOVEN: My dad? I don't think that's considered sex. (silence)

CB: Do you remember how my dog used to howl whenever you played the piano? What do you think happens to pets when they die?

BEETHOVEN: They go to heaven. . . There has to be some reward for having to live through this.

CB: (looks depressed) But my dog killed a living thing. Wouldn't God be mad?

BEETHOVEN: He was sick, CB. He couldn't help it. They say a dog sees God in his master. A cat looks in the mirror.

CB: (chuckling) I hate cats.

TRANSITION

ACTOR 2: When asked to describe the melancholy of his original comic strip Peanuts, Charles Shultz said . . . it’s simple

ACTOR 1: “All the loves in the strip are unrequited; all the baseball games are lost; all the test scores are D-minuses; the Great Pumpkin never comes; and the football is always pulled away.”

ACTOR 2: Life is hard in elementary school, and it doesn’t get any easier in high school.

ACTOR 1: CB and Beethoven, both confused and looking for love, begin a relationship

ACTOR 2: But over the course of the next few weeks, the anxiety for Beethoven becomes pronounced. Beethoven at the piano. CB approaches with a paper sack and starts unpacking lunch on the piano.

CB: (Pg 41-43) I brought you lunch. (Beethoven stops playing and gives CB a look of despair and frustration) Hey, halfway through the day and I only got called a queer three times.

BEETHOVEN: That's because people are scared you'll beat them up.

CB: Don't worry. I've already started spreading the word that if they mess with my boyfriend, I'll be kicking some ass. (kisses the top of Beethoven's head)

BEETHOVEN: Your boyfriend? I don't want a boyfriend. . . This can't happen. CB, I really need to practice.

CB: You really need to eat.

BEETHOVEN: (losing it) CB! Just stop! Okay? This isn't what I want.

CB: What's the problem?

BEETHOVEN: THIS is the problem! I'm stressed out right now and I'm trying to calm my nerves by playing the piano . . . Look. The other night was great, but . . .You go back to being yourself. This is just too weird.

CB: (getting perturbed) Fine. I'll leave you alone. (grabs backpack and starts to exit; turns back)

BEETHOVEN: Just give me time. (CB exits) (to himself) Oh my God. (resumes playing with a smile as Matt enters)

MATT: Hey there, Liberace. (Beethoven stops playing and turns, trying to conceal his terror)

BEETHOVEN: Matt, you're not supposed to be in here.

MATT: Where's your boyfriend?

BEETHOVEN: He's not my boyfriend . . . Just leave me alone, okay? Please. I didn't do anything.

MATT: Play something. (Beethoven doesn't move. Matt bends Beethoven’s finger backwards, leading him to the keys; he begins to play) So, are you two, like, a couple now? Are you going to parade around the halls holding hands? Go to prom together? (beat) Can't you people just keep it hidden? Instead of throwing it in our faces? (Beethoven stops and looks at him; he realizes Matt's secret) CB is not like you. And if you so much as look at him again, I'll kill you. You got that, perv? (starts to exit)

BEETHOVEN: No.

MATT: What? (goes back to the piano) What did you say?

BEETHOVEN: I said no . . . Pigpen. (Matt grabs Beethoven in an act of violence; Beethoven screams) ***** SCENE *******

CB: (to audience) Frederic Chopin died of tuberculosis on October 17, 1849. He had two requests. He was terrified of being buried alive, so he asked that his heart be removed from his body. The second request was that Mozart's "Requiem" be sung at his funeral. (long beat) Beethoven didn't leave a note. So, I don't know if he had any last requests. (bell rings for class) ***** Classroom. CB does not want to be there *******

TEACHER: (Pg 44-45) (whaa – whaa question)

CB: Huh? (whaa – whaa question again) How does his death make me feel? No one even liked him. Who cares? He's dead! That's life. The world is full of people who have tough lives. But do you see them killing themselves? No. There are people out there who can't walk. Can't see. Do they give up? No. They keep going. Suicide is pathetic bullshit. It's weak. (Losing it) DID HE SAY GOODBYE TO ME?! I wish he was still here so I could twist his arm behind his back and shove his face in a toilet. (hits the wall and storms off) ***** SCENE *******

CB: (Pg 46) (writing to his pen pal – Actor 2 voices lines while Actor 1 “acts”) Sorry for unloading all of this. (Forcing a smile) I bet this is the longest letter you've ever gotten. Thanks for listening. Sincerely. No. Yours truly. No. Your pen pal. CB. TRANSITION

ACTOR 2: And weeks later, shockingly, CB’s silent pen pal replies CB stands alone, holding the letter; just staring at it. He opens it tentatively (Both actors share the lines of this letter, with their voices sometimes overlapping. Actor 2 should be “off-stage, so consider creative blocking for the final section) (NOTE: In the original script, which includes many more characters . . . multiple characters not included in this cutting are assigned voice-over lines from the letter while CB silently reads it – This cutting contains all the original lines, but they have been divided between the 2 actors of this DUO – if rules for your tournament do not allow this cutting modification, then only 1 actor (your choice) should present all lines – Suggested that Actor 2 voice overs all lines while Actor 1 “acts”) ACTOR 1 (CB): (Pg 47-49) Dear CB. How unexpected to get a letter from you after all these years.

ACTOR 2: I thought you had forgotten about me. It sounds like you're going through a pretty rough time and having to deal with situations that you feel like you can't handle - But if anyone is equipped to deal with these things, it's you.

TOGETHER: I promise that things get better.

ACTOR 2: I was talking to a girl the other day who told me of an incident that happened at her high school. There was a boy. Bullied. Tormented. To the point of opening fire on their cafeteria.

ACTOR 1 (CB): He was quiet and awkward. No one ever spoke to him unless it was to insult him. He took the lives of many people.

ACTOR 2: How differently things could have been through just one connection.

ACTOR 1 (CB): No matter how great or small.

ACTOR 2: She lives where I live now. A place where there is no violence. Everyone treats others with kindness, love and respect. Can you imagine such a place? Don't concern yourself with death. Immerse yourself in life.

TOGETHER: Enjoy every moment that you're allowed. But keep asking questions, my dear friend.

ACTOR 2: A boy recently came to live down the street from me. He's had a tough life, but things are better for him now. He plays the piano like your friend.

ACTOR 1 (CB): I often hear his music wafting from an open window, where a small yellow bird sits. Sometimes I cry when I hear it. But mostly I smile.

ACTOR 2: He found a dog who likes to sing along. He tells me of a person he knew; Someone who means more than anything to him. A person that reminds me of you.

TOGETHER: Maintain in your heart all that makes you who you are. You are a good man. (pause)

ACTOR 2: Your Pen Pal. CS. (CB drops the letter and cries for his dog, his friend and for himself) CLOSING

ACTOR 1: C.S. -- Could this be Charles Shultz? or a symbolic message from the “Creator” or God.

ACTOR 2: Pop culture hits like the Peanuts endure by being constantly recreated and experimented on by fervent fans.

ACTOR 1: RIP Charles Shultz, your characters and your legacy live on.
```

---

## IC-0994: Don’t Fear the Reaper

- Title: Don’t Fear the Reaper
- Author (byline): Eddie Zipperer
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: Sept 2008
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ANNOUNCER, DONNIE, STEVE, SATAN, GOD, DEATH, BILL, BIL, JEREMY, CONCEPTION, TV ANCHORMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 2138
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
ACTOR 1: Steve fell asleep with chips in his mouth.

ACTOR 2: What a horrible way to die.

ACTOR 1: It’s called sloth and it’s one of the deadly sins.

ACTOR 2: But when Death arrives to take his immortal soul, he finds that Steve has achieved a perfect balance upon the scales of good and evil.

ACTOR 1: Mediocrity to the highest degree!

ACTOR 2: So, going against protocol, Death gives Steve the opportunity to decide for himself if he will be sent to heaven or hell by playing

ACTOR 1: THE FATING GAME.

TOGETHER: Don’t Fear the Reaper by Eddie Zipperer
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actor 1: Announcer, Steve, God, Jeremy, Conception

Actor 2: Donnie, Satan, Death/Bill, TV Anchorman

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

DEATH: (Death’s pager goes off loudly – He looks at it and sees that it is GOD who is summoning him. Flustered) For a while, but don’t worry, I’ll be back soon. ****** Scene Break ******** Setting: God is in an office, working. Death enters in his classical form, black cloak and scythe.

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

BIL: Death can’t be biased, but –

GOD: And why must Death remain unbiased?

BILL: Because otherwise people end up in the wrong place.

GOD: And wouldn’t you agree that people ending up in the wrong place is a monumental error.

BILL: Yes.

GOD: Or do I need to remind you of the three days after you sent Jesus to hell?

BIL: He told me he was responsible for all the sin in the world! What was I supposed to think.

GOD: That’s the point I’m getting at. You are not supposed to be thinking at all. You go by the book. I don’t want to go into the bureaucratic nightmare of getting Jesus back. Let’s just say I’m not interested in dealing with that problem again.

BILL: I’m sorry. It just started to become painful for me. All this sorting people into Heaven souls or Hell souls. People are scared enough when they’ve just died. It was easy when I first got started, but as I got older and sorted more souls, I started to realize that Heaven and Hell is a black and white idea. There’s no middle ground.

Someone who’s just a little evil goes to the same place as Hitler? That doesn’t make sense. I’m sorry. It got difficult and stressful for me because it’s kind of dumb, but I’ll go by the book from now on.

GOD: I’m sorry, but unfortunately, I have no choice but to replace you. You’re fired, Bill.

BIL: What! For a little compassion? For trying to do the right thing? I just want people to have a good death. A painless transition from Earth to afterlife

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

JEREMY: He took the scythe. That can’t be good. (God gives him a scathing look) I’ll go find him. (Jeremy exits)

****** Scene Break ********

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

BILL: (Scared) Jeremy, can you tell me what’s – what’s going to happen to me now?

JEREMY: I can tell you what’s going to happen to you if you call me Jeremy one more time.

BILL: (Singing and dancing – Audio for this song, Don’t Fear the Reaper can be found at the
link provided at the end of this selection)
Come on baby, don't fear the reaper
Baby take my hand, don't fear the reaper
We'll be able to fly, don't fear the reaper
Baby I'm your man
La, la, la, la, la / La, la, la, la, la
```

---

## IC-0995: The Drowned Man

- Title: The Drowned Man
- Author (byline): Neil Simon
- Work: The Good Doctor
- Publisher: Samuel French, Inc.
- Publication date as stated: 1974
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TRAMP, WRITER
- Teaser before the introduction: Yes
- Spoken words (computed): 1212
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Simon
Book: The Good Doctor
ISBN: 0573609713
Publisher: Samuel French, Inc.
Date(Month/Year): 1974
AWARD RECORDS
2002 National Qualifier
```

### Introduction (context only: never use it for content warnings)

```text
Actor 1: "What would you do for money?" Some people would eat a spider as big as the palms of their hands. Some people would go weeks on end without bathing and brushing their teeth while they rough it on some remote island. Some people would marry a perfect stranger. All of these things are done today on national television to meet the public’s need for entertainment.

Actor 2: Although in 1974 reality television hadn’t evolved . . . Neil Simon offers his prophetic vision of what public entertainment was to become: “The Drowned Man” from The Good Doctor by Neil Simon.
```

### Performance text (classify this)

```text
TRAMP: Psst! You, sir. Can I have a word with you, sir?

WRITER: Who's there?... I can't see you in the dark.

TRAMP: 'Evening, sir... I was wondering, sir, if you might be in the mood for a little, er, "entertainment" this evening?

WRITER: "Entertainment"? I'm sure I don't know what you're talking about.

TRAMP: Sure you do, sir. Entertainment... Amusement, so to speak. A little "diversion," if you know what I mean.

TRAMP: You've never witnessed anything like this before, that I promise you. This is a once-in-a-lifetime offer... Not even a little bit curious?

WRITER: Curiosity is the nature of my profession. But I try to keep it morally elevated... Excuse me.

TRAMP: Perhaps you're right, sir. On second thought, this might be too much for a gentleman of your "sensitivities."

WRITER: Wait!

TRAMP: Got you with that last one, didn't I?

WRITER: I'm just asking, mind you, but, er... just exactly what is this "entertainment" you speak of?

TRAMP: Well, sir, how would you like to see -- a drowned man?

WRITER: I beg your pardon?

TRAMP: A drowned man! A man with his lungs filled up with salt water and stone dead from drowning. How much would you pay to see that?

WRITER: Pay? Pay to see a drowned man? Are you insane? I wouldn't look at a drowned man if they paid me. Why would I want to see a drowned man? What's the point in looking at a man who drowned? You're mad! Get out of here!

TRAMP: Three rubles, sir. That's all it'll cost you. Three rubles to see him first, before he's in the water, then in the agonizing act of drowning and then the grand finale, the man already drowned, rest his soul.

WRITER: What are you saying? That the man isn't drowned yet? That he's still alive and well?

TRAMP: Not only alive and well, but dry as bone and standing before you. I'm the drowned man, sir.

WRITER: You? You're going to drown yourself for three rubles? You expect to charge me for your own suicide?... I must get away from this lunatic.

TRAMP: No, no, no, you've got it all wrong, sir. I don't actually drown. I impersonate a drowned man. I jump into the icy cold water, splash around a bit, flail my arms, yell for help a few times, go under -- bubble, bubble, bubble -- and then come up floating head down, all puffy like. It sends a chill up your spine... Three rubles for individual performances, special rates for groups. Show starts in two minutes.

WRITER: I can't believe I'm actually discussing the price of admission to a drowning.

TRAMP: You miss the whole point, sir. This is not some sort of cheap thrill. It's a rich tableau filled with social implications. A drama, not tragic, but ironical, in view of its comic features.

WRITER: Comic? What's comic about it?

TRAMP: I blow up my cheeks and bulge my eyes out. Yell for help in a high squeaky voice. Sounds like a pig squealing. I'm the only one on the waterfront who can do it.

WRITER: Do you actually expect me to pay to hear an underwater pig squealer?

TRAMP: I've just had a very successful season, sir. Sold out in August. What do you say, sir? Would you like me to book you now for the dinner show?

WRITER: What do mean, dinner show?

TRAMP: I jump in, flail around and throw you a nice fish. I think the halibuts are running now, sir.

WRITER: Why do I stand here listening to this?

TRAMP: I wish you'd make up your mind soon, sir. In five minutes that restaurant throws its garbage in the water. Then it's messy. I have my pride.

WRITER: To hell with your pride. It doesn't prevent you from making a living imitating a deceased swimmer.

TRAMP: You sure know how to strike at a man's vulnerable points. That was cruel, sir.

WRITER: I'm sorry. I didn't mean to be cruel.

TRAMP: You completely overlook the finer points to my profession. Look here, did you ever see a coal miner at the end of a day? Filth and grime all over his body. Soot up his nostrils and in his ears, black grit in his teeth. Disgusting... Or a barber who goes home at night with the cuttings of other people's hair sticking to his hands. It gets in his bread, in his soup, it's nauseating... Do you know where a surgeon puts his fingers--

WRITER: Oh, please.

TRAMP: --or a farmer his feet? Every man who works eventually touches something filthy. On the other hand, I deal with water. Water is wet, it's clean, it's purifying. I don't have to take a bath when I come home at night. I've done it. Can you day the same, sir?

WRITER: Do you think I'm going to discuss my toilet habits with you? My God, you're infuriating. There must be a carriage around here. Cabbie! Cabbie!

TRAMP: You'll regret it. You'll be back one night, bored to death, dying to see a good drowning and I'll be gone. This is my last week here. I close on Sunday... Next week I'm in Yalta. Just for you I am reducing my price to an all time low. Eighty kopecks.

WRITER: Eighty?! Eighty, you thief! You conniving, wretched, deceiving little thief, I won't pay you more than sixty!

TRAMP: Sixty? Sixty kopeks for a drowning? But where's my profit? My towels cost me forty kopeks. And another forty for the fella who fishes me out. I'd be losing money on it. What's the point? I might as well stay under.

WRITER: You can't cheat me, sir. Sixty kopecks for the drowning, take it or leave it.

TRAMP: You're a hard man, sir. A hard man... Sixty kopeks it is. I pray to God my son doesn't want to be a drowner.

WRITER: -thirty-forty-fifty-sixty. There's your money. Now where shall I stand?

TRAMP: Right on the edge of the dock, sir. Right up close, that's where you'll see all the action.

WRITER: It's a big dark down there. You're sure I'll be able to see well?

TRAMP: That's what makes it so eerie. The eerier, the more entertaining. All the action's in the last ten seconds anyway... Well, here I go. Oh, I almost forgot. When I come up for the third time, yell at the top of your lungs, Popnichefsky! Popnichefsky!

WRITER: Who's Popnichefsky?

TRAMP: He's the fellow who jumps in after me. I can't swim, sir.

WRITER: You can't swim! Are you trying to tell me you're going to drown without knowing how to swim?

TRAMP: That's what makes it so exciting. Popnichefsky always waits till the very last second before jumping in and pulling me out. He's in that restaurant, sir, having a drink. Popnichefsky. Don't forget the name, sir... Well, I hope you enjoy the show. If you like it, tell your friends... In the soup, as we say. (He jumps in, yells for help) Help! Help, I'm drowning! I can't swim, help!

WRITER: Over here. A little toward me... I can't see you too well there...

TRAMP: Oh, God! Help! Help, somebody, I'm drowning!

WRITER: Good, very good. Yes, well, that's enough of that. I don't want to see that part any more. I don't have all night... Can you drown now?

TRAMP: Aggglllll....

WRITER: Do you hear me? I would like to have you drown now... Where the devil is he? Ahh, there you are... That's the third time, isn't it? (About to call for Popnichefsky) Good heavens, what was that fellow's name?
```

---

## IC-0996: Faith

- Title: Faith
- Author (byline): Eric Lane
- Work: Take Ten II: More Ten-Minute Plays, Pg 113
- Publisher: Vintage Books
- Publication date as stated: Nov 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MICHAEL, FATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 481
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eric Lane
Book: Take Ten II: More Ten-Minute Plays, Pg 113
ISBN: 978-1400032174
Publisher: Vintage Books
Date (Month/Year): Nov 2003
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: When a priest sexually abuses a child, the effects can be devastating.

ACTOR 2: The most trusted person imaginable suddenly does something that feels terribly wrong. It's a shattering experience.

ACTOR 1: In this selection, Michael (now a grown man) summons the courage to confront his abuser.

ACTOR 2: This performance is dedicated to the multitude of children betrayed by "pillars of the church."

TOGETHER: Faith by Eric Lane
```

### Performance text (classify this)

```text
(A confessional, simply represented by two chairs. FATHER, a priest in his forties to sixties, listens to MICHAEL 's confession. MICHAEL is in his twenties to thirties. Average looking.)

MICHAEL: . . . Bless me father for I have sinned.

FATHER: How long has it been since your last confession?

MICHAEL: Many years.

FATHER: Tell me your sins, my child.

MICHAEL: I have killed someone. (A pause.)

FATHER: Go on.

MICHAEL: Over and over. In my mind. Killed them for what they have done. And I'm scared.

FATHER: Scared of what?

MICHAEL: What will happen.

FATHER: What will happen?

MICHAEL: When it's no longer in my mind but me, actually not thinking but when it's time- Trying to believe, to find a reason not to-But less and less and wondering-

FATHER: Wondering what?

MICHAEL: Why?

FATHER: Wondering why what?

MICHAEL: How someone could have done this -- could have taken so much, when I trusted, believed . . . Why did I believe?

MICHAEL: I trusted, believed . . . Why did I believe?

FATHER: You were right to have faith.

MICHAEL: Not then. Not in him. He stole from me. Took things-

FATHER: Things.

MICHAEL: Not things. But important-Irreplaceable. Not things.

FATHER: Something closer to you.

MICHAEL: My youth. My joy. My innocence. He took my innocence.

FATHER: He hurt you.

MICHAEL: My soul. He took my soul.

FATHER: No one can take your soul. Only the Lord has that divine power.

MICHAEL: Took it. Pretending he knew things. Secrets. I didn't know.

FATHER: Your soul is still yours. No one can-

MICHAEL: Took it. When it wasn't his to take. To hold. Close. Me not knowing, thinking I should believe. That this is faith. That this is what God wants from me.

FATHER: You must forget.

MICHAEL: How can I forget?

FATHER: You must forgive.

MICHAEL: Forgive?

FATHER: You must.

MICHAEL: No. No forgiveness. Not for this. Not him.

FATHER: The Lord forgives our sins.

MICHAEL: I'm not the Lord.

FATHER: Washes them away.

MICHAEL: Too easy.

FATHER: Offers salvation.

MICHAEL: Only words.

FATHER: And hope.

MICHAEL: No meaning.

FATHER: To those who pray.

MICHAEL: I'm out of prayers.

FATHER: Prayers are answered.

MICHAEL: I can't.

FATHER: Redemption.

MICHAEL: No.

FATHER: Salvation.

MICHAEL: Can't.

FATHER: Hope.

MICHAEL: None.

FATHER: Faith.

MICHAEL: Gone.

FATHER: Joy.

MICHAEL: I can't.

FATHER: Love.

MICHAEL: I can't forgive you. (A beat.) I can't forgive you.

FATHER: Tell me your name.

MICHAEL: You don't get to ask. You don't get to do anything. You listen. And you pray. For what you've done to me.

FATHER: Who-

MICHAEL: Shut up. (A beat.) You don't even know who I am. Were there so many? You asshole. How many Hail Marys is it going to take to wipe away your sins? Now it's your turn. I want to hear it. Or I tell. Everyone. (Silence.) Now.

FATHER: What, my son?

MICHAEL: I am not your son. I never was your son. I want to hear your confession.

FATHER: I can't.

MICHAEL: Trust me.

FATHER: Only him.

MICHAEL: Where's your faith?

FATHER: My faith is in Jesus.

MICHAEL: Don't even try it.

FATHER: In the Lord Jesus Christ.

MICHAEL: Jesus Christ-

FATHER: In his divine mercy.

MICHAEL: Shut . . . up!

FATHER: I ask for his forgiveness.

MICHAEL: What about mine?

FATHER: Forgive me if I have sinned.

MICHAEL: "If." What kinda bullshit is that?

FATHER: If I have not seen-

MICHAEL: F*** you.

FATHER: Not followed-

MICHAEL: How could I have followed?

FATHER: For what I am about

MICHAEL: What are you about?

FATHER: To do.

MICHAEL: I was five years old. Do you remember? I was five years old.
```

---

## IC-0997: Fake Mustache

- Title: Fake Mustache
- Author (byline): Tom Angleberger
- Work: Not specified
- Publisher: Amulet Books
- Publication date as stated: July 2013
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, LENNY, CASPER, RED, SVEN, REPORTER, RECORDED VOICE, DIRECTOR DROPBAG, MAN, LADY, CROWD, GOVERNOR, REPORTER 2, STRANGE MAN, DR. HEIDELBERG
- Teaser before the introduction: Yes
- Spoken words (computed): 1692
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
ACTOR 1: And that’s when things started to turn out bad in a huge, earthshaking, TV-news-special-report kind of way.

ACTOR 2: But don’t worry . . . a few days later, our hero -- mild-mannered 7th grader Lenny Flem saved the world!

TOGETHER: Fake Mustache by Tom Angleberger
```

### Performance text (classify this)

```text
Suggested Roles:

ACTOR 1: Lenny, Red, Sven, Lady, Director Dropbag, Man, Crowd, Governor, Reporter 2, Strange Man

ACTOR 2: Casper, Reporter, President, Recorded Voice, Lady, Dr. Heidelberg’s echoing voice

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

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

REPORTER: (Pg 66) Heidelberg CEO Fako Mustacho is on his way to address the governor and state lawmakers about the Lenny crisis. *****

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

DR. HEIDELBERG: (echoing voice from the past) (Pg 103-104) He was a professional assassin, famous in the European underworld for his record of 300 kills and his perfect mustache. He was betrayed by a woman and arrested. When he arrived at prison, they shaved his mustache. [And now] the Heidelberg Handlebar #7 is too powerful, especially if it falls into the wrong hands. *****

LENNY: (Pg 186) Here’s what happened . . . I have a glimpse of Fako standing on the stage with his arms raised. (Casper and Lenny pantomimes the events while Lenny narrates) The French guy is squeezing the trigger . . . (Pg 188-189) and I am in motion . . . I land on the stage, grab the mustache, put it between my teeth and rip it in two. The mustache is dead! (Pg 191) And the platoon of Secret Service agents that rushed the stage found only two local Hairsprinkle schoolkids. No one saw what happened to Fako . . . and no one ever saw him again. (Pg 2) I saved the world and it all started with me and my friend Casper going to Sven’s Fair Price Store in downtown Hairsprinkle. (stage whisper) Don’t ever buy a fake mustache at Sven’s!
```

---

## IC-0998: Forgive Me, Leonard Peacock

- Title: Forgive Me, Leonard Peacock
- Author (byline): Matthew Quick
- Work: Not specified
- Publisher: Little Brown Books for Young Readers
- Publication date as stated: Aug 2013
- Event as filed: Duo Interpretation
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
ACTOR 2: Today is Leonard Peacock’s 18th birthday. He is a loner, an outcast, a misfit and maybe one day he’ll believe that being different is okay, important even. But not today.

ACTOR 1: Today he plans to commit suicide. Unless one caring teacher can convince him that the daily battle of not letting the world destroy you is worth the work.

TOGETHER: Forgive Me, Leonard Peacock by Matthew Quick
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

## IC-0999: A Funny Thing Happened on the Way to Fifth Period

- Title: A Funny Thing Happened on the Way to Fifth Period
- Author (byline): Jason Pizzarello
- Work: Random Acts of Comedy, Pgs 141-160
- Publisher: Playscripts, Inc.
- Publication date as stated: April 2011
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SUGGESTED ROLES, ACTOR 1, ACTOR 2, TOMMY, BURP, BUGS, STEPHANIE, STEVE, CHAD, VERONICA, CORA, OFF STAGE VOICE
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
AUTHOR NOTES: Feel free to change the reference to “high school” to “middle school” and
the “prom” to the “dance” or “school dance.” Any casting decisions that require characters to
change gender are fine.
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: School hallways are delicate ecosystems filled with bullies, nerds, jocks and (sings) theatre kids

ACTOR 2: So when Tommy, mild-mannered techie and professional problem-solver, gets pushed around by Burp and his not-so-bright protégé, Bugs . . .

ACTOR 1: He does what any reasonable teenager would do – comes up with a solution!

ACTOR 2: This selection is a fast-paced hallway comedy about survival, social hierarchy, and the power of lying with confidence.

ACTOR 1: Because all teen-agers know: if you can’t be popular . . .

ACTOR 2: Be convincing.

TOGETHER: A Funny Thing Happened on the Way to Fifth Period by Jason Pizzarello
```

### Performance text (classify this)

```text
SUGGESTED ROLES:

ACTOR 1: Tommy, bookworm;

ACTOR 2: Burp, head bully; Bugs, aspiring bully; Steve, friendly jock; Cora, Steve’s girlfriend; Veronica, Steve’s sister and a nerd with anger issues; Stephanie, lead actress; Chad, lead actor and Stephanie’s boyfriend.

***** Before School**** At the lockers as TOMMY reorganizes his trapper keeper, a large bull of a kid, BURP, comes up behind him and politely taps him on the shoulder. TOMMY turns around and the bull lets a burp rip so loud and foul, you can almost smell yesterday's lunch. But this isn't the first time, and TOMMY handles it with grace. BURP smiles.)

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

TOMMY: Make Veronica Jettlebaum your charity. Take her to the prom. (bell rings)

CHAD .... Okay, I'll do it. I'm sure Stephanie will understand. It's for our craft. (TOMMY and CHAD shake and head separate ways) ***** After Third Period****

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

## IC-1000: Gangster Apparel

- Title: Gangster Apparel
- Author (byline): Richard Vetere
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: Sept 1996
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: LOUIE, JOEY
- Teaser before the introduction: Yes
- Spoken words (computed): 1289
- Already set (do not supply): none

### Source block (context only)

```text
Author: Richard Vetere
ISBN: 978-0871297334
Publisher: Dramatic Publishing
Date (Month/Year): Sept 1996
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: (slick, confident) In our business, respect is everything.

ACTOR 2: (matter-of-fact) Respect. Loyalty. Tradition.

ACTOR 1: (small beat; smooths an imaginary lapel) These are the kind of guys who believe power starts in the mirror.

ACTOR 2: Because if you don’t look like somebody . . .

ACTOR 1: (judging glance) You’re dressed like a nobody.

TOGETHER: (Both freeze, subtly adjust imaginary suits at the same time) Gangster Apparel by Richard Vetere
```

### Performance text (classify this)

```text
Characters: Louie (30s) a well-dressed hit-man, and Joey (20s-30s) his less natty partner.

Scene: A dingy motel room in Queens. As they prepare for a job, Louis does his best to convince Joey that clothes make the man.

LOUIE: (ironing pants) Hey, where the hell you been? Another 5 minutes and I was going to call your mother!

JOEY: I'm sorry. I couldn't find the place. It's in the middle of nowhere.

LOUIE: I know. The boss picked it. He wants us to be discreet.

JOEY: We gotta talk.

LOUIE: About what?

JOEY: I don't know. . . I want to go to the beach. I want to see girls in bathing suits.

LOUIE: The last time I was on a beach I was 5 years old and I was burying some snot-nosed punk in seaweed 'cause he broke my sunglasses. I hate sand, I hate rocks in my toes, and I hate that smell that comes up from Jersey. And no matter what beach you are on, you are going to get hit with that smell that comes up from Jersey! Plus, you walk on a beach and you step on dead things. (steps to the bed where an expensive suit lies spread across it. Louie picks up the pants and hands them gently to Joey) Feel. (Joey touches the pants roughly) Make nice! (Joey touches the pants softly) Not any tailor. Guido on the corner near the deli. He makes the Boss's suits.

JOEY: Wow. . .

LOUIE: Georgio Armani.

JOEY: But the money it costs?

LOUIE: We are talking about clothes here. Who cares about the money? You think the Boss cares about the money?

JOEY: But he's got money.

LOUIE: He didn't always have it. He was a guy just like you and me, Joey, workin' his a** off tryin' to make something of himself.

LOUIE: Tonight, we have things to do. (Joey carefully carries the shirt to Louie who puts it on with the same dramatic flair he did the pants as Joey watches every movement) The tie. On the bed. It took me a half an hour to pick the tie to match the shirt. (Joey brings Louie the tie) You see, they compliment each other. Silk. All I could afford was one but that doesn't matter. Watch what a tie does. Check it out. . . (slowly puts on the tie and when the knot is complete, stands in the middle of the room like a prima ballerina waiting for applause) Ba da bing! See?

JOEY: Wow. . .

LOUIE: The shoes. (Joey runs to get them; brings them to Louie)

LOUIE: Be careful! No creases! (takes the shoes and slowly puts them on just as he did the other clothes, enjoying the act itself) Bally. I'd have 22 pair if I could. I will someday. (pause) Go ahead. . . touch them. (Joey gets on his hands and knees and touches the shoes) I mean, Joey, they shine so nice they cry out to be kissed! Really kissed!

JOEY: They do?

LOUIE: I noticed that the other day with the Boss. He was walking out of the club, right? And I was sittin' out in the car and I watched him get into the limo and saw how his shoes were shining! I mean, I was across the street and saw them shine! (pause) Comb. . . (Joey hands it to Louie. Louie combs his slicked back hair) Fifty bucks for the haircut. I am a man on the move!

JOEY: Nice. Real nice.

LOUIE: Now, get over here. Look in the mirror. What are you thinking when you look? Huh?

JOEY: I don't look good.

LOUIE: You got it, pal. I have been trying to tell you. . . but you don't listen. (pause) Just two hours in this dump and I already got dirt on my cuffs! Get me my gun. (Joey goes to a small bag on the chair in the corner and brings it to Louie) Go ahead. . . take it out. (Joey takes out a brand new .38 pistol and places it on the bed) Let's see your gun. Come on . . . (Joey slowly takes out a worn-out .38 pistol from his belt) What is that? What is that?

JOEY: My gun.

LOUIE: Look at it! Look!

JOEY: Come on, Louie. . . it works.

LOUIE: It works? So what, it works! How can you be seen with that? How?

JOEY: But nobody sees it.

LOUIE: Nobody sees it! I'm seeing it now! The cops who might bust you some day will see it! Come on, what's wrong with you?

JOEY: I don't know. I didn't think about it.

LOUIE: But these are the kinds of things you gotta think about! Come on, Joey. . . we started out in the same place. Running numbers back and forth to Brooklyn. . . but now who gets the good jobs, huh? Who gets the big money? Who gets the important work? Huh?

JOEY: You.

LOUIE: And 'why'?

JOEY: You are smarter.

LOUIE: And what else?

JOEY: . . . You . . . dress better?

LOUIE: I always dressed better. Even when all I could afford was a Vidal Sasson jumpsuit. . . I wore it! Every nickel in my pocket went for a pinky ring! And not just any pinky ring -- diamond! If I had 5 dollars in my pocket it went for a hair cut. Forget food! Maybe I was hungry but that's not important! I looked great! The bottom of my shoes had holes in them but they were shiny on top! Do you understand me, Joey? You tell me who you want to be. You want to be a bum or do you want to be somebody? What is that on your feet?

JOEY: Sneakers.

LOUIE: Sneakers? Huh? Who wears sneakers? You ever see the Pope wearing sneakers? Huh? You know who wears sneakers? People who have no respect for themselves, that's who wears sneakers! And what kind of pants are those?

JOEY: These are jeans, Louie.

LOUIE: Jeans? Who wears jeans? You ever see Sinatra in jeans? Okay, you want to go casual go slacks. A nice pair of black, grey slacks -- pleated, pressed, neat. A nice button-down shirt. . . matching socks and a nice belt. The whole nine yards. The trick to casual is to look like you feel comfortable. And that jacket? A low life off the street wears sneakers, jeans, and a leather jacket with a hole in the elbow! Nobody important dresses like some kind of low life even in his own house! At home? Try a robe with a silk lining . . . good slippers! And PJ's. Silk. Always silk. The cops bust in on you and see you dressed in a nice robe with silk lining, a silk pair of PJ's and good slippers and they will treat you like somebody! You understand me, Joey? (walks over to a suit hanging on the closet doorknob and tosses it on the bed) There. That is for you.

JOEY: Huh?

LOUIE: Go ahead, try it on. (Joey slowly approaches the suit in awe) Yo! Joey, you don't examine it; you wear it! It's a suit. Had it made for you. Special. Joey, listen to me. . . tonight I change your life. You got that? Now, put it on . . . hurry. (Joey undresses. Louie looks at his gun, Joey's gun, and shakes his head 'no'. Standing in his boxer shorts Louie hands him the pants, the socks, the shirt and tie) Now go over it all with me.

JOEY: (dressing) I park the car on Bleecker.

LOUIE: Right. Bleecker faces east. . . You sit in the car. Good.

JOEY: Then at 9:15 you come walking down Bleecker toward my car.

LOUIE: Good. Then what?

JOEY: He comes out of the restaurant at 9:15. If he's got one bodyguard I blink the lights once. If he's got two bodyguards I blink the lights twice.

LOUIE: Twice for two. (takes his brand new pistol and puts it in his belt) I will then walk up behind him like this... Ba ba bing! (holds his pistol in one hand as if he is aiming at the back of someone's head. Acting it out) And pop him twice in the back of the head. Then when the first bodyguard turns around I go bam twice right through the heart! Now, if the other bodyguard is there ready to pounce on me, what happens?

JOEY: (acting it out) I am right there with you, Louie. I put two slugs into him. Bam! Bam!

LOUIE: (watching Joey) Good. Very good. Then what?

JOEY: Back to the car we go. Nonchalant-like. Then we drive right on Broadway and left on Delancy. Then over the bridge and back to Queens. Safe and sound.

LOUIE: (Joey, now dressed, does not seem comfortable in the expensive clothes. Louie looks him over) You got to look comfortable in them. You just don't wear clothes, you become the clothes. It's a mental attitude. You are a somebody so walk like a somebody. You know? Look, show me how you are gonna walk up to this bodyguard. Show me. Go ahead. (Joey bops instead of walks across the room) No! No! You walk like that and the whole street will know you are a hood who's gonna pop some big shot!

JOEY: Then how should I walk? (Louie walks gracefully and slowly takes out his gun)

LOUIE: Like this. . . see? I am a man who enjoys walking. . . see? Like that. Look good doin' it. Come on, pal, don't you watch TV?

JOEY: (looks in the mirror) We look good. Louie. We look good!

LOUIE: (joins Joey in the mirror) Movie stars, or what?

JOEY: When you, Louie 'pop' a guy, what are you thinking?

LOUIE: I am thinking how fabulous I look! What else would I be thinking? It's not what is inside your head. . . It's how you look that matters! And one day when we are famous, the papers will say "Louie Falco and Joey Pugg are the two best dressed hoods in town." Let's do it.
```
