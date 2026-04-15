# Mapeamento, ALLIANZ

Data: 2026-04-14

## Seguradora
- nome: ALLIANZ
- tipo de receita: comissão sobre vendas
- prioridade: média

## Origem do valor
- canal de acesso: portal
- URL base informada: `https://www.allianznet.com.br/ngx-epac/private/application`
- tela/relatório principal validada: `Gestão > Financeiro > Extrato de Comissões`
- formato final encontrado: tela/relatório

## Como localizar o valor
- usar o bloco `Comissões Pagas`
- filtro por período: preencher a data inicial e a data final do mês anterior
- exemplo operacional informado: `01/03/2026` até `31/03/2026`
- competência: usar sempre o mês anterior como referência
- janela operacional: as notas fiscais podem ser geradas até o 5º dia do mês subsequente
- filtro adicional validado por print: SUSEP `212114083` e CPF/CNPJ `41606205000100`
- campo validado para `valor_nota`: `Total Bruto`
- exemplo validado por print: período `01/03/2026` a `31/03/2026`, `Total Bruto = R$ 8.584,31`
- não usar `Total Líquido` como base da nota

## Identificação
- match principal recomendado: nome + CNPJ
- nome fiscal esperado: `ALLIANZ SEGUROS S/A`
- CNPJ fiscal esperado: `61.573.796/0029-67`

## Acesso
- precisa login: sim
- precisa senha individual: a confirmar
- tem 2FA/captcha: não
- observação de segurança: usar credencial guardada no servidor quando for necessário automatizar ou conferir o relatório

## Automação
- classificação inicial do fluxo: B
- complexidade: média
- risco principal: confirmar estabilidade do layout e se o bloco `Comissões Pagas` sempre reflete o valor fiscal correto
- recomendação inicial: semi-automático com boa chance de padronização rápida

## Lacunas que faltam validar
- se existe exportação PDF, XLSX ou CSV
- se existe mais de um mediador selecionado alterando o total
- se a NF de referência do Drive confirma o mesmo padrão de descrição fiscal
