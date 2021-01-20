import numpy as np
from scipy.misc import derivative as der
from scipy.interpolate import lagrange as lag

x = [-2.2,-0.3,0.8,1.9]
f_x = [-15.18, 10.962, 1.92, -2.04]

poly = lag(x, f_x)

deriv = der(poly, 0, 0.001, 1, order=5)
deriv2 = der(poly, 0, 0.001, 2, order=5)

print("Wartość f'(0)=", deriv)
print("Wartość f''(0)=",deriv2)