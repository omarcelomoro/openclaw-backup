# Mapa Técnico de Campos — Pipeline de Consórcio no HubSpot

## Objetivo
Definir a base técnica mínima dos campos do pipeline de consórcio da Leevre para implementação e uso via HubSpot API.

Este arquivo não depende ainda dos nomes internos reais do portal. Onde o nome interno ainda não existe, a proposta abaixo serve como padrão recomendado de criação.

---

## Regras de nomenclatura

### Nome visível
- deve ser claro para uso operacional
- deve falar a linguagem da equipe

### Nome interno
- usar snake_case
- sem acento
- sem espaço
- preferir prefixo quando ajudar organização

Sugestão de prefixo para propriedades próprias do pipeline de consórcio:
- `consorcio_`

Exemplo:
- Nome visível: `Valor pretendido da carta`
- Nome interno: `consorcio_valor_carta`

---

## Mapa técnico recomendado

| Nome visível | Nome interno sugerido | Tipo | Obrigatório | Exigido a partir da etapa | Observação |
|---|---|---|---|---|---|
| Origem do lead | consorcio_origem_lead | enumeration | sim | Lead Entrou | Ex.: orgânico, tráfego pago, indicação, parceria |
| Canal detalhado | consorcio_canal_detalhado | string | sim | Lead Entrou | Ex.: Instagram, WhatsApp, landing page |
| Responsável | hubspot_owner_id ou consorcio_responsavel | owner/enumeration | sim | Lead Entrou | Preferir owner nativo se possível |
| Data de entrada | consorcio_data_entrada | date | sim | Lead Entrou | Se já houver campo nativo confiável, reutilizar |
| Data da última interação | consorcio_data_ultima_interacao | datetime | sim | Contato Iniciado | Pode ser atualizada manualmente no início |
| Próxima ação | consorcio_proxima_acao | string | sim | Contato Iniciado | Campo crítico de gestão |
| Data do próximo follow-up | consorcio_proximo_followup | date | sim | Contato Iniciado | Base para leitura de vencidos |
| Tipo de consórcio | consorcio_tipo | enumeration | sim | Lead Qualificado | Ex.: imóvel, automóvel, serviço |
| Objetivo do cliente | consorcio_objetivo_cliente | string | sim | Lead Qualificado | Ex.: moradia, investimento, troca de patrimônio |
| Perfil do cliente | consorcio_perfil_cliente | enumeration | sim | Lead Qualificado | PF ou PJ |
| Temperatura | consorcio_temperatura | enumeration | sim | Lead Qualificado | Quente, Morno, Frio, Pausado |
| Valor pretendido da carta | consorcio_valor_carta | number | sim | Simulação Enviada | Preferir número sem máscara de moeda na API |
| Valor ou faixa de parcela desejada | consorcio_valor_parcela | string | sim | Simulação Enviada | Pode começar em texto se a operação variar muito |
| Administradora | consorcio_administradora | enumeration | não | Simulação Enviada | Ex.: Itaú, Bradesco, Porto, Servopa |
| Campo objeções | consorcio_objecoes | multiline_text | sim | Em Negociação | Registrar as objeções reais e específicas do lead |
| Mapa de decisão (Roadmap to close) | consorcio_roadmap_to_close | multiline_text | sim | Em Negociação | Caminho restante até o fechamento, com trava e próximo marco |
| Objeção principal | consorcio_objecao_principal | enumeration | sim | Em Negociação | Melhor em opções fechadas |
| Status da negociação | consorcio_status_negociacao | enumeration | não | Em Negociação | Ex.: aguardando retorno, revisando proposta |
| Pendência documental principal | consorcio_pendencia_documental | string | sim | Documentação / Fechamento | Descrever o principal gargalo documental |
| Prazo da pendência | consorcio_prazo_pendencia | date | não | Documentação / Fechamento | Ajuda a cobrar fechamento |
| Valor final | consorcio_valor_final | number | sim | Ganho | Valor final consolidado do negócio |
| Produto final | consorcio_produto_final | string | sim | Ganho | Fechamento resumido do que foi contratado |
| Data de fechamento | consorcio_data_fechamento | date | sim | Ganho | Pode haver campo nativo, validar antes |
| Motivo de perda | consorcio_motivo_perda | enumeration | sim | Perdido | Deve ser padronizado |
| Concorrente | consorcio_concorrente | string | não | Perdido | Preencher quando houver clareza |
| Motivo de pausa | consorcio_motivo_pausa | enumeration | sim | Pausado / Sem timing | Deve ser padronizado |
| Data de retomada | consorcio_data_retomada | date | sim | Pausado / Sem timing | Campo essencial para não virar cemitério |
| Observações comerciais estruturadas | consorcio_observacoes_comerciais | multiline_text | não | Lead Qualificado | Usar para contexto útil, não para compensar falta de campo |

