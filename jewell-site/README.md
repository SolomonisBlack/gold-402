# Jewell Services Website

A multi-page, mobile-first website for Jewell Services, a family-owned handyman and remodeling business serving all of Iowa. It's static HTML/CSS/JS, plus a small PHP script that emails estimate requests, so it runs on any Hostinger plan.

- `dist/`: the finished site. **Upload the contents of this folder to `public_html`.**
- `build.py`: generates `dist/` from the page content (run `python3 build.py`; needs Python 3 and Pillow)
- `src/`: CSS, JS, fonts, and `send.php` (the form handler)
- `assets/img/`: Jewell's real photos (`work/`), logo (`brand/`), and licensed stock photos (`stock/`; see `stock/CREDITS.md`)
- `PLAN.md`: the original site plan

## Pages (18)
Home · Services · 8 service pages (TV mounting and smart home, flooring, kitchen and bath, electrical, painting and drywall, exterior, repairs and assembly, lawn, snow, and hauling) · Commercial · About · Our Work (gallery) · Service Area · Contact / Free Estimate · Thank you · Privacy · 404

## Deploy to Hostinger
1. hPanel → **Websites** → your site (a free temporary domain like `something.hostingersite.com` works for review).
2. **File Manager** → `public_html` → delete the default placeholder files.
3. Upload **everything inside `dist/`**, including the hidden `.htaccess` file. Some FTP and zip tools skip dotfiles, so check that it's there.
4. To test the contact form: hPanel → **Emails** → create the mailbox `website@<your-domain>`, then set `LEAD_FROM` in `send.php` to match.

Hostinger API or MCP deploy: the `hosting_deployStaticSiteArchiveV1` tool takes a zip of the **contents** of `dist/` (no wrapping folder).

### Review build vs. launch build
The committed `dist/` is a **review build** (`STAGING=1`): every page is `noindex`, and robots.txt blocks crawlers so the temporary domain doesn't end up in Google. **Before launch** on jewell-services.com:
```bash
python3 build.py          # production build: indexable, with sitemap
```

## Before launch: things only the owner can confirm
- [ ] **Lead email**: `send.php` currently sends to a testing inbox. Change `LEAD_TO` to Jewell's email.
- [ ] **Licensing**: the site says "licensed and insured" (from their current site). Confirm which licenses they hold, especially for electrical work.
- [ ] **Home city / base location**: add it to the topbar, footer, and schema (better local search ranking).
- [ ] **Owner and family names** for the About page, plus a short note from the owner.
- [ ] **Real reviews**: none were available, so none are shown (nothing was made up). Set up a Google Business Profile, ask happy customers for reviews, and then add a reviews section.
- [ ] **More finished-job photos**, especially kitchens and bathrooms. These pages currently use licensed stock photos, with no "our work" captions on them.
- [ ] Answers for common questions: how soon you can come out, trip fees outside the metro, payment methods.
- [ ] Google Analytics 4 / Google Ads tag (the site already fires `generate_lead`, `click_to_call`, and `click_to_text` events once a tag is added).

## Conversion features
- Click-to-call and "text us a photo" (prefilled text message) on every page, plus a sticky mobile action bar
- Short estimate form on the home page, every service page, and the commercial page; full form with photo upload on Contact
- Service pages preselect the service. `?offer=single-mom` pre-checks the 10% discount.
- Trust signals: licensed and insured, 1-year warranty, price match, family owned, 10+ years
- Real project photos with a tap-to-enlarge gallery
- If the form can't send, visitors get a call/text fallback with their details prefilled, so no lead is lost

## Form handling (send.php)
Emails each request (with up to 5 photos, resized in the browser first) and keeps a private backup log outside `public_html` when possible. Spam protection: hidden honeypot field, minimum fill-time check, same-site check, and a per-IP rate limit. Suspected spam is logged, not deleted.
