# Estrutura final enxuta — Pipeline de Consórcio no HubSpot (Leevre)

## Decisão de contexto
O HubSpot da Leevre fica dedicado **somente a consórcio por enquanto**.

Objetivo:
- dar visibilidade comercial real
- organizar follow-up
- evitar deals sem próxima ação
- registrar objeções e caminho até o fechamento
- preparar base para automação futura sem bagunça

---

## Pipeline final recomendado

### 1. Lead Entrou
**Objetivo:** registrar entrada e origem do lead.

**Campos mínimos:**
- origem do lead
- canal detalhado
- responsável
- data de entrada

---

### 2. Contato Iniciado
**Objetivo:** garantir que houve abordagem e que existe próxima ação.

**Campos mínimos:**
- data da última interação
- próxima ação
- data do próximo follow-up

---

### 3. Lead Qualificado
**Objetivo:** confirmar aderência mínima do lead ao processo.

**Campos mínimos:**
- tipo de consórcio
- objetivo do cliente
- perfil do cliente
- temperatura

---

### 4. Simulação Enviada
**Objetivo:** registrar cenário apresentado.

**Campos mínimos:**
- valor pretendido da carta
- valor ou faixa de parcela desejada
- administradora (quando aplicável)

---

### 5. Em Negociação
**Objetivo:** deixar clara a trava comercial e o caminho até fechar.

**Campos mínimos:**
- campo objeções
- objeção principal
- mapa de decisão (roadmap to close)
- status da negociação
- próxima ação
- data do próximo follow-up

**Regra:**
nenhuma deal deve ficar em negociação sem clareza sobre:
- o que está travando
- quem decide
- o que falta acontecer
- qual é o próximo marco

---

### 6. Documentação / Fechamento
**Objetivo:** acompanhar o fechamento sem perder pendência crítica.

**Campos mínimos:**
- pendência documental principal
- prazo da pendência
- próxima ação
- data do próximo follow-up

---

### 7. Ganho
**Objetivo:** consolidar o fechamento.

**Campos mínimos:**
- valor final
- produto final
- data de fechamento

---

### 8. Perdido
**Objetivo:** registrar perda de forma gerencial.

**Campos mínimos:**
- motivo de perda
- concorrente (quando aplicável)

---

### 9. Pausado / Sem timing
**Objetivo:** evitar que deal parada vire cemitério.

**Campos mínimos:**
- motivo de pausa
- data de retomada

---

## Campos prioritários para começar
Se precisar subir a versão mais enxuta primeiro, começar por estes:
- origem do lead
- canal detalhado
- responsável
- próxima ação
- data do próximo follow-up
- temperatura
- objetivo do cliente
- valor pretendido da carta
- campo objeções
- objeção principal
- roadmap to close
- motivo de perda
- motivo de pausa
- data de retomada

---

## Regras operacionais obrigatórias
- toda deal ativa precisa de responsável
- toda deal ativa precisa de próxima ação
- toda deal ativa precisa de data de follow-up
- nenhuma deal sobe de etapa sem evidência real de avanço
- deal pausada precisa de motivo e data de retomada
- deal perdida precisa de motivo de perda

---

## Como usar os 2 campos novos

### Campo objeções
Registrar a objeção real do lead em linguagem objetiva.

Exemplo:
- cliente quer carta maior, mas parcela confortável não fecha
- esposa ainda não está convencida
- compara com financiamento e ainda não entendeu a estratégia

### Roadmap to close
Responder:
- o que falta para fechar
- quem decide
- qual trava principal existe
- qual é o próximo marco

Exemplo:
- casal avaliando carta de 300k vs 400k
- decisão depende de alinhamento financeiro
- trava principal: esposa ainda insegura
- próximo marco: revisar cenário final até terça
- se aprovar, avança para documentação

---

## Leitura gerencial mínima
O CRM precisa permitir enxergar:
- quantidade por etapa
- deals sem próxima ação
- follow-ups vencidos
- perdas por motivo
- ganhos por origem
- deals pausadas sem data de retomada

---

## Próximo passo recomendado
1. criar ou ajustar pipeline de consórcio
2. subir campos prioritários
3. testar com 5 a 10 deals reais
4. só depois pensar em automação via API
