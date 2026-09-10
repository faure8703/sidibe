/* Bandeau d'information cookies - maitresalifou.com
   Aucun cookie publicitaire ni traceur de ciblage n'est depose par le site.
   Le bandeau informe l'utilisateur et memorise son choix. */
(function () {
    "use strict";

    var STORAGE_KEY = "ms_cookie_choice";

    function getChoice() {
        try {
            return window.localStorage.getItem(STORAGE_KEY);
        } catch (e) {
            return null;
        }
    }

    function setChoice(value) {
        try {
            window.localStorage.setItem(STORAGE_KEY, value);
        } catch (e) {
            /* stockage indisponible : le bandeau se reaffichera a la prochaine visite */
        }
    }

    function build() {
        var bar = document.createElement("div");
        bar.id = "cookie-notice";
        bar.setAttribute("role", "dialog");
        bar.setAttribute("aria-live", "polite");
        bar.setAttribute("aria-label", "Information sur les cookies");
        bar.style.cssText = [
            "position:fixed",
            "left:0",
            "right:0",
            "bottom:0",
            "z-index:9999",
            "background:#1b1b1b",
            "color:#fff",
            "padding:14px 20px",
            "font-size:14px",
            "line-height:1.5",
            "box-shadow:0 -2px 12px rgba(0,0,0,.35)"
        ].join(";");

        var text = document.createElement("span");
        text.innerHTML =
            "Ce site ne d\u00e9pose <strong>aucun cookie publicitaire ni traceur publicitaire</strong>. " +
            "Seuls des cookies techniques (h\u00e9bergement, m\u00e9morisation de ce choix) et ceux de " +
            "services tiers (Google Maps, WhatsApp) peuvent \u00eatre utilis\u00e9s. " +
            "Plus de d\u00e9tails dans la <a href=\"politique-confidentialite.html\" " +
            "style=\"color:#6fd08c;text-decoration:underline;\">politique de confidentialit\u00e9</a>.";
        text.style.display = "inline-block";
        text.style.maxWidth = "100%";
        bar.appendChild(text);

        var actions = document.createElement("span");
        actions.style.cssText = "display:inline-block;margin-left:14px;white-space:nowrap;";

        function button(label, bg, value) {
            var b = document.createElement("button");
            b.type = "button";
            b.textContent = label;
            b.style.cssText =
                "margin-left:8px;padding:8px 16px;border:0;border-radius:4px;cursor:pointer;" +
                "font-weight:600;background:" + bg + ";color:#fff;";
            b.addEventListener("click", function () {
                setChoice(value);
                if (bar.parentNode) {
                    bar.parentNode.removeChild(bar);
                }
            });
            return b;
        }

        actions.appendChild(button("Accepter", "#128C7E", "accepted"));
        actions.appendChild(button("Refuser", "#555", "refused"));
        bar.appendChild(actions);

        document.body.appendChild(bar);
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", function () {
            if (!getChoice()) {
                build();
            }
        });
    } else if (!getChoice()) {
        build();
    }
})();
