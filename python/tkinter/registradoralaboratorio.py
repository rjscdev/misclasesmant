import tkinter as tk
from tkinter import ttk, messagebox
import json ##importacion de las dependecias a utilizar 

class PatientRegisterApp: #inicializacion de clase
    def __init__(self, root): #definicion de parametros #self para declar instancia inicial y root como variable inicial que define la interfaz
        self.root = root #re declaracion de la variable #recordar que sel.root es la instancia inicial por lo que esta no se ve afectada y para asignar valor
        #se vuelve a asignarle la misma variable
        #para evitar problemas a la hora de identificar diferencias en el codigo les recomiendo cambiar el nombre de root por interfaz o el nombre que ustedes desean
        #pero tenerlo muy en cuenta a la hora de asignar posteriormente el resto de elemntos
        self.root.title("Patient Register App")#titutlo de la aplicacion

        #declaracion de las variables con las que se va a trabajar en todo el programa, todas estas variables estan basadas en el numero de campos que contiene el programa
        self.name = tk.StringVar() #el metodo tk.StringVar() lo que hace es recolectar los datos de un elemento de tkinter y trasnmutarlo en una cadena de texto almacenable
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

        self.create_widgets()#llamado a la funcion que se encarga de definir todos los campos y elemntos necesarios para crear la interfaz

    #creacion de la funcion que se encarga de definir todos los elementos de la interfaz
    def create_widgets(self):#en este caso el unico parametro a utilizar es self ya que solo se hará instanciamineto de los elementos
        
        #estructura:
        #tk.Elmento(self, nombredelavariableinterfaz, propiedades).grid(estilos)
        #aqui algo que no explique y es que se pueden añadir estilos directamente dentro de una misma linea de codigo sin tener que rellamar la variable y ponerle metodo pack
        #esto se ha ce con el metodo .grid el cual permite asignar distintos valores de estilos
        #en este caso como pueden ver tenemos las opciones como row, que hacen referencia al numero de fila, column el numero de columna, columnspan es la distancia entre columnas
        #pady es el espacio en vertical y padx en horizontal
        tk.Label(self.root, text="Datos del Paciente").grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.root, text="Nombre:").grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        #aqui como pueden ver ya hay una diferencia entre los elementos de tkinter ya que estos es una entrada, de la cual nosotros extraeremos nuestro texto
        #si recuerdan al principio nosotros asignamos instancias de objeto incial para los elementos que se trabajaran a qui por lo que ahora haremos uso de dichos elementos para 
        #poder trabajar de mejor manera. esto lo que hara es que podamos escribir los textos en las entradas y estos generen su propio objeto del cual nosotros posteriormente extraeremos
        #datos para poder almacenarlos. 
        #por tanto hacemos uso de la propiedad textvariable, que lo que hace es definir el campo como una variable para su posterior asignacion, por lo que a esta propiedad le asignamos
        #la instancia de variable correspondiente dependiendo del campo en el que nos encontremos.
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
        
    #definicion de la funcion encargada de registrar los datos
    def register_data(self):
        #a partir de esta seccion es donde depende todo el programa para su buen funcionamiento. si leyeron las instrucciones, sabe que el programa esta ligado a una condicion
        #la cual dicta que el programa solo debe funcionar si el paciente tiene numero de afiliacion por lo que se hace la siguiente comparacion/condicional haciendo uso de puertas logicas
        
        #en lenguaje humano esto quedaria tal que asi:
        #?si no existe self.affiliation_number.get() entonces:
        #ahora, que es lo que pasa aqui? lo que hace es verificar si la variable self.affiliation_number en primer lugar exista, posterior a eso utiliza metodo .get para obtener datos
        #por lo que de obtenerlos la condicional no funciona, esto ya que al usar la puerta logica not, estamos comparando su no existencia, la condicion solo funciona
        #si el programa es incapasz de recavar datos de la variable self.affiliation_number, ya que de no hacerlo no se debe ejecutar, por lo que se muestra el mensaje de error
        #en el caso de la condicion falle, y el programa si tenga la variable y recave datos, se ejecutara todo el demas codigo luego del return, el cual es encargado de romper la 
        #condicional
        if not self.affiliation_number.get():
            messagebox.showwarning("Advertencia", "Debe ingresar el número de afiliación.")
            return
        #posterior a eso definimos la estructura de datos que se va a utilizar dentro del programa. en este caso la estructura corresponde a la de un archivo .json
        #este archivo es especializado en el almacenamiento de datos en javascript, el cual usaremos para su posteiror uso en bases de datos de tipo json como lo son mongoDB
        #por lo que la estructura es la siguiente
        data = { #primero se define la variabel que almacenara toda la estructura de dicho archivo
            "Datos del Paciente": {#este es el cabecero o incio de contenedor
                "Nombre": self.name.get(),#posterior a eso se define el nombre o clave del dato y posterior a eso el dato. basicamente este archivo es como un diccionario pero mas complejo
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

        self.save_to_json(data) #posterior a eso se hace un instanciamiento de funcion con self y dentro de los parametros de la funcion se pone la variable que contiene la estructura
        

    def save_to_json(self, data): #definicion de la funcion encargada de almacenar los datos en archivos .json
        #para esto usamos la siguiente estrucutra de datos para el correcto alamacenamiento del archivo, esto haciendo uso de la libreria previamente importada de json
        #la estrucutra es:
        # variable = f"{nombredelarchivo}.json"
        #en este caso el nombre del archivo es tomado del numero de afiliacion. pero esto puede ser cambiado por lo que nosotros queramos
        filename = f"{self.affiliation_number.get()}.json"
        #cuando esto esta definido lo que hara es intentar alamcenar los datos para ello hace uso de la funcion try
        try:
            #dentro de esto le dice que con funcion open, tome el nombre del archivo y lo almacene como un archivo json, pero en este caso es defincion de funcion
            with open(filename, 'w') as json_file:
                #aqui pasa a crearse la funcion haciendo llamado de las siguientes subfuciones
                #usa json para crear el archivo, luego metodo dump para tirar los datos y almacenarlos, posterior a eso se definde de donde viene la informacion, posterior a eso la estrucutra
                #y le asigna una identacion
                json.dump(data, json_file, indent=4)
            #en el caso del registro exitoso se muestra el siguiente mensaje
            messagebox.showinfo("Éxito", "Datos registrados correctamente.")
            #en caso fallido se hace una excepcion y se muestra el mensaje de error
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron guardar los datos: {e}")

#define la condicion que hace que el programa funcione, esto solo una verificacion para ver si el program corre en su archivo madre y no es importado como script en otro archivo
if __name__ == "__main__":
    #aqui se define la interfaz inicializandola con root = tk.Tk()
    root = tk.Tk()
    app = PatientRegisterApp(root) #definie la aplicacion llamando a la clase incialmente creada y la propiedad root
    root.mainloop() #el bucle de todo el programa y la interfaz
    
