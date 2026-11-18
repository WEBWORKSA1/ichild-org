# Phase-wise build prompt — iChild.org

Use these phases in order to rebuild or extend the site.

## Phase 1 — Strategy and research
"Build iChild.org as a free child-development and parenting toolkit for parents and caregivers (pregnancy to age 12). Study leading sites (CDC Act Early, Pathways.org, HealthyChildren, KidsHealth, Raising Children, BabyCenter-style tool sites, Nameberry, Common Sense Media, Safe Kids, Vroom, plus children's charities for donation UX). Record their features, forms, monetization and design. Output RESEARCH.md."

## Phase 2 — Architecture and design system
"Create a static, GitHub-Pages-ready site (HTML/CSS/vanilla JS, no build step needed to serve). Use a warm palette (coral #ff6b5c, teal #13a89e, sun #ffc145, cream #fffaf5), the Fraunces and Nunito fonts, dark mode, a sticky header, mobile menu and WCAG-AA basics. On top of every page show a bar: 'Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership' linked to https://web.works/contact."

## Phase 3 — Core tools
"Build client-side tools: milestone checker (2 months–5 years, saved in localStorage, printable), exact age, due date, sleep and bedtime, mid-parental height, child BMI (percentile caveat), screen-time planner, childcare cost, allowance, car seat stage finder, and a baby-name finder (200+ names, filters, shortlist)."

## Phase 4 — Content for AdSense approval
"Write at least 12 original, plain-language guides (600+ words each) on milestones, safe sleep, screen time, tantrums, solids, reading, childproofing, car seats, emotional intelligence, school-age sleep, picky eating, online safety, speech and childcare. Add Article and FAQ schema, a sitemap, robots.txt, ads.txt (pub-6620975821265271), and About, Contact, Privacy (AdSense and children's-privacy wording), Terms, Medical Disclaimer, Cookies, Editorial, Accessibility and Trademark/Copyright pages. Put the AdSense auto-ads script in every page's head. Make it clear that the site is directed at adults."

## Phase 5 — Monetization and conversion
"Add: (a) lead generation: a 3-step 'Free personalized plan' form, a quick home-page form and a local service referral form; (b) Partners: sponsorship, advertising, local leads, licensing and prize-partner inquiry form; (c) Donations: preset tiers, frequency, designation (operations, promotion, hiring, contests) and a not-a-charity disclosure; (d) Contests with official rules and child-privacy safeguards; (e) Careers with an application form. Route every form to one inbox. Assemble that address in JavaScript so it never appears in the page or the source; send through FormSubmit AJAX, with a mailto fallback."

## Phase 6 — Automation
"Add scripts/update_data.py and a GitHub Actions workflow (every 6h, on push and on manual dispatch). The script pulls children's product recalls (CPSC and Health Canada), research headlines (Google News RSS) and the latest videos from trusted YouTube channels into /data/*.json, then commits any changes. A tip of the day rotates on the client."

## Phase 7 — QA and launch
"Run headless-browser checks on desktop and mobile, check for JS errors, test every calculator, confirm the email never appears in the output, then push to the main branch of webworksa1/ichild-org and enable GitHub Pages from main /(root). After DNS points to GitHub, add a CNAME of ichild.org and submit the sitemap to Search Console and the site to AdSense."
