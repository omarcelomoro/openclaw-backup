# Checklist de Implementação — Pipeline de Consórcio no HubSpot

## Objetivo
Subir o pipeline de consórcio da Leevre no HubSpot com critério operacional, usando a integração já existente via API.

A meta não é só criar etapas. É deixar o funil utilizável para gestão, follow-up e previsibilidade.

---

## Etapa 1 — Confirmar a base atual

### Checklist
- [ ] Validar se já existe pipeline separado para consórcio
- [ ] Confirmar se o pipeline atual de seguros continua isolado
- [ ] Listar stages existentes hoje no HubSpot
- [ ] Identificar propriedades já existentes que podem ser reaproveitadas
- [ ] Identificar propriedades duplicadas, vagas ou inúteis

### Saída esperada
- mapa do que já existe
- lista do que manter
- lista do que criar
- lista do que ajustar

---

## Etapa 2 — Criar ou ajustar o pipeline de consórcio

### Stages aprovados
- [ ] Lead Entrou
- [ ] Contato Iniciado
- [ ] Lead Qualificado
- [ ] Simulação Enviada
- [ ] Em Negociação
- [ ] Documentação / Fechamento
- [ ] Ganho
- [ ] Perdido
- [ ] Pausado / Sem timing

### Regras
- [ ] Não criar stage redundante
- [ ] Não misturar etapa comercial com etapa administrativa sem necessidade
- [ ] Garantir que cada etapa reflita avanço real

### Saída esperada
- pipeline criado ou ajustado
- ordem final de etapas validada

---

## Etapa 3 — Subir propriedades mínimas

### Propriedades obrigatórias
- [ ] origem do lead
- [ ] canal detalhado
- [ ] tipo de consórcio
- [ ] objetivo do cliente
- [ ] valor pretendido da carta
- [ ] valor ou faixa de parcela desejada
- [ ] perfil do cliente (PF/PJ)
- [ ] prioridade ou temperatura
- [ ] responsável
- [ ] próxima ação
- [ ] data do próximo follow-up
- [ ] data da última interação
- [ ] campo objeções
- [ ] mapa de decisão (roadmap to close)
- [ ] objeção principal
- [ ] motivo de perda
- [ ] motivo de pausa
- [ ] observações comerciais estruturadas

### Regras
- [ ] Padronizar nomes dos campos
- [ ] Evitar criar campo demais
- [ ] Priorizar campo que ajude a decidir ou acompanhar
- [ ] Usar opções fechadas quando fizer sentido

### Saída esperada
- propriedades criadas
- propriedades antigas consolidadas ou descartadas

---

## Etapa 4 — Padronizar opções fechadas

### Temperatura
- [ ] Quente
- [ ] Morno
- [ ] Frio
- [ ] Pausado

### Motivos de perda
- [ ] sem timing
- [ ] preço ou parcela não encaixou
- [ ] decidiu por outra solução
- [ ] fechou com concorrente
- [ ] perfil não aderente
- [ ] sem resposta após tentativas
- [ ] desistiu do objetivo

### Motivos de pausa
- [ ] aguardando organização financeira
- [ ] aguardando decisão familiar ou societária
- [ ] aguardando documento
- [ ] aguardando momento de compra
- [ ] voltou para análise futura

### Regras
- [ ] Não abrir opções demais
- [ ] Evitar motivo genérico tipo “outros” como padrão principal
- [ ] Garantir que motivos sirvam para leitura de gestão

---

## Etapa 5 — Definir regra de passagem entre etapas

### Checklist por etapa
- [ ] Lead Entrou exige origem, canal, responsável e data de entrada
- [ ] Contato Iniciado exige última interação, próxima ação e próximo follow-up
- [ ] Lead Qualificado exige tipo de consórcio, objetivo, perfil e temperatura
- [ ] Simulação Enviada exige valor de carta, parcela desejada e retorno previsto
- [ ] Em Negociação exige campo objeções, roadmap to close, objeção principal e próximo passo
- [ ] Documentação / Fechamento exige pendência principal e prazo
- [ ] Perdido exige motivo de perda
- [ ] Pausado exige motivo de pausa e data de retomada

### Regra-mãe
- [ ] Nenhum negócio sobe de etapa sem evidência real de avanço
- [ ] Nenhum negócio fica sem próxima ação, salvo ganho ou perdido

---

## Etapa 6 — Definir disciplina operacional

### Checklist
- [ ] Todo negócio tem responsável
- [ ] Todo negócio ativo tem próxima ação
- [ ] Todo negócio ativo tem data de follow-up
- [ ] Todo negócio perdido tem motivo
- [ ] Todo negócio pausado tem data de retomada
- [ ] Propostas enviadas não podem ficar sem revisão posterior

### Ritual sugerido
- [ ] revisão diária de urgentes e follow-ups vencidos
- [ ] revisão semanal de pipeline por etapa
- [ ] revisão quinzenal de perdas e pausas

---

## Etapa 7 — Validar leitura gerencial mínima

### Métricas que precisam existir
- [ ] quantidade por etapa
- [ ] negócios sem próxima ação
- [ ] negócios com follow-up vencido
- [ ] tempo por etapa
- [ ] taxa de avanço entre etapas
- [ ] perdas por motivo
- [ ] ganhos por origem

### Regra
- [ ] Se o HubSpot não entregar essa leitura com clareza, a configuração ainda não está boa

---

## Etapa 8 — Validar usabilidade com casos reais

### Teste mínimo
- [ ] criar ou revisar 5 a 10 negócios reais no pipeline
- [ ] testar preenchimento das propriedades mínimas
- [ ] testar passagem entre etapas
- [ ] testar leitura de follow-up vencido
- [ ] testar leitura de pausados e perdidos

### Perguntas de validação
- [ ] o time consegue preencher sem travar?
- [ ] a próxima ação ficou visível?
- [ ] o pipeline mostra gargalo de verdade?
- [ ] existe clareza do que cobrar e acompanhar?

---

## Etapa 9 — Preparar implementação via API

### Checklist
- [ ] mapear IDs do pipeline e das etapas
- [ ] mapear nomes internos das propriedades
- [ ] confirmar formatos de campo usados pela API
- [ ] listar o que será criado manualmente e o que pode ser automatizado depois
- [ ] evitar automação antes de validar o processo manual

### Regra
- [ ] primeiro clareza operacional
- [ ] depois automação

---

## Entregável final esperado
Ao final, a Leevre deve ter:
- pipeline de consórcio separado e funcional
- propriedades mínimas padronizadas
- critérios claros de movimentação
- leitura real de follow-up e gargalos
- base pronta para automação futura via API

---

## Ordem prática recomendada
1. mapear o que já existe
2. ajustar pipeline
3. criar propriedades mínimas
4. padronizar opções fechadas
5. definir regra de passagem
6. testar com negócios reais
7. só depois pensar em automação via API
