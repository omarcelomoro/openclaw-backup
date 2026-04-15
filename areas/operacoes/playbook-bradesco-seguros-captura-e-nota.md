# Playbook, BRADESCO SEGUROS, captura de valor e emissão da nota

Data base: 2026-04-14

## Objetivo
Padronizar como levantar o valor mensal da BRADESCO SEGUROS e transformar isso em preenchimento correto da planilha `lancamentos_mensais`, seguido da emissão da NFSe da Leevre.

## Status do fluxo
- captura do valor: mapeada
- emissão da nota: tecnicamente pronta pelo fluxo já validado da Virei Contador
- automação futura: viável

## Fonte do valor
- portal: Portal de Negócios Bradesco Seguros
- tela operacional: `Auto > Comissões > Extrato de Comissões`
- saída atual: tela/relatório com cards consolidados

## Regras já consolidadas
- usar sempre o mês anterior como referência
- preencher o período completo do mês anterior
- exemplo informado: `01/03/2026` a `31/03/2026`
- clicar em `Buscar`
- a nota deve ser gerada até o 5º dia do mês subsequente
- usar o card `Comissões` como `valor_nota`
- não usar `Crédito líquido` como valor da nota
- usar a NF de referência do Drive como parâmetro para tomador, CNPJ, descrição e padrão fiscal

## Passo a passo operacional

### 1. Entrar no portal
- acessar o portal da Bradesco Seguros
- autenticar com login e senha válidos

### 2. Abrir a tela certa
- navegar até `Auto > Comissões > Extrato de Comissões`

### 3. Preencher os filtros
- empresa: `Bradesco Auto Re`
- agência/conta: `Todas`
- período: preencher do 1º ao último dia do mês anterior
- exemplo para março/2026: `01/03/2026` até `31/03/2026`

### 4. Gerar o relatório
- clicar em `Buscar`
- confirmar que os cards consolidados foram carregados

### 5. Capturar o valor correto
- localizar o card `Comissões`
- usar esse número no campo `valor_nota` da planilha
- ignorar `Crédito líquido` para preenchimento da nota
- exemplo validado: `R$ 2.274,67`

### 6. Atualizar a planilha mensal
Na aba `lancamentos_mensais`, preencher a linha da BRADESCO SEGUROS com:
- `valor_nota` = valor do card `Comissões`
- `status_emissao` = `PENDENTE` até emitir
- `emitir_agora` = `SIM` quando a linha estiver pronta

### 7. Emitir a nota
- usar a NF do Drive como parâmetro fiscal
- usar o fluxo assistido já validado na Virei Contador
- conferir tomador, descrição e valor
- emitir a NFSe
- registrar de volta:
  - `status_emissao`
  - `numero_nota`
  - `link_nota`
