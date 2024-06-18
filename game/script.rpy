﻿default affection = 0

label start:
    jump intro

label act_1:
    scene bg lecturehall
    with dissolve

    show classmate sad at left
    pause 0.8
    show classmate sad at left, flip

    play music "chill_intro.ogg"
    queue music "chill_verse.ogg"

    player "Hey Alex, you okay? You seem a bit off today."
    classmate "{alpha=0.7}{i}(sigh){/i}{/alpha} Just dealing with some stuff. It’s been a tough week."

    menu:
        "If you need to talk, I’m here for you.":
            $ affection += 1
            classmate "Thanks. I appreciate it."

        "We all have tough weeks, you’ll get through it.":
            $ affection -= 1
            classmate "Yeah, I guess..."

    show teacher normal at scale(0.6), right

    "Class begins, but you can’t help but notice Alex’s distracted state. The teacher discusses the importance of mental health awareness, which deeply resonates with you."

    stop music fadeout 4

    queue music "sad1_intro.ogg"
    queue music "sad1_verse.ogg"

    scene bg club
    with dissolve

    show classmate upset at scale(0.7), right

    "Later, in the hallway, you overhear Alex talking to another student."
    classmate "{alpha=0.7}{i}(frustrated){/i}{/alpha} I don’t know what to do anymore. It just feels like everything is falling apart."

    menu:
        "Alex, I overheard what you were saying. Do you want to talk about it?":
            $ affection += 1
            player "Alex, I overheard what you were saying. Do you want to talk about it?"
            classmate "It’s just... everything feels so heavy. My family is going through a lot, and I’ve been feeling really low."

        "Maybe you should try to relax and take it easy.":
            $ affection -= 1
            classmate "I wish it were that simple..."

    player "I’m really sorry to hear that. Have you considered talking to the school counselor? They might be able to help."
    classmate "Maybe... I just don’t know if it will change anything."
    player "It’s worth a try. Sometimes just talking to someone can make a big difference."
    classmate "Thanks. I appreciate it."

    stop music fadeout 4

    queue music "sad2_intro.ogg"

    scene bg meadow
    with dissolve

    "Later that evening, you check social media and see a post from Alex."
    classmate "Sometimes I wonder if it’s all worth it. Life just feels like one big mess."

    queue music ["sad2_verse.ogg", "sad2_bridge.ogg"]

    menu:
        "Hey, I saw your post. I’m really concerned about you. Please, let’s talk.":
            $ affection += 1
            classmate "..."
            classmate "Thanks for reaching out. I’m just really struggling right now."
            player "Remember what we talked about today? Maybe talking to the counselor could help. I can go with you if you want."
            classmate "Okay. Maybe tomorrow."

        "Ignore the post.":
            $ affection -= 1

    stop music fadeout 4

    scene bg lecturehall
    with dissolve

    queue music "tense_intro.ogg"
    queue music "tense_verse.ogg"

    "You get to class the next day and notice that Alex is absent. The room feels tense."
    player "{alpha=0.7}{i}(thinking){/i}{/alpha} Where’s Alex? She said she’d be here today."

    if affection > 0:
        jump good_ending
    else:
        jump bad_ending
