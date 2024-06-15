diccionario  = {
    "nombre": "Luisa",
    "apellido": "Porras",
    "edad": 23
}

#print(diccionario)
for key in diccionario :
    print(key) # me muestras las claves
    
for key in diccionario.items() :
    print(key) # con .items() me permite iterar las claves y valores del diccionario

#forma de desagrupar los valores y recorriendo los valores
for datos in diccionario.items() :
    key = datos[0]
    value= datos [1]
    print(f"la clave es {key} y el valor es { value}")  
 