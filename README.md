# 📊 Mini Projeto Avaliativo — Análise de Dados com Python

## 🎯 Objetivo

Este projeto tem como objetivo realizar uma **Análise Exploratória de Dados (AED)** sobre uma base de dados de varejo, aplicando técnicas de importação, limpeza, transformação e análise dos dados utilizando Python.

O projeto foi desenvolvido como atividade avaliativa do curso de **Análise de Dados com Python — SENAI | SCTEC**.

---

## 🛠️ Tecnologias utilizadas

- 🐍 Python
- 🐼 Pandas
- 🔢 NumPy
- 📈 Matplotlib
- 🔧 Git
- 🌐 GitHub

---

## 📁 Base de dados

A base utilizada é a `Base Varejo.csv`, contendo informações relacionadas a:

- 🛒 Compras
- 👥 Clientes
- 📦 Produtos
- 🏷️ Categorias
- 📅 Datas

Inicialmente, a base possuía:

- **830.000 registros**
- **14 colunas**

Durante a importação foi identificado que o arquivo utilizava `;` como separador das colunas.

---

# 🚀 Sprints do projeto

## 📥 Sprint 1 — Importação dos dados

Foi realizada a importação da base `Base Varejo.csv` utilizando a biblioteca **Pandas**.

Após a leitura, foram analisadas:

- As primeiras linhas da base;
- As dimensões da tabela;
- Os nomes das colunas;
- Os tipos de dados.

A base inicialmente possuía **830.000 registros e 14 colunas**.

Durante essa etapa também foi identificado que:

- A coluna `DATA` estava inicialmente como texto;
- Existiam colunas sem informações preenchidas;
- O arquivo utilizava `;` como separador.

---

## 🔄 Sprint 2 — Transformação dos dados

Nesta etapa foram realizadas transformações e padronizações nas informações da base.

### 🔤 Strings

As colunas de texto foram analisadas e padronizadas utilizando métodos de string do Pandas.

Na coluna `PR_CAT`, foi identificado o valor `#N/D`, utilizado para representar uma categoria ausente.

Esse valor foi substituído por:

`Sem Categoria`

Na coluna `PR_NOME`, os textos foram padronizados utilizando:

- `strip()` → remoção de espaços desnecessários;
- `upper()` → padronização dos textos em letras maiúsculas.

### 📅 Data

A coluna `DATA`, inicialmente identificada como texto, foi convertida para o tipo `datetime` utilizando `pd.to_datetime()`.

Foi utilizado o formato:

`%d/%m/%Y`

Após a conversão, não foram identificadas datas inválidas.

### 🔎 Expressões regulares

Foi utilizada uma expressão regular para identificar possíveis caracteres especiais nos nomes dos produtos.

Durante essa verificação foram encontrados registros contendo `#N/D` na coluna `PR_NOME`, que foram posteriormente analisados e tratados na etapa de limpeza dos dados.

---

## 🧹 Sprint 3 — Limpeza de nulos e duplicatas

Nesta etapa foram realizadas análises e tratamentos relacionados à qualidade dos dados.

Foram verificadas:

- Valores nulos;
- Colunas completamente vazias;
- Registros duplicados;
- Valores ausentes representados por `#N/D`.

### 🗑️ Colunas vazias

Foram identificadas quatro colunas que não possuíam nenhum valor preenchido:

- `Unnamed: 10`
- `Unnamed: 11`
- `Unnamed: 12`
- `Unnamed: 13`

Essas colunas foram removidas por não apresentarem informações úteis para a análise.

### ♻️ Duplicatas

Inicialmente foram identificadas **96.553 duplicatas completas**.

Durante a análise também foram encontradas repetições de produtos dentro de uma mesma compra.

Essas repetições não foram consideradas necessariamente erros, pois um mesmo produto pode aparecer mais de uma vez em uma compra.

Dessa forma, optou-se por remover somente os registros em que **todas as colunas apresentavam exatamente os mesmos valores**, preservando possíveis repetições legítimas de produtos.

Após a remoção, uma nova verificação foi realizada e o resultado foi:

`Quantidade de duplicatas: 0`

### ⚠️ Valores ausentes

Foi realizada uma verificação dos valores `#N/D` em todas as colunas.

Na coluna `PR_CAT`, o valor `#N/D` foi substituído por:

