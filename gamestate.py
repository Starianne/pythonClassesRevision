class GameState:
    def __init__(self):
        self.money = 0
        self.keys = 0 #not sure about this one right now
        self.sweets = 0
        self.hats = 0
        self.flags = {}
        self.event_log = []

    def set_flag(self, name, value=True):
        self.flags[name] = value
    
    def get_flag(self, name):
        return self.flags.get(name, False)
    

    def add_money(self, amount):
        self.money += amount
        self.add_log(f"Goob got +£{amount}")

    def add_sweets(self, amount):
        self.sweets += amount
        if amount == 1:
            self.add_log(f"Goob got +{amount} sweet")
        else:
            self.add_log(f"Goob got +{amount} sweets")

    def add_hats(self, amount):
        self.add_hats += amount
        if amount == 1:
            self.add_log(f"Goob got +{amount} hat")
        else:
            self.add_log(f"Goob got +{amount} hats")

    def add_log(self, message):
        self.event_log.append(message)
        self.event_log = self.event_log[-10:] #last 10 only