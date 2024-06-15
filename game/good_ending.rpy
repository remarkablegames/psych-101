label good_ending:
    if affection > 0:
        show teacher happy

    show teacher sadder

    teacher "I don’t know how to say this, but unfortunately, one of our classmates took her own life last night."
    player "{i}(thinking){/i} No, it can’t be her. Please don’t be her."
    teacher "For the privacy of the individual, we’re currently not able to say who it was. But please be respectful for the time being."

    show classmate smile at scale(0.6), left

    classmate "I’m sorry I’m late. I had an appointment with the counselor this morning."
    player "{i}(thinking){/i} Thank goodness she’s okay."

    queue music ["tropical_house1_intro.ogg", "tropical_house1_verse.ogg"]

    #put counselor/therapist's office background below
    scene bg uni

    "You and Alex visit the counselor together, talking openly about Alex’s struggles. The counselor provides resources and support."

    show teacher happy at scale(0.6), right

    teacher "It’s great to see friends supporting each other. Alex, we’re here for you. Let’s work together to help you through this."

    show classmate smile at scale(0.6), left

    classmate "Thank you. I feel like I have a bit more hope now."

    scene bg lecturehall
    with dissolve

    "In the following days, you and Alex continue to support each other. Alex starts to feel more positive and engaged in class."

    show classmate smile

    classmate "{i}(smiling){/i} Thanks for everything. I really appreciate you being there for me."
    player "Anytime, Alex. We’re in this together."

    scene bg uni
    with dissolve

    "The school organizes a mental health awareness event. You and Alex participate, sharing your story to help others."

    show classmate smile

    player "It’s important to reach out and support each other. We can all make a difference."

    classmate "I’m living proof that talking to someone and getting help can change everything. Never again will I be afraid to speak up."

    scene black
    with dissolve

    "{b}Good Ending{/b}."

    return
