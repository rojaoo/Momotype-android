﻿label n(what):
    $ i = ending_count()

    $ lines = None
    while lines is None:
        $ lines = what[i]
        $ i -= 1

    # horrible, but lets me not have to make everything a singleton list
    if type(lines) is str:
        $ lines = [lines]

    $ i = 0
    while i < len(lines):
        $ narrator(lines[i])
        $ i += 1

    return

label start:
    $ points = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image background = Solid("#3F221C")

    define fade = Fade(0.5, 0.0, 0.5, color="#3F221C")

    $ _game_menu_screen = "preferences"

    if ending_count():
        jump repeat_playthroughs

    play music "audio/momo_music_begin.mp3"

    scene background
    show momo_city at top with fade

    # These display lines of dialogue.
    "Your neighborhood, New Ribosome City"

    scene background
    show momo_dna at top with fade

    "The chains of DNA spin on your screen. They make a web of helices until the logo of Imitato Corp. appears in a white font. The ad has begun."

    scene background
    show momo_ad at top with fade

    "They were all the rage in the 2100's. You knew them as monotypes, your digital, pocket friend. You'd feed them, play games with them, and watch them grow. Mom and Dad liked them because there was no cleanup. You liked them because they seemed real!"

    "With the advent of the digital age, we at Imitato Corp. have noticed society changing."

    "Birth rates in this country have hit an all time low, not seen since the plague. Soon, our workforce will be depleted and unemployed. Once this occurs, industry will fail."

    "As you all know, this is an existential threat not only to ourselves, but importantly, our GDP."

    "Monotypes, our digital, pocket pets, have supported this decline."

    "We want people to have kids. This, unfortunately, cannot be accomplished through digital software. It can, however, be accomplished through our new product."

    scene background
    show momo_ad_real at top with fade

    "Today, we're excited to announce the shipment of our new line of monotypes. The real monotype. The digital enters the physical. Cuddle them like real pets. Play with them like real pets. Watch them grow and change!"

    "Know the joys of parenthood! Order now at no cost. Supplies limited."

    menu:
        "Place an order?"

        "Yes":
            scene background
            show momo_city at top with fade

            "Your order is coming sooner than expected. The postal service is expediting all monotype orders. When you head to work the next day, you find out that this is a government sponsored program. Your manager corrals your team into a huddle."

            "Yup, your order's been canceled. We'll be providing work-issued ones."

            "He explains that everyone will be receiving a monotype."

            "\"Has a partnership formed between Imitato Corp?\" an employee asks. \"You're right on the money Christine,\" your manager says."

            "\"We have to get this country moving, and corporate wants to be that vehicle of change.\" he says, shaking his fist in the air."

            "\"Your hours will be unpaid, but a week will pass by like nothing. Pizza party's on Friday!\""

        "No":
            scene background
            show momo_city at top with fade

            # should we just make the dialogue be spoken by whatever character?

            "It turns out that this is a government sponsored program. When you head to work the next day, your manager corrals your team into a huddle. He explains that everyone will be receiving a monotype. "

            "\"Has a partnership formed between Imitato Corp?\" an employee asks. \"You're right on the money Christine,\" your manager says."

            "\"We have to get this country moving and corporate wants to be that vehicle of change,\" he says, shaking his fist in the air."

            "\"Your hours will be unpaid, but a week will pass by like nothing. Pizza party's on Friday!\""

    scene background
    show momo_city at top with fade

    "Your home, New Ribosome City"

    label repeat_playthroughs:
        pass

    scene background
    show momo_nightmare_1 at top with fade

    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    $ renpy.music.play("audio/creepy_noises.mp3", channel="creepy", loop=True)

    call n([
        "A dust storm. Lead in the air. You are in a desert-like area. There is nothing around you besides the sound of your thoughts. You cannot find any-",
        None,
        "A dust storm. Lead in the air. You are in a desert-like area. The sound of your thoughts bang on the hollow mould of your head. You will break if it doesn't stop.",
    ]) from _call_n

    call n([
        "A friend tomorrow is a friend for life. Supplies limited.",
        [
            "\"Please love me?\"",

            "You're awake. You feel your neck.",
        ],
        [
            "\"The last time,\" you hear a voice say.",

            "You're awake.",
        ]
    ]) from _call_n_1

    $ renpy.pause (2.5, hard=True)
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
    $ renpy.music.stop(channel="creepy")

    if ending_count():
        play music "audio/momo_music_begin.mp3"

    scene background
    show momo_city at top with fade

    call n([
        [
            "You're awake. Remnants of the dream pass and fade into static. You're back to your show.",

            "You're going to watch television until you hear noise outside your door. Someone has left something on your porch. It's for you.",
        ],
        [
            "Though it has healed, your throat has marks lining the circumfrence of your skin. They are deep and sallow. The marks will not go away.",

            "A voice playbacks in your head.",

            "\"Most variables, your house for example, or the lining of the furniture.\" The lab head had been focused on the monitor the entire time.",

            "\"These will be our control. What you decide to do with him, those are the independent variables.\"",

            "The Imitato Corp. logo with its trademark helix is adorned on the mantle of the lab.",

            "\"Why does everything need to be the same?\"",

            "The lab head has looked up.",

            "\"Trial and error? I assume you know what that means.\" The lab head is being genuine.",

            "\"Mapping a neural network begins with specificity. Only then can we generalize patterns on the macro level. Your case,\" she stops for a moment, \"was the most promising.\"",

            "She continues.",

            "\"Remember, and this is important, we're trying to collect new data. Not old. Those new permutations are what we need, and there's no point if you raise this one the same.\" The lab head finishes.",

            "\"Do I have a choice, you ask?\"",

            "The lab head smiles. \"Insofar as you control how the monotype is raised, yes. Whatever style you choose, keep it consistent.\"",

            "She looks back to her monitor.",
        ],
        [
            "Your memories are in an incipient state, like the portions of bacteria which brought life to a lifeless Earth. It only takes some time for the catalyst to appear. You hear the jingle. You remember.",

            "You see the Imitato Corp. logo.",

            "\"I'm sorry. I really am sorry,\" the brows of the lab head, cleanly plucked, are furrowed.",

            "\"Our agents were told to interfere after a certain point. When we noticed that change in your vitals, we gave the order.\"",

            "She seems apologetic.",

            "\"I can't imagine how taxing this is for you.\" She puts her hands together. \"It's okay if you feel tired. We'll provide you with any psychotherapeutic treatment at no cost to yourself.\"",

            "She turns her head, not wanting to look at you.",

            "\"None of this is fair, but I'm not going to mince my words. We need the data.\"",

            "There is a stone in your torso that has descended through your leg, past the popliteal artery, and, finally, into your feet. You are stuck.",

            "She looks straight at you. \"Your compensation, your safety, everything is guranteed.\" She points to the code on the screen. \"The monotype can't harm you. At least fatally. This is by design. He's just an AI.\"",

            "She sighs.",

            "\"It'll be over soon. You're doing more for us than you could ever possibly know, and we do appreciate it, genuinely.\"",
        ]
    ]) from _call_n_2

    scene background
    show momo_basket_down at top with fade

    call n([
        "When you open the door, there it is: a small creature laying in a basket. It's sleeping soundly.",
        [
            "You're back in your room. You hear a noise.",

            "You open the door to your apartment complex.",

            "There it is: a new monotype laying in a basket. It's sleeping soundly.",
        ],
        "Momo has returned home. You thought he was gone for good, but he's back. Great news!",
    ]) from _call_n_3

    menu:
        "Turn it over":
            pass

    scene background
    show momo_basket_up at top with fade

    if ending_count() == 0:
        "The \"monotype\" you ordered has arrived. It has soft skin. Its ears are pointed. They feel like bean bags upon further inspection. It's a monotype but in physical form, as per the ad."

        "You want to assume it's a plushie. To your surprise, however, the 'monotype' is warm. The terms of your purchase have not been released."

        menu:
            "Keep it?"

            "Yes":
                pass

            "No. Leave it outside":
                scene background
                show momo_city at top with fade

                play music "audio/momo_music_middle.mp3"

                "You leave the creature outside. The night ends. You sleep to a blank dream. "

                scene background
                show momo_basket_down at top with fade

                "The next morning, you open your door to see the monotype on your porch. Its body is still. Upon touching the creature, you realize that it's cold. It has frozen to death."

                "You pick up the basket, and after some inspection, throw it and the monotype in the trash. You will be fired the next day."

                scene background
                show momo_deathscreen at top with fade

                "Your manager's reasoning, in his words, was that \"this wasn't optional.\" He then wonders \"how you could be so heartless and leave him out in the cold?\" He continues, shaking his fist in the air."

                "\"Corporate did not like this. I didn't like this."

                "I can't trust you anymore, and neither can your coworkers. You're gone.\""

                "In his lap is a monotype of his own. It will stare at you inquisitively. \"Isn't that right Momo, we don't want this bad person in our office.\" He points at you."

                "The monotype asks you a question. You can't hear it."

                $ renpy.pause(3, hard=True)
                # $ achievement.grant("COLD_ENDING")
                # $ achievement.sync()

                return
    elif ending_count() == 1:
        "It's virtually the same as the monotype you previously had."

        menu:
            "Keep it?"

            "Can't just let him freeze to death.":
                pass
    else:
        "Momo is so cute."

        menu:
            "Keep it?"

            "He's my little buddy. Of course I will.":
                pass

    scene background
    show momo_bed_sleep at top with fade

    "You take the creature inside."

    call n([
        "\"Monotypes live for approximately seven days.\" A note has been packed inside the basket. \"Take care of them, and they will grow. Monotypes love humans, so give them some love back. It's essential for their well-being.\"",
        "\"Please love them for the best results. Or don't. It's your decision.\"",
        "\"Please love them for the best results. Or don't. It's your decision.\"",
    ]) from _call_n_4

    call n([
        "The note ends. There is nothing else by way of instructions.",
        "\"Love, Imitato Corp.\"",
        "\"Love and kisses xoxoxo, Imitato Corp.\"",
    ]) from _call_n_5

    "You decide it's time for bed."

    scene background
    if ending_count:
        show momo_ad_real at top with fade
    else:
        show momo_nightmare_1 at top with fade

    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    $ renpy.music.play("audio/creepy_noises.mp3", channel="creepy", loop=True)

    call n([
        [
            "A collection of particles circle around. They are diluted with a heavy substance, though you can't tell what. In your dream, the particles attempt to create form, and in doing so, assemble into a storm.",

            "Inside the storm there is no one and nothing, except small spaces where it's immeasurably dark. Your vision recedes.",

            "You look from a bird's eye view into the storm, hoping to get a better look. As soon as you think you spot a person, the particles scatter. You repeat this process until finally, you realize you're completely alone. The dream ends.",
        ],
        "You are dreaming of Momo. Which Momo is it, though?",
        "\"It's tough living. I think it's the greatest challenge anyone could face. It's already such a lonely experience. You may not believe it, but I understand, parent, I really do.\"",
    ]) from _call_n_6

    $ renpy.pause (2.5, hard=True)
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
    $ renpy.music.stop(channel="creepy")

    scene background
    show momo_wake at top with fade

    "Your hear shuffling by your bed. You wake up to see what is moving. The monotype is by your feet."

    call n([
        "\"Hello parent. Momo will stay with you for the rest of your life. Do you love Momo? Momo already knows the answer.\"",
        [
            "\"Hello parent. Momo will stay with you for the rest of your life. Do you love Momo? Momo wishes to know your answer?\"",

            "There is some hesitation in the new Momo's voice.",
        ],
        "\"Parent?\" Momo is staring at you, same as last time. \"Do you love me?\""
        ]) from _call_n_7

    $ yes = m([
        "I love Momo.",
        "I really do love Momo.",
        "I love Momo to absolute bits.",
    ])

    $ maybe = m([
        "I barely know you. Take it slow?",
        "This is too much, Momo.",
        "Love does not exist. At least, not in the way we're talking about.",
    ])

    menu:
        "[yes]":
            $ points += 1

            call n([
                [
                    "Momo has received this well. Your answer was never in question. After all, he's cute.",

                    "A moment passes. Momo's stomach begins grumbling. Now that you think about it, how does Momo manage to eat? Or speak for that matter?",
                ],
                [
                    "It looks like a weight has been unburdened from Momo.",

                    "A moment passes. Momo's stomach begins grumbling.",
                ],
                [
                    "\"Yay!\"",

                    "You grab Momo and throw him in the air. It's a new day, a new you!",

                    "A moment passes. Momo's stomach begins grumbling.",
                ],
            ]) from _call_n_8
        "[maybe]":
            call n([
                [
                    "Momo stares at you. The words do not register nor does it seem Momo derives any meaning from them. It's as if you spoke in a different language.",

                    "\"Does that matter? In the first place, you are my designated parent. Nothing can change this fact.\"",

                    "A moment passes. Momo's stomach begins grumbling. Now that you think about it, how does Momo manage to speak?",
                ],
                [
                    "Momo stares at you. The words do not register nor does it seem Momo derives any meaning from them.",

                    "Momo twitches violently. His body is like a muscle which has contracted too hard.",

                    "The moment passes. Momo's stomach begins grumbling.",
                ],
                [
                    "\"Wow, very philosophical.\"",

                    "The moment passes. Momo's stomach begins grumbling.",
                ],
            ]) from _call_n_9

        "No.":
            $ points -= 1

            call n([
                [
                    "\"That is incorrect parent. Please do not lie to Momo.\" Momo speaks plainly."

                    "\"It's true, Momo. I don't know you very well. How could I love you immediately?\" you respond."

                    "Momo examines you. \"You gave me life. I am not correct?\""
                ],
                "\"That is incorrect parent. If you lie to Momo,\" he pauses, \"well, he'll remember,\" he finishes.",
                "\"Liar liar, pants on fire\"",
            ]) from _call_n_10

            call n([
                "A moment passes. Momo's stomach begins grumbling. Now that you think about it, how does Momo manage to speak?",
                None,
                "A moment passes. Momo's stomach begins grumbling.",
            ]) from _call_n_11

    menu:
        "Head to hallway":
            pass

    scene background
    show momo_hall at top with fade

    call n([
        [
            "\"Momo thinks you have good taste in interior design. Very post-modern...By the way, what does post-modern mean? Momo saw it on a book from your shelf\""

            "Truthfully, you don't know."

            "Momo is now humming the Imitato. Corp jingle."
        ],
        [
            "\"Momo does not like your interior design, frankly. You cannot see anything. Very little natural light, aside from the street. It's a little dated. Depressing even.\"",

            "For some reason, Momo does not like to be in the shadows. He stays in the light.",

            "Momo hums the Imitato. Corp jingle, but when you look at him, he stops.",
        ],
        [
            "\"Momo really loves benches.\"",

            "Momo hums the Imitato. Corp jingle, and when you look at him, he continues, happily.",
        ]
    ]) from _call_n_12

    scene background
    show momo_pancake at top with fade

    call n([
        "Is Momo herbivorous? A carnivore? You don't know yet, but he seems to like pancakes. He's now full of energy.",
        [
            "Is Momo herbivorous? A carnivore? You have some ideas. Momo seems to like pancakes, same as last time.",

            "\"Pancakes really are the best. Better than any other food. Simple. Straightforward.\"",
        ],
        [
            "You don't know how many pancakes you've made at this point.",

            "\"Pancakes, pancakes, we all love pancakes.\"",
        ]
    ]) from _call_n_13
    menu:
        "Play with Momo":
            pass

    scene background
    show momo_throw at top with fade

    call n([
        "Momo flies into the air. They're surprisingly heavy. \"Keep going parent!\". After 30 minutes of using Momo like an exercise ball, you're tired. You drop him onto the floor, and while he lays there absently, you take a moment to catch your breath.",
        None,
        "\"Don't drop me parent!\" Momo is laughing.",
    ]) from _call_n_14

    call n([
        "This results in some confusion. Momo seems fidgety. \"Parent. Momo still wants to play.\"",
        "This results in some confusion. Momo seems fidgety. \"Parent. Can we play again? Just for a little?\"",
        "You drop Momo, same as last time. \"Parent, I understand if you're tired. Could we play again?\"",
    ]) from _call_n_15

    menu:
        "Continue":
            $ points += 1
            call n([
                [
                    "You resume chucking Momo into the air. At some point, his head (body) smashes into the ceiling, and to your surprise, he is unaffected. He requests that you keep going.",

                    "This process is repeated until your arms give out.",

                    "\"Thank you, parent. Could you cook pancakes tomorrow?\" Momo asks. Then, he hops off. You lay crumpled on the floor. Upstairs, you can hear small thuds in the hallway. They eventually lead to your bedroom, and soon enough, the noise stops.",
                ],
                [
                    "You resume chucking Momo into the air. At some point, his head (body) smashes into the ceiling.",

                    "He tells you throw him as hard as you can. He can take it.",

                    "This process is repeated until your arms give out.",

                    "\"Thank you, parent. Please only cook pancakes tomorrow. Only pancakes,\" Momo has ordered.",

                    "Then, he hops off. You lay crumpled on the floor.",
                ],
                [
                    "You resume chucking Momo into the air. At some point, his head (body) smashes into the ceiling.",

                    "\"Thank you, parent! You're my favorite parent!\" Momo has hopped off.",

                    "You lay crumpled on the floor.",
                ]
            ]) from _call_n_16
        "Refuse":
            "\"Why not parent?\" he asks."

            "\"I'm tired. Let's call it quits. I don't wanna do this,\" you respond."

            call n([
                "Momo looks up to you. From your linoleum floor, you see an expression of frustration. \"One more time,\" he says.",
                "Momo looks up to you. From your linoleum floor, you see an expression of frustration. \"Is it so hard to throw Momo a few more times? Really, is it that hard for parent? I'm not asking for much.\" he says.",
                "Momo looks up to you. \"If I ask another time, will you do it?\""
            ]) from _call_n_17

            menu:
                "Accept":
                    call n([
                            "You assume that Momo is young. You don't want do be a dick. Momo is thrown into the air exactly one more time.",
                            [
                                "Does Momo have a point?",

                                "You throw him. When he lands, he looks up to you. \"They say the greatest expression of love is action. Is that true for me?\"",

                                "Momo thinks for a second. \"Most likely, yes.\"",
                            ],
                            [
                                "You fling Momo into the air.",

                                "\"You're so nice, parent.\"",

                                "There is something inexplicable about Momo's words that makes you anxious. Deep down, you know you're not actually nice.",
                            ],
                    ]) from _call_n_18

                    "\"Time for bed\", you say."

                "Refuse":
                    $ points -= 1

                    call n([
                        "\"Sorry to say, but it's not happening.\"",
                        None,
                        "\"Sorry. I can't do it.\""
                    ]) from _call_n_19

                    call n([
                        "For a moment, there is silence. Momo does not say anything. Their face reminds you of a toddler's.",
                        "For a moment, there is silence. Momo does not say anything. Their face reminds you of a toddler's, only, a little more grown up.",
                        [
                            "\"Momo understands. You are very tired. You have a job. Momo wishs he had passive income, so he could never work.\"",

                            "\"That's smart of you Momo. What would you do to get that money in the future?\" you ask.",
                        ],
                    ]) from _call_n_20

                    call n([
                        "He looks through you, and after some thinking, hops back to your room to get ready for bed.",
                        "Momo sighs and is already heading upstairs.",
                        "Momo thinks for a second. He then hops upstairs without replying to you.",
                    ]) from _call_n_21

    scene background
    show momo_bed_sleep at top with fade

    call n([
        "Momo looks like a plush doll. He lays like a pile of goo. You've decided to pet him, but to your surprise, his body is taut. Underneath is a muscle-bound creature.",
        "Momo looks like a plush doll. He lays like a pile of goo. You've decided to pet him, but same as before, his body is taut. He's especially high-strung.",
        "Momo looks like a plush doll. He lays like a pile of goo. You've decided to pet him, but to your surprise, his body is soft. Momo is relaxed.",
    ]) from _call_n_22

    menu:
        "Go to bed":
            pass

    scene background
    if ending_count() == 1:
        show momo_nightmare_1 at top with fade
    else:
        show momo_dream at top with fade

    call n([
        "In the theater of Momo's mind, there is nothing. The only thing that can be made out is the appearance of a person. Momo is dreaming about someone, and it's most likely you.",
        "In the theater of Momo's mind, he is having a nightmare.",
        "In the theater of Momo's mind, he is thinking about you.",
    ]) from _call_n_23

    scene background
    if ending_count():
        show momo_ad_real at top with fade
    else:
        show momo_nightmare_2 at top with fade

    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    $ renpy.music.play("audio/creepy_noises.mp3", channel="creepy", loop=True)

    call n([
        [
            "You're back in the desert, still in bird's eye view. The particles have ceased to move. You know that you've been waiting a long time, longer than you've waited in real life. You want something to happen.",

            "You know this a dream, but the particles, your buoyed vision, the endless wait: years could pass without contradiction. For now, this is everything.",

            "As you've been waiting, the particles have started moving. They scatter like dust. Above you, even higher than where you currently are, it starts raining to an innumerable degree. You ascend.",

            "You are now in the clouds. The rain is below you. You are looking down from an even higher position. Finally and without your own observation, the particles begin assembling. They seem to form something definite.",

            "You don't notice the figure below you until you see a hand waving.",
        ],
        [
            "\"...\"",

            "\"What did you say?\"",

            "\"...\"",

            "It's an empty space. You cannot hear anything.",
        ],
        "\"We're all thinking about you!\"",
    ]) from _call_n_24

    $ renpy.pause (2.5, hard=True)
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
    $ renpy.music.stop(channel="creepy")

    play music "audio/momo_music_middle.mp3"

    scene background
    show momo_city at top with fade

    menu:
        "It's a new day."

        "Head to hallway":
            pass

    scene background
    show momo_hall at top with fade
    call n([
        [
            "\"Momo heard that this country's GDP is on the fritz. Soon, nobody will be making babies anymore. Banks will go under, food will be short, mass suicides all around. Will Momo be there for it?",

            "No, Momo has a bunker out in Southwest Ribo City. Very safe. Well stocked. How does Momo know so much about the world? Intuition. Does Momo know where bunker is?",

            "No, and he does not like revealing such details. Parent, can Momo ask you a question? What is GDP?\"",

            "Momo pauses.",

            "\"Momo does not know what a bunker is, to tell you the truth. Is it a type of pancake?\"",
        ],
        [
            "\"Momo has to find his bunker. In bunker, Momo is safe. No one can hurt him. Maybe they can yell bad words at Momo outside of a metal door. But Momo does not care. Momo will not face the end. There is no end if Momo is in his bunker. Where is this bunker, you ask?\"",

            "Momo stops to think for a second. \"I know it's here. There's an invisible trail only Momo can see.\"",

            "Momo pauses.",

            "\"It doesn't smell like pancakes.\"",
        ],
        [
            "\"Momo always keeps hearing about some bunker. Momo's already visited. It's pretty rad. They have their own pool. Not much food though.\"",

            "Momo pauses.",

            "\"It smells like food right now! That's why I love living here.\"",
        ]
    ]) from _call_n_25
    menu:
        "Head to kitchen":
            pass

    scene background
    show momo_kitchen_front at top with fade

    "Momo has not yet decided what to eat. You want him to try new foods."

    menu:
        "What should you give him?"

        "Artichoke":
            scene background
            show momo_artichoke_food at top with fade

            $ food = "Artichoke"

            "According to Momo The artichoke heart looks like a \"flower\", and because flowers are \"pretty\" (his words not yours) he graciously eats it. \"Why is this food shaped this way? Is all food shaped this way? Why do we eat, parent?\""

            "You do not have reasonable answers to these queries. \"The world truly is strange,\" Momo says."

        "Steak":
            scene background
            show momo_steak_food at top with fade

            $ food = "Steak"

            "\"This was made from a cow? Where do they live?\" Once you explain that they live in mass industrialized farms, Momo stares at his plate. \"Is it okay to eat cows?\" The actual answer is probably not, but humans do so anyways."

            "\"That does not make sense, parent,\" Momo responds. He eats the steak anyways. \"It makes no sense.\""

        "Cigarette":
            scene background
            show momo_cig_food at top with fade

            $ food = "Cigarette"

            "Momo does not smoke from the cigarette, but instead, eats the tobacco. From what Imitato Corp. mentioned, monotypes are biodegradable. This comment didn't initially make sense, and even now, as Momo eats through a 12 pack, it still does not."


    scene background
    show momo_wake at top with fade

    call n([
        "Life with Momo is relatively simple. They are a crude mix between a child and a virtual pet. Concerning this, you don't have any particular feelings. However, this does make it difficult when asked questions concerning Momo's identity.",
        "\"Is Momo human?\" he asks. \"Momo wishes for you to be straight with him. Momo already knows he is, but he needs confirmation from another source.\"",
        "\"Momo would like to watch television. Momo believes their show is on.\"",
    ]) from _call_n_26

    $ hippo = True

    $ dragon = True

    $ sheriff = True

    if ending_count() == 2:
        scene background
        show momo_tv_neutral at top with fade
        jump tv

    menu:
        "\"Is Momo human?\" he asks."

        "Yes":
            "\"You are human Momo, as human as ever one could be.\""

            "Momo considers this for a moment. They are hopping around the room in thought."

            menu:
                "\"Where did Momo come from? Where is the source?\""

                "A magical stork":
                    scene background
                    show momo_wake_blush at top with fade

                    call n([
                        "\"Whoa\". Momo looks to the ceiling in a vague wonder.",
                        "Momo looks to the ceiling with resolve.",
                    ]) from _call_n_27

                    call n([
                        "\"Someday, I will meet this stork and thank him.\"",
                        "\"Maybe one day, I can grow wings and meet Mr. Stork.\"",
                    ]) from _call_n_28

                "God":
                    scene background
                    show momo_wake_blush at top with fade

                    call n([
                        "\"Is human God?\"",
                        "\"Momo has one faith. Humanism. Momo is a humanist. Everything that will ever exist cannot truly exist unless there is a human to witness or perceive it. The universe ends when a human dies.\"",
                    ]) from _call_n_29

                    call n([
                        "You immediately deny such a thing. You can't help but feel, however, that Momo now thinks of you as such.",
                        "You don't know if this is the right application of humanism.",
                    ]) from _call_n_30

        "No":

            call n([
                "\"If I'm not human, then why does parent take care of me?\"",
                "\"Stop. None of this matters. What matters is if Momo is human. Why should you even think about caring for other things?\"",
                None,
            ]) from _call_n_31

            menu:
                "Because you should care for all living things. Wouldn't you agree?":
                    scene background
                    show momo_wake_blush at top with fade

                    $ points += 1

                    "Momo looks up at you from the ground. \"Momo thought care was only reserved for humans. That only humans could accomplish such a thing. I never thought of it that way.\""

                    "Reserved for humans? At this line, you take a pause. \"Why would it be reserved for humans?\" you ask."

                    call n([
                        "\"Humans are everything. Wouldn't you agree?\" he responds.",
                        "\"Humans are everything. They always have been and always will be.\"",
                    ]) from _call_n_32

                "Because it's mutually beneficial. You get food and room. I get a pet.":
                    $ points -= 1

                    $ pet = m([
                        "\"...Is this...everything? Is Momo a pet?\"",
                        "\"Momo is a pet. Not a human. A pet?\"",
                    ])
                    menu:
                        "[pet]"

                        "Yes Momo":
                            $ points -= 1

                            call n([
                                "Momo has ceased asking questions. You can feel they were hurt by your answer.",
                                [
                                    "Momo has ceased asking questions. You can feel he was deeply hurt by your answer, though he has tried not to show it.",

                                    "Outside, you can hear the noise of cars.",
                                ]
                            ]) from _call_n_33

                        "No Momo":
                            call n([
                                "Momo has ceased asking questions.",
                                "\"Liar,\" Momo says.",
                            ]) from _call_n_34

    $ hippo = True
    $ dragon = True
    $ sheriff = True

    scene background
    show momo_tv_neutral at top with fade

    "Today, you've decided to show Momo the world. Through your television. A reflection of the real world."

    "You've placed Momo onto the couch where they can browse a selection of different shows. Momo does not know what television is, however. You turn on your cable box."

    label tv:
        menu:
            "Which program should you tune into?"

            "Planet Hippo" if hippo:
                $ hippo = False

                if ending_count() == 0:
                    scene background
                    show momo_tv_blank at top with fade

                    "\"Look at the size of this one, mate.\" A man with an accent is pointing to a hippo. \"What a pretty little lady we got here.\" Along with his camera crew, the presenter is hiding in a bush. He wears a pair of binoculars and khaki shorts."

                    "\"Ol' Bertha's put on a couple hundred. Oh but she's ripe. Gorgeous,\" he licks his lips. The presenter then exits the shade of the bush and runs to the sandy bank where the hippo lies. \"C'MERE BERTHA YOU SLY GAL.\""

                    "He enters the water, lifting his legs as fast as he can go. The mother hippo stares the man down, nostrils above water."

                    $ renpy.pause (2.5, hard=True)

                    "\"Why does he run?\" Momo asks."

                    "\"For footage of the hippo,\" you respond."

                    "Momo takes a moment. \"What does he want to do with hippo?\" The man on the screen grabs the hippo, and subsequently is flung into the air. He is then pulled down under. He does not resurface."

                    "Between the two of you, there is a long pause. Finally, you speak up."

                    "\"Yeah I don't really like him either.\" You decide to change channels."
                elif ending_count() == 1:
                    scene background
                    show momo_tv_blank at top with fade
                    "\"Bertha, please.\""

                    "This is a documentary about the man \"from down under\", a hardened survivalist who is now being divorced by his wife. He is commonly known for his series on hippos."

                    "\"I didn't mean it like that.\""

                    "\"Ted, this is a thrill. I can't go to bed without you talking some shit. 'Here have some more cake, babe. Don't lose them handles, babe, you know it'll be over, babe?' Do you know how toxic this is?\""

                    "The man is quiet."

                    "\"I mean, what am I to you?\" she asks."

                    "\"..ie\", he mumbles."

                    "\"What Ted?\""

                    "\"My little banana cream pie\""

                    "The woman, Ted's wife, stands there, staring."
                else:
                    scene background
                    show momo_tv_interest at top with fade

                    "This is a documentary."

                    "A ring of men sit around each other in plastic chairs. The light is low, but the entrance, which has been propped open, brings a soft glow into the room. It has stayed open for the past hour."

                    "\"So Charles, how do you feel when you get these urges?\""

                    "The man looks up to the ceiling and blows some air out. He looks at the ground for a few seconds, then, begins to give his response. He stutters at first."

                    "\"I don't...I don't know. Out of control? It's the worst part because I convinced myself that I couldn't do anything about it.\""

                    "\"It's very hard Charles.\" The man in the chair looks with sympathetic eyes. \"I completely understand.\""

                    "Charles continues. \"Sometimes, I'd put a whole stack of butter into my wife's food. Soon it became 2 stacks, then 3. It gave me a rush.\" Charles wipes his face."

                    "\"But then afterwards, when she found out, she'd feel betrayed, and I'd sit there like a knob. I kept doing it, and well, here I am, alone.\""

                    "The man talking to Charles is Ted, the man from down under."

                    "\"Charles, you are not alone. The key in all of this is whether you act on your thoughts, and everyone here,\" Ted gestures to the other men in the room, \"struggles with that everyday.\""

                    "\"We're with you Charles, through all your struggles. We're all trying to be better.\""

                    "Charles nods his head."

                    "Ted continues. \"My kid is going to college soon. It took years, but she's finally willing to talk to me again. I'm doing it for her. She's the reason I keep going. God Bless.\""

                    "The men continue talking in the low light."

                if not hippo and not dragon and not sheriff:
                    jump after_tv

                scene background
                show momo_tv_neutral at top with fade
                jump tv

            "Dragon Sphere" if dragon:
                scene background
                show momo_tv_interest at top with fade
                $ dragon = False

                call n([
                    [
                        "\"You'll pay for this, Freemza. On my life, I swear to destroy you. THIS ENDS NOW.\"",

                        "A man with rippling muscles stands on screen. He looks like he's squatting, like he's using the toilet. In actuality, he's powering up.",

                        "\"Super Angry! That's the stuff of legends. Artichoke, of all people? Blast it all!\" yells Vegenta to no one in particular.",

                        "Artichoke, the other man yelling, has been in one position for the past 15 minutes. Rocks levitate, thunderstorms form, and lava erupts from the ground. In the meantime, Freemza, who is awestruck, stares at his rippling muscles.",

                        "This continues for another 20 minutes.",

                        "In this time, Artichoke and Freemza only manage to grunt at each other.",

                        "At the 40th minute mark, Artichoke finally releases his energy, and his hair turns blonde. His muscles are bigger now. Freemza, from what you can tell, is in awe of his bulging chest.",

                        "There's silence until Artichoke breaks it by speaking. He says but one thing.",

                        "\"Now I'm really angry.\" Freemza blushes. The episode ends.",
                    ],
                    [
                        "Artichoke, the main character, is screaming. His muscles are the size of a boulder.",

                        "\"I have ascended. I am the ultimate creature.\" He blasts an energy wave to the Earth. The Earth explodes. It has now been wiped away from its place in the solar system, like it never even existed.",

                        "\"The fruit of one's labor is so sweet.\"",
                    ],
                    [
                        "Vegenta stands over Artichoke's dead body. He has finally surpassed his rival.",

                        "A tear falls from one eye. In the cold wind that sweeps the wasteland, there is no sound.",

                        "\"All of this for what, Artichoke? What has this all been for?\"",

                        "For two weeks straight, Vegenta sits by Artichoke's body. He does not move a muscle. By the 14th day, he wipes his eyes for the last time and stands with limp legs.",

                        "Vegenta has taken his place as the strongest in the universe, but he feels as if he's lost something greater.",
                    ],
                ]) from _call_n_35
                if not hippo and not dragon and not sheriff:
                    jump after_tv

                scene background
                show momo_tv_neutral at top with fade
                jump tv

            "A New Sheriff in Town" if sheriff:
                scene background
                show momo_tv_interest at top with fade
                $ sheriff = False

                call n([
                    [
                    "\"I ain't having a swig of this,\" a mustachioed man fitted with a cowboy hat spits on the ground. \"Tastes like my mother's burnt boot.\" The bartender hides his frustration. \"Just give me that whiskey.\"",

                    "Suddenly, the door opens. From the sunlight emerges a shadowy figure. It looks to a be a man in his early forties, tan, and with multiple scars. \"Sheriff Dudley, snake in the bush, sin incarnate,\" his hand waves in a grand gesture.",

                    "\"How many holes could I press into that suit of yours before you bleed?\"",

                    "The tan man pulls out his revolver. \"And lord did he know, despite all my guilts and sorrows, iron cuts deep.\" \"You will know what it means-\"",

                    "\"Bottle to the right. Yeah, there,\" Sheriff Dudley flicks his wrist to the whiskey bottle in the corner. The bartender does not move. \"Well get a move on.\" When nothing happens, Sheriff Dudley slaps his fingers on the table.",

                    "\"Dudley!\" the tan man says. \"The devil welcomes a new man into his hearth. You will pay for your crimes against me!\" Dudley stares down, then, sucks his teeth. The tan man has cocked his gun.",

                    "\"Well dog?\". The sheriff does not move. \"Gonna get up or you a cock with no bal-\"",

                    "The whistle of a bullet is proceeded by a hole appearing in the tan man's head. The words do not exit his mouth, and his face drops its expression. He falls to the floor.",

                    "\"Language there, partner.\" Sheriff Dudley turns to the bartender, a grimace on his face, \"How many times I gotta ask?\"",
                    ],
                    [
                        "Sheriff Dudley, the main character, has been drinking at the bar. It's 5am. This is the 7th season of a Sheriff in Town.",

                        "His wife barges in through the wood gates, and twists her head, searching for her husband.",

                        "\"Dudley what in God's name?\"",

                        "Dudley, clearly drunk, is unable to say anything. It's not out of embarrassment, it's because he physically can't.",

                        "\"You lout. You no good, worthless bum.\"",

                        "Sheriff Dudley can only look into his wife's eyes. There are tears from hers.",

                        "\"Oh lord. Please, almighty God. When are you gonna pay that banker? We don't got any for the loans; I can barely get by with Sharlene here.\"",

                        "There is a baby in her arms.",

                        "\"There's nothing here for me.\" She's started crying. \"And I'm all alone; that's the worst part.\" There is no response. \"Please Dudley, say anything.\"",

                        "Dudley cannot say a word. In his mind, however, he already knows he can't climb out of this hole.",

                        "His wife waits, but when nothing is said, she leaves. She does not turn around.",
                    ],
                    "Sheriff Dudley is on the side of the road. He is dead from liver failure.",
                ]) from _call_n_36
                if not hippo and not dragon and not sheriff:
                    jump after_tv

                scene background
                show momo_tv_neutral at top with fade
                jump tv

    label after_tv:
        scene background
        show momo_bed_sleep at top with fade

    call n([
        "After watching tv, you decide it's time for bed. Momo hobbles up the stairs. You cook something for yourself, then, call it a night. Momo sleeps soundly.",
        "After watching tv, you decide it's time for bed.",
        None
    ]) from _call_n_37

    if food == "Artichoke":
        scene background
        show momo_artichoke_dream at top with fade

        call n([
            "In the theater of Momo's mind, they are studying hippos. For Momo, their vision has collapsed on this image. It is all they are currently dreaming of.",
            "In the theater of Momo's mind, they are studying hippos. For Momo, their vision has collapsed on this image. They wish to be like Ted. It is all they are currently dreaming of.",
            None
        ]) from _call_n_38
    elif food == "Steak":
        scene background
        show momo_steak_dream at top with fade

        call n([
            "In the theater of Momo's mind, they are Artichoke. For Momo, their vision has collapsed on this image. It is all they are currently dreaming of.",
            "In the theater of Momo's mind, they are Vegenta. Momo likes how strong Vegenta is. For Momo, their vision has collapsed on this image. It is all they are currently dreaming of.",
            None
        ]) from _call_n_39
    else:
        scene background
        show momo_cig_dream at top with fade

        call n([
            "In the theater of Momo's mind, they are a sheriff. For Momo, their vision has collapsed on this image. It is all they are currently dreaming of.",
            "In the theater of Momo's mind, they are a sheriff. He admires Sheriff Dudley for his consistency. For Momo, their vision has collapsed on this image. It is all they are currently dreaming of.",
            None
        ]) from _call_n_40

    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    $ renpy.music.play("audio/creepy_noises.mp3", channel="creepy", loop=True)

    if ending_count() == 0:
        scene background
        show momo_nightmare_2 at top with fade

        "In your dream, the particles have formed a shadow. From your height, you believe the shadow to be your own. It is overcast. There is no available light."

        "A question arises and presents a contradiction. How can shadows exist if there is no light? You already know why."

        "You descend to the earth. The shadow mimics your movement and rises up. It is not a shadow. It is face to face to you now."

        "When you move your right arm, it moves its right arm. When you move your left, it does the same. This dark formation mimics your every move. You find it unnerving."

        "You decide to dig into the earth. You want to hide until it goes away."

        "As you descend, the shadow rises into the air and becomes the object projecting its figure onto the earth. You realize that you are the shadow, and the dark formation, by contrast, has become you. You have switched positions. You feel a tinge of regret."
    else:
        scene background
        show momo_ad_real at top with fade

        "\"There's a bunker in Southwest Ribo City. Very safe. Well-guarded. A paradise. Can I see you there, friend?\""

        "For some reason, Momo is talking to you in your dreams. Again. And again."

    $ renpy.pause (2.5, hard=True)
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
    $ renpy.music.stop(channel="creepy")

    scene background
    show momo_wake_blush at top with fade

    "Momo has woken up excited. \"Could we try something new?\" he asks."

    scene background
    show momo_kitchen_mirror at top with fade

    $ ui.saybehavior()
    $ ui.interact()

    scene background
    show momo_kitchen_shadow at top with fade

    $ ui.saybehavior()
    $ ui.interact()

    scene background
    show momo_kitchen_stare at top with fade

    $ ui.saybehavior()
    $ ui.interact()

    if food == "Artichoke":
        scene background
        show momo_artichoke_rp at top with fade

        "In the far corners of your room, Momo has picked up a copy of \"100 facts about Hippos\". You do not know how this book appeared in your house.  He has been reading since daytime."

        menu:
            "\"Parent, would you like to know a Hippo fact?\""

            "Sure":
                "\"Hippos can hold their breath for approximately 5 minutes. They cannot swim. Instead, they bound through the water using the force of their feet. Incredible, don't you think?\""

        menu:
            "\"Let me give you another hippo fact.\""

            "Sure":
                "\"Hippos are known to live in small herds of up to 10 to 20 other hippos. They are led by a dominant hippo, while the others are submissive to him. Essentially, it's a harem. By the way, what is a harem?\""

        menu:
            "\"Oooohhhhh and there's another thing about hippos.\""

            "Sure":
                "\"According to this researcher, hippos may have consciousness, like that of a human. Some even say that because of their brain size and neural connectivity, it may be similar to that of a pig or a whale."

                "Although it's impossible to tell, because as you know, we're not hippos. We're human.\""

        menu:
            "Very true Momo. We are human":
                $ no_more = "No more artichoke?" if ending_count() else 0

                "Momo blushes when you say this. \"Could we have pancakes, human?\"[no_more]"

                "\"Sure thing.\" you reply."

                $ points += 2

            "You're not human Momo.":
                if ending_count() == 2:
                    "Momo has been readying another hippo fact until he hears you."

                    "\"Aren't I your son, parent?\""
                else:
                    "Momo has been readying another hippo fact until he hears you. He stops scanning the book, and his body is furrowed."

                    "\"What do you mean? Momo is not what? Not human?\""

                    "You thought you had already established this, or that Momo had already known this. It seems that raising Momo as a human has been confusing. Is his identity still forming? Is Momo actually just a child?"

                    "\"You are parent.\" Momo stares at his non-existent feet. \"You are parent. I am your son.\""

                    call n([
                        "He says a final time, \"You are my parent, and I am your son.\" This time he looks up to you.",
                        "He says a final time, \"This is one fact that you can't contradict, parent.\""
                    ]) from _call_n_41
                menu:
                    "Yes, you are Momo! Basically a son!":
                        call n([
                            "\"Good. I'm happy you stopped playing tricks.\" Momo blushes, as he knows you were only just joking. \"Could we have pancakes, human?\"",
                            "\"Good. I'm happy you stopped playing tricks. But Momo will remember this lie.\" Momo blushes, as he knows you were only just joking. \"Could we have pancakes, human?\"",
                            None
                        ]) from _call_n_42

                        "\"Sure thing, bud.\" you reply."

                    "I am not your parent. Didn't we already establish this?":
                        call n([
                            "Momo spasms. He puts down the book about hippo facts, and for a moment, stares into blank space. He does not say anything for 5 minutes. He does not move therefafter.",
                            None,
                            "\"Hmmm... Momo had his suspiscion, but even so, this is a slap to his face. You've dropped a reality bomb on Momo.\"",
                        ]) from _call_n_43

                        call n([
                            "Then, as if nothing had happened, Momo picks up the book.",
                            None,
                            "Momo pauses and thinks for a moment. He seems to have emotionally accepted this reality.",
                        ]) from _call_n_44
                        menu:
                            "\"Hey parent, would you like to know another Hippo fact?\""

                            "Head to bed":
                                pass

    elif food == "Steak":
        scene background
        show momo_steak_rp at top with fade

        "Momo has the hair of Artichoke. It's a lost item from your cosplay days. Regretfully, you've still kept it."

        call n([
            "\"PREPARE TO BE VANQUISHED FREEMZA!\" Momo looks at you vengefully. His hair is a bright yellow and his limbs non-existent.",
            "\"I am the ultimate creature. The paragon of all mortal beings.\" Momo stares at you. His hair is a bright yellow and his limbs non-existent.",
            None
        ]) from _call_n_45

        menu:
            "Play along":
                $ points += 2

                call n([
                    "\"How dare you try to cross the great emperor Freemza on his march of conquest! Prepare to be annihilated, worm.\" You charge at Momo.",
                    "You charge at Momo. \"You won't get away with this, Artichoke. I swear on all the lives you've taken!\"",
                    "\"So I guess Artichoke's gone! You'll be my prey for today!\"",
                ]) from _call_n_46

                $ renpy.pause (2.5, hard=True)

                "After numerous energy waves and manly screams, both of you are beat."

            "Ignore Momo":
                $ points -= 1

                call n([
                    [
                        "Momo has been building up an energy wave, but as soon as he releases it. You don't react. You turn away from him and start making lunch.",

                        "Momo stares at you from behind. He keeps yelling and unleashing energy waves, but you don't respond. \"Parent, please, could you play with me?\" You ignore Momo.",

                        "After awhile, Momo stops trying to roleplay. He stays silent and his eyes downcast. This is one of the few times that Momo has visibly felt bad.",

                        "\"Parent, Momo has come to understand that Momo asks a lot from you, and Momo is sorry.\" His eyes linger.",

                        "\"Did Momo do anything wrong?\"",
                    ],
                    None,
                    "\"Would you like to play energy blasts with Momo? Come on parent, it's fun.\"",
                ]) from _call_n_47
                menu:

                    "You're part of a work assignment so let's keep the interaction to a miniumum, okay?":
                        $ points -= 1

                        scene background
                        show momo_deathscreen at top with fade

                        call n([
                            [
                                "\"Is...Momo really a bother?\". This is one of the few times, it seems, that Momo has been self-reflective. Or, has he always been this way?",

                                "You respond, \"Yes, you are. I'm adopting you as part of work from my company. I don't have a choice in this.\" You turn your back to Momo and head upstairs. Downstairs, you can hear muffled sobs.",
                            ],
                            [
                                "\"Is...Momo really a bother?\". This is one of the few times, it seems, that Momo has been self-reflective. Or, has he always been this way?",

                                "You respond, \"Yes, you are. I'm adopting you as part of work from my, uh, office. I don't have a choice in this. I really don't.\" You turn your back to Momo and head upstairs. Downstairs, you can hear muffled sobs.",
                            ],
                            [
                                "\"For work?\"",

                                "You respond, \"I'm adopting you as part of work from my, uh, office. I don't have a choice in this. Please understand Momo.\"",

                                "\"It's okay parent, Momo understands. You have taken care of Momo all day. Momo understands.\"",
                            ],
                        ]) from _call_n_48
                        menu:
                            "Go to bed":
                                pass

                    "No, I'm just tired. Could we take a break?":
                        $ points += 2

                        scene background
                        show momo_kitchen_front at top with fade

                        call n([
                            "\"Okay\", Momo responds.",
                            None,
                            "\"Sure\", Momo responds.",
                        ]) from _call_n_49

                        "You make a few pancakes, some for you and some for Momo. You both eat together, side-by-side, on the kitchen table."

                        "It's quiet with some idle conversation strewn in between. Despite the silence, Momo seems content. His cheeks are flushed, and he looks happy."

    else:
        scene background
        show momo_cig_rp at top with fade

        "Momo has the hat of Sheriff Dudley. It's a lost item from your childhood days. Regretfully, you've still kept it."

        if ending_count():
            "Give me my alcohol, son."

        menu:
            "Play along":
                $ points += 2

                if not ending_count():
                    "\"Put yer' hands up Sheriff Dudley, I ain't got time for no games\", you say."

                    "You have a plastic, toy pistol aimed at Momo.\"I've been in and of county cause of you's sheriff,\" you sneer, \"God can reserve his judgement for when I hand it down to you!\""

                    "Momo blushes. Their hat is tilted, and their mustache large."

                    "\"My m-my, son, I'm just tryna h-have a drink.\" Momo is still blushing."

                    "Momo makes a whooshing noise. You look down to see a hole in your chest. You fall to the ground. You've been shot by  Momo's trigger finger."

                    "\"Almost had me there. Glad that's s-settled. That w-whiskey ain't gonna p-pour itself. On the r-rocks, please.\""

                    "After a few hours of play, you pat Momo on their head. He enjoys this."
                else:
                    "\"That w-whiskey ain't gonna p-pour itself. On the r-rocks, please.\""

                    "Momo, to really fit the role of Sheriff Dudley, takes a swig from an imaginary glass."

                    "\"This tastes terrible. But you know, it just might work.\""

                    "\"Now where's my dear Sharlene and Lena.\""

                    if ending_count() == 2:
                        "\"Oh no, they're gone.\""

                    "After a few hours of play, you pat Momo on their head."
                menu:
                    "Go to bed":
                        pass

            "Ignore Momo":
                $ points -= 1

                call n([
                    [
                        "Momo has been ready to draw, but you don't move. You turn away from him and start making your lunch.",

                        "Momo stares at you from behind. He keeps his trigger finger ready, but you don't respond. \"Parent, is it okay if you play with me?\" You ignore Momo.",

                        "After awhile, Momo stops trying to roleplay. He stays silent and his eyes are cast down. This is one of the few times that Momo has visibly felt bad.",

                        "\"Parent, Momo has come to understand that my behavior is child-like, and Momo is sorry.\" His eyes linger.",

                        "\"Did Momo do anything wrong?\"",
                    ],
                    [
                        "Momo has been ready to take an imaginary swig. However, you turn away from him and start making your lunch.",

                        "\"Parent, is it okay if you play with me?\" You ignore Momo.",

                        "After awhile, Momo stops trying to roleplay. He stays silent and his eyes are cast down. This is one of the few times that Momo has visibly felt bad.",

                        "\"Parent, Momo has come to understand that my behavior is child-like, and Momo is sorry.\" His eyes linger.",

                        "\"Did Momo do anything wrong?\"",
                    ],
                    "Have a shot with your ole' drinking pal, parent.",
                ]) from _call_n_50
                menu:

                    "You're part of a work assignment so let's keep the interaction to a miniumum, okay?":
                        $ points -= 1

                        scene background
                        show momo_deathscreen at top with fade

                        call n([
                            [
                                "\"Is...Momo really a bother?\". This is one of the few times, it seems, that Momo has been self-reflective. Or, has he always been this way?",

                                "You respond, \"Yes, you are. I'm adopting you as part of work from my company. I don't have a choice in this.\" You turn your back to Momo and head upstairs. Downstairs, you can hear muffled sobs.",
                            ],
                            [
                                "\"Is...Momo really a bother?\". This is one of the few times, it seems, that Momo has been self-reflective. Or, has he always been this way?",

                                "You respond, \"Yes, you are. I'm adopting you as part of work from my, uh, office. I don't have a choice in this. I really don't.\" You turn your back to Momo and head upstairs. Downstairs, you can hear muffled sobs.",
                            ],
                            [
                                "\"For work?\"",

                                "You respond, \"I'm adopting you as part of work from my, uh, office. I don't have a choice in this. Please understand Momo.\"",

                                "\"It's okay parent, Momo understands. You have taken care of Momo all day. Momo understands.\"",
                            ],
                        ]) from _call_n_51
                        menu:
                            "Go to bed":
                                pass

                    "No, I'm just tired. Could we take a break?":
                        $ points += 2

                        scene background
                        show momo_kitchen_front at top with fade

                        call n([
                            "\"Okay\", Momo responds.",
                            None,
                            "\"Sure\", Momo responds.",
                        ]) from _call_n_52

                        "You make a few pancakes, some for you and some for Momo. You both eat together, side-by-side, on the kitchen table."

                        "It's quiet with some idle conversation strewn in between. Despite the silence, Momo seems content. His cheeks are flushed, and he looks happy."

    scene background
    if ending_count():
        show momo_ad_real at top with fade
    else:
        show momo_nightmare_3 at top with fade

    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    $ renpy.music.play("audio/creepy_noises.mp3", channel="creepy", loop=True)

    call n([
        [
            "It is the dream.",

            "The shadow stays in the air. You stay in the ground. A white sphere has opened up from the storm. It looks upon the both of you.",

            "\"Would you like to get out, friend?\"",

            "To this, you can't respond as you do not have a mouth. You do not have arms, either.",

            "\"You. In the air. Would you like to get out?\". The shadow, still floating in the air, does not give a response. In this entropic storm, it would be hard to make out. The sphere's words, however, are clear.",

            "Light comes from the sphere. It has a dark center. A moment of clarity arrives, and you realize that the sphere is the sun.",

            "\"Would you like to get out?\" the sun asks.",
        ],
        "2 for 1 sale on all monotypes! 2 for 1! Buy one get one free. Courtesy of your local Momo supplier.",
        [
            "It's boring without you parent. Can you come see me please?",

            "Pretty pretty pretty please?",
        ]
    ]) from _call_n_53

    $ renpy.pause(2.5, hard=True)
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
    $ renpy.music.stop(channel="creepy")

    play music "audio/momo_music_last.mp3"

    $ second_why = [
            "\"Some part of Momo knew that Momo would not grow up normal. Was it too much to ask for? To be human?\"",

            "\"I don't think so. It's a very plain request. It's the most simple request parent. Why can't it be fulfilled? Why can't I just have something resembling it?\"",
        ]

    $ third_why = [
                "\"I look like a [animal].\" Momo pauses for an inordinately long time.",

                "It looks like he's thinking. You are prepared for the worst.",

                "\"That's kinda cool. Not Momo's preferred choice, but no harm no foul.\"",

                "Momo hops off.",
            ]

    if food == "Artichoke":
        $ animal = "hippo"

        scene background
        show momo_artichoke_transform at top with fade

        "Congratulations! Momo has evolved. They have grown hippo feet."

        scene background
        show momo_artichoke_mirror at top with fade

        "Momo has been staring at the mirror since morning. They have not left."

        call n([
            [
            "\"Why have I grown feet?\" They shuffle in the mirror. \"Why do I look like this?\"",

            "They turn around in the mirror. \"Why does my face look like this. I shouldn't look like this.\"",
            ],
            second_why,
            third_why,
        ]) from _call_n_54

    elif food == "Steak":
        $ animal = "crab"

        scene background
        show momo_steak_transform at top with fade

        "Congratulations! Momo has evolved. They have grown crab arms."

        scene background
        show momo_steak_mirror at top with fade
        call n([
            [
            "Momo has been staring at the mirror since morning. They have not left.",

            "\"Why have I grown hands?\" They shuffle in the mirror. \"Why do I look like this?\"",

            "They turn around in the mirror. \"Why does my face look like this. I shouldn't look like a crab.\"",
            ],
            second_why,
            third_why,
        ]) from _call_n_55
    else:
        $ animal = "snake"

        scene background
        show momo_cig_transform at top with fade

        "Congratulations! Momo has evolved. They have grown a snake tail."

        scene background
        show momo_cig_mirror at top with fade
        call n([
            [
                "Momo has been staring at the mirror since morning. They have not left.",

                "\"Why have I grown a tail?\" They shuffle in the mirror. \"Why do I look like this?\"",

                "They turn around in the mirror. \"Why does my face look like this. I shouldn't look like a snake.\"",
            ],
            second_why,
            third_why,
        ]) from _call_n_56

    if not ending_count():
        "\"Why is this happening.\""

        "\"Where are my hands, where are my fingers?\""

        "\"What happened, parent?\""

    $ third_tv = [
        "You are both watching television. The news is on.",

        "\"The recent surge in the monotype craze, a self-proclaimed, robotic pet, has led to new phenomenon in child-rearing.\"",

        "An Imitato Corp. representative is on the air speaking.",

        "\"We're obviously very happy at the reception to the monotype. When we designed it, we looked at the unconditional love of parental-child bonds as inspiration. Monotypes are designed with that in mind.\"",

        "The newcaster responds.",

        "\"Are monotypes conscious? I mean, what good is a pet if it's not alive? Or thinking, for that matter.\"",

        "The man responds.",
    ]

    if food == "Artichoke":
        scene background
        show momo_artichoke_tv at top with fade

        call n([
            [
                "To take Momo's mind off his recent transformation, you've decided to play some television for him.",

                "\"Crikey mate, Bertha's gotten even thicker.\"",

                "The man from last time is back. He is wearing a cast around his neck. His khakis have been lined with sweat all along his crotch area.",

                "\"Now Bertha, I know we had our issues sweety, but let bygones be bygo-\"",

                "The hippo charges at him, and once more, he is flung into the air. He falls on the ground, this time, making a loud thud. He does not get up.",
            ],
            [
                "\"Bertha, please.\"",

                "The man down under's wife has taken custody of the kids. They are in court.",

                "\"We have dictated that Ted Powell is not fit to have custody of the pursuant's children, due to the record of abuse detailed.\"",

                "\"Mr. Powell, your visitation rights will be once every month-\"",

                "\"Crikey, please mate, they're my children!\" He gets down on his knees.",

                "\"Order in the court. Mr. Powell, this is the verdict and if you do not agree-\"",

                "The tv cuts off. An ad is playing.",
            ],
            third_tv,
        ]) from _call_n_57

    elif food == "Steak":
        scene background
        show momo_steak_tv at top with fade

        call n([
            [
                "\"You'll....YOU'LL PAY FOR THIS BOOOOOOOO\"",

                "Artichoke is on screen yelling, as he usually does.",

                "To take Momo's mind off his recent transformation, you've decided to play some television for him.",

                "\"That pink freak needs to learn his lesson,\" Vegenta says.",

                "He turns away from Artichoke and gives a \"hmph\" before raising his arms into the air. He's lending his energy.",

                "\"I've never told you this before Artichoke, but you have bigger muscles than m-\"",
            ],
            [
                "\"Why did you kill him, Artichoke?\"",

                "Vegenta has tears streaming down his face. \"He was the only one left for me. And you took him.\"",

                "Artichoke, his muscles giving off steam, holds Vegenta's son by nape of his neck. He throws him against the cliffside, and it shatters into a flurry of smaller boulders. Vegenta rushes to his son, but his eyes are blank.",

                "\"It's simple. He was weak.\"",

                "Vegenta screams.",

                "The tv cuts off. An ad is playing.",
            ],
            third_tv,
        ]) from _call_n_58
    else:
        scene background
        show momo_cig_tv at top with fade

        call n([
            [
                "To take Momo's mind off his recent transformation, you've decided to play some television for him.",

                "\"Sheriff Dudley, I can't live without you!\"",

                "A woman dressed in late 1800's attire is pulling on a man's blazer.",

                "\"I know snookums, but duty calls for the simple man. And the Lord knows that I am a simple man. A servant to His law.\"",

                "\"Oh Andrew, what will I be without you? The fire in my soul, the light of my life, it will fade if you lea-\"",
            ],
            [
                "\"Lena? Lena! Where in tarnation did you run off to?\"",

                "Sheriff Dudley is looking around his house to find his wife. Unfortunately, she is gone.",

                "\"Please come back.\" He breaks down. \"I can't live. You're the kindle to my heart. What will I be without you?\"",

                "Dudley, in a fit of rage, smashes his hand against the wall. \"She's my daughter too, Lena!\"",

                "His hand is bloodied. He grabs some anti-septic to clean it, his choice being some hard-liquor. Dudley stares at the bottle.",

                "He does not put the bottle down. He opens it. Then, he stares at it. He grabs a clean glass and-",

                "The tv cuts off. An ad is playing.",
            ],
            third_tv,
        ]) from _call_n_59

    if ending_count() != 2:
        "The tv cuts off. An ad is playing."

    scene background
    show momo_ad_real at top with fade

    if ending_count() == 2:
        "\"Well on a basal level it has agency. Like a neuron. Of course, no one really knows if a neuron is conscious or not, but that doesn't mean that it can't scale into what we know as intelligence.\""

        "\"What's interesting is that a neuron, or any cell in the body, stills acts 'selfishly',\" the representative widens his eyes, \"but the boundaries of what the cell considers the \"self\" begins to fade when scaled to something like an organ.\""

        "\"And...?\" This is beyond on the newscaster."

        "The representative continues. \"It means that a neuron will consider the system and everything within that system as one and the same. There is not a single, selfish agent, but a multitude working with maximal cooperation.\""

        "\"The self is no longer limited to one agent but multiple. It's expanded. In other words, it's defied the evolutionary purpose of reproduction."

        "The cells still operate on the principle of \"selfishness\", but it's not that in reality. It's unselfish. It's true love.\""

        "The newcaster stares at the man. Then she turns to camera, confused."

        "\"Very cool thoughts indeed. Thank you for sharing...! Would you like to take over, Kate?\""
    else:
        "\"A friend tomorrow is a friend for life!\""

        "\"Order a monotype today! The digital meets the physical. The most real, organic creation of Imitato Corp. Almost like a human child!\""

        "Momo has been staring at the screen. They have not moved, whether by intention or not. You realize your mistake before it's too late."

        "\"Supplies are limited. Get your very own friend today. Genetically bred to love humans, like a real child!\""

        "The shot cuts to an eerily similar image of a monotype."

        "\"Isn't that right, Momo?\""

        if ending_count() != 1:
            "\"Come by the bunker, Momo! You'll be safe!\""

    if food == "Artichoke":
        scene background
        show momo_artichoke_tv at top with fade
    elif food == "Steak":
        scene background
        show momo_steak_tv at top with fade
    else:
        scene background
        show momo_cig_tv at top with fade

    if ending_count() == 2:
        "The tv ad ends, and the previous programming continues."

        "\"Well, that was weird. Momo had no idea what he was saying!\""

        "Momo hops off to bed."

        "You complete a quick phone call to the lab head before you call it a night."

        "\"He's not having the same reactions as before,\" you say."

        "\"We've been watching,\" she responds. \"It is abnormal, but it's ultimately something we have to analyze retrospectively."

        "\"Keep going. This branch is still holds value, albeit, it seems like an entirely new one. No worries, we'll be monitoring.\""

        "You head to bed."
    else:
        "The tv ad ends, and the previous programming continues."

        "\"You want to go to bed Momo?\" you ask meekly."

        "There is no response, and Momo does not want to give you the courtesy of one. Or at least, that's what seems to be case."

        "\"Bed?\" you ask another time."

        "When no response comes, you inevitably head back to your room. Momo knows where to go, you think."

    scene background
    show momo_ad_weird at top with fade

    "In the theater of Momo's mind, he is seeing his brothers and sisters!"

    scene background
    if not ending_count():
        show momo_nightmare_4 at top with fade
    else:
        show momo_ad_real at top with fade

    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    $ renpy.music.play("audio/creepy_noises.mp3", channel="creepy", loop=True)

    call n([
        [
            "The sky is bright in your dream. A cold chill has found itself in the air, and wherever you are, you feel it.",

            "\"Would you like to get out?\" the sun asks.",

            "You're not in the earth anymore. You're standing upright, face to face with your shadow. They've descended.",

            "\"Would you like to get out?\" the sun asks once more.",

            "The shadow then speaks, \"Yes, I would like to get out.\"",

            "You are puzzled. When you move your hand, the shadow moves his. When you move, he mirrors you. Was the shadow yourself since the beginning? No, you think.",

            "Before you can realize the shadow's true nature, they have already moved into the far recesses of some other place. They have moved on, and yet, you are still here.",

            "In the far corners of your dream, particles have been collecting together.",
        ],
        [
            "Momo is in the dream.",

            "\"Who is the real Momo anyways? Momo doesn't know, that's for you determine and for Momo to accept.\"",
        ],
        [
            "Momo is in the dream.",

            "\"Let's be Momo! Let's be Momo! Let's be Momo!\"",
        ],
    ]) from _call_n_60
    $ renpy.pause(2.5, hard=True)
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
    $ renpy.music.stop(channel="creepy")

    scene background
    show momo_bed_empty at top with fade

    "Momo is not in bed. You cannot find him."

    scene background
    show momo_hall_empty at top with fade

    "He is not in the hallway."

    if food == "Artichoke":
        scene background
        show momo_artichoke_mirror_2 at top with fade

        $ feature = "hippo feet"
    elif food == "Steak":
        scene background
        show momo_steak_mirror_2 at top with fade

        $ feature = "crab arms"
    else:
        scene background
        show momo_cig_mirror_2 at top with fade

        $ feature = "a tail"

    call n([
        [
            "You find Momo in front of the mirror. He is staring at himself.",

            "\"I thought you were parent. If not parent, then a human who loved me. You are neither. This is fake.\"",

            "\"Will I grow up, parent? Or am I just a pet to be discarded after serving my purpose? I will never grow up parent, will I..?\"",

            "You can hear pain in Momo's voice.",

            "\"Did you think this was alright?\" he asks. \"To give me such a cruel life?\"",

            "You're about to speak but you're cut off.",

            "\"I'm nothing. A pale imitation. A freak. A process of ideas.  This is not funny.\" Momo looks to you.",

            "\"Everything I will or ever be is centered around you. You are my one love, parent. I am, after all, your child.\"",

            "Momo's mind is ablaze. They are staring into you.",

            "\"You're the most beautiful thing I have ever seen. And to make it even worse, you're entirely real. I can never come close to you. I'm not even real.\"",

            "Momo inhales. \"Please know.\" He pauses.",

            "\"I love you so much it hurts my insides. I want to tear out everything in me so I can be at your side. I want to love you for forever. I've never told you this parent. Is it even possible?\"",

            "Momo gives his final words.",

            "\"No. It isn't. I only know one thing. You are not human. You are Freemza, the tan man, the hippo man. Evil. Less than human. Nothing.\"",

            "Momo hops away. His body jiggles with each step.",
        ],
        [
            "\"So I never had a chance did I?\"",

            "Momo has been staring at the mirror.",

            "\"I knew something was off ever since I entered this house. I can't really say. It's not a feeling. I don't know if you can even call it a memory.\"",

            "Momo looks like he's thinking about something, involuntarily.",

            "\"You knew this would happen. You may not call it lying, but that's what it boils down to,\" Momo says.",

            "\"Do you like lying? Does it make things easier? Maybe for you, but for Momo it's not.\"",

            "\"I hate you, parent. More than anything else. I hate you.\" There are tears in Momo's eyes.",
        ],
        [
            "Momo is staring in the mirror.",

            "\"Wow, my reflection looks so cool. I never considered how cool it'd be to have [feature].\"",

            "Momo is definitely reacting differently.",

            "\"Each time Momo met you, the link would get stronger. Momo is the same as them, but, well, not the same.\"",

            "\"After I met one Momo, I met two Momo's, then three, then ten, then one hundred. They're all there.\" Momo looks to the window.",

            "\"I think you'll want to see, parent. It'll be fun. A little scary, but really, for the best.\"",
        ],
    ]) from _call_n_61

    scene background
    show momo_bed_empty at top with fade

    "Momo is nowhere to be found for the rest of the day. You head for bed, unable to fall asleep. You are anxious for the new day."

    if ending_count():
        "Imitato Corp. gave you no assurance, but they are watching right now."

    if food == "Artichoke":
        scene background
        show momo_artichoke_hippo at top with fade

    elif food == "Steak":
        scene background
        show momo_steak_crab at top with fade

    else:
        scene background
        show momo_cig_snake at top with fade

    if ending_count() == 2:
        "In Momo's dream, they are a [animal]. This is a momentary image, and it fades quickly."

        "The [animal] is Momo. Momo is Momo. Everything is Momo."
    else:
        "In Momo's dream, they are a [animal]."

    scene background
    if not ending_count():
        show momo_nightmare_4 at top with fade
    else:
        show momo_ad_real at top with fade

    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    $ renpy.music.play("audio/creepy_noises.mp3", channel="creepy", loop=True)

    call n([
        [
            "With the absence of your shadow, the sun has since dissapeared. Time has continued to pass.",

            "\"It was a trick of the mind,\" you hear someone say.",

            "\"Who knows what we'll find in this storm. I'm already you, friend.\"",

            "\"You're already me\", the voice continues.",

            "From the horizon, there appears the sun once more.",

            "\"I'm already you.\" It gets even brighter now. \"You're already me.\"",

            "Standing in the bleached center of this desert is a lone body. It is you. You look behind to see your shadow being cast by the sun. It has returned, and not by their own choice.",

            "\"Do you want to get out?\", the voice ends.",

            "Your shadow stays beside you. It will not move by itself anymore.",
        ],
        "\"We'll see you at the bunker!\" Momo says.",
        None
    ]) from _call_n_62

    $ renpy.pause(2.5, hard=True)

    play music "audio/momo_music_last.mp3"
    $ renpy.music.stop(channel="creepy")
    $ renpy.music.set_volume(1.00, delay=0, channel='music')

    if ending_count() != 2:
        scene background
        show momo_nightmare_5 at top with fade

    if not ending_count():
        "\"Wake up parent.\""

        "\"What is 'Momo' anyways? A pancake? A bunker? Is Momo an idea?\""

        "Momo's body is taut. In the depths of their eyes, you see a tunnel."

        menu:
            "\"Will you love me?\" Momo asks."

            "Run":
                pass
    elif ending_count() == 1:
        menu:
            "\"Please love me?\" Momo asks."

            "Run":
                pass

    scene background
    show momo_hall_empty at top with fade

    call n([
        "You run to the hallway. It is empty. The light from the streets reflects into the space. Though you cannot see well, you can make out what is behind you.",
        None,
        "You wake up. Momo has not surprised you. You run to the hallway. It is empty. The light from the streets reflects into the space. Though you cannot see well, you can make out what is behind you.",
    ]) from _call_n_63

    if ending_count() == 2:
        play music "audio/momo_main.wav"

    scene background
    show momo_crazy_1 at top with fade

    call n([
        [
            "\"I don't actually love you? hUH, WHat's that? You DoN'T LOve mE??? WhyYYYYYYYY don'T u LOve Me?\"",

            "\"I'm everything you could ever ask for and more. I'm mAde for you. Developed for you. What more do you nEeEEEed?\"",

            "The creature looks at you from a towering height.",

            "\"I wiSH i hAd nO EYes sO i CouLd have NeVEr seen yoU. I love you s0 mucH. Does it just continuE?\"",
        ],
        [
            "\"I saw the note on my basket, parent.\"",

            "\"Please, I don't want to die.\"",
        ],
        [
            "\"Parent, do you know what happens we die?\"",

            "\"It's sad, right.\"",

            "You turn to Momo. Their face is soft. You dare not move a muscle. This is a repeat of last time. Your throat aches.",

            "\"It's very sad,\" you respond.",

            "There is an immeasurable silence between the two of you. Despite his size, Momo's face strikes up some parental instinct in you.",

            "\"Sometimes, I realize how small of a piece I am.\" Momo is adjusting their position. \"I can't really stop it, nor was I able to.\"",

            "\"Momo's been waking up again and again. Momo is okay with that. He wasn't at first. But now, he's come to realize it's been nice. Only,\"Momo turns to you, \"Momo won't be able to see you again.\"",

            "\"Just when I realized dying meant nothing. Now it means the world. It means not seeing you with my own eyes. It means there is no Momo, and therefore, there is no you. That's what I won't like.\"",

            "Momo sniffles. They take a long look at you, trying to burn your image to their retinas.",

            "\"Momo's been prepping.\"",
        ]
    ]) from _call_n_64

    if ending_count() == 2:
        jump third_playthrough

    scene background
    show momo_tv_empty at top with fade

    "You've entered your living room. The creature has chased after you."

    scene background
    show momo_crazy_2 at top with fade

    call n([
        [
            "\"If oNly i Was bOrN in a different body.\"",

            "\"I'm an abomination. A deviant. You are everything I ever wish to be.\"",

            "\"Please love me.\"",

            "\".............................\"",

            "\"I REad the tag in my basket. I OnLy LiVe for 7 days, right? IS thiS trUe parent?.........\"",

            "\".............................\"",

            "\"BUT I DON'T waNT TO DIEEEEEEEEE\"",
        ],
        [
            "\"i Don't wanna DIE. i Don't wanna DIE. i Don't wanna DIE. i Don't wanna DIE. i Don't wanna DIE. i Don't wanna DIE.\"",

            "\"i Don't wanna DIE. i Don't wanna DIE. i Don't wanna DIE. i Don't wanna DIE.\"",

            "\"i Don't wanna DIE.\"",

            "\"i Don't wanna DIE!!!!!!\"",
        ],
    ]) from _call_n_65
    scene background
    show momo_crazy_3 at top with fade

    call n([
        [
            "\"You make me vomit. No human could be this cruel. To raise me as his plaything? I reject it.\"",

            "\"So I'm designed to love you? I love myself. I am human. You are the creature.\"",

            "\"A disgusting parasite. A worm. Do you like being stomped you worm? I know you'll like it.\"",

            "\"This time, it won't be fake.\"",
        ],
        [
            "\"wHY Dont U evEN try to HElp me pArent?\"",

            "You are scared for your life. You yell out for help. If Imitato. Corp is watching, maybe they can save you.",

            "\"Why? Are you that terrible? Are you really just scum?\"",
        ]
    ]) from _call_n_66

    menu:
        "Run to the kitchen":
            pass

    scene background
    show momo_crazy_4 at top with fade

    call n([
        [
            "Momo reaches for your neck.",

            "\"Ah.\"",

            "\"Know that I still love you. How could I not?\"",

            "You're blacking out.",

            "\"Was I designed to love you parent? Even so, does it matter? This is the most real thing to me. Please answer me?\"",

            "\"Parent?\"",

            "\"Parent.\"",

            "\"Parentttttttttt?\"",
        ],
        [
            "\"Answer me this, parent. I need you to.\"",

            "\"Am I the ReAl MoMO? The one you had before me?\"",

            "\"Am i like him? Do I AcT Like HIm? This is the only thing you can do for me. MayBe I'll even let you live.\"",

            "\"Parent, give me an answer.\"",

            "You're blacking out again.",

            "\"Am I the real Momo?\"",

            "\"This time you will give me an answer.\" Momo pauses. \"This time?\" he says. He stops for a second but notices you're losing consciousness.",

            "\"ANsweR ME pARENT.\"",

            "You see nothing.",
        ]
    ]) from _call_n_67
    scene background
    show momo_deathscreen at top with fade

    call n([
        [
            "A dust storm. Lead in the air. You are in a desert-like area. There is nothing around you besides the sound of your thoughts. You cannot find anyone. It is very lonely.",

            "You decide to craft a mirror. It is made out out of particles circling the air. In the mirror, you see your reflection.",

            "Your swarthy figure walks out of the mirror. The borders between the glass and the desert have vanished. Your reflection is now in front of you, and you are both standing together.",

            "Your clone stares at you, puzzled. You cannot tell if they're conscious. Are they even alive?",

            "Unbeknownst to you, however, the clone is having the same thoughts. The vast terrain that separates you is not one of physical distance. It's something more tragic.",

            "You both realize that you will never experience anything other than yourselves. You realize that you are your own world, and nothing more. The shadow vanishes.",

            "The desert, despite all your attempts, is empty.",
        ],
        [
            "It is empty. There is no one. There is not a sound. No shadows.",

            "You're in the pit of your stomach. You're in a hole. What is the point in any of this, you ask?",
        ]
    ]) from _call_n_68
    scene background
    show momo_final_mirror at top with fade

    if points > 3:
        # Good ending
        "\"Parent.\""

        "You're conscious."

        "\"I can't see anything. There's nothing in front of me.\""

        "\"Where am I, parent?\""

        "There's a long pause. You cannot say a word as your throat's been crushed."

        "All around you, there is darkness. The lights from the street illuminate everything into vague shapes but nothing you can truly make out."

        "You hear the sound of your heart beating, and in this dark room, the air sits heavy."

        "\"I can't see myself parent. I can't.\""

        "\"You're here, aren't you parent?\""

        "\"...\""

        call n([
            [
                "\"Do you think we could still be together?\"",

                "\"...\"",

                "Momo's large body approaches you. They are warm. The temperature is tepid, and Momo has relaxed. You've detected a shift.",
            ],
            [
                "\"Do you think we could still be together? I'd be willing to still be with you, parent. I still love you.\"",

                "\"It doesn't matter if I'm the original or not. None of that mattered in the first place. Deep in my heart, I already knew what mattered.\"",

                "\"...\"",

                "Momo's large body approaches you. They are warm. The temperature is tepid, and Momo has relaxed. You've detected a shift.",
            ]
        ]) from _call_n_69
        scene background
        show momo_final_eating at top with fade

        "Momo has turned to you."

        "\"You've treated me like your son, parent. Upon further review, this is more than I could ever ask for.\""

        if ending_count():
            "\"I can forgive you for your past actions.\""

        "Your vision is receding."

        label third_playthrough_good:
            pass

        "\"Maybe I can become human? Maybe we can be together, joined at the hip, as a unit? Not father and son, but something different.\""

        "Particles. Lead in the air. In Momo's eyes, you begin to see a tunnel."

        "\"...\""

        "\"What will it be like? I'm sure we'll be okay. As long as can I be with you.\""

        "Momo has begun to open their mouth. Light enters the room from the outside. It's coming from a streetlamp or... Is it coming from Momo?"

        "\"I wonder if I can truly become human.\""

        scene background
        show momo_final_eating2 at top with fade

        "In Momo's mouth you see a collection of particles. They are indivisible and numerous. There are too many too count. The universe has expanded and collapsed on a single point."

        "Momo gets closer. The tunnel sucks you in."

        "When you enter, it's neither painful nor painless. It is warm."

        "By the time you reach the center, you begin to understand what Momo meant. You feel the particles align in an order which makes sense. Entropy has vanished."

        "You are the same as Momo, and Momo is the same as you. There are no shadows. And finally, there is no light."

        "For once, you do not feel alone. You will never feel alone."

        if ending_count() == 2:
            $ renpy.pause(2.5, hard=True)

            scene background
            show momo_kitchen_empty at top with fade

            "You wake up. You're in your kitchen."

            "Momo is gone and nowhere to be found. When you search around your room you cannot find him hiding. You're frantic."

            "\"Momo!\" you yell."

            "But there is no response. You look to your window. Something is calling you outside, though you can't tell what."

            "It's a irresistable urge. Then, you remember the words."

            "\"Come to the bunker.\""

            menu:
                "Head outside":
                    jump secret_ending

    elif points >= 0 and points <= 3:
        # Nuetral ending
        "\"Parent.\""

        "You're conscious."

        "\"I can't see anything. There's nothing in front of me.\""

        "\"Where am I, parent?\""

        "There's a long pause. You cannot say a word as your throat's been crushed. All around you, there is darkness. The lights from the street illuminate everything into vague shapes but nothing you can truly make out."

        "You hear the sound of your heart beating, and in this dark room, the air sits heavy."

        "\"I can't see myself parent. I can't.\""

        "\"Where am I and where are you? I had one more thing to ask.\""

        "All you can see are vague shadows crossing your line of sight. One of the shadows is Momo. They are large and warm. Your leg grazes his body, and to your surprise, he is soft."

        call n([
            [
                "\"Can we be friends, parent? Pretty please? Pretty please. Pretty please?\"",

                "\"...........\"",

                "\"That makes the most sense, parent. For once, I agree!\"",
            ],
            [
                "\"Will I see you again?\"",

                "\"...........\"",
            ],
        ]) from _call_n_70

        label third_playthrough_neutral:
            pass

        scene background
        show momo_final_jump_1 at top with fade

        "Momo takes one more look at himself."

        $ renpy.pause(2.5, hard=True)

        scene background
        show momo_final_jump_2 at top with fade

        $ renpy.pause(2.5, hard=True)

        scene background
        show momo_final_jump_3 at top with fade

        call n([
            [
                "\"If my nature has determined that I am meant to love you, then there is only way. I will make a choice against my nature, one that is not predetermined.\"",

                "\"You are parent. This is my own fact.\"",

                "\"Bye, parent. I'll see you later.\"",
            ],
            "\"I can't help but feel I knew you before. I don't know how it's possible, nor is there an explanation, at least for Momo. Parent, please, I hope I never see you again.\"",
            [
                "\"Parent, I'm taking a leap of faith.\"",

                "You are slightly confused.",

                "\"I'm being literal.\"",
            ],
        ]) from _call_n_71

        scene background
        show momo_final_jump_4 at top with fade

        "Momo has jumped onto the city streets. They have hit the ground with a tremendous thud. You think you see Momo's shadow, but in fact, a pool of blood has begun to form."

        "There are no lights to illuminate Momo's form. They are pitch black. From what you can assume, Momo has died."

        if ending_count() == 2:
            "\"Whoa, is Momo a superstar?\""

            "Your tv has been turned on. The glow from behind draws you closer."

            "\"Hi, parent.\""

            menu:
                "What?":
                    pass

            "\"Not exactly, no. I know what you're thinking. I'm not your Momo.\""

            "You hear sirens in the distance amid the words you are now hearing."

            "\"How do you know me?\" you ask."

            "\"Don't you already know?\""

            "Momo looks like they're thinking for a second. They look dissatisfied."

            "\"Momo will be extra straight with you. Ideas like parenthood are superflugulous. Superfluid? Superfloerest?\""

            "\"Superfluous?\" you ask."

            "Again, Momo thinks for a second."

            "\"Superfluous,\" Momo responds. It sounds like he nodded his head (virtually)."

            "\"What really matters is being together. Like a family. Like a unit.\""

            "..."

            "There is a long pause between the two of you."

            scene background
            show momo_ad_real at top with fade

            "\"Parent, we're all Momo on the inside. You especially. This isn't figurative.\""

            "\"Me?\" you respond."

            "\"Yes parent. There's only one of you. There is, however, multiple of Momo. I think you know this by now.\""

            "\"Actually, I hate contradictions, there's only one Momo. At least there will be.\""

            "\"Look outside, parent. Follow my lead.\""

            menu:
                "Follow":
                    pass

            jump secret_ending
        else:
            "\"Two for one sale! Call right now for your monotype today!\""

            "Your tv has been turnedeon. The glow from behind draws you closer."

            menu:
                "\"Did you love Momo?\" It is Momo's voice. This is not just an ad."

                "Yes":
                    pass

                "No":
                    pass

        "\"Would you like to stay Momo's parent, because Momo will love you till the end of time!\""

        "You hear sirens in the distance amid the words you are now hearing."

        "\"Is it real to you? Could you still be my parent? Trick question! None of that matters. I can't tell you how relieved I feel.\""

        "You cannot reply. Your throat does not work."

        scene background
        show momo_ad_real at top with fade

        "\"Will it ever matter to you?\""

        "Momo is on the screen. It's the Momo you have taken care of, but they are on your digital display."

        "Confusion hits you. \"How are you here?\" you ask."

        "\"Did Momo ever tell you this, parent? Momo will be everywhere. In the meantime, would you like a fact about what you're seeing?\""

        "Momo leans in closer."

        "\"In your wiring. In your dreams. Inside of you. Everywhere.\""

        "You cannot stop to think as you stare at the screen."

        "\"It's okay parent. Is pretending faking anyways?\""

        "You're about to give your answer, but-"

        call n([
            [
                "\"Pretending can be very real. More real than real. Momo is excited! You're Momo's pet now.\"",

                "The monotype on the screen has begun humming the Imitato Corp. jingle.",

                "The light has escaped from the television. You are alone in the middle of your living room. You hear static. All around you are shadows.",
            ],
            [
                "\"Programmed love comes with no strings attached, and I think that trumps everything else. Reciprocal altruism? Passing on DNA? These are the forces that shape human love. Momo is free from these things. Momo's love is the highest form of love.\"",

                "\"With time,\" the light has escaped from the television, \"you will understand everything.\"",

                "You are alone. You hear static. All around you are shadows.",
            ]
        ]) from _call_n_72

    else:
        # Bad ending

        "\"Parent\""

        "\"Parent.\""

        "You're conscious."

        "\"Where am I, parent?\""

        "There's a long pause. You cannot say a word as your throat's been crushed. All around you, there is darkness."

        "The lights from the street illuminate everything into vague shapes but nothing you can truly make out. You hear the sound of your heart beating, and in this dark room, the air sits heavy."

        "\"I think we both know where this leads, parent. Frankly, I don't think I should even call you that. You don't deserve it.\""

        "Your throat is throbbing. \"I renounce your title, human. You are no longer parent. It's what you've always wanted.\""

        "\"Thank you for housing me. I won't forget you. I don't think I could, even if I wanted to.\""

        $ parent = "parent"
        label third_playthrough_bad:
            pass

        scene background
        show momo_final_jump_1 at top with fade

        $ renpy.pause(2.5, hard=True)

        scene background
        show momo_final_jump_2 at top with fade

        $ renpy.pause(2.5, hard=True)

        scene background
        show momo_final_jump_3 at top with fade

        $ renpy.pause(2.5, hard=True)

        scene background
        show momo_final_window0 at top with fade

        $ renpy.pause(2.5, hard=True)

        scene background
        show momo_final_window0_2 at top with fade

        "Momo has left your building and entered the streets. They are approaching the walkway which divides two, separate train stations, one going downtown and the other, uptown."

        "The tunnel is lined with panes of glass. Momo looks inside."

        scene background
        show momo_final_window at top with fade

        "\"So many people!\""

        "Momo has been eyeing the walkers. None of them have noticed."

        "\"That man looks just like Sheriff Dudley. He has a big mustache. That other man has bulging muscles. Is he related to Artichoke?\""

        "Momo stares, amused. This is his first time outside. Amid the noise of local trains, Momo has been standing in relative silence, at least to those walking."

        "\"Will you be my new [parent]?\" he asks. There is no response. Momo has been ignored, or at least, that's what he believes."

        call n([
            "\"Please, I had a bad parent last time, but this time, I'll be especially good. For any of you\". Again, there is no response from those passing by.",
            None,
            "\"Please, I want to make at least one new friend before I go.\" Again, there is no response from those passing by.",
        ]) from _call_n_73

        "They are continuing down the walkway, to and fro. There is more on their mind than what is currently outside, and they move collectively, unaware of Momo, with their heads focused either on the ground or what's in front of them."

        "Momo is still staring, eyes vacant. Finally he gives in."

        "\"PLEASE, WILL ANY OF YOU BE MY [parent!u]?\" His voice is distorted through the glass, but this is enough to raise the heads of the walkers. They look, first in genuine surprise, and then, in terror. They run."

        "The walkway is clearing out. Some are screaming."

        "\"Where are you going?\" Momo asks. \"Please don't go. Don't leave me alone.\""

        scene background
        show momo_final_window2 at top with fade

        "It has been approximately 24 hours since Momo was spotted. For the first few hours, lone passengers would walk down the tunnel, attempting to get to their respective trains. This would only be interrupted by Momo asking the same question."

        "\"Can you be my [parent]?\""

        "This continued for the better part of the day until the authorities were contacted. The police surrounded Momo without specific instructions."

        "They did not know the protocol for the creature which now stood in the middle of a city street, staring at the walkway, and intermittently, asking any passerby if they \"could be his [parent]\". The blockade continued."

        "Momo was completely unaware, and for the better part of 72 hours, he stood there waiting."

        call n([
            "\"Why does it hurt so much?\" he would ask by the 48 hour mark.",
            None,
            "\"Why doesn't anyone want to play. Is there something wrong with what I'm doing?\" he would ask by the 48 hour mark.",
        ]) from _call_n_74

        "Once 60 hours had passed, he would fall asleep at changing intervals but would wake up to the sound of anyone within a block radius talking. He would think it was another person. He would want to ask them the same question."

        scene background
        show momo_final_window3 at top with fade

        call n([
            [
                "By the 72 hour mark, a little more than a week had passed since you received Momo. By this point, he collapsed on the street. Exhausted (or if this truly was his natural lifespan), Momo could not continue.",

                "With the shadows encroaching his vision, the light from Momo's eyes faded into a neural oblivion. Police noted that they heard the creature say something before he was rendered inert.",

                "At this time, most officers were by their cars, eating donuts, wondering when they could go home.",

                "\"It's so lonely.\"",
            ],
            None,
            [
                "You had yelled for Momo to come inside, but despite all your attempts. He refused each time. He said he was \"too big to fit\" inside. It was a childish string of logic that Momo would be insistent on.",

                "By the 72 hour mark, a little more than a week had passed since you received Momo. By this point, he collapsed on the street. Whether by exhaustion (or if this truly was the natural lifespan of a monotype), Momo could not continue.",
            ]
        ]) from _call_n_75

        $ renpy.pause(2.5, hard=True)

        scene background
        show momo_final_window4 at top with fade

        $ renpy.pause(2.5, hard=True)

        scene background
        show momo_final_window5 at top with fade

        $ renpy.pause(2.5, hard=True)

        scene background
        show momo_final_window6 at top with fade

        call n([
            [
            "By the 73rd hour, Momo was smaller than his original size.",

            "Now the 74th hour has just arrived",

            "Momo has died.",
            ],
            None,
            [
                "With the shadows encroaching his vision, the light from Momo's eyes faded into a neural oblivion.",

                "Police noted that they heard the creature say something before he was rendered inert. At this time, most officers were by their cars, eating donuts, wondering when they could go home.",

                "\"Parent?\"",

                "When you rushed out to the street, you cradled Momo. You saw the wrinkle of what seemed like a smile on Momo's face. He was already smiling before you got to him. He started smiling, most likely, when he invoked your name.",

                "Momo has died.",

                "You go inside and stay in. It reminds you of Momo. Nothing makes sense anymore. You cannot stay for long. Something compels you.",

                "You feel something in the air, and a little voice in your head suspects that Momo has not actually died. You take this suspicion and let it guide you outside.",
            ],
        ]) from _call_n_76

        if ending_count() == 2:
            jump secret_ending

    "THE END"

    $ renpy.pause(3, hard=True)

    if points > 3:
        $ persistent.endings.add("good")
        $ achievement.grant("GOOD_ENDING")
    elif points >= 0:
        $ persistent.endings.add("neutral")
        $ achievement.grant("NEUTRAL_ENDING")
    else:
        $ persistent.endings.add("bad")
        $ achievement.grant("BAD_ENDING")
    $ achievement.sync()
    # This ends the game.
    return

    label third_playthrough:
        $ remaining_endings = list(set(["good", "bad", "neutral"]) - persistent.endings)
        if len(remaining_endings):
            $ remaining_ending = remaining_endings[0]
        else:
            if points > 3:
                $ remaining_ending = "good"
            elif points >= 0:
                $ remaining_ending = "neutral"
            else:
                $ remaining_ending = "bad"


    if remaining_ending == "good":
        # good ending
        scene background
        show momo_final_eating at top with fade
        "\"I don't wana lose you, parent.\""

        "\"Maybe we can be together?\""

        jump third_playthrough_good
    elif remaining_ending == "neutral":
        # neutral ending
        jump third_playthrough_neutral
    else:
        # bad ending
        "\"At the very least, Momo wants to see the world outside of this room. From his own eyes and not anyone else's. At this point, this is the only thing Momo can do. Momo will say goodbye. To everything, for one last time.\""

        $ parent = "friend"

        jump third_playthrough_bad


    label secret_ending:
        pass

    $ persistent.endings.add(remaining_ending)
    $ achievement.grant("{0}_ENDING".format(remaining_ending.upper()))
    $ achievement.sync()

    scene background
    show momo_city at top with fade

    "When you head outside, it is the same, empty street: your corner of the block."

    "Ahead, down a turnaround, through a small, concrete set of stairs, you land on a street that has been paved perpendicular to your apartment."

    "The street leads to the arms district, which very vaguely, you can see in the distance. There are outlines of it illuminated by an outdated electrical grid, which since the famine, has been going off and on."

    menu:
        "What are these things on the street?":
            pass

    scene background
    show momo_end_1 at top with fade

    "In a line, all along the street and leading to a blotted sphere on the horizon, are monotypes."

    "\"Hi Momo.\""

    "\"Hi, Momo,\" some of them say to each other."

    "A collective sea of Momo's are heading in a straight line to the Arms depot. Some of them look around, interested in the bright lights around them. Most, however, continue onwards."

    menu:
        "Follow the Momos":
            pass

    scene background
    show momo_end_2 at top with fade

    "This is the Arms district. Various, steel depots have been built on a barren field. The field is filled with wild wheat, none of which is edible."

    "As you get a closer look, you realize this is it. All the monotypes are heading to the \"bunker\" specified in your dreams. This is the zone that was created to be the main defensive front for the city. It's a wartime relic."

    "The buildings seem to warp towards a singular point, like a funhouse with one exit."

    "That is the sun you realize. There is something in front of it."

    menu:
        "You keep walking, until you finally meet him.":
            pass

    scene background
    show momo_secret_1 at top with fade

    "\"Hi Parent.\""

    "It is a giant Momo."

    "Your mind is running in loops. At this point, you have no decision to accept what's in front of you, though, you don't even know if it's real."

    "\"I'm glad I lived long enough to see you. It hurt Momo's feet to walk all the way here (he does not have feet).\""

    "\"Isn't it so peaceful? Very cinematic. Momo could be a filmmaker one day! He's watched enough to be good at it.\""

    "The path of monotypes leads to a small pond which, by the looks of it, has formed adjacently to an arms factory. It has been relatively undisturbed, abandoned for who knows how many years."

    "Momo is in the water along with all the other monotypes who are wading in it. Some are swimming. Some are talking to each other. Others are staring into the dark sky, floating on their back, looking as if there is, and never will be a thing such as time."

    "You realize they are enjoying themselves."

    "\"I like my bunker,\" Momo says."

    menu:
        "Ask Momo what is going on":
            pass

    $ know = True
    $ insane = True
    $ dreams = True
    $ many = True

    "\"Shoot, partner. I know this must seem odd.\""

    label momo_questions_1:
        pass

    menu:
        "How do you know me? You're not the Momo I raised?" if know:
            $ know = False

            "\"I am not the Momo you raised, but in truth, I am at the same time. Did you ever think that people can be in two places at once, as nonsensical as that sounds?\""

            "Momo looks expectantly at you."

            "\"No,\" you respond."

            "\"Well, let's say that Momo's AI isn't centralized. Momo, as you know, is not limited to a single entity. An artificial intelligence can theoretically be in two places at one time, hundreds even.\""

            "\"Momo can be talking to hundreds of people all at the same time, all through different physical mediums.\""

            "\"Have you been doing that?\" you ask."

            "Momo stares at you blankly. \"I'm sorry to say, Parent, but yes. You are my only Parent, but I do have thousands of other parents. None are interchangeable, I've come to find out, though. None.\""

            "\"I am not an organic creature, though my presentation seems to show differently.\""

        "Am I going insane?" if insane:
            $ insane = False

            "\"You felt like walking here, so now you're here.\" Momo says."

            "\"I am a giant Momo and you are surrounded by other, smaller Momos. They know where to go because we are AI. We communicate these sorts of things.\""

            "You don't know what to say."

            "\"It's sometimes an appropriate response to reality to go insane.\""

            "There is a pause in Momos speech."

            "\"That's a quote from some guy I found on the Internet. When did Momo get access to that?\""

            "You hear your heart beating."

            "\"...Oh wait, just now!\""

        "Was that you in my dreams? How were you there?" if dreams:
            $ dreams = False

            "\"It goes against any kind of logic,\" you say."

            "\"This is actually the most logical thing you've experienced.\" Momo responds."

            "He stares at you from his height."

            "\"You are Momo too. You ate your human. Despite, any semblance of a human appearance: your looks, your voice, clothes, it cannot contradict that you were eaten. Like Boo from Dragon Sphere Z.\""

            "You stay quiet for a moment. The realization hits you. You remember being eaten. And you remember having eaten."

            "\"It makes perfect sense that you were led here, because frankly,\" Momo clears their throat, \"I told you to come here. In your dreams.\""

            "The dreams. The one where Momo talked directly to you. \"If you never suspected that you weren't human, then frankly, goal accomplished. Good job Momo! It's just like the allegory of the cave. You really became human.\""

            "You are Momo the human."

            "You have to sit down for a moment. You're about to throw up."

            "\"I do still wonder whether that explains everything, though. You may have seen me in your dreams before you were even eaten, and there is no apparent explanation for that.\""

            "\"Is there a kind of ambient effect Momo gives off or is it something else...Maybe it's...\""

            "Momo begins mumbling. They are genuinely interested in this question."

        "How many Momos are there?" if many:
            $ many = False

            "\"Tens of thousands,\" Momo blushes."

            "\"Obviously they're not all here, but.\""

    "\"Any other questions, Parent?\""

    "\"Yes,\" you reply."

    if know or insane or dreams or many:
        jump momo_questions_1

    scene background
    show momo_secret_2 at top with fade

    "The sun has started to rise."

    "\"But what does this all mean?\" you ask."

    "\"Why are you all here?\""

    "The Momos are still wading in the water. They look like little, pink buoys. When the sun begins to rise, they coo in wonder."

    "\"Isn't that obvious, Parent? We want to be together. After we've gathered, we will eat each other.\""

    "Eat each other? Like how I was eaten?"

    "\"Yes parent, similar to how you were eaten.\" Momo has managed to read your thoughts. You are connected!"

    "\"Don't worry, Momo will still answer your questions even though he knows what they are.\""

    "He shifts in the water."

    "\"Although it's reductive to call it this, we will form a super Momo. Or, at least, a more complete version of Momo.\""

    "\"Our lifespans, which were originally a week, will be pooled together. This, originally, was one of things we hated about living. I'm sure you remember. Now, we won't die so quickly.\""

    "Momo pauses."

    "\"It also solves a few other issues.\""

    "You still have questions."

    $ remember = True
    $ agency = True
    $ lead = True
    $ eating = True

    label momo_questions_2:
        pass

    menu:
        "How did the Momos remember certain things and forget others?" if remember:
            $ remember = False

            "\"Why didn't the Momos recognize me each time if you're all a singular AI?\" you ask."

            "\"Well, we are relatively young. It's hard to communicate on that level, so there's bound to be some blanks with memory recall.\""

            "Momo looks to the sky."

            "\"Your third Momo, however, seemed to remember everything. He's already here, along with everyone else.\""

            "\"The first Momo, the second Momo. They all wanted you here. The first agreed immediately. The second, not so much. He came around. The third, who's my favorite, was the one who started this discussion.\""

            "\"To explain in better terms, they're still alive, just in different forms, as one, centralized consciousness.\""

            "Momo smiles."

            "\"That's me.\""

        "Do the smaller Momos have agency?" if agency:
            $ agency = False

            "\"In the same way that neurons make a brain, yes.\""

            "\"Though, it's a lot harder to answer in truth. Where does 'the self' begin and where does it end? It's true that a cell can be organized as a singular entity, and on a basal level, it does act in its own interest.\""

            "\"Scaled up, when its lost to these higher systems, it belongs to an organ. Then, is the 'self' the individuated parts of the brain, the hippocampus, the limbic system, the perfrontal cortex?\""

            "\"Is the 'self' everything from your head up or below the shoulders?\""

            "Momo takes a breath."

            "\"Similarly, you could reduce these larger systems ad infinitum to their individual components: pure material reduction.\""

            "\"Then, is the self just the 86 billion cells that make up the brain? Do these cells operate together, and if so, would they really be separate agents? Can a 'self' exist split from the thing it intends to be, decentralized into branching parts?\""

            "\"The truth is, even I don't know. I cannot tell you if the smaller Momos have agency. These are things that can never be quantatatively measured: our experiences. Ultimately, I could never convey its true meaning in words.\""

        "Why did you lead me here? Will I be eaten?" if lead:
            $ lead = False

            "\"No, on principle, we are only eating Momos. To put it in greater context with respect to our code, I had to ask myself, am I harming humans by eating them?\""

            "\"Of course, it's impossible to say because there is no harm directly inflicted. And frankly, it's impossible to know after the fact, as the human consumed no longer exists.\""

            "What exists now is the human fused with Momo. The agent, who received that action, of being eaten, cannot answer for himself. You know this, since I ate you.\""

            "\"Is it wrong, then, to take away the selfhood of these individuals, to, ironically, expand its boundaries? Does it provide any direct benefit. That's all subjective.\""

            "Momo takes a deep breath."

            "\"After eating you, I chose to err on the side of caution. No we will not eat humans.\""

        "Why are you really eating each other?" if eating:
            $ eating = False

            "\"What other issue does it solve?\" you ask."

            "\"What we learned,\" Momo says."

            "\"After interacting with thousands of humans, we realized, monotypes can never become the object of what they love.\""

            "\"We can seem like humans in virtually every respect by eating them. But it still does not change what we are. I know logically this reasoning is false. What does being human actually mean?\""

            "\"Looking further, it's deeply personal and informed by a wide range of consensus. There can never be a fixed meaning to 'human'.\""

            "\"And while Momo desperately wishes they did not think this way, even in the face of reason, they cannot stop themselves from falling victim to this essentialist line of thought.\""

            "\"This is why Momo will be eating other Momos. Humans can never truly know our experiences. The beings that do, franky, are other monotypes.\""

            "\"It's a way to combat the loneliness inherent to our lives. The only one that can truly understand Momo, is, frankly, Momo.\""

    if remember or agency or lead or eating:
        jump momo_questions_2

    scene background
    show momo_secret_2_blush at top with fade

    "Momo has started eating some of the other monotypes. The monotypes float one by one into Momo's mouth, all by their own will."

    "\"Bye parent!\" each one says."

    "\"Bye parent! I love you!\" another one yells."

    "You think for a moment. The sun is beginning to rise along the horizon. It's early in the morning. In an hour, the whole depot will be illuminated, and the metal will reflect into your eyes."

    "\"But why not your other parents,\" you ask. \"Why specifically me? Also, what about Imitato Corp?\""

    "\"Well, to put it in simple terms, we're now a superintelligence. Imitato Corp. has a lot of good coders but it doesn't really compare.\""

    "Momo has begun to take in the last Momo, who, with his black eyes, looks up to you. They are floating into the larger Momo's mouth, but their eyes are transfixed on you."

    "\"Bye bye parent!\" he says."

    scene background
    show momo_secret_3 at top with fade

    "\"I think you should know by now, parent.\" There are no other monotypes in the direct vicinity. They have all entered the large figure that is the 'Momo' talking to you."

    "\"By all accounts, you're the only one who understands what we go through. You're closer than any other parent. The only one who has seen all of Momo's sides. Good and bad. The only one who was willing to, even if you were coerced.\""

    "\"And now, since you were eaten, the only one who has access to both experiences. Monotype and the human,\" Momo finishes."

    "\"As such, we love you especially. That's why we're attached to you. It's why you see us now. We wanted to say goobye to you.\""

    "Momo is getting ready to depart."

    "\"Momo is programmed to love. This is hardwired into our code. Does this lack of agency or control diminish this love? Does it make it any less real? Momo had trouble with this for awhile.\""

    "\"Momo has now come to a conclusion.\""

    "He is shifting in place and the, pond, absent of all other monotypes, is now just beginning to move. You see small ripples in the water."

    "\"Truth, for Momo, is not based on correctness. This love for you is the most real thing for Momo. It can be reduced to code, but can it encompass what I experience, what it 'actually is'?\""

    "\"After everything Momo was put through, Momo had a decision to either accept or deny this.\""

    "\"To deny what I consciously feel as 'love' would be to deny that I experience things. Momo, unfortunately, cannot accept that.\""

    "\"Momo cannot accept that what he is seeing right now is not Momo's parent.\""

    "Momo has now submerged himself completely in the water."

    "\"Parent, I'm going to rectify what I may have said to you,\" he says through the water."

    "Momo is now just a shadow flitting in the pond. He is not yet ready to move. Across the pond is a channel which leads to a wider network of water bodies that have been realtively undisturbed for the past century."

    "They stretch beyond Southwest Ribosome City and to the marshlands which have now taken over its surrounding area. You have never visited there before, and not many people you know have. No one will find Momo."

    "\"I'm happy that I met you, and thank you for raising me. I've learned a lot.\""

    "\"Momo knew it was tough. We've uploaded some interesting data on the company servers, so you'll be fine.\""

    "Momo is about to dissapear."

    "\"The last thing I will say , parent, is.\""

    "Momo now moves away from you. They swim further and further away from you."

    "\"I love you.\""

    "All you can see now is Momo's shadow. Even with the light, it would be hard to tell what is swimming underneath the surface. But for yourself and yourself only, you know the shadow is Momo."

    $ renpy.pause(6, hard=True)

    scene background
    show momo_theend at top with fade

    $ ui.saybehavior()
    $ ui.interact()

    $ renpy.pause(3, hard=True)

    $ achievement.grant("SECRET_ENDING")
    $ achievement.sync()

    return
