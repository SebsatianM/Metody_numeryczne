import numpy as np
from scipy.integrate import simps 
import math
def f(x1, x2):
    return 1/np.sqrt(1-np.sin(x1/2)**2*np.sin(x2)**2)
X_from = 0
X_to = math.pi/2

angles = [15, 30, 45,0]

for alfa in angles:
    x = np.linspace(X_from, X_to, 3)
    f_x = f(np.radians(alfa), x)
    integ = simps(f_x, x)
    print("Wartość h({0})={1}".format(alfa,integ))
    
print("Wartość pi/2:",math.pi/2)