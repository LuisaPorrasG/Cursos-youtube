def frase (nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase_resultante = frase("Luisa", "Porras", "Profesional")
print(frase_resultante)


frase_resultante2 = frase(adjetivo="Pro", apellido= "Porras", nombre="Luisa")
print(frase_resultante2) #también lo puedo ejecutar de esta manera