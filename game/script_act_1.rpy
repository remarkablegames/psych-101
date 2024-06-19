label act_1:
    scene bg lecturehall
    with dissolve

    show classmate smile at left
    pause 0.8
    show classmate smile at left, flip

    player "Hey, looks like we’re going to be seatmates."
    classmate "Yeah, seems like it! I’m Alex, nice to meet you."

    menu:
        "Nice to meet you too!":
            $ affection += 1
            classmate "I think we’ll get along just fine."

        "This teacher definitely has mental health problems!":
            $ affection -= 1
            classmate "(laughs) I know, right?"

    "You and Alex start making small talk and quickly become friends."

    scene bg uni
    with dissolve

    show classmate smile at left

    player "How are you feeling now, Alex?"
    classmate "Pretty good! Just trying to keep up with everything."

    menu:
        "Let’s take a break and grab a snack.":
            $ affection += 1
            classmate "That sounds nice. Thanks for suggesting it."

        "Maybe diving into our studies will help distract you.":
            $ affection -= 1
            classmate "Yeah, maybe. It’s hard to concentrate, though."

    scene bg club
    with dissolve

    show classmate smile at left

    player "What do you feel like having? My treat."
    classmate "I think I’ll have a hot chocolate. Thanks!"

    menu:
        "So, what do you like to do in your free time?":
            $ affection += 1
            classmate "I enjoy reading and painting. It’s a good way to relax."

        "My goodness, this world is so depressing.":
            $ affection -= 1
            classmate "It definitely is."

    "As you spend more time with Alex, you notice her mood is generally upbeat and positive. She starts to smile more often."

    scene bg meadow
    with dissolve

    player "Hey Alex, want to join me for a walk in the park this weekend?"
    classmate "Sure, that sounds nice."

    "You and Alex enjoy the fresh air and the beauty of nature. Alex seems to relax more as you walk together."

    classmate "Thanks for inviting me. This is really nice."
    player "I'm glad you're enjoying it."

    show classmate smile at left

    "You and Alex find a bench and sit down to rest for a while."

    menu:
        "Have you thought about what you want to do in the future?":
            $ affection += 1
            player "Have you thought about what you want to do in the future?"
            classmate "I have some ideas, but I’m not sure yet. How about you?"

        "You text your friends to see what they’re doing.":
            $ affection -= 1
            player "(You text your friends to see what they’re doing.)"
            classmate "Oh, are you bored? We can leave."

    scene bg lecturehall
    with dissolve

    "The next day, you enter the classroom and sit next to Alex, who is still in a good mood."

    player "Hey Alex, how’s it going?"
    classmate "Pretty good, thanks! How about you?"

    menu:
        "I’m doing well, thanks!":
            $ affection += 1
            classmate "Great to hear!"

        "Could be better.":
            $ affection -= 1
            classmate "Oh, anything you want to talk about?"

    "Class begins, and the teacher discusses the importance of mental health awareness. You notice Alex paying attention and taking notes."

    scene bg uni
    with dissolve

    show classmate smile at left

    player "Need help with any subjects?"
    classmate "Actually, yes. I'm struggling a bit with our psychology assignment."

    menu:
        "You’re doing great, Alex. Keep it up!":
            $ affection += 1
            classmate "Thanks, [player_name]. Your support means a lot."

        "I find that making flashcards helps. Maybe we can create some together?":
            $ affection -= 1
            classmate "That’s a great idea!"

    scene bg club
    with dissolve

    show classmate smile at left

    player "How about we get something to drink? My treat."
    classmate "That sounds nice. Thanks."

    menu:
        "Talk about hobbies.":
            $ affection += 1
            player "So, what do you like to do in your free time?"
            classmate "I enjoy reading and painting. It's a good way to relax."

        "Complain about the news.":
            $ affection -= 1
            player "My goodness, this world is so depressing."
            classmate "It definitely is."

    "As you spend more time with Alex, you notice her mood improving slightly. She starts to smile more often."

    scene bg meadow
    with dissolve

    player "Hey Alex, want to join me for a walk in the park this weekend?"
    classmate "Sure, that sounds nice."

    "You and Alex enjoy the fresh air and the beauty of nature. Alex seems to relax more as you walk together."

    classmate "Thanks for inviting me. This is really nice."
    player "I'm glad you're enjoying it."

    show classmate smile at left

    "You and Alex find a bench and sit down to rest for a while."

    menu:
        "Have you thought about what you want to do in the future?":
            $ affection += 1
            player "Have you thought about what you want to do in the future?"
            classmate "I have some ideas, but I'm not sure yet. How about you?"

        "You text your friends to see what they’re doing.":
            $ affection -= 1
            player "(You text your friends to see what they’re doing.)"
            classmate "Oh, are you bored? We can leave."

    "Over the next few days, you continue to hang out with Alex, who remains upbeat and positive."

    scene bg lecturehall
    with dissolve

    "One day, you notice Alex is a bit quieter than usual."

    player "Hey Alex, you seem a bit off today. Everything okay?"
    classmate "{i}(sigh){/i} Just dealing with some stuff. It’s been a tough week."

    menu:
        "If you need to talk, I’m here for you.":
            $ affection += 1
            classmate "Thanks. I appreciate it."

        "We all have tough weeks, you’ll get through it.":
            $ affection -= 1
            classmate "Yeah, I guess..."

    "Class begins, but you can’t help but notice Alex’s distracted state. The teacher discusses the importance of mental health awareness, which resonates deeply with you."

    scene bg uni
    with dissolve

    "Later that day, you and Alex decide to study together."

    show classmate sad at left

    player "How are you feeling now, Alex?"
    classmate "Not great, honestly. This week has been really hard."

    menu:
        "Let’s take a break and grab a snack.":
            $ affection += 1
            classmate "That sounds nice. Thanks for suggesting it."

        "Maybe diving into our studies will help distract you.":
            $ affection -= 1
            classmate "Yeah, maybe. It’s hard to concentrate, though."

    scene bg club
    with dissolve

    show classmate sad at left

    player "What do you feel like having? My treat."
    classmate "I think I’ll have a hot chocolate. Thanks."

    menu:
        "So, what do you like to do in your free time?":
            $ affection += 1
            classmate "I enjoy reading and painting. It’s a good way to relax."

        "My goodness, this world is so depressing.":
            $ affection -= 1
            classmate "It definitely is."

    "As you spend more time with Alex, you notice her mood improving slightly, but she still seems troubled."

    scene bg meadow
    with dissolve

    player "Hey Alex, want to join me for a walk in the park this weekend?"
    classmate "Sure, that sounds nice."

    "You and Alex enjoy the fresh air and the beauty of nature. Alex seems to relax more as you walk together."

    classmate "Thanks for inviting me. This is really nice."
    player "I'm glad you're enjoying it."

    show classmate smile at left

    "You and Alex find a bench and sit down to rest for a while."

    menu:
        "Have you thought about what you want to do in the future?":
            $ affection += 1
            player "Have you thought about what you want to do in the future?"
            classmate "I have some ideas, but I’m not sure yet. How about you?"

        "You text your friends to see what they’re doing.":
            $ affection -= 1
            player "(You text your friends to see what they’re doing.)"
            classmate "Oh, are you bored? We can leave."

    jump personality_test_agreeableness
