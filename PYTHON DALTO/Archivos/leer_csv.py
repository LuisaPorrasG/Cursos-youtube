import csv

with open("archivos\\datos.csv") as archivo:
    #print(f"data leida correctamente {archivo.read()}") //opcion sin la importacion de libreria csv
    reader= csv.reader(archivo)
    #itero por filas 
    for row in reader :
        print(row)
