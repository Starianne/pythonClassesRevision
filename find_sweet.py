import pygame
from event_dialogue import EventDialogue

def find_sweet_event(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/forest.png").convert()
    portraits = {
        "Goob": pygame.image.load("graphics/portraits/goob_sprite.png").convert_alpha(),
    }

    event_dialogue = {
        "start": {
            "character": "Goob",
            "text": "Is that… a sweet?",
            "options": [],
            "next_states": ["hesitate"],
        },
        "hesitate": {
            "character": "Goob",
            "text": "It's probably fine.",
            "options": [],
            "next_states": ["take_it"],
        },
        "take_it": {
            "character": "Goob",
            "text": "Free sweet!",
            "options": [],
            "next_states": [],
            "reward": lambda give_sweets: give_sweets.add_sweets(1),
        },
    }

    event = EventDialogue(game_state, event_dialogue, font, screen_size, background=background, screen=screen)
    event.portraits = portraits
    return event