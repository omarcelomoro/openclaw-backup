# Mapeamento, PORTO SEGUROS

Data: 2026-04-14

## Seguradora
- nome: PORTO SEGUROS
- tipo de receita: comissão sobre vendas
- prioridade: alta

## Origem do valor
- canal de acesso: portal
- URL base sanitizada: `https://corretor.portoseguro.com.br/`
- tela/relatório principal validada: `COMISSÕES - NOTA FISCAL ELETRÔNICA`
- formato final encontrado: tela com geração de relatório
- observação: o link enviado continua parecendo sessionizado, então deve ser tratado só como referência de navegação, não como URL fixa de automação

## Como localizar o valor
- susep/favorecida exibida: `31340J`
- filtro principal: `Mês`
- filtro adicional: `Filial`
- ação principal: `Gerar relatório`
- competência: usar sempre o mês anterior
- janela operacional: as notas podem ser geradas até o 5º dia do mês subsequente
- leitura operacional atual: abrir a tela de nota fiscal eletrônica, selecionar mês e filial corretos, gerar relatório e capturar o valor-base da nota

## Identificação
- match principal recomendado: nome + CNPJ
- nome fiscal validado na emissão: `PORTO SEGURO COMPANHIA DE SEGUROS GERAIS`
- CNPJ fiscal validado: `61.198.164/0015-65`

## Acesso
- precisa login: sim
- precisa senha individual: a confirmar
- tem 2FA/captcha: não
- observação de segurança: o link enviado no chat parece sessionizado e contém dados sensíveis, então não deve ser tratado como URL permanente nem copiado para documentação operacional bruta

## Automação
- classificação inicial do fluxo: A/B
- complexidade: média
- risco principal: deep link com sessão expirada ou parâmetros temporários do portal, além de possível variação do relatório por filial
- recomendação inicial: semi-automático com forte chance de virar fluxo padronizado cedo

## Leitura operacional
Este é um bom candidato para virar fluxo padronizado cedo, mas o ponto certo é automatizar a navegação a partir do portal/base de login, e não depender do link profundo com parâmetros de sessão.

## Relatório validado
- saída atual: página web/relatório HTML em `wwws.portoseguro.com.br/notaeletronica/exibirrelatorionotafiscal.do`
- mês de referência exibido: `03/2026`
- filial/CNPJ exibido: `41606205/0001-00`
- susep exibida: `31340J`
- empresa exibida: `PORTO SEGURO CIA DE SEGUROS GERAIS`
- campo principal para preencher `valor_nota`: `VALOR BRUTO`
- exemplo validado: `VALOR BRUTO = R$ 16.002,71`
- retenções exibidas separadamente: `ISS`, `IR`, `INSS`
- valor líquido exibido: `VALOR LÍQUIDO = R$ 15.682,66`
- conclusão operacional: para emissão da NF da Leevre, usar o `VALOR BRUTO`, não o líquido
- conclusão estrutural: o relatório já traz um valor consolidado, sem necessidade de somar linhas na tela principal

## Próximos dados que faltam
- confirmar se existe versão exportável do relatório além da tela HTML
- confirmar se a filial padrão será sempre `41606205/0001-00` ou se pode variar por operação
