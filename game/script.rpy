default affection = 0

label class_1:
    queue music ["dark_intro.ogg", "dark_verse.ogg"]

    scene bg lecturehall
    with dissolve

    "You head to class and quickly find an empty seat. You notice a cute girl sitting next to you."

    show classmate surprised at left
    with moveinleft

    menu:
        "Introduce yourself.":
            $ affection += 1
            player "Hi there!{w=0.1} Looks like we’re going to be seatmates."

        "Say nothing.":
            $ affection -= 1
            player "..."

    show classmate smile at left, flip

    classmate "Hi, I’m [classmate.name],{w=0.1} nice to meet you."
    player "Nice to meet you,{w=0.1} I’m [player_name]."
    player "What brings you to Psych 101?"
    classmate "I’m interested in positive psychology."
    classmate "And you?"

    menu:
        "I’m here for the easy A.":
            $ affection -= 1
            classmate "Haha, fair."

        "I want to learn how psychology applies to our everyday lives.":
            $ affection += 1
            classmate "Nice."

    "You and [classmate.name] continue to talk some more before being interrupted by the teacher."

    show teacher normal at scale(0.6), right
    with moveinright

    teacher "Alright, let’s start class.{w=0.2} Today we’re going to learn about Pavlov’s dog."

    stop music fadeout 4

    jump after_class_1

label after_class_1:
    scene bg uni
    with fade

    "Class finished and you find yourself strolling with [classmate.name]."

    queue music ["sad4_verse.ogg", "sad4_hook.ogg"]

    show classmate smile
    with dissolve

    player "What did you think of the lesson, [classmate.name]?"
    classmate "Pretty good!{w=0.2} Just trying to keep up with everything."
    player "I find it interesting how animals can be conditioned to a stimulus."
    classmate "True."

    stop music

    "The school bell rings."

    menu:
        "Want to grab a snack?":
            $ affection += 1
            classmate "Sure, let’s do it."
            jump after_class_1_break

        "I have to go back and study.":
            $ affection -= 1
            classmate "Alright,{w=0.1} see you later."
            jump after_class_1_study

label after_class_1_break:
    scene bg club
    with dissolve

    queue music ["sad8_verse.ogg", "sad8_hook.ogg"]

    "You and [classmate.name] make your way to the school’s cafeteria."

    show classmate smile at flip, center
    with dissolve

    menu:
        "What would you like? My treat.":
            $ affection += 1
            classmate "Thanks."

        "I left my wallet back in class.":
            $ affection -= 1
            classmate "No worries,{w=0.2} I got you."

    classmate "I’ll have a cupcake."
    classmate "What are you having?"

    menu:
        "Hot dog":
            classmate "Nice."

        "Taco":
            classmate "Yummy."

    "After buying the food, you both find a table and starting chowing down."

    menu:
        "So what do you like to do in your free time?":
            $ affection += 1
            classmate "I enjoy reading and painting. It’s a good way to relax."

        "Did you hear the news about the mental illness rate going up?":
            $ affection -= 1
            show classmate surprised
            classmate "I haven’t. That’s worrisome to hear."

    show classmate smile
    "As you spend more time with [classmate.name], you notice her mood is generally upbeat and positive. She starts to smile more often."

    stop music fadeout 4

    jump after_class_1_study

label after_class_1_study:
    scene black
    with fade

    queue music "sad2_intro.ogg"

    "You went to the library and studied for a few hours."
    "Feeling exhausted, you decided to wrap up the session."
    "As you head back home, you bump into someone familiar."

    jump after_class_1_hangout

label after_class_1_hangout:
    scene bg meadow
    with dissolve

    queue music "sad2_verse.ogg"

    show classmate surprised
    with moveinbottom
    with vpunch

    pause 1

    player "Hey [classmate.name], didn’t expect you here."
    player "Want to join me for a walk?"

    show classmate smile at flip, center

    classmate "Sure, that sounds nice."

    "You and [classmate.name] enjoy the fresh air and the beauty of nature. [classmate.name] seems to relax more as you walk together."

    classmate "Thanks for inviting me. This is really nice."
    player "I’m glad you’re enjoying it."

    show classmate smile at right
    with moveinleft

    "You and [classmate.name] find a bench and sit down to rest for a while."

    menu:
        "Have you thought about what you want to do in the future?":
            $ affection += 1
            classmate "I have some ideas, but I’m not sure yet. How about you?"

        "You text your friends to see what they’re doing.":
            $ affection -= 1
            classmate "Oh, are you bored? We can leave."

    stop music fadeout 4

    scene bg lecturehall
    with dissolve

    queue music ["dark_intro.ogg", "dark_verse.ogg"]

    "The next day, you enter the classroom and sit next to [classmate.name], who is still in a good mood."

    show classmate surprised at left
    pause 0.8
    show classmate smile at left, flip

    player "Hey [classmate.name], how’s it going?"
    classmate "Pretty good, thanks! How about you?"

    menu:
        "I’m doing well, thanks!":
            $ affection += 1
            classmate "Great to hear!"

        "Could be better.":
            $ affection -= 1
            classmate "Oh, anything you want to talk about?"

    "Class begins, and the teacher discusses the importance of mental health awareness. You notice [classmate.name] paying attention and taking notes."

    scene bg uni
    with dissolve

    show classmate smile at left
    with fade

    player "Need help with any subjects?"
    classmate "Actually, yes. I’m struggling a bit with our psychology assignment."

    menu:
        "You’re doing great, [classmate.name]. Keep it up!":
            $ affection += 1
            classmate "Thanks, [player_name]. Your support means a lot."

        "I find that making flashcards helps. Maybe we can create some together?":
            $ affection -= 1
            classmate "That’s a great idea!"

    stop music fadeout 4

    jump personality_test_agreeableness

