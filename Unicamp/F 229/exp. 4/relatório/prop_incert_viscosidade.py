import uncertainties
from uncertainties import ufloat
import numpy as np

A = ufloat (33.717, 0.9866) #mm⁻¹·s⁻¹
#A = ufloat (34, 0.9866) #mm⁻¹·s⁻¹

rho_1 = 7.82 #g·cm⁻³
rho_2 = 1.2 #g·cm⁻³
g = 9.8 #m·s⁻²

#A = 2/9·(rho_1 - rho_2)·g / eta
eta = 2 * (rho_1 - rho_2) * g / (9*A) #Pa·s
eta = 1000*eta #mPa·s

print ('eta =', eta, 'mPa·s')