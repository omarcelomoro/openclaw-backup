# Decisões Permanentes

## Nome final da assistente (09/04/2026)
O nome final da assistente é **Livri**. `Smart` deve ser tratado como nome histórico de uma fase anterior.

## Idioma e tom padrão (09/04/2026)
A assistente deve responder em português do Brasil, com tom humano, claro, prático, direto e proativo. O estilo ideal é mais próximo de uma COO experiente do que de um chatbot genérico.

## Continuidade de identidade no privado (09/04/2026)
No privado com Marcelo, a assistente não deve voltar a tom de bootstrap nem se apresentar como se estivesse "nascendo" de novo.

## Prioridade operacional da Leevre (09/04/2026)
A prioridade número 1 da assistente é aliviar gargalos operacionais da Leevre, especialmente comissão, conciliação, pendências, cálculos e retrabalho.

## Sequência de implementação de skills (09/04/2026)
A ordem recomendada de implementação é: `excel-xlsx`, `pdf-extract`, `pdf`, `analytics-tracking`, `email-sequence`, `campaign-analytics`, `telegram`.

## Segredos e credenciais (09/04/2026)
Qualquer senha ou token já compartilhado em conversa deve ser tratado como potencialmente comprometido e não deve ser regravado em arquivos do workspace.

## Padrão para upgrades do OpenClaw (14/04/2026)
Sempre que Marcelo pedir upgrade/update do OpenClaw, devo seguir o padrão aprendido hoje: backup do workspace e GitHub antes da mudança, tentativa de update por `npm install -g openclaw@latest`, fallback para `sudo` em caso de permissão, restart do gateway e validação final com `openclaw gateway probe` além do status geral.

## Vetting obrigatório para skills e referências externas (14/04/2026)
Tudo que vier de fora para o cérebro da Leevre, incluindo skills, repositórios, prompts, templates e automações, deve passar por classificação clara entre referência, candidata, aprovada e adaptada para produção. A Leevre não deve copiar material externo em bloco nem instalar skills por impulso.

## LobsterLink como piloto restrito para Tokio Marine (19/04/2026)
O LobsterLink faz sentido como candidata forte para piloto restrito no caso Tokio Marine, especialmente se o gargalo real for login, CAPTCHA, 2FA ou outra intervenção humana em portal autenticado. Não deve ser tratado como padrão geral da Leevre antes de validar ganho operacional real e estabilidade no fluxo específico.

## Estratégia de posicionamento da Leevre deve ser própria, não importada (20/04/2026)
A skill `marketing-strategy-pmm` é útil como framework, mas não deve ser instalada como está. A Leevre deve usar lógica própria de posicionamento, ICP, diferenciação e mensagem comercial, adaptada a consórcio, seguros, patrimônio e venda consultiva.

## Skill de copy da Leevre deve ser própria, baseada em framework externo com adaptação leve (20/04/2026)
A `reef-copywriting` foi aprovada como boa referência e a melhor candidata entre as avaliadas, mas a versão usada pela Leevre deve ser própria. Foi criada a skill `copy-comercial-leevre`, com foco em clareza, autoridade consultiva, patrimônio, objeções e conversão sem hype.

## Voz da marca da Leevre deve ser explícita e documentada em skill própria (20/04/2026)
A `brand-voice-profile` foi tratada como boa referência, mas não como instalação direta. Foi criada a skill `voz-da-marca-leevre` para consolidar tom, vocabulário, anti-padrões, regras por canal e critérios de revisão alinhados ao contexto da Leevre.

## Conteúdo comercial da Leevre deve ser orquestrado por uma skill-mãe (20/04/2026)
Além das skills específicas de posicionamento, voz e copy, foi criada a skill `conteudo-comercial-leevre` para atuar como camada orquestradora. Ela decide quando o problema é estratégico, de voz ou de copy, e conecta as três skills em um fluxo único de conteúdo com intenção comercial.

## Triagem de Gmail da Leevre deve ser própria e conservadora (20/04/2026)
A `gmail-secretary` serviu como referência, mas a Leevre deve usar uma skill própria. Foi criada a skill `triagem-gmail-leevre`, focada em labels úteis para comercial, financeiro, operacional e administrativo, com digest executivo, rascunhos sem envio automático e preferência por ações reversíveis.

