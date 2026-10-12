"""Static site generator for D Dynamic Fitness.

Edit BUSINESS below (NAP, domain, socials), then run:  python build.py
Every page, the JSON-LD schema, sitemap.xml (with video entries) and robots.txt are regenerated.
"""
import json
import re
import os
from datetime import date
from html import escape
from urllib.parse import quote

import content
from content import CATEGORY_IMG, FAQS, GALLERY, IMG
from content_extra import AREA_EXTRA, SERVICE_EXTRA
from content_more import ICONS, NEW_SERVICES, ORDER, VIDEO_CATEGORY, VIDEO_FOR, VIDEOS

# ---------------------------------------------------------------- business data (NAP)
# TODO before launch: replace every value marked PLACEHOLDER with the client's real details,
# and make sure they match the Google Business Profile character for character.
BUSINESS = {
    "name": "D Dynamic Fitness",
    "coach": "Don Michael Ondiro",
    "category": "Personal Trainer",
    "city": "Nairobi",
    "region": "Nairobi County",
    "country": "KE",
    "street": "",  # PLACEHOLDER: leave empty for a service-area business, or add the gym's street address
    "postcode": "",  # PLACEHOLDER
    "phone_display": "+254 700 000 000",  # PLACEHOLDER
    "phone_e164": "+254700000000",  # PLACEHOLDER (also used for WhatsApp)
    "email": "hello@ddynamicfitness.co.ke",  # PLACEHOLDER
    "site_url": "https://www.ddynamicfitness.co.ke",  # PLACEHOLDER: final domain, no trailing slash
    "geo": (-1.2921, 36.8219),  # Nairobi centre; replace with the gym's coordinates if it has one
    "hours": "Mon to Sat, 6:00am to 8:00pm",  # PLACEHOLDER: confirm with client
    "hours_schema": [  # PLACEHOLDER: must match GBP hours
        {"days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "opens": "06:00", "closes": "20:00"},
    ],
    "instagram": "https://www.instagram.com/d_dynamicfitness_/",
    "threads": "https://www.threads.com/@d_dynamicfitness_",
    "facebook": "",  # PLACEHOLDER: add the Facebook page URL when available
    "map_embed": "https://www.google.com/maps?q=Nairobi,+Kenya&output=embed",  # swap for the GBP embed URL
}
B = BUSINESS
# Optional overrides for preview hosting, e.g. GitHub Pages:
#   SITE_URL=https://user.github.io/repo BASE_PATH=/repo/ python build.py
if os.environ.get("SITE_URL"):
    B["site_url"] = os.environ["SITE_URL"].rstrip("/")
BASE_PATH = os.environ.get("BASE_PATH", "/")
OUT = os.path.dirname(os.path.abspath(__file__))
TODAY = date.today().isoformat()

# ---------------------------------------------------------------- merge content
_all = {s["slug"]: dict(s) for s in content.SERVICES + NEW_SERVICES}
for slug, extra in SERVICE_EXTRA.items():
    _all[slug]["sections"] = list(_all[slug]["sections"]) + extra["sections"]
    _all[slug]["faqs"] = list(_all[slug]["faqs"]) + extra["faqs"]
for k, v in CATEGORY_IMG.items():
    _all[k]["img"] = v
SERVICES = [_all[k] for k in ORDER]
SVC = {s["slug"]: s for s in SERVICES}

AREA_ADD = {"westlands": "gym-training", "kilimani": "aerobics-cardio", "kileleshwa": "kids-teens-fitness",
            "lavington": "weight-loss-training", "karen": "group-fitness", "parklands": "mma-training"}
AREA_VIDEO = {"westlands": "shadow", "kilimani": "one_arm", "kileleshwa": "jkd_kicks",
              "lavington": "squats", "karen": "gym_endurance", "parklands": "partner"}
AREAS = []
for a in content.AREAS:
    a = dict(a)
    a["services"] = a["services"] + [AREA_ADD[a["slug"]]]
    a["sections"] = AREA_EXTRA[a["slug"]]["sections"]
    a["faqs"] = a["faqs"] + AREA_EXTRA[a["slug"]]["faqs"]
    AREAS.append(a)

LOGO_SVG = open(os.path.join(OUT, "assets", "logo-mark.svg"), encoding="utf-8").read().replace('role="img"', 'aria-hidden="true"')


def wa_link(text="Hi Coach Don, I'd like to book a training session."):
    return f"https://wa.me/{B['phone_e164'].lstrip('+')}?text={quote(text)}"


def address_line():
    parts = [p for p in (B["street"], B["city"], B["postcode"]) if p]
    return ", ".join(parts) + ", Kenya"


def img_tag(key, root, cls="", eager=False):
    f, alt, w, h = IMG[key]
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    return f'<img src="{root}images/{f}" alt="{escape(alt)}" width="{w}" height="{h}" {load} decoding="async"{c}>'


def icon(slug, cls="ico"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="{ICONS[slug]}"/></svg>'


def video_tag(key, root, caption=False):
    stem, title, desc, _, _, orient = VIDEOS[key]
    w, h = (1280, 720) if orient == "h" else (720, 1280)
    cap = f"<figcaption>{escape(title)}</figcaption>" if caption else ""
    return (f'<figure class="vid vid-{orient}"><video controls preload="none" playsinline width="{w}" height="{h}" '
            f'poster="{root}videos/{stem}.jpg" title="{escape(title)}"><source src="{root}videos/{stem}.mp4" type="video/mp4">'
            f'Your browser does not support video.</video>{cap}</figure>')


# ---------------------------------------------------------------- schema
def abs_url(p):
    return B["site_url"] + "/" + p


def business_id():
    return B["site_url"] + "/#business"


def business_schema():
    return {
        "@type": ["LocalBusiness", "SportsActivityLocation"],
        "@id": business_id(),
        "name": B["name"],
        "description": "Certified personal trainer in Nairobi offering personal training, gym and weight training, MMA, aerobics, Jeet Kune Do, boxing fitness, calisthenics, weight loss, group classes and kids martial arts.",
        "url": B["site_url"] + "/",
        "image": [abs_url("images/" + IMG[k][0]) for k in ("portrait", "kick", "squat")],
        "logo": abs_url("assets/logo-mark-512.png"),
        "telephone": B["phone_e164"],
        "email": B["email"],
        "address": {
            "@type": "PostalAddress",
            **({"streetAddress": B["street"]} if B["street"] else {}),
            "addressLocality": B["city"],
            "addressRegion": B["region"],
            **({"postalCode": B["postcode"]} if B["postcode"] else {}),
            "addressCountry": B["country"],
        },
        "geo": {"@type": "GeoCoordinates", "latitude": B["geo"][0], "longitude": B["geo"][1]},
        "areaServed": [{"@type": "City", "name": "Nairobi"}] + [{"@type": "Place", "name": f"{a['name']}, Nairobi"} for a in AREAS],
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": h["days"], "opens": h["opens"], "closes": h["closes"]}
            for h in B["hours_schema"]
        ],
        "founder": {"@id": B["site_url"] + "/#coach"},
        "sameAs": [u for u in (B["instagram"], B["threads"], B["facebook"]) if u],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Fitness coaching services",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"], "url": abs_url(f"services/{s['slug']}.html")}}
                for s in SERVICES
            ],
        },
    }


