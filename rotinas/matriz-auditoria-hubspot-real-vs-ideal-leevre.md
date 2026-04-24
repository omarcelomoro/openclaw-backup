# Matriz de Auditoria — HubSpot Real vs Estrutura Ideal da Leevre

## Objetivo
Comparar o HubSpot atual da Leevre com a estrutura ideal desenhada para o pipeline de consórcio.

Esta matriz existe para evitar três erros:
- criar coisa que já existe
- duplicar campo bom com nome diferente
- automatizar um CRM que ainda não está operacionalmente confiável

---

## Como usar
Para cada item abaixo, preencher:
- **Status atual**
- **Gap**
- **Ação recomendada**
- **Prioridade**

Sugestão de status:
- Existe e serve
- Existe, mas precisa ajuste
- Não existe
- Existe, mas está duplicado
- Existe, mas não serve

Sugestão de prioridade:
- Alta
- Média
- Baixa

---

# 1. Estrutura de pipeline

| Item ideal | Status atual | Gap | Ação recomendada | Prioridade |
|---|---|---|---|---|
| Existe pipeline separado para consórcio |  |  |  | Alta |
| Pipeline de seguros segue separado |  |  |  | Alta |
| Ordem das etapas reflete operação real |  |  |  | Alta |
| Não há etapas redundantes |  |  |  | Média |
| Etapas de perda e pausa estão separadas |  |  |  | Alta |

## Etapas ideais para comparação
- Lead Entrou
- Contato Iniciado
- Lead Qualificado
- Simulação Enviada
- Em Negociação
- Documentação / Fechamento
- Ganho
- Perdido
- Pausado / Sem timing

### Auditoria por etapa

| Etapa ideal | Existe hoje? | Nome atual | Ajuste necessário | Prioridade |
|---|---|---|---|---|
| Lead Entrou |  |  |  | Alta |
| Contato Iniciado |  |  |  | Alta |
| Lead Qualificado |  |  |  | Alta |
| Simulação Enviada |  |  |  | Alta |
| Em Negociação |  |  |  | Alta |
| Documentação / Fechamento |  |  |  | Alta |
| Ganho |  |  |  | Alta |
| Perdido |  |  |  | Alta |
| Pausado / Sem timing |  |  |  | Alta |

---

# 2. Campos mínimos do pipeline

## Campos críticos

| Campo ideal | Nome interno sugerido | Existe hoje? | Campo equivalente atual | Serve como está? | Ação recomendada | Prioridade |
|---|---|---|---|---|---|---|
| Origem do lead | consorcio_origem_lead |  |  |  |  | Alta |
| Canal detalhado | consorcio_canal_detalhado |  |  |  |  | Alta |
| Responsável | hubspot_owner_id ou consorcio_responsavel |  |  |  |  | Alta |
| Data de entrada | consorcio_data_entrada |  |  |  |  | Média |
| Data da última interação | consorcio_data_ultima_interacao |  |  |  |  | Alta |
| Próxima ação | consorcio_proxima_acao |  |  |  |  | Alta |
| Data do próximo follow-up | consorcio_proximo_followup |  |  |  |  | Alta |
| Tipo de consórcio | consorcio_tipo |  |  |  |  | Alta |
| Objetivo do cliente | consorcio_objetivo_cliente |  |  |  |  | Alta |
| Perfil do cliente | consorcio_perfil_cliente |  |  |  |  | Média |
| Temperatura | consorcio_temperatura |  |  |  |  | Alta |
| Valor pretendido da carta | consorcio_valor_carta |  |  |  |  | Alta |
| Valor ou faixa de parcela desejada | consorcio_valor_parcela |  |  |  |  | Alta |
| Administradora | consorcio_administradora |  |  |  |  | Média |
| Campo objeções | consorcio_objecoes |  |  |  |  | Alta |
| Mapa de decisão (Roadmap to close) | consorcio_roadmap_to_close |  |  |  |  | Alta |
| Objeção principal | consorcio_objecao_principal |  |  |  |  | Alta |
| Status da negociação | consorcio_status_negociacao |  |  |  |  | Média |
| Pendência documental principal | consorcio_pendencia_documental |  |  |  |  | Média |
| Prazo da pendência | consorcio_prazo_pendencia |  |  |  |  | Média |
| Valor final | consorcio_valor_final |  |  |  |  | Média |
| Produto final | consorcio_produto_final |  |  |  |  | Média |
| Data de fechamento | consorcio_data_fechamento |  |  |  |  | Média |
| Motivo de perda | consorcio_motivo_perda |  |  |  |  | Alta |
| Concorrente | consorcio_concorrente |  |  |  |  | Baixa |
| Motivo de pausa | consorcio_motivo_pausa |  |  |  |  | Alta |
| Data de retomada | consorcio_data_retomada |  |  |  |  | Alta |
| Observações comerciais estruturadas | consorcio_observacoes_comerciais |  |  |  |  | Média |

