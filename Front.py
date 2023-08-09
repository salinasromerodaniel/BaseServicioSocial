import mysql.connector
from database import obtener_ubicaciones, obtener_info_sistema_operativo, obtener_nombres_subtipo, obtener_responsables_resguardo, obtener_info_ram
from database import obtener_responsables_interno, obtener_usuarios_finales, obtener_info_modelo, insertar_dispoI, insertar_dispoH, insertar_dispoL
from database import obtener_libros, eliminar_libros, obtener_info_almacenamiento, obtener_libroID
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
        return render_template('ADispos.html', nombres_ubicacion=nombres_ubicacion, nombres_so=nombres_so, 
                               nombres_subtipo=nombres_subtipo, nombres_modelo=nombres_modelo, nombres_ram=nombres_ram,  
                                nombres_resguardo= nombres_resguardo, nombres_interno=nombres_interno, 
                                nombres_almacenamiento=nombres_almacenamiento, nombres_usuarios=nombres_usuarios)
    else:
        return redirect(url_for('logout'))
    
@app.route('/agregar_dispositivo', methods=['POST'])
def agregar_dispositivo():
    # Obtener los datos del formulario
    factura = request.form.get('factura')
    serial = request.form.get('serial')
    num_inventario = request.form.get('num_inventario')
    subtipo = request.form.get('subtipo')
    nombre = request.form.get('nombre')
    ram_instalada = request.form.get('ram_instalada')
    ram_maxima = request.form.get('ram_maxima')
    fecha_ram = request.form.get('fecha_ram')
    num_procesadores = request.form.get('num_procesadores')
    modelo = request.form.get('modelo')
    caracteristicas = request.form.get('caracteristicas')
    ubicacion = request.form.get('ubicacion')
    usuario = request.form.get('usuario')
    resguardo = request.form.get('resguardo')
    interno = request.form.get('interno')
    contador_so = int(request.form.get('lista_ids_sistemas'))
    contador_ram = int(request.form.get('lista_ids_ram'))
    contador_almacenamiento = int(request.form.get('lista_ids_almacenamiento'))
    ids_so = []
    ids_ram = []
    ids_almacenamiento = []
    if contador_so >= 1:
        for i in range (1, contador_so + 1) :
            ids_so.append(request.form.get(f'sistema_operativo_{i}'))
    if contador_ram >= 1:
        for i in range (1, contador_ram + 1) :
            ids_ram.append(request.form.get(f'ram_{i}'))
    if contador_almacenamiento >= 1:
        for i in range (1, contador_almacenamiento + 1) :
            ids_almacenamiento.append(request.form.get(f'almacenamiento_{i}'))

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
                            usuario=usuario, resguardo=resguardo, interno=interno, ids_so=ids_so, 
                            ids_almacenamiento=ids_almacenamiento, ids_ram=ids_ram, fecha_ram=fecha_ram))


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
    usuario = int(request.args.get('usuario'))
    resguardo = int(request.args.get('resguardo'))
    interno = int(request.args.get('interno'))
    num_inventario = request.args.get('num_inventario')
    lista_ids_sistemas = request.args.getlist('ids_so')
    lista_ids_ram = request.args.getlist('ids_ram')
    lista_ids_almacenamiento = request.args.getlist('ids_almacenamiento')
    for i in range(len(lista_ids_sistemas)):
        lista_ids_sistemas[i] = int(lista_ids_sistemas[i])
    for i in range(len(lista_ids_ram)):
        lista_ids_ram[i] = int(lista_ids_ram[i])
    for i in range(len(lista_ids_almacenamiento)):
        lista_ids_almacenamiento[i] = int(lista_ids_almacenamiento[i])

    insertar_dispoI(factura, serial, num_inventario, subtipo, nombre, ram_instalada, ram_maxima, num_procesadores, modelo,
                    caracteristicas, ubicacion, usuario, resguardo, interno, lista_ids_sistemas, lista_ids_ram, fecha_ram,
                    lista_ids_almacenamiento)
    # Renderizar la página de resultados con los datos recibidos
    return render_template('resultados.html', factura=factura, serial=serial, num_inventario=num_inventario,
                           subtipo=subtipo, nombre=nombre,
                           ram_instalada=ram_instalada, ram_maxima=ram_maxima,
                           num_procesadores=num_procesadores, modelo=modelo,
                           caracteristicas=caracteristicas, ubicacion=ubicacion,
                           usuario=usuario, resguardo=resguardo, interno=interno, fecha_ram=fecha_ram)

