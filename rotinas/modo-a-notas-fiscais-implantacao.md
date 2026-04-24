# Implantação do Modo A, notas fiscais

## Resultado esperado
Marcelo poderá dizer:
- `emitir notas de abril`

E a rotina deverá:
1. capturar os valores
2. montar a prévia
3. esperar `confirmado`
4. emitir as notas

## Checklist de implantação

### 1. Credenciais
Salvar no servidor:
- `~/.config/leevre-secrets/porto.env`
- `~/.config/leevre-secrets/banestes.env`
- `~/.config/leevre-secrets/hdi.env`
- `~/.config/leevre-secrets/allianz.env`
- `~/.config/leevre-secrets/bradesco.env`
- `~/.config/leevre-secrets/yelum.env`
- `~/.config/leevre-secrets/virei.env`

### 2. Captura por portal
Implementar browser/script por seguradora para:
- login
- navegação
- filtro da competência
- leitura do valor correto

### 3. Consolidação
Gerar arquivo em:
- `state/operacao/notas-fiscais/pre-emit/YYYY-MM.json`

### 4. Emissão
Usar `state/emitir_nf_virei_contador.py` para os casos em `script_api`.

### 5. Confirmação
No Modo A, a etapa de emissão só roda depois da mensagem humana `confirmado`.

## Regras do Modo A
- não emitir sem confirmação
- se houver item bloqueado, destacar na prévia
- se faltar valor, tomador ou descrição, não emitir aquele item
- registrar PDF e número da nota no resumo final

## Estado atual
- desenho operacional: pronto
- configuração inicial das seguradoras: pronta
- playbooks: prontos
- automação ponta a ponta: pendente