def coach_schema():
    return {
        "@type": "Person",
        "@id": B["site_url"] + "/#coach",
        "name": B["coach"],
        "jobTitle": "Certified Fitness and Performance Coach",
        "image": abs_url("images/" + IMG["portrait"][0]),
        "worksFor": {"@id": business_id()},
        "knowsAbout": ["Personal training", "Weight training", "Calisthenics", "Jeet Kune Do", "Mixed martial arts",
                       "Boxing", "Aerobics", "Strength and conditioning", "Mobility training"],
        "sameAs": [B["instagram"], B["threads"]],
    }


def website_schema():
    return {"@type": "WebSite", "@id": B["site_url"] + "/#website", "url": B["site_url"] + "/", "name": B["name"],
            "publisher": {"@id": business_id()}, "inLanguage": "en-KE"}


def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


def breadcrumb_schema(crumbs):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": abs_url(u)} for i, (n, u) in enumerate(crumbs)]}


def video_schema(key):
    stem, title, desc, up, dur, _ = VIDEOS[key]
    return {
        "@type": "VideoObject",
        "@id": abs_url(f"videos.html#{stem}"),
        "name": title,
        "description": desc,
        "thumbnailUrl": abs_url(f"videos/{stem}.jpg"),
        "contentUrl": abs_url(f"videos/{stem}.mp4"),
        "uploadDate": up + "T12:00:00+03:00",
        "duration": dur,
        "publisher": {"@id": business_id()},
        "creator": {"@id": B["site_url"] + "/#coach"},
    }


def service_schema(s):
    return {
        "@type": "Service",
        "@id": abs_url(f"services/{s['slug']}.html#service"),
        "name": s["name"],
        "serviceType": s["short"],
        "description": s["meta"],
        "provider": {"@id": business_id()},
        "areaServed": [{"@type": "City", "name": "Nairobi"}] + [{"@type": "Place", "name": f"{a['name']}, Nairobi"} for a in AREAS],
        "image": abs_url("images/" + IMG[s["img"]][0]),
        "url": abs_url(f"services/{s['slug']}.html"),
    }


def jsonld(nodes):
    data = {"@context": "https://schema.org", "@graph": nodes}
    return '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=1) + "\n</script>"


# ---------------------------------------------------------------- layout
def head(title, meta, path, root, schema_nodes, og_img=None):
    canonical = abs_url(path)
    og_url = abs_url("images/" + IMG[og_img][0]) if og_img else abs_url("assets/og-image.jpg")
    return f"""<!doctype html>
<html lang="en-KE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(meta)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow, max-image-preview:large, max-video-preview:-1">
<meta name="geo.region" content="KE-110">
<meta name="geo.placename" content="Nairobi">
<meta name="geo.position" content="{B['geo'][0]};{B['geo'][1]}">
<meta name="ICBM" content="{B['geo'][0]}, {B['geo'][1]}">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_KE">
<meta property="og:site_name" content="{B['name']}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(meta)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_url}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escape(title)}">
<meta name="twitter:description" content="{escape(meta)}">
<meta name="twitter:image" content="{og_url}">
<meta name="theme-color" content="#0e0f11">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{root}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/style.css">
{jsonld(schema_nodes)}
</head>
<body>
"""


def logo(root):
    return (f'<a class="brand" href="{root}index.html" aria-label="{B["name"]} home">{LOGO_SVG}'
            f'<span class="brand-text"><span class="brand-name">Dynamic<b>Fitness</b></span><span class="brand-tag">Nairobi &middot; Coach Don</span></span></a>')


def header(root, active=""):
    svc_links = "".join(f'<li><a href="{root}services/{s["slug"]}.html">{icon(s["slug"])}{s["short"]}</a></li>' for s in SERVICES)
    area_links = "".join(f'<li><a href="{root}areas/{a["slug"]}.html">{a["name"]}</a></li>' for a in AREAS)

    def cls(k):
        return ' aria-current="page"' if k == active else ""

    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
 <div class="wrap nav-row">
  {logo(root)}
  <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Open menu"><span></span><span></span><span></span></button>
  <nav id="nav" class="nav" aria-label="Main">
   <ul>
    <li><a href="{root}index.html"{cls('home')}>Home</a></li>
    <li><a href="{root}about.html"{cls('about')}>About</a></li>
    <li class="has-sub mega"><a href="{root}services/index.html"{cls('services')}>Training</a><ul class="sub">{svc_links}</ul></li>
    <li class="has-sub"><a href="{root}areas/index.html"{cls('areas')}>Areas</a><ul class="sub">{area_links}</ul></li>
    <li><a href="{root}videos.html"{cls('videos')}>Videos</a></li>
    <li><a href="{root}gallery.html"{cls('gallery')}>Gallery</a></li>
    <li><a href="{root}faq.html"{cls('faq')}>FAQ</a></li>
    <li><a href="{root}contact.html"{cls('contact')}>Contact</a></li>
   </ul>
   <a class="btn btn-sm" href="{wa_link()}" target="_blank" rel="noopener">Book a Session</a>
  </nav>
 </div>
