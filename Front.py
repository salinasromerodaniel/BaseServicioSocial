import mysql.connector
from database import obtener_nombres_marca, obtener_nombres_modelo, obtener_nombres_ubicacion
from flask import Flask, render_template, request, redirect, url_for, session
from flask import g

app = Flask(__name__)

# Configuración para la sesión. Se necesita una clave secreta para firmar las cookies.
app.secret_key = 'mi_clave_secreta'


# Simulación de usuarios y contraseñas (reemplaza esto con una base de datos en un entorno de producción)
users = {
    'admin': 'admin'
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
        nombres_marca = obtener_nombres_marca()
        nombres_modelo = obtener_nombres_modelo()
        nombres_ubicacion = obtener_nombres_ubicacion()
        return render_template('ADispos.html', nombres_marca=nombres_marca, nombres_modelo=nombres_modelo, nombres_ubicacion=nombres_ubicacion)
    else:
        return redirect(url_for('logout'))
    
@app.route('/activos/herramientas')
def herramientas():
    # Comprobamos si el usuario está logeado. Si no, lo redirigimos al inicio de sesión.
    if 'logged_in' in session and session['logged_in']:
        # El usuario está logeado, renderizamos la página con la acción "Marca".
        return render_template('MHerramientas.html')
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