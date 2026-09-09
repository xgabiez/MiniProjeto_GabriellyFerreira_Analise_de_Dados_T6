# Sprint 1 - Importacao e leitura dos dados 
import pandas as pd

# Carregando a base de dados - Base Varejo
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