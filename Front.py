import mysql.connector
from database import *
from flask import Flask, render_template, request, redirect, url_for, session
from flask import g
from collections import defaultdict
import re
import datetime

app = Flask(__name__)

# Configuración para la sesión. Se necesita una clave secreta para firmar las cookies.
app.secret_key = 'mi_clave_secreta'


# Simulación de usuarios y contraseñas (reemplaza esto con una base de datos en un entorno de producción)
users = {
    'admin': 'admin',
    'david': 'david',
    'salac': 'fraqfrnhe3r4'
}

@app.route('/')
def index():
    return render_template('login.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            # Inicio de sesión exitoso, almacenamos el estado de inicio de sesión en la sesión del usuario.
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('menuP'))
        else:
            return 'Credenciales inválidas. Por favor, vuelve a intentarlo.'
    else:
        return render_template('login.html')
    
@app.route('/menuP')
def menuP():
    # Comprobamos si el usuario está logeado. Si no, lo redirigimos al inicio de sesión.
    if 'logged_in' in session and session['logged_in']:
        # El usuario está logeado, renderizamos la página con el menú.
        return render_template('MenuPrincipal.html')
    else:
        return redirect(url_for('logout'))
    
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # Cerramos la sesión del usuario limpiando los datos de la sesión.
    session.clear()
    return redirect(url_for('login'))

@app.route('/activos')
def activos():
    # Comprobamos si el usuario está logeado. Si no, lo redirigimos al inicio de sesión.
    if 'logged_in' in session and session['logged_in']:
        # El usuario está logeado, renderizamos la página con la acción "Marca".
        return render_template('MActivosPrincipal.html')
    else:
        return redirect(url_for('logout'))
    
@app.route('/activos/dispos')
def dispos():
    # Comprobamos si el usuario está logeado. Si no, lo redirigimos al inicio de sesión.
    if 'logged_in' in session and session['logged_in']:
        # El usuario está logeado, renderizamos la página con la acción "Marca".
        return render_template('MDispos.html')
    else:
        return redirect(url_for('logout'))
    
@app.route('/activos/dispos/agregar')
def ADispos():
    # Comprobamos si el usuario está logeado. Si no, lo redirigimos al inicio de sesión.
    if 'logged_in' in session and session['logged_in']:
        # El usuario está logeado, renderizamos la página con la acción "Marca".
        nombres_ram = obtener_info_ram()
        nombres_ubicacion = obtener_ubicaciones()
        nombres_so = obtener_info_sistema_operativo()
        nombres_subtipo = obtener_nombres_subtipo()
        nombres_resguardo = obtener_responsables_resguardo()
        nombres_interno = obtener_responsables_interno()
        nombres_usuarios = obtener_usuarios_finales()
        nombres_modelo = obtener_info_modelo()
        nombres_almacenamiento = obtener_info_almacenamiento()
        nombres_micro = obtener_info_micro()
        nombres_tarjeta = obtener_info_tarjeta()
        nombres_puerto = obtener_nombres_puerto()
        nombres_lectora = obtener_info_lectora()
        nombres_red = obtener_info_red()
        return render_template('ADispos.html', nombres_ubicacion=nombres_ubicacion, nombres_so=nombres_so, 
                               nombres_subtipo=nombres_subtipo, nombres_modelo=nombres_modelo, nombres_ram=nombres_ram,  
                                nombres_resguardo= nombres_resguardo, nombres_interno=nombres_interno, 
                                nombres_almacenamiento=nombres_almacenamiento, nombres_usuarios=nombres_usuarios, nombres_micro=nombres_micro,
                                nombres_tarjeta=nombres_tarjeta, nombres_puerto=nombres_puerto, nombres_lectora=nombres_lectora, nombres_red=nombres_red)
    else:
        return redirect(url_for('logout'))
    
@app.route('/agregar_dispositivo', methods=['POST'])
def agregar_dispositivo():
    # Obtener los datos del formulario
    factura = request.form.get('factura')
    serial = request.form.get('serial').upper()
    num_inventario = request.form.get('num_inventario')
    subtipo = request.form.get('subtipo')
    nombre = request.form.get('nombre').upper()
    ram_instalada = request.form.get('iram_instalada')
    ram_maxima = request.form.get('tram_maxima')
    fecha_ram = request.form.get('fecha_ram')
    num_procesadores = request.form.get('num_procesadores')
    modelo = request.form.get('modelo')
    caracteristicas = request.form.get('caracteristicas').upper()
    ubicacion = request.form.get('ubicacion')
    contador_so = int(request.form.get('lista_ids_sistemas'))
    contador_ram = int(request.form.get('lista_ids_ram'))
    contador_almacenamiento = int(request.form.get('lista_ids_almacenamiento'))
    contador_micro = int(request.form.get('lista_ids_micro'))
    contador_tarjeta = int(request.form.get('lista_ids_tarjeta'))
    contador_puerto = int(request.form.get('lista_ids_puerto'))
    contador_lectora = int(request.form.get('lista_ids_lectora'))
    contador_red = int(request.form.get('lista_ids_red'))
    contador_ip = int(request.form.get('lista_ids_ip'))
    contador_mac = int(request.form.get('lista_ids_mac'))
    contador_resguardo = int(request.form.get('lista_ids_resguardo'))
    contador_interno = int(request.form.get('lista_ids_interno'))
    contador_usuario = int(request.form.get('lista_ids_usuario'))
    ids_so = []
    ids_ram = []
    ids_almacenamiento = []
    ids_micro = []
    ids_tarjeta = []
    ids_puerto = []
    ids_lectora = []
    ids_red = []
    ids_ip = []
    ids_mac = []
    ids_resguardo = []
    ids_interno = []
    ids_usuario = []
    if contador_so >= 1:
        for i in range (1, contador_so + 1) :
            ids_so.append(request.form.get(f'sistema_operativo_{i}'))
    if contador_ram >= 1:
        for i in range (1, contador_ram + 1) :
            ids_ram.append(request.form.get(f'ram_{i}'))
    if contador_almacenamiento >= 1:
        for i in range (1, contador_almacenamiento + 1) :
            ids_almacenamiento.append(request.form.get(f'almacenamiento_{i}'))
    if contador_micro >= 1:
        for i in range (1, contador_micro + 1) :
            ids_micro.append(request.form.get(f'micro_{i}'))
    if contador_tarjeta >= 1:
        for i in range (1, contador_tarjeta + 1) :
            ids_tarjeta.append(request.form.get(f'tarjeta_{i}'))
    if contador_puerto >= 1:
        for i in range (1, contador_puerto + 1) :
            ids_puerto.append(request.form.get(f'puerto_{i}'))
    if contador_lectora >= 1:
        for i in range (1, contador_lectora + 1) :
            ids_lectora.append(request.form.get(f'lectora_{i}'))
    if contador_red >= 1:
        for i in range (1, contador_red + 1) :
            ids_red.append(request.form.get(f'red_{i}'))
    if contador_resguardo >= 1:
        for i in range (1, contador_resguardo + 1) :
            ids_resguardo.append(request.form.get(f'resguardo_{i}'))
    if contador_interno >= 1:
        for i in range (1, contador_interno + 1) :
            ids_interno.append(request.form.get(f'interno_{i}'))
    if contador_usuario >= 1:
        for i in range (1, contador_usuario + 1) :
            ids_usuario.append(request.form.get(f'usuario_{i}'))
    if contador_ip >= 1:
        for i in range(1, contador_ip + 1):
            ip_value = request.form.get(f'ip_{i}')
            if not ip_value:
                ip_value = "NO ASIGNADA"
            ids_ip.append(ip_value)
    if contador_mac >= 1:
        for i in range(1, contador_mac + 1):
            mac_value = request.form.get(f'mac_{i}').upper()
            if not mac_value:
                mac_value = "NO INDICADA"
            ids_mac.append(mac_value)

    if not factura:
        factura = "NO SE ENCUENTRA"
    if not serial:
        serial = "N/A"
    if not caracteristicas:
        caracteristicas = "N/A"
    if num_inventario is not None and num_inventario != '':
        num_inventario = int(num_inventario)
    else:
        num_inventario = None
    if request.form.get('ram_unit') == 'TB':
        ram_maxima = str(int(ram_maxima) * 1024)
    # Redireccionar a la página de resultados y pasar los datos como parámetros en la URL
    return redirect(url_for('mostrar_resultados', factura=factura, serial=serial, num_inventario=num_inventario,
                            subtipo=subtipo, nombre=nombre,ram_instalada=ram_instalada, 
                            ram_maxima=ram_maxima,num_procesadores=num_procesadores, modelo=modelo,
                            caracteristicas=caracteristicas, ubicacion=ubicacion,
                            ids_usuario=ids_usuario, ids_resguardo=ids_resguardo, ids_interno=ids_interno, ids_so=ids_so, 
                            ids_almacenamiento=ids_almacenamiento, ids_ram=ids_ram, fecha_ram=fecha_ram, ids_micro=ids_micro,
                            ids_tarjeta=ids_tarjeta, ids_puerto=ids_puerto, ids_lectora=ids_lectora, ids_red=ids_red, ids_ip=ids_ip, ids_mac=ids_mac))


@app.route('/mostrar_resultados')
def mostrar_resultados():
    # Obtener los datos de la URL
    factura = request.args.get('factura')
    serial = request.args.get('serial')
    num_inventario = request.args.get('num_inventario')
    subtipo = int(request.args.get('subtipo'))
    nombre = request.args.get('nombre')
    ram_instalada = int(request.args.get('ram_instalada'))
    ram_maxima = int(request.args.get('ram_maxima'))
    fecha_ram = (request.args.get('fecha_ram'))
    num_procesadores = int(request.args.get('num_procesadores'))
    modelo = int(request.args.get('modelo'))
    caracteristicas = request.args.get('caracteristicas')
    ubicacion = int(request.args.get('ubicacion'))
    num_inventario = request.args.get('num_inventario')
    lista_ids_sistemas = request.args.getlist('ids_so')
    lista_ids_ram = request.args.getlist('ids_ram')
    lista_ids_almacenamiento = request.args.getlist('ids_almacenamiento')
    lista_ids_micro = request.args.getlist('ids_micro')
    lista_ids_tarjeta = request.args.getlist('ids_tarjeta')
    lista_ids_puerto = request.args.getlist('ids_puerto')
    lista_ids_lectora = request.args.getlist('ids_lectora')
    lista_ids_red = request.args.getlist('ids_red')
    lista_ids_ip = request.args.getlist('ids_ip')
    lista_ids_mac = request.args.getlist('ids_mac')
    lista_ids_resguardo = request.args.getlist('ids_resguardo')
    lista_ids_interno = request.args.getlist('ids_interno')
    lista_ids_usuario = request.args.getlist('ids_usuario')
    for i in range(len(lista_ids_sistemas)):
        lista_ids_sistemas[i] = int(lista_ids_sistemas[i])
    for i in range(len(lista_ids_ram)):
        lista_ids_ram[i] = int(lista_ids_ram[i])
    for i in range(len(lista_ids_almacenamiento)):
        lista_ids_almacenamiento[i] = int(lista_ids_almacenamiento[i])
    for i in range(len(lista_ids_micro)):
        lista_ids_micro[i] = int(lista_ids_micro[i])
    for i in range(len(lista_ids_tarjeta)):
        lista_ids_tarjeta[i] = int(lista_ids_tarjeta[i])
    for i in range(len(lista_ids_puerto)):
        lista_ids_puerto[i] = int(lista_ids_puerto[i])
    for i in range(len(lista_ids_lectora)):
        lista_ids_lectora[i] = int(lista_ids_lectora[i])
    for i in range(len(lista_ids_red)):
        lista_ids_red[i] = int(lista_ids_red[i])
    for i in range(len(lista_ids_ip)):
        lista_ids_ip[i] = lista_ids_ip[i]
    for i in range(len(lista_ids_mac)):
        lista_ids_mac[i] = lista_ids_mac[i]
    for i in range(len(lista_ids_resguardo)):
        lista_ids_resguardo[i] = lista_ids_resguardo[i]
    for i in range(len(lista_ids_interno)):
        lista_ids_interno[i] = lista_ids_interno[i]
    for i in range(len(lista_ids_usuario)):
        lista_ids_usuario[i] = lista_ids_usuario[i]

    insertar_dispoI(factura, serial, num_inventario, subtipo, nombre, ram_instalada, ram_maxima, num_procesadores, modelo,
                    caracteristicas, ubicacion, lista_ids_usuario, lista_ids_resguardo, lista_ids_interno, lista_ids_sistemas, lista_ids_ram, fecha_ram,
                    lista_ids_almacenamiento, lista_ids_micro, lista_ids_tarjeta, lista_ids_puerto, lista_ids_lectora, lista_ids_red,
                    lista_ids_ip, lista_ids_mac)
    # Renderizar la página de resultados con los datos recibidos
    #return render_template('resultados.html', factura=factura, serial=serial, num_inventario=num_inventario, subtipo=subtipo, nombre=nombre, ram_instalada=ram_instalada, ram_maxima=ram_maxima, num_procesadores=num_procesadores, modelo=modelo, caracteristicas=caracteristicas, ubicacion=ubicacion, fecha_ram=fecha_ram)
    datos_dispos = obtener_dispos()
    return render_template('Sdispos.html', datos_dispos=datos_dispos)

