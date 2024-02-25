import pymysql
import sqlite3


from datetime import datetime

# Conexión a la base de datos
connection = pymysql.connect(host='localhost',
                             user='usuario',
                             password='contraseña',
                             database='lab_ing_software',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# Función para insertar un registro en la tabla
def insertar_registro():
    try:
        # Conexión a la base de datos
        conexion = conectar_bd()
        cursor = conexion.cursor()

        # Seleccionar un ID aleatorio de las otras dos tablas
        tabla1_id = random.randint(1, 100)  # Reemplaza con el rango apropiado
        tabla2_id = random.randint(1, 100)  # Reemplaza con el rango apropiado

        # Generar datos para el nuevo registro
        dato1 = "Dato1"
        dato2 = "Dato2"

        # Insertar el nuevo registro en la tabla
        cursor.execute("INSERT INTO tu_tabla (campo_fk_tabla1, campo_fk_tabla2, dato1, dato2) VALUES (%s, %s, %s, %s)",
                       (tabla1_id, tabla2_id, dato1, dato2))

        # Confirmar la transacción
        conexion.commit()

        print("Registro insertado correctamente.")

    except mysql.connector.Error as error:
        print("Error al insertar registro:", error)

    finally:
        # Cerrar la conexión
        if conexion.is_connected():
            cursor.close()
            conexion.close()




# Función para filtrar usuarios por apellido
def filtrar_usuarios_por_apellido(apellido):
    try:
        # Conexión a la base de datos
        conexion = conectar_bd()
        cursor = conexion.cursor()

        # Consulta SQL para seleccionar usuarios cuyo apellido termine en la cadena especificada
        consulta = "SELECT * FROM usuario WHERE apellido LIKE %s"
        apellido_param = f"%{apellido}"  # Añade '%' al final para buscar coincidencias en el final del apellido
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

                elif seleccionUsuario == 2:
                    # Pedir al usuario la cadena para filtrar por apellido
                    cadena_apellido = input("Introduce la cadena para filtrar por apellido: ")

                    # Ejecutar la función para filtrar usuarios por apellido
                    filtrar_usuarios_por_apellido(cadena_apellido)

                elif seleccionUsuario == 3:

                elif seleccionUsuario == 4:

            else:
                print("No ingresaste un valor válido")


        except ValueError:
            print("Error: Por favor, ingresa un número entero válido.")
    # Pedir al usuario la cadena para filtrar por apellido
    cadena_apellido = input("Introduce la cadena para filtrar por apellido: ")


    # Ejecutar la función para filtrar usuarios por apellido
    filtrar_usuarios_por_apellido(cadena_apellido)

