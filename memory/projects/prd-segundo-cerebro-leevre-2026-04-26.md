# PRD — Segundo Cérebro da Leevre (Pessoal, Empresa, Diretoria)
Data: 2026-04-26

## 1. Objetivo
Definir como a Leevre deve evoluir do cérebro atual para uma arquitetura em 3 camadas, sem substituir cegamente o que já existe:
- cérebro pessoal
- cérebro da empresa/time
- cérebro da diretoria

## 2. Diagnóstico do estado atual da Leevre
A Leevre **já tem um cérebro funcional**, mas ele é **único e híbrido**, não separado formalmente em 3 repositórios.

### O que já existe hoje
- identidade operacional do agente (`SOUL.md`, `IDENTITY.md`, `USER.md`, `AGENTS.md`)
- memória persistente (`MEMORY.md`, `memory/context/*`, `memory/projects/*`, `memory/sessions/*`)
- contexto institucional (`empresa/*`)
- skills da Leevre (`skills/*`)
- rotinas operacionais (`rotinas/*`)
- artefatos, estado e auditorias (`state/*`)

### O que isso significa
A Leevre **não está começando do zero**.
A base atual já cumpre parte do papel de:
- cérebro da empresa
- memória viva do agente principal
- centro de execução operacional

### Limitações da estrutura atual
- não existe cérebro pessoal separado do Marcelo
- não existe cérebro sensível de diretoria
- não existe separação formal entre conteúdo privado, operacional e sensível
- a documentação atual tem incoerências estruturais:
  - `empresa/mapa-do-cerebro.md` descreve `areas/*`, mas essa estrutura não aparece hoje no workspace ativo
  - `cerebro/index.md` fala em `onboarding/` e `referencias/`, mas isso não está refletido como estrutura central atual

## 3. Decisão recomendada
**Não substituir o cérebro atual da Leevre agora.**

### Por quê
Porque já existe contexto, memória, skills e rotinas vivas demais aqui. Trocar tudo agora criaria:
- risco de perda de contexto
- ruptura operacional
- retrabalho de adaptação
- confusão entre estrutura nova e operação real atual

### Caminho melhor
**Adaptar o que já existe** e usar os templates como referência de arquitetura futura.

## 4. Como os 3 templates podem ajudar

### 4.1 Cérebro pessoal
Função:
- notas privadas do Marcelo
- contexto individual
- buffer estratégico pessoal
- origem do que depois sobe para empresa ou diretoria

Ajuda prática:
- separar pensamento bruto do Marcelo do operacional da empresa
- evitar misturar reflexão pessoal com canônico do time
- criar lugar próprio para `/save` e `/team-sync`

### 4.2 Cérebro empresa
Função:
- operacional do time
- marketing, vendas, atendimento, operações, produto
- staging + inbox + consolidação

Ajuda prática:
- organizar colaboração futura
- separar visitante de gestor
- criar fluxo explícito de captura e promoção para canônico

### 4.3 Cérebro diretoria
Função:
- dados sensíveis: financeiro nominal, RH, jurídico, governança

Ajuda prática:
- preparar a Leevre para crescer sem jogar tema sensível no mesmo cérebro do time
- criar regra clara para dados que hoje ainda estão misturados ou nem têm lugar certo

## 5. Vale criar diretoria agora?
**Não como cérebro operacional completo. Sim como desenho/plano futuro.**

### Minha leitura
Hoje a Leevre ainda não tem estrutura de diretoria madura o suficiente para justificar o custo operacional de abrir esse cérebro em produção já.

### Recomendação
- **agora:** desenhar e validar o template
- **depois:** abrir de verdade quando aparecerem casos recorrentes de:
  - dinheiro com nome próprio
  - RH nominal
  - contrato/governança/jurídico sensível

## 6. Resultado dos testes com os templates

## Template pessoal — achados
### Acerto
- filosofia é boa: pessoal privado, `/save`, `/team-sync`, `main` only

