Qualidade de Dados em Ação (Python)

Este repositório contém um pipeline automatizado em Python para validação, monitoramento e melhoria contínua da qualidade de dados, com regras reutilizáveis, classificação de severidade e comparação de resultados antes e depois.

Observação: projeto demonstrativo para portfólio. Os dados são simulados e não representam informações reais.

O que este projeto resolve

Em projetos de dados, é comum encontrar problemas como:

Valores duplicados e inconsistentes

Campos obrigatórios ausentes

Valores fora do domínio esperado

Datas inválidas ou mal formatadas

Falta de visibilidade sobre a evolução da qualidade dos dados

Na prática, muitos fluxos apenas apontam erros, sem medir impacto ou acompanhar melhorias ao longo do tempo.

Este projeto transforma a validação de dados em um processo estruturado, mensurável e rastreável.

Visão geral do fluxo

Geração ou ingestão dos dados

Dataset tabular com problemas simulados de qualidade

Validação inicial (baseline)

Execução de regras automatizadas de qualidade

Classificação das falhas por severidade (ERROR / WARNING)

Geração de relatório e logs

Ações de melhoria

Aplicação de correções seguras e justificáveis

Sem mascarar problemas estruturais dos dados

Revalidação

Execução das mesmas regras após as melhorias

Comparação objetiva dos resultados antes e depois

Evidência e rastreabilidade

Relatórios CSV versionados

Logs automáticos para auditoria

Principais funcionalidades

Pipeline reutilizável de validação de dados

Regras automatizadas de qualidade (nulos, duplicados, domínio, datas)

Classificação de falhas por severidade (ERROR / WARNING)

Comparação antes e depois das ações corretivas

Geração de relatórios em CSV

Logging estruturado para auditoria e histórico

Código organizado e fácil de evoluir

Regras de qualidade implementadas

Verificação de valores nulos em campos críticos

Validação de intervalo de valores (ex.: idade)

Identificação de duplicidade de chaves e e-mails

Validação de datas inválidas

Classificação do impacto das falhas

Abordagem de melhoria contínua

O projeto segue a lógica de:

Medir → Melhorar → Medir novamente

O critério de qualidade permanece o mesmo entre as execuções.
Apenas os dados são alterados.

Isso permite:

Medir impacto real das correções

Acompanhar a evolução da qualidade dos dados

Identificar problemas que precisam ser corrigidos na origem

Resultados observados

Com a aplicação do pipeline, é possível observar:

Eliminação de registros duplicados

Correção de valores fora do domínio permitido

Redução significativa de datas inválidas e valores nulos

Identificação clara de limitações estruturais nos dados de entrada

Os resultados ficam registrados em relatórios antes e depois, permitindo comparação objetiva.

Estrutura do projeto

O projeto está organizado em um único arquivo Python contendo:

Gerador de dados com erros simulados

Contrato de validação padronizado

Funções de validação reutilizáveis

Pipeline de execução

Funções de melhoria de dados

Geração de relatórios e logs

Essa abordagem mantém o projeto simples, legível e alinhado a cenários reais.

Tecnologias utilizadas

Python

Pandas

Logging (Python nativo)

Relatórios em CSV

Como executar (modo demonstração)

Clone o repositório

Instale as dependências (pandas)

Execute o script principal em Python

O pipeline irá:

Gerar os dados

Executar a validação inicial

Aplicar melhorias

Reexecutar a validação

Salvar relatórios e logs

Observações técnicas

As ações corretivas são intencionais e conservadoras

Nem todo erro é corrigido automaticamente

Falhas remanescentes indicam problemas na origem dos dados

O projeto prioriza clareza e rastreabilidade em vez de “limpeza agressiva”

Licença

Projeto desenvolvido para fins educacionais e de portfólio.
