import math
I_start= 1.0
for n in range(2,20):
    I_temp = math.e - (n + 1) * I_start
    print("n", n, I_temp)
    I_start = I_temp 