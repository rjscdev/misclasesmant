<<<<<<< HEAD
#LAS CONDICIONALES SON ESTRUCTURAS DE CONTROL LAS CUALES PERMITEN LA TOMA DE DECISIONES DENTRO DE NUESTRO CODIGO
#LO CUAL NOS PERMITE MANEJAR SECCIONES DE CODIGO DE DIFERENTE FORMA DEPENDIENDO DE CIERTOS PARAMETROS ESPECIFICOS.



var persona = "juanito"
var hadesayunado = True
=======
func ready_():
    var persona = "juanito"
    var hadesayunado = True
>>>>>>> a02380845c2c95ddaa16444f92e4858aad9096d3

    if hadesayunado:
        print(persona, "si ha desayunado y tiene energia.")
    else:
        print(persona, "no ha desayunado, no tiene energia.")
    
    pass

var numero = 45

if numero >= 45:
    print("el numero es mayor a 45")
else: 
    print("el numero no es mayor")