import pygame
from event_dialogue import EventDialogue


def find_money_5_event(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/forest.png").convert()
    portraits = {
        "Goob": pygame.image.load("graphics/portraits/goob_sprite.png").convert_alpha(),
    }

    event_dialogue = {
        "start": {
            "character": "Goob",
            "text": "Oh. Is that money?",
            "options": [],
            "next_states": ["take_it"],
        },
        "take_it": {
            "character": "Goob",
            "text": "£5 on the ground. Neat.",
            "options": [],
            "next_states": [],
            "reward": lambda give_money: give_money.add_money(5),
        },
    }

    event = EventDialogue(game_state, event_dialogue, font, screen_size, background=background, screen=screen)
    event.portraits = portraits
    return event