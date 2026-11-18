/* iChild.org — interactive parenting tools (all calculations run locally in the browser) */
(function () {
  "use strict";
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const store = window.iChildStore;
  const esc = window.iChildEsc || (s => s);
  const show = (el, html) => { el.innerHTML = html; el.classList.add("show"); };
  const DAY = 864e5;

  /* ===== 1. Milestone checker ===== */
  const MILESTONES = {
    "2 months": ["Calms down when spoken to or picked up", "Looks at your face", "Smiles when you talk or smile", "Makes sounds other than crying", "Holds head up during tummy time", "Opens hands briefly"],
    "4 months": ["Smiles on their own to get your attention", "Chuckles when you try to make them laugh", "Makes cooing sounds back at you", "Turns head toward your voice", "Brings hands to mouth", "Holds head steady without support when held"],
    "6 months": ["Knows familiar people", "Likes to look at self in a mirror", "Laughs", "Takes turns making sounds with you", "Reaches to grab a toy", "Rolls from tummy to back", "Leans on hands to support self when sitting"],
    "9 months": ["Shy, clingy or fearful around strangers", "Shows several facial expressions", "Reacts when you leave", "Makes sounds like 'mamamama' and 'babababa'", "Looks for objects dropped out of sight", "Sits without support", "Moves things from one hand to the other"],
    "12 months": ["Plays games with you, like pat-a-cake", "Waves bye-bye", "Calls a parent 'mama', 'dada' or another special name", "Understands 'no'", "Puts something in a container", "Pulls up to stand", "Walks holding on to furniture"],
    "15 months": ["Copies other children while playing", "Shows you an object they like", "Tries to say one or two words besides 'mama' or 'dada'", "Points to ask for something", "Tries to use things the right way (phone, cup, book)", "Takes a few steps alone", "Uses fingers to feed self"],
    "18 months": ["Moves away from you but checks you are close", "Points to show you something interesting", "Tries to say three or more words", "Follows one-step directions without gestures", "Copies you doing chores", "Walks without holding on", "Climbs on and off a couch or chair", "Tries to use a spoon"],
    "2 years": ["Notices when others are hurt or upset", "Looks at your face to see how to react", "Points to things in a book when you ask", "Says at least two words together", "Points to at least two body parts", "Holds something in one hand while using the other", "Kicks a ball", "Runs"],
    "30 months": ["Plays next to and sometimes with other children", "Shows what they can do by saying 'look at me'", "Says about 50 words", "Names things in a book when you point", "Uses things to pretend (feeding a doll)", "Follows two-step instructions", "Takes some clothes off by themselves", "Jumps off the ground with both feet"],
    "3 years": ["Calms down within 10 minutes after you leave", "Notices other children and joins them to play", "Talks with you in conversation using back-and-forth", "Asks 'who', 'what', 'where' or 'why' questions", "Says first name when asked", "Draws a circle when shown how", "Avoids touching hot objects when warned", "Strings items together, like large beads"],
    "4 years": ["Pretends to be something else during play", "Asks to go play with known children", "Comforts others who are hurt or sad", "Says sentences with four or more words", "Names a few colors", "Tells what comes next in a well-known story", "Catches a large ball most of the time", "Unbuttons some buttons"],
    "5 years": ["Follows rules or takes turns when playing games", "Sings, dances or acts for you", "Does simple chores at home", "Tells a story with at least two events", "Answers simple questions about a book after reading", "Counts to 10", "Writes some letters in their name", "Hops on one foot"]
  };
  const msBox = $("#milestoneTool");
  if (msBox) {
    const sel = $("#msAge"), list = $("#msList"), bar = $("#msBar i"), out = $("#msOut");
    Object.keys(MILESTONES).forEach(k => sel.insertAdjacentHTML("beforeend", "<option>" + k + "</option>"));
    const render = () => {
      const age = sel.value, saved = store.get("ic-ms-" + age, []);
      list.innerHTML = MILESTONES[age].map((m, i) => '<li><input type="checkbox" id="ms' + i + '" ' + (saved.includes(i) ? "checked" : "") + '><label for="ms' + i + '" style="margin:0;font-weight:600">' + esc(m) + "</label></li>").join("");
      update();
    };
    const update = () => {
      const age = sel.value, boxes = $$("input", list), done = boxes.map((b, i) => (b.checked ? i : -1)).filter(i => i > -1);
      store.set("ic-ms-" + age, done);
      const pct = Math.round((done.length / boxes.length) * 100);
      bar.style.width = pct + "%";
      out.innerHTML = "<strong>" + done.length + " of " + boxes.length + "</strong> milestones observed (" + pct + "%). " +
        (pct === 100 ? "Wonderful — keep celebrating every new skill!" : pct >= 60 ? "Great progress. Keep playing, reading and talking together every day." : "Every child develops at their own pace. If your child is missing several milestones or has lost skills they once had, share this checklist with your child's doctor.");
      out.classList.add("show");
    };
    sel.addEventListener("change", render);
    list.addEventListener("change", update);
    $("#msPrint") && $("#msPrint").addEventListener("click", () => window.print());
    render();
  }

  /* ===== 2. Child age calculator ===== */
  const ageForm = $("#ageForm");
  ageForm && ageForm.addEventListener("submit", e => {
    e.preventDefault();
    const dob = new Date($("#dob").value), now = new Date();
    if (isNaN(dob) || dob > now) return;
    let y = now.getFullYear() - dob.getFullYear(), m = now.getMonth() - dob.getMonth(), d = now.getDate() - dob.getDate();
    if (d < 0) { m--; d += new Date(now.getFullYear(), now.getMonth(), 0).getDate(); }
    if (m < 0) { y--; m += 12; }
    const days = Math.floor((now - dob) / DAY), weeks = Math.floor(days / 7), months = y * 12 + m;
    let nb = new Date(now.getFullYear(), dob.getMonth(), dob.getDate()); if (nb <= now) nb.setFullYear(nb.getFullYear() + 1);
    const toBday = Math.ceil((nb - now) / DAY);
    show($("#ageOut"), "Your child is <strong>" + y + " years, " + m + " months, " + d + " days</strong> old.<br>That is " + months + " months · " + weeks.toLocaleString() + " weeks · " + days.toLocaleString() + " days.<br>🎂 Next birthday in <strong>" + toBday + " days</strong>.");
  });

  /* ===== 3. Due date calculator ===== */
  const dueForm = $("#dueForm");
  dueForm && dueForm.addEventListener("submit", e => {
    e.preventDefault();
    const lmp = new Date($("#lmp").value), cycle = +$("#cycle").value || 28;
    if (isNaN(lmp)) return;
    const edd = new Date(lmp.getTime() + (280 + (cycle - 28)) * DAY);
    const gest = Math.floor((Date.now() - lmp.getTime() - (cycle - 28) * DAY) / DAY);
    const wk = Math.floor(gest / 7), dd = gest % 7;
    const tri = wk < 14 ? "first" : wk < 28 ? "second" : "third";
    const left = Math.ceil((edd - Date.now()) / DAY);
    show($("#dueOut"), "Estimated due date: <strong>" + edd.toDateString() + "</strong><br>" +
      (gest >= 0 && left >= -14 ? "You are about <strong>" + wk + " weeks " + dd + " days</strong> along (" + tri + " trimester) · <span class='countdown'>" + Math.max(left, 0) + "</span> days to go." : "Check the date you entered.") +
      "<br><span class='notice'>Only about 1 in 20 babies arrive on their exact due date. Your care provider may adjust it after an early ultrasound.</span>");
  });

  /* ===== 4. Sleep needs ===== */
  const sleepForm = $("#sleepForm");
  sleepForm && sleepForm.addEventListener("submit", e => {
    e.preventDefault();
    const months = +$("#sleepAge").value;
    const bands = [[0, 3, "14–17 hours (newborn, across the day and night)", 14, 17], [4, 11, "12–16 hours including naps", 12, 16], [12, 35, "11–14 hours including naps", 11, 14], [36, 71, "10–13 hours including naps", 10, 13], [72, 155, "9–12 hours", 9, 12], [156, 216, "8–10 hours", 8, 10]];
    const b = bands.find(x => months >= x[0] && months <= x[1]);
    const wake = $("#wake").value || "07:00";
    const [h, mi] = wake.split(":").map(Number);
    const mid = (b[3] + b[4]) / 2, napShare = months < 36 ? (months < 12 ? 3.5 : 2) : 0;
    const night = mid - napShare;
    const bed = new Date(2000, 0, 1, h, mi); bed.setMinutes(bed.getMinutes() - night * 60);
    show($("#sleepOut"), "Recommended: <strong>" + b[2] + "</strong> per 24 hours.<br>With a " + wake + " wake-up, aim for lights-out around <strong>" + bed.toTimeString().slice(0, 5) + "</strong>" + (napShare ? " plus about " + napShare + " hours of daytime naps." : ".") + "<br><span class='notice'>Ranges reflect pediatric sleep-medicine consensus guidance. Consistent routines matter more than exact minutes.</span>");
  });

  /* ===== 5. Adult height predictor (mid-parental method) ===== */
  const hForm = $("#heightForm");
  hForm && hForm.addEventListener("submit", e => {
    e.preventDefault();
    const unit = $("#hUnit").value, f = +$("#hDad").value, m = +$("#hMom").value, sex = $("#hSex").value;
    if (!f || !m) return;
    const toCm = v => (unit === "in" ? v * 2.54 : v), fc = toCm(f), mc = toCm(m);
    const t = sex === "boy" ? (fc + mc + 13) / 2 : (fc + mc - 13) / 2;
    const fmt = cm => unit === "in" ? Math.floor(cm / 2.54 / 12) + "′" + Math.round((cm / 2.54) % 12) + "″" : Math.round(cm) + " cm";
    show($("#heightOut"), "Estimated adult height: <strong>" + fmt(t) + "</strong><br>Typical range: " + fmt(t - 8.5) + " – " + fmt(t + 8.5) + "<br><span class='notice'>Mid-parental height is a rough genetic target. Nutrition, sleep and health all play a role.</span>");
  });

  /* ===== 6. Child BMI ===== */
  const bForm = $("#bmiForm");
  bForm && bForm.addEventListener("submit", e => {
    e.preventDefault();
    const u = $("#bUnit").value, w = +$("#bW").value, h = +$("#bH").value;
    if (!w || !h) return;
    const kg = u === "imperial" ? w * 0.453592 : w, m = u === "imperial" ? h * 0.0254 : h / 100;
    const bmi = kg / (m * m);
    show($("#bmiOut"), "BMI: <strong>" + bmi.toFixed(1) + "</strong><br><span class='notice'>For children and teens, BMI must be read as a percentile for age and sex. Plot this number on your country's official growth chart (WHO for under-2s; CDC or WHO 2–19) or ask your pediatrician at the next check-up.</span>");
  });

  /* ===== 7. Screen time planner ===== */
  const stForm = $("#screenForm");
  stForm && stForm.addEventListener("submit", e => {
    e.preventDefault();
    const age = +$("#stAge").value;
    let rule, mins;
    if (age < 1.5) { rule = "Avoid screens other than video-chatting with family."; mins = 0; }
    else if (age < 2) { rule = "If you introduce media, choose high-quality programs and watch together."; mins = 20; }
    else if (age < 6) { rule = "About 1 hour per day of high-quality programming, co-viewed when possible."; mins = 60; }
    else { rule = "Set consistent limits that protect sleep (8–12h), physical activity (60 min/day) and homework."; mins = +$("#stCap").value || 90; }
    const plan = [["Physical play / outdoors", age < 6 ? 180 : 60], ["Reading together", age < 6 ? 20 : 30], ["Screen time (max)", mins], ["Screen-free meals", 0], ["No screens 1h before bed", 0]];
    show($("#screenOut"), "<strong>" + rule + "</strong><div class='table-wrap' style='margin-top:10px'><table><tr><th>Daily habit</th><th>Target</th></tr>" + plan.map(p => "<tr><td>" + p[0] + "</td><td>" + (p[1] ? p[1] + " min" : "✓ every day") + "</td></tr>").join("") + "</table></div>");
  });

  /* ===== 8. Childcare cost estimator ===== */
  const ccForm = $("#careForm");
  ccForm && ccForm.addEventListener("submit", e => {
    e.preventDefault();
    const rate = +$("#ccRate").value, per = $("#ccPer").value, units = +$("#ccUnits").value, kids = +$("#ccKids").value || 1, disc = +$("#ccDisc").value || 0, inc = +$("#ccInc").value || 0;
    const weekly = per === "hour" ? rate * units : per === "day" ? rate * units : rate;
    let total = 0; for (let k = 0; k < kids; k++) total += weekly * (k === 0 ? 1 : 1 - disc / 100);
    const month = total * 52 / 12, year = total * 52;
    show($("#ccOut"), "Weekly: <strong>" + total.toFixed(0) + "</strong> · Monthly: <strong>" + month.toFixed(0) + "</strong> · Yearly: <strong>" + year.toFixed(0) + "</strong>" + (inc ? "<br>That is <strong>" + ((year / inc) * 100).toFixed(1) + "%</strong> of household income." : "") + "<br><span class='notice'>Check employer dependent-care benefits and local childcare subsidies — they can cut this substantially.</span>");
  });

  /* ===== 9. Allowance calculator ===== */
  const alForm = $("#allowForm");
  alForm && alForm.addEventListener("submit", e => {
    e.preventDefault();
    const age = +$("#alAge").value, per = +$("#alPer").value || 1;
    const wk = age * per, s = [+$("#alSave").value || 40, +$("#alSpend").value || 50, +$("#alGive").value || 10];
    const sum = s.reduce((a, b) => a + b, 0) || 100;
    show($("#alOut"), "Suggested weekly allowance: <strong>" + wk.toFixed(2) + "</strong> (" + per + " per year of age).<br>💰 Save " + (wk * s[0] / sum).toFixed(2) + " · 🛍️ Spend " + (wk * s[1] / sum).toFixed(2) + " · 💝 Give " + (wk * s[2] / sum).toFixed(2) + "<br>After one year your child will have saved about <strong>" + (wk * s[0] / sum * 52).toFixed(0) + "</strong>.");
  });

  /* ===== 10. Car seat stage finder ===== */
  const csForm = $("#seatForm");
  csForm && csForm.addEventListener("submit", e => {
    e.preventDefault();
    const age = +$("#csAge").value, h = +$("#csH").value || 0, unit = $("#csUnit").value;
    const inches = unit === "cm" ? h / 2.54 : h;
    let stage, why;
    if (age < 2) { stage = "Rear-facing car seat"; why = "Keep your child rear-facing as long as possible, until they reach the highest weight or height allowed by the seat maker — many seats allow this to age 4 or beyond."; }
    else if (age < 5) { stage = "Rear-facing (if still within limits) or forward-facing with 5-point harness"; why = "Move forward-facing only after outgrowing the rear-facing limits, and use the harness until the seat's top limits."; }
    else if (inches && inches >= 57 && age >= 8) { stage = "Seat belt (if the 5-step test passes)"; why = "Lap belt low across the upper thighs, shoulder belt across the chest, knees bend at the seat edge, feet flat. Children under 13 should ride in the back seat."; }
    else { stage = "Belt-positioning booster seat"; why = "Use a booster until the vehicle belt fits properly — typically around 4′9″ (145 cm), often between ages 8 and 12."; }
    show($("#seatOut"), "Recommended stage: <strong>" + stage + "</strong><br>" + why + "<br><span class='notice'>Always follow your seat's manual and local law. Many fire stations and certified technicians offer free fitting checks.</span>");
  });

  /* ===== 11. Baby name finder ===== */
  const nameBox = $("#nameTool");
  if (nameBox) {
    let names = [], favs = store.get("ic-favs", []);
    const q = $("#nameQ"), g = $("#nameG"), o = $("#nameO"), out = $("#nameOut"), favOut = $("#favOut");
    const paintFavs = () => { favOut.textContent = favs.length ? favs.join(" · ") : "Tap ♡ to shortlist names."; };
    const render = () => {
      const s = q.value.trim().toLowerCase();
      const list = names.filter(n => (!s || n.n.toLowerCase().startsWith(s) || n.m.toLowerCase().includes(s)) && (g.value === "all" || n.g === g.value) && (o.value === "all" || n.o === o.value)).slice(0, 120);
      out.innerHTML = list.length ? list.map(n => '<div class="card name-chip"><div><h3 style="margin:0">' + esc(n.n) + '</h3><p class="notice" style="margin:0">' + esc(n.o) + " · " + (n.g === "b" ? "boy" : n.g === "g" ? "girl" : "unisex") + " — " + esc(n.m) + '</p></div><button class="fav" data-n="' + esc(n.n) + '" aria-label="Shortlist ' + esc(n.n) + '">' + (favs.includes(n.n) ? "♥" : "♡") + "</button></div>").join("") : '<p class="notice">No names match. Try fewer filters.</p>';
      $("#nameCount").textContent = list.length + " names shown";
    };
    out.addEventListener("click", e => {
      const b = e.target.closest(".fav"); if (!b) return;
      const n = b.dataset.n; favs = favs.includes(n) ? favs.filter(x => x !== n) : favs.concat(n);
      store.set("ic-favs", favs); paintFavs(); render();
    });
    [q, g, o].forEach(el => el.addEventListener("input", render));
    $("#nameRandom") && $("#nameRandom").addEventListener("click", () => {
      const pool = names.filter(n => (g.value === "all" || n.g === g.value) && (o.value === "all" || n.o === o.value));
      if (!pool.length) return; const n = pool[Math.floor(Math.random() * pool.length)]; q.value = n.n; render();
    });
    fetch((document.body.dataset.root || "") + "data/names.json").then(r => r.json()).then(d => {
      names = d; [...new Set(d.map(n => n.o))].sort().forEach(x => o.insertAdjacentHTML("beforeend", "<option>" + esc(x) + "</option>"));
      paintFavs(); render();
    });
  }
})();
