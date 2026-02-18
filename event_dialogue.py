import pygame
from text_box import Textbox
from base_event import BaseEvent
from button import Button


class EventDialogue(BaseEvent):
    def __init__(self, game_state, dialogue, font, screen_size, background=None, screen=None):
        super().__init__(game_state)
        self.dialogue = dialogue
        self.current_key = list(dialogue.keys())[0] #keys - this is a dictionary!!
        self.font = font
        self.screen_width, self.screen_height = screen_size
        self.background = background
        self.textbox = None
        self.last_node = None
        self.screen = screen

        self.choice_buttons = []
        self.waiting_for_choice = False

    def handle_input(self, events):
        if self.waiting_for_choice:
            return
        
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                next_states = self.dialogue[self.current_key]["next_states"]
                if next_states:
                    self.current_key = next_states[0]
                else:
                    self.done = True



    def create_choice_buttons(self, options, next_states):
        self.choice_buttons.clear()
        button_width = 400 
        button_height = 80
        spacing = 20
        total_height = len(options) * (button_height + spacing)
        start_y = self.screen_height - total_height - 50

        for i, option_text in enumerate(options):
            x = (self.screen_width - button_width) // 2
            y = start_y + i * (button_height + spacing)

            def hand_back_choice(state):
                return lambda: self.choose(state) #like anonymous function in javascript
        
            btn = Button(x, y, button_width, button_height, self.font, hand_back_choice(next_states[i]), option_text, screen=self.screen)
            self.choice_buttons.append(btn)

    def choose(self, next_key):
        self.current_key = next_key
        self.waiting_for_choice = False
        self.choice_buttons.clear()

    def update(self):
        node = self.dialogue[self.current_key]
        if self.last_node != self.current_key:
            self.textbox = Textbox(node["text"], self.font, self.screen_width, self.screen_height)
            self.choice_buttons.clear()
            self.waiting_for_choice = False
            options= node["options"]
            next_states = node["next_states"]

            if options:
                self.waiting_for_choice = True
                self.create_choice_buttons(options, next_states) #lets hope this will work

            reward = node.get("reward")
            if reward:
                reward(self.game_state)
        
        self.last_node = self.current_key
        

    def draw(self, screen):
        if self.background:
            self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
            screen.blit(self.background, (0,0)) #transform scale then blit

        node = self.dialogue[self.current_key]
        character = node.get("character")

        if character and character in self.portraits:
            portrait = self.portraits[character]
            screen.blit(portrait, (50, self.screen_height - portrait.get_height() - 150))

            name_surf = self.font.render(character, True, "black")
            screen.blit(name_surf, (50, self.screen_height - 200))


        if self.textbox:
            self.textbox.draw(screen)

        for btn in self.choice_buttons:
            btn.process()

