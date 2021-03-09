"""Class for dice."""

import random


class Dice():
    """Create class."""

    def __init__(self):
        """Initialize dice."""
        self.dice_value = None

    def turn(self):
        """Turn dice."""
        self.dice_value = random.randint(1, 6)
        return self.dice_value
