# Instalação técnica — piloto LobsterLink para Tokio Marine

Data: 2026-04-19
Status: plano técnico
Escopo: piloto restrito

## Objetivo
Instalar e validar o LobsterLink de forma controlada no browser isolado do OpenClaw, com possibilidade clara de rollback, para testar uso no portal da Tokio Marine.

---

## Princípio
Esta instalação não é rollout geral.
É um experimento controlado, reversível e documentado.

---

## Fase 0 — antes de mexer

## Confirmar hipótese
Só seguir se o fluxo alvo da Tokio Marine realmente tiver algum destes bloqueios:
- login manual
- 2FA
- CAPTCHA
- validação humana pontual

Se o problema for só navegação ou parsing, pausar a instalação e testar primeiro com browser normal.

---

## Fase 1 — backup e baseline

## 1. Backup do workspace
```bash
cd /home/marcelo/.openclaw/workspace
git status --short
git add .
git commit -m "backup antes do piloto lobsterlink tokio" || true
git push origin master
```

## 2. Snapshot da config atual
Registrar a config antes de qualquer mudança:
```bash
cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.bak-lobsterlink-$(date +%F-%H%M%S)
```

## 3. Baseline do browser/gateway
```bash
openclaw gateway status
openclaw status
```

Objetivo:
- saber o estado anterior
- facilitar comparação depois

---

## Fase 2 — staging local da extensão

## 4. Baixar o repositório em área controlada
Sugestão de destino:
```bash
mkdir -p /home/marcelo/.openclaw/workspace/imports/browser-extensions
cd /home/marcelo/.openclaw/workspace/imports/browser-extensions
git clone https://github.com/davidguttman/lobsterlink.git
```

## 5. Definir caminho fixo da extensão
Usar o diretório clonado como fonte da extensão.
Evitar diretórios temporários, porque o browser precisa de caminho estável.

Exemplo esperado:
```bash
/home/marcelo/.openclaw/workspace/imports/browser-extensions/lobsterlink
```

---

## Fase 3 — inspeção antes da mudança

## 6. Inspecionar schema/config do browser
Antes de editar config, confirmar o formato correto dos campos:
- `browser`
- `browser.defaultProfile`
- `browser.extraArgs`

Regra:
- preservar o que já existe
- adicionar só o necessário

---

## Fase 4 — ativação controlada

## 7. Ajustar config do browser
Objetivo:
- garantir uso do perfil isolado `openclaw`
- carregar a extensão por `extraArgs`

Formato esperado:
```json
{
  "browser": {
    "defaultProfile": "openclaw",
    "extraArgs": [
      "--disable-extensions-except=/CAMINHO/ABSOLUTO/lobsterlink",
      "--load-extension=/CAMINHO/ABSOLUTO/lobsterlink"
    ]
  }
}
```

### Cuidados
- não apagar outros `extraArgs` úteis já existentes
- não usar caminho relativo
- não misturar com perfil `user`

---

## 8. Reiniciar serviço conforme necessário
Após mudança de config:
```bash
openclaw gateway restart
```

Se o browser estiver aberto, reiniciar o fluxo do browser isolado também.

---

## Fase 5 — verificação técnica da instalação

## 9. Validar browser isolado
Objetivo:
- confirmar que o Chromium do OpenClaw foi lançado com as flags da extensão
- confirmar que a extensão realmente carregou

Validar:
- `--disable-extensions-except=...lobsterlink`
- `--load-extension=...lobsterlink`
- presença de alvo `chrome-extension://...`
- bridge funcional

---

## 10. Descobrir Extension ID
Depois de carregada, descobrir o ID real da extensão e registrar.

Saída esperada:
```text
chrome-extension://<EXTENSION_ID>/bridge.html
```

---

## 11. Atualizar a skill runtime do LobsterLink
Atualizar a cópia usada em runtime para substituir placeholders por:
- bridge URL real
- extension id
- data de instalação
- status instalado

Objetivo:
- evitar reinstalação desnecessária
- permitir uso posterior no piloto

---

## Fase 6 — teste funcional com Tokio Marine

## 12. Abrir o portal alvo no browser isolado
Validar o fluxo real até o ponto de bloqueio.

## 13. Iniciar host da aba
Usar o bridge para compartilhar a aba correta.

## 14. Executar intervenção humana
Humano entra apenas para:
- login
- 2FA
- CAPTCHA
- passo manual específico

## 15. Validar continuidade
Depois da intervenção, confirmar:
- a sessão continua autenticada
- o agente consegue seguir navegando
- o fluxo avança até a área relevante

---

## Fase 7 — decisão

## GO restrito
Se:
- instalação estável
- sessão mantida
- desbloqueio humano útil
- navegação posterior possível

## NO-GO
Se:
- ganho pequeno
- instabilidade relevante
- sessão não se sustenta
- problema real não era autenticação

## INCONCLUSIVO
Se:
- teste não representou o fluxo real
- faltou clareza do dado que seria extraído
- houve bloqueio fora do escopo do LobsterLink

---

## Rollback técnico

## 1. Remover as flags da extensão da config
Remover:
- `--disable-extensions-except=...lobsterlink`
- `--load-extension=...lobsterlink`

## 2. Restaurar config anterior se necessário
```bash
cp ~/.openclaw/openclaw.json.bak-lobsterlink-AAAA-MM-DD-HHMMSS ~/.openclaw/openclaw.json
```

## 3. Reiniciar gateway
```bash
openclaw gateway restart
```

## 4. Validar retorno ao estado anterior
```bash
openclaw gateway status
openclaw status
```

## 5. Registrar motivo da reversão
Documentar se o rollback ocorreu por:
- instabilidade
- falta de ganho
- conflito com browser
- complexidade excessiva

---

## Checklist final de instalação
- [ ] hipótese do piloto confirmada
- [ ] workspace salvo e sincronizado
- [ ] config original copiada
- [ ] extensão clonada em caminho estável
- [ ] schema/config do browser revisados
- [ ] flags adicionadas sem quebrar args existentes
- [ ] gateway reiniciado
- [ ] extensão carregada no browser isolado
- [ ] extension id descoberto
- [ ] bridge URL validado
- [ ] skill runtime atualizada
- [ ] teste da Tokio Marine executado
- [ ] decisão final registrada
- [ ] rollback pronto se necessário

---

## Recomendação operacional
Não executar esta instalação em modo corrido.
Fazer em janela controlada, com tempo para:
- backup
- validação
- teste real
- reversão, se necessário
