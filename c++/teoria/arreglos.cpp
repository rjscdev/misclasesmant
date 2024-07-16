#include <iostream>
using namespace std;

int main() {
    //*para declarar un arreglo es similar a una variable
    //*con la diferencia que declaramos el volumen de datos que nuestro arreglo
    //contendra con [numero]
    //la estructura es la siguiente: tipodedato nombre[no.volumen] = {datos}
    int numeros[5] = {1, 2, 3, 4, 5};
    string nombres[4] = {"roberto", "maria", "patrocolo", "Jose"}

    //en este caso lo que hacemos es imprimir en consola uno de los datos de un
    //arreglo, para ello se llama el arreglo y el numero de indice del dato a mostrar
    //?en los arreglos se empieza a contar desde 0, por tanto el dato 0 corresponde
    //?al numero 1 en el arreglo de numeros.
    cout << "el primer elemento es:" << numeros[0]
    cout << "el ultimo elemento es:" << numeros[4]

    //*en este caso para imprimir todo el arreglo, lo que se hace es usar un bucle for
    for (int i = 0; i < 5; ++i){
        cout << "elemento en la posicion" << i << ":" << numeros[i] << endl;
     }

     return 0;
}

