# Classification request: batch 38 of 63 (40 records, IC-1481 to IC-1520)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-038-reply.json`.

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

## IC-1481: . Michael Jackson Made Me Do It

- Title: . Michael Jackson Made Me Do It
- Author (byline): Gregg Moeller
- Work: . Michael Jackson Made Me Do It
- Publisher: SpeechGeek
- Publication date as stated: 2016
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: DELBERT
- Teaser before the introduction: No
- Spoken words (computed): 1883
- Already set (do not supply): none

### Source block (context only)

```text
.
Michael Jackson Made Me Do It by Gregg Moeller
ISBN: 978-1-61387-107-2
Copyright 2016 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2016, is identical to the printed published
version of this same publication dated 2016. This statement along with the entire printed PDF of
this publication must be presented at any National Speech and Debate Association District or
National event for the script to comply with NSDA rules per the request of the Executive
Director.
This and other selections of quality performance literature for competitive oral interpretation
are published by SpeechGeek.
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
.

LURLEEN. Mavis…MAVIS! I got a question for ya.
MAVIS. Lurleen. It is 5 AM. Questions are illegal from 3-6.
LURLEEN. Mavis—when do you know you or some significant udder is
possessed by…SATAN?
MAVIS. Significant udder? You got a cow with pentagram carved
on it?
LURLEEN. No, no no…other—other!
MAVIS. Other what?
LURLEEN. Seeg-niff-ihh-CANT other!

(Pause)

MAVIS. This train of thought derailed way too close to the station, Lurleen. LURLEEN. Satan! SAY-TAN! MAVIS. What about him? LURLEEN. The Beast! The Demon! Beelzebub! The Deceiver! The Father of Lies! MAVIS. You know you are also describing my ex-husband Jo-Jo. Get to the point, Lurleen! LURLEEN. He has struck us, Mavis. Struck us deep and true! MAVIS. Struck us? Is the carbon monoxide filter on your gas generator backed up again? LURLEEN. In his Satanic glory, Lucifer has struck down one of our own. Struck him down like a jogging nun at a Hell’s Angels rally. MAVIS. Nun at a…Lurleen—get to the POINT! LURLEEN. It is my brother Delbert. Delbert is under the scourge of the Serpent of Old! MAVIS. Delbert? He ain’t possessed…he’s in detox. And that ain’t Satan—that’s Old Turkey. LURLEEN. He was released today and he arrived on my doorsteps bridegroom of Beelzebub. MAVIS. He’s been married four times. And to be blunt, Beelzebub is probably a step up from the previous four.

LURLEEN. Shush. DELBERT! Get out here and show you’s possessed like I says you were! MAVIS. Oh, for the love of…

(DELBERT enters with a wide eyed, glazed look on his face)

.

MAVIS. Delbert, you look like you’ve been ridden all day and put
up wet.
DELBERT. She Told Me Her Name Was Billie Jean,
As She Caused A Scene
Then Every Head Turned
With Eyes That Dreamed
Of Being The One
Who Will Dance
On The Floor
In The Round
She Says I Am The One,
But The Kid Is Not My Son
LURLEEN. You see? SATAN!
DELBERT. People Always Told Me Be Careful Of What You Do
And Don't Go Around Breaking Young Girls' Hearts
And Mother Always Told Me Be Careful Of Who You Love
And Be Careful Of What You Do 'Cause The Lie Becomes
The Truth
MAVIS. That ain’t Satan. That’s Michael Jackson.
LURLEEN. Close enough, Mavis. Close enough.
DELBERT. Billie Jean Is Not My Lover
She's Just A Girl Who Claims That I Am The One
LURLEEN. Lord help us. The Rapture is upon us!
DELBERT. But The Kid Is Not My Son
LURLEEN. It’s the end of the world as we know it—and I don’t feel
fine, Mavis!
MAVIS. Lurleen, I’m pretty certain that in the Book of Revelation
Michael Jackson is remarkably absent. Nickelback?
Well…
LURLEEN. It is the end of the world. The EE-cops-a liss!
MAVIS. The whut?
LURLEEN. ECOPALYSS! You know, the Four Freshman!
MAVIS. You mean, uh-pock-a-lips. And that’s the four Horsemen.
LURLEEN. I don’t give a rat’s bladder if they’re riding ten speed
bikes—Delbert is a Soldier of Doom, and the Devil’s
using him like Jeff Dunham!
MAVIS. I see that he got divorced.
LURLEEN. Really? He seems like such a nice guy.
MAVIS. I just love Achmed. “Shut up! I KEEL YOU!”
LURLEEN. I like that pickle guy. The Mexican.
MAVIS. That’s a jalapeno. And that’s racist.

LURLEEN. I am NOT racist! I have a Whitney Houston album!

.

DELBERT: Ben, you're always running here and there
(here and there)
You feel you're not wanted anywhere
(anywhere)…
LURLEEN. Oh, good Lord—she’s moved onto “Ben”!

DELBERT: I used to say, I and me
Now it's us, now it's we
(I used to say, I and me)
(now it's us, now it's we)
MAVIS. Oh, my stars and garters.

DELBERT: Ben, most people would turn you away
I don't listen to a word they say
MAVIS. This IS serious, Lurleen--Delbert’s spouting lyrics about a
pet rat.

DELBERT: I'm sure they'd think again
If they had a friend like Ben
LURLEEN. “Ben” is about a rat? Really?
MAVIS. Focus on the topic at hand, Lurleen…Delbert—DELBERT!

DELBERT: (a friend) Like Ben
(like Ben)
Like Ben
LURLEEN. Delbert loves a rat named Ben?
MAVIS. That’s not our Delbert talkin’—that’s Michael Jackson.
Michael Jackson is Satan.
LURLEEN. Mavis—what will we do? I don’t want to see what
happens when he gets to “Thriller”!
MAVIS. Lurleen…we gotta think…what would ELVIS do?
BOTH. Our Lord and Savior.
LURLEEN. Depends. Do you mean Fat Vegas Elvis or 50’s Elvis?

DELBERT: They print my message in the Saturday Sun
I had to tell them I ain't second to none
MAVIS. We can’t wait—we gotta exorcism Delbert—now!
LURLEEN. But how?
MAVIS. We need an old priest and a young priest.
LURLEEN. That only works with Linda Blair. We’re facing the
Acopmalice!
MAVIS. The spirit of Elvis compels you!
BOTH. THE SPIRIT OF ELVIS COMPELS YOU!

DELBERT: And I told about equality and it's true Either you're wrong or you're right…hee hee. LURLEEN. Gosh all-Mighty—“Black or White”!

.

DELBERT: But, if you're thinkin' about my baby
It don't matter if you're black or white
LURLEEN. Humanity is DOOMED. Mavis!
MAVIS. Not yet. You know what we need to do!
LURLEEN. You mean…
MAVIS. Exactly!

(MAVIS and LURLEEN say their lines in unison while DELBERT says his at the same time.)

BOTH. You ain’t nutin but a hound dog, Michael Jackson! Lying all the time! You ain’t nuthin but a hound dog, Michael Jackson! Crying all the time! You ain’t never caught a rabbit—you ain’t no friend of mine!

DELBERT: ABC It's easy as, 1 2 3
As simple as, do re mi
A B C, 1 2 3
Baby, you and me girl
LURLEEN. Michael Jackson is too strong, Mavis. Stronger than Elvis!

(DELBERT starts moving about the room, as if floating)

DELBERT: (says the following while LURLEEN and MAVIS talk) Say, say, say what you want but don't play games with my affection… LURLEEN. MAVIS! Delbert is lemonaiding! MAVIS. Lemonaiding? LURLEEN. Levertating? He’s LEVERTATING!!! MAVIS. The WORD is LEVITATING! And I can see! When your brother starts flying around a living room, it’s a bit hard not to notice! LURLEEN. Delbert! You stop laminating around my trailer! Those ceiling panels are new!

DELBERT: Take, take, take what you need but don't leave me with no direction… MAVIS. I have had JUST ABOUT ENOUGH of this! You get down here this INSTANT, you evil flying Michael Jackson Delbert!

DELBERT: (Said while L and M talk) All alone I sit home by the phone waiting for you baby

(baby)

.

Through the years how can you stand to hear my pleading for you dear?

LURLEEN. Should I hit ‘em with my tennis racket?
MAVIS. (pause) You play tennis?
LURLEEN. Not really. I mostly use it to kill bats.
MAVIS. Now, THAT has to be a sight!
LURLEEN. But I don’t want to swat Delbert—even if he’s possessed
by Michael Jackson. And looking like a moth about to
kamikaze a bug zapper.

DELBERT: You know I'm crying, ooh ooh ooh ooh ooh MAVIS. Oh, for cryin’ out loud—MICHAEL JACKSON! Get down here before we nail you with this bat-killin’ tennis racket.

(DELBERT stops levitating)

MAVIS. Quick—you still got your Intranet?
LURLEEN. Sure!
MAVIS. Search “How to do an exorcism in a double wide trailer
after Elvis has failed”!

DELBERT: Because I'm bad, I'm bad come on
You know I'm bad, I'm bad come on, you know
You know I'm bad, I'm bad come on, you know
LURLEEN. That’s too long!
MAVIS. Just type, Lurleen!
LURLEEN. It’s times like this I miss “Ask Jeeves”..
MAVIS. TYPE!
LURLEEN. Okay (types slowly—hunt and peck) How do you spell
exorcism?
MAVIS. Move over! (pause) Boy…you have an interesting
search history, Lurleen…”Garth Brooks nekkid”?
LURLEEN. NEVER MIND THAT! Type!

DELBERT: And the whole world has to
Answer right now
Just to tell you once again
Who's bad
MAVIS. Okay—here we go…HEY! When they do exorcisms in
Japan they make you take a bath in vodka to “cleanse the
body and spirit”…
LURLEEN. We ain’t in JAPAN, Mavis! Focus!
MAVIS. Excuse ME for tryin’ to educate you…
LURLEEN. What does it say?

.

MAVIS. It says, “Tell it to go away.”
LURLEEN. What? That’s it? Don’t we need holy water and a Bible?
MAVIS. Whatcha got?
LURLEEN. Diet Coke and a copy of “The Elvis Cookbook”.
MAVIS. That’s it? You don’t have a Bible?
LURLEEN. I’m a light reader.
MAVIS. Beggars can’t be choosers. Let’s do this!
BOTH. The Spirit of Elvis’s cookbook compels you!
MAVIS. Pour the Diet Coke on her!
LURLEEN. I most certainly will not. I just rug-doctored my carpet!

DELBERT: 'Cause this is thriller, thriller night
And no one's gonna save you from the beast about to
Strike
LURLEEN. Oh,no…THRILLER!

DELBERT: You know it's thriller, thriller night
You're fighting for your life inside a killer
Thriller tonight
MAVIS. DO IT!! Heed our righteous Diet Coke, Satan Michael
Jackson!
LURLEEN. (lamely pours Diet Coke) Heed this diet cola beverage,
Satan! Heed! Heed!
MAVIS. What does “heed” mean?
LURLEEN. I think it is the past tense of “Hide”.
MAVIS. How can it mean “hide” when you’re pouring Diet Coke
on Satan?
LURLEEN. Don’t yell at me! I’ve never exorcised Michael Jackson
before! One doesn’t normally plan for such events!

DELBERT: You better run, you better do what you can Don't wanna see no blood, don't be a macho man You wanna be tough, better do what you can So beat it, but you wanna be bad LURLEEN. It’s no use! Michael Jackson has beaten us! MAVIS. I will not concede defeat to “the KING’ of Pop! LURLEEN. Read from the HOLY COOKBOOK! It’s our last chance! MAVIS. The Official Elvis Peanut Butter, Banana and Bacon Sandwich Recipe—ahem… LURLEEN. Heed the recipe, Satan Michael Jackson! MAVIS. Shut up, Lurleen! AHEM…Place 2 pieces of white bread in the toaster on a light setting. Heat skillet over medium heat with 2 tablespoons butter. While the bread is toasting, in a small bowl, using a fork mash the ripe banana until it reaches a smooth consistency. Using a knife, take both…

.

(while MAVIS reads the recipe, DELBERT chants the following)

DELBERT: Just beat it, beat it, beat it, beat it
No one wants to be defeated
Showin' how funky strong is your fight
It doesn't matter who's wrong or right….
MAVIS. Oh for cryin’ out loud—I’ve had enough! Time to get
physical! FEEL The WRATH OF ELVIS, MICHAEL
JACKSON!

(MAVIS hits DELBERT with the cookbook—DELBERT immediately snaps out of spell)

DELBERT: Hey-hey-hey….HEY! What—What the HADES are you doin’? MAVIS. Speak not thy lies, Satan! (hits him again)

DELBERT: I am NOT Satan! MAVIS. Then, away with thee, Michael Jackson! LURLEEN. Hit him again! He’s still twitchin’!

DELBERT: What the…I’m Delbert Flanagan, Mavis! MAVIS. Lies, Beelzebub!

DELBERT: STOP HITTIN’ ME! MAVIS. You not Michael Jackson no more?

DELBERT: I most certainly am not.
LURLEEN. Then will you kindly explain what’s going on?
MAVIS. Be thorough. Or I’ll brain ya with this holy cookbook
again.

DELBERT: I got out of detox, and I sort of…celebrated at the Dixie Lounge and Grill. Stuff got fuzzy after that. LURLEEN. That aint the point of detox, Delbert.

DELBERT: Well, if I stop drinkin’, will you stop hitting me with
cookbooks?
MAVIS. Only if Elvis --
ALLURLEEN. --Our Lord and Savior—
MAVIS. --Deems it so.

DELBERT: I’ll take my chances. Can I go now? I ‘ve got a massive headache from that cookbook….jeez Louise… MAVIS. Well, it looks like we—with the help of our Lord and Savior Elvis—have saved Thelma, and probably the universe from the perverted eeee-vil of Michael Jackson. Pretty, good…huh, Lurleen? Lurleen?

.

LURLEEN. You and I must make a pact,
MAVIS. Oh, no.
LURLEEN. we must bring salvation back
MAVIS. Lurleen, NO!
LURLEEN. Where there is love…
BOTH. I'll be there…
```

---

## IC-1482: Stand: The Rosa Parks Story

- Title: Stand: The Rosa Parks Story
- Author (byline): Stephanie Spencer
- Work: Stand: The Rosa Parks Story
- Publisher: SpeechGeek
- Publication date as stated: 2013
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1340
- Already set (do not supply): none

### Source block (context only)

```text
Stand: The Rosa Parks Story by Stephanie Spencer
ISBN: 978-1-61387-043-3
Copyright 2013 by SpeechGeek.
Free performance of this play for high school and college level
competitive forensics is permitted. All other rights reserved.
This PDF version of this selection, e-published in 2013, is identical to the
printed published version of this same publication dated 2013. This
statement along with the entire printed PDF of this publication must be
presented at any National Forensic League District or National event for the
script to comply with NFL rules per the request of the Executive Director.
This and other selections of quality performance literature for competitive
oral interpretation are published by SpeechGeek.
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
SCENE ONE

(An old Rosa Parks is waiting at a bus stop.)

ROSA. Mmm-hmm. As usual, I’m just waiting to take the Cleveland Avenue bus home. Yep, I’m still riding them. Seems a little silly for me, of all people, not to. Can you imagine me, Rosa Parks, taking a taxicab? That don’t even sound right.

When I was a girl there were thirty-six seats on a Montgomery bus. First ten were only for whites, even if there were no white passengers on the bus. There was no law about the last ten seats, so you know what that means. Mmmhmm, they were for us black folk. That’s right. And if those filled up then we had to stand. And when we wanted to get on the bus they had to pay in the front go around and climb into the back. Shoot! Some days I think I wasn’t even resisting segregation that day in 1955. I was just tired and wanted to sit down!

(chuckles to herself) It seems I took a stand by sitting.

SCENE TWO ROSA. I know what they say about me in the books, nowadays. But I’ll be the first to tell you, I was a regular person. I was just as good as anybody else. That’s why all this started.

One of my earliest memories was a remarkable time right after World War 1. I was five or six years old and a soldier from the north patted me on the head and said I was a cute little girl. Later that evening, my family just couldn’t quit talking about how the Yankee soldier had treated me like I was just another little girl and not a little black girl.

I think it was right around that time that I was old enough to realize that we were not actually free. The Klu Klux Klan was riding through the black community, burning churches, beating up people, and even killing people. At one point, the violence was so bad that we’d go to bed with our clothes on so we’d be ready to run if Klansmen broke into our house.

Sometimes I’m asked how I lived with that kind of fear. The only way I knew how: I got me an attitude.

Any little thing I could do, I did. It wouldn’t be anything of great significance, but it was my small way of expressing hostility. I remember that sometimes I would call white men by their first names or their whole names and not say “Miss” or ”Mister.”

Never really lost that attitude. It drove my grandma mad. She once remarked that I was much too headstrong. If I weren’t careful, she said, I’d be lynched before I reached twenty years old. She said I was “so high-strung that I was going to get myself strung high.”

I don’t mind telling you that it hurt when she said that. I felt I was very much in my right to defend myself. It was later that I came to understand that she was scolding me because she was afraid for me. It wasn’t because she thought they were right but because she thought they was stronger than her— stronger than justice.

When I was older, I joined the National Association for the Advancement of Colored People all because of folks like Recy Taylor. A black woman on her way home from church, Recy was kidnapped and raped by six white men. A grand jury refused to indict the men even though the driver of the car confessed and named his accomplices.

You see, that was the 1940's when people took a lot without fighting back. They bowed their heads and said their “misses” and “misters.”

But look at me. Do I look like someone who can take a whole lot? No. I mean, here it was half a century after the first segregation law and there were 50,000 African Americans in Montgomery. More of us rode the buses than whites did. It was humiliating riding segregated buses twice a day and five days a week just to go downtown and work for white people.

The Montgomery N.A.A.C.P. was beginning to think about having a boycott of the city buses. That’d really hurt the bus company. I remember them asking a few people if they would be willing to stay off the buses to make to make things better for us and them saying that they had to go too far to work. Folks thought a petition would be a good start. I didn't feel anything could be accomplished with a piece of paper in my hand asking white folks for any favors.

I knew that the only way we could fight was by filing suit against the city of Montgomery over bus segregation. But they had to have the right plaintiff and a strong case. The best plaintiff would be a woman because a woman would get more sympathy than a man. And the woman would have to be above reproach, have a good reputation, and have done nothing wrong but refuse to give up her seat. So yes, we were planning on setting up a scene.

But that is not why I refused to give up my bus seat to a white man on Thursday, December 1st, 1955. I did not intend to get arrested. I did not intend on starting the Civil Rights Movement. Tell you the truth, if I had been paying attention I wouldn’t have gotten on that bus in the first place.

See, what happened was when I got off from work that evening, I went to Quart Square, as usual, to take the Cleveland Avenue bus home. A bus came and, without even checking the number, I got on.

SCENE THREE

(The scene is a flashback of a YOUNG ROSA confronting a BUS DRIVER.)

YOUNG ROSA. Here’s my dime.

BUS DRIVER. Get off the bus and go to the back door and get on.

YOUNG ROSA. (sighs) Sir, I’m already on the bus and I’m very tired. I don’t really see the need of getting off and then getting back on. Can I just go on through?

BUS DRIVER. Them’s the rules, get off and get back on or just get off.

YOUNG ROSA. Sir, there are no seats back there and I don’t know how I’m going to squeeze in.

BUS DRIVER. Look, if you can’t get through the back door and sit back with your kind, then get off my bus.

YOUNG ROSA. (thinks about it) No.

BUS DRIVER. Excuse me?

YOUNG ROSA. I said NO. (YOUNG ROSA sits down in the front seat.)

BUS DRIVER. Get up or I’ll call the police.

YOUNG ROSA. You may do that sir, but I’m not moving.

BUS DRIVER. Are you crazy?

YOUNG ROSA. I do not accept being pushed even at the cost of my life. I was raised to be proud and I have no need for some white person to disapprove of me sitting down in an empty seat. I’m tired, tired of all of this. So, no!

BUS DRIVER. You’re going to jail!

YOUNG ROSA. Then you’re driving me there in this here seat!

SCENE FOUR

(The older ROSA returns to the audience.)

ROSA. Like I said, that attitude never did go away. So they arrested me, of course. Shortly thereafter the Montgomery bus boycott began.

Some people think it only took a few months for things to change, but that ain’t true. It took generations. I think of it now, it took us the whole of our history in this country for things to change. If you wanna know the truth, I think it’s sad and terrible that so many people know my name but not nobody know the name of the hundreds of thousands of black folk who died before me. I try to remember what it takes for one person to be regular. It takes a lot of folks fighting hard to get you there. And here I am, just a regular person that a lot of folks think changed the world. Imagine what anybody else can do.

It’s nice to see how far we come. (looks up) Ah, my bus is here. But we’ve still got a long way to go.
```

---

## IC-1483: Still

- Title: Still
- Author (byline): Darlene S. Auxajas
- Work: Still
- Publisher: SpeechGeek
- Publication date as stated: 2010
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 816
- Already set (do not supply): none

### Source block (context only)

```text
Still by Darlene S. Auxajas
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
(Jana begins by singing from the song “Hush Little Baby.”)

She’ll be seven months in a couple days. It’s crazy how quickly time flies by, because it seems like just yesterday I was trying to convince my husband Richard that having a child was the best thing for us then. I ended up telling him that I once heard on a television show: raising a kid is like raising a dog that slowly learns how to talk. And it worked.

Would you like something to drink? Coffee? Tea? Yes? Okay. (trip over shoes)

Oh, these are Richard’s shoes. I like to leave them out…just in case. I know it’s weird; people keep telling me to just put them away because “he’s not coming home, Jana!” But I think it’s easier for Annabel if I leave his things out. If not, it’s reassuring to me, at least. It’s been really hard without him around.

And I know Annabel’s barely seven months old but I think she still knows what’s going on--maybe not that her father is serving a life time sentence in jail--but she recognizes his presence is gone.

It’s not easy being here by myself, but Annabel’s my world.

To make matters worse, the newspapers are filled with stories of Richards’s trial. “How does his wife feel about this?” “What’s the next step for Annabel?” Because in Lenard, Oklahoma--population two hundred--there’s nothing else to talk about and everyone knows everyone.

Across the street there’s Marcel Stremp: the poster woman for The Old Cat lady—she’s got like fifty. Next door to her are the Prices—beautiful family, but Judy Prices’ downstairs is like a clown car, you know, just kid after kid after kid. And then next to them are Mr. and Mrs. Jones. They have a son around Annabel’s age. They were good friends.

Oh! The kettle! Your tea! Sorry!

We’ll make a cup for Richard, too. Just in case he comes home, he’ll have a warm cup of tea waiting for him. So he sees his family has missed him.

The press likes to wonder if I’m angry with Richard for what he did. No, I’m not. Because he was a damn good father and husband, no matter what they say. He was loving and hard working and—yes, he had a temper—but he was loyal. I could never be angry. Heartbroken without him, maybe, but no anger. The tabloids all argue that he should be given the death sentence. But capital punishment is just so controversial these days; they can’t make a decision, which is good. Because no one really knows what happened--or understands—and, frankly, Annabel needs a father.

We were a happy family before all this, you know. See our Christmas picture from a last December? We were so happy, (melt into photo) posing there. Richard was holding Annabel, but she started to cry and cry so I took her from him. And I’d try explaining that crying was just how she communicates, Richard, but he was just getting angry and yelling and threatening until, “I got it Richard. Maybe she wouldn’t cry so much if you didn’t yell so often. I’ll handle it.”

(melt out)

Annabel’s much better now, though. It’s still not easy raising a daughter on your own, but she doesn’t cry much anymore. She sleeps most of the time. She is so peaceful when she sleeps.

Thank you for visiting. Tragedy is hard and we haven‘t had many visitors lately. It’s like heartbreak is contagious. It’s nice having someone else around. Oh, the neighbor Mrs. Jones from down the street came by a few days ago, but that was unexpected. (melt into scene)

I was making dinner, and setting the table when the doorbell rang. So I pick Annabel up and go to answer it. It was Mrs. Jones, who needed to borrow some sugar. So I say, “Of course. Just hold Annabel for a moment.” And I go back to the kitchen to get her a cup of sugar. And when I return, Mrs. Jones’ face had turned a pale blue and she was shaking like a leaf holding my daughter.

“What are you doing? What you’re doing to this poor child—to yourself—it’s sick, Jana. It’s insane. You’re crazy, Jana. Crazy”. (melt out)

Shh, sweetie. Shh. (Places Annabel in the crib while humming “Hush Little Baby” once more.)

Maybe I haven’t handled Richard’s murder trial ideally. I leave the hall lights on at night in case he comes home. I leave his shoes out in the hallway. I set his plate at the table when it’s time for supper. But I’m not crazy. I just can’t let him go. Not any piece of him—every piece of him needs to stay. We were a family. Now he’s in jail for killing…killing…Annabel. Sick of her constant crying, suffocating her perfect little face. (lean onto crib) But when I look at her porcelain, still, little body I remember our family. I’m not crazy. Richard and Annabel will live forever.

(Brush off meltdown, pick up Annabel, and kiss her forehead. Final line to the audience.) Shh. The baby is sleeping. (Sings a line of “Hush Little Baby” once more.)
```

---

## IC-1484: Sugar Addiction

- Title: Sugar Addiction
- Author (byline): Gregg Moeller
- Work: Sugar Addiction
- Publisher: SpeechGeek
- Publication date as stated: 2016
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1508
- Already set (do not supply): none

### Source block (context only)

```text
Sugar Addiction by Gregg Moeller
ISBN: 978-1-61387-099-0
Copyright 2016 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is permitted. All
other rights reserved.
This PDF version of this selection, e-published in 2016, is identical to the printed published version of this
same publication dated 2016. This statement along with the entire printed PDF of this publication must
be presented at any National Speech and Debate Association District or National event for the script to
comply with NSDA rules per the request of the Executive Director.
This and other selections of quality performance literature for competitive oral interpretation are
published by SpeechGeek.
For more information and performance rights, contact SpeechGeek.
SpeechGeek
248 Arlington Park Dr.
Hot Springs, AR 71901
Phone: 1-888-742-2028
Email: thegeek@speechgeek.com
Web: www.speechgeek.com
Facebook: www.facebook.com/speechgeek
2
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
CHARACTERS_ Jinx Munroe—member of the “Sugar Snacks” , the world’s biggest singing group Margaret—Jinx’s biggest fan, and singer wannabe—

(Scene opens on JINX tied up in a chair and blindfolded, with Margaret panicking)
MARGARET. Oh, God—what have I done?
JINX. Like, why am I tied up? HEY! Is Ryan Seacrest behind this?
MARGARET. Quiet! People will hear you!
JINX. Ryan? You goofy goob! Untie me!
MARGARET. Ryan Seacrest isn’t here.
JINX. Snooki? Is this your idea? Gimme a hug!
MARGARET. What? I’m not Snooki!
JINX. Michelle Obama? No? Betty White! You never could hold your

liquor! Now untie me before I tell folks about you and Colin

Farrell!
MARGARET. None of those people are here—just me. Your biggest fan!
JINX. My biggest fan?
MARGARET. Yes. I’ve idolized you since your first Disney Channel special,

“Sugar my Syrup!” All of my clothes are from your Jinx Munroe

Fashion Line at Dollar General. I have an irregular heartbeat

from overdosing on Sugar Snacks chewable vitamins. I have

kidnapped you, Jinx Munroe, and I am going to BE you. JINX. Oh—Okay! MARGARET. Don’t you get it? I want to replace you. I want to take over your

life and live it as my own! JINX. Gnarly! Sugar-licious! MARGARET. I watched your documentary, “Insulin for the Sugar Smacks” on

E-TV five times! I know everything about you!

3 JINX. Oooh-kay! Who was my first boyfriend in grade school! MARGARET. (insert any celebrity here)! You met him at Church camp, and he

gave you a hickey on your arm so you could tell people you fell

down while genuflecting! JINX. Really? That’s—SO COOL! Okay—what are like, my likes and

like dislikes? MARGARET. You like unicorns (both squeal), candy corn, Will Farrell when

he’s sincere, boys who are not afraid to commit to a

monogamous relationship and unicorns—again! (both squeal

again) JINX. This is so FUN! Now what are my dislikes? MARGARET. You dislike meat (unless it is rotisserie chicken or fajitas), most of

the people at NBC Nightly News, the Philadelphia Phillies and

things with gravy on it!
JINX. Yay me!!
MARGARET. Miss Munroe…I’ve always worshipped you.
JINX. Now—don’t say “worship”—that puts me with God and Jesus and

Madonna. Say, “Idolize with a frenzy usually applied to rabid

skunks”! Or just say “Sugar Smack Love!” MARGARET. Exactly. Sugar-Smack Love! That is why I must BE you. That is

why you’re tied up. JINX. So…you’re not Ryan Seacrest?

JINX. Is this a surprise party? (squeals) MARGARET. No—no—no…I’ve kidnapped you. I’ve taken you against your

will. JINX. Against my will? Well, that was not nice. MARGARET. But that is the ony way that I can become a Sugar Snack—you

needed to be ou of the way. So, I kidnapped you.

4 JINX. But how? MARGARET. I drugged your choco/marshmallow latte and snuck you out

through a laundry chute. JINX. Really? This is a surprise party isn’t it? Did Selena Gomez put

you up to this? Selena, get out! MARGARET. Don’t you understand? I have kidnapped you! I have taken you

against your will, and you are locked up in a mobile home

parked in a undisclosed location!
JINX. Oh—Oh…I get it now…you are Zac Effron.
MARGARET. No! I am not Zac Effron!
JINX. Corbin Bleu? Vanessa Hutchins!
MARGARET. Oh, for crying out loud…(removes blindfold) See? There is no

one but me! JINX. You are not Ashley Tisdale. Or even Madonna. MARGARET. No! I am not! I am…or was…your biggest fan! I want to BE you!

I want to sing and dance on stage and record albums and tour

and party with the social elite! So I have kidnapped you to take

your place! JINX. How could you do that? MARGARET. Once you disappeared, the other Sugar Snacks –Brownie,

Twinkie, Maple and Yoko—would be panic stricken! “How can

we ever replace Jinx? There’s no one here that could do that!”

And I would walk in, and the others would be swept away by—

moi! JINX. Why me? MARGARET. I wrote you letters…”Tell me how I can be you?” I even sent in a

dvd of me singing along with your ABC special, “Sugar Snacks

Do the Tupac Shakur Songbook”! JINX. That was a short special.

5 MARGARET. And you never, never responded. And I was your national fan

club president for three years. JINX. No, you couldn’t be her—she was some loser who kept writing

loser letters about not going to prom or being homecoming

queen…oh. But look at what you’ve made of yourself?
MARGARET. I’m nothing—you are ev-ree-thin—guh.
JINX. But--
JINX. But, don’t you remember the Sacred Sugar Snack Pack Code of

Allegiance? C’mon..do the oath… BOTH: The Sugar Snack Pack Code of Honor Number One—Don’t

Kidnap Any Member of the Sugar Snacks in some Desperate Act. MARGARET. I always wondered why that was there. JINX. (Voice changes to a sinister timber) I knew this would happen. I

hoped it would happen. And now you have come. To save me

from myself. MARGARET. Save—you? JINX. You don’t know the pain of being a Sugar Snack. George

Clooney kisses you, then yells, “Hey—Sugar Snacks give you

cavities!” …when Taylor Swift calls you “shallow”…The nasty

looks from Barbara Streisand when she serves you at

Applebees… MARGARET. But—you’re a star! Isn’t that what you wanted? JINX. What I wanted? All I wanted was to be professor of entomology

at Stanford. To be a brain. MARGARET. A brain…you wanted to study bugs? JINX. Bugs are incredible creatures. Tireless workers—dedicated to

the common cause…and I was to be their queen. MARGARET. You wanted to be the queen of bugs? JINX. I am not “Jinx Munroe”. I am…or I used to be…Patricia Shamsky.

High school valedictorian, with a dream.

6 MARGARET. To be the idol of millions? To be a pop superstar? JINX. Superstar? (evil laugh) I wanted to teach cockroaches to attack,

and I was going to lead my army of insects and destroy Kevin

Schilling. He dumped me for some French foreign exchange

student at homecoming. MARGARET. What stopped you? JINX. Some record company executive was looking for a girl to join his

new girl group. He was missing one vital element—and then he

saw me feeding boxelder bugs in a park.
MARGARET. And you sang to them, and he fell in love with your voice?
JINX. No. He saw…my cheekbones.
MARGARET. They are magnificent.
JINX. I know. They are real. And they are spectacular. But with great

cheekbones comes great responsibility. BOTH. Just like Spiderman. JINX. Next thing I know, my hair is bleached and I’m renamed “Jinx

Munroe” and I’m dating Hugh Hefner. He’s a cheekbone man. MARGARET. And...Patricia Shamsky? JINX. Dead—like a Brazilian millipede that was stepped on by some

guy harvesting coffee beans. MARGARET. And Kevin Schilling? JINX. Him? I set fire to his house and blamed it on Beyonce. (starts

crying) MARGARET. Jinx? Jinx—why are you crying? JINX. I never wanted this—all I had were magnificent cheekbones,

and a dream to turn insects into my own personal army of

destruction. HOW did I end up here? MARGARET. But you are so talented.

7 JINX. I’ve got nothing! I can’t dance! My outfits have special electric

prods that shock me. When you think I’m dancing I’m actually

getting shocks that would cripple a heifer. MARGARET. But your voice—you sing so beautifully on “Baby Be My Sponge

Mop Sweeze”
JINX. All auto-tuning. I can’t carry a tune with a handle.
MARGARET. Oh, c’mon. I’ve been to your concerts! I’ve bought your cds!
JINX. You want proof? You’ve got proof!

Baybee—be my sponge mop squeeze

Squeeze my sponge mop, don’t tease

Squeeze me please baby baby please

Be my sponge mop squeeze…
MARGARET. God, that’s horrible.
JINX. You wanted proof.
MARGARET. My whole life is a lie.
JINX. It could be worse…you could be a eighteen year old college

freshman, majoring in advanced entomology…all you know is

insects…larvae…you dream of having your own little

pupae…WAIT! You CAN be ME!
MARGARET. Huh?
JINX. Let me see your cheekbones.
MARGARET. But, I could never match with…
JINX. LET ME SEE THEM!

(JINX grabs her face rather roughly—she checks out the cheekbones) JINX. Yes…this could work. This could work. MARGARET. What could work?

8 JINX. Making your dream---and mine—a reality. You said you can

sing—do it.
MARGARET. What?
JINX. SING, YOU TROLL!
MARGARET. You’re scaring me…
JINX. Who kidnapped who?
MARGARET. Good point.

Squeezy Squeezy Sponge Mop-Mop

Come on baby be the top

Squeezy Squeezy Sponge Mop-Mop

Squeeze my love dry for you
JINX. Uh, yeah.
MARGARET. But maybe if I add some choreography…”Squeezy Squeezy—“
JINX. NO! No—that’ll do just fine. (MARGARET continues to sing while

Jinx pulls out a cellphone) JINX. (In her dumb Jinx voice) Hello…Irving? Jinx here. No—I’m fine—

I just was diverticulitis for a few minutes….say--, don’t be afraid

if I’ve changed when I get back—oh, hair color, height, clothes—

I was decapitated this morning, but I’m all better now! Oh, you

silly—you KNOW the cheekbones are perfect as ever! Love you

better! MWAH!

(as MARGARET continues singing and “dancing”) JINX. Free…free…FREE! HA HA HA!!!

9
```

