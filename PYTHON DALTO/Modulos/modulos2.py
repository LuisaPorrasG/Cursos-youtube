#si el modulo se encutra en una carpeta en la misma ruta
#import funciones_buenas.saludar as m_saludar

import sys

sys.path.append("C:\\Users\\Luisa Porras\\Documents\\PYTHON DALTO\\funciones_buenas")

import saludar as modulo_saludar

print(modulo_saludar.saludar("Luisa"))