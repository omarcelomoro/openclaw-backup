# Leevre OS — Arquitetura operacional com agentes

Data: 2026-05-05
Responsável: Livri

## Princípio central

Comissão, conciliação, leads, renovações, follow-ups e pendências não podem depender da cabeça do Marcelo.

A Leevre precisa operar com:

1. entrada clara
2. classificação por área
3. responsável definido
4. próxima ação
5. prazo/checkpoint
6. memória operacional
7. relatório de exceções

---

# 1) Papel da Livri COO

Sim: a Livri já orquestra tudo.

Mas a diferença entre “Livri faz tudo” e “Livri orquestra agentes” é escala e foco.

## Livri COO deve fazer

- definir prioridade geral
- resolver conflito entre áreas
- cobrar cadência
- consolidar visão executiva
- registrar decisões importantes
- transformar aprendizados em sistema

## Livri COO não deve ser gargalo de tudo

A Livri não deve ser o único lugar onde comissão, marketing, comercial e triagem são processados. Ela deve ser a central de comando, não o único operador.

---

# 2) Agentes por função

## Já existentes

### Pessoal / Aristóteles

Uso recomendado:

- decisões pessoais do Marcelo
- dilemas de longo prazo
- saúde mental/energia/foco
- riscos de vida e prioridade
- conversas que não devem se misturar com operação da Leevre

Não usar para:

- comissão
- follow-up comercial
- marketing operacional
- triagem de e-mails da empresa

### Marketing / Kotler

Uso recomendado:

- tendências
- ideias de conteúdo
- benchmark
- ganchos
- roteiros
- Reels/carrosséis/posts
- posicionamento orgânico

Ajuste recomendado:

Kotler deve ficar mais no radar criativo/estratégico de conteúdo. O novo agente Marketing da Leevre pode ficar mais operacional: pauta, calendário, copy, CTA e tracking.

---

## Novos agentes preparados

Criei a estrutura de arquivos para quatro agentes:

1. `agents/leevre-operacional`
2. `agents/leevre-comercial`
3. `agents/leevre-marketing`
4. `agents/leevre-triagem`

Cada um recebeu:

- `AGENTS.md`
- `SOUL.md`
- `IDENTITY.md`

---

# 3) Função de cada área

## A) Operacional — comissão/conciliação/renovações/pendências

### Responsabilidade

- comissão de produtores
- conciliação de recebimentos
- conferência de repasses
- pendências com administradoras/seguradoras/clientes
- renovações de seguros
- relatório operacional semanal

### Entrada típica

- planilha de comissão
- extrato/relatório de seguradora ou administradora
- print de pendência
- e-mail operacional
- mensagem sobre pagamento ou divergência

### Saída padrão

- resumo executivo
- divergências encontradas
- pendências críticas
- dados faltantes
- ações recomendadas
- próximo checkpoint

---

## B) Comercial Consórcio — leads/follow-up/CRM/propostas

### Responsabilidade

- leads de consórcio de imóvel
- qualificação
- estágio do funil
- follow-up
- propostas/simulações
- objeções
- motivo de perda
- próxima ação

### Regra de ouro

Nenhum lead pode ficar sem próxima ação.

### Saída padrão

- leads prioritários
- próxima ação por lead
- follow-up sugerido
- risco de perda
- objeções/padrões
- decisão necessária

---

## C) Marketing/Conteúdo — pauta/copy/tracking

### Responsabilidade

- calendário editorial
- copy
- CTA
- tracking
- reaproveitamento de conteúdo
- análise de performance
- organização de campanha

### Diferença para Kotler

Kotler é mais criativo/estratégico/radar de atenção.

Marketing Leevre é mais operador de esteira:

- o que publicar
- quando publicar
- qual CTA
- qual origem registrar
- como medir
- como reaproveitar

---

## D) Triagem Gmail/WhatsApp

### Responsabilidade

