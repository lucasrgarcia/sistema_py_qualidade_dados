# Qualidade de Dados em Ação (Python)

Este repositório contém um **pipeline automatizado em Python** que implementa um fluxo de **validação → classificação de falhas → melhoria de dados → revalidação → evidência de resultados antes e depois**.

> **Observação:** projeto demonstrativo para portfólio. Os dados são simulados e não representam informações reais.

---

## O que este projeto resolve

Em projetos de dados, é comum haver:
- **Valores duplicados** ou inconsistentes
- **Campos obrigatórios nulos**
- **Valores fora do domínio esperado**
- **Datas inválidas ou mal formatadas**
- **Falta de rastreabilidade** sobre a evolução da qualidade dos dados

Na prática, muitos processos apenas identificam erros pontuais, sem medir impacto ou acompanhar melhorias ao longo do tempo.

Este projeto transforma a validação de dados em um **processo padronizado**, mensurável e auditável.

---

## Visão geral do fluxo

1. **Geração ou ingestão dos dados**
   - Dataset tabular com problemas simulados de qualidade

2. O pipeline executa:
   - Validação automática de regras de qualidade
   - **Classificação das falhas por severidade** (ERROR / WARNING)
   - Geração de **relatório inicial** e logs

3. **Ações de melhoria de dados**
   - Remoção de duplicidades
   - Tratamento de valores fora do domínio
   - Padronização de campos
   - Conversão segura de datas inválidas

4. **Revalidação**
   - Execução das **mesmas regras** após as melhorias
   - Comparação objetiva dos resultados **antes e depois**

5. **Evidência e rastreabilidade**
   - Relatórios em CSV
   - Logs automáticos para auditoria

---

## Principais funcionalidades

- **Pipeline reutilizável** de validação de dados
- **Regras automatizadas** de qualidade (nulos, duplicados, domínio, datas)
- **Severidade de falhas** (ERROR / WARNING)
- **Comparação antes e depois** das ações corretivas
- **Relatórios em CSV** para histórico
- **Logging estruturado** para rastreabilidade
- Código organizado e fácil de evoluir

---

## Regras de qualidade implementadas

- **Valores nulos** em campos críticos
- **Intervalos de valores** (ex.: idade)
- **Duplicidade** de chaves e e-mails
- **Datas inválidas** ou mal formatadas
- Classificação de impacto das falhas

---

## Abordagem de melhoria contínua

O projeto segue a lógica de:
- Medir a qualidade dos dados
- Aplicar melhorias seguras onde possível
- Medir novamente usando os mesmos critérios

O critério de validação **não muda** entre as execuções.  
Apenas os dados são alterados.

Isso garante transparência e evita mascarar problemas estruturais dos dados.

---

## Resultados observados

Com a aplicação do pipeline, é possível observar:
- Eliminação de registros duplicados
- Correção de valores fora do domínio permitido
- Redução significativa de datas inválidas e valores nulos
- Identificação clara de problemas que exigem correção na origem dos dados

Os resultados ficam registrados em relatórios **antes e depois**, permitindo comparação objetiva.

---

## Estrutura do projeto

O projeto está organizado em um único arquivo Python contendo:
- Gerador de dados com erros simulados
- Contrato de validação padronizado
- Funções de validação reutilizáveis
- Pipeline de execução
- Funções de melhoria de dados
- Geração de relatórios e logs

Essa estrutura mantém o projeto simples, legível e alinhado a cenários reais.

---

## Tecnologias utilizadas

- **Python**
- **Pandas**
- **Logging (Python nativo)**
- **Relatórios em CSV**

---

## Como usar (modo demonstração)

1. Clone o repositório
2. Instale as dependências (pandas)
3. Execute o script principal em Python
4. O pipeline irá:
   - Gerar os dados
   - Executar a validação inicial
   - Aplicar melhorias
   - Reexecutar a validação
   - Salvar relatórios e logs

---

## Observações técnicas

- As ações corretivas são conservadoras e justificáveis
- Nem todo erro pode ser corrigido automaticamente
- Falhas remanescentes indicam problemas na origem dos dados
- O foco do projeto é **evidência de melhoria**, não limpeza agressiva

---

## Licença

Uso demonstrativo e educacional, desenvolvido para portfólio profissional.
