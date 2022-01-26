#this code will do a small random parrafe
import random as rd,tkinter as tk
parrafo_uno="""Sofía había ido a hacer algunas compras 
cuando se encontró con Rocío, su prima y amiga.
Juntas decidieron ir a la tienda de ropas para ver las
“grandes ofertas” que allí se promocionaban."""
parrafo_dos="""Cerca de las 13 horas, y cuando ya el comercio
 se disponía a cerrar sus puertas, Sofía “recordó” que no 
 había comprado aquellas cosas que su madre le había 
 encargado esa mañana.
"""
def denuevo():
	xd=rd.choice(parrafo)
	texto["text"]=xd
	texto["bg"]=rd.choice(["red","blue","cyan","fuchsia","yellow"])
parrafo=[]
parrafo.append(parrafo_uno)
parrafo.append(parrafo_dos)
xd=rd.choice(parrafo)
print(xd)
raiz=tk.Tk()
texto=tk.Label(text=xd,bg="red")
texto.pack()
boton=tk.Button(text="cambiar texto",command=denuevo).pack()
raiz.config(background="red")
raiz.mainloop()
xd="sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"
