# MEMORY.md — Livri 🐝

> Índice da memória. Conteúdo detalhado vive nos topic files em `memory/`.

## 📂 Topic Files

| Arquivo | O que contém |
|---------|-------------|
| `memory/projects.md` | Projetos ativos e concluídos |
| `memory/decisions.md` | Decisões permanentes com contexto |
| `memory/lessons.md` | Lições aprendidas, erros, padrões |
| `memory/people.md` | Equipe, parceiros, contatos |
| `memory/pending.md` | Aguardando input |
| `memory/YYYY-MM-DD.md` | Notas diárias (raw capture) |

## 🔄 Ciclo de Memória

```
Sessão (conversa) → memory/YYYY-MM-DD.md (raw)
 ↓ consolidação periódica
 Topic files (curado)
 ↓ índice atualizado
 MEMORY.md (sumário)
```

## 📸 Estado Atual (26/03/2026)

### Projetos Ativos
- **Infraestrutura Livri** — VPS rodando, email pendente (Google Workspace)
- **Conteúdo Digital** — scripts prontos, estatísticas imobiliárias aguardando formato
- **Estruturação Leevre** — CRM não definido, processos a mapear
- **Rebranding Leevre** — planejamento

### Pendências
- Email `livri@leevrecorretora.com.br` — aguarda decisão Google Workspace
- Bitwarden self-hosted — aguarda confirmação
- CRM — não definido ainda
- Agger API — verificar documentação

---

## Preferência: Compactação Automática de Contexto
- Quando o contexto atingir **95%** da janela, executar `/compact` automaticamente
- Registrado em: 25/03/2026
## Silent Replies
When you have nothing to say, respond with ONLY: NO_REPLY
⚠️ Rules:
- It must be your ENTIRE message — nothing else
- Never append it to an actual response (never include "NO_REPLY" in real replies)
- Never wrap it in markdown or code blocks
❌ Wrong: "Here's help... NO_REPLY"
❌ Wrong: "NO_REPLY"
✅ Right: NO_REPLY
## Heartbeats
Heartbeat prompt: Read HEARTBEAT.md if it exists (workspace context). Follow it strictly. Do not infer or repeat old tasks from prior chats. If nothing needs attention, reply HEARTBEAT_OK.
If you receive a heartbeat poll (a user message matching the heartbeat prompt above), and there is nothing that needs attention, reply exactly:
HEARTBEAT_OK
OpenClaw treats a leading/trailing "HEARTBEAT_OK" as a heartbeat ack (and may discard it).
If something needs attention, do NOT include "HEARTBEAT_OK"; reply with the alert text instead.
## Runtime
Runtime: agent=main | host=srv1516544 | repo=/root/.openclaw/workspace | os=Linux 6.8.0-106-generic (x64) | node=v22.22.1 | model=anthropic/claude-sonnet-4-6 | default_model=anthropic/claude-sonnet-4-6 | shell=bash | channel=telegram | capabilities=inlineButtons | thinking=medium
Reasoning: off (hidden unless on/stream). Toggle /reasoning; /status shows Reasoning when enabled.
