# Tool Updates — 2026-04-22

## Summary
✅ **COMPLETE** — Audited and installed two critical tool updates:

### 1. gogcli v0.13.0
- **Download:** https://github.com/steipete/gogcli/releases/tag/v0.13.0
- **Status:** ✅ INSTALLED
- **Location:** ~/.local/bin/gog
- **Checksum (SHA256):** a1fe25c47cc3297c6695d61c1b0b3abb7e88634b11e86d77bc0d930377287e3d ✓ Verified
- **Audit:** ✅ PASSED (skill-audit security review)

**Key Features:**
- Safer Gmail sending with no-send guardrails
- Forwarding, autoreplies, full-body search
- Markdown-to-Docs conversion in Drive
- Chart management in Sheets
- Secondary calendar creation in Calendar
- Better auth security & credential cleanup
- Agent safety improvements (denylist/allowlist)

### 2. mcporter v0.9.0
- **Download:** https://github.com/steipete/mcporter/releases/tag/v0.9.0
- **Status:** ✅ INSTALLED
- **Location:** /tmp/package/ (npm package with deps)
- **Checksum (SHA256):** 7ebe1d1050f04a9ddea0478f8314b94239b6716f87061b2daad750d281b84526 ✓ Verified
- **Audit:** ✅ PASSED (skill-audit security review)

**Key Features:**
- Per-server tool filtering (allowedTools/blockedTools)
- OAuth support for protected servers
- Improved child-process timeout handling
- Windows URL quoting fix for OAuth
- Schema-aware parameter coercion

## Security Audit Results

Both releases passed full OWASP ASI Top 10 + Snyk ToxicSkills analysis:
- ✅ No prompt injection vectors
- ✅ No data exfiltration patterns
- ✅ No code execution risks
- ✅ No credential exposure
- ✅ No suspicious dependencies
- ✅ No obfuscated content
- ✅ Proper permission scoping
- ✅ No social engineering markers

## Recommendation
✅ **Both approved for production use**

Particularly suitable for:
- gogcli: LLM/Agent integration with Google Workspace (with guardrails)
- mcporter: Model Context Protocol server proxying for agentic workflows
