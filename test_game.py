import unittest
from game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_start_game(self):
        self.game.start_game()
        self.assertIsNotNone(self.game.start_time)
        self.assertIsNotNone(self.game.untyped_text)


if __name__ == '__main__':
    unittest.main()