# Roteiro de Coleta — HubSpot API para Auditoria da Leevre

## Objetivo
Guia prático para puxar dados do HubSpot via API e preencher a matriz de auditoria real vs ideal.

Este roteiro pressupõe que você já tem acesso à API do HubSpot e um token válido.

---

## Requisitos mínimos
- Token de API válido do HubSpot
- Acesso administrativo ou de leitura ao portal
- Ferramenta para fazer requisições HTTP (curl, Postman, scripts Python/Node, etc.)

## Onde conseguir o token
1. ir para HubSpot Settings → Integrations → Private apps
2. criar ou selecionar uma app existente
3. copiar o token
4. usar como header `Authorization: Bearer seu_token`

---

## Passo 1 — Listar pipelines existentes

### Requisição
```
GET /crm/v3/objects/deals/pipelines
Headers: Authorization: Bearer seu_token
```

### O que procurar
- nome do pipeline de consórcio (se existir)
- nome do pipeline de seguros
- IDs dos pipelines
- quantos pipelines existem no total

### Como interpretar
- se houver 1 pipeline apenas, provavelmente consórcio e seguros estão misturados
- se houver pipelines sem nome claro, pode haver confusão operacional
- anote os IDs para os próximos passos

### Preencher na matriz
Seção **1. Estrutura de pipeline**
- [ ] Existe pipeline separado para consórcio
- [ ] Pipeline de seguros segue separado

---

## Passo 2 — Listar etapas de cada pipeline

### Requisição
```
GET /crm/v3/objects/deals/pipelines/{pipeline_id}
Headers: Authorization: Bearer seu_token
```

(Repetir para cada pipeline_id que encontrou no Passo 1)

### O que procurar
- nomes das etapas
- quantas etapas cada pipeline tem
- ordem das etapas
- se o pipeline de consórcio tem as 9 etapas recomendadas

### Como interpretar
- menos de 5 etapas = pipeline muito simples, provavelmente não reflete realidade operacional
- mais de 12 etapas = pipeline complexo demais, pode destruir preenchimento
- ausência de "Perdido" ou "Pausado" = falta visibilidade de ciclo de vida

### Preencher na matriz
Seção **1. Estrutura de pipeline** → **Auditoria por etapa**
- para cada etapa ideal, marcar se existe e com que nome

---

## Passo 3 — Listar todas as propriedades do objeto Deal

### Requisição
```
GET /crm/v3/objects/deals/properties
Headers: Authorization: Bearer seu_token
```

### O que procurar
- nome visível de cada propriedade
- nome interno (internalName)
- tipo (string, enumeration, number, date, datetime, etc.)
- se é obrigatório ou não
- quais opções fechadas existem (para enumerations)

### Como interpretar
- propriedades com nomes genéricos tipo "custom_field_1" = falta padronização
- muitas propriedades = pode haver duplicação
- propriedades sem tipo claro = configuração fraca

### Dicas práticas
- salvar a saída em JSON para análise posterior
- procurar por propriedades com prefixo consistente (ex.: "consorcio_", "leevre_", etc.)
- procurar por propriedades óbvias como "origem", "canal", "próxima_ação", "follow_up"

### Preencher na matriz
Seção **2. Campos mínimos do pipeline**
- para cada campo ideal, marcar se existe, qual é o nome atual, e se serve como está

---

## Passo 4 — Detalhar opções fechadas (enumerations)

Para cada propriedade de tipo enumeration que encontrou:

### Requisição
```
GET /crm/v3/objects/deals/properties/{property_name}
Headers: Authorization: Bearer seu_token
```

### O que procurar
- quais são as opções disponíveis
- se estão padronizadas
- se cobrem o que a Leevre precisa

### Exemplos de propriedades a detalhar
- temperatura / priority / status
- motivo_perda / reason_lost / motivo_de_perda
- motivo_pausa / motivo_pausado
- tipo_consorcio / tipo_acordo / tipo

