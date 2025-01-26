import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('practica.csv')
fig, ax =plt.subplots(2,figsize = (10,6))
ax[0].scatter(x =df['Gr Liv Area'], y =df['SalePrice'])
ax[0].set_xlabel('terreno de cosntruccion')
ax[0].set_ylabel('Precio de la casa')
#
ax[1].scatter(x =df['Overall Qual'], y =df['SalePrice'])
ax[1].set_xlabel('calidad general')
ax[1].set_ylabel('precio de la casa')

plt.show()