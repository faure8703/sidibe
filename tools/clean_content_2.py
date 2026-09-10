#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Round 2 : suppression des signaux a risque restants
- "retour a l'envoyeur" / nuire a autrui (politique Google : pas de services censes nuire)
- promesses medicales (pathologies, fertilité, tension...)
- promesses d'invulnerabilite, de gain d'argent, d'influence sur la justice
- contenus coercitifs (emprise sur la liberte d'une personne)
"""
import re
import sys
from pathlib import Path

ROOT = Path("/home/user/sidibe")

CHECK = '<i class="fa fa-check-circle" style="color:green;"></i>'

LITERAL = [
    # ------------------------------------------------------- index : protection
    ("index.html",
     "Contre la sorcellerie, la malchance et les ennemis, retour à l'envoyeur.",
     "Contre la sorcellerie, la malchance et les influences négatives : protection et purification.", 1),
    ("index.html",
     "Contre sorcellerie, malchance et ennemis : désenvoûtement et retour à l'envoyeur.",
     "Contre sorcellerie, malchance et influences négatives : protection et purification.", 1),

    # ------------------------------------------- protection / désenvoûtement
    ("protection-desenvoutement.html",
     "contre sorcellerie, malchance, ennemis. Talisman, bague et savon de protection, retour à l'envoyeur.",
     "contre la sorcellerie, la malchance et les influences négatives. Talisman, bague et savon de protection.", 3),
    ("protection-desenvoutement.html",
     "savon de protection avec retour à l'envoyeur.",
     "savon de protection et de purification.", 1),
    ("protection-desenvoutement.html",
     "de vous <strong>protéger et de renvoyer le mal à son envoyeur</strong>, dans le respect",
     "de vous <strong>protéger et de purifier votre environnement</strong>, dans le respect", 1),
    ("protection-desenvoutement.html",
     "<strong>Suivi personnalisé</strong> jusqu'au retour complet à une vie apaisée.",
     "<strong>Suivi personnalisé</strong> pour vous accompagner vers plus de sérénité.", 1),

    # ------------------------------------------------------------ savons/parfums
    ("savons-parfums.html",
     "<strong>Savon de protection</strong> avec retour à l'envoyeur contre sorcellerie et jalousie",
     "<strong>Savon de protection</strong> pour la purification et contre les ondes négatives", 1),

    # ------------------------------------------------------------ justice
    ("justice-proces.html", "Faveur & Apaisement", "Sérénité & Apaisement", 4),
    ("justice-proces.html",
     "Faveur, apaisement, issue heureuse", "Sérénité, apaisement, protection", 1),

    # ------------------------------------------------------------ divers produits
    ("diversproduit.html",
     'Gain Facile (<a href="chance-travail.html">Gagner au jeu de\n\t\t\t\t\t\t\t\thasard</a>)',
     '<a href="chance-travail.html">Chance aux examens et concours</a>', 1),
    ("diversproduit.html",
     "Provocation de divorce", "Médiation et apaisement dans le couple", 1),
    ("diversproduit.html",
     '<a href="protection-desenvoutement.html">Protection contre ennemis</a>',
     '<a href="protection-desenvoutement.html">Protection contre les influences négatives</a>', 1),
    ("diversproduit.html",
     '<a href="fertilite-famille.html">Ménopause Précoce</a>',
     '<a href="fertilite-famille.html">Accompagnement féminin (ménopause)</a>', 1),
    ("diversproduit.html",
     '<a href="protection-desenvoutement.html">Contre-attaques</a>',
     '<a href="protection-desenvoutement.html">Protection du foyer</a>', 1),
    ("diversproduit.html",
     '<a href="fertilite-famille.html">Règle douloureuses</a>',
     '<a href="fertilite-famille.html">Confort féminin (accompagnement traditionnel)</a>', 1),
    ("diversproduit.html", "Pour sauver une personne", "Soutien et écoute d'un proche", 1),
    ("diversproduit.html", "Pour soigner la folie", "Écoute et soutien moral", 1),
    ("diversproduit.html", "Ce-dèmes", "Apaisement et réconfort moral", 1),
    ("diversproduit.html", "Pour provoquer la menstrues", "Accompagnement du cycle féminin", 1),
    ("diversproduit.html",
     '<a href="fertilite-famille.html">Pour régulariser les règles</a>',
     '<a href="fertilite-famille.html">Accompagnement du cycle féminin</a>', 1),
    ("diversproduit.html", "Contre tétanos", "Protection symbolique du foyer", 1),
    ("diversproduit.html", "Azoospermies", "Accompagnement de la fertilité du couple", 1),
    ("diversproduit.html", "Hypotension", "Apaisement et gestion du stress", 1),
    ("diversproduit.html", "Contre tension", "Apaisement et gestion du stress", 1),
    ("diversproduit.html", "Contre les balles et les\n\t\t\t\t\t\t\t\tcouteaux",
     "Protection symbolique en déplacement", 1),
    ("diversproduit.html", '<a href="protection-desenvoutement.html">Contre accident</a>',
     '<a href="protection-desenvoutement.html">Protection symbolique en déplacement</a>', 1),
    ("diversproduit.html", '<a href="protection-desenvoutement.html">Contre le braquage</a>',
     '<a href="protection-desenvoutement.html">Sérénité dans les déplacements</a>', 1),
    ("diversproduit.html", "Contre affectations non désirées", "Apaiser les relations difficiles", 1),
    ("diversproduit.html", "Hypertension", "Apaisement et gestion du stress", 1),
    ("index.html",
     "Stérilité du couple, protection de grossesse, entente familiale, bonheur au foyer.",
     "Difficultés à concevoir, accompagnement de la maternité, entente familiale, bonheur au foyer.", 1),
    ("index.html",
     "stérilité du couple et pour protéger la grossesse et le foyer.",
     "difficultés à concevoir et pour accompagner la maternité et le foyer.", 1),
    ("purification-lieux.html",
     "Malheurs, maladies ou disputes depuis l'ins",
     "Malheurs, tensions ou disputes depuis l'ins", 1),
]

REGEX = [
    ("fertilite-famille.html",
     r"Stérilité féminine ou\s*\n\s*masculine du couple",
     "Difficultés à concevoir (accompagnement du couple)", 1),
    ("diversproduit.html",
     r"La stérilité féminine et\s*\n\s*masculin",
     "Accompagnement de la fertilité du couple", 1),
    ("diversproduit.html",
     r"Recette pour faire un garçon\s*\n\s*</li>",
     "Accompagnement traditionnel de la grossesse</li>", 1),
    ("diversproduit.html",
     r"Protection et retour à\s*\n\s*l['’]envoyeur",
     "Protection et purification", 1),
    ("diversproduit.html",
     r"Pour éviter de faire des enfants\s*\n\s*mort(e)?s",
     "Accompagnement traditionnel de la maternité", 1),
    ("diversproduit.html",
     r"Pour en engendrer ou engrosser\s*\n\s*facilement",
     "Accompagnement du désir d'enfant", 1),
    ("diversproduit.html",
     r"Pour empêcher une femme de\s*\n\s*sortir",
     "Conseil et médiation dans le couple", 1),
]


def main():
    problems = []
    cache = {}

    def read(fname):
        if fname not in cache:
            cache[fname] = (ROOT / fname).read_text(encoding="utf-8")
        return cache[fname]

    for fname, old, new, expected in LITERAL:
        html = read(fname)
        found = html.count(old)
        if found != expected:
            if found == 0 and new in html:
                continue
            problems.append(f"[COUNT] {fname}: attendu {expected}, trouvé {found} -> {old[:70]!r}")
            continue
        cache[fname] = html.replace(old, new)

    for fname, pattern, new, expected in REGEX:
        html = read(fname)
        found = len(re.findall(pattern, html, flags=re.DOTALL))
        if found != expected:
            if found == 0 and new[:40] in html:
                continue
            problems.append(f"[COUNT-RE] {fname}: attendu {expected}, trouvé {found} -> {pattern[:70]!r}")
            continue
        cache[fname] = re.sub(pattern, lambda m: new, html, flags=re.DOTALL)

    for fname in sorted(ROOT.glob("*.html")):
        html = cache.get(fname.name, fname.read_text(encoding="utf-8"))
        (ROOT / fname).write_text(html, encoding="utf-8")

    print(f"Fichiers mis à jour : {len(cache)}")
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    print("OK : round 2 appliqué.")


if __name__ == "__main__":
    main()
