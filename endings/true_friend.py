import pygame
from event_dialogue import EventDialogue


def true_friend_ending(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/forest.png").convert()
    portraits = {"Jay" : pygame.image.load("graphics/portraits/placeholder.png").convert_alpha(),
                 "Goob" : pygame.image.load("graphics/portraits/goob_sprite.png").convert_alpha(),}
    event_dialogue = {
        "start" : {
            "character" : "Jay",
            "text" : "You know Goob,",
            "options" : [],
            "next_states" : ["middle"]
        },
        "middle" : {
            "character" : "Jay",
            "text" : "We should hang out.",
            "options" : [],
            "next_states" : ["end"]
        },
        "end" : {
            "character" : "Goob",
            "text" : "Oh! Sure!",
            "options" : [],
            "next_states" : []
        },
    }
    event = EventDialogue(game_state, event_dialogue, font, screen_size, background=background, screen=screen)
    event.portraits = portraits
    return event
