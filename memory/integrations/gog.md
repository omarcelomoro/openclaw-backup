# GOG CLI — Google Workspace

**Instalado:** 26/03/2026
**Versão:** v0.12.0

## Contas autenticadas

| Conta | Serviços | Uso |
|-------|----------|-----|
| `atendimento@leevrecorretora.com.br` | Gmail, Calendar, Drive | Conta da Livri — envio de emails, automações |
| `marcelo@leevrecorretora.com.br` | Gmail, Calendar, Drive | Conta do Marcelo — monitoramento de agenda e email |

## Credenciais
- Client secret: `/root/.openclaw/gog_client_secret.json`
- Projeto Google Cloud: `livri-491419`
- Keyring password: `GOG_KEYRING_PASSWORD` no `.env`
- Conta padrão Livri: `GOG_ACCOUNT` no `.env`
- Conta Marcelo: `MARCELO_GOG_ACCOUNT` no `.env`

## Uso básico
```bash
export GOG_KEYRING_PASSWORD=...

# Calendário do Marcelo
gog calendar events marcelo@leevrecorretora.com.br --from 2026-03-26 --to 2026-04-05 --account marcelo@leevrecorretora.com.br

# Gmail do Marcelo
gog gmail search 'is:unread' --max 10 --account marcelo@leevrecorretora.com.br

# Enviar email pela conta da Livri
gog gmail send --to destinatario@email.com --subject "Assunto" --body "Mensagem" --account atendimento@leevrecorretora.com.br
```

## Calendário Marcelo — compromissos registrados (26/03/2026)
- 27/03 10h — Vencimento cobrança R$1.500,00 (AGENCIA POCT LTDA)
- 02/04 08h30 — Boleto La Mobili
- 02/04 10h30 — Boleto Itaú
- 05/04 — Aniversário (pessoa não identificada)
