"""Class for dice."""


class DiceHand():
    """Dice hand class."""

    def __init__(self):
        """Dice hand created."""
        self.dice_list = []

    def add_score(self, dice_pt):
        """Add score."""
        self.dice_list.append(dice_pt)
        return self.dice_list
