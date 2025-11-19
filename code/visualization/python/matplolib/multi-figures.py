from matplotlib import pyplot as plt
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)

# Create a time array
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.01)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.title('Damped oscillation')

plt.subplot(212)
plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')

plt.show()
