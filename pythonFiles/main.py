import pygame
import os
from sys import exit
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #add player image.covert_alpha()
        #add player rect

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
    
    

'''class Character():
    def __init__(self, name):
        self.name = name
        self.money = 5
        self.experience = 0
        self.roadPosition = 0
    
    def getName(self):
        return self.name
    
    def getMoney(self):
        return self.money
    
    def getExperience(self):
        return self.experience
    
    def getRoadPosition(self):
        return self.roadPosition
    
    def updateValues(self, type, value):
        if type == "money":
            self.money += value
        elif type == "experience":
            self.experience += value

    def changePosition(self, move):
        self.roadPosition += move

    '''

def road_set(null_road): # sets 10 prizes randomly on the road set and gives the complete road back
    flag = True
    count = 10
    
    while flag == True:
        if count != 0:
            road_space = randint(0,49)
            if null_road[road_space] == 0:
                count -= 1
                null_road[road_space] = Prize("Box", 'money', 25)
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
            print(road[i].getValue())


road = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
game_road = road_set(road)
display_road(game_road)

character1 = Character('Jamal')
new_position = 0
while new_position < 50:
    move = randint(1,4)
    character1.changePosition(move)
    new_position = character1.getRoadPosition()
    if new_position < 50 and game_road[new_position] != 0:
        prize_type = game_road[new_position].getType()
        value_amount = game_road[new_position].getValue()
        character1.updateValues(prize_type,value_amount)
        print(f"Congrats you are in position {new_position} and found {game_road[new_position].getName()}")
        print(f"Money = {character1.getMoney()} and experience = {character1.getExperience()}")
print(f"{character1.getName()} You have finished")


allPrizes = [] #to store prizes to win


pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1' #called after pygame.init()
info = pygame.display.Info() #called before set_mode()
screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height-50), pygame.RESIZABLE) #coords so must have another set of brackets around them to define them, then lets user change screen size after
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

while True:
    pygame.draw.rect(screen, 'red', [200,200,100,100])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)


