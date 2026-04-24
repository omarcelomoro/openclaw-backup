# HubSpot — mapa operacional

**Papel:** CRM principal para dar visibilidade comercial do consórcio.
**Status atual:** conectado via API; decisão atual é dedicar o HubSpot ao consórcio por enquanto.

## Para que serve
- pipeline
- próximos passos
- follow-up
- perdas e pausas
- leitura de funil

## Estado atual conhecido
- existe acesso funcionando
- há pipeline ativo mais voltado para seguros/renovações
- 14 deals de seguros já foram criados e documentados em `memory/projects/hubspot-seguros.md`
- a Leevre já tem direção aprovada para separar consórcio e seguro
- existe material de implementação e auditoria em `rotinas/`

## Materiais relacionados
- `memory/projects/hubspot-seguros.md`
- `rotinas/checklist-implementacao-pipeline-consorcio-hubspot-leevre.md`
- `rotinas/plano-execucao-hubspot-api-consorcio-leevre.md`
- `rotinas/mapa-tecnico-campos-pipeline-consorcio-hubspot-leevre.md`
- `rotinas/matriz-auditoria-hubspot-real-vs-ideal-leevre.md`

## O que já está claro
- HubSpot fica dedicado a consórcio por enquanto
- não misturar consórcio e seguro no mesmo raciocínio operacional
- não automatizar bagunça
- validar estrutura com negócios reais antes de API pesada
- toda deal ativa precisa de próxima ação e data de follow-up

## O que falta
- auditar estrutura real vs ideal
- confirmar se já existe pipeline de consórcio utilizável
- criar ou corrigir etapas ideais de consórcio
- definir propriedades mínimas obrigatórias por etapa
- transformar uso em rotina, não só configuração

## Campos e sinais que importam
- origem do lead
- canal detalhado
- tipo de consórcio/seguro
- próxima ação
- data do próximo follow-up
- data da última interação
- motivo de perda
- motivo de pausa
- responsável
- temperatura

## Leitura gerencial mínima desejada
- quantidade por etapa
- negócios sem próxima ação
- follow-ups vencidos
- perdas por motivo
- ganhos por origem

## Riscos
- usar como repositório passivo e não como sistema de gestão
- misturar consórcio e seguro no mesmo raciocínio operacional
- automatizar cedo demais sem higiene de dados
- subir etapa sem evidência real de avanço

## Próximo passo sugerido
Ajustar o HubSpot para o pipeline de consórcio e parar de tratá-lo como ambiente misto.
