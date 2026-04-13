# Adaptação para a Leevre

## O que foi importado
Base estrutural da pasta `imersao-openclaw-negocios-main`, com foco em:
- arquitetura de cérebro empresarial
- organização por áreas, contexto, rotinas e skills
- governança de agentes
- marketing com ciclo hipótese → criativo → teste → dado → conclusão
- rotinas comerciais de follow-up e leads esfriando
- modelos de auditoria de integridade

## O que faz sentido aproveitar na Leevre

### 1. Estrutura operacional do cérebro
A lógica de `empresa/`, `areas/`, `agentes/`, `rotinas/`, `skills/` já conversa bem com a estrutura atual da Leevre. O ganho aqui não é copiar a empresa demo, e sim reforçar padrão, disciplina e governança.

### 2. Marketing como sistema, não como posts soltos
O material de `trafego-pago` trouxe um ponto forte: marketing precisa rodar em ciclo fechado.

Adaptação para Leevre:
- hipótese comercial
- criativo / conteúdo
- publicação / campanha
- dado
- conclusão
- novo teste

Isso combina diretamente com:
- hooks de consórcio
- criativos de autoridade
- testes de promessa
- tracking mínimo
- decisão de pausar, insistir ou escalar

### 3. Follow-up baseado em temperatura real
A skill de `follow-up-leads` é útil como referência, mas precisa sair do modelo de infoproduto e entrar no contexto de consórcio/seguro.

Adaptação necessária:
- trocar `dados/leads.csv` por CRM/planilha real
- incluir estágio, próxima ação, motivo de perda, valor de carta e urgência
- separar lógica de consórcio e seguro
- priorizar lead parado com proposta, simulação ou documentação em aberto

### 4. Auditoria de integridade do cérebro
O modelo de auditoria é valioso para evitar bagunça silenciosa.

Adaptação para Leevre:
- verificar se skills estão indexadas
- verificar se rotinas batem com a operação real
- identificar arquivos órfãos
- auditar coerência entre áreas, agentes e memória
- revisar segurança e permissões do OpenClaw

## O que NÃO deve ser copiado cegamente
- empresa fictícia e seus dados demo
- referência a Meta Ads API como se já fosse stack ativa da Leevre
- rotinas de suporte e onboarding genéricas sem conexão com operação real
- agentes demais antes da base operacional estar redonda
- automações que dependem de API não validada

## Direção recomendada
A Leevre deve absorver o que aumenta:
- clareza
- cadência
- visibilidade
- governança
- reutilização de conhecimento

E ignorar o que só aumenta complexidade bonita.

## Blocos aprovados para adaptação imediata
1. processo de tráfego pago e hipóteses
2. rotina de leads esfriando e follow-up
3. auditoria de integridade do cérebro
4. governança mínima de agentes e permissões

## Resultado desta importação
A pasta importada vira:
- referência
- biblioteca de padrões
- fonte de adaptação

Ela não vira fonte de verdade da Leevre. A fonte de verdade continua sendo o workspace atual da Leevre.
