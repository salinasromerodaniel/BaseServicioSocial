import mysql.connector
from flask import Flask, render_template, request
from flask import g

app = Flask(__name__)

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
    'admin': 'admin',
    'user2': 'password2',
    # Agrega más usuarios aquí...
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # Aquí puedes agregar código para iniciar sesión, como establecer una sesión de usuario.
        return f'¡Bienvenido, {username}!'
    else:
        return 'Credenciales inválidas. Por favor, vuelve a intentarlo.'

if __name__=='__main__':
    app.run(debug=True, port=5000)