import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
# Crear una figura y ejes
plt.figure(figsize=(10, 6))
# Graficar las líneas
plt.plot(x, y1, label='Seno(x)', color='blue', linewidth=2, linestyle='-')
plt.plot(x, y2, label='Coseno(x)', color='red', linewidth=2, linestyle='--')
plt.plot(x, y3, label='Tangente(x)', color='green', linewidth=2, linestyle=':')
# Personalizar el gráfico
plt.title('funciones trigonométricas')
plt.xlabel('Valores de x', fontsize=12)
plt.ylabel('Valores de y', fontsize=12)
plt.grid(True,alpha=0.3)
plt.legend()
# Mostrar el gráfico
plt.axhline(y=0, color='pink', linewidth=0.5)
plt.axvline(x=5, color='gray', linewidth=0.5, linestyle='--')
plt.show()