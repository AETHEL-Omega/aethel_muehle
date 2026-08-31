# aethel_muehle — Mühle auf dem M4

Nine Men's Morris. Kein Engine-SDK, kein Netz, kein Flutter. Der Kern ist ein
**Regelwerk aus reinen Funktionen**, das AIX per rotem Test wachsen lässt.

Warum dieses Spiel auf dem M4: 24 Punkte, 16 Mühlen, fail-closed illegale Züge.
Ein lokaler 7B-Coder schließt **eine Regel pro Auftrag**. Nach Job 8 spielt ihr
zu zweit im Terminal. Danach kommt die Maschine als Gegner.

```bash
cd ~/workspace/aethel_muehle
python3.14 tests/test_board.py     # muss GRÜN sein (Brettgraph)
python3.14 tests/test_place.py     # Job 1 grün
python3.14 tests/test_forms_mill.py  # Job 2 grün
python3.14 tests/test_capture.py     # Job 3 grün
python3.14 tests/test_mill_protection.py  # Job 4 grün
```

Übernehmen nur bei `proof_strength=strong`. Testdateien nicht umschreiben.
Nächste Jobs: `CURRICULUM.md` (Job 5 `move`).
