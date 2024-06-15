#permiso de agregacon con , "a"
with open ('archivos\\texto_de_luisa.txt','a', encoding="UTF-8") as archivo:
    #agreganfdo el archivo 
    archivo.write("\n")
    for i in range(5):
        archivo.write(f'Linea {i+1} agregada \n')
