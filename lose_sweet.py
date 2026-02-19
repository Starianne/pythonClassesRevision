import pygame
from event_dialogue import EventDialogue


def lose_sweet_event(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/forest.png").convert()
    portraits = {
        "Goob": pygame.image.load("graphics/portraits/goob_sprite.png").convert_alpha(),
    }

    event_dialogue = {
        "start": {
            "character": "Goob",
            "text": "Wait… I had more sweets than this.",
            "options": [],
            "next_states": ["realisation"],
        },
        "realisation": {
            "character": "Goob",
            "text": "Oh no.",
            "options": [],
            "next_states": ["accept"],
        },
        "accept": {
            "character": "Goob",
            "text": "One of them is gone.",
            "options": [],
            "next_states": [],
            "reward": lambda give_sweets: give_sweets.add_sweets(-1),
        },
    }

    event = EventDialogue(
        game_state,
        event_dialogue,
        font,
        screen_size,
        background=background,
        screen=screen,
    )
    event.portraits = portraits
    return event