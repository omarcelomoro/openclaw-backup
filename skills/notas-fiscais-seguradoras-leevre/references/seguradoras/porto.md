# Porto — fluxo operacional

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
2. validar se a descrição segue o padrão da operação
3. rodar `state/emitir_nf_virei_contador.py` com IDs confirmados
4. emitir a nota
5. baixar o PDF
6. salvar evidência

## Bloqueios conhecidos
- divergência de valor bruto
- falha de login na Virei
- erro de emissão retornado pela API

## Saída esperada
- nota emitida
- número da nota
- PDF salvo
- registro operacional salvo
