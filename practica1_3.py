import pandas as pd
def datos(calificaciones):
    calificaciones = pd.Series(calificaciones)
    #estadisticas=pd.Series([calificaciones.min(),calificaciones.max(), calificaciones.mean(),calificaciones.std()],index=['Min','Max','Media','Desviacion'])
    return calificaciones.describe()

calificaciones={'Ramiro':8, 'Roberto':9, 'Rocio':7, 'Rigoberto':8, 'Cintia':9, 'Maria':10}
print(datos(calificaciones))