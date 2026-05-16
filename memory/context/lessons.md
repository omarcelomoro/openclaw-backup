# Lições Aprendidas

## 🔒 Estratégicas

### O cérebro existia, a continuidade falhou (09/04/2026)
A base técnica e operacional do sistema já havia sido montada no passado, mas a memória persistente e a costura autobiográfica falharam. A prioridade é preservar identidade, contexto e decisões, não só infraestrutura.

### Backup de workspace não é igual a backup de memória viva (09/04/2026)
Um repositório GitHub pode existir e ainda assim não conter `SOUL.md`, `USER.md`, `IDENTITY.md`, `AGENTS.md` e `MEMORY.md` da forma esperada. Sempre validar a estrutura real do backup.

### Primeiro atacar gargalo real, depois automação bonita (09/04/2026)
Na Leevre, o maior ganho imediato vem de comissão, conciliação, PDFs e planilhas. Marketing, tracking e Telegram vêm depois da base operacional mínima.

## 🤖 Arquitetura de Agentes (referência)

### Padrão Browserbase/bb: agente generalista com skill routing (11/05/2026)
A Browserbase construiu um único agente interno (`bb`) que opera via Slack para toda a empresa (eng, ops, vendas, suporte, exec). Não constroem bots específicos por função — constroem um loop central e carregam skills por demanda. Lições:
- **Skill routing explícito no system prompt**: tabela que mapeia tipo de pedido → skills que devem ser carregadas
- **Carrega só o necessário**: não sobe todas as skills pra todo request — contexto menor, performance melhor
- **Sandbox isolado por thread/sessão**: conversa do Slack = workspace persistente com contexto, arquivos e histórico
- **Credential brokering**: sandbox nunca vê chave real; só recebe token de sessão. Chave real só existe dentro da função serverless proxy
- **RBAC + ABAC**: controle por papel + por atributo de agente — cada sessão carrega escopo explícito de permissões
- **Snapshot pre-aquecido**: sandbox já inicia com código, deps e ferramentas instaladas — startup quase instantâneo

Referência: https://www.browserbase.com/blog/internal-agents (Kyle Jeong, abr/2026)

### Plugin `@browserbasehq/openclaw-browserbase` existe mas requer API key (11/05/2026)
Plugin oficial da Browserbase para o OpenClaw. Substitui o browser tool padrão por sessões em nuvem com anti-bot stealth, CAPTCHA solving e residential proxies. Não instalar sem uma API key configurada. Se Marcelo criar conta no Browserbase (tem plano gratuito), configurar em: `openclaw plugins install @browserbasehq/openclaw-browserbase` + config da API key.

## ⏳ Táticas

### O workspace atual está mais pobre do que o histórico (09/04/2026)
O estado atual do workspace não reflete toda a riqueza do cérebro histórico. `USER.md` está curto e o backup GitHub atual parece seguir outra arquitetura.

### Revisar `tools.exec.security` antes de assumir permissões amplas (09/04/2026)
Existe histórico de `tools.exec.security = full`. Isso precisa ser confirmado no estado atual antes de ser tratado como desejável.

### Upgrade do OpenClaw deve seguir ritual de backup e validação (14/04/2026)
Quando Marcelo pedir upgrade/update do OpenClaw, a sequência padrão deve ser: validar Git no workspace, fazer backup local e push para o GitHub antes da atualização, executar `npm install -g openclaw@latest` e, se houver `EACCES`, orientar o uso de `sudo`, reiniciar o gateway, validar com `openclaw gateway status`, `openclaw status` e confirmar reachability real com `openclaw gateway probe` antes de considerar encerrado.

### Troca de modelo exige reindexação, warm-up e validação em camadas (15/05/2026)
Após troca de modelo, perda de continuidade pode vir de desalinhamento entre índice semântico, memória recente, boot de contexto e estilo de retrieval do novo modelo. O ritual recomendado é: reindexar com `openclaw memory index --force`, aquecer a sessão com contexto real, validar arquivos de boot, confirmar modelo em status e registrar decisões antes de compactação.
