# -*- coding: utf-8 -*-
"""Home page, hub pages and static pages."""
from data_site import SITE, STATS, PROCESS, TRUST_POINTS, HOME_FAQ, TESTIMONIALS, \
    BRAND_LOGOS_TEXT, WHY_DEALERSHIP, CTA_TEXT
from data_services import CORE_SERVICES, ROADSIDE_SERVICES, ROADSIDE_HUB
from data_catalog import BRAND_GROUPS, MARQUES, LOCATIONS, SENSORS, MODULES, POSTS
from render import icon, img, whatsapp_url, nav_structure
from templates import (shell, section, cards, faq_block, estimate_form, cta_band, stats_band,
                       related_services, testimonial_slider, process_steps, breadcrumbs,
                       page_hero, simple_hero, local_business_ld, breadcrumb_ld, esc)


# --------------------------------------------------------------------- home page
def home_page():
    featured = ["car-scanning-and-diagnostic", "car-engine-repair", "car-oil-change",
                "car-tyres-and-flat-tyre", "car-transmission-repair", "car-battery-replacement"]
    by_slug = {s["slug"]: s for s in CORE_SERVICES}
    body = []

    # --- three pillars -------------------------------------------------------
    pillars = [
        {"img": "roadside-night", "eyebrow": "24 hours, every day",
         "title": "Roadside help anywhere in Dubai",
         "text": "Flat battery on a Tuesday morning, a puncture on Sheikh Zayed Road at midnight, keys locked in the car outside a mall — our crews are dispatched with the right equipment for the job, not a van that has to go back for tools. Typical arrival inside the city is 30 to 45 minutes, and we tell you the honest window when you call.",
         "cta": ("Get roadside help", "/roadside-assistance/")},
        {"img": "hero-workshop", "eyebrow": "Al Quoz, one roof",
         "title": "Every repair without a second trip",
         "text": "Mechanical work, diagnostics, air conditioning, brakes, tyres, batteries, electrics, bodywork and paint are all done in the same facility. That means one job card, one accountable team and one price — instead of being sent to three specialists who each blame a different system.",
         "cta": ("See all services", "/services/")},
        {"img": "diagnostics", "eyebrow": "All makes and models",
         "title": "Technicians matched to your car",
         "text": "We assign work according to the vehicle in front of us. Japanese, Korean, German, British, American, French, Italian, Chinese, luxury, hybrid and electric — each with the diagnostic platform, technical data and parts route that marque actually needs.",
         "cta": ("Explore brands", "/car-brands/")},
    ]
    pillar_html = []
    badges = [("24/7", "recovery &amp; mobile crews"),
              ("Same day", "on most routine jobs"),
              ("25+", "marques covered in-house")]
    for i, p in enumerate(pillars):
        big, small = badges[i]
        pillar_html.append(
            '<div class="split%s reveal">'
            '<div class="split-media">%s<div class="badge-float">%s<span><strong>%s</strong><span>%s</span></span></div></div>'
            '<div><span class="eyebrow">%s</span><h2>%s</h2><p class="muted">%s</p>'
            '<a class="card-link" href="%s">%s %s</a></div></div>'
            % (" rev" if i % 2 else "", img(p["img"], p["title"]), icon("clock"),
               big, small, esc(p["eyebrow"]), esc(p["title"]), esc(p["text"]),
               p["cta"][1], esc(p["cta"][0]), icon("arrow")))
    body.append('<section class="section"><div class="wrap" style="display:grid;gap:clamp(34px,5vw,66px)">%s</div></section>'
                % "".join(pillar_html))

    # --- featured services tabs ---------------------------------------------
    tabs, panels = [], []
    for i, slug in enumerate(featured):
        s = by_slug[slug]
        tabs.append('<button class="tab-btn" type="button" data-tab-group="svc" data-tab="%s" role="tab" aria-selected="%s">%s</button>'
                    % (slug, "true" if i == 0 else "false", esc(s["name"])))
        inc = s.get("includes", {}).get("items", [])[:6]
        panels.append(
            '<div class="tab-panel%s" data-panel-group="svc" data-panel="%s" role="tabpanel">'
            '<div class="split">'
            '<div class="split-media">%s</div>'
            '<div><span class="eyebrow">%s</span><h2>%s</h2><p class="muted">%s</p>'
            '<ul class="ticklist">%s</ul>'
            '<div class="btn-row" style="margin-top:24px">'
            '<a class="btn" href="/services/%s/">%s Full service details</a>'
            '<a class="btn btn-ghost" href="%s" target="_blank" rel="noopener">%s Book on WhatsApp</a>'
            '</div></div></div></div>'
            % (" is-active" if i == 0 else "", slug, img(s["img"], s["name"]), esc(s["tag"].title()),
               esc(s["h1"]), esc(" ".join(s["intro"][:1])),
               "".join("<li>%s</li>" % esc(x) for x in inc),
               slug, icon("arrow"), whatsapp_url(), icon("whatsapp")))
    body.append(section("Services we are known for",
                        "Six of the jobs that fill our diary every week. Tap a category to see what the work actually involves.",
                        '<div class="tabs" role="tablist" aria-label="Featured services">%s</div>%s' % ("".join(tabs), "".join(panels)),
                        centered=True))

    # --- three big destination cards ----------------------------------------
    dest = [
        {"slug": "roadside", "href": "/roadside-assistance/", "name": "Roadside Assistance", "icon": "tow", "img": "roadside-night",
         "text": "Towing, jump-starts, flat tyres, fuel delivery, lockouts, winch recovery and accident recovery — dispatched 24 hours a day across the whole emirate."},
        {"slug": "repair", "href": "/services/car-repair-dubai/", "name": "Car Repair", "icon": "wrench", "img": "engine-repair",
         "text": "From a warning light that needs proper diagnosis to a full engine or gearbox job, carried out to manufacturer specification with a fixed written quote."},
        {"slug": "garage", "href": "/services/car-garage-dubai/", "name": "Car Garage", "icon": "service", "img": "team-workshop",
         "text": "A complete workshop facility: lifts, alignment, air conditioning machinery, bodyshop and a parts desk, a few minutes off Sheikh Zayed Road."},
    ]
    body.append(section("Three ways we help", None,
        '<div class="grid g-3">%s</div>' % "".join(
            '<article class="media-card reveal"><figure>%s</figure><div class="mc-body">'
            '<div class="card-icon">%s</div><h3><a href="%s">%s</a></h3><p>%s</p>'
            '<a class="card-link" href="%s">%s %s</a></div></article>'
            % (img(d["img"], d["name"]), icon(d["icon"]), d["href"], esc(d["name"]), esc(d["text"]), d["href"], "Explore", icon("arrow"))
            for d in dest), alt=True, centered=True))

    # --- editorial blocks ----------------------------------------------------
    body.append(section("What separates a good independent workshop",
                        None,
        '<div class="split reveal"><div class="content">'
        '<p>When something goes wrong with your car, the choice is usually between a franchised dealership and an independent workshop. '
        'For anything outside warranty, the independent route is normally faster and considerably cheaper — provided the workshop has the '
        'right equipment, the right technical information and technicians who work on your type of car regularly. That last point is where '
        'most cheap garages fall down.</p>'
        '<p>We match the technician to the vehicle rather than treating every car as interchangeable. Oil services, brake work, engine '
        'diagnostics, gearbox repairs, air conditioning faults and collision bodywork are all handled here, with pricing agreed in writing '
        'before a single bolt is undone.</p>'
        '<h3>Maintenance built for Gulf conditions</h3>'
        '<p>Heat, dust and stop-start traffic age components faster than the service intervals written for temperate climates. Coolant '
        'degrades, rubber perishes, batteries lose capacity and air conditioning systems work far harder than their designers expected. '
        'We specify fluids and parts for the conditions your car actually operates in, and we adjust intervals accordingly.</p>'
        '<h3>Luxury, performance and electrified vehicles</h3>'
        '<p>European luxury cars, performance models, hybrids and electric vehicles all need manufacturer-level diagnostic access, correct '
        'torque data and, in the case of high-voltage systems, safe isolation procedures. We invest in that tooling and training rather than '
        'sending these cars away.</p>'
        '<h3>Air conditioning, brakes and electrics: the three most requested jobs</h3>'
        '<p>Refrigerant leaks, compressors and condensers; pads, discs, fluid and ABS faults; batteries, alternators, wiring and modules. '
        'These are the systems the climate punishes hardest, so we stock the common parts and keep the equipment calibrated to find faults '
        'quickly instead of guessing.</p>'
        '</div><div class="split-media">%s<div class="badge-float">%s<span><strong>%s</strong><span>independent workshop</span></span></div></div></div>'
        % (img("engine-repair", "Technicians at work"), icon("shield"), "Since %d" % SITE["founded_year"])))

    # --- why drivers trust us ------------------------------------------------
    body.append(section("Why drivers across Dubai keep coming back",
                        "Trust is built by being consistent: the same pricing on the tenth visit as the first, the same standard of work "
                        "whatever the badge on the bonnet, and a location that makes 'near me' genuinely mean something.",
                        cards([
                            {"title": "Every make, one workshop", "icon": "car",
                             "text": "Japanese, Korean, German, British, American, French, Italian, Chinese, luxury, hybrid and electric — no need to hunt down a different specialist for each car in the household."},
                            {"title": "Depth of service", "icon": "wrench",
                             "text": "Mechanical repair, diagnostics, air conditioning, tyres, batteries, electrics, bodywork, paint, inspections and detailing. Most needs are handled without a referral elsewhere."},
                            {"title": "Explanations in plain language", "icon": "note",
                             "text": "You get told what is wrong, why it is wrong, what it costs and what can wait. Photos of worn parts on request, old components shown at hand-back."},
                            {"title": "Records you can use", "icon": "shield",
                             "text": "Every visit is documented with parts, specifications and recommendations — useful for warranty questions, resale value and simply knowing your car's history."},
                        ], cols=4), alt=True, centered=True))

    body.append(estimate_form())
    body.append(process_steps())
    body.append(stats_band())
    body.append(testimonial_slider())

    # --- areas + brands strips ----------------------------------------------
    body.append(section("Areas we cover",
                        "The workshop is in Al Quoz with easy access from Sheikh Zayed Road, and mobile crews and recovery units operate across the entire emirate.",
                        '<ul class="pill-list">%s</ul>' % "".join(
                            '<li><a href="/areas-we-serve/%s/">%s</a></li>' % (l["slug"], esc(l["name"])) for l in LOCATIONS),
                        centered=True))

    body.append(section("Brands we work on every week", None,
                        '<ul class="pill-list">%s</ul>' % "".join(
                            "<li>%s</li>" % esc(b) for b in BRAND_LOGOS_TEXT) +
                        '<div class="center" style="margin-top:26px"><a class="btn btn-ghost" href="/car-brands/">%s See brand pages %s</a></div>'
                        % ("Browse by marque", icon("arrow")), alt=True, centered=True))

    body.append(faq_block(HOME_FAQ, "Frequently asked questions",
                          "The questions we get asked most often, answered plainly.", centered=True))
    body.append(cta_band())

    hero = (
        '<section class="hero"><div class="hero-media">%s</div><div class="hero-grid-lines"></div>'
        '<div class="wrap"><div class="hero-inner">'
        '<span class="eyebrow">%s · Al Quoz, Dubai</span>'
        '<h1>Car Repair in Dubai with <span class="hl">24/7 Roadside Assistance</span></h1>'
        '<p class="hero-lede">An independent workshop that diagnoses properly, quotes in writing and fixes it once. '
        'Mechanical repair, air conditioning, brakes, tyres, diagnostics, bodywork and round-the-clock recovery — '
        'for every make of car in Dubai.</p>'
        '<div class="btn-row" style="margin-top:28px">'
        '<a class="btn" href="%s" target="_blank" rel="noopener">%s Book a service on WhatsApp</a>'
        '<a class="btn btn-light" href="tel:%s">%s %s</a>'
        '<a class="btn btn-ghost" href="/services/">%s Explore services</a>'
        '</div>'
        '<div class="hero-badges">'
        '<span class="chip">%s %s</span>'
        '<span class="chip">%s %s</span>'
        '<span class="chip">%s %s</span>'
        '<span class="chip">%s %s</span>'
        '</div></div></div></section>'
    ) % (img("hero-workshop", "Modern car repair workshop in Al Quoz, Dubai", loading="eager"),
         esc(SITE["brand"]), whatsapp_url(), icon("whatsapp"), SITE["tel"], icon("phone"), SITE["phone_label"],
         icon("wrench"), icon("clock"), "Same-day servicing",
         icon("shield"), "Fixed written quotes",
         icon("car"), "All makes &amp; models",
         icon("recovery"), "24/7 recovery across Dubai")

    title = "%s | Car Repair &amp; 24/7 Roadside Assistance in Dubai" % SITE["brand"]
    meta = ("Independent car repair workshop in Al Quoz, Dubai: engine and gearbox repair, diagnostics, air conditioning, "
            "brakes, tyres, batteries, bodywork and 24-hour roadside assistance for every make of car.")
    return shell(title, meta, "/", "".join(body),
                 jsonld=[local_business_ld()], hero=hero)


