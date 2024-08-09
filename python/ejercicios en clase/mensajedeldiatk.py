import tkinter as tk
import random

diccionario = {
    'clave1' : "el aady",
    'clave2' : "hola",
    'clave3' : "la carne de chancho",
    'clave4' :  "la vida es una lenteja o la tomas o la dejas"
}

def mostrarmensaje():
    mensaje = random.choice(list(diccionario.values()))
    label.config(text= mensaje)
    


root = tk.Tk()
root.title("Mensaje diario")
root.geometry("300x300")

label = tk.Label(root, text="")
label.pack(pady= 5)

boton = tk.Button(root, text="generar mensaje", command= mostrarmensaje)
boton.pack(pady= 5)

root.mainloop()    