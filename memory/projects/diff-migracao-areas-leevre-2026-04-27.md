# Diff / Plano de Migração Concreto — Leevre atual → `areas/`
Data: 2026-04-27
Status: proposta de arquitetura — **não executar ainda**

## Objetivo
Traduzir a estrutura atual da Leevre para uma organização explícita por áreas:
- `areas/marketing/`
- `areas/vendas/`
- `areas/operacoes/`
- `areas/atendimento/`
- `areas/produto/`

Sem ruptura, sem apagar origem agora e sem tratar o template como rolo compressor.

---

## 1. Princípio de migração

### Regra-mãe
- o workspace atual continua sendo a base
- `memory/`, `skills/`, `rotinas/` e `state/` continuam existindo
- `areas/` vira a nova camada canônica de leitura operacional
- no início, migrar por **duplicação orientada + consolidação**, não por arrasto bruto

### O que isso evita
- quebrar links mentais e referências existentes
- perder contexto vivo no meio da reorganização
- gerar estrutura bonita, mas vazia

---

## 2. Estrutura-alvo mínima

```text
areas/
├── marketing/
│   ├── contexto/
│   ├── planos/
│   ├── conteudo/
│   └── referencias/
├── vendas/
│   ├── contexto/
│   ├── pipeline/
│   ├── playbooks/
│   └── follow-up/
├── operacoes/
│   ├── contexto/
│   ├── comissoes/
│   ├── conciliacao/
│   ├── renovacoes/
│   └── fiscal/
├── atendimento/
│   ├── contexto/
│   ├── faq/
│   ├── handoff/
│   └── padroes/
└── produto/
    ├── contexto/
    ├── melhorias/
    ├── onboarding/
    └── automacoes/
```

---

## 3. Diff proposto por arquivo atual → destino sugerido

## 3.1 Arquivos de `empresa/`

### Marketing
- `empresa/escala-digital-leevre.md`
  → `areas/marketing/planos/escala-digital-leevre.md`
- `empresa/visao-e-metas.md`
  → desdobrar em:
  - `areas/marketing/contexto/metas-marketing.md`
  - `areas/vendas/contexto/metas-vendas.md`
  - `areas/operacoes/contexto/metas-operacoes.md`
  - manter original em `empresa/` por enquanto como visão executiva transversal

### Vendas
- `empresa/metricas-principais.md`
  → desdobrar em:
  - `areas/vendas/contexto/metricas-vendas.md`
  - `areas/marketing/contexto/metricas-marketing.md`
  - `areas/operacoes/contexto/metricas-operacoes.md`
  - manter original enquanto não houver versão consolidada por área
- `empresa/pessoas-chave.md`
  → manter em `empresa/` como transversal
  → criar depois referências derivadas em:
  - `areas/vendas/contexto/responsaveis-comerciais.md`
  - `areas/operacoes/contexto/responsaveis-operacionais.md`

### Operações / transversal
- `empresa/padrao-visual-relatorios-html-leevre.md`
  → `areas/operacoes/contexto/padrao-visual-relatorios-html-leevre.md`
- `empresa/padrao-visual-relatorios-pdf-leevre.md`
  → `areas/operacoes/contexto/padrao-visual-relatorios-pdf-leevre.md`
- `empresa/decisoes-estrategicas.md`
  → manter em `empresa/` como transversal
  → no futuro, extrair decisões operacionais específicas para cada `areas/*/contexto/decisoes.md`
- `empresa/protocolo-vetting-skills-e-referencias-leevre.md`
  → manter em `empresa/` (governança transversal)
- `empresa/mapa-do-cerebro.md`
  → manter em `empresa/` até a nova estrutura existir de fato
- `empresa/README.md`
  → manter em `empresa/`

---

## 3.2 Arquivos de `rotinas/`

### Marketing
- `rotinas/teste-1-conteudo-consorcio-carta-contemplada.md`
  → `areas/marketing/conteudo/teste-1-conteudo-consorcio-carta-contemplada.md`
- `rotinas/workflow-conteudo-batch-20-30-leevre.md`
  → `areas/marketing/planos/workflow-conteudo-batch-20-30-leevre.md`
- `rotinas/workflow-conteudo-opensquad-leevre.md`
  → `areas/marketing/planos/workflow-conteudo-opensquad-leevre.md`
