import numpy as np

A=np.array([[1,-2,1],
            [0,2,-8],
            [-4,5,9]  
            ])

b=np.array([0,8,-9])

solucion = np.linalg.solve(A,b)

print(solucion)