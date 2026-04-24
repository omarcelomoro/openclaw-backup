# Workflow — Conteúdo em Batch (20-30/Semana)

**Data:** 2026-04-22  
**Objetivo:** Produzir 20-30 conteúdos por semana para 3-4 canais sem perder qualidade

---

## Visão Geral do Fluxo

```
SEGUNDA (Pesquisa)
    ↓ 5 temas + 15 ideias
TERÇA-QUARTA (Redação)
    ↓ 15-21 textos prontos
QUINTA (Design)
    ↓ 15-20 imagens prontas
SEXTA (Upload & Schedule)
    ↓ Conteúdo distribuído + automações
```

**Tempo Total:** 10-14h/semana (você coordena, tools fazem trabalho)

---

## SEGUNDA — PESQUISA (2-3h)

### Step 1: Trending Topics (30 min)
Use skill: `competitive-analysis-leevre` + web search

**Busque:**
- Google Trends: "consórcio", "seguro", "financiamento"
- LinkedIn trending: palavras-chave do seu setor
- Reddit/Quora: Perguntas que as pessoas fazem
- News: Notícias relevantes (taxa de juros, mercado imobiliário, etc)

**Output:**
```
TRENDING TOPICS (Semana de 2026-04-22)
1. "Consórcio vs Empréstimo" — 8.5k buscas/mês
2. "Seguro de vida para PJ" — 4.2k buscas/mês
3. "Renovação de seguro em 2026" — 3.1k buscas/mês
4. "Alavancagem patrimonial imóvel" — 2.8k buscas/mês
5. "Consórcio para negócio" — 2.1k buscas/mês
```

### Step 2: Competitive Intelligence (1h)
Use skill: `competitive-analysis-leevre`

**Analise:**
- O que 3 concorrentes estão postando?
- Qual tipo de conteúdo deles gera mais engajamento?
- Qual gap existe (eles não cobrem)?

**Output:**
```
COMPETITOR CONTENT GAPS

Concorrente A:
- Postam muito sobre "velocidade de aprovação"
- Pouco sobre "renovação"
- Zero sobre "cross-sell"

GAP LEEVRE: Você pode dominar "renovação" + "cross-sell"
```

### Step 3: Ideation (1h)
Brainstorm 15-20 ideias baseado em trending + gaps

**Template:**

```
SEMANA: 2026-04-22 a 2026-04-28
TEMAS PRIORITÁRIOS: 5

Tema 1: "Consórcio vs Empréstimo"
  Angle 1: Juros — consórcio 0%, empréstimo 12%
  Angle 2: Prazos — consórcio 2-3 meses, empréstimo 24h
  Angle 3: Risco — consórcio seguro, empréstimo variável
  Variações: Instagram carousel, LinkedIn thread, Email sequence

Tema 2: "Seguro de Vida para PJ"
  Angle 1: Proteção da família
  Angle 2: Dedutibilidade fiscal
  Angle 3: Comparação preço x cobertura
  Variações: Instagram stories, LinkedIn post, Email

Tema 3: "Renovação de Seguro"
  Angle 1: Não deixe vencer (alerta)
  Angle 2: Oportunidade de renegociar
  Angle 3: Novos produtos desde última renovação
  Variações: Email reminder, WhatsApp para clientes, LinkedIn

... x 5 temas
```

---

## TERÇA-QUARTA — REDAÇÃO (4-5h)

### Step 1: Estrutura de Conteúdo por Canal

**Template Universal:**

```
TEMA: [Tema Escolhido]
ANGLE: [Ângulo Específico]
TARGET: [Quem lê: cliente novo / cliente ativo / ambos]

═══════════════════════════════════════════════════════

VERSÃO 1 — INSTAGRAM CAROUSEL (5 slides)

Slide 1 (Hook):
[Pergunta provocadora / Estatística chocante]
CTA: "Swipe →"

Slide 2-4 (Educação):
[Desenvolvimento da ideia]

Slide 5 (Conversão):
"Quer saber mais?"
[Link bio / CTA clara]

═══════════════════════════════════════════════════════

VERSÃO 2 — LINKEDIN POST

[Abertura em 2 linhas que prende]

[Story / Problema em 3-4 linhas]

[Solução / Insight em 2-3 linhas]

[CTA específica — comentar / reagir / marcar]

═══════════════════════════════════════════════════════

VERSÃO 3 — EMAIL (Newsletter / Follow-up)

Assunto: [Clear, sem clickbait]

Abertura: [Porque esse assunto importa agora]

Corpo: [Problema → Solução → Call-to-action]

CTA: [Link ou telefone — UMA coisa só]

═════════════════════════════════════════════════════════
```

