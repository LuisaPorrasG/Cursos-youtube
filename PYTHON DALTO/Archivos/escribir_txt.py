#permiso de escritura con , "w"
with open ('archivos\\texto_de_luisa.txt','w', encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("JAJAJA aqui estoy reescribiendo el texto")
    archivo.writelines(["-Jelou genteeee \n", " como andamos \n"])
    #agregando otras dos lineas con writelines
    archivo.writelines(["-Bien y vos que tal \n", " como andas?"])
    