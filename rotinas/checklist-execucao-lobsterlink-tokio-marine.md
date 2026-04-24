# Checklist de execução — LobsterLink para Tokio Marine

Data: 2026-04-19
Uso: execução prática do piloto

## Bloco 1 — antes de instalar
- [ ] confirmar que o gargalo real da Tokio Marine é login, 2FA, CAPTCHA ou intervenção humana
- [ ] confirmar que vale testar LobsterLink em vez de browser normal
- [ ] garantir tempo para instalar, testar e reverter se necessário

## Bloco 2 — backup
- [ ] rodar `git status --short` no workspace
- [ ] fazer commit de backup se houver mudança
- [ ] fazer `git push origin master`
- [ ] copiar `~/.openclaw/openclaw.json` para um `.bak` com timestamp
- [ ] registrar baseline com `openclaw gateway status` e `openclaw status`

## Bloco 3 — staging da extensão
- [ ] clonar LobsterLink em caminho estável dentro do workspace
- [ ] confirmar caminho absoluto da extensão
- [ ] não usar pasta temporária

## Bloco 4 — config
- [ ] revisar schema/config atual do browser
- [ ] preservar `extraArgs` existentes
- [ ] adicionar:
  - [ ] `--disable-extensions-except=/caminho/absoluto/lobsterlink`
  - [ ] `--load-extension=/caminho/absoluto/lobsterlink`
- [ ] garantir `browser.defaultProfile = openclaw`

## Bloco 5 — ativação
- [ ] reiniciar gateway
- [ ] reiniciar fluxo do browser isolado se necessário
- [ ] confirmar que o browser isolado subiu com as flags da extensão

## Bloco 6 — verificação técnica
- [ ] confirmar que a extensão carregou de verdade
- [ ] descobrir extension ID
- [ ] validar bridge URL `chrome-extension://<id>/bridge.html`
- [ ] atualizar a skill runtime com bridge URL real e status de instalada

## Bloco 7 — teste funcional Tokio Marine
- [ ] abrir portal Tokio Marine no browser isolado
- [ ] navegar até o ponto real de bloqueio
- [ ] iniciar host da aba certa
- [ ] abrir viewer link
- [ ] executar intervenção humana
- [ ] validar que a sessão continua ativa
- [ ] validar que o agente consegue seguir navegando

## Bloco 8 — decisão
- [ ] GO restrito
- [ ] NO-GO
- [ ] INCONCLUSIVO
- [ ] registrar motivo da decisão

## Bloco 9 — rollback se necessário
- [ ] remover flags da extensão da config
- [ ] restaurar backup do `openclaw.json` se necessário
- [ ] reiniciar gateway
- [ ] validar retorno ao estado anterior
- [ ] registrar causa da reversão

## Definição rápida de sucesso
Sucesso = login/desbloqueio humano funcionou, sessão ficou ativa e o agente continuou no portal.

## Definição rápida de falha
Falha = muita instabilidade, sessão caiu, bridge não sustentou o fluxo ou o problema real não era autenticação humana.
