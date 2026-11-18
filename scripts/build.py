#!/usr/bin/env python3
"""Static site generator for iChild.org. Run: python3 scripts/build.py
Outputs plain HTML to the repo root so GitHub Pages (main branch) serves it as-is."""
import datetime as dt
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import PAGES, ARTICLES  # noqa: E402

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SITE = "https://ichild.org"
NAME = "iChild.org"
TAGLINE = "Tools, guides & trusted answers for every stage of childhood"
ADSENSE = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>'
INQUIRY = "https://web.works/contact"
TODAY = dt.date.today().isoformat()

NAV = [
    ("index.html", "Home"), ("tools.html", "Tools"), ("milestones.html", "Milestones"), ("guides/index.html", "Guides"),
    ("safety.html", "Safety"), ("videos.html", "Videos"), ("baby-names.html", "Names"), ("donate.html", "Support"),
]

LOGO = ('<svg width="38" height="38" viewBox="0 0 64 64" aria-hidden="true"><rect width="64" height="64" rx="18" fill="#ff6b5c"/>'
        '<circle cx="32" cy="22" r="8" fill="#fff"/><path d="M18 50c2-10 8-16 14-16s12 6 14 16" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>'
        '<circle cx="47" cy="15" r="5" fill="#ffc145"/></svg>')


def head(title, desc, path, root, extra_schema=None, kind="website"):
    url = SITE + "/" + path.replace("index.html", "")
    t = html.escape(title)
    d = html.escape(desc)
    schema = [{
        "@context": "https://schema.org", "@type": "Organization", "name": NAME, "url": SITE,
        "logo": SITE + "/assets/img/logo.svg", "description": TAGLINE,
    }, {
        "@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": SITE,
        "potentialAction": {"@type": "SearchAction", "target": SITE + "/guides/?q={q}", "query-input": "required name=q"},
    }]
    if extra_schema:
        schema.append(extra_schema)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<script>document.documentElement.classList.add("js")</script>
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#ff6b5c">
<meta property="og:type" content="{kind}"><meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{t}"><meta property="og:description" content="{d}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="google-adsense-account" content="ca-pub-6620975821265271">
<link rel="icon" href="{root}assets/img/logo.svg" type="image/svg+xml">
<link rel="manifest" href="{root}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,700;9..144,800&family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/style.css">
{ADSENSE}
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head>"""


def header(path, root):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == path or (href == "guides/index.html" and path.startswith("guides/")) else ""
        items.append(f'<li><a href="{root}{href}"{cur}>{label}</a></li>')
    return f"""<body data-root="{root}">
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><a href="{INQUIRY}" target="_blank" rel="noopener">Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership</a></div>
<header class="site-header"><div class="container nav">
<a class="logo" href="{root}index.html" aria-label="{NAME} home">{LOGO}<span>i<b>Child</b>.org</span></a>
<button class="icon-btn menu-btn" id="menuBtn" aria-label="Open menu" aria-expanded="false" aria-controls="navLinks">☰</button>
<ul class="nav-links" id="navLinks">{''.join(items)}<li><a class="btn btn-primary btn-sm" href="{root}free-plan.html" style="color:#fff">Free Plan</a></li></ul>
<button class="icon-btn" id="themeToggle" aria-label="Toggle dark mode">🌙</button>
</div></header>
<main id="main">"""


def footer(root):
    return f"""</main>
