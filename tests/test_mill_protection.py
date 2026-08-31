"""Job 4 — capture refuses a mill stone unless every opponent stone is in a mill."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from muehle.board import empty_board
from muehle.rules import MuehleError, capture, place


def _black_top_mill():
    board = empty_board()
    for point in ("a7", "d7", "g7"):
        board = place(board, point, "black")
    return board


class TestMillProtection(unittest.TestCase):
    def test_mill_stone_is_protected_while_a_free_stone_exists(self):
        board = place(_black_top_mill(), "a1", "black")
        with self.assertRaises(MuehleError):
            capture(board, "d7", "white")

    def test_free_stone_can_be_taken_beside_a_mill(self):
        board = place(_black_top_mill(), "a1", "black")
        out = capture(board, "a1", "white")
        self.assertIsNone(out["a1"])
        self.assertEqual(out["d7"], "black")

    def test_mill_stone_can_be_taken_when_all_opponent_stones_are_in_mills(self):
        board = _black_top_mill()
        out = capture(board, "d7", "white")
        self.assertIsNone(out["d7"])
        self.assertEqual(out["a7"], "black")

    def test_does_not_mutate_input(self):
        board = place(_black_top_mill(), "a1", "black")
        with self.assertRaises(MuehleError):
            capture(board, "d7", "white")
        self.assertEqual(board["d7"], "black")
        self.assertEqual(board["a1"], "black")


if __name__ == "__main__":
    unittest.main()
