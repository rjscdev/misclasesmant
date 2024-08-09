import tkinter as interfaz
from tkinter import messagebox, ttk

def mostrarmensaje():
    variable = entry.gey()
    


root = interfaz.Tk()
root.title("prueba")
root.geometry("400x300")

boton = interfaz.Button(root, text= "holamundo", command=mostrarmensaje)
boton.pack(pady= 5)

root.mainloop()
