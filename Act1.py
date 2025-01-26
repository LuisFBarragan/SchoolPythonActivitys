import pandas as pd

inicio = int(input('Introduce el año inicial '))
fin = int(input('Introduce el año final '))
ventas={}

for i in range(inicio, fin):
    ventas[i] = float(input('Introduce las ventas del año '+str(i)+';'))

ventas =pd.Series(ventas)
print('ventas\n', ventas)