# D Dynamic Fitness: website

A static site for Coach Don Michael Ondiro (@d_dynamicfitness_), personal trainer in Nairobi. It follows the ProfResults local SEO playbook.

## Edit, then rebuild
1. Open `build.py` and fill in every `PLACEHOLDER` in `BUSINESS`: phone, email, domain, hours, Facebook URL, and street address (if there is a gym). These values must match the Google Business Profile exactly.
2. Swap `map_embed` for the GBP's own embed URL once the profile exists.
3. Confirm the services and areas with the client before launch. Copy lives in:
   - `content.py`: original services, areas, FAQs, images
   - `content_extra.py`: long-form sections for the original services and areas
   - `content_more.py`: the newer categories, the video library, which videos appear on which page, and category order
   - `CATEGORY_IMG` in `content.py`: the main photo for each category
4. Run `python build.py`. All pages, the schema, `sitemap.xml` (with video entries) and `robots.txt` are regenerated.

## Site map (26 pages + 404)
- Home, About, Videos, Gallery, FAQ, Contact
- 12 training categories under `/services/`:
  - Personal Training, Gym & Weight Training, MMA, Aerobics & Cardio
  - Jeet Kune Do, Boxing & Kickboxing, Calisthenics, Weight Loss
  - Strength & Conditioning, Group & Partner, Kids & Teens, Mobility
- 6 area pages under `/areas/`: Westlands, Kilimani, Kileleshwa, Lavington, Karen, Parklands

## Brand
- `assets/logo-mark.svg`: logo mark (a "D" with a lightning bolt and speed lines). Also used as `favicon.svg`.
- `assets/logo-mark-512.png`: used as the logo in the schema. `apple-touch-icon.png`.
- `assets/og-image.jpg`: 1200×630 social share card.

## Videos
There are 11 Instagram reels in `/videos/`, re-encoded to 720p H.264 (about 97 MB total), each with a poster image. Ten are Coach Don's own; the squat session was posted by his client @valen_qalen_fit and tags him.
- `VIDEO_FOR` in `content_more.py` decides which videos appear on each category page, and `VIDEO_CATEGORY` decides where each one sits on the Videos page. Kids & Teens and Mobility have no matching footage yet, so they use photos until the client sends videos.
- On desktop, hovering a category card plays a muted preview of that category's video.
- Players use `preload="none"`, so a reel only downloads when someone presses play.
- The hero uses two short muted loops: `hero-loop.mp4` (2.5 MB) and `hero-loop-vertical.mp4` (0.7 MB).
- Every video has VideoObject schema and an entry in the video sitemap.
- If hosting bandwidth matters, put the videos on a CDN, or on YouTube and embed them from there.

## On-page SEO (from the playbook)
- **Titles:** BEST + category + city + services + near me. **H1:** category + city. **H2s:** services.
- **NAP:** in every footer, plus a NAP card and an embedded map on Home and Contact.
- **Schema (JSON-LD):**
  - LocalBusiness with areaServed, an OfferCatalog and the founder as a Person
  - WebSite, Service, BreadcrumbList and FAQPage
  - VideoObject, ImageGallery, AboutPage and ContactPage
- **Interlinking:** service pages link to areas and area pages link to services. Home and Contact link to all areas and the main services.

## Not included on purpose
- No reviews or ratings. There are none to cite yet, so nothing was invented.
- Main article copy is about 420–960 words per service page and about 500–550 per area page, plus the FAQs. The playbook's advanced target is 1,000–2,000 for services and 1,200–2,200 for areas. Add more if the site can't reach the top 3.

## Validate after deploy
- https://validator.schema.org/
- Google Search Console: submit `/sitemap.xml`
