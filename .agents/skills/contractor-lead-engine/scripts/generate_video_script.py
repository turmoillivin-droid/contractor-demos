#!/usr/bin/env python3
"""
Contractor Video Script & Caption Generator
Outputs ready-to-use hooks, voiceovers, on-screen text overlays,
and platform-optimized captions for TikTok, Instagram Reels, and YouTube Shorts.
"""

import argparse

def generate_scripts(args):
    business = args.name
    trade = args.trade
    city = args.city
    phone = args.phone
    cost = args.cost or "R4,500 – R8,500"
    project = args.project or f"{trade} project"

    output = f"""
================================================================================
🎬 VIDEO MARKETING PACK FOR: {business}
📍 LOCATION: {city} | TRADE: {trade}
================================================================================

--------------------------------------------------------------------------------
🔥 OPTION 1: THE VIRAL TIKTOK COST BREAKDOWN (Highest Lead Volume)
--------------------------------------------------------------------------------
⏱ DURATION: 15–25 seconds
🎥 VISUAL: Slow panning video across the completed job site.

[ON-SCREEN HOOK (Bold text in center for 0–3 sec)]:
👉 "How much did this {project} cost in {city}? 🇿🇦"

[VOICEOVER / TALKING SCRIPT]:
"Client called us out to {city} because their old {trade.lower()} needed a complete overhaul.
Here is what went into it:
- Site preparation & leveling: Day 1
- Professional installation & laser alignment: Day 2 to 3
- Final finishing, grouting & site cleanup: Day 4
Total turnaround: Under a week.
Labor quote: {cost}.
If you want an honest quote for your home, tap the WhatsApp link in bio or WhatsApp {phone}!"

[TIKTOK CAPTION]:
How much does professional {trade.lower()} cost in {city}? Here's the exact breakdown. 🛠️ Direct contractor rates, zero middleman fees. WhatsApp {phone} for free site visits!
#satiktok #southafricabuilders #{city.lower().replace(' ', '')} #{trade.lower().replace(' ', '')} #renovationssouthafrica #mzansihomes

--------------------------------------------------------------------------------
✨ OPTION 2: THE INSTAGRAM REEL (High-End Aesthetic & Trust)
--------------------------------------------------------------------------------
⏱ DURATION: 10–15 seconds
🎥 VISUAL: 2 seconds of the messy/raw room -> transition on the beat to the finished room.

[ON-SCREEN TEXT]:
Beat 1 (0:00 - 0:02): "Wait for the finish... 👀"
Beat 2 (0:02 - 0:12): "📍 {city} | {business}"
Beat 3 (0:12 - 0:15): "WhatsApp {phone} for quotes"

[AUDIO SUGGESTION]:
Trending acoustic house or deep ambient beat.

[INSTAGRAM CAPTION]:
Clean lines. Solid workmanship. Done right the first time. 💯
Supervised on-site by {business} across {city} and surrounding areas.
📲 Tap the link in bio for our instant WhatsApp quote calculator!
📞 Call/WhatsApp: {phone}
.
.
#{city.lower().replace(' ', '')}homes #{trade.lower().replace(' ', '')}southafrica #southafricanhomes #joburgcontractors #homeimprovementza

--------------------------------------------------------------------------------
📺 OPTION 3: YOUTUBE SHORTS (Google Search & Evergreen Leads)
--------------------------------------------------------------------------------
[VIDEO TITLE]:
{trade.title()} in {city} (Cost & Time Breakdown) #Shorts

[PINNED COMMENT]:
💬 Need a quote for your property in {city}?
Chat directly with {business} on WhatsApp: https://wa.me/{phone.replace(' ', '')}

[DESCRIPTION]:
Professional {trade.lower()} in {city} by {business}. Fast turnarounds, transparent pricing, and quality workmanship. 
Call or WhatsApp: {phone}
================================================================================
"""
    print(output)
    if args.save:
        with open(args.save, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"✅ Saved script pack to: {args.save}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate Contractor Short-Form Video Scripts")
    parser.add_argument('--name', required=True, help="Contractor / Business name")
    parser.add_argument('--trade', required=True, help="Trade (e.g. Ceramic Tiling, Smooth Plastering, House Building)")
    parser.add_argument('--city', required=True, help="City / Suburb (e.g. Centurion, Sandton, Durbanville)")
    parser.add_argument('--phone', required=True, help="Phone / WhatsApp number")
    parser.add_argument('--project', default="", help="Specific project (e.g. 60sqm living room tiling)")
    parser.add_argument('--cost', default="", help="Approx labor cost (e.g. R6,500)")
    parser.add_argument('--save', default="", help="Path to save output file")
    args = parser.parse_args()
    generate_scripts(args)
