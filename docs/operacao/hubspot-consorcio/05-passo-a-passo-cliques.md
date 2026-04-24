# Passo a passo de cliques — HubSpot Consórcio Leevre

## Objetivo
Executar a implantação do HubSpot de consórcio da Leevre com instruções diretas de navegação no portal.

---

## Parte 1 — Abrir a área certa

### Caminho
- entrar no HubSpot
- clicar em **Configurações**
- no menu lateral, abrir **Objetos**
- clicar em **Negócios**

Aqui você vai usar principalmente duas áreas:
1. **Pipelines**
2. **Propriedades**

---

## Parte 2 — Ajustar o pipeline

### Caminho
- em **Negócios**, abrir **Pipelines**
- localizar o pipeline atual

### O que fazer
- editar o pipeline atual ou criar um novo se preferir separar com clareza
- deixar a ordem final exatamente assim:
  1. Lead Entrou
  2. Contato Iniciado
  3. Lead Qualificado
  4. Simulação Enviada
  5. Em Negociação
  6. Documentação / Fechamento
  7. Ganho
  8. Perdido
  9. Pausado / Sem timing

### Validar antes de sair
- não existe stage redundante
- “Pausado / Sem timing” está separado de “Perdido”
- o pipeline está com cara de processo comercial real

---

## Parte 3 — Criar os campos prioritários

### Caminho
- voltar em **Configurações**
- **Objetos > Negócios > Propriedades**
- clicar em **Criar propriedade**

### Criar primeiro estes campos

#### Grupo sugerido
Se o HubSpot pedir grupo, usar algo como:
- `Informações do negócio` se quiser simplicidade
ou
- criar grupo próprio tipo `Consórcio Leevre`

### Campos

#### 1. origem do lead
- tipo: seleção
- opções: Orgânico, Tráfego pago, Indicação, Parceria, Outro

#### 2. canal detalhado
- tipo: texto de uma linha

#### 3. próxima ação
- tipo: texto de uma linha

#### 4. data do próximo follow-up
- tipo: data

#### 5. temperatura
- tipo: seleção
- opções: Quente, Morno, Frio, Pausado

#### 6. objetivo do cliente
- tipo: texto de uma linha

#### 7. valor pretendido da carta
- tipo: número

#### 8. campo objeções
- tipo: texto de múltiplas linhas

#### 9. objeção principal
- tipo: seleção
- opções:
  - Agora não é o momento
  - Preciso pensar melhor
  - Ficou caro
  - Vou comparar com outra opção
  - Não entendi direito como funciona
  - Tenho medo de errar
  - Vou decidir com cônjuge ou sócio
  - Perdi prioridade nisso agora

#### 10. roadmap to close
- tipo: texto de múltiplas linhas

#### 11. motivo de perda
- tipo: seleção
- opções:
  - Sem timing
  - Preço ou parcela não encaixou
  - Decidiu por outra solução
  - Fechou com concorrente
  - Perfil não aderente
  - Sem resposta após tentativas
  - Desistiu do objetivo

#### 12. motivo de pausa
- tipo: seleção
- opções:
  - Aguardando organização financeira
  - Aguardando decisão familiar ou societária
  - Aguardando documento
  - Aguardando momento de compra
  - Voltou para análise futura

#### 13. data de retomada
- tipo: data

---

## Parte 4 — Criar segunda camada de campos

### Ainda em Propriedades
Criar depois estes campos:

- data da última interação → data/hora
- tipo de consórcio → seleção
- perfil do cliente → seleção (PF/PJ)
- valor ou faixa de parcela desejada → texto
- administradora → seleção
- status da negociação → seleção
- pendência documental principal → texto
- prazo da pendência → data
- valor final → número
- produto final → texto
- concorrente → texto
- observações comerciais estruturadas → múltiplas linhas

---

## Parte 5 — Organizar a visualização do negócio

### Caminho
- abrir qualquer deal de teste
- clicar em personalização da barra lateral/propriedades visíveis

### Garantir que apareçam com destaque
- responsável
- próxima ação
- data do próximo follow-up
- temperatura
- objetivo do cliente
- valor pretendido da carta
- campo objeções
- objeção principal
- roadmap to close
- motivo de perda
- motivo de pausa
- data de retomada

Objetivo: o time precisa bater o olho e entender a situação do negócio.

---

## Parte 6 — Regras por etapa

### Aplicação prática
Ao mover uma deal, conferir:

#### Lead Entrou
- origem do lead
- canal detalhado
- responsável

#### Contato Iniciado
- próxima ação
- data do próximo follow-up

#### Lead Qualificado
- objetivo do cliente
- temperatura

#### Simulação Enviada
- valor pretendido da carta

#### Em Negociação
- campo objeções
- objeção principal
- roadmap to close
- próxima ação
- data do próximo follow-up

#### Documentação / Fechamento
- pendência documental principal
- próxima ação

#### Perdido
- motivo de perda

#### Pausado / Sem timing
- motivo de pausa
- data de retomada

---

## Parte 7 — Testar com deals reais

### Caminho
- abrir a tela de negócios
- escolher 5 a 10 deals reais
- preencher e mover pelas etapas

### Validar
- ficou fácil preencher?
- a deal mostra claramente o que falta para fechar?
- o roadmap to close ajuda ou está virando texto inútil?
- pausado ficou controlado?
- follow-up vencido ficou fácil de enxergar?

---

## Parte 8 — O que não fazer agora
- não automatizar mudança de etapa
- não criar campo demais no começo
- não deixar deal ativa sem próxima ação
- não usar observações longas para substituir campo estruturado

---

## Arquivos de apoio
- `rotinas/folha-de-cola-hubspot-consorcio-leevre.md`
- `rotinas/checklist-execucao-hubspot-consorcio-leevre.md`
- `rotinas/estrutura-final-pipeline-consorcio-hubspot-leevre.md`
- `rotinas/plano-implantacao-real-hubspot-consorcio-leevre.md`