---

## IC-1485: Terrestrial News at Five

- Title: Terrestrial News at Five
- Author (byline): Matt Mills
- Work: Terrestrial News at Five
- Publisher: SpeechGeek
- Publication date as stated: 2015
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1900
- Already set (do not supply): none

### Source block (context only)

```text
Terrestrial News at Five by Matt Mills
ISBN: 978-1-61387-089-1
Copyright 2015 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2015, is identical to the printed published
version of this same publication dated 2015. This statement along with the entire printed
PDF of this publication must be presented at any National Speech and Debate Association
District or National event for the script to comply with NFL rules per the request of the
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
(Two news reporters, Stacy and Randy, stand holding microphones in front of a large park.)

STACY. Welcome back to Channel 12, KOPP…PPPP, Your News at Five.

I'm Stacy Stacyson… RANDY. Along with, as always, Randy Randerson. Boat collector

extraordinaire (winks). STACY. We're coming to you live tonight for a very special broadcast. As

you can see we are not in our normal studio... RANDY. I mean, there aren't any walls around here! Can't be the studio.

Look! Where are the walls? STACY. Earlier this afternoon, two bearded hunters on their way back

from an unsuccessful hunting trip to the Poconos spotted an alien

ship landing here at our very own Walterson Park. RANDY. I mean, right?! Isn't that insane! Crazy. STACY. While many of you may not subscribe to the idea that aliens

exist— RANDY. I subscribe! To a lot of things. Cat Fancy, Bird Fancy... STACY. We'd like to share with you their stories of what exactly

happened. RANDY. Oh, gosh, I'm too excited. Stories! STACY. We have with us now the two gentlemen in question. Failed

hunters, tell us…what exactly did you see here in Walterson

Park?
HUNTER 1. Well, there was like, you know. This big…thing.
HUNTER 2. Yep, yep. I seen it.
HUNTER 1. And then it went, like, down a little bit.
HUNTER 2. Little to the side, too.
HUNTER 1. Yeah, to the side. And uh…there was this light.
HUNTER 2. Big light.
HUNTER 1. Ginormous.
HUNTER 2. Downright prodigious.
HUNTER 1. So then it sort of, like, landed. Like the way a hamburger lands on

them plastic trays at a fast food station. HUNTER 2. You're makin' my tummy growl, Reggie-Ray. STACY. This “thing” you two spotted…was it like anything you'd ever

seen before?
HUNTER 1. No, ma'am, it was unlike anything I'd ever seen before.
HUNTER 2. Yes’sir.
RANDY. Were you scared? (to the camera) I'd be scared.
HUNTER 2. Yes’sir.
HUNTER 1. No ma'am.
HUNTER 2. What?
HUNTER 1. I was fine.
HUNTER 2. Alright then.
STACY. So this “thing” landed, there was a bright light and…what

happened next? HUNTER 1. So all of a sudden this thing just opens up and…BOOM! Out

comes…our little friend here...

(He slides forward a big scary alien!)

ALIEN. (drools and growls)
STACY. Uh...
RANDY. Oh my gosh, can we keep it?!
STACY. Is that what I think it is?
HUNTER 1. Depends on what you think it is.
HUNTER 2. If you think it's an alien, you're right. If you think it's something

else, I'm pretty sure you're wrong, but not positive. ALIEN. (growls) STACY. Fellows…are you telling us and our viewers at home that you

have actually captured an extra-terrestrial? HUNTER 1. Heck yes, ma'am! May not have been able to catch any pheasant

this morning, but we sure got us a marlin and then some on this

one! HUNTER 2. Then some. STACY. Wow, planet Earth, you just heard it first here on Channel 12—an

alien creature has landed in Walterson Park and is here with us

right now.
RANDY. My horoscope was so right; this is a big day for me!
HUNTER 1. So…what do we do now?
HUNTER 2. He don't look so friendly…
ALIEN. (growls)
STACY. As one of the first members of the human race to communicate

with an extra-terrestrial life force, I will do my best to give it the

benefit of the doubt and hope that it comes in peace. I will do so

by conducting an interview, the same way I would conduct an

interview with any other person of interest.
RANDY. Ooh, yeah! Ask him what his favorite Leo DiCap' movie is!
STACY. No. Now, Mr. Alien…
RANDY. Is that your name? What if we call him, like…Bob? Ooh, or

Juancardo?!
HUNTER 1. I've been callin' her Sheila.
HUNTER 2. Chrysanthemum.
STACY. We'll figure out its name shortly enough, guys. Let's just focus.

Now… Mr. or Ms. or Mrs. Alien…uh…shoot, I'm drawing a blank.

What should I ask it?
RANDY. Do you have jello in space?
ALIEN. (pause, growls menacingly)
RANDY. Okay, no jello. Got it.
HUNTER 1. Do you like sports?
ALIEN. (pause, smiles)
HUNTER 2. Oh! That's nice.
STACY. Where do you come from?

(The alien glares silently back at her. Then it burps obnoxiously at them.) STACY. Well, that's rude. RANDY. Alright, next question… Do you want to go to the dance with me?

Check yes, no, maybe—
STACY. Randy!
RANDY. What? You're not mad that I didn't ask you, are—
STACY. There are more important matters for us to discuss at the

moment! RANDY. Um…like?! STACY. Why this alien is here, why it traveled millions of miles just to end

up her at Walterson Park talking to a news crew from the third-

rated news source on its own channel? RANDY. Hey, we'll get to second some day! STACY. We've got to figure out its motive. Its agenda. What it wants. (to

the alien) What do you want? ALIEN. (pause) Destroy humans. RANDY. Okay, cool! We got it figured out. Now, on a scale of 1-10…(re:

his appearance) Go. STACY. Randy, he just said he wants to destroy the human race! RANDY. Oh. Huh. Well, maybe there's something wrong with the

translation. STACY. Yeah? RANDY. I mean, I'm amazed it knows any English. I mean, we live like

twenty miles from Mexico and I don't know a lick of Spanish past

tortilla. This thing's from at least…like…nine-hundred…miles

away, so…yeah. Ask him again.
STACY. (clearly) Alien…do you come in peace?
ALIEN. No.
STACY. And you want to…
ALIEN. Destroy humans.
RANDY. Uh…and you will stop at…
ALIEN. Nothing.
STACY. Until we're…
ALIEN. Destroyed!
STACY. Huh.
RANDY. You know… I think that might be a problem.
STACY. Yeah, that doesn't sound any better.
HUNTER 1. Nope.
HUNTER 2. This is bad.
HUNTER 1. Real bad.
HUNTER 2. Running out of deer-urine in the middle of a hunt kind of bad.
STACY. Well, America, uh…I'm sorry, I feel like I should be doing

something here to help us out as a species, but...I'm somewhat in

shock right now. RANDY. Should we like…trap it in a cardboard box? With like a little trap

and a carrot to draw it in-- STACY. I think it'll figure that out. ALIEN. Prepare for extinction, earthlings!

(The alien raises its arms and flicks its tongue at them in an intimidating show.)
STACY. Oh, my!
RANDY. Son of a biscuit that's terrifying. Oof!
STACY. For anyone who's watching, please call the police, or…the

president, or a tow-truck, or something!

RANDY. Call my mom and say hi and that I love her and that my cat needs

to be fed on Tuesdays and Thursdays! Tuesdays and Thursdays,

Mom, you always forget! Gah!
ALIEN. Agh, earthlings!
STACY. Randy, look!
RANDY. Oh…oh my…my…Channel 12 viewers, it appears as though the

whole county is descending upon the scene, this is madness!

Darn tootin' madness!
ALIEN. Humans, bad! Must…destroy!
RANDY. Aw…you know, he's actually kind of cute when he talks like that.
STACY. No he's not, Randy. He wants to kill us all! Channel 12, it appears

we are all in grave danger here. Please, do not come down to

Walterson--oh, oh my, my…here come the soldiers!

(Two soldiers come marching down, looking around through the scopes on their rifles.)
SOLDIER 1. Do you see the target?
SOLDIER 2. It's right there.
SOLDIER 1. There?
SOLDIER 2. No, there.
SOLDIER 1. Ohhh, there.
SOLDIER 2. There.
SOLDIER 1. Thanks.
SOLDIER 2. You've got it!
RANDY. Save us please, majestic soldiers!
STACY. Channel 12, things are getting out of hand down here at the park.

The army has arrived, and-- RANDY. Oh my god, hi Tom! Tom Tom, over here! STACY. That is General Tom Tomerson we are seeing as he leads the

troops towards saving the world from this vile and, honestly,

somewhat smelly extra-terrestrial demon.

(The general marches around the scene, barking orders at his assistant, who follows
behind.)
GENERAL. Give me seven snipers over there...
ASSISTANT. Snipers, go sniping!
GENERALS. Infantry come up through these trees…
ASSISTANT. Infantry, don't act like infants in those trees!
GENERAL. And leave radio ops with me.
ASSISTANT. Radio ops, uh…opt to use your radio, should you need to?
GENERAL. Good work, Henry. I'm moving in to confront this little monster.
ASSISTANT. You go, general!
RANDY. Yes, he's the best! TOM! GIVE ME YOUR AUTOGRAPH LATER--

he's a little busy, it's okay. STACY. Planet Earth, it appears as though United States General Tom

Tomerson has arrived on the scene to enter into talks with the

alien beast. Thank you, General!
RANDY. God I love that guy.
STACY. Who doesn't?!
ALIEN. (growls)
STACY. Oh, yeah.
RANDY. That makes sense.

GENERAL. Alright, Alien, we're gonna talk this whole thing through. But

first...Henry, come here!
ASSISTANT. (runs up) What is it, General?
GENERAL. I'm going to use you as a human shield.
ASSISTANT. Oh. Really?
GENERAL. Yes.
ASSISTANT. Okay, General.
GENERAL. Get on over here…

(His assistant trudges in front of him; the general shifts into place.)
GENERAL. Good. Now, Mr. Trespasser--I mean, Mr. Alien…
ALIEN. (growls violently)
GENERAL. What do you expect to get from our planet?
ALIEN. Destroyed humans!
GENERAL. Hm…and what can we do to change your mind?
ALIEN. Nothing! I change your mind!
GENERAL. Oh, really?
STACY. Alright now America, it appears as though the extra-terrestrial is

going to debate our fearless general.
RANDY. Ooh, an honest competition of intellect and wit?! Who's gonna
win?!
STACY. Gotta love debate, America.
GENERAL. What chance do you think you have against us, huh? You're one

measly little gremlin against the best army in the world. We'd

blow you to pieces before you could even try anything. ALIEN. I promise you, general. We're very convincing in our ways. GENERAL. Yeah, right. Like you could ever—

(With a pulse shot from the alien, the general gets zapped--he stares back in a daze.) GENERAL. You're right, alien overlord. You are very convincing in your ways. STACY. Oh, my. It appears…it appears as though our planet's visitor has

begun using its powers to brainwash the United States Army!
RANDY. Looks like we've got ourselves in a pickle, gang!
SOLDIER 1. I want to kill and then repopulate.
SOLDIER 2. Blorg blorg blorg blorg blorg.
RANDY. It's like they're speaking Spanish!
ALIEN. (growls, waves)
STACY. Uh, oh. What's that? It looks like the alien wants our attention.
RANDY. Finally. About time you're ready to answer my questions! So. Leo

DiCap, go!
STACY. Randy!
RANDY. Sorry.
ALIEN. News-humans of Earth…
STACY. Yes?
RANDY. That's us!
ALIEN. Talk to me.
RANDY. Okay! About what? We could talk about movies, or coffee roasts,

or Italian prime ministers… ALIEN. Talk to me about me!

STACY. Huh? RANDY. Now...that's kind of a silly request, Mr. Terrestrial...only

celebrities and Bridezillas can demand to talk about themse—

(The alien fires a pulse shot at them! Stacy and Randy get zapped then stare at the alien,
dazed.)
STACY. We're very glad you're here, Bolzor.
RANDY. Yes. You are a beautiful creature and a wise and all-consuming
leader.
STACY. Yes.
RANDY. Yes.
HUNTER 1. Oh, no.
HUNTER 2. Oh, yes, Reggie-Ray. I think we're goners!
ALIEN. (growls)
HUNTERS. AH! Run away!

(The hunters run as the alien continues zapping everyone in sight.)

(Transition to the news studio in the future. Stacy and Randy sit as anchors.) STACY. Well, I hope none of you missed our harrowing experience down

at Walterson Park. It certainly was a monumental night that

forever changed the course of human history. RANDY. Yeah, that sure was something else. Some. Thing. Else. STACY. I know I, personally, am forever changed by what happened. RANDY. Me, too. Me, too. STACY. Well, my fellow Blorgmericans, this is Bloxblor, reporting for

Channel Blorg: 'More Blorg At Four'. RANDY. And I'm Blorgy. Tune in next week as we uncover the truth about

the human race that once existed and talk about the greatest films

that one man, Leonardo DiCaprio, ever created.
STACY. That's all we have for tonight, but remember...
RANDY. Conquer the galaxy and all hail Lord Boxlblorg.
STACY. Goodblorg, fellow Blorgs.
RANDY. And remember…you stay blorgy, Blorgmerica!
```

---

## IC-1486: The Art of Assembly

- Title: The Art of Assembly
- Author (byline): Jonas Taylor
- Work: The Art of Assembly
- Publisher: SpeechGeek
- Publication date as stated: 2017
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1216
- Already set (do not supply): none

### Source block (context only)

```text
The Art of Assembly by Jonas Taylor
ISBN: 978-1-61387-303-8
Copyright 2017 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2017, is identical to the printed published
version of this same publication dated 2017. This statement, along with the entire printed
PDF of this publication, must be presented at any National Speech and Debate Association
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
NICK. (to the paper instructions) Okay, what comes next? What comes next?

(to the audience) I’m not trying to be melodramatic, but IKEA is evil. Seriously, look at this! In what world are these instructions useful? I have been working on this crib for weeks. And I know I’m not, like, Bob the Builder or anything, but I have a hard time believing this is my fault.

I almost got the crib together about a week ago, then Rachel, my wife, came in and said, “I think you built it upside down. It’s supposed to have a bottom to sleep on, not a top to keep her in.” And she was right. Instead of a crib for my firstborn child, I had built a Swedish cage.

Rachel says it’s my soon-to-be-daddy nerves. But each night when I put my ear to her stomach and listen to that little heartbeat, I feel this stillness come over me. And I like to think it’s calm, but maybe it is dread.

All I know is…she’s almost here. Almost.

When expecting parent, Nick, experiences the unexpected—the unimaginable—he learns that life isn’t about putting the pieces together perfectly, it’s about learning how to pick the pieces up after everything shatters. The Art of Assembly by Jonas Taylor

Nick. I am getting used to the never-ending trips to Target. I almost have the aisles memorized. I can tell you off the top of my head the exact location of all of Rachel’s snacks, the shortest route from the front door to the baby section, and that checkout lanes 3, 6, and 7 are all susceptible to computer problems. I think I am even starting recognize my favorite cart on sight.

And it astonishes me how much stuff we apparently need to care for a tiny human. There are carriers and seats, blankeys and binkys, and let me be clear: I have never been a prude, but buying the creams, wipes, and breast accessories has been a real test of my manhood. I asked Rachel how our ancestors did it without American Express. She says they fashioned shopping carts out of tortoise shells and hunted wild beasts to make blankets from pelts and binkys from the knuckle bones! And thus, the original Target was born! Well...we thought we were funny.

It just feels like more because we’re doing most of the shopping at the last minute.

See, we didn’t want to buy the baby stuff too soon because, well…we’ve had a lot of trouble getting pregnant. At first we thought it was Rachel, and then we thought it was me, and then we thought it was God, and I’d ask, “What did I do to you?” You know? But it wasn’t punishment, it just took patience. And even if it took a little longer than expected, she’s almost here. So now I’m at Target all the time.

We picked out a name. I’m not supposed to tell anyone what it is, but it’s Stella. I know, I know. It’s bad luck. But isn’t that just the prettiest name you’ve ever heard? Stella. Steeeeellllllaaaaaa.

Yep, that’s my girl.

I’m home! Hello lovely baby oven, and hello little tiny bun.

(He begins to sing horribly.) “Well, I guess, you’d say, what can make me feel this way? My girl. My girl. Talking ‘bout my girl.” Hey, I think she likes it! She’s kicking up a storm in there.

(Rachel tells him to get back to work.) Okay, okay. Back to the crib. Back to her crib.

Do you want to see a picture? That’s what everybody says when I ask that question: big sigh and then a “sure.” And I know that before they are born, it’s just a black and white x-ray of my wife’s stomach. But she’s beautiful, especially for a blob. We just got this one last week; it’s that kind of bumpy MRI image. And you can totally see a facial expression. The first time I saw it, I said “I know that facial expression! I’ve been married to that facial expression for seven years!” It’s the look that says I’ve got a secret.

Well, I can’t wait to find out what that secret is. My Stella.

TRANSITION

Morning, Rach. Before you start, I was up half the night, and the crib is done. It’s done. I need to run a few more tests to make sure it’s stable, but…what’s wrong?

Weird? How? Like, do you think she’s turning? The doctor said she was gonna start getting ready to drop soon...it could be. Not moving, at all? Well...honey, I’m sure she’s just sleeping. Okay, okay. Calm down. Let me have a listen. (He kneels and listens to the stomach. He hears nothing. Panic starts to build.)

Nothing. I hear nothing. Okay, here’s what we’re going to do. We’re gonna get in the car and go to the hospital. We are not gonna panic; we’re not gonna call anyone. We’re just gonna get in the car, go in, and get checked out. Just to be sure, okay? Just to be sure.

TRANSITION

(on the phone) No. Don’t, mom. There’s nothing you can do. Nothing we can do. So, I’ll pick you and Dad up at the airport tomorrow? Good. Yeah. Me, too. I’m sorry, too. Bye. (hangs up)

See, we got there, and they were great. They got us right in and got the sonogram and the heart monitor all set up. All the beeping, we thought it was a good thing. I even made a joke like, “Is all that beeping because she’s swearing at us? Like, why the beep did you beeping beeps wake me up? I was beeping sleeping?” But...no one laughed.

That’s when I knew something was wrong. Something horrible.

See, they…they couldn’t find a heartbeat. The beeping meant that she wasn’t...wasn’t alive anymore. Stella. She’s just gone.

We couldn’t believe it.

I mean, this photo…this was last week! She was…

It’s rare, they said, with no indication, to just lose a fetus so late. And I wanted to tell them off. You know, tell them we didn’t lose her, and that she’s not a fetus, she’s Stella. But the words got closed up in my throat.

But, Rachel started screaming. She couldn’t stop screaming. They had to sedate her. She’s at the hospital still until tomorrow. When they will have to induce labor. And then, Rachel is going to have push and struggle and bring our first child into the world. But instead of bringing her home, we’ll bury her.

And it would be one thing if we’d lost her at six, eight, thirteen weeks in. But after all this... tomorrow. This is wrong. It’s so…so wrong. She was supposed to come home. The mobile, the wallpaper, that freaking crib. She was supposed to have all of this. And we were supposed to have her.

What did I do to you?

What did she do to you?

She was almost here. Almost.

She was so beautiful. My girl. I just hope you know how much we loved you. I think you did. My Stella.

I’m going to keep this, I think. Nothing else. Not the Target stuff or the crib…which I think we can all agree is probably for the best.

I am going to keep you, right here.

Well, I’d better go back to the hospital. For Rachel. For me. To figure out what comes next.
```

---

## IC-1487: The Body Politic

- Title: The Body Politic
- Author (byline): CJ Harvey
- Work: The Body Politic
- Publisher: SpeechGeek
- Publication date as stated: 2018
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1428
- Already set (do not supply): none

### Source block (context only)

```text
The Body Politic by CJ Harvey
ISBN: 978-1-61387-200-0
Copyright 2018 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2018, is identical to the printed published
version of this same publication dated 2018. This statement along with the entire printed
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
Authors Note: The goal of this performance is to explore issues of gender identity and public identity. Therefore, while this script is written from a female perspective, the performer may be of any gender. To that effect, if the performer wishes, the pronouns in the performance (male, female, he, she, wife, husband, etc.) may be altered in order to reflect the performers’ preference.

GOVERNOR. (Enters limping slightly, sore and exhausted. Speaks on the phone.) No, I have no comment for them. Well, you can tell them that I am looking forward to getting back to work for my constituents.

Yes, you can tell them the president called.

No, you don’t tell them I didn’t accept the call. Talk about adding insult to injury.

Did the ACLU call back yet?

Dammit. Okay. Well, let me know. Thank you. (hangs up the phone)

You know, they never tell you how much it hurts. I mean, obviously, when you get shot it hurts. But the thing is, when it happened, I didn’t really feel it.

There was so much screaming, and I was knocked about every which way. I mean, I heard the shot, but I didn’t feel anything. When my assistant, Daniel, tackled me to the ground—that hurt. So much so that when he asked me, “Governor Jones, are you okay?” I told him off. I said, “I was fine until you crushed me to death.”

And then we saw the blood. But even then, that wasn’t when it hurt. It hurt when I woke up in the hospital after surgery.

It hurt when I tried to laugh at my own terrible joke about my cat-like reflexes failing me. Even now two weeks later, it hurts even though they tell me I’m out of danger.

Obviously…doctor’s don’t read newspapers.

My danger has just begun.

In April 2015, 20.7 million viewers tuned in to 20/20 to watch Bruce Jenner publicly confirm that she was transgender. Since then, the visibility for transgender Americans has grown exponentially. In fact, nine transgender individuals were elected to public office in 2017.

However, such progress was not an overnight phenomenon. In fact, for the better part of the 20th century, transgender individuals have been cast aside as anomalies, mental cases, and even perverts. And unfortunately, the media still treats such stories of personal reclamation and liberation as a sideshow. In her drama, CJ Harvey explores the difference between public approval and personal acceptance, recognizing that the road to progress is often paved with the tears of pioneers.

GOVERNOR. I really don’t pretend to know what comes next.

I gave you this interview, because yours in the only newspaper that seems to think that I am still a victim in this.

You’re going to have to listen to me on this because I don’t have the energy to tell you this multiple times. This whole thing has become such a twisted mess. I don’t necessarily feel the need to defend myself but some have insinuated that all of this started because somewhere along the line I decided I didn’t need to be truthful.

So let me be clear: I didn’t decide anything. Some man decided to shoot me for reasons unknown. Some nurse or an intern decided that the world had a right to know my personal medical history. And the press decided that I… look, I am fine with being labeled a freak…an…an abomination, or whatever language you’d like to use. But I was never a liar.

But, just to…confirm…what every newspaper in the country is obsessed with reporting: yes, I was born a male, biologically.

And I say biologically, because to me, that’s an important distinction. I mean, people change their biological form all the time. You might have been born a blonde or a redhead and desired to change that. You might have been born with genes that lent themselves to be overweight, but you worked hard to claim the life—the identity—that you wanted for yourself. And no one is standing outside your house with hateful signs that say you “defied God.”

I was born a male, but I have always been a woman. And my husband and I have had many, many conversations about the differences between male and female, man and woman. We say a woman is someone who owns her femininity, someone who identifies psychologically, culturally, and spiritually as part of a sisterhood of women. Someone who sees other women and thinks “That’s what I am.”

It was around four years old that I started noticing that I didn’t quite…fit…in my own skin. My parents were always correcting me. “No, sweetie. Y=You’re a boy,” or “Say he.”

The only day I truly felt comfortable was Halloween. And no, I didn’t dress up as a girl.

I was Superman.

Every year.

Because I understood what it was like to walk through the world like an alien, you know? And all I wanted was to disappear into a phone booth and emerge a completely different person. My true self.

I wasn’t Sam. I was Samantha, and I was lucky to figure it out very early in my life. And when I told my parents, they were incredibly kind. They were proud to have a child who knew her own mind.

It doesn’t matter when I physically transitioned. Do you hear me? It doesn’t. What matters is when I embraced who I was. It was the same year I decided I wanted to go into public service, to be a different kind of Superman—you know, truth, justice and The American Way.

It was the same year I met the love of my life. And when I told him my story, do you know what he said to me? “Samantha, you are the most courageous person I know. Not for what you’ve been through. That’s only part of the story.”

In the hospital, the look on my husband’s face when I woke up… He was so relieved and so, so sad—like he knew it was going to be far worse for me to wake up than to just slip away.

Maybe I should have.

But that’s not who I am. Yes, to call me transgender is accurate, but that’s only part of the story.

The rest of the story could have been that I got married in a church, I ran for city council, I worked my way up to chairman. I instituted changes that helped students from all over my city get a better education, I helped public transportation improve so seniors could access health care. I ran for Governor on a positive, issue-based platform, and I won. I work tirelessly to make the world better, and maybe that sounds cheesy, but what the hell? It’s what I believe in and that’s what people should care about.

What I value.

What I fight for.

But no.

The only story people care about is the front of these damned newspapers!

“The Scandal in the Governor’s Mansion”

“How Far Did the Cover-Up Go?”

“Is the Governor’s Husband Gay?”

Now I am finished. I won’t resign, but I’ll never be re-elected. The world we live in remembers headlines not articles of the Constitution. And I could sue. I would absolutely have grounds for slander and libel and all of it—but, on some level, wouldn’t it be worse for them to be able to paint me as some self-loathing transphobic nobody, instead of the governor? The governor who almost dodged one bullet, but couldn’t escape another. Truth, justice, and The American Way, right?

I want to tell people that I think it’s sick. I think it’s sick that the focus here is not on gun violence, it’s not on mental health issues, it’s not even on the fact that public debate has devolved so far in this country that a citizen whom I would have gladly listened to, felt the need to…to…

For God’s sake, I almost died!

And the only thing people care about is what is between my legs!

I am so, so tired of apologizing for making myself into the person I already was.

You wonder why I never felt the need to tell people?

I gave you this interview because you’re the only one who wants to talk about the shooting. Ironic that it’s the only thing I haven’t talked about. But that’s the thing about truth: it comes out whether you want it to or not.

I just wanted someone to know me. Not for myself but for all of us. For the men and women I am so proud to serve.
```

---

## IC-1488: The Boyhood Adventures of Clark Kent: Episode One

- Title: The Boyhood Adventures of Clark Kent: Episode One
- Author (byline): Anthony Doyle
- Work: The Boyhood Adventures of Clark Kent: Episode One
- Publisher: SpeechGeek
- Publication date as stated: 2013
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 869
- Already set (do not supply): none

### Source block (context only)

```text
The Boyhood Adventures of Clark Kent: Episode One by
Anthony Doyle
ISBN: 978-1-61387-043-3
Copyright 2013 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2013, is identical to the printed published
version of this same publication dated 2013. This statement along with the entire printed PDF of
this publication must be presented at any National Forensic League District or National event for
the script to comply with NFL rules per the request of the Executive Director.
This and other selections of quality performance literature for competitive oral interpretation
are published by SpeechGeek.
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
NARRATOR. When it comes to American stories, most of the really

good ones take place in Kansas. This is how we know

they’re fictional, because nothing really good actually

happens in Kansas. This story starts in Kansas in 1952,

when an honest and hardworking farmer named Jonathan

Kent heard an explosion one morning. Jonathan and his

wife Martha wandered out into the middle of the field and

found an enormous crater.
JONATHAN. Holy hole!
MARTHA. Oh, Jonathan! Look!
NARRATOR. Inside the crater there was a strange metal sphere.
JONATHAN. Oh god, it’s that Sputnik devil sent by the Commies!

Martha! Get the bible! NARRATOR. But when Martha approached she noticed something. It

wasn’t a Soviet satellite. It was a little space ship and

inside was… MARTHA. A baby! Oh Jonathan! It’s a baby, just for us! JONATHAN. What kind of Commie stork delivers Commie babies in

space ships? NARRATOR. But in spite of Jonathan’s reservations he and Martha

adopted the baby and named him.
MARTHA. How about Allen?
JONATHAN. It sounds too much like alien.
MARTHA. Rich?
JONATHAN. Let’s not be ironical, Martha.
MARTHA. How about Clark?
JONATHAN. Clark Kent. That sounds downright American.
MARTHA. Little Clark Kent, my son.
NARRATOR. As the three settled into their quiet Kansas life together,

Jonathan and Martha soon realized their child wasn’t like

other children.
JONATHAN. See here, Clark. This is a hammer.
CLARK. (CLARK sneezes and rips it in half.)
JONATHAN. Oh my.
NARRATOR. With the help of Jonathan, Clark soon found that he had

extreme strength and speed. He had the ability to fly. And

they even discovered that Clark was bullet proof, a

discovery that got Jonathan in a lot of trouble with Martha.

But one day, while Clark was plowing the field with just his

fingers, he told his Dad what he wanted more than

anything else.
CLARK. Dad, I want to be a boy scout.
JONATHAN. Why’s that son?
CLARK. They get badges on their chest for doing good things. I

want that too.

JONATHAN. That the only reason? CLARK. Chicks dig badges. JONATHAN. An American answer! Nice! (They high five each other.) AH!

(JONATHAN recoils in pain.) NARRATOR. Well, after Jonathan returned from the hospital, he told

Martha all about Clark and the boy scouts. JONATHAN. (arm in a sling) Isn’t it wonderful, Martha? MARTHA. Clark, sweetie, are you sure you want to do this? It’s not

going to be easy.
CLARK. I’m sure.
NARRATOR. So off he went to boy scout camp.
SCOUT LEADER. Welcome to The Kansas Boy Scouts of America Cam, or as

we like to call it, KaB SAC. This is where boys go to

become scouts. So the question is: Are you ready? CLARK. (enthusiastic) YES! SCOUT LEADER. Oh sorry, that was a rhetorical question. But I like your

spirit, scout. What’s your name? CLARK. Clark Kent. SCOUT LEADER. That sounds downright American! Well, I suppose you’d

better meet your fellow scouts. Sound off!
TWITCH. Twitchy!
SLOBBER. (gargling and lisping sounds)
CHUBS. Chubs!
BUG EYES. I’m Bug Eyes!
NARRATOR. The other boys looked like Clark, well, except for Bug

Eyes. He looked like a bug. No matter how he tried, Clark

just couldn’t seem to fit in with them.
TWITCH. Clark! Wanna arm wrestle?
CLARK. Sure! (accidentally rips off boy’s arm) Oops.
TWITCH. (screams) Ah!
NARRATOR. No one invited Clark to arm wrestling after that. In fact, no

one invited Clark to do anything. That wasn’t so bad. Soon

it came time to test for badges. Clark was excited.
CLARK. So excited!
NARRATOR. First up is the fire badge test.
SCOUT LEADER. For the fire badge, rub your two sticks together to make

fire. CLARK. (CLARK rubs the sticks together unsuccessfully. Then he

uses his heat vision to light the fire.) Done!
NARRATOR. The other boy scouts were upset.
SLOBBER. (SLOBBER gargles and lisps while pointing at CLARK.)
SCOUT LEADER. What?
SLOBBER. (SLOBBER continues to gargle and lisp, then re-enacts

CLARK lighting the fire with his eyes.)

SCOUT LEADER. Um, right. Anyway, Clark, you didn’t do it right, so no

badge for you.
CLARK. Darn.
NARRATOR. Clark tried again with the metal working badge.
CLARK. (bends it with his fingers) Done!
NARRATOR. The other boy scouts were mad.
TWITCH. Scout Leader!
SCOUT LEADER. Settle down, it must not be real metal (hits it, it hurts) Ow!
NARRATOR. Once again, Clark had failed.
CLARK. Darn it.
NARRATOR. Finally, it was time for the archery badge test.
CLARK. (releases the arrow) Oops, that’s going to miss, hang on.

(runs and catches the arrow) I’ll try again.
NARRATOR. The other boy scouts were furious.
BUG EYES. You’re cheating!
CLARK. Cheating? How?
BUG EYES. You’re a freak.
NARRATOR. With that, they sent Clark home without any badges.

When Clark got home he told his parents what happened. JONATHAN. Cheating?! It’s not your fault you have Commie

superpowers!
CLARK. I didn’t mean to do it wrong.
MARTHA. You didn’t do it wrong, sweetheart. Just different.
CLARK. Well, I guess different doesn’t get you badges.
NARRATOR. The next morning when Clark came downstairs to

breakfast, Martha was waiting. MARTHA. Clark, the world can be a hard place for people who do

things differently. I’m proud of you for being who you are.

And you did earn a very special badge. CLARK. I did? MARTHA. You earned this badge. I made it for you, for being

different.
CLARK. Does the “S” stand for special?
MARTHA. I think the “S” stands for super.
LOIS. Hey Clark
CLARK. Hey Lois
LOIS. Nice badge.
JONATHAN. Nice! (He gives CLARK a high five with his other hand.) AH!

(recoils in pain) NARRATOR. Clark would grow up and face many challenge for being

different. He always wore that badge to remind himself

and others that sometimes being different isn’t just good,

it’s super.
```

---

## IC-1489: The Fortunate

- Title: The Fortunate
- Author (byline): Alexandra Rojhan
- Work: The Fortunate
- Publisher: SpeechGeek
- Publication date as stated: 2017
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1402
- Already set (do not supply): none

### Source block (context only)

