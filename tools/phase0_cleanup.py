#!/usr/bin/env python3
"""Phase 0 — nettoyage de inkipits.json (voir tools/AUDIT.md).

  python3 tools/phase0_cleanup.py            # réécrit inkipits.json
  python3 tools/phase0_cleanup.py --dry-run  # affiche seulement le résumé

Ce script ne crée JAMAIS de texte d'incipit : il ne fait que choisir entre des
entrées déjà présentes (doublons), séparer des champs, retirer des champs faux
et poser des drapeaux « à vérifier ». Les décisions sont listées en clair
ci-dessous, une ligne par cas, pour pouvoir les relire / les contester.

Compatibilité app iOS : l'app ne décode que text, author, cover, description,
bio, amazon, emojis, complete_wrongs, author_pic (Incipit.swift, CodingKeys).
Les nouveaux champs (title, author_name, year, source, verified, flag) sont
ignorés par elle ; « author » reste au format « Titre — Auteur, Année ».
"""
import json, re, sys, unicodedata
from collections import Counter, defaultdict
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "inkipits.json"

# ── Doublons ────────────────────────────────────────────────────────────────
# keep: entrée conservée (sa position dans le fichier est gardée)
# drop: entrées supprimées ; leurs champs absents de `keep` (photo, cover…)
#       sont récupérés avant suppression
# text_from: prend le texte (et les complete_wrongs, qui en dépendent) d'une
#            autre entrée du groupe — la version la plus complète
# year: corrige l'année quand les deux entrées se contredisaient
DUPLICATES = [
    dict(keep=362, drop=[141], year="1978", why="141 « C'est un garçon sans histoire. » n'est pas l'incipit ; 1978 = parution (Goncourt 1978)"),
    dict(keep=348, drop=[105], why="105 « Il faisait un froid de canard… » n'est pas l'incipit"),
    dict(keep=344, drop=[229], why="même phrase ; 344 a la ponctuation et les accents"),
    dict(keep=349, drop=[104], year="1951", why="104 « Je ne sais pas pourquoi j'écris. » n'est pas l'incipit ; parution 1951"),
    dict(keep=388, drop=[89], year="2017", why="89 est une paraphrase ; parution 2017 (Goncourt 2017)"),
    dict(keep=268, drop=[4], why="même phrase, 268 plus complète"),
    dict(keep=300, drop=[20], why="même phrase ; « 189… » est la leçon du texte"),
    dict(keep=367, drop=[137], year="1999", why="137 « Je m'en vais. » tronqué ; parution 1999 (Goncourt 1999)"),
    dict(keep=373, drop=[152], year="2000", why="152 « Il y a des moments où tout bascule. » n'est pas l'incipit ; parution 2000"),
    dict(keep=330, drop=[106], why="106 « Je suis un monstre. » n'est pas l'incipit"),
    dict(keep=27, drop=[180], year="1877", why="deux traductions ; on garde 27, traduction à sourcer"),
    dict(keep=343, drop=[15], why="même phrase"),
    dict(keep=306, drop=[103], why="103 « Le ciel était d'un bleu si pur… » n'est pas l'incipit"),
    dict(keep=263, drop=[99], why="99 « Vers la fin de novembre 1625… » n'est pas l'incipit"),
    dict(keep=299, drop=[110], why="110 « Je ne suis pas un héros. » n'est pas l'incipit"),
    dict(keep=341, drop=[93], text_from=93, year="1951", why="même phrase, 93 plus complète ; parution 1951"),
    dict(keep=206, drop=[131], why="131 « Je suis tombé amoureux d'une ombre. » n'est pas l'incipit"),
    dict(keep=318, drop=[204], text_from=204, why="même phrase, 204 plus complète"),
    dict(keep=363, drop=[88], why="88 (CAPES à Annecy) n'est pas l'incipit"),
    dict(keep=260, drop=[8], why="même phrase, 260 plus complète"),
    dict(keep=352, drop=[50, 192], why="trois variantes ; 352 = traduction Durand, la plus répandue"),
    dict(keep=346, drop=[184], why="même phrase"),
    dict(keep=254, drop=[10], why="10 « Il y avait aujourd'hui » : le texte dit « Il y a aujourd'hui »"),
    dict(keep=176, drop=[31], why="deux traductions ; on garde celle de Vialatte, traduction à sourcer"),
    dict(keep=284, drop=[94], why="94 tronque « du théâtre des Variétés »"),
    dict(keep=321, drop=[0], text_from=0, why="même phrase, 0 plus complète"),
]
# Doublons NON tranchés (les deux restent, avec un drapeau) : voir SUSPECT.

