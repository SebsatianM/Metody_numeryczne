from scipy.linalg import hilbert
import numpy as np

M=hilbert(6)

res = np.linalg.eig(M)
print("Wartości własne\n", res[0],"\nWektory własne\n", res[1])
