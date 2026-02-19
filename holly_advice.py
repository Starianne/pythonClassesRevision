import pygame
from event_dialogue import EventDialogue


def holly_advice_event(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/forest.png").convert()
    portraits = {"Holly" : pygame.image.load("graphics/portraits/placeholder.png").convert_alpha(), 
                 "Goob" : pygame.image.load("graphics/portraits/goob_sprite.png").convert_alpha(),
                 }
    event_dialogue = {
        "holly_start": {
            "character": "Holly",
            "text": "Hey. Uh. You got a minute?",
            "options": [],
            "next_states": ["holly_explains"],
        },
        "holly_explains": {
            "character": "Holly",
            "text": "I'm thinking about going to uni. Don't make a big deal out of it.",
            "options": [],
            "next_states": ["holly_worried"],
        },
        "holly_worried": {
            "character": "Holly",
            "text": "But my sister's gonna laugh at me. Or get mad. Or both.",
            "options": [],
            "next_states": ["goob_responds"],
        },
        "goob_responds": {
            "character": "Goob",
            "text": "Oh, uh. What do you wanna do?",
            "options": ["Support Holly", "Think about her sister"],
            "next_states": ["goob_supports", "goob_warns"],
        },
        "goob_supports": {
            "character": "Goob",
            "text": "I think you should do it. It's your life, not hers, and maybe she'll be happy for you?",
            "options": [],
            "next_states": ["holly_decides_yes"],
        },
        "goob_warns": {
            "character": "Goob",
            "text": "I mean… your sister's important to you. Maybe think it over?",
            "options": [],
            "next_states": ["holly_decides_no"],
        },
        "holly_decides_yes": {
            "character": "Holly",
            "text": "Yeah… yeah, you're right. She'll freak out, but she always does.",
            "options": [],
            "next_states": ["holly_confident"],
            "reward" : lambda gu: gu.set_flag("uni"),
        },
        "holly_confident": {
            "character": "Holly",
            "text": "I'm doing it. Thanks. Don't tell anyone.",
            "options": [],
            "next_states": ["goob_ends"],
        },
        "holly_decides_no": {
            "character": "Holly",
            "text": "Ugh… I hate that you're right. I don't wanna hurt her.",
            "options": [],
            "next_states": ["holly_soft"],
        },
        "holly_soft": {
            "character": "Holly",
            "text": "Maybe I'll wait. Just for now.",
            "options": [],
            "next_states": ["goob_ends"],
        },
        "goob_ends": {
            "character": "Goob",
            "text": "Uh. Good luck. Either way.",
            "options": [],
            "next_states": [],
        },
    }
    event = EventDialogue(game_state, event_dialogue, font, screen_size, background=background, screen=screen)
    event.portraits = portraits
    return event

