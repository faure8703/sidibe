#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nettoyage du contenu du site maitresalifou.com
Objectif : conformite Google Ads (pas de resultat garanti, pas de promesse
medicale / judiciaire / financiere, pas d'emprise sur la volonte d'autrui).
Tous les remplacements sont LITTERAUX (sauf la liste REGEX) et verifies.
"""
import re
import sys
from pathlib import Path

ROOT = Path("/home/user/sidibe")

# (fichier, ancien texte, nouveau texte, occurrences attendues)
LITERAL = [
    # ------------------------------------------------------------------ index
    ("index.html",
     "Vous êtes venu à bon port. Avec l'aide du grand maître médium marabout africain voyant",
     "Vous êtes venu à bon port. Avec le grand maître médium marabout africain voyant", 1),
    ("index.html",
     "vous avez la solution rapide et efficace à tous vos problèmes :",
     "vous trouverez une écoute attentive, un diagnostic et un accompagnement personnalisé :", 1),
    ("index.html",
     "Initié par son grand-père en Afrique, ses pouvoirs occultes sont appréciés et sollicités",
     "Initié par son grand-père en Afrique, son savoir traditionnel est apprécié et sollicité", 1),
    ("index.html",
     "par celles et ceux qui n'ont pas eu satisfaction auprès d'autres marabouts.",
     "par celles et ceux qui souhaitent un avis clair et un accompagnement.", 1),
    ("index.html",
     "vous garantit un travail de qualité,", "vous propose un accompagnement sérieux,", 1),
    ("index.html",
     "Expert dans la résolution de tous les problèmes :",
     "Accompagnement dans tous les domaines de la vie :", 1),
    ("index.html",
     "avec un accompagnement personnalisé jusqu'à satisfaction.",
     "avec un suivi personnalisé et confidentiel, sans promesse de résultat.", 1),
    ("index.html",
     "Peu importe vos problèmes et vos inquiétudes, contactez-moi à tout moment pour votre",
     "Peu importe vos problèmes et vos inquiétudes, contactez-moi à tout moment pour en", 1),
    ("index.html",
     "satisfaction, où que vous soyez dans le monde.",
     "parler librement, où que vous soyez dans le monde.", 1),
    ("index.html",
     "Éclairez vos choix grâce à l'oracle du Fa : amour, travail, famille. Réponse en 24-48h.",
     "Éclairez vos choix grâce à l'oracle du Fa : amour, travail, famille. Réponse rapide, généralement sous 48 heures.", 1),
    ("index.html",
     "Alliance avec la Reine des eaux pour obtenir gloire, richesse et puissance.",
     "Alliance symbolique avec la Reine des eaux, dans la tradition vaudou.", 1),
    ("index.html",
     "Puissante bague en argent qui attire la richesse, la chance et la grâce divine sur son",
     "Bague en argent préparée selon la tradition : symbole de chance, de protection et de", 1),
    ("index.html",
     "rituel Mami Wata, bague magique, voyance du Fa",
     "rituel Mami Wata, bague traditionnelle, voyance du Fa", 3),
    ("index.html",
     "Marabout Voyant Africain Sérieux SIDIBE Salifou | Retour d'Affection, Voyance, Protection",
     "Marabout Voyant SIDIBE Salifou | Consultation, Conseils & Guidance", 4),
    ("index.html",
     "Grand Maître Marabout Voyant Africain Sérieux SIDIBE Salifou du Bénin :",
     "Grand Maître Marabout Voyant SIDIBE Salifou du Bénin :", 3),
    ("index.html",
     "<h1>Grand Maître Marabout Voyant Africain Sérieux SIDIBE Salifou du Bénin</h1>",
     "<h1>Grand Maître Marabout Voyant SIDIBE Salifou du Bénin : consultation et conseils traditionnels</h1>", 1),

    # ------------------------------------------------------- retour d'affection
    ("retouraffection.html",
     "Retour d'Affection Rapide & Efficace", "Retour d'Affection : Consultation & Accompagnement", 4),
    ("retouraffection.html",
     "Retour d'affection rapide du Marabout SIDIBE Salifou : rituels sérieux pour faire revenir l'être aimé et sauver votre couple. Discrétion totale, disponible 24h/24.",
     "Retour d'affection : consultation et accompagnement traditionnel du Marabout SIDIBE Salifou pour votre situation amoureuse. Écoute, discrétion totale, disponible 24h/24. Aucun résultat garanti.", 3),
    ("retouraffection.html",
     "<h1>Reconquête de l’être aimé & possession amoureuse avec résultat en 7 jours</h1>",
     "<h1>Retour d'affection : écoute, consultation et accompagnement personnalisé</h1>", 1),
    ("retouraffection.html",
     "Le retour de l’être aimé est la problématique que le grand chef occulte peut résoudre en apportant une solution adaptée et personnelle.",
     "Le retour de l’être aimé est une situation délicate : j’accompagne chaque cas par une consultation préalable, une écoute et des conseils personnalisés.", 1),
    ("retouraffection.html",
     "Produits très efficace et moins coûteux", "Produits traditionnels à petit prix", 1),

    # ------------------------------------------------------------------ bague
    ("bague.html",
     "Puissante Bague Magique en Argent", "Bague Traditionnelle en Argent", 4),
    ("bague.html",
     "Puissante bague traditionnelle en argent du Marabout SIDIBE Salifou : attire la fortune, la chance, la protection et la réussite commerciale. Préparée personnellement en 3 jours.",
     "Bague traditionnelle en argent du Marabout SIDIBE Salifou : un symbole de chance, de protection et de réussite, préparé personnellement en 3 jours. Aucun résultat garanti.", 3),
    ("bague.html",
     "Cette puissante bague magique, attire la richesse et la grâce divine sur son porteur, la",
     "Dans la tradition, cette bague en argent est un symbole de chance et de protection pour son", 1),
    ("bague.html",
     "chance l'accompagnera partout. L'influence de cette bague agit surtout dans le domaine\n\t\t\t\t\t\t\tfinancier du porteur.",
     "porteur. Elle est préparée et remise dans un cadre symbolique : chaque pièce est unique et\n\t\t\t\t\t\t\tpersonnelle.", 1),
    ("bague.html",
     "Cette bague a transformé des mendiants en rois dans un intervalle de 7 semaines.",
     "Chaque bague est préparée selon vos intentions, dans le respect de la tradition.", 1),
    ("bague.html",
     "ouvrira pour vous toutes les porte de la richesse et de l'abondance, vos affaire fleuriront\n\t\t\t\t\t\t\tde manière incontrôlable. C'est une bague Magique utiliser par beaucoup de grand hommes,\n\t\t\t\t\t\t\tfaites attention à leur doigts. Satisfaction garantie 100%.",
     "devient le support symbolique de vos intentions : chance, protection, réussite. Beaucoup de\n\t\t\t\t\t\t\tpersonnes portent au quotidien une bague de ce type, comme on porte un porte-bonheur.\n\t\t\t\t\t\t\tAucun résultat — financier ou autre — ne peut être garanti.", 1),
    ("bague.html",
     "Produits très efficace et moins coûteux", "Produits traditionnels à petit prix", 1),

    # ----------------------------------------------------------------- rituel
    ("rituel.html",
     "Rituel Mami Wata : Richesse & Puissance", "Rituel Mami Wata : Tradition & Symbolique", 4),
    ("rituel.html",
     "Rituel Mami Wata du Marabout SIDIBE Salifou : initiation et alliance avec la Reine des eaux pour la richesse et la puissance, sans danger pour vous et votre famille.",
     "Rituel Mami Wata du Marabout SIDIBE Salifou : ce que représente, dans la tradition vaudou, l'alliance avec la Reine des eaux. Un accompagnement symbolique, sans promesse d'enrichissement.", 3),
    ("rituel.html",
     "Beaucoup de personnes dans le monde qui veulent entrer en contact avec la Reine des eaux pour obtenir gloire et richesse se posent le plus souvent la question de savoir comment fait-on pour signer un pacte avec Mamy wata.",
     "Beaucoup de personnes dans le monde souhaitent entrer en contact avec la Reine des eaux et se posent la question de savoir comment se déroule, dans la tradition, un pacte avec Mamy wata.", 1),
    ("rituel.html",
     "Produits très efficace et moins coûteux", "Produits traditionnels à petit prix", 1),

    # -------------------------------------------------------- mari / femme de nuit
    ("mari-femme-nuit.html",
     "pour chasser définitivement l'esprit et purifier votre chambre.",
     "pour travailler symboliquement sur la rupture des liens et purifier votre chambre.", 1),
    ("mari-femme-nuit.html",
     "plus vite votre vie amoureuse et votre sommeil se normalisent. Discrétion totale garantie.",
     "plus tôt vous pourrez engager une démarche d'apaisement. Discrétion totale.", 1),

    # --------------------------------------------------------------- guide / FAQ
    ("guide-consultation-faq.html",
     "suivi personnalisé jusqu'à satisfaction.", "suivi personnalisé.", 1),
    ("guide-consultation-faq.html",
     "jours, d'autres en quelques semaines. Méfiez-vous de ceux qui promettent tout, tout de\n\t\t\t\t\t\t\tsuite, sans même étudier votre cas.",
     "jours, d'autres en quelques semaines, d'autres encore ressentent surtout un apaisement\n\t\t\t\t\t\t\tpersonnel. <strong>Aucun résultat ne peut être garanti à 100 % : la voyance n'est pas une\n\t\t\t\t\t\t\tscience exacte.</strong> Méfiez-vous de ceux qui promettent tout, tout de suite, sans même\n\t\t\t\t\t\t\tétudier votre cas.", 1),

    # ----------------------------------------------------------- consultation Fa
    ("consultation-voyance.html",
     "Plus de 20 ans d'expérience, réponse en 24-48h, discrétion totale.",
     "Plus de 20 ans d'expérience, réponse rapide (généralement sous 48 heures), discrétion totale.", 3),
    ("consultation-voyance.html",
     "fidélité, mariage, retour de l'être aimé", "fidélité, mariage, questions de cœur", 1),
    ("consultation-voyance.html",
     "<li><strong>Réponse en 24 à 48 heures</strong>, avec des conseils concrets et, si",
     "<li><strong>Réponse rapide</strong> (généralement sous 48 heures), avec des conseils concrets et, si", 1),

    # ------------------------------------------------------------------ contact
    ("contact.html",
     "Peu importe vos problèmes et vos inquiétudes, contactez-moi à tout moment pour votre\n\t\t\t\t\t\t\tsatisfaction. La consultation peut se faire",
     "Peu importe vos problèmes et vos inquiétudes, contactez-moi à tout moment pour en parler.\n\t\t\t\t\t\t\tLa consultation peut se faire", 1),

    # -------------------------------------------------------------- divers produits
    ("diversproduit.html",
     "<h1>Optez pour mes produits les plus efficaces</h1>",
     "<h1>Découvrez mes produits et accompagnements traditionnels</h1>", 1),
    ("diversproduit.html",
     "J'interviens dans tous ces domaines pour la satisfaction et le traitement de vos différentes\n\t\t\t\t\t\t\tinquiétudes vraiment à moindre coût",
     "Je vous accompagne dans tous ces domaines par une écoute et un conseil personnalisé, à\n\t\t\t\t\t\t\tmoindre coût", 1),
    ("diversproduit.html",
     '<li><i class="fa fa-check-circle" style="color:green;"></i> Impuissance total</li>',
     '<li><i class="fa fa-check-circle" style="color:green;"></i> Accompagnement traditionnel du couple</li>', 1),
    ("diversproduit.html",
     '<li><i class="fa fa-check-circle" style="color:green;"></i> Ulcères</li>',
     '<li><i class="fa fa-check-circle" style="color:green;"></i> Apaisement et réconfort moral</li>', 1),
    ("diversproduit.html",
     '<li><i class="fa fa-check-circle" style="color:green;"></i> Epilepsie</li>',
     '<li><i class="fa fa-check-circle" style="color:green;"></i> Soutien moral dans les épreuves</li>', 1),
    ("diversproduit.html",
     '<li><i class="fa fa-check-circle" style="color:green;"></i> Drépanocytose</li>',
     '<li><i class="fa fa-check-circle" style="color:green;"></i> Accompagnement des familles</li>', 1),
    ("diversproduit.html",
     '<li><i class="fa fa-check-circle" style="color:green;"></i> Dépression mental</li>',
     '<li><i class="fa fa-check-circle" style="color:green;"></i> Écoute et soutien dans les périodes de doute</li>', 1),
    ("diversproduit.html",
     '<li><i class="fa fa-check-circle" style="color:green;"></i> Développement de sexe</li>',
     '<li><i class="fa fa-check-circle" style="color:green;"></i> Équilibre intime (accompagnement traditionnel)</li>', 1),
    ("diversproduit.html",
     '<li><i class="fa fa-check-circle" style="color:green;"></i> Battement de cœur</li>',
     '<li><i class="fa fa-check-circle" style="color:green;"></i> Apaiser les tensions du quotidien</li>', 1),
    ("diversproduit.html",
     '<li><i class="fa fa-check-circle" style="color:green;"></i> <a href="protection-desenvoutement.html">Contre poison</a></li>',
     '<li><i class="fa fa-check-circle" style="color:green;"></i> <a href="protection-desenvoutement.html">Protection symbolique du foyer</a></li>', 1),
    ("diversproduit.html",
     '<li><i class="fa fa-check-circle" style="color:green;"></i> <a href="fertilite-famille.html">Contre la faiblesse d\'une\n\t\t\t\t\t\t\t\tgrossesse</a></li>',
     '<li><i class="fa fa-check-circle" style="color:green;"></i> <a href="fertilite-famille.html">Accompagnement de la maternité</a></li>', 1),

    # ----------------------------------------------------------------- fertilité
    ("fertilite-famille.html",
     "Soyez sans\n\t\t\t\t\t\t\tcrainte : avec les forces occultes et les traitements thérapeutiques à base de\n\t\t\t\t\t\t\t<strong>plantes traditionnelles</strong>, le grand médium Marabout\n\t\t\t\t\t\t\t<strong>SIDIBE Salifou</strong> vous accompagne pour vous aider à avoir un enfant.",
     "Mon approche associe un accompagnement spirituel, des conseils de tradition à base de\n\t\t\t\t\t\t\t<strong>plantes</strong> et une écoute du couple. Le grand médium Marabout\n\t\t\t\t\t\t\t<strong>SIDIBE Salifou</strong> vous accompagne dans cette démarche, en complément —\n\t\t\t\t\t\t\tjamais en remplacement — d'un suivi médical.", 1),

    # ------------------------------------------------------------------ justice
    ("justice-proces.html",
     "mettez toutes les chances de votre côté pour un procès, un héritage ou un litige de terrain. Rituels de faveur et d'apaisement.",
     "un accompagnement spirituel et symbolique pour un procès, un héritage ou un litige de terrain, en complément du conseil d'un avocat.", 3),

    # --------------------------------------------------------------- clientèle
    ("clientele-commerce.html",
     "puis d'appliquer la solution adaptée, avec un suivi de vos résultats.",
     "puis de proposer un accompagnement adapté, avec un suivi régulier.", 1),

    # ------------------------------------------------------------------ maître
    ("maitre-sidibe.html",
     "Marabout honnête, professionnel, efficace, discret",
     "Marabout à l'écoute, professionnel et discret", 1),
    ("maitre-sidibe.html",
     "Ses travaux et ses résultats lui ont permis d'être élevé à l'ordre du mérite des grands",
     "Sa pratique et son expérience lui ont valu d'être distingué par ses pairs parmi les grands", 1),
    ("maitre-sidibe.html",
     "marabouts africains et d'être élu plusieurs fois <strong>marabout de l'année à Paris,\n\t\t\t\t\t\t\tBruxelles, en Suisse et aux USA</strong>. Faites-lui confiance : ses travaux sont d'une\n\t\t\t\t\t\t\tgrande qualité, avec un suivi adéquat et une confidentialité totale.",
     "marabouts africains, ainsi que la reconnaissance de consultants venus de <strong>Paris,\n\t\t\t\t\t\t\tBruxelles, Suisse et USA</strong>. Il reçoit chaque demande avec une rigueur constante,\n\t\t\t\t\t\t\tun suivi et une confidentialité totale.", 1),

    # ------------------------------------------------------------- témoignages
    ("temoignages.html",
     "Témoignages & Avis Clients Vérifiés", "Témoignages & Retours d'expérience", 4),
    ("temoignages.html",
     "Témoignages des clients du Marabout SIDIBE Salifou : retour d'affection, voyance, désenvoûtement, réussite. Découvrez leurs histoires et leurs satisfactions.",
     "Témoignages et retours d'expérience des clients du Marabout SIDIBE Salifou : retour d'affection, voyance, protection, réussite. Expériences individuelles, sans caractère de garantie.", 3),
    ("temoignages.html",
     "L'efficacité de mes services a permis à de nombreuses personnes d'être satisfaites et de\n\t\t\t\t\t\t\tse réjouir de la résolution de leurs divers problèmes. Voici quelques-uns de leurs\n\t\t\t\t\t\t\ttémoignages.",
     "De nombreuses personnes m'ont fait confiance au fil des années. Voici quelques retours\n\t\t\t\t\t\t\td'expérience, partagés avec leur accord. <strong>Chaque situation étant unique, ces\n\t\t\t\t\t\t\ttémoignages relatent des parcours individuels : ils ne constituent pas une promesse ni une\n\t\t\t\t\t\t\tgarantie de résultat.</strong>", 1),
    ("temoignages.html",
     "Suite aux divers rituels effectués pour la résolution de mes problèmes, j'ai finalement trouvé satisfaction. Toutes les prédictions reçues se sont réalisées. Aujourd'hui, je suis heureux.",
     "Suite à la consultation et aux rituels effectués, j'ai trouvé un apaisement. La plupart des orientations reçues se sont révélées justes. Aujourd'hui, je vais mieux.", 1),
    ("temoignages.html",
     "Grâce à ce Voyant Féticheur, ma femme est revenue à la maison après 5 jours de travaux, j'ai été désenvoûté, j'ai repris mon travail et tout est rentré dans l'ordre.",
     "Grâce à cet accompagnement, j'ai retrouvé un meilleur équilibre : ma femme est revenue à la maison, j'ai repris mon travail et les choses se sont apaisées. Ce qui a fonctionné pour moi reste propre à mon histoire.", 1),
    ("temoignages.html",
     "mon ex est redevenu l'élu de mon cœur grâce à un maître marabout vaudou qui a vraiment fait un miracle dans ma vie.",
     "mon ex est redevenu l'élu de mon cœur, et j'ai surtout retrouvé la paix du cœur grâce à l'accompagnement de ce maître marabout vaudou.", 1),
]

# (fichier, motif regex, remplacement, occurrences attendues)
REGEX = [
    ("retouraffection.html",
     r"En dehors des puissants rituels de retour d['’]affection.*?envoutée\.",
     "Selon la tradition, l’accompagnement commence toujours par une consultation : j’étudie votre situation, votre histoire et vos intentions avant de vous proposer un travail personnalisé. Le <strong>bocio à deux têtes</strong> — une femme et un homme réunis en une seule statuette — est un objet symbolique de la tradition vaudou, façonné avec des éléments et des formules anciennes. On y associe le nom, la date de naissance et les souhaits de la personne concernée, dans un cadre rituel et symbolique. Ces pratiques relèvent de la tradition et de la symbolique : elles ne sont ni une promesse de résultat, ni une contrainte exercée sur la volonté de quelqu’un.", 1),
    ("rituel.html",
     r"Le pacte avec la Reine des eaux est en effet une alliance entre un individu et ce génie pour demander des faveurs \(richesse et puissance\)\..*?votre richesse\.",
     "Le pacte avec la Reine des eaux est, dans la tradition vaudou, une alliance symbolique entre un individu et ce génie. Il s’inscrit dans un cadre culturel et spirituel : il ne s’agit en aucun cas d’une promesse d’enrichissement, et aucun résultat matériel ne peut être garanti. Cet accompagnement n’apporte aucune garantie financière et ne remplace pas un conseil financier ou juridique.", 1),
    ("justice-proces.html",
     r"Après étude de votre dossier par l['’]oracle du Fa.*?laisser le temps aux travaux d['’]agir\.",
     "Après étude de votre situation par l'oracle du Fa, je réalise les rituels adaptés — apaisement, sérénité, protection — et je vous prépare pour le jour J avec les produits de chance appropriés. Cet accompagnement est d'ordre spirituel et symbolique : il ne remplace en aucun cas l'avis et le travail d'un avocat, et ne garantit aucune décision de justice. Contactez-moi <strong>le plus tôt possible avant l'audience</strong>.", 1),
    ("diversproduit.html",
     r'<li><i class="fa fa-check-circle" style="color:green;"></i> Retour d[\'’]affection en trois\s*jours</li>',
     '<li><i class="fa fa-check-circle" style="color:green;"></i> <a href="retouraffection.html">Accompagnement retour d’affection</a></li>', 1),
]

# appliques a TOUS les fichiers HTML
GLOBAL_REPLACEMENTS = [
    ("Produits très efficace et moins coûteux", "Produits traditionnels à petit prix"),
    ("bague magique en argent", "bague traditionnelle en argent"),
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
                continue  # deja applique lors d'une execution precedente
            problems.append(f"[COUNT] {fname}: attendu {expected}, trouvé {found} -> {old[:60]!r}")
            continue
        cache[fname] = html.replace(old, new)

    for fname, pattern, new, expected in REGEX:
        html = read(fname)
        found = len(re.findall(pattern, html, flags=re.DOTALL))
        if found != expected:
            if found == 0 and new[:60] in html:
                continue  # deja applique
            problems.append(f"[COUNT-RE] {fname}: attendu {expected}, trouvé {found} -> {pattern[:60]!r}")
            continue
        cache[fname] = re.sub(pattern, lambda m: new, html, flags=re.DOTALL)

    for fname in sorted(ROOT.glob("*.html")):
        html = cache.get(fname.name, fname.read_text(encoding="utf-8"))
        for old, new in GLOBAL_REPLACEMENTS:
            html = html.replace(old, new)
        (ROOT / fname).write_text(html, encoding="utf-8")

    print(f"Fichiers mis à jour : {len(cache)}")
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    print("OK : tous les remplacements ciblés ont été appliqués.")


if __name__ == "__main__":
    main()
