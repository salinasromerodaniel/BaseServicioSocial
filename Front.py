import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, session
from flask import g

app = Flask(__name__)

# Configuración para la sesión. Se necesita una clave secreta para firmar las cookies.
app.secret_key = 'mi_clave_secreta'

# Configura la conexión a la base de datos MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',
    'database': 'Inventario',
}
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()


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

@app.route('/activos', methods=['GET', 'POST'])
def activos():
    return render_template('MenuPrincipal.html')

@app.route('/personas', methods=['GET', 'POST'])
def personas():
    return render_template('MenuPrincipal.html')

@app.route('/historico', methods=['GET', 'POST'])
def historico():
    return render_template('MenuPrincipal.html')

if __name__=='__main__':
    app.run(debug=True, port=5000)