@app.route('/seleccionar_dispos')
def SDispos():
    # Comprobamos si el usuario está logeado. Si no, lo redirigimos al inicio de sesión.
    if 'logged_in' in session and session['logged_in']:
        # El usuario está logeado, renderizamos la página con la acción "Marca".
        datos_dispos = obtener_dispos()
        #nombres_modelo = obtener_info_modelo() #no se ocupa el modelo
        return render_template('Sdispos.html', datos_dispos=datos_dispos)
    
@app.route('/eliminar_dispo/<int:dispo_id>')
def eliminar_dispo(dispo_id):
    if 'logged_in' in session and session['logged_in']:
        #Eliminacion del registro indiciado (no tiene confirmacion)
        eliminar_dispos(dispo_id)
        # se deben obtener los datos para poder redirigir a seleccionar dispos
        datos_dispos = obtener_dispos()
        return render_template('Sdispos.html', datos_dispos=datos_dispos)
    else:
        return redirect(url_for('logout'))
    
@app.route('/editar_dispo/<int:dispo_id>')
def editar_dispo(dispo_id):
    if 'logged_in' in session and session['logged_in']:
        nombres_so = obtener_info_sistema_operativo()
        nombres_ram = obtener_info_ram()
        nombres_almacenamiento = obtener_info_almacenamiento()
        nombres_micro = obtener_info_micro()
        nombres_tarjeta = obtener_info_tarjeta()
        nombres_puerto = obtener_nombres_puerto()
        nombres_lectora = obtener_info_lectora()
        nombres_red = obtener_info_red()
        nombres_ubicacion = obtener_ubicaciones()
        nombres_resguardo = obtener_responsables_resguardo()
        nombres_interno = obtener_responsables_interno()

        obtener_dispoIDs = obtener_dispoID(dispo_id)
        obtener_ubicacion_original = obtener_ubicacionID(dispo_id)
        obtener_interno_original = obtener_internoID(dispo_id)
        obtener_resguardo_original = obtener_resguardoID(dispo_id)
        obtener_so_original = obtener_soID(dispo_id)
        obtener_ram_original = obtener_ramID(dispo_id)
        obtener_almacenamiento_original = obtener_almacenamientoID(dispo_id)
        obtener_micro_original = obtener_microID(dispo_id)
        obtener_tarjeta_original = obtener_tarjetaID(dispo_id)
        obtener_puerto_original = obtener_puertoID(dispo_id)
        obtener_lectora_original = obtener_lectoraID(dispo_id)
        obtener_red_original = obtener_redID(dispo_id)
        obtener_ip_original = obtener_ipID(dispo_id)
        obtener_mac_original = obtener_macID(dispo_id)

        nombres_subtipo = obtener_nombres_subtipo()
        nombres_modelo = obtener_info_modelo()

        numeroDeClics = len(obtener_interno_original) -1
        numeroDeClics_so = len(obtener_so_original) -1
        numeroDeClics_ram = len(obtener_ram_original) -1
        numeroDeClics_almacenamiento = len(obtener_almacenamiento_original) -1
        numeroDeClics_micro = len(obtener_micro_original) -1
        numeroDeClics_tarjeta = len(obtener_tarjeta_original) -1
        numeroDeClics_puerto = len(obtener_puerto_original) -1
        numeroDeClics_lectora = len(obtener_lectora_original) -1
        numeroDeClics_red = len(obtener_red_original) -1

        return render_template('Udispos.html', obtener_dispoIDs=obtener_dispoIDs, nombres_subtipo=nombres_subtipo,nombres_modelo=nombres_modelo,
                               obtener_ubicacion_original=obtener_ubicacion_original, nombres_ubicacion=nombres_ubicacion, obtener_resguardo_original=obtener_resguardo_original,
                                nombres_resguardo= nombres_resguardo, nombres_interno=nombres_interno, numeroDeClics=numeroDeClics,
                                obtener_interno_original=obtener_interno_original, nombres_so=nombres_so, nombres_ram=nombres_ram,
                                nombres_almacenamiento=nombres_almacenamiento, nombres_micro=nombres_micro, nombres_tarjeta=nombres_tarjeta,
                                nombres_puerto=nombres_puerto, nombres_lectora=nombres_lectora, nombres_red=nombres_red, obtener_so_original=obtener_so_original,
                                numeroDeClics_so=numeroDeClics_so, obtener_ram_original=obtener_ram_original, numeroDeClics_ram=numeroDeClics_ram,
                                obtener_almacenamiento_original=obtener_almacenamiento_original, numeroDeClics_almacenamiento=numeroDeClics_almacenamiento,
                                obtener_micro_original=obtener_micro_original, numeroDeClics_micro=numeroDeClics_micro, obtener_tarjeta_original=obtener_tarjeta_original,
                                numeroDeClics_tarjeta=numeroDeClics_tarjeta, obtener_puerto_original=obtener_puerto_original, numeroDeClics_puerto=numeroDeClics_puerto,
                                obtener_lectora_original=obtener_lectora_original, numeroDeClics_lectora=numeroDeClics_lectora, obtener_red_original=obtener_red_original,
                                numeroDeClics_red=numeroDeClics_red, obtener_ip_original=obtener_ip_original, obtener_mac_original=obtener_mac_original)
    else:
        return redirect(url_for('logout'))
    
@app.route('/modificar_dispo/<int:dispo_id>', methods=['POST'])
def modificar_dispo(dispo_id):
    # Obtener los datos del formulario
    factura = request.form.get('factura')
    serial = request.form.get('serial').upper()
    num_inventario = request.form.get('num_inventario')
    nombre = request.form.get('nombre').upper()
    estado = request.form.get('estado').upper()
    modelo = request.form.get('modelo')
    caracteristicas = request.form.get('caracteristicas')
    num_procesadores = request.form.get('num_procesadores')
    ram_instalada = request.form.get('iram_instalada')
    ram_maxima = request.form.get('tram_maxima')
    subtipo = request.form.get('subtipo')
    fecha_modificacion = datetime.date.today()

    obtener_interno_original = obtener_internoID(dispo_id)
    contador_interno = int(request.form.get('lista_ids_interno'))
    ids_interno = []
    if contador_interno >= 1:
        for i in range (1, contador_interno + 1) :
            ids_interno.append(request.form.get(f'interno_{i}'))
    for i in range(len(ids_interno)):
        if ids_interno[i]:
            ids_interno[i] = int(ids_interno[i])
    ids_interno = [x for x in ids_interno if x is not None]
    internof, internon = encontrar_cambios_con_repeticiones(obtener_interno_original, ids_interno)
    if internon:
        internon = [x for x in internon if x is not None]
    modificar_interno(dispo_id, internof, internon, fecha_modificacion)

    obtener_so_original = obtener_soID(dispo_id)
    contador_so = int(request.form.get('lista_ids_sistemas'))
    ids_so = []
    if contador_so >= 1:
        for i in range (1, contador_so + 1) :
            ids_so.append(request.form.get(f'sistema_operativo_{i}'))
    for i in range(len(ids_so)):
        if ids_so[i]:
            ids_so[i] = int(ids_so[i])
    ids_so = [x for x in ids_so if x is not None]
    sof, son = encontrar_cambios_con_repeticiones(obtener_so_original, ids_so)
    if son:
        son = [x for x in son if x is not None]
    modificar_so(dispo_id, sof, son, fecha_modificacion)

    obtener_ram_original = obtener_ramID(dispo_id)
    contador_ram = int(request.form.get('lista_ids_ram'))
    ids_ram = []
    if contador_ram >= 1:
        for i in range (1, contador_ram + 1) :
            ids_ram.append(request.form.get(f'ram_{i}'))
    for i in range(len(ids_ram)):
        if ids_ram[i]:
            ids_ram[i] = int(ids_ram[i])
    ids_ram = [x for x in ids_ram if x is not None]
    ramf, ramn = encontrar_cambios_con_repeticiones(obtener_ram_original, ids_ram)
    if ramn:
        ramn = [x for x in ramn if x is not None]
    modificar_ram(dispo_id, ramf, ramn, fecha_modificacion)

    obtener_tarjeta_original = obtener_tarjetaID(dispo_id)
    contador_tarjeta = int(request.form.get('lista_ids_tarjeta'))
    ids_tarjeta = []
    if contador_tarjeta >= 1:
        for i in range (1, contador_tarjeta + 1) :
            ids_tarjeta.append(request.form.get(f'tarjeta_{i}'))
    for i in range(len(ids_tarjeta)):
        if ids_tarjeta[i]:
            ids_tarjeta[i] = int(ids_tarjeta[i])
    ids_tarjeta = [x for x in ids_tarjeta if x is not None]
    tarjetaf, tarjetan = encontrar_cambios_con_repeticiones(obtener_tarjeta_original, ids_tarjeta)
    if tarjetan:
        tarjetan = [x for x in tarjetan if x is not None]
    modificar_tarjeta(dispo_id, tarjetaf, tarjetan, fecha_modificacion)

    obtener_puerto_original = obtener_puertoID(dispo_id)
    contador_puerto = int(request.form.get('lista_ids_puerto'))
    ids_puerto = []
    if contador_puerto >= 1:
        for i in range (1, contador_puerto + 1) :
            ids_puerto.append(request.form.get(f'puerto_{i}'))
    for i in range(len(ids_puerto)):
        if ids_puerto[i]:
            ids_puerto[i] = int(ids_puerto[i])
    ids_puerto = [x for x in ids_puerto if x is not None]
    puertof, puerton = encontrar_cambios_con_repeticiones(obtener_puerto_original, ids_puerto)
    if puerton:
        puerton = [x for x in puerton if x is not None]
    modificar_puerto(dispo_id, puertof, puerton, fecha_modificacion)

    obtener_micro_original = obtener_microID(dispo_id)
    contador_micro = int(request.form.get('lista_ids_micro'))
    ids_micro = []
    if contador_micro >= 1:
        for i in range (1, contador_micro + 1) :
            ids_micro.append(request.form.get(f'micro_{i}'))
    for i in range(len(ids_micro)):
        if ids_micro[i]:
            ids_micro[i] = int(ids_micro[i])
    ids_micro = [x for x in ids_micro if x is not None]
    microf, micron = encontrar_cambios_con_repeticiones(obtener_micro_original, ids_micro)
    if micron:
        micron = [x for x in micron if x is not None]
    modificar_micro(dispo_id, microf, micron, fecha_modificacion)

    obtener_almacenamiento_original = obtener_almacenamientoID(dispo_id)
    contador_almacenamiento = int(request.form.get('lista_ids_almacenamiento'))
    ids_almacenamiento = []
    if contador_almacenamiento >= 1:
        for i in range (1, contador_almacenamiento + 1) :
            ids_almacenamiento.append(request.form.get(f'almacenamiento_{i}'))
    for i in range(len(ids_almacenamiento)):
        if ids_almacenamiento[i]:
            ids_almacenamiento[i] = int(ids_almacenamiento[i])
    ids_almacenamiento = [x for x in ids_almacenamiento if x is not None]
    almacenamientof, almacenamienton = encontrar_cambios_con_repeticiones(obtener_almacenamiento_original, ids_almacenamiento)
    if almacenamienton:
        almacenamienton = [x for x in almacenamienton if x is not None]
    modificar_almacenamiento(dispo_id, almacenamientof, almacenamienton, fecha_modificacion)
    

    ubicacion_original = int(obtener_ubicacionID(dispo_id))
    ubicacion_nueva = int(request.form.get('ubicacion'))
    resguardo_original = int(obtener_resguardoID(dispo_id))
    resguardo_nueva = int(request.form.get('resguardo_1'))
    

    if ubicacion_original != ubicacion_nueva:
        modificar_ubicacion(dispo_id, ubicacion_nueva, fecha_modificacion)
    if resguardo_original != resguardo_nueva:
        modificar_resguardo(dispo_id, resguardo_nueva, fecha_modificacion)
    
    if not factura:
        factura = "NO SE ENCUENTRA"
    if not serial:
        serial = "N/A"
    if num_inventario is not None and num_inventario != '':
        num_inventario = int(num_inventario)
    else:
        num_inventario = None
    
    if ram_instalada is not None and ram_instalada != '':
        ram_instalada = int(ram_instalada)
    else:
        ram_instalada = None
    if  ram_maxima is not None and  ram_maxima != '':
         ram_maxima = int( ram_maxima)
    else:
         ram_maxima = None
    if request.form.get('ram_unit') == 'TB':
        ram_maxima = str(int(ram_maxima) * 1024)
    # Redireccionar a la página de resultados y pasar los datos como parámetros en la URL
    return redirect(url_for('mostrar_ModificacionD', dispo_id=dispo_id, factura=factura, serial=serial, num_inventario=num_inventario,
                            nombre=nombre, estado=estado, modelo=modelo, caracteristicas=caracteristicas, num_procesadores=num_procesadores,
                            ram_instalada=ram_instalada, ram_maxima=ram_maxima, subtipo=subtipo, fecha_modificacion=fecha_modificacion))

