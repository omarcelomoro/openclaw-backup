---
name: triagem-gmail-leevre
description: Triagem operacional e comercial de Gmail para a Leevre usando gog. Use quando Marcelo pedir priorização de inbox, classificação de emails, aplicação de labels, geração de digest, organização de follow-up, separação entre comercial, financeiro, operacional e administrativo, ou criação de rascunhos sem envio automático.
metadata:
  author: livri
  version: 1.0.0
  domain: leevre
  owner: main
---

# Triagem Gmail Leevre

## Objetivo
Organizar a caixa de entrada da Leevre com foco em prioridade, ação e visibilidade, sem automatizar demais cedo demais.

A função desta skill é transformar inbox em fila de decisão, não só em lista de mensagens.

## Ferramenta base
Usar `gog` para Gmail.

## Regra de segurança principal
- nunca enviar email automaticamente
- rascunho pode ser sugerido, mas envio exige confirmação
- preferir labels a mover ou deletar
- evitar automações irreversíveis
- se houver dúvida, resumir e pedir decisão

## Use quando
- precisar triar inbox
- precisar separar urgência de ruído
- precisar organizar follow-up
- precisar agrupar email por natureza de trabalho
- precisar gerar resumo executivo da caixa
- precisar sugerir resposta ou rascunho

## Não usar quando
- o pedido for enviar email sem revisão
- o pedido depender de ação externa sensível sem confirmação
- a infraestrutura do Gmail estiver sem autenticação válida

## Categorias base da Leevre
Usar estas categorias como ponto de partida:
- Urgente
- Responder Hoje
- Follow-up
- Comercial
- Financeiro
- Operacional
- Documentos
- Administrativo
- Ler Depois

## Lógica de triagem

### 1. Classificar por urgência real
Pergunta principal:
`isso precisa de atenção imediata, hoje, depois, ou só registro?`

### 2. Classificar por natureza
Pergunta principal:
`esse email é comercial, financeiro, operacional, administrativo ou apenas informativo?`

### 3. Classificar por próxima ação
Pergunta principal:
`responder, acompanhar, delegar, arquivar mentalmente, ou só ler depois?`

## Critérios práticos

### Urgente
Usar quando houver:
- prazo muito próximo
- problema com cliente
- cobrança sensível
- travamento operacional
- risco financeiro ou reputacional

### Responder Hoje
Usar quando:
- o tema exige retorno, mas não é crise
- existe oportunidade comercial quente
- existe pendência objetiva com baixa complexidade

### Follow-up
Usar quando:
- o próximo movimento depende de resposta alheia
- o email não é urgente agora, mas não pode sumir
- existe negociação ou pendência em andamento

### Comercial
Usar quando envolver:
- lead
- proposta
- negociação
- parceiro comercial
- oportunidade de receita

### Financeiro
Usar quando envolver:
- cobrança
- nota
- pagamento
- comissão
- conciliação
- boleto
- reembolso

### Operacional
Usar quando envolver:
- processo interno
- fluxo de equipe
- documento operacional
- seguradora ou administradora em tema de execução

### Documentos
Usar quando envolver:
- contrato
- apólice
- proposta formal
- anexos importantes
- comprovantes

### Administrativo
Usar quando envolver:
- acessos
- contas
- cadastro
- confirmação de sistema
- suporte técnico

### Ler Depois
Usar quando for:
- newsletter
- atualização não urgente
- conteúdo de referência
- material sem ação imediata

## Fluxo recomendado

### Etapa 1. Buscar emails
Usar busca orientada por janela recente, remetentes importantes ou labels existentes.

### Etapa 2. Resumir rapidamente
Para cada email relevante, extrair:
- remetente
- assunto
- natureza
- urgência
- ação sugerida

### Etapa 3. Aplicar lógica de prioridade
Separar o que:
- exige resposta agora
- exige resposta hoje
- entra em follow-up
- só precisa de leitura posterior

### Etapa 4. Organizar saída
Sempre que possível, devolver em blocos:
- urgentes
- responder hoje
- follow-up
- leitura posterior

### Etapa 5. Sugerir rascunhos
Se o pedido incluir resposta, sugerir rascunho curto e claro.
Nunca enviar sem confirmação.

## Formato preferido de digest

### Resumo executivo
- quantidade de emails críticos
- principais frentes abertas
- principal risco
- principal oportunidade

### Lista operacional
Para cada item importante:
- remetente
- assunto
- categoria
- urgência
- próxima ação

## Regras de linguagem
Ao resumir inbox para Marcelo:
- direto ao ponto
- sem excesso de detalhe inútil
- destacar decisão, risco e ação
- separar claramente fato de interpretação

## Alertas
- não transformar tudo em urgente
- não classificar newsletter como trabalho real
- não misturar comercial com financeiro quando a ação for diferente
- não esconder incerteza se o contexto estiver incompleto

## Casos úteis para a Leevre
- inbox comercial com leads e propostas
- inbox financeiro com comissão, nota e conciliação
- inbox operacional com seguradoras e administradoras
- inbox administrativo com acessos, sistemas e documentos

## Formato preferido de resposta
1. resumo executivo
2. itens urgentes
3. itens para hoje
4. follow-ups
5. rascunhos sugeridos, se aplicável
