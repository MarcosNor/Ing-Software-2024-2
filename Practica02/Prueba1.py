import pymysql

# Establecer conexión a la base de datos
conn = pymysql.connect(
    host='localhost',
    user='lab',
    password='Developer123!',
    database='lab_ing_software'
)

# Crear un cursor
cursor = conn.cursor()

# Datos a insertar en la tabla
datos_pelicula = [
    ("Nombre de la Película 1", "Drama", 120, 5),
    ("Nombre de la Película 2", "Comedia", 90, 3),
    ("Nombre de la Película 3", "Acción", 150, 8)
]

# Consulta SQL para insertar datos
query = "INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)"

# Ejecutar la consulta con los datos
cursor.executemany(query, datos_pelicula)

# Confirmar la transacción
conn.commit()

# Cerrar el cursor y la conexión
cursor.close()
conn.close()