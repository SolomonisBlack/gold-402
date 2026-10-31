#!/usr/bin/env python3
"""Build the Jewell Services static site into ./dist.

Usage:  python3 build.py
Output is plain HTML/CSS/JS/PHP that can be uploaded as-is to Hostinger (public_html).
Edit business details in BUSINESS below; edit page copy in the page functions.
"""
import html
import json
from urllib.parse import quote_plus
import os
import shutil
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).parent
SRC = ROOT / "src"
IMG = ROOT / "assets" / "img"
DIST = ROOT / "dist"

BUSINESS = {
    "name": "Jewell Services",
    "tagline": "We treat your home like jewels.",
    "phone_display": "515-451-9566",
    "phone_e164": "+15154519566",
    "email": "",  # set when known; shown on contact page and used in form fallback
    "facebook": "https://www.facebook.com/profile.php?id=61570843493368",
    "url": os.environ.get("SITE_URL", "https://jewell-services.com").rstrip("/"),
    "area": "All of Iowa",
}
HOURS = [  # (js day index, label, hours)
    (1, "Monday", "9:00 am – 5:00 pm"),
    (2, "Tuesday", "9:00 am – 5:00 pm"),
    (3, "Wednesday", "9:00 am – 5:00 pm"),
    (4, "Thursday", "9:00 am – 5:00 pm"),
    (5, "Friday", "9:00 am – 5:00 pm"),
    (6, "Saturday", "By appointment"),
    (0, "Sunday", "By appointment"),
]
# "fallback" = no server-side mail (static preview hosts); "php" = post to send.php (Hostinger)
FORM_MODE = os.environ.get("FORM_MODE", "php")
# STAGING=1 marks every page noindex (for preview/temporary domains)
STAGING = os.environ.get("STAGING") == "1"
SMS_BODY = "Hi Jewell Services! I'd like a free estimate. Here's a photo of the job:"

esc = html.escape

# ---------------------------------------------------------------- icons
_I = {
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "sms": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M8 9h8M8 13h5"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "check-circle": '<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "award": '<circle cx="12" cy="8" r="6"/><path d="M15.48 12.89 17 22l-5-3-5 3 1.52-9.11"/>',
    "tag": '<path d="M20.59 13.41 13.42 20.6a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><circle cx="7" cy="7" r="1.5"/>',
    "heart": '<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78L12 21.23l8.84-8.84a5.5 5.5 0 0 0 0-7.78z"/>',
    "home": '<path d="m3 10 9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/>',
    "tv": '<rect x="2" y="4" width="20" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>',
    "layers": '<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 17 10 5 10-5M2 12l10 5 10-5"/>',
    "hammer": '<path d="m15 12-8.5 8.5a2.12 2.12 0 0 1-3-3L12 9"/><path d="M17.64 15 22 10.64M20.91 11.7l-1.25-1.25c-.6-.6-.93-1.4-.93-2.25v-.86L16.01 4.6a5.56 5.56 0 0 0-3.94-1.64H9l.92.82A6.18 6.18 0 0 1 12 8.4v1.56l2 2h2.47l2.26 1.91"/>',
    "zap": '<path d="M13 2 3 14h9l-1 8 10-12h-9z"/>',
    "brush": '<path d="M18.37 2.63 14 7l-1.59-1.59a2 2 0 0 0-2.82 0L8 7l9 9 1.59-1.59a2 2 0 0 0 0-2.82L17 10l4.37-4.37a2.12 2.12 0 1 0-3-3z"/><path d="M9 8c-2 3-4 3.5-7 4l8 10c2-1 6-5 6-7"/>',
    "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94z"/>',
    "leaf": '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10z"/><path d="M2 21c0-3 1.85-5.36 5.08-6"/>',
    "snow": '<path d="M12 2v20M4.93 4.93l14.14 14.14M2 12h20M4.93 19.07 19.07 4.93"/>',
    "truck": '<path d="M10 17h4V5H2v12h3"/><path d="M20 17h2v-3.34a4 4 0 0 0-1.17-2.83L19 9h-5v8h1"/><circle cx="7.5" cy="17.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/>',
    "camera": '<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>',
    "door": '<path d="M13 4h3a2 2 0 0 1 2 2v14M2 20h3M13 20h9M10 12v.01"/><path d="M13 4.56v16.18a.5.5 0 0 1-.65.48L5 19V5.79a2 2 0 0 1 1.51-1.94l4-1A2 2 0 0 1 13 4.56z"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
    "building": '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M16 6h.01M12 6h.01M12 10h.01M12 14h.01M16 10h.01M16 14h.01M8 10h.01M8 14h.01"/>',
    "arrow": '<path d="M5 12h14M12 5l7 7-7 7"/>',
    "chev": '<path d="m6 9 6 6 6-6"/>',
    "facebook": '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
    "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    "clipboard": '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1"/><path d="m9 14 2 2 4-4"/>',
    "gem": '<path d="M6 3h12l4 6-10 13L2 9z"/><path d="M11 3 8 9l4 13 4-13-3-6M2 9h20"/>',
    "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "image": '<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.09-3.09a2 2 0 0 0-2.82 0L6 21"/>',
    "msg": '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22z"/>',
    "school": '<path d="m4 6 8-4 8 4M18 10l4 2v8a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-8l4-2"/><path d="M14 22v-4a2 2 0 0 0-4 0v4M18 5v17M6 5v17"/><circle cx="12" cy="9" r="2"/>',
    "dumbbell": '<path d="M14.4 14.4 9.6 9.6M18.66 21.51a2 2 0 1 1-2.83-2.82l-1.77 1.77a2 2 0 1 1-2.83-2.83l6.37-6.36a2 2 0 1 1 2.83 2.83l-1.77 1.77a2 2 0 1 1 2.83 2.83zM21.5 21.5l-1.4-1.4M3.9 3.9 2.5 2.5M6.4 12.77a2 2 0 1 1-2.83-2.83l1.77-1.76a2 2 0 1 1-2.83-2.83l2.83-2.83a2 2 0 1 1 2.83 2.83l1.76-1.77a2 2 0 1 1 2.83 2.83z"/>',
    "baby": '<path d="M9 12h.01M15 12h.01M10 16c.5.3 1.2.5 2 .5s1.5-.2 2-.5"/><path d="M19 6.3a9 9 0 0 1 1.8 3.9 2 2 0 0 1 0 3.6 9 9 0 0 1-17.6 0 2 2 0 0 1 0-3.6A9 9 0 0 1 12 3c2 0 3.5 1.1 3.5 2.5s-.9 2.5-2 2.5c-.8 0-1.5-.4-1.5-1"/>',
    "briefcase": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
    "dollar": '<path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
    "sparkle": '<path d="m12 3-1.9 5.8a2 2 0 0 1-1.3 1.3L3 12l5.8 1.9a2 2 0 0 1 1.3 1.3L12 21l1.9-5.8a2 2 0 0 1 1.3-1.3L21 12l-5.8-1.9a2 2 0 0 1-1.3-1.3z"/>',
    "star": '<path d="m12 2 3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01z"/>',
}


