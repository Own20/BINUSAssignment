from random import randint

class Dice:
    def __init__(self, numSides=6):
        self.numSides = numSides
    
    def roll(self):
        return randint(1, self.numSides)