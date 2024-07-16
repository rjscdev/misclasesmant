#contrario del for, while es un bucle infinito, el cual se ejecuta si y solo si
#se cumple la condicion que lleva dentro. while solo deja de ejecutarse
#si dicha condicion se rompe

contador = 0 #*variable externa, while usa variables externas contrario 
#*a for que usa una interna
#en este caso la estructura es la siguiente:

#while variable condicion:
#   nuestro codigo
while contador <5: #en este caso se define que la condicion sea que el bucle se 
    #!ejecutara si y solo si la variable contador es menor que 5. 
    # por tanto el bucle se ejecuta dado que contador tiene un valor de 0
    print(contador)#imprime infinitamente la variable hasta que se rompa el bucle.
    
#!dado que while se ejecuta infinitamente, siempre se debe especificar que rompe la condicion. 
# en este caso:
#?lo que se hace es que se le suma un valor de 1 a la variable por cada iteracion. por tanto:
#se sabe que en algun punto la variable contador alcanzara un valor de 5, 
#con ello rompiendo asi la condicion que ejecuta el bucle si contador es menor que 5.
    contador +=1 