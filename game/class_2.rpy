label class_2:
    scene bg lecturehall
    with dissolve

    show classmate sad at left
    pause 0.8
    show classmate sad at left, flip

    queue music "chill_intro.ogg"
    queue music "chill_verse.ogg"

    "One day, you notice [classmate.name] is a bit quieter than usual."

    player "Hey [classmate.name],{w=0.3} you okay?{w=0.4} You seem a bit off today."
    classmate "{alpha=0.7}{i}(sigh){/i}{/alpha}{w=0.5} Just dealing with some stuff.{w=0.3} It’s been a tough week."

    menu:
        "If you need to talk, I’m here for you.":
            $ affection += 1
            classmate "Thanks.{w=0.1} I appreciate it."

        "We all have tough weeks, you’ll get through it.":
            $ affection -= 1
            classmate "Yeah, I guess..."

    show teacher normal at scale(0.6), right

    "Class begins, but you can’t help but notice [classmate.name]’s distracted state.{w=0.2} The teacher discusses the importance of mental health awareness, which deeply resonates with you."

    stop music fadeout 4

    jump after_class_2

label after_class_2:
    queue music "sad1_intro.ogg"
    queue music "sad1_verse.ogg"

    scene bg club
    with dissolve

    "Later in the hallway, you overhear [classmate.name] talking to another student."

    show classmate upset at scale(0.7), right
    pause 0.8
    show classmate upset at right, flip

    classmate "{alpha=0.7}{i}(frustrated){/i}{/alpha}{w=0.2} I don’t know what to do anymore.{w=0.3} It just feels like everything is falling apart."

    menu:
        "[classmate.name], I overheard what you were saying. Do you want to talk about it?":
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

    jump personality_test_conscientiousness
