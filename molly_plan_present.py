import pygame
from event_dialogue import EventDialogue


def molly_plan_present_event(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/forest.png").convert()
    portraits = {
        "Molly": pygame.image.load("graphics/portraits/placeholder.png").convert_alpha(),
        "Goob": pygame.image.load("graphics/portraits/goob_sprite.png").convert_alpha(),
    }

    event_dialogue = {
        "molly_start": {
            "character": "Molly",
            "text": "Hey Goob, I got her gift. How do you think I should give it to her?",
            "options": [],
            "next_states": ["goob_thinks"],
        },
        "goob_thinks": {
            "character": "Goob",
            "text": "Uhm well you could hand it to her directly, or maybe make it a little surprise.",
            "options": ["Directly", "Surprise her", "Leave it somewhere she'll find it"],
            "next_states": ["molly_direct", "molly_surprise", "molly_hide"],
        },
        "molly_direct": {
            "character": "Molly",
            "text": "Yeah, I think I'll just give it straight to her.",
            "options": [],
            "next_states": ["molly_confident"],
        },
        "molly_surprise": {
            "character": "Molly",
            "text": "Aw I could totally do the surprise thing she used to do to me when we were younger.",
            "options": [],
            "next_states": ["molly_confident"],
        },
        "molly_hide": {
            "character": "Molly",
            "text": "I could hide it somewhere and let her find it.. that could be cute.",
            "options": [],
            "next_states": ["molly_confident"],
        },
        "molly_confident": {
            "character": "Molly",
            "text": "K, I think I've got it. Thanks again",
            "options": [],
            "next_states": ["goob_ends"],
        },
        "goob_ends": {
            "character": "Goob",
            "text": "Good luck Molly!",
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