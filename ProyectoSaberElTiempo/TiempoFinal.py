import pandas as pd
from codaio import Coda, Document, Cell, Row 
import requests
import time
import datetime

def actualizar2():
    celda1 = Cell(column='c-TGQkNI9AD9', value_storage= location)
    celda2 = Cell(column='c-IXDIhRIpB9', value_storage= description)
    celda3 = Cell(column='c-B_BH0xdaVE', value_storage= temperature)
    celda4 = Cell(column='c-yF5y_9DV0e', value_storage= horaformato)
    celda5 = Cell(column='c-ToyoKzUWnY', value_storage= fechaformato)
    celda6 = Cell(column='c-zZuwi_NyyZ', value_storage= location)
    table.update_row(id_fila, [celda2, celda3, celda4, celda5, celda6])

headers = {'Authorization': 'Bearer c5149980-deb1-4979-952f-f3d49ec5b038'}
uri = f'https://coda.io/apis/v1/docs/05ZbXhV8oe/tables/grid-MArENxYZlC/rows'
res = requests.get(uri, headers=headers)
data = res.json()

coda = Coda('c5149980-deb1-4979-952f-f3d49ec5b038')
doc = Document('05ZbXhV8oe', coda=coda)
table = doc.get_table("Temperaturas Completar")

df= pd.DataFrame(table.to_dict())
ciudades= df["Ciudad"].values.tolist()
print (ciudades)

for ciudad in ciudades:
    if ciudades.count(ciudad) > 1:
        print(f"La ciudad duplicada es {ciudad}")
        valor = "verdadero"
        break
    else:
        valor = "falso"
        break
params = {
  'access_key': 'a69243c437bb7176dc4e097d14ae1869',
  'query': ciudad
}
headers = {'Authorization': 'Bearer c5149980-deb1-4979-952f-f3d49ec5b038'}
uri = f'https://coda.io/apis/v1/docs/05ZbXhV8oe/tables/grid-MArENxYZlC/rows'
res = requests.get(uri, headers=headers)
data = res.json()
idprimerafila= data['items'][0]['id']
api_result = requests.get('http://api.weatherstack.com/current', params)
#Clima, temperatura
data2 = api_result.json()
location = data2['location']['name']
temperature = data2['current']['temperature']
description = data2['current']['weather_descriptions'][0]
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

if valor == "falso":
    for item in data['items']: 
        if item['values']["c-zZuwi_NyyZ"] == "":
            id_fila = item['id']
            ciudad = item['values']['c-TGQkNI9AD9']
            break
    print(f"El id de de la fila con la ciudad {ciudad} es {id_fila}") 
    print("Rellenando los datos de la nueva ciudad")
    actualizar2()
else:
    print("Hay una ciudad repetida")
    for item in data['items']: 
        if item['name'] == ciudad:
            id_fila = item['id']
            break
    print(f"El id de una de las filas con la ciudad {ciudad} es {id_fila}") 
    fila= table.get_row_by_id(id_fila)
    fila.delete()
    print ("La fila ha sido eliminada correctamente")

    time.sleep(15)
    res = requests.get(uri, headers=headers)
    data = res.json()

    for item in data['items']: 
        if item['name'] == ciudad:
            id_fila = item['id']
            print(f"El id de fila de la ciudad {ciudad} es {id_fila}") 
            break
    print("Rellenando los datos de la nueva ciudad")
    actualizar2()