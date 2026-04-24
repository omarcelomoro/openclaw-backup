# Plano priorizado de adaptação para a Leevre

Data: 2026-04-14
Base de referência:
- `imports/github-references/openclaw-BrunoOkamoto`
- `imports/github-references/awesome-openclaw-skills`

## Objetivo
Definir o que adaptar primeiro para fortalecer o cérebro da Livri e acelerar a Leevre sem trazer complexidade prematura.

---

## Resumo executivo

A ordem correta para a Leevre não é instalar muitas skills nem abrir multiagentes agora.

A ordem correta é:
1. endurecer cérebro, memória e segurança operacional
2. melhorar runbooks e disciplina de troubleshooting
3. organizar pipeline de skills externas com auditoria
4. só então expandir para CRM, PDF, pesquisa e produtividade

Isso respeita o gargalo real da Leevre hoje:
- operação ainda pesa demais
- comissão e conciliação seguem na frente
- CRM e tracking ainda precisam de base mais sólida
- complexidade excessiva agora aumenta risco e retrabalho

---

## Prioridade 1 — adaptar já

## 1. Padrão de vetting de referências, skills e automações

### O que adaptar
Criar um padrão explícito para classificar tudo que vier de fora em 4 estados:
- referência
- candidata
- aprovada
- adaptada para produção

### Por que isso é prioridade
A Leevre está começando a puxar muitas referências externas. Sem triagem clara, o cérebro vira bagunça e risco.

### Resultado esperado
- menos instalação por impulso
- menos risco de importar instrução errada
- mais clareza do que é inspiração e do que já faz parte da operação

### Recomendação prática
Criar uma área simples de inventário e um pequeno protocolo interno de aprovação.

---

## 2. Runbook operacional de update, backup, rollback e troubleshooting

### O que adaptar
Absorver do material do Bruno:
- checklist de update
- regra de backup antes de mudanças estruturais
- regra de restart/validação de gateway
- lógica de rollback e validação final

### Por que isso é prioridade
Acabamos de viver um update real e já houve aprendizado prático valioso. Esse padrão precisa virar sistema.

### Resultado esperado
- menos improviso em manutenção
- menos risco de quebrar operação
- troubleshooting mais rápido

### Recomendação prática
Criar um runbook próprio da Leevre/Livri, baseado no que aprendemos hoje e reforçado com os melhores pontos do repositório analisado.

---

## 3. Fortalecer arquitetura do cérebro da Livri

### O que adaptar
Puxar boas práticas de:
- memória por camadas
- `MEMORY.md` como índice
- topic files bem definidos
- heartbeat como rotina de manutenção útil
- documentação de decisões e lições

### Por que isso é prioridade
Esse é o núcleo da continuidade. Sem isso, toda evolução futura perde consistência.

### Resultado esperado
- memória mais confiável
- menos perda de contexto
- decisões mais fáceis de recuperar
- menos repetição de erros

### Recomendação prática
Não substituir nossos arquivos. Apenas refinar o que já existe com padrões melhores quando houver ganho real.

---

## Prioridade 2 — preparar em seguida

## 4. Biblioteca interna de runbooks da Leevre

### O que adaptar
Usar a pegada do repo Bruno para criar runbooks curtos e práticos sobre:
- update e manutenção do OpenClaw
- troubleshooting de gateway/canais
- estrutura de memória
- backup e rollback
- auditoria de referências externas

### Por que isso importa
A Leevre precisa de sistema, não de lembrança solta em conversa.

### Resultado esperado
- operação mais previsível
- onboarding interno melhor
- menos dependência da memória do momento

---

## 5. Shortlist auditável de skills externas

### O que adaptar
Transformar o catálogo de skills em um funil de decisão:
- shortlist por tema
- auditoria individual
- decisão: instalar, adaptar ou só usar como referência

### Ordem sugerida de auditoria
1. segurança / vetting
2. deep research
3. PDF / documentos
4. Gmail / Calendar / produtividade
5. CRM / task / follow-up

### Por que isso importa
Evita ruído e garante que cada skill tenha justificativa operacional.

---

## 6. Pesquisa e inteligência como rotina estruturada

### O que adaptar
Aproveitar referência de deep research e transformar em padrão Leevre para:
- concorrentes
- posicionamento
- conteúdo
- canais
- benchmarks

### Por que isso importa
Marketing e conteúdo têm alto potencial, mas hoje ainda precisam de pesquisa mais disciplinada e acionável.

### Observação
Isso já é útil agora, mas ainda abaixo de operação, memória e segurança.

---

## Prioridade 3 — depois da base arrumada

## 7. Expansão para skills de CRM e follow-up

### Quando faz sentido
Depois que houver mais clareza do funil, próxima ação, cadência e rotina comercial mínima.

### Motivo
Instalar ou adaptar skill de CRM antes da disciplina comercial mínima pode automatizar bagunça.

---

## 8. Expansão para PDF/documentos mais sofisticados

### Quando faz sentido
Assim que entrarem os documentos reais de comissão, extrato e recebimento.

### Motivo
Essa é uma frente altamente promissora para a Leevre, mas depende de exemplos reais para não virar arquitetura sem matéria-prima.

---

## 9. Browser automation e multiagentes mais pesados

### Quando faz sentido
Só depois que:
- base operacional estiver firme
- runbooks estiverem consolidados
- skills externas já tiverem régua de auditoria

### Motivo
Complexidade extra sem base clara tende a aumentar o caos.

---

## Top 10 adaptações mais úteis para começar

1. protocolo interno de vetting de skills e referências
2. runbook de update/backup/rollback
3. checklist de troubleshooting de gateway e canais
4. refinamento da arquitetura de memória e topic files
5. inventário de referências externas já importadas
6. shortlist auditável de skills externas por prioridade
7. padrão Leevre de deep research
8. runbook de segurança operacional do OpenClaw
9. preparação de trilha para PDF/documentos reais
10. preparação da trilha futura de CRM/follow-up

---

## Recomendação final

Se for para escolher o que adaptar primeiro, eu escolheria nesta ordem:

### Bloco 1
- vetting de skills e referências
- update / backup / rollback
- troubleshooting / segurança operacional

### Bloco 2
- refinamento do cérebro e memória
- biblioteca interna de runbooks
- padrão de deep research

### Bloco 3
- shortlist auditada de skills
- PDF/documentos
- CRM/follow-up

Essa sequência é a que mais respeita a realidade da Leevre hoje: menos hype, mais base, menos improviso, mais sistema.
