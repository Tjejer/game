
import random

class Dice():
    dice_value = None

    def __init__(self):
        self.dice_value = None

    def turn(self):
        self.dice_value = random.randint(1,6)
        return self.dice_value
