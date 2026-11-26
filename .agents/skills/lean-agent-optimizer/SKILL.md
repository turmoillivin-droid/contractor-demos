---
name: lean-agent-optimizer
description: >-
  Architectural patterns, client-side scripts, and local runners that slash AI agent token consumption and execution costs by 90-95%. Use when designing high-volume scraping workflows, batch website/asset generation, subagent delegation architectures, or optimizing long-running agent conversations.
---

# Lean Agent Optimizer: The 90–95% Cost Reduction Engine

This skill provides the end-to-end blueprint for building high-speed, cost-optimized AI agent workflows. It shifts heavy computational lifting from expensive cloud LLMs to local CPU automation, collapsing multi-turn agent operations into single-turn executions.

---

## The Core Philosophy: "Judgments from AI, Execution in Code"

```
[❌ The Expensive Way]
AI Model ──(30 Turns)──▶ Clicks DOM ──(800 Tokens)──▶ Writes HTML ──(500 Tokens)──▶ Zips Files
Cost: ~$45.00 | Time: ~20 mins | Failure Points: High

[✅ The Lean Way]
AI Model ──(1 Turn)──▶ Evaluates DOM ──(100 Tokens)──▶ Emits Pure JSON
                                                            │
                                                            ▼ (Local Mac CPU / $0.00)
                                                    • Downloads assets in parallel
                                                    • Generates HTML from templates
                                                    • Compiles .zip archives
                                                    • Updates CRM & Git repos
Cost: ~$2.00 | Time: ~35 secs | Failure Points: Near Zero
```

---

## The 4 Pillars of Token Optimization

### 1. The 1-Turn Client-Side DOM Evaluator
* **Anti-Pattern:** Having a browser subagent click buttons, navigate pagination, and wait for screenshots step-by-step. Each click triggers a full DOM tree and screenshot capture (~100k–200k tokens per action).
* **Lean Pattern:** Inject a single JavaScript evaluator into the browser context. It queries the DOM in memory, applies regex filters (e.g. phone numbers, email patterns), extracts media links, and returns a compact JSON array in **1 turn**.
* **Bundled Script:** `scripts/batch_dom_extractor.js`

### 2. Local Deterministic Runners ($0.00 Compute)
* **Anti-Pattern:** Asking an LLM to generate full HTML files, write CSS classes, format Markdown files, or write shell scripts in the chat window.
* **Lean Pattern:** Keep code templates locally in Python/Node. The AI only outputs a **10-line JSON payload** containing dynamic entities (name, phone, area, image links). A local Python script parses the JSON, populates the templates, creates the files, and compiles zip packages on your Mac CPU at **0 tokens and 0 latency**.
* **Bundled Script:** `scripts/lean_batch_runner.py`

### 3. Model Pinning for Subagents
* **Anti-Pattern:** Allowing high-volume worker subagents to inherit large reasoning models (`pro`, `claude-3-7-sonnet`).
* **Lean Pattern:** Explicitly pin scraping, document reading, and data formatting subagents to lightweight, high-speed models:
  ```json
  {
    "TypeName": "browser",
    "Model": "flash",
    "Role": "Data Extractor"
  }
  ```
* **Cost Difference:** Flash models cost ~$0.075 / 1M input tokens compared to ~$3.00+ / 1M on flagship models (**~25x to 40x cost drop**).

### 4. Strict Thread Hygiene & Session Compaction
* **Anti-Pattern:** Keeping a single development thread running for 400+ turns. Turn 400 carries 220,000 tokens of chat history on every turn.
* **Lean Pattern:**
  1. Complete a batch of work (5–10 items).
  2. Commit and push all code to Git.
  3. Save state to a local Markdown or Obsidian file.
  4. Run `/compact` or start a fresh thread that reads the project memory (`GEMINI.md`) in **under 2,000 tokens**.

---

## Quick Reference: Cost & Speed Benchmarks

| Metric | Unoptimized LLM Loop | Lean Optimized Pipeline | Efficiency Gain |
| :--- | :---: | :---: | :---: |
| **Context per Turn** | ~220,000 tokens | ~15,000 tokens | **93% Reduction** |
| **Turns per 10 Units** | 60–100 turns | 2–3 turns | **95% Fewer Turns** |
| **Model Rate** | $3.00 / 1M tokens | $0.075 / 1M tokens | **40x Cheaper** |
| **Batch Cost (20 Items)** | **$35.00 – $50.00** | **$1.50 – $2.50** | **95% SAVINGS** |
| **Batch Completion Time** | ~20 minutes | ~40 seconds | **30x FASTER** |
