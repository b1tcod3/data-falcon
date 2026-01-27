from polyreg2 import *

u_test, y_test = generate_data(beta, sig, n)

MSE = []
X_test = np.ones((n,1))

for p in p_range:
    if p > 1:
        X_test = np.hstack((X_test, u_test**(p-1)))
    y_hat = X_test @ betahat[p]
    MSE.append( np.sum((y_test - y_hat)**2 / n ))

plt.plot(p_range, MSE, 'b',p_range,MSE,'bo')
plt.xticks(ticks=p_range)
plt.xlabel('Number of parameters $p$')
plt.ylabel('Test Loss')
