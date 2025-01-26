import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df =  pd.read_csv('practica.csv')

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

x= df['SalePrice']
y = df['Gr Liv Area']
z = df['Overall Qual']

ax.scatter(x,y,z)
ax.set_xlabel('precio de venta')
ax.set_ylabel('area de construccion')
ax.set_zlabel('calidad general')
plt.show()