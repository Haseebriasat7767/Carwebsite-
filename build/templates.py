# -*- coding: utf-8 -*-
"""Page templates: shell + every page type used across the site."""
import html as _h
from data_site import SITE, STATS, PROCESS, TRUST_POINTS, HOME_FAQ, TESTIMONIALS, \
    BRAND_LOGOS_TEXT, WHY_DEALERSHIP, CTA_TEXT
from render import icon, img, header, footer, floating, whatsapp_url, nav_structure

DOMAIN = SITE["domain"]


def esc(s):
    """Escape text, collapsing any entities that were already escaped upstream."""
    s = str(s)
    prev = None
    while s != prev:
        prev = s
        s = _h.unescape(s)
    return _h.escape(s, quote=True)


def mk(s):
    """Pass through when the value already carries intentional markup, else escape."""
    s = str(s)
    return s if "<" in s else esc(s)


# ------------------------------------------------------------------ shared bits
def shell(title, meta, path, body, jsonld="", extra_head="", hero=""):
    canonical = DOMAIN + path
    ld = ['<script type="application/ld+json">%s</script>' % j for j in ([jsonld] if isinstance(jsonld, str) and jsonld else jsonld)]
    return (
        '<!doctype html>\n<html lang="en">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<title>%s</title>\n'
        '<meta name="description" content="%s">\n'
        '<link rel="canonical" href="%s">\n'
        '<meta name="theme-color" content="#0a0e13">\n'
        '<meta property="og:type" content="website">\n'
        '<meta property="og:site_name" content="%s">\n'
        '<meta property="og:title" content="%s">\n'
        '<meta property="og:description" content="%s">\n'
        '<meta property="og:url" content="%s">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        '<link rel="icon" type="image/svg+xml" href="/assets/img/favicon.svg">\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&amp;family=Inter:wght@400;500;600&amp;display=swap" rel="stylesheet">\n'
        '<link rel="stylesheet" href="/assets/css/styles.css">\n'
        '%s%s\n</head>\n<body id="top">\n'
        '<script>window.GC_SITE=%s;</script>\n'
        '%s\n<main id="main">\n%s\n%s\n</main>\n%s\n%s\n'
        '<script src="/assets/js/main.js" defer></script>\n</body>\n</html>\n'
    ) % (esc(title), esc(meta), esc(canonical), esc(SITE["brand"]), esc(title), esc(meta), esc(canonical),
         "\n".join(ld), extra_head,
         '{"brand":"%s","phoneLabel":"%s","tel":"%s","whatsapp":"%s","email":"%s"}' % (
             SITE["brand"].replace('"', "'"), SITE["phone_label"], SITE["tel"], SITE["whatsapp"], SITE["email"]),
         header(_active_for(path)), hero, body, footer(), floating())


def _active_for(path):
    if path in ("/", "/index.html"):
        return "home"
    if path.startswith("/services/"):
        return "services"
    if path.startswith("/roadside"):
        return "roadside"
    if path.startswith("/car-brands/") or path.startswith("/car-sensors/") or path.startswith("/control-modules/"):
        return "brands"
    if path.startswith("/areas-we-serve/"):
        return "areas"
    if path.startswith("/blog/"):
        return "blog"
    if path.startswith("/about/"):
        return "about"
    if path.startswith("/reviews/"):
        return "reviews"
    return ""


def breadcrumbs(crumbs):
    out = ['<nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a>']
    for label, href in crumbs:
        out.append('<span class="sep" aria-hidden="true">/</span>')
        out.append('<a href="%s">%s</a>' % (href, esc(label)) if href else '<span>%s</span>' % esc(label))
    out.append("</nav>")
    return "".join(out)


def page_hero(h1, lede, crumbs, image=None, eyebrow=None):
    media = ('<div class="hero-media">%s</div>' % img(image, h1, loading="eager")) if image else ""
    return (
        '<section class="hero%s">'
        '%s<div class="hero-grid-lines"></div>'
        '<div class="wrap"><div class="hero-inner">'
        '%s%s<h1>%s</h1><p class="hero-lede">%s</p>'
        '<div class="hero-badges">'
        '<span class="chip">%s %s</span><span class="chip">%s %s</span><span class="chip">%s %s</span>'
        '</div>'
        '<div class="btn-row" style="margin-top:26px">'
        '<a class="btn" href="%s" target="_blank" rel="noopener">%s Book on WhatsApp</a>'
        '<a class="btn btn-ghost" href="tel:%s">%s Call %s</a>'
        '</div></div></div></section>'
    ) % (" hero-media-on" if image else "", media,
         breadcrumbs(crumbs),
         ('<span class="eyebrow">%s</span>' % esc(eyebrow)) if eyebrow else "",
         mk(h1), mk(lede),
         icon("clock"), "24/7 roadside &amp; recovery",
         icon("shield"), "Written quote before work",
         icon("wrench"), "All makes &amp; models",
         whatsapp_url(), icon("whatsapp"), SITE["tel"], icon("phone"), SITE["phone_label"])


