class Event:
    def __init__(self, game_state):
        self.game_state = game_state
        self.done = False

    def handle_input(self, events):
        pass

    def update(self, dt):
        pass

    def draw(Self, screen):
        pass