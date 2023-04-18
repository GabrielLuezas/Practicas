from codaio import Coda, Document, Cell, Row 
import pandas as pd
import datetime
import requests

coda = Coda('c5149980-deb1-4979-952f-f3d49ec5b038')
doc = Document('05ZbXhV8oe', coda=coda)
table = doc.get_table("Temperaturas Completar")

#Conseguir el ultimo valor añadido a la tabla de la columna Ciudad
df = pd.DataFrame(table.to_dict())
ultimafila=(df.head(1))
ciudad=ultimafila.loc[ultimafila.index[0], 'Ciudad']
print(ciudad)

fila = table.find_row_by_column_id_and_value({'c-TGQkNI9AD9':'Logroño'})
filaid= fila.id
print(filaid)

params = {
  'access_key': '9fb25c002a54d299b97223b9503828a0',
  'query': ciudad
}
api_result = requests.get('http://api.weatherstack.com/current', params)
#Clima, temperatura
data = api_result.json()
location = data['location']['name']
temperature = data['current']['temperature']
description = data['current']['weather_descriptions'][0]
#Fecha y hora
hora_actual = datetime.datetime.now()
horaformato = hora_actual.strftime("%H:%M")
fecha_actual = datetime.date.today()
fechaformato = fecha_actual.strftime("%d/%m/%Y")
print(f'El clima actual en {location} es {description} con una temperatura de {temperature} grados Celsius a las {horaformato} el {fechaformato}')