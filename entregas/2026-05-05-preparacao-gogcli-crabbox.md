# Preparação técnica — gogcli + crabbox

Data: 2026-05-05
Responsável: Livri

## Estado atual verificado

### gogcli

- Binário encontrado: `/usr/local/bin/gog`
- Versão: `v0.14.0`
- Conta configurada: `marcelo@leevrecorretora.com.br`
- Status: instalado, mas autenticação bloqueada por keyring/senha.

Erro atual:

```text
read token for marcelo@leevrecorretora.com.br: read token: read encoded file keyring item: aes.KeyUnwrap(): integrity check failed.
```

Interpretação prática:

O gogcli está instalado e vê a conta, mas não consegue abrir o token salvo. Provável causa: `GOG_KEYRING_PASSWORD` diferente da senha usada quando o token foi salvo, ou entrada corrompida no keyring de arquivo.

### crabbox

- Binário encontrado: `/root/.local/bin/crabbox`
- Versão: `0.3.0`
- Pré-requisitos locais OK:
  - git
  - ssh
  - ssh-keygen
  - rsync
  - curl
  - chave SSH por lease
- Status: instalado, mas sem token Hetzner/broker configurado.

Erro atual:

```text
HCLOUD_TOKEN or HETZNER_TOKEN is required
missing hcloud token
```

Interpretação prática:

O crabbox está pronto no ambiente local, mas ainda não consegue criar/listar máquinas porque falta credencial de cloud/provedor ou login/broker apropriado.

---

# O que falta para ficar 100% operacional

## 1) gogcli — recuperar autenticação Google

Opções:

### Opção A — se soubermos a senha correta do keyring

Garantir que a variável esteja igual à senha original:

```bash
export GOG_KEYRING_PASSWORD='SENHA_CORRETA'
gog auth doctor --check
```

Se passar, testar:

```bash
gog auth list
gog gmail search 'newer_than:7d' --max 5 --json
```

### Opção B — reautenticar a conta

Se a senha do keyring foi perdida ou o token corrompeu, o caminho mais limpo é refazer OAuth:

```bash
gog auth add marcelo@leevrecorretora.com.br --services gmail,calendar,drive,contacts,sheets,docs
```

Depois validar:

```bash
gog auth doctor --check
```

Observação: isso pode abrir fluxo de autorização Google. Precisa de ação humana se pedir login/consentimento.

---

## 2) crabbox — configurar credencial ou login

### Caminho esperado com Hetzner

Definir token:

```bash
export HCLOUD_TOKEN='TOKEN_HETZNER'
# ou
export HETZNER_TOKEN='TOKEN_HETZNER'
```

Validar:

```bash
crabbox doctor
crabbox list
```

### Caminho broker/login, se aplicável

```bash
crabbox login
crabbox doctor
```

Se o ambiente pedir login interativo, precisa de confirmação humana.

---

# Próximo checkpoint recomendado

1. Corrigir gogcli primeiro, porque ele já tem conta corporativa configurada e libera Gmail/Drive/Sheets.
2. Depois configurar crabbox com token/login, porque ele depende de credencial de infraestrutura.
3. Só depois rodar testes reais ou automações que mexam com dados/infra.

---

# Segurança operacional

- Não salvar tokens em arquivos versionados.
- Não colar credenciais em chats se puder evitar.
- Preferir variáveis de ambiente ou secret manager.
- Confirmar antes de enviar e-mails, criar eventos ou disparar automações externas.
