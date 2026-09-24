#!/usr/bin/env python3
"""Phase 0b — applique la vérification des incipits suspects (tools/verif_suspects.tsv).

Vérification faite par recherche web de la phrase exacte (septembre 2026) :
  FAUX        une source montre un autre début de livre      → retiré
  INTROUVABLE la phrase n'est citée nulle part comme début     → retiré
  FORMULATION bon début, mauvaise formulation                → gardé, note avec la source
  PARTIEL     phrase authentique mais pas (ou pas entière) au début → gardé, note

Les entrées retirées sont sauvegardées dans tools/retires.json (restauration possible).
Les « vrais débuts » du TSV sont des indices pour retrouver la source : ils ne sont
JAMAIS copiés dans le corpus par ce script — un texte se copie depuis la source.
"""
import csv, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "inkipits.json").read_text(encoding="utf-8"))
assert len(data) == 366, "inkipits.json a changé depuis la vérification — relire les index"
rows = list(csv.DictReader(open(ROOT / "tools/verif_suspects.tsv", encoding="utf-8"), delimiter="\t"))

remove, notes = set(), {}
for r in rows:
    i = int(r["index"])
    if r["statut"] in ("FAUX", "INTROUVABLE"):
        remove.add(i)
    elif r["statut"] == "FORMULATION":
        notes[i] = f"formulation fausse — recopier la phrase exacte depuis la source : {r['source']}"
    elif r["statut"] == "PARTIEL":
        notes[i] = r["vrai_debut_selon_source"] + (f" — {r['source']}" if r["source"] else "")

for i, note in notes.items():
    data[i]["flag"] = note

removed = [dict(x, _raison=next(r["statut"] for r in rows if int(r["index"]) == i)) for i, x in enumerate(data) if i in remove]
kept = [x for i, x in enumerate(data) if i not in remove]
(ROOT / "tools/retires.json").write_text(json.dumps(removed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(ROOT / "inkipits.json").write_text(json.dumps(kept, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"retirés {len(removed)} · gardés avec note {len(notes)} · total {len(kept)}")
