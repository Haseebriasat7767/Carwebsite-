# GearCraft Auto Works — static website

A complete, dependency-free multi-page website for a Dubai car repair workshop and
24/7 roadside assistance business: **125 HTML pages**, one original stylesheet, one
original script file, and original artwork.

> **About the source brief.** The site was built to mirror the *structure* of an
> existing car-garage website — same page architecture, same service catalogue, same
> page types — but every word of copy, the visual design, the code and all imagery are
> original to this project. No text, photographs, logos or theme assets were copied
> from any third party, so there is nothing here that carries someone else's copyright.

---

## Run it locally

The site is plain static HTML — no build step is required to view it, but it must be
served over HTTP (paths are root-relative, e.g. `/assets/css/styles.css`).

```bash
cd Carwebsite-
python3 -m http.server 8000 --bind 0.0.0.0
# open http://localhost:8000
```

Any static host works too (Netlify, Vercel, GitHub Pages with a redirect rule for
`404.html`, nginx, Apache, S3 + CloudFront).

## Rebuild the site

Pages are generated from content data by a small Python generator. To change copy or
add a page, edit the data files and re-run the build:

```bash
python3 build/build.py
```

| File | What it holds |
|---|---|
| `build/data_site.py` | Brand, **contact details**, opening hours, stats, process steps, home FAQ, reviews |
| `build/data_services.py` | 21 workshop services + 15 roadside/recovery services (all copy) |
| `build/data_catalog.py` | 10 brand groups, 14 marque pages, 10 Dubai areas, 17 sensors, 16 control modules, 8 blog guides |
| `build/render.py` | Icons (inline SVG), logo, header/nav, footer, floating action buttons |
| `build/templates.py` | Page shell, hero, sections, cards, FAQ accordion, estimate form, schema.org JSON-LD |
| `build/pages.py` | Home page and all hub/static pages |
| `build/build.py` | Writes every page, plus `sitemap.xml`, `robots.txt`, `humans.txt` |

## Before going live — placeholders to replace

All contact details are **placeholders**. They live in one place: `build/data_site.py`.

```python
"phone":        "+971 50 000 0000",
"tel":          "+971500000000",     # used for tel: links
"whatsapp":     "971500000000",      # used for wa.me links (international format, no +)
"email":        "workshop@gearcraft-auto.example",
"address_street": "Warehouse 14, Street 8, Al Quoz Industrial Area 3",
"domain":       "https://www.example-gearcraft.ae",   # used for canonical URLs + sitemap
```

Then re-run `python3 build/build.py`. Also swap:

- `brand`, `brand_short`, `tagline`, `founded_year`, `license_note`
- The map links in `build/pages.py` (currently generic Google Maps searches for
  "Al Quoz Industrial Area 3, Dubai") — point them at your real listing, or drop in an
  embedded map iframe inside `.map-frame`.
- Social profile links in `footer()` inside `build/render.py` (currently `#`).

## Forms

There is no backend. Both forms (estimate + contact) compose the message in the
browser and hand it to **WhatsApp** (`wa.me`) or **email** (`mailto:`), so nothing is
silently dropped and no server is needed. To collect submissions server-side instead,
point the `submit` handlers in `assets/js/main.js` at your own endpoint or a service
such as Formspree.

## Page inventory

**Main pages** — home, services hub, roadside hub, car brands hub, sensors hub,
control modules hub, areas hub, blog index, about, contact, reviews, FAQ, 404.

**Workshop services (21)** — car repair Dubai, car garage Dubai, engine repair &
rebuild, AC repair & regas, gearbox/transmission, brakes, battery & charging, oil &
filters, scanning & diagnostics, tyres/balancing/alignment, wheel alignment, suspension
& steering, auto electrical, body repair & painting, mobile car mechanic, pre-purchase
inspection, minor service, major service, interval service plans, classic car
restoration, hybrid & EV service, detailing & paint protection.

**Roadside & recovery (15)** — towing, car recovery, flatbed recovery, breakdown repair,
battery jump start, battery boosting, flat tyre repair, mobile tyre replacement, fuel
delivery, lockout service, key recovery, winch service, basement pull-out, off-road
pull-out, accident recovery.

**Brands (24)** — Japanese, German, European, British, American, French, Italian,
Chinese, exotic & luxury, classic cars; plus marque pages for BMW, Mercedes-Benz, Audi,
Volkswagen, Porsche, Toyota, Nissan, Lexus, Land Rover & Range Rover, Ford, Chevrolet &
GMC, Hyundai & Kia, Jeep & Dodge, Volvo.

**Areas (10)** — Al Quoz, Dubai Marina & JBR, Downtown, Business Bay, JVC, Motor City,
Palm Jumeirah, Bluewaters Island, Nad Al Sheba & Meydan, JLT.

**Electronics (33)** — 17 sensor pages (ABS, TPMS, wheel speed, oxygen, crankshaft and
camshaft position, exhaust camshaft, oil pressure and level, fuel level and pressure,
temperature, washer fluid, rain, parking, intake manifold, GPS/IMU) and 16 control
module pages (ECM, PCM repair + programming, SCM, airbag, chassis, transfer case,
headlight, blind spot, spoiler, tailgate, immobiliser, MMI/infotainment, window switch,
fuse box, wiring harness).

**Guides (8)** — batteries in summer heat, AC faults, oil change intervals, dashboard
warning lights, buying a used car, tyre safety, brake noises, highway breakdown drill.

## Features

- Sticky header with mega-menu dropdowns, mobile drawer navigation, live "open now"
  indicator computed in Gulf Standard Time
- Service tab switcher, animated stat counters, auto-advancing review slider with
  dots/arrows, FAQ accordions, scroll-reveal animations (all honouring
  `prefers-reduced-motion`)
- Floating WhatsApp / call / back-to-top actions
- SEO: unique title + meta description per page, canonical URLs, Open Graph,
  `AutoRepair` / `BreadcrumbList` / `FAQPage` / `Article` JSON-LD, generated
  `sitemap.xml` and `robots.txt`
- Fully responsive down to 320px; no external CSS/JS frameworks; ~10 KB of JavaScript

## Images

`assets/img/*.jpg` were generated for this project (no stock or third-party photos).
`build/render.py` falls back to a contextually related image if a named file is
missing, so the build never produces broken images.
