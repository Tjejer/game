from src import dice

class Dice_hand:
    
    def __init__(self):
        """Dice hand created."""
        self.dice_list = []

    def add_score(self, dice_pt):
        self.dice_list.append(dice_pt)
        return self.dice_list


    

    