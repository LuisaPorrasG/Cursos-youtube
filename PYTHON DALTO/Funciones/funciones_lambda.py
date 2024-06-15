#es como las funciones flecha en javascript
#las funciones lambda retorna automaticamente   

numeros = [1,2,3,4,5,6,7,8,9]
multiplicar_por_dos = lambda x : x*2 #lambda crea funciones anonimas
print(multiplicar_por_dos(5))

#creando una función común que diga si es par o no

def es_par (num):
    if num %2== 0:
        return True

#usando filtrer con una función común
numeros_pares= filter(es_par, numeros)
print(list(numeros_pares))


#creando lo mmismo me antes pero con lambda
num_par = filter(lambda numer: numer%2 ==0, numeros)
print(list(numeros_pares))