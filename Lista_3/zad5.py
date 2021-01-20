import numpy as np
import scipy.linalg as sc

print("Norma dla 5-elementowej macierzy Hilberta:",np.linalg.norm(sc.hilbert(5)))
print("Norma dla 10-elementowej macierzy Hilberta:",np.linalg.norm(sc.hilbert(10)))
print("Norma dla 20-elementowej macierzy Hilberta:",np.linalg.norm(sc.hilbert(20)))

print("\nWskaźnik uwarunkowania dla 5-elementowej macierzy Hilberta:",np.linalg.cond(sc.hilbert(5)))
print("Wskaźnik uwarunkowania dla 10-elementowej macierzy Hilberta:",np.linalg.cond(sc.hilbert(10)))
print("Wskaźnik uwarunkowania dla 20-elementowej macierzy Hilberta:",np.linalg.cond(sc.hilbert(20)))