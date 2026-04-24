# Piloto LobsterLink — Tokio Marine

Data: 2026-04-19
Status: proposta de piloto controlado

## Objetivo
Validar se o LobsterLink ajuda a Leevre a destravar acesso e extração em portal autenticado da Tokio Marine sem exigir compartilhamento de credenciais com o agente.

## Decisão de contexto
O LobsterLink não entra como padrão geral da Leevre neste momento.
Ele entra, se aprovado, como **piloto específico** para o caso Tokio Marine.

---

## Hipótese do piloto
Se o gargalo principal da Tokio Marine for:
- login
- 2FA
- CAPTCHA
- validação humana pontual

então o LobsterLink pode reduzir bloqueio operacional porque permite:
- o humano assumir só a aba necessária
- completar o passo manual
- devolver a sessão autenticada ao browser do agente

---

## Quando faz sentido seguir
Seguir com piloto se o portal da Tokio Marine:
- exigir autenticação em área restrita
- bloquear automação pura em algum ponto crítico
- permitir ganho real ao reutilizar sessão autenticada depois do desbloqueio humano

## Quando não faz sentido seguir
Não seguir agora se:
- o browser atual do OpenClaw já resolver o fluxo sem intervenção extra
- a extração ainda estiver mal definida
- o gargalo real não for autenticação humana, e sim estrutura da navegação ou parsing dos dados

---

## Escopo do piloto
O piloto deve validar apenas:
1. instalação controlada da extensão
2. abertura e uso do bridge
3. acesso humano à aba compartilhada
4. login/desbloqueio em portal da Tokio Marine
5. continuidade da sessão autenticada no browser do agente
6. capacidade de seguir navegação/exploração após o desbloqueio

O piloto **não** valida ainda:
- pipeline completo de scraping para todas as seguradoras
- padronização para toda a operação
- rollout definitivo em produção ampla

---

## Pré-requisitos

### Técnicos
- backup do workspace antes de alterar config/browser
- confirmação do estado atual do browser do OpenClaw
- ambiente com possibilidade de rollback
- registro claro do que foi alterado

### Operacionais
- um fluxo real da Tokio Marine definido para teste
- clareza sobre qual passo costuma travar
- alguém disponível para executar a intervenção humana no momento do teste

---

## Etapas do piloto

## Etapa 1 — preparação
1. confirmar fluxo alvo da Tokio Marine
2. registrar comportamento atual sem LobsterLink
3. confirmar se o problema real é autenticação/bloqueio humano

### Evidência esperada
- descrição do fluxo
- ponto de bloqueio identificado
- hipótese clara do ganho esperado

---

## Etapa 2 — instalação controlada
1. fazer backup antes da mudança
2. instalar LobsterLink no browser isolado do OpenClaw
3. validar bridge URL e skill runtime
4. reiniciar/validar browser conforme necessário

### Evidência esperada
- extensão carregada
- flags corretas no browser
- bridge funcional
- rollback documentado

---

## Etapa 3 — teste funcional
1. abrir portal Tokio Marine no browser do agente
2. iniciar compartilhamento da aba
3. abrir viewer link do LobsterLink
4. executar login/desbloqueio humano
5. devolver controle ao agente
6. validar se a sessão autenticada permaneceu ativa

### Evidência esperada
- viewer link funcionando
- interação humana possível
- sessão mantida após intervenção
- agente conseguindo continuar navegação

---

## Etapa 4 — teste de valor real
Depois do desbloqueio, validar se o agente consegue:
- acessar a área necessária
- navegar até a página relevante
- localizar os dados de interesse
- preparar caminho para extração futura

### Ponto importante
Se o LobsterLink só destravar login, mas o restante do fluxo continuar inviável, ele resolve apenas parte do problema.

---

## Critérios de sucesso
O piloto é considerado bem-sucedido se:
- a instalação funcionar sem quebrar o browser do agente
- o compartilhamento da aba funcionar
- o humano conseguir completar o bloqueio real
- a sessão autenticada continuar ativa depois
- o agente conseguir avançar no portal após o desbloqueio

---

## Critérios de falha
O piloto deve ser considerado falho ou inconclusivo se:
- a instalação adicionar fragilidade excessiva ao browser
- o viewer ficar instável ou preto de forma recorrente
- o portal continuar bloqueando mesmo após intervenção humana
- a sessão autenticada cair logo depois
- o problema principal não for resolvido pelo uso da ferramenta

---

## Checklist de teste
- [ ] fluxo alvo da Tokio Marine definido
- [ ] gargalo real identificado
- [ ] backup feito antes da instalação
- [ ] extensão instalada no browser isolado
- [ ] bridge validado
- [ ] aba compartilhada corretamente
- [ ] intervenção humana executada
- [ ] sessão autenticada mantida
- [ ] agente navegou depois do desbloqueio
- [ ] conclusão registrada: go / no-go / inconclusivo

---

## Rollback
Se o piloto não compensar:
1. remover flags/extensão do browser do OpenClaw
2. restaurar config anterior
3. reiniciar gateway/browser
4. validar que o browser voltou ao estado anterior
5. registrar o motivo do rollback

---

## Decisão final do piloto
Ao final, classificar como:
- **GO restrito** — aprovado apenas para Tokio Marine
- **GO ampliado** — aprovado para testar em outras seguradoras autenticadas
- **NO-GO** — não compensa manter
- **INCONCLUSIVO** — precisa de novo teste com fluxo melhor definido

---

## Recomendação atual
Minha recomendação hoje é:
- tratar LobsterLink como **piloto restrito para Tokio Marine**
- não elevar para padrão geral antes de validar o ganho real
- só ampliar se a sessão autenticada realmente destravar a navegação e a futura extração
