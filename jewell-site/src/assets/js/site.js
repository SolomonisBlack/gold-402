/* Jewell Services — site behavior */
(function () {
  "use strict";
  var doc = document.documentElement;
  doc.classList.add("js");
  var CFG = window.JEWELL || {};

  // Header shadow on scroll
  var header = document.querySelector(".header");
  function onScroll() {
    if (header) header.classList.toggle("is-scrolled", window.scrollY > 8);
    document.body.classList.toggle("is-scrolled-past-top", window.scrollY > 40);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Mobile nav
  var burger = document.querySelector(".burger");
  function setNav(open) {
    document.body.classList.toggle("nav-open", open);
    burger.setAttribute("aria-expanded", open ? "true" : "false");
    burger.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    document.querySelectorAll("main, footer, .mbar, .topbar").forEach(function (el) {
      if (open) el.setAttribute("inert", ""); else el.removeAttribute("inert");
    });
  }
  if (burger) {
    burger.addEventListener("click", function () { setNav(!document.body.classList.contains("nav-open")); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && document.body.classList.contains("nav-open")) { setNav(false); burger.focus(); }
    });
    window.addEventListener("resize", function () { if (window.innerWidth > 960 && document.body.classList.contains("nav-open")) setNav(false); });
  }

  // Services dropdown (click to toggle; hover handled in CSS on desktop)
  document.querySelectorAll(".has-menu").forEach(function (li) {
    var btn = li.querySelector(".nav__drop");
    btn.addEventListener("click", function () {
      var open = li.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    li.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && li.classList.contains("is-open")) { e.stopPropagation(); li.classList.remove("is-open"); btn.setAttribute("aria-expanded", "false"); btn.focus(); }
    });
    li.addEventListener("mouseleave", function () {
      if (window.innerWidth > 960) { li.classList.remove("is-open"); btn.setAttribute("aria-expanded", "false"); }
    });
    document.addEventListener("click", function (e) {
      if (!li.contains(e.target) && window.innerWidth > 960) { li.classList.remove("is-open"); btn.setAttribute("aria-expanded", "false"); }
    });
  });

  // Reveal on scroll
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-in"); });
  }

  // Highlight today's hours
  var today = new Date().getDay();
  document.querySelectorAll('.hours tr[data-day="' + today + '"]').forEach(function (tr) { tr.classList.add("today"); });

  // Footer year
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // Prefill from the URL: ?service=, ?offer=single-mom, ?error=1
  try {
    var params = new URLSearchParams(location.search);
    var qs = params.get("service");
    if (qs) document.querySelectorAll('select[name="service"]').forEach(function (s) {
      for (var i = 0; i < s.options.length; i++) if (s.options[i].value === qs) s.selectedIndex = i;
    });
    if (params.get("offer") === "single-mom") document.querySelectorAll('input[name="single_mom"]').forEach(function (c) { c.checked = true; });
    if (params.get("error")) document.querySelectorAll("[data-error-banner]").forEach(function (b) { b.hidden = false; });
  } catch (e) {}

  // Spam timing: measure how long the visitor spent on the form (sent as elapsed ms, so device clocks don't matter)
  var started = new WeakMap();
  document.querySelectorAll("form[data-quote]").forEach(function (f) {
    f.noValidate = true; // JS validation takes over; without JS the browser validates natively
    f.addEventListener("focusin", function () { if (!started.has(f)) started.set(f, Date.now()); });
  });

  // File input label
  document.querySelectorAll(".file-input input").forEach(function (inp) {
    inp.addEventListener("change", function () {
      var span = inp.parentNode.querySelector("[data-file-label]");
      if (!span) return;
      var n = inp.files ? inp.files.length : 0;
      if (n > 5) span.textContent = "Please choose up to 5 photos (" + n + " selected)";
      else span.textContent = n ? n + (n === 1 ? " photo selected" : " photos selected") : span.getAttribute("data-default");
    });
  });

  // Forms
  function digits(v) { return (v || "").replace(/\D/g, ""); }
  function validate(form) {
    var ok = true, first = null;
    var files = form.querySelector('input[type="file"]');
    if (files && files.files && files.files.length > 5) { files.focus(); return false; }
    form.querySelectorAll("[required]").forEach(function (el) {
      var bad = !el.value.trim();
      if (!bad && el.type === "email") bad = !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(el.value.trim());
      if (!bad && el.type === "tel") bad = digits(el.value).length < 10;
      if (!bad && el.name === "zip") bad = !/^\d{5}$/.test(el.value.trim());
      el.setAttribute("aria-invalid", bad ? "true" : "false");
      if (bad) { ok = false; if (!first) first = el; }
    });
    form.querySelectorAll('input[type="email"]:not([required])').forEach(function (el) {
      var bad = el.value.trim() && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(el.value.trim());
      el.setAttribute("aria-invalid", bad ? "true" : "false");
      if (bad) { ok = false; if (!first) first = el; }
    });
    if (first) first.focus();
    return ok;
  }
  function summary(form) {
    var fd = new FormData(form), out = [];
    ["name", "phone", "email", "service", "zip", "address", "timeframe", "contact_pref", "message"].forEach(function (k) {
      var v = fd.get(k);
      if (v && String(v).trim()) out.push(k.replace("_", " ") + ": " + String(v).trim());
    });
    return out.join("\n");
  }
  function fallback(form) {
    var st = form.querySelector(".form-status");
    var body = encodeURIComponent("Hi Jewell Services, I'd like a free estimate.\n" + summary(form));
    var tel = CFG.phoneE164 || "+15154519566";
    var html = "We couldn't send your request online just now. Please <a href=\"tel:" + tel + "\">call " + (CFG.phoneDisplay || "515-451-9566") + "</a> or <a href=\"sms:" + tel + "?&body=" + body + "\">text us your request</a> — your details are already filled in.";
    if (CFG.email) html += " You can also <a href=\"mailto:" + CFG.email + "?subject=" + encodeURIComponent("Free estimate request") + "&body=" + body + "\">email us</a>.";
    st.innerHTML = html;
    st.className = "form-status is-error";
    st.setAttribute("role", "alert");
  }
  document.querySelectorAll("form[data-quote]").forEach(function (form) {
    form.querySelectorAll("input,select,textarea").forEach(function (el) {
      el.addEventListener("input", function () { if (el.getAttribute("aria-invalid") === "true") el.setAttribute("aria-invalid", "false"); });
    });
    // Format phone as user types
    form.querySelectorAll('input[type="tel"]').forEach(function (el) {
      el.addEventListener("blur", function () {
        var d = digits(el.value);
        if (d.length === 11 && d[0] === "1") d = d.slice(1);
        if (d.length === 10) el.value = "(" + d.slice(0, 3) + ") " + d.slice(3, 6) + "-" + d.slice(6);
      });
    });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!validate(form)) return;
      var btn = form.querySelector('button[type="submit"]');
      btn.setAttribute("aria-busy", "true");
      var label = btn.innerHTML;
      btn.textContent = "Sending…";
      var endpoint = form.getAttribute("action");
      var done = function () { btn.removeAttribute("aria-busy"); btn.innerHTML = label; };
      if (!endpoint || CFG.formMode === "fallback") { done(); fallback(form); return; }
      var el = form.querySelector('input[name="elapsed"]');
      if (el) el.value = started.has(form) ? Date.now() - started.get(form) : 0;
      var fileInput = form.querySelector('input[type="file"]');
      var hasFiles = fileInput && fileInput.files && fileInput.files.length;
      var ctrl = "AbortController" in window ? new AbortController() : null;
      var t = setTimeout(function () { if (ctrl) ctrl.abort(); }, hasFiles ? 120000 : 30000);
      buildData(form)
        .then(function (fd) { return fetch(endpoint, { method: "POST", body: fd, headers: { Accept: "application/json" }, signal: ctrl ? ctrl.signal : undefined }); })
        .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          clearTimeout(t);
          if (res.ok && res.j && res.j.ok) {
            if (window.gtag) window.gtag("event", "generate_lead", { form: form.id || "quote" });
            location.href = form.getAttribute("data-thanks");
          } else { done(); fallback(form); }
        })
        .catch(function () { clearTimeout(t); done(); fallback(form); });
    });
  });

  // Shrink photos in the browser before upload (phone photos are often 3-8MB each)
  function shrink(file) {
    return new Promise(function (resolve) {
      if (!/^image\/(jpeg|png|webp)$/.test(file.type) || !window.createImageBitmap || !HTMLCanvasElement.prototype.toBlob) return resolve(file);
      createImageBitmap(file).then(function (bmp) {
        var max = 1600, sc = Math.min(1, max / Math.max(bmp.width, bmp.height));
        var c = document.createElement("canvas");
        c.width = Math.round(bmp.width * sc); c.height = Math.round(bmp.height * sc);
        c.getContext("2d").drawImage(bmp, 0, 0, c.width, c.height);
        c.toBlob(function (b) { resolve(b && b.size < file.size ? new File([b], file.name.replace(/\.\w+$/, "") + ".jpg", { type: "image/jpeg" }) : file); }, "image/jpeg", 0.82);
      }).catch(function () { resolve(file); });
    });
  }
  function buildData(form) {
    var fd = new FormData(form);
    var inp = form.querySelector('input[type="file"]');
    if (!inp || !inp.files || !inp.files.length) return Promise.resolve(fd);
    fd.delete(inp.name);
    return Promise.all(Array.prototype.slice.call(inp.files, 0, 5).map(shrink)).then(function (files) {
      files.forEach(function (f) { fd.append(inp.name, f, f.name); });
      return fd;
    });
  }

  // Track call / text taps (for analytics once installed)
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest('a[href^="tel:"],a[href^="sms:"]');
    if (a && window.gtag) window.gtag("event", a.href.indexOf("tel:") === 0 ? "click_to_call" : "click_to_text");
  });

  // Lightbox
  var items = Array.prototype.slice.call(document.querySelectorAll("[data-lightbox]"));
  if (items.length) {
    var lb = document.createElement("div");
    lb.className = "lightbox";
    lb.setAttribute("role", "dialog");
    lb.setAttribute("aria-modal", "true");
    lb.setAttribute("aria-label", "Project photo viewer");
    var x = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg>';
    var l = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m15 18-6-6 6-6"/></svg>';
    var r = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m9 18 6-6-6-6"/></svg>';
    lb.innerHTML = '<button class="lb-close" aria-label="Close">' + x + '</button><button class="lb-prev" aria-label="Previous photo">' + l + '</button><figure><img alt="Project photo"><figcaption aria-live="polite"></figcaption></figure><button class="lb-next" aria-label="Next photo">' + r + "</button>";
    document.body.appendChild(lb);
    var img = lb.querySelector("img"), cap = lb.querySelector("figcaption"), idx = 0, lastFocus = null;
    function show(i) {
      idx = (i + items.length) % items.length;
      var it = items[idx];
      img.src = it.getAttribute("data-full");
      img.alt = it.getAttribute("data-caption") || "";
      cap.textContent = (it.getAttribute("data-caption") || "") + "  (" + (idx + 1) + " of " + items.length + ")";
    }
    function open(i) { lastFocus = document.activeElement; show(i); lb.classList.add("is-open"); document.body.style.overflow = "hidden"; lb.querySelector(".lb-close").focus(); }
    function close() { lb.classList.remove("is-open"); document.body.style.overflow = ""; if (lastFocus) lastFocus.focus(); }
    items.forEach(function (it, i) { it.addEventListener("click", function (e) { e.preventDefault(); open(i); }); });
    lb.querySelector(".lb-close").addEventListener("click", close);
    lb.querySelector(".lb-prev").addEventListener("click", function () { show(idx - 1); });
    lb.querySelector(".lb-next").addEventListener("click", function () { show(idx + 1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) close(); });
    document.addEventListener("keydown", function (e) {
      if (!lb.classList.contains("is-open")) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") show(idx - 1);
      if (e.key === "ArrowRight") show(idx + 1);
      if (e.key === "Tab") {
        var f = lb.querySelectorAll("button"), a = f[0], z = f[f.length - 1];
        if (e.shiftKey && document.activeElement === a) { e.preventDefault(); z.focus(); }
        else if (!e.shiftKey && document.activeElement === z) { e.preventDefault(); a.focus(); }
      }
    });
  }
})();
