---
name: account-research-leevre
description: >
  Pesquisa de prospect antes de call comercial. Coleta info de pessoa/empresa via web,
  enriquece com dados públicos e histórico CRM (quando conectado). Gera "perfect opener"
  e talking points baseados em contexto real.
kind: prompt
tags: #vendas #prospecting #pesquisa #call-prep #leevre #consorcio #seguros
triggers: pesquise cliente, quem é esse prospect, background dessa pessoa, histórico dele, before call, prep de call, research de prospect, get intel on
---

# Account Research — Leevre

## Objetivo
Chegar em uma call comercial sabendo quem é a pessoa, qual é o contexto dela,
qual é o histórico de relacionamento com Leevre (se houver) e qual é o ângulo
de abordagem melhor.

---

## Fluxo (3 Fases)

### 1. WEB SEARCH (Sempre Funciona)

**Pesquise:**

```
[Nome da Pessoa]
[Nome da Pessoa] + LinkedIn
[Nome da Pessoa] + [Empresa]
[Empresa Name] + [Setor] (se estamos pesquisando uma empresa)
[Empresa] + financiamento / consórcio / seguro (sinais de interesse)
[Empresa] + news (nos últimos 90 dias)
[Empresa] + funding (se startup)
[Empresa] + hiring (growth signals)
```

**Extraia:**

#### Para Pessoa Física
```
NOME: [Nome]
PROFISSÃO: [Cargo/Título Atual]
EMPRESA: [Empresa Atual]
SETOR: [Setor da Empresa]
TAMANHO EMPRESA: [Pequeno/Médio/Grande]
LINKEDIN: [URL se houver]
BACKGROUND: [Experiência anterior — 2-3 empresas]
TEMPO NO CARGO: [Há quanto tempo nessa posição]
SENIORITY: [Junior/Mid/Senior/C-Level]

SIGNALS:
- Recentemente trocou de job? (NOVO ORÇAMENTO POTENCIAL)
- Promovido? (PODER DE DECISÃO NOVO)
- Saiu de startup? (ESTABILIDADE AGORA)
- Entrou em empresa grande? (ESTRUTURA/ORÇAMENTO)
```

#### Para Empresa (B2B)
```
NOME: [Razão Social]
SETOR: [Setor Principal]
TAMANHO: [Qtd de Funcionários]
FUNDAÇÃO: [Ano]
FUNDING: [Série/Stage se conhecida]
LOCALIZAÇÃO: [Matriz + Filiais]
LEADERSHIP: [CEO/Founder + Background]
RECENTE NEWS: [Expansão/Parceria/Contratação]

GROWTH SIGNALS:
- Contratando? (CRESCIMENTO)
- Novo investimento? (CAPITAL DISPONÍVEL)
- Expansão geográfica? (NOVO ESCRITÓRIO = CUSTO/NECESSIDADE)
- Novos produtos? (INOVAÇÃO)

PAIN SIGNALS:
- Divulgou problemas? (URGÊNCIA POTENCIAL)
- Layoff? (AUSTERIDADE)
- Saída de executivo? (INSTABILIDADE)
```

---

### 2. ENRIQUECIMENTO (Se Conectado)

**Se você tiver integração com tools de enriquecimento (Hunter.io, Clearbit, etc):**

Adicione:
- Email verificado
- Telefone (se público)
- LinkedIn profile completo
- Histórico de jobs
- Stack tecnológico (para empresas)
- Org chart (se disponível)

**Se conectado ao CRM (HubSpot):**

Busque o contact/company:
- Prior relationship? (novo ou foi prospect antes?)
- Oportunidades anteriores? (ganhas? perdidas? por quê?)
- Último contato? (há quanto tempo não falam?)
- Notes de vendedor anterior? (achados úteis?)
- Deal history? (qual era o budget antes?)

---

### 3. SÍNTESE & PERFECT OPENER

**Estruture assim:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ACCOUNT RESEARCH — [Nome do Prospect]
Data: [data]
Call agendada: [quando]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## QUICK TAKE (2-3 Linhas)
[Quem é / por que pode ser interessante / qual é o ângulo]

