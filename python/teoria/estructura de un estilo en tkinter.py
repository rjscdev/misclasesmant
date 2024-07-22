import tkinter as tk
#*ttk sera el modulo que nos permita estilizar los objetos
from tkinter import ttk

#*se define la interfaz:
root = tk.Tk()
root.title("Ejemplo de estilos en Tkinter")
#!###################################################################################
#?variable = modulo.metodo.
style = ttk.Style() #*configuracion y llamado del estilo.

#?style es una variable y configure el metodo
#*variable.metodo
#?en este caso el estilo se aplica a un elemento label
#*ttk.Label()
style.configure('Tlabel', #nombre del estilo
                font = ("Helvetica", 15),#configuracion de la fuente
                foregroud = "blue",#color del texto
                background = "yellow", #color del fondo
                padding = 10) #espacio en pantalla      
        #?para configurar un estilo en un objeto en este caso seria
        #*variable = ttk.objetoausar(interfaz, text="texto", style = "nombredeestilo")

#!###################################################################################

