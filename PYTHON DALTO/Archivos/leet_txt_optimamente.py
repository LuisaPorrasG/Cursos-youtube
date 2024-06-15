#abrimos el archivo con with open 
with open("archivos\\texto_de_luisa.txt", encoding="UTF-8") as archivo:
    #leemos el archivo
    contenido = archivo.read()
    #mostramos el archivo
    print(contenido)
