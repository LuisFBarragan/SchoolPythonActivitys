cadena = """
Otelo es una de las obras más conocidas de Shakespeare. Es un drama sobre los efectos de los celos. Otelo es un 
general de Venecia en la época más poderosa del imperio veneciano. Tras triunfar en varias batallas es nombrado gobernador
de Chipre que pertenecía en esa época a Venecia. Se casa con la hija de un rico veneciano llamada Desdemona. El matrimonio
es muy feliz en los inicios. Otelo está profundamente enamorado de Desdemona por su feminidad y dulzura y ella a su vez
de su masculinidad y fortaleza. Ambos se instalan en Chipre en el Palacio del Gobernador. El tercer gran protagonista de
Otelo es Yago. Es un subordinado de Otelo que quiere destruirle. Toma como aliado a Rodrigo que está enamorado de 
Desdemona y se siente muy frustrado por haber sido rechazado por ella y que Desdemona haya preferido a Otelo que es
un moro de piel oscura. La estrategia de Yago es hacer que Otelo se ponga muy celoso. Para ello lo primero que hace
es inducir sospechas sobre una relación adultera entre Casio, el número dos del gobierno de Chipre, y la propia
Desdemona. Roba a Desdemona un pañuelo que había sido regalado en un momento muy especial por Otelo y lo introduce
en las habitaciones de Casio. De esta manera empieza a sembrar en Otelo dudas sobre la fidelidad de su mujer.
Otelo es un hombre directo, muy posesivo y excesivamente apasionado. El amor loco que siente por su mujer, unido
a una cierta inseguridad por el color de su piel, hace que empiece a creerse las acusaciones de Yago, que
utiliza estratagemas muy diversas.
"""

menu = """
-----Menu-----
1.- Replace
2.- Find 
3.- Count
4.- Upper
5.- Lower
6.- Salir        
-----------------
"""
Fin = True
while Fin == True:
    print(menu)
    op = int(input("Introduzca una opcipon a elegir: \n"))

    if op == 1:
      print("-----Metodo Replace()-----")
      replace1 = input("Ingrese la cadena a cambiar: \n")
      replace2 = input("Ingrese la cadena por la que se va a cambiar: \n")
      cadenaR = cadena.replace(replace1,replace2)
      print("La cadena nueva queda: \n",cadenaR)

    elif op == 2:
      print("-----Metodo Find()-----")
      Findd = input("Ingrese la cadena a buscar: \n")
      cadenaF= cadena.find(Findd)
      print(cadenaF)
            
    elif op == 3:
      print("-----Metodo Count()-----")
      Count = input("Ingrese cadena que se desea a contar: \n")
      print(cadena.count(Count))
    
    elif op == 4:
      print("-----Metodo Upper()-----")
      cadenaUP = cadena.upper()
      print(cadenaUP)

    elif op == 5:
      print("-----Metodo Lower-----")
      CadenaLow = cadena.lower()
      print(CadenaLow)
            
    elif op == 6:
      Fin = False
      print("Se salio del programa correctamente")
     