from flask import Flask
from sqlalchemy import and_, or_

from alchemyClasses import db
from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Rentar import Rentar
from alchemyClasses.Usuario import Usuario
from cryptoUtils.CryptoUtils import cipher
from hashlib import sha256

#from model.model_alumno import borra_alumno

#mysql+pymysql://ferfong:Developer123!@localhost:3306/ing_soft
#<dialecto>+<driver>://<usuario>:<passwd>@localhost:3306/<db>
#mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_soft
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_soft'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

def eleccion():
    print("Da el número del ejercicio que quieres ejecutar (1-4)")
    while True:
        try:
            seleccionUsuario = int(input())
            if seleccionUsuario >= 1 and seleccionUsuario <= 4:

                if seleccionUsuario == 1:
                    menu_1()
                    break

                elif seleccionUsuario == 2:
                    # Pedir al usuario la cadena para filtrar por apellido
                    menu_2()
                    break

                elif seleccionUsuario == 3:
                    menu_3()
                    break


                elif seleccionUsuario == 4:
                    menu_4()
                    break


            else:
                print("No ingresaste un valor válido")

        except ValueError:
            print("Error: Por favor, ingresa un número entero válido.")
    # Pedir al usuario la cadena para filtrar por apellido
    cadena_apellido = input("Introduce la cadena para filtrar por apellido: ")

    # Ejecutar la función para filtrar usuarios por apellido
    filtrar_usuarios_por_apellido(cadena_apellido)

def menu_1():
    print("¿De qué tabla quieres ver los registros?")
    print("1. Película. 2.Usuarios. 3.Rentar")
    while True:
        try:
            seleccionUsuario = int(input())

            if seleccionUsuario >= 1 and seleccionUsuario >= 3:
                if seleccionUsuario == 1:
                    for pelicula in Pelicula.query.all():
                        print(pelicula)
                    break
                elif seleccionUsuario == 2:
                    for usuario in Usuario.query.all():
                        print(usuario)
                    break
                elif seleccionUsuario == 3:
                    for rentar in Rentar.query.all():
                        print(rentar)
                    break
            else:
                print("No ingresaste un valor válido")



        except ValueError:
            print("Error: Por favor, ingresa un número entero válido.")


def menu_4():
    print("¿Quieres eliminar un registro por ID o todos los registros?")
    print("1. Por ID. 2.Todos los registros")
    while True:
        try:
            seleccionUsuario = int(input())
            if seleccionUsuario >= 1 and seleccionUsuario <= 2:
                if seleccionUsuario == 1:
                    while True:
                        try:
                            seleccionUsuario2 = int(input("¿De qué tabla quieres eliminar por ID? "))
                            if seleccionUsuario2 >= 1 and seleccionUsuario2 <= 3:
                                if seleccionUsuario2 == 1:
                                    while True:
                                        try:
                                            seleccionUsuario3 = int(input("Ingresa el ID: "))
                                            if seleccionUsuario2 >= 1 and seleccionUsuario2 <= 3:
                                                if seleccionUsuario2 == 1:
                                                    seleccionUsuario2 = int(input("Ingresa el ID a eliminar: "))
                                            else:
                                                print("No ingresaste un valor válido")


                                        except ValueError:
                                            print("Error: Por favor, ingresa un número entero válido.")
                            else:
                                print("No ingresaste un valor válido")


                        except ValueError:
                            print("Error: Por favor, ingresa un número entero válido.")
            else:
                print("No ingresaste un valor válido")


        except ValueError:
            print("Error: Por favor, ingresa un número entero válido.")

if __name__ == '__main__':
    with app.app_context():

