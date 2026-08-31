"""Job 2 — forms_mill: stone on point is in a completed mill of its color."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from muehle.board import empty_board
from muehle.rules import forms_mill, place


class TestFormsMill(unittest.TestCase):
    def test_top_row_mill(self):
        board = empty_board()
        for point in ("a7", "d7", "g7"):
            board = place(board, point, "white")
        self.assertTrue(forms_mill(board, "a7"))
        self.assertTrue(forms_mill(board, "d7"))
        self.assertTrue(forms_mill(board, "g7"))
        self.assertFalse(forms_mill(board, "a1"))

    def test_two_stones_are_not_a_mill(self):
        board = place(empty_board(), "a7", "white")
        board = place(board, "d7", "white")
        self.assertFalse(forms_mill(board, "a7"))
        self.assertFalse(forms_mill(board, "d7"))
        self.assertFalse(forms_mill(board, "g7"))

    def test_mixed_colors_are_not_a_mill(self):
        board = place(empty_board(), "a7", "white")
        board = place(board, "d7", "white")
        board = place(board, "g7", "black")
        self.assertFalse(forms_mill(board, "a7"))
        self.assertFalse(forms_mill(board, "g7"))

    def test_empty_point_is_not_a_mill(self):
        self.assertFalse(forms_mill(empty_board(), "d7"))

    def test_vertical_mill(self):
        board = empty_board()
        for point in ("a7", "a4", "a1"):
            board = place(board, point, "black")
        self.assertTrue(forms_mill(board, "a4"))
        self.assertFalse(forms_mill(board, "d7"))

    def test_does_not_mutate_input(self):
        start = place(empty_board(), "a7", "white")
        forms_mill(start, "a7")
        self.assertEqual(start["a7"], "white")
        self.assertIsNone(start["d7"])


if __name__ == "__main__":
    unittest.main()
