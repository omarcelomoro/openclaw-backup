# Mapeamento, HDI

Data: 2026-04-14

## Seguradora
- nome: HDI
- tipo de receita: comissão sobre vendas
- prioridade: média

## Origem do valor
- canal de acesso: portal
- URL informada: `https://www.hdi.com.br/digital2/home`
- observação de segurança: a URL enviada contém chave de sessão/usuário e não deve ser tratada como link fixo de automação
- tela/relatório principal validada: `Adm > Relatórios > Comissões`
- formato final encontrado: tela/relatório com grade e totalizador

## Como localizar o valor
- filtro por período: preencher a data inicial e a data final do mês anterior
- exemplo operacional informado: `01/03/2026` até `31/03/2026`
- ação principal: `Visualizar`
- competência: usar sempre o mês anterior como referência
- janela operacional: as notas fiscais podem ser geradas até o 5º dia do mês subsequente
- campo validado para `valor_nota`: total de `Vlr. Bruto`
- não usar `Líquida` como base da nota
- exemplo validado por print: período de março/2026 com total `Vlr. Bruto = R$ 5.161,81`

## Identificação
- match principal recomendado: nome + CNPJ
- nome fiscal esperado: `HDI SEGUROS S.A.`
- CNPJ fiscal esperado: a confirmar na NF de referência do Drive

## Acesso
- precisa login: sim
- precisa senha individual: a confirmar
- tem 2FA/captcha: não
- observação de segurança: usar credencial guardada no servidor quando for necessário automatizar ou conferir o relatório

## Automação
- classificação inicial do fluxo: B
- complexidade: média
- risco principal: confirmar se a coluna `Vlr. Bruto` sempre representa exatamente a base fiscal em todos os meses
- recomendação inicial: semi-automático com boa chance de padronização rápida

## Lacunas que faltam validar
- NF de referência do Drive para confirmar tomador, CNPJ e descrição fiscal
- se há múltiplas sucursais que possam alterar o total
- se a exportação em Excel mantém o mesmo total da tela
