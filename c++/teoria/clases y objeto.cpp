#include <iostream>
#include <string>

using namespace std;

// Se define la clase persona
class persona {
public:
    // Variables a utilizar que almacenan los datos
    string nombre;
    int edad;
    string ciudad;

    // Constructor de la clase persona
    persona(string n, int e, string c) {
        nombre = n;
        edad = e;
        ciudad = c;
    }

    // Funci�n que no retorna valor para mostrar la informaci�n
    void mostrarinformacion() {
        cout << "Nombre: " << nombre << ", Edad: " << edad << ", Ciudad: " << ciudad << endl;
    }
};
class espada{
public:
	
	string espnom;
	int dano;
	int crit;
	int vamp;
	int velatt;
	
	espada(string sp, int d, int c, int v, int va){
		espnom = sp;
		dano = d;
		crit = c;
		vamp = v;
		velatt = va;
	}
	void mostrarinformacionesp() {
        cout << "nombre objeto" << espnom << "da�o fisico: " << dano << "Porcentaje de critico: " << crit << "omnivampirismo: " << vamp << "velocidad de ataque:" << velatt << endl;;
    }
};

int main() {
    // Se crea una instancia de la clase y se crea un objeto
    persona persona1("Juan", 25, "Ciudad de Guatemala");
    espada espada1("bebedor de sangre", 45, 25, 18, 25);

    // Se llama al objeto y la funci�n que previamente se cre� para 
    // mostrar la informaci�n
    persona1.mostrarinformacion();
    espada1.mostrarinformacionesp();
    
    return 0;
}

