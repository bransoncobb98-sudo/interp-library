# Classification request: batch 1 of 63 (40 records, IC-0001 to IC-0040)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-001-reply.json`.

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

## IC-0001: 26 Pebbles

- Title: 26 Pebbles
- Author (byline): Eric Ulloa
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Oct 2017
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: JENN, MIKE, SUPERINTENDENT MESSAGE, ACTOR 6, DARREN, CAROLE, FATHER, MICHAEL, PRESIDENT OBAMA’S SPEECH, RABBI, CARRIE, ACTOR 2, ACTOR 3, ACTOR 4, ACTOR 5, GEORGIA, ACTOR 1, STARR, FATHER WEISS, BILL, SALLY, JOE, CARLA, JULIE, YOLIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1521
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eric Ulloa
ISBN: 978-0573706646
Publisher: Samuel French, Inc.
Date (Month/Year): Oct 2017
```

### Introduction (context only: never use it for content warnings)

```text
On December 14, 2012, Adam Lanza killed his mother, then walked into Sandy Hook Elementary School and killed twenty-six innocent souls before taking his own life. These twenty-six innocent deaths, like pebbles thrown into a pond, created ripples and vibrations that were felt far beyond the initial rings. This is the story of those vibrations. Playwright Eric Ulloa conducted interviews with members of the community in Newtown and crafted them into an exploration of gun violence and a small town shaken by a horrific event.

26 Pebbles by Eric Ulloa
```

### Performance text (classify this)

```text
JENN: (Pg 13) Communities like ours don’t just form themselves. A true sense of community comes from strangers wanting to come together and know one another for the greater good of their neighborhood. And we need more of that nowadays, right?

MIKE: You know on [December 13, 2012], you didn’t know where Newtown was or that we had a flagpole, or a creamery, or a parade. Obscure was nice.

JENN: He’s right. Obscurity was nice. (Pg 14) They say the world is connected through six degrees, but out here in Newtown, it’s about one. And if you were born and raised here, everyone is family. (Pg 20) There are a lot of people from other areas that moved here. [See] Newtown was written up as one of the top ten places to raise kids.

SUPERINTENDENT MESSAGE: (Pg 22-23) All Newtown public schools are in lockdown due to a shooting.

MIKE: I hear sirens from a distance, like rally far out. We were walking back to the office and at the Subway there were four teachers. I intercepted them and I said, “What’s going on?” And they were in shock and tears. And they said, “Something very very bad. Gunshots. Many gunshots.”

ACTOR 6: All clergy go down to the firehouse immediately. All clergy down to the firehouse immediately!

JENN: I got a call saying, “You can pick up your kids at the school, at the firehouse.

MIKE: It’s as if somebody open the floodgates right in that moment, and every personnel, police, you name it, first responders in the world was coming.

JENN: (Pg 25) I, I just can’t even describe how panicked it started to get for me because [my husband] wasn’t answering his phone and the texts were flying. “Do you have him?” Where’s our son? What’s going on?” An I was just leaving him these messages and starting to get that rising panic inside.

DARREN: They said the shooter inside was dead. They said, they, uh, he was (Sniffles) He was found dead in a classroom, found in a classroom. I knew that was the worst case. Shoot . . . shoot . . . shooter killing himself. I – I knew he didn’t just walk in and shoot himself in front of the kids. (Sniffles) And the numbers, we just watched in horror, as it went from a handful . . .to a dozen . . . twenty. (Beat)

CAROLE: (Pg 29-30) The safety of this little town has been shattered. I think that’s the biggest thing that happened her, the shattering of the illusion of . . . our little world. How did this happen to us? What? What just happened here?

FATHER: Don’t get me wrong, I think the story needs to be out there. But I’d never seen anything like it in my life. I mean there were literally hundreds and hundreds [of reporters] there in just the first few hours.

CAROLE: Horrible. Invasive. There was no escape and there was no time for us to grieve. We would all be watching everybody and when somebody went down . . . I mean at the grocery store people would, would go down to their knees and there was a hive of people l that would be there to just let them cry. You know? And you can’t, you can’t do that with the media because it’s so intrusive. They just want – many they want you sobbing. They want to see you in pain.

DARREN: (Pg 31) There’s no place within Newtown or Sandy Hook that you could go. It took us to get from our house to Sandy Hook normally, maybe five minutes. The first couple of weeks you’d have to allow at least an hour to get into town because of the traffic jams.

People, news truck(s) – Because the highway sign says “Newtown,” people pull off the highway just to see. Just to see.

JENN: (Pg 32) The next week was just funerals and wakes and – it was – it was pretty indescribable. Responds to the flashes from numerous cameras)

MICHAEL: (Also responding to camera flashes – he yells at the press) Please! Just, just let us mourn.

PRESIDENT OBAMA’S SPEECH: (Pg 33) . . . And that’s what should drive us forward in everything we do. God has called them all home. For those of us who remain, let us find the strength to carry on, and make our country worthy of their memory.

JENN: How could any God let something like that happen?

RABBI: (Pg 36) This was not an act of God, this was an act of man. You got free will and that means that anything could happen. Adolf Hitler can happen. Senseless deaths and shootouts and hold-up and robberies can happen and do happen every day in this country.

CARRIE: He did this, it wasn’t God’s doing. He chose to do this. But I guess my questions are, well, if he had a mental illness then it isn’t really free will. He can’t help it right? Then my daughter asks me, “Is he in hell?” And we tried to explain: “Well, you know, he was probably sick and he didn’t know what he was doing.” And then she would ask, “Well if he was sick then that means he wasn’t an evil person, so would God forgive him? What if he’s sorry? Does he still have to go to hell?” These are questions that we as adults don’t have the answer for. What does a parent do?

ACTOR 2: (Pg 37) In the shooter’s home, police found the following

ACTOR 3: A seven-foot pole, with a blade on one side and a spear on the other.

ACTOR 4: A metal bayonet

JENN: (Pg 37) I’m – I’m angry. Obviously there was a lot more to this story in terms of his upbringing . . . Just the lack of care that he probably received as a child. Did nobody say anything?

ACTOR 5: Three samurai swords

ACTOR 6: .323 caliber bolt-action rifle

GEORGIA: (Pg 38) Not that I’m blaming any one persons, but the village raises the child. I think one of the biggest problems was his isolation. We’re meant to be connected. And when someone’s not connected . . . bad things start to happen.

ACTOR 1: .22 caliber Savage Mark II rifle

ACTOR 3: New articles on the 2008 shooting at Northern Illinois University

ACTOR 6: And inside his gun safe was a holiday card from his mother, [with] a check for the purchase of his next firearm.

STARR: (Pg 39) [He] had counseling just before the divorce. Three months prior to this incident, he was fine, then he was disturbed that his Dad and brother moved. He had nobody else to talk to. And that just . . . snapped the camel’s back. When he was on medication and in therapy, he was the one who would take his shirt off his back to help you. He did tutoring for the younger.

FATHER WEISS: I always have twenty-eight candles out. I believe in forgiveness. And that is one of the big issues. Is it twenty-six or twenty-eight?

CAROLE: (Pg 40) The thing is, and maybe it’s not appropriate, but twenty-eight people died that day. It wasn’t twenty-six, it was twenty-eight people who lost their lives. Twenty-eights families that mourned.

BILL: There is no difference between a man who’s being chased by someone with a machine gun, and a man who THINKS he’s being chased by someone with a machine gun.” And the sad part is that he was over eighteen years old, and legally there’s not a thing we could do. We’re no different from Mrs. Lanza.

SALLY: I think that his mother did everything she possibly could. There is a point where you are scared, you’re afraid, but it’s your son. And you have hope because he’s not a monster, he’s mentally ill. Some people honestly just don’t know the difference between right and wrong.

JOE: (Pg 41) The only thing any asshole does, is that he succeeds in becoming infamous. And . . . And he will become a mark in a history book, if we let him. How do you bury people like that so people forget them? Because that’s what you need to do. You need to forget them.

CARLA: (Pg 42) There were these people demonstrating outside the National Shooting building. It’s a resource for people who hunt and it’s a very positive organization, and it’s been here for decades. So people were outside it saying . . .

RABBI: (Pg 43) (Leading this protest) “GET OUT OF NEWTON! GET OUT! GET OUT!“ We live in a society of 32,000 deaths by guns alone every year! IF these people died in the battlefields of Afghanistan, we wouldn’t accept it. Yet when it happens right here in the cities of America, we somehow are mysteriously silent.

CARLA: I was just begging, begging for them to stop, stop making – stop perpetuating this hate. There’s so much division now, and it’s very strange, ‘cause it’s like (snaps fingers) overnight. (Beat)

DARREN: (Pg 45) We don’t know all the things that are broken. We’re still discovering them.

JULIE: (Pg 44) They seem to be okay for a while, then my son started to show signs of Post Traumatic Stress Disorder, PTSD. You just have that fear of not being safe. So kids, children, end up just being scared. They weren’t scared of monsters before? Now they’re scared of monsters

JOE: (Pg 53) This all leaves you with a lot of questions, and I don’t think that’s a bad thing. The more people are questioning, the more they’re talking about it. “where do we go from here? What can we learn from this? That’s so cliché, but it’s true. What can we learn from this?

YOLIE: It’s all about how you ripple out, and what these vibrations can be. We are love. We are Newtown. That message says it all.
```

---

## IC-0002: 40 Questions (from Tell Me How It Ends)

- Title: 40 Questions (from Tell Me How It Ends)
- Author (byline): Valeria Luiselli
- Work: Harper’s Magazine
- Publisher: The Harper's Magazine Foundation
- Publication date as stated: February 2017
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, LITTLE GIRL, BOY
- Teaser before the introduction: Yes
- Spoken words (computed): 1952
- Already set (do not supply): none

### Source block (context only)

```text
Author: Valeria Luiselli
Magazine: Harper’s Magazine
ISSN: 2169-7612
Weblink: https://harpers.org/archive/2017/08/forty-questions/
Publisher: The Harper's Magazine Foundation
Date (Month/Year): February 2017
```

### Introduction (context only: never use it for content warnings)

```text
*As a translator, it's Luiselli's task to help these kids, most of whom came alone and were either caught at the border or went to the authorities themselves. Without the assistance of an adult or other family member, these children must answer 40 questions that will determine their fate.

For instance, Question 7 asks, "Did anything happen on your trip to the U.S. that scared you or hurt you?" Luiselli says that children rarely give an honest answer, not because they're lying or evasive, but because the truth is too awful to tell. You see, 80 percent of migrant girls and women who cross Mexico to the U.S are raped along the way. She reminds us that few immigrants abandon their past and brave death to come to America for dark reasons. They come as an expression of hope.

40 Questions from Tell Me How It Ends by Valeria Luiselli
```

### Performance text (classify this)

```text
NARRATOR: I started working as an interpreter for Spanish-speaking children in the NYC Immigration Court in March 2015. On my first day of work, I took the subway downtown and walked to the ominous building at 26 Federal Plaza. Inside, the building branches into hallways, offices, courtrooms, and waiting rooms, with few people you can ask for assistance. It’s easy to get lost. The building is, in a way, a replica of the U.S. immigration system. Some find their way out and some don’t. Those who don’t might remain there forever, invisible specters wandering the hallways, imprisoned in circular nightmares.

NARRATOR: The room where screenings are conducted feels like a small refugee camp, furnished only with benches lined up one after another. At the front, a wooden balustrade cordons off an area for the interviews -- at which children, lawyers, and interpreters sit. Crayons and paper are set at the ends of two large mahogany tables to entertain the younger children. During each interview, the child’s relatives sit on the benches on the other side of the balustrade and wait. It’s against protocol for relatives to join the children during the interviews, since their presence could influence the children’s answers.

I didn’t quite grasp the bigger picture during the first screenings. Blindly, I followed all the questions on the questionnaire, one by one, and translated the answers. What I was really doing was providing backup for the federal government’s decision to create a priority juvenile docket.

Before the immigration crisis was declared in the summer of 2014, minors were given twelve months to find a lawyer before their first court hearing. But then, the Obama Administration created the “priority juvenile docket,” which reduced that window to 21 days. What child can find a lawyer in twenty-one days? The priority docket grouped together cases involving unaccompanied minors from Central America and moved them to the top of the list. For the children involved, being at the top of the list accelerated deportation proceedings by 94%. The priority juvenile docket was the cruelest possible response to the arrival of refugee children -- a backdoor escape route from the reality suddenly knocking at the country’s door.

