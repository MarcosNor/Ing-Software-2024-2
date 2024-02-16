import random

# Sé que no usé las mejores prácticas de programación jaja, pido perdón
def nombreCorrecto(nombre):
    print("El nombre")

def jugadorComienza(jugador1,jugador2,contador):
    if contador == 0:
        jugadores = [jugador1, jugador2]
        jugadorElegido = random.choice(jugadores)

        if jugadorElegido == jugador1:
            contador = 1
            return jugadorElegido
        elif jugadorElegido == jugador2:
            contador = 2
            return jugadorElegido

    if contador == 1:
        return jugador2
        contador = 2
    elif contador == 2:
        contador = 1
        return jugador1

    return jugadorElegido


def logicaSets(puntaje, jugador1, jugador2):
    while True:
        ganadorSet = 0
        ganadorSet = logicaPuntosJuego(puntaje)

        if ganadorSet == 1 or ganadorSet == 2:
            return ganadorSet

        try:
            puntoParaJugador = int(input("¿Qué jugador hace punto? ingresa el número correspondiente: "))
            if puntoParaJugador == 1 or puntoParaJugador == 2:
                if puntoParaJugador == 1:
                    print("Punto para jugador 1")
                    puntos[0] += 1

                elif puntoParaJugador == 2:
                    print("Punto para jugador 2")
                    puntos[1] += 1
            else:
                print("Ingresa un número válido")
        except ValueError:
            print("Error: Por favor, ingresa un número entero válido.")


#Función para calcular los puntos reales del juego
def logicaPuntosJuego(puntaje):

    if puntaje[0] >= 4 or puntaje [1] >= 4:
        if puntaje[0] - puntaje[1] == 0:
            print("Puntaje: 40 - 40")
        elif puntaje[0] - puntaje[1] == 1:
            print("Puntaje: adv. - 40")
        elif puntaje[0] - puntaje[1] >= 2:
            return 1
        elif puntaje[1] - puntaje[0] == 1:
            print("Puntaje: 40 - adv.")
        elif puntaje[1] - puntaje[0] >= 2:
            return 2

    elif puntaje[0] == 0 and puntaje[1] == 0:
        print("Puntaje: 0 - 0")
    elif puntaje[0] == 0 and puntaje[1] == 1:
        print("Puntaje: 0 - 15")
    elif puntaje[0] == 0 and puntaje[1] == 2:
        print("Puntaje: 0 - 30")
    elif puntaje[0] == 0 and puntaje[1] == 3:
        print("Puntaje: 0 - 40")

    elif puntaje[0] == 1 and puntaje[1] == 0:
        print("Puntaje: 15 - 0")
    elif puntaje[0] == 1 and puntaje[1] == 1:
        print("Puntaje: 15 - 15")
    elif puntaje[0] == 1 and puntaje[1] == 2:
        print("Puntaje: 15 - 30")
    elif puntaje[0] == 1 and puntaje[1] == 3:
        print("Puntaje: 15 - 40")

    elif puntaje[0] == 2 and puntaje[1] == 0:
        print("Puntaje: 30 - 0")
    elif puntaje[0] == 2 and puntaje[1] == 1:
        print("Puntaje: 30 - 15")
    elif puntaje[0] == 2 and puntaje[1] == 2:
        print("Puntaje: 30 - 30")
    elif puntaje[0] == 2 and puntaje[1] == 3:
        print("Puntaje: 30 - 40")

    elif puntaje[0] == 3 and puntaje[1] == 0:
        print("Puntaje: 40 - 0")
    elif puntaje[0] == 3 and puntaje[1] == 1:
        print("Puntaje: 40 - 15")
    elif puntaje[0] == 3 and puntaje[1] == 2:
        print("Puntaje: 40 - 30")
    elif puntaje[0] == 3 and puntaje[1] == 3:
        print("Puntaje: 40 - 40")


if __name__ == '__main__':
    print("¡Hola! Bienvenido al partido de tenis\n")
    print("Ingresa el nombre de los jugadores")

while True:
    try:
        jugador1 = input("Jugador 1: ")

        # Verificamos que el nombre no esté vacío
        if jugador1.strip() == "":
            raise ValueError("No has ingresado ningún nombre.")
        # Verificamos si el nombre tiene algún número
        elif any(c.isdigit() for c in jugador1):
            raise ValueError("El nombre no puede contener números.")
        else:
            print("Nombre ingresado correctamente:", jugador1)
            break

    except ValueError as e:
        print("Error:", e)

while True:
    try:
        # Pedir al usuario que ingrese un nombre
        jugador2 = input("Jugador 2: ")

        # Verificar si el nombre está vacío
        if jugador2.strip() == "":
            raise ValueError("No has ingresado ningún nombre.")
        # Verificar si el nombre contiene algún número
        elif any(c.isdigit() for c in jugador2):
            raise ValueError("El nombre no puede contener números.")
        else:
            print("Nombre ingresado correctamente:", jugador2)
            break

    except ValueError as e:
        print("Error:", e)

print("\nEl mejor de 3 sets, gana")
numeroSets = 0



sets = 1
contadorJugadorSaca = 0
puntajeSets = [0,0]


while True:

    puntos = [0, 0]

    if puntajeSets[0] >= 3 or puntajeSets[1] >= 3:
        if puntajeSets[1] - puntajeSets[0] > 0:
            print("\n¡¡El jugador " + str(jugador1) + " gana!!")
            break
        elif puntajeSets[0] - puntajeSets[1] > 0:
            print("\n¡¡El jugador " + str(jugador2) + " gana!!")
            break

    jugadorSaca = jugadorComienza(jugador1, jugador2, contadorJugadorSaca)

    print("Comienza set " + str(sets))
    print("En este set saca el jugador " + jugadorSaca)


    puntosJuego = [0, 0]
    ganadorDelSet = logicaSets(puntos, jugador1, jugador2)

    if ganadorDelSet == 1:
        print("\nEl jugador " + str(jugador1) + " gana un set")
        sets += 1
        puntajeSets[0] += 1
    elif ganadorDelSet == 2:
        print("\nEl jugador " + str(jugador2) + " gana un set")
        sets += 1
        puntajeSets[1] += 1

    print("Puntuación sets: " + str(puntajeSets[0]) + " - " + str(puntajeSets[1]))

