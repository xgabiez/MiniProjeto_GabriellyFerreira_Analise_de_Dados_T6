# ---------- Sprint 1 - Importacao e leitura dos dados -------------
import pandas as pd

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

