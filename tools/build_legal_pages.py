#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genere les 3 pages obligatoires Google Ads :
  - mentions-legales.html
  - politique-confidentialite.html
  - cgu.html
Le squelette (head + header + footer) est repris d'une page existante
pour garder exactement la meme navigation et le meme design.
"""
from pathlib import Path

ROOT = Path("/home/user/sidibe")
TPL = ROOT / "conseil-preparer-consultation.html"
SITE = "https://maitresalifou.com"
UPDATE = "10 septembre 2026"

tpl = TPL.read_text(encoding="utf-8")
footer_at = tpl.index('<footer class="footer"')
head_tpl = tpl[:tpl.index("</header>") + len("</header>")]
footer_tpl = tpl[footer_at:]

# bloc flottant WhatsApp (identique au reste du site)
wa_start = tpl.rindex('<a href="https://wa.me/', 0, footer_at)
wa_end = tpl.index("</a>", wa_start) + len("</a>")
wa_block = tpl[wa_start:wa_end]


def page(title, description, h1, crumb, content, filename):
    head = head_tpl
    head = head.replace(
        "<title>Bien Préparer sa Consultation de Voyance | Blog SIDIBE Salifou</title>",
        f"<title>{title}</title>")
    head = head.replace(
        '<meta name="description" content="Conseil du Maître : 5 conseils pour bien préparer votre consultation de voyance — question claire, informations, honnêteté. Sur place à Adja ou à distance.">',
        f'<meta name="description" content="{description}">')
    head = head.replace(
        '<meta property="og:title" content="Bien Préparer sa Consultation de Voyance | Blog SIDIBE Salifou">',
        f'<meta property="og:title" content="{title}">')
    head = head.replace(
        '<meta property="og:description" content="Conseil du Maître : 5 conseils pour bien préparer votre consultation de voyance — question claire, informations, honnêteté. Sur place à Adja ou à distance.">',
        f'<meta property="og:description" content="{description}">')
    head = head.replace(
        '<meta property="og:image" content="assets/img/voyance-fa.jpg">',
        '<meta property="og:image" content="assets/img/hero-area.jpg">')
    head = head.replace(
        '<meta property="og:image:alt" content="Bien Préparer sa Consultation de Voyance | Blog SIDIBE Salifou">',
        f'<meta property="og:image:alt" content="{title}">')
    head = head.replace(
        '<meta name="twitter:title" content="Bien Préparer sa Consultation de Voyance | Blog SIDIBE Salifou">',
        f'<meta name="twitter:title" content="{title}">')
    head = head.replace(
        '<meta name="twitter:description" content="Conseil du Maître : 5 conseils pour bien préparer votre consultation de voyance — question claire, informations, honnêteté. Sur place à Adja ou à distance.">',
        f'<meta name="twitter:description" content="{description}">')
    head = head.replace(
        '<meta name="twitter:image" content="assets/img/voyance-fa.jpg">',
        '<meta name="twitter:image" content="assets/img/hero-area.jpg">')

    body = f"""
	<section class="hero-area breadcrumb-area">
		<div class="container">
			<div class="row">
				<div class="col-lg-12">
					<div class="hero-area-content">
						<h1>{h1}</h1>
						<ul>
							<li><a href="index.html">Accueil</a></li>
							<li><a href="{filename}">{crumb}</a></li>
						</ul>
					</div>
				</div>
			</div>
		</div>
	</section>
	<section class="blog-detail" id="legal">
		<div class="container">
			<div class="row">
				<div class="col-lg-10 col-lg-offset-1">
					<div class="blog-details">
						<div style="background:#f7f7f7;border-left:5px solid #0074da;padding:18px 22px;margin-bottom:30px;">
							<strong><i class="fa fa-exclamation-triangle"></i> Avertissement légal :</strong>
							les consultations de voyance et conseils spirituels sont proposés à titre indicatif
							et ne remplacent en aucun cas un avis médical, juridique ou financier.
							<strong>Aucun résultat ne peut être garanti à 100 %.</strong>
						</div>
{content}
						<p><em>Dernière mise à jour : {UPDATE}</em></p>
					</div>
				</div>
			</div>
		</div>
	</section>
	{wa_block}
