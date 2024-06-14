# Declare characters used by this game.
define classmate = Character("Alex", color="#bb8493")
define player = Character("[player_name]", color="#c8c8ff")
define teacher = Character("Teacher", color="#faf0e6")

# Variables.
default affection = 0

# Transforms.
transform flip():
    xzoom -1.0

transform scale(ratio):
    zoom ratio

# The game starts here.
label start:
    "I see a cute girl walking up to me..."

    # Show a background.
    scene bg uni
    with fade

    # Show a character sprite.
    show teacher neutral at scale(0.6), center
    with dissolve

    # Ask the player for a name.
    python:
        player_name = renpy.input("Hi there! What's your name?", length=32)
        player_name = player_name.strip()

        if not player_name:
            player_name = "Player"

    show teacher smile at scale(0.6), center

    # Display lines of dialogue.
    teacher "Nice to meet you, [player_name]!"
    teacher "I'm going to ask a few questions to understand how you're feeling. This will help me support you better."
    teacher "Let's start. On a scale of 1 to 10, how often do you feel anxious or worried?"

    # This is where the player will take a Myers-Briggs test.
    teacher "Thank you for your honesty. Remember that taking care of your mental health is just as important as taking care of your physical health."

    scene bg lecturehall
    with dissolve

    show classmate sad at left
    pause 0.8
    show classmate sad at left, flip

    player "Hey Alex, you okay? You seem a bit off today."
    classmate "(sigh) Just dealing with some stuff. It's been a tough week."

    menu:
        "If you need to talk, I'm here for you.":
            $ affection += 1
            classmate "Thanks. I appreciate it."

        "We all have tough weeks, you'll get through it.":
            $ affection -= 1
            classmate "Yeah, I guess..."

    show teacher normal at scale(0.6), right

    "Class begins, but you can't help but notice Alex's distracted state. The teacher discusses the importance of mental health awareness, which resonates deeply with the you."

    scene bg club
    with dissolve

    show classmate upset at scale(0.6), right

    "Later, in the hallway, you overhear Alex talking to another student."
    classmate "(frustrated) I don't know what to do anymore. It just feels like everything is falling apart."

    menu:
        "Alex, I overheard what you were saying. Do you want to talk about it?":
            $ affection += 1
            player "Alex, I overheard what you were saying. Do you want to talk about it?"
            classmate "It's just... everything feels so heavy. My family is going through a lot, and I've been feeling really low."

        "Maybe you should try to relax and take it easy.":
            $ affection -= 1
            classmate "I wish it were that simple..."

    player "I'm really sorry to hear that. Have you considered talking to the school counselor? They might be able to help."
    classmate "Maybe... I just don't know if it will change anything."
    player "It's worth a try. Sometimes just talking to someone can make a big difference."
    classmate "Thanks. I appreciate it."

    scene bg meadow
    with dissolve

    "Later that evening, you check social media and see a post from Alex."
    classmate "Sometimes I wonder if it's all worth it. Life just feels like one big mess."

    menu:
        "Hey, I saw your post. I'm really concerned about you. Please, let's talk.":
            $ affection += 1
            classmate "..."
            classmate "Thanks for reaching out. I'm just really struggling right now."
            player "Remember what we talked about today? Maybe talking to the counselor could help. I can go with you if you want."
            classmate "Okay. Maybe tomorrow."

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
        show teacher happy at scale(0.6), center

    show teacher sadder at scale(0.6), right

    teacher "I don't know how to say this, but unfortunately, one of our classmates took her own life last night."
    player "(thinking) No, it can't be her. Please don't be her."
    teacher "For the privacy of the individual, we're currently not able to say who it was. But please be respectful for the time being."

    show classmate smile at scale(0.5), left

    classmate "I'm sorry I'm late. I had an appointment with the counselor this morning."
    player "(thinking) Thank goodness she's okay."

    scene black
    with dissolve

    "{b}Good Ending{/b}."

    return

label bad_ending:
    if affection < 0:
        show classmate sad

    scene black
    with dissolve

    "{b}Bad Ending{/b}."

    return
