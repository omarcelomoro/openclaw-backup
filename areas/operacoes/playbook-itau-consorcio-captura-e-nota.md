# Playbook, Itaú Consórcio, captura de valor e emissão da nota

Data base: 2026-04-19

## Objetivo
Padronizar como localizar o valor operacional do Itaú Consórcio e transformar isso em preenchimento correto da planilha mensal para futura emissão da nota.

## Status do fluxo
- captura do valor: mapeada
- emissão da nota: pronta para uso assistido, com base fiscal já validada
- automação futura: provável, depende de validar navegação real no portal

## Fonte do valor
- portal: DOC Acesso, Gestão Veículos
- URL base: `https://doc.acesso.io/gestaoveiculos/LoginSafeDoc.aspx?ReturnUrl=%2Fgestaoveiculos%2F`
- tela/relatório: `https://doc.acesso.io/gestaoveiculos/UserInboxDomain_Advanced.aspx`
- caminho operacional: `Processo > Caixa por domínio`

## Regras já consolidadas
- o valor fica na linha com status textual de pendência de inclusão
- localizar o campo em `Descrição do Objeto`
- usar o valor que aparece nessa linha como base operacional
- não há filtro explícito de competência no fluxo informado
- precisa login
- não tem 2FA/captcha

## Passo a passo operacional
1. acessar o portal do Itaú Consórcio
2. autenticar com login e senha válidos
3. navegar até `Processo > Caixa por domínio`
4. clicar em `Filtrar` (botão azul)
5. localizar em `Descrição do Objeto` a linha que conste `pendente de inclusão`
6. capturar o valor dessa linha
7. lançar esse valor em `lancamentos_mensais`
8. revisar descrição final antes da emissão

## Campos de conferência
- tomador fiscal: `ITAU ADMINISTRADORA DE CONSORCIOS LTDA`
- CNPJ fiscal: `00.000.776/0001-01`
- descrição-base da NF de referência: `Corretores e agentes de seguros neste periodo:`
- município da prestação: `Vitória - ES`

## Riscos conhecidos
- ausência de filtro de competência pode exigir conferência manual do período
- a descrição-base da NF de referência pede padronização futura
- o portal pode depender de nomenclatura exata da fila/processo

## Regra operacional atual
A captura já pode ser feita por esse fluxo. A emissão deve seguir em modo assistido até validarmos melhor a descrição final e a recorrência operacional do portal.
