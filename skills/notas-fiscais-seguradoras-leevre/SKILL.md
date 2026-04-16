# Skill: notas-fiscais-seguradoras-leevre

## Objetivo
Executar o fluxo operacional de emissão de notas fiscais da Leevre para seguradoras, com segurança, rastreabilidade e reaproveitamento de playbooks já validados.

## Dono
Agente de Operações.

## Quando usar
- quando houver comissão fechada para emitir nota
- quando a seguradora já tiver mapeamento operacional e fiscal confirmado
- quando for necessário reaplicar um fluxo já validado

## Não usar quando
- faltarem dados fiscais críticos
- faltarem IDs internos confirmados da Virei Contador para automação via API
- o portal da seguradora tiver mudado e o playbook estiver desatualizado

## Entradas mínimas
- seguradora
- competência
- valor bruto
- referência operacional da captura do valor
- dados fiscais confirmados ou NF de referência

## Saídas esperadas
- nota emitida ou bloqueio explicado
- número da nota, quando emitida
- PDF/evidência salvo
- status operacional registrado

## Fontes de verdade
- `references/fontes-oficiais.md`
- `cerebro/referencias/seguradoras/`
- `cerebro/referencias/notas-fiscais/`
- `state/emitir_nf_virei_contador.py`

## Fluxo padrão
1. identificar seguradora e competência
2. localizar playbook e mapeamento existentes
3. confirmar valor bruto correto no portal/evidência
4. confirmar tomador, CNPJ, descrição e retenções
5. decidir modo de execução:
   - manual assistido
   - API/script Virei Contador
   - bloqueado por falta de dado crítico
6. emitir a nota
7. baixar e salvar PDF/evidência
8. registrar resultado e pendências

## Regras invioláveis
- nunca chutar clientId, productId, serviceId ou dados fiscais
- sempre preferir NF de referência quando existir
- em caso de divergência entre playbook e portal real, registrar e escalar
- toda emissão precisa deixar rastro verificável

## Seguradoras já mapeadas parcialmente ou totalmente
- Porto
- Banestes
- Allianz
- HDI
- Bradesco Seguros
- Yelum (operacional parcial, fiscal pendente)

## Referências internas da skill
- `references/fluxo.md`
- `references/seguradoras.md`
- `references/checklist-por-seguradora.md`
- `references/fontes-oficiais.md`
- `references/evidencia-e-saida.md`

## Fluxos operacionais por seguradora
- `references/seguradoras/porto.md`
- `references/seguradoras/banestes.md`
- `references/seguradoras/allianz.md`
- `references/seguradoras/hdi.md`

## Saída padronizada por emissão
- seguradora
- competência
- valor bruto
- modo de execução
- status final: emitida ou bloqueada
- número da nota, quando houver
- pendências encontradas
- caminho da evidência salva

## Evolução prevista
- automação browser para captura de valores
- descoberta assistida de IDs internos da Virei via DevTools/Network
- geração de evidência padronizada por emissão
