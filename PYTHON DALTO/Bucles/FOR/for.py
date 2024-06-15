animales = ["perro", "gato", "loro", "cocodrilo"]
numeros = [10,62,12,72]

for animal in animales:
    print(f"Ahora animal es = {animal}")
#recorriendo la lista numeros y multiplicando el valor por 10    
for numero in numeros:
    resultado = numero *10
    print(resultado)
    
#iterar 2 listas al mismo tiempo con zip

for numero, animal in zip(animales, numeros):
    print(f"Recorriendo lista 1 {numero}") 
    print(f"Recorriendo lista 2 {animal}")   
    

for num in range (5,10):
    print(num)  #muestra numeros del 5 al 10
    
#recorrer una lista por el  indice, sin embargo no es la forma correcta    
for num in range (len(numeros)):
    print(numeros[num])  
    
#forma correcta re recorrer una lista

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