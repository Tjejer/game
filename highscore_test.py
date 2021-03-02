"""Class for unittesting the highscore class."""

import unittest
import os
import highscore

# import player


class TestHighScoreClass(unittest.TestCase):
    """Unittesting the highscore class."""

    def test_get_scores(self):
        """Test get the highscores."""
        high = highscore.Highscore("file_test.txt")
        high.log_score(12, 1)
        res = high.get_scores()
        exp = ['12:1']
        self.assertEqual(res, exp)
        os.remove("file_test.txt")

    def test_sort_scores(self):
        """Test sorting the scores."""
        high = highscore.Highscore("file_test.txt")
        test_list = ['12:1', '1:2']
        res = high.sort_scores(test_list)
        exp = ['1:2', '12:1']
        self.assertEqual(res, exp)
        os.remove("file_test.txt")
