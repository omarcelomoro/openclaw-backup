# Lições Aprendidas

## 🔒 Estratégicas

### O cérebro existia, a continuidade falhou (09/04/2026)
A base técnica e operacional do sistema já havia sido montada no passado, mas a memória persistente e a costura autobiográfica falharam. A prioridade é preservar identidade, contexto e decisões, não só infraestrutura.

### Backup de workspace não é igual a backup de memória viva (09/04/2026)
Um repositório GitHub pode existir e ainda assim não conter `SOUL.md`, `USER.md`, `IDENTITY.md`, `AGENTS.md` e `MEMORY.md` da forma esperada. Sempre validar a estrutura real do backup.

### Primeiro atacar gargalo real, depois automação bonita (09/04/2026)
Na Leevre, o maior ganho imediato vem de comissão, conciliação, PDFs e planilhas. Marketing, tracking e Telegram vêm depois da base operacional mínima.

## ⏳ Táticas

### O workspace atual está mais pobre do que o histórico (09/04/2026)
O estado atual do workspace não reflete toda a riqueza do cérebro histórico. `USER.md` está curto e o backup GitHub atual parece seguir outra arquitetura.

### Revisar `tools.exec.security` antes de assumir permissões amplas (09/04/2026)
Existe histórico de `tools.exec.security = full`. Isso precisa ser confirmado no estado atual antes de ser tratado como desejável.

### Upgrade do OpenClaw deve seguir ritual de backup e validação (14/04/2026)
Quando Marcelo pedir upgrade/update do OpenClaw, a sequência padrão deve ser: validar Git no workspace, fazer backup local e push para o GitHub antes da atualização, executar `npm install -g openclaw@latest` e, se houver `EACCES`, orientar o uso de `sudo`, reiniciar o gateway, validar com `openclaw gateway status`, `openclaw status` e confirmar reachability real com `openclaw gateway probe` antes de considerar encerrado.
