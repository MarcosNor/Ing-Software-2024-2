import mysql
import pymysql
import sqlite3
from datetime import datetime

def conectar_bd():

    conexion = pymysql.connect(
        host='localhost',
        user='lab',
        password='Developer123!',
        database='lab_ing_software'
    )
    return conexion


# Función para insertar un registro en la tabla
def insertar_registro():

    conexion = conectar_bd()
    cursor = conexion.cursor()
    try:
        with conexion.cursor() as cursor:
            # Insertar un usuario
            sql = "INSERT INTO usuarios (nombre, password, email, superUser) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, ('Nombre usuario', 'contraseña', 'usuario@gmail.com', 0))
            id_usuario = cursor.lastrowid

            # Insertar una película
            sql = "INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, ('Nombre pelicula', 'genero', 90, 5))
            id_pelicula = cursor.lastrowid  # Obtener el ID de la película insertada

            # Insertar un registro de renta
            sql = "INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (id_usuario, id_pelicula, datetime.now(), 7, 1))

        # Confirmar la transacción
        conexion.commit()

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def filtrar_usuarios_por_apellido(apellido):
    try:

        conexion = conectar_bd()
        cursor = conexion.cursor()

        #Buscamos en la tabla usuario los apellidos que contengan lo que hay en like
        consulta = "SELECT * FROM usuario WHERE apellido LIKE %s"
        apellido_param = f"%{apellido}"
        cursor.execute(consulta, (apellido_param,))

        # Obtener resultados
        resultados = cursor.fetchall()

        # Mostrar los usuarios encontrados
        if resultados:
            print("Usuarios encontrados:")
            for usuario in resultados:
                print(usuario)
        else:
            print("No se encontraron usuarios con ese apellido.")

    except mysql.connector.Error as error:
        print("Error al filtrar usuarios:", error)

    finally:
        # Cerrar la conexión
        if conexion.is_connected():
            cursor.close()
            conexion.close()


if __name__ == '__main__':

    try:
        conexion = pymysql.connect(host='localhost',
                                   user='lab',
                                   password='Developer123!',
                                   db='lab_ing_software')
        print("Conexión correcta")
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)

    print("Da el número del ejercicio que quieres ejecutar (1-4)")

    while True:
        try:
            seleccionUsuario = int(input())

            if seleccionUsuario > 1 or seleccionUsuario > 4:

                if seleccionUsuario == 1:
                    # Ejecutar la función para insertar un registro
                    insertar_registro()
                    break

                elif seleccionUsuario == 2:
                    # Pedir al usuario la cadena para filtrar por apellido
                    cadena_apellido = input("Introduce la cadena para filtrar por apellido: ")

                    # Ejecutar la función para filtrar usuarios por apellido
                    filtrar_usuarios_por_apellido(cadena_apellido)
                    break

                elif seleccionUsuario == 3:
                    break

                elif seleccionUsuario == 4:
                    break

            else:
                print("No ingresaste un valor válido")


        except ValueError:
            print("Error: Por favor, ingresa un número entero válido.")