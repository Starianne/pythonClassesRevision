import pygame
from event_dialogue import EventDialogue


def molly_advice_event(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/forest.png").convert()
    portraits = {
        "Molly": pygame.image.load("graphics/portraits/molly.png").convert_alpha(),
        "Goob": pygame.image.load("graphics/portraits/goob_sprite.png").convert_alpha(),
    }

    event_dialogue = {
        "molly_start": {
            "character": "Molly",
            "text": "Hey Goob, decide something for me.",
            "options": [],
            "next_states": ["molly_explains"],
        },
        "molly_explains": {
            "character": "Molly",
            "text": "It's Holly's birthday soon, and I don't know what to get her.",
            "options": [],
            "next_states": ["goob_asks"],
        },
        "goob_asks": {
            "character": "Goob",
            "text": "Huh what kind of stuff does she like?",
            "options": [],
            "next_states": ["molly_options"],
        },
        "molly_options": {
            "character": "Molly",
            "text": "She loves anything cute, but like maybe books would be better? And like with a massive thing of sweets",
            "options": ["Get a cute gift", "Get a book"],
            "next_states": ["goob_cute", "goob_practical"],
        },
        "goob_cute": {
            "character": "Molly",
            "text": "Yeah you know what, I think I saw something on her Wintrest",
            "options": [],
            "next_states": ["molly_decides"],
        },
        "goob_practical": {
            "character": "Goob",
            "text": "A book would be good, don't you think? I swear I saw her reading out here a couple of days ago too.",
            "options": [],
            "next_states": ["molly_decides"],
        },
        "goob_sweets": {
            "character": "Goob",
            "text": "Sweets are always a safe bet",
            "options": [],
            "next_states": ["molly_decides"],
        },
        "molly_decides": {
            "character": "Molly",
            "text": "Yeah I'll go look for it later then. Thanks.",
            "options": [],
            "next_states": ["goob_ends"],
        },
        "goob_ends": {
            "character": "Goob",
            "text": "Nooo problem.",
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
