import tkinter as tk
import random

# Lista de mensajes del día
mensajes = {
    "mensaje1": "Hoy es un buen día para aprender algo nuevo.",
    "mensaje2": "La perseverancia es la clave del éxito.",
    "mensaje3": "La creatividad es la inteligencia divirtiéndose.",
    "mensaje4": "Cada día es una nueva oportunidad para ser mejor.",
    "mensaje5": "La actitud positiva es contagiosa. Sé un portador."
}

# Función para mostrar un mensaje aleatorio
def mostrar_mensaje():
    mensaje = random.choice(list(mensajes.values()))
    etiqueta.config(text=mensaje)

# Configuración de la ventana principal de tkinter
ventana = tk.Tk()
ventana.title("Mensaje del Día")

# Configuración de la etiqueta para mostrar el mensaje
etiqueta = tk.Label(ventana, text="")
etiqueta.pack(pady=20)

# Configuración del botón para generar un nuevo mensaje
boton = tk.Button(ventana, text="Generar Mensaje", command=mostrar_mensaje)
boton.pack(pady=20)

# Inicio del bucle principal de tkinter
ventana.mainloop()
