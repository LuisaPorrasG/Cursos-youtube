animal = " chancito feliz "
print(animal.upper()) #metodo para pasar el string a mayuscula
print(animal.lower()) #metodo para pasar el String a minuscula
print(animal.strip().capitalize()) #metodo que toma la primera letra y la pasa a mayuscula y podoemos encadenar los metodos
print(animal.title()) #Metodo que toma la primera letra de cada palabra y la pasa a mayuscula
print(animal.strip()) #remueve los espacios a la izquierda y derecha del string
print(animal.lstrip()) #quita los espacios de la izquiera
print(animal.rstrip())#quita los espacios de la derecha
print(animal.find("iz")) #devuelve el dindice de dond se encuenra los caracteres
print(animal.replace("ch", "j")) #remplaza caracteres necesariamente recibe 2 argumentos
print(" ch" not in animal) #busca los caracteres en la variable con in o no se encuentra con not in

