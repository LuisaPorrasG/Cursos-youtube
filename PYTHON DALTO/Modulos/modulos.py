#importo el modulo de saludar, es decir el archivo, puedo hacer una referencia como en sql
import modulos_saludar as  m_saludar
#si solo quiero importar una función especifica del modulo :
from modulos_saludar import saludar
#tambien podemos importar todo, pero es una mala practica
from modulos_saludar import *

#la función pasa a ser un metodo cuando la importamos, por eso para acceder a ella tiene que ser como un metodo
resultado = m_saludar.saludar ("Fernadna")
print(resultado)