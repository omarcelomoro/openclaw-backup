# Mapeamento, BRADESCO SEGUROS

Data: 2026-04-14

## Seguradora
- nome: BRADESCO SEGUROS
- tipo de receita: comissão sobre vendas
- prioridade: média

## Origem do valor
- canal de acesso: portal
- URL base informada: `https://wwwn.bradescoseguros.com.br/pnegocios/wps/myportal/portalnegocios/arealogada/auto/comissoes/paineldecomissao/extrato-de-comissoes-v2/`
- tela/relatório principal validada: `Auto > Comissões > Extrato de Comissões`
- formato final encontrado: tela/relatório com indicadores consolidados

## Como localizar o valor
- filtro por período: preencher a data inicial e a data final do mês anterior
- exemplo operacional informado: `01/03/2026` até `31/03/2026`
- ação principal: `Buscar`
- competência: usar sempre o mês anterior como referência
- janela operacional: as notas fiscais podem ser geradas até o 5º dia do mês subsequente
- empresa validada por print: `Bradesco Auto Re`
- agência/conta: `Todas`
- campo validado para `valor_nota`: `Comissões`
- não usar `Crédito líquido` como base da nota
- exemplo validado por print: período de março/2026 com `Comissões = R$ 2.274,67`, `Tributações = R$ 44,36` e `Crédito líquido = R$ 2.173,90`
- dados auxiliares visíveis no print: `Parceiro 0015563245`, `Susep 212114083`, `CPF/CNPJ 41.606.205/0001-00`

## Identificação
- match principal recomendado: nome + CNPJ
- nome fiscal esperado: `BRADESCO AUTO/RE COMPANHIA DE SEGUROS`
- CNPJ fiscal esperado: `92.682.038/0191-29`

## Acesso
- precisa login: sim
- precisa senha individual: a confirmar
- tem 2FA/captcha: não
- observação de segurança: usar credencial guardada no servidor quando for necessário automatizar ou conferir o relatório

## Automação
- classificação inicial do fluxo: B
- complexidade: média
- risco principal: confirmar se a empresa correta estará sempre selecionada e se o card `Comissões` sempre representa a base fiscal
- recomendação inicial: semi-automático com boa chance de padronização rápida

## Lacunas que faltam validar
- NF de referência do Drive para confirmar descrição fiscal e retenções
- se existem outras empresas/linhas de negócio com comportamento diferente no mesmo portal
- se o botão `Solicitar extrato` gera arquivo útil para auditoria local
