# n8n — mapa operacional

**Papel:** automações entre canais, CRM e avisos.
**Status atual:** online na VPS; ainda subutilizado frente ao potencial.

## Para que serve
- integrar sistemas
- disparar alertas
- mover dados entre formulários, WhatsApp, CRM e planilhas
- agendar rotinas determinísticas

## Estado atual conhecido
- instância online na VPS
- ferramenta já pensada para marketing e operação
- lista inicial de automações candidata já existe em `memory/projects/funil-digital.md`

## Candidatas prioritárias já mapeadas
1. alerta de renovação — 30/15/7 dias antes
2. notificação de novos leads para canal de marketing
3. lead novo via WhatsApp para HubSpot
4. relatório semanal consolidado

## O que falta
- escolher 1 ou 2 workflows com ganho claro
- documentar gatilho, entrada, saída e dono de cada automação
- definir onde o workflow escreve ou notifica
- evitar automação sem processo claro antes

## Critério de uso bom
- workflow simples
- entrada clara
- saída útil
- falha observável
- alguém responsável por revisar

## Riscos
- virar cola improvisada para processos mal definidos
- automatizar sem logging e sem dono
- criar muitos fluxos pequenos sem manutenção

## Próximo passo sugerido
Escolher os 2 workflows iniciais com maior retorno operacional: renovação e lead novo.
