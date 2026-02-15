class BaseEvent:
    def __init__(self, game_state):
        self.game_state = game_state
        self.done = False
        self.started = False

    def start(self):
        self.started = True

    def handle_input(self, events):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass