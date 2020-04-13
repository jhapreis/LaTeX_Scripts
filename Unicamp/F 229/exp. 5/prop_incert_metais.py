import uncertainties
from uncertainties import ufloat
import numpy as np

#[cobre, aço, chumbo]

# =============================================================================
# Temperaturas medidas
# =============================================================================
T_a = [27, 28, 27] #ºC
T_m = [66, 76, 64]
u_T = 0.2 #ºC
for i in range ( len(T_a) ):
    T_a[i] = ufloat(T_a[i] , u_T)
    T_m[i] = ufloat(T_m[i], u_T)
#print (T_a)
#print (T_m)
#print ()

# =============================================================================
# Masssas medidas
# =============================================================================
m_m = [93.9 , 42.9, 46.1] #g
m_a = [125.6, 202, 228,8] #água + copo; g
m_copo = 6.1 #g
u_m = 0.03
for i in range ( len (m_m) ):
    m_m[i] = ufloat(m_m[i], u_m)
    m_a[i] = ufloat(m_a[i], u_m) - ufloat(m_copo, u_m)
#print (m_m)
#print (m_a)
#print ()

# =============================================================================
# Calor específico da água e capac. tér. do calorímetro
# =============================================================================
c_a = 1 #cal·g⁻¹·ºC⁻¹
C = ufloat(-107, 5) #cal·°C⁻¹


# =============================================================================
# Temperatura final (vem da calibração feita)
# =============================================================================
#y = A*x + B
#delta_V = A*delta_T + B
A = ufloat(0.0575, 0.0005) #mV·ºC⁻¹
B = ufloat(-0.34 , 0.03) #ºC
delta_V = [1.4 , 1.31, 1.31] #mV
u_delta_V = 0.01
delta_T = [0, 0, 0]
T_f = [0, 0, 0]

for i in range (len (delta_V) ):
    delta_T[i] = (delta_V[i] - B) / A
    T_f[i] = delta_T[i] #rubinho
print ('temperaturas finais:', T_f, '°C')

print ()


# =============================================================================
# Expressão dos calores sensíveis
# =============================================================================
Q_c = [0, 0, 0]
Q_a = [0, 0, 0]
Q_m = [0, 0, 0]
c_m = [0, 0, 0]

for i in range ( len(T_f) ):
    Q_c[i] = C * (T_f[i] - T_a[i])
#    print (Q_c)
    
    Q_a[i] = m_a[i] * c_a * (T_f[i] - T_a[i])
#    print (Q_a)
    
    Q_m[i] = ( -Q_c[i] -Q_a[i] )
    c_m[i] =   Q_m[i]   /   (   m_m[i] * (T_f[i] - T_m[i])   )
    
print ('calores específicos dos metais:', c_m, 'cal·g⁻¹·ºC⁻¹')