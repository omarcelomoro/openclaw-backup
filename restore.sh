#!/bin/bash
# restore.sh — Restaura a Livri em uma nova VPS
# Uso: bash restore.sh
# Pré-requisitos: Node.js, npm, git, Docker

set -e

echo "🐝 Livri — Script de Restauração"
echo "================================="

# 1. Instala OpenClaw
echo "[1/6] Instalando OpenClaw..."
npm install -g openclaw

# 2. Clona o workspace
echo "[2/6] Clonando workspace do GitHub..."
REPO="https://github.com/omarcelomoro/openclaw-backup.git"
mkdir -p /home/marcelo/.openclaw
git clone "$REPO" /home/marcelo/.openclaw/workspace
echo "  ⚠️  Você precisará fornecer credenciais GitHub (token)"

# 3. Restaura openclaw.json
echo "[3/6] Configurando openclaw.json..."
cp /home/marcelo/.openclaw/workspace/openclaw.sanitized.json /home/marcelo/.openclaw/openclaw.json
echo "  ⚠️  Edite /home/marcelo/.openclaw/openclaw.json e substitua todos os REPLACE_ME"
echo "  Campos necessários:"
echo "    - auth.profiles.anthropic:default → ANTHROPIC_API_KEY"
echo "    - channels.telegram → TELEGRAM_BOT_TOKEN"
echo "    - tools.brave → BRAVE_API_KEY"

# 4. Cria .env com secrets
echo "[4/6] Criando .env (preencha manualmente)..."
cat > /home/marcelo/.openclaw/.env << 'EOF'
# Preencha com suas credenciais reais
ANTHROPIC_API_KEY=REPLACE_ME
TELEGRAM_BOT_TOKEN=REPLACE_ME
BRAVE_API_KEY=REPLACE_ME
EVOLUTION_API_KEY=REPLACE_ME
GITHUB_TOKEN=REPLACE_ME
EOF
chmod 600 /home/marcelo/.openclaw/.env
echo "  ⚠️  Edite /home/marcelo/.openclaw/.env com os valores reais"

# 5. Instala gogcli
echo "[5/6] Instalando gogcli..."
GOGCLI_VERSION="0.12.0"
curl -L "https://github.com/steipete/gogcli/releases/download/v${GOGCLI_VERSION}/gogcli_Linux_x86_64.tar.gz" -o /tmp/gogcli.tar.gz
tar -xzf /tmp/gogcli.tar.gz -C /tmp
mv /tmp/gogcli /usr/local/bin/gogcli
chmod +x /usr/local/bin/gogcli
echo "  ✅ gogcli instalado — rode: gogcli auth add marcelo@leevrecorretora.com.br"

# 6. Evolution API (WhatsApp)
echo "[6/6] Evolution API (WhatsApp)..."
echo "  Para restaurar o WhatsApp, veja /home/marcelo/.openclaw/workspace/memory/2026-03-27.md"
echo "  Docker Compose em: /home/marcelo/evolution/docker-compose.yml (não está no repo — recriar manualmente)"

echo ""
echo "================================="
echo "✅ Restauração base concluída!"
echo ""
echo "Próximos passos:"
echo "  1. Preencha /home/marcelo/.openclaw/.env com os secrets reais"
echo "  2. Edite openclaw.json (substitua REPLACE_ME)"
echo "  3. Execute: openclaw gateway start"
echo "  4. Reconecte Google: gogcli auth add marcelo@leevrecorretora.com.br"
echo "  5. Reconecte WhatsApp: gere novo QR code no Evolution API"
echo ""
echo "🐝 Livri estará de volta."
