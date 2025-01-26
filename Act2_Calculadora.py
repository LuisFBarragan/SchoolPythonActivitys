Fin = True
while Fin == True:
 print("Menu")
 print("1.- Suma")
 print("2.- Resta")
 print("3.- Multiplicacion")
 print("4.- Division")
 print("5.- Salir")

 respuesta = int(input("Introduzca una opcipon: \n"))

 if respuesta == 5:
     print("Se salio de la opcion correcatamente")
     Fin = False
     break

 a = int(input("Da el primer nuemro: \n"))
 b = int(input("Da el segundo nuemro: \n"))
 
 if respuesta == 1:
    def suma (a,b):
     resultado = a + b
     return resultado
    print("El resultado de la suma es: ",suma(a,b))
 
 elif respuesta == 2:
    def resta (a,b):
     resultado = a - b
     return resultado 
    print("El resultado de la rseta es: ",resta(a,b))

 elif respuesta == 3:
     def multi (a,b):
      resultado = a * b
      return resultado
     print("El resultado de la Multiplicacion es: ",multi(a,b)) 

 elif respuesta == 4:
     def divi (a,b):
      resultado = a / b
      return resultado
     print("El resultado de la division es: ",divi(a,b)) 
 