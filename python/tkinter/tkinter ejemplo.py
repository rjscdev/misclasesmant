#importacion de librerias y modulos
import tkinter as tk
from tkinter import messagebox

#codigo en bruto 
def mensaje():
    messagebox.showinfo("nombre de la caja de texto", "mensaje")

root = tk.Tk()
root.title("interfaz simple")
root.geometry("300x200") #ancho x alto    

#crear boton
boton = tk.Button(root, text="haz click aqui", command=mensaje)
boton.pack(pady=20)

root.mainloop()
