
# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv('R_AUTO_2019A.csv', sep = ';')
df

# %%
df.columns

# %% 
df.info()

# %%
# Definindo premio total
df['PREMIO_TOTAL'] = df['PRE_CASCO'] + df['PRE_CAS_CO'] + df['PRE_RCDMAT'] + df['PRE_RCDC'] + df['PRE_RCDMOR'] + df['PRE_APP_MA'] + df['PRE_APP_IA'] + df['PRE_APP_DM'] + df['PRE_OUTROS']

# %%
# reduzindo a base para manter apenas as colunas com significado para o modelo

df_reduzido = df[['PREMIO_TOTAL', 'TIPO_PES','MODALIDADE', 'TIPO_PROD', 'COBERTURA',
       'COD_TARIF', 'REGIAO', 'COD_CONT', 'TIPO_FRANQ', 'VAL_FRANQ',
       'PERC_FATOR', 'IS_CASCO', 'IS_RCDMAT', 'IS_RCDC', 'ANO_MODELO',
       'IS_RCDMOR', 'IS_APP_MA', 'IS_APP_IPA', 'IS_APP_DMH',
       'PERC_BONUS', 'CLAS_BONUS', 'PERC_CORR', 'SEXO', 'DATA_EMIS',  'DATA_NASC',
       'TEMPO_HAB', 'UTILIZACAO', 'INICIO_VIG', 'FIM_VIG']]

# %%
# Substituir valores inválidos (como "0") por NaN
df_reduzido['DATA_NASC'] = df_reduzido['DATA_NASC'].replace(0, np.nan)


#%%
# Convertendo a coluna para o tipo datetime
df_reduzido['DATA_EMIS'] = pd.to_datetime(df_reduzido['DATA_EMIS'], format='%Y%m%d')
df_reduzido['DATA_NASC'] = pd.to_datetime(df_reduzido['DATA_NASC'], format='%Y%m%d')
df_reduzido['INICIO_VIG'] = pd.to_datetime(df_reduzido['INICIO_VIG'], format='%Y%m%d')
df_reduzido['FIM_VIG'] = pd.to_datetime(df_reduzido['FIM_VIG'], format='%Y%m%d')

# %%
df_reduzido['ANO_MODELO'] = pd.to_numeric(df_reduzido['ANO_MODELO'], errors='coerce')

# %%
# Definindo novas variáveis
df_reduzido['idade_condutor'] = (df_reduzido['DATA_EMIS'] - df_reduzido['DATA_NASC']).dt.days
df_reduzido['idade_veiculo'] = df_reduzido['DATA_EMIS'].dt.year - df_reduzido['ANO_MODELO']
df_reduzido['duracao_vigencia'] = (df_reduzido['FIM_VIG'] - df_reduzido['INICIO_VIG']).dt.days

# %%
df_reduzido = df_reduzido.drop(columns=['DATA_NASC', 'DATA_EMIS', 'INICIO_VIG', 'FIM_VIG'])

#%%
df_reduzido

# %%
__all__ = ['df_reduzido']

# %%
