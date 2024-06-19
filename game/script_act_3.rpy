label act_3:
    scene bg lecturehall
    with dissolve

    "Class begins, and you notice that Alex is even more withdrawn. She barely speaks and looks exhausted."

    show classmate sad at left

    player "Hey Alex, you don’t look so good. Everything okay?"
    classmate "Not really. I’ve been having a really hard time lately."

    menu:
        "Do you want to talk about it?":
            $ affection += 1
            classmate "I don’t know if it will help, but thanks for offering."

        "Maybe you should try to get some rest.":
            $ affection -= 2
            classmate "I wish it were that simple..."

    scene bg uni
    with dissolve

    "After class, you find Alex sitting alone in the library, looking very upset."

    show classmate sad at left

    player "Alex, I’m really worried about you. Are you sure you’re okay?"
    classmate "No, I’m not okay. I feel like I’m falling apart."

    menu:
        "It’s okay to feel this way. Have you thought about talking to someone?":
            $ affection += 1
            classmate "I have, but I’m scared it won’t help."

        "You need to pull yourself together. Skipping classes won’t help.":
            $ affection -= 2
            classmate "I know... I just don’t have the energy."

    scene bg club
    with dissolve

    "Later that evening, you check social media and see another concerning post from Alex."

    show classmate sad at left

    classmate "Sometimes I feel like there’s no point to anything. Everything is just so overwhelming."

    menu:
        "Hey, I saw your post. I’m really worried about you. Please, let’s talk.":
            $ affection += 1
            classmate "...Thanks for reaching out. I’m just really struggling right now."
            player "Remember what we talked about? Maybe talking to the counselor could help. I can go with you if you want."
            classmate "Okay. Maybe tomorrow."

        "Ignore the post.":
            $ affection -= 3

    scene bg lecturehall
    with dissolve

    "The next day, you see Alex in class, but she looks even more distressed than before."

    player "Hey Alex, you seemed pretty down yesterday. Are you feeling any better today?"
    classmate "Not really. It’s been a really rough night."

    menu:
        "Do you want to talk about it?":
            $ affection += 1
            classmate "Thanks, [player_name]. It’s just... everything feels so overwhelming right now."

        "Try to focus on the good things in life.":
            $ affection -= 2
            classmate "I wish I could, but it’s hard to see any good right now."

    scene bg uni
    with dissolve

    "After class, you decide to walk with Alex."

    player "Hey Alex, want to walk together for a bit?"
    classmate "Sure, thanks."

    "You and Alex walk in silence for a while, then Alex starts talking."

    classmate "You know, it’s really hard for me to open up about my problems. I’ve always felt like I should just deal with things on my own."

    menu:
        "It’s okay to ask for help. You’re not alone.":
            $ affection += 1
            classmate "I know... it’s just hard to break that habit."

        "Everyone has their struggles, you’ve got this.":
            $ affection -= 2
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
            classmate "(frowns) It’s really complicated... and stressful."

    scene bg meadow
    with dissolve

    player "Hey Alex, want to join me for a walk in the park this weekend?"
    classmate "Sure, that sounds nice."

    "You and Alex enjoy the fresh air and the beauty of nature. Alex seems to relax more as you walk together."

    classmate "Thanks for inviting me. This is really nice."
    player "I’m glad you’re enjoying it."

    show classmate smile at left

    "You and Alex find a bench and sit down to rest for a while."

    menu:
        "Have you thought about what you want to do in the future?":
            $ affection += 1
            player "Have you thought about what you want to do in the future?"
            classmate "I have some ideas, but I’m not sure yet. How about you?"

        "You text your friends to see what they’re doing.":
            $ affection -= 3
            player "(You text your friends to see what they’re doing.)"
            classmate "Oh, are you bored? We can leave."

    scene bg lecturehall
    with dissolve

    "The next day, you notice Alex is absent again. You feel a growing sense of concern."

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
            $ affection -= 3
            classmate "I know... I just needed some time alone."

    scene bg club
    with dissolve

    "You decide to take Alex to the café again to help her relax."

    player "How about we get something to drink again? My treat."
    classmate "That sounds nice. Thanks."

    show classmate smile at left

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
    player "I’m glad you’re enjoying it."

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
    
    if affection > 0:
        jump good_ending
    else:
        jump bad_ending