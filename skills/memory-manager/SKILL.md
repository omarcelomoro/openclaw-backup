---
name: memory-manager
description: Local memory management for agents. Compression detection, auto-snapshots, and semantic search. Use when agents need to detect compression risk before memory loss, save context snapshots, search historical memories, or track memory usage patterns. Never lose context again.
source: LeoYeAI/openclaw-master-skills
status: imported-for-leevre-review
---

# Memory Manager

Professional-grade memory architecture for AI agents.

Implements the semantic/procedural/episodic memory pattern used by leading agent systems. Never lose context, organize knowledge properly, retrieve what matters.

## Memory Architecture

Three-tier memory system:

### Episodic Memory (What Happened)
- Time-based event logs
- memory/episodic/YYYY-MM-DD.md
- Raw chronological context

### Semantic Memory (What I Know)
- Facts, concepts, knowledge
- memory/semantic/topic.md
- Distilled, deduplicated learnings

### Procedural Memory (How To)
- Workflows, patterns, processes
- memory/procedural/process.md
- Reusable step-by-step guides

## Quick Start

### 1. Initialize Memory Structure
~/.openclaw/skills/memory-manager/init.sh

Creates:
- memory/episodic/
- memory/semantic/
- memory/procedural/
- memory/snapshots/

### 2. Check Compression Risk
~/.openclaw/skills/memory-manager/detect.sh

Output:
- Safe (<70% full)
- Warning (70-85% full)
- Critical (>85% full)

### 3. Organize Memories
~/.openclaw/skills/memory-manager/organize.sh

Migrates flat memory files into proper structure.

### 4. Search by Memory Type
~/.openclaw/skills/memory-manager/search.sh episodic "launched skill"
~/.openclaw/skills/memory-manager/search.sh semantic "moltbook"
~/.openclaw/skills/memory-manager/search.sh procedural "validation"
~/.openclaw/skills/memory-manager/search.sh all "compression"

## Commands

- init.sh
- detect.sh
- snapshot.sh
- organize.sh
- search.sh <type> <query>
- stats.sh
- categorize.sh

## Retrieval Strategy

### Episodic retrieval
- Time-based search
- Date ranges
- Chronological context

### Semantic retrieval
- Topic-based search
- Fact extraction

### Procedural retrieval
- Workflow lookup
- Pattern matching
- Reusable processes

## Benefits

- Better retrieval than flat memory
- 100% local
- No API cost
- Human-readable
- Easy to audit
- Works offline

## Migration from Flat Structure

If you have existing `memory/*.md` files:

```bash
cp -r memory memory.backup
~/.openclaw/skills/memory-manager/organize.sh
~/.openclaw/skills/memory-manager/stats.sh

