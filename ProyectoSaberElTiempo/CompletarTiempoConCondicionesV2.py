from codaio import Coda, Document, Cell, Row 
import pandas as pd
import datetime
import requests

def actualizar():
    celda1 = Cell(column='c-TGQkNI9AD9', value_storage= location)
    celda2 = Cell(column='c-IXDIhRIpB9', value_storage= description)
    celda3 = Cell(column='c-B_BH0xdaVE', value_storage= temperature)
    celda4 = Cell(column='c-yF5y_9DV0e', value_storage= horaformato)
    celda5 = Cell(column='c-ToyoKzUWnY', value_storage= fechaformato)
    celda6 = Cell(column='c-zZuwi_NyyZ', value_storage= location)
    table.update_row(idprimerafila, [celda2, celda3, celda4, celda5, celda6])

def actualizar2():
    celda1 = Cell(column='c-TGQkNI9AD9', value_storage= location)
    celda2 = Cell(column='c-IXDIhRIpB9', value_storage= description)
    celda3 = Cell(column='c-B_BH0xdaVE', value_storage= temperature)
    celda4 = Cell(column='c-yF5y_9DV0e', value_storage= horaformato)
    celda5 = Cell(column='c-ToyoKzUWnY', value_storage= fechaformato)
    celda6 = Cell(column='c-zZuwi_NyyZ', value_storage= location)
    table.update_row(id_fila, [celda2, celda3, celda4, celda5, celda6])
coda = Coda('c5149980-deb1-4979-952f-f3d49ec5b038')
doc = Document('05ZbXhV8oe', coda=coda)
table = doc.get_table("Temperaturas Completar")
df = pd.DataFrame(table.to_dict())
ultimafila=(df.head(1))
df2 = pd.DataFrame(table.to_dict())
clima= df2["Clima"].values.tolist()

df2 = pd.DataFrame(table.to_dict())
ciudades= df2["Comparacion"].values.tolist()

ultimafila=(df.head(1))
ciudad=ultimafila.loc[ultimafila.index[0], 'Ciudad']
print(ciudad)
print(ciudades)
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

#Encontrar el ID de la primera fila para eliminarla
headers = {'Authorization': 'Bearer c5149980-deb1-4979-952f-f3d49ec5b038'}
uri = f'https://coda.io/apis/v1/docs/05ZbXhV8oe/tables/grid-MArENxYZlC/rows'
res = requests.get(uri, headers=headers)
data = res.json()
idprimerafila= data['items'][0]['id']
fila= table.get_row_by_id(idprimerafila)

if ciudad not in ciudades:
    print("Rellenando los datos de la nueva ciudad")
    actualizar()
else:
    print("Esa ciudad ya esta, la voy a actualizar")
    #Consultamos a coda la informacion de nuestras filas
    headers = {'Authorization': 'Bearer c5149980-deb1-4979-952f-f3d49ec5b038'}
    uri = f'https://coda.io/apis/v1/docs/05ZbXhV8oe/tables/grid-MArENxYZlC/rows'
    res = requests.get(uri, headers=headers)
    informacion = res.json()
    #Hacemos un bucle, que busca en items si algun item tiene el valor de ciudad, y si lo tiene que nos de la id y salir del bucle
    index1= None
    index2= None
    for item in informacion['items']: 
        if item['values']['c-TGQkNI9AD9'] == ciudad:
            if index1 is None:
                index1 = item['index']
            else:
                index2 = item['index']
                break
    print(index1)
    print(index2)
    if index2 < index1:
        id_fila = item['id']
    print(f"El id de fila de la ciudad {ciudad} es {id_fila}") 
    actualizar2()
    print("Eliminado la fila con ciudad repetida")
    fila.delete()  
