# Plano de Execução — HubSpot API para Pipeline de Consórcio da Leevre

## Objetivo
Separar com clareza o que deve ser feito manualmente agora, o que precisa ser validado e o que só vale automatizar depois no HubSpot.

A lógica é simples:
**não automatizar bagunça.**

---

## Visão geral

### Frente 1 — Fazer manualmente agora
Usar quando a prioridade for subir base operacional correta.

### Frente 2 — Validar antes de automatizar
Usar para testar se o desenho realmente funciona no dia a dia.

### Frente 3 — Automatizar depois via API
Usar apenas no que já estiver claro, estável e útil.

---

## Frente 1 — Fazer manualmente agora

### 1. Mapear estado atual do HubSpot
Executar primeiro:
- listar pipelines atuais
- identificar se já existe pipeline de consórcio
- mapear stages existentes
- mapear propriedades já existentes
- identificar duplicações, lacunas e campos inúteis

### Saída esperada
- inventário do pipeline atual
- inventário das propriedades atuais
- lista do que reaproveitar
- lista do que criar

---

### 2. Ajustar a estrutura do pipeline
Executar manualmente primeiro para evitar erro estrutural automatizado.

Criar ou revisar estas etapas:
- Lead Entrou
- Contato Iniciado
- Lead Qualificado
- Simulação Enviada
- Em Negociação
- Documentação / Fechamento
- Ganho
- Perdido
- Pausado / Sem timing

### Saída esperada
- pipeline final definido
- stages ordenados corretamente
- critérios de passagem alinhados

---

### 3. Criar propriedades mínimas essenciais
Subir manualmente primeiro para validar utilidade real.

Criar ou revisar:
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

### Saída esperada
- propriedades mínimas ativas
- nomes padronizados
- opções fechadas definidas

---

### 4. Subir opções fechadas úteis
Padronizar manualmente antes de qualquer automação.

#### Temperatura
- Quente
- Morno
- Frio
- Pausado

#### Motivo de perda
- sem timing
- preço ou parcela não encaixou
- decidiu por outra solução
- fechou com concorrente
- perfil não aderente
- sem resposta após tentativas
- desistiu do objetivo

#### Motivo de pausa
- aguardando organização financeira
- aguardando decisão familiar ou societária
- aguardando documento
- aguardando momento de compra
- voltou para análise futura

---

## Frente 2 — Validar antes de automatizar

### 5. Testar com negócios reais
Rodar com 5 a 10 negócios reais antes de qualquer automação.

Validar:
- preenchimento dos campos
- leitura da próxima ação
- passagem entre etapas
- clareza do follow-up
- leitura de perdas e pausas

### Critério de aprovação
Só seguir se ficar claro que:
- o time consegue usar
- os campos ajudam de verdade
- os gargalos aparecem
- o pipeline não virou burocracia

---

### 6. Validar leitura gerencial mínima
Checar se o HubSpot já consegue mostrar com clareza:
- quantidade por etapa
- follow-ups vencidos
- negócios sem próxima ação
- tempo por etapa
- perdas por motivo
- ganhos por origem

### Regra
Se essa leitura ainda não estiver boa, parar aqui e ajustar estrutura antes de automatizar.

---

### 7. Definir o que fica obrigatório
Antes de API, definir regras operacionais humanas.

Obrigatório em todo negócio ativo:
- responsável
- próxima ação
- data do próximo follow-up

Obrigatório em negócios perdidos:
- motivo de perda

Obrigatório em negócios pausados:
- motivo de pausa
- data de retomada

---

## Frente 3 — Automatizar depois via API

### 8. Mapear recursos técnicos para API
Só depois da validação operacional.

Mapear:
- ID do pipeline
- IDs das etapas
- nomes internos das propriedades
- tipo de cada propriedade
- campos obrigatórios por etapa

### Saída esperada
- mapa técnico pronto para integração

---

### 9. Automatizações que fazem sentido depois
Estas são boas candidatas futuras, não agora:

#### A. Criação padronizada de negócio
Quando um lead qualificado entrar por origem específica.

#### B. Atualização automática de propriedades de rotina
Exemplo:
- data da última interação
- responsável padrão em determinadas entradas
- origem consolidada

#### C. Alertas operacionais
Exemplo:
- negócio sem próxima ação
- follow-up vencido
- negócio parado tempo demais em etapa crítica

#### D. Relatórios e painéis automáticos
Exemplo:
- perdas por motivo
- avanço por etapa
- ganhos por origem

---

### 10. Automatizações que não devem entrar cedo
Evitar no começo:
- mover etapa automaticamente sem validação humana
- preencher campo crítico por inferência fraca
- disparar automação comercial pesada antes de testar processo
- mascarar falta de disciplina com automação

---

## Ordem recomendada de execução
1. mapear estado atual
2. ajustar pipeline manualmente
3. subir propriedades mínimas
4. padronizar opções fechadas
5. testar com negócios reais
6. validar leitura gerencial
7. definir obrigatórios operacionais
8. mapear IDs e nomes internos para API
9. só então escolher automações úteis

---

## Critério de sucesso
O plano deu certo quando a Leevre tiver:
- pipeline de consórcio separado
- preenchimento mínimo viável funcionando
- próxima ação visível
- follow-up vencido visível
- perdas e pausas padronizadas
- base pronta para automação sem bagunça

---

## Próximo entregável natural
Depois deste plano, o próximo artefato ideal é:
- um mapa técnico de implementação, com
  - nome do campo
  - nome interno
  - tipo
  - obrigatório ou não
  - stage em que passa a ser exigido
