import pandas as pd

# Leer los datos desde el archivo Excel
df = pd.read_excel('Edificios.xlsx')

# Generar el script SQL
sql_script = ""
for index, row in df.iterrows():
    edificio_id = row['edificio_id']
    nombre = row['nombre']
    sql = f"INSERT INTO EDIFICIO (EDIFICIO_ID, NOMBRE) VALUES ('{edificio_id}', {nombre});\n"
    sql_script += sql

# Guardar el script SQL en un archivo
with open('datos_Edificio.sql', 'w') as file:
    file.write(sql_script)
