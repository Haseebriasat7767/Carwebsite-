/* Car Garage Auto Service — original front-end behaviour (no frameworks) */
(function () {
  "use strict";

  var SITE = window.GC_SITE || {};
  var doc = document;
  var body = doc.body;

  /* ---------- mobile navigation ---------- */
  var toggle = doc.querySelector(".nav-toggle");
  var closeBtn = doc.querySelector(".mp-close");
  var scrim = doc.querySelector(".scrim");

  function setNav(open) {
    body.classList.toggle("nav-open", open);
    if (toggle) toggle.setAttribute("aria-expanded", open ? "true" : "false");
    doc.documentElement.style.overflow = open ? "hidden" : "";
  }
  if (toggle) toggle.addEventListener("click", function () { setNav(!body.classList.contains("nav-open")); });
  if (closeBtn) closeBtn.addEventListener("click", function () { setNav(false); });
  if (scrim) scrim.addEventListener("click", function () { setNav(false); });
  doc.addEventListener("keydown", function (e) { if (e.key === "Escape") setNav(false); });

  /* ---------- sticky header shadow ---------- */
  var header = doc.querySelector(".site-header");
  var toTop = doc.querySelector(".fa-top");
  function onScroll() {
    var y = window.scrollY || doc.documentElement.scrollTop;
    if (header) header.classList.toggle("is-stuck", y > 12);
    if (toTop) toTop.classList.toggle("is-visible", y > 620);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- scroll reveal ---------- */
  var revealables = doc.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealables.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: .12 });
    revealables.forEach(function (el) { io.observe(el); });
  } else {
    revealables.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- animated counters ---------- */
  var counters = doc.querySelectorAll("[data-count]");
  if ("IntersectionObserver" in window && counters.length) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        cio.unobserve(en.target);
        var el = en.target;
        var target = parseFloat(el.getAttribute("data-count")) || 0;
        var suffix = el.getAttribute("data-suffix") || "";
        var prefix = el.getAttribute("data-prefix") || "";
        var dec = (el.getAttribute("data-decimals") | 0);
        var dur = 1400, t0 = null;
        function frame(ts) {
          if (!t0) t0 = ts;
          var p = Math.min((ts - t0) / dur, 1);
          var eased = 1 - Math.pow(1 - p, 3);
          var val = target * eased;
          el.textContent = prefix + (dec ? val.toFixed(dec) : Math.round(val).toLocaleString("en-US")) + suffix;
          if (p < 1) requestAnimationFrame(frame);
        }
        requestAnimationFrame(frame);
      });
    }, { threshold: .4 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  /* ---------- service tabs ---------- */
  var tabs = doc.querySelectorAll("[data-tab]");
  if (tabs.length) {
    tabs.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var group = btn.getAttribute("data-tab-group") || "default";
        var key = btn.getAttribute("data-tab");
        doc.querySelectorAll('[data-tab-group="' + group + '"]').forEach(function (b) {
          b.setAttribute("aria-selected", b === btn ? "true" : "false");
        });
        doc.querySelectorAll('[data-panel-group="' + group + '"]').forEach(function (p) {
          p.classList.toggle("is-active", p.getAttribute("data-panel") === key);
        });
      });
    });
  }

  /* ---------- testimonial slider ---------- */
  var slider = doc.querySelector(".tslider");
  if (slider) {
    var track = slider.querySelector(".ttrack");
    var slides = slider.querySelectorAll(".tslide");
    var dotsWrap = slider.querySelector(".tdots");
    var prev = slider.querySelector("[data-tslide='-1']");
    var next = slider.querySelector("[data-tslide='1']");
    var idx = 0, timer = null;

    slides.forEach(function (_, i) {
      var d = doc.createElement("button");
      d.className = "tdot" + (i === 0 ? " is-active" : "");
      d.type = "button";
      d.setAttribute("aria-label", "Review " + (i + 1));
      d.addEventListener("click", function () { go(i, true); });
      if (dotsWrap) dotsWrap.appendChild(d);
    });

    function go(n, stop) {
      idx = (n + slides.length) % slides.length;
      track.style.transform = "translateX(" + (-100 * idx) + "%)";
      if (dotsWrap) {
        dotsWrap.querySelectorAll(".tdot").forEach(function (d, i) {
          d.classList.toggle("is-active", i === idx);
        });
      }
      if (stop) restart();
    }
    function restart() {
      if (timer) clearInterval(timer);
      timer = setInterval(function () { go(idx + 1); }, 6500);
    }
    if (prev) prev.addEventListener("click", function () { go(idx - 1, true); });
    if (next) next.addEventListener("click", function () { go(idx + 1, true); });
    slider.addEventListener("mouseenter", function () { if (timer) clearInterval(timer); });
    slider.addEventListener("mouseleave", restart);
    slider.addEventListener("touchstart", function () { if (timer) clearInterval(timer); }, { passive: true });
    restart();
  }

  /* ---------- forms -> WhatsApp / call composer ---------- */
  function waLink(text) {
    var phone = String(SITE.whatsapp || "").replace(/[^0-9]/g, "");
    return "https://wa.me/" + phone + "?text=" + encodeURIComponent(text);
  }

  doc.querySelectorAll("[data-form='estimate']").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var lines = ["Service estimate request — " + (SITE.brand || "Car Garage Auto Service")];
      [["Name", d.get("name")], ["Phone", d.get("phone")], ["Email", d.get("email")],
       ["Make", d.get("make")], ["Model", d.get("model")], ["Year", d.get("year")],
       ["Location", d.get("location")], ["Service", d.get("service")], ["Preferred day", d.get("date")]]
        .forEach(function (pair) { if (pair[1]) lines.push(pair[0] + ": " + pair[1]); });
      if (d.get("details")) lines.push("Notes: " + d.get("details"));

      var status = form.querySelector(".form-status");
      var out = form.querySelector("[data-out]");
      var msg = lines.join("\n");
      if (out) {
        out.innerHTML =
          '<a class="btn" href="' + waLink(msg) + '" target="_blank" rel="noopener">' +
          '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.2-1.8-.9-2-1-.3-.1-.5-.2-.7.1-.2.3-.8 1-1 1.2-.2.2-.4.2-.6.1-.3-.1-1.2-.4-2.2-1.3-.8-.7-1.4-1.6-1.5-1.9-.2-.3 0-.4.1-.6l.5-.6c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5 0-.1-.7-1.6-.9-2.2-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.3-.7.3-1.3.2-1.4-.1-.1-.3-.2-.5-.3zM12 2C6.5 2 2 6.5 2 12c0 1.8.5 3.4 1.3 4.9L2 22l5.3-1.4c1.4.8 3.1 1.3 4.8 1.3 5.5 0 10-4.5 10-10S17.5 2 12 2z"/></svg>' +
          'Send on WhatsApp</a>' +
          '<a class="btn btn-ghost" href="tel:' + (SITE.tel || "") + '">Call ' + (SITE.phoneLabel || "") + '</a>';
      }
      if (status) {
        status.classList.add("is-on");
        status.textContent = "Got it — your request summary is ready below. Choose WhatsApp or a call and our service advisor will confirm pricing before any work starts.";
      }
    });
  });

  doc.querySelectorAll("[data-form='contact']").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var lines = ["Website enquiry — " + (SITE.brand || "Car Garage Auto Service")];
      [["Name", d.get("name")], ["Phone", d.get("phone")], ["Email", d.get("email")],
       ["Topic", d.get("topic")], ["Vehicle", d.get("vehicle")], ["Preferred time", d.get("time")]]
        .forEach(function (pair) { if (pair[1]) lines.push(pair[0] + ": " + pair[1]); });
      if (d.get("message")) lines.push("Message: " + d.get("message"));
      var out = form.querySelector("[data-out]");
      var status = form.querySelector(".form-status");
      if (out) {
        out.innerHTML =
          '<a class="btn" href="' + waLink(lines.join("\n")) + '" target="_blank" rel="noopener">Send on WhatsApp</a>' +
          '<a class="btn btn-ghost" href="mailto:' + (SITE.email || "") + '?subject=' + encodeURIComponent("Website enquiry") +
          '&body=' + encodeURIComponent(lines.join("\n")) + '">Send by email</a>';
      }
      if (status) {
        status.classList.add("is-on");
        status.textContent = "Thanks — pick WhatsApp or email below to send this through. We reply to every enquiry, usually within the hour during workshop hours.";
      }
    });
  });

  /* ---------- generic WhatsApp buttons with page context ---------- */
  doc.querySelectorAll("[data-wa]").forEach(function (el) {
    el.addEventListener("click", function (e) {
      var preset = el.getAttribute("data-wa");
      if (!preset) return;
      e.preventDefault();
      var page = doc.querySelector("h1");
      var ctx = page ? page.textContent.trim() : "a service";
      window.open(waLink("Hello " + (SITE.brand || "") + ", I'd like to book: " + ctx + ". " + preset), "_blank", "noopener");
    });
  });

  /* ---------- live clock for "open now" indicator ---------- */
  var openNow = doc.querySelectorAll("[data-open-now]");
  if (openNow.length) {
    function tick() {
      // Gulf Standard Time = UTC+4. If SITE.open24 is set the workshop never closes.
      if (SITE.open24) {
        openNow.forEach(function (el) {
          el.textContent = "Open 24 hours · staffed now";
          el.classList.remove("is-closed");
        });
        return;
      }
      var now = new Date();
      var gst = new Date(now.getTime() + (now.getTimezoneOffset() + 240) * 60000);
      var h = gst.getHours();
      var open = h >= 8 && h < 22;
      openNow.forEach(function (el) {
        el.textContent = open ? "Open now · closes 10:00 PM" : "Closed · opens 8:00 AM";
        el.classList.toggle("is-closed", !open);
      });
    }
    tick(); setInterval(tick, 60000);
  }

  /* ---------- current year ---------- */
  doc.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ---------- smooth anchor offset for sticky header ---------- */
  doc.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener("click", function (e) {
      var id = a.getAttribute("href");
      if (id.length < 2) return;
      var t = doc.querySelector(id);
      if (!t) return;
      e.preventDefault();
      var y = t.getBoundingClientRect().top + window.scrollY - 96;
      window.scrollTo({ top: y, behavior: "smooth" });
    });
  });
})();
