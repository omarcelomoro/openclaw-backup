# Auditoria HubSpot Leevre — 30/04/2026

## Diagnóstico direto

O HubSpot está conectado e funcional, mas ainda não virou o cérebro comercial da Leevre. Hoje ele está mais próximo de um quadro genérico de negócios do que de um CRM desenhado para consórcio + seguros.

## Estado encontrado

### Pipeline existente

Existe apenas um pipeline principal: **Pipeline de negócios** (`default`).

Etapas atuais:
1. Lead Recebido — 20%
2. Primeiro Contato — 40%
3. Simulação Enviada — 60%
4. Proposta Aceita — 80%
5. Contrato Assinado — 90%
6. Ganho — 100%
7. Perdido — 0%

### Deals existentes

Foram encontrados deals de renovação de seguros de abril/2026 dentro do pipeline `default`, misturados no mesmo funil pensado para vendas gerais/consórcio.

Amostras:
- Renovação seguro auto — Endrio Scabelo — Allianz — R$262,51 — venc. 01/04/2026
- Renovação seguro auto — Humberto Carvalho — Banestes — R$2.094,73 — venc. 30/04/2026
- Renovação seguro auto — Leonardo Senatore — Allianz — R$385,17 — venc. 30/04/2026
- Vários deals Porto sem prêmio preenchido

### Propriedades customizadas encontradas

Deals:
- `consorcio_canal_detalhado`
- `consorcio_mensagem_inicial`
- `consorcio_origem_lead`

Contacts:
- `linkedin_account`

### Propriedades essenciais ausentes

No objeto Deal, não existem propriedades estruturadas para:
- produto
- segmento
- administradora
- valor de crédito/carta
- comissão prevista
- comissão recebida
- origem do lead genérica
- corretor/produtor responsável
- vigência/vencimento
- seguradora
- placa
- CPF

No objeto Contact, não existem propriedades estruturadas para:
- CPF
- perfil de cliente
- renda/faixa de renda
- origem do lead
- cidade/estado estruturados

## Conclusão

O problema não é acesso nem ferramenta. O problema é modelagem.

O HubSpot precisa ser separado em dois fluxos operacionais:

1. **Consórcio** — funil de aquisição/venda, meta 2026, ticket alto, comissão alta.
2. **Seguros/Renovações** — funil operacional recorrente, vencimento, prêmio, seguradora, status de renovação.

Misturar os dois no mesmo pipeline enfraquece relatório, automação e prioridade comercial.

## Recomendação de estrutura

### Pipeline 1 — Consórcio

Nome sugerido: `Consórcio — Vendas`

Etapas sugeridas:
1. Lead Novo
2. Qualificado
3. Diagnóstico / Entrevista
4. Simulação Enviada
5. Follow-up / Negociação
6. Proposta Aceita
7. Contrato Assinado
8. Ganho
9. Perdido

### Pipeline 2 — Seguros

Nome sugerido: `Seguros — Renovações`

Etapas sugeridas:
1. Renovação Mapeada
2. Contato Pendente
3. Cotação Solicitada
4. Cotação Enviada
5. Cliente em Análise
6. Renovado / Ganho
7. Perdido
8. Sem Contato

## Propriedades recomendadas — Deals

### Comuns
- `produto_leevre` — Consórcio, Seguro Auto, Seguro Residencial, Seguro Empresarial, Seguro Saúde, Outro
- `origem_lead` — Instagram, Indicação, WhatsApp, Base antiga, Tráfego pago, Prospecção ativa, Renovação, Outro
- `produtor_responsavel` — Marcelo, Gustavo, Fabrício, Outro
- `status_operacional` — Novo, Em andamento, Pendente Marcelo, Pendente cliente, Concluído, Perdido
- `observacao_operacional` — texto longo

### Consórcio
- `tipo_consorcio` — Imóvel, Auto, Capital de giro, Outro
- `administradora` — Itaú, Bradesco, Servopa, Porto, Outra
- `valor_credito` — número/moeda
- `prazo_meses` — número
- `parcela_estimativa` — moeda
- `comissao_prevista` — moeda
- `comissao_recebida` — moeda
- `temperatura_lead` — Frio, Morno, Quente
- `motivo_perda` — Sem perfil, Sem retorno, Preço/parcela, Comprou fora, Momento errado, Outro

### Seguros
- `seguradora` — Porto, Allianz, HDI, Banestes, Outra
- `ramo_seguro` — Auto, Residencial, Empresarial, Saúde, Vida, Outro
- `data_vencimento` — data
- `premio_atual` — moeda
- `premio_renovacao` — moeda
- `placa` — texto
- `numero_apolice` — texto
- `renovacao_urgencia` — Vencido, 0-7 dias, 8-15 dias, 16-30 dias, 30+ dias

## Propriedades recomendadas — Contacts

- `cpf_cnpj` — texto
- `cidade` — texto
- `estado` — texto/lista
- `perfil_cliente` — PF, PJ, Empresário, Investidor, Família, Outro
- `faixa_renda` — até 5k, 5-10k, 10-20k, 20k+
- `interesse_principal` — Consórcio imóvel, Consórcio auto, Seguro, Investimento patrimonial, Outro
- `origem_primeiro_contato` — Instagram, Indicação, WhatsApp, Base antiga, Tráfego pago, Outro

## Plano de 90 dias

### 0–7 dias

- Criar pipeline separado de seguros/renovações.
- Criar propriedades mínimas obrigatórias.
- Migrar os deals de renovação de abril para o pipeline correto.
- Preencher prêmios Porto pendentes.
- Definir campos obrigatórios para novos deals.

### 8–30 dias

- Criar workflow n8n: renovação 30/15/7/0 dias → alerta Telegram + tarefa no HubSpot.
- Criar workflow de lead WhatsApp → HubSpot → alerta Telegram.
- Padronizar origem de lead e produtor responsável.
- Criar dashboard simples: PL vendido, comissão prevista, negócios por etapa, renovações próximas.

### 31–90 dias

- Integrar Agger para puxar cadastros/dados faltantes.
- Automatizar relatórios semanais de vendas e metas.
- Rodar rotina comercial semanal: pipeline review sexta 16h.
- Criar briefing automático antes de reuniões comerciais.

## Ordem de implementação recomendada

1. Criar propriedades mínimas.
2. Criar pipeline `Seguros — Renovações`.
3. Manter pipeline atual como base do `Consórcio — Vendas` ou renomear depois.
4. Migrar deals de renovação para pipeline correto.
5. Preencher prêmios faltantes.
6. Ativar workflows n8n após credencial Telegram.

## Ação que exige aprovação

Não executei nenhuma mudança no HubSpot.

Para implementar, preciso de confirmação explícita porque altera CRM/base operacional.