```text
The Fortunate by Alexandra Rojhan
ISBN: 978-1-61387-301-4
Copyright 2017 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2017, is identical to the printed published
version of this same publication dated 2017. This statement, along with the entire printed
PDF of this publication, must be presented at any National Speech and Debate Association
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
LEO. You looking for the office? It’s that way. They told me all the press have to go to the office. This is the gym. No office here. Except coach’s, and it’s eleven thirty so he’s at lunch. I’m not supposed to talk to the press. Except to tell them where the office is.

It’s that way.

My name? Leo. Like the lion in the sky. I didn’t know about the lion in the sky until Arlan told me about it. I maybe knew about it before, but I didn’t remember. But now I got this book, see? It tells me my fortune for the day cuz I’m a Leo. When is your birthday? Okay, let me see.

I haven’t been too good at remembering since my accident. That’s what I’m supposed to call it. Sounds better than I crashed a car and my brain got hurt.

When is your birthday? Ok, let me look. See I got this book that tells you your fortune for the day. And every day Arlan would stop by my office and say, “What’s our day look like?”

Yeah, I knew him. And I was here for the, what did you call it? The tragedy. I don’t like it when people use words that mean other words. It’s confusing. Cuz maybe the tragedy you mean isn’t the tragedy I mean, you know? Like what if you think the part that’s sad is the end of the story and I think the sad part is the beginning? That’s…confusing.

But I’m not supposed to talk about that. But I could tell you about Arlan, if you want.

Often times, in the wake of tragedy, our cultural focus centers on identifying who is the victim and who is the villain. However, for Leo, a janitor with special needs, the labels of victim and villain often blur together as he copes with a recent tragedy. As a result, he forces us to reconsider who we call a victim and what we learn from villains. The Fortunate by Alexandra Rojhan.

LEO. Met him in a dumpster. I’m telling the truth, I swear. I take the trash from the admin out at 12:30 and the trash from the classrooms out at 4. And one day, at 12:30 I open the dumpster and almost threw a bag of old coffee filters on his head.

I said, “Student’s not supposed to be in the dumpsters.”

He said he, uh, fell in looking at something. So I started looking too. And he said he was joking, so I said, “HA!”

I’m not very good at jokes.

His name was Arlan. After a dead grandpa. I told him my name was Leo, and he said like the lion. I didn’t understand, so he told me that Leo was a lion in the sky. See, he was so strong that warriors' clubs, swords, and spears couldn’t hurt him. It took a god called Hercules to kill him. And I asked why he killed him, and he said back then lions didn’t mean as much as gods. But now, people all over the world look up to that lion every night. So he got his respect after all. I didn’t know stars could tell stories like that, but he said that’s their whole job.

Then the next day he gave me a book from the stars. It’s called a daily horoscope. He wrote me a note, see? It says, “Thanks for helping me.” And this book is real convenient for me, cuz it works, too. See I met him on April 4th, and it said “Today a very special friendship will surprise you,” and I think nothing’s more surprising than a friend who fell in a dumpster.

Except, he told me he didn’t fall in. The other boys, the big ones in the football t-shirts put him in there. He said they did that stuff a lot. And so I said you should stay away from them. He could come have lunch with me.

See, back behind the bleachers, there’s a ladder that goes all the way up to the roof of the gym. I got a couple folding chairs up there and it’s the best view cuz you can see the courtyard and the football fields and the parking lot.

After that, he’d come up and we’d have lunch. It was nice for both of us; having a place to go to. I even gave him a sticker I found at the grocery store of a lion. I gave it to him and said it was a good luck sticker and it’d make things better. But, you know, good luck can’t make everything better.

Arlan would come see me sometimes with broken glasses or a cut lip—he didn’t lie to me about it. He knew that wasn’t nice to do to me because I get confused real easy, so he told me that them boys kept on him. So I went to my principal and I said that those boys were being cruel, and he said that he would handle it and I thought he would. But then…

Last week, I got a call on my walkie talkie, said there was vandalism on the third floor. The word “Faggot” in bright ugly spray paint…right over the top of a sticker of a lion.

I tried. I tried so hard to get that paint cleaned off as fast as I could, but the bell sounded and the hallway filled up and I looked up and saw him. I wanted to tell him that it would be okay, that he gets a new fortune tomorrow, you know. But he ran away so fast.

The next day, he surprised me in the morning with a visit and I didn’t even wait for him to ask. I had my book out and I said, “Today your decisions will change the rest of your life.”

I thought that sounded good, but he was real quiet about that. He said something then…but I don’t remember what it was. And then he left for class and I went back to work.

It was 12:30. I take the trash from the admin out at 12:30 and the trash from the classrooms out at 4. I thought the seniors were doing firecrackers again in the parking lot because sometimes they like to do that. But then I heard screaming, and I knew something was wrong. All I could think was that Arlan might be in trouble so I ran to the third floor…to his locker…he wasn’t there just the rest of that paint and a lot of screaming kids and one girl said, “The gym. He's on the roof of the gym.”

I don’t remember what I thought. I don’t know if I knew it was Arlan then, or if it was before then. But I just remember I had to get to the roof.

He stopped shooting when he saw me. He had a handgun like in the movies. And I thought maybe it was a movie. Maybe my brain got hurt again because Arlan wouldn’t be holding a gun and shooting off the roof at people. I was trying to decide if this was a joke or a movie or something and then Arlan said, “Today your decisions will change the rest of your life. I’m so sorry.”

I wanted to tell him that I wasn’t mad at him. I wanted to tell him that he's gonna be okay and that we get a whole new fortune tomorrow. But then he took that handgun and put it in his mouth and... no, no, NO!

Arlan. He was my friend.

And now I hear what you say about him on TV. He wasn’t no monster. They were. The ones who hurt him. I’m sorry those kids got hurt and I’m sorry that they didn’t like Arlan, but if you want to know what happened...if you want to know what I think the tragedy was? They killed him. They killed him first.

So, you should just know that part, too.

Oh, before you go, when is your birthday? Oh. You’re a too? Well, for us it says…”You are damaged and broken and unhinged. But so are shooting stars and comets. You will be bright even in your imperfection.” Don’t thank me. Thank Arlan.
```

---

## IC-1490: The Mortality of Trumpets

- Title: The Mortality of Trumpets
- Author (byline): Gregg Moeller
- Work: The Mortality of Trumpets
- Publisher: SpeechGeek
- Publication date as stated: 2015
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, SCENE
- Teaser before the introduction: No
- Spoken words (computed): 1705
- Already set (do not supply): none

### Source block (context only)

```text
The Mortality of Trumpets by Gregg Moeller
ISBN: 978-1-61387-089-1
Copyright 2015 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2015, is identical to the printed published
version of this same publication dated 2015. This statement along with the entire printed
PDF of this publication must be presented at any National Speech and Debate Association
District or National event for the script to comply with NFL rules per the request of the
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
CHARACTERS: Marvin Reynolds, age twenty-seven

Angel of Death, age unknown

SCENE: Hospital bed

MARVIN lies on bed, eyes closed…ANGEL hovers over the bed, as he chants last rites

DEATH. (makes sign of the Cross) …in nomine Patris, Et Filie, et

Spiritus sancti…Amen.

ANGEL checks out the situation, then gamely and clumsily tries to pic up MARVIN from the bed, as MARVIN wakes

MARVIN. groggily Wha…what are you doing? DEATH. (struggling with weight) Isn’t it obvious? MARVIN. I don’t care what is obvious…just what the HELL are

you doing? DEATH. (still struggling) I…am….trying…to…take your

immortal soul to heaven…if you don’t mind… MARVIN. My…what? DEATH. (now REALLY struggling) Your soul…spirit…your life-

force…your immortal animated essense manifested

with the Judeo-Christian ethic…(ANGEL drops

MARVIN back on the bed—barely) Geez, couldn’t you

skip a meal once in a while? If I wasn’t Death, I’d have

an aneurism by now. MARVIN. (fighting) Let me go—leave me alone, you lunatic!

Help, police! Anybody! DEATH. No one can hear you… MARVIN. Some crazy pervert’s trying to abduct me…oh, my

GOD! Rape! RAPE! DEATH. Will you SHUT UP> No one can hear you….and don’t

flatter yourself. You ain’t no prize. MARVIN. Who are you—stay away! I’ll bite…(does so, rather

pathetically to the air) DEATH. I’m Death, okay? Now, let’s go…you’re dead, and

we’re late enough as it is… (glance at hand, winces)

Now, LOOK at what you did—that fingernail will take

an eternity to leah. MARVIN. (in disbelief) Dead?

DEATH. And look at my suit…these wrinkles will never come

out. OH! And the seam… MARVIN. Dead?

DEATH. …they’ll never loan me another suit again, at this rate. MARVIN. Dead? DEATH. …especially after this. I’ll have to go back to burlap—

and that chafes me so… MARVIN. Dead? DEAD? DEATH. (aggravated) Yes…dead. Deceased, shuffled off your

mortal coil, defunct, singing with Elvis, gone to eternal

slumber, bereft of life—in short, worm food. MARVIN. (grabs ANGEL, screams) DEAD? How can I be dead? DEATH. Hold on—I think you dislocated my shoulder. MARVIN. How…could…I…be…dead? DEATH. Okay, so maybe I lied. A little. You’re not dead—yet.

But close.

A long, painful pause—then…

MARVIN. HELP!! Lunatic!!

DEATH. (wearily, as MARVIN continues screaming) Please…no

one can hear you. Please, stop this…c’mon…All right

then…

DEATH takes his index finger and places it under MARVIN’s chin and raise him up as if the finger is the sole support of MARVIN’s weight—MARVIN reacts with a horrified look and immediately shuts up and is powerless…

DEATH. (in an unspeakably EVIL voice) HEED MY WARNINGS

OR FEAR MY WRATH, WRETCHED INSECT!

DEATH pulls back finger and MARVIN drops to the floor

MARVIN. (now nervous and scared) Wow…that was pretty

impressive…Sir. DEATH. You think so? I did some theater in school. Watch

this—

(done in a bad Cockney accent) Oh, Mister Higgins, I

don’t want no gold and no diamonds—I’m a good girl,

I am…
MARVIN. How….
DEATH. (continues) The rain in Spain lays mainly in the—
MARVIN. HOW can I be…
DEATH. Dead?
MARVIN. And then not be…
DEATH. Dead? Simple. (ANGEL takes him gently aside as they

talk)

Your soul is “in transition”. It’s simple. Your core

unit—that’s what we call your body—is about to cease

operation—die. Therefore, your soul must prepare for

the transition to eternity, or heaven, as you know it.
MARVIN. So, I’m not dead…yet?
DEATH. Well, no…
MARVIN. So, go away.
DEATH. Uh, it’s not that simple…
MARVIN. If I’m not dead, I don’t want to go.
DEATH. You don’t understand…
MARVIN. Simple algebra—Not Dead Equals Alive, so by all

equations I— DEATH. (grabs MARVIN) You want proof? Fine.

ANGEL pulls MARVIN around back of the bed, and grabs his head and forces him to look at “himself”

DEATH. There you are—dying, with tubes and wires and

catheters…LOOK!
MARVIN. (numb) H…h…how?
DEATH. Blood clot—went straight to the brain.
MARVIN. No…no…no…I’m so….
DEATH. You let me no choice. Now, let’s go…I hate the smell

of these places. All that Lysol. MARVIN. But...I…I just want…. DEATH. I just hope you followed that old Mom Rule about

having on clean underwear at all times…

ANGEL tries to peek under the sheets, as MARVIN pulls back cover MARVIN. I was in a hurry, all right? What kind of “angel of

death” are you, anyway? DEATH. It’s the outfit, isn’t it? My voice…what? MARVIN. Well, you just don’t “scare” me. Isn’t death supposed

to be bony, and dressed in black and…well, scary? DEATH. You mean, like in the movies? C’mon, now…really. MARVIN. No, really. I always pictured death that way. DEATH. All right…have it your way.

ANGEL jumps on the bed, gesturing wildly with snarling evil voice and other bad sound effects attempts

DEATH. I AM DEATH….FEAR ME, PUNY MOR-TAL! MARVIN. (cowering) AAAUGH! No! Not DEATH! PLEASE…no,

that won’t work…I know it’s you. DEATH. Maybe you need something different—how about…

ANGEL jumps about wildly, making honking noises and giggling incoherently

DEATH. HI, THERE! I’m PERCY, THE DEATH CLOWN! Huh-

HA! Honk! Honk! I’m here to escort your soul to

Heaven! Ha-ha-HA! MARVIN. (unimpressed) Percy. The death clown. DEATH. Honk! (now desperate) C’mon…work with me on

this…wait—I know!

ANGEL circles the table, then crosses over to MARVIN seductively and vampishly, oozing female sensuality

DEATH. Well, hello there, Big Boy. Don’t you want to take an

eentsy-weentsy little trip with…moi? MARVIN. (aroused) Oh…baby, I…no-no-NO! I still know its

YOU in there! DEATH. (still vamping) Sorry…er, I mean, sorry. I’m trying my

best… MARVIN. Don’t you know how to DO this? DEATH. Actually…I’m filling in for a friend. I’m usually in

charge of a vital Heavenly duty on my regular tours.

Really important. Yep. MARVIN. Which is…?

DEATH. (meekly) I handle prayers from amateur bowlers

trying to nail seven-ten splits.
MARVIN. Well, I’m not going. With you.
DEATH. Aw, c’mon…help me out here.
MARVIN. (angry) Leave me alone!

MARVIN returns to “his” bedside

MARVIN. Dead…I didn’t feel anything… DEATH. Well, you aren’t dead, technically. You are actually

pretty lucky, for being in an irreversible coma and

everything… MARVIN. (outraged) Lucky? Me, LUCKY? I’m dying, I get Earl

Anthony’s guardian angel, and…I got no trumpets. DEATH. Pardon? MARVIN. Death is supposed to be a grand, majestic show, with

bright lights, heavenly choirs, the pealing of bells,

and long-dead family members calling me

forward….and trumpets. Trumpets shaking the earth

with their cries, welcoming me to Paradise.. DEATH. I can play the spoons pretty good, if that will— MARVIN. My life stunk enough—now my death has to be just as

bad?
DEATH. Sorry…
MARVIN. That takes it. No trumpets, no me. I’m not going.
DEATH. You got to.
MARVIN. (with increasing self-delusion) I’ll heal up. They’ll

operate. DEATH. The damage was too great. MARVIN. Someone will create a cure while I’m—

sleeping…yeah, sleeping… DEATH. You’re not listening… MARVIN. And when I wake up, I’ll laugh and tell everyone about

you, and then I’ll get up,and get married to a nice gal

and own my own house… DEATH. You’re on life support… MARVIN. (faltering) And then I’ll go to parties and see my

children play football and…and….I’ll… DEATH. (grabs him, and confronts him) You’re DYING! Can’t

you see that? The longer you hold onto life, the less

it’ll be worth!

MARVIN. (near tears) I’ll go to church more…I’ll— DEATH. You can’t turn back! MARVIN. (breaks free from ANGEL, with great emotion) I CAN’T

DIE! Not like this…a blood clot?

(MARVIN collapses at “his” bedside, sobbing loudly)

MARVIN. Why couldn’t it be something cool… DEATH. Cool? MARVIN. You know—a “movie death”…me gasping for

air….cool. DEATH. I don’t follow. MARVIN. C’mon…where I grab my chest… (and he does so,

very overdramatically) stagger around the room…

(again, does so with a bit too much elan) maybe a had

gesture or two, coupled with a look of painful

realization… (does same) a brief final word for my

beloved ones to treasure: “Omlet, du Fromage!” and I

drop lifelessly to the floor…(drops) Look—rigor

mortis! (stiffens a bit too realistically) DEATH. You’re sick. You want to see “real” death? Here—sit.

DEATH moves a chair stage center, and MARVIN sits. DEATH proceeds to run a “slide show” of death scenes towards the audience, as of the screen is right in front of them, and makes clicking noises while operating a projector controller, as if he running a slide projector

MARVIN. (following ANGEL’s first click, grimacing at the horrible

“images” on the “screen”) Ugh…. (second click)

Yeech… (third click—reacts with horror) Ewww…the

whole trombone?

DEATH stops slide show, puts away ‘screen’

MARVIN. I just want my death to be memorable….like Fonzie’s. DEATH. Fonzie didn’t die. He WAS in a coma once, after he

met Pinky Tuscadero. MARVIN. No, no…Richie was in the coma, after he---oh, my

God, here I am, arguing trivia with Beer Frame and I

AM DYING!

DEATH. Listen…listen to me. I understand that you don’t want

to die. All I want you to do is accept it. You will gain

nothing by fighting for a life not fit to live. Image

means nothing now. Death is not a contest! MARVIN. (frustrated and angry) But…but…why like this? No

drama…no final words. All alone. All this time and

effort for living and what does it get me? Not even

trumpets…is that all I’m worth to you, God? Silence?

That’s all?

MARVIN begins weeping, with head in hands. DEATH watches MARVIN with sympathy, then looks up and silently coaxes God, with barely audible easily visible please, of “Come on”, and “Just once, for him” and “please”, etc.

Then, slowly but excitedly, MARVIN is distracted by something detectable only to him—the sound of trumpets.

MARVIN. (silently, but building with excitement)

Trumpets…trumpets...do you hear them?

As MARVIN reacts to the ‘trumpets’, DEATH mimes a grateful “thank you” heavenward, as well as a wink and an “OK” sign

DEATH. Yes, I do…Beautiful, aren’t they?

DEATH slowly begins to lead a faltering MARVIN back to his bed, as he is now dying

MARVIN. Trumpets…feel the floor move, man! Wow…

(weakens) Oh, my…
DEATH. Just relax, and let the trumpets call you.
MARVIN. Wow…trumpets…I’m cold—I’m so cold…what’s—
DEATH. (calms and soothes him) Just focus—focus on your

trumpets.

MARVIN. (with labored breathing and increased spasms of pain,

as he is indeed dying) What—what’s happ…(MARVIN,

in his agony, looks at DEATH, and realizes he is indeed

dying—DEATH smiles, nod and comforts him)

Trumpets, man…aren’t they incredible? DEATH. Just for you. Special request.

MARVIN. Cool. DEATH. Relax, now….it will be over soon…it will take but a

moment, a twinkling of an eye… MARVIN. “…and the last trump, of the trumpets will sound…”

ANGEL gently sweeps his hand over MARVIN’s face, and MARVIN’s eyes close, and his breathing stops—he is at peace

DEATH. And we will be changed.
```

---

## IC-1491: The Pugilist

- Title: The Pugilist
- Author (byline): Michael Dean
- Work: The Pugilist
- Publisher: SpeechGeek
- Publication date as stated: 2018
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1594
- Already set (do not supply): none

### Source block (context only)

```text
The Pugilist by Michael Dean
ISBN: 978-1-61387-202-4
Copyright 2018 by SpeechGeek.
Free performance of this play for high school and intercollegiate competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2018, is identical to the printed published
version of this same publication dated 2018. This statement along with the entire printed
PDF of this publication must be presented at any National Speech and Debate Association
District or National event for the script to comply with NFL rules per the request of the
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
THE PUGILIST. Mac? I let myself in like old times. Key still under the mat… Hope that's, okay?

No one here? Good.

God, that smell: leather, canvas, sweat, and blood—like my own personal church. I'm outta shape. Suppose that's what I get. In my day, heavy bags used to run away from my hands. Sometimes I swear I'd even see 'em flinch before I hit it. Bam. Bam. Bam!

“If it don't hurt, you ain't trying hard enough.” That's what Mac'd say. ‘Cuz these heal (looks at his hands); this don't (points to his heart).

Maybe that’s why I’m here?

Maybe, I’m hoping it’ll hurt less if I can put my pain somewhere I’m used to? Maybe I’m hoping I’ll hear my dad or Mac coach me up off the canvas?

Maybe I’m just looking for one single thing that don’t remind me of her?

The American Association of Neurological Surgeons says that 90 percent of boxers sustain brain injuries. Some of which have lasting neurological consequences such as headaches, mood disorders, loss of coordination and and increased suicide risk. While the disease is technically called encephalopathy, according to former heavyweight boxer Roy Jones Jr., “The real disease is obsession. We don’t like getting hit, but we can’t stomach getting forgotten.” In his play, Michael Dean explores what happens after the bell rings. Suggesting that life is sometimes less about the punches we throw and more about the hits we take. In the end he shows us that when the lights go out, the real fight truly begins. The Pugilist by Michael Dean

THE PUGILIST. I ain't been in a ring in years. A lifetime.

I gave it up for Annie, and now it’s the only thing I got left.

A lot of ghosts in this place, I tell ya. A lot of skeletons, too.

I don’t know why I’m here, exactly. Just…well, this is where I grew up. It’s home. And sometimes you need to talk to the open space a little. Not like a crazy nut job or something, but just letting your words out of your head. First time dad brought me here, he sat in this corner—probably on this stool—and made me spar with my older brother. He caught hell for it later from my ma, making an eight-year-old spar with a fourteen-year-old. But the thing was, I won. I was slow, but I had big hands and dad knew I was gonna grow into ‘em, too. And I could take hits, man. You couldn't knock me down for nothin’.

Sure, I wasn't graceful. Dad said I moved like an elephant playing hopscotch, but that didn't matter. Movement only mattered if I didn't wanna get hit. I was never scared of getting hit. (his nose starts to bleed) Oh, crap.

Fricken nosebleeds.

Every other fricken day. It was one thing when I was getting hit all the time, but when I'm just sitting there? Nothing proud about blood that ain't earned.

I used to tell Annie it's ‘cuz of allergies.

No one ever heard of being dizzy ‘cuz of allergies, she'd say. And lately I see my hand shaking. But what do you expect, huh? I'm not the twenty-year-old bull she married anymore.

That guy…he was something. Training five hours a day, winning money left and right. I was on my way, boy. There ain’t a lot of people who can see themselves in the lights. Like truly. But I had the hands for it. I had the chin for it. I had the heart for it. I did.

Then…I met a girl. Ain’t that always the way?

Annie never liked me as a fighter. She wouldn't even go out with me at first. She said she didn't want to be with some...some brute.

And I never understood that. Maybe to her it looked like two animals in here, but it’s not. Good boxing is like, like poetry or something. It’s chess with fists. That’s why it’s called boxing not hitting. And when I would stand center ring and get my hand raised, I might be bloody, I might be tired, but I wasn’t thinking I just beat the hell outta someone. I was thinking. I proved I was stronger than my mind, that I could think my way around pain and exhaustion and some other guy’s fists. That’s not being dumb, I can tell ya that.

But you know, Annie wanted a nice guy. She said she wanted someone she could show off to her ma without black eyes and a bruised jaw.

So, I said okay. And the next day, I used some of my sister’s makeup on my face so you couldn't see the bruises, marched right over to Annie house, and knocked on the door. She answered and got ready to turn me down again, but instead, I asked to speak to her ma. Total head fake—said I wanted to introduce myself, said I was trying to win over her daughter, and wanted her to know I was a good guy. Even brought flowers.

Classy shit, right?

Yeah, Annie had no choice but to fall in love with me after that. And if you think boxing is hard, trying going twelve rounds about the laundry with that woman. I lost every time we went toe to toe. And I loved it.

But she never watched me fight. Said she couldn’t. Wouldn’t watch someone hurt me. And I told her not watching hurt me worse.

She was always on me to quit. Give it up. Give it up for her. Give it up for my health.

When I started getting the headaches and forgetting which house was ours, she’d had enough. Said she’d leave me if I didn’t leave it. So I gave it up. All of this. For her. I gave up who I was.

And for a guy ain’t nobody knocked down, I gotta tell ya…that winded me.

I started drinking. A lot. What was I supposed to do? I got a wife who can’t look at me, an empty house, and I got these two hands that feel heavier and heavier.

And then she starts in on me that I drink too much, that it’s making the headaches worse and my forgetting. Asks me to give that up, too. Said she wanted me to remember my own kids’ names. Turns out that wasn’t a problem.

We tried to get pregnant. Couldn’t. We tried to adopt. Couldn’t. We wanted to foster kids. Couldn’t. Nothing in the cards for Annie and me. Who would put kids in a house with a man who smashed skulls for a living? And I she never said it, but every time we fought, it was always there. Like a stink in the room— until one day we stopped fighting. Stopped talking altogether actually.

Then we’re at this party. And some pretty boy comes up and grabs her for a dance, right there, in front of everyone. I say, “That’s my wife.” The guy looks me up and down like he’s angling for something. I say do you even know who I am? And I hear someone say, “…who you used to be.” And I swear to god, I think it’s Annie. So I punched that guy so hard he was asleep before he hit the ground. And it felt good.

She said the booze changed me. It makes me mean. Angry. And I tell her ain’t nothing changed about me but what she changed. Of course it makes me mean, anger is all I got left. You go from training five hours a day and fighting two times a month to what? This nobody? This dumb ox working at the same factory my dad died in? Mowing the grass at the high school on the weekends. Yeah, some stuff’s gonna start to break down a little bit in here.

Then last night, in the car on the way home, she’s yelling at me.

I’m a bastard.

I’m a drunk.

I’m a brute.

And I tell her “No, I’m a fighter. And you can’t ask a fighter to not be a fighter. It don’t work that way!”

She’s telling me she doesn’t want to live like this anymore.

My nose starts bleeding, and I can’t see straight. I hear static in my ears, like, like the roar of a crowd after a hit. I see sparks and lights like flashbulbs, and it’s like I’m back there

I hear her shouting and I think, just for a second, she’s cheering me on when suddenly she screams, “Look out!”

And...they weren’t spotlights. They were headlights.

By the time I come to, we’re upside down and Annie…she’s bleeding everywhere.

And I’m holding her, and she looks so small.

She says she’s sorry, but I don’t wanna hear it.

I think about how she ain’t never wanna see me fight and I get it. She’s fighting and I can’t watch.

But she says she needs me to be stronger than that.

I tell her nothing—not a belt, not a bell, not a fist getting raised in the air—none of it ever felt as good as when she looked at me. Made me more than a fighter.

She died in the middle of a road. In my big heavy hands.

Then the whole universe stopped.

And I guess I could keep drinking, I guess I could go throw myself into some river. I wanted to. But instead I ended up here. Talking to no one.

‘Cuz these heal (holds up hands), this don't (points at heart).
```

---

## IC-1492: Until We Meet

- Title: Until We Meet
- Author (byline): Not specified
- Work: Until We Meet
- Publisher: SpeechGeek
- Publication date as stated: 2017
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1636
- Already set (do not supply): none

### Source block (context only)

```text
Until We Meet Again by Shane Cole
ISBN: 978-1-61387-115-7
Copyright 2017 by SpeechGeek.
Free performance of this script for high school and college level competitive forensics is permitted.
All other rights reserved.
This PDF version of this selection, e-published in 2017, is identical to the printed published version of this
same publication dated 2017. This statement along with the entire printed PDF of this publication must
be presented at any National Speech and Debate Association District or National event for the script to
comply with NSDA rules per the request of the Executive Director.
This and other selections of quality performance literature for competitive oral interpretation are
published by SpeechGeek.
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
(Dedicated to my loving grandfather, Marvin Maurice Scarbrough)

I knew this day was coming.
We all did, but that doesn’t make it any easier.
We knew you were sick.
We knew that the cancer was eating away your life,
But still, we held some glimmer of hope that this day would never come.
And yet still here we are and there you lie.

To many of us, grandparents are real treasures, teaching us, loving us, and becoming a strong thread in the story of our family legacy. Southern writer Shane Cole shares the coping process of the death of his mentor--his grandfather. He shows us that such a loss doesn’t magically go away, and that there is no timeline for how to grieve. He teaches us that a loved one can live on through stories, music, and memories--resulting in a loving tribute to a beautiful soul. "Until We Meet Again" by Shane Cole.

And I want to be sad. I am sad. I am. But you’ve found the land where cancer does not exist, And I can’t help but think that’s why there is a smirk on your lips.

Funerals shouldn’t be about sadness, but they are.
Anyone that tells you they aren’t are trying to fool you or they are fooled about it
themselves.
I look around at my family with tear-streaked eyes and sitting down from the exhaustion they
feel.
We all need a good meal and two days worth of sleep, but that won’t happen today, didn’t
happen yesterday, or the day before or the day before that.
We’ve spent days, weeks, and months trying to keep you alive, but we get just one day, one
hour, one minute to prepare for your death.
Yet you continue to smirk at me like I just don’t get it.
What is it that you have to say?
What is it that you wish to tell me from the grave?

Because I’m just numb now. That’s all I feel.
The numbness of too many emotions trying to take over at once.
People passing me with words like “I’m sorry”, “He’s in a better place”, and “if there is
anything that I can do, don’t hesitate to call”.

But I hear nothing. Nothing at all.
I just sit hear staring at the box built for one,
And I have to admit it’s the perfect one.
You would definitely approve. They didn’t pick out a girly box,
they picked one that makes a statement.
Just like you always did.
Never afraid to tell us what you thought,
and what you thought we should think.
I guess that’s how I got it honestly.

As the service ends, people gather around to say their goodbyes
I sit and nod while I look them in the eyes.
Emotion coming easily to them and hard for me.
I stare across the casket as the eyes of the grandchildren all meet with the same plan in
mind.

We set our task to work…so many flowers so little time.
Begin with the red roses on top of the coffin, the ones that signify love.
Each of us pulling one for ourselves and one for each family member.
When delivery is done we venture on to the ones donated by loved ones.
Roses of all colors, pink, peach, white, and orange even.
Add to those day lilies, carnations, blue bells, sunflowers, and lilies.
Beautiful colors all rolled into one large bouquet to give to our grandmother.

The smell stays with me and in my car as we journey down the interstate.

The many miles we must go to your house and wait
On the many well wishers that have come near and far
Holiday Ramblers travel from all over, as you once traveled with them, to pay their respects
to you and your kin.
The meal that is prepared could feed an army.
No one can ever say Baptists don’t know how to cook or feed in a time of need.
Then, one by one they leave, and it is only your wife, your children, and grandchildren left,
and still I can’t get that smirk of yours out of my head.

What are you thinking? What do you wish to say? What is you wanted me to know before you got away. The answer starts to come when grandma takes me by the hand. She places your ring on my finger and tells me to take care Because it signified your love for all these years, and now it is on my hand feeling my heartbeat where it once felt yours.

Is this a sign of what you wanted to say? I want to understand your plan.

As I get in my car and I turn to leave I resort back to the thing I always use to escape my minds reverie. Some are physical, some spiritual or mental, but you know me best, you know my mind is musical.

My fingers press buttons on the IPOD shuffle wanting nothing more than to absorb my
thoughts into music that will take me away…
…allow me to escape into my world of imagination.
Song One, Home by Chris Daughtry…

“I’m going home to the place where I belong. Where you love has always been enough for me.”

I hit shuffle. Song Two, Bring Me To Life by Evanesence… “How can you see into my eyes like open doors.”

I hit shuffle. Song Three, Jack Johnson’s Supposed to Be… “Maybe its up with the stars, maybe its under the sea, maybe its not very far…”

I hit pause. I catch my breath. Three songs randomly. Yet they all possess the message I don’t want to hear, and yet it keeps hitting me in the head.

Why can’t I just fix this? Why can’t I just make things like they used to be? Why can’t everyone just be happy?

I hit pause again and shuffle to the next song.

What they heck? Even Legally Blonde: The Musica is telling me I have a Chip on my Shoulder.

I turn off the music and listen to the quiet instead.
Which is quite scary if you’ve ever heard the voices in my head.
They’re telling me in unison to just breathe, and it’s the first time I’ve realized that I haven’t
been.
I’ve been holding back, been holding out, trying to be the strong one.
Never let them see you sweat…
…Or cry as the case may be.
I’d try to explain but it won’t come across easily.

I make it to my driveway and into my house.
Passing the bills left unpaid, throwing the keys on the table, and shedding the clothes until I
reach my destination.
It is not long before I fall into a deep sleep.
The trouble with sleep is you are no longer in charge.
You allow your mind to tell you all the things you wish you did not know.
You allow your mind to show you the things you wish you did not see.
The things that are usually right there in front of me.

And in my dream I see you sitting there.
In my dream I wonder how that is even possible.
And its then in my dream that I see something I could not see.
You really have found the land of cancer-free.
There are no more tubes, and no more oxygen machines.
It’s just you and me and our family.

You look me in the eyes and I see that same smirk that has been bugging me all day. I see the rest of the family already knows the trick that I’ve been to stubborn to see.

That you are simply waiting in the land of Cancer-free for me and all of our family. You say “I’m sorry”, and “I’m in a better place”, and “If you need anything do not hesitate to call.”

And in that moment I realize that funerals are not for the dead at all.

They’re for me, my family, and anyone else that has dealt with death.

To say goodbye, or as I’ve realized, maybe something else. Because my grandpa looked into my eyes and he told me that he had come home to the place where he belonged, but when he looked back to see he saw through my eyes like open doors that I could not understand that this is how its supposed to be. “Get the Chip off Your Shoulder” he smiled and said. “It really matters not that I am dead. I just made it here first, and I’ll be here waiting for you when you take your ride on what I have waiting on you.”

And it was then in that moment that I understood his smirk.
I got it. I understood what that look was for.
Because my grandpa knew that we would meet again.
That in no way is this the end.
And in his own way he left that message for me because he knows my mind works musically.

He left me a song so that I would know that this dream of mine was no joke. For in this funeral for the living, not the dead, he placed a song that is now stuck in my head…

“I’m gonna take a trip on the good old gospel ship. I’m going far beyond the sky. Oh, I’m gonna shout and sing until the heavens bring, and I’m bidding this world goodbye.”

Okay, Grandpa, I got the message.

Until we meet again.

Song Credits:

The Old Gospel Ship Composer: Johnson Oatman Public Domain

Bring Me To Life Composers: Amy Lee, Ben Moody, and David Hodges 2003

Home Composer: Christopher Daughtry 2007

Chip On Your Shoulder (Legally Blonde The Musical) Composers: Music and lyrics by Laurence O'Keefe and Nell Benjamin and book by Heather Hach 2007

Supposed to Be Composer: Jack Hody Johnson 2006
```

---

## IC-1493: What You See

- Title: What You See
- Author (byline): Not specified
- Work: What You See
- Publisher: SpeechGeek
- Publication date as stated: 2017
- Event as filed: Program Oral Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2155
- Already set (do not supply): none

### Source block (context only)