# ------------------------------------------------------------------ hub: services
def services_hub():
    groups = [
        ("core", "Repairs & diagnostics"), ("mechanical", "Engine & drivetrain"),
        ("safety", "Brakes, tyres & suspension"), ("comfort", "Cooling & climate"),
        ("electrical", "Electrical & electronics"), ("maintenance", "Servicing & maintenance"),
        ("body", "Bodywork & appearance"), ("specialist", "Specialist work"),
        ("convenience", "We come to you"), ("inspection", "Inspections"), ("diagnostics", "Diagnostics"),
    ]
    seen, blocks = set(), []
    for key, label in groups:
        items = [s for s in CORE_SERVICES if s.get("tag") == key and s["slug"] not in seen]
        if not items:
            continue
        seen.update(s["slug"] for s in items)
        blocks.append(
            '<div class="reveal"><h3 style="margin-bottom:16px">%s</h3><div class="grid g-3">%s</div></div>'
            % (esc(label), "".join(
                '<article class="card"><div class="card-icon">%s</div><h3><a href="/services/%s/">%s</a></h3>'
                '<p>%s</p><a class="card-link" href="/services/%s/">%s %s</a></article>'
                % (icon(s.get("icon", "wrench")), s["slug"], esc(s["name"]), esc(s["lede"]), s["slug"], "Details", icon("arrow"))
                for s in items)))
    body = [section("Everything the workshop does",
                    "One facility, one accountable team. Choose a service to see exactly what the work involves, what it covers and what it usually costs in time.",
                    '<div style="display:grid;gap:38px">%s</div>' % "".join(blocks), centered=False, alt=False)]
    body.append(section("Not sure which service you need?",
                        "Describe the symptom instead — a noise, a smell, a warning light, a change in how the car drives. We will point you at the right job.",
                        '<div class="grid g-3">%s</div>' % cards([
                            {"title": "Warning light on the dash", "icon": "diag", "text": "Full system scan, live data and circuit testing to establish the cause rather than the code.", "href": "/services/car-scanning-and-diagnostic/"},
                            {"title": "Noises, vibration, handling", "icon": "susp", "text": "Brakes, tyres, suspension and driveline inspection on the lift, followed by a road test.", "href": "/services/car-suspension-repair/"},
                            {"title": "Hot cabin, weak airflow", "icon": "ac", "text": "Leak detection, pressure testing, component diagnosis and recharge to specification.", "href": "/services/car-ac-repair-dubai/"},
                            {"title": "Due for a service", "icon": "service", "text": "Minor, major or interval servicing to the manufacturer schedule, adjusted for Gulf use.", "href": "/services/car-minor-service/"},
                            {"title": "Buying a used car", "icon": "inspect", "text": "Independent inspection with photographs, module scans and a costed report.", "href": "/services/car-pre-purchase-inspection/"},
                            {"title": "Car won't start", "icon": "battery", "text": "Battery, charging and starting system diagnosis — at our workshop or at your location.", "href": "/services/car-battery-replacement/"},
                        ], cols=3), alt=True, centered=True))
    body.append(stats_band())
    body.append(estimate_form("Tell us what your car is doing"))
    body.append(cta_band())
    path = "/services/"
    return shell("Car Repair Services in Dubai | %s" % SITE["brand"],
                 "Full list of car repair and maintenance services in Dubai: engine, gearbox, diagnostics, AC, brakes, tyres, batteries, suspension, electrical, bodywork, inspections and mobile mechanics.",
                 path, "".join(body), jsonld=[local_business_ld(), breadcrumb_ld("Services", path)],
                 hero=simple_hero("Car Repair &amp; Maintenance Services",
                                  "Every service we offer, listed with what it involves. Nothing hidden, nothing inflated.",
                                  [("Services", None)], eyebrow="Services", image="hero-workshop"))


