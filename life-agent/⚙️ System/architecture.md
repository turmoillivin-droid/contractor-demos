# Life-Agent System Architecture

## 1. Core Philosophy
* **Stigmergy:** Agents communicate by leaving text traces in a shared environment (the Obsidian Vault).
* **CLI Chaining:** Agents use terminal commands to trigger one another synchronously when urgent.

---

## 2. The Tech Stack

### 2.1 Obsidian (The Data Layer)
Acts as the visual dashboard on your Mac. All memory, rules, and logs are stored as local Markdown files in a centralized Vault, making them fully searchable and linkable.

### 2.2 Hermes CLI (The Engine Layer)
Runs in the zsh terminal. Executes terminal commands, handles file read/write permissions, and bridges the local file system with AI models.

### 2.3 Antigravity (The Intelligence Layer)
The heavy-reasoning model (via `soyelmismo/anti-gravity` direct SDK) that powers the backend synthesis, pattern recognition, and content generation.

### 2.4 Telegram (The Interface Layer)
A private group chat running a Python bridge script (`telegram_bridge.py`), allowing seamless interaction with the agents from anywhere (e.g., sending voice notes while out in Johannesburg).

---

## 3. The Agent Roster

### 3.1 Mirror (The Companion)
* **Role:** Your front-line listener and diary companion.
* **Function:** Captures raw diary entries, reflects thoughts without judgment, and saves transcripts.
* **Prompt:** `⚙️ System/mirror-prompt.md`

### 3.2 Forge (The Architect)
* **Role:** The background synthesizer.
* **Function:** Analyzes diary logs, extracts behavioral patterns, ingests books (removing metadata), and updates global rules.
* **Prompt:** `⚙️ System/forge-prompt.md`

### 3.3 Pulse (The Social Creator)
* **Role:** The content engine.
* **Function:** Reads brand voice guidelines and generates social media drafts (e.g., for Turmoillivin' or BLESSET TURMOIL).
* **Prompt:** `⚙️ System/pulse-prompt.md`

---

## 4. Inter-Agent Communication

### 4.1 The Comm-Hub (Asynchronous)
Agents leave notes for each other in the `📨 Comm-Hub/` directory. For example, Mirror leaves a task for Forge to analyze a recurring sleep pattern in `📨 Comm-Hub/forge-tasks.md`.

### 4.2 Terminal Execution (Synchronous)
Agents can wake each other up via the Hermes terminal tool. For example, Mirror can run `hermes run forge` during an emergency brain dump to process it immediately.
