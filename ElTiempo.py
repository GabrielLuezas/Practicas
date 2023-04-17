import requests
from codaio import Coda, Document, Cell, Row 

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

print(f'El clima actual en {location} es {description} con una temperatura de {temperature} grados Celsius.')

coda = Coda('c5149980-deb1-4979-952f-f3d49ec5b038')
doc = Document('05ZbXhV8oe', coda=coda)
table = doc.get_table("Temperaturas")
celda1 = Cell(column='c-77h06AtH4R', value_storage= location)
celda2 = Cell(column='c-b_7VlkcHlZ', value_storage= description)
celda3 = Cell(column='c-orQl3rYoNT', value_storage= temperature)
table.upsert_rows([[celda1, celda2, celda3]])
print (f"La temperatura de {location} ha sido añadida correctamente")