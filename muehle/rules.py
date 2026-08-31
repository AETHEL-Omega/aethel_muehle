"""Placement, mills, movement.

No I/O, no network, no randomness. Illegal actions raise MuehleError.
"""
from muehle.board import COLORS, MILLS, POINTS


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


def forms_mill(board, point):
    color = board.get(point)
    if color is None:
        return False
    for mill in MILLS:
        if point in mill and all(board.get(p) == color for p in mill):
            return True
    return False
