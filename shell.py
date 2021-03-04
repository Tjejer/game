"""Using the cmd module to create a shell for the main program.

You can read about the cmd module in the docs:
    cmd — support for line-oriented command interpreters
    https://docs.python.org/3/library/cmd.html
"""

import cmd
import sys
import game


class Shell(cmd.Cmd):
    """Command actions to pig game."""

    game = None

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = game.Game()

    def do_start(self, _):
        """Start the game."""
        amount_of_players = int(input("Enter 1 for Player vs. AI \
or enter 2 for Player vs Player."))
        self.game.start_game(amount_of_players)

    def do_highscores(self, _):
        """Show highscores to the player."""
        lines = self.game.show_scores()
        print(lines)
        for line in lines:
            score, player_id = line.split(':')
            print(f'Score: {score}, Player_id {player_id}')

    def do_log_score(self, score, player_id):
        """Log score for player."""
        self.game.log_score1(score, player_id)

    def do_reset_highscores(self):
        """Empty whole highscore file."""
        self.game.empty_highscores()

    def do_rules(self):
        """Show the rules."""
        print("Start the game by writing 'start'.\
            Roll the dice as many times you want by writing ‘roll’.\
            To hold and not roll another time, giving the turn to\
            the other player write ‘hold’.")

    def do_change_name(self, new_name):
        """Change current players name."""
        msg = self.game.change_name(new_name)
        print(msg)

    def do_roll(self):
        """Roll the dice."""
        value = self.game.roll_dice()
        if value == 1:
            print(f'You rolled a 1, You scored nothing.')
            self.game.change_turn()
        elif value != 1:
            print(f'You rolled a {value}')

    def do_hold(self):
        """Change turns, save score."""
        self.game.end_turn()

    def do_quit(self):
        """Quit game."""
        sys.exit()