### Preencher na matriz
Seção **3. Opções fechadas**
- para cada opção ideal de temperatura, perda, pausa, marcar se existe e com qual nome

---

## Passo 5 — Verificar visibilidade de campos críticos

Para os 10 campos críticos da Leevre:

### Lista dos 10 críticos
1. origem do lead
2. canal detalhado
3. responsável
4. próxima ação
5. data do próximo follow-up
6. temperatura
7. objetivo do cliente
8. valor da carta
9. motivo de perda
10. motivo de pausa

### O que fazer
- procurar cada um na lista de propriedades do Passo 3
- anotar o nome interno exato
- confirmar tipo
- confirmar se é obrigatório no pipeline

### Preencher na matriz
Seção **2. Campos mínimos** → marcar todos os 10 críticos com "sim" ou "não"

---

## Passo 6 — Puxar 5 deals para validação

### Requisição
```
GET /crm/v3/objects/deals?limit=5&properties=["seu_campo_1","seu_campo_2",...]
Headers: Authorization: Bearer seu_token
```

### O que procurar
- os deals existentes têm próxima ação preenchida?
- os deals têm data de follow-up?
- os deals têm responsável?
- qual é a distribuição por etapa?
- existem deals sem valores importantes preenchidos?

### Como interpretar
- se muitos deals não têm próxima ação = falta disciplina operacional
- se muitos deals não têm data de follow-up = follow-up fica invisível
- se existe deal em estágio final sem valor ou motivo = preenchimento fraco

### Preencher na matriz
Seção **6. Diagnóstico final**
- usar a amostra para validar se o pipeline realmente funciona na prática

---

## Passo 7 — Resumir achados

### Criar um documento com
- quantos deals estão no pipeline
- distribuição por etapa
- quantos estão sem próxima ação
- quantos estão sem responsável
- quantos estão sem data de follow-up
- exemplos de deals bem preenchidos
- exemplos de deals com gaps

### Preencher na matriz
Seção **6. Diagnóstico final** → **Resumo executivo**

---

## Passo 8 — Decidir padrão de coleta recorrente

Se quiser monitorar isso regularmente, sugerir:

### Opção 1 — Script manual mensal
- rodar este roteiro uma vez por mês
- preencher a matriz
- analisar tendências

### Opção 2 — Automação leve
- criar um script que rode os passos 3, 4, 5, 6
- exportar para CSV ou JSON
- revisar regularmente

### Opção 3 — Alertas operacionais
- criar alertas para:
  - deals sem próxima ação
  - deals com follow-up vencido
  - deals em etapa crítica (Fechamento) há mais de 7 dias

---

## Exemplo de requisição com curl

```bash
# Listar pipelines
curl -H "Authorization: Bearer seu_token" \
  https://api.hubapi.com/crm/v3/objects/deals/pipelines

# Listar propriedades de deals
curl -H "Authorization: Bearer seu_token" \
  https://api.hubapi.com/crm/v3/objects/deals/properties

# Detalhar uma propriedade específica
curl -H "Authorization: Bearer seu_token" \
  https://api.hubapi.com/crm/v3/objects/deals/properties/seu_campo

# Puxar deals com filtro
curl -H "Authorization: Bearer seu_token" \
  "https://api.hubapi.com/crm/v3/objects/deals?limit=10&properties=\[\"dealstage\",\"dealname\",\"amount\"\]"
```

---

## Próximas ações após coleta

1. **preencher a matriz de auditoria** com os achados
2. **identificar gaps altos** que bloqueiam execução
3. **criar plano de remediação** baseado em gaps
4. **só depois** preparar payloads de criação/atualização via API

---

## Documentação oficial de referência
- HubSpot Deals API: https://developers.hubspot.com/docs/api/crm/deals
- Propriedades customizadas: https://developers.hubspot.com/docs/api/crm/properties

---

## Segurança
- nunca compartilhar token em chat ou repositório
- usar `.env` ou variáveis de ambiente para armazenar o token
- revogar token se suspeitar de exposição
