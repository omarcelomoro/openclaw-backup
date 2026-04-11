---
name: telegram
description: OpenClaw skill for designing Telegram Bot API workflows and command-driven conversations using direct HTTPS requests (no SDKs).
source: LeoYeAI/openclaw-master-skills
status: imported-for-leevre-review
---

# Telegram Bot Skill (Advanced)

## Purpose
Provide a clean, production-oriented guide for building Telegram bot workflows via the Bot API, focusing on command UX, update handling, and safe operations using plain HTTPS.

## Best fit
- Command-first bot behavior
- Reliable update flow, webhook or polling
- Direct HTTP calls instead of SDKs

## Quick orientation
- Read references for endpoints, update types, request patterns, command UX, update normalization, and request templates.
- Keep the SKILL.md lean and push details to references.

## Required inputs
- Bot token and base API URL
- Update strategy
- Command list and conversation tone
- Allowed update types and rate-limit posture

## Operational notes
- Prefer strict command routing: `/start`, `/help`, `/settings`, `/status`
- Always validate incoming update payloads and chat context
- Handle 429s with backoff and avoid message bursts

## Security notes
- Never log tokens
- Use webhooks with a secret token header when possible

## Leevre adaptation notes
- Use for Telegram command design, bot routing, and operational message flows for Marcelo's direct use and Leevre support groups.
- Keep group behavior conservative, prefer mention-gated interactions where possible.
- Never hardcode chat IDs or tokens in the skill; store them only in runtime config or env.