```text
What You See Ain’t What You Get A program starter by
Tiembé Maboola
ISBN: 978-1-61387-304-5
Copyright 2017 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2017, is identical to the printed published
version of this same publication dated 2017. This statement, along with the entire printed
PDF of this publication, must be presented at any National Speech and Debate Association
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
This collection of poetry is intended to peel back the way assumptions color our interactions; what we see and what we think we see are often very different. Through exploring the emotions of attraction and alienation, each of these poems offer a different perspective on what it means to judge a situation or a person based on looks alone. Acknowledging the limitations of our perceptions is the first step to improving how we understand, relate, and connect to each other. The voices in these poems are intended to showcase different points of view and a variety of cultural and racial backgrounds. The conversation on race is such a volatile subject that one point of view seemed inappropriate. However, if the student prefers to speak from one ethnic vantage point, pronouns may be changed to suit the speaker’s intention.

The Power of Vulnerability

At first,
perhaps you will allow the invisible forces of nature
that attract opposites and bend light
to persuade you into thinking you stand a chance.

Glance.

Gaze an opportunity to charm your way in.
You wish to claim my heart as yours.
The way to a man’s heart is through his stomach, you surmise
So the way to a woman’s heart must be through her thighs.

Perhaps.

You saw a challenge.
Or maybe I'm not the prize
you had your eyes on
I display nothing delicate outwardly
And even though my inner battles are fought quietly
The words
Conveying nothing but naked truth
I let drip from my mouth and evaporate into your ears
undress the more I speak to you

I will not apologize For being bold and passionate, right and wrong

I won’t attempt to lure you with my looks.
I won’t gimmick you with flirtatious gestures,
or charm you with superfluous words.
I expect the same in return.

For over time I have come to learn that first impressions are as finite as love at first sight.

And these bones that frame my flaws,
holding up these walls. I keep
hiding a heart that somehow
always finds a way to my sleeve.

Its strings are being re-tuned by the chief musician, as rare birds with broken wings are.

Come.

Be sure to listen to her song. She doesn’t sing it for just anyone.

Show.

Show me your ugly,
Your sentimental
Your messy
Your blunt
Your just plain silly
Show me your weak
Your indecisive
Your cheeky/strange/repressed/impressions of what it means to be
human
Because that’s all there is to me

And if you dare to love this bird rare

Know.

Having nothing but mere metaphors to hide behind Sitting at the edge of the chasm of life’s peak, I Admit.

Admit.

That I am not all that I am, But what I try to be. Try not to be.

Speak.

My truth –
spilled out in the form of a prayer in poetry,
where I choose to undress my pride,
and risk it all to confide what’s confined inside the holy temple of my mind –
it is my Bethesda
Weak.

Yet I am strong for I have discovered sufficiency and the grace of the trinity inside of me. The soul, the body, the mind.

I no longer behold through rose tinted lenses Life becomes… The things that live on are the mountains yet to be moved

Transformed.

The truth
unchanged in the light
unbent by the forces of nature:
I am an unfiltered photograph,
I am analyzing closely.
I am a piece of art.

Why are we so afraid
of being that which we naturally are?
Indecisive, unreliable, messy matted tangles of emotion
Wrapped in skin that protects us from the outside world
And connects us to it.

Human.

With a history of scars
And assorted shames
That have added layers to my skin,
Callous
To my frame.
But this vulnerability,
it is tender but not liable;
it is neither slander nor libel.
It is its own kind of strength,
Reminding me that even though I’ve seen better
The days ahead will be greater.
And that’s not a lie,
It’s a promise.

Honest.

Because some days,
A voice is a well in the desert
and within each long pause,
Between answering life’s questions,
I’m swallowing my pride.
And showing
an ancient art form passed down of African daughters.
Woven together by divine hands.
This is a tapestry of bruised beauty

So keep glancing
Keep watching
Because the parts of me that are worth more
Looking at and loving
The parts of me unravel
only with slow work
Steady hands
And long, psalms of silence.

White Noise

It happened by accident (if you believe in such things).

Age 8 Reaching for the crossbeam on the monkey bars at the same time, our bodies collided. Like two galaxies, we were dust and atoms, gravity and momentum. And after we met, we collapsed into a pile of arms and legs. Awoken by the force of our discovery.

As the skin of our elbows and knees bloomed into bruises, we compared – how his looked like a plum-colored dahlia and mine a boring pink rose.

I wondered out loud, does that mean our blood is different colored? Probably, he said.

His came from Mexico; from rivers of music and valleys of heat; he said his grandma was stained the color of mesa from making tortillas; his mother was tinted the color of earth from working in the garden; his father was bathed in the color of blood from the last time he saw him.

And I felt very different from him.

My father, my mother, my grandmother had no tint or shade or hue. I made the mistake of thinking that meant I had no stains.

Age 11 By the time I found my voice, it was changing. Cracking and popping like knuckles under stress. Every syllable was a pressure point: say the right thing and the tension breaks. Say the wrong thing and there is that almost silence. That painful need to complete…

And when my teacher asked me to pick a hero to report on, I chose Columbus. The parallels are not lost on any middle schooler – stumbling into a world, hoping to discover meaning. A lost captain who thought he knew, but couldn’t imagine.

But my teacher’s Mayan ancestry, coiling around the double helix of her DNA like the ancient god, Kukulkan, sprouted fangs. She called me naïve. Insensitive. And asked if I would call Hitler a hero too? No, my voice cracked, he was a murderer.

I was sent to the hallway while she collected her thoughts. Later she would tell me it was a teachable moment. About history’s one-sidedness, she said. About the cost of discovery. And I knew what she meant, but didn’t mean.

And I felt very different from her.

Age 15 A beautiful girl said she like my sun kissed skin, adding heat to the burn in my cheeks. I told her that it always happens when I forget to wear sunscreen. She didn’t burn. She glowed. The more she swam in sunlight, the more she became it. And I wanted to know. Why? I wanted to know. What makes a person burn and what makes a person glow?

What chemistry, or biology, or ideology makes two humans so different: a beautiful corn-rowed caramel and a red and white peppermint stick? So I asked her what she was. And the slap that followed made my ears ring and my eyes water.

But at least the burn hid the handprint.

Age 17 The night the theater lost power, we stumbled out into the darkness together. A sea of humanity, lead by flashlights: some people seemed nervous. But not me. Instead the beauty of simple silhouettes of disappointed moviegoers struck me. We had more in common then than just about any group of strangers I’d ever been a part of.

Finding the street, bathed in orange overhead lighting, the spell was broken. And as we headed back to my car, I remember seeing a group of kids who looked my age but looked nothing like me. They were walking toward us.

We didn’t say anything. There wasn’t a moment of panic or pause. It was a subtle shift in our direction and we crossed the street.

Telling ourselves that we would’ve needed to cross the street eventually. Telling them that their darkness is scarier than a theater with no light.

Age 20
Sinking even lower in my seat as she stood taller and taller to address the teacher. In
sharp contrast:
Me: Hung over from the night before.
Her: Hung up on an assignment that was cursory and forgettable.

This isn’t important. I say to myself. She doesn’t need to make a big deal about this. She is just wasting time.

Still persistent, she decreed that a world literature class should include the works of – insert names full of accents and special symbols here. To at least introduce the idea that non-white writers exist.

The professor looked at the rest of us (all white). As if he was still one of us. And that nauseas feeling of us and them, surfaced again.

He tried to make the case that the curriculum was out of his hands. Not his call. That the works included were determined by the dean. At which point she asked, “Well, which old white dude is that?” The air is sucked out of the room. I felt a pull to sit up straighter. The teacher has gone from oppressive white to offended pale. He stammered and stuttered like he was trying to pronounce those special names and she didn’t wait for the response. She grabbed her bag but left her fat book of dead white men and walked out of the room. I wanted to join her. I could’ve been the moth that gravitated toward her flame. But I stayed in my seat. What difference would it make?

Would it change the color of my bruises? Would it remove the handprint under the burn?

Would it put me back on the right side of the street?
Or would I simply be playing the part
The white savior who could not understand
But thinks he could

The teacher shrugs.

The whitest response of all.

We return to our studies because privilege makes us immune to such displays.

And I worry about the days when I don’t care about feeling different from her.

Georgia

She sings on the corner of 15th and Franklin. A popular spot at exactly two times per day: when I am trying to get to work and when I’m trying to get away from work. Both are a struggle for me.

She doesn’t seem to have the same “employment problem”

She has grey at the temples, pronounced arthritis in her hands, and one outfit: a faded Georgia peach sweatshirt.

Every day, rain or shine, she is there. She doesn’t seem to be singing to anyone in particular, just loud hymnals to make us all aware that the blood of the lamb makes the sun shine bright – or something.

And on the day I got fired, I didn’t have anywhere to go, but I left early. In the elevator, all the way down, I wondered how I would face my family. How I would make my rent. How I would find the energy to get out of bed tomorrow.

When I heaved myself through the glass doors into the blinding and anonymous world, there she was. Sitting on the sidewalk. Singing.

“What are you doing here?”

“Singing,” She said. As if I was the crazy one. “The world needs a little singing and I need a little singing and something tells me this is the spot to do it.”

“That doesn’t even make sense. Don’t you have a home or a job? Don’t you have things to do other than stand out here? Or are you too busy being homeless and useless to even try to make sense of this world?”

“Is that what you’re doing? Making sense of this world? Because one of us is carrying his life in a box right now, and it ain’t me.”

“I just got fired. I just lost everything.”

She saw me then. Saw exactly how small I was. How pathetic and pointless I was. So, she hugged me. I didn’t want her to, but I needed her to. She hugged me until I started crying.

And she said “You’re the reason I sing. Because there are so many people who lose things everyday. Jobs. Cars. Money. Homes. The matter that don’t matter. Not everybody need to be a singer. But everybody need to find something to sing about.”

She sent me on my way then. As I got further away, her song bounced off the buildings and snuck into my head. And just before 18th street, I looked back and she was gone. But For a moment I swear I saw her halo wink in the sunlight.
```

---

## IC-1494: 130 Million Shattered Lives

- Title: 130 Million Shattered Lives
- Author (byline): Tanya (a refugee), Wang Ping
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1515
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tanya (a refugee)
On-Line Transcript:
https://www.freedomfromtorture.org/real-voices/six-
refugee-poems-insight-life-refugees-and-asylum-seekers
ISBN: N/A
Publisher: Freedom From Torture.org
Date (Month/Year): Accessed on July 3, 2024
Author: Wang Ping
Book: My Name is Immigrant, Pg 7
ISBN: 978-1934909669
Publisher: Hanging Loose Press
Date (Month/Year): May 2020
Author: Blas Manuel De Luna
Book: Bent to the Earth
ISBN: 978-0887484315
Publisher: Carnegie Mellon University
Date (Month/Year): Feb 2005
Author: Denice Frohman
Book: Alight: Best-Loved Poems from the 2013 Women of
the World Poetry Slam (Pg 86-89)
On-Line Location:
https://paperzz.com/doc/9383676/alight--the-poems-of-
wowps-2013
ASIN: B00EHA5AYU
Publisher: Bicycle Comics
Date (Month/Year): 2013
```

### Introduction (context only: never use it for content warnings)

```text
*130 million – That’s the number of people the UN Refugee Agency expects to be forcibly displaced or stateless by the end of 2024. – 130 million.

It’s difficult to find the right words to describe the plight faced by this staggering number of refugees. Being (insert age) from (insert hometown) I can only imagine the confusion, fear, and the overwhelming sense of hopelessness. For those outside the crises, these people have become statistics -- repetitive news reports -- and I worry that we have become immune to their humanity.

I don’t have the words, but many immigrant writers have brought their experiences to life through journals, letters and poetry. Their truth transcends location. I don’t have the words, so I’ll give voice to theirs.

130 Million Shattered Lives with poems by a refugee known only as Tanya, Wang Ping, Blas Manuel De Luna and Denice Frohman.
```

### Performance text (classify this)

```text
Blas Manuel DeLuna and Denice Frohman

Solidarity by Tanya Women clothed in their leader’s regalia Men, adorned in T-shirts with the leader’s face on their broad

chests. The volume of their voices singing songs Praise, adoration, appreciation and dedication could be heard

miles away. Milk and honey, they sang.

No matter how badly the weeds had grown in the fields,
People dropped everything to be there,
To attend the rally and listen first-hand.
They glided,
Some carried cockerels, goats, baskets full of eggs,
Or vegetables to give to the heroes who had fought and brought

us freedom.

We loved them, our heroes.
Nobody wanted anyone to cough or whisper,
Nobody wanted to miss a single word.
We worshipped them like gods.
Worshipping the ground they walked on.
We became very close,
Following everywhere they went, to show our solidarity.

Then things began to change.

Solidarity by Tanya (con’t) It came to me in an instance. I had bought a new cup from a second-hand shop When I lifted it up to the sunlight, I couldn’t see any flaws. When I got home, I decided to christen it with a cup of tea. But the moment I poured the boiling water, it cracked down the

middle. It came to me in an instance: what was happening in our country.

Everything looked perfect, all the words they said,
But something was very wrong.
Meetings held in secret,
People began to attend less and less.
Chiefs were threatened:
Villagers needed to attend, or food aid would be withdrawn.
The threats became more frequent
And then the militia used their force.
Gates were shut, and militia manned them:
People could come in, but no one could leave
Even if you had medical problems.
Then came the public flogging
Of those who had deserted.

Brutal! It was brutal. All our hopes, dreams shattered.

All we wanted was to have our voices heard.
To build the country as one.
But all was denied.
We had been in solidarity with them for a long time.
Now they were stabbing us and maiming all those who dared to

oppose.

things we carry on the sea by Wang Ping (Pg 7)

we carry tears in our eyes: good-bye father, good-bye mother

we carry soil in small bags: may home never fade in our hearts we carry names, stories, memories of our village, our civilization we carry scars from proxy wars of greed we carry carnage of mining, droughts, floods, genocides we carry dust of our families incinerated in mushroom clouds we carry our islands sinking under the sea

we carry our hands, feet, bones, hearts and best minds to start a new life

we carry diplomas: medicine, engineer, nurse, education, math, poetry, even if they mean nothing to the other shore we carry railroads, plantations, laundromats, bodegas, taco trucks, farms, factories, nursing homes, hospitals, schools, temples. . . built on our ancestors’ backs

we carry old homes along the spine, new dreams in our chests we carry yesterday, today and tomorrow we’re orphans of the wars forced upon us we’re refugees of the sea drowning in plastic wastes we came from the same mother in Africa we’re your children, sisters and brothers, father and mother

our tongues carry the same weight as we chant

爱(ai)，بح (hubb), ע ביל (libe), amor, love 平安 (ping’an), ملاس (salaam), shalom, paz, peace

希望（xi’wang), لمأ (’amal), hofenung, esperanza, hope, hope, hope

as we drift . . . from dream to dream . . . sea to sea . . .

TRANSITION For those refugees fortunate enough to reach the US border, you would think that their troubles are finally over --- “Give us your tired, your poor, your huddled masses yearning to breathe free . . .” Unfortunately, some borders are more than physical and cannot be crossed only by foot. Currently those arriving in the US seeking asylum protection are facing extended waiting periods – up to 7 years in some cases. Meanwhile, they have restrictions on their right to work and to assistance programs, making it nearly impossible for them to support themselves or their families.

Bent to the Earth by Blas Manuel De Luna
They had hit Ruben
with the high beams, had blinded
him so that the van
he was driving, full of Mexicans
going to pick tomatoes,
would have to stop. Ruben spun

the van into an irrigation ditch,
spun the five-year-old me awake
to immigration officers,
their batons already out,
already looking for the soft spots on the body,
to my mother being handcuffed
and dragged to a van, to my father
trying to show them our green cards.

They let us go. But Alvaro
was going back.
So was his brother Fernando.
So was their sister Sonia. Their mother
did not escape,
and so was going back. Their father
was somewhere in the field,
and was free. There were no great truths

revealed to me then. No wisdom given to me by anyone. I was a child who had seen what a piece of polished wood could do to a face, who had seen his father about to lose the one he loved, who had lost some friends who would never return, who, later that morning, bent to the earth and went to work.

Borders by Denice Frohman (Pg 86-89)

It starts before she gets here.
before the stairs tell her she is alien
to a country that knows her great
grandfather’s Mexican hands all too well.
His fingerprints still echo underneath
the railroad tracks and cotton fields
where bent knees and bent backs
once picked, plucked, pushed work
for more money than he was used to,
but less than he deserved.

For Ana Maria, it begins before the border. She walks with her two Uncles and Abuela through the desert for one week with nothing more than a few gallons of water, and a prayer tucked into their pockets, hoping both will last them long enough.

The sun is an unforgiving God, but any God is worth having right now.

The wind pushing at their backs
is the grunt of gunshots from drug cartels
and the desperation of a job to employ their stomachs.
Both have been uninvited guests at their doorstep.

so they step, step,
Ana Maria’s small hand clutches the bottom
of her Abuela’s dress,
another step,
her mother waits for her on the other side
hoping that her face still sings of home like it used to.
another step,
She is too young to know what “border” means,
she thinks that people
are just family members who haven’t met yet.

After they arrive, she will learn there are some borders you can’t cross by foot.

Ana Maria is now 10 years old.
She’s learned enough English to translate for her parents,
but says that her thick accent is still a problem
she tries to fix by leaving it in her locker.
When her teacher calls on her to read
she tries to speak proper. Like proper has a sound.

She pushes her tongue down so it doesn’t roll her “r’s,”
but she trips on the flatness of the syllables
that usually bounce with too much salsa.
She tries to rattle out the kinks in her speech,
but her tongue is a stubborn dancer.

The two boys behind her don’t know how to do long

division, but they know what a wetback is, and that Ana Maria has braids, and that Ana Maria’s hair is thicker than their sister’s, and they don’t know how they know, but they know how to treat difference when they smell it. So they say things like, “Go back to your country,” as if their Irish ancestors never walked through Ellis Island.

Ana Maria is now 16.
Her father works 18-hour days as a dishwasher.
Her mother cleans houses she’ll never get to live in
so that Ana Maria can sit in a college classroom
and say, “I am here.”

But her guidance counselor says she can’t get financial aid, or the in-state tuition rate, because of her status.

She says it like an apology.

Ana wonders if her family ever crossed the border, or if they are just stuck inside another one, aggravating it like a sore.

Her guidance counselor stands in front of her, with a mouth full of fences.

There are some borders you can’t cross by foot. Borders, I tell her, that can only be crossed by stubborn backbones

so if they ask you for your papers, show them your skin, wear your tongue like a cape, throw up your fist, like a secret you can’t keep any longer, they can’t keep you any longer, afraid you can’t ever afford to drive or dream.

So if they come for you, tell them in the language you know best, that you are not scared anymore.

*Introduction Source Information Reflections on the Global Refugee Forum and the Road Ahead in 2024 – January 3, 2024. https://refugees.org/reflections-on-the-global-refugee-forum-and-the-road-ahead-in-2024/

*Transition Source Information What happens once asylum seekers arrive in the U.S.? – June 5, 2024 https://www.rescue.org/article/what-happens-once-asylum-seekers-arrive-us
```

---

## IC-1495: The 1619 Project: Born on the Water

- Title: The 1619 Project: Born on the Water
- Author (byline): Nikole Hannah-Jones and Renee Watson Questions
- Work: Not specified
- Publisher: Kokila
- Publication date as stated: Nov 2021
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1159
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nikole Hannah-Jones and Renee Watson
ISBN: 978-0593307359
Publisher: Kokila
Date (Month/Year): Nov 2021
```

### Introduction (context only: never use it for content warnings)

```text
Who are you? For African Americans, the answer is something far more powerful than a simple family tree. Our identity is more than a litany of specific names or places. It is understanding the strength these people said to be “born on the water” needed to survive and how that drive has been passed down through generations.

African American history is not just a story of loss, but a story of resistance (no matter how small) and pride. A story that begins not in shame, but in courage.

Who am I? I am (insert name) and this is . . .

The 1619 Project: Born on the Water by Nikole Hannah- Jones and Renee Watson
```

### Performance text (classify this)

```text
My teacher gives us an assignment. “Who are you?” she

asks. “Trace your roots. Draw a flag that represents your ancestral land.”

Most of my classmates can count back many generations

and learn about the countries where their families

came from. They draw their flags. But I leave my paper blank.

I do not know where I begin, what my story is.

At home, Grandma asks, “How was school?” I tell her about the assignment, how I couldn’t finish it. How I can only count back three generations, here, in this

country -- where my parents, my grandparents, and my great-

grandparents were born. But before that, I do not know.

I tell her that I am ashamed.

Grandma gathers the whole family, says, “Come, let me tell you our beginning. Let me tell you where we’re from.”

What Grandma Tells Me They say our people were born on the water, but our people had a home, a place, a land before they were sold.

Their story is our story. Before they were enslaved, they were free.

Their Hand Had a Knowing
Their hands had a knowing.
They knew how to hold a baby close,
how to rock the child to keep her from crying.

Their hands knew how to mix herbs, how to get the just-right flavor for the meal.

Their hands knew how to beat and twist and shape iron. How to make gardening tools, armor, and weapons.

Their hearts had a knowing. They knew how to make work joyful, how to create rhythm by pounding the tools against

metal, knew how to make music to keep them company as

they worked.

Their minds had a knowing,
worldly, curious, sharp.
When they met the white people,
they learned quick, taught their tongues
to speak Portuguese,
taught their eyes to read strange words.

They knew how to mix the old with the new, how even an ancient people always had more to learn.

And They Danced
And the people moved their feet,
moved their whole bodies
to the melody of horns and stringed instruments,
of marimbas and drums.

They danced to celebrate, to mourn. They danced as a way of worship, to offer thanks.

Their bodies a song under open sky and bright sun. Their bodies a swaying testament to a beauty of

creation.

Stolen
400 years ago, in the year 1619,
. . . the white people took them anyway.
Kidnapped them.
Baptized them in the name of their god.
Stamped them with new names.

Ours is no immigrant story.

They did not get to pack bags stuffed with cherished things, with the doll grandmama had woven from tall grass, with the baby blanket handed down from generation to generation all the way back, so far back that it carried the scent of the ancestors.

They could not hug their fathers and mothers, daughters and sons, hearts thumping in rhythm, clinging to that final sweetness before the parting. No promises, whispered from mouth to ear, of seeing each other soon.

Just wails and sobs. Confusion and wrists worn raw from shackles made of iron, feet split and bloody from the 200-mile march along the Kwanza River.

They had no things. But they had their minds. The old ways, the harvest songs . . . etched in their memories.

They had their bodies. Histories and bloodlines
and drums pulsing in their veins.
With trembling fingers
they braided seeds into their hair, defiantly hiding
tiny pieces of home
to plant one day
in new soils.

No matter what some say, the people fought. And the white people took them anyway.

Forced them into the bottom of an evil ship, to sail to a “New World” they had no desire to see.

Ours is no immigration story.

The White Lion Maybe it was the second month, or the third, when they had not seen their land

or any land for so many days, they could no longer count.

Some could not bear the pain.
They refused to eat.
They shut their mouths
until their hearts gave out.

Others tossed themselves
into the teal eternity of the Atlantic Ocean,
swimming one last time
with the ancestors.
Sickness and hunger,
filth and cruelty
took the others. Almost half.

But those who did not die resolved to live no matter what.

Packed in the dark misery,
strangers chained together
head to feet, hip to hip,
in the bottom of a ship
called the White Lion,

they saw that strangers–
men, women, children, kidnapped too,
from many villages–
these were their people now.
These many people
became one people,
a new people.

And that is why the people say, We were born on the water. We come from the people who refused to die.

How to Make a Home We are in a strange land, they said. But we are here and we will make this home. We have our songs, our recipes, our know-how. We have our joy. We will love, laugh, sing and hug our children as tight as you can hold a child. We will survive because we have each other.

Resist
Life was hard,
and it would get harder
for the generations to come.

White people told the people they were not human.
That the people were things
to be bought and sold and given as gifts
alongside horses and chairs.

When the people were beaten,
they said the people did not feel pain.
When they sold the people’s children,
they said the people didn’t love.
These were lies they made up
so they could feel okay
about slavery. It was wrong, always
and forever, to own human beings.
It was wrong, always and forever, to treat
human beings like things.

The people fought back.
For 250 years,
the people resisted every day
in ways big and small.
For 250 years,
the biggest resistance of all
was that the people kept living.

Legacy
The people who were born on the water survived.
They were brokenhearted, beaten, and bruised,
but they became inventors and athletes,
nurses and cooks,
pilots and architects,
farmers and housekeepers,
singers and artists,
dancers and poets,
mathematicians and scientists.

No one could steal the people’s joy.
They wrote songs,
created jazz and hip-hop,
rhythm and blues.

Pride
Grandma looks at me and my brother, tells us,
“This is why we say
Black Lives Matter,
why we celebrate Black Girl Magic,
why we believe we are our ancestors’ wildest dreams.”

“Never forget we are their hope.
Never forget you come from a people
of great strength,” Grandma says.
“Be proud of our story, your story.”

The next day, I go to school, pull out my red crayon, my blue, and my white.

I draw the stars and I draw the stripes
of the flags of the country that my ancestors built,
that my grandma and grandpa built,
that I will help build, too.

And I am not ashamed.
I know what my story is,
where I am from,
where I begin…
```

---

## IC-1496: 1990

- Title: 1990
- Author (byline): Bob Holman
- Work: Aloud: Voices from the Nuyorican Poets Cafe
- Publisher: Holt Paperbacks
- Publication date as stated: Aug 1994
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1059
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bob Holman
Book: Aloud: Voices from the Nuyorican Poets Cafe
ISBN: 978-0805032574
Publisher: Holt Paperbacks
Date (Month/Year): Aug 1994
```

### Introduction (context only: never use it for content warnings)

```text
The Year 1990: Leading anti-apartheid campaigner Nelson Mandela is been freed from prison in South Africa after 27 years. People danced in the streets across the country and thousands clamored to see him at a rally in Cape Town. Now 71, the lawyer from the Transkei homeland was convicted of treason and sabotage in June 1964 and sentenced to life imprisonment. He spent most of his sentence on Robben Island, off Cape Town, doing hard labor. Since the 1980s he refused numerous offers for early release from the government in Pretoria because of the conditions attached. Nelson Mandela is Free! February 11, 1990 by Bob Holman.
```

### Performance text (classify this)

```text
The taking of flash photos & use of recording devices of any kind, including pens, pencils, eyes & ears, is strictly encouraged.

It's 1990 & Nelson Mandela is free!

& people are looking at each other
They're going like "Wha?"
& the other people are looking back
& they're going like "Duh?"
& finally, after this deep interaction,
You hear the wild cry of:
"Excuse me, could you tell me the time?"

What time is it?
It's Wake & Shake Time
It's Death of the Decade Time
It's Turn of the Century Time
It's Gyrate the Millennium Time
It's the End of Time
"At the sound of the tone it will be the End of Time"
It's 1 PF - it's Post Future
It's 1 PT - it's post time
It's Post Time!

It's 1990 & Nelson Mandela is free!

History's on fast forward Make that double-fast fast forward That's where you run past the Future so fast you're back in the Past Sure, it's the End of History So how come all we can think is, "What comes next?" One minute you're rolling in ecstasy because the Berlin Wall is tumbling down, The next you think, a reunited Germany! Oh God no! Here come the storm troopers! & I'm Jewish (Well, my father was Jewish,

so I'm not Jewish enough for the Jews - but I'm Jewish enough for the Nazis!) One minute it's survival tactics & the next it's where's the angle

It's 1990 & Nelson Mandela is free!

& everybody wants a little glasnost We know we want it cause we see Frank Zappa smoking cigarettes with Vaclav Havel,

who 6 months ago was in jail, an artist whose work was banned by the government,

now he's the President of Czechoslovakia So stop in for free baby burritos at the corner bar Except suddenly it's a karaoke sushi bar specializing in piranha sushi,

& everybody here's a star, Because you get to stand in front of the massive TV screen showing an MTV-minus one

video clip & sing along with the bouncing ball -- Except the words are all in Japanese and how can you sing "Feelings"

with feeling in Japanese? Kanjiru! Watashiwa, kanjiru!

It's 1990 & Nelson Mandela is free!

Communism has collapsed At last the Russians get to wear the "Happy Face" masks & stand in line for a Beeg Mek The Azerbaijanis are finally free so they get to beat up on the Armenians Yugoslavia has decided to go back to indigenous cave tribe groupings In Italy the Communists have met & decided they're not Communists They're gonna change their name to be more appealing to the Socialists and the Greens But for the time being they're calling themselves simply The Thing The Thing! Personally, I'm planning to vote for - the Thing For the time being For the time being There's nothing left anymore except for the time being You live your whole life for the time being While meanwhile -- there is no meanwhile

It's 1990 & Nelson Mandela is free!

"Play ethics by ear"
Let me out of here - but which way is out?
I'm a part of the food chain, isn't that enough?
At night I snuggle up close to the warm blue glow of
images provided for everyone

by a select few Listen, they've packaged a shopping mall so small you can only visit it with

a Video Walkperson, a cellular phone and a Visa card
The world is changing, but we're not
We're stuck in a commercial for Life
Trying to figure out who to give the money to
When, surprise! There is no money

It's 1990 & Nelson Mandela is free!

Senor Yuppie! Phone call for Senor Yuppie! Pardon me, have to step over these homeless people to close on my Home Equity Loan,

sorry "Our bodies are still tender & not full grown & the prospect of dying frightens us all,

but history calls us & we must go" But where did they go, the Chinese students on their bicycles riding towards the tanks

at Tiananmen Square, It can't happen here because it's already happened here AIDS epidemic grabs Life till we don't even see it, gone like holes in heart, Surrounded by ghosts, meeting Death in the middle of Life While lesbians and gay men still have to fight for the right to love & be sure to send your poetry to the Department of Official Bullshit to get labeled So it just has to be -- time to get a Coop! --

buy the place you used to rent, and still get to pay the rent It's time to be a great parent --

work extra hours to pay for the best childcare while you're away My kid is majoring in Nikes Don't worry! Don't be happy! Explode! The decision of birth from her body is solely & privately that of the woman herself

It's 1990 & Nelson Mandela is free!

And everything used to be something else
Now it's 1,000 words a minute, & Times Square is just so
much more interesting
We're hellbent on something, sort of positive in a senile
way
I can't even keep up with my life
It's a secret between me & my stunt double
Honey, I'm home - nuke me
Hop to it, ban cigarettes before it's too late
It's Earth Day again, if you can find any earth left
Paranoia used to be a psychosis, now it's a national
pastime
Try the new fashion: the bare breast style of no clothes
at all, & it's not cheap, either
& poetry is the newspaper of the future
Except it's locked out of the media
You know things! Think them!
There's optimism at the yacht club
The salad bar is open
Excuse me, isn't it time to mow your head?
I hate you! Thank you very much, have a nice day
They don't even know what it is, but they've already got
an option on it
They're buying into it! Let's Not Make A Deal!

It's 1990 & Nelson Mandela is free!

& there's a guy at the microphone & he's yelling at me
& he's not using language that makes any sense from
where I come from
It all rhymes & it all starts with capital letters
& it's all intense italics underlined three times in bold
face headlines
& all I can remember is the part about
It's 1990
& Nelson Mandela is free!

& around the world a sense of possibility As women slowly ease the old gray dinosaur poobahs from their penile thrones The universal remote control is being passed into your hands

Zap it! Zap it! Zap it! Zap it! Zap it!

It's 1990 & Nelson Mandela is free!
```

---

## IC-1497: An Abridged History of America

- Title: An Abridged History of America
- Author (byline): Joshua Sands
- Work: Turning Points, Pg 39-46
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 907
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joshua Sands
Book: Turning Points, Pg 39-46
ISBN: 978-0742117013
Publisher: Tichenor Publishing
Date (Month/Year): 2001
```

### Introduction (context only: never use it for content warnings)

```text
Where to start . . . Where to start . . . Ah Ha! Got it . . .

“We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness. — That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, — That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to affect their Safety and Happiness.”

Let’s start there with An Abridged History of America by Joshua Sands.
```

### Performance text (classify this)

```text
(Pg 39-46) God bless America.
Land that
I
love.
We set forth
for this
great
land
With beautiful English
ships,
English
money,
English
people.
We got settled with
English
help,
English food
shipments,
English medical
remedies.
We settled
and we spat on the
English,
shot the
English,
poured tea
on the English,
declared independence
from the
English.
Thanks
for the
memories, England.

Now leave.

We’re comin’ to America.

Indians treated
the land
with
respect.
So we shot
them,
raped them,
moved them
to five square
blocks south of
Phoenix, Arizona.
We’ll even pay
the Indians
if they show
us a
raindance.
Entertain us –
We should celebrate
Thanksgiving
by watching the
turkey with
it’s head chopped
off.
Bleed and run.

Run and bleed. We’ll catch up to you.

OK – everyone squeeze in! You can all fit, dammit. Yes, those are all the names of the people who went to Vietnam. No, you can’t visit them. Now smile!

We purchased
Blacks from
Africa,
whipped them,
beat them,
kept them illiterate,
Called them 3/5
of a regular
American
(for census
purposes only).
Even when they were
“freed”
they were uneducated,
scoffed at,
laughed at,
spat on.
Only now they
were homeless
and
hungry.
Thanks, Blacks,
For picking our
cotton.
We’re warm.
Now,
go build
a
fire.

I’m confused who you Americans look up to.
Who do you respect in your country?
You mock your leader on talk shows
and impersonate him to create a cartoon.
Who do you look up to?
We have Nobel Prize winners, novelists,
Inventors, and political officials.
You have mistresses, lotto winners,
movie stars, and basketball players.

We fought some
wars for rightful
causes:
Weird people
out there:
Stalin,
Hitler
beware.
Yet we were
and are
the only people
to drop an
A-Bomb on anyone.
And then do it again
for
emphasis.

I came to America to witness the future
I learned the language.
I brought my own money.
I came to America because they say it is the land of dreams.
I did not come to America to live here.
The street is not safe and I’m getting older.
I want to leave America, but have no money.
I want to leave America, but can’t find directions.
On those carnival rides, they let you off when you get sick.
Please stop.
I want off.

We’re homeless in America.

The Blacks found a leader: Martin Luther King.

so we
shot
him.
We found a leader:
JFK
so we
shot him.
Our leader had a brother:
Robert
so we
shot him, too
We found a singer:
John Lennon
and we shot
him, too
because we
were out of
leaders.

Buy American!
Don’t let the Japanese take over!
The Japanese school day is roughly ten hours,
consisting of rigorous study
in the sciences,
languages,
composition,
mathematics,
history.

The American school day is roughly six and one half hours,
consisting of the same subjects,
With recesses,
study halls,
club meetings,
and convocations mixed in.
The Japanese are ahead because they know mathematics:
six and a half mixed hours
do not equal
Ten quality hours.
But, still, buy American!

We went to war in Vietnam
Because it would
make us feel better.
People protested
the War
because it would
make them feel better.
People did drugs,
had free sex,
wore tie dye,
got shot.
In protest.
And it made them
geel better.

Estimated value of Beanie Baby: $800.

Person who makes Beanie Baby: Annual income, $800.

I was told the other day that we donated over ten billion

dollars to other countries in the name of foreign relief. This will improve their quality of living, or so I’m told. I was told the other day that my son needs an operation. I was told the other day that without it he will not survive. I was told the other day to put up collection jars in the

community.
I was told the other day to pray.
The other day I prayed.
The other day I prayed for a miracle.
The other day I went to the grocery store and picked up

eight dollars In loose change. Today I will pray again.

We elected an actor
to be President –
so we wouldn’t have
to train him
how to lie.
Besides,
he looked
good on TV.
And the Alzheimer’s
jokes were funny
later on
weren’t they?
The Ayatollah took
hostages and we didn’t
shoot him.
Castro was Satan;
we didn’t
shoot him.
Saddam crossed the line
so we shot his people
and their children
but didn’t shoot
him.

Oh, say can you see
Cause my fat *butt* might be in your way
By the dawn’s early light
Yeah, like we’re getting up at dawn
What so proudly we hailed
Hail to this remote control
At the twilight’s last gleaming
Where’s the chips?
Oh say does that Star Spangled Banner yet wave?
(Do the wave)
For the land of the free
But don’t smoke in public, burn flags, burn leaves, or forget
to wear your seat belt.

And the home of the brave Hell, let’s just drop an A-bomb.

We sit in our
air-conditioned
condominium
with our Volvo’s
and our e-mail
and voice mail
and cupboards full
of food
and *75* inch TV’s
With 73 channels
and cordless phones
and power tools
and jet-skis
and mutual fund reports
and Guess watches
and 2.5 kids and
a Dalmatian named
Spot.
And we say that
we deserve it
because we’re
American.
And we buy it
Every time.
```

---

## IC-1498: After the Death of Anna Gonzales

- Title: After the Death of Anna Gonzales
- Author (byline): Terri Fields
- Work: Not specified
- Publisher: Henry Holt and Co
- Publication date as stated: Nov 2002
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1083
- Already set (do not supply): none

### Source block (context only)

```text
Author: Terri Fields
ISBN: 978-0805071276
Publisher: Henry Holt and Co
Date (Month/Year): Nov 2002
```

### Introduction (context only: never use it for content warnings)

```text
Picture this: It's the beginning of an ordinary school day. The bell has just rung. The halls are almost empty except for a few students trying to make it into homeroom before they're marked tardy. The day officially gets under way as usual with morning announcements being read over the PA: "Today is Thursday, October 3rd. Volleyball practice has been moved to 5:00pm. The chess club will meet today in Mr. Malkin's room. Congratulations to the JV football team on last night's 14-0 win against the Raiders. Go JV! Student Council will be selling spirit T-shirts during both lunch periods all week in honor of their victory. And now we have a special announcement from the principal."
```

