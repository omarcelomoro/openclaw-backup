# Runbook — update, backup e rollback do OpenClaw na Leevre

Data: 2026-04-14
Status: ativo

## Objetivo
Padronizar updates do OpenClaw com segurança, backup e validação real.

## Regra principal
Antes de qualquer update:
1. validar estado do workspace
2. fazer backup local
3. garantir backup no GitHub
4. só então atualizar

---

## Sequência padrão

## 1. Validar Git e estado do workspace
```bash
cd /home/marcelo/.openclaw/workspace
git branch --show-current
git status --short
git remote -v
```

### Esperado
- branch conhecida
- remoto GitHub configurado
- entender se há mudanças pendentes

---

## 2. Fazer backup do workspace
Se houver mudanças:
```bash
cd /home/marcelo/.openclaw/workspace
git add .
git commit -m "backup antes do update"
git push origin master
```

Se não houver mudanças, ainda assim validar que o remoto está sincronizado.

---

## 3. Rodar update
Primeira tentativa:
```bash
npm install -g openclaw@latest
```

Se der erro de permissão (`EACCES`), usar:
```bash
sudo npm install -g openclaw@latest
```

---

## 4. Reiniciar o gateway
```bash
openclaw gateway restart
```

---

## 5. Validar serviço e versão
```bash
openclaw gateway status
openclaw status
openclaw gateway probe
```

### O que observar
- versão nova refletida no CLI e no gateway
- service rodando
- probe local com connect/rpc ok
- canais principais sem erro

### Regra importante
Se `openclaw status` trouxer timeout, mas `openclaw gateway probe` vier ok e os canais estiverem funcionando, tratar como possível inconsistência do status geral, não como falha imediata do gateway.

---

## 6. Fechar update só depois da validação real
Considerar update concluído apenas se:
- CLI atualizado
- gateway reiniciado
- `openclaw gateway probe` ok
- canal principal operacional

---

## Troubleshooting rápido

## Caso 1 — `npm install -g` deu `EACCES`
### Leitura
Permissão insuficiente para mexer em `/usr/lib/node_modules`

### Ação
```bash
sudo npm install -g openclaw@latest
```

---

## Caso 2 — `openclaw status` mostra gateway unreachable
### Ação
Rodar:
```bash
openclaw gateway status
openclaw gateway probe
```

### Interpretação
- se `gateway status` e `probe` estiverem ok, provavelmente não é quebra real
- se `probe` falhar, aí sim investigar logs

---

## Caso 3 — gateway não sobe certo
### Ação
```bash
openclaw gateway restart
openclaw gateway status
openclaw logs --follow
```

---

## Caso 4 — warnings após update
### Exemplos já vistos
- `config.modelFallbackPolicy is deprecated`
- `qmd binary unavailable`

### Leitura
Nem todo warning é incidente. Separar:
- warning cosmético/configuracional
- falha operacional real

---

## Checklist final
- [ ] workspace validado
- [ ] backup local feito
- [ ] GitHub sincronizado
- [ ] update executado
- [ ] gateway reiniciado
- [ ] `openclaw gateway status` ok
- [ ] `openclaw status` revisado
- [ ] `openclaw gateway probe` ok
- [ ] canal principal validado

---

## Aprendizado consolidado em 14/04/2026
O padrão correto de update da Leevre/Livri passa por:
- backup antes
- push antes
- update com fallback para `sudo` se necessário
- restart do gateway
- validação real com `openclaw gateway probe`

Sem esse ritual, o risco de falsa sensação de update concluído aumenta.
