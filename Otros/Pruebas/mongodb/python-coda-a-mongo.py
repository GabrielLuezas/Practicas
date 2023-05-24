import pymongo
import pandas as pd 
from codaio import Coda, Document, Cell, Row

coda = Coda('c5149980-deb1-4979-952f-f3d49ec5b038')
doc = Document('sATX4sy9Ea', coda=coda)
table = doc.get_table("MongoTabla")

#Conexion a Mongo
cliente = pymongo.MongoClient('localhost',
                             port=27017,
                             username='user',
                             password='password')    
db = cliente.get_database('python-mongo')
coleccion = db['Personas']
df = pd.DataFrame(table.to_dict())
print(df)

documentos = df.to_dict(orient='records')
coleccion.insert_many(documentos)
