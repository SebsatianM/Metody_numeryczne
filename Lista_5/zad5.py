import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
x = [1.0,2.5,3.5,4.0,1.1,1.8,2.2,3.7]
y = [6.008,15.722,27.13,33.772,5.257,9.549,11.098,28.828]
#polyfit(x,y,n) returns the coefficients for a polynomial p(x) of degree n that is a best fit (in a least-squares sense) for the data in y. zatem w pierwszym przypadku n ustawiamy na 1 a za drugim n=2 aby uzyskać funkcję kwadratową
f_liniowa = np.polyfit(x, y, 1)
f_kwadrat = np.polyfit(x, y, 2)
x1 = np.linspace(min(x), max(x), 100)

y_liniowa = np.polyval(f_liniowa, x)
y_kwadratowa = np.polyval(f_kwadrat, x1)
#r2_score ocenia współczynnik determinacji czyli dokładność z jaką dopasowaliśmy nasze krzywe
y_kwadratowa_to_r2_score = np.polyval(f_kwadrat, x) #tylko do określenia dokładności

print("Dokładnośc funkcji liniowej:",r2_score(y, y_liniowa))
print("Dokładnośc funkcji kwadratowej:", r2_score(y, y_kwadratowa_to_r2_score))

plt.scatter(x, y)
plt.plot(x,y_liniowa)
plt.plot(x1, y_kwadratowa)
plt.show()