default extrovert = 0
default agreeable = 0

label personality_test_extraversion:
    queue music "lofi_verse.ogg"

    teacher "I’m going to ask you a few questions. This will help me understand you better."

    menu:
        "Go for it!":
            pass
        "Uh... sure?":
            pass

    teacher "It’s Friday night and raining. What are you thinking?"
    menu:
        "Let’s go out, spending the night inside would be a waste!":
            $ extrovert += 1
        "What a perfect excuse to cancel plans and stay at home!":
            $ extrovert -= 1

    teacher "Interesting. Next question."

    teacher "You’re at a coffee shop. The only available seat is in front of a stranger."
    menu:
        "That’s okay, I can make some chit-chat.":
            $ extrovert += 1
        "I’ll down my drink and then head out.":
            $ extrovert -= 1

    show teacher happy at scale(0.6), center
    teacher "Thanks for answering my questions."

    if extrovert > 0:
        teacher "Based on my analysis, you’re an {b}extrovert{/b}."
        teacher "Conversation is your finest skill. You don’t know what awkward situations are, or how they happen to people."

    elif extrovert < 0:
        teacher "Based on my analysis, you’re an {b}introvert{/b}."
        teacher "Solitude and silence are what you long for. Books, films, and music may be your best friends, along with your neighbor’s cat."

    else:
        teacher "Based on my analysis, you’re an {b}ambivert{/b}."
        teacher "A social chameleon. Your mood changes with the seasons. Your indecisiveness makes you alluring."

    show teacher smile at scale(0.6), center

    teacher "Thanks for your honesty."
    teacher "Remember that knowing yourself is half the battle."

    show teacher happy at scale(0.6), center

    teacher "See you later in class."

    stop music fadeout 4

    jump class_1

label personality_test_agreeableness:
    queue music "lofi_verse.ogg"

    scene bg uni
    with fade

    "I see my psychology teacher walking up to me..."

    show teacher neutral at scale(0.6), center
    with dissolve

    teacher "I’m going to ask you a few questions. This will help me understand you better."

    show teacher smile at scale(0.6), center

    menu:
        "Sounds good!":
            pass

    teacher "If a new person joined your group of friends for dinner, what would you do?"
    menu:
        "Make the new person feel at ease.":
            $ agreeable += 1
        "Leave the new person alone.":
            $ agreeable -= 1

    teacher "Interesting. Next question."

    teacher "If a colleague wanted to discuss life problems with you, what would you do?"
    menu:
        "Take the time to sympathize with your friend.":
            $ agreeable += 1
        "Change the topic since you’re not interested.":
            $ agreeable -= 1

    show teacher happy at scale(0.6), center
    teacher "Thanks for answering my questions."

    if agreeable > 0:
        teacher "You scored highly on {b}agreeableness{/b}."
        teacher "You adjust your behavior to suit others.{w=0.8} Agreeable people are generally friendly, polite, and cooperative."

    elif agreeable < 0:
        teacher "You scored lowly on {b}agreeableness{/b}."
        teacher "You tend to put yourself first and “tell it like it is.”{w=0.8} You also have a more competitive nature."

    else:
        teacher "You scored so-so on {b}agreeableness{/b}."
        teacher "You change your actions depending on the situation.{w=0.8} You have a realistic balance between selfish and selfless behavior."

    teacher "Thanks for your honesty."
    teacher "Learning how to interact with others is key to subsisting in society."
    show teacher happy at scale(0.6), center

    teacher "See you later in class."

    stop music fadeout 4

    jump after_class_2
