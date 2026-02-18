import pygame

class Button:
    def __init__(self, x, y, width, height, font, onclick, text='Button', screen=None, one_press=False):
        #ordered to match main.py buttons
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.onclick = onclick
        self.font = font
        self.screen = screen


        self.fill_colors = {
            'normal': "#FF4D21",
            'hover': "#EC6F6F",
            'pressed': '#C5FAAF',
        }

        self.surface = pygame.Surface((width, height))
        self.padding = 12
        self.text_lines = self.wrap_text(self.text, (self.rect.width - self.padding * 2))
        self.text_surfs = [
            self.font.render(line.strip(), True, "white")
            for line in self.text_lines #kind of like tertanary 
        ]


    def wrap_text(self, text, max_width):
        words = text.split(" ") #splits text into array with words
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + (" " if current_line != "" else "") + word #ternary operators might be the goat
            if self.font.size(test_line)[0] <= max_width:
                current_line = test_line
            else: 
                lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        return lines

    def process(self, events):
        mouse = pygame.mouse.get_pos()
        clicked = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True
        
        self.surface.fill(self.fill_colors['normal'])# draw normal state first

        if self.rect.collidepoint(mouse):
            self.surface.fill(self.fill_colors['hover'])

        # click state
            if clicked:
                self.surface.fill(self.fill_colors['pressed'])
                self.onclick()

        if self.text_surfs:
            total_text_height = sum(surf.get_height() for surf in self.text_surfs)
            start_y = (self.surface.get_height() - total_text_height) // 2

            for surf in self.text_surfs:
                text_rect = surf.get_rect(centerx = self.surface.get_width() // 2, y = start_y)
                self.surface.blit(surf, text_rect)
                start_y += surf.get_height()


        if self.screen:
            self.screen.blit(self.surface, self.rect)