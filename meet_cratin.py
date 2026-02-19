import pygame
from event_dialogue import EventDialogue


def meet_cratin_event(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/city.png").convert()
    portraits = {"Cratin" : pygame.image.load("graphics/portraits/cratin.png").convert_alpha(), 
                 "Goob" : pygame.image.load("graphics/portraits/goob_sprite.png").convert_alpha(),
                 }
    event_dialogue = {
        "start" : {
            "text" : "*BASH*",
            "options" : [],
            "next_states" : ["cratin_start"]
        },
        "cratin_start" : {
            "character" : "Cratin",
            "text" : "HEY, I'M WALKIN HERE",
            "options" : ["apologise", "who the hell is this guy"],
            "next_states" : ["goob_apologise", "goob_square_up"]
        },
        "goob_square_up" : {
            "character" : "Goob",
            "text" : "Watch where you're going then!",
            "options" : [],
            "next_states" : ["goob_square_up_2"]
        },
        "goob_square_up_2" : {
            "character" : "Cratin",
            "text" : "YOU WATCH WHERE YOU'RE GOING",
            "options" : [],
            "next_states" : ["goob_insults"]
        },
        "goob_apologise" : {
            "character" : "Goob",
            "text" : "Sorry - didn't see you there",
            "options" : [],
            "next_states" : ["goob_apologise_2"]
        },
        "goob_apologise_2" : {
            "character" : "Cratin",
            "text" : "YEAH WELL WATCH IT",
            "options" : [],
            "next_states" : ["goob_insults"]
        },
        "goob_insults" : {
            "character" : "Goob",
            "text" : "What? cretin.",
            "options" : [],
            "next_states" : ["goob_insults_2"]
        },
        "goob_insults_2" : {
            "character" : "Cratin",
            "text" : "WHAT'D YOU SAY?",
            "options" : [],
            "next_states" : ["goob_insults_3"]
        },
        "goob_insults_3" : {
            "character" : "Goob",
            "text" : "CRET-IN.",
            "options" : [],
            "next_states" : ["goob_insults_4"]
        },
        "goob_insults_4" : {
            "character" : "Cratin",
            "text" : "YOU-",
            "options" : [],
            "next_states" : ["goob_insults_5"]
        },
        "goob_insults_5" : {
            "character" : "Cratin",
            "text" : "wait",
            "options" : [],
            "next_states" : ["goob_insults_6"]
        },
        "goob_insults_6" : {
            "character" : "Cratin",
            "text" : "awww how did I not notice that",
            "options" : [],
            "next_states" : ["goob_insults_7"]
        },
        "goob_insults_7" : {
            "text" : "The angered crate storms off",
            "options" : [],
            "next_states" : []
        },
    }

    event = EventDialogue(game_state, event_dialogue, font, screen_size, background=background, screen=screen)
    event.portraits = portraits
    return event