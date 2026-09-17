# -*- coding: utf-8 -*-
"""
Site-wide configuration + shared blocks.
All copy in this project is original, written for this build.
Contact details below are PLACEHOLDERS — swap them for your real numbers/address.
"""

SITE = {
    "brand": "GearCraft Auto Works",
    "brand_short": "GearCraft",
    "tagline": "Car Repair & 24/7 Roadside Assistance",
    "domain": "https://www.example-gearcraft.ae",
    # --- placeholders, change these ---
    "phone": "+971 50 000 0000",
    "phone_label": "+971 50 000 0000",
    "tel": "+971500000000",
    "whatsapp": "971500000000",
    "email": "workshop@gearcraft-auto.example",
    "address_street": "Warehouse 14, Street 8, Al Quoz Industrial Area 3",
    "address_city": "Dubai, United Arab Emirates",
    "address_full": "Warehouse 14, Street 8, Al Quoz Industrial Area 3, Dubai, UAE",
    "hours": "Saturday – Thursday: 8:00 AM – 10:00 PM · Friday: 8:00 AM – 12:00 PM & 2:00 PM – 10:00 PM",
    "hours_short": "Daily 8:00 AM – 10:00 PM",
    "roadside_hours": "Roadside & recovery crews: 24 hours, every day",
    "map_query": "Al Quoz Industrial Area 3, Dubai",
    "founded_year": 2006,
    "license_note": "RTA-approved workshop · Trade licence on display at reception",
}

STATS = [
    {"value": 19, "suffix": "+", "label": "Years in the trade"},
    {"value": 24500, "suffix": "+", "label": "Vehicles serviced"},
    {"value": 4.9, "suffix": "/5", "label": "Average customer rating", "decimals": 1},
    {"value": 32, "suffix": "", "label": "Technicians & support staff"},
]

PROCESS = [
    ("Book a slot that suits you", "Message us on WhatsApp, call the workshop, or use the estimate form. Tell us the car and the complaint — we will suggest a time that keeps you off the road for as little time as possible."),
    ("We inspect and diagnose", "Your car goes through a structured check: fault codes, visual inspection under the lift, fluids, brakes, tyres and a road test where relevant. Nothing is guessed at."),
    ("You approve a fixed quote", "You receive photos, an explanation in plain language and a written price for parts and labour. Work only starts after you say go — and the price does not move afterwards."),
    ("Repair, quality check, hand back", "Repairs are carried out to manufacturer tolerances, then re-tested. We finish with a wash-down and a summary of what was replaced, plus advice on what to watch next."),
]

TRUST_POINTS = [
    {"title": "Every make, one workshop",
     "text": "From a hard-working pickup to a low-mileage German saloon, we keep the tooling, software and parts sourcing for all the major marques sold in the UAE. No referrals, no second trips."},
    {"title": "Depth of service under one roof",
     "text": "Mechanical repair, gearbox work, AC, brakes, tyres, battery and electrical diagnostics, bodywork and paint, plus pre-purchase inspections — one job card, one accountable team."},
    {"title": "Straight answers, fixed pricing",
     "text": "You get a diagnosis you can understand and a quote you can hold us to. If a repair can wait, we will say so; if something is urgent, we will show you why."},
    {"title": "Gulf-ready maintenance",
     "text": "Heat, dust and stop-start traffic age components faster here than in milder climates. Our service intervals and part choices are adjusted for how cars are actually driven in Dubai."},
]

