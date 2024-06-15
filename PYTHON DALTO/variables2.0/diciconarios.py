#creando diccionario con dict()

diccionario = dict(
    nombre = "Luisa",
    apellido = "Porras", 
    edad = 23
)

print(diccionario)

#las listas no pueden ser claves [],  pero las tuplas si ()

diccionario = {("Luisa", "Porras"): "jejeje"}
print(diccionario)
#diccionario = {["Luisa", "Porras"]: "jejeje"} # no puedo por que es una lista , sin embargo puedo congelarla
diccionario = {frozenset(["Luisa", "Porras"]): "Jelou"} # ahora si me deja por que se vuelve inmutable
print(diccionario)


#creando diccionarios con fromkeys

diccionario = dict.fromkeys (["nombre", "apellido"]) #pongo la lista para que no me itere cada elemento
print(diccionario)

#con 1 parametro
diccionario = dict.fromkeys ("ABCD") # me itera cada elemento, es decir que ccada letra clave va uedar con un valor none
print(diccionario)

#con 2 parametros
diccionario = dict.fromkeys ("ABCD", 2) # cada letra va tener como valor 2

