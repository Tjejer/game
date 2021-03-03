import dice
import unittest
import random

class TestDice_Class(unittest.TestCase):
    def test_createdice(self):
        dice1 = dice.Dice()
        self.assertIsInstance(dice1, dice.Dice)

    def test_turn(self):
        dice1 = dice.Dice()
        res = dice1.turn()
        exp = [1, 2, 3, 4, 5, 6]
        self.assertIn(res, exp)
