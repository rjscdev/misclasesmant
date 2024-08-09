import random

mensajes = {
    'mensaje1': "La vida es maravillosa",
    'mesanje2': "la fuerza yace en aquellos que la buscan",
    'mensaje3': "cuando el alma esta enferma, todo el cuerpo lo está. por ello mantente alegre todo el tiempo",
    'mensaje4': "Las estrellas brillan mas cuando estas están por apagarse"
}
mensaje =(random.choice(list(mensajes.values())))
print (mensaje)