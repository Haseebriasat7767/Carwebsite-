# -*- coding: utf-8 -*-
"""HTML rendering layer: icons, chrome (header/footer), page templates."""
import os
from data_site import SITE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(ROOT, "assets", "img")

# --------------------------------------------------------------------- icons
_P = {
    "engine": '<path d="M4 14h2v-3h3V9h5v2h3l2 2h2v4h-2v2h-3v-2H9v2H6v-3H4z"/><path d="M9 9V7h4v2"/>',
    "ac": '<path d="M12 3v18M4.5 7.5l15 9M19.5 7.5l-15 9"/><path d="M12 7l-2-2M12 7l2-2M12 17l-2 2M12 17l2 2"/>',
    "brake": '<circle cx="12" cy="12" r="8.2"/><circle cx="12" cy="12" r="3.2"/><path d="M12 3.8v3M12 17.2v3M3.8 12h3M17.2 12h3"/>',
    "battery": '<rect x="2.5" y="7" width="16" height="10" rx="2"/><path d="M18.5 10h2.2v4h-2.2M6 4.8v2.2M13 4.8v2.2"/><path d="M9 12h3l-1.4 2.4"/>',
    "tyre": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="3.4"/><path d="M12 3.5v4M12 16.5v4M3.5 12h4M16.5 12h4"/>',
    "oil": '<path d="M4 17h10a3 3 0 0 0 0-6H9l-2-2H4z"/><path d="M17 8l3 3M18.5 5.5c1.5 1.6 1.4 3.2.4 4.2"/><path d="M6 11V8h3"/>',
    "diag": '<rect x="3" y="4.5" width="12" height="15" rx="2"/><path d="M6 9h6M6 12h6M6 15h3"/><path d="M15 10h3.5a2.5 2.5 0 0 1 0 5H16"/>',
    "gear": '<circle cx="12" cy="12" r="3.2"/><path d="M12 2.8v3M12 18.2v3M2.8 12h3M18.2 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M18.4 5.6l-2.1 2.1M7.7 16.3l-2.1 2.1"/>',
    "susp": '<path d="M7 3v18M17 3v18"/><path d="M7 6h10M7 18h10"/><path d="M9 8.5c3 0 3 2.5 6 2.5s3-2.5 6-2.5" /><path d="M9 13c3 0 3 2.5 6 2.5"/>',
    "elec": '<path d="M13 2.5 5 13.5h6L10 21.5l9-11.5h-6.5z"/>',
    "body": '<path d="M3 16h18"/><path d="M5.5 16V12l2-4.2h9L19 12v4"/><circle cx="7.8" cy="16.6" r="1.9"/><circle cx="16.2" cy="16.6" r="1.9"/><path d="M9.7 12h4.6"/>',
    "mobile": '<path d="M3 17h13V8.5H3z"/><path d="M16 11h3.2L21 14v3h-5"/><circle cx="7" cy="18.6" r="1.7"/><circle cx="17.6" cy="18.6" r="1.7"/><path d="M6 5.5h6M9 3.2v4.6"/>',
    "inspect": '<circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.4 15.4 21 21"/><path d="M8 10.6l1.9 1.9 3.4-3.6"/>',
    "service": '<path d="M14.5 5.5a4.2 4.2 0 0 0-5.7 5.4L4 15.7a2 2 0 1 0 2.8 2.8l4.8-4.8a4.2 4.2 0 0 0 5.4-5.7l-2.6 2.6-2.4-.6-.6-2.4z"/>',
    "classic": '<path d="M4 15.5h16"/><path d="M6 15.5v-2.2l1.6-3.1h8.8L18 13.3v2.2"/><circle cx="8" cy="16.2" r="1.7"/><circle cx="16" cy="16.2" r="1.7"/><path d="M9.4 10.2h5.2"/><path d="M12 5.6v1.8"/>',
    "ev": '<path d="M5 18V8.5L12 5l7 3.5V18"/><path d="M12 9.5v5M9.8 12h4.4"/><path d="M3 18h18"/>',
    "tow": '<path d="M3 17h9V9.5H3z"/><path d="M12 12h4.5l2.5 2.5V17h-7"/><circle cx="6.4" cy="18.4" r="1.7"/><circle cx="16.4" cy="18.4" r="1.7"/><path d="M15 12V7.5h4"/>',
    "fuel": '<path d="M5 20V6.5A1.5 1.5 0 0 1 6.5 5h5A1.5 1.5 0 0 1 13 6.5V20"/><path d="M4 20h10"/><path d="M6.8 9.4h4.4"/><path d="M13 10h2.6a1.6 1.6 0 0 1 1.6 1.6V16a1.4 1.4 0 0 0 2.8 0V9l-2.4-2.6"/>',
    "lock": '<rect x="4.5" y="10" width="15" height="10.5" rx="2"/><path d="M8 10V7.2a4 4 0 0 1 8 0V10"/><path d="M12 14v3"/>',
    "winch": '<circle cx="7" cy="14" r="3.4"/><path d="M10.4 14H21"/><path d="M17 14v-4h3.5"/><path d="M4 20h16"/>',
    "recovery": '<path d="M12 3.5 20 7v6c0 4.2-3.3 6.6-8 8-4.7-1.4-8-3.8-8-8V7z"/><path d="M9 12l2.2 2.2L15.4 10"/>',
    "key": '<circle cx="8" cy="15.5" r="3.6"/><path d="M10.6 13 20 3.8"/><path d="M16.4 7.4 18.6 9.6M14 9.8l2.2 2.2"/>',
    "offroad": '<path d="M3 18.5h18"/><path d="M6 18.5 10.5 10l3 4.5 2-2.5 3 6.5"/><circle cx="17.5" cy="6" r="2"/><path d="M4.5 8.5 8 6"/>',
    "accident": '<path d="M12 3.6 21 19H3z"/><path d="M12 9.4v4.2"/><circle cx="12" cy="16.3" r=".9" fill="currentColor" stroke="none"/>',
    "wrench": '<path d="M15.4 4.6a4.6 4.6 0 0 0-5.9 5.9L4 16a2 2 0 1 0 2.8 2.8l5.5-5.5a4.6 4.6 0 0 0 5.9-5.9l-2.8 2.8-2.6-.6-.6-2.6z"/>',
    "shield": '<path d="M12 3.2 19.5 6v6.2c0 4.1-3.1 6.6-7.5 8-4.4-1.4-7.5-3.9-7.5-8V6z"/><path d="M9.2 12.2l2 2 3.6-3.9"/>',
    "clock": '<circle cx="12" cy="12" r="8.6"/><path d="M12 7v5.3l3.4 2"/>',
    "sensor": '<circle cx="12" cy="12" r="2.6"/><path d="M7.8 7.8a6 6 0 0 0 0 8.4M16.2 16.2a6 6 0 0 0 0-8.4"/><path d="M5 5a10 10 0 0 0 0 14M19 19a10 10 0 0 0 0-14"/>',
    "chip": '<rect x="6.5" y="6.5" width="11" height="11" rx="1.8"/><path d="M10 10h4v4h-4z"/><path d="M9.5 3.2v3.3M14.5 3.2v3.3M9.5 17.5v3.3M14.5 17.5v3.3M3.2 9.5h3.3M3.2 14.5h3.3M17.5 9.5h3.3M17.5 14.5h3.3"/>',
    "paint": '<path d="M4 8.5h16v4.2H4z"/><path d="M12 12.7v3.1"/><path d="M10 15.8h4v4.7h-4z"/><path d="M7 8.5V5.2h10v3.3"/>',
    "wheel": '<circle cx="12" cy="12" r="8.6"/><circle cx="12" cy="12" r="2"/><path d="M12 3.4v4M12 16.6v4M4.6 8l3.6 2M15.8 14l3.6 2M4.6 16l3.6-2M15.8 10l3.6-2"/>',
    "calendar": '<rect x="3.5" y="5.5" width="17" height="15" rx="2"/><path d="M3.5 10h17M8 3.5v4M16 3.5v4"/><path d="M7.5 13.5h2M11 13.5h2M14.5 13.5h2M7.5 17h2M11 17h2"/>',
    "gauge": '<path d="M4 17a8.5 8.5 0 1 1 16 0"/><path d="M12 17l4.2-5.2"/><circle cx="12" cy="17" r="1.4"/>',
    "phone": '<path d="M6.2 3.5h3l1.6 4-2 1.4a12.5 12.5 0 0 0 6.3 6.3l1.4-2 4 1.6v3a2 2 0 0 1-2.2 2A17.6 17.6 0 0 1 4.2 5.7a2 2 0 0 1 2-2.2z"/>',
    "whatsapp": '<path d="M12 3.4a8.5 8.5 0 0 0-7.2 13L3.5 20.6l4.4-1.2A8.5 8.5 0 1 0 12 3.4zm0 1.7a6.8 6.8 0 1 1-3.5 12.6l-.4-.2-2.3.6.6-2.2-.2-.4A6.8 6.8 0 0 1 12 5.1zm-3 3.2c-.2 0-.5.1-.6.3-.2.2-.6.7-.6 1.6s.7 1.8.8 1.9c.1.2 1.3 2 3.2 2.8 1.6.6 2 .5 2.3.5.4 0 1.2-.5 1.4-1 .2-.5.2-.9.1-1-.1 0-.3-.1-.5-.2l-1.4-.7c-.2-.1-.3-.1-.4.1l-.5.7c-.1.1-.2.2-.4.1-.2-.1-.9-.3-1.6-1-.6-.5-1-1.1-1.1-1.3-.1-.2 0-.3.1-.4l.3-.4.2-.3v-.3l-.6-1.4c-.1-.3-.3-.3-.4-.3z"/>',
    "pin": '<path d="M12 21s6.8-6 6.8-11A6.8 6.8 0 0 0 5.2 10c0 5 6.8 11 6.8 11z"/><circle cx="12" cy="10" r="2.6"/>',
    "mail": '<rect x="3" y="5.5" width="18" height="13" rx="2"/><path d="M3.6 6.6 12 13l8.4-6.4"/>',
    "star": '<path d="m12 3.6 2.6 5.4 5.9.8-4.3 4.1 1.1 5.9L12 17l-5.3 2.8 1.1-5.9L3.5 9.8l5.9-.8z"/>',
    "check": '<path d="M4.5 12.5 9.5 17.5 19.5 6.5"/>',
    "arrow": '<path d="M4 12h15"/><path d="m13 6 6 6-6 6"/>',
    "chev": '<path d="m6 9 6 6 6-6"/>',
    "users": '<circle cx="9" cy="8.5" r="3.2"/><path d="M3.5 19.5c0-3.2 2.5-5.2 5.5-5.2s5.5 2 5.5 5.2"/><path d="M16 6.2a3.2 3.2 0 0 1 0 6.2M17.5 14.8c2 .6 3.2 2.3 3.2 4.7"/>',
    "car": '<path d="M3.5 15.5h17"/><path d="M5.8 15.5v-2.2l1.9-3.8h8.6l1.9 3.8v2.2"/><circle cx="8" cy="16.4" r="1.8"/><circle cx="16" cy="16.4" r="1.8"/><path d="M9.6 9.5h4.8"/>',
    "bolt": '<path d="M13 2.8 5.5 13.6h5.2L10 21.2l8-11.1h-5.4z"/>',
    "snow": '<path d="M12 3v18M4.2 7.5l15.6 9M19.8 7.5l-15.6 9"/><path d="M12 6.6 9.9 4.9M12 6.6l2.1-1.7M12 17.4l-2.1 1.7M12 17.4l2.1 1.7"/>',
    "quote": '<path d="M9.4 6C6.7 7.3 5 9.8 5 12.9c0 2.7 1.6 4.6 3.8 4.6 1.9 0 3.3-1.4 3.3-3.2 0-1.8-1.3-3.1-3-3.1-.4 0-.7 0-1 .2.2-1.4 1.3-2.7 2.7-3.5zm8 0c-2.7 1.3-4.4 3.8-4.4 6.9 0 2.7 1.6 4.6 3.8 4.6 1.9 0 3.3-1.4 3.3-3.2 0-1.8-1.3-3.1-3-3.1-.4 0-.7 0-1 .2.2-1.4 1.3-2.7 2.7-3.5z"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
    "facebook": '<path d="M14.5 8.5h2.2V5.3h-2.6c-2.3 0-3.8 1.5-3.8 3.9v1.6H8v3.2h2.3V21h3.3v-7h2.4l.4-3.2h-2.8V9.6c0-.7.3-1.1.9-1.1z"/>',
    "instagram": '<rect x="3.6" y="3.6" width="16.8" height="16.8" rx="4.6"/><circle cx="12" cy="12" r="4"/><circle cx="17" cy="7" r="1.1"/>',
    "youtube": '<rect x="2.8" y="5.6" width="18.4" height="12.8" rx="3.6"/><path d="m10.2 9.2 5 2.8-5 2.8z"/>',
    "tiktok": '<path d="M14.2 3.5v10.8a3.4 3.4 0 1 1-3.4-3.4c.4 0 .7 0 1 .1"/><path d="M14.2 3.5c.4 2.2 1.9 3.7 4.1 3.9"/>',
    "tag": '<path d="M3.8 11.4V4.4h7l8.4 8.4a2 2 0 0 1 0 2.8l-4.2 4.2a2 2 0 0 1-2.8 0z"/><circle cx="7.6" cy="8.1" r="1.3"/>',
    "sparkle": '<path d="M12 3.5 13.7 9l5.5 1.7-5.5 1.7L12 18l-1.7-5.6L4.8 10.7 10.3 9z"/>',
    "note": '<path d="M6 3.5h9l4 4v13H6z"/><path d="M15 3.5v4h4"/><path d="M9 12h7M9 16h5"/>',
}


