import pygame
from event_dialogue import EventDialogue


def lose_hat_event(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/forest.png").convert()
    portraits = {
        "Goob": pygame.image.load("graphics/portraits/goob_sprite.png").convert_alpha(),
    }

    event_dialogue = {
        "start": {
            "character": "Goob",
            "text": "Something feels… wrong.",
            "options": [],
            "next_states": ["notice"],
        },
        "notice": {
            "character": "Goob",
            "text": "My head feels colder.",
            "options": [],
            "next_states": ["realisation"],
        },
        "realisation": {
            "character": "Goob",
            "text": "Oh. My hat's gone.",
            "options": [],
            "next_states": ["accept"],
        },
        "accept": {
            "character": "Goob",
            "text": "I'll never forget you.",
            "options": [],
            "next_states": [],
            "reward": lambda gs: gs.add_hats(-1)
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