# Declare characters used by this game.
define classmate = Character("Alex", color="#bb8493")
define player = Character("[player_name]", color="#c8c8ff")
define teacher = Character("Teacher", color="#faf0e6")

# Variables.
default affection = 0

# Transforms.
transform halfsize: 
    zoom 0.5

# The game starts here.
label start:
    "I see a cute girl walking up to me..."

    # Show a background.
    scene bg uni
    with fade

    # Show a character sprite.
    show teacher neutral 1 at halfsize, center
    with dissolve

    # Ask player for name.
    python:
        player_name = renpy.input("Hi there! What's your name?", length=32)
        player_name = player_name.strip()

        if not player_name:
            player_name = "Player"
            affection -= 1
        else:
            affection += 1

    show teacher smile at halfsize, center

    # Display lines of dialogue.
    teacher "Nice to meet you, [player_name]! Today, we're going to go through a few questions to understand how you're feeling. This will help us support you better."
    teacher "Let's start. On a scale of 1 to 10, how often do you feel anxious or worried?"

    # This is where we will put in the Myers-Briggs test
    teacher "Great, thank you for your honesty. This will help us understand your needs. Remember, it's important to take care of your mental health just as you would your physical health."

    scene bg lecturehall
    with dissolve

    show classmate sad at left

    player "Hey Alex, you okay? You seem a bit off today."
    classmate "(sighs) Just dealing with some stuff. It's been a tough week."
    player "If you need to talk, I'm here for you."
    classmate "Thanks. I appreciate it."

    menu:
        "Good ending.":
            $ affection += 1 
            jump good_ending

        "Bad ending.":
            $ affection -= 1
            jump bad_ending

label good_ending:
    if affection > 0:
        show classmate smile
        "Affection: [affection]"

    scene black
    with dissolve

    "{b}Good Ending{/b}."

    return

label bad_ending:
    if affection < 0:
        show classmate sad
        "Affection: [affection]"

    scene black
    with dissolve

    "{b}Bad Ending{/b}."

    return
