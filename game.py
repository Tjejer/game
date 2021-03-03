"""Pig game."""

import random
import os
import highscore
import player


class Game():
    """The game class."""
    player1 = None
    player2 = None

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
    
    def create_players(self, amount_of_players):
        """Creating the players for the game."""
        if amount_of_players == 1:
            player1_name = str(input("Enter name for player 1: "))
            player1_id = int(input("Enter id for player 1: "))

            self.player1 = player.Player(player1_id, player1_name)
            self.player2 = player.Player(666, "AI")
        else:
            player1_name = str(input("Enter name for player 1: "))
            player1_id = int(input("Enter id for player 1: "))

            player2_name = str(input("Enter name for player 2: "))
            player2_id = int(input("Enter id for player 2: "))

            self.player1 = player.Player(player1_id, player1_name)
            self.player2 = player.Player(player2_id, player2_name)
