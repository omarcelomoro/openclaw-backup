---
name: Excel / XLSX
slug: excel-xlsx
version: 1.0.1
homepage: https://clawic.com/skills/excel-xlsx
description: Read, write, and generate Excel files with correct types, dates, formulas, and cross-platform compatibility.
changelog: Added Core Rules and modern skill structure
source: LeoYeAI/openclaw-master-skills
status: imported-for-leevre-review
metadata: {"clawdbot":{"emoji":"📗","requires":{"bins":[]},"os":["linux","darwin","win32"]}}
---

## Setup

On first use, read setup.md for integration guidelines. Ask user preferences naturally during conversation.

## When to Use

User needs to read, write, or generate Excel files (.xlsx, .xls, .xlsm). Agent handles type coercion, date serialization, formula evaluation, and cross-platform quirks.

## Architecture

Memory lives in ~/excel-xlsx/.

## Leevre adaptation notes
- Primary use cases: comissão, conciliação, controle operacional, import/export de bases, saneamento de listas e relatórios financeiros.
- Prefer explicit typing for IDs, phone numbers, policy numbers, proposal IDs, and any field with leading zeros.
- Treat Excel as a critical bridge between insurer exports, internal controls, and CRM migration work.

