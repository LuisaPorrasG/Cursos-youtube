#forma no optima de sumar valores
def suma (lista):
    numeros_sumados= 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados

resultado = suma([2,4,5,2,4])
print(resultado)
 
#forma optima utilizando el argumento args (*)

def suma1(nombre, *numeros):
    return f"{nombre}, la suma de los numeros es: {sum(numeros)}"

resultado = suma1("Luisa", 1,3,4,5,6,8)
print(resultado)

#otra forma optica similar a la de arriba

def otra_suma(numeros):
    return sum([*numeros])
res = otra_suma([1,2,3,4])
print(res)