<footer class="site-footer"><div class="container">
<div class="foot-grid">
<div><a class="logo" href="{root}index.html" style="color:#fff">{LOGO}<span>i<b>Child</b>.org</span></a>
<p style="margin-top:12px">{TAGLINE}. Free milestone checklists, calculators, safety recall alerts and plain-language guides for parents and caregivers.</p>
<p class="notice" style="color:#94a3b8">Educational information only — not a substitute for advice from your child's doctor. In an emergency call your local emergency number.</p></div>
<div><h4>Explore</h4><ul>
<li><a href="{root}tools.html">Parenting tools</a></li><li><a href="{root}milestones.html">Milestone checker</a></li><li><a href="{root}guides/index.html">Guides</a></li>
<li><a href="{root}safety.html">Recall alerts</a></li><li><a href="{root}videos.html">Video library</a></li><li><a href="{root}news.html">Research news</a></li><li><a href="{root}baby-names.html">Baby names</a></li></ul></div>
<div><h4>Get involved</h4><ul>
<li><a href="{root}free-plan.html">Free development plan</a></li><li><a href="{root}partners.html">Partners &amp; advertising</a></li><li><a href="{root}donate.html">Support iChild</a></li>
<li><a href="{root}contests.html">Contests &amp; prizes</a></li><li><a href="{root}careers.html">Careers</a></li><li><a href="{root}contact.html">Contact</a></li>
<li><a href="{INQUIRY}" target="_blank" rel="noopener">Buy / sponsor this domain</a></li></ul></div>
<div><h4>Trust &amp; legal</h4><ul>
<li><a href="{root}about.html">About</a></li><li><a href="{root}editorial-policy.html">Editorial policy</a></li><li><a href="{root}privacy.html">Privacy policy</a></li>
<li><a href="{root}terms.html">Terms of use</a></li><li><a href="{root}disclaimer.html">Medical disclaimer</a></li><li><a href="{root}cookies.html">Cookie policy</a></li>
<li><a href="{root}trademark.html">Trademark &amp; copyright</a></li><li><a href="{root}accessibility.html">Accessibility</a></li></ul></div>
</div>
<div class="legal">© <span class="year">2026</span> {NAME}. All rights reserved. iChild.org is an independent publication and is not affiliated with, endorsed by or sponsored by any company, product or organization using a similar name, nor by any organization referenced on this site. All third-party names and marks belong to their respective owners. See our <a href="{root}trademark.html">trademark &amp; copyright disclosure</a>.</div>
</div></footer>
<div class="consent" id="consent" role="dialog" aria-live="polite" aria-label="Cookie notice">
<strong>We value your privacy 🍪</strong>
<p class="notice" style="margin:.4em 0 0">We use cookies for essential features, analytics and to show ads (Google AdSense) that keep iChild free. See our <a href="{root}cookies.html">cookie policy</a>.</p>
<div class="actions"><button class="btn btn-primary btn-sm" data-consent="all">Accept all</button><button class="btn btn-ghost btn-sm" data-consent="essential">Essential only</button></div></div>
<script src="{root}assets/js/app.js" defer></script>
{{TOOLS}}
</body></html>"""


def write(path, title, desc, body, tools=False, schema=None, kind="website"):
    root = "../" * path.count("/")
    doc = head(title, desc, path, root, schema, kind) + header(path, root) + body.replace("{root}", root) + footer(root)
    doc = doc.replace("{TOOLS}", f'<script src="{root}assets/js/tools.js" defer></script>' if tools else "")
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(doc)
    return path


def main():
    written = []
    for p in PAGES:
        written.append(write(p["path"], p["title"], p["desc"], p["body"], p.get("tools", False), p.get("schema")))
    # Articles
    cards = []
    for a in ARTICLES:
        path = f"guides/{a['slug']}.html"
        schema = {
            "@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["desc"],
            "datePublished": "2026-11-18", "dateModified": TODAY, "author": {"@type": "Organization", "name": "iChild.org Editorial Team"},
            "publisher": {"@type": "Organization", "name": NAME, "logo": {"@type": "ImageObject", "url": SITE + "/assets/img/logo.svg"}},
            "mainEntityOfPage": SITE + "/" + path,
        }
        related = [r for r in ARTICLES if r["slug"] != a["slug"] and r["cat"] == a["cat"]][:2] + [r for r in ARTICLES if r["slug"] != a["slug"] and r["cat"] != a["cat"]][:1]
        rel = "".join(f'<article class="card"><span class="tag">{r["cat"]}</span><h3><a href="{r["slug"]}.html">{r["title"]}</a></h3><p>{r["desc"]}</p></article>' for r in related)
        body = f"""<section><div class="container article">