def simple_hero(h1, lede, crumbs, eyebrow=None, image=None):
    """Lightweight hero for inner pages (no full-bleed image)."""
    if image:
        return page_hero(h1, lede, crumbs, image, eyebrow)
    return (
        '<section class="page-hero"><div class="wrap">'
        '%s%s<h1>%s</h1><p class="lede">%s</p></div></section>'
    ) % (breadcrumbs(crumbs), ('<span class="eyebrow">%s</span>' % esc(eyebrow)) if eyebrow else "", mk(h1), mk(lede))


def section(head_title, head_text, inner, eyebrow=None, alt=False, centered=True, tight=False):
    head = ""
    if head_title:
        head = ('<div class="section-head%s"><div class="rule"></div>%s<h2>%s</h2>%s</div>'
                % (" centered" if centered else "",
                   ('<span class="eyebrow">%s</span>' % esc(eyebrow)) if eyebrow else "",
                   mk(head_title),
                   "<p>%s</p>" % mk(head_text) if head_text else ""))
    return '<section class="section%s%s"><div class="wrap">%s%s</div></section>' % (
        " section-alt" if alt else "", " section-tight" if tight else "", head, inner)


def cards(items, cols=3, link_all=None):
    out = ['<div class="grid g-%d">' % cols]
    for it in items:
        link = it.get("href")
        more = ('<a class="card-link" href="%s">%s %s</a>' % (link, it.get("cta", "Learn more"), icon("arrow"))) if link else ""
        title = ('<a href="%s">%s</a>' % (link, mk(it["title"]))) if link else mk(it["title"])
        out.append(
            '<article class="card reveal"><div class="card-icon">%s</div><h3>%s</h3><p>%s</p>%s</article>'
            % (icon(it.get("icon", "wrench")), title, mk(it["text"]), more))
    out.append("</div>")
    if link_all:
        out.append('<div class="center" style="margin-top:30px"><a class="btn btn-ghost" href="%s">%s %s</a></div>'
                   % (link_all[0], link_all[1], icon("arrow")))
    return "".join(out)


def faq_block(faqs, title="Frequently asked questions", text=None, alt=False, centered=False):
    items = "".join(
        '<details class="acc-item"><summary>%s<span class="acc-icon" aria-hidden="true"></span></summary>'
        '<div class="acc-body"><p>%s</p></div></details>' % (esc(q), esc(a)) for q, a in faqs)
    ld = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
    import json
    inner = '<div class="accordion" style="max-width:900px%s">%s</div>' % (
        ";margin-inline:auto" if centered else "", items)
    return section(title, text, inner, alt=alt, centered=centered) + \
        '<script type="application/ld+json">%s</script>' % json.dumps(ld)


def estimate_form(title="Get a repair estimate", text=None, services=None, compact=False):
    from data_services import CORE_SERVICES, ROADSIDE_SERVICES
    opts = services or [(s["name"]) for s in CORE_SERVICES] + [(s["name"]) for s in ROADSIDE_SERVICES]
    sel = "".join('<option>%s</option>' % esc(o) for o in opts)
    years = "".join('<option>%d</option>' % y for y in range(2026, 1984, -1))
    body = (
        '<div class="split%s">'
        '<div>%s<h2>%s</h2><p class="muted">%s</p>'
        '<ul class="checklist">'
        '<li>Tell us the car and the symptom — we reply with a realistic estimate, not a sales pitch.</li>'
        '<li>Diagnosis first. We identify the cause before recommending any parts.</li>'
        '<li>Fixed written quote approved by you before work starts.</li>'
        '<li>Photos of worn components on request, and old parts shown at hand-back.</li>'
        '<li>Same-day turnaround on most servicing, brakes, batteries and tyres.</li>'
        '</ul></div>'
        '<div class="form-card"><form data-form="estimate" novalidate>'
        '<div class="form-grid">'
        '<div class="field"><label for="e-name">Your name</label><input id="e-name" name="name" type="text" placeholder="Full name" autocomplete="name"></div>'
        '<div class="field"><label for="e-phone">Contact number</label><input id="e-phone" name="phone" type="tel" placeholder="+971 5X XXX XXXX" autocomplete="tel" required></div>'
        '<div class="field"><label for="e-make">Make</label><input id="e-make" name="make" type="text" placeholder="e.g. Toyota" list="makes"></div>'
        '<div class="field"><label for="e-model">Model</label><input id="e-model" name="model" type="text" placeholder="e.g. Camry"></div>'
        '<div class="field"><label for="e-year">Year</label><select id="e-year" name="year"><option value="">Select</option>%s</select></div>'
        '<div class="field"><label for="e-service">Service needed</label><select id="e-service" name="service"><option value="">Select a service</option>%s</select></div>'
        '<div class="field full"><label for="e-details">Describe the problem</label>'
        '<textarea id="e-details" name="details" placeholder="Noise, warning light, when it happens, what has already been tried…"></textarea></div>'
        '</div>'
        '<datalist id="makes">%s</datalist>'
        '<button class="btn btn-block" type="submit" style="margin-top:16px">%s Get my estimate</button>'
        '<div class="form-status" role="status" aria-live="polite"></div>'
        '<div class="btn-row" data-out style="margin-top:14px"></div>'
        '<p class="form-note">No forms go to a server — your request is composed and sent through WhatsApp or email, so you always know where it went.</p>'
        '</form></div></div>'
    ) % (" rev" if compact else "",
         '<span class="eyebrow">Free estimate</span>', mk(title),
         mk(text) if text else "Two minutes of detail now saves a phone call later. The more you can tell us about the symptom, the more accurate the estimate.",
         years, sel,
         "".join('<option value="%s">' % esc(b) for b in BRAND_LOGOS_TEXT),
         icon("note"))
    return section("", "", body, alt=True)


