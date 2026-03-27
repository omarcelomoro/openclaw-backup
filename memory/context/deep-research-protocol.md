---
name: deep-research-protocol
description: >
  Use quando pedir: "pesquisa sobre", "deep research", "investiga",
  "analisa o mercado de", "benchmark", "quero entender melhor",
  "análise de concorrentes", "me dá um overview de".
---

# Deep Research Protocol

## Protocolo (executar em ordem)

### 1. ENQUADRAMENTO (2 min)
- Qual a pergunta exata que estou respondendo?
- Qual decisão essa pesquisa vai informar?
- Profundidade: quick scan (5-10 min) | standard (15-30 min) | deep dive

### 2. COLETA MULTI-FONTE

Fontes primárias (nesta ordem):
1. web_search — varredura geral (Brave)
2. web_fetch — extrair conteúdo das URLs mais relevantes
3. Knowledge Base — se tiver conteúdo relevante já ingestado

Fontes especializadas (quando relevante):
- Reddit/HackerNews — opinião de comunidade técnica
- Twitter/X — sinais em tempo real
- YouTube — análises longas

### 3. SÍNTESE

Para cada fonte, classificar:
- FATO → confirmável, com fonte
- OPINIÃO → interpretação, marcar como tal
- SINAL → sugere tendência, monitorar

### 4. RELATÓRIO (formato padrão)

```
# [Tema] — Deep Research
Data: DD/MM/YYYY

## TL;DR
- [3-5 bullets com o essencial]

## Contexto
[Por que estamos pesquisando / qual decisão isso informa]

## Findings

### [Subtema 1]
- Finding + fonte

### [Subtema 2]
- Finding + fonte

## Análise
[Cruzamento dos findings, padrões, o que significa]

## Recomendação
[O que fazer com essa informação]

## Fontes
1. [URL 1]
2. [URL 2]
```

### 5. SALVAMENTO
- Salvar em `memory/research/YYYY-MM-DD-[slug].md`

---

## Níveis de profundidade

| Nível      | Tempo      | URLs     | Saída                        |
|------------|------------|----------|------------------------------|
| Quick scan | 5-10 min   | 3-5      | 1 parágrafo + bullets        |
| Standard   | 15-30 min  | 8-12     | Relatório 1-2 páginas        |
| Deep dive  | 30-60 min  | 15-20    | Relatório 3-5 páginas        |

---

## Vieses a evitar
- **Confirmation bias** → buscar ativamente contra-argumentos
- **Recency bias** → verificar se tendências são reais ou hype
- **Survivorship bias** → buscar casos de fracasso, não só sucesso

---

## Prompts que ativam este protocolo
- "Deep research: ferramentas de automação para WhatsApp no Brasil"
- "Analisa o mercado de cursos online de IA em 2026"
- "Pesquisa os 5 maiores concorrentes do [produto]"
- "Investiga por que a [empresa X] cresceu tão rápido"
- "Benchmark: como os melhores SaaS de [categoria] fazem onboarding?"
