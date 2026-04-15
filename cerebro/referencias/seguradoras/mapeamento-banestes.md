# Mapeamento, BANESTES

Data: 2026-04-14

## Seguradora
- nome: BANESTES
- tipo de receita: comissão sobre vendas
- prioridade: média

## Origem do valor
- canal de acesso: portal
- URL base informada: `https://portalinternet.banestes.com.br/banseg/sala_corretor/restrito/comissao/menu_comissoes.jsf`
- tela/relatório principal validada: `Comissões - EXTRATO DE PAGAMENTOS`
- formato final encontrado: tela/relatório

## Como localizar o valor
- filtro por período: preencher a data inicial e a data final do mês anterior
- exemplo operacional informado: `01/03/2026` até `31/03/2026`
- competência: usar sempre o mês anterior como referência
- janela operacional: as notas fiscais podem ser geradas até o 5º dia do mês subsequente
- leitura operacional atual: abrir o extrato de pagamentos, filtrar o período completo do mês anterior e localizar o valor consolidado a ser usado na NF
- campo validado no extrato: `Valor Base`
- regra validada para `valor_nota`: usar o total final de `Valor Base`, não `Valor Pago`
- exemplo validado por print: período `01/03/2026` a `31/03/2026`, `Valor Base total = R$ 12.056,91`

## Identificação
- match principal recomendado: nome + CNPJ
- nome fiscal esperado: `BANESTES`
- CNPJ fiscal esperado: a confirmar na base já cadastrada

## Acesso
- precisa login: sim
- precisa senha individual: a confirmar
- tem 2FA/captcha: não
- observação de segurança: usar credencial guardada no servidor quando for necessário automatizar ou conferir o relatório

## Automação
- classificação inicial do fluxo: B
- complexidade: média
- risco principal: confirmar se o layout/colunas do extrato se mantêm estáveis ao longo dos meses
- recomendação inicial: semi-automático com boa chance de padronização rápida

## Lacunas que faltam validar
- se existe exportação PDF, XLSX ou CSV
- se o nome/CNPJ do tomador exibido no portal bate 1:1 com a base fiscal
- se o layout do extrato muda quando houver outras naturezas de pagamento
