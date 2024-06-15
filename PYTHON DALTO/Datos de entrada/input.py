#pedirle un dato al usuario
#ojo un input siempre devuelve un texto así ingresemos un numero
nombre = input("Ingrese su nombre:")
print("el nombre ingresado es: " +  nombre)

numero = input("ingrese su edad: ")
numero = numero *2
print(f'este seria el numero multiplicado por 2? {numero}') #se concatena el valor mas no se realiza la operación

#convierto el numero a entero para poder haccer una función matematica, puedo convertirlo en float támbien
numero2 = input("ingrese su edad: ")
numero2 = int(numero2)*2 
print(f"así si se realiza una multiplicaicón: {numero2}")