# Project Memory & Context: Contractor Lead Generation & Marketing Automation

## Overview & Business Context
- **Market / Focus:** Local construction companies, tradespeople (tilers, builders, plasterers, roofers, painters) across **all 9 provinces of South Africa** (Gauteng, Western Cape, KwaZulu-Natal, Eastern Cape, Free State, Mpumalanga, Limpopo, North West, Northern Cape).
- **Contractor Hunting Grounds (1.2M+ Tradespeople):** Compiled in `.agents/skills/contractor-lead-engine/references/contractor_hunting_grounds_rolodex.md` covering 20 top groups dedicated exclusively to builders, tilers, plumbers, electricians, and subcontractors (e.g. *ABAKHI BEZINDLU* 542k members, *Building And Construction Jobs* 187k members, *Tenders & RFQ SA* 136k members).
- **National Homeowner Rolodex (5.4M+ Combined):** Compiled in `.agents/skills/contractor-lead-engine/references/national_provinces_facebook_rolodex.md` across all 9 provinces for client lead distribution.

## Key Learnings & Strategy
1. **Demand vs. Supply in Trade Groups:**
   - There are **0 inbound requests** asking for website developers in these trade groups.
   - 7+ freelance web designers post generic promotional flyers (R999 - R2,500) into the groups, which receive 0 engagement due to pitch fatigue and contractor skepticism.
   - Public group posting fails; personalized outbound direct outreach (especially on **WhatsApp**) with upfront value is the high-converting strategy.

2. **Lead Generation Workflow:**
   - Scan contractor posts for project photos, phone/WhatsApp numbers, and lack of an active website.
   - Build a custom, mobile-first 1-page landing page preview with a direct "Quote on WhatsApp" button, trust badges, and their real service breakdown.
   - Send a low-friction, personalized WhatsApp/email showing the preview with no upfront obligation.

