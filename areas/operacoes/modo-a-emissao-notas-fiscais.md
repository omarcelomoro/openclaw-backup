# Modo A, emissão de notas fiscais da Leevre

Data base: 2026-04-18

## Objetivo
Permitir o seguinte fluxo operacional:
1. Marcelo diz: `emitir notas de abril`
2. Livri captura os valores das seguradoras
3. Livri monta uma prévia consolidada
4. Marcelo responde: `confirmado`
5. Livri emite as notas

## Estado atual
### Já existe
- playbooks por seguradora
- base fiscal validada por NF de referência
- script de emissão assistida da Virei: `state/emitir_nf_virei_contador.py`
- quadro operacional consolidado em `areas/operacoes/quadro-operacional-notas-fiscais-seguradoras.md`

### Ainda falta para o Modo A completo
- guardar credenciais seguras de cada portal
- automatizar captura do valor nos portais
- consolidar a prévia mensal em arquivo único
- amarrar confirmação humana antes da emissão

## Fluxo-alvo

### Etapa 1, comando de captura
Entrada humana:
- `emitir notas de abril`

Interpretação operacional:
- competência alvo = `2026-04`
- capturar dados do mês operacional correspondente em cada seguradora
- montar a prévia sem emitir

### Etapa 2, captura por seguradora
Para cada seguradora ativa:
- abrir playbook operacional
- entrar no portal com credencial do servidor
- filtrar a competência correta
- capturar o valor bruto correto
- preencher estrutura consolidada da competência

### Etapa 3, montagem da prévia
Gerar uma prévia com, no mínimo:
- seguradora
- competência
- valor bruto
- tomador
- CNPJ
- descrição prevista
- modo de emissão
- status
- observações/bloqueios

### Etapa 4, confirmação humana
Mensagem esperada da Livri:
- resumo consolidado
- itens prontos para emissão
- itens bloqueados, se houver
- pedido de confirmação curta: `confirmado`

### Etapa 5, emissão
Depois do `confirmado`:
- emitir seguradoras prontas
- salvar PDFs
- registrar número das notas
- atualizar status final
- devolver resumo da execução

## Regras de segurança
- não emitir automaticamente sem confirmação no Modo A
- não salvar senhas em chat
- guardar credenciais apenas em arquivo local protegido no servidor
- bloquear emissão quando faltar dado fiscal crítico

## Estrutura recomendada de arquivos

```text
state/operacao/notas-fiscais/
  config/
    seguradoras.json
  credenciais/
    porto.env
    bradesco.env
    yelum.env
    allianz.env
    hdi.env
    banestes.env
  pre-emit/
    2026-04.json
  emitidas/
    2026-04/
      resumo.json
      PDFs/
```

## Formato da prévia mensal
Arquivo sugerido: `state/operacao/notas-fiscais/pre-emit/YYYY-MM.json`

Campos por item:
- seguradora
- competencia
- valor_bruto
- tomador_nome
- tomador_cnpj
- descricao
- modo_emissao
- status
- origem_valor
- observacoes

## Status recomendado por seguradora
- Porto: script/API
- Banestes: script/API
- HDI: script/API
- Allianz: script/API
- Bradesco: manual assistido
- Yelum: manual assistido

## Comandos operacionais-alvo

### capturar_notas_mes
Função:
- captura valores
- gera prévia
- não emite

### conferir_notas_mes
Função:
- mostra resumo da prévia
- destaca bloqueios

### emitir_notas_mes
Função:
- emite somente após confirmação humana
- salva PDFs e resumo final

## Próximo passo de implementação
1. criar o arquivo de configuração das seguradoras
2. criar a estrutura de credenciais
3. criar um script de preparação da prévia mensal
4. só depois conectar browser/script por seguradora
