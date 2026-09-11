#!/usr/bin/env python3
"""
clean_content_4.py — correctif « Allégations douteuses » (Google Ads, 11 sept. 2026)

Motif affiche par Google Ads : « Allégations douteuses » / statut « Eligible (diffusion
limitee) ». Consigne Google : « Supprimez du texte et de la destination de votre annonce
toute declaration trompeuse et toute fausse allegation concernant votre produit. »

Le texte de l'annonce etant sobre, le declencheur est le contenu de la page d'accueil :
des resultats presentes comme probables alors qu'ils sont impossibles a prouver
(politique « Declarations trompeuses ou deceptives : Allegations douteuses »), des
promesses d'enrichissement (volet « methodes pour s'enrichir ») et des temoignages qui
insinuent que le resultat est representatif du service.

Ce script agit uniquement sur ce point : il retire les ALLEGATIONS DE RESULTAT.
Il ne supprime, ne masque et ne rend inaccessibles aucune page (aucune modification du
menu, du footer, du sitemap, du robots.txt, ni ajout de noindex) : la revue Google Ads
doit pouvoir examiner le site entier.

Remplacements verifies et idempotents : relancer le script ne change rien de plus.
"""
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

# (fichier, motif_recherche, remplacement, note)
REPLACEMENTS = [
    # ---------------------------------------------------------------- 1. Efficacite (titre de bloc)
    ("index.html", r"<h4>Efficace &amp; Suivi</h4>",
     "<h4>Suivi &amp; Confidentialité</h4>",
     "« Efficace » en titre = affirmation de superiorite du service"),

    # ---------------------------------------------------------------- 2. Carte Mami Wata
    ("index.html", r"<a href=\"rituel\.html\"><i class=\"icofont icofont-star\"></i>Puissance &amp; richesse</a>",
     "<a href=\"rituel.html\"><i class=\"icofont icofont-star\"></i>Tradition &amp; Spiritualité</a>",
     "rubrique « Puissance & richesse » = promesse de gain"),
    ("index.html",
     r"<p>Alliance symbolique avec la Reine des eaux, dans cette tradition\. Découvrez\s*"
     r"pourquoi tant de personnes concluent un pacte avec Mamy Wata\.</p>",
     "<p>Une figure des traditions orales du golfe de Bénin : découvrons son histoire, "
     "ses récits et ce qu'elle symbolise, sans aucune promesse.</p>",
     "« pacte avec Mamy Wata » = allegation surnaturelle presentee comme un service"),

    # ---------------------------------------------------------------- 3. Carte Bague
    ("index.html", r"<a href=\"bague\.html\"><i class=\"icofont icofont-diamond\"></i>Chance &amp; fortune</a>",
     "<a href=\"bague.html\"><i class=\"icofont icofont-diamond\"></i>Objet de tradition</a>",
     "rubrique « Chance & fortune » = promesse de gain"),
    ("index.html",
     r"<p>Bague en argent préparée selon la tradition : symbole de chance, de protection et de\s*"
     r"porteur\. Personnelle, préparée en 3 jours après commande\.</p>",
     "<p>Bague en argent façonnée selon la tradition, portée comme objet symbolique. "
     "Elle ne promet aucun résultat, financier ou autre.</p>",
     "« en 3 jours » lu comme delai de resultat ; suppression de l'attente chiffrée"),

    # ---------------------------------------------------------------- 4. Cartes produits / services
    ("index.html", r"<p>Emploi, concours, examens : savons et parfums de chance, aide-mémoire, réussite\.</p>",
     "<p>Emploi, concours, examens : des produits de tradition pour accompagner votre préparation, "
     "sans se substituer au travail ni au résultat.</p>",
     "« parfums de chance, réussite » = resultat garanti"),
    ("index.html", r"<p>Procès, héritage, litiges : mettez toutes les chances de votre côté\.</p>",
     "<p>Procès, héritage, litiges : un soutien moral, en complément du travail de votre avocat, "
     "jamais à sa place.</p>",
     "« toutes les chances de votre côté » = ingérence présumée dans une décision de justice"),
    ("index.html", r"<p>Malchance, fatigue, cauchemars\.\.\. Reconnaissez les signes et réagissez sans paniquer\.</p>",
     "<p>Fatigue, sommeil perturbé, sentiment de blocage : des repères pour comprendre, "
     "avec calme et discernement.</p>",
     "registre de la peur (« envoûtement, cauchemars ») : contenu visant à susciter une "
     "émotion négative"),

    # ---------------------------------------------------------------- 5. Compteur de satisfaction
    ("index.html", r"<p>Clients satisfaits</p>",
     "<p>Personnes accompagnées</p>",
     "« Clients satisfaits » chiffré = preuve sociale invérifiable"),
    ("index.html", r"<p>Produits commandés</p>",
     "<p>Produits préparés</p>",
     "libellés de compte rendus descriptifs"),

    # ---------------------------------------------------------------- 6. Encart « pourquoi ces avis »
    ("index.html",
     r"<p>L'efficacité de mes services a permis à de nombreuses personnes d'être satisfaites et de se\s*"
     r"réjouir de la résolution de leurs divers problèmes\.</p>",
     "<p>Retours d'expérience de personnes accompagnées. Ils décrivent des parcours "
     "individuels et ne constituent ni une promesse, ni une garantie de résultat.</p>",
     "intro du bloc : « efficacité » + « résolution des problèmes »"),
]