def esc(s):
    import html as _h
    s = str(s)
    prev = None
    while s != prev:
        prev = s
        s = _h.unescape(s)
    return _h.escape(s, quote=True)


def icon(name, cls=""):
    d = _P.get(name) or _P["wrench"]
    fill = ' fill="currentColor" stroke="none"' if name in (
        "whatsapp", "star", "quote", "facebook", "instagram", "youtube", "tiktok", "elec", "ev", "bolt") else ""
    c = ' class="' + cls + '"' if cls else ""
    stroke_attr = '' if fill else ' stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" fill="none"'
    return '<svg%s viewBox="0 0 24 24"%s%s aria-hidden="true" focusable="false">%s</svg>' % (c, fill, stroke_attr, d)


#: Contextually sensible substitutes, used only while a named image is absent.
FALLBACKS = {
    "bodywork-paint": ["engine-repair", "hero-workshop"],
    "mobile-mechanic": ["roadside-night", "hero-workshop"],
    "team-workshop": ["hero-workshop", "diagnostics"],
    "suspension": ["brake-repair", "tyre-service"],
    "electrical-wiring": ["diagnostics", "battery-service"],
}


def img(name, alt="", cls="", loading="lazy"):
    """Return an <img> tag; fall back to an available image if one is missing."""
    candidates = ["%s.jpg" % name, "%s.webp" % name, "%s.png" % name]
    chosen = None
    for c in candidates:
        if os.path.exists(os.path.join(IMG_DIR, c)):
            chosen = "/assets/img/" + c
            break
    if not chosen:
        for fb in FALLBACKS.get(name, []) + ["hero-workshop", "diagnostics", "engine-repair"]:
            for ext in (".jpg", ".webp", ".png"):
                if os.path.exists(os.path.join(IMG_DIR, fb + ext)):
                    chosen = "/assets/img/" + fb + ext
                    break
            if chosen:
                break
    if not chosen:
        return ""
    cl = ' class="%s"' % cls if cls else ""
    return '<img src="%s" alt="%s"%s loading="%s" decoding="async">' % (chosen, esc(alt), cl, loading)


