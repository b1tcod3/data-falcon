import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

np.random.seed(19680801)

y = np.random.normal(loc=.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()

x= np.arange(len(y))

# plot with varias escalas
plt.figure(1)

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('Linear scale')
plt.grid(True)
# logarithmic
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('Logarithmic scale')
plt.grid(True)
# symlog
plt.subplot(223)
plt.plot(x, y-y.mean())
plt.yscale('symlog')
plt.title('Symmetric log scale')
plt.grid(True)
# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('Logit scale')
plt.grid(True)

plt.gca().yaxis.set_major_formatter(ScalarFormatter())

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.1, right=0.95, hspace=0.25, wspace=0.35)
plt.show()