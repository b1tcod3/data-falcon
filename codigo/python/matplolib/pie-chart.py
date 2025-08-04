import matplotlib.pyplot as plt

etiquetas = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby','Otros']
porcentajes = [30, 25, 20, 15, 5, 5]
explode = (0.1, 0, 0, 0, 0, 0)  # Resaltar el primer segmento
colores = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

fig, ax = plt.subplots(figsize=(10, 6))

wedges, texts, autotexts = ax.pie(
    porcentajes,
    explode=explode,
    labels=etiquetas,
    autopct='%1.1f%%',
    startangle=90,
    colors=colores,
    shadow=True,
    wedgeprops={'edgecolor': 'black'},
    textprops={'fontsize': 12, 'color': 'black'}
)
ax.set_title('Distribución de Lenguajes de Programación', fontsize=16, fontweight='bold')
plt.setp(autotexts, size=10, weight='bold')
centro_circle = plt.Circle((0, 0), 0.70, fc='white')  # Círculo central para hacer un gráfico de dona
fig.gca().add_artist(centro_circle)  # Añadir el círculo al gráfico

plt.axis('equal')  # Igualar el aspecto del gráfico
plt.tight_layout()  # Ajustar el diseño para evitar superposiciones
plt.show()  # Mostrar el gráfico