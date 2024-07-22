import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def mostrarmensaje():
     messagebox.showinfo("informacion", "esto es un mensaje de prueba")

#inicializacion de la interfaz
root = tk.Tk() #asignacion de modulo y clase
root.title("widgets mas usados de tkinter") #definicion del titulo de la venta
root.geometry("600x600")#ancho x largo

#etiqueta de texto
label = tk.Label(root, text="esto es una etiqueta de texto")
#variable = modulo.clase(interfaz,texto)
label.pack(pady= 5)
#variable.pack(parametro = valor) #pack hace referencia al empaquetado del widget

#boton
button = tk.Button(root, text="presionar boton", command=mostrarmensaje)
#variable = modulo.funcion(interfaz, texto, comando a ejecutar)
button.pack(pady= 5)
#variable.pack(parametro = valor) #pack hace referencia al empaquetado del widget

#campo de entrada 
entry = tk.Entry(root)
#variable = modulo.funcion(interfaz)
entry.pack(pady = 5)
#variable.pack(parametro = valor) #pack hace referencia al empaquetado del widget


#textbox
textbox = tk.Text(root, height= 4, width= 40)
#variable = modulo.funcion(interfaz, altura, ancho)
textbox.pack(pady = 5)
#variable.pack(parametro = valor) #pack hace referencia al empaquetado del widget


#listboxº
listbox = tk.Listbox(root)
#variable = modulo.funcion(interfaz)
listbox.insert(1, "elemento 1")
#variable.funcion(numero identificador, nombre del elemento)
listbox.insert(2, "elemento 2")
listbox.insert(3, "elemento 3")
listbox.pack(pady= 5)
#variable.pack(parametro = valor) #pack hace referencia al empaquetado del widget


#barra de progreso
progressbar = ttk.Progressbar(root, orient= "horizontal", length= 200, mode= "determinate")
#variable = modulo.funcion(interfaz, orientacion, largo, modo)
progressbar.pack(pady = 5)
#variable.pack(parametro = valor) #pack hace referencia al empaquetado del widget
progressbar['value'] = 50
#variable[valor] = numero del valor

#notebook
notebook = ttk.Notebook(root)
#variable = modulo.funcion (interfaz)
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text="pestaña 1")
#variable.funcion(variable, texto)
notebook.add(frame2, text= "pestaña 2")
notebook.pack(pady= 5)

#spinbox
spinbox = tk.Spinbox(root, from_= 0, to = 10)
#variable = modulo.funcion(interfaz, desde, hasta)
spinbox.pack(pady=5)
#variable.pack(parametro = valor) #pack hace referencia al empaquetado del widget

root.mainloop() #cierre del programa e inicio de ejecuion, bucle del programa