# Auditoria e Plano de Adaptação de Skills — Leevre

Data: 2026-04-09

## Escopo priorizado

Skills priorizadas para a operação da Leevre:
- telegram
- pdf
- pdf-extract
- excel-xlsx
- email-sequence
- campaign-analytics
- analytics-tracking

## Veredito resumido

### 1. telegram
- Risco: baixo
- Valor para Leevre: alto
- Uso principal: desenho de fluxos, comandos, update handling e comportamento do bot
- Adaptação necessária: governança de grupos, menções, comandos operacionais e proteção de tokens

### 2. pdf
- Risco: baixo
- Valor para Leevre: alto
- Uso principal: leitura, merge, split, geração e manipulação de PDFs
- Adaptação necessária: foco em apólices, relatórios de comissão, scripts comerciais e relatórios internos

### 3. pdf-extract
- Risco: baixo
- Valor para Leevre: alto
- Uso principal: extração rápida de texto de PDFs para processamento posterior
- Adaptação necessária: validar totais, documentos e identificadores antes de conciliação

### 4. excel-xlsx
- Risco: baixo
- Valor para Leevre: muito alto
- Uso principal: conciliação, controles, bases de comissão, higienização e importação/exportação
- Adaptação necessária: tipagem forte, cuidado com IDs longos, datas e fórmulas

### 5. email-sequence
- Risco: baixo
- Valor para Leevre: alto
- Uso principal: nurturing, onboarding, reativação e sequências comerciais
- Adaptação necessária: linguagem consultiva, foco patrimonial, fluxos de follow-up e indicação

### 6. campaign-analytics
- Risco: baixo
- Valor para Leevre: médio-alto
- Uso principal: atribuição, funil e ROI de campanhas
- Adaptação necessária: medir Instagram, TikTok, landing pages, WhatsApp, email e origem de fechamento

### 7. analytics-tracking
- Risco: baixo
- Valor para Leevre: alto
- Uso principal: plano de tracking, eventos, UTMs e padronização de conversões
- Adaptação necessária: definir eventos de negócio reais e nomenclatura única

## Skills avaliadas e não priorizadas agora

- gmail: depende de gateway externo e chave de terceiro, não priorizar agora
- imap-smtp-email: útil depois que a infra de email profissional estiver correta
- memory-manager: promissora, mas precisa compatibilizar com o modelo de memória atual do OpenClaw
- browser: útil, mas precisa revisão de escopo/segurança antes de uso operacional mais amplo
- document-parser: não priorizar, por dependência externa e baixo nível de confiança
- security-auditor: precisa limpeza e adaptação antes de adoção
- agent-memory: muito cru/incompleto no trecho recebido

## O que foi salvo no workspace

Criadas ou atualizadas as seguintes skills no workspace:
- skills/telegram/SKILL.md
- skills/pdf/SKILL.md
- skills/pdf-extract/SKILL.md
- skills/excel-xlsx/SKILL.md
- skills/email-sequence/SKILL.md
- skills/campaign-analytics/SKILL.md
- skills/analytics-tracking/SKILL.md

## Plano de uso na operação da Leevre

### Fase 1 — Operação e organização
Objetivo: ganhar controle operacional rápido

1. pdf-extract
- extrair texto de relatórios de comissão e PDFs operacionais

2. excel-xlsx
- estruturar conciliações
- padronizar bases
- preparar migração ou integração com CRM

3. pdf
- gerar relatórios internos e materiais comerciais em PDF

### Fase 2 — Marketing e crescimento
Objetivo: medir e melhorar aquisição

4. analytics-tracking
- criar plano de eventos
- padronizar UTMs
- definir nomenclatura de canais e campanhas

5. campaign-analytics
- analisar desempenho por canal
- identificar gargalos do funil
- calcular CPA, ROAS e ROI quando houver dados suficientes

6. email-sequence
- criar fluxos de nutrição
- pós-lead
- pós-proposta
- reativação
- indicação pós-contemplação

### Fase 3 — Interface e automação conversacional
Objetivo: melhorar governança do bot

7. telegram
- desenhar comandos úteis
- melhorar roteamento
- definir padrões para grupos e mensagens operacionais

## Ordem recomendada de implementação

1. excel-xlsx
2. pdf-extract
3. pdf
4. analytics-tracking
5. email-sequence
6. campaign-analytics
7. telegram

## Primeiras entregas recomendadas

### Entrega 1
Planilha mestre de conciliação de comissão
- entradas de seguradoras
- pagamentos recebidos
- pendências
- divergências

### Entrega 2
Pipeline de extração de PDFs para texto e planilha
- relatório PDF → texto bruto → tabela consolidada

### Entrega 3
Mapa de tracking da Leevre
- origem do lead
- canal
- campanha
- etapa do funil
- fechamento

### Entrega 4
Primeira sequência de email
- lead novo
- proposta enviada
- lead parado
- pedido de indicação

## Observações finais

- O pacote salvo hoje é uma base adaptada para a Leevre, não uma importação completa dos repositórios originais.
- A lógica foi preservar utilidade prática com baixo risco e sem introduzir dependências externas desnecessárias.
