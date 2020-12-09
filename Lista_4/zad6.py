import math
from scipy import optimize
import numpy as np
wyniki = []
def funk(unknown_param):
    x, y = unknown_param
    f_x = math.tan(x) - y - 1
    f_y = math.cos(x) - 3 * math.sin(y)
    return [f_x, f_y]
    

for i in np.arange(0, 1.5, 0.01):
    for j in np.arange(0, 1.5, 0.01):
        x1 = optimize.root(funk, [i, j])
        if (x1.success):
            x0_val = round(x1.x[0], 4)
            y0_val = round(x1.x[1], 4)
            if x0_val >= 0 and x0_val <= 1.5 and [x0_val, y0_val] not in wyniki:
                wyniki.append([x0_val, y0_val])

print(wyniki)