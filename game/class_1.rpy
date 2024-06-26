default affection = 0

label class_1:
    queue music ["dark_intro.ogg", "dark_verse.ogg"]

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
    player "Nice to meet you,{w=0.1} I’m [player_name]."
    player "What brings you to Psych 101?"
    classmate "I’m interested in positive psychology."
    classmate "And you?"

    menu:
        "I’m here for the easy A.":
            $ affection -= 1
            classmate "Haha, fair."

        "I want to learn how psychology applies to our everyday lives.":
            $ affection += 1
            classmate "Nice, that sounds exciting."

    "You continue to chat before the teacher interrupts you."

    show teacher normal at scale(0.6), right
    with moveinright

    teacher "Alright, class is starting.{w=0.2} Today we’re going to learn about Pavlov’s dog."

    stop music fadeout 4

    jump after_class_1

label after_class_1:
    scene bg uni
    with fade

    "You find yourself strolling with [classmate.name] after class."

    queue music ["sad4_verse.ogg", "sad4_hook.ogg"]

    show classmate smile
    with dissolve

    player "What did you think of Pavlov’s dog?"
    classmate "It’s pretty cute!"
    classmate "How about you?"

    menu:
        "Dogs are my best friends!":
            $ affection += 1
            show classmate surprised
            classmate "Amazing."

        "Eh, not a big fan of dogs.":
            $ affection -= 1
            show classmate sad
            classmate "I see."

    show classmate smile

    menu:
        "Ask [classmate.name] if she owns a pet.":
            $ affection += 1
            player "Do you have a pet?"
            classmate "Yep, I have a Golden Retriever."
            player "What’s his name?"
            classmate "His name is Buddy and he’s 13 years old."

        "Talk about class.":
            player "What did you think of the lesson?"
            classmate "Pretty good!{w=0.2} Just trying to keep up with everything."
            player "I find it interesting how animals can be conditioned to a stimulus."
            classmate "Indeed."

    play sound "school_bell.ogg" volume 0.3

    "The school bell rings."

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

    scene bg club
    with dissolve

    play music ["sad8_verse.ogg", "sad8_hook.ogg"]

    "You and [classmate.name] make your way to the school’s cafeteria."

    show classmate smile
    with dissolve

    menu:
        "What would you like? My treat.":
            $ affection += 1
            classmate "Thanks."

        "I left my wallet back in class.":
            $ affection -= 1
            show classmate surprised
            classmate "No worries,{w=0.2} I got you."

    show classmate smile

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

        "Did you read the report that the amount of people diagnosed with a mental illness is increasing?":
            $ affection -= 1
            show classmate surprised
            classmate "I haven’t. That’s worrisome."

    show classmate smile

    "As you spend more time with [classmate.name], you notice her mood is generally upbeat and positive."

    jump after_class_1_study

label after_class_1_study:
    stop music fadeout 2

    scene black
    with fade

    play music "sad8_outro.ogg" fadein 1

    "You went to the library and studied for a few hours."
    "Feeling exhausted, you decide to wrap up the session."
    "As you head back home, you bump into someone familiar."

    stop music fadeout 2

    jump after_class_1_hangout

label after_class_1_hangout:
    scene bg meadow
    with dissolve

    queue music "sad14_refrain.ogg"
    queue music "sad14_hook.ogg"

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

    queue music "sad14_intro.ogg"
    queue music "sad14_verse.ogg"

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
            "You and [classmate.name] spend the remaining time staring at the clouds before parting ways."

        "You text your friends to see what they’re doing.":
            $ affection -= 1
            show classmate sad at right
            classmate "Oh,{w=0.1} are you bored?{w=0.2} We can leave."
            player "I have some errands I need to run."
            classmate "Alright,{w=0.2} I’ll see you in class tomorrow."
            "You and [classmate.name] then part ways for the day."

    stop music fadeout 4

    jump personality_test_openness
