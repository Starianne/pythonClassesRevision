class EventManager:
    def __init__(self):
        self.current_event = None
        self.current_event_flag = None

    def start_event(self, event, flag=None):
        self.current_event = event
        self.current_event_flag = flag

    def is_active(self):
        return self.current_event is not None
    
    def update(self, events, screen):
        if not self.current_event:
            return False
        
        if not self.current_event.started:
            self.current_event.start()

        self.current_event.handle_input(events)
        self.current_event.update()
        self.current_event.draw(screen, events)

        if self.current_event.done:
            if self.current_event_flag:
                self.current_event.game_state.set_flag(self.current_event_flag)
            self.current_event = None
            self.current_event_flag = None
            return False
        
        return True