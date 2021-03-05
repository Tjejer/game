"""Unittest class for dice_hand class."""
import unittest
import dice_hand


class TestDiceHandClass(unittest.TestCase):
    """Test class for dice_hand."""

    def test_createdicehand(self):
        """Test if dice hand is created."""
        dice_hand1 = dice_hand.DiceHand()
        self.assertIsInstance(dice_hand1, dice_hand.DiceHand)

    def test_addscore(self):
        """Test to add a score."""
        dice_hand2 = dice_hand.DiceHand()
        my_list = dice_hand2.add_score(5)
        res = my_list[0]
        exp = 5
        self.assertEqual(res, exp)

    def test_empty_score(self):
        """Test emptying the list."""
        dice_hand1 = dice_hand.DiceHand()
        exp = []
        res = dice_hand1.empty_score()
        self.assertEqual(exp, res)

    def test_get_score(self):
        """Test getting the score."""
        dice_hand1 = dice_hand.DiceHand()
        dice_hand1.dice_list = [2, 1]
        exp = 3
        res = dice_hand1.get_score()
        self.assertEqual(exp, res)
