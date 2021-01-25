import numpy as np
from scipy.integrate import dblquad as dbl
import math

X_from = 0
X_to = 1

f = lambda y, x: np.sin(np.pi * y) * np.sin(np.pi * (x - y))

f_lower = lambda x: x

result = dbl(f,X_from,X_to,X_from,f_lower)
print("Wartość całki wynosi: {0}".format(result[0])) 