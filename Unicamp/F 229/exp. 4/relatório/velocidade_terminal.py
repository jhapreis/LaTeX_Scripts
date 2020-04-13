import uncertainties
from uncertainties import ufloat
import numpy as np

tempos = [3.4805, 2.53, 1.96333333333333, 1.519]
u_t = [0.096684366195713, 0.02975791211314, 0.017036561990157, 0.023296637811782]
t = []

h = ufloat (140, 0.204124145231931)


for i in range ( len(tempos) ):
    t.append ( ufloat ( tempos[i], u_t[i] ) )
    print (t[i])
    
print ()
v = []
for i in range ( len(tempos) ):
    v.append ( h / t[i] )
    print (v[i])
    
print ()
print (h)