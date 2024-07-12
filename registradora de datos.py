#importacion de librerias y recursos necesarios
import tkinter as tk
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

entry_nombre = tk.Entry()
entry_telefono = tk.Entry()
entry_direccion = tk.Entry() 

root.mainloop()