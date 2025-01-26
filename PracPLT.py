import matplotlib.pyplot as plt
import numpy as np

arrayX = np.arange(0,10,0.2)
arrayY = arrayX*np.cos(arrayX)


plt.plot(arrayX, arrayY,color="red",linewidth=5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Funcion cosenoideal')
plt.show()
