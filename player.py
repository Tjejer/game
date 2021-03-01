"""Class for player."""


class Player():
    """Player classing."""

    player_id = None
    name = None

    def __init__(self, player_id, name):
        """Player created."""
        self.player_id = int(player_id)
        self.name = name

    def change_name(self, new_name):
        """Changin the players name."""
        self.name = new_name
        return self.name

    def get_name(self):
        """Reteveing the players name."""
        return self.name
