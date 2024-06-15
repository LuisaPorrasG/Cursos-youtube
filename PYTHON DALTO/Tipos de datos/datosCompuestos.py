#LAS LISTAS SON DIFERENTES A LOS ARREGLOS
lista  = ["Luisa", "Porras", True, 1.60]#con corchete  se puede modifiticar los datos
tupla  = ("Luisa", "Porras", True, 1.60) # no se puede modificar los datos
print(lista)
print(lista[1]) #devuelve el elemento dos de la lista, empieza desde 0
lista [3] = 1.62
print(lista)


#CONJUNTO o SET, para ello se usa la función set

conjunto ={"Luisa", "Porras", True, 1.60, "Luisa"} #tampoco se puede modificar los datos
#no se puede:
#conjunto[1] = "Fernanda"
#no me deja acceder a los indices del conjunto:
#print(conjunto[1])
#pero si se pude mostrar todo el conjunto por indices pero si se puede iterar y no me deja mostrar elementos repetidos
print(conjunto)


#DICCIONARIO -> ES COMO UN JSON EN JAVASCRIP, es decir datos clave -valor

diccionario = {
    # "en vez de  buscar por el indice de dato, se busca por el nombre del valor"
    "nombre":"Luisa",
    "apellido": "Porras",
    "edad" : 23,
    "mujer" : True,
    "edadx2": 23
    
}
print(diccionario)
print(diccionario["nombre"])



