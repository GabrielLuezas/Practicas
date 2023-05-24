import mysql.connector
import pandas as pd
from codaio import Coda, Document, Cell, Row
from dateutil import parser
from mysql.connector import Error

coda = Coda('c5149980-deb1-4979-952f-f3d49ec5b038')
doc = Document('NOBRSEzMeJ', coda=coda)
table = doc.get_table("PARA-MARIADB")

mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password"
)
mycursor = mydb.cursor()

df = pd.DataFrame(table.to_dict())
df['Fecha'] = df['Fecha'].apply(lambda x: parser.parse(x).strftime('%Y-%m-%d'))
print(df)
try:
    cursor = mydb.cursor()
    cursor.execute("USE practicas")
    for _, row in df.iterrows():
        cursor.execute("INSERT INTO copia (ID, Nombre, Apellidos, Fecha) VALUES (%s, %s, %s, %s)",
                       (row['ID'], row['Nombre'], row['Apellidos'], row['Fecha']))
    mydb.commit()
    print("Datos guardados exitosamente en la tabla copia.")
except Error as e:
    print("Error al guardar los datos en MySQL:", e)
finally:
    cursor.close()
    mydb.close()