3. **Active Contractor Demos & Pipeline (20 Verified Leads Across 5 Provinces):**
   - Deep search audit verified 100% of these 20 active contractors have **zero website, no domain, and no directory presence**:
     1. **Murendeni Ratombo** (`076 284 5600`) — Ratombo Construction (Pretoria / Centurion, GP — NHBRC Luxury Estates).
     2. **Lethabo Rapanyane** (`078 948 1786`) — Raboshabane Trading (Johannesburg, GP — Double-Storey Masonry).
     3. **Maiketso Maiketso** (`063 255 0626`) — Molise Construction (Centurion, GP — Tiling & Building).
     4. **Bigboy Chinhema** (`065 624 7288`) — B.C Gutters & Steel (East Rand, GP — Gutters & Carports).
     5. **M&M Projects** (`064 845 4885`) — M&M Developments (Pretoria, GP — Structural & Plumbing).
     6. **Brian Simanyandi** (`069 422 5882`) — Simanyandi Tiling (East London, EC — Porcelain Flooring).
     7. **Mandla Sky Zulu** (`084 049 0448`) — Nozaphi Construction (Durban, KZN — 3D Plans & Turnkey).
     8. **Chenge Methusi** (`079 859 9613`) — Mchenge Electrical & Painting (Mount Frere, EC — DB Boards & Wiring).
     9. **Tsupha Thala** (`073 172 1468`) — Bafokeng Plumbing Maintenance (Rustenburg, NW — JoJo Tanks & Plumbing).
     10. **RoofGlow Team** (`062 385 2941`) — RoofGlow Property Care (Cape Town, WC — Roof Pressure Washing & UV Coating).
     11. **Thol'nhlanhla Maduna** (`083 631 2417`) — Maduna Built Ins (Durban, KZN — Fitted Kitchens & Wardrobes).
     12. **Sibusiso Maramb** (`064 961 6669`) — BM Aluminum & Steel (King William's Town, EC — Windows & Gates).
     13. **Samukeliso Manana** (`084 273 4383`) — SKWE-BUILD Construction (Ekangala, GP — Torch-On Waterproofing).
     14. **Lucky Nkuna** (`063 420 1160`) — Lucky Nkuna Plastering (Johannesburg, GP — Rhinolite & Gamazine).
     15. **Freeman Sifiso Ndimande** (`072 074 0051`) — Aqua Masters Plumbing Solution (Umlazi / Durban, KZN — Copper Reticulation & Cisterns).
     16. **Cpheh Mvelase** (`081 660 9750`) — Cpheh Mvelase Ceilings & Bulkheads (Adams Mission / Durban, KZN — Rhinoboard & Bulkheads).
     17. **Casper Mk Ndlovu** (`081 430 1227`) — Mlingo Projects & Paving (Durban, KZN — Tar Surfacing & Interlocking Paving).
     18. **Blessed Mhirimo** (`084 546 3534`) — Blessed Mhirimo Campus Building (East London, EC — Turnkey House Building & Roofing).
     19. **Senalorh Mthethwa** (`072 538 8371`) — Senalorh Mthethwa Electrical (Durban, KZN — DB Boards & House Conduit Wiring).
     20. **Vuyolwethu Hlazo** (`073 387 2140`) — Vuyolwethu Hlazo Fencing (Mthatha / Engcobo, EC — Diamond Mesh & Treated Timber Fencing).
   - **Ready Deployment Packages:** All 20 sites packaged into clean root-level `.zip` archives ready for drag-and-drop hosting on Tiiny.host / Surge / Netlify.
   - **Vault Status:** Fully synced inside `contractor-crm-vault/` (Pipeline Tracker, Leads, Demos Index, Home Dashboard, Playbooks).

4. **Strict 4-Pillar Jev Lead Qualification Protocol:**
   - **Pillar 1: Strict No-Website Verification (Zero False Positives):**
     - FB Intro: "Website" field must be blank (or only social link) + free email (@gmail/@yahoo). Custom domain email (`@company.co.za`) = auto-reject.
     - Google SERP Page 1: Search `"Business Name" + City`. Must show 0 owned `.co.za` or `.com` domain on Page 1.
   - **Pillar 2: Social-Proof Rich & High Inbound Intent:**
     - Pinned service menu, price list, or active homeowner comments asking *"How much?"*, *"Please inbox"*, *"Do you work in [Suburb]?"*.
     - Or Google Business Profile (Maps pin) with 3+ reviews but NO website button.
   - **Pillar 3: Cash-Flow Signals (Must Have 2+ Required):**
     - Sign-written fleet (bakkies, trucks, trailers).
     - Uniformed crew (2+) / scaffolding / industrial machinery.
     - Modern architectural / residential estate project markers.
     - Facebook page longevity > 12 months with steady multi-season posts.
   - **Pillar 4: Demo-Ready Brand Assets:**
     - Clean graphic logo or company badge (no blurry selfies or generic clipart).
     - 3–5 bright, daytime, wide-angle photos of completed work (no messy rubble/trenches).
     - Owner's first name identified for personal WhatsApp outreach.
   - **Automated Evaluator:** Script at `.agents/skills/contractor-lead-engine/scripts/jev_contractor_evaluator.py`.

5. **Product / Tool Roadmap & Assets:**
   - **Vetted Group Rolodex (1.5M+ Members):** Compiled in `docs/gauteng_facebook_groups_rolodex.md` covering 24 top active public groups in Centurion, Pretoria East, Sandton/Bryanston, Randburg, Midrand, and Edenvale/Bedfordview.
   - **Service & Pricing Menu:** Problem-to-price model ranging from R500 (flyers) to R1,500-R2,500 (1-page mobile site + Google Business Profile) and R1,200-R1,800/mo (done-for-you group posting retainer).
   - **Multi-Platform Video Engine (TikTok, IG Reels, YouTube Shorts):**
     - Script & caption generator tool at `.agents/skills/contractor-lead-engine/scripts/generate_video_script.py`.
     - Playbook at `.agents/skills/contractor-lead-engine/references/multi_platform_video_playbook.md`.
     - High-ticket "Omni-Channel Lead Tier" (R2,800 – R3,500/mo) turning 15s raw site clips into cross-platform lead assets.
   - **Automated Group Finder & Poster:** Developing a tool (recommended as a Chrome Extension or scheduled script) to:
     - Discover active local homeowner/community groups (e.g. Centurion, Sandton, Randburg, Midrand) with >5,000 members.
     - Automatically schedule and publish contractor flyers with randomized intervals (3–8 mins) and caption rotations to avoid Meta anti-spam / account bans.
   - **Business Model:** Packaged as a high-margin "Done-For-You" lead generation service (R1,500 – R2,500/mo per contractor) or a lightweight micro-SaaS desktop tool.