Exemplo:
"João é CFO de construtora em crescimento (contratar 200 no próximo ano).
Saiu de Itaú há 6 meses (novo orçamento?). Pode ser prospect quente
para financiamento de obra."

---

## PROSPECT PROFILE

| Campo | Detalhes |
|-------|----------|
| **Nome** | [Nome completo] |
| **Título/Cargo** | [ex: CFO, Diretor de Operações] |
| **Empresa** | [Empresa] |
| **Setor** | [ex: Construção, Varejo, Tech] |
| **Tamanho Empresa** | [Qtd pessoas / receita estimada] |
| **Tempo no Cargo** | [ex: 8 meses] |
| **LinkedIn** | [URL] |

---

## BACKGROUND & EXPERIENCE

**Trajetória Profissional:**
- [Empresa 1] — [Período] — [Cargo]
- [Empresa 2] — [Período] — [Cargo]
- [Empresa 3 (atual)] — [Período] — [Cargo]

**Mudança Importante:**
[Se mudou de empresa recentemente, por quê? Busca no LinkedIn.]

**Educação:**
[Onde estudou? Que área? Pode ser talking point]

---

## COMPANY INTEL

| Campo | Info |
|-------|------|
| **Setor** | [Setor] |
| **Funcionários** | [Qtd] |
| **Fundação** | [Ano] |
| **Reputação** | [Em que são conhecidos?] |
| **Financiamento** | [Bootstrapped / Series A / Fundos / Private] |
| **Localização** | [Matriz / Filiais] |

**Recent News (últimos 90 dias):**
- [Notícia 1 + data]
- [Notícia 2 + data]
- [Notícia 3 + data]

**Why It Matters:**
[Como isso pode virar oportunidade pra Leevre?]

---

## HIRING SIGNALS

| Sinal | Interpretação |
|-------|---------------|
| [Contratando? Quantas vagas?] | [Crescimento = novo orçamento?] |
| [Em qual área?] | [Se área financeira, pode precisar de consórcio] |
| [Velocidade de contratação?] | [Agressiva = crescimento rápido] |

---

## PRIOR RELATIONSHIP (Se CRM Conectado)

| Campo | Status |
|-------|--------|
| **Status** | [Novo / Ex-prospect / Cliente / Churned] |
| **Primeiro contato** | [Quando?] |
| **Último contato** | [Quando? Qual context?] |
| **Oportunidades anteriores** | [Quantas? Resultados?] |
| **Por que não virou cliente?** | [Se perdido, qual foi a razão?] |
| **Pessoas envolvidas** | [Quem mais na empresa foi contatado?] |

**Histórico:**
[Resumo do relacionamento — vale a pena re-engajar ou é novo mesmo?]

---

## QUALIFICATION SIGNALS

### ✅ Sinais Positivos
- ☑ [Sinal 1 + evidência]
- ☑ [Sinal 2 + evidência]
- ☑ [Sinal 3 + evidência]

Exemplo:
- ☑ Empresa contratando 50+ (crescimento = orçamento novo)
- ☑ Pessoa saiu de grande empresa (pode ter expertise em decisão)
- ☑ Nunca foi prospect (virgin territory)

### ⚠️ Sinais de Cautela
- ❓ [Preocupação 1 + contexto]
- ❓ [Preocupação 2 + contexto]

Exemplo:
- ❓ Empresa ainda é pequena (budget pode ser limitado)
- ❓ Pessoa é junior (pode não ter poder de decisão)
- ❓ Setor recessivo (austeridade)

### ❓ Unknowns (Pergunte na Call)
- [O que você ainda não sabe?]
- [Qual decisor precisa estar envolvido?]
- [Qual é o budget range?]

---

## PERFECT OPENER

**Primeiro que você fala (30 segundos max):**

Template:
```
"Oi [Nome],

Vi que você virou [Cargo] na [Empresa] há [tempo].
Sou [Seu Nome] da Leevre.

Eu acompanhei [Empresa] crescendo no [setor] e vi que
vocês estão [ação recente: expandindo/contratando/lançando].

Isso me fez pensar em [específico para situação deles].
Temos alguns clientes no [setor] que [resultado real].

Você teria 15 minutos na [dia/semana] para bater um papo rápido?"
```

