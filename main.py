import pygame
from goobs import *
from text_box import Textbox
import os
from sys import exit
from random import randint
from gamestate import GameState
from button import Button
from holly_molly import holly_molly_event

game_state = GameState()
current_event = None

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

#i reallyyyyy dont want to move ts i have to noooooooooooooooooooo


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
global game_started
game_started = False

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

#end
end_surface = text_font.render("Game 2 is over, well done!", False, "white").convert_alpha()
end_rect = title_surface.get_rect(center = (screen_width/2, (screen_height/2)-200))

#day:
global current_day
current_day = 0


#groups: 
#player sprite group
goob = pygame.sprite.GroupSingle()
goob.add(Goob(4, game_state))


#buttons:
objects = []

#since I only have a few buttons rn im not sure whether i move this yet

def start_game_func():
    global game_started 
    game_started = True
    print('started game') #to check in terminal remove later
    make_game_active_func()
    return game_started

def make_game_active_func():
    global game_active
    game_active = True
    print('active game') #same as started game
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
#uhhhh I'll fix this later
global events
events = ["birch", "thief", "pebble_art", "core_apple", "birds_eye", "holly_molly", "cratin", "sea_saw", "meowntain", "velcrows", "dont_mention_it"]

def decide_event():
    global current_event # setting this to holly molly event to test for now
    current_event = holly_molly_event(game_state, text_font, (screen_width, screen_height))


#-----------------------------------------------------------------------------------

def increment_day_func():
    global current_day
    current_day += 1
    toggle_all_movement()
    decide_event()
    return current_day

def pause_unpause_game_func():
    global game_active
    game_active = False if game_active == True else True
    return game_active

Button(screen_width/2-(screen_width/10), screen_height/2-(screen_height/10), 400, 100, 'Start Game', start_game_func, text_font, screen)
Button(screen_width/2-(screen_width/10), screen_height/2, 400, 100, 'Read Tutorial', tutorialFunc, text_font, screen)
Button(screen_width/2-(screen_width/10), screen_height/2+(screen_height/4), 400, 100, 'Keep Going!', increment_day_func, text_font, screen) #press this and current day goes up 
 #temp for testing



while running:
    #player inputs will be here
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p: #pauses game mostly except game dialogue but thats bc it just blits ontop of screen that jus changes color when you 'pause'
            pause_unpause_game_func()

    
    screen.fill("#AFEBFA")

    if game_started == False:
        screen.blit(title_surface,title_rect)
        objects[0].process() #start Game button
        objects[1].process() #tutorial button
    
        if tutorial:
            screen.blit(tutorial_surface, (100, 100))

    else:
        if game_active:
            if not current_event:
                screen.fill("#AFEBFA")
                #next year button needs to call branch of events 
                year_surface = text_font.render("GOOB - Day "+ str(current_day), False, "black").convert_alpha()
                year_rect = year_surface.get_rect(center = (screen_width/2, (screen_height/2)-200))
                screen.blit(year_surface,year_rect)
                #Actual game goes in here
                objects[2].process() 

                goob.draw(screen)
                goob.update() 

        else:
            screen.fill("blue")       

    if current_event:
        if not current_event.started:
            toggle_all_movement()
            current_event.start()

        current_event.handle_input(events)
        current_event.update()
        current_event.draw(screen)

        if current_event.done:
            current_event = None
            toggle_all_movement()




    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
