import numpy as np
from scipy.integrate import solve_ivp as s_i
import matplotlib.pyplot as plt
f = lambda t, y: np.sin(t * y)

y = [2, 2.5, 3, 3.5]
zakres = [0,6]
for x in y:
    eq = s_i(f, zakres, [x])
    plt.scatter(eq.t, eq.y[0])
    plt.plot(eq.t, eq.y[0])

plt.legend(["y=%a"%y[0],"y=%a"%y[1],"y=%a"%y[2],"y=%a"%y[3]])
plt.show()