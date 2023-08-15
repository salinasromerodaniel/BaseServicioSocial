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
                    caracteristicas, ubicacion, lista_ids_usuario, lista_ids_resguardo, lista_ids_interno, 
                    sistema_operativo_ids, lista_ids_ram, fecha_ram, lista_ids_almacenamiento, lista_ids_micro, 
                    lista_ids_tarjeta, lista_ids_puerto, lista_ids_lectora, lista_ids_red, lista_ids_ip, lista_ids_mac):
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Crear la consulta SQL para la inserción en la tabla ACTIVO
        insert_activo_query = "INSERT INTO ACTIVO (FACTURA, NUM_SERIAL, NUM_INVENTARIO, TIPO, NOMBRE, ESTADO, MODELO_ID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        # Definir los valores para la inserción en la tabla ACTIVO
        values_activo = (factura, serial, num_inventario, "I", nombre, "ACTIVO", modelo)
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
        if sistema_operativo_ids:
            insert_dispo_so_query = "INSERT INTO DISPO_SO (ACTIVO_ID, SISTEMA_OPERATIVO_ID, FECHA_COLOC, OPERANTE) VALUES (%s, %s, %s, %s)"
            for so_id in sistema_operativo_ids:
                cursor.execute(insert_dispo_so_query, (activo_id, so_id, fecha_ram, 1))
        # Insertar en la tabla DISPO_RAM para cada ID de ram
        if lista_ids_ram:
            insert_dispo_ram_query = "INSERT INTO DISPO_RAM (ACTIVO_ID, RAM_ID, FECHA_COLOC, OPERANTE) VALUES (%s, %s, %s, %s)"
            for ram_id in lista_ids_ram:
                cursor.execute(insert_dispo_ram_query, (activo_id, ram_id, fecha_ram, 1))
        # Insertar en la tabla DISPO_DD para cada ID de almacenamiento
        if lista_ids_almacenamiento:
            insert_dispo_almacenamiento_query = "INSERT INTO DISPO_DD(ACTIVO_ID, DISCO_DURO_ID, FECHA_COLOC, OPERANTE) VALUES (%s, %s, %s, %s)"
            for almacenamiento_id in lista_ids_almacenamiento:
                cursor.execute(insert_dispo_almacenamiento_query, (activo_id, almacenamiento_id, fecha_ram, 1))
        # Insertar en la tabla DISPO_MICRO para cada ID de microprocesador
        if lista_ids_micro:
            insert_dispo_micro_query = "INSERT INTO DISPO_MICRO(ACTIVO_ID, MICROPROCESADOR_ID, FECHA_COLOC, OPERANTE) VALUES (%s, %s, %s, %s)"
            for micro_id in lista_ids_micro:
                cursor.execute(insert_dispo_micro_query, (activo_id, micro_id, fecha_ram, 1))
        # Insertar en la tabla DISPO_VIDEO para cada ID de tarjeta gráfica
        if lista_ids_tarjeta:
            insert_dispo_tarjeta_query = "INSERT INTO DISPO_VIDEO(ACTIVO_ID, TARGETA_GARFICA_ID, FECHA_COLOC, OPERANTE) VALUES (%s, %s, %s, %s)"
            for tarjeta_id in lista_ids_tarjeta:
                cursor.execute(insert_dispo_tarjeta_query, (activo_id, tarjeta_id, fecha_ram, 1))
        # Insertar en la tabla DISPO_LECTORA para cada ID de PUERTO
        if lista_ids_puerto:
            insert_dispo_puerto_query = "INSERT INTO DISPO_PUERTO(PUERTO_ID, ACTIVO_ID, FECHA_COLOC, OPERANTE) VALUES (%s, %s, %s, %s)"
            for puerto_id in lista_ids_puerto:
                cursor.execute(insert_dispo_puerto_query, (puerto_id, activo_id, fecha_ram, 1))
        if lista_ids_lectora:
            insert_dispo_lectora_query = "INSERT INTO DISPO_LECTORA(ACTIVO_ID, UNIDAD_LECTORA_ID, FECHA_COLOC, OPERANTE) VALUES (%s, %s, %s, %s)"
            for lectora_id in lista_ids_lectora:
                cursor.execute(insert_dispo_lectora_query, (activo_id, lectora_id, fecha_ram, 1))
        if lista_ids_red:
            insert_dispo_red_query = "INSERT INTO DISPOSITIVO_RED(ACTIVO_ID, INTERFAZ_RED_ID, MAC, IP, FECHA_COLOC, OPERANTE) VALUES (%s, %s, %s, %s, %s, %s)"
            for red_id, mac, ip in zip(lista_ids_red, lista_ids_mac, lista_ids_ip):
                cursor.execute(insert_dispo_red_query, (activo_id, red_id, mac, ip, fecha_ram, 1))
        
        insert_dispo_ubicacion_query = "INSERT INTO HISTORICO_ACTIVO_UBICACION(FECHA_CAMBIO, UBICACION_ID, ACTIVO_ID) VALUES (%s, %s, %s)"    
        cursor.execute(insert_dispo_ubicacion_query, (fecha_ram, ubicacion, activo_id))
        
        if lista_ids_usuario:
            insert_dispo_usuario_query = "INSERT INTO HISTORICO_ACTIVO_USUARIO(FECHA_PRESTAMO, USUARIO_FINAL_ID, ACTIVO_ID, OPERANTE) VALUES (%s, %s, %s, %s)"    
            for usuario_id in lista_ids_usuario:
                cursor.execute(insert_dispo_usuario_query, (fecha_ram, usuario_id, activo_id, 1))
        if lista_ids_resguardo:       
            insert_dispo_resguardo_query = "INSERT INTO HISTORICO_ACTIVO_RESPONSABLE(FECHA_CAMBIO_RESGUARDO, RESPONSABLE_RESGUARDO_ID, ACTIVO_ID, OPERANTE) VALUES (%s, %s, %s, %s)"    
            for resguardo_id in lista_ids_resguardo:
                cursor.execute(insert_dispo_resguardo_query, (fecha_ram, resguardo_id, activo_id, 1))
        if lista_ids_interno:
            insert_dispo_interno_query = "INSERT INTO HISTORICO_ACTIVO_RESPONSABLE_INTERNO(FECHA_PRESTAMO, RESPONSABLE_INTERNO_ID, ACTIVO_ID, OPERANTE) VALUES (%s, %s, %s, %s)"    
            for interno_id in lista_ids_interno:
                cursor.execute(insert_dispo_interno_query, (fecha_ram, interno_id, activo_id, 1))
        # Confirmar las inserciones en la base de datos
        conn.commit()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        print("Inserción exitosa en las tablas.")
    except mysql.connector.Error as error:
        print("Error al insertar en las tablas:", error)



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

