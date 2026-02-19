import pygame
from event_dialogue import EventDialogue


def joel_hangout_event(game_state, font, screen_size, screen=None):
    background = pygame.image.load("graphics/backgrounds/forest.png").convert()
    portraits = {
        "Joel": pygame.image.load("graphics/portraits/placeholder.png").convert_alpha(),
        "Jay": pygame.image.load("graphics/portraits/placeholder.png").convert_alpha(),
    }

    event_dialogue = {
        "joel_start": {
            "character": "Joel",
            "text": "Oh— hey. Didn't expect to see you out here.",
            "options": [],
            "next_states": ["jay_response"],
        },
        "jay_response": {
            "character": "Jay",
            "text": "Was bored.",
            "options": [],
            "next_states": ["joel_relaxed"],
        },
        "joel_relaxed": {
            "character": "Joel",
            "text": "Fair. I was gonna walk for a bit.",
            "options": [],
            "next_states": ["jay_joins"],
        },
        "jay_joins": {
            "character": "Jay",
            "text": "I'll come.",
            "options": [],
            "next_states": ["joel_surprised"],
        },
        "joel_surprised": {
            "character": "Joel",
            "text": "Oh! Uh— yeah. Sure.",
            "options": [],
            "next_states": ["walking_silence"],
        },
        "walking_silence": {
            "character": "Jay",
            "text": "...",
            "options": [],
            "next_states": ["joel_smalltalk"],
        },
        "joel_smalltalk": {
            "character": "Joel",
            "text": "It's nice out today.",
            "options": [],
            "next_states": ["jay_agrees"],
        },
        "jay_agrees": {
            "character": "Jay",
            "text": "Yeah.",
            "options": [],
            "next_states": ["jay_admits"],
        },
        "jay_agrees": {
            "character": "Jay",
            "text": "Your friend.",
            "options": [],
            "next_states": ["joel_questions"],
        },
        "joel_questions": {
            "character": "Joel",
            "text": "Yeah?",
            "options": [],
            "next_states": ["jay_approves"],
        },
        "jay_approves": {
            "character": "Jay",
            "text": "He's alright",
            "options": [],
            "next_states": ["joel_agrees"],
        },
        "joel_agrees": {
            "character": "Joel",
            "text": "Oh, yeah he's pretty cool.",
            "options": [],
            "next_states": ["joel_content"],
        },
        "joel_content": {
            "character": "Joel",
            "text": "... You know",
            "options": [],
            "next_states": ["joel_content_2"],
        },
        "joel_content_2": {
            "character": "Joel",
            "text": "I'm glad you started coming out again.",
            "options": [],
            "next_states": ["jay_final"],
        },
        "jay_final": {
            "character": "Jay",
            "text": "Me too.",
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
