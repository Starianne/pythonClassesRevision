from random import randint

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
    
    '''def __str__(self):
        return f"{self.name} has {self.value}"'''
    
allPrizes = [] #to store prizes to win


A = Prize("Annelies","name",40)
def road_set(): # sets 10 prizes randomly on the road set and gives the complete road back
    road = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    count = 10
    flag = True
    while flag == True:
        if count != 0:
            road_space = randint(0,49)
            if road[road_space] == 0:
                count = count - 1
                road[road_space] = Prize("Box", 'money', 25)
                print(road_space)
        else:
            flag = False
    return road

la = road_set()
print(la)
