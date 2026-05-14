# 🐛 Fix: Agentes Não Carregam Identidade Própria

**Data:** 2026-05-13  
**Status:** Identificado, aguardando aplicação

## Problema

Quando você pergunta ao Kotler ou Aristóteles, eles respondem com a personalidade da Livri (minha), não com as próprias.

## Causa Raiz

Ambos os agentes estão configurados com:
```
workspace: /home/marcelo/.openclaw/workspace
```

Isso faz eles carregarem **SOUL.md, IDENTITY.md, USER.md e AGENTS.md da Livri** em vez dos arquivos próprios!

## Estrutura Atual

**Aristóteles:**
- ✅ Tem workspace próprio completo: `/home/marcelo/.openclaw/workspace-aristoteles/`
- ❌ Config aponta para workspace errado: `/home/marcelo/.openclaw/workspace`

**Kotler:**
- ✅ Tem agentDir: `/home/marcelo/.openclaw/workspace/agents/kotler/`
- ✅ Agora tem todos os arquivos (acabei de criar USER.md, TOOLS.md, HEARTBEAT.md, MEMORY.md)
- ❌ Config aponta para workspace errado: `/home/marcelo/.openclaw/workspace`

## Solução

Precisa alterar a configuração dos agentes para:

**Aristóteles:**
```yaml
workspace: /home/marcelo/.openclaw/workspace-aristoteles
```

**Kotler:**
```yaml
workspace: /home/marcelo/.openclaw/workspace/agents/kotler
```

## Como Aplicar

### Opção 1: Via Dashboard Web (Recomendado)
1. Acesse o dashboard do Gateway: http://localhost:18789 (ou URL configurada)
2. Vá em Settings → Agents
3. Edite cada agente e ajuste o campo `workspace`

### Opção 2: Via CLI (Requer Comando Específico)
```bash
# Se houver comando para editar agente:
openclaw agent update aristoteles --workspace /home/marcelo/.openclaw/workspace-aristoteles
openclaw agent update kotler --workspace /home/marcelo/.openclaw/workspace/agents/kotler
```

### Opção 3: Edição Manual do Config (Última Opção)
Se o config estiver em arquivo acessível, edite diretamente. Mas o gateway pode sobrescrever na próxima reinicialização.

## Teste Após Aplicar

1. Reinicie o gateway se necessário:
```bash
openclaw gateway restart
```

2. Teste perguntando diretamente para cada agente:
```
/agent aristoteles "Quem é você?"
/agent kotler "Quem é você?"
```

3. Eles devem responder com as próprias identidades:
   - Aristóteles: "Sou Aristóteles 🦉, conselheiro estratégico..."
   - Kotler: "Sou Kotler 📈, agente de Marketing 360..."

## Arquivos Criados

Completei o workspace do Kotler com:
- ✅ `/home/marcelo/.openclaw/workspace/agents/kotler/USER.md`
- ✅ `/home/marcelo/.openclaw/workspace/agents/kotler/TOOLS.md`
- ✅ `/home/marcelo/.openclaw/workspace/agents/kotler/HEARTBEAT.md`
- ✅ `/home/marcelo/.openclaw/workspace/agents/kotler/MEMORY.md`

## Próximos Passos

1. Aplicar a correção de workspace via método escolhido
2. Reiniciar gateway
3. Testar identidade de cada agente
4. Confirmar que estão respondendo com personalidades próprias
