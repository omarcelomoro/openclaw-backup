# OpenClaw — Smart (Backup de Configuração)

Repositório de backup automático das configurações do assistente **Smart** rodando em OpenClaw.

---

## 🚀 Deploy em Novo Servidor / VPS

### 1. Instalar o OpenClaw

```bash
npm install -g openclaw
```

### 2. Restaurar o workspace

```bash
cd /root/.openclaw
git clone https://github.com/omarcelomoro/openclaw-backup.git workspace
```

### 3. Restaurar a configuração principal

Copie o arquivo `openclaw.json.bak` para o local correto:

```bash
cp /root/.openclaw/workspace/openclaw.json /root/.openclaw/openclaw.json
```

> ⚠️ Edite o `openclaw.json` e reconfigure as chaves de API (Anthropic, Telegram, etc.) — elas não ficam no backup por segurança.

### 4. Iniciar o gateway

```bash
openclaw gateway start
```

### 5. Reconectar o Telegram

Configure o token do Telegram no OpenClaw:

```bash
openclaw configure
```

Siga o wizard e reconecte os canais.

---

## 📁 Estrutura do Workspace

| Arquivo | Descrição |
|---|---|
| `SOUL.md` | Personalidade e valores do Smart |
| `IDENTITY.md` | Nome, vibe e avatar |
| `USER.md` | Informações sobre o Marcelo |
| `AGENTS.md` | Regras de comportamento e memória |
| `TOOLS.md` | Notas locais de ferramentas |
| `HEARTBEAT.md` | Checklist de tarefas periódicas |
| `MEMORY.md` | Memória de longo prazo (gerada em uso) |
| `memory/` | Notas diárias (geradas em uso) |

---

## 🔄 Backup Automático

O backup é feito automaticamente todo dia via cron.
Script: `/root/scripts/backup-openclaw.sh`

Para rodar manualmente:

```bash
bash /root/scripts/backup-openclaw.sh
```

---

*Smart — Assistente do Marcelo Moro*
