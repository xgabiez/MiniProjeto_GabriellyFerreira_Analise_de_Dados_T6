# Mini Projeto Avaliativo - Análise de Dados com Python

## Objetivo

Este projeto tem como objetivo realizar uma Análise Exploratória
de Dados (AED) sobre uma base de dados de varejo, aplicando
técnicas de importação, limpeza, transformação e análise dos dados.

Este projeto faz parte da avaliação do Módulo 1 do curso de Análise de
Dados com Python, oferecido pelo SENAI por meio do programa SCTEC.

## Tecnologias utilizadas

- Python
- Pandas
- Git
- GitHub

## Base de dados

A base utilizada é a `Base Varejo.csv`, contendo registros de itens
comprados, clientes, produtos, categorias e datas.

## Sprint 1 - Importação dos dados

Foi realizada a importação da base `Base Varejo.csv` utilizando a
biblioteca Pandas.

A base possui:

- 830.000 registros
- 14 colunas

Também foram analisados os nomes e os tipos de dados das colunas.

Durante essa etapa foi identificado que o arquivo utiliza `;`
como separador das colunas.

## Sprint 2 - Transformação dos dados

Nesta etapa foram realizadas transformações e padronizações
nas colunas da base.

### Strings

As colunas de texto foram analisadas e padronizadas utilizando
métodos de string do Pandas, como `strip()` e `upper()`.

A coluna `PR_CAT` apresentava o valor `#N/D`, utilizado para
representar uma categoria ausente. Esse valor foi substituído
por `Sem Categoria`.

### Data

A coluna `DATA`, inicialmente identificada como texto, foi
convertida para o tipo `datetime`.

Após a conversão, não foram identificadas datas inválidas.

### Expressões regulares

Foi utilizada expressão regular para identificar possíveis
caracteres especiais nos nomes dos produtos.

Durante essa verificação foram encontrados registros com
`#N/D` na coluna `PR_NOME`, que serão avaliados na etapa
de limpeza dos dados.

## Sprint 3 - Limpeza de nulos e duplicatas

*Em desenvolvimento.*

## Sprint 4 - Estatística descritiva

*Em desenvolvimento.*

## Sprint 5 - Relatório e documentação

*Em desenvolvimento.*

## Sprint 6 - Versionamento

*Em desenvolvimento.*

## Insights e conclusões

*Serão adicionados após a conclusão da análise exploratória.*

## Reflexão teórica

### ETL

### Qualidade dos dados

