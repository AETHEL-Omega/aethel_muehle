"""Job 3 — capture: remove an opponent stone. Mill protection is Job 4."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from muehle.board import empty_board
from muehle.rules import MuehleError, capture, place


class TestCapture(unittest.TestCase):
    def test_removes_opponent_stone(self):
        board = place(empty_board(), "a1", "black")
        out = capture(board, "a1", "white")
        self.assertIsNone(out["a1"])

    def test_does_not_mutate_input(self):
        start = place(empty_board(), "d7", "black")
        capture(start, "d7", "white")
        self.assertEqual(start["d7"], "black")

    def test_empty_point_fails_closed(self):
        with self.assertRaises(MuehleError):
            capture(empty_board(), "a1", "white")

    def test_own_stone_fails_closed(self):
        board = place(empty_board(), "a1", "white")
        with self.assertRaises(MuehleError):
            capture(board, "a1", "white")

    def test_unknown_point_fails_closed(self):
        with self.assertRaises(MuehleError):
            capture(empty_board(), "z9", "white")

    def test_unknown_color_fails_closed(self):
        board = place(empty_board(), "a1", "black")
        with self.assertRaises(MuehleError):
            capture(board, "a1", "red")


if __name__ == "__main__":
    unittest.main()
