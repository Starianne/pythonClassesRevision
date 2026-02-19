import pygame
from event_dialogue import EventDialogue


def dont_mention_it_event(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/forest.png").convert()
    portraits = {"Joel" : pygame.image.load("graphics/portraits/placeholder.png").convert_alpha(), 
                 "Jay": pygame.image.load("graphics/portraits/placeholder.png").convert_alpha(),
                 "Goob" : pygame.image.load("graphics/portraits/goob_sprite.png").convert_alpha(),
                 }
    event_dialogue = {
        "Joel_start" : {
            "character" : 'Joel',
            "text" : "So Goob, what do you think?",
            "options" : [],
            "next_states" : ["Goob_start"],
        },
        "Goob_start" : {
            "character" : 'Goob',
            "text" : "Uh, well,",
            "options" : ["tell the truth", "tell a lie"],
            "next_states" : ["tell_truth", "tell_lie"],
        },
        "tell_truth" : {
            "character" : 'Goob',
            "text" : "To be honest, I don't think you put enough Lemon juice",
            "options" : [],
            "next_states" : ["tell_truth_2"],
            "reward" : lambda tt: tt.set_flag("honest"),
        },
        "tell_truth_2" : {
            "character" : 'Joel',
            "text" : "Ah, I thought so.",
            "options" : [],
            "next_states" : ["tell_truth_3"],
        },
        "tell_truth_3" : {
            "character" : 'Joel',
            "text" : "I just keep putting in extra sugar to stop myself from eating the spoon instead",
            "options" : [],
            "next_states" : ["noticed"],
        },
        "noticed" : {
            "character" : 'Goob',
            "text" : "(Wait is that what I think it is?)",
            "options" : [],
            "next_states" : ["noticed_2"],
        },
        "noticed_2" : {
            "character" : 'Jay',
            "text" : "...",
            "options" : ["mention it", "dont mention it"],
            "next_states" : ["mention", "dont_mention"],
        },
        "mention" : {
            "character" : 'Goob',
            "text" : "Sooo is he a Room mate?",
            "options" : [],
            "next_states" : ["room_mate"],
        },
        "room_mate" : {
            "character" : 'Joel',
            "text" : "Ohh! Yes, that's Jay",
            "options" : [],
            "next_states" : ["room_mate_2"],
        },
        "room_mate_2" : {
            "character" : 'Joel',
            "text" : "He moved in last week, didn't I tell you?",
            "options" : [],
            "next_states" : ["room_mate_3"],
        },
        "room_mate_3" : {
            "character" : 'Jay',
            "text" : "Hey.",
            "options" : [],
            "next_states" : ["room_mate_4"],
        },
        "room_mate_4" : {
            "character" : 'Goob',
            "text" : "Hi!",
            "options" : [],
            "next_states" : ["room_mate_5"],
        },
        "room_mate_5" : {
            "character" : 'Jay',
            "text" : "Bye.",
            "options" : [],
            "next_states" : ["Joel_thanks"],
        },
        "Joel_thanks" : {
            "character" : 'Joel',
            "text" : "Anyways. Thanks for trying the Lemon drops, I'll give you some when you leave!",
            "options" : [],
            "next_states" : ["Goob_response"],
            "reward" : lambda give_sweets: give_sweets.add_sweets(3),
        },
        "Goob_response" : {
            "character" : 'Goob',
            "text" : "No problem, wanna play Pario Kart?",
            "options" : [],
            "next_states" : ["Joel_response"],
        },
        "Joel_response" : {
            "character" : 'Joel',
            "text" : "When do we not?",
            "options" : [],
            "next_states" : [],
        },
        "tell_lie" : {
            "character" : 'Goob',
            "text" : "Yeah, they're perfect!",
            "options" : [],
            "next_states" : ["tell_lie_2"],
            "reward" : lambda tl: tl.set_flag("liar"),
        },
        "tell_lie_2" : {
            "character" : 'Joel',
            "text" : "Oh I'm so glad! I thought they might be too sweet,",
            "options" : [],
            "next_states" : ["tell_truth_3"],
        },
        "dont_mention" : {
            "character" : 'Goob',
            "text" : "(Did he.. come out of the fridge?)",
            "options" : ["mention it", "dont mention it"],
            "next_states" : ["mention", "dont_mention_2"],
        },
        "dont_mention_2" : {
            "character" : 'Goob',
            "text" : "(Why is he just staring at me)",
            "options" : ["mention it", "dont mention it"],
            "next_states" : ["mention", "dont_mention_3"],
        },
        "dont_mention_3" : {
            "character" : 'Jay',
            "text" : "...",
            "options" : ["mention it", "dont mention it"],
            "next_states" : ["mention", "dont_mention_4"],
        },
        "dont_mention_4" : {
            "character" : 'Jay',
            "text" : "...",
            "options" : ["mention it", "dont mention it"],
            "next_states" : ["mention", "dont_mention_5"],
        },
        "dont_mention_5" : {
            "character" : 'Goob',
            "text" : "(has this guy got a problem or something?)",
            "options" : ["mention it", "dont mention it"],
            "next_states" : ["mention", "dont_mention_6"],
        },
        "dont_mention_6" : {
            "character" : 'Goob',
            "text" : "(Why does he keep doing that)",
            "options" : ["mention it", "dont mention it"],
            "next_states" : ["mention", "dont_mention_7"],
        },
        "dont_mention_7" : {
            "character" : 'Goob',
            "text" : "(I give up)",
            "options" : [],
            "next_states" : ["mention"],
        },
    }

    event = EventDialogue(game_state, event_dialogue, font, screen_size, background=background, screen=screen)
    event.portraits = portraits
    return event