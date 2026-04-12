# Infraestrutura

## Servidor
- IP: 187.77.247.207
- OS: Ubuntu 24.04.4 LTS
- Kernel: 6.8.0-107-generic

## Containers
- evolution_api: WhatsApp (8080 — pendente migração Traefik)
- traefik: reverse proxy (80/443)
- n8n: automações (localhost:5678)
- openclaw-sandbox: agente Livri

## Segurança
- UFW: allow 22, 2222, 80, 443, 8080
- SSH: PasswordAuthentication no, PermitRootLogin no
- Acesso: usuário marcelo por chave ed25519

## Pendências
- Migrar Evolution para evolution.leevre.com.br
- Fechar porta 8080 após migração
- Rotacionar segredos da Evolution
- Revisar porta 2222