</header>
<main id="main">
"""


def footer(root):
    svc = "".join(f'<li><a href="{root}services/{s["slug"]}.html">{s["short"]} Nairobi</a></li>' for s in SERVICES)
    areas = "".join(f'<li><a href="{root}areas/{a["slug"]}.html">Personal Trainer {a["name"]}</a></li>' for a in AREAS)
    socials = [("Instagram", B["instagram"]), ("Threads", B["threads"]), ("Facebook", B["facebook"])]
    soc = "".join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in socials if u)
    return f"""</main>
<section class="cta-band">
 <div class="wrap cta-inner">
  <div><h2>Ready to train with Nairobi's most dynamic coach?</h2><p>Tell us your goal and we'll plan your first session.</p></div>
  <div class="cta-btns"><a class="btn" href="{wa_link()}" target="_blank" rel="noopener">WhatsApp Coach Don</a><a class="btn btn-ghost" href="tel:{B['phone_e164']}">Call {B['phone_display']}</a></div>
 </div>
</section>
<footer class="site-footer">
 <div class="wrap foot-grid">
  <div class="nap">
   {logo(root)}
   <p class="foot-desc">Certified {B['category']} in {B['city']}. Personal training, gym, MMA, aerobics and martial arts with Coach {B['coach']}.</p>
   <address>
    <strong>{B['name']}</strong><br>
    <span>{escape(address_line())}</span><br>
    <a href="tel:{B['phone_e164']}">{B['phone_display']}</a><br>
    <a href="mailto:{B['email']}">{B['email']}</a><br>
    <span>{B['hours']}</span>
   </address>
   <div class="socials">{soc}</div>
  </div>
  <div><h3>Training</h3><ul>{svc}</ul></div>
  <div><h3>Areas We Serve</h3><ul>{areas}</ul><h3 class="mt">More</h3><ul><li><a href="{root}videos.html">Training Videos</a></li><li><a href="{root}gallery.html">Gallery</a></li><li><a href="{root}faq.html">FAQ</a></li></ul></div>
 </div>
 <div class="wrap foot-bottom"><p>&copy; {date.today().year} {B['name']}, {B['city']}, Kenya. All rights reserved.</p></div>
</footer>
<a class="wa-float" href="{wa_link()}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><svg viewBox="0 0 24 24" width="28" height="28" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.3-.5 0-1 .2-3.3-.7-2.8-1.1-4.5-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.8s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .6l-.4.6-.4.4c-.1.2-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.2 1.4 2.5 1.5.3.2.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l1.9.9c.3.1.5.2.5.3.1.2.1.7-.1 1.3Z"/></svg></a>
<script src="{root}assets/main.js" defer></script>
</body>
</html>
"""


def crumbs_html(crumbs, root):
    items = []
    for i, (n, u) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            items.append(f'<li aria-current="page">{escape(n)}</li>')
        else:
            items.append(f'<li><a href="{root}{u or "index.html"}">{escape(n)}</a></li>')
    return f'<nav class="crumbs wrap" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'


def faq_html(faqs, heading="Frequently Asked Questions"):
    items = "".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in faqs)
    return f'<section class="section faq"><div class="wrap narrow"><h2>{heading}</h2>{items}</div></section>'


def map_html(query, title):
    src = B["map_embed"] if query is None else f"https://www.google.com/maps?q={quote(query)}&output=embed"
    return f'<div class="map"><iframe src="{src}" title="{escape(title)}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>'


def write(path, html):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)


def service_card(s, root):
    vk = VIDEO_FOR.get(s["slug"]) or []
    prev = f' data-preview="{root}videos/{VIDEOS[vk[0]][0]}.mp4"' if vk else ""
    play = '<span class="card-play" aria-hidden="true"></span>' if vk else ""
    return f"""<a class="cat-card" href="{root}services/{s['slug']}.html"{prev}>
 <span class="cat-media">{img_tag(s['img'], root)}{play}</span>
 <span class="cat-body"><span class="cat-chip">{icon(s['slug'])}</span><span class="cat-name">{s['name']}</span><span class="cat-blurb">{s['blurb']}</span><span class="cat-more">View {s['short']} &rarr;</span></span>
</a>"""


def category_tiles(root):
    return "".join(f'<a class="cat" href="{root}services/{s["slug"]}.html">{icon(s["slug"], "cat-ico")}<span>{s["short"]}</span></a>' for s in SERVICES)


def marquee():
    words = " &bull; ".join(s["short"].upper() for s in SERVICES)
    return f'<div class="marquee" aria-hidden="true"><div class="marquee-track"><span>{words} &bull; </span><span>{words} &bull; </span></div></div>'


# ---------------------------------------------------------------- pages
def page_home():
    root = ""
    title = (f"BEST Personal Trainer Nairobi | If you're looking for Gym Training, MMA, Aerobics, Calisthenics & Jeet Kune Do near me, "
             f"{B['name']} with Coach {B['coach']} is the place to be")
    meta = ("Certified personal trainer in Nairobi. Gym and weight training, MMA, aerobics, boxing, calisthenics, weight loss "
            "and kids martial arts with Coach Don Michael Ondiro. Book on WhatsApp.")
    general_faqs = FAQS[:5]
    showcase = ["squats", "mma_speed", "one_arm", "jkd_kicks"]
    schema = [business_schema(), coach_schema(), website_schema(), faq_schema(general_faqs)] + [video_schema(k) for k in showcase] + [
        {"@type": "WebPage", "@id": B["site_url"] + "/#webpage", "url": B["site_url"] + "/", "name": title,
         "isPartOf": {"@id": B["site_url"] + "/#website"}, "about": {"@id": business_id()}, "dateModified": TODAY}]
    cards = "".join(service_card(s, root) for s in SERVICES)
    areas = "".join(f'<li><a href="areas/{a["slug"]}.html">{a["name"]}</a></li>' for a in AREAS)
    vids = "".join(f'<div class="reel">{video_tag(k, root)}<a class="reel-tag" href="services/{VIDEO_CATEGORY[k]}.html">{SVC[VIDEO_CATEGORY[k]]["short"]}</a></div>' for k in showcase)
    body = f"""
