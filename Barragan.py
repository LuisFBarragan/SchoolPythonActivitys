import time
import numpy as np

matriz = np.ones([1000,1000])
cont = 0
start = time.time()
for i in range(1000):
    for j in range(1000):
        matriz[i][j] = cont
        cont= cont + 1
end = time.time()
Tiempo = end-start
print(matriz[1000-1][1000-1])
print("El tiempo que tardo fue de ",Tiempo,"segundos")