import pandas as pd

#Generamos el DataFrame.
barquito = pd.read_csv('velero.csv', index_col=0)
print(barquito)

#Mostrar por pantalla: 
print('Dimensiones:', barquito.shape)
print('Número de elemntos:', barquito.size)
print('Nombres de columnas:', barquito.columns)
print('Nombres de filas:', barquito.index)
print('Tipos de datos:\n', barquito.dtypes)
print('Primeras 10 filas:\n', barquito.head(10))
print('Últimas 10 filas:\n', barquito.tail(10))

#Datos del pasajero con identificador 148
print('Pasajero 148:\n ',barquito.loc[148])

#Filas pares del DataFrame.
pares =barquito.iloc[range(0,barquito.shape[0],2)]
print('Filas pares:\n ',pares)

#Personas que iban en primera clase ordenadas alfabéticamente.
ordAlf = barquito[barquito["Pclass"]==1]['Name'].sort_values()
print('Personas que iban en primera clase ordenadas alfabéticamente: \n',ordAlf)

#Porcentaje de personas que sobrevivieron y murieron
Porcentaje = ((barquito['Survived'].value_counts()/barquito['Survived'].count())* 100)
print('Porcentaje de personas que sobrevivieron y murieron: \n',Porcentaje)

#Porcentaje de personas que sobrevivieron en cada clase
Porcentaje2 = barquito.groupby('Pclass')['Survived'].value_counts(normalize=True)
print('Porcentaje de las personas que sobrevivieron en cada clase: \n', Porcentaje2)

#Eliminar del DataFrame los pasajeros con edad desconocida.

barquito.dropna(subset=['Age'])

#Edad media de las mujeres que viajaban en cada clase.
edad = barquito.groupby(['Pclass','Sex'])['Age'].mean().unstack()['female']
print('Edad media de las mujeres que viajaban en cada clase: \n',edad)

#Añadimos una nueva columna booleana para ver si el pasajero era menor de edad o no.
barquito['Young'] = barquito['Age'] < 18

#Porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
Porcentaje3 =barquito.groupby(['Pclass', 'Young'])['Survived'].value_counts(normalize = True) * 100
print('orcentaje de menores y mayores de edad que sobrevivieron en cada clase: \n',Porcentaje3)