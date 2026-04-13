---
name: auditoria-integridade-leevre
description: Audita coerência estrutural, operacional e de segurança do cérebro da Leevre. Use para revisar arquivos órfãos, skills sem index, rotinas sem uso, duplicações, riscos de configuração e desalinhamentos entre áreas, agentes e operação real.
---

# auditoria-integridade-leevre

## Objetivo
Fazer revisão periódica do cérebro da Leevre para manter clareza, governança e segurança.

## Verificar
- skills existentes versus skills indexadas
- rotinas existentes versus rotinas realmente usadas
- documentos duplicados ou conflitantes
- arquivos importados ainda não adaptados
- riscos de segurança no OpenClaw e nos fluxos de agentes
- desalinhamento entre marketing, vendas, operação e memória

## Saída esperada
- problemas encontrados
- impacto prático de cada problema
- correção sugerida
- prioridade da correção

## Regra
Não auditar só por estética. Priorizar o que afeta:
- execução
- memória útil
- segurança
- previsibilidade
