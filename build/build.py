# -*- coding: utf-8 -*-
"""Static site generator: renders every page, plus sitemap.xml and robots.txt."""
import os
import sys
from datetime import date, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_site import SITE
from data_services import CORE_SERVICES, ROADSIDE_SERVICES
from data_catalog import BRAND_GROUPS, MARQUES, LOCATIONS, SENSORS, MODULES, POSTS

import pages
import templates

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = date.today().isoformat()


def write(rel_path, content):
    full = os.path.join(ROOT, rel_path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(content)
    return rel_path


URLS = [("/", "1.0", "daily")]


def add(url, prio="0.7", freq="monthly"):
    if (url, prio, freq) not in URLS:
        URLS.append((url, prio, freq))


def build():
    made = []

    # home
    made.append(write("/index.html", pages.home_page()))
    add("/", "1.0", "daily")

    # core services
    made.append(write("/services/index.html", pages.services_hub()))
    add("/services/", "0.9", "weekly")
    for s in CORE_SERVICES:
        p = "/services/%s/" % s["slug"]
        made.append(write(p + "index.html", templates.service_page(s, "service")))
        add(p, "0.8")

    # roadside
    made.append(write("/roadside-assistance/index.html", pages.roadside_hub()))
    add("/roadside-assistance/", "0.9", "weekly")
    for s in ROADSIDE_SERVICES:
        p = "/roadside-assistance/%s/" % s["slug"]
        made.append(write(p + "index.html", templates.service_page(s, "roadside")))
        add(p, "0.8")

    # brands + marques
    made.append(write("/car-brands/index.html", pages.brands_hub()))
    add("/car-brands/", "0.8", "weekly")
    for b in BRAND_GROUPS:
        p = "/car-brands/%s/" % b["slug"]
        made.append(write(p + "index.html", templates.brand_group_page(b)))
        add(p, "0.7")
    for m in MARQUES:
        p = "/car-brands/%s/" % m["slug"]
        made.append(write(p + "index.html", templates.marque_page(m)))
        add(p, "0.6")

    # locations
    made.append(write("/areas-we-serve/index.html", pages.areas_hub()))
    add("/areas-we-serve/", "0.7", "weekly")
    for l in LOCATIONS:
        p = "/areas-we-serve/%s/" % l["slug"]
        made.append(write(p + "index.html", templates.location_page(l)))
        add(p, "0.6")

    # sensors + modules
    made.append(write("/car-sensors/index.html", pages.sensors_hub()))
    add("/car-sensors/", "0.6")
    for s in SENSORS:
        if s["system"] == "hub":
            continue
        p = "/car-sensors/%s/" % s["slug"]
        made.append(write(p + "index.html", templates.sensor_page(s)))
        add(p, "0.5")
    made.append(write("/control-modules/index.html", pages.modules_hub()))
    add("/control-modules/", "0.6")
    for m in MODULES:
        if m["kind"] == "hub":
            continue
        p = "/control-modules/%s/" % m["slug"]
        made.append(write(p + "index.html", templates.module_page(m)))
        add(p, "0.5")

    # blog
    made.append(write("/blog/index.html", pages.blog_index()))
    add("/blog/", "0.7", "weekly")
    for p in POSTS:
        path = "/blog/%s/" % p["slug"]
        made.append(write(path + "index.html", templates.post_page(p)))
        add(path, "0.6")

    # static pages
    for path, fn, prio in [("/about/", pages.about_page, "0.7"),
                           ("/contact/", pages.contact_page, "0.8"),
                           ("/reviews/", pages.reviews_page, "0.6"),
                           ("/faq/", pages.faq_page, "0.7")]:
        made.append(write(path + "index.html", fn()))
        add(path, prio)

    # 404
    made.append(write("/404.html", pages.not_found()))

    # sitemap + robots
    write("/sitemap.xml", sitemap())
    write("/robots.txt", robots())
    write("/humans.txt", humans())

    return made


def sitemap():
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url, prio, freq in URLS:
        lines.append("  <url><loc>%s%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq><priority>%s</priority></url>"
                     % (SITE["domain"], url, TODAY, freq, prio))
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def robots():
    return ("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE["domain"])


def humans():
    return ("""%s — static website
---------------------------------
Built as a hand-written static site: no framework, no CMS, no third-party theme.

  * HTML rendered by a small Python generator (build/build.py)
  * One original stylesheet   -> assets/css/styles.css
  * One original script file  -> assets/js/main.js
  * Original artwork          -> assets/img (AI-generated for this project)

All written copy on this site was composed for this build.
Contact details in build/data_site.py are placeholders — replace before going live.

Generated: %s
""" % (SITE["brand"], datetime.now().strftime("%Y-%m-%d %H:%M")))


if __name__ == "__main__":
    files = build()
    total = sum(os.path.getsize(os.path.join(ROOT, f.lstrip("/"))) for f in files)
    print("Generated %d HTML pages (%.1f KB of HTML)" % (len(files), total / 1024))
    print("Plus sitemap.xml, robots.txt, humans.txt")
