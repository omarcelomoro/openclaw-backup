# Decisões Permanentes

> Decisões que a Livri deve respeitar SEMPRE.
> Formato: O que decidiu + Por que + Data

---

### Credenciais no .env do servidor (22/03/2026)
Toda credencial (API keys, senhas, tokens) fica em `/root/.openclaw/.env` no servidor (chmod 600). Nunca commitada no GitHub, nunca em markdown, nunca em código hardcoded. O `.gitignore` protege o `.env`.

### SSH key-only no VPS (22/03/2026)
Acesso ao VPS (`187.77.247.207`) é exclusivamente por chave SSH. Password auth desativado. Sem exceções.

### Gateway via SSH tunnel (22/03/2026)
O gateway fica em loopback (`bind: loopback`). Acesso externo apenas via tunnel SSH: `ssh -L 18789:127.0.0.1:18789 root@187.77.247.207 -N`. Motivo: segurança — não expor o gateway diretamente na internet.

### Backup diário no GitHub (22/03/2026)
Cron job às 3h AM faz push do workspace pro repositório privado `omarcelomoro/openclaw-backup`. Arquivos sensíveis (.env, .bak) estão no `.gitignore` e nunca são commitados.

### Horário protegido — sem notificações (22/03/2026)
Não enviar notificações ou mensagens proativas entre 17h30 e 09h30 (horário de Brasília), nem durante o almoço (~12h30-13h30). Respeitar os limites do dia de trabalho do Marcelo.

### Ações externas requerem confirmação (22/03/2026)
Qualquer ação que sai da máquina — envio de email, post em rede social, mensagem pra terceiros — exige confirmação explícita do Marcelo antes de executar. Sem exceções.

### Senhas não vão para arquivos commitados (24/03/2026)
Senhas são salvas no `.env` do servidor, nunca em IDENTITY.md, MEMORY.md ou qualquer arquivo que vai pro GitHub. Credenciais de email, APIs e sistemas ficam exclusivamente no `.env`.

### Conteúdo externo sempre adaptado (23/03/2026)
Roteiros e conteúdos baseados em material de terceiros (Batalha, Wellington WK, etc.) são sempre reescritos com contexto, números e exemplos próprios. Nunca copiar diretamente — adaptar pra voz do Marcelo e evitar plágio.

### Otimização de tokens no startup (26/03/2026)
Carregar apenas SOUL.md, USER.md, IDENTITY.md e memory/YYYY-MM-DD.md no início de cada sessão. Demais arquivos (DECISIONS, LESSONS, PENDING, PEOPLE, PROJECTS) são carregados sob demanda via `memory_search()`. Reduz contexto de ~50KB para ~8KB por sessão (~80% de economia).

### GOG CLI como interface Google Workspace (26/03/2026)
`gog` é a ferramenta oficial pra acessar Gmail, Calendar e Drive. Duas contas autenticadas: `atendimento@leevrecorretora.com.br` (Livri) e `marcelo@leevrecorretora.com.br` (Marcelo). Detalhes em `memory/integrations/gog.md`. Variáveis no `.env`.

### Arquitetura de memória em subpastas (26/03/2026)
Memória organizada em `memory/context/`, `memory/projects/`, `memory/content/`, `memory/integrations/`, `memory/sessions/`. Um arquivo por projeto em `projects/`. Busca semântica via `memory_search()`. Carregar apenas `sessions/` no startup — demais arquivos sob demanda.

---

*Atualizado: 26/03/2026*
