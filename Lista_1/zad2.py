import matplotlib.pyplot as plt
import numpy as np

y = [0.1]
x = [0]

for i in range(0,101):
    x.append(i)
    y.append((3.5*y[-1])*(1-y[-1]))

plt.scatter(x,y)
plt.show()
np.savetxt('rozwiazania_zad2.txt', np.c_[x,y])