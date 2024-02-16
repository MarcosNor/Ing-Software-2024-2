class NodoBinario:
    def __init__(self, elemento, padre):
        self.elemento = elemento
        self.padre = padre
        self.hijoD = None
        self.hijoI = None

    # métodos para los nodos
    def getElemento(self):
        return self.elemento

    def getHijoL(self):
        return self.left

    def getHijoD(self):
        return self.right

    def getPadre(self):
        return self.parent

class ArbolBinairo:
    def __init__(self,raiz):
        self.raiz = raiz

    def insertar(self, elemento):
        nuevoNodo = NodoBinario(elemento)
        if self.empty():
            self.raiz = nuevoNodo
        else:
            insertarAux(self.root, nuevoNodo)

    def insertarAux(self):
        print("insertar aux")


def pruebaArbol():
    print("pruebaArbol")

def cadena_a_lista(cadena):
    lista_caracteres = []
    for caracter in cadena:
        lista_caracteres.append(caracter)
    return lista_caracteres

def caminante():
    while True:
        try:
            cadena = input("Ingresa la cadena en el formato UUD... : ")

            # Verificamos que el nombre no esté vacío
            if cadena.strip() == "":
                raise ValueError("No has ingresado ningún nombre.")
            # Verificamos si el nombre tiene algún número
            elif any(c.isdigit() for c in cadena):
                raise ValueError("La cadena no puede contener números")
            else:
                break

        except ValueError as e:
            print("Error:", e)

    #Guardamos la cadena en una lista
    listaCadena = cadena_a_lista(cadena)
    valles = 0
    altura = 0


    for caracter in listaCadena:
        if caracter == "U":
            altura += 1
        elif caracter == "D":
            altura -= 1
        else:
            print("Hay un carácter inválido")
            break

        if altura == 0:
            valles += 1

    print("Altura: " + str(altura))

    print("Valles: " + str(valles))


if __name__ == "__main__":

    print("¡Bienvenid@ al script 2!\n")

    print("¿Qué quieres hacer?")

    while True:
        try:
            seleccionUsuario = int(input("1. Árbol\n2. Caminante\n"))

            if seleccionUsuario == 1 or seleccionUsuario == 2:
                if seleccionUsuario == 1:
                    pruebaArbol()
                elif seleccionUsuario == 2:
                    caminante()
                    break

            else:
                print("No ingresaste un valor válido")


        except ValueError:
            print("Error: Por favor, ingresa un número entero válido.")