---

# 3. Opções fechadas

## Temperatura

| Valor ideal | Existe hoje? | Nome atual | Ajuste necessário | Prioridade |
|---|---|---|---|---|
| Quente |  |  |  | Alta |
| Morno |  |  |  | Alta |
| Frio |  |  |  | Alta |
| Pausado |  |  |  | Alta |

## Motivo de perda

| Valor ideal | Existe hoje? | Nome atual | Ajuste necessário | Prioridade |
|---|---|---|---|---|
| Sem timing |  |  |  | Alta |
| Preço ou parcela não encaixou |  |  |  | Alta |
| Decidiu por outra solução |  |  |  | Alta |
| Fechou com concorrente |  |  |  | Média |
| Perfil não aderente |  |  |  | Média |
| Sem resposta após tentativas |  |  |  | Alta |
| Desistiu do objetivo |  |  |  | Média |

## Motivo de pausa

| Valor ideal | Existe hoje? | Nome atual | Ajuste necessário | Prioridade |
|---|---|---|---|---|
| Aguardando organização financeira |  |  |  | Alta |
| Aguardando decisão familiar ou societária |  |  |  | Média |
| Aguardando documento |  |  |  | Média |
| Aguardando momento de compra |  |  |  | Alta |
| Voltou para análise futura |  |  |  | Média |

---

# 4. Regras operacionais no CRM

| Regra ideal | Existe hoje? | Gap | Ação recomendada | Prioridade |
|---|---|---|---|---|
| Todo negócio tem responsável |  |  |  | Alta |
| Todo negócio ativo tem próxima ação |  |  |  | Alta |
| Todo negócio ativo tem data de follow-up |  |  |  | Alta |
| Todo negócio perdido tem motivo de perda |  |  |  | Alta |
| Todo negócio pausado tem motivo e data de retomada |  |  |  | Alta |
| Nenhuma etapa sobe sem evidência real de avanço |  |  |  | Alta |

---

# 5. Leitura gerencial mínima

| Leitura ideal | Existe hoje? | Qualidade atual | Gap | Ação recomendada | Prioridade |
|---|---|---|---|---|---|
| Quantidade por etapa |  |  |  |  | Alta |
| Negócios sem próxima ação |  |  |  |  | Alta |
| Follow-ups vencidos |  |  |  |  | Alta |
| Tempo por etapa |  |  |  |  | Média |
| Taxa de avanço entre etapas |  |  |  |  | Média |
| Perdas por motivo |  |  |  |  | Alta |
| Ganhos por origem |  |  |  |  | Média |

---

# 6. Diagnóstico final

## Resumo executivo
- Quantos gaps altos existem?
- O que já pode ser reaproveitado?
- O que precisa ser criado do zero?
- O que está duplicado e precisa consolidar?

## Decisão sugerida
Marcar uma das opções:
- [ ] Pronto para ajuste leve
- [ ] Precisa reestruturação parcial
- [ ] Precisa reorganização forte antes de automatizar

---

# 7. Ordem de ataque recomendada
1. corrigir pipeline e etapas
2. corrigir campos críticos
3. padronizar motivos e temperatura
4. garantir próxima ação e follow-up
5. validar leitura gerencial
6. só depois preparar automação
