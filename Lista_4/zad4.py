import math
import numpy as np
from scipy import optimize
def fdz(x):
    return [x[0] + math.e ** (-x[0]) + x[1]** 3, x[0]** 2 + 2 * x[0] * x[1] - x[1]** 2 + math.tan(math.degrees(x[0]))]

x0 = np.array([0,1])
x1 = optimize.root(fdz, x0)
if x1.success:
    print(x1.x,' ',x1.nfev)