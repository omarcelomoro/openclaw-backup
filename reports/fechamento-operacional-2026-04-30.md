# Fechamento Operacional — 30/04/2026

## Decisões do Marcelo

1. HubSpot: usar apenas um funil por enquanto, focado em Consórcio.
2. Descartar prioridade de pipeline separado de Seguros/Renovações por enquanto.
3. Fechar hoje a estrutura do funil comercial.
4. Fechar hoje pendências do Brevo.
5. Agger API fica para depois.
6. Resolver Google Sheets API/acesso hoje.
7. Livri usará apenas `atendimento@leevrecorretora.com.br`.
8. Bitwarden precisa ser explicado antes de qualquer decisão.

## Estado atual verificado

### HubSpot

- Token/API funcionando.
- Existe 1 pipeline: `Pipeline de negócios` (`default`).
- Etapas atuais:
  - Lead Recebido
  - Primeiro Contato
  - Simulação Enviada
  - Proposta Aceita
  - Contrato Assinado
  - Ganho
  - Perdido
- Propriedades customizadas atuais em Deal:
  - `consorcio_canal_detalhado`
  - `consorcio_mensagem_inicial`
  - `consorcio_origem_lead`
- Ainda existem deals de renovação de seguro no pipeline default, mas Marcelo decidiu descartar esse foco por enquanto.

### Brevo

- `BREVO_API_KEY` existe no `.env`, mas a API retorna `401 Key not found`.
- Status: chave inválida/revogada/truncada.
- Para fechar hoje: gerar nova API key Brevo e configurar domínio/sender.

### Google / Atendimento

- `atendimento@leevrecorretora.com.br` existe como conta padrão nos scripts.
- Tokens gogcli existem no servidor, mas falham com `aes.KeyUnwrap(): integrity check failed`.
- Na prática: acesso Google via CLI está quebrado até reautenticar/reimportar token com a senha correta do keyring.

## HubSpot — estrutura recomendada agora

Manter 1 pipeline: `Consórcio — Vendas`.

Etapas recomendadas:
1. Lead Recebido
2. Primeiro Contato
3. Diagnóstico / Qualificação
4. Simulação Enviada
5. Objeções
6. Road to Close
7. Proposta Aceita
8. Contrato Assinado
9. Ganho
10. Perdido

## Propriedades mínimas recomendadas

Deal:
- `consorcio_origem_lead`
- `consorcio_canal_detalhado`
- `consorcio_mensagem_inicial`
- `tipo_consorcio`
- `administradora`
- `valor_credito`
- `prazo_meses`
- `parcela_estimativa`
- `comissao_prevista`
- `produtor_responsavel`
- `temperatura_lead`
- `campo_objecoes`
- `road_to_close`
- `proximo_passo`
- `data_proximo_passo`
- `motivo_perda_consorcio`

Contact:
- `cpf_cnpj`
- `cidade_leevre`
- `estado_leevre`
- `perfil_cliente`
- `interesse_principal`
- `origem_primeiro_contato`

## Bitwarden — explicação curta

Bitwarden é um cofre de senhas. Self-hosted significa hospedar o cofre no próprio servidor da Leevre, em vez de usar o Bitwarden cloud.

Serve para guardar com segurança:
- senhas
- tokens/API keys
- acessos de sistemas
- credenciais da Livri
- credenciais compartilhadas da operação

Recomendação atual: não priorizar hoje. Primeiro fechar HubSpot, Brevo e Google access.
