"""Page content for iChild.org. Bodies use {root} for relative links."""
from articles import ARTICLES  # noqa: F401

INQ = "https://web.works/contact"
HP = '<div class="hp" aria-hidden="true"><label>Leave empty<input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></label></div>'
CONSENT = ('<label class="check"><input type="checkbox" name="consent" value="yes" required> I am 18 or older, I agree to the '
           '<a href="{root}privacy.html">Privacy Policy</a> and I consent to iChild.org contacting me about this request.</label>')
COUNTRIES = "".join(f"<option>{c}</option>" for c in ["United States", "Canada", "United Kingdom", "India", "Australia", "Ireland", "New Zealand", "Singapore", "UAE", "South Africa", "Nigeria", "Philippines", "Malaysia", "Sri Lanka", "Pakistan", "Germany", "France", "Other"])
AGES = "".join(f"<option>{a}</option>" for a in ["Expecting", "0–3 months", "4–6 months", "7–12 months", "1–2 years", "2–3 years", "3–5 years", "6–8 years", "9–12 years", "13+ years"])


def card(icon, title, text, href, tag=""):
    t = f'<span class="tag">{tag}</span>' if tag else ""
    return f'<article class="card reveal"><div class="ico">{icon}</div>{t}<h3><a href="{href}">{title}</a></h3><p>{text}</p></article>'


TOOLS = [
    ("✅", "Milestone checker", "Interactive checklists from 2 months to 5 years. Progress saves on your device.", "{root}milestones.html", "Development"),
    ("🎂", "Exact age calculator", "Your child's age in years, months, weeks and days — plus a birthday countdown.", "{root}tools.html#age", "Everyday"),
    ("🤰", "Due date calculator", "Estimate your due date, current week and trimester from your last period.", "{root}tools.html#due", "Pregnancy"),
    ("😴", "Sleep needs & bedtime", "Recommended sleep by age and the ideal bedtime for your wake-up time.", "{root}tools.html#sleep", "Sleep"),
    ("📏", "Adult height predictor", "Mid-parental height estimate with a realistic range.", "{root}tools.html#height", "Growth"),
    ("⚖️", "Child BMI calculator", "Calculate BMI and learn how to read it on a growth chart.", "{root}tools.html#bmi", "Growth"),
    ("📱", "Screen-time planner", "A balanced daily plan based on pediatric screen-time guidance.", "{root}tools.html#screen", "Digital"),
    ("💸", "Childcare cost estimator", "Weekly, monthly and yearly childcare cost, with sibling discounts.", "{root}tools.html#care", "Money"),
    ("🐷", "Allowance calculator", "Age-based allowance with save, spend and give jars.", "{root}tools.html#allow", "Money"),
    ("🚗", "Car seat stage finder", "Rear-facing, forward-facing, booster or belt? Find the right stage.", "{root}tools.html#seat", "Safety"),
    ("👶", "Baby name finder", "200+ names with meanings and origins. Filter, shuffle and shortlist.", "{root}baby-names.html", "Names"),
    ("⚠️", "Live recall alerts", "Children's product recalls from official agencies, refreshed automatically.", "{root}safety.html", "Safety"),
]
TOOL_GRID = "".join(card(*t[:4], t[4]) for t in TOOLS)

LEAD_FORM = f"""<form data-form="free-plan-quick" data-success="You're in! Watch your inbox for your child's personalized plan within 24–48 hours." novalidate>
<h3 style="margin-top:0">Get your free plan</h3>
<label for="lf-name">Your first name</label><input id="lf-name" name="name" required autocomplete="given-name">
<label for="lf-email">Email</label><input id="lf-email" name="email" type="email" required autocomplete="email">
<div class="row"><div><label for="lf-age">Child's age</label><select id="lf-age" name="child_age" required><option value="">Select…</option>{AGES}</select></div>
<div><label for="lf-country">Country</label><select id="lf-country" name="country" required><option value="">Select…</option>{COUNTRIES}</select></div></div>
<label for="lf-focus">Top focus right now</label><select id="lf-focus" name="focus"><option>Milestones & development</option><option>Sleep</option><option>Behavior & tantrums</option><option>Feeding & picky eating</option><option>Speech & language</option><option>School readiness</option><option>Screen time & online safety</option></select>
{HP}{CONSENT}
<button class="btn btn-primary" type="submit" style="width:100%;justify-content:center;margin-top:12px">Send my free plan →</button>
<p class="form-msg" aria-live="polite"></p>
<p class="notice" style="margin:8px 0 0">No spam. Unsubscribe anytime. We never sell your data.</p>
</form>"""

LEAD_BOX = f"""<div class="lead-box reveal"><div>
<span class="tag" style="background:#ffffff22;color:#ffd7d1">Free · takes 60 seconds</span>
<h2>Your child's personalized development plan</h2>
<p>Tell us your child's age and your biggest focus. We'll send a tailored plan with:</p>
<ul><li>The milestones to watch for in the next 3 months</li><li>5–7 play ideas that build those exact skills</li><li>A sleep and routine template for their age</li><li>Safety checks for this stage (and recall alerts)</li><li>Warning signs that mean "talk to your doctor"</li></ul>
<p style="font-weight:800;color:#fff">Free forever · No spam · Unsubscribe anytime.</p></div>
{LEAD_FORM}</div>"""

FAQ_HOME = [
    ("Is iChild.org free?", "Yes. Every tool, checklist and guide is free. We are supported by advertising, partners and optional reader contributions."),
    ("Is my child's data stored?", "Calculators and the milestone checker run in your browser. Checklist progress is saved only on your device. We only receive information you choose to send through a form."),
    ("Is this medical advice?", "No. iChild.org provides general education drawn from public pediatric guidance. Always talk to your child's doctor about your child's health and development."),
    ("How often is the site updated?", "Recall alerts, research headlines and the video library refresh automatically several times a day. Guides are reviewed regularly."),
    ("Who is iChild.org for?", "Parents, grandparents, caregivers and educators of children from pregnancy to age 12. The site is written for adults and is not directed at children."),
]


def faq(items):
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p style=\"margin:.6em 0 0\">{a}</p></details>" for q, a in items) + "</div>"


