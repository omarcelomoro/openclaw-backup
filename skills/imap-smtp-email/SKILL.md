---
name: imap-smtp-email
description: Read and send email via IMAP/SMTP. Check for new/unread messages, fetch content, search mailboxes, mark as read/unread, and send emails with attachments. Works with any IMAP/SMTP server including Gmail, Outlook, 163.com, vip.163.com, 126.com, vip.126.com, 188.com, and vip.188.com.
source: LeoYeAI/openclaw-master-skills
status: imported-for-leevre-review
metadata:
 openclaw:
  emoji: "📧"
  requires:
   env:
    - IMAP_HOST
    - IMAP_USER
    - IMAP_PASS
    - SMTP_HOST
    - SMTP_USER
    - SMTP_PASS
   bins:
    - node
    - npm
  primaryEnv: SMTP_PASS
---

# IMAP/SMTP Email Tool

Read, search, and manage email via IMAP protocol.

