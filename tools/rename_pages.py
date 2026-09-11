#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mise en conformite Google Ads - renommage / nettoyage de deux pages :
  cadenas-amour.html            -> lien-amoureux.html
  conseil-signes-envoutement.html -> conseil-baisse-energie.html

Les anciens fichiers deviennent des pages de redirection (meta refresh + canonical).
Tous les liens internes, libelles de menu, sitemap.xml et search.js sont mis a jour.
"""
import io, os, re, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OLD1, NEW1 = "cadenas-amour.html", "lien-amoureux.html"
OLD2, NEW2 = "conseil-signes-envoutement.html", "conseil-baisse-energie.html"

WA1 = ("https://wa.me/2290196873373?text=Bonjour%20Ma%C3%AEtre%20SIDIBE%2C%20je%20viens%20de%20votre%20"
       "page%20Lien%20Amoureux%20et%20je%20souhaite%20des%20informations.")
WA2 = ("https://wa.me/2290196873373?text=Bonjour%20Ma%C3%AEtre%20SIDIBE%2C%20je%20viens%20de%20votre%20"
       "conseil%20sur%20la%20baisse%20d%27%C3%A9nergie%20et%20je%20souhaite%20un%20diagnostic.")
WA1_OLD = ("https://wa.me/2290196873373?text=Bonjour%20Ma%C3%AEtre%20SIDIBE%2C%20je%20viens%20de%20votre%20"
           "page%20Cadenas%20d%27Amour%20et%20je%20souhaite%20des%20informations.")
WA2_OLD = ("https://wa.me/2290196873373?text=Bonjour%20Ma%C3%AEtre%20SIDIBE%2C%20je%20viens%20de%20votre%20"
           "conseil%20sur%20les%20signes%20d%27envo%C3%BBtement%20et%20je%20souhaite%20un%20diagnostic.")

def read(p):
    with io.open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return f.read()

def write(p, s):
    with io.open(os.path.join(ROOT, p), "w", encoding="utf-8") as f:
        f.write(s)

# ---------------------------------------------------------------------------
# 1. Construction de la page Lien Amoureux a partir de l'ancienne
# ---------------------------------------------------------------------------
page1 = read(OLD1)

# --- balises head ---
page1 = page1.replace('<link rel="canonical" href="https://maitresalifou.com/cadenas-amour.html">',
                      '<link rel="canonical" href="https://maitresalifou.com/lien-amoureux.html">')
page1 = page1.replace(
    "<title>Cadenas d'Amour : Sceller votre Union | Praticien traditionnel SIDIBE Salifou</title>",
    "<title>Consolider le lien amoureux et l'harmonie du couple | Praticien traditionnel SIDIBE Salifou</title>")

DESC1_OLD = ("Cadenas d'amour du Praticien traditionnel SIDIBE Salifou : scellez votre union, renforcez la "
             "fidélité et sauvez votre foyer. Rituel personnalisé, discrétion totale.")
DESC1_NEW = ("Accompagnement traditionnel du praticien SIDIBE Salifou : reconstruire la confiance, renouer le "
             "dialogue et apaiser le foyer. Écoute personnalisée, discrétion totale.")
page1 = page1.replace(DESC1_OLD, DESC1_NEW)
page1 = page1.replace('content="Cadenas d\'Amour : Sceller votre Union | Praticien traditionnel SIDIBE Salifou"',
                      'content="Consolider le lien amoureux et l\'harmonie du couple | Praticien traditionnel SIDIBE Salifou"')

# --- contenu : titre, fil d'ariane, image, chapo ---
page1 = page1.replace(
    "<h1>Cadenas d'amour : un symbole d'engagement pour votre couple</h1>",
    "<h1>Consolider le lien amoureux et l'harmonie du couple</h1>")
page1 = page1.replace('<li><a href="cadenas-amour.html">Cadenas d\'Amour</a></li>',
                      '<li><a href="lien-amoureux.html">Lien Amoureux</a></li>')
page1 = page1.replace('<img src="assets/img/cadenas-amour.jpg" alt="Cadenas d\'amour">',
                      '<img src="assets/img/cadenas-amour.jpg" alt="Lien amoureux et complicité du couple">')
page1 = page1.replace(
    '<div class="post-author"><a href="#"><i class="icofont icofont-lock"></i>Union scellée, foyer protégé</a></div>',
    '<div class="post-author"><a href="#"><i class="icofont icofont-heart"></i>Confiance, dialogue et sérénité du foyer</a></div>')

BODY1_OLD = re.search(
    r"\t{6}<p>Quand l'amour est là.*?Comme tous mes travaux.*?</strong>\.</p>", page1, re.S).group(0)

BODY1_NEW = """						<p>Quand l'amour est là mais que tout semble vouloir vous éloigner — malentendus, jalousie,
							distance, routine — il reste presque toujours un chemin pour <strong>retrouver un terrain
							d'entente</strong>. Le praticien traditionnel et consultant spirituel
							<strong>SIDIBE Salifou</strong> vous reçoit pour un accompagnement personnalisé, à l'écoute
							de votre histoire et de votre couple.</p>
						<p><h4>Pour qui est fait cet accompagnement ?</h4></p>
						<p><ul>
							<li><i class="fa fa-check-circle" style="color:green;"></i> Couples traversant une période de doute ou d'éloignement</li>
							<li><i class="fa fa-check-circle" style="color:green;"></i> Conjoints qui souhaitent renouer le dialogue et apaiser les tensions</li>
							<li><i class="fa fa-check-circle" style="color:green;"></i> Après un <a href="retouraffection.html">retour d'affection</a> : consolider les bases retrouvées</li>
							<li><i class="fa fa-check-circle" style="color:green;"></i> Fiançailles et projets de mariage : préparer l'engagement avec sérénité</li>
						</ul></p>
						<p><h4>Comment se déroule l'accompagnement ?</h4></p>
						<p><ol>
							<li><strong>Consultation de l'oracle du Fa</strong> pour éclairer la situation et dégager des repères.</li>
							<li><strong>Échange personnalisé</strong> sur votre histoire, vos attentes et ce que chacun est prêt à mettre en œuvre.</li>
							<li><strong>Conseils traditionnels</strong> : gestes symboliques, périodes favorables, purification du foyer si vous le souhaitez.</li>
							<li><strong>Suivi et conseils</strong> pour entretenir la complicité au quotidien.</li>
						</ol></p>
						<p>Chaque accompagnement est unique : il se construit avec vous, à votre rythme.
							Il ne s'agit en aucun cas de contraindre la volonté ou le libre arbitre de l'autre :
							le respect de chaque personne est la première règle de ma pratique. Comme tous mes travaux,
							cet accompagnement respecte le code déontologique et reste couvert par le
							<strong>secret professionnel</strong>. <strong>Aucun résultat ne peut être garanti.</strong></p>"""
page1 = page1.replace(BODY1_OLD, BODY1_NEW)
page1 = page1.replace(WA1_OLD, WA1)
write(NEW1, page1)

# ---------------------------------------------------------------------------
# 2. Construction de la page Baisse d'énergie a partir de l'ancienne
# ---------------------------------------------------------------------------
page2 = read(OLD2)

page2 = page2.replace('<link rel="canonical" href="https://maitresalifou.com/conseil-signes-envoutement.html">',
                      '<link rel="canonical" href="https://maitresalifou.com/conseil-baisse-energie.html">')
page2 = page2.replace("<title>5 Signes d'Conseils de bien-être & Comment Réagir | Blog SIDIBE Salifou</title>",
                      "<title>5 signes de baisse d'énergie et de blocage émotionnel | Blog SIDIBE Salifou</title>")

DESC2_OLD = ("Conseil du Maître : 5 signes qui montrent que vous êtes envoûté — malchance, fatigue, cauchemars, "
             "disputes, blocages. Que faire ? Diagnostic et désenvoûtement.")
DESC2_NEW = ("Conseil du Maître : 5 signes de baisse d'énergie et de blocage émotionnel — fatigue, sommeil perturbé, "
             "moral en berne. Des repères pour comprendre et réagir avec calme.")
page2 = page2.replace(DESC2_OLD, DESC2_NEW)
page2 = page2.replace('content="5 Signes d\'Conseils de bien-être & Comment Réagir | Blog SIDIBE Salifou"',
                      'content="5 signes de baisse d\'énergie et de blocage émotionnel | Blog SIDIBE Salifou"')

page2 = page2.replace("<h1>5 signes souvent interprétés comme un envoûtement</h1>",
                      "<h1>5 signes de baisse d'énergie et de blocage émotionnel</h1>")
page2 = page2.replace('<li><a href="conseil-signes-envoutement.html">Signes d\'envoûtement</a></li>',
                      '<li><a href="conseil-baisse-energie.html">Baisse d\'énergie</a></li>')
page2 = page2.replace('<img src="assets/img/protection.jpg" alt="Signes d\'envoûtement">',
                      '<img src="assets/img/protection.jpg" alt="Signes de baisse d\'énergie">')

BODY2_OLD = re.search(r"\t{6}<p>Tout allait bien, puis plus rien ne marche.*?</p>\n\t{6}<p><a href=\"blog.html\">",
                      page2, re.S).group(0)  # noqa

BODY2_NEW = """						<p>Tout allait bien, puis plus rien ne marche ? Avant d'y voir une cause extérieure,
							observez ces <strong>5 signes</strong> que je rencontre le plus souvent chez mes consultants :</p>
						<p><ol>
							<li><strong>Les contretemps s'accumulent</strong> dans plusieurs domaines en même temps : travail, relations, projets.</li>
							<li><strong>Une fatigue qui ne passe pas</strong>, même après le repos, sans cause identifiée.</li>
							<li><strong>Un sommeil agité</strong> : réveils nocturnes, rêves intenses, impression de ne jamais récupérer.</li>
							<li><strong>Le moral qui baisse</strong> : irritabilité, envie de s'isoler, tensions avec des proches.</li>
							<li><strong>Un sentiment d'impasse</strong> : tout échoue au même stade (démarches, projets, engagements).</li>
						</ol></p>
						<p><h4>Que faire ? Surtout, ne paniquez pas</h4></p>
						<p>Un ou deux signes isolés ne prouvent rien : la vie a ses hauts et ses bas. Mais si
							<strong>plusieurs signes se cumulent depuis des semaines</strong>, le premier réflexe reste
							de consulter un <strong>professionnel de santé</strong> : l'avis médical ne se remplace pas.
							Vous pouvez aussi faire établir un <strong>diagnostic par l'oracle du Fa</strong>, qui apporte
							un éclairage symbolique et traditionnel sur la période que vous traversez. Ensuite, un
							accompagnement axé sur la <a href="protection-desenvoutement.html">protection et
							l'harmonisation</a> peut vous aider à retrouver calme, clarté d'esprit et paix intérieure.
							Décrivez-moi ce que vous ressentez sur WhatsApp, je vous réponds honnêtement.</p>
						<p><a href="blog.html">"""
page2 = page2.replace(BODY2_OLD, BODY2_NEW)
page2 = page2.replace(WA2_OLD, WA2)
write(NEW2, page2)

# ---------------------------------------------------------------------------
# 3. Anciennes URLs : pages de redirection
# ---------------------------------------------------------------------------
def redirect_page(old, new, titre):
    return """<!DOCTYPE HTML>