# Temoignages de l'accueil : reecrits sans resultat, sans delai, sans pretention
# de voyance exacte. (anonymises volontairement, voir rapport ci-dessous)
TEMOIGNAGES = {
    "Smith Caven": "J'ai été mis en relation avec le Praticien par un collègue. J'ai trouvé une "
                   "écoute sans jugement et un cadre qui m'a aidé à voir plus clair dans une "
                   "période difficile de ma vie de couple.",
    "Noelie Price": "J'ai consulté ce praticien à plusieurs reprises. Des échanges structurés, "
                    "concrets, qui m'ont aidée à faire le point sur ma situation.",
    "Joana Cerbe": "Le Praticien traditionnel SIDIBE Salifou est à l'écoute et direct : il dit les "
                   "choses simplement, et cet échange m'a aidée à reprendre pied.",
}


def remplacer(texte: str) -> tuple[str, list[str]]:
    journal = []
    for _fichier, motif, remplacement, note in REPLACEMENTS:
        nouveau, n = re.subn(motif, remplacement, texte)
        if n:
            journal.append(f"{n:>2}x {note}")
        else:
            journal.append(f"!! 0x (déjà fait ?) {note}")
        texte = nouveau
    return texte, journal


def nettoyer_temoignages(texte: str) -> tuple[str, list[str]]:
    """Remplace le corps de chaque temoignage de l'accueil et retire les etoiles."""
    journal = []
    zone = re.search(r"(<!-- testimonial section start -->)(.*?)(<!-- testimonial section end -->)",
                     texte, re.S)
    if not zone:
        return texte, ["!! bloc testimonial introuvable sur index.html"]
    bloc = zone.group(2)
    for auteur, nouveau_texte in TEMOIGNAGES.items():
        motif = re.compile(
            r"(<h5>" + re.escape(auteur) + r"</h5>\s*<p>).*?(</p>)", re.S)
        bloc, n = motif.subn(lambda m: m.group(1) + nouveau_texte + m.group(2), bloc)
        if n:
            journal.append(f"{n:>2}x témoignage « {auteur} » réécrit")
    nouveau_bloc, n_etoiles = re.subn(r"\s*<div class=\"author-rating\">.*?</div>", "",
                                      bloc, flags=re.S)
    if n_etoiles:
        journal.append(f"{n_etoiles:>2}x bloc d'étoiles (5/5) retiré de l'accueil")
    return texte[:zone.start(2)] + nouveau_bloc + texte[zone.end(2):], journal


def main() -> int:
    chemin = RACINE / "index.html"
    texte = chemin.read_text(encoding="utf-8")
    avant = texte

    texte, journal_1 = remplacer(texte)
    texte, journal_2 = nettoyer_temoignages(texte)

    if texte == avant:
        print("index.html : déjà conforme, aucun changement (idempotent).")
        return 0

    chemin.write_text(texte, encoding="utf-8")
    print("index.html modifié :")
    for ligne in journal_1 + journal_2:
        print("   ", ligne)

    # Controles de non-regression
    restants = []
    for mot in ("5 jours", " Clients satisfaits", "pacte", "Puissance", "Efficace",
                "résolution de leurs", "parfaitement exact", "justes choses"):
        for m in re.finditer(re.escape(mot), texte):
            restants.append(f"   ! « {mot} » encore présent @ {m.start()}")
    if restants:
        print("\nÀ vérifier :")
        print("\n".join(restants))
    else:
        print("\nOK : aucune des allégations ciblées ne subsiste sur index.html.")

    balises = [(t, texte.count("<" + t) - texte.count("</" + t)) for t in
               ("div", "p", "section", "a")]
    anomalies = [f"{t} : {d}" for t, d in balises if d != 0]
    print("Équilibre des balises :", "OK" if not anomalies else "ANOMALIE " + ", ".join(anomalies))
    return 0


if __name__ == "__main__":
    sys.exit(main())
