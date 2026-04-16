# Evidência e saída operacional

## Evidência mínima por emissão
- seguradora
- competência
- valor bruto
- data da emissão
- modo de execução: manual assistido ou API/script
- status final
- número da nota, quando houver
- PDF salvo, quando houver
- observações ou bloqueios encontrados

## Estrutura sugerida de evidência
- pasta por seguradora
- subpasta por competência
- arquivos nomeados com padrão consistente

Exemplo:
- `evidencias/notas-fiscais/bradesco/2026-03/`
- `evidencias/notas-fiscais/porto/2026-03/`

## Nome sugerido para arquivos
- `NF-<seguradora>-<competencia>-<numero>.pdf`
- `registro-<seguradora>-<competencia>.md`

## Status operacionais padronizados
- `emitida`
- `bloqueada-fiscal`
- `bloqueada-id-interno`
- `bloqueada-portal`
- `pendente-validacao`

## Saída textual padrão da skill
- Seguradora
- Competência
- Valor bruto
- Modo de execução
- Status final
- Número da nota, se houver
- Pendência principal, se houver
- Caminho da evidência salva