- classificar entradas
- sugerir respostas
- separar urgência
- extrair dados importantes
- encaminhar para agente certo
- montar resumo diário

### Regras

- não envia sem aprovação
- não apaga/arquiva sem autorização
- não expõe memória pessoal no grupo
- tudo vira responsável + próxima ação

---

# 4) Gateway como central de comando

## Roteamento desejado

- Lead novo → Comercial Consórcio
- Pedido de simulação → Comercial Consórcio
- Objeção ou lead frio → Comercial Consórcio + Marketing se virar pauta
- E-mail de seguradora/administradora → Operacional
- Planilha de comissão → Operacional
- Pendência de renovação → Operacional
- Ideia de conteúdo → Marketing/Kotler
- Trend/benchmark → Kotler
- Inbox misto Gmail/WhatsApp → Triagem
- Decisão estratégica → Livri COO
- Decisão pessoal → Aristóteles/Pessoal

---

# 5) Rotinas automáticas recomendadas

## Diário

### Comercial

- revisar leads sem próxima ação
- revisar leads quentes parados
- sugerir follow-ups do dia

### Triagem

- classificar novas entradas
- separar urgências
- gerar respostas sugeridas

## Semanal

### Operacional

- relatório de comissão/conciliação
- pendências críticas
- divergências abertas

### Marketing

- pauta da semana
- tracking de CTAs
- aprendizados de conteúdo

### Livri COO

- consolidar visão executiva:
  - comercial
  - operação
  - marketing
  - pendências
  - decisões

## Mensal

- fechamento de comissão
- revisão de pipeline
- análise de origem dos leads
- atualização de playbooks
- revisão das métricas principais

---

# 6) Memória em Markdown

## Estrutura recomendada

### Operação

`memory/projects/leevre-operacao.md`

Registrar:

- regras de comissão
- produtores
- pendências recorrentes
- aprendizados de conciliação
- exceções importantes

### Comercial

Criar/usar:

`memory/projects/leevre-comercial.md`

Registrar:

- funil
- objeções
- motivos de perda
- scripts de follow-up
- padrões de fechamento

### Marketing

`memory/projects/leevre-marketing.md`

Registrar:

- pilares
- CTAs
- conteúdos testados
- métricas
- aprendizados

### Pendências

`memory/pending.md`

Registrar tudo que tem dono, prazo ou próxima ação.

---

# 7) Próximas implementações técnicas

## Já feito

- Criação da estrutura local dos novos agentes.
- Documento de arquitetura Leevre OS.

## Falta aplicar no Gateway

Para rotear automaticamente dentro do grupo Leevre, falta criar/confirmar os tópicos no Telegram e vincular cada tópico ao agente certo.

Tópicos atuais identificados:

- Marketing: topic `6`, agente `kotler`
- CEO: topic `16`, sem agente dedicado
- Pessoal: topic `2263`, agente `aristoteles`

Tópicos recomendados a criar no grupo Leevre:

1. Operacional
2. Comercial Consórcio
3. Triagem Inbox
4. Comissão/Conciliação, se quiser separar de Operacional

Depois disso, aplicar bindings:

- Operacional → `leevre-operacional`
- Comercial Consórcio → `leevre-comercial`
- Marketing operacional → `leevre-marketing` ou manter Kotler no tópico Marketing e usar Marketing Leevre para execução interna
- Triagem Inbox → `leevre-triagem`

---

# Recomendação da Livri

Começar simples:

1. Criar 3 tópicos no grupo Leevre:
   - Operacional
   - Comercial
   - Triagem
2. Manter Marketing com Kotler por enquanto.
3. Usar Livri COO no tópico CEO.
4. Após 7 dias, revisar se precisa separar “Comissão/Conciliação” de “Operacional”.

Motivo: separar demais antes de ter volume real cria burocracia. Melhor começar com 3 áreas fortes e dividir quando houver repetição suficiente.
