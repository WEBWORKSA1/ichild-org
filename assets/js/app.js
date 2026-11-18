/* iChild.org — core site script */
(function () {
  "use strict";
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const store = {
    get(k, d) { try { const v = localStorage.getItem(k); return v === null ? d : JSON.parse(v); } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  };
  window.iChildStore = store;

  /* ---------- Theme ---------- */
  const root = document.documentElement;
  const saved = store.get("ic-theme", null);
  if (saved) root.dataset.theme = saved;
  else if (window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches) root.dataset.theme = "dark";
  const tBtn = $("#themeToggle");
  const paintTheme = () => { if (tBtn) tBtn.textContent = root.dataset.theme === "dark" ? "☀️" : "🌙"; };
  paintTheme();
  tBtn && tBtn.addEventListener("click", () => {
    root.dataset.theme = root.dataset.theme === "dark" ? "light" : "dark";
    store.set("ic-theme", root.dataset.theme); paintTheme();
  });

  /* ---------- Mobile menu ---------- */
  const mBtn = $("#menuBtn"), links = $("#navLinks");
  mBtn && mBtn.addEventListener("click", () => {
    const open = links.classList.toggle("open");
    mBtn.setAttribute("aria-expanded", open);
  });

  /* ---------- Year ---------- */
  $$(".year").forEach(e => (e.textContent = new Date().getFullYear()));

  /* ---------- Reveal on scroll ---------- */
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }), { threshold: 0.12 });
    $$(".reveal").forEach(el => io.observe(el));
  } else $$(".reveal").forEach(el => el.classList.add("in"));

  /* ---------- Cookie consent ---------- */
  const consent = $("#consent");
  if (consent && !store.get("ic-consent", null)) consent.classList.add("show");
  $$("[data-consent]").forEach(b => b.addEventListener("click", () => {
    store.set("ic-consent", b.dataset.consent);
    consent.classList.remove("show");
  }));

  /* ---------- Protected inbox (never rendered in the page) ---------- */
  const inbox = () => ["moc.liamg", "@", "1askrowbew"].join("").split("").reverse().join("");

  /* ---------- Forms (lead gen, donations, contests, careers, contact) ---------- */
  $$("form[data-form]").forEach(form => {
    form.addEventListener("submit", async ev => {
      ev.preventDefault();
      const msg = $(".form-msg", form) || form.appendChild(Object.assign(document.createElement("p"), { className: "form-msg" }));
      if (form.querySelector(".hp input") && form.querySelector(".hp input").value) return; // bot
      if (!form.checkValidity()) { form.reportValidity(); return; }
      const data = Object.fromEntries(new FormData(form).entries());
      delete data._gotcha;
      const kind = form.dataset.form;
      const payload = Object.assign({
        _subject: "iChild.org — " + kind + " submission",
        _template: "table",
        _captcha: "false",
        form: kind,
        page: location.href,
        submitted: new Date().toISOString()
      }, data);
      const btn = form.querySelector("[type=submit]");
      btn && (btn.disabled = true);
      msg.className = "form-msg"; msg.textContent = "Sending…";
      try {
        const r = await fetch("https://formsubmit.co/ajax/" + inbox(), {
          method: "POST",
          headers: { "Content-Type": "application/json", Accept: "application/json" },
          body: JSON.stringify(payload)
        });
        if (!r.ok) throw new Error("bad status");
        msg.className = "form-msg ok";
        msg.textContent = form.dataset.success || "Thank you! We received your submission and will be in touch shortly.";
        form.reset();
        const st = store.get("ic-submissions", 0); store.set("ic-submissions", st + 1);
        if (window.gtag) gtag("event", "generate_lead", { form: kind });
      } catch (e) {
        msg.className = "form-msg err";
        msg.innerHTML = 'We could not reach our server. <a href="#" class="mail-fallback">Send by email instead</a>.';
        const a = $(".mail-fallback", msg);
        a.addEventListener("click", x => {
          x.preventDefault();
          const body = Object.entries(payload).map(([k, v]) => k + ": " + v).join("\n");
          location.href = "mailto:" + inbox() + "?subject=" + encodeURIComponent(payload._subject) + "&body=" + encodeURIComponent(body);
        });
      } finally { btn && (btn.disabled = false); }
    });
  });

  /* Generic "email us" links: <a data-mail="Subject">…</a> */
  $$("a[data-mail]").forEach(a => a.addEventListener("click", e => {
    e.preventDefault();
    location.href = "mailto:" + inbox() + "?subject=" + encodeURIComponent("iChild.org — " + (a.dataset.mail || "Inquiry"));
  }));

  /* ---------- Multi-step forms ---------- */
  $$("[data-steps]").forEach(f => {
    const steps = $$(".step", f), bars = $$(".steps i", f);
    let i = 0;
    const show = n => { steps.forEach((s, k) => s.classList.toggle("on", k === n)); bars.forEach((b, k) => b.classList.toggle("on", k <= n)); i = n; };
    $$("[data-next]", f).forEach(b => b.addEventListener("click", () => {
      const fields = $$("input,select,textarea", steps[i]);
      for (const fl of fields) if (!fl.checkValidity()) { fl.reportValidity(); return; }
      show(Math.min(i + 1, steps.length - 1));
    }));
    $$("[data-prev]", f).forEach(b => b.addEventListener("click", () => show(Math.max(i - 1, 0))));
    show(0);
  });

  /* ---------- Donation tiers ---------- */
  $$(".tier").forEach(t => t.addEventListener("click", () => {
    $$(".tier").forEach(x => x.classList.remove("selected"));
    t.classList.add("selected");
    const amt = $("#donationAmount"); if (amt) { amt.value = t.dataset.amount; amt.focus(); }
  }));

  /* ---------- Tip of the day (self-rotating) ---------- */
  const tipEl = $("#tipOfDay");
  if (tipEl) {
    fetch(siteRoot() + "data/tips.json").then(r => r.json()).then(tips => {
      const day = Math.floor(Date.now() / 864e5);
      const t = tips[day % tips.length];
      tipEl.innerHTML = '<span class="tag" style="background:#fff8e1;color:#7a5200">' + esc(t.age) + "</span><h3>" + esc(t.title) + "</h3><p>" + esc(t.text) + "</p>";
    }).catch(() => {});
  }

  /* ---------- Data feeds (auto-refreshed daily by GitHub Actions) ---------- */
  function siteRoot() { return document.body.dataset.root || ""; }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c])); }
  window.iChildEsc = esc;

  const recallBox = $("#recalls");
  if (recallBox) {
    const limit = +recallBox.dataset.limit || 50;
    fetch(siteRoot() + "data/recalls.json", { cache: "no-cache" }).then(r => r.json()).then(d => {
      const items = (d.items || []).slice(0, limit);
      const upd = $("#recallsUpdated"); if (upd && d.updated) upd.textContent = new Date(d.updated).toLocaleString();
      if (!items.length) { recallBox.innerHTML = '<p class="notice">Recall feed refreshes daily. Meanwhile, check the official databases linked below.</p>'; return; }
      recallBox.innerHTML = items.map(it => '<article class="card recall"><div class="ico">⚠️</div><div><div class="date">' + esc(it.date) + " · " + esc(it.source) + '</div><h3 style="font-size:1.05rem;margin:.2em 0"><a href="' + esc(it.url) + '" target="_blank" rel="noopener nofollow">' + esc(it.title) + "</a></h3>" + (it.hazard ? '<p style="font-size:.92rem">' + esc(it.hazard) + "</p>" : "") + "</div></article>").join("");
      const f = $("#recallFilter");
      f && f.addEventListener("input", () => {
        const q = f.value.toLowerCase();
        $$(".recall", recallBox).forEach(c => (c.style.display = c.textContent.toLowerCase().includes(q) ? "" : "none"));
      });
    }).catch(() => { recallBox.innerHTML = '<p class="notice">Recall feed is temporarily unavailable.</p>'; });
  }

  const newsBox = $("#news");
  if (newsBox) {
    const limit = +newsBox.dataset.limit || 12;
    fetch(siteRoot() + "data/news.json", { cache: "no-cache" }).then(r => r.json()).then(d => {
      const items = (d.items || []).slice(0, limit);
      if (!items.length) { newsBox.innerHTML = '<p class="notice">Headlines refresh daily.</p>'; return; }
      newsBox.innerHTML = items.map(it => '<article class="card"><span class="tag">' + esc(it.source || "News") + '</span><h3 style="font-size:1.05rem"><a href="' + esc(it.url) + '" target="_blank" rel="noopener nofollow">' + esc(it.title) + '</a></h3><p class="notice">' + esc(it.date || "") + "</p></article>").join("");
    }).catch(() => {});
  }

  const vidBox = $("#videos");
  if (vidBox) {
    const limit = +vidBox.dataset.limit || 24;
    fetch(siteRoot() + "data/videos.json", { cache: "no-cache" }).then(r => r.json()).then(d => {
      let items = d.items || [];
      const render = cat => {
        const list = items.filter(v => !cat || cat === "all" || v.topic === cat).slice(0, limit);
        if (!list.length) { vidBox.innerHTML = '<p class="notice">New videos are added automatically every day.</p>'; return; }
        vidBox.innerHTML = list.map(v => '<article class="card"><div class="video" data-yt="' + esc(v.id) + '" role="button" tabindex="0" aria-label="Play ' + esc(v.title) + '"><img loading="lazy" src="https://i.ytimg.com/vi/' + esc(v.id) + '/hqdefault.jpg" alt=""><span class="play">▶</span></div><span class="tag" style="margin-top:12px">' + esc(v.channel) + '</span><h3 style="font-size:1rem">' + esc(v.title) + "</h3></article>").join("");
        bindVideos(vidBox);
      };
      render("all");
      $$("[data-vcat]").forEach(p => p.addEventListener("click", () => {
        $$("[data-vcat]").forEach(x => x.classList.remove("active")); p.classList.add("active"); render(p.dataset.vcat);
      }));
    }).catch(() => {});
  }
  function bindVideos(scope) {
    $$(".video[data-yt]", scope).forEach(v => {
      const go = () => { v.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + v.dataset.yt + '?autoplay=1&rel=0" title="Video" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>'; };
      v.addEventListener("click", go, { once: true });
      v.addEventListener("keydown", e => { if (e.key === "Enter") go(); });
    });
  }
  window.iChildBindVideos = bindVideos;

  /* ---------- Share ---------- */
  $$("[data-share]").forEach(b => b.addEventListener("click", async () => {
    const d = { title: document.title, url: location.href };
    if (navigator.share) { try { await navigator.share(d); } catch (e) {} }
    else { try { await navigator.clipboard.writeText(location.href); b.textContent = "Link copied ✓"; } catch (e) {} }
  }));

  /* ---------- Newsletter mini-forms also count ---------- */
  const yearsEl = $("#yearsServing"); if (yearsEl) yearsEl.textContent = "Since 2026";
})();
