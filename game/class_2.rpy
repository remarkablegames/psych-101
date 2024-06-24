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

    scene bg uni
    with dissolve

    queue music "sad1_intro.ogg"
    queue music "sad1_verse.ogg"

    "You find yourself strolling with [classmate.name] after class."

    show classmate smile
    with dissolve

    player "Need help with any subjects?"
    classmate "Actually, yes. I’m struggling a bit with our psychology assignment."

    menu:
        "You’re doing great, [classmate.name]. Keep it up!":
            $ affection += 1
            classmate "Thanks, [player_name]. Your support means a lot."

        "I find that making flashcards helps. Maybe we can create some together?":
            $ affection -= 1
            classmate "That’s a great idea!"

    stop music fadeout 4

    jump personality_test_agreeableness
