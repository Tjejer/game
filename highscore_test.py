"""Class for unittesting the highscore class."""

import unittest
import highscore
import os
# import player


class TestHighScoreClass(unittest.TestCase):
    """Unittesting the highscore class."""

    def test_get_score(self):
        h1 = highscore.Highscore("file_test.txt")
        h1.log_score(12, 1)
        res = h1.show_scores()
        exp = ['1:12', '']
        self.assertEqual(res, exp)
        os.remove("file_test.txt")
