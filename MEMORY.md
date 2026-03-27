# MEMORY.md — Livri 🐝

> Índice geral — sempre carregado na sessão principal.
> Conteúdo detalhado vive nos topic files. Busca via `memory_search()`.

## 📂 Estrutura

```
memory/
├── MEMORY.md                    ← índice geral (sempre carregado)
│
├── context/                     ← tudo que não muda rápido
│   ├── decisions.md             ← regras permanentes do agente
│   ├── lessons.md               ← erros e aprendizados
│   ├── people.md                ← equipe, fornecedores, parceiros
│   ├── pending.md               ← pendências aguardando decisão
│   └── business-context.md      ← contexto dos negócios
│
├── projects/                    ← um arquivo por projeto ativo
│   ├── infraestrutura-livri.md
│   ├── conteudo-digital.md
│   ├── estruturacao-leevre.md
│   └── rebranding-leevre.md
│
├── content/                     ← específico para produção de conteúdo
│   ├── voice/
│   │   ├── instagram.md         ← guia de tom de voz por plataforma
│   │   └── youtube.md
│   ├── ideas.md                 ← ideias de conteúdo
│   └── drafts/                  ← rascunhos de posts, scripts
│
├── integrations/                ← mapa de ferramentas e acessos
│   ├── telegram-map.md          ← IDs dos grupos e tópicos
│   └── credentials-map.md       ← onde cada credencial fica
│
└── sessions/                    ← diário (um arquivo por dia/tema)
    └── 2026-03-26.md
```

## 🔄 Ciclo de Memória

```
Sessão → sessions/YYYY-MM-DD.md (raw)
 ↓ consolidação periódica
 context/ + projects/ + content/ (curado)
 ↓ índice atualizado
 MEMORY.md
```

## 📸 Estado Atual (26/03/2026)

### Projetos Ativos
- **Infraestrutura Livri** → `memory/projects/infraestrutura-livri.md`
- **Conteúdo Digital** → `memory/projects/conteudo-digital.md`
- **Estruturação Leevre** → `memory/projects/estruturacao-leevre.md`
- **Rebranding Leevre** → `memory/projects/rebranding-leevre.md`

### Pendências principais
- Email `livri@leevrecorretora.com.br` — aguarda decisão Google Workspace
- Bitwarden self-hosted — aguarda confirmação
- CRM — não definido ainda
- Agger API — verificar documentação

## 🧠 Como usar

- `memory_search("termo")` — busca semântica em todos os arquivos
- `memory_get("memory/context/decisions.md")` — lê o trecho relevante
- Novas sessões → `memory/sessions/YYYY-MM-DD.md`
- Projeto novo → `memory/projects/nome.md`
- Ideia de conteúdo → `memory/content/ideas.md`
- Draft de post/script → `memory/content/drafts/`

## ⚡ Regras de Memória

1. Notas diárias: `memory/sessions/YYYY-MM-DD.md` a cada sessão relevante
2. Projetos: um arquivo separado por projeto em `memory/projects/`
3. **INVIOLÁVEL:** antes de compactar → extrair lições, decisões e pendências
4. Carregar no startup: SOUL.md, USER.md, IDENTITY.md, sessions/ (hoje+ontem)
5. Demais arquivos: buscar sob demanda via `memory_search()`

## Preferência: Compactação Automática
- Quando o contexto atingir **95%** da janela, executar `/compact`
- Registrado em: 25/03/2026
