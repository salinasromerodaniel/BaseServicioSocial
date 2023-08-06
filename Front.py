import mysql.connector
from database import obtener_ubicaciones, obtener_info_sistema_operativo, obtener_nombres_subtipo, obtener_responsables_resguardo
from database import obtener_responsables_interno, obtener_usuarios_finales, obtener_info_modelo, insertar_dispoI, insertar_dispoH
from flask import Flask, render_template, request, redirect, url_for, session
from flask import g

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
        nombres_ubicacion = obtener_ubicaciones()
        nombres_so = obtener_info_sistema_operativo()
        nombres_subtipo = obtener_nombres_subtipo()
        nombres_resguardo = obtener_responsables_resguardo()
        nombres_interno = obtener_responsables_interno()
        nombres_usuarios = obtener_usuarios_finales()
        nombres_modelo = obtener_info_modelo()
        return render_template('ADispos.html', nombres_ubicacion=nombres_ubicacion, nombres_so=nombres_so, 
                               nombres_subtipo=nombres_subtipo, nombres_modelo=nombres_modelo,  
                                nombres_resguardo= nombres_resguardo, nombres_interno=nombres_interno, nombres_usuarios=nombres_usuarios)
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
    sistema_operativo = request.form.get('sistema_operativo')
    ram_instalada = request.form.get('ram_instalada')
    ram_maxima = request.form.get('ram_maxima')
    num_procesadores = request.form.get('num_procesadores')
    modelo = request.form.get('modelo')
    caracteristicas = request.form.get('caracteristicas')
    ubicacion = request.form.get('ubicacion')
    usuario = request.form.get('usuario')
    resguardo = request.form.get('resguardo')
    interno = request.form.get('interno')
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
                            subtipo=subtipo, nombre=nombre, sistema_operativo=sistema_operativo,
                            ram_instalada=ram_instalada, ram_maxima=ram_maxima,
                            num_procesadores=num_procesadores, modelo=modelo,
                            caracteristicas=caracteristicas, ubicacion=ubicacion,
                            usuario=usuario, resguardo=resguardo, interno=interno))


@app.route('/mostrar_resultados')
def mostrar_resultados():
    # Obtener los datos de la URL
    factura = request.args.get('factura')
    serial = request.args.get('serial')
    num_inventario = request.args.get('num_inventario')
    subtipo = int(request.args.get('subtipo'))
    nombre = request.args.get('nombre')
    sistema_operativo = request.args.get('sistema_operativo')
    ram_instalada = int(request.args.get('ram_instalada'))
    ram_maxima = int(request.args.get('ram_maxima'))
    num_procesadores = int(request.args.get('num_procesadores'))
    modelo = int(request.args.get('modelo'))
    caracteristicas = request.args.get('caracteristicas')
    ubicacion = int(request.args.get('ubicacion'))
    usuario = int(request.args.get('usuario'))
    resguardo = int(request.args.get('resguardo'))
    interno = int(request.args.get('interno'))
    num_inventario = request.args.get('num_inventario')



    insertar_dispoI(factura, serial, num_inventario, subtipo, nombre,
                    ram_instalada, ram_maxima, num_procesadores, modelo,
                    caracteristicas, ubicacion, usuario, resguardo, interno)

    # Renderizar la página de resultados con los datos recibidos
    return render_template('resultados.html', factura=factura, serial=serial, num_inventario=num_inventario,
                           subtipo=subtipo, nombre=nombre, sistema_operativo=sistema_operativo,
                           ram_instalada=ram_instalada, ram_maxima=ram_maxima,
                           num_procesadores=num_procesadores, modelo=modelo,
                           caracteristicas=caracteristicas, ubicacion=ubicacion,
                           usuario=usuario, resguardo=resguardo, interno=interno)

@app.route('/agregar_herramientas', methods=['POST'])
def agregar_herramienta():
    # Obtener los datos del formulario
    factura = request.form.get('factura')
    serial = request.form.get('serial')
    num_inventario = request.form.get('num_inventario')
    subtipo = request.form.get('subtipo')
    nombre = request.form.get('nombre')
    sistema_operativo = request.form.get('sistema_operativo')
    ram_instalada = request.form.get('ram_instalada')
    ram_maxima = request.form.get('ram_maxima')
    num_procesadores = request.form.get('num_procesadores')
    modelo = request.form.get('modelo')
    caracteristicas = request.form.get('caracteristicas')
    ubicacion = request.form.get('ubicacion')
    usuario = request.form.get('usuario')
    resguardo = request.form.get('resguardo')
    interno = request.form.get('interno')
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
                            subtipo=subtipo, nombre=nombre, sistema_operativo=sistema_operativo,
                            ram_instalada=ram_instalada, ram_maxima=ram_maxima,
                            num_procesadores=num_procesadores, modelo=modelo,
                            caracteristicas=caracteristicas, ubicacion=ubicacion,
                            usuario=usuario, resguardo=resguardo, interno=interno))


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

@app.route('/personas', methods=['GET', 'POST'])
def personas():
    return render_template('MenuPrincipal.html')

@app.route('/historico', methods=['GET', 'POST'])
def historico():
    return render_template('MenuPrincipal.html')

if __name__=='__main__':
    app.run(debug=True, port=5000)