default extrovert = 0
default introvert = 0

label personality_test:
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
            $ introvert += 1

    teacher "Interesting. Next question."

    teacher "You’re at a coffee shop. The only available seat is in front of a stranger."
    menu:
        "That’s okay, I can make some chit-chat.":
            $ extrovert += 1
        "I’ll down my drink and then head out.":
            $ introvert += 1

    show teacher happy at scale(0.6), center
    teacher "Thanks for answering my questions."

    if extrovert > introvert:
        teacher "Based on my analysis, you’re an {b}extrovert{/b}."
        teacher "Conversation is your finest skill. You don’t know what awkward situations are, or how they happen to people."

    elif extrovert < introvert:
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

    jump act_1