@app.route('/agregar_herramientas', methods=['POST'])
def agregar_herramienta():
    # Obtener los datos del formulario
    factura = request.form.get('factura')
    serial = request.form.get('serial')
    num_inventario = request.form.get('num_inventario')
    nombre = request.form.get('nombre')
    cantidad = request.form.get('cantidad')
    contenido = request.form.get('contenido')
    modelo = request.form.get('modelo')
    descripcion = request.form.get('descripcion')
    ubicacion = request.form.get('ubicacion')
    usuario = request.form.get('usuario')
    resguardo = request.form.get('resguardo')
    interno = request.form.get('interno')
    fecha_compra = datetime.date.today()

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
                            usuario=usuario, resguardo=resguardo, interno=interno))

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
    ubicacion = int(request.args.get('ubicacion'))
    usuario = int(request.args.get('usuario'))
    resguardo = int(request.args.get('resguardo'))
    interno = int(request.args.get('interno'))
    num_inventario = request.args.get('num_inventario')
    fecha_compra = request.args.get('fecha_compra')

    insertar_dispoH(factura, serial, num_inventario, nombre,
                    modelo, fecha_compra, cantidad, contenido,
                    descripcion, ubicacion, usuario, resguardo, interno)

    # Renderizar la página de resultados con los datos recibidos
    return render_template('resultadosH.html', factura=factura, serial=serial, num_inventario=num_inventario,
                           nombre=nombre, cantidad=cantidad,
                            contenido=contenido, modelo=modelo,
                            fecha_compra=fecha_compra,
                            descripcion=descripcion, ubicacion=ubicacion,
                           usuario=usuario, resguardo=resguardo, interno=interno)



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

@app.route('/activos/proyectores')
def proyectores():
    # Comprobamos si el usuario está logeado. Si no, lo redirigimos al inicio de sesión.
    if 'logged_in' in session and session['logged_in']:
        # El usuario está logeado, renderizamos la página con la acción "Marca".
        return render_template('MProyectores.html')
    else:
        return redirect(url_for('logout'))
    
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
    serial = request.form.get('serial')
    num_inventario = request.form.get('num_inventario')
    nombre = request.form.get('nombre')
    autor = request.form.get('autor')
    editorial = request.form.get('editorial')
    anio = request.form.get('anio')
    edicion = request.form.get('edicion')
    ubicacion = request.form.get('ubicacion')
    usuario = request.form.get('usuario')
    resguardo = request.form.get('resguardo')
    interno = request.form.get('interno')

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
    # Redireccionar a la página de resultados y pasar los datos como parámetros en la URL
    return redirect(url_for('mostrar_resultadosL', factura=factura, serial=serial, num_inventario=num_inventario,
                            nombre=nombre, autor=autor,editorial=editorial, anio=anio,
                            edicion=edicion, ubicacion=ubicacion,
                            usuario=usuario, resguardo=resguardo, interno=interno))

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
    ubicacion = int(request.args.get('ubicacion'))
    usuario = int(request.args.get('usuario'))
    resguardo = int(request.args.get('resguardo'))
    interno = int(request.args.get('interno'))
    num_inventario = request.args.get('num_inventario')

    insertar_dispoL(factura, serial, num_inventario, nombre,
                    autor, editorial, anio, edicion,
                     ubicacion, usuario, resguardo, interno)

    # Renderizar la página de resultados con los datos recibidos
    return render_template('resultadosL.html', factura=factura, serial=serial, num_inventario=num_inventario,
                           nombre=nombre, autor=autor,
                            editorial=editorial, anio=anio,
                            edicion=edicion, ubicacion=ubicacion,
                           usuario=usuario, resguardo=resguardo, interno=interno)

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
        nombres_ubicacion = obtener_ubicaciones()
        nombres_resguardo = obtener_responsables_resguardo()
        nombres_interno = obtener_responsables_interno()
        nombres_usuarios = obtener_usuarios_finales()
        return render_template('Ulibros.html', obtener_libroIDs=obtener_libroIDs, nombres_ubicacion=nombres_ubicacion,  
                            nombres_resguardo= nombres_resguardo, nombres_interno=nombres_interno, nombres_usuarios=nombres_usuarios)
    else:
        return redirect(url_for('logout'))

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
    return render_template('MenuPrincipal.html')

@app.route('/historico', methods=['GET', 'POST'])
def historico():
    return render_template('MenuPrincipal.html')


##############################  M A I N ############################################################################
if __name__=='__main__':
    app.run(debug=True, port=5000)

