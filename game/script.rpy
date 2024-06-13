# Declare characters used by this game.
define alex = Character("Alex", color="#c8ffc8")
define player = Character("[player_name]", color="#c8c8ff")

# Variables.
default affection = 0

# The game starts here.
label start:
    "I see a cute girl walking up to me..."

    # Show a background.
    scene bg uni
    with fade

    # Show a character sprite.
    show sylvie blue normal
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

    show sylvie blue giggle

    # Display lines of dialogue.
    alex "Nice to meet you, [player_name]!"
    alex "[player_name], do you want the good or bad ending?"

    menu:
        "Good ending.":
            $ affection += 1
            show sylvie blue smile
            jump good_ending

        "Bad ending.":
            $ affection -= 1
            show sylvie blue surprised
            jump bad_ending

label good_ending:
    if affection > 0:
        "Affection: [affection]"

    scene black
    with dissolve

    "{b}Good Ending{/b}."

    return

label bad_ending:
    if affection < 0:
        "Affection: [affection]"

    scene black
    with dissolve

    "{b}Bad Ending{/b}."

    return
