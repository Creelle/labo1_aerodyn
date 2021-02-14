"""
Created on February 13, 2021
@author : Youri Marchal
"""
import numpy as np
import matplotlib.pyplot as plt

M_d = np.array([0.0, 0.0682, 0.1816, 0.295, 0.4084, 0.5218, 0.7485, 0.9753, 1.4289]) # [kg]
U_d = np.array([0.619, 0.928, 1.456, 1.987, 2.506, 3.035, 4.095, 5.138, 7.163]) + 0.648 # [V]
coef = np.polyfit(M_d, U_d, 1)
fun = np.poly1d(coef)

# F_d = k_d * (U_d - V0) # [N]
nu_air = 1.516*1e-5 # [m^2/s]
rho_air = 1.204 # [kg/m^3]
l = 0.5 # [m]
d = 0.05 # [m]
angles = np.concatenate((np.linspace(10, -10, 5), np.linspace(-20, -180, 17)))
h = np.array([14.2, 15.5, 16.1, 16.0, 15.2, 9.9, 3.8, -3.1, -10.4, -15.7, -18.3, -15.8, -15.0, -15.0, -14.8, -14.7,
              -14.9, -15.1, -15.5, -16.1, -15.3, -15.6]) # [mm]
rho_water = 1000.0 # [kg/m^3]
g = 9.81 # [m/s^2]
p_dyn = rho_water*g*h*1e-3 # [Pa]
U = np.sqrt(2*p_dyn/rho_air)
Re = U*d/nu_air

plt.rcParams.update({'font.size': 22})
plt.rc('text', usetex=True)

fig1 = plt.figure(figsize=(14.0, 8.0))
plt.scatter(M_d, U_d, color='royalblue')
plt.plot(M_d, U_d)
plt.grid()
plt.xlabel(r'$Hung$ $mass$ $[kg]$')
plt.ylabel(r'$Tension$ $[V]$')

fig2 = plt.figure(figsize=(14.0, 8.0))
plt.scatter(angles, p_dyn, color='royalblue')
plt.plot(angles, p_dyn)
plt.grid()
plt.xlabel(r'$Angle$ $of$ $the$ $cylinder$ $[^\circ]$')
plt.ylabel(r'$Dynamic$ $pressure$ $[Pa]$')
plt.show()

fig3 = plt.figure(figsize=(14.0, 8.0))
plt.scatter(angles, U, color='royalblue')
plt.plot(angles, U)
plt.grid()
plt.xlabel(r'$Angle$ $of$ $the$ $cylinder$ $[^\circ]$')
plt.ylabel(r'$Velocity$ $U_\infty$ $[m/s]$')
plt.show()

fig4 = plt.figure(figsize=(14.0, 8.0))
plt.scatter(angles, Re, color='royalblue')
plt.plot(angles, Re)
plt.grid()
plt.xlabel(r'$Angle$ $of$ $the$ $cylinder$ $[^\circ]$')
plt.ylabel(r'$Reynolds$ $number$ $[-]$')
plt.show()