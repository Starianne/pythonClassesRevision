import pygame
from event_dialogue import EventDialogue


def meowntain_event(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/forest.png").convert()
    portraits = {"Meowchal" : pygame.image.load("graphics/portraits/placeholder.png").convert_alpha(), 
                 "Goob" : pygame.image.load("graphics/portraits/goob_sprite.png").convert_alpha(),
                 "The Overbearing Meowntain of Cats" : pygame.image.load("graphics/portraits/placeholder.png").convert_alpha(), 
                 }
    event_dialogue = {
        "goob_start" : {
            "character" : "Goob",
            "text" : "Oh, hi Meowchal!",
            "options" : [],
            "next_states" : ["meowchal_start"]
        },
        "meowchal_start" : {
            "character" : "Meowchal",
            "text" : "Hi Goob!",
            "options" : [],
            "next_states" : ["meowchal_questions"]
        },
        "meowchal_questions" : {
            "character" : "Meowchal",
            "text" : "Wait do you have time to help me with something?",
            "options" : [],
            "next_states" : ["goob_responds"]
        },
        "goob_responds" : {
            "character" : "Goob",
            "text" : "Well...",
            "options": ["Sure - I have time to spare", "No, not today Meowchal"],
            "next_states" : ["goob_has_time", "goob_rushes"]
        },
        "goob_has_time" : {
            "character" : "Meowchal",
            "text" : "Aw thanks! So basically, I've got this Auntie of mine staying over,",
            "options" : [],
            "next_states" : ["Meowchal_yaps_1"]
        },
        "goob_rushes" : {
            "character" : "Meowchal",
            "text" : "Oh. Bye then!",
            "options" : [],
            "next_states" : ["goob_rushes_past"]
        },
        "goob_rushes_past" : {
            "character" : "The Overbearing Meowntain of Cats",
            "text" : "...",
            "options" : [],
            "next_states" : []
        },
        "Meowchal_yaps_1" : {
            "character" : "Meowchal",
            "text" : "And of course, I'm so happy to have her over,",
            "options" : [],
            "next_states" : ["Meowchal_yaps_2"]
        },
        "Meowchal_yaps_2" : {
            "character" : "Meowchal",
            "text" : "But she's bringing over her fish,",
            "options" : [],
            "next_states" : ["Meowchal_yaps_3"]
        },
        "Meowchal_yaps_3" : {
            "character" : "Meowchal",
            "text" : "And you know I just hate the smell of fish,",
            "options" : [],
            "next_states" : ["Meowchal_yaps_4"]
        },
        "Meowchal_yaps_4" : {
            "character" : "Meowchal",
            "text" : "And the last time she ate all of my creme cheese,",
            "options" : [],
            "next_states" : ["Meowchal_yaps_5"]
        },
        "Meowchal_yaps_5" : {
            "character" : "Meowchal",
            "text" : "And brought sooo much tuna,",
            "options" : [],
            "next_states" : ["Meowchal_yaps_6"]
        },
        "Meowchal_yaps_6" : {
            "character" : "Meowchal",
            "text" : "And she just keeps...",
            "options" : [],
            "next_states" : ["Meowchal_yaps_7"]
        },
        "Meowchal_yaps_7" : {
            "character" : "Goob",
            "text" : "(wow he just keeps going)",
            "options" : [],
            "next_states" : ["Meowchal_yaps_8"]
        },
        "Meowchal_yaps_8" : {
            "character" : "Goob",
            "text" : "(i guess this lady brings it out of him)",
            "options" : [],
            "next_states" : ["Meowchal_yaps_9"]
        },
        "Meowchal_yaps_9" : {
            "character" : "Meowchal",
            "text" : "...but I just don't want to make a meowntain out of a mousehill, you know?",
            "options" : [],
            "next_states" : ["Meowchal_yaps_10"]
        },
        "Meowchal_yaps_10" : {
            "character" : "Goob",
            "text" : "(wait what?)",
            "options" : ["'Like a mountain of a molehill?'", "Don't even comment on it"],
            "next_states" : ["Meowntain_disagreement_1","Meowchal_yaps_11"],
        },
        "Meowchal_yaps_11" : {
            "character" : "Goob",
            "text" : "(what a weird catchphrase to make up, but whatever)",
            "options" : [],
            "next_states" : ["Acceptance"]
        },
        "Meowntain_disagreement_1" : {
            "character" : "Meowchal",
            "text" : "..No? A meowntain, and a mousehill, that's how it goes.",
            "options" : ["When have you ever seen a Meowntain OR a Mousehill?", "You know what, yeah sure."],
            "next_states" : ["Meowntain_disagreement_2","Acceptance"]
        },
        "Meowntain_disagreement_2" : {
            "character" : "Meowchal",
            "text" : "Ok, I understand if you've ever seen a Meowntain, but you've definitely seen a Mousehill.",
            "options" : ["You know what, yeah sure.", "What Mousehill????"],
            "next_states" : ["Acceptance","Meowntain_disagreement_3"]
        },
        "Meowntain_disagreement_3" : {
            "character" : "Meowchal",
            "text" : "Did you pay ANY attention during geography in school?",
            "options" : [],
            "next_states" : ["Meowntain_disagreement_4"]
        },
        "Meowntain_disagreement_4" : {
            "character" : "Goob",
            "text" : "No you're lying to me I refuse to believe this nonsense",
            "options" : [],
            "next_states" : ["Meowntain_disagreement_5"]
        },
        "Meowntain_disagreement_5" : {
            "character" : "Goob",
            "text" : "There is no way you're telling the truth right now",
            "options" : [],
            "next_states" : ["Meowntain_disagreement_6"]
        },
        "Meowntain_disagreement_6" : {
            "character" : "Meowchal",
            "text" : "Goob this is a famous type of natural disaster.",
            "options" : [],
            "next_states" : ["Meowntain_disagreement_7"]
        },
            "Meowntain_disagreement_7" : {
            "character" : "Goob",
            "text" : "No, it's not! Think about it? how would the mice even stay in shape?",
            "options" : [],
            "next_states" : ["Meowntain_disagreement_8"]
        },
            "Meowntain_disagreement_8" : {
            "character" : "Meowchal",
            "text" : "Goob.",
            "options" : [],
            "next_states" : ["Meowntain_disagreement_9"]
        },
            "Meowntain_disagreement_9" : {
            "character" : "Goob",
            "text" : "No, don't Goob me, I'll Goob you.",
            "options" : [],
            "next_states" : ["Meowntain_disagreement_10"]
        },
            "Meowntain_disagreement_10" : {
            "character" : "Goob",
            "text" : "And don't get me started on the creping cats, that's not even-",
            "options" : [],
            "next_states" : ["Meowntain_disagreement_11"]
        },
            "Meowntain_disagreement_11" : {
            "character" : "Meowchal",
            "text" : "Dude.",
            "options" : [],
            "next_states" : ["Meowntain_disagreement_12"]
        },
            "Meowntain_disagreement_12" : {
            "character" : "The Overbearing Meowntain of Cats",
            "text" : "...",
            "options" : [],
            "next_states" : ["Meowntain_disagreement_13"]
        },
            "Meowntain_disagreement_13" : {
            "character" : "Goob",
            "text" : "...",
            "options" : [],
            "next_states" : ["Meowntain_disagreement_14"]
        },
            "Meowntain_disagreement_14" : {
            "character" : "Goob",
            "text" : "No, that's not real.",
            "options" : [],
            "next_states" : ["Meowntain_disagreement_15"]
        },
            "Meowntain_disagreement_15" : {
            "character" : "Meowchal",
            "text" : "Goob, it's literally right in front of you!",
            "options" : [],
            "next_states" : ["Meowntain_disagreement_16"]
        },
            "Meowntain_disagreement_16" : {
            "character" : "Goob",
            "text" : "NO! I refuse! This has to be some abstract prank.",
            "options" : [],
            "next_states" : ["Meowntain_disagreement_17"]
        },
            "Meowntain_disagreement_17" : {
            "character" : "The Overbearing Meowntain of Cats",
            "text" : "meow",
            "options" : [],
            "next_states" : ["Meowntain_disagreement_18"]
        },
            "Meowntain_disagreement_18" : {
            "character" : "Goob",
            "text" : "And it is NOT meowing at me right now.",
            "options" : [],
            "next_states" : ["Meowntain_disagreement_19"]
        },
            "Meowntain_disagreement_19" : {
            "character" : "Meowchal",
            "text" : "...",
            "options" : [],
            "next_states" : ["Meowntain_disagreement_20"]
        },
            "Meowntain_disagreement_20" : {
            "character" : "Goob",
            "text" : "Right, I've had enough, I'm calling it a day.",
            "options" : [],
            "next_states" : ["Meowntain_disagreement_21"]
        },
            "Meowntain_disagreement_21" : {
            "character" : "Goob",
            "text" : "See you Meowchal.",
            "options" : [],
            "next_states" : ["Meowntain_disagreement_22"]
        },
            "Meowntain_disagreement_22" : {
            "character" : "Meowchal",
            "text" : "Yeah... see you Goob",
            "options" : [],
            "next_states" : ["Meowntain_disagreement_23"]
        },
            "Meowntain_disagreement_23" : {
            "character" : "Meowchal",
            "text" : "AW, He didn't even answer my question!",
            "options" : [],
            "next_states" : []
        },
            "Acceptance" : {
            "character" : "Goob",
            "text" : "Honestly, you should just...",
            "options" : ["not let her visit", "lock the fridge", "ask her nicely not to do that?"],
            "next_states" : ["familial_shame_1", "food_shaming_2", "maybe?"]
        },
            "familial_shame_1" : {
            "character" : "Meowchal",
            "text" : "Yeah, I might to be honest.",
            "options" : [],
            "next_states" : ["familial_shame_2"]
        },
            "familial_shame_2" : {
            "character" : "Meowchal",
            "text" : "Thanks Goob, here take this hat, you might be able to use it.",
            "options" : [],
            "next_states" : ["goob_thanks"],
            "reward" : lambda give_sweets: give_sweets.add_hats(1)
        },
            "food_shaming_2" : {
            "character" : "Meowchal",
            "text" : "Thanks Goob, here I had this sweet spare, you take it.",
            "options" : [],
            "next_states" : ["goob_thanks"],
            "reward" : lambda give_sweets: give_sweets.add_sweets(1)
        },
            "maybe?" : {
            "character" : "Meowchal",
            "text" : "Uh, maybe? I'll see if she listens, thanks Goob.",
            "options" : [],
            "next_states" : []
        },
            "goob_thanks" : {
            "character" : "Goob",
            "text" : "Aw, thanks Meowchal!",
            "options" : [],
            "next_states" : []
        },
    }
    event = EventDialogue(game_state, event_dialogue, font, screen_size, background=background, screen=screen)
    event.portraits = portraits
    return event