`Sem Categoria`

Na coluna `PR_NOME`, foram identificados registros com `#N/D`.

Esses registros foram investigados utilizando `PR_ID` e `PR_CAT`. Foi identificado que os registros com `PR_NOME` igual a `#N/D` estavam associados ao `PR_ID 107` e também apresentavam `PR_CAT` como `Sem Categoria`.

Como a base não disponibilizava o nome real do produto nem a categoria correspondente ao `PR_ID 107`, não foi possível determinar essas informações com os dados disponíveis. Para preservar os registros sem inserir 

informações não existentes na base, os valores foram padronizados como `Sem Nome` e `Sem Categoria`.

Após os tratamentos, não foram identificados valores nulos na base.

### 📊 Resultado da limpeza

Ao final da Sprint 3, a base passou de:

**830.000 registros e 14 colunas**

para:

**733.447 registros e 10 colunas**

---

## 📈 Sprint 4 — Estatística descritiva

Nesta etapa foi realizada a análise estatística da coluna `CL_FHL`, correspondente ao **número de filhos dos clientes**.

Foram calculados:

- 📌 Média
- 📌 Mediana
- 📌 Desvio padrão
- 📌 Moda
- 📌 Valor máximo
- 📌 Valor mínimo
- 📌 Quantidade de registros
- 📌 Quartis

### 📊 Resultados

| Estatística | Resultado |
|---|---:|
| Média | 1,1460 |
| Mediana | 0 |
| Desvio padrão | 1,4169 |
| Moda | 0 |
| Máximo | 4 |
| Mínimo | 0 |
| Registros | 733.447 |
| 1º Quartil (25%) | 0 |
| 2º Quartil (50%) | 0 |
| 3º Quartil (75%) | 2 |

Também foi utilizada a biblioteca **NumPy** para calcular os quartis por meio da função `percentile()`.

Para complementar a análise, foi utilizado um gráfico do tipo **boxplot**, permitindo visualizar a distribuição dos valores, a mediana e os quartis da quantidade de filhos.

### 🔎 Análise

Os resultados mostram que a mediana e a moda são iguais a **0**, indicando que esse é o valor mais frequente na base.

A média de aproximadamente **1,15 filhos** é superior à mediana devido à presença de registros com maior número de filhos.

O terceiro quartil indica que **75% dos registros possuem até 2 filhos**, enquanto o valor máximo identificado foi de **4 filhos**.

---

## 📝 Sprint 5 — Relatório e documentação

Nesta etapa foi desenvolvido um relatório final exibido no terminal, reunindo informações importantes sobre a base após os processos de transformação e limpeza.

### 📋 Informações da base

| Informação | Resultado |
|---|---:|
| Registros | 733.447 |
| Colunas | 10 |
| Clientes | 1.000 |
| Compras | 18.471 |
| Produtos | 229 |
| Categorias | 7 |
| Duplicatas | 0 |

### 💡 Principais resultados

- 🥇 A categoria com maior quantidade de registros foi **ALIMENTOS**, com **384.197 registros**.
- 🛒 O produto com maior quantidade de registros foi **PRESUNTO COZIDO**, com **12.719 ocorrências**.
- 👶 O número de filhos mais frequente foi **0**, com **384.986 registros**.
- 👥 A base possui **1.000 clientes distintos**.
- 🧾 Foram identificadas **18.471 compras distintas**.
- 📦 A base possui **229 produtos distintos**.
- 🏷️ Foram identificadas **7 categorias de produtos**.
- ✅ Após a limpeza, não permaneceram registros duplicados.

---

# 💡 Insights e conclusões

A análise exploratória permitiu identificar alguns padrões importantes na base de varejo:

### 1️⃣ Predominância da categoria Alimentos

A categoria `ALIMENTOS` possui **384.197 registros**, sendo a categoria com maior presença na base.

### 2️⃣ Produto mais frequente

O produto `PRESUNTO COZIDO` apresentou a maior quantidade de registros, com **12.719 ocorrências**.

### 3️⃣ Perfil relacionado ao número de filhos

O valor mais frequente para o número de filhos foi **0**, com **384.986 registros**.

### 4️⃣ Distribuição do número de filhos

O número de filhos mais frequente foi **0**, com 384.986 registros.

