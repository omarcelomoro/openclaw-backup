# Setup — Nano Banana Pro (Google Gemini Image Generation)

**Data:** 2026-04-22  
**Status:** ✅ Instalado e Pronto

---

## ✅ O Que Foi Feito

- [x] UV instalado (`~/.local/bin/uv`)
- [x] Skill criado (`~/.codex/skills/nano-banana-pro/`)
- [x] Script Python pronto (`generate_image.py`)
- [x] Help funcionando

---

## 📋 Próximo Passo: Google API Key

### Step 1: Obter Google API Key

1. Vá para **https://console.cloud.google.com**
2. Crie um novo projeto (ou use existente)
3. Na barra de pesquisa, procure por "Generative Language API"
4. Clique em "Enable"
5. Vá para **APIs & Services → Credentials**
6. Clique em **Create Credentials → API Key**
7. Copie a chave gerada

### Step 2: Configurar No Seu Sistema

```bash
# Adicione ao seu ~/.bashrc ou ~/.zshrc (permanente)
export GEMINI_API_KEY="sua-chave-aqui"

# Ou apenas para esta sessão:
export GEMINI_API_KEY="sua-chave-aqui"
```

### Step 3: Testar

```bash
python3 ~/.codex/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "Um pôr do sol sobre montanhas, cores vibrantes, estilo digital art" \
  --filename "test-image.png" \
  --resolution 1K \
  --api-key "sua-chave-aqui"
```

---

## 🎨 TESTE 1: Consórcio + Carta Contemplada

Você tem 5 prompts prontos. Vou gerar agora (precisa da API key):

### Imagem 1 — Hook (Slide 1)
```bash
python3 ~/.codex/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "Infográfico moderno mostrando dinheiro sendo comido por inflação. Estilo: minimalista, cores azul e branco, sem texto. Dimensão: 1080x1350 (Instagram portrait)" \
  --filename "2026-04-22-teste1-slide1-hook.png" \
  --resolution 1K
```

### Imagem 2 — Problema (Slide 2)
```bash
python3 ~/.codex/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "Tabela/gráfico comparando inflação vs renda fixa. Estilo: corporate clean, tons de azul, números grandes e legíveis. Sem texto descritivo, apenas visual puro. Dimensão: 1080x1350 (Instagram portrait)" \
  --filename "2026-04-22-teste1-slide2-problema.png" \
  --resolution 1K
```

### Imagem 3 — Alternativa (Slide 3)
```bash
python3 ~/.codex/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "Ícone de alvo com moedas ao redor, significando investimento direcionado. Estilo: moderno, flat design, cores Leevre (azul/branco/verde). Dimensão: 1080x1350 (Instagram portrait)" \
  --filename "2026-04-22-teste1-slide3-alternativa.png" \
  --resolution 1K
```

### Imagem 4 — Comparação (Slide 4)
```bash
python3 ~/.codex/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "Tabela lado a lado comparando Renda Fixa vs Consórcio. Colunas com checkmarks (✅) e X (❌). Estilo: clean, sans-serif, fácil leitura em mobile. Dimensão: 1080x1350 (Instagram portrait)" \
  --filename "2026-04-22-teste1-slide4-comparacao.png" \
  --resolution 1K
```

### Imagem 5 — CTA (Slide 5)
```bash
python3 ~/.codex/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "CTA visual: Botão grande com frase 'Saiba Como Funciona'. Logo Leevre em destaque. Cores: azul (botão) + branco (fundo). Design: mobile-first, botão grande e clicável visualmente. Dimensão: 1080x1350 (Instagram portrait)" \
  --filename "2026-04-22-teste1-slide5-cta.png" \
  --resolution 1K
```

---

## 🔄 Workflow Iterativo

Para cada imagem:

1. **Gerar DRAFT (1K):**
   ```bash
   python3 ~/.codex/skills/nano-banana-pro/scripts/generate_image.py \
     --prompt "seu prompt" \
     --filename "draft-v1.png" \
     --resolution 1K
   ```

2. **Revisar:** Você vê a imagem, gosta ou ajusta?

3. **Iterar (1K):**
   ```bash
   python3 ~/.codex/skills/nano-banana-pro/scripts/generate_image.py \
     --prompt "seu prompt AJUSTADO" \
     --filename "draft-v2.png" \
     --resolution 1K
   ```

4. **Final (2K) — Quando pronta:**
   ```bash
   python3 ~/.codex/skills/nano-banana-pro/scripts/generate_image.py \
     --prompt "seu prompt final" \
     --filename "final-production.png" \
     --resolution 2K
   ```

---

## 💰 Custo

- Cada draft (1K): ~$0.01
- Cada final (2K): ~$0.03
- Teste 1 (5 imagens): $0.05 (draft) + $0.15 (final) = **$0.20 total**

**vs DALL-E:** 5 imagens × $0.10 = $0.50
**Economia:** $0.30 (60% menos)

---

## 📍 Localização

- **Script:** `~/.codex/skills/nano-banana-pro/scripts/generate_image.py`
- **README:** `~/.codex/skills/nano-banana-pro/README.md`
- **Documentação:** `/home/marcelo/.openclaw/workspace/state/auditoria-nano-banana-pro-leevre-2026-04-22.md`

---

## 🎯 Próximo Passo

1. Obter Google API Key (5 min)
2. Exportar `GEMINI_API_KEY`
3. Rodar teste rápido (testar setup)
4. Gerar 5 imagens TESTE 1 (1h)
5. Revisar e iterar (1h)
6. Gerar finals em 2K (15 min)
7. Upload no Buffer (schedule terça)

---

## ⚡ Troubleshooting

**Erro: "No API key provided"**
```bash
# Check
echo $GEMINI_API_KEY

# Se vazio, set:
export GEMINI_API_KEY="sua-chave-aqui"
```

**Erro: "Authentication failed"**
- Verifique se a chave está correta (cópia exata)
- Verifique se "Generative Language API" está enabled no Google Console
- Tente criar uma nova chave

**Script não encontrado**
```bash
# Check
ls -la ~/.codex/skills/nano-banana-pro/scripts/generate_image.py

# Se não existe, rerun setup
```

---

## Ready?

Obtenha a Google API Key e manda que eu gero as 5 imagens!

```bash
export GEMINI_API_KEY="sua-chave-aqui"
# Pronto!
```
