# Checklist padrão, mapeamento por seguradora

Objetivo: mapear de forma rápida e consistente como capturar o valor mensal de cada seguradora antes de automatizar.

## Como usar
Preencha um bloco por seguradora.
Se não souber algum campo, pode deixar em branco e eu completo depois na investigação.

---

## Template

### Seguradora
- nome:
- tipo de receita:
  - comissão sobre vendas
  - incentivo de venda
  - outro
- prioridade:
  - alta
  - média
  - baixa

### Origem do valor
- canal de acesso:
  - portal
  - planilha
  - PDF
  - email
  - outro
- URL ou caminho:
- nome da tela/relatório:
- formato final encontrado:
  - tela
  - PDF
  - XLSX
  - CSV
  - outro

### Como localizar o valor
- campo que representa o valor:
- como filtrar competência:
- filtro por data, competência ou período:
- precisa selecionar filial/corretora/produção?
- existe mais de um tipo de valor na mesma tela?
- regra para saber qual valor usar:

### Identificação
- match principal:
  - CNPJ
  - nome
  - código interno
  - outro
- nome como aparece no sistema:
- CNPJ como aparece no sistema:

### Acesso
- precisa login:
- precisa senha individual:
- tem 2FA ou captcha:
- observação de segurança:

### Automação
- classificação do fluxo:
  - A, alta automação
  - B, automação parcial
  - C, exceção/manual
- risco principal:
- recomendação inicial:
  - manual
  - semi-automático
  - automatizar cedo

### Observações livres
-

---

## Ordem recomendada para preencher primeiro
1. PORTO SEGUROS
2. BRADESCO CONSORCIO
3. ITAU CONSORCIO
4. SERVOPA

---

## Regra importante
Não enviar senhas em chat.
Se alguma credencial realmente precisar entrar no fluxo, ela deve ser guardada no servidor, de forma controlada, só depois do mapeamento do caso.