def obtener_info_lectora():
    info_lectora = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta para obtener la información de la tabla UNIDAD_LECTORA con la unión (JOIN) a la tabla TIPO_UNIDAD_LECTORA
        cursor.execute("SELECT LECT.UNIDAD_LECTORA_ID, TIPO.TIPO_UNIDAD_LECTORA_NOMBRE, LECT.UNIDAD_LECTORA_MODELO, LECT.UNIDAD_LECTORA_MARCA FROM UNIDAD_LECTORA LECT JOIN TIPO_UNIDAD_LECTORA TIPO ON LECT.TIPO_UNIDAD_LECTORA_ID = TIPO.TIPO_UNIDAD_LECTORA_ID")

        # Obtiene los resultados de la consulta y los agrega a la lista info_lectora como tuplas
        info_lectora = [(unidad_id, tipo_nombre, modelo, marca) for unidad_id, tipo_nombre, modelo, marca in cursor.fetchall()]

        # Ordena la lista info_lectora por UNIDAD_LECTORA_MARCA
        info_lectora = sorted(info_lectora, key=lambda x: x[3])

        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener la información de unidad lectora:", e)
    return info_lectora

def obtener_info_red():
    info_red = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta para obtener la información de la tabla INTERFAZ_RED con la unión (JOIN) a la tabla TIPO_INTERFAZ_RED
        cursor.execute("SELECT INTER.INTERFAZ_RED_ID, INTER.INTERFAZ_RED_NOMBRE, INTER.INTERFAZ_RED_MODELO, INTER.INTERFAZ_RED_MARCA, INTER.INTEG_O_EXTERN, TIPO.NOMBRE FROM INTERFAZ_RED INTER JOIN TIPO_INTERFAZ_RED TIPO ON INTER.TIPO_INTERFAZ_RED_ID = TIPO.TIPO_INTERFAZ_RED_ID")

        # Obtiene los resultados de la consulta y los agrega a la lista info_red como tuplas
        info_red = [(interfaz_id, nombre, modelo, marca, integ_o_extern, tipo_nombre) for interfaz_id, nombre, modelo, marca, integ_o_extern, tipo_nombre in cursor.fetchall()]

        # Ordena la lista info_red por INTERFAZ_RED_MARCA
        info_red = sorted(info_red, key=lambda x: x[3])

        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener la información de interfaz de red:", e)
    return info_red



def obtener_nombres_puerto():
    lista_puertos = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta para obtener los atributos de la tabla PUERTO
        cursor.execute("SELECT PUERTO_ID, PUERTO_NOMBRE FROM PUERTO ORDER BY PUERTO_NOMBRE")

        # Obtiene los resultados de la consulta y los agrega a la lista de puertos
        for puerto in cursor.fetchall():
            puerto_id = puerto[0]
            nombre = puerto[1]
            lista_puertos.append((puerto_id, nombre))

        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener los puertos:", e)
    return lista_puertos


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

def obtener_info_micro():
    info_micro = []
    try:
        # Realiza la conexión a la base de datos (debes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta para obtener la información de la tabla MICROPROCESADOR JOIN MARCA
        cursor.execute("SELECT MICRO.MICROPROCESADOR_ID, MICRO.NOMBRE, MICRO.ARQUITECTURA, MICRO.GENERACION, MAR.NOMBRE FROM MICROPROCESADOR MICRO JOIN MARCA MAR ON MICRO.MARCA_ID = MAR.MARCA_ID")
        
        # Obtiene los resultados de la consulta y los agrega a la lista info_micro como tuplas
        info_micro = [(micro_id, nombre, arquitectura, generacion, marca) for micro_id, nombre, arquitectura, generacion, marca in cursor.fetchall()]
        
        # Ordena la lista info_micro por marca
        info_micro = sorted(info_micro, key=lambda x: x[4])

        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener la información de microprocesador:", e)
    return info_micro

def obtener_info_tarjeta():
    info_tarjeta = []
    try:
        # Realiza la conexión a la base de datos (debes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta para obtener la información de la tabla TARGETA_GRAFICA JOIN TIPO_TARGETA_GRAFICA y TIPO_PCI
        cursor.execute("SELECT TAR.TARGETA_GARFICA_ID, TAR.TARGETA_GRAFICA_MARCA, TAR.TARGETA_GRAFICA_MODELO, TIPO.TIPO_TARGETA_GRAFICA_NOMBRE, PCI.TIPO_PCI_NOMBRE FROM TARGETA_GRAFICA TAR JOIN TIPO_TARGETA_GRAFICA TIPO ON TAR.TIPO_TARGETA_GRAFICA_ID = TIPO.TIPO_TARGETA_GRAFICA_ID JOIN TIPO_PCI PCI ON TAR.TIPO_PCI_ID = PCI.TIPO_PCI_ID")

        # Obtiene los resultados de la consulta y los agrega a la lista info_tarjeta como tuplas
        info_tarjeta = [(tarjeta_id, marca, modelo, tipo_nombre, pci_nombre) for tarjeta_id, marca, modelo, tipo_nombre, pci_nombre in cursor.fetchall()]
        
        # Ordena la lista info_tarjeta por targeta_grafica_marca
        info_tarjeta = sorted(info_tarjeta, key=lambda x: x[1])
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener la información de tarjeta:", e)
    return info_tarjeta



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
                    descripcion, ubicacion, lista_ids_usuario, lista_ids_resguardo, lista_ids_interno):
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        consumo = None
        # Crear la consulta SQL para la inserción en la tabla ACTIVO
        insert_activo_query = "INSERT INTO ACTIVO (FACTURA, NUM_SERIAL, NUM_INVENTARIO, TIPO, NOMBRE, ESTADO, MODELO_ID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        # Definir los valores para la inserción en la tabla ACTIVO
        values_activo = (factura, serial, num_inventario, "H", nombre, "ACTIVO", modelo)
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
        insert_dispo_ubicacion_query = "INSERT INTO HISTORICO_ACTIVO_UBICACION(FECHA_CAMBIO, UBICACION_ID, ACTIVO_ID) VALUES (%s, %s, %s)"    
        cursor.execute(insert_dispo_ubicacion_query, (fecha_compra, ubicacion, activo_id))
        
        if lista_ids_usuario:
            insert_dispo_usuario_query = "INSERT INTO HISTORICO_ACTIVO_USUARIO(FECHA_PRESTAMO, USUARIO_FINAL_ID, ACTIVO_ID, OPERANTE) VALUES (%s, %s, %s, %s)"    
            for usuario_id in lista_ids_usuario:
                cursor.execute(insert_dispo_usuario_query, (fecha_compra, usuario_id, activo_id, 1))
        if lista_ids_resguardo:       
            insert_dispo_resguardo_query = "INSERT INTO HISTORICO_ACTIVO_RESPONSABLE(FECHA_CAMBIO_RESGUARDO, RESPONSABLE_RESGUARDO_ID, ACTIVO_ID, OPERANTE) VALUES (%s, %s, %s, %s)"    
            for resguardo_id in lista_ids_resguardo:
                cursor.execute(insert_dispo_resguardo_query, (fecha_compra, resguardo_id, activo_id, 1))
        if lista_ids_interno:
            insert_dispo_interno_query = "INSERT INTO HISTORICO_ACTIVO_RESPONSABLE_INTERNO(FECHA_PRESTAMO, RESPONSABLE_INTERNO_ID, ACTIVO_ID, OPERANTE) VALUES (%s, %s, %s, %s)"    
            for interno_id in lista_ids_interno:
                cursor.execute(insert_dispo_interno_query, (fecha_compra, interno_id, activo_id, 1))
        conn.commit()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        print("Inserción exitosa en las tablas ACTIVO y HERRAMIENTA O CONSUMIBLE.")

    except mysql.connector.Error as error:
        print("Error al insertar en las tablas ACTIVO y HERRAMIENTA O CONSUMIBLE:", error)

