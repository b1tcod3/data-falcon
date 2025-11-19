import matplotlib.pyplot as plt

fig, ax = plt.subplots()

fruits = ['apple','blueberry','cherry','orange']
counts = [40,100,30,55]
bar_labels = ['red','blue','_red','orange']
bar_colors = ['tab:red','tab:blue','tab:red','tab:orange']

ax.bar(fruits,counts,label=bar_labels,color=bar_colors)
ax.set_ylabel('Frutas')
ax.set_title('Colores de Frutas')
ax.legend(title='Colores de frutas')

plt.show()


