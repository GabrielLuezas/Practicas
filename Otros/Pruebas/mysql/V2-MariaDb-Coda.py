import mysql.connector
import pandas as pd
from codaio import Coda, Document, Cell, Row
from datetime import datetime

coda = Coda('c5149980-deb1-4979-952f-f3d49ec5b038')
doc = Document('NOBRSEzMeJ', coda=coda)
table = doc.get_table("MARIADB")

mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password"
)
mycursor = mydb.cursor()

mycursor.execute("USE practicas")
consulta = "SELECT * FROM prueba"
df = pd.read_sql_query(consulta, mydb)
mydb.close()
print(df)

ids = df['id'].tolist()
nombres = df['nombre'].tolist()
apellidos = df['apellidos'].tolist()
fechas = df['fecha'].tolist()
fechas_bien = [fecha.strftime('%Y-%m-%d') for fecha in fechas]

rows = []
for id, nombre, apellido, fecha in zip(ids, nombres, apellidos, fechas_bien):
    celda1 = Cell(column='c-24TVrzlNY6', value_storage=id)
    celda2 = Cell(column='c-yzVuMCgPIQ', value_storage=nombre)
    celda3 = Cell(column='c-LcyjwLzH9j', value_storage=apellido)
    celda4 = Cell(column='c-_PPH3yrNP9', value_storage=fecha)
    rows.append([celda1, celda2, celda3, celda4])

table.upsert_rows(rows)
