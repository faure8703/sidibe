/* Recherche instantanée du site SIDIBE (sans accent, insensible à la casse) */
(function () {
    var PAGES = [
        { t: "Accueil", u: "index.html", k: "accueil marabout sidibe salifou voyant" },
        { t: "Retour d'affection", u: "retouraffection.html", k: "amour retour ex femme mari copain affection reconquete etre aime" },
        { t: "Harmonie du Couple", u: "harmonie-couple.html", k: "couple harmonie fidelite infidelite mariage divorce rival union" },
        { t: "Fertilité & Famille", u: "fertilite-famille.html", k: "fertilite sterilite grossesse enfant famille bebe regles fausse couche" },
        { t: "Consultation du Fa (Voyance)", u: "consultation-voyance.html", k: "voyance consultation fa oracle destin avenir prediction destin" },
        { t: "Protection & Désenvoûtement", u: "protection-desenvoutement.html", k: "protection desenvoutement sorcellerie malchance ennemi envoutement talisman" },
        { t: "Chance & Emploi", u: "chance-travail.html", k: "chance emploi travail examen concours etudiant savon parfum memoire bic" },
        { t: "Clientèle & Commerce", u: "clientele-commerce.html", k: "clientele commerce entreprise boutique marche client affaire argent" },
        { t: "Bague Magique", u: "bague.html", k: "bague anneau fortune chance protection" },
        { t: "Rituel Mami Wata", u: "rituel.html", k: "rituel mami wata maman eau richesse puissance pacte reine" },
        { t: "Divers Produits", u: "diversproduit.html", k: "produits catalogue savon talisman cadenas parfum bic miroir liste" },
        { t: "Guide & FAQ", u: "guide-consultation-faq.html", k: "guide faq aide consultation deroulement delai arnaque question distance" },
        { t: "Témoignages", u: "temoignages.html", k: "temoignage avis client satisfaction opinion" },
        { t: "Le Maître SIDIBE Salifou", u: "maitre-sidibe.html", k: "maitre sidibe salifou biographie parcours vodou benin adja" },
        { t: "Cadenas d'Amour", u: "cadenas-amour.html", k: "cadenas amour union fidelite foyer sceller" },
        { t: "Mari & Femme de Nuit", u: "mari-femme-nuit.html", k: "mari femme nuit cauchemar reve blocage delivrance" },
        { t: "Justice & Procès", u: "justice-proces.html", k: "justice proces tribunal heritage terrain litige convocation" },
        { t: "Purification des Lieux", u: "purification-lieux.html", k: "purification maison lieu boutique bureau terrain encens" },
        { t: "Savons & Parfums", u: "savons-parfums.html", k: "savon parfum chance amour protection commerce produit" },
        { t: "Enfants & Réussite", u: "enfants-reussite.html", k: "enfant ecole reussite examen protection eleve etudiant" },
        { t: "Blog Conseils", u: "blog.html", k: "blog conseil article astuce sagesse" },
        { t: "Conseil : signes d'envoûtement", u: "conseil-signes-envoutement.html", k: "signe envoutement malchance fatigue cauchemar blocage" },
        { t: "Conseil : préparer sa consultation", u: "conseil-preparer-consultation.html", k: "preparer consultation question information distance" },
        { t: "Conseil : protéger son commerce", u: "conseil-proteger-commerce.html", k: "proteger commerce boutique client vente marche" },
        { t: "Contact & Accès", u: "contact.html", k: "contact acces adresse telephone whatsapp email adja benin carte" }
    ];
    function norm(s) {
        return s.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    }
    var input = document.getElementById("site-search");
    var box = document.getElementById("search-results");
    if (!input || !box) return;
    input.addEventListener("input", function () {
        var q = norm(input.value.trim());
        if (q.length < 2) { box.innerHTML = ""; box.style.display = "none"; return; }
        var res = PAGES.filter(function (p) {
            return norm(p.t + " " + p.k).indexOf(q) !== -1;
        }).slice(0, 6);
        if (!res.length) {
            box.innerHTML = '<span class="no-result">Aucun résultat</span>';
        } else {
            box.innerHTML = res.map(function (p) {
                return '<a href="' + p.u + '">' + p.t + "</a>";
            }).join("");
        }
        box.style.display = "block";
    });
    document.addEventListener("click", function (e) {
        if (e.target !== input) box.style.display = "none";
    });
})();
