"""Using the cmd module to create a shell for the main program.

You can read about the cmd module in the docs:
    cmd — support for line-oriented command interpreters
    https://docs.python.org/3/library/cmd.html
"""

import cmd
import game


class Shell(cmd.Cmd):
    """Command actions to pig game."""

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = game.Game()
    
    def highscores(self):
        self.game.show_scores()
