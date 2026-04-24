# Brevo — mapa operacional

**Papel:** envio de emails transacionais e, depois, marketing.
**Status atual:** API validada; sender `atendimento@leevrecorretora.com.br` ainda precisa de atenção em autenticação/SPF.

## Estado atual conhecido
- chave/API funcionando
- conta `marcelo@leevrecorretora.com.br` cadastrada
- sender `Livri <atendimento@leevrecorretora.com.br>` criado
- sender apareceu com `active: false` e `spfError: true`
- mesmo assim houve teste transacional com retorno `201`

## O que já temos
- capacidade técnica de envio via API
- indício de que o gargalo não é a chave, e sim identidade/autenticação do remetente

## O que falta
- corrigir autenticação/SPF do sender/domínio
- validar se o domínio/remetente fica realmente saudável
- decidir uso prioritário: transacional, marketing, ou ambos
- definir rotinas que realmente valem email automático

## Usos prováveis na Leevre
- relatórios
- follow-up comercial por email
- avisos operacionais
- campanhas simples

## Riscos
- disparar antes de autenticar bem domínio/remetente
- confundir “conseguiu enviar” com “está pronto para operar” 
- tentar resolver operação ruim com email bonito

## Próximo passo sugerido
Tratar SPF/DKIM/remetente como pendência operacional antes de aumentar volume.