- `rotinas/setup-nano-banana-pro-leevre.md`
  → `areas/marketing/referencias/setup-nano-banana-pro-leevre.md`
- `rotinas/fluxo-vendas-pesquisa-prep-leevre.md`
  → pode ficar melhor em vendas, não marketing

### Vendas
- `rotinas/fluxo-vendas-pesquisa-prep-leevre.md`
  → `areas/vendas/playbooks/fluxo-vendas-pesquisa-prep-leevre.md`
- `rotinas/rotina-semanal-comercial.md`
  → `areas/vendas/playbooks/rotina-semanal-comercial.md`
- `rotinas/rotina-operacional-revisao-pendencias-followup-leevre.md`
  → `areas/vendas/follow-up/rotina-operacional-revisao-pendencias-followup-leevre.md`
- `rotinas/checklist-execucao-hubspot-consorcio-leevre.md`
  → `areas/vendas/pipeline/checklist-execucao-hubspot-consorcio-leevre.md`
- `rotinas/checklist-implementacao-pipeline-consorcio-hubspot-leevre.md`
  → `areas/vendas/pipeline/checklist-implementacao-pipeline-consorcio-hubspot-leevre.md`
- `rotinas/estrutura-final-pipeline-consorcio-hubspot-leevre.md`
  → `areas/vendas/pipeline/estrutura-final-pipeline-consorcio-hubspot-leevre.md`
- `rotinas/folha-de-cola-hubspot-consorcio-leevre.md`
  → `areas/vendas/pipeline/folha-de-cola-hubspot-consorcio-leevre.md`
- `rotinas/mapa-tecnico-campos-pipeline-consorcio-hubspot-leevre.md`
  → `areas/vendas/pipeline/mapa-tecnico-campos-pipeline-consorcio-hubspot-leevre.md`
- `rotinas/passo-a-passo-cliques-hubspot-consorcio-leevre.md`
  → `areas/vendas/pipeline/passo-a-passo-cliques-hubspot-consorcio-leevre.md`
- `rotinas/plano-execucao-hubspot-api-consorcio-leevre.md`
  → `areas/vendas/pipeline/plano-execucao-hubspot-api-consorcio-leevre.md`
- `rotinas/plano-implantacao-real-hubspot-consorcio-leevre.md`
  → `areas/vendas/pipeline/plano-implantacao-real-hubspot-consorcio-leevre.md`
- `rotinas/roteiro-coleta-hubspot-api-auditoria-leevre.md`
  → `areas/vendas/pipeline/roteiro-coleta-hubspot-api-auditoria-leevre.md`
- `rotinas/auditoria-hubspot-real-2026-04-24.md`
  → `areas/vendas/pipeline/auditoria-hubspot-real-2026-04-24.md`
- `rotinas/matriz-auditoria-hubspot-real-vs-ideal-leevre.md`
  → `areas/vendas/pipeline/matriz-auditoria-hubspot-real-vs-ideal-leevre.md`

### Operações
- `rotinas/checklist-fechamento-mensal.md`
  → `areas/operacoes/comissoes/checklist-fechamento-mensal.md`
- `rotinas/fechamento-comissao.md`
  → `areas/operacoes/comissoes/fechamento-comissao.md`
- `rotinas/geracao-relatorios-pdf-leevre.md`
  → `areas/operacoes/contexto/geracao-relatorios-pdf-leevre.md`
- `rotinas/relatorios-pdf-pacote-inicial.md`
  → `areas/operacoes/contexto/relatorios-pdf-pacote-inicial.md`
- `rotinas/resumo-semanal-metricas.md`
  → `areas/operacoes/contexto/resumo-semanal-metricas.md`
- `rotinas/revisao-pendencias-livri.md`
  → `areas/operacoes/contexto/revisao-pendencias-livri.md`
- `rotinas/plano-o-que-falta-leevre-pos-transcricao.md`
  → `areas/operacoes/contexto/plano-o-que-falta-leevre-pos-transcricao.md`
- `rotinas/comandos-iniciais-modo-a-notas.md`
  → `areas/operacoes/fiscal/comandos-iniciais-modo-a-notas.md`
- `rotinas/modo-a-notas-fiscais-implantacao.md`
  → `areas/operacoes/fiscal/modo-a-notas-fiscais-implantacao.md`
