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

    def test_add_score(self):
        """Test to add score."""
        player1 = player.Player(1, "Kalle")
        res = player1.add_score(6)
        exp = player1.current_score
        self.assertEqual(exp, res)

    def test_get_score(self):
        """Test to get player's score."""
        player1 = player.Player(1, "Kalle")
        exp = player1.current_score
        res = player1.get_score()
        self.assertEqual(res, exp)

    def test_get_id(self):
        """Test to get the player's id."""
        player1 = player.Player(1, "Kalle")
        exp = player1.player_id
        res = player1.get_id()
        self.assertEqual(exp, res)
