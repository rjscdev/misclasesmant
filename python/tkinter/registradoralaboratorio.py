import tkinter as tk
from tkinter import ttk, messagebox
import json

class PatientRegisterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Register App")

        # Variables
        self.name = tk.StringVar()
        self.surname = tk.StringVar()
        self.address = tk.StringVar()
        self.phone = tk.StringVar()
        self.weight = tk.StringVar()
        self.height = tk.StringVar()
        self.blood_type = tk.StringVar()
        self.affiliation_number = tk.StringVar()
        self.doctor_name = tk.StringVar()
        self.specialty = tk.StringVar()
        self.department = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Datos del Paciente
        tk.Label(self.root, text="Datos del Paciente").grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.root, text="Nombre:").grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.name).grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self.root, text="Apellido:").grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.surname).grid(row=2, column=1, padx=5, pady=5)
        tk.Label(self.root, text="Dirección de Residencia:").grid(row=3, column=0, sticky=tk.E, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.address).grid(row=3, column=1, padx=5, pady=5)
        tk.Label(self.root, text="Número Telefónico:").grid(row=4, column=0, sticky=tk.E, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.phone).grid(row=4, column=1, padx=5, pady=5)

        # Datos Clínicos
        tk.Label(self.root, text="Datos Clínicos").grid(row=5, column=0, columnspan=2, pady=10)
        tk.Label(self.root, text="Peso (kg):").grid(row=6, column=0, sticky=tk.E, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.weight).grid(row=6, column=1, padx=5, pady=5)
        tk.Label(self.root, text="Altura (cm):").grid(row=7, column=0, sticky=tk.E, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.height).grid(row=7, column=1, padx=5, pady=5)
        tk.Label(self.root, text="Tipo Sanguíneo:").grid(row=8, column=0, sticky=tk.E, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.blood_type).grid(row=8, column=1, padx=5, pady=5)

        # Número de Afiliación
        tk.Label(self.root, text="Número de Afiliación:").grid(row=9, column=0, sticky=tk.E, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.affiliation_number).grid(row=9, column=1, padx=5, pady=5)

        # Médico
        tk.Label(self.root, text="Datos del Médico").grid(row=10, column=0, columnspan=2, pady=10)
        tk.Label(self.root, text="Nombre del Médico:").grid(row=11, column=0, sticky=tk.E, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.doctor_name).grid(row=11, column=1, padx=5, pady=5)
        tk.Label(self.root, text="Especialidad:").grid(row=12, column=0, sticky=tk.E, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.specialty).grid(row=12, column=1, padx=5, pady=5)
        tk.Label(self.root, text="Departamento Médico:").grid(row=13, column=0, sticky=tk.E, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.department).grid(row=13, column=1, padx=5, pady=5)

        # Botón de Registrar
        tk.Button(self.root, text="Registrar", command=self.register_data).grid(row=14, column=0, columnspan=2, pady=10)

    def register_data(self):
        if not self.affiliation_number.get():
            messagebox.showwarning("Advertencia", "Debe ingresar el número de afiliación.")
            return

        data = {
            "Datos del Paciente": {
                "Nombre": self.name.get(),
                "Apellido": self.surname.get(),
                "Dirección de Residencia": self.address.get(),
                "Número Telefónico": self.phone.get()
            },
            "Datos Clínicos": {
                "Peso": self.weight.get(),
                "Altura": self.height.get(),
                "Tipo Sanguíneo": self.blood_type.get()
            },
            "Número de Afiliación": self.affiliation_number.get(),
            "Datos del Médico": {
                "Nombre del Médico": self.doctor_name.get(),
                "Especialidad": self.specialty.get(),
                "Departamento Médico": self.department.get()
            }
        }

        self.save_to_json(data)
        

    def save_to_json(self, data):
        filename = f"{self.affiliation_number.get()}.json"
        try:
            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            messagebox.showinfo("Éxito", "Datos registrados correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron guardar los datos: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PatientRegisterApp(root)
    root.mainloop()