@app.route('/mostrar_ModificacionD')
def mostrar_ModificacionD():
    # Obtener los datos de la URL
    id_activo = request.args.get('dispo_id')
    factura = request.args.get('factura')
    serial = request.args.get('serial')
    num_inventario = request.args.get('num_inventario')
    nombre = request.args.get('nombre')
    estado = request.args.get('estado')
    modelo = int(request.args.get('modelo'))
    caracteristicas = request.args.get('caracteristicas')
    num_procesadores = int(request.args.get('num_procesadores'))
    ram_instalada = int(request.args.get('ram_instalada'))
    ram_maxima = int(request.args.get('ram_maxima'))
    subtipo = int(request.args.get('subtipo'))
    fecha_modificacion = request.args.get('fecha_modificacion')

    modificar_dispoD(id_activo, factura, serial, num_inventario, nombre, estado, modelo,
                    caracteristicas, num_procesadores, ram_instalada, ram_maxima, subtipo, fecha_modificacion)

    # Renderizar la página de resultados con los datos recibidos
    #return render_template('resultadoUpdD.html', id_activo=id_activo, factura=factura, serial=serial, num_inventario=num_inventario, nombre=nombre, estado=estado, modelo=modelo, caracteristicas=caracteristicas, num_procesadores=num_procesadores, ram_instalada=ram_instalada, ram_maxima=ram_maxima, subtipo=subtipo, fecha_modificacion=fecha_modificacion)
    datos_dispos = obtener_dispos()
    return render_template('Sdispos.html', datos_dispos=datos_dispos)

@app.route('/agregar_herramientas', methods=['POST'])
def agregar_herramienta():
    # Obtener los datos del formulario
    factura = request.form.get('factura')
    serial = request.form.get('serial').upper()
    num_inventario = request.form.get('num_inventario')
    nombre = request.form.get('nombre').upper()
    cantidad = request.form.get('cantidad')
    contenido = request.form.get('contenido').upper()
    modelo = request.form.get('modelo')
    descripcion = request.form.get('descripcion').upper()
    fecha_compra = datetime.date.today()
    ubicacion = request.form.get('ubicacion')
    contador_resguardo = int(request.form.get('lista_ids_resguardo'))
    contador_interno = int(request.form.get('lista_ids_interno'))
    contador_usuario = int(request.form.get('lista_ids_usuario'))
    ids_resguardo = []
    ids_interno = []
    ids_usuario = []
    if contador_resguardo >= 1:
        for i in range (1, contador_resguardo + 1) :
            ids_resguardo.append(request.form.get(f'resguardo_{i}'))
    if contador_interno >= 1:
        for i in range (1, contador_interno + 1) :
            ids_interno.append(request.form.get(f'interno_{i}'))
    if contador_usuario >= 1:
        for i in range (1, contador_usuario + 1) :
            ids_usuario.append(request.form.get(f'usuario_{i}'))

    if not factura:
        factura = "NO SE ENCUENTRA"
    if not serial:
        serial = "N/A"
    if not descripcion:
        descripcion = "N/A"
    if not contenido:
        contenido = "N/A"
    if num_inventario is not None and num_inventario != '':
        num_inventario = int(num_inventario)
    else:
        num_inventario = None
    # Redireccionar a la página de resultados y pasar los datos como parámetros en la URL
    return redirect(url_for('mostrar_resultadosH', factura=factura, serial=serial, num_inventario=num_inventario,
                            nombre=nombre, cantidad=cantidad,
                            contenido=contenido, modelo=modelo,
                            fecha_compra=fecha_compra,
                            descripcion=descripcion, ubicacion=ubicacion,
                            ids_usuario=ids_usuario, ids_resguardo=ids_resguardo, ids_interno=ids_interno))

@app.route('/mostrar_resultadosH')
def mostrar_resultadosH():
    # Obtener los datos de la URL
    factura = request.args.get('factura')
    serial = request.args.get('serial')
    num_inventario = request.args.get('num_inventario')
    nombre = request.args.get('nombre')
    cantidad = int(request.args.get('cantidad'))
    contenido = request.args.get('contenido')
    modelo = int(request.args.get('modelo'))
    descripcion = request.args.get('descripcion')
    num_inventario = request.args.get('num_inventario')
    fecha_compra = request.args.get('fecha_compra')
    ubicacion = int(request.args.get('ubicacion'))
    lista_ids_resguardo = request.args.getlist('ids_resguardo')
    lista_ids_interno = request.args.getlist('ids_interno')
    lista_ids_usuario = request.args.getlist('ids_usuario')
    for i in range(len(lista_ids_resguardo)):
        lista_ids_resguardo[i] = lista_ids_resguardo[i]
    for i in range(len(lista_ids_interno)):
        lista_ids_interno[i] = lista_ids_interno[i]
    for i in range(len(lista_ids_usuario)):
        lista_ids_usuario[i] = lista_ids_usuario[i]

    insertar_dispoH(factura, serial, num_inventario, nombre,
                    modelo, fecha_compra, cantidad, contenido,
                    descripcion, ubicacion, lista_ids_usuario, lista_ids_resguardo, lista_ids_interno)

    # Renderizar la página de resultados con los datos recibidos
    #return render_template('resultadosH.html', factura=factura, serial=serial, num_inventario=num_inventario, nombre=nombre, cantidad=cantidad, contenido=contenido, modelo=modelo, fecha_compra=fecha_compra, descripcion=descripcion)
    datos_herramientas = obtener_herramientas()
    return render_template('Sherramientas.html', datos_herramientas=datos_herramientas)

@app.route('/activos/herramientas')
def herramientas():
    # Comprobamos si el usuario está logeado. Si no, lo redirigimos al inicio de sesión.
    if 'logged_in' in session and session['logged_in']:
        # El usuario está logeado, renderizamos la página con la acción "Marca".
        return render_template('MHerramientas.html')
    else:
        return redirect(url_for('logout'))

@app.route('/activos/herramientas/agregar')
def AHerramientas():
    # Comprobamos si el usuario está logeado. Si no, lo redirigimos al inicio de sesión.
    if 'logged_in' in session and session['logged_in']:
        # El usuario está logeado, renderizamos la página con la acción "Marca".
        nombres_ubicacion = obtener_ubicaciones()
        nombres_resguardo = obtener_responsables_resguardo()
        nombres_interno = obtener_responsables_interno()
        nombres_usuarios = obtener_usuarios_finales()
        nombres_modelo = obtener_info_modelo()
        return render_template('AHerramientas.html', nombres_ubicacion=nombres_ubicacion,  
                            nombres_modelo=nombres_modelo,  
                            nombres_resguardo= nombres_resguardo, nombres_interno=nombres_interno, nombres_usuarios=nombres_usuarios)
    else:
        return redirect(url_for('logout'))
    
@app.route('/seleccionar_herramientas')
def SHerramientas():
    # Comprobamos si el usuario está logeado. Si no, lo redirigimos al inicio de sesión.
    if 'logged_in' in session and session['logged_in']:
        # El usuario está logeado, renderizamos la página con la acción "Marca".
        datos_herramientas = obtener_herramientas()
        #nombres_modelo = obtener_info_modelo() #no se ocupa el modelo
        return render_template('Sherramientas.html', datos_herramientas=datos_herramientas)

@app.route('/activos/herramientas/busqueda', methods=['GET', 'POST'])
def busquedaH():
    if 'logged_in' in session and session['logged_in']:
        diccionario = {}
        nombres_ubicacion = obtener_ubicaciones()
        # Obtener los parámetros del formulario
        num_serial = request.form.get('num_serial')
        nombre = request.form.get('nombre')
        num_inventario_str = request.form.get('num_inventario')
        estado = request.form.get('estado')
        ubicacion_str = request.form.get('ubicacion')
        if num_serial:
            diccionario["A.num_serial"] = num_serial
        if nombre:
            nombre.upper()
            diccionario["A.nombre"] = nombre
        if num_inventario_str:
            num_inventario_str = int(num_inventario_str)
            diccionario["A.num_inventario"] = num_inventario_str
        if estado:
            diccionario["A.estado"] = estado
        if ubicacion_str:
            ubicacion_str = int(ubicacion_str)
            diccionario["(SELECT GROUP_CONCAT(DISTINCT HAUB.UBICACION_ID) FROM HISTORICO_ACTIVO_UBICACION HAUB WHERE A.ACTIVO_ID = HAUB.ACTIVO_ID AND HAUB.OPERANTE = 1) "] = ubicacion_str

        datos_busqueda = busqueda_herramientas(diccionario)
        datos_procesados = []  # Lista para almacenar los resultados procesados
        for row in datos_busqueda:
            ubicacion_ids = row[11]
            resguardo_ids = row[12]
            interno_ids = row[13]

            ubicacion_info_list = []
            resguardo_info_list = []
            interno_info_list = []
            
            if ubicacion_ids:
                ubicacion_id_list = ubicacion_ids.split(",")  # Separar los IDs si no están vacíos
                for ubicacion_id in ubicacion_id_list:
                    ubicacion_info = consulta_ubicacion(ubicacion_id)  # Obtener la información de RAM
                    ubicacion_info_list.append(ubicacion_info)
            if resguardo_ids:
                resguardo_id_list = resguardo_ids.split(",")  # Separar los IDs si no están vacíos
                for resguardo_id in resguardo_id_list:
                    resguardo_info = consulta_resguardo(resguardo_id)  # Obtener la información de RAM
                    resguardo_info_list.append(resguardo_info)
            if interno_ids:
                interno_id_list = interno_ids.split(",")  # Separar los IDs si no están vacíos
                for interno_id in interno_id_list:
                    interno_info = consulta_interno(interno_id)  # Obtener la información de RAM
                    interno_info_list.append(interno_info)
            
            row_dict = {
                "FACTURA": row[0],
                "NUM_SERIAL": row[1],
                "NUM_INVENTARIO": row[2],
                "ACTIVO_NOMBRE": row[3],
                "ESTADO": row[4],
                "MODELO_NOMBRE": row[5],
                "FECHA_COMPRA": row[6],
                "FECHA_CONSUMO": row[7],
                "CANTIDAD": row[8],
                "CONTENIDO": row[9],
                "DESCRIPCION": row[10],
                "UBICACION_INFO": "-\n".join(ubicacion_info_list) if ubicacion_info_list else "",
                "RESGUARDO_INFO": "-\n".join(resguardo_info_list) if resguardo_info_list else "",
                "INTERNO_INFO": "-\n".join(interno_info_list) if interno_info_list else ""
            }
            datos_procesados.append(row_dict)
        return render_template('SBherramientas.html', datos_procesados=datos_procesados, nombres_ubicacion=nombres_ubicacion)
    else:
        return redirect(url_for('logout'))
    
