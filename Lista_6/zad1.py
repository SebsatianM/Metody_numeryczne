from scipy.misc import derivative as der
import numpy as np

def f(x):
    return np.log(np.tanh(x / (x * x + 1)))
    
point = 0.2

d_1 = der(f, point, 0.0001, 1, order=5)
d_2 = der(f, point, 0.0001, 2, order=5)
d_3 = der(f, point, 0.0001, 3, order=5)

print("pochodna 1 rzędu= {0},\npochodna 2 rzędu= {1},\npochodna 3 rzędu= {2}".format(d_1,d_2,d_3))