# Playbook, HDI, captura de valor e emissão da nota

Data base: 2026-04-14

## Objetivo
Padronizar como levantar o valor mensal da HDI e transformar isso em preenchimento correto da planilha `lancamentos_mensais`, seguido da emissão da NFSe da Leevre.

## Status do fluxo
- captura do valor: mapeada
- emissão da nota: tecnicamente pronta pelo fluxo já validado da Virei Contador
- automação futura: viável

## Fonte do valor
- portal: HDI Digital
- tela operacional: `Adm > Relatórios > Comissões`
- saída atual: tela/relatório com grade, totalizador e exportação Excel

## Regras já consolidadas
- usar sempre o mês anterior como referência
- preencher o período completo do mês anterior
- exemplo informado: `01/03/2026` a `31/03/2026`
- clicar em `Visualizar`
- a nota deve ser gerada até o 5º dia do mês subsequente
- usar o total de `Vlr. Bruto` como `valor_nota`
- não usar `Líquida` como valor da nota
- usar a NF de referência do Drive como parâmetro para tomador, CNPJ, descrição e padrão fiscal

## Passo a passo operacional

### 1. Entrar no portal
- acessar o portal da HDI
- autenticar com login e senha válidos
- não depender da URL completa com chave de usuário enviada em conversa

### 2. Abrir a tela certa
- navegar até `Adm > Relatórios > Comissões`

### 3. Preencher o período
- informar `data inicial` com o 1º dia do mês anterior
- informar `data final` com o último dia do mês anterior
- exemplo para março/2026: `01/03/2026` até `31/03/2026`

### 4. Gerar o relatório
- clicar em `Visualizar`
- confirmar que a grade carregou e que o totalizador final está visível

### 5. Capturar o valor correto
- localizar a coluna `Vlr. Bruto`
- usar o total final de `Vlr. Bruto` no campo `valor_nota` da planilha
- ignorar `Líquida` para preenchimento da nota
- exemplo validado: `R$ 5.161,81`

### 6. Atualizar a planilha mensal
Na aba `lancamentos_mensais`, preencher a linha da HDI com:
- `valor_nota` = total de `Vlr. Bruto`
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
