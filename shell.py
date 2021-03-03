"""Using the cmd module to create a shell for the main program.

You can read about the cmd module in the docs:
    cmd — support for line-oriented command interpreters
    https://docs.python.org/3/library/cmd.html
"""

import cmd
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
        amount_of_players = int(input("Enter 1 for Player vs. AI or enter 2 for Player vs Player."))
        self.game.create_players(amount_of_players)

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