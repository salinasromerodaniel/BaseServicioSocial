import mysql.connector
from database import *
from flask import Flask, render_template, request, redirect, url_for, session
from flask import g
import datetime

app = Flask(__name__)

# Configuración para la sesión. Se necesita una clave secreta para firmar las cookies.
app.secret_key = 'mi_clave_secreta'


# Simulación de usuarios y contraseñas (reemplaza esto con una base de datos en un entorno de producción)
users = {
    'admin': 'admin',
    'david': 'david'
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
    return render_template('resultados.html', factura=factura, serial=serial, num_inventario=num_inventario,
                           subtipo=subtipo, nombre=nombre,
                           ram_instalada=ram_instalada, ram_maxima=ram_maxima,
                           num_procesadores=num_procesadores, modelo=modelo,
                           caracteristicas=caracteristicas, ubicacion=ubicacion, fecha_ram=fecha_ram)

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
        # se deben obtener los datos para poder redirigir a seleccionar libros
        obtener_dispoIDs = obtener_dispoID(dispo_id) #si lo imprime
        nombres_subtipo = obtener_nombres_subtipo()
        nombres_modelo = obtener_info_modelo()
        return render_template('Udispos.html', obtener_dispoIDs=obtener_dispoIDs, nombres_subtipo=nombres_subtipo,nombres_modelo=nombres_modelo)
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
    caracteristicas = request.form.get('caracterisiticas')
    num_procesadores = request.form.get('num_procesadores')
    ram_instalada = request.form.get('iram_instalada')
    ram_maxima = request.form.get('tram_maxima')
    subtipo = request.form.get('subtipo')
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
    # Redireccionar a la página de resultados y pasar los datos como parámetros en la URL
    return redirect(url_for('mostrar_ModificacionD', dispo_id=dispo_id, factura=factura, serial=serial, num_inventario=num_inventario,
                            nombre=nombre, estado=estado, modelo=modelo, caracteristicas=caracteristicas, num_procesadores=num_procesadores,
                            ram_instalada=ram_instalada, ram_maxima=ram_maxima, subtipo=subtipo))

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

    modificar_dispoD(id_activo, factura, serial, num_inventario, nombre, estado, modelo,
                    caracteristicas, num_procesadores, ram_instalada, ram_maxima, subtipo)

    # Renderizar la página de resultados con los datos recibidos
    return render_template('resultadoUpdD.html', id_activo=id_activo, factura=factura, serial=serial, num_inventario=num_inventario,
                           nombre=nombre, estado=estado, modelo=modelo, caracteristicas=caracteristicas, num_procesadores=num_procesadores,
                           ram_instalada=ram_instalada, ram_maxima=ram_maxima, subtipo=subtipo)

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
    return render_template('resultadosH.html', factura=factura, serial=serial, num_inventario=num_inventario,
                           nombre=nombre, cantidad=cantidad,
                            contenido=contenido, modelo=modelo,
                            fecha_compra=fecha_compra,
                            descripcion=descripcion)



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
    return render_template('resultadoUpdH.html', id_activo=id_activo, factura=factura, serial=serial, num_inventario=num_inventario,
                           nombre=nombre, estado=estado, modelo=modelo, fecha_compra=fecha_compra, fecha_consumo=fecha_consumo,
                            cantidad=cantidad, contenido=contenido, descripcion=descripcion)

    
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
                            ids_usuario=ids_usuario, ids_resguardo=ids_resguardo, interno=ids_interno, fecha_compra=fecha_compra))

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
    return render_template('resultadosL.html', factura=factura, serial=serial, num_inventario=num_inventario,
                           nombre=nombre, autor=autor, cantidad=cantidad,
                            editorial=editorial, anio=anio,
                            edicion=edicion)

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
    return render_template('resultadoUpdL.html', id_activo=id_activo, factura=factura, serial=serial, num_inventario=num_inventario,
                           nombre=nombre, estado=estado, autor=autor,
                            editorial=editorial, anio=anio,
                            edicion=edicion, cantidad=cantidad)


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
        datos_busqueda = busqueda_dispos()
        datos_procesados = []  # Lista para almacenar los resultados procesados
        
        for row in datos_busqueda:
            ram_ids = row[11]  # Obtener los RAM_ID concatenados
            so_ids = row[12]
            video_ids = row[13]
            puerto_ids = row[14]
            micro_ids = row[15]
            almacenamiento_ids = row[16]
            lectora_ids = row[17]

            ram_info_list = []  # Lista para almacenar la información de RAM
            so_info_list = []
            video_info_list = []
            puerto_info_list = []
            micro_info_list = []
            almacenamiento_info_list = []
            lectora_info_list = []
            
            if ram_ids:
                ram_id_list = ram_ids.split(",")  # Separar los IDs si no están vacíos
                for ram_id in ram_id_list:
                    ram_info = consulta_ram(ram_id)  # Obtener la información de RAM
                    ram_info_list.append(ram_info)  # Agregar la información a la lista
            if so_ids:
                so_id_list = so_ids.split(",")  # Separar los IDs si no están vacíos
                for so_id in so_id_list:
                    so_info = consulta_so(so_id)  # Obtener la información de RAM
                    so_info_list.append(so_info)
            if video_ids:
                video_id_list = video_ids.split(",")  # Separar los IDs si no están vacíos
                for video_id in video_id_list:
                    video_info = consulta_video(video_id)  # Obtener la información de RAM
                    video_info_list.append(video_info)
            if puerto_ids:
                puerto_id_list = puerto_ids.split(",")  # Separar los IDs si no están vacíos
                for puerto_id in puerto_id_list:
                    puerto_info = consulta_puerto(puerto_id)  # Obtener la información de RAM
                    puerto_info_list.append(puerto_info)
            if micro_ids:
                micro_id_list = micro_ids.split(",")  # Separar los IDs si no están vacíos
                for micro_id in micro_id_list:
                    micro_info = consulta_micro(micro_id)  # Obtener la información de RAM
                    micro_info_list.append(micro_info)
            if almacenamiento_ids:
                almacenamiento_id_list = almacenamiento_ids.split(",")  # Separar los IDs si no están vacíos
                for almacenamiento_id in almacenamiento_id_list:
                    almacenamiento_info = consulta_almacenamiento(almacenamiento_id)  # Obtener la información de RAM
                    almacenamiento_info_list.append(almacenamiento_info)
            if lectora_ids:
                lectora_id_list = lectora_ids.split(",")  # Separar los IDs si no están vacíos
                for lectora_id in lectora_id_list:
                    lectora_info = consulta_lectora(lectora_id)  # Obtener la información de RAM
                    lectora_info_list.append(lectora_info)
            
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
                "RAM_INFO": "-\n".join(ram_info_list) if ram_info_list else "",  # Unir la información de RAM con saltos de línea
                "SO_INFO": "-\n".join(so_info_list) if so_info_list else "",
                "VIDEO_INFO": "-\n".join(video_info_list) if video_info_list else "",
                "PUERTO_INFO": "-\n".join(puerto_info_list) if puerto_info_list else "",
                "MICRO_INFO": "-\n".join(micro_info_list) if micro_info_list else "",
                "ALMACENAMIENTO_INFO": "-\n".join(almacenamiento_info_list) if almacenamiento_info_list else "",
                "LECTORA_INFO": "-\n".join(lectora_info_list) if lectora_info_list else ""
            }
            datos_procesados.append(row_dict)
        
        return render_template('SBdispos.html', datos_procesados=datos_procesados)
    else:
        return redirect(url_for('logout'))




##############################  M A I N ############################################################################
if __name__=='__main__':
    app.run(debug=True, port=5000)

