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
   pays peuvent nécessiter une **demande de certification Google Ads** avant diffusion. Le ciblage visé
   étant **international**, la vérification doit être faite **pays par pays** dans l'aide Google Ads
   (France, Belgique, Suisse, Canada, Bénin, Côte d'Ivoire…), car les règles diffèrent fortement.
   ⚠️ **Corrigé le 11/09 : il n'existe aucune certification Google Ads pour la voyance / l'ésotérisme.**
   Les secteurs ouvrant droit à demande de certification sont le jeu, les produits financiers
   spéculatifs, les services d'endettement, la vente de billets, les documents et services
   gouvernementaux et les distributeurs de logiciels gratuits
   ([liste officielle](https://support.google.com/adspolicy/answer/16114090?hl=en)).
   Il n'y a donc **pas de voie administrative** à emprunter : la conformité du contenu est le seul levier.
6. **Activer « Enforce HTTPS »** dans les paramètres GitHub Pages du dépôt.
7. **Soumettre** le sitemap dans Google Search Console après la mise en ligne.

---

## 5. Reproductibilité

Les scripts utilisés sont conservés dans `tools/` :

- `tools/clean_content.py` — remplacements de contenu (vérifiés, idempotents)
- `tools/clean_content_2.py` — suppression des signaux à risque restants
- `tools/build_legal_pages.py` — génération des 3 pages légales
- `tools/inject_legal.py` — injection de l'avertissement, des liens légaux, du canonical et du bandeau cookies


---

## 6. Arbitrage sur le vocabulaire (« rituels », « magie », « maraboutage »)

Une recommandation fréquente consiste à **supprimer** les mots *rituel*, *magie*, *maraboutage* du site
pour les remplacer par *consultation*, *guidance*, *astrologie*, *tradition*, *écoute*.
**Cette consigne n'a été appliquée que partiellement, et volontairement.**

### Ce qui est retenu de cette recommandation

- Le vrai risque est bien **le site et les allégations qu'il porte**, pas les titres d'annonces
  (les nôtres — « Consultation Personnalisée », « Écoute & Conseils de Vie » — sont neutres).
- Les mots les plus « chargés » ont donc été **retirés** :
  *magie* / *magique* (hors 1 emploi figuré dans un article de blog), **vaudou (0 occurrence)**,
  **sorcellerie (0 occurrence)**, *Bague Magique* → *Bague Traditionnelle*,
  *Rituels & Produits* → *Traditions & Produits*, *Rituel Mami Wata* → *Tradition Mami Wata*
  (page `rituel.html` : titre « Mami Wata : Héritage & Symbolique », H1 « une tradition, son histoire
  et sa symbolique »).
- Sur les **4 pages les plus exposées** (`index.html`, `retouraffection.html`,
  `consultation-voyance.html`, `rituel.html`), « rituel » a été remplacé par
  *accompagnement*, *travail spirituel*, *tradition*, *pratiques traditionnelles*.
- Les **H1 porteurs de promesses** ont été corrigés sur tout le site
  (« provoquez votre réussite » → « préparez votre réussite » ; « faites prospérer vos affaires » ;
  « scellez votre union pour toujours » ; « devenir un Homme puissant, riche » ; etc.).
- La formule « des rituels sérieux pour **faire revenir l'être aimé** » (présente sur 23 pages) a été
  remplacée par « un accompagnement traditionnel et personnalisé de votre vie de couple ».

### Ce qui n'a volontairement PAS été fait

Supprimer **marabout** (294 occurrences), **voyance** (211) et **rituel** (202 restantes sur les pages
secondaires) reviendrait à renommer l'activité. Or :

- Google Ads sanctionne les **allégations** (résultat garanti, retour de l'ex, richesse, guérison),
  pas le vocabulaire d'une pratique déclarée.
  ⚠️ **Corrigé le 11/09 :** la « politique dédiée aux services ésotériques » citée ici **n'existe pas**.
  Le Règlement Google Ads compte 30 rubriques de contenu restreint (alcools, contrefaçon, crypto,
  rencontres, santé et médicaments, jeux, contenu sexuel…) et **aucune** rubrique ésotérisme/voyance
  ([Règlement Google Ads](https://support.google.com/adspolicy/answer/6008942?hl=fr)).
  Cela ne veut pas dire « activité libre » mais « **sans cadre dédié** » : l'activité est jugée
  entièrement par les règles générales de *Déclarations trompeuses ou déceptives*, qui s'appliquent
  à **l'annonce et à la destination**, donc au site.
- maquiller le maraboutage en « astrologie / guidance » constitue une **dissimulation de la nature de
  l'activité** → motif « **Contournement des systèmes** », le seul qui entraîne une suspension
  définitive du compte annonceur (et une pratique commerciale trompeuse au sens du droit français) ;
- côté SEO, ces termes sont exactement les requêtes qui font vivre le site.

### Recommandation complémentaire (à faire si les annonces sont refusées)

Si malgré tout une annonce est refusée au motif « allégations trompeuses », la meilleure réponse n'est
pas d'effacer le vocabulaire du site mais de **créer une page d'atterrissage dédiée**
(`consultation.html`) : vocabulaire « consultation, écoute, guidance, tradition », aucun produit,
ni témoignage chiffré, prix + déroulé + avertissement légal, CTA WhatsApp — puis d'y pointer les
annonces. L'alignement annonce ↔ page est assuré sans jamais dissimuler l'activité.

---

## 7. Incident du 11 septembre — « Éligible (diffusion limitée) / Allégations douteuses »

### Ce que Google a affiché

> « Supprimez du texte **et de la destination** de votre annonce toute déclaration trompeuse et toute
> fausse allégation concernant votre produit. »

L'annonce étant sobre (« consultation », « écoute »), le déclencheur était **la page d'accueil elle-même**.
Rappel de la règle appliquée — [Déclarations trompeuses : Allégations douteuses](https://support.google.com/adspolicy/answer/15936857?hl=fr) :
« faire des allégations inexactes ou des allégations **présentant comme probables certains résultats
improbables (même si les résultats annoncés sont possibles)** », plus le volet
« allégations liées aux méthodes pour s'enrichir » et l'exigence de clauses de non-responsabilité
**lorsque les témoignages insinuent que les résultats sont représentatifs**.

### Ce qui a été corrigé (scripts `tools/clean_content_4.py` et `tools/clean_content_5.py`)

**`index.html` — 15 correctifs**

| Élément | Avant | Après |
|---|---|---|
| Titre de bloc | « **Efficace** & Suivi » | « Suivi & Confidentialité » |
| Carte Mami Wata | « **Puissance & richesse** » / « concluent un **pacte** avec Mamy Wata » | « Tradition & Spiritualité » / récit ethnographique, « sans aucune promesse » |
| Carte Bague | « Chance & fortune », « symbole de chance », « préparée **en 3 jours** » | « Objet de tradition », « objet symbolique… ne promet aucun résultat, financier ou autre » |
| Carte Conseils relationnels | « **Faites revenir l'être aimé** et rétablissez l'harmonie… » (phrase en outre **cassée** par l'édition du 10/09 : « … grâce à des / un accompagnement ») | « espace d'écoute et de conseils relationnels… sans promesse de résultat » |
| Carte Chance & Emploi | « savons et parfums **de chance**, aide-mémoire, **réussite** » | « produits de tradition pour accompagner votre préparation, sans se substituer au travail ni au résultat » |
| Carte Justice | « mettez **toutes les chances** de votre côté » | « soutien moral, en complément du travail de votre avocat, jamais à sa place » |
| Carte Envoûtement | « **Malchance**, fatigue, **cauchemars**… » | « Fatigue, sommeil perturbé, sentiment de blocage : des repères pour comprendre » (registre de la peur écarté) |
| Intro témoignages | « L'**efficacité** de mes services a permis à de nombreuses personnes d'être satisfaites et de se réjouir de la **résolution** de leurs problèmes » | « Retours d'expérience… **parcours individuels**, ni promesse ni garantie » |
| Témoignage Smith Caven | « ma femme est revenue **après 5 jours de travaux**, j'ai été désenvoûté, j'ai repris mon travail » | écoute, cadre, « voir plus clair dans une période difficile » |
| Témoignage Noelie Price | « ce marabout… excellent voyant… ce qu'il m'a prédit… **parfaitement exact** » | échanges structurés, « m'a aidée à faire le point » |
| Témoignage Joana Cerbe | « il **ressent** ce que nous ressentons… il nous dit **toujours les justes choses**… la **solution** » | écoute, franchise, « reprendre pied » |
| Notes | 3 blocs d'**étoiles 5/5** | supprimés de l'accueil |
| Compteurs | « **Clients satisfaits** : 58 », « Produits commandés : 62 » | « Personnes accompagnées », « Produits préparés » |

**Pages liées depuis l'accueil — 8 correctifs** : H1 `justice-proces.html`, paragraphe
« pauvres devenus riches du jour au lendemain… pacte avec la Reine des eaux et profitent des faveurs »
(`rituel.html`, **le texte le plus grave resté en ligne**), 3 occurrences de « pacte » harmonisées en
« alliance », témoignage dupliqué nettoyé dans `temoignages.html`, meta descriptions de `bague.html`
(« symbole de chance… en 3 jours ») réécrites.

> Les scripts sont **idempotents et rejouables à froid** : vérifié en restaurant `HEAD` puis en rejouant
> les deux scripts → résultat identique au fichier corrigé, balises équilibrées sur les 5 pages.

### Ce qui a été **volontairement refusé**

Une recommandation extérieure proposait de « **créer une page tunnel fermée, sans menu ni liens vers les
articles sensibles**, afin de ne pas donner aux robots de Google de liens internes à explorer », et, en
variante, de **déplacer l'URL finale** vers une page épurée en gardant les allégations sur l'accueil.
**Non appliqué**, parce que :

- c'est l'inverse exact de la consigne de bonne pratique Ads : « **Simplifiez l'accès** : assurez-vous
  que Google peut examiner facilement **l'ensemble des pages** de votre site Web », et la liste des
  exemples de cloaking inclut la « **restriction d'accès** (…) pour que nous ne puissions pas examiner
  efficacement votre annonce, votre site ou votre compte »
  ([règle](https://support.google.com/adspolicy/answer/15938075?hl=fr)) ;
- « Diffusion limitée / Allégations douteuses » s'applique aux annonces **et à la destination**, et Google
  évalue « votre annonce, **votre site Web**, vos comptes et des sources tierces » : une destination
  nettoyée à côté d'un accueil qui promet continue de compter comme dissimulation ;
- le motif « Contournement des systèmes » est traité comme **flagrant** : suspension **immédiate et sans
  avertissement**, contagion par l'identité et le mode de paiement, appel quasi perdu d'avance.
  Un refus d'annonce se corrige ; une suspension pour contournement se conteste.

Aucune modification du **menu**, du **footer**, du **`robots.txt`**, du **`sitemap.xml`**, aucun `noindex`,
aucune redirection, aucun contenu différent servi à Googlebot.

### Procédure de déblocage (dans cet ordre)

1. **Publier** : merger cette branche sur `main` et attendre le build GitHub Pages (1–2 min).
   **Ne pas faire appel avant** : Google re-scanne la destination en ligne, un appel déposé sur une
   version non encore déployée échouera.
2. **Vérifier en ligne** : `curl -s https://maitresalifou.com/ | grep -c "5 jours de travaux"` doit renvoyer `0`
   (et idem pour « pacte avec », « Puissance & richesse », « Faites revenir »).
3. **Renvoyer l'examen** : bouton « Faire appel » sur l'annonce, ou modifier l'annonce (un caractère suffit)
   pour relancer la revue. Argument d'appel recommandé, factuel et transparent :
   « Landing page updated on <date> — testimonials and outcome/delay claims removed site-wide; see
   `CONFORMITE-GOOGLE-ADS.md`. The advertised service is a paid consultation; no result is promised. »
4. **Ne jamais** créer un second compte, ni reformuler l'annonce refusée en « variante », ni réutiliser
   un domaine ayant déjà porté ces allégations : ce sont trois exemples nommés de contournement.
5. Si le refus persiste : basculer l'URL finale sur `consultation-voyance.html` (page **déjà** sobre :
   pas de produit, pas de témoignage chiffré, avertissement légal, CTA WhatsApp). C'est un choix
   d'**alignement** annonce↔page, pas une mesure d'occultation — l'accueil doit rester conforme de toute façon.

### Ce qui reste ouvert

- **Le secteur lui-même** : une promesse qui ne peut pas être prouvée reste fragile en Ads, même sans mot
  interdit, car « proposer un service que vous ne pouvez pas garantir » relève des *Pratiques commerciales
  inacceptables*. La robustesse vient du cadrage (« consultation », « écoute ») — sur **tout** le site, pas
  seulement sur la destination.
- `blog.html` et les pages `conseil-*` conservent un vocabulaire descriptif (« signes d'envoûtement ») :
  acceptable en l'état, à surveiller au prochain refus.
- E-mail et n° d'immatriculation toujours à compléter dans les mentions légales (bloquant pour la
  transparence de l'annonceur, et indépendant de cet incident).
