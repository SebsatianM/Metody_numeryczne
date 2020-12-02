import math
from scipy import optimize
import numpy as np
def funk(unknown_param):
    x, y = unknown_param
    f_x = math.tan(x) - y - 1
    f_y = math.cos(x) - 3 * math.sin(y)
    return [f_x, f_y]
    

for i in np.arange(0, 1.5, 0.01):
    for j in np.arange(0, 1.5, 0.01):
        x1 = optimize.root(funk, [i, j])
        if (x1.success):
            print(x1)