@app.route('/eliminar_herramienta/<int:herramienta_id>')
def eliminar_herramienta(herramienta_id):
    if 'logged_in' in session and session['logged_in']:
        #Eliminacion del registro indiciado (no tiene confirmacion)
        eliminar_herramientas(herramienta_id)
        # se deben obtener los datos para poder redirigir a seleccionar libros
        datos_herramientas = obtener_herramientas()
        return render_template('Sherramientas.html', datos_herramientas=datos_herramientas)
    else:
        return redirect(url_for('logout'))

@app.route('/editar_herramienta/<int:herramienta_id>')
def editar_herramienta(herramienta_id):
    if 'logged_in' in session and session['logged_in']:
        # se deben obtener los datos para poder redirigir a seleccionar libros
        obtener_herramientaIDs = obtener_herramientaID(herramienta_id)
        #print(obtener_libroIDs) # no debería haber4 problema si los busco
        nombres_ubicacion = obtener_ubicaciones()
        nombres_resguardo = obtener_responsables_resguardo()
        nombres_interno = obtener_responsables_interno()
        nombres_usuarios = obtener_usuarios_finales()
        nombres_modelo = obtener_info_modelo()
        return render_template('Uherramientas.html', obtener_herramientaIDs=obtener_herramientaIDs, nombres_ubicacion=nombres_ubicacion,  
                            nombres_resguardo= nombres_resguardo, nombres_interno=nombres_interno, nombres_usuarios=nombres_usuarios, nombres_modelo=nombres_modelo)
    else:
        return redirect(url_for('logout'))

@app.route('/modificar_herramienta/<int:herramienta_id>', methods=['POST'])
def modificar_herramienta(herramienta_id):
    # Obtener los datos del formulario
    factura = request.form.get('factura')
    serial = request.form.get('serial').upper()
    num_inventario = request.form.get('num_inventario')
    nombre = request.form.get('nombre').upper()
    estado = request.form.get('estado').upper()
    modelo = request.form.get('modelo').upper()
    fecha_compra = request.form.get('fecha_compra')
    fecha_consumo = request.form.get('fecha_consumo')
    cantidad = request.form.get('cantidad')
    contenido = request.form.get('contenido').upper()
    descripcion = request.form.get('descripcion').upper()
    #ubicacion = request.form.get('ubicacion')
    #usuario = request.form.get('usuario')
    #resguardo = request.form.get('resguardo')
    #interno = request.form.get('interno')
    if not factura:
        factura = "NO SE ENCUENTRA"
    if not serial:
        serial = "N/A"
    if num_inventario is not None and num_inventario != '':
        num_inventario = int(num_inventario)
    else:
        num_inventario = None
    if not fecha_compra:
        fecha_compra = None
    if not fecha_consumo:
        fecha_consumo = None
    # Redireccionar a la página de resultados y pasar los datos como parámetros en la URL
    return redirect(url_for('mostrar_ModificacionH', herramienta_id=herramienta_id, factura=factura, serial=serial, num_inventario=num_inventario,
                            nombre=nombre, estado=estado, modelo=modelo,
                            fecha_compra=fecha_compra, fecha_consumo=fecha_consumo, cantidad=cantidad, contenido=contenido, descripcion=descripcion))

@app.route('/mostrar_ModificacionH')
def mostrar_ModificacionH():
    # Obtener los datos de la URL
    id_activo = request.args.get('herramienta_id')
    factura = request.args.get('factura')
    serial = request.args.get('serial')
    num_inventario = request.args.get('num_inventario')
    nombre = request.args.get('nombre')
    estado = request.args.get('estado')
    modelo = request.args.get('modelo')
    fecha_compra = request.args.get('fecha_compra')
    fecha_consumo = request.args.get('fecha_consumo')
    cantidad = request.args.get('cantidad')
    contenido = request.args.get('contenido')
    descripcion = request.args.get('descripcion')
    #ubicacion = int(request.args.get('ubicacion'))
    #usuario = int(request.args.get('usuario'))
    #resguardo = int(request.args.get('resguardo'))
    #interno = int(request.args.get('interno'))

    modificar_dispoH(id_activo, factura, serial, num_inventario, nombre, estado, modelo,
                    fecha_compra, fecha_consumo, cantidad, contenido, descripcion)

    # Renderizar la página de resultados con los datos recibidos
    #return render_template('resultadoUpdH.html', id_activo=id_activo, factura=factura, serial=serial, num_inventario=num_inventario, nombre=nombre, estado=estado, modelo=modelo, fecha_compra=fecha_compra, fecha_consumo=fecha_consumo, cantidad=cantidad, contenido=contenido, descripcion=descripcion)
    datos_herramientas = obtener_herramientas()
    return render_template('Sherramientas.html', datos_herramientas=datos_herramientas)
    
@app.route('/activos/libros')
def libros():
    # Comprobamos si el usuario está logeado. Si no, lo redirigimos al inicio de sesión.
    if 'logged_in' in session and session['logged_in']:
        # El usuario está logeado, renderizamos la página con la acción "Marca".
        return render_template('MLibros.html')
    else:
        return redirect(url_for('logout'))

@app.route('/activos/libros/agregar')
def ALibros():
    # Comprobamos si el usuario está logeado. Si no, lo redirigimos al inicio de sesión.
    if 'logged_in' in session and session['logged_in']:
        # El usuario está logeado, renderizamos la página con la acción "Marca".
        nombres_ubicacion = obtener_ubicaciones()
        nombres_resguardo = obtener_responsables_resguardo()
        nombres_interno = obtener_responsables_interno()
        nombres_usuarios = obtener_usuarios_finales()
        #nombres_modelo = obtener_info_modelo() #no se ocupa el modelo
        return render_template('Alibros.html', nombres_ubicacion=nombres_ubicacion,  
                            nombres_resguardo= nombres_resguardo, nombres_interno=nombres_interno, nombres_usuarios=nombres_usuarios)
    else:
        return redirect(url_for('logout'))
    
@app.route('/agregar_libros', methods=['POST'])
def agregar_libros():
    # Obtener los datos del formulario
    factura = request.form.get('factura')
    serial = request.form.get('serial').upper()
    num_inventario = request.form.get('num_inventario')
    nombre = request.form.get('nombre').upper()
    autor = request.form.get('autor').upper()
    editorial = request.form.get('editorial').upper()
    anio = request.form.get('anio')
    edicion = request.form.get('edicion').upper()
    cantidad = request.form.get('cantidad')
    fecha_compra = datetime.date.today()
    ubicacion = request.form.get('ubicacion')
    contador_resguardo = int(request.form.get('lista_ids_resguardo'))
    contador_interno = int(request.form.get('lista_ids_interno'))
    #print(contador_interno)#aqui llega bien
    contador_usuario = int(request.form.get('lista_ids_usuario'))
    ids_resguardo = []
    ids_interno = []
    ids_usuario = []
    if contador_resguardo >= 1:
        for i in range (1, contador_resguardo + 1) :
            ids_resguardo.append(request.form.get(f'resguardo_{i}'))
    if contador_interno >= 1:
        for i in range (1, contador_interno + 1) :
            ids_interno.append(request.form.get(f'interno_{i}'))
    if contador_usuario >= 1:
        for i in range (1, contador_usuario + 1) :
            ids_usuario.append(request.form.get(f'usuario_{i}'))
    #print(contador_interno)#aqui llega bien
    if not factura:
        factura = "NO SE ENCUENTRA"
    if not serial:
        serial = "N/A"
    if not autor:
        autor = "N/A"
    if not editorial:
        editorial = "N/A"
    if not edicion:
        edicion = "N/A"
    if num_inventario is not None and num_inventario != '':
        num_inventario = int(num_inventario)
    else:
        num_inventario = None
    if anio is not None and anio != '':
        anio = int(anio)
    else:
        anio = None
    if cantidad is not None and cantidad != '':
        cantidad = int(cantidad)
    else:
        cantidad = None
    # Redireccionar a la página de resultados y pasar los datos como parámetros en la URL
    return redirect(url_for('mostrar_resultadosL', factura=factura, serial=serial, num_inventario=num_inventario,
                            nombre=nombre, autor=autor,editorial=editorial, anio=anio, cantidad=cantidad,
                            edicion=edicion, ubicacion=ubicacion,
                            ids_usuario=ids_usuario, ids_resguardo=ids_resguardo, ids_interno=ids_interno, fecha_compra=fecha_compra))

@app.route('/mostrar_resultadosL')
def mostrar_resultadosL():
    # Obtener los datos de la URL
    factura = request.args.get('factura')
    serial = request.args.get('serial')
    num_inventario = request.args.get('num_inventario')
    nombre = request.args.get('nombre')
    autor = request.args.get('autor')
    editorial = request.args.get('editorial')
    anio = int(request.args.get('anio'))
    edicion = request.args.get('edicion')
    cantidad = request.args.get('cantidad')
    num_inventario = request.args.get('num_inventario')
    fecha_compra = request.args.get('fecha_compra')
    ubicacion = int(request.args.get('ubicacion'))
    lista_ids_resguardo = request.args.getlist('ids_resguardo')
    lista_ids_interno = request.args.getlist('ids_interno')
    lista_ids_usuario = request.args.getlist('ids_usuario')
    #print(lista_ids_interno) #llega vacia
    for i in range(len(lista_ids_resguardo)):
        lista_ids_resguardo[i] = lista_ids_resguardo[i]
    for i in range(len(lista_ids_interno)):
        lista_ids_interno[i] = lista_ids_interno[i]
    for i in range(len(lista_ids_usuario)):
        lista_ids_usuario[i] = lista_ids_usuario[i]

    insertar_dispoL(factura, serial, num_inventario, nombre,
                    autor, editorial, anio, edicion, cantidad,
                     ubicacion, lista_ids_usuario, lista_ids_resguardo, lista_ids_interno, fecha_compra)

    # Renderizar la página de resultados con los datos recibidos
    #return render_template('resultadosL.html', factura=factura, serial=serial, num_inventario=num_inventario, nombre=nombre, autor=autor, cantidad=cantidad, editorial=editorial, anio=anio, edicion=edicion)
    datos_libros = obtener_libros()
    return render_template('Slibros.html', datos_libros=datos_libros)

@app.route('/seleccionar_libros')
def SLibros():
    # Comprobamos si el usuario está logeado. Si no, lo redirigimos al inicio de sesión.
    if 'logged_in' in session and session['logged_in']:
        # El usuario está logeado, renderizamos la página con la acción "Marca".
        datos_libros = obtener_libros()
        #nombres_modelo = obtener_info_modelo() #no se ocupa el modelo
        return render_template('Slibros.html', datos_libros=datos_libros)
    else:
        return redirect(url_for('logout'))

