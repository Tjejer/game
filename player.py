"""Class for player."""


class Player():
    """Player classing."""

    def __init__(self, player_id, name):
        """Player created."""
        self.player_id = int(player_id)
        self.name = name
        self.current_score = 0

    def change_name(self, new_name):
        """Change the players name."""
        self.name = new_name
        return self.name

    def get_name(self):
        """Reteveing the players name."""
        return self.name

    def add_score(self, score):
        """Add score to player current player's score."""
        self.current_score += score
        return self.current_score

    def get_score(self):
        """Get player's score."""
        return self.current_score

    def get_id(self):
        """Get player's id."""
        return self.player_id
