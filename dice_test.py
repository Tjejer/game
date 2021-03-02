from src import dice
import unittest
import random

class TestDice_Class(unittest.testcase):
    def test_createdice(self):
        dice1 = dice.Dice()
        self.assertIsInstance(dice1, dice.Dice)

    def test_turn(self):
        dice1 = dice.Dice()
        dice_value = dice1.turn
        res = dice_value
        exp = [1, 2, 3, 4, 5, 6]
        self.assertIsIn(res, exp)

        
