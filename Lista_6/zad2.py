import numpy as np
from scipy.misc import derivative as der
from scipy.interpolate import lagrange as lag

x = [0.0, 0.1, 0.2, 0.3, 0.4]
f_x = [0.0, 0.078348, 0.13891, 0.192916, 0.244981]

poly = lag(x, f_x)

deriv = der(poly, 0.2, 0.0001, 1, order=5)

print("Wartość f'(0.2)=", deriv)
