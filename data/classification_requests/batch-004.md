# Classification request: batch 4 of 63 (40 records, IC-0121 to IC-0160)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-004-reply.json`.

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

## IC-0121: Credo

- Title: Credo
- Author (byline): Craig Lucas
- Work: What I Meant Was
- Publisher: Theatre Communications Group
- Publication date as stated: June 1999
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1219
- Already set (do not supply): none

### Source block (context only)

```text
Author: Craig Lucas
Book: What I Meant Was
ISBN: 155936159X
Publisher: Theatre Communications Group
Date (Month/Year): June 1999
```

### Introduction (context only: never use it for content warnings)

```text
It used to be all the rage to write a "personal creed." When "honor" wasn't looked at as something to avoid, "compassion" wasn't an indication of weakness, and "armed forces" weren't something to avoid at all costs, men and women took the time to figure out what make themselves tick. Determining what you believe, what you value, and where you want to place your time and effort can give you a certainty about your life like nothing else can. Determining what you're all about...your mission statement, if you will...makes it so you know in advance what you will and won't do in life. What’s your Credo by Craig Lucas.
```

### Performance text (classify this)

```text
It's Christmas eve,
I go out with the dog.
Jim and I have just broken up.
I've just been to an AA meeting
Where a woman got up
And said she had no friends,
Her best friend is her VCR
And it's broken.
I came home to the hole where the sofa was.
There's no Christmas tree either.
I can't stand the thought of sweeping up all the dead needles
And dragging the carcass out to the street
To join all the other dead trees
With what's happening to the rain forest.
I know the two aren't connected,
But anyway, I pull up a folding chair
And heat up a piece of cold pizza.

This, I think, is the low point. The walls show little ghosts where the pictures once were. I go out.

Did I tell you I didn't get my Christmas bonus?
Well, I wasn't expecting it,
But I haven't been able to take Apple to the vet about her problem,
So she dribbles a little across the lobby,
Past the doorman who isn't smiling at me;
I'm sure it's because I haven't given him his Christmas bonus,
But maybe's it's the trail of urine, too,
I don't stop to ask.
I smile bravely
And step outside where it has of course started to rain. .
And people are running and looking very upset.
Surely the rain isn't that bad.
I turn
There's been an accident on my corner
I snap my head away,
I know if I look there'll be a baby carriage there
ln the middle of the street.
I refuse to look.
They certainly don't need another person standing around not doing anything.
I put my mind ... Where can I put my mind?
Vienna.
Where Jim has gone with the woman he left me for.
You can't escape these thoughts.

All I know is her name.
Her name ... is Carmella.
Apparently.
And I believe that she has had a sex change.
As far as I know, this has no basis in fact,
But I believe it as firmly as-I believe
That there is nothing wrong with New York City
That can't be solved at least in part by keeping
Cardinal John J. O'Connor out of city politics
And back doing what he really does best
Which, if we are to take his word for it, is:
Exorcisms.

Where,
Where can I put my thoughts?
Ecuador.
My parents are in Ecuador.
They asked me to join them,
And I said
No, Jim and I would be spending the holiday together.
I hope that he and Carmella are caught
In the crossfire of some terrorist ...
No, I don't .
Not really. But you know:
The sort of thing you see
On the evening news.
If you have a TV
Or a phone.
Jim stopped paying the bills months ago,
As a kind of secret warning of what was to come.
But I refuse,
In my bones I refuse
To see myself as a victim.
I have gotten myself into this.
I allowed him to talk me into maintaining a joint bank account.
Every time a little voice in my head would say
Watch out.
He's cute,
But he's not that nice.
Beneath it all,
Behind the charm,
His chin,
That first night,
And then again in Barbados,
Beneath it all
Is him.
I alone took each and every step
Which brought me here
To this street corner
In the rain
On Christmas eve
With my dog whose urinary infection
I cannot afford to fix.
And at that moment, my friends,
My dog squats.
And the worst thing that has ever happened to me
Unfolds before my very eyes.
A wire, loose plug from somebody's Christmas decorations
Carelessly strung in front of their little tea shop ...
Electrocutes my dog.
And she falls immediately dead
On the sidewalk
In a sputter of sparks ...
And the lights go out all down the front of the tea shop.
And a man comes out:
"What did you do?"
And I drop to my knees, unafraid,
Let me die, too,
Electrocute me.
And I embrace my dog, Apple,
Whom I have had for sixteen years.
She is my oldest friend.
She has seen me in my darkest, most drunken days.
She has been to every corner of my life,
She growled at the dogs on the dog food commercials.
She has been across the country and back.
Apple, I'm not afraid to say, is the purest,
Most uncomplicated expression of love I have ever known.
And she has been killed by an electric current
In the last sick days of her valiant existence.

The man stares at me from above.
"Oh my god" he says.
He can't believe it
Any more than I can believe it.
Come in, he says.
We carry Apple into the shop.
To me she smells good,
But to some people she does not.
It's been too cold to bathe her.
It's hard for one person to hold her in the shower.
She doesn't like the water.

The man offers me the only thing he has.
Tea.
We talk
And he assures me that the accident on the corner
Did not involve a child.
And no one was killed.
What to do now with Apple?
I can't cry anymore.
I have cried so much the last two weeks
I can't cry for her now.
And I know ...
In some way I see all at once that
Jim was not really good enough for me,
That I will meet someone else.
And even if I don't I will have
An extraordinary and rich and complicated life.
It is entirely up to me.
I will most likely survive all the roadblocks and the detours.
As my dad always says:
"Life can be rough, but think about the alternative."

But then again
He's never been sick a day in his life.
He hasn't ever had to struggle just to stand
Or been unable to stop himself from peeing
Where he knows he shouldn't
And doesn't want to,
But there it is in a stream,
Surprising him and me.
He's never had to look up
With big sorrowful eyes which say:
"I had no idea.
Don't yell."

No.
I only hope that 1 will go as quickly as Apple
When the time comes.
And if I don't,
I will absolutely,
I know I will face that bravely
And with dignity.
I know.

And if,
For some unforeseen but totally justified reason,
I can't,
And I am making a complete ass of myself,
Saying things I wouldn't ever say
And acting childishly
And turning into a prude
And a conservative
And am being a complete drag on everyone
For months and years,
I know my friends will forgive me.

And if for some equally valid and twisted,
But ultimately logical reason,
They don't
Or they can't,
Or they're all dead by then,
Or it's August and they're away
Then I will forgive them,
Right?
The same way I forgave myself
For yelling at Apple the first time she peed
Before I realized what was going on.

And if. ..
Again, if I can't,
And everything is entirely for shit
And I can't even find my way to the end of a sentence ...
And ... you can fill in all the blanks ...
That will be fine, too.
```

---

## IC-0122: Crying in H Mart

- Title: Crying in H Mart
- Author (byline): Michelle Zauner
- Work: Not specified
- Publisher: Knopf
- Publication date as stated: April 2021
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MICHELLE
- Teaser before the introduction: Yes
- Spoken words (computed): 1674
- Already set (do not supply): none

### Source block (context only)

```text
Author: Michelle Zauner
ISBN: 978-0525657743
Publisher: Knopf
Date (Month/Year): April 2021
```

### Introduction (context only: never use it for content warnings)

```text
Crying in H Mart by Michelle Zauner
```

### Performance text (classify this)

```text
MICHELLE: (Pg 8-14) Ever since my mom died, I cry in H Mart.

H Mart is a supermarket chain that specializes in Asian food. The H stands for han ah reum, a Korean phrase that roughly translates to "one arm full of groceries." H Mart is where parachute kids flock to find the brand of instant noodles that reminds them of home. It's where Korean families buy rice cakes to make tteokguk, the beef and rice cake soup that brings in the New Year. It's the only place where you can find a giant vat of peeled garlic, because it's the only place that truly understands how much garlic you'll need for the kind of food your people eat.

H Mart is freedom from the single-aisle "ethnic" section in regular grocery stores. They don't prop Goya beans next to bottles of sriracha here. Instead, you'll likely find me crying by the banchan refrigerators, remembering the taste of my mom's soy-sauce eggs and cold radish soup. Or in the freezer section, holding a stack of dumpling skins, thinking of all the hours that Mom and I spent at the kitchen table folding minced pork and chives into the thin dough. Sobbing near the dry goods, asking myself, “Am I even Korean anymore if there's no one left to call and ask which brand of seaweed we used to buy?”

MICHELLE: Growing up in America with a Caucasian father and a Korean mother, I relied on my mom for access to our Korean heritage. While she never actually taught me how to cook (Korean people tend to disavow measurements and supply only cryptic instructions along the lines of "add sesame oil until it tastes like Mom's"), she did raise me with a distinctly Korean appetite.

Food was how my mother expressed her love. No matter how critical or cruel she could seem --constantly pushing me to meet her intractable expectations -- I could always feel her affection radiating from the lunches she packed and the meals she prepared for me just the way I liked them. I can hardly speak Korean, but in H Mart it feels like I'm fluent. I fondle the produce and say the words aloud -- chamoe melon, danmu ji. I fill my shopping cart with every snack that has glossy packaging decorated with a familiar cartoon. I think about the time Mom showed me how to fold the little plastic card that came inside bags of Jolly Pong, how to use it as a spoon to shovel caramel puffed rice into my mouth, and how it inevitably fell down my shirt and spread all over the car. I remember the snacks Mom told me she ate when she was a kid and how I tried to imagine her at my age. I wanted to like all the things she did, to embody her completely.

My grief comes in waves and is usually triggered by something arbitrary.

I can tell you with a straight face what it was like watching my mom's hair fall out in the bathtub, or about the five weeks I spent sleeping in hospitals, but catch me at H Mart when some kid runs up double-fisting plastic sleeves of ppeongtwigi and I'll just lose it. Those little rice-cake Frisbees were my childhood, a happier time when Mom was there and we'd crunch away on the Styrofoam-like disks after school, splitting them like packing peanuts that dissolved like sugar on our tongues.

I'll cry when I see a Korean grandmother eating seafood noodles in the food court, discarding shrimp heads and mussel shells onto the lid of her daughter's tin rice bowl. Her gray hair frizzy, cheekbones protruding like the tops of two peaches, tattooed eyebrows rusting as the ink fades out. I'll wonder what my mom would have looked like in her seventies, if she'd have wound up with the same perm that every Korean grandma gets, as though it were a part of our race's evolution. She'd pluck the lint off my coat and pick on me -- how my shoulders slumped, how I needed new shoes, how I should really start using that argan-oil treatment she bought me -- but we'd be together.

If I'm being honest, there's a lot of anger. I'm angry at this old Korean woman I don't know, that she gets to live and my mother does not. Why is she here slurping up spicy jjamppong noodles and my mom isn't? Other people must feel this way. Life is unfair, and sometimes it helps to irrationally blame someone for it.

Sometimes my grief feels as though I've been left alone in a room with no doors. Every time I remember that my mother is dead, it feels like I'm colliding with a wall that won't give. There's no escape, just a hard surface that I keep ramming into over and over, a reminder of the reality that I will never see her again.

H Marts are usually situated on the outskirts of the city and serve as a secondary center for strip malls of Asian storefronts and restaurants that are always better than the ones found closer to town. You'll know that you're headed the right way because there will be signs to mark your path. The lettering on the awnings slowly begins to turn into symbols that you may or may not be able to read. Suddenly, it's another country. Everyone is Asian, a swarm of different dialects crisscross like invisible telephone wires, [and] the only English words are HOT POT and LIQUORS.

Inside an H Mart complex, there will be some kind of food court, an appliance shop, and a pharmacy. My local H Mart is in Elkins Park, a town northeast of Philadelphia. [It] has two stories; the grocery is on the first floor and the food court is above it -- an array of stalls serving different kinds of food. One is dedicated to sushi, one is strictly Chinese. There's a stall for Korean street food [and] there's my personal favorite: Korean-Chinese fusion, which serves tangsuyuk -- a glossy, sweet-and-sour orange pork-seafood noodle soup, fried rice, and black bean noodles.

The food court is the perfect place to people-watch. I think about my family who lived in Korea, before most of them died, and how Korean-Chinese was always the first thing we'd eat when my mom and I arrived in Seoul after a fourteen-hour flight from America. Twenty minutes after my aunt would phone in our order, the apartment ringer would buzz, and up would come a helmeted man, fresh off his motorcycle, with a giant steel box. He'd slide open the metal door and deliver heaping bowls of noodles and deep-fried battered pork with its rich sauce on the side. We'd dribble black, chunky goodness all over the noodles and pour the shiny, sticky, translucent orange sauce over the pork. We'd sit cross-legged on the cool marble floor, slurping and reaching over one another. My aunts and mom and grandmother would jabber on in Korean, and I would eat and listen, unable to comprehend, bothering my mom every so often, asking her to translate.

I wonder how many people at H Mart miss their families. How many are thinking of them as they bring their trays back from the different stalls. If they're eating to feel connected, to celebrate these people through food. Which ones weren't able to fly back home this year, or for the past ten years? Which ones are like me, missing the people who are gone from their lives forever?

It's a beautiful, holy place. A cafeteria full of people from all over the world who have been displaced in a foreign country, each with a different history. But I know we are all here for the same reason. We're all searching for a piece of home, or a piece of ourselves. We look for a taste of it in the food we order and the ingredients we buy. H Mart is where your people gather under one odorous roof, full of faith that they'll find something they can't find anywhere else. In the H Mart food court, I find myself again, searching for the story I want to tell about my mother.

I am sitting next to a Korean mother and her son. The kid dutifully gets their silverware from the counter and places it on paper napkins for both of them. He's eating fried rice and his mom has seolleongtang, ox-bone soup. He must be in his early twenties, but his mother is still instructing him on how to eat, just like my mom used to. "Dip the onion in the paste." "Don't add too much gochujang or it'll be too salty." Some days, the constant nagging would annoy me. Woman, let me eat in peace! But, most days, I knew it was the ultimate display of a Korean woman's tenderness, and I cherished that love. A love I'd do anything to have back.

The boy's mom places pieces of beef from her spoon onto his. He is quiet and looks tired and doesn't talk to her much. I want to tell him how he should be kind to his mom, remember that life is fragile and she could be gone at any moment. Tell her to go to the doctor and make sure there isn't a small tumor growing inside her too.

Within five years, I lost both my aunt and my mother to cancer. So, when I go to H Mart, I'm not just on the hunt for cuttlefish; I'm searching for memories. I'm collecting the evidence that the Korean half of my identity didn't die when they did. H Mart is the bridge that guides me away from the memories that haunt me, of chemo and skeletal bodies and hydrocodone. It reminds me of who they were before, beautiful and full of life, wiggling Chang Gu honey-cracker rings on all ten of their fingers, showing me how to suck a Korean grape from its skin and spit out the seeds.

[You see, that’s why] . . . Ever since my mom died, I cry in H Mart.
```

---

## IC-0123: ‘da Kink in my Hair

- Title: ‘da Kink in my Hair
- Author (byline): Trey Anthony
- Work: Not specified
- Publisher: Playwrights Canada Press
- Publication date as stated: Sept 2005
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NOVELETTE, PATSY
- Teaser before the introduction: Yes
- Spoken words (computed): 1491
- Already set (do not supply): none

### Source block (context only)

```text
Author: Trey Anthony
ISBN: 978-0887547560
Publisher: Playwrights Canada Press
Date (Month/Year): Sept 2005
```

### Introduction (context only: never use it for content warnings)

```text
According to George Yancy, author of Our Black Sons Matter . . . “There are millions of loving mothers of Black sons who are painfully aware of what it means to give birth to and raise [them] in a world that marks their sons from birth as “unwanted,” as “problems,” who are already so-called criminals, uneducable thugs and surplus bodies.

The future for many young black males in America is not bright. They face a greater rate of imprisonment, a greater chance of being killed and a greater chance of being unemployed. Trey Anthony explores the emotional struggles of a mother trying her best to raise a black son in ‘da Kink in My Hair.
```

### Performance text (classify this)

```text
NOVELETTE: (Pg 3) (addresses the audience while she readies her hairdressing shop for the day) My work is never done! I’m always working, working, working. You want me to talk to you, explain what’s going on? I have no time to talk to you today! I’m a busy busy career woman. (She grabs a broom and begins sweeping) I’m telling you between doing my makeup, sweeping, and of course doing hair, the work never stops! Being a hairdresser is not an easy thing. People rushing in here talking about oh Novelette, I want this style, this cut, this washed, this coloured, don’t they see I’m busy – (Pg 4) I’m telling you if it’s not one thing it’s the other. Women rushing in here, looking like they got run over by a Mac truck, then expecting me to make them look like Janet Jackson. I said (to a customer who sits in her chair) lady I’m a hairdresser not a magician! (Pg 12) And don’t you dare come back in here again looking like Donald Trump! (begins to wash, cut and style her customer as she returns to her conversation with the audience) I tell you as a hairdresser you get to know everybody’s business. (Pg 5) Not that I’m nosy or anything. But if they don’t tell you the hair will. Don’t believe me? Well let me tell you . . my mother was a hairdresser, my mother’s mother was a hairdresser , and my granny granny (She counts on her fingers) granny, branny use to b a hairdresser. If you want to know about a woman, a black woman, that is. Touch her hair Cause our hair carries our journey. ‘Cause that’s where we carry all our hopes, all our dreams, our hurts, our disappointments. They’re all in our hair. (She shakes her head) You don’t believe me well watch this!

(She begins to weave her fingers through her customer’s hair. The hair sends her a message. She closes her eyes, her fingers entwined deeply in the woman’s hair) (pg 6-7) I’m telling you the hair sends me a message. Some of the things it tells me makes me want to laugh, makes me want to cry. And some of the things it tells me I don’t even want to know. Because some of us are hurting. Hurting real bad. And you know as women we cry, cry a lot. Cry on the inside too proud to cry on the outside. And some of the thing, which the ahair tells me maks me want to cry. But I don’t I keep it up here (touches her head) Right here in my head. Right here in my hair. . . .

NOVELETTE: (Pg 17) Lord, Patsy, I didn’t think you were coming again. What time you running on West Indian or Christian time? (She ushers Patsy into the chair)

PATSY: (She shakes her head obviously amused) Sorry, Letty, prayer meeting ran over and you know you cannot rush the Lord.

NOVELETTE: (She laughs gently) Well, I am glad you made it. You know I’ve been meaning to come over and have a little tea or a strong drink of rum with you.

PATSY: Oh the Lord knows I’m going to pray for you darling.

NOVELETTE: (Pg 18) Well while you’re praying. You think you could ask the man up above about the Lotto numbers for me! Because I want to win some money!

PATSY: (Pg 19-23) Novelette! Please. Could you just give me the same thing like every week. A nice wash and set. A simple uptwist, with three hairpins thanks.

(Novelette touches Patsy’s hair. As her fingers root themselves deeply into Patsy’s hair, a preacher’s voice is heard in the distance)

PATSY as PREACHER: And the Lord says who shall believe in me will receive salvation.

PATSY: Romey use to say "Mom you worry too much. Ain't nothing ever gonna happen to me. "And then he would smile that easy slow smile that crept across his beautiful face. And those eyes, eyes full of mischief. Eyes that always let me know that child was up to something. (beat) Like taking four cookies instead of two. Changing that C minus on his report card to some messed up looking A. But he was a good kid. Yes he was. (beat)

I would say Jerome. I would call him Jerome when I get serious or I got something important to say. Otherwise he was just Romey, my Romey. And I remember that night, I said, Jerome I don't have a good feeling about this. Why don't you and Damion rent some movies and I'll fix you some Kool-aid, order some pizza and you boys just can stay in. The streets are not safe for young boys. (beat) And Romey rolled his eyes and smiled that easy slow smile. And he said "Mom, you worry too much, nothing going to happen to me. And besides Mom, we ain't on the streets it's a school dance. Nothing going to happen at a school dance. And Mom you know Denna Stewart going to be there, and you know I got a thing for Denna Stewart. I 'm gonna show her my moves on the dance hall and she's gonna be all mine." (She laughs.) And before I know it Damion's at the door, honking the horn. And Romey' s racing down the front step. And I said (very urgent) "Jerome! Be careful." And he smiled that easy slow smile. And he said "I'll be home by twelve-thirty" and I said "you better be in here by twelve a.m." and he took off running. And we both knew he wouldn't be home till twelve-forty-five. That's Romey always trying to get away with something. But he was a good kid. My boy was good. And that's all I said "be home by twelve." And he was gone. (beat, emotion begins to build, voice wavers) And I'm real mad with myself. Cause I thought I should have told him wear your brown coat cause it's a real warm coat. But I let him leave wearing the blue one and that not a real warm coat. And I should have told him I loved him-(yells out) I love you! And I should have just listened to that rotting feeling in my gut and begged him to stay. (yells out) Stay home Romey! But I didn't. I should have just said (yells) Wear your brown coat Romey, it's a warmer coat! Because he was lying on the ground you know, on the cold hard ground. Bleeding to death. And maybe if he was just wearing his brown coat-maybe the coat would have kept him-maybe ... But brown coats don't protect little black boys from bullets do they. Damion said they were outside in the school parking lot. Romey was talking to Denna. And one minute he was laughing, and there was a bang and Romey fell to the ground. (two beats)

No one knows who did it. No one knows why. And no one is talking about it. There was no witnesses. No witnesses? Nearly two hundred kids in a parking lot and no one saw anything. But someone shot Romey three times. Three times and my baby's gone. Because they killed him! They can do that! Your son can kill my son just because! Because, maybe he didn't like the color of his jacket. They are killing each other! (two beats) And the police claim they are doing all that they can. But who is protecting our children from some of them police. How much is my son's life worth? (beat) Why do you need a license to shoot a damn bird! You go to jail for leaving your dog outside! But my baby, can lie on the ground for twenty minutes before someone calls an ambulance. (beat) Because there is no sign posted "warning Black boys are in danger of becoming extinct." How come they can't grow up to be Black men? (three beats) And I know as a mother, you're suppose to love them, teach them, keep their butts in line, tell them to wear brown coats instead of blue-but you're not suppose to bury them! (beat) A mother isn't supposed to bury her son ... (three beats)

I took my ultrasound yesterday. And it's a boy. Me a mother again? And I thought about you Romey. Maybe he'll have your slow moving easy smile. Or maybe he'll have your eyes. Eyes full of mischief. And I cried. Cried for my baby. Right there in the waiting room I bawled, nose running and everything, a real ugly kinna cry. I cried for my sons. Cried for our sons. (two beats) And all the other mothers in the waiting room, they just looked away. Just looked away. Cause they understood. (beat) No, they understand.

(PATSY returns back to the chair and the lights change. NOVELETTE's hands are still in her hair and has told her the story. Novelette speak softly, gently with this new knowledge)

NOVELETTE: So there you go a nice wash and set. This hair is growing, nice and thick. You know, they say a woman's hair grows when she's pregnant.

PATSY: Letty, how did you know? I haven't told anyone but my husband and God .

NOVELETTE: I know.

PATSY: Oh, Letty, I don't know if I can do this again. You know with Romey and everything ... and what if I'm not a good mother and maybe it's too soon. And and-- I just can't help thinking about Romey and if I had only ... (sighs) and maybe I'm too old. Novelette you think I'm too old?

NOVELETTE: Patsy, you're not too old! And I'm no Christian or anything, but I believe God knew you had a lot more love to give so he decided to give you another chance. I knew Romey and that boy was a good kid. And good kids don't raise themselves Patsy. You were [and will be] a good mother. (To audience) (Pg 5) You want to know about a woman, a black woman that is. Touch her hair. That’s where we carry all our hopes, all our dream, our hurts, our disappointments. [It’s] ‘da kink in our hair.
```

---

## IC-0124: Dancing with a Devil

- Title: Dancing with a Devil
- Author (byline): Brooke Berman
- Work: Humana Festival 1999: The Complete Plays
- Publisher: Smith and Kraus Publishers
- Publication date as stated: 1999
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 986
- Already set (do not supply): none

### Source block (context only)

```text
Author: Brooke Berman
Book: Humana Festival 1999: The Complete Plays
ISBN: 978-1575252070
Publisher: Smith and Kraus Publishers
Date (Month/Year): 1999
```

### Introduction (context only: never use it for content warnings)

```text
In this selection, a young woman moves to the city so she can pretend to live life on the edge . . . She finds out she is not as safe as she had believed. Dancing with a Devil by Brooke Berman
```

### Performance text (classify this)

```text
WOMAN: I am 24 years old, and I live in New York City. My life is shiny and new, and just barely discovered. I am an emerging something or other, waiting tables and writing stories. I go to parties with people whose skin sparkles and whose names are known. I like to tell stories about how I am 24 years old and still a virgin, deconstructing the relationship between my heart and my skin and my sex.

WOMAN: I like to dance, to feel air inside my body. I think that dancing will save me from pain. The music will earth me and the beat will bring me to the ground. I go dancing in gay bars with funny names. I take great pleasure being a girl in a boy-bar, enjoying the fact no one is going to try and pick me up. My life is safe. I play outrageous, but my life is safe . . . because I have made it that way. Just enough outrage, and lots of safety nets.

On the first day of the new year, I write down a list of my dreams and goals. I have many dreams, the foremost of which is this. “I want to be transformed.” I write it down: “I want to be transformed.” Because that is what I want.

I look for transformation anywhere I can. I look for it in the eyes of other people, but I don’t see it there. I look for it in the mountains in New Mexico, in the water of the hot springs, in the air of New York City and in the words that come to me while I dream.

It is June, I am 24, and I am about to be transformed. (PAUSE)

It’s June, June 19th to be precise, just barely after midnight. And I am about to fall asleep in my safe bed, in my safe SoHo fourth floor walk up. It’s four in the morning and I open my eyes, certain that Sarah, my old roommate, has come home, though she moved out months ago and this makes no sense. I am sure that Sarah is in the apartment and I open my eyes, fully believing I will see her there.

But I don’t see Sarah. I see someone I do not know. I open my eyes to a stranger standing at the foot of my bed wearing a little black half mask and a black turtleneck, looking a little bit like Zorro or like an existentialist Lone Ranger, and I cannot understand how this stranger has penetrated my sleep or entered my apartment.

The stranger just stares at me. He doesn’t move. He says, “Good evening.” And then the stranger moves towards me very, very slowly, like in slow motion and I understand everything that is about to happen. I understand it in my mind before he even touches me. I think: “This can’t happen to me.” I think this can’t happen to me because I am very smart. I have read Roland Barthes and I know how to deconstruct sexuality. I am a virgin, and I am very smart, and things like this aren’t supposed to happen to people like me.

The stranger says, “Everything will change now, everything about you will change, you will no longer be who you were, you will have to become someone else to even understand this, to even put it behind you. You will leave your friends, your home, your family in order to become a person who can put this behind herself. I am the answer to your prayers. I am giving you what you asked for. I am giving you the gift of transformation.”

But I don’t want to transform. Not like this. I don’t want to go through with it.

I am dancing with the devil right now in a time that lasts longer than ordinary time.

It was all over quickly. It seemed to take a long time, but I know that in the reality we call reality, it happened within the span of ten, maybe 15, minutes. He turned me over like some object and covered my head with a pillow and stuck his rage and his pain all inside me, and then it was over. And he was gone, as quietly and mysteriously as he came. He came out of the night and went back inside of it and was never caught.

I have taken the pain of some man that I do not know inside of me. I have taken it inside and transformed it . . . inside. I have go to rape crisis centers and to therapy and to psychic healing in order to transform the pain he stuck inside me one morning. Me, a stranger. I carry energy inside of me, some of which you deposited there. Rapists don’t use protection.

But I am not a repository for some stranger’s suffering. Do you hear me? I DON’T WANT YOUR SUFFERING. YOU CAN JUST PUT IT SOMEWHERE ELSE, AND I HOPE THAT YOU SUFFER TIL THE END OF TIME, TIL THE END OF EVERYTHING. MAY YOUR SOULD KNOW WHAT YOU HAVE DONE TO ME AND MAY YOU . . . MAY you . . . may you be healed.

Everything will change, he said. And it did.

I am not 24 years old anymore. I have changed. I do not know the people I knew then. My friends are different, my work is different. I have lived in seven different apartments in the last three years. I do no live along. I sleep with a nightlight.

I am a statistic. How many women in ten? I meet young women who remind me of myself, before it happened, and they scare me. I am afraid that something will cause them to leave a piece of themselves behind forever. I hope not. But . . . . everything has changed. Except that I still wake up at four in the morning expecting to find him there.
```

---

## IC-0125: Dead Men’s Fingers

- Title: Dead Men’s Fingers
- Author (byline): Don Nigro
- Work: Cincinnati and Other Plays
- Publisher: Samuel French, Inc.
- Publication date as stated: 1989
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: OPHELIA
- Teaser before the introduction: Yes
- Spoken words (computed): 2233
- Already set (do not supply): none

### Source block (context only)

```text
Author: Don Nigro
Book: Cincinnati and Other Plays
ISBN: 978-0573621055
Publisher: Samuel French, Inc.
Date (Month/Year): 1989
```

### Introduction (context only: never use it for content warnings)

```text
Shakespeare’s Ophelia – A weak woman who descends into madness? Obedient daughter? Subservient?

In Don Nigro’s interpretation as presented in Dead Men’s Fingers – we are allowed into Ophelia’s innermost thoughts about love, family, life and ultimately her own death. And Nigro’s Ophelia is anything but weak, obedient and subservient.

Dead Men’s Fingers by Don Nigro
```

### Performance text (classify this)

```text
OPHELIA: The fact is, I am, and have always been, much too intelligent for my own good-it was I think my downfall, in fact, that I could think, and think much more deeply and efficiently than that poor spoiled delinquent . Hamlet ever could, but there was a kind of blindness all about me, they could not see it, would not see it, for along with my intelligence came a desire to be thought good, to be kind to those around me, to give my father what pleasure I could, to keep my brother Laertes, who was in his own way even stupider than my dear moronic father, as serene from moment to moment as could be expected - my tragedy was that while I loved all these people I knew how stupid they were, and could do nothing about it.

OPHELIA: It's very strange, not what I had expected it to be. I don't know what I expected, exactly, but this definitely isn't it. And yet it seems, in the end, to have been more or less inevitable that this is what it should have turned out, finally, to be like. Remembrance. Death is remembrance. As of a performance. As of a play completed. In a dark, empty theatre. Do you know what I keep thinking of?

We're very small, playing in the garden, under the crab apple tree, Hamlet, Laertes and me. Hamlet suggests that we play Adam and Eve in the Garden of Eden. Hamlet's games, even then, always seemed to take the form of elaborate stage plays, with himself as director, god and star. First, he says, Laertes and I must take off all our clothing. I have some reservations about this, but in the end we always do everything Hamlet tells us to. Now, says Hamlet, Laertes is Adam and Ophelia is Eve. But she's my sister, protests Laertes. So was Eve Adam's sister, says Hamlet. They had the same father, didn't they? Oh, says Laertes. He was never very bright. Now, says Hamlet, I am the serpent, and Laertes must go away and name some animals. Which animals? asks Laertes. I can't say, answers Hamlet reasonably, until you've named them, can I? So Laertes goes off sulking to find some animals to name. We have no animals in Denmark, he says, kicking the dirt and bruising the knuckles of his toes.

When Laertes is gone, Hamlet turns to me and says, Hello, Eve. I'm the serpent. I don't like serpents. I say. Oh, but you must like me, he says, I'm a very nice serpent. I've come to bring you knowledge. What knowledge? I ask, very suspicious, and beginning to get cold, standing there naked in the garden. Knowledge, says Hamlet, of good and evil. And then he pulls me towards him, and he kisses me, and puts his tongue in my mouth. What on earth are you doing? I ask, pulling away. I'm being a serpent, he says. Serpent tongues do that. Not in my mouth, they don't, I say. Tell me about good and evil. Well, he says-but before he can tell me, my father catches us, and I get a good whipping. Hamlet, of course, gets off with a tongue lashing from the old King, who is rather amused by the whole thing. This by the way was the pattern of our youth, Hamlet would get other people in trouble and then somehow evade responsibility for it.

I always regretted not getting from him the answer about good and evil, it was an important question for me. But my misfortune was that, although I thought much about such things, I tended to keep them to myself, and thus I perpetuated the myth that I was beautiful but not very bright. Gradually I began to go insane. It was not, as some have thought, a direct result of my father's murder. Oh, no, no, such things only give us an excuse to manifest the madness that is already within us. No, the madness began in my childhood, it was the result of my attempts to solve the mystery of the knowledge of the tree of good and evil- I could make no sense of it. For everything around me seemed such a terrible admixture of things partly lovely and partly horrid.

Hamlet was kind and funny and utterly charming and yet cruel and selfish and cold and full of hatred. The Queen was beautiful and kind and gentle and considerate and also blind and foolish and vain and weak. Claudius was ambitious and deceitful and a murderer, but he was also rather more intelligent than the others, well read, a gifted painter, a person who could discuss botany or point out the constellations or recall the name of a poor tailor he had met in the street twelve years ago and ask him about his three children and his wife with the glass eye. He was in many ways a better king than the brother he murdered. And he loved Gertrude with all his heart. He felt that Hamlet was mentally ill and very dangerous, and he was right on both counts. And Laertes loved me with great apparent devotion, but Hamlet's remark about eating a crocodile at my shabby burial service was, I'm sorry to say, much to the point, for in fact I believe Laertes loved the idea of having a sister more than he loved me in particular - in reality I believe his actual attachment to me was more sexual than anything else, he desired me, physically desired me, at least from the day Hamlet cast us as Adam and Eve in the garden.

And then there is Father, my dear father, who often spoke words of great wisdom without, unfortunately, listening to what he was saying, who would give wise counsel mixed with absolute rubbish and never be able to tell the difference, whose love for me I found genuine and touching at one moment, only to be in the next moment utterly forgotten in a storm of peevishness.

They were all such jumbles of contradictions, they made me so angry and confused, I could not deal with one of them in a consecutive way, each time I walked into a room and found one, I had to hold back, to wait and see what face they had put on this day, when what I wanted was to run at them and desperately put my arms around them and hug them, yes, even Claudius or the old dead King, hug them and tell them how hopelessly I loved them, and how fervently I hated them, but it was no use, I could do neither, it would have fallen dead upon their ears.

Now, Yorick, however, Yorick, I sometimes felt, did understand this, or at least some of this, and me, or at least some of me, and much else, perhaps, but Yorick was always drunk, and then he went and fell off the battlements in a stupor one dark night and broke his neck and my heart, and there I was, still a child, and with no one to talk to for the rest of my life. It was one manifestation of my madness, I think, early on, that I would from time to time speak with Yorick, after a fashion, subsequent to his swan dive from the south tower. He would appear to me and I would speak with him, although I could never quite make out what he was saying to me, as he seemed to be speaking under water with a great wad of hay in his mouth. At any rate it was thus to Yorick's probably imaginary ghost that I confided the fact-and only to him-that I was carrying a child in my body.

In a way it had all been Yorick's fault, for we had, as small children, once spied upon him engaging in a spirited act of intercourse with a young serving maid, what was her name? Gretel?

Lord, lord, we couldn't take our eyes off them, at first, but then Hamlet did a characteristic thing, he turned away in disgust, but not me, not me, I watched to the bitter end, in utter fascination. The girl lay there naked like an old painting, she was really quite beautiful, and she touched her face to his shoulder so easily, as if it had all been carefully choreographed, as if God had taught her how to do this before he allowed her to be born, and I wondered if I also knew, if I had her secret knowledge, and if Hamlet had his as well.

And so it was that, some years later, with him suffering, suffering, for the death of his father the old King, and the infidelity of his mother the Queen, and the treachery of his uncle the new King, him so sad, so sad and troubled, and I was going past his chamber, one night I couldn't sleep, and I heard him crying, crying like a baby, him, who I'd never seen cry in his life, not for any amount of pain, not when he broke his arm or when Yorick died or when his father died, even, but then, months after, there, in his room, crying and crying, as if his heart would break, and so I crept in, in the dark, it was very dark and cool in his chamber, and I took off my nightgown, let it slip to the floor, and slipped quietly into his bed, he was so cold, and I knew how, just as Gretel the servant girl had known, God had taught me how and I had forgotten until it became necessary, and there we made the beast together, Hamlet and I, him desperate, me serene, very serene, with the ghost of the old King watching us in the dark, his two red eyes glowing in the blackness, it was after this that he turned on me and began to hate me, what do you think that nunnery business was really all about, you fools?

It was his guilt, his horrible stupid guilt for it, and his anger at me for my compassion, and because I felt no guilt at all, so I could not very well tell him, could I, that I was carrying his child, and so, in the course of time, after he had conveniently murdered my poor idiot of a father, there was nothing left, I could tell, nothing left but to let the madness come gushing out like a freshwater spring, and take a swim in it.

There was a willow grown aslant a brook. Actually I think it was a pond, the Queen was not a stickler for precise definitions, even in her better days. And so I did. Billowed up. Feeling the cool water creep up my legs and thighs and into my body like a snake to caress my child inside, I sang, I sang, and then, and then, gradually, up came the water over my shoulders and up my neck, I shuddered and slid under, so gently, so gently under the cold water, and the dumb Queen watched and did nothing. I had entered into a deeper reality.

Do you know why poor Hamlet loved the players so? Because they made alternative realities. He was not fond of the reality he'd been cast in by time or chance or the great maniacal playwright deity. He was a fool. Much more than Yorick was. I, on the other hand, played out my part to the end. Am I to be succour, or am I to be innocence? This is the heroine's dilemma. But I of course was both and neither.

It's so sad he couldn't appreciate the beauty of it. The beauty in the entire pattern of it. The whole labyrinth as it is traced. The entire play one is cast in, so to speak. I suppose his play was about him not wanting to be in his play. But I had my own play, and it turned out rather well, actually, when seen from the larger point of view that madness or deity affords. That's the beauty of having the privilege of playing a character in one of the myriad of interconnected playlets in the vast dramatic epic cycle which is God's megadrama. You get to be at once vividly and inevitably the person you are cast as, but also, if you are, like me, also rather more clever than the usual player, you get, in another part of your mind, to sense the beauty of the moving action of the play that you are a character in, and of the wondrous intricacy of that play's relation to the larger set of plays with which it is simultaneously being performed. How terrible it is, and how complex and strangely beautiful, as I was saying only the other century to Yorick's ghost, with whom I and my dead child live quite happily as spectators in the dark auditorium, as all ghosts are.

And so, there I am, you see. A bit of rue. A bit of rosemary. Some pansies for thoughts. Death is remembrance, a kind of quiet theatre. And there, in the pond, hung all about, I can still see them, dipping into the water, all about me, mysterious and lovely, I see dead men's fingers.
```

---

## IC-0126: Deaf Day

- Title: Deaf Day
- Author (byline): Leslie Ayvazian
- Work: Four From EST Marathon '99
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: April 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MOTHER
- Teaser before the introduction: No
- Spoken words (computed): 1004
- Already set (do not supply): none

### Source block (context only)

```text
Author: Leslie Ayvazian
Book: Four From EST Marathon '99
ISBN: 978-0822217329
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): April 2001
```

### Introduction (context only: never use it for content warnings)

```text
In the United States, more than 40,000 profoundly deaf children struggle to compete in a hearing world. Deaf children, in many respects, are not all that different from hearing children. They can be fascinated by a passing butterfly . . . devastated by a sudden rainstorm . . . rejoice in digging into a pile of autumn leaves. However, in other respects, hearing-impaired children are definitely distinct from their peers. They have their own way of communicating…their own way of looking at the world . . . and their own way of interacting, both with each other and with the hearing world at large. Their first teachers are, of course, their parents and for this very reason they have a major impact on whether their child faces his/her hearing loss as a disability or as a challenge.

Deaf Day by Leslie Ayvazian.
```

### Performance text (classify this)

```text
[A deaf mother talking to a deaf child, who does not appear on stage. Spoken aloud in English and also in Sign Language]

MOTHER: Ok.
Ready?
Come on!
Sun's up, Day's here. Let's go!
Rise and shine.
That means: "Get up and...be happy!" Come on.
Don't ignore me.
Look at me! Yes!
We have to practice English.
Yes. Today is practice day.
Your teacher said.
So look at me. Look at me!
Put your hearing aids in. Yes!
Now! Good.

Ok.
We're going to the playground.
No, not at Deaf School.
In the Park.
Yes, there will be hearing children there.
I don't know if there will be any deaf kids. You can speak to the hearing children.
Yes, you can.
Sure, you can.
Remember the new boy on our Street? Roger? Maybe we'll see new boy Roger and his Dog!
You can talk to them. Yes!
And to other kids too.
Yes, you can.
You stand in front of them.
Look directly in their faces.
If they look away, say:
[No Sign.] "Could you please repeat that?" [No Sign.] "Could you please repeat that?"
[With Sign.]
Yes, you can!
Say:
[No Sign.] "I can't hear you because I'm deaf." [Continues aloud and with Sign.]
Some will laugh.
Some won't laugh.
Talk to the ones who don't laugh. Come on, honey.
Yes.
Put your shoes on.
Put your shoes on!
I'll put them on you!
Then sit down and put them on! Sit down!

Now tie your shoes.
Good.
Ok.
Get up. Get up! Get up! Look at me!
Don't turn your head away. Come on.
Ok.
I'll wait...
[She waits. She taps her foot.]
Hi.
Yes, I'll stay in the park with you, of course.
I'll sit on the closest bench.
You can talk to me whenever you want.
People may watch you.
And some may think: "WOW! Look at this kid!
He knows two languages! How cool!"
Well, some will think, "WOW!"
Some might be stupid.
We will ignore the stupid ones.
Do we feel sorry for the stupid ones?
Nah.
We think they're stupid.
But, some people will see how wonderful you are.
And those people will want to talk to you.
So, watch their faces.
Read their lips.
If they walk away without telling you where they are going, don't be mad.
Hearing people talk with their backs to each other.
At those times, wave to me.

We will talk.
And then, we'll come home. Yes.
And you can be quiet for as long as you want to be quiet.
No voices. Quiet.
Quiet.
Ok.
You ready?
Hearing aids, turned on!
Eyes open!
Let's go!
No, we don't have to march.
We can walk slowly!
We can walk real slowly. And we'll look at each other. And we'll talk.
In Sign.
We'll talk.
I promise. [Without Sign.] Good. [Without Sign.]
[Lights shift. Lights come up. It is the same day: evening. She speaks aloud and with Sign.]
Hey.
It's almost time for bed! Yes, it is!
And you have sleepy eyes. Yes, yes, yes, you do. But first. . .
Look at me, honey. [Hits floor for his attention.]
[In just Sign.] Look at me! Good. [Continues aloud and with Sign.]
Let's practice English before we go to bed.
Practice Day is nearly finished. Watch my face.
Come on, watch.
Let's talk about the Park.
No. No Roger! No dog. No.
But the seesaw! Yes!

That girl!
No, we don't know her name.
But you two were perfectly balanced!
You sat in the air at the same time.
That's very special.
But the slide. I know.
They pushed you down the slide.
They wanted you to go faster.
They said: "HEY! ...HEY!"
They didn't know that you couldn't hear them. So, they pushed.
They pushed hard. I know.
It surprised you.
And it hurt you. I know.
They pushed you because they were frustrated with you.
But I think you can understand.
Sure you can.
Think about your deaf friends at school
When you want their attention, sometimes you grab them. Sometimes you hit them. Sure
you do. Because you want them to look at you.
And you get frustrated. Yes, you do!
So, next time, if the kids are waiting, you go fast! Ok!
Go fast down that slide.
You kick butt!
Yes!
Then no one will push you.
And no one will laugh.
You need to be fast and quick, quick, quick. Like a bunny.
Yes.

A fast bunny who kicks butt!
That's you!
Yes!
Right! Jackie Chan!
Ok.
[Jumps up and does Jackie Chan stance.]
Jackie Chan!
Auhhhhhh!
[Does Tae Kwon-Do kick.]
We are Jackie Chan!
[Another move.]
But we have sleepy eyes!
Yes.
[Said in Korean, no Sign.] Cha-Ryut. Kyung-Net. [Bows to him.] Tae Kwon-Do.
[Back to Sign and English.] So get in bed, Jackie Chan! And maybe, tomorrow we'll go to
the Planetarium. Or the Zoo?
Maybe the Park.
And you can get back in the saddle.
That means: When you ride a horse and fall off, you need to get back on the horse right
away. So you don't feel scared.
Back in the saddle.
Back in the Park.
Back on the slide.
Ok?
Ok.
Now sleep, honey.
Sweet dreams.
[She waves.]
Sweet dreams.

[She leaves "his room" and sits. She waits. Then she gets back up and goes to his room. She sees he is still awake, but sleepy. She waves again. She leaves and goes back to her chair. She waits.

Then she goes again and checks on him. He's asleep. She returns to her chair and sits. She breathes a sigh of relief Beat. She notices he has walked into the room. She speaks aloud and in Sign]

What's up?
Tomorrow? Stay home? All day?
No voices?
Quiet?
I'm thinking.
[She gets up and sits on the floor]
Ok.
Tomorrow.
Quiet.
I promise.
Yes.
[In just Sign.] Quiet. Quiet. I promise. [In Sign and aloud.] Good night.
[In just Sign.] Good night.
[She sits watching her son. Lights fade.]
```

---

## IC-0127: Dear Husband

- Title: Dear Husband
- Author (byline): Joyce Carol Oates
- Work: Not specified
- Publisher: Ecco Press
- Publication date as stated: April 2010
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: LAURI LYNN
- Teaser before the introduction: Yes
- Spoken words (computed): 1717
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joyce Carol Oates
ISBN: 978-0061704321
Publisher: Ecco Press
Date (Month/Year): April 2010
```

### Introduction (context only: never use it for content warnings)

```text
On the morning of June 20, 2001, Andrea Yates drowned her five children in the family’s bathtub. Then she called 911 and waited for the police to arrive. Born Andrea Pia Kennedy on July 2, 1964, in Houston, Texas, Andrea thrived at Milby High School. She was valedictorian, a member of the National Honor Society, and the swim team captain. However, she also had an eating disorder and considered suicide. As an adult, she would be diagnosed with depression, delusional thinking, and schizophrenia. Still, she lived a relatively stable, simple, and devoutly religious life with her husband, Russell, and their family. But by 2001, Andrea Yates was convinced that she and her children were destined for hell. She came to believe the only way to save her children and prevent Satan from returning to Earth was by killing them — and being executed for the crime.

Joyce Carol Oates boldly reimagines the mental state of Andrea Yates in her fictionalized short story, Dear Husband.
```

### Performance text (classify this)

```text
LAURI LYNN: (Pg 316+) Dear Husband, You alone will know the truth of what has happened in this house, in the early hours 6:10 a.m. to 6:50 a.m. You alone have the right to condemn me. It was my failure as a wife and the mother of your children that is my true crime. I am confessing this crime only to you, dear husband, for it is you I have wronged.

LAURI LYNN: Loell, Jr. was a very happy baby. [He] had such a sparkle in his eyes though he came late to speech and could not seem to hear words spoken to him unless loudly, and you were facing him. It was God’ wish to cause our first born to be as he was. And then God sent us twin daughters: Rosalyn and Rosanna. Bright lively girls with white-blond hair. The twins were closest to Mommy’s heart. And little Paul, with his Daddy’s sharp eyes and wavy hair, and Dolly-Ann, our “sudden gift” from God, born within a year of your second son. All of my life has been our family, dear husband.

You are praised as a draftsman and you work with blueprints out of a computer I can’t comprehend. It is like a foreign language to me. Though in high school I took algebra, geometry, trigonometry. Each semester my name was on the honor roll. [I was] a guard on the girls’ basketball team and at the Christian Youth Conference in Atlanta, I was a delegate in my senior year. You would not remember for you were three years older than “Lauri Lynn Mueller” and popular on the football team. It was unbelievable to me that Loell McKeon would wish to date me, still less to marry me!

Dear husband, this letter will be on the kitchen table. I will dial 911 when it is time. On the counter, there are three knives. Who has placed them there so shiny-sharp, I am not certain. I have swallowed five OxyContin tablets saved out of my prescription, and there are twelve more I am to swallow when God so instructs me. Upstairs, the children are peaceful at last. They have been placed on our bed in the exact order of their age for it is this order in which God sent them to us. Those children are so peaceful!

Dear husband, when the “bad feelings” first began, I would have a dream while awake and my eyes staring open driving out on the highway and my hands would turn the wheel of the car to the right—quick as a lightning-flash!—before any of the children could perceive it, we would crash into the concrete wall at the overpass and all would be over in an explosion of flame. This was long ago it seems when Rosalyn and Rosanna were still in car seats in the back. Later, when Paulie was in back with the twins, it was the station wagon I was driving, and the children were fretting as usual, for a kind of devil would come into them when Mommy was behind the wheel and anxious in traffic. Little Paulie would shriek to torment me, his cries were sharp like an ice pick in my brain!

Your mother said, “Can’t you control these children, Lauri Lynn? It should not be that hard, you are their mother.” In her face there is disappointment like a creased glove someone has crushed in his hand.

At Thanksgiving, I was very anxious. You said, “Why on earth are you hiding away in the kitchen washing dishes before the meal is concluded, why do you behave so rudely, what is wrong with you?” Little Dolly-Ann had diarrhea and the twins could not be seated together for their giggling and squabbling and Loell, Jr. ate so fast, with his head lowered, and was so messy, and Paulie sulked wanting to play his videos and shoved at me saying, “Go away Mommy, I don’t love you Mommy.”

Mother McKeon crinkled her nose saying, “You’d think these children are starving, and nobody taught them table manners, look at the messes they make.”

Dear husband, I have tried to keep them bathed. It is hard to fight them sometimes, for they kick and splash in the bath knowing how fearful I am that the floor will get wet, and the tile will warp, and water will drip down through the dining room ceiling. I have tried to keep this house clean. You would laugh at me, your angry laugh like silk tearing -- but I have tried.

When the police come into this house this morning, I am ashamed of what [they] will discover. The bathrooms are not clean. The toilets cannot be kept clean. The boys’ rooms are not clean -- bedclothes stained. There is a harsh smell of the baby’s diapers and of bleach. The twins’ hair cannot be kept free of snarls. They push at my hands, they whimper and kick, when I try to comb their hair. And so many dirtied clothes, socks and sneakers, and towels. I am so ashamed of what will be revealed to you, after I am gone.

It was my fault. I know that such terrible words would never erupt from your mouth, dear husband, except for me. You said, “Lauri Lynn what the hell do you do all day? Look at this house. You have nothing to do but take care of the children and this house and look at this house, Lauri Lynn. You are a failure as a mother as you are a failure as a wife, Lauri Lynn. Tricked me into marrying you, pretending to be someone you are not.”

And never would you strike a woman. My jaw still hurts, but it is a good hurt. A waking-up hurt. I am so ashamed, yet there is a fascination in it, what I have become. I am not now Lauri Lynn, a plain girl known for her smiles. Where that girl has gone, I do not know. Lauri Lynn is not here, the children scarcely knew her. I am a bad mother, and now all the world will know. My children are flawed and broken like the dolls and toys they break, the stuffed animals they have torn. It is for this reason, I think, that this morning at last I acted, as God has instructed. For now what is done, is done. For now it cannot be undone.

It was very hard to force them, dear husband. I began with Loell, Jr. for he was the oldest, and the biggest. He fought me, I was surprised. When I chased him in the upstairs hallway he ran screaming—he fought me, and bit my fingers, but I was too strong for him, and carried him back to the bathroom and to the tub where the water was just warm the way the children like it, and now there is so much water on the floor, it is leaking through the floor and through the dining room ceiling, you will be so disgusted.

Some parts of what happened, I don’t remember. I remember laying Loell, Jr. on our bed, his pajamas so wet. Jesus said to me, “It is true that you are a bad mother but there is a way: ‘If thine eye offend thee, pluck it out.’” And God instructed me, “Lauri Lynn! You must act now.” The little ones believed it was their bath time. And the promise of bath time in the morning is breakfast. If they do not misbehave, they can have their favorite cereal. It was so very early—not yet dawn!

I will not break down and cry. I will not be ridiculed or pitied. I will not be laughed at. I have done a good job, I think. But I am so tired . . .

One by one I drowned them in the tub, it was not so very different from bathing them, for always they kicked, and splashed, and whimpered, and whined, and made such ugly faces. Some parts of what God instructed me, I can recall, but others are faded already now, like a dream that is so powerful when you are asleep, you would wish to keep it, but when your eyes open, already it begins to fade.

“Mommy!” Rosanna cried but I did not heed her, for the strength of God flowed through my limbs. It was a hard task but needed to be accomplished for the children had not turned out right, that is the simple fact. At birth, some babies are not right, malformed, or their hearts are too small, or their brains, or the baby itself is too small, and God does not mean for such babies to survive. These children did not show their deformities to the eye. God has instructed me, and Jesus Christ has guided my hand. I am a bad mother; I will be punished by the laws of man, but I will not be punished by God for God has forgiven me.

The baby did not suffer, I promise. Like the others Dolly-Ann thrashed and kicked with surprising strength for a five-month infant but could not fight her mother as the others tried to do, and beneath the water little Dolly-Ann could not scream. How many times you have pressed your hands over your ears, dear husband: “Why does that baby scream so? Why is it our baby that screams?”

Dear husband, in Heaven, the children will be at peace. They will no longer be dirty, and squabbling; they will be perfect as they were meant to be. From this day forward, your beloved children are with God.

The twins, I have wrapped in their new plaid coats, to lay on the bed. I brushed out their snarled hair like halos around their heads. The others are in their wet pajamas, and I have hidden their faces with a sheet. In the place where I am going, I will not have children.

I am very tired, it is all that I can do to swallow these pills, and take up the carving knife. You will find another woman to honor and to cherish and to bear your children and they will be perfect.

Your loving wife, Lauri Lynn
```

---

## IC-0128: Dear Sara Jane

- Title: Dear Sara Jane
- Author (byline): Victor Lodato
- Work: The Back Stage Book of New American Short Plays 2005, Pgs 173-180]
- Publisher: Backstage Books
- Publication date as stated: Oct 2004
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SARA JANE
- Teaser before the introduction: Yes
- Spoken words (computed): 1103
- Already set (do not supply): none

### Source block (context only)

```text
Author: Victor Lodato
Book: The Back Stage Book of New American Short Plays 2005, Pgs 173-180]
ISBN: 978-0823088089
Publisher: Backstage Books
Date (Month/Year): Oct 2004
```

### Introduction (context only: never use it for content warnings)

```text
The Dalai Lama once said: “War is neither glamorous nor attractive. It is monstrous. Its very nature is one of tragedy and suffering.” Today it seems as if most of our world is mired in armed conflict: Sudan, Haiti, Gaza, Ukraine – The list seems endless as troops are deployed.

So imagine . . . Your loved one is fighting in a far-away war -- A war with atrocities you can only imagine. When and if they return home, will they be the same person; or will the war have changed them in brutal and irreversible ways? This is the question plaguing the wife of Jerry Housetree in . . .

Dear Sara Jane by Victor Lodato
```

### Performance text (classify this)

```text
A young woman next to a small table. On the table is a human skull, a letter and perhaps a framed mirror. The woman begins the scene regarding the skull, she stares and stares at it.

Finally, she speaks to the audience. She is emotionally agitated, but attempts to appear casual, composed – even lighthearted.

SARA JANE: [Trembling, she picks up the letter from the table, reads] Dear Sara Jane . . . Dear Sara Jane. That's me. Sara Jane. My husband's Jerry. Jerry sent me this. Jerry sent me this skull. In a box.

Dear Sara Jane. That's me. I did not kill him. He was already dead. When we found him, I took his head with my own knife. Not easy. I boiled it down, scraped it, then boiled it again. It is bleached and so it is clean, don't worry. We will keep it. It is terrible but we are winning. I will be home soon.

Who loves you? Do you know? Jerry. Jerry. And Jerry. [puts down the letter, her hands still shaking]

SARA JANE: I love my husband. Jerry. I do. Green eyes. With little bits of copper in them. And his hair, his hair is this wonderful color. Cinnamon. And this deep voice. It rum-bles. Rumbles. Makes you melt. And big, big beautiful hands. And they're always warm. Mine are always cold. Ice. Even in the summer. He must be sweating over there. Cause it's so hot where he is. Very hot. I worry about him. It hardly seems real. All of this. I don't like to watch it. On the television. I turned it on once, and there was this picture, this, this image. Oh, I mean half of what you see is probably not even true. I'm not going to let my children watch it. Not too much anyway. Jerry and I don't have kids yet. We're gonna though. Two or three. He says two. I saw this image. Children running. And it looked like the street was a river. Of blood. Some of the children were bleeding. Some children were dragging other children. Trying to carry them. Maybe they were dead, I don't know, you couldn't tell. And the screaming was like birds -- I've never heard screaming like that. Like a singing, a siren. And the street like a river. And they were running. And I kept thinking, shoes of blood. Couldn't get that out of my head. Shoes of blood, shoes of blood, shoes of blood. [a nervous giggle] Just spinning. Around and around.

I read in the newspaper about this one village -- it was all women and children, just like they say in the movies, you know, to make it very dramatic, women and children -- and they were all killed. Burned. Well, you know, they say even the children are setting traps in the woods. That these children, from a very early age, are taught these things -- how to set these horrible traps that can kill a man. I'm not saying these children in this village were killers. I'm not saying that. I talked to my mother about it. Because I was confused, I was upset. She said: 'Honey, innocent people always die in a war, that's just the way it is. In a war.' And that word! Is it a war, isn't it a war. Oh, my god. They don't stop with that. A war.

I don't really understand the whole thing. You know? I don't get it. This house, it's a beautiful house we live in. We've only been here six months. There's a swing set out back. Rusty, but Jerry says he can fix it up. He's an ace at fixing cars. That's what he was doing. Before he left. He's going back to school when he comes home. He will come home. We're just a couple of miles from the community college. We don't know what he's going to study. Restaurant management, I thought. Oh, I would love to open a restaurant one day. Jerry's not sure. Maybe hotel management, he says. He's smart. He is. You wouldn't think it at first. But he is. He's quick. He's funny. Oh, my god, is he funny. Makes everybody laugh. I mean, how could a person maintain even a basic level of sanity in the middle of all that? All that blood.

And snakes, there's snakes, you know, everywhere. And the screaming.

And explosions. Something happens to your mind. Something must have happened to Jerry's mind to do something like this. Running around in the woods. Not the woods, that's not what they call it. The jungle. I'm not going to pretend a person could maintain their manners in the middle of something like that. In the middle of a jungle. In the middle of a war.

[looks at the skull, touches the eye sockets] This is where the eyes were. One here. And one here. Little eyes. Slanty eyes. And there was a brain in here. And skin. Tongue. Lips. Just like a regular person. Eyebrows. Hair. Ears. He did it all himself. Jerry. Cleaned it up. All of it. Yes, he did. Oh, my god. And he did a good job, didn't he? He's an ace at cars. With his hands.

I love my husband. I do.

I mean, how do you ever really know another person? Really know them. I have secrets. Sure I do. Even from Jerry. I have dreams. I have ideas. Things you'd be embarrassed to say. But you know what? When Jerry comes home, I'm gonna tell him everything. Everything. I'm not gonna be embarrassed to tell him anything. And I want him to tell me everything. I mean, my god, how could he? Because two people should tell each other shouldn't they? They should tell each other every little thing.

So there's nothing between them. Because doesn't it feel sometimes there's a life inside you and it's trying to come out, it's trying to find its way out. So you have to talk about these things. Where have we been? Where are we going? Because you don't want to get lost. I want to have everything in order. Everything in order. When Jerry comes home. Because that's when our life starts, doesn't it?

I just wish I could fall asleep. That's the thing. Just a few hours of sleep. [pause] It's so quiet in the house. Oh my god, it's so quiet. [looks at the skull] And this one -- this one -- says nothing.

Who loves you? Do you know? Take a guess. Jerry. Jerry. And Jerry. [looks at the audience] I'm so scared. I'm so scared. I'm so scared.
```

---

## IC-0129: Deja Vu (Again)

- Title: Deja Vu (Again)
- Author (byline): Cole Kazdin
- Work: The Moth Presents All These Wonders, Pgs 112-118
- Publisher: Crown/Archetype
- Publication date as stated: March 2017
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: COLE
- Teaser before the introduction: Yes
- Spoken words (computed): 1651
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cole Kazdin
Book: The Moth Presents All These Wonders, Pgs 112-118
ISBN: 978-1101904404
Publisher: Crown/Archetype
Date (Month/Year): March 2017
```

### Introduction (context only: never use it for content warnings)

```text
50 First Dates, a comedy starring Drew Barrymore and Adam Sandler made us all chuckle. Every morning, Drew’s character, Lucy, woke up with no memory of what had occurred before she slept. She remembered people, she remembered how to drive, but painted the same mural day after day after day; her family whitewashing her work each night as she slept. It was cute, it was funny . . . it was devastating.

Cole Kazdin gives us insight into life with amnesia in Déjà vu (Again)
```

### Performance text (classify this)

```text
COLE: (Pg 112-118) I wanted a fresh start. I was living in New York. My boyfriend, Adam, had just broken up with me and moved across the country to Los Angeles. Neither of us had done anything horrible, like have an affair. We just weren't a good fit.

But Adam and I were both just passive enough to keep it going. If things got bad, and one of us might begin to muster the courage to pull the plug, then it would be one of our birthdays. Or we’d get really great concert tickets. And that would keep the relationship going for a few more months. And months turned into years.

In three years, Adam never told me he loved me. I think I loved him, but I wasn't going to say it first. (Because I'm so mature.) Then one night Adam took me out to this beautiful dinner. He told me he cared about me very deeply . . . And that he never wanted to marry me. It was essentially a reverse proposal.

COLE: And that was it. He broke up with me, he moved to Los Angeles, it was over. And it was so painful for me.

I remember just wanting to forget him -- forget the past three years and just wake up one morning and start fresh. I got my wish.

I woke up in an ambulance, wearing a cheerleading outfit (which, if you're over thirty and it's not Halloween, raises questions, you know?). There were EMTs all around me, and then I was being placed into a CT scanner, and then I was in this hospital room with all these concerned strangers gathered around me.

But they weren't strangers. I just couldn't identify them. What I didn't know was that earlier that day there’d been an accident. I’d been filming this television pilot. It was a movie spoof show. The pilot was a parody of Bring It On, the cheerleading movie. We were asked to do a stunt that we never rehearsed.

The stunt was I was to be thrown high up in the air and caught. . . I was thrown high up in the air . . . but I landed on my back and my head. I suffered a massive concussion and a slipped disk in my back. I could barely walk, and I had no idea who I was.

Diagnosis: amnesia.

So I also didn't know that my boyfriend had dumped me a few weeks before and moved to Los Angeles. I didn't know anything.

In the hospital someone put a phone up to my ear and told me it was my mother. I heard this frantic female voice on the other end of the line, and it meant nothing. A friend knew where I lived, took me home, dug the keys out of my purse, got me into my apartment, and put me into bed.

I wanted to call my dad. I remember having that thought. My friend said, "Why don't you rest? We can call him later."

But I wanted to call my dad, and I needed help, because I didn't know the number. Again my friend kind of put me off. "Why don't you rest? We'll call later. Sleep a couple of hours." I started getting frustrated. "Why aren't you helping me? I want to call my dad!" My friend was looking at me like I was out of my mind. Finally he said, "Don't you remember? You just called your dad. You've talked to him three times. We've done this three times. So you can call him, but it'll be the fourth time. And I'm just worried we're starting to freak him out."

I had both short- and long-term amnesia. So I knew some things: I knew how to speak, and I knew how to read. But I didn't know the big stuff, like who I was. I also couldn't retain anything. So if someone left the room and came back ten minutes later, we had to start over. I was living quite literally moment to moment.

Everyone that came and went, they were just strangers to me from a past I didn't even know existed. They tried to help. I remember my best friend, Amy, stormed into the bedroom, screaming, "She's a vegetarian! Don't let her eat any meat!!" That sounded familiar, but it didn't mean anything. I mean, I could have been gnawing on a veal shank. But it sounded important, and I didn't want to forget it, so I wrote it down. There was a pad of Post-it notes on a table next to my bed. I wrote, "You are a vegetarian."

Someone had called Adam, and he flew in from L.A. right away and was at my bedside with tears in his eyes. In fact, the first night he slept in my bed with me, which I remember was kind of weird and, I thought, presumptuous because, like, Who is this guy in my bed? He said he was my boyfriend, but he could have been the mailman. I don't know - I've got amnesia.

The next day Adam showed me pictures of us together, to see if maybe that would jog my memory (and maybe even to make a case for the fact that we were a couple). Pictures of a recent trip I had taken to L.A.: Adam and Cole at the beach, Adam and Cole in front of Mann's Chinese Theatre, Adam and Cole in the Ferris wheel on the Santa Monica Pier. I was in the pictures, but I remembered none of it.

I wrote down everything. I was terrified of forgetting. Every piece of information was precious. Anytime someone told me something, or on the rare occasions when something might come back on its own, I wrote it down.

"You are a vegetarian." "We are at war with Iraq." "Kristen is your friend."

One afternoon I was in a cab, coming home from physical therapy, going over the Queensboro Bridge. I noticed the hole in the skyline where the Twin Towers used to be. My accident happened in November of 2001, and this was a month or so after that.

I thought, That's funny . . . I wrote it down on a Post-it: "Twin Towers gone."

Adam was the Wonderful Boyfriend. This accident was the best thing that could ever have happened to our relationship. He moved into my apartment. He took me to my weekly neurologist appointments and almost-daily physical therapy. He doled out my medications at night and then held me when I woke screaming in the middle of the night from the nightmares that those medications gave me. Or from the sheer disorientation of not knowing who or where I was.

A girl from yoga visited. I do yoga? What else do I do? I was on this detective mission to find out who I was.

I found journals written in my handwriting, in another language. Adam told me it was Portuguese from when I lived in Brazil. I lived in Brazil? Cool. What else? Do I paint? Can I cook?

I overheard doctors saying things like, "We don't know how long she's going to be like this" and "We're not sure if she'll ever fully recover." And they're talking about me. I mean, I'm sitting right there in the room.

The only thing I could be sure of was this growing pile of Post-it notes on my bedside table. I thought the bigger that pile got, the more of a person I became. But it still wasn't me. It was just information, filling an empty space.

Then one afternoon I was in a cab coming home from physical therapy, going over the Queensboro Bridge again. I started to cry. I had no idea why. But I couldn't stop. And it was right as we passed the hole in the skyline where the Twin Towers used to be. When it first happened, there was that really chilling empty space, like ghosts of buildings.

I felt flooded. I mean, I wailed. And I couldn't figure it out. And then it came to me: I was remembering. But it wasn't a fact or a thing - it was a feeling. It was the first time since the accident that I felt real.

That night Adam was tucking me into bed. He had just given me my medications, and he was writing it down on a Post-it note, for when in five minutes I asked if it was time for my medications, as I did every night.

I watched this man taking such wonderful care of me, and I was overcome with emotion.

I said, "I love you." And he said nothing. So I said it again (because I had amnesia and I could get away with that).

"I love you." Again nothing. I didn't understand . . . And then I remembered. The breakup and all the pain that went with it. His move to L.A. Then a post - 9/11 reconciliation. September 11 happened, and we were going to give it one more try.

I went out to L.A. to visit him. We went to the beach, and we went to Mann's Chinese Theatre, and we rode the Ferris wheel at the Santa Monica Pier. I thought of everything he was doing for me. If this wasn't love, what was? Why was he even here? And I think the answer is, he's a good, good man, and he cared for me very deeply.

It took about six months for me to recover. My memory just came back slowly over time. And then I must have been fully healed, because a few months after that, Adam and I broke up again. Only this time I knew it was coming because we'd done it before.

I wanted this fresh start. And I got it. I lost myself completely, and then got myself back, almost as if following a script, replaying my entire history with Adam. Nothing had changed.

But this time, that was comforting. Because if nothing changed, it meant I knew who I was. That I was a real person. And that even without my memory, I was still me.
```

---

## IC-0130: Disturbed

- Title: Disturbed
- Author (byline): Brad Bosen
- Work: Millennium Monologs: 95 Contemporary Characterizations for Young Actors, ed. Gerald Lee Ratliff - Daphne’s Monologue Only, Pgs 147-149
- Publisher: Meriwether Publishing
- Publication date as stated: Nov 2002
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BOB, DAPHNE
- Teaser before the introduction: Yes
- Spoken words (computed): 2490
- Already set (do not supply): none

### Source block (context only)

```text
Author: Brad Bosen
Book: Millennium Monologs: 95 Contemporary Characterizations for Young Actors, ed.
Gerald Lee Ratliff - Daphne’s Monologue Only, Pgs 147-149
ISBN: 978-1566080828
Publisher: Meriwether Publishing
Date (Month/Year): Nov 2002
Full play can be found here: https://www.geocities.ws/quietharry/pboese02.html
A note from the playwright: Monologues may be used at no cost and without prior permission for
classes, competitions and auditions, as may small scenes used strictly for classroom or competition
purposes. If you do use any of my stuff for auditions, classes and such, though, please e-mail me
and tell me how it went for you at mulberries@bjboesen.com
```

### Introduction (context only: never use it for content warnings)

```text
Emotional scars, although they may heal over time or are invisible to the world at large, never really disappear. But we develop coping mechanisms to deal with the pain and to protect ourselves. We build walls – much like this imaginary wall dividing Daphne and Bob from the babies on the other side. An invisible glass wall built for safety. But these coping mechanisms – these walls – are they healthy or are they merely survival techniques to cover up the fact that we are all, in our own way . . . Disturbed by Brad Boesen

DAPHNE: [a bit hesitant] Are you alright? [Silence. Bob continues to stare ahead] Sir? [growing

more concerned. Agonizing over whether to help or leave him alone, she softly touches his

elbow. He looks at her and she quickly pulls her hand back] I'm sorry. . . Are you alright? You
```

### Performance text (classify this)

```text
The nursery of a city hospital. The audience is where the babies would be. The actors are on the other side of the "glass" Daphne is peering out at the audience happily cooing and making faces at the "babies. Bob enters. About the same age as Daphne, he is obviously in a very dark mood. He stares blankly at the babies, seemingly oblivious to Daphne's continued antics. Daphne, sensing Bob's depression, begins to include him -- pointing him out to the babies, making grouchy faces, trying to improve his mood until a long, mournful sigh from Bob stops her.

look. . .

BOB: Yeah. [he looks at the babies, senses she's not convinced, turns back] I'm fine. [flashes an unconvincing smile and turns back towards the babies]

DAPHNE: [playing along] Oh. . . ok. . . well, good. [uncomfortable with the silence, but not wanting to leave, she decides to fill it] I love babies. I come here almost every day to look at them. I work right across the street. At that little diner. By the time lunch break rolls around I'm so tired of all that food I just don't even want to think about eating, so I come over here and look at them. [one of the babies does something cute] Ahhhhhh! Look at him! [laughing, rattling a box of tic tacs, and talking to the baby] Hellooooo. Hello in there.

BOB: [watching her this time. More incredulous than angry or annoyed] Are you always this cheerful? [she pauses, uncertain how to react] I mean you just keep babbling at them like. . .

DAPHNE: They're cute! Don't you think they're cute? [Bob considers the babies for a moment, shrugs as if to say "sure, if you say so. Daphne begins replacing items in her purse she has been using to amuse the babies. One of the items is a pack of gum, sensing a possible conversation starter, she offers some to him] Gum?

BOB: No, thanks.

DAPHNE: It's Juicy Fruit. [Bob shakes his head "no"] It's alright, really, I've got plenty. I've got kind of a sweet tooth. A whole mouth full of them actually. [beat. Daphne senses Bob’s depression] My mom always used to say that all you have to do to chase away the blues is look at a sunset. . . or a flower. [pause] The beauty of God's creation. [pause] Then she'd down another fifth of vodka and pass out on the couch. [She laughs. Bob walks downstage closer to the babies. Daphne watches him] It's a valid concept, though, when you think about it. . . the sunset, not the vodka. Although, I suppose. . .

BOB: My wife died today. [silence] In childbirth. . . She and the baby both.

DAPHNE: [softly] Oh, my. . . Oh my God, I'm. . . Really? I mean. . . I'm sorry. [pause. Bob turns, sees her expression and bursts out laughing. Daphne is frozen in confusion] What?

BOB: [laughs even more hysterically at this reaction] I'm sorry. [still laughing] You just kept yammering.

DAPHNE: You were joking?

BOB: [nods his head, wiping tears from his eyes] I'm not even married! [more laughter]

DAPHNE: That was. . . HORRIBLE! How COULD you. . .

BOB: [laughter finally dying down a bit] Oh, come on. What? [Daphne turns away] It was a joke! Come on! If you could have seen the look on your face. [He bursts into laughter again] I'm Bob, by the way. [he reaches out as if to shake hands]

DAPHNE: I have to go now, Bob. [she turns to leave, Bob moves with her, blocking her path]

BOB: What? Come on! It was a joke. I was making conversation.

DAPHNE: CONVERSATION! THAT is NOT "making conversation"! THAT was. . . sick!

BOB: Oh, please. . . come on! You were boring yourself with all that crap about babies and the "beauty of God's creation"!

DAPHNE: Ok. Fine. But I really need to leave.

BOB: I'm sorry, ok? I'm sorry. I may have been slightly. . . inappropriate, but at least it got us talking. Right? Lunch break can't be over yet, you just got here. We'll talk. [Daphne clutches her purse to her chest and looks around for another way out] You can look at the babies. You Look at them. Aren't they cute? [she looks at the babies, smiles] My sense of humor takes a little getting used to. Ever since I was a kid. Drove my teachers crazy.

DAPHNE: Well. . . [polite smile-still wary] Well, I'm glad I could help you out of your mood. When you came in, you seemed so. . .

BOB: Oh, That. It's nothing, really. I think too much. You can loosen your grip on that purse if you want.

DAPHNE: Oh! I was just. . . I'm sorry. I, um. . .

BOB: Relax. You're perfectly safe. I'm weird, not violent.

DAPHNE: Well. . . [she tries to relax, without much success]

BOB: There you go. [long, uncomfortable pause]

DAPHNE: So. . . Um. . . Where are you from, Bob?

BOB: Here. Well, not here. I mean not from this hospital. [nervous laugh. Daphne nods politely] I just meant here in town. I've been in that diner you work at. You probably don't remember me.

DAPHNE: Well, I. . .

BOB: No, no, I understand. It's a busy place. [she nods] You're cheerful there, too. I mean, you have to be, right? You're grouchy, you don't get tips. But it's like you enjoy it or something. [she smiles] I mean it can get on your nerves after a while. . . Always cheerful. Always. . . up. Like with the babies before. [she smiles and looks at the babies. She can't resist a little wave. Bob shakes his head] Years from now they'll probably all be in therapy. [she looks at him] Recurring dreams of a huge lady rattling tic tacs in their face. [sees her reaction--quickly] I couldn't do it. Be cheerful all the time. So, where are you from, Daphne?

DAPHNE: [surprised, slightly wary] You know my name? [Bob points to the name tag on her chest. She's still dressed for work] Oh! Oh, of course, [my name tag]. [laughing] I'm sorry. I'm from Nebraska.

BOB: Nebraska. Wow. I bet they're all like you in Nebraska. Happy, smiling. . . riding horses, milking cows.

DAPHNE: I've never been on a horse in my life. And I've never touched a cow.

BOB: Sure, sure, I believe you. [small pause -- smiling]

DAPHNE: You've never been to Nebraska, have you?

BOB: No. But I've read about it. -- Stephen King. "Children of the Corn." And "The Stand". . . that old lady that talked to God. She was from Nebraska.

DAPHNE: [joking] If you went by those books, you'd expect everyone in Nebraska to be like you.

BOB: What do you mean?

DAPHNE: [slight pause--unsure if she's insulted him or if he's kidding] I don't know.

BOB: What am I like?

DAPHNE: I don't know. Nothing.

BOB: No, really, I want to know.

DAPHNE: I'm sorry. I didn't mean anything. You're just. . . dark, you know [very uncomfortable, struggling for words that won't insult him] somber. . . spooky.

BOB: What do you mean, "spooky"? And somber? What's somber?

DAPHNE: [throughout the following lines, Daphne becomes increasingly anxious and uncomfortable] I don't even know you. . .

BOB: What kind of word is "Somber"?

DAPHNE: I'm sorry, I just. . .

BOB: Calling a guy "spooky" and "somber"

DAPHNE: LOOK! YOU ASKED! [silence] I mean, I'm sorry if I insulted you. [pause] What are you doing here, anyway? Why are you bothering me?

BOB: I didn't know I was bothering you.

DAPHNE: I was having a perfectly good time, and then you come in here. . .

BOB: [overlapping slightly--interrupting] I'm visiting someone. [small pause]

DAPHNE: Oh, right, your dead wife and child. I'm so sorry.

BOB: I'm visiting my father.

DAPHNE: [not believing him] Your father.

BOB: He's. . . not doing well. I thought, maybe if I came down here, maybe the kids would cheer me up or something.

DAPHNE: Uh huh.

BOB: Look, I'm sorry I said that before, about my wife and kid, it's just. . . well, I knew you were going to ask, sooner or later, why I was here, and I didn't want to talk about it. Ok?

DAPHNE: [still skeptical, but what if he's telling the truth?] What's he got? [pause -- Bob looks at the babies] I'm sorry. You don't want to talk about it. I'll just. . . [turns to leave]

BOB: He shot himself. [silence] I found him this morning. [long pause--Bob stares ahead, expressionless]

DAPHNE: Oh, Bob. . . Um, you probably want to be alone. [turns again to go]

BOB: [when she's almost out the door] He left a note. [she stops] They always do that in books, you know. In movies. They always have some big message. . . something meaningful. You wanna know what his said? It said, "Bobby, you're the man of the family now. Take care of mother, and always remember [pause] people from Nebraska will believe anything you tell them." [pause]

DAPHNE: No. [Bob turns and smiles at her] Oh, no. [Bob bursts out in laughter. Daphne is shaken and enraged] You are SICK!

BOB: Oh, come on! You wanted spooky.

DAPHNE: I did not WANT spooky!

BOB: [still laughing] Look, I'm sorry. [she turns away] I couldn't resist. It was a joke.

DAPHNE: How could you say something like that? About your father?

BOB: What's the big deal? You never told a joke about your father? Come on. [she turns to face him]

DAPHNE: You want to hear a joke about my father? One night, when I was twelve years old, my father decided to decorate the house for Christmas. About a week before Christmas, dad went out and bought up all of the lights and decorations he could find. There wasn't much left, but he still got a lot. One store owner was so glad to get rid of everything so close to Christmas, that he threw in an old mannequin and Santa costume that had been cluttering up his storeroom. Dad built his whole display around it. [pause--smiles at the memory]

We didn't have a big chimney like you see in movies, so he put Santa on the roof of the porch, peering into the window of my parents' bedroom. Around all of the windows, he put red lights. Green lights around the edge of the roof. And combinations criss-crossed up and down in all the bushes and trees. . . It was beautiful.

I remember it was really cold that year, so he did all this with these gloves and a huge coat. I couldn't imagine how, with all those heavy clothes on, he could climb up that ladder and hang all those lights, but he did. And in between each string of lights, he would come down the ladder, pick me up off the ground, spin me around, and sit me up on his shoulders to get a better look. It took almost a week to finish it, but when he finally lit it all up, the whole town came out to see it. Everyone! I was so happy. I was sure that this was going to be the best Christmas in the history of Christmases; living in this. . . cocoon of color and light, with the rest of the world lining up outside to admire it.

On Christmas eve, dad went downtown to this bar that he used to hang out in. He liked to spend Christmas eve with his buddies, because, on Christmas, all the aunts and uncles would be over, and I guess being hungover gave him an excuse not to be a good host. [small pause] By the time he got home, it was past midnight. Mom had turned out all the Christmas lights for the night--she couldn't sleep when they were on, because they would shine in through her window--so the only light was from the streetlight at the end of the block, and, I guess, in the darkness, after drinking all night, dad forgot about the Santa mannequin. . . mistook it for a burglar or something because I woke up to hear shouting on the lawn. . . gunshots. . . breaking glass.

I ran into mom and dad's room, because I didn't know what was happening, but mom and dad weren't in bed. And it was cold, like someone had left the window open, so I looked. . . and there was my mother, just lying there on the floor, in the middle of all this shattered glass and blood. She must have been standing at the window when. . . [pause--Bob is frozen. Daphne stands staring into space--reliving the story] and I just stood there. . . I couldn't move. It was like a dream.

But then I heard the front door open, and footsteps running up the stairs. I was terrified. I thought that whoever had been shouting on the lawn must be coming to get me now, and there was no place to hide. The only thing I could think to do was lay down beside my mother and play dead. I thought whoever it was wouldn't hurt me if they thought I was already dead. So, when dad got to the door of the bedroom, he saw me and my mother and all that blood, and. . . he said. . . something. . . it didn't register at first, I was so scared, and concentrating so hard on not moving. . . and then he stumbled backwards out of the room, and I heard him crying and saying, "No, no, no,". . . over and over again. "No, no. . ." [pause] and I recognized his voice. It was dad. But before I could say anything there was another gunshot. [pause] And then he wasn't crying anymore. [pause] I guess he didn't have time to leave a funny note like your dad.

BOB: Oh, God I'm. . . I'm so sorry.

DAPHNE: Well, thank you, Bob, but right now I just really would like to be alone with the babies if you don't mind.

BOB: No. No, of course. I'll just. . . um. . . [he begins to exit; turns back, can't think of anything to say. Exits.]

DAPHNE: [doesn't watch him go, but stares ahead at the babies. She stands expressionless for a moment then smiles at something one of the babies has done. She laughs and waves with her index finger] Hello. Hello in there. Ahhhhhhhh! [laughs again -- still speaking to the baby] Try and ruin my day, will he? Well, that'll teach him teach him, won't it. Yes it will. [continues to coo, wave to the babies as the lights slowly fade to black]

Acting notes from the playwright: Though it would seem to be the easy assumption to make (and EVERYONE seems to make it), I think it's much more interesting if Daphne's story *isn't* just a joke. In other words, her story is true, but she still uses it to get back at Bob for what he's done to her. The original inspiration for the piece was my belief that people who are always extremely cheerful and "up" all the time are often the most screwed up people you could ever meet. I think Daphne is the most "disturbed" person in this play, not Bob.

That being said, I still leave it completely up to the director and/or performer to decide on whether her story is true or not. Either way, the audience and Bob must believe every moment of it. My goal was for the audience to leave the performance still wondering if she (or Bob) was actually lying. Whether or not YOU believe Daphne's story, the audience should still be wondering when they leave your performance.
```

---

## IC-0131: Dreamland

- Title: Dreamland
- Author (byline): Sarah Dessen
- Work: Not specified
- Publisher: Penguin Young Readers Group
- Publication date as stated: May 2004
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CAITLIN, CASSANDRA, MOTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1393
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sarah Dessen
ISBN: 978-0142401750
Publisher: Penguin Young Readers Group
Date (Month/Year): May 2004
```

### Introduction (context only: never use it for content warnings)

```text
As humans, we may want to focus on reality but sometimes catch ourselves. . . daydreaming. Daydreaming has the power to take us away from pushy parents, a difficult class at school, or work. But what if this semi-conscious dreamland is suddenly turned into a living nightmare?

In this selection, a nightmare slowly overtakes Caitlin who seeks out Rogerson as an escape from her reality: A missing sister, a withdrawn mother and an overall lackluster life. But she soon comes to realize that semi-conscious dreamlands aren’t always an escape.

Dreamland by Sarah Dessen
```

### Performance text (classify this)

```text
CAITLIN: My sister, Cassandra, had been the best at everything, even when it came to boys. She’d spend hours on the phone at night telling her latest boyfriend goodbye, this involving about twenty-I love you’s and pet names like “my little pumpkin“. Little did we know she was planning on leaving to be with her latest in California.

CASSANDRA: Oh, Caitlin, someday this will happen to you! You won’t feel like you’re missing out!

CAITLIN: God, I hope not. If I act like that, be sure to put me out of my misery.

But that was before I met Rogerson Biscoe. He was standing next to this black BMW; brown mass of curls; so mysterious and very different. I had never seen any other guy like him and at that moment, I could see myself setting across uncharted territory, places I’d never been or seen or even heard of. My world was suddenly wide and limitless, and I was ready.

CAITLIN: I was hooked on him. With Rogerson I was someone else. There were so many things I already loved about him. The smell of his skin, the way he pressed his hand in to the small of my back, whenever I walked into any place with him. And he was so attentive, always keeping one eye on me regardless of what else he was doing.

Since Cassandra was gone, my parents thought it would be good for me to join something. My making cheerleader changed my mother’s life. But the truth was, I hated cheerleading.

Whatever pep the other girls had was missing in me, like a genetic or chemical malfunction. I felt like an imposter, and it showed. And after Rogerson and I started going together, cheerleading meant nothing to me.

Rogerson was always there. He drove me home everyday. And we never really went on dates. With Rogerson, it was all about being in motion. Going from party to party, place to place. And, of course, there were the drugs. Rogerson operated a brisk business selling pot and other various illegals to the kids around town. The more I was around Rogerson, the less I became involved with my friend Rina and cheerleading.

Sometimes, however, Rogerson wouldn’t talk and he just wanted to be near me. It was never clear. But I did know this: he was quiet and never spoke without thinking. That he drove like a maniac. That the only time I saw the small simmering of temper behind his cool demeanor was when someone was late or not where they said they’d be. He was punctual to the second.

And I guess that’s what made my perfect relationship slide on through. Everything was perfect... before I missed his ride to the Winter Athletic Ceremony at school. Before he hit me. It was like a crack, like a gunshot. And it wasn’t like in the movies, where the person just stands there and takes it. I reeled back hitting my head against the seat of his car. He acted like what he had done was my fault. And after that, he drove me home, like nothing had happened, nothing at all.

It was during this time that I took up photography. Despite the fact that cheerleading was going from bad to worse, taking pictures was the first thing I had done in a long time that I was truly proud of. Until Rogerson saw me talking to my photography class instructor. He punched me in the jaw as soon as I got in his car. I convinced my mother when I got home that I had “slipped on the ice” by the mailbox.

MOTHER: It’s just so red. You must have hit so hard.

CAITLIN: I felt as if I couldn’t tell anyone about Rogerson-as long as I didn’t say it out loud, it wasn’t real.

As if by silent agreement since that night, Rogerson had taken only to hitting me where I could cover it. I wore only long-sleeved shirts, big sweaters, and turtlenecks, but at least now my face was off-limits.

On Christmas Eve, he gave me this beautiful silver necklace and that night, I slept with him for the first time. It was then that I gave him all of me, believing that I could trust him.

There was no pattern, no way of knowing when to expect it. Whenever he did hit me, I could count on a 24-hour safe period, which I had come to rely on, like home base. Those were the good days. But no matter what we were doing, the fact that he hit me was always on my mind.

One day, he was working on his car and I glanced at my reflection in the chrome of the bumper in front of me: skinny, long baggy shirt hiding the bruises across my skin and bones like a road map of all that had happened, every mile of the journey. And it was getting harder to hide.

See, my family always has this April Fool’s Party in the backyard, a small neighborhood get-together and my mom was just so determined to get me to wear this short white swooshy-skirted dress. It was beautiful, the kind of dress you wore with bare legs, uncovered arms, and white strappy sandals.

MOTHER: I’m concerned, Caitlin. All you ever wear now is black. An occasional red or white, but that’s it. You know how nice you always looked in blue.

CAITLIN: And I kept thinking, ‘I still do, look here, on the back of my wrist, those two spots the size of fingertips. Or here at the base of my back; that’s blue, too.’ I looked up into her face, but she didn’t seem to see me, even as I pleaded that she would.

My parents had no idea until the night of that party. Rogerson and I were supposed to hang out that day, but Rina had kidnapped me, taking me to the lake. I tried calling him, many times, but he just wouldn’t pick up.

I arrived home late, and his car was already parked in front. It didn’t take him long to start grabbing at me, pushing me around. His fist came and hit me right over my left eye and that’s when I slid down onto the grass and stayed there. I tried rolling away from him, but everything hurt all at once; my face, my fingers, the back of my head, the skin itself. Each place he’d ever struck me, like old war wounds on rainy days.

He was still pleading with me to get up when my mother came running outside. She wrapped her arms around me, trying to find a spot that wasn’t hurt. And even after my father called the police and they led Rogerson away, I still pulled out of the hands of all my family and friends, sobbing, screaming, everything hurting, to try and make him stay.

After that night, when my dreams of Rogerson were finally shattered, I was admitted into the Evergreen Care Center. The irony in this is just a few years back my sister and I had made fun of their slogan, “We can’t heal you at Evergreen, but we can help you heal yourself.“ I’d cried for Rogerson and for myself. How had I let it get so far? It was easier to take the days in tiny swallows, rather than biting everything off at once, and I was learning how to heal myself day by day with the help of my many visitors who cared so much about me.

A month went by and they finally decided I was well enough to go home. Before stepping outside my room, I looked up at my mirror. I looked so different from the day I’d arrived. I’d gained weight, my hair was longer, my skin clearer. I lowered my camera to my waist, tilting it upward. Then I put my finger on the shutter and smiled at the girl in the mirror. She smiled back, and I knew she understood it all, what I had gone through to make it this far. This is who I wanted to be. This was the person who I needed to become. So I kept my eyes on hers, steady, and pressed down on the button of the camera to catch this final face.

Click.
```

---

## IC-0132: Dressing

- Title: Dressing
- Author (byline): Mona Mansour and Tala Manassah
- Work: Facing Our Truth
- Publisher: Samuel French, Inc.
- Publication date as stated: 2015
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SON, MOM
- Teaser before the introduction: Yes
- Spoken words (computed): 771
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mona Mansour and Tala Manassah
Book: Facing Our Truth
ISBN: 978-0573704260
Publisher: Samuel French, Inc.
Date (Month/Year): 2015
```

### Introduction (context only: never use it for content warnings)

```text
For years now, many of us have supported the movement to “pull up your pants” but have not looked at how the judgment and condemnation of Black youth, be it hoodies or sagging pants, is directly linked to racist stereotypes.

In fact, after the Tayvon Martin shooting in 2012; a message was sent by the media warning parents not to let their children wear hoodies. Why? Because it sends a sinister signal. You see, 17-year-old Tayvon Martin was wearing a “dark hoodie,” which led a George Zimmerman to conclude that he was a “suspicious guy” and ultimately led to Martin’s shooting death.

Hardworking or lazy; trustworthy or dangerous: People too often make assumptions about someone's character and personality based solely on how they're dressed. What we must realize is a tailored suit does not mean innocence, nor do sagging pants or a hoodie mean guilt. Dress is not a reason for someone to be to be condemned nor it is a reason for someone to be harmed.

Dressing by Mona Mansour and Tala Manassah
```

### Performance text (classify this)

```text
SON: Part one: He’s off to school. His pants hang low – This is an issue.

MOM: (grabbing a belt loop on her son’s pants, which are hanging low. They engage in a conversation, having fun. They like this ritual) This is an issue. Do you know where it came from? This style, this – symbol. It’s a symbol of . . .

SON: (Wresting away and readjusting his pants to the lower level) I know. Prison. Prisoners aren’t allowed to have belts. See? I remember.

MOM: Right. And the pants sag. Which even just symbolically plays into

SON: School-to-prison pipeline, all that . . . (Smiles) But I have 3.8. [GPA] (Mom smiles. He pulls his pants back up to appease her) Okay? (laughing) Just leave it, please?

MOM: I just worry . . . It feels symbolic to me. A competition over who has the best armor. (he pulls on a t-shirt) And what is this? I don’t understand why you can’t wear the ones I got you.

SON: The button-up-the-front things? Yeah. Not today. (She gives him a look) Another day . . .

MOM: Um-hmm, when’s that?

SON: When I turn into a Jehovah’s Witness and go door to door selling Bibles. (He laughs and exits)

MOM: Part two. No. Not part two. Not yet. I can’t. I’m gonna – Just talk for a minute. About other things . . . I used to take him to tae kwon do – I’d stand with all the other parents in the window, watching, these wiggly little bodies punching, you know, they look ridiculous. And it’s the same routine every time. But you stand there. These parents who say EVERYTHING THEIR CHILD DOES IS MAGICAL? They are lying. And I mean, I coulda done other things with my time. We both could have. But you want to create a foundation.

Give him that mental-physical discipline.

So once when he was like eight or so, I left to take a call, I’m gone fifteen minutes, maybe?, I come back, and suddenly he’s doing these kicks, these crazy double kicks. He’s two feet off the ground. Suddenly everything’s coordinated. He’s like a little pro. Now how did that happen? Two years of these lessons and nothing seems to click.

And I think: Was I watching him too hard?

Did my leaving help him to make that leap? Did he need me to stop watching just so he could stretch that way?

You have to be able to look away, to turn around, to let go. But how? (and she doesn’t want to, but she says . . . )

Part Two. The mother gets a phone call. (We hear 3 loud pops . . . a long beat)

You have to so gee – Someone drives you. And as they drive, you remember the pain of childbirth, the tenuousness of those first moments, you remember small eyes, and small gasps, and the very tiny hands that reached for you. Tiny hands reaching.

You don’t remember how you got here. To this building. But somehow you know exactly where to go.

Cause we’ve been doing this dance, right? We know how to do this! We know where to go, we know how to behave! And they take you into this room, and then another one, and another one, and your legs move, something primordial moves you forward, and you dig your nails into your hands so you won’t feel anything, and it’s not YOUR body that moves you forward. It’s – that body, the one that’s in your core.

THIS is the thing that you have been carrying. Always carrying.

It’s all going forward now, you don’t want it to be, it’s going forward, time, and your body, you have no choice. And finally: There it is . . . And there it is . . . And there it is. (Long beat)

Part Three: She folds his clothes. (She’s back at home. In his room, or at least with his clothes. She’s folding them)

I used to go into his closet and move these three thirst – button up the front ones – I’d put, put them in the front, like he would suddenly see them and realize he wanted to wear them. Like moving the okra on his plate so he’d want to eat it – “See how good this looks?” Ridiculous.

It's not about class. It was never about that. Me trying to get him dressed up so we could elevate him in other people’s eyes. Not really.

The clothes . . . It’s . . . you do these thing, these small things to protect his . . . protect his . . . . his (She breaks) body. That body. Oh. (She buries her face in the clothes) Oh, vulnerable body. I thought I knew. How much. Oh.

I heard someone on – you know, some panel, say this thing: Men in black bodies have since the founding of this country been vulnerable by way of the body that they inhabit. Oh. That’s a crazy thing to think about, that’s a crazy thing to carry. For him. Right.

(She holds one of the shirts) And this – these – never were going to protect him. Were they? Why did I think they could? (Clarity. Beyond pain. Exhaustion. Beat)

And now I will do another dance.

With other mothers, some that I know on a molecular level, and some who live in places I don’t even know exist. I would like to know those women, but not in this way. This is an involuntary and wicked dance. (She is alone with the shirt, maybe hums a song)
```

---

## IC-0133: Eleemosynary

- Title: Eleemosynary
- Author (byline): Lee Blessing
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ECHO, DOROTHEA, ARTIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1863
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lee Blessing
ISBN: 978-0822203544
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
That’s Echo. She’s amazing – a true genius and so young. Through a series of flashbacks, you’ll find out more about her, her mother and her grandmother soon - a character study in triplicate. None of these women are exactly like me or you, or probably anyone we know, but you’ll find bits of them in all of us. And perhaps enough information to contemplate some questions.

As women, how do we make our way through life? How do we behave as parents? How do we become who we are because of or in spite of our parents? Let’s rejoin Echo now in

Eleemosynary by Lee Blessing
```

### Performance text (classify this)

```text
ECHO: (Pg 7) (to audience) Eleemosynary. E-L-E-E-M-O-S-Y-N-A-R-Y. Eleemosynary. It's my favorite word. Not just because I won with it, either. Eleemosynary: "Of or pertaining to alms; charitable." Eleemosynary. (slowly approaches the imagined image of Dorothea laying in bed, studies her for a moment) This is my grandmother. She had a stroke. (opening the drapes) She can't really talk. I can hear her, though. At least I think I can. She's seventy-five years old . . .

ECHO: (Pg 7-9) (to audience) My grandmother believed she could fly using only a pair of homemade wings. In 1958 she made a movie of herself and her daughter, my mother, trying it out. Mom was only fifteen then. (Echo steps into the scene as Dorothea)

DOROTHEA: (Speaking with force and assurance, as though to a film camera) Hello. I am Dorothea Wesbrook. Today I am going to prove that man - or, in this case, woman - can fly without the aid of any motor of any kind, using only the simple pair of wings you see my daughter, Artemis, wearing here. (Artie begins to edge off camera. Dorothea stops her gently without interrupting her speech) We will try two experiments today. First, the very steep hill, and second, the wooden tower. (turns to Artie, suddenly shouting) Flap! For God's sake, you call that flapping?! You're being filmed!

ARTIE: (running, flapping) It's not working! I'm not flying!

DOROTHEA: You will! Keep trying! Concentrate!

ARTIE: (suddenly drops the wings and speaks like a 30-year-old woman to the audience) Never have a daughter. Never have a child, for that matter, but never have a daughter. She won't like you.

DOROTHEA: Keep flapping! (Artie wails picks up her wings and begins flapping) (to camera) (Pg 11-13) Well, the very steep hill seems not to have done the trick. We are moving on, therefore, to the wooden tower. (Artie gives an "Are you serious?" look then climbs a ladder to the platform of a wooden tower while Dorothea watches) My daughter is now, oh, about twelve feet above the ground, and . . . Let go of the railing, dear.

ARTIE: (eyes closed) No!

DOROTHEA: Don't be stubborn. You want to fly, don't you?

ARTIE: No!

ECHO: (Dorothea steps out of scene to narrate as Echo) I do . . . There’s something about the Wesbrook women. We have this expectation to be extraordinary. It’s a little like having a disease in the family. I fly with words. Oh, I know it sounds stupid to say, but it's true. When I was still in my crib, my grandmother was constantly shoving words and numbers in front of me. My grandmother made me love words. My mom helped, too. A little. (steps back into the scene as Dorothea)

DOROTHEA: Why are you so afraid to make history, Artie? (to the camera, embarrassed) Well. . . it appears we will not be able to complete our experiment today.

ARTIE: (eyes closed, holding on) Damn right. You are nuts! And now you're nuts on film! (freezes)

ECHO: (Dorothea steps out of the scene to narrate as Echo) Dorothea was one of the notable eccentrics of her time. She went on to other projects: communication with the dead, spontaneous combustion, astral projection - but she never filmed those. I can feel my grandmother in me. My mother, too - a little. *****Scene*****

ARTIE: (Pg 16-17) (to audience) My mother made sure I had tutors from the age of four. My father worried that too much learning would hurt my hopes for marriage. But Dorothea told him a smart girl can hide what she knows, so there's still a chance for happiness. (Dorothea.)

DOROTHEA: (breaks in, to audience) Well, that's true in a way . . .

ARTIE: I'm telling this. (turning to audience) When I was eighteen, I got pregnant.

DOROTHEA: It was an accident . . .

ARTIE: Mother! In fourteen years of tutoring, no one - including my mother - ever brought up the facts of life. I didn't know anything about the men 'til I went out with one of them.

DOROTHEA: (speaking to an 18-year-old Artie) You can't be pregnant! You can't! You're eighteen. Your college career . . .

ARTIE: What college career? I'm going to be a mother.

DOROTHEA: No. No, you're not. You don't have to be. Think about it. (beat)

ARTIE: What - you mean give it up for adoption?

DOROTHEA: No. That would mean your father finding out. If he knew about this, he'd have you married to someone in five minutes - and no college, either. You have to do something else.

ARTIE: What? (beat) That's illegal!

DOROTHEA: In this state. But if you go . . .

ARTIE: No! I won't do that. It's a life. (beat)

DOROTHEA: (quiet, steadfast) It's that life or yours. . . If you keep it, none of our plans, none of your potential . . . You won't be you anymore. You'll just be something a child needs.

ARTIE: I don't want to be anything more.

DOROTHEA: When a soldier in battle suddenly has to kill someone, we say that's all right. It's his life or someone else's. Well, you have a choice, too. Between living your life or someone else's. And you have to choose now.

ARTIE: (to audience) I waited. A little while, anyway. But finally we crossed the state line, and (beat) I ran away right after that. Across three state lines. I lied about my age and got a job teaching at a private school. *****Scene***** [Many years passed. Finally, Artie called her mother]

ARTIE: (Pg 26-28) (on phone) Mom? I'm going to have a baby.

DOROTHEA: Is this your way of telling me you're married?

ARTIE: Yes . . . um, his name is Richard [and] I've finished grad school - Biochem.

DOROTHEA: That's lovely. When's the baby due?

ARTIE: Six months. (to audience) A week later, there she was. She bought a house on our block. I couldn't function with her around. She'd come over with some theory for making toads fly. . .

DOROTHEA: Don't get upset, dear. I'll be down the street when you need me.

ARTIE: (to audience) When I had my baby, she took me to the hospital.

DOROTHEA: (holds a baby in her arms) A girl. (suddenly lifts the baby high above her) This one will fly. I can feel it.

ARTIE: (to audience) One month after Echo was born, my husband died in a car accident.

ECHO: (Dorothea steps out of scene to narrate as Echo) When my father died, Mom didn't talk for days. That's what Grandma said, anyway. Not even to ask for food or anything. I think she really loved him. *****Scene*****

DOROTHEA: (Pg 14) (to Echo) Are we all waked up from our nap? We're all waked up and we're three months old, and we're ready to go to school. (tickling Echo) Do we like school? Of course we do. Listen, Artie - she's laughing.

ARTIE: She's laughing because you're tickling her.

DOROTHEA: Well, I'm sure that's part of it. (to Echo, playing with a toy alphabet over the crib) Do we know this letter? That's "A." Can you say "A?" All right, how about this one? "B."

ARTIE: Mom, she's three months old. She can't talk yet. It's physiologically impossible.

DOROTHEA: (smiling) Echo? Try these (dangling another string of letters) This is "Alpha." Can you say that? And this is "Beta."

ARTIE: (to audience) Those baby alphabets are the same ones she had over my crib. Pink for Latin, blue for Greek.

ECHO: (Pg 29) (Dorothea steps out of scene to narrate as Echo) When I was a year old, the three of us moved back East into Grandma's house [and for a year everything was fine . . . then]. *****Scene*****

ARTIE: (Pg 30-31) (beat) I have a job offer [in] Europe.

DOROTHEA: Are you planning to take Echo with you? (beat)

ARTIE: I want you to keep her.

DOROTHEA: Keep her? For how long?

ARTIE: For good. I want you to keep her for good.

ECHO: (Pg 11) (Dorothea steps out of scene to narrate as Echo) Dorothea raised me from the time I was two. *****Scene***** 5 years later

ARTIE: (Pg 33-37) I called up my mother once - from Europe - when Echo was seven. I had some news. (on the phone) I'm coming back. I have a job opportunity in the states. I won't come visit.

DOROTHEA: Call then. You can call us anytime. Do you want Echo back? (long beat)

ARTIE: No. (to audience) Once I got settled, I started to call my mother and Echo now and then. Things went on this way for . . . six years, actually.

ECHO: [Over time] Mom suggested spelling bees. It got pretty important. She ended up calling me a lot more. At twelve, I decided to be the greatest speller in history. For life!

ARTIE: (on the phone) I'll find one. Just a minute. (paging through a dictionary) Metamorphosis. You know that one, huh? Ok, how about . . . Syllepsis? You know that? (Listening, nodding.) What do you mean that's not a hard one? Oppugun is a hard one. Spell it.

ECHO: (dutifully) Oppugn. O-P-P-U-G-N. Oppugn. (beat, to audience) It was strange suddenly talking to her so much. (beat) I decided I was going to get Mom to the National Spelling Bee finals. Dorothea was coming. I wanted them both in the audience when I won it. To see that no matter what they'd done - no matter how they'd done it - they'd produced someone that was completely . . . all right. Someone with perspective. P-E-R-S-P-E-C-T-I-V-E. Perspective. *****Scene***** [At the national spelling bee – The final round – Only Echo and one boy are left]

ECHO: (Pg 37-39) Glunch. G-L-U-N-C-H. Glunch. (quickly) I knew I was right! Glunch is such an easy word. (beat) What's he getting? Donzel?! (suddenly outraged) He guessed! He guessed and he got it! (suddenly her public self) Yes, Ma'am, I'm ready. (listens) Palinode. P-A-L-I-N-O-D-E. Palinode. (her inner thoughts) This can't go on forever, buddy. I'm going to crack you like an egg.

ARTIE: Echo was a little different than I thought she'd be. I mean, she was terrific and everything, but she seemed so . . . desperate.

ECHO: (with great intensity) Come on, miss it! You don't know it. You know you don't. (eyes widen, in a whisper of awe) He missed it! Dear God, please let me win! Please! Just five minutes when I'm the most famous child in America, and Mom and Dorothea see it! (her public self again) Excuse me, could you repeat the word?

ARTIE: I didn't know why she was behaving that way, so competitive.

ECHO: Eleemosynary. E-L-E-E-M-O-S-Y-N-A-R . . . Y. (raises her arms in triumph)

ARTIE: I slowly made my way to the front of the room. Echo was being mobbed, but all I could look at was the boy she'd beaten. He looked like a dead mouse.

ECHO: (Pg 41) (to audience) Eleemosynary. That's the one I won with. (beat) I thought having both of them there would be a good thing. But it wasn't. It made me realize that I was just like them. I was just a very intelligent, vicious person. (beat) I called Mom a few times after the spelling bee. She was always civil, but . . . she was different. I stopped calling after a while. For two years we hardly talked at all. Then Dorothea had a stroke. So Mom came home. *****Scene*****

ECHO: (Pg 44-45) What's wrong with me? Why do you keep leaving me!?

ARTIE: Echo . . . ECHO: Why!?

ARTIE: (tiredly) I used to teach you wrong things. Do you know that? When you were little. Dorothea was with you every day, waggling those . . . goddamn letters and cooing. The two of you got along great. (sighs) So I taught you the wrong names for things. When you were starting to talk, I'd point at the floor and say, "ceiling." I'd point at the door and say, "window." And you'd smile and say ceiling and window, and I began to hope if I could just . . . retard you a little . . .

ECHO: Retard me?!

ARTIE: Just to be normal. I thought if you didn't seem so bright, she might get disinterested and leave us alone. But she didn't. She accused me of "intellectual child abuse." That sounds ridiculous, but it was true. I was angry at you. For picking her. For wanting her more.

ECHO: I wanted you both.

ARTIE: You couldn't have both. You got her. She was better for you than I could've been.

ECHO: Did you love me? When you left me with her? Did you?

ARTIE: Whether I loved you then or now ...

ECHO: Did you love me? Do you?

ARTIE: (beat) Yes. And no. It's always yes and no.

ECHO: (Pg 46-47) (beat) Maybe the smartest thing would be to forget you completely. And Grandma. After all, what did I ever get from the two of you, except a good education? You especially - what were you ever to me, except a voice on the phone now and then? Hiding behind spelling words, making excuses. Just a sound that said, "I love you, and I failed you." I hate that sound. And I will never settle for it, because no one failed me. No one ever failed me. Not Grandma and not you. I'm your daughter. That's what I choose to be. (beat) No matter what we've done - no matter how we've done it - we're all three of us, in our own way, completely . . . eleemosynary. E-L-E-E-M-O-S-Y-N-A-R-Y
```

---

## IC-0134: Emma Goldman: Love, Anarchy and Other Affairs

- Title: Emma Goldman: Love, Anarchy and Other Affairs
- Author (byline): Jessica Litwak
- Work: Women Heroes: Six Short Plays from the Women’s Project
- Publisher: Hal Leonard Corporation
- Publication date as stated: 1987
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: EMMA, NARRATOR
- Teaser before the introduction: No
- Spoken words (computed): 3038
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jessica Litwak
Book: Women Heroes: Six Short Plays from the Women’s Project
ISBN: 0936839228
Publisher: Hal Leonard Corporation
Date (Month/Year): 1987
```

### Introduction (context only: never use it for content warnings)

```text
NARRATOR: SEPTEMBER 9, 1901. Three days ago President William McKinley was shot. The assassin was quickly apprehended. His name is Leon Czolgosz. He has confessed to being an anarchist. He stated that he became an anarchist through the influence of EMMA GOLDMAN, whose writings and lectures incited him to commit this act of violence against the President of the United States. Vice President Roosevelt has stated that the nation will take action to stamp out anarchy all together. A nationwide search for Emma Goldman commenced. In Chicago, homes of several anarchists were raided and six men known to be friendly with Emma Goldman were arrested and charged with conspiracy, but the woman anarchist could not be found. However, this evening the authorities have traced Emma Goldman to Chicago-to an apartment building at 308 Sheffield Avenue. Thirteen officers have surrounded the premises. Fully armed, the officers watch the windows of the third floor apartment and wait for…Emma Goldman: Love, Anarchy and Other Affairs. By Jessica Litwak
```

### Performance text (classify this)

```text
EMMA: The strangest thing just happened to me. I was walking through the crowds with my bag held up to my face, to protect it. So if I got hit, my face would remain unharmed. No scars. I can't believe it, I was protecting my face. Such feminine vanity. What would Sasha say? Hello. I am.. . Smith. E. G. Smith. At least that's the name I've been using recently. This is not my room. This is my friend Max's room. Max has agreed to let me stay here tonight. My lover is in prison and I have been recently accused of conspiring to assassinate the President of the United States. All over the streets they are saying, "Anarchists should be exterminated. Their tongues cut out, their carcasses soaked in oil and burnt alive." Just this afternoon I was riding the streetcar with this charming young lady. She turned to me and said, "Have you read the morning papers? This Emma Goldman is a beast. A blood thirsty monster; she should have been locked up long ago." "Locked up nothing," said the gentleman standing behind us, "She should have her heart cut out and fed to my dog." I nodded politely. . . After all, what do I know of Emma Goldman. I'm Smith. Just plain old E. G. This poor boy. . . this. . .assassin. I wonder what drove him to do this thing? He is reported to have said, "I did it for the working people." Sasha also did something once for the working people. . . but the people are asleep. They are indifferent and afraid. . . I promised Max I would escape to Canada in the morning. . . Max says I have no business being in Chicago . . . he says the police are thirsty for my blood. . . Well, things have been worse. After all, Sasha-that is, Alexander Berkman-is in prison-he's been in prison now for ten years. I don't like to think about it. Perhaps I should have a bath, now. . . you know what Max said? Max said if anyone was to come here tonight, I am to say, "I am the maid." The maid. . . Isn't that what they called Joan of Arc? Shall I tell you a story? To pass the time till Max comes. Yes. Let's see tonight is September 9th, 1901 in Chicago, America, I am hiding, NO. . . waiting, NO. . . relaxing at Max's house, and I will tell you a little story. . . My story. . . A love story. I was born in Kovno, Lithuania on June 27, 1869. I came to America-to Rochester, New York at the age of 16. I worked in a factory making two dollars and fifty cents a week.. At this time, all over the country labor strikes were breaking out-the people were demanding an 8 hour day-on May 4, 1887 a mass meeting of workers was called in Chicago's Haymarket Square. It was addressed by several leading anarchist speakers. It was a quiet and orderly meeting until police burst in and began beating people with clubs. A bomb sailed through the air killing several policemen. All of the anarchists were arrested and on November II, Friday, Black Friday. . . the day I became an anarchist. . . I was walking home from a meeting with my sister Helena. . . I was walking home from a meeting with my sister Helena. . . We have just heard the news. The brave anarchists have been hanged. One of them has committed suicide in his cell. Helena is crying, and I am in shock. We go to my father's house. I am in the kitchen staring at the tea kettle. Everyone is talking about the news from Chicago. I know they were innocent-five of them dead, arrested and hung. . . I hear a woman's shrill voice from across the room: "Those anarchists were murderers-they deserve to be hung!" One leap and I'm at her throat. They pull me back. "The child's gone crazy." I pick up a pitcher of water and I throw it in her face. "Get out. Get out or I will kill you!" My father slaps me. Helena is crying. "I know they were innocent! Five of them dead!" I fall on the floor in a dead faint. They put me to bed. I woke up early. My head was clear for the first time. I had the distinct sensation that something new and wonderful had happened to me. I had an ideal, a reason for living. I decided to devote my life to anarchism. August 15th, 1889. The day I met Alexander Berkman. I arrive in New York City. I have left everything behind me to start a new life. I wander around, and on Third Street I meet a man I have seen in Rochester. He takes me to Sach's Cafe-a gathering place for artists, and revolutionists and workers. . . we sit down at a table. . . I hear a loud voice: "Bring me an extra large steak. An extra large cup of coffee!" "Who is that glutton?" I ask. "That is Alexander Berkman. He never has much money, but when he does he eats Sach's right out of food. He's a very serious young anarchist. One of those obsessive types. The cause above all else you know the kind. . . shall I introduce him to you?" We approach the table. He stands up to shake my hand. "Alexander Berkman, Emma Goldman." He is a boy of eighteen but with the neck and chest of a giant. Big shoulders. Brown eyes. Very severe forehead. Somehow a little frightening. We look at each other. "Hello." Very nervous. "Pleased to meet you." I am smiling, I don't know why.

1890. Sasha. After one meeting of the anarchists, Sasha and I walked home in silence. When we got to the house where I lived. . . my whole body began to shake. Like a fever. I looked at Sasha. He came upstairs. I had a very narrow bed. We were squished together in the darkness. He whispered soft Russian words into my ear. . . that made me drowsy., . I began to drift into a dreamy sleep. . . then suddenly I was roused by an electric current rushing through me... a soft, shy hand. . . trembling. . . touching me tenderly. . . I reached out for the hand. . . we were in a wild embrace. A terrific pain-like a sharp knife. . . breaking through everything that had been dormant, unconscious and suppressed. . . in the morning I was still reaching out--eagerly, hungrily. . . seeking. . . he was sleeping now. . . and I raised myself up on one elbow and watched him . . . the face of this boy that attracted me and repelled me at the same time. . . he was so hard and yet so tender. I kissed his thick black hair and then I fell asleep beside him. . . That was the first time. Sasha is upstairs building a bomb. He's never done it before, but we have a copy of The Science of Revolutionary Warfare. . . and it gives a pretty good description.

May 1892. Henry Clay Frick. Big Boss. Carnegie Steel Mills. Wages are cut. Workers strike. Mills close. Workers attacked. Beaten and killed. Henry Clay Frick. An infamous piece of scum. Sasha has decided to kill him.Sasha knows where he can get dynamite-from a man on Staten Island. Sasha says. . . "I have waited all my life for the sublime moment to serve the cause. To give my life for the people." Sasha says although he will live long enough to justify his act in court, he knows he will be condemned to death. "I have waited all my life for the sublime moment to serve the cause. To give my life. . . " Oh Sasha. The more you talk, the sicker I feel. I am oblivious of everything else--Cause, Duty, Message. . . what do these things mean compared with the force of our love?-Does our three years together mean so little to you that you can sit there calmly expecting me to go on living after you've been blown to bits or strangled to death? I will go with you, Sasha. . . I can help. Besides, I simply must go with you... do you understand, Sasha? An argument ensues. Finally he agrees to let me go with him-at least as far as Pittsburgh. . . on the train. The bomb didn't go off. . . and if the test bomb doesn't go off, that means the second bomb made out of the same materials won't go off either. We have lost forty dollars and a week of our time. Now I'll never be able to go with Sasha-we don't have enough money for train fare. . . we have to raise the money to buy a gun. So how does one go about raising quick cash? How does a woman, alone in New York City, go about raising a large amount of cash quickly? How far does one go for the man one loves? For the cause? Well, I got the idea from Dostoyevsky. In Crime and Punishment, Sonia became a prostitute to support her little brothers and sisters. . . and when the men came, she lay on her cot with her shoulders twitching and her face to the wall. If sensitive Sonia could sell her body, if Sasha can give his life to the cause, then certainly I can . . .The question is, am I attractive enough for the men on the street? I look tired. But my complexion is good. I have nice hair. I'm too large in the hips for my age, but I'm a Jew, I look like my grandmother-it's something to be proud of! . . . Anyway, I could always wear a corset and high heels. Oy.

July 16th, 1892. I am walking up and down Fourteenth Street. I join the long procession of girls I have seen so often. I try to mimic their calm. The weather doesn't seem to affect them. They disappear into doorways with men and then reappear again. . . each time a man comes by me, I get nauseous. . . and then I panic as he passes me by . . . I have to raise the money to buy a gun! It's 11:00 and still I've had no luck. Finally an elderly man in a pinstripe suit approaches me . . . he beckons me to follow him into a cafe... He orders two glasses of wine. "I don't know what drove you to the streets, but I'm sure it wasn't looseness, or lack of excitement in your personal life." "Many girls are driven to it by economic necessity!" I told him. "I'm not interested in economic necessity, or in the reason you were out there, I'll just tell you one thing: There's nothing in prostitution unless you have the knack for it . . . and you most certainly do not." He put a ten dollar bill down on the table. "Now go home," he said. "Don't you want me to do something? Take off my clothes or something?" He smiled. "You are a sweet kid, but you are silly and stupid, and immature." "I was twenty-three last month!" He laughed at me. I ran all the way home. With ten dollars for the gun. I cling to Sasha. He is already on the train. I am on the lower step. . . his face is bent low to mine. . . he is holding me: "My sailor girl." . . . the train moves. . . "Comrade, you will be with me to the very last. Steam. Wheels turning. He loosens his hold and gently helps me down. . . I have to jump a little off the step. . . I'm running, waving and crying after the departing train. . . Sasha, Sashenka! Arms outstretched. A life is being snatched away. . .

July 23rd. Saturday. I ran after the departing train. We only had money for one ticket. He said only one person was needed for the job. He barged into Frick's office and shot the bastard three times. In the neck, in the shoulder. There was blood. Men ran in. They took the gun. He had a knife. Poison dagger. He stabbed Frick in the leg. They took the knife. He put something in his mouth. They pinned him to the ground. They pried open his jaws. Candy, he said. There was a capsule of fulminate of mercury. All he had to do was chew on the capsule and the whole room would have blown up and everyone in it. They held his head back. They removed the capsule. They beat him unconscious. Sasha has been in prison now for ten years, many of them in solitary confinement-in a dungeon. And Frick survived and became a hero in the press and the public turned against the workers and the strike was broken. It was said we set back the American labor movement forty years.

I am in the visitor's room in the Western Pennsylvania Penitentiary. I am frightened. I haven't seen Sasha in months. I am waiting and then all of a sudden he's there. In a grey outfit. Looking thin. He has lost some hair. The guard is watching us. I am shaking in the knees. But I keep my hands steady so Sasha can't see. . . ah Sasha. Hello, my love. . . He won't look at me. . . He seems weak. The guard thinks I'm his sister. We sit together on the wooden bench. He has changed. The shoulders hunched, the spirit broken. The brown eyes full of despair. The guard is pacing. Door slams somewhere in the hallway. Sasha jerks his head up. Our eyes meet. I am smiling at him. I don't know why. The guard comes to stand over us. "Your time's up." Sasha jumps to his feet. I feel so helpless. He kisses me, and I feel something pass from his mouth into mine. . . Then he is gone as quickly as he came. In my mouth was a message from Sasha. It said that I should go to Inspector Reed and try to get a second visitor's pass for the next day. But by the next day my identity had been discovered and no one was in the mood for doing Emma Goldman any favors. . . No, after that day I didn't see Sasha again for nine years.

I wonder where Max is? He should be home by now. I only came to Chicago because so many of my friends were being arrested-just for having their names linked with mine. I thought perhaps I would turn myself in but then Max said. . . I don't like to think about it. Sometimes I wonder if my life has been wonh living up to this point. Has anything been heard? Has the world shifted even a little? Here I am pretending to be a maid in someone's apartment, getting ready to run off to Canada like a horse thief. I don't know. . . If you're buried under a ton of din, isn't it better to hack away at it with the heel of your shoe rather than turn away from the task for lack of a shovel? .., Isn't it. better to fight for breath than to resign oneself to suffocation? Anarchism is a process, not a finality. Oh Sasha. I am trying to be brave. I paid the first due for my opinions in 1893 . . . with a year's free residence at Blackwell's Island Penitentiary. I was arrested after a speech I gave at Union Square. They grabbed me as I left the meeting. There were three of them. They held my hands behind my back and pushed me against a wall. "Why am I being arrested?" I asked them. No response. "What am I being arrested for?!" "For being Emma Goldman," one of them replied. . .

Well, if Max doesn't show up soon, I'll go to bed. . . I have a big trip ahead of me in the morning; I don't particularly want to go to Canada, but 1 guess it's the best thing. 1 can't hide here forever using a fake name---especially Smith. 1 suppose I'll have that bath now. . . there's nothing like warm water to calm the nerves. . . Oh, I'm not frightened. I've had a lovely evening. . . I've thought of Sasha... it's so good to be able to look back, to forgive oneself. . . and to feel proud of the things one has accomplished. But even more, to feel proud of the pain, and the silliness. . . and the lovemaking. These are trying but wonderful times. There is great work to do. Be brave beloved comrades. Our enemy is fighting a losing battle. They are of the dying past. . . We, are of the glowing future.

NARRATOR: At 10:00 on the night of September 9th, 1901, Emma Goldman was arrested for her alleged complicity in the plot to assassinate President McKinley. She was captured at the home of an anarchist friend, Mr. Max Baginski. At the time of the discovery of her whereabouts, Emma Goldman was taking a bath. There was a scratching at the window and then a crash of glass. She emerged from the bath in a house robe, to find an officer clutching the window ledge with one h and, and holding a gun in the other. The apartment, on the third floor of the building, had no fire escape. She reached towards the officer at the window, "Look out, you'll break your neck!" she recalled. He entered the room through the broken window and ran to the locked front door. He opened the door. Twelve officers crowded into the apartment. The chief officer, Captain Schueffler, grabbed Emma Goldman's arm. "Who are you?" he asked. "I am the maid," she replied. "Who lives here?" inquired the captain. There was no response. When further questioned as to the whereabouts of Emma Goldman, the alleged maid claimed to be a Swedish servant girl who did not speak English. The officers completed a thorough search of the apartment, finding no evidence, until one detective discovered a fountain pen on the floor... the pen was engraved with the name "Emma Goldman." The captain ordered three of his men to remain on the premises to await the return of the woman anarchist. Goldman realized the game was up. There was no way out. No sign of her friend returning home, no use keeping up her false identity. "Excuse me, officer," she said. All the policemen turned to look at her. . .

EMMA: I am Emma Goldman.
```

---

## IC-0135: The End of Aaron

- Title: The End of Aaron
- Author (byline): David James Poissant
- Work: The Heaven of Animals, Pgs 63-77
- Publisher: Simon and Schuster
- Publication date as stated: Mar 2014
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: GRACE, AARON, MANDY
- Teaser before the introduction: Yes
- Spoken words (computed): 1985
- Already set (do not supply): none

### Source block (context only)

```text
Author: David James Poissant
Book: The Heaven of Animals, Pgs 63-77
ISBN: 978-1476729961
Publisher: Simon and Schuster
Date (Month/Year): Mar 2014
```

### Introduction (context only: never use it for content warnings)

```text
Aaron has suffered from paranoid disorders since childhood. Choosing again to stop taking his medication, he is in the middle of another mental health crisis and has locked himself in the basement of his home to escape the apocalypse he believes is imminent. Can his girlfriend Grace convince save him from himself or will this be . . .

The End of Aaron by David James Poissant
```

### Performance text (classify this)

```text
GRACE: (Pg 63-77) Aaron calls to say we’re running out of time,

AARON: Grace, get ten—twenty—gallons of water, eight rolls of duct tape, five pounds of jerky, and a pear. I like pears.

GRACE: And I know we’re going to have to do it all over again -- the collecting, the hiding, the waiting to come out. For Aaron, the world is always ending. It’s the third time this year, and it’s only July. Probably he’s off his meds. (beat) Used to be, he’d warn me.

AARON: I’m just going to try. Just for a week or two.

GRACE: When I stopped supporting these experiments, he stopped telling me. Now, I have to guess, which isn’t hard given the things that come out of his mouth. The trick is figuring out how long he’s been off.

GRACE: First, he’ll feel nothing. Then, week two will hit, and like clockwork, Aaron will start in on that year’s fear. It wasn’t always the end of the world. For a while, Aaron was afraid to leave the house. Then there was the year of the bees. When he was a child, a bee sting put him in the hospital for two days. Now, everywhere he goes, there’s an EpiPen in his pocket. Aaron gets stung, he has less than a minute to plunge the needle into his leg before his throat swells shut. He’s only been stung the one time, but twice he’s put himself back in the hospital.

I blame his parents. Not for the depression—I mean, maybe that’s their fault. Maybe there’s something messed up with their genes. I don’t know. I only know that his folks bought into the whole Y2K thing, and Aaron’s never been the same since.

Imagine it: You’re eight years old, it’s New Year’s Eve and, instead of watching the ball drop with your parents, you’re huddled in the basement, stocked with two years’ worth of water, batteries, and green beans, watching your mom cry. Upstairs, Dick Clark counts down. Downstairs, you shut your eyes and wait for the end of the world. Aaron’s been waiting ever since.

I’ve known Aaron most of his life. Truth is, we’re twenty and we live with our parents, but that’s okay because we have each other, and I’ve come to believe that each other is enough.

I get everything on Aaron’s list. His therapist calls this enabling. I call it love. Home, I pop the trunk. It’s got a dozen gallons in it, and I grab the first two. I start up the front steps and almost kick over the jar -- a mason jar fat with amber, lid collared by a yellow bow—a thank-you for ignoring the bees. A while back, the woman next door set up a hive. Aaron’s mom petitioned the homeowners association, but the HOA let the lady keep her bees, provided no one got stung, and, in two years, no one has. And now we get honey.

I find Aaron in the basement where he lives. The clothes he has on are the clothes he wore yesterday, and I wonder how long it’s been since he slept.

AARON: Come on, come on!

GRACE: He pulls the jar from my hand, and I run back to the car and unload the gallons. I make half a dozen trips up and down the stairs, carrying water, the rolls of tape, the jerky in its five-pound bag. And Aaron stocks his pantry. When I come down the stairs with the last gallon of water Aaron is crying.

AARON: (screaming and sobbing) There’s no room. There’s no more room!

GRACE: I touch his shoulder and he turns, wild-eyed. I hold up the last gallon. (to Aaron)

We can slide it under the bed.

(to audience) How, you’re wondering. How could she love a man who yells, who cries, who makes her carry jugs of water up and down the stairs? But you’re only seeing Aaron unwell. Aaron at his best is better than anyone I’ve ever known. He’s gentle. He’s kind. But those are just words. Here’s a story: I’m twelve, and, one day, this girl, Mandy Templeton, empties her carton of milk onto my tray and floods my lunch.

MANDY: What’re you gonna do, cry about it?

GRACE: We’re at that age where, at lunch, boys sit with boys and girls sit with girls, but Aaron hears this; walks over. He taps Mandy Templeton on the shoulder, and, when she turns, he punches her, hard as he can, right in the mouth. Mandy’s teeth never looked right afterward, and no one ever messed with Aaron again.

Aaron’s always worked that way. And if the trade-off is that, a few weeks a year, he goes cuckoo, then that’s a trade-off I’m willing to take. And so I buy the water. I tape the windows. I hunker down with Aaron, and, when I can, I get him to take his medication, knowing that, in a few days, it will kick back in and the man I love will come bubbling up from the ocean floor. He’ll break the surface.

Aaron uncaps the honey jar and sticks a finger in. He doesn’t offer me any, and I don’t ask. (to Aaron) So . . . How do you know? (to audience) I may as well be asking a toddler how the spaghetti sauce got all over the walls.

AARON: I can feel it.

GRACE: (to Aaron) How does it happen? (to audience) Aaron turns the TV on. According to the news, there’s been a strike in Pakistan. Something to do with American missiles. and the threat of nuclear armament. It’s all the evidence Aaron needs.

AARON: If there’s a detonation, even a hundred miles away, the fallout alone will keep us underground for ten years.

GRACE: I don’t know where Aaron gets his information. Maybe he makes stuff up. Maybe he’s trying to scare me, or maybe he believes what he says. Aaron changes the channel. More Middle East, more death. The pill bottle is on the dresser. I reach it and uncap it. The next part, I have to be careful.

(to Aaron) How about some medicine, sweetie. (to audience) And Aaron knocks the bottle from my hand. The first pill’s the hardest, but it’s only the beginning. They’re antipsychotics, not miracle drugs, and sometimes it’s a week before they kick in. Even if I can get this one into him, I have a long road ahead of me. I stand, hands on my hips. Aaron pops the pill.

I brush my teeth over the kitchen sink and when I move back to the bed, Aaron’s already asleep. It’s almost midnight when he wakes. I tell him to take another pill, and I hear him move to the pantry, hear the honey jar lid come unscrewed followed by a quiet, occasional slurping. (to Aaron) Wake me up for the end of the world.

AARON: Don’t worry, I will

GRACE: -- no trace of irony, sarcasm, any of it. Maybe it’s going to be an easy one. In March, Aaron and I spent an afternoon under the bed. In May, he stayed in the basement, lights off, for a week. But I know that, one of these times, it’s not going to be easy. One of these days, no matter what I do, I won’t be able to get Aaron back on his meds. (beat) The end of the world? It could happen. No one’s denying that. But it’s the end of Aaron that scares me.

I wake. I turn to put my arm around Aaron, but all I get is pillow. The TV’s off. It’s still dark outside. I check under the bed. I check the cabinet below the kitchen sink. Aaron doesn’t leave the basement, not when he’s like this. This is new, and new is scary. There’s a sock on his dresser, weirdly out of place. Beneath the sock, I find the pills, chalky, deformed, and I wonder how long each stayed tucked under his tongue before I looked away. This worries me, but not as much as the honey jar -- empty, licked clean.

I tell myself no way could he be where I think he is, but, nights like this, I know better than to underestimate Aaron. I’m up the stairs in seconds, out the door and running through the yard. The garage door is up. Gardening tools scatter the driveway like a tornado came. I run faster, into the neighbor’s yard. The perimeter is a fence of wood planks too high to climb, but an open gate tells me which way Aaron went. A floodlight flicks on. And there is Aaron. And there is the hive -- a white, wooden box half a coffin in length.

I don’t see any bees. No, what I see is Aaron with a rake in his hands in what I can only guess is an attempt to pry open the lid. The rake quivers in his hands. He’s got an EpiPen in each leg. I don’t know what a jarful of honey and two shots of adrenaline do to a man, but Aaron doesn’t look good. He shakes, almost convulsing.

I could call 911. I could run back to the house and pick up the phone, but by then it would be too late. “Aaron,” I say, and he jumps. I take a step closer. I don’t want to scare him. I don’t want him making any sudden moves. From somewhere, a bee rises and swims, lazy, in the air around us.

AARON: I wanted to surprise you.

GRACE: His arms tremble and the rake scrapes the box. (to Aaron) Aaron, I want you to put the rake down. Now. (to audience) Perhaps, at night, the bees go to bed and don’t fly and don’t sting. God, I want to believe it. I take another step forward.

AARON: (shrieking) Stop!

GRACE: I hold up my hands like a bank teller on the wrong end of a gun.

AARON: (crying) I ate all the honey, it’s not fair. You didn’t get any.

GRACE: I take another step. (to Aaron) I’m fine. I don’t even like honey all that much. (to audience) The rake slaps the hive and rattles the lid. A bee lands on the rake, then lifts back into the sky. Another circles Aaron’s head. I’m close. If I lunged, I could grab the rake. I think I could take him down, but what will it mean if I’m wrong.

A hum has started in the box, and that can’t be good. (to Aaron) Aaron, I want you to put the rake down and come inside. (to audience) He’s looking right at me, but it’s like he can’t hear me, can’t hear past the grim determination to do the thing he set out to do. (beat) It’s my fault. I shouldn’t have slept.

AARON: (voice garbled and far-away) Once the bombs fall, there won’t be any honey. It’s for you . . . All of the honey . . . for you.

GRACE: There are bees in his hair, bees covering the lid of the box. Their wings shine like diamonds in the security lights, and I give up the hope that Aaron hasn’t been stung. I leap. I knock Aaron to the ground and pry the rake from his hands. I fling it like a javelin across the yard, far from the hive, and I sit on Aaron’s chest, hands pinning his wrists to the lawn.

They say that, with enough adrenaline, you can do anything. You hear stories of mothers lifting cars off their kids. I’m on top of Aaron, but I see too late that the weight of my body is nothing compared to what courses through his veins.

And then I’m in the air. I’m falling and I hit something, hard. The hive comes apart, the buzz turns to roar, and the moon, like magic, goes out of the sky. I hear grunting and turn to see Aaron dragging himself toward me on his elbows, like a soldier passing beneath barbed wire.

I feel a sting, then another. My legs are lightning, and, soon, I can’t even look at Aaron, who’s no longer crawling, but rolling, a man on fire. I look up and the swarm descends, looking like the end of the world.
```

---

## IC-0136: Epiphany

- Title: Epiphany
- Author (byline): Heidi Decker
- Work: The Agony and the Irony
- Publisher: Heinemann
- Publication date as stated: March 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1239
- Already set (do not supply): none

### Source block (context only)

```text
Author: Heidi Decker
Book: The Agony and the Irony
ISBN: 0325002479
Publisher: Heinemann
Date(Month/Year): March 2001
```

### Introduction (context only: never use it for content warnings)

```text
A usually sudden manifestation or perception of the essential nature or meaning of something. An intuitive grasp of reality through a simple and/or striking event. An Epiphany. We’ve all had those moments when the “light bulb goes on,” the synapses in our brains click and we realize the meaning of some random thought or event. Some people call it an “AHA” moment.

But what if your “AHA” moment makes no rational sense? What if your“AHA” makes you begin to doubt your sanity. This is the story of a crab, a woman, and . . . . an Epiphany by Heidi Decker.
```

### Performance text (classify this)

```text
(Woman, 20-30. Articulates well, but speaks as if everything is one continuous thought and sentence. Not ditzy by any means, only genuinely perplexed. She has been up for hours, mulling something over. She speaks aloud to try to make some sense of it all.)

All right, maybe I'm just losin' it. It's not unheard of, these days, for someone to just lose it for no apparent reason. Maybe that's it. Either that or I've had some deeply symbolic, spiritual experience and I just didn't get it. I don't know.

All I know is that now, I can't get it out of my head. It's just there, right behind my eyes, and it won't leave me alone.

Don't get me wrong, I'm not obsessed or anything. It's just that I feel like the whole thing is supposed to . . . I don't know . . . tell me something. I know how really dumb that sounds. I just wonder if this is one of those experiences that you read about. . . things that don't hardly ever happen, and when you try to explain it, out loud, it sounds really dumb, but in some weird way it can change your life. . . sorta. See, last night I was leaving work, it was about ten o'clock at night, and I was hungry but I didn't have very much money. I decided to go to the grocery store because it's open 'til midnight and they have a deli section where they have fresh sandwiches made every day and after nine o'clock at night they mark them half price 'cause they have to get rid of them 'cause they can't sell them the next day. . . because they're advertised to be made fresh every day. So, you can get a really big sandwich for a dollar.

Then I began walking across the back part of the store to the dairy section to get some milk. I was walking along, trying to decide whether I wanted skim or two percent, when something in the seafood section caught my eye.

You know how a lot of grocery stores have a big tank with lobsters in it? And there's usually about a dozen all piled in there, with rubber bands wrapped around their claws so they can’t snap at anyone, or defend themselves or anything. . . Well, last night there weren't any lobsters. One tank was empty, and the other had seven or eight crabs in it. Big ones. Kind of like soft-shell but not exactly. . . maybe they were snow crabs. . . you know, with those huge front claws that you see people in restaurants pounding on with a hammer.

Apparently these guys were a specialty item running for a few days. What caught my eye was this: all those crabs were huddled over in one corner, looking like they were trying to keep warm or play king of the mountain or something. . . all but one. One of them was way far away from the others. He was sitting right at the edge of the tank, pressed up against the glass, and, I swear to God, watching what was going on in the store. Like a little kid with his hands pressed against the glass watching some guy toss pizza crust.

Well, there's no one around but me, so I was the only thing moving. . . and. . . you know how they have those little eyes on top of their heads?

Every time I moved, they would follow me. Back and forth, up and down. Now that's not so strange. I'm sure had he been in the ocean he would have been watching whatever happened to be moving.

I stepped up close to the glass and I guess it kind of startled him because his eyes disappeared into his head for a few seconds, but I stood there and slowly his eyes came back out. I bent down a little bit and put my hand up to the glass. It was really cold outside and I still had my gloves on. I'm crouched down next to a lobster tank with my hand up against the glass watching this crab watch me, when I heard someone pushing a shopping cart pass by me.

The noise made me remember where I was and I stood up quickly, and as I did, the crab's eyes ducked back down into his head. I stood there for a few seconds, waiting, but they didn't come back out again.

I noticed that my hands were getting sweaty so I took off my gloves and as I did, I happened to look at my watch and saw that it was getting late. I started to walk away when. . . I swear. . . I heard a little. . . tapping. . . noise.

I looked back, and that crab was tapping the glass with one of his claws. He was lifting one of his front claws a little and tapping steadily on the glass. I'd never seen anything like it. Well, who has? So I crouched down again to get a closer look.

He just kept. . . tapping. . . until finally I put my fingers against the glass, right in the spot where he was tapping. He stopped. He just left his claw there on the glass.

I tapped my fingers, twice, against the glass. He tapped back. Twice! I swear. I tapped once. He tapped once. I don't even know why I think it was a he, I just do. And then. . . and then, I put my other hand against the glass. And waited. And slowly, he lifted his other claw, and put it against the glass, opposite of where my hand was.

So I'm in the middle of this grocery store, crouched down nose to nose with the daily under-the-sea special and. . . and for a second. . . I swear to you, for a second. . . . I. . . felt. . . something.

I don't know what. I know it sounds ridiculous but he had his claws against my hands and my eyes were level with his, with just half an inch of glass between us and for a second I felt. . . something. . . right in the middle of my chest. Not like heartburn or anything, just, sort of, I don't know. . . warm. I guess. I could feel it on my skin, but inside too. . . kind of like a . . . glow. Just for a second. Then he brought his claws back down. He backed away and turned away a little, then stopped, and kind of looked at me . . . then turned himself around and crawled to the back of the tank. I just crouched there and watched him, half expecting him to turn and wave, with a sunset shimmering behind him.

By now my knees were killing me so I stood up, kinda shaky. I left the sandwich I was going to buy there, on the floor, and walked out of the store. Out in the parking lot it was freezing cold, but I could still feel that. . . whatever it was . . . it was the strangest feeling. I got in my car and went home. I was in kind of a daze, I guess.

And so now, I can't get it out of my head. I know it sounds weird but nothing like this has ever happened to me, and what if. . . well, what if, at some point in your life, everyone has some sort of experience, something unusual like this, and it's supposed to mean something, to tell you something. . . and I just don't know what.

I mean, really, what? Don't eat seafood? What was I supposed to do, buy him? Where would I have kept him? (Sigh) I mean, some people hear voices, some people have visions. . . but me, I . . . I have a spiritual experience with a ... crab. What the hell does that mean?!?
```

---

## IC-0137: Exonerated

- Title: Exonerated
- Author (byline): Jessica Blank and Erick Jensen
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Jan 2004
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SUNNY, BLACK COP, RHODES, WHITE COP 1, WHITE COP 2, STATE ATTORNEY
- Teaser before the introduction: Yes
- Spoken words (computed): 1895
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jessica Blank and Erick Jensen
ISBN: 978-0822219460
Publisher: Dramatists Play Service
Date (Month/Year): Jan 2004
```

### Introduction (context only: never use it for content warnings)

```text
Today there are roughly 2 million people incarcerated in the US. An alarming number of them are wrongly convicted, in some cases spending decades behind bars for crimes they did not commit. According to the University of Michigan's National Registry of Exonerations established in 1989 as of January 2025, 3,658 people have been exonerated due to false or misleading forensics evidence, a false confession, mistaken witness identification or official misconduct by arresting officers.*

Sunny Jacobs was only 26 when her life changed forever. This is her story. Exonerated by Jessica Blank and Erick Jensen
```

### Performance text (classify this)

```text
Sonia (aka Sunny) white 50. A bright, pixie-ish yoga teacher from California; her lightness and positivity contrast with moments of great depth and clarity.

SUNNY: Sunny Jacobs. (beat) In 1976, I was sentenced to death row, which for me wasn't a row at all, because I was the only woman in the country who had the sentence of death. So I suggested they put me in the same cell as my husband! But let me start at the beginning. (beat)

SUNNY: (Pg 22-23) When I was twenty-six, Jesse and I had been together for three years. We weren't officially married, but I considered him my husband, you know. Our daughter had just been born, and Jesse said he was gonna get himself a regular job, maybe painting murals or something, but he just needed to go to Florida one last time to do a little deal. Now, I didn't want to know about this deal, because I knew it wasn't positive; it wasn't violent, but it wasn't positive. And finally he calls and says that the deal fell through, and not only is he broke and has no way home, but he's staying with some girl! So, of course, me, instead of saying, "Well, when you get it together, me and the kids will be here waiting for you," I said, "I'll be right there to getcha!"

My son Eric was nine, and I was driving, shifting, singing, and nursing Tina all at the same time. So anyway, we get there, get Jesse, the car dies, and we're all stuck in Florida. And so Jesse says he'll ask this guy he knows if we can stay with him until we can scrape the money together to get home. And that's when I met Walter Rhodes. (Pg 26-27) [He] agreed to give me, Jesse, and the kids a ride. And we left, but the traffic got bad and it was getting late, so the decision was made to pull off the road until morning.

And according to the police reports, the cops came to do a routine check on the rest area. And when they look in the window, they see a gun between Rhodes's feet. They order him out of the car and ask for his ID. The policeman calls in the ID information, and then tells Rhodes . . .

BLACK COP: Stand over there, I'm finished with you.

SUNNY: And then they ask my husband Jesse to get out. And then the police radio comes back with the announcement that Rhodes is on parole -- and possession of a gun is a parole violation. And that changed everything. The policeman drew his gun. He said-

BLACK COP: Okay, the next one to move is dead.

SUNNY: It all happened so fast, you know. I just ducked down to cover the kids. (four loud gunshots) And then it was silence. I mean dead silence. There wasn't an earthly sound. And then Rhodes runs around the front of the police car with a gun in his hand . . .

RHODES: Come on, we're gonna take the police car!

SUNNY: I mean, Rhodes had just killed two policemen, had a gun, and was telling us to get in the police car. And, you know, people say, "Why didn't you just refuse to go?" And I think, you've never been at the other end of a gun, have you? So we get in the police car. We couldn't speak . . . We were kidnapped at that point, and we just didn't dare.

But then all of a sudden, the traffic gets terrible, and you can hear the helicopters, and I know there must be a roadblock. "Hey, we're gonna be rescued! Help is on the way, you know, the cavalry!" And out of nowhere, Rhodes makes a sharp left to try and avoid the roadblock -- and this whole line of policemen opens fire on the car. The car was literally bouncing with all the bullets. So again I cover the kids. And finally we crash. And a bunch of cops surround us, and I'm trying to explain that we were kidnapped, but they just wouldn't listen.

****In Sunny’s interrogation room****

WHITE COP 1: Are you aware of the fact that you have been charged and arrested on First Degree murder?

SUNNY: [beat] You just told me now. (Pg 29-30) [to audience] So I actually did at first try to lie, and I told the cops I didn't know these people, I was just a hitchhiker. Stupid. Because of course they think you're lying because you did something. But I was just scared.

WHITE COP 2: Let me ask you point blankly: Who shot the highway patrolman and the other officer?

SUNNY: I don't know . . . I'm sorry. People were shot. The patrolmen were shot and that's what this is all about -- I don't know -- [breaking down] This is very upsetting because how does -- this guy, he told -- he just told us to sit in the car, you know -- and I'll stay here and I won't make any calls and I haven't done anything except the wrong choice of people and I just -- I don't want to be blamed for something that I had nothing to do with and I don't want them to take the kids away and I -- 'cause the baby's crying and crying and crying and Eric's scared and (long pause while she composes herself)

(Pg 31) [to audience] And what I didn't know was at the same moment I was being questioned and Jesse was being questioned, was that Rhodes, from his hospital bed, was negotiating a deal. He'd been in prison before, he knew how the system worked. And so he was claiming that he didn't do it -- we did. **** Rhodes Hospital Room ****

STATE ATTORNEY: Okay, Mr. Rhodes. Who had the gun in their hands when the first shot was fired?

RHODES: [overly helpful, exaggerating] When the gun first went off, Sonia was the one holding the gun. [then scrambling] This is to the best of my knowledge, I am not one hundred percent sure. To the best of my knowledge, she fired two shots, I believe then Jesse pulled the gun from her and shot him one more time and then he shot the other cop twice.

Then I started to go toward my car, to get in, it didn't even enter into my mind, but Jesse said, "Get in the police car. We have got to get out of here," or something, and I said, "No," you know, "what happened?!" Anyway I did get in the police car, I was damn near in shock myself. ******back to Sunny*******

SUNNY: (Pg 35 – 36) [to audience] They tell you exactly how they're gonna do it. They're gonna send 2,200 volts of electricity through your body until you’re dead. And then they ask you if you have anything to say to that, and really it's kind of dumbfounding. So after the judge read the sentence, I just said, "Are you finished?" I didn't have anything to say. What do you say? How can you say anything to that?

They decided to clear out an entire disciplinary unit at the women's prison. It's a very old prison, it's like a dungeon-type place. It was six steps from the door to the toilet bowl -- you could stretch out your arms and touch both walls. They take your clothes; they give you a number, so basically they're taking . . . who you are from you. You no longer have a name, you're a number. You're locked inside this tomb. It's like you're thrown to the bottom of the well.

(Pg 43-44) First I had to decide, I am not going to let them do this to me. 'Cause if you sit there, rubbing two sticks together and crying on your sticks, they're never gonna make a spark. But, you know, if you stop feeling sorry for yourself, just because you're determined not to believe in hopelessness, then a spark happens, and then you just keep fanning that little spark until you got a flame.

And I realized that it was like a big trick. That I wasn't just a little lump of flesh that they could put in a cage. And I decided that I would have faith, that there was some power out there greater than them, to which I could make my appeal.

Now, you people that don't believe, you could say I was like Dumbo and I put this feather in my nose and I flew because I could fly anyway. Or you could say that there really is something out there, and if we have faith in it and we appeal to it, it will answer us. And maybe we're both right. I don't know.

(Pg 46-47) In 1979, Walter Rhodes wrote the following letter to the judge.

RHODES: I, Walter Norman Rhodes, hereby depose and say that I am under no duress nor coercion to execute this affidavit. On February 20, 1976, at approximately 7:15 a.m., I did, in fact, shoot to death two law enforcement officers with a nine-millimeter Browning pistol.

My previous testimony against Jesse Tafero and Sonia Jacobs was false and part of the statements I was instructed to make by the assistant state attorney, who did coerce me into lying.

SUNNY: Keep in mind that I wasn't released until 1992. So I'll just give you a moment to reflect: From 1976 to 1992, just remove that entire chunk from your life, and that's what happened. [long pause] But after all that, one day, the guard came into my cell and told me I was getting out. I thought he was trying to trick me. (cell door opening) And it was just so joyous. I mean, I know a lot of people are angry, and I was angry some, but I didn't want to waste my time being mad.

(Pg 51) You see, I got another chance, because I looked for it. I looked to turn a pile of manure into flowers. I didn't even get lemons; I got manure [laughs]. I mean, I'm not glad for what happened to me -- when I was in there, my parents died, my children grew up without a family . . . and my husband was executed -- very, very brutally: Jesse's execution was known worldwide. The chair malfunctioned and made a mess of it. And – (pause) they had to pull the switch three times.

And he didn't die. It took thirteen and a half minutes for Jesse to die. Three jolts of electricity that lasted fifty-five seconds each. Almost a minute. Each. Until finally flames shot out from his head, and smoke came from his ears, and the people that came to see the execution, on behalf of the press, are still writing about it. Years afterwards. Why do we do that?

(Pg 52) I want to be a living memorial. When I die, I want 'em to plant tomatoes on me, or apple trees or something, so that I can still be part of things. And while I'm still alive, I'm planting my seeds everywhere I go, so that they'll say, "I once heard this woman, and she didn't let them stop her, and she didn't get crushed, and if that little woman person can do it, then I can do it." And that's my revenge. That's my legacy, and my memorial.

You know, I've never been to Jesse's grave, and for a long time it was a bone of contention between his mother and me. But I explained to her, I said, "That grave is not where Jesse really is." I said, "That grave is your monument, and this is mine. My life is my monument."
```

---

## IC-0138: Expecting Adam

- Title: Expecting Adam
- Author (byline): Martha Beck
- Work: Not specified
- Publisher: Berkley Publishing Group
- Publication date as stated: Aug 2000
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MARTHA, JUDY, JOHN, GRENDEL, VOICE IN MARTHA’S HEAD
- Teaser before the introduction: Yes
- Spoken words (computed): 1557
- Already set (do not supply): none

### Source block (context only)

```text
Author: Martha Beck
ISBN: 978-0425174487
Publisher: Berkley Publishing Group
Date (Month/Year): Aug 2000
```

### Introduction (context only: never use it for content warnings)

```text
Growing up with 47 chromosomes is not terribly different from growing up with 46. Children with Down Syndrome read, write, play sports, sing show tunes, and parade around the house in “full pirate regalia” instead of getting ready for school. They have their ups and down; dreams and disappointments; but fundamentally they want what anybody wants — to be valued, respected and accepted for the wonderful people they are.

But for young parents, finding out your child will be born with Down Syndrome is overwhelming.

Expecting Adam by Martha Beck
```

### Performance text (classify this)

```text
MARTHA: (Pg 60) The word mother is more powerful when it is used as a verb than as a noun. There are women who bear and raise children without ever mothering them, and there are people (both male and female) who mother all their lives without ever giving birth. This was one of the greatest gifts I would receive from Adam . . . Against all odds, despite everything that works against it on this unpleasant, uncomfortable planet, mothering is here in abundance.

JUDY: (Pg 127-136) (Martha and John enter; Martha pushes the blinking light on her answering machine to hear messages) [Beep] Martha, this is University Health Services. I need to get in touch with you immediately – immediately – regarding the results of the tests. Please get in touch with me as soon as possible.

MARTHA: (Martha dials the phone) Hi, Judy. This is Martha Beck. Is there something wrong?

JUDY: We got an unusual reading on your alpha-fetoprotein levels. It was a bit below normal.

MARTHA: Below normal? Well, that’s good, isn’t it?

JUDY: It’s not necessarily bad. But there is a slight statistical correlation between low levels of AFP and Down syndrome.

MARTHA: (taken aback) What are my odds?

JUDY: Based on this one test, which is only preliminary, of course – your odds of having a Down’s baby are 1 in 895. We want to do the test again to see if we get the same results. Just to be on the safe side. We don’t have much time.

MARTHA: Time? Time for what?

JUDY: To terminate. If there’s something wrong. (Martha slowly hangs up the phone and turns to John)

JOHN: What exactly is the problem.

MARTHA: (shaking her head in disbelief) We’ve got a 1 in 895 shot at a retarded baby.

JOHN: (smiling and making light of the situation) I can live with those odds.

MARTHA: (trying to smile) I’m . . . I’m a little scared.

JOHN: That’s understandable. But even if there’s a problem, we’ve caught it in time. The worst-case scenario is that you might have to have an abortion, and that’s a ling shot. Everything’s going to be fine.

MARTHA: I might have to have an abortion? I might have to have an abortion? (growing angry) Since when do you decide what I have to do with my body?

JOHN: (surprised) It’s just that if the tests show something wrong with the baby, of course we’ll abort. We’ve talked about this.

MARTHA: (in a low, dangerous voice) What we’ve talked about is that I am pro-choice. That means I decide whether or not I’d abort a baby with a birth defect. You steer clear of this one, John-boy. It is not your call! (beat, while Martha calms herself) It’s just not ethically consistent. I mean, not abortion in general, just this kind of abortion. This designer-baby stuff.

JOHN: (surprised) You mean screening for birth defects? What in the world is wrong with it? It’s better for everyone.

MARTHA: I’m not so sure of that. But . . . It’s not as though we’re deciding whether or not to have a baby. We’re deciding what kind of baby we’re willing to accept. If it’s perfect in every way, we keep it. If it doesn’t fit the right specifications, whoosh! Out it goes!

JOHN: (shaking his head) Don’t be silly. You know that isn’t true. We’re talking about the difference between a healthy, normal baby and a defective one

MARTHA: (bristles at the word defective) So what exactly is a ‘defective’ baby? I mean, I know there are babies born so damaged they can’t survive on their own, but what about the ones that would actually live unless they were aborted? Where do you draw the line? What if this baby had a clubfoot or something? Would you tell me I ‘had to have’ an abortion?

JOHN: Martha, why are you on this soapbox? What’s your point?

MARTHA: My point is that I’m trying to get you to tell me what you think constitutes a ‘defective’ baby. What about . . . oh, I don’t know, a hyperactive baby? Or an ugly one?

JOHN: They can’t test for those things, and . . .

MARTHA: What if they could? Medicine can do all kinds of magical rick these days. Pretty soon we’re going to be aborting babies because they have the gene for alcoholism, or homosexuality, or manic-depression. Did you know that in China they abort a lot of fetuses just because they’re female? Is being a girl ‘defective’ enough for you?

JOHN: I didn’t say . . .

MARTHA: (cutting him off) Just exactly how smart does a baby have to be before its parents accept it? How good-looking? How healthy? How strong?

JOHN: Honey, this is not eugenics. We aren’t talking about breeding a race of supermen. We’re talking about taking some of the tragedy out of life. Abortion is a way to deal with the problem, you know? To limit it. That’s all I was saying.

MARTHA: And you’d still want me to abort this baby if it wasn’t normal. Wouldn’t you?

JOHN: Look, the way I see it, if a baby is going to be deformed or something, abortion is a way to keep everyone from suffering – especially that baby. It’s like shooting a horse that’s broken its leg. A lame horse dies in terrible pain. It can’t run anymore, so it can’t enjoy life even if it doesn’t die. Horses live to run; that’s what they do. If a baby is born not being able to do what other people do, I think it’s better not to prolong its suffering.

MARTHA: (softly) And what is it that people do? (Beat, then to audience) And then I understood . . . The part of us that makes our brief, improbably little lives worth living is the ability to reach through out own isolation and find strength, and comfort, and warmth for and in each other. This is what human beings do. This is what we live for, the way horses live to run. ***** Break *****

(Pg 181-183) (the phone rings and Martha answers)

JUDY: Hello, Martha. It’s Judy Trenton from University Health Services. I have some . . . not so good news for you. The results from your amniocentesis are in, and they show that you are carrying a Down syndrome fetus. (silence) Martha? Are you there?

MARTHA: (Softly) Yeah. (to audience) By the time the Down syndrome was diagnosed. I could not more have asked for an abortion than I could have shot [my older daughter] Katie in the head. (to Judy) I don’t want to terminate the pregnancy. (she hangs up slowly) (Pg 211-212) Those first few days after hearing the diagnosis, I swallowed thousands of appalling bits of information from insensitive and outdated sources. The mustard-yellow book I’d bought at the Co-op was the worst. It had last been updated in 1950, when people with Down syndrome were rarely seen outside of institutions. It makes me sick to think of the thousands of children who were raised in institutions. Isolated, bored and aching with loneliness, many literally turned their faces to the wall and died by the time they were in their teens. The book described this as the normal life course for the human beings it called “mongoloid idiots.” I want to state for the record that putting a person with Down’s into an institution is like forcing an otter to live in a Pringle’s can. There is nothing wrong with the social adaptability of people like Adam. They thrive on loving interaction. But in the days after Adam’s diagnosis, I hadn’t learned any of these things. I’d forced myself to accept claims that were both untrue and brutally unkind.: 1. The birth of a Down syndrome child generally destroyed the mother’s mental health. 2. The inability of such children to control their bodily functions and their antisocial inclinations.

3. The typical IQ for “mongoloids” – about 35, and by way of comparison, the IQ of a chimpanzee is about 50. In the days following Adam’s diagnosis, I seemed to have no strength at all. I made a half-hearted effort at sleeping, but barely even tried to eat. I was dehydrated and probably needed an IV. But the through of going back to University Health Service was almost unbearable. . . (Pg 214) The admitting physician recommended that I spend the night. (Pg 216) The next morning I was surprised to see Dr. Grendel approach my bed. (He takes the chart from the end of the bed are reviews it quickly)

GRENDEL: (Pg 217) Your chart says that you haven’t eaten for four days. (Gently) We all know what you’re trying to do. There are more efficient ways to take care of this problem than starving yourself until the fetus dies.

MARTHA: (shocked) Excuse me?

GRENDEL: Martha, listen to me. I have been in this business for a very long time. You realize that you are placing a very heavy burden on yourself and your entire family. Did you know that 80% of couples who have a child with this condition end up divorcing? I would not make the choice that you have made. I have never known anyone who would.

VOICE IN MARTHA’S HEAD: (Pg 238) (From the books she’s been reading) It is the duty of every woman to screen her pregnancies and eliminate fetuses that would be a detriment to society.

MARTHA: (Pg 220) (to audience) Dr. Grendel, who had never seen a woman elect to keep a Down syndrome baby, was ignorant when it came to the actual consequences of my choice. (to Grendel) (Pg 222-223) Thank you. You can go now. As Grendel stared at me in frustration and disbelief, Adam gave me a cheerful wallop just below the navel. Briefly, for the first time since I had bought the mustard-yellow book and started soaking in the prejudices against the developmentally disabled world, I was not afraid at all. *****Break*****

MARTHA: Today, [Adam is nine] and (Pg 317) living with Adam, loving Adam has taught me a lot about the truth. He has taught me to look at things in themselves, not at the value a brutal and often senseless word assigns to them. As Adam’s mother I have been able to see quite clearly that he is no less beautiful for being called ugly, no less wise for appearing dull, no less precious for being seen as worthless. And neither am I. Neither are you. Neither is any of us.
```

---

## IC-0139: Explaining Death to the Dog

- Title: Explaining Death to the Dog
- Author (byline): Susan Perabo
- Work: Who Was I Supposed to Be, Pgs 77-84
- Publisher: Simon & Schuster
- Publication date as stated: June 27, 2006
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, TODD
- Teaser before the introduction: Yes
- Spoken words (computed): 2263
- Already set (do not supply): none

### Source block (context only)

```text
Author: Susan Perabo
Book: Who Was I Supposed to Be, Pgs 77-84
ISBN: 978-0743290371
Publisher: Simon & Schuster
Date (Month/Year): June 27, 2006
```

### Introduction (context only: never use it for content warnings)

```text
Explaining Death to the Dog by Susan Perabo
```

### Performance text (classify this)

```text
NARRATOR: (Pgs 77-84) After the baby died, I found it imperative that my German shepherd Stu understand and accept the concept of death. The first week wasn't so bad, what with all our friends and relatives around, smothering Stu with affection. And Todd was home from work that week, dumping well-meaning casseroles accidentally-on-purpose onto the kitchen floor for Stu to indulge in. So Stu didn't notice the absence so much, didn't seem to. He trotted around the house happily, oblivious to the fact that the baby, who he had had a big hand in raising, was missing.

Then the party ended. Guests cried the last of their tears at my front door, said "What a waste" for the thousandth and final time, and made their separate ways back to their separate lives, lives that sailed along quite smoothly despite the absence of the infant whom they had been mourning for a good seven or eight days.

Todd went back to work; packed up his briefcase and kissed me good-bye. He nearly tripped over Stu in his rush to get out of the house. He wanted away, wanted to get busy again. Stu and I stood at the window and watched him drive away. Stu looked up at me and then back at the empty driveway. He lay down on the floor in front of the window. I sat next to him and rubbed his stomach. He sighed.

NARRATOR: What to do with the baby dead? No diapers, no screaming, no feeding. What had I done before the baby? I had been pregnant. Pregnant for longer than she had been alive. And what had I done before I got pregnant? I tried to remember. I supposed I had cleaned the house. Cooked. Taken Stu to the park. It didn't seem like it could have been nearly enough to take up a whole day. In the afternoon I made myself a sandwich from one of the two whole hams that were still in the refrigerator and sat in front of the television. I waited for Stu, waited for him to emerge from wherever he was sleeping, jingling and jangling his way to a possible meal. The house was quiet. Still, very still. The morning the baby died Todd shook me awake to the stillness and said, "Listen, she's sleeping ... "

I set my sandwich on the coffee table and got up to look for Stu. I called him a few times. Nothing. I walked through the house, from room to room. I found him upstairs, in the baby's room. The room was empty, except for one chair. Todd and the relatives had cleaned it out the day of the funeral because they said it was just too sad to look at. They stashed the crib in the back of a stranger's car and carted it away, hid the dolls and mobiles with the cobwebs in the basement. Then Todd's mother said the room looked so bare, so she had taken a chair from our bedroom and set it by the window. It looked unnatural by itself in the baby's room. Worse than bare. Just awkward.

Stu was lying in the middle of the empty room. His ears were back and his eyes open. He didn't raise his head when I came in. He just followed me with his eyes. (to the dog) Stu. Stu, what the hell are you doing? (to the audience) He looked like he had eaten too much casserole, was what it was, looked like he might toss his canine cookies at any moment. He stood up lazily. He walked in circles around the room. You could tell he was looking for the baby.

(to the dog) No. (patting his head) No more baby. Baby's gone. No baby. (to the audience) He looked at me with the universal blank dog look. He had no idea what I was talking about. It was then that I realized the impossibility of the situation. It wasn't even like trying to explain death to a child. The dog simply couldn't understand the language. He had a brain the size of a walnut and all he knew was that the baby wasn't where she was supposed to be. I imagined it must be even worse than knowing the baby was dead. At least Todd had been able to logically spell it out for me that morning to get me to stop shaking her and trying to wake her up, hold the little girl up in my face, point to the chest. NO BREATHING.

It was then I decided that I needed to teach Stu about death, whatever the cost. I figured he had a right to know, being a member of the family.

(to the dog) Come on, boy. (to the audience) On the coffee table we had a book. A big Life magazine book. Best of Life, something like that. I gave Stu part of my ham sandwich to lure him up on the couch with me. I opened the book out on the coffee table, paged through it, looking for the sixties, the best lesson of death on film. I turned the dog's head toward the contorted face of Lee Harvey Oswald, and the man behind him, a man whose name they never mentioned, looking like he might jump right out of his skin from the shock of it. Oswald was holding his stomach, hadn't even hit the floor.

(to the dog) Dead. Stu, it's dead. (to the audience) Stu didn't seem to see the picture. He looked at the book, sure, but there was nothing in his eyes that said that he saw the proverbial farm being bought. The way he looked at it, it could have been a picture of a rolling wheat field. I turned the page, looking for something bigger, and found a two-page spread from Memphis, 1968, the man dead on the balcony, people pointing out into the sky. It was big; you couldn't miss it.

(to the dog) Death. No more. (to the audience) Again Stu glanced at the picture, then back at my ham sandwich. I jabbed my finger on Martin Luther King, Jr., held the picture up in Stu's face, and still his eyes didn't focus on it. What was I expecting? I don't know. If Todd had been there he would have clapped the book shut and told me the dog didn't know what the hell was going on and he'd be over it in a day and a half anyway. But Todd was gone. Strange things happen when you're alone in the house with pets all day . . .

In the middle of the night I woke up and heard the baby crying. I sat up and reached for my glasses before I remembered. It was not a staggering thing. It washed over me slowly, the way you remember what day it is when you wake up in the morning. I looked at Todd lying on his stomach next to me, the side of his face pressed to the pillow, his mouth open. The first week it was him who couldn't sleep. I'd open my eyes and he'd be sitting up in bed, his back against the wall, staring into space. The minister had come by and Todd told him about not being able to sleep. The minister said it was probably guilt, thinking that if he'd been awake when the baby started dying he could have done something about it. After that I guess Todd became comfortable with the guilt, because he didn't sit up nights anymore.

Todd? . . . Todd? (to the audience) I didn't have the courage to touch him, to wake him up and force him to share the grief, to try to explain to me why I might have heard the baby crying when the baby had been dead for over a week. I lay back down next to him and started thinking about the simplicity of a dog's mind. I tried to think of a way to explain to Stu just exactly what was going on.

The morning was cool and dark. It was May and the natural order of things said it should have been warm and bright. But the natural order of things was wrong, so it was ugly out. Todd sat at breakfast and looked at the newspaper in much the same way Stu had looked at the coffee table book. His spoon went from the cereal bowl to his mouth without being led by anything but habit. I stared at him and he didn't even notice.

NARRATOR: (to Todd) I think Stu misses the baby.

TODD: (looking up from the paper, his mouth open and his eyes empty. What?

NARRATOR: Yesterday he was lying in her room.

TODD: Close the door.

NARRATOR: I was thinking. I was trying to figure out how to get it across to him that she's not coming back.

TODD: Why would you think something like that?

NARRATOR: I just thought it was interesting. I wondered how dogs understand those kinds of things.

TODD: What are you doing today? Why don't you call somebody for lunch?

NARRATOR: No one wants to have lunch with me.

TODD: (sighing) We'll go out tonight, then.

NARRATOR: (to the audience) But he wasn't even looking at me. He was looking over my shoulder out the back door, out into the grayness that was passing itself off as morning.

I decided I would go ahead and take Stu to the park, force him down the slide for a good laugh, spin us both around on the merry-go-round just for a change of pace. There would be no baby carriage to drag through the sand, no need to worry about it slipping from my grip and careening down a hill into the creek. The park was different with no baby. It seemed much safer.

Then we found the squirrel. Stu walked right past it, didn't even notice, but I saw it. It was lying on its side in the grass. Its mouth was open, its eyes empty holes. Other than that it was fine. Perfectly whole, not the work of a cat or a child with a BB gun.

(to the dog) Stu. Stu, come here baby. (to the audience) He stopped, turned back, then trotted to where I was kneeling on the ground. He saw the squirrel and stopped for a second. He looked at me. I reached out to touch the squirrel and Stu took a step back. Its fur was damp and brittle. Stu walked up to the squirrel, then turned his head away and looked at me like I had gotten him into something he wasn't near ready for. A fly landed on the squirrel's head and crawled into the empty eye socket.

(to the dog) Stu. This is important. (takes his head and turns it toward the rodent, pushing his nose closer to the body) The squirrel's dead. You understand? (to the audience) Squirrels, I could hear Stu thinking. I chase these things. This squirrel is not running. Stu backed away from the animal. I tried to hold on to him but he pulled me backward and I fell from my knees onto the wet grass. Stu ran in circles around me, afraid he was in trouble . . . So we were going to go out for dinner. Todd came home and sat on the couch in a heap. His tie was askew and his hair mussed. I asked him if he had a bad day and he said he was just a little tired. (to Todd) Does that mean we're not going to dinner?

TODD: (wearily) I didn't say that. I didn't say we weren't going out. (pause) Where do you want to go?

NARRATOR: We could go someplace fancy. We haven't been someplace fancy in a long time.

TODD: (noticing the dog) What's up with him?

NARRATOR: I told you. He's confused.

TODD: He's confused. The dog is confused. (shakes his head sadly)

NARRATOR: (to the audience) I was trying to think of a way to make a case for how confused Stu really was, but Todd didn't seem receptive to the idea.

TODD: (loosening his tie) Let me change. We'll go out. I just have to get out of these clothes.

NARRATOR: (to the audience) I sat on the couch with Stu and waited. Stu put his head on my thigh and looked up at me. I wanted to do something for him, take him out to dinner with us to get his mind off the mystery of the missing baby. We sat there for a few minutes. I couldn't hear any noises coming from the bedroom, so I got up and went down the hallway. I looked in the door and saw Todd sitting on the edge of the bed. He was banging the side of his head, crying while he was doing it. Actually he wasn't really crying. He was more making little howling noises with his throat. And he just kept whacking himself on the head.

I went back into the living room. I had a desire to get Stu off the couch and give him a push toward the bedroom, so he could stumble upon Todd and see what the death thing was all about, but I didn't have the heart . . .

I woke again in the middle of the night, but I didn't hear any crying. I got out of bed anyway and went into the baby's room. Stu hopped up and followed me, hopefully, but the room was still empty except for the chair by the window. Still, the dog wandered around, sniffing out the emptiness, the way he had the day before, and the day before that, and the way I realized he probably would for quite a while. I sat down in the chair by the window.

Everything was quiet, and I thought of saying to Stu that that was it, that was death, the quiet. But Stu was still sniffing around the room, trying to pick up the scent of the baby, and I realized he would never understand death. All he would come to understand was that the baby was not coming back.
```

---

## IC-0140: Extenuating Circumstances

- Title: Extenuating Circumstances
- Author (byline): Joyce Carol Oates
- Work: Haunted: Tales of the Grotesque
- Publisher: Dutton Books
- Publication date as stated: 1994
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1688
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joyce Carol Oates
Book: Haunted: Tales of the Grotesque
ISBN: 978-0525936558
Publisher: Dutton Books
Date (Month/Year): 1994
```

### Introduction (context only: never use it for content warnings)

```text
I offer you . . . . A mother's tale about murdering her two-year-old child and her reasons for doing so. Every sentence begins with "Because" and ends with a twisted explanation. For every action there is always a plethora of Extenuating Circumstances by Joyce Carol Oates.
```

### Performance text (classify this)

```text
• Because. it was a mercy.
• Because God even in His cruelty will sometimes grant mercy.
• Because Venus was in the sign of Sagittarius.
• Because you laughed at me, my faith in the stars. My hope.
• Because he cried, you do not know how he cried.
• Because at such times his little face was so twisted and hot, his nose running

with mucus, his eyes so hurt.
• Because in such he was his mother, and not you.
• Because I wanted to spare him such shame.
• Because he remembered you, he knew the word Daddy.
• Because watching TV he would point to a man and say, Daddy-?
• Because this summer has gone on so long, and no rain. The heat lightning

flashing at night, without thunder. • Because in the silence, at night, the summer insects scream. • Because by day there are earthmoving machines and grinders operating hour

upon hour razing the woods next to the playground. • Because the red dust got into our eyes, our mouths. • Because he would whimper Mommy?-in that way that tore my heart.

• Because last Monday the washing machine broke down, I heard a loud

thumping that scared me, The dirty soapy water would not drain out. • Because in the light of the bulb overhead he saw me holding the wet sheets

in my hand crying What can I do? what can I do? • Because the sleeping pills they give me now are made of flour and chalk, I am

certain. • Because I loved you more than you loved me even from the first when your

eyes moved on me like candleflame. • Because I did not know this yet; yes I knew it but cast it from my mind. • Because there was shame in it. Loving you knowing you would not love me

enough. • Because my job applications are laughed at for misspellings and torn to

pieces as soon as I leave. • Because they will not believe me when listing my skills. Because since he was

born my body is misshapen, the pain is always there. • Because I see that it was not his fault and even in that I could not spare

him.

• Because even at the time when he was conceived (in those early days we

were so happy! so happy I am certain! lying together on top of the bed the

corduroy bedspread in that narrow jiggly bed hearing the rain on the roof

that slanted down so you had to stoop being so tall and from outside on the

street the roof with its dark shingles looking always wet was like a lowered

brow over the windows on the third floor and the windows like squinty eyes

and we would come home together from the University meeting at the Har-

dee's corner you from the geology lab or the library and me from Accounting

where my eyes ached because of the lights with their dim flicker no one else

could see and I was so happy your arm around my waist and mine around

yours like any couple, like any college girl with her boy friend, and walking

home, yes it was home, I thought always it was home, we would look up at the

windows of the apartment laughing saying who do you think lives there? what

are their names? who are they? that cozy secret-looking room under the

eaves where the roof came down, came down dripping black runny water I

hear now drumming on this roof but only if I fall asleep during the day with

my clothes on so tired so exhausted and when I wake up there is no rain, only

the earthmoving machines and grinders in the woods so I must acknowledge

It is another time, it is time) yes I knew.

• Because you did not want him to be born.

• Because he cried so I could hear him through the shut door, through all the

doors.

• Because I did not want him to be Mommy, I wanted him to be Daddy in his

strength.

• Because this washcloth in my hand was in my hand when I saw how it must

be.

• Because the checks come to me from the lawyer's office not from you.

• Because in tearing open the envelopes my fingers shaking and my eyes

showing such hope I revealed myself naked to myself so many times.

• Because to this shame he was a witness, he saw.

• Because he was too young at two years to know. Because even so he knew.

• Because his birthday was a sign, falling in the midst of Pisces. Because in

certain things he was his father, that knowledge in eyes that went beyond

me in mockery of me.

• Because one day he would laugh, too, as you have done.

• Because there is no listing for your telephone and the operators will not tell

me.

• Because in any of the places I know to find you, you cannot be found.

• Because your sister has lied to my face, to mislead me.

• Because she who was once my friend, I believed, was never my friend.

• Because I feared loving him too much, and in that weakness failing to

protect him from hurt.

• Because his crying tore my heart but angered me too, so I feared laying

hands upon him wild and unplanned.

• Because he flinched seeing me. That nerve jumping in his eye.

• Because he was always hurting himself, he was so clumsy falling off the

swing hitting his head against the metal post so one of the other mothers

saw and cried out Oh.' oh look your son is bleeding! and that time in the

kitchen whining and pulling at me in a bad temper reaching up to grab the pot

handle and almost overturning the boiling water in his face so I lost control

slapping him shaking him by the arm Bad! bad! bad! bad! my voice rising in

fury not caring who heard.

• Because that day in the courtroom you refused to look at me your face shut

like a fist against me and your lawyer too, like I was dirt beneath your shoes.

Like maybe he was not even your son but you would sign the papers as if he

was, you are so superior.

• Because the courtroom was not like any courtroom I had a right to expect,

not a big dignified courtroom like on TV just a room with a judge's desk and

three rows of six seats each and not a single window and even here that

flickering light that yellowish-sickish fluorescent tubing making my eyes

ache so I wore my dark glasses giving the judge a false impression of me,

and I was sniffing, wiping my nose, every question they asked me I'd hear

myself giggle so nervous and ashamed even stammering over my age and my

name so you looked with scorn at me, all of you.

• Because they were on your side, I could not prevent it. Because in granting

me child support payments, you had a right to move away.

• Because I could not follow.

• Because he wet his pants, where he should not have, for his age.

• Because it would be blamed on me. It was blamed on me.

• Because my own mother screamed at me over the phone. She could not help

me with my life she said, no one can help you with your life, we were

screaming such things to each other as left us breathless and crying and I

slammed down the receiver knowing that I had no mother and after the first

grief I knew It is better, so.

• Because he would learn that someday, and the knowledge of it would hurt

him.

• Because he had my hair coloring, and my eyes. That left eye, the weakness in

it.

• Because that time it almost happened, the boiling water overturned onto

him, I saw how easy it would be. How, if he could be prevented from

screaming, the neighbors would not know.

• Because yes they would know, but only when I wanted them to know. • Because you would know then. Only when I wanted you to know. • Because then I could speak to you in this way, maybe in a letter which your

lawyer would forward to you, or your sister, maybe over the telephone or

even face to face. • Because then you could not escape. • Because though you did not love him you could not escape him.

• Because I have begun to bleed for six days quite heavily, and will then Spot

for another three or four. Because soaking the blood in wads of toilet paper

sitting on the toilet my hands shaking I think of you who never bleed.
• Because I am a proud woman, I scorn your charity.
• Because I am not a worthy mother.
• Because I am so tired.
• Because the machines digging in the earth and grinding trees are a torment

by day, and the screaming insects by night. • Because there is no sleep. • Because he would only sleep, these past few months, if he could be with me

in my bed.
• Because he whimpered, Mommy!-Mommy don't!
• Because he flinched from me when there was no cause.
• Because the pharmacist took the prescription and was gone such a long time,

I knew he was telephoning someone. • Because at the drugstore where I have shopped for a year and a half they

pretended not to know my name. • Because in the grocery store the cashiers stared smiling at me and at him

pulling at my arm spilling tears down his face. • Because they whispered and laughed behind me, I have too much pride to

respond. • Because he was with me at such times, he was a witness to such. • Because he had no one but his Mommy and his Mommy had no one but him.

Which is so lonely. • Because I had gained seven pounds from last Sunday to this, the waist of my

slacks is so tight.
• Because I hate the fat of my body.
• Because looking at me naked now you would show disgust.
• Because I was beautiful for you, why wasn't that enough?
```

---

## IC-0141: Fairness

- Title: Fairness
- Author (byline): Chinelo Okparanta
- Work: Happiness, Like Water; Pgs 32-40
- Publisher: Mariner Books
- Publication date as stated: Aug 2013
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CHINELO, BARNA, ENO, EKAITE, MAMA, PAPA
- Teaser before the introduction: No
- Spoken words (computed): 1588
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chinelo Okparanta 2017 National Qualifier
Book: Happiness, Like Water; Pgs 32-40 2023 National Qualifier
ISBN: 978-0544003453 NIETOC
Publisher: Mariner Books
Date (Month/Year): Aug 2013
* Intro Source and additional information about skin bleaching in African Nations.
https://files.aho.afro.who.int/afahobckpcontainer/production/files/Skin_Bleaching_in_Africa_reg
ional_fact_sheet_Nov23.pdf
```

### Introduction (context only: never use it for content warnings)

```text
Whether we like to admit it or not, our global society is segregated -- divided by tribe, religion, even skin color. Colorism, much like racism, is a form of discrimination that regards darker skin as inferior, ugly and unacceptable and lighter or “fair” skin as superior. All over the world, people with darker skin tones attempt to gain social acceptance by bleaching their skin. It is not uncommon to see videos of people peeling off layers of their skin to reveal a lighter hue. In fact, according to a 2023 World Health Organization report*, 77% of Nigerian women use skin bleaching products.

In this selection, Nigerian author Chinelo Okparanta shares a tale from her youth even though it’s ugly – inferior -- unacceptable. Her actions were all in the quest for. . . Fairness by Chinelo Okparanta
```

### Performance text (classify this)

```text
CHINELO: (Pgs 32-40) We gather outside the classroom in the break between morning and afternoon lectures. We stand on the concrete steps, chewing groundnuts and meat pies, all of us with the same dark skin, matching, like the uniforms we wear. All of us, excepting Onyechi of course, because her skin has now turned color, and we are eager to know how. She no longer belongs. She is now one of the others, one of the girls with fair skin.

BARNA: (chuckling in disbelief; she claps her hands, eyes wide) 'Chi mo! My God! How fast the miracle!

CHINELO: Onyechi shakes her head, tells us that it was no miracle at all. She tells us of the bleach. I listen and nod, trying to catch every bit of the formula. Our skin is the colour not of ripe pawpaw peels, but of its seeds. We are thirsty for fairness. I think of returning home and telling Eno.

Hours later, I sit on a stool outside. Ekaite is at the far end of the backyard where the clotheslines hang. She collects Papa's shirts from the line, which wave in the breeze like misshapen flags. Even in the near darkness, I can see the yellowness of Ekaite's skin. A natural yellow, not like Onyechi's or some of the other girls'. Not like Mama's.

Eno sits with me. It is late evening, and the sky is grey. Mosquitoes swirl around. (swats at biting mosquitoes) At the clothesline, Ekaite is slapping even more than Eno and I. Her skirt only comes down to her knees. (to Eno) They bite us all the same.

ENO: (with angry dejection) No, they bite Ekaite more. Even the mosquitoes prefer fair skin.

CHINELO: The scent of chlorine billows in the air, and I think of Onyechi. I toss it about in my mind, like a pebble in the air, to get a feel for its texture, its potential, its capacity for success. And then I tell Eno.

When the sky grows black, we go into the house. We cut through the kitchen, pass the dining room, and enter together into the bathroom. Papa and Mama do not catch us. In the bathroom, we pour bleach into the bucket, only a quarter of the way full. Then we watch water bubble out of the faucet. We inhale and exhale deeply, and the sound of our breathing is weirdly louder than the sound of the running water. We turn the faucet off and gaze into the bucket.

EKAITE: Eno . . . Eno!

CHINELO: (both girls jump) Eno runs off to answer, more quickly than usual because she knows she should not be in the bathroom with me. She must use the house girls' bathroom, outside in the far corner of the backyard. But mostly, Eno runs off, because dinner will be served in an hour, and Eno will have to help in its preparation.

At the dining table, Papa sits at the head, Mama by his side. The scent of egusi soup enters through the kitchen. Mama picks up her spoon, looks into it, unscrews the tiny canister, still with the spoon in her hand. The lipstick is a rich colour, red like the hibiscus flower; and it rises from the container slowly, steadily, like a lizard cautiously peeking out of a hole. Overhead the ceiling fan rattles and buzzes. The air conditioner hums, like soft snoring. In the kitchen we hear the clangclanging of food preparation: of the pestle hitting the mortar, yam being pounded for the soup. And then I hear the shutting of the fridge, that shiny, stainless-steel door all the way from America. And I wonder if Ekaite ever takes the time to look at her reflection in the door. And if she does, does she see herself in that superior way in which I imagine all fair people see themselves?

A bowl of velvet tamarinds sits at the centre of the table. Mama bought the bowl on one of her business trips overseas. She returned from that trip with other things too -- silk blouses from Macy's, Chanel, Nike apparel. The evening she returned, she held up the overseas items for me to see. One blouse she held to my chest. It was the yellow of a ripe pineapple.

MAMA: Will lighten you up. . .

CHINELO: The first magazine arrived two weeks later, Cosmopolitan, pale faces and pink lips decorating the cover, women with hair the colour of fresh corn. Next was Glamour, then Elle.

I remember the bucket in the bathroom, and I feel hope billowing in me. Eno serves our food -- dishes of pounded yam and soup. Mama waves Eno away. I watch her hand waving, the gold rings on her fingers, the bracelet that dangles from her wrist.

MAMA: U zoamaka. You are looking very tattered today. It's no way to present yourself at the dinner table.

CHINELO: The words tumble out of her mouth that American way, one tumbling into the next with no space between. Papa looks at me for a moment, as if for the first time in a long time.

PAPA: How was school today?

MAMA: (to Papa) A good week. A good month even. Imagine, an entire month and no strike! Surprising, with the way those lecturers are always on strike. Not to worry. (pause) Arrangements are already being made. (to Chinelo) You need a good education. That is what America will give you. A solid education. And no strikes. (smiling widely) With a degree from America, you can land a job with a big company here, or maybe even remain in America. Land of opportunities. (pause) In the meantime, you can't walk around looking tattered, shirt untucked, hair unbrushed. As for your face, dab some powder on. It will help brighten you up. (clears her throat) Even Ekaite presents herself better than you do. Very well mannered, that one. Takes care of herself. Beautiful all around.

CHINELO: (rolling her eyes) Eno is pretty too.

MAMA: (mocking in a sing-song) Eno is pretty too. Eno is no comparison. No comparison at all.

CHINELO: It's only bias, the way Mama feels about Ekaite. Ekaite's face reminds her of the faces she sees on her magazines. Because, of course, Ekaite's complexion is light and her nose is not as wide and her lips not as thick as mine or Eno's.

I remember the first time [Mama] came back with boxes of those creams. Esoterica, Movate, Skin Success, Ambi. It was around the time television commercials started advertising them -- the fade creams. We'd go to the Everyday Emporium, and there'd be stacks of them at the entrance. It was around this time too that the first set of girls in school started to grow lighter. Mama's friends started to grow lighter, too. Mama did not at first grow light with them. She was cautious. She'd only grow light if she had the best-quality creams, the kinds she knew America would have, not just the brands they sold at the Everyday Emporium.

In just a few weeks, her skin had turned that shade of yellow. She insisted I use the cream too. With Movate, dark and light patches formed all over my skin, like shadows on a wall. She insisted I stop. People would know, she said. Those dark knuckles and kneecaps and eyelids. People would surely know. We tried Esoterica next. No progress at all. Same with Skin Success and Ambi.

I tell Mama that I'm not feeling well and excuse myself from the table before she has a chance to respond. I carry my dishes into the kitchen, where Eno is waiting for me. Inside the bathroom, the air is humid and smells clean, purified, a chemical kind of fresh. Eno holds the towel and stands back, but I call her to me, because I am again finding myself skeptical of the water and bleach. Fear catches me, and I think perhaps we should just pour everything out. But then I hear Mama's voice, saying, ' Eno is no comparison. No comparison at all.' (taking the towel from Eno) You should go first. You're not supposed to be here. That way you'll be done by the time anyone comes to chase you out.

(to audience) She gets on her knees so that her face is just above the bucket. (to Eno) We'll do only the face today. Only get up when you feel you feel something like a tingle. (Eno takes a deep breath and dips her face into the water; long pause) Do you feel it yet? (Eno shakes her head face still in the water, long pause) Not yet? -- Okay. Come up. (Eno lifts her face from the water and takes a shuddering breath)

(to audience) The colour of her skin seems softer, a little lighter than before (to Eno, smiling) It's working! But we need to go full force. (to audience) The bath bowl is sitting in the sink. I pick it up, pour the bleach straight into it. I call Eno to my side, tell her to place her face into the bowl. (Eno takes a deep breath and dips her face into the bleach)

ENO: (screams and screams)

CHINELO: Her scream fills the bathroom. There is the thud of the door slamming into the wall. Ekaite rushes towards us. She holds Eno's face in her palms.

ENO: (twisting her face away, screaming)

CHINELO: I feel the pain in my own face. Papa looms in the doorway

PAPA: (fiercely) What did you do to her? What did you do?

CHINELO: In the doorway, I see Mama just watching. I turn to him, wanting desperately to make my case, but I don't find the words. My legs feel weak. I think of Mama and her creams. (to Eno) Don't worry. We'll find something that works. . .

Days later, when the scabs start to form, I imagine peeling them off. Eno's flesh underneath the scabs is reddish-yellow, not quite the yellow of a ripe pawpaw peel. And even if I know that this scabby fairness of hers is borne of injury -- a temporary fairness of skinless flesh, patchy and ugly -- I think how close she has come to having skin like Onyechi's, and I feel something like envy in me, because what she has wound up with is fairness after all. Fairness, if only for a while.
```

---

## IC-0142: The Family Tree

- Title: The Family Tree
- Author (byline): Karen Smith Vastola
- Work: The Best Women’s Stage Monologues of 1998
- Publisher: Smith and Kraus
- Publication date as stated: Sept 1999
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ELIZABETH
- Teaser before the introduction: No
- Spoken words (computed): 1170
- Already set (do not supply): none

### Source block (context only)

```text
Author: Karen Smith Vastola
Book: The Best Women’s Stage Monologues of 1998
ISBN: 1575251841
Publisher: Smith and Kraus
Date (Month/Year): Sept 1999
```

### Introduction (context only: never use it for content warnings)

```text
ELIZABETH: No one ever seems to pay religion much mind until they absolutely have to. You don’t focus on where you’re going to spend eternity until you find out just how close that eternity is. You begin to think differently when you realize your day is coming sooner than you had expected. There are so many questions to be answered. What’s going to happen to you after you die? What’s going to happen to your family after you die? It may be time to re-evaluate this whole “religion” thing, and what better place to start than “The Family Tree” by Karen Smith Vastola.
```

### Performance text (classify this)

```text
(Cancer has taught Elizabeth to prepare for the future. Here, she explains why she's become a Methodist.)

ELIZABETH: Do you know I've recently changed religions? I mean, I've become a member of another faith, so to speak. Do you find that interesting? I find it amazing. Or at least, found it amazing. Now, I think nothing of it. As if I were always a Methodist. Born a Methodist. Not the Roman Catholic that I was baptized when I was six weeks old. My mother. God. My mother was horrified. Horrified. When I broke the news, about being a Methodist. Although there's not much to become. You just show up at the church on Sundays, sing some John Wesley hymns, and join your fellow parishioners for coffee and cookies after the service. Anyway, I told my mother on New Year's Eve. It had become a particularly boring moment in the festivities, the family party we have every New Year's. It was about ten-thirty. Everyone was laying allover the chairs and sofas in my sister's living room after having eaten and drunk too much. All except me, I hadn't drunk a thing. Methodists don't drink. That seemed to be another good reason to be a Methodist. There must be a lot of alcoholics in the Methodist church. Or recovering alcoholics. I was one. I hadn't had a drink in five years. I quit for health reasons. What a joke. So this was my fifth year of sobriety at the family New Year's party. And you know how those things go. You could always use a good buzz on to get through those things. So I was sitting there thinking about that fact and I tried to think of something I could say to liven things up. You know something I would probably say if I did have a good buzz on. I mean here we are, an hour and a half to ball-drop time. No one's talking. Everyone's just laying there staring at the twentieth century fireplace-the television. Only during the holidays it's not even television, if there is a child under twenty around or an adult male-it's Nintendo! We're all staring at the James Bond Golden-Eye Game. You know (Hum theme music.) daada dadad dada. My nephew has worked his way up from pistol to flame thrower to a.k.70. And I think, why not now? Why not drop the news right now. They can't be really angry with me for turning my back on eighteen years of Catholic education. They'll be grateful to throw some insults my way. They should thank me for relieving the boredom. So I say, nice and loud, to wake up the ones that are sleeping with their eyes open. "You know Janey and I have been going to the Methodist church for the past couple months." "What?" my mother says. That got her. She was just about to nod off into REM sleep, but that statement brought her back. "Now, Elizabeth, don't tell me you're going to a Methodist church. Roaring Methodist? And you're bringing your daughter? Now don't tell me you're doing that?" We've been doing it and we both enjoy it. Janey has found a little friend to play with in Sunday school and I like the desserts. "She likes the desserts," my sister screams and almost falls off her chair with laughter. "It worked," I say to myself. Two of them are up and breathing. So I send off another zinger. "I even baked some muffins and poured the coffee myself last Sunday." Well they all carried on for about a half hour with that news. My mother leading the pack with warnings about how once you do a coffee, little by little they'll sucker you into all kinds of activities and before you know it you'll be washing the floors and then sleeping on them because they'll ask you for money and you'll give it all to them and then you'll have no place to live. Like Catholics never ask you for a dime, I could have countered. But I don't say much, just let them rave on. At eleven they run out of juice, but its got their adrenaline flowing again and several of them get up and walk around looking for even more to eat and drink. I'm satisfied with the results. They've been introduced to the topic. Now when my mother calls me on Sunday she won't be shocked to hear I'm at church and that it's not the Catholic one. Let them think what they want; they don't have to know the other reasons I became a Methodist, not yet. Let Janey think she's found a new playmate and not that in some of those Sunday school lessons they'll be some discussions about life and death and the sweet hereafter. You know just in case she has to try and understand it and I won't be there to explain. Not that I'm going to die anytime soon. Of course I'm not. The doctors don't think so. It's just that I may die sooner than everyone else I know. Or I may not. Everyone else I know could step off a curb tomorrow and be hit by a truck. That's what the doctors tell me when I want to talk about numbers and probability of cure or re-occurrence. So I'm just warning everyone out there. Don't count on anything. It could happen to all of you tomorrow. Anyway, the church will just be one more thing for Janey that will be there for her if I'm not. And they're all very friendly there and she likes their cookies too. And they'll know her and they would have known me. And that's the other reason I joined the church, because it's small and friendly and they know me. And if the time ever comes. I mean if it comes sooner rather than later, they'll know me and my husband and family won't have to decide whether to slip some old, half-in-the-bag Catholic priest a fifty or a hundred as they try and sum up my life in five simple sentences so that someone I don't even know can stand there in front of a dead person he doesn't even know and repeat the five big occurrences or concerns of my life punctuated by, "God rest her soul," or "She's found her peace now." I really don't want to leave that way. I mean I want some kind of personal association, even if my minister only says, "I liked her cranberry muffins, or sometimes I'd look over at her while she was singing a hymn and I'd see tears in her eyes or she always shook my hand and said good morning and sometimes complimented my sermon and she meant it." And he would have known me, when I was alive and not just dead... But that's not something you can easily explain to your family or your mother on New Year's Eve. So let them think I became a Methodist because I like their cookies...1 do like their cookies.
```

---

## IC-0143: Fifteen Minutes (from Talking With)

- Title: Fifteen Minutes (from Talking With)
- Author (byline): Jane Martin
- Work: Talking With
- Publisher: Samuel French, Inc.
- Publication date as stated: April 1983
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS
- Teaser before the introduction: Yes
- Spoken words (computed): 1024
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jane Martin
Book: Talking With
ISBN: 978-1880399200
Publisher: Samuel French, Inc.
Date (Month/Year): April 1983
```

### Introduction (context only: never use it for content warnings)

```text
All the world's a stage, And all the men and women merely players; They have their exits and their entrances, And one man in his time plays many parts, You may recognize this as a quote from As You Like It by William Shakespeare, but the words are just as true today as when they were penned in the 16th century. In Fifteen Minutes by Jane Martin we are allowed into the thoughts of a working actress who pours herself out on the literal and figurative stage of life.
```

### Performance text (classify this)

```text
A theatrical dressing room. A table and chair. Makeup for the evening's production is laid out on the table. Over the loudspeaker we hear the Stage Manager call, "15 minutes, please. The call is 15 minutes." The actress enters hurriedly and goes to the table. She wears a kimono over a slip.

During the course of the piece she completes her makeup and dresses for the play she is doing.

Though not actually present she looks into a mirror and thus directly toward the audience. She speaks to an unseen dressing room partner.

ACTRESS: Anyway, this guy, the director, actually used a buzzer. ZZZZZZZZZZZ. Really. He would sit there wearing a Yankee's baseball cap and push this buzzer after each laugh line for as long as he thought the laugh would last. Laugh line. ZZZZZZZZZ. This was to train us not to step on the laugh. Can you believe it? Really. Oh, he trained us, believe me. The show opens, there are no laughs but we are waiting for the buzzer. A two-hour play lasted three hours while we paused for laughs that didn't exist. I aged seven years in a night. Directors! Last year I did Katrin in Mother Courage for this really dour, silent, unapproachable, East German woman. She sat on a camp stool, immovable, for hours during rehearsal. With her eyes closed yet. No reactions. Really. I felt like a radio show. Anyway, after a week she asks me out for a beer and suggests that we should sleep together to get in tune with the play. I tell her she wants to get in tune with the play she should sleep with the author. She says, 'My dear, Bertholt has been dead for thirty years!' I said, 'In that case you're perfect for each other.'

(S)HE called fifteen right? My! Sooooooo, we're really going to do this? Of course we are. It's really mysterious, you know? I mean they're already out there right? Sitting out there. Eating little candies. Peering in pocket mirrors. Who are they? Who knows. What are they expecting? Who knows. We do it. They watch it. We finish. They applaud. They go home. We go home. What was it? Who knows.

What I want to know, is how the hell do they live in a town like this without a decent Chinese restaurant?

O.K., O.K., O.K., O.K., ... so, it's fifteen and I am in here getting ready for an evening of 'lacerating self exposure' and there are people out there reading the program, reading my bio, you know getting a little personal insight, getting to know me. And what I want to know . . . you think this is enough eyes for this house? Great. And what I want to know is who are they? Fair's fair, right?

What I would like other than some decent light in this dressing room what I would like is a program delivered to me every night with bio's of the audience, you know, so we'd start out even ... I am really a mutt, you know it? ... where they live, last play they saw, favorite color, sexual preference, last relationship they screwed up, you know just basic stuff. Because then we'd be in this together, right? I do a little lacerating self exposure, they do a little lacerating self exposure and afterwards who knows maybe we get together for a drink, because then ... O.K., what you see is what you get ... because then there would be an exchange, an exchange and not this unilateral crap, this "I'm in the light, you're in the dark" stuff, which truth to tell is beginning to wear on me. Me. Moira, the semi-Taurus from Julliard, with two Broadway credits, this baby, and an unreleased horror film where I am eaten by stone griffins on the towers of Notre Dame.

(Stage Manager's voice: "5 minutes. The call is 5 minutes, please.") Right; five minutes, right. (SHE begins to put on her clothes.) I mean I have nothing against these people, these humans who have paid their money, some would say too much money, for an evening of ... for an evening of ... (SHE pauses a moment transfixed by a memory.) Entertainment. Wow. Y'ever think of it like that ... what you are, you, are an entertainment? I strike me as a number of things, but I do not strike me as ... look, what I would like ... once ... just after my entrance, is to walk downstage ... (SHE does, right to the footlights.) and say, "Excuse me. Excuse me, could we have the house lights for a second please?" (They come up.) Hey, O.K., thanks. And I would like to look at them, the people who seriously believe that I am an entertainment ... Hi ... How are you? I would just look at them, you know, take them in ... (SHE does. A fairly long pause.) And then I would say ... see this would be better already ... I mean it's better to have seen their faces. I would say that I'm ... a little fragile ... freaked out, you know ... sort of at the end of a personal relationship ... I mean not the character, well I mean the character is too but ... you've all been through that, right? The end of a crucial relationship? You know, the self-doubt and everything ... the feeling that you're not lovable ... that you're a mutt, too much of a mutt to be loved . . . and that you have . . . I don't know. . . a crisis of confidence ... is that a good description?

That it's hard to act ... hard to be the entertainment for people you don't know ... haven't looked at. So I just needed to see you tonight, O.K.? Just see you for a minute. That's all ... O.K.? (The stage manager calls places: "Places, please. The call is places. Places, please." SHE stands a moment longer and then moves back up to the dressing table. The house lights fade.) Sooooooooo. Hey, O.K.! Ready to Rock-and-Roll, right? Ready to do it in the dark. For whoever and whatever, whoever makes of it. Hey, that's the way it's 'sposed to be. They got a law on this thing. Besides, hey listen, I ain't a mutt. I am supremely self-confident. I lacerate with my self exposure. Listen, don't screw with me, they said it in the newspaper! I am the entertainment and when lope' my lips, let no dog bark! Plus, fuck 'em if they can't take a joke right?

(SHE checks the mirror one more time.) And me, hey, I'm the joke! (SHE loses herself again for a moment, staring in front of her, just for a moment.) On the other hand, I'm in the light. (SHE crosses out right. Lights fade out, sound of vacuum, which continues during scene change.)
```

---

## IC-0144: Final Placement

- Title: Final Placement
- Author (byline): Ara Watson
- Work: Win/Lose/Draw
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MARY, LUELLEN
- Teaser before the introduction: Yes
- Spoken words (computed): 1534
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ara Watson
Book: Win/Lose/Draw
ISBN: 978-0822212621
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
Placements in foster care have dramatically increased over the past 10 years. Today over 500,000 children in the U.S. currently reside in some form of foster care. What leads to such drastic measures by social service workers? Simply put, many of these children have suffered some form of serious abuse or neglect—removal of these children from their homes is a protective measure. The situation is stressful for all involved . . . parents, children and the social workers who attempt to intervene in the best interest of the child. Stress often leads to parental violence directed toward the social workers themselves. In fact, Seventy (70) percent of front-line caseworkers have been victims of violence or received threats of violence. In protecting children from domestic violence, the very people who intervene become targets themselves.

Final Placement by Ara Watson.
```

### Performance text (classify this)

```text
MARY: (To Audience/Dictation) Last name: James. First name: Jimmy. Age: four years. Date: October ten, 1981. This office was contacted by Dr. Timothy Bowman of the Northside Medical Clinic concerning four-year-old Jimmy James. Dr. Bowman reported that he has treated Jimmy twice in the last six weeks-once for a cut over the eye and once for a broken wrist. The parents attributed both injuries to accidents. On each of the visits, Dr. Bowman noted the child had a number of bruises on his body which the mother explained resulted from Jimmy's-quote-"always falling down"-end quote. On the second of these visits with Jimmy, Dr. Bowman also noted burn marks on the child's buttocks which he believed were caused by a cigarette. He determined at this point to contact this office and request an investigation of the situation by the Department.

MARY: What are-? (A moment’s hesitation.) Hello. You . . . you startled me.

LUELLEN: There wasn't no one at the front desk.

MARY: Oh? Well, she. . . she must have stepped away a minute.

LUELLEN: I heard your voice, so I followed it, but I didn't want to disturb you. Boy, sure is quiet up here.

MARY: Yes. Yes, I guess it is.

LUELLEN: Where is everybody anyway? Looks like you're the only one in the whole place.

MARY: (quickly lying) No. Everybody's here. They're all . . . just busy. . . keeping their heads down. But. . . they're all here. I like your hair like that.

LUELLEN: Needs cuttin'.

MARY: No, I like it longer. Makes you look . . .It's nice. (Slight pause.) How is . . . Are you all right?

LUELLEN: I walked all the way here.

MARY: From your house?

LUELLEN: Must be ten miles, I bet. Don't you think it's about that? 'Bout ten miles?

MARY: Well . . . It's certainly longer than I'd care to walk, anyway. Especially today. Did you. . . come just co see me or . . . ? (Luellen nods but avoids looking at Mary.) Well, I'm glad to see you, Luellen, but, you know, it might have been better if you'd called me first . . . to make sure I was in, that I didn't have a client with me . . . (Luellen still doesn't look at her.) You lucked out, I guess.

MARY: (To Audience/Dictation) The worker has visited twice weekly with Jimmy since his removal from the James home and his subsequent placement in foster care on October 19. Mr. and Ms. James have remained in group therapy, and it is that group leader's judgment that both, but especially Ms. James, have made substantial progress. As a result, the court has ordered that supervised trial visits between Jimmy and his natural parents begin immediately with the goal of eventual reintegration of the James family.

MARY: Luellen, you walked a very long way on a very hot day to see me . . . Luellen? . . . (Luellen looks at her quickly and then away.) I would like to know why - what I can do to help you - but you are going to have to tell me. (No response.) Will you? (No response.) Well. I'm sorry, I wish I had more time, but I do have this appointment, so, if you'll let me get my things together, I'll take you . . .

LUELLEN: (quickly and with a new energy) No, but, see, see, I got this real good idea. It's real good, too. See, I'm fixin' to move out on Ol' Ray. He just don't know it yet, but I am. I'm goin' to get me a place to live and I'm goin' to get me a job maybe with the phone company maybe. My girlfriend works for the phone company. Or a waitress. I could do that.

MARY: Jobs are a little hard to find these days, but. . . but that sounds. . . I think you'd enjoy working . . .

LUELLEN: (big smile) I think I would, too; and my girlfriend lives in a duplex and her neighbors is goin' to move maybe and I could move in there if they did. It's got a fenced-in backyard and a big side yard and I wouldn't even let Ol' Ray even come visit only if he got over doin' them things.

MARY: (realizing) Wait a minute

LUELLEN: (going on) I know he don't mean to. He just loses his temper sometimes is all, but he's gettin' a whole lot better 'bout it since we went to that group. I sure to 'preciate you makin' us go to them meetin's. See, we had a lot of pressure on us and we was probably just takin' it out on . . .

MARY: Luellen. Wait a minute here.

LUELLEN: No, no. I still wouldn't let him' come and stay. Not no matter how much he yelled at me or how much 'he begged me, he couldn't. A daddy don't need to be with his son like a mama does. (Slightly choked, but going on.) A mama needs to be with her child. You know that, don't you? I know you do and I'm goin' to get a place for me and Jimmy to live and you can . . .

MARY: You know that's . . .

LUELLEN: (going on) And you could come visit Jimmy ever'day. You could take him out in your car and you could buy him a Coke and ask him questions. . . I'd share him with you. We could share him. (She looks pleadingly at Mary. Pause.)

MARY: Luellen, please don't do this to yourself.

LUELLEN: I ain't

MARY: You're hurting yourself with this. You're building up a fantasy that

LUELLEN: It ain't a fantasy. I thought it all out.

MARY: Thinking it out doesn't mean it can happen that way.

LUELLEN: (a protest) Yes!

MARY: No. I'm sorry.

LUELLEN: (looks at her a moment quietly) You ain't sorry.

MARY: Yes, I am. I'm sorry for how you feel right now. I know how very

LUELLEN: You know what? You know what it's like to have your kid stole by the Welfare? To sit in a room and remember that your little boy ain't bein' quiet 'cause he's sleepin' or into somethin', but that he's bein' quiet 'cause he ain't even there no more. And you don't know where he is or when he's comin' back? You don't know.

MARY: No. I guess. . . no one can. . . really. . . but you have to. . .

LUELLEN: (watching her coldly) What? I have to what? Forget about him? You ain't got no kids, do you?

MARY: No.

LUELLEN: No. You want one?

MARY: Someday. . .

LUELLEN: Like my Jimmy? (Mary doesn't answer this.) I know you like him a whole lot. You like him better than the other ones? He your favorite? You know what Ol' Ray told me once after you'd come out to visit? He said, “You better watch out, Lu girl. That woman wants your baby for herself and she's a' gonna get him, too." That's what he said, but I didn't believe him. Sometimes, though, that Ray knows what he's talkin' 'bout. You got him?

MARY: What?

LUELLEN: You got him at your house, ain't you?

MARY: No. That's

LUELLEN: You don't want me to know where you live 'cause

MARY: This is a state agency. There are rules here, Luellen. Even if I wanted to do something like-

LUELLEN: Oh, you want to. You want to and you did. (The two look at each other a long moment.)

MARY: (reasonably) No matter how much I care about Jimmy -- and I do, I care about him -- that simply isn't the reason he was taken out of your home. You know that. I did not "steal" him. He is not at my house. O.K.? Now. I want you to tell me precisely what it is you think I can do, so I can answer you in as clear a way as possible. . . so we understand each other.

LUELLEN: (trying to be "reasonable" in turn) I want to see Jimmy.

MARY: I understand that, but what do you want me to do?

LUELLEN: I want you to go get him.

MARY: I can't do that. I don't have that authority. It's out of my hands.

LUELLEN: You go get him and bring him here.

MARY: I can't

LUELLEN: Go get him.

MARY: You were in the courtroom. You heard what the judge said.

LUELLEN: Then call him.

MARY: Who?

LUELLEN: Call that judge. Right now. Tell him I can have my baby back.

MARY: I'm not going to argue with you

LUELLEN: Call him.

MARY: This interview is ended.

LUELLEN: Call him. (She moves in on Mary.)

MARY: I can't call the judge!

LUELLEN: Yes, you can! (Continuing to move in on Mary -- cold and menacing.) And you better.

MARY: (backing away, fear showing) Luellen.

LUELLEN: You better do it. (She is almost in Mary's face.)

MARY: Get out of my face.

LUELLEN: (fists clenched) I mean it!

MARY: Now . . . stop this!

LUELLEN: If you don't, I'll do something. I'll hurt you. I can. I ain't kiddin' either.

MARY: God-damn-it! God-damn-it! (Turns on Luellen who steps back) Just who the hell do you think you are? What do you think you're doing here? You can't ever-not ever in this life-see that child again. Not ever.

LUELLEN: (more of a cry) Yes, I can. .

MARY: Do you think the state or the judge would put that little boy back after what you did?

LUELLEN: I didn't. . . I never done -- Ray. Ray done it.

MARY: You! You! Face that reality at least. You. You admitted it to me, to the judge

LUELLEN: (shaking her head) Ray.

MARY: Ray may have done a lot of it, but not that last, Luellen.

LUELLEN: (childlike) Well . . . he made me.

MARY: He made you hold that child's hands on a hot stove till he had first- and second-degree burns? I'll tell you one thing, Ray couldn't have made me do that!

LUELLEN: (meekly) We was just teaching him

MARY: (going on) And, then, you ran off and left him, just left him -- and in all the months we've had him in foster care, you haven't contacted me once, not one time, to find out how he was doing. So why today? Why do you people suddenly turn up out of the blue and think -- Christ. (Takes a breath to calm herself) We explained everything to you six months ago. (Brief pause.) You could hold a gun to my head or a knife to my throat and it still wouldn't get him back for you. (Pause.)

MARY: (To Audience/Dictation) Jimmy was taken to the State Office for final adoptive placement with his new family on September 3, 1982.
```

---

## IC-0145: Fireworks from Above

- Title: Fireworks from Above
- Author (byline): Faye Lane
- Work: The Moth: 50 True Stories; Pgs 385-391
- Publisher: Hachette Books
- Publication date as stated: Sept 2013
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: FAYE, CEO, WOMAN, MAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1788
- Already set (do not supply): none

### Source block (context only)

```text
Author: Faye Lane
Book: The Moth: 50 True Stories; Pgs 385-391
ISBN: 978-1401311117
Publisher: Hachette Books
Date (Month/Year): Sept 2013
```

### Introduction (context only: never use it for content warnings)

```text
Are you a people person? Let’s check. Take a moment to think about people and things that irritate you – that make you angry . . . (pause) Okay, okay . . . that’s plenty. If you are like me there’s a whole list of things that cause frustration for you every single day. But you know what?

Every day, we have a choice regarding how we view the world. We cannot change our past. We cannot change the way others choose to act. We cannot change the inevitable. The only thing we can do is play the one card we have – our attitude. I am convinced that life is 10% what happens to us and 90% how we react to it.

Let me give you another example: Fireworks from Above by Faye Lane
```

### Performance text (classify this)

```text
FAYE: (Pg 385-391) What I always wanted as a little girl was to tell stories on the stage, because I wanted to be connected to something bigger than myself, and I wanted to be connected to other people. And I believe that a really good performer takes a group of individuals and, through a shared emotional experience, turns it into a collective. For as long as I can remember, I’ve wanted to do this.I’ve wanted to be a performer. . . slash STEWARDESS!

FAYE: I grew up in my mama’s beauty shop in Texas. It was this old A-frame house with big mirrors and swivel chairs in the front room and shampoo bowls in what had been the back bedroom. My mama had this long line of hood dryers on one wall, and I would wait until all the ladies were held captive under the dryers and give mandatory concerts. That was my very first stage.

When I wasn’t telling stories and doing show for the ladies, I would play stewardess, and I would push this little manicure cart around the beauty shop. (with thick Southern drawl as she enacts this memory) "Miss Helen, Miss Melba, would y'all like a magazine? Would y'all like a cocktail?"

And the ladies would say, "Baby, you just give great customer service." I was all about customer service.

And sometimes I'd sit on the porch playing with my Barbie's Friendship airplane, and I would wear this long, silk scarf tied on the side (and it's hot in Texas in the summer). But I loved playing stewardess.

Well, about 10 years ago, I was living in New York City, working as a performer, telling stories and singing songs on the stage. Bad pay, no job security, no benefits. I really needed a job. And I very randomly met this lovely girl with a long, silk scarf tied on the side, who said nine words that changed my life forever: "Have you ever thought about being a flight attendant?"

I had!

Three weeks later, I was in Miami training. Training was so exciting. It was a brand-new airline. They had seven airplanes, a handful of destinations, and a lot of great buzz. They had buzz around the fact that there was live TV at every seat. And they had blue potato chips and designer uniforms. But most of the buzz was around the fact that they had amazing customer service. Perfect! I was all about customer service back at the beauty shop.

And when the founder and CEO of the airline came into our training class and gave this amazing, uplifting speech, I knew I was in the right place.

CEO: Every one of you is here for a reason, and that reason is your ability to smile and be kind. We can teach you how to evacuate an airplane. We can teach you how to handle a medical emergency. We can teach you how to serve. But we cannot teach you to smile and be kind. Your mother did that. Please thank her for me.

FAYE: So beautiful. He said he saw this not as an airline, not as a corporation, but as a humanitarian experiment. He said his goal was to bring humanity back to air travel. I was right on board with this vision. I was so caught up in it. And when I graduated, they made me president of my class, and they even gave me this special certificate called the Spirit Award.

I couldn't wait to get out there on the line -- to surprise people with kindness and, in the process of moving people from Point A to Point B, really, actually move people. And then I graduated and started the job. Maybe you see where this is going. I had this epiphany almost right away: This job is hard, and people are horrible! Really horrible.

First of all, the job was physically exhausting. In the beginning I was on reserve, which meant I was on call and had to be within 2 hours of Kennedy Airport at all times. So I was either running to get to the airport or waiting for the phone call to run to get to the airport, constantly on edge.

And then the actual commute to the airport was extremely hard. I had to take the subway to the bus to the shuttle to the terminal. Even before I got on the plane, I was exhausted. And then when I did get on the plane, there was a whole world of hurt.

My feet hurt. There's this thing that happens where you get bruises on the bottom of your feet from turbulence, and it was horrible. And new flight attendants are sick a lot, because it's kind of like being a kindergarten teacher -- you're exposed to a lot of germs. At one point I had pinkeye in both eyes, a sinus infection, a double ear infection, and strep throat all at the same time. I couldn't see, I couldn't hear, I couldn't talk. And it was mainly because I was taking garbage from everyone all day. And saying "thank you" for it!

"Thank you. Thank you for your garbage. Thank you." They actually made us stop calling it trash. We had to call it "service items," because some of the really bitter girls would say, "Sir . . . you('re) trash," "Ma'am . . . your whole family's trash."

But I understand why they were jaded, because I was kind of getting jaded too. I just couldn't believe how horrible people could be. It's really hard to be mean when someone is smiling at you and handing you a cup of coffee and a cookie, but people are. Because a lot of times they don't see you -- they just see a uniform.

And traveling is hard. It's stressful, and people get ugly. I tried really hard to keep that vision and to smile and be kind, even in the face of meanness. But I hit bottom one day when I had a passenger who had a heart attack on my flight. He was lying in the aisle, and we had opened his shirt and had the pads of the defibrillator on him. I was holding an oxygen bottle. And this woman in the row sitting next to me kept tugging on my blouse:

WOMAN: Excuse me. Excuse me!

FAYE: (to woman) Just a minute, please. We're trying to save this guy's life. (to audience) She kept tugging and tugging . . . (to woman) Just a minute! JUST A MINUTE! (to audience) And then I thought: Wait a minute. Maybe she has an emergency, or maybe she knows something. (to woman) What is it? (to audience) And she held up her coffee cup

WOMAN: This coffee is cold.

FAYE: And I learned that people can be cold. There's something that happens to your psychology because you see the world from above when you fly a lot. And I saw a lot of really horrible things from the air, like devastating California forest fires, New Orleans under water, and most upsetting for me, lower Manhattan smoldering for weeks and weeks.

In late September of 2001, I was working a flight, and a passenger came on with a garbage bag, which is kind of a flight attendant pet peeve, because, "Really, sir, a garbage bag? 14th Street, $9.99. Get a roll-aboard." You know? But you see that. Sometimes people just throw things in a garbage bag and bring it on.

So he goes to row two, which is where he was seated, and he opened the overhead bin and put the garbage bag in. And my next thought was: What's in that garbage bag? Because in late September of '01, we were all still a little edgy and paranoid, so I was kind of keeping my eye on him and the bag. And he put it in the overhead bin and closed the bin and stood there with his hand on it, guarding it.

Which is another flight attendant pet peeve. The overhead bins are shared space, okay? And if you hog up all the space, somebody's bag is gonna get checked. And by the way, if you're in row 12, please don't leave your bag in row 1. It's not nice. You're taking somebody's space.

So my instinct was to go up to this man and say, "Sir, please sit down." But I thought: Just let it go. Just smile and be kind, and if we need the space, I'll deal with it later. [Then] he got up while the seat belt sign was on and stood, waiting for the bathroom. If the seat belt sign is on, it's because the captain knows something we don't know, okay? (to man) Sir, the seat belt sign is on.

MAN: I know, I know, but I really need to go.

FAYE: (to audience) And I thought: Let it go. Just let it go. I was sitting on the jump seat, and it was kinda awkward because he was just standing there, and I felt like I should say something. (to man) Are you traveling for business or pleasure?

MAN: Neither. I live in California, but I came to New York because my son was a first responder at Ground Zero, and he died there. I came to pick up his uniform, which is all I have of him.It's in a bag in the overhead bin.

FAYE: And I remembered why I was there and why I wanted that job. I remembered that everybody has a story, and I don't know what that story is. People fly for a reason. Maybe they're going to a funeral or to see someone who's sick, or maybe it's something joyful, like a wedding. I don't know what their story is, but for that little piece of time, I'm a part of it, and I have an impact on their experience.

What I love about performing is taking a group of individuals and, through a shared emotional experience, turning it into a collective. But my job as a flight attendant is to take a collective and to turn it back into a group of individuals.

Flight attendants talk about "crowds" sometimes, like, "Avoid the Fort Lauderdale crowd. They're horrible," or "Avoid the Long Beach crowd." But every crowd is a group of individuals, and every individual has a story. And yeah, I’ve seen a lot of horrible things from the air. But I've also seen a lot of amazing, beautiful things, like the Grand Canyon, the Northern Lights, fireworks from above.

And now when I go through the cabin with my garbage bag, saying "thank you" and smiling, I mean it, because I'm making a gratitude list in my head. And every time I say, "thank you," I think of something I'm grateful for: "Thank you" (for my job). "Thank you" (for these comfy shoes). "Thank you" (for my life). Because my job enables me to be part of something bigger than me, and to be connected to other people, like this. So thank you.
```

---

## IC-0146: The Fish Story

- Title: The Fish Story
- Author (byline): Naomi Wallace
- Work: Monologues for Women
- Publisher: Heinemann
- Publication date as stated: Dec 1994
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: GIRL
- Teaser before the introduction: Yes
- Spoken words (computed): 1474
- Already set (do not supply): none

### Source block (context only)

```text
Author: Naomi Wallace
Book: Monologues for Women
ISBN: 978-0435086305
Publisher: Heinemann
Date (Month/Year): Dec 1994
```

### Introduction (context only: never use it for content warnings)

```text
This is “The Fish Story” by Naomi Wallace
```

### Performance text (classify this)

```text
(A young girl is telling a story. She has a lure box with her)

GIRL: [I remember the day] I landed a four-pound small-mouthed bass. Almost snapped my line. It took me fifteen minutes to bring that monster close enough to the bank so my father could scoop it up in the net. Daddy and I skinned it right there and cooked it over the fire. I can tell you I was proud that day. And Daddy was proud of me too. Have you ever made your father proud of you? I mean, [really, really] proud?

GIRL: It was almost like they knew they were going to be crucified. First they would like still on your palm, as though dead. Only a slight tremor, at one end or the other, gave their trick away. It was this moment. This moment of clam right before it happened, that I liked most, when their tender, fleshy bodies studded with black dirt, would lay in my hand like the trust of an old friend. At seven years old, that glistening body of plumped worminess was more beautiful to me than any . . . . (Breaks off).

But when the hook came up close, the thing would start to writhe like all hell-fire was upon it. (Beat) It isn’t true that worms wriggle when they’re threaded on the hook. Those who say they do never hooked a worm in their life. No, worms don’t wriggle, they writhe.

It didn’t bother my father. He’d just pluck the worm from the jar and thread it on the hook without blinking an eye. When he wasn’t looking, I’d whisper “hush, hush” to the worm and when it turned its stomach to me, that pink ban that circles its body like a wedding ring, I’d strike fast, straight through the center

(She opens the box and carefully lays out some lures).

No one made me do it but myself and for while I felt sorry for the worms, I loved hauling in the bass. And me and my father would stand side by side, casting the deep stream pools. We’d bet on who would holler first “I got one!”

Daddy was my friend. He liked fishing the way I liked it. When he cast a good one, his lips would go white and his chin would tremble just a little as he waited for a strike. Sometimes one of his ears would go red with all that waiting. Not both of them, just the left one. Red as a worm.

(Singing) Oh my love is like a red, red worm. Once I hooked that red ear. I was fly fishing and I hauled back to snap the line and toss it on a new patch of water and (Beat. She screams as though she were her father.) That’s how he sounded.

(She polishes some lures)

I didn’t know at first what had happened so I kept jerking at the rod until my Daddy caught hold of my line with his free hand and jerked back; the rod flew out of my hands and snapped in two on the ground between us. And there hung my fly with three hooks, one hook embedded in that red ear which was redder than I’d ever seen it. He made me get it out. He didn’t say a word, just opened his lure box, took out a pair of pliers and handed them to me. (Beat) When a bluegill swallows an artificial fly or a spinner, it usually hooks down into its lungs.

You see, bluegills have small mouths and what does in doesn’t come out. If it isn’t your favorite lure, you can cut the line and throw the fish back in. They say the creek water will rust a hook out of a fish’s mouth in forth-eight hours. If it’s your favorite lure, and one time it was my favorite, you just have to pull. That’s when a piece of the lung will come out with the hook. (Beat) But an ear isn’t a fish. And yet my father’s ear was tougher than a catfish lip. I had to twist and pull. Twist and pull. The ear fought me. It wouldn’t let go. It held on tight. My father just sat there and I knew if I didn’t get it out, if he had to do it himself, then . . . well, twist and pull. Twist and pull. Finally it tore. The ear. And out the hook came.

He let me choose. My father was good about that. He said I could have a spanking, without my shorts on, or eat a worm as my punishment for not looking behind me when I’d swung the rod. So I dug down into the jar and pulled one out, praying I’d grab a dead one. But that worm must have been sleeping ‘cause the moment it got near my mouth it sparked like a firecracker trying to get loose. (Beat) Well, I looked at the worm and if a worm can look, it did so at me. I’d never had one before, thought once my Daddy let me choose between biting the tail off a grasshopper or not watching television for two whole weeks when I spilled a can of paint in the garage. I went for the grasshopper. Like a saltine cracker, almost exactly, when I ate it (She hangs the lures on her outstretched arm as she speaks until they hand like decorations in a row.)

They say a worm has seven hearts and that if you cut it in the right places, two or three of the pieces will live. The problem was, I didn’t know where the hearts were or where to bite. I held it up to the light but I couldn’t see anything but red worm. I put it halfway into my mouth. I figured biting it halfway was a choice. Random would kill it for sure. I closed my eyes but I couldn’t bite down. The half of the worm that was inside started tickling the roof of my mouth like how the dentist does. I started to laugh but then Daddy started shouting for me to do it. He was saying “Now, now, now” (Beat)

Then Daddy slapped me on the back of the head and I bit down.

I only use artificials now. I like the sound of their names: Switchback, Rapala, Zarco spinner, Bass magnet, Zephyr Puppy, Double-headed jig, and Jitterbug. Twelve-pound line. Eight-pound line. Six-pound line. I was using four-pound line later that day. I cast my line right between a fallen tree and rock ledge. It fell on the water with hardly a splash. I twitched the line once. Twice. Just before the third twitch and reel, the bass struck it.

There must have been some magic to the flesh of that worm I ate because that afternoon I landed a four-pound small-mouthed bass. Almost snapped my line. It took me fifteen minutes to bring that monster close enough to the bank so my father could scoop it up in the net. Daddy and I skinned it right there and cooked it over the fire. I can tell you I was proud that day. And Daddy was proud of me too. He kissed me on the mouth four times, one kiss for each pound of that bass. Have you ever made your father that proud of you? I mean, that proud? Four times. He kissed me four times. On the mouth. Have you ever? Four times? On the mouth? (Beat) I can show you. It’s hard to tell you just how it went unless I show you. That’s how proud he was. That’s how. Yes. And I closed my eyes because I had to. Because if a worm has seven hearts it could have eight and I wanted him to know I could take it. And I took it. On the mouth. But once it’s cut. The worm. You never can tell just which parts have been killed and which parts will crawl away and start over because all of the parts are moving. All of the parts are trying to live. But only one or two of them do. Live.

I’ll tell you a secret: I’m not a very good daughter. It was worse. His pride in me. Worse. Than eating that worm. Silly, isn’t it? Know what I mean? Do you? Four times. On the mouth. That’s how it started. Then we went home to tell Mother about my bass.

You wouldn’t know it, would you? To look at me. Some of this, here (Motions to parts of her body, slowly) isn’t really alive anymore. Deceptive, isn’t it? How can one look at the body and see nothing but the whole of it. But I know. I know which parts went on and lived and which parts gave up and died. I can tell them apart just by touching them. (She gently touches herself in different places, not necessarily sexual parts of her body) Can you tell them apart? If you touch yourself, here and here, or there and there? Go on. Try it. That’s it. Can you tell just which parts of you are dead and which parts of you are still alive? (Beat) Got it? All right then. When ready. (Beat) Let’s go fishing.
```

---

## IC-0147: Flying

- Title: Flying
- Author (byline): Carol K. Mack
- Work: Even More Monologues for Women by Women
- Publisher: Heinemann
- Publication date as stated: March 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1520
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carol K. Mack
Book: Even More Monologues for Women by Women
ISBN: 0325002479
Publisher: Heinemann
Date(Month/Year): March 2001
```

### Introduction (context only: never use it for content warnings)

```text
Flying by Carol K. Mack

During the following relived memory, Kay, 19, very bright, vulnerable, quirky, transforms from human to bird. She may be speaking to us in her Post-Avian state from a place on the lawn of her school or home or hospital. Wherever she is, she is alone and she wants us to understand her story. The birdlike mannerisms that express themselves throughout the story and that finally overwhelm her are to be invented by the actress.
```

### Performance text (classify this)

```text
OK, here's the hard part. . . OK, a couple of months ago? When I was human, that's when it all started. Right in front of the student center on February 10th at three o'clock. The bells on the campus chapel were going off, which is how I know the time. Anyhow, I was just standing there when I saw this feather. It was lying on the snow? (She reaches down, picks it up, examines it.) It was white as the snow so it was nearly invisible. And it had these. . . markings. This weird blue design on the underside, almost like a code, and it . . . well, it smelled so familiar, and that's when it hit me. This was all a message. And for the first time in my life, everything fell into place. I realized. . . I knew that my real father was a bird. (Shifts uncomfortably, lifting her elbows, shoulders.)

So then what? I mean I knew I'd have to confront my mom with this. But she'd never admit it. She hates talking about what she calls "closed chapters" of her life? That includes a lotta stuff; I mean was it a one-night stand? And how could she forget? My mom is so . . . How could I ask her about transpecies lovers? And there are other questions. DNA-related ones. Like, could I fly? I mean at that point I still didn't know. (Moves around, slightly more avian, annoyed at the memory.)

The day before the feather, I had, coincidentally, picked my freshman term-paper topic from this list of choices and of course I picked Quetzalcoatl. I always had this, connection, to Quetzalcoatl, y'know, that gorgeous Aztec plumed serpent god. But this witch, Ashley Williams? She claimed her great-great-grandmother was one-eighth Guatemalan, and she picked Quetzalcoatl too. So the professor told me that since the Aztecs were really more Ashley's than mine, why didn't I think about Druids or something!? I said to Tim, "It's not fair." "Life's not fair, mate," Tim said. He used to call my roommate "mate," too, when they were dating. So I never know-is it 'cause he gets us mixed up or 'cause he's from Australia? Everybody's from somewhere but me . . . (She crosses her arms, flaps her elbows.) Bummer.

Before the feather it was such a totally awful year. My roommate freaked out and dropped out and then I moved in with her ex, Tim. He has this gorgeously unpronounceable name and is so . . . intense, and he's also very cute. All I wanted was a name like his, with two clinking consonants at the top that linked me to some exotic ancient land. Something mysterious to sign my papers with. A name with maybe only clicks. A name that if you said it the wrong way would mean something like fart. But being from Long Island, well, like Tim says, that's Kansas. It's all Kansas, mate. (Growing indignant and “ruffled”)

So, anyhow, it was this very next day that my dad sent me his message by feather, and it wasn't long before "Kay Smith," in what looks like an ordinary human body, is utterly transformed. I began to hover, mentally at first. And in the library, I began hunting for my roots, my own folk culture, back to the first soaring Archaeopteryx! (Fascinated, enthusiastic) My dad's ancestral superiority is pretty evident! He had visual acuity way beyond human. And what about those impossible migratory navigational feats with no maps at all! Probably the most important find is this organ called the amygdala. It's this perfect snug core coiled way deep inside every single human brain. What does it do? It gives you this adrenal rush the minute an identifiable Other comes into view. (Triumphantly) And it's mine. It's MINE. I've got the original! It's premammal! It's this amygdala that's like the most important thing on campus! This amazing organ is more part of my heritage than my classmates' and never given credit! Ignored! But this very amygdala practically rules the roost and not just for sex, but even for (looking around) who you sit with in the cafeteria! Me? (Perches, rolling her shoulders) I sit by myself! And I begin to think a lot about flying.

(Romantically) Now that I'm no longer "Kay," who am I? I mean my real name must be so ancient a sound it couldn't even be represented by glyph! It's indecipherable, just a wingbrush, maybe a feathery noise like a breeze or a whisper. I wore my beautiful white feather at all times under my T-shirt, folded in my bra, near my heart. Hidden. (Annoyed) Of course I avoided wearing it in any fashion that I realized was just plain plumage display. Somebody might think it was some kind of Native American rip-off. It's not! And it's not Kabbalah, either! It's a Bird Thing!

OK? Anyhow, as an Avian creature I am Beyond Culture. And also am totally beyond guilt for ever being anywhere where anybody was oppressed anytime in history' cause my dad's folks' folks were originally connected to the Great Auk. And the Great Auk lived on all these uninhabited isles and developed a near mythic reputation. But, well, that's only a guess. Dad may have been a swan.

To attempt to be true to my heritage I started to eat only trail mix. Tim said, "Losing weight, mate?" And I thought, what a jerk! What a jerk. Bird weight gain and loss is all timing. It's all about Nesting and Migration-why bother, he'd never understand. I just blinked at him. Then I realized I hadn't blinked in a week! You know what that means. Also I noticed this feeling of tension in my shoulder blades. I didn't know if it was stress and my knapsack or some latent sprouting at the base of my blades.

And I was just blown away by thinking about my amazing dad-I mean when I think about his air sacs, his fused hips, his great scaly feet: a faster heartbeat, air in his bones, and at least three times as many vertebrae in his neck! All these Avian traits filled me with such pride I could hardly keep from crowing. And to think that humans denigrate these glorious creatures with names like "secretary bird" and "grebes"!? And how about "crazy as a loon"? Or that really odious comparison of vultures to lawyers! (angry determination) I'll redress this. Yes. Why, we're everybody's icon: the eagle, the falcon, the dove! There's no ceiling on bird power. And where does Nietzsche come off using the eagle as if he had some inside track? You wish, Nietzsche! And Edgar Allen Poe. Nevermore!

My paper's due, and I decide to present my own topic. Iit's gonna be all about bird sound and finally show how to talk to a bird. I know now. I can caw and warble. In bed I make new burry noises in my throat that scare Tim!

It was during finals, I "fixed on" the crowd sitting in their little tribal formations in the cafeteria. I decided right then to eliminate my memories and thus gain the necessary lightness for a demonstration. (Getting up on a bench, excitedly) I concentrated on my hidden feather, visualizing it a thousand fold, and when all I could see were white feathers with faint blue markings, I imagined myself covered with them, and I climbed onto my corner table and I rose up into the air! (arms spread in awe)

It was in this final soaring flight to the cafeteria ceiling, a burst of energy and weightlessness, that I first became aware of this sound under me. (Still, awe) The sounds rise unlike anything else in the universe! Each voice utterly unique, each vibration like no other in all time. And yes, YES, greater than any birdsong! It is this chorus of human voices that forms the up-current on which I glide. By human hum I hover, and I look down at all those eyes looking back at me! Those eyes. They're all filled with expression and each pair unlike any other pair, without the Avian brilliance or opaqueness-why they're filled with wonder at my flight! (Blinks away the humanity.) OH! I try a new bird squint, first raising my powerful lower eyelid halfway up, then sliding the nictitating membrane, my third eyelid, horizontally across. I discover the use of this membrane which has eluded human ornithologists: what it does is filter the field of vision. OH! Now I can see all those amazing eyes with birdsight! They're like a shimmering lake, a continuum of light facets! OH! How incredible! (In a very different tone) That was my last conscious thought before I fell down near the hot trays. . . . (Moves to another place)

When I wake up, Tim's kneeling next to the doctor, looking worried. I try to speak, my beak. . . can't get my beak around the words. Nobody can hear me. Tim shrugs and he's swinging his ponytail, saying, "I dunno, mate. Magical realism?"

And then I look around and they're all looking so, helpless, so . . . sad and worried, all myoid classmates, so amazingly different, each of them. My Avian Pride dies right then. A tear drops onto my T-shirt. Human! Birds can't cry. But then I see the tear roll down my arm, and I see the downy underfeathers sprouting now as my arm turns wing. Too late. Too late. I'm speechless, and I feel only love. Love. Oh, I wish I could communicate with the species!
```

---

## IC-0148: For Colored Girls Who Have Considered Suicide

- Title: For Colored Girls Who Have Considered Suicide
- Author (byline): Ntozake Shange (En-toe-ZAK-kay SHONG-gay)
- Work: Not specified
- Publisher: Bantam Books, Inc.
- Publication date as stated: 1980
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTER
- Teaser before the introduction: No
- Spoken words (computed): 1471
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ntozake Shange
ISBN: 978-0553133073
Publisher: Bantam Books, Inc.
Date (Month/Year): 1980
```

### Introduction (context only: never use it for content warnings)

```text
Let me take you back to the late 60’s/early 70s and just how difficult it was to be a black female at the time. Facing hardships and continuing to survive despite horrific experiences, being black as well as female placed these women in a double minority. In For Colored Girls Who Have Considered Suicide, Ntozake Shange shares the good and bad personal experiences of women of color. First to share her perspective is the Lady in Blue . . .
```

### Performance text (classify this)

```text
Character: Lady in Blue

i'm outside manhattan

i used ta live in the world

then i moved to HARLEM

& my universe is now six blocks

when i walked in the pacific
i imagined waters ancient from accra/ tunis
cleansing me/ feeding me
now my ankles are coated in grey filth
from the puddle near the hydrant

my oceans were life
what waters i have here sit stagnant
circling ol men's bodies
& broken lil whiskey bottles
left to make me bleed

iusedta live in the world
now i live in harlem & my universe is six blocks
a tunnel with a small train
ican ride anywhere
remaining a stranger
icd stay alone
a woman in the world
then i moved to
HARLEM
icome in at dusk
stay close to the curb

wdnt be good
not good at all
to meet a tall short black brown young man fulla his power
in the dark
in my universe of six blocks

iusedta live in the world
really be in the world
free & sweet talkin
good mornin & thank-you & nice day
uh-huh
ican't now
ican't be nice to nobody
nice is such a rip-off
reglar beauty & a smile in the street
is just a set-up

ihadda right to the world
then i moved to harlem for the set-up
a universe
six blocks of cruelty
piled up on itself
a tunnel
closin

we deal wit emotion too much
so why dont we go on ahead & be white then/
&make everythin dry & abstract wit no rhythm & no
reelin for sheer sensual pleasure/yes let's go on
&be white/ we're right in the middle of it/ no use
holdin out/ holdin onto ourselves/ lets think our
way outta feelin/ let's abstract ourselves some families
&thinkin wont do me a bit of
good tonite/ i need to be loved/ & havent the audacity
to say
where you are/ & dont know who to say it to

one thing i dont need
is anymore apologies
igot sorry greetin me at my front door
you can keep yrs
idont know what to do wit em
they dont open doors
or bring the sun back
they dont make me happy
or get a mornin paper
didnt nobody stop usin my tears to wash cars
cuz a sorry

iam simply tired of collectin

i didnt know

i was so important to you'
i'm gonna haveta throw some away
icant get to the clothes in my closet
for alla sorries
i'm gonna tack a sign to my door
leave a message by the phone

'if you called

to say yr sorry

call somebody

else

i dont use em anymore'
ilet sorry/ didnt meanta/ & how cd i know abt that
take a walk down a dark & musty street in brooklyn
i'm gonna do exactly what i want to
&i wont be sorry for none of it
letta sorry soothe yr soul/
i'm gonna soothe mine

you were always inconsistent
doin somethin & then bein sorry
beatin my heart to death
talkin bout you sorry
well
iwill not call
i'm not going to be nice
iwill raise my voice
&scream & holler
&break things & race the engine
&tell all yr secrets about yrself to your face
&i will list in detail everyone of my wonderful lovers
&their ways
&i wont be sorry for none of it

iloved you on purpose
iwas open on purpose
istill crave vulnerability & close talk
& i'm not even sorry bout you bein sorry
you can carry all the guilt & grime ya wanna
just dont give it to me
icant use another sorry
next time
you should admit
you're mean/ lowdown /trifin/ & no count straight out
steada being sorry alla the time
enjoy being yrself

ifound god in myself &i loved her/ i loved her fiercely

& this is for colored girls who have considered

suicide/ but are movin to the ends of their own rainbows

TRANSITION

While the Lady in Blue struggles to adjust to a life in Harlem, surrounded by values and a society very different from what she has known . . . While she struggles to come to terms with what she is willing to accept and what she wants for herself , The Lady in Yellow relates a quite different reality: The celebration of her graduation from high school . . .

CHARACTER: Lady in Yellow

it was graduation nite & i waz the only virgin in the crowd
bobby mills martin jerome & sammy yates eddie jones & randi
all cousins
all the prettiest niggers in this factory town
carried me out wit em
in a deep black buick
smellin of thunderbird & ladies in heat
we rambled from camden to mount holly
laughin at the afternoon’s speeches
& danglin our tassles from the rear view mirror
climbin different sorta project stairs
movin toward snappin beer cans &
GET IT GET IT THAT’S THE WAY TO DO IT MAMA
all mercer county graduated the same nite
cosmetology secretarial pre-college autoshop & business
all us movin from mama to what ever waz out there
that nite we raced a big ol truck from the barbeque stand
trying to tell him bout the party at jacqui’s
where folks graduated last year waz waitin to hit it wid us
i got drunk & cdnt figure out
whose hand waz on my thigh/but it didn’t matter
cuz these cousins martin eddie sammy jerome & bobby
waz my sweethearts alternately since the seventh grade
& everybody knew i always started cryin if somebody actually
tried to take advantage of me
at jacqui’s
ulinda mason was stickin her mouth all out
while we tumbled out the buick
eddie jones waz her lickin stick
but i knew how to dance
it got soo hot
vincent ramos puked all in the punch
& harly jumped all in tico’s face
cuz he was leavin for the navy in the mornin
hadda kick *** so we’d all remember how bad he waz
seems like sheila & marguerite waz fraid
to get their hair turnin back
so they laid up against the wall
lookin almost sexy
didnt wanna sweat
but me & my fellas
we waz dancin
since 1963 i’d won all kinda contests
wid the cousins at the POLICE ATHLETIC LEAGUE DANCES
all mercer county knew
any kin to martin yates cd turn somersaults
fore smokey robinson cd get a woman excited
we danced
doin nasty ol tricks i’d been thinkin since may
cuz graduation nite had to be hot
& i waz the only virgin
so i hadda make like my hips waz inta some business
that way everybody thot whoever was gettin it
was a older man cdnt run the streets wit youngsters
martin slipped his leg round my thigh
the dells bumped "stay"
up & down-up & down the new carver homes
WE WAZ GROWN
WE WAZ FINALLY GROWN
ulinda alla sudden went crazy
went over to eddie cursin & carryin on
tearin his skin wid her nails
the cousins tried to talk sense to her
tried to hold her arms
lissin **** sammy went on
bobby whispered i shd go wit him
fore they go ta cuttin
fore the police arrived
we teetered silently thru the parkin lot
no un uhuh
we didn’t know nothin bout no party
bobby started lookin at me
yeah
he started looking at me real strange
like i waz a woman or somethin/
started talkin real soft
in the backseat of that ol buick
WOW
TRANSITION

And although every black women has her own unique experience, they also are united by their color and gender in a world that too often marginalized their existence. The Lady in Brown makes a final plea for black women in America. Listen carefully, for humanity unites us all.

CHARACTER: Lady in Brown

dark phrases of womanhood
of never havin been a girl
half-notes scattered
without rhythm/no tune
distraught laughter fallin
over a black girl’s shoulder
it’s funny/it’s hysterical
the melody-less-ness of her dance
don’t tell nobody don’t tell a soul
she’s dancin on beer cans & shingles
this must be the spook house
another song with no singers
lyrics/no voices
& interrupted solos
unseen performances
are we ghouls?
children of horror?
the joke?
don’t tell nobody don’t tell a soul
are we animals? have we gone crazy?
i can’t hear anythin
but maddening screams
& the soft strains of death
& you promised me
you promised me...
somebody/anybody
sing a black girl’s song
bring her out
to know herself
to know you
but sing her rhythms
carin/struggle/hard times
sing her song of life
she’s been dead so long
closed in silence so long
she doesn’t know the sound
of her own voice
her infinite beauty
she’s half-notes scattered
without rhythm/no tune
sing her sighs
sing the song of her possibilities
sing a righteous gospel
let her be born
let her be born
& handled warmly.
& this is for colored girls who have considered suicide
but moved to the ends of their own rainbows.
```

---

## IC-0149: Franziska: A Silent Protest against Sterilization

- Title: Franziska: A Silent Protest against Sterilization
- Author (byline): Ina R. Friedman
- Work: The Other Victims
- Publisher: Sandpiper
- Publication date as stated: Sept 1995
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: POST SCRIPT
- Teaser before the introduction: Yes
- Spoken words (computed): 1320
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ina R. Friedman
Book: The Other Victims
ISBN: 978-0395745151
Publisher: Sandpiper
Date (Month/Year): Sept 1995
```

### Introduction (context only: never use it for content warnings)

```text
Franziska (Franny) Schwarz was blond, a German Aryan and . . . deaf. When she was sixteen, the Nazis knocked at her door. To Hitler, Jews and gypsies weren’t the only “undesirables” Franziska:. A Silent Protest against Sterilization by Ina R. Friedman. It is time her voice is heard.
```

### Performance text (classify this)

```text
Everything was done legally. First a law was passed to remove the “undesirable” elements from public service. Jews lost their jobs as teachers, civil servants, and doctors in hospitals. This decree was followed in 1933 by the “Law for the Prevention of Offspring with Hereditary Defects.” It required that persons who were blind, deaf, physically or mentally handicapped, or were alcoholic be sterilized.

Teachers in schools for the deaf, who were themselves, hearing, turned over the names of their deaf pupils to the Nazi authorities. From 1934 to 1939, between 350,000 and 400,000 people lost their ability to have children in this unjust and unscientific program.

[Today] Hitler is dead and the Nazi regime is ancient history. But the laws for sterilization are still on the books of West Germany. Today there are people who say the Holocaust never happened, that it is only an “invention.” But each law, each action affected an individual.

NOTE: Should be spoken (at least in part) with the affectation of a deaf person (ie Actress Marlee Matlin ) Being able to use sign language would also be a plus for this selection!

I never saw anything wrong with being deaf. My younger sister, Theresa, and most of my friends were deaf. In deaf school, the teachers go mad if I signed. They wanted me to read lips and to use my voice. I got so tired of watching the teacher’s lips. I couldn’t look away for a minute. It was even harder when she tried to teach me to say the letters correctly. The teacher put a strip of paper in front of my lips. (with a German accent) “To make the B sound, purse your lips and blow just enough to make the paper quiver. To make a P, blow a little harder and make the paper shake.” Day after day the teacher drilled me.

When I was fourteen, Hitler took over Germany. But I couldn’t hear the radio, so I never got excited about Hitler. Not until the trouble started in 1935. I came home and found Mother crying. “What’s the matter?” I signed.

She handed me the letter that read, “Frau Schwarz and her daughter Franziska are to come to the health office to arrange for their sterilization. Heil Hitler.”

“I won’t go,” I cried. “I want to be able to have babies.” The previous year, I had met a boy I like, Christian Mikus. As a child, he had had scarlet fever and lost his hearing in one ear. Whenever he saw children playing, he’d smile and sign, “One day, we will have children, too.”

“Father looked sad. “If you don’t go, the police will drag you to the hospital.”

I screamed all the way . . The nurse locked me in a room with two other deaf teenagers. The three of us cried all night. When the nurse came to give us tranquilizers, I tried to fight her off. She held me down and gave me the injection. In the morning, I woke up in a room full of beds. My stomach hurt. I touched the bandages and started to cry. The nurse who brought me water was crying too. “I’m sorry, there’s nothing I could do to help you. With Hitler, you have to be quiet.” Her finger pointed to the portrait of Hitler handing over the bed. She tapped her temple with her finger, to indicate, “He’s crazy.”

I had so much pain, I couldn’t go to work. I asked the public health insurance office for the standard sick pay.

“Why should you get sick pay?” the social worker sneered. “You can have all the fun you want. You don’t have to worry about getting pregnant.”

When Christian came to the house, I started to cry. “The doctors sterilized me. I guess you won’t want to be my boyfriend anymore.” Christian made the sign for love. “Whatever happens, we’ll be together. As soon as you’re twenty-one, we’ll get married.”

In 1938, in spite of being sterilized, I missed my period. My mother was out of town helping a sick relative. When she returned, a few months later, she saw my swollen stomach. “How could you do this?”

“Please, please, don’t be angry. We want a baby so much. I was afraid I’d never have one. Now Christian and I can get married.”

“All right, but I want to be sure you have proper care. I want you to go to a gynecologist.”

The gynecologist who examined me was very jolly. “Congratulations. The Fuehrer wants every young girl to have a baby.” Then I saw my mother say, “I’m surprised Franziska got pregnant. She’s been sterilized.”

Within a few days, I had a letter from the health office. “Fraulein Schwarz Is to come to the Women’s Hospital for an examination.”

I took off my clothes and went into the examining room. The doctor felt my stomach. “Yes, you’re pregnant. The pregnancy appears normal. Go into the other room.”

The doctor pushed me inside the changing room and locked the door. I looked out the window. I was on the fifth floor, too far to jump. I hid behind the door. When the nurse brought lunch, I escaped and ran toward the stairs. All the nurses ran after me. They caught me and locked me in the room.

For three days, I lay there, biting my nails and screaming. Then [on the 4th day] the nurse dragged me by the hair into the hall and put me in a room with barred windows. I banged on the wall so they would let me out. The nurse shoved me into bed and gave me an injection. I woke up just as the stretcher was being wheeled into the operating room. There was a big tray next to the operating table. My baby is going to be on that tray, I thought, instead of inside me. “No, No,” I tried to shout. . . . Christian!

Christian didn’t know where I was. Every day, he went to my house, but my mother wouldn’t open the door. Finally my mother told him “Franziska is in the Women’s Hospital. They took the baby.”

When I woke up from a nap, I saw Christian standing next to the bed. My face was so white he dropped the flowers he had brought me. “Franziska, I’m sorry they took the baby. But we’ll still get married. We can’t stop Hitler, but he can’t stop us from loving each other.”

The nurse handed me a notice when I left the hospital. “You are to return to this hospital within 10 weeks to be sterilized.” I started to cry. “It’s hopeless. I won’t go. It’s too painful. I’ll hide in a convent until the war is over. Then we can get married and have children.”

“No,” Christian said. “The Nazis will find you. They’ll take you and do it whether you want it or not. Hitler is winning the war.”

My Uncle Karl wrote to the judges for a hearing. My mother, my father, and all his brothers went to the court. The judges refused to change the order. My uncle’s face got very red. “God damn Hitler! How can he do this to a young girl?”

The judge stood up. His face got so red and twisted he looked like the gargoyle in the corner of the church. “Arrest this man. He has slandered the Fuehrer.”

His brothers tried to get him released. They promised he would join the army and fight for the Fuehrer. The Nazis wouldn’t listen. They beheaded Uncle Karl and sent the family the bill for the executioner. It was a horrible time for me and my family.

POST SCRIPT: Franziska Schwarz Mikus survived the war and she and Christopher were married. They moved to Munich and Franziska has been active in promotion arts and crafts among the deaf, serving as secretary to three different organizations. Christian died a few years ago. His death was mourned by the entire deaf community of Germany and Europe. He had become well known for his coaching abilities and his soccer team had participated in the international deaf games.
```

---

## IC-0150: Free Barbie

- Title: Free Barbie
- Author (byline): Eve Ensler
- Work: I am an Emotional Creature
- Publisher: Villard
- Publication date as stated: Jan 2011
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1114
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eve Ensler
Book: I am an Emotional Creature
ISBN: 978-0812970166
Publisher: Villard
Date(Month/Year): Jan 2011
```

### Introduction (context only: never use it for content warnings)

```text
Since the 1950’s girls under the age of thirteen have viewed Barbie as the embodiment of an American beauty, but her roots prove that she is anything but a true American. In fact, no Barbies have ever been made in the USA. She actually descends from rundown sweatshops, tucked in the slums of third world countries. Children have no idea that their new doll was actually made by a young Chinese girl, no older than they are. The little girl who made this doll withstands fifteen hour work days, less than livable pay, and excruciating physical pain just to produce your child’s toy. The naïveté of our society’s children is to be expected, as a child I too was captivated by the utter perfection of Barbie, but a parent should not be so easily deceived. After one examines the truth behind the vibrant label, it is evident that the path that a Barbie doll has to travel to reach your hands is anything but glamorous. Free Barbie by Eve Ensler
```

### Performance text (classify this)

```text
Hello, my name is Chang Ying. I wish I could write you a proper letter, but I‘m in a factory and I work 12 hours a day and if I’m late or I complain they will throw me out. Even thinking these thoughts could get me in trouble cause I could mess up and get my hand caught in the machine. They hate it when we hurt the machines. They hate it when anything happens to us cause it slows everything down. That’s how LiJuan died. There was a fire one day and she was scared to leave her station ‘cause she needed the job to feed her family and she was burned too badly.

But I can’t lie, I couldn’t really write you a letter cause I can’t read. I’m 13 and I have been working since I was a kid. I speak good Chinese, I just can’t write it or read it. But I have a lot to say and I think I can help you.

You may not think some poor girl who only makes a few cents an hour has anything to teach you. But I know a lot about Barbie. I am one of the people who makes her head. I actually see what goes into it.

As you can tell by now I have found a way to get this message to you. It isn’t a letter or internet or phone. It’s what I call Head Send. Can you feel it? It is very strong. I started doing it when I was 5. You have to think a thought very, very intensely and then you have to imagine someone receiving the thought and then you close your eyes and concentrate and your head sends it.

Because I make Barbie’s head I head send my thoughts into each one of her brains. So whatever girl gets her will hear my thoughts. I have made many, many heads so my message is in a lot of places.

If you listen very closely to your Barbie—put her head to your ear like a shell—you will hear what I have to say.

Many, many of us girls are needed to make Barbie because three Barbies are sold every second. They told us this the first day of the job. They said girls like me were working in a lot of countries to make Barbie perfect. Her body omes from Taiwan. Her hair gets stuck on in Japan. Then she comes to China to get clothes and get her head put on. They said that 23,000 trucks a day go back and forth to the harbor crammed with Barbies so they can all sail to America and get packaged in pink and sent out.

They told us what we did here in China was the most important part and that we had to do it fast or we would not keep up and then little girls couldn’t get their Barbies.

At the beginning I used to worry about this and I would always be very nervous. I cut my hand a few times in the machine.

Then I saw a picture of Barbie’s dream house and it made me start thinking about where I live. I live in a nightmare house. It’s not even a house, a dormitory. It’s like prison Barbie, all us girls shoved into one ugly place. I started thinking about how one Barbie costs 200 yuan, but I work here where it is so hot, all day, six days a week and I don’t make that much in a whole week.

I have never been anywhere else but I do not think anyone really looks like Barbie. She is so skinny, I heard she can’t even get her period. And my cousin who lives in America told me that Barbie makes the girls who own her stop eating because they try and look like her. I started thinking about how it’s actually hard to love Barbie they way she is now. She is very tough, so much plastic. She’s not cuddly at all. She can’t even put her arms around you. You have to do things for her: worship her, dress her, buy her things. She wants everything. She is very greedy and needy. That’s how they get you to spend more money.

Listen, it’s not Barbie’s fault, she doesn’t even have a chance. So many people control her—from the first plastic mold to her final accessory. In many ways she has less freedom than even me. She has no ability to walk away. Her legs probably wouldn’t hold her up anyway. So many people abuse her. You know, there is a whole group of Barbies—here at the factory we secretly call them the unfortunate ones—they get sent to Barbie headquarters in Los Angeles and a room of Barbie experts throw them and kick them and bite them to see if they can take it.

My cousin also told me that many girls love their Barbie at the beginning then when they get older they turn on her. They cut off all her hair or even her head or put her in the microwave oven.

The people who are in charge make her say really stupid things. They put words in her mouth:

Will we ever have enough clothes?

I want to go shopping?

Math is hard.

I know Barbie doesn’t really want to say any of this cause I know what’s going on in her head. She talks to me. She’s really angry. She’s really hurting. She is really guilty. She hates shopping and feels badly about all the girls who are starved to make her and are starving to be like her. She’s actually very messy and surprisingly loud. She is not at all polite and she hates being shoved into really tight clothes and pointy high uncomfortable shoes.

Barbie isn’t who you think she is. She’s so much smarter than they will let her be. She’s got great powers and is kind of a genius.

There are more than 1 billion Barbies in the world. Imagine if we freed them. Imagine if they came alive in all the villages and cities and bedrooms and landfills and dream houses. Imagine if they went from makeover to takeover. Imagine if they started saying what they really felt. Let Barbie speak. Head Send:

Free Barbie! Head Send:

Free Barbie!

Free Barbie!

Free Barbie!

Ow! I just got my hand caught! It hurts. It’s bleeding. They are going to be very angry. Head Send:

Free Chang Ying! Head Send:

Free Chang Ying!

Let her out of this dirty sweaty factory. Head Send

Please.
```

---

## IC-0151: French Fries from Talking With

- Title: French Fries from Talking With
- Author (byline): Jane Martin
- Work: Talking With
- Publisher: Samuel French, Inc.
- Publication date as stated: April 1983
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ANNA MAE
- Teaser before the introduction: No
- Spoken words (computed): 972
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jane Martin
Book: Talking With
ISBN: 0573630216
Publisher: Samuel French, Inc.
Date(Month/Year): April 1983
```

### Introduction (context only: never use it for content warnings)

```text
Forget the Seven Wonders of the World. Globally, the Golden Arches are surely the most infamous man-made landmark. For over 50 years, more consumers have chosen McDonald's as the site of their McConsumption than any other fast food chain. With over 25,000 restaurants worldwide, McDonald's has certainly achieved an overwhelming presence. Could we live without McDonalds? Oh sure, we say we could live without Micky D's, but when push comes to shove we've all got Big Mac on the mind. Come on, admit it, you want one right now don't you? Meet Anna Mae . . . she’s attached to McDonald’s and here’s why. . . French Fries from Talking With by Jane Martin.
```

### Performance text (classify this)

```text
She is an old woman in a straight-back chair holding a McDonald’s cup. She is surrounded by several bundles of newspapers. She wears thick glasses that distort her eyes in the viewer.

ANNA MAE: If I had one wish in my life, why I’d like to live in McDonald’s. Right there in the restaurant. ‘Stead of in this old place. I’ll come up to the brow of the hill, bowed down with my troubles, hurtin’ under my load and I’ll see that yellow horseshoe, sort of like part of a rainbow, and it gives my old spirit a life. Lord, I can sit in a McDonald’s all day. I’ve done it too. Walked the seven miles with the sun just on its way, and then sat there on the curb till vie minutes of seven. First one there and the last to leave. Just like some ol’ French fry they forgot.

I like the young people workin’ there. Like a team of fine young horses when I was growin’ up. All smilin’. Tell you what I really like though is the plastic. God gave us plastic so there wouldn’t be no stains on his world. See, in the human world of earth it gets all scratched, stained, tore up, faded down. Loses it’s shine. All of it does. In time. Well, God gave us the idea of plastic so we’d know what the everlasting really was. See if there’s plastic then there’s surely eternity. It’s God’s hint.

You ever watch folks when they come on in the McDonalds? They always speed up, almost run the last few steps. You see if they don’t. Old Dobbin with the barn in sight. They know it’s safe in there and it ain’t safe outside. Now it ain’t safe outside and you know it.

I’ve seen a man healed by a Big Mac. I have. I was just sittin’ there. Last summer it was. Oh, they don’t never move you on. It’s a sacred law of McDonald’s, you can sit for a hundred years. Only place in this world. Anyway, a fella, maybe thirty five, maybe forty, come on in there dressed real nice, real bright tie, bran’ new baseball cap, nice white socks and he had him that disease. You know the one I mean, Cerebral Walrus they call it. Anyway, he had him a cock leg. His poor old body had it two speeds at the same time. Now he got him some coffee, with a lid on, and sat him down and Jimmy the tow-head cook knew him, see, and he brought over a Big Mac. Well, the sick fella ate maybe half of it and then he was just sittin’, you know, suffering those tremors, when a couple of ants come right out of the burger. Now there ain’t no ants in McDonald’s no way. Lord sent those ants and the sick fella he looked real sharp at the burger and a bunch more ants marched on out nice as you please and his head lolled right over and he pitched himself out of that chair and banged his head on the floor, loud. THWACK! Like a bowling ball dropping. Made you half sick to hear it. We jump up and run over but he was cold out. Well those servin’ kids, so cute, they watered him, stuck a touch pepper up his nostril, slapped him up right smart, and bang, up he got. Standin’ an’ blinkin’. .Well how are you, we say. An’ he looks us over, looks tight in our eyes, and he says, I’m fine.. And he was. He was fine! Tipped his Cincinnati Reds baseball cap, big, jus’ swallowed the canary grin, paraded out of there clean, straight like a polebean poplar, walked him a plumb line without no trace of the walrus.. Got outside, jumped up, whooped, hollered, sang him the National Anthem, flagged down a Circle Line bus, an’ rode off up Muhammad Ali Boulevard wavin’ an’ smilin’ like the King of the Pharaohs. Healed by a Big Mac. I saw it.

McDonald’s. You ever see anybody die in a McDonald’s? Nor sir. No way. Nobody has ever died in one. Shoot, they die in Burger Kings all the time. Kentucky Fried Chicken’s got their own damn ambulances. Noooooooooo, you can’t die in a McDonald’s no matter how hard you try. It’s the spices. Seals you safe in this life like it seals in the flavor. Yesssssssss, yes!

I asked Jarrell could I live there. See they close up around ten, and there ain’t a thing goin’ on in ‘em till seven A.M. I’d just sit in those nice swingy chairs and lean forward. Rest my head on those cool, cool, smooth tables, sing me a hymn, and sleep like a baby. Jarrell, he said he’d write him a letter up the chain of command and see would they let me. Oh, I got my bid in. Peaceful and clean.

Sometimes I see it like the last of a movie. You know how they start the picture up real close and then back it off steady and fat? Well, that’s how I dream it. I’m living in McDonald’s and it’s real late at night and you see me up close, smiling, and then you see the whole McDonald’s from the outside, lit up and friendly. And I get smaller and smaller, like they do, and then it’s just a light in the darkness, like as star, and I’m in it. I’m part of that light, part of the whole sky, and its all McDonald’s, but part of something even bigger, something fixed and shiny. like plastic.

I know. I know. It’s just a dream. Just a beacon in the storm. But you got to have a dream. It’s our dreams make us what we are.
```

---

## IC-0152: From the Flow

- Title: From the Flow
- Author (byline): Janet O’Neill
- Work: Turning Points, Pgs 63-65
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: TEACHER, MOTHER
- Teaser before the introduction: No
- Spoken words (computed): 964
- Already set (do not supply): none

### Source block (context only)

```text
Author: Janet O’Neill
Book: Turning Points, Pgs 63-65
Publisher: Tichenor Publishing
ISBN: 978-0742117013
Date: 2001
```

### Introduction (context only: never use it for content warnings)

```text
What I should have said: Suicide is not chosen; it happens when pain exceeds resources for coping with pain. That’s all it’s about. You are not a bad person, or crazy, or weak, or flawed because you feel suicidal. It doesn’t even mean that you really want to die – it only means that you have more pain than you can cope with right now. There are people out there (I’m one of them) who can be with you in this horrible time, and will not judge you, or argue with you, or send you to a hospital, or try to talk you out of how badly you feel. They will . . . I will simply care for you. I’m here . . . let me help.

What I did say: Keep the pen flowing. Never drop the pen . . . Just flow.

From the Flow by Janet O’Neill
```

### Performance text (classify this)

```text
TEACHER: (Pg 63-65) Welcome to my home away from home. Room 316. Parkside High. For thirteen years I have taught English composition to teens. Show them their voice. Help find their voice in print. I read a lot of Peter Elbow, who postulates that if you help someone find their voice, as a teacher, you are an educational success. So that's what I do; I develop voices. They write daily journals and that gives me the chance to delve into what makes teenagers tick. One writes of an impending pom squad tryout, another about their love of Nascar. One day, one writes, “Sometimes I wish the world would leave me alone. Or that I could leave it alone.” My inquisitive mind reels. Am I reading too much into it?

Journals develop voices. That's a fact. When I was sixteen, my English teacher made us write ten minutes a day. No subject. No "daily topic." And confidential -- no telling the parents anything! The only objective was to keep the pen flowing. Never drop the pen, he announced. Just flow.

His name is Dean Aiken and his journal has become my Friday obsession. Once a week, the students stack their notebooks under the chalkboard and I quickly race to Dean's writings first as soon as the bell rings. While others are talking about how the cafeteria food needs improvement, Dean writes in the abstract. He's a junior but hasn't made varsity baseball yet. He doesn't like that. He doesn't like having to take the bus to school. His parents used to take him. His writings were the same, yet constantly differing. Altering from the glass being half full to half empty. Why can't they just leave me alone? he’d write. "They" could be anyone. "They" were anyone.

Just flow. So I wrote. I told my teacher about how students told me I was a lesbian because of the way I dressed. Told him about how Tim Robertson always calls me a slut if I don't let him copy off my paper. Told him about how I felt sitting alone in the cafeteria for lunch until a teacher sat with me. It helped. And he helped, too. One day, we got a seating chart. Tim was seated in the opposite corner from me. It was only a seating chart, but it was a signal. He was helping me.

Dean's writing became erratic. Days would be skipped completely. Lines would be erased. I felt like some sort of voyeur trying to uncover the mystery of what he'd erased. Then he wrote: My granddad had it tough. He worked at a coal mine 6 to 6. But God helped him. He's resting at the cemetery next to a beautiful tree. He can sleep when he wants. Get up when he wants. He must like that. I know I will. Not "would," but "will." My God, I thought. Does this child really want to die? I slipped a card for a local youth center into his journal. Maybe he'll go, I thought. He has to go.

People think I'm weird, he'd write, but they just don't know what's going down. The messages became blatant cries. I have nowhere to go. I kept him after class to discuss things. What things? He’d say. We'd stare at each other and fifteen minutes later, he'd leave with a pass. Sorry to waste your time. My teacher solved it with a seating chart. I can do this. I can.

My mind raced. What should I do?? I can't tell his parents -- that's the whole point of the journals. It's a secret. But they should know. Could I tell the principal? That'd be worse. He's not even family. Besides, he hasn't actually said he's suicidal, right?

The classes are called to the auditorium over the intercom. The principal steps to the microphone. He announces that a student at our school, Dean Aiken, has died from a fatal gunshot wound to the head. I pinch myself. Wake up! I said. Wake up! But there I was. In an auditorium filled with now-mourning people, apparently the only one who saw it coming. And the only one that did nothing about it. Newspapers ran stories that night, denouncing his father for keeping a gun in the house. Part of me wanted to blame him. I needed someone to share the blame.

Class was canceled for the funeral. Dean has a lot of friends. I could have helped. I could have told. How bad could it have been? I could have done something. Instead, l’d told him to flow.

When his mother asked for a meeting, I was not shocked. She had gathered his belongings from his locker and scoured over them undoubtedly. I would have done it, too. (the conversation echoes in her memory)

MOTHER: Do you read these journals??

TEACHER: Yes. Yes I do. Every Friday.

MOTHER: Then explain to me why you passed Dean's over.

TEACHER: I didn't. I read it.

MOTHER: Well, if you read it you would have known! We all would have known!

TEACHER: I knew . . . I knew.

MOTHER: Then why. Why!!

TEACHER: I don't know. See, the journals are confidential –

MOTHER: Damn you! He came to you. I don't know why he came to you, but he did. You chose to sit there.

TEACHER: No -- I kept him after class –

MOTHER: You call yourself a teacher. You murdered him.

TEACHER: I know, I know. Please forgive me. (to audience) Only I knew I wasn't just asking forgiveness from her. I was asking God as well.

TEACHER: I open my journal and write the events of the day. Usually, I write of achievements.

Accomplishments at the job. At home. With my family. Today, I write of being accused of murder. Today I write without having a response. I write to escape. I write to release. I write out of habit.

Just flow, I think. Just flow.
```

---

## IC-0153: From the Mississippi Delta

- Title: From the Mississippi Delta
- Author (byline): Endesha Ida Mae Holland
- Work: Not specified
- Publisher: Simon and Schuster
- Publication date as stated: Oct 1997
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MAMA, DR. FEINBERG, IDA MAE, CHILD, MAN, JEAN, WHITE NURSE 1, WHITE NURSE 2
- Teaser before the introduction: Yes
- Spoken words (computed): 2033
- Already set (do not supply): none

### Source block (context only)

```text
Author: Endesha Ida Mae Holland
ISBN: 978-0684810119
Publisher: Simon and Schuster
Date (Month/Year): Oct 1997
```

### Introduction (context only: never use it for content warnings)

```text
For a young Black girl growing up in Mississippi in the turbulent 1960’s life held promises of poverty, prejudice, and broken dreams. Ida Mae Holland refused to accept such a bitter legacy, and with her mother’s inspiration, reinvented herself from meager beginnings. But as a young Civil Rights activist, she encounters the greatest test of her spirit and perseverance – the fire-bombing of her home with her mother inside.

From the Mississippi Delta by Endesha Ida Mae Holland
```

### Performance text (classify this)

```text
NARRATOR (Adult Ida Mae): (Pg 49-50) Children who spend most of their time around grown-ups grow old and wise faster than children who seldom see grown-ups except at meals or when some teacher is talking at them. Children left to other children are only children, but children like me – with Mama always talking and telling me about life – are at one child and adult. One of her favorite topics was how proud I’d be of her once she got her permit to practice granny midwifery, a goal that always seemed somehow out of reach.

MAMA: You gots ta have a dream, ‘f’n you gwine be somebody.

NARRATOR (Adult Ida Mae): In Mama’s dream, she was dressed in a clean white starched dress just like nurses wore, and she was toting a bulging black bag like doctors carried. But the hospital wouldn’t treat colored women, so Mama would help until Dr. Feinberg and the granny midwife got there. Mama had magic hands. Once they arrived much later than the baby who’d arrived [only] with Mama’s help. Dr. Feinberg said . .

DR. FEINBERG: You ought to become a granny catcher your own self.

NARRATOR (Adult Ida Mae): That’s when it started, Mama’s dream of catching babies.

NARRATOR (Adult Ida Mae): (Pg 50-51) Now to lots of folks any dream of bettering yourself was an uppity kind of dream. Too many of them had dreamed of a better life, even worked at it, without success. And rather than be tortured by dreams, many decided not to dream at all. So Mama was brave, in dreaming – in wanting something despite the odds. And the odds were long. A licensed granny midwife had to be able to read and write . . . Mama didn’t know her ABC’s! [But] This was Mama’s grand dream, the dream from which I learned how to dream-- big and unafraid, no matter what obstacles or bitterness are put in your way.

MAMA: You gotta start somewhere, an’ a dream is jest as good a place as any!

NARRATOR (Adult Ida Mae): Mama had another dream -- that I would go to college. She was proud that I could read and write and she understood the importance of education. Although it was too late for her, it wasn’t for me.

IDA MAE: (Pg 52-53) I gots me a dream, too.

MAMA: What for! Dreamt ‘bout pee-de-bed?

IDA MAE: No, Mama. I’s talkin’ bout a dream like yours.

MAMA: I beg your pardon, chile -- what you mean?

IDA MAE: I mean I wants to be a drum majorette! (marching and twirling an invisible baton)

MAMA: (laughing) Well, now you jest oughta do dat, Ida Mae. Ain’t nobody kin turn a stick like you do! You is nine years old – but you got mo’ sense den folkses ten time ol’er den you is. Yet dere be thangs in dis world you don’t know nothing ‘bout.

IDA MAE: (hopping on one foot, she tosses the imaginary baton in the air and catches it) Thangs like what, Mama?

MAMA: (sadly) Thangs dat mama hens gots to do to feed her chicks. I knows dat you is ‘shame o’ me.

NARRATOR (Adult Ida Mae): I never told Mama how my schoolmates low-rated our family. Their insults escalated into the dozens. They’d sing songs they made up to tease me as well.

CHILD: (sing-song voice) Mr. So-and-So came a-knockin’ on Aint Baby’s door, and when his wife finds out, man, will she be sore!

NARRATOR (Adult Ida Mae): They’d accompany the song with nasty gestures to illustrate what went on in the other side of our row house and out back in the wood house.

MAMA: I’m gwine git me my dream, Ida Mae! You gwine see. I be marchin’ down yon’er to git my permit to practice!

IDA MAE: You gonna be Somebody!

TRANSITION The Delta town of Greenwood, Mississippi may have well been the most southern place on the earth and in the 1960’s still deeply segregated. The dream of equality, of bettering yourself in a white world was still very much a dream; but for Ida Mae a dream worth fighting for . . .

(echoing in a solemn voice) A story, a story. Another story is coming. Stop talking and listen. Let it go, let it come – African Griot’s Preamble

NARRATOR (Adult Ida Mae): (Pg 210-212) The people I was working with were interested in one thing and one thing only: freedom.

IDA MAE: (to Mama, excited) I be signing’ up de folkses to go to de courthouse to vote

MAMA: (angrily) Vote! Vote! You be messin’ ‘round wit’ dem Riders who ain’t got no sense. You best lissen t’me, gal. Don’cha git in wit’ dem fools. All dey gwine do is git a lotta folkses kilt. Stirrin’ up trouble twix de white an’ us coloreds. Makin’ us ‘fraid for our life wit’ dey talk ‘bout reddishin’ t’ vote and bein’ good as de white folkses. Lawdy, Lawd (looks to the sky) us’n poor ol’ colored folkses needs you now! NARRATOR (Adult Ida Mae): (Pg 254) (proudly) In 1963 I was arrested 13 times. My rap sheet included “disturbing the peace,” “inciting a riot,” “unlawful assembly,” and “parading without a permit.” (Pg 290-292) We began 1964 with integration and equality as our goal, led by such big-spirited souls as Bob Moses and Martin Luther King, Jr. The Nobel Peace Prize Dr. King received was hailed as a victory for our cause, but to me it seemed more like a funeral wreath. But by then, Greenwood was no longer a hotbed of Civil Rights activity. On the whole, nobody wanted to stir up white people’s anger, so a quiet pall hung over Greenwood. Even the Klan had been strangely quiet [until one morning . . . ]

MAMA: (whispering) Ida Mae! Ida Mae! Wake up gal an’ lissen!

IDA MAE: (heart pounding) What is it, Mama? What’s wrong?

MAMA: Dem dogs, Lissen how they be barkin’.

IDA MAE: Aww Mama, they just treed a cat.

MAMA: Gal, I knows how dogs sound when dey tree de cat. Sound t’me like dey gots a crook in de th’oat! C’mon now-git up an’ see—An’ don’t turn dat light on, neither!

NARRATOR (Adult Ida Mae): I stood with the back door open. I doubted whether anyone would want to break into our house; we didn’t have anything worth stealing. Still, all the neighborhood dogs were barking. seemed wrong, exactly, but then again, things didn’t seem quite right.

IDA MAE: (crossing arms for warmth) Just Frisgo and a whole buncha dogs, Mama.

NARRATOR (Adult Ida Mae): I chained Frisgo to the wood house and came back in. The sun was almost up, so I filled the tin tub to bathe. I had a big day ahead. A squad of us local Civil Rights workers had assigned ourselves the task of integrating the lunch counter at the white hotel. I would take my seat in the plush “white only” hotel and politely ask for my cup of coffee. I dressed – overalls starched and ironed – clothes I could afford to get beat-up and arrested in.

MAMA: Gal, I don’t know why y’all gots t’ drank coffee wit’ de white folkses who don’t want y’all round. Runnin’ down yon’er t’ cause trouble--

IDA MAE: Mama.

MAMA: Never mind.

NARRATOR (Adult Ida Mae): Later, I would spend many sleepless nights trying to recall exactly what happened next. I remember . . . (Pg 294-295) I heard the explosion and saw the hot, black smoke turn February into summer, day into night. I heard a scream, but I couldn’t move. I knew that trouble had come for me, but there was nothing I could do.

I saw a ball of fire floating across our yard toward the rose bush. The ball rolled over and turned into (beat – in horror) Mama! All Mama’s skin and hair had burned off, leaving charred flesh and pink muscle. Our old house was gutted ruin, its frame burning greedily. Frisgo’s barbecued body dangling by a blackened iron chain from the charred post of the wood house.

Mama was still alive, but barely.

MAN: Don’t touch her!

NARRATOR (Adult Ida Mae): (holding out her hand in horror) . . . because her skin came off in your hand. Men loaded Mama into the hearse and I piled in after her. (Pg 296-297) As we screeched down Main Street for the hospital, I found the only unburned place on Mama’s body -- the palm of her hand -- and held it gently. There was nothing else I could do. The next time I saw Mama, she was in the colored wing, bandaged from head to toe.

JEAN: I knowed you was gonna git somebody kilt – messin’ wit’ dese white folkses!

NARRATOR (Adult Ida Mae): I had broken an important rule of the [Civil Rights] Movement: never take on the power structure without knowing that reinforcements were available. I took a chair on one side of the bed -- a different kind of sit-in. I found the unburned pink palm again and held it. For more than a week, Mama just lay there, wheezing through her scorched throat. A steady stream of friends and relatives came by to pay their respects – one by one they refused to look into my eyes. While I was out in the hall after one of these visits . . .

WHITE NURSE 1: I can’t stand the smell of that colored girl!

WHITE NURSE 2: Shhhh! She can’t help it. Besides, she won’t last much longer.

NARRATOR (Adult Ida Mae): When I went back in, Mama’s eyes were open for the first time since the fire.

IDA MAE: (Pg 298-299) You want water, Mama?

MAMA: (painfully) Tote me t’vote, gal.

NARRATOR (Adult Ida Mae): (crying) I couldn’t hug her, so I just clutched the edge of the bed till my knuckles turned white. A few days later, she died. I stood by her bed and it was just me and Mama alone as it had been for so much of my life. Her wide old face was placid -- like it was all finished -- satisfied with what it had done in life and glad to be free of it. I traced Mama’s lips with my finger and told her . . .

IDA MAE: I’m gonna be Somebody. You rest now. I swear ‘fore God, Mama -- I’m gonna be somebody. (kisses her)

NARRATOR (Adult Ida Mae): I’m going to tell you something that you may not believe. After I made my promise, I swear that Mama said, clear as day:

MAMA: Gwine see - thank de Lawd.

NARRATOR (Adult Ida Mae): She had nothing more to say. I suppose I should’ve been scared or spooked, but all I was was happy. Funny thing is, I continued to hear her voice every now and again after that. Sometimes it made me cry, but it never made me sad. I have heard it off and on for years. (beat)

(Pg 304-305) After Mama’s death, I had a hard time rationalizing the gains we had made as having been worth all they’d cost us. True, there was talk about black children going to the local white schools, but I had heard that kind of talk a decade ago. Dr. Kind led the march from Selma to Montgomery – the last great battle in the voter registration wars. But even that was overshadowed by the 6-day riot in Watts, the black ghetto in Los Angeles – a sign of black people’s social and economic frustration. And Malcom X assassinated in New York.

I began to see that a child does not need to dwell in her mother’s house forever to be a loyal daughter or stay in her birthplace to remember where she’s from. I left Greenwood for good. Like so many others before me, I headed north to find a life that, simply by being “normal,” would be better than the one I had left behind.

(Pg 313) Since I’ve let mama take her ease among the stars, these are thoughts that crowd into my mind most often: • If you’re so far down and out, you feel you can’t get back up, I assure you from the bottom of my soul, the journey home is shorter than you think. • If your mama is still living, give her a great big hug and kiss from me, and always remember where you came from. • If you happen to be a white man or woman . . . I made it. Those black boys and girls you see around you can make it too. You may give them something had to push against or you may give them a helping hand – that’s up to you. But the helping hand feels a lot better. • Finally make a promise right now that you will never, ever give up your dreams. If you’ve been a ho’, be a doctor too. If you’ve hurt a man, be a healer. The world began when you were born. It will be whatever you make it.

(Pg 308) Twenty years after I’d left the Delta, I marched down the University of Minnesota mall -- the only black face among all the doctoral candidates. (Pg 311) I had come a long way from the Mississippi Delta. Somwhere in the midst of all the hollering, I heard my Mama’s voice.

MAMA: (Pg 212) Lawdy, Lawd (looks to the sky) (Pg 49) You gots ta have a dream, ‘f’n you gwine be somebody.
```

---

## IC-0154: Frozen

- Title: Frozen
- Author (byline): Bryony Lavery
- Work: Not specified
- Publisher: Faber and Faber, Inc.
- Publication date as stated: April 2003
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NANCY, AGNETHA, RALPH
- Teaser before the introduction: Yes
- Spoken words (computed): 1695
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bryony Lavery
ISBN: 978-0571217380
Publisher: Faber and Faber, Inc.
Date (Month/Year): April 2003
```

### Introduction (context only: never use it for content warnings)

```text
Frozen by Bryony Lavery is much more than a story of child abduction and murder. It is a story of the struggle to understand and to forgive when the very act of forgiveness seems absurd. Malcolm Gladwell once wrote: “The difference between a crime of evil and a crime of illness is the difference between a sin and a symptom . . .” *

An illness can be forgiven; but can someone who is inherently evil? And how do you determine the difference? In this selection Nancy, the mother of a murdered child and Agnetha, a psychologist, work through the struggle 20 years after Rhona disappears.

Frozen by Byrony Lavery
```

### Performance text (classify this)

```text
NANCY: (Pg 22-23) (in a school hall, to audience) On April 17th, 1980, my daughter, Rhona walked out of my house to go to her Grandma’s house. She never got there. She never came back. She was ten. She’s been missing for five years. She will be fifteen years old tonight. I know she’s alive, I have Faith. Every night I pray that whatever reason is stopping her coming home will be removed and that she’ll phone or write or just knock on the door and say “Mum, it’s me.”

NANCY: (Pg 28-29) Four days ago, two young policeman say . . . “We have apprehended a man in the unsuccessful attempted abduction of a young girl . . . subsequent inquiries have uncovered a lock-up shed. The earth floor contains the remains of other children. The man is now giving us names. One of them, he says, is Rhona.” All this time I’ve been growing her up she’s been -- He’s had her buried away . . . ******* A large, academic hall *****

AGNETHA: (Pg 34-35) (in “lecture mode – to audience) "Serial Killing ... A Forgivable Act?" It is a critical examination of the differences between crimes of evil and crimes of illness. I base my critique upon a psychiatric and neurological study of the criminal brain. My name is Dr. Agnetha Gottmundsdottir. I am a psychiatric explorer. My chosen expedition -- the Arctic frozen sea that is . . . the criminal brain. (Ralph's head lit as if it is an exhibit) Let us take a look. (walks over to stand behind Ralph, gesturing around his head, but not touching)

The cortex is the thick covering of grey matter on the upper part of every human brain and the function of the cortex, in particular, the frontal lobes, is to modulate the impulses that surge up from within the brain. To provide judgement, to learn and stick to rules of everyday life. They are responsible for making us human.

Ralph Ian Wantage is currently in Long Larron Maximum Security Prison serving a life sentence for the abduction, sexual assault and murder of 7 young girls over a period of 21 years. ****** Agnetha and Ralph, prison cell*****

AGNETHA: (Pg 37) I’m not gonna harm you. I’m gonna tap you on the nose . . . (She the bridge of his nose.

RALPH: (blinks rapidly, distressed) Hey, hey, hey, hey . . .

AGNETHA: (moves away, showing us on her own nose) When you tap someone on the bridge of the nose, it's reasonable for the person to blink a coupla times because there is a threat from outside. When it's clear there is no threat, a person should be able to accommodate that. But if the subject blinks more than three times, that's what we call "insufficiency of suppression" which may show frontal lobe disfunction. You can't adapt to a new situation. There's a certain rigidity there. Like the person is ice-bound ******* Nancy’s house******

NANCY: (Pg 38) You can go and be there when they die . . . murderers. They show you the electric chair, how it all works. And then, you can be present, members of the victims’ families at that final moment. (Pg 37) I’d like to see him die. Watch him suffer. He wouldn’t suffer like she suffered. But it would be something. An eye for an eye. ******* A large, academic hall *****

AGNETHA: (Pg 46) (in “lecture” mode – to audience) Over the years Dr. Nabkus and myself have studied more than 250 dangerous criminals. In significant numbers, these men have incurred physical damage to the brain. After Dr. Nabkus has finished his medical history, I look for evidence of child abuse (Pg 50) [It] causes profound and pathological changes in the structure of the brain as surely as does physical injury. We brain scanned the children of severe neglect [and] found that entire structures of their cortex never properly developed. (Pg 51-52) What you get is a kind of erraticness -- they can be very different in one situation compared to another. There is a sense that they don't have a larger moral compass. ***** Ralph and Agnetha, prison cell*****

AGNETHA: (Pg 62) No remorse then, Ralphie?

RALPH: Remorse. So what is that . . . remorse?

AGNETHA: Like Regret. But more. You repent your sin. You feel sorrow, pity, compassion. A sort of . . . tender feeling.

RALPH: I can’t say I do. (pause, thinks) The only thing I’m sorry about is that it’s not legal

AGNETHA: What’s not legal?

RALPH: Killing girls. ****** Nancy meets with Agnetha *****

NANCY: (Pg 59-61) I’m “in a very bad space.” I know that. I know I’m ready.

AGNETHA: How?

NANCY: He . . . (she has to do this) forced her into the van. And, and, and he. . . wrapped her in polythene sheeting. She was unconscious but she wasn’t dead then. He took her to a shed and we think he sexually assaulted her before he held the polythene on her face and suffocated her. (short of breath)

AGNETHA: Breathe. (both inhale and exhale; Nancy following Agnetha)

NANCY: I’m accepting she’s dead. But (pause. somehow an awful admission of guilt) I’m not! And I need to (hand gesture of moving forward) So he’s the next step. I want to know why. I want to know why her. She’s 10! I want him to know what he’s done. I want him to know how I feel. I want to understand. If I could understand why . . . I might be able to (hand gesture of moving forward) They said you could help. It’s time -- I want a visit. ******* The following are separate monologues from Agnetha and Nancy interspersed – they are not talking to one another.

AGNETHA: (Pg 67) (calm, clinical) Most forensic psychiatrists tend to buy into the notion of evil. I don’t. I can’t. I find no evidence that people are born evil. To be evil is to be “morally depraved.” That bespeaks having conscious control over something. The serial murders I have tested are not in that category. Their deeds themselves are bizarre, grotesque, life-destroying -- but not evil. They are driven by forces beyond their control.

NANCY: (Pg 65) (angry) I’d swing that bloody American doctor woman round by her. . . (quotes) “The experiment is unviable! The components unstable!" Who does she think she is? I've written some letters made some phone calls. I'll get that visit!

AGNETHA: (Pg 67) (calm, clinical) The difference between a crime of evil and a crime of illness is the difference between a sin and a symptom.

NANCY: (Pg 55-56) (incensed) If I go to see him, I’m taking a gun. Blow his brains all over the wall. I’m taking a knife; slice his thing off. Stick the blade through his eye and take out his brains! What he thought to do -- what he did . . . She was my little girl! And she said (pause) forgive that monster. I can’t do that. How can I do that? It’s too much. (long pause as she battles with her emotions)

AGNETHA: (Pg 67-68) (somewhat judgy) I guess as a moral society -- as a punishment society . . . We can’t let the notion of these deeds being “symptoms” intrude in the relationship between murderers and the rest of us.

NANCY: (Pg 39) (deep breath) I can forgive. But I can’t forget. *****Prison visiting room -- Nancy enters*****

NANCY: (Pg 68-73) (to guard) That’s him? (goes to stand in front of Ralph) Ralph Wantage? (he looks up; barely nods) Nancy Shirley. You got my letter. You agreed to see me.

RALPH: She was your kid . . . one of them.

NANCY: Rhona RALPH: Rhona. (pause)

NANCY: I want you to know I forgive you for killing my daughter. (silence -- Ralph abruptly covers his eyes with both hands) I don’t hate you. I used to, but I don’t anymore. (silence, Ralph has nothing to say) I’ve brought some photographs, would you like to see them?

RALPH: Of . . . her?

NANCY: Rhona (she gets them out. A small dog-eared selection, hands them to him in turn) As a baby. (next) That’s me holding her. Her cat is Fluff. (next) This is Rhona dressed as an octopus for a fancy-dress competition.

RALPH: Did she win?

NANCY: She came third behind Little Miss Muffet and a Loch Ness Monster.

RALPH: She should have won. (beat) I don’t think I hurt her . . .

NANCY: You did.

RALPH: I don’t think she was frightened at all . . .

NANCY: She must have been. She must have been frightened! (Ralph thinks . . . Nancy watches him carefully. When he looks up suddenly, she holds his gaze. He looks away . . . she touches his arm) Your dad? What did he do?

RALPH: My dad, well, he was the disciplinarian obviously.

NANCY: Made you behave, did he?

RALPH: Oh, yes! Say you swore filthy language . . . He’s got you by the hair here (back of neck) And you’re in the washing up water. Wash your mouth out with soap water! Or you done wrong . . . anything . . . he’s (in Dad’s voice) “See it in my eyes? Can you see it, you little pillock? I’m looking into you and I’m seeing shit! You keep yourself clean! You hear me?

(sound of a thump on flesh . . . Ralph registers it, side of head) You deaf little bugger! (another thump, same side of head) You listening to me? (tap on forehead) You sand still and don’t move one muscle! Not one! You don’t even blink until you know I mean what I say. See it in my eyes?” (blinking rapidly)

NANCY: Frightening bugger. (Ralph nods) Hurt you a lot. (beat, then another nod) Can you see it hurt Rhona then? Can you see it frightened her? What you did.

RALPH: (Ralph thinks impassive for a long time, then) Yes. (nods, tears in his eyes . . . he wipes them fiercely. Violently. Dry painful sobs start. Nancy watches. He holds his chest in pain as the sobs subside. Calmly Nancy takes out a tissue and hands it to him) (harshly) Don’t come and bother me again. (Nancy exits) ***** Agnetha and Ralph – Prison cell*******

AGNETHA: (Pg 76-78) Well, Ralph. This is my last visit. I wondered if you wanted to tell me anything more. And I came to say “Goodbye.”

RALPH: (cautiously) I’ve been wanting to tell you things. I think I caught cancer or something. (motions to his chest) Here. That’s lungs right? Lung cancer.

AGNETHA: What does the doctor say?

RALPH: Says it’s just stress! Stress is in here (motions to his forehead) I know where stress is! This gnawing, here! (motions to his chest) Not stress!

AGNETHA: That’s your heart, Ralph. How long have you been in pain?

RALPH: It started . . . night after that mother of that girl Rhona I done came . . . That was Thursday . . . so (Counts on his fingers) It’s been a bit.

AGNETHA: Mrs. Shirley came to see you? I recommended she . . .

RALPH: Well, you were overruled by the Doctor-in-Charge!

AGNETHA: And she visited with you?

RALPH: She’s forgive me, actually. (spasm in his chest)

AGNETHA: (thoughtfully) What you are feeling may be psychological. What you are feeling may be remorse and that will be very painful for you, Ralph.

RALPH: (hardens again, he speaks to himself) It’s a question of finding a window of opportunity ***** Ralph, alone in his cell******

RALPH: (Pg 79) (Ralph, in his cell, sweating. Fashioning a noose with his belt and a long cloth. He slings it over the pull up bar and stands on his chair) Gnawed to death? I don’t think so.

(completes his preparations. Kicks the chair away from him. He hangs, choking, jerking) ***** Graveside – Ralph’s funeral******

(Nancy stands at the gravesite. Athena, entering, watches her for a few seconds)

AGNETHA: (Pg 79-82) Not a big funeral . . .

NANCY: (sarcastically) Bit of a surprise . . . person with his talent for putting sunshine in everybody’s life.

AGNETHA: You went to see him.

NANCY: And you tried to stop me.

AGNETHA: I was trying to protect everybody

NANCY: Him. AGNETHA: Everybody

NANCY: Him. How much time and energy did you give him? And me? (beat) You look upset. Were you fond of (beat) Ralph?

AGNETHA: It’s not for Ralph . . . It’s for somebody else. For me.

NANCY: Me as well. I couldn’t feel much for him really . . .

AGNETHA: No. It was . . . not easy. (Both nod thoughtfully)

NANCY: Do you think he did it . . . the . . . suicide . . . because I went to see him?

AGNETHA: (long silence) Yes. (long silence, then in a rare show of emotion) My colleague and best friend, David, died three months ago. Stupid accident – wearing a seat belt, observing the speed limit. A truck goes out of control – smashes the care. The truck driver is unhurt. David – I worked with him every day for 10 years. Two days before he died I slept with him. It just happened. His wife is a very good friend. Why am I telling you this?

NANCY: Why are you?

AGNETHA: Do I tell her?

NANCY: No. You just suffer. “The difference between a crime of evil and a crime of illness is the difference between a sin and a symptom . . .” Your words. I read your thesis. You knew what you were doing. Live with it.
```

---

## IC-0155: Gargoyle

- Title: Gargoyle
- Author (byline): Joyce Carol Oates
- Work: Not specified
- Publisher: Narrative Magazine
- Publication date as stated: 2009
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2878
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joyce Carol Oates
On-line Magazine: Stories of the Week: 2008 - 2009
Website: https://www.narrativemagazine.com/issues/stories-week-2008-2009/story-
week/gargoyle-joyce-carol-oates
Publisher: Narrative Magazine
Date (Month/Year): 2009
About the Website: *Narrative is dedicated to advancing literature in the digital age by
supporting the finest writing talent and encouraging reading across generations, in schools,
and around the globe. Our digital library of new literature by celebrated authors and by the
best new and emerging writers is available for free.
```

### Introduction (context only: never use it for content warnings)

```text
What to make of loneliness. Can you imagine? Aloneness. Loneliness isn’t fashionable. It isn’t considered a subject one can talk about. “Gargoyle” by Joyce Carol Oates
```

### Performance text (classify this)

```text
Three-fifteen a.m. and you lie spread-eagled in bed in your cocoon of a bed in your ripe swollen cocoon of a body while I drive through the snowy drizzle querying myself about life.

Driving along a deserted boulevard. Yellow street lights high atop slender poles. Rain, snow. Mist. Wind. What to make of loneliness. Not anger, not rage, not the wish to die or even the wish to murder. I’m too exhausted for all that. Just loneliness. What to make of it. Aloneness. Can you hear me? Can you guess? Never. You are eight months pregnant now and lie sleepless beside my lover, your spine aching, your stomach bloated, you are a beached bewildered mammalian creature gasping in the air. Can you guess at me? Never. But do you sense me, do you fear me?

Three-sixteen a.m. on a Friday morning, or do I mean a Thursday night. I drive too fast, and then slow down, skidding on a patch of ice a quarter-mile from your bed. My loneliness has turned sinister. I can’t be trusted. Your husband sleeps beside you and in the confused instant of waking he could not know—he could not possibly know—which woman lies with him beneath the covers. Suppose he smells the sweet-stale odor of blood, what then? His face would stiffen with disapproval and even with disgust but he could not know who lay close beside him in the night. Your husband. My lover.

What to make of aloneness in the slowly falling snow. In the bluish dusk of a city’s night. I know your house well and I have even visited your bedroom and your bed and I know how you lie awake, your eyes burning, not allowing yourself to think of me. It’s difficult to find a comfortable position in that bed. Not only is your stomach so swollen—a little too big, in fact, for an eight-months’ pregnancy—but the mattress sags toward the center. You don’t want to press against your husband because you might wake him and his personality, introduced into the night, will injure it. He’s breathing harshly, with chortling gasping sounds. His sleep isn’t easy, isn’t restful. He has never lied to you. Of course not. You with three children and a fourth imminent and your head crowded with visions: you are never lonely. Never. If you could imagine me driving alone on Maidstone Avenue at three-twenty a.m., smoking my cigarettes and talking to myself, and singing snatches of half-remembered songs, you would feel only pity. And if you could guess that I was dramatizing my condition, working it into an interesting anecdote I might someday (not soon: but someday) tell my lover—how you might laugh, scornfully, and with slight hysteria. Suppose I told him. And he listened attentively enough, and then flushed with embarrassment. And irritation. My melodic laughter. My slender pretty inconsequential face. Or am I pretty?

You are rather ugly these days. Sallow-skinned, with dark pouches beneath your eyes like bruises. This fourth pregnancy (which was whose idea?—surely not his) is nearly as difficult as the first. But you aren’t going to be frightened. You aren’t going to wonder if it was a mistake. . . . Three weeks pregnant; and then two months; and then five; and six; and seven; and eight. A wide dark river carried you along with it. If you sat gasping for breath at the top of the stairs, your knuckles pressed against your mouth, you never told anyone; nor did you tell anyone about your dread of the upcoming birth. Nor about the crazy fear during the first several months that you would miscarry, or would arrange for an abortion, carried along like a woman in a dream.

You haven’t been lonely for years, have you. Not since your marriage. Why do you keep so much from your husband, don’t you trust him? He doesn’t love you but, of course, he’s very fond of you. He still approves of your appearance: that sturdy strong-boned flesh of yours, the face of a Flemish peasant who is almost beautiful. When he looks at you, you shy away, not wanting him to see the shadows beneath your eyes, the death-mask, the slightly twisted, sullen, mad mouth. I no longer love her but I’m very fond of her, he said. I’m deeply committed to her.

I think about you, lying there in your bed. I think about myself driving along the empty streets seeking knowledge. And adventure, perhaps. I wonder—didn’t you ever smell me on him? My hair, my skin, my body? There were times when we lay pressed together for hours, our skins sleekly wet, our eyelashes touching. Little whore, he whispered fondly, admiringly. Aren’t you a little whore.

Once you stared at him and saw the awed, sickened love in his face, the web of his thoughts stuck close against his skin. What are you thinking about, you might have asked, uneasily. Sullenly. What are you making faces at—! He glanced up at you guiltily. Your eyes met in shame. Are you beginning to sense me now?

Driving east along Flat Rock Avenue. Three-twenty-five a.m. The pill’s famous effect is generated out of one’s resistance to it: staying conscious while the drug urges unconsciousness. Shadowy arms reach up to pull me down but I resist. Not yet. Not yet. The car’s wheels turn of their own volition onto a side street where the snow seems to be falling more thickly than elsewhere. What to make of loneliness. Aloneness.

The fashion today, which you and I both read about in women’s magazines, is independence. The joys of living alone. Autonomy. Or maybe the fashion is to dwell upon the sporadic loneliness within a family, within (even) a marriage. Crap. Glamorous crap. I am talking about the real thing. Which you know nothing about, you with your three adorable children and your bloated stomach and the life kicking within it, and your snoring husband at your side.

Loneliness isn’t fashionable. It isn’t considered a subject one can talk about. There are people who brag about living alone, who speak in public about the joys of aloneness, but they fall silent if someone asks them about loneliness. The Well of Loneliness. Loneliness. The Well of. Never read the novel. Paged through it years ago, in high school. Struck by the title. Loneliness: The Well of. You wouldn’t know because you have not fallen into that well. You wouldn’t know because you are stuffed with life like a sausage filled to bursting. You wouldn’t know because you tell so many lies, even to yourself.

The snow is mixed with grit. I don’t know why. The windshield wipers leave a scummy glaring mess.

You heave yourself from bed, gasping. My lover murmurs but does not wake. Thank God. His hoarse labored breathing begins again. Barefoot you stand beside the bed in the faint light from the window, uneasy, puzzled. You cannot quite see me. Once when you stared at your husband’s face, at his sad cunning hooded eyes, you caught a glimpse of a face: a ghostly face; but in the next instant it vanished. What are you thinking about, you asked him sullenly. The fear began then but you never acknowledged it.

I am driving north now along a narrow street called Railway. It intersects with your street, as you know. I am not drunk, I am not high, I am perfectly sane. Wide awake for the second night, in fact. Wide awake. The bars are closed and there is nothing to do but drive and call to you, whisper to you. That heavy trembling in your belly—do you suppose I can’t feel it? That panic that rises in you, rankly powerful as an odor of something foul, and secret—do you suppose I don’t understand it? You don’t approve, do you? Drawing your arm across your sweaty forehead, standing with your legs apart, your toes curling upon the floor.

My second night without sleep. Or is it the third.

What to make of loneliness—what is it, exactly? Do you know?

A few weeks ago an extraordinary compulsion came over you and you sat in the kitchen alone, in secret, and ate bread: piece after piece. You were ravenous. You didn’t smear butter or jam on the bread but simply ate it piece after piece. Your jaws ground. It drew upon you, it demanded nourishment at once. Everything was distant to you at that time, during those bizarre forty-five minutes—your children, your husband, your own individual life. You were utterly alone with the baby-to-be. You were utterly alone with its appetite.

I think that would have frightened me—the realization that another being pulsed along my veins, and that I was subordinate to it. That I did not exist, maybe. Not as I liked to think.

The stubborn clotted bit of flesh was expelled from my body. I didn’t succumb to it. How many years of love, you are wondering.

Making your way clumsily downstairs, lowering yourself from step to step with caution, not wanting the stairs to squeak. Are you hungry again? Headed for the refrigerator again? Pale sick trembling ghoulish woman! Someone’s arms rise to pull you down, you shudder and arch your back, resisting. No. Not yet. Not here. One by one lights in the brain go out, extinguished for the night, and the trick is to resist keeling over. What are you listening for, at the foot of the stairs?

What to make of loneliness. Like old clothes, old shoes. You can’t wear them but you can’t throw them out either. You can’t wear them. No matter how costly they were or how you liked them at one time. Dresses so short they might have belonged to grammar school girls, or hat check girls. (The dress of white wool that your husband liked: holding my face and talking fancifully of winter, snow, he and I isolated somewhere together, wolves baying in the distance. A forlorn crescent moon, the anguish of kisses that will come to nothing, the glamour of the unattainable. I examined the dress critically, saw that the inside of the skirt was stained, a stiff milkish stain. I must have put the dress away at the back of the closet without sending it out to be cleaned, as if I knew I’d never wear it again.)

Your breasts hang heavy inside your nightgown. They are uncomfortably large, with soft brown nipples. Your legs ache. In the darkened house you stand on guard, your eyes fairly bulging in their sockets. Surely you are not afraid of me . . . ?

I wonder, though, why you never guessed. Those years. The odor of my body must have been carried home to you many times. Your husband isn’t a very fastidious man, he showers several times a week, of course, but isn’t exceptionally clean, and the odor of my desperation must have come to you. Or are you too ignorant to understand? I don’t think you are ignorant at all. I think you are very wise.

Those sessions of love-making in his car. By the river, high above the river. For months afterward I dreamt of the hundred-foot drop, the muffled noise of the river, the curious wailing of the wind. A wide river, a steep incline. Wooded bluffs across the way. In his arms I clutched and wept, knowing he would let me go, knowing he hadn’t the strength to hold me as I fell. Falling down, down into the warm, thick liquid, the two of us struggling, gagging—always I was falling as the edge crumples, pitched into air, into nothing. Into that warm suffocating liquid that is so terrifying. And then I awake: sometimes there is a dull ache in my loins, an ache of sexual distress; sometimes there is only a sensation of loss, of numbness. Do you fall in your sleep too, knowing his arms won’t hold you—won’t support you? I drove out there one afternoon last week. For no reason. For the hell of it. Someone was parked there, in the very place my lover and I used to park. I wanted to tap on the window and ask: Is it good for you two here? Don’t you know the danger? The height—the river—the wind—the loneliness.

He didn’t lie. I don’t think they were lies. I think he believed them. I was the princess, he said; I was beautiful. He was in love. You, of course, were the third party, the excluded one: to be pitied, to be scorned. But taken seriously. (For you were suicidal, he claimed.) What a silly woman, I said, hearing of my rival’s behavior. He showed me a snapshot of you, reluctantly, and I said nothing at all, though my eyes curled with contempt. That face. Those eyes. How had she deserved so fine a man—! He enumerated your flaws: your moods, your bad temper, your messiness, your jealousy. Your nervousness.

Once in a second-hand jewelry and antique store on lower Main Street your husband and I prowled amidst tarnished candlestick holders and lacquered chests of drawers and cedar-lined trunks from the early 1900’s and rickety chairs and tables, and lamps, and vases, and untidy displays of chinaware, some of it very beautiful. But damaged. He offered to buy me a statuette of a puckish, rather battered Cupid. He was a little drunk. From wine. From lunch. From love. Maybe from the excitement of betraying you.

“Is that a gargoyle?” I asked.

“It’s a Cupid,” your husband said. “A misshapen Cupid. See, his wings are gone—they were broken off.”

We laughed over the thing. Love made us dizzy. Daring. Rather cruel. (For the salesman stood watching us patiently and we ignored him.) I turned the carving from side to side. It was a toad-like grimacing creature, about three feet tall, sly and lecherous yet, at the same time, babyish. What was it, I wanted suddenly to know. Who could have labored over such a monstrosity.

“The artist was serious, evidently,” your husband said. “Look at the detail here around the eyes.”

“He couldn’t have been serious,” I said.

One eye was screwed up in a gay bawdy knowing wink, and the other was wide-open and bulging. What did it mean, I wondered, surprised at its weight. There was something icy and shrewd about the Cupid’s expression, yet he remained an infant; he was infantile. His monstrousness was not his fault.

“I hate it,” I whispered.

Your husband was in fine spirits that day. He was not just a husband but a lover as well. His girl was a princess, his girl was beautiful, she was impregnable and exalted and slender as you were not, and near-virginal as, of course, you were not. Her breasts were small and hard, her nipples tiny, her belly flat and smooth, very smooth. Her legs were long. Her eyes often flashed. There was no one quite like her: she was remarkably young.

I walked quickly away into another part of the store. The Cupid did not amuse me.

My lover followed along behind me and took hold of my waist and kissed the side of my cheek. I smelled wine on his breath. “You love me, don’t you,” my lover whispered.

Barefoot at the bottom of the stairs you stand in your darkened house, your hands pressed on your enormous belly. Across the street a porch light burns. Snow falls in random spasmodic puffs. You do not allow yourself to think of my lover, who groaned aloud with passion in my arms, as if passion would kill him. As if no one had ever experienced passion before. You do not allow yourself to think of me, though I am driving along your street now, slowly, fearful of skidding on the ice.

Your belly is stretched to bursting. Bluish-white. You stagger with your own weight, a woman with a noble profile, a ravaged skin. I, who am empty inside, who was scraped empty inside, do not envy you. I would be afraid to be you, in fact. I’ve never been unfaithful, your husband says coldly. He stares at you, daring you to guess. He hates you, fears you, lives in awe of you.

Once he shook me by the shoulders, hard, blaming me for your unhappiness. Little whore, he whispered, what do you want from me . . . ?

I park at the curb, I leave the car cautiously, afraid of slipping on the ice. Who is that at the door, peering through the window of the door, watching for me? Why are you so still, so ghostly? In the street light I appear to you, a woman in a long dark coat and boots, moving like a sleepwalker. My arms outstretched. Are you going to let me in? Do you recognize me at last? I make my way cautiously to your front door and put out my hand, as if to ring the doorbell. But I don’t ring the bell: I merely press my fingertips against the window. And you, inside, in the warm slumberous depths of the house, hesitate only a moment before putting out your hand as well, so that our fingertips meet—nearly meet— through the glass.
```

---

## IC-0156: Gidion’s Knot

- Title: Gidion’s Knot
- Author (byline): Johnna Adams
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: March 2014
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CORRYN, HEATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 2103
- Already set (do not supply): none

### Source block (context only)

```text
Author: Johnna Adams
ISBN: 978-0822229674
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): March 2014
```

### Introduction (context only: never use it for content warnings)

```text
Gidion’s Knot . . . a reference to a legendary chapter in the life of Alexander the Great in which he is tasked with unraveling several knots so tightly entangled that it is impossible to see how they are fastened. Since then, the phrase “Gordian Knot” has been used to describe a complex or unsolvable problem.

Gidion's Knot by Johnna Adams turns out to be as difficult to unravel as the Gordian one for which it's named. You see, this is a play about the death of a child. It is also a play about the right to freedom of expression and whether it is limited by society’s needs. And it is a play about the support a mother must and will give her child. Ultimately it is the story of a confrontation between a mother and a teacher.

Gidion’s Knot by Johnna Adams
```

### Performance text (classify this)

```text
Setting: A 5th grade classroom in a public school in the Lake Forest suburb of Chicago.

CORRYN: I missed open house. So we never got to meet.

HEATHER: You’re Gidion’s mother.

CORRYN: You can call me Corryn. You sent a note home with my son. Asking to meet with me. . . . Telling me he was suspended.

HEATHER: I’m so sorry. I’m so sorry. I’m so very, very sorry.

CORRYN: The reason you suspended him? I’d really like to know. I’ve been wondering. Your note was vague. The voicemail was cryptic. I’ve been up for about 72 hours. I can’t sleep. I can’t sleep because I’ve been playing this conversation out over and over again in my mind, wondering how it will go. You were more vocal in these little fantasies. You contributed. You explained . . . I don’t know why you . . . did this to him. I don’t know what happened.

HEATHER: . . .

CORRYN: He looked devastated. When he handed me the note. He was shaking. He—

HEATHER: God! . . . oh god . . . I didn’t think you’d keep the appointment. It never occurred to me that you would keep the appointment.

CORRYN: He’s my son.

HEATHER: I didn’t think you’d still want to talk about—

CORRYN: About my son?

HEATHER: That it might be painful to. . . To talk about him so soon after his death. I’m really very sorry—

CORRYN: You’ve said so.

HEATHER: . . .

CORRYN: Thank you. . . . I’m sorry I missed open house. Gidion’s father is dead. I’m a single mother. Getting a babysitter on a school night is like squeezing milk from stones. Do you have children?

HEATHER: No.

CORRYN: How long have you been teaching?

HEATHER: Two years. Maybe we should reschedule. Find a time when the principal can join us. You should be with family now.

CORRYN: I’m exactly where I should be. You sent a note home with my son. You suspended him. Five days.

HEATHER: Yes. You should take some time to grieve before . . . this. We all should take some time—

CORRYN: Who’s Jake?

HEATHER: He’s a boy in the sixth grade.

CORRYN: Is he one of the children that Gidion made angry? On Friday? The day he died? . . . There’s a Jake on facebook who left comments on Gidion’s facebook page over the weekend saying “You’re a faggot” and “You’re a lying faggot.” After Gidion was dead, in fact, so-- . . . untimely.

HEATHER: He couldn’t have known Gidion was dead. The kids didn’t know until this morning. Jake’s been troubled lately. It’s out of character if he did that. . . Can I get you something to drink? The faculty lounge is just down the hall.

CORRYN: No thank you. I’m fine . . . Do you want to know what I do? You won’t see this coming . . . I’m a teacher.

HEATHER: What do you teach?

CORRYN: Literature. At Northwestern. In the graduate program. . . Jesus Christ. What the hell happened? I thought this would be largely a transactional exchange. I ask, you give. Even-- well, correct me if I’m wrong-- you have two years of professional experience, but, even if the circumstances around my son’s suspension weren’t . . . charged, let’s say, by the fact of his death, I would expect the reasons for his suspension to have at least come up

HEATHER: . . . . (Heather pulls out a key ring. She finds a key and unlocks a drawer. She takes out a folder covered in comic book superheroes and sets it on her desk.)

CORRYN: What is it?

HEATHER: What got Gidion suspended. She offers the folder to Corryn. Corryn doesn’t take it.

HEATHER: It’s something Gidion wrote . . . A story.

CORRYN: You have got to be kidding me. You suspended my son over a story?

HEATHER: It’s disturbing.

CORRYN: I have a feeling there are miles between what you and I find disturbing.

HEATHER: Read it and we’ll see. (Heather starts to leave.)

CORRYN: Don’t. . . I want you to explain things to me. I don’t want to sit alone here. I didn’t come here for that. I don’t want to figure things out. I want them explained! I want you to read it to me.

HEATHER: It’s not the way you want your son remembered.

CORRYN: You don’t know what I want.

HEATHER: Trust me.

CORRYN: Read it.

HEATHER: I’m sorry. I honestly can’t read that again. And certainly not out loud.

CORRYN: As bad as all that?

HEATHER: Yes.

CORRYN: As bad as facing what you did?

HEATHER: That’s not fair. . . That is not fair. I know you’re angry with me. I can’t imagine how angry you must be with me. And you want to punish me. . . I don’t know what went on in your house. . . Once he left this classroom my responsibility ended. This-- this is not a product of my classroom. He learned this (gesturing to the folder) in your house.

CORRYN: I can’t read it. I need you to do this. . . Because it’s in his handwriting . . . And I can’t read his handwriting without seeing his suicide note in my hands. Please? (Corryn holds the folder out to Heather. Heather takes it and opens it.)

HEATHER: It began during a war, as things do. We all formed tribes and began killing the teachers. I cut Mr. Shawn apart myself with a hunting knife my grandfather gave me the last time he took me hunting. We needed his entrails for our weavers and our poets. I think Mr. Shawn was grateful. A group of sixth graders had caught him in the cafeteria earlier, by the vending machines, and cut out his eyes, flayed him. He was spitting blood up because of something they’d broken in him and I think he loved me for cutting him open. I took a broomstick out of the janitor’s closet and nailed one end of his intestines to it and then rolled the rest of his intestines out of his stomach, twisting them around the broomstick-- they stretched more than 25 feet when I was done. Mr. Shawn had told me that intestines were that long in science class a month ago, but I didn’t believe him until we started collecting them for the weavers and the poets. He was lucky. Most kids wouldn’t have killed him first. I put the thick roll of Mr. Shawn’s intestines over my shoulder and started walking to the gym, which is the room where we kept the weavers.

Around the corner in the hall outside the nurse’s office, the nurse, Carole from the office and the fat principal were hanging from the walls by nails punched through their wrists and ankles and knees and shoulders. Their bodies were just gaping, empty bags. No entrails to salvage.

The broomstick was heavy and I had enough guts, so I made my way to the gym, where the weavers worked. Since the weavers started working, the gym stopped smelling like a gym and started smelling like a butchers’ shop and a toilet. All those entrails being braided and woven. You wondered how the weavers could stand it, but when they changed into weavers, maybe they lost their sense of smell. We had been in home period, in Ms. Clark’s room when the first weaver was chosen. We don’t know by who, some think there are aliens on earth like the body snatchers and some think God did it. But whoever did it, in the middle of class this girl suddenly screamed and her eyes turned into balls of blue glass and her arms stretched out like poles and her hands grew new fingers and grew big. This was happening in other classes, but we didn’t know that. And she started asking for entrails. Not to eat, but to make things with. So we put her and the others in the gym and they started making looms out of the janitor’s supplies. And we started killing for them. We had to give the weavers what they needed. Some of us sort of hung back to see what the weavers were making from the teachers’ entrails before we started killing and gutting. But when the first cloak was made and the first poet climbed the hill, I knew I had to kill however many teachers I needed to so that I could have one.

I gave a weaver my last pile of entrails and she tied them onto the ends of the other entrails I had brought her and started weaving. The cloth the weavers make from the teachers’ entrails is like nothing you’ve ever seen. It’s like a river and a taste of salt. It’s like an ocean with fish moving through black water. When the weaver finished my gut-cloak she put it around my shoulders and I felt the pull. And I walked out of the building to the soccer field where the tribes who kept the first through third grade kids as slaves had made them build a mountain. And I climbed the mountain and joined the poets there. We watch the war and we write about the great deeds done or the horrors done. And that is how God remembers you-- the way we write you. And no other way. (Heather shuts the folder and puts it in front of Corryn on a desk.)

He was passing it around. To the other students. It’s my responsibility to-- . . . I’m sure you understand. I can’t imagine what it-- . . . . I don’t think, at heart, that he-- . . . . Well. . . . I know this isn’t all there was to him.

CORRYN: This is magnificent! This is wonderful writing. Strong. Fearless. Fierce. Brave. Cruel. Remarkable. This is a wonderful story. About art and its purpose. About man and divine judgement. Oh god. God, it’s beautiful.

HEATHER: I disagree.

CORRYN: Why?

HEATHER: I have a responsibility to my students. To protect them.

CORRYN: From what?

HEATHER: From things like this. Damaging things.

CORRYN: Poetry?

HEATHER: Hate-filled, poisonous attacks. He passed this around to a room full of children . . .

CORRYN: Oh, God. I put him here. Into a pit. Full of the unenlightened. Into the hands of the conventional. Who the hell are you to tell my son what not to write about?

HEATHER: His teacher.

CORRYN: What were you teaching him? How to disappear into some mold you wanted to pour him into?

HEATHER: This decision wasn’t about him. It was about the other children. Their well-being. This is a fifth-grade classroom.

CORRYN: This is a small box. Full of smaller boxes. One of which you tried to keep my son in. And when he couldn’t fit inside it, he shot himself in the head. Over not fitting in a box cut to your dimensions. I blame you for this. He wanted to be a writer. He was going to be one.

He didn’t die because of what he wrote, or because you suspended him. He died because he couldn’t face telling me about it-- . . . god damn it . . . He could have told me this. God. I’m not a good mother. . . There are so many things that could go wrong-- so many ways I could ruin things-- but this? This? This was my good mother moment. What happened? He could have told me this. I would have told him: “This is magnificent. You are a poet. You’re perfect. They’re wrong.” My good mother moment. The one time-- the one time I would have been the mother he needed and not just the one he got.

HEATHER: . . .

CORRYN: I don’t know what I did to make him think he couldn’t tell me. . . This. (Motioning to the folder) It’s based on a story I used to tell him when he was little. About the Great Poet's war. Once upon a time in the green hills of ancient Gaul, two warring clans met on the battlefield of Ballycrief. Each clan had a master poet and a poet's apprentice. And they sent their poets to the top of the hill. So they could see" Because men aren't afraid of dying, but they are afraid of not being remembered.

HEATHER: . . .

CORRYN: Sign this. (taking the suspension notice out of her purse) You sent this home with him. I’m supposed to meet with you and get it signed. Unless it is no longer important . . . I was grading papers when he gave it to me. I knew it was something big. He couldn’t look at me. He was shaking. I saw what it was and told him everything would be all right. Asked him if he wanted to talk about it. He shook his head no. He went up to his room. I didn’t hear him go into the garage. I called him to come down for dinner. He didn’t answer so I started up the stairs to go get him and I heard the gun shot. I thought he was upstairs still and I couldn’t imagine-- I called out again and told him to stay in his room and then I went into the garage. He had taken garbage bags-- the ones for gathering dead leaves, and taped them in a large rectangle on the floor. Like a tarp. But, he didn’t understand. Because he put the gun under his chin. So, nothing. . . nothing landed on the tarp. So. He didn’t leave behind the tidy mess he thought he would.

HEATHER: . . .

CORRYN: He left a note. (takes another slip of paper from her purse)

HEATHER: . . .

CORRYN: “I’ve gone to stand with the poets.”

HEATHER: . . . That’s beautiful.

CORRYN: When someone tells you what her child’s suicide note says, you aren’t supposed to say “that’s beautiful.” It really isn’t appropriate. But you said it. Because you felt it . . . Thank you.
```

---

## IC-0157: girl.

- Title: girl.
- Author (byline): Megan Mostyn-Brown
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Jan 2008
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MONDAY HANNAH, HANNAH
- Teaser before the introduction: Yes
- Spoken words (computed): 1767
- Already set (do not supply): none

### Source block (context only)

```text
Author: Megan Mostyn-Brown
ISBN: 978-0573651045
Publisher: Samuel French, Inc.
Date (Month/Year): Jan 2008
Cut from the section titled: Things You Can’t Tell Just by Looking at Her
```

### Introduction (context only: never use it for content warnings)

```text
Hannah’s week starts with a sentence she can’t quite wrap her head around: Lizzie’s gone. And while everyone expects her to cry – to break down -- she’s stuck thinking about morgue tiles and why Lizzie’s life has been reduced to a newspaper statistic. Hannah’s story reveals the kind of family people don’t put in sympathy cards: the fights, the missed moments, the quiet way a daughter can disappear while parents chase the memory of one who’s already gone. There are so many things you can’t tell just by looking at her.

From girl. by Megan Mostyn-Brown
```

### Performance text (classify this)

```text
MONDAY HANNAH: My sister Lizzie died today. Wow, what a weird thing to say, you know? Because it’s true. I mean, it sounds like the beginning of a poem that your teacher would read in English class or somethin’ – “My sister Lizzie died today . . . dadum . . . dadum . . . dadum.” Yeah. It’s not like we didn’t expect it . . . she’s been missing for like, months. And even before that she was always in and out. Runnin’ away n’ shit. So mom and I were always like, “Lizzie’s gone”. . . Not like we said it to each other on a daily basis or even said it at all. But it was always just there hangin’ in the air: Lizzie’s gone, dot, dot, dot.

HANNAH: Lizzie’s gone, dot, dot, dot. Maybe that’s what’s different, no ellipses. It’s, ahhh, what do ya call it? Yeah, a declarative sentence, I think. Anyway, not it’s the kind of sentence with a period at the end of it. “Lizzie’s gone” period. It’s funny, you know? I didn’t cry at all today. And I felt really bad because, well, you’re supposed to cry when people die. But, honest to god, all I could think about all day is that if I were going to jump off a bridge, like her, I wouldn’t do it in the middle of July. And that’s f***ed up right? To be thinking about that instead of being sad. I would do it in November, or the beginning of March, on one of those days when you wake up with a chill because it never really stops drizzling. And the bridge would be just a little bit slippery. And the water really cold. And people would have to wonder, “Did she do it on purpose or was the hand rail too slick?”

But today was the kind of day where it’s like ninety-eight degrees before noon - not a cloud in the sky, and all anyone can manage to do is keep from sticking to the furniture. (Pause)

My mom hasn’t said anything all day. I take that back. She hasn’t said anything to me. She said thank you to the police officer who came to the house. And she mumbled Lizzie’s name to the receptionist at the morgue. I didn’t go in. I sat in a plastic chair in the hallway and counted the number of tiles on the floor from my feet to the front desk. There are seventy-two. They didn’t have any pamphlets to read, which was really surprising because like every place in the hospital has at least one pamphlet. But, what would the morgue have pamphlets about?

Anyway, I’m glad I didn’t go in with mom, you know, to look at the body and stuff. Because when people drown they get all blue and bloated; not like I’ve ever seen it, but that’s what happens in movies. I’d like to think of Lizzie like that picture, the one of Ophelia, I don’t remember who painted it, but it’s Ophelia floating on her back in this pond and she’s wearing a really beautiful dress with a crown of flowers on her head. That’s how I’d like to think of her. (Pause)

There’s going to be a funeral. And who are we gonna invite? Because mom and I don’t know who Lizzie’s friends are. She stopped telling us stuff like that years ago. Mom pressed her for it. And they would fight. You know, screaming, yelling, breaking things etc . . . Pretty soon she just stopped coming home at all. Now that she’s gone for good, it’s like we can erase all the bad shit - Wow. It sounds like I’m glad she’s dead. (Beat)

Um, I guess it’ll just be me and mom at the funeral. Jesus . . . maybe her friends, wherever or whomever they are, are having a little funeral for her somewhere else and one of them’s gonna get up to say a few words about her. I’d like to think that’s true. I mean, someone somewhere HAS to have a few words to say about her . . .

TUESDAY I’ve been thinking, like a lot. It sucks cuz all I can think about is Lizzie. There was this article in the paper today about “Lost Youth” and they mentioned her, saying how sad it was that her life ended so soon and what a statement it made on “the demise of adolescence in our society”. Then they gave all these statistics about suicide and that’s it. They didn’t even talk to us. Or list any details about her life. They just mentioned her name, some facts about her death, and then placed her in a section of a pie chart. Jesus, they left out everything. It’s like they felt sorry for her without even knowing what really -- I mean she was a f***ing drug addict. (Beat)

Um . . . this one night right before she ran away for good, this car pulls up in front of the house and whoever’s in the driver’s seat sorta just throws Lizzie onto the lawn. And she’s layin’ with her face in the grass and I don’t know if she’s . . . . So, I go outside to see what’s goin’ on, the car’s driven away by then, and all the shit from her purse is all over the lawn, and when I roll her over she’s laughing, and her eyes, well, I can only see the white parts. And she says my name in this really gross way. And I’m so afraid mom’s gonna wake up or that the neighbors will see. So I try to get her to be quiet so I can get her into the house and like splash water on her face or somethin’, because you know that’s supposed to sober people up, I guess.

And I pinch my arm really hard so I won’t . . . See, cuz all of this . . . . It’s just a lot when you’re fifteen. See I’ve started – well . . . (Beat) For a while now I’ve been (Beat) hurting myself. (Pause)

WEDNESDAY Um . . so, so last night, the house is like suffocating quiet. So I use a (Beat) straight razor. I usually don’t. I prefer the pink Bic kind . . . does the job, less damage. So I use a straight razor and after it’s like fireworks and deep breaths and the good kind of weak knees all at once. Um . . . until I notice, well . . . (As the next passage goes on Hannah gets really into it, like she’s there) there’s no point in being graphic. Suffice to say there’s a lot of blood and it won’t stop no matter how much pressure I put on it and I start to get worried cuz I feel sort of faint and I don’t know what to do to make it stop. And I don’t want to call my mom, so I walk to the emergency room, which is good, because they stitch me up. Ten stitches with the kind of thread that will dissolve when the wound is all healed. But since I’m a minor, and they know that my arm isn’t the accident I play it off to be, they call Mom and make me sit in this office with a nurse who asks me if I’ve ever done anything like this before. Which is the stupidest question, because she can see the marks all over my arm. And I answer yes in this voice that doesn’t sound like me at all and I can’t look her in the eye, so I stare at the floor which has the exact same tiling as the morgue. She asks me how many years this has been going on and I say two. I lift up the salmon pink hospital gown and Jesus . . . . (makes a vague gesture at her legs) there’s a lot. Like words carved . . . “Hate” “Ugly.”

So I’m like . . . can I go home now? I’m a good person. I get straight A’s, swear to God. I promise I won’t do it again. I just wanna go home like really badly. But I can’t leave until my mom gets here. And I think I’m gonna throw up or break into a million little pieces . . . so I stare at my toes cuz maybe, just maybe, if I make myself small enough, all of this will go away.

THURSDAY I get up this morning and Mom’s not a work. She’s at home making plans for the funeral. All the knives were gone and my razor, you know, to shave my legs with, was missing. At dinner this evening we sat in complete silence. I don’t know why we even go through the motions. And she served soup and a salad, you know, things you don’t have to cut. And she acts like I didn’t notice her peeking at my arms, I mean, it’s not as though she’s going to see anything anyway. I mean I haven’t stopped. I can’t. It’s the only thing in this whole mess that’s mine. So I’ve just moved my activities to a new region. Under here (Gestures at her breasts but keeps looking straight out) And the only thing that keeps me sane is this stupid fantasy where I clear everything off the table with one swoop of my arm, you know, like people do in movies when someone’s like ROYALLY dicked them over and they want to make a point. Anyway, all the dishes go crashing to the floor and [Mom] just like sits there because she’s so in shock that I did this horrible violent thing. Anyway, I take off all my clothes, strip down to my underwear so she can see all the marks and scars and I tell her where each one is from.

I’d say . . . (the following passage should start out slow and then pick up with dizzying momentum) This one right here, this I did the night you yelled at me when Lizzie broke curfew for like the eighty-seventh time. And this one is from when you missed my school play because you were too tired from roaming the city all night looking for her. And this . . . THIS . . . I did after I cleaned the house, scrubbed the floors, and EVERYTHING and you didn’t even notice because SHE had stolen the stereo. This one I did after we picked her up from jail. These along my arm are the last six months she was missing. This one is from when you left me standing in front of the cashier with a conveyer belt full of groceries and a line of angry customers because you thought you saw her in the parking lot. And while all of the NORMAL families loaded brown bags into their station wagons to have REAL FAMILY DINNRS, I was the MOTHER and held your head in my lap while you cried because it wasn’t her. This long one that curves from my wrist is because you haven’t spoken to me since Monday when she died. I am HERE. I STILL EXIST! (Long pause. She should be out of breath, dizzy. She takes a beat, composes herself and then. . . nothing)
```

---

## IC-0158: Girl in Pieces

- Title: Girl in Pieces
- Author (byline): Kathleen Glasgow
- Work: Not specified
- Publisher: Delacorte Press
- Publication date as stated: Aug 2016
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARLIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1319
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kathleen Glasgow
ISBN: 978-1101934715
Publisher: Delacorte Press
Date (Month/Year): Aug 2016
```

### Introduction (context only: never use it for content warnings)

```text
Studies show that 75% of girls with low self-esteem reported engaging in negative activities like cutting, smoking, drinking and drugs. Charlie Davis is one of those girls. Nearly broken by a suicide attempt and a rush of personal losses, she finds solace in the broken shards of a mason jar.

First came the death of her father, followed by her mother’s abuse and abandonment. Charlie turns to her only friend, Ellis, her Beautiful Girl. But Ellis is battling her own demons and is left stuck in limbo -- cutting deeply enough to cause significant blood loss but not enough to die.

Bandaged and silent, Charlie ends up in a psych unit for self-harmers, trying desperately to put herself back together. Girl in Pieces, by Kathleen Glasgow.
```

### Performance text (classify this)

```text
CHARLIE: (Pg 81-83) A girl is born.
Her father loves her. Her mother loves her father.
Her father is sad.
Her father drinks and smokes, rocks and cries.
Into the river, he goes.
The mother becomes a fist.
The girl is alone.
No one likes the girl.
She tries.
But her mouth is mush
Stupid girl. Angry girl.
Girl finds knife. Girl makes herself small, small, smaller. World gone.

Girl meets girl. Beautiful Girl! They watch planets move on the ceiling.
Beautiful Girl meets Wolf Boy. He fills her up, but makes her small.
Girl stays with Beautiful Girl, but wolf boy leaves drugs.
Beautiful Parents are angry. Beautiful Girl lies and blames Girl for drugs.
Girl on street. Girl goes home.

Beautiful Girl texts and texts. Something wrong Hurts
Girl slips headphones on. Girl slides phone under pillow.
Beautiful Girl bleeds too much.
Girl gets messed up too, too messed up, broken heart, guilt.
World gone.

(Intro by 4N6 Fanatics Staff)

CHARLIE: (Pg 3) Like a baby harp seal, I’m all white. My forearms are thickly bandaged, heavy as clubs. My thighs are wrapped tightly, too; white gauze peeks out from the shorts Nurse Ava pulled from the lost and found box behind the nurses’ station. Like an orphan, I came here with no clothes. Like an orphan, I was wrapped in a bedsheet and left on the lawn of Regions Hospital in the freezing sleet and snow, blood seeping through the flowered sheet. The security guard who found me was bathed in menthol cigarettes and the flat stink of machine coffee. He said, “Holy Mother of God, girl, what’s been done to you?” My mother didn’t come to claim me. But I remember the stars that night. They were like salt against the sky, like someone spilled the shaker against very dark cloth. That mattered to me, their accidental beauty. The last thing I thought I might see before I died on the cold, wet grass.

(beat)

(Pg 4) The girls here, they try to get me to talk. I hear their stories every day in Group, at lunch, in Crafts, at breakfast, at dinner. . .These words that spill from them, black memories, they can’t stop. Their stories are eating them alive, turning them inside out. They cannot stop talking. I cut all my words out. My heart was too full of them.

(Pg 5) I room with Louisa. Louisa is older and her hair is like a red and gold noisy ocean down her back. There’s so much of it, she can’t even keep it in with braid or buns or scrunchies. Her hair smells like strawberries; she smells better than any girl I’ve ever known.

My first night here, when she lifted her blouse to change for bed, I saw them, all of them, and I sucked my breath in hard. She said, “Don’t be scared, little one.” I wasn’t scared. I just never seen a girl with skin like mine. (beat)

(Pg 9) Sometimes I can’t breathe in this Goddamn place; my chest feels like sand. I don’t understand what’s happening. I was too cold and too long outside. I start to panic, shake, choke, and Louisa, she comes up very close to me in our room. She cups my cheek and even that makes me flinch. She says, “Little one, you’re with your people.” (long Pause as Charlie is lost in thought)

(Pg 15) We’re never in darkness. Every room has lights on in the walls that ping on at 4 p.m. and ping off at six a.m. How long have I been here? I’m waking from something. From somewhere. A dark place.

(Pg 20) It isn’t true that I want to be like the turtle and be alone. What’s true is that I want Ellis back, but she can never come back, ever, ever. Not the way she was, anyway. When I think about Ellis, I feel sadness, and while I say sadness, what I really mean is a black hole inside me filled with nails and rocks and broken glass and the words I don’t have anymore.

(beat)

(Pg 42) The first time I ever cut myself, the best part was after: swabbing the wound with a cotton ball, carefully drying it, inspecting it, this way and that, cradling my arm protectively against my stomach. There, there.

I cut because I can’t deal. It’s as simple as that. The world becomes an ocean, the ocean washes over me, the sound of the waves is deafening, the water drowns my heart, my panic becomes as large as planets. I need release, I need to hurt myself more than the world can hurt me, and then I can comfort myself. There, there.

(Pg 44) It hurts to make a river. The pain is sharp and bleary all at once; curtains part and shut over your eyes; bull breath from your nostrils. It f**** hurts, hurts, hurts. But when the blood comes, everything is warmer and calmer.

(Pg 90) I wondered why [Ellis] picked me to be her friend: me with my haphazardly cut red-and-black hair, my holey cardigans and ripped jeans.

(Pg 69) I know who I am. I mean, I don’t know know, because I’m only 17, but I know who I am when I’m with people, or when they're looking at me. [I’m] that one, the kid who never gets anything right, and sits alone in the cafeteria, and draws all the time, and sometimes she gets mad and punches, because what else is there? So when [someone] says, “Who keeps your secrets?” I think, “Nobody.” Nobody until Ellis.

(Pg 74) [Sometimes] I say Ellis killed herself, but she did not die, die. She isn’t in the ground. There were drugs, wolf boy, and she slid very far from me. And when the wolf was done, he left her gaunt, my Ellis, my plump and glowing friend. And then I guess she tried to be like me. She tried to drain herself, make herself smaller, only cutting wasn’t her thing. I imagine her room soaked in blood, rivers of it, her parents fighting upstream to get to her. But there was too much, do you understand? A person can only lose so much blood, you can only starve the brain of oxygen for so long, or you suffer an anoxic brain injury after hemorrhagic shock, which emptied out my friend and left only her body.

(Pg 342) The text messages flicker in front of my eyes. Smthing hrts. U never sd hurt like this. 2 much.

(Pg 40 – 41) The hands on the wall clock tell me it’s time to get my bandages off. It’s one of the day nurses, Vinnie, who does it, his big hands chapped and methodical. He pauses before he begins unpeeling the pads on my arms. “You want someone here?” I shake my head, No. “Yeah, that’s right. You a tough girl, Davis.”

(Pg 41-42) Carefully he unwinds the gauze from each arm. They make a wet soft, thwack as he tosses them in the metal trash bin. I stare at the ceiling lights so hard dark clouds form over my eyes. There’s the sound of trickling water. Vinnie is washing his hands. I lift my arms up. They’re pale and puckered from being wrapped up for so long. Turning them over, I look at the red ropy scars rivering from my wrists to my elbows. I touch them gingerly; there, there. Underneath these new scars, I can see the old ones. My scars are like a dam or something.

(Pg 45-46) My eyes are fierce with water, and I want Ellis, the Ellis who would dab my cuts and steal wine from her dad so we could cry together. Because when you’re hurt, and someone loves you, they’re supposed to help you, right? When you’re hurt and someone loves you, they kiss you tenderly, and they hold the bottle to your mouth, they stroke your hair with their fingers, right? I’m in a place filled with girls who are filled with longing and I want none of them. I want the one I can’t have, the one who is never coming back.
```

---

## IC-0159: The Girls Who Went Away

- Title: The Girls Who Went Away
- Author (byline): Ann Fessler
- Work: Not specified
- Publisher: Penguin Books
- Publication date as stated: May 2006
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ANNIE, MOTHER, DOCTOR, MOM, FESSLER, NANCY, DIANE, CLAUDIA, GLORY, MARGARET, PRINCIPAL, YVONNE, DAD, MARY, POLLIE, LYNNE, DEBORAH, KAREN, CASEWORKER
- Teaser before the introduction: Yes
- Spoken words (computed): 2018
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ann Fessler
ISBN: 978-1594200946
Publisher: Penguin Books
Date (Month/Year): May 2006
```

### Introduction (context only: never use it for content warnings)

```text
Margaret Atwood wrote in The Handmaid’s Tale: “But who can remember pain, once it’s over? All that remains of it is a shadow, not in the mind even, in the flesh. Pain marks you, but too deep to see. Out of sight, out of mind.”

The Girls Who Went Away by Ann Fessler
```

### Performance text (classify this)

```text
ANNIE: (Pg 36-37) Mother, we didn’t go to the circus last night. We went to a doctor.

MOTHER: Oh my God, don’t tell me you’re pregnant!

ANNIE: Within a few days, she took me to her doctor . . .

DOCTOR: There’s a place where they send girls like her in Kansas City. It’s pretty expensive. If you have any money put aside for her, use it for this. She doesn’t deserve to have it anyway.

MOM: (to Annie) . . . and you’re going to stay there until you have the baby. Then you’re going to give your baby up for adoption and you’re going to come home and forget that this ever happened. Someday you’ll thank me.

ANNIE: That was when the shame began. At sixteen, I had to do everything that my mother said. That was it. There were no options. It was all decided for me.

FESSLER: (Pg 20-21) Just about everyone who lived through [the 1950s-1960s] has a memory of a girl from their high school, college, or neighborhood who disappeared. The girls who went away were told by family members, social-service agencies, and clergy that relinquishing their child for adoption was the only acceptable option. It would preserve their reputation and save both mother and child from a lifetime of shame. They must surrender their child, keep their secret, move on, and forget. (beat) Between the end of World War II in 1945 and the passage of Roe v. Wade in 1973, one and a half million babies were relinquished for nonfamily adoptions.

FESSLER: (Pg 19) Despite the increase in the number of young people having sex in the 1950s and 1960s, access to birth control and sex education lagged far behind. Fearing that sex education would promote or encourage sexual relations, parents and schools thought it best to leave young people uninformed.

NANCY: (Pg 55) . . . (to mother) How do they get rid of the mark when they take the baby out?” She stood there, three feet from me, with a look of horror on her face and said.

MOM: My God, Nancy, that baby comes out the same way it went in.

NANCY: I was sixteen and pregnant and I did not know how babies were born. It’s pathetic, but it’s true. I mean, it’s borderline child abuse not to share this kind of information. How can anyone think that we will just absorb it naturally, or that it’s our responsibility as children to figure it out?

FESSLER: (Pg 39) By 1973 the percentage of unmarried girls who had gone “all the way” before they were 20 years old had risen to 68%. (Pg 20) The result was an explosion in premarital pregnancy and in the numbers of babies surrendered for adoption.

DIANE: (Pg 43) Girls are only two types, a Madonna or a whore, and not the singer Madonna, the virgin Madonna. You were good or bad. You were very bad if you had sex. So, you couldn’t really plan to have sex; it had to just happen.

CLAUDIA: (Pg 64) I don’t remember any dialogue around having choices. (mimicking those in charge) You are gonna do the only thing that is right. You’re gonna give that baby to good people, decent people, people who can take care of it because you are so bad and so flawed for just having this happen. (pause as a memory surfaces) (Pg 67) I named my baby Raina Elizabeth [and] I did get to hold her for three days. She had a little tiny heart-shaped mouth, big dark eyes, beautiful skin, and tons and tons of black hair. (pause) And then on the third day my parents came. It was the beginning of it being invisible. It was never, ever, brought up again. It was never talked about—not once, not ever.

GLORY: (Pg 72) I called my folks from college to tell them I was pregnant and my dad said . . . “Don’t come home.” At the time, my dad was a sheriff. He would be up for reelection and he did not want a daughter like me around. It was fine while I was class valedictorian and the shining star, but not while I was pregnant, no.

FESSLER: (Pg 75) In one of the strictest forms of banishment, high schools and most colleges required a pregnant girl to withdraw immediately. It was not until Title IX of the Education Amendments Act of 1972 that federally funded high schools and colleges, by law, could not expel a pregnant girl or a teenage mother.

MARGARET: I got called down to the office and the principal said . . .

PRINCIPAL: There’s a lot of gossip about you being pregnant. We figure that you’re about three to four months and you may not return to school until you have a doctor’s note saying that you’re not pregnant.

MARGARET: The gym teacher helped me clean out my locker and drove me home, and the school called my mother. I had been this girl who didn’t smoke, didn’t drink, didn’t do anything wrong. Everybody’s parents wanted their daughters to be with me. Now, when I walked down the street, parents made their daughters cross the street.

FESSLER: (Pg 77) Meanwhile, the young men who had fathered these children largely escaped social condemnation. Their role in the pregnancy wasn’t publicly visible, so they were not expelled from school, and were generally not treated with scorn, and not considered a disgrace to their families. Most parents supported the double standard by holding their daughters, but not their sons, accountable. (Pg 78) The standards of the day dictated that a young woman was responsible for stopping the advances of a young man. She was ultimately responsible both for his behavior and it was “her own fault” if she got pregnant.

YVONNE: (Pg 89) My dad said . . .

DAD: I’m not going to spend one damn cent on that little bastard.

YVONNE: (Pg 92) What’s worse -- for a child to grow up being adopted or being labeled illegitimate? What’s going to be harder for him to live with? (Pg 98) From everything I see, I think the general public believes that mothers who give their babies away are glad to be rid of them, they’re glad to be rid of the problem. They think, “She didn’t care about that kid. She just wanted him out of the way so that she could go on having a good time.” I’ve heard people say that. It’s like if you have a child and you’re not married, you don’t have those same maternal feelings that other mothers have? I have never, ever met a mother who felt that way. Never.

MARY: (Pg 102) I told my mother and she started screaming at me. It was horrific. I was told to leave the house and not return. I was not allowed to make a phone call -- not allowed to take any clothes, pack a suitcase, nothing. I don’t remember where I went to use a phone, but I called the doctor I had babysat for and I went to their house. He pleaded with my mother and father to let me come home. But they refused to take me back.

POLLIE: (Pg 103) My mother was horrified. She called me a slut, a whore. And it seemed like just a day or so after that, my mother came in and had me go to the bathroom, disrobe, and get into the bathtub, which was very humiliating in itself. She administered a douche, which was very painful. I didn’t know anything about a douche. I found out later that what she had used was Lysol from the brown bottle. . .

LYNNE: (Pg 132) We drove to the maternity home on back roads. I walked in and there were all of these strange pregnant people and these nuns. And some of the nuns were harsh. Harsh. I had committed a sin. It’s not like today when you go through therapy, for God’s sakes. No. There was no therapy.

DEBORAH: (Pg 133) I found the letters I wrote [to my parents] while I was away. They are hard to read because I was still so naïve. I was trying to protect them, trying to give them this picture of a normal life with my continual, Shirley Temple kind of “I’m having a great day, the baby is kicking, everything is wonderful,” like it was a normal thing. I mean, I was living in an institution, for Christ’s sake. They locked us in at night. It wasn’t normal life.

LYNNE: (Pg 143) I remember the nun at St. Andre’s telling me that it was God’s will. We were fulfilling the needs of women who couldn’t have children. God chose us to bear these children for these women who couldn’t have any. I was so susceptible to this thinking: I must accept God’s will. I could have more children, you see, so what’s one child to be given away? I would see this child in heaven.

KAREN: (Pg 149) Then they would say things about the baby. It’s always “the baby,” never “your baby.”

CASEWORKER: This experience will end. You will forget that you went through this. You will get over it. You know what you did was wrong? You know that you are really not worthy of keeping your own child? That child needs a mother and a father, and the things that they can give that child. You can’t provide anything that child needs.

KAREN: (Pg 152-153) We were not told any of our rights. We were not told we had the right to keep our own baby. The social workers should have been required to tell us what was available to us, so we could make an informed decision. We were never told anything except adoption—it was the only option offered to us. We weren’t told that we could get child support from the fathers. We weren’t told that we could apply for welfare or Aid to Families with Dependent Children, which was available then. There was a lack of informed consent. All of our rights were abused. Ignored and abused. The rights that people take for granted today, we were denied. We didn’t know because we were young, and we trusted our parents, and we trusted authority. They would tell us what was best. So, we figured if that’s what was best, then that was what we needed to do. They’ve injured and damaged millions of people. You’re just so beaten down by being in that place and being told, “You can’t, you can’t, you can’t.” And “You aren’t a mother, you don’t deserve to be a mother.” It was just overwhelming . . .

The whole point was to keep us scared and feeling guilt all the time. And compliant, you know? “You do this and you can go home.” It makes me very, very angry today to think about that manipulation. To me, it was evil. Nobody ever said, “What do you want, Karen? Do you want to keep your baby?” (pause to regain composure, then with anger)

CASEWORKER: No, no, no. Don’t even think of that because it’s not your child. It’s these people’s child over here. It’s been promised to them. You should be happy you’re giving your child to someone so wonderful who has so much to offer that child. You should be grateful we’re solving your problem. You made this mistake. You caused this problem for everyone.

KAREN: (Pg 154) There was such emotional and mental damage done. We were not criminals. We were mothers. The difference was I was not an authenticated mother. I was an illegal mother. I was a denied mother. And I had to come home and live my life as if I was an unwilling accomplice to the kidnapping of my own child. You have to live with the trauma of losing your child and then you have to live with the trauma of knowing you didn’t stop it. How do you do that?

CONCLUSION We’ve come a long way from 1950 -- from the lack of education; the stigma of being an unwed mother; and a woman’s right to choose. But the pendulum of values began shifting again in 2022. *Since the Supreme Court overturned Roe v. Wade and the federal right to abortion in 2022, there has been a nationwide expansion of maternity homes – many of them faith-based. As abortion restrictions increase, anti-abortion advocates want to open more of these transitional housing facilities, which often have long waitlists. As of 2024, there are more than 450 maternity homes in the U.S. You see . . . ““Nothing changes instantaneously: in a gradually heating bathtub you'd be boiled to death before you knew it.” -- Margaret Atwood, the Handmaid’s Tale
```

---

## IC-0160: Grace and Glorie

- Title: Grace and Glorie
- Author (byline): Tom Ziegler
- Work: Not specified
- Publisher: Doubleday
- Publication date as stated: Feb 1997
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: GRACE, GLORIA
- Teaser before the introduction: Yes
- Spoken words (computed): 2053
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tom Ziegler
ISBN: 978-1568652726
Publisher: Doubleday
Date (Month/Year): Feb 1997
```

### Introduction (context only: never use it for content warnings)

```text
Two women -- Two lives that could not be more different. One is 90 years old. She is weathered by loss, sustained by faith, and preparing for the final chapter of her life. The other built a life of success in the city—educated, accomplished, and certain she understood how the world worked… until tragedy shattered everything she believed.

In a small farmhouse, surrounded by pain, memory, anger, and hope, two strangers confront questions that follow every life: Why do we suffer? What do we hold onto when everything is gone? And what does it mean to let go?

Grace and Glorie by Tom Ziegler
```

### Performance text (classify this)

```text
GRACE: (Pg 50) (singing softly to herself*) “He will give me grace and glory and go with me all the way.”

GLORIA: (Pg 5-8) Hi. I’m Gloria Whitmore (waiting for some recognition, getting none) You probably don’t remember, but we met briefly at the hospital last week.

GRACE: I remember. Wha’cha think, I’m senile?

GLORIA: No, of course not. Is there anyone here with you? Is your grandson here?

GRACE: Roy? He’ll be back this evenin’. You need to talk to Roy?

GLORIA: You should have someone here with you – to care for you.

GRACE: Roy takes care of me. Cuts my fire wood, fetches me things from the IGA. I gotta pay him. Roy don’t do nothin’ for free.

GLORIA: I’m not here to talk to Roy, Mrs. Stiles, I’m here to see you. When you left the hospital this morning you forgot your medication. Here. (taking a package from her bag)

GRACE: You must think I’m a mighty forgetful ol’ lady! Well, I’m not! Told the doctor I didn’t want none o’ that stuff. You people and your drugs. I’ve been doin’ it your way for mor’n a year now, and all I can say is enough’s enough!

GLORIA: (a breath) I’m a volunteer with an organization – it’s called Hospice. Your doctor said he told you all about us.

GRACE: Listen, honey, I don’t mean to be unfriendly, but whatever it is you’re sellin’, I’m sure I’m way past needin’ it. (Pg 14) Broke my hip last year. Had to go to the hospital. That’s when they found the cancer. (Pg 17) I’m dying -- got a few weeks. Honey, when you’re 90 years old, death don’t come as no surprise. I buried my parents, my husband, and all of my five boys. If there’s one thing I know about its death. You do this for a living, help people die?

GLORIA: Why are you making this seem so ridiculous? You know, you’re a perfect example of what Hospice is all about! Your grandson, he picks you up from the hospital and dumps you here. You have no one to turn to for help. And believe me, Mrs. Stiles, you’re going to need help!

GRACE: But I’m not alone. The good Lord’s here with me.

GLORIA: Look, this hospice booklet. There are several stories in here about women just like you. Won’t you at least read it?

GRACE: I don’t think so. In the first place I’m not interested! In the second (she can’t read) – we’ll just stop with the first place.

GLORIA: Mrs Stiles, do you – You don’t do you? My, God, that explains everything.

GRACE: Don’t you have a family at home to take care of? Or a job. Thought all you young women nowadays had jobs!

GLORIA: I had a job in New York. I’ve looked for something around here, but there isn’t anything – That’s when I heard about this new hospice program, that they were desperate for volunteers with professional skills. I have an MBA from Harvard!

GRACE: Just tell me one thing. What do you get out of this?

GLORIA: Nothing! Okay, let’s just say I’m interested in –

GRACE: Death? You can’t even say the word.

GLORIA: Death. (Pg 25) And my name is Gloria. (Pg 37) [My] son. Danny. He was killed in an automobile accident a couple of years ago.

GRACE: These young people today and their automobiles. Why do they insist on driving so fast?

GLORIA: Danny was only twelve years old. He wasn’t driving. I was.

GRACE: Ter’ble thing to lose a child. My Carroll died when he was a baby. Went in to check on him one morning and he wasn’t breathin’. Doctor come. Said these things just happen. Few years later Duane was out huntin’ with his Daddy. Tripped over some barbed wire buried under the snow? Gun went off. He was 10 years old. Got so I hated to let the little ones out o’ my sight. Thought I was goin’ to lose ‘em all. Guess I did, though, didn’t I? Guess my only comfort is I’ll be seein’ ‘em all real soon now.

GLORIA: Do you really believe that? About seein’ your children in another life?

GRACE: Course I do, don’t you?

GLORIA: I . . . No.

GRACE: S’pose next you’re goin’ to say you don’t believe in God. (Pg 50) When I was just a girl, there was this hymn my Mama liked to sing. Called “Where He Leads Me.” (singing*) “He will give me grace and glory, and go with me all the way.” Mama used to laugh “We got our little Grace,” she’d say. “Now all we need is a little Glorie.” (Pg 52) (irritably) Why don’t you go home?

GLORIA: I’m not leaving you here alone. Are you going to let me put you to bed?

GRACE: No! (Pg 53) I don’t want to be asleep when He comes.

GLORIA: When who comes?

GRACE: Death. Oh, I’m afraid of Him, I am. But it’s like this time my Daddy hauled us kids all the way to Richmond to the State Fair. They had this Ferris wheel there. Looked to be least a mile high. I wanted to ride that thing mor’n anything in the world, but I was too scared. My whole life’s been like that. Always too scared. But this time I’m ready to be lifted up into that Promised Place (breaking down) where I won’t hurt or be afraid ever again. (Gloria goes to her but Grace, embarrassed pushes her away)

GLORIA: (Pg 55) (backing away) Okay, okay.

GRACE: I regretted not havin’ a daughter. Always felt I had so much to give, so many secrets to share. Boy children, they ain’t interested in learnin’ nothin’. All they want to do is break away. Get out and tear up the earth. You know I’ve always marveled the human race has been able to survive long as it has in the hands of men.

GLORIA: You sound like a liberated woman, Grace. I’m impressed.

GRACE: Sure, I’m liberated all right. Ain’t been mor’n fifty miles from this farm since the day I got married . . . (quiet for a moment) What I just said, ‘bout boy children tearing up the earth? I wasn’t talkin’ ‘bout your little boy. He wasn’t like that, was he?

GLORIA: No.

GRACE: What was his name? Danny? (Gloria nods) Bet he was smart.

GLORIA: Yes. (beat) But he was still very much a boy. My husband saw to that. But for every jock thing Peter pushed Danny into, I insisted on equal time. Like with his piano. I mean he was only 12 years old and already developing his own style. He reminded me of – me when I was his age.

GRACE: Just look at your face. All lit up. Wondered if I’d ever see you smile like that.

GLORIA: Oh, Grace, that was such a time in my life. I had just moved to a very large [law] firm, brought in, I might add, as full partner. I finally had power, Grace. And money. I bought a car. An expensive car . . . (tapers off, lost in thought; shakes it off and changes the subject) Your children. The ones you lost when they were small. How did you deal with . . . losing them?

GRACE: Deal with it? I’m not sure I know what you mean. I grieved. Still do. But it was the good Lord’s will.

GLORIA: And you didn’t question it? The good Lord’s will.

GRACE: What I don’t think a person like you understands, people like us, people tied to the earth, we’re used to death. You civilized people. You’ve moved so far away from death you forget it’s as much a part of life as being born -- these things just happen.

GLORIA: (moving away) Oh yes, it certainly did happen. One warm, September afternoon

GRACE: Honey, don’t –

GLORIA: . . . it had been Danny’s first day at school. I decided to pick him up. In the new car. We were heading back across town. I don’t know where it came from. The newspaper truck. When it hit us, we were pinned inside the wreck for more than an hour. Danny was on my lap. And as I held him, I could feel his life slowly slipping from his body. And there was nothing I could do. . . so we buried him. This gentle, gifted boy. Disposed of his clothes, his – things. And then, I just shut down. ouldn’t go to work. Wouldn’t answer the phone. Wouldn’t even go outside. Peter dragged me from one doctor to another. We ended up with a shrink who suggested a change, somewhere far from the city. So now here I am . . . Okay, maybe I did deserve to get slapped down. I mean, I had become a little lofty, a little full of myself. But if these were my sins, MY SINS, why was it Danny who paid for them? You talk about God? What kind of God is this? Look at your life. Haven’t you ever asked yourself . . . (stops. gropes for control) I’m sorry. I don’t know why I’m doing this.

GRACE: My life. What about my life? Say it.

GLORIA: (trying to push it back but can’t) You buried not one child, but five! You have a grandson. Who are you to him? A woman he charges to run errands and cut wood. Haven’t you ever asked yourself what your life’s been for? Here you are a sick old woman, ravaged with pain, without a soul in the world to even care whether you live or – Grace, I – I think I’d better go home after all.

GRACE: I never have asked myself that question. What’s my life been for – Maybe I should. I sure ain’t left my mark on much o’ nothin’.

GLORIA: Grace, I’m sorry.

GRACE: Why should you be sorry for my miserable life? Got nothin’ to do with you. I’d still like to know what you’re doin’ here, messin’ with death. So, you lost a child.

GLORIA: Things happen . . . just happen. No rhyme, no reason. No one pulling the strings.

GRACE: I didn’t say there was no reason.

GLORIA: Then what is it?

GRACE: How should I know? You accept each day as it comes. You don’t question. Something like this happens, you start over. Good heavens, honey, either you do a thing or you don’t. What other choice you got?

GLORIA: Oh, I’ve got choices. At least a few.

GRACE: Like what? (slowly) Oh. Oh, I see. That what this is, this volunteerin’ you do? You here to try Death on for size ‘fore you go off and kill yourself? Is that it? IS IT!

GLORIA: IT SHOULDN’T HAVE HAPPENED, GODDAMNIT! He was a brilliant, innocent boy with his whole life in front of him. You’re the one with the faith, you tell me! What heavenly purpose was served by crushing his body and leaving it on my lap to die? All I want is an answer, Grace! One lousy reason! (beat) Except there is no answer, is there? I’m sorry, but whatever this – game is, I can’t play it anymore!

GRACE: (Pg 70) (long pause) I don’t like what’s happenin’ to me [either]. Ain’t sayin’ I’m doubtin’. Never doubted the good Lord one second o’ my life. But you got me wonderin’. So many things. (Pg 80) You said it yourself. My life’s been for nothin’! Absolutely nothin’! I’m an illiterate, backwards old woman! (Pg 95) (freezes. takes a quick breath. her face goes blank)

GLORIA: Grace? Grace, what is it?

GRACE: Pain . . . Goin’ to be bad.

GLORIA: Grace?

GRACE: Oh, sweet Jesus.

GLORIA: (reaching for the morphine in her bag) Listen to me. Grace, this is morphine.

GRACE: NO! NO DRUGS! . . . Oh, sweet Jesus!

GLORIA: DAMNIT, GRACE! THERE IS NO REASON TO SUFFER LIKE THIS!

GRACE: I DON’T CARE! WON’T DO NO GOOD! (Gloria holds Grace’s mouth open, administers the drops. Grace pulls away) Only fools believe in God. That’s what I am. A FOOL! All the times I was cold and hungry and hurtin’ and wantin’ to run away from this miserable farm. But I though this is where God wanted me to be. Is that what you come here for? (shouting) TO TELL ME MY WHOLE LIFE WAS FOR NOTHIN’?!

GLORIA: Grace, please.

GRACE: Honey, I know I’m ignorant, but I’ve been happy in my ignorance! WHY COULDN’T YOU O’ JUST LET ME DIE THAT WAY? I DON’T WANT YOU HERE! GET OUT! I’m an old woman. Why can’t you understand that? Go on, get out of here! I don’t need you!

GLORIA: Yes, you do! (beat) Grace, I’ll probably never believe in the same things you do. But you’ve shown me . . . that it might be possible to believe in something again. Are you listening to me? Grace?

GRACE: (a little surprised) Pain’s goin’ away. It’s that morphine ain’t it? (Gloria nods) (Pg 101) (thinking, then speaks) I think that’s all God wants any of us to do . . . hold on to each other with all our might. (tears) Look at me, cryin’ like a baby! (long pause) (Pg 102) If I take a nap, you think I’ll wake up? (Gloria’s eyes fill with tears) (Pg 103) You cryin’, honey? Why?

GLORIA: I don’t know.

GRACE: (holding out her hand) Maybe you’re grievin’ for me already . . . That’s what this is, this messin’ with death you do. You think if you stop grievin’ you’ll finally have to let go of your little boy.

GLORIA: (takes Grace’s hand) I loved him so much, Grace.

GRACE: ‘Course you did. But, honey, it wasn’t death tied you and that little boy together, it was life. (closes her eyes and falls asleep)

GLORIA: (kneels by her side, holding her hand; sings softly) “He will give me grace and glory, and go with me all the way.”*
```
