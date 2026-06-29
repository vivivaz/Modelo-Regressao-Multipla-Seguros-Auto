# %%
import statsmodels.api as sm
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression

# %%
# Adicionar uma constante para o intercepto
X = sm.add_constant(X)

# Ajustar o modelo
model = sm.OLS(y, X).fit()

# Resumo do modelo
print(model.summary())

# %%
model = LinearRegression()
rfe = RFE(model, n_features_to_select=12)
fit = rfe.fit(X, y)
print("Features selecionadas:", X.columns[fit.support_])

# %%
X = X[['COD_END', 'TIPO_PES', 'MODALIDADE', 'TIPO_PROD', 'COBERTURA',
       'COD_TARIF', 'REGIAO', 'COD_CONT', 'TIPO_FRANQ', 'TAB_REF',
       'PERC_BONUS', 'SEXO']]

y = df['PREMIO']

# %%
X = sm.add_constant(X)

# Ajustar o modelo
model = sm.OLS(y, X).fit()

# Resumo do modelo
print(model.summary())