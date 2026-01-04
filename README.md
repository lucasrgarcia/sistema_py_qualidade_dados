Visão Geral

Este projeto demonstra como a qualidade de dados pode ser tratada como um processo contínuo, e não apenas como uma verificação pontual.
A solução implementa um pipeline automatizado de validação de dados capaz de identificar problemas de qualidade, classificar falhas por impacto e medir objetivamente a evolução da qualidade dos dados ao longo do tempo.

O projeto foi desenvolvido para refletir cenários reais encontrados em ambientes corporativos, comuns em times de dados, BI e melhoria contínua.

Problema

Dados com baixa qualidade podem gerar análises incorretas, retrabalho constante, decisões equivocadas e perda de confiança nas informações.
Na prática, muitos projetos apenas apontam erros, sem mensurar impacto ou acompanhar melhorias.

Este projeto aborda esse problema ao tratar a qualidade dos dados como um processo mensurável e rastreável.

Solução

Foi criado um sistema automatizado de qualidade de dados que executa o seguinte fluxo:

Medição inicial da qualidade dos dados

Validação automatizada com regras reutilizáveis

Classificação das falhas por severidade

Aplicação de melhorias seguras onde possível

Revalidação usando os mesmos critérios

Comparação objetiva dos resultados antes e depois

Esse fluxo garante transparência e evita mascarar problemas estruturais dos dados.

Como Funciona

O pipeline executa validações automáticas, incluindo:

Verificação de valores nulos

Validação de intervalos de valores

Identificação de registros duplicados

Validação de datas inválidas

Classificação das falhas por severidade (ERROR e WARNING)

Após a validação inicial, são aplicadas ações corretivas simples e justificáveis, como remoção de duplicados, tratamento de valores fora do domínio, padronização de campos e conversão segura de datas.

Em seguida, o pipeline é executado novamente para medir o impacto dessas ações.

Abordagem de Melhoria Contínua

O projeto segue a lógica de medir, melhorar e medir novamente.
O critério de qualidade permanece o mesmo entre as execuções; apenas os dados são alterados.

Essa abordagem permite acompanhar a evolução da qualidade dos dados e identificar problemas que exigem correção na origem.

Resultados

Com a aplicação do pipeline, foi possível observar:

Eliminação de registros duplicados

Correção de valores fora do domínio permitido

Redução significativa de datas inválidas e valores nulos

Identificação clara de limitações estruturais nos dados de origem

Os resultados são registrados em relatórios CSV e logs automáticos, permitindo auditoria e acompanhamento histórico.

Estrutura do Projeto

O projeto está organizado em um único arquivo Python contendo:

Gerador de dados com erros simulados

Contrato de validação padronizado

Regras de validação reutilizáveis

Pipeline de execução

Funções de melhoria de dados

Relatórios antes e depois

Logging estruturado

Essa abordagem mantém o projeto simples, legível e fácil de evoluir.

Tecnologias Utilizadas

Python
Pandas
Logging (Python nativo)
Relatórios em CSV

Principais Aprendizados

Qualidade de dados deve ser tratada como processo contínuo

Nem todo erro pode ou deve ser corrigido automaticamente

Classificar falhas por severidade auxilia na priorização

Evidência de melhoria é mais importante do que apenas apontar erros

Simplicidade e clareza são fundamentais em projetos reais

Possíveis Evoluções

Configuração de regras via JSON ou YAML

Integração com orquestradores

Dashboards para acompanhamento histórico

Testes automatizados

Integração com bancos de dados
