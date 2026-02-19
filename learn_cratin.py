import pygame
from event_dialogue import EventDialogue


def learn_cratin_event(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/city.png").convert()
    portraits = {
        "Cratin": pygame.image.load("graphics/portraits/cratin.png").convert_alpha(),
        "Goob": pygame.image.load("graphics/portraits/goob_sprite.png").convert_alpha(),
    }

    event_dialogue = {
        "cratin_start": {
            "character": "Cratin",
            "text": "Oi. You there.",
            "options": [],
            "next_states": ["goob_cautious"],
        },
        "goob_cautious": {
            "character": "Goob",
            "text": "Oh. Hey?",
            "options": [],
            "next_states": ["cratin_apology"],
        },
        "cratin_apology": {
            "character": "Cratin",
            "text": "About the other day. I came in a bit hot.",
            "options": [],
            "next_states": ["goob_listens"],
        },
        "goob_listens": {
            "character": "Goob",
            "text": "Yeah?",
            "options": [],
            "next_states": ["cratin_realisation"],
        },
        "cratin_realisation": {
            "character": "Cratin",
            "text": "You called me a cretin.",
            "options": [],
            "next_states": ["cratin_realisation_2"],
        },
        "cratin_realisation_2": {
            "character": "Cratin",
            "text": "Took me a day to realise the boys at work do the same.",
            "options": [],
            "next_states": ["cratin_story"],
        },
        "cratin_story": {
            "character": "Cratin",
            "text": "They say “crate-in”. Like me.",
            "options": [],
            "next_states": ["cratin_story_2"],
        },
        "cratin_story_2": {
            "character": "Cratin",
            "text": "Same word. Different spelling.",
            "options": [],
            "next_states": ["goob_understands"],
        },
        "goob_understands": {
            "character": "Goob",
            "text": "Ohhh... cool?",
            "options": [],
            "next_states": ["cratin_chuckles"],
        },
        "cratin_chuckles": {
            "character": "Cratin",
            "text": "Yeah. Kinda funny though.",
            "options": [],
            "next_states": ["cratin_no_malice"],
        },
        "cratin_no_malice": {
            "character": "Cratin",
            "text": "No malice in it. Just the guys you know.",
            "options": [],
            "next_states": ["goob_apologises"],
        },
        "goob_apologises": {
            "character": "Goob",
            "text": "Sorry. Just got a bit annoyed",
            "options": [],
            "next_states": ["cratin_accepts"],
        },
        "cratin_accepts": {
            "character": "Cratin",
            "text": "All good. Gave me a laugh in the end.",
            "options": [],
            "next_states": ["cratin_end"],
        },
        "cratin_end": {
            "character": "Cratin",
            "text": "We're square.",
            "options": [],
            "next_states": ["goob_end"],
        },
        "goob_end": {
            "character": "Goob",
            "text": "Actually I think you're cubed.",
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