# ------------------------------------------------------------------ hub: roadside
def roadside_hub():
    hub = ROADSIDE_HUB
    body = []
    body.append(section("", "",
        '<div class="split reveal"><div><span class="eyebrow">Dispatched 24/7</span>'
        '<h2>Help that arrives with the right equipment</h2>'
        '<p class="muted">%s</p><p class="muted">%s</p>'
        '<div class="btn-row" style="margin-top:22px">'
        '<a class="btn" href="%s" target="_blank" rel="noopener">%s Request help now</a>'
        '<a class="btn btn-ghost" href="tel:%s">%s %s</a></div></div>'
        '<div class="split-media">%s<div class="badge-float">%s<span><strong>30–45 min</strong><span>typical arrival in Dubai</span></span></div></div></div>'
        % (esc(hub["intro"][0]), esc(hub["intro"][1]), whatsapp_url(), icon("whatsapp"),
           SITE["tel"], icon("phone"), SITE["phone_label"],
           img(hub["img"], hub["h1"]), icon("clock"))))

    body.append(section("Roadside & recovery services",
                        "Every service below is available around the clock, including public holidays.",
                        '<div class="grid g-3">%s</div>' % "".join(
                            '<article class="card reveal"><div class="card-icon">%s</div>'
                            '<h3><a href="/roadside-assistance/%s/">%s</a></h3><p>%s</p>'
                            '<a class="card-link" href="/roadside-assistance/%s/">%s %s</a></article>'
                            % (icon(s.get("icon", "tow")), s["slug"], esc(s["name"]), esc(s["lede"]), s["slug"], "Details", icon("arrow"))
                            for s in ROADSIDE_SERVICES), centered=True, alt=True))

    body.append(section("Why use our recovery crews", None, cards([
        {"title": t, "text": x, "icon": i} for (t, x), i in zip(hub["why"], ["clock", "wrench", "gauge", "note"])
    ], cols=4)))

    body.append(section("What to do while you wait", None,
        '<div class="steps">%s</div>' % "".join('<div class="step reveal"><h3>%s</h3><p>%s</p></div>' % (esc(t), esc(x)) for t, x in [
            ("Move to safety", "Get the car off the carriageway if you can, hazards on, and stand away from traffic — behind a barrier if there is one."),
            ("Make it visible", "Warning triangle well behind the vehicle, sidelights on at night. Give approaching drivers time to react."),
            ("Send your location", "A location pin beats a description. Include direction of travel, and basement level plus height limit if you are parked underground."),
            ("Describe the fault", "What happened, what the car is doing now, any warning lights, and the vehicle type. It decides which unit gets dispatched."),
        ]), centered=True, alt=True))

    body.append(stats_band())
    body.append(faq_block(hub["faqs"], "Roadside assistance questions", alt=False))
    body.append(estimate_form("Need help at your location?",
                              "Tell us where you are and what the car is doing. For urgent breakdowns, call the 24-hour line directly — it is faster than a form.",
                              services=[s["name"] for s in ROADSIDE_SERVICES]))
    body.append(cta_band("Stranded somewhere in Dubai?",
                         "Call the 24-hour line and a crew is dispatched. You will be told the arrival window and the cost before anything happens."))
    path = "/roadside-assistance/"
    return shell(hub["title"], hub["meta"], path, "".join(body),
                 jsonld=[local_business_ld(), breadcrumb_ld("Roadside Assistance", path)],
                 hero=page_hero(hub["h1"], hub["lede"], [("Roadside Assistance", None)], image=hub["img"], eyebrow="24/7 dispatch"))


