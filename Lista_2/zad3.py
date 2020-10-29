import math

def l_1(x):
    return math.sqrt(pow(x,2)+1)-1

def l_2(x):
    return (pow(x,2))/(math.sqrt(pow(x,2)+1)+1)

for n in range(2,24,2):
    print("Wersja 1",l_1(pow(2,-n)))
    print("Wersja 2",l_2(pow(2,-n)))