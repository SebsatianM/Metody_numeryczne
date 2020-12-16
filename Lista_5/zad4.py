import numpy
import matplotlib.pyplot as plt
Re = [0.2, 2, 20, 200, 2000, 20000]
Cp = [103, 13.9, 2.72, 0.8, 0.401, 0.433]

plt.scatter(Re, Cp)
plt.yscale('log')
plt.xscale('log')
plt.show()