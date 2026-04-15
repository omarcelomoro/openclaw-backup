# Playbook, ALLIANZ, captura de valor e emissão da nota

Data base: 2026-04-14

## Objetivo
Padronizar como levantar o valor mensal da ALLIANZ e transformar isso em preenchimento correto da planilha `lancamentos_mensais`, seguido da emissão da NFSe da Leevre.

## Status do fluxo
- captura do valor: mapeada
- emissão da nota: tecnicamente pronta pelo fluxo já validado da Virei Contador
- automação futura: viável

## Fonte do valor
- portal: AllianzNet
- tela operacional: `Gestão > Financeiro > Extrato de Comissões`
- saída atual: tela/relatório

## Regras já consolidadas
- usar sempre o mês anterior como referência
- preencher o período completo do mês anterior
- exemplo informado: `01/03/2026` a `31/03/2026`
- a nota deve ser gerada até o 5º dia do mês subsequente
- usar o bloco `Comissões Pagas`
- usar `Total Bruto` como `valor_nota`
- não usar `Total Líquido` como valor da nota
- usar a NF de referência do Drive como parâmetro para tomador, CNPJ, descrição e padrão fiscal

## Passo a passo operacional

### 1. Entrar no portal
- acessar o portal da Allianz
- autenticar com login e senha válidos

### 2. Abrir a tela certa
- navegar até `Gestão > Financeiro > Extrato de Comissões`

### 3. Preencher os filtros
- informar SUSEP `212114083`
- informar CPF/CNPJ `41606205000100`
- preencher `Data Inicial` com o 1º dia do mês anterior
- preencher `Data Final` com o último dia do mês anterior
- exemplo para março/2026: `01/03/2026` até `31/03/2026`
- se houver seleção de mediador, validar se não há mistura indevida

### 4. Gerar o extrato
- clicar em `Aplicar`
- confirmar que o bloco `Total do período selecionado` foi carregado

### 5. Capturar o valor correto
- localizar `Total Bruto`
- usar esse número no campo `valor_nota` da planilha
- ignorar `Total Líquido` para preenchimento da nota
- exemplo validado: `R$ 8.584,31`

### 6. Atualizar a planilha mensal
Na aba `lancamentos_mensais`, preencher a linha da ALLIANZ com:
- `valor_nota` = total bruto do extrato
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
