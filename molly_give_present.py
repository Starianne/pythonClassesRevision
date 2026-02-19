import pygame
from event_dialogue import EventDialogue


def molly_give_present_event(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/forest.png").convert()
    portraits = {
        "Holly": pygame.image.load("graphics/portraits/placeholder.png").convert_alpha(),
        "Goob": pygame.image.load("graphics/portraits/goob_sprite.png").convert_alpha(),
    }

    event_dialogue = {
        "holly_start": {
            "character": "Holly",
            "text": "Goob. Do you like my new book?",
            "options": [],
            "next_states": ["goob_listens"],
        },
        "goob_listens": {
            "character": "Goob",
            "text": "Oh. Uh. Yeah looks cool.",
            "options": [],
            "next_states": ["holly_excited"],
        },
        "holly_excited": {
            "character": "Holly",
            "text": "Molly got me my birthday present and it was actually really good.",
            "options": [],
            "next_states": ["goob_surprised"],
        },
        "goob_surprised": {
            "character": "Goob",
            "text": "Really?",
            "options": [],
            "next_states": ["holly_explains"],
        },
        "holly_explains": {
            "character": "Holly",
            "text": "Like- a hikitty plush, lord of the things book and these matcha sweets! Actually so good",
            "options": [],
            "next_states": ["holly_soft"],
        },
        "holly_soft": {
            "character": "Holly",
            "text": "She acted all casual about it, but like she really thought about it.",
            "options": [],
            "next_states": ["goob_responds"],
        },
        "goob_responds": {
            "character": "Goob",
            "text": "Sounds like she really cares.",
            "options": [],
            "next_states": ["holly_deflects"],
        },
        "holly_deflects": {
            "character": "Holly",
            "text": "Ew don't say that, only I can be nice about my sister",
            "options": [],
            "next_states": ["holly_grateful"],
        },
        "holly_grateful": {
            "character": "Holly",
            "text": "But yeah, it was really sweet",
            "options": [],
            "next_states": ["goob_ends"],
        },
        "goob_ends": {
            "character": "Goob",
            "text": "um glad you liked it then",
            "options": [],
            "next_states": [],
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