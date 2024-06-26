label bad_ending:
    stop music fadeout 1
    play sound piano_oneshot volume 0.5

    player "A chill runs down your spine." with hpunch

    scene bg funeral
    with fade

    play music sad3_verse

    "You stand alone at a grave, holding a bouquet of flowers."

    player "I brought you flowers."
    player "I’m sorry I wasn’t there for you."
    player "I promise I won’t let it happen to anyone else."

    queue music sad3_hook

    "You place the flowers on the grave,{w=0.1} tears streaming down your face."
    "You vow to take the lessons to heart and support others in need."

    scene black
    with dissolve

    # Put message on why it's important to listen. Add suicide facts, maybe suicide hotline.
    # Ask the player if maybe they could have done something different.

    "{b}Bad Ending{/b}." 

    return
