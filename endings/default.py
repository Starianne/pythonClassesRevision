import pygame
from event_dialogue import EventDialogue


def default_ending(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/forest.png").convert()
    event_dialogue = {
        "start" : {
            "character" : "Goob",
            "text" : "Well",
            "options" : [],
            "next_states" : ["end"]
        },
        "end" : {
            "character" : "Goob",
            "text" : "That was eventful",
            "options" : [],
            "next_states" : []
        },
    }
    return EventDialogue(game_state, event_dialogue, font, screen_size, background=background, screen=screen)