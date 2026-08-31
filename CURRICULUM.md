# M4-Warteschlange — aethel_muehle

Jedes Job ist ein `aix-solve` mit eigenem rotem Test. Kein I/O bis Job 8.
Brettgraph (`tests/test_board.py`) bleibt immer grün.

## Job 1 — Stein setzen (jetzt, muss rot sein)

`place(board, point, color)` in `muehle/rules.py`. Kopie des Bretts, Punkt
`white` oder `black`. `MuehleError` bei unbekanntem Punkt, belegtem Punkt,
ungültiger Farbe. Eingabe-Brett nicht mutieren.

```bash
python3.14 tests/test_place.py
aix-solve "Add place(board, point, color) in muehle/rules.py. Copy the board, set point to white or black. Raise MuehleError if point unknown, occupied, or color not white/black. Do not mutate the input board." \
  --test "python3.14 tests/test_place.py" --repo .
```

## Job 2 — Mühle erkennen

`forms_mill(board, point) -> bool`. True genau dann, wenn der Stein auf
`point` Teil einer vollen dreier Mühle seiner Farbe ist.

## Job 3 — Schlagen nach Mühle

`capture(board, point, by_color)`. Entfernt einen gegnerischen Stein.
`MuehleError` wenn der Punkt leer ist oder die eigene Farbe trägt.

## Job 4 — Mühle-Steine sind geschützt

`capture` verweigert einen Stein, der in einer Mühle steht, **es sei denn**
alle gegnerischen Steine stehen in Mühlen.

## Job 5 — Ziehen entlang der Kanten

`move(board, src, dst)`. Nur auf leeren Nachbarn laut `NEIGHBORS`.
`MuehleError` sonst.

## Job 6 — Fliegen mit drei Steinen

Hat eine Farbe genau drei Steine, darf `move` auf **jedes** leere Feld
(nicht nur Nachbarn).

## Job 7 — Gewinn

`winner(board, to_move)` ist die gegnerische Farbe, wenn `to_move` weniger
als drei Steine hat oder keinen legalen Zug. Sonst `None`.

## Job 8 — ASCII-Brett

`render(board) -> str` mit den drei Quadraten, Steine als `W`/`B`, leer als `·`.
Kein I/O — nur String.

## Job 9 — Zwei Spieler im Terminal

`python3.14 -m muehle` wechselt weiß/schwarz, liest Züge `a1`, `d7-d6`.
Erst hier I/O.

## Job 10 — Zufallslegaler Gegner, dann Minimax

`legal_actions(board, color)` und `choose(board, color)` — zuerst zufällig
unter legalen Zügen (Seed im Test), danach Bewertungsfunktion.
