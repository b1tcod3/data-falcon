import matplotlib.pyplot as plt
import numpy as np

categorias = ['Velocidad', 'Fuerza', 'Resistencia', 'Flexibilidad', 'Coordinación']
valores_1 = [92, 85, 78, 90, 88]
valores_2 = [80, 75, 85, 70, 90]

n_categorias = len(categorias)
angulos = np.linspace(0, 2 * np.pi, n_categorias, endpoint=False).tolist()
valores_1 += valores_1[:1]  # Cerrar el gráfico
valores_2 += valores_2[:1]  # Cerrar el gráfico
angulos += angulos[:1]  # Cerrar el gráfico

fig = plt.figure(figsize=(8, 8), dpi=100)
ax = fig.add_subplot(111, polar=True)

#jugador 1
ax.plot(angulos, valores_1, '-o',color='blue', linewidth=2, label='Jugador 1')
ax.fill(angulos, valores_1, color='blue', alpha=0.25)

#jugador 2
ax.plot(angulos, valores_2, '-o', color='red', linewidth=2, label='Jugador 2')
ax.fill(angulos, valores_2, color='red', alpha=0.25)

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_thetagrids(np.degrees(angulos[:-1]), categorias)

# limites radiales  
ax.set_rlabel_position(0)
plt.yticks([20, 40, 60, 80, 100], ["20","40","60", "80", "100"],color="gray", size=8)
plt.ylim(0, 100)

ax.set_title('Comparación de Jugadores', size=20, color='black', y=1.1)
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

plt.tight_layout()
plt.show()