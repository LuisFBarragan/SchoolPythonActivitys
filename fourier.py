import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

# 1. Graficado
N = 600
# espacio de la muestra
tmax = 3/4
T = tmax / N # =1.0 / 800.0
x1 = np.linspace(0.0, N*T, N)
y1 = np.sin(50.0 * 2.0*np.pi*x1) + 0.5*np.sin(80.0 * 2.0*np.pi*x1)
yf1 = scipy.fftpack.fft(y1)# transformaciones rápidas de Fourier 
xf1 = np.linspace(0.0, 1.0/(2.0*T), N//2)

# 2. Número de períodos 
tmax = 1
T = tmax / N # espaciado de la muestra 
x2 = np.linspace(0.0, N*T, N)
y2 = np.sin(50.0 * 2.0*np.pi*x2) + 0.5*np.sin(80.0 * 2.0*np.pi*x2)
yf2 = scipy.fftpack.fft(y2)# transformaciones rápidas de Fourier 
xf2 = np.linspace(0.0, 1.0/(2.0*T), N//2)

# 3. Posicionamiento correcto de las fechas en relación con la teoría FFT (naranja en lugar de graficado) 
tmax = 1
T = tmax / N # espaciado de muestra 
x3 = T * np.arange(N)
y3 = np.sin(50.0 * 2.0*np.pi*x3) + 0.5*np.sin(80.0 * 2.0*np.pi*x3)
yf3 = scipy.fftpack.fft(y3)# transformaciones rápidas de Fourier 
xf3 = 1/(N*T) * np.arange(N)[:N//2]

fig, ax = plt.subplots()
# Trazar solo la parte izquierda del espectro para no mostrar el aliasing 
ax.plot(xf1, 2.0/N * np.abs(yf1[:N//2]), label='Transformada de fourier', marker = 'o',linewidth=0.25)
ax.plot(xf2, 2.0/N * np.abs(yf2[:N//2]), label='Número de períodos ', marker = 'o',linewidth=1)
ax.plot(xf3, 2.0/N * np.abs(yf3[:N//2]), label='Posicion correcta de los datos', marker = 'o',linewidth=0.5)
plt.title("Grafica de Fourier")
plt.legend()
plt.grid()
plt.show()