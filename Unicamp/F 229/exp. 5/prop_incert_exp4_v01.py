import uncertainties
from uncertainties import ufloat
import numpy as np

diametro_esferas = [2.49, 2.99, 3.49, 3.95] #mm
u_d = [0.002041241452319, 0.002041241452319, 0.002041241452319, 0.002041241452319] #mm
d = [] #mm
r = [] #mm
for i in range ( len(diametro_esferas) ):
    d.append ( ufloat (diametro_esferas[i], u_d[i]) )
    r.append ( d[i] / 2 )
    print (r[i])
print ()

diametro_tubo = ufloat (55, 0.0102) #mm
R = diametro_tubo / 2
print (R)
print ()

H = ufloat (380, 0.2041) #cm --> mm
print (H)
print ()

k = [] #adimensional
for i in range (len (r) ):
    k.append (  ( 1 + 2.4*r[i]/R ) * ( 1 + 3.3*r[i]/R  ) )
    print (k[i])
print ()
    
r_2 = []
for i in range ( len(r) ):
    r_2.append ( r[i] * r[i] )
    print (r_2[i])
print ()

x = []
for i in range ( len(r_2) ):
    x.append ( r_2[i] / k[i] )
    print (x[i])
    






