"""Pig game."""

import random
import highscore


class Game():
    """The game class."""

    def __init__(self):
        """Init the object."""
        random.seed()

    def show_scores(self):
        h = highscore.Highscore("file.txt")
        highscores = h.get_scores()
        return highscores
    
    def log_score(self, score, player_id):
        h = highscore.Highscore("file.txt")
        h.log_score(score, player_id)