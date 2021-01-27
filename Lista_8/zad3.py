import numpy as np
from scipy.sparse.linalg import eigsh

def macierz(n):
    print("Dla n równego",n)
    neg_one=-1*np.ones(int(n)-1)                                  #wartosci
    two=2*np.ones(int(n))                                     #wartosci
    M = np.diag(two) + np.diag(neg_one, k=1) + np.diag(neg_one, k=-1)     #Tworzenie macierzy A, k jako pozycja 
    res =eigsh(M,k=5,which='SM')                #SM -> smallest , k<n
    print(M) 
    print("Wartości własne\n", res[0],"\nWektory własne\n", res[1])
          

macierz(10)
macierz(100)