I recall the first story I heard in court. Perhaps because of a piece of paper he pulled from his pocket toward the end of the interview. Its creases and edges were worn. He unfolded it gently [and] placed it in front of me. He explained that it was a copy of a police report he had filed more than a year and a half earlier. The report stated in capital letters and with some grammatical mistakes, that the subject in question raised a complaint against gang members who waited for him every day outside his high school, followed him home, and had begun threatening to kill him. It ended with a vague promise that the police would “investigate” the situation. [Question #38: What do you think will happen if you go back home? Question #39: Are you scared to return?]

After showing it to me, the boy folded the document back up and put it in his pants pocket, rubbing his palm now and then against the denim, as if he were activating a lucky charm. Originally, it had been a legal document, a complaint filed by a boy hoping to change his life. Now it was a road map of migration, a testimony to the 5,000 miles it had traveled inside a boy’s pocket, on foot, in trucks, across national borders, all the way to an immigration court in a distant city, where it was finally read by a stranger who had to ask: [Question #1] Why did you come to the United States?

This “immigration crisis” -- the sudden surge of Central American children to the United States was viewed as a problem that Homeland Security was “suffering” and that Congress and immigration judges had to “solve.” The political response therefore, always centered on one question: What do we do with all these children now? Or, in blunter terms: How do we get rid of them?

Questions 9, 10, and 11 on the intake questionnaire are: “How do you like where you’re living now?”; “Are you happy there?”; “Do you feel safe?” It’s hard to imagine that these children, considered a burden to institutions and unwanted intruders by a large part of society, soon to face a judge and defend themselves against a removal order, “like” where they are living. (pause)

Often, my daughter asks me: So, how does the story of those children end? I don’t know how it ends yet . . . [but] there is one story -- a story I tell her only in pieces. It begins with two girls in the courtroom. They’re 5 and 7 years old, from a small village in Guatemala. Spanish is their second language. We sit around the mahogany table, and their mother observes from one of the benches in the back. The little girl concentrates on her coloring book, a crayon in her hand. The older one has her hands crossed as an adult might, and she answers my questions one by one. She is a little shy but tries to be clear and precise in her answers, delivering all of them with a big smile, toothless here and there. (to the child) [Question #1] Why did you come to the United States?

LITTLE GIRL: I don’t know.

NARRATOR: [Question #6] How did you travel here?

LITTLE GIRL: A man brought us.

NARRATOR: A coyote?

LITTLE GIRL: No, a man.

NARRATOR: [Question #6, con’t] And where did you cross the border?

LITTLE GIRL: I don’t know.

NARRATOR: Texas? Arizona?

LITTLE GIRL: Yes! Texas Arizona.

NARRATOR: I realize it’s impossible to go on with the interview, so I ask the lawyers to make an exception and allow the mother to meet with us. We go back to question 1, and the mother responds for the girls, explaining things, and also telling her own story. When the younger of her daughters turned two, the woman migrate[d] north, leaving them in the care of their grandmother. She crossed two national borders with no documents. She wasn’t detained by the Border Patrol and after a few weeks she arrived in Long Island. Years passed, and the girls grew up; she remarried; she had another child.

One day she called her mother and said that the time had come: She had saved enough money to bring the girls over. The grandmother noted the instructions and explained them to the girls: A man was going to come for them, a man who would help them get back to their mother. She told them that he would keep them safe.

The day before they left, their grandmother sewed a 10-digit phone number on the collar of the dress each girl would wear. The girls had not been able to memorize the number so she had decided to embroider it on their dresses and repeat, over and over, a single instruction: They should never take these dresses off, not even to sleep, and as soon as they reached America, as soon as they met the first American policeman, they were to show the inside of their collars to him. He would dial the number the rest would follow.

The rest did follow: They made it to the border, were kept in custody, in the hielera (“icebox”). They didn’t remember how many days, but said they were colder there than they had ever been. After that they went to a shelter, and a few weeks later they were put on a plane and flown to JFK, where their mother, baby brother, and stepfather were waiting for them.

That’s how it ends -- but of course it doesn’t end there. That’s just where it begins, with a court summons: a Notice to Appear. Once children receive a Notice to Appear, they have to present themselves in immigration court. It is the children’s responsibility to find a lawyer who can defend their case against the U.S. government attorney seeking to deport them.

The most common forms of immigration relief are special immigrant juvenile status (S.I.J.) and asylum. For a child to apply for S.I.J. status, a court must determine that he or she is impeded from reunification with at least one parent because of abuse, abandonment or neglect, and that return to the home country is not in the child’s best interest. Asylum is granted to people who are fleeing from persecution of their race, religion, nationality, or political opinion. It is not enough that these children have suffered unspeakable harm, that they will continue to fall victim to the targeted violence of criminal groups. The harm or persecution must be proved.

[So] . . . If the child answers the questionnaire “correctly,” he or she is more likely to have a pro bono attorney. In the warped world of immigration, it is a “correct” answer when, for example, a girl reveals that her father is an alcoholic who physically or sexually abused her, or when a boy reports that he received death threats or that he was beaten repeatedly by gang members — and has the physical injuries to prove it. When children don’t have enough battle wounds to show, they will most likely be “removed” to their home country, often without a trial.

The interpreters have no control over the type of legal assistance a child receives. We listen to their stories in Spanish and note key points in English. We must pay close attention to the details and find ways to classify them. We look for categories for each story that may tip the legal scale in a future trial — categories such as abandonment, prostitution, sex trafficking, gang violence, and death threats. But we cannot make up the answers, nor can we lead the children to give us answers that are favorable to their cases.

In my interview with the girls, their answers weren’t really working in their favor. What I needed to hear was that they had been doing hard labor, labor that put their safety in danger; [Question #29: How many hours did you work each day?] that they were being exploited, abused, punished, [Question #32: How often were you punished?] maybe threatened with death by gangs [Question #37: Have you ever been a member of a gang? Any tattoos?] The girls were so young that even if they had a story that might secure legal intervention, they didn’t have the words to tell it. (pause) [But] One boy says . . .

BOY: The gang followed me after school, and I ran, with my eyes closed I ran.

NARRATOR: So I write that down, and then, in the margin, make a note: Persecution?

BOY: And they followed me to school and later they followed me home with a gun.

NARRATOR: So I write that down too, and then make a note: Death threats?

BOY: They kicked my door open and shot my little brother.

NARRATOR: So I write that down too, but then I’m not sure what note to make in the margin: Home country poses life-threatening danger? Not in child’s best interest to return? What words are the most precise ones? All too often I find myself not wanting to write anymore, wanting to just sit there, quietly listening, wishing that the story I’m hearing had a better ending.

I listen, hoping that the bullet shot at this boy’s little brother misses. But it doesn’t. The little brother is killed, and the boy flees. And now he is being screened, by me. His screening, like many others, is filed and sent to a lawyer: a snapshot of a life that will wait in the dark until maybe someone finds it and decides to make it a case.

[Question 40: Who will take care of you if you were to return to your home country?]
```

---

## IC-0003: About Time

- Title: About Time
- Author (byline): Joshua Sands
- Work: Turning Points
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1984
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joshua Sands
Book: Turning Points
Publisher: Tichenor Publishing
ISBN: 0742117014
Date: 2001
```

### Introduction (context only: never use it for content warnings)

```text
Death is the great equalizer. It’s a common factor all of humanity shares. It matters not when, or how or why you died. The fact is, you died…just like everyone else. Just like Hitler, just like Gandhi, just like your great grandmother and mine. For some, it was too soon, for others not soon enough. But for most, it was simply “About Time” by Joshua Sands.
```

### Performance text (classify this)

```text
Two days ago, the organist at my church died. Doris Mantiglia. 86 years old. Lung cancer. Smoked like a chimney for 69 of those years. At the funeral, everyone hummed their mantra: She smoked too much. It was about time. She smoked too much. It was about time.

When a life ends, when the final chapter is entered in the log, our final measure is whether it was about time. We take three bits of data to determine this. Name, age, cause of death. If the death is considered early, it's tragic. Bruce Mickem, 38, aneurysm. What a shame! But if, as in poor Doris' case, it was about time, then there is nothing more to say. It was simply time. All of this psychobabble about how it's the journey that counts. No one remembers the stories. They remember the final destination. The journey is nothing. It's a page 10 story in a small town paper. We merely measured the journey in years. How far did you make it? Well, that's about as far as most people. Racing toward nothing. A journey with a finish line no one can cross.

Three bits of data: name, age, cause of death. Anna Kinder, 92, liver cancer. Kevin Harpring, 65, heart disease. Ty Ackerman, 42, drunk driver.

When I attempted to uncover my heritage - the legacy of my birth parents, I was looking for the journey, but all I found was the final destination. Phil Gregory, 26, gun shot wound to the head. Melissa McClish, 20, died in child birth.

The journey wasn't even a page 10 story.

Indeed, I am one of the selfish. I grew up with two loving parents, yet longed for two more. If that makes me a jerk, so be it. I suppose you're tired of the sob stories: Oh, it's so terrible. I'll never know where I really came from. Something just feels out of place. But for me, something was missing. The story. I could have grown up with my adopted parents - mom and dad, but let's call them Jean and Steve because I need to detach them - and been solidly content if I just knew the story. How did I become an orphan? Tell me more than the three bits of data. No matter what anyone argues, that data does not stand on its own. The beauty of death is that, if you desire, you can determine the number of people at your funeral. There's a curve that's undeniable. If you're an infant, you get a dozen people tops. Your death is too tragic to put on display. You're attendance increases dramatically as you enter school. If you go to college close to your hometown, you peak out. Tons at that funeral. College friends and high school friends alike. Add some church members, maybe an old fast-food boss or two, and they'll all have a good cry. Unless you did something stupid like a drug overdose, in which case all bets are off

You continue to have a decent turn-out at the funeral for a few decades after that. Once you hit 50, your death no longer has the shock factor. Subtract a dozen or two. By the time you hit 60, your peers start dying. Subtract a dozen or two. 70, 80, 90, it's about time. Still, attendance is about the same. People die, but you enter retirement homes. People who you sat with at dinner once now will speak at your funeral and dub you inspirational. Don't live past 90, though. After that, everyone dies. You get your kids who have likely moved far away from home and some grandchildren waiting for the reading of the will. That's about it. No tears either. After all, it was more than about time. Did my parents have a funeral? Were they married? How many people came? Death in childbirth. Add three dozen. Tragic.

I find myself driving to San Francisco. Not exactly an easy drive from Indiana, but it's the summer and college break lasts for another six weeks. Besides, I tell myself if I don't get any information, I've at least heard there's some great bars there. Why San Francisco? It's where the birth certificate is dated. Why didn't I call? Because there isn't a computerized option for " If you know anything about the lives of Phil and Melissa, press 1."

I arrive at a hospital near North Beach and the hospital employees tell me they can give me a COPY of the birth certificate and the names and ages of both parents, who, they inform me like it's some sort of SkyTracker Weather bulletin, are both deceased.

"Phil Gregory, 26, gunshot wound to the head. Melissa McClish, 20, died in child birth," the nurse says.

"Yes, I know. But I want to know more."

"More? What for? They're dead."

"I don't know. Maybe I'd like to know what they liked to do on a Saturday afternoon, or whether they were in love, or whether I inherited my red hair from my mother or from my father. .. "

"Well, I see you have quite an investigation on your hands. Happy snooping! "

Snooping? This is my life.

There is a fourth piece of data that is infrequently used, but can be thrown in for dramatic effect. Irony. If your death is ironic considering the life you lived, you get the fourth dimension. Like Natalie Wood. Scared of the water all her life. Death by drowning. Natalie gets the fourth dimension. Bear Bryant. Alabama football coach for four decades. Says he'll die if he stops coaching. Months after retirement, the Old Bear kicks the bucket. Fourth dimension for him. Why does irony warrant the additional information? Because even if it was "about time," there is something about being able to predict the time that spooks us. Spookiness warrants the fourth dimension.

Did mom die in a spooky way? Maybe she said "This babies gonna be the death of me." That counts. Maybe she had dark dreams where she envisioned a doctor giving her an epidural, then hearing a baby crying, and then the brightest light she'd even seen. That would definitely count. If this were a movie, it'd be nighttime right now. I'd be pulling my Blue Taurus up to the front of a two-story frame house of a person I believed would have all the answers. Instead, it's 92 degrees at 1:30 in the afternoon as I knock on the apartment door of Francesca Stephenson, mother of Melissa McClish. Again, different last names. I guess it didn't matter just makes the story even more convoluted. She lives on a bad part of Market Street - not the place you want to be.

Francesca was a woman in her early sixties. Graying in every place except her eyebrows, which were still a stern black, letting people know exactly when and how she was concerned.

"My name is Chris. Chris Tyree," I say bluntly, as if I know there is no way to dull the news I was about to say.

"Nice to meet you Chris Tyree-did you come over to look at the apartment? They said someone would be by to -"

"Melissa was my mother. ... Melissa ... your daughter. .. "

"Oh," she said with half the energy she once had. "Oh, then you're not here to see the apartment."

"No, Mrs. Stephenson. I'm not."

"I'm supposed to fill in the blanks here, aren't I?"

"Are you able?"

"We'll find out, won't we?"

See, people misconstrue my issues. They think I'm obsessed with heritage. I'm not. I don't even realize that Francesca Stephenson is my grandmother. Doesn't even cross my mind to call her Nan, much less want to. People also think I'm obsessed with dying. Like the reason I want to know about my parents is because I knew they died in tragic ways. That's not it either. I'm obsessed with the final tale of the tape. The three measures that tell the story. When the three measures don't tell the story, I want to know more. So often, the measures suffice. Laura Bancroft, 51, heart attack. She was overweight. It was about time. Cam Fox, 99, died of natural causes one day before his 100th birthday. How ironic. Samantha Stevens, 65, breast cancer. James Carter, 71, urinary tract infection. Hey, it happens.

I imagine myself clairvoyant. I can envision a person's death. My friend, Kristen Carpenter, 82, liver cancer. The dentist, Ryan Overhouse, 60, stroke. The grocery store clerk, Tricia Drake, 21, malaria. You thought that overseas exchange program was a good idea. You thought 'wrong.

Do people become clairvoyant when they are about to die? Was my father playing Russian Roulette when he clicked the trigger and had this tenth of a second when he thought My God, this is it? Did my mother scream when she was having me? Right before she died, did she ponder the question: Is this child worth it? If she did, what was her answer?

Francesca insists on serving tea to tell this story. I don’t drink tea. Today, I drink tea.

"Do you want to ask questions or shall this old woman spin a yarn?" she said.

Speechless, I reply: "Spin away."

For the next 45 minutes, fill-in-the blank sentences become stories. Stories become narratives. Narratives become novels in my mind as I cognitively add and embellish what it must have been like. Phil, I mean Dad's, story still had the mystery. He was no good, never was. Drug rings, strip clubs and dirt bikes. That was his life. One night Melissa came to his place to find him sitting in his Laz- E- Boy chair, bleeding out both of sides of his head. Could have been a drug debt. A gambling debt. A jealous girlfriend - he had several of those, reported Francesca. In my mind, I thought. OK, father's a bum. Any hope for mom?

Mom was something different. Granted, grandmothers always think so, but Francesca would pin the medal of honor on her even now. Very creative. An artist. State champion swimmer. None of that rubbed off on me, I thought. Phil had been her haphazard attempt at rebellion.

"Everyone dates a loser," Francesca argued, "and Philip was her rotten apple."

After Philip was found dead, little Melissa was left with a gaping hole in her life. No one close to her had died before. No one. That hole was filled by pregnancy. I became her lifeline. Not to Phil - but to a better world that was once within her grasp. The doctor had warned her it was high risk. Melissa said she would rather die than give me up. Prophetic. A fourth dimension.

Francesca said she pleaded with Melissa to reconsider. "If she didn't, she would die. We all knew that," Francesca murmured. "Biggest mistake she ever made was - no offense."

"None taken." I said it with a remarkably honest tone. I meant it.

"She made her choice, I suppose."

I couldn't speak. I asked if I could come back and hear the rest tomorrow. Francesca complied.

All my life I looked for the story behind the story. Melissa McClish, 20, died in childbirth. There had to be more. Never once did I stop to consider it a choice that could be made. It was merely a tragedy that could not be avoided. Now I knew better.

She made her choice. My mother made a heroic, honorable choice. A choice I must now live up to. What was I doing in California? I had a life to live that had been bartered for. An odd, renewed energy tingled my spine.

Melissa McClish, 20, died giving life. What would my story be? Would it have a fourth dimension?

We all have a fourth dimension. Sometimes it's evident. Other times, you have to take a road trip to decipher it. Three things are remembered. Four things matter.
```

---

## IC-0004: Act of Devotion

- Title: Act of Devotion
- Author (byline): Deborah Tannen
- Work: The Best American Short Plays 1993-1994
- Publisher: Applause Books
- Publication date as stated: May 2000
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: FATHER, DAUGHTER
- Teaser before the introduction: Yes
- Spoken words (computed): 2795
- Already set (do not supply): none

### Source block (context only)

```text
Author: Deborah Tannen
Book: The Best American Short Plays 1993-1994
ISBN: 978-1557831996
Publisher: Applause Books
Date (Month/Year): May 2000
```

### Introduction (context only: never use it for content warnings)

```text
When speaking about the Holocaust, author Jane Yolen once said “Fiction cannot recite the numbing numbers, but it can be that witness, that memory. A storyteller can attempt to tell the human tale, can make a galaxy out of the chaos, can point to the fact that some people survived even as most people died. And can remind us that the swallows still sing around the smokestacks.” How the Holocaust impacted the future generations of Jewish families is a topic not often addressed, but in Act of Devotion by Deborah Tannen, we find a daughter traveling back to Warsaw with her Jewish family – a family that survived and love of a father figure shines through the tears. Act of Devotion by Deborah Tannen.
```

### Performance text (classify this)

```text
FATHER: a man of eighty-five

DAUGHTER: a woman in her late forties

A hotel room in Warsaw in August, late afternoon. FATHER speaks in the voice of his memory, a younger version of himself. The tone of both DAUGHTER's and FATHER's dialogue is understatement and subtle irony, not stereotypically or exaggeratedly Jewish cadences}.

DAUGHTER: The first thing we did after checking into our hotel in Warsaw was to take a taxi to where my father had lived as a child. The street was still there, with its street sign, Twarda [Pronounced "tuarda"], but in place of the apartment house he had lived in was a grim gray building with a cement wall covered with obscene spray-painted graffiti - I was overwhelmed with the thought that I was standing on the street I had heard my father talk about all my life.

FATHER: We stood under the sign, Twarda Ulica [pronounced "tuarda ooleetsa"]. How dull and quiet it was, how faceless and bland the buildings that had been put up since the war. When I was a child, the neighborhood was always in commotion and crowded with life. Both sides of the street were lined with stores, and the sidewalks were teeming with people - Hasidim with their long beards, black boots, and the ritual fringes of their prayer shawls peeking out from under their vests. Working men, women shopping, men going to and from the synagogue. There were "tragers" - carriers - men hired by people too poor to hire a wagon, carrying amazing loads on their backs - a desk, a bed. Epileptics would fall down and have convulsions in the street. No one stopped to watch, because it was common. And beggars, everywhere beggars in torn clothes. Some wore garments sewn from sacks, some had rags on their feet instead of shoes. Many of the beggars were cripples. When I came to America, I always wondered: where were the cripples?

DAUGHTER: On the second day, we went to the National History museum where we'd heard there was a film about the destruction of Warsaw during World War II. The narrator told how the inhabitants of the city were deported to another part of the country as the Germans systematically demolished their city. When the war ended, the city's inhabitants returned. There was inspiring documentary footage of the Poles handing stones from man to man as they rebuilt Warsaw - but nothing about the killing of thirty percent of the population of the city - the entire Jewish population. There were a few fleeting shots of Jews being deported, as the narrator's voice said, "The Jews were the first to go." He neglected to mention that they didn't come back.

FATHER: In the street were droshkis [pronounced "DROSHkeez'j - horsedrawn carriages that took passengers, and open wagons for trade. The drivers were beating and yelling at their horses, and yelling at pedestrians to get out of the way. Occasionally a "kareta" drove by - a fancy carriage that rich people rode in. One day an old Hasid stepped off the curb just as an automobile came rushing into the space between the streetcar and the curb, and its wheel ran over the old man's foot. As the man shrieked in pain, the driver stopped his car, got out, rushed over to the old man, and began loudly berating him for getting in his way. Soon after I arrived in America, I saw a cab driver and his passenger standing by the cab, arguing with each other. I couldn't get over the contrast. In Poland, if you were rich enough to drive an automobile, you had the right to yell at anyone. In America, a cab driver, in his worker's cap, was shouting at a rich man in a silk top hat.

DAUGHTER: We went to the Jewish cemetery where my father's grandmother was buried. He told us about attending her funeral when he was eleven, shortly before he left for America. He said his grandmother's funeral was so vivid in his mind, he felt as if he could walk right to her grave, but he couldn't walk to it, because the cemetery he'd visited as a child had been destroyed during the war. Headstones had been smashed by vandals or uprooted by trees that sprouted up; paths had been obliterated by undergrowth.

FATHER: Our apartment building was built around a cobblestone courtyard. You entered through a huge archway with wooden doors that were locked at night. There were storefronts facing the courtyard, at ground level. During the day vendors came in, shouting about what they had to sell. Beggars came in and went from door to door, asking for a kopek or a piece of bread, which they'd put into a sack.

DAUGHTER: We went to the memorial to the Warsaw ghetto uprising. There's a long approach to the monument, leading up to a dynamic statue hurtling out of a stone wall: muscular young men brandishing arms, who chose to die fighting rather than follow orders for deportation. On another day, a Polish woman, took us back to see the other side of the monument: a frieze of a throng of people streaming to their deaths - a rabbi carrying a torah, families with children dwarfed by the legs around them. This, she told us, was the truer representation. There were sixty thousand people left in the ghetto at the time of the uprising. Three hundred thousand of the ghetto's inhabitants had been killed in Treblinka in the months before. We had missed this part of the monument on our first visit. We hadn't thought to walk around and look at the back.

FATHER: Vendors came into the courtyard, shouting about what they had to sell. One man had a grinding wheel; people brought him knives and scissors to sharpen. Another man would push a wheelbarrow into the courtyard and set up shop. He took iron pots blackened from cooking and returned them sparkling and shiny.

DAUGHTER: At the ghetto monument, my father got into a conversation with a young Danish woman holding a guidebook. As he walked away, I told her that he had grown up in Warsaw, that his grandfather had died in the ghetto, and that other family members and people he'd grown up with had died there, or lived there and died in the camps. I brandished this information as a badge of honor, as if it gave me a greater right to be visiting the memorial.

FATHER: Our third-floor apartment was my grandfather's home. I was born there, and so was my mother. I lived there until I was seven. My mother was one of the oldest of sixteen brothers and sisters. The youngest was only six years older than I, so I was like the youngest brother, and my grandfather was the closest I ever came to having a father. For years I thought my grandfather's name was "zahzogit" because that's what my grandmother called him: "Zahzogit, would you pull out that chair?", "Zahzogit, may I have money to shop for food?" Then I found out that "zahzogit" meant "be so good." When she spoke to him, she began that way to be properly deferential to her husband. His children feared him, because he was stern and author-itarian with them, but he was always kind and gentle to me.

DAUGHTER: When I was seven or eight, I wrote my first story. It was about my father when he was a child. The story took place in the stairwell outside his apartment in Warsaw. It was a story he'd told me: when he was very little, his mother dressed him in his older sister's outgrown dresses, rather than spend money buying boy's clothes for him. He was too ashamed to go out and play dressed as a girl, so he sat in the stairwell all day and cried.

FATHER: My mother was married at eighteen to a man she'd never met, and she never liked him. She threw him out when I was two. She never told me directly that I was ugly, but whenever she spoke of my father, she's say how she hated his looks, especially his long hooked nose. And whenever she spoke about me, she'd say I looked exactly like him. When I did something she didn't like, which was just about anything I ever did, she'd say, "Just like your father.” It wasn't until I was an adult and talked to people who knew him that I found out my father had been a wonderful man. They said he was kind, gentle, intelligent, and generous. Everyone loved him, except my mother.

DAUGHTER: My father talked so much about his childhood that I felt it as if it had happened to me. But it hadn't happened to me. I believed that nothing that happened to me could be as significant as what he had suffered. What right did I have to be miserable. In my memory, my childhood is an endless train of days spent with my mother, missing my father. He left the house before I woke up in the morning, and he often worked late, so he came home after I had gone to sleep. My favorite object in the house was an old black typewriter with yellow keys rimmed in silver. I'd spend hours typing letters to my father, telling him what had happened to me during the day and laying out my grievances against my mother. I couldn't have any grievances against him, because he wasn't there.

FATHER: My father had tuberculosis. My mother told people that was why she threw him out - so he wouldn't infect my sister and me. And she said she never remarried because she didn't want her children to grow up with a stepfather. Maybe it was true. But I always believed she preferred to live on her own. She wasn't the kind of woman who wanted to spend her life waiting on a man.

DAUGHTER: Sometimes when he was home at our bedtime, my father told us stories that he made up himself -long elaborate tales of dragons and eagles in which we were the heroes. As we lay in our beds, he'd move around the room, acting out all the parts, suddenly rushing right up to our delighted, mock-scared, laughing faces. And then, when it was time to sleep, he'd lie down with us, and we'd snuggle up to him with our heads on his shoulder. That way I could always fall asleep . . . When I was a teenager, I prided myself on my irreverence. I liked to shock people by saying, "If my father had stayed in Poland, he'd be a lamp shade."

FATHER: When I was six, my father died. He was twenty-seven years old. Since I didn't know him, I wasn't sad; I thought it was an interesting piece of news. When I ran into a neighbor on the staircase, I boasted excitedly that I knew something she didn't. "What is it?" she asked. "That your father died?" Though I never knew my father, I certainly knew my grandfather. There was no question in my mind that he was the most powerful, most dignified man in the world, and I was sure everyone else knew this too. But one day, after World War I finally ended, he took me with him on an expedition to the home of someone who owed him money. I was shocked to see the manner he assumed in this house, as he doffed his cap in deference. I couldn't believe my eyes: my grandfather, taking his hat off to someone!

DAUGHTER: Years ago I had a dream. I'm having a birthday party. My father is there, but he's suspended about two feet off the ground, with his head near the ceiling. I don't know what he's doing up there; he doesn't seem to be doing anything, just floating in his own world. I can't reach him, and he doesn't hear me or see me. I desperately try to make contact with him, but he's stuck up there and I can't get him to come down.

FATHER: When we were about to leave for America, my grandfather called me to him and took me on his lap. Tears streamed from beneath his gold-rimmed glasses, down his cheeks, and into his beard. He knew he would never see me again. With his arm around my shoulders, he said, "Never forget that you are a Jew."

DAUGHTER: I'd always known that my father's grandfather died in the Warsaw ghetto, but somehow I'd assumed he died of old age, and the ghetto happened to be where he lived when his time came. In my mind, "the ghetto" was just a dilapidated section of town where Jews were forced to live. But one day, I realized how much I didn't know - that Jews had been crammed into the ghetto from all over the city and the country; that 1 00,000 people died there from starvation, and from epidemics that broke out, caused by the overcrowding and unsanitary conditions. Naked corpses lay in the streets - corpses in the street because people had to pay a fee to bury their dead and they had no money; naked because every shred of cloth had to be salvaged and used. Women nursed infants in the street, but they had no breasts, no nourishment to give their dying babies. German soldiers strolled through the ghetto on their way to somewhere else and shot people for fun. I thought I knew about the Warsaw ghetto, but I really didn't know anything about it at all.

FATHER: Those were my grandfather's last words to me: "Never forget you are a Jew." He believed that when Jews went to America, they ceased to be Jews, because they stopped being Hasidic. Have I betrayed him? What do my daughters know of their Jewish heritage? What can being Jewish mean to them, having grown up in America? Only one of them married a Jew - and she doesn't have children, so what difference does it make?

DAUGHTER: We went to the Unschlagplatz, where each day thousands ofJews gathered to be shipped to Treblinka, where they'd be gassed. Today it's a green park with a monument, a series of stone walls. One wall is a glittering white stone slab with Jewish names, meant to represent the three hundred thousand people who had been sent to be killed from this square. Mordechai, Moishe, Shmuel, Abraham, Rachel, Rebecca, Naomi, Leah, Sarah, Miriam, Deborah. Another stone slab bore the words of a poem. We all lined up facing this wall, and asked my father to translate the Polish text etched into the stone. [As she speaks these lines, DAUGHTER walks over to FATHER and stands beside him on his left, as they both enact the scene she describes.] He began to read the words, but his voice faltered, and he stopped. I turned to see that his body was shaking. He put his right hand up to his left cheek, palm out, making a barrier between our eyes, so I couldn't see his face as he sobbed. I put my arm around him. He gathered himself up and started to read again. But again, he stopped. Again, he held his hand to the side of his face, like a shield against my gaze. On the third try he read:

FATHER: "Earth, do not cover my blood; wind, do not silence my screams ... "

DAUGHTER: As we walked away, my mother whispered to me that in the sixty years of their marriage, she had never seen him break down before. Days later, he told us what overcame him was a picture in his mind of his grandfather and his uncle Joshua, the only son who had stayed behind with the old man, and Joshua's wife and five children. They had all almost certainly been shipped to their deaths from the spot on which we stood. And he kept thinking, "What had they done to deserve their fate? They had never done anything to hurt anyone."

FATHER: I stood under the street sign, Twarda Ulica. Inside my head, it was all still there: the busy courtyards, the people calling out of the windows, the streetcars clanging, the drivers yelling, my grandfather going to shul, But outside, there was nothing. No trace of the world I grew up in. In place of the three-story apartment house with its courtyard was a gray utilitarian building covered with obscene graffiti. After I'm gone, who will remember? If no one remembers, what will remain?

DAUGHTER: My father wanted to take pictures of the Jewish cemetery, but he hates to waste pictures with no one in them, but I hung back. I couldn't figure out if it was a desecration to pose for pictures, like tourists, in a place like that, or if it was an act of devotion, to try to remember.
```

---

## IC-0005: Adult Child/Dead Child

- Title: Adult Child/Dead Child
- Author (byline): Claire Dowie
- Work: Why is John Lennon Wearing a Skirt and Other Stand-Up Theatre Plays, Pgs 3-31
- Publisher: A&C Black
- Publication date as stated: Oct 1996
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SPEAKER
- Teaser before the introduction: Yes
- Spoken words (computed): 1672
- Already set (do not supply): none

### Source block (context only)

```text
Author: Claire Dowie
Book: Why is John Lennon Wearing a Skirt and Other Stand-Up Theatre Plays, Pgs 3-31
ISBN: 978-0413710901
Publisher: A&C Black
Date (Month/Year): Oct 1996
```

### Introduction (context only: never use it for content warnings)

```text
Mental illness often begins invisibly, shaped by neglect, fear, and silence. In this selection, the name for that mental illness is “Benji,” an imaginary friend who becomes both refuge and threat, carrying the anger a child cannot express. As violence erupts, the consequences are devastating -- but not final.

Adult Child/Dead Child by Claire Dowie
```

### Performance text (classify this)

```text
SPEAKER: (Pgs 3-31) (with growing agitation) Clean house, spotless, nothing out of place except me. Can't seem to please them, can't win for losing. My mother despaired of me. My sister was an angel -- never put a foot wrong; a perfect child, a joy to behold. My father was an actor: pretended to be a father, pretended to have feelings, demanded perfection. 100% do it right, do it the best. Be brainy, be sporty; be talented, be good; well-mannered, polite. Know it all, do it all. 100%. (beat) I failed always failed.

SPEAKER: I remember being in the garden. I was about six or seven and there were friends of my parents visiting. I can't remember now who, but somebody gave me a cowboy and Indian set -- a cowboy hat and gun and holster and a tin star with the word 'sheriff' on it and an Indian feather thing with a band on it and a tomahawk. And my dad said let's play with it and first he was the cowboy and I was the Indian and everybody was watching and I ran at him with my tomahawk but he shot me so I lost. And then we changed round and I was the cowboy and my dad was the Indian but before I could shoot him, he threw the tomahawk and it hit my head and everybody laughed. (beat) I didn't want to play with my cowboy and Indian set anymore.

I was a clumsy child, clumsy! Never a day would go by that I wasn't walking into things, tripping up, knocking things over. It drove my parents crazy. Fidgeting was another habit I couldn't seem to shake, which annoyed my parents intensely. Once my dad got so mad about it he tied me down to a chair. My parents were great believers in eye for eye and tooth for tooth punishments.

(realizes how it sounds and is quick to clarify) I was never what you'd call an abused child. Not abused. But there was the cupboard under the stairs: dark, silent, claustrophobic nothing to do, nothing to say, nothing to be but lifeless, invisible. Sitting in the cupboard till I 'learn to behave myself and show some respect.' Everything I got I deserved except the cupboard under the stairs. I never locked anyone in a cupboard but my parents did. (struggles to explain the feelings)

When you are a child the adults have the power and they know everything -- to know what you are feeling, so you want to hit out because of this lack of love that you can't explain. They won't help you with your feelings -- this hurt and frustration because you can't explain so you stop trusting the adults. (beat)

My invisible friend came I think when I was 4 or 5 but by the age of 7 she was with me always -- chattering a way, making jokes telling stories. I didn't give my invisible friend a name till I was 8. . . I called her Benji. She sat next to me at the dinner table (and she didn't like cabbage either). By the time I was eight, [my parents] were telling me I was too old for imaginary friends. Stupid. Benji was still there, I could hear her, I could feel her. We did things together.

So what if my sister lost her charm bracelet! It was a horrible charm bracelet -- it rattled! (to Mom) I don't know maybe she just dropped it somewhere maybe it just fell off. I don't know! (to audience) We got away with it for a long time, mostly because Benji was a good liar and would tell me what to say if anyone asked: Benji did it. (as Mom) Oh, don't be so stupid. (to Mom) She did. It was Benji. (as Mom) Look, it was you, now just stop it, you're too old for all that rubbish.

(to audience) Then she's going on and on about money missing from her purse. My dad joins in; my sister sits there all innocent and perfect. It’s getting on my nerves all their questions, accusations, fingers pointing in my face. (to Mom) Benji did it. (to audience) Benji's getting annoyed. Benji's getting angry, I can feel her.

You build a wall of anger and mistrust and hatred. Further and further away, no understanding, no communication. Me and Benji in our own little world and all the rest in theirs. The only time our worlds collided was when Benji did something wrong and I got the blame for it.

Benji would swear. But it wasn't, wasn't just swearing, she had tantrums and threw things all over the room -- threw furniture! She thought it was funny. I didn't. I never wanted to get into trouble, [but] it was just trouble all the time. I couldn't control her. I couldn't stop her. She scared me. (beat)

Mr Kent, he was a woodwork teacher. By now I was 13 and hated by everybody including Mr Kent. Benji was in control of everything now, and I hated her. (beat) I was making a toast rack in woodwork. Mr Kent said it was crap -- said I was a worthless human being. [He] went on and on and on till Benji jumped out and threw a hammer at him. I was suspended from school for two weeks because Mr Kent couldn't take a joke, well all right, it wasn't funny, no, it was very dangerous, but it had missed and he had asked for it.

All night I am awake, or sort of awake, or something, I'm not sure. I don't know what's happening with me. Benji doesn't stop talking, telling me that my dad's going to kill me when he finds out. Benji keeps telling me over and over . . . (whispers in Benji’s voice) remember when you kicked your sister how he kicked you? Remember when you threw stones at those boys how he threw stones at you? An eye for an eye, tooth for tooth! (to audience, distraught) and I never did those things, I never did! Benji did them, it was Benji! (beat, near tears) I don't know what's happening. I don't! (whispers in Benji’s voice) And the cupboard after, the cupboard, cupboard . . . he's going to kill you. (argues with the voice) I didn't do anything, it was you, you threw it! (in Benji’s voice, more assertive) But they won't believe you will they, they never do, they never did (as speaker, whimpering) You threw the hammer . . .

(in Benji’s voice, loud and strong) He's going to kill you when he finds out, he's going to kill you! Eye for eye, and tooth for tooth! He's going to kill you unless you kill him first. Do it first, to save yourself, to defend yourself. (long silence)

(to audience) It was a long night, and I can't understand any more. I don't know what's happening to me and Benji won't shut up. I don't know! (stands quietly with a hammer drawn back) And then it's dawn and I'm in their bedroom with the hammer and I don't understand. . . . (brings the hammer down, shocked)

And then I hit him with it. I hit him! Somebody had to make a move, stop the tension, do something! So I did. I did something: (almost chanting as he hits himself in the head with the hammer) Clear the air. Make amends. Even the score. Eye for eye. Tooth for tooth. (stops, long beat, then in amazement) I hit myself with the hammer. I was 13.

They sent me to a psychiatrist. (in Benji’s voice) Lunatic. Mad. Insane.(to audience) I didn't know anything about psychiatrists or mental health except what I'd watched on television. (in Benji’s voice) Deranged. Psychopath. Crazy. First you tried to hammer the woodwork teacher, then you hammered your father, then you hammered yourself.

(beat, to audience) Mental hospitals aren't that bad quite nice really. I was there for 6 weeks and they gave me some drugs to calm me down and Benji faded a bit and I got a grip of myself and felt a lot better. (beat) We all went to family therapy, and my parents and my sister talked and I said nothing. When the therapist asked me anything, I said I dunno. And the weeks passed and I didn't get into trouble anymore and I never went into the cupboard again and the eye for eye retributions stopped.

It made me think a lot. I had always been a disappointment to my parents, a waste of effort, now I was a waste of space. , . When I was 17 I thought the best thing to do was get out, get away, leave home.

(thoughtful) Frustration comes because you are an adult. You are no longer a child but you feel like a child because you need love like a child. You are an adult, but the child needs love . . . and the anger grows. You can't ask for love like a child because you are adult. (shakes if off and continues the story)

I was ready and they got me a flat and all my friends came and helped me decorate and arrange the furniture. I felt good, much too old for imaginary friends. But I was lonely. I couldn't bear the emptiness and silence. I'd never been on my own before -- always had Benji. Then I thought, I'm just being silly. I'm sure everybody feels like this when they move into a new place. I've just got to get used to it, just got to keep busy, not think about it. I was too old for imaginary friends but I couldn't cope on my own. And it was just at that point, just at that point when I thought “I can't do it -- have to go back to hospital or something” -- it was just at that point that I had this brilliant idea: (suspenseful beat, then happily) I got a dog! And she's a real dog, she's not imaginary. And we do everything together, always together, just like Benji. (beat, a confession)

I do sometimes have this urge though, to stop taking the medication, just for a while. I'd like Benji to come back just one more time. I feel I need to say sorry, cus I know now that it wasn't Benji really. I know that it was me really, my anger, my emotion that caused all that trouble. [Benji] was my best friend, she was, she was my best friend and I blamed her all those years, so I would just like to say sorry. And I'd like to say goodbye. (shakes it off)

But I can't even think about it. (with conviction) I'm too old for imaginary friends. I should just think about my dog, cus she makes me happy, she does! She's a great dog, a real scallywag, always into everything. I call her . . . Lady (shrugs) It's just a name.
```

---

## IC-0006: After I Was Thrown in the River and Before I Drowned

- Title: After I Was Thrown in the River and Before I Drowned
- Author (byline): Dave Eggers
- Work: Speaking with the Angel
- Publisher: Riverhead Books
- Publication date as stated: Feb 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: UN-NAMED PIT BULL, PIT BULL, SQUIRREL 1, SQUIRREL 2
- Teaser before the introduction: Yes
- Spoken words (computed): 2014
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Eggers
Book: Speaking with the Angel
ISBN: 978-1573228589
Publisher: Riverhead Books
Date (Month/Year): Feb 2001
```

### Introduction (context only: never use it for content warnings)

```text
Pit Bulls are probably the most abused dogs on the planet. The breed suffers horribly at the hand of humans. In the face of potential and outright banning of this breed, the dogs--very real victims--are often completely overlooked.

Case #5125 . . . Severely dehydrated, starved and beaten with a metal pipe. This pit bull was barely clinging to life after losing a fight and being bagged and thrown in the river to die by its former owner. But fate intervened and this pup was found in the nick of time. This is where our story begins

After I was Thrown in the River and Before I Drowned by Dave Eggers.
```

### Performance text (classify this)

```text
UN-NAMED PIT BULL: OH I'M A FAST DOG. I'm fast- fast. It's true and I love being fast I admit It I love it. You know fast dogs. Dogs that just run by and you say, That's a fast dog! Well that's me. A fast dog. I'm a fast- fast dog. Hoooooooo! Hooooooooooooo!

PIT BULL: I love it I love it. I run to feel the cool air cool through my fur. I run to feel the cold water come from my eyes. I run to feel my jaw slacken and my tongue come loose and flap from the side of my mouth and I go and go and go my name is Steven.

I was once in a river. I was thrown in a river when I was small. You just cannot know. I was swimming, trying to know why I had been thrown in the river. I was six months old, and my eyes were burning, the water was bad. I paddled and it was like begging. The land on either side was a black stripe, indifferent. I saw the gray water and then the darker water below and then my legs wouldn't work, were stuck in some kind of seaweed or spider web and then I was in the air. I opened my burning eyes and saw him in yellow. The fisherman. I was lifted from the water, the water was below me. Then shivering on their white plastic boat bottom and they looked at me with their mustaches. I dried in the sun. They brought me to the place with the cages and I yelled for days. Others were yelling too.

Everyone was crazy. Then people and a car and I was new at home. Ate and slept and it was dry, walls of wood. Two people and two girls, thin twins who sleep in the next room, with a dollhouse between them.

Every night I walk from the neighborhood and head to the woods and meet the others. It's shadowy out, the clouds low. I see the blues jumping inside the windows. I want all these people gone from the buildings and moved to the desert so we can fill the buildings with water. It's an idea I have. The buildings would be good if filled with water, or under water.

These people. The only ones I like are the kids. I come to the kids and lick the kids. I run to them and push my nose into their stomachs. I run around them and around again as they run forward. They're slow but they are perfect things, almost perfect.

I just cannot tell you how much I love all this, these woods, the dirt, and the smell of dogs nearby waiting to run. Tonight is cool, almost cold. There are no stars or clouds. We're all-impotent but there is running. I jog down the trail and see the others. Six of them tonight-Edward, Franklin, Susan, Mary, Robert, and Victoria.

Tonight I race Edward. Edward is a bull terrier and he is fast and strong but his eyes want to win too much; he scares us. The course is a simple one. We run from the entrance through the black-dark interior and out to the meadow and across the meadow and into the next woods, along the creek, then over the gap over the drainpipe and then along the creek until the highway. The jump over the drainpipe is the hard part. On the banks of the creek, near the drainpipe, on the dirt and in the weeds and on the branches of the rough gray trees are the squirrels. The squirrels have things to say; they talk before and after we jump. Sometimes while we're jumping they talk.

SQUIRREL 1: He is running funny.

SQUIRREL 2: She will not make it across.

PIT BULL: When we do not make it across the gap, and instead fall into the sandy bank, the squirrels say other things, their eyes full of glee.

SQUIRREL 1: It makes me laugh that she did not make it across the gap.

SQUIRREL 2: I am very happy that he fell and seems to be in pain.

PIT BULL: Sometimes one of the dogs, annoyed past tolerance, catches a squirrel in his mouth and crushes him. But then the next night they are back, all the squirrels, more of them. Always more.

Edward is nudging me as I run. He bites me and bumps me and yells things at me. When we come to the bend he tries to bump me into the tree. I skid and then find my footing and keep running. I catch up to him quickly and because I am faster I gain all the speed and then I see the gap. Two more strides and I jump.

I clear the gap by two feet and turn to see Edward jumping, and Edward's face looking across the gap, looking at my side of the gap, and his eyes still on the grass, exploding for it, and then he is falling, and only his front paws, claws, land above the bank. He yells something as he grabs, his eyes trying to pull the rest of him up, but he slides down the bank. He is fine but in the past others have been hurt. One dog, Wolfgang, died here, years ago. The other dogs and I jump down to help Edward up. The squirrels say things.

SQUIRREL 1: That was a terrible jump.

SQUIRREL 2: Bad landing. . . . Awful landing.

PIT BULL: I run the rest of the race alone. After we all run we go home. The next night I walk alone to the woods, my claws clicking on the sandpaper cement.

Tonight I race Susan. Susan is a retriever, a small one, fast and pretty with black eyes. We take off, through the entrance through the black-dark interior and out to the meadow. Then the straightaway before the gap. Now we have to think about our own legs and muscles and timing before the jump. Susan looks at me and smiles but looks tired. Two more strides and I jump and then the hard ground rushes toward me and I land and hear her scream. I turn to see her face failing down the gap and run back to the gap. Robert and Victoria are down with her already. Her leg is broken and bleeding from the joint. She screams then wails, knowing everything already. The squirrels are above and talking.

SQUIRREL 1: Well, looks like she got what she deserved.

SQUIRREL 2: That's what you get when you jump.

PIT BULL: Some of them laugh. Franklin is angry. He walks slowly to where they're sitting; they do not move. He grabs one in his jaws and crushes all its bones. Their voices are always talking but we forget they are so small, their head and bones so tiny. The rest run away. He tosses the squirrel's broken form into the slow water.

We go home. I jog to the buildings with Susan on my back. . I take her home and scratch at her door until she is let in. I go home and see the thin twins with their dollhouse and I go to the room with the bed and fall asleep before they come.

The next night I don't want to go to the woods. I can't see someone fall, and can't hear the squirrels, and don't want Franklin to crush them in his jaws. I stay at home and I play with the twins in their pajamas. They put me on a pillowcase and pull me through the halls. I like the speed and they giggle. I stay with them tonight and then stay home for days.

When I come to the woods again, after ten days away, Susan has lost her leg. Susan has three legs, a bandage around her front shoulder. Her smile is a new and more fragile thing. It's colder out and the wind is mean and searching. Mary says that the rain has made the creek swell and the current too fast. The gap over the drainpipe is wider now so we decide that we will not jump.

I race Franklin. Franklin is still angry about Susan's leg; neither of us can believe that things like that happen, that she has lost a leg and now when she smiles she looks like she's asking to die. When we get to the straightaway I feel so strong that I know I will go. I'm not sure I can make it but I know I can go far, farther than I've jumped before. I want this so much, the floating.

I run and see the squirrels and their mouths are already forming the words they will say if I don't make it across. On the straightaway Franklin stops and yells to me that I should stop but it's just a few more strides and I've never felt so strong so I jump yes jump.

When I hit my head it was obvious. I hit my head and had a moment when I could still see - I saw Susan's face, her eyes open huge, and then the current took me out and then I fell under the surface. After I fell and was out of view the squirrels spoke.

SQUIRREL 1: He was a fool.

SQUIRREL 2: Everything he ever did was worthless.

PIT BULL: Franklin was angry and took five or six of them in his mouth, crushing them, tossing them one after the other. After I died, so many things happened that I did not expect. The first was that I was there, inside my body, for a long time. I was at the bottom of the river, stuck in a thicket of sticks and logs, for six days. I was dead, but was still there, and I could see out of my eyes. I could move around inside my body like it was a warm loose bag.

I had been thrown into the river, a different river, when I was young by a man because I would not fight. I was supposed to fight and he kicked me and slapped my head and tried to make me mean. I didn't know why he was kicking me, slapping. I wanted him to be happy. I wanted the squirrels to jump and be happy as we dogs were. But they were different than we were, and the man who threw me to the river was also different. I thought we were all the same but as I was inside my dead body and looking into the murky river bottom I knew that some are wanting to run and some are afraid to run and maybe they are broken and are angry for it.

After the sixth day I woke up and it was bright. I knew I was back. I stood and was in a wide field of buttercups. I could smell their smell and walked through them, my eyes at the level of the yellow, a wide blur of a line of yellow.

I should say that it's very much the same here as there. There are more hills, and more waterfalls, and things are cleaner. I like it. Each day I walk for a long time, and I don't have to walk back. I can walk and walk, and when I am tired I can sleep. When I wake up, I can keep walking and I never miss where I started and have no home.

I haven't seen anyone yet. I don't miss the cement like sandpaper on my feet, or the buildings with the sleeping men reaching. I sometimes miss the other dogs and the running.

The one big surprise is that as it turns out. God is the sun. It makes sense, if you think about it. Why we didn’t see it sooner I cannot say. Every day the sun was right there burning, our and other planets hovering around it, always apologizing, and we didn't think it was God. Why would there be a God and also a sun? Of course God is the sun. Everyone in the life before was cranky, I think, because they just wanted to know.
```

---

## IC-0007: After the Death of Anna Gonzales

- Title: After the Death of Anna Gonzales
- Author (byline): Terri Fields
- Work: Not specified
- Publisher: Henry Holt and Co
- Publication date as stated: Nov 2002
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1032
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
Anna Gonzales

(Pg 99-100) "I will slip away,

Making little fuss.

And being less remembered,

which is pretty much the way I have always been.

Never pretty or popular enough to matter.

Never outrageous or outstanding enough

to get attention.

Sometimes, I have to pinch myself to make certain

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

So I say good-night to this world

Feeling since it has never embraced me

It will not mind if I have abandoned it."

Principal Barron

(Pg 6 -7) Thirty years in education.
I’ve broken up fights.
Fired a teacher.
Failed a student.
But not this.
This is too much to ask.

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

“I am sorry to tell you of the death of one of our students.”

Must continue. Rumors always worse than truth.

“Anna Gonzales took her life last night.

Our sympathies to her family and friends.

Grief counselors will be available all day.”

TRANSITION

And so, life goes on, but how does it go on? How does one life really affect another? If I am here today and not tomorrow, would that make an impact on your life in any way? Anna Gonzales is dead. She committed suicide. If you could take a notebook and somehow chronicle what went through the minds of students and faculty immediately after that announcement

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

Feel forgotten.

But damn it, Anna,

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

According to the Center for Disease Control, suicide is responsible for almost 4,400 deaths of young people each year. The same study speculates that students aged 10 to 14 are more likely to commit suicide than other age group. Even more concerning is that the suicide of a peer is often a traumatic experience for adolescents (many of whom are left bewildered by the lack of warning signs), often influencing other teens who are already feeling suicidal. The following two poems are by students who have already felt the closeness of death – Anna’s suicide had a dramatic impact on these vulnerable teens as well.

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
even if I married at forty. Who predicted no one would be a
better Grandpa.
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

That empty seat in the third row. Anna will be back. She must
be. Quiet, sweet'
A face framed by long lush brown hair. Almond eyes always seemed
luminous. Giving no hint that this unnatural sleep would be her
fate.

I've tried to teach through literature

The wonder of life.

Yet the quiet rebuke of that empty chair

Speaks louder than the most vocal of student skeptics.

I cannot take my eyes from the spot.

"There in the sudden blackness, the black pall

Of nothing, nothing, nothing--nothing at all."
```

---

## IC-0008: Almost Normal

- Title: Almost Normal
- Author (byline): Jason Sheets
- Work: Turning Points, Pgs 159-161
- Publisher: Tichenor Publishing
- Publication date as stated: Jan 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MRS. SIMPKINS, RULE #1, RULE #2, RULE #3, RULE #4
- Teaser before the introduction: Yes
- Spoken words (computed): 956
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jason Sheets
Book: Turning Points, Pgs 159-161
Publisher: Tichenor Publishing
ISBN: 978-0742117013
Date: Jan 2001
```

### Introduction (context only: never use it for content warnings)

```text
Wow. That was really hard to say, and even harder to do. Why? Because it felt wrong. It felt hateful. No one ever uses diabetes or cancer to denigrate another person. You see, having a medical condition does not make someone lesser or sub-human, and having a cognitive condition shouldn’t be any different.

But it wasn’t always so . . . The R-word was once a slang term that could be heard everywhere: on playgrounds, in hallways and locker rooms; in televisions shows, movies and all-over social media.

In fact, it wasn’t until 2010 that our federal government removed the term “mental retardation” from all federal statutes and replaced it with the term “intellectual disability.”

You see, words have power. They can crush a heart or heal it. They can shame a soul or liberate it. They can shatter dreams or energize them.

In this selection, our narrator comes to the realization that his brother Todd is NOT a ‘retard’ . . . He’s Almost Normal by Jason Sheets.
```

### Performance text (classify this)

```text
NARRATOR: When I was in the fourth grade, my friends and l? We knew how to mess around! We would kick little first graders off the teeter-totters or take Becky Phipher's four-square ball. But our favorite game of all was to imitate the kids from Mrs. Johnson's special ed. class. "Act Like a Retard!" we'd call it. Really clever title. But I was good at this game. I was the master. I had the hand gestures down and everything. I could make fun of those retards better than anyone. Jimmy Stinson always said I was the best actor he'd ever met. I said no. I'd just learned it from my brother.

NARRATOR: My brother, Todd, is nine years older than me. I wasn't even born yet when Todd was diagnosed with mild to moderate mental retardation. Which basically means that somehow, some way, he managed to score a 40 on an IQ test he couldn't even read.

It was kind of difficult figuring out who the baby of the family was: me, because of my age, or Todd, because of his mentality. Either way, Todd caused our entire family to be the object of pity from people in town. I remember one teacher, Mrs. Simpkins, who would always say:

MRS. SIMPKINS: It must be rough having a simple-minded brother. Does it bother you much?

NARRATOR: No. Not until people start talking about it. That was the truth. It didn't bother me much. It just meant that there were certain rules around the house:

RULE #1: Don't say anything you don't want repeated. Like once I said, "U2 sucks." Just a general comment. So then he's walking around the house saying, “You hear that? It SUCKS! U2 sucks!” A half-hour later he asks: "What's U2?"

RULE #2: Don't let Todd request songs at church. Last time he did, he wanted everyone to "do the Vogue!"

RULE #3: Never play Uno with Todd. He'll play a red card and say "WILD! Change it to red!"

RULE #4: Never, ever, expect anyone to have any time for you because YOU are normal. YOU don't need attention.

And Todd loved to talk. It didn't matter if anyone else was in the room, he'd keep up both ends of the conversation. Once I saw him just staring at the wall, talking to himself. I said, "This guy is crazy. He really needs professional help!" Then I thought: who am I talking to?

His favorite topic of conversation was whether he was “retarded” or not. I would just tell him that we are all retarded in certain ways. See, retarded means "slow," not "stupid."

But I put up with his ramblings. 24 hours a day; 365 days a year. I wasn't even safe on my birthday. I didn't even have parties anymore. I was getting ready to blow out the candles when Todd walked up and blew them out for me. And not to be selfish, but that was my birthday moment! My wish. . . and I could have used one!

What did my parents do? They hugged him. See, Todd had never blown out a candle before. They brought out the camera and took a picture of him with the cake.

April 11, 1982: The night of my big solo at the spring concert. Mom missed it. She was out in the lobby giving Todd his 8:00 dose of Mellaril. He has to have it at exactly 8:00. So, she missed my solo. Dad saw it and said I was great. Mom took his word for it.

My brother is rather hard to describe. Let's see . . . he likes anything with cops or firemen, so his favorite TV show is "Rescue 911." His favorite movie is "Beverly Hills Cop." His favorite color is red -- fire-engine red.

Number of embarrassing moments he has caused: 447.
Number of shirts he owns: 25.
Number of shirts he wears: 6.
Number he can count to: 19.
Number of dishes he has broken: 38.
Number of times he's said "I love you": 2,714.
Number of times I've told him I love him: 4.

Trips to the mall were the worst. For some reason, Todd saw this as his chance to pick up chicks. I tried to explain to him that "Whew, shake it for my baby!" was not the coolest pick-up line.

One day, we were walking out of Walgreen's when a store clerk stopped us. She said Todd had taken something from their store without paying for it. I explained to her that he couldn't have because Todd does not steal. He may be slow, but he does not steal. She asked if she could search his pockets. I said "Fine, go ahead." Then she pulled out two packs of M&M's and a Twix bar from Todd's coat pocket. I couldn't believe it. I asked him why he did it. He said he was hungry.

I pleaded with the clerk not to call mom and dad, but she did anyway. When they heard, they decided it was time to place Todd in a group home. They said they couldn't control him anymore. But they could have. They just didn't want to.

I'll never forget the look on his face when we dropped him off at that group home forever. I said, "I love you" and he said nothing. He stared at me with those big, blue eyes, tears streaming down his cheek, looking at me like I was some sort of Judas. That was two years ago. Todd still gets to come home on the holidays, and I still visit him every Saturday. Sometimes we talk. Sometimes not. He appears a year older every time I see him. It's the same Todd, but something is missing. Something real. Something good.
```

---

## IC-0009: Aunt Leaf

- Title: Aunt Leaf
- Author (byline): Barbara Wiechmann
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: 2012
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: VOICE 1, VOICE 2, FATHER, FAMILY, AUNT LEAF, ANNABELLE, MOTHER, TEACHER, SISTER
- Teaser before the introduction: Yes
- Spoken words (computed): 1721
- Already set (do not supply): none

### Source block (context only)

```text
Author: Barbara Wiechmann
ISBN: 978-1583427798
Publisher: Dramatic Publishing
Date (Month/Year): 2012
```

### Introduction (context only: never use it for content warnings)

```text
When you have an idea, how do you share it with someone else? Wait, wait. I know the answer. You text them or email them. Because technology is everything. It’s fast, it’s efficient. But somehow, it loses something in the translation -- True human connection. That’s why we struggled so much during COVID when ALL forms of connection went digital. Even these types of competitions – we missed the connection. Jimmy Neil Smith, the Director of the International Storytelling Center explains: “There isn’t a stronger connection between people than storytelling.

• “Stories make us more alive, more human, more courageous, more loving.”

-- Madeleine L’Engle

• “That’s what storytellers do. Restore order with imagination. Instill hope again and

again.” – Walt Disney

Living things are filled with stories. When you sink your toes in the mud you're sinking in

•

stories. When you lie breathing in the dark, you're breathing stories . . .

So today, I’m going to tell you a story . . . A story about stories.

Aunt Leaf by Barbara Wiechmann
```

### Performance text (classify this)

```text
Note from the Author: (pg 7-8) Aunt Leaf is a story about storytelling. It was never my intent to have one actor play one role. In the original production, three performers “shared” the entire script, shared the story. All performers played all roles, completely unbiased as to gender, race and age. A storyteller can play anything. If you envision the play as a solo performance or a storytelling play for 20, give it a try. The only limit should truly be your imagination.

VOICE 1: (Pg 11-12) Do you know this story? Do you know the story of Aunt Leaf?

VOICE 2: The story of Aunt Leaf is also the story of a little girl. Annabelle Wood.

VOICE 1: Annabelle lived one hundred years ago in a house surrounded by trees on the banks of the Hudson River.

VOICE 2: In those days the river was just as wide and glittering as it is today, but the forests were thicker, wilder, more dangerous and more mysterious.

VOICE 1: Annabelle did not worry about this. She was 11 years old . . . she fished along the riverbank, climbed the branches of a big tulip tree and lived safe inside the house with her cheerful and talkative family.

VOICE 2: Annabelle rarely talked at all [and her] silence concerned her family.

VOICE 1: (Pg 13) One morning at breakfast Annabelle's father made an unusual announcement:

FATHER: My Great-Aunt Leaf has slipped on an acorn in that crazy house of hers in the woods. It isn't safe for her to live alone anymore! She'll have to come live with us.

VOICE 1: And so Aunt Leaf came.

VOICE 2: Annabelle's father opened the passenger-side door. . . Slowly, slowly out came a pile of blinking black rags.

VOICE 1: Aunt Leaf could have been eight trillion years old. Gnarled hands with long grey fingers stuck out of the sleeves of her stiff dress like twigs on a winter tree. She smelled like a swamp.

FAMILY: (Pg 14-15) (except for ANNABELLE, in a sudden rush and overlapping) Hello, Aunt Leaf! You must be tired. Are you hungry?

Do you like dolls? Do you know any riddles? Do you like pie?

AUNT LEAF: I want to go home! Take me home! Take me home!

VOICE 1: Annabelle's mother tried her best to make Aunt Leaf happy.

VOICE 2: She planned spontaneous family sing-a-longs

VOICE 1: Stuffed Aunt Leaf in a canoe and paddled her downstream for a picnic.

VOICE 2: Made exotic meals for Annabelle and her sisters to take up to her on decorative trays.

VOICE 1: But Aunt Leaf did not want any of it. Day by day she grew thinner. If she spoke at all it was to complain.

AUNT LEAF: The room is too hot!! The house has too many doors! My skin is just a bruise!

VOICE 1: One morning she just screamed.

VOICE 2: Only Annabelle continued to bring up the meals. Every morning silently up the stairs. And every evening down again with the untouched tray.

VOICE 1: It was the same every day. Every day. Till one night something different happened.

VOICE 1: (Pg 15-16) That night long after the rest of the family had fallen into deep sleep . . .

AUNT LEAF: (calling far off) Annabelle! ANNABELLE!

VOICE 1: Annabelle hearing her calls jumped out of bed and ran to Aunt Leaf's room. Aunt Leaf met her at the door. Her twiggy fingers pinched Annabelle's wrist.

AUNT LEAF: Go! Quick Quick! Go-outside-see if you see! See if you see! Quick! Quick!

VOICE 1: So Annabelle ran down the stairs, out the back door, and into the dark of the lawn and the woods. (she stands looking around in the dark)

AUNT LEAF: (Pg 17-19) What do you see? What do you see?! (ANNABELLE says nothing) Anything!?

ANNABELLE: Nothing.

AUNT LEAF: I heard your Great-uncle Greenleaf whistling on the lawn. Just the way he used to. Whistling to his dog. Did you hear? (ANNABELLE shakes her head) He'll come back. You'll see him next time. If you move fast enough.

ANNABELLE: Aunt Leaf, I don’t think so. I've been to the cemetery. I’ve seen his grave!

AUNT LEAF: (pause) People come back.

ANNABELLE: That's not real. That's only in stories.

AUNT LEAF: This is a story. (beat) Everything is a story.

ANNABELLE: This isn't a story.

AUNT LEAF: Yes, yes, yes, it is! Spiders, rocks, pinecones. Living things are made of stories -- filled with stories. When you sink your toes in the mud you're sinking in stories. When you lie breathing in the dark you're breathing stories . . . I heard my husband.

VOICE 1: Later that night Annabelle lay in bed thinking and rethinking.

ANNABELLE: What could it hurt to tell one little story. (beat) If it makes someone happy. . . What could it hurt to tell one tiny lie. . .

VOICE 1: (Pg 20-21) Day after day Annabelle's family talked and talked and Annabelle barely spoke at all, but now sometimes during the night she would wake up --

AUNT LEAF: Annabelle! Annabelle!

VOICE 1: -- run silently down the stairs, ghost like out the back door and began to do something she had never done before; she began to make things up:

ANNABELLE: (reporting back to AUNT LEAF, tentatively at first, but with more and more confidence) The clouds were moving very fast. (AUNT LEAF nods) I heard a dog bark across the river.

AUNT LEAF: That's a sign . . . What else?

ANNABELLE: (Pg 22-23) I found a bootprint in the mud!

AUNT LEAF: Yes! Yes!

ANNABELLE: I saw a shadow! Ripple across the grass in the moonlight- and something else. Smoke! Curls of blue smoke

AUNT LEAF: From his pipe tobacco drifting through the branches

ANNABELLE: Yes! It was him. Uncle Leaf. I saw his shadow. It was him! It was him!

AUNT LEAF: (softly) Bring me something from outside.

VOICE 1: (Pg 24-25) She pinned a swamp buttercup in Aunt Leaf's hair. Didn't Aunt Leaf look lovely? Didn't she seem young? Wasn't she happy?

AUNT LEAF: He built our house in the woods. Every morning he walked into the forest with his ax. Cut away the dead wood, made room for the new growth. Every night I waited for his footsteps. I have lit the fire for supper. I am wearing my new blue dress.

VOICE 1: (Pg 26-27) In the dark by herself Annabell began to see. The more she saw the more she wondered. The more she wondered the more she imagined. The more she imagined, the more she told.

ANNABELLE: I saw a pair of tall boots disappear into the twilight. I saw a wagging tail and the back of a dog. It was huge. . . as big as a pony. . .

VOICE 2: All that July, Aunt Leaf grew fat and hopeful on the small fibs Annabelle fed her.

AUNT LEAF: Wash my face. Hook my pearls. VOICE 1: All that August, Annabelle looked at Open the window. The air smells sweet. the way the fish jumped in the river, the I'll tell you a story . . . This is the story of way the screech owl sat on his branch in the Uncle Leaf and the summer the spiders dark. She looked for her Uncle Greenleaf’s came. . . This is the story of Uncle Leaf handsome eyes in the leaves and began to and the blizzard that covered the house . wish her own stories were true. Uncle Leaf . . Uncle Leaf and the witch of the hides himself in the shapes of animals and Athens woods. . . Uncle Leaf and the birds . . . Uncle Leaf knows the secret Bullfrog children . . .The mysterious lights language of the crows . . . Uncle Leaf knows . . . The water snake . . . the black ice . . . every story ever told the fire ball . . . the wolves. . .

VOICE 1: (Pg 29) Voices from the daytime world called to her as if through the thickness of dream . . .

MOTHER: Annabelle! You look pale. Are you all right?

TEACHER: Miss Woods! It is rude to yawn.

SISTER: Annabelle! Get up! We’re late for school!

VOICE 2: (Pg 31) But Annabelle paid no attention . . . She was busy listening to another voice. A new one. Her own.

VOICE 1: And when October came, Annabelle was wandering farther and farther into the forest, staying out longer and longer. Bringing stories from the night to share with Aunt Leaf.

VOICE 2: (Pg 33) But as the leaves turned yellow and fell one by one onto the grey earth, Aunt Leaf herself spoke less and less.

VOICE 1: Sometimes she spoke and made no sense at all . . .

AUNT LEAF: Bats in the grass! Stop pinching me! Don't eat that egg! Poison! Poison!

VOICE 1: (Pg 34-35) But Annabelle didn't care. She came back from the woods every night shining and shivering, climbed the stairs to where Aunt Leaf was waiting and told stories till the old woman fell asleep.

ANNABELLE: (very softly) This is the story of the blue pebble. This is the story of the dark. This is the story of the deep river. This is the story of the moon. *****

VOICE 2: Now came the bitter cold and one freezing night . . . Annabelle was not in her room.

FATHER: (Pg 36-37) Annabelle! Annabelle! My little girl is missing. My child is lost!

VOICE 2: Soon men arrived with lanterns and torches. They rowed out onto the river. They crisscrossed the fields on horseback. And they walked deep into the woods. . .

VOICE 1: Annabelle's mother put a vat of spiced cider on the stove and stirred and stirred so she would not be afraid.

SISTER: People come back. They do come back . . .
TRANSITION
They found Annabelle clad only in her nightgown, skin so white it was almost blue – almost
green. They brought her home and bundled her into bed.

VOICE 2: (Pg 40-41) What is real and what is not?

VOICE 1: Annabelle did not know anymore. [She] was so sick that dreams overtook her. She slept and woke and slept but could not tell which was which. She thought she heard Aunt Leaf call – but was too weak to get up.

VOICE 2: What is real and what is not? [Finally she got better]

ANNABELLE: (Pg 42-46) (rousing to look out the window) What has happened? Weren’t there leaves? Weren’t the woods filled with animals and birds? Didn't we spend all night telling stories? Aunt Leaf! Aunt Leaf?!

VOICE 2: But only the snow answered, softy brushing the window with its icy crystals.

ANNABELLE: Aunt Leaf? (long pause) What happened? I made it up. Aunt Leaf is just an old woman asleep upstairs. I was sick and now I'm better. And I am almost 12. I made everything up! Aunt Leaf!

VOICE 2: Annabelle stood in Aunt Leaf's dark room. . .

ANNABELLE: Did you know it was snowing? I went out in the snow. I went out because I heard a man chopping trees. I knew who he was. Uncle Greenleaf! I saw him walk to the tulip tree and I was afraid. No! No! You can’t have that one. It’s mine! It’s mine! One chop and it fell. Quiet. Like a cloud falling. It made no sound. He looked at me. Then he whistled for his dog and they walked back into the woods. But it was real. It was more than a story. Aunt Leaf! Aunt Leaf!

VOICE 2: Aunt Leaf did not move. (ANNABELLE puts her hand up to AUNT LEAF's cheek)

VOICE 1: Some things do not change when morning comes. Some things are not a dream. Annabelle sat looking out the window at the foggy world.

VOICE 2: Outside, the Tulip Tree lay on the white snow.

VOICE 1: Downstairs, Aunt Leaf’s body lay in a long black box.

VOICE 2: Do you know this story? Do you know the story of Aunt Leaf?
```

---

## IC-0010: Beyond Magenta: Transgender Teens Speak Out

- Title: Beyond Magenta: Transgender Teens Speak Out
- Author (byline): Susan Kuklin, Editor
- Work: Not specified
- Publisher: Candlewick
- Publication date as stated: March 2015
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: GIRL 1, GIRL 2, CHRISTINA, SCHOOL COUNSELOR, BEST FRIEND, NARRATOR, MOM, LOUDSPEAKER, PRINCIPAL, THE DEAN, DEAN, BOYS, CHRISTINA’S MOM
- Teaser before the introduction: Yes
- Spoken words (computed): 1151
- Already set (do not supply): none

### Source block (context only)

```text
Author: Susan Kuklin, Editor
ISBN: 978-0763673680
Publisher: Candlewick
Date (Month/Year): March 2015
```

### Introduction (context only: never use it for content warnings)

```text
The Human Rights Foundation has estimated that there are more than 2 million transgendered individuals in the US. We are parents, siblings, and children. We are your coworkers, your neighbors, and your friends -- A diverse community, representing all racial and ethnic backgrounds, as well as all faith traditions.

In 2021, President Biden declared March 31 as the Transgender Day of Visibility. A day to publicly recognize the resilience, strength and joy of not only transgender, but also nonbinary and gender nonconforming people. And it was a step . . .

But we still face severe discrimination, stigma and systemic inequality. In fact, according to The Human Rights Campaign, 2022 is on pace with more state legislation targeting transgender youth than any prior year.

Today, I want to give voice to a beautiful woman, Christina. This is her story and these are her words as found in Beyond Magenta edited by Susan Kuklin
```

### Performance text (classify this)

```text
NOTE: Speaker is a transgender woman

GIRL 1: (Pg 31-32) (laughing and gesturing) I don’t know what that is.

GIRL 2: Yeah, what is that?

CHRISTINA: Are those girls talking about me? (Christina stares at them)

GIRL 1: Can I help you with something?

CHRISTINA: Yeah, can you stop laughing at me?

GIRL 1: This is a free country; I can laugh at whoever I want. And how do you know I’m laughing at-chu?

CHRISTINA: Because I’m not stupid. I heard you say, “I don’t know what that is.”

GIRL 1: I know you’re a man with that big face.

CHRISTINA: (Pg 33) (to audience) I was trying not to cry, but it was really hurtful because . . . (holding back tears) People can be so nasty, so rude. I didn’t do anything to her. (beat) I’ve been called a man before. That makes me feel less a woman. I start questioning: Do I really pass in society? I don’t want to get emotional. I really, really hate being transgender. It’s a constant struggle. While everyone else my age is saving up for a car, I’m saving up to look possible. (Pg 34) When I go out, I can’t make any mistakes. My hair has to be exactly right. My makeup, my outfit, even my smell must be feminine. (beat) There were days when I would not go to school. My appearance stopped me. I just turned back.

CHRISTINA: (Pg 34) When I was born, I was named Matthew. When I was little, I wanted to be a girl, but I didn’t have a full understanding about it. I knew I was a boy because my mom and my dad told me I was one. (Pg 35) The teasing began in elementary school. They called me a sissy and a faggot. There was this girl in fifth grade. All the boys were crazy about her. She was the it girl. My ideal. I wanted to look like her. I wanted the attention from boys. Her name was Christina. At the time I thought that if I was a girl, my name would be Christina. My mom hates that name.

(Pg 36-37) My mother comes from a Catholic family who always went to church. I really was close to my family, but not anymore. They are just so narrow-minded. Every time I go to my grandmother’s house, they want to pray for me. I really don’t need to be prayed for.

My oldest brother had gone to an all-boys Catholic high school, where he became disciplined and focused. So off I went to Mount Saint Michael Academy, a Catholic high school for boys. I was so nervous. I asked my brother, “How do I act like a man?” He told me I had to walk a certain way, with a little lean, like a gangsta boy. I practiced . . . He taught me how to sit with my legs open. It was the most uncomfortable feeling in the world for me. It looked gross. He told me I had to deepen my voice and talk like a man.

(to other students) Oh, hey, what’s up? My name is Matthew. (to audience) It came off so phony; it just wasn’t me. At all! No one accepted me as a straight boy. Within a week, people started talking. “I think he’s gay.”

(Pg 39-40) I wasn’t really interested in learning. If there was a test, I’d study, but I wasn’t interested in English or history. I was interested in art and fashion. I drew girls a lot. To this day, I draw girls. One of the school counselors said.

SCHOOL COUNSELOR: I want to see your sketchbook . . . your art.

CHRISTINA: I showed her pictures of girl after girl after girl.

SCHOOL COUNSELOR: You know, when people draw, it’s a way of escaping. People draw what they want to be.

CHRISTINA: The moment she said that. I started thinking, Well, yeah, I want to be a girl, but it will never happen. (to counselor) I’d worry about passing. I don’t want people wondering what I am. I don’t want to get hurt. (to audience) But always in the back of my mind, I wished I was a girl. (Pg 41) One day, (Pg 43) I told my best friend that I wanted to become a girl . . .

BEST FRIEND: Don’t do that! God made you a boy for a reason. For a purpose. Why can’t you just be a gay man?

CHRISTINA: Before I educated myself about what being transgender really is, I thought that I must be a gay person. [But] the Google site said, “Sexual orientation has nothing to do with gender identity. There are gay and straight transgenders.” I thought I was gay because I was attracted to men. (beat) Straight men, not gay men.

NARRATOR: (Pg 42) [Finally], the summer before her senior year, Christina stopped worrying about what her mother would think . . .

CHRISTINA: (Pg 45) My senior year was my best and worst year in high school. (Pg 44) My hair grew long pretty fast. I dyed it red and got bangs. (Pg 45) The day before school started, I got my nails done. Pink. My mom completely freaked out.

MOM: You’re going to get in trouble. You’re going to get hurt. Somebody’s going to hurt you, baby.”

CHRISTINA: Mom, I’ll be fine. (to audience) I blew out my hair. I put on my makeup: purple eye shadow, mascara, blush and lipstick. (Pg 46) People just stared at me. I didn’t think I looked like a girl yet, but there was something about people acknowledging me, wondering what I was, that made me happy. (a big, confident smile) (long beat and the smile fades) I quickly became the school’s joke.

LOUDSPEAKER: (Pg 48-49) Send Matthew V to the principal’s office NOW.

PRINCIPAL: You can’t come to school dressed like a woman.

CHRISTINA: I am a woman.

PRINCIPAL: (angrily) You’re a boy! You’re creating this whole circus. Anything that happens to you is your fault because you’re coming to school dressed like a clown!

THE DEAN: (calmer and a little nicer) Look, Matthew, you know you can’t be wearing nails to school. [And] Why do you need to wear so much makeup? My wife doesn’t even wear that much make up.

CHRISTINA: Every girl is different. it’s not in the handbook, so I can do it.

DEAN: We didn’t think we had to address these things because it’s all boys here.

CHRISTINA: (long beat) I think the other students were freaked out because I looked like a girl and I was pressing gender boundaries. There were some instances . . .

BOYS: (Pg 50) You don’t belong here. Go somewhere else. Get out! Faggot!

CHRISTINA: So many people hated me for no reason (beat) (Pg 64) Sometimes I see Matthew in the mirror. Sometimes . . . when I’m lounging around the house with no makeup on or anything, I see him. (Pg 45) Sometimes I feel my mom misses her son. She doesn’t tell me, but she misses her son. (Looks critically in the mirror)

CHRISTINA’S MOM: (Pg 66) (enters) Hold on! Hold on! I have something to say. After all, I’m the one who had the problem with this. [I’m] Christina’s mom. (beat – she hugs Christina) I love my children. I would never throw them out. Some families throw their kids out and they wind up dead. I would never, ever do that.

I told [her] (to Christina) I’m glad that you are proud to be transsexual. But you can’t let people know. . . I had a lot of learning to do. (beat)

Don’t say horrible things to your child. Hug your children. (she hugs Christina) Hug them. I learned through Christina. I listened to my daughter. And I learned by letting her be.
```

---

## IC-0011: The Book Thief

- Title: The Book Thief
- Author (byline): Markus Zusak
- Work: Not specified
- Publisher: Knopf Books for Young Readers
- Publication date as stated: Sept 2007
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DEATH, RED
- Teaser before the introduction: Yes
- Spoken words (computed): 1204
- Already set (do not supply): none

### Source block (context only)

```text
Author: Markus Zusak
ISBN: 978-0375842207
Publisher: Knopf Books for Young Readers
Date (Month/Year): Sept 2007
```

### Introduction (context only: never use it for content warnings)

```text
U Krakovianki once stated, “Death is constantly interrupting us – and then the story moves on. The interruptions do not stop the story – it goes on. Some people are no longer a part of the story, but it goes on just the same until death interrupts again: a pattern as old as the world.”

Death is inevitable. We hear about it, witness it, and fearfully wait for it. And though we see it as the enemy, it’s a natural part of life. In this selection, by humanizing death and putting a name and face to the “enemy,” we are shown that nothing is purely black and white. Death personified is just as affected as we are by occurrences that take place in the novel, The Book Thief by Markus Zusak.
```

### Performance text (classify this)

```text
DEATH: (Pg 3) ***HERE IS A SMALL FACT*** You are going to die.

Does this worry you? I urge you – don’t be afraid. I’m nothing if not fair. I am in all truthfulness attempting to be cheerful about this whole topic, though most people find themselves hindered in believing me. Please, trust me. I most definitely can be cheerful. I can be amiable. Agreeable. Affable. And that’s only the A’s. Just don’t ask me to be nice. Nice has nothing to do with me.

DEATH: (Pg 4-5) I could introduce myself properly, but it’s not really necessary. You will know me well enough and soon enough, depending on a diverse range of variables. At some point in time, I will be standing over you. Your soul will be in my arms. A color will be perched on my shoulder [and[ I will carry you gently away. The question is, what color will everything be at the moment when I come for you? What will the sky be saying? I try to enjoy every color I see – the whole spectrum. A billion or so flavors, none of them quite the same. My one saving grace is distraction. It helps me cope, considering the length of time I’ve been performing this job. The trouble is, who could ever replace me? The answer, of course, is nobody, which has prompted me to make a conscious, deliberate decision – to make distraction my vacation. Needless to say, I vacation in increments. In colors. (Pg 6) First up is something white. Of the blinding kind. Some of you are most likely thinking that white is not really a color. Well, I’m here to tell you that it is. White is, without question a color, and personally, I don’t think you want to argue with me. Please, be calm, despite that previous threat. I am all bluster – I am not violent. I am not malicious. I am a result. (Pg 9) Next is a signature black, to show the poles of my versatility, if you like. It is the darkest moment before the dawn. Sometimes I arrive too early. I rush, and some people cling longer to life than expected. (Pg 11) For just a moment, despite all of the colors that touch and grapple with what I see in this world, I will often catch an eclipse when a human dies.I’ve seen millions of them. I’ve seen more eclipses than I care to remember.

(Pg 12) The last [color is] red. (Pg 14) When I recollect, I see a long list of colors, but it’s these three that resonate the most. Sometimes I manage to float far above those [colors]. I hang suspended, until a septic truth bleeds toward clarity. That’s when I see them formulate. ***THE COLORS***

RED: WHITE: BLACK.
They fall on top of each other. The scribbled signature black, onto the blinding global
white, onto the thick soupy red.
(Pg 174-175) I’ve seen so many young men
Over the years who think they’re
Running at other young men.
They are not.
They’re running at me.

(Pg 307-309) I do not carry a sickle or scythe. I only wear a hooded black robe when it’s cold. And I don’t have those skull-like facial features you seem to enjoy pinning on me from a distance. My travels, what I saw in ’42. There’s a reason for me explaining what I saw in that time. There were certainly some rounds to be made that year, from Poland to Russia to Africa and back again. You might argue that I make the rounds no matter what year it is, but sometimes the human race likes to crank things up a little. They increase the production of bodies and their escaping souls. A few bombs usually do the trick. Or some gas chambers, or the chitchat of faraway guns. So many humans.

So many colors. And then. There is death. Making [my] way through all of it. On the surface: unflappable, unwavering. Below: unnerved, untied, and undone. In all honesty, I was still getting over Stalin, in Russia. The so-called second revolution – the murder of his own people. Then came Hitler. They say that war is death’s best friend, but I must offer you a different point of view on that one. To me, war is like the new boss who expects the impossible. He stands over your shoulder repeating one thing, incessantly: “Get it done, get it done.” So you work harder. You get the job done. The boss, however, does not thank you. He asks for more. (Pg 349) I’ll never forget the first day in Auschwitz, the first time in Mauthausen. I picked them up from the bottom of the great cliff, when their escapes fell awfully awry. There were broken bodies and dead, sweet hearts. Still it was better than the gas. Some of them I caught when they were only halfway down. Saved you, I’d think, holding their souls in midair as the rest of their being – their physical shells – plummeted to the earth. All of them were light, like the cases of empty walnuts. (Pg 336) I carried them in my fingers, like suitcases. Or I’d throw them over my shoulder. It was only the children I carried in my arms. (Pg 350) I shiver when I remember – as I try to de-realize it. I blow warm air into my hands, to heat them up. But it’s hard to keep them warm when the souls still shiver. God. I always say that name when I think of it. God.

Twice, I speak it. I say His name in a futile attempt to understand. “But it’s not your job to understand.” That’s me who answers. God never says anything. You think you’re the only one he never answers? “Your job is to…” And I stop listening to me, because I tire me. When I start thinking like that, I become so exhausted, [but] I’m compelled to continue on, because although it’s not true for every person on earth, it’s true for the vast majority – that death waits for no man – and if he does, he doesn’t usually wait very long. Please believe me when I tell you that I picked up each soul as if it were newly born. I even kissed a few weary, poisoned cheeks. I listened to their last, gasping cries. Their vanishing words. I watched their love visions and freed them from their fear. They were French, they were Jews, and they were you. (Pg 503) So many people chased after me in that time, calling my name, asking me to take them with me. (Pg 543) It has been many years since all of that, but there is still plenty of work to do. I can promise you that the world is a factory. The sun stirs it, the humans rule it. And I remain. I carry them away. (Pg 549) Yes, I have seen a great many things in this world. I attend the greatest disasters and work for the greatest villains. But then there are other moments. There’s a multitude of stories that I allow to distract me as I work, just as the colors do. I pick them up in the unluckiest, unlikeliest places and I make sure to remember them as I go about my work. (Pg 550) ***A LAST NOTE FROM YOUR NARRATOR*** I am haunted by humans.
```

---

## IC-0012: Boy Gets Girl

- Title: Boy Gets Girl
- Author (byline): Rebecca Gilman
- Work: Not specified
- Publisher: Faber and Faber, Inc
- Publication date as stated: May 2000
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: THERESA'S VOICE, TONY, THERESA, MERCER, BECK
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
Theresa agrees to go on a brief blind date with Tony, a man who knows a friend of a friend. Over a drink, the two engage in stilted small talk . . . But when he asks for a follow up dinner date shortly into their conversation, the first red flag emerges. Theresa is careful to maintain boundaries however, refusing to give out her home phone number and shrugging off his hug in favor of a handshake. At the following dinner date she calmly informs him that there will not be a third date. End of experience. Or not . . . Tony’s phone calls become constant and an endless succession of flower bouquets come to her office. He eventually sneaks his way up to her office, asking her to lunch. Theresa assertively tells Tony to leave her alone and never contact her again. She assumes that she’s seen the last of him, but she’s not so lucky . . .

Boy Gets Girl by Rebecca Gilman

Theresa's apartment: a small apartment with a futon couch/bed, desk, and lots of bookshelves. It is late Saturday night. THERESA is fully dressed, sitting up in bed, working on a laptop. The phone rings, but she makes no move to answer it. After a couple of rings her machine picks up. Theresa's voice comes on.
```

### Performance text (classify this)

```text
NOTE: In the play Beck is a female officer, but this cutting does not reference a gender for either – Mercer is Male.

THERESA'S VOICE: You've reached my machine. Leave a message. (Tony’s voice comes on)

TONY: Hi, it's me again. It's past one and it's too late for you to be out by yourself, I think. I know you don't really want to talk to me or anything, but I'm just worried about you. I'm wondering if you've gone out of town or something. You haven't answered your phone all night. I did what you asked, and I stopped sending you flowers. But anyway, I know you've been working hard lately and I want to do something for you, but you won't let me send you flowers, so I was just thinking, maybe you'd let me cook you dinner? Maybe tomorrow night? I mean, you haven't even seen my place yet. So give me a call when you get in, because I'll be up. Okay? . . . Okay. Bye.

(The machine clicks. THERESA, who has stopped working in the middle of it, starts again. Pause. The phone rings again. Her voice comes on)

THERESA'S VOICE: You've reached my machine. Leave a message.

TONY: It's me again. I just . . . I left that message to call me when you got in and then I just had a thought: maybe you're not getting in. Maybe you're sleeping with somebody else right now. And the thought of that just made me feel like I wanted to throw up. If you're seeing somebody else I just want to know. I don't want you to think you have to spare my feelings, because if you think that, then you must think I'm some pathetic jerk. Which would make me very angry, Theresa, because I don't need your pity. I'm not asking for your pity for one ***** second. I just think that you owe me the truth. (THERESA, who has been staring at her computer through this, suddenly loses it and makes a grab for the phone.)

THERESA: (Snatching up the receiver) Stop calling me! Don't send me things, don't try to see me. Don't ever speak to me again! (She hangs up) Jesus Christ!

(Beat. The phone rings again. Furious, she tries to unplug it, can't get the plug out, then rips the cord from the wall. Silence. She goes back to the bed, sits down. She is shaking. She looks toward the window. She sits for a moment and thinks, then she quickly turns off the lights. In the dark she gets up, goes to the door, and checks it. It's locked. Then she gets a chair and pushes it up under the handle.)

TRANSITION According to the National Center for Victims of Crime, 6.6 million people are stalked in each in the United States. But to go even further . . . 54% of female murder victims had reported stalking to police before they were killed by their stalkers. Anyone can be a victim of stalking.

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

## IC-0013: The Clown of God

- Title: The Clown of God
- Author (byline): Tomie dePaola
- Work: Not specified
- Publisher: Voyager Books
- Publication date as stated: 978-0156181921
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, GIOVANNI, MAESTRO, CROWD, BROTHER, TOWNPERSON, PEOPLE, WOMAN, BROTHER SEXTON, PRIEST
- Teaser before the introduction: No
- Spoken words (computed): 1277
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tomie dePaola
ISBN: 978-0156181921
Publisher: Voyager Books
Date (Month/Year): 978-0156181921
```

### Introduction (context only: never use it for content warnings)

```text
(Hum a few lines from The Little Drummer Boy)

It was Saint Therese of Lisieux who said: “You know well enough that Our Lord does not look so much at the greatness of our actions, nor even at their difficulty, but at the love with which we do them.” This was true of America’s Little Drummer boy and can be found in many legends and fables world-wide. A poor soul with little worthy to give a King, but with a heart so big, so open – that in itself becomes a gift.

based upon a French legend . . . The Clown of God by Tomie dePaola
```

### Performance text (classify this)

```text
NARRATOR: Many, many years ago, in Sorrento . . . there lived a small boy named Giovanni who had no mother and not father. He dressed in rags and begged his bread and slept in doorways. But he was happy, and he could do something wonderful. He could juggle. Every day he would go to Signor Baptista’s fruit and vegetable stall and juggle.

He would juggle lemons and oranges, apples and eggplants, and even zucchini. Crowds would gather to watch, and when Giovanni had finished, they would buy from Signor Baptista. Then Signor Baptista’s wife would give Giovanni a bowl of hot soup. It was a very good arrangement.

One day a troupe of traveling players came to town, and Giovani watched as Arlecchino and Colombina*, in their beautiful clothes, danced and sang.

GIOVANNI: (wonderstruck) Oh, that is the life for me!

NARRATOR: So when the play was over, Giovanni went and spoke to the Maestro.

MAESTRO: No, no. I have no need for a ragamuffin. Go beg your bread somewhere else.

GIOVANNI: (pleading) But I could be very helpful. I could help unpack and pack up. I could take care of the donkey, And, Maestro . . . . I can juggle! (he demonstrates)

MAESTRO: Not bad. With a bit more training and practice . . . All right! But no money. A place to sleep, the companionship of the finest players in Italy, and a bowl of noodles. That’s all.

GIOVANNI: Grazi, Signor.

MAESTRO: Go get your things. We leave in an hour.

NARRATOR: And so Giovanni said good-bye to Signor and Signora Baptista and became a traveling player.

Not long after, the Maestro gave him a costume and Giovanni juggled for the crowds. He would put on a clown face, step out from the curtain before the play began, bow, open up a colorful bag, roll out a carpet, and begin. He would juggle sticks. Plates. Then he would balance the plates on the sticks and twirl them. He would juggle clubs, rings, and burning torches.

Finally he would toss a red ball and an orange ball. Then a yellow ball. A green, a blue, and a violet ball until it looked as if he were juggling the rainbow.

GIOVANNI: And now for the Sun in the Heavens!

NARRATOR: Still juggling, he would pick up a shining golden ball and toss it higher and higher, faster and faster. And how the crows would cheer.

CROWD: (cheering)

NARRATOR: Giovanni became very famous, and it wasn’t long before he said good-bye to the traveling troupe and set off on his own. Up and down Italy he traveled, and although his costume became more beautiful, he always kept the face of a clown. Once he juggled for a duke. Once for a prince! And it was always the same.

First the sticks, then plates, then the clubs, rings, and burning torches. Finally the rainbow of colored balls.

GIOVANNI: And now for the Sun in the Heavens!

NARRATOR: And the golden ball would fly higher and higher and the crowds would laugh and clap and cheer.

One day, between two towns, Giovanni was sitting in the shade of a tree, eating a lunch of bread and cheese. Two Little Brothers came down the road.

BROTHER: Will you share your food with us, good clown, for the love of God and the blessing of our Brother Francis?

GIOVANNI: Sit down, good fellows. There is more than enough.

NARRATOR: As the three men ate, the two Little Brothers told Giovanni how they went from town, begging their food and spreading the joy of God.

BROTHER: Our founder, Brother Francis says that everything signs of the glory of God. Why, even your juggling.

GIOVANNI: That’s well and good for men like you, but I only juggle to make people laugh and applaud.

BROTHER: It’s the same thing. If you give happiness to people, you give glory to God as well.

GIOVANNI: (laughing) If you say so! But now I must be off to the next town. Arrivederi, good brothers – and good luck!

NARRATOR: Wherever Giovanni went, the air was filled with his flying sticks and plates, his clubs and rings and torches. And, always, his rainbow of balls and “the Sun in the Heavens.” And wherever Giovanni went, the faces of the crowds would be all smiles, and the sound of laughter and cheers would ring through the towns. Years passed. Giovanni grew old and times became hard. People no longer stopped to watch.

TOWNPERSON: It’s only the old clown who juggles things. We’ve all seen him before.

NARRATOR: Giovanni was sad, but still he juggled, until one day he dropped “the Sun in the Heavens,” and the rainbow of balls came crashing down and the crowd stood around him and laughed!

CROWD: (pointing and laughing)

NARRATOR: But not from joy. Then they did a terrible thing. They threw vegetables and stones at Giovanni, so that he had to run for his life.

Beside a stream, Giovanni took off his clown face. He put away his sticks and his plates, his clubs and rings and colored balls. He put away his costume and he gave up juggling forever. What little money he had soon was gone, and his clothes became rags. He begged his bread and slept in doorways as he had done as a child.

GIOVANNI: (wearily) It’s time to go home.

NARRATOR: And he headed back to Sorrento. It was a cold winter night when he finally arrived. The wind blew hard, and an icy rain was falling. Up ahead loomed the monastery church of the Little Brothers. The windows were in darkness. Wet and cold, old Giovanni crept inside and fell in a heap in a corner. Soon he was asleep. (Giovanni snores softly) It was the music that woke him up. The church was blazing with candlelight and filled with people singing

PEOPLE: (singing) Gloria! Gloria!

NARRATOR: Giovanni could scarcely believe his eyes. So much beauty! A long procession of brothers, priests, sisters and townspeople, all carrying beautiful gifts was winding its way through the church. They placed their gifts in front of a statute – of a lady and her child.

GIOVANNI: What is all this?

WOMAN: Why, old man, it’s the birthday of the Holy Child. It’s the procession of the gifts.

NARRATOR: Giovanni watched in amazement until the singing was over. Then the church emptied of all the people and was darkened except for the bright candles surrounding the Lady and the Child. Giovanni moved closer. The Child in the Lady’s arms seemed so serious, so stern.

GIOVANNI: (kneeling) Oh, Lady. I wish I had something to offer, too. Your child seems so dad, even with all these beautiful gifts. But wait – I used to make people smile.

NARRATOR: Giovanni opened his bag and shook out his old costume. Then he put on his clown face, bowed, rolled out the little rug, and began to juggle. First the sticks. Then the plates. Next he twirled the plates on the sticks. And then the clubs and rings . . .

The Brother Sexton, who was coming in to lock the doors, saw Giovanni juggling. He was horrified.

BROTHER SEXTON: Father Master! A sacrilege! Come quickly!

NARRATOR: But Giovanni didn’t hear or notice him.

GIOVANNI: (smiling at the Child) And now . . . First the red ball, then the orange . . . Next the yellow. And the green, blue and violet.

NARRATOR: Around and up they went until they looked like a rainbow.

GIOVANNI: And finally . . . The Sun in the Heavens!

NARRATOR: The gold ball flew up and around and around, higher and higher. Giovanni had never juggled so well in all his life. Higher and higher, faster and faster. A blaze of color filled the air. It was magnificent! Giovanni’s heart was pounding.

GIOVANNI: For You, sweet Child, for You! (he suddenly collapses)

NARRATOR: The priest and Brother Sexton came rushing in.

PRIEST: (kneeling over Giovanni, he makes the sign of the cross) Why, the poor clown is dead. May his soul rest in peace.

NARRATOR: But the Brother Sexton backed away . . .

BROTHER SEXTON: (backing away, he gapes at the statue of the Lady and her Holy Child; he points) Oh, Father! Oh, Father, look!

NARRATOR: The Child was smiling, and in His hand He held the golden ball.

(Softly hum a few lines from The Little Drummer Boy)
```

---

## IC-0014: Consequences

- Title: Consequences
- Author (byline): Aaron Fraire
- Work: Consequences
- Publisher: SpeechGeek
- Publication date as stated: 2015
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1352
- Already set (do not supply): none

### Source block (context only)

```text
Consequences by Aaron Fraire
ISBN: 978-1-61387-116-4
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
Please Note: This role is written as a male, but it may be played by a female. Adjustments are allowed for pronouns and spouse references, if desired.

The Interrogator is a CIA defense contractor working in Iraq. The Interrogator is a master manipulator who can be both friendly and sinister. He can turn on a dime and is always engaged in psychological warfare. However, he has also been in this job for too long and has seen too much. As a result, he is as fractured as many of the detainees he interviews.

INTERROGATOR. Hey, you’re the new guy? OK. Well…

You’ve seen the rest of the base? Good. Well, this is the break room. No, no, not “the breaking” room. We don’t do interrogations in here. This is just for us. This room has carpet.

This room is just for us. We come here to reset between interrogations. So, if you need to vomit or wash up, you’ll do it there. If you need whiskey, or a cigarette, or pills to get right, they’re there. There’s porn there, there, and there. And if you’re religious...sorry. God’s not here. We tell God to wait outside.

Welcome to Iraq...hell’s outhouse. Charming, right?

In April 2004, CBS News published proof that the United States Army and the CIA had committed torture and human rights violations against detainees in the Abu Ghraib prison in Iraq. While some defended these actions as interrogation tactics and wartime necessities, others argued that such measures were inhumane and thoroughly un-American. In his play, Aaron Fraire examines the cost of torture from an unusual vantage point – the interrogator.

Ultimately suggesting that when we abandon our humanity, even in the name of duty, we must be prepared for Consequences by Aaron Fraire.

INTERROGATOR. Here’s how it works. Every few days a truck full of assets arrives and we sort them into priority intelligence groups – PIGs. And every one of these PIGs comes with a folder like this one. Inside we have every piece of information available: addresses, aliases, contacts, bank accounts, blood type, shoe size. Sometimes they are large packets of information. Other times, it’s just one sentence: Suspected of Anti-Coalition Activities. You just never know.

And here, on the front, it tells us what the objectives are and what level PIG we’re dealing with.

See, level 1 PIGs are worthless guys – messengers, foot soldiers, etc. Level 2 PIGs are important, but not directly responsible parties – brokers, family members, coordinators, and the like. And Level 3 PIGs are the doers - bombmakers, spies, kidnappers, the nameless faceless terrorists that make this world so uncomfortable. Every once in awhile we get a Level 4 – a faction leader, an overlord, a frontrunner - someone who sows the seeds in this perennial crap fest.

You know sometimes I wonder what Level we would be. I think other people would say we’re a 2. Just tools of the trade. But I don’t know…

So, I got six days left and then, I’m headed back to the states and this place is all yours. khalas jayid (Good riddance) You ever feel like that?

Oh. This is your first post? Wow. Why would they send you here on your first assignment? No, don’t get me wrong, I’m sure you’re good but…

Your first post, Jesus.

Well, hal tatakallamee ara’rabiyya? (Do you speak Arabic?) Not bad.

So, you wanna know, like, all of it? Everything?

Ok...I’ve got an idea. Nah, this’ll be fun. Interrogate me. I’m serious, Rookie. Let’s see what you’ve got. I’ve got information, you need information. Interrogate me.

Family? OK. Yes. I’ve got a wife and two kids. What does that matter? You’re trying to establish a rapport, OK. But you’ve got me here. I know where I am and why I’m here. You’re not going to sneak information out of me. So don’t do that. You don’t have time to be shitty at this, try again.

I know, it’s weird. There’s carpet in here, and you don’t have a folder, but you know what you wanna ask me…

How did I get here? Good. Better. I ask myself that same question every day.

I did two tours in Iraq with the Rangers and I got that sand in my blood, I guess. I applied at the Agency and got jumped into the interrogation program. I’ve been with the CIA for almost 5 years, been in this hell hole for 2 of them, I’ve done over 900 interrogations and, I don’t wanna brag, but I’ve become a very high functioning alcoholic.

Look, kid. You have to have a sense of humor in this place or the stench alone will make you go funny. It’s not easy, I know. Nothing about this job is easy. Well, I shouldn’t say that. What I should say is that when this job starts to feel easy, that’s when you get out. That’s what Taylor said - you get out or it gets you out.

Taylor? Good guy. He’s gone now, but he was here with me… before. He was here for eighteen months, I think? Must be. He arrived a few months after me. Or was it before me? I gotta tell you, I can’t keep my days straight sometimes. Which is actually really funny, because that’s one of the ways we screw with PIGs. We try to fuss with their sense of things. You know?

Taylor knew. He knew that the blood doesn’t come off. That’s why he hung himself right there.

Taylor. Never could get it right. You don’t do it in a room with carpet.

Taylor is a good soft spot! You smelled that out, didn’t you? Yeah. Oh, nice moves, Rookie. Good work. Now, you gotta choose. Are you gonna push on it, probe it to see if it’ll upset me? You gonna let it go? Is it a way in, or is it a dead end? Where do you want this thing to go? Keep your eye on the ball!

Because what you do, interrogation, isn’t just about getting information. It’s about getting inside their heads. Its getting someone's will to work against them. The idea is that you put two opposing voices in someone’s head. So, like, one voice suggests that I shouldn't be cooperating, that Rookies should learn for themselves and another voice that suggests that I should make you fully aware of what you’re walking into. You know which voice you want me to listen to...So ask!

What does it feel like? That’s the $64,000 question! That’s the one that sets your teeth on edge. You wanna know what it’s like, so you can tell yourself you’re ready. You’re never ready.

You’ll walk into the room, it’ll be dark and wet and cold. They’ll sit him down in front of you like the sack of trash they want you to think he is, they’ll tell you he did something - anything - doesn’t even matter what anymore, and you’ll go to work. You’ll ask him questions, but part of you won’t want him to answer. Part of you will want to punish him for what you saw, the generations of lives lost because of him and his friends, so you’ll use your hands, and you’ll use rope, you’ll hook his ass up to a generator and jumpstart him like a car. You’ll do it until the only screaming left is yours saying, “Have you had enough?”

You’ll do it until you finally answer back, “YES! I’ve had enough.”

Because what we do destroys people. And it’s not just them. You can’t do this without getting it all over you.

Why do we do it? Now that...is a great question. They’ll tell you it’s for intel. That it’s to save American lives. And you’ll believe that. You’ll have to. But somewhere inside you’ll know that you won’t be one of those lives saved. That’s the price we pay for doing this, Rook.

So there you go. Good interrogation, kid. Seriously, couldn’t have done it better myself.

6 more days. Until I go home to my wife and my kids…and my conscience.

God bless America.
```

---

## IC-0015: Count Alaric’s Lady

- Title: Count Alaric’s Lady
- Author (byline): Barbara Leonie Picard
- Work: Selected Fairy Tales
- Publisher: Oxford University Press
- Publication date as stated: Oct 1995
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ALARIC, LADY, MAGDA, FAIRY PEOPLE
- Teaser before the introduction: Yes
- Spoken words (computed): 2103
- Already set (do not supply): none

### Source block (context only)

```text
Author: Barbara Leonie Picard
Book: Selected Fairy Tales
ISBN: 0192741624
Publisher: Oxford University Press
Date(Month/Year): Oct 1995
```

### Introduction (context only: never use it for content warnings)

```text
Count Alaric’s Lady by Barbara Leonie Picard
```

### Performance text (classify this)

```text
Early in the morning of one Midsummer Day, young Count Alaric rode out of his castle alone. The count was joyful as he rode his horse over his fields, for the sun was shining and life was good. Halfway across a meadow, he saw a maiden in a gown of green, sitting on the grass. Her feet were bare, and on her hair of flaxen gold she wore a wreath of moon daisies. Alaric reined in his horse.

ALARIC: You are a stranger here, fair lady. Will you tell me your name?

LADY: I do not know my name.

ALARIC: (in surprise) But where do you come from?

LADY: I do not know.

ALARIC: Can you tell me nothing about yourself?

LADY: Nothing, but that for an hour or two I have sat in this field, watching the sun rise higher and listening to the song of the lark. Count Alaric looked down at her pale, strange beauty, and she looked up at him and smiled, and he knew he wanted to help her more than anything in the world. Yet there was a look in her golden-green eyes that he had never seen before—a look as though, even while she smiled at him, she was thinking of something else.

ALARIC: My castle is yonder. Will you come there with me?

LADY: I will. As the maiden had no name, he called her Catherine, because he knew of no name more beautiful. And since he loved her and she was willing, he married her.

But though they were happy and talked and laughed together, whenever he looked into her eyes he saw she was thinking of something else. With others, she was shy and silent, and when dances were held at the castle, she would sit by the wall and watch and smile. But one day Alaric came upon her in a room alone, dancing in a shaft of sunlight that streamed through a window.

ALARIC: You dance so lightly and gracefully. Why will you never dance with me?

LADY: (Puzzled frown) I never want to dance.

ALARIC: (laughs) You were dancing a moment ago, dearest. I saw you as I came in.

LADY: (face lightens) Ah yes. I heard the music and I had to dance.

ALARIC: But, dearest, there was no music.

LADY: But there was! Sometimes I hear it in the distance, but today it seemed quite near. (Listens for a moment)

LADY: (sadly) It is all silent now.

ALARIC: (taking her hand in his.) Tell me truly, Catherine, are you happy with me?

LADY: Of course I am happy with you. But his heart was heavy, for still he saw the look in her eyes, as though she thought of something else. A year passed, and it happened that on Midsummer Eve, Count Alaric was returning home from a short journey. All through the night he rode, hoping to be with Catherine at the very same hour he had found her, twelve months before. Towards dawn, as he passed the meadow where he had first seen her, he heard strains of sweet music. He rode towards it over the grass, and in the fading moonlight he could see some twenty or thirty figures in gowns of green, dancing barefoot in the dew.

ALARIC: (wonderingly, to himself) It is the fairy people. They have come here to dance on Midsummer Eve. And then he noticed that one among them wore crimson instead of green.

ALARIC: That hair, and that little chin. And I have seen her wear that gown before. But he could scarcely believe it, and he watched for many minutes before he knew beyond doubt that the dancer was Lady Catherine.

ALARIC: The fairy people have lured her from the castle! There is no time to lose. I must save her from their power. He urged his horse forward, but the horse took fright and bolted, fleeing like a mad creature back the way it had come. It carried him three miles before he could calm it and turn it around. But before he reached the meadow, the cock had crowed, and he found the field deserted. He rode on to the castle and went straight to his lady’s room, fearing to find it empty. But when he flung back the velvet curtains around the bed, he saw her sleeping there, her pale hair spread over the pillow. She awoke and smiled.

ALARIC: Dearest, is all well with you?

LADY: Of course. You are home early, and I am glad.

ALARIC: What did you do last night, Catherine?

LADY: I slept. What else should I do? (smiles) I am tired, and you ask so many questions. Wake me again when the sun is high.

ALARIC: (softly to himself) I must have been mistaken. It could not have been her in the meadow. He turned from the bed and walked softly away. But there hanging over a chair was her gown of crimson brocade, and he saw that the hem was dark and wet, as though it had been dragged in the dew. Count Alaric thought much on what had passed that Midsummer Eve, and on the look he saw always in his lady’s eyes. And at last he told himself,

ALARIC: I can bear this no longer. I will go out on the moors and visit wise old Magda. If anyone can advise me, it is she. So Count Alaric rode across the heath to the tumbledown hut of Magda. He knocked, and a voice of dignity answered.

MAGDA: Come in. He stooped to pass inside the door, and in the dim light he saw Magda, standing by the fire and stirring a pot of steeping herbs with her strong peasant hands. She turned to him and smiled.

MAGDA: Good day, Count Alaric. Sit you down. You are in trouble, or you would not have sought me out.

ALARIC: It is of my Lady Catherine that I would speak with you. And he told her all about the strange maiden he had married, and how he had seen her on Midsummer Eve dancing with the fairy people, and about the look always in her eyes, as though she were thinking of something else. When he had done, Magda was silent for a while, then looked at him with eyes full of pity and understanding.

MAGDA: Alaric, your lady is one of the fairy people.

ALARIC: It cannot be!

MAGDA: The time you found her, she must have been dancing on Midsummer Eve as the fairy people do, and happened to remain in the meadow at dawn when the others departed. Away from her people, she would forget much of her life with them, and so could tell you nothing of herself.

ALARIC: But if she is one of them, must I then lose her?

MAGDA: So long as she remembers anything of her fairy life, she will never be wholly yours. She will always hear the fairy music borne on the wind, and on Midsummer Eve she will have to dance with her people—and one day she may not return. And even if she should come back each time, you will always see in her eyes the look that troubles you.

ALARIC: (in despair) Is there no way to make her forget the fairy people? Can I never win her completely for my own?

MAGDA: There is only one way. You must give her a love that is perfect—a love that leaves no room for memory of any other life.

ALARIC: But my love is perfect. Magda, I would die for her!

MAGDA: (shakes her head) If your love were truly perfect, she would be wholly yours. But do not despair. Go home and see what time will do to help. From that day on, Count Alaric was even kinder to his lady than before, if that were possible. Yet daily he grew more sad, for still he saw she thought of something else. Winter came, and after that the spring, then spring was gone and summer back again. On Midsummer Eve, Count Alaric watched and waited, and at dusk he saw his lady slip through the castle gate and run toward the fields. He buckled on his sword and mounted his horse. When he reached the meadow, he heard the music and saw once again the fairy people, dancing barefoot in their fluttering gowns of green. And among them in blue velvet was his lady, her feet bare and her pale hair flying, just the same as theirs. The count left his horse and came nearer, keeping to the shadows where he could. And as he watched his lady dance and laugh, he felt his heart would break.

ALARIC: (softly to himself) She must be mine! I will take her at any cost. He stepped among the dancers and seized her by the wrist. The fairy people scattered and fluttered into a group a little way off, with their white faces turned to him in the moonlight. And his lady would have followed, but he held her fast.

ALARIC: Catherine, it is Alaric, your husband. I have come to fetch you home.

LADY: Let me go! And the fairy people held out their arms like white moonbeams and moaned, “Come back, our sister, come back.” Yet Alaric’s hold was too strong, and after a while she ceased her struggling. Then she smiled cunningly at him, and touched his cheek and stroked his hair.

LADY: Dear husband, my people wait for me. Let me join in the dance, and when it is over, I promise I will come back to you.

ALARIC: (shakes his head) The promises of the fairy people are as breath in the wind. If I let you go, you may never come back to me.

LADY: (in tears) The fairy people have no tears, but you have taught me how to weep. And Alaric turned his gaze away so pity should not make him weak. The fairy people swayed closer. Around the count and his lady they made a circle, and she cried out to them,

LADY: Give me now your strength, my people!

FAIRY PEOPLE: Be strong, our sister, be strong.
And Count Alaric’s lady became a sapling, and his hand was on its trunk, and a
strong wind bent it away to tear it from his hold.
But he clung to the tree tightly, and the wind died down and was still.

FAIRY PEOPLE: Be wild, our sister, be wild.
And Count Alaric’s lady became a vixen, which twisted and turned and snapped at
him.
But he held it close until it lay panting in his arms.

FAIRY PEOPLE: Be flowing, our sister, be flowing.
And Count Alaric’s lady became water which would have trickled through his
fingers.
But he cupped his hands and caught every drop.

FAIRY PEOPLE: Be fiery, our sister, be fiery.
And Count Alaric’s lady became a magic flame that seemed to scorch away his
flesh.
But he cried in his pain,

ALARIC: If I hold you till dawn, you will still be partly mine. . . . and he did not let go of the flame. Then Count Alaric’s lady in her own shape sank upon the grass.

LADY: (softly) You are too strong for me, and I cannot leave you.
The voices of the fairy people rose in a wail, and the circle broke.
The count looked up and saw with joy a streak of saffron in the east. But when he
looked down to where his lady crouched and moaned, his heart was troubled.

ALARIC: (gently) Catherine, if you stay with me, will you remember your people and be sad?

LADY: I shall only faintly remember them. I shall not be sad, but I shall always feel there is something I have lost.

ALARIC: And if you went back to your people, would you remember me and our life together and regret that it was past?

LADY: I should remember none of it. So I should have no regrets and be only happy.

ALARIC: (remains silent a moment) I would not wish your happiness lessened for even a minute. Dearest, go back to your people. And he let go of her wrist. In the distance, the first cock crowed. Alaric turned and ran to his horse, and he never looked back, for he could not bear to see the meadow empty behind him. For an hour he rode blindly, not caring where his horse carried him. When again he noticed where he was, he found himself nearing the castle. And there on the dusty road before him trudged a solitary figure in blue velvet.

ALARIC: Catherine! (He raced to her side and found her very close to tears)

LADY: Oh, Alaric! I woke up and found myself alone in a meadow, and I was so afraid. I must have walked there in my sleep. Did you ride out to look for me? Were you afraid too?

ALARIC: (smiling) I rode out to look for you. And I was afraid.
Alaric dismounted and took her hand, and when he looked into her eyes, he saw she
thought only of him and of her and of their life together.
And he knew that now she was wholly his, for his love at last was perfect.
```

---

## IC-0016: The Crickets Have Arthritis

- Title: The Crickets Have Arthritis
- Author (byline): Shane Koyczan
- Work: Our Deathbeds Will Be Thirsty, Pgs 30-35
- Publisher: McKellar and Martin
- Publication date as stated: 2012
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1297
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shane Koyczan
Book: Our Deathbeds Will Be Thirsty, Pgs 30-35
ISBN: 978-0986576775
Publisher: McKellar and Martin
Date (Month/Year): 2012
```

### Introduction (context only: never use it for content warnings)

```text
* According to the American Childhood Cancer Organization, each year in the U.S. an estimated 15,800 children between the ages of birth and 19 years of age are diagnosed with cancer. Approximately one in 285 children will be diagnosed with cancer before their 20th birthday.

Unfortunately, for some children the battle with cancer doesn't end in the word "remission" or "cure," but in death. These brave little warriors have lost their battle with the cancer monster; and have traded their armor for angel wings.

The Crickets Have Arthritis by Shane Koyczan
```

### Performance text (classify this)

```text
(Pg 30-35) it doesn’t matter why I was there, where the air is sterile and the sheets sting. it doesn’t matter that I was hooked up to this thing that buzzed and beeped every time my heart leaped, like a man whose faith tells him: gods hands are big enough to catch an airplane

or a world,

doesn’t matter that I was curled up like a fist protesting death,
or that every breath was either hard labor or hard time,
or that I’m either always too hot or too cold
it doesn’t matter because my hospital roommate wears star wars pajamas,
and he’s nine years old
His name is Louis

and I don’t have to ask what he’s got, the bald head with the skin and bones frame speaks volumes. The Gameboy and feather pillow blooms like they’re trying to make him feel at home ‘cause he’s gonna be here a while I manage a smile the first time I see him and it feels like the biggest lie I’ve ever told. so I hold my breath ‘cause I’m thinking any minute now he’s gonna call me on it I hold my breath ‘cause I’m scared of a fifty seven pound boy hooked to a machine, because he’s been watching me, and maybe I’ve got him pegged all wrong, like

maybe he’s bionic or something. so I look away.

like I just made eye contact with a gang member who’s got a rap sheet the length of a lecture on dumb mistakes politicians have made. I look away like he’s gonna give me my life back the minute I’ve got something to trade, I nearly pull out my pack and say

Cigarette?

but my fear subsides in the moment I realize Louis is all about show and tell. he’s got everything
from a shot gun shell to a crow’s foot and he can put them all in context like:
See, this is from a shooting range and
see, this is from a weird girl

I watch his hands curl around a cuff link and a tie tack and realize that every nick knack is a treasure and every treasure’s got a story and every time I think I can’t handle more he hits me with another story. says:

See, this is from my father. see, this is from my brother. see, this is from that weird girl. see this is from my mother. it took me two days to figure out that

that weird girl, is his sister.

took him about two hours today after she left for him to figure out he missed her.

they visit every day and stay well past visiting hours. because for them that term doesn’t apply. but when they do leave Louis and I are left alone and he says the worst part about being sick is you get all the free ice cream you ask for. and he says the worst part about that is realizing that there’s

nothing more they can do for you. he says:

Ice Cream can’t make everything ok.

and there’s no easy way of asking and I already know what he’s gonna say, but maybe he just needs to say it so I ask him any way. Are you scared? Louis doesn’t even lower his voice when he says

“Hell” yeah.

I listen to a nine year old boy say the word *Hell*, like he was a thirty year old man with a nose bleed being lowered into a shark tank, he’s got a right to it and if it takes this kid a curse word to help him get through it, I want to teach him to swear like the devil was sitting there taking notes with a pen and a pad but before I can forget that Louis is nine years old he says:

please don’t tell my dad.

he asks me if I believe in angels,

and before I realize I don’t have the heart to tell him, I tell him Not lately, and I just lay there waiting for him to hate me. but he doesn’t know how to, so he never does.

Louis loves like a man who lived in a time before God gave religion to men and left it to them to figure out what hate was.

He never greets me with silence. only smiles. and a patience I’ve never seen in someone who knows they’re dying. and I’m trying so hard not to remind him, I’ll be out of here in a couple of days, taking my life for granted. and he’ll still be planted in this bed like a flower that refuses to grow, I’ve been with him for five days and all I really know is Louis loves to pull feathers out of his pillow, and watch them float to the ground, almost as if he was the philosopher inside of the scientist ready to say that its gravity that’s been getting us down. but the truth is

there’s not enough miracles to go around kid,

and there’s too many people petitioning God for the winning lotto ticket. and for every answered prayer there’s a cricket with arthritis, and the only reason we can’t find answers is the search party didn’t invite us, and Louis right now the crickets have arthritis

so there is no music. no symphony of nature swelling to crescendos, as if we bent halo’s into melodies that could keep rhythm with the way our hearts beat.

so we must meet silence with the same level of noise that the parents of dying nine year old boys make when they take liberties in talking with heaven. we must shout until we shatter in our own vibrations then let our lives

echo, and grow echo, and grow echo, and grow

Grow distant.

grow distant enough to know that as far as our efforts go we don’t always get a reply. but I swear to whatever God I can find in the time I have left I’m gonna remember you kid. gonna tell your story as often as every story you told me, and every time I tell it I’ll say see, there’s bravery in this world

there’s 6.5 billion people curled up like fists protesting death, but every breath we take has to be given back, a nine year old boy taught me that.

so hold your breath. the same way you’d hold a pen when writing thank you letters on your skin to every tree that gave you that breath to hold.

then let it go. as if you understand something about getting old and having to give back because what is your night worth without a story to tell, and why wield a word like worth if you’ve got nothing to sell. people drop pennies down a wishing well as if the cost of a desire is equal to that of a thought. but if you’ve got expectations expect others have bought your exact same dream for the price of the hard work, hang in, hold on mentality, like I accept any challenge so challenge me like

I’ve brought a knife to this gun fight, the other night I mugged a mountain so bring that . . . I’ve had practice.

Louis and I cracked this world wide open and found the prize inside because we never lied to ourselves, never told ourselves it would be easy or undemanding. so we sing in our own vibration and dare angels to eavesdrop and stop midflight to pluck feathers from their wings and write demands on God’s hands

I don’t often believe in angels, but on the day I left, Louis pulled a feather from his pillow and said this is for you,

I half expected him to say See, this is the first one I grew.
```

---

## IC-0017: Encouraging Kelly

- Title: Encouraging Kelly
- Author (byline): Seema Renee Gertsen
- Work: Chicken Soup for the Teacher's Soul
- Publisher: Health Communications, Inc.
- Publication date as stated: April 2002
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: TEACHER, ASSISTANT, MOTHER
- Teaser before the introduction: No
- Spoken words (computed): 1151
- Already set (do not supply): none

### Source block (context only)

```text
Author: Seema Renee Gertsen
Book: Chicken Soup for the Teacher's Soul
ISBN: 978-1558749788
Publisher: Health Communications, Inc.
Date (Month/Year): April 2002
```

### Introduction (context only: never use it for content warnings)

```text
What makes some children special? Perhaps they have a physical or mental handicap; But does that condition warrant that these children be treated differently than other children? The answer is really quite simple. There should be no difference in the way we treat or acknowledge them. Special children laugh and cry and savor and hurt just like other children.... In this selection, a first year teacher learns this very valuable lesson in the process of

Encouraging Kelly by Seema Renee Gertsen.
```

### Performance text (classify this)

```text
TEACHER: It was my very first teaching job, and I was anxious to make an excellent first impression. I had been hired to lead a vibrant group of four-year-olds. As the parents escorted children into the room, I attempted to deal with crying kids, teary-eyed moms and tense dads. Finally, I managed to seat the kids on the carpet and we were ready to start our "morning circle time."

We were in the middle of a rousing rendition of "Old McDonald" when the door opened and a mysterious woman entered the room. She stood next to the door quietly observing the children and me. My voice and smile never faltered, but quite frankly I was very nervous. Who is this woman? Why is she here? What exactly is she observing? When I looked up again she was gone.

The day went relatively smoothly, but by the time the last child was picked up, I was physically and emotionally drained. I longed for a nonfat latte, some Chopin and a bubble bath. Then my director came in and asked to meet with me before I left for the day.

My heart raced. Did this have anything to do with the woman who had observed my class? Did I choose the wrong songs? Was the circle time too long? Too short? By the time I reached the office, I was an emotional wreck. I sat perched on the edge of my seat and waited for the axe to fall. My director told me the woman who had visited my room earlier was a potential parent to the school and was concerned about how her daughter would function in a regular classroom. Her little girl was born with a birth defect that required she wear leg braces from the knees down. The child was ambulatory but walked very slowly with a lopsided gait. She would need to be carried out to the yard and back to the classroom. Her balance was poor, and she had a tendency to topple over if she was jostled, even slightly. We would need to remind the other children to be careful when walking near her so they wouldn't accidentally cause her to fall.

The director asked me how I felt about her becoming a member of my group. I was speechless. Here I was wondering if I could possibly survive a school year with fifteen of the liveliest four-year-olds in North America, and now I was being asked to take on a child with special needs? I replied that I would accept the child on a trial basis.

That night I couldn't fall asleep. I tossed and turned until morning, then drove to work with my stomach in knots. We were all gathered on the carpet for our morning circle when the door opened and the woman walked in carrying her daughter. She introduced herself as Kelly's mommy and she gingerly sat her daughter down on the edge of the carpet. Most of the children knew Kelly from synagogue and greeted her with warm, affectionate hugs. I looked at Kelly and she looked at me. (To Kelly on her level) Welcome to our room, Kelly. We are so excited that you will be a member of our group.

The first day went really well; Kelly only fell over twice. After several days of carrying her to and from the yard, I thought, Why not encourage her to walk down the hallway a little by herself? I asked Kelly if she would like to try it, and she became very excited. The next day I sent the class out to the yard with my two assistants, and Kelly began her first journey down the hallway. She walked all the way to the next classroom, a total of ten feet. We were both thrilled! But my assistants were aghast that I was encouraging this poor child to walk. They pleaded with me to carry her outside and seat her on the bench so she could watch the other children run and play.

ASSISTANT: It would be so much easier.

TEACHER: But Kelly was persistent and eager to give it her best shot. And so we began the strenuous task of walking daily down the hall. I winced when Kelly teetered precariously too far to the right, but she just giggled and told me not to worry, she was perfectly fine. I began to cherish our quiet moments alone in the hallway, my arms outstretched to help her regain her balance. Kelly always grinned and told me she had never felt better.

Each day Kelly and I continued our slow walk down the corridor. I charted her progress with little pencil marks on the wall. Every few days the pencil marks got farther and farther apart. Kelly's classmates started to notice and began cheering for her as she plodded along. After several weeks, Kelly made it all the way to the yard! She positively glowed as the children congratulated her with gentle pats on the back and warm hugs. My assistants were astonished and prepared a special snack in honor of Kelly's tremendous accomplishment.

Weeks passed and Kelly continued to walk out to the yard every single day. We rarely carried her as she became more independent.

One week in mid-December, Kelly was absent for several days. When I called her home I was told she was in Manhattan getting her annual checkup with her doctors. On Monday morning, when her mom brought her back to school, she inquired if I had been doing anything differently with Kelly. I wasn't quite sure what she meant. Then came the dreaded question

MOTHER: Have you been forcing Kelly to walk?

TEACHER: I was dumbfounded. Maybe I shouldn't have encouraged Kelly to walk to the yard every day. Maybe I had caused permanent damage to her weakened legs. Maybe Kelly would need to be in a wheelchair for the rest of her life.

I very softly told Kelly's mom that I had encouraged her to walk outside to the yard by herself. I explained that she seemed to enjoy walking independently. The mother gently lifted Kelly's dress to show me that Kelly's knee braces had been replaced with ankle braces.

MOTHER: (with tears in her eyes) Her legs have gotten more exercise in the past few months than in the past four years of her life. I don't know how to thank you for everything you have done for my daughter.

TEACHER: (hugging her) Having Kelly as a member of my group has been a privilege.

(to audience) Seventeen years later, I still think back to the first time Kelly made it down the long hallway. Whenever I have a bad day teaching and life seems too overwhelming, I think of Kelly and her exuberant smile as she painstakingly walked down that hallway. She taught me that no obstacle in life is too big to overcome. You just need to keep working at it-one step at a time.
```

---

## IC-0018: Every Brilliant Thing

- Title: Every Brilliant Thing
- Author (byline): Duncan Macmillan and Jonny Donahoe
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: 2016
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, DAD
- Teaser before the introduction: Yes
- Spoken words (computed): 1620
- Already set (do not supply): none

### Source block (context only)

```text
Author: Duncan Macmillan and Jonny Donahoe
ISBN: 978-0822235644
Publisher: Dramatists Play Service
Date (Month/Year): 2016
```

### Introduction (context only: never use it for content warnings)

```text
Every Brilliant Thing by Duncan MacMillan and Jonny Donahoe
```

### Performance text (classify this)

```text
NARRATOR: (Pg 13) The list began after her first attempt. A list of everything brilliant about
the world. Everything worth living for.
1. Ice cream.
2. Water fights.
3. Staying up past your bedtime and being allowed to watch TV.
4. The color yellow.
5. Things with stripes.
6. Rollercoasters.
7. People falling over.

All things that, at seven, I thought were really good but not necessarily things Mum would agree with. I started the list on the 9th of November...

NARRATOR: (Pg 14) Up until that day, my only experience of death was that of my dog, Sherlock Bones. He was a central part of my existence . . . [but] he was really sick and so the vet came around to put him down. (Enters the memory . . . He/she kneels and cradles Sherlock Bones in his arms) (Pg 16-17) I held Sherlock Bones, who I’d known my entire life. I held him as he died. (Strokes the dog gently) And I thought about the walk we’d had that morning. And about the smell of him in my room. His toys in the garden. His bed under the stairs. All the things that could now be thrown away. (Stares at the dog for a long moment) And he became lighter. Or heavier, I’m not sure. But different. (Exits the memory, as he/she stands)And that was my experience of death. A loved one, becoming an object . . and being taken away forever.

(Pg 17-21) (He/she sits or crouches to wait) [So] It’s the 9th of November. All the other kids had gone home long ago. Eventually, my Dad pulls up. (He/she stands and peers through the car window) Dad looked at me . . . When something bad happens, your body feels it before your brain can know what’s happening. It’s a survival mechanism. It feels like a trapdoor opening beneath you. Fight or flight or stand as still as you can. I stood very still, looking at my Dad . . . Eventually, I got into the car.

DAD: Put on your seatbelt. Cars can be dangerous because other drivers don’t always pay attention.

NARRATOR: Why?

DAD: Well, because there’s lots to think about when you’re a grown up. There are bills to pay and work to do and relationships to sustain and there’s never enough time to do it all.

NARRATOR: Why?

DAD: Because there are only twenty-four hours in a day

NARRATOR: Why?

DAD: Because . . . . I don’t know everything . . . If you were able to know everything then life would be unlivable.

NARRATOR: Why?

DAD: Because then there would be no mystery, no curiosity, no creativity, no conversation, no discovery. Nothing would be new ad we’d have no need to use our imaginations. Our imaginations are what make life bearable . . . In order to live in the present we have to be able to imagine a future that will be better than the past. Put your seatbelt on. We’re going to the hospital.

NARRATOR: Why?

DAD: Because that’s where your mother is. She hurt herself. . . she can’t see anything worth living for.

NARRATOR: At least, that’s how I like to remember it. But we actually just sat in silence The only thing he said to me was:

DAD: Your Mother’s done something stupid.

NARRATOR: I didn’t know what that meant. . . At the hospital, Mum saw me and said ‘not him.’ So I sat in the corridor (He/she sits looks around for a moment, then takes a notebook from his backpack) I don’t know exactly when I had the idea for the list, but it was here that I started to write it down. (Pg 23) 23. Danger Mouse 24. Spaghetti 25. Wearing a cape

(Pg 26-31) Mum did eventually come home from the hospital, and by that time the list was eights pages long and h ad three hundred and fourteen things on it. I left it on her pillow with the title: EVERY BRILLIANT THING. She never mentioned it to me, but I knew she’d read it because she’d corrected my spelling.

I don’t want to make it sound like my Mother was a monster or that my childhood was miserable because it wasn’t. (In a cheerful voice) We had a piano in our kitchen. We’d gather around it and sing soul songs. There’s a Ray Charles song, “Drown in My own Tears” that she sang a lot. (Sing a few lines from the song*)

313: Having a piano in the kitchen

I forgot about the list until her second attempt, just over ten years later. Dad showed up halfway through Chemistry. The same trapdoor feeling. Fight or flight. The same wordless drive to the hospital. As a teenager I dealt with it less well. The night she came home and said that if it wasn’t for the ham and pineapple pizza lining her stomach from the night before she’d be dead. And I said . . .

You took three weeks’ worth of anti-depressants, a packet of Aspirin and half a tub of antihistamines. You’re probably healthier than I am. If you’re going to kill yourself go jump off a bridge.

Rather than storm off, I sat there and was furious that she was wishing she was dead. (Long silence) And then she started to laugh. I started shaking. Have you ever had that? Where you notice that hour hands are shaking and your breaking is deeper and you realize that, I’m really upset. I must be really upset.

I couldn’t sleep that night. I started to clear out my room. Inside a box under my bed, I
found the list.
1. Ice cream
2. Water fights

The younger me had dealt with this so much better. The younger me was hopeful. Naïve, of course, but hopeful. I picked up a pen and continued where that little boy had left off. 315. The smell of old books. 316. The even numbered Star Trek films. 317. Making up after an argument.

The next morning I sat at the end of Mum’s bed and I read the list to her. She got up and left the room. Over the next few weeks I spent a lot of time talking to her back. 201. Hammocks 761. Deciding you’re not too old to climb trees.

I began leaving Post-It notes around the house . . . 575. Piglets 823. Skinny dipping.

It was my aim to reach a thousand. No repetition. Things had to be genuinely wonderful and life-affirming. Not too many material items. 992. Knowing to jangle keys at the wildlife park if you want the otters to come out. 995. Really good oranges.

It’s common for the children of suicides to blame themselves. It’s natural. 999. Sunlight However much you know that you’re not to blame, you can’t help feeling like you failed them. It’s not fair to feel this way. But it’s natural. The first week I left for university, I posted the list to my Mum. When I returned that Christmas I found it on my desk, neatly folded back in its envelope. I still don’t know whether or not she had read it. It certainly hadn’t seemed to change her outlook. That Christmas was quiet. Difficult. Dad Drove me back to university.

(Pg 34) I read up on suicide. [It’s] contagious. Every time suicide is front-page news, every time a celebrity or a character on prime-time television takes their own life there is a spike in the number of suicides. It’s called the “Werther Effect” 1006: (Pg 41) Surprises 1007: Sometimes there is a perfect song to match how you’re feeling

(Sing a few lines from the song “Drown in My own Tears” by Ray Charles*) (Pg 39) I never told anyone about my Mum. Ever. As a kid there were times when . . . I’d have nothing in my lunchbox or I wouldn’t have socks on or something and I . . . I didn’t want people to think that because my Mother was . . . I don’t know. (Pg 40-42) I have some advice for anyone who has been contemplating suicide. It’s really simple advice. It’s this: Don’t do it. Things get better. They might not always get brilliant . . . but they get better.

(He/she dances and sings a few lines from Move On Up by Curtis Mayfield*) 1008: Dancing in private 1009: Dancing in public, fearlessly

I wrote late into the night. 1010: Reading 1427: No worrying about how much money you’re spending

I wanted to get to 2000 and I kept writing as the sun came up. So much to include that my
hand cramped up. I passed
2000: Coffee . . . With . . .
2001: Films that are better than the books they’re adapted from.

I wrote new list entries every day. Pages and pages of it.
2390: People who can’t sing but either don’t know or don’t care
9995: Falling in love
9999: Staying up all night talking.

(Pg 45) Studies have shown that children with depressed mothers have a heightened reactivity to stress. It actually changes the chemistry of the brain, the fight or flight impulse. But the real risk as I perceived it . . .

253263: (Pg 47) The feeling of calm which follows the realization that, although you may be in a regrettable situation, there’s nothing you can do about it. (Pg 45) The real risk, that I’d felt my whole life, was that I would one day feel as low as my Mum had and take the same action. Because alongside the anger and incomprehension is an absolute crystal clear understanding of why someone would no longer want to continue living • (Pg 51) That horrible feeling when something is broken and can’t ever be fixed • The trapdoor swinging open • Fight or flight or stay as still as you can.

I’d been feeling like that for a long time. I found it hard to notice new [and brilliant] things . . . the list ended. It was finished. (Long pause) (Pg 54) I did talk to someone. A group. A support group. (He/she turns to the group) Hello, everyone. This is my first session. When I was younger I was much better at being happy. At feeling joy. I um . . . . I made a list. Everything that’s brilliant about the world. A present for my Mum. It’s kind of a long story . . . (He/she steps out of the group session) (Pg 56) I wasn’t around for the last time. Dad wasn’t around either. A neighbor complained about the exhaust fumes and eventually the police cut through the garage door. Hosepipe through the driver-side window. (He/she sings softly) • When the dog bites • When the bee stings • When I'm feeling sad • I simply remember my favorite things . . . And then I don't feel so bad *

31. (Pg 57) Birdsong 45. Hugging 1092. Conversation.

The list hadn’t stopped her. Hadn’t saved her. Of course it hadn’t.
```

---

## IC-0019: Fear (from Seven Signs of Life)

- Title: Fear (from Seven Signs of Life)
- Author (byline): Aoife Abbey
- Work: Sevens Signs of Life, Pgs 17-31
- Publisher: Arcade
- Publication date as stated: Oct 2019
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: AIOFE
- Teaser before the introduction: Yes
- Spoken words (computed): 2368
- Already set (do not supply): none

### Source block (context only)

```text
Author: Aoife Abbey
Book: Sevens Signs of Life, Pgs 17-31
ISBN: 978-1948924825
Publisher: Arcade
Date (Month/Year): Oct 2019
```

### Introduction (context only: never use it for content warnings)

```text
Grief. Anger. Hope. Joy . . . Fear. All emotions we expect to encounter over our lifetime. But what if this was every day? And what if your ability to manage them was the difference between life and death? For a doctor in Intensive Care this is part of the job. And the fear in the eyes of a terminally ill patient who pleads with you to not let them die can be overwhelming.

In the words of Nelson Mandela: I learned that courage was not the absence of fear, but the triumph over it ...

Fear from Seven Signs of Life by Aoife Abbey
```

### Performance text (classify this)

```text
AIOFE: (Pgs 17-31) If someone had asked me in medical school what I might be most afraid of, dead people wouldn't even have made the list. The first body I ever saw was when my grandmother died. She was laid out in her best clothes on top of her own duvet on her own bed. I remember being 11 years old and sitting on the bed beside my cousin, chatting, whilst absent-mindedly rearranging the rosary beads around her cold, dead fingers.

AIOFE: My first job as a doctor was on an elderly care ward and, for obvious reasons, it didn't take long until the issue of a dead patient presented itself. I don't think I had even considered it might be my job to 'verify' death. I entered the room alone and shut the door behind me. I approached the bedside and when I placed my stethoscope on her chest, I could hear those hollow noises that rumble inside the thorax of somebody who is dead - the sort of noises that make a newly qualified doctor think: What if they're not dead at all? What if I say they are dead, and then the family walk in the door and she moves?

Verification of death involves looking in the pupils, checking for a response to pain and stating that there is no respiratory effort, no palpable pulse and no heart sounds. I stood for the requisite 2 minutes with my stethoscope on her chest and my hand on her neck, where you would find a carotid pulse in a living person. I became convinced that she was going to open her eyes. I pictured them snapping open, her hand lurching towards my wrist, clamping shut with a strength that I knew she did not have in recent life. I let my imagination construct the whole terrifying ordeal; I couldn't stop it, and when the second-hand signaled the passing of 2 minutes, I raced out of the room, heart pounding.

I don't know if I've ever experienced undiluted fear quite like that again, though I do think that at least some of what I do requires a level of courage. And how can I call myself brave, if I cannot admit to still feeling fear?

It reminds me of something . . . In my childhood home, we had a staircase, and the first seven steps had empty spaces between the treads. As a child, I would convince myself that a hand was about to spring from one of those holes and grab my ankles. It wasn't real, I knew it wasn't, but I let myself believe it and I ran so fast up those stairs. Perhaps it is true that we create most of the fear we experience.

George Eliot said that 'we learn words by rote, but not their meaning; that must be paid for with our life-blood, and printed in the subtle fibers of our nerves'. From the first day that I started working as a doctor, I knew what a 'Do not Resuscitate' (DNR) order was. But more than 3 years into my career, I stood with a patient and a DNR order, and fear made me question everything I knew.

It was 4 a.m. and I had found myself on the way to the oncology ward to see a woman in her fifties. She was about the same age as my own mother and was very short of breath. I still recall thinking how calm and composed she was, for somebody who was struggling so obviously. I enquired if the woman had any pain. She shook her head. 'You don't have any pain in your chest? Can you slow your breathing down?' I placed my stethoscope on the patient's back and listened to her breath sounds; air moved in and out of her lungs, and they sounded clear. 'I'll be back,' I said, as I left her behind me to look at the ECG, which had been placed on the nurses' station outside. I picked up her folder and there, poking out of the front cover, was the DNR order. It had been discussed and signed just two days before, citing metastatic cancer. I remembered only in that instant that I was on the oncology ward.

The nurse called from the patient's bedside, 'You better come back in here, Doctor.' My patient lay flat on top of her bed: breathing, heart beating, but unresponsive. Seconds ticked past and I was helpless, standing there thinking that I owed her something, but she was dying so abruptly. The nurse said she would go and call her family, although the patient would probably be dead before they arrived. I couldn't bring myself just to leave this woman alone.

In that moment, time surrounded me like an army advancing: step, step, the sound of heavy boots on ground, rifles brandished with their bayonets pointed in. Was there even a minuscule chance that there was something else that could be done, beyond standing there and watching her die? For a doctor who was scared, yes, it was the right thing for me. Within seconds, I felt my patient's pulse slip away and then she was dead. Was it the right thing for my patient? I don't believe it was, entirely. The best thing would have been for me to hold her hand and be present with her for her death. That wasn't the doctor she got that night; I did not have that presence of mind, and I don't mind admitting it.

Doctors have coping strategies to explain away fear. Mostly this happens unconsciously - the goal is to micromanage it. You cannot be a rabbit in the headlights - it simply isn't helpful. As an intensive-care doctor, my patients are often afraid. In many ways, their fear becomes routine. It is something I expect, and there is a standard reassuring phrase that I have come to say: 'Don't worry, everything is going to be okay. We're all here to keep you safe.' When I call a patient's fear 'routine', it is not a value judgement, it is just part of my routine. The sort of work I do doesn't leave a lot of time to work through the origins of fear with a patient. They need something, urgently, and you are required to deliver it, urgently, whether or not they're frightened. So you find yourself focusing on reassurance: ‘. . . everything is going to be okay, we've got you.’ In practical terms, what else can you say?

I'm not sure why, but one day I tried an approach that was less paternalistic in its reassurance. The patient had been thrown through a windscreen in a car accident. He was a young male in his twenties, bleeding, a lot, and I had found myself in the position of keeping my hand pressed on his previously gushing neck-wound.

'Am I going to die?' he asked suddenly. 'We're doing absolutely everything we can to help you. I know it is hard, but I need you to try and stay calm. Louder: 'But am I going to die?' 'You've got some significant wounds; we're going to do everything we can to make sure that doesn't happen.' Now shouting: 'AM I GOING TO DIE?'

He wanted a definitive: a yes or no, and I could have chosen either, but they would both have been a lie. I had no guarantees. The reality is that some patients look at you through their terrified, dilated pupils and they want you to say it's going to be okay. In the end, either I am right and they will be okay, or I am wrong and I will live with the fact that I chose to tell them otherwise: 'Don't worry, everything is going to be okay. We're all here to keep you safe.' Was I strong enough to cope with the burden of telling patients they would be all right, when actually there was always some chance - however remote - that they might be dead. Maybe it wasn't my job to take away a patient's fear -- usually what was happening to them was frightening . . . But you go to work the next day and stare into the next set of terrified eyes. That patient's fear explodes into the moment that you share together.

I have distracted frightened children with YouTube videos and teddy bears, so that somebody can put a cannula into their hand. I have stood by an MRI machine with a claustrophobic patient while she had her whole spine scanned and massaged her feet, because it helped her get through the scan. Sometimes, though, patients hand you their fear and you can do absolutely nothing about it. There is no control; no question to be answered; no trick, no procedure to be done. That is the sort of encounter that really clings to my bones.

'I am just so frightened- everything has changed so quickly.' These were the words of ninety-three-year-old Michael. Despite the fact that macular degeneration had left him able to see only shapes and shadows, Michael still lived independently, and his mind was sharp. Unfortunately he had recently fallen at home. And, in an instant, the wheels had stopped moving; he had come to hospital and we had shown him that he was old. His poor eyesight meant that he could no longer read, and the patient next to him was in no fit state for conversation.

I found myself defending Michael in referrals. There was a roll of the eyes from some colleagues when his age slipped from my lips and it set my defensive barriers soaring up, like walls. I wanted to shout, 'Don't write my patient off!' I wanted to ask them if they knew that Michael had managed a farm for his entire life. I wanted to ask them if they knew that he had wanted to be a painter; or that his teacher had slapped him for writing with his left hand. I wanted them to know that he had told me who he was planning to vote for in the next election.

'I am just so frightened- everything has changed so quickly.' His words had imprinted themselves inside my head: he had laid his fear at my feet, and how could I not fight to keep him safe from it? But there was also a rhyme that played ominously in the background: 'All the King's horses, and all the King's men, couldn't put Michael together again.'

We had had a conversation and I'd asked if he had ever thought about what he might want at the end of his life. What did he want to happen when his heart stopped? It took courage for me to approach Michael that day. His fears were still raw in my ears, and yet we discussed CPR and the limitations of this 'treatment'. When we had finished our discussion, he stopped to think for a moment and then asked me if I thought God would mind if he just accepted death. I told him I wasn't an expert on God, but I didn't think He would.

When I consider the faces of fear that I encounter, it can be ones with less urgency that weigh most heavily. Michael's fear of becoming less able, in the context of his advancing age, was heartbreaking, and there is a human reflex, I think, to want to hand fear back to people as something else, and to reshape it. I could have smiled and said, 'Don't worry, you are going to be back on your feet before you know it', but it did not seem like the right thing to do. You try to allow a patient's fear to be present, even if you risk feeling their pain yourself.

I met Gloria when I was less than a month qualified. She was ninety years old and had been in hospital for many weeks. She was frail and had become immobile with pneumonia. It was clear that she was in the last days of her life. I remember standing by her bed one morning, when she gripped my hand suddenly and, looking at me with desperation, said, 'Please, don't let me die.' What could I do? You can't say, 'Of course you are dying, Gloria; you are ninety years old, you have been dying for weeks and I can't change that now.' I tried to explain, to soothe her, but she couldn't hear me through her anguish. As a new doctor, I don't think I expected elderly people to be frightened of dying. I guess it is just easier if they are not; easier for me, anyway.

I prescribed Gloria medications to help her death pass as comfortably and painlessly as possible, but that didn't seem helpful enough, so I called the consultant. I told him that I thought Gloria needed emotional support. The consultant suggested we should phone and invite the family in that afternoon for a conversation. With apprehension, I asked them if they had any thoughts about how Gloria was feeling. As it turned out, they had already suspected she was frightened, and they thought what would bring Gloria comfort was a chaplain. It seemed like such a straightforward and obvious answer. Why did I not think of it myself? Confronted by her fear, I had panicked because I had no medical solutions.

Gloria died that night, sooner than any of us had expected. I believe the chaplains gave her what she needed - that which I couldn't give her - and I don't think she died frightened. I like to think that Gloria's fear became something else. If you are lucky, I believe that is what happens. Your fear of death becomes an impetus to find comfort. Your fear of losing your hard-fought independence becomes the momentum you need to stand on your feet again. Your fear of becoming the reason your family must experience grief gives you the strength to seek out truths that may be painful to hear.

And the fear of standing over a patient, with their life in your hands? [That fear] becomes the push you need to know that you did your best. . . . 'Don't worry, everything is going to be okay.
```

---

## IC-0020: Fontaine

- Title: Fontaine
- Author (byline): Whoopi Goldberg
- Work: Extreme Exposure
- Publisher: Theatre Communications Group
- Publication date as stated: March 2000
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: FONTAINE
- Teaser before the introduction: Yes
- Spoken words (computed): 2178
- Already set (do not supply): none

### Source block (context only)

```text
Author: Whoopi Goldberg
Book: Extreme Exposure
ISBN: 978-1559361552
Publisher: Theatre Communications Group
Date (Month/Year): March 2000
```

### Introduction (context only: never use it for content warnings)

```text
Germany has spent much of the past 50 years in the excruciating process of dealing with the country’s national crimes. What does it mean to come to terms with the fact that your father, even if not a passionate Nazi, did nothing whatever to stop them, but watched silently as his Jewish doctor or neighbor was sent to the ghettos and ultimately the concentration camps. In this selection, a modern-day ex-junkie from the US travels to Europe for the first time and the evidence of the Jewish Holocaust leaves him/her with a new perspective on life and questioning humanity. Fontaine by Whoopi Goldberg
```

### Performance text (classify this)

```text
FONTAINE: "Around the world in eighty days. . ." (He is singing, dancing, providing percussion sounds. He breaks into a shoo-bop version of the song – See NOTE at the end of this selection for lyrics and music to this song) What's happening? (No answer.) What's happening? (No answer.) Hey look y'all, my name is Fontaine and love is my game.

FONTAINE: You know a lot of people can't handle me. I don't understand it, 'cause like, I feel like I'm a friendly person. But you know, some people's attitude really drove me out of the country a while back. No, they did. But I got the kind of gig that allows me the freedom to cruise, because I am a thief. It's the all-American, traditional gig. People always got stuff; people always want stuff; I provide a service. Checked out these bad apartments. Found me these gold-plated, digital escargot forks. Cashed them little [suckers] in, picked up the cash, went on down to JFK 'cause you know on TV they always tell ya, "Come down to pick up your ticket to Europe." So that's what I did. And I said to the dude real politely, "Hey, where's my ticket to Europe at?"

And that man looked at me like I farted on his best suit. But he wrote the ticket out. I mean, he handed it to me, you know. I took it and walked away. He come running up behind me talking about how I have ta pay for it first. I said, "What?" I mean, you really expect me to pay before I fly? I'm a business person, okay? If I have a product I want you to buy from me I'm gonna give you a taste first just so you know I stand behind my product. Because that's good business, you know? But the airlines, they don't feel like that. They get your money and get you up in the air and then they [crash the plane], you know? The dude says he gonna call the police on me. So I gave him $956 and I walked ten steps away over to this chick who is standing there looking at me like this. (Giggling, he makes a pinched, hyper-friendly face) I said, "What are you grinnin' at?" And she looks at me talking about (prissy, condescending voice), "We have a bit of a problem. Now what's happened is we've oversold this flight. Now what that means is that we have a hundred seats on the plane but we've sold tickets to three thousand people. So I guess you're not going anywhere are you?" Now I pulled [a stunt] that I'm gonna hip you to just in case you find yourself in the same position. 'Cause I got it down, in effect. I said, "Hey," I say, "I been through your pocketbook and I know where you live." And needless to say I got me a seat on the plane. That's right man. I checked my bags through. We landed in Amsterdam, and I was lucky because I had a map already, you know, tell you all the [places] to go check out. The Diamond Exchange, the Van Gogh Museum, the ballet. . . and in the middle of this long list I see this name that I think I recognize because it said The Anne Frank House. And I wonder if it's the same chick. So I said I'm gonna go check the pad out. So, like I cruise on over to the street that's described on the map, and in the middle of this block is a white brick building. Has a door and a bronze plaque to the right of it that says The Anne Frank House. So I walk in and immediately I'm hip to the fact that it's a museum. And they got a lady sitting behind the information desk and she got all these pamphlets talking about The Anne Frank House and what to do and why they there. And behind her there were all these huge pictures that look like they suspended in midair. And attached to these pictures are headphones. And the photos are of Amsterdam and Holland during the war, and the headphones give you the narration that goes with the sequence of the photographs. . . And as I was perusing the area, I noticed a small staircase leading up to a big bookcase, and I'm into books you know, I got a Ph.D. in literature from Columbia. I have an education. I got a Ph.D. I can't do anything with. So I went on up the stairs because I want to see this one book. And I pulled on this book, and when I did that, the bookcase opened up and on the other side was this whole other room. Now, wasn't nobody up there said don't go in and there weren't no signs or nothing, so I walked on in. And the first thing you see when you're cruising into this room is a row of huge windows and all the windowpanes are blacked out so there ain't no sunlight coming in. And you look at the walls that are surrounding these windows and they are covered in this kind of wallpaper, got little flowers on it. And you get up closer and you can tell at one time it was tan but now of course it's old and brown with age and water spots, and peeling off the walls in strips. And on these walls was pictures of movie stars from like, the thirties and forties-Myrna Loy, Carol Lombard-beautiful black-and-white pictures. And when I was looking at that I happened to turn my head and see the skylight and I said, "Oh my, I'm in the room where Anne Frank's family hid." And that kinda like, threw me. 'Cause this ain't something I was really on top of in terms of history. It wasn't; my forte is American history from the twenties to the present time. Now why is that hard to believe? I mean, I’m a junkie, but I’m not stupid in some respects. So like, I was checking, you know, the differences because like, here we knew what was happening, things like the Civil Rights Movement. 'Cause we was ready for that. When I say "we" I mean all the people who was involved in making civil rights happen. Because we knew, as soon as Rosa Parks did not get her [butt] up off that bus, what was coming. We knew. We wasn't quite ready for people getting blown away in cars or little girls getting blown up in churches, but we knew it was gonna be a struggle. The difference over in Europe is that the Jews wasn't ready. See, they was living and integrating into these areas as well as they could be and they thought of themselves as Germans or Austrians or whatever. And when these people changed on them, started calling them nasty names and turning them in, they turned around and said, "Well hey, we been through this kind of thing before, you know, this is gonna pass." And when they realized what was happening, it was too late. They ended up in the camps, and leaving and going into hiding. And that kinda blew me away, too, because I always thought when you went into hiding it was like moving from one apartment to another. Because everybody I ever knew who went into hiding, I knew where they were. The only people who didn't know was the police. But it was a little bit different 'cause here you get nineteen to twenty-five people in one bedroom, but they can all go outside, you know, cruise around. But these folks was stuck in this room for two years. And it wasn't like they was living. They got in there, they had twenty hours a day of non-movement. Non-movement. No noise. They sat with no sound.

(Several beats of silence.) Nerve-wracking, ain't it? Yeah, and I discovered just like you just did that I couldn't do it. See I'd had to make some noise and mess up and I realized that that was really a stupid way to do things' cause why cut off your nose to spite your face? And when that hit me so did the fact that I was in an empty room crying. I said, "No, this don't have nothing to do with me, get out." And I ran to the door, but I got stopped by a big sign that said: IN SPITE OF EVERYTHING I STILL BELIEVE PEOPLE ARE GOOD AT HEART. I said "What?" I mean, who put this up? Why would they put it in this room? I just couldn't understand it. So I copped an attitude and decided to write a letter to the author of the quote. So I got up close enough to see the author's name and my jaw dropped 'cause it said Anne Frank. And I thought, this is too childish for words! What are you talking about? You didn't even make it! And as soon as I said that it made perfect sense. Of course Anne Frank could say that, she was a child, she was a kid, and you know no matter what you do to children they always able to still see some good in it, see? 'Cause they got that ability to see the light at the end of the tunnel. I don't have it. I'm what you call jaded. And I thought, yeah, man. What can I say? And I started examining my own [life], you know. What are my day-to-day worries? Things like, Why can't I get an American Express card? Why can't I find a hairdresser to mess with my coif? These are my big day-to-day worries, but then you go into a room like this and you hold your coif and your card up against life and death and you know the true meaning of trivial pursuit. So, I decided what I was gonna do was try to adopt this philosophy somehow, this "in spite of everything. . ." because it might help me in case I got home and I caught some [idiot] in my house ripping off my stereo. Yes, I would still break their legs, but I would remember that in spite of everything this person is still good at heart and that would save their life. So I decided, and I figured that it was cool, and I needed to see the other side of that, 'cause this is only half of the story. So I took the train from Amsterdam into Germany, and going to Germany was a whole other trip 'cause I didn't go to big cities. I went to little, tiny towns, places in the Schwarzfeld which is the black forest, and me and the black forest was it. Some of these people ain't seen no black people since Hannibal. And as a matter of fact, I get off the train, I have five or six little kids running up on me biting on my arms talking about (In a German accent), "Ooh, choco-latte." And you start talking to all these people and you find out that a lot of these folks are born in these villages, raised in these villages and they gonna die in these villages. And they don't go nowhere. And people come up on you and say weird [stuff] like, "We see how, on the American documentaries, see how it is for the black people in the United States. Please to tell us how it is for you to live in the ghetto and please eat this watermelon, we got it special for you." And you know I have to say I was really surprised to discover such. . . to hear those people say watermelon kinda freaked me out. . . to discover such rampant ignorance in the world, 1983-84, especially coming from the United States where such a thing would never happen. I mean we're beyond that subject, right? Yeah, yeah. . . I said, "Oh my, I got to get home." Because I'm there with the wrong attitude, you know. 'Cause I'm walking around looking for bombed-out buildings, saying shit to people, talking about, "Why you fighting this terrible war?" Could not even see 1983. I said, "I gotta get [it] together. I’m had a lot of time to think . . . I’m one of these people, you know where if you don’t speak English don’t come up to me in the street and ask me where [stuff] is. Yeah, you the same way, right? “Yeah, go talk to somebody who know what the hell you talking about . . . come over here take my job . . . “ Yeah, well you know it's real hard to be that cold once you been the alien. See, and once you been the alien, you find out how hard it is to have to ask somebody where shit is. And you find out what it takes to be able to tell them. It don’t take nothing but a little bit of graciousness, that’s it. Just a little bit. And that coupled with everything else that happened to me kinda freaked me out. Because I realized that life is a constant thing, it's constant live and learn. I’ll never get over that.
```

---

## IC-0021: Gains and Losses

- Title: Gains and Losses
- Author (byline): Xiao Xi Zhang
- Work: Chicken Soup for the Preteen Soul
- Publisher: Health Communications, Inc.
- Publication date as stated: Oct 2000
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 810
- Already set (do not supply): none

### Source block (context only)

```text
Author: Xiao Xi Zhang
Book: Chicken Soup for the Preteen Soul
ISBN: 978-1558748002
Publisher: Health Communications, Inc.
Date (Month/Year): Oct 2000
```

### Introduction (context only: never use it for content warnings)

```text
Katherine Lambert – Scronce once said “The mind can have tremendous control of the body; very few ailments can defeat focused energy and a determined spirit.” And what can boost a determined spirit more than the prayers of her children . . . .

Please God help my mother. She is an angel here on earth to everyone who knows her. Words can't express the pride and love I have knowing that I am a part of her. She's special in so many ways, you don't have to know her very long to realize it.

In the end it’s all about Gains and Losses by Xiao Xi Zhang
```

### Performance text (classify this)

```text
Most of us have experienced unforgettable moments in our lives. The moment that I will never forget happened in my family.

For the first fifteen years of my life, I was the only child in my family. I didn’t have any siblings. Fortunately, I’ve always had my parents, who love and care about me a lot. They help solve any problem and they will do anything for me. What I’d never really thought about is that, someday, one of them could no longer be there for me.

One day, I found out that my mother was pregnant. Which was big news in my family. Everyone was excited and happy, especially me. I imagined that I would have a baby brother, and I thought about playing and having fun with him. He would have a cute face and look at me with his naïve eyes, begging me to play with him. I was expecting that day to come soon. I kept asking my mother questions about what my brother was going to look like, what he would eat and when he was going to be born.

Finally one morning, my mother went into labor and she and my father went to the hospital, while I went to school. Of course, I thought everything would be fine. After all, women have babies every day. Thus, I was hoping to see my baby brother as soon as I got to the hospital.

After school, when I went to the hospital, my brother had already been born. But my mother was still inside the operating room, while my father waited anxiously outside. After waiting for a long time, the doctor came out and told us that after my mother had given birth to my brother, they had trouble stopping the bleeding. He told us not to worry; my mother would be fine. Then, he went back into the operating room. Seconds later, lots of doctors and nurses rushed inside. My father and I were growing more anxious by the minute. Waiting was very painful for us, because we had finally realized that anything could happen and all we could do was wait.

At 7 p.m, my mother came out of surgery. She lay on the bed with an oxygen mask and an IV. Her skin was ghastly pale, and her eyes were closed.

“Mom, Mom . . . ,” I called to her, but she didn’t react. The doctor told us that if my mother survived this night, she would be fine. Then the doctors sent my mother to the intensive-care unit.

Inside the room were many instruments for checking blood pressure, pulse rate and heart rate. Standing next to the bed, I tried to talk to my mother, whether she could hear me or not.

“You have to wake up, you have things that you have not done yet . . . You have me, my father and your new-born son. You cannot just leave us . . . and you will be fine . . . trust me . . . “

I was scared to death. At that moment, I felt that I would lose my mother forever—that she was never going to come back.

Many thoughts flashed through my mind. What would life be like if the unthinkable happened—life without my mother? I could only imagine that my life would be full of darkness, sadness and hopelessness. I would lose my closest relative, my dearest friend, and I would never again have the chance to enjoy the love of my mother. Remember, during these fifteen years, my mother was always around, watching over me, no matter what. I could not imagine how I was possibly going to survive without her.

Of course I told myself that it would not happen, that she might leave me after thirty, forty, fifty or more years, but definitely not now, not yet. It was too early. I wasn’t ready to let her go.

After I slowly came back to reality, I noticed that a flood of tears was running down my cheeks.

My mother survived that night. You can imagine my great relief when she woke up the next morning. I was so excited. I gave her a big hug as I cried tears of happiness.

My mother told me that she had actually heard the words that I had said to her when she was unconscious. Three times she had almost stopped breathing, but she told herself to stay alive, for us, her family.

Later, many nurses said my mother was incredibly lucky to survive because she had lost a lot of blood. Of course, I gave them the most glorious smile which said it all.

Today, my brother is almost two years old. On the day of his birthday, I always remember this unforgettable event in my life. I remember that I’m a really lucky person, with great parents and a wonderful little brother.
```

---

## IC-0022: Get Up, Stand Up - Station 19 (Season 4, Episode 12)

- Title: Get Up, Stand Up - Station 19 (Season 4, Episode 12)
- Author (byline): Krista Vernoff
- Work: Not specified
- Publisher: TV Show Transcripts.ourboard.org
- Publication date as stated: Aired April 22, 2021
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BEN, DR. LEWIS, VIC, SULLIVAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1264
- Already set (do not supply): none

### Source block (context only)

```text
Author: Krista Vernoff with contributions from Station 19’s writing/support staff and cast
ISBN: N/A
Publisher: TV Show Transcripts.ourboard.org
Date (Month/Year): Aired April 22, 2021
Full Transcript can be found at
https://tvshowtranscripts.ourboard.org/viewtopic.php?f=847&t=43548
```

### Introduction (context only: never use it for content warnings)

```text
Eight minutes and 46 seconds. That's how long a white Minneapolis police officer knelt on George Floyd's neck, while he was handcuffed and face down on the pavement, screaming out that he couldn't breathe. Floyd's murder on May 25, 2020 sparked a renewed effort against police brutality and systemic racism.

In April 2021, ABC’s Station 19 aired an episode hailed as one of the most powerful reflections of George Floyd’s murder on television. In this selection we hear the raw emotions of 3 of Station 19’s black first responders as they work through their fear, anger and grief with Counselor Dr. Diane Lewis.

Get Up, Stand Up by Krista Vernoff with contributions from Station 19’s writing/support staff and cast.
```

### Performance text (classify this)

```text
To be performed by a black actor

Characters:

Diane Lewis: In the wake of national outcry after the murder of George Floyd, Captain Maya Bishop brings in Dr. Lewis to grief counsel the team.

Ben Warren: Previously a surgical resident and anesthesiologist. He is the first to seek out counseling with Diana and opens up about his fears and the struggles of raising black sons in the current political climate.

Victoria Hughes (Vic): A young mixed-race firefighter struggling to deal with Floyd’s death and the media coverage. She struggles to understand how people (white people) didn’t know that racism is still problematic.

Robert Sullivan: Trying to cope with the realization that police brutality and systemic racism won’t go away if no one speaks out.

BEN: (Enters, he is exhausted) How do you do it? I mean, how do you. . . I-I-I know you have to be as shaken up as I am, so how do you. . .

DR. LEWIS: How do I do my job? You fought a fire this morning. How did you do it?

BEN: I pushed my pain aside and did what had to be done. (long beat) I feel like a hypocrite. (long beat) When the police made me lie down on the street like an animal during a routine traffic stop. . . I didn't do much of anything at all. I did yell, you know, whi. . . which was . . . Yeah. I have two kids.

Anyway, m-my wife and I, we . . . We gave "the talk" and explained that young Black men don't get to behave any old way they want when dealing with the police. We told them to do whatever it took to get home safe. But when I had a run-in with the police myself, I . . . I-I yelled at that officer as he got into his car. I mean, if my boys had yelled at a cop like that, I... I'd be upset! I'd . . . (Sighs) But I'd also be proud. . . Because they'd be right. You know, I was right. But y-you can't do that. You can't yell at a cop because, you know, w. . . Because they've got a gun, you know? They're given authority. They have the power t. . . (Sighs) D-Do you have kids?

DR. LEWIS: Three teenagers.

BEN: Oh, wow. Okay, so, you get just how frustrating and infuriating it is to pour every ounce of energy and brain power you have into them to. . . To try and mold them into confident young men. . . To make them honestly believe that they can accomplish anything, to. . . to work so hard to get them to s-stand tall and feel good in their own skin. . . Only to then have to tell them that because of the color of that skin, they have to shrink when in the presence of a police officer.

DR. LEWIS: Do you tell them that? Do you tell them to shrink?

BEN: No. No, I. . . I don't tell them to shrink. I. . . (Sighs) I tell them to stand with dignity, and I tell them to de-escalate. I-I tell them that in any confrontational situation, their job is to de-escalate. But it should be the cop's job.

DR. LEWIS: You're right. It should. (Clears throat) So, let me just make sure I have this straight. You're mad at yourself that you didn't do more after that cop treated you that way, and you're mad at yourself that you didn't do less after that cop treated you that way.

BEN: Look. . . I'm exhausted, you know? (Stammers) I'm exhausted by navigating a. . . a w. . . a world that sees me and. . . And my kids as a threat. I mean, it's. . . it's this. . . It's this constant nagging worry that. . . That never goes away. And i-if I do manage to forget and just. . . You know, just exist. . . a comment or a look or the news that a man has been killed in the street reminds me that I have to be careful. And. . . And it steals all of my mental and emotional energy that I should be giving to my wife and my kids. (long beat) Being Black in America is a life-threatening condition. ****** Scene ******

VIC: (Enters and paces in frustration) (Sighs) I like to fix things. I see a fire and I put it out. But we have been having this same fight for so long. . . For so long. I mean, my grandma used to tell me about the sit-ins and boycotts she used to do in the '60s. And we're how many moments and movements and marches later, and what do we have to show for it? And to see so many people act like this is news. . . Like this is just some brand-new information they're just now waking up to. Do you know how many white friends texted me or emailed me just out of the blue? (Laughs) Right? And everything under this guise of just checking in and just asking how I was doing. "How are you feeling?" (Laughs) I knew they meant well, but I also knew what was behind it. . . guilt. So, I. . . Pbht. I don't know, how am I feeling? (long beat) Yeah. Yeah. T-T-The spin already afoot by usual suspects in the media trying to vilify him rather than the murder of him. You kn. . . You know what's almost equally as enraging to me, too? It's the people patting themselves on the back trying to humanize him. It's like, you're trying to humanize a person. (Exhales sharply) Do you really have to look for proof that we're people, too? (Scoffs) Really? We should care more about him because he was a. . . A good father or a loving brother or a high-school athlete or he's fun at a party? No, we. . . we should care about him because he was a person. (Voice breaking) George Floyd shouldn't have been treated this way because he's a person. A cop. . . should not have had his knee on his neck until the last gasp of life was choked out of him, because he is a person. ****** Scene ******

SULLIVAN: (Enters – he is visibly angry) (Sighs) This one was different. This wasn't just another video of an innocent Black man being shot by police. This wasn't an officer making a split-second decision that resulted in another Black man losing his life. This wasn't fight-or-flight or panic-induced impulse or unconscious bias or unnecessary escalation. This was the murder of an unarmed, defenseless, compliant Black man in the middle of the street in broad daylight. Right in front of our eyes. . . All of our eyes. And, you know, white people are finally realizing that we aren't hysterical or beating a dead horse. They saw that white woman in Central Park casually use a racist police system as a weapon, and they're starting to understand that all of it renders us Black people terrorized. Hunted. Exhausted by everyday life. And, you know, I'm tired. I'm. . . And I'm mad, and I'm sad. And I'm tired for having to explain why I'm mad and sad. I'm mad because I have to take a magic pause every time I'm being tracked by eyeballs in a store. Or when people who are in life-threatening danger choose to take their chances by themselves rather than being rescued by a Black firefighter. (Scoffs) But, you know, mostly, I'm scared. I'm scared. Because no matter how tired I am, how mad I get, how sad I get, there's nothing I can say to change their minds. There's nothing I can do that will make them see me as a hardworking professional. A loving husband. Or just a man. There's nothing that prevents something like this from happening to me. Nothing.

(Sighs) I'm scared because I am eight minutes away from being another George Floyd. I’ve had so many dark thoughts. Sometimes, I doubt my own... my own goodness.
```

---

## IC-0023: The Glass

- Title: The Glass
- Author (byline): Eric Bogosian
- Work: Pounding Nails in the Floor With My Forehead
- Publisher: Theatre Communications Group
- Publication date as stated: Nov 1994
- Event as filed: Dramatic Interpretation
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

## IC-0024: Here Come Da Judge from The Shack

- Title: Here Come Da Judge from The Shack
- Author (byline): William Paul Young
- Work: The Shack
- Publisher: Windblown Media
- Publication date as stated: July 2007
- Event as filed: Dramatic Interpretation
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
Our story begins with Mackenzie "Mack" Phillips, a father suffering great pain because of the death of his young daughter at the hands of a serial killer. Mack receives a note from "Papa" to meet him at the rundown shack in the woods where police had found evidence of his daughter’s murder six years earlier. Mack, who was raised by a hypocritical, vicious and abusive father who was also a pastor, already understands from previous experience that "Papa" is God. The following scene occurs midway through the book after Mack has already met: (in the character of Papa) Papa -- a large beaming African-American woman; (in the character of Jesus) Jesus -- a Middle Eastern man dressed as a laborer; (in the character of the Holy Spirit) And the Holy Spirit -- a woman of Asian ethnicity. It is the Holy Spirit who walks Mack through “The Judgment”

Here Come Da Judge from The Shack by William Paul Young
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

WOMAN: But it's a start, isn't it, Mackenzie? And you didn't move beyond your father's inability on your own, it was God and you together who changed you to love this way. And now you love your children much the way Father loves his. (Mack’s anger rises, he tries to cover his emotions, but he is clearly angry) Hmmmmm.

Something I said bother you, Mackenzie? (pause) Mackenzie? Is there something you would like to say?

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

---

## IC-0025: How to Say It

- Title: How to Say It
- Author (byline): Beth Stillman
- Work: The Moth Presents Occasional Magic (Pg 77-80)
- Publisher: Crown/Archetype
- Publication date as stated: Mar 2019
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SPEAKER
- Teaser before the introduction: Yes
- Spoken words (computed): 1038
- Already set (do not supply): none

### Source block (context only)

```text
Author: Beth Stillman
Book: The Moth Presents Occasional Magic (Pg 77-80)
ISBN: 978-1101904428
Publisher: Crown/Archetype
Date (Month/Year): Mar 2019
```

### Introduction (context only: never use it for content warnings)

```text
Every patient death is a different situation; but for health care professionals, one thing is for certain: Telling someone their loved one has died is never easy. How to Say It by Beth Stillman.
```

### Performance text (classify this)

```text
SPEAKER: (Pg 77-80) “I’m sorry. He's dead. We did everything we could."
Is he breathing? Is he bleeding? Is his heart beating?
“I’m sorry. He's dead. We did everything we could."
He’s dead . . . he’s dead . . . he’s dead.

SPEAKER: I know what happens after you die. I take your family into a quiet room, with Kleenex, and then I say the word "dead." Not "expired" (because you are a person, not milk), and not "passed on," because families always want to believe that means I just transferred you to another hospital.

Dead.

I have to say it.

That's basically all they taught us about how to deliver bad news in medical school. A one-hour lecture.

So we learned by watching our teaching physicians. We were their constant companions in this sort of theater of the bereaved, lurking in doorways and at bedsides and the hospital's ER, waiting to see how soft they made their voices. When did they touch someone on the shoulder? How much medical jargon did they use before getting to the word "dead"?

When you train to become a doctor, they don't really teach you about death. They teach you how to prevent it, how to fight it, how to say it, but not how to face it.

So on one of my first nights as a teaching physician in the emergency room, as we work on the body of a sixteen-year-old boy with eight bullet holes in his chest and abdomen, we are almost angry at his body for not responding to our efforts.

Is he breathing? Is he bleeding? Is his heart beating?

I go to the head of the bed, and I hook him up to a respirator that breathes for him.

We put tubes ... everywhere. A large-bore IV goes into each arm, an even larger one into his groin, and through that we start pressure-bagging type-0-negative blood, trying to replace what he's lost. I call for another unit of blood, but no matter how fast we work, we can't work fast enough.

The monitor begins to sound this shrill insect whine meant to alert us that the patient is crashing, which we already know, so it feels less like a warning and more like a rebuke.

Then we lose his blood pressure and his pulse. But he's sixteen.

So I perform a trauma Hail Mary. I grab a ten-blade scalpel and make a deep incision from the nipple all the way down to the bed. I take the scissors and cut through the intercostal muscles. I take the rib spreaders, push them between the ribs, and crank his chest open.

There's a giant gush of blood and then a moment of stillness, like the second after a lightning strike. Even his blood smells metallic, like ozone.

I reach my hands into his chest, and I put them around his still heart. I begin pumping it for him, feeling for damage. I slide my fingers down the length of his aorta, but it is so riddled with holes that the frayed pieces disintegrate in my hands.

The first time I had to be the one to break that news to a family, I was in my second year of residency. I remember I had to do it in the patient's room, because his adult daughter refused to leave his bedside.

I said, “I’m sorry. He's dead. We did everything we could."

And then I was supposed to step out of the room, give her a few moments alone. But I was paralyzed, rooted to the spot by a sense of failure and loss. When I looked at the bed, I couldn't stop imagining my own father lying in it.

My attending physician must have seen what was going on in my face, because she grabbed me by the arm and she dragged me outside.

She said, "Don't you ever do that again. Don't you EVER pretend that grief belongs to you when it doesn't. One day the person you love will be in that bed. But today you say you're sorry, you mean it. Then you have to walk away."

I look up from the sixteen-year-old boy and see that my own audience has formed. They wait to see what I will do next.

I realize that in front of me is a gaping hole, and the boy's family will probably be here very soon, so I turn to the surgery resident, and I say, "Listen, you have to get this kid closed up as fast as you can."

Not ten minutes go by when we hear the sound of a woman demanding to be let in.

We are not ready.

We are shoving tubes and gauze and surgical supplies into giant trash bags. Security is trying to keep her out, but she is a tsunamic force. We barely had this boy closed up and half covered with a sheet when I see her standing in the doorway.

Clearly his mother. And she goes absolutely quiet. “I’m sorry. He's dead. We did everything we could."

She takes a running leap toward the body. The nurse at the head of the bed sees a large needle still attached to the sutures holding him together and plucks it off the table just before his mother lands on top of his body, trying to protect it with her own.

She starts keening. It's a terrible sound.

I repeat, “I’m sorry. He's dead. We did everything we could."

She slides off his body. I see her touch the boy's fingers to her mouth briefly before holding them against her cheek. I leave the room as soon as the social worker enters, motioning for everybody to follow me out.

I think, That's what they can learn from watching me: how to walk away. And without a moment's break, I go to see the next patient. Because there are forty people in the waiting room who all want immediate attention, and they can't know that I still feel the dead boy's heart in my hands like an anchor.

But I know that if I don't put it down now, I might never remember that this loss doesn't belong to me.

One day that grief will be mine. But not tonight.
```

---

## IC-0026: I Never Knew

- Title: I Never Knew
- Author (byline): Rosanne Martorella
- Work: Chicken Soup for the Teenage Soul on Tough Stuff
- Publisher: Health Communications
- Publication date as stated: Oct 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1453
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rosanne Martorella
Book: Chicken Soup for the Teenage Soul on Tough Stuff
ISBN: 978-1558749429
Publisher: Health Communications
Date (Month/Year): Oct 2001
```

### Introduction (context only: never use it for content warnings)

```text
According to a 2020 study by the American Academy of Child and Adolescent Psychology, approximately 1 in every 4 girls and 1 in every 13 boys in the US experience sexual abuse at some time in their childhood. Because no child is prepared to cope with the repeated pain and fear of sexual abuse, victims have a higher chance of developing depression, PTSD, and drug addictions. For some, like Cindy, the pain and despair are simply too much to bear. I Never Knew by Rosanne Martorella
```

### Performance text (classify this)

```text
She was my best friend and I loved her. She was the coolest girl in junior high and everyone wanted to be like her…and she chose me to be her best friend. Her name was Cindy. She was beautiful with her black hair and tall, thin body. While the rest of us in eighth and ninth grade were still looking amorphous, trying to take shape, Cindy was already beautifully poised in her adult body.

Her mother had died when she was a little girl. She was an only child and she lived alone with her father. By the time we would get home from school every day, he would already be at work. He wouldn't come home until two or three in the morning, so we had free reign of the house. No parental supervision was the greatest thing we could ask for as teenagers. Her house was a big, two-story that was concealed by a large grove of orange trees. You couldn't see the house from the street, and we liked it that way. It added to the mystique and allure that we were always trying to create.

At school she was pretty much the center of attention. One whole corner of the quad was dedicated to Cindy and her "followers." If there was new music, clothes, hairstyles or even new ways to take notes or study, you could be fairly sure that it came out of that corner of the quad. Even the school faculty caught on to the power this girl held, and convinced her to run for class president. Cindy and I were voted in as class president and vice president by a landslide.

By day we were the acting liaison between students and faculty, by night we hosted social activities at Cindy's house. If we weren't having a party, people would come just to hang out anyway. Kids would be there for all kinds of reasons - to talk about relationships, their parents, to do their homework, or just because they knew someone they liked would be showing up.

After everyone left, I would usually spend the night. My mom wouldn't like it very much if it was a school night. Sometimes Cindy would come back to my house to spend the night, but my mom didn't like that much either because we would stay up all night laughing and talking. Cindy didn't like to be home alone.

That following summer, after I came home from vacation with my family, things were starting to change. Cindy looked thinner than usual with dark circles under her eyes, and she had started to smoke. The strikingly beautiful girl looked pale and gaunt. She said she missed me a lot. While it was a boost to my ego, I couldn't believe it could be entirely true. After all, there were always people trying to be close to her and get into her circle of friends.

My solution: two weeks at the beach. Our parents pitched in to rent a beach house in Ventura for two weeks. My mom would be the only supervision. In Cindy's inimitable style, we collected a group of beach friends within a couple of days. We'd all hang out at this local café during the day, when we were not in the water or on the sand, and at night we'd hang out around this fire pit on the beach.

Cindy started to look like her old self, but better. She was tan. She looked great in a bikini and all the guys on the beach wanted to be around her. But she was still smoking. She told me it calmed her nerves.

One night, Cindy came back to the beach house very late. She was all disoriented and noticeably excited. She told me she and this one guy had been drinking and smoking marijuana, and they had gotten together. She said that I had to try marijuana because it made everything better, clearer, in fact. She said she really liked this guy and wanted to run away with him. I knew she was just high and she'd feel differently in the morning.

When school started that next year, things weren't the same and I missed the old routine. Cindy wanted to get into different things than I wanted, and she started hanging around guys more and more. We would still hang out from time to time, but it wasn't as fun as it used to be. Cindy would get really serious and tell me that I just didn't understand how things were. I just thought that she was maturing faster emotionally than the rest of us, like she had physically.

One morning when I arrived at school, there were police cars all around and a lot of nervous activity in the halls. When I proceeded toward my locker, my counselor and another woman stopped me. I was asked to follow them to the office. My heart was pounding so fast and hard that I could hardly catch my breath. My head was racing with the different scenarios that might have caused this odd behavior.

When we all sat down in my counselor's office, the principal came in and took a seat. Was I in some kind of trouble? The principal began by prefacing the news by talking about life and maturity and circumstances. Now my head was really spinning. And then it happened. My world froze in time with the words, "…And Cindy took her own life last night using her father's gun." I couldn't talk, I couldn't move. Tears started to stream from my eyes before my heart could even comprehend the pain. She was only fifteen years old.

As the suicide note explained, her father had repeatedly sexually abused her and she knew no other way out. Months after he was arrested, he finally confessed. The note also said something else. It said that the only family she ever knew and cared about was me. She left me a ring that her mother had left to her.

I cried for weeks. How is it that I never knew? We were closer than anyone and talked about everything; how come she never told me that? I was certain that I could have helped her and I began to blame myself.

After weeks of grief counseling, I came to understand that the burden of Cindy's sexual abuse was too much for her to bear, especially when she started to become intimate with boys. The counselor explained to me that her shame was too great to even talk about, even to her best friend. It dawned on me how alone she must have felt and it suddenly became clear to me why she never wanted to spend nights alone in her own house.

My own suffering - weeks of pain and confusion - was eased greatly with all the help and support I received. Teachers, counselors, friends and family members all participated in nurturing me. It was clear to everyone that this situation was going to change my life forever, but because I let help in, it would subsequently add to my life an aspect of wisdom and compassion. I had wished that Cindy could have known the relief that comes from letting others help you with your pain.

Cindy's suicide note also requested that she be cremated. The note said that I should spread her ashes wherever I wanted to. I chose the ocean off the beach where we had spent two weeks that summer.

On the day of the memorial we rented a boat to take us out to sea. The boat was packed with friends and teachers, even though it was a rainy, overcast day. We stood on the bow and took turns sharing our experiences and love for our friend. When it came time for me to free her ashes, I was hesitant. I didn't want to turn them loose in a sea that looked dark and menacing. I thought she had had enough of that in her own life.

My hesitancy gained attention and both my mother and my counselor stepped up on the platform and put their arms around me. With their support I opened the lid and set my friend free. As some of the ashes hit the surface of the water, the sun broke through for a moment and sent beautiful rays of light that sparkled on the surface of the water. The clouds parted some more and soon the whole boat was bathed in warm sunlight. At that moment, I felt calmer than I had in weeks. Somehow I knew that the Angels had come for my friend and that she would be all right - and so would I.
```

---

## IC-0027: I’ll Tell You at Sunrise

- Title: I’ll Tell You at Sunrise
- Author (byline): Franky D. Gonzalez
- Work: Jenny Magazine, on-line Issue 013, Fall 2017
- Publisher: Jenny Magazine
- Publication date as stated: Fall 2017
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MAN, VAGABOND
- Teaser before the introduction: Yes
- Spoken words (computed): 1474
- Already set (do not supply): none

### Source block (context only)

```text
Author: Franky D. Gonzalez
Book: Jenny Magazine, on-line Issue 013, Fall 2017
https://archive.jennymag.org/fall-17-issue
ISBN: On-Line Transcript
Publisher: Jenny Magazine
Date (Month/Year): Fall 2017
```

### Introduction (context only: never use it for content warnings)

```text
*According to the CDC, the United States reported nearly 50,000 deaths by suicide in 2022 and for 2023 rates continue to rise.

So, what should you do if someone you know is in crisis or may be having thoughts of suicide? Don’t avoid the subject. It’s a myth that asking about suicide will give someone the idea to do so. And you don’t have to be an expert. You just need to show genuine care and concern.

Many professionals suggest starting a conversation with something like this:“It sounds like you’re feeling incredibly trapped, overwhelmed, sad, (pick the best adjective to describe what you are seeing). Sometimes when people feel like this, they think about suicide. Is that something you’re thinking about?”

In this selection two strangers discuss the topic of suicide. . . I’ll Tell You at Sunrise by Franky D. Gonzalez
```

### Performance text (classify this)

```text
Characters: A well-to-do man; any race or age A homeless vagabond;, any race, age or gender. Scene: A subway platform bench. Time: Present. Directional Notes: Parentheses indicate where the dialogue overlaps or is interrupted. A Beat is a change in the pacing of the conversation. A Pause is one second long. A Silence is between two and three seconds long.

MAN: (speaks in a weariness that has become emotionless) Do you understand?

VAGABOND: (has a calculating way of talking, as though choosing their words carefully) I've dug ditches before. Filling one shouldn't be hard.

MAN: I mean, you have no objections?

VAGABOND: No. I don't -- just. . . I've always been taught that when you want to help someone. If l could help you some other way (like convincing you this isn't a good idea) --

MAN: You can help by doing what I asked you to do.

VAGABOND: But that ain't really helping you. Who you helping when you bury the dead? Isn't it more helpful to save a life?

MAN: So, you do have objections.

VAGABOND: You asked for help. I'm trying to help you.

MAN: I want you to do as I asked. If you can't do it, why did you say yes?

VAGABOND: You offer someone a few thousand dollars for an hour of work, you'd be a fool not to do it. But I'm gonna try to find a better way if I can.

MAN: But you'll do what I ask?

VAGABOND: I will. But I have a condition.

MAN: What?

VAGABOND: Talk with me. Until my train comes. That's all I ask. (Silence)

MAN: You want to know why.

VAGABOND: I do. Yes. You don't have to answer. But, I mean . . . what does it matter if you're buried or not? Once you're dead, you're dead.

MAN: I have my reasons.

VAGABOND: No doubt. It's just. . . I don't understand.

MAN: You're not getting paid to understand.

VAGABOND: No. I guess not. (Silence) Whatever is going on. . . whatever it is, you can get past it. But you won't get past it ignoring your problem and dying.

MAN: I know that. I'm aware.

VAGABOND: You don't know me, so you don't gotta say jack to me. But, you got a family don't you? You got friends? Anyone that you can talk about this with? You can't get past it until you can talk about it.

MAN: Maybe I don't want to get past it.

VAGABOND: Then you wouldn't have asked for help. Every problem has a solution

MAN: I already found (my solution) --

VAGABOND: Suicide isn't a solution.

MAN: It's always a solution.

VAGABOND: What could possibly be happening that this is the solution? (Pause) If this were a solution to the problems of life, we'd all be dead.

MAN: How long until your train gets here?

VAGABOND: You're stuck with me for a few more minutes. Sorry.

MAN: I didn't mean (to imply that you were annoying me) --

VAGABOND: I know what you meant.

MAN: Either do the job, or don't, but I don't want any more questions. (Silence)

VAGABOND: No more questions. Gotcha. But I'm gonna keep talking. Till my train comes.

MAN: Why?

VAGABOND: Because I care about you.

MAN: You don't know me.

VAGABOND: But I relate.

MAN: Yeah? Really?

VAGABOND: Yes. (Silence) I -- I was going to once . . . awhile back.

MAN: Once what?

VAGABOND: End it. (Silence, then with hesitation and an attempted restraint of emotion) It was . . . buncha stupid stuff. Happening all at once. Whole thing felt hopeless. And I don't know why. I don't really remember it, but I stayed up something like two days straight when I decided that I was done. And I um . . . had this thing about falling leaves, right? I thought that it'd be kinda romantic . . . you know . . . to fall like a leaf to the ground. And the . . . the door up to my apartment's roof, right? The lock was broken. I thought it'd be really .... nice. Just floating down. I don't know what I was thinking back then. But I remember that when I finally decided I was going to kill myself, everything became so easy. You feel that, right? Like there's peace at last. . . And it sounds so stupid, but I decided that I was going to wander the city. Like a leaf floating and spinning around in the wind. And when I had nothing left in me, I'd jump from my apartment building. The last gust of wind for the leaf that couldn't fly anymore. (Pause) So, I spent all my money and walked till my legs felt like they were gonna give up. I walked back to my apartment building, right? And next to my apartment building was this Little Italy Sub Shop. And I kid you not, just when I was walking past this sub place, this guy comes out and sees me. He says, "Hey, you look hungry. Eat." And he hands me this sub and walks off.

Never see him again. And I'm not even thinking, right? I just keep going.

And I get to the last flight of steps and I'm on the roof, right? This was it -- the last thing I'd ever see. Being honest with you, everything up there looked beautiful. There is nothing like looking at the skyline the moment before you die. It's breathtaking. And I start walking to the edge of the roof and I realize, I'm carrying this 12-inch sub. So, I'm thinking, what the hell, right? I sit down, my back up against the AC unit and I watched the city. The lights like little stars. (Pause) I don't know how long I sat there, but when I stood up again, the sun was coming out. And I don't know what it was, maybe it was the sub or the skyline or maybe at the end of the day we just need to wander around for two days and spend all our money and realize that this whole thing . . . is beautiful. Life is beautiful and eventually it all works out. A sub and a skyline did that for me. Most times that's all it takes. (Silence)

MAN: Did everything work out?

VAGABOND: Well. . . I mean . . . I'm homeless now. (beat; they laugh).

MAN: You're pretty funny.

VAGABOND: Thank you

MAN: So, life doesn't get better, eh?

VAGABOND: It's hard to answer that question. I don't know what makes a better life.

MAN: You have no home. You have nothing that you can call yours.

VAGABOND: But possessions can't be what life is all about, can it? I mean we leave them behind when we die, right? What about walking around with the sun on your face? What about a kid laughing when they see a magic trick? What about skylines at dawn, or eating the best damn sub in the world? What about that first kiss with someone you love? What about looking into the eyes of a newborn? Or listening to your favorite song on the road? Or . . . or sitting in a train station trying to remind a friend that life might actually be worth living? (Silence) Talk to me. You can't want to give that all up. Life's like the seasons. Ice eventually melts and every season has its fruit you can eat. Nothing is so hopeless that

(killing yourself is the answer)

MAN: (loudly and then lowering) Enough! Please. Just. . . (Silence)

VAGABOND: I'm sorry. I didn't mean (to overstep my boundaries)

MAN: It's okay.

VAGABOND: Look, I'm not trying to be one of those bullshit self-help guides, because that stuff's fake. I just want to reach you, man. I want you to see another side to this. I'm not going to promise that things are going to get better. I'm not going to lie to you and say that it's gonna fix itself, but there's always a chance. You can't discount hope. Sure. There's a chance it might not get better. But we both know it almost always does. If not, at least it'll get tolerable. But I ain't gonna try to stop you. This is the one thing that you have absolute control over and it's not for me to take that away from you, but please. Please reconsider.

(Silence)

MAN: Go over it with me again . . . what you're gonna do tomorrow. (Silence)

VAGABOND: (sighs) I'm gonna go to the place at sunrise with two subs from Little Italy Sub Shop and stand over the hole. I'm gonna call out to you. You're gonna respond, and I pull you out.

MAN: And if l don't respond?

VAGABOND: I'm going to pull you out of that hole at sunrise and we'll eat subs before I take you home.

MAN: But if l don't respond?

VAGABOND: Some things are easier to do than to say. I'm gonna do what you asked me if it comes to that. I promise.

MAN: Let me hear it. Please.

VAGABOND: If you don't respond, I take the shovel and I bury you.

MAN: Thank you.

VAGABOND: Don't thank me. (sound of a train in the distance) That's my train coming.

MAN: (pulling out an envelope from his pocket) Here take this. Half up front.

VAGABOND: No. Tomorrow. I'll take it tomorrow.

MAN: Okay. I'll see you tomorrow. Well . . . you'll see me tomorrow.

VAGABOND: We'll see each other tomorrow, man. I know we will. (Sound of a train pulling in and opening its doors. The Vagabond stands up and offers a hand to the Man. The Man shakes it) Until tomorrow. (begins to exit)

MAN: Wait! What's your name?

VAGABOND: (turns back and chuckles) I'll tell you at sunrise. (he exits)

(The man sits alone for a moment. Silence)
CONCLUSION
If you or someone you know needs support, please call, text, or chat with the 988 Suicide &
Crisis Lifeline or visit 988lifeline.org for 24/7 access to free and confidential services.

Playwright's Note: The play's ending is left ambiguous purposefully. There is no "One Size Fits AIl" solution to suicide prevention when you're trying to talk someone out of it.
```

---

## IC-0028: Joe Egg

- Title: Joe Egg
- Author (byline): Peter Nichols
- Work: Not specified
- Publisher: Grove Press, Inc
- Publication date as stated: June 1967
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BRI, SHEILA, BR
- Teaser before the introduction: Yes
- Spoken words (computed): 1666
- Already set (do not supply): none

### Source block (context only)

```text
Author: Peter Nichols
ISBN: 978-0802151155
Publisher: Grove Press, Inc
Date (Month/Year): June 1967
```

### Introduction (context only: never use it for content warnings)

```text
How do parents come to terms with their daughter's persistent vegetative state? At first, it seems that they deal with the situation by laughing about it. However, after nearly 10 years, Bri has given up hope for his daughter and believes that her death would be a release. His wife, Sheila, believes that she will one day recover. Bri's humor is indeed his way of dealing with the trauma. But Sheila's laughter is an attempt to keep Bri happy and the marriage together. The characters of Bri and Sheila represent opposite sides of the moral argument on such cases: Do we have the right to decide whether a human being should live or die or is it cruel to artificially prolong a life that consists only of severe fits and constant pain?

Joe Egg by Peter Nichols
```

### Performance text (classify this)

```text
BRI: Sheila’s got a theory about Joe’s birth. She doesn’t blame the doctors. She blames herself.

SHEILA: I don’t say that. I say it wasn’t entirely the doctors.

BRI: Because she’d slept around

SHEILA: I think it was partly because I’d been promiscuous, yes, and my subconscious was making me shrink or withdraw from motherhood, all right!

BRI: That vicar told us it was the devil’s doing. Why don’t you believe that? It’s about as brilliant.

SHEILA: (shrugs) It comes down in the end to what you believe.

BRI: I’ll tell you what I believe.

SHEILA: I know what you believe.

BRI: (points at audience) They don’t. (To audience) I believe the doctor botched it. There was no other cause. (To Sheila) That specialist said as much, he said it had nothing at all to do with the way you’d lived or whether there was a nut in the family . . . or what kind of [cigarettes] you smoked. . .

SHEILA: He didn’t say the doctor did it either.

BRI: No. You’ve got a good point there. He didn’t mention that, quite true. He didn’t say, “Yes, he’s a shoddy midwife, my colleague, always was, I’ll see he gets struck off the register.” Very true Weakens my argument. That.

SHEILA: Oh, you’re so clever!

BRI: He’d only say for certain that it was a chance in a million it could happen again . . . It’s due to this that Joe lives at home with us.

SHEILA: She’s our daughter.

BRI: (to audience) She was on the way before we married. That feeds the furnace of guilt.

SHEILA: No need to tell them everything. (to audience) But she’s no trouble. It’s Brian. I don’t know which is the greatest baby. Watching somebody as limited as Joe over ten years, I’ve begun to feel she’s only one kind of cripple. Everybody’s damaged in some way. There’s a limit to what we can do. Brian, for instance, he goes so far – and hits the ceiling. Just can’t fly any higher. Then he drops to the floor and we get self-pity again . . . despair.

BRI: (To audience) How long do your labours last? Two, three hours? A day? Dilettantes! (Points a Sheila) Five days!

SHEILA: (To audience) This doctor kept on drugging me. (To Bri) You never thought it was going on too long?

BRI: Yes, but you leave it to them, don’t you? My mum taught me to believe in doctors.

SHEILA: The next I knew, they handed me this hairless yellow baby with forceps-scars all over her scalp. She was gorgeous. . . . But soon I began to notice these funny turns. We took her to our new G.P. (Sheila mimes holding a baby)

BRI: Baby. (Indicates mimed baby). (Points to himself) Doctor. What seems to be the trouble.

SHEILA: I don’t really know. Funny turns. Face-making. Blinking with her eyes, working with her tongue, shaking her head, then going all limp.

BRI: (tickling the baby and talking to it) Funny turns indeed at your age! Saucy beggar. We are not amused.

SHEILA: But what d’you think it is?

BRI: Gas. Have you tried Gripe Water? Let’s see what we can find in here. (Rummages in drawer, finds medicine, reads label). Ah, yes, this’ll put a stop to it.

SHEILA: Doctor – I wish you could see one of these turns.

BRI: Oh, I’ve seen them, dear. Got three of my own. Your first, is it? First baby?

SHEILA: Yes.

BRI: Well, dear, it’s like this. Take it easy, give ’em a chance. (Tickles the baby, looks again at medicine). Let’s see. Three times daily after meals. I’ve got a waiting-room full of people, dear. You try her with this and come back if there’s no improvement in – say – a week. And don’t fret, Bye-bye. . . . . Three days later

SHEILA: (urgently) Doctor –

BRI: Didn’t I say come back in a week? Why so soon?

SHEILA: She’s gone into a coma. She won’t take anything. She hasn’t fed for two days.

BRI: (Looks at baby, listens to it, claps hands by it, finally shakes it like a piggy-bank – goes humming back to the table, mimes dialing) Get me the Children’s Hospital . . . quick!

SHEILA: (turning to audience) I said to Brian, “I’ve got a feeling we shan’t bring her back.” But we did . . . eventually. I stayed in hospital with her for a few weeks, then left her there having tests. A few weeks later they called me to collect Joe from the hospital by which time we’d gathered that she wasn’t ever going to amount to much. But I was determined to know the best we could expect. And the worst. The pediatrician was German. (For this sketch, Bri uses a music-hall German accent)

BRI: Vell, mattam, zis baby off yours has now been soroughly test and ve need ze bets razzer battly so it’s better you take her home. I sink I can promise she von’t be any trouble. Keep her vell sedated you’ll hartly know she’s zere.

SHEILA: But, Doctor – can’t you tell me the results of the tests?

BRI: Vitch ones? Zere vere so many – (slight laugh. Lists on fingers) Electro-encephalopraph, scree-dimensional eggs-ray, blood urine and stool analyses, zis business vis needles in ze fontanelle –

SHEILA: Is that why her hair’s been shaved off?

BRI: Vell of course –

SHEILA: She’d only just begun to grow it. And did the needles make that scar on her head?

BRI: Ach, nein. Zis vos a liddle biopsy to take a sample of her brain tissue.

SHEILA: That’s a relief (She smiles quickly) I thought at first you bored a hole in her skull to let the devil out.

BRI: (Looks interested, confers with his assistant). Sounds gut. Did you try it? (To Sheila) My colleague says ve don’t do zat any more. (Shrugs) Pity! Vell – if you eggscuse me. (Moves to go)

SHEILA: But – Doctor, Doctor – What can she do?

BRI: Do? She can’t do nozzing at all.

SHEILA: Will she ever?

BRI: Mattam, let me try and tell you vot your daughter iss like. Do you know vot I mean ven I say your daughter vos a wegetable?

SHEILA: (Thinks for a moment, gets it, smiles) Yes! You mean “Your daughter was a vegetable.”

BRI: Ach himmel! Stil is, stil iss, always vill be! I have trouble vis Englisch werbs. Zere’s von born every eight hours, you know.

SHEILA: No, I didn’t. Is that true?

BRI: Oh, ja, ja. Not all as bas as zees case, of course –

SHEILA: Isn’t there anything at all we can do?

BR: But jawohl! You must feed her, vosh her nappies, keep her varm. Just like any ozzer mozzer.

SHEILA: But for how long?

BRI: Who can tell? Anysing can happen. You know zat. Diphtheria, pneumonia . . . vooping cough. (Breaks character) So—what happened then? We brought her home.

SHEILA: And the hospital passed the can back to our local G.P. He had to supply phenobarbitone and keep us happy. But the time came when I asked him whose fault it was.

BRI: Which is when he suggested the vicar might call.

SHEILA: Yes. Nice vicar. Sensitive. So concerned and upset at the sight of Joe – the fits were unusually bad that day – so we left her in the cot and had our chat in another room.

BRI: She’s a beautiful child. It’s tragic. Tell me – when you first – knew there was nothing to be done, how did you feel?

SHEILA: Well, of course, you find out gradually, not all at once. But there is a point when you finally accept it. And that’s – (shakes her head) Oh, very nasty. You think “why me?” I don’t know about the other mothers but I kept saying, “Why me, why us?” all day long. Then you get tired of that and you say, “Why not me?”

BRI: Tell me, what was your husband’s reaction to the child?

SHEILA: He used to say, “Think of something worse.” And of course that’s easy. Joe could have grown older and developed into a real person before it happened. Or she could have been a very intelligent spastic without the use of her limbs. Which is worse, I think, than being a kind of living parsnip.

BRI: Quote. You count your blessings . . . and that give you fortitude.

SHEILA: No, but it’s something to do. When you’re up against a – disaster of this kind – an Act of God – (Bri clears his throat) – it’s so numbing you feel you msut make some sense of it –botherwise – you’d –

BRI: Give up hope?

SHEILA: Yes. My husband doesn’t feel the need to make sense of anything. He lives with despair.

BRI: (coming out of character) Did you tell him that?

SHEILA: He says I shouldn’t look for explanations.

BRI: He doesn’t believe in God?

SHEILA: His own kind of God. A manic-depressive – He doesn’t like me praying.

BRI: You’ve been praying?

SHEILA: What else can I do? I look at that flawless little body, those glorious eyes, and I pray for some miracle to – get her started. It seems, if we only knew the key or the combination, we could get her moving. D’you think the story of Sleeping Beauty was about a spastic? (breaks out of sketch) He was a good man, kind and sincere.

BRI: He was, yes.

SHEILA: (to audience) As soon as we were admitted to the free-masonry of spastics parents, we saw she had even less character than the other children. So we began to make them for her.

BRI: Some never really suited.

SHEILA: No. Like the concert pianist dying of t.b.

BRI: I used to like the drunken bag who threw bottles at us if we didn’t fetch her gin and pip-tobacco.

SHEILA: But they were all too active. The facial expression wasn’t right. (Bri freezes – Sheila – to audience) I join in these jokes to please him. IF it helps him live the her, I can’t see the ham, can you? He hasn’t any faith she’s ever going to improve. Where I have, you see . . . I believe, even if she showed improvement, Bri wouldn’t notice. He’s dense about faith – faith isn’t believing in fairy-tales, its being in a receptive state of mind. I’m always on the look-out for some sign . . . . I think while there’s life there’s hope, don’t you? I wish he’d talk more seriously about her. I wonder if he ever imagines what she’d be like if her brain worked. I do.

BRI: Our marriage might have worked as well as most if Joe hadn’t happened. I was too young for it, that’s true, of course. I always will be. But Sheila might just have dragged me screaming into manhood. ‘Stead of which, I was one of the menagerie. She loved me as much as any goldfish or [plant]. So now it was a question of how to tell her I was leaving her. And when I went into it, I saw it wouldn’t only be about Joe, but also about my ambitions . . . . so in the end I better just creep away without a word . . . (Begins hurriedly putting various objects into his pockets, putting on coat, etc) So I’ve shaved and washed and packed a case . . . (Gets case from hall, stands near by) haven’t decided where I’m going yet.

SHEILA: I shall go on up. Will you carry Joe to her room when you come up? She’s such a lump. (Bri nods, Sheila leaves, Bri picks up his case and goes).
```

---

## IC-0029: The Kentucky Cycle

- Title: The Kentucky Cycle
- Author (byline): Robert Schenkkan
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: STAR, PATRICK
- Teaser before the introduction: Yes
- Spoken words (computed): 1031
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Schenkkan
ISBN: 0822213095
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Sixteen years before, Star was taken captive from her tribe by the brutal Michael Rowen, who severed the tendon in her heel so she couldn't run away. She has since resigned herself to life with the arrogant man.

ACTRESS: Their son, Patrick, has fallen in love with a girl on a neighboring farm, and here asks his mother for help in courting her.

TOGETHER: The Kentucky Cycle by Robert Schenkkan.

(Dusk. The front yard of the Rowen house. The original single room has been expanded. Among other additions is a simple front porch and steps. The house and yard are bare and unadorned, strictly functional. There is a pile of logs on the porch and an old axe. In the yard is a tin tub, partially filled with water. Patrick enters, cradling his rifle and a leather bag containing a pair of dead rabbits. Star limps in, carrying two wooden buckets full of water. She stops and looks at Patrick.)
```

### Performance text (classify this)

```text
Characters: Star (30s) a Cherokee woman kidnapped by Michael Rowen with the express purpose of providing him with an heir, and Patrick (16) their son. Scene: The Rowen homestead in Eastern Kentucky, 1792

STAR: Ostas hindhalid? [Good hunting?]

PATRICK: Couple of rabbits. Here, gimme those, Ma. (He throws his bag on the porch, lays his rifle down and takes the buckets from her. He pours them into the tub.)

STAR: To hi ju? [How are you?]

PATRICK: I'm fine.

STAR: It embarrasses you now to speak the language of your grandfathers?

PATRICK: No. It don't embarrass me. I just don't see the point.

STAR: Not to forget who you are, that is the point.

PATRICK: Not much danger of that around here, is there? (Beat.)

STAR: I'll bring your supper out. Cooler on the porch. (He sits. She goes in, returns with a bowl of food. She picks up the rabbits while he eats.)

PATRICK: Good.

STAR: Took you all day to get these? Losin' your touch.

PATRICK: Didn't take me all... (Before he can finish protesting, Star goes inside with the rabbits. She returns.) Most of the mornin' I sat up on the ridge.

STAR: Oh. Corn gonna plant itself this year?

PATRICK: I finished that piece on the Shilling.

STAR: Uh-huh. What's on the ridge worth a visit?

PATRICK: Nothin'. Just did me some thinkin'.

STAR: Alone? (Beat.)

PATRICK: Mostly.

STAR: I knew when that Talbert girl come sniffin' round here this morn in' you wasn't gonna get a lick of work done.

PATRICK: I planted the damn field!

STAR: Don't curse in front of your ma.

PATRICK: Don't see what you got against the Talberts. From what I hear you're a regular visitor over there. (Beat.)

STAR: What is it you hear?

PATRICK: You doctored her Pa.

STAR: His name is Joseph.

PATRICK: Joseph? Michael know about it?

STAR: What do you think?

PATRICK: I think he hears about it, he'll skin you alive.

STAR: Are you gonna tell him? (Beat.) Folks think I have the Gift for healin' and readin' dreams. Because I'm different. Because I'm Cherokee. Michael laughs, but as long as they pay, he laughs to himself. I think, why should he have all this money? Why not my son? And so, when I can, I see people secretly. Like Joseph.

PATRICK: For me?

STAR: Someday you'll want land of your own. A woman of your own.

PATRICK: Why hide it from me?

STAR: So if Michael finds out, he'll be angry only with me. (Beat. He crosses over and hugs her knees, puts his head in her lap.)

PATRICK: Do yu jiskanoqi. Skidoliga? [I am sorry. Forgive me?] (She kisses him on the top of his head, strokes his hair roughly.)

STAR: I gvkewidina. [It is forgotten.] You want this Ruth Talbert?

PATRICK: Rebecca.

STAR: Whatever. What she wants, you can give her easy enough. You don't have to marry her for that.

PATRICK: She ain't like that.

STAR: I see. Maybe she's smarter than I thought.

PATRICK: I love her.

STAR: You love her. Now. Today, you love her. But tomorrow? Next year? Chuji. Why so much hurry? Why marry her? (Beat.)

PATRICK: If I marry her, maybe her pa'd gimme that piece of bottom land next to ours. (She cuffs him.)

STAR: You are your father's son. Truly.

PATRICK: Not so's he'd notice.

STAR: I never understand this. What you two have is never enough. You work from sunrise to sunset and you can't plow all what you have now, but you want more. More land! Why?

PATRICK: It's the only thing that lasts. (Beat.)

STAR: You live like that, Chuji, you live a lonely life.

PATRICK: Somethin' different.

STAR: Everybody gotta right to some happiness, osta Chuji. You gotta right.

PATRICK: She makes me happy. Rebecca. (Beat.) You help me?

STAR: How?

PATRICK: Talk to him for me. 'Bout us. (She walks to the tub, runs her hand through the water.)

STAR: Michael don't listen to me.

PATRICK: He's comin' back. (She hesitates.)

STAR: You seen him?

PATRICK: This morn in' .

STAR: You sure?

PATRICK: Somebody was movin' thru the gap in a hurry.

STAR: Coulda been anybody.

PATRICK: Who?

STAR: When'lI he get here?

PATRICK: Tonight mebbe. Tomorrow for sure. But tonight I think.(Beat.) You could tell him... tell him that Talbert bottom land'd give us a third agin as much.

STAR: It'd give your pa a third agin as much. (She takes his bowl and starts into the house.)

PATRICK: Same thing. It's all gonna come down to me, innit?

STAR: Is it? (She sits on the porch. Patrick stares at her in confusion.)

PATRICK: What're you talkin' 'bout? STAR: I'm not sayin' nothin'. Said too much already. (Preoccupied, she absentmindedly strokes her injured leg.)

PATRICK: Your leg botherin' you a lot? (She shrugs. Looks off into the woods where Michael is.) Here. Lemme rub it for you. (He sits next to her. She hikes up her skirt and swings her leg into his lap. He begins to knead her scarred calf She leans back against a post, her eyes closed.) What'd you mean about... about the land not comin' to me. I'm his only son.

STAR: Are you?

PATRICK: What d'you mean, "Are you?" -"Is it?" You know somethin' why don't you just say it, 'stead of dancin' around!

STAR: Lower.

PATRICK: What?

STAR: Rub lower. (He does so.) What does Michael do in Louisville?

PATRICK: I don't know.

STAR: Home come?

PATRICK: 'Cause I ain't never been.

STAR: How come?

PATRICK: 'Cause I gotta stay here and take care of things! (Beat.) STAR: He got a woman down there.

PATRICK: How do you know?

STAR: I seen her in a dream.

PATRICK: You seen her?

STAR: Blue eyes, corn-silk hair. She always be crossin' a muddy river in my dreams.

PATRICK: Muddy water? That's death. (She nods.) Mebbe she's dead already.

STAR: Mebbe.

PATRICK: What I care if he got some woman down there? Specially if she's dead. now.

STAR: Mebbe she had him a baby.

PATRICK: He... got him another family down there?

STAR: Why else he always got to go alone? You a growned man, Chuji. With your help, he could pack in twice as much on these trips. You ever knowed Michael to turn his back on a dollar? How come he don't take you?

PATRICK: You seen the baby in your dream?

STAR: Clear as the bottom of the Shillin'.

PATRICK: Boy or girl?

STAR: She give him a son.

PATRICK: A son!

STAR: Where does that leave you?

PATRICK: I'd still be the oldest! It'd all still come to me! That's the law!

STAR: Law? (She laughs.) Michael ever pay a whole lotta mind to the law?

PATRICK: Why wouldn't he let me have my share?

STAR: You know why.

PATRICK: Why!

STAR: 'Cause he hates you.

PATRICK: That's a lie!

STAR: Look me in the face and tell me it is! (He can't.)

PATRICK: Why? Why's he hate me? Nothin' I ever do is right. Never has been. He looks at me like I was some kinda mad dog, gonna tear somethin' precious away from him.

STAR: He's afraid of you.

PATRICK: Afraid?! Hell, Michael Rowen ain't afraid of nothin'!

STAR: Look at yourself, Chuji, look! See yourself as you really are not like that hungry dog he turns you into, the one who whines and licks the hand that beats him. You are bigger than him now. And stronger. He sees you and he feels old. He feels tired. He sees death in you. That's how you scare him, Chuji, and that's why he hates you. Because there is no forgiving that. And that's why he will never give you your rightful share of this land. Your land. Not till you bury him innit! (Beat.) Ask him. You don't believe me? Ask him for your share and see what he says.
```

---

## IC-0030: Last Requests

- Title: Last Requests
- Author (byline): Giles Smith
- Work: Speaking with the Angel
- Publisher: Riverhead Books
- Publication date as stated: Feb 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: COOK
- Teaser before the introduction: Yes
- Spoken words (computed): 1420
- Already set (do not supply): none

### Source block (context only)

```text
Author: Giles Smith
Book: Speaking with the Angel
ISBN: 978-1573228589
Publisher: Riverhead Books
Date (Month/Year): Feb 2001
```

### Introduction (context only: never use it for content warnings)

```text
According to Pew Research.org, use of the death penalty has gradually declined in the United States in recent decades. But, while state-level executions have decreased, the federal government put more prisoners to death (a total of 87) under President Donald Trump than at any point since the U.S. Supreme Court reinstated capital punishment in 1976. As of September 1, 2021, five executions by lethal injection have taken place this year in the US.

Study media reports of executions, recent or decades-old, and you’ll probably find mention of the prisoner’s last meal. Although the custom has a rich and controversial history, last meals evoke a morbid curiosity and leave many people wondering, “What would I choose as my final meal?”

This prison cook has quite a lot to say about the prisoners’ Last Requests by Giles Smith
```

### Performance text (classify this)

```text
COOK: (Pg 31-43) Pork chop – nice and thick – with sprouts, a carrot-and-swede mix, mashed potatoes and gravy. Now, that’s a proper meal. And after, fruit pie and custard or cream. A proper, home-backed pie, mind you – none of your tins and packets. Proper, wholesome food. But a lot of them, these days, they don’t want that. It’s all burgers and fries. Milkshakes, some of them. Well, that’s not a proper meal is it? Not what I call a proper, sit-down meal. With my three, every night, there was meat and vegetables and a pie afterwards, never fail. Always. Not like the kids all picky and refusing to eat. I’d crack the whip. No getting down until that bowl’s clean. Come on: chop chop, eat up, or you’ll waste away.

COOK: Steak – that’s popular. Quite a few of them ask for steak, and when the do, I try to get a nice one. I do a good steak. The problem with steak is, it’s quite a long way from the kitchen to the Row. You’ve got to go out of the canteen block then across “Y” yard and up three flights. It can take a few minutes what with the security grilles. Really, with a steak, that’s not the best thing. A steak should be out of the frying pan and onto the plate and then straight into your mouth, all hot and melty. You don’t want to wait around for a steak. They might be better off with a stew or a pie. Something which keeps its heat. I don’t think any of them think about that – though why should they? It’s not like they haven’t got plenty on their minds already, my God.

I’ve been doing it for two and a bit years now, and I suppose you get into something like a routine. There was all sorts of fuss when they brought it back. People say, we didn’t used to need it. But you’d have to say it was a more innocent world then. There wasn’t the terrorism, for one thing. Or there was, but not nearly so much of it. And you never heard about people having guns, the way you do now. And all the business with the children, when people got very worked up about. I don’t know why, as time goes by there just seems to be more wickedness generally. Like the one they sent off last night. Nineteen years old. Climbed a tree by a playground in a park and started firing. Eleven little ones he killed, and three mothers. They asked him why and he said, “I wanted to see them scared.” Well, what are you going to do with someone like that? No, on the whole, I think they had to bring it back.

Some people think they don’t deserve anything. Jean from next door, she’s said to me before, “I don’t know how you can bring yourself. Cooking a special tea for someone who’s evil.” And I know what she means, except I don’t really see it like that. I know the kind they get up there. They’ve done awful things, wicked things, it’s unimaginable what they’ve done, some of them. But even so, I think there’s human standards and you’ve got to treat them right. You’ve got to remember, they’ve been up there for months [years], some of them – sitting around, thinking about what’s coming. It’s a difficult time for them. And they don’t get any special treatment up there, day to day, far from it, just the same food as the rest which, between you and me . . . I mean, we do our best, but the budget’s tight and anyway you’re cooking for nineteen hundred. There’s not exactly going to be the personal touch, is there?

I don’t know what it must be like, to know you’re going to die. We know they’ve done wrong and we know we can’t forgive them, but at least we can give them their dignity at the end. Well, that’s how I see it. I said to Jean, “You’d want the same if it was you, Jean.”

They can have what they like, within reason, up to a maximum of three courses, with coffee or tea and a piece of confectionery if they want it. No alcohol, for obvious reasons. You’ll get the jokers, like the one who said he wanted a whole roast pig with an apple in its mouth. Or the governor’s head, one of them said he wanted. The boy in the tree wanted cauliflower cheese. Which, to be honest, I think of more as a snack than a proper supper.

There’s some that are so negative, I don’t pretend to understand. “20 Marlboro Lights, one packet of chewing gum.” A shame really, when you think what he could have had. But there’s quite a number, in actual fact, who only want cigarettes. Or bowls of cereal, even. It’s as if they’ve already given up, in a way. And you wouldn’t believe the writing on some of those forms. It’s good the wardens go through it with them first, because some of them, frankly, I wouldn’t be able to read. Big letters and small letters all jumbled. And as for spelling . . . it’s all they can do, some of them, to write their names.

I think the fact you could have anything kind of paralyses them in a way. It’s almost as if they’d be better off with a menu, a range of options, so they could choose. There was one the other week who just wanted a sandwich. They’d gone up at midday to collect the form and he was just sitting there, hadn’t written anything. He was this middle-aged man who’d killed his children, four of them, at breakfast one morning, with a rifle – for no real reason, apparently. He just got angry and that was that, and the next thing he was phoning the police and asking them to come and get him. Just a sandwich. Sad, really, but I think it’s true of a lot of them on the Row that they don’t really know their own minds by the end. I made him a cheese and pickle one, because nobody ever objects to that.

I’ve never met any of the ones I’ve done the meal for. They don’t let them in the canteen area, so I never set eyes on them. I suppose I am curious sometimes, to know what they’re like. The one who killed his children. I’d have like to try and tempt him into something more than a sandwich. Sometimes the wardens will pass something on; “He looked happy with that. “

The meal goes up at 8:00 and the executions are directly after midnight. There’s some legal reason for that, I think. But that’s four hours between the meal and the end of it and I often wonder if they get puckish again. Every now and again, you’ll send the meal up and they’ll eat it, and then the phone call comes through from the judge and they get a reprieve. All very dramatic. Well, good for them. But often it’s only temporary and, a month later, you’re cooking the same meal for them all over again. There’s one up there now who’s had his last meal five times.

I can be away by 8:30, which is plenty of time for the bus. There’s often a crowd outside when I leave. People come to the gates when there’s an execution. There’s a man with a big black parka. He’s always there. I don’t know why. It’s not like there’s anything to see. There isn’t even a clock that chimes. It just gets to be after midnight, and at that point they all go away again. So the wardens tell me. Sometimes, when I leave, there might be some banners and there might be a bit of shouting going on. But more often than not they’re just standing there quietly, like they’re waiting for something, I’ve no idea what.

Last night was odd, though. I hadn’t quite managed to get the monthly freezer check done during the day, so after they’d taken up the cauliflower cheese for the boy in the tree, I finished the job off. I’d got my coat on when Dave came back with the tray. [He] didn’t say anything, just put it down and turned away and I got a good look then and I wished I hadn’t because, do you know what, he hadn’t touched it.
```

---

## IC-0031: Life Support

- Title: Life Support
- Author (byline): Stephanie Summerville
- Work: The Moth, Pg 358-365
- Publisher: Hachette Books
- Publication date as stated: Sept 2013
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1423
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephanie Summerville
Book: The Moth, Pg 358-365
ISBN: 978-1401311117
Publisher: Hachette Books
Date (Month/Year): Sept 2013
```

### Introduction (context only: never use it for content warnings)

```text
In the US, health care workers take an oath to treat all patients equally, but that’s not always the case. According to numerous studies, members of the Black community experience more illness, worse outcomes and premature death compared to their white counterparts. In addition to disparities in income, housing and education, inherent racial bias also occurs in our healthcare system. That racial bias—whether conscious or not—can lead to prejudicial behavior.

And while we have made tremendous progress from the days of the Civil War, we still have work to do; to eliminate these disparities and to discover that regardless of the color of our skin, we are human and deserve grace.

Life Support by Stephanie Summerfield.
```

### Performance text (classify this)

```text
NOTE: Narrator should be African American

NARRATOR: (Pg 358-365) It was the 1980s and I finally got up the nerve to look for a job. I got excited because the new thing was to have home health-care aides -- people who would sit with the elderly, feed them, give them their medicine and things like that. So when I opened up the newspaper and saw it, it was a hallelujah moment: Ahh! Sitter! I can do this job. What better job than just sitting? So I went to this temp agency called Health Skills. They gave me my first assignment. On the first day, I walk up to this house on cinder blocks in a working-class, all-white neighborhood. I knock on the door, and I see this woman peer out.

WOMAN: (peering through a partially open door and in blatant disgust) Go away!

NARRATOR: And so I say, "Hi, ma'am. I'm here from Health Skills. I'm here because you needed a sitter." I think that will help, but she says.

WOMAN: Go away! I don't want you here!

NARRATOR: She goes to the phone, and she calls the company! I'm standing outside and I'm waiting on her to get through this phone call, and finally she just slams down the phone, comes to the door and lets me in.

NARRATOR: So I am walking through this house. You have to walk through the living room and kitchen to get to the bedroom, so you can see all the way through the house. Well, I get to the bedroom, and I am hit with this horrible stench. The air is filled with the smell of bile, and there's this man lying on a hospital bed in an otherwise normal-looking bedroom. He has breathing tubes and IVs and he's completely unconscious. And the breathing machine is working, and it's pumping up this brown mousse out of his mouth and nose. It kind of looks like styling foam. (looking at a healthcare chart) And what I discover is that this man is dying of cirrhosis of the liver. In the final stages the liver and bile are breaking down, building up as fluid in the lungs, and the body is trying desperately to get rid of that so that he can breathe. So that's what's coming up out of his mouth and nose. Every fifteen minutes this process goes through, and I have to stand there and clean it up. So me being an overachiever and wanting to do well, I throw myself into the job. This woman who let me in is very aggressive. She doesn't say anything, but she's not very kind to me.

So we clean up this man, and there's nothing for me to do but to just wait. So I say, "Maybe I should just sit down." And this woman, she's staring at me with hate pouring from her eyes. I don't know what I've done. I've just done my job, and I've done it pretty well. So I look at her, and I say, "Look, I can get this, I'm fine now."

She turns around, doesn't say a word to me, and walks right back down that hallway and sits on the couch. And even though she's sitting across from the TV, she's sitting in profile so she can see down the hallway, and she's staring at me -- she's got her eye on me.

I sit down, and I'm looking around the room, and it's filled with this nice Shaker furniture, and it's got a floor-to-ceiling Confederate flag behind the man's bed.

And I have to tell you, it takes a little while for the gears to kick in. I'm taking in the furniture -- there's a lovely armoire, and I'm so Martha Stewart, I'm into decorating and everything. And they have a little coat tree, and on the coat tree there's this beautiful robe. Kind of like a church robe except it's white, and it has a round circle with a white cross on it and a hood. But I'm still not grasping what's happening because I am totally amazed by this hood and the buttonhole stitching around the eyes of the hood. I was like, You know, maybe I should take up sewing ...

And then I looked down the hallway, and the woman is still looking at me. So I thought, OK. I'm just going to sit here. And oh! There's a table and a book. Hooray!

So I'm flipping through the book, and it looks like a Bible because it's got gilt lettering on the outside, and I thought, Oh great! It's a Bible! I know that! Corinthians, Ephesians; Proverbs for wisdom, Psalms if you're sad. So I'm trying to look for something peaceful and happy to read, and instead I come across this horrible-looking manifesto that talks about the superiority of the white race and how we need to annihilate everyone but them for their own safety. And I shut the book.

And it finally hits me that I am in the home of an honest-to-Ggod Klansman, and I am black. And I look down the hallway at this woman, and she's looking back at me like, Do you get this now? And I'm like, Oh shit!

And then right at this moment, the mousse starts coming up out of this man's mouth and nose again, and I think, Thank God! I've got something to do, I've got something to do!

So I run over to this man, and I'm cleaning him up, very calm and professional - - cleaning, cleaning! But inside my mind, I'm like, Oh my God! I'm so glad he's not conscious, he probably hates me and, you know, I don't hate him personally, but my people hate him. And I'm feeling all this anxiety, and then I think, You cannot do this right now because you need a job, OK? You do not have time for a Rosa Parks moment. You have to get through this. OK? I'm an overachiever. I can do this. I am not going to let a little racism stand in my way. I am going to get this done, I am going to do it well, I am going to get an A+, I am going to get a check, and I am going to get the *hell* out of here, OK!?!

And that is exactly what I did. I did it every fifteen minutes for four hours that day. For four hours. And I came back the next day. She opened the door, and she wasn't quite as unfriendly. I guess she recognized that I was not going to kill the man. And I came back the third day -- she was so tired, and I realized that this woman was not getting any rest unless I was there to take care of him; that nobody would come to save her, or help her, which was really sad.

By the fourth day, she just came to the door and immediately lay down, and I did the job. I had to wake her up at the end of that four hours. And then on the fifth day, the temp agency called me (picks up the phone), and said, "We don't need you anymore." The man had passed away. But the lady had called to leave me a message.

She wanted me to know that I'd given him the best care that he'd had since he left the hospital, and the most peace and rest that she got was when I was there, and she wanted to thank me personally. And I thought, Man, that is amazing. And she left me a tip, which the temp agency would not let me keep.

But a few months later, I realized I really did get a tip and it was this: the knowledge that we had come together, she and I, these two incredibly desperate people in a highly charged situation. And it could have been a train wreck; it could have been a mess. But instead, we came together, and our lives touched, and in that touching we changed the trajectory of our lives just a little bit.

I'd like to think that I changed the way that she thought about people of color -- that we weren't whatever it was that those people were teaching her, and that she might reconsider her prejudices. And for myself, I got a job that I desperately needed. I had left Indiana to change the world. And I didn't; I couldn't. But I realized that even if I couldn't change the world, I could change the little piece of the world that I was in, and that was enough for me.
```

---

## IC-0032: Live to Tell

- Title: Live to Tell
- Author (byline): Lisa Gardner
- Work: Not specified
- Publisher: Bantam Books
- Publication date as stated: December 2010
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: VICTORIA, EVAN, MICHAEL
- Teaser before the introduction: Yes
- Spoken words (computed): 1164
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lisa Gardner
ISBN: 978-0553591910
Publisher: Bantam Books
Date (Month/Year): December 2010
```

### Introduction (context only: never use it for content warnings)

```text
A father is gunned down... a mother is bludgeoned to death ... by a son... a daughter... While tabloid television has brought us closer to the everyday horrors of our society, nothing still shocks as much as a child killing a parent. Such an act, though thought uncommon, is almost a daily event in the United States. Between 1977 and 1986, more than 300 parents were killed each year by their own children. In Live to Tell by Lisa Gardner we are witness to the unthinkable decisions that the parents of a seriously emotional disturbed child must make and the impacts that those decisions ultimately have on the family. Live to Tell by Lisa Gardner
```

### Performance text (classify this)

```text
VICTORIA: Please, baby. You know I love you. Please

EVAN: I’m gonna kill you. I’m gonna do it in the middle of the night. But I’ll wake you up first. I want you to know. You locked up the knives. You locked up the knives. But did you lock up all the knives? Did you, did you did you? (smiles gleefully)

VICTORIA: My gaze goes instinctively to the drying rack, contents now strewn across the kitchen floor. Had there been a knife in that rack? Had I washed one just this morning? I can’t remember, and that’s going to cost me. Something is always going to cost me.

EVAN: I will kill you quickly, with a knife. I’ll slide the blade in . . . right here (motions to his mother’s throat)

VICTORIA: I pour a couple of tablets into the palm of my hand. Slowly, I open his mouth with one finger and poke the first quick-dissolving tablet into the pouch of his cheek. His facial muscles start to relax as the drug takes effect. Ten minutes later, I have him in bed. Now in the silence of the aftermath, I admire the way his hair curves into one golden cowlick right above his left temple, the way his lips always purse slightly in his sleep, lake a baby’s. I take his hand, lax now, not hurting, not destroying and hold it in my own. And I wonder if tonight will be the night he will finally kill me.

Meet Evan, my son. He is eight years old.

[Victoria wakes up in the hospital with her ex-husband dozing in a chair by her bed-side]

VICTORIA: Evan? (panicked)

MICHAEL: How do you feel?

VICTORIA: Th-thirsty. Evan?

MICHAEL: He’s OK.

VICTORIA: Chelsea?

MICHAEL: She’s at my place, with Melinda. What do you remember? [Victoria notices the pain in her side and the bandages covering the knife wound] The knife penetrated your live. If the EMTs hadn’t gotten you here in time for emergency surgery, you would’ve died.

VICTORIA: Evan?

MICHAEL: Do you understand me, Victoria? You would’ve died.

VICTORIA: He didn’t mean to . . .

MICHAEL: [Angry] You know why I left? You know why I took Chelsea and got the hell out of our home? [Victoria shakes her head, frightened] Because I figured it was only a matter of time before I had to kill my son in order to protect my wife and daughter. And call me crazy, but I didn’t want to kill Evan. Dammit, I love him too, Victoria. I’ve always loved him, too.

Do you know what you’ve done to him? He’s eight, and now has to deal with the knowledge that he stabbed his own mother. That he nearly killed you. He’s just a kid, for Christ’s sake. How’s he supposed to handle that? With everything else going on in his messed-up head, how the hell is he ever supposed to deal with that?

I thought you’d died. I got the call, and the way the emergency room nurse was talking . . . I raced all the way here thinking you were dead. That Evan had murdered you. Then I run into the emergency room and the police have a million questions and the doctors have a million questions. I can’t even see you; you’ve already been whisked away to the operating room. And Evan’s shackled to a hospital bed. They’ve got him cuffed and everything. My son. My little boy.

I had to call Darren. I had to get legal advice for Evan. That’ where we are with things, Victoria.

VICTORIA: He didn’t mean . . . .

MICHAEL: Shut up. Just shut up. I don’t care that you’re hurt. I don’t care that you almost died. I want to hurt you worse, Victoria. I want to slap you until you realize once and for all that your denial is destroying our soon. Even did mean to hurt you. He intentionally stole that goddamn knife out of the drying rack. He cleverly slipped it inside the fabric on the underside of the sofa, where you wouldn’t find it. And he carefully retrieved it during an opportune moment, just so he could drive it through your ribs.

VICTORIA: How do you know all that? How can you possibly know?

MICHAEL: Because he told me. [Victoria is shocked] He’s broken. He answered my questions by rote. There’s no light in his eyes. He stabbed you, but he broke himself. And I don’t know if we’ll get him back. Sure this was better than institution, Vic?

VICTORIA: Did . . . did they arrest Evan?

MICHAEL: I’m sure an arrest warrant is only a matter of time. At the moment, however, given his fragile mental state, he’s been hospitalized upstairs. Turns out this medical center has a locked-down pediatric psych word on the eighth floor. Evan’s now a patient. [Victoria starts to protest]

I don’t want to hear it. I had Darren pull our divorce decree. I still have custodial rights to Evan and, given your current physical and emotional state, I’ll take you to court and demand full custody if I have to. Our son’s experienced a psychotic break. He’s upstairs and he’s gonna stay there.

VICTORIA: He’s just a child . . .

MICHAEL: Which is why it’s a pediatric ward.

VICTORIA: Bastard.

MICHAEL: I wish I’d become one sooner. Maybe then we could’ve avoided this.

VICTORIA: [whispers] I’m not a bad mom.

MICHAEL: No, you’re not a bad mom, Vic. And I’m not a bad dad, and Evan, when he’s Evan is not a bad kid. And yet, here we are.

VICTORIA: [Aside/her thoughts] There are so many things I want to tell my son. That I love him. That I still believe in him. I’m not in denial. I’ve seen the darkness in his eyes. But I’ve seen the light, too. I’ve seen all the moments that Evan got to be Evan, and I wouldn’t have missed those moments for anything.

[To Michael] You said I was lucky the EMTs got me to the hospital in time. But how did they know? Who called them?

MICHAEL: Evan. He dialed nine-one-one, told the operator he’d stabbed his mother. He said you were bleeding and needed help.

VICTORIA: He tried to save me.

MICHAEL: Maybe. Maybe not. The operator asked him what happened. You know what he said? [Victoria shakes her head, bewildered] He said the Devil made him do it. And he said the ambulance had better come quick, because the Devil wasn’t finished yet.

EVAN: [From a locked psych ward] Mommy? Mommy? I just want my mommy. I hurt her. Had the knife. Had to use it. Had to, had to. Nobody loves a boy as naughty as me. Blood is sticky. Warm. Didn’t know she’d bleed like that. I didn’t know! Mommy. Mommy. Mommy. [Change of persona – softly then growing in intensity] I will get you the next time. Next time I will carve out your heart!

VICTORIA: [Aside / to judge] You try as a parent. You love beyond reason. You fight beyond endurance. You hope beyond despair. You never think until the very last moment that it still might not be enough. No matter what, Evan is my son . . . He is eight years old.
```

---

## IC-0033: Mick Harte Was Here

- Title: Mick Harte Was Here
- Author (byline): Barbara Park
- Work: Not specified
- Publisher: Scholastic, Inc.
- Publication date as stated: Jan 1995
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR
- Teaser before the introduction: No
- Spoken words (computed): 1069
- Already set (do not supply): none

### Source block (context only)

```text
Author: Barbara Park
ISBN: 978-0590929837
Publisher: Scholastic, Inc.
Date (Month/Year): Jan 1995
```

### Introduction (context only: never use it for content warnings)

```text
When I was a kid I rode my bike all the time. I rode it all around my block and up and down my street. I rode it with my dad and brother to the local high school where we'd play a makeshift game of bike tag.

Sure, there was the occasional scare. Once I rode into a street without looking and a car had to stop quite short to avoid hitting me. My dad wasn't too thrilled about that, but nothing bad happened and it wasn't as if I was punished.

And not once, NOT ONCE, did I ever wear a bike helmet. At the time, I had some vague sense that I was invincible. Today, I look at that near miss with the car and silently shudder. I shudder, but not quite to the same extent as the speaker in

Mick Harte was Here by Barbara Park
```

### Performance text (classify this)

```text
NARRATOR: I just want to say, right off the bat that this isn’t the kind of story where you meet the main character, and you get to like him real well and then he dies at the end. I hate those kinds of stories. I don’t want to make you cry; I just want to tell you about Mick. But I thought you should know right up front that he’s not here anymore. I just thought that would be fair to you.

It was a bike accident. It was about as “accidental” as you can get, too. Like Mick wasn’t riding crazy. Or dodging in and out of traffic. And both of his hands were on the handlebars and all like that. His tire just hit a rock. And he skidded into the back of a passing truck. And that was that.

I’m only ten months older than he was. I was “planned.” Mick was a surprise. He loved it, too. Being a surprise, I mean. He was always teasing my parents about it. Telling them that even before he existed, he could outsmart two chemistry majors with birth control pills.

I remember the first big caper we pulled together, we scratched the letters F-A-R-T in the new driveway that had just been poured next to our house. It was, without a doubt, the funniest thing anyone had ever done in the entire history of the universe. But it’s amazing how a little fart in the driveway can totally lose its humor when your father sees it. He and mom stood us in front of them and made us “solemnly swear” to tell them the “complete and honest truth” about how it got there. Mick swallowed hard, took a big step forward, and told them “a monkey did it.” Then – just to make the story even more believable – Mick said the monkey’s name was Zippy. And the two of us had saved the day by chasing him “all the way back to Africa.”

You know, I’ve heard that sometimes when people you love die, you forget their voices. But I haven’t forgotten Mick’s. Not yet, anyway. I have a weird kind of memory, I think. Like I’ve never once been able to remember my parents’ anniversary in time to buy them a card. But I can still remember the exact conversation I had with Santa Claus when I was in kindergarten. He said, “Ho ho ho.” I said, “Your breath smells.” And he said, “Get down.” It wasn’t much of a chat, but the point is, it happened eight years ago and I still remember it like it was yesterday. I guess that’s why it doesn’t surprise me that I can still remember everything about the day of the accident.

See, Mick said he needed me to ride his bike home because he was going over to this kid Dillon Rigby’s house after school, but I said, “Sorry. I’ve got soccer practice after school. Plus I’ve got a ton of books to carry home tonight.” And he said, “Great, now I have to ride over there all by myself and I don’t even know where the kid lives.” And I said, “Aaah, no big deal. You’ll be fine,” and he said, “Gee, you’re really cool.” Then he just walked away. I didn’t even get to say goodbye.

I’m running sprints at soccer practice when I hear the siren. It bothers me that I’m kind of hypnotized by the sight of an ambulance. I don’t want to be one of those creeps who gawks at accident scenes. But I am, I think. Because as soon as I see the flashing red light appear over the fence, I can’t take my eyes off it. The ambulance is getting closer to the soccer field now. But instead of speeding past, it seems to be slowing down. Then it slows even more and turns the corner in front of the building. My stomach starts to churn.

I don’t like having the ambulance turn there. By now it should be speeding off to someone else’s neighborhood. A neighborhood where I don’t know anyone. Then all of a sudden, the door of the ambulance flies open and my dad comes rushing out and I close my eyes and I just wanted it not to be Mick. My dad puts his arms around me and pulls me close. Then he sort of cradles my head in his hand. Real gentle. Like I might break or something. Then in a voice so faint I could barely hear him – he whispers the words, “Mick’s gone.”

Yesterday was the official one-month anniversary of the accident. I used to think that anniversaries only celebrated happy things. But now I know that they’re just a way of measuring time. I went to soccer practice after school. I didn’t feel much like running though. The weird thing is, after practice was over, I didn’t want to leave the field. All I wanted to do was sit on the sidelines and think about Mick. Right across the field from me, a group of workmen were putting up a new set of bleachers. They were setting them in concrete. So, it was pretty clear they were going to be there for a while…but I decided to wait them out. It was almost dark when they finished. I still can’t believe no one stayed behind to guard the new sidewalk they just poured. I mean, you’ve gotta be nuts leaving wet cement unguarded at a junior high school. Especially if there’s an eighth grader sitting across the field who’s been watching you all afternoon. And I was totally calm when I did it. I walked over, bent down, and wrote, “MICK HARTE WAS HERE.” Because he was. And for twelve years and five months, my brother was one of the neatest kids you’ve ever want to meet. And I just wanted to tell you about him, that’s all. I just thought you should know.

CLOSING – AUTHOR’S NOTE

Head injury is the main cause of death in fatal bicycle crashes. Researchers tell us that if all bicyclists wore helmets, as many as one death every day and one head injury every four minutes could be prevented. I urge you, if you do not have your children wear bike helmets, please reconsider your decision. Today. Please. It’s a matter of life or death.
```

---

## IC-0034: A Monster Calls

- Title: A Monster Calls
- Author (byline): Patrick Ness
- Work: Not specified
- Publisher: Candlewick
- Publication date as stated: March 2013
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MONSTER, CONOR, MUM
- Teaser before the introduction: Yes
- Spoken words (computed): 1024
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patrick Ness
ISBN: 978-0763660659
Publisher: Candlewick
Date (Month/Year): March 2013
```

### Introduction (context only: never use it for content warnings)

```text
Elizabeth Kubler Ross created a pathway to grief with her five stages: Denial, Anger, Bargaining, Depression, Acceptance. These stages are meant to allow grief to be understood, and the sufferer to let go. When Conor O’Malley finds out his mother is dying of cancer, he lives in denial and pent-up anger. No one talks about her death -- not her, not his grandmother, not his father, and not him. Not until he is forced to face the inevitable and deal with his grief. This grief takes the form of a monster. A monster who forces him to face the truth and guides him to acceptance.

A Monster Calls by Patrick Ness
```

### Performance text (classify this)

```text
NARRATOR: (Pg 1-2) The monster showed up just after midnight. As they do. Conor was awake when it came. He’d had a nightmare. Well, not a nightmare. The nightmare. The one he’d been having a lot lately. The one with the darkness and the wind and the screaming. He’d told no one about the nightmare. Not his mum, obviously, but no one else either. What happened in the nightmare was something no one else ever needed to know. The nightmare was slipping from him, but there was something he couldn’t put his finger on, something different . . . He listened, but all he could hear was the quiet house around him. Nothing. And then something. Something he realized was the thing that had woken him. Someone was calling his name . . .

MONSTER: Conor.

MONSTER: (Pg 4) Conor.

CONOR: (heart thumping and impatient) What?

NARRATOR: A cloud moved in front of the moon, and then passed, and the moon shone again. On a yew tree. Which now stood firmly in the middle of his backyard. And here was the monster.

MONSTER: (Pg 136) The yew is a healing tree. It is the form I choose most to walk in. (Pg 137) If your mother can be healed, then the yew tree will do it.

CONOR: (Pg 30) What do you want from me?

MONSTER: (Pg 36) You will tell me the truth.

CONOR: The truth?

MONSTER: Not just any truth. Your truth. You know that your truth, the one that you hide, Conor O’Malley, is the thing you are most afraid of. For this is why you called me.

CONOR: (confused) Called you? I didn’t call you— (Pg 141) “What’s going to happen with my mum? You said you were a tree of healing. Well, I need you to heal!”

MONSTER: (Pg 172) Conor O’Malley, I did not come to heal her, I came to heal you.

CONOR: Me? I don’t need healing. My mum’s the one who’s...

NARRATOR: But he couldn’t say it. Even now he couldn’t say it. Even though he’d known it all along. Of course he did, no matter how much he’d wanted to believe it wasn’t true, he knew. But still, he couldn’t say it. Couldn’t say she was--

MONSTER: It is time, for [your truth].

NARRATOR: The mist surrounded them again. And once more, [he] was in the middle of the nightmare . . . (Pg 174-175) He recognized the clearing he was in, bordered on three sides by a dark forest; the fourth side, a cliff, flying off into further blackness. And on the cliff’s edge, his mum. (Actress assumes the character of Conor’s Mum at the edge of a cliff)

CONOR: (drops to his knees, struggling to stand; he yells) Mum! You have to get out of here!

MUM: (Turning at the sound of his voice) I’m fine, darling. There’s nothing to worry about.”

(Turns back to the cliff as if she’s heard something calling her)

CONOR: (whispering to himself) No.

NARRATOR: He pulled himself forward some more, but she was too far, too far to reach in time, and he felt so heavy-- There was a low sound from below the cliff. A rumbling, booming noise. Conor knew. It was too late. The real monster was coming. (Pg 178-181) With a roar, a cloud of burning darkness lifted two giant fists over the cliff top. They hovered in the air, over his mum as she tried to scramble back. But she was too weak, much too weak-At last, Conor could run. With a shout, he broke across the clearing, running so fast he nearly toppled over, and he threw himself toward her as the dark fists pulled her over the edge. And his hands caught hers. (Actor lunges toward his mum as he speaks this last line)

MUM: (yelling) Help me, Conor! Don’t let go!

CONOR: I won’t! I promise!

NARRATOR: The nightmare monster pulled harder, its fists straining around his mother’s body. And she began to slip from Conor’s grasp.

CONOR: No!

MUM: (screaming in terror) Please, Conor! Hold on to me!

NARRATOR: [But even as she said this, her hands] were slipping from his grasp, and she was getting heavier and heavier; The nightmare monster pulling harder and harder. He fell forward onto his chest from the weight of her. She screamed again.

CONOR: (falling forward from the weight of his mum’s grasp -- whispering) Please! Please! (he loses his grip and his mother falls; Conor screams) NO!

MONSTER: And here is the truth of Conor O’Malley. (Pg 185-189) You let her go.

CONOR: (shouting) I didn’t let her go! She fell!

MONSTER: You must tell the truth or you will never leave this nightmare. You will be trapped here alone for the rest of your life.

CONOR: (still shouting and fighting the urge to speak) I don’t know what you mean!

MONSTER: (low and threatening) You do know.

NARRATOR: And there was a sudden quiet. Because yes, Conor knew. The truth. The real truth from the nightmare.

CONOR: Please don’t make me, please don’t make me say it.

MONSTER: You let her go. You could have held on for longer, but you loosened your grip. You wanted her to go.

CONOR: NO!

MONSTER: You must speak the truth, Conor O’Malley. Say it. You must.

CONOR: I can’t.

MONSTER: You let her go. Why? Tell me WHY! Before it’s too late!

NARRATOR: A moan started in his throat, a moan that rose into a cry and then a loud wordless yell and he opened his mouth. And he spoke the truth.

CONOR: (crying out) I can’t stand it anymore! I can’t stand knowing that she’ll go! I just want it to be over! I want it to be finished! I’ve known forever that she wasn’t going to make it. And I started to think how much I wanted it to be over. How I couldn’t stand the waiting anymore. I couldn’t stand how alone it made me feel.

NARRATOR: He began to cry now, more than he thought he’d ever done. More than when he found out his mum was ill. (Pg 203) He wanted to ask the monster what was going to happen then, but he didn’t dare. Because he knew. (Actor assumes the role of Conor and pantomimes the following) [And then they were in his mother’s hospital room] (Pg 202) The monster’s hands gently but firmly guided him toward [her]. (Pg 203-205) (Conor looks down at her and takes her hand.) She opened her eyes, briefly, catching him there. Then she closed them again. But she’d seen him. And he knew it was here. He knew there really was no going back. That it was going to happen. And he knew he was going to get through it. And at last, he spoke the final and total truth . . .

CONOR: (tears falling from his eyes) I don’t want you to go.

MUM: (in a heavy voice) I know my love. I know.

CONOR: I don’t want you to go. (he leans forward and puts his arms around her, holding her)

NARRATOR: And that was all he needed to say. He could feel the monster, holding him up and letting him stand there. (Actor speaks from Actors position, still cradling Conor’s mother in his arms) He knew it would come. The moment she would slip from his grasp, no matter how tightly he held on. And by doing so, he could finally let her go.

MONSTER: (whispering) But not this moment. Not just yet.
```

---

## IC-0035: My Children! My Africa!

- Title: My Children! My Africa!
- Author (byline): Athol Fugard
- Work: Not specified
- Publisher: Theatre Communications Group
- Publication date as stated: Oct 1990
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: THAMI, ISABEL
- Teaser before the introduction: No
- Spoken words (computed): 1925
- Already set (do not supply): none

### Source block (context only)

```text
Author: Athol Fugard
ISBN: 1559360143
Publisher: Theatre Communications Group
Date (Month/Year): Oct 1990
```

### Introduction (context only: never use it for content warnings)

```text
Actor 1: When playwright Athol Fugard wrote his drama "My Children, My Africa," he did it to save his country. It was 1985. The apartheid laws that denied freedom to blacks were fueling riots, boycotts and demonstrations across South Africa. Worried that his country would never see peace, Fugard wrote the play in hopes that the polarization between blacks and whites would end.

Actor 2: Based on real events, "My Children, My Africa" tells the story of a teacher's attempt to bring understanding between two of his students. The teacher, Mr. M, arranges a debate between Isabel, a middle class white girl, and Thami, a black boy who grew up in the Coketown ghetto. Their journey toward understanding each other brings acceptance, but not without pain and tragedy along the way.

Together: My Children! My Africa! By Athol Fugard.
```

### Performance text (classify this)

```text
(THAMI waiting. ISABEL arrives.)

THAMI: Isabel.

ISABEL: (It takes her a few seconds to respond.) Hello, Thami.

THAMI: Thank you for coming.

ISABEL: (SHE is tense. Talking to him is not easy.) I wasn't going to. Let me tell you straight out that there is nothing in this world... nothing!...that I want to see less at this moment than anything or anybody from the location. But you said in your note that it was urgent, so here I am. If you've got something to say, I'll listen.

THAMI: Are you in a hurry?

ISABEL: I haven't got to be somewhere else, if that's what you mean. But if you're asking because it looks as if I would like to run away from here, from you!...very fast, then the answer is yes. But don't worry, I'll be able to control that urge for as long as you need to say what you want to.

THAMI: (Awkward in the face of Isabel's severe and unyielding attitude.) I just wanted to say goodbye.

ISABEL: Again?

THAMI: What do you mean?

ISABEL: You've already done that, Thami. Maybe you didn't use that word, but you turned your back on me and walked out of my life that last afternoon the three of us... (SHE can't finish.) How long ago was that?

THAMI: Three weeks I think.

ISABEL: So why do you want to do it again? Aren't you happy with the last time? It was so dramatic, Thami.

THAMI: (patiently.) I wanted to see you because I'm leaving the town; I'm going away for good.

ISABEL: Oh, I see. This is meant to be a "sad" goodbye is it? (SHE is on the edge.) I'm sorry if I'm hurting your feelings but I thought you wanted to see me because you had something to say about recent events in our little community... (Out of a pocket a crumpled little piece of newspaper which SHE opens with unsteady hands.) ...certain unrest related... I think that is the phrase they use...yes...here is is... (Reading.) "...unrest related incident in which according to witnesses the defenseless teacher was attacked by a group of blacks who struck him over the head with an iron rod before setting him on fire."

THAMI: Stop it, Isabel.

ISABEL: (Fighting hard for self-control.) Oh, Thami I wish I could! I've tried everything, but nothing helps. It just keeps going around and around inside my head. I've tried crying. I've tried praying! I've even tried confrontation. Ja, the day after it happened I tried to get into the location. I wanted to find the witnesses who reported it so accurately and ask them: ...why didn't you stop it! There was a police roadblock at the entrance and they wouldn't let me in. They thought I was crazy or something and "escorted" me back into the safekeeping of two now very frightened parents. There is nothing wrong with me! All I need is someone to tell me why he was killed. What madness drove those people to kill a man who had devoted his whole life to helping them. He was such a good man, Thami! He was one of the most beautiful human beings I have ever known and his death is the ugliest thing I have ever known.

THAMI: (Gives her a few seconds to calm down. Gently.) He was an informer, Isabel. Somehow or the other somebody discovered that Mr. M was an informer.

ISABEL: You mean that list of pupils taking part in the boycott? You call that informing?

THAMI: No. It was worse than that. He went to the police and gave them the names and addresses of our political action committee. All of them were arrested after his visit. They are now in detention.

ISABEL: Mr. M did that?

THAMI: Yes.

ISABEL: I don't believe it.

THAMI: It's true, Isabel.

ISABEL: No! What proof do you have?

THAMI: His own words. He told me so himself. I didn't believe it either when he was first accused, but the last time I saw him, he said it was true, that he had been to the police.

ISABEL: (Stunned disbelief.) Mr. M? A police spy? For how long?

THAMI: No. It wasn't like that. He wasn't paid or anything. He went to the police just that one time. He said he felt it was his duty.

ISABEL: What do you mean?

THAMI: Operation Qhumisa...the boycotts and strikes, the arson... you know he didn't agree with any of that. But he was also very confused about it all. I think he wished he had never done it.

ISABEL: So he went to the police just once. As a matter of conscience. That doesn't make him an "informer," Thami!

THAMI: Then what do you call somebody who gives information to the police?

ISABEL: No! You know what that word really means, the sort of person it suggests. Was Mr. M one of those? He was acting out of concern for his people...you said so yourself. He though he was doing the right thing! You don't murder a man for that!

THAMI: (Near the end of his patience.) Be careful, Isabel.

ISABEL: Of what?

THAMI: The words you use.

ISABEL: Oh? Which one don't you like? Murder? What do you want me to call it... "an unrest related incident?" If you are going to call him an informer, then I am going to call his death murder!

THAMI: It was an act of self-defense.

ISABEL: By who?

THAMI: The People.

ISABEL: (Almost speechless with outrage.) What? A mad mob attacks one unarmed defenseless man and you want me to call it...

THAMI: (Abandoning all attempts at patience. HE speaks with the full authority of the anger inside him.) Stop it, Isabel! You just keep quiet now and listen to me. You're always saying you want to understand us and what it means to be black...well if you do, listen to me carefully now. I don't call it murder, and I don't call the people who did it a mad mob and yes, I do expect you to see it as an act of self-defense... listen to me!.. .blind and stupid but still self-defense.

He betrayed us and our fight for freedom. Five men are in detention because of Mr. M's visit to the police station. There have been other arrests and there will be more. Why do you think I'm running away? How were those people to know he wasn't a paid informer who had been doing it for a long time and would do it again? They were defending themselves against what they thought was a terrible danger to themselves. What Angela Myalatya did to them and their cause is what your laws define as treason when it is done to you and threatens the safety and security of your comfortable white world. Anybody accused of it is put on trial in your courts and if found guilty they get hanged. Many of my people have been found guilty and have been hanged. Those hangings we call murder! Try to understand, Isabel. Try to imagine what it is like to be a black person, choking inside with rage and frustration, bitterness, and then to discover that one of your own kind is a traitor, has betrayed you to those responsible for the suffering and misery of your family, of your people. What would you do? Remember there is no magistrate or court you can drag him to and demand that he be tried for that crime. There is no justice for black people in this country other than what we make for ourselves. When you judge us for what happened in front of the school four days ago just remember that you carry a share of the responsibility for it. It is your laws that have made simple, decent black people so desperate that they turn into "mad mobs."

(ISABEL has been listening and watching intently. It looks as if SHE is going to say something but SHE stops herself)

THAMI: Say it, Isabel.

ISABEL: No.

THAMI: This is your last chance. You once challenged me to be honest with you. I'm challenging you now.

ISABEL: (SHE faces him.) Where were you when it happened, Thami? (pause.) And if you were, did you try to stop them?

THAMI: Isn't there a third question, Isabel? Was I one of the mob that killed him?

ISABEL: Yes. Forgive me, Thami...please forgive me! ...But there is that question as well. Only once! Believe me, only once.. .late at night when I couldn't sleep. I couldn't believe it was there in my head, but I heard the words... "Was Thami one of the ones who did it?"

THAMI: If the police catch me, that's the question they will ask.

ISABEL: I'm asking you because... (An open, helpless gesture.) ...I'm lost! I don't know what to think or feel anymore. Help me. Please. You're the only one who can. Nobody else seems to understand that I loved him. (This final confrontation is steady and unflinching on both sides.)

THAMI: Yes, I was there. Yes, I did try to stop it. (THAMI gives Isabel the time to deal with his answer.) I knew how angry the people were. I went to warn him. If he had listened to me he would still be alive, but he wouldn't. It was almost as if he wanted it to happen. I think he hated himself very much for what he had done, Isabel. Re kept saying to me that it was all over. Re was right. There was nothing left for him. That visit to the police station had finished everything. Nobody would have ever spoken to him again or let him teach their children.

ISABEL: Oh, Thami, it is all so wrong! So stupid! That's what I can't take...the terrible stupidity of it. We needed him. All of us.

THAMI: I know.

ISABEL: Then why is he dead?

THAMI: You must stop asking these questions, Isabel. You know the answers.

ISABEL: They don't make any sense, Thami.

THAMI: I know what you are feeling. (pause.) I also loved him. Doesn't help much to say it now, I know, but I did. Because he made me angry and impatient with his "old fashioned" ideas, I didn't want to admit it. Even if I had, it wouldn't have stopped me from doing what I did, the boycott and everything, but I should have tried harder to make him understand why I was doing it. You were right to ask about that. Now...? (A helpless gesture.) You know the most terrible words in your language, Isabel? Too late. I'll never forgive myself for not trying harder with him and letting him know.. .my true feelings for him. Right until the end I tried to deny it...to him, to myself.

ISABEL: I'm sorry I...

THAMI: That's all right.

ISABEL: Are the police really looking for you?

THAMI: Yes. Some of my friends have already been detained. They're pulling in anybody they can get their hands on.

ISABEL: Where are you going? Cape Town?

THAMI: No. That's the first place they'll look. I've written to my parents telling them about everything. I'm heading north.

ISABEL: To where?

THAMI: Far, Isabel. I'm leaving the country.

ISABEL: Does that mean what I think it does?

THAMI: (Nods.) I'm going to join the movement. I want to be a fighter. I've been thinking about it for a long time. Now I know it's the right thing to do. I don't want to end up being one of the mob that killed Mr. M-but that will happen to me if I stay here.

ISABEL: Oh, Thami.

THAMI: I know I'm doing the right thing. Believe me. And you?

ISABEL: I don't know what to do with myself, Thami. All I know is that I'm frightened of losing him. Re's only been dead four days and I think I'm already starting to forget what he looked like. But the worst thing is that there's nowhere for me to go and.. .you know.. .just be near him. That's so awful. I got my father to phone the police but they said there wasn't enough left of him to justify a grave. What there was had been disposed of in a "Christian manner." So where do I go? The burnt-out ruins of the school? I couldn't face that.

THAMI: Get your father or somebody to drive you to the top of the Wapadsberg Pass. It's on the road to Craddock. It was a very special place to him. He told me that it was there where it all started, where he knew what he wanted to do with his life...being a teacher, being the Mr. M we knew. You'll be near him up there
```

---

## IC-0036: Neferti-iti

- Title: Neferti-iti
- Author (byline): Ethyl Eichelberger
- Work: Extreme Exposure: An Anthology of Solo Performance Texts from the 20th Century
- Publisher: Theatre Communications Group
- Publication date as stated: February 1999
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2349
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ethyl Eichelberger
Book: Extreme Exposure: An Anthology of Solo Performance Texts from the 20th Century
ISBN: 978-1559361552
Publisher: Theatre Communications Group
Date (Month/Year): February 1999
```

### Introduction (context only: never use it for content warnings)

```text
Nefertiti was the wife of the Egyptian Pharaoh Amenhotep IV (later Akhenaten), and mother-in-law of the Pharaoh Tutankhamun. Her name roughly translates to "the beautiful one is come". Famed throughout the ancient world for her outstanding beauty, Nefertiti remains the one of the most well known Queen of Egypt. Though Akhenaten had several wives, Queen Nefertiti was his chief wife. Nefertiti joined her husband in worship of a new religion that celebrated the power of the sun-disk Aten - a god of light. In this religion, she was a priest. Supposedly, It was only through the combined royal pair, that the full blessing of god Aten could be bestowed. May I introduce you to the woman who was . . . . . Neferti-iti by Etyhl Eichelberger.

Ancient Egypt, Eighteenth Dynasty, inside the royal sunshade of Nefert-iti. The Egyptian queen has barricaded herself inside the tomb built for her by her husband Akhenaten. Her sisters and her lover, Bek, the artist who created the queen's famed bust, pay visits, yet remains locked outside the tomb.
```

### Performance text (classify this)

```text
Thank Aten I'm a beautiful woman!
Without that I'd have nothing, no one, nor my self-respect!
(" Impassioned hormones" with a need to be expressed, a professional woman,
a serious live-er of life!)
Quel joie to be alone each day here in this lovely sunshade Akhenaten built me!
Today is different, though
All Egypt will regret!

(Laughter like the tinkling of bells is heard from offstage.)
It's lovely here
with no one telling me what to do!
No one turning my priceless uniqueness into worthless guilt!

Sometimes in this sunshade I have the distinct feeling I'm being watched, but I am alone here, you can see that!

(Knocking is heard on tomb door.)
There is a knocking at my temple door-who could it be?
I'll ignore the eager knock!
Go away, there's no one here! (Listens at door.)
I won't go back to Memphis-I won't! You can't make me!

Scarcity is valued, so value me--
I've made myself scarce!
I'll keep right on praying to Aten, thank you.
I'm too old to change! Time is running out!
There just aren't enough hours in the day to worship all those other gods again!
Besides, I've sworn my Ka to Aten, the one and only God,
the god whose golden rays come streaming down to give me life!

(Knocking is again heard on tomb door.) Go 'way!
No not Osiris;
I won't let my beautiful body be shriveled into a dried-up image of Osiris
Give me life, give me the globe, Aten;
I have no need to be preserved forever,
when I'm dead and gone they'll not forget me!
"She passed like a meteor, leaving the world astonished and amazed!" (Knocking on door
continues.)
Stop that pounding and send for Bek-
Have him make a bust of me, then carve my thoughts beneath it.

And for Aten's sake make sure he carves my cartouche right this time; there is only one uraeus, not two!

My dear, if Bek paid as much attention to his work as he did to his diet, something would
get done around here!
Tell me, what good are lazy people?
Everybody has to work!
I don't mind ...
I love to work; the busier the better! Fill my life with work!
But my father is a military genius,
I've always been moderately wealthy and relatively unhappy -- could have spoiled me
rotten, but he didn't-
He cracked the whip at home and made us girls work!
"People who don't work are bums," he taught us! "Bums!"
What does he know? Who does he think he is anyway?
The father of God!
Casta diva ...
Oh, Aten, make father Ay butt out of my life!
He doesn't give me credit for anything!
I've had to claw my way to the sanctity of this sunshade!
Isis knows it hasn't been easy!
It's a lot of hard work being a queen!
And there are factions out there who don't like what I represent!
Tough noogies!

I have a right to be here!
Don't do that here!
"Don't be a queen," they say!
The kinder ones tell me that I transcend queenery-
They let me know they'll overlook my queenly failings and benignly be so gracious as to
accept me as one of them.
It's true most people would rather queens should stay under wraps, so to speak!
Hide!
Deny your feminine soul!
Being a queen frightens them!
But I am a queen, a beautiful one, at that!
I know who I am!
Ms. Marcia and I share the same madnessI have seen it in a dream!
If my soul were to present itself to me within a miraculous vision,
I would have that soul emblazoned on my back for all the world to see! (Knocking on tomb
door starts again.)
Quit pounding on that door!
You're giving me a headache.
I don't care if the Hittites are coming I won't come out!
Oh, go on, I'm not afraid!
They wouldn't dare come in here! I am safe here!
This is a magic place!
Aten will protect me ...
(More knocking on tomb door is heard.) What light, lovely knocking now!
Mut-Nodjme, Honey, is that you, my sweet little sister?
No, Dear-heart, I shan't come out again
I've decided to refuge myself in here forever.
Oooeee, what is that awful stench?
Mut, Honey, have you got those stinking dwarves with you again?
I don't care if the Mitannia emperor did give them to you, do you have to take them
everywhere you go?
I will not shut up! I don't care if I hurt their little feelings!
Let them hang around your sunshade!
Mut-Nodjme, don't go away mad!
Mut-Nodjme!
Gone!
Have a pleasant voyage back to Memphis!
I'll miss you, light of my life!
She's such a sweet girl -ambitious-
But she's nice, my little Nodjme!

Whoever followed me about and aped my ways!
Will I never ever see happy Mut-Nodjme?
She'll remember me kindly all her days!
I'm hot!
The Aten's globe has risen to its zenith! Now is the time to pray! (Starts to play dulcimer
and sing-stops.)
Merytaten should be here to shake her little sistrum
while I play-ah, children!!!
What can you do with them?
All she cares for is that foolish Smenkhare and his vegetarian ways!
She'll be sorry!
Where is Meketaten now?
I miss her so! ... (pause.)
Oh, I won't let myself get started on that; not now!
This is a joyous day! I must think positive!
If Ankhesenpaten were here, she'd tell me a joke and tickle her little Neferneferura!
Ah, three lovely children have I now,
even though three lovely more have died -three daughters live while three have passed
overthree out of six-not bad,
could have been worse!
Praise be to Aten ... (plays dulcimer and sings.)
And here I sit alone-" I'm never bored!"
This must be what life is like to barren people,

disciples of Seth with never hope of having childrenactually, it's not so bad, I rather like
having no one's company but my own! (Picks up hand mirror and looks into it.)
I know who I am-
you know who I am-
and then there is the real me who grins and hides from sight!
Thank goodness I've brought clay tablets and senet games!
I'll summon Thoth and write 'til day is done!
Thoth- Thoth(No response.) and here I sit alone!
Dear Aunt Tiye once told me:
"Being alone is not the worst thing in the world!" -But, it is!!! Yes it is-
it's horrible=deplorable->
especially when the Aten begins his nightly journey beneath the Nile!
Where are my lover's arms to hold me!
Oh for pity's sake!
I hereby choose to be alone-
I renounce my children; I have no children,
I renounce my husband; I have no husband
my belief in the Aten will sustain me-
l have my beliefs in one God to guide me! (Knocking on tomb door starts again.)
Cease knocking-
I won't go back to Memphis, I won't; you can't make me!

There just aren't enough hours in the day to worship all those other godsI am a student of
the late Amenophis-son-of-Hapu who has given me the strength to fight for my
belief in Tiye, no, not "Inti," but "Aten!" (Listens at tomb door.)
Who sighs beside my door and stirs the desert's silence?
Is it you at last?
The sound of your voice awakens flowers in my heart!
Go away!
Do not tempt me!
Let me feel nothing once again!
Yes, I long to see you, hold you, give myself up to my caged desires like I did when you
first looked into my eyes-
Do I make no sense?
I never asked you to understand me
Joy was mine when you but listened!
No, it is too late-our lives got in the way!
No, no! Of course I love you!
You are the divine father, my lover, the sacred possessor of Min's phallic treasures!

Call me by my rightful name again and sing to me of happiness, make hunger fly my aching
heart!
I do not choose to hear them, Bek!
For me they do not exist!
While you stand close, all I can hear are fleet gazelle and leopards screaming when the
hounds have dragged them down!
Oh bless you, simplicity becomes you,
it is I who am pretentious-
But you will always remain in my mind
if I may use your own words: "Pretentiously unpretentious!"
All right, for Aten's sake, labels, labels, labels!
Forgive me, I've offended you again! ...
But we don't change, do we?
... Good-bye! ...
Yes, I'm telling you to go! Would you rob me of
my few remaining shreds of dignity!
Leave me, let me be! I was happy before I needed you!
No, I'm neither happy nor unhappy!
I try not to think about it anymore! I exist! ...

Of course I have survived!
There was nothing left inside me to destroy after you had had your way ...
Oh, please don't leave just yet! ...
Yes, I do remember well! It was early morning!
I was gazing out upon the azure Nile when suddenly I knew
this homely, snoring stranger lying next to me with beer upon his breath was surely the
greatest love of my life and I would live forever needing him alone!
It made me violently depressed!
Somehow I felt short-changed, tricked, cheated.
Were you what I had lived for, hoped for, longed for all my days?
Yee-gods! "What next," I thought! ...
Am I repeating myself again?
Yes, yes, of course I would do anything!
I won't go back to Memphis, I won't; you can't make me!
No, I can't come out, I give myself to God.
I no longer belong to your race!
I have given myself up to the great Aten from whom I spring each morning when the
sacred lotus blooms anew!

Sometimes I truly wish with all my might that I were a human being instead of whatever it
is I am!
I can feel, I want to be like the rest!
I have a right to some sort of life like other people.
Bek, Dear-heart, it's just not that easy!
Let myself fall in love again? With whom if not with you?
Oh, a lovely thought-
the maiden returning from the tryst with a functioning looney on her arm!
And what could I offer him, sagging flesh and swollen eyes?
Bek, Bek, you're most kind!
Yes, they'll say I was a lost woman; only my bust was found!
That splendid bust!
Do you really still have it where it was?
Bek, what must your wife think?
If only life could imitate art!
If only it were true that truth is beauty!
I can speak true!
But if truth were beauty, more girls would get their hair done at the library!
Yes, no, of course I've brought my mirror, what queen would be without one?
All right, I'll look into it once again! Yes! Is that what you have seen?
No! Must I say?
Bek, what I see couldn't turn a trick in Boy's Town!

No, I'm not being negative!
Go then, back to your wife and leave me be!
What do you need me for?
You can create alone! You are an artist!
Bek, I didn't mean it! Bek There is no key to let you in!
Please don't accuse me of being negative again!
I couldn't stand it! I am trying! I am trying!
I will be positive!
Oh, God, don't leave me again, Bek. I couldn't stand it to be alone, abandoned!
Bek, talk to me! Say something!
Bek, Almighty Aten, bring him back! Bek!
Don't leave me here to die alone!
All right, I'm through.
You have won.
I don't believe in you-
Is that what you want me to say?
I curse you, I curse the name of the Aten.
I believe in nothing.
Strike me dead if you will! I don't believe in you!
There is no chance of everlasting life!
When I am dead, my detractors will erase my face and name from every building, every
tablet, every wall!
Bek will leave my image here to crumble into dust when he goes back to Memphis!
The name of Nefert-iti will be gone forever! No one will remember who I am!
I know what will be said:
"Who is Achenchae, Nefertiti who?" "I've never heard of Akhenastae!
Who was she?"
Aten has tricked me! I believed in a calf of gold!
Hear me, Aten, I believe in you no more!
You are hateful!
You lied when in a blast of fire you told me you were coming back to get me!
You have abandoned me! I hate you! I hate you!
Oh, why have you forsaken me?
What have I said? What does it matter?
Talk is cheap in the end Where is the Kohl to stain my eyes?
Where is camel hair ground to bruise my lips?
There is no one left to help me! I must carry on alone?!
I have driven all away!
Once I had many friends and lovers, they are all gone now; life goes on

(Drinks poison. Plays dulcimer and sings "The Song of Abandon.") Give me a sign, kind Aten!

Send gentle spirits down to join my dance!
Is there no justice in the world? Must I accept what comes my way?
No! I am fighting back!
There must be some sort of justice, even in Egypt!
I demand it!
I won't be thrown out the door like yesterday's dinner to be eaten by crocodiles or
hippopotami!
I must be worth more than that, I can still learn!
Hapu's son taught me to be forever a student!
To be learned is to be trained for a world already gone, he said.
Change, change and more change!
It's happening fast-too fast!
Busy, busy, busy, but I'm never too busy to count my assets!
That's rule #1 in business and I have assets, Aten, hear me! I can work hard and long!
I can listen!
For a while, at least, I can be trusted!
I am a true friend to a few and kind to many
I can love,
I've been burned once too often! You are looking at damaged goods!

I have been abandoned! I can't find my way! Aten, do something! Help me! I beseech you!
I will not be ignored any longer!
Look at me!
Acknowledge me!
React or something
Give me a sign!
Aten! Aten! Aten!
I've had it! Hapu's son was wrong! Believe in the one true God, he said and you will have
everlasting life!

(Nefert-iti dies.)
```

---

## IC-0037: Self-Evident

- Title: Self-Evident
- Author (byline): Ani DiFranco
- Work: Ani DiFranco: Verses
- Publisher: Seven Stories Press
- Publication date as stated: Sept 2007
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1100
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ani DiFranco
Book: Ani DiFranco: Verses
ISBN: 978-1583228234
Publisher: Seven Stories Press
Date (Month/Year): Sept 2007
```

### Introduction (context only: never use it for content warnings)

```text
We hold these truths to be self evident . . . .
• Some 3000 people died in the attacks on the World Trade Center.
• Over 3000 people died in the bombing of Afghanistan.
• Unknown hundreds of immigrants have been detained and deported.
• Over 1.3 million people have joined the ranks of people in the US who are living under
the poverty line, and the nation's poverty rate is increasing for the first time in eight
years.
• A man who was not popularly elected president has declared war on the world.

And where did it all begin . . . September 11, 2001. New York City . . . Soon after the terror attacks, Ani DiFranco began a poem that she ended up calling, "Self Evident."
```

### Performance text (classify this)

```text
yes,
us people are just poems
we're 90% metaphor
with a leanness of meaning
approaching hyper-distillation
and once upon a time
we were moonshine
rushing down the throat of a giraffe
yes, rushing down the long hallway
despite what the p.a. announcement says>
yes, rushing down the long stairs
with the whiskey of eternity
fermented and distilled
to eighteen minutes
burning down our throats
down the hall
down the stairs
in a building so tall
that it will always be there
yes, it's part of a pair
there on the bow of noah's ark
the most prestigious couple
just kickin back parked
against a perfectly blue sky
on a morning beatific
in its indian summer breeze
on the day that america
fell to its knees
after strutting around for a century
without saying thank you
or please

and the shock was subsonic
and the smoke was deafening
between the setup and the punch line
cuz we were all on time for work that day
we all boarded that plane for to fly
and then while the fires were raging
we all climbed up on the windowsill
and then we all held hands
and jumped into the sky

and every borough looked up when it heard the first blast
and then every dumb action movie was summarily surpassed
and the exodus uptown by foot and motorcar
looked more like war than anything i've seen so far
so far
so far
so fierce and ingenious
a poetic specter so far gone
that every jackass newscaster was struck dumb and stumbling
over 'oh my god' and 'this is unbelievable' and on and on
and i'll tell you what, while we're at it
you can keep the pentagon
keep the propaganda
keep each and every tv
that's been trying to convince me
to participate
in some prep school punk's plan to perpetuate retribution
perpetuate retribution
even as the blue toxic smoke of our lesson in retribution
is still hanging in the air
and there's ash on our shoes
and there's ash in our hair
and there's a fine silt on every mantle
from hell's kitchen to brooklyn
and the streets are full of stories
sudden twists and near misses
and soon every open bar is crammed to the rafters
with tales of narrowly averted disasters
and the whiskey is flowin
like never before
as all over the country
folks just shake their heads
and pour

so here's a toast to all the folks who live in palestine afghanistan iraq

el salvador

here's a toast to the folks living on the pine ridge reservation under the stone cold gaze of mt. rushmore

here's a toast to all those nurses and doctors
who daily provide women with a choice
who stand down a threat the size of oklahoma city
just to listen to a young woman's voice

here's a toast to all the folks on death row right now
awaiting the executioner's guillotine
who are shackled there with dread and can only escape into their heads
to find peace in the form of a dream

cuz take away our playstations
and we are a third world nation
under the thumb of some blue blood royal son
who stole the oval office and that phony election
i mean
it don't take a weatherman
to look around and see the weather
jeb said he'd deliver florida, folks
and boy did he ever

and we hold these truths to be self evident:
#1 george w. bush is not president
#2 america is not a true democracy
#3 the media is not fooling me
cuz i am a poem heeding hyper-distillation
i've got no room for a lie so verbose
i'm looking out over my whole human family
and i'm raising my glass in a toast

here's to our last drink of fossil fuels
let us vow to get off of this sauce
shoo away the swarms of commuter planes
and find that train ticket we lost
cuz once upon a time the line followed the river
and peeked into all the backyards
and the laundry was waving
the graffiti was teasing us
from brick walls and bridges
we were rolling over ridges
through valleys
under stars
i dream of touring like duke ellington
in my own railroad car
i dream of waiting on the tall blonde wooden benches
in a grand station aglow with grace
and then standing out on the platform
and feeling the air on my face

give back the night its distant whistle
give the darkness back its soul
give the big oil companies the finger finally
and relearn how to rock-n-roll
yes, the lessons are all around us and a change is waiting there
so it's time to pick through the rubble, clean the streets
and clear the air
get our government to pull its big dick out of the sand
of someone else's desert
put it back in its pants
and quit the hypocritical chants of
freedom forever

cuz when one lone phone rang
in two thousand and one
at ten after nine
on nine one one
which is the number we all called
when that lone phone rang right off the wall
right off our desk and down the long hall
down the long stairs
in a building so tall
that the whole world turned
just to watch it fall

and while we're at it
remember the first time around?
the bomb?
the ryder truck?
the parking garage?
the princess that didn't even feel the pea?
remember joking around in our apartment on avenue D?

can you imagine how many paper coffee cups would have to change their design following a fantastical reversal of the new york skyline?!

it was a joke, of course
it was a joke
at the time
and that was just a few years ago
so let the record show

that the FBI was all over that case
that the plot was obvious and in everybody's face
and scoping that scene
religiously
the CIA
or is it KGB?
committing countless crimes against humanity
with this kind of eventuality
as its excuse
for abuse after expensive abuse
and it didn't have a clue
look, another window to see through
way up here
on the 104th floor
look
another key
another door
10% literal
90% metaphor
3000 some poems disguised as people
on an almost too perfect day
should be more than pawns
in some asshole's passion play
so now it's your job
and it's my job
to make it that way
to make sure they didn't die in vain
sshhhhhh....
baby listen
hear the train?
```

---

## IC-0038: Shadow Box

- Title: Shadow Box
- Author (byline): Michael Cristofer
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: June 1977
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BEVERLY, MARK
- Teaser before the introduction: Yes
- Spoken words (computed): 1331
- Already set (do not supply): none

### Source block (context only)

```text
Author: Michael Cristofer
ISBN: 978-0573616136
Publisher: Samuel French, Inc.
Date (Month/Year): June 1977
```

### Introduction (context only: never use it for content warnings)

```text
In this scene from Michael Cristofer’s The Shadow Box, Beverly, Brian’s ex-wife, and Mark, Brian’s gay lover, meet for the first time. And although the circumstances of this meeting would never be ideal – this meeting occurs because Brian is dying. Now I know what you’re thinking… AIDS, right? Wrong. Now, I don’t blame you for jumping to that conclusion. The media has pushed the horror of AIDS for quite some time. . .But unfortunately, it has been to the detriment of other illnesses that lead to an even greater death toll. Cancer kills more people every six weeks than AIDS is projected to kill this year. And that “less publicized” but equally devastating disease is what has brought Beverly and Mark together today.

The Shadow Box by Michael Cristofer
```

### Performance text (classify this)

```text
BEVERLY: Surprise! Oh, who are you? I’m sorry. I’m looking for Brian . . . uh . . . Two. They said cottage two. I must have . . .

MARK: No. This is two. This is cottage two.

BEVERLY: Oh ! Thank God. Is . . . uh . . . .

MARK: No. Not at the moment. But he should be back any minute.

BEVERLY: Good. I wanted to surprise him and he’s not here. Well, Surprise! Hmmm. Very nice. Very nice. All the comforts of home. Amazing what you can do with a coffin if you put your mind to it.

MARK: What?!

BEVERLY: Oh, sorry. Sorry. Introductions first. That way you’ll know who you’re throwing out. I’m Beverly. No doubt you’ve . . .

MARK: Yes. Brian’s wife.

BEVERLY: Ex-wife MARK: Former

BEVERLY: Yes. Former. He prefers former, doesn’t he.

MARK: Yes. I figured it was you.

BEVERLY: And you’re . . . uh . . . MARK: Mark

BEVERLY: Well, now that we know who we are . . . how about a drink?

MARK: A what? Oh, no. We don’t keep any liquor here. I could get you some coffee or some penicillin, if you’d like

BEVERLY: No. No. I was inviting you. I had an accident with the scotch on the way out here. There’s quite a dent in it. Anyway, we both look like we could use a little. Hmm?

MARK: No. I don’t drink.

BEVERLY: Ah, a dope man.

MARK: Neither. I like to avoid as much poison as possible.

BEVERLY: I see.

MARK: Well, you go ahead if you feel you have to.

BEVERLY: No. No, really. I don’t need it. I mean. I’m not . . . Forget it. So. How is he?

MARK: Dying. How are you?

BEVERLY: Ooooops. Let’s start again. Is he feeling any pain?

MARK: Are you?

BEVERLY: Strike two. Well, think we’ve got it all straight now. He’s dying. I’m drunk. And you’re pissed off. Did I leave anything out?

MARK: No. I think that just about covers it.

BEVERLY: Tell me. How is he?

MARK: Hard to say. One day he’s flat on his ass, the next day he’s running around like a two-year-old. But he is terminal – officially. He has fainting spells. They’re harmless. Well, that’s what they tell me. But it’s embarrassing for him because he falls down a lot and his face gets a little purple for a minute. I just want you to know. If you’re staying around. I mean, I think it would hurt him if people noticed.

BEVERLY: Well, if he turns purple and falls on the floor, it’d be sort of difficult not to notice, wouldn’t it?

MARK: Look. I don’t mean to be rude or stupid about this . . .

BEVERLY: Why not? I like people to be rude and stupid. It’s one of the ways you can be sure they’re still alive.

MARK: You’re very stoned aren’t you? And you’re dressed in funny clothes, and you’re saying a lot of funny things but I’m just not sure, frankly, what you’re doing here.

BEVERLY: Neither am I.

MARK: . . . . when I met Brian, I was hustling outside a bar in San Francisco. Right after the great “Summer of Love.” People were starving to death in the streets.

BEVERLY: Sounds lovely.

MARK: Like everybody else, I was very hungry, very desperate. So there I was one night, selling it down on Market Street. I wasn’t very good at it, and Brian walks up to me . . . and asks me the time. Right? Well, I did my little number about time for what and how much it was worth to him . . . and all of a sudden, he starts explaining exactly what time was worth to him . . . time warps even! Jesus, I though, I’ve got a real freak on my hands. And he’s talking and talking and talking. Finally, I say “Look man, I haven’t eaten in a long time, and I’m getting a headache. Why don’t we talk some business before I starve to death?”

BEVERLY: What did he do?

MARK: He bought me dinner! I couldn’t believe it. I mean, what did he want from me? And he never stopped talking. Never.

BEVERLY: He didn’t want anything from you.

MARK: It doesn’t matter, and that’s how I got to know him. I got interested in what he was doing. He gave me a room. I could use it whenever I wanted. We talked and talked endlessly. What am I talking about?

BEVERLY: Dead people.

MARK: Exactly! I mean, exactly!

BEVERLY: Exactly what?

MARK: I mean it’s not enough! We are dying here lady. That’s what it’s about. Brian looks at me and I can see it in his eyes. You can wipe up the mucous and the blood and the piss. You can burn the sheets and boil his clothes, but it’s still there. You can smell it on him. You can smell it on me. It’s sick and putrid and soft and rotten and it’s killing me.

BEVERLY: It’s killing him too.

MARK: That’s right, lady. And some of us have to watch it. Some of us have to live with it and clean up after it. Some of us are here for the duration. . . . And it’s not easy.

BEVERLY: And some of us wouldn’t mind changing places with you at all.

MARK: And some of us just don’t care anymore.

BEVERLY: What?

MARK: Some of us just don’t care.

BEVERLY: You’re cute, Mark. But next to me, you are the most selfish *person* I’ve ever met.

MARK: Oh, wonderful! That’s exactly what I needed. Yes, sir. That’s just what I needed.

BEVERLY: Let me tell you something– what you do is your business. You can drag *yourself* through every gutter from here to Morocco. You can trade it, sell it, or give it away. I don’t care. I’ll even show you the best way to do it. But Brian is different. Because Brian is different. Because Brian is stupid. Because Brian is blind. Because Brian doesn’t know where you come from or who you come from or why or how or even what you are coming to. Because Brian happens to need you. And if that is not enough for you, then you get yourself out of his life – fast.

MARK: That simple, huh?

BEVERLY: When the money and the time and the people are all running out faster than you can count, and the reasons don’t sound as good as they used to and you don’t remember any more why . . . why you walked out on the one person who said yes, you do what you have to because I love you. And you can’t remember anymore what it was you thought you had to do or who you thought you were that was so important that you couldn’t hang around long enough to say goodbye or find out what it was you were saying goodbye to . . . One human being who cares. My God, why isn’t that ever enough?

MARK: You want an answer to that?

BEVERLY: I want you to get yourself together or get yourself away from him.

MARK: Just leave? I can’t leave him.

BEVERLY: Why not?

MARK: I owe him.

BEVERLY: What? Pity? I mean, what’s in it for you?

MARK: Nothing’s in it for me.

BEVERLY: He’s just a tired, sick old man . . . A tired old trick with some phony ideas that don’t hold water . . . a broken-down sewer, that’s all he is.

MARK: I didn’t say that . . .

BEVERLY: You don’t need that. You don’t need to dirty your hands with that kind of rotten putrid filth. Unless of course you need the money. What does he do – pay you by the month? Or does it depend on how much you put out?

MARK: . . . I don’t want him to die. I don’t . . . Please . . . I don’t want him to die.

BEVERLY: Hopes, baby. That’s what you got. A bad case of the hopes. They sneaked up on you when you weren’t looking. You think maybe it’s not gonna happen. You think maybe you’ll find some way out. Some word that’s still alive, some word that will make it all different . . . Please, baby, just one favor you owe him. Don’t hurt him. Don’t hurt him with your hope. He needs somebody. That was my answer, too . . . Bye, baby.

MARK: Wait . . . .

BEVERLY: Tell Brian goodbye for me

MARK: Don’t you want to see him?

BEVERLY: No, I’ve got a plane to catch. It’s funny. He always makes the same mistake. He always cares about the wrong people.
```

---

## IC-0039: Sharpies

- Title: Sharpies
- Author (byline): David Narter
- Work: Best Ten Minute Plays of 2019
- Publisher: Smith and Kraus
- Publication date as stated: March 2019
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CHRISTINA, BRETT, MR. GLENN
- Teaser before the introduction: Yes
- Spoken words (computed): 1403
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Narter
Book: Best Ten Minute Plays of 2019
ISBN: 978-1575259338
Publisher: Smith and Kraus
Date (Month/Year): March 2019
```

### Introduction (context only: never use it for content warnings)

```text
It's that time of the year! Application forms, tests, early admission, teacher recommendations, and even a sleepless night or two. Time to apply for college? Try preschool! Twenty years ago, they just had to show up and not eat glue. These days it seems that if a kid isn’t ‘gifted’, they’re behind. In fact, in many of the larger cities (New York, San Francisco, Chicago) spots are limited and it can be super competitive.

What exactly are elite pre-schools looking for? According to Patty Washburn of the North Shore Country Day School, "We are not looking for children who can just handle the program; we also want children who can give something back to the class." So often, applicants (ie children) are observed in a “play-date” setting with numerous others to see how they fit in.

Sharpies by David Narter.
```

### Performance text (classify this)

```text
(BRETT and CHRISTINA are in a waiting room in which there is a single chair upon which is a scattering of brochures and forms. CHRISTINA is pacing. Frequently, they look toward the audience - the window of the playroom.)

CHRISTINA: Oh, God. This is so nerve-wracking.

BRETT: No. Tyler's fine. He'll do fine. (Long pause)

CHRISTINA: Did you talk with him last night?

BRETT: Excuse me?

CHRISTINA: When you two were out for ice cream, you were supposed to talk to him about this.

BRETT: About what? What am I supposed to tell him? Be smart?

CHRISTINA: So you didn't talk to him? Brett, you were supposed to let him know the situation and what was expected of him.

BRETT: Oh, Christina. C'mon. Does it really matter what I say to him? He's going to be doing arts and crafts and listening to story time.

CHRISTINA: Yes, it matters! Some of these kids are going to cry as soon as they get here and some kids are going to be comfortable in the situation and doing what they're supposed to do - maybe going beyond what's expected, Brett. Are you familiar with that expression, Brett? Beyond what's expected?

BRETT: Christina, I'll be happy if he doesn't eat the paste.

BRETT: Seriously, how does watching him play tell them anything about him.

CHRISTINA: It doesn't, Brett. It tells them about us.

BRETT: What?

CHRISTINA: How we parent. That's what they want to know.

BRETT: So this is about us. Don't you think that's a little self- centered?

CHRISTINA: Ugh! So did you tell Tyler anything at all, Brett?

BRETT: Well actually, I told him ... (in an announcer voice) "kill the competition!"

CHRISTINA: What are you talking about?

BRETT: It's an ad. It was an ad for Home Depot or something. He was a little freaked out, and I told him it was a figure of speech about competition and doing your best. I told him ... confidence. (reconsiders and then comes back to it) Confidence.

CHRISTINA: Oh. Oh. Well, good.

BRETT: Yeah. You know, I wasn't really talking about this at all though. It was actually - to be honest, I think he was kind of freaked out about the slogan. So, I just kind of generalized.

CHRISTINA: Well, sure. You tell a toddler to "kill the ... "

BRETT: Right. Listen, Christina, I said that there's lots of people and you have to do your best if you want to get noticed. That's all.

CHRISTINA: Right. Well good. That's good. That's good. So why didn't you just tell me that when I asked?

BRETT: Because I wasn't really talking about this. I mean I think he really thought about it, but I don't remember if I really said anything specific about today.

CHRISTINA: Hmm. Well, that's fine. I did.

BRETT: Yeah? When?

CHRISTINA: When we were driving in.

BRETT: What'd you say?

CHRISTINA: Same as you.

BRETT: Yeah?

CHRISTINA: Yeah, I told him that there are a lot of other kids who he'll see in his life and a lot in the room today and there are winners and there are losers. I told him it's best to think of himself as the sun and always make sure the teacher can see him shining bright. And that it is his job to be sure no one got in the way of his sunshine. (Long pause)

BRETT: Oh.

CHRISTINA: I just reminded him that it's a big world. And one little person can get crowded out by a lot of the mediocrity around him if he doesn't make sure he gets himself in the front of the line. Just like you - kill the competition.

BRETT: Just like me? I told him to be confident! I didn't tell him to "kill the competition"!

CHRISTINA: Well, neither did I.

BRETT: Are you kidding????

CHRISTINA: (realizing this is getting out of hand) Brett. Brett. Listen. Listen. You said it before. This isn't about Tyler. It's about us.

BRETT: I didn't say that. You did.

CHRISTINA: Anyway. We don't want to be arguing when they're watching him. Tyler is going to be Tyler and he's a part of us both. And I'm sure they'll see the best of us when they see him. Okay? Okay?

BRETT: Yeah, you're - right. (looks to audience: a glass through which they can see Tyler play) Hey, there he is!

CHRISTINA: Hey, baby. Who's my little handsome man? (MR. GLENN enters)

MR. GLENN: Oh, he can't see you. That's a one-way window -- or mirror. I suppose it all depends on which side you're on.

BRETT: Well, that's a little creepy.

MR. GLENN: Oh, for the most part it's pretty benign. We use it to evaluate staff members usually. But of course, assuming Tyler is accepted into the program, you're always welcome to watch him play without affecting the ... the chemistry of the classroom environment.

CHRISTINA: Oh. That's nice. What a little fella. He's gonna do a little painting.

MR. GLENN: He's an interesting young man.

CHRISTINA: Really?!

MR. GLENN: Absolutely. We had a good conversation before we went in. He told me he got ice cream last night.

BRETT: Yes he did.

MR. GLENN: He also said something about the radio scaring him. It seems he was a little anxious about it.

CHRISTINA: Really?

BRETT: Yeah. There was some ad - really freaked him out. I changed the station.

CHRISTINA: Yeah. Tyler's a very quiet - well - thoughtful boy. He thinks a lot. (long pause)

MR. GLENN: Well, that's good.

BRETT: Oh, look at that. He's got himself a girlfriend.

CHRISTINA: No, no. Tyler's teaching her how to paint.

BRETT: Yeah, how ‘bout that? They're painting together.

CHRISTINA: No. He's teaching her.

MR. GLENN: Really?

CHRISTINA: He's teaching her how to paint. See he's helping her hold the brush. No. No. Take turns, now. Hmm.

BRETT: Whoa, yeah that's not a lesson. That's a fight.

CHRISTINA: Nonsense, he's helping her, but she's not paying attention.

BRETT: Hmm. Nope they're fighting over that brush. Yeah, that's a fight.

CHRISTINA: Well, of course it's not a fight. Tyler is twice her size. He's helping her.

BRETT: I don't know. Okay, that's a shove.

CHRISTINA: Hey, now! That really was a shove. That little girl just pushed Tyler down. Mr. Glenn, shouldn't the teacher be interceding at some point?

MR. GLENN: I'm not sure that she's seen it yet. Oh! (All of them gasp in horror)

BRETT: Oh, my God. That's just right in her eye!

CHRISTINA: No, of course it isn't.

BRETT: Oh, it's in there.

MR. GLENN: Oh dear. (calling to be heard through the window) Mrs. Schiff!

CHRISTINA: That's not his fault.

BRETT: Christina.

CHRISTINA: It's not his fault. That girl was pulling and he just let go. He was letting her have the brush. He was being generous!

MR. GLENN: Finally, she's noticed.

BRETT: Whoa that was quick!

MR. GLENN: We do have a nurse on sight. And if that button is pushed ... well, as you can see, she's there in an instant.

BRETT: Jeez, I am so sorry ... I don't know what happened there.

CHRISTINA: It was an accident.

MR. GLENN: Of course. Of course it was.

CHRISTINA: Tyler no, no. No, honey. There are other brushes, you don't need that one. Not that one! (Horrified gasp from all three)

BRETT: Oh. That just popped right out.

CHRISTINA: What? Why is she yelling at Tyler? Oh, c'mon now. She's just upsetting him more.

BRETT: (rushing to the door of the observation room) Okay, this is over. I'm going ... (the door is locked) Mr. Glenn. Do you have a key?

MR. GLENN: No. I didn't even know there was a lock.

BRETT: Well, there's something keeping this from opening!

MR. GLENN: Dear God. He's locked us in here.

CHRISTINA: That's ridiculous. Tyler could not have done that.

BRETT: There's no way out!l!

CHRISTINA: Tyler, honey. This is mommy. It's okay. It's okay.

MR. GLENN: He's going for the scissors!

BRETT: No, Tyler!

CHRISTINA: Tyler! Tyler! Use the roundies, honey. Not the sharpies, not the sharpies!

(Both men freeze and look at Christina in shock. Then, looking back at the window, they all gasp in terror)

BRETT: There goes the nurse.

MR. GLENN: (patting his pockets) He's taken my cellphone!

BRETT: Christina. Your phone.

CHRISTINA: Don't be rude, Brett. (Brett makes a dash for her purse and rifles through it till he gets the phone)

CHRISTINA: No. No. Tyler. That's not nice. Gentle hands. Gentle hands.

BRETT: (fumbling with the phone) C'mon! C'mon!

CHRISTINA: Don't you run with those scissors.

MR. GLENN: Why is he climbing up there? (Their eyes follow him up a jungle gym)

CHRISTINA: He's playing king of the mountain! He's a little Moufasa! (She does a tiny wave) Look, Brett. They're all his little subjects! (Their eyes follow him jumping from the jungle gym. Again, the men gasp in horror and Brett drops the phone.)

BRETT: Oh, God.

CHRISTINA: Tyler. Mouths are for food. No biting! No!

MR. GLENN: Oh, that's the entire ear!

CHRISTINA: Tyler, no! People are not food! No! (Suddenly they all exhale.)

MR. GLENN: Oh, dear God.

CHRISTINA: Oh, look who's tired. No. No. Find your own space. Let her sleep. No! (As the men become even more shocked) Hands to yourself, Tyler. Hands to yourself!

MR. GLENN: How did he ... ? He knew exactly where the heart was.

BRETT: Well, that's something.

CHRISTINA: We have a few anatomy CD's. He's very advanced.

MR. GLENN: Dear God, he's walking to window.

BRETT: It's like he can see us.

MR. GLENN: He's looking right at us!

CHRISTINA: Hi, baby. (In baby talk) Who's got the messy red hands? Who's my messy boy? No. No. Wipe on a towel sweety. Not the window.

MR. GLENN: (recoiling in terror) He sees us! He sees us!

CHRISTINA: Don't be silly. He's writing letters. C - 0 -

MR. GLENN: They're backwards. Oh God! He can see us!

CHRISTINA: I know. He is very smart. Aren't you Tyler sweetie! Aren't you!

BRETT: N - F - I - D -

MR. GLENN: Confidence. He spelled confidence.

CHRISTINA: Oh, my little Moufasa is tired. Look at the little angel. He's just gonna lie down and have a "widdle nappie." (She watches him lovingly while Mr. Glenn cowers in the corner, panting)

BRETT: Mr. Glenn. I'm so ... well, I just don't know what to say.

MR. GLENN: There's nothing to say.

BRETT: Of course. Of course ... I just ... this is just... unbelievable.

MR. GLENN: Yes. Yes. (He collects himself and organizes his notes. He then pulls two sheets from the stack.) Well. You'll need to fill out these two forms. And I'll need a copy of Tyler's physical and a copy of your insurance card.
```

---

## IC-0040: Therac 25

- Title: Therac 25
- Author (byline): Adam Pettle
- Work: Not specified
- Publisher: Scirocco Drama
- Publication date as stated: Sept 2000
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ALAN, MOIRA
- Teaser before the introduction: Yes
- Spoken words (computed): 1606
- Already set (do not supply): none

### Source block (context only)

```text
Author: Adam Pettle 2003 National Qualifier
ISBN: 978-1896239705 2004 National Qualifier
Publisher: Scirocco Drama 2005 National Qualifier
Date (Month/Year): Sept 2000 2007 National Qualifier
2009 National Qualifier
2010 National Qualifier
2014 National Qualifier
NOTE: Here’s a link to Cat Steven’s Moonshadow to help with the signing parts:
https://www.youtube.com/watch?v=hr0rDW5j1KU
```

### Introduction (context only: never use it for content warnings)

```text
Cancer blossoms like a fleur du mal in the human body. That's a scary fact of life. Less certain -- and far more delicate -- is the love that flowers in a hospital cancer ward in Therac 25. Alan and Moira, the most unlikely of partners. From that first mutual look of interest as they wait for their ongoing therapies, they're a couple destined to alternate between tentative offers of comfort and spiky retreat. Therac 25 by Adam Pettle
```

### Performance text (classify this)

```text
A waiting room, the Princess Margaret Hospital. Early in the morning. Alan (22) sits in the waiting room. He has a black, bound journal in his lap; he is trying to write. After a beat or two, Moira enters the waiting room. She grabs a Reader’s Digest and sits down in a chair, feigning interest in the magazine. There is a long silence . . .

ALAN: What year is it?

MOIRA: What?

ALAN: The Digest

MOIRA: Oh. (checking the cover) Eighty-four.

ALAN: A fine year. The Summer Games in L.A., the arrival of E.T . . . Christ! That’s ten years ago already . . . . Now why would they want us to read articles from ten years ago? We’re cancer patients, not historians . . . . I’m Alan

MOIRA: Moira

ALAN: So, where’s your . . . ?

MOIRA: On my mind.

ALAN: And what number treatment is this?

MOIRA: Nine.

ALAN: Of?

MOIRA: Twenty-five.

ALAN: Hey! Me too. I’ve got two today.

MOIRA: Yum. . . . Are you trying to pick me up?

ALAN: What?! No, I mean, no! Christ, I’ve never even tried in a bar, I mean I just never know what to say, and in a waiting room at the Princess Margaret I think I’d really be out of my league. (Grabbing his journal) That could be my book: “One Hundred and One Lines to Pick Up a Cancer Patient” (He begins writing the idea down in his journal) (Pause)

MOIRA: “Hey, baby! Want to go for some platinum injections?”

ALAN: (Laughing) “You know, ah, I don’t want to brag, but I’ve got the lowest white blood cell count in this place.”

MOIRA: “I don’t know if anyone has ever told you this, but you’ve got the most scannable skull I have ever . . . “ (OVER THE INTERCOM) Mr. Feldman to Vault Forty-one. Mr. Feldman.

ALAN: That’s me. (Getting his stuff together) What are you doing this afternoon?

MOIRA: I have chemo at eleven-thirty.

ALAN: You’re doing both! Mon Dieu.

MOIRA: Just for another week. Then my cycle is over.

ALAN: Well do you have plans after chemo? Another one for the book.

MOIRA: Vomiting

ALAN: Can I join you?

MOIRA: You are trying to pick me up.

ALAN: I’m just . . . It’s just that I have eight hours in between my two treatment . . . If I go home, I’ll fall asleep in front of Geraldo, if I stay down here, I’ll wander from coffee shop to coffee shop. We could go for coffee in the four-star cafeteria.

MOIRA: Why would you want to go out with me? I’m . . . I’m bald.

ALAN: I’m Jewish.

MOIRA: Imagine what our kids would look like.

ALAN: My grandfather. What do you say?

MOIRA: I’ll meet you in the caf at twelve-thirty.

ALAN: Great! Have a good . . . Do you say “Have a good chemo?”

MOIRA: No.

(Alan walks out of the room, Moira closes her eyes and puts her face in her hands. Alan re-enters the room.)

ALAN: Did you say twel . . . ?

MOIRA: What?

ALAN: Sorry, I . . . Are you . . . How are you feeling?

MOIRA: Don’t say that.

ALAN: I know – the world’s worst question and yet I ask it; it’s just –

MOIRA: No! It’s not a joke. If you want to know me, you can never ask me that, it’s a rule, you understand?

ALAN: Yes. (Pause) Do you still want to meet me for coffee?

MOIRA: Maybe I’ll be there and maybe I won’t.

(SCENE)

(Alan sits in the cafeteria drinking a tea, anxiously looking to the door. After a few beats Moira enters the cafeteria and approaches Alan’s table, gingerly)

ALAN: You came.

MOIRA: I decided to forgive you.

ALAN: Thanks. How was . . . ?

MOIRA: Don’t ask. (She takes a pill out of her bad and washes it down with her bottled water.) So when was your diagnosis?

ALAN: Late August.

MOIRA: And what was . . . ?

ALAN: Oh, ah . . . a tumor on my thyroid gland which was removed two weeks later, along with eleven cancerous lymph nodes and the nerve attached to my left vocal cord. The tumor was wrapped around the nerve, which was a surprise to me and to Dr Brierly. He spent an hour during my surgery deciding whether to remove the nerve or –

MOIRA: Will you excuse me for a second? (Before the question is answered, she is up and out)

ALAN: (To himself) I think she’s gone to throw up. Is it the chemo, or the smell of the meatloaf? Or me? I wish I could . . . Maybe she wants me to go out there. I can’t. Christ, you know most people pick an early move and a bit afterwards for their first date . . . We are not most people.

MOIRA: (Re-entering the cafeteria) Sorry. What were you saying? We were talking about your surgery.

ALAN: Right. Ah, gone: thyroid, parathyroid, eleven lymph nodes – enough for a soccer team – the nerve attached to vocal cord, gained a . . . a new pair of eyes. You know, I was hopein they would do something about this nose, but . . . not enough OR time, I guess. Cutbacks, you know? Did you have surgery?

MOIRA: No. It’s inoperable. Like your nose. I have a high-grade pineal tumor that resembles meduloblastoma.

ALAN: (Pause) So, what do you want to be when you grow up?

MOIRA: Alive.

ALAN: I . . . I hear there’s good money in that.

MOIRA: I was in my third year of Sociology. I was thinking about social work.

ALAN: You are thinking about social work.

MOIRA: Whatever. Chris . . . my boyfriend . . . is coming to get me at one-thirty. Do you need a lift somewhere?

ALAN: Oh, no thanks, I’ve got my car.

MOIRA: Ooooh, he’s got a car.

ALAN: Yeah, she’s a ’79 Gremlin. It was my high school graduation present.

MOIRA: A Gremlin?

ALAN: Yeah, well, I didn’t do that well in high school. Do you drive?

MOIRA: I do, but not lately. I mean, you know what they say about morphine and driving.

ALAN: Well, you should give me your number. I mean, I’m coming down here every day, I’d be happy to give you a life if you – (She starts writing her phone number down and laughing.) What?

MOIRA: I was just thinking . . . I wonder what’s more distasteful: the chemo, or being driven to it in a Gremlin.

ALAN: Eh! Enough with the car. Here, I’m going to give you mine, too. (He writes down his number, starts to hand it to her, then pulls it back.) Now no crank calls, OK?

MOIRA: I promise

(SCENE)

(A small Greet Orthodox church beside the hospital)

MOIRA: Thanks for bringing me here. I haven’t been in a church in three years.

ALAN: Happy halfway home. Treatment number thirteen, c’est finis!

MOIRA: Why do you do that? . . . That French thing at the end of your sentences. If we were married that would be one of those things that would secretly drive me crazy and eventually force me into an adulterous affair.

ALAN: C’est dommage! I think the way that you stare at my hairline when I’m speaking would have me banging the maid long before you had a chance to .

MOIRA: Banging the maid? Is that what sex is with you? Banging?

ALAN: Do you think this is the place to be discussing this?

MOIRA: No. (Pause) If you’d said I would be nailing the maid, then we’d

ALAN: Oh. Nice. Crucifixion jokes, we are in big trouble.

MOIRA: Oh, you’re right, I shouldn’t mock God, make . . . make jokes about Jesus, I should be grateful for all this great luck I’ve been having . . . I’m sorry, God, please don’t give me locusts or . . . or a brain tumor, or . . .

ALAN: Moira, please –

MOIRA: Excuse me! I’m talking to God. And when I die, please take care of mommy and daddy and my dog Suzie . . .

ALAN: Do you ever wonder why everyone cries when they’re born? I men, not everyone cries when they die, right? At least not on TV.

MOIRA: No, they don’t. I think you’re on to something Nietzsche.

ALAN: I’m not talking about dying tomorrow, it’s a long way off, for both of us, but it is inevitable, and . . . and I think we could talk about it.

MOIRA: I don’t want to talk about it. . . Your top three.

ALAN: What?

MOIRA: Your top three biggest regrets if you die tomorrow, not that it’s going to happen. What are the chances of your cancer recurring, what?! Seventy-five percent it won’t.

ALAN: Yes! And you’ve got a good chance, too. I looked up meduloblastoma, it’s treatable! You’ve got a really good shot at beating this thing!

MOIRA: I think I’m going to throw up. . . No I am going to throw up. (Moira begins to sing Moonshadow to herself. After a beat or two, she begins to vomit)

ALAN: Ah . . . is there anything I can do for you?

MOIRA: Sing Moonshadow . . . Cat Stevens, Moonshadow, sing it.

ALAN: Moira, I . . . I . . . I don’t know it. (Moira puts her hand on Alan’s back; Alan moves away) No, I can’t

MOIRA: Can’t want?

ALAN: Be touched. I’m sorry I . . . I tried to tell you. It’s just that since September, since my surgery, I . . . I have days when I can’t be touched, not by hands, not by drugs, not even a hug from my mother. And I need you to know that it’s not your hands that are making me nauseous, it’s this body . . . How am I supposed to have a relationship? How am I supposed to explain why I’m crying for the ninth night in a row? . . . You know, I don’t even like it when someone holds my hand.

MOIRA: I think I’d better go. (Moira begins walking out, staggering a little. Suddenly she grabs the back of her neck then falls, convulsing in a seizure.)

ALAN: Oh my God! (Lights fade)

(SCENE)

(A hospital room. Moira sits in a hospital bed hooked to an IV. She is staring out the window, Alan enters.

MOIRA: I don’t want you here. I want you to leave. It’s going to be really embarrassing if I have to call Security – for both of us – so I’m asking you once more to leave.

ALAN: I can’t just leave things like this.

MOIRA: Which part of that didn’t you understand? Go away!

ALAN: No – you – just let me apologize, OK, and then I’ll leave.

MOIRA: Oh! I get it! You think this is your fault. This is a guilt visit. You won’t be able to live with yourself thinking you caused the seizure that broke the camel’s back.

ALAN: (simultaneously with “live”) That’s not what I’m saying. I just need to talk to you.

MOIRA: You need to talk to me? What could there possible be to talk about? Now get out and don’t come back.

ALAN: “I’m being followed by a moon shadow, moon shadow, moon shadow. I’m leaping and hopping on a moon shadow, moon shadow, moon shadow . . . “ (He has some trouble remembering the words) “And if I ever lose my eyes, lose my eyes, if I lose. And if I ever lose my eyes, oh way hey hey hey hey hey hey hey hey, I won’t have to see again.”

MOIRA: It’s a joke (near tears) (pause)

ALAN: What’s happening?

MOIRA: I told you that my tumor resembled meduloblastoma, but what makes it different is that it can travel through the spinal fluid to other parts of the brain and . . . mine has.

ALAN: What does that mean?

MOIRA: That I’m going to die.

ALAN: When?

MOIRA: Soon.

ALAN: Is there anything I can do? (Moira shakes her head, but then it slowly turns into a nod. She looks at him, reaches down and touches his nose. Alan does not pull away. Moira runs her hand down his face, and then takes his hand and puts it on her chest.) Moira . . . how are you feeling?

MOIRA: I’m scared.
```
