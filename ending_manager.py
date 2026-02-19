from endings_list import ENDINGS

def select_ending(game_state):
    valid = []

    for ending in ENDINGS:
        if all(req(game_state) for req in ending["requires"]):
            valid.append(ending)

    valid.sort(key=lambda e: e["priority"], reverse=True)
    return valid[0] if valid else None