# -------------------------------------------------------------------- hub: brands
def brands_hub():
    body = []
    body.append(section("Choose your car's origin",
                        "Fault patterns, diagnostic systems and parts sourcing differ between engineering traditions. These pages explain what we see most often on each group.",
                        '<div class="grid g-3">%s</div>' % "".join(
                            '<article class="card reveal"><div class="card-icon">%s</div>'
                            '<h3><a href="/car-brands/%s/">%s</a></h3><p>%s</p>'
                            '<p class="small muted">%s</p>'
                            '<a class="card-link" href="/car-brands/%s/">%s %s</a></article>'
                            % (icon(b.get("icon", "wrench")), b["slug"], esc(b["name"]), esc(b["lede"]), esc(b["marques"]),
                               b["slug"], "Details", icon("arrow")) for b in BRAND_GROUPS), centered=True))

    body.append(section("Or go straight to your marque", None,
                        '<div class="grid g-4">%s</div>' % "".join(
                            '<a class="tile reveal" href="/car-brands/%s/">%s<span>%s</span></a>' % (m["slug"], icon("car"), esc(m["name"]))
                            for m in MARQUES), alt=True))

    body.append(section("Electronics, sensors and control modules",
                        "Modern cars are networks of modules and sensors. When a warning light appears, the fault is as often in the wiring or coding as in the part itself.",
                        '<div class="grid g-2">'
                        '<div class="info-box reveal"><h3>Sensor replacement &amp; testing</h3>'
                        '<p class="muted">ABS, TPMS, oxygen, crankshaft and camshaft position, oil pressure and level, fuel pressure, '
                        'temperature, rain, parking, manifold and driver-assistance sensors — tested before they are replaced.</p>'
                        '<a class="card-link" href="/car-sensors/">%s All sensors %s</a></div>'
                        '<div class="info-box reveal"><h3>Control module repair &amp; programming</h3>'
                        '<p class="muted">Engine and powertrain modules, safety and airbag modules, chassis, transfer case, lighting, '
                        'tailgate, immobiliser, infotainment, fuse boxes and wiring harness repair.</p>'
                        '<a class="card-link" href="/control-modules/">%s All modules %s</a></div>'
                        '</div>' % (icon("arrow"), icon("arrow"), icon("arrow"), icon("arrow")), alt=True, centered=True))
    body.append(stats_band())
    body.append(estimate_form("Book service for your make"))
    body.append(cta_band())
    path = "/car-brands/"
    return shell("Car Brands We Service in Dubai | %s" % SITE["brand"],
                 "Car repair by brand in Dubai: Japanese, German, European, British, American, French, Italian, Chinese, exotic and classic vehicles, plus marque-specific pages and electronics work.",
                 path, "".join(body), jsonld=[local_business_ld(), breadcrumb_ld("Car Brands", path)],
                 hero=simple_hero("Every Make, Serviced Properly",
                                  "Technicians matched to the vehicle in front of them, with the diagnostic platforms and parts routes each brand needs.",
                                  [("Car Brands", None)], eyebrow="Brands", image="diagnostics"))


def sensors_hub():
    body = [section("Sensor testing & replacement",
                    "A fault code identifies a circuit, not a culprit. We measure supply, earth, signal and wiring before recommending a part — and we will tell you when the sensor is fine.",
                    '<div class="grid g-3">%s</div>' % "".join(
                        '<article class="card reveal"><div class="card-icon">%s</div>'
                        '<h3><a href="/car-sensors/%s/">%s</a></h3><p>%s</p>'
                        '<p class="small muted"><strong>Symptom:</strong> %s</p>'
                        '<a class="card-link" href="/car-sensors/%s/">%s %s</a></article>'
                        % (icon("sensor"), s["slug"], esc(s["name"]), esc(s["what"]), esc(s["symptom"]), s["slug"], "Details", icon("arrow"))
                        for s in SENSORS if s["system"] != "hub"))]
    body.append(faq_block([
        ("Why test before replacing a sensor?", "Because the code points at a circuit. Corroded connectors, damaged wiring, weak supply voltages and module faults all produce identical symptoms at very different repair costs."),
        ("Do cheap sensors cause problems?", "Frequently. Low-quality units drift, fail early or produce signal characteristics the module does not recognise, which leads to repeat visits. We specify quality brands."),
        ("Can sensors be replaced at my location?", "Many can, through our mobile mechanic service. Sensors requiring calibration, lifting or specialist access are done in the workshop."),
    ], "Sensor questions", alt=True))
    body.append(estimate_form("Get a sensor diagnosis quote"))
    path = "/car-sensors/"
    return shell("Car Sensor Replacement & Testing in Dubai | %s" % SITE["brand"],
                 "Car sensor diagnosis and replacement in Dubai: ABS, TPMS, oxygen, crankshaft, camshaft, oil pressure, fuel, temperature, parking and driver-assistance sensors.",
                 path, "".join(body), jsonld=[local_business_ld(), breadcrumb_ld("Car Sensors", path)],
                 hero=simple_hero("Car Sensor Diagnosis &amp; Replacement",
                                  "Tested properly before anything is fitted — because the code is a clue, not a conclusion.",
                                  [("Car Brands", "/car-brands/"), ("Sensors", None)], eyebrow="Electronics", image="electrical-wiring"))


