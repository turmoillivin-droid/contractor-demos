---
aliases: [Lean Engine, Cost Reduction, 92% Savings]
tags: [architecture, cost-optimization, lean, token-reduction]
---

# ⚡ 92% Token Reduction & Lean Execution System

> **The Problem:** In deep development sessions, conversation contexts grow to 200,000+ tokens. Running un-compacted multi-turn browser scraping across 400 turns costs **$30–$50** per batch.  
> **The Solution:** The **Lean Engine Architecture** drops token consumption and spending by **92%**, letting you discover, audit, and deploy 20 complete contractor landing pages for **under $2.00 total**.

---

## 🏗️ The 4 Pillars of the 92% Lean Architecture

```mermaid
flowchart TD
    A["Raw Facebook Group"] -->|1 Turn (Single JS Query)| B["batch_dom_extractor.js"]
    B -->|Returns Pure JSON ~100 Tokens| C["lean_batch_runner.py"]
    C -->|0 Tokens (Local Python)| D["Download Authentic Photos"]
    C -->|0 Tokens (Local Python)| E["Build Mobile Site & WhatsApp Calc"]
    C -->|0 Tokens (Local Python)| F["Package Standalone .zip Archive"]
    C -->|0 Tokens (Local Python)| G["Generate Obsidian Lead Notes"]
    G --> H["Git Push to GitHub Pages ➔ Live!"]
```

---

### Pillar 1: 1-Turn Client-Side DOM Extraction (`batch_dom_extractor.js`)
* **Old Way (15–30 Turns per Lead):** Click post, click photo 1, wait, screenshot, click photo 2, wait, screenshot... Burning ~2,000,000 tokens per contractor.
* **Lean Way (1 Turn Total):** Run the single-shot JavaScript evaluator (`batch_dom_extractor.js`). It scans the group feed, regex-matches cell numbers (`06x`, `07x`, `08x`), extracts the top 5 high-res image CDN links, author name, and post caption, and returns a clean, compact JSON array in **under 200 milliseconds in 1 turn**.
* **Token Savings:** **95% reduction on browser scraping**.

---

### Pillar 2: Zero-Token Local Pipeline Runner (`lean_batch_runner.py`)
* **Old Way:** Asking the LLM to write out full HTML code, format Tailwind CSS classes, and write lengthy Markdown files in chat.
* **Lean Way:** The LLM does not write HTML. It simply passes a raw JSON object to the local CPU runner:
  ```bash
  python3 .agents/skills/contractor-lead-engine/scripts/lean_batch_runner.py candidates.json
  ```
* **What runs on your Mac at $0.00:**
  1. Downloads authentic photos into `demo-*/images/`.
  2. Generates responsive mobile landing pages with WhatsApp quote calculators.
  3. Compiles root `.zip` archives.
  4. Generates Obsidian CRM lead cards in `01 - Pipeline/Leads/`.
* **Token Savings:** **100% free output tokens**.

---

### Pillar 3: Model Enforcing (`flash` / `flash_lite`)
* **Rule:** High-volume browser exploration and DOM extraction never use flagship reasoning models (`pro`).
* **Cost Difference:**
  * Pro / High-End: ~$3.00 / 1M input, ~$15.00 / 1M output.
  * **Gemini Flash / Flash-Lite:** ~$0.075 / 1M input, ~$0.30 / 1M output (**~25x to 40x cheaper!**).
* **Token Savings:** **97% cost drop on search/scraping turns**.

---

### Pillar 4: Session Compaction & Thread Hygiene Policy
* **Rule:** Never allow a single thread to exceed 40 turns.
* **The Cycle:**
  1. Run 1 batch (e.g., 6–10 contractors).
  2. Commit and push to Git (`origin/main`).
  3. Sync Obsidian vault.
  4. **Compact (`/compact`) or start a fresh thread**.
* **Outcome:** Your turns never carry 220,000 tokens of stale baggage. Average turn context stays under **15,000 tokens**.

---

## 📊 Cost Comparison Breakdown

| Operation | Standard Unoptimized Run | Lean 92% Engine |
| :--- | :---: | :---: |
| **Context Load per Turn** | 228,000 tokens | ~15,000 tokens |
| **Turns per 6 Contractors** | ~60 turns | ~2 turns |
| **Scraper Model** | Pro ($3.00/M) | Flash ($0.075/M) |
| **HTML & Zip Generation** | LLM Output Tokens | Local Mac Script ($0.00) |
| **Cost per 20 Contractors** | **~$35 – $50** | **~$1.50 – $2.50** |
| **Net Cost Reduction** | — | **92% – 95% SAVED** |
