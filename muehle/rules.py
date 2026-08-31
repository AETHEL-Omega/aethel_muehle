"""Placement, mills, movement.

No I/O, no network, no randomness. Illegal actions raise MuehleError.
"""
from muehle.board import COLORS, POINTS


class MuehleError(ValueError):
    """Fail-closed: the action is not legal in Mühle."""


def place(board, point, color):
    if point not in POINTS:
        raise MuehleError
    if color not in COLORS:
        raise MuehleError
    if board.get(point) is not None:
        raise MuehleError
    out = dict(board)
    out[point] = color
    return out
