# Projeto: Funil Digital & Automação

**Status:** backlog
**Criado:** 27/03/2026

---

## Contexto

Hoje 99% das vendas do Marcelo são offline via rede de relacionamento.
Objetivo: criar presença digital, gerar leads online e automatizar o funil de vendas.

## Canais e Fontes de Lead

- **Atual:** 100% offline — rede de relacionamento pessoal
- **Futuro:** Instagram, TikTok, tráfego pago (Meta Ads / Google Ads), email, indicação

## Componentes do Projeto

### 1. WhatsApp Business API
- Marcelo usa WhatsApp Business (não o comum) — ✅ já tem a base
- Automação via **Z-API** ou **Evolution API** (self-hosted no VPS)
- Fluxo: lead entra → bot qualifica → agenda reunião → CRM atualiza

### 2. Gestão de Redes Sociais
- Instagram @omarcelomoro + TikTok @omarcelo.moro
- Crescimento orgânico + tráfego pago
- Automação de postagens (Buffer, Later ou n8n)

### 3. Email Marketing
- Campanhas automatizadas
- Plataforma a definir: Resend (já no radar), Mailchimp ou ActiveCampaign
- Fluxos: boas-vindas, nurturing, follow-up pós-reunião

### 4. Marketing de Indicação
- Fluxo automatizado de referral
- Estruturar mecanismo de recompensas para indicadores
- Integrar com WhatsApp e email

### 5. Tráfego Pago
- Meta Ads (Instagram/Facebook)
- Google Ads (busca por "consórcio imóvel [cidade]")
- Pixel de conversão + CRM integrado

## Próximos Passos

1. Configurar WhatsApp Business API (Z-API ou Evolution API)
2. Definir CRM (necessário antes de automatizar funil)
3. Criar landing page de captura de leads
4. Estruturar fluxo de email marketing
5. Ativar tráfego pago após funil validado manualmente

## Pendência adicionada — 30/03/2026

### To-do: Integração Slack + CRM + Automação SDR→BDR

**Objetivo:** SDR (agente IA) qualifica lead → preenche CRM automaticamente → BDR recebe lead quente com contexto completo

**Decisões que precisam ser tomadas primeiro:**
1. Qual CRM? (HubSpot Free, RD Station, Pipedrive — decidir antes de integrar)
2. Quer usar Slack interno ou só WhatsApp + Telegram?
3. SDR será agente IA (Evolution API) ou humano inicialmente?

**Stack proposta (após decisão de CRM):**
- Evolution API (WhatsApp) → n8n → CRM → notifica BDR no Slack/Telegram
- Agente IA qualifica via WhatsApp → extrai: nome, renda, produto de interesse, urgência → cria card no CRM
- BDR recebe card já preenchido com score do lead

**Bloqueia:** definição do CRM
