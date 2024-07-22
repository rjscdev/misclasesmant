#include <iostream>
using namespace std;


int main(){
	bool itworks = true; //*se declara la variable que almacena el dato verdadero
	if (itworks){   //*plantea la condicion de la que depende todo el programa
    //? si itworks es verdadero entonces:
    int iterador = 0;//*se declara una variable de la cual hara uso el bucle
    while (iterador <6)//*se especifica que el bucle solo funciona si iterador es
                       //*menor que 6
    {
        cout << "Iteracion" << iterador << endl;//?si la condicion se cumple
        //?en consola se mostrara el resultado: "Iteracion [valor de variable]"
        ++iterador;//!suma a iterador un valor de 1 por cada iteracion
        //!eventualmente la variable llegara a 6 por lo que el bucle será roto
    }
    
	}
	else{//*que pasa si la condicion inicial no se cumple
		cout << "error" << endl; //*muestra el mensaje de error
	}
	return 0;
}
