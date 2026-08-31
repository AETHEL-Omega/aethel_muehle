"""Placement, mills, movement. Job 1: place() is the red specification.

No I/O, no network, no randomness. Illegal actions raise MuehleError.
"""


class MuehleError(ValueError):
    """Fail-closed: the action is not legal in Mühle."""
