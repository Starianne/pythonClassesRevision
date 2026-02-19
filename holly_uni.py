import pygame
from event_dialogue import EventDialogue


def holly_uni_event(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/forest.png").convert()
    portraits = {
        "Holly": pygame.image.load("graphics/portraits/holly.png").convert_alpha(),
        "Molly": pygame.image.load("graphics/portraits/molly.png").convert_alpha(),
    }

    event_dialogue = {
        "holly_start": {
            "character": "Holly",
            "text": "Okay, don't laugh or like freak out at me.",
            "options": [],
            "next_states": ["molly_confused"],
        },
        "molly_confused": {
            "character": "Molly",
            "text": "What? Spit it out.",
            "options": [],
            "next_states": ["holly_confesses"],
        },
        "holly_confesses": {
            "character": "Holly",
            "text": "I'm... going to university. Or at least, I wanna.",
            "options": [],
            "next_states": ["holly_braces"],
        },
        "holly_braces": {
            "character": "Holly",
            "text": "You can say it. I know it sounds stupid, and I know we said we'd keep working at Kosta together, and-",
            "options": [],
            "next_states": ["molly_reacts"],
        },
        "molly_reacts": {
            "character": "Molly",
            "text": "Stupid? Please. You'd be stupid if you didn't go.",
            "options": [],
            "next_states": ["holly_surprised"],
        },
        "holly_surprised": {
            "character": "Holly",
            "text": "What? You sure?",
            "options": [],
            "next_states": ["molly_supports"],
        },
        "molly_supports": {
            "character": "Molly",
            "text": "I mean, someone's gotta be the smart one. Might as well be you.",
            "options": [],
            "next_states": ["holly_relief"],
        },
        "holly_relief": {
            "character": "Holly",
            "text": "You're not mad?",
            "options": [],
            "next_states": ["molly_soft"],
        },
        "molly_soft": {
            "character": "Molly",
            "text": "Nah. Just don't forget me when you're all like fancy and educated.",
            "options": [],
            "next_states": ["holly_grateful"],
        },
        "holly_grateful": {
            "character": "Holly",
            "text": "Of course I wouldn't...",
            "options": [],
            "next_states": ["molly_teases"],
        },
        "molly_teases": {
            "character": "Molly",
            "text": "Ugh, don't get emotional. Go be a nerd already.",
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
