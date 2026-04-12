#!/usr/bin/env bash
set -euo pipefail

BACKUP_DIR="/home/marcelo/.openclaw/backups"
WORKSPACE_DIR="/home/marcelo/.openclaw/workspace"
TS="$(date -u +%Y-%m-%dT%H-%M-%SZ)"
OUT="${BACKUP_DIR}/workspace-backup-${TS}.tar.gz"
LOG="/home/marcelo/.openclaw/backups/backup.log"

mkdir -p "$BACKUP_DIR"

tar -czf "$OUT" -C /home/marcelo/.openclaw workspace

echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] local backup created: $OUT" >> "$LOG"

cd "$WORKSPACE_DIR"

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git add -A >> "$LOG" 2>&1 || true

  if ! git diff --cached --quiet; then
    git config user.name "Livri" >> "$LOG" 2>&1 || true
    git config user.email "livri@local" >> "$LOG" 2>&1 || true
    git commit -m "backup: $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$LOG" 2>&1 || true
  fi

  if git remote get-url origin >/dev/null 2>&1; then
    CURRENT_BRANCH="$(git branch --show-current 2>/dev/null || echo master)"
    if git push origin "$CURRENT_BRANCH" >> "$LOG" 2>&1; then
      echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] github push ok" >> "$LOG"
    else
      echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] github push failed" >> "$LOG"
    fi
  else
    echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] github remote not configured" >> "$LOG"
  fi
fi

ls -1t "$BACKUP_DIR"/workspace-backup-*.tar.gz 2>/dev/null | tail -n +15 | xargs -r rm -f
