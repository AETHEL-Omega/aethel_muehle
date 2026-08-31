"""Board graph is the seed. These tests must stay green while rules grow."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from muehle.board import MILLS, NEIGHBORS, POINTS, empty_board


class TestBoard(unittest.TestCase):
    def test_twenty_four_points(self):
        self.assertEqual(len(POINTS), 24)
        self.assertEqual(len(set(POINTS)), 24)

    def test_every_point_has_neighbors_on_the_board(self):
        for point, neighbors in NEIGHBORS.items():
            self.assertIn(point, POINTS)
            self.assertGreaterEqual(len(neighbors), 2)
            for other in neighbors:
                self.assertIn(point, NEIGHBORS[other])

    def test_sixteen_mills_of_three(self):
        self.assertEqual(len(MILLS), 16)
        for mill in MILLS:
            self.assertEqual(len(mill), 3)
            self.assertTrue(mill.issubset(POINTS))

    def test_empty_board_has_no_stones(self):
        board = empty_board()
        self.assertEqual(set(board), set(POINTS))
        self.assertTrue(all(stone is None for stone in board.values()))


if __name__ == "__main__":
    unittest.main()
