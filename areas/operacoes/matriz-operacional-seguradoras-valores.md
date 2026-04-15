# Matriz operacional, seguradoras e captura de valores

Data base: 2026-04-14

## Objetivo
Organizar a coleta dos valores mensais por seguradora/tomador antes de pedir credenciais e antes de automatizar emissão em lote.

A lógica correta é:
1. mapear a origem do valor
2. classificar o tipo de fluxo
3. identificar exceções
4. só então decidir se precisa de login e senha

---

## Tipos de fluxo

### Tipo A, alta automação
- valor sai de relatório exportável ou tela padronizada
- mesma navegação todo mês
- baixa ambiguidade de competência
- bom candidato para automação cedo

### Tipo B, automação parcial
- portal existe, mas há pequenas variações
- exige conferência humana antes de lançar
- bom candidato para preenchimento semi-automático

### Tipo C, exceção/manual
- fluxo muda muito
- campo do valor não é padronizado
- depende de interpretação
- deve ficar fora do primeiro lote de automação

---

## Matriz inicial

| Tomador | Tipo de receita | Origem do valor | Formato esperado | Match principal | Precisa login? | Tipo de fluxo | Complexidade | Status de mapeamento | Prioridade | Observações |
|---|---|---|---|---|---|---|---|---|---|---|
| ALLIANZ | comissão sobre vendas | portal, tela `Gestão > Financeiro > Extrato de Comissões` | tela/relatório | CNPJ + nome | sim | B | média | mapeado | média | usar bloco `Comissões Pagas`, filtrar período do mês anterior, usar `Total Bruto` como `valor_nota`, não `Total Líquido`, ver `areas/operacoes/mapeamento-allianz.md` |
| ANADEM | comissão sobre vendas | site/portal da seguradora | tela ou relatório | CNPJ + nome | a confirmar | B | média | não mapeado | média | confirmar origem mensal do valor |
| BANESTES | comissão sobre vendas | portal, tela `Comissões - EXTRATO DE PAGAMENTOS` | tela/relatório por período | CNPJ + nome | sim | B | média | mapeado | média | filtrar data inicial e final do mês anterior, notas até o 5º dia do mês subsequente, usar total de `Valor Base` como `valor_nota`, não `Valor Pago`, ver `areas/operacoes/mapeamento-banestes.md` |
| BRADESCO CONSORCIO | comissão sobre vendas | site/portal da seguradora | tela ou relatório | CNPJ + nome | a confirmar | A/B | média | não mapeado | alta | já existe histórico de emissão fiscal |
| BRADESCO SEGUROS | comissão sobre vendas | portal, tela `Auto > Comissões > Extrato de Comissões` | tela/relatório com cards consolidados | CNPJ + nome | sim | B | média | mapeado | média | usar card `Comissões` como `valor_nota`, não `Crédito líquido`, separar de Bradesco Consórcio, ver `areas/operacoes/mapeamento-bradesco-seguros.md` |
| HDI | comissão sobre vendas | portal, tela `Adm > Relatórios > Comissões` | tela/relatório com totalizador | CNPJ + nome | sim | B | média | mapeado | média | filtrar período do mês anterior, clicar `Visualizar`, usar total de `Vlr. Bruto` como `valor_nota`, não `Líquida`, ver `areas/operacoes/mapeamento-hdi.md` |
| ICATU | comissão sobre vendas | site/portal da seguradora | tela ou relatório | CNPJ + nome | a confirmar | B | média | não mapeado | média | confirmar se existe extrato mensal |
| ITAU CONSORCIO | comissão sobre vendas | site/portal da seguradora | tela ou relatório | CNPJ + nome | a confirmar | A/B | média | não mapeado | alta | bom candidato se houver extrato consistente |
| MAPFRE | comissão sobre vendas | site/portal da seguradora | tela ou relatório | CNPJ + nome | a confirmar | B | média | não mapeado | média | validar se precisa consulta por período |
| PORTO SEGUROS | comissão sobre vendas | portal, tela `COMISSÕES - NOTA FISCAL ELETRÔNICA` | tela/relatório HTML | CNPJ + nome | sim | A | média | mapeado | alta | susep `31340J`, filtros `Mês` e `Filial`, ação `Gerar relatório`, usar `VALOR BRUTO` como `valor_nota`, relatório já traz valor consolidado, ver `areas/operacoes/mapeamento-porto-seguros.md` |
| SERVOPA | comissão sobre vendas | site/portal da seguradora | tela ou relatório | CNPJ + nome | a confirmar | A/B | média | não mapeado | alta | há também linha separada de incentivo |
| SERVOPA | incentivo de venda | site/portal da seguradora | tela ou relatório | CNPJ + nome + tipo de receita | a confirmar | B/C | média/alta | não mapeado | média | precisa separar incentivo de comissão comum |
| SOMPO | comissão sobre vendas | site/portal da seguradora | tela ou relatório | CNPJ + nome | a confirmar | B | média | não mapeado | média | validar formato do extrato |
| TOKIO | comissão sobre vendas | site/portal da seguradora | tela ou relatório | CNPJ + nome | a confirmar | B | média | não mapeado | média | confirmar recorrência mensal |
| YELLUM | comissão sobre vendas | site/portal da seguradora | tela ou relatório | CNPJ + nome | a confirmar | B/C | média | não mapeado | média | confirmar se é portal ou envio externo |

---

## Ordem recomendada de automação

### Lote 1, primeiro bloco para mapear
Prioridade mais alta por potencial de repetição e impacto:
1. PORTO SEGUROS
2. BRADESCO CONSORCIO
3. ITAU CONSORCIO
4. SERVOPA, comissão

### Lote 2, depois que o padrão estiver firme
5. BRADESCO SEGUROS
6. ALLIANZ
7. HDI
8. MAPFRE
9. TOKIO
10. ICATU

### Lote 3, exceções e variações
11. ANADEM
12. BANESTES
13. SOMPO
14. YELLUM
15. SERVOPA, incentivo de venda

---

## Regra de credenciais

Não pedir todas as credenciais antes.

Pedir só quando houver:
- fluxo confirmado
- necessidade real de login
- prioridade aprovada
- local seguro no servidor para guardar

### Decisão prática
- se a seguradora tiver relatório exportável sem fricção, mapear primeiro
- se o portal for instável ou cheio de exceção, deixar para depois
- se duas seguradoras tiverem fluxo parecido, padronizar juntas

---

## Dados que precisamos levantar por seguradora

Para cada uma, preencher:
- URL exata do portal
- nome da tela ou relatório
- campo que contém o valor
- como filtrar competência
- se existe exportação CSV/XLSX/PDF
- se precisa login individual
- se tem 2FA/captcha
- nome do valor no sistema, por exemplo comissão, incentivo, repasse, produção
- se o match fiscal final será por nome ou CNPJ

---

## Melhor próximo passo

Em vez de mandar todas as senhas, o caminho certo é:
1. escolher 1 seguradora do lote 1
2. mapear o fluxo inteiro dela
3. classificar o padrão
4. repetir nas próximas parecidas

Isso reduz risco, retrabalho e exposição de credenciais.

Checklist de apoio:
- `areas/operacoes/checklist-mapeamento-seguradora.md`
