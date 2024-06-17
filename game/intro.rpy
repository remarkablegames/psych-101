default player_age = 0

label intro:
    play music "lofi_intro.ogg" fadein 1.2

    "I see my psychology teacher walking up to me..."

    scene bg uni
    with fade

    show teacher neutral at scale(0.6), center
    with dissolve

    queue music "lofi_verse.ogg"

    # Ask for the player's name.
    python:
        player_name = renpy.input("Hi there! What’s your name?", length=32)
        player_name = player_name.strip()

        if not player_name:
            player_name = "Player"

    show teacher smile at scale(0.6), center

    teacher "Nice to meet you, [player_name]!"

    # Ask for the player's age.
    $ player_age = int(renpy.input("How old are you?", length=3, allow="0123456789"))

    if player_age < 18:
        show teacher annoyed at scale(0.6), center

        teacher "You must be 18 years or older to attend Pysch 101."

        return

    teacher "Welcome to Pysch 101!"

    jump personality_test
