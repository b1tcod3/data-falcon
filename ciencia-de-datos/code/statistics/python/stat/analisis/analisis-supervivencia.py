from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'tiempo': [12, 24, 36, 48, 60, 72, 84, 96, 108, 120,23, 32],
    'evento': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    'grupo': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C']
}

df_surv = pd.DataFrame(data)

kmf = KaplanMeierFitter()

plt.figure(figsize=(10, 6))

for grupo in df_surv['grupo'].unique():
    grupo_df = df_surv[df_surv['grupo'] == grupo]
    kmf.fit(grupo_df['tiempo'], grupo_df['evento'], label=f"Grupo {grupo}")
    kmf.plot_survival_function(ci_show=True)

plt.title('Curvas de Supervivencia por Grupo')
plt.xlabel('Tiempo')
plt.ylabel('Probabilidad de Supervivencia')
plt.legend()
plt.grid(True)
plt.show()
