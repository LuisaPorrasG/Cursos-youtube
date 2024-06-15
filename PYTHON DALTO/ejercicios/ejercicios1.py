

curso_dalto= 1.5
curso_min = 2.5
curso_max = 7
curso_pro = 4

curso_promedio = 5
datolto_curso = 3.5
#Mostrando las diferencias de duración (ejercicio a)
print("--------------------------------------------")
diferencia_min = 100 - (curso_dalto / curso_min *100)
print(f"el curso de dalto dura: {diferencia_min}% menos que el curso minimo")
diferencia_max = 100 - (curso_dalto *1000 // curso_max / 10) # podria divirlo entero con // y no me devuelva un fotante, muevo literalmente la coma del numero flotante para que me salga almenos dos decimales
print(f"el curso de dalto dura: {diferencia_max}% menos que el curso máximo")
diferencia_pro = 100 - (curso_dalto / curso_pro *100)
print(f"el curso de dalto dura: {diferencia_pro}% menos que el curso promedio")
print("--------------------------------------------")
#Mostrando la cantidad de espacios vacios que se remueven (ejercicio b)
tiempo_vacio_pro = 100- curso_pro *1000 // curso_promedio /10
tiempo_vacio_dalto = 100- curso_dalto *1000 // datolto_curso /10

print(f"Un curso promedio elimina un :{tiempo_vacio_pro}% de tiempo vacio")
print(f"Este curso elimina el :{tiempo_vacio_dalto}% de tiempo vacio")
print("--------------------------------------------")
#Mostrando diferencias si los cursos duraran 10 horas
print(f"Ver 10 horas de este curso equivalen a ver {curso_pro *100 // curso_dalto / 10} horas de otros cursos")
print(f"Ver 10 horas de otros cursos equivalen a ver {curso_dalto *100 // curso_pro / 10} horas de otros cursos")
print("--------------------------------------------")