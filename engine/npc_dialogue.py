"""
Dialogue text with with player responses.
- necromancer
- rat
"""

# 80 characters for reference:
#------------------------------------------------------------------------------#

from engine.instances import my_player

necromancer_dialogue = {
    1: {
        "text":
"""I have to say, I am impressed. I sensed you intruding my lair and you managed
to pass through my traps and creatures up until now. Now tell me, do you wish
to die here or do you wish to be the test subject for my new experiment? It will
be painful either way!""",

        "options": [
            (f"My name is {my_player.name}. I've heard of your exploits against the people of\n\
   Stennerden and I've come to bring justice. Duel me, necromancer!", 2),
            ("I don't care for chat, I will be the last thing you will ever see! (fight)", 21),
            ("SKIP TO 17.", 17)
            ]
        },
    2: {
        "text":
"""HAH! A peasant human with your little toy against ME, a mage with years of
conjuration practice and whose life is devoted entirely towards the dark arts?!
I mirth at your feebleness!""",

        "options": [
              ################################################################################...
            ("Do not underestimate me, mage. I've passed all your traps and destroyed all your\n\
   monsters and came out a better warrior than I ever was! Now, will you duel\n\
   me?", 3),
            ("Who you are does not scare me at all. I've come for one thing and one thing\n\
   only: your head! (fight)", 21)
            ]
        },
    3: {
        "text":
"""How very brave. I have met some of you. Though none have lived to tell the tale
of winning a duel with a necromancer. But before I end your life, I will tell
you this: Do you really know why you are here? Randolf only told you what you
needed to know.""",

        "options": [
              ################################################################################...
            ("You're really tempting me here, mage... but of course. My job here is simple.\n\
   You harrass the innocent townspeople and I'm here to stop you. For good.", 4),
            ("I trust Randolf and his word. I have no quarrel with him either and a fat sum of\n\
   aurels is waiting for me back in Stennerden in exchange for your head. What\n\
   do you have in mind?", 5),
            ("I don't stay and chat with the likes of you. Your time ends here! (fight)", 21)
            ]
        },
    4: {
        "text":
'''I am not surprised by your words. Those "innocent" townspeople have caused me
nothing but agony and humiliation. They were all his believers. It was not
enough either that I had my home scorched up in flames and be sent to a pillory.
And I tell them that Randolf is a cruel and corrupt man, that the blood was
falsely placed on my hands, but to no avail.''',

        "options": [
            ("What do you mean?", 6),
            ("A change of mind, I don't care to hear a word more. Die! (fight)", 21)
            ]
        },
    5: {
        "text":
'''I am not surprised by your words. Randolf is a manipulative liar and should be
sentenced to the gallows for what he has done to me and to his fellow
townspeople. But they were all his believers. It was not enough either that I
had my home scorched up in flames and be sent to a pillory. And I tell them that
Randolf is a cruel and corrupt man, that the blood was falsely placed on my
hands, but to no avail.''',

        "options": [
            ("What do you mean?", 6),
            ("A change of mind, I don't care to hear a word more. Die! (fight)", 21),
            ]
        },
    6: {
        "text":
"""As I have said previously, Randolf always gets his way out with bribery and
coercion. At least once a week he would set off in the evening with some young
maiden from the village and take her to his manor. And often those maidens were
unwilling as they loved their husbands. But you already know in his nature, he
still managed to submit them to his henious desires, through ways I do not wish
to imagine... But it was until one evening that-""",

        "options": [
            ("*let him continue*", 7),
            ("Stop, I don't believe any of this. You're trying to get me to side with you.", 20),
            ("You know what, I have no more time for this. Taste my steel! (fight)", 21),
            ]
        },
    7: {  # Point of no return, you may only listen to his backstory from now on haha.
        "text":
"""-I came home to the sound of struggle and yelping. The front door was locked
so I ran up from the back and to my eyes I saw my poor wife, my beautiful
darling, being mishandled by that pot-bellied, dog-headed whoreson they call the
town bailiff. I yelled her name. I lunged at the bastard and we fought for a bit
until at one moment got the best of me and pulled a dagger to my wife's throat,
claiming he would kill her if I got any closer.""",

        "options": [
            ("...", 8)
            ]
        },
    8: {
        "text":
"""It was at this point I had to recollect my wits before I could do any sudden
moves. Then there was a knock on the front door. It threw him off guard and a
chance for her to try to release herself and I to intervene. She squared him in
the nose but his stagger dodged my lunge and by then, the dagger was already in
her gut.""",

        "options": [
            ("...", 9)
            ]
        },
    9: {
        "text":
"""I grabbed a candlestick from the table and whacked him across his fat skull. And
in a fit of rage, I took the knife from his loosened clasp and proceeded to
repeatedly insert it back and forth across his abdomen all while he screeched
for help. It was most unfortunate that two guards happened to come by through
the back door at this state. They saw the blade buried underneath him and a dead
woman laying beside me.""",

        "options": [
            ("...", 10)
            ]
        },
    10: {
        "text":
"""They took me in for the town's jail, scheduled for the pillory on the morrow,
and the gallows over the next. The bailiff narrowly avoided bleeding out by
hasty action from the town's surgeon, and in hindsight, I should have went for
the throat. But as for her... the Gods could not save her. No form or amount of
explanation overrode his authority as he told them I was strangling my own wife
and that he had come in from the noises to stop me, only to be attacked and
stabbed.""",

        "options": [
            ("...", 11)
            ]
        },
    11: {
        "text":
"""Pillory day. A God-awful entire day as hurls of rotten vittles, insults, and
whatever filth they brought in rained upon what was left of my dignity. Back in
the cell I was, and they only fed me whatever scraps that were left from the
platform I was on. The last day came and I was only a few hours away from having
my neck hanged up from the gallows. But then I heard this mysterious voice in my
head, telling me how he had a plan for me and that I could still save her.""",

        "options": [
            ("...", 12)
            ]
        },
    12: {
        "text":
"""She... she was my sole reason to be, and without her the ounce of light I had
left in me had been taken. I chanced upon the offer and it was by some divine
intervention that I was given the fortitude and willpower to strangle the guard
from inside of the cell, unlocked it with his keys, and sneaked out. It was only
a matter of time before others would find out, and I raced to the graveyard and
found her lifeless, cold body still on a cart waiting to be buried.""",

        "options": [
            ("...", 13)
            ]
        },
    13: {
        "text":
"""I stole her away and escaped into the northern woods. Since then the intrusion
in my head would lead me to things I never would have imagined. I delved into
the mystic arts, into necromancy, still trying to preserve her beautiful body.
For years and years, I studied immensely, still following the voice. But I had
one other thing in mind the whole time. Randolf. And I am so very close to
perfecting my plan in having revenge. And then you came along.""",

        "options": [
            ("...", 14)
            ]
        },
    14: {
        "text":
"""...Heh, I see that you have been listening attentively to my backstory. And I am
quite certain you are wondering why I have not killed you yet.""",

        "options": [
            ("...", 15),
            ("Well, why are you telling me all this then?", 15),
            ("I do, you are trying to convert me to your side! You fear me!", 15),
            ("I'm still itching for a fight mage, despite what you say!", 15)
            ]
        },
    15: {
        "text":
"""I have decided during our little conversation to give you a chance. You heard
the truth about what happened in Stennerden. I can offer you more than they will
ever reward you. I have a plan for you.""",

        "options": [
            ("A plan? You mean the plan the voice in your head told you? I'm curious...", 16),
            ("This... this isn't right. Indeed, Randolf is scum, and I thank you\n\
   for showing me the truth. The town is greater off without such a corrupt and\n\
   incompetent man. But hear me: You cannot escape death, not even your\n\
   loved ones can. That voice is corrupting you.", 17),
            ]
        },
    16: {
        "text":
"""I want you to join me. I am able to see it within you, your reliability, your
determination, your fearlessness. And perhaps your loyalty... You would make a
valuable asset. I will show you a new way of life, powers you never could have
dreamt...""",
              ################################################################################
        "options": [
            ("You are right with your words. You were wronged and you deserve more with my\n\
   help. I accept your proposal. (end convo)", 18),
            ("This... this isn't right. Indeed, Randolf is scum, and I thank you\n\
   for showing me the truth. The town is greater off without such a corrupt and\n\
   incompetent man. But hear me: You cannot escape death, not even your\n\
   loved ones can. That voice is corrupting you.", 17),
            ]
        },
    17: {
        "text":
f"*Sigh*... Perhaps you may have misunderstood me. {my_player.name},\n\
this world in all its cruelness, where people can be moreso cruel than even\n\
monsters, is not to be treaded so heedlessly. To this, one must be\n\
opportunistic. Take advantage so that you may rise against those who oppose you.\n\
I can see it inside you, orphaned before you could even talk, you are alone in\n\
this world. Off to fend for yourself at an early age, you only had yourself to\n\
take care of. I can offer you a true home here. And together, I will give you a\n\
purpose. Join me.",

        "options": [
            ("I stand by my principles. You are an ill and disturbed old man and your\n\
   unethical practices would do no good in this world. I will not accept. (end\n\
   convo)", 19),
            ("Your... your words are right. I never would have thought of coming\n\
   into the samemind with the likes of you but... you are right. You were wronged\n\
   and I shall help you rise up in this dishonorable world. I accept. (end convo)", 18)
            ]
        },
    18: {  # Player chooses to join villain's side.
        "text":
"""Excellent. You chose reason and potential over petty, mortal affairs. My name is
Benswald Nightcaster. I foresee a marvelous future ahead of us. Now, come with
me...""",

        "options": 2
        },
    19: {  # Player rejects villain's proposal, commence final battle.
        "text":
"""Alas, it is a shame you were not able to see reason. You would still make a
valuable asset however... BY USING YOUR BLOOD!""",

        "options": 1
        },
    20: {
        "text":
"""I assure you I am truthfully telling you how it is, how I was wronged, and why I
chose this lifestyle. Now, shall I continue?""",

        "options": [
            ("Go on...", 7),
            ("This is all bogus. I don't want to hear any further. (fight)", 21)
            ]
        },
    21: {  # Player fights villain immediately without hearing backstory.
        "text":
"""Then so be it, YOU WON'T LEAVE HERE ALIVE!""",

        "options": 0
        },
    }

