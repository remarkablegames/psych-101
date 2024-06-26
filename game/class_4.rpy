label before_class_4:
    queue music "sad2_intro.ogg"

    scene bg meadow
    with dissolve

    "Later that evening, you check social media and see a post from [classmate.name]."
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

    jump class_4

label class_4:
    scene bg lecturehall
    with dissolve

    queue music "tense_intro.ogg"
    queue music "tense_verse.ogg"

    "You get to class the next day and notice that [classmate.name] is absent. The room feels tense."
    player "{alpha=0.7}{i}(thinking){/i}{/alpha}{w=0.1} Where’s [classmate.name]?{w=0.2} She said she’d be here today."

    show teacher sadder at scale(0.6), center
    with dissolve

    teacher "I don’t know how to say this,{w=0.3} but one of our classmates took her own life last night."
    player "..."
    player "{alpha=0.7}{i}(thinking){/i}{/alpha}{w=0.1} No,{w=0.2} it can’t be her."
    teacher "For the privacy of the individual,{w=0.1} we’re unable to share any news.{w=0.1} But please be respectful for the time being."

    stop music fadeout 1

    if affection > 0:
        jump good_ending
    else:
        jump bad_ending