<html lang="fr">

<head>
\t<meta charset="UTF-8">
\t<meta name="robots" content="noindex, follow">
\t<link rel="canonical" href="https://maitresalifou.com/{new}">
\t<meta http-equiv="refresh" content="0; url={new}">
\t<title>Page déplacée — {titre}</title>
</head>

<body>
\t<p>Cette page a été déplacée. Si vous n'êtes pas redirigé automatiquement,
\t<a href="{new}">cliquez ici pour continuer vers « {titre} »</a>.</p>
\t<script>window.location.replace("{new}");</script>
</body>
</html>
""".format(new=new, titre=titre)

write(OLD1, redirect_page(OLD1, NEW1, "Lien Amoureux"))
write(OLD2, redirect_page(OLD2, NEW2, "5 signes de baisse d'énergie"))

# ---------------------------------------------------------------------------
# 4. Mise a jour de tous les liens / libelles dans le site
# ---------------------------------------------------------------------------
targets = [f for f in os.listdir(ROOT) if f.endswith(".html") and f not in (OLD1, OLD2)]
targets += ["sitemap.xml", os.path.join("assets", "js", "search.js")]

for f in targets:
    src = read(f)
    orig = src
    src = src.replace('href="%s"' % OLD1, 'href="%s"' % NEW1)
    src = src.replace('href="%s"' % OLD2, 'href="%s"' % NEW2)
    src = src.replace("Cadenas d'Amour", "Lien Amoureux")
    src = src.replace("cadenas d'amour", "lien amoureux")
    src = src.replace("cadenas-amour.html", NEW1)
    src = src.replace(OLD2, NEW2)
    if src != orig:
        write(f, src)
        print("mis a jour :", f)

# ---------------------------------------------------------------------------
# 5. Corrections de texte complementaires
# ---------------------------------------------------------------------------
blog = read("blog.html")
blog = blog.replace(
    '<img src="assets/img/protection.jpg" alt="Signes d\'envoûtement" style="margin-bottom:10px;">',
    '<img src="assets/img/protection.jpg" alt="Signes de baisse d\'énergie" style="margin-bottom:10px;">')
blog = blog.replace("<h4><a href=\"conseil-baisse-energie.html\">5 signes qui montrent que vous êtes envoûté</a></h4>",
                    "<h4><a href=\"conseil-baisse-energie.html\">5 signes de baisse d'énergie et de blocage émotionnel</a></h4>")
blog = blog.replace("<p>Malchance répétée, fatigue inexpliquée, cauchemars... Apprenez à reconnaître les signes d'un "
                    "envoûtement et découvrez que faire sans paniquer.</p>",
                    "<p>Fatigue, sommeil perturbé, sentiment d'impasse : apprenez à reconnaître les signes d'une baisse "
                    "d'énergie et découvrez comment réagir, avec calme et discernement.</p>")
blog = blog.replace("signes d'envoûtement, préparer sa consultation, protéger son commerce",
                    "baisse d'énergie, préparer sa consultation, protéger son commerce")
write("blog.html", blog)
print("mis a jour : blog.html (texte)")

hc = read("harmonie-couple.html")
hc = hc.replace("""éloignement des
							rivaux, et produits comme le <strong>cadenas d'amour</strong> ou le parfum pour être aimé,
							afin de sceller durablement votre union.""",
                """apaisement des
							tensions, soutiens symboliques et conseils personnalisés,
							afin de vous aider à consolider votre union à votre rythme.""")
write("harmonie-couple.html", hc)
print("mis a jour : harmonie-couple.html (texte)")

js = read(os.path.join("assets", "js", "search.js"))
js = js.replace('{ t: "Cadenas d\'Amour", u: "cadenas-amour.html", k: "cadenas amour union fidelite foyer sceller" }',
                '{ t: "Lien Amoureux", u: "lien-amoureux.html", k: "lien amoureux couple complicite confiance dialogue union" }')
js = js.replace('{ t: "Conseil : signes d\'envoûtement", u: "conseil-signes-envoutement.html", k: "signe envoutement malchance fatigue cauchemar blocage" }',
                '{ t: "Conseil : baisse d\'énergie", u: "conseil-baisse-energie.html", k: "baisse energie fatigue sommeil moral blocage emotionnel" }')
write(os.path.join("assets", "js", "search.js"), js)
print("mis a jour : assets/js/search.js (index de recherche)")

print("OK")
