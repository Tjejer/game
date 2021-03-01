"""Class for unittesting the player class."""

import unittest
import player


class TestPlayerClass(unittest.TestCase):
    """Unittesting the player class."""

    def test_constructor(self):
        """Setting name and id."""
        player1 = player.Player(1, "Kalle")
        name1 = player1.name
        id1 = player1.player_id
        self.assertEqual(id1, 1)
        self.assertEqual(name1, "Kalle")

    def test_change_name(self):
        """Testing to change the players name."""
        player1 = player.Player(1, "Kalle")
        player1.change_name("Kalele")
        self.assertEqual(player1.name, "Kalele")

    def test_get_name(self):
        """Testing retreveing the name of the player."""
        player1 = player.Player(1, "Kalle")
        exp = player1.name
        res = player1.get_name()
        self.assertEqual(exp, res)
