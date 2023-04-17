import requests
from codaio import Coda, Document, Cell, Row 
import datetime

ciudad = input("Dime una Ciudad: ")
params = {
  'access_key': '3814acbde3108b3c251e2654e9573de5',
  'query': ciudad
}

api_result = requests.get('http://api.weatherstack.com/current', params)

data = api_result.json()
location = data['location']['name']
temperature = data['current']['temperature']
description = data['current']['weather_descriptions'][0]
hora_actual = datetime.datetime.now()
horaformato = hora_actual.strftime("%H:%M")
fecha_actual = datetime.date.today()
fechaformato = fecha_actual.strftime("%d/%m/%Y")

if description == "Sunny":
    description = ("soleado")
elif description == "Clear":
    description = ("despejado")
elif description == "Light rain shower":
    description = ("lluvia ligera")
elif description == "Patchy light rain":
    description = ("lluvia ligera irregular")
elif description == "Partly cloudy":
    description = ("parcialmente nublado")
elif description == "Fog":
  description = ("neblina")
elif description == "Patchy rain possible":
    description = ("posible lluvia irregular")
elif description == "Light Rain":
    description = ("lluvia ligera")
elif description == "Light Rain, Fog":
    description = ("lluvia ligera con niebla")
print(f'El clima actual en {location} es {description} con una temperatura de {temperature} grados Celsius a las {horaformato} el {fechaformato}')

coda = Coda('c5149980-deb1-4979-952f-f3d49ec5b038')
doc = Document('05ZbXhV8oe', coda=coda)
table = doc.get_table("Temperaturas")
celda1 = Cell(column='c-77h06AtH4R', value_storage= location)
celda2 = Cell(column='c-b_7VlkcHlZ', value_storage= description)
celda3 = Cell(column='c-orQl3rYoNT', value_storage= temperature)
celda4 = Cell(column='c-oIsDqmPb5H', value_storage= horaformato)
celda5 = Cell(column='c-unFl3Gz49K', value_storage= fechaformato)
table.upsert_rows([[celda1, celda2, celda3, celda4, celda5]])
print (f"La temperatura de {location} ha sido añadida correctamente")