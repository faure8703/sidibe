# Mise en conformité Google Ads — maitresalifou.com

Travaux réalisés le **10 septembre 2026** sur les 28 pages du site pour réduire les risques de refus
d'annonce et de suspension de compte (motifs « Contournement des systèmes », « Pratiques trompeuses »,
« Site compromis »).

---

## 1. Nettoyage du contenu (promesses et signaux à risque)

### Promesses de résultat supprimées

| Page | Avant | Après |
|---|---|---|
| `retouraffection.html` | Titre « Retour d'Affection **Rapide & Efficace** », H1 « … avec **résultat en 7 jours** », « rituels qui amènent l'être désiré **en 7 jours** », « emprise et **obsession aveugle** », « jeter un sort » | « Retour d'Affection : Consultation & Accompagnement », H1 « écoute, consultation et accompagnement personnalisé », bocio présenté comme objet **symbolique**, mention explicite : ni promesse de résultat, ni contrainte sur la volonté |
| `bague.html` | « **Satisfaction garantie 100 %** », « attire la richesse », « transformé des mendiants en rois en 7 semaines », « vos affaires fleuriront » | Symbole traditionnel de chance/protection, « **Aucun résultat — financier ou autre — ne peut être garanti** » |
| `rituel.html` | « gloire, **richesse** et puissance », « on a droit à **toutes les richesses terrestres** » | Alliance **symbolique** dans la tradition vaudou, « aucune promesse d'enrichissement » |
| `index.html` | « la solution **rapide et efficace** à tous vos problèmes », « vous **garantit** un travail de qualité », « jusqu'à **satisfaction** » | « écoute attentive, diagnostic et accompagnement personnalisé », « suivi personnalisé et confidentiel, **sans promesse de résultat** » |
| `consultation-voyance.html` | « Réponse **en 24-48h** » | « Réponse rapide, **généralement** sous 48 heures » |
| `temoignages.html` | « Avis clients **vérifiés** », « **Toutes** les prédictions se sont réalisées », « ma femme est revenue après **5 jours de travaux** », « un **miracle** » | « Retours d'expérience », parcours individuels, encadré : « ne constituent pas une promesse ni une garantie de résultat » |
| `guide-consultation-faq.html` | FAQ délais sans réserve | Ajout : « **Aucun résultat ne peut être garanti à 100 % : la voyance n'est pas une science exacte** » |
| `maitre-sidibe.html` | « marabout honnête, professionnel, **efficace** », « élu marabout de l'année… » | « à l'écoute, professionnel et discret », reconnaissance par ses pairs |
| `diversproduit.html` / `fertilite-famille.html` | Listes de pathologies (épilepsie, drépanocytose, ulcères, hypertension, impuissance…), « stérilité », « retour d'affection en 3 jours », « recette pour faire un garçon », « pour empêcher une femme de sortir », « gain facile / jeu de hasard » | Reformulation en « accompagnement », « soutien moral », « médiation dans le couple », suppression de tout argumentaire médical, de sélection du sexe, de coercition et de gain d'argent |
| `justice-proces.html` | « **faveur** devant le juge », « rituels de faveur » | « Sérénité & Apaisement », « ne remplace en aucun cas l'avis et le travail d'un avocat, et ne garantit aucune décision de justice » |
| `protection-desenvoutement.html`, `savons-parfums.html`, `index.html`, `diversproduit.html` | « **retour à l'envoyeur** », « renvoyer le mal à son envoyeur », « contre-attaques » (services laissant croire à un acte destiné à nuire) | « protection et purification », « purifier votre environnement », « protection du foyer » |
| `mari-femme-nuit.html` | « chasser **définitivement** », « discrétion totale **garantie** » | « travailler symboliquement sur la rupture des liens », « discrétion totale » |
| `clientele-commerce.html` | « suivi de vos **résultats** » | « suivi régulier » |

> Les mentions « les rituels ne sont jamais réalisés dans le but de nuire à autrui », déjà présentes, ont été conservées.

### Avertissement légal

Un encadré **« Avertissement légal »** est affiché sur **les 28 pages**, juste au-dessus du pied de page :

> Les consultations de voyance et conseils spirituels sont proposés à titre indicatif et ne remplacent en
> aucun cas un avis médical, juridique ou financier. **Aucun résultat ne peut être garanti à 100 %.**

---

## 2. Pages obligatoires créées

