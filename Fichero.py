#argumento
# r: letura solamente 
# w: escritura
# a: escritura 
# r+: permite leer y escribir
# w+: permite leer y escribir, pero borra el contenidoanterior 
# a+: permite leer y escribir, y hace un append al final deldocumento.
# b: de binary y agragado a los argumentos, permite hacer las funcines antes descritas leyendo y escribiendobinarios 

fichero = open("archivo.txt","w")  

#lineas de escritura 
fichero.write("Hola, soy la funcion escribir \n")
fichero.write("esta es una linea. \n")
fichero.write("esta es una linea. \n")
fichero.write("esta es una linea. \n")
fichero.close()#Para cerrarS

#lineas de lectura 
#ficheror = open("archivo.txt","r") 
#cuerpo = ficheror.read()
#print(cuerpo)
#ficheror.close()#para cerrar

#ficheror = open("archivo.txt","r") 
#print(ficheror.readline())
#print(ficheror.readline())
#ficheror.close()

#ficheror = open("archivo.txt","r")
#for l in ficheror.readline():
    #print(l)
#ficheror.close()

# seek(): permite pocisionarse en una determinada parte del fichero.
#ficheror = open("archivo.txt","r") 
#ficheror.seek(10)
#print(ficheror.read())
#ficheror.close()

# r+: permite leer y escribir(sobrescribe)
'''fichero1 = open("archivo.txt","r+")  
fichero1.write("Iniciamos las pruebas ")

fichero1.seek(0)
print(fichero1.read())
fichero1.close()
'''
# w+: permite leer y escribir, pero borra el contenidoanterior (Borra todo y escribe de nuevo)
fichero1 = open("archivo.txt","w+")  
fichero1.write("Pruebas parte 2 \n")
fichero1.write("Nueva linea \n")

fichero1.seek(0)
print(fichero1.read())
fichero1.close()


# a+: permite leer y escribir, y hace un append al final deldocumento. (Escribe abajpo de lo que ya esta escrito)
fichero1 = open("archivo.txt","a+")  
fichero1.write("Y ya con esta son todas las pruebas \n")
fichero1.write("Ultima linea de las pruebas <3 \n")

fichero1.seek(0)
print(fichero1.read())
fichero1.close()









  