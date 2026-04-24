# Teste — Skill de Notas Fiscais Leevre

## Objetivo do teste
Validar um fluxo em 2 etapas:
1. ler uma pasta do Google Drive com documentos base
2. extrair dados e consolidar em Google Sheets

Depois disso, em uma segunda fase, conectar isso à emissão no site da contabilidade.

## Escopo do teste 1
- origem: pasta `NF` no Google Drive
- leitura esperada:
  - tomador
  - CNPJ/CPF do tomador
  - serviço prestado
  - observações relevantes
- saída:
  - Google Sheets modelo para preenchimento mensal dos valores

## Fase 2, depois do teste 1
- ler a planilha mensal
- acessar o portal da contabilidade
- preencher dados da nota
- emitir nota fiscal

## Validação real concluída em 2026-04-14
- primeira emissão real concluída com sucesso no portal da Virei Contador
- tomador validado: `PORTO SEGURO COMPANHIA DE SEGUROS GERAIS`
- valor validado: `R$ 16.002,71`
- número emitido: `57`
- status final: `EMITIDA`
- PDF salvo em `state/nf-teste/NFSE-PORTO-SEGUROS-57.pdf`
- registro técnico do caso: `state/nf-teste/primeira-emissao-real-2026-04-14.md`
- script assistido criado: `state/emitir_nf_virei_contador.py`

## Riscos
- OCR ou PDF ruim pode exigir revisão manual
- tomador pode vir com variações de nome/CNPJ
- site da contabilidade pode ter captcha, 2FA ou fluxo instável
- emissão real é ação externa sensível, então precisa de confirmação antes do envio final

## Recomendação operacional
Seguir em modo assistido:
- leitura automática
- planilha consolidada
- emissão com script/API e revisão de dados antes do disparo
- só depois automatização completa por lote
