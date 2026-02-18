import pygame
from goobs import *
from text_box import Textbox
import os
from random import randint
from gamestate import GameState
from button import Button
from event_manager import EventManager
from holly_molly import holly_molly_event

game_state = GameState()

event_manager = EventManager()

start_buttons = []
game_buttons = []
event_buttons = []


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

#maingame:
main_surface = pygame.image.load('graphics/backgrounds/goobs_city.png').convert()
main_surface = pygame.transform.scale(main_surface, (3*screen_width/5, 3*screen_height/5))
main_rect = main_surface.get_rect(center = (2*screen_width/3, 2*screen_height/5))

#terminal:
terminal_surface = pygame.Surface((int(2*screen_width/7), int(5*screen_height/7)))
terminal_surface.fill("#AFEBFA")
terminal_rect = terminal_surface.get_rect(topleft = (screen_width/20, screen_height/10))

#make function for text in terminal:
def make_terminal(screen, game_state, font, rect):
    padding = screen_height/45
    y = rect.top + padding

    pygame.draw.rect(screen, "#AFEBFA", rect)

    title = font.render("Terminal:", True, "black")
    screen.blit(title, (rect.left + padding, y))
    y += screen_height/20

    for log in game_state.event_log:
        log_surf = font.render(log, True, "black")
        screen.blit(log_surf, (rect.left + padding, y))
        y += screen_height/25

    stats = [
        f"Money: £{game_state.money}",
        f"Sweets: {game_state.sweets}",
        f"Hats: {game_state.hats}",
    ]
    stats_y = rect.bottom - screen_height/5

    for stat in stats:
        stat_surf = font.render(stat, True, "black")
        screen.blit(stat_surf, (rect.left + padding, stats_y))
        stats_y += screen_height/20


#end
end_surface = text_font.render("Game 2 is over, well done!", False, "white").convert_alpha()
end_rect = title_surface.get_rect(center = (screen_width/2, (screen_height/2)-200))

#day:
global current_day
current_day = 0


#groups: 
#player sprite group
goob = pygame.sprite.GroupSingle()
goob.add(Goob(4, game_state, 2*screen_width/3, 2*screen_height/5 + screen_height/30))

def start_game_func():
    global game_started 
    game_started = True
    print('started game') #to check in terminal remove later
    make_game_active_func()
    toggle_all_movement()
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
    event_manager.start_event(holly_molly_event(game_state, text_font, (screen_width, screen_height), screen))


#-----------------------------------------------------------------------------------

def increment_day_func():
    global current_day
    current_day += 1
    decide_event()
    return current_day

def pause_unpause_game_func():
    global game_active
    game_active = False if game_active == True else True
    return game_active

start_buttons.append(Button(7*screen_width/18, screen_height/2-(screen_height/10), 400, 100, text_font, start_game_func, 'Start Game', screen))
start_buttons.append(Button(7*screen_width/18, screen_height/2, 400, 100, text_font, tutorialFunc, 'Read Tutorial', screen))
game_buttons.append(Button(7*screen_width/18, screen_height/2+(screen_height/4), 400, 100, text_font, increment_day_func, 'Keep Going!', screen)) #press this and current day goes up 

#game loop -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

while running:
    #player inputs will be here
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill("#4595DF")

    if game_started == False:
        screen.blit(title_surface,title_rect)
        for btn in start_buttons:
            btn.process()
    
        if tutorial:
            screen.blit(tutorial_surface, (100, 100))
     
    elif event_manager.is_active():
        event_manager.update(events, screen)


    elif game_active:
            goob.sprite.control_mode = "idle"
            day_surface = text_font.render("GOOB - Day "+ str(current_day), False, "white").convert_alpha()
            day_rect = day_surface.get_rect(center = (screen_width/2, screen_height/16))
            screen.blit(day_surface,day_rect)
            screen.blit(main_surface, main_rect)
            make_terminal(screen, game_state, text_font, terminal_rect)
            #Actual game goes in here
            game_buttons[0].process() 

            goob.draw(screen)
            goob.update()          

    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