def insertar_dispoL(factura, serial, num_inventario, nombre,
                    autor, editorial, anio, edicion,
                     ubicacion, lista_ids_usuario, lista_ids_resguardo, lista_ids_interno, fecha_compra):
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Crear la consulta SQL para la inserción en la tabla ACTIVO
        insert_activo_query = "INSERT INTO ACTIVO (FACTURA, NUM_SERIAL, NUM_INVENTARIO, TIPO, NOMBRE, ESTADO, MODELO_ID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        # Definir los valores para la inserción en la tabla ACTIVO
        # el modelo simepre debe estar como N/A=id(76)
        values_activo = (factura, serial, num_inventario, "L", nombre, "ACTIVO", 76)
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
        insert_dispo_ubicacion_query = "INSERT INTO HISTORICO_ACTIVO_UBICACION(FECHA_CAMBIO, UBICACION_ID, ACTIVO_ID) VALUES (%s, %s, %s)"    
        cursor.execute(insert_dispo_ubicacion_query, (fecha_compra, ubicacion, activo_id))
        if lista_ids_usuario:
            insert_dispo_usuario_query = "INSERT INTO HISTORICO_ACTIVO_USUARIO(FECHA_PRESTAMO, USUARIO_FINAL_ID, ACTIVO_ID, OPERANTE) VALUES (%s, %s, %s, %s)"    
            for usuario_id in lista_ids_usuario:
                cursor.execute(insert_dispo_usuario_query, (fecha_compra, usuario_id, activo_id, 1))
        if lista_ids_resguardo:       
            insert_dispo_resguardo_query = "INSERT INTO HISTORICO_ACTIVO_RESPONSABLE(FECHA_CAMBIO_RESGUARDO, RESPONSABLE_RESGUARDO_ID, ACTIVO_ID, OPERANTE) VALUES (%s, %s, %s, %s)"    
            for resguardo_id in lista_ids_resguardo:
                cursor.execute(insert_dispo_resguardo_query, (fecha_compra, resguardo_id, activo_id, 1))
        if lista_ids_interno:
            insert_dispo_interno_query = "INSERT INTO HISTORICO_ACTIVO_RESPONSABLE_INTERNO(FECHA_PRESTAMO, RESPONSABLE_INTERNO_ID, ACTIVO_ID, OPERANTE) VALUES (%s, %s, %s, %s)"    
            for interno_id in lista_ids_interno:
                cursor.execute(insert_dispo_interno_query, (fecha_compra, interno_id, activo_id, 1))
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
        #cursor.execute("SELECT A.ACTIVO_ID, A.FACTURA, A.NUM_SERIAL, A.NUM_INVENTARIO, A.TIPO, A.NOMBRE, A.ESTADO,  A.USUARIO_FINAL_ID, (SELECT F.NOMBRE FROM USUARIO_FINAL F WHERE F.USUARIO_FINAL_ID = A.USUARIO_FINAL_ID) AS NOMBRE_USUARIO_FINAL, A.RESPONSABLE_INTERNO_ID, (SELECT I.NOMBRE FROM RESPONSABLE_INTERNO I WHERE I.RESPONSABLE_INTERNO_ID = A.RESPONSABLE_INTERNO_ID) AS NOMBRE_RESPONSABLE_INTERNO, (SELECT I.AP_PATERNO FROM RESPONSABLE_INTERNO I WHERE I.RESPONSABLE_INTERNO_ID = A.RESPONSABLE_INTERNO_ID) AS AP_PATERNO_RESPONSABLE_INTERNO, (SELECT I.AP_MATERNO FROM RESPONSABLE_INTERNO I WHERE I.RESPONSABLE_INTERNO_ID = A.RESPONSABLE_INTERNO_ID) AS AP_MATERNO_RESPONSABLE_INTERNO, A.RESPONSABLE_RESGUARDO_ID, (SELECT R.NOMBRE FROM RESPONSABLE_RESGUARDO R WHERE R.RESPONSABLE_RESGUARDO_ID = A.RESPONSABLE_RESGUARDO_ID) AS NOMBRE_RESPONSABLE_RESGUARDO, (SELECT R.AP_PATERNO FROM RESPONSABLE_RESGUARDO R WHERE R.RESPONSABLE_RESGUARDO_ID = A.RESPONSABLE_RESGUARDO_ID) AS AP_PATERNO_RESPONSABLE_RESGUARDO, (SELECT R.AP_MATERNO FROM RESPONSABLE_RESGUARDO R WHERE R.RESPONSABLE_RESGUARDO_ID = A.RESPONSABLE_RESGUARDO_ID) AS AP_MATERNO_RESPONSABLE_RESGUARDO, A.UBICACION_ID, (SELECT U.NOMBRE FROM UBICACION U WHERE U.UBICACION_ID = A.UBICACION_ID) AS NOMBRE_UBICACION, L.EDITORIAL, L.EDICION, L.ANIO, L.AUTOR FROM ACTIVO A JOIN LIBRO L ON A.ACTIVO_ID = L.ACTIVO_ID WHERE A.ESTADO <> 'BAJA';")
        cursor.execute("SELECT A.ACTIVO_ID, A.FACTURA, A.NUM_SERIAL, A.NUM_INVENTARIO, A.TIPO, A.NOMBRE, A.ESTADO, L.EDITORIAL, L.EDICION, L.ANIO, L.AUTOR FROM ACTIVO A JOIN LIBRO L ON A.ACTIVO_ID = L.ACTIVO_ID WHERE A.ESTADO <> 'BAJA'")
        # Obtiene los resultados de la consulta y los agrega a la lista de ubicaciones
        for libro in cursor.fetchall():
            activo_id = libro[0]
            factura = libro[1]
            num_serial = libro[2]
            num_inventario = libro[3]
            tipo = libro[4]
            nombre_activo = libro[5]
            estado = libro[6]
            #usuario_final_id = libro[7] #no ocupo este id, pues ocupo el nombre
            #nombre_usuario_final =libro[8]
            #responsable_interno_id = libro[9] #no ocupo este id, pues ocupo su nombre y apellidos
            #nombre_responsable_interno = libro[10]
            #APRI = libro[11]
            #AMRI = libro[12]
            #responsable_interno = nombre_responsable_interno + ' ' + APRI + ' ' + AMRI #CONCATENACION DE LOS 3 VALORES ANTERIORES
            #responsable_resguardo_id = libro[13]  #no ocupo este id, pues ocupo su nombre y apellidos
            #nombre_responsable_resguardo = libro[14]
            #APRR = libro[15]
            #AMRR = libro[16]
            #responsable_resguardo = nombre_responsable_resguardo + ' ' + APRR + ' ' + AMRR #CONCATENACION DE LOS 3 VALORES ANTERIORES
            #ubicacion_id = libro[17] #no ocupo este id, pues ocupo el nombre
            #nombre_ubicacion = libro[18]
            editorial = libro[7]
            edicion = libro[8]
            anio = libro[9]
            autor = libro[10]

            #ver si se pueden concatenar los atributos de los responsables
            
            libros.append((activo_id, factura, num_serial, num_inventario, tipo, nombre_activo, estado,
                           editorial, edicion, anio, autor))
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
        #delete_query = "DELETE FROM LIBRO WHERE ACTIVO_ID = %s" #esto elimina el registro
        delete_query = " UPDATE ACTIVO SET ESTADO = 'BAJA' WHERE ACTIVO_ID = %s"
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
        #cursor. execute(f"SELECT A.ACTIVO_ID, A.FACTURA, A.NUM_SERIAL, A.NUM_INVENTARIO, A.TIPO, A.NOMBRE AS NOMBRE_ACTIVO, A.ESTADO,L.EDITORIAL, L.EDICION, L.ANIO, L.AUTOR, A.USUARIO_FINAL_ID, A.RESPONSABLE_INTERNO_ID, A.RESPONSABLE_RESGUARDO_ID, A.UBICACION_ID FROM ACTIVO A INNER JOIN LIBRO L ON A.ACTIVO_ID = L.ACTIVO_ID WHERE A.ACTIVO_ID = {id_especifico}")
        cursor.execute(f"SELECT A.ACTIVO_ID, A.FACTURA, A.NUM_SERIAL, A.NUM_INVENTARIO, A.TIPO, A.NOMBRE AS NOMBRE_ACTIVO, A.ESTADO, L.EDITORIAL, L.EDICION, L.ANIO, L.AUTOR FROM ACTIVO A  INNER JOIN LIBRO L ON A.ACTIVO_ID = L.ACTIVO_ID  WHERE A.ACTIVO_ID = {id_especifico}")
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
            #usuario_final = libro[11]#
            #responsable_interno = libro[12]#
            #responsable_resguardo = libro[13]#
            #ubicacion = libro[14]#
            libros.append((activo_id, factura, num_serial, num_inventario, tipo, nombre_activo, estado, editorial, edicion, anio, autor))
        
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener los libros:", e)
    return libros


