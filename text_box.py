import pygame


class Textbox():
    def __init__(self, text, font, screen_width, screen_height):
        self.text = text
        self.font = font
        self.x, self.y = screen_width/3, screen_height/3

        self.line_width = screen_width//3
        self.padding = 10

        self.lines = self.wrap_text()
        self.line_height = self.font.get_height()
        self.area_height = len(self.lines) * self.line_height + self.padding * 2

        self.message_back_surface = pygame.Surface((self.line_width, self.area_height))
        self.message_back_surface.fill("white") #to set up textbox
    
    def wrap_text(self):
        words = self.text.split(" ") #splits text into array with words
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + (" " if current_line != "" else "") + word #ternary operators might be the goat
            if self.font.size(test_line)[0] <= self.line_width - self.padding * 2:
                current_line = test_line
            else: 
                lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        return(lines)

    def draw(self, screen):
        self.message_back_surface.fill("white") #to cover old text box

        y=self.padding
        for line in self.lines:
            text_surf = self.font.render(line, True, "black")
            self.message_back_surface.blit(text_surf, (self.padding, y))
            y += self.line_height
        
        screen.blit(self.message_back_surface, (self.x, self.y))
