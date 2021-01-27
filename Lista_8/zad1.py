import numpy as np

M=np.array([[-1, -4, 1],[-1, -2, -5],[5 ,4 ,3]])

res = np.linalg.eig(M)
print("Wartości własne\n", res[0],"\nWektory własne\n", res[1])
