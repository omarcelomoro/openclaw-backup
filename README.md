# Livri 🐝 — Workspace da Leevre Corretora

COO digital do Marcelo Moro. Cuida da operação, conteúdo, infraestrutura e memória da Leevre Corretora de Seguros.

---

## Estrutura do Repositório

```
workspace/
├── SOUL.md              # Personalidade e valores da Livri
├── USER.md              # Perfil do Marcelo Moro
├── IDENTITY.md          # Identidade, email, modelos de IA
├── AGENTS.md            # Regras de operação e startup
├── MEMORY.md            # Memória de longo prazo (índice)
├── HEARTBEAT.md         # O que checar periodicamente
├── TOOLS.md             # Ferramentas e configurações locais
├── DECISIONS.md         # Decisões permanentes tomadas
├── LESSONS.md           # Lições aprendidas
├── PENDING.md           # Pendências ativas
├── PEOPLE.md            # Equipe, parceiros, benchmarks
├── PROJECTS.md          # Projetos ativos e backlog
├── openclaw.sanitized.json  # Config OpenClaw (sem secrets)
├── restore.sh           # Script de restauração em nova VPS
│
├── memory/              # Memória por data e tópico
│   ├── 2026-MM-DD.md    # Notas diárias
│   ├── context/         # Protocolos e contextos
│   ├── projects/        # Detalhes de cada projeto
│   └── research/        # Resultados de deep research
│
├── conteudo/            # Scripts, roteiros, calendário editorial
│
└── skills/              # Skills customizadas
    ├── gog/             # Integração Google (gogcli)
    └── openai-whisper-api/
```

---

## Infraestrutura

- **VPS:** 187.77.247.207 (Ubuntu)
- **OpenClaw:** gateway em loopback, acesso via SSH tunnel
- **WhatsApp:** Evolution API v1.8.7 (Docker, porta 8080)
- **Google:** gogcli v0.12.0, contas `marcelo@` e `atendimento@leevrecorretora.com.br`
- **Backup:** cron diário 03:00 UTC → este repositório

---

## Restaurar em nova VPS

```bash
git clone https://github.com/omarcelomoro/openclaw-backup.git /root/.openclaw/workspace
bash /root/.openclaw/workspace/restore.sh
```

Veja `restore.sh` para o passo a passo completo.

---

## Contexto do Negócio

- **Empresa:** Leevre Corretora de Seguros
- **Foco:** Consórcio imobiliário e seguros
- **Meta 2026:** R$60M em consórcio (dobrar vs 2025)
- **Administradoras:** Itaú, Bradesco, Servopa, Porto
