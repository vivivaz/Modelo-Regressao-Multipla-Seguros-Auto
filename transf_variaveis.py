# %%
%run pre_processing.py

df_reduzido

# %%
import pandas as pd
import numpy as np

# %%
# Definindo indicadoras

df_reduzido['SEXO'] = df_reduzido['SEXO'].replace({
    'F': 1,
    'M': 0,
    0: np.nan
})

df_reduzido['TIPO_PES'] = df_reduzido['TIPO_PES'].replace({
    'F': 1,
    'J': 0
})

# %%
# Definindo Dummies

# %%
df_reduzido['TIPO_PES'] = pd.to_numeric(df_reduzido['TIPO_PES'])
df_reduzido['SEXO'] = pd.to_numeric(df_reduzido['SEXO'])

# %%
df_reduzido.columns

# %%
# Definindo a matriz X e a variável resposta y
X =

y = 

# %%
corr_matrix = X.corr()
corr_matrix

# Remover linhas com valores ausentes em X ou y
X = X.dropna()
y = y.loc[X.index]

