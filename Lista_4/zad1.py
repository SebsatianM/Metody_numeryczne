from scipy import optimize
def f(x):
    return (2 * x ** 4 + 24 * x ** 3 + 61 * x ** 2 - 16 * x + 1)

roots=[]   
roots.append(optimize.ridder(f, -9, -8))
roots.append(optimize.ridder(f, -5, -1))
roots.append(optimize.ridder(f, 0, 0.1214))
roots.append(optimize.ridder(f, 0.1214, 2))

print(roots)