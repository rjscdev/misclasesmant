import tkinter as tk
from tkinter import ttk

diccionario = {
    'dato1': "Hola dato1",
    'dato2': 256,
    'dato3': 2.58
    
}

root = tk.Tk()
root.title("Interfaz")
root.geometry("400x300")

label1 = tk.Label(root, text=diccionario.get('dato1'))
label1.pack(pady= 5)
label2 = tk.Label(root, text=diccionario.get('dato2'))
label2.pack(pady= 5)
label3 = tk.Label(root, text=diccionario.get('dato3'))
label3.pack(pady= 5)

root.mainloop()