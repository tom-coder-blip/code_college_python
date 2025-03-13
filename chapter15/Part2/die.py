from random import randint

class Die:
    #A class representing a single die

    def __init__(self, num_sides=6):
        #Initialize a die with a given number of sides (default is 6)
        self.num_sides = num_sides

    def roll(self):
        #return a random value between 1 and the number of sides
        return randint(1, self.num_sides)
    
    