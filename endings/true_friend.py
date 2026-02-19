import pygame
from event_dialogue import EventDialogue


def true_friend_ending(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/forest.png").convert()
    event_dialogue = {
        "start" : {
            "character" : "Jay",
            "text" : "You know Goob,",
            "options" : [],
            "next_states" : ["end"]
        },
        "end" : {
            "character" : "Jay",
            "text" : "You're alright.",
            "options" : [],
            "next_states" : []
        },
    }
    return EventDialogue(game_state, event_dialogue, font, screen_size, background=background, screen=screen)