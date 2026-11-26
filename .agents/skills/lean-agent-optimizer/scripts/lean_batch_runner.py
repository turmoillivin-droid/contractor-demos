#!/usr/bin/env python3
"""
Lean Batch Runner (92% Token Reduction Engine)
Executes end-to-end demo generation, photo downloads, zip archiving,
and Obsidian CRM updates locally with ZERO LLM token consumption.
"""

import os
import sys
import json
import re
import urllib.request
import zipfile
import subprocess

WORKSPACE_ROOT = "/Users/mac/Documents/showhow-main"
SCRIPTS_DIR = os.path.join(WORKSPACE_ROOT, ".agents/skills/contractor-lead-engine/scripts")
VAULT_LEADS_DIR = os.path.join(WORKSPACE_ROOT, "contractor-crm-vault/01 - Pipeline/Leads")

def slugify(text):
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[-\s]+', '-', text)

def download_images(urls, target_dir):
    os.makedirs(target_dir, exist_ok=True)
    saved_paths = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        'Referer': 'https://www.facebook.com/'
    }
    
    for idx, url in enumerate(urls, 1):
        filename = f"photo-{idx}.jpg"
        filepath = os.path.join(target_dir, filename)
        if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
            saved_paths.append(filepath)
            continue
            
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=12) as resp:
                content = resp.read()
                if len(content) > 3000:
                    with open(filepath, "wb") as f:
                        f.write(content)
                    saved_paths.append(filepath)
        except Exception as e:
            print(f"    ⚠️ Warning downloading image {idx}: {e}")
            
    return saved_paths

def create_zip(folder_path, output_zip_path):
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, folder_path)
                zipf.write(abs_path, rel_path)

def process_candidate(candidate):
    name = candidate.get("name", "Contractor")
    phone = candidate.get("phone", "071 000 0000")
    owner = candidate.get("owner", name.split()[0] if name else "Owner")
    city = candidate.get("city", "Johannesburg")
    province = candidate.get("province", "Gauteng")
    trade = candidate.get("trade", "Building & Home Improvements")
    services = candidate.get("services", "Residential Building, Renovations, Alterations")
    photos = candidate.get("photos", [])

    slug = slugify(f"{name}-{city}")[:35]
    demo_dir_name = f"demo-{slug}"
    demo_dir = os.path.join(WORKSPACE_ROOT, demo_dir_name)
    images_dir = os.path.join(demo_dir, "images")
    zip_path = os.path.join(WORKSPACE_ROOT, f"{slug}.zip")

    print(f"\n🚀 Processing: {name} ({trade} in {city})")

    # 1. Download Photos locally
    print(f"  📥 Downloading {len(photos)} project photos...")
    downloaded = download_images(photos, images_dir)
    print(f"  ✅ Saved {len(downloaded)} authentic photos to {demo_dir_name}/images/")

    # 2. Generate Demo HTML
    print(f"  ⚡ Generating mobile site with WhatsApp calculator...")
    gen_script = os.path.join(SCRIPTS_DIR, "generate_demo.py")
    out_html = os.path.join(demo_dir, "index.html")
    
    cmd = [
        sys.executable, gen_script,
        "--name", name,
        "--owner", owner,
        "--phone", phone,
        "--city", city,
        "--province", province,
        "--services", services,
        "--output", out_html
    ]
    subprocess.run(cmd, check=True)

    # 3. Create Standalone .zip Package
    create_zip(demo_dir, zip_path)
    zip_size_kb = round(os.path.getsize(zip_path) / 1024)
    print(f"  📦 Packaged standalone {slug}.zip ({zip_size_kb} KB)")

    # 4. Create Obsidian Lead Card
    lead_md_name = f"{owner} - {name}.md"
    lead_md_path = os.path.join(VAULT_LEADS_DIR, lead_md_name)
    
    lead_content = f"""---
company: "{name}"
owner: "{owner}"
phone: "{phone}"
trade: "{trade}"
location: "{city}, {province}"
status: "ready-to-pitch"
target_offer: "R1,999 setup + R1,500/mo retainer"
demo_path: "{demo_dir_name}/index.html"
tags: [lead, {slugify(province)}, {slugify(trade)}]
---

# [[{owner} - {name}]]

## 🏢 Business Profile
- **Company Name:** {name}
- **Contact:** {owner}
- **WhatsApp / Call:** `{phone}`
- **Location:** {city}, {province}

## 📁 Project Demo Asset
- **Local Demo Path:** `{demo_dir_name}/index.html`
- **Ready Deployment Archive:** `{slug}.zip` ({zip_size_kb} KB)
- **Live URL:** [https://turmoillivin-droid.github.io/contractor-demos/{demo_dir_name}/](https://turmoillivin-droid.github.io/contractor-demos/{demo_dir_name}/)

## 💬 Tailored WhatsApp Pitch
```text
Hello {owner},

Saw your recent {trade.lower()} work in {city}—solid craftsmanship.

Homeowners looking for quotes on WhatsApp want fast, visual estimates. Without a dedicated website, it's easy to lose clients to competitors on Google.

I put together a clean 1-page mobile preview for {name} with an instant WhatsApp quote calculator:
👉 https://turmoillivin-droid.github.io/contractor-demos/{demo_dir_name}/

It shows off your real installation photos with a direct quote button to your {phone} number.

Take a look—if you want to keep it live to win more residential contracts, let me know!
```
"""
    with open(lead_md_path, "w", encoding="utf-8") as f:
        f.write(lead_content)
    print(f"  🗂️ Synced Obsidian lead card: {lead_md_name}")

    return {
        "name": name,
        "owner": owner,
        "phone": phone,
        "city": city,
        "trade": trade,
        "dir": demo_dir_name,
        "zip": f"{slug}.zip",
        "photos_count": len(downloaded)
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 lean_batch_runner.py candidates.json")
        sys.exit(1)

    json_file = sys.argv[1]
    with open(json_file, "r", encoding="utf-8") as f:
        candidates = json.load(f)

    results = []
    for c in candidates:
        res = process_candidate(c)
        results.append(res)

    print("\n" + "=" * 65)
    print(" 🎉 LEAN BATCH COMPLETE (0 LLM TOKENS CONSUMED)")
    print("=" * 65)
    for r in results:
        print(f"  • {r['name']} ({r['trade']}) ➔ {r['dir']}/ | {r['zip']}")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    main()