"""
    html = head + body + footer_tpl
    (ROOT / filename).write_text(html, encoding="utf-8")
    print(f"écrit : {filename}")


def h4(t):
    return f"\t\t\t\t\t\t<p><h4>{t}</h4></p>\n"


def p(t):
    return f"\t\t\t\t\t\t<p>{t}</p>\n"


# ------------------------------------------------------------------ mentions légales
mentions = ""
mentions += h4("1. Éditeur du site")
mentions += p(
    "Le site <strong>maitresalifou.com</strong> est édité par <strong>M. SIDIBE Salifou</strong>, "
    "praticien exerçant une activité de consultation de voyance, de conseil et d'accompagnement "
    "traditionnel et spirituel, à titre individuel.")
mentions += """						<p>
							<ul>
								<li><i class="fa fa-check-circle" style="color:green;"></i> <strong>Nom commercial :</strong> Marabout Voyant SIDIBE Salifou</li>
								<li><i class="fa fa-check-circle" style="color:green;"></i> <strong>Adresse :</strong> Adja, République du Bénin</li>
								<li><i class="fa fa-check-circle" style="color:green;"></i> <strong>Téléphone / WhatsApp :</strong> <a href="tel:+2290196873373">+229 01 96 87 33 73</a></li>
								<li><i class="fa fa-check-circle" style="color:green;"></i> <strong>E-mail :</strong> <em>[à compléter : adresse e-mail de contact]</em></li>
								<li><i class="fa fa-check-circle" style="color:green;"></i> <strong>Immatriculation :</strong> entreprise individuelle établie en République du Bénin — <em>[à compléter : n° IFU / registre de commerce]</em></li>
								<li><i class="fa fa-check-circle" style="color:green;"></i> <strong>Directeur de la publication :</strong> M. SIDIBE Salifou</li>
							</ul>
						</p>
"""
mentions += h4("2. Hébergeur")
mentions += p(
    "Le site est hébergé par <strong>GitHub, Inc.</strong> (service GitHub Pages) — 88 Colin P. Kelly Jr. Street, "
    "San Francisco, CA 94107, États-Unis. L'hébergeur assure la mise à disposition technique du site ; "
    "il n'intervient pas sur le contenu des consultations.")
mentions += h4("3. Nature de l'activité")
mentions += p(
    "Les prestations proposées sont des <strong>consultations de voyance, des conseils et des accompagnements "
    "d'ordre traditionnel, spirituel et symbolique</strong>, ainsi que la préparation et l'envoi de produits "
    "rituels (bagues, savons, parfums, talismans). Elles relèvent du domaine divinatoire et du bien-être "
    "personnel : elles ont une visée d'accompagnement, de réflexion et de divertissement.")
mentions += """						<div style="background:#fff3cd;border-left:5px solid #e6a200;padding:15px;margin:20px 0;">
							<strong><i class="fa fa-exclamation-triangle"></i> Important :</strong> les consultations ne
							constituent en aucun cas un acte médical, paramédical, juridique ou financier. Aucune
							prestation n'est remboursée par un organisme de santé ou d'assurance. En cas de problème
							médical, psychologique, juridique ou financier, consultez un professionnel qualifié.
						</div>
