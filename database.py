# database.py
import mysql.connector
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',
    'database': 'inventario',
}

def insertar_dispoI(factura, serial, num_inventario, subtipo, nombre,
                    ram_instalada, ram_maxima, num_procesadores, modelo,
                    caracteristicas, ubicacion, usuario, resguardo, interno, sistema_operativo_ids, lista_ids_ram, fecha_ram):
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Crear la consulta SQL para la inserción en la tabla ACTIVO
        insert_activo_query = "INSERT INTO ACTIVO (FACTURA, NUM_SERIAL, NUM_INVENTARIO, TIPO, NOMBRE, ESTADO, USUARIO_FINAL_ID, RESPONSABLE_INTERNO_ID, RESPONSABLE_RESGUARDO_ID, MODELO_ID, UBICACION_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # Definir los valores para la inserción en la tabla ACTIVO
        values_activo = (factura, serial, num_inventario, "I", nombre, "ACTIVO", usuario, interno, resguardo, modelo, ubicacion)
        # Ejecutar la consulta de inserción en la tabla ACTIVO
        cursor.execute(insert_activo_query, values_activo)
        # Obtener el ID generado automáticamente en la tabla ACTIVO
        activo_id = cursor.lastrowid
        # Crear la consulta SQL para la inserción en la tabla DISPO_INTELIGENTE
        insert_dispo_query = "INSERT INTO DISPO_INTELIIGENTE (ACTIVO_ID, CARACTERISTICAS, NUM_PROCESADORES, RAM_INSTALADA, RAM_MAX, SUBTIPO_ID) VALUES (%s, %s, %s, %s, %s, %s)"
        # Definir los valores para la inserción en la tabla DISPO_INTELIGENTE
        values_dispo = (activo_id, caracteristicas, num_procesadores, ram_instalada, ram_maxima, subtipo)
        # Ejecutar la consulta de inserción en la tabla DISPO_INTELIGENTE
        cursor.execute(insert_dispo_query, values_dispo)
        # Insertar en la tabla DISPO_SO para cada ID de sistema operativo
        insert_dispo_so_query = "INSERT INTO DISPO_SO (ACTIVO_ID, SISTEMA_OPERATIVO_ID) VALUES (%s, %s)"
        for so_id in sistema_operativo_ids:
            cursor.execute(insert_dispo_so_query, (activo_id, so_id))
        # Insertar en la tabla DISPO_RAM para cada ID de sistema operativo
        insert_dispo_ram_query = "INSERT INTO DISPO_RAM (ACTIVO_ID, RAM_ID, FECHA_COLOC) VALUES (%s, %s, %s)"
        for ram_id in lista_ids_ram:
            cursor.execute(insert_dispo_ram_query, (activo_id, ram_id, fecha_ram))
        # Confirmar las inserciones en la base de datos
        conn.commit()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        print("Inserción exitosa en las tablas ACTIVO, DISPO_INTELIGENTE y DISPO_SO.")
    except mysql.connector.Error as error:
        print("Error al insertar en las tablas ACTIVO, DISPO_INTELIGENTE y DISPO_SO:", error)



def obtener_info_modelo():
    info_modelo = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta para obtener la información de la tabla MODELO con la unión (JOIN) a la tabla MARCA
        cursor.execute("SELECT M.MODELO_ID, M.NOMBRE, MAR.NOMBRE FROM MODELO M JOIN MARCA MAR ON M.MARCA_ID = MAR.MARCA_ID")

        # Obtiene los resultados de la consulta y los agrega a la lista info_modelo como tuplas (MODELO_ID, NOMBRE_MODELO, NOMBRE_MARCA)
        info_modelo = [(modelo_id, nombre_modelo, nombre_marca) for modelo_id, nombre_modelo, nombre_marca in cursor.fetchall()]

        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()

        # Utilizar un conjunto para obtener las marcas únicas
        marcas_unicas = set(nombre_marca for _, _, nombre_marca in info_modelo)

        # Ordenar alfabéticamente las marcas únicas
        marcas_ordenadas = sorted(marcas_unicas)

        # Crear una lista para almacenar las tuplas de (MODELO_ID, NOMBRE_MODELO, NOMBRE_MARCA) agrupadas por marca
        info_modelo_agrupado = []

        # Iterar sobre las marcas ordenadas y agregar los modelos asociados a cada marca a la lista info_modelo_agrupado
        for marca in marcas_ordenadas:
            modelos_de_marca = [(modelo_id, nombre_modelo, nombre_marca) for modelo_id, nombre_modelo, nombre_marca in info_modelo if nombre_marca == marca]
            info_modelo_agrupado.append((marca, modelos_de_marca))

    except mysql.connector.Error as e:
        print("Error al obtener la información del modelo:", e)

    return info_modelo_agrupado

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

