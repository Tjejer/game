"""Class for unittest of dice class."""

import unittest
import dice


class TestDiceClass(unittest.TestCase):
    """Test for dice class."""

    def test_createdice(self):
        """Test to create a dice."""
        dice1 = dice.Dice()
        self.assertIsInstance(dice1, dice.Dice)

    def test_turn(self):
        """Test to turn dice."""
        dice1 = dice.Dice()
        res = dice1.turn()
        exp = [1, 2, 3, 4, 5, 6]
        self.assertIn(res, exp)
