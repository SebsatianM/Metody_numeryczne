import numpy as np

def m_hilbert(n):
    return np.array([[1 / (i + j + 1) for j in range(n)] for i in range(n)])

print(m_hilbert(4))
print(m_hilbert(8))


print(np.linalg.inv(m_hilbert(4)))
print(np.linalg.inv(m_hilbert(8)))

for n in range (5, 21):
    print(np.linalg.det(m_hilber(n)))