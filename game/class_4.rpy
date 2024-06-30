label before_class_4:
    call personality_test_agreeableness
    jump class_4

label class_4:
    scene bg lecturehall
    with dissolve

    show classmate sad at left

    queue music chill_intro
    queue music chill_verse

    "You notice [classmate.name] is quieter than usual."

    show classmate sad at left, flip

    player "Hey [classmate.name],{w=0.3} you okay?{w=0.4} You seem a bit off today."
    classmate "{alpha=0.7}{i}(sigh){/i}{/alpha}{w=0.5} Just dealing with some stuff.{w=0.3} It’s been a tough week."

    menu:
        "If you need to talk, I’m here for you.":
            $ affection += 1
            classmate "Thanks,{w=0.1} I appreciate it."

        "We all have tough weeks, you’ll get through it.":
            $ affection -= 1
            classmate "Yeah, I guess..."

    show teacher talking at scale(0.6), right

    "Class begins, but you can’t help but notice [classmate.name]’s distracted state.{w=0.2} The teacher discusses the importance of mental health awareness, which deeply resonates with you."

    stop music fadeout 4

    jump after_class_5

label after_class_5:
    queue music sad1_intro
    queue music sad1_verse

    scene bg club
    with dissolve

    "Later in the hallway, you overhear [classmate.name] talking to another student."

    show classmate upset at scale(0.7), right
    pause 0.8
    show classmate upset at right, flip

    classmate "{alpha=0.7}{i}(frustrated){/i}{/alpha}{w=0.2} I don’t know what to do anymore.{w=0.3} It feels like everything is falling apart."

    menu:
        "Reach out to see if you can help.":
            $ affection += 1

            jump after_class_5_help

        "Avoid being too nosy.":
            $ affection -= 1

            "You feel it’s not in your place to stick your nose in [classmate.name]’s affairs."
            "Hopefully [classmate.name]’s situation will pass after a good night’s sleep."

            jump after_class_5_study

label after_class_5_help:
    show classmate upset at right, unflip

    player "Hey [classmate.name], is everything alright?"

    show classmate sad at scale(1), center
    with dissolve

    classmate "It’s just...{w=0.3} everything feels so heavy...{w=0.3} My family is going through a lot, and I’ve been feeling really low."
    player "What happened?"
    classmate "Buddy passed away."

    menu:
        "Who’s Buddy?":
            $ affection -= 1
            classmate "He’s my dog..."
            player "I’m sorry to hear."

        "I’m sorry to hear.":
            $ affection += 1

    classmate "..."
    player "Have you considered talking to a school counselor?{w=0.2} They might be able to help."
    classmate "Maybe...{w=0.4} I don’t know if anything will change."
    player "It’s worth a try.{w=0.2} Sometimes talking to someone is enough and can make a difference."
    classmate "Thanks, I’ll keep that in mind."

label after_class_5_study:
    stop music fadeout 2

    scene black
    with fade

    play music sad8_outro fadein 1

    "You went back home to do some studying, but something doesn’t sit right with you."
    "You decide to shower and go to bed early."

    stop music fadeout 4
    jump before_class_5
