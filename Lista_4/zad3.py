from math import log
import numpy as np
u = 2510
M0 = 2.8 * 10 ** 6
m = 13.3 * 10 ** 3
g = 9.81
v = 0
t = 0
def Saturn_speed():
    for t in np.arange(0.0,100.0,0.001):
        v_new = u * log(M0 / (M0 - m * t )) - (g * t )
        if v_new >= 335: break
    return t
    
print("Prędkość saturna V wyniesie 335m/s po %fs" % Saturn_speed())