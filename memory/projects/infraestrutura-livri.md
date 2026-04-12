# Infraestrutura Livri (VPS + OpenClaw)

**Status:** em andamento
**Última atualização:** 02/04/2026

## Próximo passo
Configurar email `livri@leevrecorretora.com.br` via Google Workspace

## Bloqueios
- Marcelo precisa decidir sobre Google Workspace (~R$30/mês)
- Informar onde o domínio `leevrecorretora.com.br` está hospedado

## Concluído
- VPS configurado (IP: 187.77.247.207)
- SSH key-only, password auth desativado (ATENÇÃO: PasswordAuthentication yes no sshd_config atual — revisar)
- UFW + Fail2ban ativos
- Gateway rodando em loopback (tunnel SSH)
- Backup diário no GitHub (`omarcelomoro/openclaw-backup`)
- Credenciais em `/root/.openclaw/.env` (chmod 600)
- SSH ouvindo nas portas 22 e 2222 (2222 para redes que bloqueiam 22)
- Firewall Hostinger reativado — grupo "Leevre-VPS" (ID: 256935) com portas 22, 2222, 80, 443, 18789
- **WhatsApp integrado** (27/03/2026) — número Leevre: 5527996101272, via @leevrebot
- API Token Hostinger configurado (salvo no .env)

## Notas importantes (02/04/2026)
- Problema de conexão resolvido: rede do escritório bloqueava porta 22
- Solução: usar `ssh -p 2222 root@187.77.247.207` quando na rede do escritório
- UFW foi temporariamente desativado durante diagnóstico e reativado
- Firewall Hostinger: grupo antigo (256672) deletado, novo grupo "Leevre-VPS" (256842→256935) ativo
