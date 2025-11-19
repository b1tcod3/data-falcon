from statsmodels.stats.power import TTestIndPower
import numpy as np
import matplotlib.pyplot as plt

# analisis de poder estaditico parra diseño experimental

effect_sizes = np.arange(0.1, 1.0, 0.1)
sample_sizes = np.arange(10, 200, 10)

analysis = TTestIndPower()

analysis.plot_power(
    dep_var='nobs',
    nobs=sample_sizes,
    effect_size=effect_sizes,
    alpha=0.05,
    alternative='larger'
)

plt.title('Poder estadístico para diferentes tamaños de muestra y tamaños del efecto')
plt.xlabel('Tamaño de la muestra')
plt.ylabel('Tamaño del efecto')
plt.grid(True)

plt.legend([f'ES={es:.1f}' for es in effect_sizes], title='Tamaño del efecto')

# calculo de tamaño muestral necesario para un poder estadístico
required_n = analysis.solve_power(
    effect_size=0.5,
    power=0.8,
    alpha=0.05,
    alternative='larger'
)
print(f'Tamaño muestral rquerido por grupo: {np.ceil(required_n).astype(int)}')

plt.show()



