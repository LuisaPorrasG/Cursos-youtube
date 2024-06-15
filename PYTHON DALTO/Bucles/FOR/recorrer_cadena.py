cadena = "Hola Luisa"
numeros = [2,5,8,10]



for letra in cadena :
    print(letra)
    
#numeros duplicados con for normal
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append (numero *2)   

print(numeros_duplicados)


#for en una sola linea de código
numeros_duplicados = [x*2 for x in numeros] # expresion matematica,  x  solo es una expresion, este puede ser cambiado
print(numeros_duplicados)