- `rotinas/checklist-execucao-lobsterlink-tokio-marine.md`
  → `areas/operacoes/renovacoes/checklist-execucao-lobsterlink-tokio-marine.md`
- `rotinas/instalacao-tecnica-lobsterlink-piloto-tokio-marine.md`
  → `areas/operacoes/renovacoes/instalacao-tecnica-lobsterlink-piloto-tokio-marine.md`
- `rotinas/piloto-lobsterlink-tokio-marine.md`
  → `areas/operacoes/renovacoes/piloto-lobsterlink-tokio-marine.md`
- `rotinas/update-backup-rollback-openclaw-leevre.md`
  → manter fora de `areas/` em `rotinas/` ou mover para `infra/` futura; isso não é operação de negócio, é infraestrutura

### Atendimento
- hoje não há bloco maduro já pronto em `rotinas/`
- criar do zero a partir de materiais futuros de FAQ, triagem e handoff

### Produto
- hoje não há bloco maduro já pronto em `rotinas/`
- candidatos embrionários:
  - `rotinas/plano-o-que-falta-leevre-pos-transcricao.md`
  - partes de automação espalhadas em `state/` e `skills/`

---

## 3.3 Arquivos de `memory/projects/`

### Marketing
- `memory/projects/conteudo-digital.md`
  → `areas/marketing/contexto/conteudo-digital.md`
- `memory/projects/leevre-marketing.md`
  → `areas/marketing/contexto/leevre-marketing.md`
- `memory/projects/rebranding-leevre.md`
  → `areas/marketing/planos/rebranding-leevre.md`

### Vendas
- `memory/projects/funil-digital.md`
  → `areas/vendas/contexto/funil-digital.md`
- `memory/projects/hubspot-seguros.md`
  → `areas/vendas/pipeline/hubspot-seguros.md`

### Operações
- `memory/projects/leevre-operacao.md`
  → `areas/operacoes/contexto/leevre-operacao.md`
- `memory/projects/estruturacao-leevre.md`
  → dividir entre `operacoes` e `produto`; manter original até maturar recorte

### Produto
- `memory/projects/infraestrutura-livri.md`
  → `areas/produto/melhorias/infraestrutura-livri.md` **ou** manter em trilha de infra transversal; não jogar em produto comercial sem critério

### Transversal / estratégia
- `memory/projects/planejamento-estrategico-2026.md`
  → manter em `memory/projects/` por enquanto
- `memory/projects/prd-segundo-cerebro-leevre-2026-04-26.md`
  → manter em `memory/projects/`
- `memory/projects/mapa-adaptacao-cerebro-empresa-leevre-2026-04-26.md`
  → manter em `memory/projects/`
- `memory/projects/second-brain-implementacao-log-2026-04-26.md`
  → manter em `memory/projects/`

---

## 3.4 Arquivos de `state/`

## Regra
`state/` não vira canônico por padrão.
Só sobe para `areas/` o que já for reaproveitável, explicável e recorrente.

### Marketing — candidatos a promover
- `state/roteiro-podcast-200k-500k.md`
  → `areas/marketing/conteudo/roteiro-podcast-200k-500k.md`
- `state/template-relatorio-leads-esfriando-leevre.html`
  → `areas/marketing/referencias/template-relatorio-leads-esfriando-leevre.html` **se** o uso for comercial/marketing

### Vendas — candidatos a promover
- `state/template-relatorio-pipeline-leevre.html`
  → `areas/vendas/referencias/template-relatorio-pipeline-leevre.html`
- `state/relatorio-pipeline-leevre-exemplo.pdf`
  → manter em `state/` como exemplo, não canônico
- `state/checklist-go-no-go-lobsterlink-tokio-marine.md`
  → se foco for decisão comercial/implantação, pode ir para `areas/vendas/playbooks/` ou `areas/operacoes/renovacoes/`; hoje pende mais para operações

### Operações — candidatos a promover
- `state/leevre-comissao-conciliacao-workflow.md`
  → `areas/operacoes/conciliacao/leevre-comissao-conciliacao-workflow.md`
- `state/operacao-comissoes-template.csv`
  → `areas/operacoes/comissoes/operacao-comissoes-template.csv`
- `state/gerar_pdf_relatorio.py`
  → `areas/operacoes/contexto/gerar_pdf_relatorio.py` **ou** manter em `state/` enquanto não houver pasta técnica melhor
