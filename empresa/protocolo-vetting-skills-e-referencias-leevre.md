# Protocolo de vetting de skills e referências da Leevre

Data: 2026-04-14
Status: ativo

## Objetivo
Criar uma régua clara para qualquer material externo que entre no cérebro da Leevre, incluindo:
- skills
- repositórios
- prompts
- templates
- tutoriais
- automações
- integrações sugeridas

A meta é simples: aproveitar aprendizado externo sem importar risco, bagunça ou playbook genérico fora de contexto.

---

## Regra central
Nada externo entra em produção porque “parece bom”.

Todo item externo deve ser classificado antes em um destes estados:
1. **Referência**
2. **Candidata**
3. **Aprovada**
4. **Adaptada para produção**

---

## 1. Referência

### O que é
Material útil para estudo, benchmarking ou inspiração.

### Exemplos
- repositório interessante
- skill promissora
- template de SOUL/AGENTS/MEMORY
- tutorial de OpenClaw
- playbook de automação

### O que pode fazer
- clonar em área separada
- ler
- resumir
- extrair princípios
- comparar com o contexto da Leevre

### O que não pode fazer
- instalar direto
- substituir arquivo crítico da operação
- alterar config sensível com base apenas nessa referência

---

## 2. Candidata

### O que é
Item que aparenta ter utilidade real para a Leevre e merece auditoria mais profunda.

### Critérios para virar candidata
- resolve gargalo real da Leevre
- tem aderência com operação, comercial, marketing ou memória
- não depende de stack que não usamos
- não aumenta complexidade sem benefício claro

### Checklist mínimo
- qual problema real resolve?
- em que área da Leevre ajuda?
- quais dependências exige?
- que credenciais usa?
- qual risco operacional traz?

---

## 3. Aprovada

### O que é
Item auditado e considerado seguro/sensato para uso controlado.

### Requisitos
- escopo compreendido
- segurança mínima analisada
- dependências entendidas
- aderência ao contexto confirmada
- conflitos com arquitetura atual identificados

### Importante
“Aprovada” não significa “instalar em tudo”.
Significa apenas que pode seguir para adaptação ou uso controlado.

---

## 4. Adaptada para produção

### O que é
Quando o material deixa de ser cópia externa e passa a existir em versão própria da Leevre.

### Regra
Sempre que possível, adaptar ao nosso contexto em vez de espelhar integralmente.

### Sinais de adaptação correta
- linguagem alinhada à Leevre
- decisões compatíveis com a stack atual
- foco em gargalo real
- sem instruções desatualizadas ou genéricas
- documentação própria do porquê foi adotado

---

## Critérios de decisão

## Aderência ao contexto
Pergunta principal:
**isso ajuda a Leevre a operar melhor agora?**

Priorizar o que ajuda em:
- comissão
- conciliação
- PDFs e documentos
- rotina operacional
- CRM e follow-up
- tracking e analytics
- pesquisa de mercado e conteúdo
- segurança operacional do cérebro

## Segurança
Todo item deve ser observado para:
- prompt injection
- exfiltração de dados
- comandos destrutivos
- dependências obscuras
- credenciais hardcoded
- escopo excessivo para a função declarada

## Complexidade
Evitar itens que:
- aumentam manutenção cedo demais
- exigem infraestrutura que não temos
- trazem dependência externa desnecessária
- criam arquitetura mais sofisticada do que a operação atual suporta

## Atualidade
Validar se o material está alinhado com a versão atual do OpenClaw e da stack usada.
Se houver conflito entre referência externa e ambiente real, prevalece o ambiente real.

---

## Fluxo padrão

### Etapa 1 — triagem
Classificar como referência ou descartar.

### Etapa 2 — aderência
Se fizer sentido, promover para candidata.

### Etapa 3 — auditoria
Auditar escopo, risco, dependências, credenciais e impacto operacional.

### Etapa 4 — decisão
Escolher entre:
- descartar
- manter só como referência
- aprovar para uso controlado
- adaptar para produção

### Etapa 5 — documentação
Registrar o que foi decidido e por quê.

---

## Regras práticas da Livri

1. **Não copiar repo inteiro para a raiz do workspace**
2. **Não instalar skill de terceiros por impulso**
3. **Não tratar catálogo como selo de segurança**
4. **Não substituir cérebro atual por template externo**
5. **Não automatizar bagunça**
6. **Toda credencial deve seguir o padrão atual validado do OpenClaw**
7. **Toda adaptação precisa respeitar o contexto real da Leevre**

---

## Pergunta final antes de aprovar algo
Se isso entrar hoje, a operação da Leevre fica:
- mais clara?
- mais segura?
- mais rápida?
- mais previsível?

Se a resposta não for claramente sim em pelo menos um desses pontos, não entra agora.
