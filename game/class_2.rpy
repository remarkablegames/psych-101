label class_2:
    scene bg lecturehall
    with dissolve

    queue music ["dark_intro.ogg", "dark_verse.ogg"]

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

    "Before you can say anything, class begins and the teacher discusses the importance of mental health awareness. You notice [classmate.name] paying attention and taking notes."

    stop music fadeout 4

    jump after_class_2

label after_class_2:
    queue music "sad1_intro.ogg"
    queue music "sad1_verse.ogg"

    scene bg uni
    with dissolve

    "You find yourself strolling with [classmate.name] after class."

    show classmate smile
    with dissolve

    player "Need help with any subjects?"
    classmate "Actually, yes. I’m struggling a bit with our psychology assignment."

    menu:
        "It's definitely a tough one. We'll need all the luck we can get.":
            $ affection -= 1
            classmate "Even that might not be enough."
            "You and [classmate.name] walk away anxiously."

        "I find that making flashcards helps. Maybe we can create some together?":
            $ affection += 2
            classmate "That’s a great idea!"

            jump after_class_2_study

label after_class_2_study:
    stop music fadeout 4

    play music "sad9_intro.ogg"
    queue music ["sad9_verse.ogg", "sad9_hook.ogg"]

    scene black

    "You and [classmate.name] begin making flash cards to study for the upcoming assignment on memory."

    player "I believe in us. We've got this. Okay, which one is first?"

    classmate "Let's see... How's this for our first flashcard:{w=0.3} Semantic memory{w=0.3} is the component of long-term memory{w=0.3} responsible for storing general world knowledge."
    menu:
        "True":
            classmate "That's correct!"

        "False":
            classmate "No, that's false.{w=0.1} Let's go over that again later."
    
    classmate "Okay, here's the next one: Psychologists distinguish between three necessary stages in the learning and memory process:{w=0.3} encoding,{w=0.3} dispersal,{w=0.3} and retrieval."
    menu:
        "True":
            classmate "That's false.{w=0.3} The three stages are encoding,{w=0.3} storage,{w=0.3} and retrieval."

        "False":
            classmate "Correct. Well done!{w=0.3} The three stages are encoding,{w=0.3} storage,{w=0.3} and retrieval."

    classmate "How about this one... Ready?"
    classmate "A memory-enhancing strategy,{w=0.3} called elaborative rehearsal,{w=0.3} is a type of memory rehearsal that is useful in transferring information into long-term memory."
    menu:
        "True":
            classmate "Correct. You're doing well!"

        "False":
            classmate "This one is true."
    
    "You and [classmate.name] left the library after a few hours, drained, but feeling productive."

    stop music fadeout 4

    jump personality_test_agreeableness
