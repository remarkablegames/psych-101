label before_class_5:
    call personality_test_neuroticism
    jump class_5

label class_5:
    scene bg lecturehall
    with fade

    queue music tense_intro
    queue music tense_verse

    "You get to class the next day and notice that [classmate.name] is absent. The room feels tense."
    player "{alpha=0.7}{i}(thinking){/i}{/alpha}{w=0.1} Where’s [classmate.name]?{w=0.2} She said she’d be here today."

    show teacher very sad at scale(0.6), center
    with dissolve

    teacher "I was just informed of unfortunate news."
    teacher "But one of our classmates took her own life last night."
    player "..."
    player "{alpha=0.7}{i}(thinking){/i}{/alpha}{w=0.1} No,{w=0.2} it can’t be her."
    teacher "For the privacy of the individual,{w=0.1} we’re unable to share any details.{w=0.1} Please be respectful for the time being."

    if affection > 0:
        jump good_ending
    else:
        jump bad_ending