def obtener_info_ram():
    info_ram = []
    try:
        # Realiza la conexión a la base de datos (debes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta para obtener la información de la tabla RAM con la unión (JOIN) a la tabla TIPO_RAM
        cursor.execute("SELECT RAM.RAM_ID, RAM.MARCA, RAM.NUM_SERIE, TIPO.NOMBRE, RAM.CAPACIDAD FROM RAM "
                       "JOIN TIPO_RAM TIPO ON RAM.TIPO_RAM_ID = TIPO.TIPO_RAM_ID")

        # Obtiene los resultados de la consulta y los agrega a la lista info_ram como tuplas (RAM_ID, MARCA, NUM_SERIE, NOMBRE, CAPACIDAD)
        info_ram = [(ram_id, marca, num_serie, nombre, capacidad) for ram_id, marca, num_serie, nombre, capacidad in cursor.fetchall()]

        # Ordena la lista info_ram por marca
        info_ram = sorted(info_ram, key=lambda x: x[1])

        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener la información de la RAM:", e)
    return info_ram

def obtener_info_almacenamiento():
    info_almacenamiento = []
    try:
        # Realiza la conexión a la base de datos (debes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta para obtener la información de la tabla DISCO_DURO
        cursor.execute("SELECT DISCO_DURO_ID, NUMERO_SERIE, DISCO_DURO_MARCA, DISCO_DURO_MODELO, DISCO_DURO_CAPACIDAD FROM DISCO_DURO")
        
        # Obtiene los resultados de la consulta y los agrega a la lista info_almacenamiento
        info_almacenamiento = [(disco_id, num_serie, marca, modelo, capacidad) for disco_id, num_serie, marca, modelo, capacidad in cursor.fetchall()]
        
        # Ordena la lista info_almacenamiento por marca
        info_almacenamiento = sorted(info_almacenamiento, key=lambda x: x[2])

        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener la información de almacenamiento:", e)
    return info_almacenamiento




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


def insertar_dispoH(factura, serial, num_inventario, nombre,
                    modelo, fecha_compra, cantidad, contenido,
                    descripcion, ubicacion, usuario, resguardo, interno):
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        consumo = None
        # Crear la consulta SQL para la inserción en la tabla ACTIVO
        insert_activo_query = "INSERT INTO ACTIVO (FACTURA, NUM_SERIAL, NUM_INVENTARIO, TIPO, NOMBRE, ESTADO, USUARIO_FINAL_ID, RESPONSABLE_INTERNO_ID, RESPONSABLE_RESGUARDO_ID, MODELO_ID, UBICACION_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # Definir los valores para la inserción en la tabla ACTIVO
        values_activo = (factura, serial, num_inventario, "H", nombre, "ACTIVO", usuario, interno, resguardo, modelo, ubicacion)
        # Ejecutar la consulta de inserción en la tabla ACTIVO
        cursor.execute(insert_activo_query, values_activo)
        # Obtener el ID generado automáticamente en la tabla ACTIVO
        activo_id = cursor.lastrowid
        # Crear la consulta SQL para la inserción en la tabla DISPO_INTELIGENTE
        insert_dispo_query = "INSERT INTO HERRAMIENTA_CONSUMIBLE (ACTIVO_ID, FECHA_COMPRA, FECHA_CONSUMO, CANTIDAD,CONTENIDO, DESCRIPCION) VALUES (%s, %s, %s, %s, %s, %s)"
        # Definir los valores para la inserción en la tabla DISPO_INTELIGENTE
        values_dispo = (activo_id, fecha_compra,consumo, cantidad, contenido, descripcion)
        # Ejecutar la consulta de inserción en la tabla DISPO_INTELIGENTE
        cursor.execute(insert_dispo_query, values_dispo)
        # Confirmar las inserciones en la base de datos
        conn.commit()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        print("Inserción exitosa en las tablas ACTIVO y HERRAMIENTA O CONSUMIBLE.")

    except mysql.connector.Error as error:
        print("Error al insertar en las tablas ACTIVO y HERRAMIENTA O CONSUMIBLE:", error)

