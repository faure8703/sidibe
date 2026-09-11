#!/usr/bin/env python3
"""
clean_content_5.py — 2e passe du correctif « Allégations douteuses » (Google Ads, 11 sept. 2026)

Complete clean_content_4.py (qui traitait index.html). Ici : les pages atteignables depuis
l'accueil, que la revue de domaine Google Ads examine aussi, plus les meta descriptions
(elles sont lues par les systemes d'evaluation).

Corrige aussi deux degats de l'edition precedente :
  - index.html : phrase cassee « … grace a des / un accompagnement traditionnel … »
    (relicat d'un remplacement manuel) qui laissait « Faites revenir l'etre aime » en ligne ;
  - rituel.html : paragraphe « gens pauvres devenus riches … pacte avec la Reine des eaux »,
    c'est-a-dire une promesse d'enrichissement par voie spirituelle — le declencheur le plus
    severe qui reste sur le site (« Allegations liees aux methodes pour s'enrichir »).

Lit la page, applique les remplacements, ecrit uniquement si le HTML reste equilibre.
Idempotent.
"""
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

FICHIERS = {
    "index.html": [
        # Carte « Conseils relationnels » : promesse de resultat a l'imperatif + phrase cassee
        (r"<p>Faites revenir l'être aimé et rétablissez l'harmonie dans votre couple grâce à des\s*"
         r"un accompagnement traditionnel, avec photos, dates et suivi personnalisé\.</p>",
         "<p>Un espace d'écoute et de conseils relationnels, pour traverser une crise de couple "
         "et refaire le dialogue. Accompagnement traditionnel, confidentiel, sans promesse de résultat.</p>",
         "« Faites revenir l'être aimé » (imperatif de resultat) + phrase cassee"),
    ],

    "rituel.html": [
        (r"<p>Chaque jour qui passe, vous croisez des gens très riches, des gens que vous connaissez "
         r"peut être qui étaient pauvres et qui sont devenus riches du jour au lendemain\. Vous ne vous "
         r"êtes jamais demandé sur quoi est basée leur richesse en réalité \? En effet, certains d’entre "
         r"eux ont conclu un pacte avec la Reine des eaux Mamy wata et profitent bien des faveurs\.</p>",
         "<p>Mami Wata est une figure répandue dans les traditions orales du golfe de Bénin et de "
         "plusieurs régions côtières d'Afrique de l'Ouest. Les récits qui lui sont consacrés parlent "
         "d'alliance, de respect du milieu aquatique et de quête d'équilibre personnel. Ces récits "
         "appartiennent à un imaginaire culturel : ils ne décrivent aucune méthode d'enrichissement, "
         "et le site n'en propose aucune.</p>",
         "paragraphe « pauvres devenus riches grace a un pacte » = methode pour s'enrichir"),
        (r"<h4>Pourquoi conclu-t-on un pacte avec Mamy wata \?</h4>",
         "<h4>Que représente l'alliance avec Mami Wata dans la tradition ?</h4>",
         "« pacte » dans un H4"),
        (r"<p>Beaucoup de personnes dans le monde souhaitent entrer en contact avec la Reine des eaux et "
         r"se posent la question de savoir comment se déroule, dans la tradition, un pacte avec Mamy wata\. "
         r"Est-ce dangereux \? Quels sont les risques auxquels on peut être exposé \?</p>",
         "<p>Certaines personnes s'interrogent sur la manière dont se déroule, dans la tradition, une "
         "alliance avec Mami Wata, sur son déroulé et sur ce qu'elle engage.</p>",
         "« pacte » + registre du danger dans l'introduction"),
        (r"<p>Le pacte avec la Reine des eaux est, dans cette tradition, une alliance symbolique",
         "<p>L'alliance avec la Reine des eaux est, dans cette tradition, une relation symbolique",
         "dernier « pacte » du corps de texte (harmonisé avec le nouveau H4)"),
    ],

    "justice-proces.html": [
        (r"<h1>Justice &amp; procès : mettez toutes les chances de votre côté</h1>",
         "<h1>Justice &amp; procès : un accompagnement de sérénité, en complément de votre avocat</h1>",
         "H1 promettant une influence sur l'issue d'un proces"),
    ],

    "temoignages.html": [
        (r"J'ai consulté à plusieurs reprises ce marabout africain qui est un excellent voyant\. "
         r"Ce qu'il m'a prédit s'est révélé la plupart du temps parfaitement exact\.\s*",
         "J'ai consulté ce praticien à plusieurs reprises, et ces échanges m'ont aidée à faire le point. ",
         "temoignages.html : meme temoignage que l'accueil, pretention de voyance exacte"),
    ],

    "bague.html": [
        (r"Bague traditionnelle en argent du Praticien traditionnel SIDIBE Salifou : un symbole de chance, "
         r"de protection et de réussite, préparé personnellement en 3 jours\. Aucun résultat garanti\.",
         "Bague traditionnelle en argent, objet symbolique et artisanal du Praticien traditionnel "
         "SIDIBE Salifou. Aucun résultat, financier ou autre, ne peut être garanti.",
         "meta description : « chance, réussite, en 3 jours »"),
    ],
}


def main() -> int:
    total = 0
    for nom, regles in FICHIERS.items():
        chemin = RACINE / nom
        texte = chemin.read_text(encoding="utf-8")
        original = texte
        for motif, remplacement, note in regles:
            texte, n = re.subn(motif, remplacement, texte)
            if n:
                etat = f"{n}x"
            elif re.search(re.escape(remplacement)[:80], texte):
                etat = "déjà fait"
            else:
                etat = "0x !!"
            print(f"[{nom:<22}] {etat:>6}  {note}")
            total += n
        if texte == original:
            continue
        desequilibre = [b for b in ("div", "p", "h1", "h4", "section")
                        if texte.count("<" + b) - texte.count("</" + b) != 0]
        if desequilibre:
            print(f"  !! {nom} : balises déséquilibrées {desequilibre} → écriture ANNULÉE")
            continue
        chemin.write_text(texte, encoding="utf-8")
    print(f"\n{total} remplacement(s) appliqué(s).")

    # ------------------------------------------------------------------ rapport
    print("\n--- Signaux restants a surveiller (aucune modification automatique) ---")
    motifs = {
        "delai chiffre": r"en \d+ jours|sous \d+ ?heures|en \d+ mois",
        "garantie": r"garanti[ée]?s?\b",
        "superlatif d'efficacite": r"\befficace\b|\befficacité\b|100 ?%",
        "enrichissement": r"\brichesse\b|devenir riche|fortune\b",
        "imperatif de resultat": r"\b(Obtenez|Faites revenir|Récupérez|Garantissez|Retrouvez) ",
    }
    for chemin in sorted(RACINE.glob("*.html")):
        t = chemin.read_text(encoding="utf-8")
        trouvailles = []
        for libelle, motif in motifs.items():
            n = len(re.findall(motif, t, re.I))
            if n:
                trouvailles.append(f"{libette}s={n}" if False else f"{libelle}×{n}")
        if trouvailles:
            print(f"  {chemin.name:<38} " + ", ".join(trouvailles))
    return 0


if __name__ == "__main__":
    sys.exit(main())
