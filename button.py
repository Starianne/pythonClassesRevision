import pygame

class Button:
    def __init__(self, x, y, width, height, font, onclick, text='Button', screen=None, one_press=False):
        #ordered to match main.py buttons
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.onclick = onclick
        self.font = font
        self.screen = screen
        self.one_press = one_press
        self.already_pressed = False

        self.fill_colors = {
            'normal': "#FF4D21",
            'hover': "#EC6F6F",
            'pressed': '#C5FAAF',
        }

        self.surface = pygame.Surface((width, height))
        try: # to stop error at when you close game
            self.text_surf = self.font.render(self.text, True, "white")
        except Exception:
            self.text_surf = None

        # If no screen provided, use the current display surface
        if self.screen is None:
            try:
                self.screen = pygame.display.get_surface()
            except Exception:
                self.screen = None

        try:
            import main
            if hasattr(main, 'objects'):
                main.objects.append(self)
        except Exception:
            pass

    def process(self):
        mouse = pygame.mouse.get_pos()

        # draw normal state first
        self.surface.fill(self.fill_colors['normal'])

        if self.rect.collidepoint(mouse):
            self.surface.fill(self.fill_colors['hover'])
            if pygame.mouse.get_pressed()[0]:
                self.surface.fill(self.fill_colors['pressed'])
                if self.one_press or not self.already_pressed:
                    try:
                        self.onclick()
                    except Exception:
                        pass
                    self.already_pressed = True
            else:
                self.already_pressed = False

        if self.text_surf:
            self.surface.blit(
                self.text_surf,
                self.text_surf.get_rect(center=self.surface.get_rect().center),
            )

        if self.screen:
            self.screen.blit(self.surface, self.rect)