def ic(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{_I[name]}</svg>')


# ---------------------------------------------------------------- images
_dims = {}
USED_IMAGES = set()


def _variants(key):
    """Ensure jpg/webp + -sm variants exist for assets/img/<key>.jpg. Returns (w,h) of full size."""
    if key in _dims:
        return _dims[key]
    src = IMG / f"{key}.jpg"
    im = Image.open(src)
    if im.width > 1400:
        im = im.convert("RGB")
        im.thumbnail((1400, 1400), Image.LANCZOS)
        im.save(src, quality=80, optimize=True, progressive=True)
    full = Image.open(src).convert("RGB")
    for path, wmax, fmt in [(IMG / f"{key}.webp", None, "webp"), (IMG / f"{key}-sm.jpg", 640, "jpg"), (IMG / f"{key}-sm.webp", 640, "webp")]:
        if not path.exists():
            j = full.copy()
            if wmax:
                j.thumbnail((wmax, wmax), Image.LANCZOS)
            if fmt == "webp":
                j.save(path, quality=70, method=6)
            else:
                j.save(path, quality=80, optimize=True, progressive=True)
    _dims[key] = full.size
    return full.size


def sms_link(body=SMS_BODY):
    from urllib.parse import quote
    return f'sms:{BUSINESS["phone_e164"]}?&body={quote(body)}'


def pic(key, alt, P, cls="", eager=False, sizes="(max-width: 700px) 100vw, 50vw"):
    w, h = _variants(key)
    sw = Image.open(IMG / f"{key}-sm.jpg").width
    base = f"{P}assets/img/{key}"
    USED_IMAGES.add(key)
    load = {"high": 'fetchpriority="high"', True: 'decoding="async"'}.get(eager, 'loading="lazy" decoding="async"')
    c = f' class="{cls}"' if cls else ""
    return (f'<picture><source type="image/webp" srcset="{base}-sm.webp {sw}w, {base}.webp {w}w" sizes="{sizes}">'
            f'<img{c} src="{base}.jpg" srcset="{base}-sm.jpg {sw}w, {base}.jpg {w}w" sizes="{sizes}" '
            f'width="{w}" height="{h}" alt="{esc(alt)}" {load}></picture>')


# ---------------------------------------------------------------- content
SERVICES = [
    {
        "slug": "tv-mounting-smart-home",
        "desc": 'TV mounting, picture hanging, security cameras, and video doorbells installed level, secure, and tested. Free estimates across Iowa.',
        "name": "TV Mounting & Smart Home",
        "nav": "TVs, art, security cameras & video doorbells",
        "icon": "tv",
        "card": "work/tv-fireplace-wall",
        "hero": "work/tv-fireplace-wall",
        "cta": "Get a free TV mounting quote",
        "title": 'TV Mounting & Camera Installation in Iowa',
        "h1": "TV mounting, cameras & video doorbells, done right",
        "intro": "Get your TV on the wall, your art hung straight, and your home watched over. We mount TVs professionally anywhere you like, then level, secure, and test everything before we leave.",
        "card_text": "TVs mounted level and secure anywhere you like, plus pictures, art, cameras, and video doorbells.",
        "items": [
            ("TV mounting", "Any room, any wall: living rooms, bedrooms, over the fireplace. We find the studs, level it, and leave the cords neat."),
            ("Pictures, mirrors & art", "Gallery walls, heavy mirrors, and artwork hung straight, at the right height, with the right hardware."),
            ("Security camera installation", "Indoor or outdoor cameras placed for real coverage of entries, driveways, and yards."),
            ("Video doorbell installation", "See who's at the door from your phone. We install, connect, and test it with you."),
        ],
        "photos": [("work/tv-fireplace-wall", "TV mounted above an electric fireplace"), ("work/owner-tv-mount", "Bedroom TV mounted and leveled"), ("stock/security-camera", "Outdoor security camera")],
        "options": ["TV Mounting", "Camera Installation", "Doorbell Installation"],
        "faqs": [
            ("Can you mount a TV above a fireplace?", "Yes. We mount TVs anywhere you like, including above fireplaces, and we'll talk through viewing height and wall type before we start."),
            ("Do I need to buy the mount?", "You can supply your own mount or ask us what fits your TV and wall. Tell us your TV size when you request an estimate."),
        ],
    },
    {
        "slug": "flooring",
        "desc": 'Luxury vinyl plank and tile flooring installed with care, from basements to kitchens. Licensed, insured, 1-year warranty. Free estimates.',
        "name": "Tile & LVP Flooring",
        "nav": "Luxury vinyl plank, tile & floor prep",
        "icon": "layers",
        "card": "work/lvp-flooring",
        "hero": "work/lvp-flooring",
        "cta": "Get a free flooring quote",
        "title": 'LVP & Tile Flooring Installation in Iowa',
        "h1": "Tile & luxury vinyl plank flooring installed with care",
        "intro": "We install many kinds of flooring, and luxury vinyl plank (LVP) is our most popular. It's durable, water-resistant, and looks great in kitchens, basements, and busy family rooms.",
        "card_text": "Durable, beautiful floors. LVP is our most popular install, and we do tile too.",
        "items": [
            ("Luxury vinyl plank (LVP)", "Water-resistant and kid- and pet-friendly, with a wood look at a friendlier price. Our most requested floor."),
            ("Tile flooring", "Bathrooms, entryways, laundry rooms, and kitchens, laid flat and finished clean."),
            ("Floor prep & sanding", "A good floor starts underneath. We prep and sand so your new floor goes down right."),
            ("Basements & gym floors", "From finished basements to home gyms, we cover the space you actually use."),
        ],
        "photos": [("work/lvp-flooring", "Gray LVP flooring install"), ("work/floor-sanding", "Hardwood floor sanding"), ("work/home-gym", "Home gym flooring and equipment")],
        "options": ["Tile/LVP Flooring"],
        "faqs": [
            ("How long does an LVP install take?", "It depends on the size of the room and the condition of the subfloor. We'll give you a clear timeline with your free estimate."),
            ("Can you install flooring in a basement?", "Yes. LVP is a great choice for basements because it handles moisture better than many other floors."),
        ],
    },
    {
        "slug": "kitchen-bathroom-remodeling",
        "desc": 'Kitchen and bathroom remodels, from a quick refresh to a full renovation. Family-owned, licensed and insured. Free estimates across Iowa.',
        "name": "Kitchen & Bath Remodeling",
        "nav": "Refreshes to full renovations",
        "icon": "home",
        "card": "stock/kitchen-remodel",
        "hero": "stock/kitchen-remodel",
        "cta": "Plan your remodel with a free estimate",
        "title": 'Kitchen & Bathroom Remodeling in Iowa',
        "h1": "Kitchen & bathroom remodels with a personal touch",
        "intro": "From a minor refresh to a major renovation, we help you upgrade the rooms you use most, with clear communication from the first walkthrough to the final wipe-down.",
        "card_text": "Kitchen and bathroom upgrades, from a quick refresh to a full renovation.",
        "items": [
            ("Kitchen remodels", "New layouts, cabinets, backsplash, lighting, and flooring, or just a refresh that makes it feel new."),
            ("Bathroom remodels", "Upgrade your personal space with tile, vanities, fixtures, and finishes you'll love."),
            ("Framing & build-outs", "Walls, rooms, and basement build-outs framed square and ready to finish."),
            ("Finishing touches", "Paint, trim, caulking, and hardware so the whole room looks complete."),
        ],
        "photos": [("work/basement-framing", "Basement wall framing"), ("stock/kitchen-remodel", "Bright modern kitchen"), ("stock/bathroom-remodel", "Modern tiled bathroom")],
        "options": ["Kitchen Remodel", "Bathroom Remodel"],
        "faqs": [
            ("Do you do small updates or only full remodels?", "Both. Plenty of clients start with a refresh: new fixtures, paint, flooring, or a backsplash."),
            ("Will you help me plan the project?", "Yes. Your free estimate includes a walkthrough where we talk through what you want, your budget, and your timeline."),
        ],
    },
    {
        "slug": "electrical",
        "desc": 'Everyday electrical repairs, light fixture upgrades, and ceiling fan installation across Iowa. Free estimates from Jewell Services.',
        "name": "Electrical Services",
        "nav": "Repairs, light fixtures & ceiling fans",
        "icon": "zap",
        "card": "work/electrical-panel",
        "hero": "stock/electrical-fixture",
        "cta": "Get a free electrical quote",
        "title": 'Light Fixtures, Ceiling Fans & Electrical Repairs',
        "h1": "Electrical repairs, light fixtures & ceiling fans",
        "intro": "Flickering lights, dated fixtures, a room that needs a fan. We handle everyday electrical repairs, light fixture upgrades, and ceiling fan installs carefully and cleanly.",
        "card_text": "Electrical repairs, light fixture upgrades, and ceiling fan installation.",
        "items": [
            ("Electrical repairs", "Troubleshooting and fixing the things that aren't working the way they should."),
            ("Light fixture upgrades", "Swap dated fixtures for modern lighting inside and out."),
            ("Ceiling fan installation", "New fans or replacements, balanced and wobble-free."),
            ("Upgrades for your project", "Electrical pieces of a bigger job, like a new TV wall, updated lighting, or a remodel."),
        ],
        "photos": [("work/electrical-panel", "Electrical panel work"), ("stock/electrical-fixture", "Pendant light installation")],
        "options": ["Electrical Services"],
        "faqs": [
            ("What kinds of electrical work do you do?", "Everyday repairs and upgrades: light fixtures, ceiling fans, and fixing things that aren't working right. Tell us about your project and we'll let you know if it's a fit."),
            ("Can you replace a light with a ceiling fan?", "In many cases, yes. We'll check the existing box and wiring and let you know what's needed."),
        ],
    },
    {
        "slug": "painting-drywall",
        "desc": 'Interior and exterior painting plus drywall repair and installation, with careful prep and clean lines. Free estimates across Iowa.',
        "name": "Painting & Drywall",
        "nav": "Interior & exterior painting, drywall repair",
        "icon": "brush",
        "card": "stock/painting",
        "hero": "stock/painting",
        "cta": "Get a free painting or drywall quote",
        "title": 'Painting & Drywall Repair in Iowa',
        "h1": "Interior & exterior painting and drywall repair, done clean",
        "intro": "Fresh paint and smooth walls change how a home feels. We do interior and exterior painting, plus drywall work from minor patching to new installation.",
        "card_text": "Interior and exterior painting, plus drywall from small patches to new installs.",
        "items": [
            ("Interior painting", "Walls, ceilings, trim, and doors, with clean lines and careful prep."),
            ("Exterior painting", "Protect and refresh siding, trim, doors, and more."),
            ("Drywall repair", "Holes, cracks, water damage, and dents patched so they disappear."),
            ("New drywall installation", "Hang, tape, mud, and finish for basements, additions, and remodels."),
        ],
        "photos": [("stock/painting", "Interior wall painting"), ("stock/drywall", "Drywall finishing")],
        "options": ["Custom Painting", "Drywall Repair"],
        "faqs": [
            ("Do you move furniture and protect floors?", "We protect floors and nearby surfaces and work carefully around your belongings. Let us know about anything fragile ahead of time."),
            ("Can you match my existing paint?", "Usually, yes. If you have the paint name or a can, that helps. If not, we can match it from a sample."),
        ],
    },
    {
        "slug": "exterior",
        "desc": 'Siding, window, door, deck, and fence repair and replacement to protect your Iowa home. Licensed and insured. Free estimates.',
        "name": "Siding, Windows, Doors & Decks",
        "nav": "Siding, windows, doors, decks & fences",
        "icon": "door",
        "card": "work/siding-repair",
        "hero": "work/siding-repair",
        "cta": "Get a free exterior repair quote",
        "title": 'Siding, Windows, Doors, Decks & Fences in Iowa',
        "h1": "Exterior repairs that protect your home",
        "intro": "Iowa weather is tough on a house. We repair and replace siding, windows, doors, decks, and fences, so your home stays protected, efficient, and good-looking.",
        "card_text": "Siding, windows, doors, decks, and fences, repaired or replaced.",
        "items": [
            ("Siding", "Damaged or loose siding repaired or replaced to keep weather out."),
            ("Windows", "Repair, replacement, and energy-efficient upgrades."),
            ("Doors", "Entry, storm, and interior doors repaired, replaced, or installed."),
            ("Decks & fencing", "Broken deck boards and faded color fixed. Sagging fences and broken gates repaired."),
        ],
        "photos": [("work/siding-repair", "Siding repair"), ("stock/deck", "Wood deck"), ("stock/fence", "Wood privacy fence")],
        "options": ["Siding", "Windows/Doors", "Deck/Fencing"],
        "faqs": [
            ("Can you fix just a few damaged siding pieces?", "Yes. We handle small repairs as well as larger replacements."),
            ("Do you replace windows for better energy efficiency?", "Yes. We do window repair, replacement, and upgrades for energy efficiency."),
        ],
    },
    {
        "slug": "home-repairs-assembly",
        "desc": 'Hand us your to-do list: household repairs, gutter cleaning, and furniture, grill, and bike assembly. Free estimates across Iowa.',
        "name": "Home Repairs & Assembly",
        "nav": "To-do lists, gutters & furniture assembly",
        "icon": "wrench",
        "card": "stock/assembly",
        "hero": "stock/assembly",
        "cta": "Send us your to-do list",
        "title": 'Handyman Repairs & Furniture Assembly in Iowa',
        "h1": "Knock out your whole to-do list in one visit",
        "intro": "That list on the fridge? Hand it to us. From small repairs and gutter cleaning to assembling furniture, bikes, grills, and cabinets, we get it done so you get your weekend back.",
        "card_text": "Your whole to-do list in one visit, from gutters and repairs to assembly.",
        "items": [
            ("Household repairs & to-do lists", "Small fixes and odd jobs bundled into one visit."),
            ("Gutter cleaning", "Keep water flowing away from your home."),
            ("Sanding & upgrades", "Smooth out, touch up, and upgrade the little things that add up."),
            ("Assembly", "Furniture, bikes, cabinets, grills, and home gym equipment, built right."),
        ],
        "photos": [("work/home-gym", "Home gym equipment assembly"), ("stock/assembly", "Furniture assembly")],
        "options": ["Household Repairs / To-Do List", "Assembly"],
        "faqs": [
            ("Is my job too small?", "No. Small jobs are what a handyman is for. Bundle a few into one visit to make the most of it."),
            ("Can you assemble things I bought online?", "Yes. Furniture, bikes, grills, cabinets, and more."),
        ],
    },
    {
        "slug": "lawn-snow-hauling",
        "desc": 'Snow removal, lawn care, junk removal, and moving help from a family-owned Iowa team. Call or text for a free estimate.',
        "name": "Lawn, Snow & Hauling",
        "nav": "Snow removal, lawn care, junk removal & moving",
        "icon": "truck",
        "card": "work/trailer-hauling",
        "hero": "stock/snow-removal",
        "cta": "Get a free lawn, snow, or hauling quote",
        "title": 'Snow Removal, Lawn Care & Junk Hauling in Iowa',
        "h1": "Snow removal, lawn care & hauling, all year long",
        "intro": "Iowa seasons keep you busy. We handle snow removal in winter, lawn care in summer, and junk removal and moving help whenever you need it.",
        "card_text": "Snow removal, lawn care, junk removal, and moving help.",
        "items": [
            ("Snow removal", "Driveways and walkways cleared so you can get where you need to go."),
            ("Lawn care", "Mowing and yard upkeep to keep your property looking sharp."),
            ("Junk removal", "Old furniture, debris, and clutter hauled away."),
            ("Moving & hauling", "Extra hands and a trailer for moves, deliveries, and big items."),
        ],
        "photos": [("work/trailer-hauling", "Hauling with our trailer"), ("work/storm-cleanup", "Storm cleanup job"), ("stock/snow-removal", "Snow removal")],
        "options": ["Snow Removal", "Lawn Care", "Junk Removal", "Moving/Hauling"],
        "faqs": [
            ("Do you offer recurring snow removal or lawn care?", "Ask us about recurring service when you request your estimate, and we'll set up what works for your property."),
            ("What kind of junk do you haul?", "Furniture, yard debris, and general clutter. Tell us what you have and we'll let you know."),
        ],
    },
]

ALL_OPTIONS = [(s["name"], s["options"]) for s in SERVICES] + [("Commercial", ["Commercial / Building Maintenance"])]

COMMERCIAL_ITEMS = [
    ("Move-out cleanings", "Get units and spaces ready for the next tenant."),
    ("AC coil cleaning & filter replacement", "Keep systems efficient and air quality healthy."),
    ("Auto flush valve repair & replacement", "Restroom fixtures repaired or replaced so they keep working."),
    ("Exhaust vent piping & fan motor cleaning", "Clean, quiet, properly working ventilation."),
    ("Bathroom caulking", "Fresh, watertight seals that look clean."),
    ("General repairs", "Doors, drywall, paint, fixtures, and the punch list that never ends."),
]
SECTORS = [("school", "Schools"), ("dumbbell", "Gyms"), ("baby", "Daycares"), ("briefcase", "Offices")]

GENERAL_FAQS = [
    ("Do you offer free estimates?", "Yes, every estimate is free. Call or text 515-451-9566, or fill out the form, and we'll get back to you during business hours."),
    ("Are you licensed and insured?", "Yes. Jewell Services is licensed and insured, so your home and your project are protected."),
    ("Do you guarantee your work?", "Yes. Our work comes with a 1-year warranty. If something we did isn't right, we'll come back and make it right."),
    ("Do you price match?", "Yes. If you have a comparable written quote from another company, let us know and we'll match it."),
    ("What areas do you serve?", "We serve all of Iowa. Tell us your ZIP code when you reach out and we'll confirm scheduling for your area."),
    ("What are your hours?", "Monday through Friday, 9 am to 5 pm. Saturdays and Sundays are available by appointment."),
    ("Do you offer any discounts?", "Yes. Single mothers get 10% off any service. Just mention it when you request your estimate."),
    ("Do you work with businesses?", "Yes. We provide building and property maintenance for schools, gyms, daycares, and offices, with discounted weekly and monthly plans."),
]

CITIES_CENTRAL = ["Des Moines", "West Des Moines", "Ankeny", "Urbandale", "Johnston", "Waukee", "Clive", "Altoona", "Grimes", "Pleasant Hill", "Norwalk", "Indianola", "Ames", "Newton"]
CITIES_STATE = ["Cedar Rapids", "Iowa City", "Davenport", "Waterloo", "Cedar Falls", "Sioux City", "Council Bluffs", "Dubuque", "Mason City", "Fort Dodge", "Marshalltown", "Ottumwa"]

GALLERY = [
    ("work/tv-fireplace-wall", "TV mounted over an electric fireplace"),
    ("work/lvp-flooring", "New LVP flooring"),
    ("work/siding-repair", "Siding repair"),
    ("work/basement-framing", "Basement wall framing"),
    ("work/owner-tv-mount", "Bedroom TV mounted and leveled"),
    ("work/home-gym", "Home gym flooring and equipment"),
    ("work/electrical-panel", "Electrical panel work"),
    ("work/floor-sanding", "Hardwood floor sanding"),
    ("work/landscape-bed", "Raised garden bed build"),
    ("work/trailer-hauling", "Hauling with our trailer"),
    ("work/storm-cleanup", "Storm cleanup job"),
]

# ---------------------------------------------------------------- layout


def rel(depth):
    return "../" * depth if depth else "./"


def nav_html(P, current):
    def a(path, label):
        cur = ' aria-current="page"' if current == path else ""
        return f'<a href="{P}{path}"{cur}>{label}</a>'
    menu = "".join(
        f'<a href="{P}services/{s["slug"]}/"{" aria-current=\"page\"" if current == "services/" + s["slug"] + "/" else ""}><span class="menu__ic">{ic(s["icon"])}</span><span><strong>{esc(s["name"])}</strong>{esc(s["nav"])}</span></a>'
        for s in SERVICES)
    svc_cur = ' style="box-shadow:inset 0 -2px 0 var(--green)"' if current.startswith("services") else ""
    return f'''<nav class="nav" id="site-nav" aria-label="Main">
<ul>
<li class="has-menu"><button class="nav__drop" aria-expanded="false" aria-controls="svc-menu"{svc_cur}>Services {ic("chev")}</button>
<div class="menu" id="svc-menu">{menu}<a class="menu__all" href="{P}services/">View all services {ic("arrow")}</a></div></li>
<li>{a("commercial/", "Commercial")}</li>
<li>{a("projects/", "Our Work")}</li>
<li>{a("about/", "About")}</li>
<li>{a("service-area/", "Service Area")}</li>
<li>{a("contact/", "Contact")}</li>
</ul>
<div class="nav__mobile-cta">
<a class="btn btn--lg" href="{P}contact/">{ic("clipboard")} Get a Free Estimate</a>
<a class="btn btn--ghost btn--lg" href="tel:{BUSINESS["phone_e164"]}">{ic("phone")} Call {BUSINESS["phone_display"]}</a>
<a class="btn btn--ghost btn--lg" href="{sms_link()}">{ic("sms")} Text us a photo</a>
</div>
</nav>'''


def header_html(P, current):
    b = BUSINESS
    return f'''<a class="skip" href="#main">Skip to content</a>
<aside class="topbar" aria-label="Contact information"><div class="wrap">
<div class="topbar__items"><span>{ic("pin")} Serving all of Iowa</span><span class="topbar__hide">{ic("shield")} Licensed &amp; insured</span><span class="topbar__hide">{ic("award")} 1-year warranty</span></div>
<div class="topbar__items"><span class="topbar__hide">{ic("clock")} Mon–Fri 9–5 · Weekends by appt.</span><a href="tel:{b["phone_e164"]}">{ic("phone")} {b["phone_display"]}</a></div>
</div></aside>
<header class="header"><div class="wrap">
<a class="brand" href="{P}" aria-label="Jewell Services home"><picture><source type="image/webp" srcset="{P}assets/img/brand/logo-sm.webp"><img src="{P}assets/img/brand/logo-sm.png" width="300" height="233" alt="Jewell Services"></picture></a>
<button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="site-nav"><span></span></button>
{nav_html(P, current)}
<div class="header__cta">
<a class="header__phone" href="tel:{b["phone_e164"]}"><small>Call or text</small><strong>{b["phone_display"]}</strong></a>
<a class="btn" href="{P}contact/">Free Estimate</a>
</div>
</div></header>'''


def hours_rows():
    return "".join(f'<tr data-day="{d}"><td>{n}</td><td>{h}</td></tr>' for d, n, h in HOURS)


def footer_html(P, current=""):
    b = BUSINESS
    svc = "".join(f'<li><a href="{P}services/{s["slug"]}/">{esc(s["name"])}</a></li>' for s in SERVICES)
    return f'''<footer class="footer"><div class="wrap">
<div class="footer__grid">
<div>
<a class="footer__logo" href="{P}"><picture><source type="image/webp" srcset="{P}assets/img/brand/logo-sm.webp"><img src="{P}assets/img/brand/logo-sm.png" width="300" height="233" alt="Jewell Services" loading="lazy"></picture></a>
<p>Family-owned, Black-owned, and locally operated home repair and remodeling, serving all of Iowa.</p>
<a class="footer__phone" href="tel:{b["phone_e164"]}">{b["phone_display"]}</a>
<div class="social"><a href="{b["facebook"]}" target="_blank" rel="noopener" aria-label="Jewell Services on Facebook">{ic("facebook")}</a><a href="{sms_link()}" aria-label="Text Jewell Services">{ic("sms")}</a></div>
</div>
<div><h2>Services</h2><ul>{svc}<li><a href="{P}commercial/">Commercial maintenance</a></li></ul></div>
<div><h2>Company</h2><ul>
<li><a href="{P}about/">About us</a></li><li><a href="{P}projects/">Our work</a></li><li><a href="{P}service-area/">Service area</a></li><li><a href="{P}contact/">Free estimate</a></li><li><a href="{P}privacy/">Privacy policy</a></li></ul></div>
<div><h2>Hours</h2><table class="hours"><tbody>{hours_rows()}</tbody></table>
<p style="margin-top:16px">{ic("pin", "")} Serving all of Iowa</p></div>
</div>
<div class="footer__bottom"><span>© <span data-year>2026</span> Jewell Services. All rights reserved.</span><span>Licensed &amp; insured · 1-year warranty · Price match</span></div>
</div></footer>
{mbar(P, current)}'''


def mbar(P, current):
    b = BUSINESS
    if current in ("contact/", "thank-you/"):
        return (f'<nav class="mbar mbar--2" aria-label="Quick contact"><a class="mbar__main" href="tel:{b["phone_e164"]}">{ic("phone")} Call</a>'
                f'<a href="{sms_link()}">{ic("sms")}Text a photo</a></nav>')
    return (f'<nav class="mbar" aria-label="Quick contact"><a href="tel:{b["phone_e164"]}">{ic("phone")}Call</a>'
            f'<a href="{sms_link()}">{ic("sms")}Text</a>'
            f'<a class="mbar__main" href="{P}contact/">{ic("clipboard")}<span><span class="long">Free </span>Estimate</span></a></nav>')


def schema_business(P_abs):
    b = BUSINESS
    days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"}
    return {
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "@id": b["url"] + "/#business",
        "name": b["name"],
        "slogan": b["tagline"],
        "url": b["url"] + "/",
        "telephone": b["phone_e164"],
        "logo": b["url"] + "/assets/img/brand/logo.png",
        "image": [b["url"] + "/assets/img/work/team-family.jpg", b["url"] + "/assets/img/work/owner-tv-mount.jpg"],
        "areaServed": {"@type": "State", "name": "Iowa"},
        "sameAs": [b["facebook"]],
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": list(days.values()), "opens": "09:00", "closes": "17:00"}],
        "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"], "url": f'{b["url"]}/services/{s["slug"]}/'}} for s in SERVICES],
    }


