#!/usr/bin/env python3
"""
Integrated Contractor Lead Auditor
Ties visual gallery heuristics together with strict Jev qualification scoring.
"""

import os
import sys
import json
import argparse
from audit_gallery_heuristics import audit_contractor_gallery
from jev_contractor_evaluator import evaluate_contractor

def run_complete_lead_audit(profile_json_path, images_dir):
    """
    Executes the full automated audit pipeline:
    1. Audits project photos for daytime clarity, resolution, and count.
    2. Runs Jev 4-Pillar scoring using verified business data.
    3. Outputs a single integrated audit report.
    """
    if not os.path.exists(profile_json_path):
        return {"error": f"Profile file not found: {profile_json_path}"}
        
    with open(profile_json_path, "r", encoding="utf-8") as f:
        profile = json.load(f)
        
    # Step 1: Visual Gallery Audit
    gallery_report = audit_contractor_gallery(images_dir)
    
    # Update profile with verified photo count and quality
    usable_photos = gallery_report.get("usable_images", 0)
    profile["hero_photos_count"] = usable_photos
    
    if gallery_report.get("gallery_verdict") != "PASSED":
        profile["hero_photos_count"] = 0
        
    # Step 2: Jev 4-Pillar Evaluation
    jev_report = evaluate_contractor(profile)
    
    return {
        "contractor": profile.get("name"),
        "city": profile.get("city"),
        "trade": profile.get("trade"),
        "audit_status": jev_report.get("decision"),
        "jev_score": jev_report.get("jev_score"),
        "cash_flow_signals": jev_report.get("cash_flow_signals_count"),
        "gallery_audit": {
            "total_photos": gallery_report.get("total_images"),
            "usable_photos": usable_photos,
            "verdict": gallery_report.get("gallery_verdict")
        },
        "pillar_breakdown": jev_report.get("pillar_scores"),
        "recommendation": jev_report.get("recommendation"),
        "passing_factors": jev_report.get("passing_factors"),
        "rejection_factors": jev_report.get("rejection_factors")
    }

def main():
    parser = argparse.ArgumentParser(description="End-to-End Automated Lead Auditor")
    parser.add_argument("--profile", type=str, required=True, help="Path to contractor profile JSON")
    parser.add_argument("--images", type=str, required=True, help="Path to images directory")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()
    
    report = run_complete_lead_audit(args.profile, args.images)
    
    if args.json:
        print(json.dumps(report, indent=2))
        return
        
    status_icon = "🟢" if report["audit_status"] == "TIER_1_PRIORITY" else ("🟡" if report["audit_status"] == "TIER_2_QUALIFIED" else "🔴")
    print("\n" + "=" * 65)
    print(f" {status_icon} AUTOMATED LEAD AUDIT: {report['contractor'].upper()}")
    print("=" * 65)
    print(f"  • Decision:        {report['audit_status']}")
    print(f"  • Jev Score:       {report['jev_score']} / 100")
    print(f"  • Gallery Status:  {report['gallery_audit']['verdict']} ({report['gallery_audit']['usable_photos']} usable photos)")
    print(f"  • Cash-Flow Signs: {report['cash_flow_signals']} / 4 (Min 2 required)")
    print(f"  • Recommendation:  {report['recommendation']}")
    print("-" * 65)
    print("  📊 Pillar Scores:")
    for k, v in report["pillar_breakdown"].items():
        print(f"     - {k.replace('_', ' ').title()}: {v} pts")
    print("-" * 65)
    print("  ✅ Passing Signals:")
    for f in report["passing_factors"]:
        print(f"     + {f}")
    if report["rejection_factors"]:
        print("\n  ❌ Disqualification Reasons:")
        for r in report["rejection_factors"]:
            print(f"     - {r}")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    main()