| Page | Contenu |
|---|---|
| `mentions-legales.html` | Identité de l'éditeur (SIDIBE Salifou, Adja, Bénin), contact, **hébergeur GitHub Pages**, nature de l'activité, avertissement, propriété intellectuelle, limitation de responsabilité, droit applicable et règlement des litiges |
| `politique-confidentialite.html` | Données collectées (WhatsApp, commandes, données techniques), finalités, bases légales, destinataires (Meta, GitHub, Google, transporteur), durées, **cookies**, droits des personnes, sécurité, mineurs |
| `cgu.html` | CGU/CGV : objet, nature des prestations, avertissement, demande de consultation, tarifs, préparation/livraison des produits, droit de rétractation (14 j sur les produits non personnalisés), obligations du client, responsabilité, confidentialité, litiges |

Elles sont liées **en pied de page de chaque page** du site et référencées dans `sitemap.xml`.

### À compléter (obligatoire pour que les mentions légales soient valables)

- **Adresse e-mail de contact** : `[à compléter : adresse e-mail de contact]` (2 occurrences, mentions légales + politique de confidentialité)
- **Immatriculation** : `[à compléter : n° IFU / registre de commerce]` (mentions légales)

> Ces modèles couvrent les exigences habituelles d'un site francophone. Faites-les relire par un
> professionnel du droit (Bénin + droit de la consommation français/européen si vous visez la France).

---

## 3. Intégrité technique

| Point | État |
|---|---|
| HTTPS | Site servi par GitHub Pages (IP `185.199.109.x`) ; `http://` redirige vers `https://`. À vérifier : **Enforce HTTPS** doit être coché dans *Settings → Pages* du dépôt |
| Contenu mixte | **0 ressource en `http://`** : toutes les images, CSS, JS et iframes sont en relatif ou en `https://` |
| Scripts externes | Suppression de l'ancien bloc IE `oss.maxcdn.com` (domaine hors service, présent sur 25 pages) |
| Liens WhatsApp | Tous en `https://wa.me/2290196873373` — pas de redirecteur intermédiaire, pas d'URL masquée |
| HTML | **0 anomalie de structure** sur les 28 pages (vérifié : `</div>` surnuméraires corrigés sur 7 pages, imbrications `<p>` invalides corrigées sur `bague.html` et `rituel.html`) |
| Liens internes | **0 lien cassé** |
| `sitemap.xml` | 28 URL, désormais en **URL absolues** `https://maitresalifou.com/…` (elles étaient relatives donc invalides) |
| `robots.txt` | `Sitemap:` en URL absolue |
| Canonical | `<link rel="canonical">` ajouté sur chaque page |
| Referrer | `<meta name="referrer" content="strict-origin-when-cross-origin">` |
| Cookies | Bandeau d'information (`assets/js/cookie-notice.js`) : aucun cookie publicitaire n'est déposé, choix mémorisé en `localStorage` |

Le site est **statique (GitHub Pages)** : il n'y a ni WordPress, ni extension, ni thème, ni base de
données — donc pas d'injection de type « site compromis » côté serveur d'application.

---

## 4. Reste à faire avant de lancer les campagnes (à la main)

1. **Compléter** l'e-mail et le numéro d'immatriculation dans les mentions légales.
2. **Passer un scanner externe** : [Sucuri SiteCheck](https://sitecheck.sucuri.net/),
   [VirusTotal](https://www.virustotal.com/gui/home/url), puis **Google Search Console**
   (rapport « Problèmes de sécurité » et « État du sitemap »).
3. **Vérifier l'alignement annonce ↔ page d'atterrissage** : si l'annonce parle d'« écoute » ou de
   « guidance », pointez vers une page qui parle bien de consultation/conseil (par ex.
   `consultation-voyance.html` ou `guide-consultation-faq.html`) et non vers une page produit.
4. **Éviter** dans les annonces : « résultat garanti », « retour de l'être aimé », « en 24h/48h »,
   « 100 % efficace », « riche », « guérison ». Préférer « consultation », « écoute », « conseil »,
   « guidance », « voyance ».
5. **Vérifier le ciblage** : les services de voyance / ésotérisme soumis à restrictions dans certains
   pays peuvent nécessiter une **demande de certification Google Ads** avant diffusion. À vérifier dans
   l'aide Google Ads pour chaque pays visé (France, Belgique, Suisse, Bénin…).
6. **Activer « Enforce HTTPS »** dans les paramètres GitHub Pages du dépôt.
7. **Soumettre** le sitemap dans Google Search Console après la mise en ligne.

---

## 5. Reproductibilité

Les scripts utilisés sont conservés dans `tools/` :

- `tools/clean_content.py` — remplacements de contenu (vérifiés, idempotents)
- `tools/clean_content_2.py` — suppression des signaux à risque restants
- `tools/build_legal_pages.py` — génération des 3 pages légales
- `tools/inject_legal.py` — injection de l'avertissement, des liens légaux, du canonical et du bandeau cookies