def cta_band(title=None, text=None, phone_label="Speak to a technician now"):
    return (
        '<section class="section-tight"><div class="wrap"><div class="cta-band reveal"><div class="cta-inner">'
        '<div><span class="eyebrow">%s</span><h2>%s</h2><p>%s</p>'
        '<div class="btn-row" style="margin-top:20px">'
        '<a class="btn" href="%s" target="_blank" rel="noopener">%s Message on WhatsApp</a>'
        '<a class="btn btn-ghost" href="/contact/">%s Send an enquiry</a></div></div>'
        '<div><span class="cta-phone">%s %s</span>'
        '<p class="small muted" style="margin-top:8px">%s<br>%s</p></div>'
        '</div></div></div></section>'
    ) % (esc(SITE["roadside_hours"]), esc(title or CTA_TEXT["title"]), esc(text or CTA_TEXT["text"]),
         whatsapp_url(), icon("whatsapp"), icon("mail"),
         icon("phone"), SITE["phone_label"], esc(SITE["hours"]), esc(SITE["address_full"]))


def stats_band():
    items = []
    for s in STATS:
        items.append('<div class="stat"><div class="stat-num" data-count="%s" data-suffix="%s"%s>0</div>'
                     '<div class="stat-label">%s</div></div>'
                     % (s["value"], s.get("suffix", ""),
                        ' data-decimals="%d"' % s["decimals"] if s.get("decimals") else "",
                        esc(s["label"])))
    return section("", "", '<div class="stats reveal">%s</div>' % "".join(items), tight=True)


def related_services(slugs, title="Related services"):
    n = nav_structure()
    lookup = {}
    for s in n["services"]:
        lookup[s["slug"]] = ("/services/%s/" % s["slug"], s)
    for s in n["roadside"]:
        lookup[s["slug"]] = ("/roadside-assistance/%s/" % s["slug"], s)
    cards_html = []
    for slug in slugs:
        if slug not in lookup:
            continue
        href, s = lookup[slug]
        cards_html.append(
            '<a class="tile reveal" href="%s">%s<span>%s</span></a>' % (href, icon(s.get("icon", "wrench")), esc(s["name"])))
    if not cards_html:
        return ""
    return section(title, None, '<div class="related-strip">%s</div>' % "".join(cards_html), tight=True)


def testimonial_slider():
    slides = []
    for t in TESTIMONIALS:
        initials = "".join(w[0] for w in t["name"].split()[:2]).upper()
        stars = "".join(icon("star") for _ in range(5))
        slides.append(
            '<div class="tslide"><div class="quote-card"><span class="quote-mark" aria-hidden="true">&ldquo;</span>'
            '<div class="stars" aria-label="Rated 5 out of 5">%s</div>'
            '<p class="quote-text">%s</p>'
            '<div class="quote-meta"><span class="avatar" aria-hidden="true">%s</span>'
            '<span><span class="quote-name">%s</span><br><span class="quote-sub">%s</span></span></div>'
            '</div></div>' % (stars, esc(t["text"]), initials, esc(t["name"]), esc(t["role"])))
    return section("What drivers say about the workshop",
                   "Reviews collected from customers across Dubai — private cars, family SUVs, performance vehicles and small fleets.",
                   '<div class="tslider reveal"><div class="ttrack">%s</div>'
                   '<div class="tnav"><div class="tdots"></div>'
                   '<button class="tarrow" type="button" data-tslide="-1" aria-label="Previous review">%s</button>'
                   '<button class="tarrow" type="button" data-tslide="1" aria-label="Next review">%s</button>'
                   '</div></div>' % ("".join(slides), icon("chev"), icon("chev")),
                   centered=True, alt=True)


def process_steps():
    steps = "".join('<div class="step reveal"><h3>%s</h3><p>%s</p></div>' % (esc(t), esc(d)) for t, d in PROCESS)
    return section("How a visit works", "Four steps from your first message to driving away — no surprises at any of them.",
                   '<div class="steps">%s</div>' % steps, centered=True)


def trust_cards():
    items = [{"title": t, "text": x, "icon": i} for (t, x), i in
             zip(TRUST_POINTS, ["car", "wrench", "note", "snow"])]
    return cards(items, cols=4)


