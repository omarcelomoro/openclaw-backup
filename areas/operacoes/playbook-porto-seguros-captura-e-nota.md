# Playbook, Porto Seguros, captura de valor e emissão da nota

Data base: 2026-04-14

## Objetivo
Padronizar como levantar o valor mensal da Porto e transformar isso em preenchimento correto da planilha `lancamentos_mensais`, seguido da emissão da NFSe da Leevre.

## Status do fluxo
- captura do valor: mapeada
- emissão da nota: validada
- automação futura: viável

## Fonte do valor
- portal: Corretor Online Porto
- tela operacional: `COMISSÕES - NOTA FISCAL ELETRÔNICA`
- saída: relatório HTML

## Regras já validadas
- usar sempre o mês anterior como referência
- a nota deve ser gerada até o 5º dia do mês subsequente
- usar o campo `VALOR BRUTO` como `valor_nota`
- não usar `VALOR LÍQUIDO` como valor da nota
- as retenções aparecem separadas no relatório e servem como conferência, não como base do `valor_nota`
- no caso validado, a filial exibida foi `41.606.205/0001-00`
- susep/favorecida usada: `31340J`

## Passo a passo operacional

### 1. Entrar no portal
- acessar o portal base da Porto
- autenticar com login e senha válidos
- não depender de link profundo com sessão antiga

### 2. Abrir a tela certa
- navegar até `COMISSÕES - NOTA FISCAL ELETRÔNICA`

### 3. Preencher os filtros
- `Mês`: mês anterior ao da emissão
- `Filial`: selecionar a filial correta
- validar se a susep/favorecida exibida é `31340J`

### 4. Gerar o relatório
- clicar em `Gerar relatório`
- confirmar que a tela de retorno mostra:
  - mês de referência
  - filial/CNPJ
  - susep
  - empresa
  - valor bruto
  - retenções
  - valor líquido

### 5. Capturar o valor correto
- localizar `VALOR BRUTO`
- usar esse número no campo `valor_nota` da planilha
- ignorar `VALOR LÍQUIDO` para preenchimento da nota

### 6. Atualizar a planilha mensal
Na aba `lancamentos_mensais`, preencher a linha da Porto com:
- `valor_nota` = valor bruto do relatório
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
- tomador fiscal correto: `PORTO SEGURO COMPANHIA DE SEGUROS GERAIS`
- CNPJ fiscal correto: `61.198.164/0015-65`
- descrição do serviço correta para a competência do mês
- valor da nota igual ao `VALOR BRUTO` do relatório

## Riscos conhecidos
- link profundo do portal pode expirar
- a filial pode variar conforme operação futura
- o layout da Porto pode mudar
- o login não deve ser enviado por chat

## Regra de acesso
- se o acesso à Porto for necessário para automação ou conferência, usar login e senha apenas por meio seguro no servidor
- não tratar o link enviado em conversa como URL fixa de automação
- se a senha mudar, basta atualizar a credencial segura no servidor

## Próximo bloco recomendado
- repetir o mesmo padrão para `BRADESCO CONSORCIO`
