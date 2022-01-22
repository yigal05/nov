#this code will do a small random parrafe
import random as rd
parrafo_uno="""Sofía había ido a hacer algunas compras 
cuando se encontró con Rocío, su prima y amiga.
Juntas decidieron ir a la tienda de ropas para ver las
“grandes ofertas” que allí se promocionaban."""
parrafo_dos="""Cerca de las 13 horas, y cuando ya el comercio
 se disponía a cerrar sus puertas, Sofía “recordó” que no 
 había comprado aquellas cosas que su madre le había 
 encargado esa mañana.
"""
parrafo=[]
parrafo.append(parrafo_uno)
parrafo.append(parrafo_dos)
print(rd.choice(parrafo))
