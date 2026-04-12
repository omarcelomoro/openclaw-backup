# Lições Aprendidas

> Erros, padrões e aprendizados do dia a dia com a Livri.
> 🔒 Estratégicas = permanentes | ⏳ Táticas = expiram em 30 dias

---

## 🔒 Estratégicas

### Senhas de app do Gmail não funcionam em contas novas (Mar/2026)
O Google desativou senhas de app para contas pessoais novas. Para envio de email via SMTP, usar Google Workspace (domínio próprio) ou serviço transacional como Resend.

### PDF com emojis quebra no weasyprint (Mar/2026)
O servidor não tem fonte com suporte a emojis. Solução: substituir emojis por texto antes de gerar PDF (ex: 🐝 → [abelha], ✅ → [OK]). Pandoc + weasyprint funciona bem para o restante.

### Gateway restart via exec é interrompido por SIGTERM (Mar/2026)
`openclaw gateway restart` via exec mata a própria sessão antes de terminar. O gateway reinicia normalmente — o erro de saída pode ser ignorado. Confirmar status depois com `openclaw gateway status`.

### `reserveTokensFloor` fica dentro de `compaction` no config (Mar/2026)
O campo correto é `agents.defaults.compaction.reserveTokensFloor`, não `agents.defaults.reserveTokensFloor`. Validação do config rejeita chaves fora do namespace correto.

### Conteúdo de terceiros exige adaptação obrigatória (Mar/2026)
Roteiros baseados em Batalha, Wellington WK ou outros criadores precisam ser reescritos com contexto, números e exemplos próprios. Nunca copiar diretamente — risco de plágio e perda de voz autoral do Marcelo.

### thinking mode é slash command, não CLI (Mar/2026)
`openclaw thinking medium` não existe como comando de terminal. O correto é `/thinking medium` diretamente no chat. Mesma lógica para `/model` e outros slash commands.

---

## ⏳ Táticas

### Fallback configurado: claude-sonnet-4 (Mar/2026 — expira Jun/2026)
Fallback adicionado caso `claude-sonnet-4-6` falhe. Revisar quando novos modelos forem lançados.

### Sub-agentes usando claude-haiku-3-5 (Mar/2026 — expira Jun/2026)
Configurado `agents.defaults.subagents.model = anthropic/claude-haiku-3-5`. Revisar se Haiku tiver nova versão disponível.

### Grupo LEEVRE no Telegram: ID -1003706469372 (Mar/2026 — expira Set/2026)
Livri adicionada ao grupo. Responde apenas quando mencionada. Migração do grupo registrada nos logs (ID antigo: -5196571765).

---

*Criado: 26/03/2026 | Revisão mensal: deletar táticas vencidas.*
