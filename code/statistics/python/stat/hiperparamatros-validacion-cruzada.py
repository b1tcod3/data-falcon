from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#cargar datos de viviendas

df = pd.read_csv('https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv')

df = df.dropna()
X = df.drop('median_house_value', axis=1)
y = df['median_house_value']
X = pd.get_dummies(X, columns=['ocean_proximity'])

param_dist = {
    'n_estimators': randint(100, 500),
    'max_depth': [None]+list(np.arange(5,30)),
    'max_features': uniform(0.1, 0.9),
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 10),
    'bootstrap': [True, False]
}

model = RandomForestRegressor(random_state=42)
search = RandomizedSearchCV(
    model, 
    param_distributions=param_dist, 
    n_iter=100,
    cv=5,
    scoring='neg_mean_squared_error',
    random_state=42,
    n_jobs=-1 
)
search.fit(X, y)

print("Mejores hiperparámetros encontrados:", search.best_params_)
print("Mejor puntuación (MSE negativo):", search.best_score_)

best_model = search.best_estimator_
feature_importances = pd.Series(best_model.feature_importances_, index=X.columns)
feature_importances = feature_importances.sort_values(ascending=False)

plt.figure(figsize=(10, 6))
feature_importances.plot(kind='barh')
plt.title('Importancia de las características')
plt.xlabel('Importancia')
plt.ylabel('Características')
plt.show()

