import math

def bez_straty(x):
    return (pow(x,4))/(math.sqrt(pow(x,4)+4)+2)

for n in range(24):
    print("wynik: ",bez_straty(n))
