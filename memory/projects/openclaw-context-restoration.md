# Restauração de Contexto após Troca de Modelo no OpenClaw

## Objetivo
Criar um processo simples, replicável e confiável para recuperar continuidade, memória operacional e aderência ao contexto após trocar o modelo de um agente OpenClaw.

## Diagnóstico técnico
Quando um agente piora depois de trocar de modelo, a causa provável não é só qualidade do modelo. O problema costuma estar na combinação entre:
- índice de memória antigo ou incompleto
- retrieval semântico desalinhado com a forma como o novo modelo pergunta e interpreta contexto
- sessão recente pobre, sem decisões e projetos dominantes
- boot que não injeta corretamente arquivos-base
- GitHub ou workspace deixando de ser fonte de verdade consistente
- decisões e pendências não salvas antes de compactação

## Por que reindexação ajuda
Mesmo sem trocar o embedding model, `openclaw memory index --force` ajuda porque força o OpenClaw a reler todos os arquivos de memória, recriar registros do índice, limpar estado antigo e reconstruir relações semânticas a partir do conteúdo atual. Na prática, reduz ruído de índice velho e melhora a chance de recuperar o contexto certo depois da troca.

## Por que warm-up ajuda
O warm-up cria memória recente dominante. Alguns minutos relembrando projetos, decisões, preferências, pendências e padrões de execução dão ao modelo um contexto operacional fresco antes de tarefas críticas. Isso reduz resposta genérica e melhora aderência ao jeito real do usuário.

## Checklist de correção
- Confirmar modelo default com `openclaw models status --plain`.
- Confirmar modelo da sessão ativa no status do OpenClaw.
- Rodar `openclaw memory index --force`.
- Verificar se `SOUL.md`, `USER.md`, `MEMORY.md`, notas recentes e sessões recentes estão sendo lidos no boot.
- Fazer warm-up com projetos ativos, decisões, preferências e tarefas abertas.
- Validar fluxo GitHub: pull, leitura de contexto, execução, validação, registro e push quando aplicável.
- Antes de compactar, salvar decisões, lições, projetos, pendências e nota diária.

## Quick wins imediatos
- Manter `MEMORY.md` como índice e mover conteúdo durável para `memory/context/*.md` e `memory/projects/*.md`.
- Criar ou atualizar nota diária quando faltar `memory/YYYY-MM-DD.md`.
- Registrar toda troca de modelo em `memory/context/decisions.md`.
- Usar status em camadas: config, catálogo de modelos, sessão ativa e Gateway.
- Fazer uma conversa curta de warm-up antes de qualquer tarefa crítica.

## Recomendações para outros usuários
- Não assuma que trocar modelo é só trocar ID: valide boot, memória e retrieval.
- Reindexe sempre que reorganizar memória, trocar modelo ou restaurar backup.
- Faça warm-up com contexto real, não com resumo genérico.
- Trate GitHub como fonte de verdade apenas se o ciclo pull-execute-register-push estiver disciplinado.
- Automatize só depois de validar que o agente está recuperando decisões e pendências corretamente.

## Execução em 2026-05-15
- Skill externa `codex-review` auditada e instalada em `/home/marcelo/.openclaw/agents/main/agent/codex-home/skills/codex-review`.
- Reindexação forçada executada com `HOME=/home/marcelo openclaw memory index --force`.
- Resultado: índice `main` atualizado, índice `marcelo-pessoal` atualizado, dois agentes com busca desabilitada.
- Alerta observado: `sqlite-vec unavailable`; busca vetorial pode ficar degradada até corrigir a extensão.
- `openai-codex/gpt-5.5` foi rejeitado pelo runtime da sessão como modelo não permitido.
- Estado operacional suportado: `openai/gpt-5.5` com Runtime `OpenAI Codex`.
- Preferência registrada: GPT 5.5 para uso diário; GPT 5.4 para crons `agentTurn` quando houver campo `payload.model`.