<nav class="breadcrumb" aria-label="Breadcrumb"><a href="{{root}}index.html">Home</a> › <a href="index.html">Guides</a> › {a['cat']}</nav>
<span class="tag">{a['cat']} · {a['age']}</span>
<h1>{a['title']}</h1>
<p class="meta">By the iChild.org Editorial Team · Reviewed against public pediatric guidance · Updated <time datetime="{TODAY}">{TODAY}</time> · {a['mins']} min read</p>
<p class="lead" style="font-size:1.15rem">{a['desc']}</p>
{a['body']}
<div class="callout"><strong>Important:</strong> This guide is general education, not medical advice. Every child is different — talk with your pediatrician, family doctor or child-health nurse about your child's specific needs.</div>
<p><button class="btn btn-ghost btn-sm" data-share>Share this guide</button> <a class="btn btn-primary btn-sm" href="{{root}}free-plan.html">Get your free personalized plan →</a></p>
</div></section>
<section class="alt"><div class="container"><div class="section-head"><h2>Keep reading</h2></div><div class="grid g3">{rel}</div></div></section>"""
        written.append(write(path, a["title"] + " | iChild.org", a["desc"], body, False, schema, "article"))
        cards.append(a)
    # Guides index
    cats = sorted({a["cat"] for a in ARTICLES})
    pills = '<button class="pill active" data-gcat="all">All</button>' + "".join(f'<button class="pill" data-gcat="{c}">{c}</button>' for c in cats)
    grid = "".join(f'<article class="card reveal" data-cat="{a["cat"]}" data-text="{html.escape((a["title"] + " " + a["desc"]).lower())}"><div class="ico">{a["icon"]}</div><span class="tag">{a["cat"]} · {a["age"]}</span><h3><a href="{a["slug"]}.html">{a["title"]}</a></h3><p>{a["desc"]}</p></article>' for a in cards)
    gbody = f"""<section class="hero" style="padding-bottom:10px"><div class="container"><span class="eyebrow">📚 {len(cards)} in-depth guides</span><h1>Parenting guides</h1>
<p class="lead">Plain-language, evidence-informed guides for babies, toddlers and school-age kids — written to be practical at 3 a.m.</p>
<div class="search-box" style="margin-top:16px"><input id="gq" type="search" placeholder="Search guides — e.g. sleep, tantrums, car seat" aria-label="Search guides"></div>
<div class="pill-row" style="margin-top:14px">{pills}</div></div></section>
<section><div class="container"><div class="grid g3" id="guideGrid">{grid}</div></div></section>
<script>
(function(){{const q=document.getElementById('gq'),cards=[...document.querySelectorAll('#guideGrid .card')];let cat='all';
const p=new URLSearchParams(location.search).get('q');if(p)q.value=p;
function f(){{const s=q.value.toLowerCase();cards.forEach(c=>c.style.display=((cat==='all'||c.dataset.cat===cat)&&c.dataset.text.includes(s))?'':'none')}}
q.addEventListener('input',f);document.querySelectorAll('[data-gcat]').forEach(b=>b.addEventListener('click',()=>{{document.querySelectorAll('[data-gcat]').forEach(x=>x.classList.remove('active'));b.classList.add('active');cat=b.dataset.gcat;f()}}));f();}})();
</script>"""
    written.append(write("guides/index.html", "Parenting Guides — Sleep, Behavior, Safety, Feeding | iChild.org", "Free, practical parenting guides on milestones, sleep, tantrums, feeding, screen time, safety and more — from babies to school-age kids.", gbody))
    # 404
    with open(os.path.join(BASE, "404.html"), "w", encoding="utf-8") as f:
        f.write(head("Page not found | iChild.org", "This page could not be found.", "404.html", "/").replace('<meta name="robots" content="index,follow,max-image-preview:large">', '<meta name="robots" content="noindex">')
                + header("404.html", "/") + '<section class="hero"><div class="container" style="text-align:center"><h1>Oops — this page wandered off 🧸</h1><p class="lead" style="margin:auto">Let\'s get you back on track.</p><p class="hero-cta" style="justify-content:center"><a class="btn btn-primary" href="/index.html">Go home</a><a class="btn btn-ghost" href="/tools.html">Open the tools</a></p></div></section>' + footer("/").replace("{TOOLS}", ""))
    # Sitemap
    urls = [w for w in written]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        loc = SITE + "/" + u.replace("index.html", "")
        pr = "1.0" if u == "index.html" else ("0.8" if u.startswith("guides/") or u in ("tools.html", "milestones.html", "safety.html") else "0.6")
        sm.append(f"<url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    with open(os.path.join(BASE, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(sm) + "\n")
    print(f"Built {len(written)} pages + 404 + sitemap")


if __name__ == "__main__":
    main()
