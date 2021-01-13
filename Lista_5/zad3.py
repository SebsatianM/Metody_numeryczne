import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
Re = [0.2, 2, 20, 200, 2000, 20000]
Cp = [103, 13.9, 2.72, 0.8, 0.401, 0.433]

log_Re = np.log(Re)
log_Cp = np.log(Cp)
Log_CubSpl = interpolate.CubicSpline(log_Re, log_Cp)
x_to_find = [5, 50, 5000]
y = np.exp(Log_CubSpl(np.log(x_to_find)))
print("pierwiastki:", y)
plt.scatter(Re, Cp)
plt.yscale('log')
plt.xscale('log')
plt.show()