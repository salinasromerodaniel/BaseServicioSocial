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

def obtener_nombres_subtipo():
    subtipos = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta para obtener los atributos de la tabla SUBTIPO
        cursor.execute("SELECT SUBTIPO_ID, NOMBRE FROM SUBTIPO ORDER BY NOMBRE")

        # Obtiene los resultados de la consulta y los agrega a la lista de subtipos
        for subtipo in cursor.fetchall():
            subtipo_id = subtipo[0]
            nombre = subtipo[1]
            subtipos.append((subtipo_id, nombre))

        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        print("Error al obtener los subtipos:", e)

    return subtipos

def obtener_ubicaciones():
    ubicaciones = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta para obtener los atributos de la tabla UBICACION
        cursor.execute("SELECT UBICACION_ID, NOMBRE FROM UBICACION ORDER BY NOMBRE")

        # Obtiene los resultados de la consulta y los agrega a la lista de ubicaciones
        for ubicacion in cursor.fetchall():
            ubicacion_id = ubicacion[0]
            nombre = ubicacion[1]
            ubicaciones.append((ubicacion_id, nombre))

        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        print("Error al obtener las ubicaciones:", e)

    return ubicaciones




def obtener_info_sistema_operativo():
    info_sistema_operativo = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta para obtener la información de la tabla SISTEMA_OPERATIVO con la unión (JOIN) a la tabla TIPO_SO
        cursor.execute("SELECT SO.SISTEMA_OPERATIVO_ID, TIPO.NOMBRE, SO.NUM_VERSION, SO.ARQUITECTURA FROM SISTEMA_OPERATIVO SO JOIN TIPO_SO TIPO ON SO.TIPO_SO_ID = TIPO.TIPO_SO_ID")

        # Obtiene los resultados de la consulta y los agrega a la lista info_sistema_operativo como tuplas (SISTEMA_OPERATIVO_ID, NOMBRE, NUM_VERSION, ARQUITECTURA)
        info_sistema_operativo = [(sistema_id, nombre, num_version, arquitectura) for sistema_id, nombre, num_version, arquitectura in cursor.fetchall()]

        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        print("Error al obtener la información del sistema operativo:", e)

    return info_sistema_operativo

def obtener_responsables_resguardo():
    responsables = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta para obtener los atributos de la tabla RESPONSABLE_RESGUARDO
        cursor.execute("SELECT RESPONSABLE_RESGUARDO_ID, NOMBRE, AP_PATERNO, AP_MATERNO FROM RESPONSABLE_RESGUARDO")

        # Obtiene los resultados de la consulta y los agrega a la lista de responsables
        for responsable in cursor.fetchall():
            responsable_id = responsable[0]
            nombre = responsable[1]
            ap_paterno = responsable[2]
            ap_materno = responsable[3]
            # Utilizamos un formato legible para el usuario pero almacenamos RESPONSABLE_RESGUARDO_ID como atributo personalizado
            responsable_str = f"{nombre} {ap_paterno} {ap_materno}"
            responsables.append({"id": responsable_id, "nombre": responsable_str})

        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        print("Error al obtener los responsables de resguardo:", e)

    return responsables

def obtener_responsables_interno():
    responsables = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta para obtener los atributos de la tabla RESPONSABLE_RESGUARDO
        cursor.execute("SELECT RESPONSABLE_INTERNO_ID, NOMBRE, AP_PATERNO, AP_MATERNO FROM RESPONSABLE_INTERNO")

        # Obtiene los resultados de la consulta y los agrega a la lista de responsables
        for responsable in cursor.fetchall():
            responsable_id = responsable[0]
            nombre = responsable[1]
            ap_paterno = responsable[2]
            ap_materno = responsable[3]
            responsable_str = f"{nombre} {ap_paterno} {ap_materno}"
            responsables.append((responsable_id, responsable_str))

        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        print("Error al obtener los responsables internos:", e)

    return responsables


def obtener_usuarios_finales():
    usuarios_finales = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta para obtener los atributos de la tabla USUARIO_FINAL
        cursor.execute("SELECT USUARIO_FINAL_ID, NOMBRE, SECTOR_ID, PERFIL_USUARIO_ID FROM USUARIO_FINAL")

        # Obtiene los resultados de la consulta y los agrega a la lista de usuarios finales
        for usuario_final in cursor.fetchall():
            usuario_final_id = usuario_final[0]
            nombre = usuario_final[1]

            # Consulta para obtener el nombre del SECTOR usando la llave foránea SECTOR_ID
            cursor.execute("SELECT NOMBRE FROM SECTOR WHERE SECTOR_ID = %s", (usuario_final[2],))
            sector_nombre = cursor.fetchone()[0]

            # Consulta para obtener el nombre del PERFIL usando la llave foránea PERFIL_USUARIO_ID
            cursor.execute("SELECT PERFIL_USUARIO_NOMBRE FROM PERFIL WHERE PERFIL_USUARIO_ID = %s", (usuario_final[3],))
            perfil_nombre = cursor.fetchone()[0]

            usuario_final_str = f"{nombre} {sector_nombre} {perfil_nombre}"
            usuarios_finales.append((usuario_final_id, usuario_final_str))  # Guardamos el ID y el nombre completo

        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        print("Error al obtener los usuarios finales:", e)

    return usuarios_finales