@app.route('/activos/libros/busqueda', methods=['GET', 'POST'])
def busquedaL():
    if 'logged_in' in session and session['logged_in']:
        diccionario = {}
        nombres_ubicacion = obtener_ubicaciones()
        # Obtener los parámetros del formulario
        num_serial = request.form.get('num_serial')
        nombre = request.form.get('nombre')
        num_inventario_str = request.form.get('num_inventario')
        estado = request.form.get('estado')
        ubicacion_str = request.form.get('ubicacion')
        if num_serial:
            diccionario["A.num_serial"] = num_serial
        if nombre:
            nombre.upper()
            diccionario["A.nombre"] = nombre
        if num_inventario_str:
            num_inventario_str = int(num_inventario_str)
            diccionario["A.num_inventario"] = num_inventario_str
        if estado:
            diccionario["A.estado"] = estado
        if ubicacion_str:
            ubicacion_str = int(ubicacion_str)
            diccionario["(SELECT GROUP_CONCAT(DISTINCT HAUB.UBICACION_ID) FROM HISTORICO_ACTIVO_UBICACION HAUB WHERE A.ACTIVO_ID = HAUB.ACTIVO_ID AND HAUB.OPERANTE = 1) "] = ubicacion_str

        datos_busqueda = busqueda_libros(diccionario)
        datos_procesados = []  # Lista para almacenar los resultados procesados
        for row in datos_busqueda:
            ubicacion_ids = row[10]
            resguardo_ids = row[11]
            interno_ids = row[12]

            ubicacion_info_list = []
            resguardo_info_list = []
            interno_info_list = []
            
            if ubicacion_ids:
                ubicacion_id_list = ubicacion_ids.split(",")  # Separar los IDs si no están vacíos
                for ubicacion_id in ubicacion_id_list:
                    ubicacion_info = consulta_ubicacion(ubicacion_id)  # Obtener la información de RAM
                    ubicacion_info_list.append(ubicacion_info)
            if resguardo_ids:
                resguardo_id_list = resguardo_ids.split(",")  # Separar los IDs si no están vacíos
                for resguardo_id in resguardo_id_list:
                    resguardo_info = consulta_resguardo(resguardo_id)  # Obtener la información de RAM
                    resguardo_info_list.append(resguardo_info)
            if interno_ids:
                interno_id_list = interno_ids.split(",")  # Separar los IDs si no están vacíos
                for interno_id in interno_id_list:
                    interno_info = consulta_interno(interno_id)  # Obtener la información de RAM
                    interno_info_list.append(interno_info)
            
            row_dict = {
                "FACTURA": row[0],
                "NUM_SERIAL": row[1],
                "NUM_INVENTARIO": row[2],
                "ACTIVO_NOMBRE": row[3],
                "ESTADO": row[4],
                "EDITORIAL": row[5],
                "EDICION": row[6],
                "ANIO": row[7],
                "AUTOR": row[8],
                "CANTIDAD": row[9],
                "UBICACION_INFO": "-\n".join(ubicacion_info_list) if ubicacion_info_list else "",
                "RESGUARDO_INFO": "-\n".join(resguardo_info_list) if resguardo_info_list else "",
                "INTERNO_INFO": "-\n".join(interno_info_list) if interno_info_list else ""
            }
            datos_procesados.append(row_dict)
        return render_template('SBlibros.html', datos_procesados=datos_procesados, nombres_ubicacion=nombres_ubicacion)
    else:
        return redirect(url_for('logout'))
    
@app.route('/editar_libro/<int:libro_id>')
def editar_libro(libro_id):
    if 'logged_in' in session and session['logged_in']:
        # se deben obtener los datos para poder redirigir a seleccionar libros
        obtener_libroIDs = obtener_libroID(libro_id)
        #print(obtener_libroIDs) # no debe de haber problema si se llama
        nombres_ubicacion = obtener_ubicaciones()
        nombres_resguardo = obtener_responsables_resguardo()
        nombres_interno = obtener_responsables_interno()
        nombres_usuarios = obtener_usuarios_finales()
        return render_template('Ulibros.html', obtener_libroIDs=obtener_libroIDs, nombres_ubicacion=nombres_ubicacion,  
                            nombres_resguardo= nombres_resguardo, nombres_interno=nombres_interno, nombres_usuarios=nombres_usuarios)
    else:
        return redirect(url_for('logout'))

@app.route('/modificar_libro/<int:libro_id>', methods=['POST'])
def modificar_libro(libro_id):
    # Obtener los datos del formulario
    factura = request.form.get('factura')
    serial = request.form.get('serial').upper()
    num_inventario = request.form.get('num_inventario')
    nombre = request.form.get('nombre').upper()
    estado = request.form.get('estado').upper()
    autor = request.form.get('autor').upper()
    editorial = request.form.get('editorial').upper()
    anio = request.form.get('anio')
    edicion = request.form.get('edicion').upper()
    cantidad = request.form.get('cantidad')
    #ubicacion = request.form.get('ubicacion')
    #usuario = request.form.get('usuario')
    #resguardo = request.form.get('resguardo')
    #interno = request.form.get('interno')
    if not factura:
        factura = "NO SE ENCUENTRA"
    if not serial:
        serial = "N/A"
    if not autor:
        autor = "N/A"
    if not editorial:
        editorial = "N/A"
    if not edicion:
        edicion = "N/A"
    if num_inventario is not None and num_inventario != '':
        num_inventario = int(num_inventario)
    else:
        num_inventario = None
    if anio is not None and anio != '':
        anio = int(anio)
    else:
        anio = None
    if cantidad is not None and cantidad != '':
        cantidad = int(cantidad)
    else:
        cantidad = None
    # Redireccionar a la página de resultados y pasar los datos como parámetros en la URL
    return redirect(url_for('mostrar_ModificacionL', libro_id=libro_id, factura=factura, serial=serial, num_inventario=num_inventario,
                            nombre=nombre, estado=estado, autor=autor,editorial=editorial, anio=anio,
                            edicion=edicion, cantidad=cantidad))

@app.route('/mostrar_ModificacionL')
def mostrar_ModificacionL():
    # Obtener los datos de la URL
    id_activo = request.args.get('libro_id')
    factura = request.args.get('factura')
    serial = request.args.get('serial')
    num_inventario = request.args.get('num_inventario')
    nombre = request.args.get('nombre')
    estado = request.args.get('estado')
    autor = request.args.get('autor')
    editorial = request.args.get('editorial')
    anio = int(request.args.get('anio'))
    edicion = request.args.get('edicion')
    cantidad = request.args.get('cantidad')
    #ubicacion = int(request.args.get('ubicacion'))
    #usuario = int(request.args.get('usuario'))
    #resguardo = int(request.args.get('resguardo'))
    #interno = int(request.args.get('interno'))
    #num_inventario = request.args.get('num_inventario')

    modificar_dispoL(id_activo, factura, serial, num_inventario, nombre, estado,
                    autor, editorial, anio, edicion, cantidad)

    # Renderizar la página de resultados con los datos recibidos
    #return render_template('resultadoUpdL.html', id_activo=id_activo, factura=factura, serial=serial, num_inventario=num_inventario, nombre=nombre, estado=estado, autor=autor, editorial=editorial, anio=anio, edicion=edicion, cantidad=cantidad)
    datos_libros = obtener_libros()
    return render_template('Slibros.html', datos_libros=datos_libros)


@app.route('/eliminar_libro/<int:libro_id>')
def eliminar_libro(libro_id):
    if 'logged_in' in session and session['logged_in']:
        #Eliminacion del registro indiciado (no tiene confirmacion)
        eliminar_libros(libro_id)
        # se deben obtener los datos para poder redirigir a seleccionar libros
        datos_libros = obtener_libros()
        return render_template('Slibros.html', datos_libros=datos_libros)
    else:
        return redirect(url_for('logout'))

@app.route('/personas', methods=['GET', 'POST'])
def personas():
    if 'logged_in' in session and session['logged_in']:
        return render_template('MPersonas.html')
    else:
        return redirect(url_for('logout'))

@app.route('/personas/edificio', methods=['GET', 'POST'])
def edificio():
    # Comprobamos si el usuario está logeado. Si no, lo redirigimos al inicio de sesión.
    if 'logged_in' in session and session['logged_in']:
        # El usuario está logeado, renderizamos la página con la acción "Marca".
        datos_edificio = obtener_edificio()
        #nombres_modelo = obtener_info_modelo() #no se ocupa el modelo
        return render_template('Sedificio.html', datos_edificio=datos_edificio)
    else:
        return redirect(url_for('logout'))
    
@app.route('/personas/titulo', methods=['GET', 'POST'])
def titulo():
    # Comprobamos si el usuario está logeado. Si no, lo redirigimos al inicio de sesión.
    if 'logged_in' in session and session['logged_in']:
        # El usuario está logeado, renderizamos la página con la acción "Marca".
        datos_titulo = obtener_titulo()
        #nombres_modelo = obtener_info_modelo() #no se ocupa el modelo
        return render_template('Stitulo.html', datos_titulo=datos_titulo)
    else:
        return redirect(url_for('logout'))
    
@app.route('/personas/division', methods=['GET', 'POST'])
def division():
    # Comprobamos si el usuario está logeado. Si no, lo redirigimos al inicio de sesión.
    if 'logged_in' in session and session['logged_in']:
        # El usuario está logeado, renderizamos la página con la acción "Marca".
        datos_division = obtener_division()
        #nombres_modelo = obtener_info_modelo() #no se ocupa el modelo
        return render_template('Sdivision.html', datos_division=datos_division)
    else:
        return redirect(url_for('logout'))
    
@app.route('/personas/perfil', methods=['GET', 'POST'])
def perfil():
    # Comprobamos si el usuario está logeado. Si no, lo redirigimos al inicio de sesión.
    if 'logged_in' in session and session['logged_in']:
        # El usuario está logeado, renderizamos la página con la acción "Marca".
        datos_perfil = obtener_perfil()
        #nombres_modelo = obtener_info_modelo() #no se ocupa el modelo
        return render_template('Sperfil.html', datos_perfil=datos_perfil)
    else:
        return redirect(url_for('logout'))
    
@app.route('/personas/sector', methods=['GET', 'POST'])
def sector():
    # Comprobamos si el usuario está logeado. Si no, lo redirigimos al inicio de sesión.
    if 'logged_in' in session and session['logged_in']:
        # El usuario está logeado, renderizamos la página con la acción "Marca".
        datos_sector = obtener_sector()
        #nombres_modelo = obtener_info_modelo() #no se ocupa el modelo
        return render_template('Ssector.html', datos_sector=datos_sector)
    else:
        return redirect(url_for('logout'))

@app.route('/catalogos', methods=['GET', 'POST'])
def catalogos():
    if 'logged_in' in session and session['logged_in']:
        return render_template('MCatalogos.html')
    else:
        return redirect(url_for('logout'))

@app.route('/catalogos/marca', methods=['GET', 'POST'])
def marca():
    if 'logged_in' in session and session['logged_in']:
        datos_marca = obtener_marca()
        return render_template('Smarca.html', datos_marca=datos_marca)
    else:
        return redirect(url_for('logout'))

@app.route('/catalogos/microprocesador', methods=['GET', 'POST'])
def micro():
    if 'logged_in' in session and session['logged_in']:
        datos_micro = obtener_micro()
        return render_template('Smicro.html', datos_micro=datos_micro)
    else:
        return redirect(url_for('logout'))

