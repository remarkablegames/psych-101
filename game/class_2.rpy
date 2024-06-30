label before_class_2:
    call personality_test_openness
    jump class_2

label class_2:
    scene bg lecturehall
    with dissolve

    queue music [dark_intro, dark_verse]

    "You enter the classroom and sit next to [classmate.name], who’s still in a good mood."

    show classmate surprised at left
    pause 0.8
    show classmate smile at left, flip

    player "Hey [classmate.name], how’s it going?"
    classmate "Pretty good! How about you?"

    menu:
        "Good as well!":
            $ affection += 1
            classmate "Great to hear!"
            player "Are you excited for today’s class?"
            classmate "Yep, I’m looking forward to learning how to improve my memory."
            player "Nice, this stuff will come useful during finals."
            classmate "Agreed."

        "Could be better.":
            classmate surprised "Oh, anything you want to talk about?"
            player "So-"

    show classmate smile at left, scale(0.8)
    with dissolve

    show teacher talking at scale(0.6), right
    with moveinright

    teacher "Class is starting.{w=0.2} Today we’re going to learn about the magical number 7 plus or minus 2."

    stop music fadeout 2

    jump after_class_2

label after_class_2:
    queue music sad1_intro
    queue music sad1_verse

    scene bg uni
    with fade

    "You find yourself strolling with [classmate.name] after class."

    show classmate smile
    with dissolve

    player "Need help with any subjects?"
    classmate "Actually, yes.{w=0.2} I’m struggling with our psychology assignment."

    menu:
        "Tell her that she’s not studying enough.":
            $ affection -= 1

            player "You have to study more."
            classmate embarrassed "I hear you, but even that might not be enough."
            player "I know, but there’s a correlation between how much time you study and your overall grades."
            classmate "..."
            player "Alright, I’m going to head home and study."
            "You and [classmate.name] walk away anxiously."

            jump after_class_2_home

        "Ask her if she wants to make flashcards.":
            $ affection += 1

            player "Want to create flashcards together?"
            classmate surprised "That’s a great idea!"
            player "Let’s head to the library then."

            jump after_class_2_study

label after_class_2_study:
    stop music fadeout 2

    scene bg library
    with fade

    play music sad9_intro
    queue music [sad9_verse, sad9_hook]

    show classmate smile at flip
    with dissolve

    "You and [classmate.name] begin making flashcards to study for the upcoming assignment on memory."

    player "Alright, we got this.{w=0.2} Let’s go over the first one."

    classmate "Let’s see...{w=0.2} How’s this for our first flashcard."

    menu:
        classmate "{i}Semantic memory{/i} is the component of long-term memory responsible for storing general world knowledge."

        "True":
            classmate "That’s correct!"

        "False":
            classmate surprised "No, that’s incorrect."
            classmate "Semantic memory {i}is{/i} the component of long-term memory responsible for storing general world knowledge."

    classmate smile "Here’s the next one."

    menu:
        "What are the 3 stages in the learning and memory process?"

        "Encoding, dispersal, and retrieval.":
            classmate surprised "That’s incorrect."
            classmate "The 3 stages are: {i}encoding{/i}, {i}storage{/i}, and {i}retrieval{/i}."

        "Encoding, storage, and retrieval.":
            classmate "That’s correct!"

        "Encoding, decoding, and formation.":
            classmate surprised "That’s incorrect."
            classmate "The 3 stages are: {i}encoding{/i}, {i}storage{/i}, and {i}retrieval{/i}."

    classmate smile "How about this one?"

    menu:
        "A memory-enhancing strategy, called {i}elaborative rehearsal{/i}, is a type of memory rehearsal that’s useful in transferring information into long-term memory."

        "True":
            classmate "Correct!"

        "False":
            classmate surprised "That’s incorrect."
            classmate "Elaborative rehearsal {i}is{/i} a type of memory rehearsal that’s useful in transferring information into long-term memory."

    show classmate smile

    "You and [classmate.name] spend a few more hours at the library before leaving feeling productive."

    stop music fadeout 2
    jump after_class_2_home

label after_class_2_home:
    play music sad8_outro fadein 1

    scene black
    with fade

    "You went home and studied some more before going to bed."
    "You look forward to tomorrow’s psych class."

    stop music fadeout 2
    jump before_class_3
