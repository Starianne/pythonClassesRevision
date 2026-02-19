import pygame
from event_dialogue import EventDialogue


def jay_meet_event(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/forest.png").convert()
    portraits = {
        "Jay": pygame.image.load("graphics/portraits/placeholder.png").convert_alpha(),
        "Goob": pygame.image.load("graphics/portraits/goob_sprite.png").convert_alpha(),
    }

    event_dialogue = {
        "jay_start": {
            "character": "Jay",
            "text": "You told him.",
            "options": [],
            "next_states": ["goob_unsure"],
        },
        "goob_unsure": {
            "character": "Goob",
            "text": "Told Joel... about the lemon drops?",
            "options": [],
            "next_states": ["jay_confirms"],
        },
        "jay_confirms": {
            "character": "Jay",
            "text": "Yeah.",
            "options": [],
            "next_states": ["goob_explains"],
        },
        "goob_explains": {
            "character": "Goob",
            "text": "I figured he should know.",
            "options": [],
            "next_states": ["jay_approves"],
        },
        "jay_approves": {
            "character": "Jay",
            "text": "Good.",
            "options": [],
            "next_states": ["goob_relieved"],
        },
        "goob_relieved": {
            "character": "Goob",
            "text": "...Good?",
            "options": [],
            "next_states": ["jay_adds"],
        },
        "jay_adds": {
            "character": "Jay",
            "text": "Honesty matters.",
            "options": [],
            "next_states": ["jay_ends"],
        },
        "jay_ends": {
            "character": "Jay",
            "text": "Joel trusts you.",
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