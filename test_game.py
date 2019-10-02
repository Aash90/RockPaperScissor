import unittest
from game import Game


class TestGameScore(unittest.TestCase):

    def setUp(self):
        self.g = Game('P1', 'P2')

        self.g.score = {self.g.player1: 2, self.g.player2: 3}

    def test_get_game_score(self):

        (player1_name, player1_score,player2_name, player2_score) = self.g.get_game_score()
        self.assertEqual(player1_score, 2)
        self.assertEqual(player2_score, 3)


class TestGameWinner(unittest.TestCase):

    def setUp(self):
        self.g = Game('P1', 'P2')

        self.g.player1.throw = 'Rock'
        self.g.player2.throw = 'Scissor'

    def test_get_winner(self):

        winner = self.g.get_winner()

        self.assertEqual(self.g.player1, winner)



if __name__ == '__main__':
    unittest.main()

