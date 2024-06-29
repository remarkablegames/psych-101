label class_2:
    scene bg lecturehall
    with dissolve

    queue music [dark_intro, dark_verse]

    "The next day, you enter the classroom and sit next to [classmate.name], who is still in a good mood."

    show classmate surprised at left
    pause 0.8
    show classmate smile at left, flip

    player "Hey [classmate.name], how’s it going?"
    classmate "Pretty good! How about you?"

    menu:
        "Good as well!":
            $ affection += 1
            classmate "Great to hear!"

        "Could be better.":
            $ affection -= 1
            show classmate surprised at left, flip
            classmate "Oh, anything you want to talk about?"

    show teacher normal at scale(0.6), right
    with moveinright

    teacher "Class is starting.{w=0.2} Today we’re going to learn about the magical number seven plus or minus two."

    stop music fadeout 4

    jump after_class_2

label after_class_2:
    queue music sad1_intro
    queue music sad1_verse

    scene bg school
    with fade

    "You find yourself strolling with [classmate.name] after class."

    show classmate smile
    with dissolve

    player "Need help with any subjects?"
    classmate "Actually, yes. I’m struggling with our psychology assignment."

    menu:
        "You need to spend more time studying.":
            $ affection -= 1

            classmate embarrassed "Even that might not be enough."
            "You and [classmate.name] walk away anxiously."

            scene black
            with fade

            "You go home and study for a bit before heading to bed."

            stop music fadeout 4

            jump personality_test_agreeableness

        "Want to create flashcards together?":
            $ affection += 2

            classmate surprised "That’s a great idea!"

            jump after_class_2_study

label after_class_2_study:
    stop music fadeout 4

    scene bg library
    with fade

    play music sad9_intro
    queue music [sad9_verse, sad9_hook]

    show classmate smile at flip
    with dissolve

    "You and [classmate.name] begin making flashcards to study for the upcoming assignment on memory."

    player "I believe in us. We got this. Okay, which one is first?"

    classmate "Let’s see...{w=0.2} How’s this for our first flashcard."

    menu:
        classmate "{i}Semantic memory{/i} is the component of long-term memory responsible for storing general world knowledge."

        "True":
            classmate "That’s correct!"

        "False":
            classmate surprised "No, that’s false.{w=0.1} Let’s go over that again later."

    classmate smile "Okay,{w=0.1} here’s the next one."

    menu:
        "What are the three stages in the learning and memory process?"

        "Encoding, dispersal, and retrieval.":
            classmate surprised "That’s incorrect.{w=0.2} The three stages are: {i}encoding{/i}, {i}storage{/i}, and {i}retrieval{/i}."

        "Encoding, storage, and retrieval.":
            classmate "That’s correct!{w=0.2} The three stages are: {i}encoding{/i}, {i}storage{/i}, and {i}retrieval{/i}."

        "Encoding, decoding, and formation.":
            classmate surprised "That’s incorrect.{w=0.2} The three stages are: {i}encoding{/i}, {i}storage{/i}, and {i}retrieval{/i}."

    classmate smile "How about this one?"

    menu:
        "A memory-enhancing strategy, called {i}elaborative rehearsal{/i}, is a type of memory rehearsal that is useful in transferring information into long-term memory."

        "True":
            classmate "Correct, you’re doing well!"

        "False":
            classmate surprised "The correct answer is true."

    show classmate smile

    "You and [classmate.name] spend a few more hours at the library before leaving feeling productive."

    stop music fadeout 4

    jump personality_test_agreeableness