# ------------------------------------------------------------------ navigation
def nav_structure():
    from data_services import CORE_SERVICES, ROADSIDE_SERVICES
    from data_catalog import BRAND_GROUPS, MARQUES, LOCATIONS, POSTS
    return {
        "services": CORE_SERVICES,
        "roadside": ROADSIDE_SERVICES,
        "brands": BRAND_GROUPS,
        "marques": MARQUES,
        "locations": LOCATIONS,
        "posts": POSTS,
    }


def header(active):
    n = nav_structure()
    core = [s for s in n["services"] if s.get("tag") in ("core", "mechanical", "diagnostics", "safety")]
    comfort = [s for s in n["services"] if s.get("tag") in ("comfort", "electrical", "maintenance", "body", "specialist", "convenience", "inspection")]
    rs = n["roadside"][:8]
    rs2 = n["roadside"][8:]
    brands = n["brands"]
    marques = n["marques"]
    locs = n["locations"]
    posts = n["posts"][:5]

    def dd_links(items, urlfn, namekey="name"):
        return "".join('<a class="dd-link" href="%s"><span>%s</span></a>' % (urlfn(i), esc(i[namekey])) for i in items)

    def item(label, href, key, dd_html=None):
        cur = ' aria-current="page"' if active == key else ""
        chev = icon("chev", "chev") if dd_html else ""
        a = '<a class="nav-link" href="%s"%s>%s%s</a>' % (href, cur, label, chev) if href else \
            '<button class="nav-link" type="button" aria-expanded="false">%s%s</button>' % (label, chev)
        return '<div class="nav-item">%s%s</div>' % (a, dd_html or "")

    services_dd = (
        '<div class="dropdown mega">'
        '<div><div class="dd-group-title">Repairs &amp; diagnostics</div>' +
        dd_links(core, lambda s: "/services/%s/" % s["slug"]) + '</div>'
        '<div><div class="dd-group-title">Servicing &amp; specialists</div>' +
        dd_links(comfort, lambda s: "/services/%s/" % s["slug"]) + '</div>'
        '<div><div class="dd-group-title">Popular right now</div>' +
        dd_links([{"name": "Air conditioning repair", "slug": "car-ac-repair-dubai"},
                  {"name": "Computer diagnostics", "slug": "car-scanning-and-diagnostic"},
                  {"name": "Brake pads &amp; discs", "slug": "car-brake-repair"},
                  {"name": "Battery replacement", "slug": "car-battery-replacement"},
                  {"name": "Tyres &amp; alignment", "slug": "car-tyres-and-flat-tyre"},
                  {"name": "Minor service", "slug": "car-minor-service"},
                  {"name": "Major service", "slug": "car-major-service"}],
                 lambda s: "/services/%s/" % s["slug"]) +
        '<div class="dd-foot"><p>Not sure what you need? Send the symptom and we will tell you.</p>'
        '<a class="btn btn-sm" href="/contact/">Book an inspection</a></div></div>'
        '</div>'
    )

    roadside_dd = (
        '<div class="dropdown mega two-col">'
        '<div><div class="dd-group-title">24/7 recovery</div>' + dd_links(rs, lambda s: "/roadside-assistance/%s/" % s["slug"]) + '</div>'
        '<div><div class="dd-group-title">On-site help</div>' + dd_links(rs2, lambda s: "/roadside-assistance/%s/" % s["slug"]) +
        '<div class="dd-foot"><p>Stranded right now? Call the 24-hour line.</p>'
        '<a class="btn btn-sm" href="tel:%s">Call %s</a></div></div>'
        '</div>' % (SITE["tel"], SITE["phone_label"])
    )

    brands_dd = (
        '<div class="dropdown mega two-col">'
        '<div><div class="dd-group-title">By origin</div>' + dd_links(brands, lambda b: "/car-brands/%s/" % b["slug"]) + '</div>'
        '<div><div class="dd-group-title">By marque</div>' + dd_links(marques, lambda m: "/car-brands/%s/" % m["slug"]) + '</div>'
        '</div>'
    )

    areas_dd = (
        '<div class="dropdown mega two-col">'
        '<div><div class="dd-group-title">Where we work</div>' + dd_links(locs[:6], lambda l: "/areas-we-serve/%s/" % l["slug"]) + '</div>'
        '<div><div class="dd-group-title">&nbsp;</div>' + dd_links(locs[6:], lambda l: "/areas-we-serve/%s/" % l["slug"]) +
        '<div class="dd-foot"><p>Mobile mechanics and recovery crews cover the whole emirate.</p>'
        '<a class="btn btn-sm" href="/areas-we-serve/">All areas</a></div></div></div>'
    )

    blog_dd = ('<div class="dropdown mega two-col">'
               '<div><div class="dd-group-title">Latest guides</div>' + dd_links(posts, lambda p: "/blog/%s/" % p["slug"], "title") + '</div>'
               '<div><div class="dd-group-title">Browse</div>' +
               '<a class="dd-link" href="/blog/"><span>All articles</span></a>' +
               '<a class="dd-link" href="/faq/"><span>Frequently asked questions</span></a>' +
               '<a class="dd-link" href="/reviews/"><span>Customer reviews</span></a>' +
               '<a class="dd-link" href="/about/"><span>About the workshop</span></a></div></div>')

    html = ['<a class="skip-link" href="#main">Skip to content</a>',
            '<div class="topbar"><div class="wrap"><div class="topbar-left">',
            '<span class="topbar-item"><span class="pulse-dot" aria-hidden="true"></span><span data-open-now>Open now · closes 10:00 PM</span></span>',
            '<span class="topbar-item opt-hide">%s %s</span>' % (icon("pin"), SITE["address_street"]),
            '</div><div class="topbar-right">',
            '<span class="topbar-item opt-hide">%s %s</span>' % (icon("mail"), '<a href="mailto:%s">%s</a>' % (SITE["email"], SITE["email"])),
            '<span class="topbar-item">%s <span>%s</span></span>' % (icon("clock"), esc(SITE["roadside_hours"])),
            '</div></div></div>',
            '<header class="site-header"><div class="wrap header-inner">',
            '<a class="brand" href="/" aria-label="%s home">' % SITE["brand"],
            '<span class="brand-mark">%s</span>' % logo_svg(),
            '<span class="brand-text"><span class="brand-name">Gear<em>Craft</em></span>'
            '<span class="brand-tag">%s</span></span></a>' % esc(SITE["tagline"]),
            '<nav class="main-nav" aria-label="Main navigation">',
            item("Home", "/", "home"),
            item("Services", "/services/", "services", services_dd),
            item("Roadside", "/roadside-assistance/", "roadside", roadside_dd),
            item("Car Brands", "/car-brands/", "brands", brands_dd),
            item("Areas", "/areas-we-serve/", "areas", areas_dd),
            item("Guides", "/blog/", "blog", blog_dd),
            item("About", "/about/", "about"),
            item("Reviews", "/reviews/", "reviews"),
            '</nav>',
            '<div class="header-cta">',
            '<a class="header-phone" href="tel:%s">%s %s</a>' % (SITE["tel"], icon("phone"), SITE["phone_label"]),
            '<a class="btn btn-sm" href="%s" target="_blank" rel="noopener">%s WhatsApp</a>' % (whatsapp_url(), icon("whatsapp")),
            '</div>',
            '<button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false"><span></span></button>',
            '</div></header>',
            mobile_panel(active),
            '<div class="scrim" aria-hidden="true"></div>']
    return "\n".join(html)


