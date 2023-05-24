import pymongo
import pandas as pd 
import math
from codaio import Coda, Document, Cell, Row

coda = Coda('c5149980-deb1-4979-952f-f3d49ec5b038')
doc = Document('sATX4sy9Ea', coda=coda)
table = doc.get_table("MongoTabla")

#Conexion a Mongo
cliente = pymongo.MongoClient('localhost',
                             port=27017,
                             username='user',
                             password='password')    

#Mostrar todas las bases de datos
print (cliente.list_database_names())

db = cliente.get_database('python-mongo')
coleccion = db['Personas']

datos = list(coleccion.find())
df= pd.DataFrame(datos)
df = df.drop('_id', axis=1)
print(df)

df = df.where(pd.notnull(df), " ")

print(df)

nombres = df['Nombre'].tolist()
apellidos = df['Apellido'].tolist()
frutasfavoritas = df['FrutaFavorita'].tolist()
profesion = df['Profesión'].tolist()

rows = []
for nombre, apellido, fruta, profesion in zip(nombres, apellidos, frutasfavoritas, profesion):
    celda1 = Cell(column='c-w50vBdwrVp', value_storage=nombre)
    celda2 = Cell(column='c-KjRN8GJPiY', value_storage=apellido)
    celda3 = Cell(column='c-OTEYXjf6tT', value_storage=fruta)
    celda4 = Cell(column='c-3-M__Vgwmf', value_storage=profesion)
    rows.append([celda1, celda2, celda3, celda4])
table.upsert_rows(rows)