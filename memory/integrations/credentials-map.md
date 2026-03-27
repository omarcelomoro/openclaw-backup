# Mapa de Credenciais

**Atualizado:** 26/03/2026

> ⚠️ Este arquivo contém APENAS onde as credenciais estão — nunca os valores.
> Valores ficam em `/root/.openclaw/.env` (chmod 600, nunca commitado).

## Onde cada credencial fica

| Serviço | Onde está | Status |
|---------|-----------|--------|
| OpenClaw API Key | `/root/.openclaw/.env` | ativo |
| GitHub (backup) | `/root/.openclaw/.env` | ativo |
| Gmail (atendimentolivri@gmail.com) | `/root/.openclaw/.env` | ativo |
| Google Workspace (gog OAuth) | `/root/.openclaw/gog_client_secret.json` + `.env` (GOG_KEYRING_PASSWORD) | ativo — 2 contas autenticadas |
| HubSpot CRM (Leevre) | `/root/.openclaw/.env` → `HUBSPOT_API_KEY` | ativo — Private App "Livri" |
| Agger API | — | pendente — verificar documentação |
| Bitwarden | — | pendente — não instalado |

## Regra
Senhas e tokens NUNCA vão em:
- MEMORY.md
- IDENTITY.md
- Qualquer arquivo commitado no GitHub

Sempre em `/root/.openclaw/.env`.