def modules_hub():
    body = [section("Control module repair, coding & programming",
                    "Modules fail from heat, water, vibration and electrical stress. We verify the network and power supply first, repair where possible, and code replacements correctly.",
                    '<div class="grid g-3">%s</div>' % "".join(
                        '<article class="card reveal"><div class="card-icon">%s</div>'
                        '<h3><a href="/control-modules/%s/">%s</a></h3><p>%s</p>'
                        '<span class="small muted">%s</span>'
                        '<a class="card-link" href="/control-modules/%s/">%s %s</a></article>'
                        % (icon("chip"), m["slug"], esc(m["name"]), esc(m["what"]), esc(m["kind"]), m["slug"], "Details", icon("arrow"))
                        for m in MODULES if m["kind"] != "hub"))]
    body.append(section("Related electrical work", None,
                        '<div class="related-strip">%s</div>' % "".join(
                            '<a class="tile reveal" href="/services/%s/">%s<span>%s</span></a>' % (s["slug"], icon(s.get("icon", "elec")), esc(s["name"]))
                            for s in CORE_SERVICES if s.get("tag") in ("electrical", "diagnostics")), alt=True, tight=True))
    body.append(estimate_form("Describe the fault"))
    path = "/control-modules/"
    return shell("Control Module Repair & Programming in Dubai | %s" % SITE["brand"],
                 "Car control module repair and programming in Dubai: ECM, PCM, airbag, safety, chassis, transfer case, lighting, immobiliser, infotainment, fuse box and wiring harness work.",
                 path, "".join(body), jsonld=[local_business_ld(), breadcrumb_ld("Control Modules", path)],
                 hero=simple_hero("Control Module Repair &amp; Programming",
                                  "Network diagnosis before module replacement — the difference between a repair and a parts lottery.",
                                  [("Car Brands", "/car-brands/"), ("Control Modules", None)], eyebrow="Electronics", image="electrical-wiring"))


def areas_hub():
    body = [section("Where we work",
                    "Our workshop is in Al Quoz Industrial Area 1 on First Al Khail Street, minutes from Sheikh Zayed Road and open 24 hours. Mobile technicians and recovery units cover the whole emirate around the clock.",
                    '<div class="grid g-3">%s</div>' % "".join(
                        '<article class="card reveal"><div class="card-icon">%s</div>'
                        '<h3><a href="/areas-we-serve/%s/">%s</a></h3><p>%s</p>'
                        '<a class="card-link" href="/areas-we-serve/%s/">%s %s</a></article>'
                        % (icon("pin"), l["slug"], esc(l["name"]), esc(l["lede"]), l["slug"], "Coverage details", icon("arrow"))
                        for l in LOCATIONS), centered=True)]
    body.append(section("Not on the list?",
                        "We cover all of Dubai — Deira, Bur Dubai, Mirdif, International City, Silicon Oasis, Dubai South, Al Barsha, Umm Suqeim, Jumeirah, Rashidiya, Warsan and everywhere between.",
                        '<div class="map-frame"><div class="map-static"><div>%s<strong>%s</strong>%s<br>'
                        '<a class="btn btn-sm" style="margin-top:14px" href="%s" target="_blank" rel="noopener">%s Get directions</a></div></div></div>'
                        % (icon("pin"), esc(SITE["address_street"]), esc(SITE["address_city"]),
                           SITE["map_url"],
                           "Open in Maps", ), alt=True, centered=True))
    body.append(stats_band())
    body.append(estimate_form("Book in your area"))
    body.append(cta_band())
    path = "/areas-we-serve/"
    return shell("Areas We Serve in Dubai | %s" % SITE["brand"],
                 "Car repair and 24/7 roadside assistance across Dubai: Al Quoz, Marina, Downtown, Business Bay, JVC, Motor City, Palm Jumeirah, Bluewaters, Nad Al Sheba and JLT.",
                 path, "".join(body), jsonld=[local_business_ld(), breadcrumb_ld("Areas We Serve", path)],
                 hero=simple_hero("Areas We Serve Across Dubai",
                                  "One central workshop, mobile crews everywhere — plus 24-hour recovery dispatch for the whole emirate.",
                                  [("Areas We Serve", None)], eyebrow="Coverage", image="roadside-night"))


def blog_index():
    body = [section("Guides from the workshop",
                    "Practical advice written by the people doing the repairs — what fails, why it fails in Gulf conditions, and what it costs to fix properly.",
                    '<div class="grid g-3">%s</div>' % "".join(
                        '<article class="media-card post-card reveal"><figure>%s</figure><div class="mc-body">'
                        '<div class="pc-meta"><span>%s</span><span>·</span><span>%s</span><span>·</span><span>%s read</span></div>'
                        '<h3><a href="/blog/%s/">%s</a></h3><p>%s</p>'
                        '<a class="card-link" href="/blog/%s/">%s %s</a></div></article>'
                        % (img(p["img"], p["title"]), esc(p["category"]), esc(p["date"]), esc(p["read"]),
                           p["slug"], esc(p["title"]), esc(p["excerpt"]), p["slug"], "Read the guide", icon("arrow"))
                        for p in POSTS), centered=True)]
    cats = sorted(set(p["category"] for p in POSTS))
    body.append(section("Browse by topic", None,
                        '<div class="tag-cloud">%s</div>' % "".join('<a href="/blog/">%s</a>' % esc(c) for c in cats),
                        alt=True, tight=True))
    body.append(cta_band("Have a question we have not answered?",
                         "Ask it directly — a technician will reply, not a salesperson. If we cannot help, we will tell you who can."))
    path = "/blog/"
    return shell("Car Repair Guides & Advice | %s" % SITE["brand"],
                 "Practical car maintenance and repair guides for Dubai drivers: batteries, air conditioning, oil intervals, warning lights, tyres, brakes, used car buying and roadside emergencies.",
                 path, "".join(body), jsonld=[local_business_ld(), breadcrumb_ld("Guides", path)],
                 hero=simple_hero("Guides &amp; Advice from the Workshop",
                                  "What actually goes wrong with cars in this climate, and what to do about it.",
                                  [("Guides", None)], eyebrow="Blog", image="diagnostics"))


