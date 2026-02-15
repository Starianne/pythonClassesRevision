class GameState:
    def __init__(self):
        self.money = 0
        self.keys = 0
        self.sweets = 0
        self.hats = 0
        self.flags = {}

    def set_flag(self, name, value=True):
        self.flags[name] = value
    
    def get_flag(self, name):
        return self.flags.get(name, False)