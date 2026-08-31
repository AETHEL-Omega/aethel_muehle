"""Job 1 — must start RED. place() does not exist yet."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from muehle.board import empty_board
from muehle.rules import MuehleError, place


class TestPlace(unittest.TestCase):
    def test_place_on_empty_point(self):
        board = place(empty_board(), "a1", "white")
        self.assertEqual(board["a1"], "white")
        self.assertIsNone(board["g7"])

    def test_place_does_not_mutate_input(self):
        start = empty_board()
        place(start, "d7", "black")
        self.assertIsNone(start["d7"])

    def test_occupied_point_fails_closed(self):
        board = place(empty_board(), "a1", "white")
        with self.assertRaises(MuehleError):
            place(board, "a1", "black")

    def test_unknown_point_fails_closed(self):
        with self.assertRaises(MuehleError):
            place(empty_board(), "z9", "white")

    def test_unknown_color_fails_closed(self):
        with self.assertRaises(MuehleError):
            place(empty_board(), "a1", "red")


if __name__ == "__main__":
    unittest.main()
