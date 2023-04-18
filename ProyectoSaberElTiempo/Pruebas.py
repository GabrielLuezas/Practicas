import pandas as pd
from codaio import Coda, Document, Cell, Row 
import requests
import datetime
coda = Coda('c5149980-deb1-4979-952f-f3d49ec5b038')
doc = Document('05ZbXhV8oe', coda=coda)
table = doc.get_table("Temperaturas")

#Conseguir la Ciudad
ciudad = input("Dime una Ciudad: ")
params = {
  'access_key': '9fb25c002a54d299b97223b9503828a0',
  'query': ciudad
}
#Get para conseguir informacion sobre el tiempo
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
#Traduccion de el clima ingles - español 
if description == "Sunny":
    description = ("Soleado")
elif description == "Clear":
    description = ("Despejado")
elif description == "Light rain shower":
    description = ("Lluvia ligera")
elif description == "Patchy light rain":
    description = ("Lluvia ligera irregular")
elif description == "Partly cloudy":
    description = ("Parcialmente nublado")
elif description == "Fog":
  description = ("Neblina")
elif description == "Patchy rain possible":
    description = ("Posible lluvia irregular")
elif description == "Light Rain":
    description = ("Lluvia ligera")
elif description == "Light Rain, Fog":
    description = ("Lluvia ligera con niebla")
elif description == "Haze":
    description = ("Bruma")
elif description == "Light Drizzle":
    description = ("Llovizna ligera")
elif description == "Overcast":
    description = ("Nublado")
elif description == "Rain":
  description = ("Lluvia")
elif description == "Hail":
    description = ("Granizo")
elif description == "Light Snow":
    description = ("Nieve Ligera")
elif description == "Mist":
    description = ("Neblina")
elif description == "Moderate or heavy rain shower":
    description = ("Chubasco de lluvia moderada o fuerte")
elif description == "Patches Of Fog":
    description = ("Parches de niebla")
elif description == "Mist, Haze":
    description = ("Niebla/Neblina")
elif description == "Patchy light rain with thunder":
    description = ("Lluvia ligera irregular con truenos")

#Conseguir la columna Ciudad
df2 = pd.DataFrame(table.to_dict())
ciudades= df2["Ciudad"].values.tolist()

print(ciudades)
#Si ya existe, la fila se actualizara, si no existe crear la fila
if ciudad in ciudades:
    print("La ciudad introducida ya esta en ciudades, voy a actualizar la fila con los nuevos valores")
    print(f'El clima actual en {location} es {description} con una temperatura de {temperature} grados Celsius a las {horaformato} el {fechaformato}')
    #Parte de Coda
    coda = Coda('c5149980-deb1-4979-952f-f3d49ec5b038')
    doc = Document('05ZbXhV8oe', coda=coda)
    table = doc.get_table("Temperaturas")

    
else:
    print("La ciudad introducida no esta en ciudades")
    print(f'El clima actual en {location} es {description} con una temperatura de {temperature} grados Celsius a las {horaformato} el {fechaformato}')
    #Parte de Coda
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
