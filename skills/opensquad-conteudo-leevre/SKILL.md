---
name: opensquad-conteudo-leevre
description: >
  Squad de produção de conteúdo comercial para Leevre. Automatiza pesquisa de mercado,
  geração de copy com intenção de venda, design de visuais e aprovação antes de publicar.
  Funciona em pipeline com checkpoints humanos entre cada etapa.
kind: prompt
tags: #conteudo #marketing #opensquad #consorcio #seguros #leevre
triggers: criar conteúdo, produzir post, gerar copy, fazer carrossel, escrever email comercial, conteúdo para venda
---

# Squad de Conteúdo — Leevre

## Objetivo
Produzir conteúdo comercial (posts, emails, copy, carrosséis) para Leevre de forma sistemática,
com pesquisa validada, redação clara e design alinhado à marca.

## Arquitetura do Squad

Cada squad é um pipeline de agentes com **checkpoints de aprovação humana**.

```
PESQUISADOR → [você aprova] → REDATOR → [você aprova] → DESIGNER → [você aprova] → REVISOR
```

### Agente 1: Pesquisador
**Objetivo:** Coletar inteligência de mercado para informar o conteúdo.

**Tarefas:**
- Buscar tendências do mercado de consórcio/seguros
- Identificar dores do público-alvo
- Análise rápida de 2-3 concorrentes
- Extrair 3-5 insights acionáveis

**Entrega:**
```
# Pesquisa para [Tema]
- Insight 1: [achado]
- Insight 2: [achado]
- Ângulo recomendado: [sugestão]
- Tom recomendado: [consultivo/urgência/confiança/etc]
```

**Checkpoint:** Você aprova os insights antes de seguir para redação.

---

### Agente 2: Redator
**Objetivo:** Escrever copy comercial clara, com intenção de venda.

**Tarefas:**
- Usar insights da pesquisa
- Escrever headline + copy principal
- Incluir CTA claro
- Adaptar tom para o canal (Instagram/LinkedIn/Email)

**Entrega (por canal):**

**Instagram (Carrossel):**
```
Slide 1: Headline + hook visual
Slide 2-4: Educação/problema/solução
Slide 5: CTA
```

**LinkedIn (Post):**
```
Abertura (hook em 2 linhas)
Story/problema (3-4 linhas)
Solução/promessa (2-3 linhas)
CTA específica
```

**Email (Newsletter/Follow-up):**
```
Assunto: [clara, sem clickbait]
Preview: [primeiros 50 chars atraem]
Corpo: abertura → problema → solução → CTA
```

**Checkpoint:** Você aprova copy antes de ir para design.

---

### Agente 3: Designer
**Objetivo:** Criar visuais que acompanhem o copy.

**Tarefas:**
- Gerar 1-3 opções visuais (imagens/mockups)
- Respeitar voz visual da Leevre (cores, fontes)
- Adaptar para cada plataforma (1:1 Instagram, 16:9 LinkedIn, etc)

**Entrega:**
- Mockups prontos para publicar
- Ou brief visual para designer humano (se mais sofisticado)

**Checkpoint:** Você aprova visuais antes de seguir.

---

### Agente 4: Revisor
**Objetivo:** Validação final antes de publicar.

**Tarefas:**
- Verificar coerência copy ↔ visual
- Checar ortografia, tom, CTAs
- Validar conformidade com marca
- Gerar checklist de publicação

**Entrega:**
```
# Checklist de Publicação
☑ Copy aprovado
☑ Visuais aprovados
☑ Tom alinhado com marca
☑ CTA clara e acionável
☑ Sem erros ortográficos
☑ Publicar em: [canais]
```

---

## Como Usar Este Squad

### Setup Inicial (Uma Vez)
```
1. Você cria um prompt no Claude Code / Cursor dizendo:
   "/opensquad create Squad que produz conteúdo comercial para consórcio"

2. O opensquad vai te fazer perguntas:
   - Qual é o tema?
   - Qual é o tom?
   - Qual é o público-alvo?
   - Quais canais?

3. Ele monta o squad com 4 agentes + checkpoints
```

### Uso Recorrente
```
/opensquad run conteudo-comercial-leevre

Input:
- Tema: "Por que consórcio é melhor que empréstimo"
- Público: Pessoas buscando alavancagem patrimonial
- Canais: Instagram + LinkedIn + Email

O squad roda:
1. Pesquisador coleta insights
2. [VOCÊ APROVA]
3. Redator escreve 3 versões (1 Instagram, 1 LinkedIn, 1 Email)
4. [VOCÊ APROVA]
5. Designer cria visuais
6. [VOCÊ APROVA]
7. Revisor faz checklist final
8. Output pronto pra publicar
```

