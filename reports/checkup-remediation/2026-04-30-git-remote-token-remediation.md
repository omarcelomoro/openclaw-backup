# Git Remote Token Remediation — 2026-04-30

## Change applied
- Replaced Git remote URL from HTTPS with embedded GitHub PAT to SSH.
- New remote: `git@github.com:omarcelomoro/openclaw-backup.git`

## Verification
- SSH auth to GitHub succeeded as `omarcelomoro`.
- `git ls-remote --heads origin` succeeded after the change.

## Important human action still required
- Revoke the old GitHub PAT in GitHub settings because it was previously stored in `.git/config`.
- Path: GitHub → Settings → Developer settings → Personal access tokens.

## Note
- A temporary pre-change snapshot was intentionally deleted because it contained the old token in `.git/config`.
