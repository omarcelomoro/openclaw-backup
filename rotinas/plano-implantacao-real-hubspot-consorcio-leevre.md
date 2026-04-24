# Plano de implantação real — HubSpot Consórcio Leevre

## Objetivo
Implantar o HubSpot como CRM exclusivo de consórcio da Leevre, com o menor nível de complexidade possível e com leitura gerencial real.

---

## Fase 1 — Limpar a direção

### Decisão já tomada
- HubSpot será usado apenas para consórcio por enquanto

### O que isso implica
- não desenhar campos pensando em seguro
- não manter lógica híbrida no pipeline
- usar o CRM para follow-up, negociação e fechamento de consórcio

---

## Fase 2 — Ajustar o pipeline

### Pipeline final a implementar
1. Lead Entrou
2. Contato Iniciado
3. Lead Qualificado
4. Simulação Enviada
5. Em Negociação
6. Documentação / Fechamento
7. Ganho
8. Perdido
9. Pausado / Sem timing

### Regras dessa fase
- não criar etapas extras por ansiedade
- cada etapa precisa refletir avanço real
- pausado deve existir separado de perdido

### Saída esperada
- pipeline criado ou ajustado com essas 9 etapas

---

## Fase 3 — Criar os campos prioritários

### Campos para subir primeiro
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

### Regra
Se houver dúvida entre criar tudo ou começar, começar por esses.

### Saída esperada
- base mínima operacional pronta

---

## Fase 4 — Criar os campos da segunda camada

### Campos da segunda camada
- data da última interação
- tipo de consórcio
- perfil do cliente
- valor ou faixa de parcela desejada
- administradora
- status da negociação
- pendência documental principal
- prazo da pendência
- valor final
- produto final
- data de fechamento
- concorrente
- observações comerciais estruturadas

### Regra
Só subir essa camada depois da primeira estar inteligível e utilizável.

---

## Fase 5 — Padronizar opções fechadas

### Temperatura
- Quente
- Morno
- Frio
- Pausado

### Objeção principal
- Agora não é o momento
- Preciso pensar melhor
- Ficou caro
- Vou comparar com outra opção
- Não entendi direito como funciona
- Tenho medo de errar
- Vou decidir com cônjuge ou sócio
- Perdi prioridade nisso agora

### Motivo de perda
- Sem timing
- Preço ou parcela não encaixou
- Decidiu por outra solução
- Fechou com concorrente
- Perfil não aderente
- Sem resposta após tentativas
- Desistiu do objetivo

### Motivo de pausa
- Aguardando organização financeira
- Aguardando decisão familiar ou societária
- Aguardando documento
- Aguardando momento de compra
- Voltou para análise futura

---

## Fase 6 — Definir regra de preenchimento por etapa

### Lead Entrou
Obrigatório:
- origem do lead
- canal detalhado
- responsável

### Contato Iniciado
Obrigatório:
- próxima ação
- data do próximo follow-up

### Lead Qualificado
Obrigatório:
- objetivo do cliente
- temperatura

### Simulação Enviada
Obrigatório:
- valor pretendido da carta

### Em Negociação
Obrigatório:
- campo objeções
- objeção principal
- roadmap to close
- próxima ação
- data do próximo follow-up

### Documentação / Fechamento
Obrigatório:
- pendência documental principal
- próxima ação

### Perdido
Obrigatório:
- motivo de perda

### Pausado / Sem timing
Obrigatório:
- motivo de pausa
- data de retomada

---

## Fase 7 — Teste com deals reais

### Teste mínimo
Usar 5 a 10 deals reais.

### Validar
- se o time consegue preencher sem travar
- se a próxima ação aparece com clareza
- se follow-up vencido fica visível
- se negociação deixa claro o que falta para fechar
- se pausado não vira cemitério

### Critério de aprovação
Só seguir se o CRM estiver ajudando a decidir e cobrar.

---

## Fase 8 — Leitura gerencial mínima

O HubSpot precisa responder com clareza:
- quantos deals existem por etapa
- quais estão sem próxima ação
- quais estão com follow-up vencido
- quais estão pausados sem retomada
- quais perdas estão concentradas por motivo
- quais origens geram mais ganho

---

## Fase 9 — Só depois pensar em automação

Automação futura pode entrar para:
- alertar deals sem próxima ação
- alertar follow-up vencido
- consolidar origem
- gerar relatórios

### Não automatizar cedo
- mudança automática de etapa
- preenchimento de campo crítico por inferência fraca
- automação comercial pesada sem validação manual

---

## Ordem prática resumida
1. ajustar pipeline
2. subir campos prioritários
3. subir opções fechadas
4. definir obrigatórios por etapa
5. testar com deals reais
6. validar leitura gerencial
7. só depois automatizar

---

## Próximo passo imediato recomendado
Abrir o HubSpot e executar a implantação manual da Fase 2 e Fase 3 primeiro.
