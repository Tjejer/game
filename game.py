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
    highscores = highscore.Highscore("file.txt")
    game_running = False

    def __init__(self):
        """Init the object."""
        random.seed()

    def error_info(self):
        """Execute when player needs to start the game first\
 to run the command."""
        print('Start the game before writing this command.')

    def end_game(self):
        """End the game."""
        self.game_running = False
        self.player1 = None
        self.player2 = None
        self.current_player = None
        self.dicerino = None
        self.dicerino_hand = None
        self.game_running = False
        print('End of the game.')
        print('Start the game again by writing "start"')

    def game_won(self):
        """When the player has scored 100 points they win."""
        total_score = self.current_player.get_score() +\
            self.dicerino_hand.get_score()
        winner_name = self.current_player.get_name()
        print(f'Congratz {winner_name}!\
             You won the game with {total_score} points.')
        self.log_scores(total_score, self.current_player.get_id())
        self.end_game()

    def roll_dice(self):
        """Roll the dice."""
        value = self.dicerino.turn()
        if value != 1:
            self.dicerino_hand.add_score(value)
        elif value == 1:
            self.dicerino_hand.empty_score()
        return value

    def hold_turn(self):
        """End the player's turn."""
        score = self.dicerino_hand.get_score()
        self.current_player.add_score(score)
        self.change_turn()

    def start_game(self, amount_of_players):
        """Start the game. Randomize first player. Set it to current player."""
        self.game_running = True
        self.dicerino = dice.Dice()
        self.dicerino_hand = dice_hand.DiceHand()
        self.create_players(amount_of_players)
        self.player1, self.player2 = \
            self.randomize_player(self.player1, self.player2)
        self.current_player = self.player1

    def change_turn(self):
        """Change turns."""
        current_score = self.current_player.get_score()
        print(f'Your score is now {current_score}.')
        if self.current_player == self.player1:
            self.current_player = self.player2
            self.dicerino_hand.empty_score()
            print(f'Now it is {self.player2.get_name()} turn')
        elif self.current_player == self.player2:
            self.current_player = self.player1
            self.dicerino_hand.empty_score()
            print(f'Now it is {self.player1.get_name()} turn')

    def show_scores(self):
        """Show scores to the player."""
        highscore_list = self.highscores.get_scores()
        self.highscores.sort_scores(highscore_list)
        highscore_list = self.highscores.get_scores()
        return highscore_list

    def log_scores(self, score, player_id):
        """Log scores into the file."""
        self.highscores.log_score(score, player_id)

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