<section class="hero hero-video">
 <video class="hero-bg" autoplay muted loop playsinline preload="metadata" poster="videos/push-up-variations-calisthenics-nairobi.jpg" aria-hidden="true">
  <source src="videos/hero-loop.mp4" type="video/mp4">
 </video>
 <div class="hero-shade"></div>
 <div class="wrap hero-grid">
  <div class="hero-copy">
   <p class="eyebrow">Certified Fitness &amp; Performance Coach &middot; Nairobi</p>
   <h1>Personal Trainer in Nairobi</h1>
   <p class="lead">Personal training, gym work, MMA, aerobics and martial arts with Coach {B['coach']}. One coach, a plan built for you, and sessions that move you forward every week.</p>
   <div class="hero-btns"><a class="btn" href="{wa_link()}" target="_blank" rel="noopener">Book on WhatsApp</a><a class="btn btn-ghost" href="#categories">See Training</a></div>
   <ul class="hero-stats"><li><b>12</b> training categories</li><li><b>6</b> Nairobi areas</li><li><b>JKD</b> &amp; MMA trained</li></ul>
  </div>
  <div class="hero-media">
   <div class="phone"><video autoplay muted loop playsinline preload="metadata" poster="videos/mma-striking-speed-drill-nairobi.jpg" aria-label="Coach Don MMA striking drill"><source src="videos/hero-loop-vertical.mp4" type="video/mp4"></video></div>
   <div class="badge-float">{LOGO_SVG}<span><b>Coach Don</b>Certified &middot; JKD &middot; MMA</span></div>
  </div>
 </div>
</section>
{marquee()}

<section class="section" id="categories">
 <div class="wrap">
  <div class="section-head split-head"><div><p class="eyebrow">Training Categories</p><h2>Gym, MMA, Aerobics &amp; More in Nairobi</h2></div><p>Pick a goal. Each one has its own plan and videos.</p></div>
  <div class="cat-grid">{cards}</div>
 </div>
</section>

<section class="section alt">
 <div class="wrap">
  <div class="section-head split-head"><div><p class="eyebrow">Watch</p><h2>Coach Don in Action</h2></div><a class="btn btn-ghost" href="videos.html">All videos</a></div>
  <div class="reel-row">{vids}</div>
 </div>
</section>

<section class="section">
 <div class="wrap split">
  <div class="duo">
   <div class="duo-a">{img_tag('portrait', root)}</div>
   <div class="duo-b">{img_tag('curl', root)}</div>
  </div>
  <div>
   <p class="eyebrow">Your Coach</p>
   <h2>Meet {B['coach']}</h2>
   <p>Don is a certified fitness and performance coach, a Jeet Kune Do and leisure MMA martial artist, and holds a BA in Economics. His students call him Sensei.</p>
   <p>His rule for training: repetition breeds mastery. Use your space, anywhere and anytime. You can see it on his Instagram, from one-arm push-ups to 100 push-ups a day.</p>
   <ul class="ticks"><li>Certified fitness and performance coach</li><li>Jeet Kune Do and MMA</li><li>Gym, calisthenics and conditioning</li></ul>
   <a class="btn btn-ghost" href="about.html">About Don</a>
  </div>
 </div>
</section>

<section class="section alt">
 <div class="wrap">
  <div class="section-head"><p class="eyebrow">Getting Started</p><h2>How Training Works</h2></div>
  <ol class="steps">
   <li><b>Message us</b><span>Send your goal, location and preferred times on WhatsApp.</span></li>
   <li><b>Assessment</b><span>Your first session checks movement, strength and fitness.</span></li>
   <li><b>Your plan</b><span>A programme built for you that progresses every week.</span></li>
   <li><b>Check-ins</b><span>Track strength, measurements and progress as you go.</span></li>
  </ol>
 </div>
</section>

<section class="section">
 <div class="wrap split split-top">
  <div>
   <p class="eyebrow">Areas We Serve</p>
   <h2>Personal Training Across Nairobi</h2>
   <p>{B['name']} trains clients across Nairobi, including:</p>
   <ul class="area-list cols">{areas}</ul>
   <a class="more" href="areas/index.html">All areas we serve &rarr;</a>
  </div>
  <div class="nap-card">
   <h3>{B['name']}</h3>
   <p>{escape(address_line())}<br><a href="tel:{B['phone_e164']}">{B['phone_display']}</a><br>{B['hours']}</p>
   {map_html(None, 'Map of ' + B['name'] + ' in Nairobi')}
  </div>
 </div>
</section>
{faq_html(general_faqs)}
"""
    write("index.html", head(title, meta, "", root, schema) + header(root, "home") + body + footer(root))


def page_about():
    root = ""
    title = f"About Coach {B['coach']} | Certified Personal Trainer & Jeet Kune Do Martial Artist in Nairobi | {B['name']}"
    meta = f"Meet {B['coach']}, certified fitness and performance coach, Jeet Kune Do and MMA martial artist, and founder of {B['name']} in Nairobi."
    crumbs = [("Home", ""), ("About", "about.html")]
    schema = [business_schema(), coach_schema(), breadcrumb_schema(crumbs), video_schema("gym_endurance"),
              {"@type": "AboutPage", "url": abs_url("about.html"), "name": title, "mainEntity": {"@id": B["site_url"] + "/#coach"}}]
    body = f"""{crumbs_html(crumbs, root)}
