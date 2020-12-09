"""
x = 10 //odległość gdzie piłka wpadnie do kosza
y = 3 //ponieważ w naszym ogólnym wzorze na współrzędną y już uwzględniamy wzrost koszykarza
alfa = 45 
x = v0*cos(alfa)*t
y = 2 + v0*sin(alfa)*t -(g*t^2)/2
==>
10 = v0*cos(45)*t
3 = 2+v0*sin(45)*t-4,905*t^2
"""
import math
from scipy import optimize
dl = 10
g = 9.81
kat_end = 45
def rzut_ukosny(unknown_param):
    v0, kat = unknown_param
    t = dl / (v0*math.cos(math.radians(kat)))
    f_x = v0 * math.sin(math.radians(kat)) * t - ((g * t**2)/2) - 1
    f_y = v0 * (math.cos(math.radians(kat))+math.sin(math.radians(kat))) -(g*t)
    return [f_x, f_y]
    
wynik = optimize.fsolve(rzut_ukosny, [10.4,math.radians(kat_end)])
print("Prędkość początkowa: ", wynik[0],)
print("Kąt początkowy: ",wynik[1])
