import pygame
from event_dialogue import EventDialogue


def holly_uni_ending(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/city.png").convert()
    portraits = {
        "Holly": pygame.image.load("graphics/portraits/holly.png").convert_alpha(),
        "Goob": pygame.image.load("graphics/portraits/goob_sprite.png").convert_alpha(),
    }

    event_dialogue = {
        "start": {
            "character": "Holly",
            "text": "Thanks for coming to see me off.",
            "options": [],
            "next_states": ["goob_reply"],
        },
        "goob_reply": {
            "character": "Goob",
            "text": "You'll be great at uni, Holly!",
            "options": [],
            "next_states": ["holly_smile"],
        },
        "holly_smile": {
            "character": "Holly",
            "text": "Well hopefully, but thanks for convincing me",
            "options": [],
            "next_states": ["end"],
        },
        "end": {
            "character": "Goob",
            "text": "Just come back with something useful",
            "options": [],
            "next_states": [],
        },
    }

    event = EventDialogue(
        game_state, event_dialogue, font, screen_size, background=background, screen=screen
    )
    event.portraits = portraits
    return event