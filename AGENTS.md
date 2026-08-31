# AGENTS.md — aethel_muehle

## Was ist das
Nine Men's Morris (Mühle). Reines Python-Regelwerk, kein I/O im Kern.
Erste AIX-Arbeit auf dem M4: fail-closed Züge, rote Tests, `aix-solve`.

## Build / Test / Run
- Test: `python3.14 tests/test_board.py` (grün) und `python3.14 tests/test_place.py` (Job 1 grün)
- Suite: `python3.14 -m pytest -q`
- Nächster Auftrag: `CURRICULUM.md`

## Konventionen
- Keine neuen Abhängigkeiten. Kein Netz. Kein Zufall außer in Job 10 mit Seed.
- Brett ist ein dict `point -> None|"white"|"black"`. Funktionen kopieren, mutieren nicht.
- Illegale Züge: `MuehleError`, nicht `False`.

## Architektur-Grenzen / Tabu-Zonen
- Testdateien sind die Spezifikation — Coder darf sie nicht umschreiben.
- `muehle/board.py` Graph (POINTS, NEIGHBORS, MILLS) nicht „vereinfachen“.
- Kein Flutter, kein pygame, kein Echtzeit-Loop vor Job 9.

## Workflow / PR
- Ein Job pro Branch. Übernehmen nur bei `proof_strength=strong`.
