#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Round 3 - Assouplissement du vocabulaire sur les pages les plus exposees
(index, retour d'affection, consultation de voyance, Mami Wata)
+ retrait des termes les plus "charges" (magie, vaudou, sorcellerie)
+ correction des H1 porteurs de promesses.

Principe : on garde "marabout" et "voyance" (identite reelle de l'activite,
pas de dissimulation), on remplace "rituel" par "accompagnement / tradition /
travail spirituel" sur les pages susceptibles de servir de page d'atterrissage.
"""
import re
import sys
from pathlib import Path

ROOT = Path("/home/user/sidibe")

# (fichier, ancien, nouveau, occurrences attendues)  -- fichier None = tous les fichiers
LITERAL = [
    # ------------------------------------------------- pages exposees : H1 / titres
    ("rituel.html",
     "<title>Rituel Mami Wata : Tradition & Symbolique | Marabout SIDIBE Salifou</title>",
     "<title>Mami Wata : Héritage & Symbolique | Marabout SIDIBE Salifou</title>", 1),
    ("rituel.html",
     "Mami Wata : Tradition & Symbolique | Marabout SIDIBE Salifou",
     "Mami Wata : Héritage & Symbolique | Marabout SIDIBE Salifou", 3),
    ("rituel.html",
     "Rituel Mami Wata du Marabout SIDIBE Salifou : ce que représente, dans la tradition vaudou, l'alliance avec la Reine des eaux. Un accompagnement symbolique, sans promesse d'enrichissement.",
     "Mami Wata : ce que représente, dans cette tradition, l'alliance avec la Reine des eaux. Un accompagnement symbolique, sans promesse d'enrichissement.", 3),
    ("rituel.html",
     "<h1>Initiation mami wata pour devenir un Homme puissant, riche</h1>",
     "<h1>Mami Wata : une tradition, son histoire et sa symbolique</h1>", 1),
    ("rituel.html",
     '<li><a href="rituel.html">Le rituel de mamiwata</a></li>',
     '<li><a href="rituel.html">La tradition Mami Wata</a></li>', 1),
    ("rituel.html", "votre%20page%20Rituel%20Mami%20Wata", "votre%20page%20Mami%20Wata", 3),

    ("bague.html",
     "<h1>PUISSANTE BAGUE MAGIQUE : En argent, favorise la fortune, la chance, le commerce, les\n\t\t\t\t\t\t\tentreprises, etc....</h1>",
     "<h1>BAGUE DE TRADITION EN ARGENT : un symbole personnel de chance et de protection</h1>", 1),
    ("bague.html",
     '<li><a href="#">PUISSANTE BAGUE MAGIQUE</a></li>',
     '<li><a href="#">BAGUE DE TRADITION</a></li>', 1),
    ("bague.html",
     "Cette bague magique est conçu sous la forme d'une bague naturelle selon votre choix, que soit",
     "Cette bague de tradition est conçue sous la forme d'une bague naturelle selon votre choix, que soit", 1),

    # ------------------------------------------- H1 porteurs de promesses (corriger)
    ("cadenas-amour.html",
     "<h1>Cadenas d'amour : scellez votre union pour toujours</h1>",
     "<h1>Cadenas d'amour : un symbole d'engagement pour votre couple</h1>", 1),
    ("chance-travail.html",
     "<h1>Chance, emploi &amp; examens : provoquez votre réussite</h1>",
     "<h1>Chance, emploi &amp; examens : préparez votre réussite</h1>", 1),
    ("clientele-commerce.html",
     "<h1>Clientèle &amp; commerce : faites prospérer vos affaires</h1>",
     "<h1>Clientèle &amp; commerce : l'accompagnement des commerçants et entrepreneurs</h1>", 1),
    ("conseil-signes-envoutement.html",
     "<h1>5 signes qui montrent que vous êtes envoûté</h1>",
     "<h1>5 signes souvent interprétés comme un envoûtement</h1>", 1),
    ("protection-desenvoutement.html",
     "<h1>Protection spirituelle &amp; désenvoûtement : reprenez le contrôle</h1>",
     "<h1>Protection spirituelle &amp; purification : retrouver la sérénité</h1>", 1),
    ("savons-parfums.html",
     "<h1>Savons &amp; parfums rituels : les produits du Maître</h1>",
     "<h1>Savons &amp; parfums de tradition : les produits du Maître</h1>", 1),
    ("savons-parfums.html",
     "<title>Savons & Parfums Rituels de Chance & d'Amour | Marabout SIDIBE Salifou</title>",
     "<title>Savons & Parfums de Tradition pour la Chance & l'Amour | Marabout SIDIBE Salifou</title>", 1),
    ("savons-parfums.html",
     "Savons & Parfums Rituels de Chance & d'Amour | Marabout SIDIBE Salifou",
     "Savons & Parfums de Tradition pour la Chance & l'Amour | Marabout SIDIBE Salifou", 3),

    # --------------------------------------------- pages exposees : corps de texte
    ("index.html",
     "Tous les rituels proposés sont réalisés avec le plus grand sérieux, par le Maître lui-même,\n\t\t\t\t\t\t\tdans le respect du code déontologique et du secret professionnel. Les rituels de magie\n\t\t\t\t\t\t\tblanche et de vaudou proposés ici ne sont jamais réalisés dans le but de nuire à autrui.",
     "Tous les accompagnements proposés sont réalisés avec le plus grand sérieux, par le Maître\n\t\t\t\t\t\t\tlui-même, dans le respect du code déontologique et du secret professionnel. Les pratiques\n\t\t\t\t\t\t\ttraditionnelles proposées ici ne sont jamais réalisées dans le but de nuire à autrui.", 1),
    ("index.html",
     "rituels de retour affectif sérieux, avec photos, dates et suivi personnalisé.",
     "un accompagnement traditionnel, avec photos, dates et suivi personnalisé.", 1),
    ("index.html",
     "Chance, amour, protection, commerce : les produits rituels du Maître.",
     "Chance, amour, protection, commerce : les produits de tradition du Maître.", 1),
    ("consultation-voyance.html",
     "besoin, les rituels adaptés.", "besoin, les accompagnements adaptés.", 1),

    # ----------------------------------------------- termes "chargés" (site entier)
    (None, "Rituels &amp; Produits", "Traditions &amp; Produits"),
    (None, "Rituel Mami Wata", "Tradition Mami Wata"),
    (None, "Rituel Mamy Wata", "Tradition Mamy Wata"),
    (None, "Bague Magique", "Bague Traditionnelle"),
    (None, "praticiens vaudou", "praticiens traditionnels"),
    (None, "dans la tradition vaudou", "dans cette tradition"),
    (None, "maître marabout vaudou", "maître marabout"),
    (None, "Contre la sorcellerie, la malchance et les influences négatives",
     "Contre la malchance et les influences négatives"),
    (None, "Contre sorcellerie, malchance et influences négatives",
     "Contre la malchance et les influences négatives"),
    (None, "contre la sorcellerie, la malchance et les influences négatives",
     "contre la malchance et les influences négatives"),
    # promesse de résultat : "faire revenir l'être aimé"
    (None,
     "Le retour d'affection du Marabout SIDIBE Salifou : des rituels sérieux pour faire revenir l'être aimé et rétablir l'harmonie dans votre couple.",
     "Le retour d'affection du Marabout SIDIBE Salifou : un accompagnement traditionnel et personnalisé de votre vie de couple."),
    (None,
     "Non. Les rituels de magie blanche et de vaudou que je propose ne sont jamais réalisés\n\t\t\t\t\t\t\tdans le but de nuire à autrui, ni à vous, ni à votre famille.",
     "Non. Les accompagnements traditionnels que je propose ne sont jamais réalisés dans le but\n\t\t\t\t\t\t\tde nuire à autrui, ni à vous, ni à votre famille."),
]

# (fichier ou None, motif regex, remplacement, occurrences attendues par fichier)
REGEX = [
    ("index.html",
     r"rituel Mami Wata, bague traditionnelle, voyance du Fa",
     "tradition Mami Wata, bague traditionnelle, voyance du Fa", 3),
]


def apply_to(path: Path, items, regex_items, problems):
    html = path.read_text(encoding="utf-8")
    orig = html
    for old, new, expected in items:
        found = html.count(old)
        if expected is not None and found != expected:
            if found == 0 and new in html:
                continue
            problems.append(f"[COUNT] {path.name}: attendu {expected}, trouvé {found} -> {old[:60]!r}")
            continue
        if found == 0:
            continue
        html = html.replace(old, new)
    for pattern, new, expected in regex_items:
        found = len(re.findall(pattern, html, flags=re.DOTALL))
        if expected is not None and found != expected:
            if found == 0 and new[:40] in html:
                continue
            problems.append(f"[COUNT-RE] {path.name}: attendu {expected}, trouvé {found} -> {pattern[:60]!r}")
            continue
        if found == 0:
            continue
        html = re.sub(pattern, lambda m: new, html, flags=re.DOTALL)
    if html != orig:
        path.write_text(html, encoding="utf-8")
        return True
    return False


def main():
    problems = []
    per_file = {}
    for fname, old, new, *rest in LITERAL:
        per_file.setdefault(fname, []).append((old, new, rest[0] if rest else None))
    per_re = {}
    for fname, pattern, new, expected in REGEX:
        per_re.setdefault(fname, []).append((pattern, new, expected))

    updated = 0
    for path in sorted(ROOT.glob("*.html")):
        items = per_file.get(path.name, []) + per_file.get(None, [])
        res = per_re.get(path.name, []) + per_re.get(None, [])
        if apply_to(path, items, res, problems):
            updated += 1

    print(f"Fichiers mis à jour : {updated}")
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    print("OK : round 3 appliqué.")


if __name__ == "__main__":
    main()
