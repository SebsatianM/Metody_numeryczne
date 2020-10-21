import numpy as np

A = np.array([[4,-2,1],[-2,4,-2],[1,-2,4]])
B = np.array([[4,2,0],[2,5,2],[0,2,4]])
w = np.array([[1],[-2],[3]])
#mnożenie 
AB = A.dot(B)
Aw = A.dot(w)
BAw = B.dot(Aw)
#wyznaczniki macierzy
det_A = np.linalg.det(A)
det_B = np.linalg.det(B)
#macierze odwrotne
inver_A = np.linalg.inv(A)
inver_B = np.linalg.inv(B)

print(w)
print(AB)
print(Aw)
print(BAw)

print("Wyznacznik A:",det_A)
print("Wyznacznik B:",det_B)
print(inver_A)
print(inver_B)