import pygame
from text_box import Textbox
from base_event import BaseEvent
from button import Button

#tomorrow add in button for choices

class EventDialogue(BaseEvent):
    def __init__(self, game_state, dialogue, font, screen_size):
        super().__init__(game_state)
        self.dialogue = dialogue
        self.current_key = list(dialogue.keys())[0] #keys - this is a dictionary!!
        self.font = font
        self.screen_width, self.screen_height = screen_size
        self.textbox = None
        self.last_node = None

    def handle_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                next_states = self.dialogue[self.current_key]["next_states"]
                if next_states:
                    self.current_key = next_states[0]
                else:
                    self.done = True

    def update(self):
        node = self.dialogue[self.current_key]
        self.textbox = Textbox(node["text"], self.font, self.screen_width, self.screen_height)
        self.last_node = self.current_key

    def draw(self, screen):
        if self.textbox:
            self.textbox.draw(screen)