# ------------------------------------------------------------------- page types
def service_page(d, kind="service"):
    """Generic long-form service/roadside page."""
    base = "/services/" if kind == "service" else "/roadside-assistance/"
    hub = ("Services", "/services/") if kind == "service" else ("Roadside Assistance", "/roadside-assistance/")
    crumbs = [hub, (d["name"], None)]
    body = []

    # intro split
    intro_html = "".join("<p>%s</p>" % esc(p) for p in d["intro"])
    inc = d.get("includes")
    inc_html = ""
    if inc:
        inc_html = ('<div class="info-box reveal"><h3>%s</h3><ul class="ticklist">%s</ul></div>'
                    % (esc(inc["title"]), "".join("<li>%s</li>" % esc(i) for i in inc["items"])))
    body.append(section("", "",
        '<div class="split">'
        '<div><span class="eyebrow">%s</span><h2>%s</h2>%s'
        '<div class="btn-row" style="margin-top:22px">'
        '<a class="btn" href="%s" target="_blank" rel="noopener">%s Ask about this service</a>'
        '<a class="btn btn-ghost" href="tel:%s">%s %s</a></div></div>'
        '<div class="split-media">%s<div class="badge-float">%s<span><strong>Same day</strong><span>on most routine jobs</span></span></div></div>'
        '</div>' % (esc(d["name"]), esc(d.get("h2_intro", "What we do and how we do it")), intro_html,
                   whatsapp_url(), icon("whatsapp"), SITE["tel"], icon("phone"), SITE["phone_label"],
                   img(d["img"], d["h1"]), icon("clock")),
        alt=False))

    if inc_html:
        body.append(section(inc["title"] if not body else "", "", '<div class="grid g-2"><div>%s</div>%s</div>' % (
            inc_html, symptoms_box(d)), alt=True, tight=True) if d.get("symptoms") else
            section("", "", inc_html, alt=True))

    if d.get("why"):
        items = [{"title": t, "text": x, "icon": i} for (t, x), i in zip(
            d["why"], ["clock", "wrench", "gauge", "note"])]
        body.append(section("Why drivers choose us for this", None, cards(items, cols=4), centered=True))

    if d.get("steps"):
        body.append(section("How we approach it", None,
                            '<div class="steps">%s</div>' % "".join(
                                '<div class="step reveal"><h3>%s</h3><p>%s</p></div>' % (esc(t), esc(x)) for t, x in d["steps"]),
                            centered=True, alt=True))

    body.append(stats_band())
    if d.get("faqs"):
        body.append(faq_block(d["faqs"], "Questions about %s" % d["name"].lower(), alt=False))
    body.append(estimate_form(services=[d["name"]]))
    if d.get("related"):
        body.append(related_services(d["related"]))
    body.append(cta_band("Talk to us about your %s" % d["name"].lower(),
                         "Send the symptom, the car and your location. We will tell you what it is likely to be and what it will cost before you commit to anything."))

    ld = [local_business_ld(), breadcrumb_ld(d["h1"], base + d["slug"] + "/")]
    return shell(d["title"], d["meta"], base + d["slug"] + "/",
                 "".join(body), jsonld=ld,
                 hero=page_hero(d["h1"], d["lede"], crumbs, image=d["img"]))


def symptoms_box(d):
    s = d.get("symptoms")
    if not s:
        return ""
    return ('<div class="info-box reveal"><h3>%s</h3><ul class="ticklist">%s</ul></div>'
            % (esc(s["title"]), "".join("<li>%s</li>" % esc(i) for i in s["items"])))