def modificar_dispoL(id_activo, factura, serial, num_inventario, nombre, estado,
                    autor, editorial, anio, edicion):
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Crear la consulta SQL para la modificacion en la tabla ACTIVO
        update_activo_query = " UPDATE ACTIVO SET FACTURA = %s, NUM_SERIAL = %s, NUM_INVENTARIO = %s, NOMBRE = %s, ESTADO = %s WHERE ACTIVO_ID = %s"
        # Definir los valores para la modificacion en la tabla ACTIVO
        # el modelo simepre debe estar como N/A=id(76)
        #values_activo = (factura, serial, num_inventario, nombre, estado, usuario, interno, resguardo, ubicacion, id_activo)# ya no se ocupa porque se quitaron unos atributos
        values_activo = (factura, serial, num_inventario, nombre, estado, id_activo)
        # Ejecutar la consulta de inserción en la tabla ACTIVO
        cursor.execute(update_activo_query, values_activo)
        # Crear la consulta SQL para la inserción en la tabla DISPO_INTELIGENTE
        update_libro_query = "UPDATE LIBRO SET EDITORIAL = %s, EDICION = %s, ANIO = %s, AUTOR = %s WHERE ACTIVO_ID = %s"
        # Definir los valores para la inserción en la tabla DISPO_INTELIGENTE
        values_libro = ( editorial, edicion, anio, autor, id_activo)
        # Ejecutar la consulta de inserción en la tabla DISPO_INTELIGENTE
        cursor.execute(update_libro_query, values_libro)
        # Confirmar las inserciones en la base de datos
        conn.commit()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        print("Modificación exitosa en la tabla LIBRO.")
    except mysql.connector.Error as error:
        print("Error al modificar en la tabla LIBRO:", error)

