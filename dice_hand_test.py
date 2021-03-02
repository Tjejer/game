from src import dice_hand
import unittest

class TestDice_handClass(unittest.testcase):
    def test_createdicehand(self):
        dice_hand1 = dice_hand.Dice_hand()
        self.assertIsInstance(dice_hand1, dice_hand.Dice_hand)

    def test_addscore(self):
        dice_hand2 = dice_hand.Dice_hand()
        my_list = dice_hand2.add_score(5)
        res = my_list[0]
        exp = 5
        self.assertEqual(res, exp)


