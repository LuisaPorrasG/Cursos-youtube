import pandas as pd

#print(type(pd))
#df = data frame ...leyendo un archivo csv con funcion read.csv
#y con name = asigno valores al encabezado
df = pd.read_csv("archivos\\datos.csv",names=["name", "LastName", "age"])
df2 = pd.read_csv("archivos\\datos.csv")
#obteniendo los datos de la columna nombre
nombres = df["name"]
#print(df)


#funcionamiento de Slicing [incio:final]
cadena ="012345789"
print(cadena[2:3])

#ordenando el dataframe por edad de forma descendiente
df_ordenado_des = df.sort_values("age")
#print(df_ordenado_des)

#ordenando el dataframe por edad de forma ascendientemente
df_ordenado_asc = df.sort_values("age",ascending=False)
#print(df_ordenado_asc)

#concaatenando los 2 dataframe y los pongo en una lista []
df_concatenado = pd.concat([df, df2])
#print(df_concatenado)

#accediendo a la primer fila con head() (1)--> accedo al numero de fila que deseo
primer_fila = df.head(3)
#print(primer_fila)

#accediendo a las últimas 3 filas con tail ()
ultima_fila = df.tail(3)
#print(ultima_fila)

#accediendo a la cantidad de filas y columnas con shape
filas_y_columnas = df.shape
filas_totales = filas_y_columnas [0] #accedo a las filas
columnas_totales = filas_y_columnas [1] #accedo a las columnas

#*o tambien podemos desempaqueta la duplaque nos arroja filas y columnas*
filas_t, columnas_t = filas_y_columnas
#print(filas_y_columnas)
#print(filas_t)
#print(columnas_t)


#obteniendo data estadistica del dataframe
df_info= df.describe()
#print(df_info)

#accediendo a un elemento especifico con loc
elemento_especifico = df.loc[2, "age"]
#print(elemento_especifico)

#accediendo a un elemnto por index con  iloc
elemento_especifico = df.iloc[2,2]
#print(elemento_especifico)

#accediento a todas las filas de una columna
apellidos = df2.iloc[:,1]
#print(apellidos)

#accediendo  a la fila 3 con loc
fila3 = df2.loc[2,:]
print(fila3)