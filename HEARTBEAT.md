# HEARTBEAT.md — Livri 🐝

## Horários ativos
- **Falar:** 09:30–17:30 (Brasília) → UTC 12:30–20:30
- **Calar:** madrugada, antes das 9h30, após 17h30, fins de semana (exceto urgências)

## O que checar

### 📧 Email (marcelo@leevrecorretora.com.br)
- Buscar: `is:unread is:important`
- Avisar se: email importante de clientes, administradoras (Itaú, Bradesco, Servopa, Porto), parceiros ou assuntos financeiros
- Ignorar: promoções, newsletters, marketing

### 📅 Agenda (Google Calendar)
- Checar eventos nas próximas 24h
- Avisar se: compromisso em <2h sem aviso prévio dado

### 📋 Projetos parados
- Se algum projeto em PROJECTS.md ficou sem atualização >7 dias → mencionar

## Regras de silêncio
- Nada urgente → `HEARTBEAT_OK` (sem mensagem)
- Organização de memória → fazer em background sem avisar
- Não mandar mais de 1 alerta por assunto por dia

## Comandos úteis
```bash
# Email urgente
gogcli gmail search "is:unread is:important" -a marcelo@leevrecorretora.com.br

# Agenda
gogcli calendar events list -a marcelo@leevrecorretora.com.br
```