<section class="page-hero"><div class="wrap"><h1>About Coach {B['coach']}</h1><p class="lead">Certified personal trainer in Nairobi. Martial artist. Life in and around fitness.</p></div></section>
<section class="section">
 <div class="wrap split">
  <div class="split-media">{img_tag('portrait', root)}</div>
  <div>
   <h2>Who is Don Michael Ondiro?</h2>
   <p>Don Michael Ondiro is the coach behind {B['name']}. He is a certified fitness and performance coach, trains in Jeet Kune Do and leisure MMA, and holds a BA in Economics. He describes himself first as God-fearing, and his faith shows in the discipline and care he brings to coaching.</p>
   <p>On Instagram, Don shares his own training: one-arm push-ups on both sides, bare-knuckle push-up challenges, kicking drills and the "100 push-ups a day keeps your weakness away" habit. He trains the same way he coaches.</p>
  </div>
 </div>
</section>
<section class="section alt">
 <div class="wrap">
  <div class="section-head"><h2>Coaching Philosophy</h2></div>
  <div class="values">
   <div><h3>Repetition breeds mastery</h3><p>Small, consistent reps beat occasional heroic workouts. Use your space, anywhere and anytime.</p></div>
   <div><h3>Be your masterpiece</h3><p>Your only competition is who you were last month. Every programme is built around your own progress.</p></div>
   <div><h3>Take care of the temple</h3><p>"Both physical and spiritual endurance are gifts from God." Training is a way of caring for the body you've been given.</p></div>
   <div><h3>Necessary motivation</h3><p>Accountability and encouragement on the days you need it most.</p></div>
  </div>
 </div>
</section>
<section class="section">
 <div class="wrap split">
  <div>
   <h2>Qualifications &amp; Experience</h2>
   <ul class="ticks">
    <li>Certified Fitness and Performance Coach</li>
    <li>Jeet Kune Do martial artist</li>
    <li>Leisure MMA training</li>
    <li>BA in Economics</li>
    <li>Coaching clients in personal training, gym, MMA, aerobics, calisthenics and strength</li>
   </ul>
   <p>Ready to start? Explore our <a href="services/index.html">training categories in Nairobi</a>, watch <a href="videos.html">Don's training videos</a> or see the <a href="areas/index.html">areas we serve</a>.</p>
  </div>
  <div class="vid-single">{video_tag('gym_endurance', root)}</div>
 </div>
</section>
"""
    write("about.html", head(title, meta, "about.html", root, schema, og_img="portrait") + header(root, "about") + body + footer(root))


def page_services_index():
    root = "../"
    title = f"BEST Personal Training Services Nairobi | Gym, MMA, Aerobics, Boxing, Calisthenics, Weight Loss & Kids Martial Arts near me | {B['name']}"
    meta = "All training categories at D Dynamic Fitness in Nairobi: personal training, gym, MMA, aerobics, Jeet Kune Do, boxing, calisthenics, weight loss, group and kids classes."
    crumbs = [("Home", ""), ("Training", "services/index.html")]
    schema = [business_schema(), breadcrumb_schema(crumbs),
              {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": abs_url(f"services/{s['slug']}.html"), "name": s["name"]} for i, s in enumerate(SERVICES)]}]
    cards = "".join(service_card(s, root) for s in SERVICES)
    body = f"""{crumbs_html(crumbs, root)}
<section class="page-hero"><div class="wrap"><h1>Training Categories in Nairobi</h1><p class="lead">Gym, MMA, aerobics, martial arts and more. Find the programme that fits your goal.</p><div class="cats cats-sm">{category_tiles(root)}</div></div></section>
<section class="section"><div class="wrap"><div class="cat-grid">{cards}</div></div></section>
<section class="section alt"><div class="wrap narrow">
 <h2>Not sure which category is right for you?</h2>
 <p>Most clients combine two programmes, for example <a href="gym-training.html">gym training</a> with <a href="aerobics-cardio.html">aerobics</a>, or <a href="mma-training.html">MMA</a> with <a href="strength-conditioning.html">strength and conditioning</a>. Message Coach Don on WhatsApp with your goal and he will recommend a plan. We train clients across Nairobi; see <a href="../areas/index.html">all areas we serve</a>.</p>
</div></section>
"""
    write("services/index.html", head(title, meta, "services/index.html", root, schema) + header(root, "services") + body + footer(root))


def page_service(s):
    root = "../"
    path = f"services/{s['slug']}.html"
    crumbs = [("Home", ""), ("Training", "services/index.html"), (s["name"], path)]
    vkeys = VIDEO_FOR.get(s["slug"], [])
    schema = [business_schema(), service_schema(s), breadcrumb_schema(crumbs), faq_schema(s["faqs"])] + [video_schema(k) for k in vkeys]
    secs = s["sections"]
    sections = ""
    vid_done = False
    for h, html in secs:
        sections += f"<h2>{h}</h2>{html.format(root=root)}"
        if h.startswith("Watch") and vkeys:
            sections += f'<div class="vid-pair">{"".join(video_tag(k, root) for k in vkeys)}</div>'
            vid_done = True
    if vkeys and not vid_done:
        sections = (f'<h2>Watch: {s["short"]} in action</h2><p>Training footage from Coach Don in Nairobi.</p>'
                    f'<div class="vid-pair">{"".join(video_tag(k, root) for k in vkeys)}</div>') + sections
    served = [a for a in AREAS if s["slug"] in a["services"]]
    others = [a for a in AREAS if a not in served]
    area_links = served + others[: max(0, 5 - len(served))]
    a1 = served[0] if served else AREAS[0]
    area_sentence = (f'<p>We coach {s["short"].lower()} clients right across Nairobi, with many in '
                     f'<a href="../areas/{a1["slug"]}.html">{a1["name"]}</a> and nearby neighbourhoods.</p>')
    area_list = "".join(f'<li><a href="../areas/{a["slug"]}.html">{s["short"]} in {a["name"]}</a></li>' for a in area_links)
    rel_cards = "".join(service_card(o, root) for o in [x for x in SERVICES if x["slug"] != s["slug"]][:3])
    book = wa_link("Hi Coach Don, I am interested in " + s["name"] + ".")
    body = f"""{crumbs_html(crumbs, root)}
