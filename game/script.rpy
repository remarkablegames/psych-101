# Declare characters used by this game.
define player = Character("[player_name]", color="#c8c8ff")
define teacher = Character("Teacher", color="#c8ffc8")

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

    show teacher neutral at halfsize, left

    player "Hey Alex, you okay? You seem a bit off today."
    teacher "(sighs) Just dealing with some stuff. It's been a tough week."

    menu:
        "If you need to talk, I'm here for you.":
            $ affection += 1
            player "If you need to talk, I'm here for you."
            teacher "Thanks. I appreciate it."

        "We all have tough weeks, you'll get through it.":
            $ affection -= 1
            player "We all have tough weeks, you'll get through it."
            teacher "Yeah, I guess..."


    show teacher neutral at halfsize, right

    "Class begins, but you can't help but notice Alex's distracted state. The teacher discusses the importance of mental health awareness, which resonates deeply with the you."

    scene bg club
    with dissolve

    show teacher frustrated at halfsize, left

    "Later, in the hallway, you overhear Alex talking to another student."
    teacher "(frustrated) I don't know what to do anymore. It just feels like everything is falling apart."

    show player neutral at halfsize, right

    menu:
        "Alex, I overheard what you were saying. Do you want to talk about it?":
            $ affection += 1
            player "Alex, I overheard what you were saying. Do you want to talk about it?"
            teacher "It's just... everything feels so heavy. My family is going through a lot, and I've been feeling really low."

        "Maybe you should try to relax and take it easy.":
            $ affection -= 1
            player "Maybe you should try to relax and take it easy."
            teacher "I wish it were that simple..."

    player "I'm really sorry to hear that. Have you considered talking to the school counselor? They might be able to help."
    teacher "Maybe... I just don't know if it will change anything."
    player "It's worth a try. Sometimes just talking to someone can make a big difference."
    teacher "Thanks. I appreciate it."

    scene bg meadow
    with dissolve

    "Later that evening, you check social media and see a post from Alex."
    teacher "Sometimes I wonder if it's all worth it. Life just feels like one big mess."

    menu:
        "Hey, I saw your post. I'm really concerned about you. Please, let's talk.":
            $ affection += 1
            player "Hey, I saw your post. I'm really concerned about you. Please, let's talk."
            teacher "(after a pause) Thanks for reaching out. I'm just really struggling right now."
            player "Remember what we talked about today? Maybe talking to the counselor could help. I can go with you if you want."
            teacher "Okay. Maybe tomorrow."

        "Ignore the post.":
            $ affection -= 1
    
    scene bg lecturehall
    with dissolve

    "You get to class the next day and notice that Alex is absent. The room feels tense."
    player "(thinking) Where is Alex? She said she'd be here today."

    if affection > 0:
        jump good_ending
    else:
        jump bad_ending

label good_ending:
    if affection > 0:
        show teacher smile at halfsize, center
        "Affection: [affection]"
    show teacher sad at halfsize, right

    teacher "I don't know how to say this, but unfortunately, one of our classmates took her own life last night."
    player "(thinking) No, it can't be her. Please don't be her."
    teacher "For the privacy of the individual, we're currently not able to say who it was. But please be respectful for the time being."

    show teacher tired at halfsize, left

    teacher "I'm sorry I'm late. I had an appointment with the counselor this morning."
    player "(thinking) Thank goodness she's okay."

label bad_ending:
    if affection < 0:
        show teacher sad 2 at halfsize, center
        "Affection: [affection]"

    scene black
    with dissolve

    "{b}Bad Ending{/b}."

    return