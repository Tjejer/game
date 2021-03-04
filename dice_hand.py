"""Class for dice."""


class DiceHand():
    """Dice hand class."""
    dice_list = None

    def __init__(self):
        """Dice hand created."""
        self.dice_list = []

    def add_score(self, dice_pt):
        """Add score."""
        self.dice_list.append(dice_pt)
        return self.dice_list

    def empty_score(self):
        """Empty score list."""
        self.dice_list = []

    def get_score(self):
        score = sum(self.dice_list)
        return score
