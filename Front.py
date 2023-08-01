import mysql.connector
from flask import Flask, render_template, request
from flask import g

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin"
)

app = Flask(__name__)

print(mydb)