import pygame
import spritesheet #wait
from goobs import *
from text_box import Textbox
import os
from sys import exit
from random import randint
from holly_molly import holly_molly_event

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


#removed the textbox stuff to put be organised by its own class so i dont have the circular imports anymore       

#probably will change what i do with this later
def day_events():
    days = []
    for i in range(0,99):
        events = [ ]




pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1' #called after pygame.init()
info = pygame.display.Info() #called before set_mode()
screen_width, screen_height = info.current_w, info.current_h #grabs screen width and height
global screen
screen = pygame.display.set_mode((screen_width, screen_height)) #coords so must have another set of brackets around them to define them
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
global text_font
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
#player sprite group
goob = pygame.sprite.GroupSingle()
goob.add(Goob(4))


#buttons:
objects = []

#since I only have a few buttons rn im not sure whether i move this yet

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

#movement toggles
def toggle_horizontal_movement():
    s = goob.sprite
    if s is None:       
        return
    s.horizontal_available = 0 if s.horizontal_available == 1 else 1 #ternary/conditional expression did not know this was a thing in python too
    return s.horizontal_available

def toggle_vertical_movement():
    z = goob.sprite
    if z is None:       
        return
    z.vertical_available = 0 if z.vertical_available == 1 else 1 #ternary/conditional expression did not know this was a thing in python too
    return z.vertical_available

def toggle_all_movement():
    toggle_horizontal_movement()
    toggle_vertical_movement()


#events--------------------------------------------------------------------

global events
events = ["birch", "thief", "pebble_art", "core_apple", "birds_eye", "holly_molly", "cratin", "sea_saw", "meowntain", "velcrows", "dont_mention_it"]

def decide_event():
    events_length = len(events) - 1
    selected = randint(0, events_length)
    match selected:
        case 0 :
            return birch_event()

#birch event

def birch_event():
    screen.fill("#AFEBFA")
    birch_surface = pygame.Surface((int(screen_width/16), int(screen_height/8)))
    birch_surface.fill("green")
    screen.blit(birch_surface, (screen_width/6,screen_height/2))
    
#-----------------------------------------------------------------------------------

def incrementDayFunc():
    global current_day
    current_day += 1
    toggle_all_movement()
    decide_event()
    return current_day

birch_text = ["Goob do you like my hat?", "I can't take it off", "My branch dresser sneezed"] #test data
    
#Button(30, 30, 400, 100, 'Button One (onePress)', myFunction)
#Button (30, 140, 400, 100, 'Button Two(multiPress)', myFunction, True) hold down the button for multiple inputs

Button(screen_width/2-(screen_width/10), screen_height/2-(screen_height/10), 400, 100, 'Start Game', startGameFunc)
Button(screen_width/2-(screen_width/10), screen_height/2, 400, 100, 'Read Tutorial', tutorialFunc)
Button(screen_width/2-(screen_width/10), screen_height/2+(screen_height/4), 400, 100, 'Keep Going!', incrementDayFunc) #press this and current day goes up
 #temp for testing



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
       #next year button needs to call branch of events 
      
        year_surface = text_font.render("GOOB - Day "+ str(current_day), False, "black").convert_alpha()
        year_rect = year_surface.get_rect(center = (screen_width/2, (screen_height/2)-200))
        screen.blit(year_surface,year_rect)
        #Actual game goes in here
        objects[2].process() 
        goob.draw(screen)
        goob.update()

    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
