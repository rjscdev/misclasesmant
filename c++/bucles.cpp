#include <iostream>
using namespace std; 

int main(){
    //El bucle for se utiliza cuando 
    //se conoce de antemano el número de iteraciones que se desea realizar.
    //for(inicializacion; condicion; actualizacion)
    
    for(int i = 0; i < 5; ++i){
        cout << "iteracion" << i << endl;
    }

    // ejecuta el bloque de codigo mientras la condicion sea verdadera
    //en este bucle no se sabe la cantidad de iteraciones
    // while(condicion){}
    int f = 1;
    while (f <= 10){
        cout << "iteracion" << f << endl;
        ++f;

    } 
}