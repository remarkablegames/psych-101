label act_2:
    scene bg lecturehall
    with dissolve

    "Class begins, and you notice that Alex is not her usual self. She seems more distracted and less engaged."

    show classmate sad at left

    player "Hey Alex, you seem a bit off today. Everything okay?"
    classmate "{i}(sigh){/i} Just dealing with some stuff. It’s been a tough week."

    menu:
        "If you need to talk, I’m here for you.":
            $ affection += 1
            classmate "Thanks. I appreciate it."

        "We all have tough weeks, you’ll get through it.":
            $ affection -= 1
            classmate "Yeah, I guess..."

    scene bg uni
    with dissolve

    "After class, you and Alex decide to study together in the library."

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
            $ affection -= 2
            classmate "It definitely is."

    "You notice that Alex is more reserved and doesn't smile as much as she used to."

    scene bg meadow
    with dissolve

    player "Hey Alex, want to join me for a walk in the park this weekend?"
    classmate "Sure, that sounds nice."

    "You and Alex enjoy the fresh air and the beauty of nature, but Alex seems quieter than usual."

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
            $ affection -= 2
            player "(You text your friends to see what they’re doing.)"
            classmate "Oh, are you bored? We can leave."

    scene bg lecturehall
    with dissolve

    "The next day in class, you notice Alex is absent. You feel a pang of worry."

    player "{i}(thinking){/i} Where is Alex? She said she’d be here today."

    scene bg uni
    with dissolve

    "Later, in the hallway, you overhear Alex talking to another student."

    show classmate sad at left

    classmate "{i}(frustrated){/i} I don’t know what to do anymore. It just feels like everything is falling apart."

    menu:
        "Alex, I overheard what you were saying. Do you want to talk about it?":
            $ affection += 1
            player "Alex, I overheard what you were saying. Do you want to talk about it?"
            classmate "It’s just... everything feels so heavy. My family is going through a lot, and I’ve been feeling really low."

        "Maybe you should try to relax and take it easy.":
            $ affection -= 2
            classmate "I wish it were that simple..."

    player "I’m really sorry to hear that. Have you considered talking to the school counselor? They might be able to help."
    classmate "Maybe... I just don’t know if it will change anything."
    player "It’s worth a try. Sometimes just talking to someone can make a big difference."
    classmate "Thanks. I appreciate it."

    scene bg uni
    with dissolve

    "Later that evening, you check social media and see a post from Alex."

    show classmate sad at left

    classmate "Sometimes I wonder if it’s all worth it. Life just feels like one big mess."

    menu:
        "Hey, I saw your post. I’m really concerned about you. Please, let’s talk.":
            $ affection += 1
            classmate "...Thanks for reaching out. I’m just really struggling right now."
            player "Remember what we talked about today? Maybe talking to the counselor could help. I can go with you if you want."
            classmate "Okay. Maybe tomorrow."

        "Ignore the post.":
            $ affection -= 2

    scene bg lecturehall
    with dissolve

    "The next day, you see Alex in class again, looking even more distressed."

    player "Hey Alex, you seemed pretty down yesterday. Are you feeling any better today?"
    classmate "Not really. It's been a really rough night."

    menu:
        "Do you want to talk about it?":
            $ affection += 1
            classmate "Thanks, [player_name]. It's just... everything feels so overwhelming right now."

        "Try to focus on the good things in life.":
            $ affection -= 2
            classmate "I wish I could, but it's hard to see any good right now."

    scene bg uni
    with dissolve

    "After class, you decide to walk with Alex."

    player "Hey Alex, want to walk together for a bit?"
    classmate "Sure, thanks."

    "You and Alex walk in silence for a while, then Alex starts talking."

    classmate "You know, it's really hard for me to open up about my problems. I've always felt like I should just deal with things on my own."

    menu:
        "It's okay to ask for help. You're not alone.":
            $ affection += 1
            classmate "I know... it's just hard to break that habit."

        "Everyone has their struggles, you’ve got this.":
            $ affection -= 1
            classmate "Thanks, [player_name]. That means a lot."

    scene bg club
    with dissolve

    "You and Alex decide to stop by a café to grab something to drink."

    player "How about we get something to drink? My treat."
    classmate "That sounds nice. Thanks."

    show classmate sad at left

    menu:
        "Talk about a fun memory.":
            $ affection += 1
            player "Remember that funny story you told me last time? It really made me laugh."
            classmate "(smiles) Yeah, that was pretty funny."

        "Ask about her family issues.":
            $ affection -= 2
            player "So, what exactly is going on with your family?"
            classmate "(frowns) It's really complicated... and stressful."

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
            $ affection -= 2
            player "(You text your friends to see what they’re doing.)"
            classmate "Oh, are you bored? We can leave."

    scene bg lecturehall
    with dissolve

    "The next day, you enter the classroom and find out that Alex is absent again. You feel a pang of worry."

    player "(thinking) Where is Alex? She said she’d be here today."

    scene bg uni
    with dissolve

    "You find Alex sitting alone in the library, looking very upset."

    show classmate sad at left

    player "Alex, I’ve been looking for you. Are you okay?"
    classmate "Not really... I just couldn’t face the class today."

    menu:
        "It’s okay to have bad days. Do you want to talk about it?":
            $ affection += 1
            classmate "Thanks, [player_name]. It just feels like everything is too much right now."

        "You can’t keep skipping classes. It will only make things worse.":
            $ affection -= 2
            classmate "I know... I just needed some time alone."

    scene bg club
    with dissolve

    "You decide to take Alex to the café again to help her relax."

    player "How about we get something to drink again? My treat."
    classmate "That sounds nice. Thanks."

    show classmate sad at left

    menu:
        "Talk about a fun memory.":
            $ affection += 1
            player "Remember when we went to the park? That was a really nice day."
            classmate "(smiles) Yeah, it was."

        "Ask about her struggles again.":
            $ affection -= 2
            player "So, what exactly is going on with your family now?"
            classmate "(frowns) It's really complicated... and stressful."

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
            $ affection -= 2
            player "(You text your friends to see what they’re doing.)"
            classmate "Oh, are you bored? We can leave."

    jump personality_test_agreeableness