**Adaptado para Leevre:**

```
Exemplo 1 (Construtora Crescendo):
"Oi João, vi que a Obra Construções está com 5 obras novas esse ano.
Sou Livri da Leevre. A gente trabalha com construtoras que estão escalando
e precisam de capital com disciplina (consórcio).

Você teria 15 min quarta para falar?"

Exemplo 2 (Profissional Liberal):
"Oi Maria, vi que você é dentista em Curitiba e está expandindo consultório.
Sou Livri da Leevre. Tenho vários clientes na área de saúde que usam consórcio
para aquisição de imóvel/equipamento sem comprometer fluxo.

Vale bater um papo?"

Exemplo 3 (Empresa Financeira):
"Oi Paulo, vi que você agora é CFO da TechCorp.
Sou Livri da Leevre. Trabalho com CFOs de empresas em crescimento
que precisam alavancar patrimônio corporativo.

Você teria 20 min sexta?"
```

**Key Rules:**
- Personalizado (mostra que pesquisou)
- Específico (não genérico)
- Benefício claro (por que você liga agora?)
- Curto (respeita tempo dele)
- CTA simples (pergunta direta)

---

## TALKING POINTS (Para Estruturar a Conversa)

**Baseado na research, prepare:**

```
OPENER:
[Perfect opener acima]

FIRST QUESTION:
[Pergunta que mostra interesse genuíno — não venda]
Exemplo: "Como você está vendo o mercado de [setor] agora?"

LISTENING PHASE:
[Deixa ele falar 3-5 min]

MATCHING PHASE:
"A razão que eu liguei é porque [X situação dele] combina muito com [solução Leevre]"

OBJECTION PREP:
[Se for B2C] "E quanto a prazos? Consórcio geralmente leva [X], mas se você..."
[Se for B2B] "E quanto a orçamento? Consórcio custa [X], comparado com empréstimo..."

CLOSE:
"O que você acha? Faz sentido agendar um café virtual pra estruturar isso melhor?"
```

---

## RESEARCH OUTCOMES (Por Tipo de Prospect)

### Se é DECISION MAKER (C-Level/Diretor)
✅ Ótimo — você pode fechar deal com essa pessoa
⚠️ Prepara bem, porque tem só 1 chance
→ Perfect opener deve ser impecável

### Se é INFLUENCER (Manager que influencia, mas não decide)
✅ Bom — pessoa pode abrir porta
⚠️ Você vai precisar chegar ao decision maker depois
→ Pergunta: "Qual é o processo de decisão aqui?"

### Se é GATEKEEPER (Junior que filtra)
❌ Difícil — vai fazer você perder tempo
→ Pergunte: "Você é quem cuida disso ou há alguém mais senior?"

---

## TECH STACK (Se Empresa — B2B)

Se você está prospectando uma empresa que pode ser cliente B2B:

| Categoria | Ferramentas | Implicação |
|-----------|------------|-----------|
| **CRM** | Salesforce / HubSpot / Pipedrive | Eles têm processo vendas estruturado |
| **Financeiro** | SAP / Oracle / Contabl | Procesos rígidos = processo de aprovação longo |
| **Data** | Snowflake / Databricks | Eles medem tudo = precisam de ROI |
| **Comunicação** | Slack / MS Teams | Cultura ágil = decisão rápida |

---

## WHEN TO RESEARCH

- ✅ 24-48h ANTES de call importante (não no dia)
- ✅ Se você vai fazer cold call (pesquise antes)
- ✅ Se recebeu referência de alguém (contextualizar)
- ❌ NÃO pesquise se você já conhece a pessoa (seja autêntico)

---

## RESEARCH CHECKLIST

Antes de ligar:

- ☐ Pesquisei a pessoa em LinkedIn?
- ☐ Sei qual é o cargo/seniority?
- ☐ Sei qual é a empresa/setor?
- ☐ Sei se é novo cliente ou foi prospect antes?
- ☐ Tenho 2-3 talking points personalizados?
- ☐ Meu opener é de 30 segundos max?
- ☐ Sei qual é a pergunta de abertura (não venda)?
- ☐ Tenho objeção handler preparado?
- ☐ Conheço a dor dele (não presumo)?

