class Prize():
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
    
A = Prize("Annelies","name",40)

print(A.name)
print(A)