import numpy as np
from scipy.special import roots_legendre as rt
import math
def f(x):
    return np.log(x)/(x**2-2*x+2)
    
X_from = 1
X_to = math.pi

wezly = [2, 4]

for w in wezly:
    x_i, a_i = rt(w)
    Integ_N = 0
    for i in range(len(a_i)):
        Integ_N += (X_to-X_from)/2*a_i[i] * f((X_to+X_from)/2 + (X_to-X_from)/2*x_i[i])
    print("Wartość całki dla {0} węzłów = {1} ".format(w,Integ_N))