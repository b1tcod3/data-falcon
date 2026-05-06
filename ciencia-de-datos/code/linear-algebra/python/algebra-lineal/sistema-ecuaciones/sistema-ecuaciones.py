import numpy as np

A=np.array([[2,3,-1],
            [4,-1,2],
            [-1,2,3]  
            ])

b=np.array([5,6,4])

solucion = np.linalg.solve(A,b)

print(solucion)
# [29. 16.  3.]