def obtener_herramientas():
    herramientas = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Ejecuta la consulta para obtener los atributos de la tabla LIBRO con información de ACTIVO
        #cursor.execute("SELECT A.ACTIVO_ID, A.FACTURA, A.NUM_SERIAL, A.NUM_INVENTARIO, A.TIPO, A.NOMBRE, A.ESTADO,  A.USUARIO_FINAL_ID, (SELECT F.NOMBRE FROM USUARIO_FINAL F WHERE F.USUARIO_FINAL_ID = A.USUARIO_FINAL_ID) AS NOMBRE_USUARIO_FINAL, A.RESPONSABLE_INTERNO_ID, (SELECT I.NOMBRE FROM RESPONSABLE_INTERNO I WHERE I.RESPONSABLE_INTERNO_ID = A.RESPONSABLE_INTERNO_ID) AS NOMBRE_RESPONSABLE_INTERNO, (SELECT I.AP_PATERNO FROM RESPONSABLE_INTERNO I WHERE I.RESPONSABLE_INTERNO_ID = A.RESPONSABLE_INTERNO_ID) AS AP_PATERNO_RESPONSABLE_INTERNO, (SELECT I.AP_MATERNO FROM RESPONSABLE_INTERNO I WHERE I.RESPONSABLE_INTERNO_ID = A.RESPONSABLE_INTERNO_ID) AS AP_MATERNO_RESPONSABLE_INTERNO, A.RESPONSABLE_RESGUARDO_ID, (SELECT R.NOMBRE FROM RESPONSABLE_RESGUARDO R WHERE R.RESPONSABLE_RESGUARDO_ID = A.RESPONSABLE_RESGUARDO_ID) AS NOMBRE_RESPONSABLE_RESGUARDO, (SELECT R.AP_PATERNO FROM RESPONSABLE_RESGUARDO R WHERE R.RESPONSABLE_RESGUARDO_ID = A.RESPONSABLE_RESGUARDO_ID) AS AP_PATERNO_RESPONSABLE_RESGUARDO, (SELECT R.AP_MATERNO FROM RESPONSABLE_RESGUARDO R WHERE R.RESPONSABLE_RESGUARDO_ID = A.RESPONSABLE_RESGUARDO_ID) AS AP_MATERNO_RESPONSABLE_RESGUARDO, A.UBICACION_ID, (SELECT U.NOMBRE FROM UBICACION U WHERE U.UBICACION_ID = A.UBICACION_ID) AS NOMBRE_UBICACION, L.EDITORIAL, L.EDICION, L.ANIO, L.AUTOR FROM ACTIVO A JOIN LIBRO L ON A.ACTIVO_ID = L.ACTIVO_ID WHERE A.ESTADO <> 'BAJA';")
        #cursor.execute("SELECT A.ACTIVO_ID, A.FACTURA, A.NUM_SERIAL, A.NUM_INVENTARIO, A.TIPO, A.NOMBRE, A.ESTADO,  A.MODELO_ID, (SELECT M.NOMBRE FROM MODELO M WHERE M.MODELO_ID = A.MODELO_ID) AS NOMBRE_MODELO, A.USUARIO_FINAL_ID, (SELECT F.NOMBRE FROM USUARIO_FINAL F WHERE F.USUARIO_FINAL_ID = A.USUARIO_FINAL_ID) AS NOMBRE_USUARIO_FINAL, A.RESPONSABLE_INTERNO_ID, (SELECT I.NOMBRE FROM RESPONSABLE_INTERNO I WHERE I.RESPONSABLE_INTERNO_ID = A.RESPONSABLE_INTERNO_ID) AS NOMBRE_RESPONSABLE_INTERNO, (SELECT I.AP_PATERNO FROM RESPONSABLE_INTERNO I WHERE I.RESPONSABLE_INTERNO_ID = A.RESPONSABLE_INTERNO_ID) AS AP_PATERNO_RESPONSABLE_INTERNO, (SELECT I.AP_MATERNO FROM RESPONSABLE_INTERNO I WHERE I.RESPONSABLE_INTERNO_ID = A.RESPONSABLE_INTERNO_ID) AS AP_MATERNO_RESPONSABLE_INTERNO, A.RESPONSABLE_RESGUARDO_ID, (SELECT R.NOMBRE FROM RESPONSABLE_RESGUARDO R WHERE R.RESPONSABLE_RESGUARDO_ID = A.RESPONSABLE_RESGUARDO_ID) AS NOMBRE_RESPONSABLE_RESGUARDO, (SELECT R.AP_PATERNO FROM RESPONSABLE_RESGUARDO R WHERE R.RESPONSABLE_RESGUARDO_ID = A.RESPONSABLE_RESGUARDO_ID) AS AP_PATERNO_RESPONSABLE_RESGUARDO, (SELECT R.AP_MATERNO FROM RESPONSABLE_RESGUARDO R WHERE R.RESPONSABLE_RESGUARDO_ID = A.RESPONSABLE_RESGUARDO_ID) AS AP_MATERNO_RESPONSABLE_RESGUARDO, A.UBICACION_ID, (SELECT U.NOMBRE FROM UBICACION U WHERE U.UBICACION_ID = A.UBICACION_ID) AS NOMBRE_UBICACION, HC.FECHA_COMPRA, HC.FECHA_CONSUMO, HC.CANTIDAD, HC.CONTENIDO, HC.DESCRIPCION FROM ACTIVO A JOIN HERRAMIENTA_CONSUMIBLE HC ON A.ACTIVO_ID = HC.ACTIVO_ID WHERE A.ESTADO <> 'BAJA' ")
        cursor.execute("SELECT A.ACTIVO_ID, A.FACTURA, A.NUM_SERIAL, A.NUM_INVENTARIO, A.TIPO, A.NOMBRE, A.ESTADO,  A.MODELO_ID, (SELECT M.NOMBRE FROM MODELO M WHERE M.MODELO_ID = A.MODELO_ID) AS NOMBRE_MODELO, HC.FECHA_COMPRA, HC.FECHA_CONSUMO, HC.CANTIDAD, HC.CONTENIDO, HC.DESCRIPCION FROM ACTIVO A JOIN HERRAMIENTA_CONSUMIBLE HC ON A.ACTIVO_ID = HC.ACTIVO_ID WHERE A.ESTADO <> 'BAJA'")
        # Obtiene los resultados de la consulta y los agrega a la lista de ubicaciones
        for herramienta in cursor.fetchall():
            activo_id = herramienta[0]
            factura = herramienta[1]
            num_serial = herramienta[2]
            num_inventario = herramienta[3]
            tipo = herramienta[4]
            nombre_activo = herramienta[5]
            estado = herramienta[6]
            modelo_id = herramienta[7] #no ocupo este id, solo el nombre
            modelo = herramienta[8]
            #usuario_final_id = herramienta[9] #no ocupo este id, pues ocupo el nombre
            #nombre_usuario_final =herramienta[10]
            #responsable_interno_id = herramienta[11] #no ocupo este id, pues ocupo su nombre y apellidos
            #nombre_responsable_interno = herramienta[12]
            #APRI = herramienta[13]
            #AMRI = herramienta[14]
            #responsable_interno = nombre_responsable_interno + ' ' + APRI + ' ' + AMRI #CONCATENACION DE LOS 3 VALORES ANTERIORES
            #responsable_resguardo_id = herramienta[15]  #no ocupo este id, pues ocupo su nombre y apellidos
            #nombre_responsable_resguardo = herramienta[16]
            #APRR = herramienta[17]
            #AMRR = herramienta[18]
            #responsable_resguardo = nombre_responsable_resguardo + ' ' + APRR + ' ' + AMRR #CONCATENACION DE LOS 3 VALORES ANTERIORES
            #ubicacion_id = herramienta[19] #no ocupo este id, pues ocupo el nombre
            #nombre_ubicacion = herramienta[20]
            fecha_compra = herramienta[9]
            fecha_consumo = herramienta[10]
            cantidad = herramienta[11]
            Contenido = herramienta[12]
            descripcion = herramienta[13]
            #ver si se pueden concatenar los atributos de los responsables
            herramientas.append((activo_id, factura, num_serial, num_inventario, tipo, nombre_activo, estado,
                        modelo, fecha_compra, fecha_consumo, cantidad, Contenido, descripcion))
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener los libros:", e)
    return herramientas

def eliminar_herramientas(herramienta_id):
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Sentencia SQL para eliminar el libro con el libro_id proporcionado
        #delete_query = "DELETE FROM LIBRO WHERE ACTIVO_ID = %s" #esto elimina el registro
        delete_query = " UPDATE ACTIVO SET ESTADO = 'BAJA' WHERE ACTIVO_ID = %s"
        # Ejecuta la eliminación con el libro_id proporcionado
        cursor.execute(delete_query, (herramienta_id,))
        # Confirma los cambios en la base de datos
        conn.commit()
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al eliminar la herramienta:", e)
        # Maneja el error adecuadamente (puedes levantar una excepción o imprimir un mensaje)


def obtener_herramientaID(id_especifico):
    herramientas = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta con el filtro para el ID específico
        #cursor.execute(f"SELECT A.ACTIVO_ID, A.FACTURA, A.NUM_SERIAL, A.NUM_INVENTARIO, A.TIPO, A.NOMBRE AS NOMBRE_ACTIVO, A.ESTADO, HC.FECHA_COMPRA, HC.FECHA_CONSUMO, HC.CANTIDAD, HC.CONTENIDO, HC.DESCRIPCION, A.USUARIO_FINAL_ID, A.RESPONSABLE_INTERNO_ID, A.RESPONSABLE_RESGUARDO_ID, A.UBICACION_ID, A.MODELO_ID FROM ACTIVO A INNER JOIN HERRAMIENTA_CONSUMIBLE HC ON A.ACTIVO_ID = HC.ACTIVO_ID WHERE A.ACTIVO_ID = {id_especifico}")
        cursor.execute(f"SELECT A.ACTIVO_ID, A.FACTURA, A.NUM_SERIAL, A.NUM_INVENTARIO, A.TIPO, A.NOMBRE AS NOMBRE_ACTIVO, A.ESTADO, HC.FECHA_COMPRA, HC.FECHA_CONSUMO, HC.CANTIDAD, HC.CONTENIDO, HC.DESCRIPCION, A.MODELO_ID FROM ACTIVO A  INNER JOIN HERRAMIENTA_CONSUMIBLE HC ON A.ACTIVO_ID = HC.ACTIVO_ID WHERE A.ACTIVO_ID = {id_especifico}")
        # Obtiene los resultados de la consulta y los agrega a la lista de libros
        for herramienta in cursor.fetchall():
            activo_id = herramienta[0] #no se debe mostrar para cambiar
            factura = herramienta[1]#
            num_serial = herramienta[2]#
            num_inventario = herramienta[3]#
            tipo = herramienta[4] #no se debe mostrar para cambiar
            nombre_activo = herramienta[5]#
            estado = herramienta[6]#
            fecha_compra = herramienta[7]#
            fecha_consumo = herramienta[8]#
            cantidad = herramienta[9]#
            contenido = herramienta[10]#
            descripcion = herramienta[11]#
            # Agrega los atributos de usuario final, responsable interno, responsable resguardo y ubicación si es necesario
            #usuario_final = herramienta[12]#
            #responsable_interno = herramienta[13]#
            #responsable_resguardo = herramienta[14]#
            #ubicacion = herramienta[15]#
            modelo = herramienta[12]#
            herramientas.append((activo_id, factura, num_serial, num_inventario, tipo, nombre_activo, estado, fecha_compra, fecha_consumo, cantidad, contenido, descripcion,  modelo))
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener las herramientas:", e)
    return herramientas

