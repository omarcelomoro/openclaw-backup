# Auditoria gogcli — 2026-05-05

## Resumo executivo

O `gogcli` foi auditado e atualizado com sucesso.

- Versão anterior: `v0.14.0 (469f4b4 2026-04-28T09:39:03Z)`
- Versão instalada agora: `v0.15.0 (e0338d5 2026-05-05T05:50:19Z)`
- Binário ativo: `/usr/local/bin/gog`
- Backup do binário anterior: `/usr/local/bin/gog.bak.20260505T085442Z`
- Checksum do pacote Linux AMD64: validado com `checksums.txt` oficial da release

## Fonte usada

Repositório oficial informado por Marcelo:

https://github.com/steipete/gogcli

Release mais recente no momento da instalação:

https://github.com/steipete/gogcli/releases/tag/v0.15.0

Pacote instalado:

`gogcli_0.15.0_linux_amd64.tar.gz`

Checksum validado:

```text
bfa2a9c8092bd329db89aa100f8074a3f14251e3db716b927627793e47148c9d  gogcli_0.15.0_linux_amd64.tar.gz
```

Resultado:

```text
gogcli_0.15.0_linux_amd64.tar.gz: OK
```

## Estado técnico atual

Comando:

```bash
gog --version
```

Resultado:

```text
v0.15.0 (e0338d5 2026-05-05T05:50:19Z)
```

## Autenticação Google

O binário está instalado e funcional, mas a autenticação OAuth salva ainda não está utilizável.

Conta OAuth armazenada:

```text
marcelo@leevrecorretora.com.br
```

Erro:

```text
read token: read encoded file keyring item: aes.KeyUnwrap(): integrity check failed.
```

Diagnóstico:

O token existe no keyring, mas não pode ser descriptografado. Causa provável:

1. `GOG_KEYRING_PASSWORD` diferente da senha usada ao criar o token; ou
2. entrada de token corrompida; ou
3. troca de backend/ambiente de keyring.

O `gog auth doctor --check` confirmou:

```text
ok config.path /root/.config/gogcli/config.json
ok keyring.backend auto
ok keyring.dir /root/.config/gogcli/keyring
ok keyring.open opened
error token.default.marcelo@leevrecorretora.com.br aes.KeyUnwrap(): integrity check failed
ok tokens 0 readable OAuth tokens of 1 stored token account
status error
```

## Observação importante

O `gog auth status --json` mostrou conta preferida como:

```text
atendimento@leevrecorretora.com.br
```

Mas o token armazenado encontrado é de:

```text
marcelo@leevrecorretora.com.br
```

Isso precisa ser conferido antes de automações, para evitar rodar comandos com a conta errada.

## Próxima ação necessária

Para deixar 100% operacional, falta revalidar a autenticação.

### Caminho A — se souber a senha correta do keyring

```bash
export GOG_KEYRING_PASSWORD='SENHA_CORRETA'
gog auth doctor --check
```

Depois testar leitura segura:

```bash
gog gmail search 'newer_than:7d' --max 5 --json --no-input
```

### Caminho B — se não souber a senha ou token estiver corrompido

Refazer OAuth:

```bash
gog auth add marcelo@leevrecorretora.com.br --services gmail,calendar,drive,contacts,sheets,docs
```

ou, se a conta correta for atendimento:

```bash
gog auth add atendimento@leevrecorretora.com.br --services gmail,calendar,drive,contacts,sheets,docs
```

## Recomendações de uso seguro

- Para automações de leitura: usar `--json --no-input`.
- Para Gmail, manter `--gmail-no-send` quando o objetivo não for envio.
- Confirmar manualmente antes de enviar e-mails, criar eventos ou alterar arquivos no Drive/Sheets.
- Padronizar a conta usada via variável:

```bash
export GOG_ACCOUNT='conta@leevrecorretora.com.br'
```

- Não salvar senha/tokens em arquivos versionados.
