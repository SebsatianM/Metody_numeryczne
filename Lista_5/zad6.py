import numpy as np
import matplotlib.pyplot as plt
h = [0,1.525,3.05,4.575,6.1,7.625,9.150]
p = [1,0.8617,0.7385,0.6292,0.5328,0.4481,0.3741]

plt.scatter(h,p)
f_kwadrat = np.polyfit(h, p, 2)

x = np.linspace(min(h)-1, max(h)+2, 100)
y = np.polyval(f_kwadrat, x)
plt.plot(x,y)
print("Ciśnienie na wysokości 10.5km wynosi:",np.polyval(f_kwadrat,10.5))

plt.show() 