def faq_schema(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def featured_guides(n=6):
    return "".join(card(a["icon"], a["title"], a["desc"], "{root}guides/" + a["slug"] + ".html", a["cat"]) for a in ARTICLES[:n])


HOME = f"""
<section class="hero"><div class="container hero-grid">
<div><span class="eyebrow">👋 For parents, caregivers &amp; educators</span>
<h1>Every child, growing &amp; thriving — with tools that actually help.</h1>
<p class="lead">Milestone checklists, smart calculators, live safety recall alerts and practical guides for pregnancy through age 12. Free, private, and updated every day.</p>
<div class="hero-cta"><a class="btn btn-primary" href="{{root}}milestones.html">✅ Check milestones</a><a class="btn btn-ghost" href="{{root}}free-plan.html">Get a free personalized plan</a></div>
<div class="stats"><div><span>12+</span>free tools</div><div><span>{len(ARTICLES)}</span>in-depth guides</div><div><span>4×</span>daily data refresh</div><div><span>0–12</span>years covered</div></div></div>
<div class="hero-art"><div class="tip-card" id="tipOfDay"><span class="tag" style="background:#fff8e1;color:#7a5200">Today's tip</span><h3>Loading today's tip…</h3></div>
<form id="ageForm" style="margin-top:18px"><label for="dob">Quick check: how old is your child exactly?</label><div class="search-box"><input type="date" id="dob" required><button class="btn btn-teal" type="submit">Calculate</button></div><div class="result" id="ageOut" aria-live="polite"></div></form>
</div></div></section>

<section class="alt"><div class="container"><div class="section-head"><div><h2>Free parenting tools</h2><p>Fast, private calculators and checklists — nothing to install, nothing to sign up for.</p></div><a class="btn btn-ghost" href="{{root}}tools.html">All tools →</a></div>
<div class="grid g4">{TOOL_GRID}</div></div></section>

<section><div class="container">{LEAD_BOX}</div></section>

<section class="alt"><div class="container"><div class="section-head"><div><h2>Popular guides</h2><p>Clear, evidence-informed answers to the questions parents ask most.</p></div><a class="btn btn-ghost" href="{{root}}guides/index.html">All guides →</a></div>
<div class="grid g3">{featured_guides(6)}</div></div></section>

<section><div class="container grid g2" style="align-items:start">
<div><div class="section-head"><div><h2>⚠️ Latest recall alerts</h2><p>Children's products recalled by official safety agencies. Updated automatically.</p></div></div>
<div class="grid" id="recalls" data-limit="5"><p class="notice">Loading recalls…</p></div><p style="margin-top:14px"><a class="btn btn-ghost btn-sm" href="{{root}}safety.html">See all recalls &amp; safety checklists →</a></p></div>
<div><div class="section-head"><div><h2>📰 Child research news</h2><p>Fresh headlines on child development, health and learning.</p></div></div>
<div class="grid" id="news" data-limit="5"><p class="notice">Loading headlines…</p></div><p style="margin-top:14px"><a class="btn btn-ghost btn-sm" href="{{root}}news.html">More news →</a></p></div>
</div></section>

<section class="alt"><div class="container"><div class="section-head"><div><h2>🎬 Watch &amp; learn</h2><p>Short videos from trusted child-health and early-learning channels.</p></div><a class="btn btn-ghost" href="{{root}}videos.html">Video library →</a></div>
<div class="grid g3" id="videos" data-limit="6"><p class="notice">Loading videos…</p></div></div></section>

<section><div class="container grid g3">
{card("💛", "Support iChild", "Keep every tool free. Fund operations, outreach, new hires and family contests.", "{root}donate.html", "Donate")}
{card("🏆", "Contests &amp; prizes", "Monthly Little Artists, Parent Hack and Story Time challenges with prizes.", "{root}contests.html", "Win")}
{card("🧑‍💻", "We're hiring", "Writers, pediatric reviewers, video creators, ambassadors and partnership reps.", "{root}careers.html", "Careers")}
</div></section>

<section class="alt"><div class="container grid g2" style="align-items:center">
<div><h2>Partner with iChild</h2><p>Reach engaged parents at the exact moment they are making decisions about sleep, feeding, safety, learning and childcare. Sponsor a tool, list your service, or license content.</p>
<p><a class="btn btn-primary" href="{{root}}partners.html">Partnership options</a> <a class="btn btn-ghost" href="{INQ}" target="_blank" rel="noopener">Sponsor / acquire this domain</a></p></div>
<div><h2 style="font-size:1.5rem">Frequently asked</h2>{faq(FAQ_HOME)}</div>
</div></section>
"""


def tool_section(id_, icon, title, intro, form_html, out_id):
    return f'<article class="card tool reveal" id="{id_}"><div class="ico">{icon}</div><h2 style="font-size:1.5rem">{title}</h2><p>{intro}</p>{form_html}<div class="result" id="{out_id}" aria-live="polite"></div></article>'


TOOLS_BODY = f"""
<section class="hero" style="padding-bottom:10px"><div class="container"><span class="eyebrow">🧰 Free · private · instant</span><h1>Parenting tools &amp; calculators</h1>
<p class="lead">Everything runs in your browser — we never see what you type into a calculator.</p>
<div class="pill-row" style="margin-top:14px"><a class="pill" href="#age">Age</a><a class="pill" href="#due">Due date</a><a class="pill" href="#sleep">Sleep</a><a class="pill" href="#height">Height</a><a class="pill" href="#bmi">BMI</a><a class="pill" href="#screen">Screen time</a><a class="pill" href="#care">Childcare cost</a><a class="pill" href="#allow">Allowance</a><a class="pill" href="#seat">Car seat</a><a class="pill" href="{{root}}milestones.html">Milestones</a><a class="pill" href="{{root}}baby-names.html">Names</a></div></div></section>
<section><div class="container grid g2">
{tool_section("age", "🎂", "Exact age calculator", "Find your child's precise age — handy for milestone checklists, vaccine schedules and forms.",
  '<form id="ageForm"><label for="dob">Date of birth</label><input type="date" id="dob" required><button class="btn btn-primary" style="margin-top:12px" type="submit">Calculate age</button></form>', "ageOut")}
{tool_section("due", "🤰", "Pregnancy due date calculator", "Uses Naegele's rule, adjusted for your cycle length.",
  '<form id="dueForm"><div class="row"><div><label for="lmp">First day of last period</label><input type="date" id="lmp" required></div><div><label for="cycle">Average cycle (days)</label><input type="number" id="cycle" value="28" min="20" max="45"></div></div><button class="btn btn-primary" style="margin-top:12px" type="submit">Find due date</button></form>', "dueOut")}
{tool_section("sleep", "😴", "Sleep needs &amp; bedtime calculator", "How much sleep does your child need, and when should lights go out?",
  '<form id="sleepForm"><div class="row"><div><label for="sleepAge">Child\'s age</label><select id="sleepAge"><option value="1">0–3 months</option><option value="6">4–11 months</option><option value="18">1–2 years</option><option value="48">3–5 years</option><option value="96" selected>6–12 years</option><option value="180">13–18 years</option></select></div><div><label for="wake">Wake-up time</label><input type="time" id="wake" value="07:00"></div></div><button class="btn btn-primary" style="margin-top:12px" type="submit">Get bedtime</button></form>', "sleepOut")}
{tool_section("height", "📏", "Adult height predictor", "The mid-parental method gives a genetic target height with a typical ±8.5 cm range.",
  '<form id="heightForm"><div class="row"><div><label for="hSex">Child</label><select id="hSex"><option value="boy">Boy</option><option value="girl">Girl</option></select></div><div><label for="hUnit">Units</label><select id="hUnit"><option value="cm">cm</option><option value="in">inches</option></select></div></div><div class="row"><div><label for="hDad">Father\'s height</label><input type="number" id="hDad" required step="0.1"></div><div><label for="hMom">Mother\'s height</label><input type="number" id="hMom" required step="0.1"></div></div><button class="btn btn-primary" style="margin-top:12px" type="submit">Predict height</button></form>', "heightOut")}
{tool_section("bmi", "⚖️", "Child &amp; teen BMI calculator", "Calculate body mass index, then check it on an age-and-sex growth chart with your doctor.",
  '<form id="bmiForm"><label for="bUnit">Units</label><select id="bUnit"><option value="metric">kg / cm</option><option value="imperial">lb / inches</option></select><div class="row"><div><label for="bW">Weight</label><input type="number" id="bW" required step="0.1"></div><div><label for="bH">Height</label><input type="number" id="bH" required step="0.1"></div></div><button class="btn btn-primary" style="margin-top:12px" type="submit">Calculate BMI</button></form>', "bmiOut")}
{tool_section("screen", "📱", "Screen-time planner", "A balanced daily plan built on pediatric media guidance.",
  '<form id="screenForm"><div class="row"><div><label for="stAge">Age (years)</label><input type="number" id="stAge" min="0" max="18" step="0.5" value="4" required></div><div><label for="stCap">Your cap for 6+ (minutes)</label><input type="number" id="stCap" value="90" min="0" max="300"></div></div><button class="btn btn-primary" style="margin-top:12px" type="submit">Build my plan</button></form>', "screenOut")}
{tool_section("care", "💸", "Childcare cost estimator", "Use your local currency. Includes sibling discounts and a share-of-income check.",
  '<form id="careForm"><div class="row"><div><label for="ccRate">Rate</label><input type="number" id="ccRate" required min="0" step="0.01"></div><div><label for="ccPer">Rate is per</label><select id="ccPer"><option value="hour">hour</option><option value="day">day</option><option value="week">week</option></select></div></div><div class="row"><div><label for="ccUnits">Hours or days per week</label><input type="number" id="ccUnits" value="40" min="0"></div><div><label for="ccKids">Children</label><input type="number" id="ccKids" value="1" min="1" max="6"></div></div><div class="row"><div><label for="ccDisc">Sibling discount %</label><input type="number" id="ccDisc" value="10" min="0" max="100"></div><div><label for="ccInc">Annual household income (optional)</label><input type="number" id="ccInc" min="0"></div></div><button class="btn btn-primary" style="margin-top:12px" type="submit">Estimate cost</button></form>', "ccOut")}
{tool_section("allow", "🐷", "Allowance calculator", "A common rule of thumb is a set amount per year of age, per week.",
  '<form id="allowForm"><div class="row"><div><label for="alAge">Child\'s age</label><input type="number" id="alAge" value="8" min="3" max="18" required></div><div><label for="alPer">Amount per year of age</label><input type="number" id="alPer" value="1" min="0" step="0.25"></div></div><div class="row"><div><label for="alSave">Save %</label><input type="number" id="alSave" value="40"></div><div><label for="alSpend">Spend %</label><input type="number" id="alSpend" value="50"></div></div><label for="alGive">Give %</label><input type="number" id="alGive" value="10"><button class="btn btn-primary" style="margin-top:12px" type="submit">Calculate</button></form>', "alOut")}
{tool_section("seat", "🚗", "Car seat stage finder", "General guidance based on child passenger safety recommendations.",
  '<form id="seatForm"><div class="row"><div><label for="csAge">Age (years)</label><input type="number" id="csAge" min="0" max="13" step="0.5" required></div><div><label for="csH">Height (optional)</label><input type="number" id="csH" min="0" step="0.1"></div></div><label for="csUnit">Height units</label><select id="csUnit"><option value="in">inches</option><option value="cm">cm</option></select><button class="btn btn-primary" style="margin-top:12px" type="submit">Find my stage</button></form>', "seatOut")}
<article class="card tool reveal"><div class="ico">✅</div><h2 style="font-size:1.5rem">More tools</h2><p>Track development with our <a href="{{root}}milestones.html">milestone checker</a>, shortlist names in the <a href="{{root}}baby-names.html">baby name finder</a>, and stay current with <a href="{{root}}safety.html">live recall alerts</a>.</p><p><a class="btn btn-teal" href="{{root}}free-plan.html">Get a personalized plan</a></p></article>
</div></section>
<section class="alt"><div class="container">{LEAD_BOX}</div></section>
"""

MILESTONES_BODY = f"""
<section class="hero" style="padding-bottom:10px"><div class="container"><span class="eyebrow">✅ 2 months – 5 years</span><h1>Developmental milestone checker</h1>
<p class="lead">Tick the skills you have seen your child do. Your progress is saved privately on this device so you can come back any time — and print it for your next check-up.</p></div></section>
<section><div class="container grid g2" style="align-items:start">
<div class="card" id="milestoneTool"><label for="msAge">Choose your child's age</label><select id="msAge"></select>
<div class="bar" id="msBar" style="margin:16px 0"><i></i></div>
<ul class="milestone-list" id="msList"></ul>
<div class="result" id="msOut" aria-live="polite"></div>
<p style="margin-top:14px"><button class="btn btn-ghost btn-sm" id="msPrint" type="button">🖨️ Print for my doctor</button> <a class="btn btn-primary btn-sm" href="{{root}}free-plan.html">Get play ideas for this age →</a></p></div>
<div>
<h2>How to use this checklist</h2>
<p>Milestones are skills most children (roughly 3 out of 4) show by a certain age. They cover four areas: <strong>social and emotional</strong>, <strong>language and communication</strong>, <strong>thinking and problem-solving</strong>, and <strong>movement and physical development</strong>.</p>
<p>If your baby was born prematurely, use their <em>adjusted age</em> (age minus the weeks born early) until about age 2.</p>
<h3>When to act early</h3>
<ul><li>Your child is missing several milestones for their age.</li><li>Your child <strong>loses skills</strong> they once had — at any age.</li><li>You have a gut feeling something isn't right.</li></ul>
<div class="callout">Early support works. If you have concerns, ask your child's doctor about a <strong>developmental screening</strong>, and ask about early-intervention services in your area — you usually don't need a diagnosis or referral to request an evaluation.</div>
<p class="notice">Checklist items are written by iChild.org in plain language and informed by public developmental guidance from national health agencies. It is not a screening or diagnostic tool.</p>
<h3>Keep learning</h3><ul><li><a href="{{root}}guides/developmental-milestones-guide.html">Milestones 0–5: the complete parent guide</a></li><li><a href="{{root}}guides/speech-language-development.html">Speech &amp; language: what to expect</a></li><li><a href="{{root}}videos.html">Milestone videos</a></li></ul>
</div></div></section>
<section class="alt"><div class="container">{LEAD_BOX}</div></section>
"""

NAMES_BODY = """
<section class="hero" style="padding-bottom:10px"><div class="container"><span class="eyebrow">👶 Meanings · origins · shortlist</span><h1>Baby name finder</h1>
<p class="lead">Browse names from more than 25 cultures. Search by first letter or meaning, filter by origin, and tap ♡ to build your shortlist (saved on your device).</p></div></section>
<section><div class="container" id="nameTool">
<div class="card"><div class="search-box"><input id="nameQ" type="search" placeholder="Start typing a name or a meaning (e.g. 'light')" aria-label="Search names">
<select id="nameG" aria-label="Gender" style="max-width:160px"><option value="all">All</option><option value="g">Girl</option><option value="b">Boy</option><option value="u">Unisex</option></select>
<select id="nameO" aria-label="Origin" style="max-width:200px"><option value="all">All origins</option></select>
<button class="btn btn-teal" id="nameRandom" type="button">🎲 Surprise me</button></div>
<p class="notice" id="nameCount" style="margin:10px 0 0"></p>
<p style="margin:10px 0 0"><strong>Your shortlist:</strong> <span id="favOut"></span></p></div>
<div class="grid g3" id="nameOut" style="margin-top:20px"></div>
</div></section>
<section class="alt"><div class="container grid g2"><div><h2>Tips for choosing a name</h2>
<ul><li><strong>Say it out loud</strong> with your surname — rhythm matters. A short first name often pairs well with a long surname and vice versa.</li><li><strong>Check the initials</strong> and common nicknames.</li><li><strong>Think across languages</strong> if your family is multilingual — make sure the name is easy to say and has a positive meaning in each.</li><li><strong>Sleep on it.</strong> Keep a shortlist for a few weeks and see which names you still love.</li></ul></div>
<div><h2>Expecting?</h2><p>Use our <a href="{root}tools.html#due">due date calculator</a>, then get a week-by-week plan for the newborn months.</p><p><a class="btn btn-primary" href="{root}free-plan.html">Get my free plan</a></p></div></div></section>
"""

SAFETY_BODY = """
<section class="hero" style="padding-bottom:10px"><div class="container"><span class="eyebrow">⚠️ Auto-updated recall feed</span><h1>Child safety &amp; product recalls</h1>
<p class="lead">Recalled cribs, car seats, toys and baby gear from official safety agencies — refreshed automatically several times a day. Last update: <strong id="recallsUpdated">checking…</strong></p>
<div class="search-box" style="margin-top:14px"><input id="recallFilter" type="search" placeholder="Filter recalls — e.g. crib, stroller, magnet" aria-label="Filter recalls"></div></div></section>
<section><div class="container"><div class="grid g2" id="recalls" data-limit="80"><p class="notice">Loading recalls…</p></div>
<p class="notice" style="margin-top:16px">Sources: U.S. Consumer Product Safety Commission and Health Canada public recall data. Always confirm details (model numbers, dates) on the official notice before acting.</p></div></section>
<section class="alt"><div class="container"><h2>Check official recall databases</h2><div class="grid g4">
<article class="card"><h3><a href="https://www.cpsc.gov/Recalls" target="_blank" rel="noopener">United States — CPSC</a></h3><p>Consumer products, toys and nursery gear.</p></article>
<article class="card"><h3><a href="https://www.nhtsa.gov/recalls" target="_blank" rel="noopener">United States — NHTSA</a></h3><p>Car seats and vehicles.</p></article>
<article class="card"><h3><a href="https://recalls-rappels.canada.ca/en" target="_blank" rel="noopener">Canada — Recalls &amp; safety alerts</a></h3><p>Consumer products, food and vehicles.</p></article>
<article class="card"><h3><a href="https://ec.europa.eu/safety-gate-alerts/screen/webReport" target="_blank" rel="noopener">EU — Safety Gate</a></h3><p>Dangerous non-food products in Europe.</p></article>
<article class="card"><h3><a href="https://www.gov.uk/product-safety-alerts-reports-recalls" target="_blank" rel="noopener">United Kingdom — OPSS</a></h3><p>Product safety alerts and recalls.</p></article>
<article class="card"><h3><a href="https://www.productsafety.gov.au/recalls" target="_blank" rel="noopener">Australia — ACCC</a></h3><p>Product Safety Australia recalls.</p></article>
<article class="card"><h3><a href="https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts" target="_blank" rel="noopener">United States — FDA</a></h3><p>Food, formula and medicine recalls.</p></article>
<article class="card"><h3>Register your products</h3><p>Fill in the registration card for car seats, cribs and strollers so the maker can contact you directly about a recall.</p></article>
</div></div></section>
<section><div class="container grid g3">
<article class="card"><div class="ico">🛏️</div><h3>Safe sleep checklist</h3><ul><li>Baby on their back for every sleep</li><li>Firm, flat mattress with a fitted sheet</li><li>Nothing else in the crib</li><li>Room-share without bed-sharing</li><li>No inclined sleepers or weighted sleep products</li></ul><a href="{root}guides/safe-sleep-for-babies.html">Read the guide →</a></article>
<article class="card"><div class="ico">🏠</div><h3>Babyproofing essentials</h3><ul><li>Anchor furniture and TVs to the wall</li><li>Lock away medicines, cleaners and button batteries</li><li>Gates at the top and bottom of stairs</li><li>Window guards and cord-free blinds</li><li>Smoke and CO alarms on every level</li></ul><a href="{root}guides/childproofing-your-home.html">Room-by-room guide →</a></article>
<article class="card"><div class="ico">🌊</div><h3>Water &amp; outdoor safety</h3><ul><li>Arm's-reach supervision near any water</li><li>Four-sided pool fencing with a self-latching gate</li><li>Life jackets on boats and open water</li><li>Helmets for bikes, scooters and skates</li><li>Sun protection and hydration</li></ul><a href="{root}tools.html#seat">Car seat stage finder →</a></article>
</div></section>
<section class="alt"><div class="container"><div class="callout"><strong>Emergency?</strong> Call your local emergency number immediately. For a suspected poisoning, contact your regional poison control center — keep the number saved in your phone.</div></div></section>
"""

VIDEOS_BODY = """
<section class="hero" style="padding-bottom:10px"><div class="container"><span class="eyebrow">🎬 Auto-updated daily</span><h1>Video library</h1>
<p class="lead">The latest videos from trusted child-health, development and early-learning channels — gathered automatically so you don't have to search.</p>
<div class="pill-row" style="margin-top:14px"><button class="pill active" data-vcat="all">All</button><button class="pill" data-vcat="development">Development</button><button class="pill" data-vcat="health">Health</button><button class="pill" data-vcat="safety">Safety</button><button class="pill" data-vcat="parenting">Parenting</button><button class="pill" data-vcat="learning">Learning with kids</button></div></div></section>
<section><div class="container"><div class="grid g3" id="videos" data-limit="60"><p class="notice">Loading videos…</p></div>
<p class="notice" style="margin-top:16px">Videos are embedded from YouTube in privacy-enhanced mode and belong to their creators. iChild.org is not affiliated with these channels. Want your channel featured? <a href="{root}partners.html">Partner with us</a>.</p></div></section>
<section class="alt"><div class="container"><h2>Browse topics on YouTube</h2><div class="pill-row">
<a class="pill" target="_blank" rel="noopener" href="https://www.youtube.com/results?search_query=baby+developmental+milestones">Baby milestones</a>
<a class="pill" target="_blank" rel="noopener" href="https://www.youtube.com/results?search_query=tummy+time+tips">Tummy time</a>
<a class="pill" target="_blank" rel="noopener" href="https://www.youtube.com/results?search_query=toddler+tantrum+strategies+pediatrician">Toddler tantrums</a>
<a class="pill" target="_blank" rel="noopener" href="https://www.youtube.com/results?search_query=car+seat+installation+tips">Car seat installation</a>
<a class="pill" target="_blank" rel="noopener" href="https://www.youtube.com/results?search_query=infant+cpr+training">Infant CPR</a>
<a class="pill" target="_blank" rel="noopener" href="https://www.youtube.com/results?search_query=speech+development+toddler+tips">Speech development</a>
<a class="pill" target="_blank" rel="noopener" href="https://www.youtube.com/results?search_query=kids+sleep+routine+tips">Sleep routines</a>
<a class="pill" target="_blank" rel="noopener" href="https://www.youtube.com/results?search_query=baby+led+weaning+starting+solids">Starting solids</a></div></div></section>
"""

NEWS_BODY = """
<section class="hero" style="padding-bottom:10px"><div class="container"><span class="eyebrow">📰 Refreshed automatically</span><h1>Child development &amp; parenting research news</h1>
<p class="lead">Headlines from around the web on child development, pediatrics, early education and digital childhood. Links open the original publisher.</p></div></section>
<section><div class="container"><div class="grid g3" id="news" data-limit="40"><p class="notice">Loading headlines…</p></div>
<p class="notice" style="margin-top:16px">Headlines are aggregated automatically and link to the original source. Inclusion is not an endorsement. Read with care and discuss health decisions with your doctor.</p></div></section>
"""

FREE_PLAN_BODY = f"""
<section class="hero"><div class="container hero-grid">
<div><span class="eyebrow">🎁 Free · personalized · 60 seconds</span><h1>Get your child's free development &amp; routine plan</h1>
<p class="lead">Answer a few quick questions and we'll email a plan built for your child's exact age and your biggest challenge — plus monthly updates as they grow.</p>
<div class="grid g2" style="margin-top:20px">
<div class="card"><div class="ico">🧠</div><h3>Next milestones</h3><p>What to watch for in the coming 3 months.</p></div>
<div class="card"><div class="ico">🧸</div><h3>Play ideas</h3><p>Simple activities that build those exact skills.</p></div>
<div class="card"><div class="ico">🌙</div><h3>Routine template</h3><p>Sleep and daily rhythm for their age.</p></div>
<div class="card"><div class="ico">🛡️</div><h3>Safety checks</h3><p>Stage-specific babyproofing and recall alerts.</p></div></div></div>
<div class="card" style="padding:28px">
<form data-form="free-plan" data-steps data-success="🎉 Done! Your personalized plan is on its way. Check your inbox (and promotions folder) within 24–48 hours." novalidate>
<div class="steps"><i></i><i></i><i></i></div>
<div class="step"><h3>1 · About your child</h3>
<label for="fp-age">Child's age</label><select id="fp-age" name="child_age" required><option value="">Select…</option>{AGES}</select>
<label for="fp-kids">Number of children</label><select id="fp-kids" name="children"><option>1</option><option>2</option><option>3</option><option>4+</option></select>
<label>What would help most? (choose any)</label>
<label class="check"><input type="checkbox" name="focus_milestones" value="yes"> Milestones &amp; development</label>
<label class="check"><input type="checkbox" name="focus_sleep" value="yes"> Sleep</label>
<label class="check"><input type="checkbox" name="focus_behavior" value="yes"> Behavior &amp; tantrums</label>
<label class="check"><input type="checkbox" name="focus_feeding" value="yes"> Feeding &amp; picky eating</label>
<label class="check"><input type="checkbox" name="focus_speech" value="yes"> Speech &amp; language</label>
<label class="check"><input type="checkbox" name="focus_school" value="yes"> School readiness &amp; learning</label>
<label class="check"><input type="checkbox" name="focus_screens" value="yes"> Screens &amp; online safety</label>
<button class="btn btn-primary" type="button" data-next style="margin-top:14px">Continue →</button></div>
<div class="step"><h3>2 · About you</h3>
<label for="fp-name">First name</label><input id="fp-name" name="name" required autocomplete="given-name">
<label for="fp-email">Email</label><input id="fp-email" name="email" type="email" required autocomplete="email">
<div class="row"><div><label for="fp-country">Country</label><select id="fp-country" name="country" required><option value="">Select…</option>{COUNTRIES}</select></div>
<div><label for="fp-role">I am a…</label><select id="fp-role" name="role"><option>Parent</option><option>Expecting parent</option><option>Grandparent</option><option>Caregiver / nanny</option><option>Educator</option><option>Health professional</option></select></div></div>
<label for="fp-help">Would you like help finding local services?</label><select id="fp-help" name="service_interest"><option>No, just the plan</option><option>Childcare / daycare</option><option>Tutoring / learning support</option><option>Speech or occupational therapy</option><option>Pediatrician / family doctor</option><option>Parenting classes</option><option>Kids' activities &amp; camps</option></select>
<p style="margin-top:14px"><button class="btn btn-ghost" type="button" data-prev>← Back</button> <button class="btn btn-primary" type="button" data-next>Continue →</button></p></div>
<div class="step"><h3>3 · Almost done</h3>
<label for="fp-note">Anything else we should know? (optional)</label><textarea id="fp-note" name="note" rows="4" placeholder="e.g. My 2-year-old wakes at 5 a.m. every day"></textarea>
<label class="check"><input type="checkbox" name="newsletter" value="yes" checked> Send me the monthly iChild newsletter with age-based tips</label>
<label class="check"><input type="checkbox" name="partner_offers" value="yes"> I'd like to hear about relevant offers from trusted iChild partners</label>
{HP}{CONSENT}
<p style="margin-top:14px"><button class="btn btn-ghost" type="button" data-prev>← Back</button> <button class="btn btn-primary" type="submit">Send my free plan 🎁</button></p>
<p class="form-msg" aria-live="polite"></p></div>
</form></div></div></section>
<section class="alt"><div class="container grid g2"><div><h2>Looking for a provider?</h2><p>Need childcare, a tutor, a speech therapist or kids' activities near you? Tell us what you need and we'll share options from partners in your area as our network grows.</p></div>
<form class="card" data-form="service-referral" data-success="Thanks! We'll reply with options in your area." novalidate>
<div class="row"><div><label for="sr-name">Name</label><input id="sr-name" name="name" required></div><div><label for="sr-email">Email</label><input id="sr-email" name="email" type="email" required></div></div>
<div class="row"><div><label for="sr-need">Service</label><select id="sr-need" name="service" required><option value="">Select…</option><option>Childcare / daycare</option><option>Nanny / babysitter</option><option>Tutoring</option><option>Speech therapy</option><option>Occupational therapy</option><option>Pediatrician</option><option>Swim / sports / arts classes</option><option>Summer camp</option></select></div>
<div><label for="sr-city">City / postal code</label><input id="sr-city" name="location" required></div></div>
<div class="row"><div><label for="sr-age">Child's age</label><select id="sr-age" name="child_age"><option value="">Select…</option>{AGES}</select></div><div><label for="sr-when">Start</label><select id="sr-when" name="timeline"><option>As soon as possible</option><option>Within 1 month</option><option>1–3 months</option><option>Just researching</option></select></div></div>
{HP}{CONSENT}<button class="btn btn-teal" type="submit" style="margin-top:12px">Request options</button><p class="form-msg" aria-live="polite"></p></form></div></section>
<section><div class="container"><h2>Questions</h2>{faq([("How quickly will I get my plan?", "Most plans go out within 24–48 hours. Check your promotions or spam folder if you don't see it."), ("Is it really free?", "Yes. The plan and newsletter are free. iChild is supported by ads, partners and optional contributions."), ("Will you share my email?", "We never sell personal data. If you opt in to partner offers, we only introduce you to relevant partners with your permission."), ("Can I unsubscribe?", "Anytime — every email includes an unsubscribe link, or contact us and we'll remove you.")])}</div></section>
"""

PARTNERS_BODY = f"""
<section class="hero"><div class="container"><span class="eyebrow">🤝 Advertising · sponsorship · partnerships</span><h1>Reach parents when it matters</h1>
<p class="lead">iChild.org reaches parents and caregivers at high-intent moments — checking milestones, planning sleep, comparing childcare costs and checking product safety. Let's build something useful together.</p>
<p class="hero-cta"><a class="btn btn-primary" href="#partner-form">Start a conversation</a><a class="btn btn-ghost" href="{INQ}" target="_blank" rel="noopener">Domain / website acquisition inquiry</a></p></div></section>
<section class="alt"><div class="container grid g3">
{card("🧰", "Sponsor a tool", "Put your brand on a high-use calculator (sleep, childcare cost, car seat) with a clearly labeled sponsorship.", "#partner-form", "Sponsorship")}
{card("📍", "Get listed for local leads", "Childcare centers, tutors, therapists and activity providers can receive opted-in referral requests.", "#partner-form", "Lead gen")}
{card("📰", "Sponsored guides &amp; newsletter", "Clearly disclosed sponsored content and newsletter placements matched to child age.", "#partner-form", "Content")}
{card("🎁", "Contest prize partner", "Fund monthly family contest prizes and get featured to every entrant.", "{root}contests.html", "Engagement")}
{card("🎬", "Video &amp; creator collabs", "Feature your educational channel in our auto-updating video library.", "#partner-form", "Video")}
{card("📄", "Content licensing", "License our plain-language guides and tools for your clinic, school or app.", "#partner-form", "Licensing")}
</div></section>
<section><div class="container grid g2" style="align-items:start">
<div><h2>Our partner standards</h2><ul><li>All sponsorships and ads are clearly labeled.</li><li>We do not accept advertising for products that conflict with public child-safety guidance (for example inclined infant sleepers, or products under active recall).</li><li>Sponsors never influence editorial guidance.</li><li>Leads are only shared with explicit parent consent.</li><li>We never market directly to children.</li></ul>
<h3>Who we work with</h3><p>Baby &amp; kids brands, childcare and education providers, family health services, ed-tech and kids' apps, insurers and family-finance products, publishers and nonprofits.</p></div>
<form class="card" id="partner-form" data-form="partnership" data-success="Thank you! Our partnerships team will reply within 2 business days." novalidate>
<h3 style="margin-top:0">Partnership inquiry</h3>
<div class="row"><div><label for="pa-name">Your name</label><input id="pa-name" name="name" required></div><div><label for="pa-email">Work email</label><input id="pa-email" name="email" type="email" required></div></div>
<div class="row"><div><label for="pa-org">Organization</label><input id="pa-org" name="organization" required></div><div><label for="pa-web">Website</label><input id="pa-web" name="website" type="url" placeholder="https://"></div></div>
<div class="row"><div><label for="pa-type">Interest</label><select id="pa-type" name="interest" required><option value="">Select…</option><option>Advertising / display</option><option>Tool sponsorship</option><option>Sponsored content / newsletter</option><option>Local provider listing &amp; leads</option><option>Contest prize partner</option><option>Content licensing</option><option>Domain / website acquisition</option><option>Other partnership</option></select></div>
<div><label for="pa-budget">Monthly budget (USD)</label><select id="pa-budget" name="budget"><option>Not sure yet</option><option>Under $500</option><option>$500–$2,000</option><option>$2,000–$10,000</option><option>$10,000+</option></select></div></div>
<label for="pa-msg">Tell us about your goals</label><textarea id="pa-msg" name="message" rows="4" required></textarea>
{HP}{CONSENT}<button class="btn btn-primary" type="submit" style="margin-top:12px">Send inquiry</button><p class="form-msg" aria-live="polite"></p></form>
</div></section>
"""

DONATE_BODY = f"""
<section class="hero"><div class="container hero-grid"><div><span class="eyebrow">💛 Reader-supported</span><h1>Help keep iChild free for every family</h1>
<p class="lead">Your support pays for servers and data feeds, reaches more parents, hires expert writers and reviewers, and funds prizes for our family contests.</p>
<div class="grid g2" style="margin-top:18px">
<div class="card"><div class="ico">⚙️</div><h3>Operations · 40%</h3><p>Hosting, data feeds, tools and security.</p></div>
<div class="card"><div class="ico">📣</div><h3>Promotion &amp; marketing · 25%</h3><p>Reaching new parents, clinics and schools.</p></div>
<div class="card"><div class="ico">🧑‍⚕️</div><h3>Hiring talent · 25%</h3><p>Writers, medical reviewers, translators, video creators.</p></div>
<div class="card"><div class="ico">🏆</div><h3>Contests &amp; prizes · 10%</h3><p>Monthly prizes for kids' art and parent tips.</p></div></div></div>
<div class="card" style="padding:28px">
<h2 style="font-size:1.5rem">Choose your support</h2>
<div class="grid g4" style="grid-template-columns:repeat(4,1fr);gap:10px">
<div class="card tier" data-amount="5" tabindex="0"><div class="amt">$5</div><p class="notice">Coffee</p></div>
<div class="card tier selected" data-amount="15" tabindex="0"><div class="amt">$15</div><p class="notice">Supporter</p></div>
<div class="card tier" data-amount="50" tabindex="0"><div class="amt">$50</div><p class="notice">Champion</p></div>
<div class="card tier" data-amount="250" tabindex="0"><div class="amt">$250</div><p class="notice">Patron</p></div></div>
<form data-form="donation-pledge" data-success="Thank you so much! We'll email you a secure payment link and a receipt within 24 hours." novalidate>
<div class="row"><div><label for="donationAmount">Amount (USD)</label><input id="donationAmount" name="amount" type="number" min="1" value="15" required></div>
<div><label for="dn-freq">Frequency</label><select id="dn-freq" name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div></div>
<label for="dn-use">Direct my support to</label><select id="dn-use" name="designation"><option>Where it's needed most</option><option>Ongoing operations</option><option>Promotion &amp; marketing</option><option>Hiring talent</option><option>Contests &amp; prizes</option></select>
<div class="row"><div><label for="dn-name">Name</label><input id="dn-name" name="name" required></div><div><label for="dn-email">Email</label><input id="dn-email" name="email" type="email" required></div></div>
<label for="dn-pay">Preferred payment method</label><select id="dn-pay" name="payment_method"><option>Card (secure link)</option><option>PayPal</option><option>Bank transfer</option><option>UPI (India)</option><option>Interac e-Transfer (Canada)</option></select>
<label class="check"><input type="checkbox" name="public_thanks" value="yes"> Thank me publicly on the supporters wall</label>
{HP}{CONSENT}<button class="btn btn-primary" type="submit" style="width:100%;justify-content:center;margin-top:12px">Pledge my support 💛</button><p class="form-msg" aria-live="polite"></p></form>
<p class="notice" style="margin-top:10px">iChild.org is an independent, privately operated publication — not a registered charity. Contributions support the website's operations and are not tax-deductible.</p></div></div></section>
<section class="alt"><div class="container grid g3">
{card("🏢", "Corporate sponsorship", "Sponsor a tool, the newsletter or monthly contest prizes.", "{root}partners.html", "Business")}
{card("🎁", "Donate a prize", "Books, toys, learning kits or gift cards for our family contests.", "{root}contests.html#prize", "In-kind")}
{card("🤲", "Volunteer your skills", "Translate guides, review content or help with outreach.", "{root}careers.html", "Time")}
</div></section>
"""

CONTESTS_BODY = f"""
<section class="hero"><div class="container"><span class="eyebrow">🏆 New contests every month</span><h1>Family contests &amp; prizes</h1>
<p class="lead">Celebrate creativity and share what works. Parents and guardians enter on behalf of their family — winners are featured on iChild.org and receive a prize.</p></div></section>
<section><div class="container grid g3">
<article class="card reveal"><div class="ico">🎨</div><span class="tag">Ages 3–12</span><h3>Little Artists Monthly</h3><p>Theme: <strong>"My favorite place"</strong>. Share a photo of your child's drawing or painting (artwork only — no faces).</p><p><strong>Prize:</strong> gift card + featured artwork gallery spot.</p></article>
<article class="card reveal"><div class="ico">💡</div><span class="tag">Parents</span><h3>Parent Hack of the Month</h3><p>Your best tip for bedtime, mealtime, mornings or travel — in 150 words or fewer.</p><p><strong>Prize:</strong> gift card + your tip in our newsletter.</p></article>
<article class="card reveal"><div class="ico">📖</div><span class="tag">Families</span><h3>Story Time Challenge</h3><p>Log 20 shared reading sessions this month and tell us your family's favorite book.</p><p><strong>Prize:</strong> book bundle for 3 random qualifying families.</p></article>
</div></section>
<section class="alt"><div class="container grid g2" style="align-items:start">
<form class="card" data-form="contest-entry" data-success="Entry received — good luck! Winners are announced in the first week of next month." novalidate>
<h2 style="font-size:1.5rem;margin-top:0">Enter a contest</h2>
<label for="ce-contest">Contest</label><select id="ce-contest" name="contest" required><option value="">Select…</option><option>Little Artists Monthly</option><option>Parent Hack of the Month</option><option>Story Time Challenge</option></select>
<div class="row"><div><label for="ce-name">Parent/guardian name</label><input id="ce-name" name="name" required></div><div><label for="ce-email">Email</label><input id="ce-email" name="email" type="email" required></div></div>
<div class="row"><div><label for="ce-child">Child's first name or initial (optional)</label><input id="ce-child" name="child_first_name" maxlength="20"></div><div><label for="ce-country">Country</label><select id="ce-country" name="country" required><option value="">Select…</option>{COUNTRIES}</select></div></div>
<label for="ce-link">Link to entry (Google Drive, Dropbox, etc.)</label><input id="ce-link" name="entry_link" type="url" placeholder="https://">
<label for="ce-text">Your entry / description</label><textarea id="ce-text" name="entry_text" rows="4" required maxlength="1200"></textarea>
<label class="check"><input type="checkbox" name="rules" value="accepted" required> I am the parent/legal guardian, 18+, and accept the official rules below. I confirm the entry contains no child's face, full name or personal details.</label>
{HP}{CONSENT}<button class="btn btn-primary" type="submit" style="margin-top:12px">Submit entry</button><p class="form-msg" aria-live="polite"></p></form>
<div><h2>Official rules (summary)</h2><ol><li><strong>No purchase necessary.</strong> A purchase does not improve your chances.</li><li>Open to parents/legal guardians aged 18+ where permitted by law. Void where prohibited.</li><li>One entry per family per contest each month. Entries close on the last day of the month at 23:59 UTC.</li><li>Little Artists and Parent Hack winners are chosen by a judging panel on creativity, originality and usefulness. Story Time winners are drawn at random from qualifying entries.</li><li>Winners are notified by email and must respond within 14 days. Prize values and any sponsor are posted with each month's announcement.</li><li>By entering, you grant iChild.org a non-exclusive license to display the entry on the site and newsletter with first name/initial only. You keep ownership.</li><li>We never publish children's faces, full names or locations.</li></ol>
<h3 id="prize">Sponsor a prize</h3><p>Brands and readers can donate prizes. <a href="{{root}}partners.html">Become a prize partner</a>.</p></div>
</div></section>
"""

CAREERS_BODY = f"""
<section class="hero"><div class="container"><span class="eyebrow">🧑‍💻 Remote · flexible · mission-driven</span><h1>Careers at iChild</h1>
<p class="lead">Help millions of parents get clear, kind, trustworthy answers. We work remotely with freelancers, contractors and volunteers worldwide.</p></div></section>
<section><div class="container grid g3">
{card("✍️", "Parenting &amp; child-health writer", "Freelance · per article. Turn research into warm, practical guides at a Grade 7 reading level.", "#apply", "Writing")}
{card("🩺", "Medical reviewer", "Contract · pediatricians, pediatric nurses, dietitians, SLPs and OTs to review guides for accuracy.", "#apply", "Clinical")}
{card("🎬", "Video &amp; short-form creator", "Freelance · create explainer videos and reels from our guides and tools.", "#apply", "Video")}
{card("📣", "Community &amp; social media manager", "Part-time · grow our parent community and newsletter.", "#apply", "Marketing")}
{card("🤝", "Partnerships &amp; ad sales", "Commission-based · bring brands and local providers onto iChild.", "#apply", "Sales")}
{card("🌍", "Translators &amp; ambassadors", "Volunteer or paid · Spanish, French, Hindi, Arabic, Tamil, Sinhala and more.", "#apply", "Global")}
</div></section>
<section class="alt" id="apply"><div class="container grid g2" style="align-items:start">
<div><h2>How we work</h2><ul><li>100% remote, asynchronous-first</li><li>Paid per project or per hour, agreed in writing up front</li><li>Clear editorial standards and style guide</li><li>Your name credited on your work</li></ul><p>We welcome applicants of every background, especially parents and caregivers returning to work.</p></div>
<form class="card" data-form="job-application" data-success="Application received — thank you! We review applications weekly and will reply if there's a match." novalidate>
<h3 style="margin-top:0">Apply now</h3>
<label for="ja-role">Role</label><select id="ja-role" name="role" required><option value="">Select…</option><option>Writer</option><option>Medical reviewer</option><option>Video creator</option><option>Community &amp; social media</option><option>Partnerships &amp; ad sales</option><option>Translator / ambassador</option><option>Other</option></select>
<div class="row"><div><label for="ja-name">Full name</label><input id="ja-name" name="name" required></div><div><label for="ja-email">Email</label><input id="ja-email" name="email" type="email" required></div></div>
<div class="row"><div><label for="ja-loc">Location / time zone</label><input id="ja-loc" name="location" required></div><div><label for="ja-rate">Expected rate</label><input id="ja-rate" name="rate" placeholder="e.g. $40/hour"></div></div>
<label for="ja-port">Portfolio, LinkedIn or CV link</label><input id="ja-port" name="portfolio" type="url" placeholder="https://" required>
<label for="ja-why">Why iChild? (and relevant credentials)</label><textarea id="ja-why" name="message" rows="4" required></textarea>
{HP}{CONSENT}<button class="btn btn-primary" type="submit" style="margin-top:12px">Submit application</button><p class="form-msg" aria-live="polite"></p></form>
</div></section>
"""

CONTACT_BODY = f"""
<section class="hero" style="padding-bottom:10px"><div class="container"><h1>Contact iChild</h1><p class="lead">Questions, corrections, partnership ideas or feedback — we read every message.</p></div></section>
<section><div class="container grid g2" style="align-items:start">
<form class="card" data-form="contact" data-success="Thanks for reaching out! We usually reply within 2 business days." novalidate>
<div class="row"><div><label for="ct-name">Name</label><input id="ct-name" name="name" required></div><div><label for="ct-email">Email</label><input id="ct-email" name="email" type="email" required></div></div>
<label for="ct-topic">Topic</label><select id="ct-topic" name="topic"><option>General question</option><option>Correction / content feedback</option><option>Advertising &amp; sponsorship</option><option>Partnership</option><option>Press / media</option><option>Domain or website acquisition</option><option>Privacy request</option><option>Technical issue</option></select>
<label for="ct-msg">Message</label><textarea id="ct-msg" name="message" rows="6" required></textarea>
{HP}{CONSENT}<button class="btn btn-primary" type="submit" style="margin-top:12px">Send message</button><p class="form-msg" aria-live="polite"></p></form>
<div><div class="card"><h3>Interested in this website or domain?</h3><p>For acquisition of the iChild.org domain or website, sponsorship, advertising or partnership:</p><p><a class="btn btn-teal" href="{INQ}" target="_blank" rel="noopener">Contact the owner</a></p></div>
<div class="card" style="margin-top:20px"><h3>Prefer email?</h3><p>Use our secure email link — your mail app will open with the address filled in.</p><p><a class="btn btn-ghost" href="#" data-mail="Website inquiry">✉️ Email iChild</a></p></div>
<div class="callout"><strong>We can't give individual medical advice.</strong> For concerns about your child's health, contact your doctor. In an emergency, call your local emergency number.</div></div>
</div></section>
"""

ABOUT_BODY = f"""
<section class="hero"><div class="container article"><span class="eyebrow">💛 Our mission</span><h1>About iChild.org</h1>
<p class="lead">iChild.org helps parents and caregivers raise healthy, confident children with free, practical tools and plain-language guidance — from pregnancy to age 12.</p>
<h2>What we do</h2><p>Parenting information is everywhere, but it is often scattered, contradictory or buried under jargon. We bring the most useful pieces together in one fast, friendly place: interactive milestone checklists, calculators for everyday decisions, live product-recall alerts, an auto-updating video library and guides written for real life.</p>
<h2>How we're different</h2><ul><li><strong>Tools first.</strong> Answers you can act on in seconds.</li><li><strong>Private by design.</strong> Calculators run in your browser; checklist progress stays on your device.</li><li><strong>Always fresh.</strong> Recall alerts, research news and videos refresh automatically several times a day.</li><li><strong>Grounded in public guidance.</strong> Our guides draw on recommendations from national health agencies and pediatric professional bodies. See our <a href="{{root}}editorial-policy.html">editorial policy</a>.</li></ul>
<h2>Who we serve</h2><p>Parents, expecting parents, grandparents, nannies, early-childhood educators and anyone caring for a child. iChild.org is written for adults and is not directed at children.</p>
<h2>How we're funded</h2><p>iChild.org is free to use and supported by advertising (including Google AdSense), clearly labeled partnerships and optional reader contributions. Advertisers never influence our editorial guidance.</p>
<h2>Independence</h2><p>iChild.org is an independent publication. It is not affiliated with any government agency, hospital, charity or company referenced on the site, or with any business using a similar name. See our <a href="{{root}}trademark.html">trademark &amp; copyright disclosure</a>.</p>
<p class="hero-cta"><a class="btn btn-primary" href="{{root}}contact.html">Contact us</a><a class="btn btn-ghost" href="{{root}}careers.html">Join the team</a></p></div></section>
"""


def legal(title, updated, sections):
    body = "".join(f"<h2>{h}</h2>{t}" for h, t in sections)
    return f'<section><div class="container article"><h1>{title}</h1><p class="meta">Last updated: {updated}</p>{body}</div></section>'


UPD = "November 18, 2026"
PRIVACY_BODY = legal("Privacy policy", UPD, [
    ("Overview", "<p>This policy explains what information iChild.org (\"we\", \"us\") collects, how we use it and your choices. By using the site you agree to this policy.</p>"),
    ("Information you give us", "<p>When you submit a form (free plan, referral request, partnership inquiry, donation pledge, contest entry, job application or contact form) we receive the details you enter, such as your name, email, country, your child's age range and your message. We use this only to respond to you, deliver what you requested and — if you opted in — send our newsletter or introduce relevant partners.</p><p>Form submissions are transmitted securely through a third-party form-processing service to our private inbox.</p>"),
    ("Information that stays on your device", "<p>Our calculators and the milestone checker run entirely in your browser. Checklist progress, baby-name shortlists and your theme preference are stored in your browser's local storage and never sent to us. You can clear them anytime by clearing site data.</p>"),
    ("Children's privacy", "<p>iChild.org is a general-audience website directed at adults (parents and caregivers). We do not knowingly collect personal information from children under 13 (or the applicable age in your country). Forms require users to confirm they are 18 or older. Contest entries must not include a child's face, full name or location. If you believe a child has sent us personal information, contact us and we will delete it.</p>"),
    ("Advertising and Google AdSense", "<p>We use Google AdSense to show ads. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits to our site and/or other sites on the Internet.</p><p>You may opt out of personalized advertising by visiting <a href=\"https://adssettings.google.com\" target=\"_blank\" rel=\"noopener\">Google Ads Settings</a> or <a href=\"https://www.aboutads.info/choices\" target=\"_blank\" rel=\"noopener\">www.aboutads.info</a>. Learn more about <a href=\"https://policies.google.com/technologies/partner-sites\" target=\"_blank\" rel=\"noopener\">how Google uses information from sites that use its services</a>.</p>"),
    ("Cookies and analytics", "<p>We use essential cookies/local storage for site features, and advertising cookies as described above. See our <a href=\"{root}cookies.html\">cookie policy</a>.</p>"),
    ("Embedded content", "<p>Videos are embedded from YouTube in privacy-enhanced mode and load only when you press play. Embedded content behaves as if you visited the other website and is subject to its privacy policy.</p>"),
    ("Sharing", "<p>We do not sell your personal information. We share it only with service providers that help us run the site (hosting, form processing, email), with partners when you have explicitly opted in, or when required by law.</p>"),
    ("Retention and security", "<p>We keep submissions only as long as needed for the purpose you gave them, then delete them. The site is served over HTTPS.</p>"),
    ("Your rights", "<p>Depending on where you live (including under GDPR, UK GDPR, PIPEDA, CCPA/CPRA and India's DPDP Act) you may have the right to access, correct, delete or port your data, and to withdraw consent or object to processing. To exercise these rights, use our <a href=\"{root}contact.html\">contact form</a> and choose \"Privacy request\".</p>"),
    ("Changes", "<p>We may update this policy and will change the date above when we do.</p>"),
])
TERMS_BODY = legal("Terms of use", UPD, [
    ("Acceptance", "<p>By accessing iChild.org you agree to these terms. If you do not agree, please do not use the site.</p>"),
    ("Educational purpose only", "<p>All content, tools and calculators are provided for general educational purposes and are not medical, legal or financial advice. See our <a href=\"{root}disclaimer.html\">medical disclaimer</a>.</p>"),
    ("Acceptable use", "<p>You agree not to misuse the site, submit unlawful or harmful content, attempt to disrupt the service, scrape it at scale, or submit personal information about children beyond what a form requests.</p>"),
    ("Intellectual property", "<p>Original text, design, code and graphics on iChild.org are owned by iChild.org and protected by copyright. You may share links and short quotations with attribution. Third-party content (videos, headlines, recall notices, trademarks) belongs to its respective owners.</p>"),
    ("User submissions", "<p>When you submit contest entries, tips or feedback you grant us a non-exclusive, royalty-free license to display them on iChild.org and in our newsletter. You confirm you have the right to submit them.</p>"),
    ("Third-party links", "<p>We link to external websites for your convenience. We are not responsible for their content or practices.</p>"),
    ("Contributions", "<p>Contributions are voluntary support for the operation of iChild.org, an independent publication that is not a registered charity. Contributions are not tax-deductible and are non-refundable except where required by law.</p>"),
    ("Disclaimer of warranties and liability", "<p>The site is provided \"as is\" without warranties of any kind. To the fullest extent permitted by law, iChild.org is not liable for any loss arising from your use of the site or reliance on its content.</p>"),
    ("Changes", "<p>We may revise these terms at any time by updating this page.</p>"),
])
DISCLAIMER_BODY = legal("Medical disclaimer", UPD, [
    ("Not medical advice", "<p>The information on iChild.org — including guides, milestone checklists, calculators, videos and news — is for general education only. It is not intended to diagnose, treat, cure or prevent any condition and is not a substitute for professional medical advice, diagnosis or treatment.</p>"),
    ("Always consult a professional", "<p>Always seek the advice of your pediatrician, family doctor, nurse or other qualified health provider with any questions about your child's health or development. Never disregard professional advice or delay seeking it because of something you read on this site.</p>"),
    ("Emergencies", "<p>If you think your child may have a medical emergency, call your local emergency number immediately. For a suspected poisoning, contact your regional poison control center.</p>"),
    ("Tools and calculators", "<p>Calculators give estimates based on general formulas and population guidance. Results may not apply to your child, especially for children born prematurely or with health conditions.</p>"),
    ("Third-party content", "<p>Videos, news headlines and recall notices come from third parties. We do not control or endorse their content; always check the original source.</p>"),
])
COOKIES_BODY = legal("Cookie policy", UPD, [
    ("What are cookies?", "<p>Cookies and similar technologies (like local storage) are small files stored on your device that help websites work and remember preferences.</p>"),
    ("Essential", "<p>We use local storage to remember your theme, cookie choice, milestone progress and name shortlist. These never leave your device.</p>"),
    ("Advertising", "<p>Google AdSense and its partners may set cookies to serve and measure ads, including personalized ads where permitted. Manage these at <a href=\"https://adssettings.google.com\" target=\"_blank\" rel=\"noopener\">Google Ads Settings</a>. In the EEA, UK and Switzerland, Google requires consent through a certified consent management platform before personalized ads are shown.</p>"),
    ("Embedded media", "<p>YouTube videos load from youtube-nocookie.com only after you press play.</p>"),
    ("Your choices", "<p>Use the cookie banner, your browser settings, or the links above to control cookies. Blocking some cookies may affect site features.</p>"),
])
TRADEMARK_BODY = legal("Trademark &amp; copyright disclosure", UPD, [
    ("Our name", "<p>\"iChild.org\" is the domain name and descriptive title of this independent website, read as \"i child\" — information for every child. We use it only to identify this website.</p>"),
    ("No affiliation", "<p>iChild.org is <strong>not affiliated with, endorsed by, sponsored by or connected to</strong> any company, product, app, school, charity or organization that uses the word \"iChild\", \"i-Child\" or a similar name or mark, in any country. Any such names or marks belong to their respective owners. We do not use the \"i\"-prefix in reference to, or to suggest connection with, any technology company's product line.</p>"),
    ("Third-party marks", "<p>Names of agencies, organizations, YouTube channels, publishers and brands mentioned on this site (for example in recall notices, sources or video credits) are trademarks of their respective owners and are used only for identification and reference (nominative fair use). Their mention does not imply endorsement.</p>"),
    ("Copyright", "<p>© 2026 iChild.org. Original text, layout, graphics, code and tools on this site are protected by copyright. Videos, headlines and recall notices remain the property of their owners and are linked or embedded using the owners' public sharing features.</p>"),
    ("Infringement notices", "<p>If you believe content on iChild.org infringes your trademark or copyright, send a notice through our <a href=\"{root}contact.html\">contact form</a> including: your contact details, the work or mark concerned, the URL of the material, a statement of good-faith belief and a statement that the information is accurate and that you are authorized to act. We respond promptly and remove infringing material where appropriate.</p>"),
])
EDITORIAL_BODY = legal("Editorial policy", UPD, [
    ("Our standards", "<p>Every guide is written in plain language, aims for accuracy, and is checked against current public guidance from national health agencies and professional pediatric bodies. We update content when guidance changes.</p>"),
    ("Sources", "<p>We prioritize government health agencies, peer-reviewed research and professional medical organizations. We avoid presenting single studies as settled fact.</p>"),
    ("Review", "<p>As our team grows, guides are reviewed by qualified professionals (pediatric nurses, physicians, dietitians and therapists). Review status is shown on each guide.</p>"),
    ("Independence from advertising", "<p>Advertisers and sponsors have no input into editorial content. Sponsored material is always labeled.</p>"),
    ("Corrections", "<p>Spotted an error? Tell us through the <a href=\"{root}contact.html\">contact form</a> (choose \"Correction\"). We review every report and fix confirmed errors quickly.</p>"),
])
ACCESS_BODY = legal("Accessibility statement", UPD, [
    ("Our commitment", "<p>We want iChild.org to be usable by everyone. We aim to meet WCAG 2.2 Level AA.</p>"),
    ("What we do", "<ul><li>Semantic HTML, skip links and labeled form fields</li><li>Keyboard-accessible menus, tools and video players</li><li>Dark mode and respect for reduced-motion settings</li><li>Readable type sizes and color contrast</li></ul>"),
    ("Feedback", "<p>If anything is hard to use, please <a href=\"{root}contact.html\">tell us</a> and we'll fix it.</p>"),
])

PAGES = [
    {"path": "index.html", "title": "iChild.org — Child Development Tools, Milestones & Parenting Guides", "desc": "Free milestone checker, parenting calculators, live children's product recall alerts and practical guides for pregnancy through age 12.", "body": HOME, "tools": True, "schema": faq_schema(FAQ_HOME)},
    {"path": "tools.html", "title": "Free Parenting Tools & Calculators | iChild.org", "desc": "Child age, due date, sleep, height, BMI, screen time, childcare cost, allowance and car seat calculators — free and private.", "body": TOOLS_BODY, "tools": True},
    {"path": "milestones.html", "title": "Developmental Milestone Checker (2 Months–5 Years) | iChild.org", "desc": "Interactive developmental milestone checklists from 2 months to 5 years. Save progress, print for your doctor, and learn when to act early.", "body": MILESTONES_BODY, "tools": True},
    {"path": "baby-names.html", "title": "Baby Name Finder — Meanings & Origins | iChild.org", "desc": "Search 200+ baby names with meanings and origins. Filter by gender and culture, shuffle ideas and build your shortlist.", "body": NAMES_BODY, "tools": True},
    {"path": "safety.html", "title": "Children's Product Recalls & Child Safety Alerts | iChild.org", "desc": "Auto-updated recalls of cribs, car seats, toys and baby gear from official agencies, plus safe sleep and babyproofing checklists.", "body": SAFETY_BODY},
    {"path": "videos.html", "title": "Parenting & Child Development Video Library | iChild.org", "desc": "The latest videos from trusted child-health, development and early-learning channels, updated automatically every day.", "body": VIDEOS_BODY},
    {"path": "news.html", "title": "Child Development & Parenting Research News | iChild.org", "desc": "Daily headlines on child development, pediatrics, early education and kids' digital life.", "body": NEWS_BODY},
    {"path": "free-plan.html", "title": "Free Personalized Child Development Plan | iChild.org", "desc": "Get a free plan for your child's age: upcoming milestones, play ideas, routine template and safety checks — delivered by email.", "body": FREE_PLAN_BODY},
    {"path": "partners.html", "title": "Advertise, Sponsor & Partner with iChild.org", "desc": "Sponsorship, advertising, local provider leads, content licensing and contest partnerships with iChild.org.", "body": PARTNERS_BODY},
    {"path": "donate.html", "title": "Support iChild.org — Keep Parenting Tools Free", "desc": "Support operations, outreach, hiring and family contests that keep iChild.org free for every family.", "body": DONATE_BODY},
    {"path": "contests.html", "title": "Family Contests & Prizes | iChild.org", "desc": "Monthly Little Artists, Parent Hack and Story Time contests with prizes. Free to enter for parents and guardians.", "body": CONTESTS_BODY},
    {"path": "careers.html", "title": "Careers at iChild.org — Remote Writing, Review, Video & Sales Roles", "desc": "Join iChild.org as a writer, medical reviewer, video creator, community manager, partnerships rep or translator.", "body": CAREERS_BODY},
    {"path": "contact.html", "title": "Contact | iChild.org", "desc": "Contact iChild.org for questions, corrections, partnerships, press and privacy requests.", "body": CONTACT_BODY},
    {"path": "about.html", "title": "About iChild.org — Our Mission", "desc": "iChild.org offers free, practical tools and plain-language guidance to help parents raise healthy, confident children.", "body": ABOUT_BODY},
    {"path": "privacy.html", "title": "Privacy Policy | iChild.org", "desc": "How iChild.org collects, uses and protects information, including Google AdSense cookies and children's privacy.", "body": PRIVACY_BODY},
    {"path": "terms.html", "title": "Terms of Use | iChild.org", "desc": "Terms governing use of iChild.org.", "body": TERMS_BODY},
    {"path": "disclaimer.html", "title": "Medical Disclaimer | iChild.org", "desc": "iChild.org provides general education, not medical advice.", "body": DISCLAIMER_BODY},
    {"path": "cookies.html", "title": "Cookie Policy | iChild.org", "desc": "How iChild.org uses cookies and local storage.", "body": COOKIES_BODY},
    {"path": "trademark.html", "title": "Trademark & Copyright Disclosure | iChild.org", "desc": "iChild.org trademark, affiliation and copyright disclosure.", "body": TRADEMARK_BODY},
    {"path": "editorial-policy.html", "title": "Editorial Policy | iChild.org", "desc": "How iChild.org researches, writes, reviews and corrects content.", "body": EDITORIAL_BODY},
    {"path": "accessibility.html", "title": "Accessibility Statement | iChild.org", "desc": "iChild.org's commitment to accessibility.", "body": ACCESS_BODY},
]
