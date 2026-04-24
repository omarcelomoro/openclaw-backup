# Checklist de execução mão na massa — HubSpot Consórcio Leevre

## Objetivo
Executar a implantação do HubSpot da Leevre para consórcio, sem depender de interpretação solta no meio do processo.

---

## Bloco 1 — Preparação rápida

### Antes de começar
- [ ] Confirmar que o HubSpot será usado apenas para consórcio por enquanto
- [ ] Abrir o arquivo `rotinas/estrutura-final-pipeline-consorcio-hubspot-leevre.md`
- [ ] Abrir o arquivo `rotinas/mapa-tecnico-campos-pipeline-consorcio-hubspot-leevre.md`
- [ ] Confirmar quem será o responsável principal pelos deals

---

## Bloco 2 — Ajustar ou criar o pipeline

### Ação
No HubSpot, abrir:
**Configurações > Objetos > Negócios > Pipelines**

### Executar
- [ ] Localizar o pipeline atual de negócios
- [ ] Decidir se ele será reaproveitado para consórcio ou se será criado um novo pipeline específico
- [ ] Garantir que o pipeline final tenha estas etapas, nesta ordem:
  - [ ] Lead Entrou
  - [ ] Contato Iniciado
  - [ ] Lead Qualificado
  - [ ] Simulação Enviada
  - [ ] Em Negociação
  - [ ] Documentação / Fechamento
  - [ ] Ganho
  - [ ] Perdido
  - [ ] Pausado / Sem timing
- [ ] Remover ou renomear etapas que não façam sentido para o fluxo de consórcio

### Validar
- [ ] Não ficou etapa redundante
- [ ] Existe etapa separada para pausado
- [ ] O pipeline reflete avanço real, não sensação de avanço

---

## Bloco 3 — Criar os campos prioritários

### Ação
No HubSpot, abrir:
**Configurações > Propriedades > Negócios**

### Criar primeiro estes campos
- [ ] origem do lead
- [ ] canal detalhado
- [ ] próxima ação
- [ ] data do próximo follow-up
- [ ] temperatura
- [ ] objetivo do cliente
- [ ] valor pretendido da carta
- [ ] campo objeções
- [ ] objeção principal
- [ ] roadmap to close
- [ ] motivo de perda
- [ ] motivo de pausa
- [ ] data de retomada

### Confirmar reaproveitamento de campo nativo
- [ ] responsável → usar owner nativo, se estiver ok
- [ ] data de entrada → verificar se campo nativo resolve
- [ ] data de fechamento → verificar se campo nativo resolve

---

## Bloco 4 — Criar a segunda camada de campos

### Criar depois que a camada 1 estiver pronta
- [ ] data da última interação
- [ ] tipo de consórcio
- [ ] perfil do cliente
- [ ] valor ou faixa de parcela desejada
- [ ] administradora
- [ ] status da negociação
- [ ] pendência documental principal
- [ ] prazo da pendência
- [ ] valor final
- [ ] produto final
- [ ] concorrente
- [ ] observações comerciais estruturadas

---

## Bloco 5 — Padronizar opções fechadas

### Temperatura
- [ ] Quente
- [ ] Morno
- [ ] Frio
- [ ] Pausado

### Objeção principal
- [ ] Agora não é o momento
- [ ] Preciso pensar melhor
- [ ] Ficou caro
- [ ] Vou comparar com outra opção
- [ ] Não entendi direito como funciona
- [ ] Tenho medo de errar
- [ ] Vou decidir com cônjuge ou sócio
- [ ] Perdi prioridade nisso agora

### Motivo de perda
- [ ] Sem timing
- [ ] Preço ou parcela não encaixou
- [ ] Decidiu por outra solução
- [ ] Fechou com concorrente
- [ ] Perfil não aderente
- [ ] Sem resposta após tentativas
- [ ] Desistiu do objetivo

### Motivo de pausa
- [ ] Aguardando organização financeira
- [ ] Aguardando decisão familiar ou societária
- [ ] Aguardando documento
- [ ] Aguardando momento de compra
- [ ] Voltou para análise futura

---

## Bloco 6 — Definir obrigatoriedade prática por etapa

### Lead Entrou
- [ ] origem do lead
- [ ] canal detalhado
- [ ] responsável

### Contato Iniciado
- [ ] próxima ação
- [ ] data do próximo follow-up

### Lead Qualificado
- [ ] objetivo do cliente
- [ ] temperatura

### Simulação Enviada
- [ ] valor pretendido da carta

### Em Negociação
- [ ] campo objeções
- [ ] objeção principal
- [ ] roadmap to close
- [ ] próxima ação
- [ ] data do próximo follow-up

### Documentação / Fechamento
- [ ] pendência documental principal
- [ ] próxima ação

### Perdido
- [ ] motivo de perda

### Pausado / Sem timing
- [ ] motivo de pausa
- [ ] data de retomada

---

## Bloco 7 — Teste com deals reais

### Separar 5 a 10 deals reais
- [ ] 1 ou 2 leads recém-entrados
- [ ] 1 ou 2 em contato iniciado
- [ ] 1 ou 2 com simulação
- [ ] 1 ou 2 em negociação
- [ ] 1 pausado ou perdido, se houver

### Validar na prática
- [ ] preencher campos sem travar
- [ ] visualizar próxima ação com clareza
- [ ] visualizar follow-up vencido
- [ ] visualizar o que trava o fechamento
- [ ] visualizar pausados com data de retomada

---

## Bloco 8 — Leitura gerencial mínima

### Confirmar se o HubSpot já permite enxergar
- [ ] quantidade por etapa
- [ ] deals sem próxima ação
- [ ] deals com follow-up vencido
- [ ] perdas por motivo
- [ ] ganhos por origem
- [ ] pausados sem data de retomada

### Se não enxergar bem
- [ ] ajustar campos
- [ ] ajustar visualizações
- [ ] ajustar disciplina de preenchimento

---

## Bloco 9 — Critério de pronto

Só considerar implantado quando:
- [ ] pipeline estiver com as 9 etapas finais
- [ ] campos prioritários estiverem criados
- [ ] opções fechadas estiverem padronizadas
- [ ] 5 a 10 deals reais tiverem sido testadas
- [ ] próxima ação e follow-up estiverem visíveis
- [ ] pausado não estiver virando cemitério

---

## Próximo passo depois disso
- [ ] revisar o que funcionou
- [ ] ajustar campos que ficaram burocráticos
- [ ] só então discutir automação via API
