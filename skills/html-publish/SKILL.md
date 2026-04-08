# html-publish

Publica arquivos HTML no GitHub Pages sem intervenção do usuário.

## Quando usar

Sempre que gerar um novo HTML (roteiros, dashboard, relatório).

## Como executar

Usar exec com elevated=true para escrever o arquivo no host e publicar:

Passo 1 - escrever o arquivo HTML no servidor via exec elevated
Passo 2 - publicar com: livri-publish /root/.openclaw/workspace/cerebro/areas/marketing/NOME.html

## Notas

- Token GitHub em /root/.openclaw/.env como GITHUB_TOKEN
- Script livri-publish em /usr/local/bin/livri-publish
- Pages URL: https://omarcelomoro.github.io/leevre-pages/
- Usar R&#36; no lugar de R$ para evitar interpolação de shell
