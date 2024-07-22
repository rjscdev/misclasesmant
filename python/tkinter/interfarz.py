# importacion de libreria, framework, o biblioteca, etc
import tkinter as tk
from tkinter import messagebox # importacion de modulo 


# funcion principal
# define que se realizara a posterior al hacer click en el boton
def mensaje():
    messagebox.showinfo("Mensaje", "Hola mundo")
    
#creacion de ventana: 
#root es la interfaz raiz
root = tk.Tk() #importa funcion tk de tkinter
root.title("interfaz simple") #la funcion title añade el titulo de la ventana
root.geometry("300x200") #la funcion geometry sirve para declarar el largo y ancho de la ventana

#creacion de boton
#definimos la clase boton
boton = tk.Button(root,text = "haz clic aqui", command=mensaje) #importamos la funcion boton para crear el
#boton, su estructura es tk.Button(interfaz, text = "texto del boton", command= la funcion que definimos)
boton.pack(pady=20) #define el margen del boton haciendo uso de funcion pack y usando la subfuncion
#pad y para añadir un margen de 20


root.mainloop() #loop o bucle principal que ejecuta el programa, es importante poner todo antes de esto.
