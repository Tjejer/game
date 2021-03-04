"""Pig game."""

import random
import os
import highscore
import player
import dice
import dice_hand


class Game():
    """The game class."""

    player1 = None
    player2 = None
    current_player = None
    dicerino = None
    dicerino_hand = None

    def __init__(self):
        """Init the object."""
        random.seed()

    def roll_dice(self):
        """Roll the dice."""
        value = self.dicerino.turn()
        if value != 1:
            self.dicerino_hand.add_score(value)
            return value
        elif value == 1:
            self.dicerino_hand.empty_score()
            return value

    def end_turn(self):
        """Ends the player's turn."""
        score = self.dicerino_hand.get_score()
        self.current_player.add_score(score)
        self.change_turn()

    def start_game(self, amount_of_players):
        """Start the game. Randomize first player. Set it to current player."""
        self.dicerino = dice.Dice()
        self.dicerino_hand = dice_hand.DiceHand()
        self.create_players(amount_of_players)
        self.player1, self.player2 = \
            self.randomize_player(self.player1, self.player2)
        self.current_player = self.player1

    def change_turn(self):
        """Change turns."""
        if self.current_player == self.player1:
            self.current_player = self.player2
        elif self.current_player == self.player2:
            self.current_player = self.player1

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
        """Create the players for the game."""
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

    def randomize_player(self, player1, player2):
        """Randomize player."""
        current = random.randint(1, 2)

        if current == 1:
            print("Player", player1.get_name(), "will start the game.")
            return player1, player2
        else:
            print("Player", player2.get_name(), "will start the game.")
            return player2, player1

    def change_name(self, new_name):
        """Change the current players name."""
        self.current_player.change_name(new_name)
        return f'Your name has been changed to {new_name}'
