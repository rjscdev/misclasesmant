itworks = False#*se declara una variable booleana la cual hace que todo el programa
              #*Funcione
              
if itworks == True:#*se hace la condicion de todo el programa
    #?si la variable itworks es igual a True, entonces: 
    iterator = 0#* se declara una variable para nuestro bucle con un valor de 0
    while iterator <6:#*por motivos practicos se usa while ya que es mas facil
        #?mientras qué iterador sea menor a 6:
        print("iteracion", iterator)#*imprime en consola el texto y el valor de 
                                    #*iterador
        iterator +=1#*suma un valor de 1 a la variable iterador por cada vez
        #!si esto no se especifica el bucle no será roto
else: #?Declara que pasara en el caso contrario
    print("error")#*imprime un mensaje de error en caso de que itworks sea falso