### Performance text (classify this)

```text
CAUTION - This is a Novel in Verse. We recommend checking with your regional, state or national tournament before entering this selection in POETRY. Some states may require it be entered as PROSE.

Anna Gonzales

(Pg 99-100) "I will slip away,
Making little fuss.
And being less remembered,
which is pretty much the way I have always been.

Never pretty or popular enough to matter. Never outrageous or outstanding enough

to get attention. Sometimes, I have to pinch myself to make certain

that I am even real.
Conversations swirl around me.
Invitations to others surround me.
Even Alexis, who has tried to be my best friend,
Is dragged down by my invisibility.

No, I am not pregnant
Not on drugs
Not alcohol
Not influenced by rock or heavy metal or rap
I am just not.
And I am so tired of trying to be.

So I say good-night to this world Feeling since it has never embraced me It will not mind if I have abandoned it."

Principal Barron

(Pg 6 -7) Thirty years in education.
I’ve broken up fights.
Fired a teacher.
Failed a student.

But not this. This is too much to ask.

Thirty years in education
I’ve learned school law.
Listened to angry parents.
Located lost school buses.
But not this.
This is too much to ask.

To make a difference.
To better kids’ lives.
That was why I went into education.
So how does this happen?
How do I . . .

“Mr. Barron, announcements are almost over.

Do you still have a special?”

I trudge toward the camera. Words caught in unwilling voice.

“I am sorry to tell you of the death of one of our

students.”

Must continue. Rumors always worse than truth.

“Anna Gonzales took her life last night.

Our sympathies to her family and friends.

Grief counselors will be available all day.”

TRANSITION

And so, life goes on, but how does it go on? How does one life really affect another? If I am here today and not tomorrow, would that make an impact on your life in any way? Anna Gonzales is dead. She committed suicide. If you could take a notebook and somehow chronicle what went through the minds of students and faculty immediately after that announcement was made, you would know what happened on the day . . .

After the Death of Anna Gonzales by Terri Fields

Damon Reingold

(Pg 9) The game doesn’t always go your way.
I know.
You can go to every practice
Even when your shoulder aches

Your ankle throbs

Your homework waits. You can do 100 hand-offs

1,000 free throws

10,000 reps And still sit on the bench

While You watch Darrith Evans

Slack off

Skip practice

Showboat for Debbie And still be part of the

Starting five. The game doesn’t always go your way.

Forget fair.

Feel forgotten. But damn it, Anna,

You don’t stop playing.

Lauren Reynolds

(Pg 21) Since September,
I sat one seat behind Anna in algebra.
Passed papers to her every day.
Studied for tons of tests together.

Though it often seemed impossible, Eventually, We always found the unknown for X.

But not this time.
This equation
Bounces against my brain.
And sneers at all attempted answers.

I know I'll re-examine the variables,
And reanalyze the unknowns, maybe forever.
But
It won't matter.

Because, Anna- I know I'll never figure out Y.

Y you didn't want to live- And Y I never noticed.

TRANSITION

According to the Center for Disease Control, suicide is responsible for almost 4,400 deaths of young people each year. The same study speculates that students aged 10 to 14 are more likely to commit suicide than other age group. Even more concerning is that the suicide of a peer is often a traumatic experience for adolescents

(many of whom are left bewildered by the lack of warning signs), often influencing other teens who are already feeling suicidal. The following two poems are by students who have already felt the closeness of death – Anna’s suicide had a dramatic impact on these vulnerable teens as well.

Kathleen Hays

(Pg 13) My brother was seven
When they told us the bad news:
It was a tumor
That had bloomed in his body
Like a weed.

Seven surgeries, and still he smiled.
We had his eighth birthday party in the hospital.
He said he could feel that he was almost well.
And we celebrated.

At nine, they said new cells had sprouted. The chemo was strong. The cancer was stronger.

But . . . in spite of the pills and the pain, In spite of the surgeries and suffering, He chose life.

And you, Anna, who had health, Chose death. How could you?

Karen Covington

(Pg 69) Mixed up memories
Of the daddy
Who introduced me to Winnie-the-Pooh.
Who sang every verse of kids' silly songs.
Who whispered the lullabies that lured me to sleep.
Mixed-up Memories
Of the dad
Who cheered my summer softball
Even if I never got a hit.
Who promised I would always be
His most perfect princess.
Mixed-up Memories
Of the father
Who guaranteed he'd be the proudest of all the parents
At my college graduation.

Who vowed he'd walk me down the aisle
even if I married at forty. Who predicted no one would be
a better Grandpa.
Of a morning last summer
When I learned
My hero had taken his own life.
When that was the truth,
Everything I understood of love and safety
Was a lie.
So, Anna, did you know
That when you kill yourself
Those you say you love,
They die too?

TRANSITION

Suicide is a permanent solution to temporary problems. And the suicide of a student affects not only other students, but the teachers and staff at a school as well. You’ve heard Principal Barron’s thoughts already and in the following poem, Ms. Mason, Anna’s English teacher explains her feelings.

Ms. Mason, English Teacher

(Pg 61) "Death be not proud."

"Do not go gentle into that good night'"

Fragments of poems I've taught.

Can't finish them--can't think how they go.

Brain too numb to truly believe.

That empty seat in the third row. Anna will be back. She must be.

Quiet, sweet'

A face framed by long lush brown hair. Almond eyes always seemed luminous. Giving no hint that this unnatural sleep would be her fate.

I've tried to teach through literature

The wonder of life.

Yet the quiet rebuke of that empty chair

Speaks louder than the most vocal of student skeptics.

I cannot take my eyes from the spot.

"There in the sudden blackness, the black pall

Of nothing, nothing, nothing--nothing at all."
```

---

## IC-1499: Agrippa (A Book of the Dead)

- Title: Agrippa (A Book of the Dead)
- Author (byline): William Gibson
- Work: Not specified
- Publisher: VDM Publishing House Ltd
- Publication date as stated: July 2010
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1650
- Already set (do not supply): none

### Source block (context only)

```text
Author: William Gibson
ISBN: 978-6131786624
Publisher: VDM Publishing House Ltd
Date (Month/Year): July 2010
```

### Introduction (context only: never use it for content warnings)

```text
This poem was not intended for reproduction. Performing it is against the author’s original plan. The beginning stages of “Agrippa” were recorded on a self-devouring floppy-disk intended to display the text only once, then eat itself. Therefore, in order to read it, one must destroy it. This storing system treated the poem much like the human mind treats its memories. The human state of forgetfulness is analyzed in “Agrippa” by William Gibson.
```

### Performance text (classify this)

```text
I hesitated before untying the bow that bound this book together.

A black book:
ALBUMS
CA. AGRIPPA
Order Extra Leaves
By Letter and Name

A Kodak album of time-burned black construction paper

The string he tied
Has been unraveled by years
and the dry weather of trunks
Like a lady's shoestring from the First World War
Its metal ferrules eaten by oxygen
Until they resemble cigarette-ash

Inside the cover he inscribed something in soft graphite
Now lost
Then his name
W.F. Gibson Jr.
and something, comma,
1924

Then he glued his Kodak prints down
And wrote under them
In chalk-like white pencil:
"Papa's saw mill, Aug. 1919."

A flat-roofed shack
Against a mountain ridge
In the foreground are tumbled boards and offcuts
He must have smelled the pitch, In August
The sweet hot reek
Of the electric saw
Biting into decades

Next the spaniel Moko
"Moko 1919"
Poses on small bench or table
Before a backyard tree
His coat is lustrous
The grass needs cutting
Beyond the tree,
In eerie Kodak clarity,
Are the summer backstairs of Wheeling,
West Virginia
Someone's left a wooden stepladder out

"Aunt Fran and [obscured]"
Although he isn't, this gent
He has a "G" belt-buckle
A lapel-device of Masonic origin
A patent propelling-pencil
A fountain-pen
And the flowers they pose behind so solidly
Are rooted in an upright length of whitewashed
concrete sewer-pipe.

Daddy had a horse named Dixie
"Ford on Dixie 1917"
A saddle-blanket marked with a single star
Corduroy jodhpurs
A western saddle
And a cloth cap
Proud and happy
As any boy could be

"Arthur and Ford fishing 1919"
Shot by an adult
(Witness the steady hand
that captures the wildflowers
the shadows on their broad straw hats
reflections of a split-rail fence)

standing opposite them,
on the far side of the pond,
amid the snake-doctors and the mud,
Kodak in hand,
Ford Sr.?

And "Moma July, 1919"
strolls beside the pond,
in white big city shoes,
Purse tucked behind her,
While either Ford or Arthur, still straw-hatted,
approaches a canvas-topped touring car.

"Moma and Mrs. Graham at fish hatchery 1919" Moma and Mrs. G. sit atop a graceful concrete arch.

"Arthur on Dixie", likewise 1919,
rather ill at ease.
On the roof behind the barn, behind him,
can be made out this cryptic mark:
H.V.J.M.[?]

"Papa's Mill 1919", my grandfather most regal amid a
wrack of
cut lumber,
might as easily be the record
of some later demolition, and
His cotton sleeves are rolled
to but not past the elbow,
striped, with a white neckband
for the attachment of a collar.
Behind him stands a cone of sawdust some thirty feet in
height.
(How that feels to tumble down,
or smells when it is wet)

II.
The mechanism: stamped black tin,
Leatherette over cardboard, bits of boxwood,
A lens
The shutter falls
Forever
Dividing that from this.

Now in high-ceiling bedrooms,
unoccupied, unvisited,
in the bottom drawers of veneered bureaus
in cool chemical darkness curl commemorative
montages of the country's World War dead,

just as I myself discovered
one other summer in an attic trunk,
and beneath that every boy's best treasure
of tarnished actual ammunition
real little bits of war
but also
the mechanism
itself.

The blued finish of firearms
is a process, controlled, derived from common
rust, but there
under so rare and uncommon a patina
that many years untouched
until I took it up
and turning, entranced, down the unpainted
stair,
to the hallway where I swear
I never heard the first shot.

The copper-jacketed slug recovered
from the bathroom's cardboard cylinder of
Morton's Salt
was undeformed
save for the faint bright marks of lands
and grooves
so hot, stilled energy,
it blistered my hand.

The gun lay on the dusty carpet. Returning in utter awe I took it so carefully up That the second shot, equally unintended, notched the hardwood banister and brought a strange bright smell of ancient sap to life in a beam of dusty sunlight. Absolutely alone in awareness of the mechanism.

Like the first time you put your mouth on a woman.

III.

"Ice Gorge at Wheeling 1917"

Iron bridge in the distance,
Beyond it a city.
Hotels where pimps went about their business
on the sidewalks of a lost world.
But the foreground is in focus,
this corner of carpenter's Gothic,
these backyards running down to the freeze.

"Steamboat on Ohio River",
its smoke foul and dark,
its year unknown,
beyond it the far bank
overgrown with factories.

"Our Wytheville House Sept. 1921"

They have moved down from Wheeling and my father wears his city clothes. Main Street is unpaved and an electric streetlamp is slung high in the frame, centered above the tracked dust on a slack wire, suggesting the way it might pitch in a strong wind, the shadows that might throw.

The house is heavy, unattractive, sheathed in stucco, not native to the region. My grandfather, who sold supplies to contractors, was prone to modern materials, which he used with wholesaler's enthusiasm. In 1921 he replaced the section of brick sidewalk in front of his house with the broad smooth slab of poured concrete, signing this improvement with a flourish, "W.F. Gibson 1921". He believed in concrete and plywood particularly. Seventy years later his signature remains, the slab floating perfectly level and charmless between mossy stretches of sweet uneven brick that knew the iron shoes of Yankee horses.

"Mama Jan. 1922" has come out to sweep the concrete with a broom. Her boots are fastened with buttons requiring a special instrument.

Ice gorge again, the Ohio, 1917. The mechanism closes. A torn clipping offers a 1957 DeSOTO FIREDOME, 4-door Sedan, torqueflite radio, heater and power steering and brakes, new w.s.w. premium tires. One owner. $1,595.

IV
He made it to the age of torqueflite radio
but not much past that, and never in that town.
That was mine to know, Main Street lined with
Rocket Eighty-eights,
the dimestore floored with wooden planks
pies under plastic in the Soda Shop,
and the mystery untold, the other thing,
sensed in the creaking of a sign after midnight
when nobody else was there.

In the talc-fine dust beneath the platform of the
Norfolk & Western
lay indian-head pennies undisturbed since
the dawn of man.

In the banks and courthouse, a fossil time prevailed, limestone centuries.

When I went up to Toronto
in the draft,
my Local Board was there on Main Street,
above a store that bought and sold pistols.
I'd once traded that man a derringer for a
Walther P-38.
The pistols were in the window
behind an amber roller-blind
like sunglasses.
I was seventeen or so but basically I guess
you just had to be a white boy.
I'd hike out to a shale pit and run
ten dollars worth of 9mm
through it, so worn you hardly
had to pull the trigger.
Bored, tried shooting
down into a distant stream but
one of them came back at me
off a round of river rock
clipping walnut twigs from a branch
two feet above my head.
So that I remembered the mechanism.

V. In the all night bus station they sold scrambled eggs to state troopers the long skinny clasp-knives called fruit knives which were pearl handled watermelon-slicers and hillbilly novelties in brown varnished wood which were made in Japan.

First I'd be sent there at night only
if Mom's carton of Camels ran out,
but gradually I came to value
the submarine light, the alien reek
of the long human haul, the strangers
straight down from Port Authority
headed for Nashville, Memphis, Miami.
Sometimes the Sheriff watched them get off
making sure they got back on.

When the colored restroom
was no longer required
they knocked open the cinderblock
and extended the magazine rack
to new dimensions,
a cool fluorescent cave of dreams
smelling faintly and forever of disinfectant,
perhaps as well of the travelled fears
of those dark uncounted others who,
moving as though contours of hot iron,
were made thus to dance
or not to dance
as the law saw fit.

There it was that I was marked out as a writer,
having discovered in that alcove
copies of certain magazines
esoteric and precious, and, yes,
I knew then, knew utterly,
the deal done in my heart forever,
though how I knew not,
nor ever have.

Walking home
through all the streets unmoving
so quiet I could hear the timers of the traffic lights a
block away:
the mechanism.
Nobody else, just the silence
spreading out
to where the long trucks groaned
on the highway
their vast brute souls in want.

VI.
There must have been a true last time
I saw the station but I don't remember
I remember the stiff black horsehide coat
gift in Tucson of a kid named Natkin
I remember the cold
I remember the Army duffle
that was lost and the black man in Buffalo
trying to sell me a fine diamond ring,
and in the coffee shop in Washington
I'd eavesdropped on a man wearing a black tie
embroidered with red roses
that I have looked for ever since.

They must have asked me something
at the border
I was admitted
somehow
and behind me swung the stamped tin shutter
across the very sky
and I went free
to find myself
mazed in Victorian brick
amid sweet tea with milk
and smoke from a cigarette called a Black Cat
and every unknown brand of chocolate
and girls with blunt-cut bangs
not even Americans
looking down from high narrow windows
on the melting snow
of the city undreamed
and on the revealed grace
of the mechanism,
no round trip.

They tore down the bus station
there's chainlink there
no buses stop at all
and I'm walking through Chiyoda-ku
in a typhoon
the fine rain horizontal
umbrella everted in the storm's Pacific breath
tonight red lanterns are battered,

laughing, in the mechanism.
```

---

## IC-1500: Almost – A Collection

- Title: Almost – A Collection
- Author (byline): Iain S. Thomas, Nora Cooper, Bianca Phipps and Maia Mayor
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1270
- Already set (do not supply): none

### Source block (context only)

```text
Author: Iain S. Thomas
ISBN: On-line Transcript
http://www.iwrotethisforyou.me/2010/11/angel-of-
almost.html
Publisher: I Wrote This For You.com
Date (Month/Year): Posted 11/17/2010
Also Published in
Author: Iain S. Thomas
Book: I Wrote This for You: 2007-2017
ISBN: 978-1449497040
Publisher: Andrews McMeel Publishing
Date: Oct 2018
Author: Nora Cooper
ISBN: On-line Transcript Posted 6/29/2015
https://slampoetryforthesoul.wordpress.com/2015/06/
29/4/comment-page-1/
Publisher: Slam Poetry for the Soul
Date (Month/Year): Performed at College Unions Poetry
Slam Invitational (CUPSI) 2015 in Richmond, VA
Author: Bianca Phipps
ISBN: On-line Transcript Posted 8/2/2016
https://slampoetryforthesoul.wordpress.com/tag/button/
Publisher: Slam Poetry for the Soul
Date (Month/Year): Performed at College Unions Poetry
Slam Invitational (CUPSI) 2014 in Boulder, CO
Also Published in
Author: Bianca Phipps
Book: Crown Noble
ISBN: 978-1943735792
Publisher: Button Poetry
Date: Aug 2020
Author: Maia Mayor
ISBN: On-line Transcript
https://www.poemhunter.com/poem/perfect-160/
Publisher: Poem Hunter.com
Date (Month/Year): Posted 6/19/2017
Also Published in
Author: Maia Mayor
Book: Get Lit Rising, Pg 8-11
ISBN: 978-1582705774
Publisher: Simon Pulse
Date: Oct 2016
```

### Introduction (context only: never use it for content warnings)

```text
Almost isn't a pretty word. In few contexts does it signify something positive. “I almost got the job, I almost passed the test.” The word almost doesn't bring about feelings of optimism and cheerfulness. Instead, it brings about feelings of coming so close, yet still being so far -- feelings of defeat, and feelings of inadequacy. It doesn't matter if you
```

### Performance text (classify this)

```text
The Angel of Almost by Iain S. Thomas
. . . . Then I was somewhere else, and it was bright.
A voice said,
"If you'd carried on practicing that song you almost got
right, you would've been great. Bigger than the Beatles."

It continued, "If you'd carried on working on that book you almost finished, it would've changed the lives of many, many people."

Then it said, "If you'd tried to reach the one you loved just a little bit more, when you almost had them, your life would've been completely different."

And I asked, "Is this what happens when I die?" And the voice said, "Almost."

almost . . . It’s the almost’s that make us yearn. It’s the almost’s that make us strive. It’s the almost’s that destroy us with regret. They’re what really tell the story. Almost – A Collection containing The Angel of Almost by Iain S. Thomas, I Won’t Write Your Obituary by Nora Cooper (excerpts); Almosts by Bianca Phipps, and Perfect by Maia Mayor (excerpts)

I Won’t Write Your Obituary by Nora Cooper

You asked if you could call to say goodbye if you were ever

really gonna kill yourself. Sure, but I won’t write your obituary.

But if you call me, I will write you letters, messages in

bottles, in cages, in orange peels, in the distance

between here and the moon, in forests and rivers and

bird songs. I will write you songs. I can’t write music, but I’ll find

Rihanna, and I’ll get her to write you music if it will

make you want to dance a little longer. I will write you 1-800-273-8255, that’s the suicide hotline;

we can call it together.

And yeah, you can call me, but I won’t tell you it’s okay,

that I forgive you.
I won’t say “goodbye” or “I love you” one last time.
You won’t leave on good terms with me,
Because I will not forgive you.
I will not hold your hand steady around a gun.
I won’t write your obituary.

So the answer to your question is “yes”. If you’re ever really gonna kill yourself, yes, please, call me.

Almosts by Bianca Phipps

I have never felt so at ease as the day you called me

precocious. I have never feared big words, only those that refuse to use

them
And the syllables rolled off your tongue like honey;
I was hooked.
Language became our vein of communication,

And I know that everybody uses language to communicate

but ours was different, As if in between the letters and the syllables there is a

secret message only we can decipher.

My days were filled with the sound of your voice. And your nights were littered with the loops of my

handwriting. We exchanged our favorite words, mine being ‘illuminated’

and yours being ‘cattywampus’; And our least favorites, mine ‘moist’ and yours ‘almost’. And when I asked you why, you said it was because

‘almost’ held failed potential, That it represented our ability to be just not good enough, That we had come to the brink of something beautiful but

fell short so many times, we crafted a word for it.

But even we, with our supposed mastery of the English

language,
were not immune to the shortcomings of our vocabularies.
Words can only help you if you speak them.
I never told you that I loved you.

You never told me that you were dying.
5 easy words that would’ve shattered our world,
“I love you, I think.”
“I have a brain tumor.”

You know, still to this day, I don’t know all the details

because medical jargon has never fit right in my mouth, And even now, 5 years later, it feels like an invasion of your

privacy. But I do know, I have pored over our conversations,

searching for the secret message you certainly tried to

send me, And I am sorry, but I only almost found it. Salt water is not good for paper and my tears warped your

words.

After some serious consideration, I’ve decided to change

my least favorite word,
Because, while ‘moist’ is gross, ‘malignant’ is malicious.
‘Malignant’ is uncontrollable.
Means a phone call in the phrase “He didn’t wake up.”
‘Malignant’ is messy and unfair and a thief.
‘Malignant’ means I never got to say ‘goodbye’.
‘Malignant’ is the cause of almost,
Because you were on the brink of something beautiful but

you couldn’t quite reach it and you fell too far. I am so sorry I wasn’t there to catch you. I hope your heaven is a library and I hope it is void of

‘almost’s’.

TRANSITION The word “almost” holds failed potential – it represents our ability to be just not good enough. Where does that start? For Maia Mayor, it echoed through her mother’s words which we hear in her poem, Perfect.

Perfect by Maia Mayor

(In a controlling mother’s voice)
Is there something wrong with you?
Where is your devotion to succeed?
I cook and I clean and I don't stop ‘til the soles of my feet

bleed.
But I'm fine.
I'm perfect.
Be perfect.
Be perfect like me.

Why are you down here?
Why are you down here when you need to be up here?
Up here with the ones who have a promising career
Who listen when information goes in one ear
and doesn't come out the other.
You'll never be up here.
You act as if the act of listening is a crime
or you would have heard me the six hundred and sixty-sixth

time I told you to STOP CHEWING ON YOUR NAILS. Stop chewing on your nails like a piece of trash.

You can't be trash. You have to be perfect. Be perfect like me.

I get up at 5 in the morning every day. I start my day the same way, worried that I'll collapse as my bones start to decay from cleaning up your scraps. Why is your room such a mess? The clothes go in the hamper. Not displayed on your bed like your lack of morals. Not littered on the floor collecting more dust than my

withered expectations.
You disregard my rules with stubborn contempt
in a substandard attempt at teenage rebellion.
But you can't be a rebel.
You're not interesting enough.
You need to obey and say 'yes' and 'okay'
You need to do it with a smile on your less than average

face. You need to try harder. Why don't you know how to smile?

You disappoint me.
You never appreciate what I do for you.
You never try to be a winner.
And you never eat your dinner.
You never eat the dinner I consistently provide for you
as I constantly remind you of the life I set aside for you.
That meal doesn't pay for itself.
I don't care if it's ideal, stop telling me how you feel.
You need to eat it.
Eat it all.
Eat it at a reasonable time with a glass of milk.
You need milk.
You need calcium like you need a catalyst for growth.
You'll never grow to be tall.
Be tall like me.
I drink my milk.
Be tall.
Be perfect.
Be perfect like me.

You need to pay more attention. Stop daydreaming.

Stop staring at the ceiling as if your one redeeming quality
lies hidden in the plaster.
You need to organize your life.
Your life is a disaster
Just like your room.
Just like your future,
Don't give me that look.
I'm just trying to help you.
I'm just trying to love you.
You have to let me love you

so that you can be perfect. Be perfect like me.
```

---

## IC-1501: America (It's Gotta Be the Cheese)

