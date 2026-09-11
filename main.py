# ---------- Sprint 1 - Importacao e leitura dos dados -------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregando a base de dados - Base Varejo
# O separador ';' é utilizado pois foi verificado que o arquivo CSV utiliza esse separador
df = pd.read_csv('Base Varejo.csv', sep=';')

# Exibindo as primeiras linhas da base
print(df.head())

# Quantidade de registros e colunas
print(f'Quantidade de registros: {df.shape[0]}')
print(f'Quantidade de colunas: {df.shape[1]}')

# Nome das colunas
print(f'Nome das colunas: {df.columns.tolist()}')

# Tipos de dados das colunas
print(f'Tipos de dados das colunas:\n{df.dtypes}')


#---------- Sprint 2 - Transformação de Strings, Integer, Float e Datetime.  -------------

##### Tratando Strings ######
# Removendo espaços extras das colunas de texto
df['CL_GENERO'] = df['CL_GENERO'].str.strip()
df['CL_SEG'] = df['CL_SEG'].str.strip()
df['PR_CAT'] = df['PR_CAT'].str.strip()
df['PR_NOME'] = df['PR_NOME'].str.strip()

# Inspecionando os dados para Analise

print("\nVALORES ÚNICOS - CL_GENERO:")
print(df['CL_GENERO'].unique())

print("\nVALORES ÚNICOS - CL_SEG:")
print(df['CL_SEG'].unique())

print("\nVALORES ÚNICOS - PR_CAT:")
print(df['PR_CAT'].unique()) 


if '#N/D' in df['PR_CAT'].values:
    df['PR_CAT'] = df['PR_CAT'].replace('#N/D', 'Sem Categoria')
else:
    print("Não foram encontradas categorias ausentes.")

#Verificando novamente os valores únicos da coluna 'PR_CAT' após a substituição
print("\nVALORES ÚNICOS - PR_CAT:")
print(df['PR_CAT'].unique()) 

# Verificando os dados da coluna 'PR_NOME' para identificar possíveis inconsistências
print(df['PR_NOME'].head(20).to_string())

print(df['PR_NOME'].sample(20, random_state=42).to_string(index=False))

# Padronizando os nomes dos produtos para maiúsculas e removendo espaços extras
df['PR_NOME'] = df['PR_NOME'].str.strip().str.upper()

# Verificando novamente os dados da coluna 'PR_NOME' após a padronização com dados que foi notado que possuem inconsistências
print(df[df['PR_NOME'].str.contains('LIMAO', na=False)]['PR_NOME'].unique())

# Convertendo a coluna 'DATA' para o tipo datetime
df['DATA'] = pd.to_datetime(
    df['DATA'],
    format='%d/%m/%Y',
    errors='coerce'
)

print(df['DATA'].head())
# Verificando os tipos de dados após as transformações

print("\nTIPOS APÓS AS TRANSFORMAÇÕES:")
print(df.dtypes)

print("\nDATAS INVÁLIDAS:")
print(df['DATA'].isna().sum())


# Verificando possíveis caracteres especiais nos nomes dos produtos
padrao = r'[^A-ZÀ-Ú0-9\s]'

produtos_com_caracteres_especiais = df[
    df['PR_NOME'].str.contains(padrao, regex=True, na=False)
]

print("\nPRODUTOS COM POSSÍVEIS CARACTERES ESPECIAIS:")
print(produtos_com_caracteres_especiais['PR_NOME'].head())

# Os registros encontrados serão avaliados na etapa de limpeza.

#---------- Sprint 3 - Limpeza de Nulos e Duplicatas -------------

# ANÁLISE DOS VALORES NULOS ----------

# Verificando a quantidade de valores nulos por coluna
print("\nQUANTIDADE DE VALORES NULOS POR COLUNA:")
print(df.isnull().sum())

# Verificando se as colunas 'Unnamed' possuem algum valor
print("\nVALORES NÃO NULOS NAS COLUNAS VAZIAS:")
print(df[['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13']].notna().sum())


#  LIMPEZA DAS COLUNAS VAZIAS ----------

colunas_vazias = [
    'Unnamed: 10',
    'Unnamed: 11',
    'Unnamed: 12',
    'Unnamed: 13'
]

df = df.drop(columns=colunas_vazias)

print("\nTAMANHO DATAFRAME APÓS REMOÇÃO DAS COLUNAS VAZIAS:")
print(df.shape)


# ANÁLISE DE DUPLICATAS ----------

# Verificando a quantidade de linhas completamente duplicadas
print("\nQUANTIDADE DE DUPLICATAS COMPLETAS:")
print(df.duplicated().sum())

# Verificando todas as ocorrências das linhas duplicadas
duplicatas = df[df.duplicated(keep=False)]

print("\nQUANTIDADE DE REGISTROS ENVOLVIDOS EM DUPLICAÇÕES:")
print(len(duplicatas))

# Verificando quantas vezes as mesmas linhas aparecem
print("\nQUANTIDADE DE VEZES QUE CADA LINHA DUPLICADA APARECE:")
print(duplicatas.value_counts().head(20))