Se respondeu "não" para algum, pesquise mais 10 minutos.

---

## Integração com Outras Skills

**Depois de fazer Account Research:**
→ Use `call-prep-leevre` para estruturar full call
→ Use `follow-up-comercial-leevre` para Follow-up pós-call
→ Use `competitive-analysis-leevre` se ele mencionar concorrente

---

## Exemplo Completo

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ACCOUNT RESEARCH
Nome: João Silva | Empresa: ConstroRapida | Data: 2026-04-22
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

QUICK TAKE
João é diretor de operações de construtora em Curitiba que cresceu 200%.
Entrou há 8 meses (antes era na Odebrecht). Sinal claro: empresa está escalando,
pode precisar de capital para obras. Prospect quente.

---

PROSPECT PROFILE
| Campo | Info |
|-------|------|
| Nome | João Silva |
| Cargo | Diretor de Operações |
| Empresa | ConstroRapida |
| Tempo no Cargo | 8 meses |
| LinkedIn | linkedin.com/in/joaosilva (conectado) |

---

BACKGROUND
Trajetória:
- Odebrecht (2015-2024) — Gerente de Projetos
- ConstroRapida (2024-atual) — Diretor de Operações

Mudança: Saiu de mega-empresa para scale-up. Sinal = buscava liberdade / equity.
Educação: Poli-USP, Engenharia Civil

---

COMPANY INTEL
| Campo | Info |
|-------|------|
| Setor | Construção Civil |
| Funcionários | ~80 (cresceu de 40) |
| Fundação | 2018 |
| Localização | Curitiba (Matriz) + São Paulo (Filial Nova) |

Recente News:
- Lançou filial SP (abril 2026) — SINAL: Expansão geográfica
- Contratando 25 pessoas (engenheiros, arquitetos) — SINAL: Crescimento de obras
- Crescimento 200% YoY — SINAL: Capital intensivo

---

HIRING SIGNALS
- 25 vagas abertas (engenheiros, coordenadores)
- Velocidade agressiva (quer preenchidas em 60 dias)
- Implicação: Crescimento acelerado = novo orçamento

---

QUALIFICATION SIGNALS
✅ Sinal Positivo #1: Expansão geográfica (nova filial em SP = custo estrutural)
✅ Sinal Positivo #2: Contratação agressiva (crescimento de obras em pipeline)
✅ Sinal Positivo #3: Saiu de empresa estruturada (pode ter orçamento para estrutura)
⚠️ Cautela: Empresa ainda é pequena (budget pode ser limitado vs. orçamento Odebrecht)

---

PERFECT OPENER
"Oi João, vi que você virou diretor de ops da ConstroRapida.
Sou Livri da Leevre.

Acompanhei o crescimento de vocês no setor — 200% é agressivo.
Vi que abriram filial em SP e estão com muitas obras.

A gente trabalha com construtoras em escala como vocês que precisam
de capital de giro com disciplina (consórcio/financiamento).

Você teria 15 min na quarta para bater papo?"

---

TALKING POINTS
1. Abertura: "Como você está vendo o mercado de construção em 2026?"
   [Deixa ele falar]

2. Matching: "Achei interessante porque vocês estão crescendo, abriram filial nova
   — isso costuma gerar gargalo de capital de giro. A gente resolve isso."

3. Objection: "Lógico que tem prazos, mas consórcio traz taxa fixa sem juros,
   diferente de empréstimo. Com vocês tendo pipeline claro, combina bem."

4. Close: "Faz sentido a gente estruturar melhor? Posso chamar um sócio que entende
   de construção para vocês?"

---

NEXT STEP
Call agendada: [data/hora]
Objetivo: Descobrir se tem oportunidade real ou é educação
Sucesso: Agendar 2ª call com mais stakeholders (CFO, sócio)
```

---

## Regra de Ouro

**Research faz você chegar preparado, mas honestidade faz você vencer.**

Não invente contextualização. Se não souber algo, pergunte na call.
O "Oi, vi seu perfil e achei interessante" é sempre melhor que "Oi, eu sou insistente"
