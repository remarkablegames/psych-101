label personality_test_intro(start=False):
    if not start:
        queue music "lofi_verse.ogg"

        scene bg uni
        with fade

        "I see my psychology teacher walking up to me..."

        show teacher neutral at scale(0.6), center
        with dissolve

    teacher "I’m going to ask you a few questions so I can understand you better."

    show teacher smile at scale(0.6), center

    menu:
        "Let’s do it!":
            pass

    return

default extrovert = 0

label personality_test_extraversion:
    call personality_test_intro(start=True)

    teacher "It’s Friday night and raining.{w=0.2} What are you thinking?"
    menu:
        "Let’s go out, spending the night inside would be a waste!":
            $ extrovert += 1
        "What a perfect excuse to cancel plans and stay at home!":
            $ extrovert -= 1

    teacher "Interesting.{w=0.2} Next question."

    teacher "You’re at a coffee shop.{w=0.2} The only available seat is in front of a stranger."
    menu:
        "That’s okay, I can make some chit-chat.":
            $ extrovert += 1
        "I’ll down my drink and then head out.":
            $ extrovert -= 1

    show teacher happy at scale(0.6), center
    teacher "Thanks for answering my questions."

    if extrovert > 0:
        teacher "Based on my analysis,{w=0.2} you’re an {b}extrovert{/b}."
        teacher "Conversation is your finest skill.{w=0.2} You don’t know what awkward situations are,{w=0.1} or how they happen to people."

    elif extrovert < 0:
        teacher "Based on my analysis,{w=0.2} you’re an {b}introvert{/b}."
        teacher "Solitude and silence are what you long for.{w=0.2} Books, films, and music may be your best friends,{w=0.1} along with your neighbor’s cat."

    else:
        teacher "Based on my analysis,{w=0.2} you’re an {b}ambivert{/b}."
        teacher "A social chameleon.{w=0.2} Your mood changes with the seasons.{w=0.2} Your indecisiveness makes you alluring."

    show teacher smile at scale(0.6), center

    teacher "I appreciate your honesty."
    teacher "Remember that knowing yourself is half the battle."

    show teacher happy at scale(0.6), center

    teacher "See you later in class."

    stop music fadeout 4

    jump class_1

default agreeable = 0

label personality_test_agreeableness:
    call personality_test_intro

    teacher "If a new person joined your group of friends for dinner,{w=0.2} what would you do next?"
    menu:
        "Make the new person feel at ease.":
            $ agreeable += 1
        "Let the new person figure things out.":
            $ agreeable -= 1

    teacher "Interesting.{w=0.2} Next question."

    teacher "If a colleague wanted to discuss life problems with you,{w=0.2} what’s your response?"
    menu:
        "Take the time to sympathize with your friend.":
            $ agreeable += 1
        "Change the subject.":
            $ agreeable -= 1

    show teacher happy at scale(0.6), center
    teacher "Thanks for answering my questions."

    if agreeable > 0:
        teacher "You scored high on {b}agreeableness{/b}."
        teacher "You adjust your behavior to suit others.{w=0.2} Agreeable people are generally friendly, polite, and cooperative."

    elif agreeable < 0:
        teacher "You scored low on {b}agreeableness{/b}."
        teacher "You tend to put yourself first and “tell it like it is.”{w=0.2} You also have a more competitive nature."

    else:
        teacher "You scored so-so on {b}agreeableness{/b}."
        teacher "You change your actions depending on the situation.{w=0.2} You have a realistic balance between selfish and selfless behavior."

    teacher "I appreciate your honesty."
    teacher "Learning how to interact with others is key to subsisting in society."
    show teacher happy at scale(0.6), center

    teacher "See you later in class."

    stop music fadeout 4

    jump class_3

default conscientious = 0

