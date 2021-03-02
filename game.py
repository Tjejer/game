"""Pig game."""

import random
import os
import highscore


class Game():
    """The game class."""

    def __init__(self):
        """Init the object."""
        random.seed()

    def show_scores(self):
        """Show scores to the player."""
        self.log_score1(12, 6)
        high = highscore.Highscore("file.txt")
        highscores = high.get_scores()
        high.sort_scores(highscores)
        highscores = high.get_scores()
        return highscores

    def log_score1(self, score, player_id):
        """Log scores into the file."""
        high = highscore.Highscore("file.txt")
        high.log_score(score, player_id)

    def empty_highscores(self):
        """Empty all highscores info."""
        os.remove("file.txt")