### Step 2: Batch Writing (3-4h)

Escreva 5-7 temas completos (3 versões cada = 15-21 textos)

**Ferramenta:** Use skill `copy-comercial-leevre` para cada um

**Processo:**
1. Tema 1 → Instagram + LinkedIn + Email (30 min)
2. Tema 2 → Instagram + LinkedIn + Email (30 min)
3. ... x 5-7 temas

**Output:** Documento com 15-21 textos prontos

---

## QUINTA — DESIGN (2-3h)

### Step 1: Gerar Imagens (1h)

Use: `image_generate` (DALL-E) ou Canva templates

**Prompt Template:**

```
Para Instagram (dimensão 1080x1350):
"Infográfico moderno sobre [tema], cores azul/branco,
estilo corporativo mas approachable, português do Brasil,
sem texto — só visual que complementa o post"

Para LinkedIn (dimensão 1200x628):
"Header para post sobre [tema], cores corporativas,
design clean, sans-serif, altura 628px"
```

**Processo:**
1. Tema 1 → Gerar 3 variações (escolher melhor)
2. Tema 2 → Gerar 3 variações
3. ... x 5-7 temas

**Output:** 15-20 imagens prontas

### Step 2: Revisar & Ajustar (1-2h)

- ☑ Imagem representa o conteúdo?
- ☑ Cores alinhadas com marca?
- ☑ Legível em mobile?
- ☑ CTA claro?

---

## SEXTA — UPLOAD & SCHEDULE (1-2h)

### Step 1: Setup Ferramentas (1ª vez só)

**Instagram:**
- Use: Buffer, Later, ou Meta Business Suite
- Schedule: Posts 2-3x/semana (Terça, Quinta, Sábado às 18h)

**LinkedIn:**
- Schedule: Posts 2x/semana (Terça 8h, Quinta 8h)

**Email:**
- Use: Brevo, Mailchimp, ou Klaviyo
- Schedule: Newsletter Terça 19h
- Automations: Trigger-based (lead magnet, cross-sell, etc)

**WhatsApp:**
- Use: Wapi, Twilio, ou Zapier
- Automations: Message quando lead qualificado

### Step 2: Upload Conteúdo (30-45 min)

1. **Instagram:**
   - Upload carousel + 2-3 posts
   - Schedule para dias próximos
   - Escrever captions (copiar do documento)

2. **LinkedIn:**
   - Upload 2 posts
   - Schedule para segunda semana

3. **Email:**
   - Criar uma newsletter (compile os 5-7 temas)
   - Schedule para terça
   - Ativar automations

4. **WhatsApp:**
   - Criar templates para cross-sell
   - Conectar triggers (quando lead entra em estágio X)

### Step 3: Confirmar & Track (15 min)

- ☑ Posts agendados corretamente?
- ☑ Horários estão bons?
- ☑ Links não estão quebrados?
- ☑ UTMs estão corretos (rastreamento)?

---

## DOMINGO (OPCIONAL) — ANÁLISE & OTIMIZAÇÃO (1h)

Analise semana anterior:

```
ANALYTICS DOMINGO
Semana: 2026-04-15 a 2026-04-21

INSTAGRAM:
- Impressões: [número]
- Engajamento médio: [%]
- Melhor post: [qual tema]
- Pior post: [qual tema]

LINKEDIN:
- Impressões: [número]
- Engagement rate: [%]
- Cliques: [número]

EMAIL:
- Aberta rate: [%]
- Click rate: [%]
- Conversão: [número de clientes]

LEARNINGS:
✅ "Consórcio vs Empréstimo" funciona bem
❌ "Novidades do setor" gera pouco engagement
→ Semana que vem: Mais de [tema que funciona]
```

---

## TEMPLATES PRONTOS (Use Esses)

### Instagram Carousel — Consórcio vs Empréstimo

```
SLIDE 1:
"CONSÓRCIO vs EMPRÉSTIMO
O que ninguém te conta"
[Visual: VS em letras grandes]

SLIDE 2:
"Empréstimo: você paga JUROS todo mês
Consórcio: você paga TAXA — e ganha prêmio"
[Visual: Gráfico de juros explodindo vs taxa fixa]

SLIDE 3:
"Empréstimo: 30 anos devendo
Consórcio: X anos poupando com outros"
[Visual: Pessoa em pé vs grupo caminhando]

SLIDE 4:
"A matemática é simples:
Empréstimo 300k a 12% ao ano = R$36k SÓ em juros
Consórcio 300k = taxa única"
[Visual: Números]

SLIDE 5:
"Engenharia patrimonial, não dívida.
Quer conversar?"
[CTA: Link no bio]
```