label personality_test_conscientiousness:
    call personality_test_intro

    teacher "When it comes to chores,{w=0.2} what do you tend to do?"
    menu:
        "Get them done right away.":
            $ conscientious += 1
        "Avoid doing them if possible.":
            $ conscientious -= 1

    teacher "Interesting.{w=0.2} Next question."

    teacher "After taking something out of the drawer,{w=0.2} what do you do once you’re done with it?"
    menu:
        "I would put it back in its proper place.":
            $ conscientious += 1
        "I would leave it lying around.":
            $ conscientious -= 1

    show teacher happy at scale(0.6), center
    teacher "Thanks for answering my questions."

    if conscientious > 0:
        teacher "You scored high on {b}conscientiousness{/b}."
        teacher "You’re organized and responsible.{w=0.2} Conscientiousness people tend to follow rules and prefer clean homes."

    elif conscientious < 0:
        teacher "You scored low on {b}conscientiousness{/b}."
        teacher "You’re laid back and don’t take obligations too seriously.{w=0.2} Procrastination is part of who you are."

    else:
        teacher "You scored in the middle on {b}conscientiousness{/b}."
        teacher "You can be productive if you’re motivated.{w=0.2} Setting clear goals is the key to success."

    teacher "I appreciate your honesty."
    teacher "Understanding our desires influences how we approach tasks."
    show teacher happy at scale(0.6), center

    teacher "See you later in class."

    stop music fadeout 4

default open = 0

label personality_test_openness:
    call personality_test_intro

    teacher "What’s your thoughts on abstract ideas?"
    menu:
        "I’m interested in abstract ideas.":
            $ open += 1
        "I have difficulty understanding abstract ideas.":
            $ open -= 1

    teacher "Interesting.{w=0.2} Next question."

    teacher "How would you describe your speech?"
    menu:
        "I have a rich vocabulary.":
            $ open += 1
        "I avoid difficult words.":
            $ open -= 1

    show teacher happy at scale(0.6), center
    teacher "Thanks for answering my questions."

    if open > 0:
        teacher "You’re {b}open{/b} to experiences."
        teacher "You’re a daydreamer who seeks new experiences and intellectual pursuits.{w=0.2} Curious about the world, you’re eager to learn new things."

    elif open < 0:
        teacher "You’re {b}closed{/b} to experiences."
        teacher "You’re down to earth and prefer familiar routines to new experiences.{w=0.2} You tend to be conventional with a narrower range of interests."

    else:
        teacher "You’re somewhat {b}open{/b} to experiences."
        teacher "You keep an open mind and are realistic about new things.{w=0.2} You find a happy medium between creativity and traditional thinking."

    teacher "I appreciate your honesty."
    teacher "Openness to experience can lead to new ways of thinking."
    show teacher happy at scale(0.6), center

    teacher "See you later in class."

    stop music fadeout 4

    jump class_2

default neurotic = 0

label personality_test_neuroticism:
    call personality_test_intro

    teacher "How would you describe yourself?"
    menu:
        "I get stressed out easily.":
            $ neurotic += 1
        "I’m relaxed most of the time.":
            $ neurotic -= 1

    teacher "Interesting.{w=0.2} Next question."

    teacher "How often does your mood change?"
    menu:
        "I change my mood a lot.":
            $ neurotic += 1
        "My mood stays the same.":
            $ neurotic -= 1

    show teacher happy at scale(0.6), center
    teacher "Thanks for answering my questions."

    if neurotic > 0:
        teacher "Based on my assessment, you’re {b}neurotic{/b}."
        teacher "You’re an emotional person and tend to experience feelings like anxiety and worry."

    elif neurotic < 0:
        teacher "Based on my assessment, you’re {b}not neurotic{/b}."
        teacher "You’re emotionally stable and less reactive to stress."

    else:
        teacher "Based on my assessment, you’re {b}somewhat neurotic{/b}."
        teacher "You’re someone who may be affected by emotions depending on the circumstances."

    teacher "I appreciate your honesty."
    teacher "Too much of anything is bad for you,{w=0.1} so learning how to deal with one’s emotions is important for one’s mental health."
    show teacher happy at scale(0.6), center

    teacher "See you later in class."

    stop music fadeout 4

    jump before_class_4
