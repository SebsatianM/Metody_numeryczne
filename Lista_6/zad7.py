import numpy as np
from scipy.integrate import quadrature as qd 

fun = lambda x:(np.cos(x)-np.exp(x))/np.sin(x)

X_from = -1
X_to = 1

Integ1 = qd(fun, X_from, 0, tol=1e-10,maxiter=200)

Integ2 = qd(fun, 0, X_to, tol=1e-10,maxiter=200)

#podział na dwie całki od -1 do 0 i od 0 do 1, ponieważ przy próbie całkowania od -1 do 1 iteracja dążyła do nieskończoności 

print("Wartość całki wynosi: {0}\nBłąd obliczeń wynosi: {1}".format(Integ1[0]+Integ2[0],Integ1[1]+Integ2[1])) 