def brand_group_page(b):
    from data_catalog import BRAND_GROUP_INTRO
    path = "/car-brands/%s/" % b["slug"]
    crumbs = [("Car Brands", "/car-brands/"), (b["name"], None)]
    body = []
    intro = BRAND_GROUP_INTRO.format(tradition=b["tradition"])
    body.append(section("", "",
        '<div class="split">'
        '<div><span class="eyebrow">%s specialists</span><h2>Built around how these cars actually fail</h2>'
        '<p class="muted">%s</p>'
        '<div class="btn-row" style="margin-top:22px"><a class="btn" href="%s" target="_blank" rel="noopener">%s Book this brand</a>'
        '<a class="btn btn-ghost" href="/contact/">%s Ask a question</a></div></div>'
        '<div class="split-media">%s</div></div>'
        % (esc(b["tradition"]), esc(intro), whatsapp_url(), icon("whatsapp"), icon("mail"), img(b["img"], b["h1"]))))

    points = [{"title": t, "text": x, "icon": i} for (t, x), i in zip(b["points"], ["wrench", "gear", "shield"])]
    body.append(section("What we know about %s vehicles" % b["tradition"].lower(), None, cards(points, cols=3), alt=True, centered=True))

    body.append(section("Faults we see most often on these cars",
                        "Recognising the pattern is half the diagnosis. These are the recurring complaints our technicians handle on this group.",
                        '<div class="grid g-2">%s</div>' % "".join(
                            '<div class="tile reveal">%s<span>%s</span></div>' % (icon("accident"), esc(c)) for c in b["common"]),
                        centered=True))

    marques = [m for m in nav_structure()["marques"] if m["group"] == b["slug"]]
    if marques:
        body.append(section("Marque-specific pages", None, '<div class="related-strip">%s</div>' % "".join(
            '<a class="tile reveal" href="/car-brands/%s/">%s<span>%s</span></a>' % (m["slug"], icon("car"), esc(m["name"])) for m in marques),
            alt=True, tight=True))
    body.append('<section class="section-tight"><div class="wrap"><div class="info-box reveal">'
                '<h3>Brands covered in this group</h3><p class="muted">%s</p></div></div></section>' % esc(b["marques"]))
    body.append(stats_band())
    body.append(faq_block(b["faqs"], "%s car repair questions" % b["tradition"], alt=False))
    body.append(estimate_form("Book %s car service" % b["tradition"].lower()))
    body.append(cta_band("Bring your %s car in" % b["tradition"].lower(),
                         "Manufacturer-level diagnostics, correct parts specification and honest advice about what genuinely needs doing."))
    return shell(b["title"], b["meta"], path, "".join(body),
                 jsonld=[local_business_ld(), breadcrumb_ld(b["h1"], path)],
                 hero=page_hero(b["h1"], b["lede"], crumbs, image=b["img"]))


def marque_page(m):
    group = next((g for g in nav_structure()["brands"] if g["slug"] == m["group"]), nav_structure()["brands"][0])
    path = "/car-brands/%s/" % m["slug"]
    crumbs = [("Car Brands", "/car-brands/"), (group["name"], "/car-brands/%s/" % group["slug"]), (m["name"], None)]
    h1 = "%s Repair &amp; Service in Dubai" % esc(m["name"])
    lede = ("Servicing, diagnostics and repairs for %s vehicles in Dubai, with particular depth in %s."
            % (m["name"], m["focus"]))
    title = "%s Repair & Service in Dubai | %s" % (m["name"], SITE["brand"])
    meta = ("%s repair and servicing in Dubai: diagnostics, engine, gearbox, AC, brakes, suspension, electrical work "
            "and 24/7 roadside assistance from our Al Quoz workshop." % m["name"])
    body = []
    body.append(section("", "",
        '<div class="split">'
        '<div><span class="eyebrow">%s</span><h2>%s workshop cover, not generic fixes</h2>'
        '<p class="muted">%s</p>'
        '<p class="muted">Every job starts with proper diagnosis on the correct platform for the car, then a written quote. '
        'We use genuine or manufacturer-equivalent parts and follow factory procedures for torque, fluids and calibration.</p>'
        '<div class="btn-row" style="margin-top:22px"><a class="btn" href="%s" target="_blank" rel="noopener">%s Book my %s</a>'
        '<a class="btn btn-ghost" href="tel:%s">%s %s</a></div></div>'
        '<div class="split-media">%s<div class="badge-float">%s<span><strong>%s</strong><span>part of our %s coverage</span></span></div></div></div>'
        % (esc(m["name"]), esc(m["name"]), esc("Our technicians work on %s vehicles regularly, covering %s." % (m["name"], m["focus"])),
           whatsapp_url(), icon("whatsapp"), esc(m["name"]), SITE["tel"], icon("phone"), SITE["phone_label"],
           img(group["img"], m["name"] + " service"), icon("car"), esc(m["name"]), esc(group["tradition"]))))

    body.append(section("Services available for %s owners" % m["name"], None,
        '<div class="grid g-2">%s</div>' % "".join(
            '<a class="tile reveal" href="/services/%s/">%s<span>%s</span></a>' % (s["slug"], icon(s.get("icon", "wrench")), esc(s["name"]))
            for s in nav_structure()["services"][:12]), alt=True))

    body.append(section("Common %s jobs we handle" % m["name"], None,
        '<ul class="checklist">%s</ul>' % "".join(
            "<li>%s</li>" % esc(c) for c in group["common"]), centered=False))
    body.append(stats_band())
    body.append(faq_block(group["faqs"], "%s service questions" % m["name"]))
    body.append(estimate_form("Get a %s repair estimate" % m["name"]))
    body.append(related_services([group["slug"]] + [x["slug"] for x in nav_structure()["marques"] if x["slug"] != m["slug"]][:5],
                                "More brands we service"))
    body.append(cta_band("Book your %s in" % m["name"], None))
    return shell(title, meta, path, "".join(body),
                 jsonld=[local_business_ld(), breadcrumb_ld("%s Repair" % m["name"], path)],
                 hero=simple_hero(h1, lede, crumbs, eyebrow="%s specialist" % m["name"], image=group["img"]))


