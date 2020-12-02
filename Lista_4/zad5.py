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
    t = (2*v0*math.sin(math.radians(kat)))/g
    f_x = v0 * math.cos(math.radians(kat)) * t - 10
    f_y = v0 * math.sin(math.radians(kat)) * t - ((g * t ** 2) / 2) - 1
    
    return [f_x, f_y]
    
wynik = optimize.fsolve(rzut_ukosny, [10.6,math.radians(kat_end)])
print("Prędkość początkowa: ", wynik[0],)
print("Kąt początkowy: ",math.degrees(wynik[1]),)