# ── Incipits suspects (drapeau `flag`, rien n'est supprimé) ──────────────────
# Essentiellement le lot 98–174 : phrases courtes et génériques qui ne
# correspondent pas aux débuts connus des livres. À vérifier contre une source.
SUSPECT_BATCH = set(range(98, 175)) - {
    101, 113, 114, 115, 118,          # débuts connus (Nizan, Dostoïevski, Brainard, Monterroso, Hartley)
    99, 103, 104, 105, 106, 110, 131, 137, 141, 152, 88, 89,  # supprimés comme doublons
}
SUSPECT_EXTRA = {
    159: "doublon non tranché avec 210 — aucune des deux versions n'est sourcée",
    210: "doublon non tranché avec 159 — aucune des deux versions n'est sourcée",
    111: "« Demain, dès l'aube » est un poème du livre IV, pas l'ouverture du recueil",
    267: "incipit du recueil à vérifier (doublon avec 111)",
    79: "formulation à vérifier contre la traduction",
    81: "« Il était inévitable » : formulation à vérifier contre la traduction",
    367: "apostrophe manquante corrigée (« Je men » → « Je m'en »)",
}

# ── Descriptions fausses (autre livre / autre sujet) → retirées ──────────────
WRONG_DESCRIPTION = {
    1: "description de L'Étranger",
    10: "article sur la cathédrale (EN)",
    47: "article sur l'année 1984 (EN)",
    108: "description de Huis clos",
    112: "article générique sur le conte (EN)",
    151: "article sur le film (EN)",
    153: "article sur la cité mythique (EN)",
    161: "article sur le film (EN)",
    174: "article sur le film (EN)",
    182: "article sur la notion de foyer (EN)",
    200: "article sur la planète (EN)",
}
ENGLISH_ONLY = {18: "description", 60: "description", 62: "description", 97: "description", 173: "bio"}

# ── Titre / auteur mal saisis ────────────────────────────────────────────────
SWAPPED_TITLE_AUTHOR = {224}  # « Miguel Bonnefoy — Le Rêve du jaguar »
AUTHOR_ALIASES = {
    "García Márquez": "Gabriel García Márquez",
    "Gabriel Garcia Marquez": "Gabriel García Márquez",
    "Claude Levi-Strauss": "Claude Lévi-Strauss",
    "Paul auster": "Paul Auster",
    "Francois Bégaudeau": "François Bégaudeau",
    "Hubert Selby Jr": "Hubert Selby Jr.",
    "Laszlo Krasznahorkai": "László Krasznahorkai",
    "Etienne de Senancour": "Étienne de Senancour",
}
TEXT_TYPO = {367: ("Je men vais", "Je m'en vais")}

FIELD_ORDER = ["text", "title", "author_name", "year", "author", "cover", "author_pic",
               "bio", "description", "amazon", "emojis", "complete_wrongs",
               "source", "verified", "flag"]


def split_author(field):
    """« Titre — Auteur, Année » → (titre, auteur, année). Tolère – et l'absence d'année."""
    parts = re.split(r"\s+[—–]\s+", field.strip(), maxsplit=1)
    title = parts[0].strip()
    rest = parts[1].strip() if len(parts) > 1 else ""
    m = re.match(r"^(.*?),\s*(\S.*)$", rest)
    if m and re.search(r"\d", m.group(2)):
        return title, m.group(1).strip(), m.group(2).strip()
    return title, rest, ""


