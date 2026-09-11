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

Nesta etapa foi realizada a análise estatística da coluna `CL_FHL`, correspondente ao número de filhos dos clientes.

Foram aplicadas funções estatísticas do Pandas para calcular a média, mediana, desvio padrão, moda, valor máximo, valor mínimo, quantidade de registros e quartis.

### Resultados

- **Média:** 1,1460 filhos
- **Mediana:** 0 filhos
- **Desvio padrão:** 1,4169
- **Moda:** 0 filhos
- **Máximo:** 4 filhos
- **Mínimo:** 0 filhos
- **Quantidade de registros:** 733.447
- **1º quartil (25%):** 0 filhos
- **2º quartil (50%):** 0 filhos
- **3º quartil (75%):** 2 filhos

Também foi utilizada a biblioteca NumPy para calcular os quartis por meio da função `percentile()`, permitindo comparar os resultados com os obtidos pelo Pandas.

Para complementar a análise, foi utilizado um gráfico do tipo **boxplot**, permitindo visualizar a distribuição dos valores, a mediana e os quartis da quantidade de filhos.

### Análise

Os resultados mostram que a mediana e a moda são iguais a 0, indicando que 0 filhos é o valor mais frequente na base. A média de aproximadamente 1,15 filhos é superior à mediana devido à presença de registros com maior número de filhos.

O terceiro quartil indica que 75% dos registros possuem até 2 filhos, enquanto o valor máximo encontrado foi de 4 filhos.

## Sprint 5 - Relatório e documentação

Nesta etapa foi desenvolvido um relatório final exibido no terminal, reunindo informações importantes sobre a base após o processo de limpeza e transformação.

### Informações da base

- **Registros:** 733.447
- **Colunas:** 10
- **Clientes:** 1.000
- **Compras:** 18.471
- **Produtos:** 229
- **Categorias:** 7
- **Duplicatas após a limpeza:** 0

### Principais resultados

- A categoria com maior quantidade de registros foi **ALIMENTOS**, com 384.197 registros.
- O produto com maior quantidade de registros foi **PRESUNTO COZIDO**, com 12.719 registros.
- O número de filhos mais frequente foi **0**, com 384.986 registros.
- A base possui 1.000 clientes distintos e 18.471 compras distintas.
- Após a limpeza, não permaneceram registros duplicados.

---

## Insights e conclusões

A análise exploratória permitiu identificar alguns padrões importantes na base de varejo:

1. **Predominância da categoria Alimentos:** a categoria `ALIMENTOS` possui 384.197 registros, sendo a categoria com maior presença na base.

2. **Produto com maior frequência:** `PRESUNTO COZIDO` foi o produto que apresentou a maior quantidade de registros, com 12.719 ocorrências.

3. **Perfil relacionado ao número de filhos:** o valor mais frequente para o número de filhos foi 0, com 384.986 registros. A média foi de aproximadamente 1,15 filhos.

4. **Distribuição do número de filhos:** 75% dos registros possuem até 2 filhos, enquanto o maior valor identificado foi 4 filhos.

5. **Qualidade dos dados:** após a remoção das duplicatas completas, tratamento dos valores ausentes e exclusão das colunas completamente vazias, a base ficou com 733.447 registros e 10 colunas, sem valores nulos ou duplicatas.


## Sprint 6 - Versionamento

Nesta etapa foi realizado o versionamento e envio dos arquivos do projeto para um repositório público no GitHub utilizando o Git.

Foram enviados os seguintes arquivos:

- `main.py` - script desenvolvido em Python contendo as etapas de análise e tratamento dos dados.
- `README.md` - documentação do projeto, contendo as etapas realizadas, resultados, insights e reflexão teórica.
- `df_limpo` - base de dados após os processos de transformação e limpeza realizados durante o projeto.

O versionamento foi realizado utilizando commits ao longo do desenvolvimento, permitindo acompanhar a evolução do projeto por etapas.


## Reflexão teórica

### ETL

O processo de ETL consiste nas etapas de **Extração, Transformação e Carga** dos dados.

Neste projeto, a extração ocorreu por meio da leitura do arquivo `Base Varejo.csv` utilizando a biblioteca Pandas.

Na etapa de transformação foram realizadas ações como padronização de textos, tratamento de valores ausentes, conversão da coluna de datas para `datetime`, identificação e remoção de duplicatas completas e exclusão de colunas sem informações.

A etapa de carga pode ser relacionada à disponibilização da base limpa para as análises estatísticas e exploratórias realizadas durante o projeto.


### Qualidade dos dados

A qualidade dos dados é importante para garantir que as análises sejam realizadas sobre informações consistentes e confiáveis.

Durante o projeto foram identificados problemas como colunas completamente vazias, registros duplicados e valores `#N/D` representando informações ausentes.

Os dados foram analisados antes da aplicação dos tratamentos, buSscando evitar alterações indevidas. As duplicatas foram removidas somente quando todos os campos eram exatamente iguais, enquanto repetições de produtos dentro das compras foram preservadas.

Esse processo contribuiu para tornar a base mais organizada, padronizada e adequada para as análises realizadas.

## Conclusão

O projeto permitiu aplicar na prática conceitos de análise exploratória de dados utilizando Python, principalmente com as bibliotecas Pandas e NumPy.

As etapas de transformação, limpeza, estatística descritiva e análise possibilitaram compreender melhor a estrutura e as características da base de varejo, além de demonstrar a importância da qualidade dos dados para a obtenção de resultados confiáveis.