def location_page(l):
    from data_catalog import LOCATION_INTRO
    path = "/areas-we-serve/%s/" % l["slug"]
    crumbs = [("Areas We Serve", "/areas-we-serve/"), (l["name"], None)]
    body = []
    body.append(section("", "",
        '<div class="split">'
        '<div><span class="eyebrow">%s</span><h2>Coverage across %s</h2>'
        '<p class="muted">%s</p><p class="muted">%s</p>'
        '<div class="btn-row" style="margin-top:22px">'
        '<a class="btn" href="%s" target="_blank" rel="noopener">%s Book in %s</a>'
        '<a class="btn btn-ghost" href="tel:%s">%s 24/7 recovery line</a></div></div>'
        '<div class="split-media">%s</div></div>'
        % (esc(l["name"]), esc(l["name"]), esc(LOCATION_INTRO.format(area=l["name"])), esc(l["note"]),
           whatsapp_url(), icon("whatsapp"), esc(l["name"]), SITE["tel"], icon("phone"), img(l["img"], l["name"]))))

    body.append(section("Neighbourhoods we cover from %s" % l["name"], None,
        '<ul class="pill-list">%s</ul>' % "".join("<li>%s</li>" % esc(a) for a in l["areas"]), alt=True))

    svcs = nav_structure()["services"]
    body.append(section("Services available in %s" % l["name"], None,
        '<div class="grid g-3">%s</div>' % "".join(
            '<a class="card reveal" href="/services/%s/"><div class="card-icon">%s</div><h3>%s</h3>'
            '<span class="card-link">%s %s</span></a>' % (s["slug"], icon(s.get("icon", "wrench")), esc(s["name"]), "Details", icon("arrow"))
            for s in svcs[:6])))

    body.append(section("24/7 roadside help in %s" % l["name"],
                        "Recovery crews dispatch across the whole emirate. These are the calls we get most often from this area.",
                        '<div class="related-strip">%s</div>' % "".join(
                            '<a class="tile reveal" href="/roadside-assistance/%s/">%s<span>%s</span></a>' % (s["slug"], icon(s.get("icon", "tow")), esc(s["name"]))
                            for s in nav_structure()["roadside"][:6]), centered=True, alt=True))
    body.append(stats_band())
    body.append(faq_block([
        ("How quickly can you reach %s?" % l["name"],
         "Mobile technicians and recovery units typically arrive within 30 to 60 minutes depending on traffic and time of day. You are given a realistic window when you call, and updates while the unit is en route."),
        ("Can you service my car at my home or office here?",
         "Yes. Servicing, brakes, batteries, tyres, diagnostics and many repairs can be done where the car is parked. Anything needing a lift is collected and returned."),
        ("Do you cover parking structures and basements?",
         "We do, using low-profile recovery equipment for height-restricted garages. Tell us the building and basement level when you call so we dispatch the right unit."),
    ], "Roadside help in %s" % l["name"]))
    body.append(estimate_form("Book a service in %s" % l["name"]))
    body.append(cta_band("In %s and need a hand?" % l["name"], None))
    return shell(l["title"], l["meta"], path, "".join(body),
                 jsonld=[local_business_ld(), breadcrumb_ld(l["name"], path)],
                 hero=simple_hero(l["h1"], l["lede"], crumbs, eyebrow="Areas we serve", image=l["img"]))


