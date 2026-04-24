---
name: pipeline-consorcio-hubspot-leevre
description: Estrutura operacional do pipeline de consórcio da Leevre no HubSpot. Use quando Marcelo pedir organização de pipeline, stages, propriedades mínimas, regras de movimentação, visibilidade comercial, higiene de CRM, disciplina de próxima ação, motivo de perda, pausas, ou desenho operacional do funil de consórcio considerando que o HubSpot já está integrado via API.
metadata:
  author: livri
  version: 1.0.0
  domain: leevre
  owner: main
---

# Pipeline Consórcio HubSpot Leevre

## Objetivo
Transformar o pipeline de consórcio da Leevre em ferramenta de gestão real, não vitrine bonita.

Esta skill existe para garantir visibilidade comercial, disciplina de avanço e leitura clara do funil no HubSpot, partindo do fato de que a integração via API já existe.

## Princípio central
Se um pipeline não ajuda a decidir, cobrar, priorizar e acompanhar, ele virou burocracia.

## Base operacional
- HubSpot já está integrado via API
- consórcio e seguro não devem usar o mesmo raciocínio operacional
- o pipeline de consórcio precisa refletir a jornada comercial real
- cada negócio precisa ter responsável, próxima ação e estágio coerente

## Use quando
- precisar desenhar ou revisar pipeline de consórcio
- precisar definir stages
- precisar padronizar propriedades mínimas
- precisar decidir regra de passagem entre etapas
- precisar melhorar previsibilidade comercial
- precisar organizar pausa, perda e follow-up
- precisar usar a integração do HubSpot com mais disciplina

## Não usar quando
- o pedido for auditoria ampla de todo o HubSpot, nesse caso complementar com `auditoria-hubspot-leevre`
- o pedido for copy ou comunicação comercial
- o problema for falta total de processo comercial fora do CRM

## Estrutura recomendada de pipeline

### 1. Lead Entrou
Entrou no radar, mas ainda sem contato útil.

**Condição para estar aqui**
- lead criado
- origem registrada
- responsável definido

**Não pode faltar**
- origem do lead
- canal detalhado
- responsável
- data de entrada

### 2. Contato Iniciado
Houve tentativa ou início de contato.

**Condição para mover**
- primeiro contato feito ou tentativa relevante registrada

**Não pode faltar**
- data da última interação
- próxima ação
- data do próximo follow-up

### 3. Lead Qualificado
Existe aderência mínima para seguir.

**Condição para mover**
- perfil faz sentido
- objetivo está razoavelmente claro
- interesse é real

**Não pode faltar**
- tipo de consórcio
- objetivo do cliente
- perfil PF ou PJ
- prioridade ou temperatura

### 4. Simulação Enviada
Cliente recebeu material ou proposta inicial.

**Condição para mover**
- simulação enviada de fato
- data registrada

**Não pode faltar**
- valor pretendido da carta
- faixa ou valor de parcela desejada
- administradora, se já aplicável
- próxima ação de retorno

### 5. Em Negociação
Existe conversa ativa para destravar decisão.

**Condição para mover**
- houve retorno, dúvida, ajuste ou objeção real
- oportunidade ainda está viva

**Não pode faltar**
- objeção principal
- status da negociação
- próximo passo claro

### 6. Documentação / Fechamento
Entrou em fase de fechamento operacional.

**Condição para mover**
- cliente sinalizou avanço real
- documentação ou formalização está em andamento

**Não pode faltar**
- pendência documental principal
- responsável pelo próximo passo
- prazo da pendência

### 7. Ganho
Negócio fechado.

**Não pode faltar**
- valor final
- produto final
- data de fechamento
- origem consolidada

### 8. Perdido
Negócio não avançou.

**Não pode faltar**
- motivo de perda padronizado
- observação curta do contexto
- concorrente, se relevante

### 9. Pausado / Sem timing
Negócio não morreu, mas não está no momento.

**Condição para mover**
- pausa declarada ou inferida com clareza
- existe motivo explícito

**Não pode faltar**
- motivo de pausa
- data sugerida de retomada
- próxima ação futura

## Propriedades mínimas obrigatórias
Estas são as propriedades mínimas para o pipeline ser útil:
- origem do lead
- canal detalhado
- tipo de consórcio
- objetivo do cliente
- valor pretendido da carta
- valor ou faixa de parcela desejada
- perfil do cliente (PF/PJ)
- prioridade ou temperatura
- responsável
- próxima ação
- data do próximo follow-up
- data da última interação
- objeção principal
- motivo de perda
- motivo de pausa
- observações comerciais estruturadas

## Regras de higiene do CRM
- negócio sem próxima ação está mal gerido
- stage sem critério claro gera funil mentiroso
- campo demais destrói preenchimento
- campo de menos destrói gestão
- perdido sem motivo padronizado é aprendizado desperdiçado
- pausado sem data vira cemitério de oportunidade

## Regras de movimentação
Antes de mover etapa, checar:
1. existe evidência real de avanço?
2. os campos mínimos da etapa foram preenchidos?
3. existe próxima ação clara?

Se a resposta for não, não mover só para “deixar bonito”.

## Motivos de perda sugeridos
Padronizar poucos motivos úteis:
- sem timing
- preço ou parcela não encaixou
- decidiu por outra solução
- fechou com concorrente
- perfil não aderente
- sem resposta após tentativas
- desistiu do objetivo

## Motivos de pausa sugeridos
- aguardando organização financeira
- aguardando decisão familiar ou societária
- aguardando documento
- aguardando momento de compra
- voltou para análise futura

## Métricas mínimas úteis
Com HubSpot integrado via API, priorizar leitura operacional real:
- quantidade por etapa
- tempo por etapa
- taxa de avanço entre etapas
- negócios sem próxima ação
- negócios com follow-up vencido
- perdas por motivo
- ganhos por origem

## Saídas esperadas
Quando usar esta skill, priorizar uma destas entregas:
- desenho de pipeline
- revisão de stages
- lista de propriedades mínimas
- regra de passagem entre etapas
- diagnóstico de higiene do CRM
- leitura de gargalos de pipeline

## Formato preferido de resposta
1. leitura do pipeline atual ou desejado
2. gargalos principais
3. stages recomendados
4. propriedades mínimas
5. regras operacionais
6. próximos ajustes no HubSpot