@app.route('/activos/busqueda', methods=['GET', 'POST'])
def busquedaD():
    if 'logged_in' in session and session['logged_in']:
        diccionario = {}
        conteo_puertos = defaultdict(int)
        conteo_lectora = defaultdict(int)
        conteo_so = defaultdict(int)
        conteo_ram = defaultdict(int)
        conteo_micro = defaultdict(int)
        conteo_almacenamiento = defaultdict(int)
        conteo_red = defaultdict(int)
        conteo_video = defaultdict(int)
        nombres_ubicacion = obtener_ubicaciones()
        nombres_modelo = obtener_info_modelo()
        # Obtener los parámetros del formulario
        modelo = request.form.get('modelo')
        num_serial = request.form.get('num_serial')
        num_inventario_str = request.form.get('num_inventario')
        estado = request.form.get('estado')
        ubicacion_str = request.form.get('ubicacion')
        if modelo:
            modelo = int(modelo)
            diccionario["A.modelo_id"] = modelo
        if num_serial:
            diccionario["A.num_serial"] = num_serial
        if num_inventario_str:
            num_inventario_str = int(num_inventario_str)
            diccionario["A.num_inventario"] = num_inventario_str
        if estado:
            diccionario["A.estado"] = estado
        if ubicacion_str:
            ubicacion_str = int(ubicacion_str)
            diccionario["(SELECT GROUP_CONCAT(DISTINCT HAUB.UBICACION_ID) FROM HISTORICO_ACTIVO_UBICACION HAUB WHERE A.ACTIVO_ID = HAUB.ACTIVO_ID AND HAUB.OPERANTE = 1) "] = ubicacion_str

        datos_busqueda = busqueda_dispos(diccionario)
        datos_procesados = []  # Lista para almacenar los resultados procesados
        for row in datos_busqueda:
            ram_ids = row[11]  # Obtener los RAM_ID concatenados
            so_ids = row[12]
            video_ids = row[13]
            puerto_ids = row[14]
            micro_ids = row[15]
            almacenamiento_ids = row[16]
            lectora_ids = row[17]
            red_ids = row[18]
            ubicacion_ids = row[19]
            resguardo_ids = row[20]
            interno_ids = row[21]

            ram_info_list = []  # Lista para almacenar la información de RAM
            so_info_list = []
            video_info_list = []
            puerto_info_list = []
            micro_info_list = []
            almacenamiento_info_list = []
            lectora_info_list = []
            red_info_list = []
            ubicacion_info_list = []
            resguardo_info_list = []
            interno_info_list = []
            if ram_ids:
                ram_id_list = ram_ids.split(",")  # Separar los IDs si no están vacíos
                for ram_id in ram_id_list:
                    ram_info = consulta_ram(ram_id)  # Obtener la información de RAM
                    ram_info_list.append(ram_info)  # Agregar la información a la lista
            conteo_ram = {}
            for ram in ram_info_list:
                conteo_ram[ram] = conteo_ram.get(ram, 0) + 1
            nueva_lista_ram = []
            for ram, conteo in conteo_ram.items():
                if conteo > 1:
                    nueva_lista_ram.append(f"{conteo}: {ram}")
                else:
                    nueva_lista_ram.append(f"1: {ram}")
            ram_info_modificado = [re.sub(r'(\d+:)', r'<strong>\1</strong>', item) for item in nueva_lista_ram]
            if so_ids:
                so_id_list = so_ids.split(",")  # Separar los IDs si no están vacíos
                for so_id in so_id_list:
                    so_info = consulta_so(so_id)  # Obtener la información de RAM
                    so_info_list.append(so_info)
            conteo_so = {}
            for so in so_info_list:
                conteo_so[so] = conteo_so.get(so, 0) + 1
            nueva_lista_so = []
            for so, conteo in conteo_so.items():
                if conteo > 1:
                    nueva_lista_so.append(f"{conteo}: {so}")
                else:
                    nueva_lista_so.append(f"1: {so}")
            so_info_modificado = [re.sub(r'(\d+:)', r'<strong>\1</strong>', item) for item in nueva_lista_so]
            if video_ids:
                video_id_list = video_ids.split(",")  # Separar los IDs si no están vacíos
                for video_id in video_id_list:
                    video_info = consulta_video(video_id)  # Obtener la información de RAM
                    video_info_list.append(video_info)
            conteo_video = {}
            for video in video_info_list:
                conteo_video[video] = conteo_video.get(video, 0) + 1
            nueva_lista_video = []
            for video, conteo in conteo_video.items():
                if conteo > 1:
                    nueva_lista_video.append(f"{conteo}: {video}")
                else:
                    nueva_lista_video.append(f"1: {video}")
            video_info_modificado = [re.sub(r'(\d+:)', r'<strong>\1</strong>', item) for item in nueva_lista_video]
            if puerto_ids:
                puerto_id_list = puerto_ids.split(",")  # Separar los IDs si no están vacíos
                for puerto_id in puerto_id_list:
                    puerto_info = consulta_puerto(puerto_id)  # Obtener la información de RAM
                    puerto_info_list.append(puerto_info)
            conteo_puertos = {}
            for puerto in puerto_info_list:
                conteo_puertos[puerto] = conteo_puertos.get(puerto, 0) + 1
            nueva_lista_puertos = []
            for puerto, conteo in conteo_puertos.items():
                if conteo > 1:
                    nueva_lista_puertos.append(f"{conteo}: {puerto}")
                else:
                    nueva_lista_puertos.append(f"1: {puerto}")
            puerto_info_modificado = [re.sub(r'(\d+:)', r'<strong>\1</strong>', item) for item in nueva_lista_puertos]
            if micro_ids:
                micro_id_list = micro_ids.split(",")  # Separar los IDs si no están vacíos
                for micro_id in micro_id_list:
                    micro_info = consulta_micro(micro_id)  # Obtener la información de RAM
                    micro_info_list.append(micro_info)
            conteo_micro = {}
            for micro in micro_info_list:
                conteo_micro[micro] = conteo_micro.get(micro, 0) + 1
            nueva_lista_micro = []
            for micro, conteo in conteo_micro.items():
                if conteo > 1:
                    nueva_lista_micro.append(f"{conteo}: {micro}")
                else:
                    nueva_lista_micro.append(f"1: {micro}")
            micro_info_modificado = [re.sub(r'(\d+:)', r'<strong>\1</strong>', item) for item in nueva_lista_micro]
            if almacenamiento_ids:
                almacenamiento_id_list = almacenamiento_ids.split(",")  # Separar los IDs si no están vacíos
                for almacenamiento_id in almacenamiento_id_list:
                    almacenamiento_info = consulta_almacenamiento(almacenamiento_id)  # Obtener la información de RAM
                    almacenamiento_info_list.append(almacenamiento_info)
            conteo_almacenamiento = {}
            for almacenamiento in almacenamiento_info_list:
                conteo_almacenamiento[almacenamiento] = conteo_almacenamiento.get(almacenamiento, 0) + 1
            nueva_lista_almacenamiento = []
            for almacenamiento, conteo in conteo_almacenamiento.items():
                if conteo > 1:
                    nueva_lista_almacenamiento.append(f"{conteo}: {almacenamiento}")
                else:
                    nueva_lista_almacenamiento.append(f"1: {almacenamiento}")
            almacenamiento_info_modificado = [re.sub(r'(\d+:)', r'<strong>\1</strong>', item) for item in nueva_lista_almacenamiento]
            if lectora_ids:
                lectora_id_list = lectora_ids.split(",")  # Separar los IDs si no están vacíos
                for lectora_id in lectora_id_list:
                    lectora_info = consulta_lectora(lectora_id)  # Obtener la información de RAM
                    lectora_info_list.append(lectora_info)
            conteo_lectora = {}
            for lectora in lectora_info_list:
                conteo_lectora[lectora] = conteo_lectora.get(lectora, 0) + 1
            nueva_lista_lectora = []
            for lectora, conteo in conteo_lectora.items():
                if conteo > 1:
                    nueva_lista_lectora.append(f"{conteo}: {lectora}")
                else:
                    nueva_lista_lectora.append(f"1: {lectora}")
            lectora_info_modificado = [re.sub(r'(\d+:)', r'<strong>\1</strong>', item) for item in nueva_lista_lectora]
            if red_ids:
                red_id_list = red_ids.split(",")  # Separar los IDs si no están vacíos
                for red_id in red_id_list:
                    red_info = consulta_red(red_id)  # Obtener la información de RAM
                    red_info_list.append(red_info)
            conteo_red = {}
            for red in red_info_list:
                conteo_red[red] = conteo_red.get(red, 0) + 1
            nueva_lista_red = []
            for red, conteo in conteo_red.items():
                if conteo > 1:
                    nueva_lista_red.append(f"{conteo}: {red}")
                else:
                    nueva_lista_red.append(f"1: {red}")
            red_info_modificado = [re.sub(r'(\d+:)', r'<strong>\1</strong>', item) for item in nueva_lista_red]
            if ubicacion_ids:
                ubicacion_id_list = ubicacion_ids.split(",")  # Separar los IDs si no están vacíos
                for ubicacion_id in ubicacion_id_list:
                    ubicacion_info = consulta_ubicacion(ubicacion_id)  # Obtener la información de RAM
                    ubicacion_info_list.append(ubicacion_info)
            if resguardo_ids:
                resguardo_id_list = resguardo_ids.split(",")  # Separar los IDs si no están vacíos
                for resguardo_id in resguardo_id_list:
                    resguardo_info = consulta_resguardo(resguardo_id)  # Obtener la información de RAM
                    resguardo_info_list.append(resguardo_info)
            if interno_ids:
                interno_id_list = interno_ids.split(",")  # Separar los IDs si no están vacíos
                for interno_id in interno_id_list:
                    interno_info = consulta_interno(interno_id)  # Obtener la información de RAM
                    interno_info_list.append(interno_info)
            
            row_dict = {
                "FACTURA": row[0],
                "NUM_SERIAL": row[1],
                "NUM_INVENTARIO": row[2],
                "ACTIVO_NOMBRE": row[3],
                "ESTADO": row[4],
                "MODELO_NOMBRE": row[5],
                "CARACTERISTICAS": row[6],
                "NUM_PROCESADORES": row[7],
                "RAM_INSTALADA": row[8],
                "RAM_MAX": row[9],
                "SUBTIPO_NOMBRE": row[10],
                "RAM_INFO": ", ".join(ram_info_modificado) if ram_info_modificado else "",
                "SO_INFO": ", ".join(so_info_modificado) if so_info_modificado else "",
                "VIDEO_INFO": ", ".join(video_info_modificado) if video_info_modificado else "",
                "PUERTO_INFO": ", ".join(puerto_info_modificado) if puerto_info_modificado else "",
                "MICRO_INFO": ", ".join(micro_info_modificado) if micro_info_modificado else "",
                "ALMACENAMIENTO_INFO": ", ".join(almacenamiento_info_modificado) if almacenamiento_info_modificado else "",
                "LECTORA_INFO": ", ".join(lectora_info_modificado) if lectora_info_modificado else "",
                "RED_INFO": ", ".join(red_info_modificado) if red_info_modificado else "",
                "UBICACION_INFO": "-\n".join(ubicacion_info_list) if ubicacion_info_list else "",
                "RESGUARDO_INFO": "-\n".join(resguardo_info_list) if resguardo_info_list else "",
                "INTERNO_INFO": ", ".join(interno_info_list) if interno_info_list else ""
            }
            datos_procesados.append(row_dict)
        return render_template('SBdispos.html', datos_procesados=datos_procesados, nombres_ubicacion=nombres_ubicacion, nombres_modelo=nombres_modelo)
    else:
        return redirect(url_for('logout'))

@app.route('/historico_activo/<int:activo_id>')
def historico_activo(activo_id):
    if 'logged_in' in session and session['logged_in']:
        # se deben obtener los datos para poder redirigir a seleccionar Historicos
        nombre_activo = obtener_nombvreA(activo_id)
        historico_cambios = obtener_historicoC(activo_id)
        historico_ubicaciones = obtener_historicoUB(activo_id)
        historico_usuarios = obtener_historicoUF(activo_id)#no se ocupa para ninguna tabla
        historico_resguardante = obtener_historicoRR(activo_id)
        historico_Rinterno = obtener_historicoRI(activo_id)#no necesario
        print(historico_Rinterno)
        
        return render_template('Shistoricos.html', nombre_activo=nombre_activo, historico_ubicaciones=historico_ubicaciones,historico_usuarios=historico_usuarios,
                           historico_resguardante=historico_resguardante, historico_Rinterno=historico_Rinterno, historico_cambios=historico_cambios)
    else:
        return redirect(url_for('logout'))
    
