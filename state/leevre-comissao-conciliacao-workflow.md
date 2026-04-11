# Rotina Operacional — Comissão e Conciliação Leevre

Data: 2026-04-09

## Objetivo
Reduzir trabalho manual, conferência e retrabalho no fechamento de comissão da Leevre.

## Fluxo-alvo
1. Receber PDFs e relatórios das seguradoras
2. Extrair texto/tabelas dos PDFs
3. Normalizar os dados em planilha mestre
4. Conferir valores recebidos no banco
5. Identificar divergências e pendências
6. Gerar resumo por produtor, seguradora e status

## Estrutura mínima de pastas

```text
state/operacao/comissoes/
  entrada/
    2026-04/
      seguradora-x/
      seguradora-y/
  extraido/
    2026-04/
  consolidado/
    2026-04/
  saida/
    2026-04/
```

## Planilha mestre recomendada

### Aba 1 — lancamentos
Campos:
- data_competencia
- seguradora
- produtor
- cliente
- produto
- proposta_apolice
- premio_ou_credito
- comissao_bruta
- percentual_comissao
- comissao_liquida
- status_pagamento
- data_pagamento
- origem_arquivo
- observacoes

### Aba 2 — conciliacao_bancaria
Campos:
- data_recebimento
- banco
- historico
- valor_recebido
- seguradora_prevista
- produtor_previsto
- status_conciliacao
- observacoes

### Aba 3 — divergencias
Campos:
- tipo_divergencia
- seguradora
- produtor
- referencia
- valor_esperado
- valor_recebido
- diferenca
- acao_necessaria
- responsavel
- prazo

### Aba 4 — resumo
Indicadores:
- comissão total por mês
- recebido vs pendente
- total por seguradora
- total por produtor
- divergências abertas

## Processo operacional mensal

### Etapa 1 — Entrada
- Salvar todos os PDFs e relatórios por mês e seguradora
- Nome padrão sugerido:
  - `2026-04_porto_comissao.pdf`
  - `2026-04_itau_producao.pdf`

### Etapa 2 — Extração
- Usar `pdf-extract` para texto bruto
- Quando houver tabela ruim, revisar manualmente os campos críticos:
  - seguradora
  - produtor
  - proposta/apólice
  - valor
  - data

### Etapa 3 — Normalização
- Lançar tudo na planilha mestre
- Padronizar nomes de seguradora e produtor
- Evitar IDs numéricos como número puro quando houver zeros à esquerda

### Etapa 4 — Conciliação
- Cruzar recebimentos do banco com lançamentos esperados
- Marcar cada item como:
  - conciliado
  - parcial
  - pendente
  - divergente

### Etapa 5 — Resumo executivo
Gerar 1 resumo curto com:
- total esperado
- total recebido
- total pendente
- principais divergências
- ação necessária

## Regras práticas
- Não confiar cegamente em texto extraído de PDF
- Conferir sempre totais, datas e identificadores
- Usar nomenclatura única para seguradoras e produtores
- Guardar o nome do arquivo de origem em cada linha

## O que automatizar primeiro
1. organização da pasta de entrada
2. extração de PDFs para texto
3. consolidação em planilha base
4. identificação de divergências

## O que eu preciso do Marcelo para subir isso de nível
1. 2 ou 3 PDFs reais de comissão
2. 1 extrato ou exemplo de recebimento bancário
3. nomes padronizados das seguradoras
4. regra de comissão dos produtores, quando variar
