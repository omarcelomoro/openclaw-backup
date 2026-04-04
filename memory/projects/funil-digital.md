# Funil Digital Leevre — Stack de Marketing

*Atualizado: 31/03/2026*

## Infraestrutura (VPS)

| Serviço | Porta | Status |
|---------|-------|--------|
| Evolution API (WhatsApp) | 8080 | ✅ Online |
| n8n (automações) | 5678 | ✅ Online |
| HubSpot (CRM) | cloud | ✅ Conectado |

## Canais de Distribuição

| Canal | Ferramenta | Status |
|-------|-----------|--------|
| WhatsApp | Evolution API v1.8.7 | ✅ Conectado |
| Email Marketing | Brevo | ⏳ Aguardando API key |
| Meta Ads | Pixel | ⏳ A configurar |
| Telegram Marketing | Bot OpenClaw | ✅ Chat -1003706469372 / Tópico 6 |

## Base de Clientes

- **955 registros** — 2021 a 2026
- **Sheet completo:** https://docs.google.com/spreadsheets/d/1Qe8mU9qatyjFEa5itvuDe5tebYGp4H3uLLzydUIXyiQ/edit
- **Renovações 90 dias:** https://docs.google.com/spreadsheets/d/13x9DTU_gG5RvFhyINk3FJhBVGvjMNu8xBHPCMzuGvvg/edit
  - 🔴 35 vencendo em Abril/2026
  - 🟢 18 vencendo em Maio-Junho/2026

## Automações n8n (a construir)

1. **Alerta de renovação** — 30/15/7 dias antes → WhatsApp + email ao cliente
2. **Notificação Marketing** — novos leads → Telegram grupo Marketing
3. **Lead novo WhatsApp** → HubSpot (criar contato + deal)
4. **Relatório semanal** → Telegram sexta 16h

## Próximos Passos

- [ ] Brevo: cadastrar e obter API key
- [ ] n8n: configurar workflows de renovação
- [ ] Meta Ads: pixel no site + audiência customizada da base
- [ ] Emails faltantes: coletar progressivamente via formulários/WhatsApp