def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


def crumbs_schema(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": BUSINESS["url"] + "/" + p} for i, (n, p) in enumerate(trail)]}


def page(path, title, desc, body, current="", schemas=(), og_img="brand/og-image.jpg", noindex=False, root_abs=False):
    depth = path.count("/") if path else 0
    P = "/" if root_abs else rel(depth)
    url = BUSINESS["url"] + "/" + path
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    robots = '<meta name="robots" content="noindex">' if (noindex or STAGING) else ""
    cfg = json.dumps({"phoneE164": BUSINESS["phone_e164"], "phoneDisplay": BUSINESS["phone_display"], "email": BUSINESS["email"], "formMode": FORM_MODE})
    full_title = title if "Jewell" in title else f"{title} | Jewell Services"
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc)}">
{robots}<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0d1b2a">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Jewell Services">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BUSINESS["url"]}/assets/img/{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="32x32" href="{P}assets/img/brand/favicon-32.png">
<link rel="apple-touch-icon" href="{P}assets/img/brand/apple-touch-icon.png">
<link rel="manifest" href="{P}site.webmanifest">
<link rel="preload" href="{P}assets/fonts/bricolage-grotesque.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{P}assets/fonts/figtree.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{P}assets/css/site.css?v={VERSION}">
<script>window.JEWELL={cfg};document.documentElement.classList.add("js")</script>
{ld}
</head>
<body>
{header_html(P, current)}
<main id="main">
{body(P)}
</main>
{footer_html(P, current)}
<script src="{P}assets/js/site.js?v={VERSION}" defer></script>
</body>
</html>
'''
    out = DIST / path / "index.html" if (path == "" or path.endswith("/")) else DIST / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")
    PAGES.append((path, noindex))


PAGES = []
import hashlib
VERSION = hashlib.md5((SRC / "assets/css/site.css").read_bytes() + (SRC / "assets/js/site.js").read_bytes()).hexdigest()[:8]

# ---------------------------------------------------------------- components


def service_select(selected=None, required=True, id_="service"):
    opts = ['<option value="">Choose a service…</option>']
    for group, items in ALL_OPTIONS:
        o = "".join(f'<option{" selected" if v == selected else ""}>{esc(v)}</option>' for v in items)
        opts.append(f'<optgroup label="{esc(group)}">{o}</optgroup>')
    opts.append('<option>Something else / not sure</option>')
    req = " required" if required else ""
    return f'<select id="{id_}" name="service"{req}>{"".join(opts)}</select>'


def hidden_fields(P, page_name):
    return (f'<input type="hidden" name="page" value="{esc(page_name)}">'
            f'<input type="hidden" name="elapsed" value="">'
            f'<div class="hp" aria-hidden="true"><label>Leave this empty<input type="text" name="hp_x7" tabindex="-1" autocomplete="new-password"></label></div>')


def NOTES(fid):
    return field(fid, "message", "Anything we should know?", '<textarea {id} name="message" rows="3" style="min-height:84px"></textarea>', full=True, opt=True)


CONSENT = '<p class="consent">By sending, you agree Jewell Services may call or text you about your request.</p>'


def field(fid, name, label, inp, err=None, full=False, opt=False):
    o = ' <span class="opt">(optional)</span>' if opt else ""
    e = f'<span class="err" id="{fid}-{name}-err">{err}</span>' if err else ""
    d = f' aria-describedby="{fid}-{name}-err"' if err else ""
    inp = inp.replace("{id}", f'id="{fid}-{name}"{d}')
    return f'<div class="field{" full" if full else ""}"><label for="{fid}-{name}">{label}{o}</label>{inp}{e}</div>'


def quick_form(P, fid, page_name, selected=None, heading="Get your free estimate", badge="Free · No obligation",
               sub="Tell us what you need and we'll get back to you during business hours.", button="Get My Free Estimate", extra=""):
    b = BUSINESS
    badge_html = f'<span class="quote-card__badge">{badge}</span>' if badge else ""
    sel = service_select(selected, id_=fid + "-service").replace(f'id="{fid}-service"', f'id="{fid}-service" aria-describedby="{fid}-service-err"')
    return f'''<div class="quote-card" id="estimate">{badge_html}
<h2>{heading}</h2><p>{sub}</p>
<form id="{fid}" data-quote action="{P}send.php" method="post" data-thanks="{P}thank-you/">
<div class="form-grid">
{field(fid, "name", "Your name", '<input {id} name="name" autocomplete="name" required>', "Please enter your name.", full=True)}
{field(fid, "phone", "Phone", '<input {id} name="phone" type="tel" autocomplete="tel" inputmode="tel" required>', "Enter a 10-digit phone number.")}
{field(fid, "zip", "City or ZIP", '<input {id} name="zip" autocomplete="address-level2">', opt=True)}
<div class="field full"><label for="{fid}-service">What do you need help with?</label>{sel}<span class="err" id="{fid}-service-err">Please choose a service.</span></div>
{extra}
</div>
{hidden_fields(P, page_name)}
<button class="btn btn--lg btn--block" type="submit" style="margin-top:16px">{button} {ic("arrow")}</button>
<div class="form-status" aria-live="polite"></div>
{CONSENT}
</form>
<div class="or">or reach us now</div>
<div class="quick-contact"><a href="tel:{b["phone_e164"]}">{ic("phone")} Call</a><a href="{sms_link()}">{ic("sms")} Text a photo</a></div>
</div>'''


def svc_card(P, s, tag=None, eager=False):
    t = f'<span class="svc__tag">{tag}</span>' if tag else ""
    return f'''<a class="svc reveal" href="{P}services/{s["slug"]}/">{t}<div class="svc__img">{pic(s["card"], "", P, eager=eager, sizes="(max-width:540px) 104px, (max-width:820px) 50vw, 300px")}</div>
<div class="svc__body"><h3>{esc(s["name"])}</h3><p>{esc(s["card_text"])}</p><span class="svc__more">Learn more {ic("arrow")}</span></div></a>'''


def trust_bar():
    items = [("shield", "Licensed &amp; insured", "Protected work"), ("award", "1-year warranty", "On our workmanship"), ("tag", "Price match", "Fair, honest pricing"),
             ("users", "Family owned", "Locally operated"), ("clock", "10+ years", "Of hands-on experience")]
    li = "".join(f'<li><span class="trust__ic">{ic(i)}</span><span>{a}<small>{b}</small></span></li>' for i, a, b in items)
    return f'<section class="trust" aria-label="Why homeowners trust us"><div class="wrap"><ul>{li}</ul></div></section>'


def cta_band(P, title="Ready to get it done?", text="Free estimates, honest pricing, and work backed by a 1-year warranty. Call, text, or send a request. We'll take it from there.", href="contact/"):
    b = BUSINESS
    return f'''<section class="section--tight"><div class="wrap"><div class="cta-band reveal">
<div><h2>{title}</h2><p>{text}</p></div>
<div class="btn-row"><a class="btn btn--lg" href="{P}{href}">{ic("clipboard")} Get a Free Estimate</a><a class="btn btn--ghost btn--lg" href="tel:{b["phone_e164"]}">{ic("phone")} {b["phone_display"]}</a></div>
</div></div></section>'''


def faq_html(faqs):
    return '<div class="faq">' + "".join(f'<details><summary>{esc(q)}</summary><div class="ans"><p>{esc(a)}</p></div></details>' for q, a in faqs) + "</div>"


def offers(P):
    pm = sms_link("Hi Jewell Services! I have a quote from another company I'd like you to match. Here's a photo of it:")
    return f'''<div class="offers">
<div class="offer reveal"><div class="offer__pct">10%<small>OFF</small></div><div><h3>For single mothers</h3><p>10% off any service, our way of giving back to families in our community.</p></div><a class="btn btn--ink" href="{P}contact/?offer=single-mom#estimate">Claim 10% off</a></div>
<div class="offer reveal"><div class="offer__pct">{ic("tag")}</div><div><h3>Price match promise</h3><p>Got a written quote from another company? Text us a photo of it and we'll match it.</p></div><a class="btn btn--ink" href="{pm}">Match my quote</a></div>
</div>'''


def page_hero(P, eyebrow, h1, lead, trail, img=None, ctas=True, media=None, primary="contact/", compact=False):
    """img = full-bleed background photo; media = photo shown beside the text (split layout)."""
    b = BUSINESS
    crumbs = '<nav class="crumbs" aria-label="Breadcrumb"><ol>' + "".join(
        (f'<li><a href="{P}{p}">{esc(n)}</a></li>' if i < len(trail) - 1 else f'<li aria-current="page">{esc(n)}</li>')
        for i, (n, p) in enumerate(trail)) + "</ol></nav>"
    bg = f'<div class="bg">{pic(img, "", P, eager="high", sizes="100vw")}</div>' if img else ""
    cls = "page-hero page-hero--img" if img else ("page-hero page-hero--split" if media else "page-hero")
    if compact:
        cls += " page-hero--compact"
    href = primary if primary.startswith("#") else P + primary
    btns = (f'<div class="btn-row"><a class="btn btn--lg" href="{href}">{ic("clipboard")} Get a Free Estimate</a>'
            f'<a class="btn btn--ghost btn--lg" href="tel:{b["phone_e164"]}">{ic("phone")} {b["phone_display"]}</a></div>'
            f'<p class="hero__text-cta">{ic("sms")}<span>Faster: <a href="{sms_link()}">text a photo of the job</a> to {b["phone_display"]}.</span></p>') if ctas else ""
    text = f'<div>{crumbs}<span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lead">{lead}</p>{btns}</div>'
    side = f'<div class="page-hero__media">{pic(media, "", P, eager="high", sizes="(max-width:900px) 100vw, 480px")}</div>' if media else ""
    return f'<section class="{cls}">{bg}<div class="wrap">{text}{side}</div></section>'


def iowa_map():
    # Simplified Iowa outline projected from lon/lat; dots mark example cities served.
    def xy(lon, lat):
        return round((lon + 96.7) / 6.65 * 600 + 10, 1), round((43.55 - lat) / 3.25 * 380 + 10, 1)
    outline = [(-96.45, 43.5), (-91.22, 43.5), (-91.2, 43.2), (-91.08, 42.95), (-91.15, 42.75), (-90.65, 42.5), (-90.42, 42.33), (-90.15, 42.03), (-90.2, 41.8),
               (-90.35, 41.6), (-90.9, 41.45), (-91.05, 41.17), (-90.95, 40.95), (-91.1, 40.7), (-91.42, 40.38), (-91.73, 40.61), (-95.77, 40.58), (-95.85, 40.95),
               (-95.85, 41.2), (-95.93, 41.4), (-96.1, 41.65), (-96.1, 41.8), (-96.3, 42.0), (-96.35, 42.25), (-96.45, 42.5), (-96.6, 42.7), (-96.45, 43.0), (-96.6, 43.3)]
    d = "M" + " L".join(f"{x},{y}" for x, y in (xy(*p) for p in outline)) + "Z"
    cities = [("Des Moines", -93.61, 41.59, True), ("Ames", -93.62, 42.03, False), ("Cedar Rapids", -91.67, 41.98, False), ("Iowa City", -91.53, 41.66, False),
              ("Davenport", -90.68, 41.56, False), ("Waterloo", -92.34, 42.49, False), ("Sioux City", -96.4, 42.5, False), ("Council Bluffs", -95.86, 41.26, False),
              ("Dubuque", -90.78, 42.48, False), ("Mason City", -93.2, 43.15, False), ("Fort Dodge", -94.17, 42.5, False), ("Ottumwa", -92.41, 41.02, False)]
    dots = ""
    for n, lon, lat, big in cities:
        x, y = xy(lon, lat)
        r = 9 if big else 5
        anchor = "end" if lon > -91.6 else "start"
        dx = -10 if anchor == "end" else 10
        ly = y + 4 + (14 if n == "Iowa City" else 0)
        dots += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{"#2f8a3c" if big else "#1c9fd8"}" stroke="#fff" stroke-width="2"/>'
        dots += f'<text x="{x + dx}" y="{ly}" text-anchor="{anchor}" font-size="{15 if big else 12}" font-weight="{800 if big else 600}" fill="#0d1b2a" font-family="Figtree,sans-serif">{n}</text>'
    return (f'<svg viewBox="0 0 620 400" role="img" aria-label="Map of Iowa showing statewide service coverage">'
            f'<path d="{d}" fill="#e8f5e3" stroke="#2f8a3c" stroke-width="3" stroke-linejoin="round"/>{dots}'
            f'<text x="310" y="392" text-anchor="middle" font-size="13" font-weight="700" fill="#5b6b7b" font-family="Figtree,sans-serif">WE SERVE ALL OF IOWA</text></svg>')


# ---------------------------------------------------------------- pages


def build_home():
    b = BUSINESS
    chips = "".join(f'<a class="chip" href="{{P}}services/{s["slug"]}/">{ic("check")} {esc(o)}</a>' for s in SERVICES for o in s["options"])

    def body(P):
        cards = "".join(svc_card(P, s) for s in SERVICES)
        strip = "".join(f'<a href="{P}projects/">{pic(k, c, P, sizes="(max-width:900px) 33vw, 200px")}</a>' for k, c in GALLERY[:6])
        steps = [("Tell us about the job", "Call, text, or send the form. Photos help us understand it faster."),
                 ("Get a free estimate", "Clear pricing before we start, and we'll match comparable quotes."),
                 ("We do it right", "Respectful of your home, and in touch with you until it's done."),
                 ("Backed by our warranty", "Every job comes with a 1-year warranty on our work.")]
        steps_html = "".join(f'<li class="step reveal"><span class="step__n">{i + 1}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(steps))
        cities = "".join(f"<li>{c}</li>" for c in CITIES_CENTRAL[:8] + CITIES_STATE[:6])
        return f'''
<section class="hero"><div class="wrap hero__grid">
<div>
<span class="eyebrow">Family-owned handyman · Serving all of Iowa</span>
<h1>One call handles your whole <span class="hl">to-do list.</span></h1>
<p class="hero__sub">TV mounting, repairs, new floors, remodels, and more, done right by a licensed and insured family team. Every job is backed by a 1-year warranty.</p>
<div class="btn-row"><a class="btn btn--lg" href="tel:{b["phone_e164"]}">{ic("phone")} Call {b["phone_display"]}</a><a class="btn btn--ghost btn--lg" href="{sms_link()}">{ic("sms")} Text us a photo</a></div>
<ul class="hero__checks"><li>{ic("check-circle")} Free estimates</li><li>{ic("check-circle")} Price match</li><li>{ic("check-circle")} 1-year warranty</li><li>{ic("check-circle")} All of Iowa</li></ul>
<div class="hero__family"><img src="{P}assets/img/brand/family-avatar.jpg" width="104" height="104" alt="The Jewell Services family"><p><strong>Family owned &amp; locally operated</strong>Real people who answer the phone.</p></div>
</div>
{quick_form(P, "hero-form", "Home – hero")}
</div></section>
{trust_bar()}

<section class="section"><div class="wrap">
<div class="head head--split"><div><span class="eyebrow">What we do</span><h2>One call for every project<br>on your list</h2></div>
<p class="lead">Small fixes and big upgrades, inside and out. Pick a service to see what's included, or just tell us what you need.</p></div>
<div class="svc-grid">{cards}</div>
<div class="chips">{chips.replace("{P}", P)}</div>
</div></section>

<section class="section section--white"><div class="wrap split">
<div class="split__media reveal"><div class="media-stack">
<div class="m1">{pic("work/team-family", "The Jewell Services family in their company shirts", P)}</div>
<div class="m2">{pic("work/owner-tv-mount", "Jewell Services owner after mounting a TV", P, sizes="240px")}</div>
<div class="badge"><b>10+</b><span>years of hands-on experience</span></div>
</div></div>
<div class="reveal">
<span class="eyebrow">Why Jewell Services</span>
<h2>We treat your home like jewels</h2>
<p class="lead">We're a family-owned, locally operated business, and we run every job the way we'd want our own home treated.</p>
<ul class="checklist" style="margin-top:24px">
<li>{ic("check")}<span><strong>Licensed &amp; insured.</strong> Your home and your project are protected.</span></li>
<li>{ic("check")}<span><strong>1-year warranty.</strong> If something we did isn't right, we come back and fix it.</span></li>
<li>{ic("check")}<span><strong>Price match.</strong> Bring us a comparable quote and we'll match it.</span></li>
<li>{ic("check")}<span><strong>Constant communication.</strong> We stay in touch with you until the job is done.</span></li>
</ul>
<div class="btn-row"><a class="btn" href="{P}about/">Meet the family {ic("arrow")}</a><a class="btn btn--ghost" href="{P}projects/">See our work</a></div>
</div></div></section>

<section class="section--tight"><div class="wrap">{offers(P)}</div></section>

<section class="section section--ink"><div class="wrap">
<div class="head center"><span class="eyebrow">How it works</span><h2>Getting help is easy</h2><p class="lead">Here's what working with us looks like.</p></div>
<ol class="steps">{steps_html}</ol>
<div class="btn-row" style="justify-content:center;margin-top:40px"><a class="btn btn--lg" href="{P}contact/">Start with a free estimate {ic("arrow")}</a></div>
</div></section>

<section class="section"><div class="wrap">
<div class="head head--split"><div><span class="eyebrow">Our work</span><h2>Real projects. Real Iowa homes.</h2></div><a class="btn btn--ghost" href="{P}projects/">View all projects {ic("arrow")}</a></div>
<div class="strip reveal">{strip}</div>
</div></section>

<section class="section section--white"><div class="wrap split split--rev">
<div class="split__media reveal" style="border-radius:22px;overflow:hidden;box-shadow:var(--shadow-lg)">{pic("stock/commercial", "", P)}</div>
<div class="reveal">
<span class="eyebrow">For businesses</span>
<h2>Commercial building &amp; property maintenance</h2>
<p class="lead">We maintain schools, gyms, daycares, and offices, with one-time repairs or discounted weekly and monthly maintenance plans.</p>
<ul class="checklist checklist--2" style="margin-top:24px">{"".join(f"<li>{ic('check')}<span>{esc(n)}</span></li>" for n, _ in COMMERCIAL_ITEMS[:4])}</ul>
<a class="btn" href="{P}commercial/">Get a free consultation {ic("arrow")}</a>
</div></div></section>

<section class="section"><div class="wrap area">
<div class="reveal">
<span class="eyebrow">Service area</span>
<h2>Proudly serving all of Iowa</h2>
<p class="lead">From the Des Moines metro to every corner of the state. Not sure if we cover your town? We probably do. Just ask.</p>
<ul class="city-list" style="margin-top:24px">{cities}</ul>
<a class="btn btn--ghost" href="{P}service-area/">See our service area {ic("arrow")}</a>
</div>
<div class="iowa-map reveal">{iowa_map()}</div>
</div></section>

<section class="section section--white"><div class="wrap">
<div class="head center"><span class="eyebrow">Questions</span><h2>Frequently asked questions</h2></div>
{faq_html(GENERAL_FAQS[:6])}
</div></section>

<section class="section--tight"><div class="wrap"><div class="fb-card reveal"><div class="fb-card__ic">{ic("facebook")}</div><div style="flex:1"><h3>See our latest projects on Facebook</h3><p>We post jobs as we finish them. Follow along to see the work up close.</p></div><a class="btn btn--ink" href="{b["facebook"]}" target="_blank" rel="noopener">Visit our Facebook</a></div></div></section>
{cta_band(P)}
'''
    page("", "Jewell Services | Iowa Handyman & Home Repair",
         "Family-owned Iowa handyman: TV mounting, flooring, remodels, electrical, painting, and more. Licensed, insured, with a 1-year warranty. Free estimates.",
         body, current="", schemas=[schema_business(""), faq_schema(GENERAL_FAQS[:6])])


def build_services_index():
    def body(P):
        cards = "".join(svc_card(P, s, eager=i < 3) for i, s in enumerate(SERVICES))
        return f'''{page_hero(P, "Our services", "Handyman &amp; remodeling services across Iowa", "From quick fixes to complete renovations, inside and out. Every job is backed by our 1-year warranty and price match promise.", [("Home", ""), ("Services", "services/")], media="work/tv-fireplace-wall")}
<section class="section"><div class="wrap"><div class="svc-grid svc-grid--3">{cards}
<a class="svc reveal" href="{P}commercial/"><div class="svc__img">{pic("stock/commercial", "", P, sizes="(max-width:540px) 104px, 300px")}</div><div class="svc__body"><h3>Commercial Maintenance</h3><p>Schools, gyms, daycares, and offices, with discounted weekly and monthly plans.</p><span class="svc__more">Learn more {ic("arrow")}</span></div></a>
</div></div></section>
{trust_bar()}
<section class="section"><div class="wrap"><div class="head center"><span class="eyebrow">Not sure where your job fits?</span><h2>Just tell us what you need</h2><p class="lead">If it's broken, outdated, or on your to-do list, there's a good chance we can help. Send us a quick note and we'll let you know.</p></div>
<div style="max-width:620px;margin:0 auto">{quick_form(P, "svc-form", "Services index", badge=None, heading="Describe your project", sub="We'll call or text you back with next steps and a free estimate.", extra=NOTES("svc-form"))}</div></div></section>'''
    page("services/", "Handyman & Remodeling Services in Iowa",
         "TV mounting, flooring, remodels, electrical, painting, drywall, siding, decks, snow removal, lawn care, and more. Free estimates across Iowa.",
         body, current="services/", schemas=[crumbs_schema([("Home", ""), ("Services", "services/")])])


def build_service(s):
    path = f'services/{s["slug"]}/'
    trail = [("Home", ""), ("Services", "services/"), (s["name"], path)]
    faqs = s["faqs"] + [GENERAL_FAQS[2]]
    contact = "contact/?service=" + quote_plus(s["options"][0]) + "#estimate"

    def body(P):
        items = "".join(f'<div class="card"><h3>{ic("check-circle")}{esc(n)}</h3><p>{esc(d)}</p></div>' for n, d in s["items"])
        photos = "".join(
            f'<figure>{pic(k, c, P, sizes="(max-width:640px) 50vw, 260px")}' + (f'<figcaption>{esc(c)}</figcaption>' if k.startswith("work/") else "") + "</figure>"
            for k, c in s["photos"])
        cols = len(s["photos"])
        others = [o for o in SERVICES if o["slug"] != s["slug"]]
        idx = SERVICES.index(s)
        related = "".join(svc_card(P, others[(idx + i) % len(others)]) for i in range(3))
        return f'''{page_hero(P, esc(s["name"]), esc(s["h1"]), esc(s["intro"]), trail, media=s["hero"], primary="#estimate")}
{trust_bar()}
<section class="section"><div class="wrap detail">
<div class="prose">
<h2>What we do</h2>
<div class="sub-svc">{items}</div>
<div class="photo-row" style="grid-template-columns:repeat({cols},1fr)">{photos}</div>
<h2>Common questions</h2>
{faq_html(faqs)}
</div>
<aside>{quick_form(P, "svc-" + s["slug"], s["name"], selected=s["options"][0], heading="Free estimate", badge="Free · No obligation")}
<div class="aside-card" style="margin-top:20px;box-shadow:none"><h3>Prefer to talk?</h3><p style="margin:0;color:var(--muted)">Call or text <a class="link-strong" href="tel:{BUSINESS["phone_e164"]}">{BUSINESS["phone_display"]}</a>. Mon–Fri 9–5, weekends by appointment.</p></div>
</aside>
</div></section>
<section class="section section--white"><div class="wrap"><div class="head head--split"><div><span class="eyebrow">More services</span><h2>We can help with that too</h2></div><a class="btn btn--ghost" href="{P}services/">All services {ic("arrow")}</a></div><div class="related">{related}</div></div></section>
{cta_band(P, esc(s["cta"]), href=contact)}'''
    biz = {"@type": "HomeAndConstructionBusiness", "@id": BUSINESS["url"] + "/#business", "name": BUSINESS["name"], "telephone": BUSINESS["phone_e164"], "url": BUSINESS["url"] + "/"}
    svc_schema = {"@context": "https://schema.org", "@type": "Service", "name": s["name"], "serviceType": s["name"],
                  "provider": biz, "areaServed": {"@type": "State", "name": "Iowa"}, "description": s["intro"]}
    page(path, s["title"], s["desc"], body, current=path, schemas=[svc_schema, crumbs_schema(trail), faq_schema(faqs)],
         og_img=s["hero"] + ".jpg")


def build_commercial():
    trail = [("Home", ""), ("Commercial", "commercial/")]
    faqs = [("Do you offer maintenance plans?", "Yes. We offer discounted weekly and monthly maintenance plans, as well as one-time service."),
            ("What types of facilities do you service?", "We service schools, gyms, daycares, and offices, and we're happy to talk about other commercial properties."),
            ("How do we get started?", "Request a free consultation. We'll learn what your building needs and recommend a one-time or recurring plan.")]
    sector_copy = {"Schools": "Classrooms, restrooms, and common areas kept safe and in good repair.",
                   "Gyms": "Locker rooms, restrooms, and ventilation kept clean and working.",
                   "Daycares": "A safe, well-kept space for kids, parents, and staff.",
                   "Offices": "Repairs and upkeep that keep your workspace looking professional."}

    def body(P):
        sectors = "".join(f'<div class="card sector reveal"><div class="card__ic card__ic--sky">{ic(i)}</div><h3>{n}</h3><p>{sector_copy[n]}</p></div>' for i, n in SECTORS)
        items = "".join(f'<div class="card reveal"><h3 style="display:flex;gap:10px;align-items:center">{ic("check-circle")}{esc(n)}</h3><p>{esc(d)}</p></div>' for n, d in COMMERCIAL_ITEMS)
        extra = field("commercial-form", "business", "Business or facility name", '<input {id} name="business" autocomplete="organization">', full=True, opt=True)
        return f'''{page_hero(P, "Commercial services", "Building &amp; property maintenance for Iowa businesses", "One dependable team for the repairs and recurring maintenance your facility needs. Free consultations, with discounted weekly and monthly plans.", trail, media="stock/commercial", primary="#estimate")}
<section class="section"><div class="wrap"><div class="head center"><span class="eyebrow">Who we serve</span><h2>Facilities we maintain</h2></div><div class="cards4">{sectors}</div></div></section>
<section class="section section--white"><div class="wrap"><div class="head"><span class="eyebrow">What we handle</span><h2>General building &amp; property maintenance</h2><p class="lead">Whether you need help once or on a schedule, we keep your building in shape so you can focus on your business.</p></div><div class="sub-svc cards-3col">{items}</div></div></section>
<section class="section section--ink"><div class="wrap split">
<div><span class="eyebrow">Maintenance plans</span><h2>Save with a weekly or monthly plan</h2><p class="lead">Recurring service means fewer surprises, a building that always looks cared for, and a discounted rate.</p>
<ul class="checklist" style="margin-top:24px;color:#c9d4df">
<li>{ic("check")}<span>Free consultation</span></li><li>{ic("check")}<span>One-time or recurring service</span></li><li>{ic("check")}<span>Discounted weekly &amp; monthly plans</span></li><li>{ic("check")}<span>Licensed &amp; insured</span></li></ul></div>
<div>{quick_form(P, "commercial-form", "Commercial", selected="Commercial / Building Maintenance", heading="Request a free consultation", badge="Free consultation", sub="Tell us about your facility and we'll be in touch to talk through your needs.", button="Request My Free Consultation", extra=extra)}</div>
</div></section>
<section class="section"><div class="wrap"><div class="head center"><h2>Commercial FAQs</h2></div>{faq_html(faqs)}</div></section>
{cta_band(P, "Let's keep your building in top shape", "One call for repairs and recurring maintenance. Ask about discounted weekly and monthly plans.", href="contact/?service=Commercial+%2F+Building+Maintenance#estimate")}'''
    page("commercial/", "Commercial Building Maintenance in Iowa",
         "Building maintenance for Iowa schools, gyms, daycares, and offices. Free consultations, with discounted weekly and monthly plans.",
         body, current="commercial/", schemas=[crumbs_schema(trail), faq_schema(faqs)])


def build_about():
    trail = [("Home", ""), ("About", "about/")]

    def body(P):
        values = [("gem", "We treat your home like jewels", "We protect your floors, respect your space, and clean up when we're done."),
                  ("msg", "Constant communication", "We stay in touch with our customers until the job is done. No guessing, no ghosting."),
                  ("award", "Done right, guaranteed", "Every job is backed by a 1-year warranty, and we stand behind our work."),
                  ("tag", "Fair, honest pricing", "Free estimates and a price match promise on comparable quotes."),
                  ("heart", "Giving back", "10% off any service for single mothers, because community matters."),
                  ("shield", "Licensed &amp; insured", "Real protection for your home and peace of mind for you.")]
        vh = "".join(f'<div class="card reveal"><div class="card__ic">{ic(i)}</div><h3>{t}</h3><p>{d}</p></div>' for i, t, d in values)
        return f'''{page_hero(P, "About us", "A family business that treats your home like jewels", "Jewell Services is family owned and locally operated, with more than 10 years of experience helping Iowa homeowners and businesses.", trail)}
<section class="section section--white"><div class="wrap split">
<div class="split__media reveal"><div class="media-stack">
<div class="m1">{pic("work/team-family", "The Jewell Services family in their company shirts", P)}</div>
<div class="m2">{pic("work/owner-tv-mount", "Jewell Services owner on the job", P, sizes="240px")}</div>
<div class="badge"><b>10+</b><span>years of experience</span></div></div></div>
<div class="reveal">
<span class="eyebrow">Our story</span>
<h2>Family owned. Locally operated. Built on trust.</h2>
<p>Jewell Services started with a simple idea: treat every customer's home the way we'd want ours treated. With more than 10 years of hands-on experience, we've grown from quick repairs into a full-service handyman and remodeling company with carpentry, flooring, electrical, painting, remodels, and more.</p>
<p>We're a family business, Black-owned and locally operated, and our name is on every job. That's why we stay in constant communication until your project is done, back our work with a 1-year warranty, and keep our pricing fair with a price match promise.</p>
<p>Today we serve homeowners and businesses all across Iowa, and we'd love to help with your next project.</p>
<div class="stat-row stat-row--3"><div class="stat"><b>10+</b><span>Years experience</span></div><div class="stat"><b>1 yr</b><span>Warranty</span></div><div class="stat"><b>Free</b><span>Estimates</span></div></div>
</div></div></section>
<section class="section"><div class="wrap"><div class="head center"><span class="eyebrow">What we stand for</span><h2>Our promise to you</h2></div><div class="cards3">{vh}</div></div></section>
<section class="section--tight"><div class="wrap">{offers(P)}</div></section>
{cta_band(P, "Let's take care of your home together")}'''
    page("about/", "About Us | Family-Owned Iowa Handyman",
         "Meet Jewell Services: a family-owned, locally operated Iowa handyman and remodeling company with 10+ years of experience.",
         body, current="about/", schemas=[crumbs_schema(trail)], og_img="work/team-family.jpg")


def build_projects():
    trail = [("Home", ""), ("Our Work", "projects/")]

    def body(P):
        figs = ""
        for i, (k, c) in enumerate(GALLERY):
            figs += (f'<figure class="reveal"><button type="button" data-lightbox data-full="{P}assets/img/{k}.webp" data-caption="{esc(c)}" aria-label="View larger: {esc(c)}">'
                     f'{pic(k, c, P, eager=("high" if i == 0 else True) if i < 3 else False, sizes="(max-width:700px) 100vw, 380px")}</button><figcaption>{esc(c)}</figcaption></figure>')
        return f'''{page_hero(P, "Our work", "Real projects from real Iowa homes", "Every photo here is a Jewell Services job. Tap any photo to see it larger.", trail, compact=True)}
<section class="section"><div class="wrap"><div class="gallery">{figs}</div></div></section>
<section class="section--tight"><div class="wrap"><div class="fb-card"><div class="fb-card__ic">{ic("facebook")}</div><div style="flex:1"><h2 style="font-size:1.3rem;margin-bottom:4px">More projects on Facebook</h2><p>We post new work regularly. Follow along to see what we're building.</p></div><a class="btn btn--ink" href="{BUSINESS["facebook"]}" target="_blank" rel="noopener">Follow us</a></div></div></section>
{cta_band(P, "Want results like these?")}'''
    page("projects/", "Our Work | Project Gallery",
         "See real Jewell Services projects across Iowa: TV mounting, LVP flooring, siding, framing, electrical, and more.",
         body, current="projects/", schemas=[crumbs_schema(trail)])


def build_area():
    trail = [("Home", ""), ("Service Area", "service-area/")]

    def body(P):
        c1 = "".join(f"<li>{c}</li>" for c in CITIES_CENTRAL)
        c2 = "".join(f"<li>{c}</li>" for c in CITIES_STATE)
        return f'''{page_hero(P, "Service area", "Handyman services across all of Iowa", "Wherever you are in Iowa, Jewell Services can help. Tell us your town and we'll confirm scheduling for your area.", trail, compact=True)}
<section class="section"><div class="wrap area">
<div class="iowa-map reveal">{iowa_map()}</div>
<div class="reveal">
<h2>Central Iowa &amp; the Des Moines metro</h2>
<ul class="city-list">{c1}</ul>
<h2 style="font-size:1.6rem">Across the state</h2>
<ul class="city-list">{c2}</ul>
<p class="notice">Don't see your town? <strong>We serve all of Iowa.</strong> Call or text <a class="link-strong" href="tel:{BUSINESS["phone_e164"]}">{BUSINESS["phone_display"]}</a> and we'll let you know when we can get to you.</p>
</div></div></section>
<section class="section section--white"><div class="wrap"><div class="head center"><span class="eyebrow">Available everywhere we go</span><h2>Our services</h2></div><div class="svc-grid">{"".join(svc_card(P, s) for s in SERVICES)}</div></div></section>
{cta_band(P)}'''
    page("service-area/", "Service Area | Handyman Serving All of Iowa",
         "Handyman, remodeling, and maintenance across all of Iowa, from Des Moines, Ankeny, and Ames to Cedar Rapids, Iowa City, and Davenport.",
         body, current="service-area/", schemas=[crumbs_schema(trail)])


def build_contact():
    trail = [("Home", ""), ("Contact", "contact/")]
    b = BUSINESS
    f = "c"

    def body(P):
        email_row = f'<div class="info-row">{ic("mail")}<div><small>Email</small><a href="mailto:{b["email"]}">{b["email"]}</a></div></div>' if b["email"] else ""
        sel = service_select(id_="c-service").replace('id="c-service"', 'id="c-service" aria-describedby="c-service-err"')
        return f'''{page_hero(P, "Free estimate", "Get your free estimate", "Tell us about your project and we'll get back to you during business hours. Prefer to talk? Call or text us.", trail, ctas=False, compact=True)}
<section class="section" style="padding-top:clamp(32px,4vw,56px)"><div class="wrap contact-grid">
<div class="quote-card" id="estimate">
<div class="form-banner" data-error-banner hidden role="alert">Sorry, your request didn't go through. Please try again, or call or text <a href="tel:{b["phone_e164"]}">{b["phone_display"]}</a>.</div>
<h2>Request a free estimate</h2><p>The more you tell us, the more accurate your estimate. Photos help a lot.</p>
<form id="contact-form" data-quote action="{P}send.php" method="post" enctype="multipart/form-data" data-thanks="{P}thank-you/">
<div class="form-grid">
{field(f, "name", "Your name", '<input {id} name="name" autocomplete="name" required>', "Please enter your name.")}
{field(f, "phone", "Phone", '<input {id} name="phone" type="tel" autocomplete="tel" inputmode="tel" required>', "Enter a 10-digit phone number.")}
{field(f, "email", "Email", '<input {id} name="email" type="email" autocomplete="email">', "Please check your email address.", opt=True)}
{field(f, "zip", "City or ZIP", '<input {id} name="zip" autocomplete="address-level2">', opt=True)}
<div class="field full"><label for="c-service">Service needed</label>{sel}<span class="err" id="c-service-err">Please choose a service.</span></div>
{field(f, "address", "Project address", '<input {id} name="address" autocomplete="street-address">', full=True, opt=True)}
{field(f, "when", "When do you need it?", '<select {id} name="timeframe"><option>As soon as possible</option><option>Within 2 weeks</option><option>Within a month</option><option>I&#39;m flexible</option><option>Just getting prices</option></select>')}
{field(f, "pref", "Best way to reach you", '<select {id} name="contact_pref"><option>Call</option><option>Text</option><option>Email</option></select>')}
{field(f, "msg", "Tell us about the project", '<textarea {id} name="message" placeholder="Example: Mount a 65-inch TV above the fireplace and hide the cords."></textarea>', full=True, opt=True)}
<div class="field full"><span style="display:block;font-weight:700;font-size:.88rem;color:var(--ink);margin-bottom:6px">Photos <span style="font-weight:500;color:var(--muted)">(optional, up to 5)</span></span><label class="file-input">{ic("image")}<span data-file-label data-default="Add photos of the project">Add photos of the project</span><input type="file" name="photos[]" accept="image/jpeg,image/png,image/webp,image/heic,image/heif" multiple></label></div>
<div class="field full"><label class="check-field"><input type="checkbox" name="single_mom" value="1"> <span>I'm a single mother. Apply my 10% discount.</span></label></div>
</div>
{hidden_fields(P, "Contact page")}
<button class="btn btn--lg btn--block" type="submit" style="margin-top:18px">Send My Free Estimate Request {ic("arrow")}</button>
<div class="form-status" aria-live="polite"></div>
<p class="consent">By sending, you agree Jewell Services may call or text you about your request. See our <a href="{P}privacy/">privacy policy</a>.</p>
</form>
</div>
<aside>
<div class="info-card">
<h3>Talk to us directly</h3>
<div class="info-row">{ic("phone")}<div><small>Call</small><a href="tel:{b["phone_e164"]}">{b["phone_display"]}</a></div></div>
<div class="info-row">{ic("sms")}<div><small>Text a photo</small><a href="{sms_link()}">{b["phone_display"]}</a></div></div>
{email_row}
<div class="info-row">{ic("facebook")}<div><small>Facebook</small><a href="{b["facebook"]}" target="_blank" rel="noopener">Message us on Facebook</a></div></div>
<div class="info-row">{ic("pin")}<div><small>Service area</small>All of Iowa</div></div>
<div class="info-row">{ic("clock")}<div style="flex:1"><small>Hours</small><table class="hours"><tbody>{hours_rows()}</tbody></table></div></div>
</div>
<div class="card" style="margin-top:20px"><h3>What happens next?</h3><ol style="margin:0;padding-left:1.2em;color:var(--muted)"><li>We review your request.</li><li>We reach out to talk it through.</li><li>You get a clear, free estimate.</li></ol></div>
</aside>
</div></section>'''
    page("contact/", "Free Estimate | Contact Us",
         "Request a free estimate from Jewell Services. Call or text 515-451-9566, or send your project details and photos online.",
         body, current="contact/", schemas=[crumbs_schema(trail)])


def build_thanks():
    def body(P):
        return f'''<section class="section"><div class="wrap thanks">
<div class="thanks__ic">{ic("check")}</div>
<h1>Thank you! We got your request.</h1>
<p class="lead" style="margin:0 auto 28px">We'll reach out during business hours (Mon–Fri, 9–5). Want a faster, more accurate estimate? Text us photos of the job.</p>
<div class="btn-row" style="justify-content:center"><a class="btn btn--lg" href="{sms_link()}">{ic("sms")} Text photos to {BUSINESS["phone_display"]}</a><a class="btn btn--ghost btn--lg" href="tel:{BUSINESS["phone_e164"]}">{ic("phone")} Call us</a></div>
<p style="margin-top:28px"><a class="link-strong" href="{BUSINESS["facebook"]}" target="_blank" rel="noopener">Follow our latest projects on Facebook</a></p>
</div></section>'''
    page("thank-you/", "Thank You", "Thanks for contacting Jewell Services.", body, current="thank-you/", noindex=True)


def build_privacy():
    def body(P):
        return f'''{page_hero(P, "Legal", "Privacy policy", "How we handle the information you share with us. Effective October 31, 2026.", [("Home", ""), ("Privacy", "privacy/")], ctas=False, compact=True)}
<section class="section"><div class="wrap legal">
<h2>Information we collect</h2><p>When you request an estimate, we collect the details you choose to share: your name, phone number, email address, city or ZIP code, project address, project details, and any photos you upload.</p>
<h2>How we use it</h2><p>We use your information only to respond to your request, provide estimates, schedule and complete work, and follow up about your project. We do not sell or rent your personal information.</p>
<h2>Calls and text messages</h2><p>If you give us your phone number, we may call or text you about your request. Message and data rates may apply. Just tell us if you'd like us to stop texting you, and we will.</p>
<h2>Cookies and analytics</h2><p>This website may use basic analytics to understand how visitors use the site and improve it. These tools may use cookies. You can block cookies in your browser settings.</p>
<h2>Contact</h2><p>Questions about this policy? Call or text {BUSINESS["phone_display"]}, or message us on <a href="{BUSINESS["facebook"]}">Facebook</a>.</p>
</div></section>'''
    page("privacy/", "Privacy Policy", "How Jewell Services collects, uses, and protects the information you share when you request an estimate.", body)


def build_404():
    def body(P):
        return f'''<section class="section"><div class="wrap thanks">
<h1>Sorry, we couldn't find that page.</h1>
<p class="lead" style="margin:0 auto 28px">But we can probably fix whatever's on your to-do list. Try one of these:</p>
<div class="btn-row" style="justify-content:center"><a class="btn btn--lg" href="{P}">Go to the homepage</a><a class="btn btn--ghost btn--lg" href="{P}services/">View services</a></div>
</div></section>'''
    # 404 is served from any URL depth, so it uses root-absolute paths (site lives at the domain root on Hostinger)
    page("404.html", "Page Not Found", "Page not found.", body, noindex=True, root_abs=True)


def build_static():
    shutil.copytree(SRC / "assets", DIST / "assets", dirs_exist_ok=True)
    out = DIST / "assets" / "img"
    shutil.copytree(IMG / "brand", out / "brand", dirs_exist_ok=True)
    # only ship images a page actually references
    for key in sorted(USED_IMAGES):
        (out / key).parent.mkdir(parents=True, exist_ok=True)
        for suf in [".jpg", ".webp", "-sm.jpg", "-sm.webp"]:
            shutil.copy(IMG / f"{key}{suf}", out / f"{key}{suf}")
    av = Image.open(IMG / "work/team-family.jpg").convert("RGB")
    side = min(av.size)
    av = av.crop(((av.width - side) // 2, 0, (av.width + side) // 2, side)).resize((104, 104), Image.LANCZOS)
    av.save(out / "brand" / "family-avatar.jpg", quality=82)
    shutil.copy(SRC / "send.php", DIST / "send.php")
    if STAGING:
        (DIST / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
    else:
        (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BUSINESS['url']}/sitemap.xml\n")
    urls = "".join(f"<url><loc>{BUSINESS['url']}/{p}</loc></url>" for p, noidx in PAGES if not noidx and p != "404.html")
    (DIST / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    (DIST / "site.webmanifest").write_text(json.dumps({
        "name": "Jewell Services", "short_name": "Jewell", "start_url": "./", "display": "browser", "background_color": "#fbf7f1", "theme_color": "#0d1b2a",
        "icons": [{"src": "assets/img/brand/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "assets/img/brand/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=1))
    (DIST / ".htaccess").write_text("""# Jewell Services — Apache / LiteSpeed (Hostinger) config
Options -Indexes
ErrorDocument 404 /404.html
DirectoryIndex index.html index.php

RewriteEngine On
# Force HTTPS
RewriteCond %{HTTPS} off
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
# Block the private lead backup folder (send.php prefers a folder outside public_html)
RewriteRule ^_leads(/|$) - [F,L]

<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType font/woff2 "access plus 1 year"
  ExpiresByType text/css "access plus 1 year"
  ExpiresByType application/javascript "access plus 1 year"
  ExpiresByType text/javascript "access plus 1 year"
  ExpiresByType application/manifest+json "access plus 1 week"
  ExpiresByType text/html "access plus 0 seconds"
</IfModule>
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript text/javascript image/svg+xml application/json
</IfModule>
<IfModule mod_headers.c>
  Header always set X-Content-Type-Options "nosniff"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
  Header always set X-Frame-Options "SAMEORIGIN"
</IfModule>
""")


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    build_home()
    build_services_index()
    for s in SERVICES:
        build_service(s)
    build_commercial()
    build_about()
    build_projects()
    build_area()
    build_contact()
    build_thanks()
    build_privacy()
    build_404()
    build_static()
    print(f"Built {len(PAGES)} pages into {DIST}")


if __name__ == "__main__":
    main()
