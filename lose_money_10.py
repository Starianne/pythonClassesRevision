import pygame
from event_dialogue import EventDialogue


def lose_money_10_event(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/forest.png").convert()
    portraits = {
        "Goob": pygame.image.load("graphics/portraits/goob_sprite.png").convert_alpha(),
    }

    event_dialogue = {
        "start": {
            "character": "Goob",
            "text": "It's always nice out when I walk through here",
            "options": [],
            "next_states": ["take_it"],
        },
        "take_it": {
            "character": "Goob",
            "text": "Makes me forget everything (£10 drop from his wallet)",
            "options": [],
            "next_states": [],
            "reward": lambda give_money: give_money.add_money(-10),
        },
    }

    event = EventDialogue(game_state, event_dialogue, font, screen_size, background=background, screen=screen)
    event.portraits = portraits
    return event