import numpy as np
from scipy.misc import derivative as der
from scipy.interpolate import lagrange as lag

def f(x):
    np.cos(2 * np.cos(x)**(-1))
    
X_from = -1
X_to = 1

wezly = [3, 5, 7]

for w in wezly:
    np.linspace(X_from, X_to, w)
    