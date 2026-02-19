import pygame
from event_dialogue import EventDialogue


def molly_real_name_event(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/forest.png").convert()
    portraits = {
        "Holly": pygame.image.load("graphics/portraits/holly.png").convert_alpha(),
        "Molly": pygame.image.load("graphics/portraits/molly.png").convert_alpha(),
        "Goob": pygame.image.load("graphics/portraits/goob_sprite.png").convert_alpha(),
    }

    event_dialogue = {
        "goob_start": {
            "character": "Goob",
            "text": "So... what were you two like as kids?",
            "options": [],
            "next_states": ["holly_reminisce"],
        },
        "holly_reminisce": {
            "character": "Holly",
            "text": "Oh, you know. Molly was loud, angry, and impossible.",
            "options": [],
            "next_states": ["molly_offended"],
        },
        "molly_offended": {
            "character": "Molly",
            "text": "Hey!",
            "options": [],
            "next_states": ["holly_tease"],
        },
        "holly_tease": {
            "character": "Holly",
            "text": "And she didn't go by Molly, you wanna know her real name? Sassafras.",
            "options": [],
            "next_states": ["molly_panic"],
        },
        "molly_panic": {
            "character": "Molly",
            "text": "WHY WOULD YOU TELL HIM THAT.",
            "options": [],
            "next_states": ["goob_confused"],
        },
        "goob_confused": {
            "character": "Goob",
            "text": "Oh. I mean, it's unique?",
            "options": [],
            "next_states": ["holly_smug"],
        },
        "holly_smug": {
            "character": "Holly",
            "text": "Right? She's been mad about it since we were five.",
            "options": [],
            "next_states": ["molly_threatens"],
        },
        "molly_threatens": {
            "character": "Molly",
            "text": "I trusted you.",
            "options": [],
            "next_states": ["goob_soft"],
        },
        "goob_soft": {
            "character": "Goob",
            "text": "Hey, hey. I won't call you that. Probably.",
            "options": [],
            "next_states": ["goob_ends"],
        },
        "goob_ends": {
            "character": "Goob",
            "text": "But I will bring it up if you ever call me a weird red thing.",
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