def mobile_panel(active):
    n = nav_structure()

    def links(items, urlfn, key="name"):
        return "".join('<a href="%s">%s</a>' % (urlfn(i), esc(i[key])) for i in items)

    return (
        '<div class="mobile-panel" id="mobilePanel" aria-label="Mobile navigation">'
        '<div class="mp-head"><a class="brand" href="/"><span class="brand-mark">%s</span>'
        '<span class="brand-text"><span class="brand-name">Gear<em>Craft</em></span>'
        '<span class="brand-tag">%s</span></span></a>'
        '<button class="mp-close" type="button" aria-label="Close menu">&times;</button></div>'
        '<div class="mp-acc">'
        '<a class="mp-plain" href="/">Home</a>'
        '<details><summary>Services</summary><div class="mp-links">%s<a href="/services/">All services</a></div></details>'
        '<details><summary>Roadside Assistance</summary><div class="mp-links"><a href="/roadside-assistance/">Roadside hub</a>%s</div></details>'
        '<details><summary>Car Brands</summary><div class="mp-links">%s<a href="/car-brands/">All brands</a></div></details>'
        '<details><summary>Areas We Serve</summary><div class="mp-links">%s<a href="/areas-we-serve/">All areas</a></div></details>'
        '<details><summary>Guides &amp; Info</summary><div class="mp-links">'
        '<a href="/blog/">Blog</a><a href="/faq/">FAQ</a><a href="/reviews/">Reviews</a>'
        '<a href="/about/">About us</a><a href="/contact/">Contact</a></div></details>'
        '</div>'
        '<div class="mp-foot"><a class="btn btn-block" href="%s" target="_blank" rel="noopener">%s Book on WhatsApp</a>'
        '<a class="btn btn-ghost btn-block" href="tel:%s">%s Call %s</a></div>'
        '</div>'
    ) % (logo_svg(), esc(SITE["tagline"]),
         links(n["services"], lambda s: "/services/%s/" % s["slug"]),
         links(n["roadside"], lambda s: "/roadside-assistance/%s/" % s["slug"]),
         links(n["brands"], lambda b: "/car-brands/%s/" % b["slug"]) + links(n["marques"], lambda m: "/car-brands/%s/" % m["slug"]),
         links(n["locations"], lambda l: "/areas-we-serve/%s/" % l["slug"]),
         whatsapp_url(), icon("whatsapp"), SITE["tel"], icon("phone"), SITE["phone_label"])