"""
mentions += h4("4. Propriété intellectuelle")
mentions += p(
    "L'ensemble des contenus présents sur ce site (textes, photographies, illustrations, logo, mise en page) "
    "est protégé par le droit de la propriété intellectuelle. Toute reproduction ou représentation, totale ou "
    "partielle, sans autorisation écrite préalable est interdite.")
mentions += h4("5. Données personnelles et cookies")
mentions += p(
    "Les informations relatives à la collecte et au traitement de vos données personnelles sont détaillées dans "
    "la <a href=\"politique-confidentialite.html\">politique de confidentialité</a>.")
mentions += h4("6. Liens externes")
mentions += p(
    "Le site renvoie vers des services tiers (WhatsApp, Google Maps). Je ne suis pas responsable du contenu, "
    "des conditions d'utilisation ni des politiques de confidentialité de ces services.")
mentions += h4("7. Limitation de responsabilité")
mentions += p(
    "Les informations publiées sur ce site sont fournies à titre indicatif. Aucune garantie n'est donnée quant "
    "à un résultat quelconque : chaque situation est singulière et les prestations proposées ne constituent "
    "ni une promesse, ni une garantie de résultat.")
mentions += h4("8. Droit applicable et règlement des litiges")
mentions += p(
    "Les présentes mentions sont soumises au droit en vigueur en République du Bénin. En cas de litige, une "
    "solution amiable sera recherchée en priorité en me contactant au +229 01 96 87 33 73. À défaut d'accord, "
    "le litige pourra être porté devant les juridictions compétentes. Les consommateurs résidant dans "
    "l'Union européenne peuvent également recourir gratuitement à la plateforme européenne de règlement en "
    "ligne des litiges : <a href=\"https://ec.europa.eu/consumers/odr/\" target=\"_blank\" rel=\"noopener\">"
    "https://ec.europa.eu/consumers/odr/</a>.")

page(
    "Mentions légales | Marabout SIDIBE Salifou",
    "Mentions légales du site maitresalifou.com : identité de l'éditeur SIDIBE Salifou, hébergeur GitHub Pages, nature des prestations, propriété intellectuelle et droit applicable.",
    "Mentions légales",
    "Mentions légales",
    mentions,
    "mentions-legales.html",
)

# --------------------------------------------------- politique de confidentialité
priv = ""
priv += h4("1. Responsable du traitement")
priv += p(
    "Le responsable du traitement des données collectées sur ce site est <strong>M. SIDIBE Salifou</strong>, "
    "Adja, République du Bénin, joignable au <a href=\"tel:+2290196873373\">+229 01 96 87 33 73</a> "
    "(appel ou WhatsApp) et à l'adresse e-mail <em>[à compléter]</em>.")
priv += h4("2. Données que je collecte")
priv += """						<p>
							<ul>
								<li><i class="fa fa-check-circle" style="color:green;"></i> <strong>Données que vous m'envoyez volontairement</strong>
									par WhatsApp, téléphone ou e-mail : nom, prénom, numéro de téléphone, date de naissance,
									photos, et le contenu des messages relatifs à votre demande de consultation.</li>
								<li><i class="fa fa-check-circle" style="color:green;"></i> <strong>Données de commande</strong> (produits rituels) :
									adresse de livraison et informations nécessaires à l'envoi.</li>
								<li><i class="fa fa-check-circle" style="color:green;"></i> <strong>Données techniques</strong> : adresse IP, type de navigateur,
									pages consultées (statistiques d'hébergement GitHub Pages).</li>
							</ul>
						</p>
"""
priv += h4("3. Finalités et bases légales")
priv += """						<p>
							<ul>
								<li><i class="fa fa-check-circle" style="color:green;"></i> Répondre à vos demandes et réaliser la consultation demandée (exécution du contrat).</li>
								<li><i class="fa fa-check-circle" style="color:green;"></i> Préparer, expédier et assurer le suivi des produits commandés (exécution du contrat).</li>
								<li><i class="fa fa-check-circle" style="color:green;"></i> Assurer la sécurité du site et prévenir les abus (intérêt légitime).</li>
							</ul>
						</p>
"""
priv += h4("4. Destinataires")
priv += p(
    "Vos données sont traitées par moi seul. Elles peuvent toutefois transiter par des prestataires techniques : "
    "<strong>Meta (WhatsApp)</strong> pour les échanges de messages, <strong>GitHub, Inc.</strong> pour "
    "l'hébergement du site, <strong>Google (Google Maps)</strong> pour la carte affichée sur la page contact, "
    "ainsi que le transporteur chargé de la livraison des produits.")
priv += h4("5. Durée de conservation")
priv += p(
    "Les échanges relatifs à une consultation sont conservés le temps nécessaire au suivi de votre dossier, "
    "puis supprimés. Les éléments de commande sont conservés pendant la durée légale applicable aux obligations "
    "comptables et commerciales.")
priv += h4("6. Cookies")
priv += p(
    "Ce site ne dépose <strong>aucun cookie publicitaire ni traceur de ciblage</strong>. Seuls des cookies "
    "strictement nécessaires au fonctionnement du site et de mémorisation de votre choix en matière de cookies "
    "sont susceptibles d'être utilisés. Vous pouvez à tout moment paramétrer ou supprimer les cookies depuis "
    "les réglages de votre navigateur.")
priv += h4("7. Vos droits")
priv += p(
    "Conformément à la réglementation applicable en matière de protection des données (et au RGPD pour les "
    "personnes situées dans l'Union européenne), vous disposez d'un droit d'accès, de rectification, "
    "d'effacement, de limitation, d'opposition et, le cas échéant, de portabilité de vos données. Il vous suffit "
    "de m'en faire la demande par WhatsApp au +229 01 96 87 33 73 ou par e-mail.")
priv += h4("8. Sécurité")
priv += p(
    "Des mesures techniques et organisationnelles raisonnables sont mises en œuvre pour protéger vos données "
    "contre la perte, l'accès non autorisé ou la divulgation. Le site est servi exclusivement en HTTPS.")
priv += h4("9. Mineurs")
priv += p(
    "Les prestations s'adressent aux personnes majeures. Les mineurs doivent obtenir l'accord d'un parent ou "
    "d'un tuteur.")
priv += h4("10. Modification de la présente politique")
priv += p(
    "Cette politique peut être mise à jour. La date de dernière mise à jour est indiquée en bas de page.")

page(
    "Politique de confidentialité | Marabout SIDIBE Salifou",
    "Politique de confidentialité de maitresalifou.com : données collectées (WhatsApp, commandes), finalités, destinataires, cookies, durées de conservation et exercice de vos droits.",
    "Politique de confidentialité",
    "Confidentialité",
    priv,
    "politique-confidentialite.html",
)

# -------------------------------------------------------------------------- CGU
cgu = ""
cgu += h4("1. Objet et acceptation")
cgu += p(
    "Les présentes conditions générales d'utilisation et de vente (CGU/CGV) régissent l'utilisation du site "
    "maitresalifou.com ainsi que les prestations de consultation et les commandes de produits proposés par "
    "<strong>M. SIDIBE Salifou</strong>. Toute commande ou demande de consultation implique l'acceptation "
    "pleine et entière des présentes conditions.")
cgu += h4("2. Nature des prestations")
cgu += p(
    "Sont proposés : des <strong>consultations de voyance</strong> (oracle du Fa), des <strong>conseils et "
    "accompagnements traditionnels et spirituels</strong>, ainsi que des <strong>produits rituels</strong> "
    "(bagues, savons, parfums, talismans, etc.).")
cgu += """						<div style="background:#fff3cd;border-left:5px solid #e6a200;padding:15px;margin:20px 0;">
							<strong><i class="fa fa-exclamation-triangle"></i> Avertissement :</strong> les consultations
							de voyance et conseils spirituels sont proposés à titre indicatif, dans un but
							d'accompagnement, de réflexion et de divertissement. Ils ne remplacent en aucun cas un avis
							médical, psychologique, juridique ou financier. <strong>Aucun résultat ne peut être garanti
							à 100 %.</strong> Aucune prestation ne vise à nuire à autrui.
						</div>
"""
cgu += h4("3. Demande de consultation")
cgu += p(
    "La demande s'effectue par WhatsApp ou par téléphone au +229 01 96 87 33 73. Avant toute prestation, "
    "j'indique <strong>la nature de l'accompagnement proposé, les modalités (sur place ou à distance), le "
    "tarif et les délais</strong>. Aucun travail n'est engagé sans votre accord explicite sur ces éléments.")
cgu += h4("4. Tarifs et paiement")
cgu += p(
    "Les tarifs sont communiqués en francs CFA (XOF) ou en euros avant validation de la prestation. Le paiement "
    "s'effectue selon les moyens convenus lors de l'échange. Aucun paiement n'est exigé sans que la prestation "
    "et son prix aient été clairement annoncés au préalable.")
cgu += h4("5. Produits : commande, préparation et livraison")
cgu += """						<p>
							<ul>
								<li><i class="fa fa-check-circle" style="color:green;"></i> Les produits rituels sont <strong>préparés de façon personnalisée</strong> après commande (par exemple : 3 jours pour une bague).</li>
								<li><i class="fa fa-check-circle" style="color:green;"></i> Les délais de livraison sont indicatifs et dépendent du transporteur et du pays de destination.</li>
								<li><i class="fa fa-check-circle" style="color:green;"></i> Les produits personnalisés et préparés à la commande <strong>ne peuvent ni être repris ni être échangés</strong>.</li>
							</ul>
						</p>
"""
cgu += h4("6. Droit de rétractation")
cgu += p(
    "Conformément aux usages du commerce en ligne, vous disposez d'un délai de <strong>14 jours</strong> à "
    "compter de la réception pour vous rétracter sur les <em>produits non personnalisés</em>. S'agissant des "
    "prestations de services, la rétractation n'est plus possible dès lors que la prestation a été réalisée "
    "avec votre accord préalable exprès.")
cgu += h4("7. Obligations du client")
cgu += """						<p>
							<ul>
								<li><i class="fa fa-check-circle" style="color:green;"></i> Être majeur, ou disposer de l'accord d'un représentant légal.</li>
								<li><i class="fa fa-check-circle" style="color:green;"></i> Fournir des informations exactes et complètes.</li>
								<li><i class="fa fa-check-circle" style="color:green;"></i> Ne pas solliciter de prestation visant à nuire, à contraindre ou à porter atteinte à la liberté d'une personne.</li>
								<li><i class="fa fa-check-circle" style="color:green;"></i> Ne pas utiliser les consultations à la place d'un avis médical, juridique ou financier professionnel.</li>
							</ul>
						</p>
"""
cgu += h4("8. Responsabilité")
cgu += p(
    "J'exécute les prestations avec sérieux, écoute et confidentialité. La responsabilité ne saurait être "
    "engagée à raison d'un résultat attendu non atteint, les prestations étant d'ordre spirituel, symbolique "
    "et indicatif, ni en cas d'informations inexactes fournies par le client ou d'événement indépendant de ma "
    "volonté (retard de transport, indisponibilité du réseau, etc.).")
cgu += h4("9. Confidentialité")
cgu += p(
    "Toutes les informations échangées lors d'une consultation sont couvertes par la confidentialité et le "
    "secret professionnel, et traitées conformément à la "
    "<a href=\"politique-confidentialite.html\">politique de confidentialité</a>.")
cgu += h4("10. Droit applicable et litiges")
cgu += p(
    "Les présentes conditions sont soumises au droit en vigueur en République du Bénin. En cas de différend, "
    "je vous invite à me contacter en priorité au +229 01 96 87 33 73 afin de rechercher une solution amiable. "
    "À défaut, le litige pourra être porté devant les juridictions compétentes ; les consommateurs de "
    "l'Union européenne peuvent recourir à la plateforme "
    "<a href=\"https://ec.europa.eu/consumers/odr/\" target=\"_blank\" rel=\"noopener\">"
    "https://ec.europa.eu/consumers/odr/</a>.")

page(
    "Conditions générales d'utilisation et de vente | Marabout SIDIBE Salifou",
    "CGU et CGV de maitresalifou.com : nature des prestations de voyance et conseil, tarifs, commande, livraison, rétractation, responsabilité et droit applicable.",
    "Conditions générales d'utilisation et de vente",
    "CGU / CGV",
    cgu,
    "cgu.html",
)
