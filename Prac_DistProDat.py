import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

n = 10000
valor = {}
calif = {}
area = {}
for i in range (n):
    valor[i] = np.random.randint(350000,1250000)
    calif[i] = np.random.randint(-10,10)
    area[i] = np.random.randint(150,5000)

#Exportar los tres arreglos a un solo  DataFrame
df = pd.DataFrame({'Valor':valor,'Calificacion':calif,'Area':area})
print('Creacion dataframe: \n',df)

#Buscar en la columna de Calificacion del DataFrame cada elemento que tenga símbolo negativo o menor o igual a 0 (<=0) 
# y elevar el numero al cuadrado y el resultado guardarlo en la misma posición.
y = lambda x: (x**2 )**(0.5) if x<=0 else x
df['Calificacion'] = df['Calificacion'].map(y)
print('<=0**2: \n',df)

#Buscar en la columna de Valor del DataFrame aquellos elementos que sobrepasen del 1'150,000 y eliminar toda la fila 
#en la que se encuentra el dato en cuestión
indexNames = df[ (df['Valor'] >1150000)].index
df.drop(indexNames , inplace=True)
print('eliminar elementos >1150000: \n',df)

#Reemplazar por el 6 en la columna calificación todos los elementos cuyo valor sea 0.
df['Calificacion'] = df['Calificacion'].replace(0,6)
print(df)

#Obtener los percentiles 25, 50 y 75  del DataFrame.
p1 =  np.percentile(df,25)
p2 =  np.percentile(df,50)
p3 =  np.percentile(df,75)
print("percentiles \n","25: ",p1,"\n 50: ",p2,"\n 75: ",p3)

#Exportar el DataFrame a un archivo que lleve el nombre de  resultado.csv 
df.to_csv('Resultado.csv')

#Graficar en matplotlib la columna Valor y Calificación en los ejes X y Y #respectivamente utilizando por lo menos 2 
#marcadores de matplotlib.
plt.scatter(x =  df['Calificacion'],y = df['Valor'])
plt.title('Producto 1')
plt.xlabel('Calificacion')
plt.ylabel('Valor')
plt.savefig('Producto1.png')
plt.show()

#Graficar en matplotlib la columna Valor y Area en los ejes X y Y respectivamente utilizando por lo menos 2 marcadores de 
#matplotlib.
plt.scatter(x = df['Area'],y =  df['Valor'])
plt.title('Producto 2')
plt.ylabel('Valor')
plt.xlabel('Area')
plt.savefig('Producto2.png')
plt.show()