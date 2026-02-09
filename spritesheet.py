import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0,0), ((frame * width),0 ,width,height)) #sprite sheet, start blitting from topleft corner of spritesheet, area from topleft corner to bottom right (of frame)
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey((0,0,0)) #removes the black background from sprite image
        return image