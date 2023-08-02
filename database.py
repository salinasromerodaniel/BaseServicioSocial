# database.py
import mysql.connector
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',
    'database': 'Inventario',
}
def obtener_nombres_marca():
    nombres = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta para obtener los nombres de la tabla MARCA en orden alfabético
        cursor.execute("SELECT NOMBRE FROM MARCA ORDER BY NOMBRE")

        # Obtiene los resultados de la consulta y los agrega a la lista de nombres
        nombres = [nombre[0] for nombre in cursor.fetchall()]

        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        print("Error al obtener los nombres de la tabla MARCA:", e)

    return nombres

def obtener_nombres_modelo():
    nombres = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta para obtener los nombres de la tabla MODELO en orden alfabético
        cursor.execute("SELECT NOMBRE FROM MODELO ORDER BY NOMBRE")

        # Obtiene los resultados de la consulta y los agrega a la lista de nombres
        nombres = [nombre[0] for nombre in cursor.fetchall()]

        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        print("Error al obtener los nombres de la tabla MODELO:", e)

    return nombres

def obtener_nombres_ubicacion():
    nombres = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta para obtener los nombres de la tabla UBICACION en orden alfabético
        cursor.execute("SELECT NOMBRE FROM UBICACION ORDER BY NOMBRE")

        # Obtiene los resultados de la consulta y los agrega a la lista de nombres
        nombres = [nombre[0] for nombre in cursor.fetchall()]

        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        print("Error al obtener los nombres de la tabla UBICACION:", e)

    return nombres

def obtener_info_sistema_operativo():
    nombres = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta para obtener la información de la tabla SISTEMA_OPERATIVO con la unión (JOIN) a la tabla TIPO_SO
        cursor.execute("SELECT SO.VERSION, SO.ARQUITECTURA, TIPO.NOMBRE FROM SISTEMA_OPERATIVO SO JOIN TIPO_SO TIPO ON SO.TIPO_SO_ID = TIPO.TIPO_SO_ID")

        # Obtiene los resultados de la consulta y los agrega a la lista info_sistema_operativo como tuplas (VERSION, ARQUITECTURA, NOMBRE)
        nombres = [(nombre, version, arquitectura) for version, arquitectura, nombre in cursor.fetchall()]

        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        print("Error al obtener la información del sistema operativo:", e)
    return nombres

