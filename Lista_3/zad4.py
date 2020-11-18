import numpy as np
import scipy as sc
def gauss(a, b):
    n = len(b)
    x = np.zeros(n,float)
    for k in range(n - 1):
        for i in range(k + 1, n):
            if a[i, k] == 0.0: continue
            pom = a[k, k] / a[i, k]
            for j in range(k, n):
                a[i, j] = a[k, j] - a[i, j] * pom
            b[i] = b[k]- b[i]*pom
  
    x[n - 1] = b[n - 1] / a[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += a[i, j] * x[j]
        x[i] = (b[i]-sum)/a[i,i]
    return x
#A = np.array([[0,0,2,1,2],[0,1,0,2,-1],[1,2,0,-2,0],[0,0,0,-1,1],[0,1,-1,1,-1]],float)
#b = np.array([[1],[1],[-4],[-2],[-1]],float)
A = np.array([[-1, 1, -4], [2, 2, 0], [3, 3, 2]], float)
b = np.array([[0], [1], [0.5]], float)

print(gauss(A,b))