---

## Checkpoints Explícitos

Antes de seguir para a etapa seguinte, o agente SEMPRE para e pede sua aprovação:

```
✋ PAUSA PARA APROVAÇÃO

Pesquisador terminou. Aqui estão os insights:
- [Insight 1]
- [Insight 2]
- [Insight 3]

Ângulo recomendado: [sugestão]

Você quer:
A) Prosseguir com esses insights
B) Ajustar algo
C) Cancelar
```

**Você escolhe.** Se escolher B, Pesquisador ajusta. Não prossegue sem sua OK.

---

## Integração com Outras Skills

### Depois de Pesquisador Aprovar
→ Use `deep-research-protocol` se precisar pesquisa mais profunda

### Depois de Revisor Aprovar
→ Use `conteudo-comercial-leevre` para polir copy
→ Use `html-publish` para publicar direto em blog/site
→ Use `gog` (gmail) para enviar emails

---

## Dicas Práticas

### Para Rodar Diariamente (Sem Opensquad)
Se não quiser usar opensquad CLI, você pode rodar isso manualmente:
1. Pede pra mim: "pesquise sobre [tema]"
2. Eu entrego insights
3. Você aprova
4. Pede pra mim: "escreva copy sobre [tema] para Instagram"
5. E assim vai

### Para Usar em Batch (1x por Semana)
Liste 5 temas, roda 1 squad completo por tema, aprova tudo, publica ao longo da semana.

### Integração com HubSpot (Futuro)
Quando mcporter estiver configurado:
- Pesquisador busca leads "frios" no HubSpot
- Redator escreve email de follow-up personalizado
- Revisor aprova antes de enviar via Gmail

---

## Exemplo Prático: Post Sobre Consórcio

**Input:**
```
Tema: "Consórcio para quem está com empreendimento parado"
Público: Construtoras/imobiliárias
Canais: LinkedIn + Email
```

**Pesquisador entrega:**
```
# Pesquisa
- Insight 1: 45% das obras residenciais estão paralisadas por falta de capital
- Insight 2: Construtoras buscam alternativas a empréstimo bancário (juros altos)
- Insight 3: Consórcio oferece taxa fixa + disciplina de pagamento
- Ângulo: "Capital sem amarras — como consórcio acelera projetos parados"
- Tom: Consultivo, prático, sem alarme
```

**Você aprova** ✅

**Redator entrega:**

*LinkedIn:*
```
Sua obra está parada esperando capital?

Não é só sua. 45% das obras residenciais em SP enfrentam o mesmo desafio.
Empréstimo pesa no fluxo. Equity dilui seu controle. E agora?

Consórcio é diferente.

Você não paga juros. Paga uma taxa única durante a carência. Quando sai seu número,
você tem o capital — e a propriedade toda é sua.

Melhor ainda: diferentemente de empréstimos, consórcio premia disciplina.
Quem paga em dia, sai em dia. Sem surpresa de taxa flutuante.

Se sua obra está parada esperando esse capital, vamos conversar.

📞 [CTA]
```

*Email:*
```
Assunto: Sua obra parada? Capital sem juros pode ser o caminho

Oi [Nome],

Sabemos que construtoras em SP estão enfrentando gargalo de capital.

Consórcio imobiliário é mais que um produto — é engenharia financeira que deixa
você no controle.

Quer saber como isso funciona?

[CTA]

Abraço,
Leevre
```

**Você aprova** ✅

**Designer entrega:**
```
LinkedIn Post + 2 imagens mockup
Email Header + 3 template options
```

**Você aprova** ✅

**Revisor entrega:**
```
✅ Copy aprovado
✅ Visuais aprovados
✅ Tom consultivo (alinhado com marca)
✅ CTA clara
✅ Publicar em: LinkedIn + Enviar email

Pronto! Sair do forno.
```

---

## Quando NÃO Usar Este Squad

- ❌ Para conteúdo que precisa de autorização legal/compliance prévia
- ❌ Para anúncios pagos (precisa de aprovação de orçamento antes)
- ❌ Para comunicações financeiras sensíveis (use revisor humano real)

**Para esses, o squad gera draft, mas você aprova com seu time jurídico antes de publicar.**

---

## Próximos Passos

1. Testamos este squad com 1 tema real essa semana
2. Você aprova o fluxo
3. Rodamos 2-3 conteúdos por semana
4. Automação cresce conforme você ganhar confiança

Quer começar?
