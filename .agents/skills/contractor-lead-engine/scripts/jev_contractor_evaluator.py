#!/usr/bin/env python3
"""
Jev Contractor Lead Evaluator & Scoring Engine
Strict South Africa Trades Qualification Pipeline (Version 2.0)

Evaluates prospective trade contractors against 4 strict pillars:
1. Strict "No Website" Audit (Zero False Positives: FB empty + free email + Google Page 1 clean)
2. Social-Proof Rich & High Inbound Intent (Pinned menu / active "how much" comments / GBP no site)
3. Ability to Pay / Cash-Flow Signals (Fleet branding / crew / affluent estate / >12mo) - MUST HAVE 2+
4. Demo-Ready Brand Assets (Clean logo + 3-5 daytime finished hero photos + owner name)
"""

import sys
import argparse
import json

def evaluate_contractor(data):
    reasons_reject = []
    reasons_pass = []
    
    # -------------------------------------------------------------
    # 0. HARD AUTO-EXCLUDES
    # -------------------------------------------------------------
    if data.get("auto_exclude_subcontractor", False):
        reasons_reject.append("Auto-Exclude: Subcontractor seeking day-work, not an established business owner.")
    if data.get("auto_exclude_supplier", False):
        reasons_reject.append("Auto-Exclude: Material supplier or hardware reseller, not an installation trade.")
    if data.get("days_inactive", 0) > 60:
        reasons_reject.append(f"Auto-Exclude: Inactive on social media for {data.get('days_inactive')} days (> 60 days threshold).")
    if data.get("google_domain_found", False):
        reasons_reject.append("Auto-Exclude: Owned .co.za or .com website already exists and ranks on Google Page 1.")

    # -------------------------------------------------------------
    # 1. PILLAR 1: STRICT NO-WEBSITE VERIFICATION (Max 35 pts)
    # -------------------------------------------------------------
    no_web_score = 0
    if data.get("fb_website_empty", False):
        no_web_score += 20
        reasons_pass.append("FB Website field empty or social-only link (+20)")
    else:
        reasons_reject.append("FB Website field has an external website link.")

    if data.get("free_email", False):
        no_web_score += 15
        reasons_pass.append("Uses free email provider (@gmail/@yahoo/etc), no corporate domain email (+15)")
    else:
        reasons_reject.append("Uses custom domain email (indicates existing domain/site).")

    if not data.get("google_domain_found", False):
        reasons_pass.append("Google Page 1 clean: Zero owned .co.za/.com domains found")

    # -------------------------------------------------------------
    # 2. PILLAR 2: SOCIAL PROOF & INBOUND INTENT (Max 25 pts)
    # -------------------------------------------------------------
    intent_score = 0
    if data.get("pinned_menu", False):
        intent_score += 10
        reasons_pass.append("Pinned service menu / pricing graphic active on Facebook (+10)")
    
    comments = data.get("inbound_comments", 0)
    if comments >= 3:
        intent_score += 10
        reasons_pass.append(f"High inbound intent: {comments} homeowner quote inquiries in recent comments (+10)")
    elif comments > 0:
        intent_score += 5
        reasons_pass.append(f"Moderate inbound intent: {comments} homeowner comment (+5)")

    if data.get("gbp_without_site", False):
        intent_score += 5
        reasons_pass.append("Google Business Profile (Maps pin) active with NO website button (+5)")

    # -------------------------------------------------------------
    # 3. PILLAR 3: ABILITY TO PAY / CASH-FLOW QUALIFIERS (Max 25 pts)
    # MUST HAVE AT LEAST 2 SIGNALS TO PASS
    # -------------------------------------------------------------
    cash_flow_signals = 0
    cash_flow_score = 0

    if data.get("fleet_branding", False):
        cash_flow_signals += 1
        cash_flow_score += 6
        reasons_pass.append("Sign-written fleet bakkie, truck, or trailer visible on jobsite (+6)")

    if data.get("crew_visible", False):
        cash_flow_signals += 1
        cash_flow_score += 6
        reasons_pass.append("Team of 2+ in branded workwear / scaffolding / industrial equipment (+6)")

    if data.get("affluent_suburb", False):
        cash_flow_signals += 1
        cash_flow_score += 6
        reasons_pass.append("Modern architectural / residential estate project markers (+6)")

    if data.get("page_months", 0) >= 12:
        cash_flow_signals += 1
        cash_flow_score += 7
        reasons_pass.append(f"Established page longevity: {data.get('page_months')} months active (+7)")

    if cash_flow_signals < 2:
        reasons_reject.append(f"Insufficient cash-flow signals: Only {cash_flow_signals}/4 found (minimum 2 required). High risk of non-payment.")

    # -------------------------------------------------------------
    # 4. PILLAR 4: DEMO-READY BRAND ASSETS (Max 15 pts)
    # -------------------------------------------------------------
    asset_score = 0
    if data.get("clean_logo", False):
        asset_score += 5
        reasons_pass.append("Clean graphic logo or company badge available (+5)")
    else:
        reasons_reject.append("No clean logo/badge found (blurry selfie or generic icon).")

    photos = data.get("hero_photos_count", 0)
    if photos >= 5:
        asset_score += 10
        reasons_pass.append(f"Excellent hero project gallery: {photos} wide, finished daytime photos (+10)")
    elif photos >= 3:
        asset_score += 7
        reasons_pass.append(f"Adequate hero gallery: {photos} finished project photos (+7)")
    else:
        reasons_reject.append(f"Hero photos insufficient: Only {photos} found (minimum 3 required, no rubble/trenches).")

    # -------------------------------------------------------------
    # TOTAL JEV SCORE & DECISION
    # -------------------------------------------------------------
    total_score = no_web_score + intent_score + cash_flow_score + asset_score

    # Qualification Logic
    is_disqualified = (
        len(reasons_reject) > 0 or
        cash_flow_signals < 2 or
        data.get("google_domain_found", False) or
        not data.get("fb_website_empty", False) or
        not data.get("free_email", False) or
        photos < 3
    )

    if not is_disqualified and total_score >= 85:
        decision = "TIER_1_PRIORITY"
        recommendation = "Build mobile demo immediately (< 2 hrs). High-conversion target ready for WhatsApp pitch."
    elif not is_disqualified and total_score >= 70:
        decision = "TIER_2_QUALIFIED"
        recommendation = "Qualified candidate. Build standard demo and pitch within 24 hours."
    else:
        decision = "DISQUALIFIED"
        recommendation = "Do not build demo. Disqualified based on strict criteria."

    return {
        "contractor": data.get("name", "Unknown"),
        "city": data.get("city", "Unknown"),
        "trade": data.get("trade", "Unknown"),
        "jev_score": total_score,
        "decision": decision,
        "cash_flow_signals_count": cash_flow_signals,
        "recommendation": recommendation,
        "pillar_scores": {
            "strict_no_website": no_web_score,
            "social_proof_intent": intent_score,
            "cash_flow_signals": cash_flow_score,
            "asset_readiness": asset_score
        },
        "passing_factors": reasons_pass,
        "rejection_factors": reasons_reject
    }