<section class="page-hero svc-hero"><div class="wrap svc-hero-grid"><div><p class="eyebrow">{icon(s['slug'], 'eyebrow-ico')} Training &middot; Nairobi</p><h1>{s['h1']}</h1><p class="lead">{s['blurb']}</p>
<div class="hero-btns"><a class="btn" href="{book}" target="_blank" rel="noopener">Book {s['short']}</a><a class="btn btn-ghost" href="tel:{B['phone_e164']}">Call {B['phone_display']}</a></div></div>
<figure class="svc-hero-img">{img_tag(s['img'], root, eager=True)}<span class="svc-hero-chip">{icon(s['slug'])}</span></figure></div></section>
<section class="section">
 <div class="wrap content-grid">
  <article class="prose">
   {''.join(f'<p>{p}</p>' for p in s['intro'])}
   {sections}
   <h2>{s['short']} across Nairobi</h2>
   {area_sentence}
   <h3>We also serve these areas</h3>
   <ul class="area-list">{area_list}</ul>
  </article>
  <aside class="side">
   <div class="nap-card">
    <h3>Book {s['short']}</h3>
    <p><strong>{B['name']}</strong><br>{escape(address_line())}<br><a href="tel:{B['phone_e164']}">{B['phone_display']}</a><br>{B['hours']}</p>
    <a class="btn btn-block" href="{book}" target="_blank" rel="noopener">WhatsApp Coach Don</a>
   </div>
   <div class="side-box"><h3>Other training</h3><ul>{''.join(f'<li><a href="{o["slug"]}.html">{o["short"]}</a></li>' for o in SERVICES if o["slug"] != s["slug"])}</ul></div>
  </aside>
 </div>
</section>
{faq_html(s['faqs'], s['short'] + ' FAQs')}
<section class="section alt"><div class="wrap"><div class="section-head"><h2>Other Training Categories</h2></div><div class="cat-grid">{rel_cards}</div></div></section>
"""
    write(path, head(s["title"], s["meta"], path, root, schema, og_img=s["img"]) + header(root, "services") + body + footer(root))


def page_areas_index():
    root = "../"
    title = f"Areas We Serve | BEST Personal Trainer in Westlands, Kilimani, Kileleshwa, Lavington, Karen & Parklands, Nairobi | {B['name']}"
    meta = "D Dynamic Fitness provides personal training, gym, MMA and aerobics coaching across Nairobi: Westlands, Kilimani, Kileleshwa, Lavington, Karen and Parklands."
    crumbs = [("Home", ""), ("Areas We Serve", "areas/index.html")]
    schema = [business_schema(), breadcrumb_schema(crumbs)]
    tiles = "".join(f"""<a class="area-tile" href="{a['slug']}.html"><h3>{a['name']}</h3><p>Near {a['landmarks']}</p><span>Personal training in {a['name']} &rarr;</span></a>""" for a in AREAS)
    main_svcs = "".join(f'<li><a href="../services/{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES[:5])
    body = f"""{crumbs_html(crumbs, root)}
<section class="page-hero"><div class="wrap"><h1>Personal Training Areas We Serve in Nairobi</h1><p class="lead">Coaching for clients across Nairobi's neighbourhoods. Choose your area to learn more.</p></div></section>
<section class="section"><div class="wrap"><div class="area-grid">{tiles}</div></div></section>
<section class="section alt"><div class="wrap split">
 <div><h2>Our Main Services</h2><ul class="area-list">{main_svcs}</ul></div>
 <div class="nap-card"><h3>Don't see your area?</h3><p>We work with clients all over Nairobi. Send your location on WhatsApp and we'll let you know how we can help.</p><a class="btn" href="{wa_link()}" target="_blank" rel="noopener">Ask on WhatsApp</a></div>
</div></section>
"""
    write("areas/index.html", head(title, meta, "areas/index.html", root, schema) + header(root, "areas") + body + footer(root))


def page_area(a):
    root = "../"
    path = f"areas/{a['slug']}.html"
    crumbs = [("Home", ""), ("Areas We Serve", "areas/index.html"), (a["name"], path)]
    svcs = [SVC[k] for k in a["services"]]
    title = f"BEST Personal Trainer {a['name']} Nairobi | {svcs[0]['short']}, {svcs[3]['short']} & {svcs[1]['short']} near me | {B['name']}"
    meta = f"Looking for a personal trainer in {a['name']}, Nairobi? Coach Don Michael Ondiro offers {svcs[0]['short'].lower()}, {svcs[3]['short'].lower()}, {svcs[1]['short'].lower()} and more near {a['landmarks'].split(',')[0]}."
    faqs = a["faqs"] + [FAQS[3], FAQS[4]]
    vkey = AREA_VIDEO[a["slug"]]
    area_svc = {"@type": "Service", "name": f"Personal training in {a['name']}, Nairobi", "provider": {"@id": business_id()},
                "areaServed": {"@type": "Place", "name": f"{a['name']}, Nairobi, Kenya"}, "url": abs_url(path), "serviceType": "Personal training"}
    schema = [business_schema(), area_svc, breadcrumb_schema(crumbs), faq_schema(faqs), video_schema(vkey)]
    svc_text = (f'<p>Want quick, structured workouts? See our <a href="../services/{svcs[0]["slug"]}.html">{svcs[0]["name"].lower()}</a>. '
                f'Prefer something different? Many {a["name"]} clients enjoy <a href="../services/{svcs[3]["slug"]}.html">{svcs[3]["short"].lower()}</a> too.</p>')
    svc_list = "".join(f'<li><a href="../services/{s["slug"]}.html">{s["name"]} in {a["name"]}</a></li>' for s in svcs)
    svc_list += '<li><a href="../services/index.html">All training categories</a></li>'
    other_areas = "".join(f'<li><a href="{o["slug"]}.html">{o["name"]}</a></li>' for o in AREAS if o["slug"] != a["slug"])
    extra = "".join(f"<h2>{h}</h2>{html.format(root=root)}" for h, html in a["sections"])
    book = wa_link("Hi Coach Don, I live in " + a["name"] + " and would like to book a session.")
    body = f"""{crumbs_html(crumbs, root)}
