# Auditoria real — HubSpot Leevre (24/04/2026)

## Resumo executivo

Diagnóstico atual: **precisa reestruturação parcial antes de automatizar**.

O HubSpot está conectado e operacional, mas hoje existe apenas **1 pipeline de negócios** com 7 etapas genéricas/adaptadas. Isso é suficiente para uso básico, mas ainda **não atende o desenho ideal da Leevre para consórcio**.

## Evidências levantadas ao vivo via API

### Pipeline atual
- ID: `default`
- Nome: `Pipeline de negócios`

### Etapas atuais
1. Lead Recebido
2. Primeiro Contato
3. Simulação Enviada
4. Proposta Aceita
5. Contrato Assinado
6. Ganho
7. Perdido

## Leitura do estado atual

### O que já está bom
- existe pipeline ativo
- nomes das etapas já foram parcialmente adaptados ao português
- já há stages mínimas de entrada, contato, simulação, ganho e perda
- o HubSpot já tem campos nativos úteis para owner, last activity e next activity

### Gaps principais
1. **Não existe pipeline separado para consórcio**
2. **Seguro e consórcio ainda tendem a compartilhar o mesmo raciocínio operacional**
3. **Faltam etapas-chave do modelo ideal**:
   - Lead Qualificado
   - Em Negociação
   - Documentação / Fechamento
   - Pausado / Sem timing
4. **“Proposta Aceita” e “Contrato Assinado” não cobrem bem o meio do processo comercial consultivo**
5. **Não encontrei via propriedades filtradas os campos customizados mínimos de consórcio já prontos**:
   - origem do lead
   - canal detalhado
   - tipo de consórcio
   - objetivo do cliente
   - temperatura
   - objeção principal
   - motivo de perda padronizado
   - motivo de pausa
6. **Há apoio nativo para atividade**, mas isso não substitui disciplina comercial

## Comparação com estrutura ideal

### Estrutura ideal aprovada
- Lead Entrou
- Contato Iniciado
- Lead Qualificado
- Simulação Enviada
- Em Negociação
- Documentação / Fechamento
- Ganho
- Perdido
- Pausado / Sem timing

### Diferença prática
O pipeline atual parece mais próximo de um fluxo comercial genérico. Para a Leevre, falta refletir:
- qualificação real
- negociação consultiva
- pausas sem perda
- pendência documental antes do fechamento

## Propriedades nativas úteis já disponíveis
- `hubspot_owner_id` — responsável
- `notes_last_updated` — última atividade
- `notes_next_activity_date` — próxima atividade
- `closedate`
- datas de entrada/saída de stages
- tempo na etapa atual

## Propriedades que ainda precisam existir ou ser confirmadas
- origem do lead
- canal detalhado
- tipo de consórcio
- objetivo do cliente
- valor da carta
- valor/faixa de parcela
- perfil PF/PJ
- temperatura
- próxima ação
- data do próximo follow-up
- objeção principal
- motivo de perda
- motivo de pausa
- data de retomada
- observações comerciais estruturadas

## Riscos atuais
- automatizar um pipeline ainda genérico
- usar o CRM como cadastro e não como gestão
- continuar sem leitura clara de follow-up vencido por contexto comercial
- misturar fluxo de seguro e consórcio cedo demais

## Recomendação objetiva

### Decisão sugerida
- [x] **Precisa reestruturação parcial antes de automatizar**
- [ ] Pronto para ajuste leve
- [ ] Precisa reorganização forte antes de automatizar

## Ordem de ataque recomendada
1. confirmar se o pipeline atual ficará para seguros ou se será refeito
2. criar pipeline separado para consórcio
3. subir propriedades mínimas de consórcio
4. criar etapa de pausado / sem timing
5. testar com 5 a 10 negócios reais
6. só depois pensar em automação via API

## Próximo passo mais inteligente
Executar um ajuste estrutural enxuto no HubSpot para consórcio, sem automação pesada ainda.