def modificar_dispoH(id_activo, factura, serial, num_inventario, nombre, estado, modelo,
                    fecha_compra, fecha_consumo, cantidad, contenido, descripcion):
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Crear la consulta SQL para la modificacion en la tabla ACTIVO
        update_activo_query = " UPDATE ACTIVO SET FACTURA = %s, NUM_SERIAL = %s, NUM_INVENTARIO = %s, NOMBRE = %s, ESTADO = %s, MODELO_ID = %s WHERE ACTIVO_ID = %s"
        # Definir los valores para la modificacion en la tabla ACTIVO
        # el modelo simepre debe estar como N/A=id(76)
        values_activo = (factura, serial, num_inventario, nombre, estado, modelo, id_activo)
        # Ejecutar la consulta de inserción en la tabla ACTIVO
        cursor.execute(update_activo_query, values_activo)
        # Crear la consulta SQL para la inserción en la tabla DISPO_INTELIGENTE
        update_herr_query = "UPDATE HERRAMIENTA_CONSUMIBLE SET FECHA_COMPRA = %s, FECHA_CONSUMO = %s, CANTIDAD = %s, CONTENIDO = %s, DESCRIPCION = %s WHERE ACTIVO_ID = %s"
        # Definir los valores para la inserción en la tabla DISPO_INTELIGENTE
        values_herramienta = ( fecha_compra, fecha_consumo, cantidad, contenido, descripcion, id_activo)
        # Ejecutar la consulta de inserción en la tabla DISPO_INTELIGENTE
        cursor.execute(update_herr_query, values_herramienta)
        # Confirmar las inserciones en la base de datos
        conn.commit()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        print("Modificación exitosa en la tabla HERRAMIENTA_CONSUMIBLE.")
    except mysql.connector.Error as error:
        print("Error al modificar en la tabla HERRAMIENTA_CONSUMIBLE:", error)

def obtener_dispos():
    dispos = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Ejecuta la consulta para obtener los atributos de la tabla LIBRO con información de ACTIVO
        #cursor.execute("SELECT A.ACTIVO_ID, A.FACTURA, A.NUM_SERIAL, A.NUM_INVENTARIO, A.TIPO, A.NOMBRE AS NOMBRE_ACTIVO, A.ESTADO, A.MODELO_ID, (SELECT M.NOMBRE FROM MODELO M WHERE M.MODELO_ID = A.MODELO_ID) AS NOMBRE_MODELO, DI.CARACTERISTICAS, DI.NUM_PROCESADORES, DI.RAM_INSTALADA, DI.RAM_MAX,  DI.SUBTIPO_ID, (SELECT S.NOMBRE FROM SUBTIPO S WHERE S.SUBTIPO_ID = DI.SUBTIPO_ID) AS NOMBRE_SUBTIPO, FROM ACTIVO A JOIN DISPO_INTELIIGENTE DI ON A.ACTIVO_ID = HC.ACTIVO_ID WHERE A.ESTADO <> 'BAJA';")
        #cursor.execute("SELECT A.ACTIVO_ID, A.FACTURA, A.NUM_SERIAL, A.NUM_INVENTARIO, A.TIPO, A.NOMBRE AS NOMBRE_ACTIVO, A.ESTADO, A.MODELO_ID, (SELECT M.NOMBRE FROM MODELO M WHERE M.MODELO_ID = A.MODELO_ID) AS NOMBRE_MODELO, DI.CARACTERISTICAS, DI.NUM_PROCESADORES, DI.RAM_INSTALADA, DI.RAM_MAX,  DI.SUBTIPO_ID, (SELECT S.NOMBRE FROM SUBTIPO S WHERE S.SUBTIPO_ID = DI.SUBTIPO_ID) AS NOMBRE_SUBTIPO FROM ACTIVO A JOIN DISPO_INTELIIGENTE DI ON A.ACTIVO_ID = DI.ACTIVO_ID WHERE A.ESTADO <> 'BAJA';")
        cursor.execute("SELECT A.ACTIVO_ID, A.FACTURA, A.NUM_SERIAL, A.NUM_INVENTARIO, A.TIPO, A.NOMBRE AS NOMBRE_ACTIVO, A.ESTADO,  A.MODELO_ID, (SELECT M.NOMBRE FROM MODELO M WHERE M.MODELO_ID = A.MODELO_ID) AS NOMBRE_MODELO, DI.CARACTERISTICAS, DI.NUM_PROCESADORES, DI.RAM_INSTALADA, DI.RAM_MAX,  DI.SUBTIPO_ID, (SELECT S.NOMBRE FROM SUBTIPO S WHERE S.SUBTIPO_ID = DI.SUBTIPO_ID) AS NOMBRE_SUBTIPO FROM ACTIVO A JOIN DISPO_INTELIIGENTE DI ON A.ACTIVO_ID = DI.ACTIVO_ID WHERE A.ESTADO <> 'BAJA';")
        # Obtiene los resultados de la consulta y los agrega a la lista de ubicaciones
        for dispo in cursor.fetchall():
            activo_id = dispo[0]
            factura = dispo[1]
            num_serial = dispo[2]
            num_inventario = dispo[3]
            tipo = dispo[4]
            nombre_activo = dispo[5]
            estado = dispo[6]
            modelo_id = dispo[7] #no ocupo este id, solo el nombre
            modelo = dispo[8]
            caracteristicas = dispo[9]
            num_procesadores = dispo[10]
            ram_instalada = dispo[11]
            ram_maxima = dispo[12]
            subtipo_id = dispo[13]#no ocupo este id, pues ocupo el nombre
            subtipo = dispo[14]
            #ver si se pueden concatenar los atributos de los responsables
            dispos.append((activo_id, factura, num_serial, num_inventario, tipo, nombre_activo, estado,
                        modelo, caracteristicas, num_procesadores, ram_instalada, ram_maxima, subtipo))
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener los dispositivos:", e)
    return dispos

