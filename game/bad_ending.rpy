label bad_ending:
    if affection < 0:
        show teacher sadder at scale(0.6), center

    show teacher sadder at scale(0.6), center

    teacher "I don’t know how to say this, but unfortunately, one of our classmates took her own life last night."
    player "(thinking) No, it can’t be her. Please don’t be her."
    teacher "For the privacy of the individual, we’re currently not able to say who it was. But please be respectful for the time being."
    player "A chill runs down your spine."

    scene bg meadow
    with dissolve

    "In the final scene, you stand alone at a grave, holding a bouquet of flowers."
    player "I brought you flowers. I’m sorry I wasn’t there for you. I promise, I won’t let it happen to anyone else. I promise."
    "You place the flowers on the grave, tears streaming down your face, vowing to take the lessons learned to heart and support others in need."

    scene black
    with dissolve
#Put message on why it's important to listen. Add suicide facts, maybe suicide hotline. 
#Ask the player if maybe they could have done something different. 
    "{b}Bad Ending{/b}." 

    return