def logo_svg():
    return ('<svg viewBox="0 0 48 48" aria-hidden="true" focusable="false">'
            '<defs><linearGradient id="gcl" x1="0" y1="0" x2="1" y2="1">'
            '<stop offset="0%" stop-color="#ffc44d"/><stop offset="55%" stop-color="#ff8a1e"/>'
            '<stop offset="100%" stop-color="#e85d04"/></linearGradient></defs>'
            '<path d="M24 2.6 42.4 13.2v21.6L24 45.4 5.6 34.8V13.2z" fill="#0f1620" stroke="url(#gcl)" stroke-width="2.1"/>'
            '<g fill="url(#gcl)" opacity=".92">'
            '<path d="M24 9.4a14.6 14.6 0 0 1 3.9.5l-.7 3.3a11.3 11.3 0 0 0-6.4 0l-.7-3.3a14.6 14.6 0 0 1 3.9-.5z"/>'
            '<path d="M33.6 13.7a14.6 14.6 0 0 1 2.9 2.7l-2.5 2.2a11.3 11.3 0 0 0-2.2-2.1z"/>'
            '<path d="M14.4 13.7l1.8 2.8a11.3 11.3 0 0 0-2.2 2.1l-2.5-2.2a14.6 14.6 0 0 1 2.9-2.7z"/>'
            '<path d="M38.6 24a14.6 14.6 0 0 1-.5 3.6l-3.3-.6a11.3 11.3 0 0 0 0-6l3.3-.6c.3 1.2.5 2.4.5 3.6z"/>'
            '<path d="M9.4 24c0-1.2.2-2.4.5-3.6l3.3.6a11.3 11.3 0 0 0 0 6l-3.3.6a14.6 14.6 0 0 1-.5-3.6z"/>'
            '<path d="M36.5 30.3l2.5 2.2a14.6 14.6 0 0 1-2.9 2.7l-1.8-2.8a11.3 11.3 0 0 0 2.2-2.1z"/>'
            '<path d="M11.5 30.3a11.3 11.3 0 0 0 2.2 2.1l-1.8 2.8a14.6 14.6 0 0 1-2.9-2.7z"/>'
            '<path d="M24 38.6c-1.3 0-2.6-.2-3.9-.5l.7-3.3a11.3 11.3 0 0 0 6.4 0l.7 3.3c-1.3.3-2.6.5-3.9.5z"/></g>'
            '<path d="M30.4 17.1a5.9 5.9 0 0 0-7.8 7.3l-6 6a2.3 2.3 0 1 0 3.3 3.3l6-6a5.9 5.9 0 0 0 7.3-7.8l-3 3-2.6-.7-.7-2.6z" fill="#fff"/>'
            '</svg>')


