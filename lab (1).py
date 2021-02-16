"""
Created on February 13, 2021
@author : Youri Marchal
"""
import numpy as np
import matplotlib.pyplot as plt

M_d = np.array([0.0, 0.0682, 0.1816, 0.295, 0.4084, 0.5218, 0.7485, 0.9753, 1.4289]) # [kg]
U_d = np.array([0.619, 0.928, 1.456, 1.987, 2.506, 3.035, 4.095, 5.138, 7.163]) + 0.648-0.619 # [V]
coef = np.polyfit(U_d, M_d, 1)

fun = np.poly1d(coef)

#Force on the cylinder

g = 9.81 # [m/s^2]
Cd = 0.09
kd = coef[0] #[kg/V]
V0 = 0.648 # [V]
U = 2.9 # [V]
Fd = kd * (U - V0) * g # [N]
print('Force on the cylinder ',Fd,' [N]')

#other data
l = 0.5 # [m]
D = 0.05 # [m]
angles = np.concatenate((np.linspace(-10, 10, 5), np.linspace(20, 180, 17)))
h = np.array([14.2, 15.5, 16.1, 16.0, 15.2, 9.9, 3.8, -3.1, -10.3, -15.7, -18.2, -15.8, -15.0, -15.0, -14.9, -14.8,
              -14.9, -15.1, -15.6, -16.1, -15.3, -15.6]) # [mm]

rho_water = 1000.0 # [kg/m^3]
delta_p_dyn = rho_water*g*h*1e-3 # [Pa]
print(1e6,10e-1)
rho_air = 1.204 # [kg/m^3]
nu_air = 1.506e-5 # [m^2/s]

#interpolation of a parabole
coef2 = np.polyfit(angles[0:4], delta_p_dyn[0:4],2)
x_angles = np.linspace(angles[0], angles[4], 100)
y_p = np.polyval(coef2, x_angles)


x_max = -coef2[1]/(2*coef2[0]) #summit of the parabole
print('summit of the parabole : ', x_max) #rad # Attention on oppose le signe

#1) dynamic pressure of the inflow # At the stagnation point p_tot = p_stat At the pitot tube p_tot = p_stat + 0.5*rho*u^2 <==> we can find u
p_max = max(y_p)
print('Max delta pressure : ', p_max, ' [Pa]')

u_inf = np.sqrt(2*p_max/rho_air)
Re_d = u_inf*D/nu_air

print('Speed infinity, ', u_inf, ' [m/s]')
print('Reynolds number ,', Re_d)

# Static pressure around the stagnation point (-10 deg --> 10 deg)
# p_stat =

# Pressure coefficient from -10 deg to -180 deg
# C_p =

#Cd with the balance

Cd_bal = Fd/(0.5*rho_air*u_inf**2*D*l)
print('Cd with the balance : ', Cd_bal)


#graphics

plt.rcParams.update({'font.size': 22})
#plt.rc('text', usetex=True)

fig1 = plt.figure(figsize=(14.0, 8.0))
plt.scatter(U_d, M_d, color='royalblue')
plt.plot(U_d, M_d)
plt.grid()
plt.ylabel(r'$Hung$ $mass$ $[kg]$')
plt.xlabel(r'$Tension$ $[V]$')

fig2 = plt.figure(figsize=(14.0, 8.0))
plt.scatter(angles, delta_p_dyn, color='royalblue')
plt.plot(angles, delta_p_dyn)
plt.plot(x_angles,y_p,'-r')
plt.grid()
plt.xlabel(r'$Angle$ $of$ $the$ $cylinder$ $[^\circ]$')
plt.ylabel(r'$Dynamic$ $pressure$ $[Pa]$')
plt.show()

#coucou Johnny
