import unittest
import random
from main import play
from main import winner


class TestWin(unittest.TestCase):
    def test_winner(self):
        # test outcome if player beats opponet.
        self.assertTrue(winner("p", "r"))
        self.assertTrue(winner("s", "p"))
        self.assertTrue(winner("r", "s"))
