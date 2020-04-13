import uncertainties
from uncertainties import ufloat
import numpy as np

#Temperaturas medidas
T_F = ufloat(29 , 0.2) #ºC
T_Q = ufloat(80 , 0.2) #ºC
#print (T_F , T_Q)

#Masssas medidas
m_F = ufloat(200.8 , 0.03) - ufloat(6.1 , 0.03)
m_Q = ufloat(423.6 , 0.03) - ufloat(377.2 , 0.03)
#print (m_F , m_Q)

#Calor específico da água
c_a = 1 #cal·g⁻¹·ºC⁻¹

#Temperatura final (vem da calibração feita)
#y = A*x + B
#delta_V = A*delta_T + B
A = ufloat(0.0575, 0.0005) #mV·ºC⁻¹
B = ufloat(-0.34 , 0.03) #ºC
delta_V = ufloat (2.34 , 0.01) #mV

delta_T = (delta_V - B) / A
T_f = delta_T

#Expressão da capacidade térmica

Q_Q = m_Q*c_a*(T_f - T_Q)
#print (-Q_Q)
Q_F = m_F*c_a*(T_f - T_F)
#print (-Q_F)
Q_C = ( -Q_Q - Q_F )
C = Q_C / (T_f - T_F) 

print ('T_f =', T_f, 'ºC')
print ("C =", C, 'cal·°C⁻¹' )