def about_page():
    body = []
    body.append(section("", "",
        '<div class="split reveal"><div><span class="eyebrow">About the workshop</span>'
        '<h2>An independent garage built on doing the diagnosis first</h2>'
        '<p class="muted">GearCraft Auto Works started in %d as a two-bay workshop in Al Quoz with a simple idea: find out what is '
        'actually wrong before recommending anything. That principle has not changed as the facility has grown into a full-service '
        'workshop with bodyshop, alignment bay, air conditioning equipment and round-the-clock recovery crews.</p>'
        '<p class="muted">We are independent, which means we answer to customers rather than to a manufacturer\'s parts targets. '
        'Where a component can be repaired instead of replaced, we say so. Where a job can wait, we say that too. Where something is '
        'genuinely urgent, we show you the evidence — measurements, fault data or photographs — rather than asking you to take our word.</p>'
        '<p class="muted">Today our team of technicians handles everything from a battery replacement in an office car park to a full '
        'engine rebuild, with the same documentation standards applied to both.</p>'
        '<div class="btn-row" style="margin-top:22px"><a class="btn" href="%s" target="_blank" rel="noopener">%s Meet us on WhatsApp</a>'
        '<a class="btn btn-ghost" href="/contact/">%s Visit the workshop</a></div></div>'
        '<div class="split-media">%s<div class="badge-float">%s<span><strong>%d</strong><span>years in the trade</span></span></div></div></div>'
        % (SITE["founded_year"], whatsapp_url(), icon("whatsapp"), icon("pin"),
           img("team-workshop", "GearCraft Auto Works technicians"), icon("clock"), 2026 - SITE["founded_year"])))

    body.append(section("What we believe", None, cards([
        {"title": "Diagnosis before parts", "icon": "diag", "text": "Replacing components until a fault disappears is expensive and unreliable. We test the circuit, measure the data and prove the cause."},
        {"title": "One price, agreed in advance", "icon": "note", "text": "You approve a written quote before work begins. If something else is found, you get photographs and a revised figure — not a surprise at collection."},
        {"title": "Right part for the job", "icon": "shield", "text": "Genuine or manufacturer-equivalent, with the difference explained. We do not fit the cheapest option on safety-critical systems."},
        {"title": "Records that follow the car", "icon": "car", "text": "Every visit documented with parts, specifications and recommendations — useful for warranty questions and resale value."},
    ], cols=4), alt=True, centered=True))

    body.append(section("The facility", None,
        '<div class="grid g-3">%s</div>' % "".join(
            '<div class="media-card reveal"><figure>%s</figure><div class="mc-body"><h3>%s</h3><p>%s</p></div></div>'
            % (img(i, t), esc(t), esc(x)) for i, t, x in [
                ("hero-workshop", "Workshop floor", "Multiple hydraulic lifts including high-clearance bays for SUVs and vans, with a parts desk that sources OEM and quality aftermarket components the same day."),
                ("diagnostics", "Diagnostics bay", "Manufacturer-level scanning platforms, oscilloscope testing, battery and charging analysis, and coding equipment for module work."),
                ("tyre-service", "Tyre & alignment", "Computerised four-wheel alignment, road-force balancing, tyre changing bays and a stocked range of common sizes."),
                ("ac-repair", "Air conditioning", "Dedicated recovery and recharge machines for both R134a and R1234yf, with electronic leak detection and vent temperature measurement."),
                ("bodywork-paint", "Bodyshop", "Panel repair, welding, chassis checking and a dust-controlled spray booth with colour matching to factory paint codes."),
                ("roadside-night", "Recovery fleet", "Flatbed and wheel-lift units plus low-profile equipment for basement extraction, staffed by technicians rather than drivers only."),
            ])))

    body.append(section("How we work with you", None,
        '<div class="steps">%s</div>' % "".join(
            '<div class="step reveal"><h3>%s</h3><p>%s</p></div>' % (esc(t), esc(x)) for t, x in PROCESS),
        centered=True, alt=True))
    body.append(stats_band())
    body.append(testimonial_slider())
    body.append(cta_band("Come and see the workshop",
                         "Walk in during opening hours, meet the team and have a look at the facility. No appointment needed for a conversation."))
    path = "/about/"
    return shell("About GearCraft Auto Works — Independent Car Repair Workshop in Dubai",
                 "About our independent car repair workshop in Al Quoz, Dubai: our history, standards, facilities, team and how we approach diagnosis, pricing and documentation.",
                 path, "".join(body), jsonld=[local_business_ld(), breadcrumb_ld("About", path)],
                 hero=simple_hero("About GearCraft Auto Works",
                                  "An independent workshop in Al Quoz that diagnoses before it recommends, and quotes before it starts.",
                                  [("About", None)], eyebrow="About us", image="team-workshop"))


