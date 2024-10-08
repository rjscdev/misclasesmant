#importacion de librerias y recursos necesarios
#ejercicio, completar la siguiente interfaz, mostrando las etiquetas necesesarias.
#este programa es una registradora de datos, en base a lo que se muestra, terminar la funcionalidad
#de la interfaz. todo el backend del proyecto ya ha sido trabajado, su deber es terminar la interfaz
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def guardar_datos():
    nombre = entry_nombre.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()
    
    if nombre and direccion and telefono:
        with open('registros.txt', 'a') as file:
            file.write("Nombre: {nombre}\n")
            file.write("Direccion: {direccion}\n")
            file.write("Telefono: {telefono}\n")
            file.write("-" * 40 + "\n")
            
            
        entry_nombre.delete(0, tk.END)
        entry_direccion.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        
        messagebox.showinfo("informacion", "datos registrados")
        messagebox.showwarning("advertencia", "todos los campos son obligatorios")

#definicion de interfaz, espacio de trabajo       
root = tk.Tk()
root.title("Registradora de datos")
root.geometry("400x300")
#!###################################################################################
#?variable = modulo.metodo.
style = ttk.Style() #*configuracion y llamado del estilo.

#?style es una variable y configure el metodo
#*variable.metodo
style.configure('Tlabel', #nombre del estilo
                font = ("Helvetica", 15),#configuracion de la fuente
                foregroud = "blue",#color del texto
                background = "yellow", #color del fondo
                padding = 10 #espacio en pantalla
                )      
        #?para configurar un estilo en un objeto en este caso seria
        #*variable = ttk.objetoausar(interfaz, text="texto", style = "nombredeestilo")

#!###################################################################################
#terminar interfaz, añadir etiquetas y boton que ejecute el programa.
nombrelab = ttk.Label(root, text="Nombre", style ='Tlabel')
nombrelab.pack(pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.pack(pady= 5)
tellab = tk.Label(root, text="telefono")
tellab.pack(pady= 5)
entry_telefono = tk.Entry(root)
entry_telefono.pack(pady= 5)
dirlab = tk.Label(root, text="Direccion")
dirlab.pack(pady= 5)
entry_direccion = tk.Entry(root)
entry_direccion.pack(pady= 5)
button = tk.Button(root, text="Registrar", command=guardar_datos) 
button.pack(pady= 5)

root.mainloop()