### Problemas
- achado crítico: o script de inicialização depende do diretório corrente e pode atingir o repo errado se rodado fora do root correto
- o diretório do agente **não foi renomeado** (`agentes/{{AGENTE_SLUG}}` continuou literal)
- sobram placeholders relevantes após init (`{{ORG}}`, `{{SUA_CONTA}}`, etc.)
- README promete elementos que não batem integralmente com a estrutura real

### Leitura
Bom conceito, execução ainda frágil.

## Template empresa — achados
### Acertos
- onboarding mais maduro
- staging + inbox + consolidação faz sentido
- separação gestor vs visitante é boa
- setup mais consistente que o pessoal

### Pontos de atenção
- deixa vários placeholders pro pós-init, o que é aceitável, mas aumenta ambiguidade
- depende de disciplina operacional real para funcionar

### Leitura
É o template mais útil para servir de referência de adaptação da Leevre.

## Template diretoria — achados
### Acertos
- prudência forte
- branch protection obrigatória bem sinalizada
- boa separação de sensibilidade

### Pontos de atenção
- custo operacional alto para momento atual da Leevre
- depende de maturidade anterior do cérebro empresa

### Leitura
Vale como arquitetura futura, não como prioridade imediata.

## 7. Recomendação estratégica por ordem
### Fase 1 — mapear/adaptar o cérebro atual da Leevre
Objetivo:
- declarar explicitamente que o cérebro atual já é o embrião do cérebro empresa
- corrigir incoerências da estrutura atual
- separar melhor o que é memória, contexto institucional, rotina, estado e operação

### Fase 2 — criar cérebro pessoal do Marcelo
Objetivo:
- testar o fluxo pessoal sem mexer no canônico da empresa
- validar `/save` + `/team-sync`
- criar espaço privado real

### Fase 3 — formalizar cérebro empresa no padrão novo
Objetivo:
- migrar gradualmente o cérebro atual para uma arquitetura mais parecida com o template empresa
- sem ruptura, por camadas

### Fase 4 — desenhar diretoria e só abrir quando houver gatilho real
Objetivo:
- deixar padrão pronto
- ativar só quando a operação pedir

## 8. PRD de implementação em camadas

### Camada A — Pessoal
**Objetivo:** criar o cérebro pessoal do Marcelo.

**Escopo:**
- repo privado próprio
- `/save`
- `/team-sync`
- notas privadas
- contexto pessoal/profissional do Marcelo

**Não fazer agora:** migrar memória atual da Leevre inteira pra ele.

**Critério de sucesso:**
- 1 semana de uso real sem confusão
- capturas privadas funcionando
- sincronização consciente para empresa

### Camada B — Empresa
**Objetivo:** consolidar o cérebro atual da Leevre como cérebro operacional do time.

**Escopo:**
- adaptar estrutura atual
- definir áreas canônicas
- preparar inbox/staging se fizer sentido
- preservar memória e rotinas já existentes

**Não fazer agora:** apagar estrutura atual para recomeçar do zero.

**Critério de sucesso:**
- clareza estrutural maior
- menos ambiguidade de onde guardar cada coisa
- continuidade operacional preservada

### Camada C — Diretoria
**Objetivo:** preparar um cérebro sensível futuro.

**Escopo:**
- branch protection
- regras dos 3 gatilhos
- política de acesso
- template pronto para ativação futura

**Critério de sucesso:**
- decisão clara de quando abrir
- zero pressa antes da maturidade necessária

## 9. Próximos passos práticos
1. tratar oficialmente o workspace atual como **cérebro empresa-base da Leevre**
2. corrigir incoerências da estrutura atual
3. abrir cérebro pessoal do Marcelo em repo separado
4. testar uso real por 7 a 14 dias
5. só depois decidir o quanto do template empresa vira padrão
6. deixar diretoria como blueprint até haver gatilho real

## 10. Veredicto final
- **Sim, a Leevre já tem um cérebro hoje.**
- **Não vale substituir agora. Vale adaptar.**
- **O template empresa é a melhor referência estrutural.**
- **O template pessoal vale ser testado, mas precisa correções.**
- **O template diretoria vale mais como preparação futura do que como implantação imediata.**
