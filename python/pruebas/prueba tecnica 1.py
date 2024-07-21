#########
#importar dependencias
#########
import tkinter as tk
from tkinter import messagebox, ttk
#########
#Crear una funcion que muestre un mensaje si el dato de la entrada es igual a 5. si el dato no es 5 debe arrojar un mensaje de error
#########
def stkr():
    prospectlab = text_entry.get()
    if prospectlab >= "5":
        messagebox.showinfo("Resultado", "Prueba tecnica superada")
    else:
        messagebox.showerror("Error", "valor no asignado correctamente")
        
#########
#Crear interfaz en la cual se va a mostrar todo con una resolucion de 300x400
#########
root = tk.Tk()
root.title("Prueba tecnica 1")
root.geometry("300x400")
#########
#añadir elementos necesarios
#########
label_entry = tk.Label(root, text="Ingresa el numero corresponiente")
label_entry.pack(pady= 5) 
text_entry = tk.Entry(root)
text_entry.pack(pady= 5)
funcbutt = tk.Button(root, text= "ejecutar", command = stkr)
funcbutt.pack(pady= 5)

root.mainloop()