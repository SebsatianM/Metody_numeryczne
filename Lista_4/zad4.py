import math
import numpy as np
from scipy import optimize
def fdz(x):
    return [x[0] + math.e ** (-x[0]) + x[1]** 3, x[0]** 2 + 2 * x[0] * x[1] - x[1]** 2 + math.tan(x[0])]
def calc(x):
    x1 = optimize.root(fdz, x)
    if x1.success:
        print(x1.x,' ',x1.nfev)

#jest to oszacowany na podstawie wykresu 'wykres_do_4.png' zakres x-ów w którym mogą być miejsca przecięcia się dwóch funkcji
x1 = np.array([-1.450, -1.260])
x2 = np.array([-0.750, -0.700])
x3 = np.array([1.200, 1.210])

calc(x1)
calc(x2)
calc(x3)
