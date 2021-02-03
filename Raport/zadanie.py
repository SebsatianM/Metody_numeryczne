import numpy as np
import matplotlib.pyplot as plt
from scipy.special import roots_chebyt
from scipy.integrate import quad
#tablica z wartościami całek dla x = 0.0,1.0,2.0 wyniki zostały obliczone w WolframAlpha
Iex = [np.pi,3.9774632605064226372566098326646971640806713859083192867002979776,7.1615284390502566621111407447070739394605866275279605446118868476]
x_range = np.arange(0, 2.05, 0.05)  #definowanie zakresu dla x od 0.0-2.0 z krokiem 0.05

results = []    

#definiowanie funkcji podcałkowej
def fzc(t, x):
    return (np.exp(t * x)) / (np.sqrt(1 - pow(t, 2)))
    
#definiowanie funkcji podcałkowej wymnożonej przez funkcję wagową
def fzc_p(t, x):
    return np.exp(t * x)
        
#definicja funkcji obliczająca wartość całki jako argumenty przyjmuje 
#f - funkcja podcałkowa wymnożona przez funkcję wagową
#n - ilość węzłów dla których ma wykonać obliczenia
#x - wartość z zakresu 0.0-2.0 dla których mieliśmy oblczyć całkę
#A_i - waga węzła dla metody Gaussa-Czebyszewa jest ona stała
#t_i = roots_chebyt(n)[0] 
#pętla w której obliczana jest wartość pierwiastka wielomianu Czebyszewa [t_i] oraz wartość sumy 
def qgc(f, n, x):
    A_i = np.pi / n
    suma = 0
    for k in range(n):
        t_i = np.cos((2 * (k + 1) - 1) / (2 * n) * np.pi)
        suma+= A_i*fzc_p(t_i,x)
    return suma

i = 0
result = 0  
#zestaw pętli które służą do obliczania wartości całek z zakresu 0.0-2.0 z wykorzystaniem 10 węzłów a w przypadku gdy x mają wartość {0,1.0,2.0}
#obliczna całkę do momentu aż nie będzie ona wynosiła tyle co jej obliczenia za pomocą programu WolframAlpha które znajdują się w tablicy Iex
for x in x_range:
    x = round(x,2) 
    if x == 0.0 or x == 1.0 or x == 2.0:
        I = 1
        print("\n{0}   {1}\t{2}\t\t\t{3}".format("x:","węzły:","wynik:","błąd:"))
        while (Iex[i] - result) != 0:
            result = qgc(fzc_p, I, x)  
            print(x, " \t%2d\t%18.20f\t%8.10e" % (I, result, Iex[i] - result))
            I+=1
        results.append(result)
        i+=1
    else:
        result = qgc(fzc_p, 10, x)
        results.append(result)

#szukanie maksymalnej wartości
max_g = max(results)
max_g_x = results.index(max_g)

#wyświeltanie wszystkich wyników
print("\nWartość maksymalna g({0}) = {1}".format(x_range[max_g_x], max_g))
print("\nWartości całki w zależności od x\n x:\t wartość:")
for i in range(len(results)):
    print("{0}\t{1}".format(round(x_range[i], 2), results[i]))

#Aby sprawdzić jak inna metoda radzi sobie z tą całką zdecydowałem się użyć metody quad 
print("\nAlternatywne rozwiązanie dla x = 0.0,1.0,2.0")
print("{0}   {1}\t\t{2}".format("x:", "wynik:", "błąd:"))
for x in range(0,3):
    result=quad(fzc,-1,1,args=(x,))[0]
    print("%2.1f %18.14f   %8.4e" % (x,result, Iex[x] - result))

#rysowanie wykresu
plt.scatter(np.arange(0, 2.05, 0.05), results,label="Wartości")
plt.plot(x_range, results)
plt.scatter(x_range[max_g_x],max_g,color="red",label="Wartość maksymalna")
plt.grid()
plt.xlabel("wartości x")
plt.ylabel("wartość całki")
plt.title("Wartości całki w zależności od x")
plt.legend()
plt.show()