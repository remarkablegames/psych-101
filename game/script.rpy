# Declare characters used by this game.
define player = Character("[player_name]", color="#c8c8ff")
define teacher = Character("Teacher", color="#c8ffc8")

# Variables.
default affection = 0

# The game starts here.
label start:
    "I see a cute girl walking up to me..."

    # Show a background.
    scene bg uni
    with fade

    # Show a character sprite.
    show teacher neutral 1
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

    show teacher smile 2

    # Display lines of dialogue.
    teacher "Nice to meet you, [player_name]!"
    teacher "[player_name], do you want the good or bad ending?"

    show teacher smile 1

    menu:
        "Good ending.":
            $ affection += 1
            jump good_ending

        "Bad ending.":
            $ affection -= 1
            jump bad_ending

label good_ending:
    if affection > 0:
        show teacher smile 4
        "Affection: [affection]"

    scene black
    with dissolve

    "{b}Good Ending{/b}."

    return

label bad_ending:
    if affection < 0:
        show teacher sad 2
        "Affection: [affection]"

    scene black
    with dissolve

    "{b}Bad Ending{/b}."

    return
