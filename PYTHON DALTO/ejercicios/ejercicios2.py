#cuando el profesor y los alumnos van a armar la clase

#pedir el nombre y la edad de los compañeros que vinieron hoy a clase

def obtener_compañeros (cantidad_de_compañeros):
    compañeros = []
    #ejecutando el for para pedir la información de cada compañero
    for i in range (cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: ")) #int para que se convierta automaticamente a entero
        compañero = (nombre, edad) #creo una tupla con los datos  de nombre y edad
        compañeros.append(compañero) #agrego a la lita de compañeros la tupla con el nombre  y la edad
    compañeros.sort(key=lambda x: x[1]) #sort me sirve para ordenar, en este caso voy a ordenar por la edad que es el 2 parametro [1]
    asistente = compañeros [0][0]
    profesor = compañeros [-1] [0]    #el profesor es el último elemento de la lista -1 y accedemos al nombre [0]
    return asistente, profesor
    
asistentente,profesor = obtener_compañeros(5) #desempaqueto la lista

print(f"El Profesor es {profesor} y su asistente es {asistentente}")

