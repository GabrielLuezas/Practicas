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
print(ultimafila)
print(ciudad)
#Encontrar el ID de la primera fila
headers = {'Authorization': 'Bearer c5149980-deb1-4979-952f-f3d49ec5b038'}
uri = f'https://coda.io/apis/v1/docs/05ZbXhV8oe/tables/grid-MArENxYZlC/rows'
res = requests.get(uri, headers=headers)
print(res)
data = res.json()
idprimerafila= data['items'][0]['id']
print(idprimerafila)


params = {
  'access_key': '915c29147962800727053090855eed9f',
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
print(f'El clima actual en {location} es {description} con una temperatura de {temperature} grados Celsius a las {horaformato} el {fechaformato}')

celda1 = Cell(column='c-TGQkNI9AD9', value_storage= location)
celda2 = Cell(column='c-IXDIhRIpB9', value_storage= description)
celda3 = Cell(column='c-B_BH0xdaVE', value_storage= temperature)
celda4 = Cell(column='c-yF5y_9DV0e', value_storage= horaformato)
celda5 = Cell(column='c-ToyoKzUWnY', value_storage= fechaformato)
table.update_row(idprimerafila, [celda2, celda3, celda4, celda5])
print (f"La temperatura de {location} ha sido añadida correctamente")

