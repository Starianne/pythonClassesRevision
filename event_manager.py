class EventManager:
    def __init__(self):
        self.current_event = None

    def start_event(self, event):
        self.current_event = event
    
    def update(self, events, screen):
        if not self.current_event:
            return False
        
        if not self.current_event.started:
            self.current_event.start()

        self.current_event.handle_input(events)
        self.current_event.update()
        self.current_event.draw(screen)

        if self.current_event.done:
            self.current_event = None
            return False
        
        return True