@app.route('/historico_activoD/<int:activo_id>')
def historico_activoD(activo_id):
    if 'logged_in' in session and session['logged_in']:
        # se deben obtener los datos para poder redirigir a seleccionar Historicos
        nombre_activo = obtener_nombvreA(activo_id)
        historico_cambios = obtener_historicoC(activo_id)
        historico_ubicaciones = obtener_historicoUB(activo_id)
        historico_usuarios = obtener_historicoUF(activo_id)#no se ocupa para ninguna tabla
        historico_resguardante = obtener_historicoRR(activo_id)
        historico_Rinterno = obtener_historicoRI(activo_id)#si es necesario 
        #los necesarios de DISPO INTELIGENTE:
        historico_ram = obtener_historicoHRAM(activo_id)
        historico_so = obtener_historicoHSO(activo_id)
        historico_red = obtener_historicoHRED(activo_id)
        historico_tg = obtener_historicoHV(activo_id)
        historico_dd = obtener_historicoHDD(activo_id)
        historico_Mi = obtener_historicoHM(activo_id)
        historico_ul = obtener_historicoUL(activo_id)
        historico_pu = obtener_historicoP(activo_id)
        
        return render_template('ShistoricosD.html', nombre_activo=nombre_activo, historico_ubicaciones=historico_ubicaciones,historico_usuarios=historico_usuarios,
                           historico_resguardante=historico_resguardante, historico_Rinterno=historico_Rinterno, 
                           historico_so=historico_so, historico_ram=historico_ram, historico_red=historico_red, historico_tg=historico_tg,
                           historico_dd=historico_dd, historico_Mi=historico_Mi, historico_ul=historico_ul, historico_pu=historico_pu, historico_cambios=historico_cambios)
    else:
        return redirect(url_for('logout'))

@app.route('/eliminar_hub/<int:activo_id>/<int:historico_id>')
def eliminar_hub(activo_id, historico_id):
    if 'logged_in' in session and session['logged_in']:
        #Eliminacion del registro indiciado (no tiene confirmacion)
        eliminar_HUB(historico_id)
        # se deben obtener los datos para poder redirigir a seleccionar libros
        historico_cambios = obtener_historicoC(activo_id)
        historico_ubicaciones = obtener_historicoUB(activo_id)
        historico_usuarios = obtener_historicoUF(activo_id)#no se ocupa para ninguna tabla
        historico_resguardante = obtener_historicoRR(activo_id)
        historico_Rinterno = obtener_historicoRI(activo_id)#solo es necesario para 
        return render_template('Shistoricos.html', historico_ubicaciones=historico_ubicaciones,historico_usuarios=historico_usuarios,
                           historico_resguardante=historico_resguardante, historico_Rinterno=historico_Rinterno, historico_cambios=historico_cambios)
    else:
        return redirect(url_for('logout'))

@app.route('/eliminar_hubD/<int:activo_id>/<int:historico_id>')
def eliminar_hubD(activo_id, historico_id):
    if 'logged_in' in session and session['logged_in']:
        #Eliminacion del registro indiciado (no tiene confirmacion)
        eliminar_HUB(historico_id)
        # se deben obtener los datos para poder redirigir a seleccionar libros
        historico_cambios = obtener_historicoC(activo_id)
        historico_ubicaciones = obtener_historicoUB(activo_id)
        historico_usuarios = obtener_historicoUF(activo_id)#no se ocupa para ninguna tabla
        historico_resguardante = obtener_historicoRR(activo_id)
        historico_Rinterno = obtener_historicoRI(activo_id)#solo es necesario para 
        historico_ram = obtener_historicoHRAM(activo_id)
        historico_so = obtener_historicoHSO(activo_id)
        historico_red = obtener_historicoHRED(activo_id)
        historico_tg = obtener_historicoHV(activo_id)
        historico_dd = obtener_historicoHDD(activo_id)
        historico_Mi = obtener_historicoHM(activo_id)
        historico_ul = obtener_historicoUL(activo_id)
        historico_pu = obtener_historicoP(activo_id)
        return render_template('ShistoricosD.html', historico_ubicaciones=historico_ubicaciones,historico_usuarios=historico_usuarios,
                           historico_resguardante=historico_resguardante, historico_Rinterno=historico_Rinterno,
                           historico_ram=historico_ram, historico_so=historico_so, historico_red=historico_red, historico_tg=historico_tg,
                           historico_dd=historico_dd, historico_Mi=historico_Mi, historico_ul=historico_ul, historico_pu=historico_pu, historico_cambios=historico_cambios)
    else:
        return redirect(url_for('logout'))

@app.route('/eliminar_hrr/<int:activo_id>/<int:historico_id>')
def eliminar_hrr(activo_id, historico_id):
    if 'logged_in' in session and session['logged_in']:
        #Eliminacion del registro indiciado (no tiene confirmacion)
        eliminar_HRR(historico_id)
        # se deben obtener los datos para poder redirigir a seleccionar libros
        historico_cambios = obtener_historicoC(activo_id)
        historico_ubicaciones = obtener_historicoUB(activo_id)
        historico_usuarios = obtener_historicoUF(activo_id)#no se ocupa para ninguna tabla
        historico_resguardante = obtener_historicoRR(activo_id)
        historico_Rinterno = obtener_historicoRI(activo_id)#solo es necesario para 

        return render_template('Shistoricos.html', historico_ubicaciones=historico_ubicaciones,historico_usuarios=historico_usuarios,
                           historico_resguardante=historico_resguardante, historico_Rinterno=historico_Rinterno, historico_cambios=historico_cambios)
    else:
        return redirect(url_for('logout'))
    
@app.route('/eliminar_hrrD/<int:activo_id>/<int:historico_id>')
def eliminar_hrrD(activo_id, historico_id):
    if 'logged_in' in session and session['logged_in']:
        #Eliminacion del registro indiciado (no tiene confirmacion)
        eliminar_HRR(historico_id)
        # se deben obtener los datos para poder redirigir a seleccionar libros
        historico_cambios = obtener_historicoC(activo_id)
        historico_ubicaciones = obtener_historicoUB(activo_id)
        historico_usuarios = obtener_historicoUF(activo_id)#no se ocupa para ninguna tabla
        historico_resguardante = obtener_historicoRR(activo_id)
        historico_Rinterno = obtener_historicoRI(activo_id)#solo es necesario para 
        historico_ram = obtener_historicoHRAM(activo_id)
        historico_so = obtener_historicoHSO(activo_id)
        historico_red = obtener_historicoHRED(activo_id)
        historico_tg = obtener_historicoHV(activo_id)
        historico_dd = obtener_historicoHDD(activo_id)
        historico_Mi = obtener_historicoHM(activo_id)
        historico_ul = obtener_historicoUL(activo_id)
        historico_pu = obtener_historicoP(activo_id)
        return render_template('ShistoricosD.html', historico_ubicaciones=historico_ubicaciones,historico_usuarios=historico_usuarios,
                           historico_resguardante=historico_resguardante, historico_Rinterno=historico_Rinterno,
                           historico_ram=historico_ram, historico_so=historico_so, historico_red=historico_red, historico_tg=historico_tg,
                           historico_dd=historico_dd, historico_Mi=historico_Mi, historico_ul=historico_ul, historico_pu=historico_pu, historico_cambios=historico_cambios)
    else:
        return redirect(url_for('logout'))
    
@app.route('/eliminar_hri/<int:activo_id>/<int:historico_id>')
def eliminar_hri(activo_id, historico_id):
    if 'logged_in' in session and session['logged_in']:
        #Eliminacion del registro indiciado (no tiene confirmacion)
        eliminar_HRI(historico_id)
        # se deben obtener los datos para poder redirigir a seleccionar libros
        historico_cambios = obtener_historicoC(activo_id)
        historico_ubicaciones = obtener_historicoUB(activo_id)
        historico_usuarios = obtener_historicoUF(activo_id)#no se ocupa para ninguna tabla
        historico_resguardante = obtener_historicoRR(activo_id)
        historico_Rinterno = obtener_historicoRI(activo_id)#solo es necesario para 
        return render_template('Shistoricos.html', historico_ubicaciones=historico_ubicaciones,historico_usuarios=historico_usuarios,
                           historico_resguardante=historico_resguardante, historico_Rinterno=historico_Rinterno, historico_cambios=historico_cambios)
    else:
        return redirect(url_for('logout'))
    
@app.route('/eliminar_hriD/<int:activo_id>/<int:historico_id>')
def eliminar_hriD(activo_id, historico_id):
    if 'logged_in' in session and session['logged_in']:
        #Eliminacion del registro indiciado (no tiene confirmacion)
        eliminar_HRI(historico_id)
        # se deben obtener los datos para poder redirigir a seleccionar libros
        historico_cambios = obtener_historicoC(activo_id)
        historico_ubicaciones = obtener_historicoUB(activo_id)
        historico_usuarios = obtener_historicoUF(activo_id)#no se ocupa para ninguna tabla
        historico_resguardante = obtener_historicoRR(activo_id)
        historico_Rinterno = obtener_historicoRI(activo_id)#solo es necesario para 
        historico_ram = obtener_historicoHRAM(activo_id)
        historico_so = obtener_historicoHSO(activo_id)
        historico_red = obtener_historicoHRED(activo_id)
        historico_tg = obtener_historicoHV(activo_id)
        historico_dd = obtener_historicoHDD(activo_id)
        historico_Mi = obtener_historicoHM(activo_id)
        historico_ul = obtener_historicoUL(activo_id)
        historico_pu = obtener_historicoP(activo_id)
        return render_template('ShistoricosD.html', historico_ubicaciones=historico_ubicaciones,historico_usuarios=historico_usuarios,
                           historico_resguardante=historico_resguardante, historico_Rinterno=historico_Rinterno,
                           historico_ram=historico_ram, historico_so=historico_so, historico_red=historico_red, historico_tg=historico_tg,
                           historico_dd=historico_dd, historico_Mi=historico_Mi, historico_ul=historico_ul, historico_pu=historico_pu, historico_cambios=historico_cambios)
    else:
        return redirect(url_for('logout'))

@app.route('/eliminar_hso/<int:activo_id>/<int:historico_id>')
def eliminar_hso(activo_id, historico_id):
    if 'logged_in' in session and session['logged_in']:
        #Eliminacion del registro indiciado (no tiene confirmacion)
        eliminar_HSO(historico_id)
        # se deben obtener los datos para poder redirigir a seleccionar libros
        historico_cambios = obtener_historicoC(activo_id)
        historico_ubicaciones = obtener_historicoUB(activo_id)
        historico_usuarios = obtener_historicoUF(activo_id)#no se ocupa para ninguna tabla
        historico_resguardante = obtener_historicoRR(activo_id)
        historico_Rinterno = obtener_historicoRI(activo_id)#solo es necesario para
        historico_ram = obtener_historicoHRAM(activo_id)
        historico_so = obtener_historicoHSO(activo_id)
        historico_red = obtener_historicoHRED(activo_id)
        historico_tg = obtener_historicoHV(activo_id)
        historico_dd = obtener_historicoHDD(activo_id)
        historico_Mi = obtener_historicoHM(activo_id)
        historico_ul = obtener_historicoUL(activo_id)
        historico_pu = obtener_historicoP(activo_id)
        return render_template('ShistoricosD.html', historico_ubicaciones=historico_ubicaciones,historico_usuarios=historico_usuarios,
                           historico_resguardante=historico_resguardante, historico_Rinterno=historico_Rinterno,
                           historico_ram=historico_ram, historico_so=historico_so, historico_red=historico_red, historico_tg=historico_tg,
                           historico_dd=historico_dd, historico_Mi=historico_Mi, historico_ul=historico_ul, historico_pu=historico_pu, historico_cambios=historico_cambios)
    else:
        return redirect(url_for('logout'))

