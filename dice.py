import random

class Dice:

    def __init__(self):
        pass

    def turn(self):
        self.dice_value = random.randint(1,6)
        return self.dice_value
        

    


