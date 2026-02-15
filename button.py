import pygame

class Button():
    def __init__(self, x, y, width, height, text='Button', onclick, font, screen, one_press=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.onclick = onclick
        self.font = font
        self.screen = screen
        self.one_press = one_press
        self.already_pressed = False

        self.fillColors = {
            'normal': "#FF4D21",
            'hover' : "#EC6F6F",
            'pressed': '#C5FAAF',
        }

        self.surface = pygame.Surface((width, height))
        self.text_surf = font.render(text, True, "white")


    def process(self):
        mouse = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])

        if self.rect.collidepoint(mouse):
            self.surface.fill(self.colors["hover"])
            if pygame.mouse.get_pressed()[0]:
                self.surface.fill(self.colors["pressed"])
                if self.one_press or not self.already_pressed:
                    self.onclick()
                    self.already_pressed = True
            else:
                self.already_pressed = False

        self.surface.blit(
            self.text_surf,
            self.text_surf.get_rect(center=self.surface.get_rect().center)
        )

        self.screen.blit(self.surface, self.rect)