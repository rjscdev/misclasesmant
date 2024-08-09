#diccionarios :
#los diccionarios son formas de almacenamiento de datos dentro de python
#estos almacenan datos usando una paridad de clave- valor
#siendo la clave el identificador unico de cada dato
#esto se podria ver como un conjunto de varias variables en un solo lugar.

#ejemplo de diccionario:
Mensajes = {
    'mensaje1': "La vida es maravillosa",
    'mesanje2': "la fuerza yace en aquellos que la buscan",
    'mensaje3': "cuando el alma esta enferma, todo el cuerpo lo está. por ello mantente alegre todo el tiempo",
    'mensaje4': "Las estrellas brillan mas cuando estas están por apagarse"
}

#en este caso tenemos un diccionario que almacena varios mensajes
#como se puede ver tenemos los pares de clave-valor
#siendo la clave 'mensaje' y el dato el mensaje como tal dentro de una cadena
#de texto.

#para definir un diccionario los nombres de clave deben ser unicos y no repetibles
#esto solo aplica dentro de un mismo diccionario, los nombres se pueden repetir
#entre varios diccionarios.

#aqui otro ejemplo:

#definir diccionarios es como definir variables
diccionario = {
    #clave  #valor
    'dato1': 25, #para separar datos se necesita colocar coma , 
    'dato2': 25.6,
    'dato3': True,
    'dato4': "hola mundo" #el ultimo dato nunca lleva coma , 
}

#para llamar un dato de un diccionario se utiliza el metodo .get()
#el cual nos permite recavar datos de distintos lugares
#aqui un ejemplo

print(diccionario.get('dato2')) 
#en este caso la funcion diccionario.get('dato2') tomara el dato correspondiente
#a dicha clave y lo imprimira en consola con la funcion print
#el meto .get tambien sirve para reasignar valores a otras variables

variable = diccionario.get('dato3')
#esto haria que la variable tenga el estado de True correspondiente a dicha clave