def eliminar_dispos(dispo_id):
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Sentencia SQL para eliminar el libro con el libro_id proporcionado
        #delete_query = "DELETE FROM LIBRO WHERE ACTIVO_ID = %s" #esto elimina el registro
        delete_query = " UPDATE ACTIVO SET ESTADO = 'BAJA' WHERE ACTIVO_ID = %s"
        # Ejecuta la eliminación con el libro_id proporcionado
        cursor.execute(delete_query, (dispo_id,))
        # Confirma los cambios en la base de datos
        conn.commit()
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al eliminar el dispositivo:", e)
        # Maneja el error adecuadamente (puedes levantar una excepción o imprimir un mensaje)

def obtener_dispoID(id_especifico):
    dispos = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecuta la consulta con el filtro para el ID específico
        #cursor. execute(f"SELECT A.ACTIVO_ID, A.FACTURA, A.NUM_SERIAL, A.NUM_INVENTARIO, A.TIPO, A.NOMBRE AS NOMBRE_ACTIVO, A.ESTADO,  DI.CARACTERISTICAS, DI.NUM_PROCESADORES, DI.RAM_INSTALADA, DI.RAM_MAX, DI.SUBTIPO_ID FROM ACTIVO A INNER JOIN DISPO_INTELIIGENTE DI ON A.ACTIVO_ID = DI.ACTIVO_ID WHERE A.ACTIVO_ID = {id_especifico}")
        cursor.execute(f"SELECT A.ACTIVO_ID, A.FACTURA, A.NUM_SERIAL, A.NUM_INVENTARIO, A.TIPO, A.NOMBRE AS NOMBRE_ACTIVO, A.ESTADO,  A.MODELO_ID, DI.CARACTERISTICAS, DI.NUM_PROCESADORES, DI.RAM_INSTALADA, DI.RAM_MAX, DI.SUBTIPO_ID FROM ACTIVO A INNER JOIN DISPO_INTELIIGENTE DI ON A.ACTIVO_ID = DI.ACTIVO_ID WHERE A.ACTIVO_ID = {id_especifico};")
        # Obtiene los resultados de la consulta y los agrega a la lista de libros
        for dispo in cursor.fetchall():
            activo_id = dispo[0] #no se debe mostrar para cambiar
            factura = dispo[1]
            num_serial = dispo[2]
            num_inventario = dispo[3]
            tipo = dispo[4] #no se debe mostrar para cambiar
            nombre_activo = dispo[5]
            estado = dispo[6]
            modelo = dispo[7]
            caracteristicas = dispo[8]
            num_procesadores = dispo[9]
            ram_instalada = dispo[10]
            ram_maxima = dispo[11]
            subtipo =  dispo[12]
            dispos.append((activo_id, factura, num_serial, num_inventario, tipo, nombre_activo, estado, modelo,
                           caracteristicas, num_procesadores, ram_instalada, ram_maxima, subtipo))
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener los dispos:", e)
    return dispos

def modificar_dispoD(id_activo, factura, serial, num_inventario, nombre, estado, modelo,
                    caracteristicas, num_procesadores, ram_instalada, ram_maxima, subtipo):
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Crear la consulta SQL para la modificacion en la tabla ACTIVO
        update_activo_query = " UPDATE ACTIVO SET FACTURA = %s, NUM_SERIAL = %s, NUM_INVENTARIO = %s, NOMBRE = %s, ESTADO = %s, MODELO_ID = %s WHERE ACTIVO_ID = %s"
        # Definir los valores para la modificacion en la tabla ACTIVO
        # el modelo simepre debe estar como N/A=id(76)
        values_activo = (factura, serial, num_inventario, nombre, estado, modelo, id_activo)
        # Ejecutar la consulta de inserción en la tabla ACTIVO
        cursor.execute(update_activo_query, values_activo)
        # Crear la consulta SQL para la inserción en la tabla DISPO_INTELIGENTE
        update_dispo_query = "UPDATE DISPO_INTELIIGENTE SET CARACTERISTICAS = %s, NUM_PROCESADORES = %s, RAM_INSTALADA = %s, RAM_MAX = %s, SUBTIPO_ID = %s WHERE ACTIVO_ID = %s"
        # Definir los valores para la inserción en la tabla DISPO_INTELIGENTE
        values_dispo = ( caracteristicas, num_procesadores, ram_instalada, ram_maxima, subtipo, id_activo)
        # Ejecutar la consulta de inserción en la tabla DISPO_INTELIGENTE
        cursor.execute(update_dispo_query, values_dispo)
        # Confirmar las inserciones en la base de datos
        conn.commit()
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        print("Modificación exitosa en la tabla DISPO_INTELIGENTE.")
    except mysql.connector.Error as error:
        print("Error al modificar en la tabla DISPO_INTELIGENTE:", error)


def obtener_edificio():
    edificios = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Ejecuta la consulta para obtener los atributos de la tabla USUARIO_FINAL
        cursor.execute("SELECT EDIFICIO_ID, NOMBRE FROM EDIFICIO ORDER BY NOMBRE")
        # Obtiene los resultados de la consulta y los agrega a la lista de usuarios finales
        for edificio in cursor.fetchall():
            edificio_id = edificio[0]
            nombre = edificio[1]
            edificios.append((edificio_id, nombre))
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener los edificios:", e)
    return edificios

def obtener_titulo():
    titulos = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Ejecuta la consulta para obtener los atributos de la tabla USUARIO_FINAL
        cursor.execute("SELECT TITULO_ID, NOMBRE, ABREVIATURA FROM TITULO ORDER BY NOMBRE")
        # Obtiene los resultados de la consulta y los agrega a la lista de usuarios finales
        for titulo in cursor.fetchall():
           titulo_id = titulo[0]
           nombre = titulo[1]
           abreviatura = titulo[2]
           titulos.append((titulo_id, nombre, abreviatura))
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener los titulos:", e)
    return titulos

def obtener_division():
    divisiones = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Ejecuta la consulta para obtener los atributos de la tabla USUARIO_FINAL
        cursor.execute("SELECT DIVISION_ID, ACRONIMO, NOMBRE FROM DIVISION ORDER BY NOMBRE")
        # Obtiene los resultados de la consulta y los agrega a la lista de usuarios finales
        for division in cursor.fetchall():
           division_id = division[0]
           acronimo = division[1]
           nombre = division[2]
           divisiones.append((division_id, acronimo, nombre))
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener los titulos:", e)
    return divisiones

def obtener_perfil():
    perfiles = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Ejecuta la consulta para obtener los atributos de la tabla USUARIO_FINAL
        cursor.execute("SELECT PERFIL_USUARIO_ID, PERFIL_USUARIO_NOMBRE FROM PERFIL ORDER BY PERFIL_USUARIO_NOMBRE")
        # Obtiene los resultados de la consulta y los agrega a la lista de usuarios finales
        for perfil in cursor.fetchall():
           perfil_id = perfil[0]
           nombre = perfil[1]
           perfiles.append((perfil_id, nombre))
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener los titulos:", e)
    return perfiles

def obtener_sector():
    sectores = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Ejecuta la consulta para obtener los atributos de la tabla USUARIO_FINAL
        cursor.execute("SELECT SECTOR_ID, NOMBRE FROM SECTOR ORDER BY NOMBRE")
        # Obtiene los resultados de la consulta y los agrega a la lista de usuarios finales
        for sector in cursor.fetchall():
           sector_id = sector[0]
           nombre = sector[1]
           sectores.append((sector_id, nombre))
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener los sectores:", e)
    return sectores

