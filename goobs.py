import pygame
import spritesheet


#Goob's class
class Goob(pygame.sprite.Sprite):
    def __init__(self, scale, game_state):
        super().__init__()

        self.game_state = game_state
        # spritesheet:
        spritesheet_image = pygame.image.load('graphics/player/goob_spritesheet.png').convert_alpha()
        goob_spritesheet = spritesheet.SpriteSheet(spritesheet_image)
        self.scale = scale
        self.goob_index = 0

        # availability and invent
        self.horizontal_available = 1
        self.vertical_available = 1

        self.x_pos = 100
        self.y_pos = 100

        # goob frames
        goob_stand = goob_spritesheet.get_image(0, 24, 24, scale)
        goob_step = goob_spritesheet.get_image(1, 24, 24, scale)
        goob_crouch = goob_spritesheet.get_image(2, 24, 24, scale)
        goob_jump = goob_spritesheet.get_image(3, 24, 24, scale)
        goob_win = goob_spritesheet.get_image(4, 24, 24, scale)
        goob_look_bl = goob_spritesheet.get_image(5, 24, 24, scale)
        goob_look_br = goob_spritesheet.get_image(6, 24, 24, scale)
        goob_look_ul = goob_spritesheet.get_image(7, 24, 24, scale)
        goob_look_ur = goob_spritesheet.get_image(8, 24, 24, scale)
        goob_surprise = goob_spritesheet.get_image(9, 24, 24, scale)
        goob_sweetie = goob_spritesheet.get_image(10, 24, 24, scale)
        goob_money = goob_spritesheet.get_image(11, 24, 24, scale)
        goob_envelope = goob_spritesheet.get_image(12, 24, 24, scale)
        goob_key = goob_spritesheet.get_image(13, 24, 24, scale)
        goob_dead = goob_spritesheet.get_image(14, 24, 24, scale)

        self.goob_walk = [goob_stand, goob_step]
        self.goob_jumping = [goob_crouch, goob_jump]

        # set current image and rect
        self.image = self.goob_walk[0]
        self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))

    # availability / inventory methods
    def get_horizontal_available(self):
        return self.horizontal_available
    
    def get_vertical_available(self):
        return self.vertical_available


    def animation_state(self, state):
        if state == "walk":
            self.goob_index += 0.2
            if self.goob_index >= len(self.goob_walk):
                self.goob_index = 0
            self.image = self.goob_walk[int(self.goob_index)]

    def player_input(self):
        # only allow movement when available == 1
        keys = pygame.key.get_pressed()
        if self.horizontal_available == 1:
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.animation_state("walk")
                self.x_pos -= 6
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.animation_state("walk")
                self.x_pos += 6
            self.rect.x = self.x_pos

        if self.vertical_available == 1:
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self.animation_state("walk")
                self.y_pos -= 6
            elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self.animation_state("walk")
                self.y_pos += 6
            self.rect.y = self.y_pos
            

    def update(self):
        self.player_input()