def insertar_dispoL(factura, serial, num_inventario, nombre,
                    autor, editorial, anio, edicion,
                     ubicacion, usuario, resguardo, interno):
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Crear la consulta SQL para la inserción en la tabla ACTIVO
        insert_activo_query = "INSERT INTO ACTIVO (FACTURA, NUM_SERIAL, NUM_INVENTARIO, TIPO, NOMBRE, ESTADO, USUARIO_FINAL_ID, RESPONSABLE_INTERNO_ID, RESPONSABLE_RESGUARDO_ID, MODELO_ID, UBICACION_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # Definir los valores para la inserción en la tabla ACTIVO
        # el modelo simepre debe estar como N/A=id(76)
        values_activo = (factura, serial, num_inventario, "L", nombre, "ACTIVO", usuario, interno, resguardo, 76, ubicacion)
        # Ejecutar la consulta de inserción en la tabla ACTIVO
        cursor.execute(insert_activo_query, values_activo)
        # Obtener el ID generado automáticamente en la tabla ACTIVO
        activo_id = cursor.lastrowid
        # Crear la consulta SQL para la inserción en la tabla DISPO_INTELIGENTE
        insert_dispo_query = "INSERT LIBRO (ACTIVO_ID, EDITORIAL, EDICION, ANIO, AUTOR) VALUES (%s, %s, %s, %s, %s)"
        # Definir los valores para la inserción en la tabla DISPO_INTELIGENTE
        values_dispo = (activo_id, editorial, edicion, anio, autor)
        # Ejecutar la consulta de inserción en la tabla DISPO_INTELIGENTE
        cursor.execute(insert_dispo_query, values_dispo)
        # Confirmar las inserciones en la base de datos
        conn.commit()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        print("Inserción exitosa en las tablas LIBRO.")

    except mysql.connector.Error as error:
        print("Error al insertar en las tablas LIBRO:", error)


def obtener_libros():
    libros = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta para obtener los atributos de la tabla LIBRO con información de ACTIVO
        cursor.execute("SELECT L.ACTIVO_ID, L.EDITORIAL, L.EDICION, L.ANIO, L.AUTOR, A.FACTURA, A.NUM_SERIAL, A.NUM_INVENTARIO, A.TIPO, A.NOMBRE AS NOMBRE_ACTIVO, A.ESTADO FROM LIBRO L INNER JOIN ACTIVO A ON L.ACTIVO_ID = A.ACTIVO_ID")

        # Obtiene los resultados de la consulta y los agrega a la lista de ubicaciones
        for libro in cursor.fetchall():
            activo_id = libro[0]#
            editorial = libro[1]#
            edicion = libro[2]
            anio = libro[3]
            autor = libro[4]#
            factura = libro[5]#
            num_serial = libro[6]#
            num_inventario = libro[7]#
            tipo = libro[8]#
            nombre_activo = libro[9]#
            estado = libro[10]#
            #USUARIO_FINAL
            #RESPONSABLE_INTERNO
            #RESPONSABLE_RESGUARDO
            #UBICACION
            libros.append((activo_id, editorial, edicion, anio, autor, factura, num_serial, num_inventario, tipo, nombre_activo, estado))
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener los libros:", e)
    return libros


def eliminar_libros(libro_id):
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Sentencia SQL para eliminar el libro con el libro_id proporcionado
        delete_query = "DELETE FROM LIBRO WHERE ACTIVO_ID = %s"
        # Ejecuta la eliminación con el libro_id proporcionado
        cursor.execute(delete_query, (libro_id,))
        # Confirma los cambios en la base de datos
        conn.commit()
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al eliminar el libro:", e)
        # Maneja el error adecuadamente (puedes levantar una excepción o imprimir un mensaje)

def obtener_libroID(id_especifico):
    libros = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta con el filtro para el ID específico
        cursor.execute(f"SELECT A.ACTIVO_ID, A.FACTURA, A.NUM_SERIAL, A.NUM_INVENTARIO, A.TIPO, A.NOMBRE AS NOMBRE_ACTIVO, A.ESTADO, L.EDITORIAL, L.EDICION, L.ANIO, L.AUTOR FROM ACTIVO A INNER JOIN LIBRO L ON A.ACTIVO_ID = L.ACTIVO_ID WHERE A.ACTIVO_ID = {id_especifico}")

        # Obtiene los resultados de la consulta y los agrega a la lista de libros
        for libro in cursor.fetchall():
            activo_id = libro[0] #no se debe mostrar para cambiar
            factura = libro[1]#
            num_serial = libro[2]#
            num_inventario = libro[3]#
            tipo = libro[4] #no se debe mostrar para cambiar
            nombre_activo = libro[5]
            estado = libro[6]
            editorial = libro[7]#
            edicion = libro[8]#
            anio = libro[9]#
            autor = libro[10]#
            # Agrega los atributos de usuario final, responsable interno, responsable resguardo y ubicación si es necesario
            usuario_final = libro[11]#
            responsable_interno = libro[12]#
            responsable_resguardo = libro[13]#
            ubicacion = libro[14]#
            libros.append((activo_id, factura, num_serial, num_inventario, tipo, nombre_activo, estado, editorial, edicion, anio, autor, usuario_final, responsable_interno,responsable_resguardo, ubicacion))
        
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener los libros:", e)
    return libros