def compose_author(title, name, year):
    s = f"{title} — {name}" if name else title
    return f"{s}, {year}" if year else s


def author_key(name):
    return re.sub(r"[^a-z]", "", unicodedata.normalize("NFD", name).encode("ascii", "ignore").decode().lower())


def main(dry):
    data = json.loads(PATH.read_text(encoding="utf-8"))
    assert len(data) == 393, f"inkipits.json a changé depuis l'audit ({len(data)} entrées) — relire les index"
    log = Counter()

    # 1. Doublons (index d'origine, avant toute suppression)
    to_drop = set()
    for g in DUPLICATES:
        keep = data[g["keep"]]
        for j in g["drop"]:
            for k, v in data[j].items():
                if k not in keep and v:
                    keep[k] = v
            to_drop.add(j)
        if "text_from" in g:
            src = data[g["text_from"]]
            keep["text"] = src["text"]
            keep["complete_wrongs"] = src.get("complete_wrongs") or keep.get("complete_wrongs")
        if "year" in g:
            t, n, _ = split_author(keep["author"])
            keep["author"] = compose_author(t, n, g["year"])
        log["doublons supprimés"] += len(g["drop"])

    # 2. Champs par entrée
    for i, x in enumerate(data):
        if i in TEXT_TYPO:
            a, b = TEXT_TYPO[i]
            x["text"] = x["text"].replace(a, b)
        title, name, year = split_author(x["author"])
        if i in SWAPPED_TITLE_AUTHOR:
            title, name = name, title
        name = AUTHOR_ALIASES.get(name, name)
        title = re.sub(r"\s+", " ", title).strip()
        x["title"], x["author_name"], x["year"] = title, name, year
        x["author"] = compose_author(title, name, year)
        x.pop("completeWrongs", None)  # doublon mort : l'app ne lit que complete_wrongs
        if i in WRONG_DESCRIPTION:
            x.pop("description", None)
            log["descriptions fausses retirées"] += 1
        flags = []
        if i in SUSPECT_BATCH:
            flags.append("incipit suspect : ne correspond probablement pas au début du livre")
        if i in SUSPECT_EXTRA:
            flags.append(SUSPECT_EXTRA[i])
        if i in ENGLISH_ONLY:
            flags.append(f"{ENGLISH_ONLY[i]} en anglais")
        x["source"] = x.get("source")
        x["verified"] = False
        if flags:
            x["flag"] = " · ".join(flags)
            log["entrées avec drapeau"] += 1

    data = [x for i, x in enumerate(data) if i not in to_drop]

    # 3. Photo d'auteur : même photo pour tous les livres d'un même auteur
    pics = defaultdict(Counter)
    for x in data:
        if x.get("author_pic"):
            pics[author_key(x["author_name"])][x["author_pic"]] += 1
    for x in data:
        c = pics.get(author_key(x["author_name"]))
        if not c:
            continue
        # préfère Wikimedia (licence libre, CORS), sinon la plus fréquente
        best = sorted(c, key=lambda u: ("wikimedia.org" not in u and "wikipedia.org" not in u, -c[u]))[0]
        if x.get("author_pic") != best:
            log["photos d'auteur ajoutées" if not x.get("author_pic") else "photos d'auteur harmonisées"] += 1
            x["author_pic"] = best

    data = [{k: x[k] for k in FIELD_ORDER if k in x} | {k: v for k, v in x.items() if k not in FIELD_ORDER}
            for x in data]
    log["entrées au final"] = len(data)
    for k, v in log.items():
        print(f"{k:32} {v}")
    if not dry:
        PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"→ {PATH.name} réécrit")


if __name__ == "__main__":
    main("--dry-run" in sys.argv)
