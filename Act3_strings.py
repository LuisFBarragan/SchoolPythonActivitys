#Manejo de strings
print("hola mundo")

# concatenar
salida= "hola"+ ' '+"mundo"
print(salida)

#multiplicacion 
resultado= "hola"*10
resultado1= "mundo"
print(resultado + resultado1)

#añadidura
sentencia1 = 'hola'
sentencia1 += " "
sentencia1 += "mundo"
print(sentencia1)

#extension de caracteres(medicion)
salida1=' predrito'+' '+'come un helado'
print(len(salida1))

#busqueda de cadenas
base="musica de los 80"
base1= base.find("musica")
print(base1) #6

#case versus
hash="pablito tiene 2 pesos"
hash1= hash.find("pesos")
print(hash1)#-1

#tipar minusculas
tip= "HOLA buen DIA a TODOS"
tip1= tip.lower()
print(tip1)

#tipar mayusculas
top =  "HOLA buen DIA a TODOS"
top1= top.upper()
print(top1)

# reemplazar cadenas
cad1= "volando sobre el pantano"
cad2= cad1.replace("o","a")
print(cad2)

# corte de cadenas
cut ="hola mundo"
cut1= cut[2:6]
print(cut1)

# corte de string por medio de varibles  de prametros
cer ="hola mundo"
ini=2
fini=6
med=cer[ini:fini]
print(med)

# metodo(secuencia) escape
print('\"')
#"

print('ese letrero dice que: \"tenemos que salirnos en la siguiente calle\"')
# ese letrero dice que: "tenemos que salirnos en la siguiente calle"

print('flor\ flor\ flor\n amarilla')
#flor flor flor
#amarilla

#count() contabiliza los caracteres de un string
countcad = "Hola mundo"
print(countcad.count("o") )

#capitalize() devuelve una copia de la cadena con la primera letra en mayúscula
Capitalizecad = 'hola'
print(Capitalizecad.capitalize())

#isalnum() devuelve cierto si la cadena es no vacía y sólo contiene letras y dígitos.
cadena_isalnum = "a1bc"
print(cadena_isalnum.isalnum())

#isalpha() devuelve cierto si la cadena es no vacía y sólo contiene letras.  
isalphacad2 = "Abcdd"
isalphacad3 = "12345"
print("cadena letras: ",isalphacad2.isalpha())
print("cadena solo numeros: ",isalphacad3.isalpha())

#isdigit() devuelve cierto si la cadena es no vacía y sólo contiene dígitos.
isd1='123123'
isd2='Hi xdd'
print("cadena solo numeros: ",isd1.isdigit())
print("cadena solo letras: ",isd2.isdigit())

#islower() devuelve cierto si todas las letras de la cadena son minúsculas y hay al menos una minúscula.
islcad="hola"
islcad2="HOLA"
print("cadena miniscula: ",islcad.islower())
print("cadena mayuscula: ",islcad2.islower())

#isspace() devuelve cierto si la cadena es no vacía y todos sus caracteres son espacios.
cadena_vacia=("       ")
cadena_novacia=(" a e i o u ")
print("Cadena vacia con espacio",cadena_vacia.isspace())
print("cadena no vacia con letras: ",cadena_novacia.isspace())

#isupper() devuelve cierto si todas las letras de la cadena son mayúsculas y hay al menos una mayúscula.   
cadena_May="MAYUSCULAS"
cadena_min="minusculas"
print(cadena_May.isupper())
print(cadena_min.isupper())

#lstrip() devuelve una copia de la cadena con los blancos iniciales omitidos
cadena_lstrip = "Hola o hi"
print(cadena_lstrip.lstrip())

#split([s]) devuelve una lista que contiene las palabras de la cadena. Si se incluye la cadena s, se utiliza como separador.
cadena_split = "Esta es una prueva" 
print(cadena_split.split('e'))

#Uso del ciclo for con srtings
cad="la tierra es redonda"
print("uso de for: ")
for i in cad:
  print(i)

#Uso de subsecuencias 
a ="cadena"
print(a[3])
print(a[-1])
print(a[3:5])
print(a[2:-2])
print(a[:3])
print(a[3:])