def contact_page():
    body = []
    form = (
        '<div class="form-card reveal"><form data-form="contact" novalidate>'
        '<h3 style="margin-bottom:6px">Send us a message</h3>'
        '<p class="muted small" style="margin-bottom:20px">For an urgent breakdown, call the 24-hour line — it is faster than any form.</p>'
        '<div class="form-grid">'
        '<div class="field"><label for="c-name">Your name</label><input id="c-name" name="name" type="text" autocomplete="name" required></div>'
        '<div class="field"><label for="c-phone">Phone</label><input id="c-phone" name="phone" type="tel" autocomplete="tel" required></div>'
        '<div class="field"><label for="c-email">Email</label><input id="c-email" name="email" type="email" autocomplete="email"></div>'
        '<div class="field"><label for="c-topic">What is this about?</label>'
        '<select id="c-topic" name="topic"><option>Workshop booking</option><option>Roadside assistance</option>'
        '<option>Estimate / pricing</option><option>Fleet or business account</option><option>Feedback</option>'
        '<option>Something else</option></select></div>'
        '<div class="field"><label for="c-vehicle">Vehicle (make, model, year)</label><input id="c-vehicle" name="vehicle" type="text" placeholder="e.g. 2019 Toyota Camry"></div>'
        '<div class="field"><label for="c-time">Preferred time</label><input id="c-time" name="time" type="text" placeholder="e.g. Saturday morning"></div>'
        '<div class="field full"><label for="c-message">Message</label><textarea id="c-message" name="message" placeholder="Tell us what is happening with the car…"></textarea></div>'
        '</div>'
        '<button class="btn btn-block" type="submit" style="margin-top:16px">%s Prepare my message</button>'
        '<div class="form-status" role="status" aria-live="polite"></div>'
        '<div class="btn-row" data-out style="margin-top:14px"></div>'
        '<p class="form-note">Your details stay in your browser — the message is composed locally and sent by you through WhatsApp or email.</p>'
        '</form></div>'
    ) % icon("mail")

    info = (
        '<div class="info-box reveal">'
        '<h3>Workshop details</h3>'
        '<div class="info-row">%s<span><span class="ir-label">Address</span>'
        '<span class="ir-value">%s<br><span class="muted small">%s</span></span></span></div>'
        '<div class="info-row">%s<span><span class="ir-label">Phone &amp; WhatsApp</span>'
        '<span class="ir-value"><a href="tel:%s">%s</a><br><span class="muted small">%s 24-hour recovery line</span></span></span></div>'
        '<div class="info-row">%s<span><span class="ir-label">Email</span>'
        '<span class="ir-value"><a href="mailto:%s">%s</a></span></span></div>'
        '<div class="info-row">%s<span><span class="ir-label">Workshop hours</span>'
        '<span class="ir-value">%s</span></span></div>'
        '<div class="info-row">%s<span><span class="ir-label">Roadside &amp; recovery</span>'
        '<span class="ir-value">%s</span></span></div>'
        '<div class="info-row">%s<span><span class="ir-label">Getting here</span>'
        '<span class="ir-value muted small">A few minutes from Sheikh Zayed Road, with easy access from Business Bay, Al Barsha, '
        'Umm Suqeim and Jumeirah. Plus code 46WP+F5 Dubai. Message us and we will send an entrance pin.</span></span></div>'
        '<div class="btn-row" style="margin-top:20px">'
        '<a class="btn" href="%s" target="_blank" rel="noopener">%s WhatsApp</a>'
        '<a class="btn btn-ghost" href="%s" target="_blank" rel="noopener">%s Directions</a>'
        '</div></div>'
    ) % (icon("pin"), esc(SITE["address_street"]), esc(SITE["address_city"]),
         icon("phone"), SITE["tel"], SITE["phone_label"], icon("whatsapp"),
         icon("mail"), SITE["email"], SITE["email"],
         icon("clock"), esc(SITE["hours"]),
         icon("recovery"), esc(SITE["roadside_hours"]),
         icon("car"), whatsapp_url(), icon("whatsapp"), icon("pin"),
         SITE["map_url"])

    body.append('<section class="section"><div class="wrap"><div class="split" style="align-items:start">%s%s</div></div></section>' % (form, info))
    body.append(section("Find the workshop", None,
        '<div class="map-frame"><div class="map-static"><div>%s<strong>%s</strong>%s<br>'
        '<a class="btn btn-sm" style="margin-top:14px" href="%s" target="_blank" rel="noopener">%s Open in Google Maps</a>'
        '</div></div></div>' % (icon("pin"), esc(SITE["address_full"]), SITE["license_note"],
                                SITE["map_url"], icon("pin")), alt=True, centered=True))
    body.append(section("Quick answers", None,
        '<div class="grid g-3">%s</div>' % cards([
            {"title": "Need a quote?", "icon": "note", "text": "Send the car details and the symptom. We reply with a realistic estimate and expected timeframe.", "href": "/faq/"},
            {"title": "Broken down now?", "icon": "tow", "text": "Call the 24-hour line or message on WhatsApp with your location pin.", "href": "/roadside-assistance/"},
            {"title": "Fleet or business?", "icon": "users", "text": "We set up scheduled maintenance, priority response and monthly reporting for small fleets.", "href": "/services/car-interval-service/"},
        ], cols=3), tight=True))
    body.append(cta_band())
    path = "/contact/"
    return shell("Contact GearCraft Auto Works — Car Repair Workshop in Al Quoz, Dubai",
                 "Contact our car repair workshop in Al Quoz, Dubai by phone, WhatsApp or email. Workshop hours, 24/7 roadside line, address and directions.",
                 path, "".join(body), jsonld=[local_business_ld(), breadcrumb_ld("Contact", path)],
                 hero=simple_hero("Contact the Workshop",
                                  "Message, call or walk in. For breakdowns, the 24-hour line is always staffed.",
                                  [("Contact", None)], eyebrow="Contact"))


def reviews_page():
    body = []
    cards_html = "".join(
        '<article class="quote-card reveal" style="border-radius:var(--radius)">'
        '<div class="stars" aria-label="Rated 5 out of 5">%s</div>'
        '<p class="quote-text">%s</p>'
        '<div class="quote-meta"><span class="avatar" aria-hidden="true">%s</span>'
        '<span><span class="quote-name">%s</span><br><span class="quote-sub">%s</span></span></div></article>'
        % ("".join(icon("star") for _ in range(5)), esc(t["text"]),
           "".join(w[0] for w in t["name"].split()[:2]).upper(), esc(t["name"]), esc(t["role"]))
        for t in TESTIMONIALS)
    body.append(section("Reviews from drivers across Dubai",
                        "A selection of feedback from customers who have used the workshop, the mobile mechanic service and the 24-hour recovery crews.",
                        '<div class="grid g-3">%s</div>' % cards_html, centered=True))
    body.append(stats_band())
    body.append(section("What people mention most", None,
        '<div class="grid g-4">%s</div>' % cards([
            {"title": "Clear pricing", "icon": "note", "text": "Quotes agreed before work starts, and the bill matching what was quoted."},
            {"title": "Honest diagnosis", "icon": "diag", "text": "Being told when a repair can wait, and shown evidence when it cannot."},
            {"title": "Fast response", "icon": "clock", "text": "Recovery crews arriving within the window they promised, including overnight."},
            {"title": "Proper follow-up", "icon": "shield", "text": "A call after the job to confirm everything is still right, and records kept for next time."},
        ], cols=4), alt=True, centered=True))
    body.append(section("Leave a review",
                        "If we have worked on your car, we would genuinely like to hear how it went — including where we could do better.",
                        '<div class="center btn-row" style="justify-content:center">'
                        '<a class="btn" href="%s" target="_blank" rel="noopener">%s Send feedback on WhatsApp</a>'
                        '<a class="btn btn-ghost" href="mailto:%s?subject=%s">%s Email feedback</a></div>'
                        % (whatsapp_url(), icon("whatsapp"), SITE["email"], "Feedback", icon("mail")), centered=True))
    body.append(cta_band())
    path = "/reviews/"
    return shell("Customer Reviews — %s" % SITE["brand"],
                 "Customer reviews for our car repair workshop and 24/7 roadside assistance in Dubai, covering diagnostics, air conditioning, brakes, batteries, recovery and mobile mechanics.",
                 path, "".join(body), jsonld=[local_business_ld(), breadcrumb_ld("Reviews", path)],
                 hero=simple_hero("Customer Reviews",
                                  "What drivers say after using the workshop, the mobile service and the recovery crews.",
                                  [("Reviews", None)], eyebrow="Reviews", image="team-workshop"))