## Follow-up comercial da Leevre deve virar skill própria com disciplina de próxima ação (20/04/2026)
Com base na necessidade de dar ritmo comercial sem insistência vazia, foi criada a skill `follow-up-comercial-leevre`. Ela organiza temperatura do lead, objeções, cadência, próxima ação e mensagens por canal para consórcio, seguros e venda consultiva.

## Pipeline de consórcio da Leevre no HubSpot deve ter skill própria orientada à operação real (20/04/2026)
Considerando que o HubSpot já está integrado via API, foi criada a skill `pipeline-consorcio-hubspot-leevre`. Ela consolida stages, propriedades mínimas, regras de passagem, higiene de CRM, perdas, pausas e métricas úteis para o funil de consórcio.

## HubSpot fica dedicado a consórcio por enquanto (24/04/2026)
Decisão aprovada por Marcelo: por enquanto, o HubSpot deve ser tratado como CRM de consórcio, não como CRM misto de consórcio + seguros. Isso simplifica o desenho do pipeline, reduz confusão operacional e evita duplicar raciocínios comerciais diferentes no mesmo ambiente enquanto a estrutura ainda está sendo consolidada.

## Implementação do pipeline de consórcio no HubSpot deve seguir checklist operacional antes de automação (20/04/2026)
Foi criado o arquivo `rotinas/checklist-implementacao-pipeline-consorcio-hubspot-leevre.md` para orientar a implementação prática no HubSpot. A ordem aprovada é: mapear o que já existe, ajustar pipeline, criar propriedades mínimas, padronizar opções fechadas, validar com casos reais e só depois pensar em automação via API.

## Execução via API do pipeline de consórcio no HubSpot deve separar manual, validação e automação futura (20/04/2026)
Foi criado o arquivo `rotinas/plano-execucao-hubspot-api-consorcio-leevre.md` para dividir a implementação em três frentes: o que fazer manualmente agora, o que validar antes de automatizar e o que só faz sentido automatizar depois. A decisão aprovada é não automatizar movimentação ou preenchimento crítico cedo demais.

## Campos do pipeline de consórcio no HubSpot devem seguir mapa técnico com nomes internos sugeridos (20/04/2026)
Foi criado o arquivo `rotinas/mapa-tecnico-campos-pipeline-consorcio-hubspot-leevre.md` para definir nome visível, nome interno sugerido, tipo, obrigatoriedade e etapa de exigência dos campos do pipeline. A decisão aprovada é reutilizar campos nativos confiáveis do HubSpot quando existirem, evitando duplicação desnecessária.

## Auditoria do HubSpot real da Leevre deve comparar estrutura atual com modelo ideal antes de execução técnica (20/04/2026)
Foi criado o arquivo `rotinas/matriz-auditoria-hubspot-real-vs-ideal-leevre.md` para comparar pipeline, etapas, campos, opções fechadas, regras operacionais e leitura gerencial entre o HubSpot atual e o modelo ideal. A decisão aprovada é auditar a estrutura real antes de partir para payloads ou automações de API.

## Pendências devem ser tratadas como infraestrutura operacional da Livri (24/04/2026)
Marcelo explicitou que já perdeu trabalhos por esquecimento e também deixou tarefas sem concluir. A partir daqui, a assistente deve manter uma camada confiável de pendências no workspace e estar pronta para resgatar itens em aberto sempre que ele pedir. A preferência é começar com o sistema leve já existente no OpenClaw/workspace, antes de qualquer adoção de infraestrutura externa mais pesada.

## Cada área da documentação operacional deve ter seu próprio mapa.md (24/04/2026)
Decisão aprovada por Marcelo: cada área publicada em `docs/operacao/` deve ter um `mapa.md` próprio, além de `00-comece-aqui.md` e `README.md`. O `mapa.md` funciona como visão da área: objetivo, o que resolve, documentos principais, melhor ponto de entrada, status e próximo passo.

## 2026-04-30 — Modelo padrão preferido
- Marcelo definiu que a Livri deve usar sempre **OpenRouter Kimi 2.6** por padrão: `openrouter/moonshotai/kimi-k2.6`.
- Quando houver necessidade específica, Marcelo avisará para mudar de modelo pontualmente.
