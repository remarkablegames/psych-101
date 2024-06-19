default affection = 0

label class_1:
    scene bg lecturehall
    with dissolve

    show classmate sad at left
    pause 0.8
    show classmate sad at left, flip

    play music "chill_intro.ogg"
    queue music "chill_verse.ogg"

    player "Hey Alex,{w=0.3} you okay?{w=0.4} You seem a bit off today."
    classmate "{alpha=0.7}{i}(sigh){/i}{/alpha}{w=0.5} Just dealing with some stuff.{w=0.3} It’s been a tough week."

    menu:
        "If you need to talk, I’m here for you.":
            $ affection += 1
            classmate "Thanks.{w=0.1} I appreciate it."

        "We all have tough weeks, you’ll get through it.":
            $ affection -= 1
            classmate "Yeah, I guess..."

    show teacher normal at scale(0.6), right

    "Class begins, but you can’t help but notice Alex’s distracted state.{w=0.2} The teacher discusses the importance of mental health awareness, which deeply resonates with you."

    stop music fadeout 4

    jump after_class_1

label after_class_1:
    queue music "sad1_intro.ogg"
    queue music "sad1_verse.ogg"

    scene bg club
    with dissolve

    "Later in the hallway, you overhear Alex talking to another student."

    show classmate upset at scale(0.7), right
    pause 0.8
    show classmate upset at right, flip

    classmate "{alpha=0.7}{i}(frustrated){/i}{/alpha}{w=0.2} I don’t know what to do anymore.{w=0.3} It just feels like everything is falling apart."

    menu:
        "Alex, I overheard what you were saying. Do you want to talk about it?":
            $ affection += 1
            show classmate upset at right, unflip
            classmate "It’s just...{w=0.3} everything feels so heavy...{w=0.3} My family is going through a lot, and I’ve been feeling really low."

        "Maybe you should try to relax and take it easy.":
            $ affection -= 1
            show classmate upset at right, unflip
            classmate "I wish it were that simple..."

    player "I’m really sorry to hear that.{w=0.3} Have you considered talking to the school counselor?{w=0.2} They might be able to help."

    classmate "Maybe...{w=0.4} I just don’t know if it will change anything."
    player "It’s worth a try.{w=0.2} Sometimes just talking to someone can make a big difference."
    classmate "Thanks.{w=0.2} I appreciate your concern."

    stop music fadeout 4

    jump personality_test_agreeableness

label after_class_2:
    queue music "sad2_intro.ogg"

    scene bg meadow
    with dissolve

    "Later that evening, you check social media and see a post from Alex."
    classmate "“Sometimes I wonder if it’s all worth it.{w=0.4} Life just feels like one big mess.”"

    queue music ["sad2_verse.ogg", "sad2_bridge.ogg"]

    menu:
        "Hey, I saw your post. I’m really concerned about you. Please, let’s talk.":
            $ affection += 1
            classmate ".{w=0.2}.{w=0.2}.{w=0.2}"
            classmate "Thanks for reaching out.{w=0.2} I’m just really struggling right now."
            player "Remember what we talked about today?{w=0.2} Maybe talking to the counselor could help.{w=0.1} I can go with you if you want."
            classmate "Okay.{w=0.1} Maybe tomorrow."

        "Ignore the post.":
            $ affection -= 1

    stop music fadeout 4

    jump class_3

label class_3:
    scene bg lecturehall
    with dissolve

    queue music "tense_intro.ogg"
    queue music "tense_verse.ogg"

    "You get to class the next day and notice that Alex is absent. The room feels tense."
    player "{alpha=0.7}{i}(thinking){/i}{/alpha}{w=0.1} Where’s Alex?{w=0.2} She said she’d be here today."

    show teacher sadder at scale(0.6), center

    teacher "I don’t know how to say this,{w=0.3} but one of our classmates took her own life last night."
    player "{alpha=0.7}{i}(thinking){/i}{/alpha}{w=0.1} No,{w=0.2} it can’t be her."
    teacher "For the privacy of the individual,{w=0.1} we’re unable to share any news.{w=0.1} But please be respectful for the time being."

    stop music fadeout 1

    if affection > 0:
        jump good_ending
    else:
        jump bad_ending
