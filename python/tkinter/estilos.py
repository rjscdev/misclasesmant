import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de estilos en Tkinter")

# Crear un estilo
style = ttk.Style()

# Estilizar un Label
style.configure('TLabel', 
                font=('Helvetica', 12),
                foreground='blue',
                background='yellow',
                padding=10)

label = ttk.Label(root, text="Etiqueta estilizada", style='TLabel')
label.pack(pady=10)

# Estilizar un Entry
style.configure('TEntry', 
                font=('Helvetica', 12),
                foreground='black',
                background='white',
                padding=5)

entry = ttk.Entry(root, style='TEntry')
entry.pack(pady=10)

# Estilizar un Button
style.configure('TButton', 
                font=('Helvetica', 12, 'bold'),
                foreground='black',
                background='green',
                padding=10)

button = ttk.Button(root, text="Botón estilizado", style='TButton')
button.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
