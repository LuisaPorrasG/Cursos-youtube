animales = ("gato", "perro", "loro", "cocodrilo")
numeros = (16,72,52,14)

for animal in animales:
    print(f"Ahora animal es = {animal}")
#recorriendo la conjunto numeros y multiplicando el valor por 10    
for numero in numeros:
    resultado = numero *10
    print(resultado)
    
#iterar 2 conjuntos al mismo tiempo con zip

for numero, animal in zip(animales, numeros):
    print(f"Recorriendo conjunto 1 {numero}") 
    print(f"Recorriendo conjunto 2 {animal}")   
    

#forma correcta re recorrer una conjunto
for num in enumerate (numeros):
    #print(type(num)) tipo tuplas, por eso tengo dos valores uno del indice y otro el valor del indice  ..podría desempaquetarse
    indice = num[0]
    valor = num [1]
    print(f"el indice es : {indice} y el valor es {valor}")
    
#usando el for/else --> else siempre se va a ejecutar
for numero in numeros:
    print(f"ejecutando el último bucle, el valor actual: {numero}")
else:
    print("el bucle termino")