def sensor_page(s):
    path = "/car-sensors/%s/" % s["slug"]
    crumbs = [("Car Sensors", "/car-sensors/"), (s["name"], None)]
    title = "%s Replacement & Repair in Dubai | %s" % (s["name"], SITE["brand"])
    meta = ("%s diagnosis and replacement in Dubai. We test the sensor, its wiring and the live data before recommending "
            "a part, then clear and verify the fault properly." % s["name"])
    h1 = "%s Replacement &amp; Repair" % esc(s["name"])
    lede = "Proper electrical testing before any part is replaced — the sensor, its wiring, its supply and the data it produces."
    body = []
    body.append(section("", "",
        '<div class="split"><div><span class="eyebrow">%s system</span><h2>%s</h2>'
        '<p class="muted">%s</p>'
        '<p class="muted">A stored fault code points at a circuit, not a component. Before fitting anything we check supply voltage, '
        'earth quality, signal output and the wiring between the sensor and the control module. Many faults blamed on sensors turn out '
        'to be corroded connectors, chafed looms or a weak power supply.</p>'
        '<div class="btn-row" style="margin-top:22px"><a class="btn" href="%s" target="_blank" rel="noopener">%s Book a diagnostic</a>'
        '<a class="btn btn-ghost" href="/services/car-scanning-and-diagnostic/">%s How diagnostics work</a></div></div>'
        '<div class="split-media">%s<div class="badge-float">%s<span><strong>Tested</strong><span>before parts are fitted</span></span></div></div></div>'
        % (esc(s["system"]), esc("Symptom: " + s["symptom"]), esc(s["what"]),
           whatsapp_url(), icon("whatsapp"), icon("diag"),
           img("electrical-wiring", s["name"] + " sensor testing"), icon("shield"))))

    body.append(section("How we handle a %s fault" % s["name"].lower(), None,
        '<div class="steps">%s</div>' % "".join('<div class="step reveal"><h3>%s</h3><p>%s</p></div>' % (esc(t), esc(x)) for t, x in [
            ("Read and record the codes", "Full system scan with freeze-frame data so we see the conditions when the fault set."),
            ("Inspect the circuit", "Supply, earth, signal integrity and connector condition checked with meter and oscilloscope."),
            ("Test the component", "The sensor itself is measured against specification rather than assumed faulty."),
            ("Repair, reset and verify", "Correct part fitted, codes cleared, adaptations reset where needed, then a road test to confirm."),
        ]), centered=True, alt=True))

    others = [o for o in nav_structure_sensors() if o["slug"] != s["slug"] and o["system"] != "hub"][:6]
    body.append(section("Related sensor and electrical work", None,
        '<div class="related-strip">%s</div>' % "".join(
            '<a class="tile reveal" href="/car-sensors/%s/">%s<span>%s</span></a>' % (o["slug"], icon("sensor"), esc(o["name"]))
            for o in others), tight=True))
    body.append(faq_block([
        ("Can a %s fault be repaired rather than replaced?" % s["name"].lower(),
         "Sometimes. Wiring, connectors and power supply faults are repairable and often cheaper than a new sensor. Where the component itself has failed, we fit a quality replacement and verify the repair."),
        ("Will the warning light come back after replacement?",
         "It should not, provided the underlying cause is addressed. We clear codes, reset adaptations where required and road-test to confirm the fault does not return."),
        ("Do you use genuine parts?",
         "Genuine or manufacturer-equivalent, your choice. For sensors we recommend quality brands because cheap units frequently produce repeat faults."),
    ], "%s questions" % s["name"]))
    body.append(estimate_form("Get a %s quote" % s["name"].lower()))
    body.append(cta_band("Warning light on the dash?", "Send us the code or a photo of the dashboard and we will tell you what it points to and what a repair is likely to cost."))
    return shell(title, meta, path, "".join(body),
                 jsonld=[local_business_ld(), breadcrumb_ld(s["name"], path)],
                 hero=simple_hero(h1, lede, crumbs, eyebrow="Sensor repair", image="electrical-wiring"))


def nav_structure_sensors():
    from data_catalog import SENSORS
    return SENSORS


def module_page(m):
    path = "/control-modules/%s/" % m["slug"]
    crumbs = [("Control Modules", "/control-modules/"), (m["name"], None)]
    title = "%s Repair & Programming in Dubai | %s" % (m["name"], SITE["brand"])
    meta = ("%s diagnosis, repair, coding and programming in Dubai. Network and module faults traced properly with "
            "manufacturer-level tools rather than trial-and-error replacement." % m["name"])
    h1 = "%s Repair &amp; Programming" % esc(m["name"])
    lede = "Module diagnosis, repair, coding and calibration — with the network checked before the box is blamed."
    body = []
    body.append(section("", "",
        '<div class="split"><div><span class="eyebrow">%s</span><h2>Diagnose the network, then the module</h2>'
        '<p class="muted">%s</p>'
        '<p class="muted">Module faults are frequently misdiagnosed. Before condemning a control unit we verify its power supply, '
        'earth points and data bus communication, because a weak supply or a corroded connector produces exactly the same symptoms '
        'as a failed module — at a tenth of the cost to fix.</p>'
        '<div class="btn-row" style="margin-top:22px"><a class="btn" href="%s" target="_blank" rel="noopener">%s Book module diagnostics</a>'
        '<a class="btn btn-ghost" href="/services/car-electrical-repair/">%s Electrical repair</a></div></div>'
        '<div class="split-media">%s<div class="badge-float">%s<span><strong>Coded</strong><span>and verified after fitting</span></span></div></div></div>'
        % (esc(m["kind"]), esc(m["what"]), whatsapp_url(), icon("whatsapp"), icon("chip"),
           img("electrical-wiring", m["name"]), icon("shield"))))

    body.append(section("What the job involves", None,
        '<div class="grid g-3">%s</div>' % cards([
            {"title": "Diagnosis", "text": "Power, earth and network signals verified with oscilloscope and manufacturer-level scanning before any decision is made.", "icon": "diag"},
            {"title": "Repair or replace", "text": "Where the module is repairable — solder joints, drivers, water damage — we say so. Otherwise a correct replacement unit is sourced.", "icon": "wrench"},
            {"title": "Coding & calibration", "text": "New modules are programmed, coded to the vehicle and adapted, then the system is tested to confirm normal operation.", "icon": "chip"},
        ], cols=3), alt=True, centered=True))

    from data_catalog import MODULES
    body.append(section("Other module and electrical work", None,
        '<div class="related-strip">%s</div>' % "".join(
            '<a class="tile reveal" href="/control-modules/%s/">%s<span>%s</span></a>' % (o["slug"], icon("chip"), esc(o["name"]))
            for o in MODULES if o["slug"] != m["slug"] and o["kind"] != "hub")[:6], tight=True))
    body.append(faq_block([
        ("Can my module be repaired instead of replaced?",
         "Often yes. Water ingress, failed solder joints and damaged internal drivers are common and repairable. We assess before recommending, and a repair is usually far cheaper than a new unit plus coding."),
        ("Does a replacement module need programming?",
         "In most cases yes — coding, immobiliser matching and adaptation are required before the vehicle will operate normally. We handle that as part of the job."),
        ("How long does module work take?",
         "Diagnosis is usually same-day. Sourcing and programming a replacement module can take one to three days depending on the vehicle and availability."),
    ], "%s questions" % m["name"]))
    body.append(estimate_form("Get a %s quote" % m["name"].lower()))
    body.append(cta_band("Multiple warning lights at once?", "That usually points to one root cause — a power supply, earth or network fault. We find it properly instead of replacing modules one at a time."))
    return shell(title, meta, path, "".join(body),
                 jsonld=[local_business_ld(), breadcrumb_ld(m["name"], path)],
                 hero=simple_hero(h1, lede, crumbs, eyebrow="Control module specialists", image="electrical-wiring"))