def main():
    parser = argparse.ArgumentParser(description="Jev Contractor Qualification Evaluator")
    parser.add_argument("--name", type=str, required=True, help="Business / Contractor Name")
    parser.add_argument("--owner", type=str, default="Owner", help="Owner First Name")
    parser.add_argument("--city", type=str, default="Johannesburg", help="City / Municipality")
    parser.add_argument("--trade", type=str, default="General Trade", help="Trade Specialty")
    parser.add_argument("--fb-website-empty", type=str, default="true", help="Is FB website field empty or social-only? (true/false)")
    parser.add_argument("--free-email", type=str, default="true", help="Uses @gmail/@yahoo email? (true/false)")
    parser.add_argument("--google-domain-found", type=str, default="false", help="Did Google Page 1 show owned domain? (true/false)")
    parser.add_argument("--pinned-menu", type=str, default="false", help="Has pinned services/price menu? (true/false)")
    parser.add_argument("--inbound-comments", type=int, default=0, help="Count of recent homeowner quote comments")
    parser.add_argument("--gbp-without-site", type=str, default="false", help="Google Maps listing exists with NO website button? (true/false)")
    parser.add_argument("--fleet", type=str, default="false", help="Sign-written bakkie/trailer on site? (true/false)")
    parser.add_argument("--crew", type=str, default="false", help="Uniformed crew (2+) / scaffolding / machinery? (true/false)")
    parser.add_argument("--luxury-suburb", type=str, default="false", help="Estates / luxury suburb / high-end architectural photos? (true/false)")
    parser.add_argument("--page-months", type=int, default=12, help="Age of Facebook page in months")
    parser.add_argument("--clean-logo", type=str, default="true", help="Clean graphic logo/badge available? (true/false)")
    parser.add_argument("--hero-photos", type=int, default=4, help="Count of wide, finished, daytime project photos")
    parser.add_argument("--auto-subcontractor", type=str, default="false", help="Is subcontractor seeking day-work? (true/false)")
    parser.add_argument("--auto-supplier", type=str, default="false", help="Is material/hardware supplier? (true/false)")
    parser.add_argument("--days-inactive", type=int, default=5, help="Days since last post")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    to_bool = lambda v: str(v).lower() in ("true", "1", "yes")

    payload = {
        "name": args.name,
        "owner": args.owner,
        "city": args.city,
        "trade": args.trade,
        "fb_website_empty": to_bool(args.fb_website_empty),
        "free_email": to_bool(args.free_email),
        "google_domain_found": to_bool(args.google_domain_found),
        "pinned_menu": to_bool(args.pinned_menu),
        "inbound_comments": args.inbound_comments,
        "gbp_without_site": to_bool(args.gbp_without_site),
        "fleet_branding": to_bool(args.fleet),
        "crew_visible": to_bool(args.crew),
        "affluent_suburb": to_bool(args.luxury_suburb),
        "page_months": args.page_months,
        "clean_logo": to_bool(args.clean_logo),
        "hero_photos_count": args.hero_photos,
        "auto_exclude_subcontractor": to_bool(args.auto_subcontractor),
        "auto_exclude_supplier": to_bool(args.auto_supplier),
        "days_inactive": args.days_inactive
    }

    result = evaluate_contractor(payload)

    if args.json:
        print(json.dumps(result, indent=2))
        return

    # Formatted CLI output
    status_icon = "🟢" if result["decision"] == "TIER_1_PRIORITY" else ("🟡" if result["decision"] == "TIER_2_QUALIFIED" else "🔴")
    print("\n" + "=" * 65)
    print(f" {status_icon} JEV CONTRACTOR EVALUATION: {result['contractor'].upper()}")
    print("=" * 65)
    print(f"  • Decision:        {result['decision']}")
    print(f"  • Jev Score:       {result['jev_score']} / 100")
    print(f"  • Cash-Flow Signs: {result['cash_flow_signals_count']} / 4 (Min 2 required)")
    print(f"  • City / Trade:    {result['city']} | {result['trade']}")
    print(f"  • Recommendation:  {result['recommendation']}")
    print("-" * 65)
    print("  📊 Pillar Breakdown:")
    print(f"     1. Strict No-Website: {result['pillar_scores']['strict_no_website']} / 35")
    print(f"     2. Social & Intent:   {result['pillar_scores']['social_proof_intent']} / 25")
    print(f"     3. Cash-Flow Signals: {result['pillar_scores']['cash_flow_signals']} / 25")
    print(f"     4. Brand Asset Ready: {result['pillar_scores']['asset_readiness']} / 15")
    print("-" * 65)
    print("  ✅ Passing Signals:")
    for f in result["passing_factors"]:
        print(f"     + {f}")
    if result["rejection_factors"]:
        print("\n  ❌ Disqualification Reasons:")
        for r in result["rejection_factors"]:
            print(f"     - {r}")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    main()
