label before_class_4:
    call personality_test_agreeableness
    jump class_4

label class_4:
    queue music chill_intro
    queue music chill_verse

    scene bg lecturehall
    with dissolve

    show classmate sad at left

    "You notice [classmate.name] is quieter than usual."

    show classmate sad at left, flip

    player "Hey [classmate.name],{w=0.3} you okay?{w=0.4} You seem a bit off today."
    classmate "{alpha=0.7}{i}(sigh){/i}{/alpha}{w=0.5} Just dealing with some stuff.{w=0.3} It’s been a tough week."

    menu:
        "If you need to talk, I’m here for you.":
            $ affection += 1
            classmate "Thanks,{w=0.1} I appreciate it."

        "We all have tough weeks, you’ll get through it.":
            $ affection -= 2
            classmate "Yeah, I guess..."

    show teacher talking at scale(0.6), right

    "Class begins, but you can’t help but notice [classmate.name]’s distracted state.{w=0.2} The teacher discusses the importance of mental health, which deeply resonates with you."

    jump after_class_4

label after_class_4:
    stop music fadeout 2

    scene bg club
    with dissolve

    queue music sad1_intro
    queue music sad1_verse

    "Later in the hallway, you overhear [classmate.name] talking to another student."

    show classmate upset at scale(0.7), right
    pause 0.8
    show classmate upset at right, flip

    classmate "{alpha=0.7}{i}(frustrated){/i}{/alpha}{w=0.2} I don’t know what to do anymore.{w=0.3} It feels like everything is falling apart."

    menu:
        "Reach out to see if you can help.":
            $ affection += 1

            jump after_class_4_help

        "Avoid being too nosy.":
            $ affection -= 3

            "You feel it’s not in your place to stick your nose in [classmate.name]’s affairs."
            "Hopefully [classmate.name]’s situation will pass after she gives it some time."

            jump after_class_4_home

label after_class_4_help:
    show classmate upset at right, unflip

    player "Hey [classmate.name], is everything alright?"

    show classmate sad at scale(1), center
    with dissolve

    classmate "It’s just...{w=0.3} everything feels so heavy...{w=0.3} I’m going through a lot, and I’ve been feeling really low."
    player "What happened?"
    classmate "Buddy passed away."

    menu:
        "Who’s Buddy?":
            $ affection -= 3
            classmate "He’s my dog..."
            player "Oh, I’m sorry to hear."

        "I’m sorry to hear.":
            pass

    classmate "..."
    player "Have you considered talking to a school counselor?{w=0.2} They might be able to help."
    classmate "Maybe...{w=0.4} I don’t know if anything will change."
    player "It’s worth a try.{w=0.2} Sometimes talking to someone is enough and can make a difference."
    classmate "Thanks, I’ll keep that in mind."

label after_class_4_home:
    stop music fadeout 2

    scene bg living room night
    with fade

    queue music sad2_intro

    "Later that evening, you check social media and see a post from [classmate.name]."
    classmate "“Sometimes I wonder if it’s all worth it.{w=0.4} Life just feels like one big mess.”"

    queue music [sad2_verse, sad2_bridge]

    menu:
        "Reach out to [classmate.name].":
            $ affection += 1
            player "Hey [classmate.name],{w=0.1} I saw your post.{w=0.2} I’m really concerned about you.{w=0.2} Please,{w=0.1} let’s talk."
            classmate ".{w=0.2}.{w=0.2}.{w=0.2}"
            classmate "Thanks for reaching out.{w=0.2} I’m just really struggling right now."
            player "Remember what we talked about today?{w=0.2} Maybe talking to the counselor could help.{w=0.1} I can go with you if you want."
            classmate "Okay.{w=0.1} Maybe tomorrow."

        "Ignore the post.":
            $ affection -= 5
            "You decide to ignore [classmate.name]’s post."
            "“Best not to be a nosy busybody, right?”"
            "You feel things will be better after a good night’s rest."

    stop music fadeout 2

    scene black
    with fade

    queue music sad8_outro fadein 1

    "You tried to do some more studying, but something doesn’t feel right."
    "You decide to shower and go to bed early."
    "After some tossing and turning, you eventually fell asleep."

    jump before_class_5
