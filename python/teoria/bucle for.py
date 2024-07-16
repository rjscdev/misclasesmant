#for es un bucle finito que basa sus repeticiones en un rango y se utiliza para iterar
#sobre listados. 

frutas = ["manzana", "melocoton", "banana", "fresa"] #arreglo que contiene frutas
#un arreglo es un conjunto de datos dentro de una misma variable
#se usa para almacenar mismos objetos en un solo lugar y tener todo mas ordenado

print(frutas) #imprime el arreglo de manera erronea, mostrandose asi en consola
#["manzana", "melocoton", "banana", "fresa"]

#for variablelocal in listado o variable
    #seccion de nuestro codigo a repetirse
    
for  fruta in frutas: #la duracion del bucle esta definida por la cantidad de
                      #elementos dentro de la lista frutas
    print(fruta)#en este caso el output en consola sera distinto de un print normal
    #dado que mostrara solo los datos del arreglo mas no como esta formado.add()
    
    
#para definir directamente la cantidad de veces que se repite
#se utiliza la funcion range 

for i in range(6):
    print("esta es la iteracion", i + 1)
#en este caso el bucle fue definido para repetirse un total de 6 veces
#mostrando la cadena de texto 6 veces y la variable local asignandole un valor de 1 y 
#sumandole esto por cada iteracion. 


