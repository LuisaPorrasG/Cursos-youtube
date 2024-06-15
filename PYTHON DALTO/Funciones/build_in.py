# encontrando el numero mayor y menor de una lista

numeros = [4,7,1,42,15]
numero_mas_alto = max(numeros)
numero_mas_bajo = min(numeros)
print(numero_mas_alto)
print(numero_mas_bajo)

#redondeando a 6 decimales con round anterior
numero = round(12.345 * 100)
print(numero / 100)

#redondeando a 6 decimales con round mas fácil
numero = round(12.34567, 6)
print(numero)

#retorna false -> cuando le pasamos un dato vacio, 0 o falso, none
resul = bool(0)
print(resul)

 #retorna true si todos los valores son verdaderos
 
resultado = all([124,"zxc", ["gola", 2]])   
print(resultado)

 
resultado = all([0,"zxc", ["gola", 2]])  # me va votar false por quepaso un valor falso o 0 o none 
print(resultado)

#suma de los valores de un iterable
suma_total = sum(numeros)
print(suma_total)