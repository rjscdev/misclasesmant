import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def mensaje():
    messagebox.showinfo("Boton personalizado", "este boton fue hecho con TKinter y ttk")
# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Estilos en Tkinter")

# Crear un estilo
style = ttk.Style()

# Cambiar el tema (opcional)
style.theme_use('clam')

# Configurar un estilo para los botones
style.configure('TButton', 
                font=('Fira Code', 12, 'bold'), 
                foreground='white', 
                background='#7DDA58',
                padding=10)

# Crear un botón con el estilo personalizado
label = tk.Label(root, text="Hola este es un boton especial")
label.pack(pady= 5)
boton = ttk.Button(root, text="Botón Personalizado", style='TButton')
boton.pack(pady=20)

# Ejecutar el bucle principal
root.mainloop()