def whatsapp_url(text=""):
    base = "https://wa.me/%s" % SITE["whatsapp"]
    return base + ("?text=" + text.replace(" ", "%20")) if text else base


def footer():
    n = nav_structure()
    services = n["services"][:9]
    roadside = n["roadside"][:8]
    brands = n["brands"][:8]
    areas = n["locations"][:8]

    def col(title, items, urlfn):
        lis = "".join('<li><a href="%s">%s</a></li>' % (urlfn(i), esc(i["name"])) for i in items)
        return '<div class="footer-col"><h4>%s</h4><ul>%s</ul></div>' % (title, lis)

    social = "".join(
        '<a href="#" aria-label="%s" rel="noopener">%s</a>' % (name, icon(key))
        for name, key in [("Facebook", "facebook"), ("Instagram", "instagram"), ("YouTube", "youtube"), ("TikTok", "tiktok")]
    )

    return (
        '<footer class="site-footer"><div class="wrap">'
        '<div class="footer-grid">'
        '<div class="footer-col footer-about">'
        '<a class="brand" href="/"><span class="brand-mark">%s</span>'
        '<span class="brand-text"><span class="brand-name">Gear<em>Craft</em></span>'
        '<span class="brand-tag">%s</span></span></a>'
        '<p>An independent workshop in Al Quoz handling mechanical repair, diagnostics, air conditioning, '
        'brakes, tyres, bodywork and 24-hour roadside recovery for every make of car in Dubai.</p>'
        '<div class="footer-contact">'
        '<div>%s<span>%s<br>%s</span></div>'
        '<div>%s<span><a href="tel:%s">%s</a></span></div>'
        '<div>%s<span><a href="mailto:%s">%s</a></span></div>'
        '<div>%s<span>%s</span></div>'
        '</div>'
        '<div class="footer-contact" style="flex-direction:row;gap:10px;margin-top:6px">%s</div>'
        '</div>'
        '%s'
        '%s'
        '%s'
        '</div>'
        '<div class="footer-bottom">'
        '<span>&copy; <span data-year>2026</span> %s. All rights reserved. %s</span>'
        '<nav aria-label="Footer">'
        '<a href="/about/">About</a><a href="/reviews/">Reviews</a><a href="/faq/">FAQ</a>'
        '<a href="/contact/">Contact</a><a href="/blog/">Guides</a><a href="/sitemap.xml">Sitemap</a>'
        '</nav></div></div></footer>'
        % (logo_svg(), esc(SITE["tagline"]),
           icon("pin"), SITE["address_street"], SITE["address_city"],
           icon("phone"), SITE["tel"], SITE["phone_label"],
           icon("mail"), SITE["email"], SITE["email"],
           icon("clock"), esc(SITE["hours"]),
           social,
           col("Workshop services", services, lambda s: "/services/%s/" % s["slug"]),
           col("Roadside &amp; recovery", roadside, lambda s: "/roadside-assistance/%s/" % s["slug"]),
           col("Brands &amp; areas", brands + areas, lambda i: ("/car-brands/%s/" % i["slug"]) if i in brands else ("/areas-we-serve/%s/" % i["slug"])),
           SITE["brand"], SITE["license_note"])
    )


def floating():
    return (
        '<div class="float-actions">'
        '<a class="fa-btn fa-top" href="#top" aria-label="Back to top">%s</a>'
        '<a class="fa-btn fa-call" href="tel:%s" aria-label="Call the workshop"><span class="fa-tip">Call %s</span>%s</a>'
        '<a class="fa-btn fa-wa" href="%s" target="_blank" rel="noopener" aria-label="Message us on WhatsApp"><span class="fa-tip">WhatsApp us</span>%s</a>'
        '</div>' % (icon("chev"), SITE["tel"], SITE["phone_label"], icon("phone"), whatsapp_url(), icon("whatsapp"))
    )