@app.route('/eliminar_hram/<int:activo_id>/<int:historico_id>')
def eliminar_hram(activo_id, historico_id):
    if 'logged_in' in session and session['logged_in']:
        #Eliminacion del registro indiciado (no tiene confirmacion)
        eliminar_HRAM(historico_id)
        # se deben obtener los datos para poder redirigir a seleccionar libros
        historico_cambios = obtener_historicoC(activo_id)
        historico_ubicaciones = obtener_historicoUB(activo_id)
        historico_usuarios = obtener_historicoUF(activo_id)#no se ocupa para ninguna tabla
        historico_resguardante = obtener_historicoRR(activo_id)
        historico_Rinterno = obtener_historicoRI(activo_id)#solo es necesario para
        historico_ram = obtener_historicoHRAM(activo_id)
        historico_so = obtener_historicoHSO(activo_id)
        historico_red = obtener_historicoHRED(activo_id)
        historico_tg = obtener_historicoHV(activo_id)
        historico_dd = obtener_historicoHDD(activo_id)
        historico_Mi = obtener_historicoHM(activo_id)
        historico_ul = obtener_historicoUL(activo_id)
        historico_pu = obtener_historicoP(activo_id)
        return render_template('ShistoricosD.html', historico_ubicaciones=historico_ubicaciones,historico_usuarios=historico_usuarios,
                           historico_resguardante=historico_resguardante, historico_Rinterno=historico_Rinterno,
                           historico_ram=historico_ram, historico_so=historico_so, historico_red=historico_red, historico_tg=historico_tg,
                           historico_dd=historico_dd, historico_Mi=historico_Mi, historico_ul=historico_ul, historico_pu=historico_pu, historico_cambios=historico_cambios)
    else:
        return redirect(url_for('logout'))

@app.route('/eliminar_hred/<int:activo_id>/<int:historico_id>')
def eliminar_hred(activo_id, historico_id):
    if 'logged_in' in session and session['logged_in']:
        #Eliminacion del registro indiciado (no tiene confirmacion)
        eliminar_HRED(historico_id)
        # se deben obtener los datos para poder redirigir a seleccionar libros
        historico_cambios = obtener_historicoC(activo_id)
        historico_ubicaciones = obtener_historicoUB(activo_id)
        historico_usuarios = obtener_historicoUF(activo_id)#no se ocupa para ninguna tabla
        historico_resguardante = obtener_historicoRR(activo_id)
        historico_Rinterno = obtener_historicoRI(activo_id)#solo es necesario para
        historico_ram = obtener_historicoHRAM(activo_id)
        historico_so = obtener_historicoHSO(activo_id)
        historico_red = obtener_historicoHRED(activo_id)
        historico_tg = obtener_historicoHV(activo_id)
        historico_dd = obtener_historicoHDD(activo_id)
        historico_Mi = obtener_historicoHM(activo_id)
        historico_ul = obtener_historicoUL(activo_id)
        historico_pu = obtener_historicoP(activo_id)
        return render_template('ShistoricosD.html', historico_ubicaciones=historico_ubicaciones,historico_usuarios=historico_usuarios,
                           historico_resguardante=historico_resguardante, historico_Rinterno=historico_Rinterno,
                           historico_ram=historico_ram, historico_so=historico_so, historico_red=historico_red, historico_tg=historico_tg,
                           historico_dd=historico_dd, historico_Mi=historico_Mi, historico_ul=historico_ul, historico_pu=historico_pu, historico_cambios=historico_cambios)
    else:
        return redirect(url_for('logout'))

@app.route('/eliminar_htg/<int:activo_id>/<int:historico_id>')
def eliminar_htg(activo_id, historico_id):
    if 'logged_in' in session and session['logged_in']:
        #Eliminacion del registro indiciado (no tiene confirmacion)
        eliminar_HV(historico_id)
        # se deben obtener los datos para poder redirigir a seleccionar libros
        historico_cambios = obtener_historicoC(activo_id)
        historico_ubicaciones = obtener_historicoUB(activo_id)
        historico_usuarios = obtener_historicoUF(activo_id)#no se ocupa para ninguna tabla
        historico_resguardante = obtener_historicoRR(activo_id)
        historico_Rinterno = obtener_historicoRI(activo_id)#solo es necesario para
        historico_ram = obtener_historicoHRAM(activo_id)
        historico_so = obtener_historicoHSO(activo_id)
        historico_red = obtener_historicoHRED(activo_id)
        historico_tg = obtener_historicoHV(activo_id)
        historico_dd = obtener_historicoHDD(activo_id)
        historico_Mi = obtener_historicoHM(activo_id)
        historico_ul = obtener_historicoUL(activo_id)
        historico_pu = obtener_historicoP(activo_id)
        return render_template('ShistoricosD.html', historico_ubicaciones=historico_ubicaciones,historico_usuarios=historico_usuarios,
                           historico_resguardante=historico_resguardante, historico_Rinterno=historico_Rinterno,
                           historico_ram=historico_ram, historico_so=historico_so, historico_red=historico_red, historico_tg=historico_tg,
                           historico_dd=historico_dd, historico_Mi=historico_Mi, historico_ul=historico_ul, historico_pu=historico_pu, historico_cambios=historico_cambios)
    else:
        return redirect(url_for('logout'))

@app.route('/eliminar_hdd/<int:activo_id>/<int:historico_id>')
def eliminar_hdd(activo_id, historico_id):
    if 'logged_in' in session and session['logged_in']:
        #Eliminacion del registro indiciado (no tiene confirmacion)
        eliminar_HDD(historico_id)
        # se deben obtener los datos para poder redirigir a seleccionar libros
        historico_cambios = obtener_historicoC(activo_id)
        historico_ubicaciones = obtener_historicoUB(activo_id)
        historico_usuarios = obtener_historicoUF(activo_id)#no se ocupa para ninguna tabla
        historico_resguardante = obtener_historicoRR(activo_id)
        historico_Rinterno = obtener_historicoRI(activo_id)#solo es necesario para
        historico_ram = obtener_historicoHRAM(activo_id)
        historico_so = obtener_historicoHSO(activo_id)
        historico_red = obtener_historicoHRED(activo_id)
        historico_tg = obtener_historicoHV(activo_id)
        historico_dd = obtener_historicoHDD(activo_id)
        historico_Mi = obtener_historicoHM(activo_id)
        historico_ul = obtener_historicoUL(activo_id)
        historico_pu = obtener_historicoP(activo_id)
        return render_template('ShistoricosD.html', historico_ubicaciones=historico_ubicaciones,historico_usuarios=historico_usuarios,
                           historico_resguardante=historico_resguardante, historico_Rinterno=historico_Rinterno,
                           historico_ram=historico_ram, historico_so=historico_so, historico_red=historico_red, historico_tg=historico_tg,
                           historico_dd=historico_dd, historico_Mi=historico_Mi, historico_ul=historico_ul, historico_pu=historico_pu, historico_cambios=historico_cambios)
    else:
        return redirect(url_for('logout'))

@app.route('/eliminar_hmi/<int:activo_id>/<int:historico_id>')
def eliminar_hmi(activo_id, historico_id):
    if 'logged_in' in session and session['logged_in']:
        #Eliminacion del registro indiciado (no tiene confirmacion)
        eliminar_HM(historico_id)
        # se deben obtener los datos para poder redirigir a seleccionar libros
        historico_cambios = obtener_historicoC(activo_id)
        historico_ubicaciones = obtener_historicoUB(activo_id)
        historico_usuarios = obtener_historicoUF(activo_id)#no se ocupa para ninguna tabla
        historico_resguardante = obtener_historicoRR(activo_id)
        historico_Rinterno = obtener_historicoRI(activo_id)#solo es necesario para
        historico_ram = obtener_historicoHRAM(activo_id)
        historico_so = obtener_historicoHSO(activo_id)
        historico_red = obtener_historicoHRED(activo_id)
        historico_tg = obtener_historicoHV(activo_id)
        historico_dd = obtener_historicoHDD(activo_id)
        historico_Mi = obtener_historicoHM(activo_id)
        historico_ul = obtener_historicoUL(activo_id)
        historico_pu = obtener_historicoP(activo_id)
        return render_template('ShistoricosD.html', historico_ubicaciones=historico_ubicaciones,historico_usuarios=historico_usuarios,
                           historico_resguardante=historico_resguardante, historico_Rinterno=historico_Rinterno,
                           historico_ram=historico_ram, historico_so=historico_so, historico_red=historico_red, historico_tg=historico_tg,
                           historico_dd=historico_dd, historico_Mi=historico_Mi, historico_ul=historico_ul, historico_pu=historico_pu, historico_cambios=historico_cambios)
    else:
        return redirect(url_for('logout'))

@app.route('/eliminar_hul/<int:activo_id>/<int:historico_id>')
def eliminar_hul(activo_id, historico_id):
    if 'logged_in' in session and session['logged_in']:
        #Eliminacion del registro indiciado (no tiene confirmacion)
        eliminar_HUL(historico_id)
        # se deben obtener los datos para poder redirigir a seleccionar libros
        historico_cambios = obtener_historicoC(activo_id)
        historico_ubicaciones = obtener_historicoUB(activo_id)
        historico_usuarios = obtener_historicoUF(activo_id)#no se ocupa para ninguna tabla
        historico_resguardante = obtener_historicoRR(activo_id)
        historico_Rinterno = obtener_historicoRI(activo_id)#solo es necesario para
        historico_ram = obtener_historicoHRAM(activo_id)
        historico_so = obtener_historicoHSO(activo_id)
        historico_red = obtener_historicoHRED(activo_id)
        historico_tg = obtener_historicoHV(activo_id)
        historico_dd = obtener_historicoHDD(activo_id)
        historico_Mi = obtener_historicoHM(activo_id)
        historico_ul = obtener_historicoUL(activo_id)
        historico_pu = obtener_historicoP(activo_id)
        return render_template('ShistoricosD.html', historico_ubicaciones=historico_ubicaciones,historico_usuarios=historico_usuarios,
                           historico_resguardante=historico_resguardante, historico_Rinterno=historico_Rinterno,
                           historico_ram=historico_ram, historico_so=historico_so, historico_red=historico_red, historico_tg=historico_tg,
                           historico_dd=historico_dd, historico_Mi=historico_Mi, historico_ul=historico_ul, historico_pu=historico_pu, historico_cambios=historico_cambios)
    else:
        return redirect(url_for('logout'))
    
@app.route('/eliminar_hpu/<int:activo_id>/<int:historico_id>')
def eliminar_hpu(activo_id, historico_id):
    if 'logged_in' in session and session['logged_in']:
        #Eliminacion del registro indiciado (no tiene confirmacion)
        eliminar_HP(historico_id)
        # se deben obtener los datos para poder redirigir a seleccionar libros
        historico_cambios = obtener_historicoC(activo_id)
        historico_ubicaciones = obtener_historicoUB(activo_id)
        historico_usuarios = obtener_historicoUF(activo_id)#no se ocupa para ninguna tabla
        historico_resguardante = obtener_historicoRR(activo_id)
        historico_Rinterno = obtener_historicoRI(activo_id)#solo es necesario para
        historico_ram = obtener_historicoHRAM(activo_id)
        historico_so = obtener_historicoHSO(activo_id)
        historico_red = obtener_historicoHRED(activo_id)
        historico_tg = obtener_historicoHV(activo_id)
        historico_dd = obtener_historicoHDD(activo_id)
        historico_Mi = obtener_historicoHM(activo_id)
        historico_ul = obtener_historicoUL(activo_id)
        historico_pu = obtener_historicoP(activo_id)
        return render_template('ShistoricosD.html', historico_ubicaciones=historico_ubicaciones,historico_usuarios=historico_usuarios,
                           historico_resguardante=historico_resguardante, historico_Rinterno=historico_Rinterno,
                           historico_ram=historico_ram, historico_so=historico_so, historico_red=historico_red, historico_tg=historico_tg,
                           historico_dd=historico_dd, historico_Mi=historico_Mi, historico_ul=historico_ul, historico_pu=historico_pu, historico_cambios=historico_cambios)
    else:
        return redirect(url_for('logout'))

@app.route('/personas/agregar_responsable_resguardo')
def responsableR():
    if 'logged_in' in session and session['logged_in']:
        return render_template('Shistoricos.html')
    else:
        return redirect(url_for('logout'))
    

##############################  M A I N ############################################################################
if __name__=='__main__':
    app.run(debug=True, port=5000)