---

## Opções fechadas recomendadas

### consorcio_temperatura
- Quente
- Morno
- Frio
- Pausado

### consorcio_perfil_cliente
- PF
- PJ

### consorcio_tipo
- Imóvel
- Automóvel
- Serviço
- Outro

### consorcio_motivo_perda
- Sem timing
- Preço ou parcela não encaixou
- Decidiu por outra solução
- Fechou com concorrente
- Perfil não aderente
- Sem resposta após tentativas
- Desistiu do objetivo

### consorcio_motivo_pausa
- Aguardando organização financeira
- Aguardando decisão familiar ou societária
- Aguardando documento
- Aguardando momento de compra
- Voltou para análise futura

### consorcio_objecao_principal
- Agora não é o momento
- Preciso pensar melhor
- Ficou caro
- Vou comparar com outra opção
- Não entendi direito como funciona
- Tenho medo de errar
- Vou decidir com cônjuge ou sócio
- Perdi prioridade nisso agora

### consorcio_status_negociacao
- Aguardando retorno
- Revisando proposta
- Ajustando cenário
- Validando documentação
- Em decisão final

---

## Como aplicar os dois campos novos

### Campo objeções (`consorcio_objecoes`)
Esse campo existe para registrar a objeção real do lead em linguagem humana, sem perder nuance.

Use para anotar coisas como:
- cliente quer carta maior, mas a parcela confortável não fecha
- casal ainda não está alinhado sobre momento de compra
- cliente compara com financiamento e ainda não entendeu a lógica do consórcio

Regra de uso:
- curto
- objetivo
- focado no que trava avanço

### Mapa de decisão / Roadmap to close (`consorcio_roadmap_to_close`)
Esse campo serve para mostrar **o que ainda precisa acontecer para o negócio fechar**.

Ele ajuda muito quando a venda é consultiva, tem mais de um decisor, envolve timing, comparação de cenário ou documentação.

Estrutura sugerida:
- etapa atual
- quem decide
- o que falta acontecer
- trava principal
- próximo marco

Exemplo:
- casal avaliando carta de 300k vs 400k
- decisão depende de alinhamento entre parcela e plano patrimonial
- trava principal: esposa ainda não está convencida
- próximo marco: revisar cenário final até terça
- se aprovado, avança para documentação

---

## Campos realmente críticos
Se for preciso começar menor, estes são os indispensáveis:
- consorcio_origem_lead
- consorcio_canal_detalhado
- hubspot_owner_id ou consorcio_responsavel
- consorcio_proxima_acao
- consorcio_proximo_followup
- consorcio_temperatura
- consorcio_objetivo_cliente
- consorcio_valor_carta
- consorcio_objecoes
- consorcio_roadmap_to_close
- consorcio_motivo_perda
- consorcio_motivo_pausa

---

## Campos que merecem validação antes de criar
Validar se já existe campo nativo ou equivalente útil no HubSpot para:
- responsável
- data de entrada
- data de fechamento
- owner
- valor do negócio

Se existir equivalente confiável, preferir reutilizar em vez de duplicar.

---

## Ordem de criação recomendada
1. criar campos críticos
2. criar opções fechadas
3. subir campos de negociação e fechamento
4. testar preenchimento com casos reais
5. só depois travar obrigatoriedade mais ampla

---

## Próximo uso deste arquivo
Este mapa serve para:
- criação manual de propriedades no HubSpot
- conferência de nomes internos
- preparação de chamadas via API
- construção futura de payloads de criação e atualização
