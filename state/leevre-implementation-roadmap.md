# Roadmap de Implementação — Skills da Leevre

Data: 2026-04-09

## Objetivo
Implementar as 7 skills priorizadas da Leevre de forma prática, começando pelo maior gargalo operacional e depois avançando para marketing, tracking e automação.

## Ordem de implementação

### Fase 1 — Operação e controle
1. `excel-xlsx`
2. `pdf-extract`
3. `pdf`

### Fase 2 — Medição e crescimento
4. `analytics-tracking`
5. `email-sequence`
6. `campaign-analytics`

### Fase 3 — Bot e automação conversacional
7. `telegram`

## Implementação por fase

### Fase 1 — Operação e controle

#### Skill: excel-xlsx
Uso na Leevre:
- planilha mestre de comissão
- conciliação de pagamentos
- controle de pendências
- base de produção por produtor
- importação/exportação para CRM

Entregas:
- template de conciliação
- dicionário de colunas
- rotina mensal de fechamento

#### Skill: pdf-extract
Uso na Leevre:
- extrair texto de relatórios de comissão
- capturar dados de apólices e comunicados
- transformar PDF em base tratável

Entregas:
- fluxo PDF → texto
- checklist de validação de totais
- estrutura de pasta por seguradora/mês

#### Skill: pdf
Uso na Leevre:
- consolidar relatórios em PDF
- gerar materiais internos
- gerar relatórios executivos e scripts

Entregas:
- modelo de relatório operacional
- modelo de resumo executivo mensal

### Fase 2 — Medição e crescimento

#### Skill: analytics-tracking
Uso na Leevre:
- mapear origem dos leads
- rastrear funil de venda
- medir canal, campanha, criativo e conversão

Entregas:
- dicionário de eventos
- padrão de UTM
- mapa do funil

#### Skill: email-sequence
Uso na Leevre:
- lead novo
- lead parado
- proposta enviada
- pós-venda
- pedido de indicação

Entregas:
- 4 sequências base
- regras de entrada e saída
- CTA por etapa

#### Skill: campaign-analytics
Uso na Leevre:
- medir ROI por canal
- avaliar criativos
- medir conteúdo e campanhas

Entregas:
- painel de análise por canal
- relatório mensal de performance

### Fase 3 — Bot e automação

#### Skill: telegram
Uso na Leevre:
- comandos úteis
- alertas operacionais
- notificações de pendência
- resumos rápidos de indicadores

Entregas:
- mapa de comandos
- regras de grupos
- notificações críticas

## Regra de implementação
- Sempre começar por algo que elimine retrabalho manual.
- Só automatizar depois de definir a estrutura mínima do processo.
- Validar 1 fluxo real antes de escalar.

## Próximo passo imediato
Implementar a rotina operacional de comissão e conciliação usando `excel-xlsx` + `pdf-extract`.
