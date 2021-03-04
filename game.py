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

    def start_game(self, amount_of_players):
        """Start the game."""
        self.create_players(amount_of_players)
        self.player1, self.player2 = self.randomize_player(self.player1, self.player2)

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

    def randomize_player(self, x, y):
        """Randomize player."""
        current = random.randint(1 ,2)

        if current == 1:
            print("Player", x.get_name(), "will start the game.")
            return x, y
        else:
            print("Player", y.get_name(), "will start the game.")
            return y, x
