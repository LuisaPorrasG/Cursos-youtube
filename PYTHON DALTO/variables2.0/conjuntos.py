#Creando conjuntos con SET, normalmente los conjuntos se declaran con {}

conjunto = set(["Luisa", "Porras", 23]) 
print(conjunto)

#Metiendo un conjunto de otro conjunto

conjunto1 = frozenset(["dato1", "dato2"]) #tengo que poner frozenser para congelar el conjunto
conjunto2 = {conjunto1, "dato3"}
print(conjunto2)

#teoria de conjuntos
conjunto1= {1,3,5,7,}
conjunto2 = {1,3,7}

#conjunto2 es subconjunto de conjun1? metodo .issubset
resultado = conjunto2.issubset (conjunto1)  #true, metoodo 1
print(resultado )
resultado = conjunto2 <= conjunto1 #true, metodo 2
print(resultado )

#verificar si es un super conjunto
resultado = conjunto1.issuperset (conjunto2)  #true, metoodo 1
print(resultado)
resultado = conjunto1 >= conjunto2 #true, metodo 2
print(resultado)

#verificar si hay un numero en común, paraa ello da falso el resultado ya que hay numeros en comun
resultado = conjunto2.isdisjoint(conjunto2)

