# iChild.org

Free child-development tools, milestone checklists, live recall alerts and parenting guides. It's a static site hosted on GitHub Pages from the `main` branch, at the repo root.

- `scripts/build.py` regenerates all HTML pages from `scripts/content.py` and `scripts/articles.py`. Run it with `python3 scripts/build.py`.
- `scripts/update_data.py` refreshes `data/recalls.json`, `data/news.json` and `data/videos.json`. It runs automatically through `.github/workflows/auto-refresh.yml` every 6 hours.
- All forms post through FormSubmit to a private inbox. The address is assembled at runtime and never appears in the HTML.
- AdSense: the auto-ads script is in every page's `<head>`, and `ads.txt` is at the root.

See `RESEARCH.md` for the niche research and `PROMPT.md` for the phase-wise build prompt.
