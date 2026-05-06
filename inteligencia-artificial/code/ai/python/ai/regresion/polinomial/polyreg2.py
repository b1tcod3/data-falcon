from polyreg1 import *

max_p = 18
p_range = np.arange(1, max_p+1, 1)

X = np.ones((n,1))
u_mean = np.mean(u)
u_centered = u - u_mean
betahat, trainloss = {},{}

for p in p_range:
    if p > 1:
        X = np.hstack((X, u_centered**(p-1)))
    betahat[p] = solve(X.T @ X, X.T @ y)
    trainloss[p] = ( norm(y - X @ betahat[p])**2 / n )
    
p = [2, 4, 6]

xx_centered = xx - u_mean

plots = [plt.plot(u, y,'k.', markersize=8)[0],
         plt.plot(xx, yy,'k--', linewidth=3)[0]]

for pi in p:
    yy = np.polyval(np.flip(betahat[pi]), xx_centered)
    plots.append(plt.plot(xx, yy, linewidth=2)[0])

plt.xlabel(r'$u$')
plt.ylabel(r'$h^{\mathcal{H}_p}_{\tau}(u)$')
plt.legend(plots, ('data points', 'true', '$p=2$, underfit', '$p=4$', '$p=16$, overfit'), loc='upper left')

plt.show()