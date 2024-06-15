#código para apertura de archivo
archivo_sin_leer = open("archivos\\texto_de_luisa.txt", encoding="UTF-8")#UTE-8 para que no salgan errores en la escritura del código
#códio para lectura de archivo con el método . read
#archivo = archivo_sin_leer.read()
#print(archivo)

#leear lineas por lineas del archivo
lineas= archivo_sin_leer.readlines() #me devuelve en arreglo las lineas del archivo
#leer una sola linea
linea1 = archivo_sin_leer.readline()
print(linea1)

#cerrar el archivo

archivo_sin_leer.close()