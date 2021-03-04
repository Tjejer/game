"""
Lets play a game of "Pig".

Start the game by writing 'start'.
Roll the dice as many times you want by writing ‘roll’.
To hold and not roll another time, giving the turn to
the other player write ‘hold’.
"""

import shell


if __name__ == '__main__':
    print(__doc__)
    shell.Shell().cmdloop()
