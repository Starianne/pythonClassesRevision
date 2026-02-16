class BaseEvent:
    def __init__(self, game_state):
        self.game_state = game_state
        self.done = False
        self.started = False
        self.background = None
        self.portraits = {}
        self.current_speaker = None

    def start(self):
        self.started = True

    def handle_input(self, events):
        pass

    def update(self):
        pass

    def draw(self, screen):
        if self.background:
            screen.blit(self.background, (0,0))