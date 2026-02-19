from endings.true_friend import true_friend_ending
from endings.default import default_ending

ENDINGS = [
    {
        "id" : "true_friend",
        "priority": 100,
        "requires" : [
            lambda g: g.get_flag("honest")
        ],
        "event" : true_friend_ending
    },
    {
        "id" : "default",
        "priority": 0,
        "requires" : [],
        "event" : default_ending
    }
]