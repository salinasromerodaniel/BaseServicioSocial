import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="9806"
)

print(mydb)