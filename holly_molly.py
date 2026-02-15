from event_dialogue import EventDialogue
Holly = None
Holly_rect = None
Molly = None
Molly_rect = None
Goob = None



def holly_molly_event(game_state, font, screen_size):
    event_dialogue = {
        "holly_start" : {
            "character" : Holly,
            "text" : "Hey, weird red thing",
            "options" : [],
            "next_states" : ["molly_start"]
        },
        "molly_start" : {
            "character" : Molly,
            "text" : "We need you to like, answer this question",
            "options" : [],
            "next_states" : ["holly_question"],
        },
            "holly_question" : {
            "character" : Holly,
            "text" : "Which season is better?",
            "options" : [],
            "next_states" : ["goob_answers"],
        },
            "goob_answers" : {
            "character" : Goob,
            "text" : "Uhhhhh",
            "options" : ["Winter", "Summer"],
            "next_states" : ["molly_agrees", "holly_agrees"],
        },
            "molly_agrees" : {
            "character" : Molly,
            "text" : "See Holly? Summer is for losers, you can literally just sit in a sunbed.",
            "options" : [],
            "next_states" : ["molly_rewards"],
        },
            "holly_agrees" : {
            "character" : Holly,
            "text" : "See Molly? I told you, Summer is the best.",
            "options" : [],
            "next_states" : ["holly_rewards"],
        },
            "molly_rewards" : {
            "character" : Molly,
            "text" : "Take this, since you weren't a moron",
            "options" : [],
            "next_states" : ["holly_grumbles"],
        },
            "holly_rewards" : {
            "character" : Holly,
            "text" : "Since you made the OBVIOUS correct choice",
            "options" : [],
            "next_states" : ["molly_grumbles"],
        },
            "molly_grumbles" : {
            "character" : Molly,
            "text" : "Go and crisp somewhere",
            "options" : [],
            "next_states" : ["goob_thanks"],
        },
            "holly_grumbles" : {
            "character" : Holly,
            "text" : "yeah whatever",
            "options" : [],
            "next_states" : ["goob_thanks"],
        },
            "goob_thanks" : {
            "character" : Goob,
            "text" : "thanks",
            "options" : [],
            "next_states" : [],
        },
    }
    
    return EventDialogue(game_state, event_dialogue, font, screen_size)

