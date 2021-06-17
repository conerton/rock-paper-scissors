import unittest
import random
from main import play
from main import winner

user = input(
    "What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()

computer = random.choice(['r', 'p', 's'])


class TestWin(unittest.TestCase):
    def test_winner(self):
        # test outcome if player beats opponet.
        self.assertTrue(winner("p", "r"))
        self.assertTrue(winner("s", "p"))
        self.assertTrue(winner("r", "s"))
