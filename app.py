from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

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

@app.route('/')
def index():
    return render_template('index.html')

#INSERTAR EN EDIFICIO
@app.route('/insertar', methods=['POST'])
def insertar_Edificio():
    if request.method == 'POST':
        # Obtiene los datos del formulario
        nombre = request.form['nombre']
        edificio_ID = int(request.form['eficio_ID'])

        # Inserta el registro en la tabla de la base de datos
        query = "INSERT INTO EDIFICIO (NOMBRE, EDIFICIO_ID) VALUES (%s, %s)"
        data = (nombre, edificio_ID)
        cursor.execute(query, data)
        conn.commit()

        return redirect(url_for('index')) #cambiar al nombre correcto de URL

if __name__ == '__main__':
    app.run(debug=True)