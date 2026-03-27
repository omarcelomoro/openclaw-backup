# Infraestrutura Livri (VPS + OpenClaw)

**Status:** em andamento
**Última atualização:** 26/03/2026

## Próximo passo
Configurar email `livri@leevrecorretora.com.br` via Google Workspace

## Bloqueios
- Marcelo precisa decidir sobre Google Workspace (~R$30/mês)
- Informar onde o domínio `leevrecorretora.com.br` está hospedado

## Concluído
- VPS configurado (IP: 187.77.247.207)
- SSH key-only, password auth desativado
- UFW + Fail2ban ativos
- Gateway rodando em loopback (tunnel SSH)
- Backup diário no GitHub (`omarcelomoro/openclaw-backup`)
- Credenciais em `/root/.openclaw/.env` (chmod 600)
