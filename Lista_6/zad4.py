import numpy as np
from scipy.misc import derivative as der
from scipy.integrate import simps 

def f(x):
    return np.cos(2 * np.cos(x)**(-1))
    
X_from = -1
X_to = 1

wezly = [3, 5, 7]

for w in wezly:
    x = np.linspace(X_from, X_to, w)
    f_x = f(x)
    r = simps(f_x, x)
    print("Wynik całki dla {0} węzłów = {1}".format(w,r))  
#Wynik jest dokładniejszy im większa jest ilość węzłów, ponieważ wynik tej całki oznaczonej obliczony w WolframAlpha jest równy -1.365544451 