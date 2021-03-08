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

    def do_cheat(self):
        """Cheat and finish the game. Nothing will be scored nor highscored."""
        if self.game.game_running:
            print('You chose to cheat. This is unacceptable!\
    You will not have your highscore displayed in the highscores.')
            self.game.end_game()
        else:
            self.game.error_info()

    def do_reset_highscores(self, _):
        """Empty whole highscore file."""
        self.game.empty_highscores()

    def do_rules(self, _):
        """Show the rules."""
        print("\nRules:\
\nWin the game by being the first one to score at least 100 points.\
\nYou can repeatedly roll the dice as many times as you want.\
\nIf you roll a 1, you score nothing and it becomes your opponents turn.\
\nIf you roll anything but a 1, points will be added to your score. \
\nChoose if you want to roll the dice again or end your round by typing\
'roll' or 'hold'.\
\nType 'start' to start the game.\n\
\nIf you want to see highscores from previous games, type 'highscores'.\
\nType 'rules' to see the rules again.\
\nType 'change_name' to change your name during your turn, followed by your\
new name.\
\nType 'restart' to restart the game.\
\nType 'cheat' if you want to be a cheater and win the game.\
\nType 'quit' to quit the game.")

    def do_change_name(self, new_name):
        """Change current players name."""
        if self.game.game_running:
            msg = self.game.change_name(new_name)
            print(msg)
        else:
            self.game.error_info()

    def do_roll(self, _):
        """Roll the dice."""
        if self.game.game_running:
            self.game.roll_dice()
        else:
            self.game.error_info()

    def do_hold(self, _):
        """Change turns, save score."""
        if self.game.game_running:
            self.game.hold_turn()
        else:
            self.game.error_info()

    def do_quit(self, _):
        """Quit game."""
        sys.exit()

    def do_restart(self, _):
        """Restart the game."""
        self.game.end_game()
        self.do_start(_)