def faq_page():
    from data_services import CORE_SERVICES
    groups = [
        ("Workshop & booking", HOME_FAQ[:3]),
        ("Services & capability", HOME_FAQ[3:6]),
        ("Pricing, warranty & records", [
            ("How do you price work?", "Diagnosis first, then a written quote separating parts, labour and consumables. You approve before work starts, and if we find something additional we come back to you with photographs rather than adding it silently to the bill."),
            ("Is there a minimum charge?", "Diagnostics carry a fixed fee that is offset against the repair if you proceed with us. Mobile visits have a call-out charge that is also offset when work is carried out."),
            ("Do you guarantee your work?", "Yes. Parts carry their manufacturer's warranty and our workmanship is guaranteed. If a repair we carried out fails prematurely, we put it right."),
            ("Can I see the old parts?", "Always. We keep replaced components and show them at hand-back, which is one of the simplest ways to verify what was actually done."),
            ("Which payment methods do you take?", "Card, bank transfer and cash. Business and fleet accounts can be arranged with monthly invoicing."),
        ]),
        ("Roadside assistance", [
            ("How fast is roadside response?", "Typically 30 to 45 minutes inside central Dubai depending on traffic and time of day, longer in outlying areas. We give you a realistic window when you call and update you while the unit is en route."),
            ("What does a call-out cost?", "You are told the call-out charge and any likely extras before dispatch. It does not change unless you alter the destination or scope."),
            ("Can you repair at the roadside?", "Often — batteries, tyres, fuel, belts, fuses and many electrical faults are resolved on site. Anything needing a lift or specialist equipment is recovered to the workshop."),
            ("Do you recover from basement parking?", "Yes, using low-profile equipment for height-restricted garages. Tell us the building, level and ceiling height when you call."),
            ("Are you available on public holidays?", "Yes. Recovery crews operate 24 hours a day, every day of the year."),
        ]),
        ("Vehicle types", [
            ("Do you service hybrid and electric cars?", "Yes, with high-voltage safety procedures, insulated tooling and battery health diagnostics. We handle hybrids, plug-in hybrids and full EVs."),
            ("What about classic and collector cars?", "We recommission stored vehicles, repair mechanical and electrical systems, and manage staged restoration projects with documented progress."),
            ("Can you work on commercial vans and fleets?", "We look after small and medium fleets with scheduled servicing, priority response, downtime planning and monthly reporting."),
            ("Do you handle imported and non-GCC specification cars?", "Yes, and we specify parts to match your car's actual configuration rather than assuming GCC specification."),
        ]),
    ]
    blocks = []
    for title, items in groups:
        blocks.append('<div><h2 style="font-size:1.5rem">%s</h2><div class="accordion">%s</div></div>' % (
            esc(title), "".join(
                '<details class="acc-item"><summary>%s<span class="acc-icon" aria-hidden="true"></span></summary>'
                '<div class="acc-body"><p>%s</p></div></details>' % (esc(q), esc(a)) for q, a in items)))
    body = [section("Frequently asked questions",
                    "Answers to the questions we field every day, grouped so you can find yours quickly.",
                    '<div style="display:grid;gap:42px">%s</div>' % "".join(blocks), centered=False)]
    body.append(section("Still unsure?", None,
        '<div class="grid g-3">%s</div>' % cards([
            {"title": "Ask a technician", "icon": "whatsapp", "text": "Describe the symptom on WhatsApp and get a straight answer, not a sales pitch.", "href": "/contact/"},
            {"title": "See the services", "icon": "wrench", "text": "Every service we offer, with what it involves and what it usually takes.", "href": "/services/"},
            {"title": "Read the guides", "icon": "note", "text": "Practical articles on batteries, air conditioning, tyres, brakes and warning lights.", "href": "/blog/"},
        ], cols=3), alt=True, centered=True))
    body.append(cta_band())
    path = "/faq/"
    return shell("FAQ — Car Repair & Roadside Assistance Questions | %s" % SITE["brand"],
                 "Answers to common questions about car repair, servicing, diagnostics, pricing, warranty, roadside assistance and recovery in Dubai.",
                 path, "".join(body), jsonld=[local_business_ld(), breadcrumb_ld("FAQ", path)],
                 hero=simple_hero("Frequently Asked Questions",
                                  "Straight answers about booking, pricing, roadside response and what we can work on.",
                                  [("FAQ", None)], eyebrow="Help & info"))


def not_found():
    n = nav_structure()
    body = [
        '<section class="err-page"><div class="wrap">'
        '<div class="err-code">404</div>'
        '<h1 style="margin-top:10px">This page has driven off</h1>'
        '<p class="muted" style="max-width:52ch;margin-inline:auto">The link may be old or mistyped. '
        'Everything we offer is one click away below — or call the workshop and we will point you in the right direction.</p>'
        '<div class="btn-row center" style="justify-content:center;margin-top:24px">'
        '<a class="btn" href="/">%s Back to home</a>'
        '<a class="btn btn-ghost" href="/services/">%s All services</a>'
        '<a class="btn btn-ghost" href="tel:%s">%s %s</a></div>'
        '</div></section>' % (icon("car"), icon("wrench"), SITE["tel"], icon("phone"), SITE["phone_label"]),
        section("Popular pages", None, '<div class="related-strip">%s</div>' % "".join(
            '<a class="tile reveal" href="%s">%s<span>%s</span></a>' % (h, icon(i), esc(t)) for t, h, i in [
                ("Roadside assistance", "/roadside-assistance/", "tow"),
                ("Car repair in Dubai", "/services/car-repair-dubai/", "wrench"),
                ("AC repair", "/services/car-ac-repair-dubai/", "ac"),
                ("Diagnostics", "/services/car-scanning-and-diagnostic/", "diag"),
                ("Battery replacement", "/services/car-battery-replacement/", "battery"),
                ("Tyres & alignment", "/services/car-tyres-and-flat-tyre/", "tyre"),
            ]), tight=True),
        section("Services", None, '<ul class="pill-list">%s</ul>' % "".join(
            '<li><a href="/services/%s/">%s</a></li>' % (s["slug"], esc(s["name"])) for s in n["services"]), alt=True),
    ]
    return shell("Page Not Found | %s" % SITE["brand"],
                 "The page you were looking for does not exist. Browse car repair services, roadside assistance and guides instead.",
                 "/404.html", "".join(body), jsonld=[local_business_ld()])
