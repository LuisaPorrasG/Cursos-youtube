#definiendo funcion saldudar
def saludar ():
    print ("Hola mundo")

saludar()    

#crear una funcion que tenga parámetros
def saludar2 (nombre):
    print(f"Hola {nombre}, como estas?")

saludar2("Luisa")
saludar2("Fernanda")

#creando una funcion como la de arriba pero pidiendo el dato

nombre = input ("Ingresa tu nombre: ")
def  saludar_nombre ():
    print(f"hola {nombre}, como vas?")
saludar_nombre()

#creando una funcion con dos parametros

def  saludar3 (nombre1, sexo):
    sexo = sexo.lower()
    if(sexo == "mujer"):
        print(f"Hola guapa {nombre1}, como vas")
    elif (sexo == "hombre"):
        print(f"Hola guapo {nombre1} como vas")
    else:
        print(f"Hola linde {nombre1} como vas")

saludar3("Luisa","mujer")
saludar3("Diana","nose")
saludar3 ("jose","hombre")

#crear una funcion que nos retorne valores

def crear_contraseña (num):
    char = "abcdefghij"
    numero_entero = str(num) #convertir a string el primer numero 
    num = int (numero_entero[0]) #numero entero que obtenga el valo inical del string
    c1 = num -2 #caracter 1 es igual al numero - 2
    c2 = num #caracter 2 es igualal numero de sitrin
    c3 = num -5
    contraseña = f"{char[c1]}{char[c2]}{char[c3]}{num*2}"#h,j,e,18
    print(contraseña)
    return contraseña, num
crear_contraseña(98)

password, primer_numero = crear_contraseña(23) #sempaquetando contraseña y primer numero, claramente antes tiene que retornar los dos valores
print(f"Tu contraseña es {password}")
print(f"El numero usado para la contraseña es {primer_numero}")
