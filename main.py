"""
Welcome to the Pig game!
Rules:
 Win the game by being the first one to score at least 100 points.
You can repeatedly roll the dice as many times as you want.
If you roll a 1, you score nothing and it becomes your opponents turn.
If you roll anything but a 1, points will be added to your score. 
Choose if you want to roll the dice again or end your round by typing "roll" or "hold".
Type "start" to start the game.

If you want to see highscores from previous games, type "highscores".

Type "rules" to see the rules again.
Type "change_name" to change your name during your turn, followed by your new name.
Type "restart" to restart the game.
Type "cheat" if you want to be a cheater and win the game.
Type "quit" to quit the game.
"""

import shell


if __name__ == '__main__':
    print(__doc__)
    shell.Shell().cmdloop()
