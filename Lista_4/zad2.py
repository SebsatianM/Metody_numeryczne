import numpy as np
from scipy import optimize

x = int(input("Podaj liczbę z jakiej chcesz obliczyć pierwiastek: "))
n = int(input("Podaj stopień pierwiaskta który chcesz obliczyć: "))
y = lambda x,a: x**n-a
dy = lambda  x,a: n*x**(n-1)
root = optimize.newton(y, 3, fprime=dy, args=(x,))

print("Pierwiastek %.0f-stopnia z %d jest równy %s" % (n,x,root))