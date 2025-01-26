import pandas as pd

def comportamiento(fichero):
    df=pd.read_csv(fichero,sep=';',decimal=',',thousands='.',index_col=0)
    rl= pd.DataFrame([df.min(),df.max(),df.mean()], index=['Min','Max','Media'])
    print(rl)
    return rl
    

comportamiento('cotizacion.csv')