# Comandos iniciais do Modo A, notas fiscais

## 1. Preparar a prévia do mês
```bash
state/operacao/notas-fiscais/scripts/preparar_previa_mes.py 2026-04
```

## 2. Atualizar Porto na prévia
```bash
state/operacao/notas-fiscais/scripts/capturar_porto.py 2026-04 \
  --valor-bruto 16002.71 \
  --origem 'captura manual assistida' \
  --descricao 'SERVIÇOS DE CORRETAGEM COMPETÊNCIA 04/2026'
```

## Resultado esperado
O arquivo abaixo passa a concentrar a prévia mensal:
```text
state/operacao/notas-fiscais/pre-emit/2026-04.json
```

## Próximo estágio
Replicar o mesmo padrão de script para:
- Banestes
- HDI
- Allianz
- Bradesco
- Yelum

## Observação
Neste momento, a Porto já está com a estrutura de captura conectada à prévia mensal.
