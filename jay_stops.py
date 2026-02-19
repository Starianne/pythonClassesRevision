import pygame
from event_dialogue import EventDialogue


def jay_stops_event(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/forest.png").convert()
    portraits = {
        "Jay": pygame.image.load("graphics/portraits/jay.png").convert_alpha(),
        "Goob": pygame.image.load("graphics/portraits/goob_sprite.png").convert_alpha(),
    }

    event_dialogue = {
        "jay_start": {
            "character": "Jay",
            "text": "You lied.",
            "options": [],
            "next_states": ["goob_confused"],
        },
        "goob_confused": {
            "character": "Goob",
            "text": "Uh. About what?",
            "options": [],
            "next_states": ["jay_explains"],
        },
        "jay_explains": {
            "character": "Jay",
            "text": "The lemon drops. Joel asked you.",
            "options": [],
            "next_states": ["goob_defends"],
        },
        "goob_defends": {
            "character": "Goob",
            "text": "I didn't wanna hurt his feelings.",
            "options": [],
            "next_states": ["jay_disappointed"],
        },
        "jay_disappointed": {
            "character": "Jay",
            "text": "Lying hurts more.",
            "options": [],
            "next_states": ["goob_apologizes"],
        },
        "goob_apologizes": {
            "character": "Goob",
            "text": "Uh... yeah. I guess you're right.",
            "options": [],
            "next_states": ["jay_ends"],
        },
        "jay_ends": {
            "character": "Jay",
            "text": "Be honest next time.",
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