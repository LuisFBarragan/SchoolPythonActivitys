#Primeramente importamos las siguientes librerías:
import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(100)
y = np.random.randn(100)
t = np.arange(100)

plt.scatter(x, y, c=t)
plt.show()