import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt

N = 1000
# cambiar a 0.8
r = 0.80
Sigma = np.array([[1.0, r], [r, 1.0]])

B = np.linalg.cholesky(Sigma)
x = B @ randn(2, N)

plt.scatter([x[0,:]], [x[1,:]], alpha=0.4, s = 4)

plt.show()
