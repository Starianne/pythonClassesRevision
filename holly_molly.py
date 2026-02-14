from text_box import Textbox
import pygame

Holly = None
Holly_rect = None
Molly = None
Molly_rect = None
user = None
#event structure:
choice = [["Winter", "Summer"]]
event_dialogue = None

def holly_molly_event():
    global Holly, Holly_rect, Molly, Molly_rect, event_dialogue
    from main import screen, screen_width, screen_height, next_box #imports inside function to not have circular imports
    
    #now define all variables
    Holly = pygame.Surface((int(screen_width/16), int(screen_height/8)))
    Holly.fill("green")
    Holly_rect = Holly.get_rect()
    Molly = pygame.Surface((int(screen_width/16), int(screen_height/8)))
    Molly.fill("red")
    Molly_rect = Molly.get_rect()
    
    event_dialogue = [[Holly, "Hey, weird red thing"], [Molly, "Yeah, you come here"], [Holly, "which season is better"], [user, choice[0]]]
    
    i = 0
    for dialogue in event_dialogue[i][1]:
        surface_rect = event_dialogue[i][0].get_rect()
        screen.blit(event_dialogue[i][0], surface_rect)
        next_box(dialogue)
