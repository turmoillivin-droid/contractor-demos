---
name: contractor-lead-engine
description: >-
  Lead generation, automated demo site creation, and community group marketing playbook for tradespeople and contractors in South Africa. Use when researching trade businesses on Facebook, building contractor landing pages with WhatsApp quote calculators, or executing social media group distribution campaigns.
---

# Contractor Lead Engine & Digital Partner Playbook

This skill provides the end-to-end operational runbook for acquiring local trade contractors (builders, tilers, plasterers, roofers, painters) in South Africa, building instant high-converting mobile demos, and retaining them on monthly lead generation contracts.

---

## The 4-Stage Operating Pipeline

```
[1. Prospecting] ──▶ [2. Fast Demo Build] ──▶ [3. Direct WhatsApp Hook] ──▶ [4. Retainer Upsell]
   Scan FB Groups       5-Min Mobile Site        Personalized Video/Link        1.5M+ Group Poster
```

---

## 1. Candidate Prospecting & Vetting Across All 9 Provinces

Target Facebook trade and local business groups in any of South Africa's 9 provinces. Use the national directory: [references/national_provinces_facebook_rolodex.md](./references/national_provinces_facebook_rolodex.md).

### Provincial Demand Patterns:
- **Gauteng (GP):** Tiling, bricklaying, boundary walls, patio & room extensions, estate modernizations.
- **Western Cape (WC):** Coastal damp proofing, roof waterproofing, high-end tiling, heritage exterior paint.
- **KwaZulu-Natal (KZN):** Rust treatment, damp sealing, retaining walls, timber decking, roof repairs.
- **Eastern Cape (EC):** Weather-coat painting, roofing, home building, plumbing.
- **Mpumalanga & Limpopo:** Foundation-to-roof home construction, durable ceramic tiling, plastering.
- **North West & Free State:** Bricklaying, paving, student/townhouse additions, roof insulation.
- **Northern Cape:** Thermal masonry insulation, heat-reflective coatings, roofing.

---

## 2. Instant Demo Site Generation

Do not sell a concept; generate the completed mobile site **before** contacting them.

### Running the Generator Script:
Use the bundled Python generator to create a complete, styled HTML page with an interactive WhatsApp quote calculator:

```bash
python3 .agents/skills/contractor-lead-engine/scripts/generate_demo.py \
  --name "Molise Construction & Tiling" \
  --owner "Maiketso" \
  --phone "0632550626" \
  --alt-phone "0670917772" \
  --city "Centurion" \
  --province "Gauteng" \
  --services "Ceramic Tiling, House Building, Smooth Plastering, Painting" \
  --output "demo-molise-construction/index.html"
```

### Essential Features Every Contractor Site Must Have:
1. **Interactive WhatsApp Quote Calculator:** Form letting homeowners select trade, enter suburb, and tap to auto-open WhatsApp with a formatted quote request.
2. **Trust Badges:** Experience years, own tools/transport guarantee, clear upfront pricing.
3. **Sticky/Floating WhatsApp Button:** Pulsing button in bottom-right corner for mobile users.
4. **Local Suburb Badges:** Explicitly naming nearby target suburbs.

---

## 3. High-Converting WhatsApp Outreach

Contractors live on WhatsApp. Generic spam flyers get blocked; sending a personalized finished preview gets responses.

### WhatsApp Pitch Template:
```text
Dumelang / Hello [Owner Name],

I saw your recent work and flyer in the [Group Name] group for [Business Name]. Great work on your recent [Trade/Service] projects around [Area].

I noticed you don’t currently have a dedicated link to showcase your work when quoting residential clients or estate homeowners who ask for proof of past jobs.

I put together a clean 1-page mobile website preview for [Business Name] so you can see how it looks:
👉 [Paste Live Demo URL]

It includes:
- Your core services ([Service 1], [Service 2], [Service 3])
- An instant "Quote on WhatsApp" button that connects directly to your [Phone Number]
- Your service areas across [Target Suburbs]

If you like how it looks and want to keep it live to help you close more quotes, let me know! No pressure at all.
```

---

## 4. Problem-to-Price Menu & Closing Packages

When they reply, position yourself as their complete **Internet & Marketing Partner**:

| Package | Scope | Price (ZAR) |
| :--- | :--- | :--- |
| **Starter Pack** | Mobile 1-page site + Google Maps (GBP) pin + 1 flyer | **R1,999 once-off** |
| **Group Lead Retainer** | Scheduled posting to 15+ Gauteng groups 3x/week | **R1,500 / month** |
| **All-in-One Partner** | Site + Google Maps + Domain + Weekly Group Leads | **R2,500 setup + R1,800/mo** |

See [references/pricing_menu.md](./references/pricing_menu.md) for full a la carte pricing.

---

## 5. Group Distribution & Safe Posting Rules

Use the vetted 24-group rolodex with **1,500,000+ members** across Centurion, Pretoria East, Sandton, Randburg, Midrand, and Edenvale. Full list with URLs: [references/gauteng_facebook_groups_rolodex.md](./references/gauteng_facebook_groups_rolodex.md).

### Meta Anti-Ban Safety Rules:
- **Maximum Volume:** Post to 3–5 groups in the morning (7:00 AM – 8:30 AM) and 3–5 in the late afternoon (5:00 PM – 6:30 PM).
- **Random Delay:** Insert a 4 to 8-minute random delay between posts.
- **Caption Variations:** Rotate 3 different headlines (e.g. Focus on Tiling vs. Focus on Renovations).
- **Source Tracking:** Always use suburb-tagged WhatsApp links (`wa.me/27...?text=Hi, saw your post in the Sandton group...`).

---

## 7. Short-Form Video Marketing Engine (TikTok, IG Reels & YouTube Shorts)

Trades are highly visual and addictive to watch on short-form video. Homeowners in South Africa respond heavily to cost transparency and aesthetic transformations.

See the complete playbook: [references/multi_platform_video_playbook.md](./references/multi_platform_video_playbook.md).

### Generating Multi-Platform Video Scripts & Captions:
Run the video script generator to get exact hooks, on-screen text, voiceovers, and hashtags:
```bash
python3 .agents/skills/contractor-lead-engine/scripts/generate_video_script.py \
  --name "Molise Construction & Tiling" \
  --trade "Ceramic Floor Tiling" \
  --city "Centurion" \
  --phone "0632550626" \
  --project "50sqm porcelain lounge tiling" \
  --cost "R6,800"
```

### The "Shoot Once, Distribute Everywhere" Retainer Upsell:
- Contractor films 15–30 seconds of on-site work with their phone and sends via WhatsApp.
- You format and post across **TikTok**, **Instagram Reels**, and **YouTube Shorts**.
- Upsell as the **Omni-Channel Lead Tier** (R2,800 – R3,500/month).
