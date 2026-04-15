---
name: emitir-notas-fiscais-leevre
description: Ler PDFs de uma pasta do Google Drive, extrair dados de tomador e serviço, consolidar base em Google Sheets e preparar emissão de notas fiscais da Leevre. Use quando houver rotina mensal de notas, leitura de PDFs modelo, cadastro de tomadores, preenchimento de valores e emissão assistida no portal da contabilidade.
---

# emitir-notas-fiscais-leevre

## Objetivo
Transformar a rotina de notas fiscais da Leevre em um fluxo confiável, reaproveitável e menos manual.

## Fluxo principal
1. ler pasta de PDFs no Google Drive
2. identificar tomador, documento e serviço prestado
3. consolidar a base em Google Sheets
4. receber valor mensal na planilha
5. preparar emissão assistida no portal da contabilidade
6. registrar status, número e link da nota

## Campos mínimos
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

## Regras operacionais
- começar em modo assistido
- só automatizar emissão final depois de validar o fluxo real
- tratar PDF ruim ou OCR ruim como exceção manual
- registrar sempre origem do documento e retorno da emissão

## Recursos
- Ler `references/fluxo.md` para detalhes do processo.
