import numpy
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

x = [1,1.25,1.5,1.75,2,2.25,2.5,2.75,3]
y = [-0.5403,-0.0104,0.9423,1.7445,1.3073,-0.7718,-2.4986,-0.7903,2.7334]

mypolynomial = numpy.poly1d(numpy.polyfit(x, y, 8))

myline = numpy.linspace(1,3, 100)

plt.scatter(x, y)
plt.plot(myline, mypolynomial(myline))
val_in_2_1 = mypolynomial(2.1)
print("Wartości w punkcie 2.1: ", val_in_2_1)
mypoly2 = mypolynomial.deriv()
val2_in_2_1 = mypoly2(2.1)
print(mypoly2)
print("Wartości w punkcie 2.1: przy y' ", val2_in_2_1)
print("pierwiastki: ",mypolynomial.roots)
plt.show() 