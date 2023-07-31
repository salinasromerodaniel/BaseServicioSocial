import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="unam"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE inventario")