import pandas as pd
from  pandas.core.frame import DataFrame

#Generar un DataFrame con los datos de los ficheros.
balance18 = pd.read_csv('BALANCE_2018.csv',sep=',')
balance19 = pd.read_csv('BALANCE_2019.csv',sep=',')
balance20 = pd.read_csv('BALANCE_2020.csv',sep=',')
bg = pd.concat([balance18,balance19,balance20])
print(bg)

#Crear una nueva columna con el nombre de [DIFERENCIA] en la cual se escribirá el resultado de ventas - gastos.
print('Columna con el nombre de [DIFERENCIA] en la cual se escribirá el resultado de ventas - gastos')
resta = bg['VENTAS']-bg['GASTOS']
bg = bg.assign(DIFERENCIA=resta)
print(bg)

#Eliminar las filas en las cuales el ingreso sea =0 (dropna, iloc, etgc)
print('Eliminar las filas en las cuales el ingreso sea = 0')
elimina = bg.replace({'VENTAS':0},pd.NA)
print(elimina.dropna())

#Reemplazar los valores de 0 por 100 en cada uno de los registros de la fila de gastos
print('Reemplazar los valores de 0 por 100 en cada uno de los registros de la fila de gastos')
remplaza = bg.replace({'VENTAS':0},100)
print(remplaza)

#Generar un archivo csv con el DataFrame resultante, el nombre del archivo será: "final.csv" 
bg.to_csv('final.csv')