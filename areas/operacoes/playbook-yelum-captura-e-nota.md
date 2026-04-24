# Playbook, Yelum, captura de valor e emissão da nota

Data base: 2026-04-18

## Objetivo
Fechar o mapeamento operacional e fiscal da Yelum para transformar o fluxo em rotina reaproveitável de emissão de NFSe.

## Status do fluxo
- captura do valor: mapeada
- emissão da nota: parcialmente bloqueada
- automação futura: viável, dependendo do fechamento fiscal e do armazenamento seguro da credencial

## O que já existe
- PDF de referência salvo em `state/nf-teste/lote/NF YELLUM.pdf`
- print operacional do portal com totalizador de março/2026
- valor operacional identificado para o exemplo validado: `Total bruto = R$ 4.121,07`

## Fonte do valor
- portal: Novo Meu Espaço Corretor, Yelum Seguradora
- URL base: `https://novomeuespacocorretor.yelumseguros.com.br/lp/commissions`
- tela operacional: `Financeiro > Comissões > Demonstrativo mensal detalhado`
- formato final encontrado: tela com totalizador e grade de detalhes

## Regras já consolidadas
- usar sempre o mês anterior como referência
- preencher mês anterior no ano corrente
- as notas fiscais podem ser geradas até o 5º dia do mês subsequente
- usar `Total bruto` como base de `valor_nota`
- não usar `Valor líquido` como base da nota
- no exemplo validado por print para `03/2026`, os campos visíveis foram:
  - `Total bruto = R$ 4.121,07`
  - `Desconto = R$ 2.412,99`
  - `Total líquido = R$ 1.708,08`
  - `IR = R$ 0,00`
  - `ISS = R$ 0,00`
  - `INSS = R$ 0,00`
  - `Valor líquido = R$ 1.708,24`

## Passo a passo operacional
1. acessar o portal da Yelum
2. autenticar com login e senha válidos
3. navegar até `Financeiro > Comissões > Demonstrativo mensal detalhado`
4. selecionar o mês anterior e o ano corrente
5. clicar em `Buscar`
6. localizar o campo `Total bruto`
7. usar esse valor no campo `valor_nota` da planilha mensal
8. seguir para emissão apenas depois de confirmar dados fiscais da NF de referência

## Acesso
- precisa login: sim
- tem 2FA/captcha: não
- observação de segurança: credenciais não devem ser enviadas por chat; salvar no servidor de forma controlada

## Dados fiscais confirmados pela NF de referência do Drive
- tomador fiscal: `YELUM SEGUROS S.A`
- CNPJ fiscal: `61.550.141/0001-72`
- descrição da nota de referência: `SERVIÇOS DE CORRETAGEM COMPET.12/2025`
- código de tributação nacional: `10.01.02 - Agenciamento, corretagem ou intermediação de seguros.`
- local da prestação: `Vitória - ES`
- valor do serviço na NF de referência: `R$ 4.659,99`
- retenção do ISSQN: `Não Retido`
- ISSQN apurado: `-`
- retenções federais: `-`
- valor líquido da NF de referência: `R$ 4.659,99`

## O que ainda falta confirmar
- modo final de emissão: manual assistido ou API
- IDs internos da Virei, caso a operação migre para script/API

## Regra operacional atual
A captura do valor já pode seguir o playbook. A emissão da Yelum já tem base fiscal mínima confirmada pela NF de referência do Drive e pode seguir em modo assistido, desde que competência, descrição e valor sejam revisados antes do envio final.
