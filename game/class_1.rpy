default affection = 0

label before_class_1:
    call personality_test_extraversion
    jump class_1

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
            player "Hi there!{w=0.1} Looks like we’re seatmates."

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
            player "I thought it would be an easy class since the ratings were so high."
            classmate "We’ll make it through."
            player "For sure!"

        "I want to learn how psychology applies to our everyday lives.":
            $ affection += 1
            classmate @ surprised "Nice, that sounds exciting."
            classmate "I also want to learn how to be a better person by understanding psychology."
            player "How so?"
            classmate embarrassed "Like how to manage my emotions and think more optimistically."
            player "That’s a great goal."
            classmate smile "Haha, thanks."

    "You chat for a bit before the teacher interrupts you."

    show classmate smile at left, scale(0.8)
    with dissolve

    show teacher talking at scale(0.6), right
    with moveinright

    teacher "Alright, class is starting.{w=0.2} Today we’re going to learn about Pavlov’s dog."

    jump after_class_1

label after_class_1:
    stop music fadeout 2

    scene bg uni
    with fade

    queue music [sad4_verse, sad4_hook]

    "You find yourself strolling with [classmate.name] after class."

    show classmate smile
    with dissolve

    player "What did you think of Pavlov’s dog?"
    classmate "Super interesting!"
    classmate "How about you?"

    menu:
        "Agreed. Plus, I love dogs!":
            $ affection += 1
            classmate @ surprised "Gear to hear!"

        "Eh, I thought it was boring. Also not a fan of dogs.":
            $ affection -= 1
            classmate @ sad "I see..."

    menu:
        "Ask [classmate.name] if she owns a pet.":
            $ affection += 1
            player "Do you have a pet?"
            classmate "Yep, I have a Golden Retriever."
            player "What’s his name?"
            classmate "His name is Buddy and he’s 13 years old."
            player "Isn’t that old in dog years?"
            classmate @ surprised "Yep, but he’s still going strong!{w=0.2} I can’t see myself without my best bud."

        "Talk about class.":
            player "What did you think of the lesson?"
            classmate "Pretty good!{w=0.2} Just trying to keep up with everything."
            player "It’s interesting how animals can be conditioned."
            classmate surprised "Like how we can train dogs to do almost anything?"
            player "Yeah, I wonder what we’re conditioned to that we’re unaware of."
            classmate smile "Good question.{w=0.2} Probably more than what you expect."
            player "Indeed."

    menu:
        "Want to grab a snack?":
            $ affection += 1
            classmate "Sure, let’s do it."
            jump after_class_1_break

        "I have to go back and study.":
            classmate "Alright,{w=0.1} see you later."
            jump after_class_1_study

label after_class_1_break:
    stop music fadeout 2

    scene bg restaurant
    with dissolve

    queue music [sad8_verse, sad8_hook]

    "You and [classmate.name] make way to the cafeteria."

    show classmate smile at left
    with dissolve

    menu:
        "What would you like? My treat.":
            $ affection += 1
            classmate "Thanks!"

        "I left my wallet back in class.":
            $ affection -= 1
            classmate @ surprised "No worries,{w=0.2} I got you."

    classmate "I’ll have a cupcake."
    classmate "What are you having?"

    menu:
        "Hot dog":
            classmate "Yummy."

        "Tacos":
            classmate "Delicious."

    "After buying the food, you and [classmate.name] find a table and start chowing down."

    show classmate smile at center, flip
    with move

    show classmate smile at center, ypos(1.25)
    with move

    menu:
        "What do you like to do in your free time?":
            $ affection += 1
            classmate "I enjoy reading and painting.{w=0.2} It’s a good way to relax."
            player "What kind of genres do you read?"
            classmate @ embarrassed "I’ve recently been into philosophy and self-help."
            player "Do you have any recommendations?"
            classmate @ surprised "I really liked “Meditations” by Marcus Aurelius."
            player "Thanks for the recommendation, I’ll check it out."

        "Did you hear that mental illness is on the rise?":
            classmate surprised "I haven’t,{w=0.1} that’s troubling to hear."
            player "In 2021, more than 4 in 10 students felt persistently sad and nearly one-third experienced poor mental health."
            classmate "Why do you think this is the case?"
            player "I believe this is caused by the rise in social media,{w=0.1} the COVID-19 pandemic,{w=0.1} and societal pressures."
            classmate "I see.{w=0.2} I hope things will get better."
            player "Same."

    show classmate smile

    "As you spend more time with [classmate.name], you notice her mood is generally upbeat and positive."

    jump after_class_1_study

label after_class_1_study:
    stop music fadeout 2

    scene bg library
    with fade

    queue music sad2_intro

    "You went to the library and studied for a few hours."
    "Feeling exhausted, you decide to wrap up the session."

    scene black
    with fade

    "As you head back home, you bump into someone familiar."

    jump after_class_1_hangout

label after_class_1_hangout:
    stop music fadeout 2

    scene bg park
    with fade

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

    show classmate smile at ypos(1.1)
    with move

    menu:
        "Ask Alex about her future.":
            $ affection += 1
            player "Have you thought about what you want to do in the future?"
            classmate embarrassed "I have some ideas, but I’m not sure yet."
            player "Don’t worry, you still have time."
            classmate smile "I hope so."
            "You and [classmate.name] watch the drifting clouds before parting ways."

        "Text your friends to see what they’re doing.":
            $ affection -= 1
            classmate sad "Oh,{w=0.1} are you bored?{w=0.2} We can leave."
            player "I have some errands to run."
            classmate "No worries,{w=0.1} I’ll see you in class tomorrow."
            "You part ways and head home."

    jump after_class_1_home

label after_class_1_home:
    stop music fadeout 2

    scene black
    with fade

    queue music sad8_outro fadein 1

    "You went home exhausted, took a quick shower, and fell asleep shortly after."
    "You look forward to tomorrow’s psych class."

    jump before_class_2
