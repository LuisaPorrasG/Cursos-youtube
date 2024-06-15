#creando una listsa con list
lista = list(["Luisa", "Porras", 24])
#forma 2
lista2 = ["otra", "forma"]
lista3 = ["Luisa", "Porras", "Diva"]
print(lista)

#LEN-> cuenta la cantidad de elementos de una lista
resultado = len(lista)
print(resultado)

#APPEND -> agrega un elemento a la lista
lista.append("Cali")
print(lista)

#INSERT -> agrega un elemento a la lista en un indice especifico
lista.insert(2, 1.60)
print(lista)

#EXTENDS -> agrega varios elementos a la lista
lista.extend (["Diva", "Hermosa"])
print(lista)

#POP ->eliimina un elemento de la list
lista.pop (2)
print(lista)
lista.pop(-1) #elimina el ultimo de la fila, -2 el penultimo y asi sucesivaemente
print(lista)

#REMOVE -> elimina un elemento opor su valor
lista2.remove("otra")
print(lista2)

#CLEAR - > elimina todos los elementos de una lista
lista2.clear()
print(lista2)

#SORT -> Ordena una lista de manera ascendiente a descendiente, OJO solo puede tener un tipo de dato
lista3.sort()
print(lista3)

#REVERSE ->Ordena una lista de descendiente a ascendinte, OJO solo puede tener un tipo de dato
lista3.reverse()
print(lista3)
# o tambien
lista3.sort(reverse=True)
print(lista3)
