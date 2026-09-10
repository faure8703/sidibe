#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Injecte sur toutes les pages HTML :
  1. la section "Avertissement legal" + liens vers les pages obligatoires
  2. les liens légaux dans le pied de page (copyright)
  3. <link rel="canonical"> et <meta name="referrer">
  4. le bandeau cookies (assets/js/cookie-notice.js)
  5. suppression de l'ancien script IE oss.maxcdn.com (domaine mort)
Script idempotent : peut être rejoué sans dupliquer.
"""
import re
import sys
from pathlib import Path

ROOT = Path("/home/user/sidibe")
SITE = "https://maitresalifou.com"

DISCLAIMER = '''	<!-- ===== Avertissement légal & pages obligatoires (conformité Google Ads) ===== -->
	<section class="ptb-60" id="avertissement-legal" style="background:#f7f7f7;border-top:1px solid #e5e5e5;padding:40px 0;">
		<div class="container">
			<div class="row">
				<div class="col-lg-12">
					<div style="max-width:900px;margin:0 auto;text-align:center;color:#555;font-size:14px;line-height:1.7;">
						<h4 style="color:#222;margin-bottom:12px;">Avertissement légal</h4>
						<p style="margin-bottom:12px;">Les consultations de voyance et conseils spirituels sont proposés à titre indicatif
							et ne remplacent en aucun cas un avis médical, juridique ou financier. <strong>Aucun résultat ne peut être garanti à 100 %.</strong></p>
						<p style="margin-bottom:0;">
							<a href="mentions-legales.html" style="color:#0074da;">Mentions légales</a> &nbsp;·&nbsp;
							<a href="politique-confidentialite.html" style="color:#0074da;">Politique de confidentialité</a> &nbsp;·&nbsp;
							<a href="cgu.html" style="color:#0074da;">CGU / CGV</a>
						</p>
					</div>
				</div>
			</div>
		</div>
	</section>
	<!-- ===== /Avertissement légal ===== -->
'''

FOOTER_LINKS = '''
							<p class="footer-legal-links" style="margin-top:10px;font-size:13px;">
								<a href="mentions-legales.html" style="color:#fff;">Mentions légales</a> &nbsp;|&nbsp;
								<a href="politique-confidentialite.html" style="color:#fff;">Politique de confidentialité</a> &nbsp;|&nbsp;
								<a href="cgu.html" style="color:#fff;">CGU / CGV</a>
							</p>
'''


def process(path: Path):
    html = path.read_text(encoding="utf-8")
    orig = html
    notes = []

    # 1. section avertissement avant le footer
    if "id=\"avertissement-legal\"" not in html:
        idx = html.find('<footer class="footer"')
        if idx == -1:
            notes.append("FOOTER INTROUVABLE")
        else:
            html = html[:idx] + DISCLAIMER + html[idx:]
            notes.append("avertissement")

    # 2. liens légaux dans le pied de page
    if "footer-legal-links" not in html:
        html, n = re.subn(r"(<p>&copy;.*?</p>)", r"\1" + FOOTER_LINKS, html, count=1, flags=re.DOTALL)
        if n:
            notes.append("liens footer")
        else:
            notes.append("COPYRIGHT INTROUVABLE")

    # 3. canonical + referrer
    if 'rel="canonical"' not in html:
        url = SITE + "/" if path.name == "index.html" else f"{SITE}/{path.name}"
        tags = (f'\t<link rel="canonical" href="{url}">\n'
                '\t<meta name="referrer" content="strict-origin-when-cross-origin">\n')
        marker = '\t<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        if marker in html:
            html = html.replace(marker, marker + tags, 1)
            notes.append("canonical")
        else:
            notes.append("VIEWPORT INTROUVABLE")

    # 4. bandeau cookies
    cookie_tag = '\t<!-- cookie notice -->\n\t<script src="assets/js/cookie-notice.js"></script>\n'
    if "cookie-notice.js" not in html:
        if "</body>" in html:
            html = html.replace("</body>", cookie_tag + "</body>", 1)
            notes.append("cookies")
        else:
            notes.append("BODY INTROUVABLE")

    # 5. suppression du script IE (oss.maxcdn.com : domaine hors service)
    html, n_ie = re.subn(r"\s*<!--\[if lt IE 9\]>.*?<!\[endif\]-->\n?", "\n", html, flags=re.DOTALL)
    if n_ie:
        notes.append("IE-script supprimé")

    if html != orig:
        path.write_text(html, encoding="utf-8")
    return notes


def main():
    files = sorted(ROOT.glob("*.html"))
    for f in files:
        notes = process(f)
        print(f"{f.name:38s} {', '.join(notes) if notes else 'déjà à jour'}")
    print(f"\n{len(files)} pages traitées.")


if __name__ == "__main__":
    main()