label class_2:
    scene bg lecturehall
    with dissolve

    show classmate sad at left
    pause 0.8
    show classmate sad at left, flip

    play music "chill_intro.ogg"
    queue music "chill_verse.ogg"

    "One day, you notice [classmate.name] is a bit quieter than usual."

    player "Hey [classmate.name],{w=0.3} you okay?{w=0.4} You seem a bit off today."
    classmate "{alpha=0.7}{i}(sigh){/i}{/alpha}{w=0.5} Just dealing with some stuff.{w=0.3} It’s been a tough week."

    menu:
        "If you need to talk, I’m here for you.":
            $ affection += 1
            classmate "Thanks.{w=0.1} I appreciate it."

        "We all have tough weeks, you’ll get through it.":
            $ affection -= 1
            classmate "Yeah, I guess..."

    show teacher normal at scale(0.6), right

    "Class begins, but you can’t help but notice [classmate.name]’s distracted state.{w=0.2} The teacher discusses the importance of mental health awareness, which deeply resonates with you."

    stop music fadeout 4

    jump after_class_2

label after_class_2:
    queue music "sad1_intro.ogg"
    queue music "sad1_verse.ogg"

    scene bg club
    with dissolve

    "Later in the hallway, you overhear [classmate.name] talking to another student."

    show classmate upset at scale(0.7), right
    pause 0.8
    show classmate upset at right, flip

    classmate "{alpha=0.7}{i}(frustrated){/i}{/alpha}{w=0.2} I don’t know what to do anymore.{w=0.3} It just feels like everything is falling apart."

    menu:
        "[classmate.name], I overheard what you were saying. Do you want to talk about it?":
            $ affection += 1
            show classmate upset at right, unflip
            classmate "It’s just...{w=0.3} everything feels so heavy...{w=0.3} My family is going through a lot, and I’ve been feeling really low."

        "Maybe you should try to relax and take it easy.":
            $ affection -= 1
            show classmate upset at right, unflip
            classmate "I wish it were that simple..."

    player "I’m really sorry to hear that.{w=0.3} Have you considered talking to the school counselor?{w=0.2} They might be able to help."

    classmate "Maybe...{w=0.4} I just don’t know if it will change anything."
    player "It’s worth a try.{w=0.2} Sometimes just talking to someone can make a big difference."
    classmate "Thanks.{w=0.2} I appreciate your concern."

    stop music fadeout 4

    jump personality_test_conscientiousness

label before_class_4:
    queue music "sad2_intro.ogg"

    scene bg meadow
    with dissolve

    "Later that evening, you check social media and see a post from [classmate.name]."
    classmate "“Sometimes I wonder if it’s all worth it.{w=0.4} Life just feels like one big mess.”"

    queue music ["sad2_verse.ogg", "sad2_bridge.ogg"]

    menu:
        "Hey, I saw your post. I’m really concerned about you. Please, let’s talk.":
            $ affection += 1
            classmate ".{w=0.2}.{w=0.2}.{w=0.2}"
            classmate "Thanks for reaching out.{w=0.2} I’m just really struggling right now."
            player "Remember what we talked about today?{w=0.2} Maybe talking to the counselor could help.{w=0.1} I can go with you if you want."
            classmate "Okay.{w=0.1} Maybe tomorrow."

        "Ignore the post.":
            $ affection -= 1

    stop music fadeout 4

    jump class_4

label class_4:
    scene bg lecturehall
    with dissolve

    queue music "tense_intro.ogg"
    queue music "tense_verse.ogg"

    "You get to class the next day and notice that [classmate.name] is absent. The room feels tense."
    player "{alpha=0.7}{i}(thinking){/i}{/alpha}{w=0.1} Where’s [classmate.name]?{w=0.2} She said she’d be here today."

    show teacher sadder at scale(0.6), center

    teacher "I don’t know how to say this,{w=0.3} but one of our classmates took her own life last night."
    player "..."
    player "{alpha=0.7}{i}(thinking){/i}{/alpha}{w=0.1} No,{w=0.2} it can’t be her."
    teacher "For the privacy of the individual,{w=0.1} we’re unable to share any news.{w=0.1} But please be respectful for the time being."

    stop music fadeout 1

    if affection > 0:
        jump good_ending
    else:
        jump bad_ending