<section class="page-hero"><div class="wrap"><p class="eyebrow">Areas We Serve &middot; Nairobi</p><h1>Personal Trainer in {a['name']}, Nairobi</h1><p class="lead">Certified coaching for {a['name']} residents, near {a['landmarks']}.</p>
<div class="hero-btns"><a class="btn" href="{book}" target="_blank" rel="noopener">Book in {a['name']}</a></div></div></section>
<section class="section">
 <div class="wrap content-grid">
  <article class="prose">
   <p>{a['intro']}</p>
   <h2>Fitness Coaching for {a['name']} Residents</h2>
   <p>{a['local']}</p>
   {svc_text}
   <h2>Services We Offer in {a['name']}</h2>
   <ul class="area-list">{svc_list}</ul>
   {extra}
   <h2>Why {a['name']} Locals Choose {B['name']}</h2>
   <ul class="ticks">
    <li>Certified fitness and performance coach with martial arts experience</li>
    <li>Programmes built around your goal, schedule and current fitness</li>
    <li>Gym, MMA, aerobics, calisthenics and Jeet Kune Do under one coach</li>
    <li>Simple nutrition guidance using food you already eat</li>
    <li>Fast replies on WhatsApp to book and reschedule</li>
   </ul>
   <h2>Watch a Session</h2>
   <div class="vid-single">{video_tag(vkey, root)}</div>
   <h2>Training Near {a['landmarks'].split(',')[0]}</h2>
   <p>We work with clients living and working around {a['landmarks']}. Send your location when you book and we'll confirm the most convenient training option for you in {a['name']}.</p>
   {map_html(a['name'] + ', Nairobi, Kenya', 'Map of ' + a['name'] + ', Nairobi')}
  </article>
  <aside class="side">
   <figure class="side-img">{img_tag(svcs[0]['img'], root)}</figure>
   <div class="nap-card"><h3>{B['name']}</h3><p>{escape(address_line())}<br><a href="tel:{B['phone_e164']}">{B['phone_display']}</a><br>{B['hours']}</p>
   <a class="btn btn-block" href="{book}" target="_blank" rel="noopener">WhatsApp Coach Don</a></div>
   <div class="side-box"><h3>Other areas we serve</h3><ul>{other_areas}</ul></div>
  </aside>
 </div>
</section>
{faq_html(faqs, 'Personal Training in ' + a['name'] + ': FAQs')}
"""
    write(path, head(title, meta, path, root, schema, og_img=svcs[0]["img"]) + header(root, "areas") + body + footer(root))


def page_videos():
    root = ""
    title = f"Training Videos | Watch MMA, Jeet Kune Do, Calisthenics & Gym Workouts with a Nairobi Personal Trainer | {B['name']}"
    meta = "Watch Coach Don Michael Ondiro's training videos from Nairobi: MMA striking, Jeet Kune Do kicks, one-arm push-ups, gym workouts and partner challenges."
    crumbs = [("Home", ""), ("Videos", "videos.html")]
    schema = [business_schema(), breadcrumb_schema(crumbs)] + [video_schema(k) for k in VIDEOS]
    groups = ""
    for s in SERVICES:
        keys = [k for k, c in VIDEO_CATEGORY.items() if c == s["slug"]]
        if not keys:
            continue
        reels = "".join(f'<div class="reel" id="{VIDEOS[k][0]}">{video_tag(k, root)}</div>' for k in keys)
        groups += (f'<div class="vid-group span{len(keys)}"><div class="vid-group-head">{icon(s["slug"], "cat-ico")}'
                   f'<h2><a href="services/{s["slug"]}.html">{s["short"]}</a></h2></div><div class="vid-group-reels">{reels}</div></div>')
    body = f"""{crumbs_html(crumbs, root)}
<section class="page-hero"><div class="wrap"><h1>Personal Training Videos from Nairobi</h1><p class="lead">Training footage from Coach Don, sorted by category. New videos every week on <a href="{B['instagram']}" target="_blank" rel="noopener">@d_dynamicfitness_</a>.</p></div></section>
<section class="section"><div class="wrap"><div class="vid-groups">{groups}</div></div></section>
"""
    write("videos.html", head(title, meta, "videos.html", root, schema) + header(root, "videos") + body + footer(root))


def page_gallery():
    root = ""
    title = f"Training Gallery | Personal Trainer Nairobi Photos: Gym, MMA, Calisthenics & Boxing | {B['name']}"
    meta = "Photos from D Dynamic Fitness training sessions in Nairobi: gym training, MMA and boxing pad work, calisthenics, Jeet Kune Do and mobility."
    crumbs = [("Home", ""), ("Gallery", "gallery.html")]
    schema = [business_schema(), breadcrumb_schema(crumbs),
              {"@type": "ImageGallery", "name": "D Dynamic Fitness training gallery", "url": abs_url("gallery.html"),
               "image": [{"@type": "ImageObject", "contentUrl": abs_url("images/" + IMG[k][0]), "caption": IMG[k][1]} for k in GALLERY]}]
    figs = "".join(f'<figure>{img_tag(k, root)}</figure>' for k in GALLERY)
    body = f"""{crumbs_html(crumbs, root)}
<section class="page-hero"><div class="wrap"><h1>Personal Training Gallery, Nairobi</h1><p class="lead">Real sessions and challenges from Coach Don and his clients. Prefer moving pictures? <a href="videos.html">Watch the training videos</a>.</p></div></section>
<section class="section"><div class="wrap"><div class="gallery">{figs}</div></div></section>
"""
    write("gallery.html", head(title, meta, "gallery.html", root, schema, og_img="kick") + header(root, "gallery") + body + footer(root))


def page_faq():
    root = ""
    title = f"FAQ | Personal Training in Nairobi: Prices, Booking, Gym, MMA, Aerobics & Areas | {B['name']}"
    meta = "Answers to common questions about training with D Dynamic Fitness in Nairobi: booking, gym, MMA, aerobics, kids classes, areas, beginners and pricing."
    crumbs = [("Home", ""), ("FAQ", "faq.html")]
    all_faqs = FAQS + [f for s in SERVICES for f in s["faqs"][:1]]
    schema = [business_schema(), breadcrumb_schema(crumbs), faq_schema(all_faqs)]
    body = f"""{crumbs_html(crumbs, root)}