- `state/emitir_nf_virei_contador.py`
  → `areas/operacoes/fiscal/emitir_nf_virei_contador.py`
- `state/teste-skill-notas-fiscais-leevre.md`
  → `areas/operacoes/fiscal/teste-skill-notas-fiscais-leevre.md`
- PDFs e bases em `state/nf-drive/` e `state/nf-teste/`
  → **não migrar para `areas/` agora**; manter em `state/` como material operacional bruto/referência de execução

### Produto — candidatos a promover
- `state/leevre-implementation-roadmap.md`
  → `areas/produto/melhorias/leevre-implementation-roadmap.md`
- `state/leevre-proximos-blocos.md`
  → `areas/produto/melhorias/leevre-proximos-blocos.md`
- `state/lacunas-criticas-para-escala-digital-leevre.md`
  → `areas/produto/contexto/lacunas-criticas-para-escala-digital-leevre.md`

### Manter em `state/` sem migrar agora
- auditorias técnicas do OpenClaw/tokenjuice/repos
- backups e tmp-merge-backup
- credenciais template `.env`
- PDFs exemplo e insumos brutos

---

## 4. Skills por área — leitura operacional

## Marketing
- `skills/conteudo-comercial-leevre/`
- `skills/copy-comercial-leevre/`
- `skills/analise-concorrentes-conteudo/`
- `skills/competitive-analysis-leevre/`
- `skills/estrategia-posicionamento-leevre/`
- `skills/voz-da-marca-leevre/`
- `skills/opensquad-conteudo-leevre/`

## Vendas
- `skills/follow-up-comercial-leevre/`
- `skills/followup-consorcio/`
- `skills/pipeline-consorcio-hubspot-leevre/`
- `skills/call-prep-leevre/`
- `skills/account-research-leevre/`
- `skills/auditoria-hubspot-leevre/`

## Operações
- `skills/conciliacao-comissao-leevre/`
- `skills/gestao-renovacoes-seguro/`
- `skills/emitir-notas-fiscais-leevre/`
- `skills/notas-fiscais-seguradoras-leevre/`
- `skills/relatorio-comissao-conciliacao-pdf-leevre/`
- `skills/consolidacao-metricas-semanais/`

## Atendimento
- ainda sem skill nuclear madura
- lacuna real a preencher depois

## Produto
- ainda sem skill nuclear própria da área
- hoje a inteligência de produto está dispersa entre operação, marketing e infra

---

## 5. Ordem concreta de implementação

### Fase 1 — criar leitura por área sem mover arquivo físico
1. criar `areas/marketing`, `areas/vendas`, `areas/operacoes`, `areas/atendimento`, `areas/produto`
2. criar um `README.md` ou `contexto/index.md` em cada área
3. preencher esses índices com links para os arquivos já existentes

### Fase 2 — promover os blocos maduros
4. migrar primeiro os arquivos mais óbvios de marketing, vendas e operações
5. deixar `atendimento` e `produto` como esqueletos conscientes, sem fingir maturidade

### Fase 3 — consolidar canônico
6. transformar `areas/*` em ponto principal de consulta operacional
7. manter `empresa/` como camada institucional transversal
8. manter `memory/projects/` para trabalho em andamento e material histórico

### Fase 4 — limpeza controlada
9. só depois decidir o que vira arquivo legado, stub, redirect ou arquivo arquivado
10. não arquivar nada bruto de `state/` até saber o que ainda é usado

---

## 6. Leitura honesta por área

### Marketing
Já existe material suficiente para virar área real agora.

### Vendas
Já existe material suficiente para virar área real agora.

### Operações
Já existe material suficiente para virar área real agora.

### Atendimento
Ainda é lacuna estrutural, não área madura.
Criar a pasta faz sentido. Fingir que ela já existe de verdade, não.

### Produto
Ainda é mais “melhoria operacional e sistema” do que produto estruturado.
Criar a pasta faz sentido como direção. Encher a pasta artificialmente, não.

---

## 7. Veredito
O próximo passo certo não é sair arrastando arquivo.
O próximo passo certo é:
1. criar `areas/`
2. consolidar índices por área
3. promover primeiro marketing, vendas e operações
4. usar atendimento e produto como áreas em construção consciente

Esse é o caminho mais limpo para a Leevre ganhar arquitetura sem perder memória viva.
