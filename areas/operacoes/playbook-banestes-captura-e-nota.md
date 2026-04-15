# Playbook, BANESTES, captura de valor e emissão da nota

Data base: 2026-04-14

## Objetivo
Padronizar como levantar o valor mensal da BANESTES e transformar isso em preenchimento correto da planilha `lancamentos_mensais`, seguido da emissão da NFSe da Leevre.

## Status do fluxo
- captura do valor: parcialmente mapeada
- emissão da nota: tecnicamente pronta pelo fluxo já validado da Virei Contador
- automação futura: viável, mas depende de validar o campo correto do extrato

## Fonte do valor
- portal: Banestes, sala do corretor
- tela operacional: `Comissões - EXTRATO DE PAGAMENTOS`
- saída atual: tela/relatório por período

## Regras já consolidadas
- usar sempre o mês anterior como referência
- preencher o período completo do mês anterior
- exemplo informado: `01/03/2026` a `31/03/2026`
- a nota deve ser gerada até o 5º dia do mês subsequente

## Passo a passo operacional

### 1. Entrar no portal
- acessar o portal da BANESTES
- autenticar com login e senha válidos

### 2. Abrir a tela certa
- navegar até `Comissões - EXTRATO DE PAGAMENTOS`

### 3. Preencher o período
- informar `data inicial` com o 1º dia do mês anterior
- informar `data final` com o último dia do mês anterior
- exemplo para março/2026: `01/03/2026` até `31/03/2026`

### 4. Gerar o extrato
- executar a consulta do período
- confirmar que a tela retornou o extrato de pagamentos correspondente

### 5. Capturar o valor correto
- localizar a coluna `Valor Base`
- usar o total final de `Valor Base` no campo `valor_nota` da planilha
- não usar `Valor Pago` como base da nota
- exemplo validado: no período `01/03/2026` a `31/03/2026`, o total de `Valor Base` foi `R$ 12.056,91`

### 6. Atualizar a planilha mensal
Na aba `lancamentos_mensais`, preencher a linha da BANESTES com:
- `valor_nota` = valor correto do extrato
- `status_emissao` = `PENDENTE` até emitir
- `emitir_agora` = `SIM` quando a linha estiver pronta

### 7. Emitir a nota
- usar o fluxo assistido já validado na Virei Contador
- conferir tomador, descrição e valor
- emitir a NFSe
- registrar de volta:
  - `status_emissao`
  - `numero_nota`
  - `link_nota`

## Campos de conferência
Antes de emitir, conferir:
- usar a NF de referência salva no Drive como parâmetro principal
- tomador fiscal correto, espelhando a NF de referência
- CNPJ fiscal correto, espelhando a NF de referência
- descrição do serviço correta para a competência do mês, baseada no padrão já usado na NF do Drive
- valor da nota igual ao total correto do extrato

## Riscos conhecidos
- o extrato pode mostrar mais de um total em cenários diferentes
- o layout do portal pode mudar
- o login não deve ser enviado por chat

## Regra de acesso
- se o acesso à BANESTES for necessário para automação ou conferência, usar login e senha apenas por meio seguro no servidor
- não tratar links de sessão como URL fixa de automação

## Regra operacional validada por print
- para a BANESTES, o campo que alimenta `valor_nota` é o total de `Valor Base`
- no exemplo validado, `Valor Pago` total foi `R$ 11.815,77`, mas o valor correto da nota é `Valor Base total = R$ 12.056,91`
- para tomador, CNPJ, descrição e demais parâmetros fiscais, usar a NF de referência do Drive como base antes de emitir