- Title: America (It's Gotta Be the Cheese)
- Author (byline): Jim Daniels and Eitan Kadosh
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 701
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jim Daniels
Book: Show and Tell: New and Selected Poems
by Jim Daniels, Pg 9
ISBN: 978-0299185848
Publisher: University of Wisconsin Press
Date (Month/Year): March 2003
Author: Eitan Kadosh
Book: Poetry Slam: The Competitive Art of Performance
Poetry, Pgs 58-59
ISBN: 978-0916397661
Publisher: Manic D Press
Date (Month/Year): Sept 2000
```

### Introduction (context only: never use it for content warnings)

```text
Fast, greasy American diners! They even make TV series about them. They are part of what makes America, well . . . America! But have you ever asked people from other countries what they think about Americans? Our school had the opportunity to host some foreign exchange students this year, and I was amazed to find out just how different they found Americans to be:

1. We talk to strangers randomly in public places.

2. Teenagers get jobs, drive cars and are

encouraged to move out of the house at 18.

(in other countries children live with their

parents until they get married)

3. In American everything is Super-Sized, Jumbo,

XXL (not true in most countries)

4. And our eating habits are weird – we eat

whenever and wherever . . . all the time!

Well, Americans may seem odd to people from other countries, but I know what’s really special about the USA and so does Eitan Kadosh.

America (It’s Gotta Be the Cheese) by Eitan Kadosh
```

### Performance text (classify this)

```text
Short-Order Cook by Jim Daniels (Pg 9) An average joe comes in and orders thirty cheeseburgers and thirty fries.

I wait for him to pay before I start cooking. He pays. He ain't no average joe.

The grill is just big enough for ten rows of three. I slap the burgers down throw two buckets of fries in the deep frier and they pop pop, spit spit. . . pssss. . . The counter girls laugh. I concentrate. It is the crucial point-- they are ready for the cheese: my fingers shake as I tear off slices toss them on the burgers/fries done/dump/ refill buckets/burgers ready/flip into buns/ beat that melting cheese/wrap burgers in plastic/ into paper bags/fries done/dump/fill thirty bags/ bring them to the counter/wipe sweat on sleeve and smile at the counter girls. I puff my chest out and bellow: Thirty cheeseburgers! Thirty fries! I grab a handful of ice, toss it in my mouth do a little dance and walk back to the grill. Pressure, responsibility, success. Thirty cheeseburgers, thirty fries.

America (It’s Gotta Be the Cheese) by Eitan Kadosh

(Pg 58-59) Everybody writes about America
And everybody paints America
Because from Jasper Johns to Allen Ginsberg
They are all looking for the same thing
Searching for the real America
The one that lies under the costumes and the war paint

that lies under the Seinfeld and Springer

under the bad *movies* and good basketball

And I am no exception Except that one night, late last week I actually found it, this elusive America -- in the dairy case at Andronico’s market Lurking beside the jacks and the cheddars, the goudas, swisses, stiltons, jarlsbergs, gorgonzolas, whole parmesan, ricottas, and myriad other imported and domestic cheeses There -- it beckoned suddenly An immaculately wrapped unbelievably orange package of American Pasteurized Process Cheese food glory God bless this country

We pasteurized We processed We manipulated this cheese until it suited our purposes This was engineered cheese This was the scientific method at work -- Jonas Salk Albert Einstein Copernicus This was smooth no lumps melted technology at work -- the light bulb phonograph model T radio television internet Nike Air rolled into one And all for $1.99

I was so moved I broke into the Pledge of Allegiance right

there and then
I bought Charlton Heston’s autobiography
Became a Daughter of the American Revolution
Oh god how I long to be wrapped in golden singles of

American cheese.
Drizzled with its salty goodness
Oh god put me in a sauna so that the cheese will melt and
when it does it will melt evenly over every square inch of

my body. Rivulets of warm cheese will run down my face like tropical

rain caress my body Oh god Take me Take me and dip me like fondue into your vat of silken American cheese food products scoop it on to me like a nacho and let it cool like a second skin oh god cheese food I will use it for everything

For breakfast melted on an English muffin for lunch in a sandwich with processed lunch meat processed salad spread on processed white bread for dinner obliterating my broccoli at bed on my toothbrush so my breath will be cheesy American fresh in the morning I will gargle with it and wash my face with a congealed vat of the stuff I keep on my sink and smear on like Noxema. I will cook my girlfriend romantic dinners in which every course will concisely and creatively utilize and emphasize our most holy of sacraments. Because it’s gotta be the cheese.

America land of the free – it’s gotta be the cheese Home of the brave – it’s gotta be the cheese Land of possibility, opportunity and the certain unalienable

rights of manifest destiny – it’s gotta be the cheese who shot J.F.K, J.R. Ewing, J.C. Penney – it’s gotta be the

cheese

the WWF – it’s gotta be the cheese
Kurt Cobain – it’s gotta be the cheese
Jerry Lewis – it’s gotta be the cheese
The hydrogen bomb the neutron bomb and pantyhose

Mom the flag and apple pie It’s gotta be the cheese

Source information for Introduction https://blog.icesusa.org/americans-do-the-strangest-things
```

---

## IC-1502: America Poem

- Title: America Poem
- Author (byline): S.A. Griffin
- Work: Outlaw Bible of American Poetry, Pg 573-575
- Publisher: Thunder's Mouth Press
- Publication date as stated: Oct 1999
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 590
- Already set (do not supply): none

### Source block (context only)

```text
Author: S.A. Griffin
Book: Outlaw Bible of American Poetry, Pg 573-575
ISBN: 978-1560252276
Publisher: Thunder's Mouth Press
Date (Month/Year): Oct 1999
```

### Introduction (context only: never use it for content warnings)

```text
Imagine a slide show of images . . . images that capture America in all its glory and all its shame. A slide show of images . . . dependent on the viewer to assign value to each image, to catalog and to judge America from various perspectives. This is what S.A. Griffin has achieved but not with visual images . . . this poet takes the challenge one step further and paints his pictures with words. So, sit back, open your mind, your imagination and your memory of what is America and how it has changed since the turn of the century.

America Poem by S.A. Griffin
```

### Performance text (classify this)

```text
(Pg 573-575) it was the pledge of allegiance
everyday
to the flag
it was the pledge of allegiance
it was our country 'tis of thee
New Yorkers that never saw a cow
cows that never saw a city
mothers fathers sons and daughters
the born and unborn
it was a house that was always there
like wood and brick eternity
it was gold silver oil
it was t.v. that was American
it was "made in the U.S.A."
it was small towns that was somewhere else
big cities that was everywhere else

that was somewhere

it was a wheel it was wheels it was the Wizard of Oz white man ethic that snuck into grandma's womb and exploded like Pandora's box over the rising sun

all hail the glory that was God!

it was deliverance
lovers and lies that were promises
birds piloting over silent streams of sky
it was dreams and dreaming
and it was flying higher than God
it was faith
pure and uncut
it was spent cartridges that hammered our dreams
fast to reality
it was Monroe
Garbo
Harpo
Chico
Groucho
Presley
Gone With The Wind
The Babe and baseball
hearts filled with hotdogs and homeruns
jazz pouring out of speakeasies like
hot pepper sauce over flat tongues
F.D.R.
J.F.K.
Gary Cooper and High Noon
Hank Williams
Pete Seeger
Huddie Ledbetter and
America
was an eager young debutante
in soft white and pink crinoline and taffeta dresses
and waves of waterfall tresses
in love with
storybook princes and princesses

it was "I have been to the mountaintop" assassinations and angry black clouds of riot

it was the coming of age of Harlow and Hitler and the bastardization of Nietzche by Hitler and Hollywood blonde breasts sagging into fading hairlines it was desperate to be un-understood leaders who wanted to follow

it was a generation of giants and giantesses
spawned by chrome gods and goddesses
in the backfields of glorious houses
Chevys
Fords
Mercurys
Oldsmobiles
Chryslers and
Buicks that longed to become Cadillacs

it was men who hated men
pathetic pawns of power
begging for manhood
borne of paper
thrusting accusations of
"communist, red f*gg*t, n***, wop, spic, kike, white trash,
whore"

it was a time it is a time it is America

it is a can opener
a microwave
a long distance telephone call
satellite Jesus crucified by capitalist commanders
hip new fads of neon nostalgia
sitcoms t.v. dinners
used used cars
fast fast cars
55 miles per hour
fast fast food
and the killing that rages unresolved in the
french fried inside and outside

the headlines the hairlines the waistlines

it is the dead inside of a quarter pounder with cheese and the sesame seeds of love that should have

it is valleys of vines
plains of corn and wheat and dyed red meat
cut picture perfect
estrogen fed chickens with centerfold breasts
it is a single stalk of corn
growing out of a crack in the sidewalk
on a Hollywood street corner
it is forty years of fallout
and four hundred more
it is the one that got away
the soulmate
perfect one
it is the perfection of imperfection
and the searching for truth
it is the heartland

it is America

it is the great love and admiration
the stifling addled ambition
it is the people and the truth
which is somewhere searching in a
rambling car that only stops for
dollar gas
hot coffee
then races off again over the stoic face of
what is
America
```

---

## IC-1503: America, Reloading – A Program

- Title: America, Reloading – A Program
- Author (byline): Harryette Mullen, Andrea Gibson, and Richard Blanco
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1166
- Already set (do not supply): none

### Source block (context only)

```text
Author: Harryette Mullen
Book: Sleeping with the Dictionary, Pg 77
ISBN: 978-1943735426
Publisher: University of California Press
Date (Month/Year): Feb 2002
also online at
https://www.poetryfoundation.org/poems/145281/we-are-
not-responsible
Author: Andrea Gibson
Book: Lord of the Butterflies, Pgs 51-54
ISBN: 978-1943735426
Publisher: Button Poetry
Date (Month/Year): Nov 2018
Author: Richard Blanco
Book: How to Love a Country: Poems, Pg 63
ISBN: 978-0807025918
Publisher: Beacon Press
Date (Month/Year): March 2019
also online at
https://www.poetryfoundation.org/poems/148210/seventeen-
funerals
```

### Introduction (context only: never use it for content warnings)

```text
We can’t be held responsible. (Sigh) But until we are ready to accept responsibility for the growing number of mass and school shootings in America -- until we are ready to do more than offer thoughts and prayers - - we will live in a society of petrified people, terrified children, followed only by the brief silence of . . .

America, Reloading – A Program with poems by Harryette Mullen, Andrea Gibson and Richard Blanco
```

### Performance text (classify this)

```text
We Are Not Responsible by Harryette Mullen (Pg 77) We are not responsible for your lost or stolen relatives. We cannot guarantee your safety if you disobey our instructions. We do not endorse the causes or claims of people begging for handouts. We reserve the right to refuse service to anyone. Your ticket does not guarantee that we will honor your reservations. In order to facilitate our procedures, please limit your carrying on. Before taking off, please extinguish all smoldering resentments. If you cannot understand English, you will be moved out of the way. In the event of a loss, you’d better look out for yourself. Your insurance was cancelled because we can no longer handle your frightful claims. Our handlers lost your luggage and we are unable to find the key to your legal case. You were detained for interrogation because you fit the profile. You are not presumed to be innocent if the police have reason to suspect you are carrying a concealed wallet. It’s not our fault you were born wearing a gang color. It is not our obligation to inform you of your rights. Step aside, please, while our officer inspects your bad attitude. You have no rights we are bound to respect. Please remain calm, or we can’t be held responsible for what happens to you.

America, Reloading by Andrea Gibson

(Pg 51-54) Mostly because of dying stars,
scientists say space smells like barbecue
and gunpowder. Which is to say
space smells like the United States --

a holiday where we celebrate the independence
of machine guns, how anyone can buy
a cemetery at a sporting goods store
on their 18th birthday

and open carry it to an elementary school
where children are learning tears
don't fall in space. Weightless, without
gravity, they never leave the eye.

Is that what happens to the NRA?
they ask after they’ve watched the bodies
of half their class use every red crayon
in the universe to scream goodbye.

Do the NRA’s tears not drop

because they're astronauts?

How does a parent tell a 6-year-old
that gun sales spike every time
our right to bear massacres
makes a coroner faint,

makes a medical examiner say, I can't,

my god, I can't.

But we can, can't we, America?
Each election, don't we say can
stomach the boy loading a black hole
into his backpack and unloading it

in the high school hallway
on Valentine's Day? It would take
light years to count how many times
the terrified texted I LOVE YOU,
I LOVE YOU, I LOVE YOU
in Parkland, Florida
while the NRA kept crying

in space.

My friend, a second grade teacher,
is instructed to practice hiding her children
in the closet. Twenty-three 7-year-olds
huddle holding their breath.

Holding your breath in space

is the fastest way to die.

The lungs explode in that vacuum
almost as quickly as an AR-15
can make blood-dust
of a closet door.

Of the twenty children murdered at Sandy Hook,
not one of them needed an ambulance.
That's how dead they were.
That's how well the Second Amendment works.

Because there is no air, it is silent in space.
But not as silent as the Christians
on the Senate floor while twenty more families
are asked if they would like to talk

to a priest. Christ could tear the nails
from his hands and scrape them down
a shrapnel-battered chalkboard
and they’d still be praying for their bank accounts.

After Columbine, parents were notified About their children in tiny conference rooms. One family said, We could hear the family before us screaming, and we knew we were next.

Now loved ones check Facebook
to see who is dead. A mother's status is, I CAN’T
REACH MY DAUGHTER. I CAN’T REACH
MY DAUGHTER. Decades after her child is slaughtered

in the cafeteria
that thought will still be
tearing her from her bed -- I CAN’T
REACH MY DAUGHTER –

The footprints left by astronauts
on the moon are permanent.
They will never ever go away
like the grief of a father

identifying his son by his shoes
because the rest of his son's body
was out-lobbied by the NRA, by suits
whispering into the ears of Washington –
this is what we mean
by freedom and justice, the names
of our cities becoming synonymous
with babies being buried

like seeds in the greed gardens of the wealthy. But you should know your teacher was a hero, we say, her body was found bunkering a group of your friends.

And that's as happy as the ending gets
right now. The heroes almost always dead.
The flag at half mass grave.
Children huddled

in basements, trying to tear off their ears on the Fourth of July because the fireworks sound like the day everyone died crying, died with gravity pouring

their next 80 birthdays from their eyes, while America reloaded,

and moved on

to the next.

Seventeen Funerals by Richard Blanco (Pg 63) Seventeen suns rising in seventeen bedroom windows. Thirty-four eyes blooming open with the light of one more morning. Seventeen reflections in the bathroom mirror. Seventeen backpacks or briefcases stuffed with textbooks or lesson plans. Seventeen good mornings at kitchen breakfasts and seventeen goodbyes at front doors. Seventeen drives through palm-lined streets and miles of crammed highways to Marjory Stoneman Douglas High School at 5901 Pine Island Road. The first bell ringing-in one last school day on February fourteenth, 2018. Seventeen echoes of footsteps down hallways for five class periods: algebra, poetry, biology, art, history. Seventeen hands writing on whiteboards or taking notes at their desks until the first gunshot at 2:21pm. One AR-15 rifle in the hands of a nineteen-year-old mind turning hate for himself into hate for others, into one hundred fifty bullets fired in six minutes through building number twelve. Seventeen dead carried down hallways they walked, past cases of trophies they won, flyers for clubs they belonged to, lockers they won’t open again. Seventeen Valentine’s Day dates broken and cards unopened. Seventeen bodies to identify, dozens of photo albums to page through and remember their lives. Seventeen caskets and burial garments to choose for them. Seventeen funerals to attend in twelve days. Seventeen graves dug and headstones placed—all marked with the same date of death. Seventeen names: Alyssa. Helena. Scott. Martin—seventeen absentees forever—Nicholas. Aaron. Jamie. Luke—seventeen closets to clear out— Christopher. Cara. Gina. Joaquin—seventeen empty beds— Alaina. Meadow. Alex. Carmen. Peter—seventeen reasons to rebel with the hope these will be the last seventeen to be taken by one of *three-hundred-ninety-three-million guns in America. *They were not*

For more statistical data about school shootings, see the K-12 School Shooting Database at https://k12ssdb.org/

* Statistic confirmed at How Many Gun Owners are in America (2024 Statistics) on 8/9/2024 https://ammo.com/articles/how-many-gun-owners-in-america#:~:text=Based%20on%20NICS%20background% 20data,owned%20firearms%20in%20the%20U.S.
```

---

## IC-1504: America the Beautiful – A Program

- Title: America the Beautiful – A Program
- Author (byline): Katharine Lee Bates; Langston
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 643
- Already set (do not supply): none

### Source block (context only)

```text
Author: Katharine Lee Bates
ISBN: 978-0689852459
Publisher: Atheneum Books for Young Readers
Date (Month/Year): June 2002
Author: Langston Hughes
Book: Collected Poems of Langston Hughes
ISBN: 978-0679764083
Publisher: Vintage
Date (Month/Year): Oct 1995
Author: Various Authors (denoted within poem)
Book: Russell Simmons Def Poetry Jam on Broadway . . .
and More
ISBN: 978-0743476218
Publisher: Atria Books
Date (Month/Year): Aug 2003
```

### Introduction (context only: never use it for content warnings)

```text
In February of 2014, Coca Cola’s entry into the Super Bowl ad campaign had a message that was a Coke Classic: it celebrated the many kinds, colors, lifestyles and origins of Americans. Over a collage of American faces, young, old, brown, white, straight, gay, in cowboy hats and hijabs, played a patriotic song -- “America the Beautiful” sung in eight languages.

Who knew the commercial would cause such an uproar? Conservatives instantly lit up social media with objections -- many vowing to boycott the soda company’s products as “un-American.”

America the Beautiful – A Program of poems by Katharine Lee Bates (circa 1900); Langston Hughes (circa 1960) and the Poets of Russell Simmons Def Poetry Jam on Broadway

(circa 2003).
```

### Performance text (classify this)

```text
Hughes and the Poets of Russell Simmons Def Poetry Jam on Broadway

America the Beautiful by Katharine Lee Bates

(May choose to sing his stanza)
O beautiful for spacious skies,
For amber waves of grain,
For purple mountain majesties
Above the fruited plain!
America! America!
God shed His grace on thee,
And crown thy good with brotherhood
From sea to shining sea!

I, Too, Sing America by Langston Hughes
I, too, sing America.
I am the darker brother.
They send me to eat in the kitchen
When company comes,
But I laugh,
And eat well,
And grow strong.

Tomorrow,
I’ll be at the table
When company comes.
Nobody’ll dare
Say to me,
“Eat in the kitchen,"
Then.

Besides,
They’ll see how beautiful I am
And be ashamed—
I, too, am America.

TRANSITION

A merica -- no other place in the world has such a diverse population. And yet, culturally speaking, we as a nation have difficulty thinking of anybody who doesn’t have white skin and whose first language isn’t English as “American.” Just how beautiful is America?

I Write America

(Poets for each stanza denoted within)

I write America a Dear John letter
I’m not leaving but things have to
get better
Learn to pronounce my name correctly
I am a taxpayer
and brick layer
These poems are us
Our history,
you have no choice but to recognize
me and mine
for the fire next time,
I rewrite America -- Suheir Hammad

I write America for the people just like me,
too busy blamin’ instead of claiming
that America is the best place to be.
This is my family
Yea, my kin folk have problems and issues
like every family does
but I’m going to make my difference right
here
for us
I write America -- Poetri

I dream America for the day I won’t have
to hyphenate my identity
For the day everyone will be tri-lingual
For the day I won’t be asked where I’m
really from or complimented on how
well I speak English
For the day the American dream includes me
I write America -- Mayda Del Valle

I write America for the
not-so-funny-face
of Will and Grace
That dear old, queer old USA
Langston Hughes, Zora Neale Hurston,
James Baldwin . . .
For the voices who broke the silence
I write America. -- Staceyann Chin

I will always write America for the poor people And I’m not trying to tell you how to live but vanity will kill you so will MTV Cribs For the poor people, I write America. -- Lemon

I write America
love notes in my protest poems
Because this is my home
Because between the shining seas
and redwood forests
I am one voice in a chorus
composing ourselves from wounded knees
We write America
because even when it’s not
we assume that it’s free
We write America. -- Steve Colman

I would write America
but I’m too suspicious
I know
the powers that be
are vicious
and they wouldn’t
have a problem
sacrificing the lives
of twenty-five hundred people
at the bottom of Manhattan
in order
to boost their economy.
See, they’ve been sacrificing the lives
of the youth around my way
to fill their filthy pockets
since I can remember
So instead
I just watch America. -- Black Ice

I have to write America
Because no one else will do it for me
Chinatown is America,
Bruce Lee is America
my mother is America.
My people
you should never have to accent less
never view yourselves as other
and never have to
fear internment again
I am America. -- Beau Sia

I CHANGE AMERICA . . . by living life to the fullest
Fight those who try to pull s*** and always
resist the unjust system
I serve only Him or She, so
I write to free my brothers and sisters
no matter what the color.
Speak only the truth
so the blind can see
WE MUST MAKE AMERICA
A TRUE DEMOCRACY -- Georgia Me
```

---

## IC-1505: Angel Island – Words from

- Title: Angel Island – Words from
- Author (byline): Not specified
- Work: Island: Poetry and History of Chinese Immigrants on Angel Island, 1910-1940
- Publisher: University of Washington Press
- Publication date as stated: May 1991
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 893
- Already set (do not supply): none

### Source block (context only)

```text
Author: Poetry Translated by Genny Lim
Book: Island: Poetry and History of Chinese Immigrants
on Angel Island, 1910-1940
ISBN: 978-0295971094
Publisher: University of Washington Press
Date (Month/Year): May 1991
```

### Introduction (context only: never use it for content warnings)

```text
Between 1910 and 1940 thousands of Chinese were detained and interrogated on Angel Island for weeks, months or years Separated from family, they lived in crowded, squalid communal living quarters. The ordeal left an indelible mark on the detainees. Their feelings of anger, frustration, uncertainty, hope and despair filled the walls of the detention barrack. Today more than 220 poems have been recorded and preserved. Most are undated and unsigned, presumably for fear of retribution.

Angel Island – Words from the Barracks; poetry translated by Genny Lim
```

### Performance text (classify this)

```text
Poetry translated by Genny Lim

(38 / #unknown; combined) Over a hundred poems

are on the walls. They are all cries of suffering and sadness What can one sad person say to another? Gain or lose, how is one to know what is predestined? Rich or poor, who is to say it is not the will of Heaven? Why should one complain if he is detained and

imprisoned here? From ancient times, heroes often were the first ones to

face adversity. The day that I am rid of this prison and become

successful I must remember that this chapter once existed . . .

(10) Encouraging the Traveler Not without hard work were one thousand pieces of

gold dug up and gathered together. There were words of farewell to the parents, but the

throat choked up first. There were many feelings, many tears flowing face to

face, when parting with the wife.
Waves big as mountains often astonished this traveler.
Do not forget this day when you land ashore.
Push yourself ahead and do not be lazy or idle.

-- One Named Huie from Heungshan (7) Originally, I had intended to come to America last

year. I ate wind and tasted waves for more than twenty days. Fortunately, I arrived safely on the American continent. I thought I could land in a few days. How was I to know I would become a prisoner

suffering? The barbarians' abuse is really difficult to take. When my family's circumstances stir my emotions,

a double stream of tears flows. I only wish I can land in San Francisco soon, Thus sparing me this additional sorrow here.

(3) Sitting alone in the customs office,
How could my heart not ache?
Had my family not been poor,
I would not have traveled far away from home.
It was my elder brother who urged me
To embark on a voyage to this shore.
The black devil here is unjust-
He forces the Chinese to clean the floor.
Two meals a day are provided,
But I wonder, when will I be homeward bound?

- Lee from Toishan District, September 4, 1911

(48) I thoroughly hate the barbarians because they

do not respect justice. They continually promulgate harsh laws to show off

their prowess. They oppress the overseas Chinese and also violate

treaties.

(56) The young children do not yet know worry. Arriving at the Golden Mountain, they were

imprisoned in the wooden building. Not understanding the sad and miserable situation

before their eyes, They must play all day like calves.

(24) Random Thoughts Deep at Night In the quiet of night, I heard, faintly, the whistling of

wind. The forms and shadows saddened me; upon seeing the

landscape, I composed a poem. The floating clouds, the fog, darken the sky.

The moon shines faintly as the insects chirp. Grief and bitterness entwined are heaven sent. The sad person sits alone, leaning by a window.

--Written by Yee of Toishan

(24) After leaping into prison, I cannot come out. From endless sorrows, tears and blood streak. The Jingwei 1 bird carries gravel to fill its old grudge. The migrating wild goose complains to the moon,

mourning his harried life. When Ziqing 2 was in distant lands, who pitied and

inquired after him? When Ruan Ji 3 reached the end of the road, he shed

futile tears. The scented grass and hidden orchids complain of

withering and falling. When may I be allowed to soar at my own pleasing?

-- Written by Lee Gengbo of Toishan

(43) Imprisoned in the wooden building day after day, My freedom withheld; how can I bear to talk about it? I look to see who is happy, but they only sit quietly.

I am anxious and depressed and cannot fall asleep. The days are long and the bottle constantly empty; my

sad mood, even so, is not dispelled. Nights are long and the pillow cold; who can pity my

loneliness? After experiencing such loneliness and sorrow, Why not just return home and learn to plow the fields?

(49) I cannot bear to describe the harsh treatment

by the doctors. Being stabbed for blood samples and examined for

hookworms4 was even more pitiful. After taking the medicine, I also drank liquid, Like a dumb person eating the huanglian. 5

(50) It is indeed pitiable the harsh treatment of our

fellow countrymen. The doctor extracting blood caused us the greatest

anguish. Our stomachs are full of grievances, but to whom can

we tell them? We can but pace to and fro, scratch our heads, and

question the blue sky.

(52) The barbarian issued orders to change rooms. Running up and down, my breath grew short. It was like warfare, when people's minds are

bewildered.

(53) I have lingered here three days moving again and

again. It is difficult to compare this to the peacefulness at

home. Life need not be so demeaning. Rushing about so much, smoke came out of my mouth.

(55) Shocking news, truly sad, reached my ears. We

mourn you. When will they wrap your corpse for

return?
You cannot close your eyes.
Whom are you depending on to voice your complaints?
If you had foresight, you should have regretted coming

here. Now you will be forever sad and forever resentful. Thinking of the village, one can only futilely face the

Terrace for Gazing Homeward. Before you could fulfill your ambition, you were buried

beneath clay and earth. I know that even death could not destroy your

ambition.
```

---

## IC-1506: The Anthem (If famous poets had written “The Star- Spangled Banner”)

- Title: The Anthem (If famous poets had written “The Star- Spangled Banner”)
- Author (byline): Garrison Keillor
- Work: Atlantic Monthly Magazine (Volume 297)
- Publisher: Atlantic Monthly Magazine
- Publication date as stated: January/February 2006
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 739
- Already set (do not supply): none

### Source block (context only)

```text
Author: Garrison Keillor
Book: Atlantic Monthly Magazine (Volume 297)
ISBN: B00007987Y
Publisher: Atlantic Monthly Magazine
Date (Month/Year): January/February 2006
```

### Introduction (context only: never use it for content warnings)

```text
Since World War II the Star-Spangled Banner has become a permanent fixture at sports events in the United States. And over the last 30 years artists have gradually made non-traditional renditions of the song commonplace. Frequency doesn't necessarily breed acceptance, however. While America may seem less surprised by new renditions of the national anthem, it still considers the song's performance a litmus test for patriotism. Garrison Keillor takes this rendition tradition on step further in The Anthem: If famous poets had written “The Star-Spangled Banner.”
```

### Performance text (classify this)

```text
Oh, say can you see by the dawn's early light

What so proudly we hailed at the twilight's last gleaming? Whose broad stripes and bright stars thru the perilous fight, O'er the ramparts we watched were so gallantly streaming?

And the rocket's red glare, the bombs bursting in air,

Gave proof through the night that our flag was still there.

Oh, say does that star-spangled banner yet wave

O'er the land of the free and the home of the brave?

Walt Whitman . . . Here on the shore of Baltimore observing the barrage of rockets and bombs from the man o' war, The gunnery mates stripp'd to the waist and glistening with sweat, Shouting each to the other and working together in close drill, Ramming the powder charge and then the enormous projectile, Each of them a man like myself and possessed of secret longings, Each of them comely and well-appointed, Especially the tall one on the left with black curls and taut abdominal muscles, Who looks so long and lovingly at me, a stranger in big boots, And I return his gaze—O aficionado, come, take my hand— Leave your cannonading and we shall travel the open road Where there are no banners except of affection and the love of dear comrades.

Emily Dickinson . . . The Banner—that we watched in Air So Proudly as it Gleamed Was Proven by the Rocket Glare Or so to us it Seemed—

And so we waited for the Dawn
To see if it still flew
Or if—in Tatters—it is Gone—
As happened once—with You.

I woke up—at the Matin Bell—
A vast and empty Bed—
The Pillow bore—the slightest smell
Of Oil—from your Head.

A fleeting Phantasy—perhaps—
The Ghost of—Not To Be—
And Postmen—in their Crimson Caps—
Aim their Artillery.

Robert Frost . . . Whose flag this is I think I know His house is being bombed now though He will not see that I have come To watch the twilight's ebbing glow.

My little horse must think it dumb,
The cannons' pandemonium,
The rockets bursting in the air,
The sound of bugle, fife, and drum,

He turns and shakes his derrière To show me that he doesn't care Who takes this battle flag or why, When in the redness of the glare

I see the banner flying high
Through the tumult in the sky
And, knowing all is now okay,
We walk away, my horse and I.

The flag is lovely, hip hooray, But I have things to do today, Some here and others far away, Before I stop to hit the hay.

E. E. Cummings . . .
She being brand
New he threw
A flag over h
Er & began
The bombard
Ment & was soon
Rocketing
A (long) & feeling
Braveandfreeand(proudly)perilous
Can you see? Said he
Oui oui, said she
And it was love and it was
Spring and roses and it was
Dawn &
He
B
U
R
S
T
Into song.

William Carlos Williams . . .
This is just to say
I have taken
The flag
That was
Flying

And which
You probably expected
To see
This morning
Forgive me
It was beautiful
So free
And so brave

Billy Collins . . . On the ship, I sit and wait for the dawn In the midst of the bombs and rockets and so forth, A prisoner of these British marines who might shoot me, You never know in a situation like this.

Like so many great moments in history,
You come upon it without meaning to.
You're a lawyer who goes to negotiate for the release of
a prisoner
And voilà you become one yourself.

There is this incredibly perilous fight going on
And I suppose a person should be thinking about
freedom
Or bravery but I must admit
I would give anything for a cup of coffee right now.

Like a Starbucks made by a girl in a striped blouse,
A latte streaming and gleaming.
But that seems less likely at the moment
Than Betsy Ross doing a striptease, stripe by stripe.

The graceful arc of the rockets, like Don
Larsen's curve ball for the Bronx Bombers.
He was a hero and then suddenly he was gone.
I wonder what's going to happen to that flag.
Somebody could write a poem about this,
Something to mark this whole thing that's going on,
But if they did, probably they shouldn't include
The coffee and the part about Betsy dropping the flag.
```

---

## IC-1507: The Art of Teaching

- Title: The Art of Teaching
- Author (byline): Joshua Sands
- Work: Turning Points
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 831
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joshua Sands
Book: Turning Points
Publisher: Tichenor Publishing
ISBN: 978-0742117013
Date: 2001
```

### Introduction (context only: never use it for content warnings)

```text
Once I perfect The Art of Teaching by Joshua Sands.
```

### Performance text (classify this)

```text
When I was seven
my Sunday school teacher first taught me the story of
Joseph
and his coat of many colors.
The story of Job is the popular story of Biblical
perseverance;
I prefer Joseph.
Ostracized by his own brothers
sent away to be a slave
Predicting great famines
yet for years,
no one knew

no one cared. One day they realized Joseph's gifts and there was much rejoicing.

As I regularly inhabit classroom 208 I envision myself a modern-day Joseph.

I believe I can teach. I await the day when my gifts will be realized. There will be much rejoicing.

Gradually, I lose control. 30 teachers

650 students.
Hardly fair.
They take control
like a modern-day Trojan Horse
One by one, they jump out of the horse
into 208
into 208
into 208.
The Trojans are in the classroom
assigned seats.
Plotting
Plotting
Plotting
a takeover.
Plotting
Plotting
Plotting
My destruction.
I don't understand them
Any of them.
All of them.
I watch what they watch
read what they read
I listen.
Gradua11y, I lose Control.
Can I qo to the bathroom?
Tell him to stop
Is this for a qrade?
When will I need to learn this?
What time is it?
What time is it?
What time is it?
It's half past Puff Daddy.

Do you know where your kids are? After school:

parent-teacher conferences. Notice: it's always

parent - teacher
never
teacher-parent.
Whv?
Because it's the parent approaching the teacher
the parent hearing the news
the parent finding out
what's going on
what's going on

what's going on
The parents time to catch up:
lis, he's reading at a fourth grade level.
lis, we're doing all we can.
lis, I'm sure he's doing his best.

lis, I'll do more.
Just once
let's have
teacher-parent conferences
where the teacher shows up at the door
and the teacher hears the news
the teacher finds out
what's going on
the teacher finds out
why this kid never gets a haircut
why this kid falls asleep in class
why this kid got caught with a Hustler in his locker
why this kid thinks farting is so funny
why this kid is part of the Trojan Horse.
I watch what they watch:
I see guns blazing
firing
taking over
taking over
taking over
I watch what they watch:
I see men calling each
other *BLEEP*
I see kids laughing
because they said *BLEEP*.
I watch and they're
taking over
taking over
taking over
What time is it?
What time is it?
What time is it?

It's quarter 'til Menace II Society.
Do you know where your kids are?
Eyeryone wants to know
what's going on?
what's going on?
what's going on?
You're not listening
Not listening
Not listening.
He's pulling the trigger.
Don't you get it?
He's pulling the trigger.

He's back in the Trojan Horse now.
He's reloading.
An observer watches my class,
Gradually I lose control.
The Trojans are rioting today
It's a show.
Didn't you know?
The observer tells me:
Well, I think you need to try this
Read this
Watch this
Rework this
Be better prepared for this
for this
for this.
I've finally figured it out:
There are people who know what to do.
But they're all busy observing.
Gradually,
gradually,
I've lost control.
They're no longer the Trojans
they're the *BLEEP*.

I said *BLEEP*
*BLEEP*
Isn't that funny?
Laugh
Isn’t it that funny?
They will sit in their seats.
They will do their work.
They will like it.
They will do it without laughing
Farting
Giggling
Passing notes
Asking to go pee
Whispering
Complaining.
They will do it or else
for 208 is my home
Don't deface my home.

What's going on?
What's going on?
What's going on?
Stay away from 208.
I'm armed and I'm dangerous.
Stay away from 208
unless you really
read Romeo and Juliet
and are prepared to discuss it
and mean it
and like it.
Stay away from 208
because I'm gonna teach
and you don't want me to.
You can charge into 204
205
206
207
But stay away from 208.
It's my home.

I am Joseph
waiting for the day
when I'll be told to come home.
C'mon
it was all a bad joke
You weren't meant to be a slave
You have visions
Talents
Skills
Things we need.
Come home.
Come home.
Come home.
And I wait to come home.
I wait for the meaning
the moral
the message
the reason why I went through this
Why I paid the penance.
Who would understand?
Joseph.

Joseph would put his arms
around me and say it's OK.
It's over now.
Come home.
This is why I must join Joseph.
This is why I must go.
There must be other jobs.
I'll find one.
208 is not my home.
It never was.
What time is it?
What time is it?
What time is it?
It's time to change our tune.
Do you know where your kids are?
```

---

## IC-1508: Autopsy (Selections from)

- Title: Autopsy (Selections from)
- Author (byline): Donte Collins
- Work: Not specified
- Publisher: Button Poetry
- Publication date as stated: July 2017
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1168
- Already set (do not supply): none

### Source block (context only)

```text
Author: Donte Collins
ISBN: 978-1943735112
Publisher: Button Poetry
Date (Month/Year): July 2017
```

### Introduction (context only: never use it for content warnings)

```text
Perhaps writer David Ferguson words will help explain how difficult it is to cope with the loss of your mother: “The magnitude and bottomlessness of the pain you feel is a testament to the love you shared. And while I don’t ever expect to arrive at a point in life where I’m alright with the fact that my mother is gone, I know that I am so, so lucky to have loved and been loved that much by anyone.”

Selections from Autopsy by Donte Collins
```

### Performance text (classify this)

```text
Death Ain’t Nothing but a Song

My mother moved out of her body decided it was no longer worthy

it couldn’t contain her laughter

she couldn’t obey the house

rules of human her spirit,

that young & fresh fever wanted
to call the night her dance club
wanted to try on new clothes
stay out later

my mother now wears the world

dresses herself with the tall grass

blushes her cheeks with red clay

she laughs & a forest fire awakens she laughs & every mountain bows to her sharp thunder she laughs

& each cicada begins to

sing last

night Saint Paul was cloaked in

steam:

fog traveled from some distant

heat.

no, I think you’ve got it all wrong. Someone must have asked my mother

to

dance

The Orphan Performs an Autopsy on the Garden

there are many ways to pull a weed but only one will keep the garden clean come the end of summer

your mother will be dead

13 years - 2 months - 11 days - 7 hours from now

& you curse her beneath your breath. flick beaded sweat

gathered like pearls at the crease of your brow & continue to rip up

the earth

why does heat make the body confess what it will not do

otherwise? drunk on july & nerve you rip handfuls of color from along

the fence thorns like brief alarms warning your fevered temper of

what blood will soon stain your teeth. never. ruin. your. mother’s. new.

plants

your mother will be dead

3 years - 6 months - 9 hours from now

why does heat make the body confess what it will not do

otherwise? sneaking out of a house built of creaking wood can only end

with red smeared across checkered linoleum. can only cause a

mother to lock the doors from the outside. deadbolt & don’t

disrespect my house again! basement stairs & belt buckle branded—a birthmark

across your sprouting back. see me: a field of dry &

rebellious wheat thrashing until flaming. until ash

your mother will be dead

3 days - 6 hours - 14 minutes from now

& wants to take you to lunch. insists on giving you all your

old inhalers, face-cream, old shoes. says you never know. says if i died i

wouldn’t know what to do with all of this—points—the china

cabinet, a small museum of memories. says we laughed a lot, too. our faces

framed & frozen to happy. says if you & lamar don’t know i love you,

know now & now she is weeping. see her: a black sky cracking,

offering water: as if to say: forgiveness is a fertile thing—is what makes

tomorrow grow

& / just / like / that / she’s / dead / a / porch / light / gone /

out / a wind / chime / songless / sunken / into / soil / you /

untethered / 19 returning / to / an / empty / home / find / your / hands /

busy / in an / abandoned / garden / joy / must / be / a / flower /

among / all of / this / knotted / agony / there / are / many / ways / to /

pull / grief from / the / body / but / only / one / will / keep / the / boy/

alive

TRANSITION

And as you struggle to accept the grief, to give yourself grace to mourn . . . the wheels of society are working to find a new family to care for you.

Words that begin with the letter A: Autopsy . . . . Adoption

Alternate Beginning: The Game

is simple & played with my brother

in the backseat, as each home flutters

past you point & say yes or no

yes, you would live there

no, you would not maybe a home with grass, the good kind, the shiny kind, the kind outside the courthouse. the kind that reaches all the way to the

curb: no dirt patches, no dead bulking brown, no yellow weeded intruders spotting through crumbling cement, no

abandoned sideways tricycle, rain rusted & waiting & waiting

maybe a home with a tree fit for five-year-old feet, a garden even, visible from the street. maybe our newer mother will grow things. good things. the nutritious kind. the kind that chemicals

cannot produce. the kind that doesn’t kindle or make lamar, my

older bro, cough like he does. like a factory in his chest or a fight

maybe a home with windows, ones you can see both in & out of, &

curtains blue & wavy, then sometimes it’ll be like you’re near the

water & river weed & sleep will come easy. unlike breath, unlike those men with badges on their chests always upturning

the mattress dumping out cabinets, like they searching for something

bad something they need, something bagged & that easily

burns

maybe a home with brick or blue plaster with ribbons tied to the railing,

maybe they’ll know we’re coming, maybe they won’t know where

we’ve been then it’ll be like we’re new & nameless. a porch swing. A

welcome mat. yes, yes i ask the man driving if adoption hurts like a needle. i ask if

lamar, my older bro will be there too. to him my questions are

caught flies charging the glass. he opens the window & out falls my:

yes, yes

maybe a home

with a porchlight. maybe a home

with a white fence. maybe a home

without holes. maybe a home

with fresh paint. maybe a home

without screams in the front screens

yes, yes. maybe a home

with a doorbell. maybe a home

with a door

Grief, Again

[AND STILL . . . ] every black woman with grey hair is your

dead mother you collapse in Walmart knees buckled at the

sight of an electric scooter you wrap yourself around

yourself & wail into a naked mattress you show the dean

the death certificate & are allowed to stay another

semester drowning would be easiest you think as rain draws razor thin lines down your bedroom window grief is

a paper cut at every bend in your body grief shaves each

bone down to a shriveled white 􀉻ag you want to die but

don’t want to leave a mess you throw a mug across the

kitchen & envy its sudden dissection every word your

mother last spoke scuttles like mice in your deserted head

memory is a ruptured organ memory is a ghost begging for

new flesh memory taps a gun to your inner skull &

demands you bring back the dead

LONG STORY SHORT

someone who is dead now taught you

how best to clean up your blood. then

how to clean up blood when it is not

your own. how to push from your elbow

properly sweep a floor, spell c o n t i n u e

three syllables donte, go on & like a god

or a bird, or a boy salted with grief, you

want the earth to kneel for you, want every

clock to confess its slick motive. to say,

suddenly, that death is only a joke the earth’s biggest punchline. she’s been

gone 15,840 minutes & you have felt the

godless storm of each of them, are waiting

for your mother to walk into her funeral, to

sit next to all of her children at once, to lean

into the soft of her shoulder, for her to whisper

it’s okay son, i’m here now, i’m here
```

---

## IC-1509: Away from the Sun

- Title: Away from the Sun
- Author (byline): Brad Arnold
- Work: Not specified
- Publisher: Online Sheet Music.com
- Publication date as stated: April 25, 2013
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 255
- Already set (do not supply): none

### Source block (context only)

```text
Author: Brad Arnold
ISBN: B00COD4ZTI
Publisher: Online Sheet Music.com
Date (Month/Year): April 25, 2013
NOTE: This poem is from a song lyric. The lyrics are in
digital print in e-Kindle format
```

### Introduction (context only: never use it for content warnings)

```text
The statistics on teen depression are sobering. Studies indicate that one in five children have some sort of mental, behavioral, or emotional problem, and that one in ten may have a serious emotional problem. Among adolescents, one in eight may suffer from depression. Of all these children and teens struggling with emotional and behavioral problems, a mere 30% receive any sort of intervention or treatment. The other 70% simply struggle through the pain of mental illness or emotional turmoil, doing their best to make it to adulthood far Away from the Sun by Brad Arnold.
```

### Performance text (classify this)

```text
It's down to this I've got to make this life make sense Can anyone do what I've done I missed life I missed the colours of the world Can anyone go where I am

'Cause now again I've found myself So far down, away from the sun That shines into the darkest place I'm so far down, away from the sun again Away from the sun again

I'm over this
I'm tired of living in the dark
Can anyone see me down here
The feeling's gone
There's nothing left to lift me up
Back into the world I've known

'Cause now again I've found myself So far down, away from the sun That shines into the darkest place I'm so far down, away from the sun That shines the life away from me To find my way back into the arms That care about the ones like me I'm so far down, away from the sun again It's down to this I've got to make this life make sense And now I can't do what I've done

And now again I've found myself So far down, away from the sun That shines the life away from me

'Cause now again I've found myself
So far down, away from the sun
That shines into the darkest place
I'm so far down, away from the sun
That shines the life away from me
To find my way back into the arms
That care about the ones like me
I'm so far down, away from the sun again
```

---

## IC-1510: Ballad of the Seven Songs: A Poem for Emancipation Day

- Title: Ballad of the Seven Songs: A Poem for Emancipation Day
- Author (byline): Langston Hughes
- Work: The Collected Poems of Langston Hughes
- Publisher: Random House LLC
- Publication date as stated: 1994
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1259
- Already set (do not supply): none

### Source block (context only)

```text
Author: Langston Hughes
Book: The Collected Poems of Langston Hughes
ISBN: 978-0307949387
Publisher: Random House LLC
Date (Month/Year): 1994
```

### Introduction (context only: never use it for content warnings)

```text
Balllad of the Sven Songs: A Poem for Emancipation Day by Langston Hughes
```

### Performance text (classify this)

```text
Seven letters,
Seven songs,
The seven letters
F-R-E-E-D-O-M
Spell Freedom.
The seven songs
Capture segments of its history
In terms of black America.

Seven songs, Seven names:

Cudjoe

Sojourner Truth

Harriet Tubman

Frederick Douglass

Booker T. Washington

Dr. Carver

Jackie Seven men and women From unrecorded slavery to recorded free:

For Emancipation Day
Seven songs,
Seven men,
Seven letters
That spell Freedom.

It was an easy name to give a slave
So they called him Cudjoe,
There were four million Cudjoes
Before Emancipation came.

What did it mean to be a slave?
That you could not choose your own son’s name,
Nor your own son’s father or mother,
Nor your own son’s home, or work, or way of life,
(No indeed could you choose your own)
Nor choose to have or not have a son.
No part of life or self
Belonged to Cudjoe – slave.

To Cudjoe – slave –
Only a dream belonged.
Seven letters spelled the dream:
F-R-E-E-D-O-M
Freedom!
But in the cane fields, in the rice fields,
In the bondage of the cotton,
In the deep dark of the captive heart,
Sometimes Freedom seemed so far away,
Farther than the farthemost star,
So far, so far –
That only over Jordan was there a dream
Called Freedom.
Cudjoe’s song was:

Deep river,

My home is over Jordan.

Deep river, Lord,

I want to cross over into camp ground.

O, don’t you want to go to that gospel feast,

That promised land where all is peace? . . .

Deep river, Lord,

I want to cross over into camp ground.

(See http://www.youtube.com/watch?v=H7iOBqmwZOE for music)

Death was a deep river,
And only over Jordan, Freedom.
Oh, night! Oh, moon! Oh, stars!
Oh, stars that guide lone sailing boats
Across the great dark sea,
Star, guide thou me!

Star! Star! Star!
North Star! North.
I cannot catch my breath
For fear of that one star
And that one word:
Star – Free – Freedom – North Star!
Where is the road that leads me to that star?

Ah, ha! The road?
Dogs guard that road
Patrollers guard that road,
Bloodhounds with dripping muzzles
Guard that road!
Gun, lash, and noose
Guard that road!

Freedom was not a word:
Freedom was the dark swamp crossed,
And death defied,
Fear laid aside,
And a song that whispered, crooned,
And while it whispered cried:

Oh, Freedom!

Freedom over me!

Before I’d be a slave

I’d be buried in my grave

And go home to my Lord

And be free!

(See http://www.youtube.com/watch?v=veiJLhXdwn8 for music)

Harriet Tubman – slave. She wanted to be free.

She’d heard of that word with seven letters.
She could not read the word,
Nor spell the word,
But she smelled the word,
Tasted the word,
On the North wind heard the word.
And she saw it in a star.

Before I’d be a slave,

I’d be buried in my grave

And go home to my Lord

And be free!

Sojourner Truth – slave.
She wanted to be free.
Her sons and daughters sold away,
Still she wanted to be free.
She said:

I look up at de stars,

My chillum look up at de stars.

They don’t know where I be

And I don’t know where they be,

God said, Sojourner, go free!

Go free! Free! Freedom! Free!

Before I’d be a slave

I’d be buried in my grave . . .

Before Emancipation thousands of slaves
Made their way to freedom –
Through swamp and brier, over field and hill,
By dark of night, prayer-guided, star-guided,
Guided by that human will that makes men love
A word called Freedom –
And the deep river was not Jordan, but the Ohio,
Home was not heaven, but the North.
North! North Star! North!

Frederick Douglass called his paper “The North Star.”

Douglass had made his way to freedom.
Sojourner Truth made her way to freedom.
Harriet Tubman made her way to freedom;
Then she went back into slavery land,
And back again, and back again, and again, again,
Each time bringing a band of slaves
(Who once were slaves, no slaves no more )
To freedom!
Before the Civil War,
Long before ’61,
Before Emancipation,
Freedom had begun!

Go down, Moses,

Way down in Egypt land

Tell old Pharaoh

To let my people go!

(See http://www.youtube.com/watch?v=SP5EfwBWgg0 for music)

Linking arms for freedom
With the one-time slaves,
With Douglass, Harriet, Sojourner,
Were Whittier, Garrison, Lovejoy, Lowell –
Great Americans who believed in all men being free.
And thousands more – white, too, but no so famous –
Dared arrest and scorn and persecution
That black men might be free:
The stations of the underground railroad to freedom
Became many –
And the North Star found a million friends.
And of that time a book was born, “uncle Tom’s Cabin.”
And a spirit was born, John Brown.
And a song was born:

Mine eyes have seen the glory of the coming of

the Lord:

He is trampling out the vintage where the grapes

of wrath are stored;

He hath loosed the fateful lightning of his

terrible swift sword: . . .

(See http://www.youtube.com/watch?v=WDuVApacL7Q for music)

And a war was born:

John brown’s body lies

A-mouldering in the grave –

But his soul goes marching on!

(See http://www.youtube.com/watch?v=LGPN2x0ChnY for music)

And a voice to set the nation right:

With malice toward none,

With charity for all . . .

Lincoln . . .

In the beauty of the lilies Christ was born across

the sea,

Abraham . . .

With a glory in His bosom that transfigures you

and me;

Lincoln . . .

As he died to make men holy, let us die to make

men free,

Abraham . . .

While God is marching on.

Lincoln . . .

In giving freedom to the slave

We assure freedom to the free . . .

Abraham . . .

No man is good enough to govern another

Man without that other’s consent.

Lincoln . . .

I do ordain . . . thenceforward and forever free.

But the fields still needed planting,
The cane still needed cutting,
The cotton still needed picking.
The old mule still needed a hand to guide the plow:

De cotton needs pickin’

So bad, so bad, so bad!

De cotton needs pickin’ so bad!

Gonna glean all over this field!

(See http://www.youtube.com/watch?v=W9CUOwDqrBw for music)

And on the river boats the song:

Roll dat bale, boy!

Roll dat bale! . . .

(No sample for this lyric)

Up the river to Memphis, Cairo, St. Louis, Work and song, work and song – stevedores, foundry men, Brick layers, builders, makers, section hands, railroad shakers:

There ain’t no hammer

In this mountain

Rings like mine, boys,

Rings like mine!

(Sung to the tune of John Henry: See http://www.youtube.com/watch?v=xxReOxRwS-g for music )

Freedom is a mighty word,
But not an easy word.
You have to hold hard to freedom.
And as somebody said,
Maybe you h ave to win it all over again every generation.
There’s no color lines in freedom.
But not all the “free” are free.
Still it’s a long step from Cudjoe – slave,
From Harriet Tubman – slave,
Sojourner Truth – slave,
Fredrick Douglass – slave
Who had to run away to freedom –

It’s a long step to Booker T. Washington
Building Tuskegee,
To Dr. W.E.B. Du Bois building a culture for America.
It’s a long step from Cudjoe – slave
Hoeing cotton –
To George Washington Carver – once slave –
Giving his discoveries in agricultural chemistry to the
world.
It’s a long song from:

Before I’d be a slave

I’d be buried in my grave . . .

To Dorothy Maynor singing, “Dupuis le jour.” It’s a long step from Cudjoe – slave – To Jackie Robinson hitting a homer.

Yet to some Freedom is still
Only a part of a word:
Some of the letters are missing.
Yet it’s enough of a word
To lay hands on and hope,
It’s enough of a word
To be a universal star –
Not just a North Star anymore:

Thenceforward and forever – free!

Oh, Freedom!

Freedom over me!

Before I’d be a slave

I’d be buried in my grave

And go home to my Lord

And be free!
```

---

## IC-1511: Behind the Staff Room Door – A Collection

- Title: Behind the Staff Room Door – A Collection
- Author (byline): Brian Moses, Bruce Lansky, Darren Sardelli and Bill Dodds
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1274
- Already set (do not supply): none

### Source block (context only)

```text
Author: Brian Moses (all poems by this author)
Book: Lost Magic – The Very Best of Brian Moses
ISBN: 978-1509838745
Publisher: Macmillan Children's Books
Date (Month/Year): Dec 2016
Author: Bruce Lansky
Book: No More Homework! No More Tests!
ISBN: 978-0671577025
Publisher: Running Press Adult
Date (Month/Year): Aug 1997
Author: Darren Sardelli
Book: Galaxy Pizza and Meteor Pie
ISBN: 978-0615284699
Publisher: Laugh-A-Lot Books
Date (Month/Year): Jan 2009
Author: Bill Dodds
Book: Kids Pick the Funniest Poems: Poems that Make
Kids Laugh (Edited by Bruce Lansky) Pgs 48-51
ISBN: 978-0671747695
Publisher: Meadowbrook
Date (Month/Year): Nov 1991
```

### Introduction (context only: never use it for content warnings)

```text
When you are little, your brain tries to make sense of the world as you experience it. Magic is real and logic is relative. For example, when I was little, I honestly believed that teachers actually lived at the school and were specially modified to never have to go to the bathroom. Their personal rooms, kind of like dorm rooms, were behind the door marked “Teacher’s Lounge.” I mean, what other explanation was there?

I present today, education from a kid’s perspective in. Behind the Staff Room Door – A Collection with poems by Brian Moses, Bruce Lansky, Darren Sardelli
```

### Performance text (classify this)

```text
Targets by Brian Moses (Pg 132)

My teacher says my targets are:
To write more neatly,
to spell more words correctly,
to get more sums right,
to chatter less,
and to behave myself.

But the targets I set myself are far more interesting:

To climb a tree to the top, to stop time before my spelling test, to think up a disappearing spell and try it out on my teacher, to leap from up high and to defy gravity.

These are my targets, the ones I’m aiming to complete before next week . . .

The ones my teacher sets may take a little longer . . .

and Bill Dods

Behind the Staffroom Door by Brian Moses (Pg 135-136)

Ten tired teachers slumped in the staffroom at playtime, one collapsed when the coffee ran out, then there were nine.

Nine tired teachers making lists of things they hate, one remembered playground duty, then there were eight.

Eight tired teachers thinking of holidays in Devon, one slipped off to pack his case, then there were seven.

Seven tired teachers, weary of children's tricks, one hid in the stock cupboard, then there were six.

Six tired teachers, under the weather, barely alive, one gave an enormous sneeze, then there were five.

Five tired teachers, gazing at the open door, one made a quick getaway, then there were four.

Four tired teachers, faces lined with misery, one locked herself in the ladies, then there were three.

Three tired teachers, wondering what to do, one started screaming when the bell rang, then there were two.

Two tired teachers, thinking life really ought to be fun, one was summoned to see the Head, then there was one.

One tired teacher caught napping in the afternoon sun, fled quickly from the staffroom, then there were none.

How to Torture Your Teacher by Bruce Lansky (Pg 38-39)

Only raise your hand when
you want to sharpen your pencil
or go to the bathroom.
Repeat every ten minutes.

Never raise your hand
when you want to answer a question;
instead, yell, “Oooh! Oooh! Oooh!”
and then, when the teacher calls on you,
say, “I forgot what I was going to say.”

Lean your chair back,
take off your shoes, and
put your feet up on your desk.
Act surprised when the teacher
puts all four legs of your chair back on the floor.

Drop the eraser end of your pencil on your desk. See how high it will bounce.

Drop your books on the floor See how loud a noise you can make.

Hum. Get all your friends to join in.

Hold your nose, make a face, and say, “P.U.!”

Fan the air away from your face, and point to the kid in front of you.

On the last day of school,
lead your classmates in chanting:
“No more pencils!
No more books!
No more teachers’
dirty looks!”

Then, on your way out
the door, tell the teacher,
“Bet you’re looking forward
to summer vacation this year.
But I’ll sure miss you.
You’re the best teacher
I’ve ever had.”

Billy’s Coming Back by Brian Moses (Pg 123-124)

Word is out on the street, Billy's coming back.

There's a sound outside of running feet,
somebody, somewhere's switched on the heat,
policemen are beating a swift retreat
now Billy's coming back.

Only last year when he went away
everyone heaved a sigh,
now news is out, and the neighborhood
is set to blow sky-high.

Words are heard in the staff room,
teachers' faces deepen with gloom,
can't shrug off this feeling of doom,
now Billy's coming back.

It was wonderful when he upped and left,
a carnival feeling straightaway,
no looking over shoulders,
each day was a holiday.

And now like a bomb, no one dares to defuse, time ticks on while kids quake in their shoes no winners here, you can only lose, now Billy's coming back.

It's dog eat dog on the street tonight, it's cat and mouse, Billy's looking for a fight, so take my advice, keep well out of sight now Billy's coming back.

Silliest Teacher in School by Darren Sardelli (Pg 5)

Our teacher gave detention
to the fountains in the hall.
She handed extra homework
to the artwork on the wall.

We saw her point a finger
at a banner and a sign.
She said their bad behavior
was completely out of line.

The principal approached her
and said, “What is all this fuss?
I heard you tried to punish
all the tires on a bus.

“You’ve made the teachers angry
by disrupting all their classes,
so if you want to keep this job,
you have to wear your glasses!”

TRANSITION

We had recess and story time. Elementary schools was MARVELOUS! Until the day your beloved teacher didn’t appear. You know what that means . . . a substitute!(sad face, rapidly changing to mischievous)

YAY! Chaos! -- switching names, pretending you get 5 recesses instead of 3; telling the poor soul that “that’s not the way Mrs. Smith does it!” all day long. Well, that’s what usually happens (beat) unless your substitute is

(maniacal laugh and evil teacher face) Mrs. Stein . . .

Mrs. Stein by Bill Dodds (Pg 48-51)

The school bell rings, we go inside,
Our teacher isn’t there.
“Maybe she’s sick!” her pet cries out.
Yeah, right. As if I’d care.

I have a D in Language Arts,
My grade in math’s the same.
And now my teacher might be sick.
Could be I’m part to blame.

She doesn’t like me, that’s a fact,
I wouldn’t tell a lie.
She says stuff like: “You’re very smart,
But you don’t even try.”

I start to laugh—my teacher’s sick! And boy, I’m feeling fine . . .

When someone knocks the door right in, And there stands Frankenstein.

She’s six-foot-eight, her dress is black,
She’s wearing combat boots.
I start to gasp, she growls and says,
“I’ll be your substitute.”

The teacher’s pet is whimpering;
She doesn’t stand a chance.
The smart kid stares and points and faints.
The bully wets his pants.

“My name is Mrs. Stein,” she says,
And every student cringes.
She leans the door against the wall,
She’s knocked it off its hinges.

“Now let’s begin. You there! Stand up!”
She looks me in the eye.
I try to move, my legs won’t work.
I know I’m going to die!

In one big step she’s next to me,
And she does more than hover.
She blocks the sun, it’s dark as night,
My classmates run for cover.

“Now get up to the board,” she says. “I’d like to see some action.

Pick up the chalk, explain to us Division of a fraction.”

I leap away to save my life,
This time I really try.
I think and think and think and croak,
“Invert and multiply.”

“Correct! She says. I breathe again
And head back for my chair.
“You, FREEZE!” she shouts, and I stop cold.
“And don’t go anywhere.”

This all begins at nine o’clock,
I fight to stay alive.
It seems to last a million years—
The clock says nine-o-five.

That’s just three hundred seconds,
And then my turn is through.
She points at every one of us—
“Now you. Now, you. Now, you.”

We all get nailed this awful day,
There’s nowhere we can hide.
The lunch bell rings, we cannot eat,
We simply crawl outside.

We can’t believe the other kids Who run and play their games.

Not us, who have big Mrs. Stein— Our world is not the same.

The bell has tolled, I must go in,
My time on earth is through.
I’ll leave this on the playground—
Here’s what you have to do.

You must listen to your teacher
And pray her health is fine,
Or one day soon you’ll hear the words:
“My name is Mrs. Stein.”
```

---

## IC-1512: Between the Star and the Street – A Collection

- Title: Between the Star and the Street – A Collection
- Author (byline): Jonathan B. Tucker and Nour Abdel Latif
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1086
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jonathan B Tucker *
Book: Speaking Truths: Young Adults, Identity, and
Spoken Word Activism by Valerie Chepp, Pgs 4-8
ISBN: 978-1978801103
Publisher: Rutgers University Press
Date (Month/Year): Feb 2022
Author: Nour Abdel Latif *
ISBN: On-Line Transcript
https://newyorkwarcrimes.com/if-i-must-starve
Publisher: New York War Crimes.com
Date (Month/Year): Oct 6, 2026
Author: Nour Abdel Latif
ISBN: On-Line Transcript
https://refaatwritesback.beehiiv.com/p/buried-truths-rising-
voices-4c6d
Publisher: Refaat Writes Back
Date (Month/Year): August 25, 2025
```

### Introduction (context only: never use it for content warnings)

```text
The following 3 poems live in the raw space between Jewish identity and Palestinian suffering -- where shared history collides with unequal power and unresolved grief. They trace how a symbol like the Star of David can become a source of shame, how Gaza exists not as a headline but as a place of memory, and how voices rooted in truth can come to be treated as threats.

What happens when survival hardens into domination? What happens when inherited trauma is used to justify present violence? I urge you to listen with an open mind and to recognize both sides of a conflict where human lives are too often erased in the name of history.

Between the Star and the Street – A Collection by Jonathan B. Tucker and Nour Abdel Latif
```

### Performance text (classify this)

```text
Dear David by Jonathan B. Tucker (Pgs 4-8) A six-sided star fishes for identity on my

chest Tucked under a mixed family It dangles like a worm on a hook under American

waters

David, you’ve become a constellation we no longer

strain to see
Like a king’s crown
Your yellow light showed us through the darkest times
Exposed us to the darkest crimes
When you labeled us a problem
A question
They answered with genocide
Another problem
Another question
They answered with atomic bombs
More problems
We stop asking
And instead promise never again

We lie
Dead
As our babies
Boom
Might as well drop them out of the planes
Makes as much sense as cartoons as war propaganda

Dear David They gave you a nation but what did you say? Are you trapped between those two blue bars or can

you still get away? Because Israel was dropped on top of Palestine and is

there to stay
Like one triangle
Turned around and dropped on another
You see, David, my brother cannot be anti-Semitic if

he is as Semitic as me Isaac, Ishmael just wants to be free But you’ve got him building pyramids out of the

charred dust of bulldozed homes
In the Gaza
Stripped of rights
You’ve let your brother sleep naked and hungry too

many nights

You pharaoh
Cashing checks from the West
Bank
You’ve become
Settled
In your thinking
Unlike your Torah
You do not move
You have not turned

You six-sided sinner You blind Goliath You have a hexagon center that points nowhere but

inward
What are you looking for out in that desert?
Is it another ghetto?
Are you somehow jealous of the swastika’s popularity

among disaffected youth?
I mean, are you trying to be a bad a**?
Or are you just an abused child
Now grown up
Molesting your nephew and calling him names?

Dear David Our homeland is neither Just like the Christian Right. . . . How ashamed you’ve

made us I used to cover all my notebooks with little pictures of

you Now I tuck you under my shirt in order to hide my

association with My role in unwillingly supporting your racial, national,

religious apartheid You make me sick David

Oceans away
You fish for identity on my chest
Reminding me who I am
Because of how you can’t be
Reminding me where I come from
By showing us where we can’t go
You are a fallen star
Not lucky
Nor bright
Yet I still see myself in you far too often
Like some birthright trip to hypocrisy
From Crofton, Maryland
Because all I can say
Is never again
As I tuck my necklace away
And pray that we end this oppression

* Jonathan B. Tucker, foundation relations manager at

Refugees International, was born in Washington, D.C.

Prior to joining Refugees International, Tucker served as

the director of youth programs at Split This Rock, where

he taught and coached the award-winning DC Youth

Poetry Slam Team and co-founded the Louder Than a

Bomb DMV Teen Poetry Slam Festival.

Between Here and Gone by Nour Abdel Latif
How can I press a city to my chest?
Embrace its streets, its homes, its windows?
How can my heart stretch wide,
To hold a longing this deep?
And how can I kiss its wounded ground,
Without my soul collapsing?

How do I hold a scream so deep,
In the alley where I used to play?
How do I wipe a silent tear,
On the stone where Dad once sat?
How do I bring our laughs once more,
To streets we knew?

And how do I say, I missed you so, Without letting the heartbreak show?

How do I mend my shadow on her timeworn stone, Where every crack once knew me as its own?

How do I walk the same streets of my young feet, Without the weight of all that’s lost, replayed? How do I hear the rising call to prayer, And not let tears betray my hidden cries? How do I say, I had to go away, When my soul never left?

Gaza...
How can one hug hold all your scattered cries?
How can my heart survive the loss each time your
name goes by?
I walk your streets, yet I’m not there,
I search your face—it’s lost.
You break inside me,
Without a reason I know why.

Gaza still stands—but not the same,
A shadow walks where once burned flame.
And the ache left within my chest
Is deeper, harsher—
A grief beyond a single death.

* Nour Abdel Latif is a mother of three and a writer who

lived in North Gaza until repeated displacements forced

her to move south. Her work, which includes both poetry

and personal diaries, provides a firsthand account of the

war, the destruction of her home and business, and the

challenges of survival and displacement in Gaza Buried Truths, Rising Voices by Nour Abdel Latif

For all the blue vests killed in Gaza *

It resembled us—
that voice, grown from our anguish,
carrying pain washed clean by dew,
telling our stories with unheard tone,
as if he spoke from behind a soundproof glass.

A voice of ours, born of our wounds,
steady as dawn on Gaza’s brow,
like a sea resisting the blade of fate,
like a field of anemones in spring’s gentle glow—
Full of longing, even as it fades.

It was just a voice.
No weapon in hand, no blood on its breath,
just a melody,
perhaps borne by the wind beyond the edge,
or a whisper
that reached the hearts of those who were numb to
the truth.

Why did they silence it?
Was it because it looked like us?
Because he loved the land
as if his soul were forged in her dust?

Yes, it was a voice,
a light from the heart when the sky turns black,
illuminating ruin, gifting breath to hope—
and so, they feared it
and buried it beneath the ground—without a tear,

without even a tremble.

But a voice born of truth
is never laid to rest.
It lingers—
in the dust, in the wind,
in every heartbeat that dares to remember.
One day, it will rise again—
not as a whisper,
but as a storm.

*As of August 2005, more than 270 journalists and media workers (blue vests) have been killed by Israeli attacks in Gaza. Read more here: https://www.aljazeera.com/news/2025/8/11/here-are-the-names-of-the-journalists-israel-killed-in-gaza
```

---

## IC-1513: Birmingham Collection

- Title: Birmingham Collection
- Author (byline): Jasmine Mans and Dominique Christina
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1378
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jasmine Mans
Book: Chalk Outlines of Snow Angels, Pg 81-82
ISBN: 978-1476259376
Publisher: Thorn10 Publishing
Date (Month/Year): June 2012
Author: Dominique Christina
Book: They are All Me
ISBN: 978-0692460009
Publisher: Swimming with Elephants Publications
Date (Month/Year): July 2012
```

### Introduction (context only: never use it for content warnings)

```text
It was a sunny, September Sunday in Birmingham Alabama. The children of the 16th Street Baptist Church, dressed in their Sunday best, were in charge of the lesson that morning -- “A Love that Forgives.” The sermon was based on Luke 23:34: “Then Jesus said, ‘Father, forgive them; for they know not what they do’.” But before the lesson ever began, a dynamite blast ripped through the congregation, claiming the lives of Denise McNair who was only 11 years old, Addie Mae Collins, Carole Robertson and Cynthia Wesley

(all 14). In the words of Jasmine Mans from her poem “Birmingham Girl” -- God can’t always protect you from the boogieman.
```

### Performance text (classify this)

```text
Birmingham Girl by Jasmine Mans (Pg 81-82)

Mama said the bomb wasn’t meant for me, I think it was meant for Pastor Martin Because he be having them dreams

Maybe those white men didn’t know
That little black girls be going to church too
And we be folding our hands,
Praying, and taking communion
Just like their daughters do
I was supposed to wear my church shoes
If I listened maybe the bad men would not have came for me.
I knew they matched my dress but they always be hurting my
feet.

I be wondering if
God christened the bombs that exploded my flesh into
sacrifice?
And does anybody be hearing those scriptures
Spoken in tongues
Claiming Christ before everything went boom
Before the smoke and the rubble baptized these collapsing
bones
You know these stain glass windows be hiding destruction

I be thinking maybe if they knew
We were like the most beautiful flowers
Right before the wind and the dirt started playing tug of war
With the delicates of our petals.

Mama said one man died for the sins of the entire world, So how did that man let this church tremble on my soul I don’t remember there being enough Holy water to stop the burning, To calm all that smoke.

Mama said some heartbreaks be too hard
To swallow at communion
Some serpents be finding salvation
In baptismal pools
Some church mice be screaming
America’s dirty little secrets

Momma told me
Some deaths be too black and white
To be labeled holy
And that some baby dolls are sacrificed
Without permission
Some sacrifice comes without fair warning
God can’t always protect you
From the boogieman
Some baby girls will reach the pearly gates
And not be tall enough
To turn the handle.

Mama would always be saying
Some men will be too guilty
To claim innocence with Christ.
But I didn’t . . . do anything
I never wanted . . . to play with the white girls.
I never asked . . . for integration,

I be wondering if God was too busy
Trying to protecting Martin
To think about us
I never asked . . . for his dream
But Momma say his dream be asking for me.

TRANSITION

Even though the legal system was slow to provide justice, the effect of the bombing of the 16th Street Baptist Church was immediate and significant. Outrage over the death of the four young girls helped build increased support behind the continuing struggle to end segregation—support that would help lead to the passage of both the Civil Rights Act of 1964 and the Voting Rights Act of 1965. In that important sense, the bombing’s impact was exactly the opposite of what its perpetrators had intended. Dominique Christina creates another powerful character who describes the attack in “Birmingham Sunday.”

Birmingham Sunday by Dominique Christina

I do not know what came a’loose first.

A church ain’t made for fallin’ in on itself.
You don’t build ‘em prepared for destruction.
You build ‘em thinkin’ bout the praise shout,
the hand clap, the open-mouthed communions,
how many choir members can fit in the pulpit,
the pancake breakfast you gon’ have in the basement
and the stained-glass Jesus.
Even in Birmingham Alabama 1963,
where you had to account for dynamite.
For the sharp teeth of segregation chewin’ through
waterlogged protest marchers swept
clean off their feet. They fell
like blood-torn right angles to
foamin’ at the mouth police dogs,
billy clubs and batons.

But churches ain’t made for fallin’ down. And I don’t know what came a’loose first, if the pillars tipped over before the pulpit shuddered if the windows hung for a moment in their frames before the terrible speed of shrapnel got in the way of everything . . .

If you were a colored girl in Birmingham,
you knew how to duck and shrink
how to be a misspelled word,
an incomplete sentence
squelched down to sugar-softened
press-and-curl perkiness.
Their silence was so loud,
their teeth a locked gate.
Their mouths held annual sit-ins
for their flame-red throats,
the sizzle and spill of every unsaid thing.
And it is hard to be so still
with all that playground and star-shine
shimmy in the stretch of our bones,
but on Sundays we get it near right.

The mornings rollout in hot cakes and black coffee.
Daddy is a baritone down the hall singin’ hymns,
Mama is fixin’ his tie then yellin’ bout stockings and
Get on in here and eat before this food gets cold!
And we can wear our hair down.
It will be curled round our ears
and stopped with ribbon.
And the wild hunger of Jim Crow
cannot find you in church.
So we slidin’ round the kitchen in
our white shoes without a single scuff,
and your sister gets to dab a little rouge
on her cheeks just on Sundays,
just on Sundays.
And the car ride is a sovereign floating joy
the whole way ‘cuz mama can sing
and she’s rollin’ that pretty bell-tinkle
soprano out and we pickin’ up the chorus
where we can and though
we have to keep tuggin’ at our slip
so it doesn’t dip below our dress. . .

We are everything new and shiny
that God has ever loved, and deep
and high in our colored girl
sometime-loveliness,
because Jim Crow did not seek you in church.

I don’t know what came a’loose first.
But when the choir was singin’
I wish I knew how it would feeeeel to be free . . . *
And you were a wet giggle with your sister
in Sunday school,
The sky fell down and smothered everything.

Ceiling tiles flew like occasional birds,
smacked the walls and smoldered
skulls and incandescent smoke
a wild death for a young girl --
the crackle and pop of spinning fire
that burns everything to cinder.
A valley of broken jawbones
baby teeth scattered like confetti,
a stony, vexing sleep

The sun crazy with shining anyway,
the flesh insulted rubble.
The refugeed clergy diggin’ through
the glass and mortar,
Findin’ tiny limbs and

The world is a singed skirt.

I don’t know what came a’loose first
But it all came a’loose didn’t it, Addie and Denise?
Didn’t it, Cynthia? Didn’t it, Carole?
Didn’t it all break a’loose,
didn’t it drop the winter in?
Didn’t it catch and keep the sky snatched low
by the terrible clang of dynamite?

It’s funny. It’s a dream. And the dream is a roar.

And the roar keeps time with dragons.

I don’t know what came a’loose first. Churches ain’t for fallin’ down. Colored girls should be safe on Sunday.

No one should offer you a heaven,
no matter how honeyed,
when you had’t even had your period yet.
Or been to your first boy/girl dance,
or had the chance to gossip about it the next day
laughin’ foot-stop girrrrrrrrrl wait-til-you-hear-this

whimsy That was STILL your right. No matter what Jim Crow said . . .

And can’t nobody re-flesh those bones.
Your mama will never be the same
pleated skirt or
sometimes silly sista
who could smile with all her teeth . . .
Because somebody lifted a sheet,
and underneath it was your bomb-blasted body
and the world broke open and swallowed her whole . . .

Things come a’loose, fall down and fall apart lawd . . .
The center will NOT hold, but
You hear that?
Just over all that ugly, you hear that?
Past the thunder crack of grief and Go down Moses. . .
You hear that?
Can’t no detonated handmade nothing’ touch it.

Just over the tracks and down the street a ways,
there is still hide and seek rough and tumble
tag and tea parties. Some little girl is hula hoop
and hopscotch lemon cookie wonderful twirlin’
in her mama’s old stitched and restitched skirts.
And she’s gon’ go to church on Sunday singin’

I wish I knew how . . . it would feeeeeeel to be free . . .*

And mean it. And mean it.

* Music and Lyrics to I Wish I Knew How It Would Feel to Be Free by Nina Simone: https://www.youtube.com/watch?v=HDqmJEWOJRI

Sources for historical research:

Birmingham Church Bombing https://www.history.com/topics/black-history/birmingham-church-bombing

Jim Crow Laws in Birmingham, Alabama https://herb.ashp.cuny.edu/items/show/866
```

---

## IC-1514: The Black Clown and The Bitter River

- Title: The Black Clown and The Bitter River
- Author (byline): Langston Hughes
- Work: The Collected Poems of Langston Hughes
- Publisher: Vintage Contemporaries
- Publication date as stated: Oct 1995
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1011
- Already set (do not supply): none

### Source block (context only)

```text
FOR BOTH POEMS
Author: Langston Hughes
Book: The Collected Poems of Langston Hughes
ISBN: 978-0679764083
Publisher: Vintage Contemporaries
Date(Month/Year): Oct 1995
```

### Introduction (context only: never use it for content warnings)

```text
The early blackface minstrel shows of the 19th century portrayed blacks as joyous, naive, superstitious, and ignorant—characteristics related to the way slaveholders in earlier years believed them to be. But in The Black Clown by Langston Hughes a black minstrel challenges this stereotype, discards his clown costume and asserts his basic humanity.
```

### Performance text (classify this)

```text
You laugh
Because I’m poor and black and funny—
Not the same as you—
Because my mind is dull
And dice instead of books will do
For me to play with
When the day is through.

I am the fool of the whole world.

Laugh and push me down. Only in song and laughter I rise again—a black clown. Strike up the music. Let it be gay. Only in joy Can a clown have his day.

Three hundred years
In the cotton and the cane,
Plowing and reaping
With no gain—
Empty handed as I began.

A slave—under the whip,
Beaten and sore.
God! Give me laughter
That I can stand more.

God! Give me the spotted
Garments of a clown
So that the pain and the shame
Will not pull me down.

Freedom!
Abe Lincoln done set me free—
One little moment
To dance with glee.

Then sadness again—
No land, no house, no job,
No place to go.
Black—in a white world
Where cold winds blow.
The long struggle for life:
No schools, no work—
Not wanted here; not needed there—
Black—you can die.

Nobody will care—

Yet clinging to the ladder,
Round by round,
Trying to climb up,
Forever pushed down.

Day after day White spit in my face— Worker and clown am I For the “civilized” race.

Nigger! Nigger! Nigger! Scorn crushing me down. Laugh at me! Laugh at me! Just a black clown!

Laugh at me then,
All the world round—
From Africa to Georgia
I’m only a clown!

But no! Not forever
Like this will I be:
Here are my hands
That can really make me free!

Suffer and struggle.
Work, pray, and fight.
Smash my way through
To Manhood’s true right.

Say to all foemen:
You can’t keep me down!
Tear off the garments
That make me a clown!
Rise from the bottom,
Out of the slime!

Look at the stars yonder Calling through time!

Cry to the world
That all might understand:
I was once a black clown
But now—
I’m a man!

TRANSITION A large portion of the white population, however, had difficulty accepting the basic humanity of the black man. Instead radical steps were taken to keep the black man “in his place. For many African Americans growing up in the South in the 19th and 20th centuries, the threat of lynching was commonplace. The popular image of an angry white mob stringing a black man up to a tree is only half the story. Lynching, an act of terror meant to spread fear among blacks, served the broad social purpose of maintaining white supremacy in the economic, social and political spheres. The Bitter River is dedicated to the memory of Charlie Lang and Ernest Green, each fourteen years old when lynched together beneath the Shubuta Bridge over the Chicasawhay River in Mississippi, October 12th, 1942. The Bitter River by Langston Hughes There is a bitter river Flowing through the South. Too long has the taste of its water Been in my mouth. There is a bitter river Dark with filth and mud. Too long has its evil poison Poisoned my blood.

I've drunk of the bitter river
And its gall coats the red of my tongue,
Mixed with the blood of the lynched boys
From its iron bridge hung,
Mixed with the hopes that are drowned there
In the snake-like hiss of its stream
Where I drank of the bitter river
That strangled my dream:
The book studied-but useless,
Tool handled-but unused,
Knowledge acquired but thrown away,
Ambition battered and bruised.
Oh, water of the bitter river
With your taste of blood and clay,
You reflect no stars by night,
No sun by day.

The bitter river reflects no stars-
It gives back only the glint of steel bars
And dark bitter faces behind steel bars:
The Scottsboro boys behind steel bars,
Lewis Jones behind steel bars,
The voteless share-cropper behind steel bars,
The labor leader behind steel bars,
The soldier thrown from a Jim Crow bus behind steel
bars,
The 150 mugger behind steel bars,
The girl who sells her body behind steel bars,
And my grandfather's back with its ladder of scars
Long ago, long ago-the whip and steel bars -
The bitter river reflects no stars.

"Wait, be patient," you say.
"Your folks will have a better day."
But the swirl of the bitter river
Takes your words away.
"Work, education, patience
Will bring a better day-"
The swirl of the bitter river
Carries your "patience" away.
"Disrupter! Agitator!
Trouble maker!"you say.

The swirl of the bitter river
Sweeps your lies away.
I did not ask for this river
Nor the taste of its bitter brew.
I was given its water
As a gift from you.
Yours has been the power
To force my back to the wall
And make me drink of the bitter cup
Mixed with blood and gall.

You have lynched my comrades
Where the iron bridge crosses the stream,
Underpaid me for my labor,
And spit in the face of my dream.
You forced me to the bitter river
With the hiss of its snake-like song-
Now your words no longer have meaning-
I have drunk at the river too long:
Dreamer of dreams to be broken,
Builder of hopes to be smashed,
Loser from an empty pocket
Of my meagre cash,
Bitter bearer of burdens
And singer of weary song,
I've drunk at the bitter river
With its filth and its mud too long.
Tired now of the bitter river,
Tired now of the pat on the back,
Tired now of the steel bars
Because my face is black,
I'm tired of segregation,
Tired of filth and mud,
I've drunk of the bitter river
And it's turned to steel in my blood.

Oh, tragic bitter river
Where the lynched boys hung,
The gall of your bitter water
Coats my tongue.
The blood of your bitter water
For me gives back no stars.
I'm tired of the bitter river!
Tired of the bars!
```

---

## IC-1515: Blessed are the Confused – A Collection

- Title: Blessed are the Confused – A Collection
- Author (byline): Clayton Jennings
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 953
- Already set (do not supply): none

### Source block (context only)

```text
Author: Clayton Jennings
Spoken Word Album: Goodbye Religion, Track 8
ISBN: Digital Album
Author: Clayton Jennings
Spoken Word Album: King Nothing, Track 2
ISBN: Digital Album
```

### Introduction (context only: never use it for content warnings)

```text
What happens when someone grows up in a church that promises love and guidance but instead leaves them feeling judged, confused, and alone? “Goodbye Religion” follows a narrator who has spent years trying to find God, only to feel let down by hypocrisy, unanswered prayers, and church leaders who care more about power than people. “Church Hurt” shows how a teenager loses trust in church because the adults act holy in public but hide serious problems at home. Church communities, when their actions don’t match their message, often push young people to question what they believe and what real faith should look like.

Blessed are the Confused – A Collection by Clayton Jennings
```

### Performance text (classify this)

```text
Goodbye Religion How do I describe you when my words come from the

mouth of a spiritual infant? I read the letters and fell in love with the miracles in it. And I get a picture of you from the pictures portrayed in

the snapshots of Scripture . . .

I've hung pictures of you on my wall, and I stared

with doubt. I don't know if you look like the pictures we portray you to

be. What's my purpose, God? What did you create me to be? I'm dying for you to show up and just say it to me.

I'm only thirty, but the weight of this stress pushes so hard

on my chest
And sometimes, I literally feel like I can't breathe.
You said I'd have peace and joy, but that can't be
Because I'm so sick of church politics and religious greed,
I had to take back my life.

I don't want you, and I don't need you. I've spent my whole life looking for you, but I still can't see

you.
And maybe that's because you're invisible
I hope you're enjoying Heaven, because down here I'm
miserable.

In Sunday school, they told me Jesus loves the little

children.

So where were you in Parkland when that gunman

showed up to kill them? I guess you had the day off, didn't you, Jesus? I'm doubting everything these fake pastors feed us. You do nothing when radicals attack us and beat us. Do you even care about the way that they treat us? It's like you turn a blind eye, and you don't even need us. My eyes are far from blind, and I'm not turning or shutting

them. I've spent 30 years of my life with my nose in your book,

just studying And where did that ever get me except confused and

anxious? Half of what I read felt aloof and ancient. Your Holy Book was written 2000 years ago.

I sat in the pews scared as a kid, and my tears would flow And I prayed for dad to be healed with a miracle. You turned water into wine, but in my eyes, you couldn't

take that water from mine. You never came to save the day, and everything dad built

for 35 years, you had double-minded men take away.

And I know they'll get theirs someday, but I'd rather slit my throat than sit under another corrupt elder board Monday to Sunday.

I grew up in a cult, and I got told you're everything. You're

not.
And I'm standing here right now with everything that I got
And I don't have much to offer you.
As a kid, I'd sit under that preaching and doze off in the

pew And I'd wake up to people picking me up and passing me

around "He's gonna grow up to be the next Billy Graham," they'd

say around town. But every one of those fakes bailed on me when I was

down. A church pew kid who found out religion is nothing but a

cult. When I woke up, I split from that place like Usain Bolt. And I left the wannabe-elect and ran to the only thing I

believed to be true.

I'm here right now telling you what you need to do.

I need you to erase every memory of that place and the

lies I was taught. And if you want me to be strong, I can try, but I'm not. I need you to rescue me from everything I saw as a church

pew kid . . . Jesus, take my old thoughts about you, and cleanse me.

(Check publication requirements for your

tournament before performing) Publisher: 897065 Records DK Date (Month/Year): June 2018

Lyrics available online at: https://genius.com/Clayton-jennings-goodbye-religion-lyrics

Church Hurt
Wake up, shake up, get ready for church!
We found the right one after a two-month search.
We like this pastor 'cause he doesn't curse
Our last pastor was the worst
He was so self-righteous.
Satan tempted us, and we were like try us.

We're the perfect family, eye us --
Mister and misses pious
And we go to church in our nice little Prius.
First at the potluck, there if you need us.
And when the offering plate gets passed, we promise

you'll see us.
Look at how bad these heathens wanna be us.
We love our money, in God we trust.
Big donation means our name on the bus.
Look at us, look at us,
We don't go to church to worship, we go for the rush

We live two houses down from the church. My mom works in the lobby and sells their merch. Welcome to the Holy Church of Jesus the Nazarene Christ If you donate enough money, it'll change your life. I'm trying to figure out my own In and out of boys' homes.

Almost 18, can't wait to get treated like I'm grown. Hated church ever since Dad left us alone. He ran off with a deacon's wife who lived down the road. And this Sunday, yeah, it's Father's Day.

It's gonna be awkward and odd to stay.
And I know fifty people are gonna come up to pray
"Lord, take their pain away"
But it'll stay right where it is.

My breathing gets heavy, and I ball up my fists.
I'm done worshipping Jesus. . .
So look at me, what's the matter?
I'm the guy four rows back getting yelled at by the pastor.
Little does he know, my homelife's a disaster.
Why can't he tell me about who I am in God?
Why does he always have to tell me who I'm not?

(Check publication requirements for your

tournament before performing) Publisher: 897065 Records DK Date (Month/Year): May 2019

Lyrics available online at: https://genius.com/Clayton-jennings-church-hurt-lyrics
```

---

## IC-1516: Blue Front

- Title: Blue Front
- Author (byline): Martha Collins
- Work: Not specified
- Publisher: Graywolf Press
- Publication date as stated: May 2006
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1384
- Already set (do not supply): none

### Source block (context only)

```text
Author: Martha Collins
ISBN: 978-1555974497
Publisher: Graywolf Press
Date (Month/Year): May 2006
```

### Introduction (context only: never use it for content warnings)

```text
Martha Collin’s father, as a five-year-old boy, sold fruit in front of the Blue Front Restaurant in Cairo, Illinois, in November 1909. What he witnessed there and then, along with the reported 10,000 spectators, is shocking.

Blue Front by Martha Collins
```

### Performance text (classify this)

```text
(Pg 3) He was five. He sold fruit on the street

He sold fruit. People came He made change

came to see him make change

(Pg 14) Welcome to Cairo

(Pg 4) the street was Commercial
Dowling Pressing
Saloon Drugstore Opera House
Three States Buggy Champion Tools
Blue Front Restaurant
(Pg 5) a town where people lived
together black and white

(pg 64) Eleven White churches Eleven black churches

(pg 5) couldn’t look out the same
window couldn’t read
the same books laundry
couldn’t be washed
in the same machines

water came from the same source but couldn’t be drunk from the same fountains

(pg 13) couldn’t be sworn in on the same Bible

(Pg 28) couldn’t read the same books read only the others’ old couldn’t be served in restaurants only backdoor take-out kitchens couldn’t swim in the swimming pool or skate at the skating rink

(Pg 8) Springfield [247 miles away and a year earlier] in 1908 a black was accused of killing a white another black of raping a white where in 1908 a mob finding the prisoners gone burned the transporting car destroyed 24 black businesses 40 black homes killed 2 successful black and also accidentally 4 whites

Where in 1908 events occurred that led a 1909 Cairo paper to say its citizens were not moved by race prejudice, nor did they permit themselves to be led into wanton destruction of property, or the taking of innocent lives, as in Springfield

(Pg 9) my father he sold fruit on the street

(pg 16) he sold fruit in front of the Blue Front he was five he could make change

(pg 10) someone must have held him up his uncle his father’s shoulders so he could see

(Pg 17) 10,000 including children on parents’ shoulders who saw what occurred in November 1909

(Pg 19) it is supposed that it is believed that Miss
Anna Pelly Miss Annie Pelley Miss Anne
Miss Pelly age 24 age 22 who worked
In the Pupkin Dry Good store and lived
an orphan who lived with her married sister

(Pg 9) my father (Pg 19) was five would not have seen he could have known the little girl who found the body she was seven or three but that would not have been till the next day

It is supposed she was assaulted on Elm near her home it is believed she struck

(Pg 20) her assailant who gagged with such cruel force it is thought he carried her into the alley the ground showed she was dragged it is known she was outraged not a doubt and strangled a virgin unquestionably pure

(Pg 21) said him because she was large and he
was larger he was large enough said
him because she was white and he
was black and could have therefore
must have necessarily him because
Was what they said it always was was why they said
they had to must but it wasn’t always rape (alleged) it wasn’t
always murder (alleged) it wasn’t always even alleged

(Pg 22) bloodhounds got the scent from the flour-sack cloth found in the mouth led authorities

to Poplar Street then more hounds more to the same place and later all the way to the city jail

Where Will ‘Froggie’ James Will the Frog Will alias Frog who drove for Cairo Ice and Coal

Who stayed with Loving Green who stayed with Georgia Cooper

To Poplar Street the house of Loving Lovey Lovie Green a negress of bad repute where James stayed she was found

Washing a cloth that exactly matches no
a similar cloth
Will James was arrested while driving his wagon
(Pg 23) no scratches blood
no missing items

But Anna Pelley’s sister said he delivered ice last summer he was insolent she had complained

(Pg 44) he was seventeen once too he could have gone to school Sumner High

(colored) had been in town since the 1883 protests

But we do not know
if he went to school
above average intelligence
says a 1910 book but adds
for one of his race

(Pg 23) authorities are taking extraordinary precautions to protect their prisoners because excitement is high in all parts of Cairo

(Pg 3) [My father] was five.
(Pg 32) he wouldn’t have seen the train
make an extra stop for the prisoner
who was spirited away from jail
and into the sheriff’s hands

mutterings of lynchings heard all day would he have heard?

there may be a lynching tonight

(Pg 33) at nine the mob went to the city jail they searched the cells wooden and steel struck matches threatened to lynch the police chief and jailer if they would not produce

the mob was composed almost entirely of strangers

(Pg 32) there may be a lynching tonight

(Pg 38) hang

As a mirror on a wall, or the fall
of a dress.
to fasten to dry.
so the act of doing it
changes the verb, tense not
quite right. With rope, like a swing
from a tree, from a pole, like a flag

In the night, in the air (Pg 50) the victim hanged, though not on a tree

There were trees on those streets
trees that shaded the fenced-in yards of the large
Victorian houses
trees that were known to the crowd

Not on a tree
they used a steel arch
with electric lights, and later a lamppost, this
was a modern event, the trees were not involved.

(Pg 51) a crowd waited at Union Depot four
doors down from the Blue Front
(Pg 9) my father he sold
fruit on the street

(pg 16) he sold fruit in front of the Blue Front

(pg 51) the prisoner dragged to Eight and Commercial

would his father and uncle
have carried him joined
men women and children filled from side
to side the entire width of the 100-foot street
a wild rush flashes of gunfire shouts

Would he have understood
as they neared the arch
10,000 people massed together
a great angry wave of humanity shouted
‘You dog! You black brute! Kill him! Burn him!’

Would he have understood

(pg 52) when someone turned on the lights on the arch flooding the street the victim the crowd

He would have clearly seen

When they raised the victim when the rope broke and the living body fell

he would have seen

when they dragged the victim fifty feet shot 500 bullets into him dragged him heavy to throw to the river but changed their minds

He would have seen When a woman lit the fire while the crowd danced and shrieked

And while the body was burning they cut off the half-burnt head cut open the chest cut out the heart for souvenirs

He would have seen

When they placed the half-burnt head in a park on a hitching post / a tire stick / a pole

He would have seen (pg 55) he was five

(pg 59) Children were often there they were being taught.

(pg 63)

[The Belleville Illinois News Democrat reported it this way on November 12, 1909]

In ferociously dramatic fashion the infuriated populace staged a tragedy. The pent-up fountains of human passion, human resentment, and human revenge broke forth. A so-called mob outbreak is as much a magnificent and grand natural phenomena as a cyclone or an earthquake, or a thunderbolt or a flood is, and it is much more unerring, more just and more terrible. The curtain has dropped. The band has ceased to play, the crowd is gone, the lights are out, the house is dark and it is over. The outburst has done its work of purifying and of cleansing, and in that way it has fully accomplished its heaven-destined purpose.

(pg 64) Eleven White churches Eleven black churches

Eleven white churches heard . . .

The failure of civil authorities to maintain law and order

the lynchings it seems were necessary to arouse the people to startle

the worst class of criminal
is the criminal negro, the worst
creature on earth, the politician
has patted this class on the head as one
pats a dog but you would not pat a mad
dog with your hand, you would use a club

The papers did not record what was said in eleven black churches

(Pg 9) my father he sold
fruit on the street
(pg 16) he sold fruit in front
of the Blue Front

He would have seen (pg 55) he was five

(pg 77) And the last day [the day before my father died] he said You know this would could be

A better place just

Promise me that you will help he waited

(pg 16) he sold fruit in front of the Blue Front

(pg 77) he made change may I help you please make change
```

---

## IC-1517: Body of an American

- Title: Body of an American
- Author (byline): John Dos Passos
- Work: 1919: Volume Two of the U.S.A. Trilogy
- Publisher: Mariner Books
- Publication date as stated: May 2000
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 949
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Dos Passos
Book: 1919: Volume Two of the U.S.A. Trilogy
ISBN: 978-0618056828
Publisher: Mariner Books
Date (Month/Year): May 2000
```

### Introduction (context only: never use it for content warnings)

```text
The bodies of many soldiers killed in World War I could not be identified. To honor them, the remains of one were brought to the U.S. Capitol to lie in state, and on Armistice Day 1921 they were ceremoniously buried in Arlington National Cemetery. The tomb bears the inscription "Here rests in honored glory an American soldier known but to God." Congress later directed that an "Unknown American" from subsequent wars -- World War II, Korea and Vietnam - - be similarly honored. Because of the development of DNA technology, the Unknown Soldier from the Vietnam War was recently exhumed and identified. There may never be another unknown soldier. At this time of our continued war on terrorism throughout the world it seems fitting to reflect upon our first world crisis with John Dos Passos’s tribute to all those young, unidentified men of WWI, who gave up their lives in honor of their country . . . Body of an American by John Dos Passos.
```

### Performance text (classify this)

```text
WhereastheCongressoftheunitedstatesbyaconcurrentre solutionadoptedonthe 4thdayofmarchlast-authorizedtheSecretaryofwartocausetobebroughttothe unitedstatesthe body of an American whowasamemberoftheAmericanexpeditionary forceineuropewholosthislifeduringtheworldwarandwhosei dentityhasnotbeenestablished forburialinthememorialamphitheatreofthenationalcemet eryatarlingtonvirginia In the tarpaper morgue at Chalons-sur-Marne in the reek of chloride of lime and the dead, they picked out the pine box that held all that was left of enie menie minie moe plenty of other pine boxes stacked up there containing what they’d scraped up of Richard Roe and other person or persons unknown. Only one can go. How did they pick John Doe? . . .

how can you tell a guy’s a hundredpercent when all you’ve got’s a gunnysack full of bones, bronze buttons stamped with the screaming eagle and a pair of roll puttees?

. . . and the gagging chloride and the puky dirtstench of the yearold dead . . .

The day withal was too meaningful and tragic for applause. Silence, tears, songs and prayer, muffled drums and soft music were the instrumentalities today of national approbation.

John Doe was born (thudding din of blood of love into the shuddering soar of a man and a woman alone indeed together lurching into and ninemonths sick drowse waking into scared agony and the pain and blood and mess of birth). John Doe was born and raised in Brooklyn, in Memphis, near the lakefront in Cleveland, Ohio, in the stench of the stockyards in Chi, on Beacon Hill, in an old brick house in Alexandria Virginia, on Telegraph Hill, in a halftimbered Tudor cottage in Portland the city of roses, in the Lying-In Hospital old Morgan endowed on Stuyvesant Square, across the railroad tracks, out near the country club, in a shack cabin tenement apartmenthouse exclusive residential suburb; scion of one of the best families in the social register, won first prize in the baby parade at Coronado Beach, was marbles champion of the Little Rock grammarschools, crack basketballplayer at the Booneville High, quarterback at the State Reformatory, having saved the sheriff’s kid from drowning in the Little Missouri River was invited to Washington to be photographed shaking hands with the President on the White House steps; —

though this was a time of mourning, such an assemblage necessarily has about it a touch of color. In the boxes are seen the court uniforms of foreign diplomats, the gold braid of our own and foreign fleets and armies, the black of the conventional morning dress of American statesmen, the varicolored furs and outdoor wrapping garments of mothers and sisters come to mourn, the drab and blue of soldiers and sailors, the glitter of musical instruments and the white and black of a vested choir— busboy harveststiff hogcaller boyscout champeen cornshucker of Western Kansas bellhop at the United States Hotel at Saratoga Springs office boy callboy fruiter telephone lineman longshoreman lumberjack plumber’s helper, worked for an exterminating company in Union City, filled pipes in an opium joint in Trenton, N.J.

Y.M.C.A. secretary, express agent, truckdriver, fordmechanic, sold books in Denver Colorado: Madam would you be willing to help a young man work his way through college?

President Harding, with a reverence seemingly more significant because of his high temporal station, concluded his speech:

We are met today to pay the impersonal tribute; the name of him whose body lies before us took flight with his imperishable soul . . .

as a typical soldier of this representative democracy he fought and died believing in the indisputable justice of his country’s cause . . .

by raising his right hand and asking the thousands with the sound of his voice to join in the prayer:

Our Father which art in heaven hallowed by thy name . . .

John Doe’s heart pumped blood: alive thudding silence of blood in your ears

down in the clearing in the Oregon forest where the punkins were punkincolor pouring into the blood through the eyes and the fallcolored trees and the bronze hoopers were hopping through the dry grass, where tiny striped snails hung on the underside of the blades and the flies hummed, wasps droned, bumble-bees buzzed, and the woods smelt of wine and mushrooms and apples, homey smell of fall pouring into the blood,

and I dropped the tin hat and the sweaty pack and lay flat with the dogday sun licking my throat and adamsapple and the tight skin over the breastbone.

The shell had his number on it.

The blood ran into the ground.

The service record dropped out of the filing cabinet when the quartermaster sergeant got blotto that time they had to pack up and leave the billets in a hurry.

The identification tag was in the bottom of the Marne.

The blood ran into the ground, the brains oozed out of the cracked skull and were licked up by the trenchrats, the belly swelled and raised a generation of blue-bottle flies.

and the incorruptible skeleton,

and the scraps of dried viscera and skin bundled in khaki

they took to Chalons-sur-Marne
and laid it out neat in a pine coffin
and took it home to God’s Country on a battleship
and buried in a sarcophagus in the Memorial
Amphitheatre in the Arlington National Cemetery
and draped the Old Glory over it
and the bugler played taps

and Mr. Harding prayed to God and the diplomats and the generals and the admirals and the brasshats and the politicians and the handsomely dressed ladies out of the society column of theWashington Post stood up solemn

and thought how beautiful sad Old Glory God’s Country it was go have the bugler play taps and the three volleys made their ears ring.

Where his chest ought to have been they pinned

the Congressional Medal, the D.S.C., the Medaille Militaire, the Belgian Croix de Guerre, the Italian gold medal, the Vitutea Militara sent by Queen Marie of Rumania, the Czechoslovak war cross, the Virtuti Militari of the Poles, a wreath sent by Hamilton Fish, Jr., of New York, . . . . All the Washingtonians brought flowers.

Woodrow Wilson brought a bouquet of poppies.
```

---

## IC-1518: Borders, Accents and Weapons

- Title: Borders, Accents and Weapons
- Author (byline): Denice Frohman
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1340
- Already set (do not supply): none

### Source block (context only)

```text
Author: Denice Frohman
Book: Alight: Best-Loved Poems from the 2013 Women
of the World Poetry Slam (Pg 86-89)
On-Line Location:
https://paperzz.com/doc/9383676/alight--the-poems-of-
wowps-2013
ASIN: B00EHA5AYU
Publisher: Bicycle Comics
Date (Month/Year): 2013
Author: Denice Frohman
ISBN: On-Line Transcript Only
Publisher: Narrative Northeast.com
Date (Month/Year): March 11, _____
https://narrativenortheast.com/?p=1952
Author: Denice Frohman
ISBN: On-Line Transcript Only
Publisher: Narrative Northeast.com
Date (Month/Year): March 11, _____
https://narrativenortheast.com/?p=1952
```

### Introduction (context only: never use it for content warnings)

```text
In the words of Julian Castro, former Mayor of San Antonio, “. . . the American dream is not a sprint, or even a marathon, but a relay. Our families don’t always cross the finish line in the span of one generation. But each generation passes on to the next the fruits of their labor.”

These days, more than ever, we need words of wisdom, inspiration, and empowerment in the Latino community. When so many are spewing hateful words, we must remind ourselves of all the talent, goodness and strength that lives within us.

The resilience, work ethic, and beauty of the Hispanic community lifts every corner of this country, and yet . . . There are still some borders you can’t cross by foot.

Borders, Accents and Weapons by Denice Frohman
```

### Performance text (classify this)

```text
Borders (Pg 86-89)
It starts before she gets here.
before the stairs tell her she is alien
to a country that knows her great
grandfather’s Mexican hands all too well.
His fingerprints still echo underneath
the railroad tracks and cotton fields
where bent knees and bent backs
once picked, plucked, pushed work
for more money than he was used to,
but less than he deserved.

For Ana Maria, it begins before the border. She walks with her two Uncles and Abuela through the desert for one week with nothing more than a few gallons of water, and a prayer tucked into their pockets, hoping both will last them long enough.

The sun is an unforgiving God, but any God
is worth having right now.
The wind pushing at their backs
is the grunt of gunshots from drug cartels
and the desperation of a job to employ their stomachs.
Both have been uninvited guests at their doorstep.

so they step, step,
Ana Maria’s small hand clutches the bottom
of her Abuela’s dress,
another step,
her mother waits for her on the other side
hoping that her face still sings of home like it used to.
another step,
She is too young to know what “border” means,
she thinks that people
are just family members who haven’t met yet.

After they arrive, she will learn there are some borders you can’t cross by foot.

Ana Maria is now 10 years old.
She’s learned enough English to translate for her parents,
but says that her thick accent is still a problem
she tries to fix by leaving it in her locker.
When her teacher calls on her to read
she tries to speak proper. Like proper has a sound.

She pushes her tongue down so it doesn’t roll her “r’s,”
but she trips on the flatness of the syllables
that usually bounce with too much salsa.
She tries to rattle out the kinks in her speech,
but her tongue is a stubborn dancer.

The two boys behind her don’t know how to do long

division, but they know what a wetback is, and that Ana Maria has braids, and that Ana Maria’s hair is thicker than their sister’s, and they don’t know how they know, but they know how to treat difference when they smell it. So they say things like, “Go back to your country,” as if their Irish ancestors never walked through Ellis Island.

Ana Maria is now 16.
Her father works 18-hour days as a dishwasher.
Her mother cleans houses she’ll never get to live in
so that Ana Maria can sit in a college classroom
and say, “I am here.”

But her guidance counselor says she can’t get financial aid, or the in-state tuition rate, because of her status.

She says it like an apology.

Ana wonders if her family ever crossed the border, or if they are just stuck inside another one, aggravating it like a sore.

Her guidance counselor stands in front of her, with a mouth full of fences.

There are some borders you can’t cross by foot. Borders, I tell her, that can only be crossed by stubborn backbones

so if they ask you for your papers, show them your skin, wear your tongue like a cape, throw up your fist, like a secret you can’t keep any longer, they can’t keep you any longer, afraid you can’t ever afford to drive or dream.

So if they come for you, tell them in the language you know best, that you are not scared anymore.

TRANSITION

The language I know best is Spanish. Mi familia habla español casi exclusivamente en casa. And I often help translate for them. I am blessed with two languages – Spanish and English. But my mom? She holds her accent like a shotgun . . .

Accents
my mom holds her accent like a shotgun,
with two good hands.
her tongue,
all brass knuckle
slipping in-between her lips.
her hips are all laughter
and wind clap.
she speaks a sancocho of spanish and english,
pushing up and against one another in rapid fire.
there is no tellin’ my mama to be “quiet.”
she don’t know “quiet.”
her voice is one size
better fit all and you best not
tell her to hush. she waited
too many years for her voice to arrive
to be told it needed house-keeping.
english sits in her mouth, remixed
so “strawberry” becomes eh-strawbeddy
and “cookie” becomes eh-cookie
and kitchen, key chain, and chicken
all sound the same.
my mama doesn’t say, “yes.”
she says, ah ha
and suddenly
the sky in her mouth
becomes a Hector Lavoe song.
her tongue
can’t lay itself down
flat enough
for the english language.

it got too much hip.
too much bone,
too much conga,
too much cuatro
to two step.
got too many piano keys
in between her teeth.
it got too much clave,
too much hand clap, got
too much salsa to sit still.
it be an anxious child
wanting to make play-doh
out of concrete. english be too neat
for her kind of wonderful.
her words spill in conversation
between women whose hands are all they got.
sometimes our hands are all we got,
and accents remind us that we are still
bomba, still plena.
say, “wepa!”
and a stranger becomes your hermano.
say, “dale!”

and a crowd becomes a family reunion.
my mama’s tongue is a telegram from her mother
decorated with the coqui’s of el campo,
so even when her lips can barely
stretch themselves around english,
her accent
is a stubborn compass
always pointing her
towards home.

TRANSITION

Families are safe havens . . . as they should be. Another safe haven should be our schools. But for students, especially students of color, 'Do You Have Weapons?' is heard more often than 'Do You Have Dreams?' Poet Denice Frohman points out that there are many manifestations of violence. Not just the physical, but something cultural, emotional and psychological that must be addressed.

Weapons At entrance of a West Philadelphia high school, an officer with a gun perched on each waist, asks me if I have any weapons. I hold up my book. He doesn't find that funny. Tells me to empty pockets, walk through metal detector. 8:03am. I wait for 2 students to pass through first. Already I wonder what they have learned. I am escorted to an auditorium, where there are 130 Black and Latino students. We talk about hip-hop, they think poetry is what old white people do. I tell them my favorite poem is "Ms. Fat Booty"

because I like the storytelling. They giggle as if they are still kids. One girl shouts her favorite song is, "Rack City, bitch!" And the whole room explodes in unison, their bodies bouncing as if they were dancing on trampolines. I ask them if they have dreams. 11 students raise their hands, barely above their shoulders as if they were sitting in History class unsure of the right answer. One student in the first row named Luciano is waiting for me to tell him what page to turn to. One student in the first row named Luciano is waiting for me to tell him what page to turn to. Another student, in the 8th row studies my face, trying to decide if this is a trick question. There is no right answer, I say but they are far too comfortable with the right to remain silent.

So I ask them do you have a family member in prison, 122 students mechanically raise both of their hands, as if a string, tied around their wrists, was yanked for them. Their hands remain up this time. And I can see all of them, perfectly. I heard the newly built prison a few miles away bought their test scores as wallpaper. The principal is now staring at me in anticipation of what I have to say next. He is afraid they will leave with weapons. I am afraid they will not know the ones that already exist.
```

---

## IC-1519: Bouquet of Red Flags – A Collection

- Title: Bouquet of Red Flags – A Collection
- Author (byline): Taylor Mali
- Work: Bouquet of Red Flags
- Publisher: Write Bloody Publishing
- Publication date as stated: Nov 2014
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1045
- Already set (do not supply): none

### Source block (context only)

```text
Author: Taylor Mali
Book: Bouquet of Red Flags
ISBN: 978-1938912511
Publisher: Write Bloody Publishing
Date (Month/Year): Nov 2014
* Kids say the darnedest things, and every line in this
poem is based off one written for me by students at the
International School of Beijing in the spring of 2014. I
asked them all to make lists of things: favorite hiding
places, things they hear from their family a lot, games
they played as children, and popular punishments in
their family. – Based on the form of the poem ‘Origins'
by Jeffrey McDaniel (https://upittpress.org/wp-
content/uploads/2019/03/9780822959953exr.pdf)
```

### Introduction (context only: never use it for content warnings)

```text
Our families teach us, intentionally or not, how we see the world . . . a world where contradictions can and do live side by side. The words and memories echo even more loudly upon the death of a parent – or in Taylor Mali’s case both parents -- sometimes playing an endless loop of emotion that we can’t easily quiet.

You see, our relationships are preserved, not just in objects or people, but in the way they are remembered.

Poems from Bouquet of Red Flags by Taylor Mali
```

### Performance text (classify this)

```text
Magnifies an Object Ten Times
“Magnifies an Object Ten Times” is what it clearly said
on the handle of the magnifying glass
my father received on his fifth birthday.
He took it as a warning; the birthday gift
would only work its magic ten times
and no more, becoming, after that,
just a small round window with no miracle,
toy giant's monocle, a circle of simple glass.

And so he went about his days with curious thrift, weighing how much he needed to see any part of the world up close, observing as best he could with his own eyes first, thinking, Do I need to see that dead bug big? That dandelion, that blade of grass, that wriggling moth in the spider’s web? I can imagine most of nature’s gifts and crimes. Best not to waste one of my ten precious times.

He lost count of how many miracles he had left, and for weeks after half expected the magic of the glass to simply stop. And I have asked him to tell me of the thrilling moment he realized, or was told, "ten times" in this context simply meant tenfold and not ten instances, but he cannot remember. Likewise the joy that must have come with such a limitless epiphany. But what he does recall and says most he misses still is the way the magic made him see the world the rest of the time, not through the glass, but all the time he thought that magic would not last.

My Deepest Condiments

I send you my deepest condiments was in no way what my old friend meant to say or write or send the night she penned a note to me one week after my father died.

Not condolences, or sentiments, she sent me her deepest condiments instead, as if the dead have need of relish, mustard, and ketchup on the other side.

O, the word made me laugh
so hard out loud it hurt!
So wonderfully absurd,
and such a sweet relief
at a time when it seemed

only grief was allowed in
after my father's death,
sweet and simple laughter,
which is nothing more than breath
from so far deep inside

it often brings up with it tears.
And so I laughed and laughed
until my sides were sore.
And later still, I even cried
a little more.
TRANSITION
Memories of childhood come flashing back . . .

Shut up and You Know I Love You
* Author’s note about this poem
They're from kitchen cabinets, behind the poison
and insecticides.
They're from locked bedroom doors.
They're from dolls and Hunger Games,
rock, paper, scissors,
three lives, and you're dead.
You're out.
You are not my friend.
No. Not it.
That seat is taken.

They're from shut up and you know I love you.

They're from get out of my room. They're from stupid. They're from fat, ugly, and I hate you.

Shut up and you know I love you.

They're from you're not a part of the real family. You're adopted. Why do you keep hitting yourself?

Why do you keep hitting yourself? Look what you made me do. Mom and Dad said you were a mistake.

They're from please don't tell. This can be our secret. Two hours of piano every night before dinner. Do you want the stick? Do I need to get the belt? Don't make me tell you again. You brought this on yourself.

They're from tears of laughter, and tears,
and I never wanted any of this to happen.
I am so sorry. I promise I'll never do it again.
They're from you know I love you.
This is going to hurt me more than it hurts you.

TRANSITION

Within weeks of his father’s death, Taylor Mali’s mother also passed away. Her name was Jane and “The Troubled Muddle of the Midfield” describes Mali’s reflections of the day she died . . . “not knowing how to help or where to run.”

The Troubled Muddle of the Midfield The afternoon of the evening my mother was to die I lingered on the sidelines of a soccer game too long just to watch the Burden twins do what they do best.

Six minutes between the two, offensive sister and her defensive twin separated by only six minutes, except for the entire troubled muddle of the midfield, that huddled gaggle of other girls who ran crookedly between the two sisters like a sad flock on stilts.

Jane was the goalie, and she repelled every shot
she did not devour, while Jane -- The Other Jane,
that was her name,
or rather what we called the younger
just to keep them straight
(instead of questioning the inane logic of their names,
How insane must you be to name both your daughters
Jane?) --
she reigned over the field at center forward,
left foot like a laser beam.

The afternoon of the evening my mother was to die
I prepared two weeks of lesson plans
for the teachers who would take my place
while I was away.

And I made a wish that the Girls' Varsity Soccer Team
would one day have a more capable midfield
instead of the cacophony of awkwardness,
the never knowing where to go
to be of any use to anyone,
which explains the long balls arcing downfield
from the massive volley of Jane
to the sparkling feet of The Other Jane,
juking her way through the stupefied topiary of opposing
players.

I suspect there are several ways a man can deal with grief, but the afternoon of the evening my mother was to die I watched the Burden twins beat their rivals seven-zero, watched them for longer than I should have, knowing I had a four-hour drive to the bedside of still another Jane and the near certain promise of mourning.

My mother died without me.
And it has now been years since
the missing of that moment,
the lingering in this riddled life she suffered
waiting for me to tell her
what I only hope she knew already.

Still now sometimes when I think of her,
I see Jane and The Other Jane
and the wonder of the way they moved,
the one never letting anything in,
the way the other made motionless the world.
And also the confusion of everything in between,
midfield of the twin Burdens,
the not knowing how to help or where to run.
```

---

## IC-1520: Bouquets

- Title: Bouquets
- Author (byline): Diane Wakoski
- Work: Virtuoso Literature for Two & Four Hands
- Publisher: Doubleday
- Publication date as stated: March 1975
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 440
- Already set (do not supply): none

### Source block (context only)

```text
Author: Diane Wakoski
Book: Virtuoso Literature for Two & Four Hands
ISBN: 978-0385004633
Publisher: Doubleday
Date (Month/Year): March 1975
```

### Introduction (context only: never use it for content warnings)

```text
The bystander is a modern archetype, from the Holocaust to the genocide in Rwanda to the current environmental crisis,” says Charles Garfield, a clinical professor of psychology at the University of California, San Francisco. Why do some people respond to the obvious needs of others while some people turn away? Diane Wakoski examines this same phenomenon in her poem Bouquets.
```

### Performance text (classify this)

```text
Bouquets

of blood/ on the street. I know what it is, saw the man fall (from his bicycle when his child stuck his shoe in the spokes), saw his neighbor, the lady who wanted to help, bring out the roll of paper towels, thinking

to wipe up the blood from the asphalt after the ambulance left/ but giving up her purpose knowing she meant to wipe away memory, perhaps.

I saw the ambulance leave, carrying him with the flesh and bone gone from his nose, the blood covering one eye as if in some child's coloring book, a 3-year old had scribbled red over a raccoon's face, and I sat in a foreign household and watched a neatly clad housewife bring out her roll of paper towels, thinking to wipe up the blood off the street.

What restrained her?
I wonder.
Knowing there was so much there perhaps?
A pool so big,
the parodying of all those tv ads-"It's absorbent!"
Suburban Housewife, tell all of our listeners now just
how absorbent it is!"

"You wiped up a whole pool of blood spilled on the street!"

"Now that is something, isn't it!"

all you listeners out there,
and the exclamation points follow everything, remember
you can wipe anything away
with paper towels.
But what impressed me,
the voyeur,
the foreign visitor to this American suburb,
was that this housewife walked out, with her roll of
paper towels, and then she silently,
almost. stealthily, put them behind her back,
-ashamed, I wonder
and walked back into her house
without using them.
The pool of blood too big?
No, not for the absorbent towels.
Perhaps some sense of history
that you cannot wipe a man's blood from the pavement
when his child has thrown him there.
The bouquet

of blood
blackens,
wears itself into the street, the stain a reminder
of a simple deadly accident.

Of life.
I remember the simple dignity
of the neighbor,
the housewife who wanted to help,
bringing out her roll of absorbent paper towels
and then not touching the pool of blood,
refraining from wiping up a man's blood as if it were
some sticky mess
her kids dropped on the floor.

Daily life dulls us.
Going to the office,
cleaning up the messes of others,
and yet some sensitivity was left to this woman.
She understood, looking at the pool of blood scraped out
of the man
her neighbor's face, as if he had been strip-mined by
some exploiting industrialist,
she knew that she could not just wipe his blood from the
street with her paper towels.
She understood history,
memory,
record.
And I will not forget her,
a common housewife,
who rose above her nature.
```
