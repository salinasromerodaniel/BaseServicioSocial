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
