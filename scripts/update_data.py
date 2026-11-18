#!/usr/bin/env python3
"""Daily auto-refresh for iChild.org.

Pulls fresh, public data and writes small JSON files the static site reads:
  data/recalls.json  - children's product recalls (US CPSC + Health Canada)
  data/news.json     - child development & parenting research headlines
  data/videos.json   - latest videos from trusted child-health YouTube channels
Every source is optional: if one fails, the previous file is kept.
Standard library only, so it runs on a bare GitHub Actions runner.
"""
import datetime as dt
import json
import os
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html import unescape

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
UA = {"User-Agent": "Mozilla/5.0 (compatible; iChildBot/1.0; +https://ichild.org)"}
NOW = dt.datetime.now(dt.timezone.utc)

KID_WORDS = re.compile(
    r"\b(child|children|kid|kids|baby|babies|infant|toddler|crib|bassinet|stroller|car seat|"
    r"high ?chair|pacifier|toy|toys|teether|sleeper|onesie|bib|playpen|play yard|walker|"
    r"youth|juvenile|nursery|bunk bed|bike helmet|swing|rattle|doll|puzzle|crayon|backpack|"
    r"button batter|magnet|pajama|diaper)\b",
    re.I,
)


def get(url, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def load(name):
    try:
        with open(os.path.join(ROOT, name), encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"updated": None, "items": []}


def save(name, items):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        json.dump({"updated": NOW.isoformat(), "items": items}, f, ensure_ascii=False, indent=1)
    print(f"wrote {name}: {len(items)} items")


# ---------------- Recalls ----------------
def cpsc():
    start = (NOW - dt.timedelta(days=150)).strftime("%Y-%m-%d")
    data = json.loads(get(f"https://www.saferproducts.gov/RestWebServices/Recall?format=json&RecallDateStart={start}"))
    out = []
    for r in data:
        title = r.get("Title") or ""
        prods = " ".join((p.get("Name") or "") + " " + (p.get("Type") or "") for p in r.get("Products") or [])
        blob = f"{title} {prods} {r.get('Description') or ''}"
        if not KID_WORDS.search(blob):
            continue
        hazard = "; ".join(h.get("Name", "") for h in r.get("Hazards") or [] if h.get("Name"))
        out.append({
            "date": (r.get("RecallDate") or "")[:10],
            "source": "US CPSC",
            "title": title.strip(),
            "hazard": hazard[:280],
            "url": r.get("URL") or "https://www.cpsc.gov/Recalls",
        })
    return out


def health_canada():
    data = json.loads(get("https://healthycanadians.gc.ca/recall-alert-rappel-avis/api/recent/en"))
    res = data.get("results", {})
    pool = (res.get("CPS") or []) + (res.get("ALL") or [])
    out, seen = [], set()
    for r in pool:
        title = r.get("title") or ""
        if not KID_WORDS.search(title) or title in seen:
            continue
        seen.add(title)
        ts = r.get("date_published")
        try:
            date = dt.datetime.fromtimestamp(int(ts), dt.timezone.utc).strftime("%Y-%m-%d")
        except Exception:
            date = ""
        url = r.get("url") or ""
        if url.startswith("/"):
            url = "https://recalls-rappels.canada.ca" + url
        out.append({"date": date, "source": "Health Canada", "title": title.strip(), "hazard": "", "url": url or "https://recalls-rappels.canada.ca"})
    return out


def recalls():
    items = []
    for fn in (cpsc, health_canada):
        try:
            items += fn()
        except Exception as e:  # keep going on any single-source failure
            print("recall source failed:", fn.__name__, e)
    if not items:
        return
    items.sort(key=lambda x: x["date"], reverse=True)
    save("recalls.json", items[:80])


# ---------------- News ----------------
NEWS_QUERIES = [
    "child development study",
    "parenting research",
    "pediatrics new guidance children",
    "early childhood education",
    "children screen time study",
]


def news():
    items, seen = [], set()
    for q in NEWS_QUERIES:
        url = "https://news.google.com/rss/search?q=" + urllib.parse.quote(q + " when:14d") + "&hl=en-US&gl=US&ceid=US:en"
        try:
            root = ET.fromstring(get(url))
        except Exception as e:
            print("news failed:", q, e)
            continue
        for it in root.iter("item"):
            title = unescape(it.findtext("title") or "").strip()
            src = it.find("source")
            source = src.text if src is not None else ""
            if source and title.endswith(" - " + source):
                title = title[: -len(source) - 3]
            key = title.lower()[:80]
            if not title or key in seen:
                continue
            seen.add(key)
            pub = it.findtext("pubDate") or ""
            try:
                d = dt.datetime.strptime(pub[:25], "%a, %d %b %Y %H:%M:%S").strftime("%Y-%m-%d")
            except Exception:
                d = ""
            items.append({"title": title, "source": source, "date": d, "url": it.findtext("link")})
    if items:
        items.sort(key=lambda x: x["date"], reverse=True)
        save("news.json", items[:40])


# ---------------- Videos ----------------
# (handle, topic) — trusted public channels on child health, development and learning.
CHANNELS = [
    ("@Pathwaysorg", "development"),
    ("@CDCgov", "health"),
    ("@AmerAcadPeds", "health"),
    ("@ChildMindInstitute", "parenting"),
    ("@HarvardCenterontheDevelopingChild", "development"),
    ("@ZEROTOTHREE", "development"),
    ("@raisingchildrennetwork", "parenting"),
    ("@unicef", "parenting"),
    ("@SesameStreet", "learning"),
    ("@KhanAcademyKids", "learning"),
    ("@commonsensemedia", "parenting"),
    ("@NemoursKidsHealth", "health"),
]
SAFETY_WORDS = re.compile(r"(safe|safety|car seat|drown|poison|sleep|injur|recall|choking)", re.I)
NS = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015", "m": "http://search.yahoo.com/mrss/"}


def channel_id(handle):
    html = get("https://www.youtube.com/" + handle).decode("utf-8", "ignore")
    m = re.search(r'"(?:externalId|channelId)":"(UC[\w-]{22})"', html) or re.search(r"channel_id=(UC[\w-]{22})", html)
    return m.group(1) if m else None


def videos():
    items = []
    for handle, topic in CHANNELS:
        try:
            cid = channel_id(handle)
            if not cid:
                continue
            feed = ET.fromstring(get("https://www.youtube.com/feeds/videos.xml?channel_id=" + cid))
            chan = feed.findtext("a:title", default=handle, namespaces=NS)
            for e in feed.findall("a:entry", NS)[:6]:
                vid = e.findtext("yt:videoId", namespaces=NS)
                title = e.findtext("a:title", default="", namespaces=NS)
                link = e.find("a:link", NS)
                if link is not None and "/shorts/" in (link.get("href") or ""):
                    continue
                t = "safety" if SAFETY_WORDS.search(title) else topic
                items.append({"id": vid, "title": title, "channel": chan, "topic": t, "date": (e.findtext("a:published", default="", namespaces=NS) or "")[:10]})
        except Exception as ex:
            print("video channel failed:", handle, ex)
    if items:
        items.sort(key=lambda x: x["date"], reverse=True)
        save("videos.json", items[:72])


if __name__ == "__main__":
    recalls()
    news()
    videos()