def obtener_marca():
    marcas = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Ejecuta la consulta para obtener los atributos de la tabla USUARIO_FINAL
        cursor.execute("SELECT MARCA_ID, NOMBRE FROM MARCA ORDER BY NOMBRE")
        # Obtiene los resultados de la consulta y los agrega a la lista de usuarios finales
        for marca in cursor.fetchall():
           marca_id = marca[0]
           nombre = marca[1]
           marcas.append((marca_id, nombre))
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener las marcas:", e)
    return marcas

def obtener_micro():
    micro = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Ejecuta la consulta para obtener los atributos de la tabla USUARIO_FINAL
        cursor.execute("SELECT MICRO.MICROPROCESADOR_ID, MICRO.NOMBRE, MICRO.ARQUITECTURA, MICRO.GENERACION, MAR.NOMBRE FROM MICROPROCESADOR MICRO JOIN MARCA MAR ON MICRO.MARCA_ID = MAR.MARCA_ID")
        micro= cursor.fetchall()
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener las marcas:", e)
    return micro

def busqueda_dispos():
    dispos = []
    try:
        # Realiza la conexión a la base de datos (puedes definir db_config aquí o importarlo desde app.py)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Ejecuta la consulta para obtener los atributos de la tabla ACTIVO, MODELO, DISPO_INTELIIGENTE y SUBTIPO,
        # y los RAM_ID, SISTEMA_OPERATIVO_ID y TARGETA_GARFICA_ID concatenados
        cursor.execute("""
            SELECT A.FACTURA, A.NUM_SERIAL, A.NUM_INVENTARIO, A.NOMBRE AS ACTIVO_NOMBRE, A.ESTADO, M.NOMBRE AS MODELO_NOMBRE, 
                DI.CARACTERISTICAS, DI.NUM_PROCESADORES, DI.RAM_INSTALADA, DI.RAM_MAX, S.NOMBRE AS SUBTIPO_NOMBRE,
                GROUP_CONCAT(DISTINCT DR.RAM_ID) AS RAM_ID_CONCAT,
                GROUP_CONCAT(DISTINCT DSO.SISTEMA_OPERATIVO_ID) AS SO_ID_CONCAT,
                GROUP_CONCAT(DISTINCT DV.TARGETA_GARFICA_ID) AS VIDEO_ID_CONCAT
            FROM ACTIVO A 
            JOIN MODELO M ON A.MODELO_ID = M.MODELO_ID 
            JOIN DISPO_INTELIIGENTE DI ON A.ACTIVO_ID = DI.ACTIVO_ID 
            JOIN SUBTIPO S ON DI.SUBTIPO_ID = S.SUBTIPO_ID 
            LEFT JOIN DISPO_RAM DR ON A.ACTIVO_ID = DR.ACTIVO_ID AND DR.OPERANTE = 1
            LEFT JOIN DISPO_SO DSO ON A.ACTIVO_ID = DSO.ACTIVO_ID AND DSO.OPERANTE = 1
            LEFT JOIN DISPO_VIDEO DV ON A.ACTIVO_ID = DV.ACTIVO_ID AND DV.OPERANTE = 1
            WHERE A.TIPO = 'I'
            GROUP BY A.ACTIVO_ID
        """)
        dispos = cursor.fetchall()  # Obtener todos los resultados de la consulta
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener los dispositivos:", e)
    return dispos



def consulta_ram(ram_id):
    ram_info = ""
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT RAM.MARCA, RAM.NUM_SERIE, RAM.CAPACIDAD, TIPO_RAM.NOMBRE AS TIPO_RAM_NOMBRE FROM RAM JOIN TIPO_RAM ON RAM.TIPO_RAM_ID = TIPO_RAM.TIPO_RAM_ID WHERE RAM.RAM_ID = %s", (ram_id,))
        ram_data = cursor.fetchone()  # Obtener el resultado de la consulta como un diccionario
        
        if ram_data:
            ram_info = f"{ram_data['MARCA']} {ram_data['NUM_SERIE']} {ram_data['CAPACIDAD']}GiB {ram_data['TIPO_RAM_NOMBRE']}\n"
        
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener información de RAM:", e)
    return ram_info

def consulta_so(so_id):
    so_info = ""
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT TIPO.NOMBRE, SO.NUM_VERSION, SO.ARQUITECTURA FROM SISTEMA_OPERATIVO SO JOIN TIPO_SO TIPO ON SO.TIPO_SO_ID = TIPO.TIPO_SO_ID WHERE SO.SISTEMA_OPERATIVO_ID = %s", (so_id,))
        so_data = cursor.fetchone()  # Obtener el resultado de la consulta como un diccionario
        
        if so_data:
            so_info = f"{so_data['NOMBRE']} {so_data['NUM_VERSION']}, {so_data['ARQUITECTURA']}\n"
        
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener información de SISTEMA OPERATIVO:", e)
    return so_info

def consulta_video(video_id):
    video_info = ""
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT TAR.TARGETA_GRAFICA_MARCA, TAR.TARGETA_GRAFICA_MODELO, TIPO.TIPO_TARGETA_GRAFICA_NOMBRE, PCI.TIPO_PCI_NOMBRE FROM TARGETA_GRAFICA TAR JOIN TIPO_TARGETA_GRAFICA TIPO ON TAR.TIPO_TARGETA_GRAFICA_ID = TIPO.TIPO_TARGETA_GRAFICA_ID JOIN TIPO_PCI PCI ON TAR.TIPO_PCI_ID = PCI.TIPO_PCI_ID WHERE TAR.TARGETA_GARFICA_ID = %s", (video_id,))
        video_data = cursor.fetchone()  # Obtener el resultado de la consulta como un diccionario
        
        if video_data:
            video_info = f"{video_data['TARGETA_GRAFICA_MARCA']} {video_data['TARGETA_GRAFICA_MODELO']} {video_data['TIPO_TARGETA_GRAFICA_NOMBRE']} {video_data['TIPO_PCI_NOMBRE']}\n"
        
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener información de video:", e)
    return video_info

def consulta_puerto(video_id):
    video_info = ""
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT TAR.TARGETA_GRAFICA_MARCA, TAR.TARGETA_GRAFICA_MODELO, TIPO.TIPO_TARGETA_GRAFICA_NOMBRE, PCI.TIPO_PCI_NOMBRE FROM TARGETA_GRAFICA TAR JOIN TIPO_TARGETA_GRAFICA TIPO ON TAR.TIPO_TARGETA_GRAFICA_ID = TIPO.TIPO_TARGETA_GRAFICA_ID JOIN TIPO_PCI PCI ON TAR.TIPO_PCI_ID = PCI.TIPO_PCI_ID WHERE TAR.TARGETA_GARFICA_ID = %s", (video_id,))
        video_data = cursor.fetchone()  # Obtener el resultado de la consulta como un diccionario
        
        if video_data:
            video_info = f"{video_data['TARGETA_GRAFICA_MARCA']} {video_data['TARGETA_GRAFICA_MODELO']} {video_data['TIPO_TARGETA_GRAFICA_NOMBRE']} {video_data['TIPO_PCI_NOMBRE']}\n"
        
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print("Error al obtener información de video:", e)
    return video_info


