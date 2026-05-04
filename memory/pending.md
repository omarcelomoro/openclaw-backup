# Pendências

> Regra operacional aprovada em 24/04/2026: esta lista deve funcionar como memória viva de tarefas abertas e esquecimentos evitáveis. Quando Marcelo pedir, a assistente deve resgatar daqui o que está pendente, parado ou sem conclusão.

## Prioridade agora
- [ ] Enviar 2 ou 3 PDFs reais de comissão
- [ ] Enviar 1 exemplo de extrato/recebimento bancário
- [ ] Confirmar nomes padronizados das seguradoras
- [ ] Confirmar se a regra de comissão dos produtores varia

## Aguardando Marcelo
- [ ] Confirmar outputs de hardening atual na VPS (UFW, Fail2ban, SSH, exec security)
- [ ] Validar se `IDENTITY.md`, `USER.md`, `AGENTS.md` e `MEMORY.md` existem ou existiram no backup GitHub

## Aguardando sistema / investigação
- [ ] Confirmar se `tools.exec.security` ainda está em `full`
- [ ] Confirmar se já existiu `MEMORY.md` funcional antes ou se essa camada nunca ficou pronta

## Depois / estrutural
- [ ] Consolidar mapas das ferramentas principais da operação
- [x] Criar rotina leve de revisão de pendências e itens parados — ver `rotinas/rotina-operacional-revisao-pendencias-followup-leevre.md`

## Para amanhã — 2026-05-04
- [ ] Finalizar auditoria do ClawSweeper e transformar o método em rotina interna da Leevre/OpenClaw, sem instalar o bot por enquanto.
- [ ] Decidir o que fazer com o plugin `crabbox`, pois a auditoria marcou uso de `child_process` como crítico.
- [ ] Avaliar criação de `plugins.allow` explícito para reduzir superfície de plugin.
- [ ] Corrigir/validar pinagem do `lossless-claw` no registro para remover alerta de spec npm não pinado.
- [ ] Rodar nova auditoria `openclaw security audit --deep` depois das correções e registrar resultado.
- [ ] Consolidar template operacional inspirado em `/goal`: contexto aquecido → definição quantificada de pronto → caça/diagnóstico → correção com gates.
- [ ] Decidir atualização/uso do Crabbox: atual local `0.3.0`, release pública `0.4.0`; avaliar se mantém desabilitado, atualiza plugin/CLI ou remove enquanto não houver uso real.
