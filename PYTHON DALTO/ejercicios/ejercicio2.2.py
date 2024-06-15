#creando una función que nos devuelva los numeros primos hasta el numero que le pasemos

def es_primo (num):
    for i in range (2,num-1): #desde 2 hasta el numero ingresado -1
        if num%i == 0: return False
    return True

resultado= es_primo(10)
print(resultado)

def primos_hasta (num):
    primos = []
    for i in range (2, num+1):#le doy +1 para incluir el numero 13
        resultado= es_primo(i)
        if resultado==True:primos.append(i)
    return primos

res = primos_hasta(13)
print(res)
            