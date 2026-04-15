# Fluxo da skill de notas fiscais Leevre

## Fase 1, ingestão e preparo
1. ler PDFs da pasta `NF` no Google Drive
2. extrair dados-base por tomador
3. consolidar cadastro base em Google Sheets
4. deixar coluna mensal de valor para preenchimento manual

## Campos mínimos por linha
- competencia
- arquivo_origem
- tomador_nome
- tomador_documento
- tipo_documento
- servico_prestado
- municipio
- observacoes
- valor_nota
- status_emissao
- numero_nota
- link_nota

## Fase 2, emissão assistida
1. ler planilha mensal
2. filtrar linhas prontas para emissão
3. montar o payload no formato real do emissor
4. criar a venda em `/api/sales`
5. emitir em `/api/sales/{id}/emitir-nfse`
6. sincronizar status em `/api/sales/{id}/sync-nfse`
7. baixar o PDF em `/api/sales/{id}/nfse/pdf`
8. registrar retorno na planilha

## Caso real já validado
- primeira emissão real: 2026-04-14
- tomador: PORTO SEGURO COMPANHIA DE SEGUROS GERAIS
- valor: R$ 16.002,71
- número emitido: 57
- status final: EMITIDA
- referência técnica: `state/nf-teste/primeira-emissao-real-2026-04-14.md`

## Regras
- não emitir automaticamente sem modo de confirmação até validar o fluxo
- tratar OCR ruim como exceção manual
- registrar origem do PDF e status da emissão
- manter cadastro do tomador separado do valor mensal quando isso facilitar manutenção
