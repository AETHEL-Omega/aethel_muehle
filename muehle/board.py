"""Nine Men's Morris (Mühle) — 24 points on three squares.

Coordinates are algebraic, same as the German board: a-file left, 1-rank bottom.
No diagonals. Stones move only along the mill lines in NEIGHBORS.
"""

from __future__ import annotations

Color = str | None

POINTS: tuple[str, ...] = (
    "a7", "d7", "g7",
    "b6", "d6", "f6",
    "c5", "d5", "e5",
    "a4", "b4", "c4", "e4", "f4", "g4",
    "c3", "d3", "e3",
    "b2", "d2", "f2",
    "a1", "d1", "g1",
)

NEIGHBORS: dict[str, frozenset[str]] = {
    "a7": frozenset({"d7", "a4"}),
    "d7": frozenset({"a7", "g7", "d6"}),
    "g7": frozenset({"d7", "g4"}),
    "b6": frozenset({"d6", "b4"}),
    "d6": frozenset({"d7", "b6", "f6", "d5"}),
    "f6": frozenset({"d6", "f4"}),
    "c5": frozenset({"d5", "c4"}),
    "d5": frozenset({"d6", "c5", "e5"}),
    "e5": frozenset({"d5", "e4"}),
    "a4": frozenset({"a7", "b4", "a1"}),
    "b4": frozenset({"b6", "a4", "c4", "b2"}),
    "c4": frozenset({"c5", "b4", "c3"}),
    "e4": frozenset({"e5", "f4", "e3"}),
    "f4": frozenset({"f6", "e4", "g4", "f2"}),
    "g4": frozenset({"g7", "f4", "g1"}),
    "c3": frozenset({"c4", "d3"}),
    "d3": frozenset({"c3", "e3", "d2"}),
    "e3": frozenset({"e4", "d3"}),
    "b2": frozenset({"b4", "d2"}),
    "d2": frozenset({"d3", "b2", "f2", "d1"}),
    "f2": frozenset({"f4", "d2"}),
    "a1": frozenset({"a4", "d1"}),
    "d1": frozenset({"a1", "g1", "d2"}),
    "g1": frozenset({"g4", "d1"}),
}

MILLS: tuple[frozenset[str], ...] = (
    frozenset({"a7", "d7", "g7"}),
    frozenset({"b6", "d6", "f6"}),
    frozenset({"c5", "d5", "e5"}),
    frozenset({"a4", "b4", "c4"}),
    frozenset({"e4", "f4", "g4"}),
    frozenset({"c3", "d3", "e3"}),
    frozenset({"b2", "d2", "f2"}),
    frozenset({"a1", "d1", "g1"}),
    frozenset({"a7", "a4", "a1"}),
    frozenset({"b6", "b4", "b2"}),
    frozenset({"c5", "c4", "c3"}),
    frozenset({"d7", "d6", "d5"}),
    frozenset({"d3", "d2", "d1"}),
    frozenset({"e5", "e4", "e3"}),
    frozenset({"f6", "f4", "f2"}),
    frozenset({"g7", "g4", "g1"}),
)

COLORS = frozenset({"white", "black"})


def empty_board() -> dict[str, Color]:
    return {point: None for point in POINTS}


def occupied(board: dict[str, Color], point: str) -> bool:
    return board.get(point) is not None
