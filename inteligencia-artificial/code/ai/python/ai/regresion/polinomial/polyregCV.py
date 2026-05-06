from polyreg3 import *

K_vals = [5, 10, 100]
cv = np.zeros((len(K_vals), max_p))
X = np.ones((n,1))
u_centered = u - np.mean(u)

for p in p_range:
    if p > 1:
        X = np.hstack((X, u_centered**(p-1)))
    j = 0
    for K in K_vals:
        loss = []
        for k in range(1,K+1):
            test_ind = ((n/K)*(k-1) +np.arange(1, n/K+1)-1).astype('int')
            train_ind = np.setdiff1d(np.arange(n), test_ind)
            
            X_train, y_train = X[train_ind,:], y[train_ind,:]
            X_test, y_test = X[test_ind,:], y[test_ind]
            
            betahat = solve(X_train.T @ X_train, X_train.T @ y_train)
            loss.append( norm(y_test - X_test @ betahat)**2 )
        cv[j,p-1] = np.sum(loss) / n
        j += 1

plt.plot(p_range, cv[0, :], 'k-.')
plt.plot(p_range, cv[1, :], 'r')
plt.plot(p_range, cv[2, :], 'b--')

plt.show()