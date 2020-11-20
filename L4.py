#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Base para la solución del Laboratorio 4

# Los parámetros T, t_final y N son elegidos arbitrariamente

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#var = varianza
var = 8
# w0 constante real
w0= np.pi

# Variables aleatorias A y Y
vaX = stats.norm(0, np.sqrt(var))    #CAMBIE X POR A y 3 por 0
vaY = stats.norm(0, np.sqrt(var))   # -np.pi/2, np.pi norm e ves de unifor y +0

# Creación del vector de tiempo
T = 100			# número de elementos
t_final = 10	# tiempo en segundos
t = np.linspace(0, t_final, T)

# Inicialización del proceso aleatorio X(t) con N realizaciones
N = 10
X_t = np.empty((N, len(t)))	# N funciones del tiempo x(t) con T puntos

# Creación de las muestras del proceso x(t) (X y Y independientes)
for i in range(N):
	X = vaX.rvs()   #a por x
	Y = vaY.rvs()    # z por y
	w_t = X *np.cos(w0*t) + Y *np.sin(w0*t)  #np.cos(np.pi*t + Z)
	X_t[i,:] = w_t
	plt.plot(t, w_t) #w por x

# Promedio de las N realizaciones en cada instante (cada punto en t)
P = [np.mean(X_t[:,i]) for i in range(len(t))]
plt.plot(t, P, lw=6)

# Graficar el resultado teórico del valor esperado
E = 0*t   #6/np.pi * np.cos(np.pi*t)
plt.plot(t, E, '-.', lw=4)

# Mostrar las realizaciones, y su promedio calculado y teórico
plt.title('Realizaciones del proceso aleatorio $X(t)$')
plt.xlabel('$t$')
plt.ylabel('$x_i(t)$')
plt.show()

# T valores de desplazamiento tau
desplazamiento = np.arange(T)
taus = desplazamiento/t_final

# Inicialización de matriz de valores de correlación para las N funciones
corr = np.empty((N, len(desplazamiento)))

# Nueva figura para la autocorrelación
plt.figure()

# Cálculo de correlación para cada valor de tau
for n in range(N):
	for i, tau in enumerate(desplazamiento):
		corr[n, i] = np.correlate(X_t[n,:], np.roll(X_t[n,:], tau))/T
	plt.plot(taus, corr[n,:])

# Valor teórico de correlación
Rww =  var*np.cos(w0*taus)

# Gráficas de correlación para cada realización y la
plt.plot(taus, Rww, '-.', lw=4, label='Correlación teórica') # acmbio a Rww
plt.title('Funciones de autocorrelación de las realizaciones del proceso')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$R_{ww}(\tau)$')
plt.legend()
plt.show()
                     
# Gráfica del valor medio
plt.plot(taus, E, '-.', lw=4, label='Valor teórico de la media')
plt.title('Valor teórico de la media')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$E[W(\tau)])(\tau)$')
plt.legend()
plt.show()
                     