<section class="page-hero"><div class="wrap"><h1>Personal Training FAQs, Nairobi</h1><p class="lead">Everything you need to know before your first session.</p></div></section>
{faq_html(all_faqs, 'Your Questions Answered')}
<section class="section alt"><div class="wrap narrow center"><p>Still have a question? <a href="contact.html">Contact us</a> or browse our <a href="services/index.html">training categories</a>.</p></div></section>
"""
    write("faq.html", head(title, meta, "faq.html", root, schema) + header(root, "faq") + body + footer(root))


def page_contact():
    root = ""
    title = f"Contact {B['name']} | Book a Personal Trainer in Nairobi | Call or WhatsApp {B['phone_display']}"
    meta = f"Book a session with {B['coach']}, personal trainer in Nairobi. Call or WhatsApp {B['phone_display']}, or send a message through the contact form."
    crumbs = [("Home", ""), ("Contact", "contact.html")]
    schema = [business_schema(), breadcrumb_schema(crumbs),
              {"@type": "ContactPage", "url": abs_url("contact.html"), "name": title, "about": {"@id": business_id()}}]
    opts = "".join(f"<option>{s['name']}</option>" for s in SERVICES)
    area_opts = "".join(f"<option>{a['name']}</option>" for a in AREAS)
    areas = "".join(f'<li><a href="areas/{a["slug"]}.html">{a["name"]}</a></li>' for a in AREAS)
    main_svcs = "".join(f'<li><a href="services/{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES[:4])
    body = f"""{crumbs_html(crumbs, root)}
<section class="page-hero"><div class="wrap"><h1>Contact a Personal Trainer in Nairobi</h1><p class="lead">Tell us your goal and we'll reply on WhatsApp to arrange your first session.</p></div></section>
<section class="section">
 <div class="wrap split split-top">
  <form class="contact-form" id="contact-form" data-wa="{B['phone_e164'].lstrip('+')}">
   <label>Your name<input name="name" required autocomplete="name"></label>
   <label>Training category<select name="service">{opts}<option>Not sure yet</option></select></label>
   <label>Area<select name="area">{area_opts}<option>Other part of Nairobi</option></select></label>
   <label>Your goal<textarea name="goal" rows="4" placeholder="e.g. lose 8 kg, learn MMA, first pull-up"></textarea></label>
   <button class="btn" type="submit">Send via WhatsApp</button>
  </form>
  <div>
   <div class="nap-card">
    <h2>{B['name']}</h2>
    <p>Coach {B['coach']}<br>{escape(address_line())}<br>Phone: <a href="tel:{B['phone_e164']}">{B['phone_display']}</a><br>Email: <a href="mailto:{B['email']}">{B['email']}</a><br>Hours: {B['hours']}</p>
    {map_html(None, 'Map of ' + B['name'] + ' in Nairobi')}
   </div>
   <h3>Areas we serve</h3><ul class="area-list cols">{areas}</ul>
   <h3>Our main services</h3><ul class="area-list">{main_svcs}</ul>
  </div>
 </div>
</section>
"""
    write("contact.html", head(title, meta, "contact.html", root, schema) + header(root, "contact") + body + footer(root))


def page_404():
    root = BASE_PATH
    body = f"""<section class="page-hero"><div class="wrap center"><h1>Page Not Found</h1><p class="lead">That page has moved or doesn't exist. Try one of these instead:</p>
<div class="hero-btns" style="justify-content:center"><a class="btn" href="{root}index.html">Home</a><a class="btn btn-ghost" href="{root}services/index.html">Training</a><a class="btn btn-ghost" href="{root}contact.html">Contact</a></div></div></section>"""
    html = head(f"Page not found | {B['name']}", "This page could not be found.", "404.html", root, [website_schema()])
    html = html.replace('content="index, follow, max-image-preview:large, max-video-preview:-1"', 'content="noindex, follow"')
    write("404.html", html + header(root) + body + footer(root))


def sitemap_and_robots():
    pages = {"": ["mma_speed", "one_arm", "jkd_kicks", "hundred"], "about.html": ["gym_endurance"], "services/index.html": []}
    for s in SERVICES:
        pages[f"services/{s['slug']}.html"] = VIDEO_FOR.get(s["slug"], [])
    pages["areas/index.html"] = []
    for a in AREAS:
        pages[f"areas/{a['slug']}.html"] = [VIDEO_FOR[a["services"][0]][0]]
    pages.update({"videos.html": list(VIDEOS), "gallery.html": [], "faq.html": [], "contact.html": []})
    urls = ""
    for p, vk in pages.items():
        v = ""
        for k in vk:
            stem, t, d, up, dur, _ = VIDEOS[k]
            m = re.match(r"PT(?:(\d+)M)?(?:(\d+)S)?", dur)
            secs = int(m.group(1) or 0) * 60 + int(m.group(2) or 0)
            v += (f"<video:video><video:thumbnail_loc>{abs_url('videos/' + stem + '.jpg')}</video:thumbnail_loc>"
                  f"<video:title>{escape(t)}</video:title><video:description>{escape(d)}</video:description>"
                  f"<video:content_loc>{abs_url('videos/' + stem + '.mp4')}</video:content_loc>"
                  f"<video:duration>{secs}</video:duration>"
                  f"<video:publication_date>{up}T12:00:00+03:00</video:publication_date></video:video>")
        urls += f"<url><loc>{abs_url(p)}</loc><lastmod>{TODAY}</lastmod>{v}</url>\n"
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
          f'xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">\n{urls}</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {B['site_url']}/sitemap.xml\n")
    return len(pages)


if __name__ == "__main__":
    page_home()
    page_about()
    page_services_index()
    for s in SERVICES:
        page_service(s)
    page_areas_index()
    for a in AREAS:
        page_area(a)
    page_videos()
    page_gallery()
    page_faq()
    page_contact()
    page_404()
    n = sitemap_and_robots()
    print(f"Built {n} pages (+404) into {OUT}")