### LinkedIn — Seguro de Vida PJ

```
Conheci PJ que confunde "seguro de vida" com "seguro saúde".
É como confundir carro com bicicleta.

Ambos te levam a um lugar. A experiência é diferente.

SEGURO SAÚDE:
- Você paga mensalidade
- Usa para consulta/exame/internação
- Se saudável, "gasta" menos

SEGURO DE VIDA:
- Você paga prêmio mensal
- Se algo acontecer, família recebe [valor]
- Dedutível fiscal (você abate do IR)
- Tranquilidade enquanto trabalha

PJ que pensa — proteção de família + benefício fiscal.
PJ que não pensa — risco de deixar dependentes expostos.

Se você é PJ e nunca pensou nísso, deixa mensagem nos comentários.
Tenho um material que pode te ajudar.
```

### Email — Renovação de Seguro

```
Assunto: Seu seguro vence em [data] — 3 coisas que mudaram

Oi [Nome],

Seu seguro vence em [data].

Antes de renovar automaticamente, 3 coisas que você deve saber:

1. COBERTURA — Mudou sua situação? Dependentes? Patrimônio?
   Pode ser que o seguro antigo não cubra tudo.

2. PREÇO — Desde sua última renovação, novas seguradoras entram no mercado.
   Você pode estar pagando 20-30% a mais do que deveria.

3. NOVOS PRODUTOS — Existem produtos que não existiam há 2 anos.
   Ex: proteção contra inflação, renda vitalícia, etc.

Se você quer conversar antes de renovar automaticamente,
posso ajudar em 15 minutos.

[Botão: Agendar conversa]

Abraço,
[Seu nome]
Leevre
```

---

## CHECKLIST SEMANAL

```
SEGUNDA:
☐ Pesquisei trending topics (Google Trends + Reddit)
☐ Analisei 3 concorrentes
☐ Criei 15-20 ideias de conteúdo
☐ Documente em: [arquivo]

TERÇA-QUARTA:
☐ Escrevi 5-7 temas (3 versões cada)
☐ Revisei typos e CTA
☐ Salvei em: [arquivo]

QUINTA:
☐ Gerei imagens para cada tema
☐ Revisei alinhamento com marca
☐ Salvei em: [pasta]

SEXTA:
☐ Uploadei no Instagram (schedule)
☐ Uploadei no LinkedIn (schedule)
☐ Criei newsletter + automations (email)
☐ Configurei WhatsApp automations
☐ Confirmei rastreamento (UTMs)

DOMINGO (Opcional):
☐ Analisei performance da semana anterior
☐ Documentei learnings
☐ Identifiquei 1-2 temas que devo repetir
```

---

## MÉTRICAS DE SUCESSO

**Após 4 Semanas:**
- ☑ 80-120 conteúdos publicados
- ☑ 20% aumento em followers
- ☑ 3-5% taxa de engajamento
- ☑ 2-3 leads via conteúdo
- ☑ Email automations rodando (40%+ open rate)

**Após 8 Semanas:**
- ☑ +30% leads qualificados
- ☑ +20% cross-sell conversão
- ☑ 5-8% taxa de engajamento
- ☑ Sistema praticamente automático

---

## FERRAMENTAS RECOMENDADAS

| Função | Ferramenta | Custo | Notes |
|--------|-----------|-------|-------|
| Design | DALL-E / Canva | $10-20/mês | Use DALL-E pra geração rápida |
| Instagram Schedule | Buffer | Grátis (5 posts) | Ou Later ($25/mês) |
| Email | Brevo | Grátis (300/dia) | Ótima base |
| Analytics | Google Analytics + Sheets | Grátis | Suficiente |
| UTM Builder | UTM.io | Grátis | Quick builder |

**Total:** $30-50/mês

---

## PRÓXIMO PASSO

Responda:

1. **Quer começar SEGUNDA ou na próxima semana?**
2. **Qual canal priorizar primeiro? (Instagram / LinkedIn / Email)**
3. **Quer que eu faça TESTE 1 batch de conteúdo agora?**

Com isso, vocês saem da semana que vem com sistema de verdade rodando.
