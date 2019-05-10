from src.connect_4 import ConnectFour

import unittest


class GameTestSuit(unittest.TestCase):
    """Test for connect 4 basic functionality"""

    def test_can_setup_board(self):
        connect4 = ConnectFour()
        self.assertEqual(connect4.board, [
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ']
        ])


if __name__ == '__main__':
    unittest.main()