# ANÁLISE DE PRODUTOS REPETIDOS ----------

# Verificando quantas vezes um produto aparece dentro da mesma compra
duplicatas_compra_produto = (
    df.groupby(['CO_ID', 'PR_NOME'])
      .size()
      .sort_values(ascending=False)
)

print("\nPRODUTOS REPETIDOS DENTRO DA MESMA COMPRA:")
print(duplicatas_compra_produto.head(20))

# Identificando combinações de compra + produto que aparecem mais de uma vez
compras_com_produtos_repetidos = (
    duplicatas_compra_produto[duplicatas_compra_produto > 1]
)

print(
    "\nQUANTIDADE DE COMBINAÇÕES COMPRA + PRODUTO REPETIDAS:",
    len(compras_com_produtos_repetidos)
)


# TRATAMENTO DAS DUPLICATAS ----------

quantidade_duplicatas = df.duplicated().sum()

print("\nDUPLICATAS ENCONTRADAS ANTES DA LIMPEZA:", quantidade_duplicatas)

# Removendo somente linhas completamente idênticas
df = df.drop_duplicates()

print("DUPLICATAS APÓS A LIMPEZA:", df.duplicated().sum())

# TRATAMENTO DE #N/D ---------

# Verificando a quantidade de valores #N/D em todas as colunas
# para identificar onde existem dados ausentes representados por esse marcador
print("\nQUANTIDADE DE #N/D POR COLUNA:")
print((df == '#N/D').sum())

# Visualizando as colunas PR_ID, PR_CAT e PR_NOME dos 20 primeiros registros
print(df[df['PR_NOME'] == '#N/D'][['PR_ID', 'PR_CAT', 'PR_NOME']].head(20))

# Agrupando os produtos sem nome por PR_ID e PR_CAT
# para verificar a quantidade de registros em cada grupo
print(
    df[df['PR_NOME'] == '#N/D']
    .groupby(['PR_ID', 'PR_CAT'])
    .size()
    .sort_values(ascending=False)
    .head(20)
)
# Verificando quais nomes estão associados ao PR_ID 107
# para confirmar que todos os registros estão sem nome
print(df[df['PR_ID'] == 107]['PR_NOME'].unique())

# Verificando se existem produtos sem nome e substituindo #N/D por "Sem Nome"

if '#N/D' in df['PR_NOME'].values:
    df['PR_NOME'] = df['PR_NOME'].replace('#N/D', 'Sem Nome')
else:
    print("Não foram encontrados produtos sem nome.")

print("\nQUANTIDADE DE PRODUTOS SEM NOME APÓS A LIMPEZA:")
print((df['PR_NOME'] == 'Sem Nome').sum())

#Verificando novamente os valores após limpeza

print("\nQUANTIDADE DE VALORES NULOS APÓS A LIMPEZA:")
print(df.isnull().sum())

print("\nDIMENSÕES DA BASE APÓS A LIMPEZA:")
print(df.shape)

print("\nTIPOS DE DADOS APÓS A LIMPEZA:")
print(df.dtypes)

#---------- Sprint 4 - Estatística Descritiva -------------

# Valores estatísticos descritivos da coluna CL_FHL (número de filhos)
print("\nINFORMAÇÕES SOBRE O NÚMERO DE FILHOS:")
print(df['CL_FHL'].describe())

# Calculando a média do número de filhos
print("\nMÉDIA DO NÚMERO DE FILHOS:")
print(df['CL_FHL'].mean())

# Calculando a mediana do número de filhos
print("\nMEDIANA DO NÚMERO DE FILHOS:")
print(df['CL_FHL'].median())

# Calculando o desvio padrão do número de filhos
print("\nDESVIO PADRÃO DO NÚMERO DE FILHOS:")
print(df['CL_FHL'].std())

# Calculando a moda do número de filhos
print("\nMODA DO NÚMERO DE FILHOS:")
print(df['CL_FHL'].mode())

# Calculando o valor máximo do número de filhos
print("\nMÁXIMO DE FILHOS:")
print(df['CL_FHL'].max())

# Calculando o valor mínimo do número de filhos
print("\nMÍNIMO DE FILHOS:")
print(df['CL_FHL'].min())

# Calculando a quantidade de registros válidos na coluna CL_FHL
print("\nQUANTIDADE DE REGISTROS:")
print(df['CL_FHL'].count())

# Calculando os quartis do número de filhos
print("\nQUARTIS DO NÚMERO DE FILHOS:")
print(df['CL_FHL'].quantile([0.25, 0.50, 0.75]))

print("\nQUARTIS COM NUMPY:")
print(np.percentile(df['CL_FHL'], [25, 50, 75]))

# criando gráfico de boxplot para visualizar a distribuição do número de filhos
plt.boxplot(df['CL_FHL'])
plt.title('Distribuição do Número de Filhos')
plt.ylabel('Número de Filhos')
plt.show()

