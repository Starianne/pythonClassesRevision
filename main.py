import pygame
import os
from sys import exit
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #add player image.covert_alpha()
        player_idle_1 = pygame.image.load('graphics/player')
        #add player rect

def generate():
        container = ["an envelope", "a box", "a suitcase", "a chest"]
        types = ["money", "deed","idk something"]
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



def road_set(null_road): # sets 10 prizes randomly on the road set and gives the complete road back
    flag = True
    count = 10
    
    while flag == True:
        if count != 0:
            road_space = randint(0,49)
            if null_road[road_space] == 0:
                count -= 1
                null_road[road_space] = generate()
                print(road_space)
        else:
            flag = False
    return null_road

def display_road(road):
    for i in range(0,49):
        print(f"Space {i+1}")
        if road[i] == 0:
            print("empty")
        else:
            print(road[i].present())


road = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
game_road = road_set(road)
display_road(game_road)




allPrizes = [] #to store prizes to win





pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1' #called after pygame.init()
info = pygame.display.Info() #called before set_mode()
screen_width, screen_height = info.current_w, info.current_h #grabs screen width and height
screen = pygame.display.set_mode((screen_width, screen_height-50), pygame.RESIZABLE) #coords so must have another set of brackets around them to define them, then lets user change screen size after
pygame.display.set_caption('Runner')
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
title_surface = text_font.render("Game 2", False, "white").convert()
title_rect = title_surface.get_rect(center = (screen_width/2, (screen_height/2)-200))
#tutorial:
tutorial = False
tutorial_surface = pygame.Surface((int(screen_width/2), int(screen_height/2)))
tutorial_surface.fill("white")


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
#Button(30, 30, 400, 100, 'Button One (onePress)', myFunction)
#Button (30, 140, 400, 100, 'Button Two(multiPress)', myFunction, True) hold down the button for multiple inputs

Button(screen_width/2-(screen_width/10), screen_height/2, 400, 100, 'Start Game', startGameFunc)
Button(screen_width/2-(screen_width/10), screen_height/2-(screen_height/10), 400, 100, 'Read Tutorial', tutorialFunc)




while running == True:
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
        #Actual game goes in here
           
    






    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
