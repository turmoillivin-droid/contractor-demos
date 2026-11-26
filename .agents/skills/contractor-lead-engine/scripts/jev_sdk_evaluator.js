#!/usr/bin/env node
/**
 * TypeSafe AI (Jev) Contractor Evaluator (ESM)
 * Uses the official @typesafe-ai/sdk (System 1 classification & vision)
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { TypeSafeClient, noul, choice, score, image } from '@typesafe-ai/sdk';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Load environment from .env
function loadEnv() {
  const envPath = path.resolve(__dirname, '../../../.env');
  if (fs.existsSync(envPath)) {
    const lines = fs.readFileSync(envPath, 'utf-8').split('\n');
    for (const line of lines) {
      const trimmed = line.trim();
      if (trimmed && !trimmed.startsWith('#') && trimmed.includes('=')) {
        const [k, ...v] = trimmed.split('=');
        const key = k.trim();
        const val = v.join('=').trim().replace(/^["']|["']$/g, '');
        if (key && !process.env[key]) {
          process.env[key] = val;
        }
      }
    }
  }
}

loadEnv();

export async function evaluateWithJev(options) {
  const apiKey = process.env.TYPESAFE_API_KEY;
  if (!apiKey) {
    console.error("\n❌ Error: TYPESAFE_API_KEY is not set in .env.");
    console.error("Please add your key to /Users/mac/Documents/showhow-main/.env\n");
    process.exit(1);
  }

  const client = new TypeSafeClient({
    apiKey,
    defaultHeaders: { 'TypeSafe-Danger-Zone-Images': 'true' }
  });

  const stateData = {
    contractor_name: options.name || 'Unknown',
    city: options.city || 'South Africa',
    post_text: options.text || ''
  };

  if (options.imagePath && fs.existsSync(options.imagePath)) {
    const fileBytes = fs.readFileSync(options.imagePath);
    stateData.project_photo = image(fileBytes);
  }

  console.log(`\n⚡ Calling TypeSafe Jev System 1 for: ${options.name}...`);

  const response = await client.systemOne({
    state: stateData,
    questions: {
      is_established_contractor: noul("Is this business an established trade contractor rather than a solo handyman seeking day labor?"),
      trade_category: choice("What primary construction trade is being offered?", {
        tiling_masonry: null,
        roofing_waterproofing: null,
        aluminium_steel: null,
        plumbing: null,
        electrical: null,
        carpentry_kitchens: null,
        other: null
      }),
      shows_cashflow_signals: noul("Does the post or photo show indicators of serious capital (branded bakkie, scaffolding, large estate home, or commercial tools)?"),
      shows_finished_work: noul("Does the photo show clean, completed, high-quality finished work rather than unfinished rubble or muddy trenches?"),
      client_inbound_interest: choice("What is the level of client demand in the comments?", {
        high_inbound_leads: null,
        moderate_interest: null,
        no_client_comments: null
      })
    }
  });

  return response.answers;
}

// CLI Execution
async function main() {
  const args = process.argv.slice(2);
  let name = "Raboshabane Trading";
  let text = "Double storey masonry building and concrete slabs in Johannesburg. Call 078 948 1786 for quotation.";
  let imgPath = null;

  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--name') name = args[++i];
    if (args[i] === '--text') text = args[++i];
    if (args[i] === '--image') imgPath = args[++i];
  }

  try {
    const answers = await evaluateWithJev({ name, text, imagePath: imgPath });
    console.log("\n=================================================");
    console.log(` 🟢 TYPESAFE JEV EVALUATION RESULT: ${name}`);
    console.log("=================================================");
    console.log("  • Established Contractor:", answers.is_established_contractor?.noul ? "✅ Yes" : "❌ No");
    console.log("  • Trade Category:        ", answers.trade_category?.choice);
    console.log("  • Capital / Cash-Flow:   ", answers.shows_cashflow_signals?.noul ? "✅ Strong" : "⚠️ Weak");
    console.log("  • Finished Work Quality: ", answers.shows_finished_work?.noul ? "✅ High" : "⚠️ Low");
    console.log("  • Inbound Demand:        ", answers.client_inbound_interest?.choice);
    console.log("=================================================\n");
  } catch (err) {
    console.error("TypeSafe Jev Execution Error:", err.message);
  }
}

if (process.argv[1] && process.argv[1].endsWith('jev_sdk_evaluator.js')) {
  main();
}
