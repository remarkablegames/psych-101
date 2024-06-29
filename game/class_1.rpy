default affection = 0

label class_1:
    queue music [dark_intro, dark_verse]

    scene bg lecturehall
    with dissolve

    "You head to class and quickly find an empty seat. You notice a cute girl sitting next to you."

    show classmate surprised at left
    with moveinleft

    menu:
        "Introduce yourself.":
            $ affection += 1
            player "Hi there!{w=0.1} Looks like we’re going to be seatmates."

        "Say nothing.":
            $ affection -= 1
            player "..."

    show classmate smile at left, flip

    classmate "Hi, I’m [classmate.name],{w=0.1} nice to meet you."
    player "Nice to meet you too,{w=0.1} I’m [player_name]."
    player "What brings you to Psych 101?"
    classmate "I’m interested in positive psychology."
    classmate "And you?"

    menu:
        "I’m here for the easy A.":
            $ affection -= 1
            classmate "Haha, aren’t we all?"
            classmate @ shy "But I hear the exams are pretty tough."
            player "Oh, I didn't know about that."
            player "I enrolled since I saw the class ratings were pretty high."
            classmate "We’ll get through it."
            player "For sure!"

        "I want to learn how psychology applies to our everyday lives.":
            $ affection += 1
            classmate @ surprised "Nice, that sounds exciting."
            classmate "I also want to learn how to be a stronger person by understanding my psychology."
            player "How so?"
            classmate embarrassed "Like how to manage my emotions and think more optimistically."
            player "That’s a great goal."
            classmate smile "Haha, thanks."

    "You chat for a bit more before the teacher interrupts you."

    show classmate smile at left, scale(0.8)
    with dissolve

    show teacher talking at scale(0.6), right
    with moveinright

    teacher "Alright, class is starting.{w=0.2} Today we’re going to learn about Pavlov’s dog."

    stop music fadeout 4

    jump after_class_1

label after_class_1:
    scene bg school
    with fade

    play sound school_bell volume 0.15
    queue music [sad4_verse, sad4_hook]

    "After class ends, you take a quick stroll with [classmate.name] on the school campus."

    show classmate smile
    with dissolve

    player "What did you think of Pavlov’s dog?"
    classmate "Super interesting!"
    classmate "How about you?"

    menu:
        "Agreed. Plus, I love dogs!":
            $ affection += 1
            classmate @ surprised "Amazing."

        "Eh, I thought it was boring. Also not a fan of dogs.":
            $ affection -= 1
            classmate @ sad "I see."

    menu:
        "Ask [classmate.name] if she owns a pet.":
            $ affection += 1
            player "Do you have a pet?"
            classmate "Yep, I have a Golden Retriever."
            player "What’s his name?"
            classmate "His name is Buddy and he’s 13 years old."
            player "Isn’t that old in dog years?"
            classmate "Yep, but he’s still going strong!{w=0.2} I can’t see myself without my best bud."

        "Talk about class.":
            player "What did you think of the lesson?"
            classmate "Pretty good!{w=0.2} Just trying to keep up with everything."
            player "It’s interesting how animals can be conditioned to a stimulus."
            classmate surprised "Like how we can train dogs to do almost anything?"
            player "Yeah, I wonder about the things we’re conditioned to that we don’t realize."
            classmate smile "Good question.{w=0.2} It’s probably more than what is expected."
            player "For sure."

    menu:
        "Want to grab a snack?":
            $ affection += 1
            classmate "Sure, let’s do it."
            jump after_class_1_break

        "I have to go back and study.":
            $ affection -= 1
            classmate "Alright,{w=0.1} see you later."
            jump after_class_1_study

label after_class_1_break:
    stop music fadeout 4

    scene bg restaurant
    with dissolve

    play music [sad8_verse, sad8_hook]

    "You and [classmate.name] make way to the school’s cafeteria."

    show classmate smile
    with dissolve

    menu:
        "What would you like? My treat.":
            $ affection += 1
            classmate "Thanks."

        "I left my wallet back in class.":
            $ affection -= 1
            classmate @ surprised "No worries,{w=0.2} I got you."

    classmate "I’ll have a cupcake."
    classmate "What are you having?"

    menu:
        "Hot dog":
            classmate "Delicious."

        "Tacos":
            classmate "Yummy."

    "After buying the food, you both find an empty table and starting chowing down."

    menu:
        "What do you like to do in your free time?":
            $ affection += 1
            classmate "I enjoy reading and painting. It’s a good way to relax."

        "Did you hear that mental illness is on the rise?":
            $ affection -= 1
            classmate @ surprised "I haven’t. That’s troubling."

    "As you spend more time with [classmate.name], you notice her mood is generally upbeat and positive."

    jump after_class_1_study

label after_class_1_study:
    stop music fadeout 2

    scene black
    with fade

    play music sad8_outro fadein 1

    "You went to the library and studied for a few hours."
    "Feeling exhausted, you decide to wrap up the session."
    "As you head back home, you bump into someone familiar."

    stop music fadeout 2

    jump after_class_1_hangout

label after_class_1_hangout:
    scene bg park
    with dissolve

    queue music sad14_refrain
    queue music sad14_hook

    show classmate surprised at flip, center
    with moveinbottom
    with vpunch

    pause 1

    player "Hey [classmate.name], didn’t expect you here."
    player "Want to join me for a walk?"

    show classmate smile at flip, center

    classmate "Sure, that sounds nice."

    "You and [classmate.name] enjoy the fresh air and the beauty of nature. [classmate.name] seems to relax more as you walk together."

    classmate "Thanks for inviting me. This is really nice."
    player "I’m glad you’re enjoying it."

    queue music sad14_intro
    queue music sad14_verse

    "You and [classmate.name] find a bench and sit down to rest for a while."

    show classmate smile at right
    with ease

    menu:
        "Have you thought about what you want to do in the future?":
            $ affection += 1
            show classmate embarrassed at right
            classmate "I have some ideas, but I’m not sure yet."
            player "Don’t worry{w=0.1}, you’re still young.{w=0.2} You have the time to figure things out."
            show classmate smile at right
            classmate "I hope so."
            "You and [classmate.name] spent some time staring at clouds before parting ways."

        "You text your friends to see what they’re doing.":
            $ affection -= 1
            show classmate sad at right
            classmate "Oh,{w=0.1} are you bored?{w=0.2} We can leave."
            player "I have some errands I need to run."
            classmate "Alright,{w=0.2} I’ll see you in class tomorrow."
            "You and [classmate.name] then part ways for the day."

    stop music fadeout 4

    jump personality_test_openness