A média encontrada foi de aproximadamente **1,15 filhos**, enquanto o terceiro quartil indica que aproximadamente **75% dos registros possuem até 2 filhos**.

### 5️⃣ Qualidade dos dados

Após os processos de limpeza, foram removidas colunas completamente vazias, tratados valores ausentes e removidas duplicatas completas.

A base final ficou com **733.447 registros e 10 colunas**, sem valores nulos e sem registros duplicados.

---

# 📚 Reflexão teórica

## 🔄 ETL

O processo de **ETL** consiste nas etapas de:

- **E — Extract (Extração)**
- **T — Transform (Transformação)**
- **L — Load (Carga)**

Neste projeto, a extração ocorreu por meio da leitura do arquivo `Base Varejo.csv` utilizando a biblioteca Pandas.

Na etapa de transformação foram realizadas ações como:

- Padronização de textos;
- Tratamento de valores ausentes;
- Conversão da coluna de datas para `datetime`;
- Identificação e remoção de duplicatas completas;
- Exclusão de colunas sem informações.

A etapa de carga pode ser relacionada à disponibilização da base limpa para as análises estatísticas e exploratórias realizadas durante o projeto.

## ✅ Qualidade dos dados

A qualidade dos dados é fundamental para garantir que as análises sejam realizadas sobre informações consistentes e confiáveis.

Durante o projeto foram identificados problemas como:

- Colunas completamente vazias;
- Registros duplicados;
- Valores `#N/D` representando informações ausentes.

Os dados foram analisados antes da aplicação dos tratamentos, buscando evitar alterações indevidas.

As duplicatas foram removidas somente quando todos os campos eram exatamente iguais, enquanto repetições de produtos dentro das compras foram preservadas.

Esse processo contribuiu para tornar a base mais organizada, padronizada e adequada para as análises realizadas.

---

# 📦 Sprint 6 — Versionamento

Nesta etapa foi realizado o versionamento e envio dos arquivos do projeto para um repositório público no **GitHub**, utilizando o Git.

Foram enviados os seguintes arquivos:

- 🐍 `main.py` — script desenvolvido em Python contendo as etapas de análise e tratamento dos dados.
- 📖 `README.md` — documentação do projeto, contendo as etapas realizadas, resultados, insights e reflexão teórica.
- 🧹 `df_limpo.csv` — base de dados após os processos de transformação e limpeza.

O projeto foi versionado por meio de commits ao longo do desenvolvimento, permitindo acompanhar a evolução das etapas realizadas.

---

# ▶️ Como executar o projeto

## 📋 Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- 🐍 **Python 3.10 ou superior**
- 📦 **Pandas**
- 🔢 **NumPy**
- 📈 **Matplotlib**

### 📥 Instalação das dependências

Caso necessário, instale as bibliotecas utilizando o comando:

```bash
pip install pandas numpy matplotlib

````
## 🚀 Execução

### 1. Clone o repositório

Clone este repositório para sua máquina ou faça o download dos arquivos do projeto.

### 2. Verifique os arquivos

Certifique-se de que os arquivos estejam na mesma pasta:

```text
📁 Miniprojeto_GabriellyFerreira_Analise_de_Dados_T6
│
├── 📄 main.py
├── 📄 Base Varejo.csv
├── 📄 df_limpo.csv
└── 📄 README.md\

```
### 3. Abra o projeto

Abra a pasta do projeto em uma IDE, como:

- 💻 Visual Studio Code
- 📓 Jupyter Notebook

### 4. Execute o script

No terminal, execute:

```bash
python main.py

```
Durante a execução, o programa irá:

- 📥 Importar a base de dados;
- 🔍 Verificar informações iniciais;
- 🔄 Transformar e padronizar os dados;
- 🧹 Limpar valores ausentes e duplicatas;
- 📊 Realizar análises estatísticas;
- 📈 Gerar o boxplot;
- 📝 Exibir o relatório final;
- 💾 Exportar a base limpa como `df_limpo.csv`.

---

# 👩‍💻 Autora

**Gabrielly Ferreira**

Projeto desenvolvido para o curso de **Análise de Dados com Python — SENAI | SCTEC**.

---

⭐ **Projeto desenvolvido com Python, Pandas, NumPy e Matplotlib para aplicação prática de análise e tratamento de dados.**