#------------------------------------------------------------------------------#

gay_rat_dialogue = {
    1: {
        "text": "Greetings, I'm Gil the gay rat. And who are you? :3",
        "options": [
            ("Wait, you're a talking rat? How?", 2),
            (f"My name is {my_player.name}, what are you doing here?", 3),
            ("Wait, you're gay? I must slay you! (fight)", 6),
            ]
        },
    2: {
        "text":
"""Why yes I am, unlike my fellow brothers and sisters. The necromancer here made
me who I am. Say, what brings you here?""",

        "options": [
            ("I'm looking for the necromancer, I heard from folks he's based around here. Know\n\
   where he is?", 4),
            ("Just exploring around this place, looking for adventure wherever I go.", 5),
            ("Enough chatting, time to die! (fight)", 6),
            ]
        },
    3: {
        "text":

"""Oh, I live here as the necromancer's pet. I wasn't like this before you know, I
just sort of... became me all of a sudden. He's quite an intelligent man too.
But he doesn't need me right now so I'm just going around for scraps, mating
with other gay rats, you know, stuff.""",

        "options": [
            ("Speaking of the necromancer, know of his whereabouts?", 4),
            ("Alright, I've had enough of this nonesense. (fight)", 6),
            ]
        },
    4: {
        "text":
"""Yes, he lives right over there to the north and I believe he's performing some
experiments in his chamber currently. Why do you ask?""",

        "options": [
            ("I've come to bring justice to the people of Stennerden and kill this madman!", 6),
            ("Oh, I'm a friend of his, just need a little word with him, is all. (lie)", 5),
            ]
        },
    5: {
        "text": "Well alright then. I'd better get going.",
        "options": 0
        },
    6: {
        "text": "I will defecate all over your dead body! >:(",
        "options": 1
        },
    }
