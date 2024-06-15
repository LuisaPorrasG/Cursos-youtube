frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]

#saltando la fruta manzana del bucle, pero aún así continua
for fruta in frutas:
    if fruta == "granada":
        continue
    print(f"Me voy a comer : {fruta}")
    

#saltando la fruta pera pero el bucle no cotinua, se detiene(si puesiera un else el else tampoco lo ejecuta por que el break termina todo)
for fruta in frutas:
    if fruta == "pera":
         continue 
    print(f"Me voy a comer : {fruta}")