cadena1 ="Hola, soy, Luisa"
cadena2 ="HoLamakInola"
cadena3 ="Eres fuerte y valiente"

#print(dir(cadena1))
resultado = dir(cadena1) #dir es una funcion la cual posee de metodos que puedo usar en una cadena o cualquier tipo de dato
print(resultado)

#UPPER->conveirte la cadena de texto a máyusculas
resultado = cadena1.upper()
print(resultado)

#LOWER->conveirte la cadena de texto a Minusculas
resultado = cadena1.lower()
print(resultado)

#CAPITALIZE->conveirte la primera letra a máyuscula
resultado = cadena1.capitalize()
print(resultado)

#FIND-> Buscamos la posicion de la cadena, si no encuentra nada me devuelve -1
resultado = cadena1.find("Hola") # posición 0
print(resultado)
resultado = cadena1.find("soy") # posición 0
print(resultado)

#INDEX-> Buscamos una cadena en otra cadena, si no encuentra nada me devulve una excepcion o erro
#resultado = cadena1.index("!") # posición 0
#print(resultado)

#ISNUMERIC-> Si es un numero devuelve  un True
resultado = cadena1.isnumeric() 
print(resultado)

#ISALPHA-> Si es alfanumerico devuelve  un True
resultado2 = cadena2.isalpha()#true porque son alfanumericos, ojo los espacio son caracteres pero no alfanumericos
print(resultado2)

#COUNT-> Devuelve la coincidencia de la cadena
resultado = cadena2.count("a")#hay tres coincidencias en la cedena, si no se encuentra devulve 0
print(resultado)

#LEN-> Devuelve la longitud de la cadena, ojo len si es una función por lo tanto su escritura o llamado es diferente
resultado = len(cadena1) #tiene 14 caracteres incluyendo los espacios
print(resultado)

#STARTSWIND-> COrrobora si una cadena comeiza por : x, este es un metodo
resultado = cadena1.startswith("H") #True
print(resultado)

#ENDSWIND-> COrrobora si una cadena Finaliza por : x, este es un metodo
resultado = cadena1.endswith("H") #False
print(resultado)

#REPLACE-> REmplaza un valor por otro
resultado = cadena1.replace("Hola", "Hi") #False
print(resultado)

#SPLIT-> Devuelve una matris o cadena

resultado = cadena1.split(",")   # separo la cadena por las comas que hay
print(resultado)
resultado = cadena3.split()   # separo la cadena por las los espacios
print(resultado)