def post_page(p):
    path = "/blog/%s/" % p["slug"]
    crumbs = [("Guides", "/blog/"), (p["title"], None)]
    body = ['<section class="section"><div class="wrap"><div class="split" style="grid-template-columns:1.35fr .65fr;align-items:start">']
    body.append('<article class="content">')
    for h, txt in p["body"]:
        body.append("<h2>%s</h2><p>%s</p>" % (esc(h), esc(txt)))
    body.append('<div class="callout"><strong>Want this checked on your car?</strong> '
                'Our technicians will diagnose the same issues in the workshop or at your location across Dubai. '
                '<a href="%s">Send us the details</a>.</div>' % "/contact/")
    body.append('</article>')
    body.append('<aside class="info-box reveal" style="position:sticky;top:96px">'
                '<h3>Book this check</h3>'
                '<div class="info-row">%s<span><span class="ir-label">Workshop</span><span class="ir-value">%s</span></span></div>'
                '<div class="info-row">%s<span><span class="ir-label">Phone &amp; WhatsApp</span><span class="ir-value"><a href="tel:%s">%s</a></span></span></div>'
                '<div class="info-row">%s<span><span class="ir-label">Opening hours</span><span class="ir-value">%s</span></span></div>'
                '<div class="info-row">%s<span><span class="ir-label">Recovery</span><span class="ir-value">%s</span></span></div>'
                '<div class="btn-row" style="margin-top:18px"><a class="btn btn-block" href="%s" target="_blank" rel="noopener">%s WhatsApp us</a>'
                '<a class="btn btn-ghost btn-block" href="/services/">%s All services</a></div>'
                '</aside>' % (icon("pin"), esc(SITE["address_street"]), icon("phone"), SITE["tel"], SITE["phone_label"],
                             icon("clock"), esc(SITE["hours"]), icon("recovery"), esc(SITE["roadside_hours"]),
                             whatsapp_url(), icon("whatsapp"), icon("wrench")))
    body.append('</div></div></section>')
    body.append(faq_block(p.get("faqs", []), "Related questions", alt=True) if p.get("faqs") else "")
    body.append(cta_band())
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": p["title"],
           "datePublished": p["date"], "author": {"@type": "Organization", "name": SITE["brand"]},
           "publisher": {"@type": "Organization", "name": SITE["brand"]}}]
    return shell("%s | %s" % (p["title"], SITE["brand"]), p["excerpt"], path, "".join(body),
                 jsonld=ld + [breadcrumb_ld(p["title"], path)],
                 hero=simple_hero(esc(p["title"]), esc(p["excerpt"]), crumbs,
                                  eyebrow="%s · %s min read" % (p["category"], p["read"]), image=p["img"]))


# ------------------------------------------------------------------- schema.org
def local_business_ld():
    import json
    return json.dumps({
        "@context": "https://schema.org", "@type": "AutoRepair",
        "name": SITE["brand"], "description": "Independent car repair workshop in Al Quoz, Dubai offering mechanical repair, diagnostics, air conditioning, brakes, tyres, bodywork and 24/7 roadside assistance.",
        "telephone": SITE["tel"], "email": SITE["email"], "url": DOMAIN,
        "address": {"@type": "PostalAddress", "streetAddress": SITE["address_street"],
                    "addressLocality": "Dubai", "addressCountry": "AE"},
        "geo": {"@type": "GeoCoordinates", "latitude": 25.1305, "longitude": 55.2248},
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification", "dayOfWeek":
            ["Monday", "Tuesday", "Wednesday", "Thursday", "Saturday", "Sunday"],
            "opens": "08:00", "closes": "22:00"}],
        "priceRange": "AED",
        "areaServed": {"@type": "City", "name": "Dubai"},
    })


def breadcrumb_ld(name, path):
    import json
    return json.dumps({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"},
            {"@type": "ListItem", "position": 2, "name": name, "item": DOMAIN + path},
        ]})
