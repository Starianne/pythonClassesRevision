import pygame
import spritesheet
import os
from sys import exit
from random import randint

class Goob(pygame.sprite.Sprite):
    def __init__(self, scale):
        super().__init__()

        # spritesheet:
        spritesheet_image = pygame.image.load('graphics/player/goob_spritesheet.png').convert_alpha()
        goob_spritesheet = spritesheet.SpriteSheet(spritesheet_image)
        self.scale = scale
        self.goob_index = 0

        # availability and invent
        self.available = 1
        self.money = 0
        self.keys = 0
        self.sweets = 0

        self.x_pos = 100

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
        self.rect = self.image.get_rect(topleft=(self.x_pos, 100))

    # availability / inventory methods
    def get_available(self):
        return self.available

    def add_money(self, money):
        self.money = money

    def add_keys(self, keys):
        self.keys = keys

    def add_sweets(self, sweets):
        self.sweets = sweets

    def get_money(self):
        return self.money

    def get_keys(self):
        return self.keys

    def get_sweets(self):
        return self.sweets

    def animation_state(self, state):
        if state == "walk":
            self.goob_index += 0.2
            if self.goob_index >= len(self.goob_walk):
                self.goob_index = 0
            self.image = self.goob_walk[int(self.goob_index)]

    def player_input(self):
        # only allow movement when available == 1
        if self.available == 1:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.animation_state("walk")
                self.x_pos -= 6
            elif keys[pygame.K_d]:
                self.animation_state("walk")
                self.x_pos += 6
            self.rect.x = self.x_pos

    def update(self):
        self.player_input()

def generate():
    container = ["an envelope", "a box", "a suitcase", "a chest"]
    types = ["money", "sweet","key"]
    name = container[randint(0,3)]
    type = types[randint(0,2)]
    if type == "money":
        value = 25 * randint(1, 15)
    else:
        value = randint(1,3)
    return Prize(name, type, value)

class Prize(): #Prize class with 3 variables and their getters
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

    def getName(self):
        return self.name
    
    def getType(self):
        return self.type

    def getValue(self):
        return self.value
    
    def present(self):
        message = ""
        if self.type =="money":
            message = "You got " + self.name + " with £" + str(self.value) + " in!"
        else:
            if self.value > 1:
                message = "You got " + self.name + " with " + str(self.value) + " " + self.type + "s in!"
            else: 
                message = "You got " + self.name + " with 1 " + self.type + " in!"
        return message



def day_events():
    days = []
    for i in range(0,99):
        events = [ ]




pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1' #called after pygame.init()
info = pygame.display.Info() #called before set_mode()
screen_width, screen_height = info.current_w, info.current_h #grabs screen width and height
screen = pygame.display.set_mode((screen_width, screen_height-50), pygame.RESIZABLE) #coords so must have another set of brackets around them to define them, then lets user change screen size after
pygame.display.set_caption('Game 2')

#game state vars
global game_active
game_active = False

global game_complete
game_complete = False

clock = pygame.time.Clock()
running = True
dt = 0


#must be under pygame.init()

#font:
text_font = pygame.font.Font('font/TenorSans-Regular.ttf', 50)

#intro:
title_surface = text_font.render("Game 2", False, "white").convert_alpha()
title_rect = title_surface.get_rect(center = (screen_width/2, (screen_height/2)-200))

#tutorial:
tutorial = False
tutorial_surface = pygame.Surface((int(screen_width/2), int(screen_height/2)))
tutorial_surface.fill("white")

#day:
global current_day
current_day = 0


#groups:
goob = pygame.sprite.GroupSingle()
goob.add(Goob(4))

#buttons:
objects = []

#trying to make a button class
class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=False, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': "#FF4D21",
            'hover' : "#EC6F6F",
            'pressed': '#C5FAAF',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = text_font.render(buttonText, True, 'white')
        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)

def myFunction():
    print('Button Pressed')

def startGameFunc():
    global game_active 
    game_active = True
    print('started game')
    return game_active

def tutorialFunc():
    global tutorial
    tutorial = True
    return tutorial

def incrementDayFunc():
    global current_day
    current_day += 1
    return current_day

def turn_off_movement():
    s = goob.sprite
    if s is None:       #got annoyed and put this into chat, will test and comment on this tomorrow
        return
    s.available = 0 if s.available == 1 else 1
    return s.available
    
#Button(30, 30, 400, 100, 'Button One (onePress)', myFunction)
#Button (30, 140, 400, 100, 'Button Two(multiPress)', myFunction, True) hold down the button for multiple inputs

Button(screen_width/2-(screen_width/10), screen_height/2-(screen_height/10), 400, 100, 'Start Game', startGameFunc)
Button(screen_width/2-(screen_width/10), screen_height/2, 400, 100, 'Read Tutorial', tutorialFunc)
Button(screen_width/2-(screen_width/10), screen_height/2+(screen_height/4), 400, 100, 'Keep Going!', incrementDayFunc) #press this and current day goes up
Button(screen_width/2-(screen_width/10), screen_height/2, 400, 100, 'Turn on/off movement', turn_off_movement)


while running:
    #player inputs will be here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    screen.fill("#AFEBFA")

    if game_complete == False and game_active == False:
        screen.blit(title_surface,title_rect)
        objects[0].process() #start Game button
        objects[1].process() #tutorial button
    
    if tutorial:
        screen.blit(tutorial_surface, (100, 100))

    if game_active:
        screen.fill("#AFEBFA") 
        year_surface = text_font.render("GOOB - Day "+ str(current_day), False, "black").convert_alpha()
        year_rect = year_surface.get_rect(center = (screen_width/2, (screen_height/2)-200))
        screen.blit(year_surface,year_rect)
        #Actual game goes in here
        
        objects[2].process() #next year button
        objects[3].process() #turn off movement button to test disabling player input
        goob.draw(screen)
        goob.update()

    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
