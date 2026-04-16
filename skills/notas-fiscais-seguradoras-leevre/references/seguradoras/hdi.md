# HDI — fluxo operacional

## Status
Pronta para emissão.

## Pré-condições
- competência definida
- valor bruto confirmado
- cliente e serviço já validados na Virei
- script operacional disponível

## Entrada mínima
- competência
- valor bruto
- data da venda/emissão
- descrição da nota

## Execução padrão
1. confirmar competência e valor bruto
2. revisar se a emissão segue o padrão já validado
3. rodar `state/emitir_nf_virei_contador.py` com IDs confirmados
4. emitir a nota
5. baixar o PDF
6. salvar evidência

## Bloqueios conhecidos
- divergência de valor
- falha de login
- erro de emissão retornado pelo emissor

## Saída esperada
- nota emitida
- número da nota
- PDF salvo
- registro operacional salvo
