import random

class Die():
    ### define a dice for any board game ###
    ### simply call the dice with a number and this is the number of side ###


    def __init__(self, sides=6):
        #super(ClassName, self).__init__()
        self.sides = sides

    def roll(self):
        return random.randint(1,self.sides)

num_sides = int(input("define dice"))
gamble = Die(num_sides)
print(gamble.roll())