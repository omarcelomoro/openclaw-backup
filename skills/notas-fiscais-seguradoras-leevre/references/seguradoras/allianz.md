# Allianz — fluxo operacional

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
2. revisar a descrição fiscal esperada
3. rodar `state/emitir_nf_virei_contador.py` com IDs confirmados
4. emitir a nota
5. baixar o PDF
6. salvar evidência

## Bloqueios conhecidos
- divergência entre valor capturado e valor a emitir
- falha de autenticação
- falha no retorno da emissão

## Saída esperada
- nota emitida
- número da nota
- PDF salvo
- registro operacional salvo
