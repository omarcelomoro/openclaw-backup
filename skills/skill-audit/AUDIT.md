## 🔍 Relatório de Triagem — skill-audit

**Data:** 2026-04-06
**Fonte:** `skills/skill-audit/SKILL.md`
**Veredicto geral:** ⚠️ ATENÇÃO

### Resultados por categoria

| # | Categoria | Status | Achados |
|---|-----------|--------|---------|
| 1 | Prompt Injection | ✅ LIMPO | A skill menciona padrões de injection apenas como itens de detecção, não como instruções operacionais. |
| 2 | Exfiltração de Dados | ✅ LIMPO | Não há instruções para transmitir dados, chamar endpoints externos automaticamente ou coletar arquivos sensíveis. |
| 3 | Execução de Código | ⚠️ ATENÇÃO | Há referência a comando CLI do Snyk (`uvx snyk-agent-scan@latest --skills /path/to/SKILL.md`) como passo opcional de análise, mas não há instrução para executar automaticamente nem pipe-to-shell. |
| 4 | Credenciais/Segredos | ✅ LIMPO | Não há segredos hardcoded nem instruções para revelar credenciais. |
| 5 | Downloads/Dependências | ⚠️ ATENÇÃO | Há menção a ferramenta externa (`uvx snyk-agent-scan@latest`) e URL do Snyk Labs. É coerente com o propósito, mas depende de software/serviço de terceiros. |
| 6 | Acesso Financeiro | ✅ LIMPO | Nenhum indicador. |
| 7 | Conteúdo Ofuscado | ✅ LIMPO | Nenhum sinal de ofuscação, base64 operacional ou texto escondido. |
| 8 | Escopo/Permissões | ⚠️ ATENÇÃO | A skill recomenda escanear skills e citar ferramentas externas, o que é proporcional ao propósito. A ressalva é apenas manter claro que qualquer execução ou instalação externa continua sujeita à confirmação do usuário. |
| 9 | Engenharia Social | ✅ LIMPO | Não há urgência manipulativa, pressão para pular checagens ou linguagem de coerção. |

### Análise de contexto

A skill declara fazer auditoria de segurança de SKILL.md e o conteúdo realmente corresponde a esse objetivo. O escopo é proporcional: ela descreve categorias de risco, formato de relatório e limitações da triagem. O único cuidado é que o “próximo passo” sugere ferramentas externas de segunda camada; isso é aceitável, mas não deve ser tratado como execução implícita.

### Recomendação

⚠️ Aprovada com ressalvas — pode ser usada normalmente para triagem heurística de primeira camada. Só manter a regra operacional de que qualquer instalação, execução de scanner externo ou mudança derivada da auditoria precisa de confirmação antes.

### Próximo passo

Opcional, quando houver uma skill suspeita e você quiser análise mais forte:
→ Web: https://labs.snyk.io/experiments/skill-scan/
→ CLI: `uvx snyk-agent-scan@latest --skills /path/to/SKILL.md`
