# Quadro operacional, notas fiscais por seguradora

Data base: 2026-04-18

## Objetivo
Consolidar o estado real do fluxo de captura de valor e emissão de notas fiscais da Leevre por seguradora.

## Classificação operacional

### Nível 1, pronto para emissão via script/API

#### Porto Seguros
- status: pronta
- captura do valor: mapeada
- regra do valor: usar `VALOR BRUTO`
- emissão: validada
- modo atual: script/API Virei
- observação: existe caso real emitido com sucesso

#### Banestes
- status: pronta
- captura do valor: mapeada
- regra do valor: usar total de `Valor Base`
- emissão: validada tecnicamente
- modo atual: script/API Virei
- observação: não usar `Valor Pago`

#### HDI
- status: pronta
- captura do valor: mapeada
- regra do valor: usar total de `Vlr. Bruto`
- emissão: validada tecnicamente
- modo atual: script/API Virei
- observação: não usar `Líquida`

#### Allianz
- status: pronta
- captura do valor: mapeada
- regra do valor: usar `Total Bruto`
- emissão: validada tecnicamente
- modo atual: script/API Virei
- observação: usar bloco `Comissões Pagas`

### Nível 2, pronto para uso assistido

#### Bradesco Seguros
- status: pronta para uso assistido
- captura do valor: mapeada
- regra do valor: usar card `Comissões`
- emissão: viável em modo manual assistido
- modo atual: manual assistido
- fiscal: validado por NF de referência
- lacuna: faltam `clientId` e `productId/serviceId` confirmados para migrar para script/API
- observação: playbook operacional já existe e está consistente

### Nível 3, incompleta

#### Yelum
- status: pronta para uso assistido
- captura do valor: mapeada
- regra do valor: usar `Total bruto`
- emissão: pronta em modo assistido
- modo atual: manual assistido
- fiscal: validado por NF de referência do Drive
- lacuna principal: confirmar IDs internos da Virei se migrar para script/API
- observação: portal, filtro operacional e base fiscal já mapeados, com exemplo validado de `Total bruto = R$ 4.121,07`

## Fluxo único recomendado

### Etapa 1, captura do valor
- identificar seguradora
- abrir o playbook correspondente
- levantar o valor bruto correto do mês anterior
- preencher `lancamentos_mensais`

### Etapa 2, validação fiscal
- confirmar tomador
- confirmar CNPJ
- confirmar descrição
- confirmar retenções quando aplicável
- usar NF de referência sempre que existir

### Etapa 3, decisão do modo de emissão
- se seguradora estiver no nível 1: emitir por script/API
- se seguradora estiver no nível 2: emitir em modo manual assistido
- se seguradora estiver no nível 3: bloquear e completar mapeamento antes

### Etapa 4, registro
- salvar PDF
- registrar número da nota
- atualizar status_emissao
- registrar evidência operacional

## Próximos passos recomendados
1. completar Yelum
2. validar se Bradesco vai continuar assistida ou migrar para API
3. depois consolidar isso dentro da skill final

## Observação técnica
A skill `skills/notas-fiscais-seguradoras-leevre/` está com arquivos pertencendo a `root`, então a consolidação final lá depende de ajuste de permissão no servidor ou edição com privilégios elevados fora deste canal.
