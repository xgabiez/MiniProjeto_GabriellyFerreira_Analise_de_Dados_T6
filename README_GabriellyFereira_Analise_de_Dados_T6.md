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

Nesta etapa foram realizadas análises e tratamentos relacionados à qualidade dos dados, 
incluindo a identificação de valores nulos, colunas completamente vazias, registros duplicados 
e valores ausentes representados por `#N/D`.

### Valores nulos e colunas vazias

Inicialmente, foi realizada a verificação da quantidade de valores nulos em cada coluna.

Durante essa análise, foram identificadas quatro colunas (`Unnamed: 10`, `Unnamed: 11`, `Unnamed: 12` e `Unnamed: 13`) 
que não possuíam nenhum valor preenchido. Essas colunas foram removidas por não apresentarem informações úteis para a análise.

### Duplicatas

Foi realizada a identificação de registros duplicados utilizando todas as colunas da base.

Durante a análise, foram encontradas repetições de produtos dentro de uma mesma compra. Essas repetições não foram consideradas necessariamente erros, pois um mesmo produto pode aparecer mais de uma vez em uma compra.

Dessa forma, optou-se por remover somente os registros em que **todas as colunas apresentavam exatamente os mesmos valores**, preservando as possíveis repetições legítimas de produtos.

Após a remoção das duplicatas completas, a quantidade de duplicatas foi verificada novamente, resultando em zero registros duplicados.

### Valores ausentes

Foi realizada uma verificação dos valores `#N/D` em todas as colunas da base.

Na Sprint 2, foi identificado o valor `#N/D` na coluna `PR_CAT`, que representa uma categoria ausente. Esse valor foi substituído por `Sem Categoria`.

Durante a Sprint 3, uma nova verificação foi realizada e identificou a presença de `#N/D` na coluna `PR_NOME`. Os registros foram investigados utilizando o `PR_ID` e a `PR_CAT`. Foi identificado que os registros com `PR_NOME` igual a `#N/D` estavam associados ao `PR_ID 107` e à categoria `Sem Categoria`.

Para preservar os registros e padronizar a representação da informação ausente, os valores `#N/D` da coluna `PR_NOME` foram substituídos por `Sem Nome`.

Após os tratamentos, foi realizada uma nova verificação, não sendo identificados valores nulos nas colunas da base.

### Resultado da limpeza

Ao final da Sprint 3, a base passou de **830.000 registros e 14 colunas** para:

- **733.447 registros**
- **10 colunas**

Também foi realizada uma verificação dos tipos de dados após a limpeza, mantendo a coluna `DATA` no formato `datetime` e os demais campos com os tipos adequados para a análise.

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