HOME_FAQ = [
    ("Which services does the workshop provide?",
     "Mechanical repair and servicing, engine and gearbox work, computer diagnostics, air conditioning, brakes, suspension and steering, batteries and auto electrics, tyres, body repair and painting, pre-purchase inspections, plus 24/7 roadside assistance and recovery across Dubai."),
    ("How do I book an appointment?",
     "Message us on WhatsApp, call the workshop number, or fill in the estimate form on any page and we will confirm a slot. Walk-ins are welcome during opening hours, although booked cars are always seen first."),
    ("Is roadside assistance really available around the clock?",
     "Yes. Recovery crews operate 24 hours a day, seven days a week, covering towing, jump-starts, flat tyres, fuel delivery, lockouts, winch recovery and accident recovery anywhere in Dubai."),
    ("Do you work on luxury, hybrid and electric cars?",
     "We do. Our technicians are trained on brand-specific diagnostic systems and high-voltage safety procedures, so European luxury cars, hybrids and EVs are handled by people who work on them regularly."),
    ("Can a mechanic come to my home or office?",
     "Yes — our mobile mechanic service covers many diagnostics, batteries, brakes, filters, tyres and minor repairs on site. Anything needing a lift or specialist equipment is collected and returned by recovery."),
    ("Will using an independent workshop affect my warranty?",
     "In most cases, no. Routine maintenance carried out to manufacturer specification with OEM-grade parts and documented properly does not by itself invalidate a new-car warranty in the UAE. We keep detailed service records for every visit."),
    ("How long does a typical job take?",
     "Servicing, brakes, batteries and tyres are usually same-day. Air conditioning repairs, gearbox work and diagnostics that depend on parts can take one to three days. We give you a realistic timeframe when you approve the quote."),
    ("Which areas of Dubai do you cover?",
     "Our workshop is in Al Quoz with easy access from Sheikh Zayed Road, and our mobile crews cover the whole emirate — Marina, JBR, Downtown, Business Bay, JVC, Motor City, Palm Jumeirah, Bluewaters, Nad Al Sheba, Mirdif, Deira and beyond."),
]

TESTIMONIALS = [
    {"name": "Rashid A.", "role": "Land Cruiser owner · Mirdif",
     "text": "My car had been to two other garages for a rough idle and nobody could pin it down. GearCraft found a cracked intake gasket in under an hour, quoted it honestly and had it fixed the same afternoon. The follow-up call two weeks later was a nice touch."},
    {"name": "Elena M.", "role": "Compact hatchback owner · Dubai Marina",
     "text": "My AC stopped cooling in July, which in Dubai is an emergency. They diagnosed a failed compressor, explained the options and the price difference, and did not push the most expensive one. Cabin is cold again and the bill matched the quote exactly."},
    {"name": "Daniel O.", "role": "German saloon owner · Downtown",
     "text": "I was worried about taking a European car to an independent workshop. They used the right diagnostic software, showed me the fault codes on screen and replaced only what was needed. Dealership-level work without the dealership wait."},
    {"name": "Fatima K.", "role": "Family SUV owner · JVC",
     "text": "Flat tyre on Sheikh Zayed Road at 11pm with two kids in the car. The recovery crew arrived in about 35 minutes, changed the wheel safely and stayed until we were moving. Calm, professional and genuinely kind."},
    {"name": "Imran S.", "role": "Delivery van fleet · Al Quoz",
     "text": "We keep six vans on the road and GearCraft handles the lot. Scheduled servicing, brake work, tyres, and they understand that a van off the road costs us money. Paperwork is clean and turnaround is dependable."},
    {"name": "Sophie B.", "role": "Convertible owner · Palm Jumeirah",
     "text": "Bought a used car and had them do a pre-purchase inspection first. They found previous accident repair that the seller had not mentioned, which saved me from a bad deal. Clear written report with photos."},
]

BRAND_LOGOS_TEXT = [
    "Toyota", "Nissan", "Mitsubishi", "Honda", "Mazda", "Suzuki", "Lexus",
    "BMW", "Mercedes-Benz", "Audi", "Volkswagen", "Porsche", "Land Rover",
    "Ford", "Chevrolet", "GMC", "Cadillac", "Renault", "Peugeot", "Fiat",
    "Hyundai", "Kia", "Geely", "Changan", "MG", "BYD", "Tesla",
]

WHY_DEALERSHIP = [
    ("Pricing you can plan around",
     "Independent workshops carry lower overheads than franchised dealers, so labour rates and parts margins are usually lower for the same specification of work. You see the price before we start, and it holds."),
    ("Shorter waiting times",
     "Dealer service departments often book days ahead. Because we hold common filters, pads, belts, batteries and fluids in stock, most routine work is finished the same day you bring the car in."),
    ("One team that knows your car",
     "Repeat customers get a service history with us — previous faults, parts replaced, upcoming maintenance. That context makes diagnosis faster and stops the same problem being sold to you twice."),
    ("Warranty-friendly documentation",
     "Every job is recorded with part numbers, oil specification and torque settings where relevant. If you ever need to prove maintenance was done properly, you have a paper trail to show."),
]

CTA_TEXT = {
    "title": "Book your car in today",
    "text": "Routine service, a warning light you would rather not ignore, an AC that has given up in the heat — whatever it is, we will tell you straight what the problem is and what it will cost. Message the workshop or call and speak to a technician, not a call centre.",
}
